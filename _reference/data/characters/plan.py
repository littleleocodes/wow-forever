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
TEXT_STAT = {"intellect": "intellect", "stamina": "stamina", "spirit": "spirit", "strength": "strength", "agility": "agility",
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
    parts = ("profile", "equipment", "professions", "specializations", "quests", "quests-completed", "reputations")
    return {p: json.loads((arm / f"{p}.json").read_text(encoding="utf-8")) for p in parts
            if (arm / f"{p}.json").exists()}, (arm / "fetched.txt").read_text(encoding="utf-8").strip()


def weights(cls, rot):
    w = json.load(open(HERE / "weights" / f"{cls}-{rot}.json", encoding="utf-8"))
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


def reagents_of(spell):
    """[(name, count, item id)] of a craft spell: Forever's recipe (Blizzard's API) when known, else the Classic one."""
    names = {int(r["item"]): r["name"] for r in csv.DictReader(open(IP.RAW / "item_names.csv", encoding="utf-8"))}
    if spell in FRECIPES:
        return [(names.get(i, str(i)), n, i) for i, n in FRECIPES[spell]["reagents"]]
    for r in csv.DictReader(open(IP.RAW / "craft_spells.csv", encoding="utf-8")):
        if int(r["spell"]) == spell:
            return [(names.get(int(x.split(":")[0]), x.split(":")[0]), int(x.split(":")[1]), int(x.split(":")[0]))
                    for x in r["reagents"].split(";") if x]
    return []


PRICES = None     # ah_prices.Prices of the character's auction house (character.json "ah"), or None
VENDOR = {}       # vendor price of vendor-sold reagents (thread, dye, vials), copper
RECIPES = []        # the recipes the character knows (professions.known_recipes)
KNOWN = set()       # their spell ids
COMPLETED = set()   # quest ids the character has completed (Blizzard's API): their rewards are gone
INLOG = set()       # quest ids in the character's quest log now


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
                log += (f"; the chain starts with \"{row.get('title', st[0])}\"" + (f" from {st[1]}" if st[1] else "")
                        + (f", level {row['min_level']}" if row.get("min_level") not in (None, "", "0") else ""))
            elif st and st[1] and s.get("quest") not in INLOG:
                log += f"; from {st[1]}"
            out.append(f"quest \"{s['name']}\" ({s.get('zone') or '?'}{lv}{log})")
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
                need = (f"turns yellow at {s['skill']} in the client's data" if (s.get("learn") or "").startswith("a Forever recipe")
                        else f"Classic asked skill {s['skill'] if s.get('skill') else '?'}, Forever often less")
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
BONUS = []                # dungeon drops worth chasing on top of the sure plan (bonus_drops)
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
    if GOLD is None:
        return set()
    train, need = training_by_level(cfg["class"]), needed_spells(cfg)
    tr = lambda L: sum(c for n, c in train.get(L, []) if n in need)
    budget = max(0.0, GOLD - tr(lv + 1) - tr(lv + 2))
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


def dungeon_lines(sched):
    o = []
    for r in sched:
        o += [f"- **{r['zone']}** ({r['lo']}-{r['hi']}), run at level {r['run']}"
              + (f"; its drops are worth about {r['worth']} min on average" if r["worth"] else "") + ":"]
        if r["quests"]:
            o += ["  - Quests: " + "; ".join(f"{q['title']} ({q['level']}{', in your log' if q['log'] else ''}"
                                               f"{', ' + q['start'] if q['start'] else ''}{', grey for you by then' if q['grey'] else ''})"
                                               for q in r["quests"])]
        o += [f"  - Drop: {x}" for x in r["drops"]]
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
                         f"{ch:.0%} drop{', chance unknown' if not any(x.get('chance') for x in ss) else ''}"
                         + (f"; the other half drops in {oz}, {op:.0%}" if oz else "")
                         + f"): over your {e['over']}, {pct(e['bonus_gain'])} faster, about {e['bonus_minutes']:.0f} min saved "
                         + ("with both halves" if oz else "if it drops"))
        out.append({"zone": z, "lo": lo, "hi": hi, "worth": round(worth), "own": worth >= MIN_MINUTES, "items": items,
                    "first": min(e["level"] for e, _ in merged.values())})
    return out


DQ = {}


def dungeon_schedule(cfg, lv, runs):
    """Every leveling dungeon you have not outgrown, once (2026-11-09, user: "Make sure dungeons are not being skipped, because dungeons
    are so worth to run at least once. The XP from the dungeon quests is significant, and I can collect the quest and then run the dungeon
    once"): the level to run it (the middle of its quests you have not done, inside its range, not below yours), its quests with where
    each starts (dungeon_quests.csv: a quest whose target, item or giver exists only in that dungeon), and its drops worth hoping for
    (`runs`, dungeon_runs). A dungeon whose quests are all five or more levels below you and that drops nothing for you is left out."""
    if not DQ:
        for r in csv.DictReader(open(IP.RAW / "dungeon_quests.csv", encoding="utf-8")):
            DQ.setdefault(int(r["map"]), []).append(int(r["quest"]))
    chain_step(0)   # (loads the quest tables)
    race_mask = 77 if cfg["faction"] == "alliance" else 178
    cls_bit = 1 << (IP.CLASS_ID[cfg["class"]] - 1)
    drops = {r["zone"]: r for r in runs}
    out = []
    for m, zid in IP.MAP_TO_ZONE.items():
        if zid not in IP.DUNGEONS:
            continue
        name, lo, hi, side = IP.DUNGEONS[zid]
        if (side and side != cfg["faction"]) or hi < lv:
            continue
        qs = {}
        for q in DQ.get(m, []):
            r = CQUESTS.get(q)
            if not r:
                continue
            rr, rc, ql = int(r["required_races"] or 0), int(r["required_classes"] or 0), int(r["quest_level"] or 0)
            if (rr and not rr & race_mask) or (rc and not rc & cls_bit) or ql >= 60 or ql < lo - 10 or q in COMPLETED:
                continue   # (a quest far below the dungeon is a data quirk: Rocknot's Ale reads level 1)
            qs.setdefault(r["title"], (q, ql))
        levels = sorted(v[1] for v in qs.values() if v[1] > 0)
        run = levels[len(levels) // 2] if levels else (lo + hi) // 2
        dr = drops.get(name)
        if dr:   # a drop you would wear early pulls the run forward (Scarlet Monastery's one Alliance quest is level 40, its Library drop 32)
            run = min(run, dr["first"] + 1)
        run = max(lv, lo + 2, min(run, hi - 2))
        quests = []
        for title, (q, ql) in sorted(qs.items(), key=lambda kv: kv[1][1]):
            st = chain_step(q)
            start = ""
            if st and st[0] != q and st[0] not in INLOG:
                first = (CQUESTS.get(st[0]) or {}).get("title", st[0])
                start = (f"start with part 1" if first == title else f"start with \"{first}\"") + (f" from {st[1]}" if st[1] else "")
            elif st and st[1]:
                start = f"from {st[1]}"
            quests.append({"title": title, "level": ql, "start": start, "grey": ql < run - 5, "log": q in INLOG})
        if not dr and not any(not x["grey"] for x in quests):
            continue
        out.append({"zone": name, "lo": lo, "hi": hi, "run": run, "quests": quests, "drops": (dr or {}).get("items", []),
                    "worth": (dr or {}).get("worth", 0)})
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
            why = f"only {pct(g)} faster"
        elif certainty(evs[c], held(k)) < 1 and m >= MIN_MINUTES:
            why = f"{pct(g)} faster, but a dungeon drop ({certainty(evs[c], held(k)):.0%} in your run): a surer upgrade saves more on average"
        elif m < MIN_MINUTES:
            why = f"{pct(g)} faster, saves about {m:.0f} min before {'60' if not nxt else 'its next upgrade'}"
        elif price and m < earn:
            why = f"{pct(g)} faster, saves about {m:.0f} min, but its {AH.money(price)} takes about {earn:.0f} min of play to earn"
        else:
            why = f"{pct(g)} faster, but a later upgrade of the slot saves more without it"
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
def talents_check(cfg, snap, level):
    sys.path.insert(0, str(DATA))
    import level_guides as LG
    import run as FR
    b, order, prov, rot = LG.pick(cfg["class"], cfg["spec"])
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
    path = [(level + 1 + i, n) for i, n in enumerate(queue[:free])]
    return b, rot, rows, sum(have.values()), sum(want.values()), path, queue[free:]


def pct(x):
    return f"{x * 100:.1f}%"


def write_page(cfg, d, snap, fetched, at, eq, events, ench, profs, wfile):
    lv = snap["profile"]["level"]
    name = f"{snap['profile']['name']} {snap['profile'].get('surname', '')}".strip()
    b, rot, tdiff, have_n, want_n, tpath, tdrop = talents_check(cfg, snap, lv)
    o = [f"# {name}", "",
         f"> Generated by `_reference/data/characters/plan.py {cfg['name']}` from Blizzard's character API (fetched {fetched}). Do not hand-edit:",
         "> refresh with the same command. Item values are seconds per kill from this project's fight lab for the leveling page build",
         f"> ([{cfg['spec']}](../../{cfg['class']}/leveling/{cfg['page']}.md), rotation `{rot}`), a model of the beta, not a measurement.", ""]
    race, cls = snap["profile"]["race"]["name"], snap["profile"]["character_class"]["name"]
    o += [f"Level **{lv}** {race} {cls}, {snap['profile']['faction']['name']}. Professions: " +
          ", ".join(f"{k} {v[0]}/{v[1]}" for k, v in profs.items()) + "." +
          (f" Gold: **{AH.money(GOLD)}**." if GOLD is not None else " Gold: unknown (log in with bnet_login.py; the login lasts a day)."), ""]
    # talents
    o += ["## Talents", ""]
    if not tdiff:
        o += [f"Your {have_n} talent points match the page's order at level {lv}.", ""]
    else:
        o += [f"Against the page's order at level {lv} ({want_n} points; you have {have_n} spent):", "", "| Talent | Yours | The page |", "|---|---|---|"]
        o += [f"| {n} | {h} | {w} |" for n, h, w in tdiff] + [""]
        o += ["Your next talents (the page's order from where you are): " + ", ".join(f"{L} {n}" for L, n in tpath[:6]) + "."]
        if tdrop:
            o += [f"You stay one point off the page's order; at 60 you go without its last point ({', '.join(tdrop)}), which measures "
                  "least of its talents."]
        o += [""]
    o += [f"- {x}" for x in cfg.get("talent_notes", [])] + ([""] if cfg.get("talent_notes") else [])
    CTX.update({"head": {"name": name, "level": lv, "race": race, "class": cls, "gold": GOLD, "fetched": fetched,
                         "faction": snap["profile"]["faction"]["name"], "professions": {k: list(v) for k, v in profs.items()},
                         "ah_age": PRICES.age_hours() if PRICES else None, "spec": cfg["spec"], "page": cfg["page"]},
                "talents": {"diff": tdiff, "path": tpath[:6], "drop": tdrop, "have": have_n, "want": want_n}})
    o += change_lines(d, events, lv)
    # now: the upgrades to go after at this level or within LOOKAHEAD levels, by what you do for them
    wl = at(lv)
    soon = [e for e in events if max(e["get_at"], lv) <= lv + LOOKAHEAD]
    global SPENDABLE
    gs, SPENDABLE = gold_plan(cfg, snap, at, lv)
    o += gs
    o += [f"## Now (level {lv})", "",
          f"Everything below is worth doing at your level or within {LOOKAHEAD} levels: items you can wear now, and items you can get now "
          "and wear a level or two later. Percentages are how much faster you kill a mob of your level once the item replaces what you "
          "wear (fight lab).", ""]
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
    o += ["### Enchant", ""] + (enchant_lines(worn, ench, profs, wl, at, lv) or ["- Nothing worth 0.1% faster kills at your Enchanting skill."]) + [""]
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
    sched = dungeon_schedule(cfg, lv, runs)
    CTX["dungeons"] = sched
    near = [r for r in sched if r["run"] <= lv + LOOKAHEAD]
    if near:
        o += ["### Dungeon runs", "", "Run each once, with its quests in your log first: the quests' experience is the main reward. A drop that "
              "beats what the plan has you wear is a bonus; the plan works without it.", ""]
        o += dungeon_lines(near)
    o += ["### Talents and the rest", "", "- Talents: see above. Food, drink, bandages: the [by-level guide](../../" +
          f"{cfg['class']}/leveling/{cfg['page']}-by-level.md) for your rotation.", ""]
    o += profession_section(profs)
    # current gear
    o += ["## Your gear", "", "| Slot | Item | Worth at your level | Replaced at |", "|---|---|---|---|"]
    first = {}
    for e in events:
        first.setdefault(e["slot"], e)
    for slot in SLOT_ORDER:
        it = eq.get("main-hand") if slot == "weapon" else eq.get(slot)
        rep = first.get(slot)
        if not it:
            o += [f"| {slot} | **empty** | 0 | {('level ' + str(rep['level']) + ': ' + rep['item']['name']) if rep else 'nothing worth 0.5% before 60'} |"]
            continue
        v = value(it["stats"], wl) + value(it["enchant_stats"], wl)
        o += [f"| {slot} | {it['name']}{' (' + ', '.join(it['enchant']) + ')' if it['enchant'] else ''} | {pct(v / wl['time'])} faster kills | "
              f"{('level ' + str(rep['level']) + ': ' + rep['item']['name']) if rep else 'not before 60 by 0.5%'} |"]
    o += [""]
    # level by level: by the level you act (the earliest the quest, dungeon or recipe allows); "wear at" when it comes later
    o += ["## Level by level", "", f"Each upgrade worth {UPGRADE:.1%} faster kills or more, under the level at which you can go and get it, "
          "with the level you can wear it when that is later. Dungeon drops carry Classic's drop chance and a fallback if they do not drop; "
          "auction house items on later visits are ones the house usually lists, at their usual price.", ""]
    later = [e for e in events if max(e["get_at"], lv) > lv + LOOKAHEAD]
    for L in range(lv + LOOKAHEAD + 1, LAST + 1):
        ev = [e for e in later if max(e["get_at"], lv) == L]
        if ev:
            o += [f"### Level {L}", ""] + action_sections(ev, at, L, head="####") + [""]
    # every dungeon run, by level
    if sched:
        o += ["## Dungeon runs", "", "Every leveling dungeon you have not outgrown, once, at the level its quests fit: pick the quests up first. "
              "Drops are bonuses over what the plan has you wear: wear one if it drops, the plan goes on as written if not. Drop chances "
              "are Classic's (25% where it has none); \"about N min\" is a drop's minutes of killing saved over the plan's item, and a "
              f"run's drops are worth that times their chances. Minutes assume {KILL_SHARE:.0%} of your experience comes from kills.", ""]
        o += dungeon_lines(sched)
    o += ["## How this is worked out", "",
          f"- Stat values: `_reference/data/characters/weights/{wfile}` (stat_weights.py): the page build in the fight lab at levels 20-60 with each "
          "stat raised, common random numbers; smoothed over neighbouring levels. Spell crit and hit from items, resistances and defense read 0.",
          f"- Minutes saved: at each level an item is worn, the seconds per kill its stats save over what it replaces (stats are worth less as "
          f"you level) x the kills of that level ({KILL_SHARE:.0%} of the level's experience from kills, an estimate), until the plan "
          "replaces it. Quests, travel and dungeon time are not counted. Gear you find or buy that the plan cannot see (world drops, later "
          "auction listings) may replace an item sooner.",
          "- School damage counts by the build's share: " + ", ".join(f"{k} {v:.0%}" for k, v in cfg["school_share"].items()) + " (an estimate).",
          "- Quests Forever added carry no level in Blizzard's data: their zone's level range stands in. Dungeons Forever added: the range of their "
          "drops' required levels. Crafts: the recipe's skill from the Classic database (Forever may differ); a craft counts once your profession "
          "rank allows the skill at that level.",
          f"- An upgrade is listed when it is worth {UPGRADE:.1%} of the time per kill or more over what you would be wearing then, and "
          f"it saves at least {MIN_MINUTES:.0f} minutes of killing before the next upgrade of the slot replaces it, worn at least {MIN_LASTS} levels "
          "(level 60 ends leveling). A smaller or shorter-lived upgrade is left out, and the next one is counted against what you would still "
          "be wearing. Quest rewards you get anyway: wear them when the game shows them as better. Enchants: only when the enchant saves "
          f"{MIN_MINUTES:.0f} minutes before you replace the item.",
          f"- Data: the simulator's WoW: Forever item database at {DATAVER['sim']} ({DATAVER['items']} items; it grows as the game is played, "
          "and a refresh picks the new items up), the CMaNGOS Classic dump at c33f90b8e (recipe skills, quest levels, dungeon loot), Blizzard's "
          f"API for the character (fetched {fetched}) and for Forever's own quests (asked again weekly), stat values measured {DATAVER['weights']} "
          f"for {DATAVER['weights_build']}.",
          "- Raid preparation (items worth keeping for 60) waits for the mage raid lane's gear redo: today's pre-raid set still holds "
          "Naxxramas and Ahn'Qiraj quest rewards (the gear pool fault of 2026-11-05).", ""]
    (d / "README.md").write_text("\n".join(o) + "\n", encoding="utf-8")


PLAY_KILL_SHARE = 0.5   # the share of play time spent killing (the rest: travel, quest turn-ins, looting, vendoring): an estimate
ESSENTIALS = {"mage": {"Arcane Intellect", "Frost Armor", "Ice Armor", "Conjure Water", "Conjure Food", "Frost Nova", "Blink", "Counterspell"}}
MOUNT = {"level": 40, "riding": 200000, "mount": 800000, "discount_rep": "Honored"}   # Classic: riding 20g + mount 80g, 10% off the
                                                                                        # mount at Honored with the race's faction


def training_by_level(cls):
    """{level: [(spell name, cost copper)]} the class trainer teaches (Classic prices, class_training.csv)."""
    out = {}
    for r in csv.DictReader(open(IP.RAW / "class_training.csv", encoding="utf-8")):
        if int(r["class"]) == IP.CLASS_ID[cls] and r["name"]:
            out.setdefault(int(r["level"]), []).append((r["name"], int(r["cost"])))
    return out


def needed_spells(cfg):
    """The spells the character's rotation and kit use: every bold name of its by-level guide, plus the class's essentials (buffs,
    conjures, the escape and control kit); other trainer spells are optional (a frost mage's fire spells, teleports)."""
    g = json.load(open(DATA / "level-guides" / f"{cfg['class']}.json", encoding="utf-8"))
    x = next((x for x in g["guides"] if x["spec"] == cfg["spec"]), {})
    return set(re.findall(r"\*\*([^*]+)\*\*", json.dumps(x))) | ESSENTIALS.get(cfg["class"], set())


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
    need = needed_spells(cfg)
    race = snap["profile"]["race"]["name"]
    reps = {r["faction"]["name"]: r["standing"]["name"] for r in (snap.get("reputations") or {}).get("reputations") or []}
    rep = reps.get(RACE_FACTION.get(race, ""), "Neutral")
    discount = STANDING.index(rep) >= STANDING.index(MOUNT["discount_rep"]) if rep in STANDING else False
    mount = MOUNT["riding"] + MOUNT["mount"] * (0.9 if discount else 1.0)
    rows, saved, mount_at = [], GOLD or 0, None
    gear = {}
    for L, c in PLANNED:
        gear[L] = gear.get(L, 0) + c
    for L in range(lv, 60):
        inc = income_per_level(L, qpl)
        nt = sum(c for n, c in train.get(L + 1, []) if n in need)
        ot = sum(c for n, c in train.get(L + 1, []) if n not in need)
        saved += inc - nt - gear.get(L, 0)
        if L + 1 >= MOUNT["level"] and mount_at is None and saved >= mount:
            mount_at = L + 1
        rows.append((L, inc, nt, ot, [n for n, c in train.get(L + 1, []) if n in need]))
    reserve = sum(r[2] for r in rows[:2])
    spend = None if GOLD is None else max(0, GOLD - reserve)
    opt = {L + 1: [n for n, c in train.get(L + 1, []) if n not in need] for L in range(lv - 1, 60)}
    CTX["training"] = [{"level": lv, "need": [n for n, c in train.get(lv, []) if n in need],
                        "cost": sum(c for n, c in train.get(lv, []) if n in need), "optional": opt.get(lv, []),
                        "optional_cost": sum(c for n, c in train.get(lv, []) if n not in need)}] + \
                      [{"level": L + 1, "need": names, "cost": nt, "optional": opt.get(L + 1, []), "optional_cost": ot}
                       for L, inc, nt, ot, names in rows[:8] if nt or ot]
    by40 = (GOLD or 0) + sum(r[1] - r[2] - gear.get(r[0], 0) for r in rows if r[0] < MOUNT["level"])
    at60 = saved - (mount if mount_at else 0)
    CTX["gold"] = {"gold": GOLD, "reserve": reserve, "spend": spend, "mount": mount, "mount_level": MOUNT["level"], "by40": by40,
                   "mount_at": mount_at, "at60": at60, "gear_share": GEAR_SHARE,
                   "gear_before40": sum(c for L, c in PLANNED if L < MOUNT["level"]),
                   "income": [(r[0], r[1]) for r in rows[:6]]}
    o = ["## Gold plan", "",
         f"Gold now: **{AH.money(GOLD) if GOLD is not None else 'unknown (log in)'}**. Training you need at the next two levels: "
         f"**{AH.money(reserve)}**. Free for gear now: **{AH.money(spend) if spend is not None else 'unknown'}**."
         + (f" You are **{AH.money(reserve - GOLD)} short** of that training: sell your crafts before you buy anything."
            if GOLD is not None and GOLD < reserve else ""), "",
         f"Income is an estimate from Classic's data: coin and loot from about {kills_per_level(lv):.0f} kills a level (cloth, greens and "
         "other trade goods at the auction house's usual sale price after its cut, the rest at vendor prices), plus your pace of "
         f"{qpl:.1f} quests a level at Classic's quest money. It assumes you sell what drops or use it in place of buying it. \"Training\" counts the spells your rotation and kit use; optional ones (a frost mage's fire "
         "spells, teleports) are listed apart.", "",
         "| Level | Income (estimate) | Training you need at the next level | Optional training |", "|---|---|---|---|"]
    for L, inc, nt, ot, names in rows[:LAST - lv + 1][:14]:
        o += [f"| {L} | {AH.money(inc)} | {AH.money(nt) if nt else '-'}{' (' + ', '.join(names) + ')' if names else ''} | "
              f"{AH.money(ot) if ot else '-'} |"]
    o += ["", f"Mount at {MOUNT['level']}: about **{AH.money(mount)}** (Classic prices: riding {AH.money(MOUNT['riding'])} and the mount "
          f"{AH.money(MOUNT['mount'])}{', 10% off at ' + rep + ' with ' + RACE_FACTION.get(race, '') if discount else ''}; Forever's not "
          f"confirmed). At this income you would have about {AH.money(by40)} by {MOUNT['level']} after training and the plan's gear"
          + (f", enough for the mount at {mount_at}." if mount_at else ", not enough by 60 on income alone: auction sales have to make up the rest."),
          "", f"Gear budget: the gold above the next two levels' training now, then {GEAR_SHARE:.0%} of each level's income after training "
          "(character.json \"gear_share\"); the rest saves for the mount and for 60. Every bought or crafted upgrade below fits it. The plan's "
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
    out = f"- **{e['slot']}**: {what}, {pct(e['gain'])} faster kills{rep} ({wear}{until}; saves about {minutes_saved(e, at):.0f} min of killing). {src}."
    if e.get("wait"):
        out += f" {e['wait']}."
    if e.get("passed") and (e["until"] or 60) - e["level"] >= 8:   # a long-held item: why nothing replaces it sooner
        alts = sorted(e["passed"], key=lambda x: -x[2])[:3]
        out += " Why it stays: " + "; ".join(f"{n} at {L}, {why}" for L, n, g, why in sorted(alts)) + "."
    fb = e.get("fallback")
    miss = "If you do not craft it" if e.get("unsure") == "craft" else "If it does not drop"
    if fb and "keep" in fb:
        return out + (f" {miss}, keep your {fb['keep']}." if fb["keep"] else "")
    if fb:
        when = f"from level {fb['level']}" if fb["level"] > e["level"] else "instead"
        out += f" {miss}, wear {fb['item']['name']} {when} ({pct(fb['gain'])} faster kills; {sources_text(fb['item'])})."
    return out


KIND_ORDER = ["dungeon", "quest", "craft", "vendor", "auction", "market"]


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
            verdict = f" Saves about {saves:.0f} min of killing; earning its price takes about {earn:.0f} min of play."
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
    for prof in ("Tailoring", "Enchanting", "Cooking"):
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
    train, need = training_by_level(cfg["class"]), needed_spells(cfg)
    nxt = next((L for L in range(lv + 1, 61) if any(n in need for n, c in train.get(L, []))), lv + 2)
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
        rows.append((CONSUMABLE_KIND[c["type"]], c["name"], st, xp, gain, minutes, how, cost, per_hour))
    import math
    income_min = (income_per_level(level, QPL) / minutes_per_level(level, at)) if at else None   # copper a minute of play
    out = []
    CTX["consumables"] = []
    for kind in ("Weapon oil", "Food", "Elixir", "Scroll"):
        ks = sorted([r for r in rows if r[0] == kind], key=lambda r: -(r[4] + r[3] / 100 * 0.5))[:3]
        scored = []
        for k, name, st, xp, gain, minutes, how, cost, per_hour in ks:
            saved = 60 * (gain * PLAY_KILL_SHARE + xp / 100 * KILL_SHARE)   # play minutes an hour of it saves
            earn = per_hour / income_min if per_hour and income_min else None   # play minutes its hour's cost takes to earn
            qty = math.ceil(trip_min / minutes) if trip_min and minutes else None
            scored.append((k, name, st, xp, gain, minutes, how, cost, per_hour, saved, earn, qty))
        good = [x for x in scored if x[10] is not None and x[9] >= x[10]]
        pick = max(good, key=lambda x: x[9] - x[10])[1] if good else None   # the one that saves the most beyond its price
        for k, name, st, xp, gain, minutes, how, cost, per_hour, saved, earn, qty in scored:
            eff = ", ".join(f"+{v:g} {x.replace('_', ' ')}" for x, v in st.items()) + (f", +{xp}% kill experience" if xp else "")
            worth = earn is not None and saved >= earn
            CTX["consumables"].append({"kind": kind, "item": name, "effect": eff, "pct": pct(gain), "minutes": minutes, "how": how,
                                       "cost": cost, "hour": per_hour, "best": name == (pick or scored[0][1]), "qty": qty,
                                       "total": qty * cost if qty and cost else None, "saved": saved, "earn": earn, "worth": worth})
            buy = f"×{qty} ({AH.money(qty * cost)})" if qty and cost else "?"
            verdict = (f"yes: saves {saved:.1f} min an hour, costs {earn:.1f}" if worth else
                       f"no: saves {saved:.1f} min an hour, costs {earn:.1f}" if earn is not None else "?")
            out.append(f"| {kind} | {name} | {eff} | {pct(gain)} | {minutes or '?'} min | {how} | {AH.money(cost) if cost else 'no price'} | "
                       f"{buy} | {verdict} |")
    if not out:
        return []
    return (["| Kind | Item | Effect | Faster kills | Lasts | How | One costs | For your trip | Earns its price back |",
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
        fbt = f"{fb['item']['name']}, {pct(fb['gain'])} faster ({sources_text(fb['item'])})"
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
            "wait": e.get("wait"),
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
    was = {(s, n): L for s, L, n in old["plan"]}
    now = {(e["slot"], e["item"]["name"]): e["level"] for e in events}
    new = [f"{n} ({s}, level {L})" for (s, n), L in sorted(now.items(), key=lambda kv: kv[1]) if (s, n) not in was]
    gone = [f"{n} ({s})" for (s, n) in was if (s, n) not in now]
    moved = [f"{n} ({s}) level {was[(s, n)]} to {L}" for (s, n), L in now.items() if (s, n) in was and was[(s, n)] != L]
    CTX["changes"] = {"time": old["time"], "level": old["level"], "gold_then": old.get("gold"), "new": new, "gone": gone, "moved": moved}
    o = [f"## Since your last refresh ({old['time']}, level {old['level']})", ""]
    if old.get("gold") is not None and GOLD is not None:
        o += [f"- Gold: {AH.money(old['gold'])} then, {AH.money(GOLD)} now."]
    o += [f"- New in the plan: {', '.join(new)}." if new else "- Nothing new in the plan."]
    if gone:
        o += [f"- Left the plan (worn, replaced by a better choice, or no longer listed): {', '.join(gone)}."]
    if moved:
        o += [f"- Moved: {', '.join(moved)}."]
    return o + [""]


def judge_lines(worn, events, wl, lv, cfg):
    """A quick test for a random drop or an auction find (2026-11-09, user: "random drops, whatever is available"): per slot what the
    item you will wear adds in spell power equivalents (each stat at this level's value over spell power's) and what a find must add on
    top to save MIN_MINUTES before the plan's next upgrade of the slot (and 0.5% faster kills)."""
    sp = wl["w"].get("spell_power") or 0
    if sp <= 0:
        return []
    rate = {k: wl["w"].get(k, 0.0) / sp for k in ("intellect", "spirit", "stamina", "mp5", "armor")}
    sch = ", ".join(f"{k} {v:.0%}" for k, v in cfg["school_share"].items())
    o = ["### Judging a drop or an auction find", "",
         f"Count a piece's stats in spell power: 1 intellect = {rate['intellect']:.2f}, 1 spirit = {rate['spirit']:.2f}, 1 stamina = "
         f"{rate['stamina']:.2f}, 1 mana per 5 sec = {rate['mp5']:.2f}, 100 armor = {100 * rate['armor']:.2f}; school damage counts by your "
         f"build's share ({sch}: +10 frost damage counts {10 * cfg['school_share'].get('frost', 0):.1f}), \"spell damage and healing\" in "
         "full. A find is worth wearing when it reaches the number below: enough to save "
         f"{MIN_MINUTES:.0f} minutes before the plan's next upgrade of the slot.", "",
         "| Slot | You wear (or the plan's next piece) | Worth (spell power) | A find must reach | Next planned upgrade |", "|---|---|---|---|---|"]
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
    CTX["rates"] = {k: round(v, 2) for k, v in rate.items()}
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
                out.append(f"- {who}: skip, {now['name']} saves only about {minutes_saved(life, at):.0f} min of killing before you replace it"
                           + (f" at level {it['until']}." if it.get("until") else "."))
                continue
        if now and (nv - have) / wl["time"] >= 0.001:
            txt.append(f"{now['name']} (Enchanting {now['skill']}, {now['learn']}), {pct((nv - have) / wl['time'])} faster kills"
                       + (f" over its {', '.join(it['enchant'])}" if it.get("enchant") else "") + ". Materials: "
                       + mats_text(now["reagents"]) + ".")
        nxt = sorted([e for e in opts if skill < e["skill"] <= skill + 30 and (value(e["stats"], wl) - max(have, nv)) / wl["time"] >= 0.001], key=lambda e: e["skill"])[:1]
        for e in nxt:
            if at and lv and minutes_saved({"gain": (value(e["stats"], wl) - have) / wl["time"], "level": max(lv, it.get("since") or lv),
                                            "until": it.get("until")}, at) < MIN_MINUTES:
                continue   # the same 20-minute bar as the enchant you can make now
            txt.append(f"At Enchanting {e['skill']}: {e['name']} ({e['learn']}), {pct((value(e['stats'], wl) - have) / wl['time'])} faster kills.")
        if txt:
            out.append(f"- {who}: " + " ".join(txt))
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("name")
    ap.add_argument("--no-refresh", action="store_true")
    a = ap.parse_args()
    d = char_dir(a.name)
    cfg = json.load(open(d / "character.json", encoding="utf-8"))
    snap, fetched = snapshot(cfg, d, not a.no_refresh)
    sys.path.insert(0, str(DATA))
    import level_guides as LG
    b, order, prov, rot = LG.pick(cfg["class"], cfg["spec"])
    wfile = f"{cfg['class']}-{rot}.json"
    at, wrec = weights(cfg["class"], rot)
    commit, n_items = IP.sim_version()
    DATAVER.update({"sim": commit, "items": n_items, "weights": wrec.get("date"), "weights_build": wrec.get("build")})
    if wrec.get("build") != b["id"]:
        print(f"WARNING: stat values were measured for {wrec.get('build')}; the page now shows {b['id']}: re-run stat_weights.py")
    pool = IP.pool(cfg["class"], cfg["faction"], cfg["school_share"], cfg.get("region", "us"))
    profs = skills(snap)
    PROFS.update(profs)
    global MIN_LASTS, MIN_MINUTES, PRICES, GOLD
    GOLD = character_gold(cfg)
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
    SCHOOL_SHARE.update(cfg["school_share"])
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
    sched = dungeon_schedule(cfg, lv0, dungeon_runs(BONUS))
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
    write_page(cfg, d, snap, fetched, at, eq, events, ench, profs, wfile)
    import checklist   # the town checklist page (2026-11-09, user: "an easy to look at almost to-do list of every time I'm in a city")
    checklist.write(cfg, d, CTX)
    if not a.no_refresh:   # the plan this refresh made, for the next refresh's change list
        (d / "state.json").write_text(json.dumps(plan_state(events, lv0, fetched), indent=1) + "\n", encoding="utf-8")
    print(f"wrote {d / 'README.md'}: {len(events)} upgrades to 60")


if __name__ == "__main__":
    main()
