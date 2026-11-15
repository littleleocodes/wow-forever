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
        """Stunned, incapacitated or feared: the PvP trinket when it frees this class from what holds it, the control has a while to
        run, and health is low or the control is a long incapacitate or fear."""
        t = d.t
        left = max(me.stun_until, me.incap_until, me.fear_until) - t
        frees = me.trinket_frees(t)
        if left < self.trinket_min_left or not (frees & {"stun", "fear", "polymorph", "charm"}):
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

    def rotation(self, d, me, foe):
        """The spec's own leveling rotation (the fight lab's decide), with the opponent as the mob. When its choice cannot be cast
        (its school locked by an interrupt, out of reach), the class's fillers, then the wand, so nobody stands idle (2026-11-14: two
        mages that had Counterspelled each other stood for ten seconds and half the mirrors ran out the clock)."""
        if foe.stealthed:
            return None
        a = me.mod.decide(me.fight)
        if a in ("wand", "advance", "shoot", "retreat"):
            return a
        if a is not None:
            name = a.name if hasattr(a, "name") else a
            if me.can(name):
                return a
        for name in self.fillers:
            if me.can(name):
                return name
        if self.keep_range > 0 and me.p.mana_max > 0 and me.mod.wand_damage() > 0 and d.dist <= 30.0:
            return "wand"
        return None

    def damage_taken(self, d, me, src, spell, amount):
        return amount

    def pet_held(self, d, me, t):
        return False
