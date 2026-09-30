"""Healer and tank specs level straight into their raid build (2026-09-30, user decision: "the healer and tank leveling order should
really just be what the raid specs are for those and then just deciding what the leveling order to get the best raid builds for each
spec at 60").

    python _reference/data/raid_path_leveling.py [classes] [--fights 3000] [--write]

For every healing or tanking tree (spec_modes.LEVEL_AS: Holy and Discipline priest, Holy and Protection paladin, Protection warrior,
Restoration shaman and druid):
1. The target is the spec's raid pick at 60, as the raid page shows it (render_modes.rank_builds: healers by healing capacity, tanks
   by tank value).
2. Three orders to it: the stats model's leveling order (Optimizer.order under the spec's leveling model, derive_leveling.LEVEL, the
   way every leveling build gets its order), "own tree first" (every point in the spec's tree before the others) and "own tree last".
   Talent tiers only count points spent in the same tree, so moving whole trees earlier or later while each tree keeps its own
   sequence is always legal.
3. The fight lab plays each order at levels 20-60 (the spec's leveling rotation, seed 3, --fights per level); the fastest by
   level-weighted time per kill is the spec's leveling build. The other two orders' times stay in the record and on the page.
Writes `<tree>-leveling` (derived: leveling, `raid_path`: the raid build's id) into proposed-builds.json and the numbers into
`_reference/data/derived-leveling.json` (the record render_modes reads), replacing the earlier derivation for these trees.
"""
import argparse
import datetime
import json
import multiprocessing
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[1]
sys.path[:0] = [str(HERE / "fightlab"), str(HERE / "scorer"), str(HERE)]
import run as FR  # noqa: E402  (fightlab/run.py)
import paths  # noqa: E402
import spec_modes as SM  # noqa: E402
import derive_leveling as DL  # noqa: E402
from fmt_json import dumps  # noqa: E402

LEVELS = [20, 30, 40, 50, 60]
TODAY = datetime.date.today().isoformat()


def expand(order):
    """Compressed order -> [(tree, talent)] one entry per point."""
    return [(s["tree"], s["talent"]) for s in order for _ in range(s["points"])]


def compress(points, start=10):
    out = []
    for i, (tree, name) in enumerate(points):
        lv = start + i
        if out and out[-1]["talent"] == name:
            out[-1]["points"] += 1
            out[-1]["levels"] = f"{out[-1]['levels'].split('-')[0]}-{lv}"
        else:
            out.append({"levels": str(lv), "tree": tree, "talent": name, "points": 1})
    return out


def _run(job):
    cls, spec, alloc, level, fights = job
    return FR.simulate(cls, alloc, level, spec, fights, 3, 0)["time_per_kill"]


def weighted(per):
    tot = sum(L / 10 for L in per)
    return sum(v * L / 10 for L, v in per.items()) / tot


def raid_pick(cls, tree):
    import render_modes as RM
    builds = json.load(open(paths.builds_json("forever", cls), encoding="utf-8"))["builds"]
    nums = (RM.raid_numbers(cls), RM.leveling_numbers(cls), RM.healer_numbers(cls))
    ranked = RM.rank_builds(cls, "raid", SM.grid(cls, builds)[tree]["raid"], nums)
    role = "healer" if tree in SM.HEAL_TREES.get(cls, ()) else "tank"
    ranked = [b for b in ranked if b.get("role") == role] or ranked
    return ranked[0] if ranked else None


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("classes", nargs="*")
    ap.add_argument("--fights", type=int, default=3000)
    ap.add_argument("--jobs", type=int, default=4)
    ap.add_argument("--write", action="store_true")
    a = ap.parse_args()
    from optimize import Optimizer
    FR.apply_gear("greens")
    rec = json.load(open(DL.OUT, encoding="utf-8")) if DL.OUT.exists() else {}
    pool = multiprocessing.Pool(a.jobs)
    for (cls, tree), _other in sorted(SM.LEVEL_AS.items()):
        if a.classes and cls not in a.classes:
            continue
        spec, model = DL.LEVEL[(cls, tree)]
        target = raid_pick(cls, tree)
        if not target:
            print(f"== {cls} {tree}: no raid build", flush=True)
            continue
        flat = {n: r for items in target["allocation"].values() for n, r in items if r}
        opt = Optimizer("forever", cls, model, "leveling-st")
        steps = opt.order(flat, lookahead=DL.SB.LOOKAHEAD.get(cls, 16))
        scorer = [{"levels": lv, "tree": t, "talent": n, "points": p} for lv, t, n, p in opt.compress_order(steps)]
        pts = expand(scorer)
        orders = {"stats model's order": scorer,
                  "own tree first": compress([p for p in pts if p[0] == tree] + [p for p in pts if p[0] != tree]),
                  "own tree last": compress([p for p in pts if p[0] != tree] + [p for p in pts if p[0] == tree])}
        res = {}
        for name, order in orders.items():
            b = {"allocation": target["allocation"], "order": order}
            times = pool.map(_run, [(cls, spec, FR.allocation_at(b, L), L, a.fights) for L in LEVELS])
            res[name] = {L: t for L, t in zip(LEVELS, times)}
        best = min(res, key=lambda k: weighted(res[k]))
        first = next(int(s["levels"].split("-")[0]) for s in orders[best] if s["tree"] == tree)
        print(f"== {cls} {tree}: raid build {target['id']} ({'/'.join(str(sum(r for _, r in v)) for v in target['allocation'].values())}); "
              + ", ".join(f"{k} {weighted(v):.1f}s" for k, v in res.items()) + f" -> {best} (first {tree} point at {first})", flush=True)
        r = rec.setdefault(cls, {}).setdefault(tree, {})
        r.update({"spec": spec, "model": model, "tree": tree, "date": TODAY, "verdict": "new", "raid_path": target["id"], "order_kind": best,
                  "orders": {k: {"weighted": weighted(v), "levels": v} for k, v in res.items()}, "levels": {str(L): t for L, t in res[best].items()},
                  "keep_incumbent": False})
        if not a.write:
            continue
        bp = paths.builds_json("forever", cls)
        data = json.load(open(bp, encoding="utf-8"))
        bid = f"{SM.slug(tree)}-leveling"
        others = "; ".join(f"{k} {weighted(v):.0f} s" for k, v in res.items() if k != best)
        b = {"id": bid, "name": f"{tree} — Leveling into the raid build", "role": "dps", "content": "leveling", "tier": "draft", "spec": tree,
             "generated": TODAY, "derived": "leveling", "raid_path": target["id"],
             "summary": (f"Level with the talents of the {tree} raid build ({target['id']}) so you arrive at 60 ready to "
                         f"{'heal' if tree in SM.HEAL_TREES.get(cls, ()) else 'tank'}; the order is the fastest of three the fight lab raced "
                         f"({best}: {weighted(res[best]):.0f} s per kill over levels 20-60, the {spec} rotation)."),
             "allocation": target["allocation"], "order": orders[best], "core": target.get("core", []), "flex": [],
             "notes": [f"{TODAY} (raid_path_leveling.py, user decision): healer and tank specs level into their raid build. Orders raced "
                       f"(fight lab, seed 3, {a.fights} fights per level, level-weighted): {best} {weighted(res[best]):.0f} s; {others}. "
                       f"First {tree} point at level {first}.",
                       "Fight-lab numbers are a model of the beta, not in-game measurements."],
             "open_questions": [f"Check the {tree} leveling pace at launch; the raid build's talents may cost speed early."],
             "sources": target.get("sources", [])}
        data["builds"] = [x for x in data["builds"] if x["id"] != bid]
        data["builds"].append(b)
        bp.write_text(dumps(data) + "\n", encoding="utf-8")
    if a.write:
        DL.OUT.write_text(json.dumps(rec, indent=1) + "\n", encoding="utf-8")
        print(f"wrote {DL.OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
