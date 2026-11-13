"""Stat values and caps for the in-game gear add-on, every class (2026-11-13, user: "this is being made for all classes right? And before
it's built I think we should make sure all the stats are scored"; replaces addon_weights.py, which covered Arcea and Tara only).

    python _reference/data/characters/addon_values.py      -> _reference/data/characters/addon/forever-gear-values.json

- leveling: every leveling page pick (weights/leveling/<class>-<build id>.json, stat_weights_all.py): by level the fight lab's seconds per
  kill each point of a stat saves (negative readings are the lab's noise: 0), the kill time, the build's damage by spell school (one lab
  run per level: school-specific spell damage counts by that share) and the unit the add-on shows a gain in (Spell Power or attack power,
  whichever the build values more);
- raid: every damage spec with an ML record: the simulator's stat weights in the spec's phase-1 BiS set (gear.bis.weights) over the unit
  stat's, with hit below the cap from raidsim/hit-below-cap.json (a BiS set at the cap reads hit as 0);
- tank: weights/<class>-tank.json (tank_weights.py: the raid simulator's tank value per point) over Stamina's;
- ratings and caps (_reference/forever-stats.md).
Numbers are models of the beta (fight lab, simulator), not measurements.
"""
import datetime
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
DATA = HERE.parent
ROOT = DATA.parent.parent
RAID = DATA / "raidsim"
OUT = HERE / "addon"
sys.path[:0] = [str(DATA / "fightlab"), str(DATA / "scorer"), str(DATA)]

RATINGS = {"hit_rating": 10, "crit_rating": 14, "haste_rating": 10, "expertise_rating": 10, "dodge_rating": 12, "parry_rating": 15,
           "block_rating": 5, "defense_rating": 1}
CAPS = {
    "spell_hit": {"unit": "percent", "vs_level_diff": {"-3": 1, "-2": 2, "-1": 3, "0": 4, "1": 5, "2": 6, "3": 17},
                  "note": "Spell miss by the target's level minus yours (bosses +3). No 1% minimum miss: hit counts up to the whole miss "
                          "chance and nothing above. Count talent and racial hit (the character's current spell hit). Leveling: the "
                          "same-level row (4%); raids: 17%. Client tooltip CR_*_HIT_CAP_TOOLTIP."},
    "melee_hit": {"unit": "percent", "vs_level_diff": {"0": 5, "1": 5.5, "2": 6, "3": 8}, "dual_wield_white_extra": 19,
                  "note": "Special attacks and a single weapon's swings; a dual-wielder's white swings miss 19 points more (27% vs bosses). "
                          "Client tooltip: 8% melee/ranged and 27% dual wielding against raid bosses, 5% against your level."},
    "expertise": {"unit": "percent", "mob_dodge": 5, "mob_parry": 5, "boss_dodge": 6.5, "boss_parry": 14,
                  "note": "Expertise lowers the target's dodge and parry alike: worth its value until dodge is gone (parry too when you "
                          "stand in front, as solo leveling and tanking do)."},
    "defense": {"unit": "skill", "crit_immune_at_60": 440, "per_point_percent": 0.04,
                "note": "A boss crits a tank 5.6% at 300 defense skill, 0.04% less per point: 440 at 60. Below 60: 5 x level + 140 "
                        "against a boss three levels up."},
    "spell_penetration": {"note": "Worth 0 while leveling (mobs of your level have no resistance); raid values from the simulator."},
    "haste": {"note": "10 rating = 1% faster casts and swings at every level. Whether haste shortens the global cooldown is open "
                      "(the simulator says yes for spells, the client's Nature's Grace suggests no; _reference/forever-stats.md row 7)."},
}
SIM_STAT = {"StatSpellDamage": "spell_power", "StatFrostDamage": "frost_damage", "StatArcaneDamage": "arcane_damage", "StatFireDamage": "fire_damage",
            "StatShadowDamage": "shadow_damage", "StatNatureDamage": "nature_damage", "StatHolyDamage": "holy_damage", "StatIntellect": "intellect",
            "StatSpirit": "spirit", "StatStamina": "stamina", "StatStrength": "strength", "StatAgility": "agility",
            "StatAttackPower": "attack_power", "StatRangedAttackPower": "ranged_attack_power", "StatFeralAttackPower": "feral_attack_power",
            "StatCritRating": "crit_rating", "StatHitRating": "hit_rating", "StatHasteRating": "haste_rating",
            "StatExpertiseRating": "expertise_rating", "StatArmorPenetration": "armor_penetration", "StatSpellPiercing": "spell_penetration",
            "StatMP5": "mp5", "PseudoStatMainHandDps": "mh_weapon_dps", "PseudoStatOffHandDps": "oh_weapon_dps",
            "PseudoStatRangedDps": "ranged_weapon_dps"}
TANK_STAT = {"hit": "hit_rating", "crit": "crit_rating", "haste": "haste_rating", "expertise": "expertise_rating", "defense": "defense_rating",
             "block": "block_rating", "dodge": "dodge_rating", "parry": "parry_rating", "weapon_dps": "mh_weapon_dps"}
CLASSES = "druid hunter mage paladin priest rogue shaman warlock warrior".split()


def r(x):
    return round(x, 5)


def school_shares(cls, alloc, level, rot):
    """The build's damage by spell school at one level (300 fights): {school: share}; physical damage is left out."""
    import run as FR
    mod = FR.make_module(cls, alloc, level, rot)
    o = FR.simulate(cls, alloc, level, rot, 300, 9, 0)
    by = {}
    for name, dmg in (o.get("damage") or {}).items():
        sp = mod.book.get(name) if hasattr(mod, "book") else None
        sch = getattr(sp, "school", None) if sp is not None else None
        if sch and sch != "physical" and dmg:
            by[sch] = by.get(sch, 0.0) + dmg
    tot = sum(by.values())
    return {k: round(v / tot, 3) for k, v in sorted(by.items(), key=lambda kv: -kv[1])} if tot else {}


def leveling(cls):
    import level_guides as LG
    import run as FR
    SA = LG.fightlab_signature_audit()
    out = []
    for slot in SA.page_slots(cls):
        if not slot[1]:
            continue
        spec, b = slot[0], slot[1][0]
        f = HERE / "weights" / "leveling" / f"{cls}-{b['id']}.json"
        if not f.exists():
            out.append({"spec": spec, "build": b["id"], "missing": f.name})
            continue
        w = json.loads(f.read_text(encoding="utf-8"))
        _, order, _, rot = LG.pick(cls, spec)
        lv = {}
        for L, row in sorted(w["levels"].items(), key=lambda kv: int(kv[0])):
            v = {k: r(max(0.0, x)) for k, x in row["weights"].items()}
            unit = "spell_power" if v.get("spell_power", 0) >= v.get("attack_power", 0) else "attack_power"
            share = school_shares(cls, FR.allocation_at({"allocation": b["allocation"], "order": order}, int(L)), int(L), rot)
            if v.get("spell_power"):
                for s, x in share.items():
                    v[f"{s}_damage"] = r(v["spell_power"] * x)
                v["spell_damage"] = v["spell_power"]
            lv[L] = {"seconds_per_kill": row["time_per_kill"], "unit": unit, "unit_seconds": v.get(unit, 0.0), "school_share": share, "values": v}
        out.append({"spec": spec, "build": b["id"], "rotation": rot, "source": f"fight lab {w['date']}, {w['fights']} fights x 2 seeds",
                    "levels": lv})
    return out


def raid(cls, below):
    out = []
    for f in sorted((RAID / "ml").glob(f"{cls}-*.json")):
        d = json.loads(f.read_text(encoding="utf-8"))
        w = ((d.get("gear") or {}).get("bis") or {}).get("weights")
        if not w:
            continue
        vals = {SIM_STAT.get(k, k): x for k, x in w.items()}
        hb = (below.get("specs") or {}).get(f.stem)
        if hb and hb.get("hit_below_cap"):
            vals["hit_rating_below_cap"] = hb["hit_below_cap"]
        unit = max(("spell_power", "attack_power", "ranged_attack_power"), key=lambda k: vals.get(k, 0.0))
        base = vals.get(unit) or 1.0
        out.append({"spec": d["spec"], "slug": f.stem.split("-", 1)[1], "build": d.get("best"), "unit": unit,
                    "source": f"raid simulator, {f.name} (the spec's best build in its phase-1 BiS set, full raid)",
                    "values": {k: r(max(0.0, x) / base) for k, x in vals.items()}})
    return out


def tank(cls):
    f = HERE / "weights" / f"{cls}-tank.json"
    if not f.exists():
        return None
    w = json.loads(f.read_text(encoding="utf-8"))
    sp = w["share_per_point"]
    return {"spec": "Protection" if cls != "druid" else "Feral Combat (bear)", "build": w["build"], "unit": "stamina",
            "source": f"raid simulator, {w['build']} in {w['entry']}, {w['date']}: tank value per point (threat, damage taken, effective health)",
            "values": {TANK_STAT.get(k, k): r(x / sp["stamina"]) for k, x in sp.items()}}


def main():
    below = json.loads((RAID / "hit-below-cap.json").read_text(encoding="utf-8")) if (RAID / "hit-below-cap.json").exists() else {}
    o = {"made": datetime.date.today().isoformat(), "ratings_per_percent": RATINGS, "caps": CAPS,
         "note": ("Leveling values: seconds per kill one point saves at that level (fight lab; interpolate between levels; an item's gain = "
                  "sum of stat x value, its share of faster kills = gain / seconds_per_kill); unit_seconds is the unit stat's value (show a "
                  "gain in that stat: gain / unit_seconds). Raid and tank values: in the unit stat (1 Spell Power, 1 attack power or 1 "
                  "Stamina = 1). Ratings per rating point (10 hit rating = 1%, at every level). Count each item line as listed: '+N Spell "
                  "Power' is N damage and N healing, '+N Spell Healing' items list their third as a separate '+N Spell Damage' line. "
                  "Models of the beta, not measurements."),
         "classes": {}}
    for cls in CLASSES:
        o["classes"][cls] = {"leveling": leveling(cls), "raid": raid(cls, below), "tank": tank(cls)}
        print(f"{cls}: {len(o['classes'][cls]['leveling'])} leveling builds, {len(o['classes'][cls]['raid'])} raid specs, "
              f"tank {'yes' if o['classes'][cls]['tank'] else 'no'}", flush=True)
    OUT.mkdir(exist_ok=True)
    p = OUT / "forever-gear-values.json"
    p.write_text(json.dumps(o, indent=1) + "\n", encoding="utf-8", newline="\n")
    print(f"wrote {p.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
