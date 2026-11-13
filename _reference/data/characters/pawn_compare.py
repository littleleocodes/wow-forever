"""Our stat values against Pawn's: the best set each picks from one gear pool, raced in the fight lab (2026-11-13; user: "we should test it
to make sure our understanding of the stats is correct versus Pawn's ratings. So we should compare gear at the same level for a character,
and the gear sets can be picked based on what Pawn thinks is best at that level versus what we think is best and then raced and compared").

    python _reference/data/characters/pawn_compare.py [classes...] [--levels 20,30,40,50,60] [--fights 3000] [--jobs 10] [--write]

Per leveling page pick (weights/leveling/<class>-<build id>.json, stat_weights_all.py) and level:
- the pool: every item of the simulator's Forever database the class can use with a required level from 6 below the level to the level,
  green or blue, no raid, PvP or reputation item; random-suffix items in each of their suffix versions (item_pool.suffix_stats);
- Pawn's set: Pawn 2.14.2's built-in Forever weights (ClassicHawsJon.lua) for the tree with the most points, applied the way Pawn applies
  them (pawn_scales: "+N Spell Power" counted 0, ratings times Classic's per-percent factors, melee and spell ratings merged by the larger,
  no caps): per slot the item with the highest Pawn score (two different rings and trinkets; a two-hander against the best main hand and
  off hand);
- our set: the same pool and rules scored with our seconds-per-kill values, hit and expertise counted only up to what the mob's miss,
  dodge and parry leave after the build's own talents (a swap search on the whole set);
- both raced in the fight lab at that level (common random numbers, seeds 3 and 4): the gear's stats replace the lab's typical gear.
The race uses the fight lab our values come from, so our set has a built-in edge: the race proves the values are applied right (caps,
non-linear effects) and measures what Pawn's picks cost if the fight lab is right, not that the fight lab matches the game.
Record characters/pawn-compare.json, page _reference/pawn-comparison.md (--write).
"""
import argparse
import datetime
import json
import multiprocessing
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
DATA = HERE.parent
ROOT = DATA.parent.parent
sys.path[:0] = [str(DATA / "fightlab"), str(DATA / "scorer"), str(DATA), str(HERE)]
import item_pool as IP  # noqa: E402
import level_guides as LG  # noqa: E402
import run as FR  # noqa: E402
import tables as TB  # noqa: E402
from pawn_scales import (PAWN_CLASS, TREES, pawn_item_stats, pawn_scales, pawn_score, pawn_spec,  # noqa: E402
                         tree_of)

# what each class may equip (Classic rules): armor types (mail and plate from 40), (weapon type, hand) pairs (None: any hand), ranged types
ONE, MAIN, OFF, TWO = 2, 1, 3, 4
AXE, DAGGER, FIST, MACE, HELD, POLE, SHIELD, STAFF, SWORD = 1, 2, 3, 4, 5, 6, 7, 8, 9
BOW, XBOW, GUN, THROWN, WAND, IDOL, LIBRAM, TOTEM = 1, 2, 3, 4, 5, 6, 7, 8
USE = {
    "warrior": ({1, 2, 3}, {4}, {(AXE, None), (DAGGER, None), (FIST, None), (MACE, None), (POLE, TWO), (STAFF, TWO), (SWORD, None), (SHIELD, OFF)},
                {BOW, XBOW, GUN, THROWN}),
    "paladin": ({1, 2, 3}, {4}, {(AXE, None), (MACE, None), (SWORD, None), (POLE, TWO), (SHIELD, OFF), (HELD, OFF)}, {LIBRAM}),
    "hunter": ({1, 2}, {3}, {(AXE, None), (DAGGER, None), (FIST, None), (POLE, TWO), (STAFF, TWO), (SWORD, None)}, {BOW, XBOW, GUN, THROWN}),
    "rogue": ({1, 2}, set(), {(DAGGER, None), (FIST, None), (MACE, MAIN), (MACE, ONE), (MACE, OFF), (SWORD, MAIN), (SWORD, ONE), (SWORD, OFF)},
              {BOW, XBOW, GUN, THROWN}),
    "priest": ({1}, set(), {(DAGGER, None), (MACE, MAIN), (MACE, ONE), (STAFF, TWO), (HELD, OFF)}, {WAND}),
    "shaman": ({1, 2}, {3}, {(AXE, None), (DAGGER, None), (FIST, None), (MACE, None), (STAFF, TWO), (SHIELD, OFF), (HELD, OFF)}, {TOTEM}),
    "mage": ({1}, set(), {(DAGGER, None), (SWORD, MAIN), (SWORD, ONE), (STAFF, TWO), (HELD, OFF)}, {WAND}),
    "warlock": ({1}, set(), {(DAGGER, None), (SWORD, MAIN), (SWORD, ONE), (STAFF, TWO), (HELD, OFF)}, {WAND}),
    "druid": ({1, 2}, set(), {(DAGGER, None), (FIST, None), (MACE, None), (STAFF, TWO), (HELD, OFF)}, {IDOL}),
}
SLOT_OF = {1: "head", 2: "neck", 3: "shoulder", 4: "back", 5: "chest", 6: "wrist", 7: "hands", 8: "waist", 9: "legs", 10: "feet",
           11: "finger", 12: "trinket"}
ARMOR_SLOTS = ["head", "neck", "shoulder", "back", "chest", "wrist", "hands", "waist", "legs", "feet"]
# our gear keys (item_pool.lab_stats) -> the value file's keys
LAB_TO_W = {"hit": "hit_rating", "crit": "crit_rating", "haste": "haste_rating", "expertise": "expertise_rating", "defense": "defense_rating",
            "block": "block_rating", "dodge": "dodge_rating", "parry": "parry_rating"}


# ------------------------------------------------------------------ the pool
def item_pool(cls, level, school_share, faction="alliance"):
    """Item versions a class can wear at `level` from items with a required level from level-6 to level: {"id", "name", "slot", "hand",
    "wtype", "stats" (raw by stat id), "lab" (item_pool.lab_stats keys), "dps", "ranged"}."""
    db = IP.sim_db()
    sufs = {x["id"]: x for x in db.get("randomSuffixes") or []}
    light, heavy, weapons, ranged = USE[cls]
    armor_ok = light | (heavy if level >= 40 else set())
    out = []
    for it in db["items"]:
        req = it.get("reqLvl") or 0
        if not (level - 6 <= req <= level) or it.get("quality", 2) not in (2, 3):
            continue
        if it.get("classAllowlist") and IP.CLASS_ID[cls] not in it["classAllowlist"]:
            continue
        if it.get("factionRestriction") and it["factionRestriction"] != IP.FACTION_ID[faction]:
            continue
        srcs = {list(s)[0] for s in it.get("sources") or []}
        if srcs & {"pvp", "rep"} or any("drop" in s and (s["drop"].get("zoneId") in IP.RAIDS) for s in it.get("sources") or []):
            continue
        t = it.get("type")
        if t in SLOT_OF:
            if it.get("armorType") not in (None, 0) and it["armorType"] not in armor_ok:
                continue
            slot, hand, wtype, rng = SLOT_OF[t], None, None, False
        elif t == 13:
            w, h = it.get("weaponType"), it.get("handType")
            if not any(w == uw and (uh is None or h == uh) for uw, uh in weapons):
                continue
            slot, hand, wtype, rng = "weapon", h, w, False
        elif t == 14:
            if it.get("rangedWeaponType") not in ranged:
                continue
            slot, hand, wtype, rng = "ranged", None, it.get("rangedWeaponType"), True
        else:
            continue
        so = (it.get("scalingOptions") or {}).get("0") or {}
        dps = ((so.get("weaponDamageMin", 0) + so.get("weaponDamageMax", 0)) / 2 / (it.get("weaponSpeed") or 2.0)) if so.get("weaponDamageMax") else 0.0
        opts = it.get("randomSuffixOptions") or [None]
        for sid in opts:
            if sid is None:
                raw = {int(k): v for k, v in (so.get("stats") or {}).items()}
                name = it["name"]
            else:
                if sid not in sufs:
                    continue
                pts = so.get("randPropPoints") or 0
                raw = {int(k): v for k, v in (so.get("stats") or {}).items()}
                for k, alloc in enumerate(sufs[sid].get("stats") or []):
                    if alloc:
                        raw[k] = raw.get(k, 0) + int(alloc * pts / 10000 + 0.5)
                name = f"{it['name']} {sufs[sid]['name']}"
            fake = {"type": t, "rangedWeaponType": it.get("rangedWeaponType"), "weaponSpeed": it.get("weaponSpeed"),
                    "scalingOptions": {"0": dict(so, stats={str(k): v for k, v in raw.items()})}}
            lab = IP.lab_stats(fake, school_share)
            if raw.get(15) and cls == "hunter":
                lab["ranged_ap"] = lab.get("ranged_ap", 0) + raw[15]
            if raw.get(16) and cls == "druid":
                lab["attack_power"] = lab.get("attack_power", 0) + raw[16]
            out.append({"id": f"{it['id']}" + (f":{sid}" if sid else ""), "name": name, "slot": slot, "hand": hand, "wtype": wtype,
                        "ranged": rng, "raw": raw, "lab": lab, "dps": dps, "unique": bool(it.get("unique"))})
    return out


# ------------------------------------------------------------------ our values
def our_values(cls, bid, level):
    f = HERE / "weights" / "leveling" / f"{cls}-{bid}.json"
    w = json.loads(f.read_text(encoding="utf-8"))
    lv = sorted(int(k) for k in w["levels"])
    lo = max([x for x in lv if x <= level] or [lv[0]])
    hi = min([x for x in lv if x >= level] or [lv[-1]])
    a, b = w["levels"][str(lo)]["weights"], w["levels"][str(hi)]["weights"]
    k = 0 if hi == lo else (level - lo) / (hi - lo)
    return {s: a.get(s, 0) * (1 - k) + b.get(s, 0) * k for s in set(a) | set(b)}


def our_item_value(vals, it, setup):
    """Seconds per kill an item version saves (its stats times our values), hit and expertise left to the set (caps)."""
    v = 0.0
    for k, x in it["lab"].items():
        if k in ("hit", "expertise"):
            continue
        if k == "weapon_dps":
            if it["ranged"]:
                k = "ranged_weapon_dps"
            elif it.get("as_oh"):
                k = "oh_weapon_dps"
            else:
                k = "mh_weapon_dps"
        elif k == "wand_dps":
            k = "wand_dps"
        elif k == "ranged_ap":
            k = "attack_power" if setup["ranged_build"] else None
        else:
            k = LAB_TO_W.get(k, k)
        if k:
            v += vals.get(k, 0.0) * x
    if it["slot"] == "ranged" and it["dps"] and setup["ranged_build"] and "weapon_dps" not in it["lab"]:
        v += vals.get("ranged_weapon_dps", 0.0) * it["dps"]
    return v


def setup_of(cls, alloc, level, rot):
    """The build's weapon setup and the hit and expertise room its talents leave, from the fight lab's own player."""
    mod = FR.make_module(cls, alloc, level, rot)
    p = mod.make_player(level)
    spell = next((s for s in mod.book.values() if getattr(s, "dmg_max", 0) > 0 and getattr(s, "kind", "") not in ("melee", "ranged")), None)
    spell_hit = mod.hit_bonus(spell) if spell is not None else 0.0
    caster = cls in ("mage", "priest", "warlock") or (p.mh is None)
    melee_miss = TB.MELEE_MISS + (TB.DW_MISS_PENALTY if p.dual_wield else 0.0)
    return {"dual": bool(p.dual_wield), "two_hand": bool(p.mh is not None and getattr(p.mh, "kind", "") == "2h"), "shield": p.block > 0,
            "caster": caster, "ranged_build": cls == "hunter" and not (hasattr(mod, "is_melee") and mod.is_melee()),
            "spell_room": max(0.0, TB.spell_miss(0) - spell_hit), "melee_room": max(0.0, melee_miss - p.hit_bonus),
            "exp_room": max(0.0, TB.MOB_DODGE + TB.MOB_PARRY - mod.dodge_parry_reduction()), "mh_kind": getattr(p.mh, "kind", None)}


# ------------------------------------------------------------------ set selection
def candidates(pool, setup, cls):
    """Candidates by slot; the off hand follows the build's setup: a one-hander when it dual-wields, a shield when it carries one,
    else an off-hand item (held in the off hand)."""
    by = {}
    for it in pool:
        if it["slot"] != "weapon":
            by.setdefault(it["slot"], []).append(it)
            continue
        h, w = it["hand"], it["wtype"]
        if h == TWO:
            by.setdefault("2h", []).append(it)
        if h in (MAIN, ONE) and w not in (SHIELD, HELD):
            by.setdefault("mh", []).append(it)
        if setup["dual"]:
            ok = h in (ONE, OFF) and w not in (SHIELD, HELD)
        elif setup["shield"]:
            ok = w == SHIELD
        else:
            ok = w == HELD
        if ok:
            by.setdefault("oh", []).append(dict(it, as_oh=True))
    return by


def choose(by, score, set_score=None, setup=None):
    """The set: per slot the best item by `score`; two different rings and trinkets; the two-hander against main hand + off hand. With
    `set_score` (a function of the whole set), a swap search afterwards (caps)."""
    def best(lst, n=1, avoid=()):
        lst = sorted((x for x in lst if x["id"].split(":")[0] not in avoid), key=score, reverse=True)
        out, seen = [], set(avoid)
        for x in lst:
            base = x["id"].split(":")[0]
            if base in seen:
                continue
            out.append(x)
            seen.add(base)
            if len(out) == n:
                break
        return out
    s = {}
    for slot in ARMOR_SLOTS:
        b = best(by.get(slot, []))
        if b:
            s[slot] = b[0]
    for slot, n in (("finger", 2), ("trinket", 2)):
        for k, x in enumerate(best(by.get(slot, []), n)):
            s[f"{slot}{k + 1}"] = x
    r = best(by.get("ranged", []))
    if r:
        s["ranged"] = r[0]
    two = best(by.get("2h", []))
    mh = best(by.get("mh", []))
    oh = best(by.get("oh", []), avoid={mh[0]["id"].split(":")[0]} if mh else ())
    want_two = setup and setup.get("two_hand")
    want_one = setup and (setup.get("dual") or setup.get("shield"))
    pair = (score(mh[0]) if mh else 0) + (score(oh[0]) if oh else 0)
    if two and (want_two or (not want_one and score(two[0]) >= pair)):
        s["weapon"] = two[0]
    else:
        if mh:
            s["weapon"] = mh[0]
        if oh:
            s["offhand"] = oh[0]
    if set_score is None:
        return s
    # swap search with the set's own score (caps): any slot to any candidate, best improvement first, until none
    slots = {k: (by.get(k.rstrip("12"), []) if k.rstrip("12") in ("finger", "trinket") else by.get({"weapon": "mh", "offhand": "oh"}.get(k, k), []))
             for k in s}
    if "weapon" in s and s["weapon"]["hand"] == TWO:
        slots["weapon"] = by.get("2h", [])
    cur = set_score(s)
    for _ in range(40):
        gain, move = 0.0, None
        for k, lst in slots.items():
            other = {x["id"].split(":")[0] for kk, x in s.items() if kk != k}
            for x in sorted(lst, key=score, reverse=True)[:60]:
                if x["id"].split(":")[0] in other or x is s[k]:
                    continue
                t = dict(s)
                t[k] = x
                d = set_score(t) - cur
                if d > gain + 1e-9:
                    gain, move = d, (k, x)
        if not move:
            break
        s[move[0]] = move[1]
        cur += gain
    return s


def totals(s):
    o = {}
    for it in s.values():
        for k, v in it["lab"].items():
            if k == "weapon_dps":
                k = "ranged_weapon_dps" if it["ranged"] else ("oh_weapon_dps" if it.get("as_oh") else "mh_weapon_dps")
            o[k] = o.get(k, 0) + v
        if it["slot"] == "ranged" and it["dps"] and "weapon_dps" not in it["lab"] and "wand_dps" not in it["lab"]:
            o["ranged_weapon_dps"] = o.get("ranged_weapon_dps", 0) + it["dps"]
    return o


def our_set_score(vals, setup):
    def f(s):
        v = sum(our_item_value(vals, it, setup) for it in s.values())
        t = totals(s)
        room = setup["spell_room"] if setup["caster"] else setup["melee_room"]
        v += vals.get("hit_rating", 0.0) * min(t.get("hit", 0.0), room * 100 * TB.RATING_PER_PCT["hit_rating"])
        v += vals.get("expertise_rating", 0.0) * min(t.get("expertise", 0.0), setup["exp_room"] / 2 * 100 * TB.RATING_PER_PCT["expertise_rating"])
        return v
    return f


# ------------------------------------------------------------------ the race
def bonus_of(s, typical, level, setup):
    """GEAR_BONUS that turns the lab's typical gear into this set."""
    t = totals(s)
    b = {}
    for k in ("intellect", "spirit", "stamina", "agility", "strength", "armor", "spell_power", "healing"):
        d = t.get(k, 0.0) - typical.get(k, 0.0)
        if d:
            b[k] = d
    for k, w in LAB_TO_W.items():
        if t.get(k):
            b[w] = t[k]
    for k in ("mp5", "attack_power", "block_value"):
        if t.get(k):
            b[k] = t[k]
    if setup["ranged_build"] and t.get("ranged_ap"):
        b["attack_power"] = b.get("attack_power", 0) + t["ranged_ap"]
    if t.get("wand_dps"):
        b["wand_dps"] = t["wand_dps"] - TB.wand_dps(level)
    if setup["mh_kind"] and t.get("mh_weapon_dps"):
        b["mh_weapon_dps"] = t["mh_weapon_dps"] - TB.weapon_dps(level, setup["mh_kind"])
    if setup["dual"] and t.get("oh_weapon_dps"):
        b["oh_weapon_dps"] = t["oh_weapon_dps"] - TB.weapon_dps(level, "1h")
    if setup["ranged_build"] and t.get("ranged_weapon_dps"):
        b["ranged_weapon_dps"] = t["ranged_weapon_dps"] - TB.weapon_dps(level, "ranged")
    return b


def typical_gear(cls, alloc, level, rot):
    """The lab's typical gear for this build (the row its module asks for: druid-caster, shaman-caster, paladin-caster)."""
    import importlib
    seen = {}
    m = importlib.import_module(cls)
    orig = m.gear_stats

    def spy(lv, tier="leveling", row=cls):
        r = orig(lv, tier, row)
        seen.setdefault("g", r)
        return r
    m.gear_stats = spy
    try:
        mod = FR.make_module(cls, alloc, level, rot)
        mod.make_player(level)
    finally:
        m.gear_stats = orig
    return seen.get("g", {})


def race_job(a):
    cls, alloc, level, rot, fights, seed, bonus = a
    TB.GEAR_BONUS.clear()
    TB.GEAR_BONUS.update(bonus)
    try:
        return FR.simulate(cls, alloc, level, rot, fights, seed, 0)["time_per_kill"]
    finally:
        TB.GEAR_BONUS.clear()


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("classes", nargs="*", default=list(PAWN_CLASS))
    ap.add_argument("--levels", default="20,30,40,50,60")
    ap.add_argument("--fights", type=int, default=3000)
    ap.add_argument("--jobs", type=int, default=10)
    ap.add_argument("--write", action="store_true")
    a = ap.parse_args()
    levels = [int(x) for x in a.levels.split(",")]
    scales = pawn_scales()
    SA = LG.fightlab_signature_audit()
    rows, jobs = [], []
    for cls in a.classes:
        for slot in SA.page_slots(cls):
            if not slot[1]:
                continue
            spec, b = slot[0], slot[1][0]
            f = HERE / "weights" / "leveling" / f"{cls}-{b['id']}.json"
            if not f.exists():
                print(f"{cls} {spec}: no value file yet ({f.name})", flush=True)
                continue
            _, order, _, rot = LG.pick(cls, spec)
            share = {"frost": 0.0}
            for L in levels:
                alloc = FR.allocation_at({"allocation": b["allocation"], "order": order}, L)
                ti, tn = tree_of(cls, alloc)
                scale = scales.get((PAWN_CLASS[cls], pawn_spec(cls, ti, tn, spec)))
                if scale is None:
                    continue
                share = school_share(cls, b, rot)
                pool = item_pool(cls, L, share)
                setup = setup_of(cls, alloc, L, rot)
                by = candidates(pool, setup, cls)
                vals = our_values(cls, b["id"], L)
                pset = choose(by, lambda it: pawn_score(scale, pawn_item_stats(it["raw"], it["dps"], it["ranged"])), setup=setup)
                oset = choose(by, lambda it: our_item_value(vals, it, setup) + vals.get("hit_rating", 0) * it["lab"].get("hit", 0) * 0.5,
                              our_set_score(vals, setup), setup)
                typ = typical_gear(cls, alloc, L, rot)
                pb, ob = bonus_of(pset, typ, L, setup), bonus_of(oset, typ, L, setup)
                k = len(rows)
                rows.append({"class": cls, "spec": spec, "build": b["id"], "level": L, "pawn_scale": f"{cls} {TREES[cls][ti - 1]}",
                             "pawn_set": {s: x["name"] for s, x in sorted(pset.items())}, "our_set": {s: x["name"] for s, x in sorted(oset.items())},
                             "pawn_bonus": {kk: round(v, 1) for kk, v in pb.items()}, "our_bonus": {kk: round(v, 1) for kk, v in ob.items()},
                             "pool": len(pool)})
                for which, bon in (("pawn", pb), ("ours", ob)):
                    for seed in (3, 4):
                        jobs.append((k, which, seed, (cls, alloc, L, rot, a.fights, seed, bon)))
            print(f"{cls} {spec}: sets picked", flush=True)
    with multiprocessing.Pool(a.jobs, initializer=_init) as pool:
        res = pool.map(race_job, [j[3] for j in jobs], chunksize=1)
    acc = {}
    for (k, which, seed, _), t in zip(jobs, res):
        acc.setdefault((k, which), []).append(t)
    for k, r in enumerate(rows):
        p, o = sum(acc[(k, "pawn")]) / 2, sum(acc[(k, "ours")]) / 2
        r["pawn_seconds"], r["our_seconds"] = round(p, 3), round(o, 3)
        r["ours_faster"] = round(1 - o / p, 4)
        same = sum(1 for s in r["our_set"] if r["pawn_set"].get(s) == r["our_set"][s])
        r["same_slots"] = same
        print(f"{r['class']:8s} {r['spec'][:28]:28s} {r['level']:2d}: Pawn {p:6.2f}s, ours {o:6.2f}s ({100 * r['ours_faster']:+.1f}%), "
              f"{same}/{len(r['our_set'])} slots alike", flush=True)
    rec = {"date": datetime.date.today().isoformat(), "fights": a.fights, "seeds": [3, 4], "levels": levels, "rows": rows,
           "pawn": "Pawn 2.14.2, ClassicHawsJon.lua Forever weights"}
    (HERE / "pawn-compare.json").write_text(json.dumps(rec, indent=1) + "\n", encoding="utf-8", newline="\n")
    if a.write:
        write_page(rec)


def _init():
    FR_init = getattr(__import__("fl_talent_opt"), "_init", None)
    if FR_init:
        FR_init("greens")


def school_share(cls, b, rot):
    """The build's damage by school for school-specific spell damage: a character's file if one plays the build, else even shares of the
    class's damage schools (an estimate)."""
    for cf in (ROOT / "_characters").glob("*/character.json"):
        c = json.loads(cf.read_text(encoding="utf-8"))
        if c.get("class") == cls and c.get("school_share") and c.get("page") and b["id"].startswith(c["page"]):
            return c["school_share"]
    return {"mage": {"frost": 0.5, "arcane": 0.25, "fire": 0.25}, "warlock": {"shadow": 0.7, "fire": 0.3}, "priest": {"shadow": 0.6, "holy": 0.4},
            "shaman": {"nature": 0.7, "fire": 0.2, "frost": 0.1}, "druid": {"nature": 0.5, "arcane": 0.5}, "paladin": {"holy": 1.0},
            "hunter": {"nature": 0.5, "arcane": 0.5}}.get(cls, {})


def write_page(rec):
    o = ["# Our stat values against Pawn's", "",
         f"> Generated by `_reference/data/characters/pawn_compare.py --write` ({rec['date']}). Do not hand-edit. Each row: the best set from "
         "one gear pool by Pawn 2.14.2's built-in Forever weights and by our values, raced in the fight lab at that level "
         f"({rec['fights']} fights on seeds 3 and 4). The race runs in the fight lab our values come from, so our set has a built-in edge: "
         "it shows the values are applied right (caps, non-linear effects) and what Pawn's picks cost if the fight lab is right, not that "
         "the fight lab matches the game. Rules: `_reference/forever-stats.md`.", "",
         "| Class | Spec | Level | Pawn's weights | Pawn's set | Ours | Ours faster | Slots alike |", "|---|---|---|---|---|---|---|---|"]
    for r in rec["rows"]:
        o.append(f"| {r['class']} | {r['spec']} | {r['level']} | {r['pawn_scale']} | {r['pawn_seconds']:.2f} s | {r['our_seconds']:.2f} s | "
                 f"{100 * r['ours_faster']:+.1f}% | {r['same_slots']}/{len(r['our_set'])} |")
    o += ["", "## Where the sets differ", ""]
    for r in rec["rows"]:
        diff = [s for s in r["our_set"] if r["pawn_set"].get(s) != r["our_set"][s]]
        if diff:
            o.append(f"- **{r['class']} {r['spec']} {r['level']}**: " + "; ".join(f"{s}: Pawn {r['pawn_set'].get(s, '-')} / ours {r['our_set'][s]}" for s in diff))
    rf = DATA / "raidsim" / "pawn-raid-compare.json"
    if rf.exists():
        rr = json.loads(rf.read_text(encoding="utf-8"))
        o[o.index("## Where the sets differ"):o.index("## Where the sets differ")] = [
            "## Level 60, raid", "",
            f"From `raidsim/pawn_raid_compare.py` ({rr['date']}): our set is the spec's phase-1 BiS set (the simulator's stat weights, trinkets "
            "and variants raced); Pawn's comes from the same pool by the same per-slot step with Pawn's weights. Both raced by the official "
            f"simulator in a full raid ({rr['iterations']} iterations on seeds 1 and 2): its engine plays the real items, procs, set bonuses and "
            "caps, independent of either weight list.", "",
            "| Class | Spec | Pawn's weights | Pawn's set | Ours | Ours ahead | Slots that differ |", "|---|---|---|---|---|---|---|"] + [
            f"| {r['class']} | {r['spec']} | {r['pawn_scale']} | {r['pawn_dps']:.0f} DPS | {r['ours_dps']:.0f} DPS | {100 * (r['ours_ahead'] or 0):+.1f}% "
            f"| {r['slots_differ']} |" for r in rr["rows"]] + [""]
    (ROOT / "_reference" / "pawn-comparison.md").write_text("\n".join(o) + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
