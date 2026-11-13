"""The leveling ranking in Forever's own gear (2026-11-13; user: "since our stats versus something like Pawns make the specs that use spell
damage ... a lot better, is that going to change the tier list DPS ranking heavily?").

    python -u _reference/data/characters/forever_race.py [--fights 3000] [--jobs 6]   -> characters/weights/forever-race.json

The leveling pages rank each spec's pick by the fight lab's level-weighted time per kill (weights level / 10) in the lab's standard gear:
Classic 1.12's fixed-stat greens (fightlab/gear_stats.py), which leave out the random-suffix greens that carry most of a Forever caster's
Spell Power. This races every leveling page pick at levels 20-60 in two Forever sets from forever_base.py: "typical" (per slot the
median of the better half, each item at a suffix the build keeps) and "best" (the best set the level offers, greens and blues). The
standard gear's times are the measurement files' base runs (weights/leveling/, seeds 3 and 4); the Forever sets run on the same seeds.
Each set is a GEAR_BONUS over the standard gear (hit and expertise left out). Fight-lab numbers are a model of the beta.
"""
import argparse
import datetime
import json
import multiprocessing
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
DATA = HERE.parent
sys.path[:0] = [str(HERE), str(DATA / "fightlab"), str(DATA / "scorer"), str(DATA)]
LEVELS = [20, 25, 30, 35, 40, 45, 50, 55, 60]
CLASSES = "druid hunter mage paladin priest rogue shaman warlock warrior".split()


def weighted(per):
    """The pages' level weighting (render_modes.weighted): weights level / 10."""
    tot = sum(L / 10 for L in per)
    return sum(t * L / 10 for L, t in per.items()) / tot


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--fights", type=int, default=3000)
    ap.add_argument("--jobs", type=int, default=6)
    a = ap.parse_args()
    import fl_talent_opt as FT
    import level_guides as LG
    import run as FR
    import stat_weights as SW
    base = json.loads((HERE / "weights" / "forever-base.json").read_text(encoding="utf-8"))["builds"]
    SA = LG.fightlab_signature_audit()
    picks, jobs, keys = [], [], []
    for cls in CLASSES:
        for slot in SA.page_slots(cls):
            if not slot[1]:
                continue
            spec, b = slot[0], slot[1][0]
            _, order, _, rot = LG.pick(cls, spec)
            key = f"{cls}-{b['id']}"
            picks.append((cls, spec, b["id"], key))
            for L in LEVELS:
                alloc = FR.allocation_at({"allocation": b["allocation"], "order": order}, L)
                row = base[key][str(L)]
                for which, bonus in (("typical", row["bonus"]), ("best", row["best"]["bonus"])):
                    for seed in (3, 4):
                        jobs.append((cls, alloc, L, rot, a.fights, seed, bonus))
                        keys.append((key, L, which, seed))
    with multiprocessing.Pool(a.jobs, initializer=FT._init, initargs=("greens",)) as pool:
        res = dict(zip(keys, pool.map(SW.job, jobs, chunksize=1)))
    out = {"date": datetime.date.today().isoformat(), "fights": a.fights, "seeds": [3, 4], "levels": LEVELS, "builds": {}}
    for cls, spec, bid, key in picks:
        w = json.loads((HERE / "weights" / "leveling" / f"{key}.json").read_text(encoding="utf-8"))
        row = {"class": cls, "spec": spec, "build": bid}
        for which in ("standard", "typical", "best"):
            per = {}
            for L in LEVELS:
                if which == "standard":
                    per[L] = w["levels"][str(L)]["time_per_kill"]
                else:
                    per[L] = (res[(key, L, which, 3)] + res[(key, L, which, 4)]) / 2
            row[which] = {"weighted": round(weighted(per), 3), "by_level": {str(L): round(t, 3) for L, t in per.items()}}
        out["builds"][key] = row
    for which in ("standard", "typical", "best"):   # ranks: within the class, and over every pick
        allb = sorted(out["builds"].values(), key=lambda r: r[which]["weighted"])
        for i, r in enumerate(allb):
            r[which]["rank_all"] = i + 1
        for cls in CLASSES:
            cb = sorted((r for r in out["builds"].values() if r["class"] == cls), key=lambda r: r[which]["weighted"])
            for i, r in enumerate(cb):
                r[which]["rank_class"] = i + 1
    (HERE / "weights" / "forever-race.json").write_text(json.dumps(out, indent=1) + "\n", encoding="utf-8", newline="\n")
    print(f"{'build':44s} {'standard':>9s} {'typical':>9s} {'best':>9s}   overall rank std/typ/best   class rank std/typ/best")
    for r in sorted(out["builds"].values(), key=lambda r: r["standard"]["rank_all"]):
        print(f"{r['class'] + ' ' + r['spec']:44.44s} {r['standard']['weighted']:9.2f} {r['typical']['weighted']:9.2f} {r['best']['weighted']:9.2f}   "
              f"{r['standard']['rank_all']:3d} {r['typical']['rank_all']:3d} {r['best']['rank_all']:3d}            "
              f"{r['standard']['rank_class']} {r['typical']['rank_class']} {r['best']['rank_class']}", flush=True)


if __name__ == "__main__":
    main()
