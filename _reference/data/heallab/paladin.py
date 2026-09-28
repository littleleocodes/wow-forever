"""Holy paladin raid healer for the healer lab: Holy Light on the tank (downranked to the deficit) with Blessing of Light on
him, Flash of Light on everything else, Holy Shock as the instant, Divine Favor before a big Holy Light, Lay on Hands when the
tank is about to die; Illumination refunds critical heals."""
import engine as E
import tables as T

PIPELINE = {"spec": "holy-heal", "hand": "holy-raid-healer", "opt": "opt-holy-heal-raid-heal", "tag": "holy"}
BLESSING_OF_LIGHT = {"Holy Light": 400.0, "Flash of Light": 115.0}   # rank 3 on the tank (baseline spell)


class Healer(E.BaseHealer):
    CLASS = "paladin"
    SPEC = "holy-heal"
    ROLES = {"big": "Holy Light", "fast": "Flash of Light", "instant": "Holy Shock"}
    TALENT_SPELLS = {"Holy Shock": "Holy Shock", "Divine Favor": "Divine Favor"}
    MECHANICS = {
        "Illumination": "a critical heal refunds its base mana cost (20%/rank chance)",
        "Divine Favor": "guaranteed critical Holy Light on the tank every 2 min",
        "Holy Shock": "instant 307-333 heal on a 10 s cooldown: the emergency heal",
        "Holy Power": "+1%/rank critical chance with holy spells",
        "Improved Blessing of Wisdom": "+10%/rank Blessing of Wisdom (33 mp5)",
        "Infusion of Light": "+6%/rank Holy Light",
        "Benediction": "instant holy damage costs only: nothing for heals",
        "Lay on Hands": "once, when the tank is under 20% (a 20 min cooldown)",
    }
    SIMULATED = {"Illumination", "Divine Favor", "Holy Shock", "Holy Power", "Improved Blessing of Wisdom", "Infusion of Light", "Healing Light", "Divine Intellect", "Reverence"}
    SHARE_SOURCE = {"Holy Light": "holy_light", "Flash of Light": "flash", "Holy Shock": "holy_shock", "Lay on Hands": "loh"}

    def extra_mp5(self):
        return T.WISDOM_MP5 * 0.1 * self.rank("Improved Blessing of Wisdom")

    def crit_hook(self, spell, sim):
        return 0.01 * self.rank("Holy Power")

    def heal_mult_hook(self, spell, target, sim):
        m = 1.0
        if spell.name == "Holy Light":
            m *= 1 + 0.06 * self.rank("Infusion of Light")
        return m

    def expected(self, spell, target=None, sim=None):
        return super().expected(spell) + (BLESSING_OF_LIGHT.get(spell.name, 0.0) if target is None or target.tank else 0.0)

    def on_heal(self, sim, spell, target, amount, crit):
        if crit and self.rank("Illumination") and sim.rng.random() < 0.2 * self.rank("Illumination"):
            sim.gain_mana(spell.cost, "Illumination")

    def on_cast_done(self, sim, spell, target):
        if target.tank and spell.name in BLESSING_OF_LIGHT:
            sim.apply_heal(spell, target, BLESSING_OF_LIGHT[spell.name] * self.heal_mult(spell, target, sim), False, label=spell.name)

    def before_decide(self, sim):
        tank = sim.tank
        if tank.hp > 0 and tank.frac < 0.2 and self.cooldown_ready(sim, "Lay on Hands", 1200.0) and "Lay on Hands" in self.book:
            sim.cd["Lay on Hands"] = sim.t
            loh = self.book["Lay on Hands"][-1]
            sim.apply_heal(loh, tank, tank.hp_max, False, label="Lay on Hands")
            sim.mana = 0.0   # drains the paladin's mana (beta tooltip)
            sim.gcd_until = sim.t + T.GCD
            return None
        if "Divine Favor" in self.book and self.cooldown_ready(sim, "Divine Favor", 120.0) and tank.deficit > 0.6 * self.expected(self.book["Holy Light"][-1], tank):
            sim.cd["Divine Favor"] = sim.t
            sim.temp_crit = 1.0
            return (self.book["Holy Light"][-1], tank)
        return None
