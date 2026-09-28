"""Rogue module for the fight lab (Combat swords leveling).

Spell ranks are read from `_reference/data/forever-spells/rogue.json` (beta client build 1.60.1.70009); talent numbers from
each rank's tooltip in `_reference/data/forever-talents/rogue.json`. Weapons: a quest-green sword in each hand by level
(`tables.weapon_dps`, 2.6 speed), attack power from the client's base stats (1 per Strength and Agility), poisons from the
spellbook (Instant Poison main hand, Deadly Poison off hand).

Playstyle `combat-swords-raid` (the scorer's model id, used for leveling): open from stealth behind the mob with Cheap Shot
(Garrote before 26), Slice and Dice at 1-2 points when it is down, Sinister Strike to 5 points, Eviscerate (or Kidney
Shot when hurt), Riposte after a parry, Blade Flurry and Adrenaline Rush on the pull when ready, Evasion when low, Gouge
to bandage in an emergency. Between fights: a bandage below 60% health (First Aid, 60 s cooldown), food below 50%.
"""
import json
import pathlib
import re

from engine import parse_interrupt, BaseModule, Player, Spell, Weapon
from tables import (GCD, MELEE_RANGE, WEAPON_SPEED, bandage_heal, class_attack_power, class_base_health, class_base_stats, class_dodge,
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

TALENT_SPELLS = {"Riposte": "Riposte", "Blade Flurry": "Blade Flurry", "Adrenaline Rush": "Adrenaline Rush", "Cold Blood": "Cold Blood", "Mutilate": "Mutilate",
                 "Ghostly Strike": "Ghostly Strike", "Hemorrhage": "Hemorrhage", "Premeditation": "Premeditation", "Preparation": "Preparation", "Venom": "Venom"}


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
    "Remorseless Attacks": "+20%/rank crit on the first Sinister Strike after a kill",
    "Malice": "+1%/rank crit",
    "Ruthlessness": "20%/rank chance for a combo point after a finisher",
    "Murder": "+2%/rank damage vs Humanoids and Giants (half the mobs assumed: +1%/rank)",
    "Improved Slice and Dice": "+15%/rank Slice and Dice duration",
    "Relentless Strikes": "20% per combo point: a finisher restores 25 energy",
    "Improved Expose Armor": "not used",
    "Lethality": "+4%/rank crit damage bonus on Sinister Strike, Gouge, Backstab, Mutilate, Ghostly Strike, Hemorrhage",
    "Vile Poisons": "+4%/rank poison damage",
    "Cold Blood": "a guaranteed crit every 3 min (on Eviscerate)",
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
    "Hack and Slash": "swords: 1%/rank chance per hit of an extra attack",
    "Weapon Expertise": "-1%/rank chance to be dodged or parried",
    "Aggression": "+2%/rank Sinister Strike, Backstab, Eviscerate",
    "Adrenaline Rush": "double energy regen for 15 s every 5 min",
    "Camouflage": "-2s/rank Stealth cooldown, stealth speed",
    "Master of Deception": "stealth only",
    "Opportunity": "daggers / openers (+5%/rank Garrote, Ambush)",
    "Setup": "33%/rank: a combo point after a dodge",
    "Elusiveness": "not used",
    "Dirty Tricks": "not used",
    "Improved Ambush": "daggers",
    "Initiative": "33%/rank: an extra combo point on Cheap Shot / Garrote",
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
DESCRIPTION = ("Single-target leveling fights against normal mobs of your level with two swords: open from stealth behind the mob with Cheap Shot (Garrote before 26; the "
               "mob turns to face you after the opener, so it can parry from then on), Slice and Dice at 1-2 points when it is down, Sinister Strike to 5 points, "
               "Eviscerate (Kidney Shot instead when below 50% health), Riposte after a parry, Blade Flurry and Adrenaline Rush on the pull, Evasion when low; white "
               "swings with both hands (19% extra miss on white dual-wield hits), Instant Poison on the main hand and Deadly Poison on the off hand. Between fights: "
               "2 s loot, 6 s travel, a bandage below 60% health (First Aid, 60 s cooldown), food below 50%; a death costs 90 s.")
NOT_MODELLED = "runners, adds, the stealth approach time, Expose Armor, Rupture (Eviscerate is used), Gouge-and-bandage, Vanish, Sprint, weapon skill, gear upgrades within a level bracket."
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
        self.gear = gear
        self.book = {name: self.rank_at(name) for name in BOOK}
        self.spells = {n: s for n, s in self.book.items() if s is not None}
        for tname, sname in TALENT_SPELLS.items():
            if not self.t.get(tname):
                self.spells.pop(sname, None)
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
        kind = "dagger" if "dagger" in self.spec else "1h"   # daggers builds carry two daggers (1.8 s); the priority list is the same (no Backstab from the front)
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
        if spell.name == "Eviscerate" and self.rank("Flawless Execution"):
            cost = max(0.0, cost - 10.0)
        if spell.name in ("Cheap Shot", "Garrote"):
            cost = max(0.0, cost - self.tv("Dirty Deeds", 0))
        return cost

    def hit_bonus(self, spell):
        return 0.0

    def crit_bonus(self, spell, frozen):
        c = 0.0
        f = self._fight
        if f and spell.name in ("Sinister Strike", "Eviscerate") and f.p.buff("Cold Blood", f.t):
            c += 1.0
        if f and spell.name == "Sinister Strike" and f.p.buff("Remorseless", f.t):
            c += self.tv("Remorseless Attacks", 0) / 100
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
            factor /= 1.2
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
            p.buffs["Blade Flurry"] = {"until": t + 15.0}
            p.cooldowns["Blade Flurry"] = t + bf.cooldown
        ar = self.spells.get("Adrenaline Rush")
        if ar is not None and p.ready("Adrenaline Rush", t):
            p.buffs["Adrenaline Rush"] = {"until": t + 15.0}
            p.cooldowns["Adrenaline Rush"] = t + ar.cooldown
        cb = self.spells.get("Cold Blood")
        if cb is not None and p.ready("Cold Blood", t):
            p.buffs["Cold Blood"] = {"until": t + 60.0}
            p.cooldowns["Cold Blood"] = t + cb.cooldown

    def on_regen_tick(self, fight, p, t):
        if p.buff("Adrenaline Rush", t):
            p.energy = min(p.energy_max, p.energy + 20.0)   # a second energy tick

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
        if spell.name in ("Cheap Shot", "Garrote", "Kidney Shot"):
            self.opened = True
        if outcome == "parry" and "Riposte" in self.spells:
            p.buffs["Riposte"] = {"until": t + 5.0}
        if outcome in ("miss", "dodge", "parry"):
            return
        if spell.name == "Kidney Shot":
            m.debuffs["Kidney Shot"] = {"until": t + spell.stun, "stacks": 1}
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
        # extra attacks (Hack and Slash), combo points from crits (Seal Fate)
        if spell.name in ("Melee", "Melee (off-hand)") and self.rank("Hack and Slash") and fight.rng.random() < self.tv("Hack and Slash", 0) / 100 and not getattr(fight, "_extra", False):
            fight._extra = True
            fight.resolve_attack(Spell("Hack and Slash", "physical", kind="melee", resource="none"), white=True, hand="mh")
            fight._extra = False
        if outcome == "crit" and spell.combo > 0 and self.rank("Seal Fate") and fight.rng.random() < self.tv("Seal Fate", 0) / 100:
            p.combo = min(5, p.combo + 1)
        if spell.name in ("Cheap Shot", "Garrote") and self.rank("Initiative") and fight.rng.random() < self.tv("Initiative", 0) / 100:
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
        if spell.combo < 0 and spell.name != "Slice and Dice":
            if self.rank("Ruthlessness") and fight.rng.random() < self.tv("Ruthlessness", 0) / 100:
                p.combo = min(5, p.combo + 1)
            if self.rank("Relentless Strikes") and fight.rng.random() < 0.2 * max(1, fight.last_combo):
                p.energy = min(p.energy_max, p.energy + 25.0)
        if spell.name == "Eviscerate" and p.buff("Cold Blood", t):
            p.buffs.pop("Cold Blood", None)
        if spell.name == "Sinister Strike":
            p.buffs.pop("Remorseless", None)

    def on_dodge(self, fight):
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
                return evis
        if ss and can(ss):
            return ss
        return None
