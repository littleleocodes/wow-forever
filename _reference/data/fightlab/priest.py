"""Priest module for the fight lab (Shadow leveling).

Spell ranks (damage, periodic damage, heals, absorbs, cost, cast, cooldown, coefficients) are read from
`_reference/data/forever-spells/priest.json` (the beta client build named in that file); talent numbers from each rank's tooltip in
`_reference/data/forever-talents/priest.json`. What a talent *does* is coded here per talent; the numbers are the client's.

Playstyle `shadow-dps` (the scorer's model id): Power Word: Shield and Inner Fire before the pull, Mind Blast at range,
Shadow Word: Pain, Mind Flay channels (slowing the mob) and Mind Blast on cooldown, Vampiric Embrace for self-healing,
Devouring Plague (client 70425: a 24 s cooldown dot that heals you for its damage) first when hurt, then as a damage line after
Shadow Word: Pain (2026-10-17, page audit finding 16: it had been cast only below 80% health; the tuned rules gate it), Shadow
Word: Death as an execute, wand to finish without overkill; Psychic Scream when health runs low; Renew between fights until
Shadowform (which forbids heals) replaces it with eating. Forever's racial priest spells (Desperate Prayer is a Dwarf's) are
cast only for their race (RACIAL_SPELLS, PriestModule.RACE; 2026-10-09: none, the pages are race-neutral).

Playstyles `holy-leveling` and `discipline-leveling` (any spec string starting with "holy" or "discipline"; 2026-09-30): the
healing trees leveling on Smite. One priority list for both (`decide_holy`); the talents make the difference: shield before the
pull, Holy Fire as the opener, Shadow Word: Pain, Penance on cooldown (Forever's Penance damages an enemy), Mind Blast on cooldown,
Smite as the filler, wand to finish; Power Word: Shield again, Renew and Flash Heal when hurt. Talent effects only these playstyles
apply: see HOLY_MECHANICS (the Shadow playstyle keeps MECHANICS and its behaviour as it was).
"""
import copy
import json
import pathlib
import re

from engine import parse_interrupt, BaseModule, Player, Spell
from tables import (GCD, MELEE_RANGE, WAND_SPEED, class_base_health, class_base_mana, class_base_stats, class_health_regen_tick,
                    class_mana_regen_tick, class_spell_crit, gear_stats, wand_dps)

ROOT = pathlib.Path(__file__).resolve().parents[3]
SPELLBOOK = json.load(open(ROOT / "_reference/data/forever-spells/priest.json", encoding="utf-8"))
TREE = json.load(open(ROOT / "_reference/data/forever-talents/priest.json", encoding="utf-8"))
# Mental Agility's "instant cast spells" (tooltip) as the client's class mask 14520 reads in the community simulator
# (sim/priest/talents_discipline.go at db4d14a): channels and Shadow Word: Death pay full price; Devouring Plague does not.
MENTAL_AGILITY_EXCLUDED = ("Shadow Word: Death",)
# Inner Focus's crit leaves out Mind Flay and Shadow Word: Death (14751's crit modifier mask, same source); periodic effects never get it
INNER_FOCUS_NO_CRIT = ("Mind Flay", "Shadow Word: Death")

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
DOT_TICKS = {"Holy Fire": 5}   # Holy Fire's burn ticks every 2 s for 10 s (the tooltip gives only the total and the duration)
PENANCE = re.compile(r"causing (\d[\d,]*) Holy damage to an enemy")
SELF_ONLY = {"Renew", "Flash Heal", "Lesser Heal", "Heal", "Greater Heal", "Power Word: Shield", "Desperate Prayer", "Binding Heal"}
# Forever's racial priest spells (talentsforever.com's 70291 export, class_racials; Blizzard's 2026-10-08 notes list Dark Sacrifice under
# Undead). The player pages are race-neutral, so a racial spell is cast only when PriestModule.RACE names its race (default: none).
RACIAL_SPELLS = {"Divine Grace": "Human", "Feedback": "Human", "Chastise": "Dwarf", "Desperate Prayer": "Dwarf", "Elune's Grace": "Night Elf",
                 "Starshards": "Night Elf", "Confounding Flash": "Gnome", "Contingency Plan": "Gnome", "Dark Sacrifice": "Undead",
                 "Touch of Weakness": "Undead", "Hex of Weakness": "Troll", "Shadowguard": "Troll"}


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
                cost_txt = (r.get("cost") or "").replace(",", "")   # "1,070 Mana" read as 1 before 2026-10-18 (audit #30)
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
                    s.dot_ticks = CHANNEL_TICKS.get(sp["name"], DOT_TICKS.get(sp["name"], max(1, int(round(s.dot_dur / 3.0)))))
                    s.dot_coef = coefs.get("per tick", 0.0)
                if channel:
                    s.kind = "channel"
                    s.channel = s.dot_dur or 3.0
                pn = PENANCE.search(txt) if sp["name"] == "Penance" else None
                if pn:   # "causing N Holy damage to an enemy ... instantly and every 1 sec for 2 sec": three hits over a 2 s channel
                    s.dot, s.dot_dur, s.dot_ticks = 3 * _num(pn.group(1)), 2.0, 3
                    s.dot_coef, s.channel = coefs.get("per tick", 0.0), 2.0
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
# Shadowform's "reducing Physical damage taken by you by 15%" (the spell's own tooltip; applied through armor_bonus below)
_SF = (BOOK.get("Shadowform") or [None])[0]
_SF_PHYS = re.search(r"[Pp]hysical damage taken by you by (\d+)%", getattr(_SF, "text", "") or "")
SHADOWFORM_PHYSICAL_CUT = float(_SF_PHYS.group(1)) / 100 if _SF_PHYS else 0.0


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
    "Improved Shadow Word: Pain": "+3s (one tick) per rank on Shadow Word: Pain (the tooltip's seconds)",
    "Shadow Reach": "+10%/rank Shadow range: longer pulls and a longer Mind Flay reach",
    "Improved Mind Blast": "-0.5s/rank Mind Blast cooldown",
    "Improved Psychic Scream": "-2s/rank Psychic Scream cooldown",
    "Mind Flay": "unlocks Mind Flay (3s channel, 3 ticks, 50% slow)",
    "Improved Mind Flay": "each Mind Flay tick deals 10%/rank more than the one before it in the same channel (client 70425; compounding: 1, 1.2, 1.44 at 2/2; was +10%/rank, range and a weaker slow)",
    "Vampiric Embrace": "20% of Shadow damage dealt heals you for 30s (30 s cooldown since client 70425, 40 mana)",
    "Shadow Weaving": "33%/rank chance per Shadow hit: +2% Shadow damage the target takes from you per stack (5 stacks, 15s; a debuff on the mob since client 70425, so the stacks start over on every mob)",
    "Dark Inspiration": "+3%/rank Spirit (mana regeneration) for 10 s after a Mind Blast hit or a fully channelled Mind Flay (client 70425; its party share does nothing solo)",
    "Devouring Contagion": "-25%/rank Devouring Plague mana cost (the spread on a kill: not modelled)",
    "Early Demise": "+15%/rank Shadow Word: Death crit below 20% health",
    "Darkness": "+2%/rank Shadow damage",
    "Shadowform": "+10% Shadow damage, -50% Shadow mana cost, Shadow crits x2.0, -15% physical damage taken, no heals",
    "Wand Specialization": "+13/25% wand damage",
    "Twin Disciplines": "+1%/rank damage and healing of instant casts, Mind Flay and Penance included (16 Oct beta notes; forever-bugs #322, #328)",
    "Improved Power Word: Shield": "+7/14/20% absorb",
    "Martyrdom": "Focused Casting for 6s after a melee crit: no pushback",
    "Mental Agility": "-3.3%/rank mana cost of instants, Smite and Holy Fire; not channels (Mind Flay, Penance) or Shadow Word: Death (the client's "
                      "class mask 14520 as the community simulator reads it)",
    "Inner Focus": "used at the pull every 3 min: the next spell, whatever it is, is free and gets +25% crit if it is a non-periodic spell "
                   "(not Mind Flay or Shadow Word: Death; 2026-10-17: it had been spent by damage spells only and its crit never applied)",
    "Meditation": "17%/rank of Spirit regen continues while casting",
    "Improved Inner Fire": "+15%/rank Inner Fire armor and +4 charges",
    "Mental Strength": "+2%/rank Intellect (client 70425; was 3%)",
    "Soul Warding": "Power Word: Shield -15% mana",
    "Silent Resolve": "threat only",
    "Silence": "interrupts a casting mob and locks it out for 5 s (caster mobs: tables.MOB_CASTER_SHARE)",
    "Improved Mana Burn": "casters only (none here)",
    "Holy Precision": "+6%/rank Holy hit (Smite before 20)",
    "Twilight Focus": "23%/rank chance to ignore pushback",
    "Improved Renew": "+5%/rank Renew",
    "Holy Specialization": "+1%/rank Holy crit",
    "Divine Fury": "-0.1s/rank Smite, Holy Fire, Heal, Greater Heal cast time",
    "Spiritual Guidance": "spell damage +1.6%/rank of Spirit, healing +5%/rank of Spirit (the tooltip's two numbers; until 2026-10-17 heals "
                          "got the damage share)",
    "Spiritual Healing": "+3.3%/rank healing",
    "Improved Healing": "-5%/rank mana on Heal / Greater Heal",
    "Searing Light": "+2.5%/rank Holy damage",
    "Spell Warding": "-2%/rank spell damage taken: not modelled (caster bolts and melee share the engine's one damage-taken hook)",
}
# Talent effects the Holy / Discipline playstyles add (spec strings starting with "holy" or "discipline"); shadow-dps keeps MECHANICS.
HOLY_MECHANICS = {
    "Penance": "unlocks Penance: 3 Holy hits over a 2 s channel (tooltip: N Holy damage instantly and every 1 sec for 2 sec, the tooltip's "
               "spell power per hit), 12 s cooldown; the learned rank with the most damage is cast",
    "Power in Light": "+2%/rank Smite and Penance damage while your Holy Fire or Shadow Word: Pain burns on the mob (Shadow Word: Pain since client 70425)",
    "Power Infusion": "+20% spell damage and healing for 15 s, cast on yourself as a pull starts (3 min cooldown, 20% of base mana)",
    "Holy Reach": "+10%/rank Smite and Holy Fire range: longer pulls",
    "Blessed Recovery": "after a melee crit or a hit above 30% of your health: heal 8/16/25% of that hit over 6 s (the rest carries over)",
    "Renewed Hope": "+2%/rank crit on Flash Heal, Lesser Heal, Heal, Greater Heal, Binding Heal under Weakened Soul; each such heal "
                    "shortens Weakened Soul by 1 s/rank (the next Power Word: Shield comes sooner)",
    "Improved Healing": "-5%/rank mana on Lesser Heal, Heal, Greater Heal and Penance",
    "Spirit of Redemption": "no effect: the priest still dies",
    "Holy Nova": "area pulls only (AOE)",
    "Silent Resolve": "threat only",
    "Inspiration": "not modelled (armor after a critical non-periodic heal on yourself; rare in leveling fights)",
    "Divine Aegis": "not modelled (a 5%/rank absorb after a critical non-periodic heal, at most 1,200; rare in leveling fights)",
    "Litany of Light": "not modelled (mana back when alternating heals; leveling fights cast few heals)",
    "Binding Heal": "not cast (Flash Heal heals more per mana on yourself)",
}
RENEWED_HOPE_HEALS = ("Flash Heal", "Binding Heal", "Lesser Heal", "Heal", "Greater Heal")
HOLY_DESCRIPTION = ("Holy / Discipline leveling (spec strings holy-leveling, discipline-leveling): Power Word: Shield, Inner Fire and Power "
                    "Infusion before the pull, Holy Fire as the opener at 30 yd, Shadow Word: Pain, Penance and Mind Blast on cooldown, Smite as the "
                    "filler (in melee too: the shield stops pushback while it holds), wand to finish without overkill; Power Word: Shield again, "
                    "Renew and Flash Heal when hurt, Psychic Scream when health runs low. Between fights: Renew, conjured "
                    "water below 35% mana, food below 65% health.")
FIT = {
    "Mind Flay": ("replace", [{"channel": "dmg", "scope": ["type:spell"], "values": [0.15]}]),
    "Shadow Focus": ("replace", [{"channel": "hit", "scope": ["school:shadow"], "per_rank": 0.01}, {"channel": "dmg", "scope": ["school:shadow"], "per_rank": 0.005}]),
    "Blackout": ("replace", [{"channel": "surv", "scope": ["all"], "per_rank": 0.02}, {"channel": "dmg", "scope": ["school:shadow"], "per_rank": 0.005}]),
    "Vampiric Embrace": ("replace", [{"channel": "sustain", "scope": ["all"], "values": [0.15]}, {"channel": "surv", "scope": ["all"], "values": [0.10]}]),
    "Spirit Tap": "scale", "Shadowform": "scale", "Improved Mind Flay": "scale", "Shadow Weaving": "scale", "Improved Shadow Word: Pain": "scale",
    "Improved Mind Blast": "scale", "Darkness": "scale", "Twin Disciplines": "scale", "Silence": "scale", "Wand Specialization": "scale", "Meditation": "scale",
    "Improved Power Word: Shield": "scale", "Martyrdom": "scale", "Inner Focus": "scale", "Mental Strength": "scale", "Spiritual Guidance": "scale",
    "Twilight Focus": "scale", "Improved Psychic Scream": "scale", "Early Demise": "scale", "Devouring Contagion": "scale", "Shadow Reach": "scale", "Dark Inspiration": "scale",
    "Mental Agility": "scale", "Soul Warding": "scale", "Improved Renew": "scale", "Improved Inner Fire": "scale", "Holy Specialization": "scale",
    "Divine Fury": "scale", "Searing Light": "scale", "Holy Precision": "scale", "Spiritual Healing": "scale",
}
SHARE_SOURCE = {'Holy Nova': 'holy_nova', "Shadow Word: Pain": "swp", "Mind Blast": "mind_blast", "Mind Flay": "mind_flay", "Wand": "wand", "Smite": "smite",
                "Devouring Plague": "devouring_plague", "Shadow Word: Death": "swd"}
NEW_SOURCES = {'holy_nova': {'id': 'holy_nova', 'share': 0.0, 'min_level': 20, 'tags': ['type:spell', 'school:holy', 'instant', 'aoe', 'ability:Holy Nova']}, "devouring_plague": {"id": "devouring_plague", "share": 0.0, "min_level": 20, "tags": ["type:spell", "school:shadow", "dot", "instant", "ability:Devouring Plague"], "cooldown": 24},
               "swd": {"id": "swd", "share": 0.0, "min_level": 32, "tags": ["type:spell", "school:shadow", "instant", "ability:Shadow Word: Death"], "cooldown": 18}}
KEY_TALENTS = ["Mind Flay", "Shadowform", "Vampiric Embrace"]
DESCRIPTION = ("Single-target leveling fights against normal mobs of your level: Power Word: Shield and Inner Fire before the pull, Mind Blast at 30 yd, "
               "Shadow Word: Pain, Mind Flay channels (50% slow) and Mind Blast on cooldown while the mob walks in and once it is on you (the shield "
               "stops pushback while it holds), Vampiric Embrace and Devouring Plague heal, Shadow Word: Death below 20%, wand to finish without overkill; "
               "Psychic Scream when health runs low. Between fights: 2 s loot, 6 s travel, Renew (not in Shadowform), conjured water "
               "below 35% mana, food below 65% health; a death costs 90 s.")
NOT_MODELLED = ("runners, adds, Mind Soothe, Fade, Holy Nova, Penance, Prayer of Mending, Power Infusion, gear upgrades within a level bracket; "
                "racial priest spells (Desperate Prayer is a Dwarf's: off on the race-neutral pages).")
# rebuild.py: which scorer model, hand draft and optimizer build the pipeline calibrates, races and reports for this class
PIPELINE = {"variants": [{'spec': 'shadow-dps', 'opt': 'opt-shadow-dps-leveling-aoe', 'tag': 'aoe', 'profile': 'leveling-aoe', 'lookahead': 16, 'sets': ['MOBS_PER_PULL=3'], 'levels': '30,40,50,60', 'calibrate_levels': '40,60', 'label': 'AoE grinding, 3 mobs per pull'}], "spec": "shadow-dps", "hand": "leveling-shadow", "opt": "opt-shadow-dps-leveling-st", "tag": "shadow", "lookahead": 16,
            "levels": "20,30,40,50,60", "calibrate_levels": "30,60"}


class PriestModule(BaseModule):
    resource = "mana"
    special_stat = None
    WAND_BELOW = 0.0      # wand instead of Mind Flay when mana is below this fraction (APL knob, tested in the sim)
    SHIELD_BELOW = 0.0    # Power Word: Shield before the pull only when health is below this fraction (0 = always)
    ROTATION_KNOBS = {"WAND_BELOW": [0.0, 0.1, 0.2, 0.3], "SHIELD_BELOW": [0.0, 0.5, 0.8]}   # tuned by rotation_opt.py
    RACE = None           # racial priest spells (RACIAL_SPELLS) only for this race; None = race-neutral (the player pages)

    AOE = {'direct': ['Holy Nova'], 'dots': ['Shadow Word: Pain'], 'min_near': 2}

    def __init__(self, talents, level, spec="shadow-dps", gear="leveling"):
        self.t = {k: v for k, v in talents.items() if v > 0}
        self.level = level
        self.spec = spec
        self.gear = gear
        self.holy = spec.startswith(("holy", "discipline"))
        self.book = {name: self.rank_at(name) for name in BOOK}
        if self.holy and self.book.get("Penance") is not None:   # the learned rank with the most damage (an earlier beta's rank 4 hit for less)
            self.book["Penance"] = self.scale_rank(max((s for s in BOOK["Penance"] if s.level <= level), key=lambda s: (s.dot, s.level)))
        self.spells = {n: s for n, s in self.book.items() if s is not None}
        for tname, sname in TALENT_SPELLS.items():
            if not self.t.get(tname):
                self.spells.pop(sname, None)
        for sname, race in RACIAL_SPELLS.items():   # race-neutral by default: Desperate Prayer and the other racial spells only for their race
            if race != self.RACE:
                self.spells.pop(sname, None)
        swp, extra = self.spells.get("Shadow Word: Pain"), self.tv("Improved Shadow Word: Pain", 0)
        if swp is not None and extra > 0 and swp.dot_ticks:   # Improved Shadow Word: Pain: the tooltip's seconds, one more tick per 3 s
            every = swp.dot_dur / swp.dot_ticks
            add = int(round(extra / every))
            s = copy.copy(swp)   # a copy: the shared BOOK spell stays as the client lists it
            s.dot, s.dot_dur, s.dot_ticks = swp.dot * (swp.dot_ticks + add) / swp.dot_ticks, swp.dot_dur + add * every, swp.dot_ticks + add
            self.spells["Shadow Word: Pain"] = s
        self._fight = None
        self._flay_i, self._flay_t = -1, None   # the current Mind Flay channel's tick count (flay_ramp)
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

    def is_holy(self):
        return self.holy

    def not_simulated(self):
        known = {**MECHANICS, **HOLY_MECHANICS} if self.holy else MECHANICS
        return sorted(n for n in self.t if n not in known)

    def rank_at(self, name):
        ranks = [s for s in BOOK.get(name, []) if s.level <= self.level]
        return self.scale_rank(ranks[-1]) if ranks else None   # the rank at this level (row 8)

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
        if self.holy:   # the Holy Fire / Smite opener, Holy Reach extends it
            hf = self.spells.get("Holy Fire") or self.spells.get("Smite")
            base = hf.range if hf and hf.range else 30.0
            return base * (1 + self.tv("Holy Reach", 0) / 100)
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
        if (spell.cast == 0 and spell.kind != "channel" and spell.name not in MENTAL_AGILITY_EXCLUDED) or spell.name in ("Smite", "Holy Fire"):
            cost *= 1 - self.tv("Mental Agility", 0) / 100
        if spell.name in ("Heal", "Greater Heal", "Lesser Heal"):
            cost *= 1 - self.tv("Improved Healing", 0) / 100
        if self.holy and spell.name == "Penance":
            cost *= 1 - self.tv("Improved Healing", 0) / 100
        return cost

    def final_cost(self, fight, spell, cost):
        """Inner Focus: the next spell is free (any spell: the tooltip's "your next spell"; the community simulator spends it on the next
        priest spell). The buff is marked spent here and removed in after_cast, so crit_bonus still sees it while that spell resolves
        (until 2026-10-17 it was deleted here, before the spell resolved, and its crit never applied)."""
        b = fight.p.buff("Inner Focus", fight.t)
        if b and not b.get("spent"):
            b["spent"] = spell.name
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
            c += self.tv("Early Demise", 1) / 100   # index 1: the crit (15/30); index 0 is the 20% health threshold (audit 2026-10-18 #32)
        b = f.p.buff("Inner Focus", f.t) if f else None
        if (b and b.get("spent") == spell.name and not b.get("crit_used") and spell.name not in INNER_FOCUS_NO_CRIT
                and (spell.dmg_max > 0 or spell.heal_max > 0)):
            c += 0.25   # the spell that spent it, non-periodic part (notes post 4: "no longer applies ... to Periodic Effects")
            b["crit_used"] = True   # the direct roll comes first; Holy Fire's burn snapshots its crit right after (audit 2026-10-18 #23)
        if self.holy and f and spell.name in RENEWED_HOPE_HEALS and f.p.cooldowns.get("Power Word: Shield", 0.0) > f.t:
            c += self.tv("Renewed Hope", 0) / 100   # the target (you) is under Weakened Soul
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
                sw = self._fight.m.debuffs.get("Shadow Weaving")   # a debuff on the mob since client 70425 (was a buff on you)
                if sw and sw["until"] > self._fight.t:
                    m *= 1 + 0.02 * sw["stacks"]
        if spell.school == "holy":
            m *= 1 + self.tv("Searing Light", 0) / 100
        if spell.name == "Mind Flay":
            m *= self.flay_ramp()
        # Twin Disciplines: instant casts, and since the 16 Oct beta notes Mind Flay and Penance (the devs called their absence a bug:
        # forever-bugs #322, #328)
        if (spell.cast == 0 and spell.kind != "channel") or spell.name in ("Mind Flay", "Penance"):
            m *= 1 + self.tv("Twin Disciplines", 0) / 100
        if self.holy and self._fight:
            f = self._fight
            if spell.name in ("Smite", "Penance") and (f.dot_active("Holy Fire") or f.dot_active("Shadow Word: Pain")):   # SW:P: 70425
                m *= 1 + self.tv("Power in Light", 0) / 100
            if f.p.buff("Power Infusion", f.t):
                m *= 1.20
        return m

    def _sg_heal_factor(self, spell):
        """Spiritual Guidance gives healing the tooltip's first share of Spirit (25% at 5/5) and spell damage the second (8%); the player's
        spell power carries the damage share, so a heal gets the rest as a factor on its mean amount (the engine adds one spell power to
        both)."""
        f = self._fight
        if f is None or not self.rank("Spiritual Guidance"):
            return 1.0
        extra = f.p.spirit * (self.tv("Spiritual Guidance", 0) - self.tv("Spiritual Guidance", 1)) / 100
        if extra <= 0 or spell.heal_coef <= 0:
            return 1.0
        sp = f.p.spell_power
        if spell.hot > 0 and spell.heal_max <= 0:
            ticks = max(1, int(spell.hot_dur / 3.0))
            base = spell.hot + spell.heal_coef * sp * ticks
            return (base + spell.heal_coef * extra * ticks) / base if base > 0 else 1.0
        base = (spell.heal_min + spell.heal_max) / 2 + spell.heal_coef * sp
        return (base + spell.heal_coef * extra) / base if base > 0 else 1.0

    def heal_multiplier(self, spell):
        m = self._sg_heal_factor(spell)
        m *= 1 + self.tv("Spiritual Healing", 0) / 100
        if self.holy and self._fight and self._fight.p.buff("Power Infusion", self._fight.t):
            m *= 1.20
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

    def chill_extra_slow(self):
        return 0.0   # client 70425: Improved Mind Flay no longer changes Mind Flay's slow (it had weakened it to 35% / 20%)

    def flay_range(self, flay):
        """Mind Flay's reach: the spell's 20 yd and Shadow Reach's percentage (offensive Shadow spells); Improved Mind Flay's 10 yards
        are gone in client 70425."""
        return flay.range * (1 + self.tv("Shadow Reach", 0) / 100)

    def flay_ramp(self):
        """Improved Mind Flay (client 70425): "Each instance of damage of Mind Flay deals 20% more damage than its previous instance", read
        as compounding (1, 1.2, 1.44 at 2/2). The tick's place is counted per channel (pushback drops ticks from the end, so the ticks
        left do not give it): the first call at a new tick time while a Mind Flay channel is due moves the count on; the extra mobs of an
        area pull take the same tick's factor. Outside a tick (estimates) the next tick's factor is returned without counting."""
        r = self.tv("Improved Mind Flay", 0) / 100
        f = self._fight
        if not r or f is None:
            return 1.0
        ch = f.channel
        if ch and ch[0].name == "Mind Flay" and f.t >= ch[1] - 1e-9 and f.t != self._flay_t:
            self._flay_t = f.t
            self._flay_i += 1
        return (1 + r) ** max(0, self._flay_i)

    def armor_bonus(self):
        f = self._fight
        if f is None:
            return 0.0
        b = f.p.buffs.get("Inner Fire")
        bonus = self.inner_fire_armor if b and b.get("charges", 0) > 0 else 0.0
        if SHADOWFORM_PHYSICAL_CUT > 0 and self.in_shadowform():
            # Shadowform: Physical damage taken -15%. The engine's only physical-only hook is armor (tables.armor_mitigation: A / (A + K),
            # K = 400 + 85 x the attacker's level), so the cut becomes the extra armor B that lowers every melee hit by exactly that share:
            # K / (A + B + K) = (1 - r) K / (A + K)  =>  B = (A + K) r / (1 - r). Caster bolts (spell damage) are not touched.
            r = SHADOWFORM_PHYSICAL_CUT
            bonus += (f.p.armor + bonus + 400 + 85 * f.m.level) * r / (1 - r)
        return bonus

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
        if p.buff("Dark Inspiration", t):   # client 70425: +3%/rank Spirit for 10 s
            spirit *= 1 + self.tv("Dark Inspiration", 0) / 100
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
        self._flay_i, self._flay_t = -1, None
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
        pi = self.spells.get("Power Infusion") if self.holy else None
        if pi is not None and p.ready("Power Infusion", t) and p.mana >= self.mana_cost(pi) + 300:
            p.mana -= self.mana_cost(pi)
            p.buffs["Power Infusion"] = {"until": t + 15.0}
            p.cooldowns["Power Infusion"] = t + 180.0
            fight.casts["Power Infusion"] = fight.casts.get("Power Infusion", 0) + 1

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
        if spell.name == "Mind Blast" and amount > 0 and self.rank("Dark Inspiration"):   # client 70425
            p.buffs["Dark Inspiration"] = {"until": t + 10.0}
        if spell.name == "Shadow Word: Death" and m.hp > 0:
            back = 0.10 * p.hp_max
            p.hp -= back
            fight.note(f"Shadow Word: Death backlash {back:.0f}")

    def shadow_hit(self, fight, spell, amount):
        p, m, t, rng = fight.p, fight.m, fight.t, fight.rng
        if spell.school == "shadow" and self.rank("Shadow Weaving") and rng.random() < self.tv("Shadow Weaving", 0) / 100:
            b = m.debuffs.get("Shadow Weaving")   # on the mob since client 70425
            stacks = min(5, (b["stacks"] if b and b["until"] > t else 0) + 1)
            m.debuffs["Shadow Weaving"] = {"until": t + 15.0, "stacks": stacks}
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
        ifb = p.buffs.get("Inner Focus")
        if ifb and ifb.get("spent") == spell.name:
            del p.buffs["Inner Focus"]
        if spell.name == "Mind Flay":   # the channel ended: Dark Inspiration when every tick landed (fully channelled), the ramp starts over
            if self.rank("Dark Inspiration") and self._flay_i + 1 >= max(1, spell.dot_ticks):
                p.buffs["Dark Inspiration"] = {"until": t + 10.0}
            self._flay_i, self._flay_t = -1, None
        cd = spell.cooldown
        if spell.name == "Mind Blast":
            cd = max(0.0, cd - self.tv("Improved Mind Blast", 0))
        if spell.name == "Psychic Scream":
            cd = max(0.0, cd - self.tv("Improved Psychic Scream", 0))
        if spell.name == "Power Word: Shield":
            cd = 15.0
        if cd > 0:
            p.cooldowns[spell.name] = t + cd
        if self.holy and spell.name in RENEWED_HOPE_HEALS and self.rank("Renewed Hope") and p.cooldowns.get("Power Word: Shield", 0.0) > t:
            p.cooldowns["Power Word: Shield"] = max(t, p.cooldowns["Power Word: Shield"] - self.tv("Renewed Hope", 1))

    def on_hit_taken(self, fight, dmg, crit=False):
        p, t = fight.p, fight.t
        b = p.buffs.get("Inner Fire")
        if b and b.get("charges", 0) > 0:
            b["charges"] -= 1
        if crit and self.rank("Martyrdom"):
            p.buffs["Focused Casting"] = {"until": t + 6.0}
        if self.holy and self.rank("Blessed Recovery") and dmg > 0 and (crit or dmg > 0.30 * p.hp_max):
            left = sum(h[1] * h[2] for h in p.hots if h[0] == "Blessed Recovery")   # refreshing carries over the rest
            total = left + dmg * self.tv("Blessed Recovery", 1) / 100   # index 1: 8/17/25%; index 0 is the 30% threshold (audit 2026-10-18 #32)
            p.hots = [h for h in p.hots if h[0] != "Blessed Recovery"]
            p.hots.append(["Blessed Recovery", total / 3, 3, t + 2.0, 2.0, "player"])

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
        if self.holy:
            return self.decide_holy(fight)
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
        # Devouring Plague as damage (client 70425: 24 s cooldown, 24 s dot; the tuned rules set its health and mana gates)
        if dp and can(dp) and not fight.dot_active("Devouring Plague") and hp > 0.30 * m.hp_max:
            return dp
        if swd and can(swd) and hp <= 0.2 * m.hp_max and self.rank("Early Demise"):
            return swd
        if blast and can(blast):
            return blast
        if flay and can(flay) and hp > wand_hit * 3 and m.dist <= self.flay_range(flay) and p.mana >= self.WAND_BELOW * p.mana_max:
            return flay
        if smite and can(smite) and not in_melee and hp > avg(smite):
            return smite
        if smite and can(smite) and flay is None and (p.absorb > 0 and t < p.absorb_until):
            return smite
        return "wand"

    def decide_holy(self, fight):
        """Holy / Discipline leveling: Holy Fire opener, Shadow Word: Pain, Penance and Mind Blast on cooldown, Smite filler, wand finish;
        shield, Renew and Flash Heal keep the priest up."""
        if fight.others():
            r = self.decide_aoe(fight)
            if r is not None:
                return r
        p, m, t = fight.p, fight.m, fight.t
        sp = self.spells
        in_melee = m.in_melee and m.dist <= MELEE_RANGE + 0.5
        shielded = p.absorb > 0 and t < p.absorb_until

        def avg(s):
            return (s.dmg_min + s.dmg_max) / 2 + s.coef * p.spell_power if s else 0.0

        def can(s):
            return s is not None and p.ready(s.name, t) and fight.can_afford(s, self.mana_cost(s))

        swp, blast, smite, hf, pen, scream, pws, renew = (sp.get("Shadow Word: Pain"), sp.get("Mind Blast"), sp.get("Smite"), sp.get("Holy Fire"),
                                                          sp.get("Penance"), sp.get("Psychic Scream"), sp.get("Power Word: Shield"), sp.get("Renew"))
        wand_hit = self.wand_damage() * 0.65
        hp = m.hp
        # emergencies
        if p.hp < 0.30 * p.hp_max:
            dpr = sp.get("Desperate Prayer")
            if dpr and can(dpr):
                return dpr
        if p.hp < 0.40 * p.hp_max and in_melee and scream and can(scream) and hp > 0.25 * m.hp_max and not m.incapacitated(t):
            return scream
        if p.hp < 0.50 * p.hp_max and pws and not shielded and can(pws) and hp > 0.15 * m.hp_max:
            return pws
        if p.hp < 0.35 * p.hp_max and hp > wand_hit * 2:
            fh = sp.get("Flash Heal") or sp.get("Lesser Heal")
            if fh and can(fh):
                return fh
        if (p.hp < 0.60 * p.hp_max and renew and can(renew) and hp > 0.25 * m.hp_max
                and not any(h[0] == "Renew" for h in p.hots)):
            return renew
        # a casting mob: Silence it (a Discipline / Holy build rarely has it)
        sil = sp.get("Silence")
        if m.caster and m.casting(t) and sil and can(sil) and m.dist <= sil.range:
            return sil
        # finishers without overkill
        if blast and can(blast) and hp <= avg(blast) * 0.9 and hp > wand_hit * 2.5:
            return blast
        if hp <= wand_hit * 1.5:
            return "wand"
        # a shield in melee (no pushback while it holds) once Weakened Soul is gone
        if in_melee and pws and not shielded and can(pws) and p.hp < 0.80 * p.hp_max and hp > 0.30 * m.hp_max:
            return pws
        # the loop
        if hf and can(hf) and not fight.dot_active("Holy Fire") and hp > 0.40 * m.hp_max and (not in_melee or shielded):
            return hf
        if swp and can(swp) and not fight.dot_active("Shadow Word: Pain") and hp > 0.30 * m.hp_max:
            return swp
        # Devouring Plague (client 70425: every priest has it, 24 s cooldown, heals you for its damage): the same damage line as Shadow's;
        # the tuned rules (rotation_opt --spec holy-leveling / discipline-leveling) set its gates or veto it (2026-10-17)
        dp = sp.get("Devouring Plague")
        if dp and can(dp) and not fight.dot_active("Devouring Plague") and hp > 0.30 * m.hp_max:
            return dp
        if pen and can(pen) and hp > wand_hit * 2 and m.dist <= (pen.range or 30.0):
            return pen
        if blast and can(blast):
            return blast
        if smite and can(smite) and hp > avg(smite) * 0.6 and p.mana >= self.WAND_BELOW * p.mana_max:
            return smite
        return "wand"
