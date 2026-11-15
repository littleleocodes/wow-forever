"""Mage PvP layer (duellab, 2026-11-14): kiting, Frost Nova and Blink against melee, Polymorph to reset, Counterspell on heals and long
casts, Ice Block in an emergency. Damage (Frostbolt, Shatter with Ice Lance, Fingers of Frost, Fire Blast) is the spec's own
leveling rotation underneath.

Effects the fight lab does not parse: Polymorph (incapacitate, broken by damage, the target heals quickly), Blink (20 yards and free of
stuns and roots), Ice Block (10 s immune and inactive; cancelled once Frost Nova is ready again). Not modelled: Mana Shield, Presence of
Mind combos, Evocation in a duel, Arctic Reach's range.
"""
import dtables as T
from pvp_base import PvPAI, HEALS

POLY_REGEN = 0.10   # share of maximum health a polymorphed player regains per second ("will regenerate very quickly"): an assumption


class MagePvP(PvPAI):
    keep_range = 26.0
    auto_attack = False
    fillers = ("Fire Blast", "Ice Lance", "Fireball", "Scorch", "Arcane Missiles")

    def effects_for(self, me):
        return {"Polymorph": self.polymorph, "Blink": self.blink, "Ice Block": self.ice_block}

    # ------------------------------------------------------------------ effects
    def polymorph(self, d, me, foe, spell):
        dur = foe.apply_cc("incap", 50.0, "incap", "Polymorph")
        if dur > 0:
            foe.cc_regen = (d.t + dur, POLY_REGEN)
        return 0.0

    def blink(self, d, me, foe, spell):
        me.stun_until = min(me.stun_until, d.t)
        me.root_until = min(me.root_until, d.t)
        d.set_dist(d.dist + 20.0)
        me.fight.note("Blink")
        return 0.0

    def ice_block(self, d, me, foe, spell):
        me.immune_until = d.t + 10.0
        me.inactive_until = d.t + 10.0
        me.stun_until = min(me.stun_until, d.t)
        me.root_until = min(me.root_until, d.t)
        me.slow_until = min(me.slow_until, d.t)
        me.fight.note("Ice Block")
        return 0.0

    # ------------------------------------------------------------------ decisions
    def while_inactive(self, d, me, foe):
        """Inside Ice Block: leave it once Frost Nova is back and the foe is close, or when it would end anyway."""
        if self.ready(me, "Frost Nova") or d.dist > 15.0:
            me.immune_until = me.inactive_until = d.t
            me.fight.note("Ice Block cancelled")
        return None

    def while_controlled(self, d, me, foe):
        t = d.t
        if t < me.stun_until and me.stun_until - t >= 2.0 and t >= me.incap_until and t >= me.fear_until and self.ready(me, "Blink") \
                and d.dist <= 10.0:
            s = me.mod.spells["Blink"]
            me.stun_until = t   # Blink is cast while stunned
            me.cast(s)
            return None
        return super().while_controlled(d, me, foe)

    def intent(self, d, me, foe):
        t = d.t
        if foe.stealthed:
            return "hold"
        if self.melee_foe(foe):
            stuck = foe.body.rooted(t) or foe.controlled(t)
            if stuck and d.dist < 20.0:
                return "kite"
            if d.dist < 9.0 and not stuck:
                return "kite"
            return "hold" if d.dist <= self.keep_range else "close"
        return super().intent(d, me, foe)

    def off_gcd(self, d, me, foe):
        c = self.foe_cast(d, foe)
        if c is not None and me.can("Counterspell", ignore_gcd=True) and (c.name in HEALS_OR_LONG or c.cast >= 1.5 or c.kind == "channel") \
                and not foe.ai.grounding(d, foe):
            return "Counterspell"
        return None

    def decide(self, d, me, foe):
        t = d.t
        if foe.stealthed:
            return "Frost Nova" if d.dist <= 8.0 and me.can("Frost Nova") else None
        hp = me.hp_frac()
        if hp < 0.2 and me.can("Ice Block") and not me.immune(t) and d.dist <= 10.0:
            return "Ice Block"
        melee = self.melee_foe(foe)
        free = not foe.controlled(t) and not foe.body.rooted(t)
        if melee and free and d.dist <= 8.0:
            if me.can("Frost Nova"):
                return "Frost Nova"
            if me.can("Blink") and me.slow_until <= t:
                return "Blink"
            if me.can("Cone of Cold"):
                return "Cone of Cold"
        if foe.ai.grounding(d, foe) and (me.can("Counterspell", ignore_gcd=True) or me.can("Polymorph")):
            for k in ("Fire Blast", "Ice Lance", "Frostbolt"):   # pop the Grounding Totem with something cheap before a key spell
                if me.can(k):
                    return k
        if melee and free and 8.0 < d.dist <= 30.0 and me.can("Polymorph") and not foe.dots \
                and not me.p.ready("Frost Nova", t) and not me.p.ready("Blink", t) and hp < 0.75:
            return "Polymorph"
        if t < foe.incap_until and foe.incap_name == "Polymorph":
            return None   # a sheep: let it run; casting at it would break it
        a = self.rotation(d, me, foe)
        s = me.mod.spells.get(a) if isinstance(a, str) else a
        if melee and free and d.dist <= 8.0 and s is not None and getattr(s, "cast", 0) > 0 and me.mod.cast_time(s) > 0:
            for k in ("Fire Blast", "Ice Lance", "Cone of Cold"):   # a free melee next to me: instants, or walk away; no cast to be kicked
                if me.can(k):
                    return k
            return "retreat"
        return a


HEALS_OR_LONG = {"Flash Heal", "Greater Heal", "Heal", "Holy Light", "Flash of Light", "Healing Touch", "Regrowth", "Healing Wave",
                 "Lesser Healing Wave", "Chain Heal", "Penance", "Drain Life", "Fear", "Polymorph", "Mind Blast", "Shadow Bolt",
                 "Frostbolt", "Pyroblast", "Starfire", "Lightning Bolt", "Chain Lightning", "Aimed Shot", "Mind Flay", "Arcane Missiles"}
