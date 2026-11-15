"""Warrior PvP layer (duellab, 2026-11-14): Charge at the start, Intercept to close later, Hamstring kept up, Pummel on heals and long
casts, Berserker Rage against fear casts, Intimidating Shout on a healing or fleeing foe, Disarm against a weapon user. Damage
(Mortal Strike, Overpower, Execute, Slam, Heroic Strike, rage) is the spec's own leveling rotation underneath.

Effects the fight lab does not parse: Intercept (a charge: closes and stuns 3 s), Intimidating Shout (an 8 s fear), Berserker Rage
(fear immunity 10 s), Disarm (10 s), Piercing Howl (a 50% slow for 6 s). Charge only before combat starts (Classic's rule).
Not modelled: stances (every ability is usable, rage is not lost by a stance change), Retaliation, Sweeping Strikes' second target.
"""
import dtables as T
from pvp_base import PvPAI


class WarriorPvP(PvPAI):
    keep_range = 0.0
    charges = {"Charge", "Intercept"}

    def effects_for(self, me):
        return {"Intercept": self.intercept, "Intimidating Shout": self.shout, "Berserker Rage": self.zerker,
                "Disarm": self.disarm, "Piercing Howl": self.howl}

    # ------------------------------------------------------------------ effects
    def intercept(self, d, me, foe, spell):
        d.set_dist(T.MELEE)
        foe.apply_cc("stun", 3.0, T.DR_CATEGORY["Intercept"], "Intercept", physical=True)
        me.p.swing_mh = d.t
        return 0.0

    def shout(self, d, me, foe, spell):
        if d.dist <= 10.0:
            foe.apply_cc("fear", 8.0, "fear", "Intimidating Shout")
        if foe.pet_body.alive() and foe.pet_body.dist <= 10.0:
            d.pet_cc(foe, "fear", 8.0)
        return 0.0

    def zerker(self, d, me, foe, spell):
        me.fear_immune_until = d.t + 10.0
        if d.t < me.fear_until:
            me.fear_until = d.t
        return 0.0

    def disarm(self, d, me, foe, spell):
        if foe.p.mh is not None:
            foe.apply_cc("disarm", 10.0, "disarm", "Disarm", physical=True)
        return 0.0

    def howl(self, d, me, foe, spell):
        if d.dist <= 10.0 and d.t >= foe.immune_until:
            foe.slow, foe.slow_until = max(foe.slow if d.t < foe.slow_until else 0.0, 0.5), d.t + 6.0
        return 0.0

    # ------------------------------------------------------------------ decisions
    def off_gcd(self, d, me, foe):
        t = d.t
        if me.p.rage < 20 and me.can("Bloodrage", ignore_gcd=True) and d.dist <= 25.0:
            return "Bloodrage"
        k = self.kited(d, me, foe)
        if k:
            return k
        c = self.foe_cast(d, foe)
        if c is not None:
            if c.name in ("Fear", "Seduction", "Howl of Terror") and me.can("Berserker Rage", ignore_gcd=True):
                return "Berserker Rage"
            if d.dist <= T.MELEE + 0.5 and (c.cast >= 1.0 or c.kind == "channel"):
                for k in ("Pummel", "Shield Bash"):
                    if me.can(k, ignore_gcd=True) and (k != "Shield Bash" or me.p.block > 0):
                        return k
        if d.dist <= T.MELEE + 0.5 and foe.hp_frac() < 0.6:
            for k in ("Recklessness", "Death Wish"):
                if me.can(k, ignore_gcd=True):
                    return k
        return None

    def decide(self, d, me, foe):
        t = d.t
        if foe.stealthed:
            return None
        if d.dist > T.MELEE + 0.5:
            if not d.combat and me.can("Charge"):
                return "Charge"
            if me.can("Intercept"):
                return "Intercept"
            if d.dist <= 10.0 and t >= foe.slow_until and me.can("Piercing Howl"):
                return "Piercing Howl"
            return None
        healing = (c := foe.cast_spell()) is not None and c.kind == "heal"
        if (healing or foe.hp_frac() < 0.3) and t >= foe.fear_immune_until and me.can("Intimidating Shout") \
                and not foe.controlled(t):
            return "Intimidating Shout"
        if foe.hp_frac() < 0.2 and me.can("Execute"):
            return "Execute"
        if t >= foe.slow_until and not foe.controlled(t) and me.can("Hamstring"):
            return "Hamstring"
        if foe.mod.melee and foe.p.mh is not None and t >= foe.disarm_until and me.can("Disarm") and foe.hp_frac() > 0.4:
            return "Disarm"
        return self.rotation(d, me, foe)
