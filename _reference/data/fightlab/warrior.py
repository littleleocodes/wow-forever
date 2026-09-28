"""Warrior module for the fight lab (two-handed Arms leveling).

Spell ranks are read from `_reference/data/forever-spells/warrior.json` (beta client build 1.60.1.70009); talent numbers from
each rank's tooltip in `_reference/data/forever-talents/warrior.json`. Weapon damage uses a quest-green two-hander by level
(`tables.weapon_dps`), attack power from the client's base stats and the class's 2 AP per Strength.

Playstyle `arms-2h-raid` (the scorer's model id, used for leveling): Bloodrage and Charge on the pull, Battle Shout kept up,
Victory Rush after a kill, Mortal Strike on cooldown, Overpower after a dodge (or a Bloodthrill proc), Rend once, Execute
under 20%, Heroic Strike with spare rage; Battle Stance throughout. Between fights: a bandage below 60% health (First Aid,
60 s cooldown), food below 50%.
"""
import json
import pathlib
import re

from engine import parse_interrupt, BaseModule, Player, Spell, Weapon
from tables import (GCD, MELEE_RANGE, WEAPON_SPEED, bandage_heal, class_attack_power, class_base_health, class_base_stats, class_dodge,
                    class_health_regen_tick, class_melee_crit, gear_stats, weapon_dps)

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
DESCRIPTION = ("Single-target leveling fights against normal mobs of your level with a two-hander in Battle Stance: Bloodrage and Charge on the pull (the mob is stunned 1 s), "
               "Battle Shout kept up, Victory Rush after a kill, Mortal Strike on cooldown, Overpower after a dodge or a Bloodthrill proc, Rend once, Execute under 20% "
               "with all the rage, Heroic Strike with spare rage, white swings that generate rage by Classic's formula (the mob dodges 5%, parries 5%, 10% of swings "
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
        if self.spec.startswith("fury"):   # Fury: two one-handers (the dual-wield miss penalty and off-hand halving are the engine's)
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

    def on_swing(self, fight, spell, outcome, amount, hand):
        p, m, t = fight.p, fight.m, fight.t
        if outcome == "dodge":
            p.buffs["Overpower"] = {"until": t + 5.0}
        if outcome in ("miss", "dodge", "parry"):
            return
        weapon_hit = spell.name == "Melee" or spell.weapon_pct > 0
        if weapon_hit and self.rank("Unbridled Wrath") and fight.rng.random() < self.tv("Unbridled Wrath", 0) / 100:
            p.rage = min(p.rage_max, p.rage + 2.0)
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
