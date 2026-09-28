"""Restoration druid raid healer for the healer lab: Rejuvenation kept on the tank, Healing Touch (downranked to the deficit)
when the tank is low, Regrowth as the fast heal, Swiftmend and Nature's Swiftness in emergencies, Wild Growth or Tranquility
when the group is hurt, Innervate on yourself when mana runs low; Nature's Grace speeds the cast after a critical heal."""
import engine as E
import tables as T

PIPELINE = {"spec": "resto-heal", "hand": "resto-raid-healer", "opt": "opt-resto-heal-raid-heal", "tag": "resto"}


class Healer(E.BaseHealer):
    CLASS = "druid"
    SPEC = "resto-heal"
    ROLES = {"big": "Healing Touch", "fast": "Regrowth", "hot": "Rejuvenation", "group": "Wild Growth", "instant": "Swiftmend"}
    TALENT_SPELLS = {"Swiftmend": "Swiftmend", "Wild Growth": "Wild Growth", "Nature's Swiftness": "Nature's Swiftness"}
    MECHANICS = {
        "Swiftmend": "instant heal for the full periodic amount of the target's Rejuvenation or Regrowth (consumed), 15 s cooldown",
        "Nature's Swiftness": "instant Healing Touch on a tank under 35%, every 3 min",
        "Nature's Grace": "after a critical heal the next cast is 0.5 s faster",
        "Genesis": "+1%/rank periodic healing",
        "Gift of the Earthmother": "+5% periodic healing",
        "Nature's Splendor": "+4% Rejuvenation and Regrowth",
        "Wild Growth": "679 over 7 s on the group, 6 s cooldown: the group heal",
        "Innervate": "on yourself under 40% mana (every 6 min)",
    }
    SIMULATED = {"Swiftmend", "Nature's Swiftness", "Nature's Grace", "Genesis", "Gift of the Earthmother", "Nature's Splendor", "Wild Growth", "Gift of Nature",
                 "Improved Rejuvenation", "Naturalist", "Improved Regrowth", "Reflection", "Tranquil Spirit", "Living Spirit", "Nature's Majesty", "Moonglow", "Heart of the Wild"}
    SHARE_SOURCE = {"Healing Touch": "healing_touch", "Regrowth": "regrowth", "Rejuvenation": "rejuvenation", "Tranquility": "tranquility"}

    def __init__(self, allocation, game="forever"):
        super().__init__(allocation, game)
        if "Wild Growth" not in self.book:
            self.ROLES = dict(self.ROLES, group="Tranquility")

    def heal_mult_hook(self, spell, target, sim):
        m = 1.0
        if "hot" in spell.tags:
            m *= (1 + 0.01 * self.rank("Genesis")) * (1 + 0.05 * (1 if self.rank("Gift of the Earthmother") else 0))
        if spell.name in ("Rejuvenation", "Regrowth"):
            m *= 1 + 0.04 * (1 if self.rank("Nature's Splendor") else 0)
        return m

    def cast_hook(self, spell, sim):
        return 1.0

    def cast_time(self, spell, sim):
        t = super().cast_time(spell, sim)
        if t > 0 and sim.buffs.get("Nature's Grace", 0.0) > sim.t:
            sim.buffs["Nature's Grace"] = 0.0
            t = max(0.5, t - 0.5)
        return t

    def on_heal(self, sim, spell, target, amount, crit):
        if crit and self.rank("Nature's Grace"):
            sim.buffs["Nature's Grace"] = sim.t + 15.0

    def before_decide(self, sim):
        tank = sim.tank
        if "Innervate" in self.book and sim.mana < 0.4 * self.mana_max and self.cooldown_ready(sim, "Innervate", 360.0):
            sim.cd["Innervate"] = sim.t
            sim.buffs["Innervate"] = sim.t + 20.0
            sim.gcd_until = sim.t + T.GCD
            return None
        if "Nature's Swiftness" in self.book and tank.hp > 0 and tank.frac < T.EMERGENCY and self.cooldown_ready(sim, "Nature's Swiftness", 180.0):
            sim.cd["Nature's Swiftness"] = sim.t
            sim.instant_next = True
            return (self.book["Healing Touch"][-1], tank)
        return None

    def emergency_spell(self, sim, role, target):
        if role == "instant":
            sm = self.book.get("Swiftmend")
            if sm and self.cooldown_ready(sim, "Swiftmend", 15.0):
                for name in ("Regrowth", "Rejuvenation"):
                    if name in target.hots:
                        return (sm[-1], target)
            return None
        return super().emergency_spell(sim, role, target)

    def on_cast_done(self, sim, spell, target):
        if spell.name == "Swiftmend":
            for name in ("Regrowth", "Rejuvenation"):
                if name in target.hots:
                    src = self.book[name][-1]
                    per = target.hots[name][0]
                    ticks = max(1, int(round(src.hot_dur / src.tick_every)))
                    del target.hots[name]
                    sim.apply_heal(spell, target, per * ticks, False, label="Swiftmend")
                    break
