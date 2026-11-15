"""Duel lab: level-60 one-against-one PvP duels between two talent builds (2026-11-14, user: "do full research on WoW Forever PvP
builds and build whatever is necessary").

No community simulator plays PvP, so this is the project's own model, built on the fight lab. Each side is a fight-lab class module
(its spells at their level-60 ranks, its talent numbers and mechanics: Shatter, Fingers of Frost, Seal Fate, rage, energy, pets) and
a fight-lab `Fight` of its own (`SideFight`) whose target is the other player seen through `Body`, a mob-shaped view (health, armor,
distance, slows, roots, stuns, fears, debuffs, dots, casting). Every talent hook therefore works as in the fight lab; what is new is
the player-versus-player layer here:

- attack tables against a player: no glancing blows, the defender's own dodge, parry and block (none while it is stunned or
  incapacitated, and no parry or block from behind); spell hit and crit as against a same-level target;
- crowd control on players: diminishing returns per category (dtables.DR_CATEGORY), the PvP duration cap, immunities (Ice Block,
  Divine Shield, Blessing of Protection against physical attacks, Berserker Rage against fear), control broken by damage
  (Polymorph, Sap, Gouge, Blind, Seduction; fear and Frost Nova's root by chance), the PvP trinket, interrupts that lock the spell
  school, silences, cast pushback, healing reduction (Mortal Strike, Wound Poison);
- movement on a line: one distance, run speeds, slows, roots; a caster stands still to cast; charges and blinks;
- decisions (pvp_base.PvPAI and pvp_<class>.py): each class's PvP layer (openers, control, interrupts, defensive cooldowns, kiting,
  healing) on top of its spec's own tuned leveling rotation, which fills every moment the PvP layer leaves (the fight lab's
  `decide`, with the opponent as the mob: "each spec plays its own rotation").

A model of stated assumptions (open field, no line of sight, no consumables, no racials, both sides in the fight lab's level-60 gear
tier dtables.GEAR_TIER), never a measurement of the game. `duel_run.py` runs duels, matchups and talent values.
"""
import importlib.util
import pathlib
import random
import sys

HERE = pathlib.Path(__file__).resolve().parent
FL = HERE.parent / "fightlab"
for _p in (str(FL), str(HERE)):
    if _p not in sys.path:
        sys.path.insert(0, _p)


def _fightlab(name):
    """A fight-lab module by its file, under the name fl_<name>. The fight lab's run.py puts the scorer's folder first on sys.path
    when it is imported, so in a process spawned after that (a worker inherits the path) `import run` finds the scorer's run.py
    (2026-11-14); `engine` and `tables` are found in the fight lab's folder, put first here before the load."""
    key = f"fl_{name}"
    if key not in sys.modules:
        if str(FL) in sys.path:
            sys.path.remove(str(FL))
        sys.path.insert(0, str(FL))
        spec = importlib.util.spec_from_file_location(key, FL / f"{name}.py")
        mod = importlib.util.module_from_spec(spec)
        sys.modules[key] = mod
        spec.loader.exec_module(mod)
    return sys.modules[key]


import dtables as T  # noqa: E402
if str(FL) in sys.path:
    sys.path.remove(str(FL))
sys.path.insert(0, str(FL))
import engine as FE  # noqa: E402   (one copy, shared with the class modules: they import it by this name)
import tables as FT  # noqa: E402
assert pathlib.Path(FE.__file__).parent == FL and pathlib.Path(FT.__file__).parent == FL, (FE.__file__, FT.__file__)
FR = _fightlab("run")   # the only clashing name: the scorer also has a run.py

EPS = 1e-9
FROZEN_ROOTS = {"Frost Nova", "Frostbite", "Freeze"}          # roots that count as Frozen for Shatter and Ice Lance
KEEPS_STEALTH = {"Stealth", "Prowl", "Sap", "Distract", "Pick Pocket", "Vanish"}
_GEAR = {"tier": None}


def set_gear(tier):
    """Both sides' gear: the fight lab's level tables for `tier` (greens / blues), set once per process."""
    if _GEAR["tier"] != tier:
        FR.apply_gear(tier)
        _GEAR["tier"] = tier


class Body:
    """A side as the other side's module sees it: the mob-shaped view the fight lab's hooks read and write. Health, armor, distance,
    slows, roots, stuns, fears, debuffs and dots are the side's own live state; control set through it gets diminishing returns."""
    _plain = dict(level=60, swing_at=0.0, target="player", threat_player=0.0, threat_pet=0.0, pet_in_melee=False, caster=False,
                  runner=False, fled=False, flee_until=-1.0, cast_dmg=0.0, cast_next=0.0, dmg=0.0)

    def __init__(self, side):
        self.__dict__["side"] = side
        self.__dict__.update(self._plain)

    hp = property(lambda s: s.side.p.hp, lambda s, v: setattr(s.side.p, "hp", v))
    hp_max = property(lambda s: s.side.p.hp_max, lambda s, v: None)
    armor = property(lambda s: s.side.armor(), lambda s, v: None)
    dist = property(lambda s: s.side.duel.dist, lambda s, v: s.side.duel.set_dist(v))
    in_melee = property(lambda s: s.side.duel.dist <= T.MELEE + 1e-6, lambda s, v: None)
    slow = property(lambda s: s.side.slow, lambda s, v: setattr(s.side, "slow", v))
    slow_until = property(lambda s: s.side.slow_until, lambda s, v: setattr(s.side, "slow_until", v))
    root_until = property(lambda s: s.side.root_until, lambda s, v: s.side.set_control("root", v))
    stun_until = property(lambda s: s.side.stun_until, lambda s, v: s.side.set_control("stun", v))
    fear_until = property(lambda s: s.side.fear_until, lambda s, v: s.side.set_control("fear", v))
    attack_slow = property(lambda s: s.side.attack_slow, lambda s, v: setattr(s.side, "attack_slow", v))
    attack_slow_until = property(lambda s: s.side.attack_slow_until, lambda s, v: setattr(s.side, "attack_slow_until", v))
    debuffs = property(lambda s: s.side.debuffs, lambda s, v: setattr(s.side, "debuffs", v))
    dots = property(lambda s: s.side.dots, lambda s, v: setattr(s.side, "dots", v))
    armor_debuff = property(lambda s: s.side.armor_debuff, lambda s, v: setattr(s.side, "armor_debuff", v))
    dmg_reduction = property(lambda s: s.side.dmg_reduction, lambda s, v: setattr(s.side, "dmg_reduction", v))
    dmg_reduction_until = property(lambda s: s.side.dmg_reduction_until, lambda s, v: setattr(s.side, "dmg_reduction_until", v))
    cast_end = property(lambda s: s.side.cast_end(), lambda s, v: s.side.break_cast("broken") if v < 0 else None)
    lockout_until = property(lambda s: s.side.lockout_all, lambda s, v: setattr(s.side, "lockout_all", max(s.side.lockout_all, v)))

    def casting(self, t):
        return self.side.is_casting()

    def can_cast(self, t):
        return not self.side.silenced(t) and not self.side.controlled(t)

    def stunned(self, t):
        return t < self.side.stun_until

    def rooted(self, t):
        return t < self.side.root_until

    def feared(self, t):
        return t < self.side.fear_until

    def frozen(self, t):
        return t < self.side.root_until and self.side.root_frozen

    def fleeing(self, t):
        return False

    def incapacitated(self, t):
        return self.stunned(t) or self.feared(t) or t < self.side.incap_until

    def speed(self, t):
        return self.side.speed(t)

    def effective_armor(self):
        return max(0.0, self.armor - self.armor_debuff)


class SideFight(FE.Fight):
    """One side's fight-lab Fight: its module, its player, the other side as the target. Damage goes through the duel (immunities,
    absorbs, control broken by damage, pushback, rage), the attack table is a player's, control gets diminishing returns."""

    def __init__(self, side, log):
        self.side = side
        self._blocked = False
        super().__init__(side.mod, side.p, side.foe.body, side.duel.rng, t0=0.0, log=log, extra=None)

    def note(self, msg):
        if self.log is not None and "-> mob" not in msg and "-> add" not in msg:
            self.log.append(f"{self.side.duel.t:6.2f}s {self.side.name} {msg}")

    def deal(self, spell, amount, crit=False, source="player"):
        if self._blocked:
            self._blocked = False
            amount = max(0.0, amount - self.side.foe.p.block_value)
        self.side.duel.damage(self.side, self.side.foe, spell, amount, crit, source)

    def heal(self, spell, amount, target="player", crit=False):
        if target != "pet":
            amount *= 1.0 - self.side.heal_reduction()
        return super().heal(spell, amount, target, crit)

    def attack_table(self, spell, white, hand="mh"):
        p, foe = self.p, self.side.foe
        fp, t = foe.p, self.side.duel.t
        r = self.rng.random()
        if spell.kind == "ranged":
            miss = max(0.0, FT.RANGED_MISS - p.hit_bonus - self.mod.hit_bonus(spell))
            if r < miss:
                return "miss"
            r -= miss
            crit = p.ranged_crit + self.mod.crit_bonus(spell, False)
            return "crit" if r < crit else "hit"
        miss = max(0.0, FT.MELEE_MISS + (FT.DW_MISS_PENALTY if (white and p.dual_wield) else 0.0) - p.hit_bonus - self.mod.hit_bonus(spell))
        if r < miss:
            return "miss"
        r -= miss
        helpless = foe.controlled(t)   # a stunned, incapacitated or fleeing player cannot dodge, parry or block
        behind = self.side.behind(t)
        red = self.mod.dodge_parry_reduction() + p.expertise
        dodge = 0.0 if helpless else max(0.0, fp.dodge + foe.mod.dodge_bonus(foe.fight) + foe.dodge_bonus(t) - red)
        if r < dodge:
            return "dodge"
        r -= dodge
        parry = 0.0 if (helpless or behind) else max(0.0, fp.parry + foe.mod.parry_bonus(foe.fight) - red)
        if r < parry:
            return "parry"
        r -= parry
        block = 0.0 if (helpless or behind or fp.block <= 0) else fp.block + foe.mod.block_bonus(foe.fight)
        if r < block:
            self._blocked = True
            return "hit"
        r -= block
        crit = p.melee_crit + self.mod.crit_bonus(spell, False)
        return "crit" if r < crit else "hit"

    def apply_control(self, spell):
        foe, t = self.side.foe, self.side.duel.t
        weapon = spell.kind in ("melee", "ranged")
        if spell.root > 0:
            foe.apply_cc("root", spell.root, T.DR_CATEGORY.get(spell.name, "random_root"), spell.name, frozen=spell.name in FROZEN_ROOTS,
                         physical=weapon)
        if spell.stun > 0:
            foe.apply_cc("stun", spell.stun, T.DR_CATEGORY.get(spell.name, "random_stun"), spell.name, physical=weapon or spell.charge)
        if spell.fear > 0:
            foe.apply_cc("fear", spell.fear, T.DR_CATEGORY.get(spell.name, "fear"), spell.name)
        if spell.interrupt > 0 and foe.is_casting():
            foe.interrupt(spell.interrupt + self.mod.interrupt_bonus(self, spell), spell.name)
            self.interrupts += 1
        if spell.daze > 0:
            self.apply_chill(spell, spell.daze, spell.chill_dur or 10.0)

    def resolve_spell(self, spell, instant_from_talent=False):
        self.side.foe.cc_hint = spell.name
        h = self.side.ai.effects.get(spell.name)
        if h is not None:   # a PvP effect the fight lab does not parse (Polymorph, Blink, Ice Block, Blind, Fear ...): the class's handler
            self.casts[spell.name] = self.casts.get(spell.name, 0) + 1
            return h(self.side.duel, self.side, self.side.foe, spell) or 0.0
        return super().resolve_spell(spell, instant_from_talent)


class Side:
    """One combatant: its module, player, fight and PvP state (control, diminishing returns, lockouts, immunities, stealth)."""

    def __init__(self, duel, name, cls, alloc, spec, ai):
        self.duel, self.name, self.cls, self.spec = duel, name, cls, spec
        self.alloc = alloc
        self.mod = FR.make_module(cls, alloc, 60, spec)
        self.mod.veto = {}                      # the leveling rotation's tuned vetoes are PvE rules
        self.p = self.mod.make_player(60)
        self.body = Body(self)
        self.ai = ai
        self.foe = None
        self.fight = None
        self.slow = self.slow_until = 0.0
        self.root_until, self.root_frozen = 0.0, False
        self.stun_until = self.fear_until = 0.0
        self.incap_until, self.incap_name, self.incap_breaks = 0.0, None, True
        self.silence_until = self.disarm_until = 0.0
        self.immune_until = self.immune_phys_until = self.fear_immune_until = 0.0
        self.lockout, self.lockout_all = {}, 0.0
        self.dr = {}
        self.debuffs, self.dots, self.armor_debuff = {}, [], 0.0
        self.attack_slow, self.attack_slow_until = 0.25, 0.0
        self.dmg_reduction = self.dmg_reduction_until = 0.0
        self.trinket_ready = 0.0 if T.TRINKET else 1e18
        self.stealthed = False
        self.inactive_until = 0.0               # a self-imposed pause (Ice Block): no actions, no movement, no attacks
        self.cc_regen = (0.0, 0.0)              # (until, share of maximum health per second): a polymorphed player's regeneration
        self.cc_hint = None                     # the other side's spell being resolved: names control its module sets
        self.root_name = None
        self.intent = "hold"
        self.intent_until = 0.0
        self.speed_bonus = {}                   # name -> (fraction, until)
        self.dodge_buffs = {}                   # name -> (chance, until): Evasion, Deterrence
        self.wanding = False
        self.wand_next = 0.0
        self.seen_cast = None                   # (spell, time first seen): reaction delay before an interrupt
        self.stats = {"cc_taken": {}, "interrupted": 0, "trinket": 0, "dr_immune": 0}

    # ------------------------------------------------------------------ state
    @property
    def t(self):
        return self.duel.t

    def hp_frac(self):
        return max(0.0, self.p.hp) / self.p.hp_max

    def mana_frac(self):
        return self.p.mana / self.p.mana_max if self.p.mana_max > 0 else 1.0

    def armor(self):
        return self.p.armor + self.mod.armor_bonus()

    def dodge_bonus(self, t):
        return sum(c for c, until in self.dodge_buffs.values() if t < until)

    def speed(self, t):
        if t < self.stun_until or t < self.root_until or t < self.incap_until:
            return 0.0
        bonus = max([b for b, until in self.speed_bonus.values() if t < until] or [0.0])
        slow = self.slow if t < self.slow_until else 0.0
        return T.RUN_SPEED * (1.0 + bonus) * (1.0 - slow) * (T.STEALTH_SPEED if self.stealthed else 1.0)

    def controlled(self, t):
        return t < self.stun_until or t < self.incap_until or t < self.fear_until

    def silenced(self, t):
        return t < self.silence_until

    def immune(self, t):
        return t < self.immune_until

    def school_locked(self, school, t):
        return t < self.lockout_all or t < self.lockout.get(school or "", 0.0)

    def is_casting(self):
        return bool(self.fight and (self.fight.casting or self.fight.channel))

    def cast_spell(self):
        if self.fight and self.fight.casting:
            return self.fight.casting[0]
        if self.fight and self.fight.channel:
            return self.fight.channel[0]
        return None

    def cast_end(self):
        return self.fight.casting[1] if self.fight and self.fight.casting else -1.0

    def behind(self, t):
        """Whether this side can stand behind its target: from stealth (the opener), or while the target is stunned, incapacitated
        or fleeing (an open-field duel: a free target keeps facing its attacker)."""
        return self.stealthed or self.foe.controlled(t)

    def dispel_cc(self, kinds=("root", "slow", "fear", "polymorph"), magic_only=True):
        """Remove control from this side (a dispel or a cleanse on oneself): roots, slows, fears and Polymorph by default. Stuns from
        weapons and Sap, Gouge and Blind are not magic. Returns what was removed."""
        t, out = self.t, []
        if "root" in kinds and t < self.root_until and self.root_name not in ("Improved Hamstring", "Entrapment", "Improved Wing Clip"):
            self.root_until = t
            out.append("root")
        if "slow" in kinds and t < self.slow_until:
            self.slow_until = t
            out.append("slow")
        if "fear" in kinds and t < self.fear_until:
            self.fear_until = t
            out.append("fear")
        if "polymorph" in kinds and t < self.incap_until and self.incap_name in ("Polymorph", "Seduction", "Repentance", "Freezing Trap"):
            self.incap_until = t
            out.append(self.incap_name)
        if out:
            self.fight.note(f"dispelled: {', '.join(out)}")
        return out

    def purge_shields(self):
        """An offensive dispel on this side: its absorb shield (Ice Barrier, Power Word: Shield) is removed. Returns the absorb removed."""
        a = self.p.absorb if self.t < self.p.absorb_until else 0.0
        self.p.absorb = 0.0
        if a:
            self.fight.note(f"shield purged ({a:.0f})")
        return a

    def heal_reduction(self):
        t, red = self.t, 0.0
        for name, frac in T.HEAL_REDUCTION.items():
            d = self.debuffs.get(name)
            if d and d.get("until", 0) > t:
                red = max(red, frac * (d.get("stacks", 1) if name == "Wound Poison" else 1))
        return min(0.9, red)

    # ------------------------------------------------------------------ control
    def set_control(self, kind, until):
        """Control set by the other side's module through the mob view (Frostbite, Impact, Mace Specialization, a fight-lab stun or
        fear): diminishing returns by the kind's proc category."""
        cur = getattr(self, f"{kind}_until")
        if until <= cur + EPS:
            return
        src = self.foe
        hint = self.cc_hint
        cat_of = T.DR_CATEGORY.get(hint) or ""
        if hint in T.DR_CATEGORY and (kind in cat_of or (kind == "stun" and cat_of == "kidney_shot") or cat_of == ""):
            name, cat = hint, T.DR_CATEGORY[hint]
        else:
            name, cat = T.PROC_NAME.get((src.cls, kind)), T.DR_DEFAULT.get(kind)
        self.apply_cc(kind, until - self.t, cat, name, frozen=(kind == "root" and src is not None and src.cls == "mage"))

    def apply_cc(self, kind, dur, cat, name, frozen=False, breaks=None, physical=False):
        """Put a control effect on this side: immunity, the PvP cap and diminishing returns first. Returns the seconds applied."""
        t = self.t
        if dur <= 0:
            return 0.0
        if t < self.immune_until or (physical and t < self.immune_phys_until) or (kind == "fear" and t < self.fear_immune_until):
            self.fight.note(f"immune to {name or kind}")
            return 0.0
        dur = min(dur, T.PVP_CC_CAP)
        if cat:
            rec = self.dr.get(cat)
            n = rec[0] if rec and t < rec[1] + T.DR_RESET else 0
            f = T.DR_STEPS[min(n, len(T.DR_STEPS) - 1)]
            if f <= 0:
                self.stats["dr_immune"] += 1
                self.fight.note(f"immune to {name or kind} (diminishing returns)")
                return 0.0
            dur *= f
            self.dr[cat] = [n + 1, t + dur]
        if kind == "stun":
            self.stun_until = max(self.stun_until, t + dur)
            self.break_cast(name or "stunned")
        elif kind == "root":
            if t + dur > self.root_until:
                self.root_until, self.root_frozen, self.root_name = t + dur, frozen, name
        elif kind == "fear":
            self.fear_until = max(self.fear_until, t + dur)
            self.break_cast(name or "feared")
        elif kind == "incap":
            self.incap_until, self.incap_name = t + dur, name
            self.incap_breaks = (name in T.BREAKS_ON_DAMAGE) if breaks is None else breaks
            self.break_cast(name or "incapacitated")
        elif kind == "silence":
            self.silence_until = max(self.silence_until, t + dur)
            self.break_cast(name or "silenced")
        elif kind == "disarm":
            self.disarm_until = max(self.disarm_until, t + dur)
        self.wanding = False
        key = name or kind
        self.stats["cc_taken"][key] = self.stats["cc_taken"].get(key, 0.0) + dur
        self.fight.note(f"{kind} {dur:.1f}s ({name or 'proc'})")
        return dur

    def break_cast(self, why):
        if self.fight is None:
            return
        if self.fight.casting or self.fight.channel:
            spell = self.cast_spell()
            self.fight.casting = None
            self.fight.channel = None
            self.fight.note(f"{spell.name} broken ({why})")

    def interrupt(self, lock, by):
        spell = self.cast_spell()
        if spell is None:
            return
        self.break_cast(by)
        self.lockout[spell.school or ""] = max(self.lockout.get(spell.school or "", 0.0), self.t + lock)
        self.stats["interrupted"] += 1
        self.fight.note(f"{by}: {spell.school} locked {lock:.0f}s")

    def trinket_frees(self, t=None):
        """The control effects on this side its class's PvP trinket would end now (empty when it is on cooldown)."""
        t = self.t if t is None else t
        if t < self.trinket_ready:
            return set()
        b, out = T.TRINKET_BREAKS.get(self.cls, set()), set()
        if "stun" in b and t < self.stun_until:
            out.add("stun")
        if "root" in b and t < self.root_until:
            out.add("root")
        if "slow" in b and t < self.slow_until and self.slow > 0:
            out.add("slow")
        if "fear" in b and t < self.fear_until:
            out.add("fear")
        if t < self.incap_until:
            if "polymorph" in b and self.incap_name == "Polymorph":
                out.add("polymorph")
            if "charm" in b and self.incap_name in T.CHARM:
                out.add("charm")
        return out

    def use_trinket(self):
        t = self.t
        frees = self.trinket_frees(t)
        if not frees:
            return False
        if "stun" in frees:
            self.stun_until = t
        if "root" in frees:
            self.root_until = t
        if "slow" in frees:
            self.slow_until = t
        if "fear" in frees:
            self.fear_until = t
        if "polymorph" in frees or "charm" in frees:
            self.incap_until = t
        self.trinket_ready = t + T.TRINKET_CD
        self.stats["trinket"] += 1
        self.fight.note(f"PvP trinket ({', '.join(sorted(frees))})")
        return True

    # ------------------------------------------------------------------ actions
    def spell(self, name):
        return self.mod.spells.get(name)

    def can(self, name, t=None, ignore_gcd=False):
        """Whether `name` can be used now: known, off cooldown, affordable, in range, not locked or silenced (spells), not disarmed
        (weapon attacks), and the global cooldown free unless the spell is off it."""
        t = self.t if t is None else t
        s = self.mod.spells.get(name)
        if s is None or not self.p.ready(s.name, t) or t < self.inactive_until:
            return False
        if self.foe.stealthed and (s.name in self.ai.hostile_buffs or s.kind in ("melee", "ranged", "channel", "spell"))                 and s.target not in ("self", "pet") and s.kind != "heal":
            return False   # an unseen foe cannot be targeted
        if not ignore_gcd and self.mod.gcd_of(s) > 0 and t + EPS < self.p.gcd_until:
            return False
        if self.controlled(t) or self.is_casting():
            return False
        weapon = s.kind in ("melee", "ranged")
        if not weapon and (self.silenced(t) or self.school_locked(s.school, t)) and s.cost > 0:
            return False
        if weapon and t < self.disarm_until and s.kind == "melee":
            return False
        if not self.fight.can_afford(s, self.mod.mana_cost(s)):
            return False
        return self.in_range(s)

    def in_range(self, s):
        d = self.duel.dist
        if s.target in ("self", "pet") or s.kind in ("buff", "heal") and s.name not in self.ai.hostile_buffs:
            return True
        if s.charge or s.name in getattr(self.ai, "charges", ()):
            return T.MIN_RANGED <= d <= 25.0
        if s.kind == "melee":
            return d <= T.MELEE + 1e-6
        if s.kind == "ranged":
            return T.MIN_RANGED <= d <= max(s.range, 35.0)
        rng = self.ai.ranges.get(s.name, s.range or 30.0)
        return d <= rng + 1e-6

    def cast(self, s):
        """Start `s` (a Spell or its name). Casting stops movement; a hostile action ends stealth."""
        if isinstance(s, str):
            s = self.mod.spells.get(s)
        if s is None:
            return False
        if self.stealthed and s.name not in KEEPS_STEALTH:
            self.stealthed = False
        if s.charge:
            self.duel.set_dist(T.MELEE)
            self.p.swing_mh = self.t
        self.wanding = False
        return bool(self.fight.start_cast(s))


class Duel:
    """One duel: two sides, one distance, a fixed time step. run() returns "A", "B" or "draw"."""

    def __init__(self, a, b, seed=1, log=False, start_dist=None, max_time=None):
        """a, b: (class, talent allocation {name: ranks}, fight-lab spec model, PvPAI instance)."""
        set_gear(T.GEAR_TIER)
        self.rng = random.Random(seed)
        self.t = 0.0
        self.dist = T.START_DIST if start_dist is None else start_dist
        self.max_time = T.MAX_TIME if max_time is None else max_time
        self.log = [] if log else None
        self.combat = False                     # set at the first hostile hit (Charge works only before it)
        self.a = Side(self, "A", *a)
        self.b = Side(self, "B", *b)
        self.a.foe, self.b.foe = self.b, self.a
        self.a.fight = SideFight(self.a, self.log)
        self.b.fight = SideFight(self.b, self.log)
        for s in (self.a, self.b):
            s.fight.t = 0.0
            s.ai.bind(self, s)

    def set_dist(self, v):
        self.dist = max(0.5, min(80.0, v))

    def note(self, msg):
        if self.log is not None:
            self.log.append(f"{self.t:6.2f}s {msg}")

    # ------------------------------------------------------------------ damage
    def damage(self, src, dst, spell, amount, crit=False, source="player", periodic=False):
        t = self.t
        school = getattr(spell, "school", None) or "physical"
        physical = school == "physical" or getattr(spell, "kind", "") in ("melee", "ranged")
        f = src.fight
        if t < dst.immune_until or (physical and t < dst.immune_phys_until):
            f.note(f"{spell.name} immune")
            return 0.0
        raw = amount
        self.combat = True
        if amount > 0 and T.HEAL_REDUCTION.get(spell.name):
            old = dst.debuffs.get(spell.name)
            stacks = min(T.WOUND_STACKS, (old.get("stacks", 0) if old and old.get("until", 0) > t else 0) + 1) if spell.name == "Wound Poison" else 1
            dst.debuffs[spell.name] = {"until": t + (15.0 if spell.name == "Wound Poison" else 10.0), "stacks": stacks}
        if dst.p.absorb > 0 and t < dst.p.absorb_until and amount > 0:
            a = min(dst.p.absorb, amount)
            dst.p.absorb -= a
            amount -= a
        amount = dst.mod.split_damage_taken(dst.fight, amount)
        amount = dst.ai.damage_taken(self, dst, src, spell, amount)
        dst.p.hp -= amount
        f.damage[spell.name] = f.damage.get(spell.name, 0.0) + amount
        if source != "player":
            f.pet_sources.add(spell.name)
        if crit:
            f.crits[spell.name] = f.crits.get(spell.name, 0) + 1
        if raw > 0:
            if t < dst.incap_until and dst.incap_breaks:
                dst.incap_until = t
                dst.fight.note(f"{dst.incap_name} broken by {spell.name}")
            if t < dst.fear_until and self.rng.random() < T.FEAR_BREAK_CHANCE:
                dst.fear_until = t
                dst.fight.note(f"fear broken by {spell.name}")
            rb = T.ROOT_BREAK.get(dst.root_name, 0.0)
            if t < dst.root_until and rb > 0 and (not periodic or dst.root_name in T.ROOT_BREAK_PERIODIC) and self.rng.random() < rb:
                dst.root_until = t
                dst.fight.note(f"{dst.root_name} broken by {spell.name}")
            if dst.stealthed:
                dst.stealthed = False
        if amount > 0:
            if dst.p.rage_max > 0:
                dst.p.rage = min(dst.p.rage_max, dst.p.rage + FT.rage_from_damage_taken(amount, 60))
            dst.fight.damage_taken_effects(amount, crit)
        f.note(f"{spell.name}{' CRIT' if crit else ''} {amount:.0f} -> {dst.name} {max(0, dst.p.hp):.0f}")
        return amount

    # ------------------------------------------------------------------ loop
    def tick_regen(self, s, t):
        f, p = s.fight, s.p
        if t + EPS < f.regen_tick:
            return
        f.regen_tick += 2.0
        if p.mana_max > 0:
            tick = s.mod.mana_regen(p, t)
            if t < p.fsr_until:
                tick *= min(1.0, p.regen_while_casting)
            p.mana = min(p.mana_max, p.mana + tick)
        if p.energy_max > 0:
            p.energy = min(p.energy_max, p.energy + FT.ENERGY_PER_TICK)
        pet = p.pet
        if pet is not None and pet.alive:
            pet.focus = min(pet.focus_max, pet.focus + pet.focus_regen * 2.0)
            pet.mana = min(pet.mana_max, pet.mana + pet.mana_regen * 2.0)
        s.mod.on_regen_tick(f, p, t)

    def tick_periodic(self, s, t):
        """Dots on `s` (the other side's) and heals over time on `s`."""
        src = s.foe
        for dot in list(s.dots):
            if t + EPS >= dot[3]:
                amount, crit = dot[1], False
                if len(dot) > 5 and dot[5] > 0 and self.rng.random() < dot[5]:
                    crit, amount = True, amount * dot[6]
                spell = src.mod.spells.get(dot[0]) or FE.Spell(dot[0], "physical" if dot[0] in ("Deep Wounds", "Rend", "Rupture", "Garrote", "Rake", "Rip", "Lacerate") else "shadow")
                self.damage(src, s, spell, amount, crit, periodic=True)
                dot[2] -= 1
                dot[3] += dot[4]
                src.mod.on_tick(src.fight, FE.Spell(dot[0], "periodic"), amount, crit)
                if dot[2] <= 0 and dot in s.dots:
                    s.dots.remove(dot)
        if t < s.cc_regen[0] and t < s.incap_until:
            s.p.hp = min(s.p.hp_max, s.p.hp + s.cc_regen[1] * s.p.hp_max * T.DT)
        for hot in list(s.p.hots):
            if t + EPS >= hot[3]:
                s.fight.heal(FE.Spell(hot[0], "holy"), hot[1], hot[5] if len(hot) > 5 else "player")
                hot[2] -= 1
                hot[3] += hot[4]
                if hot[2] <= 0 and hot in s.p.hots:
                    s.p.hots.remove(hot)

    def velocity(self, s, t):
        """Yards per second `s` moves away from the other side (negative: toward it)."""
        if t < s.inactive_until:
            return 0.0
        if t < s.fear_until:
            return 0.6 * s.speed(t) if t >= s.root_until else 0.0   # a feared player runs, not always straight away
        sp = s.speed(t)
        if sp <= 0 or s.controlled(t):
            return 0.0
        f = s.fight
        if f.casting or f.channel:
            return 0.0
        if s.intent == "close":
            stop = s.ai.close_to(self, s)
            return -sp if self.dist > stop + 1e-6 else 0.0
        if s.intent == "kite":
            return sp
        return 0.0

    def move(self, t):
        va, vb = self.velocity(self.a, t), self.velocity(self.b, t)
        if va or vb:
            d = self.dist + (va + vb) * T.DT
            closers = [s for s, v in ((self.a, va), (self.b, vb)) if v < 0]
            if closers:
                d = max(d, min(s.ai.close_to(self, s) for s in closers))
            self.set_dist(d)
            for s, v in ((self.a, va), (self.b, vb)):
                if v:
                    s.fight.last_move = t

    def tick_attacks(self, s, t):
        f, p = s.fight, s.p
        if s.controlled(t) or s.stealthed or t < s.inactive_until:
            return
        if s.mod.melee and s.ai.auto_attack and self.dist <= T.MELEE + 1e-6 and not f.casting and t >= s.disarm_until:
            if p.mh is not None and t + EPS >= p.swing_mh:
                f.auto_swing("mh")
                p.swing_mh = t + p.mh.speed * s.mod.swing_speed_factor() * (1.0 + s.attack_slow if t < s.attack_slow_until else 1.0)
            if p.oh is not None and t + EPS >= p.swing_oh:
                f.auto_swing("oh")
                p.swing_oh = t + p.oh.speed * s.mod.swing_speed_factor() * (1.0 + s.attack_slow if t < s.attack_slow_until else 1.0)
        if s.mod.ranged and p.ranged is not None and not f.casting and not f.channel and self.dist >= T.MIN_RANGED \
                and t >= f.last_move + FT.AUTO_SHOT_STAND_STILL and t + EPS >= p.shot_at and self.dist <= 35.0:
            f.auto_shot()
            p.shot_at = t + p.ranged.speed * s.mod.swing_speed_factor()
        if s.wanding and not f.casting and not f.channel and t + EPS >= s.wand_next and self.dist <= 30.0 and t >= f.last_move + 0.5:
            f.wand_shot()
            s.wand_next = t + FE.WAND_SPEED
        pet = p.pet
        if pet is not None and pet.alive and not s.foe.stealthed:
            if not pet.engaged:
                pet.engaged = t >= s.ai.pet_arrives
                pet.swing_at = t
            elif t + EPS >= pet.swing_at and not s.ai.pet_held(self, s, t):
                f.pet_swing()
                pet.swing_at = t + pet.speed
                ab = s.mod.pet_decide(f)
                if ab is not None and pet.cooldowns.get(ab.name, -1.0) <= t:
                    f.pet_ability(ab)

    def tick_cast(self, s, t):
        f = s.fight
        if f.casting:
            spell, end, started = f.casting
            if s.silenced(t) or (spell.kind not in ("melee", "ranged") and s.school_locked(spell.school, t)):
                s.break_cast("locked")
            elif t + EPS >= end:
                f.finish_cast()
        elif f.channel:
            if t + EPS >= f.channel[1]:
                f.channel_tick()

    def act(self, s, action):
        if action is None:
            return
        if action == "trinket":
            s.use_trinket()
        elif action == "wand":
            if not s.wanding:
                s.wanding, s.wand_next = True, self.t + 0.5
        elif action == "retreat":
            s.intent, s.intent_until = "kite", self.t + s.mod.retreat_time()
        elif action == "advance":
            s.intent, s.intent_until = "close", self.t + 1.0
        elif action == "shoot":
            s.wanding = False
        else:
            s.cast(action)

    def decide(self, s, t):
        f = s.fight
        if t < s.inactive_until:
            self.act(s, s.ai.while_inactive(self, s, s.foe))
            return
        if s.controlled(t):
            self.act(s, s.ai.while_controlled(self, s, s.foe))
            return
        if f.casting or f.channel:
            self.act(s, s.ai.while_casting(self, s, s.foe))
            return
        self.act(s, s.ai.off_gcd(self, s, s.foe))
        if s.controlled(t) or f.casting or f.channel:
            return
        if t + EPS >= s.p.gcd_until:
            self.act(s, s.ai.decide(self, s, s.foe))

    def run(self):
        a, b = self.a, self.b
        for s in (a, b):
            s.mod.on_fight_start(s.fight)
            s.ai.prefight(self, s, s.foe)
        while True:
            t = self.t
            for s in (a, b):
                s.fight.t = t
            if a.p.hp <= 0 or b.p.hp <= 0:
                if a.p.hp <= 0 and b.p.hp <= 0:
                    return "draw"
                return "B" if a.p.hp <= 0 else "A"
            if t > self.max_time:
                return "draw"
            for s in (a, b):
                self.tick_regen(s, t)
                self.tick_periodic(s, t)
            for s in (a, b):
                if t >= s.intent_until:
                    s.intent = s.ai.intent(self, s, s.foe)
            self.move(t)
            for s in (a, b):
                self.tick_attacks(s, t)
                self.tick_cast(s, t)
            for s in (a, b):
                if a.p.hp > 0 and b.p.hp > 0:
                    self.decide(s, t)
            self.t = round(t + T.DT, 6)
