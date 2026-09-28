"""Validate talent builds against the real tree data.

Usage (from the project root):
    python _reference/data/validate_builds.py            # validate everything
    python _reference/data/validate_builds.py warrior    # one class

Checks, for every build in <class>/talents/classic-baseline/builds.json
(against Classic Era data) and <class>/talents/forever/proposed-builds.json
(against the Forever beta-client snapshot):

  * every talent exists in the named tree
  * points never exceed the talent's max rank
  * tier gating: a talent in tier N needs 5*(N-1) points in that tree below it
  * prerequisites (arrows) are satisfied
  * total points == 51 (or `"max_level"` - 9 when a build declares one)
  * leveling builds: the `order` is simulated level by level, and its end state
    must equal the allocation

For Classic builds it also writes <class>/talents/forever/baseline-audit.md:
talent-by-talent, what happened to each point of the Classic build in Forever
(unchanged / changed / moved / removed).

Exit code 1 if any build fails.
"""
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
DATA = ROOT / "_reference" / "data"
CLASSES = ["warrior", "paladin", "hunter", "rogue", "priest", "shaman", "mage", "warlock", "druid"]
TOTAL_POINTS = 51


# ---------------------------------------------------------------- tree loading

def load_classic():
    raw = json.load(open(DATA / "classic-era-talents.json", encoding="utf-8"))["classes"]
    out = {}
    for cls, c in raw.items():
        trees = {}
        for tr in c["trees"]:
            talents = {}
            id2name = {t["id"]: t["name"] for t in tr["talents"]}
            for t in tr["talents"]:
                talents[t["name"]] = {
                    "row": t["row"],
                    "max": t["maxRank"],
                    "requires": [(id2name[q["talent"]], q["rank"]) for q in t.get("requires", [])],
                    "ranks": t.get("ranks", []),
                }
            trees[tr["name"]] = {"talents": talents, "order": tr.get("order", 0)}
        out[cls] = trees
    return out


def load_forever():
    out = {}
    for cls in CLASSES:
        d = json.load(open(DATA / "forever-talents" / f"{cls}.json", encoding="utf-8"))
        trees = {}
        for tr in d["trees"]:
            talents = {}
            id2name = {t["id"]: t["name"] for t in tr["talents"]}
            for t in tr["talents"]:
                req = []
                if t.get("prereq"):
                    p = t["prereq"]
                    req.append((id2name.get(p["id"], p["id"]), p.get("rank", 1)))
                talents[t["name"]] = {
                    "row": t["row"],
                    "max": t["maxRank"],
                    "requires": req,
                    "ranks": t.get("ranks", []),
                    "status": t.get("status", "?"),
                    "diff": t.get("diff", []),
                    "estimated": t.get("estimated", []),
                }
            trees[tr["name"]] = {"talents": talents, "removed": tr.get("removed", [])}
        out[cls] = trees
    return out


# ---------------------------------------------------------------- validation

def norm(name: str) -> str:
    return name.lower().replace("’", "'").strip()


def find_talent(tree: dict, name: str):
    for k, v in tree["talents"].items():
        if norm(k) == norm(name):
            return k, v
    return None, None


def check_state(trees: dict, state: dict, ctx: str, errors: list):
    """state: {tree_name: {talent_name: points}} -- verify gating + prereqs + caps."""
    for tname, alloc in state.items():
        tree = trees.get(tname)
        if tree is None:
            errors.append(f"{ctx}: unknown tree '{tname}' (have {list(trees)})")
            continue
        # points per row
        row_pts = {}
        for name, pts in alloc.items():
            key, t = find_talent(tree, name)
            if t is None:
                errors.append(f"{ctx}: '{name}' is not in the {tname} tree")
                continue
            if pts < 0 or pts > t["max"]:
                errors.append(f"{ctx}: {name} has {pts} points, max is {t['max']}")
            row_pts[t["row"]] = row_pts.get(t["row"], 0) + pts
        for name, pts in alloc.items():
            key, t = find_talent(tree, name)
            if t is None or pts == 0:
                continue
            below = sum(p for r, p in row_pts.items() if r < t["row"])
            need = t["row"] * 5
            if below < need:
                errors.append(f"{ctx}: {name} (tier {t['row']+1}) needs {need} points in {tname} below it, only {below}")
            for req_name, req_rank in t["requires"]:
                have = 0
                for n2, p2 in alloc.items():
                    if norm(n2) == norm(req_name):
                        have = p2
                if have < req_rank:
                    errors.append(f"{ctx}: {name} requires {req_name} {req_rank}, have {have}")


def validate_build(trees: dict, build: dict, ctx: str) -> list:
    errors = []
    alloc = {tname: {n: p for n, p in items} for tname, items in build["allocation"].items()}
    # duplicate talent names inside a tree
    for tname, items in build["allocation"].items():
        names = [n for n, _ in items]
        dupes = {n for n in names if names.count(n) > 1}
        if dupes:
            errors.append(f"{ctx}: duplicate entries {sorted(dupes)} in {tname}")
    total = sum(sum(a.values()) for a in alloc.values())
    expected = build.get("max_level", 60) - 9
    if total != expected:
        errors.append(f"{ctx}: {total} points allocated, expected {expected}")
    check_state(trees, alloc, ctx, errors)

    # leveling order simulation
    if "order" in build:
        state = {t: {} for t in alloc}
        level = 9
        for step in build["order"]:
            lv = step["levels"]
            lo, hi = (lv.split("-") + [lv])[:2] if "-" in lv else (lv, lv)
            lo, hi = int(lo), int(hi)
            if lo != level + 1:
                errors.append(f"{ctx}: order step '{lv}' does not follow level {level}")
            if hi - lo + 1 != step["points"]:
                errors.append(f"{ctx}: order step '{lv}' spans {hi-lo+1} levels but gives {step['points']} points")
            level = hi
            tree_state = state.setdefault(step["tree"], {})
            tree_state[step["talent"]] = tree_state.get(step["talent"], 0) + step["points"]
            check_state(trees, state, f"{ctx} @ level {hi}", errors)
        if level != 60:
            errors.append(f"{ctx}: order ends at level {level}, expected 60")
        # end state must equal allocation
        for tname in set(list(alloc) + list(state)):
            a = {norm(k): v for k, v in alloc.get(tname, {}).items() if v}
            s = {norm(k): v for k, v in state.get(tname, {}).items() if v}
            if a != s:
                errors.append(f"{ctx}: order end state for {tname} {s} != allocation {a}")
    # collapse duplicates while keeping first-seen order
    seen = set()
    return [e for e in errors if not (e in seen or seen.add(e))]


def split_string(trees: dict, build: dict) -> str:
    order = sorted(trees, key=lambda t: trees[t].get("order", 0)) if all("order" in v for v in trees.values()) else list(trees)
    return "/".join(str(sum(p for _, p in build["allocation"].get(t, []))) for t in order)


# ---------------------------------------------------------------- forever audit

def forever_status(forever_trees: dict, tree_name: str, talent: str):
    """Return (status, detail) for a Classic talent name looked up in the Forever trees."""
    ft = forever_trees.get(tree_name)
    if ft is None:
        # Forever tree names can differ slightly (e.g. "Shadow Magic"); match loosely
        for k in forever_trees:
            if norm(k).startswith(norm(tree_name)[:6]):
                ft = forever_trees[k]
                tree_name = k
                break
    if ft is None:
        return "unknown", "tree not found"
    key, t = find_talent(ft, talent)
    if t is not None:
        diff = "; ".join(t.get("diff", []))
        return t["status"], f"tier {t['row']+1}, max {t['max']}" + (f" — {diff}" if diff else "")
    for r in ft.get("removed", []):
        rname = r if isinstance(r, str) else r.get("name", "")
        if norm(rname) == norm(talent):
            return "removed", "removed from Classic"
    # maybe it moved to a different tree
    for k, other in forever_trees.items():
        key2, t2 = find_talent(other, talent)
        if t2 is not None:
            return "moved-tree", f"now in {k}, tier {t2['row']+1}"
    return "unknown", "not found in Forever data"


def write_audit(cls: str, builds: dict, classic_trees: dict, forever_trees: dict):
    lines = [f"# {builds['class']} — Classic baseline vs. WoW: Forever (audit)\n",
             "> Generated by `_reference/data/validate_builds.py` from the Classic Era tree data and the "
             "Forever beta-client snapshot (build 1.60.1.70009). For every point in each Classic baseline build: does that talent still "
             "exist in Forever, and did it change? **Orphaned** points (talent removed) must be re-spent; "
             "**changed** talents must be re-evaluated. See `README.md` in this folder for the adaptation notes "
             "and `proposed-builds.json` for the resulting Forever builds.\n"]
    for b in builds["builds"]:
        split = split_string(classic_trees, b)
        lines.append(f"## {b['name']} ({split})\n")
        lines.append("| Tree | Talent | Pts | Forever status | Detail |")
        lines.append("|---|---|---|---|---|")
        orphaned = 0
        changed = 0
        for tname, items in b["allocation"].items():
            for name, pts in items:
                st, detail = forever_status(forever_trees, tname, name)
                if st == "removed":
                    orphaned += pts
                    st_txt = "**REMOVED**"
                elif st in ("changed", "moved", "moved-tree"):
                    changed += pts
                    st_txt = st
                elif st == "same":
                    st_txt = "unchanged"
                else:
                    st_txt = st
                lines.append(f"| {tname} | {name} | {pts} | {st_txt} | {detail} |")
        lines.append("")
        lines.append(f"**Orphaned points to re-spend: {orphaned}.** Points in changed/moved talents to re-evaluate: {changed}.\n")
    out = ROOT / cls / "talents" / "forever" / "baseline-audit.md"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return out


# ---------------------------------------------------------------- main

def main(argv):
    classes = [c for c in CLASSES if not argv or c in argv]
    classic = load_classic()
    forever = load_forever()
    failed = 0
    for cls in classes:
        for game, rel in (("classic-era", "classic-baseline/builds.json"), ("forever", "forever/proposed-builds.json")):
            path = ROOT / cls / "talents" / rel
            if not path.exists():
                continue
            data = json.load(open(path, encoding="utf-8"))
            trees = classic[cls] if game == "classic-era" else forever[cls]
            print(f"== {cls} / {game}: {len(data['builds'])} builds")
            for b in data["builds"]:
                errs = validate_build(trees, b, b["id"])
                split = split_string(trees, b)
                if errs:
                    failed += 1
                    print(f"  FAIL {b['id']} ({split})")
                    for e in errs:
                        print("       -", e)
                else:
                    print(f"  ok   {b['id']} ({split})")
            if game == "classic-era":
                out = write_audit(cls, data, classic[cls], forever[cls])
                print(f"  audit -> {out.relative_to(ROOT)}")
    if failed:
        print(f"\n{failed} build(s) failed validation")
        return 1
    print("\nall builds valid")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
