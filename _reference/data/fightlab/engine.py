"""Fight lab: a stochastic (Monte Carlo) fight simulator for leveling/solo play.

One `Session` plays many fights against same-level mobs in a row, carrying health, mana/energy/rage and cooldowns from
fight to fight, with looting, travel, eating/drinking and deaths between them. A fight advances in 0.1-second steps:
the mob walks in, swings, gets rooted, slowed, stunned or feared; the player casts, swings, shoots, gets pushed back,
and follows a class-specific priority list (`ClassModule.decide`). Every hit/miss/crit/proc is rolled, so the outputs
are distributions (time to kill, resource per kill, downtime, deaths), not expected values.

Class modules (mage.py, priest.py, ...) subclass `BaseModule` and provide: stats, the spellbook by level, talent
mechanics via hooks, and the decision function. The engine knows nothing about specific spells: a `Spell` is data
plus hooks the module fills in. Spell kinds: "spell" (cast/instant, direct and/or periodic damage), "channel",
"heal", "melee" / "ranged" (weapon attacks: white swings and yellow abilities), "buff" (no target effect).
Pets (`Pet`) fight the mob on their own swing timer and hold its attention until the player out-threatens them.
"""
import copy
import math
import random
import re
import statistics
from dataclasses import dataclass, field

import tables
from tables import (DEATH_TIME, DRINK_BELOW, EAT_BELOW, GCD, LOOT_TIME, MELEE_RANGE, MOB_CRIT_CHANCE, MOB_DMG_SPREAD,
                    MOB_HIT_CHANCE, MOB_HP_SPREAD, MOB_SPEED, MOB_SWING, PARTIAL_RESIST_LOSS, PUSHBACK_FIRST,
                    PUSHBACK_NEXT, ROOT_BREAK_CHANCE, SIT_DOWN, TRAVEL_TIME, WAND_SPEED, armor_mitigation, drink_rate,
                    food_rate, health_regen_tick, mana_regen_tick, mob_armor, mob_health, mob_melee_damage, ranged_miss,
                    spell_miss, CHANNEL_PUSHBACK, SPELL_HIT_CAP)

DT = 0.1
EPS = 1e-9   # timers compared with this slack: t accumulates DT in floating point (2.4999999 < 2.5 cost a step; audit of 2026-10-18 row 70)


INTERRUPT_RX = [re.compile(p) for p in (r"prevents? any spell in that school from being cast for (\d+) sec", r"preventing them from casting spells for (\d+) sec",
                                          r"interrupting any spell they are casting for (\d+) sec", r"interrupting their spellcasts for (\d+) sec",
                                          r"preventing any spell from that school of magic from being cast for (\d+) sec", r"[Ss]ilences the (?:target|enemy) for (\d+) sec")]


def parse_interrupt(text):
    """Seconds a casting mob is locked out when the ability lands (Counterspell 10, Kick 5, Earth Shock 2, Silence 5, Feral Charge 4); 0 if none."""
    best = 0.0
    for rx in INTERRUPT_RX:
        m = rx.search(text or "")
        if m:
            best = max(best, float(m.group(1)))
    return best


@dataclass
class Weapon:
    dmg_min: float
    dmg_max: float
    speed: float
    kind: str = "1h"             # "1h", "2h", "dagger", "ranged", "paw" (shapeshift)
    dps_bonus: float = 0.0       # ammo dps for ranged weapons


@dataclass
class Spell:
    name: str
    school: str
    rank: int = 1
    level: int = 1
    cost: float = 0.0            # mana, energy or rage (see `resource`)
    cast: float = 0.0            # seconds (0 = instant)
    cooldown: float = 0.0
    range: float = 30.0
    dmg_min: float = 0.0
    dmg_max: float = 0.0
    coef: float = 0.0            # spell power coefficient (direct)
    chill: float = 0.0           # slow fraction applied to the target on hit (0.4 = 40%)
    chill_dur: float = 0.0
    root: float = 0.0            # freeze duration on hit
    aoe: bool = False
    max_targets: int = 0        # area attacks: mobs hit at most (0 = everything in reach); tables.AOE_SPELLS sets it
    falloff: float = 1.0        # Chain Lightning: damage factor per further target
    aoe_range: float = 0.0      # reach of the area (yards); 0 = the spell's range, or 10 yd
    aoe_center: str = "player"  # "target": the area sits on the target (Blizzard, Rain of Fire, Volley); "player": around the caster
    tags: tuple = ()
    # periodic damage (Shadow Word: Pain, Corruption, Rend, Rip ...) and channels (Mind Flay, Drain Life ...)
    kind: str = "spell"          # "spell" | "channel" | "heal" | "melee" | "ranged" | "buff"
    dot: float = 0.0             # total periodic damage over `dot_dur`
    dot_dur: float = 0.0
    dot_ticks: int = 0
    dot_coef: float = 0.0        # spell power (or attack power) coefficient per tick
    channel: float = 0.0         # channel duration; ticks = dot_ticks
    # heals and shields
    heal_min: float = 0.0
    heal_max: float = 0.0
    heal_coef: float = 0.0
    hot: float = 0.0             # total healing over `hot_dur` (Renew, Rejuvenation)
    hot_dur: float = 0.0
    absorb: float = 0.0
    # weapon attacks
    weapon_pct: float = 0.0      # yellow attack: fraction of weapon damage added (1.0 = 100%); white swings use the Weapon directly
    hand: str = "mh"
    on_next_swing: bool = False  # Heroic Strike / Maul / Cleave: replaces the next main-hand swing, no global cooldown
    resource: str = "mana"       # "mana" | "energy" | "rage" | "focus" | "none" | "health"
    combo: int = 0               # +n combo points generated on hit, -1 = a finisher that consumes all
    # control
    stun: float = 0.0
    fear: float = 0.0
    daze: float = 0.0            # slow fraction of a daze/hamstring (with chill_dur as the duration)
    charge: bool = False         # closes to melee instantly
    target: str = "mob"          # "mob" | "self" | "pet"
    interrupt: float = 0.0       # seconds a caster mob cannot cast after this hits it mid-cast (Counterspell, Kick, Earth Shock, Silence)


@dataclass
class Pet:
    name: str
    hp_max: float
    hp: float
    armor: float
    dmg_min: float
    dmg_max: float
    speed: float = 2.0
    attack_power: float = 0.0
    crit: float = 0.05
    focus: float = 100.0
    focus_max: float = 100.0
    focus_regen: float = 10.0    # per second (client PowerType FOCUS RegenCombat 10; 5 until 2026-10-18; hunter.make_pet sets it, talents scale it)
    mana: float = 0.0
    mana_max: float = 0.0
    mana_regen: float = 0.0      # per second
    threat_mult: float = 1.0     # threat per point of damage (Voidwalker / Growl stances)
    alive: bool = True
    engaged: bool = False
    swing_at: float = 0.0
    cooldowns: dict = field(default_factory=dict)
    hit_bonus: float = 0.0
    dmg_mult: float = 1.0
    caster: bool = False         # imp: stands at range, is not attacked unless it pulls threat
    spell_power: float = 0.0     # spell damage the pet's spells add with their coefficient (2026-10-08: a demon's share of the warlock's)


@dataclass
class Mob:
    level: int
    hp_max: float
    hp: float
    dmg: float
    armor: float
    dist: float
    swing_at: float = 0.0        # time of the next melee swing (valid once in melee)
    in_melee: bool = False
    slow: float = 0.0
    slow_until: float = 0.0
    root_until: float = 0.0
    attack_slow_until: float = 0.0
    attack_slow: float = 0.25    # swing time added while attack_slow_until runs (Frost/Ice Armor 25%; Thunder Clap sets 0.20)
    stun_until: float = 0.0
    fear_until: float = 0.0
    debuffs: dict = field(default_factory=dict)   # name -> {"until", "stacks"}
    dots: list = field(default_factory=list)      # [name, per_tick, ticks_left, next_tick_time, interval, crit_chance, crit_mult]
    target: str = "player"       # "player" | "pet"
    threat_player: float = 0.0
    threat_pet: float = 0.0
    armor_debuff: float = 0.0    # armor removed (Sunder Armor, Expose Armor, Faerie Fire)
    pet_in_melee: bool = False
    caster: bool = False         # stands at range and casts bolts (see tables.MOB_CASTER_SHARE)
    runner: bool = False         # flees at low health (tables.RUNNER_SHARE)
    fled: bool = False
    flee_until: float = -1.0
    cast_dmg: float = 0.0
    cast_end: float = -1.0       # end of the current bolt cast, < 0 when not casting
    cast_next: float = 0.0
    lockout_until: float = 0.0   # interrupted: no casting until then (it runs in and melees)
    dmg_reduction: float = 0.0   # flat damage taken off every swing (Demoralizing Roar / Shout: attack power / 14 x swing time)
    dmg_reduction_until: float = 0.0

    def casting(self, t):
        return self.cast_end >= 0.0 and t < self.cast_end + 1e-9

    def can_cast(self, t):
        return self.caster and t >= self.lockout_until and not self.incapacitated(t)

    def stunned(self, t):
        return t < self.stun_until

    def rooted(self, t):
        return t < self.root_until

    def feared(self, t):
        return t < self.fear_until

    def frozen(self, t):
        return self.rooted(t)

    def fleeing(self, t):
        return t < self.flee_until

    def incapacitated(self, t):
        return self.stunned(t) or self.feared(t) or self.fleeing(t)

    def speed(self, t):
        s = self.slow if t < self.slow_until else 0.0
        return MOB_SPEED * (1.0 - s)

    def effective_armor(self):
        return max(0.0, self.armor - self.armor_debuff)


@dataclass
class Player:
    level: int
    hp_max: float
    hp: float
    mana_max: float
    mana: float
    base_mana: float
    spirit: float
    intellect: float
    spell_power: float
    armor: float
    spell_crit: float           # base spell crit chance (before talents)
    dodge: float
    ranged_crit: float
    gcd_until: float = 0.0
    fsr_until: float = 0.0      # five-second rule: no spirit regen until this time
    cooldowns: dict = field(default_factory=dict)   # spell name -> ready time
    buffs: dict = field(default_factory=dict)       # name -> dict(until=..., stacks=..., charges=...)
    absorb: float = 0.0
    absorb_until: float = 0.0
    regen_while_casting: float = 0.0   # fraction of spirit regen that continues inside the five-second rule
    last_cast_end: float = -99.0
    # melee / ranged / resources (unused by pure casters)
    strength: float = 0.0
    agility: float = 0.0
    stamina: float = 0.0
    attack_power: float = 0.0
    ranged_ap: float = 0.0
    melee_crit: float = 0.0
    hit_bonus: float = 0.0      # physical hit from gear/talents (fraction)
    mh: object = None           # Weapon
    oh: object = None
    ranged: object = None
    swing_mh: float = 0.0
    swing_oh: float = 0.0
    shot_at: float = 0.0
    energy: float = 0.0
    energy_max: float = 0.0
    rage: float = 0.0
    rage_max: float = 0.0
    combo: int = 0
    pet: object = None          # Pet
    form: str = ""              # shapeshift / stance / aura name
    parry: float = 0.0
    block: float = 0.0
    block_value: float = 0.0
    hots: list = field(default_factory=list)       # [name, per_tick, ticks_left, next, interval]

    def ready(self, name, t):
        return self.cooldowns.get(name, -1.0) <= t

    def buff(self, name, t):
        b = self.buffs.get(name)
        if b and b.get("until", 1e18) > t:
            return b
        return None

    @property
    def dual_wield(self):
        return self.oh is not None

    def pool(self, resource):
        return {"mana": self.mana, "energy": self.energy, "rage": self.rage, "health": self.hp, "none": 1e9,
                "focus": self.pet.focus if self.pet else 0.0}.get(resource, 0.0)


class BaseModule:
    """Default hooks: a class module overrides what its mechanics need. Numbers default to 'no effect'."""
    melee = False          # the player auto-attacks in melee
    ranged = False         # the player auto-shoots from range (hunter)
    resource = "mana"      # main resource shown as "<resource>/kill" in reports
    special_stat = None    # (label, key) of an extra per-level report column, e.g. ("Frozen casts", "frozen_cast_share")
    armor_spell_used = "none"
    veto = {}              # tuned rotation rules (fightlab/rotation_opt.py, rotations/<class>-<spec>.json): {spell: {"off": True,
                           # "min_mana": f, "min_hp": f, "max_hp": f}}: the spell counts as unaffordable outside them, so the priority
                           # list falls through to its next choice
    eat_below = None       # per-class override of tables.EAT_BELOW (a warlock Drain Lifes instead of eating)
    drink_below = None     # per-class override of tables.DRINK_BELOW (Life Tap instead of drinking)

    def not_simulated(self):
        return []

    # numbers
    def cast_time(self, spell):
        return spell.cast

    def mana_cost(self, spell):
        return spell.cost

    def final_cost(self, fight, spell, cost):
        return cost

    def hit_bonus(self, spell):
        return 0.0

    def crit_bonus(self, spell, frozen):
        return 0.0

    def crit_damage_bonus(self, spell):
        return 0.0

    def damage_multiplier(self, spell, frozen):
        return 1.0

    def periodic_multiplier(self, spell):
        return self.damage_multiplier(spell, False)

    def heal_multiplier(self, spell):
        return 1.0

    def resist_factor(self):
        return 1.0

    def chill_duration_bonus(self):
        return 0.0

    def chill_extra_slow(self):
        return 0.0

    def armor_bonus(self):
        return 0.0

    def wand_damage(self):
        return 0.0

    def retreat_time(self):
        return 2.0

    def pushback_resisted(self, fight, spell):
        return False

    def attacks_from_front(self):
        return True

    def mana_regen(self, p, t):
        return mana_regen_tick(p.spirit)

    def health_regen(self, p):
        return health_regen_tick(p.spirit)

    def periodic_can_crit(self, spell):
        return False

    def scale_rank(self, spell):
        """The rank at the character's level (tables.rank_level_factor, audit of 2026-10-18 row 8): a copy with the tooltip's level-60
        damage, healing and absorb scaled to what the rank gives at self.level; the spell itself when nothing scales (physical
        abilities, top ranks at their cap, RANK_LEVEL_SCALING off). A kind the rank lacks borrows the other's factor for a field the
        module filled anyway (a channel's damage read into dmg_min, a periodic rank's number into dot)."""
        if spell is None:
            return None
        f = tables.rank_level_factor(type(self).__module__.rsplit(".", 1)[-1], spell.name, spell.level, self.level)
        if not f:
            return spell
        fd = f.get("direct", f.get("periodic", 1.0))
        fp = f.get("periodic", f.get("direct", 1.0))
        fa = f.get("absorb", 1.0)
        s = copy.copy(spell)
        s.dmg_min, s.dmg_max, s.heal_min, s.heal_max = s.dmg_min * fd, s.dmg_max * fd, s.heal_min * fd, s.heal_max * fd
        s.dot, s.hot, s.absorb = s.dot * fp, s.hot * fp, s.absorb * fa
        if getattr(s, "burn", 0.0):
            s.burn = s.burn * fp
        return s

    def gcd_of(self, spell):
        """The global cooldown a spell triggers: the client's per-spell value (tables.spell_gcd: rogue, cat and totem abilities 1.0 s)."""
        return tables.spell_gcd(type(self).__module__.rsplit(".", 1)[-1], spell.name)

    def pet_decide(self, fight):
        return None

    def pet_threat_bonus(self, fight):
        return 0.0

    def split_damage_taken(self, fight, dmg):
        """Soul Link and the like: return the damage the player takes; the rest went elsewhere."""
        return dmg

    def resummon_time(self):
        return tables.PET_RESUMMON_TIME

    def swing_speed_factor(self):
        return 1.0

    def pull_range(self):
        return 30.0

    def rage_from_hit(self, fight, amount, weapon, hand, crit):
        return tables.rage_from_hit(amount, weapon.speed, hand, crit, fight.p.level, two_hand=getattr(weapon, "kind", "") == "2h")

    # events
    def on_fight_start(self, fight):
        pass

    def on_chill(self, fight, spell):
        pass

    def consume_frozen_charge(self, fight):
        return False

    def on_hit(self, fight, spell, amount, crit, frozen):
        pass

    def on_miss(self, fight, spell):
        pass

    def on_tick(self, fight, spell, amount, crit):
        pass

    def after_cast(self, fight, spell):
        if spell.cooldown > 0:
            fight.p.cooldowns[spell.name] = fight.t + spell.cooldown

    def on_hit_taken(self, fight, dmg, crit=False):
        pass

    def on_swing(self, fight, spell, outcome, amount, hand):
        pass

    def on_kill(self, fight):
        pass

    def on_pet_death(self, fight):
        pass

    def on_pet_hit(self, fight, amount, crit):
        pass

    def on_regen_tick(self, fight, p, t):
        """Every 2 s in combat, for every class (energy/rage classes get no mana tick): Adrenaline Rush, Anger Management ..."""
        pass

    def interrupt_bonus(self, fight, spell):
        """Extra lockout seconds when `spell` interrupts a cast (Improved Counterspell's silence, Improved Kick's silence chance)."""
        return 0.0

    def dodge_bonus(self, fight):
        """Temporary dodge from buffs (Evasion, Deterrence ...): read from buffs, never written into the player's stats."""
        return 0.0

    def parry_bonus(self, fight):
        """Temporary parry from buffs (Deterrence): read from buffs, never written into the player's stats."""
        return 0.0

    def dodge_parry_reduction(self):
        """Less chance for the mob to dodge or parry your melee attacks (Weapon Expertise)."""
        return 0.0

    def on_dodge(self, fight):
        pass

    def on_parry(self, fight):
        """The player parried the mob's swing (Counterattack)."""
        pass

    def block_bonus(self, fight):
        """Temporary block chance from buffs (Shield Block); only read when the player has a shield (`Player.block` > 0)."""
        return 0.0

    def on_block(self, fight):
        """The player blocked the mob's swing with a shield (Revenge, Shield Specialization's rage)."""
        pass

    def evocation(self, p, t):
        return 0.0

    def after_death(self, p, t):
        pass

    def death_time(self, p, t):
        """Seconds a death costs (corpse run); a shaman with Reincarnation ready pays less."""
        return DEATH_TIME

    def after_fight(self, p, t):
        """Out-of-combat actions right after a kill (self-heals, pet heals, re-buffs): return seconds spent."""
        return 0.0

    def decide(self, fight):
        return None

    # ---------------------------------------------------------------- pulls of several mobs
    AOE = None   # {"direct": [...area attacks...], "channel": [...], "dots": [...spread on every mob...], "min_near": 2}

    def extra_targets(self, fight, spell, white):
        """How many further mobs a non-area attack also hits (Blade Flurry, Sweeping Strikes)."""
        return 0

    def decide_aoe(self, fight):
        """A pull of several mobs (tables.MOBS_PER_PULL > 1): area attacks when enough mobs stand in their reach, then a dot on
        every mob that lacks one (the target switches to it), else None so the single-target priority runs on the current target."""
        A = self.AOE
        if not A:
            return None
        p, t = fight.p, fight.t
        alive = fight.alive()
        if len(alive) < 2:
            return None
        sp = self.spells
        target = fight.m

        def can(s):
            return s is not None and p.ready(s.name, t) and fight.can_afford(s, self.mana_cost(s))

        def in_reach(s):
            r = s.aoe_range or (s.range if s.range and s.range > MELEE_RANGE else MELEE_RANGE)
            if r <= MELEE_RANGE + 0.5:
                return [x for x in alive if x.in_melee]
            if s.aoe_center == "target":
                return [x for x in alive if abs(x.dist - target.dist) <= r + 0.5]
            return [x for x in alive if x.dist <= r + 0.5]

        need = A.get("min_near", 2)
        for name in A.get("channel", []):
            s = sp.get(name)
            if can(s) and len(in_reach(s)) >= need + 1 and p.pool(s.resource) >= self.mana_cost(s) * 1.5:
                return s
        for name in A.get("direct", []):
            s = sp.get(name)
            if can(s) and len(in_reach(s)) >= need:
                return s
        for name in A.get("dots", []):
            s = sp.get(name)
            if not can(s):
                continue
            for om in sorted(alive, key=lambda x: -x.hp):
                fight.switch(om)
                if not fight.dot_active(name):
                    return s
            fight.switch(target)
        return None


# Spells that cannot miss or be resisted (Blizzard, 16 Oct beta notes: "Changed Vampiric Embrace so that it can't be resisted").
NO_MISS = {"Vampiric Embrace"}


class Fight:
    """One fight. `mod` is the class module (hooks); `rng` rolls combat; the mob is already built."""

    def __init__(self, mod, player, mob, rng, t0=0.0, log=None, extra=None):
        self.mod, self.p, self.m, self.rng, self.t = mod, player, mob, rng, t0
        self.mobs = [mob] + list(extra or [])   # the first mob is the target; extra mobs of a pull tick after it and stay on the player
        for name, cfg in tables.AOE_SPELLS.items():   # area spells: reach and target caps (flags only matter with several mobs)
            s = getattr(mod, "spells", {}).get(name)
            if s is not None:
                s.aoe, s.max_targets, s.falloff, s.aoe_range, s.aoe_center = True, cfg.get("max_targets", 0), cfg.get("falloff", 1.0), cfg.get("radius", 0.0), cfg.get("center", "player")
        self.start = t0
        self.casting = None          # (spell, end_time, started)
        self.cast_hits = 0
        self.retreat_until = 0.0
        self.last_move = -1.0   # the last tick the player walked (retreat or advance): Auto Shot waits AUTO_SHOT_STAND_STILL after it
        self.advancing = False
        self.wand_next = None
        self.wanding = False
        self.channel = None          # [spell, next_tick, ticks_left, interval, hit]
        self.swinging = None         # the mob whose melee swing is being resolved (mob_swing sets it)
        self.channel_lost = 0.0
        self.queued_swing = None
        self.regen_tick = t0 + 2.0
        self.damage = {}             # spell name -> damage dealt
        self.pet_sources = set()     # damage names dealt by the pet or demon (signature_spells.json's "pet" core source, 2026-10-22)
        self.healing = {}
        self.casts = {}
        self.crits = {}
        self.frozen_casts = 0
        self.spell_casts = 0
        self.log = log
        self.died = False
        self.pet_died = False
        self.pushbacks = 0
        self.swings = 0
        self.last_combo = 0
        self.pet_meet = mob.dist / 2.0
        self.interrupts = 0

    # ------------------------------------------------------------ helpers

    def note(self, msg):
        if self.log is not None:
            self.log.append(f"{self.t - self.start:6.1f}s {msg}")

    def others(self):
        """The pull's other mobs that are still alive (empty for a single pull)."""
        return [x for x in self.mobs if x is not self.m and x.hp > 0]

    def alive(self):
        return [x for x in self.mobs if x.hp > 0]

    def deal(self, spell, amount, crit=False, source="player"):
        self.m.hp -= amount
        self.damage[spell.name] = self.damage.get(spell.name, 0.0) + amount
        if crit:
            self.crits[spell.name] = self.crits.get(spell.name, 0) + 1
        if source == "player":
            self.m.threat_player += amount
        else:
            self.pet_sources.add(spell.name)
            self.m.threat_pet += amount * (self.p.pet.threat_mult if self.p.pet else 1.0)
        if amount > 0 and self.m.rooted(self.t) and not spell.aoe and self.rng.random() < ROOT_BREAK_CHANCE:
            self.m.root_until = self.t
            self.note("root broken")
        if amount > 0 and self.m.feared(self.t) and self.rng.random() < tables.FEAR_BREAK_CHANCE:
            self.m.fear_until = self.t
            self.note("fear broken")

    def heal(self, spell, amount, target="player", crit=False):
        if target == "pet":
            pet = self.p.pet
            if pet is None or not pet.alive:
                return 0.0
            got = min(amount, pet.hp_max - pet.hp)
            pet.hp += got
        else:
            got = min(amount, self.p.hp_max - self.p.hp)
            self.p.hp += got
        self.healing[spell.name] = self.healing.get(spell.name, 0.0) + got
        if crit:
            self.crits[spell.name] = self.crits.get(spell.name, 0) + 1
        return got

    def add_dot(self, name, total, ticks, interval, crit_chance=0.0, crit_mult=1.5):
        if total <= 0 or ticks <= 0:
            return
        self.m.dots.append([name, total / ticks, ticks, self.t + interval, interval, crit_chance, crit_mult])

    def refresh_dot(self, name, total, ticks, interval, crit_chance=0.0, crit_mult=1.5):
        """Re-apply a periodic effect: the old one is replaced (no stacking of the same DoT)."""
        self.m.dots = [d for d in self.m.dots if d[0] != name]
        self.add_dot(name, total, ticks, interval, crit_chance, crit_mult)

    def dot_active(self, name):
        return any(d[0] == name and d[2] > 0 for d in self.m.dots)

    def dot_remaining(self, name):
        for d in self.m.dots:
            if d[0] == name:
                return d[2] * d[4]
        return 0.0

    def apply_chill(self, spell, slow, dur):
        if slow <= 0:
            return
        dur = dur * (1.0 + self.mod.chill_duration_bonus())
        slow = min(0.9, slow + self.mod.chill_extra_slow())
        # the stronger slow wins; refresh duration
        if slow >= self.m.slow or self.t >= self.m.slow_until:
            self.m.slow = slow
        self.m.slow_until = max(self.m.slow_until, self.t + dur)
        self.mod.on_chill(self, spell)

    def apply_periodic(self, spell, crit_chance=0.0):
        """A spell's periodic component (base + coefficient per tick, with the module's multiplier)."""
        if spell.dot <= 0 or spell.dot_ticks <= 0:
            return
        power = self.p.attack_power if spell.kind in ("melee", "ranged") else self.p.spell_power
        total = (spell.dot + spell.dot_coef * power * spell.dot_ticks) * self.mod.periodic_multiplier(spell)
        interval = spell.dot_dur / spell.dot_ticks if spell.dot_dur else 3.0
        crit = (self.p.spell_crit + self.mod.crit_bonus(spell, False)) if self.mod.periodic_can_crit(spell) else 0.0
        self.refresh_dot(spell.name, total, spell.dot_ticks, interval, crit, 1.5 + self.mod.crit_damage_bonus(spell))

    def apply_control(self, spell):
        m, t = self.m, self.t
        if spell.root > 0:
            m.root_until = max(m.root_until, t + spell.root)
        if spell.stun > 0:
            m.stun_until = max(m.stun_until, t + spell.stun)
            if m.casting(t):
                m.cast_end = -1.0
                self.note(f"{spell.name}: the mob's cast is broken")
        if spell.fear > 0:
            m.fear_until = max(m.fear_until, t + spell.fear)
            self.note(f"{spell.name}: mob flees")
            if m.casting(t):
                m.cast_end = -1.0
        if spell.interrupt > 0 and m.casting(t):
            m.cast_end = -1.0
            lock = spell.interrupt + self.mod.interrupt_bonus(self, spell)
            m.lockout_until = max(m.lockout_until, t + lock)
            self.interrupts += 1
            self.note(f"{spell.name} interrupts the mob's cast ({lock:.0f} s lockout)")
        if spell.daze > 0:
            self.apply_chill(spell, spell.daze, spell.chill_dur or 10.0)

    def resolve_spell(self, spell, instant_from_talent=False):
        """Roll hit/crit/damage for a damage spell against the mob and apply on-hit effects (or route by kind)."""
        if spell.kind in ("melee", "ranged"):
            return self.resolve_attack(spell)
        if spell.kind == "heal":
            return self.resolve_heal(spell)
        if spell.kind == "buff":
            self.casts[spell.name] = self.casts.get(spell.name, 0) + 1
            self.mod.on_hit(self, spell, 0.0, False, False)
            return 0.0
        p, m = self.p, self.m
        self.casts[spell.name] = self.casts.get(spell.name, 0) + 1
        self.spell_casts += 1
        charge = self.mod.consume_frozen_charge(self)   # a Fingers of Frost charge is spent by any spell cast
        frozen = m.frozen(self.t) or charge
        if frozen:
            self.frozen_casts += 1
        hit = 1.0 - spell_miss(m.level - p.level) + self.mod.hit_bonus(spell)
        if spell.name not in NO_MISS and self.rng.random() > min(SPELL_HIT_CAP, hit):
            self.note(f"{spell.name} MISS")
            self.mod.on_miss(self, spell)
            return 0.0
        if spell.dmg_max <= 0:
            self.apply_periodic(spell)
            self.note(f"{spell.name} applied")
            self.mod.on_hit(self, spell, 0.0, False, frozen)
            self.apply_chill(spell, spell.chill, spell.chill_dur)
            self.apply_control(spell)
            return 0.0
        base = self.rng.uniform(spell.dmg_min, spell.dmg_max) + spell.coef * p.spell_power
        crit_chance = p.spell_crit + self.mod.crit_bonus(spell, frozen)
        crit = self.rng.random() < crit_chance
        mult = self.mod.damage_multiplier(spell, frozen)
        amount = base * mult * (1.0 - PARTIAL_RESIST_LOSS * self.mod.resist_factor())
        if crit:
            amount *= 1.0 + 0.5 + self.mod.crit_damage_bonus(spell)
        self.deal(spell, amount, crit)
        self.note(f"{spell.name}{' CRIT' if crit else ''}{' (frozen)' if frozen else ''} {amount:.0f} -> mob {max(0, m.hp):.0f}")
        self.apply_periodic(spell)
        self.mod.on_hit(self, spell, amount, crit, frozen)
        self.apply_control(spell)
        self.apply_chill(spell, spell.chill, spell.chill_dur)
        if spell.aoe:
            self.hit_others(spell)
        return amount

    def aoe_radius(self, spell):
        return spell.aoe_range or (spell.range if spell.range and spell.range > MELEE_RANGE else 10.0)

    def switch(self, om):
        """Make another mob of the pull the target (dot spreading); the old target keeps its dots and controls."""
        self.m = om

    def in_area(self, om, spell):
        """Is this other mob inside the spell's area? Target-centred areas measure from the target, the rest from the player."""
        r = self.aoe_radius(spell) + 0.5
        return abs(om.dist - self.m.dist) <= r if spell.aoe_center == "target" else om.dist <= r

    def hit_others(self, spell):
        """An area spell also lands on every other mob of the pull within its radius (own hit / crit rolls, controls and chills)."""
        p = self.p
        target = self.m
        others = sorted([x for x in self.others() if self.in_area(x, spell)], key=lambda x: abs(x.dist - self.m.dist))
        if spell.max_targets:
            others = others[:max(0, spell.max_targets - 1)]
        for i, om in enumerate(others):
            self.m = om
            try:
                if self.rng.random() > min(SPELL_HIT_CAP, 1.0 - spell_miss(om.level - p.level) + self.mod.hit_bonus(spell)):
                    self.note(f"{spell.name} MISS (add)")
                    continue
                frozen = om.frozen(self.t)
                if spell.dmg_max <= 0:
                    self.apply_periodic(spell)
                    self.apply_chill(spell, spell.chill, spell.chill_dur)
                    self.apply_control(spell)
                    continue
                base = self.rng.uniform(spell.dmg_min, spell.dmg_max) + spell.coef * p.spell_power
                crit = self.rng.random() < p.spell_crit + self.mod.crit_bonus(spell, frozen)
                amount = base * self.mod.damage_multiplier(spell, frozen) * (1.0 - PARTIAL_RESIST_LOSS * self.mod.resist_factor()) * (spell.falloff ** (i + 1))
                if crit:
                    amount *= 1.5 + self.mod.crit_damage_bonus(spell)
                self.deal(spell, amount, crit)
                self.note(f"{spell.name}{' CRIT' if crit else ''} {amount:.0f} -> add {max(0, om.hp):.0f}")
                self.apply_periodic(spell)
                self.apply_control(spell)
                self.apply_chill(spell, spell.chill, spell.chill_dur)
            finally:
                self.m = target

    def resolve_heal(self, spell):
        p = self.p
        self.casts[spell.name] = self.casts.get(spell.name, 0) + 1
        target = "pet" if spell.target == "pet" else "player"
        mult = self.mod.heal_multiplier(spell)
        if spell.absorb > 0:
            amount = spell.absorb * mult
            if target == "player":
                p.absorb, p.absorb_until = amount, self.t + 30.0
            self.note(f"{spell.name} absorb {amount:.0f}")
        amount = 0.0
        if spell.heal_max > 0:
            amount = (self.rng.uniform(spell.heal_min, spell.heal_max) + spell.heal_coef * p.spell_power) * mult
            crit = self.rng.random() < p.spell_crit + self.mod.crit_bonus(spell, False)
            if crit:
                amount *= 1.5
            got = self.heal(spell, amount, target, crit)
            self.note(f"{spell.name}{' CRIT' if crit else ''} heals {got:.0f}")
        if spell.hot > 0:
            ticks = max(1, int(spell.hot_dur / 3.0))
            total = (spell.hot + spell.heal_coef * p.spell_power * ticks) * mult
            if tables.HOT_CRIT:   # HoT ticks can crit in Forever (beta notes, post 1: Renew): the expected value, no on-crit procs (as the healer lab)
                total *= 1.0 + 0.5 * max(0.0, min(1.0, p.spell_crit + self.mod.crit_bonus(spell, False)))
            p.hots = [h for h in p.hots if h[0] != spell.name]
            p.hots.append([spell.name, total / ticks, ticks, self.t + spell.hot_dur / ticks, spell.hot_dur / ticks, target])
        self.mod.on_hit(self, spell, amount, False, False)
        return amount

    def attack_table(self, spell, white, hand="mh"):
        """Player attack vs the mob: miss, dodge, parry, glancing (white only), crit, hit (Forever attack table vs a same-level mob)."""
        p = self.p
        r = self.rng.random()
        if spell.kind == "ranged":
            miss = max(0.0, tables.RANGED_MISS - p.hit_bonus - self.mod.hit_bonus(spell))
            if r < miss:
                return "miss"
            r -= miss
            crit = p.ranged_crit + self.mod.crit_bonus(spell, False)
            return "crit" if r < crit else "hit"
        miss = tables.MELEE_MISS + (tables.DW_MISS_PENALTY if (white and p.dual_wield) else 0.0) - p.hit_bonus - self.mod.hit_bonus(spell)
        miss = max(0.0, miss)
        if r < miss:
            return "miss"
        r -= miss
        red = self.mod.dodge_parry_reduction()   # Weapon Expertise and the like
        dodge = max(0.0, tables.MOB_DODGE - red)
        if r < dodge:
            return "dodge"
        r -= dodge
        parry = max(0.0, tables.MOB_PARRY - red) if self.mod.attacks_from_front() else 0.0
        if r < parry:
            return "parry"
        r -= parry
        if white:
            if r < tables.GLANCE_CHANCE:
                return "glance"
            r -= tables.GLANCE_CHANCE
        crit = p.melee_crit + self.mod.crit_bonus(spell, False)
        return "crit" if r < crit else "hit"

    def weapon_damage(self, weapon, ranged=False):
        p = self.p
        ap = p.ranged_ap if ranged else p.attack_power
        base = self.rng.uniform(weapon.dmg_min, weapon.dmg_max)
        return base + (ap / 14.0 + weapon.dps_bonus) * weapon.speed

    def resolve_attack(self, spell, white=False, hand="mh"):
        """A weapon attack: white swing (spell is a placeholder) or a yellow ability (weapon_pct + base damage)."""
        p, m = self.p, self.m
        ranged = spell.kind == "ranged"
        weapon = p.ranged if ranged else (p.oh if hand == "oh" else p.mh)
        if weapon is None:
            return 0.0
        self.casts[spell.name] = self.casts.get(spell.name, 0) + 1
        outcome = self.attack_table(spell, white, hand)
        if outcome in ("miss", "dodge", "parry"):
            self.note(f"{spell.name} {outcome.upper()}")
            self.mod.on_swing(self, spell, outcome, 0.0, hand)
            self.mod.on_miss(self, spell)
            return 0.0
        if white:
            amount = self.weapon_damage(weapon, ranged)
        else:
            amount = self.rng.uniform(spell.dmg_min, spell.dmg_max) + spell.coef * (p.ranged_ap if ranged else p.attack_power)
            if spell.weapon_pct > 0:
                amount += spell.weapon_pct * self.weapon_damage(weapon, ranged)
        if hand == "oh":
            amount *= 0.5
        amount *= self.mod.damage_multiplier(spell, False)
        if outcome == "glance":
            amount *= tables.GLANCE_MULT
        crit = outcome == "crit"
        if crit:
            amount *= 2.0 + self.mod.crit_damage_bonus(spell)
        if spell.school == "physical":
            amount *= 1.0 - armor_mitigation(m.effective_armor(), p.level)
        self.deal(spell, amount, crit)
        if amount > 0 or spell.dot <= 0:
            self.note(f"{spell.name}{' CRIT' if crit else ''}{' (glancing)' if outcome == 'glance' else ''} {amount:.0f} -> mob {max(0, m.hp):.0f}")
        else:
            self.note(f"{spell.name} applied")
        if spell.combo > 0:
            p.combo = min(5, p.combo + spell.combo)
        if white and p.rage_max > 0:
            p.rage = min(p.rage_max, p.rage + self.mod.rage_from_hit(self, amount, weapon, hand, crit))
        self.apply_periodic(spell)
        self.mod.on_swing(self, spell, outcome, amount, hand)
        self.mod.on_hit(self, spell, amount, crit, False)
        self.apply_control(spell)
        self.apply_chill(spell, spell.chill, spell.chill_dur)
        if self.others():   # a pull of several mobs: cleaving attacks and Blade Flurry-like buffs hit more of them
            extra = ((spell.max_targets - 1) if spell.max_targets else 99) if (spell.aoe and not white) else self.mod.extra_targets(self, spell, white)
            if extra > 0:
                self.hit_others_melee(spell, extra, white, hand)
        return amount

    def hit_others_melee(self, spell, extra, white=False, hand="mh"):
        """A cleaving attack also lands on up to `extra` other mobs within its reach: own attack-table roll and armor per mob."""
        p = self.p
        target = self.m
        radius = spell.aoe_range or MELEE_RANGE
        others = sorted([x for x in self.others() if (abs(x.dist - self.m.dist) if spell.aoe_center == "target" else x.dist) <= radius + 0.5], key=lambda x: x.dist)[:extra]
        ranged = spell.kind == "ranged"
        weapon = p.ranged if ranged else (p.oh if hand == "oh" else p.mh)
        if weapon is None:
            return
        for om in others:
            self.m = om
            try:
                outcome = self.attack_table(spell, white, hand)
                if outcome in ("miss", "dodge", "parry"):
                    self.note(f"{spell.name} {outcome.upper()} (add)")
                    continue
                if white:
                    amount = self.weapon_damage(weapon, ranged)
                else:
                    amount = self.rng.uniform(spell.dmg_min, spell.dmg_max) + spell.coef * (p.ranged_ap if ranged else p.attack_power)
                    if spell.weapon_pct > 0:
                        amount += spell.weapon_pct * self.weapon_damage(weapon, ranged)
                if hand == "oh":
                    amount *= 0.5
                amount *= self.mod.damage_multiplier(spell, False)
                if outcome == "glance":
                    amount *= tables.GLANCE_MULT
                crit = outcome == "crit"
                if crit:
                    amount *= 2.0 + self.mod.crit_damage_bonus(spell)
                if spell.school == "physical":
                    amount *= 1.0 - armor_mitigation(om.effective_armor(), p.level)
                self.deal(spell, amount, crit)
                self.note(f"{spell.name}{' CRIT' if crit else ''} {amount:.0f} -> add {max(0, om.hp):.0f}")
                self.apply_periodic(spell)
            finally:
                self.m = target

    def can_afford(self, spell, cost):
        p = self.p
        v = self.mod.veto.get(spell.name) if self.mod.veto else None
        if v:
            if v.get("off"):
                return False
            if v.get("min_mana") and p.mana_max > 0 and p.mana < v["min_mana"] * p.mana_max:
                return False
            m = self.m
            if m is not None and m.hp_max > 0:
                if v.get("min_hp") and m.hp < v["min_hp"] * m.hp_max:
                    return False
                if v.get("max_hp") and m.hp > v["max_hp"] * m.hp_max:
                    return False
        if spell.resource == "none":
            return True
        if spell.resource == "focus":
            return p.pet is not None and p.pet.focus >= cost
        return p.pool(spell.resource) >= cost

    def start_cast(self, spell):
        p = self.p
        cast = self.mod.cast_time(spell)
        cost = self.mod.mana_cost(spell)
        if not self.can_afford(spell, cost):
            return False
        if spell.on_next_swing:
            self.queued_swing = spell
            return True
        if spell.channel > 0:
            self.spend(cost, spell)
            p.gcd_until = self.t + self.mod.gcd_of(spell)
            self.casting = None
            self.wanding = False
            interval = spell.channel / max(1, spell.dot_ticks)
            hit = self.rng.random() <= min(SPELL_HIT_CAP, 1.0 - spell_miss(self.m.level - p.level) + self.mod.hit_bonus(spell)) if spell.dot > 0 or spell.dmg_max > 0 else True
            self.casts[spell.name] = self.casts.get(spell.name, 0) + 1
            self.spell_casts += 1
            if not hit:
                self.note(f"{spell.name} MISS")
                self.mod.on_miss(self, spell)
                self.mod.after_cast(self, spell)
                return True
            self.channel = [spell, self.t + interval, max(1, spell.dot_ticks), interval, True]
            self.channel_lost = 0.0
            self.cast_hits = 0
            self.apply_chill(spell, spell.chill, spell.chill_dur)
            self.note(f"{spell.name} channel")
            return True
        if cast <= 0:
            self.spend(cost, spell)
            p.gcd_until = self.t + self.mod.gcd_of(spell)
            self.resolve_spell(spell)
            self.mod.after_cast(self, spell)
            return True
        self.casting = (spell, self.t + cast, self.t)
        self.cast_hits = 0
        self.wanding = False
        p.gcd_until = self.t + self.mod.gcd_of(spell)
        return True

    def spend(self, cost, spell):
        p = self.p
        cost = self.mod.final_cost(self, spell, cost)
        if spell.resource == "mana":
            p.mana = max(0.0, p.mana - cost)
            p.fsr_until = self.t + 5.0
            p.last_cast_end = self.t
        elif spell.resource == "energy":
            p.energy = max(0.0, p.energy - cost)
        elif spell.resource == "rage":
            p.rage = max(0.0, p.rage - cost)
        elif spell.resource == "health":
            p.hp = max(1.0, p.hp - cost)
        elif spell.resource == "focus" and p.pet:
            p.pet.focus = max(0.0, p.pet.focus - cost)
        if spell.combo < 0:
            self.last_combo = p.combo
            p.combo = 0

    def finish_cast(self):
        spell, end, started = self.casting
        self.casting = None
        self.spend(self.mod.mana_cost(spell), spell)
        self.resolve_spell(spell)
        self.mod.after_cast(self, spell)

    def channel_tick(self):
        spell, next_tick, left, interval, hit = self.channel
        p, m = self.p, self.m
        power = p.spell_power
        amount = 0.0
        if spell.dot > 0:
            base = spell.dot / max(1, spell.dot_ticks) + spell.dot_coef * power
            crit = self.rng.random() < (p.spell_crit + self.mod.crit_bonus(spell, False)) if self.mod.periodic_can_crit(spell) else False
            amount = base * self.mod.periodic_multiplier(spell) * (1.0 - PARTIAL_RESIST_LOSS * self.mod.resist_factor())
            if crit:
                amount *= 1.5 + self.mod.crit_damage_bonus(spell)
            self.deal(spell, amount, crit)
            self.note(f"{spell.name} tick{' CRIT' if crit else ''} {amount:.0f} -> mob {max(0, m.hp):.0f}")
            if "drain" in spell.tags:
                self.heal(spell, amount)
            self.mod.on_tick(self, spell, amount, crit)
            if spell.aoe:
                target = self.m
                for om in self.others():
                    if not self.in_area(om, spell):
                        continue
                    self.m = om
                    try:
                        oc = self.rng.random() < (p.spell_crit + self.mod.crit_bonus(spell, False)) if self.mod.periodic_can_crit(spell) else False
                        oa = base * self.mod.periodic_multiplier(spell) * (1.0 - PARTIAL_RESIST_LOSS * self.mod.resist_factor()) * ((1.5 + self.mod.crit_damage_bonus(spell)) if oc else 1.0)
                        self.deal(spell, oa, oc)
                        self.note(f"{spell.name} tick {oa:.0f} -> add {max(0, om.hp):.0f}")
                    finally:
                        self.m = target
        if spell.hot > 0 or spell.heal_max > 0:   # a channelled heal (Mend Pet, Health Funnel, Tranquility)
            per = (spell.hot + spell.heal_coef * power * max(1, spell.dot_ticks)) / max(1, spell.dot_ticks) * self.mod.heal_multiplier(spell)
            got = self.heal(spell, per, "pet" if spell.target == "pet" else "player")
            self.mod.on_tick(self, spell, got, False)
        left -= 1
        if left <= 0 or m.hp <= 0:
            self.channel = None
            self.mod.after_cast(self, spell)
        else:
            self.channel = [spell, next_tick + interval, left, interval, hit]

    def wand_shot(self):
        p, m = self.p, self.m
        self.casts["Wand"] = self.casts.get("Wand", 0) + 1
        if self.rng.random() < ranged_miss(m.level - p.level):
            self.note("Wand miss")
            return
        dmg = self.mod.wand_damage() * self.rng.uniform(0.8, 1.2)
        # a wand deals spell-school damage (Shadow, Fire, Frost, Arcane, Nature): armor does not reduce it, partial resists do (the
        # spells' average loss, no talent factor). Until 2026-10-17 the mob's armor cut every wand shot (audit finding 8).
        dmg *= 1.0 - PARTIAL_RESIST_LOSS
        crit = self.rng.random() < p.ranged_crit
        if crit:
            dmg *= 2.0
        self.deal(Spell("Wand", "physical"), dmg, crit)
        self.note(f"Wand{' CRIT' if crit else ''} {dmg:.0f} -> mob {max(0, m.hp):.0f}")

    def auto_swing(self, hand):
        p = self.p
        weapon = p.mh if hand == "mh" else p.oh
        if weapon is None:
            return
        self.swings += 1
        if hand == "mh" and self.queued_swing is not None:
            spell = self.queued_swing
            cost = self.mod.mana_cost(spell)
            if self.can_afford(spell, cost):
                self.queued_swing = None
                self.spend(cost, spell)
                self.resolve_attack(spell, white=False, hand="mh")
                self.mod.after_cast(self, spell)
                return
            self.queued_swing = None
        white = Spell("Melee" if hand == "mh" else "Melee (off-hand)", "physical", kind="melee", hand=hand, resource="none")
        self.resolve_attack(white, white=True, hand=hand)

    def auto_shot(self):
        p = self.p
        if p.ranged is None:
            return
        self.swings += 1
        shot = Spell("Auto Shot", "physical", kind="ranged", resource="none")
        self.resolve_attack(shot, white=True)

    def pet_swing(self):
        pet, m, p = self.p.pet, self.m, self.p
        r = self.rng.random()
        miss = max(0.0, tables.MELEE_MISS + tables.MOB_DODGE + tables.MOB_PARRY - pet.hit_bonus)
        name = f"{pet.name} melee"
        if r < miss:
            self.note(f"{name} miss")
            return
        amount = (self.rng.uniform(pet.dmg_min, pet.dmg_max) + pet.attack_power / 14.0 * pet.speed) * pet.dmg_mult
        crit = self.rng.random() < pet.crit
        if crit:
            amount *= 2.0
        amount *= 1.0 - armor_mitigation(m.effective_armor(), p.level)
        self.deal(Spell(name, "physical"), amount, crit, source="pet")
        self.note(f"{name}{' CRIT' if crit else ''} {amount:.0f} -> mob {max(0, m.hp):.0f}")
        self.mod.on_pet_hit(self, amount, crit)

    def pet_ability(self, spell):
        """A pet ability chosen by the module: focus/mana cost, then a melee or spell hit from the pet."""
        pet, m, p = self.p.pet, self.m, self.p
        cost = spell.cost
        if spell.resource == "focus":
            if pet.focus < cost:
                return False
            pet.focus -= cost
        elif spell.resource == "mana":
            if pet.mana < cost:
                return False
            pet.mana -= cost
        if spell.cooldown > 0:
            pet.cooldowns[spell.name] = self.t + spell.cooldown
        self.casts[spell.name] = self.casts.get(spell.name, 0) + 1
        if spell.kind == "buff":   # a taunt (Torment, Growl): flat threat in dmg_min
            m.threat_pet += spell.dmg_min
            return True
        r = self.rng.random()
        if spell.kind == "spell":
            if r > 1.0 - spell_miss(m.level - p.level) + pet.hit_bonus:
                self.note(f"{spell.name} MISS")
                return True
            amount = (self.rng.uniform(spell.dmg_min, spell.dmg_max) + spell.coef * pet.spell_power) * pet.dmg_mult
            crit = self.rng.random() < pet.crit
            if crit:
                amount *= 1.5
        else:
            if r < max(0.0, tables.MELEE_MISS + tables.MOB_DODGE + tables.MOB_PARRY - pet.hit_bonus):
                self.note(f"{spell.name} MISS")
                return True
            amount = (self.rng.uniform(spell.dmg_min, spell.dmg_max) + spell.weapon_pct * (self.rng.uniform(pet.dmg_min, pet.dmg_max) + pet.attack_power / 14.0 * pet.speed)) * pet.dmg_mult
            crit = self.rng.random() < pet.crit
            if crit:
                amount *= 2.0
            if spell.school == "physical":
                amount *= 1.0 - armor_mitigation(m.effective_armor(), p.level)
        self.deal(spell, amount, crit, source="pet")
        if spell.dot > 0:
            self.refresh_dot(spell.name + " dot", spell.dot * pet.dmg_mult, spell.dot_ticks, spell.dot_dur / max(1, spell.dot_ticks))
        self.note(f"{spell.name}{' CRIT' if crit else ''} {amount:.0f} -> mob {max(0, m.hp):.0f}")
        self.mod.on_pet_hit(self, amount, crit)
        return True

    def mob_swing(self, mob=None):
        p = self.p
        m = mob if mob is not None else self.m
        self.swinging = m   # the mob whose swing this is: on_dodge / on_parry / on_hit_taken hooks read fight.swinging (an add's swing in a pull)
        pet = p.pet
        if m.target == "pet" and pet is not None and pet.alive:
            if self.rng.random() > MOB_HIT_CHANCE - 0.05:
                self.note("mob misses the pet")
                return
            dmg = m.dmg * self.rng.uniform(1 - MOB_DMG_SPREAD, 1 + MOB_DMG_SPREAD)
            dmg *= 1.0 - armor_mitigation(pet.armor, m.level)
            if self.rng.random() < MOB_CRIT_CHANCE:
                dmg *= 2.0
            pet.hp -= dmg
            self.note(f"mob hits pet {dmg:.0f} -> pet {max(0, pet.hp):.0f}")
            if pet.hp <= 0:
                pet.alive = False
                pet.engaged = False
                self.pet_died = True
                m.target = "player"
                m.pet_in_melee = False
                m.in_melee = False
                self.note("pet dies; mob turns to the player")
                self.mod.on_pet_death(self)
            return
        roll = self.rng.random()
        dodge = p.dodge + self.mod.dodge_bonus(self)
        parry = p.parry + self.mod.parry_bonus(self)
        if roll > MOB_HIT_CHANCE - dodge - parry:
            self.note("mob misses")
            if roll > 1.0 - dodge:
                self.mod.on_dodge(self)
            elif parry > 0 and roll > 1.0 - dodge - parry:
                self.mod.on_parry(self)
            return
        # shield block (only with a shield: Player.block > 0): the slice of the hit range just below the misses; a blocked hit
        # cannot crit and loses the block value after armor (Classic attack table). No extra random draw, so shieldless runs are unchanged.
        blocked = False
        if p.block > 0:
            block = p.block + self.mod.block_bonus(self)
            blocked = roll > MOB_HIT_CHANCE - dodge - parry - block
        pre_armor = m.dmg * self.rng.uniform(1 - MOB_DMG_SPREAD, 1 + MOB_DMG_SPREAD)
        if m.dmg_reduction > 0 and self.t < m.dmg_reduction_until:
            pre_armor = max(0.0, pre_armor - m.dmg_reduction)
        dmg = pre_armor * (1.0 - armor_mitigation(p.armor + self.mod.armor_bonus(), m.level))
        crit_taken = self.rng.random() < MOB_CRIT_CHANCE
        if blocked:
            crit_taken = False
            full = dmg
            dmg = max(0.0, dmg - p.block_value)
            pre_armor *= dmg / full if full > 0 else 0.0   # rage from damage taken: only the part that got through
            self.note(f"blocked {full - dmg:.0f}")
            self.mod.on_block(self)
        if crit_taken:
            dmg *= 2.0
        absorbed = 0.0
        if p.absorb > 0 and self.t < p.absorb_until:
            absorbed = min(p.absorb, dmg)
            p.absorb -= absorbed
            dmg -= absorbed
        dmg = self.mod.split_damage_taken(self, dmg)
        p.hp -= dmg
        if p.rage_max > 0:   # a crit taken pays rage on its doubled damage (beta notes 2026-10-08: the rage calculation now handles
            # "increased damage taken from combat multipliers, in particular from taking critical strikes"; until 2026-10-17 it did not)
            p.rage = min(p.rage_max, p.rage + tables.rage_from_damage_taken(pre_armor * (2.0 if crit_taken else 1.0), m.level))
        self.note(f"mob hits {dmg:.0f}{f' (absorbed {absorbed:.0f})' if absorbed else ''} -> me {max(0, p.hp):.0f}")
        self.damage_taken_effects(dmg, crit_taken)

    def mob_bolt(self, mob=None):
        """A caster mob's bolt lands: spell damage (no armor) on the pet or the player, pushback like a melee hit."""
        p = self.p
        m = mob if mob is not None else self.m
        self.swinging = m
        pet = p.pet
        if m.target == "pet" and pet is not None and pet.alive:
            if self.rng.random() > MOB_HIT_CHANCE:
                self.note("mob's bolt misses the pet")
                return
            dmg = m.cast_dmg * self.rng.uniform(1 - MOB_DMG_SPREAD, 1 + MOB_DMG_SPREAD)
            if self.rng.random() < tables.MOB_CAST_CRIT:
                dmg *= 1.5
            pet.hp -= dmg
            self.note(f"mob's bolt hits pet {dmg:.0f} -> pet {max(0, pet.hp):.0f}")
            if pet.hp <= 0:
                pet.alive = False
                pet.engaged = False
                self.pet_died = True
                m.target = "player"
                m.pet_in_melee = False
                m.in_melee = False
                self.note("pet dies; mob turns to the player")
                self.mod.on_pet_death(self)
            return
        if self.rng.random() > MOB_HIT_CHANCE:
            self.note("mob's bolt misses")
            return
        pre = m.cast_dmg * self.rng.uniform(1 - MOB_DMG_SPREAD, 1 + MOB_DMG_SPREAD)
        crit_taken = self.rng.random() < tables.MOB_CAST_CRIT
        dmg = pre * (1.5 if crit_taken else 1.0)
        absorbed = 0.0
        if p.absorb > 0 and self.t < p.absorb_until:
            absorbed = min(p.absorb, dmg)
            p.absorb -= absorbed
            dmg -= absorbed
        dmg = self.mod.split_damage_taken(self, dmg)
        p.hp -= dmg
        if p.rage_max > 0:
            p.rage = min(p.rage_max, p.rage + tables.rage_from_damage_taken(pre * (1.5 if crit_taken else 1.0), m.level))   # crits: as a melee hit's
        self.note(f"mob's bolt hits {dmg:.0f}{f' (absorbed {absorbed:.0f})' if absorbed else ''} -> me {max(0, p.hp):.0f}")
        self.damage_taken_effects(dmg, crit_taken)

    def damage_taken_effects(self, dmg, crit_taken):
        p = self.p
        if self.casting and dmg > 0:   # a hit that reached health pushes the cast back
            spell, end, started = self.casting
            delay = PUSHBACK_FIRST if self.cast_hits == 0 else PUSHBACK_NEXT
            cast = self.mod.cast_time(spell)
            delay = max(0.0, min(delay, 2 * cast - (end - started)))   # total pushback never exceeds the cast time (wowsims rule)
            if self.mod.pushback_resisted(self, spell):
                delay = 0.0
            self.cast_hits += 1
            self.casting = (spell, end + delay, started)
            self.pushbacks += 1
        elif self.channel and dmg > 0:   # a hit shortens a channel: lost time drops ticks from its end
            spell = self.channel[0]
            if CHANNEL_PUSHBACK > 0:   # 25% of the channel's full duration per hit (Classic, the raid simulator)
                delay = CHANNEL_PUSHBACK * spell.channel
            else:
                delay = PUSHBACK_FIRST if self.cast_hits == 0 else PUSHBACK_NEXT
            if self.mod.pushback_resisted(self, spell):
                delay = 0.0
            self.cast_hits += 1
            self.channel_lost += delay
            if self.channel_lost >= self.channel[3] and self.channel[2] > 1:
                self.channel_lost -= self.channel[3]
                self.channel[2] -= 1
                self.pushbacks += 1
        self.mod.on_hit_taken(self, dmg, crit_taken)

    # ------------------------------------------------------------ main loop

    def extra_mob_tick(self, om, t):
        """One 0.1 s step of a pull's extra mob: runs at the player, casts if a caster, flees if a runner, swings in melee."""
        p = self.p
        if om.runner and not om.fled and 0 < om.hp <= tables.RUNNER_HP * om.hp_max and not om.stunned(t) and not om.feared(t):
            om.fled = True
            if not om.rooted(t):
                om.flee_until = t + tables.RUNNER_TIME
                om.in_melee = False
        stands = om.caster and om.can_cast(t) and om.dist <= tables.MOB_CAST_RANGE
        if om.caster:
            if om.casting(t):
                if om.incapacitated(t):
                    om.cast_end = -1.0
                elif t >= om.cast_end:
                    om.cast_end = -1.0
                    om.cast_next = t + tables.MOB_CAST_GAP
                    self.mob_bolt(om)
            elif stands and t >= om.cast_next:
                om.cast_end = t + tables.MOB_CAST_TIME
        if om.fleeing(t) or om.feared(t):
            if not om.rooted(t):
                om.dist += om.speed(t) * DT
            if om.dist > MELEE_RANGE + 0.5:
                om.in_melee = False
        elif not om.in_melee:
            if not om.rooted(t) and not om.stunned(t) and not stands:
                om.dist -= om.speed(t) * DT
            if self.advancing and t >= self.retreat_until:
                om.dist -= MOB_SPEED * DT
            if om.dist <= MELEE_RANGE:
                om.dist = MELEE_RANGE
                om.in_melee = True
                om.swing_at = t
        if t < self.retreat_until:
            om.dist += MOB_SPEED * DT
            if not om.rooted(t) and not om.incapacitated(t) and not stands:
                om.dist -= om.speed(t) * DT
            if om.dist > MELEE_RANGE + 0.5:
                om.in_melee = False
        if om.in_melee and om.incapacitated(t):
            om.swing_at = max(om.swing_at, max(om.stun_until, om.fear_until, om.flee_until))
        if om.in_melee and t >= om.swing_at and not om.casting(t) and p.hp > 0:
            self.mob_swing(om)
            om.swing_at = t + MOB_SWING * (1.0 + om.attack_slow if t < om.attack_slow_until else 1.0)

    def tick_dots(self, om, t):
        for dot in list(om.dots):
            if t >= dot[3]:
                amount = dot[1]
                crit = False
                if len(dot) > 5 and dot[5] > 0 and self.rng.random() < dot[5]:
                    crit = True
                    amount *= dot[6]
                om.hp -= amount
                self.damage[dot[0]] = self.damage.get(dot[0], 0.0) + amount
                om.threat_player += amount
                dot[2] -= 1
                dot[3] += dot[4]
                if dot[2] <= 0:
                    om.dots.remove(dot)

    def run(self, max_time=600.0):
        p, m = self.p, self.m
        pet = p.pet
        self.mod.on_fight_start(self)
        while True:
            t = self.t
            if m.hp <= 0:
                nxt = self.others()
                if not nxt:
                    return "kill"
                self.m = m = nxt[0]      # the pull goes on: the next add becomes the target
                self.note(f"target down, {len(nxt)} left")
                continue
            if p.hp <= 0:
                self.died = True
                return "death"
            if t - self.start > max_time:
                return "timeout"
            # regen tick (mana only in combat; health regen is out of combat); energy ticks with it
            if t >= self.regen_tick:
                self.regen_tick += 2.0
                if p.mana_max > 0:
                    tick = self.mod.mana_regen(p, t)
                    if t < p.fsr_until:
                        tick *= min(1.0, p.regen_while_casting)
                    if "mp5" in tables.GEAR_BONUS:   # gear mana per 5 s regenerates while casting too (2026-11-09)
                        tick += tables.GEAR_BONUS["mp5"] * 0.4
                    p.mana = min(p.mana_max, p.mana + tick)
                if p.energy_max > 0:
                    p.energy = min(p.energy_max, p.energy + tables.ENERGY_PER_TICK)
                if pet is not None and pet.alive:
                    pet.focus = min(pet.focus_max, pet.focus + pet.focus_regen * 2.0)
                    pet.mana = min(pet.mana_max, pet.mana + pet.mana_regen * 2.0)
                self.mod.on_regen_tick(self, p, t)
            # damage over time: no root breaking; Forever periodic damage may crit (snapshotted chance)
            for dot in list(m.dots):
                if t >= dot[3]:
                    amount = dot[1]
                    crit = False
                    if len(dot) > 5 and dot[5] > 0 and self.rng.random() < dot[5]:
                        crit = True
                        amount *= dot[6]
                    m.hp -= amount
                    self.damage[dot[0]] = self.damage.get(dot[0], 0.0) + amount
                    m.threat_player += amount
                    self.note(f"{dot[0]} tick{' CRIT' if crit else ''} {amount:.0f} -> mob {max(0, m.hp):.0f}")
                    if crit:
                        self.crits[dot[0]] = self.crits.get(dot[0], 0) + 1
                    dot[2] -= 1
                    dot[3] += dot[4]
                    self.mod.on_tick(self, Spell(dot[0], "periodic"), amount, crit)
                    if dot[2] <= 0:
                        m.dots.remove(dot)
            for om in self.others():
                self.tick_dots(om, t)
            # heals over time on the player or pet
            for hot in list(p.hots):
                if t >= hot[3]:
                    self.heal(Spell(hot[0], "holy"), hot[1], hot[5])
                    hot[2] -= 1
                    hot[3] += hot[4]
                    if hot[2] <= 0:
                        p.hots.remove(hot)
            # a runner: flees at low health for a few seconds, then comes back (a root or stun holds it)
            if m.runner and not m.fled and 0 < m.hp <= tables.RUNNER_HP * m.hp_max and not m.stunned(t) and not m.feared(t):
                m.fled = True
                if not m.rooted(t):
                    m.flee_until = t + tables.RUNNER_TIME
                    m.in_melee = False
                    m.pet_in_melee = False
                    self.pet_meet = tables.RUNNER_TIME * MOB_SPEED
                    self.note(f"mob flees at {m.hp / m.hp_max * 100:.0f}% health")
            # a caster mob: casts from range at whoever it targets (broken by stuns / fears / interrupts, then it runs in)
            stands = m.caster and m.can_cast(t) and m.dist <= tables.MOB_CAST_RANGE and (m.target == "player" or (pet is not None and pet.alive))
            if m.caster:
                if m.casting(t):
                    if m.incapacitated(t):
                        m.cast_end = -1.0
                    elif t >= m.cast_end:
                        m.cast_end = -1.0
                        m.cast_next = t + tables.MOB_CAST_GAP
                        self.mob_bolt()
                elif stands and t >= m.cast_next:
                    m.cast_end = t + tables.MOB_CAST_TIME
                    self.note("mob starts casting")
            # pet engagement: the pet runs at the mob and the mob at the pet; they meet halfway (a casting mob stands still)
            if m.fleeing(t):
                if not m.rooted(t):
                    m.dist += m.speed(t) * DT
                if self.advancing and t >= self.retreat_until:
                    m.dist -= MOB_SPEED * DT
            elif pet is not None and pet.alive and pet.engaged and m.target == "pet" and not m.pet_in_melee:
                if not m.rooted(t) and not m.incapacitated(t) and not stands:
                    m.dist -= m.speed(t) * DT
                self.pet_meet -= (MOB_SPEED + (0 if m.rooted(t) or m.incapacitated(t) or stands else m.speed(t))) * DT
                if self.pet_meet <= 0:
                    m.pet_in_melee = True
                    pet.swing_at = t
                    m.swing_at = t
                    self.note(f"{pet.name} engages the mob at {m.dist:.0f} yd from me")
            # mob movement towards the player
            elif not m.in_melee:
                if m.feared(t):
                    m.dist += m.speed(t) * DT
                elif not m.rooted(t) and not m.stunned(t) and m.target == "player" and not stands:
                    m.dist -= m.speed(t) * DT
                if self.advancing and not m.in_melee and t >= self.retreat_until:
                    m.dist -= MOB_SPEED * DT
                if m.dist <= MELEE_RANGE:
                    m.dist = MELEE_RANGE
                    m.in_melee = True
                    self.advancing = False
                    m.swing_at = t
                    p.swing_mh = max(p.swing_mh, t)
                    p.swing_oh = max(p.swing_oh, t + p.oh.speed / 2 if p.oh else t)
                    self.note("mob in melee")
            else:
                if m.feared(t):
                    m.dist += m.speed(t) * DT
                    if m.dist > MELEE_RANGE + 0.5:
                        m.in_melee = False
            # player retreat: moving away while the mob is rooted (or slowed); no casting meanwhile
            if t < self.retreat_until:
                m.dist += MOB_SPEED * DT
                if not m.rooted(t) and not m.incapacitated(t) and m.target == "player" and not stands:
                    m.dist -= m.speed(t) * DT
                if m.dist > MELEE_RANGE + 0.5:
                    m.in_melee = False
            # threat: a pet holds the mob until the player's threat passes it by the ranged margin; it takes the mob back when its own threat passes the player's by the melee margin
            if pet is not None and pet.alive and m.target == "pet" and m.pet_in_melee and m.threat_pet > 0 and m.threat_player > tables.THREAT_SWITCH * (m.threat_pet + self.mod.pet_threat_bonus(self)) and m.threat_player > 50:
                m.target = "player"
                m.pet_in_melee = False
                m.in_melee = False
                pet.engaged = True
                self.note(f"mob turns on me (threat {m.threat_player:.0f} vs pet {m.threat_pet:.0f})")
            elif pet is not None and pet.alive and pet.engaged and m.target == "player" and (m.threat_pet + self.mod.pet_threat_bonus(self)) > 1.1 * m.threat_player:
                m.target = "pet"
                m.pet_in_melee = True
                m.in_melee = False
                m.swing_at = max(m.swing_at, t + 0.5)
                self.note(f"pet takes the mob back (threat {m.threat_pet:.0f} vs me {m.threat_player:.0f})")
            # mob swings (a rooted mob still swings if it is in melee range: a root is not a stun; a stunned or feared one does not)
            if m.target == "pet" and pet is not None and pet.alive and m.pet_in_melee:
                if m.incapacitated(t):
                    m.swing_at = max(m.swing_at, max(m.stun_until, m.fear_until))
                if t >= m.swing_at and not m.casting(t):
                    self.mob_swing()
                    m.swing_at = t + MOB_SWING * (1.0 + m.attack_slow if t < m.attack_slow_until else 1.0)
                if pet.alive and m.hp > 0 and t >= pet.swing_at:
                    self.pet_swing()
                    pet.swing_at = t + pet.speed
            else:
                if m.in_melee and m.incapacitated(t):
                    m.swing_at = max(m.swing_at, max(m.stun_until, m.fear_until))
                if m.in_melee and t >= m.swing_at and not m.casting(t):
                    self.mob_swing()
                    m.swing_at = t + MOB_SWING * (1.0 + m.attack_slow if t < m.attack_slow_until else 1.0)
                # a pet fighting a mob that is on the player: the pet keeps swinging from behind
                if pet is not None and pet.alive and pet.engaged and m.hp > 0 and (m.in_melee or m.pet_in_melee) and t >= pet.swing_at:
                    self.pet_swing()
                    pet.swing_at = t + pet.speed
            for om in self.others():
                self.extra_mob_tick(om, t)
            if m.hp <= 0 or p.hp <= 0:
                continue
            # pet abilities (Claw, Bite, Firebolt ...) between its swings
            if pet is not None and pet.alive and pet.engaged and (m.pet_in_melee or m.in_melee or pet.caster):
                ab = self.mod.pet_decide(self)
                if ab is not None and pet.cooldowns.get(ab.name, -1.0) <= t:
                    self.pet_ability(ab)
            # player auto attacks (melee classes) when in melee and not casting
            if self.mod.melee and m.in_melee and not self.casting and t >= self.retreat_until and not m.feared(t):
                if t >= p.swing_mh and p.mh is not None:
                    self.auto_swing("mh")
                    p.swing_mh = t + p.mh.speed * self.mod.swing_speed_factor()
                if p.oh is not None and t >= p.swing_oh:
                    self.auto_swing("oh")
                    p.swing_oh = t + p.oh.speed * self.mod.swing_speed_factor()
            # ranged auto shot (hunter): outside the dead zone, standing still for 0.5 s, not channelling. Blizzard's 16 Oct notes: "Your
            # character will still fire Auto Shot while casting spells like Aimed Shot or Sniper Shot" (a cast shot keeps the timer running;
            # until 2026-10-17 any cast stopped it) and "Auto Shot now requires you to stand still for 0.5 seconds before shooting".
            if t < self.retreat_until or (self.advancing and not m.in_melee):
                self.last_move = t
            if self.mod.ranged and p.ranged is not None and (not self.casting or self.casting[0].kind == "ranged") and not self.channel \
                    and t >= self.retreat_until and t >= self.last_move + tables.AUTO_SHOT_STAND_STILL and m.dist >= tables.MIN_RANGED_RANGE and t >= p.shot_at:
                self.auto_shot()
                p.shot_at = t + p.ranged.speed * self.mod.swing_speed_factor()
            # player: a cast or channel that ends this step lets the next decision happen in the same step (until 2026-10-18 it waited one
            # step, a hidden 0.1 s after every cast: audit row 70)
            if self.casting:
                spell, end, started = self.casting
                if t + EPS >= end:
                    self.finish_cast()
            elif self.channel:
                if t + EPS >= self.channel[1]:
                    self.channel_tick()
            if self.casting or self.channel or m.hp <= 0 or p.hp <= 0:
                pass
            elif t >= self.retreat_until and t + EPS >= p.gcd_until:
                action = self.mod.decide(self)
                if action is None:
                    pass
                elif action == "wand":
                    if not self.wanding:
                        self.wanding = True
                        self.wand_next = t + 0.5
                    if t >= self.wand_next:
                        self.wand_shot()
                        self.wand_next = t + WAND_SPEED
                elif action == "retreat":
                    self.retreat_until = t + self.mod.retreat_time()
                    self.wanding = False
                    self.advancing = False
                elif action == "advance":
                    self.advancing = True
                    self.wanding = False
                elif action == "shoot":
                    self.wanding = False
                else:
                    self.wanding = False
                    if getattr(action, "charge", False):
                        m.dist = MELEE_RANGE
                        m.in_melee = True
                        m.swing_at = t + 1.0
                        p.swing_mh = t
                        self.advancing = False
                    self.start_cast(action)
            elif self.wanding and t >= self.wand_next and t >= self.retreat_until:
                self.wand_shot()
                self.wand_next = t + WAND_SPEED
            self.t += DT


class Session:
    """Many fights in a row with downtime between them. Returns aggregate statistics."""

    def __init__(self, mod, level=None, fights=1000, seed=1, mob_level_offset=0, log_first=0):
        self.mod, self.level, self.fights, self.seed, self.off = mod, level or mod.level, fights, seed, mob_level_offset
        self.log_first = log_first

    def make_mob(self, i, k=0):
        r = random.Random(self.seed * 1_000_003 + i + (k * 131_071 + 7 if k else 0))   # common random numbers: the same mob for every build
        lvl = self.level + self.off
        hp = mob_health(lvl) * r.uniform(1 - MOB_HP_SPREAD, 1 + MOB_HP_SPREAD)
        dmg = mob_melee_damage(lvl) * r.uniform(0.9, 1.1)
        share = tables.MOB_CASTER_SHARE if tables.MOB_CASTER_SHARE is not None else tables.mob_caster_share(lvl)
        caster = share > 0 and r.random() < share
        if caster:
            hp *= tables.mob_caster_health(lvl) / mob_health(lvl)
            dmg *= tables.mob_caster_damage(lvl) / mob_melee_damage(lvl)
        runner = tables.RUNNER_SHARE > 0 and r.random() < tables.RUNNER_SHARE
        return Mob(level=lvl, hp_max=hp, hp=hp, dmg=dmg, armor=mob_armor(lvl), dist=self.mod.pull_range(), caster=caster,
                   cast_dmg=dmg * tables.MOB_CAST_DMG_MULT, runner=runner)

    def run(self):
        mod = self.mod
        p = mod.make_player(self.level)
        t = 0.0
        stats = {"kills": 0, "deaths": 0, "pet_deaths": 0, "fight_time": [], "downtime": 0.0, "drink_time": 0.0, "eat_time": 0.0,
                 "heal_time": 0.0, "mana_spent": [], "damage": {}, "pet_sources": set(), "healing": {}, "casts": {}, "crits": {}, "frozen_casts": 0,
                 "spell_casts": 0, "pushbacks": 0, "timeouts": 0, "hp_after": [], "mana_after": [], "logs": [], "casters": 0, "interrupts": 0, "runners": 0, "pulls": 0}
        i = 0
        while stats["kills"] < self.fights:
            mob = self.make_mob(i)
            extra = [self.make_mob(i, k) for k in range(1, max(1, int(tables.MOBS_PER_PULL)))]
            rng = random.Random(self.seed * 7_919 + i * 13 + 1)
            log = [] if i < self.log_first else None
            pool = mod.resource
            before = p.pool(pool) if pool != "none" else 0.0
            f = Fight(mod, p, mob, rng, t0=t, log=log, extra=extra)
            f.pet_meet = mob.dist if mob.caster else mob.dist / 2.0
            if mob.caster:
                stats["casters"] += 1
            if mob.runner:
                stats["runners"] += 1
            if p.pet is not None and p.pet.alive and not p.pet.caster:
                p.pet.engaged = True
                mob.target = "pet"
            result = f.run()
            t = f.t
            if log is not None:
                stats["logs"].append((result, log))
            for k, v in f.damage.items():
                stats["damage"][k] = stats["damage"].get(k, 0.0) + v
            stats["pet_sources"] |= f.pet_sources
            for k, v in f.healing.items():
                stats["healing"][k] = stats["healing"].get(k, 0.0) + v
            for k, v in f.casts.items():
                stats["casts"][k] = stats["casts"].get(k, 0) + v
            for k, v in f.crits.items():
                stats["crits"][k] = stats["crits"].get(k, 0) + v
            stats["frozen_casts"] += f.frozen_casts
            stats["spell_casts"] += f.spell_casts
            stats["pushbacks"] += f.pushbacks
            stats["interrupts"] += f.interrupts
            stats["pulls"] += 1
            stats["kills"] += sum(1 for x in f.mobs if x.hp <= 0) - (1 if result == "kill" else 0)   # adds killed (the target's kill is counted below)
            if f.pet_died:
                stats["pet_deaths"] += 1
            i += 1
            p.hots.clear()
            if result == "death":
                stats["deaths"] += 1
                stats["kills"] += 1 if mob.hp <= 0 else 0   # a target killed before the player died counts (its adds are counted above)
                t += mod.death_time(p, t)
                p.hp, p.mana = p.hp_max, p.mana_max
                p.energy, p.rage, p.combo = p.energy_max, 0.0, 0
                p.buffs.clear()
                p.absorb = 0.0
                if p.pet is not None:
                    p.pet.hp, p.pet.alive, p.pet.focus, p.pet.mana = p.pet.hp_max, True, p.pet.focus_max, p.pet.mana_max
                mod.after_death(p, t)
                continue
            if result == "timeout":
                stats["timeouts"] += 1
                p.hp, p.mana = p.hp_max, p.mana_max
                continue
            stats["kills"] += 1
            stats["fight_time"].append(f.t - f.start)
            stats["mana_spent"].append(max(0.0, before - (p.pool(pool) if pool != "none" else 0.0)) if pool in ("mana", "energy", "rage") else 0.0)
            mod.on_kill(f)
            # loot, then regen/eat/drink, then travel
            t += LOOT_TIME
            stats["hp_after"].append(p.hp / p.hp_max)
            stats["mana_after"].append(p.mana / p.mana_max if p.mana_max else 1.0)
            healt = mod.after_fight(p, t)
            stats["heal_time"] += healt
            t += healt
            down = self.downtime(p, t)
            stats["downtime"] += down["total"] + healt
            stats["drink_time"] += down["drink"]
            stats["eat_time"] += down["eat"]
            t += down["total"] + TRAVEL_TIME
            self.idle_regen(p, TRAVEL_TIME + LOOT_TIME + healt, t)
            p.gcd_until = 0.0
            p.rage = max(0.0, p.rage - tables.RAGE_DECAY * (TRAVEL_TIME + LOOT_TIME + down["total"]))
            p.energy = p.energy_max
            p.combo = 0
        stats["total_time"] = t
        return self.summarise(stats)

    def idle_regen(self, p, seconds, t_end):
        ticks = int(seconds / 2.0)
        for _ in range(ticks):
            if p.mana_max > 0:
                p.mana = min(p.mana_max, p.mana + self.mod.mana_regen(p, t_end) * (1.0 if t_end > p.fsr_until else p.regen_while_casting)
                             + (tables.GEAR_BONUS["mp5"] * 0.4 if "mp5" in tables.GEAR_BONUS else 0.0))
            p.hp = min(p.hp_max, p.hp + self.mod.health_regen(p))
            if p.pet is not None and p.pet.alive:
                p.pet.hp = min(p.pet.hp_max, p.pet.hp + tables.PET_OOC_REGEN * p.pet.hp_max)
                p.pet.focus = p.pet.focus_max
                p.pet.mana = min(p.pet.mana_max, p.pet.mana + p.pet.mana_regen * 4.0)

    def downtime(self, p, t):
        """Evocation if available and low, then drink/eat back to full when below the thresholds (pets are fed alongside)."""
        mod = self.mod
        total = drink = eat = 0.0
        evo = mod.evocation(p, t)
        if evo:
            total += evo
        if p.mana_max > 0 and p.mana < (mod.drink_below or DRINK_BELOW) * p.mana_max:
            drink = (p.mana_max - p.mana) / drink_rate(self.level) + SIT_DOWN
            p.mana = p.mana_max
        if p.hp < (mod.eat_below or EAT_BELOW) * p.hp_max:
            eat = (p.hp_max - p.hp) / food_rate(self.level) + SIT_DOWN
            p.hp = p.hp_max
        if p.pet is not None and p.pet.alive and p.pet.hp < tables.PET_EAT_BELOW * p.pet.hp_max:
            eat = max(eat, (p.pet.hp_max - p.pet.hp) / (tables.PET_OOC_REGEN * p.pet.hp_max / 2.0 + food_rate(self.level)) + SIT_DOWN)
            p.pet.hp = p.pet.hp_max
        if p.pet is not None and not p.pet.alive:
            total += mod.resummon_time()
            p.pet.alive, p.pet.hp, p.pet.focus, p.pet.mana = True, p.pet.hp_max, p.pet.focus_max, p.pet.mana_max
        total += max(drink, eat)   # eating and drinking happen at the same time
        return {"total": total, "drink": drink, "eat": eat}

    def summarise(self, s):
        ft = s["fight_time"]
        kills = max(1, s["kills"])
        total_dmg = sum(s["damage"].values()) or 1.0
        out = {
            "level": self.level, "kills": s["kills"], "deaths": s["deaths"], "timeouts": s["timeouts"], "pet_deaths": s["pet_deaths"],
            "fight_mean": statistics.fmean(ft) if ft else 0.0,
            "fight_median": statistics.median(ft) if ft else 0.0,
            "fight_p90": sorted(ft)[int(0.9 * len(ft))] if ft else 0.0,
            "fight_sd": statistics.pstdev(ft) if len(ft) > 1 else 0.0,
            "downtime_per_kill": s["downtime"] / kills,
            "drink_per_kill": s["drink_time"] / kills,
            "eat_per_kill": s["eat_time"] / kills,
            "heal_per_kill": s["heal_time"] / kills,
            "death_time_per_kill": s["deaths"] * DEATH_TIME / kills,
            "time_per_kill": s["total_time"] / kills,
            "kills_per_hour": 3600.0 * kills / s["total_time"] if s["total_time"] else 0.0,
            "mana_per_kill": statistics.fmean(s["mana_spent"]) if s["mana_spent"] else 0.0,
            "deaths_per_100": 100.0 * s["deaths"] / kills,
            "pet_deaths_per_100": 100.0 * s["pet_deaths"] / kills,
            "shares": {k: v / total_dmg for k, v in sorted(s["damage"].items(), key=lambda kv: -kv[1])},
            "pet_sources": sorted(s.get("pet_sources") or ()),
            "healing_per_kill": {k: v / kills for k, v in s["healing"].items()},
            "casts": s["casts"], "crits": s["crits"],
            "crit_rate": {k: s["crits"].get(k, 0) / v for k, v in s["casts"].items() if v},
            "frozen_cast_share": s["frozen_casts"] / max(1, s["spell_casts"]),
            "pushbacks_per_kill": s["pushbacks"] / kills,
            "caster_share": s["casters"] / max(1, s["kills"] + s["deaths"] + s["timeouts"]),
            "runner_share": s["runners"] / max(1, s["kills"] + s["deaths"] + s["timeouts"]),
            "mobs_per_pull": s["kills"] / max(1, s["pulls"]),
            "pulls": s["pulls"],
            "interrupts_per_kill": s["interrupts"] / kills,
            "hp_after_mean": statistics.fmean(s["hp_after"]) if s["hp_after"] else 1.0,
            "mana_after_mean": statistics.fmean(s["mana_after"]) if s["mana_after"] else 1.0,
            "fight_times": ft, "logs": s["logs"],
        }
        return out


def paired_delta(base_times, alt_times):
    """Mean difference and its standard error for two per-kill time series (paired by fight index where possible)."""
    n = min(len(base_times), len(alt_times))
    if n < 2:
        return 0.0, 0.0
    d = [alt_times[i] - base_times[i] for i in range(n)]
    mean = statistics.fmean(d)
    se = statistics.pstdev(d) / math.sqrt(n)
    return mean, se
