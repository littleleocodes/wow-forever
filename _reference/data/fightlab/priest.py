"""Priest module for the fight lab (Shadow leveling).

Spell ranks (damage, periodic damage, heals, absorbs, cost, cast, cooldown, coefficients) are read from
`_reference/data/forever-spells/priest.json` (beta client build 1.60.1.70009); talent numbers from each rank's tooltip in
`_reference/data/forever-talents/priest.json`. What a talent *does* is coded here per talent; the numbers are the client's.

Playstyle `shadow-dps` (the scorer's model id): Power Word: Shield and Inner Fire before the pull, Mind Blast at range,
Shadow Word: Pain, Mind Flay channels (slowing the mob) and Mind Blast on cooldown, Vampiric Embrace and Devouring Plague
for self-healing, Shadow Word: Death as an execute, wand to finish without overkill; Psychic Scream and Desperate Prayer
when health runs low; Renew between fights until Shadowform (which forbids heals) replaces it with eating.
"""
import json
import pathlib
import re

from engine import parse_interrupt, BaseModule, Player, Spell
from tables import (GCD, MELEE_RANGE, WAND_SPEED, class_base_health, class_base_mana, class_base_stats, class_health_regen_tick,
                    class_mana_regen_tick, class_spell_crit, gear_stats, wand_dps)

ROOT = pathlib.Path(__file__).resolve().parents[3]
SPELLBOOK = json.load(open(ROOT / "_reference/data/forever-spells/priest.json", encoding="utf-8"))
TREE = json.load(open(ROOT / "_reference/data/forever-talents/priest.json", encoding="utf-8"))

NUM = re.compile(r"(\d+(?:\.\d+)?)")
DMG = re.compile(r"(\d[\d,]*) to (\d[\d,]*) (\w+) damage")
DOT = re.compile(r"caus(?:es|ing) (\d[\d,]*) (\w+) damage over (\d+) sec")
BURN = re.compile(r"additional (\d[\d,]*) (\w+) damage over (\d+) sec")
HEAL = re.compile(r"[Hh]eals?[^.]*? for (\d[\d,]*) to (\d[\d,]*)(?!\s+\w+ damage)")
HOT = re.compile(r"Heals the target of (\d[\d,]*) damage over (\d+) sec")
ABSORB = re.compile(r"absorbing ([\d,]+) damage")
ARMOR = re.compile(r"increasing armor by ([\d,]+)")
CHILL = re.compile(r"slowing their movement speed by (\d+)%")
FEAR = re.compile(r"flee for (\d+) sec")
COEF = re.compile(r"([\d.]+)% of spell power \((\w+(?: \w+)?)\)")

TALENT_SPELLS = {"Mind Flay": "Mind Flay", "Vampiric Embrace": "Vampiric Embrace", "Shadowform": "Shadowform", "Silence": "Silence",
                 "Holy Nova": "Holy Nova", "Penance": "Penance", "Binding Heal": "Binding Heal", "Prayer of Mending": "Prayer of Mending",
                 "Inner Focus": "Inner Focus", "Power Infusion": "Power Infusion"}
CHANNEL_TICKS = {"Mind Flay": 3, "Starshards": 6, "Penance": 3}
SELF_ONLY = {"Renew", "Flash Heal", "Lesser Heal", "Heal", "Greater Heal", "Power Word: Shield", "Desperate Prayer", "Binding Heal"}


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
                dm, dt, bn, he, ho, ab, ar, ch, fe = (rx.search(txt) for rx in (DMG, DOT, BURN, HEAL, HOT, ABSORB, ARMOR, CHILL, FEAR))
                s = Spell(name=sp["name"], school=(r.get("school") or "holy").lower(),
                          rank=int(NUM.search(r.get("rank") or "1").group(1)) if NUM.search(r.get("rank") or "") else 1,
                          level=int(r.get("level") or 1), cost=cost, cast=cast, cooldown=_seconds(r.get("cooldown")),
                          range=_num(rm.group(1)) if rm else 0.0,
                          dmg_min=_num(dm.group(1)) if dm else 0.0, dmg_max=_num(dm.group(2)) if dm else 0.0,
                          coef=coefs.get("direct", 0.0), tags=("cost_pct",) if "base mana" in cost_txt else ())
                s.text = txt
                s.interrupt = parse_interrupt(txt)
                if dt and not dm:
                    s.dot, s.dot_dur = _num(dt.group(1)), float(dt.group(3))
                elif bn:
                    s.dot, s.dot_dur = _num(bn.group(1)), float(bn.group(3))
                if s.dot > 0:
                    s.dot_ticks = CHANNEL_TICKS.get(sp["name"], max(1, int(round(s.dot_dur / 3.0))))
                    s.dot_coef = coefs.get("per tick", 0.0)
                if channel:
                    s.kind = "channel"
                    s.channel = s.dot_dur or 3.0
                if ch:
                    s.chill, s.chill_dur = float(ch.group(1)) / 100, s.dot_dur or 3.0
                if fe:
                    s.fear = float(fe.group(1))
                if he and not dm:
                    s.kind = "heal"
                    s.heal_min, s.heal_max, s.heal_coef = _num(he.group(1)), _num(he.group(2)), coefs.get("heal", 0.0)
                if ho:
                    s.kind = "heal"
                    s.hot, s.hot_dur, s.heal_coef = _num(ho.group(1)), float(ho.group(2)), coefs.get("per tick", 0.0)
                if ab:
                    s.kind = "heal"
                    s.absorb = _num(ab.group(1))
                s.armor = _num(ar.group(1)) if ar else 0.0
                if sp["name"] in ("Shadowform", "Inner Fire", "Power Word: Fortitude", "Divine Spirit", "Fade", "Vampiric Embrace"):
                    s.kind = "buff"
                if sp["name"] == "Vampiric Embrace":
                    s.kind = "spell"   # a debuff on the mob: rolls hit like a spell, no damage
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
    "Shadow Focus": "+1% Shadow hit per rank",
    "Blackout": "2% per rank: a Shadow damage hit or tick stuns the mob 3s",
    "Spirit Tap": "20%/rank chance on a kill: +100% Spirit for 15s and 50% regen while casting",
    "Improved Shadow Word: Pain": "+3s (one tick) per rank on Shadow Word: Pain",
    "Shadow Reach": "+10%/rank Shadow range: longer pulls",
    "Improved Mind Blast": "-0.5s/rank Mind Blast cooldown",
    "Improved Psychic Scream": "-2s/rank Psychic Scream cooldown",
    "Mind Flay": "unlocks Mind Flay (3s channel, 3 ticks, 50% slow)",
    "Improved Mind Flay": "+10%/rank Mind Flay damage and +5 yd range; the slow weakens to 35/20%",
    "Vampiric Embrace": "20% of Shadow damage dealt heals you for 30s (1 min cooldown, 40 mana)",
    "Shadow Weaving": "33%/rank chance per Shadow hit: +2% Shadow damage per stack (5 stacks, 15s)",
    "Devouring Contagion": "-25%/rank Devouring Plague mana cost",
    "Early Demise": "+15%/rank Shadow Word: Death crit below 20% health",
    "Darkness": "+2%/rank Shadow damage",
    "Shadowform": "+10% Shadow damage, -50% Shadow mana cost, Shadow crits x2.0, -15% physical damage taken, no heals",
    "Wand Specialization": "+13/25% wand damage",
    "Twin Disciplines": "+1%/rank damage and healing of instant casts",
    "Improved Power Word: Shield": "+7/14/20% absorb",
    "Martyrdom": "Focused Casting for 6s after a melee crit: no pushback",
    "Mental Agility": "-3.3%/rank mana cost of instants, Smite and Holy Fire",
    "Inner Focus": "next Mind Blast free with +25% crit, every 3 min",
    "Meditation": "17%/rank of Spirit regen continues while casting",
    "Improved Inner Fire": "+15%/rank Inner Fire armor and +4 charges",
    "Mental Strength": "+3%/rank Intellect",
    "Soul Warding": "Power Word: Shield -15% mana",
    "Silent Resolve": "threat only",
    "Shadow Affinity": "threat only",
    "Improved Fade": "threat only",
    "Silence": "interrupts a casting mob and locks it out for 5 s (caster mobs: tables.MOB_CASTER_SHARE)",
    "Improved Mana Burn": "casters only (none here)",
    "Holy Precision": "+6%/rank Holy hit (Smite before 20)",
    "Twilight Focus": "23%/rank chance to ignore pushback",
    "Improved Renew": "+5%/rank Renew",
    "Holy Specialization": "+1%/rank Holy crit",
    "Divine Fury": "-0.1s/rank Smite, Holy Fire, Heal, Greater Heal cast time",
    "Spiritual Guidance": "spell damage +1.6%/rank of Spirit, healing +5%/rank of Spirit",
    "Spiritual Healing": "+3.3%/rank healing",
    "Improved Healing": "-5%/rank mana on Heal / Greater Heal",
    "Searing Light": "+2.5%/rank Holy damage",
    "Spell Warding": "-2%/rank spell damage taken (no caster mobs here)",
}
FIT = {
    "Mind Flay": ("replace", [{"channel": "dmg", "scope": ["type:spell"], "values": [0.15]}]),
    "Shadow Focus": ("replace", [{"channel": "hit", "scope": ["school:shadow"], "per_rank": 0.01}, {"channel": "dmg", "scope": ["school:shadow"], "per_rank": 0.005}]),
    "Blackout": ("replace", [{"channel": "surv", "scope": ["all"], "per_rank": 0.02}, {"channel": "dmg", "scope": ["school:shadow"], "per_rank": 0.005}]),
    "Vampiric Embrace": ("replace", [{"channel": "sustain", "scope": ["all"], "values": [0.15]}, {"channel": "surv", "scope": ["all"], "values": [0.10]}]),
    "Spirit Tap": "scale", "Shadowform": "scale", "Improved Mind Flay": "scale", "Shadow Weaving": "scale", "Improved Shadow Word: Pain": "scale",
    "Improved Mind Blast": "scale", "Darkness": "scale", "Twin Disciplines": "scale", "Silence": "scale", "Wand Specialization": "scale", "Meditation": "scale",
    "Improved Power Word: Shield": "scale", "Martyrdom": "scale", "Inner Focus": "scale", "Mental Strength": "scale", "Spiritual Guidance": "scale",
    "Twilight Focus": "scale", "Improved Psychic Scream": "scale", "Early Demise": "scale", "Devouring Contagion": "scale", "Shadow Reach": "scale",
    "Mental Agility": "scale", "Soul Warding": "scale", "Improved Renew": "scale", "Improved Inner Fire": "scale", "Holy Specialization": "scale",
    "Divine Fury": "scale", "Searing Light": "scale", "Holy Precision": "scale", "Spiritual Healing": "scale",
}
SHARE_SOURCE = {'Holy Nova': 'holy_nova', "Shadow Word: Pain": "swp", "Mind Blast": "mind_blast", "Mind Flay": "mind_flay", "Wand": "wand", "Smite": "smite",
                "Devouring Plague": "devouring_plague", "Shadow Word: Death": "swd"}
NEW_SOURCES = {'holy_nova': {'id': 'holy_nova', 'share': 0.0, 'min_level': 20, 'tags': ['type:spell', 'school:holy', 'instant', 'aoe', 'ability:Holy Nova']}, "devouring_plague": {"id": "devouring_plague", "share": 0.0, "min_level": 20, "tags": ["type:spell", "school:shadow", "dot", "instant", "ability:Devouring Plague"], "cooldown": 60},
               "swd": {"id": "swd", "share": 0.0, "min_level": 32, "tags": ["type:spell", "school:shadow", "instant", "ability:Shadow Word: Death"], "cooldown": 15}}
KEY_TALENTS = ["Mind Flay", "Shadowform", "Vampiric Embrace"]
DESCRIPTION = ("Single-target leveling fights against normal mobs of your level: Power Word: Shield and Inner Fire before the pull, Mind Blast at 30 yd, "
               "Shadow Word: Pain, Mind Flay channels (50% slow) and Mind Blast on cooldown while the mob walks in and once it is on you (the shield "
               "stops pushback while it holds), Vampiric Embrace and Devouring Plague heal, Shadow Word: Death below 20%, wand to finish without overkill; "
               "Psychic Scream and Desperate Prayer when health runs low. Between fights: 2 s loot, 6 s travel, Renew (not in Shadowform), conjured water "
               "below 35% mana, food below 65% health; a death costs 90 s.")
NOT_MODELLED = "runners, adds, Mind Soothe, Fade, Holy Nova, Penance, Prayer of Mending, Power Infusion, gear upgrades within a level bracket."
# rebuild.py: which scorer model, hand draft and optimizer build the pipeline calibrates, races and reports for this class
PIPELINE = {"variants": [{'spec': 'shadow-dps', 'opt': 'opt-shadow-dps-leveling-aoe', 'tag': 'aoe', 'profile': 'leveling-aoe', 'lookahead': 16, 'sets': ['MOBS_PER_PULL=3'], 'levels': '30,40,50,60', 'calibrate_levels': '40,60', 'label': 'AoE grinding, 3 mobs per pull'}], "spec": "shadow-dps", "hand": "leveling-shadow", "opt": "opt-shadow-dps-leveling-st", "tag": "shadow", "lookahead": 16,
            "levels": "20,30,40,50,60", "calibrate_levels": "30,60"}


class PriestModule(BaseModule):
    resource = "mana"
    special_stat = None
    WAND_BELOW = 0.0      # wand instead of Mind Flay when mana is below this fraction (APL knob, tested in the sim)
    SHIELD_BELOW = 0.0    # Power Word: Shield before the pull only when health is below this fraction (0 = always)
    ROTATION_KNOBS = {"WAND_BELOW": [0.0, 0.1, 0.2, 0.3], "SHIELD_BELOW": [0.0, 0.5, 0.8]}   # tuned by rotation_opt.py

    AOE = {'direct': ['Holy Nova'], 'dots': ['Shadow Word: Pain'], 'min_near': 2}

    def __init__(self, talents, level, spec="shadow-dps", gear="leveling"):
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
        self.armor_spell_used = "Inner Fire" if "Inner Fire" in self.spells else "none"

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
        base = class_base_stats("priest", level)
        g = gear_stats(level, self.gear, "priest")
        intellect = (base["intellect"] + g["intellect"]) * (1 + self.tv("Mental Strength", 0) / 100)
        spirit = base["spirit"] + g["spirit"]
        ds = self.book.get("Divine Spirit")
        if ds is not None:
            spirit += _num(NUM.search(ds.text.split("Spirit by")[1]).group(1))
        stamina = base["stamina"] + g["stamina"]
        pwf = self.book.get("Power Word: Fortitude")
        if pwf is not None:
            stamina += _num(NUM.search(pwf.text.split("Stamina by")[1]).group(1))
        armor = g["armor"]
        inner = self.book.get("Inner Fire")
        self.inner_fire_armor = inner.armor * (1 + self.tv("Improved Inner Fire", 0) / 100) if inner else 0.0
        self.inner_fire_charges = 20 + int(self.tv("Improved Inner Fire", 1)) if inner else 0
        sp = g["spell_power"] + spirit * self.tv("Spiritual Guidance", 1) / 100
        bm = class_base_mana("priest", level)
        p = Player(level=level, hp_max=class_base_health("priest", level) + 10 * stamina, hp=0.0, mana_max=bm + 15 * intellect, mana=0.0,
                   base_mana=bm, spirit=spirit, intellect=intellect, spell_power=sp, armor=armor,
                   spell_crit=class_spell_crit("priest", level, intellect), dodge=0.04, ranged_crit=0.03)
        p.hp, p.mana = p.hp_max, p.mana_max
        p.regen_while_casting = self.tv("Meditation", 0) / 100
        self.base_regen_while_casting = p.regen_while_casting
        p.buffs["Inner Fire"] = {"until": 1e18, "charges": 0}
        return p

    def pull_range(self):
        mb = self.spells.get("Mind Blast") or self.spells.get("Smite")
        base = mb.range if mb and mb.range else 30.0
        return base * (1 + self.tv("Shadow Reach", 0) / 100)

    def in_shadowform(self):
        return bool(self.rank("Shadowform") and "Shadowform" in self.spells)

    # ------------------------------------------------------------ engine hooks: numbers
    def cast_time(self, spell):
        c = spell.cast
        if spell.name in ("Smite", "Holy Fire", "Heal", "Greater Heal"):
            c = max(GCD, c - 0.1 * self.rank("Divine Fury"))
        return c

    def mana_cost(self, spell):
        cost = spell.cost
        if "cost_pct" in spell.tags:
            cost = cost / 100 * self._base_mana
        if spell.school == "shadow" and self.in_shadowform():
            cost *= 0.5
        if spell.name == "Devouring Plague":
            cost *= 1 - self.tv("Devouring Contagion", 0) / 100
        if spell.name == "Power Word: Shield" and self.rank("Soul Warding"):
            cost *= 1 - self.tv("Soul Warding", 1) / 100
        if (spell.cast == 0 and spell.kind != "channel") or spell.name in ("Smite", "Holy Fire"):
            cost *= 1 - self.tv("Mental Agility", 0) / 100
        if spell.name in ("Heal", "Greater Heal", "Lesser Heal"):
            cost *= 1 - self.tv("Improved Healing", 0) / 100
        return cost

    def final_cost(self, fight, spell, cost):
        if fight.p.buff("Inner Focus", fight.t) and spell.dmg_max > 0:
            del fight.p.buffs["Inner Focus"]
            return 0.0
        return cost

    def hit_bonus(self, spell):
        if spell.school == "shadow":
            return self.tv("Shadow Focus", 0) / 100
        if spell.school == "holy":
            return self.tv("Holy Precision", 0) / 100
        return 0.0

    def crit_bonus(self, spell, frozen):
        c = 0.0
        f = self._fight
        if spell.school == "holy":
            c += self.tv("Holy Specialization", 0) / 100
        if spell.name == "Shadow Word: Death" and f and f.m.hp <= 0.2 * f.m.hp_max:
            c += self.tv("Early Demise", 0) / 100
        if f and f.p.buff("Inner Focus", f.t) and spell.dmg_max > 0:
            c += 0.25
        return c

    def crit_damage_bonus(self, spell):
        if spell.school == "shadow" and self.in_shadowform():
            return 0.5   # crit multiplier 1.5 -> 2.0
        return 0.0

    def damage_multiplier(self, spell, frozen):
        m = 1.0
        if spell.school == "shadow":
            m *= 1 + self.tv("Darkness", 0) / 100
            if self.in_shadowform():
                m *= 1.10
            if self._fight:
                sw = self._fight.p.buff("Shadow Weaving", self._fight.t)
                if sw:
                    m *= 1 + 0.02 * sw["stacks"]
        if spell.school == "holy":
            m *= 1 + self.tv("Searing Light", 0) / 100
        if spell.name == "Mind Flay":
            m *= 1 + 0.10 * self.rank("Improved Mind Flay")
        if spell.cast == 0 and spell.kind != "channel":
            m *= 1 + self.tv("Twin Disciplines", 0) / 100
        return m

    def heal_multiplier(self, spell):
        m = 1 + self.tv("Spiritual Healing", 0) / 100
        if spell.name == "Renew":
            m *= 1 + self.tv("Improved Renew", 0) / 100
        if spell.name == "Power Word: Shield":
            m *= 1 + self.tv("Improved Power Word: Shield", 0) / 100
        if spell.cast == 0:
            m *= 1 + self.tv("Twin Disciplines", 0) / 100
        return m

    def periodic_can_crit(self, spell):
        return True   # Forever: periodic damage can crit (wowsims Forever OutcomeTickMagicCrit; the scorer's shadow model says so too)

    def chill_duration_bonus(self):
        return 0.0

    def armor_bonus(self):
        f = self._fight
        if f is None:
            return 0.0
        b = f.p.buffs.get("Inner Fire")
        return self.inner_fire_armor if b and b.get("charges", 0) > 0 else 0.0

    def wand_damage(self):
        return wand_dps(self.level) * WAND_SPEED * (1 + self.tv("Wand Specialization", 0) / 100)

    def pushback_resisted(self, fight, spell):
        if fight.p.buff("Focused Casting", fight.t):
            return True
        if self.rank("Twilight Focus"):
            return fight.rng.random() < self.tv("Twilight Focus", 0) / 100
        return False

    def mana_regen(self, p, t):
        spirit = p.spirit
        st = p.buff("Spirit Tap", t)
        if st:
            spirit *= 2.0
            p.regen_while_casting = max(self.base_regen_while_casting, 0.5)
        elif p.regen_while_casting != self.base_regen_while_casting:
            p.regen_while_casting = self.base_regen_while_casting
        return class_mana_regen_tick("priest", spirit)

    def health_regen(self, p):
        return class_health_regen_tick("priest", p.spirit)

    # ------------------------------------------------------------ engine hooks: events
    def on_fight_start(self, fight):
        self._fight = fight
        self._base_mana = fight.p.base_mana
        p, t = fight.p, fight.t
        # Inner Fire: re-apply when its charges are used up (10 min otherwise)
        inner = self.spells.get("Inner Fire")
        b = p.buffs.get("Inner Fire")
        if inner is not None and (b is None or b.get("charges", 0) <= 0) and p.mana >= inner.cost + 100:
            p.mana -= inner.cost
            p.buffs["Inner Fire"] = {"until": 1e18, "charges": self.inner_fire_charges}
        # Power Word: Shield before the pull (Weakened Soul 15 s lockout)
        pws = self.spells.get("Power Word: Shield")
        if pws is not None and p.ready("Power Word: Shield", t) and p.mana >= self.mana_cost(pws) + 150 and (self.SHIELD_BELOW <= 0 or p.hp < self.SHIELD_BELOW * p.hp_max):
            self.cast_shield(fight, pws)
        if self.rank("Inner Focus") and p.ready("Inner Focus", t):
            p.buffs["Inner Focus"] = {"until": t + 30.0}
            p.cooldowns["Inner Focus"] = t + 180.0

    def cast_shield(self, fight, pws):
        p, t = fight.p, fight.t
        p.mana -= self.mana_cost(pws)
        p.fsr_until = t + 5.0
        p.absorb, p.absorb_until = pws.absorb * self.heal_multiplier(pws), t + 30.0
        p.cooldowns["Power Word: Shield"] = t + 15.0
        fight.casts["Power Word: Shield"] = fight.casts.get("Power Word: Shield", 0) + 1
        fight.note(f"Power Word: Shield ({p.absorb:.0f})")

    def on_hit(self, fight, spell, amount, crit, frozen):
        p, m, t, rng = fight.p, fight.m, fight.t, fight.rng
        if spell.name == "Vampiric Embrace":
            m.debuffs["Vampiric Embrace"] = {"until": t + 30.0, "stacks": 1}
            return
        if spell.school == "shadow" and (amount > 0 or spell.dot > 0):
            self.shadow_hit(fight, spell, amount)
        if spell.name == "Shadow Word: Death" and m.hp > 0:
            back = 0.10 * p.hp_max
            p.hp -= back
            fight.note(f"Shadow Word: Death backlash {back:.0f}")

    def shadow_hit(self, fight, spell, amount):
        p, m, t, rng = fight.p, fight.m, fight.t, fight.rng
        if spell.school == "shadow" and self.rank("Shadow Weaving") and rng.random() < self.tv("Shadow Weaving", 0) / 100:
            b = p.buffs.get("Shadow Weaving")
            stacks = min(5, (b["stacks"] if b and b["until"] > t else 0) + 1)
            p.buffs["Shadow Weaving"] = {"until": t + 15.0, "stacks": stacks}
        if amount > 0:
            if self.rank("Blackout") and not m.stunned(t) and rng.random() < self.tv("Blackout", 0) / 100:
                m.stun_until = t + 3.0
                fight.note("Blackout stun")
            ve = m.debuffs.get("Vampiric Embrace")
            if ve and ve["until"] > t:
                fight.heal(Spell("Vampiric Embrace", "shadow"), 0.20 * amount)
            if spell.name.startswith("Devouring Plague"):
                fight.heal(Spell("Devouring Plague heal", "shadow"), amount)

    def on_tick(self, fight, spell, amount, crit):
        if amount > 0 and spell.school in ("shadow", "periodic") and spell.name not in ("Holy Fire",):
            self.shadow_hit(fight, spell, amount)

    def after_cast(self, fight, spell):
        p, t = fight.p, fight.t
        cd = spell.cooldown
        if spell.name == "Mind Blast":
            cd = max(0.0, cd - self.tv("Improved Mind Blast", 0))
        if spell.name == "Psychic Scream":
            cd = max(0.0, cd - self.tv("Improved Psychic Scream", 0))
        if spell.name == "Power Word: Shield":
            cd = 15.0
        if cd > 0:
            p.cooldowns[spell.name] = t + cd

    def on_hit_taken(self, fight, dmg, crit=False):
        p, t = fight.p, fight.t
        b = p.buffs.get("Inner Fire")
        if b and b.get("charges", 0) > 0:
            b["charges"] -= 1
        if crit and self.rank("Martyrdom"):
            p.buffs["Focused Casting"] = {"until": t + 6.0}

    def on_kill(self, fight):
        p, t = fight.p, fight.t
        if self.rank("Spirit Tap") and fight.rng.random() < self.tv("Spirit Tap", 0) / 100:
            p.buffs["Spirit Tap"] = {"until": t + 15.0}

    def after_fight(self, p, t):
        """Renew after a fight when hurt and allowed (Shadowform forbids heals): instant, ticks during loot and travel."""
        if self.in_shadowform() or p.hp >= 0.85 * p.hp_max:
            return 0.0
        renew = self.spells.get("Renew")
        if renew is None or p.mana < self.mana_cost(renew) + 100:
            return 0.0
        p.mana -= self.mana_cost(renew)
        total = (renew.hot + renew.heal_coef * p.spell_power * 5) * self.heal_multiplier(renew)
        p.hp = min(p.hp_max, p.hp + total)
        return 1.5

    # ------------------------------------------------------------ priority list
    def decide(self, fight):
        if fight.others():   # a pull of several mobs: the area priority first (engine.BaseModule.decide_aoe, AOE below)
            r = self.decide_aoe(fight)
            if r is not None:
                return r
        p, m, t = fight.p, fight.m, fight.t
        sp = self.spells
        in_melee = m.in_melee and m.dist <= MELEE_RANGE + 0.5

        def avg(s):
            return (s.dmg_min + s.dmg_max) / 2 + s.coef * p.spell_power if s else 0.0

        def can(s):
            return s is not None and p.ready(s.name, t) and fight.can_afford(s, self.mana_cost(s))

        swp, blast, flay, smite, swd, dp, ve, scream, wand_hit = (sp.get("Shadow Word: Pain"), sp.get("Mind Blast"), sp.get("Mind Flay"), sp.get("Smite"),
                                                                  sp.get("Shadow Word: Death"), sp.get("Devouring Plague"), sp.get("Vampiric Embrace"),
                                                                  sp.get("Psychic Scream"), self.wand_damage() * 0.65)
        hp = m.hp
        # emergencies
        if p.hp < 0.30 * p.hp_max:
            dpr = sp.get("Desperate Prayer")
            if dpr and can(dpr):
                return dpr
        if p.hp < 0.40 * p.hp_max and in_melee and scream and can(scream) and hp > 0.25 * m.hp_max and not m.incapacitated(t):
            return scream
        if p.hp < 0.35 * p.hp_max and not self.in_shadowform():
            fh = sp.get("Flash Heal") or sp.get("Lesser Heal")
            if fh and can(fh) and (p.absorb > 0 and t < p.absorb_until or not in_melee):
                return fh
        # a casting mob: Silence it
        sil = sp.get("Silence")
        if m.caster and m.casting(t) and sil and can(sil) and m.dist <= sil.range:
            return sil
        # finishers without overkill
        if swd and can(swd) and hp <= avg(swd) * 0.9:
            return swd
        if blast and can(blast) and hp <= avg(blast) * 0.9 and hp > wand_hit * 2.5:
            return blast
        if hp <= wand_hit * 1.5:
            return "wand"
        # self-healing debuffs
        if ve and can(ve) and not (m.debuffs.get("Vampiric Embrace", {}).get("until", 0) > t) and hp > 0.35 * m.hp_max:
            return ve
        if dp and can(dp) and not fight.dot_active("Devouring Plague") and hp > 0.5 * m.hp_max and p.hp < 0.8 * p.hp_max:
            return dp
        # the loop
        if swp and can(swp) and not fight.dot_active("Shadow Word: Pain") and hp > 0.30 * m.hp_max:
            return swp
        if swd and can(swd) and hp <= 0.2 * m.hp_max and self.rank("Early Demise"):
            return swd
        if blast and can(blast):
            return blast
        if flay and can(flay) and hp > wand_hit * 3 and m.dist <= flay.range + 5.0 * self.rank("Improved Mind Flay") and p.mana >= self.WAND_BELOW * p.mana_max:
            return flay
        if smite and can(smite) and not in_melee and hp > avg(smite):
            return smite
        if smite and can(smite) and flay is None and (p.absorb > 0 and t < p.absorb_until):
            return smite
        return "wand"
