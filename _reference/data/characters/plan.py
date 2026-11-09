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
import bnet  # noqa: E402
import item_pool as IP  # noqa: E402

UPGRADE = 0.005        # an upgrade worth less than 0.5% of the time per kill is not listed
MIN_CHANCE = 0.05      # a dungeon drop under 5% is not worth planning around
LAST = 59              # the plan stops at 59: level 60 gear is not leveling gear
ENDGAME = {"Naxxramas", "Ahn'Qiraj", "Ruins of Ahn'Qiraj", "Temple of Ahn'Qiraj", "Gates of Ahn'Qiraj", "Molten Core", "Blackwing Lair",
           "Zul'Gurub", "Onyxia's Lair", "Alterac Valley", "Warsong Gulch", "Arathi Basin"}
LOOKAHEAD = 3          # "a piece of gear that I will use within a couple levels": an item usable this many levels on
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
                (arm / f"{part.strip('/')}.json").write_text(json.dumps(js, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
        (arm / "fetched.txt").write_text(datetime.datetime.now().strftime("%Y-%m-%d %H:%M") + "\n", encoding="utf-8")
    return {p: json.loads((arm / f"{p}.json").read_text(encoding="utf-8")) for p in ("profile", "equipment", "professions", "specializations")
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


def text_stats(lines):
    out = {}
    for t in lines:
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
        reag = [(names.get(int(x.split(":")[0]), x.split(":")[0]), int(x.split(":")[1])) for x in r["reagents"].split(";") if x]
        out.append({"slot": ENCHANT_SLOT[m.group(1)], "name": r["name"], "stats": st, "skill": sk[1], "learn": sk[2], "reagents": reag})
    return out


def reagents_of(spell):
    names = {int(r["item"]): r["name"] for r in csv.DictReader(open(IP.RAW / "item_names.csv", encoding="utf-8"))}
    for r in csv.DictReader(open(IP.RAW / "craft_spells.csv", encoding="utf-8")):
        if int(r["spell"]) == spell:
            return [(names.get(int(x.split(":")[0]), x.split(":")[0]), int(x.split(":")[1])) for x in r["reagents"].split(";") if x]
    return []


# ---------------------------------------------------------------------------------------------------------------- the plan
def sources_text(it):
    out = []
    for s in it["sources"]:
        k = s["kind"]
        if k == "quest":
            lv = f", level {s['level']}" if s.get("level") else ""
            out.append(f"quest \"{s['name']}\" ({s.get('zone') or '?'}{lv})")
        elif k == "dungeon":
            est = ", range estimated" if s.get("estimated") else ""
            ch = f", {s['chance']:.0%} drop" if s.get("chance") else ""
            out.append(f"{s['zone']} ({s['lo']}-{s['hi']}{est}), {s['boss']}{ch}")
        elif k == "drop":
            out.append(f"drop: {s.get('boss') or 'world drop'}{', ' + s['zone'] if s.get('zone') else ''}")
        elif k == "craft":
            have = (PROFS.get(s["profession"]) or (None,))[0]
            gap = "" if have is None or not s.get("skill") else (f"; you have {have}" if have >= s["skill"] else f"; you have {have}, {s['skill'] - have} to go")
            out.append(f"{s['profession']} {s['skill'] if s.get('skill') else '?'} ({s.get('learn') or 'recipe source unknown'}{gap})")
        elif k == "vendor":
            out.append(f"vendor {s.get('npc')} ({s.get('zone')})")
        elif k in ("rep", "quartermaster", "trash") and len(it["sources"]) == 1:
            out.append({"rep": "reputation reward", "quartermaster": f"reputation or PvP vendor {s.get('npc')}", "trash": f"random trash drop in {s.get('zone')}"}[k])
    return "; ".join(out)


PROFS = {}   # the character's professions, {name: (skill, cap)}: main() fills it for the craft lines


def acquirable(it, L, start, profs):
    """The level at which this item can be had at the earliest, from `start` on, if it can be had by level L; None if not."""
    best = None
    if (it.get("quality") or 0) >= 5:   # legendaries are not leveling gear
        return None
    for s in it["sources"]:
        if s["kind"] in ("rep", "drop", "trash", "quartermaster"):
            continue
        if s["kind"] == "dungeon" and s.get("chance") is not None and s["chance"] < MIN_CHANCE:
            continue
        if s["kind"] == "quest" and ((s.get("level") or 0) >= 60 or s.get("zone") in ENDGAME):
            continue
        lo, hi = IP.window(it, s)
        if s["kind"] == "craft":
            have = profs.get(s["profession"])
            if have is None or not s.get("skill") or s["skill"] > skill_cap(L):
                continue
        a = max(lo, start)
        if a <= L and a <= hi:
            best = a if best is None else min(best, a)
    return best


def plan(cfg, snap, at, pool, profs):
    level = snap["profile"]["level"]
    eq = equipped(snap, {p["id"]: p for p in pool})
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
            if slot == "weapon":
                cands = [(value(p["stats"], wl), p, None) for p in by_slot.get("two-hand", []) if p["req"] <= L + LOOKAHEAD]
                mh = [p for p in by_slot.get("main-hand", []) if p["req"] <= L + LOOKAHEAD]
                oh = [p for p in by_slot.get("off-hand", []) if p["req"] <= L + LOOKAHEAD]
                bm = max(mh, key=lambda p: value(p["stats"], wl), default=None)
                bo = max(oh, key=lambda p: value(p["stats"], wl), default=None)
                if bm and bo:
                    cands.append((value(bm["stats"], wl) + value(bo["stats"], wl), bm, bo))
            else:
                cands = [(value(p["stats"], wl), p, None) for p in by_slot.get(slot, []) if p["req"] <= L + LOOKAHEAD]
            best = None
            for v, p, o in sorted(cands, key=lambda x: -x[0]):
                if v - cv < UPGRADE * wl["time"]:
                    break
                if p["id"] in taken or (o and o["id"] in taken):
                    continue
                a = acquirable(p, L, level, profs)
                ao = acquirable(o, L, level, profs) if o else level
                if a is None or ao is None:
                    continue
                if p["req"] > L:   # get it now, equip within LOOKAHEAD levels: only if it would also be the upgrade then
                    if value(p["stats"], at(p["req"])) - cv < UPGRADE * at(p["req"])["time"]:
                        continue
                best = (v, p, o, max(a, ao))
                break
            if best and (best[1]["req"] <= L):
                v, p, o, a = best
                gain = (v - cv) / wl["time"]
                prev = c["item"]
                events.append({"level": L, "get_at": a, "slot": slot, "item": p, "off": o, "gain": gain, "replaces": (prev or {}).get("name"),
                               "lasts_from": L, "prev": [prev, c.get("off")]})
                if slot in held:
                    held[slot]["until"] = L
                held[slot] = events[-1]
                cur[slot] = {"item": {"name": p["name"], "stats": p["stats"], "id": p["id"]}, "off": o, "since": L}
                taken.add(p["id"])
            elif best and best[1]["req"] > L:
                pass
            if c.get("item"):
                taken.add(c["item"].get("id"))
    for e in events:
        e.setdefault("until", None)
    # an upgrade replaced again within a level is not worth the trip (2026-11-09: a quest ring worn for one level): drop it, and the next
    # upgrade of the slot replaces what it replaced, its gain counted against that
    kept = []
    for slot in SLOT_ORDER:
        evs = [e for e in events if e["slot"] == slot]
        i = 0
        while i < len(evs):
            e = evs[i]
            if e["until"] is not None and e["until"] - e["level"] <= 1 and i + 1 < len(evs):
                n = evs[i + 1]
                n["replaces"], n["prev"] = e["replaces"], e["prev"]
                wl = at(n["level"])
                pv = sum(value((x or {}).get("stats"), wl) for x in n["prev"])
                nv = value(n["item"]["stats"], wl) + (value(n["off"]["stats"], wl) if n.get("off") else 0.0)
                n["gain"] = (nv - pv) / wl["time"]
                n["get_at"] = min(n["get_at"], max(n["get_at"], e["level"]))
                evs.pop(i)
                continue
            i += 1
        kept += evs
    return eq, sorted(kept, key=lambda e: (e["level"], SLOT_ORDER.index(e["slot"])))


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
          ", ".join(f"{k} {v[0]}/{v[1]}" for k, v in profs.items()) + ".", ""]
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
    # now: the upgrades to go after at this level or within LOOKAHEAD levels, by what you do for them
    wl = at(lv)
    soon = [e for e in events if max(e["get_at"], lv) <= lv + LOOKAHEAD]
    o += [f"## Now (level {lv})", "",
          f"Everything below is worth doing at your level or within {LOOKAHEAD} levels: items you can wear now, and items you can get now "
          "and wear a level or two later. Percentages are how much faster you kill a mob of your level once the item replaces what you "
          "wear (fight lab).", ""]
    worn = {s: (eq.get("main-hand") if s == "weapon" else eq.get(s)) for s in SLOT_ORDER}
    for e in sorted(soon, key=lambda e: e["level"]):
        worn[e["slot"]] = {"name": e["item"]["name"], "stats": e["item"]["stats"], "enchant": [], "enchant_stats": {},
                           "two_hand": e["item"]["slot"] == "two-hand", "planned": e["level"]}
    o += ["### Enchant", ""] + (enchant_lines(worn, ench, profs, wl) or ["- Nothing worth 0.1% faster kills at your Enchanting skill."]) + [""]
    o += action_sections(soon, at, lv)
    o += ["### Talents and the rest", "", "- Talents: see above. Food, drink, bandages: the [by-level guide](../../" +
          f"{cfg['class']}/leveling/{cfg['page']}-by-level.md) for your rotation.", ""]
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
          "with the level you can wear it when that is later. A dungeon item can drop or not: the data has no drop chances.", ""]
    later = [e for e in events if max(e["get_at"], lv) > lv + LOOKAHEAD]
    for L in range(lv + LOOKAHEAD + 1, LAST + 1):
        ev = [e for e in later if max(e["get_at"], lv) == L]
        if ev:
            o += [f"### Level {L}", ""] + action_sections(ev, at, L, head="####") + [""]
    # dungeons worth running, whole list
    runs = {}
    for e in events:
        for s in e["item"]["sources"]:
            if s["kind"] == "dungeon":
                runs.setdefault((s["zone"], s["lo"], s["hi"]), []).append((s["boss"], e))
    if runs:
        o += ["## Dungeons worth running", "", "Every dungeon with an upgrade in the plan, the boss that drops it, and the level you wear it.", ""]
        for (z, lo, hi), ev in sorted(runs.items(), key=lambda kv: kv[0][1]):
            merged = {}
            for boss, e in ev:   # one line per item: every boss that drops it
                merged.setdefault(id(e), (e, []))[1].append(boss)
            items = ", ".join(f"{e['item']['name']} ({e['slot']}, wear at {e['level']}, {' or '.join(bosses)})" for e, bosses in merged.values())
            o += [f"- **{z}** ({lo}-{hi}): {items}"]
        o += [""]
    o += ["## How this is worked out", "",
          f"- Stat values: `_reference/data/characters/weights/{wfile}` (stat_weights.py): the page build in the fight lab at levels 20-60 with each "
          "stat raised, common random numbers; smoothed over neighbouring levels. Spell crit and hit from items, resistances and defense read 0.",
          "- School damage counts by the build's share: " + ", ".join(f"{k} {v:.0%}" for k, v in cfg["school_share"].items()) + " (an estimate).",
          "- Quests Forever added carry no level in Blizzard's data: their zone's level range stands in. Dungeons Forever added: the range of their "
          "drops' required levels. Crafts: the recipe's skill from the Classic database (Forever may differ); a craft counts once your profession "
          "rank allows the skill at that level.",
          f"- An upgrade is listed when it is worth {UPGRADE:.1%} of the time per kill or more over what you would be wearing then.", ""]
    (d / "README.md").write_text("\n".join(o) + "\n", encoding="utf-8")


def line(e, at):
    p, o = e["item"], e.get("off")
    what = p["name"] + (f" + {o['name']}" if o else "")
    wear = f"wear at {e['level']}" if e["level"] > e["get_at"] else "wear it right away"
    src = sources_text(p) + (f" / {sources_text(o)}" if o else "")
    rep = f", replaces {e['replaces']}" if e.get("replaces") else ""
    until = f"; best until level {e['until']}" if e.get("until") else "; best to the end of leveling"
    return f"- **{e['slot']}**: {what}, {pct(e['gain'])} faster kills{rep} ({wear}{until}). {src}."


KIND_ORDER = ["dungeon", "quest", "craft", "vendor"]


def primary(e):
    """The source to act on: the first acquirable kind in KIND_ORDER."""
    for k in KIND_ORDER:
        for s in e["item"]["sources"]:
            if s["kind"] == k:
                return s
    return e["item"]["sources"][0] if e["item"]["sources"] else {"kind": "?"}


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
            o += [line(e, at) + (" Materials: " + ", ".join(f"{n} x{c}" for n, c in reag) + "." if reag else "")]
        o += [""]
    if by.get("vendor"):
        o += [f"{head} Buy", ""] + [line(e, at) for e in by["vendor"]] + [""]
    return o


def enchant_lines(worn, ench, profs, wl):
    """Per enchantable slot: the best enchant at the character's Enchanting skill for the item it will wear, and the next one a higher
    skill opens; only enchants worth 0.1% faster kills or more."""
    skill = (profs.get("Enchanting") or (0, 0))[0]
    out = []
    for slot in ("wrist", "chest", "back", "hands", "feet", "weapon"):
        it = worn.get(slot)
        if not it:
            continue
        kinds = ["weapon2h", "weapon"] if slot == "weapon" and it.get("two_hand") else (["weapon"] if slot == "weapon" else [slot])
        have = value(it.get("enchant_stats"), wl)
        opts = sorted([e for e in ench if e["slot"] in kinds], key=lambda e: -value(e["stats"], wl))
        now = next((e for e in opts if e["skill"] <= skill), None)
        nv = value(now["stats"], wl) if now else 0.0
        who = f"**{it['name']}** ({slot}{', once you have it at level ' + str(it['planned']) if it.get('planned') else ''})"
        txt = []
        if now and (nv - have) / wl["time"] >= 0.001:
            txt.append(f"{now['name']} (Enchanting {now['skill']}, {now['learn']}), {pct((nv - have) / wl['time'])} faster kills"
                       + (f" over its {', '.join(it['enchant'])}" if it.get("enchant") else "") + ". Materials: "
                       + ", ".join(f"{n} x{c}" for n, c in now["reagents"]) + ".")
        nxt = sorted([e for e in opts if e["skill"] > skill and (value(e["stats"], wl) - max(have, nv)) / wl["time"] >= 0.001], key=lambda e: e["skill"])[:1]
        for e in nxt:
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
    at, _ = weights(cfg["class"], rot)
    pool = IP.pool(cfg["class"], cfg["faction"], cfg["school_share"], cfg.get("region", "us"))
    profs = skills(snap)
    PROFS.update(profs)
    eq, events = plan(cfg, snap, at, pool, profs)
    ench = enchants(cfg["school_share"])
    write_page(cfg, d, snap, fetched, at, eq, events, ench, profs, wfile)
    print(f"wrote {d / 'README.md'}: {len(events)} upgrades to 60")


if __name__ == "__main__":
    main()
