"""3b's measurement pass (2026-11-23, the user: "let's try and figure out a way to correctly test things like trinkets or rings or weapons or
even armor and gear that has proc chances, to be able to test them properly against the other gear"; the audit session's item 3b, now:
trinkets, weapons, ranged and relics, rings, necks, backs). Stat weights cannot see a proc or an on-use; the simulator plays them. For each
damage spec's page pick, every item of the class with a modelled proc or on-use effect in a scope slot (effects_inventory.effect_kind; the
True BiS pool, which holds the other lists') is swapped into the spec's True Pre-BiS set, in each slot it fits (both trinket slots, both
rings, main hand and off hand), and raced against that set on common fights (1,000, seed 1, a full raid, the page's pick and entry). The
record is a screen, not a decision: gear_tiers.optimize_set races the screened items again in each make's own set (race_effect_items),
seed 1 then the top three on seed 2, and takes one only when it is ahead there.

    python _reference/data/raidsim/effect_screen.py [classes] [--spec S] [--fights 1000] [--write]   # raidsim/effect-screen/<class>-<spec>.json
"""
import argparse
import datetime
import json
import pathlib
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[2]
sys.path[:0] = [str(HERE), str(HERE.parent)]
import gear_tiers as GT  # noqa: E402
import effects_inventory as EI  # noqa: E402

G, R = GT.G, GT.R
OUT = HERE / "effect-screen"
BATCH = 60


def page_picks(classes):
    r = subprocess.run([sys.executable, str(HERE / "page_stat_weights.py"), "--list", *classes], capture_output=True, text=True, cwd=str(ROOT))
    if r.returncode:
        raise SystemExit(f"effect_screen: the page picks could not be read: {r.stderr[-600:]}")
    return [(c, s, b["id"], e) for c, rows in json.loads(r.stdout).items() for s, b, e in rows]


def screen(cls, spec, build, entry_name, repo, db, zones, fights):
    trees = R.load_trees(repo, cls)
    b = {x["id"]: x for x in json.load(open(ROOT / cls / "research/talents/forever/proposed-builds.json", encoding="utf-8"))["builds"]}[build]
    tal = R.talents_string(trees, R.alloc_of(b))
    e = R.SPECS[cls][entry_name]
    bp = GT.SETS / f"{cls}-{GT.SM.slug(spec)}-prebis.gear.json"
    if not bp.exists():
        return {"error": f"no True Pre-BiS set file {bp.name}"}
    base = GT.norm17(json.load(open(bp, encoding="utf-8"))["items"])
    pool = GT.pool_of("bis", zones, repo)
    _, _, greedy = G.class_picker(repo, cls, db, pool)
    skipped = EI.skipped_effects(repo)
    cands = []
    for it in db.values():
        if it["id"] in skipped or not it.get("itemEffects") or EI.effect_kind(it) == "other" or not pool(it):
            continue
        for lab, x in GT.effect_variants(it, base, db, greedy):
            cands.append((it, lab, x))
    rows, res = [], {}
    for i in range(0, len(cands), BATCH):
        part = cands[i:i + BATCH]
        builds = [{"label": "base", "talents": tal, "gear_json": {"items": base}}] + \
                 [{"label": lab, "talents": tal, "gear_json": {"items": x}} for _, lab, x in part]
        out = G.run_bench(repo, G.bench_cfg(e, repo, builds, fights, 1, "raid"), f"screen-{cls}-{GT.SM.slug(spec)}")
        bd = (out.get("base") or {}).get("dps") or 0.0
        for it, lab, x in part:
            d = (out.get(lab) or {}).get("dps") or 0.0
            res[lab] = (it, round(d / bd, 4) if bd else 0.0)
    best = {}
    for lab, (it, sc) in res.items():
        if it["id"] not in best or sc > best[it["id"]]["score"]:
            best[it["id"]] = {"id": it["id"], "name": it.get("name"), "group": EI.group_of(int(lab.split("@")[1])), "slot": int(lab.split("@")[1]),
                              "kind": EI.effect_kind(it), "score": sc}
    rows = sorted(best.values(), key=lambda r: -r["score"])
    return {"class": cls, "spec": spec, "build": build, "entry": entry_name, "base": bp.relative_to(ROOT).as_posix(), "fights": fights, "seed": 1,
            "setting": "raid", "candidates": len(cands), "items": len(rows), "rows": rows}


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("classes", nargs="*")
    ap.add_argument("--spec", action="append")
    ap.add_argument("--fights", type=int, default=1000)
    ap.add_argument("--write", action="store_true")
    a = ap.parse_args()
    R.set_game("forever")
    repo = R.repo_path(argparse.Namespace(repo=None))
    db, zones = GT.load_db(repo)
    commit = R.git_commit(repo)
    classes = a.classes or EI.CLASSES
    for cls, spec, build, entry in page_picks(classes):
        if a.spec and spec not in a.spec:
            continue
        r = screen(cls, spec, build, entry, repo, db, zones, a.fights)
        r.update(date=datetime.date.today().isoformat(), commit=commit)
        top = ", ".join(f"{x['name']} {x['score']:.4f}" for x in (r.get("rows") or [])[:5])
        print(f"{cls} {spec} ({build}): {r.get('candidates')} swaps, {r.get('items')} items; best {top}" if "rows" in r else f"{cls} {spec}: {r['error']}",
              flush=True)
        if a.write and "rows" in r:
            OUT.mkdir(exist_ok=True)
            (OUT / f"{cls}-{GT.SM.slug(spec)}.json").write_text(json.dumps(r, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
