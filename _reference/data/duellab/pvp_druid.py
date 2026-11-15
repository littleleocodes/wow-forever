"""Druid PvP layer (duellab, 2026-11-14): forms, a prowled opener (Pounce or Ravage), healing in caster form (Rejuvenation, Regrowth,
Swiftmend, Nature's Swiftness with Healing Touch, Innervate, Barkskin, Entangling Roots, a Bear Form Bash before the heals), shapeshifts
out of roots, slows and Polymorph, Feral Charge, Dash, Nature's Grasp, Faerie Fire against stealth; Balance kites and roots in Moonkin
Form. Damage is the spec's own leveling rotation underneath: the cat's (Claw, Rake, Rip, Ferocious Bite; Restoration builds play it
too, the project's rule) or Balance's (Moonfire, Wrath, Starfire, Eclipse, Nature's Grace, its own emergency heals).

Forms: the fight-lab module knows Cat Form (cat builds; out of it is caster form) and Moonkin Form (Balance). This layer adds a short
Bear Form stay for Bash and moves between the forms:
- entering a form costs its mana (the module's shift_in / enter_moonkin, Natural Shapeshifter), a 1.5 s global cooldown, and frees the
  druid of roots and slows (the forms' tooltips: "The act of shapeshifting frees the caster of Polymorph and Movement Impairing
  effects"); leaving one for caster form is free and instant; no shift while silenced (a shapeshift is a spell). A cat rooted for
  1.5+ s with its foe out of reach, or slowed by 40%+
  while its foe kites at 8+ yards, re-enters Cat Form (a powershift; Furor 5/5 keeps the energy, the module's furor_energy) when the
  mana for one heal cycle stays (Rejuvenation, Swiftmend, the shift back): the mage's chills had drained it in a few shifts.
- in Cat, Bear or Moonkin Form the druid is immune to Polymorph ("protects the caster from Polymorph effects") and to Disarm; in caster
  form a Polymorph is broken by shifting into Cat Form (Moonkin Form for Balance) after the reaction time (the same tooltip line; the
  druid's PvP trinket does not break Polymorph, dtables).
- Bear Form for Bash: when a cat (or a healer) wants to heal with a free melee foe in reach, it shifts to Bear Form (Furor: 10 rage a
  shift at 5/5), Bashes (4 s stun, +0.5 s a rank of Brutal Impact, physical), then heals in caster form under the stun. No auto
  attacks, armor or health from Bear Form during the stay (it lasts two global cooldowns).

Effects the fight lab does not parse, or parses for PvE only (diminishing-returns categories always from dtables.DR_CATEGORY):
- Pounce: a 2 s stun (+0.5 s a rank of Brutal Impact) applied once (the module's path applied it twice, so diminishing returns
  counted it twice), its bleed and combo point through the module. Ravage: the module's. Both only from Prowl.
- Bash (above). Feral Charge: in Cat Form "leap behind an enemy" (8-25 yards, 30 s cooldown, no root), in Bear Form a 4 s root and a
  4 s interrupt (5 rage, 15 s cooldown); one shared cooldown name.
- Swiftmend: consumes a Rejuvenation (else Regrowth) on the druid and heals what its full periodic part would (tooltip), crits as a
  spell. Barkskin: 20% less physical damage and no pushback for 15 s. Innervate: mana regeneration x5 and all of it while casting
  for 20 s. Faerie Fire: 505 armor off and no stealth for 40 s (the rogue layer reads it before Vanish). Dash: +60% speed for 15 s
  (keeps Prowl). Nature's Grasp: cast before the duel and again when ready against a melee foe (castable in forms); the next melee hit
  roots the attacker as Entangling Roots (the engine's 10 s cap, its 30% break chance on direct hits). Nature's Swiftness: the
  module's (the next Nature spell instant), off the global cooldown.

Assumptions:
- Heal thresholds (measured, 200 duels, 2026-11-14): builds led by Restoration shift out below 55% health and heal to 85%; others
  likewise against a melee foe (a two-hander's crits: feral-combat-pvp won 43% against arms-pvp at 35%/70%, 49.5% at 45%/80%, 54% at
  55%/85%) and below 35% to 70% against a foe that casts (61.5% against pvp-frost; 57% at 45%/80%, 44% at 55%/85%); the module's own
  emergency (30%) stays underneath.
  While the foe is immune (Ice Block, Divine Shield) a cat heals to 90%. A heal is cast only with the mana to shift back.
- Next to a free melee foe: Barkskin, the instants (Rejuvenation, Swiftmend, Nature's Swiftness with Healing Touch), then Entangling
  Roots (it roots, or it spends the foe's interrupt); cast heals wait while that foe's interrupt is ready (Pummel, Kick, Shield Bash,
  Counterspell, Earth Shock, Feral Charge, Spell Lock), and a rooted foe is walked out of reach first. With nothing left to cast, back
  to Cat Form while the heals over time run. Innervate below 35% mana (not below 40% health next to a melee foe).
- The opener is Pounce against a foe that casts (no melee foe) and for Restoration builds, else Ravage.
- Barkskin only in caster or Moonkin Form (Classic 1.12: not in Cat or Bear Form). Innervate and Faerie Fire likewise.
- Off the global cooldown: Dash, Nature's Swiftness, Feral Charge (the engine's off-GCD list from the raid simulator's store). The
  engine then sets the global cooldown to "now", which would cut a running one short: these restore it.
- The engine lets auto attacks hit a stealthed target, so a prowling cat stops just outside melee reach and steps in with its opener.
  Two stealthers in one duel: side B leaves stealth within 12 yards (no stealth detection in the engine).
- The module's priority knows no player lockouts: spells the engine refuses (silence, a locked school) are hidden from it, so Balance
  casts Starfire while Nature is locked instead of idling on Wrath. Its "advance" is dropped (the intent closes already; the action
  would hold the intent for 1 s and skip this layer's per-step bookkeeping: Feral Swiftness lapsed and the cat never caught a mage).
- Balance: kites like the mage layer (26 yards; offensive Balance spells reach 30 yards plus Nature's Reach), roots a free melee foe
  within 8 yards (root diminishing returns at least half), re-enters Moonkin Form when rooted by a melee foe in reach, Barkskin below
  80% health against melee, Faerie Fire on a rogue or druid, Innervate below 30% mana; no damage spells into an immunity.
- Measured and rejected (200 duels against pvp-frost): hanging back from a mage that kites at the cat's speed (feral-combat-pvp
  38.5% -> 30% wins); Dash whenever the foe kites (38.5% -> 31.5%; Dash waits for 10+ yards).

Not modelled: Hibernate (Beasts and Dragonkin only: no player), Cyclone (not in Forever), Bear Form's armor, health, swings and
abilities beyond Bash and Feral Charge (Maul, Enrage, Frenzied Regeneration, Demoralizing Roar), Travel Form, Tranquility, Wild Growth,
Hurricane, Cure Poison and Abolish Poison, Remove Curse, Nature's Grasp's damage over time, Improved Entangling Roots' higher damage
threshold before the root breaks (the engine's 30% a hit), stealth detection (Feral Instinct), Prowl's restealth (out of combat only).
"""
import collections
import dataclasses
import re
import sys

import dtables as T
import engine as FE
from pvp_base import PvPAI, HOSTILE

GCD_FORM = 1.5                                              # entering a form
OFF_GCD = {"Dash", "Nature's Swiftness", "Feral Charge"}    # the store's off_gcd list (Berserk: the module presses it itself)
STEALTH_SAFE = {"Dash"}                                     # "Does not break prowling"
INTERRUPTS = {"Pummel": 5.5, "Shield Bash": 5.5, "Kick": 5.5, "Counterspell": 30.0, "Earth Shock": 20.0, "Feral Charge": 25.0,
              "Spell Lock": 30.0, "Silence": 30.0}         # the foe's interrupt and its reach (yards)
OFFENSIVE_BALANCE = ("Wrath", "Starfire", "Moonfire", "Insect Swarm", "Entangling Roots", "Faerie Fire", "Hurricane")
FF_ARMOR = re.compile(r"armor of the target by (\d+)")


def cat(name):
    """The diminishing-returns category of a control (dtables.DR_CATEGORY; None: none)."""
    return T.DR_CATEGORY.get(name)


def dr_factor(side, category, t):
    """The share of its duration the next control of `category` would last on `side` (1, 0.5, 0.25 or 0: immune; 1 without one)."""
    if category is None:
        return 1.0
    rec = side.dr.get(category)
    n = rec[0] if rec and t < rec[1] + T.DR_RESET else 0
    return T.DR_STEPS[min(n, len(T.DR_STEPS) - 1)]


def locked_spells(me, t):
    """Spells the engine refuses now (Side.can: a spell is no weapon attack and costs mana or is a spell, channel or heal; silenced, or
    its school locked by an interrupt): hidden from the module's priority, which knows no lockouts, so it falls through to its next
    castable spell instead of naming a locked one every step."""
    silenced = me.silenced(t)
    return {n for n, s in me.mod.spells.items()
            if s.kind not in ("melee", "ranged") and (s.resource == "mana" or s.kind in ("spell", "channel", "heal"))
            and (silenced or me.school_locked(s.school, t))}


class DruidPvP(PvPAI):
    keep_range = 0.0
    auto_attack = True
    charges = {"Feral Charge"}
    hostile_buffs = HOSTILE | {"Faerie Fire", "Feral Charge"}
    HEAL_IN, HEAL_OUT = 0.35, 0.70           # cat builds led by Feral Combat against a foe that casts
    MELEE_IN, MELEE_OUT = 0.55, 0.85         # ... and against a melee foe (measured: see the docstring)
    HEALER_IN, HEALER_OUT = 0.55, 0.85       # builds led by Restoration
    POUNCE_VS = "caster"                      # Pounce opener against: "caster" (a foe that is no melee), "all", "none"

    # ------------------------------------------------------------------ setup
    def bind(self, d, me):
        super().bind(d, me)
        mod = me.mod
        self.start_dist = d.dist
        self.balance = mod.balance
        self.cat_build = mod.form == "cat"
        tree = sys.modules[type(mod).__module__].TREE   # the fight-lab module's talent data
        trees = {t["name"]: tr["name"] for tr in tree["trees"] for t in tr["talents"]}
        pts = collections.Counter()
        for n, r in me.alloc.items():
            pts[trees.get(n)] += r
        self.healer = pts.most_common(1)[0][0] == "Restoration" if pts else False
        if self.healer:
            self.heal_in, self.heal_out = self.HEALER_IN, self.HEALER_OUT
        elif self.melee_foe(me.foe):
            self.heal_in, self.heal_out = self.MELEE_IN, self.MELEE_OUT
        else:
            self.heal_in, self.heal_out = self.HEAL_IN, self.HEAL_OUT
        if self.balance:
            self.keep_range = 26.0
        reach = 30.0 * (1 + mod.tv("Nature's Reach", 0) / 100)   # "Increases the range of your offensive Balance spells by 20%" (2 ranks)
        self.ranges = {n: reach for n in OFFENSIVE_BALANCE}
        self.ranges.update({"Nature's Grasp": 100.0, "Swiftmend": 100.0})   # cast on the druid itself
        self.bear = False
        self.bear_goal = None
        self.barkskin_until = self.innervate_until = self.grasp_until = 0.0
        self.ff_until, self.ff_armor = 0.0, 0.0
        self.poly_seen = None
        self._gcd_before, self._was_stealthed = 0.0, False
        self.base_rwc = me.p.regen_while_casting
        fc = mod.spells.get("Feral Charge")
        self.cat_charge = dataclasses.replace(fc, cooldown=30.0) if fc is not None else None   # "Feral Charge (Cat): ... 30 sec cooldown"
        orig_regen, orig_push = mod.mana_regen, mod.pushback_resisted

        def mana_regen(p, t):   # Innervate: "Increases the target's Mana regeneration by 400%"
            r = orig_regen(p, t)
            return r * 5.0 if t < self.innervate_until else r

        def pushback_resisted(fight, spell):   # Barkskin: "damaging attacks will not cause spellcasting delays"
            return fight.t < self.barkskin_until or orig_push(fight, spell)

        mod.mana_regen, mod.pushback_resisted = mana_regen, pushback_resisted

    def effects_for(self, me):
        return {"Pounce": self.pounce, "Bash": self.bash, "Feral Charge": self.feral_charge, "Swiftmend": self.swiftmend,
                "Barkskin": self.barkskin, "Innervate": self.innervate, "Faerie Fire": self.faerie_fire, "Dash": self.dash,
                "Nature's Grasp": self.natures_grasp, "Nature's Swiftness": self.plain, "Rejuvenation": self.plain}

    def prefight(self, d, me, foe):
        """Undo the module's mob pull (it prowls up to melee and presses Berserk) and stand at the duel's distance: a cat in Prowl,
        Balance in Moonkin Form; Nature's Grasp before the duel against a melee foe."""
        p, t = me.p, d.t
        d.set_dist(self.start_dist)
        if p.buffs.pop("Berserk", None) is not None:
            p.cooldowns.pop("Berserk", None)
        if self.cat_build:
            me.stealthed = True
        ng = me.mod.spells.get("Nature's Grasp")
        if ng is not None and self.melee_foe(foe) and p.mana >= me.mod.mana_cost(ng):
            p.mana -= me.mod.mana_cost(ng)
            p.cooldowns["Nature's Grasp"] = t + ng.cooldown
            self.grasp_until = t + 45.0
            me.fight.note("Nature's Grasp")

    # ------------------------------------------------------------------ helpers
    def _pre(self, me):
        self._gcd_before, self._was_stealthed = me.p.gcd_until, me.stealthed

    def _after(self, me, spell):
        if spell.name in OFF_GCD:
            me.p.gcd_until = self._gcd_before
        if spell.name in STEALTH_SAFE and self._was_stealthed:
            me.stealthed = True

    def _resolve(self, me, spell):
        amount = FE.Fight.resolve_spell(me.fight, spell)
        me.fight.casts[spell.name] = me.fight.casts.get(spell.name, 1) - 1
        return amount

    def _roll(self, me, spell):
        f = me.fight
        out = f.attack_table(spell, False)
        f._blocked = False
        if out in ("miss", "dodge", "parry"):
            f.note(f"{spell.name} {out.upper()}")
            me.mod.on_swing(f, spell, out, 0.0, "mh")
            me.mod.on_miss(f, spell)
            return None
        return out

    def form(self, me):
        mod = me.mod
        if self.bear:
            return "bear"
        if self.cat_build and mod.in_cat:
            return "cat"
        if self.balance and mod.in_moonkin:
            return "moonkin"
        return "caster"

    def freed(self, d, me, why):
        t = d.t
        if t < me.root_until or (t < me.slow_until and me.slow > 0):
            me.fight.note(f"{why} frees it of roots and slows")
        me.root_until = min(me.root_until, t)
        me.slow_until = min(me.slow_until, t)

    def to_caster(self, d, me):
        mod = me.mod
        if self.bear:
            self.leave_bear(me)
        elif self.cat_build and mod.in_cat:
            mod.shift_out(me.fight)
        elif self.balance and mod.in_moonkin:
            mod.leave_moonkin(me.fight)

    def to_cat(self, d, me):
        mod, p, t = me.mod, me.p, d.t
        if me.silenced(t):
            return False   # a shapeshift is a spell
        if self.bear:
            self.leave_bear(me)
        if not mod.shift_in(me.fight, p, t):
            return False
        self.freed(d, me, "Cat Form")
        p.gcd_until = t + GCD_FORM
        return True

    def to_bear(self, d, me, goal):
        mod, p, t = me.mod, me.p, d.t
        cost = mod.shift_cost(p)   # Bear Form costs Cat Form's 55% of base mana
        if p.mana < cost or me.silenced(t):
            return False
        if self.cat_build and mod.in_cat:
            mod.shift_out(me.fight)
        p.mana -= cost
        p.fsr_until = t + 5.0
        self.bear, self.bear_goal = True, goal
        p.rage_max = 100.0
        p.rage = mod.tv("Furor", 1) if me.fight.rng.random() < mod.tv("Furor", 0) / 100 else 0.0   # "a 100% chance to gain 10 Rage" at 5/5
        p.mh = None
        self.freed(d, me, "Bear Form")
        p.gcd_until = t + GCD_FORM
        me.fight.note(f"Bear Form ({p.rage:.0f} rage)")
        me.fight.casts["Bear Form"] = me.fight.casts.get("Bear Form", 0) + 1
        return True

    def leave_bear(self, me):
        self.bear, self.bear_goal = False, None
        me.p.rage = me.p.rage_max = 0.0

    def to_moonkin(self, d, me):
        mod, p, t = me.mod, me.p, d.t
        if not mod.moonkin or me.silenced(t) or not mod.enter_moonkin(me.fight, p, t):
            return False
        self.freed(d, me, "Moonkin Form")
        p.gcd_until = t + GCD_FORM
        return True

    def hot_on(self, me, name):
        return any(h[0] == name and h[2] > 0 for h in me.p.hots)

    def foe_interrupt_ready(self, d, foe):
        t = d.t
        if foe.controlled(t) or foe.silenced(t):
            return False
        return any(n in foe.mod.spells and foe.p.ready(n, t) and d.dist <= reach for n, reach in INTERRUPTS.items())

    def physical_near(self, d, me, foe):
        """A foe that can hit the druid with weapons now: a melee foe in reach and not under control."""
        return self.melee_foe(foe) and d.dist <= T.MELEE + 0.5 and not foe.controlled(foe.t)

    def ff_wanted(self, d, me, foe):
        ff = foe.debuffs.get("Faerie Fire")
        return foe.cls in ("rogue", "druid") and not (ff and ff.get("until", 0) > d.t) and "Faerie Fire" in me.mod.spells

    # ------------------------------------------------------------------ effects
    def plain(self, d, me, foe, spell):
        amount = self._resolve(me, spell)
        if spell.name in ("Nature's Swiftness", "Rejuvenation"):
            me.fight.note(spell.name)
        self._after(me, spell)
        return amount

    def pounce(self, d, me, foe, spell):
        f, p, t = me.fight, me.p, d.t
        out = self._roll(me, spell)
        if out is None:
            return 0.0
        d.combat = True
        p.combo = min(5, p.combo + max(0, spell.combo))
        f.apply_periodic(spell)                             # the bleed (Genesis, Rend and Tear through the module)
        me.mod.on_swing(f, spell, out, 0.0, "mh")           # opened, Omen of Clarity
        foe.apply_cc("stun", spell.stun + me.mod.tv("Brutal Impact", 0), cat("Pounce"), "Pounce", physical=True)
        return 0.0

    def bash(self, d, me, foe, spell):
        if self._roll(me, spell) is None:
            self.bear_goal = None
            return 0.0
        d.combat = True
        foe.apply_cc("stun", spell.stun + me.mod.tv("Brutal Impact", 0), cat("Bash"), "Bash", physical=True)
        self.bear_goal = None
        return 0.0

    def feral_charge(self, d, me, foe, spell):
        t = d.t
        if self.bear:   # "immobilizing them and interrupting any spell they are casting for 4 sec"
            if foe.is_casting():
                foe.interrupt(4.0, "Feral Charge")
                me.fight.interrupts += 1
            foe.apply_cc("root", 4.0, cat("Feral Charge"), "Feral Charge", physical=True)
            me.p.rage = max(0.0, me.p.rage - 5.0)
        else:
            me.fight.note("Feral Charge (Cat): leaps behind")
        d.combat = True
        self._after(me, spell)
        return 0.0

    def swiftmend(self, d, me, foe, spell):
        p, f = me.p, me.fight
        h = next((x for x in p.hots if x[0] == "Rejuvenation"), None) or next((x for x in p.hots if x[0] == "Regrowth"), None)
        if h is None:
            f.note("Swiftmend: no heal over time to consume")
            return 0.0
        src = me.mod.spells.get(h[0])
        amount = h[1] * max(1, int((src.hot_dur if src else 12.0) / 3.0))   # "an amount equal to the full duration of the periodic effect"
        crit = f.rng.random() < p.spell_crit
        if crit:
            amount *= 1.5
        p.hots.remove(h)
        got = f.heal(spell, amount, "player", crit)
        f.note(f"Swiftmend ({h[0]}){' CRIT' if crit else ''} heals {got:.0f}")
        return 0.0

    def barkskin(self, d, me, foe, spell):
        self.barkskin_until = d.t + 15.0
        me.fight.note("Barkskin")
        return 0.0

    def innervate(self, d, me, foe, spell):
        self.innervate_until = d.t + 20.0
        me.p.regen_while_casting = 1.0   # "allows 100% of the target's Mana regeneration to continue while casting"
        me.fight.note("Innervate")
        return 0.0

    def faerie_fire(self, d, me, foe, spell):
        t = d.t
        m = FF_ARMOR.search(getattr(me.mod.book.get("Faerie Fire"), "text", "") or "")
        armor = float(m.group(1)) if m else 505.0
        if not self.ff_armor:
            foe.armor_debuff += armor
            self.ff_armor = armor
        self.ff_until = t + 40.0
        foe.debuffs["Faerie Fire"] = {"until": t + 40.0, "stacks": 1}
        d.combat = True
        me.fight.note("Faerie Fire")
        return 0.0

    def dash(self, d, me, foe, spell):
        me.speed_bonus["Dash"] = (0.6, d.t + 15.0)
        me.fight.note("Dash")
        self._after(me, spell)
        return 0.0

    def natures_grasp(self, d, me, foe, spell):
        self.grasp_until = d.t + 45.0
        me.fight.note("Nature's Grasp")
        return 0.0

    def cc_immune(self, d, me, kind, name):
        """The forms "protect the caster from Polymorph effects", and a druid in Cat, Bear or Moonkin Form has no weapon to disarm:
        refused up front through the engine's hook (2026-11-14; undo_poly stays for a Polymorph cast before the shift landed)."""
        f = self.form(me)
        return f in ("cat", "bear", "moonkin") and (name == "Polymorph" or kind == "disarm")

    def undo_poly(self, me):
        """A Polymorph that landed on a druid in a form: it never could (the forms "protect the caster from Polymorph effects")."""
        t = me.t
        dur = me.incap_until - t
        me.incap_until = t
        rec = me.dr.get(cat("Polymorph"))
        if rec:
            if rec[0] <= 1:
                me.dr.pop(cat("Polymorph"), None)
            else:
                rec[0] -= 1
        ct = me.stats["cc_taken"]
        if "Polymorph" in ct:
            ct["Polymorph"] = max(0.0, ct["Polymorph"] - dur)
        me.fight.note("immune to Polymorph (shapeshifted)")

    def damage_taken(self, d, me, src, spell, amount):
        t = d.t
        if t < self.barkskin_until and (getattr(spell, "school", None) or "physical") == "physical":
            amount *= 0.8   # "Physical damage taken is reduced by 20%"
        if t < self.grasp_until and src is me.foe and getattr(spell, "kind", "") == "melee" and d.dist <= T.MELEE + 0.5 and amount > 0 \
                and not d.periodic_hit:   # a strike, not a bleed's tick
            self.grasp_until = 0.0
            me.fight.note("Nature's Grasp roots the attacker")
            src.apply_cc("root", 27.0, cat("Nature's Grasp"), "Entangling Roots")   # "Entangling Roots (Rank 6)": 27 s, the engine's PvP cap
        return amount

    # ------------------------------------------------------------------ movement
    def _tick(self, d, me, foe):
        t, mod = d.t, me.mod
        f = self.form(me)
        if t < me.disarm_until and f in ("cat", "bear"):
            me.disarm_until = t
            me.fight.note("immune to Disarm (shapeshifted)")
        if f == "cat" and mod.rank("Feral Swiftness"):   # "Increases your movement speed while in Cat Form by 30%" (2 ranks)
            me.speed_bonus["Feral Swiftness"] = (mod.tv("Feral Swiftness", 0) / 100, t + T.DT + 1e-6)
        if self.innervate_until and t >= self.innervate_until:
            me.p.regen_while_casting = self.base_rwc
            self.innervate_until = 0.0
        if self.ff_armor and t >= self.ff_until:
            foe.armor_debuff = max(0.0, foe.armor_debuff - self.ff_armor)
            self.ff_armor = 0.0
        self.auto_attack = not (t < foe.immune_until or t < foe.immune_phys_until)   # no swings into Ice Block or Divine Shield
        if me.stealthed and foe.stealthed and me.name == "B" and d.dist <= 12.0:
            me.stealthed = False   # two stealthers: one shows itself (no stealth detection in the engine)
            me.fight.note("leaves Prowl (both stealthed)")

    def intent(self, d, me, foe):
        self._tick(d, me, foe)
        t = d.t
        if foe.stealthed and not me.stealthed:
            return "hold"
        if self.form(me) in ("cat", "bear"):
            return "close"   # (hanging back from a kiting mage was tried: feral-combat-pvp 38.5% -> 30% against pvp-frost)
        if self.melee_foe(foe):   # caster or Moonkin Form against melee: away while it is held, like the mage layer
            stuck = foe.body.rooted(t) or foe.controlled(t)
            if stuck and d.dist < 20.0:
                return "kite"
            if self.balance and d.dist < 9.0 and not stuck:
                return "kite"
            return "hold" if not self.balance or d.dist <= self.keep_range else "close"
        if self.balance:
            return "close" if d.dist > self.keep_range else "hold"
        return "hold"

    def close_to(self, d, me):
        if me.stealthed:
            return T.MELEE + 0.4   # just outside reach, then a step in with the opener
        if self.form(me) in ("cat", "bear"):
            return T.MELEE - 0.5
        return self.keep_range if self.balance else T.MELEE - 0.5

    # ------------------------------------------------------------------ decisions
    def while_controlled(self, d, me, foe):
        t = d.t
        if t < me.incap_until and me.incap_name == "Polymorph":
            if self.form(me) in ("cat", "bear", "moonkin"):
                self.undo_poly(me)
                return None
            if self.poly_seen is None:
                self.poly_seen = t
            if t - self.poly_seen >= T.REACTION:
                ok = self.to_moonkin(d, me) if self.balance else self.to_cat(d, me)
                if ok:
                    me.incap_until = t
                    me.fight.note("shapeshifts out of Polymorph")
                    self.poly_seen = None
            return None
        self.poly_seen = None
        return super().while_controlled(d, me, foe)

    def off_gcd(self, d, me, foe):
        self._pre(me)
        t, p, sp = d.t, me.p, me.mod.spells
        if foe.stealthed:
            return None
        f = self.form(me)
        ht = sp.get("Healing Touch")
        if f == "caster" and me.hp_frac() < 0.35 and ht is not None and "Nature's Swiftness" in sp and not p.buff("Nature's Swiftness", t) \
                and me.fight.can_afford(ht, me.mod.mana_cost(ht)) and not me.school_locked("nature", t) and me.can("Nature's Swiftness", ignore_gcd=True):
            return "Nature's Swiftness"
        if f == "cat" and not me.stealthed and self.cat_charge is not None and 8.0 <= d.dist <= 25.0 and t >= me.root_until \
                and me.can("Feral Charge", ignore_gcd=True):
            return self.cat_charge
        if f == "cat" and not me.stealthed and t >= me.root_until and "Dash" in sp and t >= me.speed_bonus.get("Dash", (0, 0))[1] \
                and d.dist > 10.0 and (foe.ai.keep_range > 0 or t < me.slow_until) and me.can("Dash", ignore_gcd=True):
            return "Dash"   # (Dash whenever the foe kites, at any distance, was tried: feral-combat-pvp 38.5% -> 31.5% against pvp-frost)
        return None

    def decide(self, d, me, foe):
        self._pre(me)
        if foe.stealthed:   # a vanished rogue or a prowling cat: heal up meanwhile
            if not me.stealthed and me.hp_frac() < self.heal_out and self.form(me) != "moonkin":
                if self.form(me) != "caster" and self.want_heal_any(me):
                    self.to_caster(d, me)
                if self.form(me) == "caster":
                    return self.caster_play(d, me, foe)
            return None
        if self.balance:
            return self.balance_play(d, me, foe)
        if me.stealthed:
            return self.prowl_play(d, me, foe)
        f = self.form(me)
        if f == "bear":
            return self.bear_play(d, me, foe)
        if f == "caster":
            return self.caster_play(d, me, foe)
        return self.cat_play(d, me, foe)

    # cat builds -------------------------------------------------------------
    def prowl_play(self, d, me, foe):
        t, p, sp = d.t, me.p, me.mod.spells
        if d.dist > T.MELEE + 0.5 + 1e-6:
            return None
        pounce = (self.POUNCE_VS == "all" or self.POUNCE_VS == "caster" and (not self.melee_foe(foe) or self.healer)) \
            and dr_factor(foe, cat("Pounce"), t) >= 0.5
        order = ["Pounce", "Ravage", "Shred", "Claw"] if pounce else ["Ravage", "Pounce", "Shred", "Claw"]
        for n in order:
            s = sp.get(n)
            if s is None or not p.ready(n, t):
                continue
            if not me.fight.can_afford(s, me.mod.mana_cost(s)):
                return None   # pool energy in Prowl
            return self.step_in(d, me, n)
        return None

    def step_in(self, d, me, name):
        old = d.dist
        d.set_dist(min(d.dist, T.MELEE - 0.5))
        if not me.can(name):
            d.set_dist(old)
            return None
        return name

    def want_heal(self, d, me, foe):
        hp = me.hp_frac()
        if hp >= self.heal_in or (foe.hp_frac() < 0.15 and hp > 0.15):
            return False
        return self.want_heal_any(me)

    def want_heal_any(self, me):
        """The mana for a heal and the shift back to Cat Form."""
        p, mod, sp = me.p, me.mod, me.mod.spells
        heals = [mod.mana_cost(sp[n]) for n in ("Rejuvenation", "Regrowth", "Swiftmend") if n in sp]
        return bool(heals) and p.mana >= (mod.shift_cost(p) if self.cat_build else 0.0) + min(heals)

    def bash_first(self, d, me, foe):
        p, mod, sp, t = me.p, me.mod, me.mod.spells, d.t
        bash = sp.get("Bash")
        if bash is None or not p.ready("Bash", t) or not self.physical_near(d, me, foe) or foe.immune(t) or t < foe.immune_phys_until:
            return False
        if dr_factor(foe, cat("Bash"), t) < 0.5:
            return False
        heal = min((mod.mana_cost(sp[n]) for n in ("Regrowth", "Rejuvenation") if n in sp), default=0.0)
        return p.mana >= 2 * mod.shift_cost(p) + heal

    def heal_reserve(self, me):
        """Mana kept for one heal cycle: a Rejuvenation, a Swiftmend and the shift back to Cat Form."""
        p, mod, sp = me.p, me.mod, me.mod.spells
        return mod.shift_cost(p) + sum(mod.mana_cost(sp[n]) for n in ("Rejuvenation", "Swiftmend") if n in sp)

    def cat_play(self, d, me, foe):
        t, p, mod, sp = d.t, me.p, me.mod, me.mod.spells
        if self.want_heal(d, me, foe) or foe.immune(t) and me.hp_frac() < 0.9 and self.want_heal_any(me):
            if not foe.immune(t) and self.bash_first(d, me, foe) and self.to_bear(d, me, "bash"):
                return None
            self.to_caster(d, me)   # a heal, or the foe's immunity (Ice Block, Divine Shield) spent healing
            return self.caster_play(d, me, foe)
        if foe.immune(t) or t < foe.immune_phys_until:
            return None   # no attacks into an immunity; energy pooled
        # a powershift out of a root, or a slow that keeps a kiting foe away, with the mana for a heal cycle kept
        rooted = t < me.root_until and me.root_until - t >= 1.5 and d.dist > T.MELEE + 0.5
        slowed = t < me.slow_until and me.slow >= 0.4 and me.slow_until - t >= 3.0 and d.dist > 8.0 and foe.intent == "kite"
        if (rooted or slowed) and not foe.controlled(t) and p.mana >= mod.shift_cost(p) + self.heal_reserve(me):
            mod.shift_out(me.fight)
            if self.to_cat(d, me):
                return None
        ng = sp.get("Nature's Grasp")
        if ng is not None and t >= self.grasp_until and self.melee_foe(foe) and d.dist <= 15.0 and p.mana >= 2 * mod.shift_cost(p) \
                and me.can("Nature's Grasp"):
            return "Nature's Grasp"
        return self.rotation(d, me, foe)

    def caster_play(self, d, me, foe):
        """Caster form: heal with the mana to shift back, root or Bash a melee foe first, then back to Cat Form."""
        t, p, mod, sp = d.t, me.p, me.mod, me.mod.spells
        hp = me.hp_frac()
        reserve = mod.shift_cost(p) if self.cat_build else 0.0
        near = self.physical_near(d, me, foe)
        kicks = near and self.foe_interrupt_ready(d, foe)   # a cast next to a free melee foe with its interrupt ready is lost

        def ok(n, extra=0.0):
            s = sp.get(n)
            return s is not None and me.can(n) and p.mana - mod.mana_cost(s) >= reserve + extra

        if p.buff("Nature's Swiftness", t) and ok("Healing Touch"):
            return "Healing Touch"
        immune = foe.immune(t)
        done = hp >= (max(self.heal_out, 0.9) if immune else self.heal_out)   # the foe's immunity is healing time
        rooted_foe = self.melee_foe(foe) and foe.body.rooted(t) and not foe.controlled(t)
        if not done:
            if near and t >= self.barkskin_until and "Barkskin" in sp and me.can("Barkskin"):
                return "Barkskin"
            if hp < 0.65 and (self.hot_on(me, "Rejuvenation") or self.hot_on(me, "Regrowth")) and ok("Swiftmend"):
                return "Swiftmend"
            if not self.hot_on(me, "Rejuvenation") and ok("Rejuvenation"):
                return "Rejuvenation"
            # a free melee foe in reach: root it (an interrupt it spends on the root leaves the next casts free)
            if near and not foe.body.rooted(t) and dr_factor(foe, cat("Entangling Roots"), t) >= 0.5 and not p.buff("Nature's Swiftness", t) \
                    and ok("Entangling Roots"):
                return "Entangling Roots"
            if rooted_foe and d.dist <= T.MELEE + 2.5:
                return None   # out of the rooted foe's reach first (intent kites), then the cast heals
            if not kicks:
                if hp < 0.75 and not self.hot_on(me, "Regrowth") and ok("Regrowth"):
                    return "Regrowth"
                if hp < 0.5 and ok("Healing Touch"):
                    return "Healing Touch"
            if p.mana < 0.35 * p.mana_max and (hp > 0.4 or not near) and "Innervate" in sp and me.can("Innervate"):
                return "Innervate"
        if self.ff_wanted(d, me, foe) and ok("Faerie Fire"):
            return "Faerie Fire"
        if not self.cat_build or immune and not done:
            return None
        # healed, or nothing more to do here: back to Cat Form (the heals over time keep running); without the mana, wait for it
        if done or near or not self.hot_on(me, "Rejuvenation") or hp >= self.heal_in:
            if self.to_cat(d, me):
                return None
        return None

    def bear_play(self, d, me, foe):
        t = d.t
        if self.bear_goal == "bash" and me.can("Bash") and dr_factor(foe, cat("Bash"), t) >= 0.5 and not foe.controlled(t):
            return "Bash"
        if self.bear_goal == "bash" and self.cat_charge is not None and 8.0 <= d.dist <= 25.0 and t >= me.root_until \
                and me.p.rage >= 5.0 and me.can("Feral Charge", ignore_gcd=True):
            return "Feral Charge"
        self.to_caster(d, me)   # the stun's window: heal in caster form (or back to Cat Form from there)
        return self.caster_play(d, me, foe)

    # Balance ------------------------------------------------------------------
    def balance_play(self, d, me, foe):
        t, p, mod, sp = d.t, me.p, me.mod, me.mod.spells
        hp = me.hp_frac()
        melee = self.melee_foe(foe)
        free = not foe.controlled(t) and not foe.body.rooted(t)
        if foe.immune(t):   # no spells into Ice Block or Divine Shield: the module's own heals only
            return self.rotation(d, me, foe, hide=("Wrath", "Starfire", "Moonfire", "Insect Swarm", "Hurricane", "Entangling Roots"))
        if self.ff_wanted(d, me, foe) and me.can("Faerie Fire"):
            return "Faerie Fire"
        if melee and d.dist <= T.MELEE + 0.5 and not foe.controlled(t) and hp < 0.8 and t >= self.barkskin_until and "Barkskin" in sp \
                and me.can("Barkskin"):
            return "Barkskin"
        keep = 2 * mod.mana_cost(sp["Starfire"]) if "Starfire" in sp else 0.0
        if t < me.root_until and me.root_until - t >= 1.5 and melee and free and d.dist <= 8.0 and mod.moonkin \
                and p.mana >= mod.moonkin_cost(p) + keep and self.to_moonkin(d, me):
            return None
        if melee and free and d.dist <= 8.0 and dr_factor(foe, cat("Entangling Roots"), t) >= 0.5 and not p.buff("Nature's Swiftness", t) \
                and me.can("Entangling Roots"):
            return "Entangling Roots"
        if p.mana < 0.3 * p.mana_max and "Innervate" in sp and me.can("Innervate"):
            return "Innervate"
        return self.rotation(d, me, foe)

    def rotation(self, d, me, foe, hide=()):
        """The spec's leveling rotation; the cat's openers stay hidden out of Prowl (Shred while the foe cannot face the druid), its
        Feral Charge too (this layer charges), locked spells, and `hide`; a shift the module makes into a form frees the druid of roots
        and slows."""
        t, mod, sp = d.t, me.mod, me.mod.spells
        hidden = {"Feral Charge"} | locked_spells(me, t) | set(hide)
        if self.cat_build:
            if not me.stealthed:
                hidden |= {"Ravage", "Pounce"}
                mod.opened = True
            if not me.behind(t):
                hidden.add("Shred")
        saved = {n: sp.pop(n) for n in hidden if n in sp}
        before = (mod.in_cat, getattr(mod, "in_moonkin", False))
        try:
            a = super().rotation(d, me, foe)
        finally:
            sp.update(saved)
        if (not before[0] and mod.in_cat) or (not before[1] and getattr(mod, "in_moonkin", False)):
            self.freed(d, me, "the shift")
        if a == "advance":
            return None   # the intent already closes; "advance" would hold it for 1 s and skip the per-step bookkeeping (_tick)
        return a
