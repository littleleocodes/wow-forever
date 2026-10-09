"""Hunter module for the fight lab (Beast Mastery leveling with a cat).

Spell ranks are read from `_reference/data/forever-spells/hunter.json` (beta client build 1.60.1.70291); talent numbers from
each rank's tooltip in `_reference/data/forever-talents/hunter.json`. Pet stats: the level-60 hunter pet of the
ElliotWood/Forever simulator (`sim/hunter/pet.go`; cat family x1.10 damage, happiness x1.25), scaled by level here, plus what it
inherits from the hunter since 2026-10-08 (`make_pet`); Claw/Bite from the beta spellbook; Summon Hawk as the raid simulator
models it since its fit to beta combat logs (`summon_hawk`: the dive bomb, then a swing on arrival and every 2.5 s for 18 s).

Playstyle `bm-leveling` (the scorer's model id): the cat runs in and Growls, the hunter shoots from 35 yd: Hunter's Mark,
Serpent Sting, Summon Hawk or Arcane Shot, Multi-Shot / Aimed Shot on their shared cooldown, Auto Shot in between; Bestial
Wrath, Intimidation and Rapid Fire on the pull when ready; Mend Pet when the pet drops low; Feign Death, Wing Clip and
Raptor Strike when a mob reaches the hunter. Between fights: Mend Pet, food and water.
"""
import json
import pathlib
import dataclasses
import re

import tables
from engine import parse_interrupt, BaseModule, Pet, Player, Spell, Weapon
from tables import (GCD, MELEE_RANGE, WEAPON_SPEED, ammo_dps, armor_mitigation, class_attack_power, class_base_health, class_base_mana,
                    class_base_stats, class_dodge, class_health_regen_tick, class_mana_regen_tick, class_melee_crit, class_ranged_ap,
                    class_spell_crit, gear_stats, weapon_dps)

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
# Summon Hawk since build 70205: "dealing 108 plus 5% of your Ranged Attack Power Physical damage and continuing its assault for 18 sec.
# Only 2 hawks can be active at once." (70205 read "of ranged attack power"; before it "dealing 108 Physical damage", which FLAT reads).
# The generic FLAT pattern cannot read the new wording, so from the 70291 refresh (2026-10-08) to 2026-10-09 the lab's hawk did nothing.
HAWK = re.compile(r"dealing (\d[\d,]*) plus (\d+(?:\.\d+)?)% of (?:your )?ranged attack power", re.I)
HAWK_LIFE = re.compile(r"continuing its assault for (\d+) sec")
HAWK_CAP = re.compile(r"Only (\d+) hawks? can be active at once")
DODGE = re.compile(r"chance to dodge by (\d+(?:\.\d+)?)%")   # Aspect of the Monkey (Forever: 8%)
# A Summon Hawk rank whose wording no pattern reads (a later rewording) keeps these instead of 0: the dive bomb's base by rank and its
# ranged attack power share, from the 70291 tooltips (the raid simulator's spell data has the same numbers, sim/hunter/summon_hawk.go).
HAWK_BASE_FALLBACK = {1: 32.0, 2: 47.0, 3: 85.0, 4: 108.0}
HAWK_RAP_FALLBACK = 0.05
HAWK_LIFE_FALLBACK, HAWK_CAP_FALLBACK = 18.0, 2
# The hawk that stays after the dive bomb, as the raid simulator fits it to beta combat logs (foreverlogs reports 2695 and 2701, two
# level 25/30 hunters, 534 landed swings at rank 1; sim/hunter/summon_hawk.go): a swing on arrival, then one every 2.5 s sped up by the
# hunter's ranged haste, each about 0.35 of the rank's dive bomb base (compared target by target with the dive bomb, so armor applies the
# same way); the swings do not crit. Until 2026-10-09 the lab used an older reading: the whole dive bomb, less 35%, every 3 s.
HAWK_SWING_SHARE = 0.35
HAWK_SWING_EVERY = 2.5
WHITE = ("Melee", "Melee (off-hand)")   # the melee auto attacks: no ability modifiers (Savage Strikes, Predator's Edge's crit damage)
HAWK_SWING = Spell("Summon Hawk", "physical", kind="melee", resource="none")   # the hawk's swings, booked under the spell's name

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
                    if name == "Summon Hawk":   # the dive bomb: the rank's base plus a share of ranged attack power (resolve_attack adds coef x RAP)
                        hm, lm, cm = HAWK.search(txt), HAWK_LIFE.search(txt), HAWK_CAP.search(txt)
                        if hm:
                            base, share = _num(hm.group(1)), float(hm.group(2)) / 100
                        elif fl and fl.group(4):   # the wording before 70291: "dealing 108 Physical damage"
                            base, share = _num(fl.group(4)), HAWK_RAP_FALLBACK
                        else:
                            base, share = HAWK_BASE_FALLBACK.get(s.rank, 0.0), HAWK_RAP_FALLBACK
                        s.dmg_min = s.dmg_max = base
                        s.coef = share
                        s.hawk_life = float(lm.group(1)) if lm else HAWK_LIFE_FALLBACK
                        s.hawk_cap = int(cm.group(1)) if cm else HAWK_CAP_FALLBACK
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
    "Deadly Aspects": ("2%/rank per landed Auto Shot under Aspect of the Hawk (the ranged builds), or per landed melee auto attack, main and off "
                       "hand, under Aspect of the Beast (the melee builds, from level 30): +30% attack speed for 12s"),
    "Endurance Training": "+3%/rank pet health and armor",
    "Focused Fire": "+1%/rank damage for you and the pet while the pet is alive",
    "Improved Aspect of the Monkey": ("+2%/rank dodge on Aspect of the Monkey, the melee builds' aspect below level 30 (its dodges light up "
                                      "Mongoose Bite); the ranged builds keep Aspect of the Hawk up"),
    "Pathfinding": "travel speed only",
    "Improved Revive Pet": "-3s/rank Revive Pet",
    "Bestial Swiftness": "+30% pet speed: the pet reaches the mob sooner",
    "Unleashed Fury": "+3%/rank pet and hawk damage",
    "Improved Mend Pet": "-10%/rank Mend Pet mana",
    "Ferocity": "+2%/rank pet and hawk crit",
    "Summon Hawk": ("unlocks Summon Hawk: a dive bomb (the rank's base + 5% of ranged attack power; Ferocity's crit and Unleashed Fury apply), "
                    "then a hawk that swings on arrival and every 2.5 s (ranged haste) for 18 s at 0.35 of the base, no crits; 2 hawks at once, "
                    "a new one replaces the one closest to leaving; shares Arcane Shot's cooldown; the ranged list casts it (the melee list "
                    "leaves it out: it measured a net loss there, its mana)"),
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
    "Savage Strikes": "+2%/rank crit on melee abilities (the client's class mask: abilities only, no auto attacks)",
    "Survivalist": "+2%/rank health",
    "Surefooted": "+1%/rank hit",
    "Lightning Reflexes": "+3%/rank Agility",
    "Predator's Edge": ("+6%/rank crit damage on melee abilities and +10%/rank off-hand weapon damage (the client's class mask, as the raid "
                        "simulator reads it: no auto attacks)"),
    "Expose Prey": ("5%/rank per landed melee or ranged attack of yours on a target with your Hunter's Mark: Mongoose Bite usable for 10 s "
                    "(a dodge opens it for 5 s); the melee list marks the mob in a free global cooldown when the build has the talent "
                    "(the tuned rules veto the mark: it measured slower per kill even with Expose Prey)"),
    "Lacerating Strikes": "Mongoose Bite adds a bleed of 40% of its damage over 21 s",
    "Strider Kick": "unlocks Strider Kick (a weapon hit, 8 s cooldown), cast on cooldown by the melee list",
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
        # the aspect: the ranged builds keep Aspect of the Hawk up; the melee builds Aspect of the Beast from level 30 and Aspect of the Monkey
        # before it (2026-10-09: the lab had given them the Beast's attack power at every level and Aspect of the Hawk's ranged attack power)
        self.monkey_dodge = 0.0
        if not self.is_melee():
            self.armor_spell_used = "Aspect of the Hawk" if "Aspect of the Hawk" in self.spells else "none"
        elif self.beast_known():
            self.armor_spell_used = "Aspect of the Beast"
        elif "Aspect of the Monkey" in self.spells:
            self.armor_spell_used = "Aspect of the Monkey"
            dm = DODGE.search(getattr(self.spells["Aspect of the Monkey"], "text", ""))
            self.monkey_dodge = ((float(dm.group(1)) if dm else 8.0) + self.tv("Improved Aspect of the Monkey", 0)) / 100
        else:
            self.armor_spell_used = "none"
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

    def beast_known(self):
        """Aspect of the Beast is trained at level 30: the melee builds' aspect from then on."""
        return self.book.get("Aspect of the Beast") is not None

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
        hawk = None if self.is_melee() else self.book.get("Aspect of the Hawk")   # the melee builds run Aspect of the Beast / Monkey instead
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
            beast = self.book.get("Aspect of the Beast")   # rank by level: +50/70/90/110 melee attack power from 30/40/50/60; none before 30
            p.attack_power += getattr(beast, "map", 0.0) if beast is not None else 0.0
        else:
            mdps = weapon_dps(level, "2h")
            p.mh = Weapon(dmg_min=mdps * WEAPON_SPEED["2h"] * 0.8, dmg_max=mdps * WEAPON_SPEED["2h"] * 1.2, speed=WEAPON_SPEED["2h"], kind="2h")
        p.hp, p.mana = p.hp_max, p.mana_max
        p.regen_while_casting = self.tv("Bestial Discipline", 1) / 100
        p.pet = None if self.rank("Lone Wolf") else self.make_pet(level, p)   # Lone Wolf: no pet, +20% on every attack of your own
        return p

    def make_pet(self, level, p=None):
        """The cat. Since 2026-10-08 it inherits from the hunter (`tables.PET_SCALING`: 10% of the higher attack power, the crit chance,
        30% of the armor, 2 health per Stamina) and swings every `tables.HUNTER_PET_SPEED` seconds with the 2.0 s base hit (Forever does not
        normalize pet damage by attack speed)."""
        f = (level - 1) / 59.0
        stat = {k: 20 + (PET[k] - 20) * f for k in ("strength", "agility", "stamina", "intellect", "spirit")}
        et = 1 + self.tv("Endurance Training", 0) / 100
        k = tables.PET_SCALING if p is not None else 0.0
        own_ap = max(p.attack_power, p.ranged_ap) if p is not None else 0.0
        hp = (pet_health(level) + 10 * stat["stamina"] * 0.5 + k * 2 * (p.stamina if p is not None else 0.0)) * PET["hp_mult"] * et
        pet = Pet(name="Cat", hp_max=hp, hp=hp, armor=(PET["armor_per_level"] * level + k * 0.30 * (p.armor if p is not None else 0.0)) * et,
                  dmg_min=PET["dmg"][0] * PET["speed"] * level / 60.0, dmg_max=PET["dmg"][1] * PET["speed"] * level / 60.0, speed=tables.HUNTER_PET_SPEED,
                  attack_power=max(0.0, 2 * stat["strength"] - 20) + k * 0.10 * own_ap,
                  crit=0.05 + stat["agility"] * 0.05 / 100 + self.tv("Ferocity", 0) / 100 + k * (p.melee_crit if p is not None else 0.0),
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
        if spell.kind == "melee" and spell.name not in WHITE:   # 2026-10-09: the off-hand auto attack had taken Savage Strikes too
            return self.tv("Savage Strikes", 0) / 100
        if spell.name == "Summon Hawk":   # "pets and hawks": the dive bomb (the hawk's swings do not crit)
            return self.tv("Ferocity", 0) / 100
        return 0.0

    def crit_damage_bonus(self, spell):
        if spell.name == "Summon Hawk":   # the hawk is no ranged weapon attack: no Mortal Shots (the raid simulator's class masks)
            return 0.0
        if spell.kind == "ranged":
            return self.tv("Mortal Shots", 0) / 100
        if spell.kind == "melee" and spell.name not in WHITE:   # 2026-10-09: abilities only, as the client's class mask (it had applied to every auto attack)
            return self.tv("Predator's Edge", 0) / 100
        return 0.0

    def damage_multiplier(self, spell, frozen):
        m = 1 + self.tv("Improved Tracking", 0) / 100
        pet = self._fight.p.pet if self._fight is not None else None
        if pet is not None and pet.alive:   # Focused Fire: "while your pet is active" (2026-10-09: it had counted with no pet out too)
            m *= 1 + self.tv("Focused Fire", 0) / 100
        if self.rank("Lone Wolf") and (self._fight is None or self._fight.p.pet is None):
            m *= 1 + self.tv("Lone Wolf", 0) / 100
        if spell.name == "Summon Hawk":   # the dive bomb and the hawk's swings: Unleashed Fury ("pets and hawks"), no Ranged Weapon Specialization
            return m * (1 + self.tv("Unleashed Fury", 0) / 100)
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

    def ranged_haste(self):
        """The hunter's ranged attack speed factor (the hawk's swings follow it): Rapid Fire, and Deadly Aspects' Aspect of the Hawk half."""
        f = 1.0
        if self._fight:
            p, t = self._fight.p, self._fight.t
            if p.buff("Rapid Fire", t):
                f *= 1.4
            if p.buff("Deadly Aspects", t) and not self.is_melee():
                f *= 1.3
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
        return (0.25 if fight.p.buff("Deterrence", fight.t) else 0.0) + self.monkey_dodge   # Aspect of the Monkey: the melee builds below 30

    def parry_bonus(self, fight):
        return 0.25 if fight.p.buff("Deterrence", fight.t) else 0.0

    def on_hit(self, fight, spell, amount, crit, frozen):
        p, m, t = fight.p, fight.m, fight.t
        if spell.name == "Deterrence":
            p.buffs["Deterrence"] = {"until": t + 10.0}
        if crit and self.rank("Resourcefulness") and fight.rng.random() < self.tv("Resourcefulness", 1) / 100:
            p.buffs["Resourcefulness"] = {"until": t + 30.0}
        # Expose Prey on your landed abilities (the auto attacks and Auto Shot roll in on_swing); not the hawk's dive bomb
        if self.is_melee() and amount > 0 and spell.kind in ("melee", "ranged") and spell.name not in WHITE + ("Auto Shot", "Summon Hawk"):
            self.expose_prey(fight)
        if self.is_melee() and spell.name == "Mongoose Bite" and amount > 0 and self.rank("Lacerating Strikes"):
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
            self.summon_hawk(fight, spell)
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

    def light_mongoose(self, fight, seconds):
        """Mongoose Bite becomes usable for `seconds` (a dodge: 5 s; Expose Prey: its tooltip's 10 s); a shorter window never cuts a longer one."""
        b = fight.p.buffs.get("Mongoose")
        until = fight.t + seconds
        if b is None or b.get("until", 0.0) < until:
            fight.p.buffs["Mongoose"] = {"until": until}

    def expose_prey(self, fight):
        """Expose Prey: "Your attacks against targets with Hunter's Mark have a 10% chance to activate your Mongoose Bite for 10 sec" (the
        deep dive: melee and ranged attacks on the target of your Hunter's Mark). One roll per landed attack of the hunter's own."""
        p, t = fight.p, fight.t
        if self.rank("Expose Prey") and p.buff("Hunter's Mark", t) and fight.rng.random() < self.tv("Expose Prey", 0) / 100:
            self.light_mongoose(fight, self.tv("Expose Prey", 1) or 10.0)

    def summon_hawk(self, fight, spell):
        """The hawk that stays after a landed dive bomb (HAWK_SWING_* above): a swing on arrival, then one every 2.5 s divided by the
        ranged haste for the hawk's life (the tooltip's 18 s); a cast past the cap (2) replaces the hawk closest to leaving. Each swing:
        0.35 of the rank's dive bomb base with the hawk's multipliers (Unleashed Fury, Focused Fire with a living pet, Improved Tracking,
        Lone Wolf without one), the target's armor as for the dive bomb, the melee miss chance as an average; no crits. The damage counts
        as the hunter's threat, as a periodic effect does in this engine."""
        p, m = fight.p, fight.m
        swing = (HAWK_SWING_SHARE * spell.dmg_min * self.damage_multiplier(HAWK_SWING, False)
                 * (1.0 - armor_mitigation(m.effective_armor(), p.level)) * (1.0 - tables.MELEE_MISS))
        if swing <= 0:
            return
        every = HAWK_SWING_EVERY / self.ranged_haste()
        ticks = max(1, int(getattr(spell, "hawk_life", HAWK_LIFE_FALLBACK) / every))
        cap = getattr(spell, "hawk_cap", HAWK_CAP_FALLBACK)
        hawks = [d for d in m.dots if d[0] == "Summon Hawk"]
        if len(hawks) >= cap:
            m.dots.remove(min(hawks, key=lambda d: d[2]))
        fight.deal(HAWK_SWING, swing)   # the arrival swing
        fight.add_dot("Summon Hawk", swing * ticks, ticks, every)
        fight.note(f"hawk out ({min(len(hawks) + 1, cap)} up), {swing:.0f} a swing")

    def decide_melee(self, fight):
        """The melee hunter: Serpent Sting from range, then stand and fight beside the pet: Raptor Strike queued on the next swing whenever
        it is ready, Deterrence when low, Counterattack after a parry, Mongoose Bite when a dodge or Expose Prey activates it, Strider Kick on
        cooldown, Immolation Trap at your feet, then (with Expose Prey) Hunter's Mark in a free global cooldown; Mend Pet for the pet."""
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
            # only the sting at range (8-35 yd): a second global cooldown here delays the walk in (2026-10-09: the mark cast first had
            # cost the sting whenever the pet met the mob within a global cooldown, which is why the tuned rules vetoed the mark)
            if m.dist >= 8.0 and sting and can(sting) and not fight.dot_active("Serpent Sting") and hp > 0.4 * m.hp_max:
                return sting
            return None   # wait for the mob to come
        # Raptor Strike first: it costs no global cooldown (it replaces the next main-hand swing), but this engine asks for a decision only
        # when the global cooldown is free, so a queue left behind a global-cooldown spell waited 1.5 s and could miss a swing (2026-10-09)
        if raptor and can(raptor) and fight.queued_swing is None:
            return raptor
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
        # 2026-10-09: Hunter's Mark (no minimum range) in a global cooldown the strikes leave free, when the build has Expose Prey (the
        # mark's only use for a melee hunter). The tuned rules still veto it: with Expose Prey working the mark measured 0.5-1.3% slower
        # per kill (level-weighted, 1,000 fights). No Summon Hawk line, unlike the raid list: tried the same day (on its timer while the mob
        # had 30% health or more), it cost the Beast-Survival build 5.6% per kill at 60 (26.4 against 25.0 s; its 190 mana a cast, no
        # mana talent pays for it) and still 0.6% when cast only above 80% mana.
        if self.rank("Expose Prey") and mark and can(mark) and not p.buff("Hunter's Mark", t) and hp > 0.3 * m.hp_max:
            return mark
        return None

    def on_swing(self, fight, spell, outcome, amount, hand):
        """Auto attacks and Auto Shot. Deadly Aspects follows the aspect: melee auto attacks, both hands, under Aspect of the Beast (the melee
        builds from 30); Auto Shot under Aspect of the Hawk (the ranged builds). 2026-10-09: the melee half had ignored the off hand and
        counted below level 30, and a melee build's Auto Shot had rolled the Hawk half."""
        p, t = fight.p, fight.t
        if outcome in ("miss", "dodge", "parry"):
            return
        da = self.rank("Deadly Aspects")
        if self.is_melee():
            if spell.name in WHITE:
                if da and self.beast_known() and fight.rng.random() < self.tv("Deadly Aspects", 0) / 100:
                    p.buffs["Deadly Aspects"] = {"until": t + 12.0}
                self.expose_prey(fight)
            elif spell.name == "Auto Shot":
                self.expose_prey(fight)
        elif spell.name == "Auto Shot" and da and fight.rng.random() < self.tv("Deadly Aspects", 0) / 100:
            p.buffs["Deadly Aspects"] = {"until": t + 12.0}

    def on_dodge(self, fight):
        self.light_mongoose(fight, 5.0)

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
