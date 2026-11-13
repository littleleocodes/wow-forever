"""Stat values and caps for the in-game gear add-on (2026-11-13, user: "a prompt ... to hand off to the wow-addons session so we can build a
small addon for this? Since we already have the testing and sims done, we should know what stats are important throughout leveling. We need
to also keep in mind caps for certain stats"; Pawn 2.14.2 values Forever's "+N Spell Power" at 0 and rating points ~5-8x high).

    python _reference/data/characters/addon_weights.py [names...]   -> _reference/data/characters/addon/<name>.json

Per character: leveling values by level (the fight lab's seconds per kill per point, from weights/<file>.json, divided by the unit stat's
value at that level: a caster's unit is 1 Spell Power, a tank's 1 Stamina), the level-60 raid values (the raid simulator's stat weights: a
caster's raid specs in their phase-1 BiS sets, ml/<class>-<spec>.json gear.bis.weights; a tank's tank value per point), the rating
conversions and the caps. Numbers are models of the beta (fight lab, simulator), not measurements.
"""
import datetime
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[2]
RAID = HERE.parent / "raidsim"
OUT = HERE / "addon"

# rating points per 1% (per skill point for defense): the pinned simulator's sim/core/base_stats_auto_gen.go (Forever's client tables)
RATINGS = {"hit_rating": 10, "crit_rating": 14, "haste_rating": 10, "expertise_rating": 10, "dodge_rating": 12, "parry_rating": 15,
           "block_rating": 5, "defense_rating": 1}
CAPS = {
    "spell_hit": {"unit": "percent", "vs_level_diff": {"-3": 1, "-2": 2, "-1": 3, "0": 4, "1": 5, "2": 6, "3": 17},
                  "note": "Spell miss chance by the target's level minus yours (bosses count +3; the simulator's sim/core/target.go and the "
                          "fight lab's tables.spell_miss). Forever has no 1% minimum miss, so hit is worth its value up to the whole miss "
                          "chance and nothing above it. Count hit from talents and buffs too (the character's current spell hit). While "
                          "leveling use the same-level row (4%); at 60 in raids the boss row (17%)."},
    "melee_hit": {"unit": "percent", "vs_level_diff": {"0": 5, "1": 5.5, "2": 6, "3": 8},
                  "note": "Special (yellow) attacks with full weapon skill. A dual-wielder's white swings miss 19 points more and are not "
                          "capped by gear in practice. Same level 5%, bosses 8% (no hit suppression in the simulator)."},
    "expertise": {"unit": "percent", "boss_dodge": 6.5, "boss_parry": 14,
                  "note": "Expertise lowers the target's dodge and parry: worth its value until the boss's dodge (6.5%) is gone; parry "
                          "only matters when you stand in front (tanks), up to 14% more."},
    "defense": {"unit": "skill", "crit_immune_at_60": 440, "per_point_percent": 0.04,
                "note": "A boss (+3) crits a tank 5.6% of the time at 300 defense skill; each point takes 0.04% off (the simulator's "
                        "MissDodgeParryBlockCritChancePerDefense), so 440 at level 60 makes you crit-immune. Below 60: 5 x your level + "
                        "140 against a boss three levels up. Past the cap a point still adds 0.04% miss, dodge, parry and block."},
    "spell_penetration": {"note": "Worth something only against resistance: mobs of your level have none while leveling (count 0); the raid "
                                  "values below come from the simulator's raid target."},
}
STAT_NAMES = {"StatSpellDamage": "spell_power", "StatFrostDamage": "frost_damage", "StatArcaneDamage": "arcane_damage",
              "StatFireDamage": "fire_damage", "StatShadowDamage": "shadow_damage", "StatNatureDamage": "nature_damage",
              "StatHolyDamage": "holy_damage", "StatIntellect": "intellect", "StatSpirit": "spirit", "StatStamina": "stamina",
              "StatCritRating": "crit_rating", "StatHitRating": "hit_rating", "StatHasteRating": "haste_rating",
              "StatSpellPiercing": "spell_penetration", "StatMP5": "mp5"}
TANK_NAMES = {"hit": "hit_rating", "crit": "crit_rating", "haste": "haste_rating", "expertise": "expertise_rating", "defense": "defense_rating",
              "block": "block_rating", "dodge": "dodge_rating", "parry": "parry_rating"}
SCHOOLS = ("frost", "arcane", "fire", "shadow", "nature", "holy")


def r(x):
    return round(x, 4)


def leveling(cfg, unit):
    w = json.loads((HERE / "weights" / cfg["weights_file"]).read_text(encoding="utf-8"))
    out = {}
    for lv, row in sorted(w["levels"].items(), key=lambda kv: int(kv[0])):
        v = row["weights"]
        base = v.get(unit) or 0
        if base <= 0:
            continue
        o = {TANK_NAMES.get(k, k): r(max(0.0, x) / base) for k, x in v.items()}   # a negative value is the lab's noise: 0
        if cfg["metric"] != "tank":   # a school's damage counts by the build's share of that school; damage-only spell damage counts in full
            for s in SCHOOLS:
                o[f"{s}_damage"] = r(o.get("spell_power", 1.0) * cfg["school_share"].get(s, 0.0))
            o["spell_damage"] = o.get("spell_power", 1.0)
            o["healing"] = 0.0
        out[lv] = {"seconds_per_kill": row.get("time_per_kill"), "unit_seconds": r(base), "values": o}   # unit_seconds: seconds per kill
        # one point of the unit stat saves at this level; an item's gain in units x unit_seconds / seconds_per_kill = its share of faster kills
    return {"source": f"fight lab, {w.get('build')} ({w.get('rotation') or w.get('entry')}), {w.get('date')}", "unit": unit,
            "levels": out, "not_measured": cfg["not_measured"]}


def raid(cfg):
    if cfg["metric"] == "tank":
        w = json.loads((HERE / "weights" / cfg["weights_file"]).read_text(encoding="utf-8"))
        sp = w["share_per_point"]
        return {"tank": {"source": f"raid simulator, {w['build']} in {w['entry']}, {w['date']}: tank value per point (threat and damage taken)",
                         "values": {TANK_NAMES.get(k, k): r(x / sp["stamina"]) for k, x in sp.items()}}}
    out = {}
    for f in sorted(RAID.glob(f"ml/{cfg['class']}-*.json")):
        d = json.loads(f.read_text(encoding="utf-8"))
        w = ((d.get("gear") or {}).get("bis") or {}).get("weights")
        if not w or not w.get("StatSpellDamage"):
            continue
        base = w["StatSpellDamage"]
        vals = {STAT_NAMES.get(k, k): r(max(0.0, x) / base) for k, x in w.items()}
        vals.setdefault("spell_damage", 1.0)
        out[f.stem.split("-", 1)[1]] = {"source": f"raid simulator ({f.name}: the spec's best build in its phase-1 BiS set, full raid)",
                                         "values": vals}
    return out


def build(name):
    d = ROOT / "_characters" / name
    c = json.loads((d / "character.json").read_text(encoding="utf-8"))
    tank = c.get("metric") == "tank"
    wf = c.get("weights") or next((p.name for p in sorted((HERE / "weights").glob(f"{c['class']}-*.json")) if "tank" not in p.name), None)
    cfg = {"class": c["class"], "metric": "tank" if tank else "kill_time", "school_share": c.get("school_share") or {}, "weights_file": wf,
           "not_measured": [] if tank else ["hit_rating", "crit_rating", "haste_rating", "spell_penetration"]}
    unit = "stamina" if tank else "spell_power"
    return {"character": name, "class": c["class"], "spec": c.get("spec"), "metric": cfg["metric"], "made": datetime.date.today().isoformat(),
            "unit": unit, "school_share": cfg["school_share"], "ratings_per_percent": RATINGS, "caps": CAPS,
            "leveling": leveling(cfg, unit), "raid_60": raid(cfg),
            "note": ("A value is what one point of a stat is worth in the unit stat (1 Spell Power for a caster, 1 Stamina for a tank): by "
                     "level while leveling (seconds per kill saved, fight lab; interpolate between listed levels) and at 60 in a raid (the "
                     "simulator). Rating stats are per rating point (10 hit rating = 1%). Leveling crit, hit, haste and penetration from gear "
                     "are not measured yet for casters (leveling.not_measured): the add-on must show them as unscored, not as 0.")}


def main(argv):
    names = argv or [p.name for p in sorted((ROOT / "_characters").iterdir()) if (p / "character.json").exists()]
    OUT.mkdir(exist_ok=True)
    for n in names:
        o = build(n)
        p = OUT / f"{n}.json"
        p.write_text(json.dumps(o, indent=1) + "\n", encoding="utf-8", newline="\n")
        lv = o["leveling"]["levels"]
        print(f"wrote {p.relative_to(ROOT)}: {len(lv)} levels ({min(lv, key=int)}-{max(lv, key=int)}), raid {sorted(o['raid_60'])}")


if __name__ == "__main__":
    main(sys.argv[1:])
