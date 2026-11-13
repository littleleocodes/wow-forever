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
SIM_STAT = {"StatStrength": "strength", "StatAgility": "agility", "StatStamina": "stamina", "StatIntellect": "intellect", "StatSpirit": "spirit",
            "StatSpellDamage": "spell_power", "StatHolyDamage": "holy_damage", "StatArcaneDamage": "arcane_damage", "StatFireDamage": "fire_damage",
            "StatFrostDamage": "frost_damage", "StatNatureDamage": "nature_damage", "StatShadowDamage": "shadow_damage", "StatHealingPower": "healing",
            "StatMP5": "mp5", "StatAttackPower": "attack_power", "StatRangedAttackPower": "ranged_attack_power",
            "StatFeralAttackPower": "feral_attack_power", "StatCritRating": "crit_rating", "StatHitRating": "hit_rating",
            "StatHasteRating": "haste_rating", "StatExpertiseRating": "expertise_rating", "StatArmorPenetration": "armor_penetration",
            "StatSpellPiercing": "spell_penetration", "StatArmor": "armor", "StatDefenseRating": "defense_rating", "StatDodgeRating": "dodge_rating",
            "StatParryRating": "parry_rating", "StatBlockRating": "block_rating", "StatBlockValue": "block_value",
            "PseudoStatMainHandDps": "mh_weapon_dps", "PseudoStatOffHandDps": "oh_weapon_dps", "PseudoStatRangedDps": "ranged_weapon_dps"}
# Left out on purpose: StatHealth, StatMana, StatArmorNoMods, StatBonusArmor (armor counts once, the item's whole armor), StatPhysicalDamage,
# resistances (not scored) and every other PseudoStat (percent channels no item line carries).
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


def norm(v, mode, cls=None):
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
        v.pop("healing", None)
        v.update(spell_power=sp, spell_damage=sp, spell_healing=0.0)
    elif mode == "heal":
        h = v.pop("healing", 0.0)
        v.update(spell_power=h, spell_damage=0.0, spell_healing=h)
    elif mode == "tank":
        sp, h = v.get("spell_power", 0.0), v.pop("healing", 0.0)
        v.update(spell_power=sp + h, spell_damage=sp, spell_healing=h)
    if cls == "druid" and "feral_attack_power" not in v:
        v["feral_attack_power"] = v.get("attack_power", 0.0)   # "+N Attack Power in Cat, Bear ... forms": the forms' attack power
    return {k: r(x) for k, x in v.items()}


def talents_of(b):
    return {n: k for lst in (b or {}).get("allocation", {}).values() for n, k in lst if k} if b else None


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
    split = {}
    for k, x in share.items():   # "fire, frost" (Frostfire Bolt): the spell takes either school's bonus, so each school line counts
        for sch in k.split(","):
            split[sch.strip()] = round(split.get(sch.strip(), 0.0) + x, 3)
    share = split
    totals_dual = bool(getattr(p, "dual_wield", False))
    return share, {"dual_wield": totals_dual, "spell_power_total": round(p.spell_power, 1), "attack_power_total": round(p.attack_power, 1),
                   "ranged_attack_power_total": round(getattr(p, "ranged_ap", 0.0), 1)}, melee


def school_shares(cls, alloc, level, rot):
    return level_info(cls, alloc, level, rot)[0]


def totals_with(cls, alloc, level, rot, bonus):
    """The lab player's Spell Power, attack power and ranged attack power totals with a GEAR_BONUS on top of the standard gear."""
    import run as FR
    import tables as TB
    TB.GEAR_BONUS.clear()
    TB.GEAR_BONUS.update(bonus)
    try:
        mod = FR.make_module(cls, alloc, level, rot)
        p = mod.make_player(level)
        return {"spell_power_total": round(p.spell_power, 1), "attack_power_total": round(p.attack_power, 1),
                "ranged_attack_power_total": round(getattr(p, "ranged_ap", 0.0), 1)}
    finally:
        TB.GEAR_BONUS.clear()


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
        fb = HERE / "weights" / "leveling-best" / f.name   # the second gear point: each level's best Forever set (forever_base.py)
        wb = json.loads(fb.read_text(encoding="utf-8")) if fb.exists() else None
        _, order, _, rot = LG.pick(cls, spec)
        lv = {}
        for L, row in sorted(w["levels"].items(), key=lambda kv: int(kv[0])):
            alloc = FR.allocation_at({"allocation": b["allocation"], "order": order}, int(L))
            v = {k: max(0.0, x) for k, x in row["weights"].items()}
            share, totals, melee = level_info(cls, alloc, int(L), rot)
            dual = totals.pop("dual_wield")
            unit = "spell_power" if v.get("spell_power", 0) >= v.get("attack_power", 0) else "attack_power"
            if unit == "attack_power" and cls == "hunter" and not melee:
                unit = "ranged_attack_power"
            if v.get("spell_power"):
                for sch, x in share.items():
                    v[f"{sch}_damage"] = v["spell_power"] * x
            v["hit_rating_above_cap"] = 0.0   # not measured: hit past the cap (a dual-wielder's white swings) counts 0 for now
            gear = [dict(label="standard", **totals, seconds_per_kill=row["time_per_kill"], values=norm(v, "leveling", cls))]
            if wb and L in wb["levels"]:
                rb = wb["levels"][L]
                vb = {k: max(0.0, x) for k, x in rb["weights"].items()}
                if vb.get("spell_power"):
                    for sch, x in share.items():
                        vb[f"{sch}_damage"] = vb["spell_power"] * x
                vb["hit_rating_above_cap"] = 0.0
                gear.append(dict(label="best Forever set", **totals_with(cls, alloc, int(L), rot, wb["base_bonus"][L]),
                                 seconds_per_kill=rb["time_per_kill"], values=norm(vb, "leveling", cls)))
            lv[L] = {"tree_points": tree_points(cls, alloc), "talents": {n: k for n, k in sorted(alloc.items()) if k}, "unit": unit,
                     "dual_wield": dual, "school_share": share, "gear": gear}
        out.append({"spec": spec, "build": b["id"], "rotation": rot,
                    "source": f"fight lab {w['date']}, {w['fights']} fights x 2 seeds" + ("" if final else "; FIRST PASS (small steps, noisy): being re-measured"),
                    "final": final, "levels": lv})
    # the tie-break for the add-on's spec match (2026-11-13, Addons: three mage builds share 0/0/21 at 30): the class's fastest leveling
    # build, by the mean seconds per kill at levels 20-60 in the lab's standard gear
    def mean_spk(e):
        xs = [lv["gear"][0]["seconds_per_kill"] for L, lv in e["levels"].items() if 20 <= int(L) <= 60]
        return sum(xs) / len(xs) if xs else 1e9
    have = [e for e in out if "levels" in e]
    if have:
        best = min(have, key=mean_spk)
        for e in have:
            e["default"] = e is best
    return out


def raid_row(cls, spec, slug, bid, B, vals, source):
    """vals: our keys (sim_keys). Dual wield = the set's off-hand weapon DPS has a value. A dual-wielder's white swings miss 19 points
    more than its special attacks (caps.melee_hit): its phase-1 BiS set sits past the special-attack cap (gear hit 70-90 rating plus
    talents), so the BiS reading of hit is hit's value from that cap to the white cap (hit_rating_above_cap); below the special-attack
    cap a hit point is worth hit_rating_below_cap (hit_below_cap.py). Everyone else: 0 above the cap."""
    unit = max(("spell_power", "attack_power", "ranged_attack_power"), key=lambda k: vals.get(k, 0.0))
    base = vals.get(unit) or 1.0
    b = B.get(bid)
    dual = vals.get("oh_weapon_dps", 0.0) > 0
    v = {k: max(0.0, x) / base for k, x in vals.items()}
    v["hit_rating_above_cap"] = v.get("hit_rating", 0.0) if dual else 0.0
    return {"spec": spec, "slug": slug, "build": bid, "tree_points": tree_points(cls, b["allocation"]) if b else None,
            "talents": talents_of(b), "unit": unit, "dual_wield": dual, "source": source, "values": norm(v, "raid", cls)}


def sim_keys(w):
    return {SIM_STAT[k]: x for k, x in w.items() if k in SIM_STAT}


def raid(cls, below, page):
    out = []
    B = builds_of(cls)
    for f in sorted((RAID / "ml").glob(f"{cls}-*.json")):
        d = json.loads(f.read_text(encoding="utf-8"))
        w = ((d.get("gear") or {}).get("bis") or {}).get("weights")
        if not w:
            continue
        vals = sim_keys(w)
        hb = (below.get("specs") or {}).get(f.stem) or page.get(f.stem)
        if hb and hb.get("hit_below_cap"):
            vals["hit_rating_below_cap"] = hb["hit_below_cap"]
        bid = d.get("best") if d.get("best") in B else (page.get(f.stem) or {}).get("build", d.get("best"))
        out.append(raid_row(cls, d["spec"], f.stem.split("-", 1)[1], bid, B, vals,
                            f"raid simulator, {f.name} (the spec's best build in its phase-1 BiS set, full raid)"))
    for stem, row in sorted(page.items()):
        if row.get("class") != cls or not row.get("weights"):
            continue
        vals = sim_keys(row["weights"])
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
                    "talents": talents_of(b), "unit": "healing", "source": f"healer lab, heallab/heal-values.json ({hv['date']}): capacity per point in {row['gear']}",
                    "values": norm(v, "heal", cls),
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
            "tree_points": tree_points(cls, b["allocation"]) if b else None, "talents": talents_of(b), "unit": "stamina",
            "source": f"raid simulator, {w['build']} in {w['entry']}, {w['date']}: tank value per point (threat, damage taken, effective health)",
            "values": norm({TANK_STAT.get(k, k): x / sp["stamina"] for k, x in sp.items()}, "tank", cls)}


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


def capped(x, room, below, above):
    return min(x, room) * below + max(0.0, x - room) * above


def delta(values, old, new, caps):
    """What swapping `old` (one item, or the summed stats of the items it replaces) for `new` is worth: every stat x its value; each
    capped stat ({stat: {cap_pct, current_pct, below, above}}: hit_rating, expertise_rating) worth `below` up to the cap and `above`
    past it, the room measured from the character's current percent with the old item's rating taken off first."""
    g = sum((new.get(k, 0.0) - old.get(k, 0.0)) * values.get(k, 0.0) for k in set(old) | set(new) if k not in caps)
    for k, c in caps.items():
        per = RATINGS[k]
        room = max(0.0, c["cap_pct"] - (c["current_pct"] - old.get(k, 0.0) / per)) * per
        g += capped(new.get(k, 0.0), room, c["below"], c["above"]) - capped(old.get(k, 0.0), room, c["below"], c["above"])
    return g


def static_score(values, stats):
    return sum(x * values.get(k, 0.0) for k, x in stats.items() if k != "hit_rating")


CASES = {
    "caster": ("INVTYPE_HEAD", "head", {"intellect": 8, "stamina": 6, "spell_power": 7}, {"intellect": 6, "spirit": 5, "spell_power": 12, "crit_rating": 14}),
    "melee": ("INVTYPE_CHEST", "chest", {"strength": 10, "stamina": 8}, {"agility": 9, "stamina": 6, "attack_power": 20, "crit_rating": 14}),
    "weapon": ("INVTYPE_WEAPON", "mainhand", {"mh_weapon_dps": 18.5, "strength": 5}, {"mh_weapon_dps": 21.0, "stamina": 4}),
    "heal": ("INVTYPE_HAND", "hands", {"intellect": 8, "spell_healing": 22, "spell_damage": 7}, {"intellect": 10, "spirit": 6, "spell_power": 18, "mp5": 4}),
    "hit": ("INVTYPE_WAIST", "waist", {"stamina": 5}, {"stamina": 3, "hit_rating": 20}),
    "expertise": ("INVTYPE_HAND", "hands", {"stamina": 5}, {"stamina": 3, "expertise_rating": 30}),
    "offhand": ("INVTYPE_WEAPON", "offhand", {"oh_weapon_dps": 15.0, "agility": 3}, {"oh_weapon_dps": 18.0, "agility": 4}),
}
RINGS = ({"stamina": 6, "intellect": 4}, {"spell_power": 9, "spirit": 3}, {"strength": 7, "agility": 5}, {"attack_power": 14, "stamina": 3})
RING_NEW = {"spell_power": 6, "intellect": 5, "attack_power": 10, "agility": 4}
STAFF_PAIR = ([("mainhand", "INVTYPE_WEAPONMAINHAND", {"intellect": 5, "spell_power": 8}), ("offhand", "INVTYPE_HOLDABLE", {"intellect": 4, "spirit": 3})],
              ("INVTYPE_2HWEAPON", {"intellect": 10, "spirit": 6, "spell_power": 14}))


def caps_for(mode, values, caster, hit_cur=0.0, exp_cur=0.0):
    """The caps a mode applies (the file's caps block): leveling at your own level, raid and heal against a boss (three levels up),
    tanks in front of the boss."""
    if mode == "leveling":
        hit_cap, exp_cap = (4.0 if caster else 5.0), 10.0
        hb, ha = values.get("hit_rating", 0.0), values.get("hit_rating_above_cap", 0.0)
    else:
        hit_cap = 17.0 if caster else 8.0
        exp_cap = 20.5 if mode == "tank" else 6.5
        hb, ha = values.get("hit_rating_below_cap", values.get("hit_rating", 0.0)), values.get("hit_rating_above_cap", 0.0)
    return {"hit_rating": {"cap_pct": hit_cap, "current_pct": hit_cur, "below": hb, "above": ha},
            "expertise_rating": {"cap_pct": exp_cap, "current_pct": exp_cur, "below": values.get("expertise_rating", 0.0), "above": 0.0}}


def vec(name, mode, cls, spec, entry_id, equipped, new, values, caps, extra, expected_of, **more):
    old = {}
    for _, _, st in equipped:
        for k, x in st.items():
            old[k] = old.get(k, 0.0) + x
    d = delta(values, old, new[1], caps)
    return dict({"name": name, "mode": mode, "class": cls, "spec": spec, "entry": entry_id,
                 "hit_cap_pct": caps["hit_rating"]["cap_pct"], "current_hit_pct": caps["hit_rating"]["current_pct"],
                 "expertise_cap_pct": caps["expertise_rating"]["cap_pct"], "current_expertise_pct": caps["expertise_rating"]["current_pct"],
                 "caps": caps, "equipped": [{"slot": s_, "equipLoc": l_, "stats": st} for s_, l_, st in equipped],
                 "new": {"equipLoc": new[0], "stats": new[1]}, "tolerance": TOLERANCE}, **extra, **more, expected=expected_of(d))


def one(case):
    loc, slot, old, new = CASES[case]
    return [(slot, loc, old)], (loc, new)


def test_vectors(o):
    out = []
    for cls, c in o["classes"].items():
        lev = [e for e in c["leveling"] if "levels" in e]
        if lev:
            e = lev[0]
            e20 = e["levels"]["20"]
            caster = e20["unit"] == "spell_power"
            ut = e20["gear"][0][e20["unit"] + "_total"] + 15
            extra = {"level": 23, "unit": e20["unit"], "unit_total": ut}
            spk, vals = lev_at(e, 23, ut)

            def exp(d, spk=spk):
                return {"seconds_per_kill": round(spk, 6), "gain_seconds": round(d, 6), "pct_faster": round(100 * d / spk, 6)}
            tag = f"{cls} leveling {e['build']}"
            main = "caster" if caster else "melee"
            out.append(vec(f"{tag}: {main}", "leveling", cls, e["spec"], e["build"], *one(main), vals, caps_for("leveling", vals, caster), extra, exp))
            hc = caps_for("leveling", vals, caster, hit_cur=(3.0 if caster else 4.0))
            out.append(vec(f"{tag}: hit at the cap edge", "leveling", cls, e["spec"], e["build"], *one("hit"), vals, hc, extra, exp))
            if not caster:
                out.append(vec(f"{tag}: weapon", "leveling", cls, e["spec"], e["build"], *one("weapon"), vals, caps_for("leveling", vals, False), extra, exp))
                ec = caps_for("leveling", vals, False, exp_cur=8.0)
                out.append(vec(f"{tag}: expertise at the cap edge", "leveling", cls, e["spec"], e["build"], *one("expertise"), vals, ec, extra, exp))
            else:
                eq, nw = STAFF_PAIR
                out.append(vec(f"{tag}: a staff against main hand + held item", "leveling", cls, e["spec"], e["build"], eq, nw, vals,
                               caps_for("leveling", vals, True), extra, exp, replaced_slots=["mainhand", "offhand"]))
            a, b = (RINGS[0], RINGS[1]) if caster else (RINGS[2], RINGS[3])
            weaker = "finger1" if static_score(vals, a) <= static_score(vals, b) else "finger2"
            r1 = vec(f"{tag}: rings (the weaker is replaced)", "leveling", cls, e["spec"], e["build"],
                     [(weaker, "INVTYPE_FINGER", a if weaker == "finger1" else b)], ("INVTYPE_FINGER", RING_NEW), vals,
                     caps_for("leveling", vals, caster), extra, exp)
            r1["equipped"] = [{"slot": "finger1", "equipLoc": "INVTYPE_FINGER", "stats": a}, {"slot": "finger2", "equipLoc": "INVTYPE_FINGER", "stats": b}]
            r1["expected"]["replaced_slot"] = weaker
            out.append(r1)
            spk7, vals7 = lev_at(e, 7, ut)
            out.append(vec(f"{tag}: below level 10 uses level 10", "leveling", cls, e["spec"], e["build"], *one(main), vals7,
                           caps_for("leveling", vals7, caster), {"level": 7, "unit": e20["unit"], "unit_total": ut},
                           lambda d, spk=spk7: {"seconds_per_kill": round(spk, 6), "gain_seconds": round(d, 6), "pct_faster": round(100 * d / spk, 6)}))
            dw = next((x for x in lev if any(lv.get("dual_wield") for lv in x["levels"].values())), None)
            if dw:
                L = next(k for k, lv in sorted(dw["levels"].items(), key=lambda kv: int(kv[0])) if lv.get("dual_wield") and int(k) >= 20)
                lvl = int(L)
                ut2 = dw["levels"][L]["gear"][0][dw["levels"][L]["unit"] + "_total"]
                spk2, v2 = lev_at(dw, lvl, ut2)
                out.append(vec(f"{cls} leveling {dw['build']}: dual-wield off hand", "leveling", cls, dw["spec"], dw["build"], *one("offhand"), v2,
                               caps_for("leveling", v2, False), {"level": lvl, "unit": dw["levels"][L]["unit"], "unit_total": ut2},
                               lambda d, spk=spk2: {"seconds_per_kill": round(spk, 6), "gain_seconds": round(d, 6), "pct_faster": round(100 * d / spk, 6)}))
        for mode, rows in (("raid", c["raid"][:1] + [x for x in c["raid"][1:] if x.get("dual_wield")][:1]), ("heal", c["heal"][:1]),
                           ("tank", [c["tank"]] if c["tank"] else [])):
            for e in rows:
                v = e["values"]
                caster = e["unit"] in ("spell_power", "healing")
                main = {"raid": "caster" if caster else "melee", "heal": "heal", "tank": "melee"}[mode]
                extra = {"level": 60, "equipped_score": 1000.0}

                def exp(d):
                    return {"score_delta": round(d, 6), "pct": round(100 * d / 1000.0, 6)}
                eid = e.get("slug") or e["build"]
                tag = f"{cls} {mode} {eid}"
                base_caps = caps_for(mode, v, caster)
                out.append(vec(f"{tag}: {main}", mode, cls, e["spec"], eid, *one(main), v, base_caps, extra, exp))
                hc = caps_for(mode, v, caster, hit_cur=base_caps["hit_rating"]["cap_pct"] - 1.0)
                out.append(vec(f"{tag}: hit at the cap edge" + (" (dual wield: past the cap counts the white-swing value)" if e.get("dual_wield") else ""),
                               mode, cls, e["spec"], eid, *one("hit"), v, hc, extra, exp))
                if not caster:
                    ec = caps_for(mode, v, False, exp_cur=base_caps["expertise_rating"]["cap_pct"] - 2.0)
                    out.append(vec(f"{tag}: expertise at the cap edge", mode, cls, e["spec"], eid, *one("expertise"), v, ec, extra, exp))
                if e.get("dual_wield"):
                    out.append(vec(f"{tag}: dual-wield off hand", mode, cls, e["spec"], eid, *one("offhand"), v, base_caps, extra, exp))
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
    # exact-tie defaults for the raid and heal lists too (Addons, 2026-11-13: a priest halfway between Holy and Discipline): the healer
    # spec with the highest healer-lab capacity, the damage spec with the highest full-raid DPS in its BiS set (raidsim/pawn-raid-compare.json)
    rc = json.loads((RAID / "pawn-raid-compare.json").read_text(encoding="utf-8")) if (RAID / "pawn-raid-compare.json").exists() else {"rows": []}
    dps = {(x["class"], x["spec"]): x["ours_dps"] for x in rc["rows"]}
    for cls, c in o["classes"].items():
        if c["heal"]:
            best = max(c["heal"], key=lambda e: (hv.get("specs") or {}).get(f"{cls}|{e['spec']}", {}).get("capacity", 0))
            for e in c["heal"]:
                e["default"] = e is best
        if c["raid"]:
            best = max(c["raid"], key=lambda e: dps.get((cls, e["spec"]), 0))
            for e in c["raid"]:
                e["default"] = e is best
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
