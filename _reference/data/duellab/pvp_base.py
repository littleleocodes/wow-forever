"""The PvP decision layer every class file extends (duellab, 2026-11-14).

A class's PvP play is two layers: its PvP layer (this class and pvp_<class>.py: openers, control, interrupts, defensive cooldowns,
kiting, the PvP trinket) and, under it, its spec's own tuned leveling rotation, the fight lab's `decide` with the opponent as the mob.
The rotation fills every moment the PvP layer leaves, so each spec plays its own damage priority (Shatter combos, Seal Fate, rage
and energy pooling, Missile Barrage) without a second copy of it here.

Hooks (all optional; d = the Duel, me / foe = Side):
  effects_for(me)          {spell name: handler(d, me, foe, spell)} for spells whose PvP effect the fight lab does not parse
  prefight(d, me, foe)     before the duel starts: stealth, a shield, a pet
  intent(d, me, foe)       movement each step: "close", "kite" or "hold"; close_to(d, me) is where closing stops
  while_controlled(...)    while stunned, incapacitated or feared: the trinket, Blink
  while_casting(...)       during a cast or channel (rarely anything)
  off_gcd(...)             before each decision: interrupts and cooldowns off the global cooldown
  decide(...)              the next action on the global cooldown; default: the rotation
  damage_taken(d, me, src, spell, amount)   damage after absorbs (Mana Shield, Divine Shield already handled)
Actions: a spell name or Spell, "wand", "retreat", "advance", "trinket" or None.
"""
import dtables as T

RETALIATION_TRADE = 0.6   # hold swings into Retaliation only while my hit is worth less than this share of its answer (judgment)

HOSTILE = {"Polymorph", "Blind", "Sap", "Fear", "Seduction", "Death Coil", "Howl of Terror", "Psychic Scream", "Intimidating Shout",
           "Hammer of Justice", "Repentance", "Entangling Roots", "Hibernate", "Scatter Shot", "Wyvern Sting", "Counterspell",
           "Kick", "Pummel", "Shield Bash", "Earth Shock", "Silence", "Spell Lock", "Mana Burn", "Dispel Magic", "Purge", "Viper Sting",
           "Disarm", "Gouge", "Cheap Shot", "Kidney Shot", "Garrote", "Ambush", "Pounce", "Ravage", "Bash", "Concussion Blow",
           "Intimidation", "Frost Nova", "Cone of Cold", "Arcane Explosion"}
HEALS = {"Flash Heal", "Greater Heal", "Heal", "Lesser Heal", "Prayer of Healing", "Holy Light", "Flash of Light", "Healing Touch",
         "Regrowth", "Healing Wave", "Lesser Healing Wave", "Chain Heal", "Penance", "Drain Life", "Health Funnel", "Binding Heal"}


class PvPAI:
    auto_attack = True        # a melee class swings while in reach
    keep_range = 0.0          # 0: a melee that closes in; else the distance a ranged side holds
    hostile_buffs = HOSTILE   # spells the fight lab files as buffs that act on the enemy (range-checked)
    ranges = {}               # spell name -> reach (yards) where the data's range is wrong for PvP
    trinket_min_left = 3.0    # trinket a control with at least this long to run ...
    trinket_hp = 0.6          # ... when health is below this share (or always for a long incapacitate or fear)

    def bind(self, d, me):
        self.d, self.me = d, me
        self.effects = dict(self.effects_for(me))
        self.pet_arrives = d.dist / 14.0 if me.p.pet is not None else 0.0
        self.retreat_left = 0.0

    def effects_for(self, me):
        return {}

    # ------------------------------------------------------------------ helpers
    def has(self, me, name):
        return name in me.mod.spells

    def ready(self, me, name):
        return name in me.mod.spells and me.p.ready(name, me.t)

    def talent(self, me, name):
        return me.mod.rank(name) if hasattr(me.mod, "rank") else 0

    def foe_cast(self, d, foe, react=None):
        """The foe's current cast (Spell) once it has run long enough to be seen and answered, else None."""
        s = foe.cast_spell()
        if s is None:
            return None
        if foe.fight.casting:
            started = foe.fight.casting[2]
        else:
            started = foe.fight.channel[1] - foe.fight.channel[3]
        return s if d.t - started >= (T.REACTION if react is None else react) else None

    def melee_foe(self, foe):
        return foe.mod.melee and foe.ai.keep_range <= 0

    # ------------------------------------------------------------------ hooks
    def prefight(self, d, me, foe):
        pass

    def intent(self, d, me, foe):
        if foe.stealthed and not me.stealthed:
            return "hold"
        if self.keep_range <= 0:
            return "close"
        return "close" if d.dist > self.keep_range else "hold"

    def close_to(self, d, me):
        return T.MELEE - 0.5 if self.keep_range <= 0 else self.keep_range

    def while_controlled(self, d, me, foe):
        """Stunned, incapacitated or feared: the PvP trinket when it frees this class from everything that holds it (Side.trinket_clears),
        the control has a while to run, and health is low or the control is a long incapacitate or fear."""
        t = d.t
        left = max(me.stun_until, me.incap_until, me.fear_until) - t
        if left < self.trinket_min_left or not me.trinket_clears(t):
            return None
        long_cc = (t < me.incap_until or t < me.fear_until) and left >= 5.0
        if me.hp_frac() < self.trinket_hp or long_cc:
            return "trinket"
        return None

    def kited(self, d, me, foe):
        """A melee held off by a root or slow while its foe stands at range: the trinket when this class's frees it."""
        t = d.t
        if self.keep_range > 0 or d.dist <= T.MELEE + 0.5:
            return None
        frees = me.trinket_frees(t)
        rooted = "root" in frees and me.root_until - t >= 2.0 and d.dist > 10.0
        slowed = "slow" in frees and me.slow >= 0.4 and me.slow_until - t >= 3.0 and d.dist > 15.0 and me.hp_frac() < 0.7
        return "trinket" if rooted or slowed else None

    def while_casting(self, d, me, foe):
        return None

    def while_inactive(self, d, me, foe):
        return None

    def off_gcd(self, d, me, foe):
        return None

    def decide(self, d, me, foe):
        return self.rotation(d, me, foe)

    fillers = ()              # spells of other schools to cast when the rotation's choice is locked out or out of reach (Fire Blast)

    @staticmethod
    def rotation_decide(me, fn):
        """fn (the module's decide) with the side's restored tuned vetoes (duel.Side.rotation_veto, the dropped-veto audit) under this
        layer's own: a layer's entry for the same spell wins. Without restored vetoes, fn alone."""
        extra = me.rotation_veto
        if not extra:
            return fn()
        old = me.mod.veto
        me.mod.veto = {**extra, **old}
        try:
            return fn()
        finally:
            me.mod.veto = old

    def rotation(self, d, me, foe):
        """The spec's own leveling rotation (the fight lab's decide), with the opponent as the mob. When its choice cannot be cast
        (its school locked by an interrupt, out of reach), the class's fillers, then the wand, so nobody stands idle (2026-11-14: two
        mages that had Counterspelled each other stood for ten seconds and half the mirrors ran out the clock)."""
        if foe.stealthed:
            return None
        a = self.rotation_decide(me, lambda: me.mod.decide(me.fight))
        if a in ("wand", "advance", "shoot", "retreat"):
            return a
        hold = self.hold_swings(d, me, foe)
        if a is not None:
            name = a.name if hasattr(a, "name") else a
            if me.can(name) and not (hold and self.strike(me, name)):
                return a
        for name in self.fillers:
            if me.can(name) and not (hold and self.strike(me, name)):
                return name
        if self.keep_range > 0 and me.p.mana_max > 0 and me.mod.wand_damage() > 0 and d.dist <= 30.0:
            return "wand"
        return None

    def damage_taken(self, d, me, src, spell, amount):
        return amount

    keeps_stealth = ()        # this class's spells that do not end its stealth (the engine's KEEPS_STEALTH has the common ones)

    def cc_immune(self, d, me, kind, name):
        """Whether this side cannot take this control now (a druid's forms against Polymorph and Disarm): refused before
        diminishing returns count it."""
        return False

    def intercepts(self, d, me, src, spell):
        """Whether this side takes `spell` (cast at it by `src`) before it resolves: a Grounding Totem. True ends the spell."""
        return False

    def after_intercept(self, d, me, src, spell):
        pass

    def grounding(self, d, me):
        """Whether a spell cast at this side now would be taken first (a charged Grounding Totem): the other side's layer can pop it
        with something cheap before its control spell."""
        return False

    def pet_held(self, d, me, t):
        return False

    def foe_retaliating(self, foe, t):
        """A free warrior under Retaliation (a buff players see): every melee strike from the front is answered (pvp_warrior); a
        stunned, incapacitated or feared warrior answers nothing."""
        r = getattr(foe.ai, "retaliation", None)
        return bool(r) and t < r[1] and r[0] > 0 and not foe.controlled(t)

    def hold_swings(self, d, me, foe):
        """No white swings (the engine asks) and no weapon strikes from the rotation now: a free warrior's Retaliation, while each of my
        hits is worth less than RETALIATION_TRADE of the one it answers with and the warrior is not nearly dead. 2026-11-14:
        Retaliation had dealt 455-1,168 a duel to paladins, shamans and druids that kept swinging. Holding every swing for its 15 s
        cost a two-hander more than the answers did (the paladin's win rate against the warrior fell from 94% to 57%), and holding at
        an even trade cost the shaman 9 points (each answer also feeds its Lightning Shield). So only a light, fast hitter holds: two
        weapons, Cat Form. A layer may add reasons of its own."""
        return self.foe_retaliating(foe, d.t) and foe.hp_frac() > 0.12 \
            and self.hit_value(me, foe) < RETALIATION_TRADE * self.hit_value(foe, me)

    def retaliation_escape(self, d, me, foe):
        """Out of the warrior's reach while this melee side holds its strikes into Retaliation (hold_swings) and can outrun it: the
        engine turns the layer's intent into "kite" for that time (Duel.run). Validation pass 2 (2026-11-15): holding in place gave the
        warrior its own swings for free (a cat stood in reach doing nothing from 3 s to 13 s and lost 1,700 health). Measured on the
        field builds, 200 duels: the druid against the warrior 11.5% -> 23.5% (attacking through instead: 6.5%), the rogue 11.5% ->
        22.5% (Crippling Poison makes it the faster)."""
        t = d.t
        return self.melee_foe(me) and not me.stealthed and self.hold_swings(d, me, foe) and me.speed(t) > foe.speed(t) + 1e-6

    @staticmethod
    def hit_value(side, target):
        """A side's average white hit on `target` after armor: the main hand's, or with two weapons the mean of the main hand's and the
        off hand's half (the engine's off-hand rule)."""
        import tables as FT   # the fight lab's (duel.py put it first on the path)
        p = side.p
        vals = [k * ((w.dmg_min + w.dmg_max) / 2.0 + (p.attack_power / 14.0 + w.dps_bonus) * w.speed)
                for w, k in ((p.mh, 1.0), (p.oh, 0.5)) if w is not None]
        if not vals:
            return 0.0
        return sum(vals) / len(vals) * (1.0 - FT.armor_mitigation(target.armor(), 60))

    @staticmethod
    def strike(me, name):
        """Whether `name` is a weapon strike that deals damage (what Retaliation answers); control without damage is not."""
        s = me.mod.spells.get(name)
        return s is not None and getattr(s, "kind", "") == "melee" and (getattr(s, "weapon_pct", 0.0) > 0 or getattr(s, "dmg_max", 0.0) > 0)

    def tick(self, d, me, foe):
        """Every step, after both sides decided: traps, totems, timers a layer keeps itself."""
        return None
