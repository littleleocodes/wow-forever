"""Warrior PvP layer (duellab, 2026-11-14): stances, Charge and Intercept to close, Hamstring and Piercing Howl against a foe that kites,
Pummel and Shield Bash on heals, crowd control and the casts that matter, Berserker Rage before a fear or incapacitate it can see coming,
Intimidating Shout on a cast (and the pet), Disarm against a weapon user, Retaliation against a melee foe, Death Wish and Recklessness
timed with the Mortal Strike window, Bloodrage when rage runs short, the pet hit by Sweeping Strikes, Whirlwind and Cleave, the PvP
trinket on stuns, roots and slows when kited, Shield Wall and Last Stand when low. The damage is the spec's own leveling rotation
underneath (arms-2h-raid: Mortal Strike, Overpower, Execute, Slam, Spearing Strike, Heroic Strike; fury-dw-raid the same with
Bloodthirst and two weapons; prot-leveling: Shield Slam, Revenge, Shield Block, sword and board), with its rage spent on what matters
in a duel.

Stances (the engine has none; the fight-lab module keeps `stance` and refuses a spell its stance does not allow, STANCES from the
spellbook's "Requires ... Stance"): this layer moves between them off the global cooldown with a 1 s stance cooldown, keeping only the
rage Tactical Mastery retains (10 plus Improved Tactical Mastery's 5 a rank: the module's _set_stance). Battle Stance: Charge, Overpower,
Hamstring, Rend, Retaliation, Sweeping Strikes, Spearing Strike, Mocking Blow. Berserker Stance (+3% critical strike chance, +10% damage
taken: Forever's tooltip): Intercept, Pummel, Berserker Rage, Whirlwind, Hamstring, Execute, Recklessness. Defensive Stance (-10% damage
taken and dealt: the module applies it to the Protection playstyle, this layer to the others): Disarm, Shield Wall, Revenge, Shield Block.
The home stance is Battle (Overpower on the foe's dodges, Hamstring, Retaliation, no extra damage taken); Protection lives in Defensive
(the module's own). A swap happens when an ability needs it (Pummel, Intercept and Berserker Rage in the same step, the swap being off
the global cooldown), and back home when the rage kept on the way loses little.

Effects the fight lab does not parse, or parses for PvE only (handlers below):
- Intercept: a charge from 8-25 yards (not while rooted), 65 damage and a 3 s stun (controlled-stun diminishing returns, physical), its
  cooldown less Improved Intercept's 5 s a rank. Charge is the module's (15 rage, 1 s stun), only before the duel's first hostile hit.
- Hamstring: the module's 50% slow for 15 s plus Improved Hamstring's 5% a rank to root 5 s (random_root diminishing returns; the
  fight lab leaves the talent unused). Piercing Howl: a 50% daze for 6 s within 10 yards (no diminishing returns).
- Berserker Rage: 10 s immune to fear and to incapacitates (Sap, Gouge, Repentance: Forever's "Fear and Incapacitate effects"; the 11-13
  hotfix "breaks Sap"), +5 rage a hit taken (the module), Improved Berserker Rage's 5/10 rage and 50/100% chance to remove movement
  impairing effects, Gore Drinker. Not usable while feared (no "removes" in its tooltip): it is cast before.
- Death Wish (+20% physical damage, +5% damage taken, fear immunity, 30 s) and Recklessness (+100% critical strike chance, fear
  immunity, +20% damage taken, 15 s) are this layer's (the module casts Death Wish at the pull; the countdown gives it back).
- Disarm (Defensive Stance): a 10 s disarm after a weapon attack roll, its cooldown less Improved Disarm's. Intimidating Shout: an 8 s
  fear on the foe within 10 yards and on its pet (the pet's control by the engine's pet_cc). Shield Bash: the module's interrupt plus
  Improved Shield Bash's 3 s silence (50% a rank). Shield Wall: -60% damage taken for 12 s (Improved Shield Wall: -5.5 min a rank).
  Last Stand: +30% maximum health for 20 s, lost after it.
- Retaliation (Battle Stance): for 15 s every melee hit taken from the front (the warrior not stunned, incapacitated or feared) is
  answered with a weapon attack at the attacker (the pet included), at most 30; resolved after the step. A bleed's tick is no strike
  (Garrote's ticks had been answered until 2026-11-14).
- Bloodthirst's +10% run speed for 10 s (Forever's tooltip; the module omits it). Iron Will: stun and fear durations -3% a rank.
- Overpower: a miss and crit roll only ("cannot be blocked, dodged or parried", its tooltip; the fight lab rolls the full table).
- Whirlwind (Berserker Stance; the module's single-target play never leaves Battle Stance, so it never had it): the Fury build's strike
  after Bloodthirst in Berserker Stance, and any build's when a pet stands in reach. Cleave in Heroic Strike's place with a pet in reach;
  Sweeping Strikes (off the global cooldown) with one in reach.

Decisions:
- Rage (Forever's normalized rage: about 15 a landed two-hander swing, little from damage taken, so the warrior is short of it):
  Mortal Strike (Bloodthirst, Shield Slam) is kept in reach. An optional spend (Heroic Strike, Slam, Spearing Strike, Rend, Battle Shout,
  Hamstring against a foe that is not kiting, Piercing Howl, Whirlwind, Sweeping Strikes) must leave the main strike its rage when it
  comes ready, the white-swing rage until then counted (rage_rate); interrupts, Overpower and Execute are not held back. Battle Shout
  and Rend (the rotation's, which puts Battle Shout first) only with SPARE_RAGE and never with the main strike due; Shield Block only
  against a melee foe. Bloodrage (off the global cooldown) when the rage falls short; above DUMP_RAGE, Heroic Strike (Cleave with a pet
  in reach) is queued off the global cooldown beside the next ability.
- Closing: Charge at the start; Intercept on a foe 8-25 yards away that casts, or that is not walking in (a caster, a hunter, a melee
  kiting), the stance swap in the same step; Hamstring kept on a foe that kites (or a mage or ranged hunter, whose layers kite a melee),
  Piercing Howl on one 5-10 yards away. The trinket on a root (a reaction time after it lands, the foe 8+ yards away) or on a 45%+ slow
  that keeps the warrior from catching a foe walking away, Improved Berserker Rage first when it is ready.
- Stuns: the trinket at once on a stun that covers the foe's heal, on one with STUN_TRINKET s or more left while the foe is free to hit,
  else the base rule (health low).
- Interrupts: Pummel (Berserker Stance) or Shield Bash (a shield) on heals, crowd control, channels and casts of 1.5 s or more;
  Concussion Blow (off the global cooldown) and Intercept on such casts too, Intimidating Shout on a heal or control cast within 10 yards.
- Berserker Rage: before a ready Psychic Scream, Howl of Terror or Death Coil (on a melee within 8 yards, the warlock layer's rule) or
  a paladin's Repentance once it is below 55% health (its heal window), each at its reach plus a second of closing; on a Fear cast seen;
  before a Sap from stealth (STEALTH_ZERKER); to break a snare (Improved Berserker Rage 2/2) or for rage (Improved Berserker Rage)
  against a foe without fear or incapacitate.
- Death Wish on the first melee contact (against a fear class at once, as an immunity); Recklessness with the main strike ready and the
  rage for it once the foe is below RECKLESS_BELOW, or against a fear class when no other fear immunity runs; Disarm on a melee weapon
  foe (not a druid in form) with the rage after the swap and the main strike not due; Retaliation against a melee weapon foe in reach
  below RETALIATE_BELOW health once no Disarm is coming (the two would overlap); Intimidating Shout on a hunter and its pet together;
  Overpower's window opened in another stance is a swap to Battle Stance. Shield Wall below WALL_AT, Last Stand below LAST_STAND_AT.

Switches measured (2026-11-14, 200 duels a matchup, common random numbers; arms-pvp, fury-pvp): kept: the long-stun trinket (arms
against pvp-hemo-prep 54.5% -> 79.5%), Retaliation (53% -> 79.5%; against enhancement-pvp 27% -> 65%), Berserker Rage against a Sap
(67.5% -> 79.5%), the slow trinket (against pvp-soul-link 42% -> 52%). Rejected: Berserker Stance as the home stance (no better
anywhere), holding Death Wish and Recklessness while a paladin's Divine Shield is ready (arms against retribution-pvp 4.5% -> 1.0%).
The rage dump measured neutral.

Not modelled: Thunder Clap and Demoralizing Shout (their attack-speed and attack-power cuts have no hook on a player), Mocking Blow and
Taunt (no effect on a player), Sunder Armor, Victory Rush (no kill before the duel ends: the module only grants it on a kill), Shield
Slam's dispel, the off hand's share of Whirlwind, rage refunds on a dodged ability, line of sight. Bloodrage at the pull is the
module's (taken in the countdown; its combat flag is assumed gone by the start, so Charge works). Intimidating Shout's target cowers
in Classic; here it is the engine's fear (it runs). Attacks into an immunity still give the engine's white-swing rage.
Assumptions: RESERVE_FOR, SPARE_RAGE and the thresholds below are judgment, not measured, unless the list above says so.
"""
import copy
import sys

import duel  # noqa: F401  (puts the fight lab first on sys.path: engine and tables are its copies)
import dtables as T
import engine as FE
import tables as FT
from pvp_base import PvPAI, HEALS

EPS = 1e-9

# ---- tooltip numbers
DEATH_WISH_SECS = 30.0
RECKLESS_SECS, RECKLESS_CRIT, RECKLESS_TAKEN = 15.0, 1.00, 0.20
BERSERKER_CRIT, BERSERKER_TAKEN = 0.03, 0.10     # Berserker Stance: "Critical strike chance increased by 3% and all damage taken is increased by 10%"
DEFENSIVE = 0.10                                 # Defensive Stance: -10% damage taken and dealt
SHIELD_WALL_SECS, SHIELD_WALL_CUT = 12.0, 0.60
LAST_STAND_SECS, LAST_STAND_SHARE = 20.0, 0.30
RETALIATION_SECS, RETALIATION_HITS = 15.0, 30
ZERKER_SECS = 10.0
BLOODTHIRST_SPEED, BLOODTHIRST_SECS = 0.10, 10.0
HOWL_YARDS, HOWL_SLOW, HOWL_SECS = 10.0, 0.50, 6.0
SHOUT_YARDS, SHOUT_SECS = 10.0, 8.0
IMP_HAMSTRING_ROOT = 5.0
SHIELD_BASH_SILENCE = 3.0

# ---- decisions (judgment, not measured)
RESERVE_FOR = 1.5           # Mortal Strike or Bloodthirst ready within this: keep its rage
SPARE_RAGE = 55.0           # Battle Shout and Rend only above this
RECKLESS_BELOW = 0.55       # Recklessness once the foe is below this share of health
RETALIATE_BELOW = 0.85      # Retaliation once below this share of health with a melee weapon foe in reach
WALL_AT = 0.35
LAST_STAND_AT = 0.25
BLOODRAGE_HP = 0.40
STUN_TRINKET = 4.0          # a stun with this much left while the foe is free to hit: the trinket at once
DUMP_RAGE = 80.0            # Heroic Strike (Cleave with a pet in reach) queued off the global cooldown above this rage
STEALTH_ZERKER = True       # Berserker Rage against a Sap from stealth (switches measured 2026-11-14, see the docstring)
SLOW_TRINKET = True         # the trinket on a slow that keeps the warrior from catching a foe walking away
HOME_BERSERKER = ()         # classes against which the home stance is Berserker (measured worse; Battle against all)

STANCE_NAMES = ("Battle Stance", "Berserker Stance", "Defensive Stance")
WEAPON_FOES = {"warrior", "rogue", "paladin", "shaman", "hunter"}     # melee weapon users Disarm matters against (a melee build)
FEAR_FOES = {"priest", "warlock", "warrior"}
HEALS_ALL = set(HEALS) | {"Riptide", "Holy Shock (heal)", "Rejuvenation", "Renew", "Penance (heal)"}
CC_CASTS = {"Polymorph", "Fear", "Seduction", "Hibernate", "Entangling Roots", "Mind Control", "Howl of Terror", "Banish", "Scare Beast"}
KNOCKOUT = {"Sap", "Gouge", "Repentance"}        # incapacitates Berserker Rage makes the warrior immune to
# the foe's fears and incapacitates Berserker Rage answers, with their reach in yards (the foe layer's ranges first)
ZERKER_THREATS = {"Psychic Scream": 8.0, "Howl of Terror": 10.0, "Intimidating Shout": 10.0, "Repentance": 20.0, "Gouge": 5.5,
                  "Death Coil": 30.0, "Sap": 10.0}
SELF_SPELLS = ("Berserker Rage", "Death Wish", "Recklessness", "Retaliation", "Shield Wall", "Last Stand", "Bloodrage", "Sweeping Strikes",
               "Battle Shout", "Piercing Howl", "Intimidating Shout")
SHIELD_SPELLS = ("Shield Bash", "Shield Block", "Shield Wall", "Shield Slam", "Revenge")
LAYER_SPELLS = {"Berserker Rage", "Death Wish", "Recklessness", "Retaliation", "Shield Wall", "Last Stand", "Concussion Blow", "Charge",
                "Intercept", "Sweeping Strikes", "Disarm", "Intimidating Shout", "Piercing Howl", "Hamstring", "Pummel", "Shield Bash",
                "Mocking Blow", "Thunder Clap", "Demoralizing Shout", "Taunt", "Challenging Shout", "Whirlwind", "Cleave"}


def dr_factor(side, cat, t):
    """The share of its duration the next control of this diminishing-returns category would last on `side` (1, 0.5, 0.25, 0)."""
    if not cat:
        return 1.0
    rec = side.dr.get(cat)
    n = rec[0] if rec and t < rec[1] + T.DR_RESET else 0
    return T.DR_STEPS[min(n, len(T.DR_STEPS) - 1)]


class WarriorPvP(PvPAI):
    keep_range = 0.0
    auto_attack = True
    charges = {"Charge", "Intercept"}

    # ------------------------------------------------------------------ set-up
    def bind(self, d, me):
        super().bind(d, me)
        mod = me.mod
        sp = mod.spells
        self.fw = sys.modules[type(mod).__module__]
        self.prot = bool(getattr(mod, "prot", False))
        self.shield = me.p.block > 0
        if not self.shield:
            for n in SHIELD_SPELLS:
                sp.pop(n, None)
        for name in SELF_SPELLS:   # cast on yourself: no target, no range (each one this layer's handler or the module's)
            s = sp.get(name)
            if s is not None:
                c = copy.copy(s)
                c.target, c.kind = "self", "buff"
                sp[name] = c
        for name, talent in (("Intercept", "Improved Intercept"), ("Disarm", "Improved Disarm")):
            s = sp.get(name)
            if s is not None and mod.rank(talent):
                c = copy.copy(s)
                c.cooldown = max(0.0, s.cooldown - mod.tv(talent, 0))
                sp[name] = c
        s = sp.get("Shield Wall")
        if s is not None and mod.rank("Improved Shield Wall"):
            c = copy.copy(s)
            c.cooldown = max(0.0, s.cooldown - 60.0 * mod.tv("Improved Shield Wall", 0))
            sp["Shield Wall"] = c
        self.ranges = {"Intimidating Shout": SHOUT_YARDS, "Piercing Howl": HOWL_YARDS}
        self.retain = mod._retain()
        self.home = "Defensive Stance" if self.prot else "Battle Stance"
        self.iron_will = mod.tv("Iron Will", 0) / 100
        # state
        self._t = -1.0
        self.gcd_before = 0.0
        self.zerker_until = 0.0
        self.reckless_until = 0.0
        self.wall_until = 0.0
        self.stand = None             # (bonus health, until): Last Stand
        self.retaliation = None       # [hits left, until]
        self.counters = []            # queued Retaliation strikes: "player" or "pet"
        self.control_since = None
        self.last_kite = -99.0        # when the foe last walked away
        for k in ("intercepts", "pummels", "zerkers", "disarms", "hamstrings", "swaps", "retaliations"):
            me.stats.setdefault(k, 0)
        self._wrap(me)

    def _wrap(self, me):
        """Instance-level wrappers on this side's own module and side: stance and cooldown modifiers, Bloodthirst's speed, Iron Will,
        Retaliation's trigger."""
        mod, ai = me.mod, self
        prot = self.prot
        base_dm, base_pm, base_split, base_crit, base_hit = (mod.damage_multiplier, mod.periodic_multiplier, mod.split_damage_taken,
                                                             mod.crit_bonus, mod.on_hit)

        def damage_multiplier(spell, frozen):
            m = base_dm(spell, frozen)
            if not prot and mod.stance == "Defensive Stance":
                m *= 1 - DEFENSIVE
            return m

        def periodic_multiplier(spell):
            m = base_pm(spell)
            if not prot and mod.stance == "Defensive Stance":
                m *= 1 - DEFENSIVE
            return m

        def split_damage_taken(fight, dmg):
            dmg = base_split(fight, dmg)
            t = me.t
            if not prot and mod.stance == "Defensive Stance":
                dmg *= 1 - DEFENSIVE
            if mod.stance == "Berserker Stance":
                dmg *= 1 + BERSERKER_TAKEN
            if t < ai.reckless_until:
                dmg *= 1 + RECKLESS_TAKEN
            if t < ai.wall_until:
                dmg *= 1 - SHIELD_WALL_CUT
            return dmg

        def crit_bonus(spell, frozen):
            c = base_crit(spell, frozen)
            if c <= -0.5 or spell.kind != "melee":
                return c
            if mod.stance == "Berserker Stance":
                c += BERSERKER_CRIT
            if me.t < ai.reckless_until:
                c += RECKLESS_CRIT
            return c

        def on_hit(fight, spell, amount, crit, frozen):
            base_hit(fight, spell, amount, crit, frozen)
            if spell.name == "Bloodthirst" and amount > 0:
                me.speed_bonus["Bloodthirst"] = (BLOODTHIRST_SPEED, fight.t + BLOODTHIRST_SECS)

        mod.damage_multiplier, mod.periodic_multiplier, mod.split_damage_taken = damage_multiplier, periodic_multiplier, split_damage_taken
        mod.crit_bonus, mod.on_hit = crit_bonus, on_hit
        apply_cc = me.apply_cc

        def cc(kind, dur, cat, name, frozen=False, breaks=None, physical=False):
            """Iron Will shortens stuns and fears."""
            if kind in ("stun", "fear") and ai.iron_will:
                dur *= 1 - ai.iron_will
            return apply_cc(kind, dur, cat, name, frozen=frozen, breaks=breaks, physical=physical)
        me.apply_cc = cc

    def effects_for(self, me):
        return {"Intercept": self.e_intercept, "Hamstring": self.e_hamstring, "Piercing Howl": self.e_howl, "Berserker Rage": self.e_zerker,
                "Death Wish": self.e_death_wish, "Recklessness": self.e_reckless, "Disarm": self.e_disarm,
                "Intimidating Shout": self.e_shout, "Shield Bash": self.e_shield_bash, "Shield Wall": self.e_wall, "Last Stand": self.e_stand,
                "Retaliation": self.e_retaliation, "Bloodrage": self.e_bloodrage, "Overpower": self.e_overpower}

    def prefight(self, d, me, foe):
        """The countdown: the module's pull spent Death Wish (given back: this layer times it); its Bloodrage stays (taken in the
        countdown). The home stance for this foe."""
        p, t = me.p, d.t
        if p.buffs.pop("Death Wish", None) is not None:
            p.cooldowns["Death Wish"] = t
            p.rage = min(p.rage_max, p.rage + me.mod.mana_cost(me.mod.spells["Death Wish"]))
            me.fight.casts["Death Wish"] = max(0, me.fight.casts.get("Death Wish", 1) - 1)
        if not self.prot:
            self.home = "Berserker Stance" if foe.cls in HOME_BERSERKER else "Battle Stance"   # swaps are instant when needed

    # ------------------------------------------------------------------ stances
    def stances_for(self, name):
        need = self.fw.STANCES.get(name)
        if not need:
            return None
        need = set(need)
        if name == "Charge" and self.me.mod.rank("Vanguard"):
            need.add("Defensive Stance")
        return need

    def stance_cd(self, me, t):
        return me.p.cooldowns.get("Stance", -1.0) > t

    def swap(self, d, me, stance):
        """Change stance now (off the global cooldown; the module keeps the rage Tactical Mastery retains)."""
        if me.mod.stance == stance:
            return True
        if stance not in me.mod.spells or self.stance_cd(me, d.t):
            return False
        ok = me.mod._set_stance(me.fight, stance)
        if ok:
            me.stats["swaps"] += 1
        return ok

    def ready_in(self, d, me, name, ignore_gcd=False):
        """The stance `name` can be used in now: the current one, or one a swap reaches with the rage it keeps; None when it cannot."""
        s = me.mod.spells.get(name)
        if s is None:
            return None
        need = self.stances_for(name)
        if not need or me.mod.stance in need:
            return me.mod.stance if me.can(name, ignore_gcd=ignore_gcd) else None
        if self.stance_cd(me, d.t):
            return None
        target = self.home if self.home in need else next(n for n in STANCE_NAMES if n in need)
        if target not in me.mod.spells:
            return None
        if min(me.p.rage, self.retain) < me.mod.mana_cost(s):
            return None
        return target if me.can(name, ignore_gcd=ignore_gcd) else None

    def use(self, d, me, name, ignore_gcd=False):
        """Swap to the stance `name` needs (if any) and return it to cast; None when it cannot be used now."""
        stance = self.ready_in(d, me, name, ignore_gcd)
        if stance is None:
            return None
        if stance != me.mod.stance and not self.swap(d, me, stance):
            return None
        return name

    def cast_free(self, me, name):
        """An off-global-cooldown ability now, the running global cooldown kept."""
        self.gcd_before = me.p.gcd_until
        ok = me.cast(name)
        me.p.gcd_until = max(me.p.gcd_until, self.gcd_before)
        return ok

    def use_free(self, d, me, name):
        if self.use(d, me, name, ignore_gcd=True) is None:
            return False
        return self.cast_free(me, name)

    # ------------------------------------------------------------------ effects
    def e_intercept(self, d, me, foe, spell):
        me.p.gcd_until = max(me.p.gcd_until, self.gcd_before)
        d.set_dist(T.MELEE)
        me.p.swing_mh = d.t
        me.stats["intercepts"] += 1
        return FE.Fight.resolve_spell(me.fight, spell)

    def e_hamstring(self, d, me, foe, spell):
        t = d.t
        immune = foe.immune(t) or t < foe.immune_phys_until
        amount = FE.Fight.resolve_spell(me.fight, spell)
        me.stats["hamstrings"] += 1
        if amount > 0 and not immune and me.mod.rank("Improved Hamstring") \
                and me.fight.rng.random() < me.mod.tv("Improved Hamstring", 0) / 100:
            foe.apply_cc("root", IMP_HAMSTRING_ROOT, T.DR_CATEGORY.get("Improved Hamstring", "random_root"), "Improved Hamstring",
                         physical=True)
        return amount

    def e_howl(self, d, me, foe, spell):
        t = d.t
        if d.dist <= HOWL_YARDS + 0.5 and not foe.immune(t):
            if t >= foe.slow_until or foe.slow <= HOWL_SLOW:
                foe.slow = HOWL_SLOW
            foe.slow_until = max(foe.slow_until, t + HOWL_SECS)
            me.fight.note(f"Piercing Howl: {HOWL_SLOW:.0%} 6s")
        return 0.0

    def e_zerker(self, d, me, foe, spell):
        t, p, mod = d.t, me.p, me.mod
        self.zerker_until = t + ZERKER_SECS
        me.fear_immune_until = max(me.fear_immune_until, t + ZERKER_SECS)
        p.buffs["Berserker Rage"] = {"until": t + ZERKER_SECS}   # the module's +5 rage a hit taken
        if mod.rank("Improved Berserker Rage"):
            p.rage = min(p.rage_max, p.rage + mod.tv("Improved Berserker Rage", 0))
            if me.fight.rng.random() < mod.tv("Improved Berserker Rage", 1) / 100:
                me.root_until, me.slow_until = min(me.root_until, t), min(me.slow_until, t)
                me.zone_slows.clear()
        mod._gore()
        me.stats["zerkers"] += 1
        me.fight.note("Berserker Rage")
        return 0.0

    def e_death_wish(self, d, me, foe, spell):
        t = d.t
        me.p.buffs["Death Wish"] = {"until": t + (me.mod.tv("Death Wish", 2) or DEATH_WISH_SECS)}
        me.fear_immune_until = max(me.fear_immune_until, t + DEATH_WISH_SECS)
        me.mod._gore()
        me.fight.note("Death Wish")
        return 0.0

    def e_reckless(self, d, me, foe, spell):
        t = d.t
        self.reckless_until = t + RECKLESS_SECS
        me.fear_immune_until = max(me.fear_immune_until, t + RECKLESS_SECS)
        me.fight.note("Recklessness")
        return 0.0

    def e_disarm(self, d, me, foe, spell):
        out = me.fight.attack_table(spell, False)
        if out in ("miss", "dodge", "parry"):
            me.fight.note(f"Disarm {out.upper()}")
            return 0.0
        if foe.apply_cc("disarm", 10.0, "disarm", "Disarm", physical=True) > 0:
            me.stats["disarms"] += 1
        return 0.0

    def e_shout(self, d, me, foe, spell):
        t = d.t
        if d.dist <= SHOUT_YARDS + 0.5:
            foe.apply_cc("fear", SHOUT_SECS, T.DR_CATEGORY.get("Intimidating Shout", "fear"), "Intimidating Shout")
        if foe.pet_body.alive():
            d.pet_cc(foe, "fear", SHOUT_SECS)
        return 0.0

    def e_shield_bash(self, d, me, foe, spell):
        amount = FE.Fight.resolve_spell(me.fight, spell)
        if amount > 0 and me.mod.rank("Improved Shield Bash") and me.fight.rng.random() < me.mod.tv("Improved Shield Bash", 0) / 100:
            foe.apply_cc("silence", SHIELD_BASH_SILENCE, None, "Improved Shield Bash")
        me.stats["pummels"] += 1
        return amount

    def e_wall(self, d, me, foe, spell):
        self.wall_until = d.t + SHIELD_WALL_SECS
        me.fight.note("Shield Wall")
        return 0.0

    def e_stand(self, d, me, foe, spell):
        me.p.gcd_until = max(me.p.gcd_until, self.gcd_before)
        bonus = LAST_STAND_SHARE * me.p.hp_max
        me.p.hp_max += bonus
        me.p.hp += bonus
        self.stand = (bonus, d.t + LAST_STAND_SECS)
        me.fight.note(f"Last Stand (+{bonus:.0f})")
        return 0.0

    def e_overpower(self, d, me, foe, spell):
        """Overpower "cannot be blocked, dodged or parried" (its tooltip; the fight lab rolls the whole attack table): a miss and crit
        roll only."""
        f = me.fight

        def table(sp, white, hand="mh"):
            p = f.p
            r = f.rng.random()
            miss = max(0.0, FT.MELEE_MISS - p.hit_bonus - me.mod.hit_bonus(sp))
            if r < miss:
                return "miss"
            r -= miss
            return "crit" if r < p.melee_crit + me.mod.crit_bonus(sp, False) else "hit"

        f.attack_table = table
        try:
            return FE.Fight.resolve_spell(f, spell)
        finally:
            del f.attack_table

    def e_bloodrage(self, d, me, foe, spell):
        """The module's pull Bloodrage in the duel (its on_fight_start only): 10 rage now and 10 over 10 s (Improved Bloodrage +25% a
        rank), 6% of maximum health (the module's cost), Gore Drinker."""
        p, t, mod = me.p, d.t, me.mod
        me.p.gcd_until = max(me.p.gcd_until, self.gcd_before)
        gain = 10.0 * (1 + mod.tv("Improved Bloodrage", 0) / 100)
        p.hp -= 0.06 * p.hp_max
        p.rage = min(p.rage_max, p.rage + gain)
        p.buffs["Bloodrage"] = {"until": t + 10.0, "left": gain, "per": gain / 10.0, "last": t}
        mod._gore()
        me.fight.note(f"Bloodrage: {p.rage:.0f} rage")
        return 0.0

    def e_retaliation(self, d, me, foe, spell):
        self.retaliation = [RETALIATION_HITS, d.t + RETALIATION_SECS]
        me.stats["retaliations"] += 1
        me.fight.note("Retaliation")
        return 0.0

    # ------------------------------------------------------------------ incoming damage
    def damage_taken(self, d, me, src, spell, amount):
        r = self.retaliation
        t = d.t
        if r is not None and t < r[1] and r[0] > 0 and not me.controlled(t) and spell.name != "Retaliation" and not d.periodic_hit:
            melee = getattr(spell, "kind", "") == "melee" or spell.name.endswith(" melee")
            if melee and d.dist <= T.MELEE + 0.5 or spell.name.endswith(" melee"):
                r[0] -= 1
                self.counters.append("pet" if spell.name.endswith(" melee") else "player")
        return amount

    def tick(self, d, me, foe):
        """After every step: Retaliation's strikes, Last Stand's end."""
        t = d.t
        if self.counters:
            queue, self.counters = self.counters, []
            for who in queue:
                if me.p.hp <= 0 or foe.p.hp <= 0 or me.controlled(t) or t < me.disarm_until:
                    break
                strike = FE.Spell("Retaliation", "physical", kind="melee", weapon_pct=1.0, resource="none")
                if who == "pet":
                    if not foe.pet_body.alive():
                        continue
                    f = me.fight
                    old = f.m
                    f.m = foe.pet_body
                    try:
                        f.resolve_attack(strike)
                    finally:
                        f.m = old
                elif d.dist <= T.MELEE + 0.5:
                    me.fight.resolve_attack(strike)
        if self.stand is not None and t >= self.stand[1]:
            bonus = self.stand[0]
            me.p.hp_max -= bonus
            me.p.hp = min(me.p.hp, me.p.hp_max)
            self.stand = None
            me.fight.note("Last Stand ends")
        return None

    def cc_immune(self, d, me, kind, name):
        """Berserker Rage: immune to incapacitates (Sap, Gouge, Repentance)."""
        return kind == "incap" and name in KNOCKOUT and d.t < self.zerker_until

    # ------------------------------------------------------------------ helpers
    def foe_held(self, foe, t):
        return max(foe.stun_until, foe.incap_until, foe.fear_until) - t

    def mortal_ready_in(self, me, t):
        """Seconds until the rotation's main strike (Mortal Strike, Bloodthirst, Shield Slam) is ready; 99 without one."""
        best = 99.0
        for n in ("Mortal Strike", "Bloodthirst", "Shield Slam"):
            if n in me.mod.spells:
                best = min(best, max(0.0, me.p.cooldowns.get(n, 0.0) - t))
        return best

    def main_cost(self, me):
        for n in ("Mortal Strike", "Bloodthirst", "Shield Slam"):
            s = me.mod.spells.get(n)
            if s is not None:
                return me.mod.mana_cost(s)
        return 0.0

    def rage_rate(self, me):
        """Rage a second from white swings (Forever's normalized rage per landed swing, about 85% of swings land) and Anger
        Management."""
        p, r = me.p, 0.0
        for w, hand in ((p.mh, "mh"), (p.oh, "oh")):
            if w is not None:
                r += 0.85 * me.mod.rage_from_hit(me.fight, 0.0, w, hand, False) / w.speed
        return r + (1.0 / 3.0 if me.mod.rank("Anger Management") else 0.0)

    def reserve(self, me, t):
        """Rage kept for the main strike when it is about to be ready."""
        if self.mortal_ready_in(me, t) > RESERVE_FOR:
            return 0.0
        return self.main_cost(me)

    def spare(self, me, name, t, extra=0.0):
        """Whether `name` leaves the main strike its rage when it comes ready (the rage income until then counted), plus `extra`."""
        s = me.mod.spells.get(name)
        if s is None:
            return False
        left = me.p.rage - me.mod.mana_cost(s)
        if left < extra:
            return False
        ready_in = self.mortal_ready_in(me, t)
        if ready_in >= 99.0:
            return True
        return left + self.rage_rate(me) * ready_in >= self.main_cost(me) + extra

    def ranged_foe(self, foe):
        return not self.melee_foe(foe)

    def kiting(self, d, foe):
        """The foe walks away from the warrior, now or lately, or is a class whose layer kites a melee (mage, ranged hunter)."""
        return foe.intent == "kite" or d.t - self.last_kite < 3.0 or (self.ranged_foe(foe) and foe.cls in ("mage", "hunter"))

    def foe_cast_worth(self, d, me, foe, c):
        """A foe cast worth an interrupt: a heal, crowd control, a channel, or a cast of 1.5 s or more."""
        if c.kind == "heal" or c.name in HEALS_ALL or c.name in CC_CASTS or c.kind == "channel":
            return True
        cast = foe.mod.cast_time(c) if c.kind != "channel" else c.channel
        return cast >= 1.5 and (c.dmg_max > 0 or c.dot > 0 or c.kind == "ranged")

    def fear_immune(self, me, t, margin=0.0):
        return t + margin < me.fear_immune_until or t + margin < me.immune_until

    def zerker_threat(self, d, me, foe):
        """A ready fear or incapacitate of the foe that Berserker Rage answers, that its layer would use on the warrior now (Psychic
        Scream, Howl of Terror and Death Coil on a melee in reach; Repentance for a heal window once the paladin is hurt), and that can
        reach the warrior within a second."""
        t = d.t
        ranges = getattr(foe.ai, "ranges", None) or {}
        for name, reach in ZERKER_THREATS.items():
            s = foe.mod.spells.get(name)
            if s is None or not foe.p.ready(name, t + 1.0) or name in ("Sap", "Gouge", "Intimidating Shout"):
                continue
            if name == "Repentance" and foe.hp_frac() > 0.55:
                continue
            if name == "Death Coil":
                reach = 8.0   # the warlock layer coils a free melee within 8 yards
            r = ranges.get(name) or reach
            closing = (foe.speed(t) if foe.intent == "close" else 0.0) + (me.speed(t) if me.intent == "close" else 0.0)
            if d.dist - closing * 1.0 <= r + 1.0:
                return name
        return None

    # ------------------------------------------------------------------ per step
    def track(self, d, me, foe):
        t = d.t
        if t <= self._t + EPS:
            return
        self._t = t
        if me.controlled(t):
            if self.control_since is None:
                self.control_since = t
        else:
            self.control_since = None
        if foe.intent == "kite":
            self.last_kite = t

    # ------------------------------------------------------------------ movement
    def intent(self, d, me, foe):
        self.track(d, me, foe)
        if foe.stealthed and not me.stealthed:
            return "hold"
        return "close"

    # ------------------------------------------------------------------ hooks
    def while_controlled(self, d, me, foe):
        """The trinket (stun, root, slow) on a stun: at once against one that covers a heal of the foe's, on a long one (STUN_TRINKET s
        or more left) while the foe is free to hit, and the base rule (health low)."""
        self.track(d, me, foe)
        t = d.t
        frees = me.trinket_frees(t)
        if "stun" in frees and me.trinket_clears(t) and me.stun_until - t >= 1.5 and self.control_since is not None \
                and t - self.control_since >= T.REACTION:
            c = self.foe_cast(d, foe)
            if c is not None and (c.kind == "heal" or c.name in HEALS_ALL) and foe.fight.casting and foe.cast_end() - t > 0.4:
                return "trinket"
            if me.stun_until - t >= STUN_TRINKET and not foe.controlled(t) and t >= foe.disarm_until and foe.hp_frac() > 0.15:
                return "trinket"
        return super().while_controlled(d, me, foe)

    def off_gcd(self, d, me, foe):
        """Off the global cooldown: Charge, Intercept, Concussion Blow on a cast, Last Stand, Bloodrage, Sweeping Strikes, the
        trinket when kited."""
        self.track(d, me, foe)
        t = d.t
        self.gcd_before = me.p.gcd_until
        if foe.stealthed:
            return None
        hp = me.hp_frac()
        if hp < LAST_STAND_AT and me.can("Last Stand", ignore_gcd=True):
            self.cast_free(me, "Last Stand")
        dist = d.dist
        # Charge at the start (Battle Stance; Vanguard: Defensive)
        if not d.combat and T.MIN_RANGED <= dist <= 25.0 and "Charge" in me.mod.spells and me.p.ready("Charge", t) \
                and t >= me.root_until and not foe.immune(t):
            if self.use_free(d, me, "Charge"):
                return None
        # Intercept: a cast to stop, or a foe that will not come to the warrior
        if T.MIN_RANGED <= dist <= 25.0 and t >= me.root_until and not foe.immune(t) and not (t < foe.immune_phys_until):
            c = self.foe_cast(d, foe)
            casting = c is not None and self.foe_cast_worth(d, me, foe, c)
            held = self.foe_held(foe, t) > 1.0
            coming = self.melee_foe(foe) and foe.intent == "close" and not held and dist < 14.0
            if (casting or not coming) and self.use_free(d, me, "Intercept"):
                return None
        # Concussion Blow on a cast in reach
        c = self.foe_cast(d, foe)
        if c is not None and dist <= T.MELEE + 0.5 and self.foe_cast_worth(d, me, foe, c) and not foe.immune(t) \
                and dr_factor(foe, "stun", t) >= 0.5 and me.can("Concussion Blow", ignore_gcd=True):
            self.cast_free(me, "Concussion Blow")
            return None
        # Bloodrage when the rage falls short of the main strike (or an interrupt)
        if me.can("Bloodrage", ignore_gcd=True) and hp > BLOODRAGE_HP and dist <= 25.0:
            need = self.reserve(me, t) or 30.0
            if me.p.rage < min(need, 30.0) - 5.0 or (c is not None and me.p.rage < 10.0):
                self.cast_free(me, "Bloodrage")
        # a rage dump: Heroic Strike (Cleave with a pet in reach) on the next swing, beside the global cooldown's ability
        if dist <= T.MELEE + 0.5 and me.p.rage >= DUMP_RAGE and me.fight.queued_swing is None and t >= me.disarm_until \
                and not foe.immune(t) and t >= foe.immune_phys_until:
            pet_near = foe.pet_body.alive() and foe.p.pet.engaged and not foe.p.pet.caster
            k = "Cleave" if pet_near and "Cleave" in me.mod.spells else "Heroic Strike"
            if self.spare(me, k, t, 10.0) and me.can(k, ignore_gcd=True):
                self.cast_free(me, k)
        # Sweeping Strikes with a pet in reach and rage to spare
        pb = foe.pet_body
        if pb.alive() and foe.p.pet.engaged and not foe.p.pet.caster and dist <= T.MELEE + 0.5 and "Sweeping Strikes" in me.mod.spells \
                and not me.p.buff("Sweeping Strikes", t) and self.spare(me, "Sweeping Strikes", t, 10.0) \
                and self.ready_in(d, me, "Sweeping Strikes", ignore_gcd=True):
            if self.use_free(d, me, "Sweeping Strikes"):
                me.p.buffs["Sweeping Strikes"] = {"until": t + self.fw.SWEEP_DURATION, "charges": self.fw.SWEEP_CHARGES}
        return self.kited(d, me, foe)

    def kited(self, d, me, foe):
        """Held off by a root, or by a slow that keeps the warrior from catching a foe walking away (just out of reach counts):
        Improved Berserker Rage first, else the trinket."""
        t = d.t
        if d.dist <= T.MELEE + 0.05 or foe.controlled(t) or foe.immune(t):
            return None
        rooted = t < me.root_until and me.root_until - t >= 1.5 and t >= self._root_seen(me) + T.REACTION
        slowed = t < me.slow_until and me.slow >= 0.45 and me.slow_until - t >= 2.5
        if not rooted and not slowed:
            return None
        if not (self.kiting(d, foe) or rooted and d.dist > 8.0):
            return None
        if slowed and not rooted and (me.speed(t) > foe.speed(t) * 1.15 or foe.intent != "kite"):
            return None   # it catches up anyway, or the foe stands
        if me.mod.rank("Improved Berserker Rage") >= 2 and self.ready_in(d, me, "Berserker Rage", ignore_gcd=True) \
                and me.p.gcd_until - t < 1.0:
            return None   # decide casts it (it frees the warrior of movement impairing effects)
        frees = me.trinket_frees(t)
        if rooted and "root" in frees and d.dist > 8.0:
            return "trinket"
        if slowed and "slow" in frees and SLOW_TRINKET:
            return "trinket"
        return None

    def _root_seen(self, me):
        """When the root on the warrior began (the trinket waits a reaction time)."""
        if getattr(self, "_root_until", None) != me.root_until:
            self._root_until = me.root_until
            self._root_at = me.t
        return self._root_at

    # ------------------------------------------------------------------ decisions
    def decide(self, d, me, foe):
        self.track(d, me, foe)
        self.gcd_before = me.p.gcd_until
        t = d.t
        if foe.stealthed:
            return self.stealth_guard(d, me, foe) if STEALTH_ZERKER else None
        for step in (self.emergency, self.interrupt, self.zerker, self.gap, self.cooldowns, self.disarm, self.dance, self.damage,
                     self.go_home):
            a = step(d, me, foe)
            if a is not None:
                return None if a == "wait" else a
        return None

    def stealth_guard(self, d, me, foe):
        """A rogue or druid in stealth before the duel's first hit: Berserker Rage against Sap once it can be in reach."""
        t = d.t
        if d.combat or t < 1.0 or self.fear_immune(me, t) or t < self.zerker_until:
            return None
        if "Sap" in foe.mod.spells and foe.p.ready("Sap", t):
            return self.use(d, me, "Berserker Rage")
        return None

    def emergency(self, d, me, foe):
        """Shield Wall below WALL_AT (Defensive Stance, a shield); Retaliation against a melee weapon foe in reach."""
        t = d.t
        hp = me.hp_frac()
        if hp < WALL_AT and self.shield and t >= self.wall_until and foe.hp_frac() > 0.1:
            a = self.use(d, me, "Shield Wall")
            if a:
                return a
        disarm_soon = foe.cls in WEAPON_FOES and foe.p.mh is not None and self.ready_in(d, me, "Disarm") is not None
        if self.melee_foe(foe) and d.dist <= T.MELEE + 0.5 and foe.cls in WEAPON_FOES | {"druid"} and not foe.controlled(t) \
                and t + 1.0 >= foe.disarm_until and not disarm_soon and hp < RETALIATE_BELOW and self.retaliation is None \
                and not foe.immune(t):
            a = self.use(d, me, "Retaliation")
            if a:
                return a
        return None

    def interrupt(self, d, me, foe):
        """Pummel or Shield Bash on a cast worth it; Intimidating Shout within 10 yards when they are down; Intimidating Shout on a hunter
        and its pet together."""
        t = d.t
        if foe.immune(t):
            return None
        c = self.foe_cast(d, foe)
        if c is not None and self.foe_cast_worth(d, me, foe, c) and (not foe.fight.casting or foe.cast_end() - t > 0.1):
            if d.dist <= T.MELEE + 0.5:
                for k in ("Shield Bash", "Pummel"):
                    a = self.use(d, me, k)
                    if a:
                        me.stats["pummels"] += k == "Pummel"
                        return a
            if (c.kind == "heal" or c.name in HEALS_ALL or c.name in CC_CASTS) and d.dist <= SHOUT_YARDS and t >= foe.fear_immune_until \
                    and dr_factor(foe, "fear", t) >= 0.5 and me.can("Intimidating Shout"):
                return "Intimidating Shout"
        if foe.cls == "hunter" and foe.pet_body.alive() and d.dist <= SHOUT_YARDS and not foe.controlled(t) \
                and t >= foe.fear_immune_until and dr_factor(foe, "fear", t) >= 1.0 and me.p.rage >= 25.0 + self.reserve(me, t) * 0.5 \
                and me.can("Intimidating Shout"):
            return "Intimidating Shout"
        return None

    def zerker(self, d, me, foe):
        """Berserker Rage before a fear or incapacitate that can reach the warrior, on a seen Fear cast, or for rage."""
        t = d.t
        if t < self.zerker_until or "Berserker Rage" not in me.mod.spells:
            return None
        threat = None
        if not self.fear_immune(me, t, 1.0) or t + 1.0 >= self.zerker_until:
            c = self.foe_cast(d, foe, react=0.0)
            if c is not None and c.name in ("Fear", "Howl of Terror") and not self.fear_immune(me, t, foe.cast_end() - t if foe.fight.casting else 0):
                threat = c.name
            elif not self.fear_immune(me, t, 1.5):
                threat = self.zerker_threat(d, me, foe)
                if threat in KNOCKOUT and t < self.zerker_until:
                    threat = None
        if threat is None and me.mod.rank("Improved Berserker Rage") and me.p.rage < 25.0 and foe.cls not in FEAR_FOES | {"paladin", "rogue"} \
                and d.dist <= T.MELEE + 0.5:
            threat = "rage"
        snared = (t < me.root_until and me.root_until - t > 1.0) or (t < me.slow_until and me.slow >= 0.45 and me.slow_until - t > 2.5)
        if threat is None and me.mod.rank("Improved Berserker Rage") >= 2 and snared and d.dist > T.MELEE + 0.5 and self.kiting(d, foe):
            threat = "snare"
        if threat is None:
            return None
        return self.use(d, me, "Berserker Rage")

    def gap(self, d, me, foe):
        """Hamstring on a foe that kites or plays at range, Piercing Howl on one 5-10 yards away."""
        t = d.t
        if foe.immune(t) or t < foe.immune_phys_until:
            return None
        slowed = t < foe.slow_until and foe.slow >= 0.45 and foe.slow_until - t > 3.0
        rooted = t < foe.root_until and foe.root_until - t > 1.0
        if slowed or rooted or self.foe_held(foe, t) > 1.5:
            return None
        if not (self.kiting(d, foe) or foe.hp_frac() < 0.25 or foe.cls in ("rogue", "hunter")):
            return None
        urgent = foe.intent == "kite" or (self.ranged_foe(foe) and foe.cls in ("mage", "hunter"))
        if d.dist <= T.MELEE + 0.5:
            if (urgent or self.spare(me, "Hamstring", t)) and self.use(d, me, "Hamstring"):
                return "Hamstring"
        elif d.dist <= HOWL_YARDS and (urgent or self.spare(me, "Piercing Howl", t)) and me.can("Piercing Howl"):
            return "Piercing Howl"
        return None

    def cooldowns(self, d, me, foe):
        """Death Wish on the first melee contact (at once against a fear class); Recklessness with the main strike ready and the foe
        below RECKLESS_BELOW, or against a fear class."""
        t = d.t
        if d.dist > T.MELEE + 0.5 or foe.immune(t) or t < foe.immune_phys_until:
            return None
        if "Death Wish" in me.mod.spells and me.can("Death Wish") and not me.p.buff("Death Wish", t):
            if foe.cls in FEAR_FOES or me.p.rage >= 10.0 + self.reserve(me, t) or foe.hp_frac() < 0.8:
                return "Death Wish"
        if "Recklessness" in me.mod.spells and t >= self.reckless_until and me.p.ready("Recklessness", t):
            fear = foe.cls in FEAR_FOES and not self.fear_immune(me, t, 2.0)
            burst = foe.hp_frac() < RECKLESS_BELOW and self.mortal_ready_in(me, t) < 1.0 and me.p.rage >= 30.0
            if (fear or burst) and me.hp_frac() > 0.3:
                a = self.use(d, me, "Recklessness")
                if a:
                    return a
        return None

    def disarm(self, d, me, foe):
        """Disarm (Defensive Stance) on a melee weapon foe, with the rage after the swap."""
        t = d.t
        if d.dist > T.MELEE + 0.5 or not self.melee_foe(foe) or foe.cls not in WEAPON_FOES or t < foe.disarm_until:
            return None
        if foe.immune(t) or t < foe.immune_phys_until or foe.controlled(t) or foe.p.mh is None:
            return None
        if getattr(foe.ai, "cc_immune", None) is not None and foe.ai.cc_immune(d, foe, "disarm", "Disarm"):
            return None
        if self.mortal_ready_in(me, t) < 1.0 and me.p.rage < 50.0:
            return None   # the main strike first
        return self.use(d, me, "Disarm")

    def dance(self, d, me, foe):
        """Overpower's window open outside Battle Stance: swap (the rotation casts it); Execute outside its stances likewise."""
        t = d.t
        if d.dist > T.MELEE + 0.5:
            return None
        if me.p.buff("Overpower", t) and "Overpower" in me.mod.spells and me.p.ready("Overpower", t) and me.mod.stance != "Battle Stance" \
                and not self.stance_cd(me, t) and min(me.p.rage, self.retain) >= 5.0:
            self.swap(d, me, "Battle Stance")
        if foe.hp_frac() <= 0.2 and "Execute" in me.mod.spells and not me.mod.stance_ok("Execute") and not self.stance_cd(me, t):
            self.swap(d, me, self.home if self.home != "Defensive Stance" else "Berserker Stance")
        return None

    def damage(self, d, me, foe):
        """The spec's rotation with this duel's rules: its rage kept for the main strike, Battle Shout and Rend only with rage to spare,
        Shield Block only against a melee foe, this layer's abilities kept off it; then Whirlwind in Berserker Stance (Fury, or a pet in
        reach) and Cleave in Heroic Strike's place with a pet in reach."""
        t = d.t
        if foe.immune(t) or (t < foe.immune_phys_until):
            return "wait"
        if d.dist > T.MELEE + 0.5:
            return None
        off = set(LAYER_SPELLS)
        if me.p.rage < SPARE_RAGE:
            off |= {"Battle Shout", "Rend"}
        for n in ("Heroic Strike", "Slam", "Spearing Strike", "Rend", "Battle Shout"):
            if n in me.mod.spells and not self.spare(me, n, t):
                off.add(n)
        if self.mortal_ready_in(me, t) < RESERVE_FOR:
            off.add("Battle Shout")   # the module's priority puts it first: not before the main strike
        if not self.melee_foe(foe):
            off.add("Shield Block")
        if t < me.disarm_until:
            off |= {n for n, s in me.mod.spells.items() if s.kind == "melee"}
        pet = foe.pet_body.alive() and foe.p.pet.engaged and not foe.p.pet.caster
        a = self.vetoed(me, off, lambda: self.rotation(d, me, foe))
        if a in ("advance", "retreat"):
            a = None
        name = a.name if hasattr(a, "name") else a
        if name == "Heroic Strike" and pet and me.can("Cleave"):
            return "Cleave"
        if a is None or name in ("Heroic Strike", "Slam"):
            ww = self.whirlwind(d, me, foe, pet)
            if ww:
                return ww
        return a

    def whirlwind(self, d, me, foe, pet):
        t = d.t
        if "Whirlwind" not in me.mod.spells or me.mod.stance != "Berserker Stance":
            return None
        if not (pet or me.p.oh is not None):
            return None
        if self.spare(me, "Whirlwind", t) and me.can("Whirlwind"):
            return "Whirlwind"
        return None

    def go_home(self, d, me, foe):
        """Back to the home stance when the rage kept on the way loses little."""
        t = d.t
        if self.prot or me.mod.stance == self.home or self.stance_cd(me, t):
            return None
        if me.p.buff("Overpower", t) and me.mod.stance == "Battle Stance":
            return None
        if me.p.rage <= self.retain + 5.0:
            self.swap(d, me, self.home)
        return None

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
