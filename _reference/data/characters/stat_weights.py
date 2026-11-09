"""Stat values for a leveling page build, level by level (2026-11-09, the character gear planner; user: "looks at my character's level and
optimizes the gear that I'm getting at each level").

    python _reference/data/characters/stat_weights.py <class> --spec "<leveling page spec>" [--fights 1500] [--jobs 8]

For each level, the fight lab runs the page's build (its talents at that level from its order, its tuned rotation, green gear) once as is
and once per stat with `tables.GEAR_BONUS` raised by a step (common random numbers, seeds 3 and 4): the seconds per kill each point saves.
Record `_reference/data/characters/weights/<class>-<rotation>.json`. Fight-lab numbers are a model of the beta; stats the lab does not
model (spell hit and crit from items, resistances, defense) read as 0.
"""
import argparse
import datetime
import json
import multiprocessing
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
DATA = HERE.parent
sys.path[:0] = [str(DATA / "fightlab"), str(DATA / "scorer"), str(DATA)]
import fl_talent_opt as FT  # noqa: E402
import level_guides as LG  # noqa: E402
import run as FR  # noqa: E402
import tables as TB  # noqa: E402

LEVELS = [20, 23, 26, 29, 32, 35, 40, 45, 50, 55, 60]
STEPS = {"intellect": 30, "spirit": 30, "stamina": 30, "spell_power": 15, "armor": 300, "mp5": 10, "wand_dps": 10}   # 2026-11-09: steps of 10 Intellect read noise
CASTER = {"mage", "priest", "warlock"}


def job(a):
    cls, alloc, level, rot, fights, seed, bonus = a
    TB.GEAR_BONUS.clear()
    TB.GEAR_BONUS.update(bonus)
    try:
        o = FR.simulate(cls, alloc, level, rot, fights, seed, 0)
    finally:
        TB.GEAR_BONUS.clear()
    return o["time_per_kill"]


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("cls")
    ap.add_argument("--spec", required=True)
    ap.add_argument("--fights", type=int, default=1500)
    ap.add_argument("--jobs", type=int, default=8)
    a = ap.parse_args()
    b, order, prov, rot = LG.pick(a.cls, a.spec)
    build = {"allocation": b["allocation"], "order": order}
    steps = dict(STEPS) if a.cls in CASTER else {k: v for k, v in STEPS.items() if k != "wand_dps"}
    jobs, keys = [], []
    for L in LEVELS:
        alloc = FR.allocation_at(build, L)
        for st in [None] + list(steps):
            for seed in (3, 4):
                jobs.append((a.cls, alloc, L, rot, a.fights, seed, {} if st is None else {st: steps[st]}))
                keys.append((L, st, seed))
    with multiprocessing.Pool(a.jobs, initializer=FT._init, initargs=("greens",)) as pool:
        res = pool.map(job, jobs, chunksize=1)
    t = dict(zip(keys, res))
    out = {"class": a.cls, "spec": a.spec, "build": b["id"], "rotation": rot, "date": datetime.date.today().isoformat(), "fights": a.fights,
           "seeds": [3, 4], "steps": steps, "unit": "seconds per kill saved per point (negative: slower)", "levels": {}}
    for L in LEVELS:
        base = (t[(L, None, 3)] + t[(L, None, 4)]) / 2
        row = {"time_per_kill": round(base, 3), "weights": {}}
        for st, step in steps.items():
            d = ((t[(L, None, 3)] - t[(L, st, 3)]) + (t[(L, None, 4)] - t[(L, st, 4)])) / 2
            row["weights"][st] = round(d / step, 5)
        out["levels"][str(L)] = row
        print(f"  {L}: {base:.2f} s per kill; " + ", ".join(f"{k} {v:+.4f}" for k, v in row["weights"].items()), flush=True)
    path = HERE / "weights" / f"{a.cls}-{rot}.json"
    path.parent.mkdir(exist_ok=True)
    path.write_text(json.dumps(out, indent=1) + "\n", encoding="utf-8")
    print(f"wrote {path}")


if __name__ == "__main__":
    main()
