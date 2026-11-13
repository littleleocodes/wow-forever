"""Forever's own items at every level, from the client's tables (2026-11-13, the gear add-on and the leveling ranking).

    python _reference/data/characters/forever_items.py --check      # compare with the simulator's item database where both have an item

The simulator's item database (assets/database/db.json) starts at item level 40: it has no green below required level 35, so the
fight lab's leveling gear (fightlab/gear_stats.py) came from Classic 1.12's fixed-stat greens, without the random-suffix greens ("of
Frozen Wrath") that carry most of a Forever caster's Spell Power (Arcea at 30: 77 Spell Power; the standard gear: 0). This reads the
client's tables (product wowf, build BUILD, downloaded from wago.tools into ~/.wow-forever-tools/wago/, never the repository) by the
simulator's own rules (wowsims/forever tools/database: dbc/item.go GetStats, GetScaledStat, GetArmorValue, addCasterSpellPower,
GetRandomSuffixType, GetWeaponTypes; dbc/item_damage.go; tables.go randomSuffixNodes and LoadAndWriteRawRandomSuffixes) and returns
items in db.json's shape, so characters/pawn_compare.item_pool and the rest read them unchanged:
- a stat = round(allocation x RandPropPoints[item level][quality][slot type] / 10000);
- caster weapons (Flags_4 0x200 / 0x400) add 20000 x budget / 10000 Spell Power, or 37600 healing and a third of it as spell damage;
- armor = ItemArmorTotal x ItemArmorQuality x ArmorLocation (shields: ItemArmorShield), weapon damage from the ItemDamage tables (the
  caster tables for Flags_1 0x200, a reduced share for Flags_4 0x100 or a suffix with a reduced-caster-DPS row);
- random suffixes = the bonus lists of the item's bonus tree (item context 0) with stat rows and a suffix name.
Sources are not in the client tables: an item carries no "sources" (reputation rewards, MinFactionID > 0, and PvP rewards,
RequiredPVPRank > 0, are left out instead).
"""
import argparse
import csv
import json
import math
import pathlib
import sys

BUILD = "1.60.1.70888"
WAGO = pathlib.Path.home() / ".wow-forever-tools" / "wago"
SIM = pathlib.Path.home() / ".wow-forever-tools" / "wowsims-forever"   # its shield block value table (dbc/GameTables)

ITEM_BONUS_STAT, ITEM_BONUS_SUFFIX, ITEM_BONUS_REDUCED_CASTER_DPS = 2, 5, 54
# ITEM_MOD -> proto Stat indices (dbc/maps.go MapBonusStatIndexToStats; proto/common.proto Stat)
MOD = {0: [30], 1: [29], 3: [1], 4: [0], 5: [3], 6: [13], 7: [2], 12: [22], 13: [25], 14: [26], 15: [23], 16: [17], 17: [17], 18: [17], 31: [17],
       19: [18], 20: [18], 21: [18], 32: [18], 28: [19], 29: [19], 30: [19], 36: [19], 37: [21], 44: [20], 38: [14, 15], 39: [15], 40: [16],
       41: [4], 42: [5], 45: [5, 4], 43: [31], 47: [12], 48: [24], 50: [28], 51: [33], 52: [34], 54: [36], 55: [35], 56: [32],
       83: [37], 84: [9], 85: [7], 86: [10], 87: [8], 88: [11], 89: [6]}
MP5 = 31   # db.json keeps mp5 at index 31 (item_pool.STAT); the proto enum's 31 is unused
INV = dict(HEAD=1, NECK=2, SHOULDERS=3, BODY=4, CHEST=5, WAIST=6, LEGS=7, FEET=8, WRISTS=9, HANDS=10, FINGER=11, TRINKET=12, WEAPON=13,
           SHIELD=14, RANGED=15, CLOAK=16, TWOHAND=17, BAG=18, TABARD=19, ROBE=20, MAINHAND=21, OFFHAND=22, HOLDABLE=23, AMMO=24, THROWN=25,
           RANGEDRIGHT=26, QUIVER=27, RELIC=28)
ITEM_TYPE = {1: 1, 2: 2, 3: 3, 5: 5, 6: 8, 7: 9, 8: 10, 9: 6, 10: 7, 11: 11, 12: 12, 13: 13, 14: 13, 15: 14, 16: 4, 17: 13, 20: 5, 21: 13, 22: 13,
             23: 13, 25: 14, 26: 14, 28: 14}
W_AXE, W_AXE2, W_BOW, W_GUN, W_MACE, W_MACE2, W_POLEARM, W_SWORD, W_SWORD2, W_WARGLAIVE, W_STAFF, W_EXOTIC, W_EXOTIC2, W_FIST, W_MISC, \
    W_DAGGER, W_THROWN, W_SPEAR, W_CROSSBOW, W_WAND, W_FISHING = range(21)
WEAPON_TYPE = {W_AXE: 1, W_AXE2: 1, W_MACE: 4, W_MACE2: 4, W_POLEARM: 6, W_SWORD: 9, W_SWORD2: 9, W_WARGLAIVE: 6, W_STAFF: 8, W_FIST: 3,
               W_DAGGER: 2}
RANGED_TYPE = {W_BOW: 1, W_CROSSBOW: 2, W_GUN: 3, W_THROWN: 4, W_WAND: 5}
A_MISC, A_CLOTH, A_LEATHER, A_MAIL, A_PLATE, A_COSMETIC, A_SHIELD, A_LIBRAM, A_IDOL, A_TOTEM, A_SIGIL, A_RELIC = range(12)
CLASS_WEAPON, CLASS_ARMOR = 2, 4


def read(table):
    p = WAGO / f"{table}-{BUILD}.csv"
    with open(p, encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def num(x):
    try:
        return int(x)
    except ValueError:
        return float(x)


_CACHE = {}


def tables():
    if _CACHE:
        return _CACHE
    sparse = {int(r["ID"]): r for r in read("ItemSparse")}
    item = {int(r["ID"]): r for r in read("Item")}
    rpp = {int(r["ID"]): {q: [int(r[f"{name}_{i}"]) for i in range(5)] for q, name in ((2, "Good"), (3, "Superior"), (4, "Epic"))} for r in read("RandPropPoints")}
    aq = {int(r["ID"]): [float(r[f"Qualitymod_{i}"]) for i in range(7)] for r in read("ItemArmorQuality")}
    at = {int(r["ItemLevel"]): r for r in read("ItemArmorTotal")}
    ash = {int(r["ItemLevel"]): [float(r[f"Quality_{i}"]) for i in range(7)] for r in read("ItemArmorShield")}
    loc = {int(r["ID"]): [float(r["Clothmodifier"]), float(r["Leathermodifier"]), float(r["Chainmodifier"]), float(r["Platemodifier"])]
           for r in read("ArmorLocation")}
    dmg = {}
    for t in ("ItemDamageOneHand", "ItemDamageOneHandCaster", "ItemDamageTwoHand", "ItemDamageTwoHandCaster", "ItemDamageRanged",
              "ItemDamageThrown", "ItemDamageWand"):
        dmg[t] = {int(r["ItemLevel"]): [float(r[f"Quality_{i}"]) for i in range(7)] for r in read(t)}
    # random suffixes: bonus lists of item context 0 with stat rows and a suffix name (tables.go randomSuffixNodes)
    bonus = {}
    for r in read("ItemBonus"):
        bonus.setdefault(int(r["ParentItemBonusListID"]), []).append(r)
    names = {int(r["ID"]): r["Description_lang"] for r in read("ItemNameDescription")}
    lists = {}
    for lid, rows in bonus.items():
        types = {int(r["Type"]) for r in rows}
        if ITEM_BONUS_STAT in types and ITEM_BONUS_SUFFIX in types:
            rows = sorted(rows, key=lambda r: int(r["OrderIndex"]))
            lists[lid] = {"id": lid, "name": next(names.get(int(r["Value_0"]), "") for r in rows if int(r["Type"]) == ITEM_BONUS_SUFFIX),
                          "mods": [(int(r["Value_0"]), int(r["Value_1"])) for r in rows if int(r["Type"]) == ITEM_BONUS_STAT],
                          "reduced_caster_dps": ITEM_BONUS_REDUCED_CASTER_DPS in types}
    nodes = {}
    for r in read("ItemBonusTreeNode"):
        if int(r["ItemContext"]) == 0 and int(r["ChildItemBonusListID"]) in lists:
            nodes.setdefault(int(r["ParentItemBonusTreeID"]), set()).add(int(r["ChildItemBonusListID"]))
    suffixes_of = {}
    for r in read("ItemXBonusTree"):
        for lid in nodes.get(int(r["ItemBonusTreeID"]), ()):
            suffixes_of.setdefault(int(r["ItemID"]), set()).add(lid)
    block = {}
    with open(SIM / "tools" / "database" / "dbc" / "GameTables" / "ShieldBlockRegular.txt", encoding="utf-8") as f:
        next(f)
        for line in f:
            parts = line.split()
            if parts and parts[0].isdigit():
                block[int(parts[0])] = [float(x) for x in parts[1:8]]
    _CACHE.update(sparse=sparse, item=item, rpp=rpp, aq=aq, at=at, ash=ash, loc=loc, dmg=dmg, lists=lists, suffixes_of=suffixes_of, block=block)
    return _CACHE


def suffix_type(cls_id, sub, inv):
    if cls_id == CLASS_WEAPON:
        if sub in (W_AXE2, W_MACE2, W_POLEARM, W_SWORD2, W_STAFF):
            return 0
        if sub in (W_THROWN, W_GUN, W_BOW, W_CROSSBOW, W_WAND):
            return 4
        return 3
    if cls_id == CLASS_ARMOR:
        if inv in (INV["HEAD"], INV["CHEST"], INV["LEGS"], INV["ROBE"]):
            return 0
        if inv in (INV["SHOULDERS"], INV["WAIST"], INV["FEET"], INV["HANDS"], INV["TRINKET"]):
            return 1
        if inv in (INV["NECK"], INV["OFFHAND"], INV["HOLDABLE"], INV["FINGER"], INV["CLOAK"], INV["WRISTS"], INV["SHIELD"], INV["RELIC"]):
            return 2
    return -1


def add(stats, mod, value):
    for s in MOD.get(mod, ()):
        k = MP5 if mod == 43 else s
        stats[k] = stats.get(k, 0) + value


def weapon_table(inv, sub, flags1):
    caster = bool(flags1 & 0x200)
    if inv in (INV["WEAPON"], INV["MAINHAND"], INV["OFFHAND"]):
        return "ItemDamageOneHandCaster" if caster else "ItemDamageOneHand"
    if inv == INV["TWOHAND"]:
        return "ItemDamageTwoHandCaster" if caster else "ItemDamageTwoHand"
    if inv in (INV["RANGED"], INV["THROWN"], INV["RANGEDRIGHT"]):
        if sub in (W_BOW, W_GUN, W_CROSSBOW):
            return "ItemDamageRanged"
        if sub == W_THROWN:
            return "ItemDamageThrown"
        if sub == W_WAND:
            return "ItemDamageWand"
    return None


def reduced_share(inv):
    if inv in (INV["WEAPON"], INV["MAINHAND"], INV["OFFHAND"]):
        return 2.0 / 3.0
    if inv == INV["TWOHAND"]:
        return 29.0 / 39.0
    return 1.0


def build_item(iid):
    """One item in db.json's shape, or None (not gear)."""
    T = tables()
    s, it = T["sparse"].get(iid), T["item"].get(iid)
    if s is None or it is None:
        return None
    cls_id, sub, inv = int(it["ClassID"]), int(it["SubclassID"]), int(s["InventoryType"])
    q, ilvl = int(s["OverallQualityID"]), int(s["ItemLevel"])
    name = s["Display_lang"]
    if q in (0, 7) or not name or not (cls_id in (CLASS_WEAPON, CLASS_ARMOR)) or inv not in ITEM_TYPE or ilvl not in T["rpp"]:
        return None
    if "Test" in name or name.startswith("QA") or name == "unused":
        return None
    st = suffix_type(cls_id, sub, inv)
    budget = T["rpp"][ilvl].get(q, [0] * 5)
    stats = {}
    for i in range(10):
        mod, alloc = int(s[f"StatModifier_bonusStat_{i}"]), num(s[f"StatPercentEditor_{i}"])
        if mod < 0 or not alloc or st < 0 or q not in (2, 3, 4):
            continue
        add(stats, mod, round(alloc * budget[st] * 0.0001))
    f1, f4 = int(s["Flags_1"]), int(s["Flags_4"])
    if (f4 & 0x200 or f4 & 0x400) and q in (2, 3, 4):
        b0 = budget[0]
        if f4 & 0x400:
            h = 37600 * b0 // 10000
            add(stats, 41, h)
            add(stats, 42, h // 3)
        else:
            add(stats, 45, 20000 * b0 // 10000)
    # armor
    armor = 0
    if cls_id == CLASS_ARMOR and q <= 6:
        if sub == A_SHIELD:
            row = T["ash"].get(ilvl)
            armor = int(math.floor(row[q] + 0.5)) if row else 0
        elif sub in (A_CLOTH, A_LEATHER, A_MAIL, A_PLATE) and inv in (1, 3, 5, 6, 7, 8, 9, 10, 16, 20):
            tot = T["at"].get(ilvl)
            qual = T["aq"].get(ilvl)
            slot = 5 if inv == 20 else inv
            if tot and qual and slot in T["loc"]:
                col = {A_CLOTH: "Cloth", A_LEATHER: "Leather", A_MAIL: "Mail", A_PLATE: "Plate"}[sub]
                armor = int(math.floor(float(tot[col]) * qual[q] * T["loc"][slot][sub - 1] + 0.5))
    if armor:
        stats[27] = stats.get(27, 0) + armor
    qm = float(s["QualityModifier"] or 0)
    if cls_id == CLASS_ARMOR and qm > 0:
        stats[28] = qm   # bonus armor: the quality modifier replaces a stat line's (dbc/item.go GetStats assigns it)
    if cls_id == CLASS_ARMOR and sub == A_SHIELD:
        bv = T["block"].get(ilvl)
        if bv:
            stats[24] = stats.get(24, 0) + bv[q]
    out = {"id": iid, "name": name, "quality": q, "reqLvl": int(s["RequiredLevel"]), "type": ITEM_TYPE[inv]}
    if cls_id == CLASS_ARMOR and sub in (A_CLOTH, A_LEATHER, A_MAIL, A_PLATE):
        out["armorType"] = sub
    # weapon kinds (dbc/item.go GetWeaponTypes)
    wt, hand, rng = 0, 0, 0
    if cls_id == CLASS_ARMOR:
        if sub == A_MISC and inv == INV["HOLDABLE"]:
            wt, hand = 5, 3
        rng = {A_TOTEM: 8, A_IDOL: 6, A_LIBRAM: 7, A_SIGIL: 9}.get(sub, 0)
        if sub == A_SHIELD:
            wt, hand = 7, 3
    elif cls_id == CLASS_WEAPON:
        if sub in RANGED_TYPE:
            rng = RANGED_TYPE[sub]
        elif sub in (W_AXE2, W_FISHING, W_SPEAR, W_STAFF, W_POLEARM, W_MACE2, W_EXOTIC2, W_SWORD2):
            hand, wt = 4, WEAPON_TYPE.get(sub, 0)
        elif sub in (W_EXOTIC, W_MACE, W_WARGLAIVE, W_FIST, W_SWORD, W_DAGGER, W_AXE):
            hand = 2 if inv == INV["WEAPON"] else (3 if inv == INV["OFFHAND"] else 1)
            wt = WEAPON_TYPE.get(sub, 0)
    if wt:
        out["weaponType"] = wt
    if hand:
        out["handType"] = hand
    if rng:
        out["rangedWeaponType"] = rng
    so = {"ilvl": ilvl, "stats": {str(k): v for k, v in sorted(stats.items())}}
    if st >= 0:
        so["randPropPoints"] = budget[st]
    if cls_id == CLASS_WEAPON:
        tname = weapon_table(inv, sub, f1)
        row = T["dmg"].get(tname, {}).get(ilvl) if tname else None
        if row:
            dps = row[min(q, 6)]
            if f4 & 0x100:
                dps *= reduced_share(inv)
            speed = int(s["ItemDelay"]) / 1000.0
            var = float(s["DmgVariance"] or 0)
            qmod = qm
            lo = dps * speed * (1 - var / 2) + qmod * speed
            hi = dps * speed * (1 + var / 2) + qmod * speed
            so["weaponDamageMin"] = math.floor(max(lo, 1) if lo >= 0 else 1)
            so["weaponDamageMax"] = math.floor((hi if hi >= 0 else 1) + 0.5)
            out["weaponSpeed"] = speed
    out["scalingOptions"] = {"0": so}
    sufs = sorted(T["suffixes_of"].get(iid, ()))
    if sufs:
        out["randomSuffixOptions"] = sufs
    cm = int(s["AllowableClass"])
    if cm not in (-1, 0) and cm & 0x7FF != 0x7FF:
        out["classAllowlist"] = [c for c in range(1, 12) if cm & (1 << (c - 1))]
    if int(s["MinFactionID"]) > 0:
        out["rep"] = True
    if int(s["RequiredPVPRank"]) > 0:
        out["pvp"] = True
    if int(s["Flags_0"]) & 0x80000:
        out["unique"] = True
    return out


def suffix_list():
    """db.json's randomSuffixes: {id, name, stats: allocation per proto stat index (db.json's mp5 index 31)}."""
    out = []
    for lid, L in sorted(tables()["lists"].items()):
        st = [0] * 40
        for mod, alloc in L["mods"]:
            for s in MOD.get(mod, ()):
                st[MP5 if mod == 43 else s] += alloc
        out.append({"id": lid, "name": L["name"], "stats": st, "reducedCasterDps": L["reduced_caster_dps"]})
    return out


CLASSIC = pathlib.Path(__file__).resolve().parents[1] / "raw" / "2026-09-26-cmangos-classic-db-z2815"


def classic_rows():
    """Classic 1.12's armor and weapons (cmangos item_stats.csv) and their on-equip spell power (item_spell_power.csv: aura 13 damage,
    135 healing)."""
    sp = {}
    with open(CLASSIC / "item_spell_power.csv", encoding="utf-8", newline="") as f:
        for r in csv.DictReader(f):
            sp[int(r["spell"])] = (int(r["aura"]), int(r["value"]), int(r["school_mask"]))
    with open(CLASSIC / "item_stats.csv", encoding="utf-8", newline="") as f:
        rows = list(csv.DictReader(f))
    return rows, sp


def classic_item(r, sp):
    """An item the client's tables lack (2026-11-13: about a third of the game's items, among them most random-suffix leveling
    greens: Elder's Sash, Durable Pants, Geomancer's Bracers): Classic's item level, required level, quality, slot and class, Forever's
    rules for the rest (armor and weapon damage from the item-level tables, random suffixes from the client's bonus trees, which list
    these items); fixed stat lines and on-equip spell power stay Classic's ("classic_stats": Forever retuned some, e.g. Silk Headband)."""
    T = tables()
    iid = int(r["entry"])
    cls_id, sub, inv, q, ilvl = int(r["class"]), int(r["subclass"]), int(r["InventoryType"]), int(r["Quality"]), int(r["ItemLevel"])
    if q not in (2, 3, 4) or cls_id not in (CLASS_WEAPON, CLASS_ARMOR) or inv not in ITEM_TYPE or ilvl not in T["rpp"]:
        return None
    stats = {}
    for i in range(1, 11):
        t, v = int(r[f"stat_type{i}"]), int(r[f"stat_value{i}"])
        if t and v:
            add(stats, t, v)
    for i in range(1, 6):
        sid = int(r.get(f"spellid_{i}") or 0)
        if sid in sp:
            aura, v, mask = sp[sid]
            if aura == 135:
                add(stats, 41, v)
            elif aura == 13:
                school = {2: 84, 4: 85, 8: 86, 16: 87, 32: 88, 64: 89}.get(mask)
                if school and mask != 126:
                    add(stats, school, v)
                else:
                    add(stats, 42, v)
    x = {"id": iid, "name": r["name"], "quality": q, "reqLvl": int(r["RequiredLevel"]), "type": ITEM_TYPE[inv], "classic_stats": True}
    fake = {"InventoryType": str(inv), "OverallQualityID": str(q), "ItemLevel": str(ilvl), "Display_lang": r["name"], "Flags_0": "0",
            "Flags_1": "0", "Flags_4": "0", "QualityModifier": "0", "ItemDelay": r["delay"] or "0", "DmgVariance": "0",
            "AllowableClass": r["AllowableClass"], "MinFactionID": "0", "RequiredPVPRank": "0", "RequiredLevel": r["RequiredLevel"],
            **{f"StatModifier_bonusStat_{i}": "-1" for i in range(10)}, **{f"StatPercentEditor_{i}": "0" for i in range(10)}}
    T["sparse"][iid] = fake
    T["item"].setdefault(iid, {"ClassID": str(cls_id), "SubclassID": str(sub)})
    try:
        b = build_item(iid)
    finally:
        del T["sparse"][iid]
    if b is None:
        return None
    so = b["scalingOptions"]["0"]
    for k, v in stats.items():
        so["stats"][str(k)] = so["stats"].get(str(k), 0) + v
    if cls_id == CLASS_WEAPON and r["dmg_max1"] not in ("", "0"):   # Classic's damage range (the tables' variance is unknown here)
        so["weaponDamageMin"], so["weaponDamageMax"] = float(r["dmg_min1"]), float(r["dmg_max1"])
    b.update(x)
    return b


def items(max_ilvl=None, classic=True):
    T = tables()
    out = []
    for iid in sorted(T["sparse"]):
        x = build_item(iid)
        if x and (max_ilvl is None or x["scalingOptions"]["0"]["ilvl"] <= max_ilvl):
            out.append(x)
    if classic:
        have = {x["id"] for x in out} | set(T["sparse"])
        rows, sp = classic_rows()
        for r in rows:
            if int(r["entry"]) in have:
                continue
            x = classic_item(r, sp)
            if x and (max_ilvl is None or x["scalingOptions"]["0"]["ilvl"] <= max_ilvl):
                out.append(x)
    return out


def check():
    """Every item both databases have: our stats, armor and weapon damage against db.json's."""
    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
    import item_pool as IP
    db = IP.sim_db()
    mine = {x["id"]: x for x in items(classic=False)}
    n = same = 0
    diffs = []
    for it in db["items"]:
        x = mine.get(it["id"])
        if x is None:
            continue
        n += 1
        a = {k: v for k, v in ((it.get("scalingOptions") or {}).get("0") or {}).get("stats", {}).items() if v}
        b = {k: v for k, v in x["scalingOptions"]["0"]["stats"].items() if v}
        sa, sb = (it.get("scalingOptions") or {}).get("0") or {}, x["scalingOptions"]["0"]
        wa = (sa.get("weaponDamageMin"), sa.get("weaponDamageMax"))
        wb = (sb.get("weaponDamageMin"), sb.get("weaponDamageMax"))
        ok = a == b and (wa == wb or wa == (None, None)) and sorted(it.get("randomSuffixOptions") or []) == x.get("randomSuffixOptions", [])
        same += ok
        if not ok and len(diffs) < 12:
            diffs.append((it["id"], it["name"], a, b, wa, wb))
    print(f"{n} items in both; {same} identical ({100 * same / max(1, n):.1f}%)")
    for d in diffs:
        print("  ", d)
    sa = {s["id"]: s for s in db.get("randomSuffixes") or []}
    sb = {s["id"]: s for s in suffix_list()}
    both = set(sa) & set(sb)
    eq = sum(1 for k in both if [round(v) for v in sa[k]["stats"][:40]] == sb[k]["stats"][:len(sa[k]["stats"][:40])] or
             {i: v for i, v in enumerate(sa[k]["stats"]) if v} == {i: v for i, v in enumerate(sb[k]["stats"]) if v})
    print(f"random suffixes: db.json {len(sa)}, ours {len(sb)}, in both {len(both)}, identical {eq}")


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--check", action="store_true")
    a = ap.parse_args()
    if a.check:
        check()
