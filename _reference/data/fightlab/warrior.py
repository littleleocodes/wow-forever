"""Warrior module for the fight lab (two-handed Arms leveling).

Spell ranks are read from `_reference/data/forever-spells/warrior.json` (beta client build 1.60.1.70009); talent numbers from
each rank's tooltip in `_reference/data/forever-talents/warrior.json`. Weapon damage uses a quest-green two-hander by level
(`tables.weapon_dps`), attack power from the client's base stats and the class's 2 AP per Strength.

Playstyle `arms-2h-raid` (the scorer's model id, used for leveling): Bloodrage and Charge on the pull, Battle Shout kept up,
Victory Rush after a kill, Mortal Strike on cooldown, Overpower after a dodge (or a Bloodthrill proc), Rend once, Execute
under 20%, Heroic Strike with spare rage; Battle Stance throughout. Between fights: a bandage below 60% health (First Aid,
60 s cooldown), food below 50%.

Playstyle `prot-leveling` (any spec string starting with "prot"): sword and board in Defensive Stance, see `decide_prot` and
PROT_NOTES below. Every other spec string runs exactly as before (the shield code is behind `self.prot`).
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
SHOUT = re.compile(r"melee attack power of all party members[^.]*? by (\d+)")
SLOW = re.compile(r"slowing the enemy's movement by (\d+)% for (\d+) sec")
AP_PCT = re.compile(r"(\d+)% of (?:your )?Attack Power")

TALENT_SPELLS = {"Mortal Strike": "Mortal Strike", "Sweeping Strikes": "Sweeping Strikes", "Piercing Howl": "Piercing Howl", "Death Wish": "Death Wish",
                 "Bloodthirst": "Bloodthirst", "Concussion Blow": "Concussion Blow", "Last Stand": "Last Stand", "Shield Slam": "Shield Slam",
                 "Spearing Strike": "Spearing Strike"}
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
                elif fl:
                    s.dmg_min = s.dmg_max = _num(fl.group(1) or fl.group(2) or fl.group(3))
                if ap:
                    s.coef = float(ap.group(1)) / 100   # attack power coefficient (Bloodthirst, Victory Rush)
                if bl:
                    s.dot, s.dot_dur = _num(bl.group(1)), float(bl.group(2))
                    s.dot_ticks = max(1, int(round(s.dot_dur / 3.0)))
                if name == "Whirlwind":
                    s.weapon_pct = 1.0
                if ch:
                    s.kind, s.charge, s.charge_rage, s.stun, s.resource = "buff", True, float(ch.group(1)), float(ch.group(2)), "none"
                if sh:
                    s.kind, s.ap = "buff", _num(sh.group(1))
                if sl:
                    s.daze, s.chill_dur = float(sl.group(1)) / 100, float(sl.group(2))
                if name in ("Bloodrage", "Berserker Rage", "Battle Stance", "Berserker Stance", "Defensive Stance", "Retaliation", "Recklessness",
                            "Death Wish", "Last Stand", "Shield Wall", "Shield Block", "Sweeping Strikes", "Demoralizing Shout", "Intimidating Shout",
                            "Challenging Shout", "Taunt", "Piercing Howl"):
                    s.kind = "buff"
                    if name in ("Bloodrage", "Berserker Rage", "Retaliation", "Recklessness", "Last Stand", "Shield Wall"):
                        s.resource = "none"
                if name == "Victory Rush":
                    s.resource = "none"
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
    "Improved Heroic Strike": "-1 rage/rank Heroic Strike",
    "Deflection": "+1%/rank parry",
    "Improved Rend": "+11.7%/rank Rend bleed",
    "Improved Charge": "+3 rage/rank on Charge",
    "Improved Tactical Mastery": "no stance changes here",
    "Improved Overpower": "+25%/rank Overpower crit",
    "Anger Management": "+1 rage per 3 s in combat",
    "Deep Wounds": "crits bleed 20%/rank of average weapon damage over 12 s",
    "Spearing Strike": "40% weapon damage instant: not used (Beasts/Humanoids)",
    "Two-Handed Weapon Specialization": "+1%/rank two-hander damage",
    "Impale": "+10%/rank ability crit damage bonus",
    "Bloodthrill": "4%/rank per main-hand hit on a Rended mob: Overpower usable for 6 s",
    "Sweeping Strikes": "AoE only",
    "Weaponmaster": "axe/polearm: +1%/rank crit (assumed weapon type)",
    "Improved Slam": "not used (Slam is a 1.5 s cast on an 18 s cooldown: Mortal Strike and Heroic Strike fill the rage)",
    "Improved Hamstring": "not used",
    "Mortal Strike": "unlocks Mortal Strike (30 rage, weapon plus 85..160, 6 s cooldown)",
    "Booming Voice": "range only",
    "Cruelty": "+1%/rank melee crit",
    "Iron Will": "PvP",
    "Unbridled Wrath": "12%/rank per weapon hit: +2 rage with a two-hander",
    "Improved Cleave": "AoE only",
    "Piercing Howl": "not used (the mob stands and fights)",
    "Blood Craze": "1%/rank health over 6 s after being crit, dropping 20% in one hit, or dealing damage with Bloodthirst",
    "Boundless Rage": "+10 max rage/rank",
    "Dual Wield Specialization": "two-hander build",
    "Raging Blows": "two-hander build",
    "Enrage": "30% chance after any hit taken: +2%/rank physical damage for 12 s",
    "Improved Execute": "-2.5 rage/rank Execute",
    "Precision": "+1%/rank hit",
    "Death Wish": "+20% damage 30 s every 3 min (on the pull)",
    "Improved Intercept": "Berserker Stance only",
    "Improved Berserker Rage": "Berserker Rage gives 10 rage (used on cooldown)",
    "Flurry": "crits: +5%/rank attack speed for the next 3 swings",
    "Bloodthirst": "unlocks Bloodthirst (30 rage, 35% AP plus 30..48, 6 s cooldown)",
    "Shield Specialization": "no shield",
    "Anticipation": "+20 Defense: ~-1.6% chance to be hit (assumed)",
    "Improved Bloodrage": "+50% Bloodrage rage",
    "Toughness": "+2%/rank armor",
    "Improved Thunder Clap": "not used",
    "Last Stand": "+30% health for 20 s every 3 min when low",
    "Master of Defense": "no shield",
    "Improved Revenge": "no shield (Revenge follows a block, dodge or parry: not used in Battle Stance)",
    "Defiance": "threat only",
    "Improved Sunder Armor": "not used",
    "Improved Disarm": "not used",
    "Vanguard": "not used",
    "Improved Shield Wall": "not used",
    "Concussion Blow": "5 s stun every 45 s (when the mob is on you)",
    "Improved Shield Bash": "no shield",
    "Bastion": "no shield",
    "Focused Rage": "-3 rage on offensive abilities",
    "Shield Slam": "no shield",
}
FIT = {
    "Improved Rend": "scale", "Improved Heroic Strike": "scale", "Deflection": "scale", "Improved Charge": "scale", "Improved Overpower": "scale",
    "Anger Management": "scale", "Deep Wounds": "scale", "Two-Handed Weapon Specialization": "scale", "Impale": "scale", "Bloodthrill": "scale",
    "Weaponmaster": "scale", "Improved Slam": "scale",
    "Mortal Strike": ("replace", [{"channel": "dmg", "scope": ["type:melee"], "values": [0.12]}]),
    "Cruelty": "scale", "Unbridled Wrath": "scale", "Blood Craze": "scale", "Boundless Rage": "scale", "Enrage": "scale", "Improved Execute": "scale",
    "Precision": "scale", "Flurry": "scale", "Death Wish": "scale", "Improved Berserker Rage": "scale", "Toughness": "scale", "Improved Bloodrage": "scale",
    "Last Stand": "scale", "Concussion Blow": "scale", "Focused Rage": "scale", "Anticipation": "scale", "Iron Will": "scale", "Piercing Howl": "scale",
    "Spearing Strike": "scale", "Sweeping Strikes": "scale", "Improved Hamstring": "scale",
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

DESCRIPTION = ("Single-target leveling fights against normal mobs of your level with a two-hander in Battle Stance: Bloodrage and Charge on the pull (the mob is stunned 1 s), "
               "Battle Shout kept up, Victory Rush after a kill, Mortal Strike on cooldown, Overpower after a dodge or a Bloodthrill proc, Rend once, Execute under 20% "
               "with all the rage, Heroic Strike with spare rage, white swings that generate rage by Forever's normalized rule (weapon speed, double on a crit; tables.RAGE_MODEL) (the mob dodges 5%, parries 5%, 10% of swings "
               "glance for 95%). Between fights: 2 s loot, 6 s travel, a bandage below 60% health (First Aid, 60 s cooldown), food below 50%, rage decays; a death costs 90 s.")
NOT_MODELLED = "runners, adds, stance dancing (Whirlwind / Intercept in Berserker Stance), Sweeping Strikes, Hamstring kiting, Retaliation, weapon skill, gear upgrades within a level bracket."
# rebuild.py: which scorer model, hand draft and optimizer build the pipeline calibrates, races and reports for this class
PIPELINE = {"variants": [{'spec': 'arms-2h-raid', 'opt': 'opt-arms-2h-raid-leveling-aoe', 'tag': 'aoe', 'profile': 'leveling-aoe', 'lookahead': 16, 'sets': ['MOBS_PER_PULL=3'], 'levels': '30,40,50,60', 'calibrate_levels': '40,60', 'label': 'AoE grinding, 3 mobs per pull'}], "spec": "arms-2h-raid", "hand": "leveling-arms", "opt": "opt-arms-2h-raid-leveling-st", "tag": "arms", "lookahead": 20,
            "levels": "20,30,40,50,60", "calibrate_levels": "30,60",
            "extra_reports": [{"spec": "fury-dw-raid", "build": "opt-fury-dw-raid-leveling-st", "compare": ["opt-arms-2h-raid-leveling-st"]}]}


class WarriorModule(BaseModule):
    resource = "rage"
    melee = True
    eat_below = 0.65   # 0.50 made a level-60 warrior die twice as often for the same time per kill (sim, 2026-09-26)

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
        self.armor_spell_used = "Battle Stance"
        self.prot = spec.startswith("prot")
        if self.prot:   # sword and board: Defensive Stance; Whirlwind (Berserker Stance) is out of the area priority
            self.armor_spell_used = "Defensive Stance"
            self.AOE = {'direct': ['Thunder Clap', 'Cleave'], 'min_near': 2}
            self.stance = "Defensive Stance"

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
        base = class_base_stats("warrior", level)
        g = gear_stats(level, self.gear, "warrior")
        strength = base["strength"] + g["strength"]
        agility = base["agility"] + g["agility"]
        stamina = base["stamina"] + g["stamina"]
        spirit = base["spirit"] + g["spirit"]
        if self.prot:   # Toughness counts the shield's armor too (armor from items)
            sh = SHIELD_GEAR.get(tables.GEAR_TIER if self.gear == "leveling" else self.gear, SHIELD_GEAR["greens"])
            sh_armor = interp([(L, a) for L, a, _ in sh], level) * (1 + (tables.GEAR_STAT_MULT - 1) / 2)
            sh_ilvl = interp([(L, i) for L, _, i in sh], level)
            armor = (g["armor"] + sh_armor) * (1 + self.tv("Toughness", 0) / 100)
        else:
            armor = g["armor"] * (1 + self.tv("Toughness", 0) / 100)
        p = Player(level=level, hp_max=class_base_health("warrior", level) + 10 * stamina, hp=0.0, mana_max=0.0, mana=0.0, base_mana=0.0,
                   spirit=spirit, intellect=base["intellect"], spell_power=0.0, armor=armor, spell_crit=0.0,
                   dodge=class_dodge("warrior", level, agility), ranged_crit=0.0)
        p.strength, p.agility, p.stamina = strength, agility, stamina
        p.attack_power = class_attack_power("warrior", level, strength, agility)
        self.base_ap = p.attack_power
        p.melee_crit = class_melee_crit("warrior", level, agility) + self.tv("Cruelty", 0) / 100 + (self.tv("Weaponmaster", 0) / 100 if self.rank("Weaponmaster") else 0.0)
        p.hit_bonus = self.tv("Precision", 0) / 100
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
        p.rage_max = 100.0 + self.tv("Boundless Rage", 0)
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
        if self.prot:
            if spell.name == "Thunder Clap":
                cost = max(0.0, cost - self.tv("Improved Thunder Clap", 0))
            if spell.name == "Sunder Armor":
                cost = max(0.0, cost - self.tv("Improved Sunder Armor", 0))
        if spell.resource == "rage" and cost > 0 and spell.kind == "melee":
            cost = max(0.0, cost - self.tv("Focused Rage", 0))
        return cost

    def final_cost(self, fight, spell, cost):
        if spell.name == "Execute":   # spends everything: the extra rage becomes damage
            self.execute_extra = max(0.0, fight.p.rage - cost)
            return fight.p.rage
        return cost

    def crit_bonus(self, spell, frozen):
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
        else:
            m = 1 + self.tv("Two-Handed Weapon Specialization", 0) / 100
        f = self._fight
        if f and f.p.buff("Enrage", f.t):
            m *= 1 + self.tv("Enrage", 1) / 100   # +2%/rank (70009); was a flat +10% at every rank
        if f and f.p.buff("Death Wish", f.t):
            m *= 1.20
        if spell.name == "Rend":
            m *= 1 + self.tv("Improved Rend", 0) / 100
        if spell.name == "Execute" and spell.dmg_max > 0:
            m *= (spell.dmg_max + getattr(spell, "rage_dmg", 0.0) * self.execute_extra) / spell.dmg_max
        return m

    def periodic_can_crit(self, spell):
        return True

    def split_damage_taken(self, fight, dmg):
        if self.prot and self.stance == "Defensive Stance":
            return dmg * 0.90   # Defensive Stance: "Decreases damage taken by 10%" (melee and spells)
        return dmg

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
            gain = 10.0 * (1 + self.tv("Improved Bloodrage", 0) / 100)
            p.hp -= 0.06 * p.hp_max
            p.rage = min(p.rage_max, p.rage + gain)
            p.buffs["Bloodrage"] = {"until": t + 10.0, "left": gain}
            p.cooldowns["Bloodrage"] = t + br.cooldown
            fight.casts["Bloodrage"] = fight.casts.get("Bloodrage", 0) + 1
        dw = self.spells.get("Death Wish")
        if dw is not None and p.ready("Death Wish", t) and p.rage >= 10:
            p.rage -= 10
            p.buffs["Death Wish"] = {"until": t + 30.0}
            p.cooldowns["Death Wish"] = t + dw.cooldown

    def on_hit(self, fight, spell, amount, crit, frozen):
        p, m, t = fight.p, fight.m, fight.t
        if spell.name == "Bloodthirst" and amount > 0 and self.rank("Blood Craze"):   # 70009: Bloodthirst damage triggers Blood Craze too
            p.hots = [h for h in p.hots if h[0] != "Blood Craze"]
            p.hots.append(["Blood Craze", p.hp_max * self.tv("Blood Craze", 0) / 100 / 3, 3, t + 2.0, 2.0, "player"])
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
            if spell.name == "Thunder Clap":   # the engine's attack slow is a flat 25% longer swing time (tooltip: 20%)
                mt = TC_TXT.search(spell.text or "")
                for x in near[:4]:
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
        if outcome == "dodge":
            p.buffs["Overpower"] = {"until": t + 5.0}
        if outcome in ("miss", "dodge", "parry"):
            return
        weapon_hit = spell.name == "Melee" or spell.weapon_pct > 0
        if weapon_hit and self.rank("Unbridled Wrath") and fight.rng.random() < self.tv("Unbridled Wrath", 0) / 100:
            p.rage = min(p.rage_max, p.rage + (1.0 if self.prot else 2.0))   # "increased to 2 Rage for two-handed weapons"
        if spell.name == "Melee" and self.rank("Bloodthrill") and fight.dot_active("Rend") and fight.rng.random() < self.tv("Bloodthrill", 0) / 100:
            p.buffs["Overpower"] = {"until": t + 6.0}
        if outcome == "crit":
            if self.rank("Deep Wounds"):
                avg = (p.mh.dmg_min + p.mh.dmg_max) / 2 + p.attack_power / 14.0 * p.mh.speed
                fight.refresh_dot("Deep Wounds", avg * self.tv("Deep Wounds", 0) / 100, 4, 3.0)
            if self.rank("Flurry"):
                self.flurry_swings = 3
        elif spell.name == "Melee" and self.flurry_swings > 0:
            self.flurry_swings -= 1

    def on_hit_taken(self, fight, dmg, crit=False):
        p, t = fight.p, fight.t
        if self.rank("Enrage") and fight.rng.random() < self.tv("Enrage", 0) / 100:
            p.buffs["Enrage"] = {"until": t + 12.0}
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
        if spell.name == "Overpower":
            p.buffs.pop("Overpower", None)

    def on_kill(self, fight):
        p, t = fight.p, fight.t
        if "Victory Rush" in self.spells:
            p.buffs["Victory Rush"] = {"until": t + 20.0}

    def after_fight(self, p, t):
        """Bandage below 60% health (First Aid by level, 8 s, 60 s cooldown); Bloodrage's trickle is dropped between fights."""
        p.buffs.pop("Bloodrage", None)
        p.buffs.pop("Enrage", None)
        if self.prot:
            p.buffs.pop("Revenge", None)
            p.buffs.pop("Shield Block", None)
        if p.hp < 0.60 * p.hp_max and p.cooldowns.get("Bandage", -1.0) <= t:
            p.hp = min(p.hp_max, p.hp + bandage_heal(p.level))
            p.cooldowns["Bandage"] = t + 60.0
            return 8.0
        return 0.0

    # ------------------------------------------------------------ priority list
    def decide(self, fight):
        if self.prot:
            return self.decide_prot(fight)
        if fight.others():   # a pull of several mobs: the area priority first (engine.BaseModule.decide_aoe, AOE below)
            r = self.decide_aoe(fight)
            if r is not None:
                return r
        p, m, t = fight.p, fight.m, fight.t
        sp = self.spells
        in_melee = m.in_melee and m.dist <= MELEE_RANGE + 0.5

        def can(s):
            return s is not None and p.ready(s.name, t) and fight.can_afford(s, self.mana_cost(s))

        charge, shout, vr, execute, over, ms, rend, hs, bt, cb, brage = (sp.get(n) for n in ("Charge", "Battle Shout", "Victory Rush", "Execute", "Overpower", "Mortal Strike", "Rend", "Heroic Strike", "Bloodthirst", "Concussion Blow", "Berserker Rage"))
        hp = m.hp
        # Bloodrage's trickle: 1 rage per second for 10 s
        br = p.buffs.get("Bloodrage")
        if br and br["until"] > t and br.get("left", 0) > 0 and not hasattr(fight, "_br_tick"):
            fight._br_tick = t
        if br and br["until"] > t and br.get("left", 0) > 0 and t - fight._br_tick >= 1.0:
            fight._br_tick = t
            br["left"] -= 1
            p.rage = min(p.rage_max, p.rage + 1.0)
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

        def can(s):
            return s is not None and p.ready(s.name, t) and fight.can_afford(s, self.mana_cost(s))

        # Bloodrage's trickle: 1 rage per second for 10 s (as in the Arms priority)
        br = p.buffs.get("Bloodrage")
        if br and br["until"] > t and br.get("left", 0) > 0 and not hasattr(fight, "_br_tick"):
            fight._br_tick = t
        if br and br["until"] > t and br.get("left", 0) > 0 and t - fight._br_tick >= 1.0:
            fight._br_tick = t
            br["left"] -= 1
            p.rage = min(p.rage_max, p.rage + 1.0)
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
