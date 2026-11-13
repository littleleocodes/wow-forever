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
# Every stat a piece of gear can carry, by class (2026-11-13, the gear add-on; user: "make sure all the stats are scored"). Ratings in rating
# points (tables.RATING_PER_PCT: the same at every level). Hit and expertise are measured as a step DOWN (a negative step): their value per
# point while under the cap, also for a build its talents already cap (Arcea's Precision 2/3 is the 4% same-level spell cap); the add-on
# applies the cap with the character's own hit. Spell penetration is 0 while leveling (mobs of your level have no resistance) and not run.
FULL_STEPS = {"stamina": 30, "armor": 300, "crit_rating": 28, "hit_rating": -20, "haste_rating": 20, "defense_rating": 20, "dodge_rating": 24,
              "intellect": 30, "spirit": 30, "mp5": 10, "spell_power": 15, "healing": 30, "wand_dps": 10,
              "strength": 30, "agility": 30, "attack_power": 60, "mh_weapon_dps": 5, "oh_weapon_dps": 5, "ranged_weapon_dps": 5,
              "expertise_rating": -20, "weapon_skill": 5, "parry_rating": 30, "block_rating": 10, "block_value": 20}
CASTER_STATS = ["intellect", "spirit", "stamina", "spell_power", "armor", "mp5", "wand_dps", "crit_rating", "hit_rating", "haste_rating",
                "defense_rating", "dodge_rating"]
MELEE_STATS = ["strength", "agility", "stamina", "attack_power", "armor", "mh_weapon_dps", "crit_rating", "hit_rating", "haste_rating",
               "expertise_rating", "weapon_skill", "defense_rating", "dodge_rating", "parry_rating"]
CLASS_STATS = {"mage": CASTER_STATS, "warlock": CASTER_STATS, "priest": CASTER_STATS + ["healing"],
               "warrior": MELEE_STATS + ["oh_weapon_dps", "block_rating", "block_value"], "rogue": MELEE_STATS + ["oh_weapon_dps"],
               "hunter": MELEE_STATS + ["intellect", "spirit", "mp5", "ranged_weapon_dps"],
               "paladin": MELEE_STATS + ["intellect", "spirit", "mp5", "spell_power", "healing", "block_rating", "block_value"],
               "shaman": MELEE_STATS + ["intellect", "spirit", "mp5", "spell_power", "healing", "oh_weapon_dps", "block_rating", "block_value"],
               "druid": MELEE_STATS + ["intellect", "spirit", "mp5", "spell_power", "healing"]}
FULL_LEVELS = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60]


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
    ap.add_argument("--full", action="store_true", help="every stat of the class at levels 10-60 -> weights/leveling/<class>-<build id>.json "
                                                         "(2026-11-13, the gear add-on); without it the planner's older set and file")
    a = ap.parse_args()
    b, order, prov, rot = LG.pick(a.cls, a.spec)
    if b is None:
        raise SystemExit(f"{a.cls} {a.spec}: no leveling page pick")
    build = {"allocation": b["allocation"], "order": order}
    if a.full:
        steps = {k: FULL_STEPS[k] for k in CLASS_STATS[a.cls]}
        levels = FULL_LEVELS
    else:
        steps = dict(STEPS) if a.cls in CASTER else {k: v for k, v in STEPS.items() if k != "wand_dps"}
        levels = LEVELS
    jobs, keys = [], []
    for L in levels:
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
    if a.full:
        out["note"] = ("Negative steps (hit_rating, expertise_rating): the value per point while under the cap, measured as a step down. "
                       "Ratings in rating points (the same at every level). A fight-lab model of the beta, not a measurement.")
        out["provisional_order"] = bool(prov)
    for L in levels:
        base = (t[(L, None, 3)] + t[(L, None, 4)]) / 2
        row = {"time_per_kill": round(base, 3), "weights": {}}
        for st, step in steps.items():
            d = ((t[(L, None, 3)] - t[(L, st, 3)]) + (t[(L, None, 4)] - t[(L, st, 4)])) / 2
            row["weights"][st] = round(d / step, 5)
        out["levels"][str(L)] = row
        print(f"  {L}: {base:.2f} s per kill; " + ", ".join(f"{k} {v:+.4f}" for k, v in row["weights"].items()), flush=True)
    path = HERE / "weights" / "leveling" / f"{a.cls}-{b['id']}.json" if a.full else HERE / "weights" / f"{a.cls}-{rot}.json"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(out, indent=1) + "\n", encoding="utf-8")
    print(f"wrote {path}")


if __name__ == "__main__":
    main()
