"""Mage PvP layer (duellab, 2026-11-14): kiting with real distance (Frost Nova, Blink, Cone of Cold, the Frostbolt slow), a Frostbolt
timed to land on a frozen foe (Shatter), Polymorph on a foe, on a hunter's pet or on a heal, Counterspell on heals, crowd control and
the casts that matter, no cast started into an interrupt or control the foe can land in time when walking avoids it, Spell Lock baited
with another school, Remove Lesser Curse, Ice Barrier and Mana Shield kept up, Evocation in a safe window, Presence of Mind, Arcane
Power and Cold Snap, Ice Block with an exit plan, the PvP trinket on fears, Polymorph and slows. The damage is the spec's own leveling
rotation underneath (frost-leveling: Frostbolt, Shatter with Ice Lance and Fingers of Frost, Fire Blast; fire-leveling: Fireball,
Scorch, Pyroblast on Heating Up, Blast Wave; arcane-leveling: Arcane Blast stacks, Arcane Missiles, Arcane Wrath), with the foe's
approach read as it is: the rotation's "the mob walks in" timing holds for a melee foe only (a caster standing at range had made it
wand instead of casting).

Effects the fight lab does not parse (handlers below):
- Polymorph: an incapacitate of up to 50 s (the PvP cap: 10 s), broken by any damage, on a Humanoid or a Beast (a hunter's pet; not a
  demon), the target regenerating POLY_REGEN of its health a second (the tooltip's "will regenerate very quickly"; the client carries
  no regeneration aura on it, so the rate is the server's: an assumption). A pet takes the same cap and no diminishing returns (the
  engine's pets have none). A spell hit roll.
- Blink: 20 yards away from the foe, free of stuns and roots, usable while stunned (Classic). Ice Block: 10 s immune and inactive,
  harmful effects removed (dots, slows, roots, curses, healing reduction: Classic's school-immunity auras, as the paladin layer
  assumes); not usable while stunned (Classic).
- Counterspell: the cast countered and its school locked 10 s, plus Improved Counterspell's silence (2/4 s) whether or not the foe
  was casting (the fight lab added the silence to the lockout). Off the global cooldown (fightlab/spell_gcd.json) like Presence of
  Mind, Arcane Power, Combustion and Cold Snap; the engine cuts a running global cooldown short on those, this layer restores it.
- Mana Shield: 570 physical damage absorbed at 2 mana a point (Forever's tooltip: physical only; the engine's wands are physical too),
  less Arcane Shielding's 17/33%; it breaks when the mana runs out. Ice Barrier recast in the duel (the fight lab casts it at the pull
  only): 819 plus 10% of spell power (client 70888's live tooltip) plus Frost Warding's 20%; no pushback while it holds (the fight lab's
  rule). With ICE_BARRIER_DAMAGE, the talent's own "+15% Frost damage for 1 min, +5% more while shielded" (its tooltip; the fight lab
  omits it): the shield's aura (13033 in client 70938) carries the absorb and the +5%, so the +15% is a separate aura that a dispel of
  the shield (the engine's purge_shields) leaves. Frost Ward and Fire Ward absorb 913 of their school (Frost Warding +20% on Frost
  Ward), cast in the countdown against a foe of that school.
- Evocation: an 8 s channel, mana regeneration x16 (+1,500%) in four 2 s ticks (the fight lab's evocation()), pushed back by damage.
- Presence of Mind and Arcane Power open the duel as at the fight lab's pull (PULL_BURST: the first cast instant under Arcane Power;
  giving them back for this layer to time measured worse: arcane-pvp against arms-pvp 59.5% -> 85%, against retribution-pvp 1.5% ->
  12.5%); Cold Snap finishes the cooldown of every other Frost spell (Frost Nova, Cone of Cold, Ice Barrier, Ice Block, Ice Lance,
  Frost Ward).
- Remove Lesser Curse on yourself: one Curse or Bane (Tongues first, then Exhaustion, Bane of Agony, the others).

Decisions:
- Casts against interrupts and control: before a cast-time spell (or channel) the layer lists the foe's ready abilities that could stop
  it (Kick, Pummel, Shield Bash, Gouge, Kidney Shot, Bash, Concussion Blow, Hammer of Justice, Intimidating Shout, Psychic Scream, Howl
  of Terror, Blind, Intercept, Feral Charge, Repentance, Earth Shock, Silence, a Felhunter's Spell Lock (also on its way in), a ready
  Grounding Totem; Death Coil and Scatter Shot only against control casts, a mage's Counterspell only against damage casts once it is
  below COUNTER_DAMAGE_AT health, a Grounding Totem against damage casts once the shaman is below GROUNDING_HP: as the foe layers use
  them), each at its reach, a reaction time after the cast is seen, with a free melee foe walking in at its speed meanwhile (its own
  arrival in reach counts too: a melee foe beating on the mage mid-cast pushes it back and lands its strikes). When
  walking away gets the mage out of all of them inside its bolt's reach (it is faster, the foe is held, or a ranged foe is not closing
  in), it walks and uses instants; when not, a short-reach answer gets instants first, a school lockout (Kick, Pummel, Shield Bash,
  Earth Shock, Counterspell, Spell Lock) is baited with a cast of another school (Fireball for Frost; Spell Lock wants 2 s or more by
  the base cast time), else the cast goes out. Against a melee foe walking in, a cast longer than MELEE_HOLD_MIN that it would stop or
  reach is not started unless the mage is cornered (Frost Nova, Blink and Cone of Cold all down): instants, and Frost Nova when it
  arrives (measured: pvp-frost against enhancement-pvp 25.5% -> 42.5%; Arcane Blast's 1.5 s casts still go out).
- Against a melee foe: Frost Nova once it is inside the nova's reach (root diminishing returns at least half, not under Blessing of
  Freedom); Blink when it is in reach and Frost Nova is not there, or out of a stun or root with it beside you; Cone of Cold on one not
  slowed; Polymorph when all three are down (Presence of Mind makes it instant; else only when nothing can stop the cast); Cold Snap
  for a second Frost Nova below 60% health. While the mage's own root holds the foe, nothing that deals damage: it walks away until the
  root leaves just the time for a cast that lands inside it (a Shatter Frostbolt), up to its range. A Frostbolt (any build that has it)
  slows a free melee foe that is not slowed. Ice Lance never breaks the mage's own root early unless it kills.
- Against a ranged foe: stand inside the bolt's reach, out of the foe's short-range control (Psychic Scream, Howl of Terror, Hammer
  of Justice, Blind, Scatter Shot) and of a stopper the walk verdict says can be left behind; Frost Nova and walk when it comes inside
  the nova; Polymorph a hunter's pet (Beasts only; a demon cannot be), and no cast that the pet, still running in, would reach and
  push back before it ends; no cast-time spell, Polymorph or Counterspell into a charged Grounding Totem (Ice Lance, Fire Blast or
  Scorch pops it). Ice Lance is no filler (8 s cooldown, four times the damage frozen).
- Counterspell (off the global cooldown, a reaction time after the cast is seen; never into a paladin's Voice of Truth or a charged
  Grounding Totem): heals, crowd control, channels that heal, and
  damage casts of 1.4 s or more of the foe's main school (warlock and priest Shadow, shaman and druid Nature, paladin Holy) or below
  COUNTER_DAMAGE_AT health; it cuts the mage's own cast short for a heal or crowd control, and for a damage cast worth it when the own
  cast still has a second or more to run (a pushed-back cast). With Counterspell down, Polymorph (instant with Presence of Mind) stops
  a heal it can beat.
- Polymorph on the foe as a peel when a melee foe is on the mage with Frost Nova, Blink and Cone of Cold down, only on a foe above
  SHEEP_NEED_FOE_HP health and at full diminishing returns unless the mage is below SHEEP_DESPERATE (the sheep regenerates the foe);
  never into a ready Devour Magic or a druid's form. A sheep is not damaged until the opener is timed to land as it ends, or at once
  from range when the foe is below OPEN_SHEEP_BELOW health.
- Ice Block below BLOCK_AT health while the foe has as much or more (below BLOCK_ALWAYS always), only when it can change the duel
  rather than delay it: the foe below BLOCK_FOE_FIRST health, dots on the mage worth a third of its health (above 12%), or a melee foe
  with Frost Nova and Blink back inside the block; Cold Snap for a second one with the foe below BLOCK_FOE_SECOND. It is left early only
  to Counterspell a heal or crowd control, or against a melee foe once Frost Nova and Blink are both back (4 s in); else it runs 10 s.
- Mana: Evocation below EVO_MANA while the foe sits in the mage's Polymorph (the mage away from a melee foe) or in Ice Block for most
  of the channel, and no dot ticks on the mage. Mana Shield in the countdown against a physical foe (or a melee pet's owner), recast in
  the duel only below SHIELD_BELOW health and above SHIELD_MANA mana once Ice Barrier is gone. Ice Barrier again whenever it is down (not
  into a Felhunter's ready Devour Magic, which eats it and heals the demon). Remove Lesser Curse: Curse of Tongues when the warlock
  cannot curse again within 2.5 s (silenced, its school locked, controlled), else at most every DECURSE_EVERY s (it re-curses at once:
  a global-cooldown war); Curse of Exhaustion against a melee foe (every DECURSE_EVERY / 2 s); a bane worth 450 (every DECURSE_EVERY
  s); each cast removes what it was cast for.
- Presence of Mind (when ready after the opener): an instant Polymorph when the cast would be stopped and the foe's trinket cannot
  break the sheep at once, or an instant nuke that kills. Arcane Power (likewise): a held foe at range or one below half health. Cold Snap (off the global cooldown): a second Ice Block, or a second Frost Nova below
  COLD_SNAP_NOVA_HP health with Blink down.
- The trinket (fear, Polymorph, slow): the base rule for fears and Polymorph; a slow of 50%+ with 4+ s left while a free melee foe is
  within 12 yards, below SLOW_TRINKET_HP health, when the mage can then walk away (the foe held, or Frost Nova ready; Blink first when
  the foe is in reach).
- Measured (2026-11-14, 200 duels a matchup): recasting Mana Shield whenever it broke cost the long fights (pvp-frost against
  feral-combat-pvp 44% wins, below half health only 81.5%; fire-pvp 25.5% -> 81.5%, arcane-pvp 4.5% -> 61%).

Not modelled: single-target spells at the foe's pet (only Polymorph and the area spells reach it); Slow and Spellsteal (not in
Forever's book); fake casts (the engine's fixed reaction time never sees them); Blizzard and Flamestrike; Amplify and Dampen Magic;
Mage Armor (the fight lab's Ice Armor stays on); line of sight. Mana Shield is not seen by the foe's dispels (only Ice Barrier's
absorb is). The foe's layers decide their own interrupts; the stopper list here assumes each ready one would be used.
"""
import copy
import re

import duel  # noqa: F401  (puts the fight lab first on sys.path: engine and tables are its copies)
import dtables as T
import tables as FT
from pvp_base import PvPAI, HEALS

EPS = 1e-9

# ---- tooltip numbers and assumptions
POLY_REGEN = 0.10           # share of maximum health a polymorphed player regains a second (assumption, see the docstring)
BLINK_YARDS = 20.0          # Blink: "Teleports the caster 20 yards forward"
ICE_BLOCK_SECS = 10.0
EVO_TICKS, EVO_EVERY, EVO_MULT = 4, 2.0, 16.0   # Evocation: 8 s, regeneration +1,500% (the fight lab's evocation(): 4 x 16 x a tick)
ICE_BARRIER_DAMAGE = True   # the talent's +15% Frost damage for 1 min and +5% while shielded (its tooltip); False: the fight lab's model
IB_BUFF, IB_SHIELDED, IB_SP_COEF = 0.15, 0.05, 0.10
WARD_SECS = 30.0

# ---- decisions (judgment, not measured)
BLOCK_AT = 0.22             # Ice Block below this share of health while the foe has as much or more
BLOCK_ALWAYS = 0.12         # ... and below this always
BLOCK_FOE_FIRST = 0.60      # an Ice Block that only delays a lost duel is not taken: the foe below this (or see block_helps)
BLOCK_FOE_SECOND = 0.40     # ... and below this for a second one after Cold Snap
EVO_MANA = 0.35             # Evocation below this share of mana, in a safe window
SHIELD_MANA = 0.30          # Mana Shield only above this share of mana ...
SHIELD_BELOW = 0.50         # ... and below this share of health when recast in the duel (always: frost 44% -> 81.5% against feral-combat-pvp; each recast costs a GCD and up to 1,140 mana)
COUNTER_DAMAGE_AT = 0.50    # Counterspell any damage cast below this share of health
KITE_MARGIN = 0.35          # a walk ends when the hold leaves the cast time plus this (a Shatter lands inside the root)
SLOW_TRINKET_HP = 0.75
DECURSE_EVERY = 20.0        # Curse of Tongues removed at most this often while the warlock can curse again at once (a GCD war)
COLD_SNAP_NOVA_HP = 0.60
MELEE_HOLD = True           # no cast a melee foe walking in would stop or reach, unless cornered (instants and Frost Nova instead) ...
MELEE_HOLD_MIN = 1.6        # ... for casts longer than this (a global-cooldown-length cast mostly lands before hits or kicks matter)
PULL_BURST = True           # Presence of Mind and Arcane Power open the duel as at the fight lab's pull (the first cast instant under
#                           # Arcane Power); False: the countdown gives them back and this layer times them
GROUNDING_HP = 0.60         # the shaman layer's GROUND_HP: below it a Grounding Totem also takes damage casts
OPEN_SHEEP_BELOW = 0.85     # a sheeped foe below this share of health is opened on at once (it regenerates)
SHEEP_NEED_FOE_HP = 0.60    # Polymorph as a peel only on a foe above this share of health (it regenerates in it) ...
SHEEP_DESPERATE = 0.35      # ... unless the mage is below this

HEALS_ALL = set(HEALS) | {"Riptide", "Holy Shock (heal)", "Rejuvenation", "Renew", "Penance (heal)", "Mend Pet"}
CC_CASTS = {"Polymorph", "Fear", "Seduction", "Hibernate", "Entangling Roots", "Mind Control", "Howl of Terror", "Banish", "Scare Beast",
            "Repentance"}
HEAL_CHANNELS = {"Drain Life", "Health Funnel", "Tranquility", "Penance (heal)"}
MAIN_SCHOOL = {"warlock": "shadow", "priest": "shadow", "shaman": "nature", "druid": "nature", "paladin": "holy"}
PHYSICAL_FOES = {"warrior", "rogue", "hunter"}
MY_ROOTS = {"Frost Nova", "Frostbite"}                     # my roots that any damage ends (dtables.ROOT_BREAK)
MY_CURSES = ("Curse of Tongues", "Curse of Exhaustion", "Curse of the Elements", "Curse of Weakness", "Curse of Recklessness")
BANES = ("Bane of Agony", "Bane of Doom")
DAMAGE_CASTS = ("Frostbolt", "Fireball", "Frostfire Bolt", "Scorch", "Pyroblast", "Arcane Blast", "Arcane Wrath", "Arcane Missiles",
                "Blizzard", "Flamestrike")
# a foe ability that stops a cast of mine (interrupt, silence, stun, fear, incapacitate) and its reach in yards (the foe layer's
# ranges, else this); a second number is the shortest distance it works from (a charge)
STOPPERS = {
    "Pummel": (5.5, 0.0), "Shield Bash": (5.5, 0.0), "Kick": (5.5, 0.0), "Gouge": (5.5, 0.0), "Kidney Shot": (5.5, 0.0),
    "Bash": (5.5, 0.0), "Concussion Blow": (5.5, 0.0), "Hammer of Justice": (10.0, 0.0), "Intimidating Shout": (10.0, 0.0),
    "Psychic Scream": (8.0, 0.0), "Howl of Terror": (10.0, 0.0), "Blind": (10.0, 0.0), "Intercept": (25.0, 8.0),
    "Feral Charge": (25.0, 8.0), "Repentance": (20.0, 0.0), "Earth Shock": (20.0, 0.0), "Scatter Shot": (15.0, 0.0),
    "Silence": (30.0, 0.0), "Counterspell": (30.0, 0.0), "Death Coil": (30.0, 0.0),
}
MELEE_STOPPERS = {"Pummel", "Shield Bash", "Kick", "Gouge", "Kidney Shot", "Bash", "Concussion Blow"}
SPELL_STOPPERS = {"Hammer of Justice", "Repentance", "Earth Shock", "Silence", "Counterspell", "Death Coil", "Psychic Scream",
                  "Howl of Terror"}
CC_ONLY = {"Death Coil", "Scatter Shot"}                   # the foe layers spend these only on a control or heal cast
LOCK_KICKS = {"Pummel", "Shield Bash", "Kick", "Counterspell", "Spell Lock"}   # school lockouts a bait can draw (Earth Shock is no
#                                                                              # bait target: it hits for about 600 and locks only 2 s)
# the foe's short-range controls a mage keeps out of while the foe is free (yards)
SHORT_CONTROLS = {"Psychic Scream": 8.0, "Howl of Terror": 10.0, "Hammer of Justice": 10.0, "Blind": 10.0, "Intimidating Shout": 10.0,
                  "Scatter Shot": 15.0}
SELF_SPELLS = ("Ice Barrier", "Mana Shield", "Ice Block", "Blink", "Evocation", "Presence of Mind", "Cold Snap", "Arcane Power",
               "Combustion", "Remove Lesser Curse", "Frost Ward", "Fire Ward")
COLD_SNAP_RESETS = ("Frost Nova", "Cone of Cold", "Ice Barrier", "Ice Block", "Ice Lance", "Frost Ward")
AREA = ("Frost Nova", "Cone of Cold", "Arcane Explosion", "Blast Wave")
LAYER_SPELLS = {"Cold Snap", "Evocation", "Presence of Mind", "Arcane Power", "Ice Block", "Polymorph", "Counterspell", "Blink",
                "Mana Shield", "Remove Lesser Curse", "Frost Ward", "Fire Ward"}   # this layer's, never the rotation's


def dr_factor(side, cat, t):
    """The share of its duration the next control of this diminishing-returns category would last on `side` (1, 0.5, 0.25, 0)."""
    if not cat:
        return 1.0
    rec = side.dr.get(cat)
    n = rec[0] if rec and t < rec[1] + T.DR_RESET else 0
    return T.DR_STEPS[min(n, len(T.DR_STEPS) - 1)]


def _num(rx, text, default):
    m = re.search(rx, text or "")
    return float(m.group(1).replace(",", "")) if m else default


class MagePvP(PvPAI):
    keep_range = 28.0
    auto_attack = False
    fillers = ("Fire Blast", "Frostbolt", "Fireball", "Scorch", "Arcane Missiles")

    # ------------------------------------------------------------------ set-up
    def bind(self, d, me):
        super().bind(d, me)
        mod = me.mod
        sp = mod.spells
        for name in ("Presence of Mind", "Arcane Power", "Combustion", "Arcane Blast"):
            if not mod.rank(name):   # talents the fight lab gates by rank, not by its spell list
                sp.pop(name, None)
        self.fire = mod.is_fire() or mod.is_frostfire()
        self.arcane = mod.is_arcane()
        self.main_school = "fire" if self.fire else ("arcane" if self.arcane else "frost")
        for name in SELF_SPELLS:   # cast on yourself: no target, no range, no hit roll (each one this layer's handler)
            s = sp.get(name)
            if s is not None:
                c = copy.copy(s)
                c.target, c.kind = "self", "buff"
                sp[name] = c
        reach = 1 + mod.tv("Arctic Reach", 0) / 100
        fire_reach = mod.tv("Flame Throwing", 0)
        arcane_reach = mod.tv("Arcane Geometry", 0)
        self.ranges = {}
        for name, s in sp.items():
            if s.target == "self":
                continue
            base = s.range or 30.0
            if name in ("Frostbolt", "Ice Lance", "Blizzard"):
                base *= reach
            if mod.sch(s, "fire") and not mod.sch(s, "frost") and name != "Blast Wave":
                base += fire_reach
            if mod.sch(s, "arcane") and name != "Arcane Explosion":
                base += arcane_reach
            self.ranges[name] = base
        self.ranges.update({"Frost Nova": 10.0 * reach, "Cone of Cold": 10.0 * reach, "Arcane Explosion": 10.0, "Blast Wave": 10.0})
        self.poly_range = self.ranges.get("Polymorph", 30.0)
        if self.fire and "Fireball" in sp:
            self.main = "Fireball"
        elif self.arcane and "Arcane Blast" in sp:
            self.main = "Arcane Blast"
        else:
            self.main = next((n for n in ("Frostbolt", "Fireball", "Arcane Missiles") if n in sp), None)
        rng = [self.ranges.get(n, 30.0) for n in ("Frostbolt", "Fireball", "Arcane Blast", "Arcane Missiles") if n in sp]
        self.bolt_range = min(36.0, max(rng)) if rng else 30.0
        self.keep_range = self.bolt_range - 2.0
        self.fillers = tuple(n for n in ("Fire Blast", "Frostbolt", "Fireball", "Scorch", "Arcane Missiles", "Arcane Blast")
                             if n in sp)   # (Ice Lance is no filler: 8 s cooldown, worth four times as much on a frozen foe)
        self.mshield_per = 2.0 * (1 - mod.tv("Arcane Shielding", 0) / 100)
        self.cs_silence = mod.tv("Improved Counterspell", 0)
        self.frost_warding = mod.tv("Frost Warding", 2) / 100
        # state
        self._t = -1.0
        self._verdicts = {}
        self.gcd_before = 0.0
        self.sheep_target = None       # "pet" or "player": the Polymorph being cast
        self.sheep_until = 0.0         # my Polymorph on the foe holds until
        self.pet_sheep_until = 0.0     # my Polymorph on its pet
        self.block_start = -99.0
        self.mshield = 0.0             # Mana Shield's absorb left
        self.mshield_until = 0.0
        self.wards = {}                # school -> [absorb, until]
        self.ib_until = 0.0            # Ice Barrier's damage buff
        self.evo_left, self.evo_next = -1, 0.0
        self.pom_for = None            # what Presence of Mind was taken for
        self.control_since = None      # when the current stun, incapacitate or fear on me began
        self.decursed_at = -99.0
        self.decurse_target = None
        for k in ("blinks", "sheeps", "pet_sheeps", "counters", "blocks", "evocations", "decurses", "baits"):
            me.stats.setdefault(k, 0)
        self._wrap(me)

    def _wrap(self, me):
        """Instance-level wrappers on this side's own module: Ice Barrier's damage buff."""
        mod, ai = me.mod, self
        # the fight lab models Frigid Power too since 2026-11-19 (mage.ICE_BARRIER_DAMAGE); in a duel this layer's bonus below is the
        # only one, so its numbers stay as they were (the duel recasts Ice Barrier, which the fight lab's pull-time buff would not see)
        mod.ib_damage = False
        if ICE_BARRIER_DAMAGE and "Ice Barrier" in mod.spells:
            base_dm, base_pm = mod.damage_multiplier, mod.periodic_multiplier

            def bonus(spell):
                if not mod.sch(spell, "frost"):
                    return 1.0
                t = me.t
                if t >= ai.ib_until:
                    return 1.0
                return 1.0 + IB_BUFF + (IB_SHIELDED if me.p.absorb > 0 and t < me.p.absorb_until else 0.0)

            mod.damage_multiplier = lambda spell, frozen, _b=base_dm: _b(spell, frozen) * bonus(spell)
            mod.periodic_multiplier = lambda spell, _b=base_pm: _b(spell) * bonus(spell)

    def effects_for(self, me):
        return {"Polymorph": self.e_polymorph, "Blink": self.e_blink, "Ice Block": self.e_ice_block, "Counterspell": self.e_counterspell,
                "Mana Shield": self.e_mana_shield, "Ice Barrier": self.e_ice_barrier, "Evocation": self.e_evocation,
                "Presence of Mind": self.e_pom, "Cold Snap": self.e_cold_snap, "Arcane Power": self.e_arcane_power,
                "Remove Lesser Curse": self.e_decurse, "Frost Ward": self.e_ward, "Fire Ward": self.e_ward}

    def prefight(self, d, me, foe):
        """The countdown: the fight lab's pull put Ice Barrier up (kept, with its damage buff) and spent Presence of Mind and Arcane Power
        (given back: this layer times them). A ward against a foe of its school; Mana Shield against a physical foe."""
        p, t = me.p, d.t
        if p.absorb > 0 and t < p.absorb_until:
            self.ib_until = t + 60.0
        for name in (() if PULL_BURST else ("Presence of Mind", "Arcane Power")):
            if p.buffs.pop(name, None) is not None:
                p.cooldowns[name] = t
                if name == "Presence of Mind" and not me.mod.rank("Combustion"):
                    p.cooldowns.pop("Combustion", None)
        for school, ward in (("frost", "Frost Ward"), ("fire", "Fire Ward")):
            if self.foe_school(foe) == school and ward in me.mod.spells:
                self.pre_cast(me, ward)
        if self.physical_foe(foe) and "Mana Shield" in me.mod.spells:
            self.pre_cast(me, "Mana Shield")

    def pre_cast(self, me, name):
        s = me.mod.spells[name]
        cost = me.mod.mana_cost(s)
        if me.p.mana < cost:
            return
        me.p.mana -= cost
        if s.cooldown:
            me.p.cooldowns[name] = me.t + s.cooldown
        me.fight.casts[name] = me.fight.casts.get(name, 0) + 1
        self.effects[name](self.d, me, me.foe, s)

    # ------------------------------------------------------------------ effects
    def lands(self, me, spell):
        """A spell hit roll against a same-level player (the fight lab's spell table, Precision included)."""
        hit = 1.0 - FT.spell_miss(0) + me.mod.hit_bonus(spell) + me.p.spell_hit
        return me.fight.rng.random() <= min(FT.SPELL_HIT_CAP, hit)

    def e_polymorph(self, d, me, foe, spell):
        target, self.sheep_target = self.sheep_target or "player", None
        t = d.t
        if target == "pet":
            pb = foe.pet_body
            if not pb.alive() or not self.beast_pet(foe):
                me.fight.note("Polymorph: no pet to sheep")
                return 0.0
            if not self.lands(me, spell):
                me.fight.note("Polymorph MISS (pet)")
                return 0.0
            d.pet_cc(foe, "incap", T.PVP_CC_CAP)
            self.pet_sheep_until = t + T.PVP_CC_CAP
            me.stats["pet_sheeps"] += 1
            return 0.0
        if foe.immune(t) or not self.lands(me, spell):
            me.fight.note(f"Polymorph {'immune' if foe.immune(t) else 'MISS'}")
            return 0.0
        dur = foe.apply_cc("incap", 50.0, T.DR_CATEGORY.get("Polymorph", "incap"), "Polymorph")
        if dur > 0 and t < foe.incap_until and foe.incap_name == "Polymorph":
            foe.cc_regen = (t + dur, POLY_REGEN)
            self.sheep_until = t + dur
            me.stats["sheeps"] += 1
        return 0.0

    def e_blink(self, d, me, foe, spell):
        t = d.t
        me.stun_until = min(me.stun_until, t)
        me.root_until = min(me.root_until, t)
        d.set_dist(d.dist + BLINK_YARDS)
        me.stats["blinks"] += 1
        me.fight.note(f"Blink ({d.dist:.0f} yd)")
        return 0.0

    def e_ice_block(self, d, me, foe, spell):
        t = d.t
        me.immune_until = me.inactive_until = t + ICE_BLOCK_SECS
        self.block_start = t
        me.fight.casting = me.fight.channel = None
        me.stun_until, me.root_until, me.slow_until = min(me.stun_until, t), min(me.root_until, t), min(me.slow_until, t)
        me.dots = []
        for n in MY_CURSES + ("Mortal Strike", "Wound Poison", "Vampiric Embrace"):
            me.debuffs.pop(n, None)
        me.zone_slows.clear()
        me.cast_slows.clear()
        self.evo_left = -1
        me.stats["blocks"] += 1
        me.fight.note("Ice Block")
        return 0.0

    def e_counterspell(self, d, me, foe, spell):
        self.restore_gcd(me)
        t = d.t
        if foe.immune(t) or not self.lands(me, spell):
            me.fight.note(f"Counterspell {'immune' if foe.immune(t) else 'MISS'}")
            return 0.0
        if foe.is_casting():
            foe.interrupt(spell.interrupt or 10.0, "Counterspell")
            me.fight.interrupts += 1
        if self.cs_silence > 0:
            foe.apply_cc("silence", self.cs_silence, None, "Improved Counterspell")
        me.stats["counters"] += 1
        return 0.0

    def e_mana_shield(self, d, me, foe, spell):
        self.mshield = getattr(spell, "absorb", 0.0) or _num(r"Absorbs (\d[\d,]*)", spell.text, 570.0)
        self.mshield_until = d.t + 60.0
        me.fight.note(f"Mana Shield ({self.mshield:.0f})")
        return 0.0

    def e_ice_barrier(self, d, me, foe, spell):
        p, t = me.p, d.t
        amount = ((getattr(spell, "absorb", 0.0) or 819.0) + IB_SP_COEF * p.spell_power) * (1 + self.frost_warding)
        p.absorb, p.absorb_until = amount, t + 60.0
        self.ib_until = t + 60.0
        me.fight.note(f"Ice Barrier ({amount:.0f})")
        return 0.0

    def e_evocation(self, d, me, foe, spell):
        ch = copy.copy(spell)
        ch.kind, ch.channel, ch.dot, ch.dot_ticks, ch.dot_dur, ch.dmg_min, ch.dmg_max = "channel", 8.0, 0.0, EVO_TICKS, 8.0, 0.0, 0.0
        me.fight.channel = [ch, d.t + EVO_EVERY, EVO_TICKS, EVO_EVERY, True]
        me.fight.channel_lost = 0.0
        me.fight.cast_hits = 0
        self.evo_left, self.evo_next = EVO_TICKS, d.t + EVO_EVERY
        me.stats["evocations"] += 1
        me.fight.note("Evocation")
        return 0.0

    def e_pom(self, d, me, foe, spell):
        self.restore_gcd(me)
        me.p.buffs["Presence of Mind"] = {"until": d.t + 60.0}
        me.fight.note(f"Presence of Mind ({self.pom_for})")
        return 0.0

    def e_arcane_power(self, d, me, foe, spell):
        self.restore_gcd(me)
        me.p.buffs["Arcane Power"] = {"until": d.t + (me.mod.tv("Arcane Power", 0) or 15.0)}
        me.fight.note("Arcane Power")
        return 0.0

    def e_cold_snap(self, d, me, foe, spell):
        self.restore_gcd(me)
        for n in COLD_SNAP_RESETS:
            me.p.cooldowns.pop(n, None)
        me.fight.note("Cold Snap")
        return 0.0

    def e_decurse(self, d, me, foe, spell):
        """Remove Lesser Curse: the curse or bane the decision named (decurse_target), else Tongues, Exhaustion, a bane, the others."""
        t = d.t
        live = [n for n in MY_CURSES if (me.debuffs.get(n) or {}).get("until", 0) > t]
        gone = None
        want, self.decurse_target = self.decurse_target, None
        bane = max((x for x in me.dots if x[0] in BANES), key=lambda x: x[1] * x[2], default=None)
        if want in live:
            gone = want
        elif want == "bane" and bane is not None:
            gone = None
        elif "Curse of Tongues" in live:
            gone = "Curse of Tongues"
        elif "Curse of Exhaustion" in live:
            gone = "Curse of Exhaustion"
        if gone is None and bane is not None:
            me.dots.remove(bane)
            gone = bane[0]
        elif gone is None and live:
            gone = live[0]
        if gone in MY_CURSES:
            me.debuffs.pop(gone, None)
            if gone == "Curse of Exhaustion" and t < me.slow_until:
                me.slow_until = t
        if gone:
            me.stats["decurses"] += 1
        me.fight.note(f"Remove Lesser Curse: {gone or 'nothing'}")
        return 0.0

    def e_ward(self, d, me, foe, spell):
        school = "frost" if spell.name == "Frost Ward" else "fire"
        amount = _num(r"Absorbs (\d[\d,]*)", spell.text, 913.0) * (1 + (self.frost_warding if school == "frost" else 0.0))
        self.wards[school] = [amount, d.t + WARD_SECS]
        me.fight.note(f"{spell.name} ({amount:.0f})")
        return 0.0

    # ------------------------------------------------------------------ incoming damage
    def damage_taken(self, d, me, src, spell, amount):
        t = d.t
        school = (getattr(spell, "school", None) or "physical").lower()
        physical = school == "physical" or getattr(spell, "kind", "") in ("melee", "ranged")
        if amount > 0 and not physical:
            for s, w in self.wards.items():
                if s in school and w[0] > 0 and t < w[1]:
                    a = min(w[0], amount)
                    w[0] -= a
                    amount -= a
                    me.fight.note(f"{s.title()} Ward absorbs {a:.0f}")
        if amount > 0 and physical and self.mshield > 0 and t < self.mshield_until:
            a = min(self.mshield, amount, me.p.mana / self.mshield_per)
            me.p.mana -= a * self.mshield_per
            self.mshield -= a
            amount -= a
            if me.p.mana < self.mshield_per or self.mshield <= 0.5:
                self.mshield = 0.0
        return amount

    # ------------------------------------------------------------------ helpers
    def restore_gcd(self, me):
        me.p.gcd_until = max(me.p.gcd_until, self.gcd_before)

    def cast_free(self, me, name):
        """An off-global-cooldown spell now, the running global cooldown kept."""
        self.gcd_before = me.p.gcd_until
        ok = me.cast(name)
        self.restore_gcd(me)
        return ok

    def beast_pet(self, foe):
        """A pet Polymorph works on: a hunter's beast (a warlock's demons are neither Beasts nor Humanoids)."""
        pet = foe.p.pet
        return pet is not None and pet.alive and foe.cls == "hunter"

    def physical_foe(self, foe):
        """A foe whose damage on the mage is mostly physical: a weapon class, a melee, or a melee pet beside the mage (a Felhunter,
        a Succubus; the engine's wands are physical too)."""
        pet = foe.p.pet
        return foe.cls in PHYSICAL_FOES or self.melee_foe(foe) or (pet is not None and pet.alive and not pet.caster)

    def pet_on_me(self, foe):
        pet = foe.p.pet
        return pet is not None and pet.alive and pet.engaged and not pet.caster

    def foe_school(self, foe):
        """The school most of the foe's spell damage comes in (wards)."""
        if foe.cls == "mage":
            m = foe.mod
            return "fire" if (m.is_fire() or m.is_frostfire()) else ("arcane" if m.is_arcane() else "frost")
        if foe.cls == "warlock":
            return "fire" if ("Conflagrate" in foe.mod.spells or foe.mod.spec.startswith("destruction")) else "shadow"
        return MAIN_SCHOOL.get(foe.cls, "physical")

    def my_sheep(self, foe, t):
        return t < self.sheep_until and t < foe.incap_until and foe.incap_name == "Polymorph"

    def pet_sheeped(self, foe, t):
        return t < self.pet_sheep_until and t < foe.pet_body.incap_until

    def held_for(self, foe, t):
        """Seconds the foe cannot come closer: stunned, incapacitated, feared, rooted or in Ice Block."""
        return max(foe.stun_until, foe.incap_until, foe.fear_until, foe.root_until, foe.inactive_until) - t

    def acting_in(self, foe, t):
        """Seconds until the foe can act (cast, strike) again: stunned, incapacitated, feared or in Ice Block (not rooted)."""
        return max(0.0, max(foe.stun_until, foe.incap_until, foe.fear_until, foe.inactive_until) - t)

    def my_root(self, foe, t):
        return t < foe.root_until and foe.root_name in MY_ROOTS

    def cast_time(self, me, name):
        s = me.mod.spells.get(name) if isinstance(name, str) else name
        return me.mod.cast_time(s) if s is not None else 99.0

    def nuke_time(self, me):
        s = me.mod.spells.get(self.main) if self.main else None
        if s is None:
            return 2.5
        return self.cast_len(me, s)

    def casting_spell(self, me, a):
        """The Spell an action would start as a cast or channel (None for instants, movement and the wand)."""
        s = me.mod.spells.get(a) if isinstance(a, str) else a
        if s is None or not hasattr(s, "kind") or s.kind in ("melee", "ranged"):
            return None
        if s.kind == "channel" or s.channel > 0:
            return s
        return s if me.mod.cast_time(s) > 0 else None

    def cast_len(self, me, s):
        return s.channel if (s.kind == "channel" or s.channel > 0) else me.mod.cast_time(s)

    def stoppers(self, d, me, foe, c, cc=False):
        """The foe's ready abilities that could stop a cast of `c` seconds started now (an interrupt, silence, stun, fear or
        incapacitate a reaction time after it is seen), each with the distance the mage would need for the cast to be out of its reach;
        a free melee foe walks in at its speed meanwhile. cc: the cast is a control or heal (Death Coil and Scatter Shot answer those)."""
        t = d.t
        if t < foe.inactive_until and foe.inactive_until - t >= c:
            return []
        act_in = self.acting_in(foe, t)
        window = c - T.REACTION - act_in              # the time the foe has to answer once it sees the cast
        if window <= 0:
            return []
        melee = self.melee_foe(foe)
        root_left = max(0.0, foe.root_until - t)
        approach = foe.speed(foe.root_until + EPS if root_left else t) if (melee and foe.intent != "kite") else 0.0
        walk = max(0.0, window - root_left) if melee else 0.0
        closest = max(T.MELEE - 0.5, d.dist - approach * walk)
        silenced = t < foe.silence_until and foe.silence_until - t >= c
        out = []
        ranges = getattr(foe.ai, "ranges", None) or {}
        for name, (reach, lo) in STOPPERS.items():
            if name in CC_ONLY and not cc:
                continue
            s = foe.mod.spells.get(name)
            if s is None or not foe.p.ready(name, t + window):
                continue
            if name in SPELL_STOPPERS and (silenced or foe.school_locked(s.school, t + window)):
                continue
            if s.resource in ("rage", "energy") and foe.p.pool(s.resource) + 10.0 * window < foe.mod.mana_cost(s):
                continue
            if name == "Kidney Shot" and foe.p.combo <= 0:
                continue
            if name == "Counterspell" and not cc and foe.cls == "mage" and foe.hp_frac() >= COUNTER_DAMAGE_AT:
                continue   # a mage counters damage casts only when low (this layer's own rule, worth_counter)
            if name in MELEE_STOPPERS and t < foe.disarm_until and name != "Kidney Shot":
                continue
            r = T.MELEE + 0.5 if name in MELEE_STOPPERS else (ranges.get(name) or reach)
            if lo > 0:
                if root_left >= c or t < foe.root_until and root_left >= window:
                    continue
                if d.dist < lo or closest > r + 0.5:
                    continue
            elif closest > r + 0.5:
                continue
            out.append((name, r + 0.5 + approach * walk))
        if melee and t >= foe.disarm_until - 1.0 and closest <= T.MELEE + 0.5:
            out.append(("Melee", T.MELEE + 0.5 + approach * walk))   # it arrives and hits (pushback, its strikes) before the cast ends
        g = foe.mod.spells.get("Grounding Totem")
        if g is not None and (cc or foe.hp_frac() < GROUNDING_HP) and foe.p.ready("Grounding Totem", t + window) \
                and not foe.ai.grounding(d, foe) and not silenced and not foe.school_locked(g.school, t + window):
            out.append(("Grounding Totem", 99.0))
        pet = foe.p.pet
        if pet is not None and pet.alive and pet.name == "Felhunter" and "Spell Lock" in foe.mod.spells \
                and (pet.engaged or getattr(foe.ai, "pet_arrives", 0.0) <= t + window):
            lock = foe.mod.spells["Spell Lock"]
            if pet.cooldowns.get("Spell Lock", -1.0) <= t + window and pet.mana >= lock.cost and not foe.pet_body.incapacitated(t):
                out.append(("Spell Lock", 99.0))
        return out

    def verdict(self, d, me, foe, c, cc=False):
        """What to do about a cast of `c` seconds now: "ok" (nothing can stop it), "walk" (walking away gets out of every stopper's
        reach inside the bolt's range: walk and use instants), "bait" (a school lockout can be drawn by another school's cast), or
        "accept" (cast anyway). Cached per step."""
        key = (round(c, 2), cc)
        v = self._verdicts.get(key)
        if v is not None:
            return v
        st = self.stoppers(d, me, foe, c, cc)
        t = d.t
        if not st:
            v = ("ok", None)
        else:
            need = max(n for _, n in st)
            held = self.held_for(foe, t) > 0.6
            faster = me.speed(t) > foe.speed(t) * 1.08 or held or (not self.melee_foe(foe) and foe.intent != "close")
            can_walk = t >= me.root_until and me.speed(t) > 0
            if need <= self.bolt_range - 0.5 and need > d.dist and faster and can_walk:
                v = ("walk", st[0][0])
            elif any(n in LOCK_KICKS for n, _ in st):
                v = ("bait", st[0][0])
            else:
                v = ("accept", st[0][0])
        self._verdicts[key] = v
        return v

    def devour_ready(self, foe, t):
        pet = foe.p.pet
        dev = foe.mod.spells.get("Devour Magic")
        return (pet is not None and pet.alive and pet.engaged and pet.name == "Felhunter" and dev is not None
                and pet.cooldowns.get("Devour Magic", -1.0) <= t + 4.0)

    def short_reach(self, d, foe):
        """The reach of the foe's ready short-range controls (Psychic Scream, Howl of Terror, Hammer of Justice ...), 0 when none."""
        t, best = d.t, 0.0
        ranges = getattr(foe.ai, "ranges", None) or {}
        for name, r in SHORT_CONTROLS.items():
            if name in foe.mod.spells and foe.p.ready(name, t + 1.0):
                best = max(best, ranges.get(name) or r)
        return best

    def worth_counter(self, d, me, foe, c):
        if c.kind == "heal" or c.name in HEALS_ALL or c.name in HEAL_CHANNELS:
            return True
        if c.name in CC_CASTS:
            return True
        if c.kind == "ranged":   # Aimed Shot
            return me.hp_frac() < 0.6
        cast = foe.mod.cast_time(c) if c.kind != "channel" else c.channel
        if cast < 1.4 and c.kind != "channel":
            return False
        school = (c.school or "").lower()
        if MAIN_SCHOOL.get(foe.cls) and MAIN_SCHOOL[foe.cls] in school:
            return True
        return me.hp_frac() < COUNTER_DAMAGE_AT

    def cs_ok(self, d, me, foe):
        """Counterspell castable at the foe now and worth it: no Grounding Totem standing in its way, no Voice of Truth on a paladin
        (a visible buff that makes it immune to interrupts and silences: the paladin layer's vot_until)."""
        return me.can("Counterspell", ignore_gcd=True) and not foe.ai.grounding(d, foe) and d.t >= getattr(foe.ai, "vot_until", 0.0)

    def kills(self, me, foe, name):
        s = me.mod.spells.get(name)
        if s is None:
            return False
        avg = (s.dmg_min + s.dmg_max) / 2 + s.coef * me.p.spell_power
        if s.kind == "channel":
            avg = s.dot + s.dot_coef * me.p.spell_power * max(1, s.dot_ticks)
        frozen = me.mod.lance_frozen_mult() if name == "Ice Lance" and me.p.buff("Fingers of Frost", me.t) else 1.0
        ehp = foe.p.hp + (foe.p.absorb if me.t < foe.p.absorb_until else 0.0)
        return ehp <= 0.9 * avg * frozen * me.mod.damage_multiplier(s, False)

    # ------------------------------------------------------------------ per step
    def track(self, d, me, foe):
        t = d.t
        if t <= self._t + EPS:
            return
        self._t = t
        self._verdicts = {}
        if me.controlled(t):
            if self.control_since is None:
                self.control_since = t
        else:
            self.control_since = None
        if self.mshield > 0 and t >= self.mshield_until:
            self.mshield = 0.0

    def pay_evocation(self, me, ticks):
        p = me.p
        if ticks <= 0:
            return
        per = me.mod.mana_regen(p, me.t)
        normal = 1.0 if me.t >= p.fsr_until else min(1.0, p.regen_while_casting)
        p.mana = min(p.mana_max, p.mana + ticks * (EVO_MULT - normal) * per)

    def tick(self, d, me, foe):
        """After every step: Evocation's mana for the ticks the engine's channel paid (its last tick ends the channel in that step)."""
        if self.evo_left > 0:
            ch = me.fight.channel
            if ch is not None and ch[0].name == "Evocation":
                if ch[1] > self.evo_next + EPS:   # ticks paid (a pushback drops ticks without moving the next one)
                    self.pay_evocation(me, int(round((ch[1] - self.evo_next) / EVO_EVERY)))
                    self.evo_next = ch[1]
                self.evo_left = ch[2]
            else:
                if self.evo_left == 1 and d.t + EPS >= self.evo_next:
                    self.pay_evocation(me, 1)
                self.evo_left = -1
        return None

    # ------------------------------------------------------------------ movement
    def intent(self, d, me, foe):
        self.track(d, me, foe)
        t = d.t
        self.step_target = None
        if foe.stealthed and not me.stealthed:
            return "hold"
        if t < foe.inactive_until or foe.immune(t):
            return "kite" if (self.melee_foe(foe) and d.dist < self.keep_range - 2.0) else "hold"
        if self.melee_foe(foe):
            return "kite" if self.kite_melee(d, me, foe) else "hold"
        return self.ranged_intent(d, me, foe)

    def kite_melee(self, d, me, foe):
        """Walk away from a melee foe: while my Polymorph holds it and the mage is not yet at range; while it is held long enough to leave
        time for a cast that lands inside the hold (a Shatter on a root), up to the bolt's range; while it is free and walking away gets
        the mage's next nuke out of its reach."""
        t, dist = d.t, d.dist
        far = self.bolt_range - 1.0
        if dist >= far or t < me.root_until or me.speed(t) <= 0:
            return False
        c = self.nuke_time(me)
        if self.my_sheep(foe, t):
            return dist < far - 1.5
        hold = self.held_for(foe, t)
        if hold > 0.3:
            return hold > c + KITE_MARGIN or dist < 12.0
        return self.verdict(d, me, foe, c)[0] == "walk"

    def ranged_intent(self, d, me, foe):
        t, dist = d.t, d.dist
        danger = self.short_reach(d, foe) if not foe.controlled(t) else 0.0
        if danger and dist < danger + 3.0 and t >= me.root_until:
            return "kite"
        if self.verdict(d, me, foe, self.nuke_time(me))[0] == "walk":
            return "kite"   # out of the reach of something that would stop the next cast
        self.step_target = self.blast_step(d, me, foe)
        if self.step_target:
            return "close"
        if dist > self.keep_range + 0.5:
            return "close"
        return "hold"

    def blast_step(self, d, me, foe):
        """Fire Blast's 20 yards against a ranged foe that already reaches the mage where it stands (a Shadow priest holding at 22 yards
        had kept the mage wanding outside it): the distance to step in to, or None. Not into a ready short-range control (short_reach),
        nor while fire is locked or the foe is immune (2026-11-14, from the duel logs)."""
        t, dist = d.t, d.dist
        fb = me.mod.spells.get("Fire Blast")
        if fb is None or foe.immune(t) or me.school_locked("fire", t) or not me.p.ready("Fire Blast", t + 0.5):
            return None
        reach = self.ranges.get("Fire Blast", fb.range or 20.0)
        if dist <= reach - 0.2:
            return None
        foe_reach = max([getattr(foe.ai, "keep_range", 0.0) + 2.0] + [r for r in (getattr(foe.ai, "ranges", None) or {}).values()
                                                                     if isinstance(r, (int, float)) and r >= 15.0] or [0.0])
        if foe_reach < dist:
            return None   # the foe cannot reach the mage here: no step into its reach for one Fire Blast
        target = reach - 0.5
        danger = self.short_reach(d, foe) if not foe.controlled(t) else 0.0
        if danger and target < danger + 3.0:
            return None
        return target

    def close_to(self, d, me):
        return getattr(self, "step_target", None) or self.keep_range

    # ------------------------------------------------------------------ hooks
    def while_inactive(self, d, me, foe):
        """Inside Ice Block: leave it to Counterspell a heal or a control cast, or against a melee foe once Frost Nova and Blink are both
        back (4 s in); else it runs its 10 s (cooldowns come back, mana regenerates, the foe's own cooldowns run out)."""
        self.track(d, me, foe)
        t = d.t
        if t >= me.inactive_until or t - self.block_start < 1.0:
            return None
        leave = False
        c = self.foe_cast(d, foe)
        if c is not None and (c.kind == "heal" or c.name in HEALS_ALL or c.name in CC_CASTS) and me.p.ready("Counterspell", t) \
                and not me.school_locked("arcane", t) and foe.fight.casting and foe.cast_end() - t > 0.3 and not foe.ai.grounding(d, foe):
            leave = True
        elif self.melee_foe(foe) and me.p.ready("Frost Nova", t) and me.p.ready("Blink", t) and t - self.block_start >= 4.0 \
                and not foe.controlled(t):
            leave = True
        if leave:
            me.immune_until = me.inactive_until = t
            me.fight.note("Ice Block cancelled")
        return None

    def while_controlled(self, d, me, foe):
        """Stunned with a melee foe beside you (or a long stun): Blink out (it frees stuns and roots). Otherwise the base trinket rule
        (fear, Polymorph)."""
        self.track(d, me, foe)
        t = d.t
        stunned = t < me.stun_until and t >= me.incap_until and t >= me.fear_until
        blink = me.mod.spells.get("Blink")
        if stunned and blink is not None and self.control_since is not None and t - self.control_since >= T.REACTION \
                and me.stun_until - t >= 1.2 and me.p.ready("Blink", t) and not me.school_locked(blink.school, t) and not me.silenced(t) \
                and me.p.mana >= me.mod.mana_cost(blink) and ((self.melee_foe(foe) and d.dist <= 10.0) or me.stun_until - t >= 2.5):
            me.stun_until = t   # Blink is cast while stunned
            me.cast(blink)
            return None
        return super().while_controlled(d, me, foe)

    def while_casting(self, d, me, foe):
        """A heal or a control cast seen while casting: cut the own cast short to Counterspell it, unless the own lands first."""
        self.track(d, me, foe)
        t = d.t
        own = me.cast_spell()
        if own is None or own.name == "Evocation":
            return None
        c = self.foe_cast(d, foe)
        if c is None or not self.worth_counter(d, me, foe, c):
            return None
        urgent = c.kind == "heal" or c.name in HEALS_ALL or c.name in CC_CASTS or c.name in HEAL_CHANNELS
        if not urgent and me.fight.casting and me.fight.casting[1] - t < 1.0:
            return None   # a damage cast: only cut a cast that is far from done (pushed back)
        cs = me.mod.spells.get("Counterspell")
        if cs is None or not me.p.ready("Counterspell", t) or me.school_locked(cs.school, t) or me.silenced(t) or foe.ai.grounding(d, foe) \
                or t < getattr(foe.ai, "vot_until", 0.0):
            return None
        if d.dist > self.ranges.get("Counterspell", 30.0) or foe.immune(t) or me.p.mana < me.mod.mana_cost(cs):
            return None
        mine_left = (me.fight.casting[1] - t) if me.fight.casting else 99.0
        theirs_left = (foe.cast_end() - t) if foe.fight.casting else 1.0
        if mine_left + 0.1 < theirs_left:
            return None   # mine lands first; Counterspell right after
        me.break_cast("Counterspell")
        self.gcd_before = me.p.gcd_until
        me.cast(cs)
        self.restore_gcd(me)
        return None

    def off_gcd(self, d, me, foe):
        """Counterspell; the trinket on a slow."""
        self.track(d, me, foe)
        t = d.t
        self.gcd_before = me.p.gcd_until
        c = self.foe_cast(d, foe)
        if c is not None and self.worth_counter(d, me, foe, c) and self.cs_ok(d, me, foe) \
                and (not foe.fight.casting or foe.cast_end() - t > 0.1):
            self.cast_free(me, "Counterspell")
            return None
        return self.slow_trinket(d, me, foe)

    def slow_trinket(self, d, me, foe):
        t = d.t
        frees = me.trinket_frees(t)
        if "slow" not in frees or me.slow < 0.5 or me.slow_until - t < 4.0 or me.hp_frac() > SLOW_TRINKET_HP:
            return None
        if not self.melee_foe(foe) or d.dist > 12.0:
            return None
        if me.p.ready("Blink", t) and not me.school_locked("arcane", t) and d.dist <= T.MELEE + 1.0:
            return None   # Blink first
        held = self.held_for(foe, t) > 1.5
        nova = me.p.ready("Frost Nova", t) and not me.school_locked("frost", t) and d.dist <= self.ranges["Frost Nova"]
        return "trinket" if held or nova else None

    # ------------------------------------------------------------------ decisions
    def decide(self, d, me, foe):
        self.track(d, me, foe)
        self.gcd_before = me.p.gcd_until
        if foe.stealthed:
            return self.prep(d, me, foe)
        for step in (self.emergency, self.peel, self.stop_heal, self.pet_control, self.setup, self.held_window, self.damage):
            a = step(d, me, foe)
            if a is not None:
                return self.before_cast(d, me, foe, a)
        return None

    def prep(self, d, me, foe):
        """A foe in stealth: shields up."""
        a = self.barrier(d, me, foe)
        if a:
            return a
        if self.physical_foe(foe) and self.mshield <= 0 and me.mana_frac() > SHIELD_MANA and me.can("Mana Shield"):
            return "Mana Shield"
        return None

    def emergency(self, d, me, foe):
        """Ice Block below BLOCK_AT while the foe has as much health or more (BLOCK_ALWAYS always); Cold Snap for a second one."""
        t = d.t
        hp = me.hp_frac()
        if me.immune(t) or hp >= BLOCK_AT or t < foe.inactive_until:
            return None
        if foe.hp_frac() < 0.08 and hp > BLOCK_ALWAYS * 0.6:
            return None   # finish it
        if hp >= BLOCK_ALWAYS and foe.hp_frac() + 0.05 < hp:
            return None
        if not self.block_helps(d, me, foe, BLOCK_FOE_FIRST):
            return None
        if me.can("Ice Block"):
            return "Ice Block"
        if "Ice Block" in me.mod.spells and not me.p.ready("Ice Block", t) and self.block_helps(d, me, foe, BLOCK_FOE_SECOND) \
                and me.can("Cold Snap", ignore_gcd=True) and not me.school_locked("frost", t):
            self.cast_free(me, "Cold Snap")
            if me.can("Ice Block"):
                return "Ice Block"
        return None

    def block_helps(self, d, me, foe, foe_below):
        """Whether 10 s of Ice Block can change the duel, not only delay it: the foe is low enough to race (below foe_below), the dots
        it clears would take a third of the health left, or a melee foe meets Frost Nova and Blink back after it."""
        t = d.t
        if foe.hp_frac() < foe_below:
            return True
        if me.hp_frac() >= 0.12 and sum(x[1] * x[2] for x in me.dots) >= 0.33 * me.p.hp:
            return True
        if self.melee_foe(foe):
            nova = me.p.cooldowns.get("Frost Nova", 0.0) - t
            blink = me.p.cooldowns.get("Blink", 0.0) - t
            return 2.0 < nova < ICE_BLOCK_SECS + 1.0 and blink < ICE_BLOCK_SECS + 1.0
        return False

    def peel(self, d, me, foe):
        """A free foe in or near reach: Frost Nova, Blink, Cone of Cold, Cold Snap for a second Frost Nova, Polymorph."""
        t, dist = d.t, d.dist
        if foe.immune(t) or foe.controlled(t) or foe.root_until - t > 0.6:
            return None
        melee = self.melee_foe(foe)
        freedom = t < getattr(foe.ai, "freedom_until", 0.0)
        root_ok = not freedom and dr_factor(foe, "root", t) >= 0.5
        if melee and t < me.root_until and dist <= T.MELEE + 1.0 and me.can("Blink"):
            return "Blink"   # rooted beside it: a Frost Nova would leave both standing in reach
        if dist <= self.ranges["Frost Nova"] - 0.3 and root_ok and me.can("Frost Nova"):
            if melee or dist <= max(self.short_reach(d, foe), T.MIN_RANGED) + 1.0:
                return "Frost Nova"
        if not melee:
            return None
        in_reach = dist <= T.MELEE + 1.0
        if in_reach and me.can("Blink") and (not root_ok or not me.p.ready("Frost Nova", t) or me.school_locked("frost", t)
                                             or t < me.root_until):
            return "Blink"
        slowed = t < foe.slow_until and foe.slow >= 0.45 and foe.slow_until - t > 2.0
        if dist <= self.ranges["Cone of Cold"] - 0.3 and not slowed and not freedom and not self.pet_sheeped(foe, t) \
                and me.can("Cone of Cold"):
            return "Cone of Cold"
        if dist <= T.MELEE + 3.0 + foe.speed(t) * 0.5:
            nova_cd = me.p.cooldowns.get("Frost Nova", 0.0) - t
            if me.hp_frac() < COLD_SNAP_NOVA_HP and nova_cd > 8.0 and not me.p.ready("Blink", t) and root_ok \
                    and "Cold Snap" in me.mod.spells and me.can("Cold Snap", ignore_gcd=True) and not me.school_locked("frost", t):
                self.cast_free(me, "Cold Snap")
                if me.can("Frost Nova"):
                    return "Frost Nova"
            return self.sheep(d, me, foe, need=True)
        return None

    def sheep(self, d, me, foe, need=False, heal=False):
        """Polymorph the foe: instant with Presence of Mind when the cast would be stopped, else only when nothing can stop it."""
        t = d.t
        if not me.can("Polymorph") or foe.immune(t) or dr_factor(foe, "incap", t) < 0.5:
            return None
        if getattr(foe.ai, "cc_immune", None) is not None and foe.ai.cc_immune(d, foe, "incap", "Polymorph"):
            return None
        if foe.cls == "warlock" and self.devour_ready(foe, t):
            return None   # the Felhunter eats it at once
        if not heal:   # it regenerates POLY_REGEN a second in the sheep
            desperate = need and me.hp_frac() < SHEEP_DESPERATE
            if foe.hp_frac() < (SHEEP_NEED_FOE_HP if need else 0.7) and not desperate:
                return None
            if dr_factor(foe, "incap", t) < 1.0 and not desperate:
                return None
        c = self.cast_time(me, "Polymorph")
        if c > 0 and self.verdict(d, me, foe, c, cc=True)[0] != "ok":
            if not me.can("Presence of Mind", ignore_gcd=True) or "polymorph" in T.TRINKET_BREAKS.get(foe.cls, ()) \
                    and t >= foe.trinket_ready:
                return None   # (no instant sheep the foe's ready trinket would break at once)
            self.pom_for = "Polymorph"
            self.cast_free(me, "Presence of Mind")
        self.sheep_target = "player"
        return "Polymorph"

    def stop_heal(self, d, me, foe):
        """A heal the foe will finish with Counterspell down: Polymorph lands first (Presence of Mind makes it instant)."""
        t = d.t
        c = self.foe_cast(d, foe)
        if c is None or not (c.kind == "heal" or c.name in HEALS_ALL) or not foe.fight.casting:
            return None
        if self.cs_ok(d, me, foe) or foe.ai.grounding(d, foe):
            return None
        left = foe.cast_end() - t
        if self.cast_time(me, "Polymorph") + 0.1 > left and not me.can("Presence of Mind", ignore_gcd=True):
            return None
        return self.sheep(d, me, foe, heal=True)

    def pet_control(self, d, me, foe):
        """A hunter's pet on me: Polymorph it (none of my damage reaches it while it lasts)."""
        t = d.t
        pb = foe.pet_body
        if not self.beast_pet(foe) or not foe.p.pet.engaged or pb.incapacitated(t) or self.pet_sheeped(foe, t):
            return None
        if me.hp_frac() < 0.2 or (self.melee_foe(foe) and d.dist < 15.0):
            return None
        self.ranges["Polymorph"] = 99.0   # it stands beside me
        try:
            ok = me.can("Polymorph")
        finally:
            self.ranges["Polymorph"] = self.poly_range
        if not ok:
            return None
        st = self.stoppers(d, me, foe, self.cast_time(me, "Polymorph"), cc=True)
        if any(n != "Scatter Shot" for n, _ in st):
            return None
        self.sheep_target = "pet"
        return "Polymorph"

    def setup(self, d, me, foe):
        """Remove Lesser Curse, Ice Barrier, Mana Shield, Evocation."""
        t = d.t
        a = self.decurse(d, me, foe)
        if a:
            return a
        a = self.barrier(d, me, foe)
        if a:
            return a
        if self.physical_foe(foe) and self.mshield <= 0 and me.mana_frac() > SHIELD_MANA and me.hp_frac() < SHIELD_BELOW \
                and (me.p.absorb <= 0 or t >= me.p.absorb_until) \
                and ((self.melee_foe(foe) and d.dist <= 12.0) or foe.cls == "hunter" or self.pet_on_me(foe)) and me.can("Mana Shield"):
            return "Mana Shield"
        if me.mana_frac() < EVO_MANA and me.can("Evocation") and not me.dots \
                and (not self.melee_foe(foe) or d.dist >= self.bolt_range - 4.0):
            if (self.my_sheep(foe, t) and foe.incap_until - t >= 5.0) or (t < foe.inactive_until and foe.inactive_until - t >= 5.0):
                return "Evocation"
        return None

    def decurse(self, d, me, foe):
        t = d.t
        if not me.can("Remove Lesser Curse"):
            return None
        tongues = me.debuffs.get("Curse of Tongues")
        if tongues and tongues.get("until", 0) - t > 4.0:
            curse = foe.mod.spells.get("Curse of Tongues")
            blocked = foe.silenced(t + 2.5) or foe.controlled(t + 2.5) or t + 2.5 < foe.inactive_until \
                or (curse is not None and foe.school_locked(curse.school, t + 2.5))
            if blocked or t - self.decursed_at >= DECURSE_EVERY:
                self.decursed_at, self.decurse_target = t, "Curse of Tongues"
                return "Remove Lesser Curse"
        ex = me.debuffs.get("Curse of Exhaustion")
        if ex and ex.get("until", 0) - t > 4.0 and self.melee_foe(foe) and t - self.decursed_at >= DECURSE_EVERY / 2:
            self.decursed_at, self.decurse_target = t, "Curse of Exhaustion"
            return "Remove Lesser Curse"
        if sum(x[1] * x[2] for x in me.dots if x[0] in BANES) >= 450.0 and me.mana_frac() > 0.25 and t - self.decursed_at >= DECURSE_EVERY:
            self.decursed_at, self.decurse_target = t, "bane"
            return "Remove Lesser Curse"
        return None

    def barrier(self, d, me, foe):
        t = d.t
        if me.p.absorb > 0 and t < me.p.absorb_until:
            return None
        if not me.can("Ice Barrier") or me.mana_frac() < 0.12:
            return None
        if foe.cls == "warlock" and self.devour_ready(foe, t):
            return None   # the Felhunter would eat it and heal itself
        return "Ice Barrier"

    def held_window(self, d, me, foe):
        """The foe held by my own breakable control (Polymorph), my own root while I walk, or immune: no damage until the opener is
        timed to land as it ends (a sheep below OPEN_SHEEP_BELOW health is opened on at once from range: it regenerates)."""
        t = d.t
        nuke = self.casting_spell(me, self.main) if self.main else None
        if foe.immune(t):
            left = foe.immune_until - t
            if nuke is not None and me.can(nuke.name) and abs(left - self.cast_len(me, nuke)) <= 0.15:
                return nuke.name
            return "wait"
        if self.my_sheep(foe, t):
            left = foe.incap_until - t
            far = d.dist >= self.bolt_range - 4.0
            if foe.hp_frac() < OPEN_SHEEP_BELOW and far:
                return None
            if not far and left > 1.5:
                return "wait"   # walk to range first (intent)
            if nuke is not None and me.can(nuke.name) and self.cast_len(me, nuke) >= left - 0.15:
                return nuke.name
            return "wait" if left > 0.3 else None
        if self.my_root(foe, t) and self.melee_foe(foe) and self.kite_melee(d, me, foe):
            return "wait"   # walking off the root: no damage breaks it yet
        return None

    def damage(self, d, me, foe):
        """The spec's rotation with this duel's rules: the foe's real approach; casts the foe can stop vetoed while walking gets the mage
        out of its reach (instants instead); Ice Lance never breaks my own root early; a Frostbolt to slow a free melee foe; the area
        spells kept off a sheeped pet; this layer's spells kept off the rotation."""
        t = d.t
        melee = self.melee_foe(foe)
        off = set(LAYER_SPELLS)
        if self.my_root(foe, t) and foe.root_until - t > 0.6 and not me.p.buff("Fingers of Frost", t) and not self.kills(me, foe, "Ice Lance"):
            off.add("Ice Lance")
        if self.pet_sheeped(foe, t):
            off |= set(AREA)
        if t < foe.root_until:
            off.add("Frost Nova")
        walk = melee and self.kite_melee(d, me, foe)
        pet = foe.p.pet
        pet_in = (getattr(foe.ai, "pet_arrives", 0.0) - t) if (self.beast_pet(foe) and not pet.engaged and "Polymorph" in me.mod.spells) else -1.0
        for name in DAMAGE_CASTS:
            s = me.mod.spells.get(name)
            if s is None:
                continue
            c = self.cast_len(me, s)
            v = self.verdict(d, me, foe, c)[0]
            if walk or v == "walk" or (pet_in > 0 and c > pet_in + 0.3):
                off.add(name)   # (a beast pet arriving before the cast ends would push it back: it is sheeped on arrival)
            elif MELEE_HOLD and v != "ok" and melee and c > MELEE_HOLD_MIN and not self.cornered(d, me, foe):
                off.add(name)   # a melee foe coming in would stop it: instants, and Frost Nova when it arrives
        a = self.slow_bolt(d, me, foe, off)
        if a:
            return a
        self.burst(d, me, foe)
        if not melee and "Fire Blast" not in off and not foe.immune(t) and me.can("Fire Blast"):
            return "Fire Blast"   # against a ranged foe, on cooldown: instant, no pushback, nothing to interrupt (the frost leveling
                                  # rotation keeps it to finish a mob; a Shadow priest's dots had pushed back every Frostbolt, 2026-11-14)
        a = self.vetoed(me, off, lambda: self.view_rotation(d, me, foe))
        if a in ("retreat", "advance"):
            a = None
        s = self.casting_spell(me, a) if a not in (None, "wand") else None
        sure = False
        if s is not None:   # a cast a short-reach stopper will take for sure: an instant first
            v, st = self.verdict(d, me, foe, self.cast_len(me, s))
            sure = v in ("bait", "accept") and (st in MELEE_STOPPERS or st in SHORT_CONTROLS or st in ("Spell Lock", "Melee"))
        if a is None or a == "wand" or sure:
            a2 = self.instant(d, me, foe, off)
            if a2 is not None:
                return a2
        if a == "wand" and (walk or d.dist > 30.0):
            return None
        return a

    def cornered(self, d, me, foe):
        """A melee foe on the mage with Frost Nova, Blink and Cone of Cold all unavailable: casting is all that is left."""
        t = d.t
        if d.dist > T.MELEE + 3.0:
            return False
        return not any(me.can(n) for n in ("Frost Nova", "Blink", "Cone of Cold"))

    def slow_bolt(self, d, me, foe, off):
        """A free melee foe coming in without a slow: a Frostbolt from a build whose rotation would not cast one."""
        t = d.t
        if not self.melee_foe(foe) or "Frostbolt" in off or not (self.fire or self.arcane):
            return None
        if foe.controlled(t) or (t < foe.slow_until and foe.slow >= 0.3) or t < foe.root_until or d.dist <= T.MELEE + 1.0:
            return None
        if self.verdict(d, me, foe, self.cast_time(me, "Frostbolt"))[0] != "ok" or not me.can("Frostbolt"):
            return None
        return "Frostbolt"

    def burst(self, d, me, foe):
        """Arcane Power (off the global cooldown) for a window: the foe held at range, or below half health."""
        t = d.t
        if "Arcane Power" not in me.mod.spells or not me.can("Arcane Power", ignore_gcd=True) or me.mana_frac() < 0.4:
            return
        if (self.held_for(foe, t) > 3.0 and not self.my_sheep(foe, t)) or foe.hp_frac() < 0.5:
            self.cast_free(me, "Arcane Power")

    def instant(self, d, me, foe, off):
        """An instant that does something now: Fire Blast, Ice Lance, Arcane Explosion in reach."""
        t = d.t
        if foe.immune(t) or self.my_sheep(foe, t):
            return None
        if "Fire Blast" not in off and me.can("Fire Blast"):
            return "Fire Blast"
        frozen = me.p.buff("Fingers of Frost", t) or (foe.root_until > t and foe.root_frozen)
        if "Ice Lance" not in off and (frozen or self.kills(me, foe, "Ice Lance")) and me.can("Ice Lance"):
            return "Ice Lance"
        if d.dist <= 10.0 and "Arcane Explosion" not in off and me.mana_frac() > 0.3 and me.can("Arcane Explosion"):
            return "Arcane Explosion"
        return None

    def view_rotation(self, d, me, foe):
        """The rotation with the foe's real approach: a caster that stands at range, or a held foe, does not walk in."""
        body = foe.body
        approach = foe.speed(d.t) if (self.melee_foe(foe) and foe.intent == "close") else 0.0
        body.speed = lambda _t, _v=approach: _v
        try:
            return self.rotation(d, me, foe)
        finally:
            del body.speed

    def vetoed(self, me, off, fn):
        mod = me.mod
        old = mod.veto
        mod.veto = dict(old)
        for n in off:
            mod.veto[n] = {"off": True}
        try:
            return fn()
        finally:
            mod.veto = old

    def before_cast(self, d, me, foe, a):
        """Last checks on the chosen action: "wait" is no action; a charged Grounding Totem is popped with a cheap instant before a
        cast-time spell or Polymorph; a school lockout in the way is baited with a cast of another school; Presence of Mind on a cast that
        kills."""
        t = d.t
        if a in ("wait", None):
            return None
        if a == "wand":
            return a
        name = a.name if hasattr(a, "name") else a
        s = me.mod.spells.get(name)
        if s is None:
            return a
        cs = self.casting_spell(me, s)
        if s.target != "self" and name not in AREA and (cs is not None or name in ("Polymorph", "Counterspell")) \
                and foe.ai.grounding(d, foe):
            for k in ("Ice Lance", "Fire Blast", "Scorch"):
                if k != name and me.can(k):
                    return k
        if cs is not None and name not in ("Polymorph", "Evocation"):
            v, st = self.verdict(d, me, foe, self.cast_len(me, cs))
            if v == "bait" and (cs.school or "").startswith(self.main_school):
                bait = self.bait(d, me, foe, name, st)
                if bait is not None:
                    me.stats["baits"] += 1
                    me.fight.note(f"{bait} to draw {st}")
                    return bait
            if v in ("bait", "accept") and me.can("Presence of Mind", ignore_gcd=True) and self.kills(me, foe, name):
                self.pom_for = name
                self.cast_free(me, "Presence of Mind")
        if name == "Polymorph" and self.sheep_target is None:
            self.sheep_target = "player"
        return a

    def bait(self, d, me, foe, name, stopper):
        """The shortest cast of another school that the stopper would also take (Spell Lock wants 2 s or more by the base cast time),
        no longer than the cast it stands in for; none against a melee foe walking in (it would close while the mage stands)."""
        if self.melee_foe(foe) and foe.intent == "close" and d.dist > T.MELEE + 1.0:
            return None
        own = self.cast_len(me, me.mod.spells[name]) if name in me.mod.spells else 99.0
        best = None
        for k in ("Scorch", "Fireball", "Frostbolt", "Arcane Missiles"):
            b = me.mod.spells.get(k)
            if b is None or k == name or (b.school or "").startswith(self.main_school) or not me.can(k):
                continue
            if stopper == "Spell Lock" and not (b.cast >= 2.0 or b.kind == "channel"):
                continue
            c = self.cast_len(me, b)
            if c <= own + 1.0 and (best is None or c < best[0]):
                best = (c, k)
        return best[1] if best else None
