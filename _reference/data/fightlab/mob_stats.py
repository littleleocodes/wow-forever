"""Mob health, damage, armor and caster share by level from the Classic 1.12 creature database.

    python _reference/data/fightlab/mob_stats.py --extract <ClassicDB_1_12_1_z2815.sql>   # SQL dump -> raw CSV (archived)
    python _reference/data/fightlab/mob_stats.py --write                                  # raw CSV -> mob_stats.json + table

Source: cmangos/classic-db, Full_DB/ClassicDB_1_12_1_z2815.sql.gz (https://github.com/cmangos/classic-db), whose
`creature_template` rows carry the sniffed 1.12 client values (MinLevelHealth/MaxLevelHealth, MinMeleeDmg/MaxMeleeDmg with
the base attack power already included, Armor, MeleeBaseAttackTime, UnitClass, Rank) and whose `creature` table lists
every world spawn. The raw extract (one line per creature template with its spawn count) is archived in
`_reference/data/raw/2026-09-26-cmangos-classic-db-z2815/creature_stats.csv` so the fit is reproducible without the 73 MB dump.

WoW: Forever caveat: these are Classic Era numbers. The beta client does not carry creature stats (they are server side)
and the Wowhead Forever NPC tooltips list level and type only, so the sim uses them as its prior until beta measurements
exist (`tables.MOB_HP_MULT` / `MOB_DMG_MULT` scale them in `sensitivity.py`).

Filter ("a normal outdoor mob you fight while leveling"): Rank 0 (normal), not a critter / totem / non-combat pet, not
civilian, no NPC flags (vendors, trainers, quest givers), attackable (UnitFlags without NON_ATTACKABLE 0x2 or
IMMUNE_TO_PLAYER 0x100), MaxMeleeDmg > 0, spawned in the world at least once, level 1-60. Every spawn counts once, so
a template with 40 spawns weighs 40 (what you actually meet). Level = the template's average level.
Casters = UnitClass 8 (mage) or 2 (paladin) templates: less health, they hit less hard and cast instead.
"""
import argparse
import csv
import json
import pathlib
import statistics
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[2]
RAW = ROOT / "_reference/data/raw/2026-09-26-cmangos-classic-db-z2815/creature_stats.csv"
OUT = HERE / "mob_stats.json"

COLS = ["Entry", "Name", "SubName", "MinLevel", "MaxLevel", "ModelId1", "ModelId2", "ModelId3", "ModelId4", "Faction", "Scale", "Family",
        "CreatureType", "InhabitType", "RegenerateStats", "RacialLeader", "NpcFlags", "UnitFlags", "DynamicFlags", "ExtraFlags",
        "CreatureTypeFlags", "StaticFlags1", "StaticFlags2", "StaticFlags3", "StaticFlags4", "SpeedWalk", "SpeedRun", "Detection",
        "CallForHelp", "Pursuit", "Leash", "Timeout", "UnitClass", "Rank", "HealthMultiplier", "PowerMultiplier", "DamageMultiplier",
        "DamageVariance", "ArmorMultiplier", "ExperienceMultiplier", "MinLevelHealth", "MaxLevelHealth", "MinLevelMana", "MaxLevelMana",
        "MinMeleeDmg", "MaxMeleeDmg", "MinRangedDmg", "MaxRangedDmg", "Armor", "MeleeAttackPower", "RangedAttackPower",
        "MeleeBaseAttackTime", "RangedBaseAttackTime", "DamageSchool", "MinLootGold", "MaxLootGold", "LootId", "PickpocketLootId",
        "SkinningLootId", "KillCredit1", "KillCredit2", "MechanicImmuneMask", "SchoolImmuneMask", "ResistanceHoly", "ResistanceFire",
        "ResistanceNature", "ResistanceFrost", "ResistanceShadow", "ResistanceArcane", "PetSpellDataId", "MovementType", "TrainerType",
        "TrainerSpell", "TrainerClass", "TrainerRace", "TrainerTemplateId", "VendorTemplateId", "GossipMenuId", "InteractionPauseTimer",
        "CorpseDecay", "SpellList", "StringId1", "StringId2", "EquipmentTemplateId", "Civilian", "AIName", "ScriptName"]
KEEP = ["Entry", "Name", "MinLevel", "MaxLevel", "CreatureType", "Rank", "UnitClass", "NpcFlags", "UnitFlags", "Civilian", "Faction",
        "HealthMultiplier", "DamageMultiplier", "MinLevelHealth", "MaxLevelHealth", "MaxLevelMana", "MinMeleeDmg", "MaxMeleeDmg",
        "Armor", "MeleeAttackPower", "MeleeBaseAttackTime", "DamageSchool"]
CASTER_CLASSES = {2, 8}
TYPE_NAMES = {1: "Beast", 2: "Dragonkin", 3: "Demon", 4: "Elemental", 5: "Giant", 6: "Undead", 7: "Humanoid", 8: "Critter",
              9: "Mechanical", 10: "Not specified", 11: "Totem"}


def sql_tuples(line):
    """Yield the value tuples of one `INSERT INTO t VALUES (...),(...);` line as lists of str/None."""
    i = line.index("VALUES") + 6
    n = len(line)
    while i < n:
        while i < n and line[i] != "(":
            i += 1
        if i >= n:
            return
        i += 1
        row, cur, in_str = [], [], False
        while i < n:
            c = line[i]
            if in_str:
                if c == "\\":
                    cur.append(line[i + 1]); i += 2; continue
                if c == "'":
                    in_str = False
                else:
                    cur.append(c)
            elif c == "'":
                in_str = True
            elif c == ",":
                row.append("".join(cur)); cur = []
            elif c == ")":
                row.append("".join(cur))
                yield [None if v == "NULL" else v for v in row]
                i += 1
                break
            else:
                cur.append(c)
            i += 1


def extract(sql_path):
    templates, spawns = {}, {}
    with open(sql_path, encoding="utf-8", errors="replace") as f:
        for line in f:
            if line.startswith("INSERT INTO `creature_template` VALUES"):
                for row in sql_tuples(line):
                    if len(row) != len(COLS):
                        raise SystemExit(f"creature_template has {len(row)} columns, expected {len(COLS)}: update COLS")
                    d = dict(zip(COLS, row))
                    templates[int(d["Entry"])] = {k: d[k] for k in KEEP}
            elif line.startswith("INSERT INTO `creature` VALUES"):
                for row in sql_tuples(line):
                    e = int(row[1])
                    spawns[e] = spawns.get(e, 0) + 1
    RAW.parent.mkdir(parents=True, exist_ok=True)
    with open(RAW, "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(KEEP + ["Spawns"])
        for e in sorted(templates):
            t = templates[e]
            w.writerow([t[k] if t[k] is not None else "" for k in KEEP] + [spawns.get(e, 0)])
    print(f"wrote {RAW.relative_to(ROOT)}: {len(templates)} templates, {sum(spawns.values())} spawns")


def load_rows():
    rows = []
    with open(RAW, encoding="utf-8") as f:
        for d in csv.DictReader(f):
            r = {k: d[k] for k in ("Entry", "Name")}
            for k in ("MinLevel", "MaxLevel", "CreatureType", "Rank", "UnitClass", "NpcFlags", "UnitFlags", "Civilian", "Faction",
                      "MeleeBaseAttackTime", "DamageSchool", "Spawns"):
                r[k] = int(float(d[k] or 0))
            for k in ("HealthMultiplier", "DamageMultiplier", "MinLevelHealth", "MaxLevelHealth", "MaxLevelMana", "MinMeleeDmg",
                      "MaxMeleeDmg", "Armor", "MeleeAttackPower"):
                r[k] = float(d[k] or 0)
            rows.append(r)
    return rows


def is_normal_mob(r):
    return (r["Rank"] == 0 and r["CreatureType"] in (1, 2, 3, 4, 5, 6, 7, 9, 10) and not r["Civilian"] and r["NpcFlags"] == 0
            and not (r["UnitFlags"] & 0x2) and not (r["UnitFlags"] & 0x100) and r["MaxMeleeDmg"] > 0 and r["Spawns"] > 0
            and 1 <= r["MinLevel"] <= 60 and r["MaxLevel"] <= 63)


def wmedian(pairs):
    """Weighted median of (value, weight)."""
    pairs = sorted(pairs)
    tot = sum(w for _, w in pairs)
    acc = 0.0
    for v, w in pairs:
        acc += w
        if acc >= tot / 2:
            return v
    return pairs[-1][0]


def wmean(pairs):
    tot = sum(w for _, w in pairs)
    return sum(v * w for v, w in pairs) / tot if tot else 0.0


def build(rows, write):
    mobs = [r for r in rows if is_normal_mob(r)]
    per_level = {L: [] for L in range(1, 61)}
    for r in mobs:
        L = round((r["MinLevel"] + r["MaxLevel"]) / 2)
        L = max(1, min(60, L))
        hp = (r["MinLevelHealth"] + r["MaxLevelHealth"]) / 2
        dmg = (r["MinMeleeDmg"] + r["MaxMeleeDmg"]) / 2 * (r["DamageMultiplier"] or 1.0)
        swing = (r["MeleeBaseAttackTime"] or 2000) / 1000.0
        per_level[L].append({"hp": hp, "dmg": dmg, "dps": dmg / swing, "swing": swing, "armor": r["Armor"], "w": r["Spawns"],
                             "caster": r["UnitClass"] in CASTER_CLASSES, "mana": r["MaxLevelMana"] > 0, "school": r["DamageSchool"]})
    table = {}
    for L in range(1, 61):
        xs = per_level[L]
        if not xs:
            continue
        melee = [x for x in xs if not x["caster"]]
        cast = [x for x in xs if x["caster"]]
        w_all = sum(x["w"] for x in xs)
        table[L] = {
            "templates": len(xs), "spawns": w_all,
            "health": wmedian([(x["hp"], x["w"]) for x in xs]), "health_mean": wmean([(x["hp"], x["w"]) for x in xs]),
            "health_p20": wquantile([(x["hp"], x["w"]) for x in xs], 0.2), "health_p80": wquantile([(x["hp"], x["w"]) for x in xs], 0.8),
            "dmg": wmedian([(x["dmg"], x["w"]) for x in xs]), "dps": wmedian([(x["dps"], x["w"]) for x in xs]),
            "swing": wmedian([(x["swing"], x["w"]) for x in xs]), "armor": wmedian([(x["armor"], x["w"]) for x in xs]),
            "caster_share": sum(x["w"] for x in cast) / w_all,
            "melee_health": wmedian([(x["hp"], x["w"]) for x in melee]) if melee else None,
            "melee_dmg": wmedian([(x["dmg"], x["w"]) for x in melee]) if melee else None,
            "caster_health": wmedian([(x["hp"], x["w"]) for x in cast]) if cast else None,
            "caster_dmg": wmedian([(x["dmg"], x["w"]) for x in cast]) if cast else None,
        }
    # smoothed anchors every 5 levels (weighted over levels L-2..L+2) for the sim's interpolation tables
    anchors = {}
    for L in range(5, 61, 5):
        window = [x for LL in range(L - 2, L + 3) for x in per_level.get(LL, [])]
        if not window:
            continue
        melee = [x for x in window if not x["caster"]]
        cast = [x for x in window if x["caster"]]
        anchors[L] = {
            "health": round(wmedian([(x["hp"], x["w"]) for x in window])),
            "health_spread": round((wquantile([(x["hp"], x["w"]) for x in window], 0.8) - wquantile([(x["hp"], x["w"]) for x in window], 0.2))
                                   / 2 / max(1.0, wmedian([(x["hp"], x["w"]) for x in window])), 3),
            "dmg": round(wmedian([(x["dmg"], x["w"]) for x in window]), 1),
            "swing": round(wmedian([(x["swing"], x["w"]) for x in window]), 2),
            "armor": round(wmedian([(x["armor"], x["w"]) for x in window])),
            "caster_share": round(sum(x["w"] for x in cast) / sum(x["w"] for x in window), 3),
            "melee_health": round(wmedian([(x["hp"], x["w"]) for x in melee])) if melee else None,
            "melee_dmg": round(wmedian([(x["dmg"], x["w"]) for x in melee]), 1) if melee else None,
            "caster_health": round(wmedian([(x["hp"], x["w"]) for x in cast])) if cast else None,
            "caster_dmg": round(wmedian([(x["dmg"], x["w"]) for x in cast]), 1) if cast else None,
            "templates": len(window), "spawns": sum(x["w"] for x in window),
        }
    anchors[1] = {**anchors[5], "health": round(wmedian([(x["hp"], x["w"]) for x in per_level[1] + per_level[2]])),
                  "dmg": round(wmedian([(x["dmg"], x["w"]) for x in per_level[1] + per_level[2]]), 1),
                  "armor": round(wmedian([(x["armor"], x["w"]) for x in per_level[1] + per_level[2]]))}
    out = {"source": "cmangos/classic-db Full_DB/ClassicDB_1_12_1_z2815.sql.gz (Classic 1.12 creature_template + creature spawns), "
                     "extracted 2026-09-26 by _reference/data/fightlab/mob_stats.py; WoW: Forever mob stats are unverified (server side, not in the beta client)",
           "filter": "Rank 0, combat creature types, not civilian, no NPC flags, attackable, MaxMeleeDmg > 0, spawned at least once; weighted by spawn count; level = template average",
           "fields": {"health": "weighted median of (MinLevelHealth+MaxLevelHealth)/2", "health_spread": "half the p20-p80 health band as a fraction of the median",
                      "dmg": "weighted median of the average melee swing (MinMeleeDmg..MaxMeleeDmg x DamageMultiplier; base attack power already included)",
                      "swing": "median MeleeBaseAttackTime in seconds", "armor": "weighted median Armor",
                      "caster_share": "share of spawns whose UnitClass is mage (8) or paladin (2)", "melee_*/caster_*": "the same medians split by that class"},
           "anchors": {str(k): v for k, v in sorted(anchors.items())},
           "by_level": {str(k): {kk: (round(vv, 3) if isinstance(vv, float) else vv) for kk, vv in v.items()} for k, v in table.items()},
           "mobs": len(mobs), "spawns": sum(r["Spawns"] for r in mobs)}
    print(f"{len(mobs)} normal outdoor mob templates, {out['spawns']} spawns")
    print(f"{'L':>3} {'tmpl':>5} {'spawns':>6} {'health':>7} {'p20-p80':>11} {'dmg':>6} {'swing':>5} {'dps':>6} {'armor':>6} {'casters':>7} {'melee hp':>8} {'caster hp':>9} {'old hp':>7} {'old dmg':>7}")
    sys.path.insert(0, str(HERE))
    for L in sorted(table):
        if L % 5 and L not in (1, 2, 3):
            continue
        r = table[L]
        old_hp = 1.0 * L * L + 10 * L + 60
        old_dmg = 0.055 * L * L + 1.5 * L + 5
        print(f"{L:>3} {r['templates']:>5} {r['spawns']:>6} {r['health']:>7.0f} {r['health_p20']:>5.0f}-{r['health_p80']:<5.0f} {r['dmg']:>6.1f} {r['swing']:>5.1f} {r['dps']:>6.1f} {r['armor']:>6.0f} "
              f"{r['caster_share'] * 100:>6.0f}% {r['melee_health'] or 0:>8.0f} {r['caster_health'] or 0:>9.0f} {old_hp:>7.0f} {old_dmg:>7.1f}")
    print("anchors (every 5 levels, window +-2):")
    for L, a in sorted(anchors.items()):
        print(f"  {L:>2}: health {a['health']} (+-{a['health_spread'] * 100:.0f}%), dmg {a['dmg']} per {a['swing']}s swing, armor {a['armor']}, casters {a['caster_share'] * 100:.0f}% "
              f"(melee hp {a['melee_health']} / dmg {a['melee_dmg']}; caster hp {a['caster_health']} / dmg {a['caster_dmg']}) from {a['templates']} templates, {a['spawns']} spawns")
    if write:
        OUT.write_text(json.dumps(out, indent=1), encoding="utf-8")
        print(f"wrote {OUT.relative_to(ROOT)}")
    return out


def wquantile(pairs, q):
    pairs = sorted(pairs)
    tot = sum(w for _, w in pairs)
    acc = 0.0
    for v, w in pairs:
        acc += w
        if acc >= tot * q:
            return v
    return pairs[-1][0]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--extract", help="path of the cmangos classic-db SQL dump: writes the raw CSV")
    ap.add_argument("--write", action="store_true")
    a = ap.parse_args()
    if a.extract:
        extract(a.extract)
    if not RAW.exists():
        raise SystemExit(f"{RAW} missing: run with --extract <ClassicDB sql>")
    build(load_rows(), a.write)


if __name__ == "__main__":
    main()
