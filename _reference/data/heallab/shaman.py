"""Restoration shaman raid healer for the healer lab: Healing Wave on the tank (downranked to the deficit), Lesser Healing Wave
when it must land fast, Chain Heal when the group is hurt, Riptide when talented, Healing Stream Totem ticking on the group,
Nature's Swiftness for an instant Healing Wave, Mana Tide when mana runs low; Ancestral Healing armors the tank after a crit."""
import engine as E
import tables as T

PIPELINE = {"spec": "resto-heal", "hand": "resto-raid-healer", "opt": "opt-resto-heal-raid-heal", "tag": "resto"}


class Healer(E.BaseHealer):
    CLASS = "shaman"
    SPEC = "resto-heal"
    ROLES = {"big": "Healing Wave", "fast": "Lesser Healing Wave", "group": "Chain Heal", "hot": "Riptide", "instant": "Riptide"}
    TALENT_SPELLS = {"Riptide": "Riptide", "Mana Tide Totem": "Mana Tide Totem", "Nature's Swiftness": "Nature's Swiftness", "Water Shield": "Water Shield"}
    MECHANICS = {
        "Nature's Swiftness": "instant Healing Wave on a tank under 35%, every 3 min",
        "Mana Tide Totem": "290 mana every 3 s for 12 s when mana is under 50%, every 5 min",
        "Ancestral Healing": "a critical heal gives the target +25% armor for 15 s (33%/rank chance)",
        "Water Shield": "a critical heal restores 2% of maximum mana (one globe every 3 s)",
        "Totemic Focus": "totem mana only: nothing for heals",
        "Riptide": "instant heal plus a 15 s HoT on a 6 s cooldown: the emergency heal and the tank's HoT",
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

    def on_heal(self, sim, spell, target, amount, crit):
        if crit and self.rank("Ancestral Healing") and sim.rng.random() < self.rank("Ancestral Healing") / 3.0:
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
