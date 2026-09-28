"""Level tables the fight simulator assumes (Classic Era formulas and rules of thumb, stated so they can be argued with).

Everything here is an assumption unless a source is named. Beta measurements (kill times, mob health, drink rates)
should replace these numbers when they exist; each function says what it stands for. Mob health, damage, armor and the
caster share by level come from `mob_stats.json` (Classic 1.12 creature database, see `mob_stats.py`): data for Classic,
still an assumption for WoW: Forever.
"""
import json
import pathlib


def interp(points, x):
    """Piecewise-linear interpolation over [(x, y), ...] sorted by x, clamped at the ends."""
    if x <= points[0][0]:
        return points[0][1]
    for (x0, y0), (x1, y1) in zip(points, points[1:]):
        if x <= x1:
            return y0 + (y1 - y0) * (x - x0) / (x1 - x0)
    return points[-1][1]


# ------------------------------------------------------------------ mobs (normal, non-elite, same level as the player)

MOB_HP_MULT = 1.0        # sensitivity knob: scales mob health (the beta NPC scans record level and zone but not health)
MOB_DMG_MULT = 1.0       # sensitivity knob: scales mob melee damage

_MOB_STATS = json.load(open(pathlib.Path(__file__).resolve().parent / "mob_stats.json", encoding="utf-8"))
_ANCHORS = sorted(((int(L), a) for L, a in _MOB_STATS["anchors"].items()), key=lambda kv: kv[0])
_HP = [(L, a["health"]) for L, a in _ANCHORS]
_DMG = [(L, a["dmg"]) for L, a in _ANCHORS]
_ARMOR = [(L, a["armor"]) for L, a in _ANCHORS]
_CASTERS = [(L, a["caster_share"]) for L, a in _ANCHORS]
_CASTER_HP = [(L, (a["caster_health"] or 0.8 * a["health"]) / a["health"]) for L, a in _ANCHORS]
_CASTER_DMG = [(L, (a["caster_dmg"] or 0.9 * a["dmg"]) / a["dmg"]) for L, a in _ANCHORS]


def mob_health(level):
    """Median health of a normal outdoor mob at the level, from the Classic 1.12 creature database (cmangos classic-db z2815, 2,262
    templates weighted by spawn count: 187 at 10, 466 at 20, 1,002 at 30, 1,844 at 40, 2,672 at 50, 3,878 at 60; `mob_stats.json`).
    Unverified for WoW: Forever (creature stats are server side; the Wowhead Forever tooltips carry level and type only)."""
    return interp(_HP, level) * MOB_HP_MULT


def mob_melee_damage(level):
    """Median melee swing of a normal mob before armor, from the Classic 1.12 creature database (13 at 10, 32 at 20, 48 at 30, 68 at 40,
    95 at 50, 117 at 60 per 2.0 s swing; the earlier rule of thumb was 2-2.5x higher). Unverified for WoW: Forever."""
    return interp(_DMG, level) * MOB_DMG_MULT


def mob_armor(level):
    """Median armor of a normal mob from the Classic 1.12 creature database (450 at 10, 817 at 20, 1,200 at 30, 2,101 at 40, 2,999 at 50, 3,489 at 60)."""
    return interp(_ARMOR, level)


MOB_SWING = 2.0          # seconds between melee swings
MOB_SPEED = 7.0          # yards per second (same as a running player)
MELEE_RANGE = 5.0        # yards at which a mob starts swinging
MOB_HIT_CHANCE = 0.95    # vs a same-level player before the player's dodge
MOB_CRIT_CHANCE = 0.05   # NPC crits deal double damage
MOB_HP_SPREAD = 0.20     # +-20% uniform spread of mob health (casters low, warriors high)
MOB_DMG_SPREAD = 0.20    # +-20% uniform spread of a swing

# caster mobs: a share of pulls is a mage-class mob that stands at range and casts a bolt every MOB_CAST_TIME seconds
# (spell damage: no armor) until interrupted (Counterspell, Kick, Earth Shock, Silence, a stun ...), then runs in and
# melees until the lockout ends. MOB_CASTER_SHARE None = the Classic creature database's share by level (mob_caster_share).
MOB_CASTER_SHARE = None
MOB_CAST_TIME = 2.5      # seconds per bolt (Classic caster mobs: 2-3 s Fireball / Shadow Bolt / Lightning Bolt)
MOB_CAST_GAP = 1.0       # seconds between bolts
MOB_CAST_DMG_MULT = 1.6  # a bolt hits for this times the mob's melee swing (Classic: Defias Pillager Fireball 25-35 vs 15-21 melee)
MOB_CAST_RANGE = 30.0    # yards from which it casts
MOB_CAST_CRIT = 0.05

# runners: a share of pulls flee at RUNNER_HP of their health for RUNNER_TIME seconds (no swings, no casts, not stopped by
# damage; roots and stuns hold them), then come back. Classic: most humanoids run at about 20% health; the creature
# database's humanoid share of normal outdoor spawns is 35-50% by level. Default 0 = not simulated (sensitivity rows use 0.2).
RUNNER_SHARE = 0.0
AOE_SPELLS = {   # area attacks: mobs hit at most (0 = all in reach), reach in yards (5 = melee), damage falloff per further target
    "Whirlwind": {"max_targets": 4, "radius": 8.0}, "Cleave": {"max_targets": 2, "radius": 5.0}, "Thunder Clap": {"max_targets": 4, "radius": 8.0},
    "Swipe": {"max_targets": 3, "radius": 5.0}, "Multi-Shot": {"center": "target", "max_targets": 3, "radius": 10.0}, "Volley": {"center": "target", "max_targets": 0, "radius": 8.0},
    "Chain Lightning": {"center": "target", "max_targets": 3, "radius": 10.0, "falloff": 0.7}, "Fire Nova": {"max_targets": 0, "radius": 10.0}, "Magma Totem": {"max_targets": 0, "radius": 8.0},
    "Rain of Fire": {"center": "target", "max_targets": 0, "radius": 8.0}, "Hellfire": {"max_targets": 0, "radius": 10.0}, "Holy Nova": {"max_targets": 0, "radius": 10.0},
    "Consecration": {"max_targets": 0, "radius": 8.0}, "Hurricane": {"center": "target", "max_targets": 0, "radius": 10.0},
    "Blizzard": {"center": "target", "max_targets": 0, "radius": 8.0}, "Arcane Explosion": {"max_targets": 0, "radius": 10.0}, "Cone of Cold": {"max_targets": 0, "radius": 10.0},
    "Flamestrike": {"center": "target", "max_targets": 0, "radius": 8.0}, "Blast Wave": {"max_targets": 0, "radius": 10.0}, "Frost Nova": {"max_targets": 0, "radius": 10.0},
}
MOBS_PER_PULL = 1        # mobs per pull (the AoE grinding profile runs with 3-5); extra mobs are the same kind, arrive together and stay on the player
RUNNER_HP = 0.20
RUNNER_TIME = 5.0


def mob_caster_share(level):
    """Share of normal outdoor mob spawns whose unit class is mage or paladin, by level, from the Classic 1.12 creature database
    (5% at 1-5, 14% at 10, 12-23% from 15 to 55, 9% at 60; `mob_stats.json`)."""
    return interp(_CASTERS, level)


def mob_caster_health(level):
    """Median health of a mage-class mob (Classic 1.12 creature database: 75-90% of the all-mob median)."""
    return mob_health(level) * interp(_CASTER_HP, level)


def mob_caster_damage(level):
    """Median melee swing of a mage-class mob (Classic 1.12 creature database: 85-100% of the all-mob median)."""
    return mob_melee_damage(level) * interp(_CASTER_DMG, level)


# ------------------------------------------------------------------ combat formulas

def spell_miss(level_diff):
    """Classic spell miss vs a mob `level_diff` levels above the caster: 4% at +0, 5% at +1, 6% at +2, 17% at +3."""
    table = {-3: 0.01, -2: 0.02, -1: 0.03, 0: 0.04, 1: 0.05, 2: 0.06, 3: 0.17}
    return table.get(max(-3, min(3, level_diff)), 0.17)


def ranged_miss(level_diff):
    """White ranged/melee miss by level difference: 4% at +0, 5% at +1, 5.5% at +2, 6% at +3 (wowsims Forever attack table)."""
    table = {0: 0.04, 1: 0.05, 2: 0.055, 3: 0.06, 4: 0.08}
    return table.get(max(0, min(4, level_diff)), 0.08) if level_diff >= 0 else 0.04


def armor_mitigation(armor, attacker_level):
    """Classic physical mitigation: armor / (armor + 400 + 85 * attacker level) for attackers under level 60."""
    if armor <= 0:
        return 0.0
    denom = armor + 400 + 85 * attacker_level
    return min(0.75, armor / denom)


def int_per_spell_crit(level):
    """Intellect per 1% spell crit: 59.5 at 60 for mages (Forever client: 0.0168% per Intellect at max level), scaling with level (~30 at 30)."""
    return max(8.0, 59.5 * level / 60.0)


PARTIAL_RESIST_LOSS = 0.025   # average damage lost to partial resists vs a same-level mob (no resistance gear)
SPELL_CRIT_BASE = 0.0091      # mage base spell crit before Intellect (Forever client PlayerExpectedStat: 0.9075%)
PUSHBACK_FIRST = 0.5          # seconds a melee hit adds to a cast (wowsims Forever: 500 ms per hit, never more than the cast time)
PUSHBACK_NEXT = 0.5           # same for further hits during the same cast
ROOT_BREAK_CHANCE = 0.20      # chance that a direct damage hit breaks a Frost Nova / Frostbite freeze early
FEAR_BREAK_CHANCE = 0.20      # chance that a damaging hit breaks a fear (Psychic Scream, Fear, Howl of Terror) early
GCD = 1.5

# player attacks vs a same-level mob (ElliotWood/Forever target.go attack table, level-60 attacker, defender at +0):
MELEE_MISS = 0.05             # yellow and single-weapon white miss
DW_MISS_PENALTY = 0.19        # extra white miss while dual wielding
RANGED_MISS = 0.05            # ranged attacks cannot be dodged, parried or glance
MOB_DODGE = 0.05
MOB_PARRY = 0.05              # only when attacking from the front (solo mobs face you)
GLANCE_CHANCE = 0.10          # white swings only; 0.95 damage vs a same-level mob (0.65 vs a +3 boss)
GLANCE_MULT = 0.95
MIN_RANGED_RANGE = 8.0        # bows and guns cannot fire inside this (wowsims Forever MinRangedRange)

# resources
ENERGY_PER_TICK = 20.0        # per 2-second tick (wowsims Forever: 20.2 per 2.02 s), 100 maximum
ENERGY_MAX = 100.0
RAGE_MAX = 100.0
RAGE_DECAY = 1.0              # rage lost per second out of combat (assumption; Classic decays it within a minute)


def rage_conversion(level):
    """Classic rage conversion value c(L) = 0.0091 L^2 + 3.23 L + 4.37 (230.9 at 60)."""
    return 0.0091 * level * level + 3.23 * level + 4.37


def rage_from_hit(amount, speed, hand, crit, level):
    """Classic rage from a white hit: 15 d / (4 c) + f s / 2 with hit factor f = 3.5 (main hand), 7 (main-hand crit),
    1.75 / 3.5 for the off-hand. The Forever simulator uses a flat 3.46 (one-hand) / 4.5 (two-hand) x speed per hit
    that it marks as untested at high levels; the Classic formula is kept here."""
    f = (7.0 if crit else 3.5) if hand == "mh" else (3.5 if crit else 1.75)
    return 15.0 * amount / (4.0 * rage_conversion(level)) + f * speed / 2.0


RAGE_PER_DAMAGE_TAKEN = 2.5   # Classic: rage from damage taken = 2.5 d / c(L); stored here as the numerator (engine divides by c)


# ------------------------------------------------------------------ pets and threat

PET_OOC_REGEN = 0.02          # fraction of maximum health a pet regains per 2-second tick out of combat (assumption)
PET_EAT_BELOW = 0.50          # feed / Mend Pet / Health Funnel the pet back to full below this fraction between fights
PET_RESUMMON_TIME = 12.0      # seconds to revive or re-summon a dead pet (10 s cast plus a shard / reagent)
THREAT_SWITCH = 1.30          # a mob leaves its pet for a ranged player once player threat exceeds 130% of the pet's (Classic aggro rule)


# ------------------------------------------------------------------ player: base stats and a "leveling greens" gear tier

# Level-60 base stats per class from the Forever beta client via the ElliotWood/Forever simulator (base_stats.go,
# ClassBaseStats / ExtraClassBaseStats / CritPerAgiMaxLevel / CritPerIntMaxLevel; Human race, no offsets). Levels 1-59 are
# interpolated from Classic level-1 values (~20 per stat, ~60 health, ~50-100 mana).
CLASS_BASE_60 = {
    #            str  agi  sta  int  spi   hp   mana  spell_crit  phys_crit  crit/agi  crit/int  ap_per_level_term
    "warrior": dict(strength=120, agility=80, stamina=110, intellect=30, spirit=45, health=1689, mana=0, spell_crit=0.0, phys_crit=1.14, crit_per_agi=0.0500, crit_per_int=0.0, ap_base=lambda L: 3.0 * L - 20),
    "paladin": dict(strength=105, agility=65, stamina=100, intellect=70, spirit=75, health=1381, mana=1512, spell_crit=3.3355, phys_crit=0.652, crit_per_agi=0.0506, crit_per_int=0.0167, ap_base=lambda L: 3.0 * L - 20),
    "hunter": dict(strength=55, agility=125, stamina=90, intellect=65, spirit=70, health=1467, mana=1720, spell_crit=3.602, phys_crit=-1.532, crit_per_agi=0.0189, crit_per_int=0.0165, ap_base=lambda L: 2.0 * L - 20),
    "rogue": dict(strength=80, agility=130, stamina=75, intellect=35, spirit=50, health=1523, mana=0, spell_crit=0.0, phys_crit=-0.295, crit_per_agi=0.0345, crit_per_int=0.0, ap_base=lambda L: 2.0 * L - 20),
    "priest": dict(strength=35, agility=40, stamina=50, intellect=120, spirit=125, health=1397, mana=1376, spell_crit=1.2375, phys_crit=3.183, crit_per_agi=0.0500, crit_per_int=0.0168, ap_base=lambda L: -10),
    "shaman": dict(strength=85, agility=55, stamina=95, intellect=90, spirit=100, health=1280, mana=1520, spell_crit=2.201, phys_crit=1.675, crit_per_agi=0.0508, crit_per_int=0.0169, ap_base=lambda L: 2.0 * L - 20),
    "mage": dict(strength=30, agility=35, stamina=45, intellect=125, spirit=120, health=1370, mana=1213, spell_crit=0.9075, phys_crit=3.4575, crit_per_agi=0.0514, crit_per_int=0.0168, ap_base=lambda L: -10),
    "warlock": dict(strength=45, agility=50, stamina=65, intellect=110, spirit=115, health=1414, mana=1373, spell_crit=1.70, phys_crit=2.00, crit_per_agi=0.0500, crit_per_int=0.0165, ap_base=lambda L: -10),
    "druid": dict(strength=65, agility=60, stamina=70, intellect=100, spirit=110, health=1483, mana=1244, spell_crit=1.8515, phys_crit=0.961, crit_per_agi=0.0500, crit_per_int=0.0167, ap_base=lambda L: -20),
}
# attack power per point of Strength / Agility (wowsims Forever class files: warrior/paladin/shaman/druid 2 per Str,
# rogue/hunter 1 per Str and 1 per Agi, hunter 2 ranged AP per Agi); dodge per Agility (wowsims: 1/20 for most, 1/25 hunter/shaman)
AP_PER_STR = {"warrior": 2, "paladin": 2, "shaman": 2, "druid": 2, "rogue": 1, "hunter": 1, "priest": 0, "mage": 0, "warlock": 0}
AP_PER_AGI = {"rogue": 1, "hunter": 1, "druid": 1, "warrior": 0, "paladin": 0, "shaman": 0, "priest": 0, "mage": 0, "warlock": 0}
RAP_PER_AGI = {"hunter": 2, "warrior": 1, "rogue": 1}
DODGE_PER_AGI = {"hunter": 1 / 25.0, "shaman": 1 / 25.0, "rogue": 1 / 14.5}   # others 1/20 (Classic: 20 Agility per 1% dodge at 60)

LEVEL1_STAT = 20.0
LEVEL1_HEALTH = 60.0
LEVEL1_MANA = 50.0


def class_base_stats(cls, level):
    """Base Strength/Agility/Stamina/Intellect/Spirit by level: level-60 client values interpolated from ~20 at level 1."""
    b = CLASS_BASE_60[cls]
    f = (level - 1) / 59.0
    return {k: LEVEL1_STAT + (b[k] - LEVEL1_STAT) * f for k in ("strength", "agility", "stamina", "intellect", "spirit")}


def class_base_health(cls, level):
    """Health before Stamina (10 health per Stamina on top): the client's level-60 value interpolated from 60 at level 1."""
    return LEVEL1_HEALTH + (CLASS_BASE_60[cls]["health"] - LEVEL1_HEALTH) * (level - 1) / 59.0


def class_base_mana(cls, level):
    """Mana before Intellect (15 mana per Intellect on top): the client's level-60 value interpolated from 50 at level 1."""
    m60 = CLASS_BASE_60[cls]["mana"]
    return 0.0 if m60 <= 0 else LEVEL1_MANA + (m60 - LEVEL1_MANA) * (level - 1) / 59.0


def class_spell_crit(cls, level, intellect):
    """Spell crit from base and Intellect: base% + crit_per_int * Int at 60 (the Int per 1% scales with level)."""
    b = CLASS_BASE_60[cls]
    per_int = b["crit_per_int"] * 60.0 / max(10.0, level) if b["crit_per_int"] else 0.0
    return b["spell_crit"] / 100 + intellect * per_int / 100


def class_melee_crit(cls, level, agility):
    """Melee/ranged crit from base and Agility: base% + crit_per_agi * Agi (per-Agi value scaled to level as for Intellect)."""
    b = CLASS_BASE_60[cls]
    per_agi = b["crit_per_agi"] * 60.0 / max(10.0, level)
    return max(0.0, b["phys_crit"] / 100 + agility * per_agi / 100)


def class_dodge(cls, level, agility):
    per = DODGE_PER_AGI.get(cls, 1 / 20.0) * 60.0 / max(10.0, level)
    return 0.03 + agility * per / 100   # ~3% base dodge plus Agility


def class_attack_power(cls, level, strength, agility):
    b = CLASS_BASE_60[cls]
    return max(0.0, b["ap_base"](level) + AP_PER_STR.get(cls, 0) * strength + AP_PER_AGI.get(cls, 0) * agility)


def class_ranged_ap(cls, level, agility):
    return max(0.0, CLASS_BASE_60[cls]["ap_base"](level) + RAP_PER_AGI.get(cls, 0) * agility)


def mage_base_stats(level):
    """Human mage base stats by level: level-60 values from the Forever beta client (Int 125, Spirit 120, Stamina 45,
    Agility 35; wowsims Forever base_stats.go, Human race offsets 0), interpolated from Classic level-1 values."""
    f = (level - 1) / 59.0
    return {"intellect": 22 + (125 - 22) * f, "spirit": 22 + (120 - 22) * f, "stamina": 20 + (45 - 20) * f, "agility": 20 + (35 - 20) * f}


def gear_stats(level, tier="leveling", cls="mage"):
    """Gear stats by level from the Classic 1.12 item database (`gear_stats.json`, built by gear_stats.py): every slot holds a typical
    good pick among the fixed-stat green items (GEAR_TIER "greens", mostly quest rewards) or the blue items ("blues") the class can wear,
    with required level 2-7 levels below the character (a mage at 40: Int 87, Spirit 66, Stamina 14; a warrior at 40: Str 86, Sta 79,
    armor 2,369 in plate). Spell power and healing come from the items' on-equip spells (spell_template auras 13 / 135; a
    school-specific bonus counts half). Classic items: unverified for WoW: Forever. GEAR_STAT_MULT scales the stats (sensitivity)."""
    t = GEAR_TIER if tier == "leveling" else tier
    if t not in _GEAR:
        raise ValueError(t)
    k = GEAR_STAT_MULT
    out = {st: interp(_gear_anchor(t, cls, st), level) * k for st in ("intellect", "spirit", "stamina", "agility", "strength")}
    out["armor"] = interp(_gear_anchor(t, cls, "armor"), level) * (1 + (k - 1) / 2)
    if any(row.get("spell_power") for row in _GEAR[t][cls].values()):   # from the items' on-equip spells (gear_stats.py)
        out["spell_power"] = interp(_gear_anchor(t, cls, "spell_power"), level) * k
        out["healing"] = interp(_gear_anchor(t, cls, "healing"), level) * k
    else:   # older gear_stats.json without item spells: the previous assumption
        sp = 2.2 if cls in ("mage", "priest", "warlock") else {"shaman": 1.2, "druid": 1.2, "paladin": 0.8}.get(cls, 0.0)
        out["spell_power"] = sp * max(0.0, level - 20) * k * (1.3 if t == "blues" else 1.0)
        out["healing"] = 0.0
    out["attack_power"] = 0.0
    return out


WEAPON_DPS_MULT = 1.0    # sensitivity knob on top of the item-database weapon dps
GEAR_STAT_MULT = 1.0     # sensitivity knob on top of the item-database gear stats
GEAR_TIER = "greens"     # "greens" (fixed-stat green items, mostly quest rewards) or "blues" (dungeon blues); see gear_stats.py
GEAR_TIERS = {"greens": {"GEAR_TIER": "greens"}, "blues": {"GEAR_TIER": "blues"}}
_GEAR = json.load(open(pathlib.Path(__file__).resolve().parent / "gear_stats.json", encoding="utf-8"))
_WEAPON_KIND = {"2h": "2h", "1h": "1h", "dagger": "dagger", "ranged": "ranged", "mace": "1h", "wand": "wand"}


def _gear_anchor(tier, cls, key):
    return [(int(L), row.get(key, 0.0)) for L, row in sorted(_GEAR[tier][cls].items(), key=lambda kv: int(kv[0]))]


def weapon_dps(level, kind="1h"):
    """Weapon dps by level from the Classic 1.12 item database (`gear_stats.json`): the median green (GEAR_TIER "greens") or blue
    ("blues") weapon of the kind with required level 2-7 levels below the character (greens: two-hand 15 at 20, 32 at 40, 49 at 60;
    one-hand and dagger 12 / 24 / 36; bow and gun 8 / 19 / 29). WEAPON_DPS_MULT scales it (sensitivity)."""
    wk = _WEAPON_KIND.get(kind, "1h")
    pts = [(int(L), row.get("dps", 0.0)) for L, row in sorted(_GEAR["weapons"][GEAR_TIER][wk].items(), key=lambda kv: int(kv[0])) if row.get("dps")]
    return interp(pts, level) * WEAPON_DPS_MULT


WEAPON_SPEED = {"2h": 3.4, "1h": 2.6, "dagger": 1.8, "ranged": 2.8, "mace": 2.5, "paw": 1.0}


def ammo_dps(level):
    """Arrows/bullets: 7.5 dps by 40, 13 dps at 60 (wowsims Forever ammo table 7.5-20.5; Classic vendor ammo)."""
    return interp([(1, 1.5), (10, 3.0), (25, 5.5), (40, 7.5), (50, 10.0), (60, 13.0)], level)


def wand_dps(level):
    """Wand dps by level from the Classic 1.12 item database (median green wand with required level 2-7 below the character:
    11 at 10, 17 at 20, 26 at 30, 33 at 40, 41 at 50, 55 at 60; blues 25 / 33 / 38 / 51 / 63 from 20)."""
    pts = [(int(L), row.get("dps", 0.0)) for L, row in sorted(_GEAR["weapons"][GEAR_TIER]["wand"].items(), key=lambda kv: int(kv[0])) if row.get("dps")]
    return interp(pts, level) * WEAPON_DPS_MULT


WAND_SPEED = 1.5


def base_mana(level):
    """Mana before Intellect: 1,213 at 60 for mages in the Forever client (PlayerExpectedStat); 15 mana per Intellect on top."""
    return 50 + (1213 - 50) * (level - 1) / 59.0


def base_health(level):
    """Health before Stamina: 1,370 at 60 for mages in the Forever client (wowsims Forever base_stats.go); 10 health per Stamina on top."""
    return 60 + (1370 - 60) * (level - 1) / 59.0


def mana_regen_tick(spirit):
    """Vanilla mage/priest mana regen per 2-second tick while not casting: 13 + Spirit / 4."""
    return 13 + spirit / 4.0


def class_mana_regen_tick(cls, spirit):
    """Classic mana regen per 2-second tick by class: mage/priest 13 + Spirit/4, warlock 8 + Spirit/4, druid/shaman/hunter/paladin 15 + Spirit/5."""
    if cls in ("mage", "priest"):
        return 13 + spirit / 4.0
    if cls == "warlock":
        return 8 + spirit / 4.0
    return 15 + spirit / 5.0


def health_regen_tick(spirit):
    """Out-of-combat health per 2-second tick (about a tenth of Spirit)."""
    return 0.1 * spirit + 1


def class_health_regen_tick(cls, spirit):
    """Classic out-of-combat health per 2-second tick by class: warrior 0.8 Spirit + 6, rogue 0.5 Spirit + 2, hunter/paladin
    0.25 Spirit + 6, druid 0.09 Spirit + 6.5, shaman 0.11 Spirit + 7, warlock 0.07 Spirit + 6, priest/mage 0.1 Spirit + 1."""
    return {"warrior": 0.8 * spirit + 6, "rogue": 0.5 * spirit + 2, "hunter": 0.25 * spirit + 6, "paladin": 0.25 * spirit + 6,
            "druid": 0.09 * spirit + 6.5, "shaman": 0.11 * spirit + 7, "warlock": 0.07 * spirit + 6}.get(cls, 0.1 * spirit + 1)


# ------------------------------------------------------------------ downtime: conjured water/food by level (mana or health per second)

def drink_rate(level):
    """Conjured water, Forever beta tooltips (Wowhead Forever items 5350/2288/2136/3772/8077/8078/8079, read 2026-09-26) at the
    Conjure Water rank levels 4/10/20/30/40/50/60: 145/18s, 420/21s, 803/24s, 1293/27s, 1915/30s, 2821/30s, 4038/30s mana."""
    return interp([(4, 145 / 18), (10, 420 / 21), (20, 803 / 24), (30, 1293 / 27), (40, 1915 / 30), (50, 2821 / 30), (60, 4038 / 30)], level)


def food_rate(level):
    """Conjured food, Forever beta tooltips (Wowhead Forever items 5349/1113/1114/1487/8075/8076/22895) at the Conjure Food rank
    levels 6/12/22/32/42/52/60: 59/18s, 234/21s, 531/24s, 841/27s, 1338/30s, 2065/30s, 3058/30s health."""
    return interp([(6, 59 / 18), (12, 234 / 21), (22, 531 / 24), (32, 841 / 27), (42, 1338 / 30), (52, 2065 / 30), (60, 3058 / 30)], level)


def bandage_heal(level):
    """First Aid bandage by level (Classic: Linen 66 at 1, Heavy Linen 114 at 10, Wool 161, Heavy Wool 301 at 20, Silk 400 at 30,
    Heavy Silk 640 at 35, Mageweave 800 at 40, Heavy Mageweave 1,104 at 45, Runecloth 1,360 at 50, Heavy Runecloth 2,000 at 55),
    healed over 8 s; 60 s Recently Bandaged cooldown. Used by classes without heals between fights."""
    return interp([(1, 66), (10, 114), (15, 161), (20, 301), (30, 400), (35, 640), (40, 800), (45, 1104), (50, 1360), (55, 2000), (60, 2000)], level)


DRINK_BELOW = 0.35      # start drinking after a fight when mana is below this fraction
EAT_BELOW = 0.65        # start eating when health is below this fraction (a cloth caster tops up early; 50% made a talentless mage die 80 times per 100 kills)
SIT_DOWN = 2.0          # seconds lost sitting/standing per eat-or-drink break
LOOT_TIME = 2.0         # seconds after each kill
TRAVEL_TIME = 6.0       # seconds to reach the next mob
DEATH_TIME = 90.0       # seconds lost per death (corpse run), then full health and mana
