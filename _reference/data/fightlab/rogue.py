"""Rogue module for the fight lab (Combat swords leveling).

Spell ranks are read from `_reference/data/forever-spells/rogue.json` (beta client build 1.60.1.70291); talent numbers from
each rank's tooltip in `_reference/data/forever-talents/rogue.json`. Weapons: a quest-green sword in each hand by level
(`tables.weapon_dps`, 2.6 speed; "dagger" in the spec string: two daggers, 1.8 speed), attack power from the client's base stats
(1 per Strength and Agility), poisons from the spellbook (Instant Poison main hand, Deadly Poison off hand).

Playstyle `combat-swords-raid` (the scorer's model id, used for leveling): open from stealth behind the mob with Cheap Shot
(Garrote before 26), Slice and Dice at 1-2 points when it is down, Sinister Strike to 5 points, Eviscerate (or Kidney
Shot when hurt), Riposte after a parry, Blade Flurry and Adrenaline Rush on the pull when ready, Cold Blood right before a
5-point Eviscerate, Evasion when low. Daggers builds with the Mutilate talent build with Mutilate from 30 instead of Sinister
Strike (2026-10-25: the list had never cast it, so no Assassination leveling build could hold its signature spell; `mutilate()`
follows the raid simulator's registerMutilate). Between fights: a bandage below 60% health (First Aid, 60 s cooldown), food below 65%
(the tuned rules in `rotations/rogue-<spec>.json` veto spells and move the thresholds on top of this list).

2026-10-09 fixes against the 70291 tooltips: Cold Blood is spent by the next Sinister Strike, Backstab, Ambush, Eviscerate or
Mutilate (it had made every Sinister Strike crit until the next Eviscerate, and was pressed at the pull); Remorseless Attacks
covers Sinister Strike, Backstab, Ambush, Mutilate and Ghostly Strike (it was Sinister Strike only); Opportunity and Serrated
Blades' armor share apply in every playstyle (they were Subtlety only, while the tuned Combat lists open with Garrote); Hack and
Slash gives daggers crit and swords an extra attack on any landed melee attack (every weapon got the sword proc, white swings
only); Kidney Shot stuns for the tooltip's seconds per combo point (its text has no "for N sec", so it stunned for 0 s);
Slice and Dice counts as a finishing move for Ruthlessness and Relentless Strikes; a finisher that misses or is dodged or parried
keeps its combo points (on_miss; engine.spend takes them before the roll, the raid simulator only on a landed finisher). The tuned
rules' Kidney Shot veto was measured while Kidney Shot stunned for 0 s: re-tune (rotation_opt.py) before trusting it.

Playstyle `subtlety-leveling` (any spec string starting with "subtlety"; 2026-09-30): a dagger in the main hand (Ambush needs
one; Hemorrhage 145% and Ghostly Strike 180% weapon damage with a dagger make up for its 1.8 s speed, so the builders lose
nothing against a 2.6 s sword at equal weapon dps) and in the off hand; "sword" in the spec string gives two swords instead
(no Ambush). Premeditation (2 points) as the pull starts, then open from stealth behind the mob with Ambush or Garrote, whichever
the module expects to be worth more (`opener_order`: Ambush in short low-level fights, Garrote once its bleed outlasts the energy
difference; Cheap Shot without either), Slice and Dice / Eviscerate / Kidney Shot as in the Combat list, Ghostly Strike on
cooldown, Hemorrhage as the builder (Sinister Strike without it), Riposte after a parry, Evasion when low (Preparation resets
it when it is on cooldown). Talent effects only this playstyle applies: see SUBTLETY_MECHANICS.

2026-11-03, Blizzard's development notes of 2026-11-02 (client 1.60.1.70753; talentsforever.com's 2026-11-03 export), which rework all three
trees. Removed: Murder, Quietus, Cutthroat, Thousand Cuts, Improved Distract. Renamed: Improved Sinister Strike -> Efficient Strikes (also
Hemorrhage), Improved Eviscerate -> Coup de Grace (also Death Mark). New baseline: **Shank** (level 24, rank 2 at 44: an off-hand strike
for 50% weapon damage that cannot miss, 5 Energy, 10 s cooldown, generates 15 / 25 Energy; `shank()`), cast in every playstyle whenever
the Energy it nets would not overflow (with Boot Knife also as a builder below 4 points); **Poised** (level 18: every pull starts at full
Energy, so the opener costs 10 less, Composure 5/10 more; `final_cost`). New talents: Death Mark (`death_mark`; the tooltip gives no
storage rate, DEATH_MARK_STORE is an assumption), Boot Knife, Flash of Steel, Blood Splatter, Composure; Venom is now a passive on Shank
(poison damage +30% and poison chance +20 points for 6 s); Relentless Strikes 4-20% per point; Aggression Sinister Strike and Eviscerate
5-15%; Seal Fate 33-100%; Lethality 10/20%; Dual Wield Specialization 25/50%; Flawless Execution 15; Puncturing Wounds also +5-15% crit on
Mutilate; Hemorrhage also +15% Garrote; Ghostly Strike lets the next Garrote within 7 s skip Stealth (Subtlety playstyle with Dirty Deeds,
whose Garrote needs no back: GHOSTLY_GARROTE_HP); Mutilate 90% weapon damage per hand (the flat amount: MUT_FLAT_BY_RANK); Instant
Poison +0.01 x attack power per hit, Deadly Poison +0.009 x attack power per stack (POISON_AP). Rupture (off by default) now follows the
tooltip's per-point table and the raid simulator's attack power per tick.
"""
import dataclasses
import json
import pathlib
import re

import tables
from engine import parse_interrupt, BaseModule, Player, Spell, Weapon
from tables import (GCD, MELEE_RANGE, WEAPON_SPEED, armor_mitigation, bandage_heal, class_attack_power, class_base_health, class_base_stats, class_dodge,
                    class_health_regen_tick, class_melee_crit, gear_stats, weapon_dps)

ROOT = pathlib.Path(__file__).resolve().parents[3]
SPELLBOOK = json.load(open(ROOT / "_reference/data/forever-spells/rogue.json", encoding="utf-8"))
TREE = json.load(open(ROOT / "_reference/data/forever-talents/rogue.json", encoding="utf-8"))

NUM = re.compile(r"(\d+(?:\.\d+)?)")
PCT = re.compile(r"(\d+)% weapon damage(?: plus (\d[\d,]*))?")
PLUS_WEAPON = re.compile(r"causes (\d[\d,]*) damage in addition to your normal weapon damage")
FLAT = re.compile(r"[Cc]auses (\d[\d,]*) damage|for (\d[\d,]*) damage")
DOT = re.compile(r"causing (\d[\d,]*) damage over (\d+) sec")
STUN = re.compile(r"[Ss]tuns the target for (\d+) sec")
CP = re.compile(r"Awards (\d) [Cc]ombo [Pp]oints?")
EVIS = re.compile(r"5 points: (\d[\d,]*)-(\d[\d,]*) damage")
RUPTURE = re.compile(r"4 points: (\d[\d,]*) damage over (\d+) sec")
SND = re.compile(r"attack speed by (\d+)%")
POISON = re.compile(r"(\d+)% chance of poisoning the enemy(?: which instantly inflicts (\d[\d,]*) to (\d[\d,]*) Nature damage| for (\d[\d,]*) Nature damage over (\d+) sec)")
INCAP = re.compile(r"incapacitates the target for (\d+) sec")
PER_POINT_SECONDS = re.compile(r"(\d) points?\s*:\s*(\d+) seconds?")   # Kidney Shot: "1 point : 2 seconds  2 points: 3 seconds ..."
RUPTURE_POINTS = re.compile(r"(\d) points?\s*:\s*(\d[\d,]*) damage over (\d+) secs?")       # Rupture: "1 point : 159 damage over 8 secs ..."
MUT_POISONED = re.compile(r"[Dd]amage increased by (\d+)% against Poisoned")    # Mutilate: "Damage increased by 20% against Poisoned targets"
DAGGER_PCT = re.compile(r"(\d+)% (?:weapon damage )?\((\d+)% if a Dagger is equipped")            # Hemorrhage, Ghostly Strike: "100% weapon damage (145% if a Dagger is equipped)"
SHANK_ENERGY = re.compile(r"generating (\d+) Energy")                           # Shank: "... dealing 50% weapon damage and generating 15 Energy"
POISED = re.compile(r"Energy cost of your next Energy ability by (\d+)")       # Poised: "... reduces the Energy cost of your next Energy ability by 10"
HEMO_BLEED = re.compile(r"Rupture and Garrote abilities by (\d+)%")             # Hemorrhage: "... increases the damage of the caster's Rupture and Garrote abilities by 15%"

# Mutilate's flat amount per hand by rank: the 70753 tooltip says only "plus an additional amount with each weapon (Blizzard: the amount was
# also increased)". These are the strike spells' NORMALIZED_WEAPON_DMG base points in the raid simulator's spell store (wowsims/forever
# bac92dbd5, client 70707: spells 1310705/399960/1241585/1241586, 23/33/48/67; the 70630 tooltips had said "plus an additional 13/19/27/38
# with each weapon"), so a lower bound if 70753 raised them again. Replace them when a tooltip or the simulator gives the 70753 number.
MUT_FLAT_BY_RANK = {1: 23.0, 2: 33.0, 3: 48.0, 4: 67.0}
# Poison attack-power coefficients (Blizzard's notes 2026-11-02; the tooltips show none): Instant Poison 0.01 x attack power per hit (was
# 0.005), Deadly Poison 0.009 x attack power per stack over its duration (was 0.0045; the raid simulator splits it over the ticks).
POISON_AP = {"Instant Poison": 0.01, "Deadly Poison": 0.009}
# Rupture's attack power per tick by combo points (the raid simulator's rupture.go, ruptureApScaling); ticks every 2 s, 3 + points ticks.
RUPTURE_AP_PER_TICK = {1: 0.01, 2: 0.02, 3: 0.03, 4: 0.03, 5: 0.03}

TALENT_SPELLS = {"Riposte": "Riposte", "Blade Flurry": "Blade Flurry", "Adrenaline Rush": "Adrenaline Rush", "Cold Blood": "Cold Blood", "Mutilate": "Mutilate",
                 "Ghostly Strike": "Ghostly Strike", "Hemorrhage": "Hemorrhage", "Premeditation": "Premeditation", "Preparation": "Preparation",
                 "Death Mark": "Death Mark"}
# the abilities a talent names in its 70753 tooltip
COLD_BLOOD_SPELLS = ("Sinister Strike", "Backstab", "Ambush", "Eviscerate", "Mutilate")             # "your next ... by 100%": the first one spends it
REMORSELESS_SPELLS = ("Sinister Strike", "Backstab", "Ambush", "Mutilate", "Ghostly Strike")        # "your next ...": the first one spends it
OPPORTUNITY_SPELLS = ("Backstab", "Garrote", "Ambush", "Mutilate")                                    # Garrote's bleed through periodic_multiplier
AGGRESSION_SPELLS = ("Sinister Strike", "Eviscerate")                                                 # 70753: Backstab no longer
EFFICIENT_SPELLS = ("Sinister Strike", "Hemorrhage")                                                  # Efficient Strikes (was Improved Sinister Strike)
LETHALITY_SPELLS = ("Sinister Strike", "Gouge", "Backstab", "Mutilate", "Ghostly Strike", "Hemorrhage")
BLEEDS = ("Garrote", "Rupture")                                                                       # Hemorrhage +15%; stored twice by Death Mark


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
                name = sp["name"]
                s = Spell(name=name, school="physical", rank=int(NUM.search(r.get("rank") or "1").group(1)) if NUM.search(r.get("rank") or "") else 1,
                          level=int(r.get("level") or 1), cost=cost, cast=0.0, cooldown=_seconds(r.get("cooldown")), range=5.0,
                          kind="melee", resource="energy" if "Energy" in cost_txt else "none")
                s.text = txt
                s.interrupt = parse_interrupt(txt)
                pc, pw, fl, dt, st, cp, ev, ru, sd, po, ic = (rx.search(txt) for rx in (PCT, PLUS_WEAPON, FLAT, DOT, STUN, CP, EVIS, RUPTURE, SND, POISON, INCAP))
                if pw:
                    s.weapon_pct, s.dmg_min, s.dmg_max = 1.0, _num(pw.group(1)), _num(pw.group(1))
                elif pc:
                    s.weapon_pct = float(pc.group(1)) / 100
                    if pc.group(2):
                        s.dmg_min = s.dmg_max = _num(pc.group(2))
                elif fl and not ev:
                    s.dmg_min = s.dmg_max = _num(fl.group(1) or fl.group(2))
                if dt:
                    s.dot, s.dot_dur = _num(dt.group(1)), float(dt.group(2))
                    s.dot_ticks = max(1, int(round(s.dot_dur / 3.0)))
                if cp:
                    s.combo = int(cp.group(1))
                if ev:
                    s.evis = (_num(ev.group(1)), _num(ev.group(2)))   # 5-point damage; per point = a fifth of the way from the 1-point value
                    m1 = re.search(r"1 point : (\d[\d,]*)-(\d[\d,]*) damage", txt)
                    s.evis1 = (_num(m1.group(1)), _num(m1.group(2))) if m1 else (s.evis[0] / 5, s.evis[1] / 5)
                    s.dmg_min, s.dmg_max = s.evis   # rolled as the 5-point range, then scaled to the points spent (damage_multiplier)
                    s.combo = -1
                if ru:
                    s.rupture4 = (_num(ru.group(1)), float(ru.group(2)))
                    s.rupture_by_points = {int(a): (_num(b), float(c)) for a, b, c in RUPTURE_POINTS.findall(txt)}
                    s.combo = -1
                if name in ("Kidney Shot", "Slice and Dice", "Expose Armor", "Death Mark"):
                    s.combo = -1
                if name == "Death Mark":   # no damage of its own: the mark is applied in on_hit (death_mark), "cannot crit or miss" (Wowhead)
                    s.kind = "buff"
                if name == "Shank":   # its strike is resolved by shank() (off hand); the energy in on_hit
                    se = SHANK_ENERGY.search(txt)
                    s.shank_energy = float(se.group(1)) if se else 0.0
                if name == "Poised":
                    po_ = POISED.search(txt)
                    s.poised = float(po_.group(1)) if po_ else 0.0
                hb = HEMO_BLEED.search(txt)
                if hb:
                    s.hemo_bleed = float(hb.group(1)) / 100
                dg = DAGGER_PCT.search(txt)
                if dg:   # Hemorrhage, Ghostly Strike: the weapon share without and with a dagger in the main hand
                    s.weapon_pct, s.dagger_pct = float(dg.group(1)) / 100, float(dg.group(2)) / 100
                if name == "Kidney Shot":   # stun seconds by combo points spent, applied in on_swing (spell.stun stays 0: the engine's stun is fixed)
                    s.stun_by_points = {int(a): float(b) for a, b in PER_POINT_SECONDS.findall(txt)}
                if st:
                    s.stun = float(st.group(1))
                if ic:
                    s.stun = float(ic.group(1))
                if sd:
                    s.kind, s.snd = "buff", float(sd.group(1)) / 100
                if po:
                    s.kind = "buff"
                    s.poison_chance = float(po.group(1)) / 100
                    if po.group(2):
                        s.dmg_min, s.dmg_max, s.school = _num(po.group(2)), _num(po.group(3)), "nature"
                    else:
                        s.dot, s.dot_dur, s.dot_ticks, s.school = _num(po.group(4)), float(po.group(5)), 4, "nature"
                if name in ("Evasion", "Sprint", "Stealth", "Vanish", "Blade Flurry", "Adrenaline Rush", "Cold Blood", "Feint", "Distract",
                            "Premeditation", "Preparation", "Blind", "Sap", "Cheap Shot", "Kidney Shot", "Slice and Dice"):
                    s.kind = "buff"
                    if name in ("Cheap Shot", "Kidney Shot", "Gouge"):
                        s.kind = "melee"
                if name == "Kick":
                    s.kind = "melee"
                book.setdefault(name, []).append(s)
    for name in book:
        book[name].sort(key=lambda x: (x.level, x.rank))
    return book


BOOK = load_spellbook()


def talent_numbers():
    out = {}
    for tr in TREE["trees"]:
        for t in tr["talents"]:
            out[t["name"]] = [[float(x) for x in NUM.findall((rank or "").replace(",", ""))] for rank in t["ranks"]]
    return out


TNUM = talent_numbers()

MECHANICS = {
    "Improved Gouge": "+0.5s/rank Gouge",
    "Remorseless Attacks": "+20%/rank crit on the next Sinister Strike, Backstab, Ambush, Mutilate or Ghostly Strike within 20 s of a kill",
    "Malice": "+1%/rank crit",
    "Ruthlessness": "20%/rank chance for a combo point after a finisher",
    "Improved Slice and Dice": "+15%/rank Slice and Dice duration",
    "Relentless Strikes": "4%/rank per combo point: a finisher restores 25 energy",
    "Improved Expose Armor": "not used",
    "Lethality": "+10%/rank crit damage bonus on Sinister Strike, Gouge, Backstab, Mutilate, Ghostly Strike, Hemorrhage",
    "Vile Poisons": "+4%/rank poison damage",
    "Cold Blood": "a guaranteed crit every 3 min: cast right before a 5-point Eviscerate, spent by the next Sinister Strike, Backstab, Ambush, Eviscerate or Mutilate",
    "Improved Poisons": "+2%/rank poison application chance",
    "Vigor": "+5 max energy/rank",
    "Seal Fate": "33%/rank: a crit from a combo-point ability adds a point",
    "Improved Kidney Shot": "+5%/rank damage to a Kidney-Shot-stunned mob",
    "Blood Splatter": "Garrote +9 s (three more 3 s ticks), Rupture +6 s (three more 2 s ticks; Rupture is off by default)",
    "Coup de Grace": "+7/13/20% Eviscerate; Death Mark's storage rate and damage likewise",
    "Efficient Strikes": "-3/-5 energy Sinister Strike and Hemorrhage",
    "Lightning Reflexes": "+1%/rank dodge",
    "Puncturing Wounds": "+5%/rank crit on Mutilate (Backstab's crit and combo point: daggers from behind, never after the opener)",
    "Deflection": "+2%/rank parry",
    "Precision": "+1%/rank hit",
    "Endurance": "-30%/rank Sprint and Evasion cooldowns",
    "Riposte": "unlocks Riposte: 150% weapon damage and a 6 s disarm after a parry",
    "Improved Sprint": "travel only",
    "Improved Kick": "Kick on a casting mob: 50%/rank chance of 2 s more lockout (caster mobs: tables.MOB_CASTER_SHARE)",
    "Flawless Execution": "-15 energy Eviscerate",
    "Dual Wield Specialization": "+25%/rank off-hand damage (white swings, Shank, Mutilate's off-hand strike)",
    "Blade Flurry": "+20% attack speed for 15 s every 2 min",
    "Hack and Slash": "swords: 1%/rank chance per landed melee attack of an extra attack; daggers: +1%/rank crit with melee attacks (no maces in the lab)",
    "Weapon Expertise": "-1%/rank chance to be dodged or parried",
    "Aggression": "+5%/rank Sinister Strike and Eviscerate",
    "Adrenaline Rush": "double energy regen for 15 s every 5 min",
    "Camouflage": "-2s/rank Stealth cooldown, stealth speed",
    "Composure": "Poised: the opener costs 5/10 energy less on top of Poised's 10 (every pull starts at full energy)",
    "Flash of Steel": "Shank: +3 energy and -0.4 s cooldown per rank",
    "Master of Deception": "stealth only",
    "Opportunity": "+4%/rank Backstab, Garrote (the opener's bleed), Ambush, Mutilate",
    "Mutilate": "daggers: the builder from 40 (2 points for 60 energy; both hands strike for 90% weapon damage plus a flat amount, +20% on a "
                "Deadly-Poisoned mob, Seal Fate per critical strike); swords: not used",
    "Venom": "passive: a landed Shank raises poison damage 30% and poison chance by 20 points for 6 s (read like Improved Poisons' +2%/rank)",
    "Setup": "15%/rank: a combo point after dodging the target's own swing (an add's dodged swing gives none)",
    "Elusiveness": "not used",
    "Dirty Tricks": "not used",
    "Quick Getaway": "not used (Sap)",
    "Improved Ambush": "+15%/rank crit on Ambush (only the Subtlety playstyle casts Ambush)",
    "Initiative": "33%/rank: an extra combo point on Cheap Shot / Garrote / Ambush",
    "Ghostly Strike": "not used",
    "Heightened Senses": "not used",
    "Premeditation": "not used",
    "Serrated Blades": "attacks ignore 3%/rank armor, +10%/rank Rupture",
    "Dirty Deeds": "-10 energy/rank Cheap Shot and Garrote",
    "Preparation": "not used",
    "Hemorrhage": "not used (swords use Sinister Strike)",
    "Boot Knife": "20%/rank: a landed Shank adds 2 combo points (Shank is then also pressed as a builder below 4 points)",
    "Death Mark": "a finisher at DEATH_MARK_CP+ points while the mob has more than DEATH_MARK_HP of its health (10 s cooldown): stores "
                  "DEATH_MARK_STORE per point (an assumption: the tooltip gives no rate) of the damage dealt to the mob for 6 s, Garrote and "
                  "Rupture twice, then deals it (no cap, lost if the mob dies first)",
}
# Talent effects as the Subtlety playstyle plays them (spec strings starting with "subtlety"; documentation: MECHANICS is what the calibration
# reads). Since 2026-10-09 Opportunity, Improved Ambush and Serrated Blades' armor share apply in every playstyle.
SUBTLETY_MECHANICS = {
    "Hemorrhage": "the builder: 100% weapon damage, 145% with a dagger main hand (the tooltip's numbers); +15% to the rogue's Garrote and Rupture for 15 s",
    "Ghostly Strike": "on cooldown (20 s): 125% weapon damage, 180% with a dagger main hand, +15% dodge for 7 s; with Dirty Deeds a Garrote within "
                      "7 s while the mob has more than GHOSTLY_GARROTE_HP of its health and no Garrote is ticking",
    "Premeditation": "2 combo points as the pull starts (2 min cooldown, off the global cooldown during the approach)",
    "Preparation": "resets Evasion (and Premeditation, Ghostly Strike) when Evasion is wanted but on cooldown (10 min)",
    "Improved Ambush": "+15%/rank crit on Ambush",
    "Opportunity": "+4%/rank Backstab, Garrote, Ambush, Mutilate",
    "Initiative": "33%/rank: an extra combo point on Ambush, Cheap Shot, Garrote",
    "Serrated Blades": "attacks ignore 3%/rank of the mob's armor (Rupture bonus unused)",
    "Death Mark": "as in MECHANICS: preferred to a 5-point Eviscerate while the mob is above DEATH_MARK_HP",
}
FIT = {
    "Malice": "scale", "Ruthlessness": "scale", "Improved Slice and Dice": "scale", "Relentless Strikes": "scale", "Lethality": "scale",
    "Coup de Grace": "scale", "Efficient Strikes": "scale", "Lightning Reflexes": "scale", "Deflection": "scale", "Precision": "scale",
    "Endurance": "scale", "Riposte": "scale", "Flawless Execution": "scale", "Dual Wield Specialization": "scale", "Blade Flurry": "scale",
    "Hack and Slash": "scale", "Weapon Expertise": "scale", "Aggression": "scale", "Adrenaline Rush": "scale", "Remorseless Attacks": "scale",
    "Vile Poisons": "scale", "Improved Poisons": "scale", "Vigor": "scale", "Seal Fate": "scale", "Cold Blood": "scale", "Improved Kidney Shot": "scale",
    "Improved Gouge": "scale", "Camouflage": "scale", "Setup": "scale", "Initiative": "scale", "Serrated Blades": "scale", "Dirty Deeds": "scale",
    "Improved Sprint": "scale", "Opportunity": "scale", "Venom": "scale", "Blood Splatter": "scale", "Composure": "scale", "Flash of Steel": "scale",
    "Boot Knife": "scale", "Puncturing Wounds": "scale", "Death Mark": "scale",
}
SHARE_SOURCE = {"Melee": "white_mh", "Melee (off-hand)": "white_oh", "Sinister Strike": "sinister", "Eviscerate": "eviscerate", "Instant Poison": "poisons",
                "Deadly Poison": "poisons", "Rupture": "rupture", "Cheap Shot": "sinister", "Garrote": "garrote", "Riposte": "riposte", "Kidney Shot": "eviscerate",
                "Gouge": "sinister", "Hack and Slash": "white_mh", "Shank": "white_oh", "Death Mark": "eviscerate"}
NEW_SOURCES = {"garrote": {"id": "garrote", "share": 0.0, "min_level": 14, "tags": ["type:melee", "dot", "school:physical", "ability:Garrote", "opener", "weapon:sword"]},
               "riposte": {"id": "riposte", "share": 0.0, "min_level": 20, "tags": ["type:melee", "yellow", "school:physical", "ability:Riposte", "weapon:sword"], "cooldown": 6}}
KEY_TALENTS = ["Dual Wield Specialization", "Malice", "Coup de Grace"]
DESCRIPTION = ("Single-target leveling fights against normal mobs of your level with two swords (the daggers models: two daggers, still Sinister Strike: the mob faces you "
               "after the opener, so no Backstab): open from stealth behind the mob with Cheap Shot (Garrote before 26; the mob turns to face you after the opener, "
               "so it can parry from then on; Poised makes the opener 10 energy cheaper), Slice and Dice at 1-2 points when it is down, Shank whenever its energy "
               "would not overflow (from 24), Sinister Strike to 5 points, Eviscerate (Kidney Shot instead when below "
               "60% health, stunning for the tooltip's seconds per point), Eviscerate at fewer points when it would kill the mob, Cold Blood right before a 5-point "
               "Eviscerate, Riposte after a parry, Blade Flurry and Adrenaline Rush on the pull, Evasion when low; white swings with both hands (19% extra miss on "
               "white dual-wield hits), Instant Poison on the main hand and Deadly Poison on the off hand. Between fights: 2 s loot, 6 s travel, a bandage below 60% "
               "health (First Aid, 60 s cooldown), food below 65%; a death costs 90 s. The tuned rules (rotations/rogue-<spec>.json) veto spells and move the "
               "thresholds on top of this list.")
NOT_MODELLED = ("runners, adds, the stealth approach time, Expose Armor, Rupture by default (Eviscerate is used; the RUPTURE_HP knob lets rotation_opt try it at 5 points), Garrote's attack power bonus (its tooltip gives no number), "
                "Gouge-and-bandage, Vanish, Sprint, weapon skill, maces (Hack and Slash's armor share), gear upgrades within a level bracket, Death Mark's "
                "storage rate (an assumption, DEATH_MARK_STORE) and its cap, whether Shank is on the global cooldown (1.0 s assumed, like every rogue ability) "
                "and whether a dodged or parried Shank still gives its energy (assumed not), Ghostly Strike's stealthless Ambush (needs the mob's back).")
# rebuild.py: which scorer model, hand draft and optimizer build the pipeline calibrates, races and reports for this class
PIPELINE = {"variants": [{'spec': 'combat-swords-raid', 'opt': 'opt-combat-swords-raid-leveling-aoe', 'tag': 'aoe', 'profile': 'leveling-aoe', 'lookahead': 16, 'sets': ['MOBS_PER_PULL=2'], 'levels': '30,40,50,60', 'calibrate_levels': '40,60', 'label': 'Two-mob pulls with Blade Flurry'}], "spec": "combat-swords-raid", "hand": "leveling-combat-swords", "opt": "opt-combat-swords-raid-leveling-st", "tag": "combat", "lookahead": 16,
            "levels": "20,30,40,50,60", "calibrate_levels": "30,60",
            "extra_reports": [{"spec": "combat-daggers-raid", "build": "opt-combat-daggers-raid-leveling-st", "compare": ["opt-combat-swords-raid-leveling-st"]}]}


class RogueModule(BaseModule):
    # rotation knobs (rotation_opt.py tunes them; the defaults are the hand-written rotation): Rupture at 5 points instead of Eviscerate while
    # the mob has more than RUPTURE_HP (default 1.01, never: Rupture at 5 points finds the mob above 60% about once in 100 kills; Combat and
    # daggers playstyles only); Death Mark at DEATH_MARK_CP+ points while the mob has more than DEATH_MARK_HP of its health (it pays only for
    # the damage dealt in the next 6 s); Garrote after Ghostly Strike (Dirty Deeds builds) while the mob has more than GHOSTLY_GARROTE_HP.
    # The finisher Venom and its knobs (VENOM_HP, VENOM_CP) went with 70753: Venom is a passive on Shank now.
    RUPTURE_HP = 1.01
    DEATH_MARK_CP = 5
    DEATH_MARK_HP = 0.4
    GHOSTLY_GARROTE_HP = 0.5
    ROTATION_KNOBS = {"RUPTURE_HP": [1.01, 0.8, 0.6, 0.4], "DEATH_MARK_CP": [1, 3, 4, 5], "DEATH_MARK_HP": [0.0, 0.2, 0.4, 0.6],
                      "GHOSTLY_GARROTE_HP": [1.01, 0.7, 0.5, 0.3]}
    # Death Mark's storage per combo point: an ASSUMPTION (the 70753 tooltip and Blizzard's notes give no number; Wowhead lists a 6 s periodic
    # aura of value 1 and a server-side script): 10% of the damage dealt to the marked mob per point (50% at 5 points), Garrote and Rupture at
    # twice the rate (100% at 5), times Coup de Grace's storage rate and damage bonus. A sensitivity, not a measurement.
    DEATH_MARK_STORE = 0.10
    DEATH_MARK_SECONDS = 6.0
    # global cooldown of the 70753 abilities the client table (tables.spell_gcd, from the raid simulator's store) does not list yet: 1.0 s like
    # every other rogue ability (an assumption: the tooltip does not say whether Shank is off the global cooldown)
    NEW_GCD = {"Shank": 1.0, "Death Mark": 1.0}
    resource = "energy"
    melee = True
    eat_below = 0.65

    AOE = {'direct': [], 'min_near': 2}


    def extra_targets(self, fight, spell, white):
        """Blade Flurry: every melee attack also strikes one more mob in reach."""
        return 1 if fight.p.buff("Blade Flurry", fight.t) else 0

    def __init__(self, talents, level, spec="combat-swords-raid", gear="leveling"):
        self.t = {k: v for k, v in talents.items() if v > 0}
        self.level = level
        self.spec = spec
        self.sub = spec.startswith("subtlety")
        self.gear = gear
        self.book = {name: self.rank_at(name) for name in BOOK}
        self.spells = {n: s for n, s in self.book.items() if s is not None}
        for tname, sname in TALENT_SPELLS.items():
            if not self.t.get(tname):
                self.spells.pop(sname, None)
        if self.sub:
            dagger = "sword" not in spec
            self.mh_dagger = dagger
            if not dagger:
                self.spells.pop("Ambush", None)
                self.spells.pop("Backstab", None)
            for sname in ("Hemorrhage", "Ghostly Strike"):   # the tooltip's weapon share, with a dagger main hand its dagger share
                if sname in self.spells:   # copies: BOOK's Spell objects are shared by every module instance
                    sp = self.spells[sname]
                    pct = getattr(sp, "dagger_pct", sp.weapon_pct) if dagger else sp.weapon_pct
                    self.spells[sname] = dataclasses.replace(sp, weapon_pct=pct)
                    self.spells[sname].text = self.book[sname].text
        else:
            self.mh_dagger = "dagger" in spec   # daggers builds carry two daggers (1.8 s); the priority list is the same (no Backstab from the front)
            mu = self.spells.get("Mutilate")
            if mu is not None:   # "Requires Daggers": a dagger build's builder, resolved by mutilate() (both hands strike); swords never have it
                if self.mh_dagger:
                    po = MUT_POISONED.search(mu.text or "")
                    flat = MUT_FLAT_BY_RANK.get(mu.rank, 0.0)   # the 70753 tooltip gives no flat amount (see MUT_FLAT_BY_RANK)
                    self.spells["Mutilate"] = dataclasses.replace(mu, kind="buff", dmg_min=flat, dmg_max=flat)   # "buff": the engine counts the
                    self.spells["Mutilate"].text = mu.text                                                     # cast and calls on_hit
                    self.mutilate_poisoned = float(po.group(1)) / 100 if po else 0.0
                else:
                    self.spells.pop("Mutilate")
        # Shank (baseline from 24): "buff" so the engine counts the cast and calls on_hit, where shank() resolves the off-hand strike;
        # Flash of Steel: "+3 energy and -0.4 sec cooldown" a rank
        sh = self.spells.get("Shank")
        self.shank_energy = 0.0
        if sh is not None:
            self.shank_energy = getattr(sh, "shank_energy", 0.0) + self.tv("Flash of Steel", 0)
            self.spells["Shank"] = dataclasses.replace(sh, kind="buff", cooldown=max(0.0, sh.cooldown - self.tv("Flash of Steel", 1)))
            self.spells["Shank"].text = sh.text
            self.shank_strike = dataclasses.replace(sh, kind="melee", hand="oh", cooldown=0.0, cost=0.0)
        # Blood Splatter: "Increases the duration of your Rupture ability by 6 seconds and your Garrote ability by 9 seconds" (the same ticks, more of them)
        gar = self.spells.get("Garrote")
        if gar is not None and self.rank("Blood Splatter") and gar.dot_dur > 0:
            extra = self.tv("Blood Splatter", 1)
            ticks = gar.dot_ticks + int(round(extra / (gar.dot_dur / gar.dot_ticks)))
            self.spells["Garrote"] = dataclasses.replace(gar, dot=gar.dot * ticks / gar.dot_ticks, dot_dur=gar.dot_dur + extra, dot_ticks=ticks)
            self.spells["Garrote"].text = gar.text
        # Poised (level 18): out of combat at full energy the next energy ability costs 10 less; Composure 5/10 more
        po = self.book.get("Poised")
        self.poised = (getattr(po, "poised", 0.0) + self.tv("Composure", 0)) if po is not None else 0.0
        self.hemo_bleed = getattr(self.book.get("Hemorrhage"), "hemo_bleed", 0.0)
        self.weapon_kind = "dagger" if self.mh_dagger else "1h"   # the same kind in both hands; "1h" is a sword (Hack and Slash: an extra attack)
        self._fight = None
        self.opened = False
        self.armor_spell_used = "Instant Poison / Deadly Poison" if "Instant Poison" in self.spells else "none"

    def gcd_of(self, spell):
        g = self.NEW_GCD.get(spell.name)
        return g if g is not None else super().gcd_of(spell)

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

    def rank_at(self, name):
        ranks = [s for s in BOOK.get(name, []) if s.level <= self.level]
        return self.scale_rank(ranks[-1]) if ranks else None   # the rank at this level (row 8)

    # ------------------------------------------------------------ character
    def make_player(self, level):
        base = class_base_stats("rogue", level)
        g = gear_stats(level, self.gear, "rogue")
        strength = base["strength"] + g["strength"]
        agility = base["agility"] + g["agility"]
        stamina = base["stamina"] + g["stamina"]
        spirit = base["spirit"] + g["spirit"]
        p = Player(level=level, hp_max=class_base_health("rogue", level) + 10 * stamina, hp=0.0, mana_max=0.0, mana=0.0, base_mana=0.0,
                   spirit=spirit, intellect=base["intellect"], spell_power=0.0, armor=g["armor"], spell_crit=0.0,
                   dodge=class_dodge("rogue", level, agility) + self.tv("Lightning Reflexes", 0) / 100, ranged_crit=0.0)
        p.strength, p.agility, p.stamina = strength, agility, stamina
        p.attack_power = class_attack_power("rogue", level, strength, agility)
        p.melee_crit = class_melee_crit("rogue", level, agility) + self.tv("Malice", 0) / 100
        p.hit_bonus = self.tv("Precision", 0) / 100
        p.parry = 0.05 + self.tv("Deflection", 0) / 100
        kind = self.weapon_kind
        dps = weapon_dps(level, kind)
        p.mh = Weapon(dmg_min=dps * WEAPON_SPEED[kind] * 0.8, dmg_max=dps * WEAPON_SPEED[kind] * 1.2, speed=WEAPON_SPEED[kind], kind=kind)
        p.oh = Weapon(dmg_min=dps * WEAPON_SPEED[kind] * 0.8, dmg_max=dps * WEAPON_SPEED[kind] * 1.2, speed=WEAPON_SPEED[kind], kind=kind)
        p.energy_max = 100.0 + self.tv("Vigor", 0)
        p.energy = p.energy_max
        p.hp = p.hp_max
        return p

    def pull_range(self):
        return 20.0

    # ------------------------------------------------------------ engine hooks: numbers
    def mana_cost(self, spell):
        cost = spell.cost
        if spell.name in EFFICIENT_SPELLS:
            cost = max(0.0, cost - self.tv("Efficient Strikes", 0))   # "Reduces the Energy costs of Sinister Strike and Hemorrhage by 3."
        if spell.name == "Eviscerate":
            cost = max(0.0, cost - self.tv("Flawless Execution", 0))   # "Reduces the Energy cost of your Eviscerate ability by 15."
        if spell.name in ("Cheap Shot", "Garrote"):
            cost = max(0.0, cost - self.tv("Dirty Deeds", 0))
        return cost

    def final_cost(self, fight, spell, cost):
        """Poised: "When you are not in combat and have your maximum Energy, you will gain Poised. Poised reduces the Energy cost of your next
        Energy ability by 10" (Composure: 5/10 more). Every pull starts at full energy (engine.Session), so the opener (or Blade Flurry
        on the pull) gets it; set in on_fight_start, spent by the first energy ability."""
        if spell.resource == "energy" and cost > 0 and fight.p.buffs.pop("Poised", None) is not None:
            return max(0.0, cost - self.poised)
        return cost

    def hit_bonus(self, spell):
        if spell.name == "Shank":   # "Shank cannot Miss" (it can still be dodged or parried)
            return 1.0
        return 0.0

    def crit_bonus(self, spell, frozen):
        c = 0.0
        f = self._fight
        if f and spell.name in COLD_BLOOD_SPELLS and f.p.buff("Cold Blood", f.t):   # spent in on_swing by the first of these
            c += self.tv("Cold Blood", 0) / 100
        if f and spell.name in REMORSELESS_SPELLS and f.p.buff("Remorseless", f.t):   # likewise
            c += self.tv("Remorseless Attacks", 0) / 100
        if spell.name == "Ambush":
            c += self.tv("Improved Ambush", 0) / 100
        if spell.name == "Mutilate":   # Puncturing Wounds: "... and your Mutilate by 5%" (Backstab's 10%: never cast after the opener)
            c += self.tv("Puncturing Wounds", 1) / 100
        if self.weapon_kind == "dagger" and spell.kind == "melee" and spell.dot <= 0:   # Hack and Slash, Dagger/Fist: crit with weapon attacks
            c += self.tv("Hack and Slash", 1) / 100                                       # (not the poisons, not a bleed's ticks)
        return c

    def crit_damage_bonus(self, spell):
        if spell.name in LETHALITY_SPELLS:   # "Grants 10% increased Critical Strike damage" a rank: +0.10 on the x2.0 melee crit, as before 70753
            return self.tv("Lethality", 0) / 100
        return 0.0

    def damage_multiplier(self, spell, frozen):
        m = 1.0
        f = self._fight
        if spell.hand == "oh":   # white off-hand swings, Shank, Mutilate's off-hand strike
            m *= 1 + self.tv("Dual Wield Specialization", 0) / 100
        if spell.name in AGGRESSION_SPELLS:
            m *= 1 + self.tv("Aggression", 0) / 100
        if spell.name == "Eviscerate":
            m *= 1 + self.tv("Coup de Grace", 0) / 100
            cp = max(1, f.last_combo) if f else 5
            lo1, hi1 = spell.evis1
            lo5, hi5 = spell.evis
            avg = ((lo1 + hi1) / 2 + ((lo5 + hi5) / 2 - (lo1 + hi1) / 2) * (cp - 1) / 4) + 0.03 * cp * (f.p.attack_power if f else 0.0)
            m *= avg / ((lo5 + hi5) / 2)
        if spell.name in OPPORTUNITY_SPELLS:   # every playstyle: the Combat lists open with Garrote too (its bleed goes through here)
            m *= 1 + self.tv("Opportunity", 0) / 100
        if spell.school == "nature":
            m *= 1 + self.tv("Vile Poisons", 0) / 100
            ven = f.p.buff("Venom", f.t) if f else None
            if ven:
                m *= 1 + ven["dmg"]
        if spell.name == "Rupture":
            m *= 1 + self.tv("Serrated Blades", 1) / 100
        if spell.name in BLEEDS and f and f.m.debuffs.get("Hemorrhage", {}).get("until", 0) > f.t:
            m *= 1 + self.hemo_bleed   # Hemorrhage: "increases the damage of the caster's Rupture and Garrote abilities by 15%" (snapshot at application)
        if f and f.m.stunned(f.t) and f.m.debuffs.get("Kidney Shot", {}).get("until", 0) > f.t:
            m *= 1 + self.tv("Improved Kidney Shot", 0) / 100
        return m

    def periodic_can_crit(self, spell):
        return True

    def health_regen(self, p):
        return class_health_regen_tick("rogue", p.spirit)

    def swing_speed_factor(self):
        f = self._fight
        if f is None:
            return 1.0
        factor = 1.0
        snd = f.p.buff("Slice and Dice", f.t)
        if snd:
            factor /= 1 + snd.get("speed", 0.2)
        if f.p.buff("Blade Flurry", f.t):
            factor /= 1 + (self.tv("Blade Flurry", 0) or 20.0) / 100   # "Increases your melee attack speed by 20% ..."
        return factor

    def dodge_parry_reduction(self):
        return self.tv("Weapon Expertise", 0) / 100   # 2026-09-27: the engine now applies it (it measured 0.0 before)

    def attacks_from_front(self):
        return self.opened   # the opener lands from behind; the mob turns to face you afterwards

    def resist_factor(self):
        return 1.0

    # ------------------------------------------------------------ engine hooks: events
    def on_fight_start(self, fight):
        self._fight = fight
        p, m, t = fight.p, fight.m, fight.t
        self.opened = False
        m.dist = MELEE_RANGE          # stealthed up to the mob
        m.in_melee = True
        m.swing_at = t + 1.5          # it needs a moment to turn
        p.swing_mh, p.swing_oh = t + 0.5, t + p.oh.speed / 2   # the opener goes first
        p.combo = 0
        if self.poised > 0 and p.energy >= p.energy_max:   # Poised: out of combat at full energy (every pull starts there)
            p.buffs["Poised"] = {"until": t + 3600.0}
        bf = self.spells.get("Blade Flurry")
        if bf is not None and p.ready("Blade Flurry", t) and p.energy >= bf.cost:
            p.energy -= self.final_cost(fight, bf, bf.cost)   # pressed on the pull: Poised goes to it
            p.buffs["Blade Flurry"] = {"until": t + (self.tv("Blade Flurry", 1) or 15.0)}   # "... Lasts 15 sec."
            p.cooldowns["Blade Flurry"] = t + bf.cooldown
        ar = self.spells.get("Adrenaline Rush")
        if ar is not None and p.ready("Adrenaline Rush", t):
            p.buffs["Adrenaline Rush"] = {"until": t + (self.tv("Adrenaline Rush", 1) or 15.0)}   # "... by 100% for 15 sec."
            p.cooldowns["Adrenaline Rush"] = t + ar.cooldown
        # Cold Blood is no longer pressed at the pull: decide() casts it right before a 5-point Eviscerate (cold_blood)
        ignore = self.tv("Serrated Blades", 0) / 100   # every playstyle: "Causes your attacks to ignore 3% of your target's Armor"
        if ignore:
            for mob in [m] + list(fight.others()):
                mob.armor_debuff = max(mob.armor_debuff, mob.armor * ignore)
        if self.sub:
            pm = self.spells.get("Premeditation")
            if pm is not None and p.ready("Premeditation", t):   # cast on the approach (20 yd), before the opener
                p.combo = min(5, p.combo + 2)
                p.cooldowns["Premeditation"] = t + pm.cooldown
                fight.casts["Premeditation"] = fight.casts.get("Premeditation", 0) + 1

    def on_regen_tick(self, fight, p, t):
        if p.buff("Adrenaline Rush", t):   # "Increases your Energy regeneration rate by 100%": one more tick's worth
            p.energy = min(p.energy_max, p.energy + tables.ENERGY_PER_TICK * (self.tv("Adrenaline Rush", 0) or 100.0) / 100)

    def interrupt_bonus(self, fight, spell):
        if spell.name == "Kick" and self.rank("Improved Kick") and fight.rng.random() < self.tv("Improved Kick", 0) / 100:
            return self.tv("Improved Kick", 1)
        return 0.0

    def dodge_bonus(self, fight):
        p, t = fight.p, fight.t
        b = 0.5 if p.buff("Evasion", t) else 0.0
        if p.buff("Ghostly Strike", t):
            b += 0.15
        return b

    # ------------------------------------------------------------ Death Mark
    def mark_store(self, fight, name, amount):
        """Death Mark: "storing a portion of the damage dealt by your attacks per Combo Point. Garrote and Rupture damage is stored at twice
        the rate." The stored damage sits in the mark's one pending tick on the marked mob (engine dots: [name, per tick, ticks, next, ...]),
        so the engine deals it when the 6 s run out; damage to another mob of the pull is not stored, and a mob that dies first takes it along."""
        if amount <= 0 or name == "Death Mark":
            return
        for d in fight.m.dots:
            if d[0] == "Death Mark" and d[2] > 0 and len(d) > 7:
                d[1] += amount * d[7] * (2.0 if name in BLEEDS else 1.0)

    def death_mark(self, fight):
        cp = max(1, fight.last_combo)
        cdg = 1 + self.tv("Coup de Grace", 1) / 100   # "the damage and storage rate of your Death Mark ability by 7%"
        rate = self.DEATH_MARK_STORE * cp * cdg * cdg
        fight.refresh_dot("Death Mark", 1e-6, 1, self.DEATH_MARK_SECONDS, 0.0, 1.0)   # "cannot crit" (Wowhead)
        for d in fight.m.dots:
            if d[0] == "Death Mark":
                d[1] = 0.0
                d.append(rate)   # d[7]: the storage rate (the engine reads d[0..6] only)
        fight.note(f"Death Mark {cp} points: stores {rate:.0%} for {self.DEATH_MARK_SECONDS:.0f}s")

    def on_tick(self, fight, spell, amount, crit):
        self.mark_store(fight, spell.name, amount)   # Garrote, Rupture (twice), Deadly Poison

    def on_swing(self, fight, spell, outcome, amount, hand):
        p, m, t = fight.p, fight.m, fight.t
        if spell.name in ("Cheap Shot", "Garrote", "Kidney Shot", "Ambush"):
            self.opened = True
        # one-use boosts: the first ability the tooltip names spends them, landed or not (its attack-table roll already had the crit)
        if spell.name in COLD_BLOOD_SPELLS:
            p.buffs.pop("Cold Blood", None)
        if spell.name in REMORSELESS_SPELLS:
            p.buffs.pop("Remorseless", None)
        if spell.name == "Garrote":
            p.buffs.pop("Ghostly Opening", None)
        if outcome == "parry" and "Riposte" in self.spells:
            p.buffs["Riposte"] = {"until": t + 5.0}
        if outcome in ("miss", "dodge", "parry"):
            return
        self.mark_store(fight, spell.name, amount)
        if spell.name == "Kidney Shot":   # "Lasts longer per combo point: 1 point : 2 seconds ... 5 points: 6 seconds"
            dur = getattr(spell, "stun_by_points", {}).get(max(1, min(5, fight.last_combo)), spell.stun)
            m.debuffs["Kidney Shot"] = {"until": t + dur, "stacks": 1}
            if dur > 0:
                m.stun_until = max(m.stun_until, t + dur)
                if m.casting(t):
                    m.cast_end = -1.0   # a stun breaks the mob's cast, as engine.apply_control does for a fixed stun
        # poisons: Instant Poison on main-hand hits, Deadly Poison on off-hand hits
        chance_bonus = self.tv("Improved Poisons", 0) / 100
        ven = p.buff("Venom", t)
        if ven:
            chance_bonus += ven["chance"]
        ip, dp = self.spells.get("Instant Poison"), self.spells.get("Deadly Poison")
        if hand == "mh" and ip is not None and fight.rng.random() < ip.poison_chance + chance_bonus:
            self.poison_hit(fight, ip)
        if hand == "oh" and dp is not None and fight.rng.random() < dp.poison_chance + chance_bonus:
            b = m.debuffs.get("Deadly Poison")
            stacks = min(5, (b["stacks"] if b and b["until"] > t else 0) + 1)
            m.debuffs["Deadly Poison"] = {"until": t + dp.dot_dur, "stacks": stacks}
            per_stack = dp.dot + POISON_AP["Deadly Poison"] * p.attack_power   # Blizzard 2026-11-02: 0.009 x attack power a stack
            fight.refresh_dot("Deadly Poison", per_stack * stacks * self.damage_multiplier(dp, False), dp.dot_ticks, dp.dot_dur / dp.dot_ticks, p.melee_crit, 2.0)
        # extra attacks (Hack and Slash, Axe/Sword: "Your successful melee attacks have a 1% chance to trigger an extra attack": white and
        # yellow hits; daggers get crit instead, crit_bonus), combo points from crits (Seal Fate)
        if (self.weapon_kind == "1h" and spell.kind == "melee" and spell.name != "Hack and Slash" and self.rank("Hack and Slash")
                and not getattr(fight, "_extra", False) and fight.rng.random() < self.tv("Hack and Slash", 0) / 100):
            fight._extra = True
            fight.resolve_attack(Spell("Hack and Slash", "physical", kind="melee", resource="none"), white=True, hand="mh")
            fight._extra = False
        if outcome == "crit" and spell.combo > 0 and self.rank("Seal Fate") and fight.rng.random() < self.tv("Seal Fate", 0) / 100:
            p.combo = min(5, p.combo + 1)
        if spell.name in ("Cheap Shot", "Garrote", "Ambush") and self.rank("Initiative") and fight.rng.random() < self.tv("Initiative", 0) / 100:
            p.combo = min(5, p.combo + 1)

    def poison_hit(self, fight, ip):
        p, m = fight.p, fight.m
        # Blizzard 2026-11-02: 0.01 x attack power a hit
        amount = (fight.rng.uniform(ip.dmg_min, ip.dmg_max) + POISON_AP["Instant Poison"] * p.attack_power) * self.damage_multiplier(ip, False)
        crit = fight.rng.random() < p.melee_crit
        if crit:
            amount *= 1.5
        fight.deal(Spell("Instant Poison", "nature"), amount, crit)
        fight.note(f"Instant Poison{' CRIT' if crit else ''} {amount:.0f} -> mob {max(0, m.hp):.0f}")
        self.mark_store(fight, "Instant Poison", amount)

    def shank(self, fight):
        """Shank: "Instantly strike with your off-hand weapon, dealing 50% weapon damage and generating 15 Energy. Shank cannot Miss." The
        strike goes through the engine's attack (the off-hand halving like every off-hand attack in the lab, Dual Wield Specialization,
        armor, the off hand's poison, Blade Flurry); the engine already counted the cast, so the strike's own count is taken back. The
        energy (with Flash of Steel), Venom and Boot Knife come with a landed strike (on_hit); a dodged or parried Shank gives nothing."""
        fight.resolve_attack(self.shank_strike, white=False, hand="oh")
        fight.casts["Shank"] = fight.casts.get("Shank", 1) - 1

    def on_hit(self, fight, spell, amount, crit, frozen):
        p, m, t = fight.p, fight.m, fight.t
        if spell.name == "Mutilate" and spell.kind == "buff":   # the cast (the engine routes it here): both strikes
            self.mutilate(fight, spell)
            return
        if spell.name == "Shank":
            if spell.kind == "buff":   # the cast: resolve the off-hand strike
                self.shank(fight)
                return
            p.energy = min(p.energy_max, p.energy + self.shank_energy)
            if self.rank("Venom"):   # "Causes your Shank ability to increase your Poison damage by 30% and your chance to apply Poisons by 20% for 6 seconds."
                p.buffs["Venom"] = {"until": t + self.tv("Venom", 2), "dmg": self.tv("Venom", 0) / 100, "chance": self.tv("Venom", 1) / 100}
            if self.rank("Boot Knife") and fight.rng.random() < self.tv("Boot Knife", 0) / 100:   # "a 20% chance to add 2 Combo Points"
                p.combo = min(5, p.combo + 2)
            return
        if spell.name == "Death Mark":
            self.death_mark(fight)
        if spell.name == "Slice and Dice":
            cp = max(1, fight.last_combo)
            dur = (9.0 + 3.0 * (cp - 1)) * (1 + self.tv("Improved Slice and Dice", 0) / 100)
            p.buffs["Slice and Dice"] = {"until": t + dur, "speed": getattr(spell, "snd", 0.2)}
            fight.note(f"Slice and Dice {dur:.0f}s")
        if spell.name == "Evasion":
            p.buffs["Evasion"] = {"until": t + 15.0}
        if spell.name == "Riposte":
            m.debuffs["Disarmed"] = {"until": t + 6.0, "stacks": 1}
            p.buffs.pop("Riposte", None)
        if spell.name == "Rupture" and amount == 0:
            # "1 point : 159 damage over 8 secs ... 5 points: 469 damage over 16 secs": 2 s ticks; attack power per tick from the raid simulator
            # (RUPTURE_AP_PER_TICK); Blood Splatter: "+6 seconds" (three more ticks of the same size)
            cp = max(1, min(5, fight.last_combo))
            base, dur = getattr(spell, "rupture_by_points", {}).get(cp) or (spell.rupture4[0] * (0.6 + 0.1 * cp), 6.0 + 2.0 * cp)
            ticks = max(1, int(round(dur / 2.0)))
            per_tick = base / ticks + RUPTURE_AP_PER_TICK[cp] * p.attack_power
            ticks += int(round(self.tv("Blood Splatter", 0) / 2.0))
            fight.refresh_dot("Rupture", per_tick * ticks * self.damage_multiplier(spell, False), ticks, 2.0, p.melee_crit, 2.0)
        if spell.combo < 0:   # "Your finishing moves ...": every finisher, Slice and Dice and Death Mark included
            if self.rank("Ruthlessness") and fight.rng.random() < self.tv("Ruthlessness", 0) / 100:
                p.combo = min(5, p.combo + 1)
            # "Your finishing moves have a 4% chance per Combo Point to restore 25 Energy." (a rank)
            if self.rank("Relentless Strikes") and fight.rng.random() < self.tv("Relentless Strikes", 0) / 100 * max(1, fight.last_combo):
                p.energy = min(p.energy_max, p.energy + self.tv("Relentless Strikes", 1))
        # (Cold Blood and Remorseless Attacks are spent in on_swing)
        if spell.name == "Hemorrhage":   # "... increases the damage of the caster's Rupture and Garrote abilities by 15%. Lasts 15 sec."
            m.debuffs["Hemorrhage"] = {"until": t + 15.0, "stacks": 1}
        if self.sub:
            if spell.name == "Ghostly Strike":
                p.buffs["Ghostly Strike"] = {"until": t + 7.0}
                # "Also causes your next Ambush or Garrote cast within 7 seconds to not require Stealth" (Garrote from the front needs Dirty Deeds)
                p.buffs["Ghostly Opening"] = {"until": t + 7.0}
            if spell.name == "Preparation":
                for n in ("Evasion", "Premeditation", "Ghostly Strike", "Vanish", "Sprint", "Cold Blood", "Kick", "Gouge", "Kidney Shot", "Riposte", "Blind",
                          "Shank", "Death Mark"):
                    p.cooldowns.pop(n, None)
                fight.note("Preparation: cooldowns reset")

    def on_miss(self, fight, spell):
        # a finisher that misses or is dodged or parried keeps its combo points (engine.spend took them before the roll; the raid
        # simulator spends them only on a landed finisher); its energy stays spent
        if spell.combo < 0 and fight.last_combo > 0:
            fight.p.combo = max(fight.p.combo, fight.last_combo)

    def on_dodge(self, fight):
        # Setup: "add a Combo Point to your target after Dodging one of their attacks": only the target's own swings (combo points sit on
        # the target); until 2026-10-18 an add's dodged swing gave one too (pulls of several mobs only; audit 2026-10-18 #23)
        if (fight.swinging or fight.m) is not fight.m:   # engine.Fight.swinging: the mob whose swing is being resolved
            return
        if self.rank("Setup") and fight.rng.random() < self.tv("Setup", 0) / 100:
            fight.p.combo = min(5, fight.p.combo + 1)

    def after_cast(self, fight, spell):
        p, t = fight.p, fight.t
        if spell.cooldown > 0:
            p.cooldowns[spell.name] = t + spell.cooldown
        if spell.name == "Evasion":
            p.cooldowns["Evasion"] = t + spell.cooldown * (1 - self.tv("Endurance", 0) / 100)

    def on_kill(self, fight):
        p, t = fight.p, fight.t
        if self.rank("Remorseless Attacks"):
            p.buffs["Remorseless"] = {"until": t + 20.0}

    def after_fight(self, p, t):
        for n in ("Evasion", "Slice and Dice", "Blade Flurry", "Adrenaline Rush", "Venom", "Ghostly Opening"):
            p.buffs.pop(n, None)
        if self.sub:
            p.buffs.pop("Ghostly Strike", None)
        if p.hp < 0.60 * p.hp_max and p.cooldowns.get("Bandage", -1.0) <= t:
            p.hp = min(p.hp_max, p.hp + bandage_heal(p.level))
            p.cooldowns["Bandage"] = t + 60.0
            return 8.0
        return 0.0

    # ------------------------------------------------------------ priority list
    def evis_estimate(self, p, evis, cp):
        """An Eviscerate's expected damage at `cp` points after an assumed 35% armor (the kill-shot check)."""
        lo1, hi1 = evis.evis1
        lo5, hi5 = evis.evis
        return (((lo1 + hi1) / 2 + ((lo5 + hi5) / 2 - (lo1 + hi1) / 2) * (cp - 1) / 4 + 0.03 * cp * p.attack_power)
                * (1 + self.tv("Coup de Grace", 0) / 100) * (1 + self.tv("Aggression", 0) / 100) * (1 - 0.35))

    def shank_wanted(self, fight, can):
        """Shank whenever it is ready and the energy it nets would not overflow; with Boot Knife also as a builder below 4 points."""
        sh = self.spells.get("Shank")
        if sh is None or not can(sh):
            return None
        p = fight.p
        net = self.shank_energy - self.mana_cost(sh)
        if p.energy + net <= p.energy_max or (self.rank("Boot Knife") and p.combo <= 3):
            return sh
        return None

    def death_mark_wanted(self, fight, can):
        """Death Mark (a finisher, 10 s cooldown) at DEATH_MARK_CP+ points while the mob has more than DEATH_MARK_HP of its health, so it lives
        through the 6 s the mark stores (Death Mark's own condition: no mark already on the mob)."""
        dm = self.spells.get("Death Mark")
        p, m = fight.p, fight.m
        if (dm is not None and p.combo >= self.DEATH_MARK_CP and m.hp > self.DEATH_MARK_HP * m.hp_max and not fight.dot_active("Death Mark")
                and can(dm)):
            return dm
        return None

    def decide(self, fight):
        if fight.others():   # a pull of several mobs: the area priority first (engine.BaseModule.decide_aoe, AOE below)
            r = self.decide_aoe(fight)
            if r is not None:
                return r
        if self.sub:
            return self.decide_subtlety(fight)
        p, m, t = fight.p, fight.m, fight.t
        sp = self.spells

        def can(s):
            return s is not None and p.ready(s.name, t) and fight.can_afford(s, self.mana_cost(s))

        cs, gar, ss, evis, snd, ks, rip, eva, gouge = (sp.get(n) for n in ("Cheap Shot", "Garrote", "Sinister Strike", "Eviscerate", "Slice and Dice", "Kidney Shot", "Riposte", "Evasion", "Gouge"))
        hp = m.hp
        # opener from stealth
        if not self.opened:
            if cs and can(cs):
                return cs
            if gar and can(gar):
                return gar
            self.opened = True
        if eva and can(eva) and p.hp < 0.50 * p.hp_max and hp > 0.3 * m.hp_max and not p.buff("Evasion", t):
            return eva
        kick = sp.get("Kick")
        if m.caster and m.casting(t) and kick and can(kick):
            return kick
        if rip and can(rip) and p.buff("Riposte", t):
            return rip
        # finishers
        if evis and can(evis) and p.combo >= 1 and hp <= self.evis_estimate(p, evis, p.combo) * 0.95:
            return evis
        if snd and can(snd) and p.combo >= 1 and not p.buff("Slice and Dice", t) and hp > 0.5 * m.hp_max and (p.combo <= 2 or hp > 0.8 * m.hp_max):
            return snd
        dm = self.death_mark_wanted(fight, can)   # builds holding the talent (Subtlety row 7, from 40)
        if dm is not None:
            return dm
        sh = self.shank_wanted(fight, can)   # from 24: free energy (and Venom's poison buff, Boot Knife's points)
        if sh is not None:
            return sh
        if p.combo >= 5:
            if ks and can(ks) and p.hp < 0.6 * p.hp_max and not m.stunned(t) and hp > 0.25 * m.hp_max:
                return ks
            rup = sp.get("Rupture") if self.RUPTURE_HP <= 1.0 else None   # off by default (RUPTURE_HP 1.01)
            if rup is not None and hp > self.RUPTURE_HP * m.hp_max and not fight.dot_active("Rupture") and can(rup):
                return rup
            if evis and can(evis):
                self.cold_blood(fight, can)
                return evis
        mu = sp.get("Mutilate")   # dagger builds holding the talent (from 40): the builder, 2 points for 60 energy against Sinister Strike's 1
        if mu is not None:
            if can(mu):
                return mu
            if p.energy < self.mana_cost(mu):
                return None   # wait for the energy; Sinister Strike only when a tuned rule holds Mutilate back
        if ss and can(ss):
            return ss
        return None

    def mutilate(self, fight, spell):
        """Mutilate (the raid simulator's registerMutilate): one roll for the cast (miss, dodge, parry); when it lands, 2 combo points, then
        an off-hand and a main-hand strike, each the tooltip's weapon share (90% since 70753) plus the rank's flat amount (MUT_FLAT_BY_RANK), with its own crit roll (Cold Blood,
        Remorseless Attacks, Hack and Slash's dagger crit, Lethality and Opportunity through the usual hooks; Seal Fate per critical
        strike), +20% while Deadly Poison is on the mob (the lab's only poison with a debuff), each strike able to apply its hand's poison.
        The off hand's weapon damage is halved and its flat amount is not (the simulator's OHNormalizedWeaponDamage). Weapon damage at
        the dagger's own speed like every yellow attack in the lab (the simulator normalizes daggers to 1.7 s); a missed cast keeps its
        energy spent like the lab's other builders (the simulator refunds part of it)."""
        p, m = fight.p, fight.m
        strikes = [dataclasses.replace(spell, kind="melee", hand=h) for h in ("oh", "mh")]
        outcome = fight.attack_table(strikes[1], False, "mh")
        if outcome in ("miss", "dodge", "parry"):
            fight.note(f"Mutilate {outcome.upper()}")
            self.on_swing(fight, strikes[1], outcome, 0.0, "mh")
            self.on_miss(fight, strikes[1])
            return
        p.combo = min(5, p.combo + spell.combo)
        crits = [fight.rng.random() < p.melee_crit + self.crit_bonus(s, False) for s in strikes]   # before on_swing spends Cold Blood
        for s, crit in zip(strikes, crits):
            if m.hp <= 0:
                break   # the off-hand strike killed it
            weapon = p.oh if s.hand == "oh" else p.mh
            amount = fight.rng.uniform(s.dmg_min, s.dmg_max) + s.weapon_pct * fight.weapon_damage(weapon) * (0.5 if s.hand == "oh" else 1.0)
            amount *= self.damage_multiplier(s, False)
            if m.debuffs.get("Deadly Poison", {}).get("until", 0) > fight.t:
                amount *= 1 + self.mutilate_poisoned
            if crit:
                amount *= 2.0 + self.crit_damage_bonus(s)
            amount *= 1.0 - armor_mitigation(m.effective_armor(), p.level)
            fight.deal(s, amount, crit)
            fight.note(f"Mutilate ({s.hand}){' CRIT' if crit else ''} {amount:.0f} -> mob {max(0, m.hp):.0f}")
            self.on_swing(fight, s, "crit" if crit else "hit", amount, s.hand)
            extra = self.extra_targets(fight, s, False) if fight.others() else 0
            if extra > 0:
                fight.hit_others_melee(s, extra, False, s.hand)

    def cold_blood(self, fight, can):
        """Cold Blood (no global cooldown) right before a 5-point Eviscerate, so its sure crit lands on the biggest hit: the next Sinister
        Strike, Backstab, Ambush, Eviscerate or Mutilate spends it (on_swing). Not before an Eviscerate that kills anyway (the
        kill-shot line above returns first)."""
        cb = self.spells.get("Cold Blood")
        p, t = fight.p, fight.t
        if cb is not None and can(cb) and not p.buff("Cold Blood", t):
            p.buffs["Cold Blood"] = {"until": t + 60.0}
            p.cooldowns["Cold Blood"] = t + cb.cooldown
            fight.casts["Cold Blood"] = fight.casts.get("Cold Blood", 0) + 1
            fight.note("Cold Blood")

    def opener_order(self, fight, amb, gar, builder):
        """Ambush or Garrote first, whichever is worth more: its expected damage minus the energy it costs (valued at the damage
        per energy of a builder-to-5-points-then-Eviscerate cycle). Garrote's bleed ignores armor and costs less (Dirty Deeds), but
        it only pays for the ticks the mob lives through, so Ambush wins in short low-level fights. Cheap Shot is the fallback."""
        if amb is None or gar is None or builder is None:
            return [amb, gar]
        p, m = fight.p, fight.m
        w = (p.mh.dmg_min + p.mh.dmg_max) / 2 + p.attack_power / 14.0 * p.mh.speed
        armor = 1.0 - armor_mitigation(m.effective_armor(), p.level)
        crit = p.melee_crit
        b_dmg = (builder.weapon_pct * w + (builder.dmg_min + builder.dmg_max) / 2) * (1 + crit) * armor
        b_cost = max(1.0, self.mana_cost(builder))
        cyc_dmg, cyc_cost = 5 * b_dmg, 5 * b_cost
        evis = self.spells.get("Eviscerate")
        if evis is not None:
            lo5, hi5 = evis.evis
            cyc_dmg += ((lo5 + hi5) / 2 + 0.15 * p.attack_power) * (1 + self.tv("Coup de Grace", 0) / 100) * (1 + self.tv("Aggression", 0) / 100) * (1 + crit) * armor
            cyc_cost += self.mana_cost(evis)
        dpe = cyc_dmg / cyc_cost
        opp = 1 + self.tv("Opportunity", 0) / 100
        # crit_bonus: Improved Ambush, plus Remorseless Attacks right after a kill and Hack and Slash with a dagger
        v_amb = (amb.weapon_pct * w + (amb.dmg_min + amb.dmg_max) / 2) * (1 + min(1.0, crit + self.crit_bonus(amb, False))) * armor * opp - dpe * self.mana_cost(amb)
        # expected fight length: white swings (both hands, ~25% missed or avoided), 10 energy a second at the cycle's rate, the bleed
        white = w / p.mh.speed * (1 + (0.5 if p.oh is not None else 0.0)) * (1 + crit) * armor * 0.75
        fight_len = m.hp / max(1.0, white + dpe * 10.0 + gar.dot / max(1.0, gar.dot_dur))
        v_gar = gar.dot * opp * min(1.0, fight_len / max(1.0, gar.dot_dur)) - dpe * self.mana_cost(gar)
        return [amb, gar] if v_amb >= v_gar else [gar, amb]

    def decide_subtlety(self, fight):
        """Subtlety leveling: Ambush opener (Premeditation's points already on the mob), Ghostly Strike on cooldown (with Dirty Deeds a Garrote
        behind it), Death Mark at 5 points, Shank for energy, Hemorrhage builder."""
        p, m, t = fight.p, fight.m, fight.t
        sp = self.spells

        def can(s):
            return s is not None and p.ready(s.name, t) and fight.can_afford(s, self.mana_cost(s))

        amb, cs, gar, hemo, gs, ss, evis, snd, ks, rip, eva, prep = (sp.get(n) for n in (
            "Ambush", "Cheap Shot", "Garrote", "Hemorrhage", "Ghostly Strike", "Sinister Strike", "Eviscerate", "Slice and Dice",
            "Kidney Shot", "Riposte", "Evasion", "Preparation"))
        hp = m.hp
        if not self.opened:
            for s in self.opener_order(fight, amb, gar, hemo or ss) + [cs]:
                if s is not None and can(s):
                    return s
            self.opened = True
        if eva and p.hp < 0.50 * p.hp_max and hp > 0.3 * m.hp_max and not p.buff("Evasion", t):
            if can(eva):
                return eva
            if prep and can(prep):
                return prep
        kick = sp.get("Kick")
        if m.caster and m.casting(t) and kick and can(kick):
            return kick
        if rip and can(rip) and p.buff("Riposte", t):
            return rip
        if evis and can(evis) and p.combo >= 1 and hp <= self.evis_estimate(p, evis, p.combo) * 0.95:
            return evis
        # Ghostly Strike: "your next Ambush or Garrote cast within 7 seconds [does] not require Stealth"; Ambush still needs the mob's back,
        # Garrote not with Dirty Deeds ("no longer requires you to be behind your target"): a fresh bleed while the mob has GHOSTLY_GARROTE_HP
        if (gar and self.rank("Dirty Deeds") and p.buff("Ghostly Opening", t) and not fight.dot_active("Garrote")
                and hp > self.GHOSTLY_GARROTE_HP * m.hp_max and can(gar)):
            return gar
        if snd and can(snd) and p.combo >= 1 and not p.buff("Slice and Dice", t) and hp > 0.5 * m.hp_max and (p.combo <= 2 or hp > 0.8 * m.hp_max):
            return snd
        dm = self.death_mark_wanted(fight, can)   # the Subtlety capstone (row 7, from 40): before a 5-point Eviscerate while the mob lives 6 s more
        if dm is not None:
            return dm
        sh = self.shank_wanted(fight, can)   # from 24: free energy (Boot Knife: also 2 points)
        if sh is not None:
            return sh
        if p.combo >= 5:
            if ks and can(ks) and p.hp < 0.6 * p.hp_max and not m.stunned(t) and hp > 0.25 * m.hp_max:
                return ks
            if evis and can(evis):
                self.cold_blood(fight, can)
                return evis
            return None   # pool energy for the finisher rather than waste a builder's point
        if gs and can(gs):
            return gs
        builder = hemo or ss
        if builder and can(builder):
            return builder
        return None
