"""Give leveling builds without a talent order one (2026-10-15, page audit C1).

    python _reference/data/order_repair.py [classes] [--fights 3000] [--jobs 6] [--write]

The 2026-10-03 repair of the builds the 70170 trees broke rewrote allocations and dropped the `order` of nine leveling builds (warrior
Arms and Fury optimizer builds and `leveling-arms`, druid `leveling-feral` and `opt-feral-cat-dps-leveling-st`, mage Fire...). The fight
lab plays a build without an order with all 51 points from level 10 (`run.allocation_at`), so those builds read 5-10% fast at low levels
and beat builds raced with orders on the pages. This keeps each allocation and races three orders to it, the way raid_path_leveling.py
does for the healer and tank trees: the stats model's leveling order (Optimizer.order under the build's scorer model and profile),
own tree first, own tree last (moving whole trees keeps every tier legal); the fight lab plays each at levels 20-60 (the build's leveling
rotation, seed 3, --fights per level), the fastest by level-weighted time per kill is written with `order_label` and a note.
Skipped: builds with `raid_path` (raid_path_leveling.py writes those), solo builds (level 60, no order) and AoE builds (`-leveling-aoe`,
which get the stats model's order under their own profile without a race: the race plays single mobs).
"""
import argparse
import datetime
import json
import multiprocessing
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path[:0] = [str(HERE / "fightlab"), str(HERE / "scorer"), str(HERE)]
import run as FR  # noqa: E402  (fightlab/run.py)
import paths  # noqa: E402
import spec_modes as SM  # noqa: E402
import derive_leveling as DL  # noqa: E402
import raid_path_leveling as RP  # noqa: E402
from fmt_json import dumps  # noqa: E402

TODAY = datetime.date.today().isoformat()
CLASSES = ["druid", "hunter", "mage", "paladin", "priest", "rogue", "shaman", "warlock", "warrior"]


def models(cls, b, tree):
    """(fight-lab rotation, scorer model, profile) for a build: an optimizer build names its model and profile in its id."""
    spec, model = DL.LEVEL[(cls, tree)]
    profile = "leveling-st"
    if b["id"].startswith("opt-"):
        m = FR.spec_of_build(cls, b["id"], None)
        if m:
            spec = model = m
            profile = b["id"][4 + len(m) + 1:]
    return spec, model, profile


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("classes", nargs="*")
    ap.add_argument("--fights", type=int, default=3000)
    ap.add_argument("--jobs", type=int, default=6)
    ap.add_argument("--write", action="store_true")
    a = ap.parse_args()
    from optimize import Optimizer
    FR.apply_gear("greens")
    pool = multiprocessing.Pool(a.jobs)
    for cls in a.classes or CLASSES:
        bp = paths.builds_json("forever", cls)
        data = json.load(open(bp, encoding="utf-8"))
        changed = False
        for b in data["builds"]:
            if b.get("content") != "leveling" or b.get("order") or b.get("raid_path"):
                continue
            tree = SM.spec_of(cls, b)
            spec, model, profile = models(cls, b, tree)
            flat = {n: r for items in b["allocation"].values() for n, r in items if r}
            opt = Optimizer("forever", cls, model, profile)
            steps = opt.order(flat, lookahead=DL.SB.LOOKAHEAD.get(cls, 16))
            scorer = [{"levels": lv, "tree": t, "talent": n, "points": p} for lv, t, n, p in opt.compress_order(steps)]
            split = "/".join(str(sum(r for _, r in v)) for v in b["allocation"].values())
            if profile != "leveling-st":
                print(f"== {cls} {b['id']} ({split}): {profile}, the stats model's order without a race", flush=True)
                b["order"], b["order_label"] = scorer, "stats model"
                b.setdefault("notes", []).append(f"{TODAY} (order_repair.py, page audit C1): the order lost in the 2026-10-03 repair is the "
                                                 f"stats model's {profile} order (not raced: the race plays single mobs).")
                changed = True
                continue
            pts = RP.expand(scorer)
            orders = {"stats model": scorer,
                      "own tree first": RP.compress([p for p in pts if p[0] == tree] + [p for p in pts if p[0] != tree]),
                      "own tree last": RP.compress([p for p in pts if p[0] != tree] + [p for p in pts if p[0] == tree])}
            res = {}
            for name, order in orders.items():
                ob = {"allocation": b["allocation"], "order": order}
                times = pool.map(RP._run, [(cls, spec, FR.allocation_at(ob, L), L, a.fights) for L in RP.LEVELS])
                res[name] = dict(zip(RP.LEVELS, times))
            full = pool.map(RP._run, [(cls, spec, flat, L, a.fights) for L in RP.LEVELS])
            best = min(res, key=lambda k: RP.weighted(res[k]))
            print(f"== {cls} {b['id']} ({split}, {spec}): " + ", ".join(f"{k} {RP.weighted(v):.2f}s" for k, v in res.items())
                  + f" -> {best}; without an order (51 points from level 10) {RP.weighted(dict(zip(RP.LEVELS, full))):.2f}s", flush=True)
            b["order"], b["order_label"] = orders[best], best
            others = "; ".join(f"{k} {RP.weighted(v):.1f} s" for k, v in res.items() if k != best)
            b.setdefault("notes", []).append(
                f"{TODAY} (order_repair.py, page audit C1): the order lost in the 2026-10-03 repair is the fastest of three the fight lab "
                f"raced (the {spec} rotation, seed 3, {a.fights} fights per level, levels 20-60 weighted by level): {best} "
                f"{RP.weighted(res[best]):.1f} s per kill; {others}.")
            changed = True
        if changed and a.write:
            bp.write_text(dumps(data) + "\n", encoding="utf-8")
            print(f"wrote {bp}", flush=True)


if __name__ == "__main__":
    main()
