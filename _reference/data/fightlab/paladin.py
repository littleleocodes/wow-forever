"""Paladin module for the fight lab (two-handed Retribution leveling).

Spell ranks are read from `_reference/data/forever-spells/paladin.json` (beta client build 1.60.1.70009); talent numbers from
each rank's tooltip in `_reference/data/forever-talents/paladin.json`. Weapon damage uses a quest-green two-hander by level,
attack power from the client's base stats (2 AP per Strength), Blessing of Might and Devotion Aura from the spellbook.

Playstyle `ret-dps` (the scorer's model id, used for leveling): Blessing of Might and Devotion Aura up, a Seal before each pull
(Seal of Command once talented, Seal of Righteousness before that), Judgement and Holy Strike on cooldown, Consecration while
mana allows, Hammer of Justice into a doubled Seal of Command judgement or as a breather, Hammer of Wrath under 20%; Divine
Protection then Holy Light when low, Lay on Hands in an emergency. Between fights: Holy Light / Flash of Light back to health,
water below 35% mana.
"""
import json
import pathlib
import re

from engine import parse_interrupt, BaseModule, Player, Spell, Weapon
from tables import (GCD, MELEE_RANGE, WEAPON_SPEED, class_attack_power, class_base_health, class_base_mana, class_base_stats, class_dodge,
                    class_health_regen_tick, class_mana_regen_tick, class_melee_crit, class_spell_crit, gear_stats, weapon_dps)

ROOT = pathlib.Path(__file__).resolve().parents[3]
SPELLBOOK = json.load(open(ROOT / "_reference/data/forever-spells/paladin.json", encoding="utf-8"))
TREE = json.load(open(ROOT / "_reference/data/forever-talents/paladin.json", encoding="utf-8"))

NUM = re.compile(r"(\d+(?:\.\d+)?)")
DMG = re.compile(r"(\d[\d,]*) to (\d[\d,]*) (?:as )?Holy damage")
HEAL = re.compile(r"[Hh]eals a friendly target for (\d[\d,]*) to (\d[\d,]*)")
WEAPON_PCT = re.compile(r"(\d+)% weapon damage")
SEAL_R = re.compile(r"additional (\d[\d,]*) to (\d[\d,]*) Holy damage")
SEAL_C = re.compile(r"Holy damage equal to (\d+)% of normal weapon damage")
JUDGE = re.compile(r"Unleashing this Seal's energy will (?:cause|judge an enemy, instantly causing) (\d[\d,]*) to (\d[\d,]*) Holy damage(?:, (\d[\d,]*) to (\d[\d,]*) if the target is stunned)?")
CONSEC = re.compile(r"doing (\d[\d,]*) Holy damage over (\d+) sec[^.]*?additional (\d[\d,]*) damage over (\d+) sec")
STUN = re.compile(r"Stuns the target for (\d+) sec")
AP = re.compile(r"increasing melee attack power by (\d+)|granting (\d+) melee attack power")
ARMOR = re.compile(r"Gives (\d[\d,]*) additional armor")
SEAL_LIGHT = re.compile(r"chance to heal the Paladin for (\d+)")
SEAL_WIS = re.compile(r"chance to restore (\d+) of the Paladin's mana")
COEF = re.compile(r"([\d.]+)% of spell power \((\w+(?: \w+)?)\)")

TALENT_SPELLS = {"Seal of Command": "Seal of Command", "Repentance": "Repentance", "Holy Shock": "Holy Shock", "Light's Vigil": "Light's Vigil",
                 "Divine Favor": "Divine Favor", "Voice of Truth": "Voice of Truth", "Swift Judgement": "Swift Judgement", "Templar's Bulwark": "Templar's Bulwark",
                 "Holy Shield": "Holy Shield"}
SEALS = ("Seal of Command", "Seal of Righteousness", "Seal of the Crusader", "Seal of Light", "Seal of Wisdom", "Seal of Justice", "Seal of Fury")


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
                s = Spell(name=name, school=(r.get("school") or "holy").lower(), rank=int(NUM.search(r.get("rank") or "1").group(1)) if NUM.search(r.get("rank") or "") else 1,
                          level=int(r.get("level") or 1), cost=cost, cast=cast, cooldown=_seconds(r.get("cooldown")),
                          range=_num(rm.group(1)) if rm else 5.0, coef=coefs.get("direct", 0.0), tags=("cost_pct",) if "base mana" in cost_txt else ())
                s.text = txt
                s.interrupt = parse_interrupt(txt)
                dm, he, wp, sr, sc, jd, cs, st, ap, ar, sl, sw = (rx.search(txt) for rx in (DMG, HEAL, WEAPON_PCT, SEAL_R, SEAL_C, JUDGE, CONSEC, STUN, AP, ARMOR, SEAL_LIGHT, SEAL_WIS))
                if name in SEALS:
                    s.kind = "buff"
                    if sr:
                        s.seal_min, s.seal_max = _num(sr.group(1)), _num(sr.group(2))
                    if sc:
                        s.seal_pct = float(sc.group(1)) / 100
                    if jd:
                        s.judge = (_num(jd.group(1)), _num(jd.group(2)))
                        s.judge_stunned = (_num(jd.group(3)), _num(jd.group(4))) if jd.group(3) else None
                    if sl:
                        s.seal_heal = float(sl.group(1))
                    if sw:
                        s.seal_mana = float(sw.group(1))
                    if ap:
                        s.ap = float(ap.group(1) or ap.group(2))
                elif name == "Holy Strike":
                    s.kind = "melee"
                    s.weapon_pct = float(wp.group(1)) / 100 if wp else 0.5
                    if dm:
                        s.dmg_min, s.dmg_max = _num(dm.group(1)), _num(dm.group(2))
                    s.school = "holy"
                elif name == "Consecration":
                    s.kind = "spell"
                    if cs:
                        s.dot, s.dot_dur = _num(cs.group(1)) + _num(cs.group(3)), float(cs.group(2))
                        s.dot_ticks = 4
                        s.dot_coef = coefs.get("per tick", 0.0)
                    s.aoe = True
                elif he and not dm:
                    s.kind = "heal"
                    s.heal_min, s.heal_max, s.heal_coef = _num(he.group(1)), _num(he.group(2)), coefs.get("heal", 0.0)
                elif dm:
                    s.dmg_min, s.dmg_max = _num(dm.group(1)), _num(dm.group(2))
                if st:
                    s.stun = float(st.group(1))
                    s.kind = "spell"
                if ap and name.startswith("Blessing"):
                    s.kind, s.ap = "buff", float(ap.group(1) or ap.group(2))
                if ar:
                    s.kind, s.armor = "buff", _num(ar.group(1))
                if name in ("Judgement", "Divine Protection", "Divine Shield", "Lay on Hands", "Blessing of Kings", "Retribution Aura", "Sanctity Aura",
                            "Righteous Fury", "Swift Judgement", "Templar's Bulwark", "Divine Favor", "Voice of Truth", "Blessing of Wisdom", "Concentration Aura"):
                    s.kind = "buff"
                if name == "Lay on Hands":
                    s.kind, s.resource = "heal", "none"
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
    "Divine Strength": "+2%/rank Strength",
    "Divine Intellect": "+2%/rank Intellect",
    "Healing Light": "+4%/rank Holy Light / Flash of Light",
    "Spiritual Focus": "35%/rank chance to ignore pushback on heals",
    "Improved Seals": "+5%/rank seal and judgement damage",
    "Unyielding Faith": "PvP",
    "Voice of Truth": "casters only",
    "Reverence": "10%/rank mana regen while casting",
    "Purifying Power": "Exorcism / Holy Wrath (Undead and Demons): not used",
    "Infusion of Light": "healers",
    "Illumination": "20%/rank: crit heals refund 50% of base mana",
    "Divine Favor": "not used",
    "Divine Precision": "+6%/rank Holy spell hit (judgements, Consecration)",
    "Holy Shock": "not used (Retribution)",
    "Consecrated Ground": "+5%/rank Holy damage vs the first mobs in Consecration",
    "Holy Power": "+3%/rank Holy Strike crit, +1%/rank spell crit",
    "Toughness": "+2%/rank armor",
    "Redoubt": "no shield",
    "Precision": "+1%/rank hit",
    "Guardian's Favor": "not used",
    "Anticipation": "+20 Defense: ~-1.6% chance to be hit (assumed)",
    "Improved Seal of Fury": "no shield",
    "Improved Righteous Fury": "not used",
    "Shield Specialization": "no shield",
    "Sacred Duty": "+2%/rank Stamina, -30 s/rank Divine Protection / Shield cooldown",
    "Swift Judgement": "not used",
    "One-Handed Weapon Specialization": "two-hander build",
    "Improved Hammer of Justice": "-5 s/rank Hammer of Justice cooldown",
    "Templar's Bulwark": "not used",
    "Reckoning": "20%/rank chance of an extra attack after being crit",
    "Iron Creed": "threat only",
    "Holy Shield": "no shield",
    "Deflection": "+1%/rank parry",
    "Benediction": "-2%/rank mana on instants",
    "Improved Judgement": "-1 s/rank Judgement cooldown",
    "Holy Conduit": "-20%/rank Consecration / Hammer of Wrath mana",
    "Conviction": "+1%/rank melee crit",
    "Vindication": "10%/rank per melee hit: +3% attack power for 30 s (the mob's attack power loss is not modelled)",
    "Sanctified Judgement": "33%/rank chance per Judgement to refund 60% of the seal's mana",
    "Seal of Command": "unlocks Seal of Command (7 procs per minute: +70% weapon damage as Holy; judgement 169..187, doubled on a stunned mob)",
    "Pursuit of Justice": "travel speed only",
    "Eye for an Eye": "10%/rank of crits taken dealt back",
    "Sacred Arbiter": "+20% Holy Strike",
    "Two-Handed Weapon Specialization": "+2%/rank two-hander damage",
    "Vengeance": "+1%/rank Physical and Holy damage per stack after a crit (3 stacks, 30 s)",
    "Repentance": "Humanoids only: not used",
    "Champion of the Light": "+33%/rank of Intellect as spell damage (seals, judgements, Consecration)",
    "Instrument of Law": "-0.5 s/rank Hammer of Wrath cast",
    "Twist of Light": "-20% seal mana",
}
FIT = {
    "Divine Strength": "scale", "Divine Intellect": "scale", "Improved Seals": "scale", "Reverence": "scale", "Illumination": "scale", "Holy Power": "scale",
    "Healing Light": "scale", "Divine Precision": "scale", "Consecrated Ground": "scale", "Toughness": "scale", "Precision": "scale", "Anticipation": "scale",
    "Sacred Duty": "scale", "Improved Hammer of Justice": "scale", "Reckoning": "scale", "Deflection": "scale", "Benediction": "scale", "Improved Judgement": "scale",
    "Holy Conduit": "scale", "Conviction": "scale", "Vindication": "scale", "Sanctified Judgement": "scale",
    "Seal of Command": ("replace", [{"channel": "dmg", "scope": ["type:melee"], "values": [0.15]}]),
    "Eye for an Eye": "scale", "Sacred Arbiter": "scale", "Two-Handed Weapon Specialization": "scale", "Vengeance": "scale", "Champion of the Light": "scale",
    "Instrument of Law": "scale", "Twist of Light": "scale", "Spiritual Focus": "scale", "Repentance": "scale", "Voice of Truth": "scale",
}
SHARE_SOURCE = {"Melee": "white", "Seal of Command": "seal", "Seal of Righteousness": "seal", "Judgement": "judgement", "Consecration": "consecration",
                "Holy Strike": "holy_strike", "Hammer of Wrath": "hammer_of_wrath", "Retribution Aura": "ret_aura"}
NEW_SOURCES = {"hammer_of_wrath": {"id": "hammer_of_wrath", "share": 0.0, "min_level": 44, "tags": ["type:spell", "school:holy", "ability:Hammer of Wrath", "weapon:2h"], "cooldown": 6}}
KEY_TALENTS = ["Seal of Command", "Conviction", "Improved Seals"]
DESCRIPTION = ("Single-target leveling fights against normal mobs of your level with a two-hander: Blessing of Might and Devotion Aura up, a Seal recast before each "
               "pull (Seal of Command once talented, Seal of Righteousness before), the mob walks in (paladins have no charge), Judgement and Holy Strike on cooldown, "
               "Consecration while mana allows, Hammer of Justice into a doubled Seal of Command judgement or when hurt, Hammer of Wrath under 20%; Divine "
               "Protection and a Holy Light when low, Lay on Hands in an emergency. Between fights: 2 s loot, 6 s travel, Holy Light or Flash of Light back to "
               "80% health, water below 35% mana; a death costs 90 s.")
NOT_MODELLED = "runners, adds, Exorcism / Holy Wrath (Undead and Demons), Repentance, Seal of Wisdom / Seal of Light twisting, Blessing of Kings, shields, gear upgrades within a level bracket."
# rebuild.py: which scorer model, hand draft and optimizer build the pipeline calibrates, races and reports for this class
PIPELINE = {"variants": [{'spec': 'ret-dps', 'opt': 'opt-ret-dps-leveling-aoe', 'tag': 'aoe', 'profile': 'leveling-aoe', 'lookahead': 16, 'sets': ['MOBS_PER_PULL=3'], 'levels': '30,40,50,60', 'calibrate_levels': '40,60', 'label': 'AoE grinding, 3 mobs per pull'}], "spec": "ret-dps", "hand": "leveling-retribution", "opt": "opt-ret-dps-leveling-st", "tag": "ret", "lookahead": 16,
            "levels": "20,30,40,50,60", "calibrate_levels": "30,60"}


class PaladinModule(BaseModule):
    resource = "mana"
    melee = True

    AOE = {'direct': ['Consecration'], 'min_near': 2}

    def __init__(self, talents, level, spec="ret-dps", gear="leveling"):
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
        self.armor_spell_used = "Devotion Aura" if "Devotion Aura" in self.spells else "none"

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

    def seal(self):
        return self.spells.get("Seal of Command") or self.spells.get("Seal of Righteousness")

    # ------------------------------------------------------------ character
    def make_player(self, level):
        base = class_base_stats("paladin", level)
        g = gear_stats(level, self.gear, "paladin")
        strength = (base["strength"] + g["strength"]) * (1 + self.tv("Divine Strength", 0) / 100)
        agility = base["agility"] + g["agility"]
        stamina = (base["stamina"] + g["stamina"]) * (1 + self.tv("Sacred Duty", 0) / 100)
        intellect = (base["intellect"] + g["intellect"]) * (1 + self.tv("Divine Intellect", 0) / 100)
        spirit = base["spirit"] + g["spirit"]
        dev = self.book.get("Devotion Aura")
        armor = g["armor"] * (1 + self.tv("Toughness", 0) / 100) + (getattr(dev, "armor", 0.0) if dev else 0.0)
        bm = class_base_mana("paladin", level)
        might = self.book.get("Blessing of Might")
        p = Player(level=level, hp_max=class_base_health("paladin", level) + 10 * stamina, hp=0.0, mana_max=bm + 15 * intellect, mana=0.0, base_mana=bm,
                   spirit=spirit, intellect=intellect, spell_power=g["spell_power"] + intellect * self.tv("Champion of the Light", 0) / 100, armor=armor,
                   spell_crit=class_spell_crit("paladin", level, intellect) + self.tv("Holy Power", 1) / 100, dodge=class_dodge("paladin", level, agility), ranged_crit=0.0)
        p.strength, p.agility, p.stamina = strength, agility, stamina
        p.attack_power = class_attack_power("paladin", level, strength, agility) + (getattr(might, "ap", 0.0) if might else 0.0)
        self.base_ap = p.attack_power
        p.melee_crit = class_melee_crit("paladin", level, agility) + self.tv("Conviction", 0) / 100
        p.hit_bonus = self.tv("Precision", 0) / 100
        p.parry = 0.05 + self.tv("Deflection", 0) / 100
        dps = weapon_dps(level, "2h")
        p.mh = Weapon(dmg_min=dps * WEAPON_SPEED["2h"] * 0.8, dmg_max=dps * WEAPON_SPEED["2h"] * 1.2, speed=WEAPON_SPEED["2h"], kind="2h")
        p.hp, p.mana = p.hp_max, p.mana_max
        p.regen_while_casting = self.tv("Reverence", 0) / 100
        return p

    def pull_range(self):
        return 20.0

    # ------------------------------------------------------------ engine hooks: numbers
    def mana_cost(self, spell):
        cost = spell.cost
        if "cost_pct" in spell.tags:
            cost = cost / 100 * self._base_mana
        if spell.cast == 0 and spell.kind != "heal":
            cost *= 1 - self.tv("Benediction", 0) / 100
        if spell.name in ("Consecration", "Hammer of Wrath", "Exorcism", "Holy Wrath"):
            cost *= 1 - self.tv("Holy Conduit", 0) / 100
        if spell.name in SEALS and self.rank("Twist of Light"):
            cost *= 0.8
        return cost

    def cast_time(self, spell):
        c = spell.cast
        if spell.name == "Hammer of Wrath":
            c = max(0.0, c - 0.5 * self.rank("Instrument of Law"))
        return c

    def hit_bonus(self, spell):
        if spell.kind == "spell" and spell.school == "holy":
            return self.tv("Divine Precision", 0) / 100
        return 0.0

    def crit_bonus(self, spell, frozen):
        if spell.name == "Holy Strike":
            return self.tv("Holy Power", 0) / 100
        return 0.0

    def damage_multiplier(self, spell, frozen):
        m = 1 + self.tv("Two-Handed Weapon Specialization", 0) / 100
        f = self._fight
        if f:
            v = f.p.buff("Vengeance", f.t)
            if v:
                m *= 1 + 0.01 * self.rank("Vengeance") * v["stacks"]
        if spell.name in SEALS or spell.name == "Judgement":
            m *= 1 + self.tv("Improved Seals", 0) / 100
        if spell.name == "Holy Strike" and self.rank("Sacred Arbiter"):
            m *= 1.20
        if spell.name == "Consecration":
            m *= 1 + self.tv("Consecrated Ground", 0) / 100
        return m

    def heal_multiplier(self, spell):
        return 1 + self.tv("Healing Light", 0) / 100

    def periodic_can_crit(self, spell):
        return True

    def mana_regen(self, p, t):
        return class_mana_regen_tick("paladin", p.spirit)

    def health_regen(self, p):
        return class_health_regen_tick("paladin", p.spirit)

    def pushback_resisted(self, fight, spell):
        if spell.kind == "heal" and self.rank("Spiritual Focus"):
            return fight.rng.random() < self.tv("Spiritual Focus", 0) / 100
        return False

    def split_damage_taken(self, fight, dmg):
        p = fight.p
        if p.buff("Divine Protection", fight.t):
            return 0.0
        return dmg

    # ------------------------------------------------------------ engine hooks: events
    def on_fight_start(self, fight):
        self._fight = fight
        self._base_mana = fight.p.base_mana
        p, t = fight.p, fight.t
        seal = self.seal()
        if seal is not None and p.mana >= self.mana_cost(seal) + 100:
            p.mana -= self.mana_cost(seal)
            p.fsr_until = t + 5.0
            p.buffs["Seal"] = {"until": t + 30.0, "name": seal.name}
            fight.casts[seal.name] = fight.casts.get(seal.name, 0) + 1

    def on_swing(self, fight, spell, outcome, amount, hand):
        p, m, t = fight.p, fight.m, fight.t
        if outcome in ("miss", "dodge", "parry"):
            return
        sealb = p.buff("Seal", t)
        seal = self.spells.get(sealb["name"]) if sealb else None
        if seal is not None and spell.name == "Melee":
            if getattr(seal, "seal_pct", 0.0):
                if fight.rng.random() < 7.0 * p.mh.speed / 60.0:   # 7 procs per minute
                    dmg = seal.seal_pct * fight.weapon_damage(p.mh) * self.damage_multiplier(seal, False)
                    crit = fight.rng.random() < p.melee_crit
                    if crit:
                        dmg *= 2.0
                    fight.deal(Spell(seal.name, "holy"), dmg, crit)
                    fight.note(f"{seal.name} proc{' CRIT' if crit else ''} {dmg:.0f} -> mob {max(0, m.hp):.0f}")
            elif getattr(seal, "seal_max", 0.0):
                dmg = (fight.rng.uniform(seal.seal_min, seal.seal_max) + seal.coef * p.spell_power) * self.damage_multiplier(seal, False)
                fight.deal(Spell(seal.name, "holy"), dmg, False)
        if spell.name == "Melee" and self.rank("Vindication") and fight.rng.random() < 0.10 * self.rank("Vindication"):
            if not p.buff("Vindication", t):
                p.attack_power = self.base_ap * 1.03
            p.buffs["Vindication"] = {"until": t + 30.0}
        if outcome == "crit" and self.rank("Vengeance"):
            v = p.buffs.get("Vengeance")
            stacks = min(3, (v["stacks"] if v and v["until"] > t else 0) + 1)
            p.buffs["Vengeance"] = {"until": t + 30.0, "stacks": stacks}

    def on_hit(self, fight, spell, amount, crit, frozen):
        p, m, t = fight.p, fight.m, fight.t
        if spell.name == "Judgement":
            sealb = p.buff("Seal", t)
            seal = self.spells.get(sealb["name"]) if sealb else None
            if seal is not None and getattr(seal, "judge", None):
                lo, hi = seal.judge
                if m.stunned(t) and getattr(seal, "judge_stunned", None):
                    lo, hi = seal.judge_stunned
                dmg = (fight.rng.uniform(lo, hi) + seal.coef * p.spell_power) * self.damage_multiplier(spell, False)
                jcrit = fight.rng.random() < p.spell_crit
                if jcrit:
                    dmg *= 1.5
                fight.deal(spell, dmg, jcrit)
                fight.note(f"Judgement ({seal.name}){' CRIT' if jcrit else ''} {dmg:.0f} -> mob {max(0, m.hp):.0f}")
                if self.rank("Sanctified Judgement") and fight.rng.random() < 0.33 * self.rank("Sanctified Judgement"):
                    p.mana = min(p.mana_max, p.mana + 0.6 * self.mana_cost(seal))
        if spell.name == "Holy Strike" and self.rank("Sacred Arbiter"):
            pass
        if spell.name == "Hammer of Justice":
            m.stun_until = max(m.stun_until, t + spell.stun)
        if spell.name == "Divine Protection":
            p.buffs["Divine Protection"] = {"until": t + 8.0}
        if spell.name == "Lay on Hands":
            fight.heal(spell, p.hp_max)
            p.mana = 0.0
        if spell.kind == "heal" and crit and self.rank("Illumination"):
            p.mana = min(p.mana_max, p.mana + 0.5 * spell.cost * self.tv("Illumination", 0) / 100)

    def on_hit_taken(self, fight, dmg, crit=False):
        p, m, t = fight.p, fight.m, fight.t
        if crit and self.rank("Reckoning") and fight.rng.random() < 0.2 * self.rank("Reckoning"):
            fight.resolve_attack(Spell("Reckoning", "physical", kind="melee", resource="none"), white=True, hand="mh")
        if crit and self.rank("Eye for an Eye") and dmg > 0:
            fight.deal(Spell("Eye for an Eye", "holy"), min(0.5 * p.hp_max, dmg * self.tv("Eye for an Eye", 0) / 100), False)

    def after_cast(self, fight, spell):
        p, t = fight.p, fight.t
        cd = spell.cooldown
        if spell.name == "Judgement":
            cd = max(GCD, cd - self.tv("Improved Judgement", 0))
        if spell.name == "Hammer of Justice":
            cd = max(10.0, cd - self.tv("Improved Hammer of Justice", 0))
        if spell.name in ("Divine Protection", "Divine Shield"):
            cd = max(60.0, cd - self.tv("Sacred Duty", 1))
        if cd > 0:
            p.cooldowns[spell.name] = t + cd
        if spell.name == "Holy Strike" and self.rank("Sacred Arbiter"):
            pass

    def after_fight(self, p, t):
        """Holy Light (or Flash of Light) back to 80% health between fights when mana allows; drinking follows the engine's threshold."""
        spent = 0.0
        hl, fl = self.spells.get("Holy Light"), self.spells.get("Flash of Light")
        for _ in range(3):
            if p.hp >= 0.80 * p.hp_max:
                break
            missing = p.hp_max - p.hp
            heal = fl if (fl is not None and missing < (fl.heal_min + fl.heal_max) / 2 * 1.5) else hl
            if heal is None or p.mana < self.mana_cost(heal):
                break
            p.mana -= self.mana_cost(heal)
            amount = ((heal.heal_min + heal.heal_max) / 2 + heal.heal_coef * p.spell_power) * self.heal_multiplier(heal)
            p.hp = min(p.hp_max, p.hp + amount)
            spent += max(GCD, heal.cast)
        return spent

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

        judge, hs, cons, how, hoj, dp, loh, hl, fol = (sp.get(n) for n in ("Judgement", "Holy Strike", "Consecration", "Hammer of Wrath", "Hammer of Justice", "Divine Protection", "Lay on Hands", "Holy Light", "Flash of Light"))
        hp = m.hp
        seal = self.seal()
        # emergencies: Lay on Hands, bubble and heal
        if loh and can(loh) and p.hp < 0.15 * p.hp_max:
            return loh
        if p.hp < 0.35 * p.hp_max and hp > 0.25 * m.hp_max:
            if dp and can(dp) and not p.buff("Divine Protection", t):
                return dp
            if hl and can(hl) and (p.buff("Divine Protection", t) or m.stunned(t)):
                return hl
            if hoj and can(hoj) and not m.stunned(t):
                return hoj
            if fol and can(fol) and p.hp < 0.25 * p.hp_max:
                return fol
        # a casting mob: Hammer of Justice breaks the cast (it stands there casting until you reach it)
        if m.caster and m.casting(t) and hoj and can(hoj) and m.dist <= hoj.range and not m.stunned(t):
            return hoj
        if not in_melee:
            return "advance"
        # keep the seal up
        if seal is not None and not p.buff("Seal", t) and can(seal) and hp > 0.15 * m.hp_max:
            return seal
        if how and can(how) and hp <= 0.2 * m.hp_max:
            return how
        # Hammer of Justice into a doubled Seal of Command judgement
        if hoj and can(hoj) and judge and p.ready("Judgement", t) and seal is not None and getattr(seal, "judge_stunned", None) and hp > 0.3 * m.hp_max and not m.stunned(t):
            return hoj
        if judge and can(judge) and p.buff("Seal", t):
            return judge
        if hs and can(hs):
            return hs
        if cons and can(cons) and p.mana > 0.45 * p.mana_max and hp > 0.3 * m.hp_max and not fight.dot_active("Consecration"):
            return cons
        return None
