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
# applies the cap with the character's own hit. Spell penetration ("Spell Piercing") is bonus damage past the target's resistance
# (tables.pierce_bonus, wowsims/forever issue #76: 138 Forever logs), so it counts while leveling too; measured for every class with
# non-Holy spell damage (hunters: Arcane Shot and stings; rogues: poisons), added 2026-11-13 with --only.
# Steps about 3x the planner's (2026-11-13 noise test, 4 independent seed pairs of 3,000 fights at levels 30 and 60): with the small steps
# crit and Intellect readings spread 30-55% between seed pairs and Destruction's Spell Power read 0 at +15 (its tuned rules do not react
# to small changes around the lab's standard gear: +15 saves 0.01 s a kill, +30 0.35 s, +60 1.03 s); the 4x steps spread 3-6x less. A
# larger step is the average value over a few items' worth around the standard gear, which is what a real character's gear differs by.
FULL_STEPS = {"stamina": 60, "armor": 900, "crit_rating": 84, "hit_rating": -60, "haste_rating": 60, "defense_rating": 60, "dodge_rating": 72,
              "intellect": 90, "spirit": 90, "mp5": 30, "spell_power": 45, "healing": 90, "wand_dps": 20,
              "strength": 90, "agility": 90, "attack_power": 180, "mh_weapon_dps": 10, "oh_weapon_dps": 10, "ranged_weapon_dps": 10,
              "expertise_rating": -60, "weapon_skill": 10, "parry_rating": 90, "block_rating": 30, "block_value": 60, "spell_penetration": 15}
CASTER_STATS = ["intellect", "spirit", "stamina", "spell_power", "armor", "mp5", "wand_dps", "crit_rating", "hit_rating", "haste_rating",
                "defense_rating", "dodge_rating", "spell_penetration"]
MELEE_STATS = ["strength", "agility", "stamina", "attack_power", "armor", "mh_weapon_dps", "crit_rating", "hit_rating", "haste_rating",
               "expertise_rating", "weapon_skill", "defense_rating", "dodge_rating", "parry_rating"]
CLASS_STATS = {"mage": CASTER_STATS, "warlock": CASTER_STATS, "priest": CASTER_STATS + ["healing"],
               "warrior": MELEE_STATS + ["oh_weapon_dps", "block_rating", "block_value"], "rogue": MELEE_STATS + ["oh_weapon_dps", "spell_penetration"],
               "hunter": MELEE_STATS + ["intellect", "spirit", "mp5", "ranged_weapon_dps", "spell_penetration"],
               "paladin": MELEE_STATS + ["intellect", "spirit", "mp5", "spell_power", "healing", "block_rating", "block_value"],
               "shaman": MELEE_STATS + ["intellect", "spirit", "mp5", "spell_power", "healing", "oh_weapon_dps", "block_rating", "block_value",
                                        "spell_penetration"],
               "druid": MELEE_STATS + ["intellect", "spirit", "mp5", "spell_power", "healing", "spell_penetration"]}
FULL_LEVELS = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60]


ABOVE = "hit_rating_above_cap"   # a pseudo-stat (2026-11-13): hit rating past the special-attack cap, worth something only to a
ABOVE_STEP = 60.0                # dual-wielder's white swings (24% miss vs 5%); measured from the cap up, --only hit_rating_above_cap


def special_cap_rating(cls, alloc, level, rot):
    """The hit rating that brings the build to the special-attack cap against a same-level mob (its talents' hit counted)."""
    mod = FR.make_module(cls, alloc, level, rot)
    p = mod.make_player(level)
    return max(0.0, TB.MELEE_MISS - p.hit_bonus) * 100 * TB.RATING_PER_PCT["hit_rating"]


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
    ap.add_argument("--base", choices=("standard", "best"), default="standard",
                    help="with --full: measure on top of the lab's standard gear, or of each level's best Forever set (forever_base.py, "
                         "weights/forever-base.json; 2026-11-13, the add-on's second gear point) -> weights/leveling-best/")
    ap.add_argument("--full", action="store_true", help="every stat of the class at levels 10-60 -> weights/leveling/<class>-<build id>.json "
                                                         "(2026-11-13, the gear add-on); without it the planner's older set and file")
    ap.add_argument("--only", nargs="*", help="with --full: measure only these stats and merge them into the existing file (the base runs "
                                               "repeat on the same seeds, so the rest stays valid)")
    a = ap.parse_args()
    b, order, prov, rot = LG.pick(a.cls, a.spec)
    if b is None:
        raise SystemExit(f"{a.cls} {a.spec}: no leveling page pick")
    build = {"allocation": b["allocation"], "order": order}
    if a.full:
        steps = {k: FULL_STEPS[k] for k in CLASS_STATS[a.cls]}
        above = bool(a.only and ABOVE in a.only)
        if a.only:
            steps = {k: v for k, v in steps.items() if k in a.only}
            if not steps and not above:
                print(f"{a.cls}: none of {a.only} is one of the class's stats; nothing to do")
                return
        levels = FULL_LEVELS
    else:
        above = False
        steps = dict(STEPS) if a.cls in CASTER else {k: v for k, v in STEPS.items() if k != "wand_dps"}
        levels = LEVELS
    base = {L: {} for L in levels}
    if a.base == "best":
        fb = json.loads((HERE / "weights" / "forever-base.json").read_text(encoding="utf-8"))["builds"][f"{a.cls}-{b['id']}"]
        base = {L: dict(fb[str(L)]["best"]["bonus"]) for L in levels}
    jobs, keys, caps = [], [], {}
    for L in levels:
        alloc = FR.allocation_at(build, L)
        for st in [None] + list(steps):
            for seed in (3, 4):
                bonus = dict(base[L])
                if st is not None:
                    bonus[st] = bonus.get(st, 0.0) + steps[st]
                jobs.append((a.cls, alloc, L, rot, a.fights, seed, bonus))
                keys.append((L, st, seed))
        if above:   # hit past the special-attack cap (a dual-wielder's white swings): from the cap up by ABOVE_STEP
            cap = special_cap_rating(a.cls, alloc, L, rot)
            caps[L] = cap
            for which, extra in (("cap0", 0.0), ("cap1", ABOVE_STEP)):
                for seed in (3, 4):
                    bonus = dict(base[L])
                    bonus["hit_rating"] = bonus.get("hit_rating", 0.0) + cap + extra
                    jobs.append((a.cls, alloc, L, rot, a.fights, seed, bonus))
                    keys.append((L, which, seed))
    with multiprocessing.Pool(a.jobs, initializer=FT._init, initargs=("greens",)) as pool:
        res = pool.map(job, jobs, chunksize=1)
    t = dict(zip(keys, res))
    out = {"class": a.cls, "spec": a.spec, "build": b["id"], "rotation": rot, "date": datetime.date.today().isoformat(), "fights": a.fights,
           "seeds": [3, 4], "steps": steps, "unit": "seconds per kill saved per point (negative: slower)", "levels": {}}
    if a.full:
        out["note"] = ("Negative steps (hit_rating, expertise_rating): the value per point while under the cap, measured as a step down. "
                       "Ratings in rating points (the same at every level). A fight-lab model of the beta, not a measurement.")
        out["provisional_order"] = bool(prov)
        out["base"] = a.base
        if a.base == "best":
            out["base_bonus"] = {str(L): base[L] for L in levels}
    for L in levels:
        base = (t[(L, None, 3)] + t[(L, None, 4)]) / 2
        row = {"time_per_kill": round(base, 3), "weights": {}}
        for st, step in steps.items():
            d = ((t[(L, None, 3)] - t[(L, st, 3)]) + (t[(L, None, 4)] - t[(L, st, 4)])) / 2
            row["weights"][st] = round(d / step, 5)
        if above:
            d = ((t[(L, "cap0", 3)] - t[(L, "cap1", 3)]) + (t[(L, "cap0", 4)] - t[(L, "cap1", 4)])) / 2
            row["weights"][ABOVE] = round(max(0.0, d) / ABOVE_STEP, 5)
            row["special_cap_rating"] = round(caps[L], 1)
        out["levels"][str(L)] = row
        print(f"  {L}: {base:.2f} s per kill; " + ", ".join(f"{k} {v:+.4f}" for k, v in row["weights"].items()), flush=True)
    folder = "leveling" if a.base == "standard" else "leveling-best"
    path = HERE / "weights" / folder / f"{a.cls}-{b['id']}.json" if a.full else HERE / "weights" / f"{a.cls}-{rot}.json"
    path.parent.mkdir(parents=True, exist_ok=True)
    if a.full and a.only and path.exists():   # merge: the file's other stats stay, these are added or replaced
        old = json.loads(path.read_text(encoding="utf-8"))
        for L, row in out["levels"].items():
            o = old["levels"].get(L)
            if o is None:
                continue
            if abs(o["time_per_kill"] - row["time_per_kill"]) > 1e-6:
                print(f"  note: level {L} base {row['time_per_kill']} differs from the file's {o['time_per_kill']} (the lab changed?)")
            o["weights"].update(row["weights"])
            if "special_cap_rating" in row:
                o["special_cap_rating"] = row["special_cap_rating"]
        old["steps"] = {k: FULL_STEPS[k] for k in CLASS_STATS[a.cls] if k in old["steps"] or k in steps}
        old.setdefault("added", {}).update({k: datetime.date.today().isoformat() for k in list(steps) + ([ABOVE] if above else [])})
        out = old
    path.write_text(json.dumps(out, indent=1) + "\n", encoding="utf-8")
    print(f"wrote {path}")


if __name__ == "__main__":
    main()
