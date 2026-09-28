"""Druid module for the fight lab (Feral cat leveling from 20).

Spell ranks are read from `_reference/data/forever-spells/druid.json` (beta client build 1.60.1.70009); talent numbers from each
rank's tooltip in `_reference/data/forever-talents/druid.json`. Cat Form attacks once a second with a "paw" whose damage grows
like a one-hander by level (`tables.weapon_dps`), attack power from the client's base stats (2 AP per Strength, 1 per Agility)
plus Cat Form's 120 + Agility and Predatory Strikes.

Playstyle `feral-cat-dps` (the scorer's model id, used for leveling): prowl up behind the mob, open with Ravage (Pounce before
32, Claw before that), Tiger's Fury, Rake once, Claw to five points, Rip on a healthy mob or Ferocious Bite, Berserk on the
pull when ready; shift out to Regrowth when low (Nature's Swiftness + Healing Touch in an emergency) and shift back (Cat Form
costs 55% of base mana, Furor keeps the energy). Between fights: Rejuvenation / Regrowth in caster form when hurt, then Cat
Form again; water below 35% mana. Levels 10-19 (Bear Form) are not simulated: the fight lab starts at 20.
"""
import json
import pathlib
import re

from engine import parse_interrupt, BaseModule, Player, Spell, Weapon
from tables import (MOB_SWING, GCD, MELEE_RANGE, class_attack_power, class_base_health, class_base_mana, class_base_stats, class_dodge,
                    class_health_regen_tick, class_mana_regen_tick, class_melee_crit, class_spell_crit, gear_stats, weapon_dps)

ROOT = pathlib.Path(__file__).resolve().parents[3]
SPELLBOOK = json.load(open(ROOT / "_reference/data/forever-spells/druid.json", encoding="utf-8"))
TREE = json.load(open(ROOT / "_reference/data/forever-talents/druid.json", encoding="utf-8"))

NUM = re.compile(r"(\d+(?:\.\d+)?)")
PCT = re.compile(r"(\d+)% (?:normal )?damage plus (\d[\d,]*)")
RAKE = re.compile(r"for (\d[\d,]*) damage and an additional (\d[\d,]*) damage over (\d+) sec")
POUNCE = re.compile(r"stunning the target for (\d+) sec and causing (\d[\d,]*) damage over (\d+) sec")
FIVE = re.compile(r"5 points: (\d[\d,]*)(?:-(\d[\d,]*))? damage(?: over (\d+) sec)?")
ONE = re.compile(r"1 point : (\d[\d,]*)(?:-(\d[\d,]*))? damage(?: over (\d+) sec)?")
EXTRA = re.compile(r"each extra point of energy into ([\d.]+) additional damage")
HEAL = re.compile(r"Heals a friendly target for (\d[\d,]*) to (\d[\d,]*)(?: and another (\d[\d,]*) over (\d+) sec)?")
HOT = re.compile(r"Heals the target for (\d[\d,]*) over (\d+) sec")
DMG = re.compile(r"Causes (\d[\d,]*) to (\d[\d,]*) (\w+) damage")
MOONFIRE = re.compile(r"Burns the enemy for (\d[\d,]*) to (\d[\d,]*) Arcane damage and then an additional (\d[\d,]*) Arcane damage over (\d+) sec")
CP = re.compile(r"Awards (\d) combo point")
FORM_AP = re.compile(r"increasing melee attack power by (\d+)")
FORM_ARMOR = re.compile(r"armor contribution from items by (\d+)%")
FORM_HP = re.compile(r"and health by (\d[\d,]*)")
MAUL = re.compile(r"next attack by (\d+) damage")
SWARM = re.compile(r"causing (\d[\d,]*) Nature damage over (\d+) sec")
STARFIRE = re.compile(r"Causes (\d[\d,]*) to (\d[\d,]*) Arcane damage")
SWIPE = re.compile(r"inflicting (\d+) damage")
ROAR = re.compile(r"melee attack power by (\d+)\. Lasts (\d+) sec")
STUN = re.compile(r"Stuns the target for (\d+) sec")
COEF = re.compile(r"([\d.]+)% of spell power \((\w+(?: \w+)?)\)")

TALENT_SPELLS = {"Berserk": "Berserk", "Feral Charge": "Feral Charge", "Primal Bite": "Primal Bite", "Swiftmend": "Swiftmend", "Nature's Swiftness": "Nature's Swiftness",
                 "Insect Swarm": "Insect Swarm", "Moonkin Form": "Moonkin Form", "Wild Growth": "Wild Growth", "Leader of the Pack": "Leader of the Pack"}
CAT = {"Claw", "Rake", "Shred", "Rip", "Ferocious Bite", "Tiger's Fury", "Pounce", "Ravage", "Cower", "Dash", "Prowl"}
BEAR = {"Maul", "Swipe", "Demoralizing Roar", "Enrage", "Bash", "Growl", "Primal Bite"}


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
                cast = 0.0 if "instant" in cast_txt or not cast_txt or "channel" in cast_txt else _seconds(cast_txt)
                coefs = {k: float(v) / 100 for v, k in COEF.findall(r.get("coefficient") or "")}
                rm = re.search(r"(\d+) yd range", r.get("range") or "")
                name = sp["name"]
                resource = "energy" if "Energy" in cost_txt else ("rage" if "Rage" in cost_txt else ("mana" if "Mana" in cost_txt or "base mana" in cost_txt else "none"))
                s = Spell(name=name, school=(r.get("school") or "nature").lower(), rank=int(NUM.search(r.get("rank") or "1").group(1)) if NUM.search(r.get("rank") or "") else 1,
                          level=int(r.get("level") or 1), cost=cost, cast=cast, cooldown=_seconds(r.get("cooldown")),
                          range=_num(rm.group(1)) if rm else 5.0, coef=coefs.get("direct", 0.0), resource=resource,
                          tags=("cost_pct",) if "base mana" in cost_txt else ())
                s.text = txt
                s.interrupt = parse_interrupt(txt)
                pc, rk, po, fv, on, ex, he, ho, dm, mf, cp, fa = (rx.search(txt) for rx in (PCT, RAKE, POUNCE, FIVE, ONE, EXTRA, HEAL, HOT, DMG, MOONFIRE, CP, FORM_AP))
                if name in CAT:
                    s.kind, s.school = "melee", "physical"
                    if pc:
                        s.weapon_pct, s.dmg_min, s.dmg_max = float(pc.group(1)) / 100, _num(pc.group(2)), _num(pc.group(2))
                    if rk:
                        s.dmg_min = s.dmg_max = _num(rk.group(1))
                        s.dot, s.dot_dur, s.dot_ticks = _num(rk.group(2)), float(rk.group(3)), 3
                    if po:
                        s.stun, s.dot, s.dot_dur, s.dot_ticks = float(po.group(1)), _num(po.group(2)), float(po.group(3)), 6
                    if fv and on:
                        s.five = (_num(fv.group(1)), _num(fv.group(2)) if fv.group(2) else _num(fv.group(1)))
                        s.one = (_num(on.group(1)), _num(on.group(2)) if on.group(2) else _num(on.group(1)))
                        s.combo = -1
                        if fv.group(3):
                            s.dot_dur, s.dot_ticks = float(fv.group(3)), 6
                        else:
                            s.dmg_min, s.dmg_max = s.five
                    if ex:
                        s.extra_energy = float(ex.group(1))
                    if cp:
                        s.combo = int(cp.group(1))
                    if name in ("Tiger's Fury", "Prowl", "Dash", "Cower"):
                        s.kind = "buff"
                elif he:
                    s.kind, s.heal_min, s.heal_max, s.heal_coef = "heal", _num(he.group(1)), _num(he.group(2)), coefs.get("heal", 0.0)
                    if he.group(3):
                        s.hot, s.hot_dur = _num(he.group(3)), float(he.group(4))
                elif ho:
                    s.kind, s.hot, s.hot_dur, s.heal_coef = "heal", _num(ho.group(1)), float(ho.group(2)), coefs.get("per tick", 0.0)
                elif mf:
                    s.dmg_min, s.dmg_max = _num(mf.group(1)), _num(mf.group(2))
                    s.dot, s.dot_dur, s.dot_ticks, s.dot_coef = _num(mf.group(3)), float(mf.group(4)), 4, coefs.get("per tick", 0.0)
                elif name == "Insect Swarm" and SWARM.search(txt):
                    sw = SWARM.search(txt)
                    s.dot, s.dot_dur, s.dot_ticks, s.dot_coef = _num(sw.group(1)), float(sw.group(2)), 6, coefs.get("per tick", 0.0)
                elif dm:
                    s.dmg_min, s.dmg_max = _num(dm.group(1)), _num(dm.group(2))
                if fa:
                    s.kind, s.form_ap = "buff", float(fa.group(1))
                    am, hm = FORM_ARMOR.search(txt), FORM_HP.search(txt)
                    s.form_armor_pct = float(am.group(1)) if am else 0.0
                    s.form_hp = _num(hm.group(1)) if hm else 0.0
                if name in BEAR:
                    s.school = "physical"
                    ma, sw, ro, st = MAUL.search(txt), SWIPE.search(txt), ROAR.search(txt), STUN.search(txt)
                    if name == "Maul" and ma:
                        s.kind, s.on_next_swing, s.weapon_pct, s.dmg_min, s.dmg_max = "melee", True, 1.0, _num(ma.group(1)), _num(ma.group(1))
                    elif name == "Swipe" and sw:
                        s.kind, s.dmg_min, s.dmg_max = "melee", _num(sw.group(1)), _num(sw.group(1))
                    elif name == "Primal Bite" and pc:
                        s.kind, s.weapon_pct, s.dmg_min, s.dmg_max = "melee", float(pc.group(1)) / 100, _num(pc.group(2)), _num(pc.group(2))
                    elif name == "Bash" and st:
                        s.kind, s.stun = "melee", float(st.group(1))
                    elif name == "Demoralizing Roar" and ro:
                        s.kind, s.roar_ap, s.roar_dur = "buff", float(ro.group(1)), float(ro.group(2))
                    else:
                        s.kind = "buff"
                if name in ("Mark of the Wild", "Thorns", "Nature's Swiftness", "Innervate", "Berserk", "Barkskin", "Omen of Clarity", "Faerie Fire", "Cat Form", "Bear Form", "Dire Bear Form", "Travel Form"):
                    s.kind = "buff"
                if name == "Feral Charge":
                    s.kind, s.charge, s.root, s.resource, s.cost = "buff", True, 4.0, "none", 0.0
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
    "Ferocity": "-1 energy/rank on Claw and Rake, -1 rage/rank on Maul, Swipe and Primal Bite",
    "Heart of the Wild": "+2%/rank Intellect, +2%/rank Strength in Cat Form, +4%/rank Stamina in Bear Form",
    "Feral Swiftness": "+2%/rank dodge",
    "Feral Instinct": "+10%/rank Swipe (bear, not used single-target) and stealth: no effect here",
    "Brutal Impact": "+0.5 s/rank Pounce and Bash stun, -15 s/rank Bash cooldown",
    "Thick Hide": "+3 armor per level per rank in forms",
    "Savage Fury": "+5%/rank Claw, Rake, Shred, Maul, Swipe",
    "Feral Charge": "cat / bear: charge that roots and interrupts a casting mob (4 s)",
    "Sharpened Claws": "+3%/rank crit in forms",
    "Shredding Attacks": "-6 energy/rank Shred (used only in the opener from behind)",
    "Primal Bite": "bear (levels 10-19): 100% weapon damage plus a bonus for 20 rage every 6 s",
    "Predatory Strikes": "+50%/rank of your level as attack power in forms",
    "Blood Frenzy": "bear (levels 10-19): 50%/rank chance of 5 rage on a critical strike",
    "Predatory Instincts": "+10%/rank crit damage bonus on abilities",
    "Leader of the Pack": "+3% crit in forms",
    "King of the Jungle": "Tiger's Fury grants 20 energy per rank",
    "Natural Reaction": "+1%/rank dodge",
    "Rend and Tear": "+2%/rank ability damage on a bleeding mob (Rake, Rip, Pounce)",
    "Berserk": "+100% crit on combo-point abilities for 15 s every 3 min",
    "Genesis": "+1%/rank periodic damage (Rake, Rip, Pounce, Moonfire) and healing",
    "Nature's Majesty": "+2%/rank crit with spells and melee",
    "Nature's Reach": "+2%/rank hit",
    "Moonglow": "caster form only",
    "Improved Moonfire": "Balance: +5%/rank Moonfire damage and crit (cat: no Moonfire)",
    "Improved Wrath": "Balance: -0.1 s/rank Wrath cast, -10%/rank mana (cat: not used)",
    "Vengeance": "Balance: +20%/rank Arcane / Nature crit damage bonus",
    "Moonfury": "Balance: +2%/rank Arcane / Nature damage",
    "Nature's Grace": "Balance: a spell crit makes the next cast 0.5 s faster",
    "Insect Swarm": "Balance: a Nature DoT kept up",
    "Improved Starfire": "Balance: -0.1 s/rank Starfire cast, 3%/rank chance of a 3 s stun",
    "Eclipse": "Balance: after a Wrath the next two Starfires cast 0.5 s faster (up to 4 charges, 15 s)",
    "Moonkin Form": "Balance: +360% armor from items from 40 (no shapeshift costs in the fights)",
    "Furor": "20%/rank of your energy kept when shifting into Cat Form; 20%/rank chance of 10 rage when shifting into Bear Form (expected value)",
    "Naturalist": "+1%/rank all damage, -0.1 s/rank Healing Touch",
    "Natural Shapeshifter": "-10%/rank shapeshift mana",
    "Reflection": "17%/rank mana regen while casting",
    "Gift of Nature": "+2%/rank heals",
    "Improved Rejuvenation": "+5%/rank Rejuvenation",
    "Tranquil Spirit": "-2%/rank Healing Touch mana",
    "Nature's Swiftness": "instant Healing Touch every 3 min when low",
    "Living Spirit": "+5%/rank Spirit",
    "Swiftmend": "instant heal of a running Rejuvenation / Regrowth",
    "Subtlety": "threat only",
    "Nature's Focus": "14%/rank less pushback on heals",
}
FIT = {
    "Ferocity": "scale", "Heart of the Wild": "scale", "Feral Swiftness": "scale", "Brutal Impact": "scale", "Thick Hide": "scale", "Savage Fury": "scale",
    "Sharpened Claws": "scale", "Shredding Attacks": "scale", "Predatory Strikes": "scale", "Predatory Instincts": "scale", "Leader of the Pack": "scale",
    "King of the Jungle": "scale", "Natural Reaction": "scale", "Rend and Tear": "scale", "Berserk": "scale", "Genesis": "scale", "Nature's Majesty": "scale",
    "Nature's Reach": "scale", "Furor": "scale", "Naturalist": "scale", "Natural Shapeshifter": "scale", "Reflection": "scale", "Gift of Nature": "scale",
    "Improved Rejuvenation": "scale", "Tranquil Spirit": "scale", "Nature's Swiftness": "scale", "Living Spirit": "scale", "Swiftmend": "scale", "Blood Frenzy": "scale",
    "Feral Charge": "scale", "Feral Instinct": "scale", "Moonglow": "scale", "Improved Moonfire": "scale", "Improved Wrath": "scale", "Nature's Focus": "scale",
}
SHARE_SOURCE = {"Melee": "white", "Shred": "shred", "Ferocious Bite": "ferocious_bite", "Rip": "rip", "Claw": "claw_rake", "Rake": "claw_rake", "Ravage": "shred",
                "Pounce": "claw_rake"}
NEW_SOURCES = {}
KEY_TALENTS = ["Predatory Strikes", "Savage Fury", "Sharpened Claws"]
DESCRIPTION = ("Single-target leveling fights against normal mobs of your level. Levels 10-19 in Bear Form: walk up, Enrage, Demoralizing Roar, Maul on every swing "
               "the rage allows, Bash when low or against a casting mob. From 20 in Cat Form: prowl up behind the mob and open with Ravage (Pounce before 32, Claw "
               "before that), Tiger's Fury, Rake once, Claw to five points (the mob faces you, so Shred is only for the opener), Rip on a healthy mob or Ferocious Bite, "
               "Berserk on the pull; when low, shift out for a Regrowth (Nature's Swiftness + Healing Touch in an emergency) and shift back at 55% of base mana with Furor "
               "keeping the energy. Between fights: 2 s loot, 6 s travel, Rejuvenation / Regrowth in caster form when hurt then Cat Form again, water below 35% mana.")
NOT_MODELLED = "levels 1-9 (Wrath / Moonfire), Moonfire / Wrath pulls in bear levels, Faerie Fire, Swipe, Growl, Dash, Innervate, Barkskin, adds, gear upgrades within a level bracket."
# rebuild.py: which scorer model, hand draft and optimizer build the pipeline calibrates, races and reports for this class
PIPELINE = {"variants": [{'spec': 'balance-dps', 'opt': 'opt-balance-dps-leveling-st', 'tag': 'bal', 'profile': 'leveling-st', 'lookahead': 16, 'sets': [],
                          'levels': '20,30,40,50,60', 'calibrate_levels': '30,60', 'label': 'Balance (its own rotation)', 'report': 'balance-dps-opt'}],
            "spec": "feral-cat-dps", "hand": "leveling-feral", "opt": "opt-feral-cat-dps-leveling-st", "tag": "cat", "lookahead": 16,
            "levels": "15,20,30,40,50,60", "calibrate_levels": "15,30,60",
            "extra_reports": [{"spec": "balance-dps", "build": "opt-balance-dps-leveling-st", "compare": ["opt-feral-cat-dps-leveling-st"]}]}


class DruidModule(BaseModule):
    resource = "energy"
    melee = True

    def __init__(self, talents, level, spec="feral-cat-dps", gear="leveling"):
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
        self.balance = spec.startswith("balance")
        self.form = "caster" if self.balance else ("cat" if "Cat Form" in self.spells else ("bear" if "Bear Form" in self.spells else "caster"))
        self.form_spell = self.spells.get("Cat Form") if self.form == "cat" else self.spells.get("Bear Form")
        self.in_cat = self.form != "caster"     # "in form" (cat or bear); the name is historical
        self.moonkin = self.balance and "Moonkin Form" in self.spells
        self.resource = "rage" if self.form == "bear" else ("mana" if self.balance else "energy")
        self.opened = False
        self.armor_spell_used = {"cat": "Cat Form", "bear": "Bear Form"}.get(self.form, "caster")

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
        base = class_base_stats("druid", level)
        g = gear_stats(level, self.gear, "druid")
        strength = (base["strength"] + g["strength"]) * (1 + self.tv("Heart of the Wild", 1) / 100 if self.form == "cat" else 1.0)
        agility = base["agility"] + g["agility"]
        stamina = (base["stamina"] + g["stamina"]) * (1 + self.tv("Heart of the Wild", 2) / 100 if self.form == "bear" else 1.0)
        intellect = (base["intellect"] + g["intellect"]) * (1 + self.tv("Heart of the Wild", 0) / 100)
        spirit = (base["spirit"] + g["spirit"]) * (1 + self.tv("Living Spirit", 0) / 100)
        motw = self.book.get("Mark of the Wild")
        mm = re.search(r"armor by (\d+)", motw.text) if motw else None
        form = self.form_spell
        armor = g["armor"] * (1 + (3.6 if self.moonkin else getattr(form, "form_armor_pct", 0.0) / 100)) + (_num(mm.group(1)) if mm else 0.0) + level * self.rank("Thick Hide")
        bm = class_base_mana("druid", level)
        cat = self.book.get("Cat Form")
        p = Player(level=level, hp_max=class_base_health("druid", level) + 10 * stamina + getattr(form, "form_hp", 0.0), hp=0.0, mana_max=bm + 15 * intellect, mana=0.0, base_mana=bm,
                   spirit=spirit, intellect=intellect, spell_power=g["spell_power"], armor=armor, spell_crit=class_spell_crit("druid", level, intellect),
                   dodge=class_dodge("druid", level, agility) + self.tv("Feral Swiftness", 1) / 100 + self.tv("Natural Reaction", 0) / 100, ranged_crit=0.0)
        p.strength, p.agility, p.stamina = strength, agility, stamina
        p.attack_power = class_attack_power("druid", level, strength, agility) + level * self.tv("Predatory Strikes", 0) / 100
        if self.form == "cat":
            p.attack_power += getattr(cat, "form_ap", 0.0) + agility
        elif self.form == "bear":
            p.attack_power += getattr(form, "form_ap", 0.0)
        p.melee_crit = class_melee_crit("druid", level, agility) + self.tv("Sharpened Claws", 0) / 100 + (0.03 if self.rank("Leader of the Pack") else 0.0) + self.tv("Nature's Majesty", 0) / 100
        p.hit_bonus = self.tv("Nature's Reach", 1) / 100
        dps = weapon_dps(level, "2h") * 0.85   # a cat's paws: assumed 85% of a quest-green two-hander's dps at a 1.0 s swing (a bear's at 2.5 s)
        if self.form == "bear":
            self.paw = Weapon(dmg_min=dps * 2.5 * 0.8, dmg_max=dps * 2.5 * 1.2, speed=2.5, kind="paw")
            p.rage_max, p.rage = 100.0, 0.0
            p.energy_max = 0.0
        else:
            self.paw = Weapon(dmg_min=dps * 1.0 * 0.8, dmg_max=dps * 1.0 * 1.2, speed=1.0, kind="paw")
            p.energy_max = 100.0
            p.energy = p.energy_max
        p.mh = self.paw if self.form != "caster" else None
        if self.balance:
            p.energy_max = 0.0
            p.spell_crit += self.tv("Nature's Majesty", 0) / 100
        p.hp, p.mana = p.hp_max, p.mana_max
        p.regen_while_casting = self.tv("Reflection", 0) / 100
        self.in_cat = self.form != "caster"
        return p

    def pull_range(self):
        return 30.0 if self.balance else 20.0

    def shift_cost(self, p):
        form = self.form_spell
        return (form.cost / 100 * p.base_mana if form else 0.0) * (1 - self.tv("Natural Shapeshifter", 0) / 100)

    # ------------------------------------------------------------ engine hooks: numbers
    def mana_cost(self, spell):
        cost = spell.cost
        if "cost_pct" in spell.tags:
            cost = cost / 100 * self._base_mana
        if spell.name == "Wrath":
            cost *= 1 - self.tv("Improved Wrath", 1) / 100
        if spell.kind == "spell" and spell.school in ("arcane", "nature") and spell.dmg_max + spell.dot > 0:
            cost *= 1 - self.tv("Moonglow", 0) / 100
        if spell.name in ("Claw", "Rake", "Maul", "Swipe", "Primal Bite"):
            cost = max(0.0, cost - self.rank("Ferocity"))
        if spell.name == "Shred":
            cost = max(0.0, cost - 6.0 * self.rank("Shredding Attacks"))
        if spell.name == "Healing Touch":
            cost *= 1 - self.tv("Tranquil Spirit", 0) / 100
        return cost

    def final_cost(self, fight, spell, cost):
        if fight.p.buff("Clearcasting", fight.t) and spell.kind in ("melee", "heal", "spell") and cost > 0:
            del fight.p.buffs["Clearcasting"]
            return 0.0
        return cost

    def cast_time(self, spell):
        c = spell.cast
        if spell.name == "Healing Touch":
            c = max(GCD, c - 0.1 * self.rank("Naturalist"))
        if spell.name == "Wrath":
            c = max(GCD, c - 0.1 * self.rank("Improved Wrath"))
        if spell.name == "Starfire":
            c = max(GCD, c - 0.1 * self.rank("Improved Starfire"))
            f = self._fight
            if f and f.p.buff("Eclipse", f.t) and f.p.buffs["Eclipse"].get("charges", 0) > 0:
                c = max(GCD, c - 0.5)
        f = self._fight
        if c > 0 and f and f.p.buff("Nature's Grace", f.t):
            c = max(GCD, c - 0.5)
        if c > 0 and self._fight and self._fight.p.buff("Nature's Swiftness", self._fight.t) and spell.school == "nature":
            return 0.0
        return c

    def crit_bonus(self, spell, frozen):
        f = self._fight
        if f and spell.combo > 0 and f.p.buff("Berserk", f.t):
            return 1.0
        return 0.0

    def crit_damage_bonus(self, spell):
        if spell.kind == "melee" and spell.name != "Melee":
            return self.tv("Predatory Instincts", 0) / 100
        if spell.kind == "spell" and spell.school in ("arcane", "nature"):
            return self.tv("Vengeance", 0) / 100 * 0.5   # +100% of the 50% crit bonus = +50% damage on a crit
        return 0.0

    def damage_multiplier(self, spell, frozen):
        m = 1 + self.tv("Naturalist", 1) / 100
        if spell.kind == "spell" and spell.school in ("arcane", "nature"):
            m *= 1 + self.tv("Moonfury", 0) / 100
            if spell.name == "Moonfire":
                m *= 1 + self.tv("Improved Moonfire", 0) / 100
        f = self._fight
        if f and f.p.buff("Tiger's Fury", f.t):
            m *= 1.15
        if spell.name in ("Claw", "Rake", "Shred", "Maul", "Swipe"):
            m *= 1 + self.tv("Savage Fury", 0) / 100
        if spell.kind == "melee" and spell.name != "Melee" and f and (f.dot_active("Rake") or f.dot_active("Rip") or f.dot_active("Pounce")):
            m *= 1 + self.tv("Rend and Tear", 0) / 100
        if spell.name == "Ferocious Bite" and f:
            cp = max(1, f.last_combo)
            lo1, hi1 = spell.one
            lo5, hi5 = spell.five
            avg = (lo1 + hi1) / 2 + ((lo5 + hi5) / 2 - (lo1 + hi1) / 2) * (cp - 1) / 4 + 0.03 * cp * f.p.attack_power + getattr(spell, "extra_energy", 0.0) * getattr(f, "_bite_extra", 0.0)
            m *= avg / ((lo5 + hi5) / 2)
        return m

    def periodic_multiplier(self, spell):
        return self.damage_multiplier(spell, False) * (1 + self.tv("Genesis", 0) / 100)

    def heal_multiplier(self, spell):
        m = (1 + self.tv("Gift of Nature", 0) / 100) * (1 + self.tv("Genesis", 0) / 100 if spell.hot > 0 else 1.0)
        if spell.name == "Rejuvenation":
            m *= 1 + self.tv("Improved Rejuvenation", 0) / 100
        return m

    def periodic_can_crit(self, spell):
        return True

    def mana_regen(self, p, t):
        return class_mana_regen_tick("druid", p.spirit)

    def health_regen(self, p):
        return class_health_regen_tick("druid", p.spirit)

    def pushback_resisted(self, fight, spell):
        if spell.kind == "heal" and self.rank("Nature's Focus"):
            return fight.rng.random() < self.tv("Nature's Focus", 0) / 100
        return False

    def attacks_from_front(self):
        return self.opened or self.balance

    # ------------------------------------------------------------ forms
    def shift_out(self, fight):
        p = fight.p
        self.in_cat = False
        p.mh = None
        fight.note(f"shifts out of {self.form_spell.name if self.form_spell else 'form'}")

    def armor_bonus(self):
        f = self._fight
        if f and self.form == "bear" and f.p.buff("Enrage", f.t):
            return -0.27 * f.p.armor
        return 0.0

    def on_regen_tick(self, fight, p, t):
        en = p.buff("Enrage", t)
        if en and en.get("left", 0) > 0:
            gain = min(4.0, en["left"])
            en["left"] -= gain
            p.rage = min(p.rage_max, p.rage + gain)

    def shift_in(self, fight_or_none, p, t):
        cost = self.shift_cost(p)
        if p.mana < cost:
            return False
        p.mana -= cost
        p.fsr_until = t + 5.0
        if self.form == "bear":
            p.rage = min(p.rage_max, p.rage + 10.0 * self.tv("Furor", 0) / 100)   # expected value of the rage chance
        else:
            p.energy = p.energy * self.tv("Furor", 1) / 100 if self.rank("Furor") else 0.0
        self.in_cat = True
        p.mh = self.paw
        name = self.form_spell.name if self.form_spell else "form"
        if fight_or_none is not None:
            fight_or_none.note(name)
            fight_or_none.casts[name] = fight_or_none.casts.get(name, 0) + 1
        return True

    # ------------------------------------------------------------ engine hooks: events
    def on_fight_start(self, fight):
        self._fight = fight
        self._base_mana = fight.p.base_mana
        p, m, t = fight.p, fight.m, fight.t
        self.opened = False
        if self.balance:
            return
        if not self.in_cat:
            if not self.shift_in(fight, p, t):
                self.in_cat = False
        if self.in_cat and self.form == "cat":
            m.dist = MELEE_RANGE          # prowled up behind the mob
            m.in_melee = True
            m.swing_at = t + 1.5
            p.swing_mh = t + 0.5
        elif self.form == "bear":
            self.opened = True            # no stealth opener: the bear walks up
        bs = self.spells.get("Berserk")
        if bs is not None and p.ready("Berserk", t) and self.in_cat:
            p.buffs["Berserk"] = {"until": t + 15.0}
            p.cooldowns["Berserk"] = t + bs.cooldown

    def on_swing(self, fight, spell, outcome, amount, hand):
        p, m, t = fight.p, fight.m, fight.t
        if spell.name in ("Ravage", "Pounce", "Shred", "Claw") and not self.opened:
            self.opened = True
        if outcome in ("miss", "dodge", "parry"):
            return
        if "Omen of Clarity" in self.spells and fight.rng.random() < 0.06:
            p.buffs["Clearcasting"] = {"until": t + 15.0}
        if outcome == "crit" and self.form == "bear" and self.rank("Blood Frenzy") and fight.rng.random() < self.tv("Blood Frenzy", 0) / 100:
            p.rage = min(p.rage_max, p.rage + 5.0)
        if spell.name == "Rip" and amount == 0:
            cp = max(1, fight.last_combo)
            lo1, _ = spell.one
            lo5, _ = spell.five
            total = (lo1 + (lo5 - lo1) * (cp - 1) / 4 + 0.06 * cp * p.attack_power) * self.periodic_multiplier(spell)
            fight.refresh_dot("Rip", total, 6, spell.dot_dur / 6.0, p.melee_crit, 2.0)

    def on_hit(self, fight, spell, amount, crit, frozen):
        p, m, t = fight.p, fight.m, fight.t
        if self.balance and spell.kind == "spell":
            if spell.name == "Wrath" and self.rank("Eclipse"):
                e = p.buffs.get("Eclipse") if p.buff("Eclipse", t) else None
                p.buffs["Eclipse"] = {"until": t + 15.0, "charges": min(4, (e["charges"] if e else 0) + 2)}
            if spell.name == "Starfire" and p.buff("Eclipse", t) and p.buffs["Eclipse"].get("charges", 0) > 0:
                p.buffs["Eclipse"]["charges"] -= 1
            if crit and self.rank("Nature's Grace") and spell.cast > 0:
                p.buffs["Nature's Grace"] = {"until": t + 15.0}
            elif spell.cast > 0 and p.buff("Nature's Grace", t) and not crit:
                del p.buffs["Nature's Grace"]
            if spell.name == "Starfire" and self.rank("Improved Starfire") and fight.rng.random() < self.tv("Improved Starfire", 1) / 100:
                m.stun_until = max(m.stun_until, t + 3.0)
        if spell.name == "Tiger's Fury":
            p.buffs["Tiger's Fury"] = {"until": t + 6.0}
            if self.rank("King of the Jungle"):
                p.energy = min(p.energy_max, p.energy + self.tv("King of the Jungle", 0))
        if spell.name == "Nature's Swiftness":
            p.buffs["Nature's Swiftness"] = {"until": t + 60.0}
        if spell.kind == "heal" and spell.cast > 0 and p.buff("Nature's Swiftness", t):
            del p.buffs["Nature's Swiftness"]
        if spell.name in ("Pounce", "Bash") and spell.stun > 0:
            m.stun_until = max(m.stun_until, t + spell.stun + 0.5 * self.rank("Brutal Impact"))
        if spell.name == "Demoralizing Roar":
            m.dmg_reduction = spell.roar_ap / 14.0 * MOB_SWING
            m.dmg_reduction_until = t + spell.roar_dur
            m.debuffs["Demoralizing Roar"] = {"until": t + spell.roar_dur}
        if spell.name == "Enrage":
            p.rage = min(p.rage_max, p.rage + 10.0)
            p.buffs["Enrage"] = {"until": t + 10.0, "left": 20.0}

    def after_cast(self, fight, spell):
        p, t = fight.p, fight.t
        if spell.cooldown > 0:
            p.cooldowns[spell.name] = t + spell.cooldown - (15.0 * self.rank("Brutal Impact") if spell.name == "Bash" else 0.0)
        if spell.name in ("Cat Form", "Bear Form"):
            self.shift_in(fight, p, t)

    def after_fight(self, p, t):
        """Heal in caster form when hurt (Rejuvenation, Regrowth), then Cat Form again if the mana allows."""
        spent = 0.0
        if self.balance:
            rj, rg = self.spells.get("Rejuvenation"), self.spells.get("Regrowth")
            for heal in (rj, rg):
                if heal is None or p.hp >= 0.85 * p.hp_max or p.hp >= 0.70 * p.hp_max and heal is rg or p.mana < self.mana_cost(heal):
                    continue
                p.mana -= self.mana_cost(heal)
                total = ((heal.heal_min + heal.heal_max) / 2 + heal.heal_coef * p.spell_power + heal.hot) * self.heal_multiplier(heal)
                p.hp = min(p.hp_max, p.hp + total)
                spent += max(GCD, heal.cast)
            return spent
        rj, rg = self.spells.get("Rejuvenation"), self.spells.get("Regrowth")
        if p.hp < 0.70 * p.hp_max and (rj or rg) and self.form != "caster":
            if self.in_cat:
                self.in_cat = False
                p.mh = None
            for heal in (rj, rg):
                if heal is None or p.hp >= 0.85 * p.hp_max or p.mana < self.mana_cost(heal) + self.shift_cost(p):
                    continue
                p.mana -= self.mana_cost(heal)
                total = ((heal.heal_min + heal.heal_max) / 2 + heal.heal_coef * p.spell_power + heal.hot) * self.heal_multiplier(heal)
                p.hp = min(p.hp_max, p.hp + total)
                spent += max(GCD, heal.cast)
        if not self.in_cat:
            if not self.shift_in(None, p, t):
                pass   # no mana to shift: the engine drinks, the next fight starts with the shift
            else:
                spent += GCD
        return spent

    # ------------------------------------------------------------ priority list: bear (levels 10-19)
    def decide_bear(self, fight, can):
        p, m, t = fight.p, fight.m, fight.t
        sp = self.spells
        maul, roar, enrage, bash, bite = (sp.get(n) for n in ("Maul", "Demoralizing Roar", "Enrage", "Bash", "Primal Bite"))
        hp = m.hp
        if enrage and can(enrage) and not p.buff("Enrage", t) and hp > 0.4 * m.hp_max:
            return enrage
        if bash and can(bash) and not m.stunned(t) and ((m.caster and m.casting(t)) or p.hp < 0.40 * p.hp_max) and hp > 0.15 * m.hp_max:
            return bash
        if roar and can(roar) and not (m.debuffs.get("Demoralizing Roar", {}).get("until", 0) > t) and hp > 0.35 * m.hp_max:
            return roar
        if bite and can(bite) and p.rage >= self.mana_cost(bite) + (self.mana_cost(maul) if maul else 0.0):
            return bite
        if maul and fight.queued_swing is None and p.rage >= self.mana_cost(maul):
            return maul
        return None

    def decide_balance(self, fight, can, in_melee):
        """Balance: Moonfire and Insect Swarm up, Wrath while the mob walks in (Eclipse charges), Starfire on Eclipse charges
        or when the mob is rooted / stunned, Wrath otherwise (pushback in melee), Regrowth below 35% health with Nature's
        Swiftness when it is up; Entangling Roots when low and the mob is not rooted."""
        p, m, t = fight.p, fight.m, fight.t
        sp = self.spells
        wrath, mf, sf, swarm, roots, rg, ns, ht = (sp.get(n) for n in ("Wrath", "Moonfire", "Starfire", "Insect Swarm", "Entangling Roots", "Regrowth", "Nature's Swiftness", "Healing Touch"))
        hp = m.hp

        def avg(s):
            return ((s.dmg_min + s.dmg_max) / 2 + s.coef * p.spell_power) * self.damage_multiplier(s, False) if s else 0.0

        if p.hp < 0.35 * p.hp_max and hp > 0.15 * m.hp_max:
            if ns and can(ns) and ht and not p.buff("Nature's Swiftness", t):
                return ns
            if ht and can(ht) and p.buff("Nature's Swiftness", t):
                return ht
            if roots and can(roots) and in_melee and not m.rooted(t) and hp > 0.3 * m.hp_max:
                return roots
            if rg and can(rg) and (m.rooted(t) or m.stunned(t) or not in_melee):
                return rg
        if mf and can(mf) and hp <= avg(mf) * 0.9:
            return mf
        if wrath and can(wrath) and hp <= avg(wrath) * 0.9:
            return wrath
        if mf and can(mf) and not fight.dot_active("Moonfire") and hp > 0.35 * m.hp_max:
            return mf
        if swarm and can(swarm) and not fight.dot_active("Insect Swarm") and hp > 0.4 * m.hp_max:
            return swarm
        eclipse = p.buff("Eclipse", t) and p.buffs["Eclipse"].get("charges", 0) > 0
        if sf and can(sf) and (eclipse or m.rooted(t) or m.stunned(t)) and hp > avg(sf) * 0.5:
            return sf
        if wrath and can(wrath) and hp > avg(wrath) * 0.5:
            return wrath
        if sf and can(sf):
            return sf
        return "wand" if p.mana < 50 else None

    def decide(self, fight):
        p, m, t = fight.p, fight.m, fight.t
        sp = self.spells
        in_melee = m.in_melee and m.dist <= MELEE_RANGE + 0.5

        def can(s):
            return s is not None and p.ready(s.name, t) and fight.can_afford(s, self.mana_cost(s))

        if self.balance:
            return self.decide_balance(fight, can, in_melee)

        claw, rake, shred, rip, bite, tf, pounce, ravage, rg, ht, ns, cat = (sp.get(n) for n in ("Claw", "Rake", "Shred", "Rip", "Ferocious Bite", "Tiger's Fury", "Pounce", "Ravage", "Regrowth", "Healing Touch", "Nature's Swiftness", "Cat Form"))
        hp = m.hp
        # caster form: heal and shift back
        if not self.in_cat:
            if p.hp < 0.55 * p.hp_max and hp > 0.15 * m.hp_max:
                if ns and can(ns) and ht and not p.buff("Nature's Swiftness", t):
                    return ns
                if ht and can(ht) and p.buff("Nature's Swiftness", t):
                    return ht
                if rg and can(rg) and p.mana >= self.mana_cost(rg) + self.shift_cost(p):
                    return rg
            if p.mana >= self.shift_cost(p):
                if self.shift_in(fight, p, t):
                    p.gcd_until = t + GCD
                    return None
            return None
        # emergency: shift out to heal
        if p.hp < 0.30 * p.hp_max and hp > 0.25 * m.hp_max and (rg or ht) and p.mana >= self.shift_cost(p) + (self.mana_cost(rg) if rg else 0.0):
            self.shift_out(fight)
            p.gcd_until = t + GCD
            return None
        if not in_melee:
            fc = sp.get("Feral Charge")
            if m.caster and m.casting(t) and fc and can(fc) and 8.0 <= m.dist <= 25.0:
                return fc
            return "advance"
        if self.form == "bear":
            return self.decide_bear(fight, can)
        # opener from prowl
        if not self.opened:
            if ravage and can(ravage):
                return ravage
            if pounce and can(pounce):
                return pounce
            if shred and can(shred):
                return shred
            self.opened = True
        if tf and can(tf) and not p.buff("Tiger's Fury", t) and hp > 0.3 * m.hp_max:
            return tf
        # finishers
        if bite and can(bite) and p.combo >= 1:
            lo1, hi1 = bite.one
            lo5, hi5 = bite.five
            est = ((lo1 + hi1) / 2 + ((lo5 + hi5) / 2 - (lo1 + hi1) / 2) * (p.combo - 1) / 4 + 0.03 * p.combo * p.attack_power) * self.damage_multiplier(Spell("x", "physical"), False) * 0.65
            if hp <= est * 0.95:
                fight._bite_extra = max(0.0, p.energy - self.mana_cost(bite))
                return bite
        if p.combo >= 5:
            if rip and can(rip) and hp > 0.5 * m.hp_max and not fight.dot_active("Rip"):
                return rip
            if bite and can(bite):
                fight._bite_extra = max(0.0, p.energy - self.mana_cost(bite))
                return bite
        if rake and can(rake) and not fight.dot_active("Rake") and hp > 0.3 * m.hp_max:
            return rake
        if claw and can(claw):
            return claw
        return None
