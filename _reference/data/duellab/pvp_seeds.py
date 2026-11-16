"""Seed builds for the PvP search from the TBC and WotLK PvP builds (2026-11-15, user: "searched PvP builds from past Expansion, mainly
Classic, TBC, and WotLK, and found what talents were taken in those builds and apply them to our builds"; _reference/pvp-plan.md step 4).

Per class and talent tree:
- the expansions' PvP builds of that spec (_reference/data/pvp-expansion-builds.json). A build counts for the tree its spec label
  names first ("Restoration (Balance dip)" -> Restoration, "Arcane/Fire hybrid" -> Arcane);
- their consensus: the talents at least half of them take, under Forever's names. The mapping's note names a renamed or merged talent
  ("As Arcane Resilience (its Classic name)", "Merged into Weaponmaster"), and a talent Forever lacks is left out. Two expansion
  talents that map onto one Forever talent count once per build. Each is taken at the median rank of the builds that take it, capped
  at Forever's;
- the seed: our PvP build of the tree with every consensus talent it lacks added, shallowest row first. Each added point is taken
  back from a talent outside the consensus, where the stats model's PvP score loses least (popular_swaps.make_swap's rule), every
  state legal. A talent that cannot be added legally is listed as skipped.

The seeds start the duel-lab search (pvp_search.py) next to our build and the community's; a consensus talent the winner skips is
evidence to race, not a rule (those builds were shaped by arenas and resilience, which Forever lacks).

    python _reference/data/duellab/pvp_seeds.py [classes] [--write]      # duellab/seeds/<class>-<tree slug>.json
"""
import argparse
import collections
import json
import pathlib
import re
import statistics
import sys

HERE = pathlib.Path(__file__).resolve().parent
DATA = HERE.parent
ROOT = DATA.parents[1]
sys.path[:0] = [str(DATA / "scorer"), str(DATA)]
import validate_builds as vb  # noqa: E402

SEEDS = HERE / "seeds"
RENAMED = re.compile(r"^(?:As|Merged into) ([A-Z][^(:.,;]*?)\s*(?:\(|:|,|\.|;|$)")


def slug(s):
    return "".join(c for c in s.lower().replace(" ", "-") if c.isalnum() or c == "-")


def label_tree(label, trees):
    first = label.split(" (")[0].split("/")[0].replace(" hybrid", "").strip()
    return first if first in trees else None


def forever_name(talent, mapping, names):
    """The Forever talent an expansion talent counts as: the note's "As X" / "Merged into X" first (the expansions' Lightning Mastery
    is Forever's Elemental Alacrity; Forever's own Lightning Mastery is another talent), none for "Forever: different effect"
    (Winter's Chill, Shadow and Flame: the same name on another talent is no evidence), else the same name."""
    if not mapping.get("in_forever"):
        return None
    note = mapping.get("note") or ""
    m = RENAMED.match(note)
    if m and m.group(1).strip() in names:
        return m.group(1).strip()
    if note.startswith("Forever: different effect"):
        return None
    return talent if talent in names else None


def consensus(cls, tree, trees):
    """([(talent, rank, builds taking it)], number of builds) for the tree, from the TBC and WotLK PvP builds."""
    d = json.load(open(DATA / "pvp-expansion-builds.json", encoding="utf-8"))["classes"][cls]
    names = {n: t for tr in trees.values() for n, t in tr["talents"].items()}
    builds = [b for exp in ("tbc", "wotlk") for b in d.get(exp, []) if label_tree(b["spec"], trees) == tree]
    count, ranks = collections.Counter(), collections.defaultdict(list)
    for b in builds:
        took = {}
        for t, r in b["talents"].items():
            n = forever_name(t, b["forever"].get(t, {}), names)
            if n and r:
                took[n] = max(took.get(n, 0), r)
        for n, r in took.items():
            count[n] += 1
            ranks[n].append(r)
    need = (len(builds) + 1) // 2
    out = [(n, min(names[n]["max"], max(1, round(statistics.median(ranks[n])))), c) for n, c in count.items() if builds and c >= need]
    return sorted(out, key=lambda x: (-x[2], int(names[x[0]]["row"]), x[0])), len(builds)


def legal(trees, al):
    state = {t: {n: r for n, r in al.items() if n in tr["talents"] and r} for t, tr in trees.items()}
    errs = []
    vb.check_state(trees, state, "x", errs)
    return not errs


def seed(cls, b, tree, trees, opt):
    """The seed build for one of our PvP builds, or None when the expansions have no build of the tree."""
    cons, nb = consensus(cls, tree, trees)
    if not cons:
        return None
    al = {n: r for items in b["allocation"].values() for n, r in items if r}
    keep = {n for n, _, _ in cons}
    added, removed = [], collections.Counter()
    todo = list(cons)
    for _pass in (1, 2):   # the most-taken first; a second pass for what the first could not place (tier points added since)
        left = []
        for n, rank, c in todo:
            need = rank - al.get(n, 0)
            if need <= 0:
                continue
            trial = dict(al)
            trial[n] = rank
            took = collections.Counter()
            for _ in range(need):
                best = None
                for m, r in trial.items():
                    if m in keep or not r:
                        continue
                    t2 = dict(trial)
                    t2[m] -= 1
                    if not legal(trees, t2):
                        continue
                    v = opt.score(trial, 60) - opt.score(t2, 60)
                    if best is None or v < best[0]:
                        best = (v, m)
                if best is None:
                    break
                trial[best[1]] -= 1
                took[best[1]] += 1
            if sum(took.values()) < need or not legal(trees, trial):
                left.append((n, rank, c))
                continue
            al = trial
            added.append(f"{n} {rank}")
            removed.update(took)
        todo = left
    skipped = [f"{n} {rank} ({c} of {nb}): no legal way to take its points back outside the consensus" for n, rank, c in todo]
    alloc = {t: [[n, al[n]] for n in tr["talents"] if al.get(n)] for t, tr in trees.items()}
    assert sum(al.values()) == sum(r for items in b["allocation"].values() for _, r in items), (cls, tree)
    return {"id": f"expansion-seed-{slug(tree)}", "class": cls, "tree": tree, "from": b["id"], "expansion_builds": nb,
            "consensus": [{"talent": n, "rank": r, "builds": c} for n, r, c in cons], "added": added,
            "removed": dict(removed), "skipped": skipped, "split": "/".join(str(sum(r for _, r in alloc[t])) for t in trees),
            "allocation": alloc}


def our_pvp(cls, trees):
    """{tree: our PvP build of that tree}: the build whose spec field names the tree, else the first that leads in it."""
    data = json.load(open(ROOT / cls / "research/talents/forever/proposed-builds.json", encoding="utf-8"))
    out = {}
    for b in data["builds"]:
        if b.get("content") != "pvp":
            continue
        pts = {t: sum(r for _, r in v) for t, v in b["allocation"].items()}
        lead = b.get("spec") if b.get("spec") in trees else max(pts, key=pts.get)
        if lead not in out or b.get("spec") == lead:
            out[lead] = b
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("classes", nargs="*")
    ap.add_argument("--write", action="store_true")
    a = ap.parse_args()
    from optimize import Optimizer
    import scenario_audit as sa
    F = vb.load_forever()
    for cls in sorted(F):
        if a.classes and cls not in a.classes:
            continue
        trees = F[cls]
        models = list(json.load(open(DATA / "scorer/specs" / f"{cls}.json", encoding="utf-8"))["models"])
        for tree, b in sorted(our_pvp(cls, trees).items()):
            model, profile = sa.model_profile(cls, b, models)
            scored_with = f"{model}, {profile}"
            if not model:   # a tree without a stats model (Arcane mage, Protection warrior): the class's first model's PvP profile
                model, profile = models[0], "pvp"
                scored_with = f"{model}, {profile} (borrowed: the tree has no stats model)"
            s = seed(cls, b, tree, trees, Optimizer("forever", cls, model, profile))
            if s is None:
                print(f"{cls} {tree}: no expansion build of this tree")
                continue
            s["scored_with"] = scored_with
            print(f"{cls} {tree} ({s['expansion_builds']} builds): {b['id']} -> {s['split']}; added "
                  f"{', '.join(s['added']) or 'nothing'}; removed {', '.join(f'{k} {v}' for k, v in s['removed'].items()) or 'nothing'}"
                  + (f"; skipped {'; '.join(s['skipped'])}" if s["skipped"] else ""))
            if a.write:
                SEEDS.mkdir(exist_ok=True)
                with open(SEEDS / f"{cls}-{slug(tree)}.json", "w", encoding="utf-8", newline="\n") as fh:
                    fh.write(json.dumps(s, indent=1, ensure_ascii=False) + "\n")


if __name__ == "__main__":
    main()
