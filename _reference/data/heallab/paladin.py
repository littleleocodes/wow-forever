"""Holy paladin raid healer for the healer lab: Holy Light on the tank (downranked to the deficit) with Blessing of Light on
him, Flash of Light on everything else, Holy Shock as the instant, Divine Favor before a big Holy Light, Light's Vigil and a
Holy Shock as the group heal, Lay on Hands when the tank is about to die; Illumination returns part of a critical heal's cost
and Infusion of Light speeds up the next Holy Light.

Talent numbers are read from the beta tooltips (`forever-talents/paladin.json`, client build 1.60.1.70291), spell numbers from
the beta spellbook (`forever-spells/paladin.json`). 2026-10-09 rework against those tooltips: Illumination returns 50% of the
spell's base cost at 20% a rank (it had returned the whole cost); Infusion of Light shortens the next Holy Light by 0.5 s a rank
after a critical Holy Shock or Flash of Light (it had been +6% a rank Holy Light healing); Light's Vigil is simulated (it was
never cast); Holy Power gives Holy Shock 3% a rank and every other heal 1% (Holy Shock had 1%); Benediction makes the instants
cheaper; Divine Favor's mana is paid; Lay on Hands heals for the paladin's maximum health, not the tank's; Blessing of Light
counts only on the tank when a rank is chosen; Improved Blessing of Wisdom (removed from the Forever trees) is gone."""
import copy
import json
import re

import engine as E
import tables as T

PIPELINE = {"spec": "holy-heal", "hand": "holy-raid-healer", "opt": "opt-holy-heal-raid-heal", "tag": "holy"}

_SPELLBOOK = json.load(open(E.ROOT / "_reference/data/forever-spells/paladin.json", encoding="utf-8"))
_TREES = json.load(open(E.ROOT / "_reference/data/forever-talents/paladin.json", encoding="utf-8"))


def _num(s):
    return float(s.replace(",", ""))


def _top_rank(name):
    """The spellbook's highest rank of a spell (the level-60 rank)."""
    for tab in _SPELLBOOK["tabs"]:
        for sp in tab["spells"]:
            if sp["name"] == name:
                return max(sp["ranks"], key=lambda r: int(r.get("level") or 0))
    raise ValueError(f"heallab/paladin.py: no {name} in forever-spells/paladin.json")


def _talent_ranks(name, pattern):
    """Per rank, the numbers a pattern captures from the talent's tooltip (rank 1 first)."""
    for tr in _TREES["trees"]:
        for t in tr["talents"]:
            if t["name"] == name:
                out = []
                for text in t["ranks"]:
                    m = re.search(pattern, text or "")
                    if not m:
                        raise ValueError(f"heallab/paladin.py: the {name} tooltip no longer matches {pattern!r}: {text!r}")
                    out.append(tuple(float(g) for g in m.groups()))
                return out
    raise ValueError(f"heallab/paladin.py: no talent {name} in forever-talents/paladin.json")


# Blessing of Light on the tank (its top rank, a baseline spell): bonus healing of each Holy Light and Flash of Light he receives
_bol = (_top_rank("Blessing of Light").get("text") or "").replace("\n", " ")
BLESSING_OF_LIGHT = {"Holy Light": _num(re.search(r"Holy Light spells used on the target by up to (\d[\d,]*)", _bol).group(1)),
                     "Flash of Light": _num(re.search(r"Flash of Light spells used on the target by up to (\d[\d,]*)", _bol).group(1))}
# per rank, from the 70291 tooltips
ILLUMINATION = [(c / 100, s / 100) for c, s in _talent_ranks("Illumination", r"(\d+)% chance to gain Mana equal to (\d+)% of the base cost")]
ILLUMINATION_SPELLS = ("Holy Light", "Flash of Light", "Holy Shock", "Light's Vigil")
INFUSION = [s for (s,) in _talent_ranks("Infusion of Light", r"by ([\d.]+) sec")]
# hotfix 113554 (ported 2026-10-31): Holy Power multiplies the whole critical heal (the simulator's applyHolyPower: 5/5 makes a heal crit
# 225%); until then +3%/rank Holy Shock crit and +1%/rank on other heals
HOLY_POWER = [v / 100 for (v,) in _talent_ranks("Holy Power", r"critical strike healing bonus of your Holy spells by (\d+)%")]
# Oath of Light (one ally, 5 min: sworn on the tank before the pull) and Boundless Light (Holy Shock crit on allies without the Oath)
OATH_OF_LIGHT = dict(zip(("Holy Light", "Flash of Light", "Holy Shock"), _talent_ranks(
    "Oath of Light", r"Holy Light on them by up to (\d+), your Flash of Light by up to (\d+), and your Holy Shock by up to (\d+)")[0]))
BOUNDLESS_LIGHT = [v / 100 for (v,) in _talent_ranks("Boundless Light", r"Holy Shock spell by (\d+)%")]
BENEDICTION = [v / 100 for (v,) in _talent_ranks("Benediction", r"by (\d+)%")]
# Light's Vigil (talent, top rank): "Your next Holy Shock cast on them triggers no cooldown and causes ... allied targets to heal their
# party for X to Y"; the healing coefficient is the spellbook's "(heal)" one
_lv = _top_rank("Light's Vigil")
_lv_text = (_lv.get("text") or "").replace("\n", " ")
_lv_heal = re.search(r"heal their party for (\d[\d,]*) to (\d[\d,]*)", _lv_text)
_lv_coef = re.search(r"([\d.]+)% of spell power \(heal\)", _lv.get("coefficient") or "")
VIGIL = {"rank": int(re.search(r"\d+", _lv.get("rank") or "1").group(0)), "level": int(_lv.get("level") or 60),
         "cost": _num(re.search(r"(\d[\d,]*)", _lv.get("cost") or "0").group(1)), "cast": E._seconds(_lv.get("cast")),
         "cooldown": E._seconds(_lv.get("cooldown")), "text": _lv_text,
         "heal": (_num(_lv_heal.group(1)), _num(_lv_heal.group(2))), "coef": float(_lv_coef.group(1)) / 100 if _lv_coef else 0.0}


class Healer(E.BaseHealer):
    CLASS = "paladin"
    SPEC = "holy-heal"
    ROLES = {"big": "Holy Light", "fast": "Flash of Light", "instant": "Holy Shock", "group": "Light's Vigil"}
    TALENT_SPELLS = {"Holy Shock": "Holy Shock", "Divine Favor": "Divine Favor"}
    MECHANICS = {
        "Illumination": "a critical Holy Light, Flash of Light, Holy Shock or Light's Vigil heal returns 50% of that spell's base mana "
                        "cost (20%/rank chance; once per spell per cast)",
        "Divine Favor": "a sure critical top-rank Holy Light on the tank every 2 min (its mana paid)",
        "Holy Shock": "instant 307-333 heal on a 10 s cooldown: the emergency heal, and the trigger of Light's Vigil",
        "Holy Power": "a critical heal heals x(1 + 10%/rank) more (hotfix 113554: 150% -> 225% at 5/5)",
        "Oath of Light": "sworn on the tank before the pull (5 min): +400 Holy Light, +115 Flash of Light, +229 Holy Shock on the tank",
        "Boundless Light": "+15%/rank critical chance with Holy Shock on a raid member without the Oath (everyone but the tank with Oath of Light)",
        "Infusion of Light": "a critical Holy Shock or Flash of Light makes the next Holy Light within 15 s 0.5 s/rank faster",
        "Benediction": "-2%/rank mana cost of the instants (Holy Shock, Divine Favor)",
        "Light's Vigil": "the group heal: Light's Vigil (1.5 s, 1,340 mana) on the lowest raid member when enough of the group is hurt "
                         "(tables.GROUP_HEAL_MIN below RAID_HEAL_AT), then a Holy Shock on them that triggers no cooldown: their party "
                         "(the whole group here) heals for 684-724 + 14.3% of healing each",
        "Lay on Hands": "once, when the tank is under 20% (a 20 min cooldown): heals for the paladin's maximum health (tables.RAID_HP, "
                        "a raid member's; the lab gives the healer no health of its own) and drains all mana",
    }
    SIMULATED = {"Illumination", "Divine Favor", "Holy Shock", "Holy Power", "Infusion of Light", "Healing Light", "Divine Intellect", "Reverence",
                 "Light's Vigil", "Benediction",
                 "Oath of Light", "Boundless Light"}
    SHARE_SOURCE = {"Holy Light": "holy_light", "Flash of Light": "flash", "Holy Shock": "holy_shock", "Lay on Hands": "loh"}

    def __init__(self, allocation, game="forever"):
        super().__init__(allocation, game)
        self._pick_target = None
        self.vigil_shock = None
        shock = self.book.get("Holy Shock")
        if self.rank("Light's Vigil") and shock:
            self.book["Light's Vigil"] = [E.Heal("Light's Vigil", VIGIL["rank"], VIGIL["level"], VIGIL["cost"], VIGIL["cast"], VIGIL["cooldown"],
                                                 "holy", VIGIL["text"], {})]
            self.vigil_shock = copy.copy(shock[-1])
            self.vigil_shock.cooldown = 0.0   # "triggers no cooldown": the engine records no Holy Shock cooldown for this cast
            self.vigil_shock.vigil = True

    # ---------------------------------------------------------------- numbers
    def crit_mult(self, spell):
        r = self.rank("Holy Power")
        return T.CRIT_MULT * (1 + HOLY_POWER[min(r, len(HOLY_POWER)) - 1]) if r else T.CRIT_MULT

    def crit_target_hook(self, spell, sim, target):
        r = self.rank("Boundless Light")
        if not r or spell.name != "Holy Shock" or target is None or (target.tank and self.rank("Oath of Light")):
            return 0.0
        return BOUNDLESS_LIGHT[min(r, len(BOUNDLESS_LIGHT)) - 1]

    def _oath(self, spell, target):
        """Oath of Light's flat bonus on the tank (sworn there before the pull; "up to": the full bonus, as the simulator reads it)."""
        return OATH_OF_LIGHT.get(spell.name, 0.0) if self.rank("Oath of Light") and (target is None or target.tank) else 0.0

    def cost_hook(self, spell, sim):
        r = self.rank("Benediction")
        if r and spell.cast <= 0:
            return 1.0 - BENEDICTION[min(r, len(BENEDICTION)) - 1]
        return 1.0

    def cast_hook(self, spell, sim):
        """Infusion of Light: the next Holy Light after a critical Holy Shock or Flash of Light (the engine asks for the cast time once,
        when the cast starts, so the buff is used up here)."""
        r = self.rank("Infusion of Light")
        if r and spell.name == "Holy Light" and sim.buffs.get("Infusion of Light", -1.0) > sim.t:
            del sim.buffs["Infusion of Light"]
            return max(0.5, spell.cast - INFUSION[min(r, len(INFUSION)) - 1]) / spell.cast
        return 1.0

    def expected(self, spell, target=None, sim=None):
        """Blessing of Light adds to Holy Light and Flash of Light on the tank only. The engine's rank choice asks without a target,
        so choice() below passes the target along."""
        target = target if target is not None else self._pick_target
        return super().expected(spell) + (BLESSING_OF_LIGHT.get(spell.name, 0.0) if target is None or target.tank else 0.0) + self._oath(spell, target)

    def choice(self, name, deficit, target, sim, max_rank=False):
        self._pick_target = target
        try:
            return super().choice(name, deficit, target, sim, max_rank)
        finally:
            self._pick_target = None

    # ---------------------------------------------------------------- events
    def on_fight_start(self, sim):
        sim.vigil_target = None    # the raid member Light's Vigil is on, until the Holy Shock that triggers it
        sim.illum_seen = set()     # spells that already returned mana through Illumination in this cast

    def on_heal(self, sim, spell, target, amount, crit):
        if not crit:
            return
        r = self.rank("Illumination")
        if r and spell.name in ILLUMINATION_SPELLS and spell.name not in sim.illum_seen:
            chance, share = ILLUMINATION[min(r, len(ILLUMINATION)) - 1]
            sim.illum_seen.add(spell.name)
            if chance >= 1.0 or sim.rng.random() < chance:
                sim.gain_mana(share * spell.cost, "Illumination")
        if self.rank("Infusion of Light") and spell.name in ("Holy Shock", "Flash of Light"):
            sim.buffs["Infusion of Light"] = sim.t + 15.0

    def on_cast_done(self, sim, spell, target):
        if target.tank and spell.name in BLESSING_OF_LIGHT:
            sim.apply_heal(spell, target, BLESSING_OF_LIGHT[spell.name] * self.heal_mult(spell, target, sim), False, label=spell.name)
        if target.tank and self._oath(spell, target):
            sim.apply_heal(spell, target, self._oath(spell, target) * self.heal_mult(spell, target, sim), False, label=spell.name)
        if spell.name == "Light's Vigil":
            sim.vigil_target = target
        elif getattr(spell, "vigil", False):
            lv = self.book["Light's Vigil"][-1]
            crit_c = self.crit_chance(lv, sim)
            for x in sim.targets:
                if x.hp > 0:
                    amt = (sim.rng.uniform(*VIGIL["heal"]) + VIGIL["coef"] * self.healing) * self.heal_mult(lv, x, sim)
                    crit = sim.rng.random() < crit_c
                    sim.apply_heal(lv, x, amt * (self.crit_mult(lv) if crit else 1.0), crit, label="Light's Vigil")
            sim.vigil_target = None
        sim.illum_seen.clear()

    # ---------------------------------------------------------------- choices
    def group_spell(self, sim, hurt):
        """Light's Vigil on the lowest hurt raid member, when its Holy Shock can follow."""
        lv = (self.book.get("Light's Vigil") or [None])[-1]
        if lv is None or self.vigil_shock is None or sim.vigil_target is not None:
            return None
        if not self.cooldown_ready(sim, "Light's Vigil", lv.cooldown) or sim.mana < self.cost(lv, sim) + self.cost(self.vigil_shock, sim):
            return None
        return (lv, min(hurt, key=lambda x: x.frac))

    def before_decide(self, sim):
        tank = sim.tank
        loh = self.book.get("Lay on Hands")
        if loh and tank.hp > 0 and tank.frac < 0.2 and self.cooldown_ready(sim, "Lay on Hands", loh[-1].cooldown or 1200.0):
            sim.cd["Lay on Hands"] = sim.t
            sim.apply_heal(loh[-1], tank, T.RAID_HP, False, label="Lay on Hands")   # the paladin's maximum health: a raid member's
            sim.mana = 0.0   # drains the paladin's mana (beta tooltip)
            sim.gcd_until = sim.t + T.GCD
            return None
        if sim.vigil_target is not None:   # Light's Vigil is up: the Holy Shock that triggers it
            if sim.vigil_target.hp > 0:
                return (self.vigil_shock, sim.vigil_target)
            sim.vigil_target = None
        df = self.book.get("Divine Favor")
        hl = self.book["Holy Light"][-1]
        if df and self.cooldown_ready(sim, "Divine Favor", df[-1].cooldown or 120.0) and tank.deficit > 0.6 * self.expected(hl, tank):
            cost = self.cost(df[-1], sim)
            if sim.mana >= cost + self.cost(hl, sim):
                sim.mana -= cost
                sim.cd["Divine Favor"] = sim.t
                sim.temp_crit = 1.0
                return (hl, tank)
        return None
