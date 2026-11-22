"""A character's leveling gear plan, level by level (2026-11-09, user: "I want to be able to reference to you at each level If I should be
looking to get a new piece of gear or put a new enchant on, or if I should be running a dungeon in order to get a piece of gear that I
will use within a couple levels, or if I should be doing certain quests so I can get a piece of gear within a couple levels").

    python _reference/data/characters/plan.py <name> [--no-refresh]

Reads `_characters/<name>/character.json` (hand-kept: the character's API slug, region, class, faction, leveling page spec, the damage
share of each spell school), fetches the character from Blizzard's API (`bnet.py`; `--no-refresh` reuses the last snapshot in
`_characters/<name>/armory/`), and writes `_characters/<name>/README.md`:
- the talents against the leveling page's order at the character's level;
- what to do now: enchants the character can make, crafts, quests and dungeons whose items it can use within a few levels;
- the gear it wears, what each piece is worth and when it is replaced;
- level by level to 60: every upgrade worth 0.5% of the time per kill or more (UPGRADE), when to get it and where.
Item value = the seconds per kill its stats save at that level (`weights/<class>-<rotation>.json` from stat_weights.py, smoothed over
neighbouring levels): fight-lab numbers, a model of the beta. Items from the simulator's WoW: Forever database (item_pool.py).
"""
import argparse
import collections
import csv
import datetime
import json
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
DATA = HERE.parent
ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path[:0] = [str(HERE), str(DATA / "fightlab"), str(DATA / "scorer"), str(DATA)]
import ah_prices as AH  # noqa: E402
import bnet  # noqa: E402
import item_pool as IP  # noqa: E402
import professions as PF  # noqa: E402
import market as MK  # noqa: E402
import rxp  # noqa: E402
import rxp_guide as RXG  # noqa: E402
import detours as DT  # noqa: E402
import legacy as LEG  # noqa: E402
import bags as BG  # noqa: E402
import own_keys as OWNK  # noqa: E402

UPGRADE = 0.005        # an upgrade worth less than 0.5% of the time per kill is not listed
MIN_CHANCE = 0.05      # a dungeon drop under 5% is not worth planning around
LAST = 59              # the plan stops at 59: level 60 gear is not leveling gear
ENDGAME = {"Naxxramas", "Ahn'Qiraj", "Ruins of Ahn'Qiraj", "Temple of Ahn'Qiraj", "Gates of Ahn'Qiraj", "Molten Core", "Blackwing Lair",
           "Zul'Gurub", "Onyxia's Lair", "Alterac Valley", "Warsong Gulch", "Arathi Basin"}
LOOKAHEAD = 3          # "a piece of gear that I will use within a couple levels": an item usable this many levels on
MIN_LASTS = 2          # an upgrade or enchant is suggested only for an item worn this many levels (character.json "min_levels")
MIN_MINUTES = 20      # and only when it saves this many minutes of killing before the next one replaces it (character.json "min_minutes")
SKILL_CAP = [(1, 75), (10, 150), (20, 225), (35, 300)]   # Classic's profession ranks: the cap a character of that level can train
API_SLOT = {"HEAD": "head", "NECK": "neck", "SHOULDER": "shoulder", "BACK": "back", "CHEST": "chest", "WRIST": "wrist", "HANDS": "hands",
            "WAIST": "waist", "LEGS": "legs", "FEET": "feet", "FINGER_1": "finger1", "FINGER_2": "finger2", "TRINKET_1": "trinket1",
            "TRINKET_2": "trinket2", "MAIN_HAND": "main-hand", "OFF_HAND": "off-hand", "RANGED": "ranged"}
SLOT_ORDER = ["head", "neck", "shoulder", "back", "chest", "wrist", "hands", "waist", "legs", "feet", "finger1", "finger2", "trinket1",
              "trinket2", "weapon", "ranged"]
ENCHANT_SLOT = {"Bracer": "wrist", "Chest": "chest", "Cloak": "back", "Gloves": "hands", "Boots": "feet", "2H Weapon": "weapon2h",
                "Weapon": "weapon"}
TEXT_STAT = {"defense": "defense", "attack power": "attack_power", "block value": "block_value", "block": "block_value",
             "intellect": "intellect", "stamina": "stamina", "spirit": "spirit", "strength": "strength", "agility": "agility",
             "spell power": "spell_power", "spell damage": "spell_power", "armor": "armor", "mana regeneration per 5 sec": "mp5",
             "mana regen": "mp5"}


# ---------------------------------------------------------------------------------------------------------------- inputs
def char_dir(name):
    return ROOT / "_characters" / name.lower()


def snapshot(cfg, d, refresh):
    arm = d / "armory"
    if refresh:
        res = bnet.fetch(cfg["slug"], cfg.get("region", "us"))
        if res["profile"][0] != 200:
            sys.exit(f"Blizzard API: {res['profile']}")
        arm.mkdir(parents=True, exist_ok=True)
        for part, (st, js) in res.items():
            if st == 200:
                (arm / f"{part.strip('/').replace('/', '-')}.json").write_text(json.dumps(js, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
        (arm / "fetched.txt").write_text(datetime.datetime.now().strftime("%Y-%m-%d %H:%M") + "\n", encoding="utf-8")
    parts = ("profile", "equipment", "professions", "specializations", "quests", "quests-completed", "reputations", "achievements")
    return {p: json.loads((arm / f"{p}.json").read_text(encoding="utf-8")) for p in parts
            if (arm / f"{p}.json").exists()}, (arm / "fetched.txt").read_text(encoding="utf-8").strip()


def fresher(cfg, snap, d, said=None):
    """Blizzard's character data change only at a logout it sees (last_login_timestamp is that logout); the add-ons write while you play
    (2026-11-14, user: "level 33", while Blizzard still had the 09:33 logout at level 32 and 12g 76s 25c, the bag add-on 5g 21s 18c at
    17:43). The bag record's level wins when it is newer and higher, and the level you give (--level, kept in level-said.json until Blizzard
    has seen a logout after your word) when it is higher still. Returns the bag record's gold when it is newer than Blizzard's, else None;
    NOTICES say where the level and gold come from."""
    import time
    p = snap["profile"]
    seen = (p.get("last_login_timestamp") or 0) / 1000
    f = d / "level-said.json"
    if said:
        f.write_text(json.dumps({"level": said, "time": int(time.time())}) + "\n", encoding="utf-8")
    word = json.loads(f.read_text(encoding="utf-8")) if f.exists() else None
    if word and word["time"] <= seen:   # Blizzard has seen a logout since your word: its level stands
        f.unlink()
        word = None
    rec = BG.record(cfg, p["name"])
    rec = rec if rec and rec["t"] > seen else None
    api_lv, src = p["level"], None
    if rec and (rec.get("level") or 0) > p["level"]:
        p["level"], p["experience"], src = rec["level"], 0, f"your bag add-on's record of {rec['when']}"
    if word and word["level"] > p["level"]:
        p["level"], p["experience"], src = word["level"], 0, "your word"
    when = datetime.datetime.fromtimestamp(seen).strftime("%Y-%m-%d %H:%M") if seen else "an unknown time"
    gold = rec.get("money") if rec else None
    if src:
        NOTICES.append(f"Level {p['level']} is {src}: Blizzard's data are from your logout at {when} (level {api_lv})"
                       + (f", and the gold is the bag add-on's ({rec['when']})" if gold is not None else "")
                       + ". Talents, quests and worn gear are as of that logout where your add-ons do not say otherwise. Log out once "
                       "and refresh to bring them up to date.")
    elif gold is not None:
        NOTICES.append(f"Gold is your bag add-on's ({rec['when']}): Blizzard's data are from your logout at {when}.")
    return gold


def weights(cls, rot, fname=None):
    w = json.load(open(HERE / "weights" / (fname or f"{cls}-{rot}.json"), encoding="utf-8"))
    lv = sorted(int(k) for k in w["levels"])
    raw = {L: w["levels"][str(L)] for L in lv}
    stats = list(raw[lv[0]]["weights"])
    sm = {}
    for i, L in enumerate(lv):   # three-point smoothing over the measured levels (single-level stat values are noisy)
        nb = [raw[x] for x in lv[max(0, i - 1):i + 2]]
        sm[L] = {"time": raw[L]["time_per_kill"], "w": {s: max(0.0, sum(r["weights"][s] for r in nb) / len(nb)) for s in stats}}

    def at(L):
        L = min(max(L, lv[0]), lv[-1])
        lo = max(x for x in lv if x <= L)
        hi = min(x for x in lv if x >= L)
        f = 0.0 if hi == lo else (L - lo) / (hi - lo)
        return {"time": sm[lo]["time"] * (1 - f) + sm[hi]["time"] * f,
                "w": {s: sm[lo]["w"][s] * (1 - f) + sm[hi]["w"][s] * f for s in stats}}
    return at, w


# The gear add-on's values (2026-11-13, user: the add-on work should "help with the checklists and the gear upgrades throughout the leveling
# process"): characters/addon/forever-gear-values.json, the same numbers the in-game tooltip shows. Every gear stat is scored (crit, hit,
# haste, expertise, defense, weapon skill, weapon damage), hit only while the build's talents leave room under the cap, and the values follow
# the character's own gear: its Spell Power or attack power (the armory's statistics) places it between the lab's standard gear and each
# level's best Forever set, and that share is kept for the levels ahead. Item stats here are item_pool.lab_stats keys.
PLAN_KEY = {"hit_rating": "hit", "crit_rating": "crit", "haste_rating": "haste", "expertise_rating": "expertise", "defense_rating": "defense",
            "block_rating": "block", "dodge_rating": "dodge", "parry_rating": "parry", "mh_weapon_dps": "weapon_dps",
            "spell_damage": "spell_power", "spell_healing": "healing"}
ADDON_FILE = HERE / "addon" / "forever-gear-values.json"


def addon_weights(cfg, b, order, rot, d):
    """(at, record) from the add-on's data for the character's page build, or None when the file has no entry for it."""
    if not ADDON_FILE.exists():
        return None
    data = json.loads(ADDON_FILE.read_text(encoding="utf-8"))
    entry = next((e for e in data["classes"].get(cfg["class"], {}).get("leveling", []) if e.get("build") == b["id"] and "levels" in e), None)
    if entry is None:
        return None
    sys.path.insert(0, str(HERE))
    import addon_values as AV
    lv = sorted(int(k) for k in entry["levels"])

    def totals(L):   # the gear points' unit totals at a level, linear between the measured levels
        L = min(max(L, lv[0]), lv[-1])
        lo, hi = max(x for x in lv if x <= L), min(x for x in lv if x >= L)
        k = 0.0 if hi == lo else (L - lo) / (hi - lo)
        a, c = entry["levels"][str(lo)], entry["levels"][str(hi)]
        key = a["unit"] + "_total"
        pts = [(g[key] * (1 - k) + h[key] * k) for g, h in zip(a["gear"], c["gear"])]
        return pts
    st = d / "armory" / "statistics.json"
    stats = json.loads(st.read_text(encoding="utf-8")) if st.exists() else {}
    unit = entry["levels"][str(lv[0])]["unit"]
    have = stats.get({"spell_power": "spell_power", "attack_power": "attack_power", "ranged_attack_power": "ranged_attack_power"}[unit])
    level = cfg.get("_level") or lv[0]
    now = totals(level)
    share = 0.0
    if have is not None and len(now) > 1 and now[-1] > now[0]:
        share = min(1.0, max(0.0, (have - now[0]) / (now[-1] - now[0])))
    rooms = {}
    try:   # hit and expertise only while the build's talents leave room (the add-on applies the character's own hit in game)
        sys.path.insert(0, str(DATA / "fightlab"))
        import pawn_compare as PC
        import run as FR
        for L in lv:
            setup = PC.setup_of(cfg["class"], FR.allocation_at({"allocation": b["allocation"], "order": order}, L), L, rot)
            rooms[L] = (setup["spell_room"] if setup["caster"] else setup["melee_room"], setup["exp_room"])
    except Exception as e:   # noqa: BLE001 - without the lab's player the caps are not applied
        print(f"note: hit and expertise rooms not read ({type(e).__name__}: {e})")

    def plan_keys(vals):
        w = {}
        for k, v in vals.items():
            if k in ("spell_power", "healing") or k.endswith("_damage") and k != "spell_damage":
                continue   # item_pool folds school damage into spell_power by the character's school shares; healing is spell_healing
            w[PLAN_KEY.get(k, k)] = v
        return w

    def at(L):
        L = min(max(L, lv[0]), lv[-1])
        pts = totals(L)
        ut = pts[0] + share * (pts[-1] - pts[0]) if len(pts) > 1 else pts[0]
        spk, vals = AV.lev_at(entry, L, ut)
        w = plan_keys(vals)
        near = min(rooms, key=lambda x: abs(x - L)) if rooms else None
        if near is not None:
            hit_room, exp_room = rooms[near]
            if hit_room <= 0:
                w["hit"] = 0.0
            if exp_room <= 0:
                w["expertise"] = 0.0
        return {"time": spk, "w": w}
    rec = {"date": data["made"][:10], "build": entry["build"], "source": "addon", "share": round(share, 3), "unit": unit, "have": have,
           "file": "addon/forever-gear-values.json", "placed_by": f"{unit} {have}"}

    def place(eq):
        """Place the character by the items it wears (2026-11-13; the add-on's own rule, addon_values.gear_share): the gain from the
        standard set to the worn items over the gain from the standard set to the best Forever set, both scored with the standard gear's
        values, hit and expertise and enchants left out (the two sets carry none); at the two measured levels around the character's,
        interpolated. Replaces the unit-stat share when every level has item stats."""
        nonlocal share
        mine = {}
        for slot, it in eq.items():
            for k, x in (it.get("stats") or {}).items():
                if k == "weapon_dps" and slot == "off-hand":
                    k = "oh_weapon_dps"
                mine[k] = mine.get(k, 0.0) + x
        skip = ("hit", "expertise")

        def at_level(L):
            g = entry["levels"][str(L)]["gear"]
            if len(g) < 2 or "item_stats" not in g[0] or "item_stats" not in g[-1]:
                return None
            w0 = plan_keys(g[0]["values"])
            conv = lambda st: {PLAN_KEY.get(k, k): x for k, x in st.items()}   # noqa: E731
            s0, s1 = conv(g[0]["item_stats"]), conv(g[-1]["item_stats"])
            keys = (set(s0) | set(s1) | set(mine)) - set(skip)
            den = sum((s1.get(k, 0.0) - s0.get(k, 0.0)) * w0.get(k, 0.0) for k in keys)
            num = sum((mine.get(k, 0.0) - s0.get(k, 0.0)) * w0.get(k, 0.0) for k in keys)
            return min(1.0, max(0.0, num / den)) if den > 0 else 0.0
        L = min(max(level, lv[0]), lv[-1])
        lo, hi = max(x for x in lv if x <= L), min(x for x in lv if x >= L)
        a, c = at_level(lo), at_level(hi)
        if a is None or c is None:
            return None
        k = 0.0 if hi == lo else (L - lo) / (hi - lo)
        old = share
        share = a * (1 - k) + c * k
        rec.update(share=round(share, 3), share_by_unit=round(old, 3), placed_by="worn items")
        return share
    rec["place"] = place
    return at, rec


def value(stats, wl):
    return sum(wl["w"].get(k, 0.0) * v for k, v in (stats or {}).items())


SCHOOL_SHARE = {}   # the character's damage by school (main), for "+32 Frost Damage" read from an item's text


def text_stats(lines):
    out = {}
    for t in lines:
        sm = re.match(r"\+(\d+) (Frost|Fire|Arcane|Shadow|Nature|Holy) (?:Spell )?Damage$", t.strip(), re.I)
        if sm:   # school damage counts by the build's share of that school (Coldspire Staff: "+32 Frost Damage")
            out["spell_power"] = out.get("spell_power", 0) + int(sm.group(1)) * SCHOOL_SHARE.get(sm.group(2).lower(), 0)
            continue
        m = re.search(r"\+(\d+) ([A-Za-z ]+?)$", t.strip()) or re.search(r"([A-Za-z ]+?) \+(\d+)$", t.strip())
        if not m:
            continue
        num, name = (m.group(1), m.group(2)) if m.group(1).isdigit() else (m.group(2), m.group(1))
        k = TEXT_STAT.get(name.strip().lower().replace("enchanted: ", ""))
        if k:
            out[k] = out.get(k, 0) + int(num)
    return out


def equipped(snap, pool_by_id):
    out = {}
    for it in snap["equipment"]["equipped_items"]:
        slot = API_SLOT.get(it["slot"]["type"])
        if not slot:
            continue
        p = pool_by_id.get(it["item"]["id"])
        if p and p["name"] != it["name"]:   # a random-suffix item: its version of that name, else the stats Blizzard reports for it (the
            p = next((x for x in pool_by_id.values() if x["name"] == it["name"]   # plain base item had read a worn Elder's Sash of
                      and str(x["id"]).split(":")[0] == str(it["item"]["id"])), None)   # Frozen Wrath as almost worthless, 2026-11-09)
        st = dict(p["stats"]) if p else text_stats([s["display"]["display_string"] for s in it.get("stats", []) if "display" in s])
        if it.get("weapon") and it["slot"]["type"] == "RANGED":
            st["wand_dps"] = it["weapon"]["dps"]["value"]
        ench = [e.get("display_string", "") for e in it.get("enchantments", [])]
        out[slot] = {"id": it["item"]["id"], "name": it["name"], "stats": st, "enchant": ench,
                     "enchant_stats": text_stats([re.sub(r"^Enchanted: ", "", e) for e in ench]),
                     "two_hand": bool(p and p["slot"] == "two-hand") or (it["slot"]["type"] == "MAIN_HAND" and "Staff" in json.dumps(it.get("item_subclass", {})))}
    return out


def skills(snap):
    out = {}
    for k in ("primaries", "secondaries"):
        for p in snap["professions"].get(k) or []:
            t = (p.get("tiers") or [{}])[-1]
            out[p["profession"]["name"]] = (t.get("skill_points") or p.get("skill_points") or 0, t.get("max_skill_points") or p.get("max_skill_points") or 0)
    return out


def skill_cap(level):
    return max(c for L, c in SKILL_CAP if level >= L)


# ---------------------------------------------------------------------------------------------------------------- enchants
def enchants(school_share):
    """Enchanting formulas: (slot, name, stats, skill, how learned, reagents). The enchants and their stats are Forever's (the simulator's
    database, by name and spell); the skill and the materials come from the Classic recipe of the same spell. 2026-11-09: matching through
    Classic's enchantment ids gave Enchant Bracer - Lesser Intellect the +5 of Forever's 2H weapon enchant (Forever moved the bracer's to
    a new +3 enchantment)."""
    db = IP.sim_db()
    rs = IP.recipe_skills()
    names = {int(r["item"]): r["name"] for r in csv.DictReader(open(IP.RAW / "item_names.csv", encoding="utf-8"))}
    crafts = list(csv.DictReader(open(IP.RAW / "craft_spells.csv", encoding="utf-8")))
    reagents = {int(r["spell"]): r["reagents"] for r in crafts}
    # Classic recipes by the enchantment they apply, with their slot word: the fallback when Forever gave an enchant a new spell (Enchant
    # Chest - Mana became Enchant Chest - Intellect on the same enchantment, 2026-11-09); only a recipe of the same slot counts
    by_effect = {}
    for r in crafts:
        mm = re.match(r"Enchant (2H Weapon|Weapon|Bracer|Chest|Cloak|Gloves|Boots|Shield) - ", r["name"])
        if r["enchant"] and mm:
            by_effect.setdefault(int(r["enchant"]), []).append((int(r["spell"]), mm.group(1)))
    out = []
    for e in db["enchants"]:
        m = re.match(r"Enchant (2H Weapon|Weapon|Bracer|Chest|Cloak|Gloves|Boots|Shield) - (.+)", e.get("name", ""))
        if not m or m.group(1) not in ENCHANT_SLOT:
            continue
        spells = [s["crafted"]["spellId"] for s in e.get("sources") or [] if "crafted" in s and s["crafted"].get("profession") == 3]
        spells += [e["spellId"]] if e.get("spellId") else []
        sp = next((x for x in spells if rs.get(x) and rs[x][0] == IP.SKILL_LINE["Enchanting"]), None)
        if sp is None:
            sp = next((x for x, slot_word in by_effect.get(e["effectId"], []) if slot_word == m.group(1) and rs.get(x)
                       and rs[x][0] == IP.SKILL_LINE["Enchanting"]), None)
        if sp is None:
            continue
        sk = rs[sp]
        r = {"name": e["name"], "reagents": reagents.get(sp, "")}
        st = {}
        for i, v in enumerate(e.get("stats") or []):
            if v and i in IP.STAT:
                st[IP.STAT[i]] = st.get(IP.STAT[i], 0) + v
            elif v and i in IP.SCHOOLS:
                st["spell_power"] = st.get("spell_power", 0) + v * school_share.get(IP.SCHOOLS[i], 0)
            elif v and i == 30:   # flat mana (Enchant Chest - Mana) as the Intellect that gives it, as item_pool.lab_stats
                st["intellect"] = st.get("intellect", 0) + v / 15.0
            elif v and i == 29:
                st["stamina"] = st.get("stamina", 0) + v / 10.0
        if not st:
            continue
        reag = [(names.get(int(x.split(":")[0]), x.split(":")[0]), int(x.split(":")[1]), int(x.split(":")[0])) for x in r["reagents"].split(";") if x]
        out.append({"slot": ENCHANT_SLOT[m.group(1)], "name": r["name"], "stats": st, "skill": sk[1], "learn": sk[2], "reagents": reag})
    return out


FRECIPES = {}   # Forever's recipe book for the character's professions (professions.forever_recipes, main)


RNAMES = {}


def reagent_name(i):
    if not RNAMES:
        RNAMES.update({int(r["item"]): r["name"] for r in csv.DictReader(open(IP.RAW / "item_names.csv", encoding="utf-8"))})
        RNAMES.update({it["id"]: it["name"] for it in IP.sim_db()["items"] if it["id"] not in RNAMES})
    if i not in RNAMES:   # a Forever item neither list has: Blizzard's item API (cached weekly)
        RNAMES[i] = (IP.item_texts([i]).get(str(i)) or {}).get("name") or f"item {i}"
    return RNAMES[i]


def reagents_of(spell):
    """[(name, count, item id)] of a craft spell: Forever's recipe (Blizzard's API) when known, else the Classic one."""
    if spell in FRECIPES:
        nm = FRECIPES[spell].get("names") or {}
        return [(nm.get(i) or reagent_name(i), n, i) for i, n in FRECIPES[spell]["reagents"]]
    names = {}
    for r in csv.DictReader(open(IP.RAW / "craft_spells.csv", encoding="utf-8")):
        if int(r["spell"]) == spell:
            return [(names.get(int(x.split(":")[0])) or reagent_name(int(x.split(":")[0])), int(x.split(":")[1]), int(x.split(":")[0]))
                    for x in r["reagents"].split(";") if x]
    return []


PRICES = None     # ah_prices.Prices of the character's auction house (character.json "ah"), or None
VENDOR = {}       # vendor price of vendor-sold reagents (thread, dye, vials), copper
RECIPES = []        # the recipes the character knows (professions.known_recipes)
KNOWN = set()       # their spell ids
COMPLETED = set()   # quest ids the character has completed (Blizzard's API): their rewards are gone
INLOG = set()       # quest ids in the character's quest log now
OWN = {}            # what the character owns but does not wear (bags.py: the add-on's bag snapshot, else its auction purchases)
BOOK = {}           # the character's spellbook (bags.spellbook: ForeverTape 0.9.5's snapshot, 2026-11-14); empty when there is none


def unit_price(item):
    """The cheaper of the vendor and the auction house for one unit, copper; None when neither is known."""
    v = VENDOR.get(item)
    a = PRICES.buy(item) if PRICES else None
    known = [x for x in (v, a) if x]
    return min(known) if known else None


def mats_text(reag):
    """Materials with their cost at today's prices (auction house or vendor)."""
    parts = ", ".join(f"{n} x{c}" for n, c, _ in reag)
    if not PRICES:
        return parts
    tot, miss = 0.0, []
    for n, c, i in reag:
        p = unit_price(i)
        if p is None:
            miss.append(n)
        else:
            tot += p * c
    return parts + f" (about {AH.money(tot)} at today's prices" + (f"; no price for {', '.join(miss)}" if miss else "") + ")"


QCHAIN, CQUESTS = {}, {}


def chain_step(q):
    """(the first quest of q's chain you have not done, its givers) from the Classic data (quest_chain.csv: PrevQuestId), or None for a
    quest the data lacks (Forever's own)."""
    if not QCHAIN:
        for r in csv.DictReader(open(IP.RAW / "quest_chain.csv", encoding="utf-8")):
            QCHAIN[int(r["quest"])] = (int(r["prev"]), r["givers"])
        CQUESTS.update(IP.classic_quests())
    if q not in QCHAIN:
        return None
    first, seen = q, set()
    while QCHAIN[first][0] and QCHAIN[first][0] not in COMPLETED and QCHAIN[first][0] in QCHAIN and first not in seen:
        seen.add(first)
        first = QCHAIN[first][0]
    return first, QCHAIN[first][1]


def spot_text(s):
    """"Zone 42.1, 65.9" of a position {zone, x, y} or (zone, x, y)."""
    if not s:
        return ""
    z, x, y = (s.get("zone"), s.get("x"), s.get("y")) if isinstance(s, dict) else s
    return f"{z} {x:.1f}, {y:.1f}" if z and x is not None else (z or "")


def chain_head(q):
    """The first quest of q's chain by Classic's PrevQuestId links."""
    chain_step(0)
    seen = set()
    while q in QCHAIN and QCHAIN[q][0] and QCHAIN[q][0] in QCHAIN and q not in seen:
        seen.add(q)
        q = QCHAIN[q][0]
    return q


START_ITEM_SURE = 20.0   # %: an item that starts a quest from a source at least this likely is something to go and get; below it, a
                         # lucky drop (An Old History Book, 1% from Duskwood's mobs) that no plan can count on


def spawn_spot(kind, sid):
    """(zone, x, y) of a creature's or object's first spawn in the open world (Classic's spawns), or None (none known, or a dungeon)."""
    DT.load()
    MAPS or MAPS.update(RXG.bounds())
    for p in DT.SPAWNS.get((kind, sid), []):
        z = DT.zone_of(p, MAPS)
        if z:
            return z
    return None


def spawn_dungeon(kind, sid):
    """The dungeon a creature or object spawns in, when every spawn of it is inside one (Classic's map ids), else None."""
    DT.load()
    zs = {IP.MAP_TO_ZONE.get(m) for m, _, _ in DT.SPAWNS.get((kind, sid), [])}
    if not zs and (kind, sid) in DT.SRCMAP:
        zs = {IP.MAP_TO_ZONE.get(DT.SRCMAP[(kind, sid)])}
    return IP.DUNGEONS[next(iter(zs))][0] if len(zs) == 1 and next(iter(zs)) in IP.DUNGEONS else None


def item_start_text(it):
    """(text, best chance %, the dungeon it drops in or None, open-world spot or None) for an item that starts a quest: "<item>, a drop
    from <mob> in <dungeon> (8%)", "<item>, a 1% drop from 33 kinds of mobs in Duskwood", "<item>, from <object> (Zone x, y)"."""
    DT.load()
    srcs = sorted(DT.ISRC.get(it, []), key=lambda s: -s[2])
    name = reagent_name(it)
    if not srcs:
        return f"{name} (where it drops is not in the data)", 0.0, None, None
    k, sid, ch = srcs[0]
    dungeon, spot = spawn_dungeon(k, sid), spawn_spot(k, sid)
    pc = f" ({ch:.0f}%)" if ch < 99.5 else ""
    if k == "o":   # an object you take it from
        who = DT.NAMES.get((k, sid)) or "an object"
        return (f"{name}, from {who}" + (f" in {dungeon}" if dungeon else f" ({spot_text(spot)})" if spot else "") + pc), ch, dungeon, spot
    mobs = [s for s in srcs if s[2] >= ch / 2]   # the sources about as likely as the best one
    if len(mobs) >= 3:   # a world drop from many mobs: where most of them are
        zones = collections.Counter(z[0] for z in (spawn_spot(s[0], s[1]) for s in mobs) if z)
        where = f" in {dungeon}" if dungeon else (f" in {' and '.join(z for z, _ in zones.most_common(2))}" if zones else "")
        art = "an" if re.match(r"(8|11|18)(\d\d)?$|8\d$", f"{ch:.0f}") else "a"   # "an 8%", "an 11%", "an 80%"
        return f"{name}, {art} {ch:.0f}% drop from {len(mobs)} kinds of mobs{where}", ch, dungeon, spot
    who = DT.NAMES.get((k, sid)) or "a mob"
    return f"{name}, a drop from {who}" + (f" in {dungeon}" if dungeon else "") + pc, ch, dungeon, spot


def start_item(q):
    """(item id, its source text, best chance %, spot) when an item starts quest q and no NPC or object gives it, else None."""
    DT.load()
    g = DT.GEO.get(q) or {}
    items = [int(i) for k, i in g.get("starts", []) if k == "i"]
    if not items or any(k in "co" for k, _ in g.get("starts", [])):
        return None
    text, ch, dungeon, spot = item_start_text(items[0])
    return items[0], text, ch, spot


def chain_start(head, lv):
    """(can you start it, how, where) for a chain's first quest (2026-11-10, user: the Stockade list held "a mega chain quests that starts
    in Deadmines from a quest item that drops off the last boss"): from an NPC or object (who and where), or from an item (the item, what
    drops it and where); a chain whose item drops only in a dungeon you have outgrown cannot be started any more. `where` is the zone or
    dungeon it starts in: a giver or a drop inside a dungeon starts it during the run (2026-11-14: Razorfen Kraul's Heralath Fallowbrook
    and Lower Blackrock Spire's Bijou were listed as quests to pick up before the run)."""
    DT.load()
    g = DT.GEO.get(head) or {}
    if head in COMPLETED or head in INLOG:
        return True, "", None
    items = [int(i) for k, i in g.get("starts", []) if k == "i"]
    if items and not any(k in "co" for k, _ in g.get("starts", [])):
        text, ch, dungeon, spot = item_start_text(items[0])
        zid = next((z for z, v in IP.DUNGEONS.items() if v[0] == dungeon), None)
        if zid is not None and IP.DUNGEONS[zid][2] <= lv:
            return False, f"starts from {text}: you have outgrown {dungeon}", None
        return True, f"starts from {text}", dungeon or (spot[0] if spot else None)
    g1, z = giver_spot(head)
    if " / " in g1 and "(" in g1:   # one step names several NPCs: the first, with the place
        g1 = g1.split(" / ")[0] + " (" + g1.split(" (", 1)[1]
    starters = [(k, int(i)) for k, i in g.get("starts", []) if k in "co"]
    if starters and not any(DT.SPAWNS.get(s) for s in starters):   # no giver in the open world (spawns.csv holds the continents
        load_dq()                                                   # only): inside the dungeon the quest belongs to
        m = next((m for m, qs in DQ.items() if head in qs), None)
        d = (IP.DUNGEONS.get(IP.MAP_TO_ZONE.get(m)) or (None,))[0] if m is not None else None
        if d:
            return True, (f"from {g1.split(' (')[0].replace(' / ', ' or ')} " if g1 else "") + f"inside {d}", d
    return True, (f"from {g1}" if g1 else ""), z


def open_chains(r):
    """A dungeon's chains as you need them: only the parts the guide does not pick up and that still give full experience."""
    out = []
    for c in r.get("chains", []):
        xs = [x for x in c["quests"] if not x["route"] and not x["grey"]]
        if xs:
            out.append(dict(c, quests=xs, log=any(x["log"] for x in xs)))
    return out


def group_text(gr, short=False):
    """A chain of a dungeon's quests as one entry: "First → Last (N parts, levels a-b), from NPC (Zone x, y)"."""
    xs = gr["quests"]
    lv = f"{xs[0]['level']}" if len(xs) == 1 or xs[0]["level"] == xs[-1]["level"] else f"{xs[0]['level']}-{xs[-1]['level']}"
    name = xs[0]["title"] if len(xs) == 1 else f"{xs[0]['title']} → {xs[-1]['title']}"
    parts = "" if len(xs) == 1 else f"{len(xs)} parts, "
    tail = (", in your log" if gr["log"] else "") + (f", {gr['start']}" if gr["start"] else "") + (f"; rewards {gr['gear']} from your gear plan" if gr.get("gear") else "")
    return f"{name} ({parts}level {lv}{tail})" if not short else f"{name} ({parts}level {lv})"


def giver_text(q):
    """Who gives quest q and where: "NPC (Zone x, y)" from RestedXP's dungeon quest guides or the NPC positions the route names
    (rxp_guide.py, 2026-11-10), else the Classic data's givers; "" when unknown."""
    return giver_spot(q)[0]


def giver_spot(q):
    """(giver_text, the giver's zone or None)."""
    if RG:
        for rows in RG["extra"].values():
            for r in rows:
                if r["quest"] == q and r.get("giver"):
                    return r["giver"] + (f" ({spot_text(r['spot'])})" if r.get("spot") else ""), (r["spot"] or [None])[0]
        g = RG["givers"].get(q)   # any guide on this PC that takes it
        if g and g.get("npc"):
            return g["npc"] + (f" ({spot_text(g)})" if g.get("zone") else ""), g.get("zone")
        if g and g.get("zone"):
            return spot_text(g), g["zone"]
    chain_step(0)
    st = QCHAIN.get(q)
    if st and st[1]:
        for n in (x.strip() for x in st[1].split(" / ")):
            sp = (RG or {}).get("npcs", {}).get(n)
            if sp:
                return f"{n} ({spot_text(sp)})", sp["zone"]
        return st[1], None
    return "", None


# ---------------------------------------------------------------------------------------------------------------- the plan
def sources_text(it):
    out = []
    for s in it.get("sources") or []:
        k = s["kind"]
        if k == "quest":
            if s.get("quest") in COMPLETED:
                continue
            lv = f", level {s['level']}" if s.get("level") else ""
            log = ", in your quest log" if s.get("quest") in INLOG else ""
            st = chain_step(s["quest"]) if isinstance(s.get("quest"), int) else None
            if st and st[0] != s["quest"] and st[0] not in INLOG:   # a chain: where to start it (2026-11-09, the "work toward" list)
                row = CQUESTS.get(st[0]) or {}
                item = start_item(st[0])   # (an item starts it: what drops it, 2026-11-14: "The Shattered Necklace" from an 8% drop)
                log += (f"; the chain starts with \"{row.get('title', st[0])}\""
                        + (f", which starts from {item[1]}" if item else f" from {st[1]}" if st[1] else "")
                        + (f", level {row['min_level']}" if row.get("min_level") not in (None, "", "0") else ""))
            elif st and st[1] and s.get("quest") not in INLOG:
                log += f"; from {st[1]}"
            inner = ", ".join(x for x in (s.get("zone"), lv.lstrip(", ")) if x)   # (no "?" for a quest whose zone is not in the data)
            out.append(f"quest \"{s['name']}\"" + (f" ({inner}{log})" if inner else f" ({log.lstrip('; ')})" if log else ""))
        elif k == "bags":
            out.append({"bags": "In your bags", "bank": "In your bank"}.get(s.get("where"), f"You bought it on {s.get('when')}; it should be in your bags")
                       + (f" (as of {s.get('when')})" if s.get("where") in ("bags", "bank") else ""))
        elif k == "auction":
            mk = next((x for x in it.get("sources") or [] if x["kind"] == "market" and x.get("price")), None)
            if mk and s.get("price") and s["price"] > 1.5 * mk["price"]:   # a listing far above the usual price: wait for another
                out.append(f"Auction House: listed now at {AH.money(s['price'])}, usually about {AH.money(mk['price'])}: wait for a cheaper one")
            else:
                out.append(f"Auction House now: {AH.money(s.get('price'))}")
        elif k == "market":
            if not any(x["kind"] == "auction" for x in it.get("sources") or []):
                out.append(f"Auction House: usually listed (in {s['share']:.0%} of the hourly snapshots), about {AH.money(s.get('price'))}, "
                           "not this hour")
        elif k == "dungeon":
            est = ", range estimated" if s.get("estimated") else ""
            ch = f", {s['chance']:.0%} drop" if s.get("chance") else ""
            out.append(f"{s['zone']} ({s['lo']}-{s['hi']}{est}), {s['boss']}{ch}")
        elif k == "drop":
            out.append(f"drop: {s.get('boss') or 'world drop'}{', ' + s['zone'] if s.get('zone') else ''}")
        elif k == "craft":
            if s.get("spell") in KNOWN:
                out.append(f"{s['profession']}: you know this recipe, craft it now")
            else:
                have = (PROFS.get(s["profession"]) or (None,))[0]
                if have is None:   # not one of your professions (2026-11-14: Tara's page read "Leatherworking: ... you have None")
                    if len(it.get("sources") or []) == 1:
                        out.append(f"a {s['profession']} craft (not one of your professions: a crafter can make it)")
                    continue
                need = (f"turns yellow at {s['skill']} in the client's data" if (s.get("learn") or "").startswith("a Forever recipe")
                        else f"Classic asked skill {s['skill']}, Forever often less" if s.get("skill") else "the skill it needs is not in the data")
                out.append(f"{s['profession']}: learn it first ({s.get('learn') or 'recipe source unknown'}; {need}; you have {have})")
        elif k == "vendor":
            out.append(f"vendor {s.get('npc')} ({s.get('zone')})")
        elif k in ("rep", "quartermaster", "trash") and len(it.get("sources") or []) == 1:
            out.append({"rep": "reputation reward", "quartermaster": f"reputation or PvP vendor {s.get('npc')}", "trash": f"random trash drop in {s.get('zone')}"}[k])
    return "; ".join(out)


DATAVER = {}   # the data versions the page names (main())
MARKET = {"windows": 0}   # market.history: the auction house over the add-on's hourly snapshots
GEAR_SHARE = 1 / 3        # the gear budget's share of each level's income after training (character.json "gear_share"); the rest saves
                          # for the mount at 40 and level 60 (user 2026-11-09: "I don't want to sit here and upgrade my gear every single level
                          # because that costs money that I need for later levels, such as level 40 ... for my mount, or for level 60")
PLANNED = []              # (level, copper) of the buys budget_walk fits, for the gold plan
NOW_LV = 0                # the character's level (main)
PLAN_EVENTS = []          # the plan's upgrades (main), for the profession section
CTX = {}                  # what the town checklist page (checklist.py) shows, filled while the README is written
FASTER, SHORT, KILLING = "faster kills", "faster", "min of killing"   # a tank (character.json "metric": "tank"): better tanking
MINUTES_OF = "minutes of killing"   # the same in running text (a tank: "minutes of group play", 2026-11-14: Tara's page read "of killing")
BONUS = []                # dungeon drops worth chasing on top of the sure plan (bonus_drops)
ROUTE = None              # the character's RestedXP route (rxp.route), when its saved files are on this PC
RG = None                 # the route step by step from the readable guide files (rxp_guide.facts), when they are on this PC
DETOURS = {"list": [], "stats": {}}   # quests off the route worth a detour (detours.find), when RG is known
AUCTION_FUTURE = False   # what-if (2026-11-09): treat today's listings as buyable at their level later (how soon cheap AH gear replaces a buy)
PROFS = {}   # the character's professions, {name: (skill, cap)}: main() fills it for the craft lines


def acquirable(it, L, start, profs):
    """The level at which this item can be had at the earliest, from `start` on, if it can be had by level L; None if not."""
    best = None
    if (it.get("quality") or 0) >= 5:   # legendaries are not leveling gear
        return None
    for s in it.get("sources") or []:
        if s["kind"] in ("rep", "drop", "trash", "quartermaster"):
            continue
        if s["kind"] == "dungeon" and s.get("chance") is not None and s["chance"] < MIN_CHANCE:
            continue
        if s["kind"] == "quest" and ((s.get("level") or 0) >= 60 or s.get("zone") in ENDGAME or s.get("quest") in COMPLETED):
            continue
        lo, hi = IP.window(it, s)
        if s["kind"] == "bags":   # yours already: had now, worn from its required level
            lo, hi = start, 60
        if s["kind"] == "market":   # usually listed (market.history): from the item's level on, at its usual price
            lo, hi = max(it.get("req") or start, start), 60
        elif s["kind"] == "auction" and AUCTION_FUTURE:   # a what-if: today's listings as a typical market, buyable at their level later
            lo, hi = it.get("req") or start, 60
        elif s["kind"] == "auction":   # listed now: buy it now (wear it at its level), only for the next few levels (listings change hourly)
            if (it.get("req") or 0) > start + LOOKAHEAD:
                continue
            if GOLD is not None and (s.get("price") or 0) > GOLD:   # more than the character has: not part of the plan
                continue
            lo, hi = start, start + LOOKAHEAD
        if s["kind"] == "craft":
            have = profs.get(s["profession"])
            # a recipe the character knows is craftable now (Forever asks no skill to craft a known recipe: Arcea knew and could make
            # Spidersilk Boots, Classic 125, at 106); an unknown one is planned by the Classic trainer's skill, which Forever may undercut
            if have is None or (s.get("spell") not in KNOWN and (not s.get("skill") or s["skill"] > skill_cap(L))):
                continue
        a = max(lo, start)
        if a <= L and a <= hi:
            best = a if best is None else min(best, a)
    return best


FULL_BY_ID = {}   # every item the planner knows, by id (main): what you wear is read from it whatever pool a plan runs on
NOTICES = []      # things the page and checklist must say up front (main): a missing guide text
ROUTE_NOTE = [None]   # the RestedXP check's line for the route section (main, 2026-11-13)


def route_unknown(e, lv0):
    """Why the route's coverage of a quest is unknown, or None: the guide text on this PC does not match where the add-on is, or the text
    for the quest's levels is missing (rxp_guide.check, 2026-11-13: such a quest is "Unknown", never "Not on your RestedXP route")."""
    tr = (RG or {}).get("trust") or {}
    if tr.get("mismatch"):
        return "the guide text on this PC does not match where your RestedXP add-on is"
    L = max(e["get_at"], lv0)
    for a, b in tr.get("missing") or []:
        if a - 3 <= L <= b + 3:
            return f"the guide text for levels {a}-{b} is not on this PC"
    return None


def plan(cfg, snap, at, pool, profs):
    level = snap["profile"]["level"]
    eq = equipped(snap, FULL_BY_ID or {p["id"]: p for p in pool})   # (the sure plan's pool has no dungeon drops: a worn dungeon staff
                                                                      # had read as worth nothing, 2026-11-09)
    by_slot = {}
    for p in pool:
        s = p["slot"]
        keys = {"finger": ["finger1", "finger2"], "trinket": ["trinket1", "trinket2"]}.get(s, [s])
        for k in keys:
            by_slot.setdefault(k, []).append(p)
    # the weapon slot: a two-hander, or a main hand plus an off hand (their values add)
    cur = {s: {"item": eq.get(s), "since": level} for s in SLOT_ORDER if s not in ("weapon",)}
    w2 = eq.get("main-hand") if eq.get("main-hand") and eq["main-hand"]["two_hand"] else None
    cur["weapon"] = {"item": w2 or eq.get("main-hand"), "off": None if w2 else eq.get("off-hand"), "since": level}
    events, held = [], {}
    for L in range(level, LAST + 1):
        wl = at(L)
        taken = set()
        for slot in SLOT_ORDER:
            c = cur[slot]
            # an item worn in another slot (the other ring or trinket) is not a candidate here: rings and trinkets are mostly unique
            taken = {x["item"]["id"] for s2, x in cur.items() if s2 != slot and x.get("item") and x["item"].get("id")}
            cv = value((c["item"] or {}).get("stats"), wl) + (value(c["off"]["stats"], wl) if slot == "weapon" and c.get("off") else 0.0)
            pair = {"finger1": "finger2", "finger2": "finger1", "trinket1": "trinket2", "trinket2": "trinket1"}.get(slot)
            if pair and value((cur[pair]["item"] or {}).get("stats"), wl) < cv - 1e-12:
                continue   # a new ring or trinket replaces the weaker of the two (the other slot's turn)
            worn_mh = worn_oh = None
            if slot == "weapon":
                cands = [(value(p["stats"], wl), p, None) for p in by_slot.get("two-hand", []) if p["req"] <= L + LOOKAHEAD]
                # a main hand and an off hand (user 2026-11-09: "Make sure we're also considering a Main + offhand weapon combo as well"):
                # every pair of the eight best of each you can get, the worn one-hander or off hand kept as one half. Only the best of
                # each by stats was tried before, and that was often one you cannot get (a random drop, a 200g listing): no pair at all,
                # and Hypnotic Blade + Orb of the Forgotten Seer (20% faster kills at 34) lost to a 16% staff.
                def top(hand):
                    xs = [p for p in by_slot.get(hand, []) if p["req"] <= L + LOOKAHEAD and acquirable(p, L, level, profs) is not None]
                    return sorted(xs, key=lambda p: -value(p["stats"], wl))[:8]
                worn_mh = c["item"] if c.get("item") and not is_2h(c["item"]) else None
                worn_oh = c.get("off")
                mhs = top("main-hand") + ([worn_mh] if worn_mh else [])
                ohs = top("off-hand") + ([worn_oh] if worn_oh else [])
                for m in mhs:
                    cands.append((value(m["stats"], wl), m, None))   # a one-hander alone (the off hand stays empty)
                    for oh_ in ohs:
                        if not (m is worn_mh and oh_ is worn_oh):
                            cands.append((value(m["stats"], wl) + value(oh_["stats"], wl), m, oh_))
            else:
                cands = [(value(p["stats"], wl), p, None) for p in by_slot.get(slot, []) if p["req"] <= L + LOOKAHEAD]
            best, alts = None, []
            for v, p, o in sorted(cands, key=lambda x: -x[0]):
                if v - cv < UPGRADE * wl["time"] or len(alts) >= 2:
                    break
                if p["id"] in taken or (o and o["id"] in taken):
                    continue
                a = level if p is worn_mh else acquirable(p, L, level, profs)
                ao = level if (o is None or o is worn_oh) else acquirable(o, L, level, profs)
                if a is None or ao is None:
                    continue
                if p.get("req", 0) > L or (o and o.get("req", 0) > L):   # an item worn later is a candidate at its own level; best_chain picks between it and what you can wear
                    continue       # now (waiting for it had skipped 1g 29s boots wearable at 26 for 2g boots at 28, 2026-11-09)
                if best is None:
                    best = (v, p, o, max(a, ao))
                elif p is not best[1] or o is not best[2]:   # the runners-up (2026-11-09: a free quest staff 0.2% behind a dungeon pair
                    alts.append((v, p, o, max(a, ao)))        # had vanished from the plan)
            if best and best[1].get("req", 0) <= L:
                v, p, o, a = best
                gain = (v - cv) / wl["time"]
                prev = c["item"]
                events.append({"level": L, "get_at": a, "slot": slot, "item": p, "off": o, "gain": gain, "replaces": (prev or {}).get("name"),
                               "lasts_from": L, "prev": [prev, c.get("off")]})
                alt_events = [{"level": L, "get_at": a2, "slot": slot, "item": p2, "off": o2, "gain": (v2 - cv) / wl["time"],
                               "replaces": (prev or {}).get("name"), "lasts_from": L, "prev": [prev, c.get("off")], "alt": True}
                              for v2, p2, o2, a2 in alts]
                if slot in held:
                    held[slot]["until"] = L
                held[slot] = events[-1]
                events += alt_events
                cur[slot] = {"item": p, "off": o, "since": L}
                taken.add(p["id"])
            elif best and best[1]["req"] > L:
                pass
            if c.get("item"):
                taken.add(c["item"].get("id"))
    for e in events:
        e.setdefault("until", None)
    # an upgrade is worth the trip only when it saves MIN_MINUTES of killing before the next one replaces it and is worn at least
    # MIN_LASTS levels (user 2026-11-09: "if I'm going to just go and get something that is only going to last one level, then there's
    # no point"; "I don't want to switch gear if it is only to save me a couple minutes, but saving multiple minutes or hours across the
    # levels until the next upgrade is substantial"). Per slot the chain of upgrades that saves the most minutes in all, each one in it
    # clearing both bars against the one before it (dropping the weakest first had dropped 19s gloves worn 14 levels for 75s gloves two
    # levels later); level 60 ends leveling.
    kept = []
    for slot in SLOT_ORDER:
        evs = [e for e in events if e["slot"] == slot]
        if evs:
            kept += best_chain(evs, at)
    return eq, sorted(kept, key=lambda e: (e["level"], SLOT_ORDER.index(e["slot"])))


CRAFT_COST = {}


def craft_cost(spell):
    """The materials of a craft at today's prices (unit_price), copper; None when one has no price."""
    if spell not in CRAFT_COST:
        reag = reagents_of(spell)
        tot = 0.0 if reag else None   # a recipe Classic's data lacks (Forever's own): its materials are unknown, not free
        for _, c, i in reag:
            p = unit_price(i)
            if p is None:
                tot = None
                break
            tot += p * c
        CRAFT_COST[spell] = tot
    return CRAFT_COST[spell]


def is_2h(x):
    return bool(x.get("two_hand")) or x.get("slot") == "two-hand"


def pieces(e):
    """The items of an upgrade: one, or a main hand and an off hand."""
    return [x for x in (e["item"], e.get("off")) if x]


def new_pieces(e, owned=None):
    """The pieces of an upgrade you still have to get: not the half of a weapon pair you hold already (owned: item ids; by default the
    ones best_chain found in the step before), and not an item you wear (it has no sources)."""
    own = owned if owned is not None else (e.get("owned") or set())
    return [it for it in pieces(e) if it.get("id") not in own and it.get("sources")]


def new_sources(e, owned=None):
    return [x for it in new_pieces(e, owned) for x in it["sources"]]


def price_of(e, owned=None):
    """What an upgrade costs in gold, both halves of a weapon pair together: None when nothing in it is bought or crafted."""
    cs = [c for c in (piece_price(it, e) for it in new_pieces(e, owned)) if c is not None]
    return sum(cs) if cs else None


def piece_price(it, e):
    """What one item costs in gold: None when a quest or a dungeon gives it (free but for the time) or you wear it already, else the
    cheapest of the auction house now, its usual price there, a vendor and the materials of a craft (2026-11-09: every bought or crafted
    upgrade must pay for itself and fit the gear budget)."""
    srcs = it.get("sources") or []
    if any(x["kind"] in ("quest", "dungeon") for x in srcs):
        return None
    cost = []
    now = (e.get("get_at") or 0) <= NOW_LV and any(x["kind"] == "auction" for x in srcs)
    for x in srcs:
        if x["kind"] == "auction" and x.get("price") and now:   # bought this visit: today's listing
            cost.append(x["price"])
        elif x["kind"] == "market" and x.get("price") and not now:   # bought later: its usual price
            cost.append(x["price"])
        elif x["kind"] == "vendor" and isinstance(it["id"], int) and VENDOR.get(it["id"]):
            cost.append(VENDOR[it["id"]])
        elif x["kind"] == "craft" and x.get("spell") and PRICES:
            c = craft_cost(x["spell"])
            if c is not None:
                cost.append(c)
    return min(cost) if cost else None


def budget_walk(events, cfg, at, lv):
    """The gear budget level by level (GEAR_SHARE): today's gold above the training of the next two levels, then GEAR_SHARE of each
    level's income after the training two levels on. Bought and crafted upgrades in the order you reach them (the most minutes per gold
    first within a level) are paid from it; one that does not fit waits up to two levels (worn later) and is dropped after that.
    Returns the item ids dropped; sets each paid event's "paid" (level, budget left) and PLANNED."""
    PLANNED.clear()
    if GOLD is None:   # no gold reading: the plan's buys at their levels, unchecked (the gold plan had totalled them "0c", 2026-11-14)
        PLANNED.extend((max(e["get_at"], lv), price_of(e)) for e in events if price_of(e))
        return set()
    train = training_by_level(cfg["class"])
    tr = lambda L: sum(c for n, c in train.get(L, []) if n in needed_at(cfg, L))
    owe = owed_training(cfg, lv)
    budget = max(0.0, GOLD - tr(lv + 1) - tr(lv + 2) - (sum(x[3] for x in owe[0]) if owe else 0))
    pending = [e for e in events if price_of(e)]
    dropped = set()
    for L in range(lv, LAST + 1):
        if L > lv:
            budget += GEAR_SHARE * max(0.0, income_per_level(L - 1, QPL) - tr(L + 2))
        due = sorted([e for e in pending if max(e["get_at"], lv) <= L], key=lambda e: -minutes_saved(e, at) / price_of(e))
        for e in due:
            if price_of(e) <= budget:
                budget -= price_of(e)
                e["paid"] = (L, budget)
                PLANNED.append((L, price_of(e)))
                if L > max(e["level"], e["get_at"]):   # bought later than planned: worn from then on
                    for x in events:
                        if x["slot"] == e["slot"] and x.get("until") == e["level"]:
                            x["until"] = L
                    e["level"], e["get_at"] = L, L
                pending.remove(e)
            elif L >= max(e["get_at"], lv) + 2 or L + MIN_LASTS >= (e["until"] or 60):
                dropped |= {it["id"] for it in pieces(e) if piece_price(it, e) is not None}
                pending.remove(e)
    dropped |= {it["id"] for e in pending for it in pieces(e) if piece_price(it, e) is not None}
    return dropped


def bonus_drops(full, events, eq, at):
    """Dungeon drops worth chasing on top of the sure plan: each upgrade of the plan with drops (full) that needs one, against what the
    sure plan (events) has you wear at every level it would be worn, until the next upgrade of the slot in the plan with drops; kept when
    it beats that by 0.5% and saves MIN_MINUTES if it drops."""
    def sure_at(slot, L):
        on = [e for e in events if e["slot"] == slot and e["level"] <= L]
        if on:
            e = max(on, key=lambda e: e["level"])
            return [e["item"], e.get("off")]
        return [eq.get("main-hand"), eq.get("off-hand")] if slot == "weapon" else [eq.get(slot)]

    def val(its, L):
        return sum(value((x or {}).get("stats"), at(L)) for x in its)

    out = []
    for d in full:
        if not any(all(s["kind"] == "dungeon" for s in it["sources"]) for it in pieces(d) if it.get("sources")):
            continue
        L0 = d["level"]
        nxt = [x["level"] for x in full if x["slot"] == d["slot"] and x["level"] > L0]
        end = min(nxt) if nxt else 60
        mine = [d["item"], d.get("off")]
        m = sum(max(0.0, val(mine, L) - val(sure_at(d["slot"], L), L)) * kills_per_level(L) for L in range(L0, end)) / 60
        g = (val(mine, L0) - val(sure_at(d["slot"], L0), L0)) / at(L0)["time"]
        if g < UPGRADE or m < MIN_MINUTES:
            continue
        over = " + ".join(x["name"] for x in sure_at(d["slot"], L0) if x) or "an empty slot"
        out.append(dict(d, owned=set(), bonus_gain=g, bonus_minutes=m, over=over, until=end if nxt else None))
    return out


MAPS = {}
# A side-trip dungeon is worth it for this many quests at full experience: 3 until Blizzard's hotfix of 2026-11-09 ("Experience from all
# dungeon enemy kills increased by 50%"), which makes a run's kills pay too, so 2 since.
DUNGEON_QUEST_BAR = 2
CAPITALS = {"Stormwind City", "Ironforge", "Darnassus", "Orgrimmar", "Thunder Bluff", "Undercity"}
ENTRANCE = {"Ragefire Chasm": "Orgrimmar", "Wailing Caverns": "The Barrens", "The Deadmines": "Westfall", "Shadowfang Keep": "Silverpine Forest",
            "Blackfathom Deeps": "Ashenvale", "The Stockade": "Stormwind City", "Gnomeregan": "Dun Morogh", "Razorfen Kraul": "The Barrens",
            "Scarlet Monastery": "Tirisfal Glades", "Razorfen Downs": "The Barrens", "Uldaman": "Badlands", "Zul'Farrak": "Tanaris",
            "Maraudon": "Desolace", "Sunken Temple": "Swamp of Sorrows", "Blackrock Depths": "Burning Steppes", "Blackrock Spire": "Burning Steppes",
            "Dire Maul": "Feralas", "Scholomance": "Western Plaguelands", "Stratholme": "Eastern Plaguelands", "The Hall of Thanes": "Dun Morogh",
            "Ruins of Lordaeron": "Tirisfal Glades", "Excavation Site: Wetlands": "Wetlands", "City of Dalaran": "Alterac Mountains"}   # where
                                                                                                                                # each one's door is


def quest_title(q):
    chain_step(0)
    if q in CQUESTS:
        return CQUESTS[q]["title"].strip()
    f = IP.forever_quests([q]).get(str(q)) or {}
    return f.get("title") or f"quest {q}"


def route_anchor(n):
    """Route point n as a moment in the guide: (text, level, step, section levels lo, hi). The quest the guide hands in, picks up or works
    on at that step, else the NPC or place it brings you to."""
    p = RG["path"][max(0, n)]
    level, zone, lo, hi, step, ops, npc, spot = p[0], p[4], p[5], p[6], p[7], p[8], p[9], p[10]
    nxt = RG["path"][n + 1] if 0 <= n + 1 < len(RG["path"]) else None
    travel = p[11] if len(p) > 11 and p[11] else (nxt[11] if nxt is not None and len(nxt) > 11 and nxt[0] == level and nxt[11] else None)
    if zone in ("Kalimdor", "Eastern Kingdoms", "Azeroth") or not spot:   # a continent-wide position: the zone it lies in
        z = DT.zone_of((p[1], p[2], p[3]), MAPS or MAPS.update(RXG.bounds()) or MAPS)
        if z:
            zone, spot = z[0], z
    where = f" ({spot_text(spot)})" if spot else f" ({zone})"
    if travel and travel.startswith("the trip to ") and travel[len("the trip to "):] in (zone, p[4]):
        travel = None   # a .zone step into the zone you are in ("in Stormwind City ..., before the trip to Stormwind City", 2026-11-14)
    t = (next((x for x in ops if x[0] == "turnin"), None) or next((x for x in ops if x[0] == "accept"), None) or (ops[0] if ops else None))
    if t:
        title = quest_title(t[1])
        txt = {"turnin": f"right after you hand in \"{title}\"" + (f" to {npc}" if npc else ""),
               "accept": f"when the guide has you pick up \"{title}\"" + (f" from {npc}" if npc else ""),
               "complete": f"while the guide has you on \"{title}\""}[t[0]] + where
    else:
        txt = f"when the guide brings you to {npc or zone}{where}"
    if travel:
        txt += f", before {travel}"
    return txt, level, step, lo, hi


def zone_exit(n):
    """The last route point of the zone visit route point n is in: where the guide leaves that zone (its quests done there)."""
    path = RG["path"]
    k = n
    while k + 1 < len(path) and path[k + 1][4] == path[n][4]:
        k += 1
    return k


def exit_before(deadline, zone=None):
    """Where to fit a detour that must be done by route point `deadline` (2026-11-10, the user's choice: the Stockade "after Step 187
    and before step 190 which says to Fly to Redridge", where the planner had put it in the middle of the Duskwood loop): when the route
    visits `zone` before the deadline, the end of that visit (its quests done first); else the last point before the deadline where the
    route leaves a zone (a flight, the hearthstone, a boat: the travel the guide does anyway); else now."""
    path = RG["path"][:max(1, deadline)]
    if zone:
        n = next((k for k, p in enumerate(path) if p[4] == zone), None)
        if n is not None:
            return min(zone_exit(n), deadline - 1), True
    exits = [k for k in range(len(path) - 1) if path[k + 1][4] != path[k][4]]
    return (exits[-1] if exits else 0), False


def nearest_before(zone, deadline):
    """The route point before `deadline` closest to a zone (its map's middle): where to fit a catch-up in."""
    MAPS or MAPS.update(RXG.bounds())
    b = next((v for v in MAPS.values() if v["name"] == zone and v["x1"] - v["x0"] < 9000), None)
    path = RG["path"][:max(1, deadline + 1)]
    if not b or not path:
        return 0, False
    c = (b["map"], (b["x0"] + b["x1"]) / 2, (b["y0"] + b["y1"]) / 2)
    k = min(range(len(path)), key=lambda i: DT.dist((path[i][1], path[i][2], path[i][3]), c))
    return k, path[k][4] == zone


def catchup(lv):
    """What the guide did before your step that it still counts on (2026-11-10, user: "What would I need to do on Arcea to have the
    checklist and RestedXP the most sync it can be? Even if it means doing something that's not optimal"): a quest it picked up earlier
    that you do not have, when it hands that quest in ahead or takes the next part of its chain ahead (otherwise it skips those steps);
    a quest in your log whose objectives it did earlier (none left ahead) that it hands in ahead. Each with its deadline (that step), who
    gives it and where, and the route point before the deadline nearest to the giver (or to the dungeon its objectives are in).
    [{"kind": "pickup"|"finish", "quests": [(id, title)], "who", "spot", "deadline": spot dict, "why", "n", "in_zone", "dungeon"}]."""
    if not RG or not RG.get("before"):
        return []
    DT.load()
    chain_step(0)
    B, Q = RG["before"], RG["quests"]
    missed = {q for q, v in B.items() if "accept" in v and q not in COMPLETED and q not in INLOG}
    follow = {}
    for q in Q:
        pv = abs((DT.GEO.get(q) or {}).get("prev", 0))
        if pv:
            follow.setdefault(pv, []).append(q)
    dq_map = {}
    for m, qs in DQ.items():
        for q in qs:
            dq_map.setdefault(q, IP.DUNGEONS.get(IP.MAP_TO_ZONE.get(m), (None,))[0])
    ran = {dq_map[q] for q in COMPLETED if dq_map.get(q)}   # dungeons you have run: one of their quests is done
    out = []
    for q in sorted(set(B) | INLOG):
        if q in COMPLETED or not (q in missed or q in INLOG):
            continue
        a = Q.get(q, {})
        dl, why, need = None, "", "do"
        if "turnin" in a and "accept" not in a:
            dl, why = a["turnin"], f"the guide hands it in at step {a['turnin']['step']} of its {a['turnin']['lo']}-{a['turnin']['hi']} part"
            if q not in INLOG and a.get("complete_at") and a["complete_at"][0] < dl["at"]:   # its objectives come first (a dungeon run)
                c = a["complete_at"]
                dl = {"at": c[0], "step": c[1], "lo": c[2], "hi": c[3]}
                why = f"the guide does its objectives at step {c[1]} of its {c[2]}-{c[3]} part and hands it in after"
                need = "pickup"   # the guide does the rest: having it in your log is enough
        nxt = [y for y in follow.get(q, []) if "accept" in Q[y]]
        if nxt:
            y = min(nxt, key=lambda y: Q[y]["accept"]["at"])
            if dl is None or Q[y]["accept"]["at"] < dl["at"]:
                dl, need = Q[y]["accept"], "do"
                why = f"the guide takes its next part, \"{quest_title(y)}\", at step {dl['step']} of its {dl['lo']}-{dl['hi']} part"
        if dl is None:
            continue
        if q not in INLOG and "accept" in a and a["accept"]["at"] < dl["at"]:
            continue   # the guide picks it up again itself before then (Southshore at step 17 of the 31-33 part, 2026-11-14)
        if q in INLOG:
            g = DT.GEO.get(q) or {}
            d = dq_map.get(q)
            if "complete" in a or not any(o[0] in "cio" for o in g.get("objectives", [])) or not d:
                continue   # the guide has you do it on the way, it is a delivery, or its objectives are where you have been questing
            if d in ran:   # (2026-11-10: Arcea ran the Stockade, The Color of Blood done, What Comes Around... in her log to hand in at the
                continue   # guide's step: the API does not show a quest's objectives, so a quest from a dungeon you ran counts as done there)
            k, inz = exit_before(dl["at"], ENTRANCE.get(d))
            out.append({"kind": "finish", "quests": [(q, quest_title(q))], "who": "", "spot": None, "deadline": dl, "why": why,
                        "n": k, "in_zone": inz, "dungeon": d, "where": d or (B.get(q, {}).get("complete") or {}).get("zone")})
            continue
        chain = [q]   # the earlier parts you also lack, back to the chain's start
        while abs((DT.GEO.get(chain[0]) or {}).get("prev", 0)) in missed and abs(DT.GEO[chain[0]]["prev"]) not in chain:
            chain.insert(0, abs(DT.GEO[chain[0]]["prev"]))
        if len(chain) > 1:
            need = "do"   # the earlier parts have to be done and handed in
        acc = B[chain[0]]["accept"]
        item = start_item(chain[0])
        if item:   # a chain an item starts (2026-11-14: An Old History Book, a 1% drop in Duskwood, read "pick up from Milton Sheaf",
            it, who, ch, spot = item   # where the guide accepts it once the book has dropped)
            if ch < START_ITEM_SURE:
                continue   # a lucky drop is nothing to plan: the guide's steps for it wait for the drop
            k, inz = exit_before(dl["at"], spot[0] if spot else None)
            out.append({"kind": "pickup", "need": need, "quests": [(x, quest_title(x)) for x in chain], "who": who, "item": True,
                        "spot": spot, "deadline": dl, "why": why, "n": k, "in_zone": inz, "dungeon": None, "where": spot[0] if spot else None})
            continue
        k, inz = exit_before(dl["at"], acc["zone"])
        out.append({"kind": "pickup", "need": need, "quests": [(x, quest_title(x)) for x in chain], "who": acc["npc"] or "",
                    "spot": (acc["zone"], acc["x"], acc["y"]) if acc["zone"] else None, "deadline": dl, "why": why, "n": k, "in_zone": inz,
                    "dungeon": None, "where": acc["zone"]})
    seen, uniq = set(), []   # a chain listed once (its last part decides the deadline)
    for x in sorted(out, key=lambda x: -len(x["quests"])):
        key = x["quests"][0][0]
        if key not in seen and not any(q in seen for q, _ in x["quests"]):
            seen |= {q for q, _ in x["quests"]}
            uniq.append(x)
    return sorted(uniq, key=lambda x: x["n"])


def chain_name(qs):
    """One name for a run of quests: "A", "A → B", or "A (5 parts)" when the parts share the name."""
    ts = [t for _, t in qs]
    if len(ts) == 1:
        return ts[0]
    return f"{ts[0]} ({len(ts)} parts)" if len(set(ts)) == 1 else f"{ts[0]} → {ts[-1]} ({len(ts)} parts)"


def catchup_line(x):
    names = chain_name(x["quests"])
    lv = sorted(int((CQUESTS.get(q) or {}).get("quest_level") or 0) for q, _ in x["quests"])
    lv = [v for v in lv if v]
    if lv:
        names += f", level {lv[0]}" + (f"-{lv[-1]}" if lv[-1] != lv[0] else "")
    dl = x["deadline"]
    if x["kind"] == "finish":
        what = (f"**Finish {names}**" + (f" in {x['dungeon']}" if x["dungeon"] else f" ({x['where']})" if x.get("where") else "")
                + " (if you have not yet)")
    else:
        what = f"**{catchup_verb(x)} {names}**" + catchup_where(x)
    return what, f"before step {dl['step']} of the guide's {dl['lo']}-{dl['hi']} part: {x['why']}"


def catchup_verb(x):
    """"Pick up" when having the quest in your log is enough (the guide does its objectives), else "Do": its objectives, and every
    earlier part you lack handed in (2026-11-14: "Pick up The Tower of Althalaxx (4 parts)" needed four quests done)."""
    return "Pick up" if x.get("need") == "pickup" else "Do"


def catchup_where(x):
    """Where a catch-up starts: ", starting with <item>, a drop from ..." for a chain an item starts, else " from <NPC> (Zone x, y)"."""
    if x.get("item"):
        return f", starting with {x['who']}"
    return (f" from {x['who']}" if x["who"] else "") + (f" ({spot_text(x['spot'])})" if x["spot"] else "")


# 2026-11-15 (user: "RestedXP does a very good job of giving the most optimal leveling path so I don't know if diverging from it is worth
# it", then "yes, make that change"): the checklist and this page list only what is worth leaving the guide for: catching up with it
# ("sync") and gear the plan counts on that the route leaves out ("gear": the gear plan's quests, side trips for a reward or drops, detours
# for the gear). Detours for experience ("xp": 2-3 minutes each on Arcea's route, inside the estimate's own error) and the guide's own
# dungeons ("guide": RestedXP runs them) are still computed and not shown.
LEAVE_GUIDE = ("sync", "gear")


def off_guide(tl):
    return [r for r in tl or [] if r.get("why") in LEAVE_GUIDE]


def timeline(sched, events, lv):
    """Everything that leaves the guide, in route order (2026-11-10, user: "I want to know at each point in time, according to the RestedXP
    route, when should I be detouring. And exactly what step of the guide ... that include the stuff that is clearly worth it and the stuff
    that is 'fun upgrades/experience' even if not 100% optimal"): dungeons (the guide's own where it runs them, side trips the next time
    the guide has you in the dungeon's zone), detours (detours.py, from the route point they start at), and the gear plan's quests off the
    route. Rows: {"n" (route index), "kind", "key", "title", "tag", "facts", "where", "pickups", "anchor", "level", "step", "lo", "hi"};
    the dungeon list's run level is set to the row's (one level for one dungeon on the page)."""
    if not RG or not RG.get("path"):
        return []
    path, rows = RG["path"], []

    def first_at(level, zone=None):
        return next((n for n, p in enumerate(path) if p[0] >= level and (zone is None or p[4] == zone)), None)

    def add(n, kind, key, title, tag, facts="", where="", pickups=(), why="xp"):   # why: sync, gear, xp, guide (LEAVE_GUIDE)
        if n is None:
            return None
        txt, level, step, lo, hi = route_anchor(n)
        rows.append({"n": n, "kind": kind, "key": key, "title": title, "tag": tag, "facts": facts, "where": where, "pickups": list(pickups),
                     "anchor": txt, "level": level, "step": step, "lo": lo, "hi": hi, "why": why})
        return level
    gear_q = {}   # the gear plan's quest rewards, by quest title (a quest can carry another id in the dungeon lists)
    gear_ids = set()   # and by quest id (a detour that hands one in is a detour for the gear)
    for e in events:
        s0 = primary(e)
        if s0["kind"] == "quest" and isinstance(s0.get("quest"), int):
            gear_q[quest_title(s0["quest"])] = upgrade_name(e)[0]
            gear_ids.add(s0["quest"])
    in_dungeon = set()
    on_detour = {t for x in DETOURS["list"] for _, t in x["quests"]}   # a quest with its own detour row is not listed again
    cu = catchup(lv)
    need_by = {}   # a dungeon a catch-up's objectives are in: run it by then
    for x in cu:
        if x["kind"] == "finish" and x["dungeon"]:
            if x["dungeon"] not in need_by or x["n"] < need_by[x["dungeon"]][0]:
                need_by[x["dungeon"]] = (x["n"], x)
    for r in sched:
        if r["verdict"] == "skip":
            continue
        in_dungeon |= {q["title"] for q in r["quests"]}
        took = sum(1 for x in r["quests"] if x["route"] and not x["grey"])
        door = ENTRANCE.get(r["zone"])
        if r["verdict"] == "guide":
            d = RG["dungeons"].get(r["zone"]) or {}
            done = [RG["quests"][q["id"]]["complete_at"][0] for q in r["quests"] if q.get("route") and "complete_at" in RG["quests"].get(q["id"], {})]
            n = d["at"][0] if d.get("at") else (min(done) if done else first_at(r["run"]))
        else:   # a side trip starts the next time the guide has you at the dungeon's door, from its lowest level on
            n = next((k for k, p in enumerate(path) if p[4] == door and max(lv, r["lo"]) <= p[0] <= r["run"] + 3), None) if door else None
            n = zone_exit(n) if n is not None else first_at(max(r["run"], r["lo"]))   # (the zone's quests first, then the side trip)
        sync = need_by.get(r["zone"])
        if sync and (n is None or sync[0] < n):   # a quest in your log the guide hands in before that: run it in time
            n = sync[0]
        if n is None:
            continue
        picks, count = [], 0
        for c in open_chains(r):   # what you can have in your log by then: started on the way, or a trip to its town first
            c["quests"] = [x for x in c["quests"] if x["title"] not in on_detour]
            if not c["quests"]:
                continue
            c["gear"] = next((gear_q[x["title"]] for x in c["quests"] if x["title"] in gear_q), None)
            z = c.get("zone")
            if z == r["zone"] and not c["log"]:   # its giver or start item is inside: it starts during the run (Bijou, the Essence of
                picks.append(INSIDE + group_text(c))   # Eranikus: listed as "a trip to Sunken Temple first", 2026-11-14)
                count += len(c["quests"])
                continue
            if c["log"] or not z or z == door or any(p[4] == z for p in path[:n + 1]):
                pass
            elif z not in CAPITALS and any(p[4] == z for p in path[n + 1:]):
                continue   # it starts in a zone the guide only takes you to after this run (a capital is a short trip: listed)
            else:
                c["start"] += f"; a trip to {z} first"
            picks.append(f"already in your log: {group_text(c, short=True)}" if c["log"] else group_text(c))
            count += len(c["quests"])
        r["picks"] = picks   # (the dungeon list shows the same)
        if r["verdict"] == "guide":
            facts = "your guide runs it here" + (f" and takes {took} of its quests" if took else "")
            level = add(n, "dungeon", "dg" + r["zone"], f"Run {r['zone']}", "with your guide", facts, pickups=picks,
                        why="sync" if sync else "guide")
            if sync:
                rows[-1]["facts"] += f"; finish {sync[1]['quests'][0][1]} here: {catchup_line(sync[1])[1]}"
        else:
            reason = r["why"].split(";")[0].replace("worth a detour: ", "")
            tag = "side trip"
            for_xp = "quests at full experience" in reason   # else a quest reward the plan counts on, or drops worth the run
            if reason.startswith("worth a detour for") and "quests at full experience" in reason:   # recounted: what you can have by then
                if not count:
                    r["verdict"], r["why"] = "skip", "none of its quests can be in your log by then"
                    continue
                new = f"{count} quest{'s' if count != 1 else ''} at full experience"
                if count < DUNGEON_QUEST_BAR:   # (2026-11-10, user: "slightly less optimal, but it's still fun and somewhat easy")
                    tag = "worth it if you like it"
                r["why"] = r["why"].replace(reason, ("worth it if you like it: " if count < DUNGEON_QUEST_BAR else "worth a detour for ") + new, 1)
                reason = new
            reason = reason.replace("worth a detour for ", "")
            notes = [x.strip() for x in r["why"].split(";")[1:]]
            facts = reason + "".join(f"; {x}" for x in notes if x.startswith("tick it"))
            if any("you have passed" in x for x in notes):
                facts += "; your guide ran it before where you are now"
            if sync:
                tag = "to stay in step with your guide"
                facts += f"; finish {sync[1]['quests'][0][1]} here, {catchup_line(sync[1])[1]}"
            level = add(n, "dungeon", "dg" + r["zone"], f"Run {r['zone']}", tag, facts, pickups=picks,
                        why="sync" if sync else "xp" if for_xp else "gear")
        if level is not None:
            r["run"] = level
    for x in DETOURS["list"]:
        add(x["anchor"], "detour", "det" + "-".join(str(q) for q, _ in x["quests"]), " → ".join(t for _, t in x["quests"]),
            {"clear": "clear win", "easy": "worth it if you like it", "gear": "for the gear"}[x["tier"]], detour_facts(x), detour_where(x),
            why="gear" if x["tier"] == "gear" or any(q in gear_ids for q, _ in x["quests"]) else "xp")
    listed = {q for x in DETOURS["list"] for q, _ in x["quests"]}
    judged = DETOURS["stats"].get("judged", {})
    for e in events:   # the gear plan's quests off the route
        s0 = primary(e)
        q = s0.get("quest") if s0["kind"] == "quest" else None
        if not isinstance(q, int) or not e.get("off_route") or q in listed or quest_title(q) in in_dungeon:
            continue
        what, _ = upgrade_name(e)
        if q in judged:
            x = judged[q]
            add(x["anchor"], "gear", f"gq{q}", " → ".join(t for _, t in x["quests"]), "for the gear, at a cost", detour_facts(x), detour_where(x),
                why="gear")
        else:   # where its chain starts (2026-11-14: The God Hakkar read "who gives it is not in the data" while the gear plan named
            st = chain_step(q)   # Yeh'kinya, who starts its chain)
            head = st[0] if st else q
            ok, how, hz = chain_start(head, lv)
            n = first_at(max(e["get_at"], lv), s0.get("zone")) or first_at(max(e["get_at"], lv), hz) or first_at(max(e["get_at"], lv))
            start = (f"start with \"{quest_title(head)}\"" + (", which " if how.startswith("starts") else " ") + how
                     if head != q and how else how)
            add(n, "gear", f"gq{q}", quest_title(q), "for the gear",
                f"rewards {what}; " + (start if start else
                                       f"who gives it is not in the data, so ask around while the guide has you in {s0.get('zone') or 'its zone'}"),
                why="gear")
    for x in cu:   # catch-ups at the route point that suits them (a dungeon's quests are in its row)
        if (x["kind"] == "finish" and x["dungeon"]) or all(t in in_dungeon for _, t in x["quests"]):
            continue
        _, when = catchup_line(x)
        lvs = sorted(v for v in (int((CQUESTS.get(q) or {}).get("quest_level") or 0) for q, _ in x["quests"]) if v)
        name = chain_name(x["quests"]) + (f", level {lvs[0]}" + (f"-{lvs[-1]}" if lvs[-1] != lvs[0] else "") if lvs else "")
        title = ("Finish " if x["kind"] == "finish" else catchup_verb(x) + " ") + name
        where = catchup_where(x).lstrip(", ").strip()
        how = "" if x["in_zone"] else (f"a trip to {x['where']}" if x["where"] in CAPITALS else f"a detour to {x['where']}") if x["where"] else ""
        add(x["n"], "catchup", "cu" + "-".join(str(q) for q, _ in x["quests"]), title, "catch up with your guide",
            when[0].upper() + when[1:] + (f"; {how} from here" if how else ""), where, why="sync")
    order = {"catchup": 0, "dungeon": 1, "detour": 2, "gear": 3}
    rows.sort(key=lambda r: (r["n"], order[r["kind"]]))
    return rows


def detour_facts(x):
    t = f"+{x['xp']:,} experience in about {x['minutes']:.0f} min"
    if x["gear"]:
        t += (f"; rewards {', '.join(x['gear'])} (about {x['gear_minutes']} min of faster killing)"
              + (f", about {x['score']:.0f} min ahead in all" if x["score"] >= 0.5 else f", about {-x['score']:.0f} min behind in all"))
    else:
        t += f", about {x['saves']:.0f} min ahead of your usual pace" if x["saves"] >= 0.5 else ", about your usual pace"
    return t


def detour_where(x):
    if x["inlog"]:
        return "already in your log"
    g = (x["giver"] or "").split(" / ")[0]
    return (f"from {g}" if g else "") + (f" ({x['start'][0]} {x['start'][1]:.1f}, {x['start'][2]:.1f})" if x.get("start") else "")


INSIDE = "inside the run: "   # a dungeon chain whose giver or start item is inside the dungeon (no pick-up before the run)


def split_picks(picks):
    """(to pick up before the run, already in your log, starting inside the run) of a dungeon's pick list."""
    log = "already in your log: "
    return ([x for x in picks if not x.startswith((log, INSIDE))], [x[len(log):] for x in picks if x.startswith(log)],
            [x[len(INSIDE):] for x in picks if x.startswith(INSIDE)])


def timeline_line(r):
    out = (f"**Level {r['level']}, step {r['step']} of the guide's {r['lo']}-{r['hi']} part**, {r['anchor']}: **{r['title']}** ({r['tag']}). "
           f"{r['facts'][0].upper() + r['facts'][1:] if r['facts'] else ''}")
    if r["where"]:
        out += f"; {r['where']}"
    new, have, inside = split_picks(r["pickups"])
    if new or have:
        out += ". Pick up first: " + "; ".join(new + [f"already in your log: {x}" for x in have])
    if inside:
        out += ". Starts inside the run: " + "; ".join(inside)
    return out + "."


def detour_text(x, short=False):
    """One detour for the page and the checklist (short: in the timeline, whose anchor already says when and where)."""
    names = " → ".join(t for _, t in x["quests"])
    kind = {"clear": "clear win", "easy": "worth it if you like it", "gear": "for the gear", "cost": "for the gear, at a cost"}[x["tier"]]
    where = f"from {x['giver']}" if x["giver"] and not x["inlog"] else ("already in your log" if x["inlog"] else "")
    if x["start"] and not x["inlog"]:
        where += f" ({x['start'][0]} {x['start'][1]:.1f}, {x['start'][2]:.1f})"
    near = f" while your route is in {x['near'][0]}" if x.get("near") else ""
    gain = (f"saves about {x['saves']:.0f} min against your usual pace" if x["saves"] >= 0.5 else
            f"about {-x['saves']:.0f} min slower than your usual pace" if x["saves"] <= -0.5 else "about your usual pace")
    gear = (f"; rewards {', '.join(x['gear'])} from your gear plan (about {x['gear_minutes']} min of faster killing"
            + (f", so about {x['score']:.0f} min ahead in all)" if x["score"] >= 0.5 else f", still about {-x['score']:.0f} min behind in all)")
            if x["gear"] else "")
    parts = f"{len(x['quests'])}-part chain: " if len(x["quests"]) > 1 else ""
    if short:
        near = ""
    return (f"**{names}** ({kind}): {parts}{where}" + ("" if short else f", around level {x['level']}{near}") + f". About {x['xp']:,} experience for about "
            f"{x['minutes']:.0f} min ({x['travel']:.0f} of it walking); {gain}{gear}.")


def dungeon_lines(sched):
    o = []
    skip = [r for r in sched if r.get("verdict") == "skip"]
    for r in sched:
        if r.get("verdict") == "skip":
            continue
        o += [f"- **{r['zone']}** ({r['lo']}-{r['hi']}{', estimated' if r.get('estimated') else ''}), run at level {r['run']}: {r.get('why', '')}"
              + (f"; its drops are worth about {r['worth']} min on average" if r["worth"] and "drops" not in r.get("why", "") else "") + "."]
        if r.get("picks") is not None:   # the timeline's list: what you can have in your log when you get there
            took = sum(1 for x in r["quests"] if x["route"] and not x["grey"])
            new, have, inside = split_picks(r["picks"])
            if new:
                o += ["  - Pick up first: " + "; ".join(new)]
            if have:
                o += ["  - Already in your log: " + "; ".join(have)]
            if inside:
                o += ["  - Starts inside the run: " + "; ".join(inside)]
        elif r.get("chains"):
            mine = open_chains(r)
            took = sum(1 for x in r["quests"] if x["route"] and not x["grey"])
            inside = [c for c in mine if not c["log"] and c.get("zone") == r["zone"]]
            if [c for c in mine if not c["log"] and c not in inside]:
                o += ["  - Pick up first: " + "; ".join(group_text(c) for c in mine if not c["log"] and c not in inside)]
            if inside:
                o += ["  - Starts inside the run: " + "; ".join(group_text(c) for c in inside)]
            if [c for c in mine if c["log"]]:
                o += ["  - Already in your log: " + "; ".join(group_text(c, short=True) for c in mine if c["log"])]
            if took:
                o += [f"  - Your guide picks up {took} of its quests itself."]
        if r.get("dropped"):
            o += ["  - Left out: " + "; ".join(r["dropped"])]
        o += [f"  - Drop: {x}" for x in r["drops"]]
    if skip:
        o += ["- Skip: " + "; ".join(f"{r['zone']} ({r['why']})" for r in skip) + "."]
    return o + [""]


def dungeon_runs(bonus):
    """[{zone, lo, hi, worth, own, items}] from the drops worth chasing: one run's worth adds up each drop's minutes over the sure plan
    times its drop chance in that dungeon (25% where the chance is unknown)."""
    runs = {}
    for e in bonus:
        for s in new_sources(e):
            if s["kind"] == "dungeon":
                runs.setdefault((s["zone"], s["lo"], s["hi"]), []).append((s, e))
    out = []
    for (z, lo, hi), ev in sorted(runs.items(), key=lambda kv: kv[0][1]):
        merged = {}
        for s_, e in ev:
            merged.setdefault(id(e), (e, []))[1].append(s_)
        def other(e):   # the other half of a weapon pair that drops elsewhere: (its dungeons, its chance within two runs)
            rest = [it for it in new_pieces(e) if not any(x["kind"] == "dungeon" and x["zone"] == z for x in it["sources"])]
            rest = [it for it in rest if it["sources"] and all(x["kind"] == "dungeon" for x in it["sources"])]
            if not rest:
                return None, 1.0
            zs = sorted({x["zone"] for it in rest for x in it["sources"]})
            pr = 1.0
            for it in rest:
                pr *= max((x.get("chance") or 0.25) for x in it["sources"])
            return " or ".join(zs), pr

        worth = sum(e["bonus_minutes"] * max((x.get("chance") or 0.25) for x in ss) * other(e)[1] for e, ss in merged.values())
        items = []
        for e, ss in merged.values():
            what, _ = upgrade_name(e)
            ch = max((x.get("chance") or 0.25) for x in ss)
            oz, op = other(e)
            items.append(f"{what} ({e['slot']}, from level {e['level']}; {' or '.join(x['boss'] for x in ss)}, "
                         + (f"{ch:.0%} drop" if any(x.get("chance") for x in ss) else f"drop chance unknown, counted as {ch:.0%}")
                         + (f"; the other half drops in {oz}, {op:.0%}" if oz else "")
                         + f"): over your {e['over']}, {pct(e['bonus_gain'])} {SHORT}, about {e['bonus_minutes']:.0f} min saved "
                         + ("with both halves" if oz else "if it drops"))
        out.append({"zone": z, "lo": lo, "hi": hi, "worth": round(worth), "own": worth >= MIN_MINUTES, "items": items,
                    "first": min(e["level"] for e, _ in merged.values())})
    return out


DQ = {}


def load_dq():
    """DQ: {dungeon map id: [quest ids]} from dungeon_quests.csv (a quest whose target, item or giver exists only in that dungeon)."""
    if not DQ:
        for r in csv.DictReader(open(IP.RAW / "dungeon_quests.csv", encoding="utf-8")):
            DQ.setdefault(int(r["map"]), []).append(int(r["quest"]))


def dungeon_schedule(cfg, lv, runs, events=None):
    """Every leveling dungeon you have not outgrown, once (2026-11-09, user: "Make sure dungeons are not being skipped, because dungeons
    are so worth to run at least once. The XP from the dungeon quests is significant, and I can collect the quest and then run the dungeon
    once"): the level to run it (the middle of its quests you have not done, inside its range, not below yours), its quests with where
    each starts (dungeon_quests.csv: a quest whose target, item or giver exists only in that dungeon), and its drops worth hoping for
    (`runs`, dungeon_runs). A dungeon whose quests are all five or more levels below you and that drops nothing for you is left out."""
    load_dq()
    chain_step(0)   # (loads the quest tables)
    race_mask = 77 if cfg["faction"] == "alliance" else 178
    cls_bit = 1 << (IP.CLASS_ID[cfg["class"]] - 1)
    drops = {r["zone"]: r for r in runs}
    out = []
    todo = [(IP.DUNGEONS[zid], DQ.get(m, []), False) for m, zid in IP.MAP_TO_ZONE.items() if zid in IP.DUNGEONS]
    extra = {n: [r["quest"] for r in rows] for n, rows in (RG or {}).get("extra", {}).items()}
    if RG:   # Forever's own dungeons (2026-11-10): the levels of the RestedXP section that runs them, the top of the range estimated
        known = {d[0][0] for d in todo}
        todo += [((n, RG["runs"][n][0], RG["runs"][n][1] + 6, None), [], True) for n in extra if n not in known and n in RG["runs"]]
    fq = IP.forever_quests(sorted({q for v in extra.values() for q in v if q not in CQUESTS})) if extra else {}
    for (name, lo, hi, side), dq, est in todo:
        if (side and side != cfg["faction"]) or hi < lv:
            continue
        qs = {}
        for q in dq + [x for x in extra.get(name, []) if x not in dq]:   # RestedXP's dungeon quest guide adds what the Classic data misses
            r = CQUESTS.get(q)
            if r:
                rr, rc, ql, title = int(r["required_races"] or 0), int(r["required_classes"] or 0), int(r["quest_level"] or 0), r["title"]
            elif (fq.get(str(q)) or {}).get("title"):   # a quest Forever added: Blizzard's title; its level where the route takes it, else
                rr = rc = 0                              # one above the level the guide runs the dungeon at
                title = fq[str(q)]["title"]
                acc = (RG["quests"].get(q) or {}).get("accept")
                ql = acc["level"] if acc else (RG["runs"].get(name) or (lo, hi))[0] + 1
            else:
                continue
            if (rr and not rr & race_mask) or (rc and not rc & cls_bit) or ql >= 60 or ql < lo - 10 or q in COMPLETED:
                continue   # (a quest far below the dungeon is a data quirk: Rocknot's Ale reads level 1)
            qs.setdefault(title, (q, ql))
        levels = sorted(v[1] for v in qs.values() if v[1] > 0)
        run = levels[len(levels) // 2] if levels else (lo + hi) // 2
        dr = drops.get(name)
        if dr:   # a drop you would wear early pulls the run forward (Scarlet Monastery's one Alliance quest is level 40, its Library drop 32)
            run = min(run, dr["first"] + 1)
        run = max(lv, lo + 2, min(run, hi - 2))
        if RG:   # the route step by step (2026-11-10): its own dungeons and the ones ticked in your RestedXP profile, from where you are
            gl = (RG["dungeons"].get(name) or {}).get("level")
        else:   # the route's section names (2026-11-09)
            gl = rxp.dungeon_level(ROUTE, name) if ROUTE else None
        if gl is not None:
            run = max(lv, gl)
        quests = []
        for title, (q, ql) in sorted(qs.items(), key=lambda kv: kv[1][1]):
            st = chain_step(q)
            first = st[0] if st and st[0] != q and st[0] not in INLOG else q
            giver = giver_text(first)
            start = ""
            if first != q:
                t1 = (CQUESTS.get(first) or {}).get("title", first)
                start = (f"start with part 1" if t1 == title else f"start with \"{t1}\"") + (f" from {giver}" if giver else "")
            elif giver:
                start = f"from {giver}"
            quests.append({"id": q, "title": title, "level": ql, "start": start, "grey": ql < run - 5, "log": q in INLOG,
                           "route": bool(RG) and "accept" in (RG["quests"].get(q) or {})})
        # chains (2026-11-10): one entry per chain, started where its first quest starts; a chain you cannot start is left out
        groups, dropped = {}, []
        for x in quests:
            groups.setdefault(chain_head(x["id"]), []).append(x)
        chains = []
        for h, xs in groups.items():
            ok, how, hz = chain_start(h, lv)
            first = min(xs, key=lambda x: (x["level"], x["id"]))
            if not ok:
                dropped.append(f"{quest_title(h)}" + (f" ({len(xs)} quests here)" if len(xs) > 1 else "") + f": it {how}")
                continue
            if first["start"] and (h in COMPLETED or not how):   # (already started: where the next part is picked up)
                how = first["start"]
            elif h not in {x["id"] for x in xs} and how:   # the chain starts before the dungeon's part: name its first quest
                how = f"start with \"{quest_title(h)}\"" + (", which " if how.startswith("starts") else " ") + how
            chains.append({"head": h, "quests": sorted(xs, key=lambda x: (x["level"], x["id"])), "start": how, "zone": hz,
                           "route": all(x["route"] for x in xs), "grey": all(x["grey"] for x in xs), "log": any(x["log"] for x in xs)})
        quests = [x for c in chains for x in c["quests"]]
        if not dr and not any(not x["grey"] for x in quests):
            continue
        # do it or not (2026-11-09, user: "I just want to do the ones you deem worth it and that I should actually do or wait for the
        # guide"): the guide's own dungeons; a side trip only for a quest reward the gear plan counts on, drops worth MIN_MINUTES on
        # average, or three quests at full experience; never one you will have outgrown (its mobs and most quests grey)
        full = [q for q in quests if not q["grey"]]
        gear_q = sorted({upgrade_name(e)[0] for e in events or [] if primary(e)["kind"] == "quest" and primary(e).get("zone") == name})
        worth = (dr or {}).get("worth", 0)
        on = sum(1 for x in quests if x["route"] and not x["grey"])
        done_here = sorted({(CQUESTS.get(q) or {}).get("title") or str(q) for q in dq + extra.get(name, []) if q in COMPLETED})
        if ROUTE and gl is not None:
            verdict, why = "guide", "your RestedXP guide runs it then" + (f" and picks up {on} of its quests" if on else "")
        elif done_here:   # run once (2026-11-10, user's rule: every dungeon "at least once"): one of its quests is done
            verdict, why = "skip", "you ran it: " + ", ".join(done_here[:3]) + (" are done" if len(done_here) > 1 else " is done")
        elif run >= hi:
            verdict, why = "skip", "you will have outgrown it"
        elif gear_q:
            verdict, why = "do", "worth a detour for " + ", ".join(gear_q) + " from its quests"
        elif worth >= MIN_MINUTES:
            verdict, why = "do", f"worth a detour: its drops are worth about {worth} min on average"
        elif len(full) >= DUNGEON_QUEST_BAR:
            verdict, why = "do", f"worth a detour for {len(full)} quests at full experience, and its kills give 50% more since 2026-11-09"
        else:
            verdict, why = "skip", (f"only {len(full)} quest{'s' if len(full) != 1 else ''} at full experience" if full else "no quests for you")
            why += " and " + (f"drops worth about {worth} min" if worth else "no drops for you")
        if RG and verdict == "do" and name in RG["taggable"]:
            why += "; tick it in RestedXP's dungeon settings and the guide picks up its quests on the way"
        if RG and gl is None and name in RG["behind"]:
            b = RG["behind"][name]
            why += f"; your guide ran it at step {b[0]} of its {b[1]}-{b[2]} part, which you have passed"
        elif RG and gl is None and name in RG["runs"] and RG["runs"][name][1] < lv:
            why += f"; your guide ran it at {RG['runs'][name][0]}-{RG['runs'][name][1]}"
        out.append({"zone": name, "lo": lo, "hi": hi, "estimated": est, "run": run, "quests": quests, "chains": chains, "dropped": dropped,
                    "drops": (dr or {}).get("items", []),
                    "worth": worth, "guide": None if not ROUTE else gl is not None, "verdict": verdict, "why": why})
    return sorted(out, key=lambda x: (x["run"], x["lo"]))


def certainty(e, owned=None):
    """The chance you have an upgrade when the plan wears it: 1 for a quest, a craft or a buy; for a piece only a dungeon drops, its drop
    chance in your one run of that dungeon (Classic's data, 25% where it has none; the user runs each dungeon once with its quests). best_chain weighs a chain's minutes by it,
    so a sure upgrade wins a close call against a drop (2026-11-09); the page still names a fallback for a drop that does not come."""
    out = 1.0
    for it in new_pieces(e, owned):
        srcs = it["sources"]
        if all(s["kind"] == "dungeon" for s in srcs):
            out *= min(1.0, max((s.get("chance") or 0.25) for s in srcs))
    return out


def best_chain(evs, at):
    """The upgrades of one slot worth making (see plan): the subset of the slot's upgrades, in level order, that saves the most minutes
    of killing, each upgrade in it worn MIN_LASTS levels and saving MIN_MINUTES over the item it replaces; their replaces, gain and until
    set to that chain."""
    import functools
    n = len(evs)
    base = evs[0]["prev"]

    def items(c):
        return base if c is None else [evs[c]["item"], evs[c].get("off")]

    def held(c):   # the item ids you hold after step c (None: what you wear now)
        return {x["id"] for x in items(c) if x and x.get("id") is not None}

    def gain(p, c):
        e = evs[c]
        wl = at(e["level"])
        prev = base if p is None else [evs[p]["item"], evs[p].get("off")]
        pv = sum(value((x or {}).get("stats"), wl) for x in prev)
        nv = value(e["item"]["stats"], wl) + (value(e["off"]["stats"], wl) if e.get("off") else 0.0)
        return (nv - pv) / wl["time"]

    def val(its, L):
        return sum(value((x or {}).get("stats"), at(L)) for x in its)

    def run(allowed, fb):
        """The chain over the steps in `allowed` that saves the most minutes in all. fb(L): what you wear at level L when a dungeon drop
        does not come (the sure plan; None in the sure plan's own run, which has no drops)."""
        allowed = sorted(allowed)

        def worth(p, c, nx):
            """c worn after p (None: the item the slot holds first) until nx (None: 60): None when the swap fails a bar (the minutes it
            saves over p, the gold test), else what it saves over the slot's first item while worn. A drop counts at its chance of
            coming within two runs, over what the sure plan wears then (you wear that when it does not drop; 2026-11-09: counting a
            missed drop as nothing, or as an earlier drop that may not have come either, had swapped a free quest staff for a chain
            of drops)."""
            L0 = evs[c]["level"]
            end = 60 if nx is None else evs[nx]["level"]
            if end - L0 < MIN_LASTS:
                return None
            m = span_minutes(items(c), items(p), L0, end, at)
            if gain(p, c) < UPGRADE or m < MIN_MINUTES:
                return None
            price = price_of(evs[c], held(p))   # a buy must also pay for itself (pays_for_itself), or a dearer one could push out a
            if price and m < price / (income_per_level(L0, QPL) or 1) * minutes_per_level(L0, at):   # cheaper one the gold test
                return None                                                                           # then rejected
            cert = certainty(evs[c], held(p))
            if cert >= 1 or fb is None:
                return span_minutes(items(c), base, L0, end, at)
            return sum((val(fb(L), L) - val(base, L) + cert * max(0.0, val(items(c), L) - val(fb(L), L))) * kills_per_level(L)
                       for L in range(L0, end)) / 60

        @functools.lru_cache(maxsize=None)
        def best(p, c):   # (minutes, chain) choosing c after p, then the best rest
            top = None
            for nx in [x for x in allowed if x > c] + [None]:
                m = worth(p, c, nx)
                if m is None:
                    continue
                rest = (0.0, ()) if nx is None else best(c, nx)
                if rest[0] < 0:
                    continue
                if top is None or m + rest[0] > top[0]:
                    top = (m + rest[0], (c,) + rest[1])
            return top or (-1.0, ())

        return max([best(None, c) for c in allowed] + [(0.0, ())], key=lambda t: t[0])[1]

    sure_pick = run([i for i in range(n) if certainty(evs[i], set()) >= 1], None)

    def fb(L):
        on = [k for k in sure_pick if evs[k]["level"] <= L]
        return items(on[-1]) if on else base

    pick = run(range(n), fb)
    # the upgrades passed over, each against the item the chain has on at its level, with the reason (user 2026-11-09: "if something like
    # the headpiece ... is the best gear until level 35 ... then that's okay. I just want there to be a reason for me keeping it")
    for c in range(n):
        if c in pick:
            continue
        on = [k for k in pick if evs[k]["level"] <= evs[c]["level"]]
        if not on:
            continue
        k = on[-1]
        nxt = [x for x in pick if evs[x]["level"] > evs[c]["level"]]
        end = evs[nxt[0]]["level"] if nxt else 60
        g = gain(k, c)
        m = span_minutes(items(c), items(k), evs[c]["level"], end, at)
        price = price_of(evs[c], held(k))
        earn = price / (income_per_level(evs[c]["level"], QPL) or 1) * minutes_per_level(evs[c]["level"], at) if price else 0
        if evs[c]["level"] == evs[k]["level"] and g <= 0:
            continue   # a runner-up at the same level the chain beat outright
        if g < UPGRADE:
            why = f"only {pct(g)} {SHORT}"
        elif certainty(evs[c], held(k)) < 1 and m >= MIN_MINUTES:
            why = f"{pct(g)} {SHORT}, but a dungeon drop ({certainty(evs[c], held(k)):.0%} in your run): a surer upgrade saves more on average"
        elif m < MIN_MINUTES:
            why = f"{pct(g)} {SHORT}, saves about {m:.0f} min before {'60' if not nxt else 'its next upgrade'}"
        elif price and m < earn:
            why = f"{pct(g)} {SHORT}, saves about {m:.0f} min, but its {AH.money(price)} takes about {earn:.0f} min of play to earn"
        else:
            why = f"{pct(g)} {SHORT}, but a later upgrade of the slot saves more without it"
        evs[k].setdefault("passed", []).append((evs[c]["level"], evs[c]["item"]["name"], g, why))
    out = []
    for k, c in enumerate(pick):
        e, p = evs[c], (pick[k - 1] if k else None)
        e["gain"] = gain(p, c)
        e["replaces"] = evs[0]["replaces"] if p is None else evs[p]["item"]["name"]
        e["prev"] = base if p is None else [evs[p]["item"], evs[p].get("off")]
        e["owned"] = held(p)
        e["until"] = evs[pick[k + 1]]["level"] if k + 1 < len(pick) else None
        out.append(e)
    return out


# ---------------------------------------------------------------------------------------------------------------- page
def pick(cfg, level=None):
    """(build, order, provisional, rotation): the spec's leveling page pick (level_guides.pick), or for a character with
    "talent_order": {"kind": "tank", "build", "entry", "tree"} that tank build in the tank-first order (2026-11-09, Tara), or with
    {"kind": "chosen", ...} the character's own path (chosen_order; the page pick's id stays, so item values are the page build's) and
    the rotation it plays at `level`."""
    t = cfg.get("talent_order")
    if t and t.get("kind") == "tank":
        import tank_order as TO
        return TO.build_of(cfg["class"], t["build"]), TO.order(cfg["class"], t["build"], t["entry"], t["tree"]), False, t.get("rotation", "group tank")
    sys.path.insert(0, str(DATA))
    import level_guides as LG
    if t and t.get("kind") == "chosen":
        b, _, _, rot = LG.pick(cfg["class"], cfg["spec"])
        alloc, order = chosen_order(cfg)
        return dict(b, allocation=alloc, chosen=t.get("name", "your own path")), order, False, rotation_at(cfg, level, rot)
    return LG.pick(cfg["class"], cfg["spec"])


def chosen(cfg):
    """The character's chosen talent path (talent_order {"kind": "chosen"}, 2026-11-22: Arcea's own build for questing and open-world
    PvP, the user's decision over the page's order), else None. A chosen path keeps its order: no race of the next points, no respec
    check against the page."""
    t = cfg.get("talent_order") or {}
    return t if t.get("kind") == "chosen" else None


def guide_spec(cfg, L=None):
    """The spec whose by-level guide the character plays at level L: a chosen path's "rotations" ([from, rotation, spec]; Arcea: the Frost
    page's until 46, the Arcane-Frost one from 47, once Missile Barrage is in), else the character's spec."""
    t = chosen(cfg)
    if t and t.get("rotations") and L is not None:   # (below the first entry's level: the first entry)
        return ([s for f, _, s in t["rotations"] if f <= L] or [t["rotations"][0][2]])[-1]
    return cfg["spec"]


def rotation_at(cfg, L, default):
    t = chosen(cfg)
    if t and t.get("rotations"):
        return ([r for f, r, _ in t["rotations"] if f <= (L or 60)] or [t["rotations"][0][1]])[-1]
    return default


def chosen_order(cfg):
    """(allocation, order) of a chosen path: "respec_to" [[talent, ranks]] (the build at the respec level) from level 10, row by row (any
    legal order holds the same build at the respec level), then "then" (one talent a level). Every level is checked legal
    (validate_builds.check_state); a path that is not raises."""
    import page_lint as PL
    import validate_builds as VB
    t = chosen(cfg)
    where = {x["name"]: (tr["name"], x["row"], i) for tr in PL.talents(cfg["class"]) for i, x in enumerate(tr["talents"])}
    first = sorted(t["respec_to"], key=lambda p: (where[p[0]][1], where[p[0]][2]))
    pts = [n for n, k in first for _ in range(k)] + list(t["then"])
    if len(pts) != 51:
        raise ValueError(f"{cfg['name']}: the chosen path holds {len(pts)} points, not 51")
    trees, errs, state, order = VB.load_forever()[cfg["class"]], [], {}, []
    for L, n in enumerate(pts, start=10):
        tree = where[n][0]
        state.setdefault(tree, {})[n] = state.get(tree, {}).get(n, 0) + 1
        VB.check_state(trees, {k: dict(v) for k, v in state.items()}, f"{cfg['name']} chosen path at {L}", errs)
        if order and order[-1]["talent"] == n and order[-1]["_to"] == L - 1:
            order[-1]["_to"], order[-1]["points"] = L, order[-1]["points"] + 1
        else:
            order.append({"_from": L, "_to": L, "tree": tree, "talent": n, "points": 1})
    if errs:
        raise ValueError("; ".join(errs[:3]))
    order = [{"levels": f"{e['_from']}" if e["_from"] == e["_to"] else f"{e['_from']}-{e['_to']}", "tree": e["tree"], "talent": e["talent"],
              "points": e["points"]} for e in order]
    alloc = {tr: [[n, k] for n, k in v.items()] for tr, v in state.items()}
    return alloc, order


def fightlab_run():
    """The fight lab's run.py, loaded by its path (a bare "import run" found raidsim's for a tank)."""
    sys.path.insert(0, str(DATA))
    sys.path.insert(0, str(DATA / "fightlab"))
    import importlib.util
    FR = sys.modules.get("fightlab_run")
    if FR is None:
        spec = importlib.util.spec_from_file_location("fightlab_run", DATA / "fightlab" / "run.py")
        FR = importlib.util.module_from_spec(spec)
        sys.modules["fightlab_run"] = FR
        spec.loader.exec_module(FR)
    return FR


NEXT_TALENTS_WORKERS = 4   # processes for next_talents.race (BelowNormal and the affinity are inherited from the caller)
LAST_TALENT_RACE = {}      # the last talents_check's race of the next points ({"race": next_talents.race result}), for the page
LAST_RESPEC = {}           # the last talents_check's respec check ({"r": respec_value.check result}), for the page and the checklist


def talents_check(cfg, snap, level):
    FR = fightlab_run()
    b, order, prov, rot = pick(cfg, level)
    want = FR.allocation_at({"allocation": b["allocation"], "order": order}, level)
    have = {}
    for g in snap["specializations"].get("specialization_groups") or []:
        if not g.get("is_active", True):
            continue
        for s in g.get("specializations") or []:
            for t in s.get("talents") or []:
                n = (t.get("talent") or {}).get("name") or ((t.get("spell_tooltip") or {}).get("spell") or {}).get("name")
                if n:
                    have[n] = have.get(n, 0) + (t.get("talent_rank") or 0)
    # Blizzard's talents are as of the last logout it has seen; a spellbook written since that holds a talent's ability they lack (Ice
    # Lance, 2026-11-14: none spent at the 09:33 logout, Ice Lance in the 17:15 book) means points were spent since: the page's order
    # through the book's level is assumed when it covers both
    stale = None
    seen = (snap["profile"].get("last_login_timestamp") or 0) / 1000
    ahead = sorted(n for n in talent_names(cfg["class"]) if n in (BOOK.get("ranks") or {}) and not have.get(n)) if BOOK.get("t", 0) > seen else []
    if ahead and BOOK.get("level"):
        at_book = {n: k for n, k in FR.allocation_at({"allocation": b["allocation"], "order": order}, min(BOOK["level"], level)).items() if k}
        if all(at_book.get(n) for n in ahead) and all(k <= at_book.get(n, 0) for n, k in have.items()):
            stale = {"api": sum(have.values()), "ahead": ahead, "book": BOOK["when"], "level": min(BOOK["level"], level),
                     "seen": datetime.datetime.fromtimestamp(seen).strftime("%Y-%m-%d %H:%M") if seen else None}
            have = at_book
    diff = sorted(set(want) | set(have))
    rows = [(n, have.get(n, 0), want.get(n, 0)) for n in diff if have.get(n, 0) != want.get(n, 0)]
    # the character's own path: the page's points in the page's order, minus the ranks it already holds (a misplaced point shifts the
    # rest by a level and the last point falls off at 60)
    import fl_levels as FL
    got, queue = dict(have), []
    for _, n in FL.expand(order):
        if got.get(n, 0) > 0:
            got[n] -= 1
        else:
            queue.append(n)
    free = 60 - level
    owed = max(0, level - 9 - sum(have.values()))   # points you have and have not spent: due now, at your level (they had been labelled
    path = [(level + max(0, i + 1 - owed), n) for i, n in enumerate(queue[:free + owed])]   # from the next level, the last ones "dropped")
    # off the page's order: the next points raced in the fight lab from the character's own talents (2026-11-17, user: "Yes, test the
    # options"; next_talents.py). The same remaining points, so the destination stays the page's build; the rest keeps the page's order.
    LAST_TALENT_RACE.clear()
    if rows and path and cfg.get("metric") != "tank" and (cfg.get("talent_order") or {}).get("kind") not in ("tank", "chosen"):
        import next_talents as NT
        k = min(NT.POINTS, len(path))
        try:
            r = NT.race(cfg["class"], rot, cfg["spec"], have, [x for _, x in path], [L for L, _ in path[:k]], workers=NEXT_TALENTS_WORKERS)
        except Exception as e:   # noqa: BLE001  (the page's order stays)
            print(f"next talents: the race failed ({type(e).__name__}: {e}); the page's order stays", flush=True)
            r = None
        if r:
            LAST_TALENT_RACE["race"] = r
            left = [x for _, x in path]
            for _, x in r["path"]:
                left.remove(x)
            path = list(r["path"]) + [(L, x) for (L, _), x in zip(path[k:], left)]
    # a character whose points mostly follow another build respecs (Tara, Retribution points for a tank, 2026-11-09): the order's points
    # up to its level to take after the respec, and the order's next points from there
    respec = []
    match = sum(min(have.get(n, 0), w) for n, w in want.items())
    # a chosen path: a respec while you hold a point it does not have at your level (until Blizzard's data show the respec)
    if want and (match < 0.5 * sum(want.values()) or (chosen(cfg) and any(k > want.get(n, 0) for n, k in have.items()))):
        pts = [n for _, n in FL.expand(order)]
        for n in pts[:max(0, level - 9)]:
            if respec and respec[-1][0] == n:
                respec[-1][1] += 1
            else:
                respec.append([n, 1])
        path = [(10 + i, n) for i, n in enumerate(pts) if 10 + i > level]
    # off the page's order with points of its own: whether a respec to the page's order pays (2026-11-20; the user, on Arcea: "Even if I
    # have to respec"; characters/respec_value.py): her path against the page's order, measured at her level and every 5 levels to 60
    LAST_RESPEC.clear()
    if rows and not respec and have and cfg.get("metric") != "tank" and (cfg.get("talent_order") or {}).get("kind") not in ("tank", "chosen"):
        import respec_value as RV
        try:
            LAST_RESPEC["r"] = RV.check(cfg["class"], rot, have, path,
                                        lambda L: FR.allocation_at({"allocation": b["allocation"], "order": order}, L), level,
                                        kills_per_level, min_minutes=cfg.get("min_minutes", MIN_MINUTES), workers=NEXT_TALENTS_WORKERS)
        except Exception as e:   # noqa: BLE001  (no respec line)
            print(f"respec check: failed ({type(e).__name__}: {e})", flush=True)
    return b, rot, rows, sum(have.values()), sum(want.values()), path, queue[free + owed:] if not respec else [], respec, want, stale


def build_at(cls, want):
    """The build at the character's level by tree, for a fresh spend (2026-11-13): ([(tree, points, [(talent, ranks)])], calculator link)."""
    import render_start_here as RSH
    data = json.load(open(DATA / "forever-talents" / f"{cls}.json", encoding="utf-8"))
    trees = []
    for tr in data["trees"]:
        got = [(t["name"], want[t["name"]]) for t in tr["talents"] if want.get(t["name"])]
        if got:
            trees.append((tr["name"], sum(n for _, n in got), got))
    return sorted(trees, key=lambda x: -x[1]), RSH.tf_link(cls, want)


def pct(x):
    return f"{x * 100:.1f}%"


def account_levels():
    """{class name: (character, level)} of the account's characters the planner knows (their last snapshots): the class-level Legacy
    challenges (Novice Paladin ...) carry no progress in the achievements document."""
    out = {}
    for f in sorted((ROOT / "_characters").glob("*/armory/profile.json")):
        p = json.loads(f.read_text(encoding="utf-8"))
        c, lv = p["character_class"]["name"], p["level"]
        if c not in out or lv > out[c][1]:
            out[c] = (p["name"], lv)
    return out


def write_page(cfg, d, snap, fetched, at, eq, events, ench, profs, wfile):
    lv = snap["profile"]["level"]
    name = f"{snap['profile']['name']} {snap['profile'].get('surname', '')}".strip()
    seen = snap["profile"].get("last_login_timestamp")   # when Blizzard last saw the character (your last logout; 2026-11-13, user: "I'm
    seen = datetime.datetime.fromtimestamp(seen / 1000).strftime("%Y-%m-%d %H:%M") if seen else None   # level 30 and I got off at 11pm")
    b, rot, tdiff, have_n, want_n, tpath, tdrop, respec, twant, tstale = talents_check(cfg, snap, lv)
    if cfg.get("metric") == "tank":   # a group tank (2026-11-09, Tara)
        o = [f"# {name}", "",
             f"> Generated by `_reference/data/characters/plan.py {cfg['name']}` from Blizzard's character API (fetched {fetched}{f'; your character as of {seen}' if seen else ''}). Do not hand-edit:",
             "> refresh with the same command. Item values are tank value: threat, damage taken and effective health, from the raid "
             f"simulator's level-60 build `{b['id']}` in its gear (`characters/weights/{wfile}`), a model of the beta, not a measurement. "
             "\"Better tanking\" is that share of tank value, and the minutes count it as the same share of faster group play (a better "
             "tank pulls more and the healer rests less: an assumption). Talents: that build in the tank-first order (`characters/tank_order.py`).", ""]
    else:
        o = [f"# {name}", "",
             f"> Generated by `_reference/data/characters/plan.py {cfg['name']}` from Blizzard's character API (fetched {fetched}{f'; your character as of {seen}' if seen else ''}). Do not hand-edit:",
             "> refresh with the same command. Item values are seconds per kill from this project's fight lab for the leveling page build",
             f"> ([{cfg['spec']}](../../{cfg['class']}/leveling/{cfg['page']}.md)"
             + (", its own rotation; your talent path plays `" + rot + "` at this level" if chosen(cfg) else f", rotation `{rot}`")
             + "), a model of the beta, not a measurement.", ""]
    race, cls = snap["profile"]["race"]["name"], snap["profile"]["character_class"]["name"]
    o += [f"Level **{lv}** {race} {cls}, {snap['profile']['faction']['name']}. Professions: " +
          ", ".join(f"{k} {v[0]}/{v[1]}" for k, v in profs.items()) + "." +
          (f" Gold: **{AH.money(GOLD)}**." if GOLD is not None else " Gold: unknown (log in with bnet_login.py; the login lasts a day)."), ""]
    # talents
    o += ["## Talents", ""]
    if chosen(cfg):   # (2026-11-22: the user's own path; the page names its reason and what no simulator measures)
        t = chosen(cfg)
        o += [f"Your own talent path, **{t.get('name')}** (chosen {t.get('decided')}): {t.get('why')}", ""]
        o += [f"- {x}" for x in t.get("notes", [])] + ([""] if t.get("notes") else [])
    if tstale:
        o += [f"Blizzard's talents are from your logout at {tstale['seen']} and show "
              + (f"{tstale['api']} points" if tstale["api"] else "none spent")
              + f"; your spellbook (ForeverTape, {tstale['book']}) already has {', '.join(tstale['ahead'])}, so you spent points since. "
              f"This assumes you took the page's order through level {tstale['level']} ({have_n} points): check your talent pane against it.", ""]
    if respec:
        trees, link = build_at(cfg["class"], twant)
        first = (f"You have no talent points spent. Spend these {sum(n for _, n in respec)} points in this order (it keeps every tier "
                 "legal): " if have_n == 0 else
                 (f"Your {have_n} points are not your chosen path yet. Respec at a trainer on your next city visit, then take these "
                  f"{sum(n for _, n in respec)} points in this order: ") if chosen(cfg) else
                 f"Your {have_n} points follow another build. Respec at a trainer, then take these {sum(n for _, n in respec)} points in this order: ")
        o += [first + ", ".join(f"**{t}** {n}" for t, n in respec) + ".", "",
              f"The build at level {lv}: " + "; ".join(f"**{tn}** {pts} ({', '.join(f'{t} {n}' for t, n in got)})" for tn, pts, got in trees)
              + f". [Open it in the talent calculator]({link}).", "",
              ("After your respec, your next talents: " if chosen(cfg) else "Your next talents: ") + ", ".join(f"{L} {n}" for L, n in tpath[:6]) + ".", ""]
    elif not tdiff:
        o += [f"Your {have_n} talent points match the page's order at level {lv}.", ""]
    else:
        o += [f"Against the page's order at level {lv} ({want_n} points; you have {have_n} spent):", "", "| Talent | Yours | The page |", "|---|---|---|"]
        o += [f"| {n} | {h} | {w} |" for n, h, w in tdiff] + [""]
        traced = LAST_TALENT_RACE.get("race")   # (not `race`: write_page's `race` is the character's)
        if traced:
            import next_talents as NT
            o += ["Your next talents (" + NT.note(traced) + "): " + ", ".join(f"{L} {n}" for L, n in tpath[:6]) + "."]
        else:
            o += ["Your next talents (the page's order from where you are): " + ", ".join(f"{L} {n}" for L, n in tpath[:6]) + "."]
        if tdrop:
            o += [f"You stay one point off the page's order; at 60 you go without its last point ({', '.join(tdrop)}), which measures "
                  "least of its talents."]
        o += [""]
        import respec_value as RV
        rtxt = RV.text(LAST_RESPEC.get("r"), lv)
        if rtxt and LAST_RESPEC["r"].get("pays"):
            trees_r, link_r = build_at(cfg["class"], LAST_RESPEC["r"]["build"])
            o += [rtxt + f" The build at level {lv}: " + "; ".join(f"**{tn}** {pts} ({', '.join(f'{t} {n}' for t, n in got)})" for tn, pts, got in trees_r)
                  + f". [Open it in the talent calculator]({link_r}).", ""]
        elif rtxt:   # (the audit session, 2026-11-20: when the line is suppressed, one sentence says so)
            o += [rtxt, ""]
    o += [f"- {x}" for x in cfg.get("talent_notes", [])] + ([""] if cfg.get("talent_notes") else [])
    worn_names = {s: (eq.get(s) or {}).get("name") for s in ("trinket1", "trinket2")}   # (the trinket keys are slot macros)
    o += OWNK.readme(cfg, lv, worn_names)   # the character's own key layout (2026-11-22, Arcea: questing and PvP in one), else nothing
    docs = [snap["achievements"]] if snap.get("achievements") else []
    docs += [json.loads(f.read_text(encoding="utf-8")) for f in sorted((ROOT / "_characters").glob("*/armory/achievements.json"))
             if f.parent.parent != d]   # the account's other characters (achievements come per character)
    lvls = account_levels()   # this character at the page's level (a newer add-on record or your word, plan.fresher)
    if lv > lvls.get(cls, (None, 0))[1]:
        lvls[cls] = (snap["profile"]["name"], lv)
    lo, CTX["legacy"] = LEG.section(cfg, docs, lvls)   # Legacy points (2026-11-10)
    o += lo
    CTX.update({"head": {"name": name, "level": lv, "race": race, "class": cls, "gold": GOLD, "fetched": fetched, "seen": seen,
                         "faction": snap["profile"]["faction"]["name"], "professions": {k: list(v) for k, v in profs.items()},
                         "ah_age": PRICES.age_hours() if PRICES else None, "spec": guide_spec(cfg, lv), "page": cfg["page"],
                         "short": SHORT, "faster": FASTER, "chosen": bool(chosen(cfg))},
                "talents": {"diff": tdiff, "path": tpath[:6], "drop": tdrop, "have": have_n, "want": want_n, "respec": respec, "stale": tstale,
                            "respec_value": LAST_RESPEC.get("r"),
                             "raced": __import__("next_talents").note(LAST_TALENT_RACE["race"]) if LAST_TALENT_RACE.get("race") else None,
                             "link": build_at(cfg["class"], twant)[1] if respec else None},
                "keys_extra": (chosen(cfg) or {}).get("keys") or [], "worn_names": worn_names})
    o += change_lines(d, events, lv)
    # now: the upgrades to go after at this level or within LOOKAHEAD levels, by what you do for them
    wl = at(lv)
    soon = [e for e in events if max(e["get_at"], lv) <= lv + LOOKAHEAD]
    global SPENDABLE
    gs, SPENDABLE = gold_plan(cfg, snap, at, lv)
    o += gs
    CTX["notices"] = list(NOTICES)   # the page shows them under the level line (at the write, below), the checklist on its Town tab
    o += [f"## Now (level {lv})", "",
          f"Everything below is worth doing at your level or within {LOOKAHEAD} levels: items you can wear now, and items you can get now "
          "and wear a level or two later. "
          + ("Percentages are how much better you tank (tank value: threat, damage taken and effective health) once the item replaces "
             "what you wear." if cfg.get("metric") == "tank" else
             "Percentages are how much faster you kill a mob of your level once the item replaces what you wear (fight lab)."), ""]
    worn = {s: (eq.get("main-hand") if s == "weapon" else eq.get(s)) for s in SLOT_ORDER}
    for s in SLOT_ORDER:   # when the item worn now is replaced (the first upgrade of the slot)
        if worn.get(s):
            worn[s] = dict(worn[s], until=next((e["level"] for e in events if e["slot"] == s), None), since=lv)
    for e in sorted(soon, key=lambda e: e["level"]):
        worn[e["slot"]] = {"name": e["item"]["name"], "stats": e["item"]["stats"], "enchant": [], "enchant_stats": {},
                           "two_hand": e["item"].get("slot") == "two-hand", "planned": e["level"], "since": e["level"], "until": e["until"]}
    o += judge_lines(worn, events, wl, lv, cfg)
    CTX["soon"] = [event_row(e, at) for e in sorted(soon, key=lambda e: (max(e["get_at"], lv), e["level"]))]
    CTX["later"] = [event_row(e, at) for e in sorted(events, key=lambda e: (max(e["get_at"], lv), e["level"]))
                    if lv + LOOKAHEAD < max(e["get_at"], lv) <= lv + 14]
    CTX["enchants"] = enchant_lines(worn, ench, profs, wl, at, lv)
    o += ["### Enchant", ""] + (enchant_lines(worn, ench, profs, wl, at, lv) or [f"- Nothing worth 0.1% {FASTER} at your Enchanting skill."]) + [""]
    tmin, tlv = trip(cfg, snap, at, lv)
    CTX["trip"] = {"minutes": tmin, "level": tlv}
    cl = consumable_lines(lv, wl, profs, cfg["school_share"], tmin, at)
    if cl:
        o += ["### Oils, food and elixirs", "", "The best three of each kind you can use now, with today's prices"
              + (f" (auction house snapshot {PRICES.age_hours():.1f} hours old)" if PRICES and PRICES.age_hours() is not None else "")
              + f". \"For your trip\": enough to keep it up for about {tmin / 60:.1f} hours of play, "
              + (f"to your next training at level {tlv}" if tlv else "your set time between town visits")
              + " (character.json \"hours_out\" sets your own). \"Earns its price back\": the play minutes an hour of it saves against "
              "the play minutes an hour of it costs to earn at your income.", ""] + cl + [""]
    o += action_sections(soon, at, lv)
    runs = dungeon_runs(BONUS)
    sched = dungeon_schedule(cfg, lv, runs, events)
    CTX["dungeons"] = sched
    tl = timeline(sched, events, lv)
    CTX["timeline"] = [dict(r, text=timeline_line(r)) for r in off_guide(tl)] if RG else None   # (LEAVE_GUIDE, 2026-11-15)
    near = [r for r in sched if r["run"] <= lv + LOOKAHEAD]
    if near:
        o += ["### Dungeon runs", "", "Run each once, with its quests in your log first: the quests' experience is the main reward. A drop that "
              "beats what the plan has you wear is a bonus; the plan works without it.", ""]
        o += dungeon_lines(near)
    cu_rows = [r for r in tl if r["kind"] == "catchup" or "your guide hands it in" in r["facts"] or "finish " in r["facts"]]
    if cu_rows:
        o += ["### Catch up with your guide", "", "Things your RestedXP guide did before your step that it still counts on: without them it "
              "skips the steps that hand them in or take their next part. Do each by its deadline (listed in Off the guide too).", ""]
        o += [f"- {timeline_line(r)}" for r in cu_rows] + [""]
    soon_t = [r for r in off_guide(tl) if r["level"] <= lv + LOOKAHEAD]
    if soon_t:
        o += ["### Off the guide", "", "In your RestedXP route's order (the full list: Off the guide, below).", ""]
        o += [f"- {timeline_line(r)}" for r in soon_t] + [""]
    o += ["### Talents and the rest", "", "- Talents: see above. Food, drink, bandages: the [by-level guide](../../" +
          f"{cfg['class']}/leveling/{cfg['page']}-by-level.md) for your rotation.", ""]
    o += profession_section(profs)
    # current gear
    o += ["## Your gear", "", "| Slot | Item | Worth at your level | Replaced at |", "|---|---|---|---|"]
    first = {}
    for e in events:
        first.setdefault(e["slot"], e)
    for slot in SLOT_ORDER:
        rep = first.get(slot)
        when = f"level {rep['level']}: {upgrade_name(rep)[0]}" if rep else None   # (a weapon pair by both halves, 2026-11-14)
        held = [("main hand", eq.get("main-hand"))] + ([("off hand", eq.get("off-hand"))] if eq.get("off-hand") else []) \
            if slot == "weapon" else [(slot, eq.get(slot))]   # (the off hand had no row: Arcea's Orb of Mystic Insight)
        for name, it in held:
            if not it:
                o += [f"| {name} | **empty** | 0 | {when or 'nothing worth 0.5% before 60'} |"]
                continue
            v = value(it["stats"], wl) + value(it["enchant_stats"], wl)
            o += [f"| {name} | {it['name']}{' (' + ', '.join(it['enchant']) + ')' if it['enchant'] else ''} | {pct(v / wl['time'])} {FASTER} | "
                  f"{when or 'not before 60 by 0.5%'} |"]
    o += [""]
    # level by level: by the level you act (the earliest the quest, dungeon or recipe allows); "wear at" when it comes later
    o += ["## Level by level", "", f"Each upgrade worth {UPGRADE:.1%} {FASTER} or more, under the level at which you can go and get it, "
          "with the level you can wear it when that is later. Dungeon drops carry Classic's drop chance and a fallback if they do not drop; "
          "auction house items on later visits are ones the house usually lists, at their usual price.", ""]
    later = [e for e in events if max(e["get_at"], lv) > lv + LOOKAHEAD]
    for L in range(lv + LOOKAHEAD + 1, LAST + 1):
        ev = [e for e in later if max(e["get_at"], lv) == L]
        if ev:
            o += [f"### Level {L}", ""] + action_sections(ev, at, L, head="####") + [""]
    if off_guide(tl):
        o += ["## Off the guide", "",
              "Only what is worth stepping off your RestedXP route for, in the route's order: catching up with your guide, and gear the plan "
              "counts on that the route leaves out (its quests, a side trip for a reward or drops). The route is a good leveling path as it is: "
              "side quests for experience (a few minutes each, inside the estimate's own error) and the guide's own dungeons are left to it "
              "(2026-11-15). Each is tied to the moment in the guide it starts from: the quest it has you hand in or pick up there (the step "
              "number is the guide's own count within that part, an estimate). Do it, then pick the guide up where you left it.", ""]
        o += [ROUTE_NOTE[0], ""] if ROUTE_NOTE[0] else []
        o += [f"- {timeline_line(r)}" for r in off_guide(tl)] + [""]
    # every dungeon run, by level
    if sched:
        o += ["## Dungeon runs", "", "Every leveling dungeon you have not outgrown, once, at the level its quests fit: pick the quests up first. "
              "Drops are bonuses over what the plan has you wear: wear one if it drops, the plan goes on as written if not. Drop chances "
              f"are Classic's (25% where it has none); \"about N min\" is a drop's {MINUTES_OF} saved over the plan's item, and a "
              f"run's drops are worth that times their chances. Minutes assume {KILL_SHARE:.0%} of your experience comes from kills.", ""]
        o += dungeon_lines(sched)
    if RG and RG["trust"]["mismatch"]:   # 2026-11-13: never "none found" when the detours were not looked for
        o += ["## Detours off your route", "",
              "Not worked out this time: the guide text on this PC does not match where your RestedXP add-on is (see Heads up at the top), "
              "so which quests the route leaves out is unknown.", ""]
    elif RG:
        st = DETOURS["stats"]
        o += ["## Detours off your route", "",
              "Quests your RestedXP route leaves out, played as a detour from where the route is at that level: walk to the giver, do it at "
              "the nearest spots, hand it in, walk back. Three kinds: **clear win** (20% faster than your usual leveling pace and 3 minutes "
              "saved), **worth it if you like it** (at your pace or a bit better), and **for the gear** (its reward is in your gear plan; a "
              "little slower than your pace is fine). Estimates: straight-line travel with a margin, Classic's quest positions, your fight-lab "
              f"time per kill. {st.get('scored', 0)} quests scored; {st.get('unknown', 0)} could not be placed (an item starts them, or a "
              "target has no known spot); Forever's own quests have no positions here.", ""]
        by = {}
        for x in DETOURS["list"]:
            by.setdefault(x["level"], []).append(x)
        for L in sorted(by):
            o += [f"### Level {L}", ""] + [f"- {detour_text(x)}" for x in by[L]] + [""]
        if not by:
            o += ["None found: your route already takes every quest that pays for its walk.", ""]
    o += ["## How this is worked out", "",
          (f"- Stat values: the gear add-on's (`_reference/data/characters/{wfile}`, addon_values.py; the in-game tooltip shows the same): the "
           "page build in the fight lab at levels 10-60 with every gear stat raised (stat_weights.py --full), on the lab's standard gear and on "
           "each level's best Forever set; the items you wear place you between the two (their stats scored with the standard gear's values, "
           "against the best set's; enchants, hit and expertise left out), and that share is kept for the levels ahead. Hit and expertise count while the build's talents leave room under the cap. Resistances and effects are not scored."
           if wfile.startswith("addon/") else
           f"- Stat values: `_reference/data/characters/weights/{wfile}` (tank_weights.py): the raid simulator's threat and damage-taken stat "
           "weights for the level-60 tank build in its gear, plus the effective health the simulator does not score, as shares of tank value "
           "(half threat, a quarter damage taken, a quarter effective health); one measurement at 60 stands for every level."
           if cfg.get("metric") == "tank" else
           f"- Stat values: `_reference/data/characters/weights/{wfile}` (stat_weights.py): the page build in the fight lab at levels 20-60 with each "
           "stat raised, common random numbers; smoothed over neighbouring levels. Spell crit and hit from items, resistances and defense read 0."),
          (f"- Minutes saved: at each level an item is worn, its share of tank value counted as the same share of faster play (an "
           "assumption: a better tank pulls more and the healer rests less), applied to the level's killing time (the spec's solo time per "
           f"kill x the kills of the level, {KILL_SHARE:.0%} of its experience from kills, an estimate), until the plan replaces it. Gear you "
           "find or buy that the plan cannot see (world drops, later auction listings) may replace an item sooner."
           if cfg.get("metric") == "tank" else
           f"- Minutes saved: at each level an item is worn, the seconds per kill its stats save over what it replaces (stats are worth less as "
           f"you level) x the kills of that level ({KILL_SHARE:.0%} of the level's experience from kills, an estimate), until the plan "
           "replaces it. Quests, travel and dungeon time are not counted. Gear you find or buy that the plan cannot see (world drops, later "
           "auction listings) may replace an item sooner."),
          "- School damage counts by the build's share: " + ", ".join(f"{k} {v:.0%}" for k, v in cfg["school_share"].items()) + " (an estimate).",
          "- Quests Forever added carry no level in Blizzard's data: their zone's level range stands in. Dungeons Forever added: the range of their "
          "drops' required levels. Crafts: the recipe's skill from the Classic database (Forever may differ); a craft counts once your profession "
          "rank allows the skill at that level.",
          f"- An upgrade is listed when it is worth {UPGRADE:.1%} of {'tank value' if cfg.get('metric') == 'tank' else 'the time per kill'} "
          f"or more over what you would be wearing then, and "
          f"it saves at least {MIN_MINUTES:.0f} {MINUTES_OF} before the next upgrade of the slot replaces it, worn at least {MIN_LASTS} levels "
          "(level 60 ends leveling). A smaller or shorter-lived upgrade is left out, and the next one is counted against what you would still "
          "be wearing. Quest rewards you get anyway: wear them when the game shows them as better. Enchants: only when the enchant saves "
          f"{MIN_MINUTES:.0f} minutes before you replace the item.",
          f"- Data: the simulator's WoW: Forever item database at {DATAVER['sim']} ({DATAVER['items']} items; it grows as the game is played, "
          "and a refresh picks the new items up), the CMaNGOS Classic dump at c33f90b8e (recipe skills, quest levels, dungeon loot), Blizzard's "
          f"API for the character (fetched {fetched}) and for Forever's own quests (asked again weekly), stat values measured {DATAVER['weights']} "
          f"for {DATAVER['weights_build']}.",
          "- Raid preparation (items worth keeping for 60) waits for the mage raid lane's gear redo: today's pre-raid set still holds "
          "Naxxramas and Ahn'Qiraj quest rewards (the gear pool fault of 2026-11-05).", ""]
    # the heads-up notices at the top, under the level line (2026-11-21, the audit session: "if Blizzard's data lag behind what the
    # add-ons show ... say so at the top"; they had sat after the gold plan, about 75 lines down)
    if NOTICES:
        i = next((k for k, line in enumerate(o) if line.startswith("Level **")), 4) + 1
        o[i:i] = [""] + [f"> **Heads up:** {n}" for n in NOTICES]
    (d / "README.md").write_text("\n".join(o) + "\n", encoding="utf-8")


PLAY_KILL_SHARE = 0.5   # the share of play time spent killing (the rest: travel, quest turn-ins, looting, vendoring): an estimate
ESSENTIALS = {"mage": {"Arcane Intellect", "Frost Armor", "Ice Armor", "Conjure Water", "Conjure Food", "Frost Nova", "Blink", "Counterspell"},
              "paladin": {"Devotion Aura", "Righteous Fury", "Seal of Righteousness", "Judgement", "Blessing of Might", "Blessing of Wisdom",
                          "Holy Light", "Flash of Light", "Lay on Hands", "Hammer of Justice", "Redemption", "Divine Protection",
                          "Divine Shield", "Blessing of Protection", "Purify", "Cleanse", "Consecration"}}
MOUNT = {"level": 40, "riding": 200000, "mount": 800000, "discount_rep": "Honored"}   # Classic: riding 20g + mount 80g, 10% off the
                                                                                        # mount at Honored with the race's faction


def training_by_level(cls):
    """{level: [(spell name, cost copper)]} the class trainer teaches this character (Classic prices, class_training.csv; training_rows)."""
    out = {}
    for L, sid, name, cost in training_rows(cls):
        out.setdefault(L, []).append((name, cost))
    return out


SUPERSEDED = {"Frost Armor": "Ice Armor"}   # a spell whose ranks stop mattering once its replacement is known (owed_training)
TRAIN = {}   # who learns what: main() sets "race" (the character's race id) and "talent_from" ({talent: the level the build takes it})
SLA_FILE = DATA / "raw" / "2026-11-09-wago-1.60.1.70862" / "SkillLineAbility.csv"   # Forever's client table (race masks)


def race_masks():
    """{spell id: [the 64-bit race mask of each of its SkillLineAbility rows]} (0: every race), loaded once."""
    if "sla" not in TRAIN:
        out = {}
        for r in csv.DictReader(open(SLA_FILE, encoding="utf-8")):
            m = (int(r["RaceMasks_0"]) & 0xFFFFFFFF) | ((int(r["RaceMasks_1"]) & 0xFFFFFFFF) << 32)
            out.setdefault(int(r["Spell"]), []).append(m)
        TRAIN["sla"] = out
    return TRAIN["sla"]


def talent_names(cls):
    """The talent names of the class's Forever trees (a trainer spell of the same name is a talent's ability)."""
    if ("talents", cls) not in TRAIN:
        data = json.load(open(DATA / "forever-talents" / f"{cls}.json", encoding="utf-8"))
        TRAIN[("talents", cls)] = {t["name"] for tr in data["trees"] for t in tr["talents"]}
    return TRAIN[("talents", cls)]


def train_level(cls, L, sid, name):
    """The level this character can learn a trainer row at, or None when it never can (2026-11-14, user: "Fix the planner and any
    bugs"; the training lists had a Gnome mage's Teleport: Orgrimmar and Pyroblast ranks without the talent): a spell its race cannot
    learn (Forever's SkillLineAbility race masks: the other faction's teleports and portals, the priests' racial spells), and a talent's
    ability (Pyroblast, Holy Shield) only with the talent: from the level the build takes it, or at once when the spellbook has it."""
    race = TRAIN.get("race")
    masks = race_masks().get(sid)
    if race and masks and not any(m == 0 or (m >> (race - 1)) & 1 for m in masks):
        return None
    if name in talent_names(cls) and name not in (BOOK.get("ranks") or {}):
        first = (TRAIN.get("talent_from") or {}).get(name)
        return max(L, first) if first else None
    return L


def training_rows(cls):
    """[(level, spell id, name, cost copper)] the class trainer teaches this character, each at the level it can be learned (train_level:
    race and talents): Classic's table (class_training.csv) without the rows Forever no longer teaches, plus Forever's own ranks
    (forever_ranks, 2026-11-14) at Classic's usual price for their level (classic_price: an estimate; their names in TRAIN["estimated"]).
    A Classic row goes when Forever's client has no skill row for its spell (Elune's Grace, Fire Nova Totem: not learnable), or when
    Forever's spell data list the spell under other ids (Curse of the Elements remade at 20/30/40/50, Classic's 32/46/60 ranks gone)."""
    fids, fnames = set(), set()
    for tab, sp, r, rank, sid in fs_ranks(cls):
        fids.add(sid)
        fnames.add(sp["name"])
    out = []
    for r in csv.DictReader(open(IP.RAW / "class_training.csv", encoding="utf-8")):
        if int(r["class"]) == IP.CLASS_ID[cls] and r["name"]:
            sid = int(r["spell"])
            if sid not in race_masks() or (sid not in fids and r["name"] in fnames):
                continue
            L = train_level(cls, int(r["level"]), sid, r["name"])
            if L is not None:
                out.append((L, sid, r["name"], int(r["cost"])))
    est = TRAIN.setdefault(("estimated", cls), set())
    for lv, sid, name, rank in forever_ranks(cls):
        L = train_level(cls, lv, sid, name)
        if L is not None:
            out.append((L, sid, name, classic_price(cls, lv)))
            est.add(name)
    return out


def fs_ranks(cls):
    """[(tab, spell, rank row, rank number, spell id)] of Forever's spell data (forever-spells/<class>.json), loaded once; a rank with no
    id gets a stable negative stand-in (the rogue's Shank), so the spellbook check and the training rows can still name it."""
    if ("fs", cls) not in TRAIN:
        import zlib
        out = []
        for tab in json.load(open(DATA / "forever-spells" / f"{cls}.json", encoding="utf-8"))["tabs"]:
            for sp in tab["spells"]:
                for r in sp["ranks"]:
                    m = re.search(r"(\d+)", r.get("rank") or "")
                    sid = r.get("id") or -(zlib.crc32(f"{sp['name']}|{r.get('rank') or ''}".encode()) & 0x7FFFFFFF)
                    out.append((tab["name"], sp, r, int(m.group(1)) if m else 0, sid))
        TRAIN[("fs", cls)] = out
    return TRAIN[("fs", cls)]


def forever_ranks(cls):
    """Forever's trainer ranks that Classic's table lacks (2026-11-14, user: "Yes add the spells", after Ice Lance's rank 3 at 34 was
    missing from Arcea's training): [(level, spell id, name, rank)], every rank Forever's spell data mark new against Classic or that
    carries a Forever-made spell id (100000 and up: Curse of the Elements' remade ranks are marked changed), in the class's own tabs.
    Left out: the hunter's Pets tab (pet abilities: no class trainer teaches them), passives (they come with the level, as far as the
    data say), a talent's first rank and a single-rank talent ability (the talent grants them), and ranks with no level."""
    known = {int(r["spell"]) for r in csv.DictReader(open(IP.RAW / "class_training.csv", encoding="utf-8"))
             if int(r["class"]) == IP.CLASS_ID[cls]}
    out = []
    for tab, sp, r, rank, sid in fs_ranks(cls):
        new = ((r.get("classic") or {}).get("status") == "new") or (r.get("id") or 0) >= 100000
        if not new or sid in known or tab == "Pets" or (r.get("rank") or "") == "Passive" or not r.get("level"):
            continue
        if sp["name"] in talent_names(cls) and rank <= 1:
            continue
        out.append((int(r["level"]), sid, sp["name"], rank))
    return out


def classic_price(cls, L):
    """Classic's usual trainer price for the class at level L (the most common price of its ranks there; else the nearest lower level
    with ranks, else the lowest): the estimate for a Forever rank Classic's table lacks (a mage's level-34 ranks: 1g 20s)."""
    if ("price", cls) not in TRAIN:
        by = {}
        for r in csv.DictReader(open(IP.RAW / "class_training.csv", encoding="utf-8")):
            if int(r["class"]) == IP.CLASS_ID[cls] and r["name"]:
                by.setdefault(int(r["level"]), []).append(int(r["cost"]))
        TRAIN[("price", cls)] = {lv: max(set(cs), key=lambda c: (cs.count(c), c)) for lv, cs in by.items()}
    p = TRAIN[("price", cls)]
    lower = [lv for lv in p if lv <= L]
    return p[max(lower)] if lower else p[min(p)]


def spell_ranks(cls):
    """{spell id: rank number} from Forever's spell data (forever-spells/<class>.json; 0 for a spell without ranks)."""
    return {sid: rank for tab, sp, r, rank, sid in fs_ranks(cls)}


def owed_training(cfg, lv):
    """The trainer's ranks at your level or below that your spellbook lacks, skipped ones included (2026-11-14, user: "Is the checklist
    able to see what current rank of spells I have?"): ([(level, name, rank, cost)] your build and kit use, [...] optional), or None
    without a spellbook snapshot. A rank is known when its spell id is in the book, or the book holds it or a higher rank of the spell (a
    book may list the highest rank only); a spell Forever's data does not rank is known when the book has it at all."""
    if not BOOK:
        return None
    ranks, need, out = spell_ranks(cfg["class"]), needed_at(cfg, lv), ([], [])
    for L, sid, name, cost in sorted(training_rows(cfg["class"])):
        if L > lv or sid in BOOK["ids"]:
            continue
        if SUPERSEDED.get(name) in BOOK["ranks"]:   # Ice Armor replaces Frost Armor: its lower ranks are no longer worth training
            continue
        r, have = ranks.get(sid), BOOK["ranks"].get(name)
        if have is not None and (not r or have >= r):
            continue
        out[0 if name in need else 1].append((L, name, r, cost))
    return out


def rank_label(name, r):
    return f"{name} (rank {r})" if r else name


NEED_AT = {}   # level -> the spells needed at that level or later (needed_at)


def needed_at(cfg, L):
    """The spells the character's rotation and kit use at level L or later (2026-11-14): the guide's bold names in the stage active at L
    and every later stage, the spells its keys hold at L or later, its general notes (intro, between fights, other) and the class's
    essentials. A spell the guide drops is optional from then on: a frost mage's Fireball after level 4, Flamestrike after 19 (the first
    spellbook read had put their ranks in the training "you need")."""
    if not NEED_AT:
        bold = lambda v: set(re.findall(r"\*\*([^*]+)\*\*", json.dumps(v)))
        sets = {}
        for lv in range(1, 61):
            spec = guide_spec(cfg, lv)   # (a chosen path plays one guide, then another: Arcea, Frost until 46, Arcane-Frost from 47)
            if spec not in sets:
                x = guide_of(cfg, lv)
                always = bold({k: x.get(k) for k in ("intro", "between", "other")}) | ESSENTIALS.get(cfg["class"], set())
                always |= {k["spell"] for k in (chosen(cfg) or {}).get("keys") or []}   # a chosen path's own keys (Ice Block for PvP)
                always |= OWNK.spells(cfg)   # the character's own key layout (2026-11-22)
                spans = []
                stages = sorted(x.get("stages") or [], key=lambda s: s["from"])
                for i, st in enumerate(stages):
                    spans.append((stages[i + 1]["from"] - 1 if i + 1 < len(stages) else 60, bold(st)))
                keys = x.get("keys") or {}
                for slot in [s for bar in keys.get("bars") or [] for s in bar.get("slots") or []] + list(keys.get("slots") or []):
                    binds = sorted(slot.get("binds") or [], key=lambda b: b["from"])
                    for i, b in enumerate(binds):
                        spans.append((binds[i + 1]["from"] - 1 if i + 1 < len(binds) else 60, ({b["spell"]} if b.get("spell") else set()) | bold(b)))
                sets[spec] = (always, spans)
            always, spans = sets[spec]
            NEED_AT[lv] = always.union(*[names for end, names in spans if end >= lv])
    return NEED_AT[min(max(int(L), 1), 60)]


def guide_of(cfg, L=None):
    """The character's by-level guide: its own (Tara the group tank, 2026-11-09) or its spec's (at level L, a chosen path's: guide_spec)."""
    if cfg.get("guide") and (DATA.parent.parent / cfg["guide"]).exists():
        return json.load(open(DATA.parent.parent / cfg["guide"], encoding="utf-8"))
    g = json.load(open(DATA / "level-guides" / f"{cfg['class']}.json", encoding="utf-8"))
    spec = guide_spec(cfg, L)
    return next((x for x in g["guides"] if x["spec"] == spec), {})


def needed_spells(cfg):
    """The spells the character's rotation and kit use: every bold name of its by-level guide, plus the class's essentials (buffs,
    conjures, the escape and control kit); other trainer spells are optional (a frost mage's fire spells, teleports)."""
    if cfg.get("guide") and (DATA.parent.parent / cfg["guide"]).exists():   # the character's own guide (Tara the group tank, 2026-11-09)
        x = json.load(open(DATA.parent.parent / cfg["guide"], encoding="utf-8"))
    else:
        g = json.load(open(DATA / "level-guides" / f"{cfg['class']}.json", encoding="utf-8"))
        specs = {cfg["spec"]} | {s for _, _, s in (chosen(cfg) or {}).get("rotations") or []}   # (every guide a chosen path plays)
        x = [x for x in g["guides"] if x["spec"] in specs]
    return (set(re.findall(r"\*\*([^*]+)\*\*", json.dumps(x))) | ESSENTIALS.get(cfg["class"], set())
            | {k["spell"] for k in (chosen(cfg) or {}).get("keys") or []} | OWNK.spells(cfg))


def loot_value(item, quality, klass, sell):
    """What one looted item brings, copper: grays and quest items their vendor price; anything else the better of the vendor and the
    auction house after its 5% cut, at the add-on's typical price (Insights), else 80% of the cheapest listing (2026-11-09). A typical
    price from listings rather than sales (source "l": three items in four, nearly every level-45 green) is an asking price: capped at
    twice the vendor's, about what greens sold for where the add-on saw sales."""
    if quality < 1 or klass == "12" or not PRICES:
        return sell
    t = PRICES.typical.get(item)
    if t and t[0]:
        v = 0.95 * t[0]
        return max(sell, v if t[1] == "s" or not sell else min(v, 2 * sell))
    c = PRICES.cheapest(item)
    return max(sell, min(0.95 * 0.8 * c[0], 2 * sell) if sell else 0.95 * 0.8 * c[0]) if c else sell


def income_per_level(L, quests_per_level):
    """Copper a level brings (Classic data): kills x (coin + the loot, each item at loot_value: cloth and greens at auction prices,
    spawn-weighted by mob level) plus the quests done in a level x the average quest money at that level. Assumes you sell what drops
    (or use it in place of buying it)."""
    if not INCOME:
        loot = {}
        lp = IP.RAW / "mob_loot.csv"
        if lp.exists():
            for r in csv.DictReader(open(lp, encoding="utf-8")):
                v = loot_value(int(r["item"]), int(r["quality"]), r["class"], int(r["sell"]))
                loot[int(r["level"])] = loot.get(int(r["level"]), 0.0) + float(r["per_kill"]) * v
        for r in csv.DictReader(open(IP.RAW / "mob_income.csv", encoding="utf-8")):
            INCOME[int(r["level"])] = float(r["coin_per_kill"]) + loot.get(int(r["level"]), float(r["vendor_per_kill"]))
        qm = {}
        for r in csv.DictReader(open(IP.RAW / "quests.csv", encoding="utf-8")):
            q = int(r["quest_level"] or 0)
            if 1 <= q <= 60:
                qm.setdefault(q, []).append(int(r.get("money") or 0))
        QUEST_MONEY.update({q: sum(v) / len(v) for q, v in qm.items()})
    return kills_per_level(L) * INCOME.get(L, 0) + quests_per_level * QUEST_MONEY.get(L, 0)


def minutes_per_level(L, at):
    return kills_per_level(L) * at(L)["time"] / 60 / PLAY_KILL_SHARE


INCOME, QUEST_MONEY = {}, {}
RACE_FACTION = {"Gnome": "Gnomeregan Exiles", "Human": "Stormwind", "Dwarf": "Ironforge", "Night Elf": "Darnassus", "Orc": "Orgrimmar",
                "Troll": "Darkspear Trolls", "Tauren": "Thunder Bluff", "Undead": "Undercity"}
STANDING = ["Hated", "Hostile", "Unfriendly", "Neutral", "Friendly", "Honored", "Revered", "Exalted"]
SPENDABLE = None   # gold free for gear now (gold minus the training the next two levels need), copper; None when the gold is unknown


def gold_plan(cfg, snap, at, lv):
    """The gold section and the copper free for gear now (2026-11-09, user: "I also don't want to have to upgrade too often. That costs a
    lot of gold that I don't get back ... looks at my current gold and factors in what % of my gold it costs and compared to how much gold
    per hour I'm making, how much training costs")."""
    done = len((snap.get("quests-completed") or {}).get("quests") or [])
    qpl = done / max(1, lv - 1)
    train = training_by_level(cfg["class"])
    need = lambda L: needed_at(cfg, L)
    race = snap["profile"]["race"]["name"]
    reps = {r["faction"]["name"]: r["standing"]["name"] for r in (snap.get("reputations") or {}).get("reputations") or []}
    rep = reps.get(RACE_FACTION.get(race, ""), "Neutral")
    discount = STANDING.index(rep) >= STANDING.index(MOUNT["discount_rep"]) if rep in STANDING else False
    mount = MOUNT["riding"] + MOUNT["mount"] * (0.9 if discount else 1.0)
    owe = owed_training(cfg, lv)   # ranks your spellbook lacks now (2026-11-14): paid before anything else
    owe_cost = sum(x[3] for x in owe[0]) if owe else 0
    rows, saved, mount_at = [], (GOLD or 0) - owe_cost, None
    gear = {}
    for L, c in PLANNED:
        gear[L] = gear.get(L, 0) + c
    for L in range(lv, 60):
        inc = income_per_level(L, qpl)
        nt = sum(c for n, c in train.get(L + 1, []) if n in need(L + 1))
        ot = sum(c for n, c in train.get(L + 1, []) if n not in need(L + 1))
        saved += inc - nt - gear.get(L, 0)
        if L + 1 >= MOUNT["level"] and mount_at is None and saved >= mount:
            mount_at = L + 1
        rows.append((L, inc, nt, ot, [n for n, c in train.get(L + 1, []) if n in need(L + 1)]))
    reserve = sum(r[2] for r in rows[:2]) + owe_cost
    spend = None if GOLD is None else max(0, GOLD - reserve)
    opt = {L + 1: [n for n, c in train.get(L + 1, []) if n not in need(L + 1)] for L in range(lv - 1, 60)}
    CTX["training"] = ([{"level": lv, "need": [rank_label(n, r) for L, n, r, c in owe[0]], "cost": owe_cost,
                         "optional": [rank_label(n, r) for L, n, r, c in owe[1]], "optional_cost": sum(x[3] for x in owe[1]),
                         "book": BOOK["when"]}] if owe is not None else
                       [{"level": lv, "need": [n for n, c in train.get(lv, []) if n in need(lv)],
                        "cost": sum(c for n, c in train.get(lv, []) if n in need(lv)), "optional": opt.get(lv, []),
                        "optional_cost": sum(c for n, c in train.get(lv, []) if n not in need(lv))}]) + \
                      [{"level": L + 1, "need": names, "cost": nt, "optional": opt.get(L + 1, []), "optional_cost": ot}
                       for L, inc, nt, ot, names in rows[:8] if nt or ot]
    est = TRAIN.get(("estimated", cfg["class"])) or set()   # Forever's own ranks, priced by Classic's level price (training_rows)
    est_seen = sorted({n for L in range(lv, 61) for n, c in train.get(L, []) if n in est})
    CTX["training_estimated"] = est_seen
    by40 = (GOLD or 0) - owe_cost + sum(r[1] - r[2] - gear.get(r[0], 0) for r in rows if r[0] < MOUNT["level"])
    at60 = saved - (mount if mount_at else 0)
    CTX["gold"] = {"gold": GOLD, "reserve": reserve, "spend": spend, "mount": mount, "mount_level": MOUNT["level"], "by40": by40,
                   "mount_at": mount_at, "at60": at60, "gear_share": GEAR_SHARE,
                   "gear_before40": sum(c for L, c in PLANNED if L < MOUNT["level"]),
                   "income": [(r[0], r[1]) for r in rows[:6]]}
    o = ["## Gold plan", "",
         f"Gold now: **{AH.money(GOLD) if GOLD is not None else 'unknown (log in)'}**. Training you need "
         f"{'now and ' if owe_cost else ''}at the next two levels: "
         f"**{AH.money(reserve)}**. Free for gear now: **{AH.money(spend) if spend is not None else 'unknown'}**."
         + (f" You are **{AH.money(reserve - GOLD)} short** of that training: sell your crafts before you buy anything."
            if GOLD is not None and GOLD < reserve else ""), "",
         *([(f"Your spellbook (ForeverTape, {BOOK['when']}) lacks, at your level or below: "
             + ", ".join(f"{rank_label(n, r)} ({L}, {AH.money(c)})" for L, n, r, c in owe[0]) + f": {AH.money(owe_cost)}, train them first."
             if owe[0] else f"Your spellbook (ForeverTape, {BOOK['when']}) has every rank your build and kit use up to level {lv}.")
            + (f" Optional ranks it lacks: {', '.join(rank_label(n, r) for L, n, r, c in owe[1])} ({AH.money(sum(x[3] for x in owe[1]))})."
               if owe[1] else ""), ""] if owe is not None else
           ["Which ranks you know is unknown: ForeverTape (0.9.5 or later) writes your spellbook after a /reload or a logout.", ""]),
         f"Income is an estimate from Classic's data: coin and loot from about {kills_per_level(lv):.0f} kills a level (cloth, greens and "
         "other trade goods at the auction house's usual sale price after its cut, the rest at vendor prices), plus your pace of "
         f"{qpl:.1f} quests a level at Classic's quest money. It assumes you sell what drops or use it in place of buying it. \"Training\" "
         "counts the spells your rotation and kit use; optional ones (spells your build does not press, teleports) are listed apart. Only "
         "spells your race can learn are counted, and a talent's spell only once your build has the talent."
         + (f" Spells new in Forever ({', '.join(est_seen)}) are not in Classic's trainer table: their price here is Classic's usual price "
            "for the level, an estimate." if est_seen else ""), "",
         "| Level | Income (estimate) | Training you need at the next level | Optional training |", "|---|---|---|---|"]
    for L, inc, nt, ot, names in rows[:LAST - lv + 1][:14]:
        o += [f"| {L} | {AH.money(inc)} | {AH.money(nt) if nt else '-'}{' (' + ', '.join(names) + ')' if names else ''} | "
              f"{AH.money(ot) if ot else '-'} |"]
    o += ["", f"Mount at {MOUNT['level']}: about **{AH.money(mount)}** (Classic prices: riding {AH.money(MOUNT['riding'])} and the mount "
          f"{AH.money(MOUNT['mount'])}{', 10% off at ' + rep + ' with ' + RACE_FACTION.get(race, '') if discount else ''}; Forever's not "
          f"confirmed). At this income you would have about {AH.money(by40)} by {MOUNT['level']} after training and the plan's gear"
          + (f", enough for the mount at {mount_at}." if mount_at else ", not enough by 60 on income alone: auction sales have to make up the rest."),
          "", f"Gear budget: the gold above the next two levels' training now, then {GEAR_SHARE:.0%} of each level's income after training "
          "(character.json \"gear_share\"); the rest saves for the mount and for 60. "
          + ("Every bought or crafted upgrade below fits it. " if GOLD is not None else
             "With your gold unknown the upgrades below are not checked against it: log in (bnet_login.py) and refresh. ")
          + "The plan's "
          f"buys and crafts come to {AH.money(sum(c for L, c in PLANNED if L < MOUNT['level']))} before {MOUNT['level']} and "
          f"{AH.money(sum(c for L, c in PLANNED))} in all; you would reach 60 with about {AH.money(max(0, at60))}"
          + (" after the mount." if mount_at else ".")]
    hist = history(cfg)
    if len(hist) >= 2:
        a, z = hist[0], hist[-1]
        lv_a = a["level"] + a["xp"] / max(1, XP.get(a["level"], 1))
        lv_z = z["level"] + z["xp"] / max(1, XP.get(z["level"], 1))
        if lv_z - lv_a >= 0.5 and a.get("gold") is not None and z.get("gold") is not None:
            o += ["", f"Measured from your refreshes: {AH.money((z['gold'] - a['gold']) / (lv_z - lv_a))} net a level "
                  f"(gold change after what you spent, {lv_z - lv_a:.1f} levels from {a['time']} to {z['time']})."]
    o += [""]
    return o, spend


def history(cfg):
    p = char_dir(cfg["name"]) / "history.jsonl"
    return [json.loads(x) for x in p.read_text(encoding="utf-8").splitlines() if x.strip()] if p.exists() else []


def pays_for_itself(e, at, price):
    """(minutes of killing it saves, minutes of play its price takes to earn at the estimated income)."""
    L = e["level"]
    inc = income_per_level(L, QPL) or 1
    return minutes_saved(e, at), price / inc * minutes_per_level(L, at)


QPL = 8.0   # quests a level (main() sets the character's pace)
KILL_SHARE = 0.5   # the share of a solo quester's experience that comes from kills (an estimate; the rest is quest experience)
XP = {}


def kills_per_level(L):
    """Mobs killed in a level: the experience to the next level x KILL_SHARE / a same-level mob's experience (45 + 5 x level, Classic's
    rule for mobs in Azeroth); the table from the CMaNGOS dump (xp_for_level.csv)."""
    if not XP:
        for r in csv.DictReader(open(IP.RAW / "xp_for_level.csv", encoding="utf-8")):
            XP[int(r["level"])] = int(r["xp_to_next"])
    return XP.get(L, 0) * KILL_SHARE / (45 + 5 * L)


def span_minutes(new, old, L0, L1, at):
    """Minutes of killing the items `new` save over the items `old` from level L0 to L1: at each level the seconds per kill the stat
    values give the difference x that level's kills (an item's stats are worth less as a character's own grow: holding its percent at
    the level it was put on had kept a level-27 hat ahead of every later one, 2026-11-09)."""
    return sum((sum(value((x or {}).get("stats"), at(L)) for x in new) - sum(value((x or {}).get("stats"), at(L)) for x in old))
               * kills_per_level(L) for L in range(L0, L1)) / 60


def minutes_saved(e, at):
    """Minutes of killing an upgrade saves while it is worn, level by level until it is replaced (or 60): by its stats against what it
    replaces when the plan knows both, else its share of faster kills x the time per kill x the kills."""
    end = e["until"] or 60
    if e.get("item") and "prev" in e:
        return span_minutes([e["item"], e.get("off")], e["prev"], e["level"], end, at)
    return sum(e["gain"] * at(L)["time"] * kills_per_level(L) for L in range(e["level"], end)) / 60


def line(e, at):
    p, o = e["item"], e.get("off")
    wear = f"wear at {e['level']}" if e["level"] > e["get_at"] else "wear it right away"
    what, src = upgrade_name(e)
    rep = f", replaces {e['replaces']}" if e.get("replaces") else ""
    until = f"; best until level {e['until']}" if e.get("until") else "; best to the end of leveling"
    out = f"- **{e['slot']}**: {what}, {pct(e['gain'])} {FASTER}{rep} ({wear}{until}; saves about {minutes_saved(e, at):.0f} {KILLING}). {src}."
    if e.get("wait"):
        out += f" {e['wait']}."
    if e.get("off_route"):
        out += f" {e['off_route']}."
    if e.get("route_unknown"):
        out += f" {e['route_unknown']}."
    if e.get("on_route"):
        out += f" {e['on_route']}."
    if e.get("passed") and (e["until"] or 60) - e["level"] >= 8:   # a long-held item: why nothing replaces it sooner
        alts = sorted(e["passed"], key=lambda x: -x[2])[:3]
        out += " Why it stays: " + "; ".join(f"{n} at {L}, {why}" for L, n, g, why in sorted(alts)) + "."
    fb = e.get("fallback")
    miss = "If you do not craft it" if e.get("unsure") == "craft" else "If it does not drop"
    if fb and "keep" in fb:
        return out + (f" {miss}, keep your {fb['keep']}." if fb["keep"] else "")
    if fb:
        when = f"from level {fb['level']}" if fb["level"] > e["level"] else "instead"
        out += f" {miss}, wear {fb['item']['name']} {when} ({pct(fb['gain'])} {FASTER}; {sources_text(fb['item'])})."
    return out


KIND_ORDER = ["bags", "dungeon", "quest", "craft", "vendor", "auction", "market"]


def primary(e):
    """The source to act on: the first acquirable kind in KIND_ORDER; a craft from a recipe you do not know yields to the auction house
    when the item is sold there (Earthen Silk Slippers, a Forever recipe nobody had found, sold at 2g 69s, 2026-11-09)."""
    srcs = new_sources(e)
    sold = any(s["kind"] in ("auction", "market") for s in srcs)
    later = (e.get("get_at") or 0) > NOW_LV and any(s["kind"] == "market" for s in srcs)
    for k in KIND_ORDER:
        for s in srcs:
            if s["kind"] == k and not (k == "craft" and sold and s.get("spell") not in KNOWN) and not (k == "auction" and later):
                return s   # bought on a later visit: the usual price, not this hour's listing
    return srcs[0] if srcs else {"kind": "?"}


def action_sections(evs, at, L, head="###"):
    """Upgrades grouped by what you do: run a dungeon (by dungeon and boss), do a quest, craft, buy."""
    o = []
    by = {}
    for e in sorted(evs, key=lambda e: -e["gain"]):
        by.setdefault(primary(e)["kind"], []).append(e)
    if by.get("bags"):   # (2026-11-10, bags.py: what you bought or carry already)
        o += [f"{head} In your bags", ""] + [line(e, at) for e in by["bags"]] + [""]
    if by.get("dungeon"):
        o += [f"{head} Dungeons to run", ""]
        dz = {}
        for e in by["dungeon"]:
            s = primary(e)
            dz.setdefault((s["zone"], s["lo"], s["hi"], s.get("estimated")), []).append((s["boss"], e))
        for (z, lo, hi, est), ev in sorted(dz.items(), key=lambda kv: -sum(e["gain"] for _, e in kv[1])):
            o += [f"- **{z}** (level {lo}-{hi}{', range estimated' if est else ''}):"]
            o += [f"  - {boss}: " + line(e, at)[2:] for boss, e in ev]
        o += [""]
    if by.get("quest"):
        o += [f"{head} Quests to do", ""] + [line(e, at) for e in by["quest"]] + [""]
    if by.get("craft"):
        o += [f"{head} Craft", ""]
        for e in by["craft"]:
            s = primary(e)
            reag = reagents_of(s["spell"]) if s.get("spell") else []
            o += [line(e, at) + (" Materials: " + mats_text(reag) + "." if reag else "")]
        o += [""]
    if by.get("vendor"):
        o += [f"{head} Buy", ""] + [line(e, at) for e in by["vendor"]] + [""]
    for kind, title in (("auction", "Buy on the Auction House (listed now; prices change hourly; most minutes saved per gold first)"),
                        ("market", "Look for on the Auction House (not listed this hour, usually is; usual prices)" if L <= NOW_LV + LOOKAHEAD
                         else "Buy on the Auction House (usually listed; usual prices, look again then)")):
        if not by.get(kind):
            continue
        o += [f"{head} {title}", ""]
        for e in sorted(by[kind], key=lambda e: -minutes_saved(e, at) / (price_of(e) or 1)):
            saves, earn = pays_for_itself(e, at, price_of(e) or 0)
            verdict = f" Saves about {saves:.0f} {KILLING}; earning its price takes about {earn:.0f} min of play."
            if e.get("paid") and e["paid"][0] > max(e["get_at"], NOW_LV):
                verdict += f" Your gear budget covers it at level {e['paid'][0]} ({AH.money(e['paid'][1])} left after it)."
            elif e.get("paid"):
                verdict += f" Fits your gear budget ({AH.money(e['paid'][1])} left after it)."
            o += [line(e, at) + verdict]
        o += [""]
    return o


GOLD = None   # the character's gold in copper (Blizzard's protected profile, after bnet_login.py), or None


def character_gold(cfg):
    """Gold from the protected profile with the user's login token (~/.wow-forever-tools/blizzard-user-token.json, about 24 hours);
    None without a valid token."""
    import time
    import urllib.parse
    p = pathlib.Path.home() / ".wow-forever-tools" / "blizzard-user-token.json"
    if not p.exists():
        return None
    t = json.loads(p.read_text(encoding="utf-8"))
    if t.get("expires_at", 0) < time.time():
        return None
    region = cfg.get("region", "us")
    ns = f"profile-forever-{region}"
    st, acct = bnet.get(region, t["access_token"], "/profile/user/wow", ns)
    if st != 200:
        return None
    for wa in acct.get("wow_accounts") or []:
        for ch in wa.get("characters") or []:
            if f"/character/{cfg['slug']}?" in (ch.get("character") or {}).get("href", "") and ch.get("protected_character"):
                st2, js = bnet.get(region, t["access_token"], urllib.parse.urlparse(ch["protected_character"]["href"]).path, ns)
                return js.get("money") if st2 == 200 else None
    return None


NAMES = {}


def item_name(i):
    if not NAMES:
        for r in csv.DictReader(open(IP.RAW / "item_names.csv", encoding="utf-8")):
            NAMES[int(r["item"])] = r["name"]
    return NAMES.get(i, f"item {i}")


def resale(item):
    """(what one sells for after the auction house's 5% cut, how many to count as sold): the usual price of real sales (Insights, source
    "s"), or 1c under today's cheapest listing when that is lower; None when the product has no sales history."""
    t = PRICES.typical.get(item) if PRICES else None
    if not t or t[1] != "s":
        return None
    c = PRICES.cheapest(item)   # you sell by undercutting the cheapest listing when it is below the usual price (2026-11-09: Spidersilk
    price = min(t[0], c[0] - 1) if c else t[0]   # Boots read 79s after the cut from past sales while 88 pairs were listed at 69s)
    return 0.95 * price, min(8, int(t[2]) if len(t) > 2 else 0)   # (value after the cut, at most 8 sold, no more than a day's sales)


def net_money(c):
    """A net cost, or what a step makes when selling its products pays more than their materials."""
    return AH.money(c) if c >= 0 else f"makes {AH.money(-c)}"


def profession_section(profs):
    """Per profession: the cheapest expected way from the character's skill to its rank's cap with the recipes it knows (professions.py),
    with the materials it takes at today's prices."""
    if not RECIPES:
        return []
    tri = PF.thresholds()
    o = ["## Professions", "",
         "The cheapest way up with the recipes you know, materials at today's prices (auction house or vendor, the cheaper). Crafts are "
         "expected counts: a yellow or green recipe does not always give a point. Forever lets you learn recipes earlier than Classic did, "
         "so check your trainer whenever a profession stalls.", ""]
    crafts = [e for e in PLAN_EVENTS if primary(e)["kind"] == "craft"]
    CTX["professions"], CTX["crafts"] = [], []
    for e in sorted(crafts, key=lambda e: e["level"]):
        s0 = primary(e)
        CTX["crafts"].append({"item": e["item"]["name"], "slot": e["slot"], "level": e["level"], "profession": s0["profession"],
                              "known": s0.get("spell") in KNOWN, "learn": s0.get("learn"), "skill": s0.get("skill"),
                              "have": (profs.get(s0["profession"]) or (0,))[0]})
    if crafts:   # what the plan's crafts ask of the professions (2026-11-09, the "work toward" list)
        o += ["Crafts in your plan:", ""]
        for e in sorted(crafts, key=lambda e: e["level"]):
            s = primary(e)
            have = (profs.get(s["profession"]) or (0,))[0]
            how = ("you know the recipe" if s.get("spell") in KNOWN else
                   f"learn it ({s.get('learn') or 'source unknown'}); Classic asked {s['profession']} {s.get('skill') or '?'}, you have {have}")
            o += [f"- {e['item']['name']} ({e['slot']}, level {e['level']}): {how}."]
        o += [""]
    for prof in [x for x in ("Tailoring", "Blacksmithing", "Leatherworking", "Engineering", "Alchemy", "Enchanting", "Cooking", "First Aid",
                              "Mining") if x in profs]:
        if prof not in profs:
            continue
        skill, cap = profs[prof]
        if skill >= cap:
            CTX["professions"].append({"name": prof, "skill": skill, "cap": cap, "stop": skill, "total": 0, "steps": [], "mats": [],
                                       "capped": True})
            o += [f"**{prof}** {skill}/{cap}: at your rank's cap; train the next rank to go on.", ""]
            continue
        groups, stop, mats = PF.skill_plan(prof, skill, cap, RECIPES, tri, unit_price, sell=resale)
        o += [f"### {prof} {skill} to {cap}", ""]
        if not groups:
            CTX["professions"].append({"name": prof, "skill": skill, "cap": cap, "stop": skill, "total": 0, "steps": [], "mats": []})
            o += ["No recipe you know gives a point at your skill: learn new ones at the trainer.", ""]
            continue
        o += ["| Skill | Recipe | Crafts (expected) | Cost after selling what you make |", "|---|---|---|---|"]
        total = 0.0
        for a, b, r, crafts, c in groups:
            total += c
            o += [f"| {a}-{b} | {r['name']} | {crafts:.0f} | {net_money(c)} |"]
        top6 = sorted(mats.items(), key=lambda kv: -(unit_price(kv[0]) or 0) * kv[1])[:6]
        CTX["professions"].append({"name": prof, "skill": skill, "cap": cap, "stop": stop, "total": total,
                                   "steps": [{"from": a, "to": b, "recipe": r["name"], "crafts": round(crafts), "cost": c,
                                              "mats": [(item_name(i), round(n * crafts)) for i, n in r["reagents"]],
                                              "product": item_name(r["out_item"]) if r.get("out_item") else None,
                                              "sell": resale(r["out_item"]) if r.get("out_item") else None}
                                             for a, b, r, crafts, c in groups],
                                   "mats": [(item_name(i), round(n)) for i, n in top6]})
        o += ["", (f"You spend about {AH.money(total)} in all" if total >= 0 else f"You make about {AH.money(-total)} in all")
              + f" to reach {stop}, after selling what you make (its usual sale price, or under today's cheapest listing when that is lower) (at most 8 of each, and "
              "no more than a day's sales; products without a sales history count as unsold)"
              + ("." if stop >= cap else f"; from {stop} no recipe you know gives points: learn new ones at the trainer.")]
        top = sorted(mats.items(), key=lambda kv: -(unit_price(kv[0]) or 0) * kv[1])[:6]
        o += ["Materials: " + ", ".join(f"{item_name(i)} x{n:.0f}" for i, n in top) + ".", ""]
    return o


CONSUMABLE_KIND = {6: "Weapon oil", 3: "Food", 11: "Elixir", 4: "Scroll"}
SKILL_NAME = {333: "Enchanting", 185: "Cooking", 171: "Alchemy"}


def consumable_effect(c, texts, school_share):
    """(fight-lab stats, kill-experience bonus %, minutes) of a consumable from its tooltip (Blizzard's item API); the database's stats
    when the tooltip names none (oils carry theirs only in the tooltip)."""
    st, txt = {}, " ".join(texts)
    m = re.search(r"spell (frost|fire|arcane|shadow|nature|holy) damage by up to (\d+)", txt, re.I)
    if m:
        st["spell_power"] = int(m.group(2)) * school_share.get(m.group(1).lower(), 0)
    else:
        m = re.search(r"spell damage(?: and healing)? by up to (\d+)|gain (\d+) Spell Damage", txt, re.I)
        if m:
            st["spell_power"] = int(m.group(1) or m.group(2))
    m = re.search(r"(\d+) mana every 5 sec", txt)
    if m:
        st["mp5"] = int(m.group(1))
    for name, key in (("Intellect", "intellect"), ("Spirit", "spirit"), ("Stamina", "stamina")):
        m = re.search(rf"(?:gain|increase[sd]?[^.]*?) (\d+) {name}|{name} by (\d+)", txt)
        if m:
            st[key] = int(m.group(1) or m.group(2))
    if not st:
        for i, v in enumerate(c.get("stats") or []):
            if v and i in IP.STAT:
                st[IP.STAT[i]] = st.get(IP.STAT[i], 0) + v
            elif v and i in IP.SCHOOLS:
                st["spell_power"] = st.get("spell_power", 0) + v * school_share.get(IP.SCHOOLS[i], 0)
    xp = re.search(r"experience gained from kills is increased by (\d+)%", txt)
    dur = re.search(r"(?:Lasts for|for) (\d+) (min|minutes|hour|hours)", txt)
    minutes = (int(dur.group(1)) * (60 if dur.group(2).startswith("hour") else 1)) if dur else None
    return st, (int(xp.group(1)) if xp else 0), minutes


def trip(cfg, snap, at, lv):
    """(minutes of play, level) to your next town visit: the next level with training you need (character.json "hours_out" overrides,
    in hours of play), from the rest of this level and the play time of the levels between (minutes_per_level)."""
    if cfg.get("hours_out"):
        return float(cfg["hours_out"]) * 60, None
    train = training_by_level(cfg["class"])
    nxt = next((L for L in range(lv + 1, 61) if any(n in needed_at(cfg, L) for n, c in train.get(L, []))), lv + 2)
    left = 1 - (snap["profile"].get("experience") or 0) / max(1, XP.get(lv) or kills_per_level(lv) and XP.get(lv, 1) or 1)
    return max(0.0, left) * minutes_per_level(lv, at) + sum(minutes_per_level(L, at) for L in range(lv + 1, nxt)), nxt


def consumable_lines(level, wl, profs, school_share, trip_min=None, at=None):
    """Oils, food, elixirs and scrolls usable now: how much faster kills, how long, what one costs (auction house, or the materials when
    the character's own profession makes it), what an hour of leveling with it costs, how many to buy for the time to your next town
    visit (2026-11-09, user: "can you make it so it says how many to buy? Since they only last so much time and sometime I don't come back
    to cities for hours") and whether it earns its price back: the play minutes an hour of it saves (faster kills over the share of play
    spent killing, and a food's extra kill experience) against the play minutes its hour's cost takes to earn."""
    db = IP.sim_db()
    cands = [c for c in db["consumables"] if c.get("type") in CONSUMABLE_KIND and (c.get("lvl") or 0) <= level]
    texts = IP.item_texts([c["id"] for c in cands])
    rs = IP.recipe_skills()
    makes = {}
    for r in csv.DictReader(open(IP.RAW / "craft_spells.csv", encoding="utf-8")):
        if r["creates"]:
            makes.setdefault(int(r["creates"]), int(r["spell"]))
    rows = []
    for c in cands:
        t = texts.get(c["id"]) or {}
        st, xp, minutes = consumable_effect(c, t.get("texts") or [], school_share)
        gain = value(st, wl) / wl["time"]
        if gain < 0.005 and not xp:
            continue
        how, cost = "buy", (PRICES.buy(c["id"]) if PRICES else None)
        sp = makes.get(c["id"])
        reag = []
        if sp and rs.get(sp) and rs[sp][0] in SKILL_NAME:
            prof = SKILL_NAME[rs[sp][0]]
            have = (profs.get(prof) or (None,))[0]
            if have is not None and have >= rs[sp][1]:
                reag = reagents_of(sp)
                mats = sum((unit_price(i) or 0) * n for _, n, i in reag) if PRICES else None
                if mats and (cost is None or mats <= cost):
                    how, cost = f"make it ({prof} {rs[sp][1]})", mats
                elif mats:
                    how = f"buy (cheaper than making it: {AH.money(mats)} in materials)"
            elif have is not None:
                how = f"buy (you make it at {prof} {rs[sp][1]}; you have {have})"
        per_hour = cost * 60 / minutes if cost and minutes else None
        rows.append((CONSUMABLE_KIND[c["type"]], c["name"], st, xp, gain, minutes, how, cost, per_hour,
                     [(n, k) for n, k, _ in reag] if how.startswith("make it") else []))
    import math
    income_min = (income_per_level(level, QPL) / minutes_per_level(level, at)) if at else None   # copper a minute of play
    out = []
    CTX["consumables"] = []
    for kind in ("Weapon oil", "Food", "Elixir", "Scroll"):
        ks = sorted([r for r in rows if r[0] == kind], key=lambda r: -(r[4] + r[3] / 100 * 0.5))[:3]
        scored = []
        for k, name, st, xp, gain, minutes, how, cost, per_hour, reag in ks:
            saved = 60 * (gain * PLAY_KILL_SHARE + xp / 100 * KILL_SHARE)   # play minutes an hour of it saves
            earn = per_hour / income_min if per_hour and income_min else None   # play minutes its hour's cost takes to earn
            qty = math.ceil(trip_min / minutes) if trip_min and minutes else None
            scored.append((k, name, st, xp, gain, minutes, how, cost, per_hour, saved, earn, qty, reag))
        good = [x for x in scored if x[10] is not None and x[9] >= x[10]]
        pick = max(good, key=lambda x: x[9] - x[10])[1] if good else None   # the one that saves the most beyond its price
        for k, name, st, xp, gain, minutes, how, cost, per_hour, saved, earn, qty, reag in scored:
            eff = ", ".join(f"+{v:g} {x.replace('_', ' ')}" for x, v in st.items()) + (f", +{xp}% kill experience" if xp else "")
            worth = earn is not None and saved >= earn
            CTX["consumables"].append({"kind": kind, "item": name, "effect": eff, "pct": pct(gain), "minutes": minutes, "how": how,
                                       "cost": cost, "hour": per_hour, "best": name == (pick or scored[0][1]), "qty": qty,
                                       "total": qty * cost if qty and cost else None, "saved": saved, "earn": earn, "worth": worth,
                                       # what to buy when you make it yourself (2026-11-14: the town list said "Buy ×14 Smoked Sagefish"
                                       "mats": [(n, c * qty) for n, c in reag] if qty else []})   # at the materials' price)
            buy = f"×{qty} ({AH.money(qty * cost)})" if qty and cost else "?"
            verdict = (f"yes: saves {saved:.1f} min an hour, costs {earn:.1f}" if worth else
                       f"no: saves {saved:.1f} min an hour, costs {earn:.1f}" if earn is not None else "?")
            out.append(f"| {kind} | {name} | {eff} | {pct(gain)} | {minutes or '?'} min | {how} | {AH.money(cost) if cost else 'no price'} | "
                       f"{buy} | {verdict} |")
    if not out:
        return []
    return ([f"| Kind | Item | Effect | {FASTER[0].upper() + FASTER[1:]} | Lasts | How | One costs | For your trip | Earns its price back |",
             "|---|---|---|---|---|---|---|---|---|"] + out +
            ["", "One food at a time (well fed), one weapon oil, scrolls by stat. Kill experience is extra: a food's +5% speeds up the "
             "experience you get from kills, not from quests. Elixirs: Classic lets several stack; Forever's rule is not confirmed."])


def upgrade_name(e):
    """(what to get, where): a weapon pair names the half you get and the half you keep."""
    new = new_pieces(e)
    keep = [it["name"] for it in pieces(e) if it not in new]
    what = " + ".join(it["name"] for it in new) or " + ".join(keep)
    if new and keep:
        what += f" (with your {', '.join(keep)})"
    return what, " / ".join(t for t in (sources_text(it) for it in new) if t) or "you hold it already"


def event_row(e, at):
    """One upgrade as the checklist page shows it."""
    pr = price_of(e)
    fb, fbt = e.get("fallback"), None
    if fb and "keep" in fb:
        fbt = f"keep your {fb['keep']}" if fb["keep"] else None
    elif fb:
        fbt = f"{fb['item']['name']}, {pct(fb['gain'])} {SHORT} ({sources_text(fb['item'])})"
    why = None
    if e.get("passed") and (e["until"] or 60) - e["level"] >= 8:
        why = "; ".join(f"{n} at {L}: {w}" for L, n, g, w in sorted(sorted(e["passed"], key=lambda x: -x[2])[:2]))
    budget = None
    if e.get("paid"):
        budget = (f"your gear budget covers it at level {e['paid'][0]}" if e["paid"][0] > max(e["get_at"], NOW_LV)
                  else "fits your gear budget")
    src = primary(e)
    mats = mats_text(reagents_of(src["spell"])) if src["kind"] == "craft" and src.get("spell") else None
    saves, earn = pays_for_itself(e, at, pr) if pr else (minutes_saved(e, at), 0)
    what, where = upgrade_name(e)
    return {"slot": e["slot"], "item": what,
            "quality": max((it.get("quality") or 2) for it in new_pieces(e)) if new_pieces(e) else 2, "pct": pct(e["gain"]),
            "minutes": round(saves), "earn": round(earn), "level": e["level"], "get_at": max(e["get_at"], NOW_LV), "until": e["until"],
            "kind": src["kind"], "where": where, "price": pr, "budget": budget, "replaces": e.get("replaces"),
            "fallback": fbt, "miss": "If you do not craft it" if e.get("unsure") == "craft" else "If it does not drop", "why": why,
            "wait": e.get("wait"), "off_route": e.get("off_route"), "on_route": e.get("on_route"), "route_unknown": e.get("route_unknown"),
            "mats": mats}


def plan_state(events, lv, fetched):
    return {"time": fetched, "level": lv, "gold": GOLD,
            "plan": sorted([e["slot"], e["level"], e["item"]["name"]] for e in events)}


def change_lines(d, events, lv):
    """What moved since the last refresh (state.json, written by refreshes only): upgrades new to the plan, gone from it, or at another
    level (2026-11-09, user: "have you look every even level or even every level and see what upgrades I can make")."""
    p = d / "state.json"
    if not p.exists():
        return []
    old = json.loads(p.read_text(encoding="utf-8"))
    f = d / "armory" / "fetched.txt"
    if (d / "state.prev.json").exists() and f.exists() and old.get("time") == f.read_text(encoding="utf-8").strip():
        old = json.loads((d / "state.prev.json").read_text(encoding="utf-8"))   # a page made again from this refresh's snapshot (--no-refresh):
        # the change list stays the refresh's own (2026-11-10: a rerun after a refresh had compared the plan with itself)
    was = {(s, n): L for s, L, n in old["plan"]}
    now = {(e["slot"], e["item"]["name"]): e["level"] for e in events}
    new = [f"{n} ({s}, level {L})" for (s, n), L in sorted(now.items(), key=lambda kv: kv[1]) if (s, n) not in was]
    try:   # why a piece left (2026-11-13, user: "Why does the checklist say this then?" of two pieces worn since): worn now, or what replaces it
        worn = {(it.get("name") or "").lower() for it in json.loads((d / "armory" / "equipment.json").read_text(encoding="utf-8"))
                .get("equipped_items") or []}
    except (OSError, ValueError):
        worn = set()
    first = {}
    for (s, n), L in sorted(now.items(), key=lambda kv: kv[1]):
        if (s, n) not in was:
            first.setdefault(s, (n, L))
    why = lambda s, n: ("worn now" if n.lower() in worn else f"{first[s][0]} at level {first[s][1]} replaces it" if s in first
                        else "dropped: nothing in its place")
    gone = [f"{n} ({s}: {why(s, n)})" for (s, n) in was if (s, n) not in now]
    moved = [f"{n} ({s}) level {was[(s, n)]} to {L}" for (s, n), L in now.items() if (s, n) in was and was[(s, n)] != L]
    CTX["changes"] = {"time": old["time"], "level": old["level"], "gold_then": old.get("gold"), "new": new, "gone": gone, "moved": moved}
    o = [f"## Since your last refresh ({old['time']}, level {old['level']})", ""]
    if old.get("gold") is not None and GOLD is not None:
        o += [f"- Gold: {AH.money(old['gold'])} then, {AH.money(GOLD)} now."]
    if new:
        o += [f"- New in the plan: {', '.join(new)}."]
    if gone:
        o += [f"- Left the plan: {', '.join(gone)}."]
    if moved:
        o += [f"- Moved: {', '.join(moved)}."]
    if not (new or gone or moved):   # ("Nothing new in the plan" had stood above a "Left the plan" line, 2026-11-14)
        o += ["- Nothing new in the plan."]
    return o + [""]


def judge_lines(worn, events, wl, lv, cfg):
    """A quick test for a random drop or an auction find (2026-11-09, user: "random drops, whatever is available"): per slot what the
    item you will wear adds in spell power equivalents (each stat at this level's value over spell power's) and what a find must add on
    top to save MIN_MINUTES before the plan's next upgrade of the slot (and 0.5% faster kills)."""
    unit = "stamina" if cfg.get("metric") == "tank" else "spell_power"   # a tank counts in stamina (2026-11-09, Tara)
    sp = wl["w"].get(unit) or 0
    if sp <= 0:
        return []
    if unit == "spell_power":
        rate = {k: wl["w"].get(k, 0.0) / sp for k in ("intellect", "spirit", "stamina", "mp5", "armor")}
        sch = ", ".join(f"{k} {v:.0%}" for k, v in cfg["school_share"].items())
        top = max(cfg["school_share"], key=cfg["school_share"].get) if cfg["school_share"] else "frost"   # (the example names the main school)
        how = (f"Count a piece's stats in spell power: 1 intellect = {rate['intellect']:.2f}, 1 spirit = {rate['spirit']:.2f}, 1 stamina = "
               f"{rate['stamina']:.2f}, 1 mana per 5 sec = {rate['mp5']:.2f}, 100 armor = {100 * rate['armor']:.2f}; school damage counts by "
               f"your build's share ({sch}: +10 {top} damage counts {10 * cfg['school_share'].get(top, 0):.1f}), \"spell damage and "
               "healing\" in full.")
        CTX["rates"] = {**{k: round(v, 2) for k, v in rate.items()}, **{f"{k} damage": round(v, 2) for k, v in cfg["school_share"].items()}}
    else:
        names = {"armor": "100 armor", "block_value": "block value", "attack_power": "attack power", "weapon_dps": "weapon damage per second",
                 "mp5": "mana per 5 sec"}
        rate = sorted(((k, v / sp * (100 if k == "armor" else 1)) for k, v in wl["w"].items() if k != unit and abs(v / sp) >= 0.005),
                      key=lambda kv: -abs(kv[1]))[:9]
        nm = lambda k: names.get(k, k.replace("_", " "))   # (a raw key had shown: "1 spell_power = 0.48", 2026-11-14)
        how = "Count a piece's stats in stamina: " + ", ".join(f"1 {nm(k)} = {v:.2f}".replace("1 100 armor", "100 armor")
                                                             for k, v in rate) + "."
        CTX["rates"] = {nm(k): round(v, 2) for k, v in rate}
    label = "spell power" if unit == "spell_power" else "stamina"
    CTX["unit"] = label
    o = ["### Judging a drop or an auction find", "",
         how + " A find is worth wearing when it reaches the number below: enough to save "
         f"{MIN_MINUTES:.0f} minutes before the plan's next upgrade of the slot.", "",
         f"| Slot | You wear (or the plan's next piece) | Worth ({label}) | A find must reach | Next planned upgrade |", "|---|---|---|---|---|"]
    for slot in SLOT_ORDER:   # against the item the plan has you in over the next levels (the planned one when it comes within LOOKAHEAD)
        it = worn.get(slot)
        since = max(lv, (it or {}).get("planned") or lv)
        nxt = min((e["level"] for e in events if e["slot"] == slot and e["level"] > since), default=60)
        kills = sum(kills_per_level(L) for L in range(since, max(nxt, since + 1)))
        need = max(UPGRADE * wl["time"], MIN_MINUTES * 60 / max(kills, 1)) / sp
        have = value((it or {}).get("stats"), wl) / sp
        name = (it or {}).get("name") or "empty"
        if (it or {}).get("planned"):
            name += f" (planned, level {it['planned']})"
        o += [f"| {slot} | {name} | {have:.0f} | {have + need:.0f} | {nxt if nxt < 60 else '-'} |"]
        CTX.setdefault("judge", []).append({"slot": slot, "item": name, "have": round(have), "need": round(have + need),
                                            "next": nxt if nxt < 60 else None})
    return o + [""]


def enchant_lines(worn, ench, profs, wl, at=None, lv=None):
    """Per enchantable slot: the best enchant at the character's Enchanting skill for the item it will wear, and the next one a higher
    skill opens; only enchants worth 0.1% faster kills or more."""
    skill = (profs.get("Enchanting") or (0, 0))[0]
    out = []
    for slot in ("wrist", "chest", "back", "hands", "feet", "weapon"):
        it = worn.get(slot)
        if not it:
            continue
        if (it.get("until") or 60) - it.get("since", 0) < MIN_LASTS:   # not worth enchanting an item you wear for a level or two
            out.append(f"- **{it['name']}** ({slot}): skip, you replace it at level {it['until']}.")
            continue
        kinds = ["weapon2h", "weapon"] if slot == "weapon" and it.get("two_hand") else (["weapon"] if slot == "weapon" else [slot])
        have = value(it.get("enchant_stats"), wl)
        opts = sorted([e for e in ench if e["slot"] in kinds], key=lambda e: -value(e["stats"], wl))
        now = next((e for e in opts if e["skill"] <= skill), None)
        nv = value(now["stats"], wl) if now else 0.0
        who = f"**{it['name']}** ({slot}{', once you have it at level ' + str(it['planned']) if it.get('planned') else ''})"
        txt = []
        if now and at and lv and (nv - have) / wl["time"] >= 0.001:   # enchant only what you keep long enough for it to save MIN_MINUTES
            life = {"gain": (nv - have) / wl["time"], "level": max(lv, it.get("since") or lv), "until": it.get("until")}
            if minutes_saved(life, at) < MIN_MINUTES:
                out.append(f"- {who}: skip, {now['name']} saves only about {minutes_saved(life, at):.0f} {KILLING} before you replace it"
                           + (f" at level {it['until']}." if it.get("until") else "."))
                continue
        if now and (nv - have) / wl["time"] >= 0.001:
            txt.append(f"{now['name']} (Enchanting {now['skill']}, {now['learn']}), {pct((nv - have) / wl['time'])} {FASTER}"
                       + (f" over its {', '.join(it['enchant'])}" if it.get("enchant") else "") + ". Materials: "
                       + mats_text(now["reagents"]) + ".")
        nxt = sorted([e for e in opts if skill < e["skill"] <= skill + 30 and (value(e["stats"], wl) - max(have, nv)) / wl["time"] >= 0.001], key=lambda e: e["skill"])[:1]
        for e in nxt:
            if at and lv and minutes_saved({"gain": (value(e["stats"], wl) - have) / wl["time"], "level": max(lv, it.get("since") or lv),
                                            "until": it.get("until")}, at) < MIN_MINUTES:
                continue   # the same 20-minute bar as the enchant you can make now
            txt.append(f"At Enchanting {e['skill']}: {e['name']} ({e['learn']}), {pct((value(e['stats'], wl) - have) / wl['time'])} {FASTER}.")
        if txt:
            out.append(f"- {who}: " + " ".join(txt))
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("name")
    ap.add_argument("--no-refresh", action="store_true")
    ap.add_argument("--level", type=int, help="your level when Blizzard's data lag (a level-up since the last logout it has seen); kept "
                    "in level-said.json until it has seen one")
    a = ap.parse_args()
    d = char_dir(a.name)
    cfg = json.load(open(d / "character.json", encoding="utf-8"))
    snap, fetched = snapshot(cfg, d, not a.no_refresh)
    addon_gold = fresher(cfg, snap, d, a.level)   # the add-ons' newer level and gold, or your word (2026-11-14)
    # which state the numbers come from while the project's model is being updated (2026-11-21, the audit session: "say on the page
    # which state the numbers come from"): the hand-kept characters/model-note.json {"text", "until"}, up front until its date
    try:
        mn = json.load(open(HERE / "model-note.json", encoding="utf-8"))
        if mn.get("text") and datetime.date.today().isoformat() <= (mn.get("until") or "9999"):
            NOTICES.append(mn["text"])
    except (OSError, ValueError):
        pass
    sys.path.insert(0, str(DATA))
    b, order, prov, rot = pick(cfg, snap["profile"].get("level"))
    # who learns which trainer spells (train_level): the race, and the level the build takes each talent (a talent's ability ranks)
    TRAIN["race"] = (snap["profile"].get("race") or {}).get("id")
    FR = fightlab_run()
    for L in range(10, 61):
        for n, k in FR.allocation_at({"allocation": b["allocation"], "order": order}, L).items():
            if k:
                TRAIN.setdefault("talent_from", {}).setdefault(n, L)
    wfile = cfg.get("weights") or f"{cfg['class']}-{rot}.json"
    aw = None if cfg.get("weights") else addon_weights(dict(cfg, _level=snap["profile"].get("level")), b, order, rot, d)
    if aw:
        at, wrec = aw
        wfile = wrec["file"]
        print(f"stat values: the gear add-on's ({wrec['date']}): {wrec['unit']} {wrec['have']} puts the character "
              f"{100 * wrec['share']:.0f}% of the way from the lab's standard gear to the level's best Forever set")
    else:
        at, wrec = weights(cfg["class"], rot, wfile)
    global FASTER, SHORT, KILLING, MINUTES_OF
    if cfg.get("metric") == "tank":
        FASTER, SHORT, KILLING, MINUTES_OF = "better tanking", "better", "min of group play", "minutes of group play"
    commit, n_items = IP.sim_version()
    DATAVER.update({"sim": commit, "items": n_items, "weights": wrec.get("date"), "weights_build": wrec.get("build")})
    if wrec.get("build") != b["id"]:
        print(f"WARNING: stat values were measured for {wrec.get('build')}; the page now shows {b['id']}: re-run stat_weights.py")
    pool = IP.pool(cfg["class"], cfg["faction"], cfg["school_share"], cfg.get("region", "us"))
    profs = skills(snap)
    PROFS.update(profs)
    global MIN_LASTS, MIN_MINUTES, PRICES, GOLD
    GOLD = addon_gold if addon_gold is not None else character_gold(cfg)
    if GOLD is None:
        # 2026-11-20 (Arcea at 38): the bag add-on's record was 3 minutes older than Blizzard's logout and Blizzard's own gold needs the
        # day-long login, so the page had read "log in for gold" and planned the mount from nothing; the older record beats no gold
        older = BG.record(cfg, snap["profile"]["name"])
        if older and older.get("money") is not None:
            GOLD = older["money"]
            seen = (snap["profile"].get("last_login_timestamp") or 0) / 1000
            NOTICES.append(f"Gold is your bag add-on's of {older['when']}, before your logout at "
                           f"{datetime.datetime.fromtimestamp(seen).strftime('%Y-%m-%d %H:%M') if seen else 'an unknown time'}: "
                           "anything you spent or looted after it is not in it.")
    global QPL
    lv0 = snap["profile"]["level"]
    QPL = len((snap.get("quests-completed") or {}).get("quests") or []) / max(1, lv0 - 1)
    if not a.no_refresh:   # the history the measured income comes from: one line per refresh
        with open(d / "history.jsonl", "a", encoding="utf-8") as f:
            f.write(json.dumps({"time": fetched, "level": lv0, "xp": snap["profile"].get("experience", 0), "gold": GOLD}) + "\n")
    global NOW_LV
    NOW_LV = lv0
    MIN_LASTS = int(cfg.get("min_levels", MIN_LASTS))
    MIN_MINUTES = float(cfg.get("min_minutes", MIN_MINUTES))
    ah = cfg.get("ah") or {}
    if ah.get("ahcopy") and pathlib.Path(ah["ahcopy"]).exists():   # the user's ForeverTape add-on, read only
        PRICES = AH.Prices(ah["ahcopy"], ah.get("insights"))
        # vendor prices: Classic's for every vendor-sold item, then the add-on project's hourly export where it has seen the vendor
        for r in csv.DictReader(open(IP.RAW / "item_names.csv", encoding="utf-8")):
            if r.get("vendor") == "1" and r.get("buy_price", "0").isdigit() and int(r["buy_price"]):
                VENDOR[int(r["item"])] = int(r["buy_price"])
        if ah.get("prices_csv") and pathlib.Path(ah["prices_csv"]).exists():
            for r in csv.DictReader(open(ah["prices_csv"], encoding="utf-8")):
                v = r.get("vendor_buy") or ""
                if v.strip().isdigit() and int(v):
                    VENDOR[int(r["item_id"])] = int(v)
        if ah.get("gear_versions_csv") and pathlib.Path(ah["gear_versions_csv"]).exists():   # random-suffix gear listed now
            pool = pool + IP.suffix_versions(cfg["class"], cfg["faction"], cfg["school_share"], ah["gear_versions_csv"])
        for p in pool:   # plain gear listed on the auction house now (random-suffix versions: suffix_versions above)
            if PRICES.listed(p["id"]):
                p["sources"].append({"kind": "auction", "price": PRICES.buy(p["id"])})
        # gear the auction house usually lists although nobody does this hour (the add-on's hourly history, 2026-11-09)
        MARKET.update(MK.history(ah.get("duckdb")))
        byid = {p["id"]: p for p in pool}
        for m in IP.market_versions(cfg["class"], cfg["faction"], cfg["school_share"], MARKET):
            if m["id"] in byid:
                byid[m["id"]]["sources"] += m["sources"]
            else:
                pool.append(m)
                byid[m["id"]] = m
    # what you own already (2026-11-10, user: "Can you see my bags and what I've purchased?"): free and certain, worn at its level
    OWN.update(BG.owned(cfg, snap))
    BOOK.update(BG.spellbook(cfg, snap["profile"]["name"]) or {})   # (2026-11-14: which ranks you know)
    owe = owed_training(cfg, snap["profile"]["level"])
    print(f"spellbook: ForeverTape {BOOK['when']}, {BOOK['n']} spells (level {BOOK['level']}); lacks "
          + (", ".join(rank_label(n, r) for L, n, r, c in owe[0]) or "nothing the build uses") if BOOK else
          "spellbook: none on this PC (ForeverTape 0.9.5 writes it after a /reload or logout): the Train step lists the level's ranks")
    # a spellbook from a lower level than Blizzard's data (2026-11-21: Arcea's was level 38 of 2026-11-20 06:52 at a level-40 logout
    # the next day, while ForeverTape kept saving the other characters): said up front, so the Train step's list is read as possibly stale
    if BOOK and int(BOOK.get("level") or 0) < int(snap["profile"].get("level") or 0):
        # the add-on's file saved after the record (a /reload, a logout) without the record: its recording is broken, not just unsaved
        # (2026-11-21: ForeverTape.lua saved at 20:31 after a /reload, every character's spellbook and bag record still of 11-20 or older)
        saved = max((pathlib.Path(f).stat().st_mtime for f in BG.saved_files(cfg)), default=0)
        tail = (f" ForeverTape saved its file at {datetime.datetime.fromtimestamp(saved).strftime('%Y-%m-%d %H:%M')} without updating it: its "
                "spellbook and bag recording is not working, so until it is fixed the Train step may list ranks you already have and the gold "
                "is that day's." if saved > BOOK["t"] + 3600 else
                " A /reload in game writes it again; until then the Train step may list ranks you already have.")
        NOTICES.append(f"Your spellbook add-on's record is from {BOOK['when']} at level {BOOK['level']}, older than Blizzard's level "
                       f"{snap['profile']['level']}." + tail)
    have = {(p.get("name") or "").lower() for p in pool}
    db = IP.sim_db()
    byname = {it["name"].lower(): it for it in db["items"]}
    sufs = sorted(db.get("randomSuffixes") or [], key=lambda x: sum(x.get("stats") or []))
    for key, o in OWN.items():   # a random-suffix piece you own that no listing put in the pool (you bought the listing): built from the
        nm = o.get("name") or ""    # item and the suffix its name ends with
        if key.startswith("id:") or key in have or " of " not in nm:
            continue
        sx = base = None
        if o.get("suffix") and o.get("id"):   # the add-on's own suffix id (ForeverTape 0.9.3)
            base = next((it for it in db["items"] if it["id"] == o["id"]), None)
            sx = next((x for x in sufs if x["id"] == o["suffix"]), None)
            base = base if sx else None
        for x in ([] if base else sufs):   # else the suffix the item can roll (its randomSuffixOptions) whose name ends the item's name
            b = byname.get(nm[: -len(x["name"]) - 1].lower()) if nm.lower().endswith(" " + x["name"].lower()) else None
            if b and x["id"] in (b.get("randomSuffixOptions") or []):
                sx, base = x, b
                break
        if base:
            built = IP.versions(cfg["class"], cfg["faction"], cfg["school_share"], [(base["id"], f"b{sx['id']}", nm, {"kind": "bags", "price": 0})])
            pool += built
            have |= {nm.lower()} if built else set()
            continue
        for x in sufs:   # the item is gone from the current database (ff9babba5 dropped Geomancer's Bracers): the pin before's item
            if not nm.lower().endswith(" " + x["name"].lower()):
                continue
            old = IP.older_item(nm[: -len(x["name"]) - 1])
            if not old or x["id"] not in (old[0].get("randomSuffixOptions") or []):
                continue
            it, osufs, commit = old
            slot = IP.SLOTS.get(it.get("type"))
            if it.get("type") == 13:
                slot = {4: "two-hand", 3: "off-hand"}.get(it.get("handType"), "main-hand")
            pool.append({"id": f"{it['id']}:b{x['id']}", "name": nm, "slot": slot, "quality": it.get("quality"), "req": it.get("reqLvl") or 0,
                         "stats": IP.suffix_stats(it, [x["id"]], osufs, cfg["school_share"]), "unique": False, "set": None,
                         "sources": [{"kind": "bags", "price": 0, "older_db": commit}]})
            have.add(nm.lower())
            break
    for p in pool:
        o = OWN.get((p.get("name") or "").lower()) or OWN.get(f"id:{p.get('id')}")
        if o:
            p["sources"] = [{"kind": "bags", "where": o["where"], "when": o["when"]}]
    CTX["owned"] = {k: v["count"] for k, v in OWN.items()}
    CTX["owned_when"] = {k: v["when"] for k, v in OWN.items()}
    COMPLETED.update(q["id"] for q in (snap.get("quests-completed") or {}).get("quests") or [])
    RECIPES[:] = PF.known_recipes(snap["profile"]["name"], ah.get("duckdb"), d / "recipes.json")
    FRECIPES.update(PF.forever_recipes([k for k in profs if k in PF.PROFESSION_ID], cfg.get("region", "us")))
    for p in pool:   # a craft Classic's data lacks (Forever's own recipes): the skill where the client table turns it yellow
        for s in p["sources"]:
            if s["kind"] == "craft" and not s.get("skill") and s.get("spell") in FRECIPES:
                s["skill"] = FRECIPES[s["spell"]]["yellow"]
                s["learn"] = s.get("learn") or "a Forever recipe: where it is taught is not in the data yet"
    KNOWN.update(r["spell"] for r in RECIPES)
    INLOG.update(q["id"] for q in (snap.get("quests") or {}).get("in_progress") or [])
    global GEAR_SHARE
    GEAR_SHARE = float(cfg.get("gear_share", GEAR_SHARE))
    # the plan within the gear budget: a buy or craft the budget cannot pay leaves the pool and the plan is made again (another item, or
    # a cheaper one, takes the slot), until every bought upgrade fits
    # the plan you can count on: quests, crafts and buys (2026-11-09, user: "We're factoring in how obtainable an item is right? Like drop
    # rates and stuff if it's within a dungeon?"). Dungeon drops stay out of it and are listed apart, each against what this plan has you
    # wear then, with its drop chance and what a run is worth; a plan built on drops had dropped the auction and quest items it needed as
    # its fallbacks from the buy list and the budget.
    # gear a profession has to wear (Spellpower Goggles Xtreme: Engineering 215, 2026-11-09): only with that profession at that rank
    # (Classic's item data; the simulator's database does not say)
    line_of = {"Engineering": 202, "Tailoring": 197, "Enchanting": 333, "Leatherworking": 165, "Blacksmithing": 164, "Alchemy": 171,
               "Mining": 186, "Herbalism": 182, "Skinning": 393, "Cooking": 185, "First Aid": 129, "Fishing": 356}
    have = {line_of[k]: v[0] for k, v in profs.items() if k in line_of}
    needs = {int(r["item"]): (int(r["required_skill"] or 0), int(r["required_rank"] or 0))
             for r in csv.DictReader(open(IP.RAW / "item_names.csv", encoding="utf-8")) if r["required_skill"] not in ("", "0")}
    pool = [p for p in pool if not (lambda n: n and have.get(n[0], 0) < n[1])(needs.get(int(str(p["id"]).split(":")[0])))]
    FULL_BY_ID.update({p["id"]: p for p in pool})
    if wrec.get("place"):   # the add-on's values: place the character by its worn items (2026-11-13)
        if wrec["place"](equipped(snap, FULL_BY_ID)) is not None:
            print(f"stat values placed by the worn items: {100 * wrec['share']:.0f}% of the way to the level's best Forever set "
                  f"(by {wrec['unit']} alone: {100 * wrec['share_by_unit']:.0f}%)")
        wrec.pop("place")
    SCHOOL_SHARE.update(cfg["school_share"])
    global ROUTE, RG
    wow = cfg.get("wow_dir") or str((cfg.get("ah") or {}).get("ahcopy", "")).split("/Interface/")[0]
    ROUTE = rxp.route(wow, f"{snap['profile']['name']}-{snap['profile'].get('surname', '')}".strip("-")) if wow else None
    RG = RXG.facts(cfg, snap, wow, ROUTE) if ROUTE else None
    if ROUTE and not RG:   # the add-on follows a guide group, but no readable guide text for it is on this PC (2026-11-13)
        msg = (f"RestedXP has a guide selected, but no readable guide text for it was found (in {cfg.get('rxp_dir') or 'F:/wow-addons'} or "
               "the add-on's own guides), so this refresh has no route steps, detours or catch-up, and the plan's quests are marked Unknown on "
               "the route rather than off it. Put the readable guide files back and refresh again.")
        print("WARNING: " + msg)
        NOTICES.append(msg)
    elif RG:   # is the guide text on this PC the route the add-on runs? (rxp_guide.check: the add-on's own step id, 2026-11-13)
        tr = RG["trust"]
        c, part = tr["current"], (ROUTE["sections"] or [{}])[0]
        if c.get("step"):
            print(f"RestedXP check: the add-on's current step is step {c.get('window')} of its {part.get('lo')}-{part.get('hi')} part "
                  + ("(its step id matches the guide text" if c.get("by_id") else "(by its saved step number; no step id matched")
                  + f", guide version {c.get('version')} of {c.get('versions')})")
            ROUTE_NOTE[0] = (f"Checked against your RestedXP add-on: you are on step {c.get('window')} of its {part.get('lo')}-{part.get('hi')} "
                             "part" + ("; the add-on's own step id matches the guide text on this PC." if c.get("by_id") else
                                       " (by the add-on's saved step number: no step id to check it against)."))
        for p in tr["problems"]:
            print("WARNING: RestedXP check: " + p)
        if tr["problems"]:
            NOTICES.append("Your RestedXP guide and the guide text on this PC do not fully match: " + "; ".join(tr["problems"])
                           + ". Quests whose place on the route cannot be confirmed are marked Unknown"
                           + ("; detours and catch-up are off until they match" if tr["mismatch"] else "") + ".")
        if tr["mismatch"]:   # catch-up counts from your position in the guide: off until the text matches
            RG["before"] = {}
        # your quest log and completed quests are Blizzard's, as of the last logout it has seen; the guide's position is the add-on's
        # last save: when that is newer, the quests the guide had you pick up since look missing (2026-11-14: Blizzard at 09:33, the
        # guide 30 steps on at 17:47, and catch-up listed The Howling Vale at the step that hands it in): off until a logout is seen
        seen = (snap["profile"].get("last_login_timestamp") or 0) / 1000
        cf = rxp.files(wow, f"{snap['profile']['name']}-{snap['profile'].get('surname', '')}".strip("-"))[1]
        if RG["before"] and seen and cf and cf.stat().st_mtime > seen + 120:
            RG["before"] = {}
            when = datetime.datetime.fromtimestamp(seen).strftime("%Y-%m-%d %H:%M")
            print(f"catch-up off: Blizzard's quests are from {when}, the guide's position from "
                  f"{datetime.datetime.fromtimestamp(cf.stat().st_mtime).strftime('%Y-%m-%d %H:%M')}")
            NOTICES.append(f"Catch up with your guide is off for this refresh: your quest log is Blizzard's from your logout at {when}, older "
                           f"than your guide's position (saved {datetime.datetime.fromtimestamp(cf.stat().st_mtime).strftime('%Y-%m-%d %H:%M')}), "
                           "so it cannot tell which quests you picked up since. Log out once and refresh.")
    if RG:   # a quest reward on the route comes when the route turns the quest in (item_pool.window: route_level), 2026-11-10
        for p in pool:
            for s in p["sources"]:
                f = RG["quests"].get(s.get("quest")) if s["kind"] == "quest" else None
                if f and f.get("turnin"):
                    s["route_level"] = f["turnin"]["level"]
    # a quest whose target, item or giver is only in a dungeon is done in that dungeon's run: its reward comes no earlier than the level
    # the guide runs it (else two above the dungeon's lowest level). 2026-11-14: Talvash's Enhancing Necklace was planned at 41 while
    # "Restoring the Necklace" needs Uldaman, which the guide runs at 46 (item_pool.window: dungeon_level).
    load_dq()
    chain_step(0)
    dmap = {q: m for m, qs in DQ.items() for q in qs}

    def chain_dungeon(q):   # the dungeon of the quest or of an earlier part you have not done (the reward quest 2361 follows 2204,
        seen = set()        # Uldaman's "Restoring the Necklace")
        while q and q not in seen and q not in COMPLETED:
            seen.add(q)
            if q in dmap:
                return dmap[q]
            q = (QCHAIN.get(q) or (0,))[0]
        return None
    for p in pool:
        for s in p["sources"]:
            m = chain_dungeon(s.get("quest")) if s["kind"] == "quest" and isinstance(s.get("quest"), int) and not s.get("route_level") else None
            if m is not None:
                dn, dlo = (IP.DUNGEONS.get(IP.MAP_TO_ZONE.get(m)) or (None, 0))[:2]
                if dn:
                    gl = ((RG or {}).get("dungeons", {}).get(dn) or {}).get("level")
                    s["dungeon"], s["dungeon_level"] = dn, gl or dlo + 2
    sure_pool = [dict(p, sources=[s for s in p["sources"] if s["kind"] != "dungeon"]) for p in pool]
    sure_pool = [p for p in sure_pool if p["sources"]]
    out = set()
    for _ in range(8):
        eq, events = plan(cfg, snap, at, [p for p in sure_pool if p["id"] not in out], profs)
        drop = budget_walk(events, cfg, at, snap["profile"]["level"])
        if not drop:
            break
        out |= drop
    pool = [p for p in pool if p["id"] not in out]
    sure_pool = [p for p in sure_pool if p["id"] not in out]
    _, full = plan(cfg, snap, at, pool, profs)
    BONUS[:] = bonus_drops(full, events, eq, at)
    sched = dungeon_schedule(cfg, lv0, dungeon_runs(BONUS), events)
    for e in events:   # a buy a dungeon drop beats soon: run the dungeon first, buy only if it does not drop
        if not price_of(e):
            continue
        for b in BONUS:
            zones = {s["zone"] for s in new_sources(b) if s["kind"] == "dungeon"}
            run = min((r["run"] for r in sched if r["zone"] in zones), default=None)
            if (b["slot"] == e["slot"] and run is not None and max(e["get_at"], lv0) - 1 <= run <= e["level"] + 2
                    and b["level"] <= run + 1 and b["over"] == upgrade_name(e)[0].split(" (with")[0]):
                ch = max((s.get("chance") or 0.25) for s in new_sources(b) if s["kind"] == "dungeon")
                e["wait"] = (f"Run {' or '.join(sorted(zones))} first (level {run}): {upgrade_name(b)[0]} ({ch:.0%} drop) beats it; "
                             "buy this only if it does not drop")
                break
    if RG:   # the route step by step (2026-11-10): on it, when it turns the quest in; off it, who gives it and where
        for e in events:
            s0 = primary(e)
            if s0["kind"] == "quest" and isinstance(s0.get("quest"), int):
                f = RG["quests"].get(s0["quest"])
                if f and f.get("turnin"):
                    t = f["turnin"]
                    e["on_route"] = f"Your RestedXP route turns it in at about level {t['level']}" + (f" in {t['zone']}" if t["zone"] else "")
                elif route_unknown(e, lv0):
                    g = giver_text(s0["quest"])
                    e["route_unknown"] = (f"Unknown whether your RestedXP route takes it ({route_unknown(e, lv0)})"
                                          + (f": from {g}" if g else ""))
                else:
                    chain_step(0)
                    prev, seen = s0["quest"], set()   # the route may take the chain's start and leave the rest to you
                    while prev in QCHAIN and QCHAIN[prev][0] and prev not in seen:
                        seen.add(prev)
                        prev = QCHAIN[prev][0]
                        if "accept" in (RG["quests"].get(prev) or {}):
                            break
                    took = (RG["quests"].get(prev) or {}).get("accept") if prev != s0["quest"] else None
                    g = giver_text(s0["quest"])
                    e["off_route"] = ("Not on your RestedXP route" + (f" (it takes the chain as far as \"{(CQUESTS.get(prev) or {}).get('title', prev)}\", "
                                                                      f"at about level {took['level']})" if took else "")
                                      + ": " + (f"from {g}" if g else f"a detour to {s0.get('zone') or 'its zone'}"))
    elif ROUTE:   # no guide text on this PC: whether the route takes a quest is unknown (2026-11-13; it had said "off your route" by zone)
        for e in events:
            s0 = primary(e)
            if s0["kind"] == "quest":
                e["route_unknown"] = ("Unknown whether your RestedXP route takes it (its guide text is not on this PC)"
                                      + (f": in {s0['zone']}" if s0.get("zone") else ""))
    # a craft from a recipe you do not know yet may not happen: the same plan without such crafts names what to wear instead
    unsure = lambda s: s["kind"] == "craft" and s.get("spell") not in KNOWN
    nod = [dict(p, sources=[s for s in p["sources"] if not unsure(s)]) for p in sure_pool]
    _, alt = plan(cfg, snap, at, [p for p in nod if p["sources"]], profs)
    for e in events:
        if new_sources(e) and all(unsure(s) for s in new_sources(e)):
            e["unsure"] = "craft"
            have = {(x or {}).get("id") for x in e["prev"]} - {None}
            cover = [x for x in alt if x["slot"] == e["slot"] and x["level"] < (e["until"] or 60) and x["item"].get("id") not in have]
            before = [x for x in cover if x["level"] <= e["level"]]
            fb = before[-1] if before else (cover[0] if cover else None)
            if fb:   # its gain against what you would still be wearing (the other plan's own chain had its own predecessor)
                wl = at(max(fb["level"], e["level"]))
                g = (value(fb["item"]["stats"], wl) + (value(fb["off"]["stats"], wl) if fb.get("off") else 0.0)
                     - sum(value((x or {}).get("stats"), wl) for x in e["prev"])) / wl["time"]
                fb = dict(fb, gain=g) if g >= UPGRADE else None
            e["fallback"] = fb or {"keep": (e["prev"][0] or {}).get("name")}
    ench = enchants(cfg["school_share"])
    PLAN_EVENTS[:] = events
    if RG and not RG["trust"]["mismatch"]:   # quests off the route worth a detour (2026-11-10); off while the guide text does not match
        kills_per_level(lv0)   # (loads the experience table)
        gear_of = {primary(e)["quest"]: (upgrade_name(e)[0], minutes_saved(e, at)) for e in events
                   if primary(e)["kind"] == "quest" and isinstance(primary(e).get("quest"), int)}
        DETOURS["list"], DETOURS["stats"] = DT.find(
            cfg, snap, lv0, RG, pace=lambda L: XP[L] / max(0.1, minutes_per_level(L, at)), tpk=lambda L: at(L)["time"],
            completed=COMPLETED, inlog=INLOG, maps=RXG.bounds(), group=cfg.get("group", cfg.get("metric") == "tank"), gear_of=gear_of)
    write_page(cfg, d, snap, fetched, at, eq, events, ench, profs, wfile)
    import checklist   # the town checklist page (2026-11-09, user: "an easy to look at almost to-do list of every time I'm in a city")
    checklist.write(cfg, d, CTX)
    if not a.no_refresh:   # the plan this refresh made, for the next refresh's change list (the one before kept for reruns)
        if (d / "state.json").exists():
            (d / "state.prev.json").write_text((d / "state.json").read_text(encoding="utf-8"), encoding="utf-8")
        (d / "state.json").write_text(json.dumps(plan_state(events, lv0, fetched), indent=1) + "\n", encoding="utf-8")
    print(f"wrote {d / 'README.md'}: {len(events)} upgrades to 60")


if __name__ == "__main__":
    main()
