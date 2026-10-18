"""Rogue module for the fight lab (Combat swords leveling).

Spell ranks are read from `_reference/data/forever-spells/rogue.json` (beta client build 1.60.1.70291); talent numbers from
each rank's tooltip in `_reference/data/forever-talents/rogue.json`. Weapons: a quest-green sword in each hand by level
(`tables.weapon_dps`, 2.6 speed; "dagger" in the spec string: two daggers, 1.8 speed), attack power from the client's base stats
(1 per Strength and Agility), poisons from the spellbook (Instant Poison main hand, Deadly Poison off hand).

Playstyle `combat-swords-raid` (the scorer's model id, used for leveling): open from stealth behind the mob with Cheap Shot
(Garrote before 26), Slice and Dice at 1-2 points when it is down, Sinister Strike to 5 points, Eviscerate (or Kidney
Shot when hurt), Riposte after a parry, Blade Flurry and Adrenaline Rush on the pull when ready, Cold Blood right before a
5-point Eviscerate, Evasion when low. Between fights: a bandage below 60% health (First Aid, 60 s cooldown), food below 65%
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

TALENT_SPELLS = {"Riposte": "Riposte", "Blade Flurry": "Blade Flurry", "Adrenaline Rush": "Adrenaline Rush", "Cold Blood": "Cold Blood", "Mutilate": "Mutilate",
                 "Ghostly Strike": "Ghostly Strike", "Hemorrhage": "Hemorrhage", "Premeditation": "Premeditation", "Preparation": "Preparation", "Venom": "Venom"}
# the abilities a talent names in its 70291 tooltip
COLD_BLOOD_SPELLS = ("Sinister Strike", "Backstab", "Ambush", "Eviscerate", "Mutilate")             # "your next ... by 100%": the first one spends it
REMORSELESS_SPELLS = ("Sinister Strike", "Backstab", "Ambush", "Mutilate", "Ghostly Strike")        # "your next ...": the first one spends it
OPPORTUNITY_SPELLS = ("Backstab", "Garrote", "Ambush", "Mutilate")                                    # Garrote's bleed through periodic_multiplier


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
                    s.combo = -1
                if name in ("Kidney Shot", "Slice and Dice", "Expose Armor"):
                    s.combo = -1
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
    "Murder": "+2%/rank damage vs Humanoids and Giants (half the mobs assumed: +1%/rank)",
    "Improved Slice and Dice": "+15%/rank Slice and Dice duration",
    "Relentless Strikes": "20% per combo point: a finisher restores 25 energy",
    "Improved Expose Armor": "not used",
    "Lethality": "+4%/rank crit damage bonus on Sinister Strike, Gouge, Backstab, Mutilate, Ghostly Strike, Hemorrhage",
    "Vile Poisons": "+4%/rank poison damage",
    "Cold Blood": "a guaranteed crit every 3 min: cast right before a 5-point Eviscerate, spent by the next Sinister Strike, Backstab, Ambush, Eviscerate or Mutilate",
    "Improved Poisons": "+2%/rank poison application chance",
    "Vigor": "+5 max energy/rank",
    "Seal Fate": "20%/rank: a crit from a combo-point ability adds a point",
    "Improved Kidney Shot": "+5%/rank damage to a Kidney-Shot-stunned mob",
    "Improved Eviscerate": "+6.7%/rank Eviscerate",
    "Improved Sinister Strike": "-2.5 energy/rank Sinister Strike",
    "Lightning Reflexes": "+1%/rank dodge",
    "Puncturing Wounds": "daggers (Backstab)",
    "Deflection": "+2%/rank parry",
    "Precision": "+1%/rank hit",
    "Endurance": "-30%/rank Sprint and Evasion cooldowns",
    "Riposte": "unlocks Riposte: 150% weapon damage and a 6 s disarm after a parry",
    "Improved Sprint": "travel only",
    "Improved Kick": "Kick on a casting mob: 50%/rank chance of 2 s more lockout (caster mobs: tables.MOB_CASTER_SHARE)",
    "Flawless Execution": "-10 energy Eviscerate",
    "Dual Wield Specialization": "+5%/rank off-hand damage",
    "Blade Flurry": "+20% attack speed for 15 s every 2 min",
    "Hack and Slash": "swords: 1%/rank chance per landed melee attack of an extra attack; daggers: +1%/rank crit with melee attacks (no maces in the lab)",
    "Weapon Expertise": "-1%/rank chance to be dodged or parried",
    "Aggression": "+2%/rank Sinister Strike, Backstab, Eviscerate",
    "Adrenaline Rush": "double energy regen for 15 s every 5 min",
    "Camouflage": "-2s/rank Stealth cooldown, stealth speed",
    "Master of Deception": "stealth only",
    "Opportunity": "+5%/rank Backstab, Garrote (the opener's bleed), Ambush, Mutilate",
    "Setup": "33%/rank: a combo point after dodging the target's own swing (an add's dodged swing gives none)",
    "Elusiveness": "not used",
    "Dirty Tricks": "not used",
    "Improved Ambush": "+15%/rank crit on Ambush (only the Subtlety playstyle casts Ambush)",
    "Initiative": "33%/rank: an extra combo point on Cheap Shot / Garrote / Ambush",
    "Ghostly Strike": "not used",
    "Improved Distract": "not used",
    "Heightened Senses": "not used",
    "Premeditation": "not used",
    "Serrated Blades": "attacks ignore 3%/rank armor, +10%/rank Rupture",
    "Dirty Deeds": "-10 energy/rank Cheap Shot and Garrote",
    "Preparation": "not used",
    "Hemorrhage": "not used (swords use Sinister Strike)",
    "Quietus": "+2%/rank Sinister Strike below 35%",
    "Cutthroat": "daggers",
    "Thousand Cuts": "daggers / Hemorrhage",
}
# Talent effects as the Subtlety playstyle plays them (spec strings starting with "subtlety"; documentation: MECHANICS is what the calibration
# reads). Since 2026-10-09 Opportunity, Improved Ambush and Serrated Blades' armor share apply in every playstyle.
SUBTLETY_MECHANICS = {
    "Hemorrhage": "the builder: 100% weapon damage, 145% with a dagger main hand (the Rupture bonus is unused: no Rupture)",
    "Ghostly Strike": "on cooldown (20 s): 125% weapon damage, 180% with a dagger main hand, +15% dodge for 7 s",
    "Premeditation": "2 combo points as the pull starts (2 min cooldown, off the global cooldown during the approach)",
    "Preparation": "resets Evasion (and Premeditation, Ghostly Strike) when Evasion is wanted but on cooldown (10 min)",
    "Improved Ambush": "+15%/rank crit on Ambush",
    "Opportunity": "+5%/rank Backstab, Garrote, Ambush, Mutilate",
    "Initiative": "33%/rank: an extra combo point on Ambush, Cheap Shot, Garrote",
    "Serrated Blades": "attacks ignore 3%/rank of the mob's armor (Rupture bonus unused)",
    "Quietus": "+2%/rank Sinister Strike, Ghostly Strike, Hemorrhage below 35%",
}
FIT = {
    "Malice": "scale", "Ruthlessness": "scale", "Murder": "scale", "Improved Slice and Dice": "scale", "Relentless Strikes": "scale", "Lethality": "scale",
    "Improved Eviscerate": "scale", "Improved Sinister Strike": "scale", "Lightning Reflexes": "scale", "Deflection": "scale", "Precision": "scale",
    "Endurance": "scale", "Riposte": "scale", "Flawless Execution": "scale", "Dual Wield Specialization": "scale", "Blade Flurry": "scale",
    "Hack and Slash": "scale", "Weapon Expertise": "scale", "Aggression": "scale", "Adrenaline Rush": "scale", "Remorseless Attacks": "scale",
    "Vile Poisons": "scale", "Improved Poisons": "scale", "Vigor": "scale", "Seal Fate": "scale", "Cold Blood": "scale", "Improved Kidney Shot": "scale",
    "Improved Gouge": "scale", "Camouflage": "scale", "Setup": "scale", "Initiative": "scale", "Serrated Blades": "scale", "Dirty Deeds": "scale",
    "Quietus": "scale", "Improved Sprint": "scale", "Opportunity": "scale",
}
SHARE_SOURCE = {"Melee": "white_mh", "Melee (off-hand)": "white_oh", "Sinister Strike": "sinister", "Eviscerate": "eviscerate", "Instant Poison": "poisons",
                "Deadly Poison": "poisons", "Rupture": "rupture", "Cheap Shot": "sinister", "Garrote": "garrote", "Riposte": "riposte", "Kidney Shot": "eviscerate",
                "Gouge": "sinister", "Hack and Slash": "white_mh"}
NEW_SOURCES = {"garrote": {"id": "garrote", "share": 0.0, "min_level": 14, "tags": ["type:melee", "dot", "school:physical", "ability:Garrote", "opener", "weapon:sword"]},
               "riposte": {"id": "riposte", "share": 0.0, "min_level": 20, "tags": ["type:melee", "yellow", "school:physical", "ability:Riposte", "weapon:sword"], "cooldown": 6}}
KEY_TALENTS = ["Dual Wield Specialization", "Malice", "Improved Eviscerate"]
DESCRIPTION = ("Single-target leveling fights against normal mobs of your level with two swords (the daggers models: two daggers, still Sinister Strike: the mob faces you "
               "after the opener, so no Backstab): open from stealth behind the mob with Cheap Shot (Garrote before 26; the mob turns to face you after the opener, "
               "so it can parry from then on), Slice and Dice at 1-2 points when it is down, Sinister Strike to 5 points, Eviscerate (Kidney Shot instead when below "
               "60% health, stunning for the tooltip's seconds per point), Eviscerate at fewer points when it would kill the mob, Cold Blood right before a 5-point "
               "Eviscerate, Riposte after a parry, Blade Flurry and Adrenaline Rush on the pull, Evasion when low; white swings with both hands (19% extra miss on "
               "white dual-wield hits), Instant Poison on the main hand and Deadly Poison on the off hand. Between fights: 2 s loot, 6 s travel, a bandage below 60% "
               "health (First Aid, 60 s cooldown), food below 65%; a death costs 90 s. The tuned rules (rotations/rogue-<spec>.json) veto spells and move the "
               "thresholds on top of this list.")
NOT_MODELLED = ("runners, adds, the stealth approach time, Expose Armor, Rupture (Eviscerate is used), Garrote's attack power bonus (its tooltip gives no number), "
                "Gouge-and-bandage, Vanish, Sprint, weapon skill, maces (Hack and Slash's armor share), gear upgrades within a level bracket.")
# rebuild.py: which scorer model, hand draft and optimizer build the pipeline calibrates, races and reports for this class
PIPELINE = {"variants": [{'spec': 'combat-swords-raid', 'opt': 'opt-combat-swords-raid-leveling-aoe', 'tag': 'aoe', 'profile': 'leveling-aoe', 'lookahead': 16, 'sets': ['MOBS_PER_PULL=2'], 'levels': '30,40,50,60', 'calibrate_levels': '40,60', 'label': 'Two-mob pulls with Blade Flurry'}], "spec": "combat-swords-raid", "hand": "leveling-combat-swords", "opt": "opt-combat-swords-raid-leveling-st", "tag": "combat", "lookahead": 16,
            "levels": "20,30,40,50,60", "calibrate_levels": "30,60",
            "extra_reports": [{"spec": "combat-daggers-raid", "build": "opt-combat-daggers-raid-leveling-st", "compare": ["opt-combat-swords-raid-leveling-st"]}]}


class RogueModule(BaseModule):
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
            for sname, pct in (("Hemorrhage", 1.45 if dagger else 1.0), ("Ghostly Strike", 1.80 if dagger else 1.25)):
                if sname in self.spells:   # copies: BOOK's Spell objects are shared by every module instance
                    self.spells[sname] = dataclasses.replace(self.spells[sname], weapon_pct=pct)
                    self.spells[sname].text = self.book[sname].text
        else:
            self.mh_dagger = "dagger" in spec   # daggers builds carry two daggers (1.8 s); the priority list is the same (no Backstab from the front)
        self.weapon_kind = "dagger" if self.mh_dagger else "1h"   # the same kind in both hands; "1h" is a sword (Hack and Slash: an extra attack)
        self._fight = None
        self.opened = False
        self.armor_spell_used = "Instant Poison / Deadly Poison" if "Instant Poison" in self.spells else "none"

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
        return ranks[-1] if ranks else None

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
        if spell.name == "Sinister Strike":
            cost = max(0.0, cost - self.tv("Improved Sinister Strike", 0))
        if spell.name == "Eviscerate":
            cost = max(0.0, cost - self.tv("Flawless Execution", 0))   # "Reduces the Energy cost of your Eviscerate ability by 10."
        if spell.name in ("Cheap Shot", "Garrote"):
            cost = max(0.0, cost - self.tv("Dirty Deeds", 0))
        return cost

    def hit_bonus(self, spell):
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
        if self.weapon_kind == "dagger" and spell.kind == "melee" and spell.dot <= 0:   # Hack and Slash, Dagger/Fist: crit with weapon attacks
            c += self.tv("Hack and Slash", 1) / 100                                       # (not the poisons, not a bleed's ticks)
        return c

    def crit_damage_bonus(self, spell):
        if spell.name in ("Sinister Strike", "Gouge", "Backstab", "Mutilate", "Ghostly Strike", "Hemorrhage"):
            return self.tv("Lethality", 0) / 100
        return 0.0

    def damage_multiplier(self, spell, frozen):
        m = 1 + self.tv("Murder", 0) / 100 / 2
        f = self._fight
        if spell.hand == "oh":
            m *= 1 + self.tv("Dual Wield Specialization", 0) / 100
        if spell.name in ("Sinister Strike", "Backstab", "Eviscerate"):
            m *= 1 + self.tv("Aggression", 0) / 100
        if spell.name == "Eviscerate":
            m *= 1 + self.tv("Improved Eviscerate", 0) / 100
            cp = max(1, f.last_combo) if f else 5
            lo1, hi1 = spell.evis1
            lo5, hi5 = spell.evis
            avg = ((lo1 + hi1) / 2 + ((lo5 + hi5) / 2 - (lo1 + hi1) / 2) * (cp - 1) / 4) + 0.03 * cp * (f.p.attack_power if f else 0.0)
            m *= avg / ((lo5 + hi5) / 2)
        if spell.name == "Sinister Strike" and f and f.m.hp < 0.35 * f.m.hp_max:
            m *= 1 + self.tv("Quietus", 0) / 100
        if self.sub:
            if spell.name in ("Ghostly Strike", "Hemorrhage") and f and f.m.hp < 0.35 * f.m.hp_max:
                m *= 1 + self.tv("Quietus", 0) / 100
        if spell.name in OPPORTUNITY_SPELLS:   # every playstyle: the Combat lists open with Garrote too (its bleed goes through here)
            m *= 1 + self.tv("Opportunity", 0) / 100
        if spell.school == "nature":
            m *= 1 + self.tv("Vile Poisons", 0) / 100
        if spell.name == "Rupture":
            m *= 1 + self.tv("Serrated Blades", 1) / 100
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
        bf = self.spells.get("Blade Flurry")
        if bf is not None and p.ready("Blade Flurry", t) and p.energy >= bf.cost:
            p.energy -= bf.cost
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

    def on_swing(self, fight, spell, outcome, amount, hand):
        p, m, t = fight.p, fight.m, fight.t
        if spell.name in ("Cheap Shot", "Garrote", "Kidney Shot", "Ambush"):
            self.opened = True
        # one-use boosts: the first ability the tooltip names spends them, landed or not (its attack-table roll already had the crit)
        if spell.name in COLD_BLOOD_SPELLS:
            p.buffs.pop("Cold Blood", None)
        if spell.name in REMORSELESS_SPELLS:
            p.buffs.pop("Remorseless", None)
        if outcome == "parry" and "Riposte" in self.spells:
            p.buffs["Riposte"] = {"until": t + 5.0}
        if outcome in ("miss", "dodge", "parry"):
            return
        if spell.name == "Kidney Shot":   # "Lasts longer per combo point: 1 point : 2 seconds ... 5 points: 6 seconds"
            dur = getattr(spell, "stun_by_points", {}).get(max(1, min(5, fight.last_combo)), spell.stun)
            m.debuffs["Kidney Shot"] = {"until": t + dur, "stacks": 1}
            if dur > 0:
                m.stun_until = max(m.stun_until, t + dur)
                if m.casting(t):
                    m.cast_end = -1.0   # a stun breaks the mob's cast, as engine.apply_control does for a fixed stun
        # poisons: Instant Poison on main-hand hits, Deadly Poison on off-hand hits
        chance_bonus = self.tv("Improved Poisons", 0) / 100
        ip, dp = self.spells.get("Instant Poison"), self.spells.get("Deadly Poison")
        if hand == "mh" and ip is not None and fight.rng.random() < ip.poison_chance + chance_bonus:
            self.poison_hit(fight, ip)
        if hand == "oh" and dp is not None and fight.rng.random() < dp.poison_chance + chance_bonus:
            b = m.debuffs.get("Deadly Poison")
            stacks = min(5, (b["stacks"] if b and b["until"] > t else 0) + 1)
            m.debuffs["Deadly Poison"] = {"until": t + dp.dot_dur, "stacks": stacks}
            fight.refresh_dot("Deadly Poison", dp.dot * stacks * self.damage_multiplier(dp, False), dp.dot_ticks, dp.dot_dur / dp.dot_ticks, p.melee_crit, 2.0)
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
        amount = fight.rng.uniform(ip.dmg_min, ip.dmg_max) * self.damage_multiplier(ip, False)
        crit = fight.rng.random() < p.melee_crit
        if crit:
            amount *= 1.5
        fight.deal(Spell("Instant Poison", "nature"), amount, crit)
        fight.note(f"Instant Poison{' CRIT' if crit else ''} {amount:.0f} -> mob {max(0, m.hp):.0f}")

    def on_hit(self, fight, spell, amount, crit, frozen):
        p, m, t = fight.p, fight.m, fight.t
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
            cp = max(1, fight.last_combo)
            base, dur = spell.rupture4
            total = base * (0.6 + 0.1 * cp) + 0.02 * cp * p.attack_power * 4
            fight.refresh_dot("Rupture", total * self.damage_multiplier(spell, False), max(1, int((dur - 2 + 2 * cp) / 2)), 2.0, p.melee_crit, 2.0)
        if spell.combo < 0:   # "Your finishing moves ...": every finisher, Slice and Dice included
            if self.rank("Ruthlessness") and fight.rng.random() < self.tv("Ruthlessness", 0) / 100:
                p.combo = min(5, p.combo + 1)
            # "Your finishing moves have a 20% chance per Combo Point to restore 25 Energy."
            if self.rank("Relentless Strikes") and fight.rng.random() < self.tv("Relentless Strikes", 0) / 100 * max(1, fight.last_combo):
                p.energy = min(p.energy_max, p.energy + self.tv("Relentless Strikes", 1))
        # (Cold Blood and Remorseless Attacks are spent in on_swing)
        if self.sub:
            if spell.name == "Ghostly Strike":
                p.buffs["Ghostly Strike"] = {"until": t + 7.0}
            if spell.name == "Preparation":
                for n in ("Evasion", "Premeditation", "Ghostly Strike", "Vanish", "Sprint", "Cold Blood", "Kick", "Gouge", "Kidney Shot", "Riposte", "Blind"):
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
        p.buffs.pop("Evasion", None)
        p.buffs.pop("Slice and Dice", None)
        p.buffs.pop("Blade Flurry", None)
        p.buffs.pop("Adrenaline Rush", None)
        if self.sub:
            p.buffs.pop("Ghostly Strike", None)
        if p.hp < 0.60 * p.hp_max and p.cooldowns.get("Bandage", -1.0) <= t:
            p.hp = min(p.hp_max, p.hp + bandage_heal(p.level))
            p.cooldowns["Bandage"] = t + 60.0
            return 8.0
        return 0.0

    # ------------------------------------------------------------ priority list
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
        if evis and can(evis) and p.combo >= 1:
            lo1, hi1 = evis.evis1
            lo5, hi5 = evis.evis
            est = ((lo1 + hi1) / 2 + ((lo5 + hi5) / 2 - (lo1 + hi1) / 2) * (p.combo - 1) / 4 + 0.03 * p.combo * p.attack_power) * (1 + self.tv("Improved Eviscerate", 0) / 100) * (1 - 0.35)
            if hp <= est * 0.95:
                return evis
        if snd and can(snd) and p.combo >= 1 and not p.buff("Slice and Dice", t) and hp > 0.5 * m.hp_max and (p.combo <= 2 or hp > 0.8 * m.hp_max):
            return snd
        if p.combo >= 5:
            if ks and can(ks) and p.hp < 0.6 * p.hp_max and not m.stunned(t) and hp > 0.25 * m.hp_max:
                return ks
            if evis and can(evis):
                self.cold_blood(fight, can)
                return evis
        if ss and can(ss):
            return ss
        return None

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
            cyc_dmg += ((lo5 + hi5) / 2 + 0.15 * p.attack_power) * (1 + self.tv("Improved Eviscerate", 0) / 100) * (1 + crit) * armor
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
        """Subtlety leveling: Ambush opener (Premeditation's points already on the mob), Ghostly Strike on cooldown, Hemorrhage builder."""
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
        if evis and can(evis) and p.combo >= 1:
            lo1, hi1 = evis.evis1
            lo5, hi5 = evis.evis
            est = ((lo1 + hi1) / 2 + ((lo5 + hi5) / 2 - (lo1 + hi1) / 2) * (p.combo - 1) / 4 + 0.03 * p.combo * p.attack_power) * (1 + self.tv("Improved Eviscerate", 0) / 100) * (1 - 0.35)
            if hp <= est * 0.95:
                return evis
        if snd and can(snd) and p.combo >= 1 and not p.buff("Slice and Dice", t) and hp > 0.5 * m.hp_max and (p.combo <= 2 or hp > 0.8 * m.hp_max):
            return snd
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
