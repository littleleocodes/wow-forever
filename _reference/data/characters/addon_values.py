"""Stat values and caps for the in-game gear add-on, every class (2026-11-13, user: "this is being made for all classes right? And before
it's built I think we should make sure all the stats are scored"; replaces addon_weights.py, which covered Arcea and Tara only).

    python _reference/data/characters/addon_values.py      -> _reference/data/characters/addon/forever-gear-values.json

- leveling: every leveling page pick (weights/leveling/<class>-<build id>.json, stat_weights_all.py): by level the fight lab's seconds per
  kill each point of a stat saves (negative readings are the lab's noise: 0), the kill time, the build's damage by spell school (one lab
  run per level: school-specific spell damage counts by that share) and the unit the add-on shows a gain in (Spell Power or attack power,
  whichever the build values more);
- raid: every damage spec with an ML record: the simulator's stat weights in the spec's phase-1 BiS set (gear.bis.weights) over the unit
  stat's, with hit below the cap from raidsim/hit-below-cap.json (a BiS set at the cap reads hit as 0);
- raid, the pages the ML records leave out (raidsim/page_stat_weights.py: Protection-Retribution, Shockadin, Assassination-Subtlety; hit
  under the cap for Beast Mastery): the simulator's weights for the page's pick in its BiS set;
- heal: every healer spec at 60 (heallab/heal_values.py: the healer lab's capacity per point in the spec's BiS set, in healing power;
  haste also with a hasted global cooldown, which is open);
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


VERSION = 1
TOLERANCE = 1e-6
NOT_SCORED = {"health_regen": "not measured (the fight lab's eating time does not read health regeneration from gear)",
              "resistances": "worth 0 (no simulator models resistance)", "spell_penetration": "worth 0 while leveling",
              "effects": "Use, Equip-proc, chance-on-hit and set-bonus effects are not scored (static stats only); relics, idols, librams and "
                         "totems with only an effect score 0 and say so"}


def norm(v, mode):
    """The three spell lines, each with its own value for the mode (2026-11-13: the add-on maps one tooltip line to one key):
    "+N Spell Power" (damage and healing) -> spell_power, "+N Spell Damage" -> spell_damage, "+N Spell Healing" -> spell_healing.
    Leveling: the lab's spell_power raises damage and heals alike, its healing heals only; damage alone is not measured apart (the
    leveling builds' own heals are small), so spell_damage takes spell_power's value. Raid damage specs: the simulator's spell damage,
    healing worth nothing. Healers: healing power, damage worth nothing. Tanks: the simulator's spell damage (threat) plus healing."""
    v = dict(v)
    if mode == "leveling":
        sp, h = v.get("spell_power", 0.0), v.pop("healing", 0.0)
        v.update(spell_power=sp, spell_damage=sp, spell_healing=h)
    elif mode == "raid":
        sp = v.get("spell_power", 0.0)
        v.update(spell_power=sp, spell_damage=sp, spell_healing=0.0)
    elif mode == "heal":
        h = v.pop("healing", 0.0)
        v.update(spell_power=h, spell_damage=0.0, spell_healing=h)
    elif mode == "tank":
        sp, h = v.get("spell_power", 0.0), v.pop("healing", 0.0)
        v.update(spell_power=sp + h, spell_damage=sp, spell_healing=h)
    return {k: r(x) for k, x in v.items()}


def builds_of(cls):
    return {b["id"]: b for b in json.loads((ROOT / cls / "research" / "talents" / "forever" / "proposed-builds.json").read_text(encoding="utf-8"))["builds"]}


def tree_points(cls, alloc):
    """[{index, name, points}] in the talent tabs' order (the client's GetTalentTabInfo index 1-3; the Forever tree data's order)."""
    import pawn_scales as PS
    pts = PS.tree_points(cls, alloc)
    order = [t["name"] for t in json.loads((DATA / "forever-talents" / f"{cls}.json").read_text(encoding="utf-8"))["trees"]]
    return [{"index": i + 1, "name": n, "points": pts.get(n, 0)} for i, n in enumerate(order)]


def level_info(cls, alloc, level, rot):
    """The build's damage by spell school at one level (300 fights; physical damage left out) and the lab player's totals in its
    standard gear: Spell Power, attack power and ranged attack power; whether the build fights in melee (hunters)."""
    import run as FR
    mod = FR.make_module(cls, alloc, level, rot)
    p = mod.make_player(level)
    o = FR.simulate(cls, alloc, level, rot, 300, 9, 0)
    by = {}
    for name, dmg in (o.get("shares") or {}).items():   # damage share by spell (white hits and pets have no school in the book)
        sp = mod.book.get(name) if hasattr(mod, "book") else None
        sch = getattr(sp, "school", None) if sp is not None else None
        if sch and sch != "physical" and dmg:
            by[sch] = by.get(sch, 0.0) + dmg
    tot = sum(by.values())
    share = {k: round(v / tot, 3) for k, v in sorted(by.items(), key=lambda kv: -kv[1])} if tot else {}
    melee = bool(getattr(mod, "is_melee", None) and mod.is_melee())
    return share, {"spell_power_total": round(p.spell_power, 1), "attack_power_total": round(p.attack_power, 1),
                   "ranged_attack_power_total": round(getattr(p, "ranged_ap", 0.0), 1)}, melee


def school_shares(cls, alloc, level, rot):
    return level_info(cls, alloc, level, rot)[0]


def leveling(cls):
    import level_guides as LG
    import run as FR
    import stat_weights as SW
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
        final = w.get("steps") == {k: SW.FULL_STEPS[k] for k in SW.CLASS_STATS[cls]}
        _, order, _, rot = LG.pick(cls, spec)
        lv = {}
        for L, row in sorted(w["levels"].items(), key=lambda kv: int(kv[0])):
            alloc = FR.allocation_at({"allocation": b["allocation"], "order": order}, int(L))
            v = {k: max(0.0, x) for k, x in row["weights"].items()}
            share, totals, melee = level_info(cls, alloc, int(L), rot)
            unit = "spell_power" if v.get("spell_power", 0) >= v.get("attack_power", 0) else "attack_power"
            if unit == "attack_power" and cls == "hunter" and not melee:
                unit = "ranged_attack_power"
            if v.get("spell_power"):
                for sch, x in share.items():
                    v[f"{sch}_damage"] = v["spell_power"] * x
            lv[L] = {"tree_points": tree_points(cls, alloc), "unit": unit, "school_share": share,
                     "gear": [dict(label="standard", **totals, seconds_per_kill=row["time_per_kill"], values=norm(v, "leveling"))]}
        out.append({"spec": spec, "build": b["id"], "rotation": rot,
                    "source": f"fight lab {w['date']}, {w['fights']} fights x 2 seeds" + ("" if final else "; FIRST PASS (small steps, noisy): being re-measured"),
                    "final": final, "levels": lv})
    return out


def raid_row(cls, spec, slug, bid, B, vals, source):
    unit = max(("spell_power", "attack_power", "ranged_attack_power"), key=lambda k: vals.get(k, 0.0))
    base = vals.get(unit) or 1.0
    b = B.get(bid)
    return {"spec": spec, "slug": slug, "build": bid, "tree_points": tree_points(cls, b["allocation"]) if b else None, "unit": unit,
            "source": source, "values": norm({k: max(0.0, x) / base for k, x in vals.items()}, "raid")}


def raid(cls, below, page):
    out = []
    B = builds_of(cls)
    for f in sorted((RAID / "ml").glob(f"{cls}-*.json")):
        d = json.loads(f.read_text(encoding="utf-8"))
        w = ((d.get("gear") or {}).get("bis") or {}).get("weights")
        if not w:
            continue
        vals = {SIM_STAT.get(k, k): x for k, x in w.items()}
        hb = (below.get("specs") or {}).get(f.stem) or page.get(f.stem)
        if hb and hb.get("hit_below_cap"):
            vals["hit_rating_below_cap"] = hb["hit_below_cap"]
        bid = d.get("best") if d.get("best") in B else (page.get(f.stem) or {}).get("build", d.get("best"))
        out.append(raid_row(cls, d["spec"], f.stem.split("-", 1)[1], bid, B, vals,
                            f"raid simulator, {f.name} (the spec's best build in its phase-1 BiS set, full raid)"))
    for stem, row in sorted(page.items()):
        if row.get("class") != cls or not row.get("weights"):
            continue
        vals = {SIM_STAT.get(k, k): x for k, x in row["weights"].items()}
        if row.get("hit_below_cap"):
            vals["hit_rating_below_cap"] = row["hit_below_cap"]
        out.append(raid_row(cls, row["spec"], stem.split("-", 1)[1], row["build"], B, vals,
                            f"raid simulator, raidsim/page-stat-weights.json (the page's pick in {row['gear_why']}, full raid)"))
    return out


def heal(cls, hv):
    out = []
    B = builds_of(cls)
    for key, row in sorted((hv.get("specs") or {}).items()):
        if row["class"] != cls:
            continue
        v = {k: max(0.0, x["healing_eq"]) for k, x in row["values"].items()}
        b = B.get(row["build"])
        out.append({"spec": row["spec"], "build": row["build"], "tree_points": tree_points(cls, b["allocation"]) if b else None,
                    "unit": "healing", "source": f"healer lab, heallab/heal-values.json ({hv['date']}): capacity per point in {row['gear']}",
                    "values": norm(v, "heal"),
                    "errors": {k: x["healing_eq_se"] for k, x in row["values"].items()},
                    "errors_note": "the bootstrap standard error of each value, same unit; for Shift details at most, not the main line",
                    "haste_rating_if_gcd_hasted": r(max(0.0, row["haste_if_gcd_hasted"]["healing_eq"]))})
    return out


def tank(cls):
    f = HERE / "weights" / f"{cls}-tank.json"
    if not f.exists():
        return None
    w = json.loads(f.read_text(encoding="utf-8"))
    sp = w["share_per_point"]
    b = builds_of(cls).get(w["build"])
    return {"spec": "Protection" if cls != "druid" else "Feral Combat (bear)", "build": w["build"],
            "tree_points": tree_points(cls, b["allocation"]) if b else None, "unit": "stamina",
            "source": f"raid simulator, {w['build']} in {w['entry']}, {w['date']}: tank value per point (threat, damage taken, effective health)",
            "values": norm({TANK_STAT.get(k, k): x / sp["stamina"] for k, x in sp.items()}, "tank")}


# ------------------------------------------------------------------ the add-on's math, as a reference for the test vectors
def lev_at(entry, level, unit_total):
    """(seconds per kill, values) of a leveling entry at a level and the character's unit-stat total: linear between the measured
    levels (below the first: the first), and between gear points by unit_total (clamped at the ends)."""
    lv = sorted(int(k) for k in entry["levels"])
    lo = max([x for x in lv if x <= level] or [lv[0]])
    hi = min([x for x in lv if x >= level] or [lv[-1]])
    k = 0.0 if hi == lo else (level - lo) / (hi - lo)

    def at(L):
        e = entry["levels"][str(L)]
        key = f"{e['unit']}_total"
        g = sorted(e["gear"], key=lambda x: x[key])
        if len(g) == 1 or unit_total <= g[0][key]:
            a, b, t = g[0], g[0], 0.0
        elif unit_total >= g[-1][key]:
            a, b, t = g[-1], g[-1], 0.0
        else:
            j = next(i for i in range(1, len(g)) if g[i][key] >= unit_total)
            a, b = g[j - 1], g[j]
            t = (unit_total - a[key]) / (b[key] - a[key])
        vals = {s: a["values"].get(s, 0.0) * (1 - t) + b["values"].get(s, 0.0) * t for s in set(a["values"]) | set(b["values"])}
        return a["seconds_per_kill"] * (1 - t) + b["seconds_per_kill"] * t, vals
    s1, v1 = at(lo)
    s2, v2 = at(hi)
    return s1 * (1 - k) + s2 * k, {s: v1.get(s, 0.0) * (1 - k) + v2.get(s, 0.0) * k for s in set(v1) | set(v2)}


def delta(values, old, new, hit_value, hit_cap_pct, current_hit_pct):
    """What swapping `old` for `new` is worth: every stat x its value; hit only up to the cap (the character's current hit with the old
    item's taken off first). Expertise works the same way with its own room (caps.expertise)."""
    g = sum((new.get(k, 0.0) - old.get(k, 0.0)) * values.get(k, 0.0) for k in set(old) | set(new) if k != "hit_rating")
    per = RATINGS["hit_rating"]
    room = max(0.0, hit_cap_pct - (current_hit_pct - old.get("hit_rating", 0.0) / per)) * per
    return g + (min(new.get("hit_rating", 0.0), room) - min(old.get("hit_rating", 0.0), room)) * hit_value


def static_score(values, stats):
    return sum(x * values.get(k, 0.0) for k, x in stats.items() if k != "hit_rating")


CASES = {
    "caster": ("INVTYPE_HEAD", "head", {"intellect": 8, "stamina": 6, "spell_power": 7}, {"intellect": 6, "spirit": 5, "spell_power": 12, "crit_rating": 14}),
    "melee": ("INVTYPE_CHEST", "chest", {"strength": 10, "stamina": 8}, {"agility": 9, "stamina": 6, "attack_power": 20, "crit_rating": 14}),
    "weapon": ("INVTYPE_WEAPON", "mainhand", {"mh_weapon_dps": 18.5, "strength": 5}, {"mh_weapon_dps": 21.0, "stamina": 4}),
    "heal": ("INVTYPE_HAND", "hands", {"intellect": 8, "spell_healing": 22, "spell_damage": 7}, {"intellect": 10, "spirit": 6, "spell_power": 18, "mp5": 4}),
    "hit": ("INVTYPE_WAIST", "waist", {"stamina": 5}, {"stamina": 3, "hit_rating": 20}),
}
RINGS = ({"stamina": 6, "intellect": 4}, {"spell_power": 9, "spirit": 3}, {"strength": 7, "agility": 5}, {"attack_power": 14, "stamina": 3})
RING_NEW = {"spell_power": 6, "intellect": 5, "attack_power": 10, "agility": 4}


def vector(name, mode, cls, spec, entry_id, case, values, hit_value, cap, cur, extra, expected_of):
    loc, slot, old, new = CASES[case] if isinstance(case, str) else case
    d = delta(values, old, new, hit_value, cap, cur)
    return dict({"name": name, "mode": mode, "class": cls, "spec": spec, "entry": entry_id, "hit_cap_pct": cap, "current_hit_pct": cur,
                 "equipped": [{"slot": slot, "equipLoc": loc, "stats": old}], "new": {"equipLoc": loc, "stats": new},
                 "tolerance": TOLERANCE}, **extra, expected=expected_of(d))


def ring_vector(name, mode, cls, spec, entry_id, values, extra, expected_of):
    a, b = (RINGS[0], RINGS[1]) if values.get("spell_power", 0) >= values.get("attack_power", 0) else (RINGS[2], RINGS[3])
    weaker = "finger1" if static_score(values, a) <= static_score(values, b) else "finger2"
    old = a if weaker == "finger1" else b
    d = delta(values, old, RING_NEW, 0.0, 0.0, 0.0)
    return dict({"name": name, "mode": mode, "class": cls, "spec": spec, "entry": entry_id, "hit_cap_pct": 0.0, "current_hit_pct": 0.0,
                 "equipped": [{"slot": "finger1", "equipLoc": "INVTYPE_FINGER", "stats": a}, {"slot": "finger2", "equipLoc": "INVTYPE_FINGER", "stats": b}],
                 "new": {"equipLoc": "INVTYPE_FINGER", "stats": RING_NEW}, "tolerance": TOLERANCE}, **extra,
                expected=dict(expected_of(d), replaced_slot=weaker))


def test_vectors(o):
    out = []
    for cls, c in o["classes"].items():
        lev = [e for e in c["leveling"] if "levels" in e]
        if lev:
            e = lev[0]
            e20 = e["levels"]["20"]
            caster = e20["unit"] == "spell_power"
            ut = e20["gear"][0][e20["unit"] + "_total"] + 15
            cap = 4.0 if caster else 5.0
            spk, vals = lev_at(e, 23, ut)
            extra = {"level": 23, "unit": e20["unit"], "unit_total": ut}
            exp = lambda d, spk=spk: {"seconds_per_kill": round(spk, 6), "gain_seconds": round(d, 6), "pct_faster": round(100 * d / spk, 6)}  # noqa: E731
            for case, cur in (("caster" if caster else "melee", 0.0), ("hit", 3.0)) + ((("weapon", 0.0),) if not caster else ()):
                out.append(vector(f"{cls} leveling {e['build']}: {case}", "leveling", cls, e["spec"], e["build"], case, vals,
                                  vals.get("hit_rating", 0.0), cap, cur, extra, exp))
            out.append(ring_vector(f"{cls} leveling {e['build']}: rings (the weaker is replaced)", "leveling", cls, e["spec"], e["build"],
                                   vals, extra, exp))
            spk9, vals9 = lev_at(e, 7, ut)
            out.append(vector(f"{cls} leveling {e['build']}: below level 10 uses level 10", "leveling", cls, e["spec"], e["build"],
                              "caster" if caster else "melee", vals9, vals9.get("hit_rating", 0.0), cap, 0.0,
                              {"level": 7, "unit": e20["unit"], "unit_total": ut},
                              lambda d, spk=spk9: {"seconds_per_kill": round(spk, 6), "gain_seconds": round(d, 6), "pct_faster": round(100 * d / spk, 6)}))
        for mode, rows in (("raid", c["raid"][:1]), ("heal", c["heal"][:1]), ("tank", [c["tank"]] if c["tank"] else [])):
            for e in rows:
                v = e["values"]
                caster = e["unit"] in ("spell_power", "healing")
                case = {"raid": "caster" if caster else "melee", "heal": "heal", "tank": "melee"}[mode]
                cap = 17.0 if caster else 8.0
                hv = v.get("hit_rating_below_cap", v.get("hit_rating", 0.0))
                extra = {"level": 60, "equipped_score": 1000.0}
                exp = lambda d: {"score_delta": round(d, 6), "pct": round(100 * d / 1000.0, 6)}  # noqa: E731
                eid = e.get("slug") or e["build"]
                out.append(vector(f"{cls} {mode} {eid}: {case}", mode, cls, e["spec"], eid, case, v, hv, cap, 0.0, extra, exp))
                out.append(vector(f"{cls} {mode} {eid}: hit at the cap edge", mode, cls, e["spec"], eid, "hit", v, hv, cap, cap - 1.0, extra, exp))
    return out


def main():
    below = json.loads((RAID / "hit-below-cap.json").read_text(encoding="utf-8")) if (RAID / "hit-below-cap.json").exists() else {}
    page = json.loads((RAID / "page-stat-weights.json").read_text(encoding="utf-8")).get("specs", {}) if (RAID / "page-stat-weights.json").exists() else {}
    hp = DATA / "heallab" / "heal-values.json"
    hv = json.loads(hp.read_text(encoding="utf-8")) if hp.exists() else {}
    o = {"version": VERSION, "made": datetime.datetime.now().strftime("%Y-%m-%d %H:%M"), "status": "", "ratings_per_percent": RATINGS,
         "caps": CAPS, "not_scored": NOT_SCORED,
         "note": ("Class keys: the client's classFile, lowercased. Leveling: values are seconds per kill one point saves (fight lab), per "
                  "level (every 5 from 10 to 60: interpolate; below 10 the level-10 numbers) and per gear point (interpolate on the "
                  "character's own total of the level's unit stat, clamped); an item's gain = sum of (new - old) x value, its share of "
                  "faster kills = gain / seconds_per_kill. Raid, heal and tank values: worth per point with the unit stat = 1 (1 Spell "
                  "Power, attack power, healing power or Stamina); an item's share = its score change over the score of everything "
                  "equipped. Spell lines map one to one: '+N Spell Power' -> spell_power, '+N Spell Damage' -> spell_damage, '+N Spell "
                  "Healing' -> spell_healing, '+N Frost Spell Damage' -> frost_damage; count every line the tooltip lists (healing items "
                  "list a third as a separate Spell Damage line). mp5 = the client's mana regeneration. Ratings per rating point, keyed "
                  "by the stat keys (flat at every level). Hit counts only up to the cap (caps; the character's current hit with the "
                  "replaced item's taken off): leveling hit_rating, raid hit_rating_below_cap. Rings and trinkets: the new item replaces "
                  "the one that scores less. Values are clamped at 0. test_vectors: reproduce 'expected' within 'tolerance'. Models of "
                  "the beta (fight lab, raid simulator, healer lab), not measurements."),
         "classes": {}}
    for cls in CLASSES:
        o["classes"][cls] = {"leveling": leveling(cls), "raid": raid(cls, below, page), "heal": heal(cls, hv), "tank": tank(cls)}
        print(f"{cls}: {len(o['classes'][cls]['leveling'])} leveling builds, {len(o['classes'][cls]['raid'])} raid specs, "
              f"{len(o['classes'][cls]['heal'])} healer specs, tank {'yes' if o['classes'][cls]['tank'] else 'no'}", flush=True)
    todo = [e["build"] for c in o["classes"].values() for e in c["leveling"] if not e.get("final")]
    parts = [f"{len(todo)} leveling builds still hold the first pass's noisy small-step numbers" if todo else "",
             "healer values not measured yet" if not hv else "",
             "one gear point per level (the lab's standard gear); gear points for Forever's own items come later"]
    o["status"] = "preliminary: " + "; ".join(x for x in parts if x)
    o["test_vectors"] = test_vectors(o)
    OUT.mkdir(exist_ok=True)
    p = OUT / "forever-gear-values.json"
    p.write_text(json.dumps(o, indent=1) + "\n", encoding="utf-8", newline="\n")
    print(f"wrote {p.relative_to(ROOT)}: {o['status']}; {len(o['test_vectors'])} test vectors")


if __name__ == "__main__":
    main()
