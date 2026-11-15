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
    "spell_penetration": {"note": "Spell Piercing: past the target's resistance it is bonus damage, on average P / (P + 8 x your level + 19) of a "
                                   "spell's damage, a tenth on DoT ticks, none on Holy (wowsims/forever issue #76, 138 Forever combat logs). "
                                   "Leveling values from the fight lab (2026-11-13), raid values from the simulator."},
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
TALENT_TOLERANCE = 1e-5   # talent_vectors' expected values are rounded to 5 decimals (r), so a port that does not round is up to 5e-6 off
NOT_SCORED = {"health_regen": "not measured (the fight lab's eating time does not read health regeneration from gear)",
              "resistances": "worth 0 (no simulator models resistance)",
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


# ----------------------------------------------------------------------------------------------------------------------------------
# Talent transforms (2026-11-14, user: "Can we make it read talents exactly and take those talents into consideration?", then "yes,
# build the talent data side for GearCheck"). The values are measured on one build per entry (its talents at each level are in the
# entry); a player's own talents can differ in exactly the talents that change what a stat is worth. Those talents, by class, with
# their per-rank numbers read from each rank's own tooltip (forever-talents/<class>.json), so a patch that changes a number changes
# the table. Kinds:
#   stat_pct    +p% of a stat (Lightning Reflexes: Agility): every point of the stat on gear is (1 + p) points
#   health_pct  +p% total health (Survivalist): Stamina's value, which is its health, scales the same way
#   mana_pct    +p% maximum mana (Fel Vitality): Intellect's own value scales with it (the lab's Intellect is mostly mana)
#   armor_pct   +p% armor from items (Toughness, Moonkin Form): armor's value scales
#   offhand_pct +p% off-hand damage (Predator's Edge, Dual Wield Specialization): the off-hand weapon's DPS value scales
#   convert     p% of stat F becomes stat T (Careful Aim: Intellect to attack power): F gains p x T's value per point of F
# A transform with "form" applies only to an entry played in that form (the entry's "forms": druids). Left out: flat bonuses (Predatory
# Strikes, Demonic Knowledge), temporary procs (Spirit Tap, Dark Inspiration), weapon-type talents (Weaponmaster, Hack and Slash) and
# crit or hit talents (they move other stats' values only second-order). talent_adjust is the reference implementation the add-on
# ports; talent_vectors in the file are its results.
TALENT_TRANSFORMS = {
    "druid": [("Heart of the Wild", "stat_pct", {"stat": "intellect"}, r"Intellect by (\d+)%"),
              ("Heart of the Wild", "stat_pct", {"stat": "stamina", "form": "bear"}, r"Stamina is increased by (\d+)%"),
              ("Heart of the Wild", "stat_pct", {"stat": "strength", "form": "cat"}, r"Strength is increased by (\d+)%"),
              ("Living Spirit", "stat_pct", {"stat": "spirit"}, r"Spirit by (\d+)%"),
              ("Natural Instinct", "convert", {"from": "intellect", "to": "spell_healing"}, r"spell healing by (\d+)% of your Intellect"),
              ("Moonkin Form", "armor_pct", {"form": "moonkin"}, r"Armor contribution from items by (\d+)%")],
    "hunter": [("Lightning Reflexes", "stat_pct", {"stat": "agility"}, r"Agility by (\d+)%"),
               ("Careful Aim", "convert", {"from": "intellect", "to": "attack_power"}, r"Attack Power by (\d+)% of your Intellect"),
               ("Survivalist", "health_pct", {}, r"Health by (\d+)%"),
               ("Predator's Edge", "offhand_pct", {}, r"Off Hand weapon damage by (\d+)%")],
    "mage": [("Arcane Mind", "stat_pct", {"stat": "intellect"}, r"Intellect by (\d+)%"),
             ("Arcane Resilience", "convert", {"from": "intellect", "to": "armor"}, r"Armor by an amount equal to (\d+)% of your Intellect")],
    "paladin": [("Divine Strength", "stat_pct", {"stat": "strength"}, r"Strength by (\d+)%"),
                ("Divine Intellect", "stat_pct", {"stat": "intellect"}, r"Intellect by (\d+)%"),
                ("Toughness", "armor_pct", {}, r"armor value from items by (\d+)%"),
                ("Champion of the Light", "convert", {"from": "intellect", "to": "spell_damage"}, r"spell damage by up to (\d+)% of your Intellect")],
    "priest": [("Mental Strength", "stat_pct", {"stat": "intellect"}, r"Intellect by (\d+)%"),
               ("Spiritual Guidance", "convert", {"from": "spirit", "to": "spell_healing"}, r"spell healing by up to (\d+)% of your total Spirit"),
               ("Spiritual Guidance", "convert", {"from": "spirit", "to": "spell_damage"}, r"spell damage by up to (\d+)% of your total Spirit")],
    "rogue": [("Dual Wield Specialization", "offhand_pct", {}, r"off-hand weapon by (\d+)%")],
    "shaman": [("Ancestral Knowledge", "stat_pct", {"stat": "intellect"}, r"Intellect by (\d+)%"),
               ("Toughness", "stat_pct", {"stat": "stamina"}, r"Stamina by (\d+)%"),
               ("Mental Quickness", "convert", {"from": "intellect", "to": "spell_power"}, r"spell damage and healing by up to (\d+)% of your Intellect"),
               ("Mental Dexterity", "convert", {"from": "intellect", "to": "attack_power"}, r"Attack Power by an amount equal to (\d+)% of your Intellect"),
               ("Improved Reincarnation", "health_pct", {}, r"maximum health by (\d+)%")],
    "warlock": [("Demonic Embrace", "stat_pct", {"stat": "stamina"}, r"Stamina by (\d+)%"),
                ("Fel Vitality", "mana_pct", {}, r"your maximum Mana by (\d+)%")],
    "warrior": [("Dual Wield Specialization", "offhand_pct", {}, r"off-hand weapon by (\d+)%")],
}


def talent_transforms(cls):
    """[{talent, kind, per_rank: [%...], stat|from|to|form}] for the class, each rank's number read from its own tooltip; a talent
    the current trees lack or whose wording no longer matches is left out with a warning."""
    import re
    trees = json.loads((DATA / "forever-talents" / f"{cls}.json").read_text(encoding="utf-8"))["trees"]
    by = {t["name"]: t for tr in trees for t in tr["talents"]}
    out = []
    for name, kind, extra, pat in TALENT_TRANSFORMS.get(cls, []):
        t = by.get(name)
        if t is None:
            print(f"WARNING: {cls} talent transform: {name} is not in the trees")
            continue
        nums = []
        for rk in t.get("ranks") or []:
            txt = rk if isinstance(rk, str) else (rk or {}).get("text") or ""
            m = re.search(pat, txt)
            nums.append(float(m.group(1)) if m else None)
        if not nums or None in nums or any(b < a for a, b in zip(nums, nums[1:])):
            print(f"WARNING: {cls} talent transform: {name} ({kind}) not read from its tooltips: {nums}")
            continue
        out.append(dict({"talent": name, "kind": kind, "per_rank": nums}, **extra))
    return out


def entry_forms(cls, mode, e):
    """The druid forms an entry is played in (its values were measured there): cat, bear or moonkin; [] for every other class."""
    if cls != "druid":
        return []
    rot, spec = (e.get("rotation") or ""), (e.get("spec") or "")
    if mode == "tank" or "bear" in spec.lower():
        return ["bear"]
    if "cat" in rot or "Feral" in spec:
        return ["cat"]
    if "balance" in rot or "Balance" in spec:
        return ["moonkin"]
    return []


def talent_pct(tr, ranks):
    """The transform's fraction for a talent rank map (rank 0 or absent: 0; a rank above the table: its last number)."""
    k = int((ranks or {}).get(tr["talent"], 0) or 0)
    return tr["per_rank"][min(k, len(tr["per_rank"])) - 1] / 100.0 if k > 0 else 0.0


def talent_adjust(values, transforms, forms, build_talents, player_talents):
    """Values measured with build_talents, re-stated for player_talents (first order). Per stat S with stat_pct p (summed over its
    transforms) and conversions S -> T at c: the build's conversion part, (1 + p_build) x c_build x v[T], is taken out, the rest
    (S's own worth) scales by (1 + p_player) / (1 + p_build), and the player's conversion part, (1 + p_player) x c_player x v[T], is
    added back, with v[T] as measured. Then Stamina by health_pct, Intellect's own worth by mana_pct, armor by armor_pct and the
    off-hand weapon's DPS by offhand_pct, each (1 + player) / (1 + build). Values stay at 0 or above."""
    live = [tr for tr in transforms if not tr.get("form") or tr["form"] in (forms or [])]
    v = dict(values)
    agg = {}
    for tr in live:
        pb, pp = talent_pct(tr, build_talents), talent_pct(tr, player_talents)
        if tr["kind"] == "stat_pct":
            a = agg.setdefault(("stat", tr["stat"]), [0.0, 0.0])
            a[0] += pb
            a[1] += pp
        elif tr["kind"] in ("health_pct", "mana_pct", "armor_pct", "offhand_pct"):
            a = agg.setdefault((tr["kind"], None), [0.0, 0.0])
            a[0] += pb
            a[1] += pp
    stats = {tr["stat"] for tr in live if tr["kind"] == "stat_pct"} | {tr["from"] for tr in live if tr["kind"] == "convert"}
    if ("mana_pct", None) in agg:   # Fel Vitality: Intellect's own part scales with mana even with no Intellect talent (2026-11-14,
        stats.add("intellect")      # the Addons session: the warlock had kept it unscaled)
    touched = set()
    for s in sorted(stats):
        if s not in values:
            continue
        mb, mp = agg.get(("stat", s), [0.0, 0.0])
        conv = [tr for tr in live if tr["kind"] == "convert" and tr["from"] == s]
        cb = sum(talent_pct(tr, build_talents) * values.get(tr["to"], 0.0) for tr in conv)
        cp = sum(talent_pct(tr, player_talents) * values.get(tr["to"], 0.0) for tr in conv)
        own = values[s] - (1 + mb) * cb
        if s == "intellect" and ("mana_pct", None) in agg:
            nb, npl = agg[("mana_pct", None)]
            own *= (1 + npl) / (1 + nb)
        v[s] = own * (1 + mp) / (1 + mb) + (1 + mp) * cp
        touched.add(s)
    for kind, key in (("health_pct", "stamina"), ("armor_pct", "armor"), ("offhand_pct", "oh_weapon_dps")):
        if (kind, None) in agg and key in v:
            b, p = agg[(kind, None)]
            v[key] = v[key] * (1 + p) / (1 + b)
            touched.add(key)
    # only the re-stated values are clamped and rounded; every other value stays exactly as measured (a tank's slightly negative haste
    # had turned 0 the moment talents were read, 2026-11-14, the Addons session)
    return {k: (r(max(0.0, x)) if k in touched else x) for k, x in v.items()}


def talent_vectors(o):
    """Cases the add-on's port of talent_adjust must reproduce (within TOLERANCE): one per class with transforms, from a real entry's
    values and talents; the player's talents are the entry's with the class's transform talents moved (dropped to 0, or set to the
    top rank), plus a guildmate's melee Survival hunter (2026-11-14) as the hunter's case."""
    out = []
    hyrax = {"Lethal Attacks": 5, "Careful Aim": 1, "Improved Tracking": 5, "Savage Strikes": 2, "Survivalist": 3, "Clever Traps": 2,
             "Surefooted": 3, "Predator's Edge": 5, "Resourcefulness": 2, "Expose Prey": 2, "Survivalist's Discipline": 2, "Strider Kick": 1,
             "Lightning Reflexes": 5}
    for cls in CLASSES:
        trs = o["talent_transforms"].get(cls) or []
        if not trs:
            continue
        c = o["classes"][cls]
        for mode in ("leveling", "raid", "heal", "tank"):
            ents = c.get(mode) or []
            ents = [ents] if isinstance(ents, dict) else ents
            if cls == "hunter" and mode == "leveling":   # the guildmate's case wants the melee Survival entry
                ents = sorted(ents, key=lambda e: "survival-open" not in (e.get("build") or ""))
            for e in ents:
                if mode == "leveling":
                    lv = e.get("levels", {}).get("45") or next(iter(e.get("levels", {}).values()), None)
                    if not lv:
                        continue
                    values, talents, level = lv["gear"][0]["values"], lv.get("talents") or {}, 45
                else:
                    values, talents, level = e.get("values") or {}, e.get("talents") or {}, 60
                names = {tr["talent"] for tr in trs if not tr.get("form") or tr["form"] in e.get("forms", [])}
                if not values or not names:
                    continue
                player = dict(talents)
                for n in names:   # flip each transform talent: taken -> 0, missing -> its top rank
                    top = len(next(tr for tr in trs if tr["talent"] == n)["per_rank"])
                    player[n] = 0 if talents.get(n) else top
                if cls == "hunter" and mode == "leveling" and "survival" in e.get("build", ""):
                    player = hyrax
                exp = talent_adjust(values, trs, e.get("forms", []), talents, player)
                out.append({"name": f"{cls} {mode} {e.get('build') or e.get('spec')} level {level}: talents flipped" if player is not hyrax
                            else "hunter melee Survival at 45 with a guildmate's level-47 talents", "class": cls, "mode": mode,
                            "entry": e.get("build"), "level": level, "forms": e.get("forms", []), "values": values,
                            "build_talents": talents, "player_talents": player, "expected": exp, "tolerance": TALENT_TOLERANCE})
                break
    return out


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
    allsh = sum((o.get("shares") or {}).values()) or 1.0
    white = (o.get("shares") or {}).get("Melee", 0.0) / allsh   # the player's own white swings (a pet's melee has its own name)
    phys = 0.0
    for name, dmg in (o.get("shares") or {}).items():   # white swings and physical specials (no school in the book, or physical)
        sp = mod.book.get(name) if hasattr(mod, "book") else None
        sch = getattr(sp, "school", None) if sp is not None else None
        if not sch or sch == "physical":
            phys += dmg
    setup = {"white_share": round(white, 3), "physical_share": round(phys / allsh, 3), "mh_kind": getattr(getattr(p, "mh", None), "kind", None)}
    return share, {"dual_wield": totals_dual, "spell_power_total": round(p.spell_power, 1), "attack_power_total": round(p.attack_power, 1),
                   "ranged_attack_power_total": round(getattr(p, "ranged_ap", 0.0), 1), "setup": setup}, melee


def school_shares(cls, alloc, level, rot):
    return level_info(cls, alloc, level, rot)[0]


WAND_CLASSES = ("mage", "priest", "warlock")
BASE_FILE = HERE / "weights" / "forever-base.json"


def set_stats(cls, std, setup, dual, ranged, level, bonus=None):
    """A gear point's summed item stats in the add-on's keys (hit and expertise left out): the lab's standard gear (forever-base.json
    "standard" plus the lab's weapon and wand dps for the level) and, with `bonus`, the best Forever set (standard + its GEAR_BONUS)."""
    import tables as TB
    o = {k: std.get(k, 0.0) for k in ("intellect", "spirit", "stamina", "agility", "strength", "armor")}
    o["spell_power"] = std.get("spell_power", 0.0)
    o["spell_healing"] = std.get("healing", 0.0)
    o["attack_power"] = std.get("attack_power", 0.0)
    if setup.get("mh_kind"):
        o["mh_weapon_dps"] = TB.weapon_dps(level, setup["mh_kind"])
    if dual:
        o["oh_weapon_dps"] = TB.weapon_dps(level, "1h")
    if ranged:
        o["ranged_weapon_dps"] = TB.weapon_dps(level, "ranged")
    if cls in WAND_CLASSES:
        o["wand_dps"] = TB.wand_dps(level)
    for k, v in (bonus or {}).items():
        if k in ("hit_rating", "expertise_rating"):
            continue
        key = {"healing": "spell_healing"}.get(k, k)
        o[key] = o.get(key, 0.0) + v
    return {k: round(v, 2) for k, v in sorted(o.items()) if v}


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


_TT = {}


def lab_offhand_fix(cls, alloc):
    """The factor a hunter's measured off-hand weapon DPS value takes (2026-11-14). The fight lab applies Predator's Edge's off-hand
    bonus to the off-hand weapon's own damage only (hunter.make_player), so a measured point of off-hand DPS (GEAR_BONUS's dps_bonus)
    carries none of it. The game's aura (A_MOD_OFFHAND_DAMAGE_PCT) and the raid simulator scale the whole off-hand hit. Until the lab
    is fixed (_reference/pvp-plan.md, fight-lab issues), the value is scaled by 1 + the build's Predator's Edge fraction at that
    level, which is what the offhand_pct talent transform expects inside it. Warriors and rogues need nothing: their Dual Wield
    Specialization already multiplies the whole off-hand hit in the lab."""
    if cls != "hunter":
        return 1.0
    if cls not in _TT:
        _TT[cls] = next((t for t in talent_transforms(cls) if t["talent"] == "Predator's Edge"), None)
    tr = _TT[cls]
    return 1.0 + (talent_pct(tr, alloc) if tr else 0.0)


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
        base = json.loads(BASE_FILE.read_text(encoding="utf-8"))["builds"].get(f"{cls}-{b['id']}", {}) if BASE_FILE.exists() else {}
        _, order, _, rot = LG.pick(cls, spec)
        lv = {}
        for L, row in sorted(w["levels"].items(), key=lambda kv: int(kv[0])):
            alloc = FR.allocation_at({"allocation": b["allocation"], "order": order}, int(L))
            v = {k: max(0.0, x) for k, x in row["weights"].items()}
            ohf = lab_offhand_fix(cls, alloc)
            if "oh_weapon_dps" in v:
                v["oh_weapon_dps"] *= ohf
            share, totals, melee = level_info(cls, alloc, int(L), rot)
            dual = totals.pop("dual_wield")
            setup = totals.pop("setup")
            ranged = cls == "hunter" and not melee
            caster = cls in WAND_CLASSES   # druids, shamans and paladins: set for the whole build below
            unit = "spell_power" if caster else ("ranged_attack_power" if ranged else "attack_power")
            brow = base.get(L)
            if v.get("spell_power"):
                for sch, x in share.items():
                    v[f"{sch}_damage"] = v["spell_power"] * x
            # hit past the special-attack cap: a dual-wielder's white swings (stat_weights.py --only hit_rating_above_cap, 2026-11-13); else 0
            v["hit_rating_above_cap"] = max(0.0, row["weights"].get("hit_rating_above_cap", 0.0)) if dual else 0.0
            gear = [dict(label="standard", **totals, seconds_per_kill=row["time_per_kill"], values=norm(v, "leveling", cls))]
            if brow:
                gear[0]["item_stats"] = set_stats(cls, brow["standard"], setup, dual, ranged, int(L))
            if wb and L in wb["levels"]:
                rb = wb["levels"][L]
                vb = {k: max(0.0, x) for k, x in rb["weights"].items()}
                if "oh_weapon_dps" in vb:
                    vb["oh_weapon_dps"] *= ohf
                if vb.get("spell_power"):
                    for sch, x in share.items():
                        vb[f"{sch}_damage"] = vb["spell_power"] * x
                vb["hit_rating_above_cap"] = max(0.0, rb["weights"].get("hit_rating_above_cap", 0.0)) if dual else 0.0
                gear.append(dict(label="best Forever set", **totals_with(cls, alloc, int(L), rot, wb["base_bonus"][L]),
                                 seconds_per_kill=rb["time_per_kill"], values=norm(vb, "leveling", cls)))
                if brow:
                    gear[-1]["item_stats"] = set_stats(cls, brow["standard"], setup, dual, ranged, int(L), wb["base_bonus"][L])
            lv[L] = {"tree_points": tree_points(cls, alloc), "talents": {n: k for n, k in sorted(alloc.items()) if k}, "unit": unit,
                     "caster": caster, "white_share": setup["white_share"], "physical_share": setup["physical_share"],
                     "dual_wield": dual, "school_share": share, "gear": gear}
        # caster or melee (2026-11-13; Addons: a per-level white-swing rule made rogues casters from 30-40 and Enhancement from 50): one
        # flag per build. Mages, priests and warlocks are casters; rogues, warriors and hunters never; a druid, shaman or paladin build is a
        # caster when its physical damage (white swings and physical specials) is under 30% of its damage at levels 20-60 (Elemental
        # 11-16%, Balance 0%; Enhancement 48-55%, paladins 30-56%, the cat 95%). The value per point is no guide: a paladin's seals and a
        # shaman's shocks make Spell Power worth more per point than attack power.
        if cls in ("druid", "shaman", "paladin"):
            ph = [x["physical_share"] for L, x in lv.items() if 20 <= int(L) <= 60]
            cst = bool(ph) and sum(ph) / len(ph) < 0.3
            for x in lv.values():
                x["caster"] = cst
                x["unit"] = "spell_power" if cst else "attack_power"
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
def gear_share(lv, item_stats):
    """Where a character's gear sits between a level's two gear points (0 = the lab's standard gear, 1 = the best Forever set): the
    gain from the standard set to the character's own items over the gain from the standard set to the best set, both scored with
    the standard gear's values (delta(); hit and expertise left out, as the sets leave them out). None without item stats."""
    g = lv["gear"]
    if len(g) < 2 or "item_stats" not in g[0] or "item_stats" not in g[-1]:
        return None
    v = g[0]["values"]
    skip = ("hit_rating", "expertise_rating")
    mine = {k: x for k, x in item_stats.items() if k not in skip}
    den = delta(v, g[0]["item_stats"], g[-1]["item_stats"], {})
    if den <= 0:
        return 0.0
    return min(1.0, max(0.0, delta(v, g[0]["item_stats"], mine, {}) / den))


def lev_at(entry, level, unit_total=None, item_stats=None):
    """(seconds per kill, values) of a leveling entry at a level and the character's unit-stat total: linear between the measured
    levels (below the first: the first), and between gear points by unit_total (clamped at the ends)."""
    lv = sorted(int(k) for k in entry["levels"])
    lo = max([x for x in lv if x <= level] or [lv[0]])
    hi = min([x for x in lv if x >= level] or [lv[-1]])
    k = 0.0 if hi == lo else (level - lo) / (hi - lo)

    def at(L):
        e = entry["levels"][str(L)]
        t = gear_share(e, item_stats) if item_stats is not None else None
        if t is not None:   # placed by the character's own items (the add-on's preferred way)
            a, b = e["gear"][0], e["gear"][-1]
            vals = {s: a["values"].get(s, 0.0) * (1 - t) + b["values"].get(s, 0.0) * t for s in set(a["values"]) | set(b["values"])}
            return a["seconds_per_kill"] * (1 - t) + b["seconds_per_kill"] * t, vals
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
            caster = e20.get("caster", e20["unit"] == "spell_power")
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
            e30 = e["levels"].get("30")
            if e30 and len(e30["gear"]) > 1:   # the gear points alone, at a measured level: halfway between the two sets, and past the best
                key = e30["unit"] + "_total"
                g0, g1 = e30["gear"][0][key], e30["gear"][-1][key]
                for name, ut3 in (("halfway between the standard gear and the best Forever set", (g0 + g1) / 2),
                                  ("past the best Forever set (clamped)", g1 + 40)):
                    spk3, vals3 = lev_at(e, 30, ut3)
                    out.append(vec(f"{tag}: {name}", "leveling", cls, e["spec"], e["build"], *one(main), vals3,
                                   caps_for("leveling", vals3, caster), {"level": 30, "unit": e30["unit"], "unit_total": round(ut3, 6)},
                                   lambda d, spk=spk3: {"seconds_per_kill": round(spk, 6), "gain_seconds": round(d, 6), "pct_faster": round(100 * d / spk, 6)}))
            if e30 and len(e30["gear"]) > 1 and "item_stats" in e30["gear"][0]:   # placed by the character's own items
                s0, s1 = e30["gear"][0]["item_stats"], e30["gear"][-1]["item_stats"]
                for name, f in (("placed by its items, a third of the way to the best Forever set", 1 / 3), ("placed by its items: the best set itself", 1.0)):
                    mine = {k: round(s0.get(k, 0.0) + f * (s1.get(k, 0.0) - s0.get(k, 0.0)), 4) for k in set(s0) | set(s1)}
                    mine = {k: x for k, x in sorted(mine.items()) if x}
                    t = gear_share(e30, mine)
                    for L32 in (30, 32):
                        spk4, vals4 = lev_at(e, L32, item_stats=mine)
                        out.append(vec(f"{tag}: {name}, level {L32}", "leveling", cls, e["spec"], e["build"], *one(main), vals4,
                                       caps_for("leveling", vals4, caster), {"level": L32, "unit": e30["unit"], "item_stats": mine,
                                                                             "gear_share_at_30": round(t, 6)},
                                       lambda d, spk=spk4: {"seconds_per_kill": round(spk, 6), "gain_seconds": round(d, 6), "pct_faster": round(100 * d / spk, 6)}))
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
                  "level (every 5 from 10 to 60: interpolate; below 10 the level-10 numbers) and per gear point. Two gear points per level: "
                  "'standard' (the lab's standard gear) and 'best Forever set'; each carries item_stats, the set's summed item stats in "
                  "these keys (hit and expertise left out). Place the character between them by its own items (preferred): share = "
                  "delta(standard values, standard item_stats, your summed item stats without hit and expertise) / delta(standard "
                  "values, standard item_stats, best item_stats), clamped 0-1, computed at each of the two levels around yours; values "
                  "and seconds_per_kill = standard + share x (best - standard). Fallback: interpolate on the character's own total of "
                  "the level's unit stat, clamped. Each level says caster (true: the spell hit cap; false: the melee cap). An item's gain = sum of (new - old) x value, its share of "
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
             "" if all(len(lv["gear"]) > 1 for c in o["classes"].values() for e in c["leveling"] for lv in e.get("levels", {}).values())
             else "some leveling levels have one gear point only (the lab's standard gear)"]
    o["status"] = ("preliminary: " + "; ".join(x for x in parts if x)) if any(parts) else (
        "complete: two gear points per leveling level (the lab's standard gear and each level's best Forever set), raid, heal and tank values")
    o["test_vectors"] = test_vectors(o)
    # talent transforms (2026-11-14): the add-on re-states each entry's values for the player's own talent ranks
    for cls, c in o["classes"].items():
        for mode in ("leveling", "raid", "heal", "tank"):
            ents = c.get(mode) or []
            for e in ([ents] if isinstance(ents, dict) else ents):
                e["forms"] = entry_forms(cls, mode, e)
    o["talent_transforms"] = {cls: talent_transforms(cls) for cls in CLASSES}
    o["talent_note"] = (
        "Talents that change what a stat is worth, per class (talent_transforms: kind, per_rank percentages read from each rank's tooltip, "
        "stat / from / to / form). Each entry's values were measured with its own talents (leveling: levels.<L>.talents; raid, heal, tank: "
        "talents); re-state them for the player's own ranks before scoring. Per stat S: p = sum of S's stat_pct, c = S's convert "
        "fractions (S -> T); own = v[S] - (1 + p_build) x sum(c_build x v[T]); v'[S] = own x (1 + p_player) / (1 + p_build) + (1 + "
        "p_player) x sum(c_player x v[T]); Intellect's own part also x (1 + mana_player) / (1 + mana_build). Then v'[stamina] x (1 + "
        "health_player) / (1 + health_build), v'[armor] x armor ratio, v'[oh_weapon_dps] x off-hand ratio. A transform with form "
        "applies only to an entry whose forms list it. Fraction for rank k: per_rank[k - 1] / 100 (0 at rank 0; the last number above "
        "the table). Use v[T] as measured. Intellect's mana scaling applies whenever a mana_pct transform is live, with or without an "
        "Intellect stat_pct or convert. Clamp at 0 and round to 5 decimals only the values re-stated; every other value stays exactly "
        "as measured. talent_vectors: reproduce expected within tolerance (1e-5: expected is rounded to 5 decimals). A first-order "
        "re-statement, not a new measurement.")
    o["talent_vectors"] = talent_vectors(o)
    OUT.mkdir(exist_ok=True)
    p = OUT / "forever-gear-values.json"
    p.write_text(json.dumps(o, indent=1) + "\n", encoding="utf-8", newline="\n")
    print(f"wrote {p.relative_to(ROOT)}: {o['status']}; {len(o['test_vectors'])} test vectors")


if __name__ == "__main__":
    main()
