"""Holy priest raid healer for the healer lab: Greater Heal on the tank (downranked to the deficit), Flash Heal when it must
land fast, Renew kept on the tank, Prayer of Healing when the group is hurt, Power Word: Shield on a tank in danger, Penance
and Prayer of Mending when talented; Inner Focus before a Greater Heal, Power Infusion on cooldown."""
import engine as E
import tables as T

PIPELINE = {"spec": "holy-heal", "hand": "holy-raid-healer", "opt": "opt-holy-heal-raid-heal", "tag": "holy"}


class Healer(E.BaseHealer):
    CLASS = "priest"
    SPEC = "holy-heal"
    ROLES = {"big": "Greater Heal", "fast": "Flash Heal", "hot": "Renew", "group": "Prayer of Healing", "shield": "Power Word: Shield", "instant": "Penance"}
    TALENT_SPELLS = {"Penance": "Penance", "Prayer of Mending": "Prayer of Mending", "Inner Focus": "Inner Focus", "Power Infusion": "Power Infusion", "Binding Heal": "Binding Heal"}
    MECHANICS = {
        "Inner Focus": "next Greater Heal free and +25% crit, every 3 min",
        "Power Infusion": "+20% healing for 15 s every 3 min (cast on yourself)",
        "Spiritual Guidance": "+5%/rank of Spirit as healing",
        "Inspiration": "a critical heal gives the target +25% armor for 15 s (33%/rank chance)",
        "Improved Power Word: Shield": "+7/14/20% absorb",
        "Soul Warding": "Power Word: Shield without its 4 s cooldown and 15% cheaper",
        "Twin Disciplines": "+1%/rank healing of instant casts",
        "Mental Agility": "-3/7/10% mana cost of instant casts",
        "Penance": "an instant 3-pulse heal on a 12 s cooldown: the emergency heal",
        "Prayer of Mending": "kept on the tank: heals 413 when he is hit, then jumps (5 charges, 10 s cooldown)",
        "Binding Heal": "cast as a Flash Heal (the self-heal part is idle in a raid)",
    }
    SIMULATED = {"Inner Focus", "Power Infusion", "Spiritual Guidance", "Inspiration", "Improved Power Word: Shield", "Soul Warding", "Twin Disciplines", "Mental Agility",
                 "Penance", "Prayer of Mending", "Meditation", "Holy Specialization", "Improved Renew", "Improved Healing", "Divine Fury", "Spiritual Healing", "Mental Strength"}
    SHARE_SOURCE = {"Greater Heal": "greater_heal", "Flash Heal": "flash_heal", "Renew": "renew", "Prayer of Healing": "prayer_of_healing", "Power Word: Shield": "shield",
                    "Heal": "heal", "Lesser Heal": "heal", "Binding Heal": "flash_heal"}

    def extra_healing(self):
        return 0.05 * self.rank("Spiritual Guidance") * self.spirit

    def heal_mult_hook(self, spell, target, sim):
        m = 1.0
        if "instant" in spell.tags:
            m *= 1 + 0.01 * self.rank("Twin Disciplines")
        if spell.name == "Power Word: Shield":
            m *= 1 + [0, 0.07, 0.14, 0.20][min(3, self.rank("Improved Power Word: Shield"))]
        if sim.t < sim.buffs.get("Power Infusion", 0.0):
            m *= 1.2
        return m

    def cost_hook(self, spell, sim):
        f = 1.0
        if "instant" in spell.tags:
            f *= 1 - [0, 0.03, 0.07, 0.10][min(3, self.rank("Mental Agility"))]
        if spell.name == "Power Word: Shield" and self.rank("Soul Warding"):
            f *= 0.85
        return f

    def on_heal(self, sim, spell, target, amount, crit):
        if crit and self.rank("Inspiration") and sim.rng.random() < self.rank("Inspiration") / 3.0:
            target.armor_buff_until = sim.t + 15.0

    def before_decide(self, sim):
        if "Power Infusion" in self.book and self.cooldown_ready(sim, "Power Infusion", 180.0) and sim.mana > 0.2 * self.mana_max:
            sim.cd["Power Infusion"] = sim.t
            sim.buffs["Power Infusion"] = sim.t + 15.0
        if "Inner Focus" in self.book and self.cooldown_ready(sim, "Inner Focus", 180.0) and sim.tank.deficit > 0.5 * self.expected(self.book["Greater Heal"][-1]):
            sim.cd["Inner Focus"] = sim.t
            sim.free_cast, sim.temp_crit = True, 0.25
            return (self.book["Greater Heal"][-1], sim.tank)
        if "Prayer of Mending" in self.book and not any(x.mending for x in sim.targets) and self.cooldown_ready(sim, "Prayer of Mending", 10.0) and sim.tank.hp > 0 and sim.tank.deficit > 0:
            sim.cd["Prayer of Mending"] = sim.t
            sim.mana -= self.cost(self.book["Prayer of Mending"][-1], sim)
            sim.tank.mending = 5
            sim.gcd_until = sim.t + T.GCD
            return None
        return None

    def mending_trigger(self, sim, target):
        pom = self.book.get("Prayer of Mending")
        if not pom or target.mending <= 0:
            return
        sim.apply_heal(pom[-1], target, pom[-1].heal_min * self.heal_mult(pom[-1], target, sim), False)
        target.mending -= 1
        if target.mending > 0:
            others = sorted([x for x in sim.targets if x is not target and x.hp > 0], key=lambda x: x.frac)
            if others:
                others[0].mending, target.mending = target.mending, 0

    def emergency_spell(self, sim, role, target):
        if role == "instant" and "Power Word: Shield" in self.book and target.tank and sim.t >= target.shield_lock and \
                (self.rank("Soul Warding") or self.cooldown_ready(sim, "Power Word: Shield", 4.0)):
            return (self.book["Power Word: Shield"][-1], target)
        return super().emergency_spell(sim, role, target)

    def hot_ok(self, sim, target):
        return True
