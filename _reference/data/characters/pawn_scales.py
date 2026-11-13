"""Pawn 2.14.2's built-in Forever weights, read and applied the way Pawn applies them (2026-11-13; _reference/forever-stats.md row 14).
Shared by characters/pawn_compare.py (leveling) and raidsim/pawn_raid_compare.py (level 60); no fight-lab or simulator imports."""
import json
import pathlib
import re
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
DATA = pathlib.Path(__file__).resolve().parent.parent

PAWN = pathlib.Path("D:/World of Warcraft/_forever_/Interface/AddOns/Pawn")
# Pawn's Forever per-percent factors (ClassicHawsJon.lua "if VgerCore.IsClassic or VgerCore.IsForever")
PER = {"HitRatingPer": 9.37931, "SpellHitRatingPer": 8, "CritRatingPer": 8.5, "SpellCritRatingPer": 8, "HasteRatingPer": 8.03,
       "SpellHasteRatingPer": 8.03, "ExpertiseRatingPer": 2.34483, "ArmorPenetrationPer": 3.75, "SpellPenetrationPer": 1,
       "DefenseRatingPer": 1.5, "DodgeRatingPer": 9.44, "ParryRatingPer": 9.44, "BlockRatingPer": 6.9}
PAWN_CLASS = {"warrior": 1, "paladin": 2, "hunter": 3, "rogue": 4, "priest": 5, "shaman": 7, "mage": 8, "warlock": 9, "druid": 11}
TREES = {"warrior": ["Arms", "Fury", "Protection"], "paladin": ["Holy", "Protection", "Retribution"],
         "hunter": ["Beast Mastery", "Marksmanship", "Survival"], "rogue": ["Assassination", "Combat", "Subtlety"],
         "priest": ["Discipline", "Holy", "Shadow"], "shaman": ["Elemental", "Enhancement", "Restoration"], "mage": ["Arcane", "Fire", "Frost"],
         "warlock": ["Affliction", "Demonology", "Destruction"], "druid": ["Balance", "Feral Combat", "Restoration"]}
PAWN_SCHOOL = {6: "ArcaneSpellDamage", 7: "FireSpellDamage", 8: "FrostSpellDamage", 9: "HolySpellDamage", 10: "NatureSpellDamage",
               11: "ShadowSpellDamage"}
PAWN_STAT = {0: "Strength", 1: "Agility", 2: "Stamina", 3: "Intellect", 13: "Spirit", 31: "Mp5", 12: "SpellPenetration", 14: "Ap",
             15: "Rap", 16: "FeralAp", 17: "HitRating", 18: "CritRating", 19: "HasteRating", 21: "ExpertiseRating", 22: "DefenseRating",
             23: "BlockRating", 24: "BlockValue", 25: "DodgeRating", 26: "ParryRating"}


# ------------------------------------------------------------------ Pawn
def pawn_scales():
    """{(Pawn class id, spec id): {stat: value}} from Pawn's Forever weights, after PawnCorrectScaleErrors' Forever rules."""
    s = (PAWN / "ClassicHawsJon.lua").read_text(encoding="utf-8", errors="replace")
    i = s.index("elseif VgerCore.IsForever then")
    j = s.index("elseif VgerCore.IsWrath then", i)
    block = s[i:j]
    out = {}
    for m in re.finditer(r"PawnAddPluginScaleFromTemplate\(\s*ScaleProviderName,\s*(\d+),[^\n]*\n\s*(\d+),[^\n]*\n\s*\{(.*?)\}\s*\)", block, re.S):
        cid, sid, body = int(m.group(1)), int(m.group(2)), m.group(3)
        vals = {}
        for k, v in re.findall(r"(\w+)\s*=\s*([^,}\n]+)", body):
            v = v.strip()
            if v == "PawnIgnoreStatValue":
                continue
            try:
                vals[k] = float(eval(v, {"__builtins__": {}}, PER))
            except Exception:
                continue
        vals.pop("SpellPower", None)   # Pawn.lua PawnCorrectScaleErrors: only Wrath and later keep SpellPower
        for prim, sec in (("HitRating", "SpellHitRating"), ("CritRating", "SpellCritRating"), ("HasteRating", "SpellHasteRating")):
            if sec in vals:   # PawnCombineStats: the larger of the two, the secondary dropped (Forever merges melee and spell ratings)
                vals[prim] = max(vals.get(prim, 0.0), vals.pop(sec))
        for k in ("Mana", "Health", "BaseArmor", "BonusArmor"):
            vals.pop(k, None)
        out[(cid, sid)] = vals
    return out


def pawn_item_stats(st, weapon_dps, ranged):
    """An item version's stats as Pawn's tooltip parser reads them on Forever."""
    o = {}
    for k, v in st.items():
        k = int(k)
        if k in PAWN_STAT:
            o[PAWN_STAT[k]] = o.get(PAWN_STAT[k], 0) + v
        elif k in PAWN_SCHOOL:
            o[PAWN_SCHOOL[k]] = o.get(PAWN_SCHOOL[k], 0) + v
        elif k in (27, 28):
            o["Armor"] = o.get("Armor", 0) + v
    h, d = st.get("4", st.get(4, 0)) or 0, st.get("5", st.get(5, 0)) or 0
    if h and h == d:   # "+N Spell Power" (damage and healing alike): Pawn's SpellPower stat, worth 0 on Forever
        o["SpellPower"] = h
    else:
        if d:
            o["SpellDamage"] = d
        if h:
            o["Healing"] = h
    if weapon_dps:
        o["RangedDps" if ranged else "MeleeDps"] = weapon_dps
        o["Dps"] = weapon_dps
    return o


def pawn_score(scale, ps):
    return sum(scale.get(k, 0.0) * v for k, v in ps.items())


def tree_points(cls, alloc):
    """Points per tree of an allocation, either form: {tree: [[talent, rank]]} (a build's) or {talent: rank} (run.allocation_at,
    run.alloc_of). 2026-11-13 fix: tree_of had passed the {talent: rank} form to spec_modes.tree_points, which reads only the first form,
    so every tree read 0 and Pawn's first-tree scale was used for every spec (Retribution scored with Holy's, Feral with Balance's)."""
    import spec_modes as SM
    if alloc and all(isinstance(v, list) for v in alloc.values()):
        return SM.tree_points(cls, {"allocation": alloc})
    data = json.loads((DATA / "forever-talents" / f"{cls}.json").read_text(encoding="utf-8"))
    where = {t["name"]: tr["name"] for tr in data["trees"] for t in tr["talents"]}
    pts = {tr["name"]: 0 for tr in data["trees"]}
    for n, r in alloc.items():
        if n in where:
            pts[where[n]] += r
    missing = [n for n in alloc if n not in where]
    if missing:
        raise ValueError(f"{cls}: talents not in the trees: {missing}")
    return pts


def tree_of(cls, alloc):
    """The tree with the most points (Pawn's automatic scale: the player's primary talent tree)."""
    pts = tree_points(cls, alloc)
    order = TREES[cls]
    best = max(order, key=lambda t: pts.get(t, 0))
    return order.index(best) + 1, best


def pawn_spec(cls, tree_index, tree_name, spec):
    if cls == "druid" and tree_name == "Feral Combat":
        return 2   # Feral (Damage): leveling plays the cat
    if cls == "druid" and tree_name == "Restoration":
        return 4
    return tree_index


