"""Restoration shaman raid healer for the healer lab: Healing Wave on the tank (downranked to the deficit), Lesser Healing Wave
when it must land fast, Chain Heal when the group is hurt, Riptide when talented, Healing Stream Totem ticking on the group,
Nature's Swiftness for an instant Healing Wave, Mana Tide when mana runs low; Ancestral Healing armors the tank after a crit."""
import json
import pathlib
import re

import engine as E
import tables as T

PIPELINE = {"spec": "resto-heal", "hand": "resto-raid-healer", "opt": "opt-resto-heal-raid-heal", "tag": "resto"}

_DATA = pathlib.Path(__file__).resolve().parent.parent


def _riptide_chain_heal_bonus():
    """Riptide: "increases the effectiveness of your Chain Heal casts directly on that target by 25%" (the beta spellbook)."""
    for tab in json.load(open(_DATA / "forever-spells" / "shaman.json", encoding="utf-8"))["tabs"]:
        for sp in tab["spells"]:
            if sp["name"] == "Riptide":
                m = re.search(r"Chain Heal casts directly on that target by (\d+)%", sp["ranks"][-1].get("text") or "")
                if m:
                    return float(m.group(1)) / 100
    return 0.25


def _ancestral_healing_armor():
    """Ancestral Healing's armor bonus per rank ("Increases your target's armor value by 8/17/25% for 15 sec after getting a critical
    effect from one of your healing spells")."""
    for tr in json.load(open(_DATA / "forever-talents" / "shaman.json", encoding="utf-8"))["trees"]:
        for tl in tr["talents"]:
            if tl["name"] == "Ancestral Healing":
                return [float(re.search(r"armor value by (\d+)%", r).group(1)) / 100 for r in tl["ranks"]]
    return [0.08, 0.17, 0.25]


RIPTIDE_CHAIN_HEAL = _riptide_chain_heal_bonus()
ANCESTRAL_HEALING_ARMOR = _ancestral_healing_armor()
ENGINE_ARMOR_BUFF = 0.25   # engine.Sim.boss_swing gives the tank +25% armor while `armor_buff_until` runs (Inspiration, Ancestral Healing)


class Healer(E.BaseHealer):
    CLASS = "shaman"
    SPEC = "resto-heal"
    ROLES = {"big": "Healing Wave", "fast": "Lesser Healing Wave", "group": "Chain Heal", "hot": "Riptide", "instant": "Riptide"}
    TALENT_SPELLS = {"Riptide": "Riptide", "Mana Tide Totem": "Mana Tide Totem", "Nature's Swiftness": "Nature's Swiftness", "Water Shield": "Water Shield"}
    MECHANICS = {
        "Nature's Swiftness": "instant Healing Wave on a tank under 35%, every 3 min",
        "Mana Tide Totem": "290 mana every 3 s for 12 s when mana is under 50%, every 5 min",
        "Ancestral Healing": "every critical heal: +8/17/25% armor on the target for 15 s (the engine's armor buff is a fixed +25%, so ranks 1-2 "
                             "apply it on 32%/68% of crits: the same average armor)",
        "Water Shield": "a critical heal restores 2% of maximum mana (one globe every 3 s)",
        "Totemic Focus": "totem mana only: nothing for heals",
        "Elemental Focus": "clearcasting from damage spells, for the next damage spell: nothing for heals",
        "Riptide": "instant heal plus a 15 s HoT on a 6 s cooldown: the emergency heal and the tank's HoT; a Chain Heal cast on a target with "
                   "your Riptide heals 25% more (every jump: the cast's effectiveness), and Chain Heal starts on a hurt member with your Riptide",
        "Healing Stream Totem": "placed at the pull: 11 (+Restorative Totems) every 2 s on the group",
    }
    SIMULATED = {"Nature's Swiftness", "Mana Tide Totem", "Ancestral Healing", "Water Shield", "Riptide", "Healing Way", "Improved Healing Wave", "Tidal Mastery", "Purification",
                 "Tidal Focus", "Restorative Totems", "Ancestral Knowledge", "Mindfulness", "Thundering Strikes"}
    SHARE_SOURCE = {"Chain Heal": "chain_heal", "Healing Wave": "healing_wave", "Lesser Healing Wave": "lesser_hw", "Healing Stream Totem": "healing_stream"}

    def on_fight_start(self, sim):
        sim.mana -= 80.0   # Healing Stream Totem
        sim.water_globe = -10.0

    def on_tick(self, sim):
        hst = self.book.get("Healing Stream Totem")
        if hst:
            per = hst[-1].hot / max(1.0, hst[-1].hot_dur / hst[-1].tick_every) if hst[-1].hot else 11.0
            mult = self.heal_mult(hst[-1], None, sim)
            for x in sim.targets:
                if x.hp > 0:
                    sim.apply_heal(hst[-1], x, per * mult, False, label="Healing Stream Totem")

    def heal_mult_hook(self, spell, target, sim):
        """Riptide: "increases the effectiveness of your Chain Heal casts directly on that target by 25%": a Chain Heal aimed at a target
        with your Riptide on it. Read as the cast's effectiveness, so every jump gains (engine.Sim.land applies one multiplier to the
        chain; healing the primary target alone more would need an engine change)."""
        if spell.name == "Chain Heal" and target is not None and "Riptide" in target.hots:
            return 1.0 + RIPTIDE_CHAIN_HEAL
        return 1.0

    def group_spell(self, sim, hurt):
        """Chain Heal starts on a target with your Riptide when there is one worth it: the tank (the lab keeps Riptide there) when it misses
        at least as much as the most hurt raid member, else the most hurt raid member with Riptide, else the most hurt (the generic choice).
        The jumps go to the most hurt others either way (engine.Sim.land)."""
        g = super().group_spell(sim, hurt)
        if not g:
            return g
        tank = sim.tank
        if tank.hp > 0 and "Riptide" in tank.hots and tank.deficit >= (hurt[0].deficit if hurt else 0.0):
            return (g[0], tank)
        rt = [x for x in hurt if "Riptide" in x.hots]
        return (g[0], rt[0]) if rt else g

    def on_heal(self, sim, spell, target, amount, crit):
        # Ancestral Healing: the tooltip's armor on every critical heal; the engine's fixed +25% stands in, on armor/25% of the crits
        rank = self.rank("Ancestral Healing")
        if crit and rank and sim.rng.random() < ANCESTRAL_HEALING_ARMOR[min(rank, len(ANCESTRAL_HEALING_ARMOR)) - 1] / ENGINE_ARMOR_BUFF:
            target.armor_buff_until = sim.t + 15.0
        if crit and "Water Shield" in self.book and sim.t >= sim.water_globe + 3.0:
            sim.water_globe = sim.t
            sim.gain_mana(0.02 * self.mana_max, "Water Shield")

    def before_decide(self, sim):
        tank = sim.tank
        if "Mana Tide Totem" in self.book and sim.mana < 0.5 * self.mana_max and self.cooldown_ready(sim, "Mana Tide Totem", 300.0):
            sim.cd["Mana Tide Totem"] = sim.t
            sim.mana -= 60.0
            sim.events += [(sim.t + 3.0 * i, 290.0) for i in range(1, 5)]
            sim.gcd_until = sim.t + T.GCD
            return None
        if "Nature's Swiftness" in self.book and tank.hp > 0 and tank.frac < T.EMERGENCY and self.cooldown_ready(sim, "Nature's Swiftness", 180.0):
            sim.cd["Nature's Swiftness"] = sim.t
            sim.instant_next = True
            return (self.book["Healing Wave"][-1], tank)
        return None

    def instant_ok(self, sim, spell, target):
        return spell.name != "Riptide" or "Riptide" not in target.hots
