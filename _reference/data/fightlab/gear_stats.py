"""Gear by level from the Classic 1.12 item database: what a leveling character wears in greens, and what dungeon blues add.

    python _reference/data/fightlab/gear_stats.py --extract <ClassicDB_1_12_1_z2815.sql>   # SQL dump -> raw CSVs (archived)
    python _reference/data/fightlab/gear_stats.py --write                                   # raw CSVs -> gear_stats.json + tables

Source: cmangos/classic-db `item_template` (every 1.12 item with its fixed stats, armor, weapon damage and speed) and
`quest_template` (reward item ids, kept for reference). Raw extracts: `_reference/data/raw/2026-09-26-cmangos-classic-db-z2815/`
`item_stats.csv` (armor and weapons of green or better quality) and `quest_rewards.csv`.

Model ("greens"): at level L a character fills every slot with a typical good pick among the green items with fixed stats
(quest rewards, vendor and crafted greens; world-drop greens with random suffixes carry their stats elsewhere and are not
in this pool) whose required level lies in [L - GEAR_LAG - 2, L - GEAR_LAG + 3] (GEAR_LAG = 4: items are picked up a few
levels after they become wearable and kept for a while; the window widens when it holds fewer than MIN_ITEMS items).
"Typical good pick" = per slot, rank the items wearable by the class by the class's stat weights and take the median of
the better half (a player chooses among rewards but does not see them all). "Blues" are the same over blue items of any
source (dungeon drops, rare quest rewards), never below the greens. Weapons: the median dps of the class's weapon type in the window.
WoW: Forever caveat: Classic Era items; Forever adds and retunes items (unverified). Knobs: GEAR_LAG, MIN_ITEMS.
"""
import argparse
import csv
import json
import pathlib
import statistics
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[2]
RAW = ROOT / "_reference/data/raw/2026-09-26-cmangos-classic-db-z2815"
OUT = HERE / "gear_stats.json"
sys.path.insert(0, str(HERE))
from mob_stats import sql_tuples  # noqa: E402

GEAR_LAG = 4
MIN_ITEMS = 4
STAT_NAMES = {3: "agility", 4: "strength", 5: "intellect", 6: "spirit", 7: "stamina"}
EXTRA_STATS = ("spell_power", "healing")   # from the items' on-equip spells (spell_template auras 13 and 135)
SLOTS = {1: "head", 2: "neck", 3: "shoulder", 5: "chest", 20: "chest", 6: "waist", 7: "legs", 8: "feet", 9: "wrist", 10: "hands",
         11: "finger", 16: "back", 13: "one-hand", 21: "main-hand", 22: "off-hand weapon", 17: "two-hand", 14: "shield", 23: "held",
         15: "ranged", 26: "ranged", 25: "thrown", 18: "bag"}
ARMOR_SUB = {0: "misc", 1: "cloth", 2: "leather", 3: "mail", 4: "plate", 6: "shield"}
WEAPON_SUB = {0: "1h", 1: "2h", 2: "ranged", 3: "ranged", 4: "1h", 5: "2h", 6: "2h", 7: "1h", 8: "2h", 10: "2h", 13: "1h", 15: "dagger",
              16: "thrown", 18: "ranged", 19: "wand", 20: "fishing"}
ARMOR_SLOTS = ["head", "shoulder", "chest", "waist", "legs", "feet", "wrist", "hands"]
CLASS_BIT = {"warrior": 1, "paladin": 2, "hunter": 4, "rogue": 8, "priest": 16, "shaman": 64, "mage": 128, "warlock": 256, "druid": 1024}
CLASS_ARMOR = {"mage": [(1, "cloth")], "priest": [(1, "cloth")], "warlock": [(1, "cloth")], "rogue": [(1, "leather")], "druid": [(1, "leather")],
               "hunter": [(1, "leather"), (40, "mail")], "shaman": [(1, "leather"), (40, "mail")], "warrior": [(1, "mail"), (40, "plate")],
               "paladin": [(1, "mail"), (40, "plate")]}
CLASS_WEAPON = {"mage": "wand", "priest": "wand", "warlock": "wand", "rogue": "1h", "druid": "2h", "hunter": "ranged", "shaman": "2h",
                "warrior": "2h", "paladin": "2h"}
# what the class values on a piece of gear (a player's pick); stamina counts for everyone
WEIGHTS = {"mage": {"intellect": 1.0, "spirit": 0.7, "stamina": 0.5, "spell_power": 1.2}, "priest": {"intellect": 1.0, "spirit": 0.8, "stamina": 0.5, "spell_power": 1.0, "healing": 0.3},
           "warlock": {"intellect": 1.0, "spirit": 0.5, "stamina": 0.6, "spell_power": 1.2}, "rogue": {"agility": 1.0, "strength": 0.6, "stamina": 0.5},
           "hunter": {"agility": 1.0, "strength": 0.3, "stamina": 0.5, "intellect": 0.2}, "warrior": {"strength": 1.0, "agility": 0.5, "stamina": 0.6},
           "paladin": {"strength": 1.0, "agility": 0.3, "stamina": 0.5, "intellect": 0.4, "spell_power": 0.3}, "shaman": {"strength": 1.0, "agility": 0.4, "stamina": 0.5, "intellect": 0.4, "spell_power": 0.5},
           "druid": {"strength": 0.8, "agility": 1.0, "stamina": 0.5, "intellect": 0.2}}
LEVELS = list(range(10, 61, 5))


def create_columns(sql_path, table):
    cols, inside = [], False
    with open(sql_path, encoding="utf-8", errors="replace") as f:
        for line in f:
            if line.startswith(f"CREATE TABLE `{table}`"):
                inside = True
                continue
            if inside:
                s = line.strip()
                if s.startswith("`"):
                    cols.append(s.split("`")[1])
                elif s.startswith(")"):
                    break
    return cols


def extract(sql_path):
    icols = create_columns(sql_path, "item_template")
    qcols = create_columns(sql_path, "quest_template")
    scols = create_columns(sql_path, "spell_template")
    keep = ["entry", "class", "subclass", "name", "Quality", "InventoryType", "AllowableClass", "ItemLevel", "RequiredLevel", "armor", "delay",
            "dmg_min1", "dmg_max1", "RandomProperty", "bonding"] + [f"stat_type{i}" for i in range(1, 11)] + [f"stat_value{i}" for i in range(1, 11)] + \
           [f"spellid_{i}" for i in range(1, 6)] + [f"spelltrigger_{i}" for i in range(1, 6)]
    items, rewards, spells = [], [], {}
    with open(sql_path, encoding="utf-8", errors="replace") as f:
        for line in f:
            if line.startswith("INSERT INTO `item_template` VALUES"):
                for row in sql_tuples(line):
                    if len(row) != len(icols):
                        raise SystemExit(f"item_template: {len(row)} values vs {len(icols)} columns")
                    d = dict(zip(icols, row))
                    if int(d["class"]) not in (2, 4) or int(d["Quality"]) < 2:
                        continue
                    items.append([d[k] if d[k] is not None else "" for k in keep])
            elif line.startswith("INSERT INTO `spell_template` VALUES"):
                for row in sql_tuples(line):
                    d = dict(zip(scols, row))
                    for i in (1, 2, 3):
                        aura = int(d.get(f"EffectApplyAuraName{i}") or 0)
                        if aura in (13, 135):   # SPELL_AURA_MOD_DAMAGE_DONE / SPELL_AURA_MOD_HEALING_DONE (on-equip item spells)
                            spells.setdefault(int(d["Id"]), []).append((aura, int(d.get(f"EffectBasePoints{i}") or 0) + 1, int(d.get(f"EffectMiscValue{i}") or 0)))
            elif line.startswith("INSERT INTO `quest_template` VALUES"):
                for row in sql_tuples(line):
                    d = dict(zip(qcols, row))
                    ids = [d.get(f"RewChoiceItemId{i}") for i in range(1, 7)] + [d.get(f"RewItemId{i}") for i in range(1, 5)]
                    for x in ids:
                        if x and int(x) > 0:
                            rewards.append([d["entry"], d.get("MinLevel", 0), d.get("QuestLevel", 0), x])
    RAW.mkdir(parents=True, exist_ok=True)
    with open(RAW / "item_stats.csv", "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(keep)
        w.writerows(items)
    with open(RAW / "quest_rewards.csv", "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(["quest", "min_level", "quest_level", "item"])
        w.writerows(rewards)
    with open(RAW / "item_spell_power.csv", "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(["spell", "aura", "value", "school_mask"])
        for sid, effs in sorted(spells.items()):
            for aura, val, mask in effs:
                w.writerow([sid, aura, val, mask])
    print(f"wrote {len(items)} armor/weapon items (green+), {len(rewards)} quest reward links and {len(spells)} spell power / healing spells to {RAW.relative_to(ROOT)}")


SPELLS = {}


def load_spells():
    p = RAW / "item_spell_power.csv"
    if p.exists():
        with open(p, encoding="utf-8") as f:
            for d in csv.DictReader(f):
                SPELLS.setdefault(int(d["spell"]), []).append((int(d["aura"]), int(d["value"]), int(d["school_mask"])))
    return SPELLS


def load():
    load_spells()
    items = {}
    with open(RAW / "item_stats.csv", encoding="utf-8") as f:
        for d in csv.DictReader(f):
            it = {"entry": int(d["entry"]), "class": int(d["class"]), "subclass": int(d["subclass"]), "name": d["name"], "quality": int(d["Quality"]),
                  "inv": int(d["InventoryType"]), "allow": int(d["AllowableClass"] or -1), "ilvl": int(d["ItemLevel"] or 0),
                  "req": int(d["RequiredLevel"] or 0), "armor": float(d["armor"] or 0), "delay": float(d["delay"] or 0),
                  "dmg_min": float(d["dmg_min1"] or 0), "dmg_max": float(d["dmg_max1"] or 0), "random": int(d["RandomProperty"] or 0), "stats": {}}
            for i in range(1, 11):
                t, v = int(d[f"stat_type{i}"] or 0), float(d[f"stat_value{i}"] or 0)
                if t in STAT_NAMES and v:
                    it["stats"][STAT_NAMES[t]] = it["stats"].get(STAT_NAMES[t], 0) + v
            for i in range(1, 6):
                sid, trig = int(d.get(f"spellid_{i}") or 0), int(d.get(f"spelltrigger_{i}") or 0)
                if sid and trig == 1:   # on equip
                    for aura, val, mask in SPELLS.get(sid, []):
                        if aura == 13 and mask & 126:   # damage done, magic schools; school-specific items count half (one class uses them)
                            it["stats"]["spell_power"] = it["stats"].get("spell_power", 0.0) + val * (1.0 if (mask & 126) == 126 else 0.5)
                        elif aura == 135:
                            it["stats"]["healing"] = it["stats"].get("healing", 0.0) + val
            items[it["entry"]] = it
    rewards = set()
    with open(RAW / "quest_rewards.csv", encoding="utf-8") as f:
        for d in csv.DictReader(f):
            rewards.add(int(d["item"]))
    return items, rewards


def item_level_req(it):
    """Required level; items without one use the Classic rule of thumb ilvl - 5 (never below 1)."""
    return it["req"] if it["req"] > 0 else max(1, it["ilvl"] - 5)


def wearable(it, cls):
    return it["allow"] in (-1, 0) or bool(it["allow"] & CLASS_BIT[cls]) or it["allow"] == 1535 or it["allow"] == 2047


def better_half_median(its, score):
    its = sorted(its, key=score, reverse=True)
    top = its[: max(1, (len(its) + 1) // 2)]
    rec = {"n": len(its), "armor": statistics.median([i["armor"] for i in top])}
    for st in list(STAT_NAMES.values()) + list(EXTRA_STATS):
        rec[st] = statistics.median([i["stats"].get(st, 0.0) for i in top])
    if top[0]["class"] == 2:
        rec["dps"] = statistics.median([(i["dmg_min"] + i["dmg_max"]) / 2 / (i["delay"] / 1000.0) for i in top if i["delay"] > 0] or [0.0])
        rec["speed"] = statistics.median([i["delay"] / 1000.0 for i in top if i["delay"] > 0] or [0.0])
    rec["example"] = top[0]["name"]
    return rec


def pick(pool, cls, L, slot_key, kind):
    """Items of one slot (kind 'armor': (slot, armor class); 'other': slot; 'weapon': weapon type) for class `cls` at level L,
    within the lag window, widened until MIN_ITEMS items are found."""
    w = WEIGHTS[cls]

    def score(i):
        return sum(i["stats"].get(st, 0.0) * wt for st, wt in w.items())

    for widen in (0, 2, 4, 7):
        lo, hi = L - GEAR_LAG - 2 - widen, L - GEAR_LAG + 3 + widen
        its = []
        for it in pool:
            r = item_level_req(it)
            if not (lo <= r <= hi) or not wearable(it, cls):
                continue
            if kind == "armor" and it["class"] == 4 and SLOTS.get(it["inv"]) == slot_key[0] and ARMOR_SUB.get(it["subclass"]) == slot_key[1]:
                its.append(it)
            elif kind == "other" and it["class"] == 4 and SLOTS.get(it["inv"]) == slot_key:
                its.append(it)
            elif kind == "weapon" and it["class"] == 2 and WEAPON_SUB.get(it["subclass"]) == slot_key and it["delay"] > 0:
                its.append(it)
        if len(its) >= MIN_ITEMS:
            if kind == "weapon":   # a player takes what drops or the quest gives: the plain median dps of the window
                rec = {"n": len(its), "armor": 0.0, "dps": statistics.median([(i["dmg_min"] + i["dmg_max"]) / 2 / (i["delay"] / 1000.0) for i in its]),
                       "speed": statistics.median([i["delay"] / 1000.0 for i in its]), "example": sorted(its, key=lambda i: (i["dmg_min"] + i["dmg_max"]) / i["delay"])[len(its) // 2]["name"]}
                for st in list(STAT_NAMES.values()) + list(EXTRA_STATS):
                    rec[st] = statistics.median([i["stats"].get(st, 0.0) for i in its])
            else:
                rec = better_half_median(its, score)
            rec["window"] = f"{lo}-{hi}"
            return rec
    return None


def character(pool, cls, L, prev=None):
    """A slot keeps the previous level's pick when the new window has nothing better for the class (a hunter at 58 keeps a
    level-45 Agility piece rather than a Strength one)."""
    arm = [a for lv, a in CLASS_ARMOR[cls] if L >= lv][-1]
    w = WEIGHTS[cls]
    tot = {st: 0.0 for st in list(STAT_NAMES.values()) + list(EXTRA_STATS)}
    tot["armor"] = 0.0
    picks = {}
    prev = prev or {}

    def score(rec):
        return sum(rec.get(st, 0.0) * wt for st, wt in w.items()) + rec.get("armor", 0.0) / 100.0

    def keep_better(slot, rec):
        old = prev.get(slot)
        if rec is None:
            return old
        if old is not None and score(old) > score(rec):
            return dict(old, kept_from=old.get("window"))
        return rec

    for slot in ARMOR_SLOTS:
        rec = pick(pool, cls, L, (slot, arm), "armor")
        if rec is None and arm in ("mail", "plate"):
            rec = pick(pool, cls, L, (slot, "leather" if arm == "mail" else "mail"), "armor")
        rec = keep_better(slot, rec)
        if rec:
            picks[slot] = rec
            for k in tot:
                tot[k] += rec.get(k, 0.0)
    for slot, times in (("back", 1), ("neck", 1), ("finger", 2), ("shield", 1 if cls in ("warrior", "paladin", "shaman") and CLASS_WEAPON[cls] == "1h" else 0)):
        if not times:
            continue
        rec = keep_better(slot, pick(pool, cls, L, slot, "other"))
        if rec:
            picks[slot] = rec
            for k in tot:
                tot[k] += rec.get(k, 0.0) * times
    wt = CLASS_WEAPON[cls]
    wrec = pick(pool, cls, L, wt, "weapon")
    if wrec is not None and prev.get("weapon") is not None and prev["weapon"].get("dps", 0) > wrec.get("dps", 0):
        wrec = dict(prev["weapon"], kept_from=prev["weapon"].get("window"))
    if wrec:
        picks["weapon"] = wrec
        for k in list(STAT_NAMES.values()) + list(EXTRA_STATS):
            tot[k] += wrec.get(k, 0.0)
    if cls in ("mage", "priest", "warlock", "druid", "shaman", "paladin"):   # a caster's held off-hand item
        held = keep_better("held", pick(pool, cls, L, "held", "other"))
        if held and CLASS_WEAPON[cls] == "wand":
            picks["held"] = held
            for k in tot:
                tot[k] += held.get(k, 0.0)
    if cls == "rogue":   # dual wield: a second one-hander's stats
        w2 = pick(pool, cls, L, "dagger", "weapon") or wrec
        if w2:
            for k in list(STAT_NAMES.values()) + list(EXTRA_STATS):
                tot[k] += w2.get(k, 0.0)
    tot["weapon_dps"] = wrec["dps"] if wrec else 0.0
    tot["weapon_speed"] = wrec["speed"] if wrec else 0.0
    tot["slots"] = len(picks)
    return tot, picks


def build(write):
    items, rewards = load()
    greens = [it for it in items.values() if it["quality"] == 2 and it["random"] == 0 and (it["stats"] or it["class"] == 2)]
    blues = [it for it in items.values() if it["quality"] == 3 and it["random"] == 0 and (it["stats"] or it["class"] == 2)]
    out = {"source": "cmangos/classic-db Full_DB/ClassicDB_1_12_1_z2815.sql.gz item_template (+ quest_template), extracted 2026-09-26 by gear_stats.py; "
                     "WoW: Forever items are unverified", "gear_lag": GEAR_LAG, "min_items": MIN_ITEMS,
           "model": "per level and slot: median of the better half (by the class's stat weights) of the fixed-stat green items (blues: blue items) "
                    "wearable by the class with required level in [L-6, L-1] (widened when sparse), summed over the slots the class wears",
           "greens": {}, "blues": {}, "weapons": {}, "picks": {}}
    print(f"{len(greens)} fixed-stat green armor/weapon items ({sum(1 for i in greens if i['entry'] in rewards)} of them quest rewards), {len(blues)} blue items")
    for tier, pool in (("greens", greens), ("blues", blues)):
        for cls in CLASS_ARMOR:
            picks = None
            for L in LEVELS:
                tot, picks = character(pool, cls, L, picks)
                if tier == "blues":   # a blue-geared character is never worse than the green one (blues are sparse below 25)
                    g = out["greens"][cls][str(L)]
                    tot = {k: max(v, g.get(k, 0.0)) for k, v in tot.items()}
                out[tier].setdefault(cls, {})[str(L)] = {k: round(v, 2) for k, v in tot.items()}
                out["picks"].setdefault(tier, {}).setdefault(cls, {})[str(L)] = {s: {k: (round(v, 2) if isinstance(v, float) else v) for k, v in r.items()} for s, r in picks.items()}
        for wt in ("2h", "1h", "dagger", "ranged", "wand"):
            for L in LEVELS:
                rec = pick(pool, "warrior" if wt != "wand" else "mage", L, wt, "weapon") or {}
                if tier == "blues" and rec:
                    g = out["weapons"]["greens"][wt][str(L)]
                    rec["dps"] = max(rec.get("dps", 0.0), g.get("dps", 0.0))
                out["weapons"].setdefault(tier, {}).setdefault(wt, {})[str(L)] = {k: (round(v, 2) if isinstance(v, float) else v) for k, v in rec.items()}
    sys.path.insert(0, str(HERE))
    import tables as T
    print(f"{'tier':6} {'class':8} {'L':>3} {'Str':>5} {'Agi':>5} {'Sta':>5} {'Int':>5} {'Spi':>5} {'SP':>4} {'heal':>4} {'armor':>6} {'wdps':>5} {'spd':>4} slots | old assumption Str/Agi/Sta/Int/Spi, wdps")
    for tier in ("greens", "blues"):
        for cls in ("mage", "priest", "rogue", "hunter", "warrior", "druid", "shaman"):
            for L in (10, 20, 30, 40, 50, 60):
                c = out[tier][cls][str(L)]
                g = T.gear_stats(L, "leveling", cls)
                wd = T.wand_dps(L) if CLASS_WEAPON[cls] == "wand" else T.weapon_dps(L, CLASS_WEAPON[cls])
                print(f"{tier:6} {cls:8} {L:>3} {c['strength']:5.0f} {c['agility']:5.0f} {c['stamina']:5.0f} {c['intellect']:5.0f} {c['spirit']:5.0f} {c.get('spell_power', 0):4.0f} {c.get('healing', 0):4.0f} {c['armor']:6.0f} {c['weapon_dps']:5.1f} {c['weapon_speed']:4.1f} {c['slots']:>5} | "
                      f"{g['strength']:.0f}/{g['agility']:.0f}/{g['stamina']:.0f}/{g['intellect']:.0f}/{g['spirit']:.0f}, {wd:.1f}")
    print("weapon dps (greens / blues):", {wt: [f"L{L}: {out['weapons']['greens'][wt][str(L)].get('dps', 0):.0f}/{out['weapons']['blues'][wt][str(L)].get('dps', 0):.0f}" for L in (20, 40, 60)] for wt in ("2h", "1h", "dagger", "ranged", "wand")})
    if write:
        OUT.write_text(json.dumps(out, indent=1), encoding="utf-8")
        print(f"wrote {OUT.relative_to(ROOT)}")
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--extract")
    ap.add_argument("--write", action="store_true")
    a = ap.parse_args()
    if a.extract:
        extract(a.extract)
    if not (RAW / "item_stats.csv").exists():
        raise SystemExit("no raw item CSV: run with --extract <ClassicDB sql>")
    build(a.write)


if __name__ == "__main__":
    main()
