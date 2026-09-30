"""Hunter module for the fight lab (Beast Mastery leveling with a cat).

Spell ranks are read from `_reference/data/forever-spells/hunter.json` (beta client build 1.60.1.70009); talent numbers from
each rank's tooltip in `_reference/data/forever-talents/hunter.json`. Pet stats: the level-60 hunter pet of the
ElliotWood/Forever simulator (`sim/hunter/pet.go`: Forever pets inherit nothing from the hunter; cat family x1.10 damage,
happiness x1.25), scaled by level here; Claw/Bite from the beta spellbook; Summon Hawk as the simulator models it (dive
bomb, then the same hit every 3 s for 18 s).

Playstyle `bm-leveling` (the scorer's model id): the cat runs in and Growls, the hunter shoots from 35 yd: Hunter's Mark,
Serpent Sting, Summon Hawk or Arcane Shot, Multi-Shot / Aimed Shot on their shared cooldown, Auto Shot in between; Bestial
Wrath, Intimidation and Rapid Fire on the pull when ready; Mend Pet when the pet drops low; Feign Death, Wing Clip and
Raptor Strike when a mob reaches the hunter. Between fights: Mend Pet, food and water.
"""
import json
import pathlib
import dataclasses
import re

from engine import parse_interrupt, BaseModule, Pet, Player, Spell, Weapon
from tables import (GCD, MELEE_RANGE, WEAPON_SPEED, ammo_dps, class_attack_power, class_base_health, class_base_mana, class_base_stats,
                    class_dodge, class_health_regen_tick, class_mana_regen_tick, class_melee_crit, class_ranged_ap, class_spell_crit,
                    gear_stats, weapon_dps)

ROOT = pathlib.Path(__file__).resolve().parents[3]
SPELLBOOK = json.load(open(ROOT / "_reference/data/forever-spells/hunter.json", encoding="utf-8"))
TREE = json.load(open(ROOT / "_reference/data/forever-talents/hunter.json", encoding="utf-8"))

NUM = re.compile(r"(\d+(?:\.\d+)?)")
DMG = re.compile(r"(\d[\d,]*) to (\d[\d,]*) (?:(\w+) )?damage")
FLAT = re.compile(r"caus(?:es|ing) (\d[\d,]*) (\w+) damage(?! over)|Inflicts (\d[\d,]*) damage|dealing (\d[\d,]*) (\w+) damage")
DOT = re.compile(r"caus(?:es|ing) (\d[\d,]*) (\w+) damage over (\d+) sec")
PLUS = re.compile(r"weapon damage plus (\d[\d,]*)")
RANGED_PLUS = re.compile(r"increases ranged damage by (\d[\d,]*)")
MEND = re.compile(r"Heals your pet (\d[\d,]*) health every second[^.]*?Lasts (\d+) sec")
RAP = re.compile(r"Ranged Attack Power[^0-9]*?by (\d+)")
MAP = re.compile(r"Melee Attack Power by (\d+)")
DAZE = re.compile(r"slowing movement speed by (\d+)% for (\d+) sec|reduces the enemy target's movement speed by (\d+)% for (\d+) sec")
STUN = re.compile(r"Stun the target for (\d+) sec")
COEF = re.compile(r"([\d.]+)% of spell power \((\w+(?: \w+)?)\)")

TALENT_SPELLS = {"Summon Hawk": "Summon Hawk", "Intimidation": "Intimidation", "Bestial Wrath": "Bestial Wrath", "Trueshot Aura": "Trueshot Aura",
                 "Scatter Shot": "Scatter Shot", "Sniper Shot": "Sniper Shot", "Counterattack": "Counterattack", "Deterrence": "Deterrence",
                 "Strider Kick": "Strider Kick", "Lacerating Strikes": "Lacerating Strikes"}
MELEE = {"Raptor Strike", "Mongoose Bite", "Wing Clip", "Counterattack", "Strider Kick"}
RANGED = {"Arcane Shot", "Multi-Shot", "Aimed Shot", "Serpent Sting", "Concussive Shot", "Scatter Shot", "Sniper Shot", "Summon Hawk", "Scorpid Sting", "Viper Sting"}
SHARED_CD = {"Multi-Shot": ("Aimed Shot",), "Aimed Shot": ("Multi-Shot",), "Arcane Shot": ("Summon Hawk",), "Summon Hawk": ("Arcane Shot",),
             "Immolation Trap": ("Explosive Trap",), "Explosive Trap": ("Immolation Trap",)}   # fire traps share their cooldown
TRAPS = ("Immolation Trap", "Explosive Trap")


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
                channel = "channel" in cast_txt
                cast = 0.0 if "instant" in cast_txt or channel or not cast_txt else _seconds(cast_txt)
                coefs = {k: float(v) / 100 for v, k in COEF.findall(r.get("coefficient") or "")}
                rm = re.search(r"(\d+) yd range", r.get("range") or "")
                name = sp["name"]
                s = Spell(name=name, school=(r.get("school") or "physical").lower(),
                          rank=int(NUM.search(r.get("rank") or "1").group(1)) if NUM.search(r.get("rank") or "") else 1,
                          level=int(r.get("level") or 1), cost=cost, cast=cast, cooldown=_seconds(r.get("cooldown")),
                          range=_num(rm.group(1)) if rm else 0.0, tags=("cost_pct",) if "base mana" in cost_txt else ())
                s.text = txt
                s.interrupt = parse_interrupt(txt)
                dm, fl, dt, pl, rp, me, ra, ma, dz, st = (rx.search(txt) for rx in (DMG, FLAT, DOT, PLUS, RANGED_PLUS, MEND, RAP, MAP, DAZE, STUN))
                if name in MELEE:
                    s.kind, s.school = "melee", "physical"
                    s.on_next_swing = name == "Raptor Strike"
                    if pl:
                        s.weapon_pct, s.dmg_min, s.dmg_max = 1.0, _num(pl.group(1)), _num(pl.group(1))
                    if "100% melee weapon damage" in txt or "50% weapon damage" in txt:
                        s.weapon_pct = 0.5 if "50%" in txt else 1.0
                elif name in RANGED:
                    s.kind = "ranged"
                    if name in ("Multi-Shot", "Aimed Shot", "Scatter Shot"):
                        s.weapon_pct = 0.5 if name == "Scatter Shot" else 1.0
                    if rp:
                        s.dmg_min = s.dmg_max = _num(rp.group(1))
                if dm and not s.dmg_max:
                    s.dmg_min, s.dmg_max = _num(dm.group(1)), _num(dm.group(2))
                elif fl and not s.dmg_max:
                    v = fl.group(1) or fl.group(3) or fl.group(4)
                    s.dmg_min = s.dmg_max = _num(v)
                if dt:
                    s.dot, s.dot_dur = _num(dt.group(1)), float(dt.group(3))
                    s.dot_ticks = max(1, int(round(s.dot_dur / 3.0)))
                if me:
                    per, dur = _num(me.group(1)), float(me.group(2))
                    s.kind, s.channel, s.dot_ticks, s.hot, s.hot_dur, s.target, s.heal_coef = "channel", dur, int(dur), per * dur, dur, "pet", 0.0
                if ra:
                    s.kind, s.rap = "buff", _num(ra.group(1))
                if ma:
                    s.kind, s.map = "buff", _num(ma.group(1))
                if dz:
                    s.daze, s.chill_dur = float(dz.group(1) or dz.group(3)) / 100, float(dz.group(2) or dz.group(4))
                if st and name == "Intimidation":
                    s.kind, s.stun = "buff", float(st.group(1))
                if name in ("Bestial Wrath", "Rapid Fire", "Feign Death", "Aspect of the Monkey", "Aspect of the Cheetah", "Call Pet", "Revive Pet", "Deterrence"):
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
    "Deadly Aspects": "2%/rank per Auto Shot: +30% ranged attack speed for 12s (Aspect of the Hawk)",
    "Endurance Training": "+3%/rank pet health and armor",
    "Focused Fire": "+1%/rank damage for you and the pet",
    "Improved Aspect of the Monkey": "not used (Aspect of the Hawk is up)",
    "Pathfinding": "travel speed only",
    "Improved Revive Pet": "-3s/rank Revive Pet",
    "Bestial Swiftness": "+30% pet speed: the pet reaches the mob sooner",
    "Unleashed Fury": "+3%/rank pet and hawk damage",
    "Improved Mend Pet": "-10%/rank Mend Pet mana",
    "Ferocity": "+2%/rank pet and hawk crit",
    "Summon Hawk": "unlocks Summon Hawk (dive bomb + the same hit every 3s for 18s, 2 hawks; shares Arcane Shot's cooldown)",
    "Spirit Bond": "hunter and pet regain 1%/rank of health per 5s in combat",
    "Intimidation": "pet stuns the mob 3s (its next hit crits), every 1 min",
    "Bestial Discipline": "+10%/rank pet focus regen, 25%/rank mana regen while casting",
    "Frenzy": "20%/rank on a pet crit: +30% pet attack speed for 8s",
    "Bestial Wrath": "+50% pet damage for 18s every 2 min (on the pull)",
    "Hawk Eye": "+2 yd/rank ranged range (longer pulls)",
    "Improved Concussive Shot": "4%/rank stun 3s on Concussive Shot",
    "Lethal Attacks": "+1%/rank crit with all attacks",
    "Improved Stings": "+6.7%/rank Serpent Sting",
    "Efficiency": "-3%/rank mana on shots, stings and melee abilities",
    "Careful Aim": "+20%/rank of Intellect as attack power",
    "Rapid Killing": "-1 min/rank Rapid Fire cooldown",
    "Improved Arcane Shot": "-0.3s/rank Arcane Shot cooldown",
    "Lone Wolf": "+20% damage with no pet: the pet is not summoned when the talent is taken (the melee build's choice)",
    "Trueshot Aura": "+ranged attack power by level (30..75)",
    "Mortal Shots": "+6%/rank ranged crit damage bonus",
    "Rapid Recuperation": "50% mana regen while casting for 15s after Serpent Sting",
    "Barrage": "+3.3%/rank Multi-Shot and Aimed Shot",
    "Scatter Shot": "not used (the pet holds the mob)",
    "Ranged Weapon Specialization": "+1%/rank ranged damage",
    "Sniper Shot": "not used (4s cast; Multi-Shot / Aimed Shot fill the slot)",
    "Improved Tracking": "+1%/rank damage (the mob is assumed tracked)",
    "Deflection": "+2%/rank parry when meleeing",
    "Savage Strikes": "+2%/rank melee ability crit",
    "Survivalist": "+2%/rank health",
    "Surefooted": "+1%/rank hit",
    "Lightning Reflexes": "+3%/rank Agility",
    "Predator's Edge": "+6%/rank melee crit damage",
    "Improved Wing Clip": "6.7%/rank root 5s on Wing Clip",
    "Deterrence": "+25% dodge and parry for 10 s; the melee rotation presses it below 40% health (5 min cooldown)",
    "Survivalist's Discipline": "-20%/rank Deterrence and trap cooldown (the melee hunter's Immolation Trap)",
    "Resourcefulness": "-30%/rank mana on melee abilities; a crit has a 30%/rank chance to let 50% of mana regen continue while casting for 30 s",
    "Counterattack": "not used (needs a parry)",
    "Entrapment": "a root when a trap fires: the melee hunter's mob stands beside it anyway (not used)",
    "Survival Tactics": "+5%/rank chance to hit with traps (the melee hunter's Immolation Trap)",
    "Clever Traps": "+15%/rank Immolation and Explosive Trap damage (the melee hunter's Immolation Trap)",
}
FIT = {
    "Unleashed Fury": "scale", "Ferocity": "scale", "Endurance Training": "scale", "Focused Fire": "scale", "Bestial Swiftness": "scale",
    "Summon Hawk": ("replace", [{"channel": "dmg", "scope": ["all"], "values": [0.10]}]),
    "Spirit Bond": "scale", "Intimidation": "scale", "Bestial Discipline": "scale", "Frenzy": "scale", "Bestial Wrath": "scale", "Deadly Aspects": "scale",
    "Improved Mend Pet": "scale", "Improved Revive Pet": "scale", "Hawk Eye": "scale", "Improved Concussive Shot": "scale", "Lethal Attacks": "scale",
    "Improved Stings": "scale", "Efficiency": "scale", "Careful Aim": "scale", "Rapid Killing": "scale", "Improved Arcane Shot": "scale", "Trueshot Aura": "scale",
    "Mortal Shots": "scale", "Rapid Recuperation": "scale", "Barrage": "scale", "Ranged Weapon Specialization": "scale", "Improved Tracking": "scale",
    "Surefooted": "scale", "Survivalist": "scale", "Lightning Reflexes": "scale", "Savage Strikes": "scale", "Deflection": "scale", "Resourcefulness": "scale",
}
SHARE_SOURCE_BY_SPEC = {"melee-dps": {"Melee": "melee", "Melee (off-hand)": "melee_oh", "Raptor Strike": "raptor_strike", "Mongoose Bite": "mongoose_bite", "Counterattack": "counterattack",
                                      "Strider Kick": "strider_kick", "Lacerate": "lacerate", "Serpent Sting": "serpent", "Cat melee": "pet", "Claw": "pet", "Bite": "pet", "Summon Hawk": "pet"}}
SHARE_SOURCE = {'Volley': 'volley', "Auto Shot": "auto", "Multi-Shot": "multi", "Arcane Shot": "arcane", "Serpent Sting": "serpent", "Melee": "melee", "Raptor Strike": "melee",
                "Cat melee": "pet", "Claw": "pet", "Bite": "pet", "Summon Hawk": "hawk", "Aimed Shot": "aimed"}
NEW_SOURCES = {'volley': {'id': 'volley', 'share': 0.0, 'min_level': 40, 'tags': ['type:spell', 'school:arcane', 'aoe', 'ability:Volley'], 'cast': 6.0, 'min_cast': 6.0}, "hawk": {"id": "hawk", "share": 0.0, "min_level": 25, "tags": ["pet", "withpet", "ability:Summon Hawk", "school:physical"], "cooldown": 6},
               "aimed": {"id": "aimed", "share": 0.0, "min_level": 20, "tags": ["type:ranged", "yellow", "school:physical", "ability:Aimed Shot", "ability:Shots", "withpet"], "cooldown": 6}}
KEY_TALENTS = ["Unleashed Fury", "Bestial Wrath", "Ferocity"]
DESCRIPTION = ("Single-target leveling fights against normal mobs of your level with a cat: the pet runs in and meets the mob halfway, Growls every 5 s and holds it "
               "until your threat passes 130% of its own. You shoot from 35 yd: Hunter's Mark, Serpent Sting, Summon Hawk or Arcane Shot, Multi-Shot / Aimed Shot on their "
               "shared cooldown, Auto Shot in between (the bow cannot fire inside 8 yd); Bestial Wrath, Intimidation and Rapid Fire on the pull when ready; Mend Pet when "
               "the pet drops below 35%; Feign Death, Wing Clip and Raptor Strike when a mob reaches you. Between fights: 2 s loot, 6 s travel, Mend Pet below 70% pet "
               "health, water below 35% mana, food below 65% health, a 10 s Revive Pet after a pet death; a death costs 90 s.")
NOT_MODELLED = "runners, adds, the ranged hunter's traps (the pet holds the mob away from them), kiting (Concussive Shot / Wing Clip and running), Scatter Shot, Disengage, Volley, pet happiness and feeding, gear upgrades within a level bracket."
# rebuild.py: which scorer model, hand draft and optimizer build the pipeline calibrates, races and reports for this class
PIPELINE = {"variants": [{'spec': 'bm-leveling', 'opt': 'opt-bm-leveling-leveling-aoe', 'tag': 'aoe', 'profile': 'leveling-aoe', 'lookahead': 16, 'sets': ['MOBS_PER_PULL=3'], 'levels': '30,40,50,60', 'calibrate_levels': '40,60', 'label': 'AoE grinding, 3 mobs per pull'},
                          {'spec': 'melee-dps', 'opt': 'opt-melee-dps-leveling-st', 'tag': 'melee', 'profile': 'leveling-st', 'lookahead': 16, 'sets': [], 'levels': '20,30,40,50,60',
                           'calibrate_levels': '40,60', 'label': 'Melee hunter (dual wield, Survival)', 'report': 'melee-dps-opt', 'share_build': 'cand-melee-pet',
                           'seeds': ['leveling-melee']}], "spec": "bm-leveling", "hand": "leveling-beast-mastery", "opt": "opt-bm-leveling-leveling-st", "tag": "bm", "lookahead": 16,
            "levels": "20,30,40,50,60", "calibrate_levels": "30,60",
            "extra_reports": [{"spec": "mm-raid", "build": "opt-mm-raid-leveling-st", "compare": ["opt-bm-leveling-leveling-st"]},
                              {"spec": "melee-dps", "build": "leveling-melee", "compare": ["opt-bm-leveling-leveling-st", "opt-melee-dps-leveling-st"]}]}

PET = dict(strength=136, agility=100, stamina=274, intellect=50, spirit=80, dmg=(18.17, 27.66), speed=2.0, armor_per_level=50, hp_mult=0.98, dmg_family=1.10, happiness=1.25)


def pet_health(level):
    """Hunter pet base health by level (a Classic cat: ~250 at 10, ~1,000 at 30, ~3,000 at 60: 0.8 L^2 + 8 L + 100)."""
    return 0.8 * level * level + 8 * level + 100


def growl_threat(level):
    """Growl threat per cast (Classic ranks ~50 at 10 to ~415 at 60: 6.9 per level)."""
    return 6.9 * level


class HunterModule(BaseModule):
    resource = "mana"
    melee = True
    ranged = True
    special_stat = ("Pet deaths/100", "pet_deaths_per_100")

    AOE = {'channel': ['Volley'], 'direct': ['Multi-Shot'], 'dots': ['Serpent Sting'], 'min_near': 2}

    def __init__(self, talents, level, spec="bm-leveling", gear="leveling"):
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
        self.hawks = 0
        self.armor_spell_used = "Aspect of the Hawk" if "Aspect of the Hawk" in self.spells else "none"
        self._fix_traps()

    def _fix_traps(self):
        """The spellbook parser reads no periodic damage from the traps' wording ("burn the first enemy to approach for 690 Fire damage over
        15 sec", "and 330 additional Fire damage over 20 sec"): fill it in (2026-09-29). Immolation ticks every 3 s, Explosive every 2 s."""
        for name, every in (("Immolation Trap", 3.0), ("Explosive Trap", 2.0)):
            s = self.spells.get(name)
            if s is None or s.dot > 0:
                continue
            m = re.search(r"(\d+) (?:additional )?Fire damage over (\d+) sec", s.text)
            if m:
                dur = float(m.group(2))
                self.spells[name] = dataclasses.replace(s, dot=float(m.group(1)), dot_dur=dur, dot_ticks=max(1, int(round(dur / every))))

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

    # ------------------------------------------------------------ character and pet
    def make_player(self, level):
        base = class_base_stats("hunter", level)
        g = gear_stats(level, self.gear, "hunter")
        agility = (base["agility"] + g["agility"]) * (1 + self.tv("Lightning Reflexes", 0) / 100)
        strength = base["strength"] + g["strength"]
        intellect = base["intellect"] + g["intellect"]
        spirit = base["spirit"] + g["spirit"]
        stamina = base["stamina"] + g["stamina"]
        bm = class_base_mana("hunter", level)
        hawk = self.book.get("Aspect of the Hawk")
        tsa = self.book.get("Trueshot Aura") if self.rank("Trueshot Aura") else None
        rap = class_ranged_ap("hunter", level, agility) + (getattr(hawk, "rap", 0.0) if hawk else 0.0) + (getattr(tsa, "rap", 0.0) if tsa else 0.0)
        ap = class_attack_power("hunter", level, strength, agility)
        careful = intellect * self.tv("Careful Aim", 0) / 100
        p = Player(level=level, hp_max=(class_base_health("hunter", level) + 10 * stamina) * (1 + self.tv("Survivalist", 0) / 100), hp=0.0,
                   mana_max=bm + 15 * intellect, mana=0.0, base_mana=bm, spirit=spirit, intellect=intellect, spell_power=0.0, armor=g["armor"],
                   spell_crit=class_spell_crit("hunter", level, intellect), dodge=class_dodge("hunter", level, agility),
                   ranged_crit=class_melee_crit("hunter", level, agility) + self.tv("Lethal Attacks", 0) / 100)
        p.strength, p.agility, p.stamina = strength, agility, stamina
        p.attack_power, p.ranged_ap = ap + careful, rap + careful
        self.base_rap = p.ranged_ap
        p.melee_crit = class_melee_crit("hunter", level, agility) + self.tv("Lethal Attacks", 0) / 100
        p.hit_bonus = self.tv("Surefooted", 0) / 100
        p.parry = 0.05 + self.tv("Deflection", 0) / 100
        rdps = weapon_dps(level, "ranged")
        p.ranged = Weapon(dmg_min=rdps * WEAPON_SPEED["ranged"] * 0.8, dmg_max=rdps * WEAPON_SPEED["ranged"] * 1.2, speed=WEAPON_SPEED["ranged"], kind="ranged", dps_bonus=ammo_dps(level))
        if self.is_melee():   # a melee hunter dual-wields one-handers (Predator's Edge: +10%/rank off-hand damage) under Aspect of the Beast
            mdps = weapon_dps(level, "1h")
            p.mh = Weapon(dmg_min=mdps * WEAPON_SPEED["1h"] * 0.8, dmg_max=mdps * WEAPON_SPEED["1h"] * 1.2, speed=WEAPON_SPEED["1h"], kind="1h")
            oh = 1 + self.tv("Predator's Edge", 1, 0.0) / 100
            p.oh = Weapon(dmg_min=mdps * WEAPON_SPEED["1h"] * 0.8 * oh, dmg_max=mdps * WEAPON_SPEED["1h"] * 1.2 * oh, speed=WEAPON_SPEED["1h"], kind="1h")
            beast = self.book.get("Aspect of the Beast")
            p.attack_power += getattr(beast, "ap", 110.0 * level / 60.0) if beast else 110.0 * level / 60.0
        else:
            mdps = weapon_dps(level, "2h")
            p.mh = Weapon(dmg_min=mdps * WEAPON_SPEED["2h"] * 0.8, dmg_max=mdps * WEAPON_SPEED["2h"] * 1.2, speed=WEAPON_SPEED["2h"], kind="2h")
        p.hp, p.mana = p.hp_max, p.mana_max
        p.regen_while_casting = self.tv("Bestial Discipline", 1) / 100
        p.pet = None if self.rank("Lone Wolf") else self.make_pet(level)   # Lone Wolf: no pet, +20% on every attack of your own
        return p

    def make_pet(self, level):
        f = (level - 1) / 59.0
        stat = {k: 20 + (PET[k] - 20) * f for k in ("strength", "agility", "stamina", "intellect", "spirit")}
        et = 1 + self.tv("Endurance Training", 0) / 100
        hp = (pet_health(level) + 10 * stat["stamina"] * 0.5) * PET["hp_mult"] * et
        pet = Pet(name="Cat", hp_max=hp, hp=hp, armor=PET["armor_per_level"] * level * et,
                  dmg_min=PET["dmg"][0] * PET["speed"] * level / 60.0, dmg_max=PET["dmg"][1] * PET["speed"] * level / 60.0, speed=PET["speed"],
                  attack_power=max(0.0, 2 * stat["strength"] - 20), crit=0.05 + stat["agility"] * 0.05 / 100 + self.tv("Ferocity", 0) / 100,
                  focus=100.0, focus_max=100.0, focus_regen=5.0 * (1 + self.tv("Bestial Discipline", 0) / 100), threat_mult=1.0)
        pet.dmg_mult = PET["happiness"] * PET["dmg_family"] * (1 + self.tv("Unleashed Fury", 0) / 100) * (1 + self.tv("Focused Fire", 0) / 100)
        self.pet_base_speed = pet.speed
        return pet

    def pull_range(self):
        return 35.0 + self.tv("Hawk Eye", 0)

    # ------------------------------------------------------------ engine hooks: numbers
    def mana_cost(self, spell):
        cost = spell.cost
        if "cost_pct" in spell.tags:
            cost = cost / 100 * self._base_mana
        if spell.kind in ("ranged", "melee") or spell.name in ("Serpent Sting", "Scorpid Sting"):
            cost *= 1 - self.tv("Efficiency", 0) / 100
        if spell.kind == "melee" or spell.name in TRAPS:   # Resourcefulness: "Trap abilities and melee abilities"
            cost *= 1 - self.tv("Resourcefulness", 0) / 100
        if spell.name == "Mend Pet":
            cost *= 1 - self.tv("Improved Mend Pet", 1) / 100
        return cost

    def hit_bonus(self, spell):
        if spell.name in TRAPS:
            return self.tv("Survival Tactics", 0) / 100
        return 0.0

    def crit_bonus(self, spell, frozen):
        if spell.kind == "melee" and spell.name != "Melee":
            return self.tv("Savage Strikes", 0) / 100
        return 0.0

    def crit_damage_bonus(self, spell):
        if spell.kind == "ranged":
            return self.tv("Mortal Shots", 0) / 100
        if spell.kind == "melee":
            return self.tv("Predator's Edge", 0) / 100
        return 0.0

    def damage_multiplier(self, spell, frozen):
        m = (1 + self.tv("Focused Fire", 0) / 100) * (1 + self.tv("Improved Tracking", 0) / 100)
        if self.rank("Lone Wolf") and (self._fight is None or self._fight.p.pet is None):
            m *= 1 + self.tv("Lone Wolf", 0) / 100
        if spell.kind == "ranged" or spell.name == "Auto Shot":
            m *= 1 + self.tv("Ranged Weapon Specialization", 0) / 100
        if spell.name in ("Multi-Shot", "Aimed Shot"):
            m *= 1 + self.tv("Barrage", 0) / 100
        if spell.name == "Serpent Sting":
            m *= 1 + self.tv("Improved Stings", 0) / 100
        if spell.name in TRAPS:
            m *= 1 + self.tv("Clever Traps", 1) / 100
        return m

    def periodic_can_crit(self, spell):
        return False

    def swing_speed_factor(self):
        f = 1.0
        if self._fight:
            if self._fight.p.buff("Rapid Fire", self._fight.t):
                f /= 1.4
            if self._fight.p.buff("Deadly Aspects", self._fight.t):
                f /= 1.3
        return f

    def mana_regen(self, p, t):
        tick = class_mana_regen_tick("hunter", p.spirit)
        if p.buff("Rapid Recuperation", t) or p.buff("Resourcefulness", t):   # both let 50% of regen continue; the best one counts
            p.regen_while_casting = max(self.tv("Bestial Discipline", 1) / 100, 0.5)
        else:
            p.regen_while_casting = self.tv("Bestial Discipline", 1) / 100
        sb = self.tv("Spirit Bond", 0) / 100
        if sb and p.pet is not None and p.pet.alive:   # 1%/rank per 5 s for both, applied on the 2-s tick
            p.hp = min(p.hp_max, p.hp + p.hp_max * sb * 0.4)
            p.pet.hp = min(p.pet.hp_max, p.pet.hp + p.pet.hp_max * sb * 0.4)
        return tick

    def health_regen(self, p):
        return class_health_regen_tick("hunter", p.spirit)

    def resummon_time(self):
        return max(3.0, 10.0 - 3.0 * self.rank("Improved Revive Pet")) + 1.5

    def pet_threat_bonus(self, fight):
        return 0.0

    # ------------------------------------------------------------ pet
    def pet_decide(self, fight):
        p, m, t, pet = fight.p, fight.m, fight.t, fight.p.pet
        if pet.cooldowns.get("Growl", -1.0) <= t and (m.pet_in_melee or m.in_melee):
            return Spell("Growl", "physical", cooldown=5.0, kind="buff", dmg_min=growl_threat(self.level), resource="none")
        bite = self.spells.get("Bite")
        if bite is not None and pet.cooldowns.get("Bite", -1.0) <= t and pet.focus >= 35:
            return Spell("Bite", "physical", cost=35.0, cooldown=10.0, kind="melee", dmg_min=bite.dmg_min, dmg_max=bite.dmg_max, resource="focus")
        claw = self.spells.get("Claw")
        if claw is not None and pet.focus >= 25:
            return Spell("Claw", "physical", cost=25.0, cooldown=1.0, kind="melee", dmg_min=claw.dmg_min, dmg_max=claw.dmg_max, resource="focus")
        return None

    def on_pet_hit(self, fight, amount, crit):
        p, m, t, pet = fight.p, fight.m, fight.t, fight.p.pet
        if crit and self.rank("Frenzy") and fight.rng.random() < self.tv("Frenzy", 0) / 100:
            p.buffs["Frenzy"] = {"until": t + 8.0}
        pet.speed = self.pet_base_speed / (1.3 if p.buff("Frenzy", t) else 1.0)
        b = p.buff("Intimidation", t)
        if b and amount > 0:
            m.stun_until = max(m.stun_until, t + 3.0)
            del p.buffs["Intimidation"]
            fight.note("Intimidation stun")

    # ------------------------------------------------------------ engine hooks: events
    def on_fight_start(self, fight):
        self._fight = fight
        self._base_mana = fight.p.base_mana
        p, t = fight.p, fight.t
        self.hawks = 0
        p.ranged_ap = self.base_rap          # Hunter's Mark is on the mob: it is gone with the last one
        p.buffs.pop("Hunter's Mark", None)
        pet = p.pet
        if pet is not None:
            pet.speed = self.pet_base_speed
        bw = self.spells.get("Bestial Wrath")
        if bw is not None and p.ready("Bestial Wrath", t) and pet is not None and pet.alive and p.mana >= self.mana_cost(bw):
            p.mana -= self.mana_cost(bw)
            pet.dmg_mult *= 1.5
            p.buffs["Bestial Wrath"] = {"until": t + 18.0}
            p.cooldowns["Bestial Wrath"] = t + bw.cooldown
            fight.casts["Bestial Wrath"] = fight.casts.get("Bestial Wrath", 0) + 1
        rf = self.spells.get("Rapid Fire")
        if rf is not None and p.ready("Rapid Fire", t) and p.mana >= rf.cost:
            p.mana -= rf.cost
            p.buffs["Rapid Fire"] = {"until": t + 15.0}
            p.cooldowns["Rapid Fire"] = t + max(60.0, rf.cooldown - 60.0 * self.rank("Rapid Killing"))
        im = self.spells.get("Intimidation")
        if im is not None and p.ready("Intimidation", t) and pet is not None and pet.alive and p.mana >= self.mana_cost(im):
            p.mana -= self.mana_cost(im)
            p.buffs["Intimidation"] = {"until": t + 15.0}
            p.cooldowns["Intimidation"] = t + im.cooldown

    def dodge_bonus(self, fight):
        return 0.25 if fight.p.buff("Deterrence", fight.t) else 0.0

    def parry_bonus(self, fight):
        return 0.25 if fight.p.buff("Deterrence", fight.t) else 0.0

    def on_hit(self, fight, spell, amount, crit, frozen):
        p, m, t = fight.p, fight.m, fight.t
        if spell.name == "Deterrence":
            p.buffs["Deterrence"] = {"until": t + 10.0}
        if crit and self.rank("Resourcefulness") and fight.rng.random() < self.tv("Resourcefulness", 1) / 100:
            p.buffs["Resourcefulness"] = {"until": t + 30.0}
        if self.is_melee() and spell.kind == "melee" and spell.name != "Melee" and amount > 0:
            if self.rank("Expose Prey") and p.buff("Hunter's Mark", t) and fight.rng.random() < self.tv("Expose Prey", 0) / 100:
                p.buffs["Mongoose"] = {"until": t + 5.0}
            if spell.name == "Mongoose Bite" and self.rank("Lacerating Strikes"):
                fight.refresh_dot("Lacerate", amount * 0.40, 7, 3.0)
        if spell.name == "Hunter's Mark":
            p.ranged_ap = self.base_rap + getattr(spell, "rap", 0.0)
            p.buffs["Hunter's Mark"] = {"until": t + 120.0}
        if spell.name == "Feign Death":
            m.threat_player = 0.0
            if p.pet is not None and p.pet.alive and p.pet.engaged:
                m.target = "pet"
                m.pet_in_melee = True
                m.in_melee = False
                fight.note("Feign Death: the mob goes back to the pet")
        if spell.name == "Summon Hawk" and amount > 0:
            self.hawks += 1
            per = (spell.dmg_min + 0.05 * p.ranged_ap) * (1 + self.tv("Unleashed Fury", 0) / 100) * (1 - 0.35)
            fight.refresh_dot(f"Summon Hawk {self.hawks % 2 + 1}", per * 6, 6, 3.0, self.spells["Summon Hawk"].rank and (0.05 + self.tv("Ferocity", 0) / 100), 2.0)
        if spell.name == "Serpent Sting" and self.rank("Rapid Recuperation"):
            p.buffs["Rapid Recuperation"] = {"until": t + 15.0}
        if spell.name == "Concussive Shot" and self.rank("Improved Concussive Shot") and fight.rng.random() < self.tv("Improved Concussive Shot", 0) / 100:
            m.stun_until = max(m.stun_until, t + 3.0)
        if spell.name == "Wing Clip" and self.rank("Improved Wing Clip") and fight.rng.random() < self.tv("Improved Wing Clip", 0) / 100:
            m.root_until = max(m.root_until, t + 5.0)

    def is_melee(self):
        return self.spec == "melee-dps"

    def on_parry(self, fight):
        if "Counterattack" in self.spells:
            fight.p.buffs["Counterattack"] = {"until": fight.t + 5.0}

    def decide_melee(self, fight):
        """The melee hunter: mark and sting from range, then stand and fight: Counterattack after a parry, Mongoose Bite when a dodge or
        Expose Prey activates it, Strider Kick on cooldown, Raptor Strike on the next swing; Deterrence when low; Mend Pet for the pet."""
        p, m, t, pet = fight.p, fight.m, fight.t, fight.p.pet
        sp = self.spells
        if m.pet_in_melee and not m.in_melee:   # the pet holds the mob: the hunter closes in and fights beside it
            m.in_melee, m.dist = True, min(m.dist, MELEE_RANGE)
        in_melee = m.in_melee and m.dist <= MELEE_RANGE + 0.5

        def can(s):
            return s is not None and p.ready(s.name, t) and fight.can_afford(s, self.mana_cost(s))

        mark, sting, raptor, mongoose, counter, kick, deter, mend = (sp.get(n) for n in ("Hunter's Mark", "Serpent Sting", "Raptor Strike", "Mongoose Bite", "Counterattack", "Strider Kick", "Deterrence", "Mend Pet"))
        trap = sp.get("Immolation Trap")
        hp = m.hp
        if mend and can(mend) and pet is not None and pet.alive and pet.hp < 0.35 * pet.hp_max and m.target == "pet":
            return mend
        if not in_melee:
            if m.dist >= 8.0:
                if mark and can(mark) and not p.buff("Hunter's Mark", t) and hp > 0.3 * m.hp_max:
                    return mark
                if sting and can(sting) and not fight.dot_active("Serpent Sting") and hp > 0.4 * m.hp_max:
                    return sting
            return None   # wait for the mob to come
        if deter and can(deter) and p.hp < 0.4 * p.hp_max and hp > 0.3 * m.hp_max:
            return deter
        if counter and can(counter) and p.buff("Counterattack", t):
            return counter
        if mongoose and can(mongoose) and p.buff("Mongoose", t):
            return mongoose
        if kick and can(kick):
            return kick
        # Immolation Trap under the mob while it has health for the 15 s burn (2026-09-29: traps work in combat; the raid rotation's
        # last line, here before the Raptor Strike queue, which is off the GCD)
        if trap and can(trap) and hp > 0.4 * m.hp_max and not fight.dot_active("Immolation Trap"):
            return trap
        if raptor and can(raptor) and fight.queued_swing is None:
            return raptor
        return None

    def on_swing(self, fight, spell, outcome, amount, hand):
        p, t = fight.p, fight.t
        if self.is_melee() and spell.name == "Melee" and outcome not in ("miss", "dodge", "parry"):
            if self.rank("Deadly Aspects") and fight.rng.random() < self.tv("Deadly Aspects", 0) / 100:
                p.buffs["Deadly Aspects"] = {"until": t + 12.0}
            if self.rank("Expose Prey") and p.buff("Hunter's Mark", t) and fight.rng.random() < self.tv("Expose Prey", 0) / 100:
                p.buffs["Mongoose"] = {"until": t + 5.0}
        if spell.name == "Auto Shot" and outcome not in ("miss", "dodge", "parry") and self.rank("Deadly Aspects") and fight.rng.random() < self.tv("Deadly Aspects", 0) / 100:
            p.buffs["Deadly Aspects"] = {"until": t + 12.0}

    def on_dodge(self, fight):
        fight.p.buffs["Mongoose"] = {"until": fight.t + 5.0}

    def after_cast(self, fight, spell):
        p, t = fight.p, fight.t
        cd = spell.cooldown
        if spell.name == "Arcane Shot":
            cd = max(GCD, cd - 0.3 * self.rank("Improved Arcane Shot"))
        if spell.name == "Deterrence" or spell.name in TRAPS:
            cd *= 1 - self.tv("Survivalist's Discipline", 0) / 100
        if cd > 0:
            p.cooldowns[spell.name] = t + cd
            for other in SHARED_CD.get(spell.name, ()):
                p.cooldowns[other] = max(p.cooldowns.get(other, 0.0), t + (cd if spell.name in TRAPS else spell.cooldown))
        if spell.name == "Bestial Wrath":
            pass

    def on_kill(self, fight):
        p = fight.p
        if p.buff("Bestial Wrath", fight.t) is None and p.pet is not None:
            pass

    def _expire_wrath(self, fight):
        p, t = fight.p, fight.t
        b = p.buffs.get("Bestial Wrath")
        if b is not None and b["until"] <= t and p.pet is not None:
            p.pet.dmg_mult /= 1.5
            del p.buffs["Bestial Wrath"]

    def after_fight(self, p, t):
        """Mend Pet (5 s channel) when the pet is below 70%; the Bestial Wrath multiplier is undone if it ran out mid-fight."""
        b = p.buffs.get("Bestial Wrath")
        if b is not None and p.pet is not None:
            p.pet.dmg_mult /= 1.5
            del p.buffs["Bestial Wrath"]
        if p.pet is not None:
            p.pet.speed = self.pet_base_speed
        spent = 0.0
        mend = self.spells.get("Mend Pet")
        pet = p.pet
        if mend is not None and pet is not None and pet.alive and pet.hp < 0.5 * pet.hp_max and p.mana >= self.mana_cost(mend):
            p.mana -= self.mana_cost(mend)   # one channel; the pet regenerates the rest on the way to the next mob
            pet.hp = min(pet.hp_max, pet.hp + mend.hot)
            spent += mend.channel
        return spent

    # ------------------------------------------------------------ priority list
    def decide(self, fight):
        if fight.others():   # a pull of several mobs: the area priority first (engine.BaseModule.decide_aoe, AOE below)
            r = self.decide_aoe(fight)
            if r is not None:
                return r
        if self.is_melee():
            return self.decide_melee(fight)
        p, m, t, pet = fight.p, fight.m, fight.t, fight.p.pet
        sp = self.spells
        self._expire_wrath(fight)
        on_me = m.target == "player" or pet is None or not pet.alive
        in_melee = m.in_melee and m.dist <= MELEE_RANGE + 0.5
        at_range = m.dist >= 8.0

        def can(s):
            return s is not None and p.ready(s.name, t) and fight.can_afford(s, self.mana_cost(s))

        mark, sting, arcane, hawk, multi, aimed, conc, mend, fd, clip, raptor, mongoose = (sp.get(n) for n in ("Hunter's Mark", "Serpent Sting", "Arcane Shot", "Summon Hawk", "Multi-Shot", "Aimed Shot", "Concussive Shot", "Mend Pet", "Feign Death", "Wing Clip", "Raptor Strike", "Mongoose Bite"))
        hp = m.hp
        # a mob on me: Feign Death sends it back to the pet; otherwise melee it (Wing Clip, Raptor Strike, Mongoose Bite after a dodge)
        if on_me and pet is not None and pet.alive and fd and can(fd) and (in_melee or m.dist < 10):
            return fd
        if not on_me and m.dist < 8.0 and pet is not None and pet.alive and m.target == "pet":
            return "retreat"   # the pet has the mob: step back out of the dead zone and shoot
        if in_melee:
            if mongoose and can(mongoose) and p.buff("Mongoose", t):
                return mongoose
            if raptor and can(raptor) and fight.queued_swing is None:
                return raptor
            if clip and can(clip) and not (m.slow_until > t) and hp > 0.15 * m.hp_max:
                return clip
            return None
        if not at_range:
            return None
        # pet care
        if mend and can(mend) and pet is not None and pet.alive and pet.hp < 0.35 * pet.hp_max and m.target == "pet":
            return mend
        # shots
        if mark and can(mark) and not p.buff("Hunter's Mark", t) and hp > 0.3 * m.hp_max:
            return mark
        if arcane and can(arcane) and hp <= arcane.dmg_max * self.damage_multiplier(arcane, False):
            return arcane
        if sting and can(sting) and not fight.dot_active("Serpent Sting") and hp > 0.4 * m.hp_max:
            return sting
        if hawk and can(hawk) and hp > 0.3 * m.hp_max:
            return hawk
        if arcane and can(arcane):
            return arcane
        if multi and can(multi):
            return multi
        if aimed and can(aimed) and hp > 0.25 * m.hp_max:
            return aimed
        return None
