"""Healer lab assumptions: the encounter one raid healer is responsible for, the healer's raid stats and consumables.

Everything here is an assumption with a knob (sensitivity rows in the reports), stated so it can be argued with. The spells,
their ranks, costs, cast times and coefficients come from the beta spellbook (`forever-spells/<class>.json`); talent numbers
from the beta tooltips (`scorer/effects/forever/<class>.parsed.json`) plus the mechanics each class module hand-codes.
"""
import importlib.util
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
_spec = importlib.util.spec_from_file_location("fightlab_tables", HERE.parent / "fightlab" / "tables.py")   # same file name: load by path
_FL = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_FL)
class_base_mana, class_base_stats, class_mana_regen_tick, class_spell_crit = _FL.class_base_mana, _FL.class_base_stats, _FL.class_mana_regen_tick, _FL.class_spell_crit

DURATION = 300.0          # seconds: a five-minute boss fight
DT = 0.1                  # simulation step
LEVEL = 60

# ---- the group this healer keeps alive: one tank taking boss melee, four raid members taking periodic raid damage
TANK_HP = 9000.0          # a phase-1 warrior tank (Classic: ~8-10k raid buffed)
RAID_HP = 4500.0          # a raid member
TANK_ARMOR_MIT = 0.55     # physical damage the tank's armor removes vs a level-63 boss (~7,000 armor)
TANK_AVOID = 0.30         # boss swings that miss, are dodged, parried or blocked away entirely (block counted as avoidance)
BOSS_SWING = 2.0          # seconds between boss melee swings
BOSS_DMG = 2600.0         # boss swing before armor (Classic MC/BWL trash-to-boss range; scaled by the capacity search anyway)
BOSS_DMG_SPREAD = 0.25    # +-25%
CRUSH_CHANCE = 0.15       # crushing blows (x1.5) vs a tank without the defense cap
CRUSH_MULT = 1.5
SPIKE_EVERY = 30.0        # a boss ability on the tank (Mortal Strike-like) this often
SPIKE_MULT = 2.0          # ... hitting for this many swings (after armor)
RAID_PULSE_EVERY = 20.0   # raid-wide damage (an AoE, a fire patch) every so often, +-RAID_PULSE_JITTER
RAID_PULSE_JITTER = 6.0
RAID_PULSE_DMG = 700.0    # per raid member, +-30%
RAID_PULSE_SPREAD = 0.30
HEALER_SHARE = 1.0        # multiplier on every incoming damage stream: the part of the raid's damage this healer must cover
DEATH_RUNS_OK = 0.10      # capacity = the damage multiplier at which no more than this fraction of runs sees a death

# ---- the healer at 60 in phase-1 raid gear (assumptions per class; the beta client's base stats come from the fight lab tables)
HEALER_GEAR = {
    "priest": {"intellect": 230, "spirit": 200, "healing": 380, "mp5": 12, "crit_gear": 0.02},
    "paladin": {"intellect": 260, "spirit": 130, "healing": 360, "mp5": 24, "crit_gear": 0.02},
    "shaman": {"intellect": 250, "spirit": 150, "healing": 360, "mp5": 20, "crit_gear": 0.02},
    "druid": {"intellect": 230, "spirit": 190, "healing": 370, "mp5": 12, "crit_gear": 0.02},
}
GEAR_KEYS = ("intellect", "spirit", "healing", "mp5", "crit_gear")


def use_gear(cls, stats):
    """Replace the class's assumed gear above with a real set's summed item and enchant stats (heallab/heal_gear.py `gear_stats`;
    run.py --gear-json; 2026-10-15). Without a call the defaults above stand, bit-identical."""
    HEALER_GEAR[cls] = {k: stats[k] for k in GEAR_KEYS}


def _top_rank_value(cls, spell, pattern, default):
    """The number `pattern` finds in the top rank of a spell in the beta spellbook (forever-spells/<cls>.json); `default` if missing."""
    import json
    import re
    data = json.load(open(HERE.parent / "forever-spells" / f"{cls}.json", encoding="utf-8"))
    for tab in data["tabs"]:
        for sp in tab["spells"]:
            if sp["name"] == spell and sp["ranks"]:
                m = re.search(pattern, (sp["ranks"][-1].get("text") or "").replace("\n", " "))
                if m:
                    return float(m.group(1).replace(",", ""))
    return default


# Raid buffs at their top rank in the beta spellbook (2026-10-18, audit 2 row 72: Mark of the Wild had Classic's 12, Blessing of Wisdom
# Classic's 33 mp5; Forever: 16 and 40)
RAID_BUFF_INT = _top_rank_value("mage", "Arcane Intellect", r"Intellect by (\d+)", 31)       # Arcane Intellect (31)
RAID_BUFF_STATS = _top_rank_value("druid", "Mark of the Wild", r"all attributes by (\d+)", 16)   # Mark of the Wild, all stats (16)
RAID_BUFF_SPIRIT = _top_rank_value("priest", "Divine Spirit", r"Spirit by (\d+)", 40)        # Divine Spirit, a priest in the raid (40)
KINGS = 1.10              # Blessing of Kings (+10% stats); 1.0 for a Horde raid
WISDOM_MP5 = _top_rank_value("paladin", "Blessing of Wisdom", r"restoring (\d+) mana every 5 sec", 40)   # Blessing of Wisdom (rank 6, 40 mp5)
MANA_PER_INT = 15.0
CRIT_MULT = 1.5           # a critical heal
# Heals over time whose ticks can crit (Blizzard's beta notes, 2026-09-24, post 1: "Corrected an issue and now Rejuvenation / Tranquility /
# Wild Growth / Renew / Riptide can land critical hits"; Regrowth is not named). Every tick carries the expected bonus, crit chance at the
# cast x (CRIT_MULT - 1) (engine.Sim.land; 2026-10-17, page audit finding 14: only Renew had it, in the priest module); a tick crit
# triggers no on-crit effect (Divine Aegis: "non-periodic critical heals"; Water Shield, Nature's Grace, Illumination read direct crits).
HOT_CRIT = ("Renew", "Rejuvenation", "Wild Growth", "Tranquility", "Riptide")
REGEN_TICK = 2.0          # spirit regen ticks every 2 s
FSR = 5.0                 # five-second rule: no spirit regen within 5 s of a cast (talents return a fraction)
GCD = 1.5
POTION_EVERY = 120.0      # Major Mana Potion cooldown
POTION_MANA = 1800.0      # 1,350-2,250
POTION_FIRST = 45.0       # first potion once mana is under POTION_BELOW and this much time has passed
POTION_BELOW = 0.65       # fraction of maximum mana
POTIONS = True
DOWNRANK = True           # cast the lowest rank that covers the deficit (Classic healing practice); False = max rank always
DOWNRANK_PENALTY = True   # Forever: ranks far below your level get less from healing power (2026-10-09; engine.downrank_multiplier); False = the old full coefficients
HOT_REFRESH_DEFICIT = 0.10   # keep a HoT on the tank while it is missing more than this fraction of its health
EMERGENCY = 0.35          # a target under this fraction of health gets the fastest big heal available
RAID_HEAL_AT = 0.70       # a raid member under this fraction gets healed
GROUP_HEAL_MIN = 3        # hurt raid members needed for a group heal


def apply_rotation(cls):
    """Tuned heal-choice settings of this class's healer (heallab/rotation_opt.py, rotations/<class>-<spec>.json), applied to this
    module's globals before a run; WOW_HL_ROTATION=default keeps the defaults above. Returns what was applied."""
    import json
    import os
    if os.environ.get("WOW_HL_ROTATION") == "default":
        return {}
    applied = {}
    for p in sorted((HERE / "rotations").glob(f"{cls}-*.json")):
        for k, v in (json.load(open(p, encoding="utf-8")).get("tables") or {}).items():
            globals()[k] = v
            applied[k] = v
    return applied
