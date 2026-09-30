"""Warlock module for the fight lab (Affliction leveling with a Voidwalker).

Spell ranks are read from `_reference/data/forever-spells/warlock.json` (beta client build 1.60.1.70009); talent numbers from
each rank's tooltip in `_reference/data/forever-talents/warlock.json`. Pet stats: level-60 demons from the ElliotWood/Forever
simulator (`sim/warlock/pets.go`: Forever demons inherit nothing from the warlock), scaled down by level here.

Playstyle `affliction-leveling` (the scorer's model id): the Voidwalker runs in and holds the mob with Torment; the warlock
puts Corruption, Bane of Agony, Siphon Life (talent) and Immolate on it, channels Wrack (talent) once the DoTs are up, fills
with Shadow Bolt while mana is plentiful and the wand otherwise, Drain Lifes when hurt, Life Taps when low on mana, Fears or
Death Coils a mob that reaches him. Between fights: Life Tap back to 70% mana, Consume Shadows / Health Funnel for the
Voidwalker, food only below 35% health (Drain Life on the next mob does the rest).
"""
import json
import pathlib
import re

from engine import parse_interrupt, BaseModule, Pet, Player, Spell
from tables import (GCD, MELEE_RANGE, WAND_SPEED, class_base_health, class_base_mana, class_base_stats, class_health_regen_tick,
                    class_mana_regen_tick, class_spell_crit, gear_stats, interp, wand_dps)

ROOT = pathlib.Path(__file__).resolve().parents[3]
SPELLBOOK = json.load(open(ROOT / "_reference/data/forever-spells/warlock.json", encoding="utf-8"))
TREE = json.load(open(ROOT / "_reference/data/forever-talents/warlock.json", encoding="utf-8"))

NUM = re.compile(r"(\d+(?:\.\d+)?)")
DMG = re.compile(r"(\d[\d,]*) to (\d[\d,]*) (\w+) damage")
FLAT = re.compile(r"caus(?:es|ing) (\d[\d,]*) (\w+) damage(?! over)")
DOT = re.compile(r"caus(?:es|ing) (\d[\d,]*) (\w+) damage over (\d+) sec")
BURN = re.compile(r"additional (\d[\d,]*) (\w+) damage over (\d+) sec")
FIRST = re.compile(r"Burns the enemy for (\d[\d,]*) Fire damage")
DRAIN = re.compile(r"Transfers (\d[\d,]*) health every (\d+) sec(?:ond)? from the target to the caster\. Lasts (\d+) sec")
SIPHON = re.compile(r"Transfers (\d[\d,]*) health from the target to the caster every (\d+) sec\. Lasts (\d+) sec")
TICK = re.compile(r"dealing (\d[\d,]*) (\w+) damage every (\d+) sec.*?Lasts (\d+) sec")
RAIN = re.compile(r"for (\d[\d,]*) (\w+) damage over (\d+) sec")                                             # Rain of Fire (a channel)
HELLFIRE = re.compile(r"(\d[\d,]*) (\w+) damage to all nearby enemies every (\d+) sec\. Lasts (\d+) sec")   # Hellfire (a channel)
FUNNEL = re.compile(r"Gives (\d[\d,]*) health to the caster's pet every second for (\d+) sec")
TAP = re.compile(r"Converts (\d[\d,]*) Health into (\d[\d,]*) Mana")
ABSORB = re.compile(r"absorb (\d[\d,]*) damage|Absorbs (\d[\d,]*) shadow damage")
ARMOR = re.compile(r"increasing armor by (\d[\d,]*)")
FEAR = re.compile(r"run in (?:fear|horror|terror)[^0-9]*?(\d+) sec|flee in terror for (\d+) sec")
CONSUME = re.compile(r"recovering (\d[\d,]*) health over (\d+) sec")
STONE = re.compile(r"instantly restore (\d[\d,]*) health")
COEF = re.compile(r"([\d.]+)% of spell power \((\w+(?: \w+)?)\)")

TALENT_SPELLS = {"Siphon Life": "Siphon Life", "Wrack": "Wrack", "Amplify Curse": "Amplify Curse", "Curse of Exhaustion": "Curse of Exhaustion",
                 "Soul Link": "Soul Link", "Shadowburn": "Shadowburn", "Conflagrate": "Conflagrate", "Incinerate": "Incinerate",
                 "Fel Domination": "Fel Domination", "Demonic Sacrifice": "Demonic Sacrifice"}


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
                cast = 0.0 if "instant" in cast_txt or channel else _seconds(cast_txt)
                coefs = {k: float(v) / 100 for v, k in COEF.findall(r.get("coefficient") or "")}
                rm = re.search(r"(\d+) yd range", r.get("range") or "")
                s = Spell(name=sp["name"], school=(r.get("school") or "shadow").lower(),
                          rank=int(NUM.search(r.get("rank") or "1").group(1)) if NUM.search(r.get("rank") or "") else 1,
                          level=int(r.get("level") or 1), cost=cost, cast=cast, cooldown=_seconds(r.get("cooldown")),
                          range=_num(rm.group(1)) if rm else 0.0, coef=coefs.get("direct", 0.0),
                          tags=("cost_pct",) if "base mana" in cost_txt else ())
                s.text = txt
                s.interrupt = parse_interrupt(txt)
                dm, dt, bn, fi, dr, tk, fu, tp, ab, ar, fe, cs, fl = (rx.search(txt) for rx in (DMG, DOT, BURN, FIRST, DRAIN, TICK, FUNNEL, TAP, ABSORB, ARMOR, FEAR, CONSUME, FLAT))
                if dm:
                    s.dmg_min, s.dmg_max = _num(dm.group(1)), _num(dm.group(2))
                elif fi:
                    s.dmg_min = s.dmg_max = _num(fi.group(1))
                elif fl and sp["name"] == "Death Coil":
                    s.dmg_min = s.dmg_max = _num(fl.group(1))
                if dt:
                    s.dot, s.dot_dur = _num(dt.group(1)), float(dt.group(3))
                elif bn:
                    s.dot, s.dot_dur = _num(bn.group(1)), float(bn.group(3))
                elif dr:
                    per, every, dur = _num(dr.group(1)), float(dr.group(2)), float(dr.group(3))
                    s.dot, s.dot_dur, s.dot_ticks = per * dur / every, dur, int(dur / every)
                    s.tags = s.tags + ("drain",)
                elif tk:
                    per, every, dur = _num(tk.group(1)), float(tk.group(3)), float(tk.group(4))
                    s.dot, s.dot_dur, s.dot_ticks = per * dur / every, dur, int(dur / every)
                elif SIPHON.search(txt):
                    si = SIPHON.search(txt)
                    per, every, dur = _num(si.group(1)), float(si.group(2)), float(si.group(3))
                    s.dot, s.dot_dur, s.dot_ticks = per * dur / every, dur, int(dur / every)
                elif channel and HELLFIRE.search(txt):   # 2026-09-27: these two parsed to 0 damage before
                    hf = HELLFIRE.search(txt)
                    per, every, dur = _num(hf.group(1)), float(hf.group(3)), float(hf.group(4))
                    s.dot, s.dot_dur, s.dot_ticks = per * dur / every, dur, int(dur / every)
                elif channel and RAIN.search(txt):
                    rn = RAIN.search(txt)
                    s.dot, s.dot_dur = _num(rn.group(1)), float(rn.group(3))
                    s.dot_ticks = max(1, int(round(s.dot_dur / 2.0)))   # a tick every 2 s
                if s.dot > 0 and not s.dot_ticks:
                    s.dot_ticks = max(1, int(round(s.dot_dur / 3.0)))
                if s.dot > 0:
                    s.dot_coef = coefs.get("per tick", 0.0)
                if channel:
                    s.kind = "channel"
                    s.channel = s.dot_dur or 5.0
                if fu:
                    per, dur = _num(fu.group(1)), float(fu.group(2))
                    s.kind, s.channel, s.dot_ticks, s.hot, s.hot_dur, s.target, s.resource = "channel", dur, int(dur), per * dur, dur, "pet", "health"
                    s.cost = per * dur   # Classic: the funnel costs the caster the health it gives
                if tp:
                    s.kind, s.resource, s.cost = "buff", "health", _num(tp.group(1))
                    s.tap = _num(tp.group(2))
                if ab:
                    s.kind, s.absorb = "heal", _num(ab.group(1) or ab.group(2))
                s.armor = _num(ar.group(1)) if ar else 0.0
                if fe:
                    s.fear = float(fe.group(1) or fe.group(2))
                if cs:
                    s.consume, s.consume_dur = _num(cs.group(1)), float(cs.group(2))
                st = STONE.search(txt)
                if st:
                    s.kind, s.heal_min, s.heal_max, s.cost, s.cooldown, s.cast = "heal", _num(st.group(1)), _num(st.group(1)), 0.0, 120.0, 0.0
                    s.resource = "none"
                if sp["name"] in ("Demon Armor", "Demon Skin", "Amplify Curse", "Soul Link", "Fel Domination") or sp["name"].startswith("Summon"):
                    s.kind = "buff"
                if sp["name"] in ("Torment", "Suffering"):
                    s.kind = "buff"
                book.setdefault(sp["name"], []).append(s)
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
    "Improved Life Tap": "+10%/rank Life Tap mana",
    "Suppression": "+1%/rank spell hit",
    "Improved Corruption": "-0.4s/rank Corruption cast (instant at 5/5), +2%/rank damage",
    "Malediction": "+1%/rank periodic damage",
    "Soul Harvesting": "not used (Drain Soul kills are not part of the loop)",
    "Improved Drains": "+7/13/20% Drain Life, Drain Soul, Wrack",
    "Improved Bane of Agony": "+5%/rank Bane of Agony",
    "Fel Concentration": "23%/rank chance to ignore pushback on drains and Wrack",
    "Amplify Curse": "+50% on the next Bane of Agony every 3 min",
    "Pandemic": "+33%/rank crit damage bonus on Corruption, Agony, drains, Siphon Life, Wrack",
    "Malevolence": "+1%/rank Shadow crit",
    "Nightfall": "2%/rank per Corruption / drain / Wrack tick: next Shadow Bolt instant (Shadow Trance)",
    "Curse of Exhaustion": "not used (the Voidwalker holds the mob)",
    "Siphon Life": "unlocks Siphon Life (instant 30s drain DoT, heals you per tick)",
    "Soul Siphon": "+4%/rank drains and Wrack per other Affliction effect on the target (up to 3)",
    "Shadow Mastery": "+1%/rank Shadow damage and drains",
    "Wrack": "unlocks Wrack (6s channel, 36/s at 60, +10% damage taken from your other Shadow DoTs)",
    "Improved Health Funnel": "+20%/rank Health Funnel healing, -15%/rank health cost",
    "Improved Imp": "+10%/rank Firebolt (levels 1-9)",
    "Demonic Embrace": "+3%/rank Stamina",
    "Unholy Power": "+2%/rank pet damage",
    "Demonic Aegis": "+15%/rank Demon Armor / Demon Skin armor",
    "Improved Voidwalker": "+10%/rank Torment threat, Consume Shadows and Sacrifice",
    "Fel Vitality": "+5%/rank pet health and mana, +5%/rank your mana",
    "Demonic Energies": "your pet is healed for 7.5%/rank of your spell damage; Life Tap mana is shared with it",
    "Master Summoner": "-2s/rank re-summon after a pet death",
    "Fel Domination": "not modelled (one fast re-summon per 5 min)",
    "Demonic Sacrifice": "not used while leveling (the Voidwalker tanks)",
    "Soul Link": "30% of damage you take goes to the pet; both deal +3%",
    "Demonic Knowledge": "+33%/rank of your level as spell power with a pet out",
    "Master Demonologist": "Voidwalker: -2%/rank physical damage taken",
    "Improved Sayaad": "not used (Voidwalker)",
    "Improved Felhunter": "not used (Voidwalker)",
    "Destructive Reach": "+10%/rank range (longer pulls)",
    "Improved Shadow Bolt": "Shadow Bolt crits: +4%/rank Shadow damage taken for 12s",
    "Bane": "-0.1s/rank Shadow Bolt / Immolate cast",
    "Molten Skin": "-2%/rank damage taken",
    "Cataclysm": "-3.3%/rank Destruction mana cost",
    "Aftermath": "+10%/rank Immolate direct damage",
    "Ruin": "+20%/rank Destruction crit damage bonus",
    "Shadowburn": "unlocks Shadowburn (instant, 15s cooldown): a finisher",
    "Intensity": "23%/rank chance to ignore pushback on Destruction spells",
    "Agonizing Flames": "+3.3%/rank Destruction damage",
}
FIT = {
    "Improved Corruption": "scale", "Malediction": "scale", "Improved Drains": "scale", "Fel Concentration": "scale", "Pandemic": "scale",
    "Malevolence": "scale", "Nightfall": "scale",
    "Siphon Life": ("replace", [{"channel": "dmg", "scope": ["all"], "values": [0.05]}, {"channel": "sustain", "scope": ["all"], "values": [0.05]}]),
    "Soul Siphon": "scale", "Shadow Mastery": "scale", "Wrack": "scale", "Improved Life Tap": "scale",
    "Suppression": ("replace", [{"channel": "hit", "scope": ["type:spell"], "per_rank": 0.01}, {"channel": "dmg", "scope": ["type:spell"], "per_rank": 0.005}]),
    "Amplify Curse": "scale", "Improved Bane of Agony": "scale", "Demonic Embrace": "scale", "Unholy Power": "scale", "Fel Vitality": "scale",
    "Demonic Energies": "scale", "Improved Voidwalker": "scale", "Improved Health Funnel": "scale", "Master Summoner": "scale", "Soul Link": "scale",
    "Demonic Knowledge": "scale", "Master Demonologist": "scale", "Demonic Aegis": "scale", "Improved Shadow Bolt": "scale", "Bane": "scale", "Ruin": "scale",
    "Cataclysm": "scale", "Destructive Reach": "scale", "Improved Imp": "scale", "Molten Skin": "scale", "Aftermath": "scale", "Agonizing Flames": "scale",
    "Shadowburn": "scale", "Intensity": "scale", "Soul Harvesting": "scale",
}
SHARE_SOURCE = {'Rain of Fire': 'rain_of_fire', "Corruption": "corruption", "Bane of Agony": "agony", "Drain Life": "drain_life", "Shadow Bolt": "shadow_bolt", "Immolate": "immolate",
                "Wand": "wand", "Voidwalker melee": "voidwalker", "Siphon Life": "siphon_life", "Wrack": "wrack", "Death Coil": "death_coil"}
NEW_SOURCES = {'rain_of_fire': {'id': 'rain_of_fire', 'share': 0.0, 'min_level': 20, 'tags': ['type:spell', 'school:fire', 'aoe', 'ability:Rain of Fire', 'ability:Destruction'], 'cast': 8.0, 'min_cast': 8.0}, "siphon_life": {"id": "siphon_life", "share": 0.0, "min_level": 30, "tags": ["type:spell", "school:shadow", "dot", "instant", "mainschool", "ability:Siphon Life", "ability:Affliction", "ability:Warlock"]},
               "wrack": {"id": "wrack", "share": 0.0, "min_level": 40, "tags": ["type:spell", "school:shadow", "channel", "mainschool", "ability:Wrack", "ability:Affliction", "ability:Warlock"]},
               "death_coil": {"id": "death_coil", "share": 0.0, "min_level": 42, "tags": ["type:spell", "school:shadow", "instant", "mainschool", "ability:Death Coil"], "cooldown": 120}}
KEY_TALENTS = ["Siphon Life", "Demonic Knowledge", "Soul Link"]
DESCRIPTION = ("Single-target leveling fights against normal mobs of your level with a Voidwalker: the pet runs in and meets the mob halfway, Torments it every 5 s, "
               "and holds it until your threat passes 130% of its own (it takes the mob back once its threat passes yours by 10%). You cast Corruption, Bane of Agony, "
               "Siphon Life and Immolate, channel Wrack once the DoTs are up, fill with Shadow Bolt while mana is plentiful and the wand otherwise, Drain Life when "
               "hurt, Life Tap when low on mana, Fear or Death Coil a mob that reaches you. Between fights: 2 s loot, 6 s travel, Life Tap back to 70% mana, Consume "
               "Shadows or Health Funnel for the pet, food only below 35% health, a 10-12 s re-summon after a pet death; a death costs 90 s.")
NOT_MODELLED = "runners, adds, soul shard economy (Drain Soul, Shadowburn shards), Curse of Exhaustion kiting, Sacrifice, Demonic Sacrifice, Succubus/Felhunter pets, gear upgrades within a level bracket."
# rebuild.py: which scorer model, hand draft and optimizer build the pipeline calibrates, races and reports for this class
PIPELINE = {"variants": [{'spec': 'affliction-leveling', 'opt': 'opt-affliction-leveling-leveling-aoe', 'tag': 'aoe', 'profile': 'leveling-aoe', 'lookahead': 16, 'sets': ['MOBS_PER_PULL=3'], 'levels': '30,40,50,60', 'calibrate_levels': '40,60', 'label': 'AoE grinding, 3 mobs per pull'}], "spec": "affliction-leveling", "hand": "leveling-affliction", "opt": "opt-affliction-leveling-leveling-st", "tag": "affliction", "lookahead": 16,
            "levels": "20,30,40,50,60", "calibrate_levels": "30,60"}

# level-60 demon stats (ElliotWood/Forever pets.go); Str/Agi/Sta/Int/Spi scale from ~20 at level 1, damage with level
PETS = {
    "Voidwalker": dict(strength=129, agility=85, stamina=234, intellect=70, spirit=150, mana=1066, dmg=(31, 46), speed=2.0, armor_per_level=60, hp_mult=1.0, caster=False, threat_mult=1.0),
    "Imp": dict(strength=122, agility=35, stamina=86, intellect=264, spirit=260, mana=576, dmg=(0, 0), speed=2.0, armor_per_level=20, hp_mult=0.45, caster=True, threat_mult=1.0),
}


def pet_health(level):
    """Pet base health by level (Classic Voidwalker ~250 at 10, ~1,000 at 30, ~1,800 at 40, ~3,200 at 60: 0.85 L^2 + 8 L + 100)."""
    return 0.85 * level * level + 8 * level + 100


def torment_threat(level):
    """Torment threat per cast: Classic ranks ~45 at 10 to ~320 at 60 (5.3 per level)."""
    return 5.3 * level


class WarlockModule(BaseModule):
    resource = "mana"
    special_stat = ("Pet deaths/100", "pet_deaths_per_100")
    eat_below = 0.55      # eat after the Life Taps when below this (a warlock tapped to 60% and then hit by a turned mob dies)
    drink_below = 0.15
    THREAT_CARE = 1.15    # hold back Shadow Bolt / Immolate / Wrack once your threat passes this multiple of the pet's (0 = never hold back)

    AOE = {'channel': ['Rain of Fire'], 'dots': ['Corruption', 'Bane of Agony', 'Immolate'], 'min_near': 2}

    def __init__(self, talents, level, spec="affliction-leveling", gear="leveling"):
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
        self.pet_name = "Voidwalker" if level >= 10 else "Imp"
        self.armor_spell_used = "Demon Armor" if "Demon Armor" in self.spells else ("Demon Skin" if "Demon Skin" in self.spells else "none")

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
        base = class_base_stats("warlock", level)
        g = gear_stats(level, self.gear, "warlock")
        intellect = base["intellect"] + g["intellect"]
        spirit = base["spirit"] + g["spirit"]
        stamina = (base["stamina"] + g["stamina"]) * (1 + self.tv("Demonic Embrace", 0) / 100)
        armor_spell = self.book.get("Demon Armor") or self.book.get("Demon Skin")
        armor = g["armor"] + (armor_spell.armor if armor_spell else 0.0) * (1 + self.tv("Demonic Aegis", 0) / 100)
        self.armor_regen = 0.0
        if armor_spell is not None:
            m = re.search(r"health regeneration by (\d+) health per 5 sec", armor_spell.text)
            self.armor_regen = float(m.group(1)) * 2 / 5 if m else 0.0   # per 2-second tick
        sp = g["spell_power"] + level * self.tv("Demonic Knowledge", 0) / 100
        bm = class_base_mana("warlock", level)
        p = Player(level=level, hp_max=class_base_health("warlock", level) + 10 * stamina, hp=0.0,
                   mana_max=(bm + 15 * intellect) * (1 + self.tv("Fel Vitality", 1) / 100), mana=0.0, base_mana=bm, spirit=spirit,
                   intellect=intellect, spell_power=sp, armor=armor, spell_crit=class_spell_crit("warlock", level, intellect), dodge=0.04, ranged_crit=0.03)
        p.hp, p.mana = p.hp_max, p.mana_max
        p.pet = self.make_pet(level)
        return p

    def make_pet(self, level):
        cfg = PETS[self.pet_name]
        f = (level - 1) / 59.0
        stat = {k: 20 + (cfg[k] - 20) * f for k in ("strength", "agility", "stamina", "intellect", "spirit")}
        hp = (pet_health(level) + 10 * stat["stamina"] * 0.5) * cfg["hp_mult"] * (1 + self.tv("Fel Vitality", 0) / 100)
        pet = Pet(name=self.pet_name, hp_max=hp, hp=hp, armor=cfg["armor_per_level"] * level,
                  dmg_min=cfg["dmg"][0] * level / 60.0, dmg_max=cfg["dmg"][1] * level / 60.0, speed=cfg["speed"],
                  attack_power=max(0.0, 2 * stat["strength"] - 20), crit=0.05 + stat["agility"] * 0.05 / 100,
                  focus=0.0, focus_max=0.0, focus_regen=0.0, mana=cfg["mana"] * level / 60.0 * (1 + self.tv("Fel Vitality", 0) / 100),
                  mana_max=cfg["mana"] * level / 60.0 * (1 + self.tv("Fel Vitality", 0) / 100), mana_regen=(15 + stat["spirit"] / 5) / 2.0,
                  threat_mult=cfg["threat_mult"], caster=cfg["caster"])
        pet.dmg_mult = (1 + self.tv("Unholy Power", 0) / 100) * (1.03 if self.rank("Soul Link") else 1.0)
        return pet

    def pull_range(self):
        return 30.0 * (1 + self.tv("Destructive Reach", 0) / 100)

    # ------------------------------------------------------------ engine hooks: numbers
    def cast_time(self, spell):
        c = spell.cast
        if spell.name == "Corruption":
            c = max(0.0, c - 0.4 * self.rank("Improved Corruption"))
            c = 0.0 if c < 0.5 else max(GCD, c)
        if spell.name in ("Shadow Bolt", "Immolate", "Incinerate"):
            c = max(GCD, c - 0.1 * self.rank("Bane"))
        if spell.name == "Shadow Bolt" and self._fight and self._fight.p.buff("Shadow Trance", self._fight.t):
            return 0.0
        return c

    def mana_cost(self, spell):
        cost = spell.cost
        if "cost_pct" in spell.tags:
            cost = cost / 100 * self._base_mana
        if spell.name in ("Shadow Bolt", "Immolate", "Searing Pain", "Incinerate", "Conflagrate", "Shadowburn", "Soul Fire"):
            cost *= 1 - self.tv("Cataclysm", 0) / 100
        if spell.name == "Health Funnel":
            cost *= 1 - self.tv("Improved Health Funnel", 1) / 100
        return cost

    def hit_bonus(self, spell):
        return self.tv("Suppression", 0) / 100

    def crit_bonus(self, spell, frozen):
        c = 0.0
        if spell.school == "shadow":
            c += self.tv("Malevolence", 0) / 100
        return c

    def crit_damage_bonus(self, spell):
        c = 0.0
        if spell.name in ("Corruption", "Bane of Agony", "Bane of Doom", "Drain Soul", "Drain Life", "Siphon Life", "Wrack"):
            c += self.tv("Pandemic", 0) / 100
        if spell.name in ("Shadow Bolt", "Immolate", "Searing Pain", "Incinerate", "Conflagrate", "Shadowburn", "Soul Fire"):
            c += self.tv("Ruin", 0) / 100
        return c

    def damage_multiplier(self, spell, frozen):
        m = 1.0 + (0.03 if self.rank("Soul Link") else 0.0)
        if self._fight and spell.school not in ("physical", None):   # Curse of the Elements: +10% magic damage taken (2026-09-29)
            coe = self._fight.m.debuffs.get("Curse of the Elements")
            if coe and coe["until"] > self._fight.t:
                m *= 1.10
        if spell.school == "shadow":
            m *= 1 + self.tv("Shadow Mastery", 0) / 100
            if self._fight:
                isb = self._fight.m.debuffs.get("Improved Shadow Bolt")
                if isb and isb["until"] > self._fight.t:
                    m *= 1 + self.tv("Improved Shadow Bolt", 0) / 100
        if spell.name in ("Shadow Bolt", "Immolate", "Searing Pain", "Incinerate", "Conflagrate", "Shadowburn", "Soul Fire"):
            m *= 1 + self.tv("Agonizing Flames", 1) / 100
        if spell.name == "Immolate" and spell.dot_ticks and self._fight and self._fight.channel is None:
            m *= 1 + self.tv("Aftermath", 0) / 100   # direct part only (the periodic multiplier below leaves it out)
        if spell.name == "Corruption":
            m *= 1 + self.tv("Improved Corruption", 1) / 100
        if spell.name == "Bane of Agony":
            m *= 1 + self.tv("Improved Bane of Agony", 0) / 100
            if self._fight and self._fight.p.buff("Amplify Curse", self._fight.t):
                m *= 1.5
        if spell.name in ("Drain Life", "Drain Soul", "Wrack"):
            m *= 1 + self.tv("Improved Drains", 0) / 100
            if self._fight:
                others = sum(1 for n in ("Corruption", "Bane of Agony", "Siphon Life") if self._fight.dot_active(n))
                m *= 1 + min(3, others) * self.tv("Soul Siphon", 0) / 100
        return m

    def periodic_multiplier(self, spell):
        m = self.damage_multiplier(spell, False)
        if spell.name == "Immolate":
            m /= 1 + self.tv("Aftermath", 0) / 100
        if spell.kind != "channel":
            m *= 1 + self.tv("Malediction", 0) / 100
            if self._fight and spell.school == "shadow":
                w = self._fight.m.debuffs.get("Wrack")
                if w and w["until"] > self._fight.t:
                    m *= 1.10
        return m

    def periodic_can_crit(self, spell):
        return True

    def armor_bonus(self):
        return 0.0

    def wand_damage(self):
        return wand_dps(self.level) * WAND_SPEED

    def pushback_resisted(self, fight, spell):
        if spell.name in ("Drain Life", "Drain Soul", "Drain Mana", "Wrack") and self.rank("Fel Concentration"):
            return fight.rng.random() < self.tv("Fel Concentration", 0) / 100
        if spell.school == "fire" and self.rank("Intensity"):
            return fight.rng.random() < self.tv("Intensity", 0) / 100
        return False

    def split_damage_taken(self, fight, dmg):
        pet = fight.p.pet
        if self.rank("Soul Link") and pet is not None and pet.alive:
            pet.hp -= 0.3 * dmg
            if pet.hp <= 0:
                pet.alive, pet.engaged = False, False
                fight.pet_died = True
                fight.m.target = "player"
            return 0.7 * dmg
        return dmg

    def mana_regen(self, p, t):
        return class_mana_regen_tick("warlock", p.spirit)

    def health_regen(self, p):
        return class_health_regen_tick("warlock", p.spirit) + self.armor_regen

    def resummon_time(self):
        return max(4.0, 12.0 - 2.0 * self.rank("Master Summoner"))

    # ------------------------------------------------------------ pet
    def pet_decide(self, fight):
        p, m, t, pet = fight.p, fight.m, fight.t, fight.p.pet
        if pet.name == "Voidwalker":
            tor = self.spells.get("Torment")
            if tor is not None and pet.cooldowns.get("Torment", -1.0) <= t and pet.mana >= tor.cost and (m.pet_in_melee or m.in_melee):
                thr = torment_threat(self.level) * (1 + self.tv("Improved Voidwalker", 0) / 100)
                return Spell("Torment", "shadow", cost=tor.cost, cooldown=5.0, kind="buff", dmg_min=thr, resource="mana")
            return None
        if pet.name == "Imp":
            fb = self.spells.get("Firebolt")
            if fb is not None and pet.cooldowns.get("Firebolt", -1.0) <= t and pet.mana >= fb.cost:
                s = Spell("Firebolt", "fire", cost=fb.cost, cooldown=fb.cast + 0.2, kind="spell", dmg_min=fb.dmg_min, dmg_max=fb.dmg_max, resource="mana")
                s.dmg_min *= 1 + self.tv("Improved Imp", 0) / 100
                s.dmg_max *= 1 + self.tv("Improved Imp", 0) / 100
                return s
        return None

    # ------------------------------------------------------------ engine hooks: events
    def on_fight_start(self, fight):
        self._fight = fight
        self._base_mana = fight.p.base_mana
        p, t = fight.p, fight.t
        if self.rank("Amplify Curse") and p.ready("Amplify Curse", t):
            p.buffs["Amplify Curse"] = {"until": t + 30.0}
            p.cooldowns["Amplify Curse"] = t + 180.0

    def on_hit(self, fight, spell, amount, crit, frozen):
        p, m, t = fight.p, fight.m, fight.t
        if spell.name == "Life Tap":
            mana = getattr(spell, "tap", spell.cost) * (1 + self.tv("Improved Life Tap", 0) / 100)
            p.mana = min(p.mana_max, p.mana + mana)
            if self.rank("Demonic Energies") and p.pet is not None and p.pet.alive:
                p.pet.mana = min(p.pet.mana_max, p.pet.mana + mana)
            fight.note(f"Life Tap +{mana:.0f} mana")
            return
        if spell.name == "Death Coil" and amount > 0:
            fight.heal(spell, amount)
        if spell.name == "Shadow Bolt" and crit and self.rank("Improved Shadow Bolt"):
            m.debuffs["Improved Shadow Bolt"] = {"until": t + 12.0, "stacks": 1}
        if spell.name == "Wrack":
            m.debuffs["Wrack"] = {"until": t + 6.0, "stacks": 1}
        if spell.name == "Bane of Agony" and p.buff("Amplify Curse", t):
            del p.buffs["Amplify Curse"]
        if amount > 0:
            self.pet_heal_from_damage(fight, amount)

    def pet_heal_from_damage(self, fight, amount):
        pet = fight.p.pet
        if self.rank("Demonic Energies") and pet is not None and pet.alive:
            pet.hp = min(pet.hp_max, pet.hp + amount * self.tv("Demonic Energies", 0) / 100)

    def on_tick(self, fight, spell, amount, crit):
        p, t = fight.p, fight.t
        if amount <= 0:
            return
        if spell.name == "Siphon Life":
            fight.heal(Spell("Siphon Life", "shadow"), amount)
        if spell.name in ("Corruption", "Drain Life", "Drain Soul", "Wrack") and self.rank("Nightfall") and fight.rng.random() < self.tv("Nightfall", 0) / 100:
            p.buffs["Shadow Trance"] = {"until": t + 10.0}
        self.pet_heal_from_damage(fight, amount)

    def after_cast(self, fight, spell):
        if spell.name == "Curse of the Elements":   # a Curse, not a Bane: it sits beside Bane of Agony (one of each per warlock)
            fight.m.debuffs["Curse of the Elements"] = {"until": fight.t + 300.0}
        p, t = fight.p, fight.t
        if spell.cooldown > 0:
            p.cooldowns[spell.name] = t + spell.cooldown
        if spell.name == "Shadow Bolt" and p.buff("Shadow Trance", t):
            del p.buffs["Shadow Trance"]

    def on_pet_death(self, fight):
        pass

    def after_fight(self, p, t):
        """Life Tap back to 70% mana while health allows; Consume Shadows (10 s) or Health Funnel (10 s) for a hurt Voidwalker."""
        spent = 0.0
        tap = self.spells.get("Life Tap")
        if tap is not None:
            while p.mana < 0.70 * p.mana_max and p.hp - tap.cost > 0.60 * p.hp_max:
                p.hp -= tap.cost
                p.mana = min(p.mana_max, p.mana + getattr(tap, "tap", tap.cost) * (1 + self.tv("Improved Life Tap", 0) / 100))
                spent += GCD
        pet = p.pet
        if pet is not None and pet.alive and pet.hp < 0.6 * pet.hp_max:
            cs = self.spells.get("Consume Shadows")
            if cs is not None and pet.mana >= cs.cost:
                pet.mana -= cs.cost
                pet.hp = min(pet.hp_max, pet.hp + getattr(cs, "consume", 0.0) * (1 + self.tv("Improved Voidwalker", 0) / 100))
                spent += 10.0
            if pet.hp < 0.5 * pet.hp_max:
                hf = self.spells.get("Health Funnel")
                if hf is not None and p.hp > 0.5 * p.hp_max:
                    give = min(pet.hp_max - pet.hp, hf.hot * (1 + self.tv("Improved Health Funnel", 0) / 100), p.hp - 0.4 * p.hp_max)
                    if give > 0:
                        pet.hp += give
                        p.hp -= give * (1 - self.tv("Improved Health Funnel", 1) / 100) / (1 + self.tv("Improved Health Funnel", 0) / 100)
                        spent += 10.0 * give / (hf.hot * (1 + self.tv("Improved Health Funnel", 0) / 100))
        return spent

    # ------------------------------------------------------------ priority list
    def decide(self, fight):
        if fight.others():   # a pull of several mobs: the area priority first (engine.BaseModule.decide_aoe, AOE below)
            r = self.decide_aoe(fight)
            if r is not None:
                return r
        p, m, t, pet = fight.p, fight.m, fight.t, fight.p.pet
        sp = self.spells
        on_me = m.target == "player" or pet is None or not pet.alive
        in_melee = m.in_melee and m.dist <= MELEE_RANGE + 0.5

        def avg(s):
            return (s.dmg_min + s.dmg_max) / 2 + s.coef * p.spell_power if s else 0.0

        def can(s):
            return s is not None and p.ready(s.name, t) and fight.can_afford(s, self.mana_cost(s))

        corr, agony, siphon, immo, wrack, bolt, drain, tap, fear, coil, burn = (sp.get(n) for n in ("Corruption", "Bane of Agony", "Siphon Life", "Immolate", "Wrack", "Shadow Bolt", "Drain Life", "Life Tap", "Fear", "Death Coil", "Shadowburn"))
        coe = sp.get("Curse of the Elements")
        hp = m.hp
        wand_hit = self.wand_damage() * 0.65
        pet_threat = m.threat_pet + self.pet_threat_bonus(fight)
        near_aggro = self.THREAT_CARE > 0 and pet is not None and pet.alive and m.target == "pet" and m.threat_player > self.THREAT_CARE * pet_threat and m.threat_player > 50
        stone = sp.get("Create Healthstone")
        # the mob is on me: Fear it at once (Death Coil when hurt), Healthstone when low, Drain Life while it flees or from range
        if stone and p.hp < 0.35 * p.hp_max and p.ready(stone.name, t):
            return stone
        if on_me and hp > 0.2 * m.hp_max and not m.incapacitated(t):
            if coil and can(coil) and p.hp < 0.6 * p.hp_max:
                return coil
            if fear and can(fear) and (in_melee or m.dist <= fear.range):
                return fear
        if on_me and drain and can(drain) and p.hp < 0.7 * p.hp_max and hp > wand_hit * 4 and m.dist <= drain.range and (m.incapacitated(t) or not in_melee):
            return drain
        # finish without overkill
        if burn and can(burn) and hp <= avg(burn) * 0.9:
            return burn
        if hp <= wand_hit * 1.5:
            return "wand"
        # health and mana: Drain Life when hurt; Life Tap behind a healthy pet when the next bolt is unaffordable
        if drain and can(drain) and p.hp < 0.60 * p.hp_max and hp > wand_hit * 4 and m.dist <= drain.range:
            return drain
        bolt_cost = self.mana_cost(bolt) if bolt else 0.0
        reserve = (self.mana_cost(fear) if fear else 0.0) + (self.mana_cost(drain) if drain else 0.0)
        pet_ok = not (on_me and in_melee) and not (pet is not None and pet.alive and m.target == "pet" and pet.hp < 0.3 * pet.hp_max)
        if tap and bolt and pet_ok and p.mana - bolt_cost < reserve and p.hp - tap.cost > 0.60 * p.hp_max and hp > avg(bolt) and not near_aggro:
            return tap
        # DoTs once each, when the mob will live long enough (Curse of the Elements first: it raises every spell after it)
        if coe and can(coe) and not (m.debuffs.get("Curse of the Elements") or {}).get("until", 0) > t and hp > 0.5 * m.hp_max:
            return coe
        if corr and can(corr) and not fight.dot_active("Corruption") and hp > 0.25 * m.hp_max:
            return corr
        if agony and can(agony) and not fight.dot_active("Bane of Agony") and hp > 0.35 * m.hp_max:
            return agony
        if siphon and can(siphon) and not fight.dot_active("Siphon Life") and hp > 0.35 * m.hp_max:
            return siphon
        if immo and can(immo) and not fight.dot_active("Immolate") and hp > 0.45 * m.hp_max and p.mana > 0.5 * p.mana_max and not (on_me and in_melee) and not near_aggro and p.mana - self.mana_cost(immo) > reserve:
            return immo
        if wrack and can(wrack) and not (m.debuffs.get("Wrack", {}).get("until", 0) > t) and fight.dot_active("Corruption") and hp > 0.25 * m.hp_max and not near_aggro:
            return wrack
        # filler: Shadow Bolt while mana lasts and the pet holds (a Shadow Trance bolt is free time), Drain Life to repair Life Taps, wand otherwise
        if bolt and can(bolt) and p.buff("Shadow Trance", t) and hp > avg(bolt) * 0.5:
            return bolt
        if bolt and can(bolt) and hp > avg(bolt) * 0.9 and not (on_me and in_melee) and not near_aggro and p.mana - bolt_cost > reserve:
            return bolt
        if drain and can(drain) and p.hp < 0.85 * p.hp_max and hp > wand_hit * 4 and m.dist <= drain.range and not near_aggro:
            return drain
        return "wand"
        # health and mana: Drain Life when hurt, Life Tap when the next bolt is unaffordable and health can pay for it
        if drain and can(drain) and p.hp < 0.60 * p.hp_max and hp > wand_hit * 4 and m.dist <= drain.range:
            return drain
        bolt_cost = self.mana_cost(bolt) if bolt else 0.0
        if tap and bolt and p.mana < bolt_cost + 50 and p.hp - tap.cost > 0.50 * p.hp_max and not (on_me and in_melee) and hp > avg(bolt):
            return tap
        # DoTs once each, when the mob will live long enough (Curse of the Elements first: it raises every spell after it)
        if coe and can(coe) and not (m.debuffs.get("Curse of the Elements") or {}).get("until", 0) > t and hp > 0.5 * m.hp_max:
            return coe
        if corr and can(corr) and not fight.dot_active("Corruption") and hp > 0.25 * m.hp_max:
            return corr
        if agony and can(agony) and not fight.dot_active("Bane of Agony") and hp > 0.35 * m.hp_max:
            return agony
        if siphon and can(siphon) and not fight.dot_active("Siphon Life") and hp > 0.35 * m.hp_max:
            return siphon
        if immo and can(immo) and not fight.dot_active("Immolate") and hp > 0.45 * m.hp_max and p.mana > 0.5 * p.mana_max and not (on_me and in_melee):
            return immo
        if wrack and can(wrack) and not (m.debuffs.get("Wrack", {}).get("until", 0) > t) and fight.dot_active("Corruption") and hp > 0.25 * m.hp_max:
            return wrack
        # filler: Shadow Bolt while mana lasts (a Shadow Trance bolt is free time), Drain Life to repair Life Taps, wand when out of both
        if bolt and can(bolt) and p.buff("Shadow Trance", t) and hp > avg(bolt) * 0.5:
            return bolt
        if bolt and can(bolt) and hp > avg(bolt) * 0.9 and hp > dots_left * 0.7 and not (on_me and in_melee):
            return bolt
        if drain and can(drain) and p.hp < 0.85 * p.hp_max and hp > wand_hit * 4 and m.dist <= drain.range:
            return drain
        return "wand"
