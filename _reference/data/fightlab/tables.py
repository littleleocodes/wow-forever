"""Level tables the fight simulator assumes (Classic Era formulas and rules of thumb, stated so they can be argued with).

Everything here is an assumption unless a source is named. Beta measurements (kill times, mob health, drink rates)
should replace these numbers when they exist; each function says what it stands for. Mob health, damage, armor and the
caster share by level come from `mob_stats.json` (Classic 1.12 creature database, see `mob_stats.py`): data for Classic,
still an assumption for WoW: Forever.
"""
import json
import math
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
# Mob health by level (audit of 2026-10-18, row 71): "classic" = the Classic 1.12 creature database's median (the default); "expected" =
# the client's ExpectedStat creature health (EXPECTED_CREATURE_HEALTH below, build 70291: 1.35x the Classic median at 20, 1.24x at 30,
# 1.13x at 60). Whether the Forever server uses it is unknown: a sensitivity row, not the default.
MOB_HP_SHAPE = "classic"

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
    hp = interp(_HP, level) * MOB_HP_MULT
    if MOB_HP_SHAPE == "expected":
        L = max(1, min(63, int(round(level))))
        hp *= EXPECTED_CREATURE_HEALTH[L] / interp(_HP, L)
    return hp


def mob_melee_damage(level):
    """Median melee swing of a normal mob before armor, from the Classic 1.12 creature database (13 at 10, 32 at 20, 48 at 30, 68 at 40,
    95 at 50, 117 at 60 per 2.0 s swing; the earlier rule of thumb was 2-2.5x higher). Unverified for WoW: Forever."""
    return interp(_DMG, level) * MOB_DMG_MULT


def mob_armor(level):
    """Median armor of a normal mob from the Classic 1.12 creature database (450 at 10, 817 at 20, 1,200 at 30, 2,101 at 40, 2,999 at 50, 3,489 at 60)."""
    return interp(_ARMOR, level)


MOB_SWING = 2.0          # seconds between melee swings
# Vindication (paladin, 2026-11-09): the tooltip's level-60 attack power cut (204 at 3/3) comes off every mob swing as / 14 x MOB_SWING.
# How it scales below 60 is unknown: "mob" keeps the share of a mob's swing it has at 60 (the cautious reading: 29 of 188 at 60, 15%),
# "level" scales it by level / 60, "flat" uses 204 at every level (most of a level-20 mob's swing), "off" the lab before 2026-11-09.
VINDICATION_SCALE = "mob"
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
# Pets (2026-10-08): Forever's pets take stats from their owner, the client's own UI text (build 70291, Camelot/PaperDollFrame.lua and
# GlobalStrings): a hunter pet 10% of the higher attack power, 100% of the crit chance, 30% of the armor, 2 health per Stamina; a demon 17%
# of the warlock's spell damage as attack power, 10% as spell damage, 35% of the armor, 2 health per Stamina (client 70753; 7.5 from 70291 to 70707), 100% of the spell crit.
# A pet's damage per hit does not depend on its attack speed (the Faster Attack passives raise a 2.0 s base; forum logs at levels 20 and
# 30 put a 1.2 s cat 42% ahead of a 2.0 s pet), so a faster pet does more damage. Same rules as the raid simulator's patches.
PET_SCALING = 1.0        # sensitivity knob: scales every stat a pet inherits (0 = pets inherit nothing, the model before 2026-10-08)
HUNTER_PET_SPEED = 1.2   # the hunter pet's swing time in seconds (the 1.2 s cat of the level-20 forum log; 2.0 = the model before 2026-10-08)
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
    """White ranged/melee miss by level difference: 5% at +0, 5.5% at +1, 6% at +2, 8% at +3 (wowsims Forever attack table, as RANGED_MISS;
    until 2026-10-18 the table was one level off: 4% against a same-level mob, audit row 73)."""
    table = {0: 0.05, 1: 0.055, 2: 0.06, 3: 0.08}
    return table.get(max(0, min(3, level_diff)), 0.08) if level_diff >= 0 else 0.05


def armor_mitigation(armor, attacker_level):
    """Classic physical mitigation: armor / (armor + 400 + 85 * attacker level) for attackers under level 60."""
    if armor <= 0:
        return 0.0
    denom = armor + 400 + 85 * attacker_level
    return min(0.75, armor / denom)


def int_per_spell_crit(level):
    """Intellect per 1% spell crit for mages: the client's PlayerExpectedStat by level (59.5 at 60; 2026-10-09), else 59.5 x L / 60."""
    per = _per_stat("mage", level, 1)
    if per:
        return 1.0 / per
    return max(8.0, 59.5 * level / 60.0)


# Average damage lost to partial resists vs a same-level mob. 0 since 2026-10-18 (audit row 70): the raid simulator's resistance code gives
# a same-level target without resistance no partial resists (fork spell_resistances.go); the 2.5% had no source. Sensitivity row: 0.025.
PARTIAL_RESIST_LOSS = 0.0
# Spell hit cap: 1.0 since 2026-10-18 (audit row 73; the raid patch removed the 99% cap / 1% miss floor, CLAUDE.md audit of 2026-10-09).
SPELL_HIT_CAP = 1.0
HOT_CRIT = True               # heal-over-time ticks crit as the expected value (beta notes post 1; the healer lab's rule); False = never (before 2026-10-18)
SPELL_CRIT_BASE = 0.0091      # mage base spell crit before Intellect (Forever client PlayerExpectedStat: 0.9075%)
PUSHBACK_FIRST = 0.5          # seconds a melee hit adds to a cast (wowsims Forever: 500 ms per hit, never more than the cast time)
PUSHBACK_NEXT = 0.5           # same for further hits during the same cast
# A hit during a channel takes this share of the channel's full duration off its end (Classic and the raid simulator: 25%: Mind Flay 0.75 s,
# Drain Life 1.25 s, Blizzard 2 s; audit of 2026-10-18 row 70). 0 = the model before: PUSHBACK_FIRST / PUSHBACK_NEXT seconds per hit.
CHANNEL_PUSHBACK = 0.25
ROOT_BREAK_CHANCE = 0.20      # chance that a direct damage hit breaks a Frost Nova / Frostbite freeze early
FEAR_BREAK_CHANCE = 0.20      # chance that a damaging hit breaks a fear (Psychic Scream, Fear, Howl of Terror) early
GCD = 1.5
# Per-spell global cooldowns from the client data (audit of 2026-10-18 row 68): rogue abilities, cat-form abilities, totems and Hammer of
# Wrath are 1.0 s (`spell_gcd.json`, written by spell_gcd.py from the raid simulator's spell store, GCDMs). SPELL_GCD_TABLE = False
# restores 1.5 s for everything. Spells the store marks off the global cooldown are listed there but not applied (not checked per module).
SPELL_GCD_TABLE = True
_SPELL_GCD_FILE = pathlib.Path(__file__).resolve().parent / "spell_gcd.json"
_SPELL_GCD = json.load(open(_SPELL_GCD_FILE, encoding="utf-8")) if _SPELL_GCD_FILE.exists() else {"gcd": {}}   # missing: 1.5 s for all


def spell_gcd(cls, name):
    """The global cooldown a spell triggers, by class and spell name."""
    if SPELL_GCD_TABLE:
        v = _SPELL_GCD["gcd"].get(cls, {}).get(name)
        if v is not None:
            return v
    return GCD


# A rank's damage, healing and absorb grow with the caster's level up to the level its scaling stops at (the client's SpellLevels and
# EffectRealPointsPerLevel; audit of 2026-10-18 row 8): Shadow Bolt rank 4 deals 58 at 20 and 62 from 25. Our tooltips are the level-60
# text, so a rank read its capped amount at every level (casters about 4% high at 20-50). `spell_scaling.json` (spell_scaling.py, from the
# raid simulator's spell store) holds the rows; engine.scale_rank applies the factor in each module's rank_at. False = the model before.
RANK_LEVEL_SCALING = True
TOOLTIP_LEVEL = 60
_SCALING_FILE = pathlib.Path(__file__).resolve().parent / "spell_scaling.json"
_SCALING = json.load(open(_SCALING_FILE, encoding="utf-8"))["classes"] if _SCALING_FILE.exists() else {}


def _effect_amount(row, level):
    """effect.go Effect.Average: floor(base + (min(level, max level) - spell level) x gain); max level 0 = no cap."""
    base, gain, sl, ml = row
    lvl = min(level, ml) if ml > 0 else level
    return math.floor(base + max(0, lvl - sl) * gain)


def rank_level_factor(cls, name, rank_level, level):
    """{"direct", "periodic", "absorb"}: the rank's amount at `level` over its tooltip (level-60) amount, for each kind the rank has
    (a kind without a gain reads 1.0: Immolate's periodic part); {} when nothing scales at that level."""
    if not RANK_LEVEL_SCALING:
        return {}
    rec = _SCALING.get(cls, {}).get(name, {}).get(str(int(rank_level)))
    if not rec:
        return {}
    out = {}
    for kind in ("direct", "periodic", "absorb"):
        rows = rec.get(kind)
        if rows:
            at60 = sum(_effect_amount(r, TOOLTIP_LEVEL) for r in rows)
            if at60 > 0:
                out[kind] = sum(_effect_amount(r, level) for r in rows) / at60
    return out if any(abs(f - 1) > 1e-9 for f in out.values()) else {}

# player attacks vs a same-level mob (ElliotWood/Forever target.go attack table, level-60 attacker, defender at +0):
MELEE_MISS = 0.05             # yellow and single-weapon white miss
DW_MISS_PENALTY = 0.19        # extra white miss while dual wielding
RANGED_MISS = 0.05            # ranged attacks cannot be dodged, parried or glance
MOB_DODGE = 0.05
MOB_PARRY = 0.05              # only when attacking from the front (solo mobs face you)
GLANCE_CHANCE = 0.10          # white swings only; 0.95 damage vs a same-level mob (0.65 vs a +3 boss)
GLANCE_MULT = 0.95
MIN_RANGED_RANGE = 8.0        # bows and guns cannot fire inside this (wowsims Forever MinRangedRange)
AUTO_SHOT_STAND_STILL = 0.5   # Blizzard, 16 Oct beta notes: "Auto Shot now requires you to stand still for 0.5 seconds before shooting"

# resources
ENERGY_PER_TICK = 20.0        # per 2-second tick (wowsims Forever: 20.2 per 2.02 s), 100 maximum
ENERGY_MAX = 100.0
RAGE_MAX = 100.0
RAGE_DECAY = 1.25             # rage lost per second out of combat (the Forever client's rage tooltip, build 70291: "1.25 Rage is lost every 1 sec")


def rage_conversion(level):
    """Classic rage conversion value c(L) = 0.0091 L^2 + 3.23 L + 4.37 (230.9 at 60)."""
    return 0.0091 * level * level + 3.23 * level + 4.37


# Rage (2026-10-09): Forever's rules, as the raid simulator has them. Blizzard's Warrior deep dive (2026-09-30): "Rage from dealing
# damage: We have fully-normalized this Rage. Rage gained is now based on the speed of the weapon that dealt the damage"; the
# ElliotWood/Forever simulator fitted 3.46 rage per second of weapon speed one-handed and 4.5 two-handed from beta logs (fork commit
# f9f9f218; the off-hand half; nothing on a miss, dodge or parry), assumed the same at every level. Critical strikes double it
# ("increased to 100% increased Rage (was 75%)": warriors 2026-10-02, druids 2026-10-08). Rage from damage taken: the simulator's
# 10 x pre-armor damage / health, with the expected creature health of the client's ExpectedStat table (build 70291) instead of the
# player's (beta notes 2026-10-08: "Fixed a bug where the Rage calculation was incorrectly using the player's health ... instead of
# an expected creature's health"); the same notes rebalance an armor assumption "in the 20% to 40% range" without a number (not
# modelled). RAGE_MODEL = "classic" restores Classic's formulas (the model before 2026-10-09: 15 d / (4 c) + f s / 2 per white hit,
# 2.5 x pre-armor damage / c(L) taken, 1.0 decay).
RAGE_MODEL = "forever"
RAGE_HIT_1H = 3.46
RAGE_HIT_2H = 4.5
RAGE_CRIT_MULT = 2.0
RAGE_TAKEN_FACTOR = 10.0
EXPECTED_CREATURE_HEALTH = {
    1: 42, 2: 55, 3: 71, 4: 86, 5: 102, 6: 120, 7: 137, 8: 156, 9: 180, 10: 208, 11: 239, 12: 272,
    13: 307, 14: 345, 15: 385, 16: 427, 17: 473, 18: 521, 19: 572, 20: 629, 21: 677, 22: 731, 23: 787, 24: 846,
    25: 909, 26: 975, 27: 1040, 28: 1109, 29: 1177, 30: 1242, 31: 1308, 32: 1374, 33: 1443, 34: 1512, 35: 1586, 36: 1660,
    37: 1737, 38: 1814, 39: 1897, 40: 1981, 41: 2061, 42: 2146, 43: 2231, 44: 2317, 45: 2402, 46: 2495, 47: 2587, 48: 2681,
    49: 2779, 50: 2909, 51: 3040, 52: 3174, 53: 3317, 54: 3458, 55: 3602, 56: 3755, 57: 3909, 58: 4105, 59: 4234, 60: 4365,
    61: 4496, 62: 4629, 63: 4763,
}


def rage_from_hit(amount, speed, hand, crit, level, two_hand=False):
    """Rage from a landed white hit. Forever: (3.46 one-hand, 4.5 two-hand) x weapon speed, half for the off-hand, x2 on a crit.
    Classic (RAGE_MODEL = "classic"): 15 d / (4 c) + f s / 2 with f = 3.5 (main hand), 7 (main-hand crit), 1.75 / 3.5 off-hand."""
    if RAGE_MODEL == "classic":
        f = (7.0 if crit else 3.5) if hand == "mh" else (3.5 if crit else 1.75)
        return 15.0 * amount / (4.0 * rage_conversion(level)) + f * speed / 2.0
    base = RAGE_HIT_1H * speed * (0.5 if hand == "oh" else 1.0)
    r = base * (RAGE_HIT_2H / RAGE_HIT_1H if two_hand else 1.0)
    # a crit adds the one-handed swing's rage again, before the two-hander's factor (the fork's fit to Magey's beta logs, sim/core/rage.go
    # CritRageBonus; a two-hander's crit is 7.96 x speed, not 9.0: audit of 2026-10-18 row 18)
    return r + base * (RAGE_CRIT_MULT - 1.0) if crit else r


RAGE_PER_DAMAGE_TAKEN = 2.5   # Classic: rage from damage taken = 2.5 d / c(L) (RAGE_MODEL = "classic")


def rage_from_damage_taken(pre_armor, level):
    """Rage from a hit taken (pre-armor damage): Forever 10 x damage / the expected creature health at that level; Classic 2.5 d / c(L)."""
    if RAGE_MODEL == "classic":
        return pre_armor * RAGE_PER_DAMAGE_TAKEN / rage_conversion(level)
    return pre_armor * RAGE_TAKEN_FACTOR / EXPECTED_CREATURE_HEALTH[max(1, min(63, int(level)))]


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
# rogue/hunter 1 per Str and 1 per Agi, hunter 2 ranged AP per Agi; the druid 0 per Agility out of Cat Form: client ChrClasses
# AttackPowerPerAgility 0, Cat Form's "plus Agility" is applied by the form, audit of 2026-10-18 row 3); dodge per Agility (wowsims: 1/20 for most, 1/25 hunter/shaman)
AP_PER_STR = {"warrior": 2, "paladin": 2, "shaman": 2, "druid": 2, "rogue": 1, "hunter": 1, "priest": 0, "mage": 0, "warlock": 0}
AP_PER_AGI = {"rogue": 1, "hunter": 1, "druid": 0, "warrior": 0, "paladin": 0, "shaman": 0, "priest": 0, "mage": 0, "warlock": 0}
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


# Base mana by class and level from the client's PlayerExpectedStat BaseMana (build 70291; audit of 2026-10-18 row 70: the line from 50 at
# level 1 was 14-57% high at levels 10-20, exact at 60). BASE_MANA_TABLE = False restores the line.
BASE_MANA_TABLE = True


def _base_mana_row(cls, level):
    if not BASE_MANA_TABLE:
        return None
    return _PES_MANA.get(cls, {}).get(str(max(1, min(60, int(round(level))))))


def class_base_mana(cls, level):
    """Mana before Intellect (15 mana per Intellect on top): the client's BaseMana at the level (else the level-60 value on a line from 50)."""
    m60 = CLASS_BASE_60[cls]["mana"]
    if m60 <= 0:
        return 0.0
    row = _base_mana_row(cls, level)
    return float(row) if row is not None else LEVEL1_MANA + (m60 - LEVEL1_MANA) * (level - 1) / 59.0


# Crit per point of Agility and Intellect by class and level, the client's PlayerExpectedStat table (build 70291; 2026-10-09 audit:
# the level-60 value scaled by 60 / level was 15-30% off at level 20 for most classes, about 10% at 30, close from 40). Levels the
# table lacks fall back to the scaling. CRIT_PER_STAT_TABLE = False restores the scaling (the model before 2026-10-09).
_PES_ALL = json.load(open(pathlib.Path(__file__).resolve().parent / "player_expected_stat.json", encoding="utf-8"))
_PES = _PES_ALL["classes"]
_PES_MANA = _PES_ALL.get("base_mana", {})
CRIT_PER_STAT_TABLE = True


def _per_stat(cls, level, i):
    if not CRIT_PER_STAT_TABLE:
        return None
    row = _PES.get(cls, {}).get(str(int(round(level))))
    return row[i] if row else None


def class_spell_crit(cls, level, intellect):
    """Spell crit from base and Intellect: base% + the client's percent per Intellect at that level (else the level-60 value x 60 / L)."""
    b = CLASS_BASE_60[cls]
    if not b["crit_per_int"]:
        return b["spell_crit"] / 100
    per_int = _per_stat(cls, level, 1)
    if per_int is None:
        per_int = b["crit_per_int"] * 60.0 / max(10.0, level)
    return b["spell_crit"] / 100 + intellect * per_int / 100


def class_melee_crit(cls, level, agility):
    """Melee/ranged crit from base and Agility: base% + the client's percent per Agility at that level (else the level-60 value x 60 / L)."""
    b = CLASS_BASE_60[cls]
    per_agi = _per_stat(cls, level, 0)
    if per_agi is None:
        per_agi = b["crit_per_agi"] * 60.0 / max(10.0, level)
    return max(0.0, b["phys_crit"] / 100 + agility * per_agi / 100)


def class_dodge(cls, level, agility):
    per = DODGE_PER_AGI.get(cls, 1 / 20.0) * 60.0 / max(10.0, level)
    return 0.03 + agility * per / 100   # ~3% base dodge plus Agility


def class_attack_power(cls, level, strength, agility):
    b = CLASS_BASE_60[cls]
    return max(0.0, b["ap_base"](level) + AP_PER_STR.get(cls, 0) * strength + AP_PER_AGI.get(cls, 0) * agility) + GEAR_BONUS.get("attack_power", 0.0)


def class_ranged_ap(cls, level, agility):
    return max(0.0, CLASS_BASE_60[cls]["ap_base"](level) + RAP_PER_AGI.get(cls, 0) * agility) + GEAR_BONUS.get("attack_power", 0.0)


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
    for st, v in GEAR_BONUS.items():   # a character's gear against the typical set (characters/stat_weights.py); empty: no change
        if st in out:
            out[st] += v
    return out


WEAPON_DPS_MULT = 1.0    # sensitivity knob on top of the item-database weapon dps
# Stats added on top of the item-database gear (2026-11-09, the character gear planner, user: "optimizes the gear that I'm getting at each
# level"): gear_stats keys (intellect, spirit, stamina, agility, strength, armor, spell_power, healing, attack_power), "wand_dps" (wand_dps)
# and "mp5" (mana every 5 seconds, also inside the five-second rule; engine regen ticks). Empty: every result bit-identical.
GEAR_BONUS = {}
# Gear ratings and the stats the item-database gear lacks (2026-11-13, the gear add-on; user: "make sure all the stats are scored ... keep
# in mind caps for certain stats"): GEAR_BONUS keys crit_rating, hit_rating, haste_rating, expertise_rating, weapon_skill, defense_rating,
# dodge_rating, parry_rating, block_rating, block_value, mh_weapon_dps, oh_weapon_dps, ranged_weapon_dps (attack_power: class_attack_power and
# class_ranged_ap). Rating points per 1% are Forever's CombatRatings game table, the same at every level (_reference/forever-stats.md row 1);
# hit and crit are one stat for melee, ranged and spells (row 2). The caps come from the attack tables themselves: hit past a mob's miss
# chance, expertise past its dodge and parry, do nothing (row 3).
RATING_PER_PCT = {"crit_rating": 14.0, "hit_rating": 10.0, "haste_rating": 10.0, "expertise_rating": 10.0, "dodge_rating": 12.0,
                  "parry_rating": 15.0, "block_rating": 5.0}
DEFENSE_PER_POINT = 0.0004   # 0.04% per defense skill point: miss, dodge, parry and block up, crits taken down (the simulator's constant)
SKILL_PER_POINT = 0.001      # weapon skill above the mob's defense: 0.1% less miss, dodge and parry per point (Classic, gap under 10)
SKILL_CRIT_PER_POINT = 0.0004
# Spell Piercing (2026-11-13; wowsims/forever issue #76, 138 Forever combat logs, and the simulator's sim/core/spell_resistances.go): piercing
# past the target's resistance is bonus damage, on average P / (P + K) of the spell's damage with K = 8 x the caster's level + 19 (the logs'
# fit over levels 20-51; the simulator's since master 2026-11-13, 9L at our pin ff9babba5); a DoT's ticks take a tenth, channels the full
# bonus; Holy and physical damage take none. Mobs of
# your level have no resistance, so all of it is bonus. GEAR_BONUS "spell_penetration"; 0 = every result bit-identical.
PIERCE_K_PER_LEVEL, PIERCE_K_BASE = 8.0, 19.0
PIERCE_ON = __import__("os").environ.get("WOW_FL_PIERCE", "1") != "0"   # WOW_FL_PIERCE=0: no piercing bonus (the model before 2026-11-13)


def pierce_bonus(level, pts=None):
    """The average bonus damage of `pts` Spell Piercing (GEAR_BONUS's when None) at a caster level."""
    pts = GEAR_BONUS.get("spell_penetration", 0.0) if pts is None else pts
    return pts / (pts + PIERCE_K_PER_LEVEL * level + PIERCE_K_BASE) if pts > 0 and PIERCE_ON else 0.0


HASTE_GCD = False   # spell haste shortens the global cooldown (to 1.0 s)? Open: the simulator says yes, the client's Nature's Grace (its own
                    # global-cooldown modifier next to its haste) says no (_reference/forever-stats.md row 7). Not wired yet: a sensitivity.


def rating_pct(key):
    """A rating key of GEAR_BONUS as a fraction (0.01 = 1%)."""
    return GEAR_BONUS.get(key, 0.0) / RATING_PER_PCT[key] / 100.0


def apply_gear_ratings(p, mod):
    """Adds GEAR_BONUS's ratings to a player the module has made (engine.Session.run calls it only while GEAR_BONUS is set)."""
    crit = rating_pct("crit_rating")
    p.spell_crit += crit
    p.melee_crit += crit
    p.ranged_crit += crit
    hit = rating_pct("hit_rating")
    p.hit_bonus += hit
    p.spell_hit += hit
    p.expertise += rating_pct("expertise_rating")
    p.weapon_skill += GEAR_BONUS.get("weapon_skill", 0.0)
    p.spell_pierce_pts = getattr(p, "spell_pierce_pts", 0.0) + GEAR_BONUS.get("spell_penetration", 0.0)   # talents' (Arcane Subtlety) + gear
    p.spell_pierce = pierce_bonus(p.level, p.spell_pierce_pts)
    d = GEAR_BONUS.get("defense_rating", 0.0) * DEFENSE_PER_POINT
    p.mob_miss += d
    p.crit_taken_red += d
    p.dodge += d + rating_pct("dodge_rating")
    if p.parry > 0:
        p.parry += d + rating_pct("parry_rating")
    if p.block > 0:
        p.block += d + rating_pct("block_rating")
        p.block_value += GEAR_BONUS.get("block_value", 0.0)
    for w, key in ((p.mh, "mh_weapon_dps"), (p.oh, "oh_weapon_dps"), (p.ranged, "ranged_weapon_dps")):
        if w is not None and GEAR_BONUS.get(key):
            w.dps_bonus += GEAR_BONUS[key]
    h = rating_pct("haste_rating")
    if h and not getattr(mod, "_gear_haste", None):   # faster casts and swings (the module's own cast-time and swing-speed rules first)
        mod._gear_haste = h
        ct, sf = mod.cast_time, mod.swing_speed_factor
        mod.cast_time = lambda spell, _ct=ct, _h=h: _ct(spell) / (1.0 + _h)
        mod.swing_speed_factor = lambda _sf=sf, _h=h: _sf() / (1.0 + _h)
LEGACY_THRILL = 0.0   # Legacy perk Thrill of Adventure (2026-11-10, the character planner): the share of maximum health and mana a killing
                      # blow gives back (5 ranks: 0.05 over 10 s; outside dungeons; the lab gives it at once after the kill); 0 = off
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
    d = interp(pts, level) * WEAPON_DPS_MULT
    return d + GEAR_BONUS["wand_dps"] if "wand_dps" in GEAR_BONUS else d


WAND_SPEED = 1.5


def base_mana(level):
    """Mana before Intellect for mages: the client's PlayerExpectedStat BaseMana (1,213 at 60); 15 mana per Intellect on top."""
    row = _base_mana_row("mage", level)
    return float(row) if row is not None else 50 + (1213 - 50) * (level - 1) / 59.0


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
    """Conjured water (mana per second while drinking; unverified against the 70425 items, audit of 2026-10-18 row 73), Forever beta tooltips (Wowhead Forever items 5350/2288/2136/3772/8077/8078/8079, read 2026-09-26) at the
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
