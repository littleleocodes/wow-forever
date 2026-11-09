"""The items a character can get while leveling, with where and when (2026-11-09, the character gear planner).

pool(cls, faction) -> [item]: every item of the simulator's WoW: Forever item database (`assets/database/db.json`, the pinned checkout) the
class can use, with its stats in fight-lab terms and its sources:
- quest: the quest's level and pick-up level from the CMaNGOS Classic dump (`raw/2026-11-09-cmangos-classic-db-c33f90b8e/quests.csv`);
  a quest Forever added (id 90000+) gets its zone and faction from Blizzard's quest API (cached in `cache/quests-forever-us.json`) and no
  level (the item's required level stands in);
- drop: a dungeon's usual level range (DUNGEONS, Classic's recommended ranges; a dungeon Forever added: its drops' required levels),
  the boss or "trash"; raids are left out (a leveling planner);
- craft: the profession, the recipe's skill (trainer or pattern) from the CMaNGOS dump, the pattern's source;
- vendor: the vendor and zone. PvP rewards are left out; reputation rewards carry the standing.
Items without any source (some Forever items) are only known when a character wears them.
"""
import csv
import json
import pathlib
import statistics
import sys

HERE = pathlib.Path(__file__).resolve().parent
DATA = HERE.parent
RAW = DATA / "raw" / "2026-11-09-cmangos-classic-db-c33f90b8e"
sys.path[:0] = [str(DATA / "raidsim"), str(DATA)]

# proto/common.proto enums (wowsims/forever)
SLOTS = {1: "head", 2: "neck", 3: "shoulder", 4: "back", 5: "chest", 6: "wrist", 7: "hands", 8: "waist", 9: "legs", 10: "feet", 11: "finger",
         12: "trinket", 13: "weapon", 14: "ranged"}
CLASS_ID = {"warrior": 1, "paladin": 2, "hunter": 3, "rogue": 4, "priest": 5, "shaman": 7, "mage": 8, "warlock": 9, "druid": 11}
FACTION_ID = {"alliance": 1, "horde": 2}
PROFESSION = {1: "Alchemy", 2: "Blacksmithing", 3: "Enchanting", 4: "Engineering", 8: "Leatherworking", 11: "Tailoring"}
SKILL_LINE = {"Tailoring": 197, "Enchanting": 333, "Leatherworking": 165, "Blacksmithing": 164, "Engineering": 202, "Alchemy": 171}
# what a class may equip: armor types, weapon types by hand, ranged types (Classic rules; mages: daggers, one-hand swords, staves, wands)
USE = {"mage": {"armor": {1}, "weapon": {(2, None), (9, 1), (9, 2), (8, 4), (5, 3)}, "ranged": {5}},
       "priest": {"armor": {1}, "weapon": {(2, None), (4, 1), (4, 2), (8, 4), (5, 3)}, "ranged": {5}},
       "warlock": {"armor": {1}, "weapon": {(2, None), (9, 1), (9, 2), (8, 4), (5, 3)}, "ranged": {5}}}
# stat ids of the database -> fight-lab gear keys; school damage counts by the spec's share of that school (SCHOOL_SHARE)
STAT = {0: "strength", 1: "agility", 2: "stamina", 3: "intellect", 5: "spell_power", 13: "spirit", 27: "armor", 28: "armor", 31: "mp5"}
SCHOOLS = {6: "arcane", 7: "fire", 8: "frost", 9: "holy", 10: "nature", 11: "shadow"}
# Classic's recommended level ranges (the client's dungeon finder of later expansions; Blizzard's level ranges of the Classic dungeons)
DUNGEONS = {2437: ("Ragefire Chasm", 13, 18, "horde"), 718: ("Wailing Caverns", 17, 24, None), 1581: ("The Deadmines", 17, 26, "alliance"),
            209: ("Shadowfang Keep", 22, 30, None), 719: ("Blackfathom Deeps", 24, 32, None), 717: ("The Stockade", 24, 32, "alliance"),
            721: ("Gnomeregan", 29, 38, None), 491: ("Razorfen Kraul", 29, 38, None), 796: ("Scarlet Monastery", 30, 45, None),
            722: ("Razorfen Downs", 37, 46, None), 1337: ("Uldaman", 41, 51, None), 1176: ("Zul'Farrak", 44, 54, None),
            2100: ("Maraudon", 46, 55, None), 1477: ("Sunken Temple", 50, 56, None), 1584: ("Blackrock Depths", 52, 60, None),
            1583: ("Blackrock Spire", 55, 60, None), 2557: ("Dire Maul", 55, 60, None), 2057: ("Scholomance", 58, 60, None),
            2017: ("Stratholme", 58, 60, None)}
RAIDS = {2717, 2159, 1977, 2677, 3428, 3429, 3456, 16076, 2366, 2367}
# Classic's outdoor zone level ranges: the level window of a quest Forever added (the API gives its zone, no level)
ZONE_LEVELS = {"Elwynn Forest": (1, 10), "Dun Morogh": (1, 10), "Teldrassil": (1, 10), "Westfall": (10, 20), "Loch Modan": (10, 20),
               "Darkshore": (10, 20), "Redridge Mountains": (15, 25), "Stonetalon Mountains": (15, 27), "Ashenvale": (18, 30),
               "Duskwood": (18, 30), "Wetlands": (20, 30), "Hillsbrad Foothills": (20, 30), "The Barrens": (10, 25),
               "Thousand Needles": (25, 35), "Alterac Mountains": (30, 40), "Arathi Highlands": (30, 40), "Desolace": (30, 40),
               "Stranglethorn Vale": (30, 45), "Dustwallow Marsh": (35, 45), "Badlands": (35, 45), "Swamp of Sorrows": (35, 45),
               "Feralas": (40, 50), "The Hinterlands": (40, 50), "Tanaris": (40, 50), "Searing Gorge": (43, 50), "Azshara": (45, 55),
               "Blasted Lands": (45, 55), "Un'Goro Crater": (48, 55), "Felwood": (48, 55), "Burning Steppes": (50, 58),
               "Western Plaguelands": (51, 58), "Eastern Plaguelands": (53, 60), "Winterspring": (53, 60), "Silithus": (55, 60),
               "Deadwind Pass": (55, 60)}


# Scourge Invasion bosses (event only; raidsim/gear_opt.EVENT_NPCS): Sever, Balzaphon, Lady Falther'ess, Revanchion, Scorn, Lord Blackwood
EVENT_NPCS = {14682, 14684, 14686, 14690, 14693, 14695}
MAP_TO_ZONE = {389: 2437, 43: 718, 36: 1581, 33: 209, 48: 719, 34: 717, 90: 721, 47: 491, 189: 796, 129: 722, 70: 1337, 209: 1176,
               349: 2100, 109: 1477, 230: 1584, 229: 1583, 429: 2557, 289: 2057, 329: 2017}
CLASSIC_STAT = {3: "agility", 4: "strength", 5: "intellect", 6: "spirit", 7: "stamina"}
CLASSIC_SLOT = {1: "head", 2: "neck", 3: "shoulder", 5: "chest", 20: "chest", 6: "waist", 7: "legs", 8: "feet", 9: "wrist", 10: "hands",
                11: "finger", 12: "trinket", 16: "back", 13: "main-hand", 21: "main-hand", 17: "two-hand", 22: "off-hand", 23: "off-hand",
                15: "ranged", 26: "ranged"}
# Classic weapon subclasses a class may use (mage: daggers 15, one-hand swords 7, staves 10, wands 19)
CLASSIC_WEAPONS = {"mage": {15, 7, 10, 19}, "priest": {15, 4, 10, 19}, "warlock": {15, 7, 10, 19}}
SCHOOL_BITS = {2: "holy", 4: "fire", 8: "nature", 16: "frost", 32: "shadow", 64: "arcane"}


def classic_items(cls, school_share):
    """Items of the Classic database by id, in pool form (stats, slot, required level), for dungeon drops the simulator's Forever database
    lacks (its mid- and high-level dungeon loot is sparse: Blackrock Depths 2 items, Dire Maul 2). Spell power from the items' equip
    spells (aura 13, by the spec's school share); mana per 5, spell crit and hit from equip spells are not read."""
    old = DATA / "raw" / "2026-09-26-cmangos-classic-db-z2815"
    sp = {}
    for r in csv.DictReader(open(old / "item_spell_power.csv", encoding="utf-8")):
        if r["aura"] == "13":
            m = int(r["school_mask"])
            share = sum(school_share.get(n, 0) for b, n in SCHOOL_BITS.items() if m & b) if m & 126 != 126 else 1.0
            sp[int(r["spell"])] = int(r["value"]) * share
    out = {}
    for r in csv.DictReader(open(old / "item_stats.csv", encoding="utf-8")):
        c, sc, inv = int(r["class"]), int(r["subclass"]), int(r["InventoryType"])
        mask = int(r["AllowableClass"])
        if mask not in (-1, 0) and not mask & (1 << (CLASS_ID[cls] - 1)):
            continue
        if c == 4 and sc not in (0, 1):
            continue
        if c == 2 and sc not in CLASSIC_WEAPONS.get(cls, set()):
            continue
        slot = CLASSIC_SLOT.get(inv)
        if not slot or c not in (2, 4):
            continue
        st = {}
        for k in range(1, 11):
            t, v = int(r[f"stat_type{k}"]), int(r[f"stat_value{k}"])
            if t in CLASSIC_STAT and v:
                st[CLASSIC_STAT[t]] = st.get(CLASSIC_STAT[t], 0) + v
        if int(r["armor"]):
            st["armor"] = int(r["armor"])
        for k in range(1, 6):
            s_id = int(r[f"spellid_{k}"])
            if s_id in sp and r[f"spelltrigger_{k}"] == "1":
                st["spell_power"] = st.get("spell_power", 0) + sp[s_id]
        if slot == "ranged" and sc == 19 and int(r["delay"]):
            st["wand_dps"] = (int(r["dmg_min1"]) + int(r["dmg_max1"])) / 2 / (int(r["delay"]) / 1000)
        out[int(r["entry"])] = {"id": int(r["entry"]), "name": r["name"], "slot": slot, "quality": int(r["Quality"]),
                                "req": int(r["RequiredLevel"]), "stats": st, "sources": [], "unique": False, "set": None, "classic_stats": True}
    return out


def classic_dungeon_drops():
    """[(zone id, boss, item, chance)] from the CMaNGOS loot tables (dungeon_drops.csv)."""
    return [(MAP_TO_ZONE[int(r["map"])], r["name"], int(r["item"]), float(r["chance"]))
            for r in csv.DictReader(open(RAW / "dungeon_drops.csv", encoding="utf-8"))
            if int(r["map"]) in MAP_TO_ZONE and int(r["creature"]) not in EVENT_NPCS]


def window(it, s):
    """(first, last) character level at which a source can be done for this item: the item is usable from its required level."""
    req = it.get("req") or 0
    if s["kind"] == "quest":
        if s.get("level"):
            return max(req, s.get("min_level") or 0, s["level"] - 3), s["level"] + 8
        lo, hi = ZONE_LEVELS.get(s.get("zone") or "", (req, req + 8))
        return max(req, lo), hi + 3
    if s["kind"] == "dungeon":
        return max(s["lo"], req - 3), s["hi"] + 3
    return req, 60
FOREVER_QUEST = 90000
ZONE_ALIAS = {1717: "Razorfen Kraul"}   # Classic quest zones the simulator's zone list names under another area id


def sim_db():
    import setup   # raidsim/setup.py: the pinned checkout
    return json.load(open(pathlib.Path(setup.checkout()) / "assets/database/db.json", encoding="utf-8"))


def sim_version():
    """(commit, item count) of the simulator database the pool reads: the page names it, so an update of the database shows."""
    import subprocess
    import setup
    repo = pathlib.Path(setup.checkout())
    commit = subprocess.run(["git", "-C", str(repo), "rev-parse", "--short=9", "HEAD"], capture_output=True, text=True).stdout.strip()
    return commit, len(sim_db()["items"])


def classic_quests():
    return {int(r["quest"]): r for r in csv.DictReader(open(RAW / "quests.csv", encoding="utf-8"))}


def recipe_skills():
    """{craft spell: (skill line, skill needed, how it is learned)}: trainer or pattern, the lowest requirement."""
    learn = {int(r["spell"]): int(r["learns"]) for r in csv.DictReader(open(RAW / "learn_spells.csv", encoding="utf-8"))}
    out = {}
    for r in csv.DictReader(open(RAW / "trainer_spells.csv", encoding="utf-8")):
        c = learn.get(int(r["spell"]))
        if c and int(r["reqskill"]):
            k = (int(r["reqskill"]), int(r["reqskillvalue"]), "trainer")
            if c not in out or k[1] < out[c][1]:
                out[c] = k
    for r in csv.DictReader(open(RAW / "recipe_items.csv", encoding="utf-8")):
        c = learn.get(int(r["teaches"]))
        if c and c not in out:
            how = "pattern: " + r["name"] + (" (vendor)" if r["vendor"] == "1" else " (drop)" if r["drop"] == "1" else "")
            out[c] = (int(r["required_skill"]), int(r["required_rank"]), how)
    return out


def forever_quests(ids, region="us"):
    """Zone and faction of quests Forever added, from Blizzard's quest API (cached; the API names no quest level)."""
    import datetime
    path = HERE / "cache" / f"quests-forever-{region}.json"
    cache = json.loads(path.read_text(encoding="utf-8")) if path.exists() else {}
    today = datetime.date.today()
    # an entry older than a week, or one the API had no answer for, is asked again: Blizzard's data for Forever is still filling in
    stale = {q for q, v in cache.items() if v.get("error") or (today - datetime.date.fromisoformat(v.get("fetched", "2000-01-01"))).days > 7}
    todo = [q for q in ids if str(q) not in cache or str(q) in stale]
    if todo:
        import bnet
        tok = bnet.token(region)
        for q in todo:
            st, js = bnet.get(region, tok, f"/data/wow/quest/{q}", f"static-forever-{region}")
            if st == 200:
                cache[str(q)] = {"title": js.get("title"), "area": (js.get("area") or {}).get("name"), "type": (js.get("type") or {}).get("name"),
                                 "faction": ((js.get("requirements") or {}).get("faction") or {}).get("type"),
                                 "xp": (js.get("rewards") or {}).get("experience"), "fetched": today.isoformat()}
            else:
                cache[str(q)] = {"error": st, "fetched": today.isoformat()}
        path.parent.mkdir(exist_ok=True)
        path.write_text(json.dumps(cache, indent=1, sort_keys=True) + "\n", encoding="utf-8")
    return cache


def usable(it, cls, faction):
    use = USE[cls]
    if it.get("classAllowlist") and CLASS_ID[cls] not in it["classAllowlist"]:
        return False
    if it.get("factionRestriction") and it["factionRestriction"] != FACTION_ID[faction]:
        return False
    t = it.get("type")
    if t in range(1, 13):
        return it.get("armorType") in (None, 0) or it["armorType"] in use["armor"]
    if t == 13:
        w, h = it.get("weaponType"), it.get("handType")
        return any(w == uw and (uh is None or h == uh) for uw, uh in use["weapon"])
    if t == 14:
        return it.get("rangedWeaponType") in use["ranged"]
    return False


def lab_stats(it, school_share):
    so = (it.get("scalingOptions") or {}).get("0") or {}
    out = {}
    for k, v in (so.get("stats") or {}).items():
        k = int(k)
        if k in STAT:
            out[STAT[k]] = out.get(STAT[k], 0) + v
        elif k in SCHOOLS:
            out["spell_power"] = out.get("spell_power", 0) + v * school_share.get(SCHOOLS[k], 0)
        elif k == 30:
            out["intellect"] = out.get("intellect", 0) + v / 15.0   # flat mana as the Intellect that gives it
        elif k == 29:
            out["stamina"] = out.get("stamina", 0) + v / 10.0
    if it.get("type") == 14 and it.get("rangedWeaponType") == 5 and so.get("weaponDamageMax"):
        out["wand_dps"] = (so["weaponDamageMin"] + so["weaponDamageMax"]) / 2 / (it.get("weaponSpeed") or 1.5)
    return out


def pool(cls, faction, school_share, region="us"):
    db = sim_db()
    zones = {z["id"]: z["name"] for z in db["zones"]}
    npcs = {n["id"]: n["name"] for n in db["npcs"]}
    cq = classic_quests()
    rs = recipe_skills()
    fid = FACTION_ID[faction]
    items = [it for it in db["items"] if usable(it, cls, faction)]
    fq = forever_quests(sorted({s["quest"]["id"] for it in items for s in it.get("sources") or [] if "quest" in s and s["quest"]["id"] >= FOREVER_QUEST
                                and s["quest"].get("faction") in (None, 0, fid)}), region)
    # dungeons Forever added: their drops' required levels give the range
    drops = {}
    for it in db["items"]:
        for s in it.get("sources") or []:
            if "drop" in s and it.get("reqLvl"):
                drops.setdefault(s["drop"].get("zoneId"), []).append(it["reqLvl"])
    # vendors that also sell reputation or PvP rewards are quartermasters (Illiyana Moonblaze's Lorekeeper's Rings need Silverwing
    # Sentinels standing, which the database does not record on the item): their wares are left out like reputation rewards (2026-11-09)
    sells = {}
    for x in db["items"]:
        for s in x.get("sources") or []:
            if "soldBy" in s:
                sells.setdefault(s["soldBy"].get("npcId"), set()).update(list(t)[0] for t in x.get("sources") or [])
    quartermasters = {n for n, kinds in sells.items() if kinds & {"rep", "pvp"}}
    out = []
    for it in items:
        st = lab_stats(it, school_share)
        if not st and it.get("type") != 14:
            continue
        srcs = []
        req = it.get("reqLvl") or 0
        for s in it.get("sources") or []:
            if "quest" in s:
                q = s["quest"]
                if q.get("faction") not in (None, 0, fid):
                    continue
                if q["id"] in cq:
                    r = cq[q["id"]]
                    srcs.append({"kind": "quest", "quest": q["id"], "name": q.get("name") or r["title"], "level": int(r["quest_level"]),
                                 "min_level": int(r["min_level"]), "zone": zones.get(int(r["zone_or_sort"])) or ZONE_ALIAS.get(int(r["zone_or_sort"]), "")})
                else:
                    f = fq.get(str(q["id"]), {})
                    if f.get("faction") and f["faction"].lower() != faction:
                        continue
                    srcs.append({"kind": "quest", "quest": q["id"], "name": q.get("name") or f.get("title"), "level": None, "min_level": None,
                                 "zone": f.get("area") or "", "type": f.get("type")})
            elif "drop" in s:
                z = s["drop"].get("zoneId")
                if z in RAIDS or s["drop"].get("npcId") in EVENT_NPCS:
                    continue
                if s["drop"].get("otherName") == "Trash" and not s["drop"].get("npcId"):
                    srcs.append({"kind": "trash", "zone": zones.get(z, "")})   # a random trash drop: listed, never recommended
                    continue
                if z in DUNGEONS:
                    name, lo, hi, side = DUNGEONS[z]
                    if side and side != faction:
                        continue
                    srcs.append({"kind": "dungeon", "zone": name, "lo": lo, "hi": hi, "boss": npcs.get(s["drop"].get("npcId")) or s["drop"].get("otherName") or "trash"})
                elif z in drops and z and z >= 16000:
                    lv = drops[z]
                    srcs.append({"kind": "dungeon", "zone": zones.get(z, str(z)), "lo": min(lv), "hi": max(lv) + 5, "estimated": True,
                                 "boss": npcs.get(s["drop"].get("npcId")) or s["drop"].get("otherName") or "trash"})
                else:
                    srcs.append({"kind": "drop", "zone": zones.get(z, ""), "boss": npcs.get(s["drop"].get("npcId")) or s["drop"].get("otherName") or ""})
            elif "crafted" in s:
                c = s["crafted"]
                prof = PROFESSION.get(c.get("profession"), str(c.get("profession")))
                line, skill, how = rs.get(c.get("spellId"), (None, None, None))
                srcs.append({"kind": "craft", "profession": prof, "spell": c.get("spellId"), "skill": skill, "learn": how})
            elif "soldBy" in s:
                v = s["soldBy"]
                if v.get("faction") not in (None, 0, fid):
                    continue
                kind = "quartermaster" if v.get("npcId") in quartermasters else "vendor"
                srcs.append({"kind": kind, "npc": v.get("npcName"), "zone": zones.get(v.get("zoneId"), "")})
            elif "rep" in s:
                r = s["rep"]
                if r.get("factionId") not in (None, 0, fid):
                    continue
                srcs.append({"kind": "rep", "rep_faction": r.get("repFactionId"), "standing": r.get("repLevel")})
        slot = SLOTS.get(it.get("type"))
        if it.get("type") == 13:
            slot = {4: "two-hand", 3: "off-hand"}.get(it.get("handType"), "main-hand")
        out.append({"id": it["id"], "name": it["name"], "slot": slot, "quality": it.get("quality"), "req": req, "stats": st, "sources": srcs,
                    "unique": bool(it.get("unique")), "set": it.get("setName")})
    # dungeon loot from the Classic loot tables, with drop chances (2026-11-09: the Forever database lists 2 Blackrock Depths items): a
    # chance on the Forever items it already lists, the dungeon source on those it lists without, and Classic items it lacks
    by_id = {p["id"]: p for p in out}
    known = {it["id"] for it in db["items"]}
    classic = None
    for zid, boss, item, chance in classic_dungeon_drops():
        name, lo, hi, side = DUNGEONS[zid]
        if side and side != faction:
            continue
        p = by_id.get(item)
        if p is None:
            if item in known:
                continue   # a Forever item the class cannot use
            classic = classic if classic is not None else classic_items(cls, school_share)
            if item not in classic:
                continue
            p = by_id[item] = dict(classic[item])
            out.append(p)
        hit = next((s for s in p["sources"] if s["kind"] == "dungeon" and s["zone"] == name and s["boss"] in (boss, "trash")), None)
        if hit:
            hit["chance"], hit["boss"] = chance, boss
        else:
            p["sources"].append({"kind": "dungeon", "zone": name, "lo": lo, "hi": hi, "boss": boss, "chance": chance})
    return out


if __name__ == "__main__":
    p = pool("mage", "alliance", {"frost": 0.85, "arcane": 0.15})
    import collections
    print(len(p), collections.Counter(s["kind"] for it in p for s in it["sources"]))
    for it in p:
        if it["name"] in ("Azure Silk Hood", "Coldspire Staff", "Incinerator's Boots", "Lesser Mystic Wand", "Greater Mystic Wand", "Bridgebreaker Bindings"):
            print(json.dumps(it))
