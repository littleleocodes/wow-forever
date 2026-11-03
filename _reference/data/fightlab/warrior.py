"""Warrior module for the fight lab (Arms two-hander, Fury dual wield and Protection sword and board leveling).

Spell ranks are read from `_reference/data/forever-spells/warrior.json` (beta client build 1.60.1.70291); talent numbers from
each rank's tooltip in `_reference/data/forever-talents/warrior.json`. Weapon damage uses a quest-green two-hander (Arms) or two
one-handers (any spec string starting with "fury") by level (`tables.weapon_dps`), attack power from the client's base stats and
the class's 2 AP per Strength. A spell is cast only in the stances its spellbook entry requires (STANCES, from the beta client's
"Requires ... Stance"): the Arms and Fury playstyles fight in Battle Stance, so Whirlwind, Berserker Rage, Pummel, Intercept and
Recklessness (Berserker Stance) are never cast.

Playstyle `arms-2h-raid` (the scorer's model id, used for leveling; `fury-dw-raid` the same priority with Bloodthirst and two
weapons): Bloodrage and Charge on the pull (Death Wish too when the build has it), Battle Shout kept up, Victory Rush after a
kill, Mortal Strike or Bloodthirst on cooldown, Overpower after a dodge (or a Bloodthrill proc), Rend once, Execute under 20%,
Heroic Strike with spare rage; Sweeping Strikes when a second mob stands in reach. Between fights: a bandage below 60% health
(First Aid, 60 s cooldown), food below `eat_below` (the tuned rules in rotations/ set it: 50% Arms, 40% Fury since 2026-10-19).

Playstyle `prot-leveling` (any spec string starting with "prot"): sword and board in Defensive Stance, see `decide_prot` and
PROT_NOTES below. Every other spec string runs exactly as before (the shield code is behind `self.prot`).

2026-10-09 (70291 review): Rend is a bleed with no direct hit (its "bleed for N damage" had been read as a hit as well) plus
Forever's 2% of attack power a tick, with Improved Rend on the bleed; Bloodthirst keeps its flat damage; Revenge and Thunder Clap
take Forever's attack power shares (FOREVER_AP); Two-Handed Weapon Specialization only with a two-hander; Dual Wield
Specialization (off-hand damage and rage), Furious Precision (off-hand hit), Gore Drinker and Sweeping Strikes are simulated;
Unbridled Wrath gives 1 rage on either hand (white swings only since 2026-10-18); Bloodthrill triggers on every main-hand attack; Blood Craze no longer triggers on
Bloodthirst; Deep Wounds rolls the main hand's average weapon damage without attack power; Flurry charges go on either hand's
landed white swings; Death Wish adds 5% damage taken; Thunder Clap never crits.

2026-10-18 (audit 2026-10-18 #6, #17, #25, #28): Slam is cast with Improved Slam (shorter cast and global cooldown, the swing keeps
running, 3 s off the cooldown; plain Slam stops and resets the swing and is left out of the hand-written priority); Spearing Strike
(40% weapon damage) is cast; Concussion Blow stuns (its "Stuns the target for 5 sec." was never parsed); Unbridled Wrath procs from
white swings only; Bloodthrill's Overpower window is the dodge's 5 s; Bloodrage's trickle pays every second it owes and takes
Improved Bloodrage's +50%.

2026-11-03 (Blizzard's notes of 2026-11-02, client 1.60.1.70753; numbers from the tooltips of talentsforever.com's 2026-11-03 export):
Reckless Swings (new, Fury row 4: 25% of base health, the next 4 melee attacks within 8 s give 5 more rage, 15 s cooldown) is cast off the
global cooldown while the warrior has health and the mob has health left (RECKLESS_ABOVE, RECKLESS_MOB, rotation knobs); Improved Whirlwind
(new, row 6: Whirlwind's cooldown -1/-2 s and +15/30% to the closest enemy) is in the hooks, but the Battle Stance and Defensive Stance
playstyles never cast Whirlwind (Berserker Stance); Flurry 10/20/30% in 3 ranks without Death Wish; Two-Handed Weapon Specialization
2/4/6%; Slam's cooldown 15 s and Improved Slam's -2.5/-5 s; Bloodthrill 10/20% in 2 ranks; Improved Tactical Mastery 5/10/15 rage;
Booming Voice also cuts Piercing Howl (not cast); Defensive Stance's 80% threat, Defiance and the threat of Blood Craze and Gore Drinker do
nothing here (threat is not modelled for a lone warrior).
"""
import json
import pathlib
import re

import tables
from engine import parse_interrupt, BaseModule, Player, Spell, Weapon
from tables import (GCD, MELEE_RANGE, WEAPON_SPEED, bandage_heal, class_attack_power, class_base_health, class_base_stats, class_dodge,
                    class_health_regen_tick, class_melee_crit, gear_stats, interp, weapon_dps)

ROOT = pathlib.Path(__file__).resolve().parents[3]
SPELLBOOK = json.load(open(ROOT / "_reference/data/forever-spells/warrior.json", encoding="utf-8"))
TREE = json.load(open(ROOT / "_reference/data/forever-talents/warrior.json", encoding="utf-8"))

NUM = re.compile(r"(\d+(?:\.\d+)?)")
PLUS = re.compile(r"(?:melee damage by|weapon damage plus) (\d[\d,]*)")
FLAT = re.compile(r"causing (\d[\d,]*) damage|for (\d[\d,]*) damage|doing (\d[\d,]*) damage")
RANGE = re.compile(r"(\d[\d,]*) to (\d[\d,]*) damage")
BLEED = re.compile(r"bleed for (\d[\d,]*) damage over (\d+) sec")
EXECUTE = re.compile(r"causing (\d[\d,]*) damage and converting each extra point of rage into (\d+) additional damage")
CHARGE = re.compile(r"generate (\d+) Rage, and Stun it for (\d+) sec")
SHOUT = re.compile(r"melee attack power of all party (?:or raid )?members[^.]*? by (\d+)")   # 70425: "all party or raid members" (16 Oct: raid wide)
SLOW = re.compile(r"slowing the enemy's movement by (\d+)% for (\d+) sec")
AP_PCT = re.compile(r"(\d+)% of (?:your )?Attack Power")
AP_PLUS = re.compile(r"of (?:your )?Attack Power plus (\d[\d,]*)")   # Bloodthirst: "45% of your Attack Power plus 48"
WPCT = re.compile(r"deals (\d+)% weapon damage")   # Spearing Strike: "A brutal attack that deals 40% weapon damage." (audit 2026-10-18 #6)
STUN = re.compile(r"(?:Stuns the target|stunning it) for (\d+) sec")   # Concussion Blow: "Stuns the target for 5 sec." (audit 2026-10-18 #28: never parsed); Intercept: "stunning it for 3 sec" (lint)
RECKLESS = re.compile(r"next (\d+) melee attacks generate (\d+) additional Rage\. Lasts (\d+) sec")   # Reckless Swings (70753)
# Attack power shares Forever adds that the client rows do not carry, as the community raid simulator fits them to beta logs
# (ElliotWood/Forever sim/warrior rend.go, revenge.go, thunder_clap.go): Rend 0.02 of attack power a tick, Revenge 0.25, Thunder
# Clap 0.0255 (fitted below level 20; the same share at 60 is assumed there too).
FOREVER_AP = {"Rend": ("tick", 0.02), "Revenge": ("hit", 0.25), "Thunder Clap": ("hit", 0.0255)}

TALENT_SPELLS = {"Mortal Strike": "Mortal Strike", "Sweeping Strikes": "Sweeping Strikes", "Piercing Howl": "Piercing Howl", "Death Wish": "Death Wish",
                 "Bloodthirst": "Bloodthirst", "Concussion Blow": "Concussion Blow", "Last Stand": "Last Stand", "Shield Slam": "Shield Slam",
                 "Spearing Strike": "Spearing Strike", "Reckless Swings": "Reckless Swings"}
NEXT_SWING = {"Heroic Strike", "Cleave"}


def _num(s):
    return float(s.replace(",", ""))


def _seconds(s):
    m = re.search(r"([\d.]+)\s*(sec|min)", s or "")
    if not m:
        return 0.0
    return float(m.group(1)) * (60 if m.group(2) == "min" else 1)


def load_spellbook():
    book = {}
    for tab in SPELLBOOK["tabs"]:
        for sp in tab["spells"]:
            for r in sp["ranks"]:
                txt = (r.get("text") or "").replace("\n", " ")
                cost_txt = r.get("cost") or ""
                cost = _num(NUM.search(cost_txt).group(1)) if NUM.search(cost_txt) else 0.0
                cast_txt = (r.get("cast") or "").lower()
                cast = 0.0 if "instant" in cast_txt or not cast_txt else _seconds(cast_txt)
                name = sp["name"]
                s = Spell(name=name, school="physical", rank=int(NUM.search(r.get("rank") or "1").group(1)) if NUM.search(r.get("rank") or "") else 1,
                          level=int(r.get("level") or 1), cost=cost, cast=cast, cooldown=_seconds(r.get("cooldown")), range=5.0,
                          kind="melee", resource="rage")
                s.text = txt
                s.interrupt = parse_interrupt(txt)
                pl, fl, rg, bl, ex, ch, sh, sl, ap = (rx.search(txt) for rx in (PLUS, FLAT, RANGE, BLEED, EXECUTE, CHARGE, SHOUT, SLOW, AP_PCT))
                if name in NEXT_SWING:
                    s.on_next_swing = True
                if pl:
                    s.weapon_pct, s.dmg_min, s.dmg_max = 1.0, _num(pl.group(1)), _num(pl.group(1))
                elif ex:
                    s.dmg_min = s.dmg_max = _num(ex.group(1))
                    s.rage_dmg = float(ex.group(2))
                elif rg:
                    s.dmg_min, s.dmg_max = _num(rg.group(1)), _num(rg.group(2))
                elif fl and not bl:   # Rend's "bleed for N damage over T sec" is the bleed, not a hit as well
                    s.dmg_min = s.dmg_max = _num(fl.group(1) or fl.group(2) or fl.group(3))
                if ap:
                    s.coef = float(ap.group(1)) / 100   # attack power coefficient (Bloodthirst, Victory Rush)
                    apf = AP_PLUS.search(txt)
                    if apf:   # Bloodthirst's flat part ("... of your Attack Power plus 48")
                        s.dmg_min = s.dmg_max = _num(apf.group(1))
                if bl:
                    s.dot, s.dot_dur = _num(bl.group(1)), float(bl.group(2))
                    s.dot_ticks = max(1, int(round(s.dot_dur / 3.0)))
                if name in FOREVER_AP:
                    how, share = FOREVER_AP[name]
                    if how == "tick":
                        s.dot_coef = share   # engine.apply_periodic: (dot + dot_coef x attack power x ticks)
                    else:
                        s.coef = share
                if name == "Whirlwind":
                    s.weapon_pct = 1.0
                wp = WPCT.search(txt)
                if wp and not pl:   # Spearing Strike's 40% (its extra 80% against Giants, Dragonkin and mounted targets: no leveling mob here)
                    s.weapon_pct = float(wp.group(1)) / 100
                st = STUN.search(txt)
                if st and not ch:
                    s.stun = float(st.group(1))
                if ch:
                    s.kind, s.charge, s.charge_rage, s.stun, s.resource = "buff", True, float(ch.group(1)), float(ch.group(2)), "none"
                if sh:
                    s.kind, s.ap = "buff", _num(sh.group(1))
                if sl:
                    s.daze, s.chill_dur = float(sl.group(1)) / 100, float(sl.group(2))
                if name in ("Bloodrage", "Berserker Rage", "Battle Stance", "Berserker Stance", "Defensive Stance", "Retaliation", "Recklessness",
                            "Death Wish", "Last Stand", "Shield Wall", "Shield Block", "Sweeping Strikes", "Battle Shout", "Demoralizing Shout", "Intimidating Shout",
                            "Challenging Shout", "Taunt", "Piercing Howl"):
                    s.kind = "buff"
                    if name in ("Bloodrage", "Berserker Rage", "Retaliation", "Recklessness", "Last Stand", "Shield Wall"):
                        s.resource = "none"
                if name == "Victory Rush":
                    s.resource = "none"
                hc = re.search(r"(\d+)% of base health", cost_txt)   # Reckless Swings (70753): "25% of base health"
                if hc:   # Reckless Swings: paid in health (a share of the class's base health at the level: mana_cost)
                    s.kind, s.resource, s.health_pct = "buff", "health", float(hc.group(1)) / 100
                rk = RECKLESS.search(txt)
                if rk:
                    s.reckless = (int(rk.group(1)), float(rk.group(2)), float(rk.group(3)))
                book.setdefault(name, []).append(s)
    for name in book:
        book[name].sort(key=lambda x: (x.level, x.rank))
    return book


BOOK = load_spellbook()

STANCE_NAMES = ("Battle Stance", "Berserker Stance", "Defensive Stance")


def load_stances():
    """{spell: the stances it can be cast in} from the beta spellbook's "requires" field ("Requires Battle Stance, Berserker Stance";
    "Requires Defensive Stance; Requires Shields"); spells without a stance requirement are absent."""
    out = {}
    for tab in SPELLBOOK["tabs"]:
        for sp in tab["spells"]:
            for r in sp["ranks"]:
                st = {s for s in STANCE_NAMES if s in (r.get("requires") or "")}
                if st:
                    out.setdefault(sp["name"], set()).update(st)
    return out


STANCES = load_stances()
WHITE = ("Melee", "Melee (off-hand)")   # the engine's auto attack placeholders (engine.Fight.auto_swing)
NOT_WEAPON_ATTACK = {"Thunder Clap", "Shield Slam", "Shield Bash"}   # damage that is not a main-hand weapon attack (Bloodthrill, Gore Drinker)
NO_CRIT = {"Thunder Clap", "Rend", "Concussion Blow"}   # Thunder Clap rolls on the spell table and warriors have no spell crit (raid
                                                        # simulator, beta logs: 0 of 799 claps crit); Rend's application and
                                                        # Concussion Blow deal no damage, so their roll is no crit either
NO_SWEEP = {"Execute", "Thunder Clap", "Whirlwind", "Cleave", "Rend", "Concussion Blow"}   # Sweeping Strikes: area attacks hit more
                                                        # mobs on their own; Execute's copy is only a weapon hit in the raid simulator; no damage, no copy
SHOUTS = {"Battle Shout", "Demoralizing Shout", "Challenging Shout", "Intimidating Shout"}   # Booming Voice's rage cost cut
SWEEP_CHARGES = int(NUM.search(BOOK["Sweeping Strikes"][-1].text).group(1))   # "Your next 5 melee attacks strike an additional nearby opponent."
SWEEP_DURATION = 20.0   # the client's duration of 12292 (the raid simulator's spell data: DurationMs 20000); the tooltip gives none
OVERPOWER_WINDOW = 5.0  # a dodge's Overpower window (the client's Offensive State aura 1282733, 5 s); Bloodthrill's too since 2026-10-18
                        # (its 6 s came from no 70425 text: the tooltip names no window; audit 2026-10-18 #25)
GORE = Spell("Gore Drinker", "physical", kind="buff", resource="none")   # healing bookkeeping for Gore Drinker


def talent_numbers():
    out = {}
    for tr in TREE["trees"]:
        for t in tr["talents"]:
            out[t["name"]] = [[float(x) for x in NUM.findall((rank or "").replace(",", ""))] for rank in t["ranks"]]
    return out


TNUM = talent_numbers()

MECHANICS = {
    "Improved Heroic Strike": "-1 rage/rank Heroic Strike",
    "Deflection": "+1%/rank parry",
    "Improved Rend": "+11.7%/rank Rend bleed",
    "Improved Charge": "+3 rage/rank on Charge",
    "Improved Tactical Mastery": "+5 rage/rank kept through a stance change (sword and board: the swap back after Charge; 70753, 3 a rank before)",
    "Improved Overpower": "+25%/rank Overpower crit",
    "Anger Management": "+1 rage per 3 s in combat",
    "Deep Wounds": "crits bleed 20%/rank of the main hand's average weapon damage over 12 s (no attack power; a crit on a running bleed adds what it still owed)",
    "Spearing Strike": "40% weapon damage instant, 15 rage, 20 s cooldown (its extra 80% against Giants, Dragonkin and mounted targets: no leveling mob here)",
    "Two-Handed Weapon Specialization": "+2%/rank damage with a two-hander (nothing with one-handers; 70753, 1% before)",
    "Impale": "+10%/rank ability crit damage bonus",
    "Bloodthrill": "10%/rank (2 ranks, 70753; 4%/rank of 5 before) per main-hand attack (white or ability) on a Rended mob: Overpower usable for 5 s "
                   "(the dodge window; the tooltip names no other)",
    "Sweeping Strikes": "pulls of several mobs: the next 5 melee attacks (20 s) also hit a second mob; 30 rage, Battle Stance, off the global cooldown",
    "Weaponmaster": "axe/polearm: +1%/rank crit (assumed weapon type)",
    "Improved Slam": "-0.25 s/rank Slam cast and global cooldown, Slam no longer stops the swing timer, -2.5 s/rank Slam cooldown (70753; Slam: weapon plus N, 1.5 s "
                     "cast, 15 s cooldown, resets the swing without the talent)",
    "Improved Hamstring": "not used",
    "Mortal Strike": "unlocks Mortal Strike (30 rage, weapon plus 85..160, 6 s cooldown)",
    "Booming Voice": "-5%/rank shout rage cost (Battle Shout; the larger area does nothing here; its Piercing Howl cut is in the hooks, Piercing Howl is not cast)",
    "Cruelty": "+1%/rank melee crit",
    "Iron Will": "PvP",
    "Lingering Rage": "not modelled (the engine decays rage between fights with no module hook)",
    "Unbridled Wrath": "12%/rank per landed white swing, either hand: +1 rage (the raid simulator's rule and its beta logs: no procs from abilities)",
    "Furious Precision": "+4/7/10% off-hand hit (dual wield)",
    "Piercing Howl": "not used (the mob stands and fights)",
    "Blood Craze": "1%/rank health over 6 s after being crit or losing 20% in one hit",
    "Dual Wield Specialization": "+5%/rank off-hand damage, +10%/rank off-hand rage (dual wield)",
    "Raging Blows": "-3 rage Cleave (Whirlwind needs Berserker Stance)",
    "Enrage": "30% chance after any hit taken: +2%/rank physical damage for 12 s",
    "Improved Execute": "-2.5 rage/rank Execute",
    "Death Wish": "+20% physical damage and +5% damage taken for 30 s every 3 min (on the pull)",
    "Improved Intercept": "Berserker Stance only",
    "Improved Berserker Rage": "Berserker Rage needs Berserker Stance: nothing in the Battle Stance and Defensive Stance playstyles",
    "Flurry": "crits: +10%/rank attack speed for the next 3 swings (3 ranks, no Death Wish needed: 70753; either hand's landed white swings spend them)",
    "Reckless Swings": "off the global cooldown (assumed) while the warrior is above RECKLESS_ABOVE of its health and the mob above RECKLESS_MOB of its own: 25% of "
                       "base health, the next 4 landed melee attacks (white or ability, either hand) within 8 s give +5 rage each, 15 s cooldown",
    "Improved Whirlwind": "not used: the Battle Stance and Defensive Stance playstyles never cast Whirlwind (Berserker Stance); the hooks take 1 s/rank off its "
                          "cooldown and add 15%/rank to the closest mob",
    "Gore Drinker": "after Enrage, Bloodrage, Death Wish or Bloodthirst the next 3 melee attacks heal 0.5%/rank of maximum health",
    "Bloodthirst": "unlocks Bloodthirst (30 rage, 45% AP plus 30..48, 6 s cooldown)",
    "Shield Specialization": "+1%/rank block, 5 rage per block (sword and board; nothing without a shield)",
    "Anticipation": "+20 Defense: ~-1.6% chance to be hit (assumed)",
    "Improved Bloodrage": "+50% Bloodrage rage (both the instant 10 and the 10 over 10 s)",
    "Improved Thunder Clap": "-2 rage/rank Thunder Clap (pulls of several mobs; Thunder Clap is off on a single mob)",
    "Last Stand": "+30% health for 20 s every 3 min when low",
    "Master of Defense": "5 rage per dodge or parry with a shield (sword and board)",
    "Improved Revenge": "+20%/rank Revenge (sword and board in Defensive Stance)",
    "Defiance": "threat only (7/13/20%, 70753)",
    "Improved Sunder Armor": "not used",
    "Improved Disarm": "not used",
    "Vanguard": "Charge in Defensive Stance (sword and board: no swap to Battle Stance for it)",
    "Improved Shield Wall": "not used",
    "Concussion Blow": "5 s stun every 45 s, no damage (when the mob is on you)",
    "Improved Shield Bash": "silence not modelled (Shield Bash's own 6 s lockout is)",
    "Bastion": "+2%/rank damage with a shield (sword and board)",
    "Focused Rage": "-3 rage on offensive abilities",
    "Shield Slam": "sword and board: 20 rage, 640..670 plus block value, 6 s cooldown",
}
FIT = {
    "Improved Rend": "scale", "Improved Heroic Strike": "scale", "Deflection": "scale", "Improved Charge": "scale", "Improved Overpower": "scale",
    "Anger Management": "scale", "Deep Wounds": "scale", "Two-Handed Weapon Specialization": "scale", "Impale": "scale", "Bloodthrill": "scale",
    "Weaponmaster": "scale", "Improved Slam": "scale",
    "Mortal Strike": ("replace", [{"channel": "dmg", "scope": ["type:melee"], "values": [0.12]}]),
    "Cruelty": "scale", "Unbridled Wrath": "scale", "Blood Craze": "scale", "Enrage": "scale", "Improved Execute": "scale",
    "Flurry": "scale", "Death Wish": "scale", "Improved Berserker Rage": "scale", "Improved Bloodrage": "scale",
    "Last Stand": "scale", "Concussion Blow": "scale", "Focused Rage": "scale", "Anticipation": "scale", "Iron Will": "scale", "Piercing Howl": "scale",
    "Spearing Strike": "scale", "Sweeping Strikes": "scale", "Improved Hamstring": "scale", "Reckless Swings": "scale",
    # simulated since 2026-10-09 (70291 review): the off-hand talents, Gore Drinker, Raging Blows' Cleave cost
    "Dual Wield Specialization": "scale", "Furious Precision": "scale", "Gore Drinker": "scale", "Raging Blows": "scale",
}
SHARE_SOURCE = {'Cleave': 'cleave', 'Thunder Clap': 'thunder_clap', "Melee": "white", "Heroic Strike": "heroic_strike", "Overpower": "overpower", "Execute": "execute", "Whirlwind": "whirlwind", "Rend": "rend",
                "Mortal Strike": "mortal_strike", "Deep Wounds": "deep_wounds", "Victory Rush": "victory_rush", "Bloodthirst": "bloodthirst"}
NEW_SOURCES = {'cleave': {'id': 'cleave', 'share': 0.0, 'min_level': 20, 'tags': ['type:melee', 'yellow', 'school:physical', 'ability:Cleave', 'aoe', 'weapon:2h'], 'cost': 20}, 'thunder_clap': {'id': 'thunder_clap', 'share': 0.0, 'min_level': 6, 'tags': ['type:melee', 'yellow', 'school:physical', 'ability:Thunder Clap', 'aoe', 'weapon:2h'], 'cost': 20}, "mortal_strike": {"id": "mortal_strike", "share": 0.0, "min_level": 40, "tags": ["type:melee", "yellow", "school:physical", "ability:Mortal Strike", "weapon:2h"], "cost": 30, "cooldown": 6},
               "deep_wounds": {"id": "deep_wounds", "share": 0.0, "min_level": 20, "tags": ["type:melee", "dot", "school:physical", "ability:Deep Wounds", "weapon:2h"], "can_crit": False},
               "victory_rush": {"id": "victory_rush", "share": 0.0, "min_level": 20, "tags": ["type:melee", "yellow", "school:physical", "ability:Victory Rush", "weapon:2h"], "cooldown": 30}}
KEY_TALENTS = ["Mortal Strike", "Deep Wounds", "Cruelty"]

# ---------------------------------------------------------------- Protection leveling (spec "prot-leveling"): sword and board
# Shield by level: median armor and item level of the green (GEAR_TIER "greens") or blue shields a warrior can wear with required
# level in the gear_stats.py lag window (Classic 1.12 item database, raw/2026-09-26-cmangos-classic-db-z2815/item_stats.csv, class 4
# subclass 6; random-property greens included, their armor is fixed). Classic data, a Forever assumption.
SHIELD_GEAR = {
    "greens": [(10, 274, 13), (15, 353, 16.5), (20, 428, 21), (25, 528, 27), (30, 611, 32), (35, 678, 36), (40, 1051, 41), (45, 1436, 46),
               (50, 1578, 51), (55, 1734, 56.5), (60, 1861, 61)],
    "blues": [(10, 471, 20), (15, 509, 22), (20, 509, 22), (25, 594.5, 26.5), (30, 680, 30), (35, 785.5, 36.5), (40, 1287, 42), (45, 1612, 46),
              (50, 1851, 52.5), (55, 1994, 58), (60, 2121, 62)],
}
SHIELD_BLOCK_PER_ILVL = 0.65   # ASSUMPTION: the archived item CSV has no block column; Classic shields block about 0.65 x item level
                               # (about 40 at item level 62). Plus Strength / 20 (Classic 1.12 block value per Strength).
BASE_BLOCK = 0.05              # Classic: 5% block with a shield against a same-level mob
DEFENSE_PER_POINT = 0.0004     # Classic: +0.04% dodge, parry and block per Defense point (Anticipation); the miss share is left out
REVENGE_WINDOW = 5.0           # Classic: Revenge is usable for 5 s after a block, dodge or parry (the Forever tooltip gives no window)
SHIELD_BLOCK_TXT = __import__("re").compile(r"block by (\d+)% for (\d+) sec, but will only block (\d+) attack")
TC_TXT = __import__("re").compile(r"by (\d+)% for (\d+) sec")
DEMO_TXT = __import__("re").compile(r"attack power of all enemies within \d+ yards by (\d+) for (\d+) sec")
SUNDER_TXT = __import__("re").compile(r"reducing it by (\d+) per Sunder Armor")
PROT_NOTES = ("Protection leveling (sword and board): a one-hander (tables.weapon_dps '1h', 2.6 s) and a shield (SHIELD_GEAR armor, block "
              "5% + Shield Specialization + Defense, block value 0.65 x item level + Strength / 20), Defensive Stance (-10% damage taken and "
              "dealt), Charge from Battle Stance (Defensive with Vanguard) then a stance swap keeping Tactical Mastery's rage.")

DESCRIPTION = ("Single-target leveling fights against normal mobs of your level. Arms (a two-hander) and Fury (a weapon in each hand) fight in Battle Stance: "
               "Bloodrage and Charge on the pull (the mob is stunned 1 s; Death Wish too when the build has it), Battle Shout kept up, Victory Rush after a kill, "
               "Mortal Strike or Bloodthirst on cooldown, Overpower after a dodge or a Bloodthrill proc, Rend once, Execute under 20% with all the rage, Heroic Strike "
               "with spare rage, Reckless Swings (when talented) while health allows; spells that need Berserker Stance (Whirlwind, Berserker Rage) are never cast. Protection fights sword and board in Defensive Stance: "
               "Charge from Battle Stance, then Shield Block while the mob hits, Revenge, Shield Slam, Rend and Heroic Strike. White swings generate rage by "
               "Forever's normalized rule (weapon speed, half for the off-hand, double on a crit; tables.RAGE_MODEL) (the mob dodges 5%, parries 5%, 10% of swings "
               "glance for 95%). Between fights: 2 s loot, 6 s travel, a bandage below 60% health (First Aid, 60 s cooldown), food below the eating threshold "
               "(65%; 40% under the tuned Arms and Fury rules), rage decays; a death costs 90 s.")
NOT_MODELLED = ("runners, stance dancing (Whirlwind, Berserker Rage, Intercept and Pummel need Berserker Stance, which the Battle Stance playstyles never "
                "take), Hamstring kiting, Retaliation, weapon skill, Lingering Rage and Anger Management's slower rage loss out of combat (the engine decays "
                "rage between fights with no module hook), gear upgrades within a level bracket.")
# rebuild.py: which scorer model, hand draft and optimizer build the pipeline calibrates, races and reports for this class
PIPELINE = {"variants": [{'spec': 'arms-2h-raid', 'opt': 'opt-arms-2h-raid-leveling-aoe', 'tag': 'aoe', 'profile': 'leveling-aoe', 'lookahead': 16, 'sets': ['MOBS_PER_PULL=3'], 'levels': '30,40,50,60', 'calibrate_levels': '40,60', 'label': 'AoE grinding, 3 mobs per pull'}], "spec": "arms-2h-raid", "hand": "leveling-arms", "opt": "opt-arms-2h-raid-leveling-st", "tag": "arms", "lookahead": 20,
            "levels": "20,30,40,50,60", "calibrate_levels": "30,60",
            "extra_reports": [{"spec": "fury-dw-raid", "build": "opt-fury-dw-raid-leveling-st", "compare": ["opt-arms-2h-raid-leveling-st"]}]}


class WarriorModule(BaseModule):
    resource = "rage"
    melee = True
    eat_below = 0.65   # 0.50 made a level-60 warrior die twice as often for the same time per kill (sim, 2026-09-26)
    RECKLESS_ABOVE = 0.8   # Reckless Swings only above this share of the warrior's health (2026-11-03, 600 fights at 30-60, Fury and Arms
                           # leveling builds with the talent added: 0.8 -2.3% / -0.5% per kill against never; 0.4-0.6 lose to never on Arms) ...
    RECKLESS_MOB = 0.3     # ... and while the mob has more than this share of its own (the rage has to be spent)
    ROTATION_KNOBS = {"RECKLESS_ABOVE": [0.5, 0.6, 0.7, 0.8, 0.9, 1.01], "RECKLESS_MOB": [0.0, 0.2, 0.3, 0.5]}   # tuned by rotation_opt.py

    AOE = {'direct': ['Whirlwind', 'Thunder Clap', 'Cleave'], 'min_near': 2}

    def __init__(self, talents, level, spec="arms-2h-raid", gear="leveling"):
        self.t = {k: v for k, v in talents.items() if v > 0}
        self.level = level
        self.spec = spec
        self.gear = gear
        self.book = {name: self.rank_at(name) for name in BOOK}
        self.spells = {n: s for n, s in self.book.items() if s is not None}
        for tname, sname in TALENT_SPELLS.items():
            if not self.t.get(tname):
                self.spells.pop(sname, None)
        self._fight = None
        self.execute_extra = 0.0
        self.flurry_swings = 0
        self.gore_charges = 0
        self.level_base_health = class_base_health("warrior", level)   # Reckless Swings' cost
        self.two_hander = False   # set by make_player (Two-Handed Weapon Specialization)
        self.armor_spell_used = "Battle Stance"
        self.stance = "Battle Stance"   # Arms and Fury level in Battle Stance (Charge, Overpower); every cast checks STANCES
        self.prot = spec.startswith("prot")
        if self.prot:   # sword and board: Defensive Stance (Battle Stance for Charge only)
            self.armor_spell_used = "Defensive Stance"
            self.stance = "Defensive Stance"
        # the area priority keeps the attacks the playstyle's stance allows: Whirlwind needs Berserker Stance, which neither playstyle
        # takes (Thunder Clap works in Battle and Defensive Stance, Cleave in any); Sweeping Strikes goes off the global cooldown (decide)
        self.AOE = {'direct': [n for n in ('Whirlwind', 'Thunder Clap', 'Cleave') if self.stance_ok(n)], 'min_near': 2}

    # ------------------------------------------------------------ talent helpers
    def rank(self, name):
        return self.t.get(name, 0)

    def tv(self, name, idx=0, default=0.0):
        r = self.rank(name)
        if not r:
            return default if default else 0.0
        nums = TNUM.get(name, [])
        if r - 1 < len(nums) and idx < len(nums[r - 1]):
            return nums[r - 1][idx]
        return 0.0

    def not_simulated(self):
        return sorted(n for n in self.t if n not in MECHANICS)

    def stance_ok(self, name):
        """Whether `name` can be cast in the current stance (the spellbook's "Requires ... Stance"; Vanguard lets Charge work in
        Defensive Stance). Spells with no stance requirement always can."""
        need = STANCES.get(name)
        if not need:
            return True
        if name == "Charge" and self.rank("Vanguard"):
            need = need | {"Defensive Stance"}
        return self.stance in need

    def rank_at(self, name):
        ranks = [s for s in BOOK.get(name, []) if s.level <= self.level]
        return self.scale_rank(ranks[-1]) if ranks else None   # the rank at this level (row 8)

    # ------------------------------------------------------------ character
    def make_player(self, level):
        base = class_base_stats("warrior", level)
        g = gear_stats(level, self.gear, "warrior")
        strength = base["strength"] + g["strength"]
        agility = base["agility"] + g["agility"]
        stamina = base["stamina"] + g["stamina"]
        spirit = base["spirit"] + g["spirit"]
        if self.prot:   # the shield's armor adds to the gear's (Toughness, which raised armor from items, left the tree in 70291)
            sh = SHIELD_GEAR.get(tables.GEAR_TIER if self.gear == "leveling" else self.gear, SHIELD_GEAR["greens"])
            sh_armor = interp([(L, a) for L, a, _ in sh], level) * (1 + (tables.GEAR_STAT_MULT - 1) / 2)
            sh_ilvl = interp([(L, i) for L, _, i in sh], level)
            armor = g["armor"] + sh_armor
        else:
            armor = g["armor"]
        p = Player(level=level, hp_max=class_base_health("warrior", level) + 10 * stamina, hp=0.0, mana_max=0.0, mana=0.0, base_mana=0.0,
                   spirit=spirit, intellect=base["intellect"], spell_power=0.0, armor=armor, spell_crit=0.0,
                   dodge=class_dodge("warrior", level, agility), ranged_crit=0.0)
        p.strength, p.agility, p.stamina = strength, agility, stamina
        p.attack_power = class_attack_power("warrior", level, strength, agility)
        self.base_ap = p.attack_power
        p.melee_crit = class_melee_crit("warrior", level, agility) + self.tv("Cruelty", 0) / 100 + (self.tv("Weaponmaster", 0) / 100 if self.rank("Weaponmaster") else 0.0)
        p.hit_bonus = 0.0   # no talent gives both hands hit in 70291 (Precision left the tree; Furious Precision is off-hand only: hit_bonus)
        p.parry = 0.05 + self.tv("Deflection", 0) / 100
        p.dodge -= 0.0
        if self.prot:   # sword and board: one one-hander and a shield (Anticipation's Defense adds dodge, parry and block)
            dps = weapon_dps(level, "1h")
            p.mh = Weapon(dmg_min=dps * WEAPON_SPEED["1h"] * 0.8, dmg_max=dps * WEAPON_SPEED["1h"] * 1.2, speed=WEAPON_SPEED["1h"], kind="1h")
            defense = self.tv("Anticipation", 0) * DEFENSE_PER_POINT
            p.dodge += defense
            p.parry += defense
            p.block = BASE_BLOCK + self.tv("Shield Specialization", 0) / 100 + defense
            p.block_value = SHIELD_BLOCK_PER_ILVL * sh_ilvl + strength / 20.0
            p.form = "Defensive Stance"
        elif self.spec.startswith("fury"):   # Fury: two one-handers (the dual-wield miss penalty and off-hand halving are the engine's)
            dps = weapon_dps(level, "1h")
            p.mh = Weapon(dmg_min=dps * WEAPON_SPEED["1h"] * 0.8, dmg_max=dps * WEAPON_SPEED["1h"] * 1.2, speed=WEAPON_SPEED["1h"], kind="1h")
            p.oh = Weapon(dmg_min=dps * WEAPON_SPEED["1h"] * 0.8, dmg_max=dps * WEAPON_SPEED["1h"] * 1.2, speed=WEAPON_SPEED["1h"], kind="1h")
        else:
            dps = weapon_dps(level, "2h")
            p.mh = Weapon(dmg_min=dps * WEAPON_SPEED["2h"] * 0.8, dmg_max=dps * WEAPON_SPEED["2h"] * 1.2, speed=WEAPON_SPEED["2h"], kind="2h")
        self.two_hander = p.mh.kind == "2h"
        p.rage_max = 100.0   # (Boundless Rage, +10 maximum rage a rank, left the tree in 70291)
        p.rage = 0.0
        p.hp = p.hp_max
        return p

    def pull_range(self):
        return 25.0

    # ------------------------------------------------------------ engine hooks: numbers
    def mana_cost(self, spell):
        cost = spell.cost
        if spell.name == "Heroic Strike":
            cost = max(0.0, cost - self.tv("Improved Heroic Strike", 0))
        if spell.name == "Execute":
            cost = max(0.0, cost - self.tv("Improved Execute", 0))
        if spell.name == "Thunder Clap":
            cost = max(0.0, cost - self.tv("Improved Thunder Clap", 0))
        if spell.name == "Sunder Armor":
            cost = max(0.0, cost - self.tv("Improved Sunder Armor", 0))
        if spell.name in ("Cleave", "Whirlwind"):   # Raging Blows: "Reduces the Rage cost of your Cleave and Whirlwind abilities by 3"
            cost = max(0.0, cost - self.tv("Raging Blows", 0))
        if spell.name in SHOUTS:   # Booming Voice: "reduces their Rage cost by 25%" (5% a rank)
            cost *= 1 - self.tv("Booming Voice", 1) / 100
        if spell.name == "Piercing Howl":   # Booming Voice (70753): "Also reduces the Rage cost of Piercing Howl by 25%"
            cost *= 1 - self.tv("Booming Voice", 2) / 100
        if spell.resource == "health":   # Reckless Swings: "25% of base health"
            return getattr(spell, "health_pct", 0.0) * self.level_base_health
        if spell.resource == "rage" and cost > 0 and spell.kind == "melee":
            cost = max(0.0, cost - self.tv("Focused Rage", 0))
        return cost

    def cast_time(self, spell):
        """Slam: 1.5 s, minus Improved Slam's 0.25 s a rank. With the talent Slam "no longer interrupts or delays your melee swing": the lab
        plays it as an instant that holds the (equally shortened) global cooldown for the cast (after_cast), so white swings keep
        running; its damage lands at the start of the cast instead of the end (audit 2026-10-18 #6)."""
        if spell.name == "Slam" and self.rank("Improved Slam"):
            return 0.0
        return spell.cast

    def pushback_resisted(self, fight, spell):
        return spell.name == "Slam" or super().pushback_resisted(fight, spell)   # a melee ability's cast is not pushed back

    def hit_bonus(self, spell):
        """Furious Precision: off-hand attacks hit more often (the engine adds the dual-wield miss penalty to white swings)."""
        if spell.hand == "oh":
            return self.tv("Furious Precision", 0) / 100
        return 0.0

    def rage_from_hit(self, fight, amount, weapon, hand, crit):
        """Forever's normalized swing rage (tables.rage_from_hit, untouched) plus Dual Wield Specialization's "Rage generated by your
        off-hand attacks" (+10% a rank)."""
        rage = super().rage_from_hit(fight, amount, weapon, hand, crit)
        if hand == "oh":
            rage *= 1 + self.tv("Dual Wield Specialization", 1) / 100
        return rage

    def final_cost(self, fight, spell, cost):
        if spell.name == "Execute":   # spends everything: the extra rage becomes damage
            self.execute_extra = max(0.0, fight.p.rage - cost)
            return fight.p.rage
        return cost

    def crit_bonus(self, spell, frozen):
        if spell.name in NO_CRIT:   # Thunder Clap (spell table, no spell crit); Rend's application and Concussion Blow (no damage)
            return -1.0
        c = 0.0
        if spell.name == "Overpower":
            c += self.tv("Improved Overpower", 0) / 100
        return c

    def crit_damage_bonus(self, spell):
        if spell.kind == "melee" and spell.name not in ("Melee", "Melee (off-hand)"):
            return self.tv("Impale", 0) / 100
        return 0.0

    def damage_multiplier(self, spell, frozen):
        if self.prot:   # no two-hander; Bastion with the shield; Defensive Stance deals 10% less
            m = 1 + self.tv("Bastion", 0) / 100
            if self.stance == "Defensive Stance":
                m *= 0.90
            if spell.name == "Revenge":
                m *= 1 + self.tv("Improved Revenge", 0) / 100
            if spell.name == "Shield Slam" and spell.dmg_max > 0:   # "increased by your Block Value"
                avg = (spell.dmg_min + spell.dmg_max) / 2
                m *= (avg + self._fight.p.block_value) / avg if self._fight else 1.0
        else:   # "damage you deal with two-handed melee weapons": nothing with one-handers (Fury dual wield)
            m = 1 + (self.tv("Two-Handed Weapon Specialization", 0) / 100 if self.two_hander else 0.0)
        if spell.hand == "oh":   # Dual Wield Specialization: "Increases the damage done by your off-hand weapon by 25%"
            m *= 1 + self.tv("Dual Wield Specialization", 0) / 100
        f = self._fight
        if f and f.p.buff("Enrage", f.t):
            m *= 1 + self.tv("Enrage", 1) / 100   # +2%/rank (70009); was a flat +10% at every rank
        if f and f.p.buff("Death Wish", f.t):
            m *= 1 + self.tv("Death Wish", 0) / 100   # "increases your Physical damage done by 20%"
        if spell.name == "Execute" and spell.dmg_max > 0:
            m *= (spell.dmg_max + getattr(spell, "rage_dmg", 0.0) * self.execute_extra) / spell.dmg_max
        if spell.name == "Whirlwind" and self.rank("Improved Whirlwind") and f and f.m is min(f.alive() or [f.m], key=lambda x: x.dist):
            m *= 1 + self.tv("Improved Whirlwind", 1) / 100   # 70753: "increases the damage it deals to the closest enemy by 15/30%"
        return m

    def periodic_multiplier(self, spell):
        """Rend's bleed (its only damage): Improved Rend ("Increases the Bleed damage done by your Rend ability by 35%", on the whole tick
        as the raid simulator fits the beta logs), the physical damage buffs (Enrage, Death Wish) and, with a shield, Bastion and
        Defensive Stance's -10% (beta logs: Rend loses its 10% there). Deep Wounds goes through refresh_dot without modifiers."""
        m = 1.0
        if spell.name == "Rend":
            m *= 1 + self.tv("Improved Rend", 0) / 100
        f = self._fight
        if f and f.p.buff("Enrage", f.t):
            m *= 1 + self.tv("Enrage", 1) / 100
        if f and f.p.buff("Death Wish", f.t):
            m *= 1 + self.tv("Death Wish", 0) / 100
        if self.prot:
            m *= 1 + self.tv("Bastion", 0) / 100
            if self.stance == "Defensive Stance":
                m *= 0.90
        return m

    def periodic_can_crit(self, spell):
        return True

    def split_damage_taken(self, fight, dmg):
        if self.prot and self.stance == "Defensive Stance":
            dmg *= 0.90   # Defensive Stance: "Decreases damage taken by 10%" (melee and spells)
        if fight.p.buff("Death Wish", fight.t):
            dmg *= 1 + self.tv("Death Wish", 1) / 100   # Death Wish: "increases all damage you take by 5%"
        return dmg

    def extra_targets(self, fight, spell, white):
        """Sweeping Strikes: a landed melee attack also hits a second mob while charges last (engine.Fight.hit_others_melee rolls it).
        Area attacks hit more mobs on their own; Execute's copy is a plain weapon hit in the raid simulator, so it is left out."""
        b = fight.p.buffs.get("Sweeping Strikes")
        if not b or b["until"] <= fight.t or b.get("charges", 0) <= 0 or spell.kind != "melee" or spell.name in NO_SWEEP:
            return 0
        b["charges"] -= 1
        if b["charges"] <= 0:
            fight.p.buffs.pop("Sweeping Strikes", None)
        return 1

    def block_bonus(self, fight):
        b = fight.p.buffs.get("Shield Block") if self.prot else None
        if b and b["until"] > fight.t and b.get("charges", 0) > 0:
            return b["chance"]
        return 0.0

    def _avoided(self, fight):
        if self.stance == "Defensive Stance" and "Revenge" in self.spells:
            fight.p.buffs["Revenge"] = {"until": fight.t + REVENGE_WINDOW}

    def on_block(self, fight):
        if not self.prot:
            return
        p = fight.p
        b = p.buffs.get("Shield Block")
        if b and b["until"] > fight.t and b.get("charges", 0) > 0:
            b["charges"] -= 1
            if b["charges"] <= 0:
                p.buffs.pop("Shield Block", None)
        if self.rank("Shield Specialization") and fight.rng.random() < self.tv("Shield Specialization", 1) / 100:
            p.rage = min(p.rage_max, p.rage + self.tv("Shield Specialization", 2))
        self._avoided(fight)

    def _master_of_defense(self, fight):
        if self.rank("Master of Defense") and fight.rng.random() < self.tv("Master of Defense", 0) / 100:
            fight.p.rage = min(fight.p.rage_max, fight.p.rage + self.tv("Master of Defense", 1))

    def on_dodge(self, fight):
        if self.prot:
            self._master_of_defense(fight)
            self._avoided(fight)

    def on_parry(self, fight):
        if self.prot:
            self._master_of_defense(fight)
            self._avoided(fight)

    def health_regen(self, p):
        return class_health_regen_tick("warrior", p.spirit)

    def on_regen_tick(self, fight, p, t):
        if self.rank("Anger Management"):
            p.rage = min(p.rage_max, p.rage + 2.0 / 3.0)   # 1 rage per 3 s, on the 2 s tick

    def swing_speed_factor(self):
        return 1.0 / (1 + self.tv("Flurry", 0) / 100) if self.flurry_swings > 0 else 1.0

    def attacks_from_front(self):
        return True

    # ------------------------------------------------------------ engine hooks: events
    def on_fight_start(self, fight):
        self._fight = fight
        p, t = fight.p, fight.t
        self.flurry_swings = 0
        if self.prot:
            self.prot_fight_start(fight)
        br = self.spells.get("Bloodrage")
        if br is not None and p.ready("Bloodrage", t) and p.hp > 0.45 * p.hp_max:
            gain = 10.0 * (1 + self.tv("Improved Bloodrage", 0) / 100)   # "all the Rage generated": the instant 10 and the 10 over 10 s
            p.hp -= 0.06 * p.hp_max
            p.rage = min(p.rage_max, p.rage + gain)
            p.buffs["Bloodrage"] = {"until": t + 10.0, "left": gain, "per": gain / 10.0, "last": t}
            p.cooldowns["Bloodrage"] = t + br.cooldown
            fight.casts["Bloodrage"] = fight.casts.get("Bloodrage", 0) + 1
            self._gore()
        dw = self.spells.get("Death Wish")
        if dw is not None and p.ready("Death Wish", t) and p.rage >= self.mana_cost(dw):
            p.rage -= self.mana_cost(dw)
            p.buffs["Death Wish"] = {"until": t + (self.tv("Death Wish", 2) or 30.0)}
            p.cooldowns["Death Wish"] = t + dw.cooldown
            fight.casts["Death Wish"] = fight.casts.get("Death Wish", 0) + 1
            self._gore()

    def _bloodrage_tick(self, fight):
        """Bloodrage's trickle: a tick every second for 10 s (10 rage; Improved Bloodrage +50%), paid for every whole second since the
        last tick. Until 2026-10-18 it paid at most 1 rage per decision (none while the warrior waited on the global cooldown), and the
        `_br_tick` stamp on the fight carried over between fights; Improved Bloodrage added nothing to it (audit 2026-10-18 #25)."""
        p, t = fight.p, fight.t
        br = p.buffs.get("Bloodrage")
        if not br or br.get("left", 0) <= 0:
            return
        last = br.get("last", br["until"] - 10.0)
        n = int(min(t, br["until"]) - last + 1e-9)
        if n <= 0:
            return
        gain = min(br["left"], n * br.get("per", 1.0))
        br["left"] -= gain
        br["last"] = last + n
        p.rage = min(p.rage_max, p.rage + gain)

    def _gore(self):
        """Gore Drinker: "Your Enrage, Berserker Rage, Bloodrage, Death Wish, and Bloodthirst abilities cause your next 3 melee attacks
        to restore 1.0% of your maximum Health" (charges spent in on_swing)."""
        if self.rank("Gore Drinker"):
            self.gore_charges = int(self.tv("Gore Drinker", 0) or 3)

    def on_hit(self, fight, spell, amount, crit, frozen):
        p, m, t = fight.p, fight.m, fight.t
        # (Blood Craze no longer triggers on Bloodthirst in 70291: Blizzard's 2026-10-02 notes and the tooltip; see on_hit_taken)
        if spell.name in ("Bloodthirst", "Berserker Rage") and (amount > 0 or spell.name == "Berserker Rage"):
            self._gore()
        if spell.name == "Charge":
            p.rage = min(p.rage_max, p.rage + getattr(spell, "charge_rage", 9.0) + self.tv("Improved Charge", 0))
            m.stun_until = max(m.stun_until, t + spell.stun)
            fight.note(f"Charge: {p.rage:.0f} rage")
        if spell.name == "Battle Shout":
            if not p.buff("Battle Shout", t):
                p.attack_power = self.base_ap + getattr(spell, "ap", 0.0)
            p.buffs["Battle Shout"] = {"until": t + 180.0}
        if spell.name == "Victory Rush" and amount > 0:
            fight.heal(spell, 0.10 * p.hp_max)
            p.buffs.pop("Victory Rush", None)
        if spell.name == "Berserker Rage" and self.rank("Improved Berserker Rage"):
            p.rage = min(p.rage_max, p.rage + 10.0)
        if self.prot:
            if spell.name == "Revenge":
                p.buffs.pop("Revenge", None)
            near = [x for x in fight.alive() if x is m or x.in_melee]   # the pull's mobs next to the warrior
            if spell.name == "Thunder Clap":   # "increasing the time between their attacks by 20% for 10 sec" (audit 2026-10-18 #73: was 25%)
                mt = TC_TXT.search(spell.text or "")
                for x in near[:4]:
                    x.attack_slow = float(mt.group(1)) / 100 if mt else 0.20
                    x.attack_slow_until = t + (float(mt.group(2)) if mt else 10.0)
            if spell.name == "Demoralizing Shout":   # attack power / 14 x the mob's 2 s swing off every hit (as the druid's Roar)
                md = DEMO_TXT.search(spell.text or "")
                if md:
                    for x in near:
                        x.dmg_reduction = float(md.group(1)) / 14.0 * tables.MOB_SWING
                        x.dmg_reduction_until = t + float(md.group(2))
            if spell.name == "Sunder Armor":
                ms = SUNDER_TXT.search(spell.text or "")
                n = min(5, getattr(m, "sunders", 0) + 1)
                m.sunders = n
                m.armor_debuff = n * (float(ms.group(1)) if ms else 0.0)

    def on_swing(self, fight, spell, outcome, amount, hand):
        p, m, t = fight.p, fight.m, fight.t
        white = spell.name in WHITE
        self._bloodrage_tick(fight)
        if outcome == "dodge":
            p.buffs["Overpower"] = {"until": t + OVERPOWER_WINDOW}
        if outcome in ("miss", "dodge", "parry"):
            return
        # Unbridled Wrath: white swings of either hand only (the raid simulator's rule, fitted to beta logs: 0 of 148 Heroic Strike and
        # Cleave hits proc it; audit 2026-10-18 #17); until 2026-10-18 every weapon ability rolled it too
        if white and self.rank("Unbridled Wrath") and fight.rng.random() < self.tv("Unbridled Wrath", 0) / 100:
            p.rage = min(p.rage_max, p.rage + self.tv("Unbridled Wrath", 1))   # "1 additional Rage" (70291: no longer 2 for a two-hander)
        attack = amount > 0 and spell.kind == "melee" and spell.name not in NOT_WEAPON_ATTACK   # a weapon attack that dealt damage
        # Bloodthrill: "Your Main Hand melee attacks against enemies afflicted by your Rend" (white swings and main-hand abilities,
        # Heroic Strike and Cleave included: Blizzard's 2026-09-24 notes; Overpower's own hit is spent by after_cast)
        if attack and hand == "mh" and self.rank("Bloodthrill") and fight.dot_active("Rend") and fight.rng.random() < self.tv("Bloodthrill", 0) / 100:
            b = p.buffs.get("Overpower")
            p.buffs["Overpower"] = {"until": max(b["until"] if b else 0.0, t + OVERPOWER_WINDOW)}   # 70425 names no window of its own
        rs = p.buffs.get("Reckless Swings")
        if attack and rs and rs["until"] > t and rs.get("charges", 0) > 0:   # Reckless Swings: "Your next 4 melee attacks generate 5 additional Rage"
            rs["charges"] -= 1
            p.rage = min(p.rage_max, p.rage + rs["rage"])
            if rs["charges"] <= 0:
                p.buffs.pop("Reckless Swings", None)
        if attack and self.gore_charges > 0:   # Gore Drinker's heal on each of the next 3 melee attacks
            self.gore_charges -= 1
            fight.heal(GORE, p.hp_max * self.tv("Gore Drinker", 1) / 100)
        if outcome == "crit" and amount > 0:
            if self.rank("Deep Wounds"):
                # 60% of the main hand's average weapon damage over 12 s, no attack power, rolling: a crit on a running bleed adds what
                # it still owed (Blizzard's 2026-10-08 notes; the raid simulator's fit to beta logs: share x average / 4 a tick)
                owed = sum(d[1] * d[2] for d in m.dots if d[0] == "Deep Wounds")
                dur = self.tv("Deep Wounds", 1) or 12.0
                fight.refresh_dot("Deep Wounds", owed + (p.mh.dmg_min + p.mh.dmg_max) / 2 * self.tv("Deep Wounds", 0) / 100, max(1, int(round(dur / 3.0))), 3.0)
            if self.rank("Flurry"):
                self.flurry_swings = int(self.tv("Flurry", 1) or 3)
        elif white and self.flurry_swings > 0:   # either hand's landed white swing spends a charge (the raid simulator's rule)
            self.flurry_swings -= 1

    def on_hit_taken(self, fight, dmg, crit=False):
        p, t = fight.p, fight.t
        if self.rank("Enrage") and fight.rng.random() < self.tv("Enrage", 0) / 100:
            p.buffs["Enrage"] = {"until": t + 12.0}
            self._gore()
        if self.rank("Blood Craze") and (crit or dmg > 0.2 * p.hp_max):
            p.hots = [h for h in p.hots if h[0] != "Blood Craze"]
            p.hots.append(["Blood Craze", p.hp_max * self.tv("Blood Craze", 0) / 100 / 3, 3, t + 2.0, 2.0, "player"])
        b = p.buffs.get("Berserker Rage")
        if b and b["until"] > t:
            p.rage = min(p.rage_max, p.rage + 5.0)
        br = p.buffs.get("Bloodrage")
        if br and br["until"] > t and br.get("left", 0) > 0:
            pass

    def on_tick(self, fight, spell, amount, crit):
        pass

    def after_cast(self, fight, spell):
        p, t = fight.p, fight.t
        if spell.cooldown > 0:
            p.cooldowns[spell.name] = t + spell.cooldown
        if spell.name == "Whirlwind" and self.rank("Improved Whirlwind"):   # 70753: "Reduces the cooldown of your Whirlwind ability by 1/2 seconds"
            p.cooldowns[spell.name] = t + max(0.0, spell.cooldown - self.tv("Improved Whirlwind", 0))
        if spell.name == "Overpower":
            p.buffs.pop("Overpower", None)
        if spell.name == "Slam":
            if self.rank("Improved Slam"):   # "Slam's cooldown is reduced by 3.0 sec"; the global cooldown is the shortened cast
                p.cooldowns["Slam"] = t + max(0.0, spell.cooldown - self.tv("Improved Slam", 1))
                p.gcd_until = t + max(0.0, spell.cast - self.tv("Improved Slam", 0))
            else:   # without the talent the cast interrupts the swing: the swing timer starts over when it ends (Classic's Slam)
                if p.mh is not None:
                    p.swing_mh = max(p.swing_mh, t + p.mh.speed * self.swing_speed_factor())
                if p.oh is not None:
                    p.swing_oh = max(p.swing_oh, t + p.oh.speed * self.swing_speed_factor())

    def on_kill(self, fight):
        p, t = fight.p, fight.t
        if "Victory Rush" in self.spells:
            p.buffs["Victory Rush"] = {"until": t + 20.0}

    def after_fight(self, p, t):
        """Bandage below 60% health (First Aid by level, 8 s, 60 s cooldown); Bloodrage's trickle is dropped between fights."""
        p.buffs.pop("Bloodrage", None)
        p.buffs.pop("Enrage", None)
        p.buffs.pop("Sweeping Strikes", None)
        p.buffs.pop("Reckless Swings", None)
        self.gore_charges = 0
        if self.prot:
            p.buffs.pop("Revenge", None)
            p.buffs.pop("Shield Block", None)
        if p.hp < 0.60 * p.hp_max and p.cooldowns.get("Bandage", -1.0) <= t:
            p.hp = min(p.hp_max, p.hp + bandage_heal(p.level))
            p.cooldowns["Bandage"] = t + 60.0
            return 8.0
        return 0.0

    # ------------------------------------------------------------ priority list
    def _sweep(self, fight):
        """Sweeping Strikes (Battle Stance, 30 rage, off the global cooldown as in the raid simulator) once a second mob stands in reach:
        the next 5 melee attacks also hit it (extra_targets)."""
        p, t = fight.p, fight.t
        ss = self.spells.get("Sweeping Strikes")
        if (ss is None or not self.stance_ok(ss.name) or p.buff("Sweeping Strikes", t) or not p.ready(ss.name, t) or not fight.m.in_melee
                or not any(x.in_melee for x in fight.others())):
            return
        cost = self.mana_cost(ss)
        if not fight.can_afford(ss, cost):
            return
        fight.spend(cost, ss)
        p.buffs["Sweeping Strikes"] = {"until": t + SWEEP_DURATION, "charges": SWEEP_CHARGES}
        p.cooldowns[ss.name] = t + ss.cooldown
        fight.casts[ss.name] = fight.casts.get(ss.name, 0) + 1
        fight.note(f"Sweeping Strikes ({SWEEP_CHARGES} attacks)")

    def _reckless(self, fight):
        """Reckless Swings (70753, Fury row 4): off the global cooldown (an assumption: the tooltip and the notes name none, as Bloodrage's)
        once the mob is in melee, while the warrior is above RECKLESS_ABOVE of its health and the mob above RECKLESS_MOB of its own: pays 25%
        of base health for 5 rage on each of the next 4 landed melee attacks within 8 s (on_swing)."""
        p, m, t = fight.p, fight.m, fight.t
        rs = self.spells.get("Reckless Swings")
        if (rs is None or not p.ready(rs.name, t) or not m.in_melee or p.hp < self.RECKLESS_ABOVE * p.hp_max or m.hp <= self.RECKLESS_MOB * m.hp_max
                or p.buff("Reckless Swings", t) or p.rage > p.rage_max - 20):
            return
        cost = self.mana_cost(rs)
        if p.hp - cost < 0.2 * p.hp_max or not fight.can_afford(rs, cost):
            return
        fight.spend(cost, rs)
        n, rage, dur = getattr(rs, "reckless", (4, 5.0, 8.0))
        p.buffs["Reckless Swings"] = {"until": t + dur, "charges": n, "rage": rage}
        p.cooldowns[rs.name] = t + rs.cooldown
        fight.casts[rs.name] = fight.casts.get(rs.name, 0) + 1
        fight.note(f"Reckless Swings (-{cost:.0f} health)")

    def decide(self, fight):
        if fight.m is not None and fight.m.in_melee:
            self._reckless(fight)
        if self.prot:
            return self.decide_prot(fight)
        if fight.others():   # a pull of several mobs: Sweeping Strikes, then the area priority (engine.BaseModule.decide_aoe, self.AOE)
            self._sweep(fight)
            r = self.decide_aoe(fight)
            if r is not None:
                return r
        p, m, t = fight.p, fight.m, fight.t
        sp = self.spells
        in_melee = m.in_melee and m.dist <= MELEE_RANGE + 0.5

        def can(s):   # every cast needs its stance (STANCES): Berserker Rage never goes off in Battle Stance
            return s is not None and self.stance_ok(s.name) and p.ready(s.name, t) and fight.can_afford(s, self.mana_cost(s))

        charge, shout, vr, execute, over, ms, rend, hs, bt, cb, brage = (sp.get(n) for n in ("Charge", "Battle Shout", "Victory Rush", "Execute", "Overpower", "Mortal Strike", "Rend", "Heroic Strike", "Bloodthirst", "Concussion Blow", "Berserker Rage"))
        slam, spear = sp.get("Slam"), sp.get("Spearing Strike")
        hp = m.hp
        self._bloodrage_tick(fight)
        if not in_melee:
            if charge and can(charge) and 8.0 <= m.dist <= 25.0 and fight.swings == 0 and not m.in_melee:
                return charge
            return "advance"
        if brage and can(brage) and self.rank("Improved Berserker Rage") and p.rage < 30:
            p.buffs["Berserker Rage"] = {"until": t + 10.0}
            return brage
        if shout and can(shout) and not p.buff("Battle Shout", t) and hp > 0.3 * m.hp_max:
            return shout
        if cb and can(cb) and p.hp < 0.35 * p.hp_max and not m.stunned(t):
            return cb
        if vr and can(vr) and p.buff("Victory Rush", t) and p.hp < 0.9 * p.hp_max:
            return vr
        if execute and can(execute) and hp <= 0.2 * m.hp_max:
            return execute
        if over and can(over) and p.buff("Overpower", t):
            return over
        if ms and can(ms):
            return ms
        if bt and can(bt):
            return bt
        if rend and can(rend) and not fight.dot_active("Rend") and hp > 0.35 * m.hp_max and (ms is None or p.rage >= 40 or not p.ready("Mortal Strike", t)):
            return rend
        reserve = 30.0 if (ms and p.cooldowns.get("Mortal Strike", 0) - t < 3.0) else 0.0
        # Slam (learned at 20; 70425: 15 rage, 18 s cooldown) with Improved Slam, and Spearing Strike (talent, 40% weapon damage), with the
        # rage Mortal Strike does not need (audit 2026-10-18 #6: neither was ever cast before; the tuned rules veto either where it does
        # not pay). Plain Slam stops the swing for its 1.5 s cast and resets it: cast like this it cost 2.6-6% per kill at 20-60
        # (2026-10-18, 1000 fights, Arms and Fury leveling builds), so it waits for the talent.
        if slam and self.rank("Improved Slam") and can(slam) and p.rage >= self.mana_cost(slam) + reserve:
            return slam
        if spear and can(spear) and p.rage >= self.mana_cost(spear) + reserve:
            return spear
        if hs and fight.queued_swing is None and p.rage >= self.mana_cost(hs) + reserve + (15 if over and p.buff("Overpower", t) is None else 0):
            return hs
        return None

    # ------------------------------------------------------------ Protection leveling (spec "prot-leveling")
    PROT_OPTIONAL = ("Thunder Clap", "Demoralizing Shout", "Rend", "Sunder Armor", "Shield Block")   # rotation pieces a test can switch off
    # off by default on a single mob (800 fights, seed 1, level 60, prot-raid-tank, 2026-09-30): Thunder Clap +1.2 s and Demoralizing
    # Shout +1.0 s per kill for no measurable safety (no deaths either way); Sunder Armor never beat Heroic Strike for the rage.
    # Thunder Clap stays in the area priority (self.AOE) and Demoralizing Shout is used on pulls of 2+ mobs (3 mobs: same time per
    # kill, deaths 1.1 -> 0.75 per 100). A knob: set `prot_off` on the module (rotation_opt's knobs work too).
    prot_off = ("Thunder Clap", "Demoralizing Shout", "Sunder Armor")
    PROT_CB_BELOW = 0.50   # Concussion Blow when the warrior's health is below this share

    def _retain(self):
        """Rage kept through a stance change: Tactical Mastery's 10 (trained at 14) plus Improved Tactical Mastery's 3 per rank."""
        if "Tactical Mastery" not in self.spells:
            return 0.0
        return 10.0 + self.tv("Improved Tactical Mastery", 0)

    def _set_stance(self, fight, name):
        """A stance change: off the global cooldown, 1 s stance cooldown, rage above what Tactical Mastery keeps is lost."""
        p = fight.p
        if self.stance == name or p.cooldowns.get("Stance", -1.0) > fight.t:
            return False
        p.rage = min(p.rage, self._retain())
        self.stance = p.form = name
        p.cooldowns["Stance"] = fight.t + 1.0
        fight.casts[name] = fight.casts.get(name, 0) + 1
        fight.note(f"{name}: {p.rage:.0f} rage kept")
        return True

    def prot_fight_start(self, fight):
        """Charge needs Battle Stance ("Requires Battle Stance"; Vanguard: Defensive Stance too): switch before the pull."""
        p = fight.p
        if "Defensive Stance" not in self.spells:   # below level 10: Battle Stance only
            self.stance = p.form = "Battle Stance"
            return
        if "Charge" in self.spells and p.ready("Charge", fight.t) and not self.rank("Vanguard"):
            self._set_stance(fight, "Battle Stance")

    def decide_prot(self, fight):
        p, m, t = fight.p, fight.m, fight.t
        sp = self.spells
        in_melee = m.in_melee and m.dist <= MELEE_RANGE + 0.5
        use = set(self.PROT_OPTIONAL) - set(self.prot_off)

        def can(s):   # every cast needs its stance (STANCES; Vanguard: Charge in Defensive Stance)
            return s is not None and self.stance_ok(s.name) and p.ready(s.name, t) and fight.can_afford(s, self.mana_cost(s))

        self._bloodrage_tick(fight)
        charge = sp.get("Charge")
        if not in_melee:
            if charge and can(charge) and 8.0 <= m.dist <= 25.0 and fight.swings == 0 and not m.in_melee and (self.stance == "Battle Stance" or self.rank("Vanguard")):
                return charge
            return "advance"
        ss, rev, tc, demo, rend, sunder, hs, sb, bash, shout, vr, cb = (sp.get(n) for n in (
            "Shield Slam", "Revenge", "Thunder Clap", "Demoralizing Shout", "Rend", "Sunder Armor", "Heroic Strike", "Shield Block", "Shield Bash",
            "Battle Shout", "Victory Rush", "Concussion Blow"))
        hp = m.hp
        # into Defensive Stance once the rage above what Tactical Mastery keeps is spent (Shield Slam, Rend, Thunder Clap work in both)
        if self.stance != "Defensive Stance" and "Defensive Stance" in sp:
            if p.rage > self._retain():
                for s in (ss, rend if "Rend" in use and not fight.dot_active("Rend") else None,
                          tc if "Thunder Clap" in use and t >= m.attack_slow_until else None):
                    if can(s):
                        return s
            self._set_stance(fight, "Defensive Stance")
        defensive = self.stance == "Defensive Stance"
        if fight.others():   # a pull of several mobs: Thunder Clap / Cleave first (engine.BaseModule.decide_aoe, self.AOE)
            r = self.decide_aoe(fight)
            if r is not None:
                return r
        if bash and can(bash) and m.casting(t):
            return bash
        # Shield Block: off the global cooldown, only while the mob swings at the warrior
        if defensive and "Shield Block" in use and sb and can(sb) and m.target == "player" and not m.stunned(t) and not p.buff("Shield Block", t):
            mt = SHIELD_BLOCK_TXT.search(sb.text or "")
            chance, dur, charges = (float(mt.group(1)) / 100, float(mt.group(2)), int(mt.group(3))) if mt else (0.75, 5.0, 1)
            fight.spend(self.mana_cost(sb), sb)
            p.buffs["Shield Block"] = {"until": t + dur, "charges": charges, "chance": chance}
            p.cooldowns["Shield Block"] = t + sb.cooldown
            fight.casts["Shield Block"] = fight.casts.get("Shield Block", 0) + 1
        if shout and can(shout) and not p.buff("Battle Shout", t) and hp > 0.3 * m.hp_max:
            return shout
        if cb and can(cb) and p.hp < self.PROT_CB_BELOW * p.hp_max and not m.stunned(t):
            return cb
        if vr and can(vr) and p.buff("Victory Rush", t) and p.hp < 0.9 * p.hp_max:
            return vr
        if defensive and rev and can(rev) and p.buff("Revenge", t):
            return rev
        if ss and can(ss):
            return ss
        if "Thunder Clap" in use and tc and can(tc) and t >= m.attack_slow_until and hp > 0.4 * m.hp_max:
            return tc
        if ("Demoralizing Shout" in use or len(fight.alive()) >= 2) and demo and can(demo) and t >= m.dmg_reduction_until and hp > 0.4 * m.hp_max:
            return demo
        if "Rend" in use and rend and can(rend) and not fight.dot_active("Rend") and hp > 0.5 * m.hp_max:
            return rend
        reserve = (self.mana_cost(ss) if ss and p.cooldowns.get("Shield Slam", 0) - t < 2.0 else 0.0) + (self.mana_cost(rev) if rev and defensive else 0.0)
        if "Sunder Armor" in use and sunder and can(sunder) and getattr(m, "sunders", 0) < 5 and hp > 0.5 * m.hp_max and p.rage >= self.mana_cost(sunder) + reserve:
            return sunder
        if hs and fight.queued_swing is None and p.rage >= self.mana_cost(hs) + reserve:
            return hs
        return None
