"""Shaman module for the fight lab (Enhancement leveling with a slow two-hander).

Spell ranks are read from `_reference/data/forever-spells/shaman.json` (beta client build 1.60.1.70009); talent numbers from
each rank's tooltip in `_reference/data/forever-talents/shaman.json`. Weapon damage uses a quest-green two-hander by level,
attack power from the client's base stats (2 AP per Strength) plus the weapon imbue (Rockbiter's attack power, or Windfury's
extra attacks from 30).

Playstyle `enhancement-dps` (the scorer's model id, used for leveling): Lightning Shield (Water Shield when talented and low on
mana) and the weapon imbue kept up, Searing Totem dropped at the pull, a Lightning Bolt while the mob walks in, then Stormstrike,
Earth Shock (buffed by Stormstrike), Flame Shock while mana allows and instant Maelstrom Lightning Bolts between white swings;
Stoneclaw Totem and a Lesser Healing Wave when low, Nature's Swiftness + Healing Wave in an emergency; Reincarnation makes a
death cheap once an hour. Between fights: heals back to 80% health, water below 35% mana.
"""
import json
import pathlib
import re

from engine import parse_interrupt, BaseModule, Player, Spell, Weapon
from tables import (DEATH_TIME, GCD, MELEE_RANGE, WEAPON_SPEED, class_attack_power, class_base_health, class_base_mana, class_base_stats, class_dodge,
                    class_health_regen_tick, class_mana_regen_tick, class_melee_crit, class_spell_crit, gear_stats, weapon_dps)

ROOT = pathlib.Path(__file__).resolve().parents[3]
SPELLBOOK = json.load(open(ROOT / "_reference/data/forever-spells/shaman.json", encoding="utf-8"))
TREE = json.load(open(ROOT / "_reference/data/forever-talents/shaman.json", encoding="utf-8"))

NUM = re.compile(r"(\d+(?:\.\d+)?)")
DMG = re.compile(r"(?:for|causing|dealing) (\d[\d,]*) to (\d[\d,]*) (\w+) damage")
FLAME = re.compile(r"causing (\d[\d,]*) Fire damage immediately and (\d[\d,]*) Fire damage over (\d+) sec")
HEAL = re.compile(r"Heals (?:a|the) friendly target for (\d[\d,]*) to (\d[\d,]*)")
ROCK = re.compile(r"increasing melee attack power by (\d+)")
WIND = re.compile(r"(\d+)% chance of granting you (\d) extra attacks with (\d+) extra melee attack power")
FLAME_W = re.compile(r"Each hit causes (\d+) to (\d+) additional Fire damage")
SHIELD = re.compile(r"struck for (\d+) Nature damage")
SEARING = re.compile(r"for (\d+) sec that repeatedly attacks an enemy within (\d+) yards for (\d+) to (\d+) Fire damage")
CLAW = re.compile(r"Stoneclaw Totem with (\d+) health at the feet of the caster for (\d+) sec")
SLOW = re.compile(r"slowing movement speed by (\d+)%\. Lasts (\d+) sec")
COEF = re.compile(r"([\d.]+)% of spell power \((\w+(?: \w+)?)\)")

TALENT_SPELLS = {"Stormstrike": "Stormstrike", "Rage of the Farseer": "Rage of the Farseer", "Water Shield": "Water Shield", "Mana Tide Totem": "Mana Tide Totem",
                 "Nature's Swiftness": "Nature's Swiftness", "Lava Burst": "Lava Burst", "Riptide": "Riptide"}


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
                coefs = {k: float(v) / 100 for v, k in COEF.findall(r.get("coefficient") or "")}
                rm = re.search(r"(\d+) yd range", r.get("range") or "")
                name = sp["name"]
                s = Spell(name=name, school=(r.get("school") or "nature").lower(), rank=int(NUM.search(r.get("rank") or "1").group(1)) if NUM.search(r.get("rank") or "") else 1,
                          level=int(r.get("level") or 1), cost=cost, cast=cast, cooldown=_seconds(r.get("cooldown")),
                          range=_num(rm.group(1)) if rm else 0.0, coef=coefs.get("direct", 0.0), tags=("cost_pct",) if "base mana" in cost_txt else ())
                s.text = txt
                s.interrupt = parse_interrupt(txt)
                dm, fs, he, rk, wf, ft, sh, se, cl, sl = (rx.search(txt) for rx in (DMG, FLAME, HEAL, ROCK, WIND, FLAME_W, SHIELD, SEARING, CLAW, SLOW))
                if name == "Stormstrike":
                    s.kind, s.weapon_pct, s.school = "melee", 1.0, "physical"
                elif fs:
                    s.dmg_min = s.dmg_max = _num(fs.group(1))
                    s.dot, s.dot_dur, s.dot_ticks, s.dot_coef = _num(fs.group(2)), float(fs.group(3)), 4, coefs.get("per tick", 0.0)
                elif dm:
                    s.dmg_min, s.dmg_max = _num(dm.group(1)), _num(dm.group(2))
                elif he:
                    s.kind, s.heal_min, s.heal_max, s.heal_coef = "heal", _num(he.group(1)), _num(he.group(2)), coefs.get("heal", 0.0)
                if rk:
                    s.kind, s.imbue_ap = "buff", float(rk.group(1))
                if wf:
                    s.kind, s.wf_chance, s.wf_attacks, s.wf_ap = "buff", float(wf.group(1)) / 100, int(wf.group(2)), float(wf.group(3))
                if ft:
                    s.kind, s.ft_min, s.ft_max = "buff", float(ft.group(1)), float(ft.group(2))
                if sh:
                    s.kind, s.shield_dmg = "buff", float(sh.group(1))
                if se:
                    s.kind, s.totem_dur, s.totem_min, s.totem_max = "buff", float(se.group(1)), float(se.group(3)), float(se.group(4))
                if cl:
                    s.kind, s.claw_hp, s.claw_dur = "buff", float(cl.group(1)), float(cl.group(2))
                if sl:
                    s.daze, s.chill_dur = float(sl.group(1)) / 100, float(sl.group(2))
                if name in ("Water Shield", "Nature's Swiftness", "Rage of the Farseer", "Mana Tide Totem", "Strength of Earth Totem", "Stoneskin Totem",
                            "Grace of Air Totem", "Windfury Totem", "Healing Stream Totem", "Mana Spring Totem", "Ghost Wolf", "Reincarnation", "Totemic Recall"):
                    s.kind = "buff"
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
    "Convection": "-2%/rank mana on shocks, Lightning Bolt, Lava Burst, Chain Lightning",
    "Concussion": "+1%/rank Lightning Bolt, Chain Lightning, Earth Shock",
    "Elemental Warding": "no caster mobs here",
    "Reverberation": "-0.2 s/rank shock cooldown",
    "Call of Flame": "+5%/rank fire totems and Flame Shock",
    "Elemental Devastation": "spell crits: +3%/rank melee crit for 10 s",
    "Elemental Focus": "10% Clearcasting: the next damage spell is free",
    "Elemental Alacrity": "-0.17 s/rank Lightning Bolt cast",
    "Improved Fire Nova": "AoE only",
    "Eye of the Storm": "23%/rank less pushback on Lightning Bolt",
    "Call of Thunder": "+3% Lightning Bolt crit",
    "Elemental Reach": "+6 yd Lightning Bolt (longer pulls)",
    "Lightning Overload": "3.3%/rank: a second half-damage Lightning Bolt",
    "Earthbound": "not used",
    "Elemental Fury": "+20%/rank spell crit damage bonus",
    "Lava Burst": "Elemental: cast on cooldown (a guaranteed crit on a Flame Shocked target)",
    "Earth's Grasp": "+25%/rank Stoneclaw Totem health",
    "Thundering Strikes": "+1%/rank crit with spells and attacks",
    "Ancestral Knowledge": "+2%/rank Intellect",
    "Guardian Totems": "not used (Stoneskin Totem is not dropped per fight)",
    "Mental Dexterity": "+33%/rank of Intellect as attack power",
    "Improved Ghost Wolf": "travel only",
    "Improved Lightning Shield": "+5%/rank Lightning Shield damage",
    "Elemental Weapons": "+6.7%/rank Rockbiter attack power, +13%/rank Windfury attack power, +? Flametongue",
    "Shamanistic Focus": "-45% mana on shocks and Lightning Shield",
    "Anticipation": "+2%/rank dodge",
    "Toughness": "+2%/rank Stamina",
    "Flurry": "crits: +5%/rank attack speed for the next 3 swings",
    "Stormstrike": "unlocks Stormstrike (weapon damage, +20% on the next Lightning Bolt / Earth Shock, 8 s cooldown)",
    "Spirit Weapons": "+5% parry",
    "Mental Quickness": "+15%/rank of Intellect as spell damage",
    "Improved Stormstrike": "Stormstrike: 50% mana regen while casting for 15 s and a chance to reset its cooldown",
    "Maelstrom Weapon": "4%/rank per melee hit: the next Lightning Bolt casts 20% faster and cheaper per stack (5 stacks = instant)",
    "Rage of the Farseer": "+30% attack speed for 25 s (on the pull, every 3 min assumed)",
    "Improved Healing Wave": "-0.1 s/rank Healing Wave cast",
    "Totemic Focus": "-5%/rank totem mana",
    "Mindfulness": "17%/rank mana regen while casting",
    "Natural Grace": "threat only",
    "Tidal Focus": "-1%/rank heal mana, +1%/rank hit",
    "Improved Reincarnation": "+2%/rank health, -10 min/rank Reincarnation cooldown",
    "Ancestral Healing": "not used",
    "Healing Focus": "23%/rank less pushback on heals",
    "Water Shield": "unlocks Water Shield: 2% mana per hit taken (3 charges), used when mana is low",
    "Tidal Mastery": "+1%/rank heal crit",
    "Restorative Totems": "not used (Mana Spring / Healing Stream are not dropped per fight)",
    "Mana Tide Totem": "not used solo (5 min cooldown; drinking is modelled)",
    "Healing Way": "+8.3%/rank Healing Wave",
    "Nature's Swiftness": "instant Healing Wave every 3 min when low",
    "Purification": "+2%/rank heals",
    "Riptide": "not used",
}
FIT = {
    "Thundering Strikes": "scale", "Ancestral Knowledge": "scale", "Mental Dexterity": "scale", "Improved Lightning Shield": "scale", "Elemental Weapons": "scale",
    "Shamanistic Focus": "scale", "Anticipation": "scale", "Toughness": "scale", "Flurry": "scale",
    "Stormstrike": ("replace", [{"channel": "dmg", "scope": ["type:melee"], "values": [0.10]}]),
    "Spirit Weapons": "scale", "Mental Quickness": "scale", "Improved Stormstrike": "scale", "Maelstrom Weapon": "scale", "Rage of the Farseer": "scale",
    "Convection": "scale", "Concussion": "scale", "Reverberation": "scale", "Call of Flame": "scale", "Elemental Devastation": "scale", "Elemental Focus": "scale",
    "Elemental Alacrity": "scale", "Eye of the Storm": "scale", "Call of Thunder": "scale", "Elemental Reach": "scale", "Lightning Overload": "scale", "Elemental Fury": "scale",
    "Improved Healing Wave": "scale", "Totemic Focus": "scale", "Mindfulness": "scale", "Tidal Focus": "scale", "Improved Reincarnation": "scale", "Healing Focus": "scale",
    "Water Shield": "scale", "Tidal Mastery": "scale", "Restorative Totems": "scale", "Mana Tide Totem": "scale", "Healing Way": "scale", "Nature's Swiftness": "scale",
    "Purification": "scale",
}
SHARE_SOURCE = {'Chain Lightning': 'chain_lightning', 'Fire Nova': 'fire_nova', 'Magma Totem': 'magma', "Melee": "white", "Windfury": "windfury", "Earth Shock": "earth_shock", "Lightning Bolt": "lightning_bolt", "Flame Shock": "flame_shock",
                "Lightning Shield": "lightning_shield", "Stormstrike": "stormstrike", "Searing Totem": "searing_totem", "Flametongue Weapon": "rockbiter"}
NEW_SOURCES = {'chain_lightning': {'id': 'chain_lightning', 'share': 0.0, 'min_level': 32, 'tags': ['type:spell', 'school:nature', 'aoe', 'ability:Chain Lightning', 'enh-nature'], 'cast': 2.0, 'min_cast': 1.5}, 'fire_nova': {'id': 'fire_nova', 'share': 0.0, 'min_level': 12, 'tags': ['type:spell', 'school:fire', 'instant', 'aoe', 'ability:Fire Nova', 'ability:Fire Nova Totem', 'totem']}, 'magma': {'id': 'magma', 'share': 0.0, 'min_level': 26, 'tags': ['type:spell', 'school:fire', 'dot', 'aoe', 'ability:Magma Totem', 'totem']}, "stormstrike": {"id": "stormstrike", "share": 0.0, "min_level": 25, "tags": ["type:melee", "yellow", "school:physical", "ability:Stormstrike", "weapon:2h"], "cooldown": 8},
               "searing_totem": {"id": "searing_totem", "share": 0.0, "min_level": 10, "tags": ["type:spell", "school:fire", "ability:Searing Totem", "ability:Fire Totems", "totem"], "can_crit": True}}
KEY_TALENTS = ["Stormstrike", "Flurry", "Maelstrom Weapon"]
DESCRIPTION = ("Single-target leveling fights against normal mobs of your level with a slow two-hander: Lightning Shield (Water Shield when talented and mana is low) and "
               "the weapon imbue up (Rockbiter's attack power until 30, Windfury's extra attacks from 30), Searing Totem dropped at the pull, a Lightning Bolt while the mob "
               "walks in, then Stormstrike, Earth Shock (buffed by Stormstrike), Flame Shock while mana allows and instant Maelstrom Lightning Bolts between white swings; "
               "Stoneclaw Totem and a Lesser Healing Wave when low, Nature's Swiftness + Healing Wave in an emergency; a death with Reincarnation ready costs 30 s "
               "instead of 90. Between fights: 2 s loot, 6 s travel, heals back to 80% health, water below 35% mana.")
NOT_MODELLED = "runners, adds, Strength of Earth / Stoneskin / Grace of Air totems (5-minute totems left behind between mobs), Frost Shock kiting, Chain Lightning, Ghost Wolf travel, gear upgrades within a level bracket."
# rebuild.py: which scorer model, hand draft and optimizer build the pipeline calibrates, races and reports for this class
PIPELINE = {"variants": [{'spec': 'enhancement-dps', 'opt': 'opt-enhancement-dps-leveling-aoe', 'tag': 'aoe', 'profile': 'leveling-aoe', 'lookahead': 16, 'sets': ['MOBS_PER_PULL=3'], 'levels': '30,40,50,60', 'calibrate_levels': '40,60', 'label': 'AoE grinding, 3 mobs per pull'},
                          {'spec': 'elemental-dps', 'opt': 'opt-elemental-dps-leveling-st', 'tag': 'ele', 'profile': 'leveling-st', 'lookahead': 16, 'sets': [],
                           'levels': '20,30,40,50,60', 'calibrate_levels': '30,60', 'label': 'Elemental (its own rotation)', 'report': 'elemental-dps-opt'}], "spec": "enhancement-dps", "hand": "leveling-enhancement", "opt": "opt-enhancement-dps-leveling-st", "tag": "enh", "lookahead": 16,
            "levels": "20,30,40,50,60", "calibrate_levels": "30,60",
            "extra_reports": [{"spec": "elemental-dps", "build": "opt-elemental-dps-leveling-st", "compare": ["opt-enhancement-dps-leveling-st"]}]}


class ShamanModule(BaseModule):
    resource = "mana"
    melee = True
    IMBUE = "auto"   # "auto" = Windfury from 30, Rockbiter before; "rockbiter" / "windfury" / "flametongue" to test

    AOE = {'direct': ['Chain Lightning', 'Fire Nova', 'Magma Totem'], 'dots': ['Flame Shock'], 'min_near': 2}

    def __init__(self, talents, level, spec="enhancement-dps", gear="leveling"):
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
        self._base_mana = 0.0
        self.flurry_swings = 0
        self.imbue = self.pick_imbue()
        self.armor_spell_used = f"{self.imbue.name if self.imbue else 'no imbue'}, Lightning Shield" if "Lightning Shield" in self.spells else "none"

    def pick_imbue(self):
        wf, rb, ft = self.spells.get("Windfury Weapon"), self.spells.get("Rockbiter Weapon"), self.spells.get("Flametongue Weapon")
        if self.IMBUE == "rockbiter":
            return rb
        if self.IMBUE == "windfury":
            return wf or rb
        if self.IMBUE == "flametongue":
            return ft or rb
        return wf if wf is not None else rb

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
        base = class_base_stats("shaman", level)
        g = gear_stats(level, self.gear, "shaman")
        strength = base["strength"] + g["strength"]
        agility = base["agility"] + g["agility"]
        stamina = (base["stamina"] + g["stamina"]) * (1 + self.tv("Toughness", 0) / 100)
        intellect = (base["intellect"] + g["intellect"]) * (1 + self.tv("Ancestral Knowledge", 0) / 100)
        spirit = base["spirit"] + g["spirit"]
        bm = class_base_mana("shaman", level)
        p = Player(level=level, hp_max=(class_base_health("shaman", level) + 10 * stamina) * (1 + self.tv("Improved Reincarnation", 1) / 100), hp=0.0,
                   mana_max=bm + 15 * intellect, mana=0.0, base_mana=bm, spirit=spirit, intellect=intellect,
                   spell_power=g["spell_power"] + intellect * self.tv("Mental Quickness", 0) / 100, armor=g["armor"],
                   spell_crit=class_spell_crit("shaman", level, intellect) + self.tv("Thundering Strikes", 0) / 100,
                   dodge=class_dodge("shaman", level, agility) + self.tv("Anticipation", 0) / 100, ranged_crit=0.0)
        p.strength, p.agility, p.stamina = strength, agility, stamina
        ap = class_attack_power("shaman", level, strength, agility) + intellect * self.tv("Mental Dexterity", 0) / 100
        imb = self.imbue
        if imb is not None and getattr(imb, "imbue_ap", 0.0):
            ap += imb.imbue_ap * (1 + self.tv("Elemental Weapons", 0) / 100)
        p.attack_power = ap
        p.melee_crit = class_melee_crit("shaman", level, agility) + self.tv("Thundering Strikes", 0) / 100
        p.hit_bonus = self.tv("Tidal Focus", 1) / 100
        p.parry = 0.05 if self.rank("Spirit Weapons") else 0.0
        dps = weapon_dps(level, "2h")
        p.mh = Weapon(dmg_min=dps * WEAPON_SPEED["2h"] * 0.8, dmg_max=dps * WEAPON_SPEED["2h"] * 1.2, speed=WEAPON_SPEED["2h"], kind="2h")
        p.hp, p.mana = p.hp_max, p.mana_max
        p.regen_while_casting = self.tv("Mindfulness", 0) / 100
        self.base_regen_while_casting = p.regen_while_casting
        return p

    def pull_range(self):
        lb = self.spells.get("Lightning Bolt")
        return (lb.range if lb and lb.range else 30.0) + self.tv("Elemental Reach", 0)

    # ------------------------------------------------------------ engine hooks: numbers
    def mana_cost(self, spell):
        cost = spell.cost
        if "cost_pct" in spell.tags:
            cost = cost / 100 * self._base_mana
        if spell.name in ("Earth Shock", "Flame Shock", "Frost Shock", "Lightning Bolt", "Lava Burst", "Chain Lightning"):
            cost *= 1 - self.tv("Convection", 0) / 100
        if spell.name in ("Earth Shock", "Flame Shock", "Frost Shock", "Lightning Shield") and self.rank("Shamanistic Focus"):
            cost *= 0.55
        if spell.name.endswith("Totem"):
            cost *= 1 - self.tv("Totemic Focus", 0) / 100
        if spell.kind == "heal":
            cost *= 1 - self.tv("Tidal Focus", 0) / 100
        if spell.name == "Lightning Bolt" and self._fight:
            mw = self._fight.p.buff("Maelstrom Weapon", self._fight.t)
            if mw:
                cost *= max(0.0, 1 - 0.2 * mw["stacks"])
        return cost

    def final_cost(self, fight, spell, cost):
        if fight.p.buff("Clearcasting", fight.t) and spell.dmg_max > 0:
            del fight.p.buffs["Clearcasting"]
            return 0.0
        return cost

    def cast_time(self, spell):
        c = spell.cast
        f = self._fight
        if spell.name in ("Lightning Bolt", "Chain Lightning", "Lava Burst"):
            c = max(GCD, c - self.tv("Elemental Alacrity", 0))
            if spell.name == "Lightning Bolt" and f:
                mw = f.p.buff("Maelstrom Weapon", f.t)
                if mw:
                    c = c * max(0.0, 1 - 0.2 * mw["stacks"])
                    if c < 0.5:
                        c = 0.0
        if spell.name == "Healing Wave":
            c = max(GCD, c - 0.1 * self.rank("Improved Healing Wave"))
        if c > 0 and f and f.p.buff("Nature's Swiftness", f.t) and spell.school == "nature":
            return 0.0
        return c

    def hit_bonus(self, spell):
        return 0.0

    def _lava_burst_crit(self, spell):
        f = self._fight
        return 1.0 if (spell.name == "Lava Burst" and f is not None and f.dot_active("Flame Shock")) else 0.0

    def crit_bonus(self, spell, frozen):
        if spell.name == "Lava Burst":
            return self._lava_burst_crit(spell)
        c = 0.0
        f = self._fight
        if spell.name in ("Lightning Bolt", "Chain Lightning"):
            c += self.tv("Call of Thunder", 0) / 100
        if spell.kind == "melee" and f and f.p.buff("Elemental Devastation", f.t):
            c += self.tv("Elemental Devastation", 0) / 100
        return c

    def crit_damage_bonus(self, spell):
        if spell.kind in ("spell", "channel") or spell.name == "Searing Totem":
            return self.tv("Elemental Fury", 0) / 100
        return 0.0

    def damage_multiplier(self, spell, frozen):
        m = 1.0
        f = self._fight
        if spell.name in ("Lightning Bolt", "Chain Lightning", "Earth Shock"):
            m *= 1 + self.tv("Concussion", 0) / 100
            if f and f.p.buff("Stormstrike", f.t):
                m *= 1.20
        if spell.name in ("Flame Shock", "Searing Totem", "Magma Totem", "Fire Nova"):
            m *= 1 + self.tv("Call of Flame", 0) / 100
        if spell.name == "Lightning Shield":
            m *= 1 + self.tv("Improved Lightning Shield", 0) / 100
        return m

    def heal_multiplier(self, spell):
        m = 1 + self.tv("Purification", 0) / 100
        if spell.name == "Healing Wave":
            m *= 1 + self.tv("Healing Way", 0) / 100
        return m

    def periodic_can_crit(self, spell):
        return True

    def swing_speed_factor(self):
        f = 1.0 / (1 + self.tv("Flurry", 0) / 100) if self.flurry_swings > 0 else 1.0
        if self._fight and self._fight.p.buff("Rage of the Farseer", self._fight.t):
            f /= 1.3
        return f

    def mana_regen(self, p, t):
        p.regen_while_casting = max(self.base_regen_while_casting, 0.5 if p.buff("Improved Stormstrike", t) else 0.0)
        return class_mana_regen_tick("shaman", p.spirit)

    def health_regen(self, p):
        return class_health_regen_tick("shaman", p.spirit)

    def pushback_resisted(self, fight, spell):
        if spell.name in ("Lightning Bolt", "Chain Lightning", "Lava Burst") and self.rank("Eye of the Storm"):
            return fight.rng.random() < self.tv("Eye of the Storm", 0) / 100
        if spell.kind == "heal" and self.rank("Healing Focus"):
            return fight.rng.random() < self.tv("Healing Focus", 0) / 100
        return False

    def death_time(self, p, t):
        if "Reincarnation" in self.spells and p.ready("Reincarnation", t):
            p.cooldowns["Reincarnation"] = t + max(600.0, 3600.0 - 600.0 * self.rank("Improved Reincarnation"))
            return 30.0
        return DEATH_TIME

    # ------------------------------------------------------------ engine hooks: events
    def on_fight_start(self, fight):
        self._fight = fight
        self._base_mana = fight.p.base_mana
        p, t = fight.p, fight.t
        self.flurry_swings = 0
        # shields: Lightning Shield by default, Water Shield when talented and mana is low
        ls, ws = self.spells.get("Lightning Shield"), self.spells.get("Water Shield")
        sh = p.buffs.get("Shield")
        if sh is None or sh.get("charges", 0) <= 0:
            if ws is not None and p.mana < 0.6 * p.mana_max:
                p.buffs["Shield"] = {"until": t + 600.0, "charges": 3, "kind": "water", "icd": 0.0}
            elif ls is not None and p.mana >= self.mana_cost(ls) + 100:
                p.mana -= self.mana_cost(ls)
                p.buffs["Shield"] = {"until": t + 600.0, "charges": 3, "kind": "lightning", "icd": 0.0, "dmg": ls.shield_dmg + ls.coef * p.spell_power}
                fight.casts["Lightning Shield"] = fight.casts.get("Lightning Shield", 0) + 1
        # Searing Totem: a fire totem that shoots the mob every 2.2 s
        st = self.spells.get("Searing Totem")
        if st is not None and p.mana >= self.mana_cost(st) + 200 and p.mana > 0.5 * p.mana_max:
            p.mana -= self.mana_cost(st)
            ticks = int(st.totem_dur / 2.2)
            per = (st.totem_min + st.totem_max) / 2 + st.coef * p.spell_power
            fight.refresh_dot("Searing Totem", per * ticks * self.damage_multiplier(st, False), ticks, 2.2, p.spell_crit, 1.5 + self.crit_damage_bonus(st))
            fight.casts["Searing Totem"] = fight.casts.get("Searing Totem", 0) + 1
            p.gcd_until = t + 1.0
        rf = self.spells.get("Rage of the Farseer")
        if rf is not None and p.ready("Rage of the Farseer", t):
            p.buffs["Rage of the Farseer"] = {"until": t + 25.0}
            p.cooldowns["Rage of the Farseer"] = t + (rf.cooldown or 180.0)

    def on_swing(self, fight, spell, outcome, amount, hand):
        p, m, t = fight.p, fight.m, fight.t
        if outcome in ("miss", "dodge", "parry"):
            return
        if outcome == "crit" and self.rank("Flurry"):
            self.flurry_swings = 3
        elif spell.name == "Melee" and self.flurry_swings > 0:
            self.flurry_swings -= 1
        imb = self.imbue
        if imb is not None and not getattr(fight, "_wf", False):
            if getattr(imb, "wf_chance", 0.0) and fight.rng.random() < imb.wf_chance:
                fight._wf = True
                bonus = imb.wf_ap * (1 + self.tv("Elemental Weapons", 1) / 100)
                p.attack_power += bonus
                for _ in range(imb.wf_attacks):
                    fight.resolve_attack(Spell("Windfury", "physical", kind="melee", resource="none"), white=True, hand="mh")
                p.attack_power -= bonus
                fight._wf = False
            elif getattr(imb, "ft_max", 0.0):
                dmg = fight.rng.uniform(imb.ft_min, imb.ft_max) * (1 + self.tv("Elemental Weapons", 2) / 100)
                fight.deal(Spell("Flametongue Weapon", "fire"), dmg, False)
        if self.rank("Maelstrom Weapon") and fight.rng.random() < 0.04 * self.rank("Maelstrom Weapon"):
            b = p.buffs.get("Maelstrom Weapon")
            stacks = min(5, (b["stacks"] if b and b["until"] > t else 0) + 1)
            p.buffs["Maelstrom Weapon"] = {"until": t + 30.0, "stacks": stacks}
        if spell.name == "Stormstrike":
            p.buffs["Stormstrike"] = {"until": t + 12.0}
            if self.rank("Improved Stormstrike"):
                p.buffs["Improved Stormstrike"] = {"until": t + 15.0}

    def on_hit(self, fight, spell, amount, crit, frozen):
        p, m, t = fight.p, fight.m, fight.t
        if spell.name in ("Lightning Bolt", "Chain Lightning", "Earth Shock") and p.buff("Stormstrike", t) and amount > 0:
            del p.buffs["Stormstrike"]
        if spell.name == "Lightning Bolt" and p.buff("Maelstrom Weapon", t):
            del p.buffs["Maelstrom Weapon"]
        if spell.name == "Lightning Bolt" and self.rank("Lightning Overload") and amount > 0 and fight.rng.random() < self.tv("Lightning Overload", 0) / 100:
            fight.deal(Spell("Lightning Bolt", "nature"), amount * 0.5, False)
        if spell.kind == "spell" and amount > 0 and self.rank("Elemental Focus") and fight.rng.random() < 0.10:
            p.buffs["Clearcasting"] = {"until": t + 15.0}
        if crit and spell.kind == "spell" and self.rank("Elemental Devastation"):
            p.buffs["Elemental Devastation"] = {"until": t + 10.0}
        if spell.name == "Nature's Swiftness":
            p.buffs["Nature's Swiftness"] = {"until": t + 60.0}
        if spell.name == "Stoneclaw Totem":
            m.stun_until = max(m.stun_until, t + 4.0)   # the mob turns on the totem for a few hits
            m.threat_player += 0.0
        if spell.kind == "heal" and spell.cast > 0 and p.buff("Nature's Swiftness", t):
            del p.buffs["Nature's Swiftness"]

    def on_hit_taken(self, fight, dmg, crit=False):
        p, m, t = fight.p, fight.m, fight.t
        sh = p.buffs.get("Shield")
        if sh and sh.get("charges", 0) > 0 and t >= sh.get("icd", 0.0):
            sh["charges"] -= 1
            sh["icd"] = t + 3.0
            if sh["kind"] == "lightning":
                dmg_out = sh["dmg"] * self.damage_multiplier(Spell("Lightning Shield", "nature"), False)
                lcrit = fight.rng.random() < p.spell_crit
                if lcrit:
                    dmg_out *= 1.5 + self.crit_damage_bonus(Spell("Lightning Shield", "nature", kind="spell"))
                fight.deal(Spell("Lightning Shield", "nature"), dmg_out, lcrit)
            else:
                p.mana = min(p.mana_max, p.mana + 0.02 * p.mana_max)

    def after_cast(self, fight, spell):
        p, t = fight.p, fight.t
        cd = spell.cooldown
        if spell.name in ("Earth Shock", "Flame Shock", "Frost Shock"):
            cd = max(GCD, cd - self.tv("Reverberation", 0))
            for other in ("Earth Shock", "Flame Shock", "Frost Shock"):   # shocks share a cooldown
                p.cooldowns[other] = max(p.cooldowns.get(other, 0.0), t + cd)
            return
        if cd > 0:
            p.cooldowns[spell.name] = t + cd

    def after_fight(self, p, t):
        spent = 0.0
        hw, lhw = self.spells.get("Healing Wave"), self.spells.get("Lesser Healing Wave")
        for _ in range(3):
            if p.hp >= 0.80 * p.hp_max:
                break
            missing = p.hp_max - p.hp
            heal = lhw if (lhw is not None and missing < (lhw.heal_min + lhw.heal_max) / 2 * 1.5) else (hw or lhw)
            if heal is None or p.mana < self.mana_cost(heal):
                break
            p.mana -= self.mana_cost(heal)
            amount = ((heal.heal_min + heal.heal_max) / 2 + heal.heal_coef * p.spell_power) * self.heal_multiplier(heal)
            p.hp = min(p.hp_max, p.hp + amount)
            spent += max(GCD, self.cast_time(heal))
        return spent

    # ------------------------------------------------------------ priority list
    def decide_elemental(self, fight, can, in_melee):
        """Elemental: Lightning Bolts from range (the pull and while the mob walks in), then Flame Shock, Earth Shock and
        Lava Burst on cooldown with Lightning Bolts between them while mana lasts; a bolt in melee eats pushback (Eye of the
        Storm resists it); the weapon swings whenever nothing is cast."""
        p, m, t = fight.p, fight.m, fight.t
        sp = self.spells
        lb, es, fs, lvb = (sp.get(n) for n in ("Lightning Bolt", "Earth Shock", "Flame Shock", "Lava Burst"))
        hp = m.hp
        avg_lb = ((lb.dmg_min + lb.dmg_max) / 2 + lb.coef * p.spell_power) * self.damage_multiplier(lb, False) if lb else 0.0
        reserve = (self.mana_cost(es) if es else 0.0) + (self.mana_cost(fs) if fs else 0.0)
        if not in_melee:
            if lb and can(lb) and m.dist <= lb.range + self.tv("Elemental Reach", 0) and (m.dist - MELEE_RANGE) / max(0.1, m.speed(t)) >= self.cast_time(lb) - 0.6:
                return lb
            if fs and can(fs) and not fight.dot_active("Flame Shock") and m.dist <= fs.range and hp > 0.3 * m.hp_max:
                return fs
            if es and can(es) and m.dist <= es.range and hp <= es.dmg_max * 1.2:
                return es
            return None
        if es and can(es) and hp <= es.dmg_max * self.damage_multiplier(es, False):
            return es
        if fs and can(fs) and not fight.dot_active("Flame Shock") and hp > 0.3 * m.hp_max:
            return fs
        if lvb and can(lvb) and hp > lvb.dmg_min * 0.5:
            return lvb
        if es and can(es) and hp > es.dmg_min * 0.5:
            return es
        if lb and can(lb) and p.mana - self.mana_cost(lb) >= reserve and hp > avg_lb * 0.6:
            return lb
        return None

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

        lb, ss, es, fs, claw, lhw, hw, ns = (sp.get(n) for n in ("Lightning Bolt", "Stormstrike", "Earth Shock", "Flame Shock", "Stoneclaw Totem", "Lesser Healing Wave", "Healing Wave", "Nature's Swiftness"))
        hp = m.hp
        mw = p.buff("Maelstrom Weapon", t)
        # emergencies
        if p.hp < 0.30 * p.hp_max and hp > 0.2 * m.hp_max:
            if ns and can(ns) and hw and not p.buff("Nature's Swiftness", t):
                return ns
            if hw and can(hw) and p.buff("Nature's Swiftness", t):
                return hw
            if claw and can(claw) and not m.stunned(t):
                return claw
        if p.hp < 0.40 * p.hp_max and hp > 0.25 * m.hp_max and lhw and can(lhw) and (m.stunned(t) or not in_melee or p.mana > 0.5 * p.mana_max):
            return lhw
        # a casting mob: Earth Shock interrupts it (2 s lockout, it runs in)
        if m.caster and m.casting(t) and es and can(es) and m.dist <= es.range:
            return es
        if self.spec.startswith("elemental"):
            return self.decide_elemental(fight, can, in_melee)
        # the pull: a bolt while the mob walks in
        if not in_melee:
            if lb and can(lb) and m.dist <= lb.range + self.tv("Elemental Reach", 0) and (m.dist - MELEE_RANGE) / max(0.1, m.speed(t)) >= self.cast_time(lb) - 0.6:
                return lb
            return "advance"
        if lb and can(lb) and mw and mw["stacks"] >= 5 and hp > lb.dmg_max:
            return lb
        if ss and can(ss):
            return ss
        if es and can(es) and hp > es.dmg_min * 0.5:
            return es
        if fs and can(fs) and not fight.dot_active("Flame Shock") and p.mana > 0.55 * p.mana_max and hp > 0.4 * m.hp_max:
            return fs
        return None
