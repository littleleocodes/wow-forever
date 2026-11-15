"""Duel lab constants (2026-11-14). Every number is an assumption with its reason; a Forever source replaces it when one is found
(_reference/pvp-research.md lists what is confirmed). Override from the command line with duel_run.py --set KEY=VALUE.
"""

DT = 0.05                 # time step (s): half the fight lab's, so a 0.3 s reaction and a 0.5 s pushback land on a step
START_DIST = 25.0         # yards between the two at the duel's start (a duel flag lands about 20-30 yards apart)
MAX_TIME = 300.0          # a duel still running after five minutes is a draw
MELEE = 5.0               # melee reach (yards), the fight lab's MELEE_RANGE
MIN_RANGED = 8.0          # bows and guns cannot fire inside this (the hunter's dead zone)
RUN_SPEED = 7.0           # yards per second, everyone's base run speed
STEALTH_SPEED = 0.7       # run speed share while stealthed (Classic's stealth slows; Camouflage and Feline Swiftness not counted)
REACTION = 0.35           # seconds a player needs to answer a new event: interrupt a cast, trinket a control, see a stealthed attacker

# Diminishing returns: Classic Era's categories (Forever is built on it), from DRList-1.0's "classic" section (github.com/wardz/
# DRList-1.0, Spells.lua at 82c200e, 2026-11-14; it has no Forever section and calls itself "mostly obsolete for Retail/Forever" since
# patch 12.0's own API): each application in a category within the reset of the last one lasts half as long, then a quarter, then the
# target is immune until the reset. Classic resets "between 15s and 20s" (DRList tracks 20); the middle is used. Forever's 2026-11-02
# notes: roots from procs diminish (Frostbite, Entrapment, Improved Wing Clip, Counterattack, Improved Hamstring), as random_root.
# Blind and Death Coil have no category (no diminishing returns), as in DRList.
DR_RESET = 17.5
DR_STEPS = (1.0, 0.5, 0.25, 0.0)
DR_CATEGORY = {
    # controlled stuns (Charge and Intercept share them in Classic); Kidney Shot has its own
    "Cheap Shot": "stun", "Hammer of Justice": "stun", "Bash": "stun", "Pounce": "stun", "Intimidation": "stun",
    "Concussion Blow": "stun", "War Stomp": "stun", "Charge": "stun", "Intercept": "stun",
    "Kidney Shot": "kidney_shot",
    # random stuns (procs)
    "Mace Stun Effect": "random_stun", "Impact": "random_stun", "Blackout": "random_stun", "Starfire Stun": "random_stun",
    "Improved Concussive Shot": "random_stun", "Seal of Justice": "random_stun", "Revenge Stun": "random_stun",
    "Stunning Blow": "random_stun", "Pyroclasm": "random_stun", "Shank": "random_stun",
    # incapacitates
    "Polymorph": "incap", "Sap": "incap", "Gouge": "incap", "Repentance": "incap", "Freezing Trap": "incap", "Wyvern Sting": "incap",
    "Scatter Shot": "incap", "Hibernate": "incap",
    # fears (Seduction is a fear here; its trinket mechanic is a charm, dtables.CHARM)
    "Fear": "fear", "Psychic Scream": "fear", "Howl of Terror": "fear", "Intimidating Shout": "fear", "Seduction": "fear",
    "Scare Beast": "fear",
    # roots
    "Frost Nova": "root", "Entangling Roots": "root", "Counterattack": "root", "Nature's Grasp": "root", "Feral Charge": "root",
    "Frostbite": "random_root", "Freeze": "random_root", "Improved Hamstring": "random_root", "Improved Wing Clip": "random_root",
    "Entrapment": "random_root",
    # no category: Blind, Death Coil (none in DRList's Classic list); silences are not diminished in Classic either
    "Blind": None, "Death Coil": None,
}
DR_DEFAULT = {"stun": "random_stun", "root": "random_root", "fear": "fear", "incap": "incap", "silence": None}   # set through the mob view
PVP_CC_CAP = 10.0         # control longer than this lasts this long on a player (TBC's rule; Polymorph, Sap, Fear, Seduction, traps)

# what damage does to control
FEAR_BREAK_CHANCE = 0.20  # each damaging hit (dots included) ends a fear with this chance (the fight lab's FEAR_BREAK_CHANCE)
ROOT_BREAK = {            # chance a damaging hit ends the root. Frost Nova: any damage (hotfix 2026-11-13 "Frost Nova now breaks on damage
    "Frost Nova": 1.0,    # from procs and Blizzard"; its tooltip: "Damage caused may interrupt the effect"); Frostbite's freeze: the user
    "Frostbite": 1.0,     # saw Ice Lance end it (2026-11-14); Entangling Roots: Classic's chance, an assumption; Improved Hamstring and the
    "Entangling Roots": 0.3,  # hunters' proc roots hold
}
ROOT_BREAK_PERIODIC = {"Frost Nova"}   # roots that dots break too (the 11-13 hotfix); others break on direct hits only
BREAKS_ON_DAMAGE = {"Polymorph", "Sap", "Gouge", "Blind", "Repentance", "Freezing Trap", "Wyvern Sting", "Seduction", "Scatter Shot"}

# The PvP trinket: one per class, rank 2 of the honor ranks, 5-minute cooldown, and each class's breaks different control (the client's
# spell effects, read 2026-11-14 in builds 70888 and 70938: _reference/pvp-research.md). Mechanics: stun, root, slow, fear, charm
# (Seduction), polymorph (Polymorph only: Sap, Gouge, Blind and traps are other mechanics).
TRINKET_CD = 300.0
TRINKET = True            # off: nobody has one (a fresh 60)
TRINKET_BREAKS = {
    "warrior": {"stun", "root", "slow"}, "hunter": {"stun", "root", "slow"}, "shaman": {"stun", "root", "slow"},
    "rogue": {"charm", "fear", "polymorph"}, "warlock": {"charm", "fear", "polymorph"},
    "mage": {"fear", "polymorph", "slow"},
    "paladin": {"fear", "polymorph", "stun"}, "priest": {"fear", "polymorph", "stun"},
    "druid": {"charm", "fear", "stun"},
}
CHARM = {"Seduction"}     # incapacitates whose mechanic is a charm
PROC_NAME = {("mage", "root"): "Frostbite", ("warrior", "root"): "Improved Hamstring", ("hunter", "root"): "Entrapment",
             ("warrior", "stun"): "Mace Stun Effect", ("mage", "stun"): "Impact", ("priest", "stun"): "Blackout",
             ("paladin", "stun"): "Seal of Justice", ("druid", "stun"): "Starfire Stun"}
HEALING_POTIONS = False   # consumables are off by default (a duel flag allows them; a fair build comparison does not)

# healing reduction debuffs (name: fraction of healing taken away)
HEAL_REDUCTION = {"Mortal Strike": 0.5, "Wound Poison": 0.1, "Aimed Shot": 0.0, "Hamstring": 0.0}
WOUND_STACKS = 5

# gear: the fight lab's level-60 tier for both sides (blues: dungeon blues). A PvP rank set is planned (pvp-plan.md).
GEAR_TIER = "blues"
