"""What the Legacy perks are worth to a character's leveling (2026-11-10, user: "work on a Legacy talent build ... Do full research",
then "Yes, both" to measuring the perks like the gear, and "Arcea is most likely my main, and will be the one that I am leveling most of
the time. Tara is my group character").

    python _reference/data/characters/legacy_value.py <character> [--fights 1500] [--jobs 8] [--from <level>]

The fight lab runs the character's leveling page build (its talents at each level from the page's order, its tuned rotation, green gear)
four ways at each level, common random numbers on seeds 3 and 4:
  - as is;
  - Talented 5/5 (talent points from level 5 instead of 10: the talents of five levels later, at most the 51 of the full build);
  - Thrill of Adventure 5/5 (5% of maximum health and mana back after each killing blow; tables.LEGACY_THRILL, given at once);
  - both.
The seconds per kill each saves x the planner's kills per level (plan.kills_per_level) = minutes of killing saved from --from (the
character's level) to 60. Well Rested is not a fight: its worth is the extra rested experience (plan.py's rule, no simulation).
Record `_reference/data/characters/legacy/<character>.json`. Fight-lab numbers are a model of the beta's mechanics, not measurements.
"""
import argparse
import datetime
import json
import multiprocessing
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
DATA = HERE.parent
ROOT = DATA.parent.parent
sys.path[:0] = [str(DATA / "fightlab"), str(DATA / "scorer"), str(DATA), str(HERE)]
import fl_talent_opt as FT  # noqa: E402
import level_guides as LG  # noqa: E402
import run as FR  # noqa: E402
import tables as TB  # noqa: E402

LEVELS = [20, 23, 26, 29, 32, 35, 40, 45, 50, 55, 60]
THRILL = 0.05     # 5 ranks x 1% (the live client's tooltip, build 70888)
TALENTED = 5      # 5 ranks: talent points from level 5


def job(a):
    cls, alloc, level, rot, fights, seed, thrill = a
    TB.LEGACY_THRILL = thrill
    try:
        return FR.simulate(cls, alloc, level, rot, fights, seed, 0)["time_per_kill"]
    finally:
        TB.LEGACY_THRILL = 0.0


def interp(rows, L):
    """A measured value at level L, straight lines between the measured levels."""
    ks = sorted(rows)
    if L <= ks[0]:
        return rows[ks[0]]
    for a, b in zip(ks, ks[1:]):
        if a <= L <= b:
            return rows[a] + (rows[b] - rows[a]) * (L - a) / (b - a)
    return rows[ks[-1]]


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("character")
    ap.add_argument("--fights", type=int, default=1500)
    ap.add_argument("--jobs", type=int, default=8)
    ap.add_argument("--from", dest="start", type=int, default=None)
    a = ap.parse_args()
    cfg = json.load(open(ROOT / "_characters" / a.character / "character.json", encoding="utf-8"))
    b, order, prov, rot = LG.pick(cfg["class"], cfg["spec"])
    build = {"allocation": b["allocation"], "order": order}
    variants = {"base": (0, 0.0), "talented": (TALENTED, 0.0), "thrill": (0, THRILL), "both": (TALENTED, THRILL)}
    jobs, keys = [], []
    for L in LEVELS:
        for v, (shift, thrill) in variants.items():
            alloc = FR.allocation_at(build, min(60, L + shift))
            for seed in (3, 4):
                jobs.append((cfg["class"], alloc, L, rot, a.fights, seed, thrill))
                keys.append((L, v, seed))
    with multiprocessing.Pool(a.jobs, initializer=FT._init, initargs=("greens",)) as pool:
        res = pool.map(job, jobs, chunksize=1)
    t = dict(zip(keys, res))
    out = {"character": a.character, "class": cfg["class"], "spec": cfg["spec"], "build": b["id"], "rotation": rot,
           "date": datetime.date.today().isoformat(), "fights": a.fights, "seeds": [3, 4], "thrill": THRILL, "talented": TALENTED,
           "unit": "seconds per kill (time_per_kill: fight, drinking, eating, looting, travel, deaths)", "levels": {}}
    for L in LEVELS:
        row = {v: round((t[(L, v, 3)] + t[(L, v, 4)]) / 2, 3) for v in variants}
        out["levels"][str(L)] = row
        base = row["base"]
        print(f"  {L}: {base:.2f} s per kill; " + ", ".join(f"{v} {100 * (base - row[v]) / base:+.1f}%" for v in variants if v != "base"),
              flush=True)
    import plan as P
    start = a.start or LEVELS[0]
    rows = {int(L): r for L, r in out["levels"].items()}
    saved = {}
    for v in variants:
        if v == "base":
            continue
        m = sum((interp({k: r["base"] for k, r in rows.items()}, L) - interp({k: r[v] for k, r in rows.items()}, L)) * P.kills_per_level(L)
                for L in range(start, 60)) / 60
        saved[v] = round(m, 1)
    kill_min = sum(interp({k: r["base"] for k, r in rows.items()}, L) * P.kills_per_level(L) for L in range(start, 60)) / 60
    out["from"], out["killing_minutes"], out["minutes_saved"] = start, round(kill_min, 1), saved
    print(f"  from {start} to 60: {kill_min:.0f} min of killing; saved: " + ", ".join(f"{v} {m:.0f} min" for v, m in saved.items()))
    path = HERE / "legacy" / f"{a.character}.json"
    path.parent.mkdir(exist_ok=True)
    path.write_text(json.dumps(out, indent=1) + "\n", encoding="utf-8")
    print(f"wrote {path}")


if __name__ == "__main__":
    main()
