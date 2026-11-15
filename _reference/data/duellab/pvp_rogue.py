"""Rogue PvP layer (duellab, 2026-11-14): a stealth approach and an opener (Sap out of combat, Premeditation, Cheap Shot, else Ambush
or Garrote), Kidney Shot as the combo-point stun, Kick, Gouge and Blind on casts, Evasion against melee, Sprint and Vanish when kited,
a Blind-Vanish reset when losing, Preparation, Crippling or Wound Poison. Damage (Sinister Strike, Mutilate, Hemorrhage, Eviscerate,
Slice and Dice, Shank, Seal Fate, Cold Blood) is the spec's own leveling rotation underneath (combat-swords-raid, combat-daggers-raid
or subtlety-leveling by the build's lead tree).

Effects the fight lab does not parse, or parses for PvE only (diminishing-returns categories always from dtables.DR_CATEGORY):
- Kidney Shot: a finisher, so the engine takes the combo points before this effect; it rolls the attack table (a miss, dodge or parry
  keeps the points, the module's on_miss) and stuns 2-6 s by the points spent (the tooltip's table), physical, in its own category
  (Classic Era's, dtables: not shared with Cheap Shot). Improved Kidney Shot's debuff and the finisher procs (Ruthlessness,
  Relentless Strikes) go through the module. The fight lab's own path set the stun through the mob view, outside Blessing of
  Protection and in the proc category.
- Cheap Shot: the fight lab's stun (4 s, 2 combo points, Initiative); it also ends the rogue's own Sap. No poison from Cheap Shot,
  Kidney Shot or Sap (they deal no damage; the module rolled its poisons on every landed strike).
- Gouge: 75 damage, then a 4 s incapacitate (+0.5 s a rank of Improved Gouge) that damage breaks, only on a foe facing the rogue
  (one not under control). The fight lab parses it as a 4 s stun.
- Blind: a 10 s disorient (no hit roll), broken by damage, 10 yards. Sap: a 45 s incapacitate (the engine's PvP cap: 10 s), only out
  of combat (the duel's first hostile hit), not on a druid in an animal form (Humanoids only), keeps stealth; Quick Getaway: +30%
  speed for 3 s. While the rogue's own Gouge, Blind or Sap holds, it does not swing or strike (energy pools) until its energy is
  nearly full or the control is about to end; nor into Ice Block, Divine Shield or Blessing of Protection.
- Kick: the interrupt (5 s school lockout) plus Improved Kick's silence (50% a rank, 2 s); the fight lab had the silence as extra
  lockout.
- Vanish: stealth again, roots and slows removed ("breaks movement impairing effects"), a hostile cast at the rogue broken, one step
  out of melee reach (see the assumptions); the next decision is a new opener. Not while Faerie Fire is on the rogue.
- Sprint: +70% speed for 15 s; Improved Sprint removes roots and slows (50% a rank). Endurance shortens its cooldown (the module
  applies it to Evasion only). Evasion: the module's +50% dodge for 15 s. Premeditation: 2 combo points. Preparation: every other
  rogue cooldown finished (its tooltip). Elusiveness and Dirty Tricks shorten Vanish and Blind, cheapen Blind and Sap.
- Riposte: armed for 5 s by the rogue's own parry (the duel reports it, Side.defend; the module armed it when the rogue's attack was
  parried, a PvE stand-in this layer undoes), the module's strike plus its 6 s disarm (the module only marked a debuff). Setup's
  combo point on a dodge comes through the same report. Ghostly Strike: +15% dodge for 7 s outside the Subtlety playstyle (the module
  applies it only there). Adrenaline Rush and Blade Flurry: pressed after the opener (the module presses them on a mob's pull).
- Poisons: the module's Instant Poison on the main hand and Crippling Poison (30% a hit, 70% slower for 12 s) on the off hand;
  Mutilate builds keep the module's Deadly Poison on the off hand (Mutilate's +20% against poisoned targets reads it) and carry
  Crippling Poison on the main hand. Against a class that heals itself (priest, paladin, shaman, druid) Wound Poison (30% a hit,
  15 s, 5 stacks) takes Crippling Poison's hand. Improved Poisons and Venom raise the chance.

Assumptions:
- Kidney Shot at 4+ combo points while it would last at least half (or at 2+ to stop a heal when Kick is down); while a stun runs out
  and Kidney Shot will be ready, finishers wait (the points go into the Kidney Shot as the stun ends).
- The opener is Cheap Shot while a stun lasts at least half, else Ambush (a dagger) or Garrote. Sap is used at the duel's start on a
  sappable foe; then Premeditation, Slice and Dice in stealth and the energy back before Cheap Shot (Classic's duel opener).
  Adrenaline Rush goes on in stealth right before the opener, Blade Flurry once the foe is not stunned (not into the stun's window).
- Spells that keep stealth: Premeditation, Sprint ("Does not break stealth"), Slice and Dice, Preparation, Adrenaline Rush, Sap,
  Vanish (Classic's behaviour; Forever unconfirmed). The engine drops stealth on every other cast, so these restore it.
- Off the global cooldown: Evasion, Sprint, Vanish, Premeditation, Cold Blood, Riposte (the engine's off-GCD list from the raid
  simulator's store). The engine then sets the global cooldown to "now", which would cut a running one short: these restore it.
- The engine lets auto attacks hit a stealthed target, so the stealthed rogue stops just outside melee reach and steps in with its
  opener, and Vanish steps out of reach (a foe cannot swing at what it cannot see).
- Two stealthers in one duel: side B leaves stealth within 12 yards (the engine has no stealth detection; else neither could act).
- Thresholds (judgment): Evasion below 65% health against a melee foe in reach; Blind then Vanish to reset below 45% health while the
  foe has 10 points more (not under Faerie Fire); Vanish to break a root of 2+ s at 10+ yards from a ranged foe; Sprint when slowed
  (or rooted, with Improved Sprint) or 12+ yards from a kiting foe. Measured and rejected (200 duels against pvp-frost, 2026-11-14):
  hanging back from a mage that kites at the rogue's speed to close on its next cast (combat-pvp 45.5% -> 16.5% wins, pvp-hemo-prep
  65.5% -> 50.5%); keeping Sprint for a root with Improved Sprint unless the mage is 26+ yards away (combat-pvp 45.5% -> 3%: a
  chilled rogue never catches a mage kiting at full speed).

Not modelled: Heightened Senses' spell and ranged avoidance, stealth detection (Master of Deception, Heightened Senses), Mind-numbing
Poison (the engine's cast slows would carry it; two weapons, two poisons: Crippling or Wound is kept), Distract, Feint, Expose Armor,
Cheat Death, bandages (no consumables), Garrote's silence (not in Forever's tooltip), Wound Poison's flat 165 a heal a stack (the
engine's 10% a stack), poison charges, Disarm's off hand (the engine stops both hands' swings; Shank still strikes).
"""
import dataclasses
import re

import dtables as T
import engine as FE
from pvp_base import PvPAI, HOSTILE, HEALS

STEALTH_SAFE = {"Premeditation", "Sprint", "Slice and Dice", "Preparation", "Adrenaline Rush"}   # restore stealth after the engine drops it
OFF_GCD = {"Evasion", "Sprint", "Vanish", "Premeditation", "Riposte"}         # the store's off_gcd list (Cold Blood: the module's own)
MY_CC = {"Gouge", "Blind", "Sap"}                                              # control that damage breaks: no attacks while it holds
NO_POISON = {"Cheap Shot", "Kidney Shot", "Sap"}                               # no damage, no poison
HEALERS = {"priest", "paladin", "shaman", "druid"}                             # classes that heal themselves: Wound Poison
FINISHERS = {"Eviscerate", "Slice and Dice", "Rupture", "Death Mark", "Expose Armor"}
CRIPPLING = re.compile(r"(\d+)% chance of poisoning the enemy, slowing their movement speed by (\d+)% for (\d+) sec")
WOUND = re.compile(r"(\d+)% chance of poisoning the enemy, reducing all healing effects.*? for (\d+) sec")


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


class RoguePvP(PvPAI):
    keep_range = 0.0
    auto_attack = True
    hostile_buffs = HOSTILE | {"Shank", "Mutilate", "Death Mark"}   # buff-kind strikes in the module: range-checked, not at a stealthed foe
    ranges = {"Blind": 10.0, "Sap": 5.0, "Shank": 5.0, "Mutilate": 5.0, "Death Mark": 20.0}
    KIDNEY_CP = 4
    EVASION_HP = 0.65
    RESET_HP = 0.45

    # ------------------------------------------------------------------ setup
    def bind(self, d, me):
        super().bind(d, me)
        self.auto_attack = True
        self.start_dist = d.dist
        self.my_cc = None                  # the breakable control this rogue holds on the foe (Gouge, Blind, Sap)
        self.reset_plan = False            # Blind then Vanish then a new opener
        self._gcd_before, self._was_stealthed = 0.0, False
        mod, sp = me.mod, me.mod.spells
        el = mod.tv("Elusiveness", 0)                       # "Reduces the cooldown of your Vanish and Blind abilities by 45 sec" a rank
        en = mod.tv("Endurance", 0) / 100                   # Sprint's half of Endurance (the module shortens Evasion)
        dt = mod.tv("Dirty Tricks", 0) / 100                # "Reduces the Energy cost of your Sap and Blind abilities by 25%" a rank
        for n in ("Vanish", "Blind", "Sprint", "Sap"):      # copies: the module's book is shared by every instance
            s = sp.get(n)
            if s is None:
                continue
            cd = s.cooldown - (el if n in ("Vanish", "Blind") else 0.0)
            cd *= (1 - en) if n == "Sprint" else 1.0
            cost = s.cost * ((1 - dt) if n in ("Blind", "Sap") else 1.0)
            sp[n] = dataclasses.replace(s, cooldown=max(0.0, cd), cost=cost)
        self.setup_poison(me)

    def setup_poison(self, me):
        """Crippling Poison (Wound Poison against a self-healer) on the hand the module's damage poison leaves free."""
        mod, foe = me.mod, me.foe
        name = "Wound Poison" if foe.cls in HEALERS else "Crippling Poison"
        src = mod.book.get(name)
        text = getattr(src, "text", "") or ""
        self.poison = None
        if name == "Crippling Poison" and CRIPPLING.search(text):
            m = CRIPPLING.search(text)
            self.poison, self.poison_chance, self.cripple, self.poison_dur = name, float(m.group(1)) / 100, float(m.group(2)) / 100, float(m.group(3))
        elif name == "Wound Poison" and WOUND.search(text):
            m = WOUND.search(text)
            self.poison, self.poison_chance, self.cripple, self.poison_dur = name, float(m.group(1)) / 100, 0.0, float(m.group(2))
        self.poison_hand = None
        if self.poison is not None and "Mutilate" in mod.spells:   # Mutilate reads the module's Deadly Poison (off hand): the PvP poison
            mod.spells.pop("Instant Poison", None)                  # replaces Instant Poison on the main hand
            self.poison_hand = "mh"
        elif self.poison is not None:
            mod.spells.pop("Deadly Poison", None)
            self.poison_hand = "oh"
        orig_swing, orig_parry = mod.on_swing, mod.on_parry
        self.riposte_until = 0.0

        def on_swing(fight, spell, outcome, amount, hand):   # the module's hook, then this layer's poison on landed hits of its hand
            if spell.name in NO_POISON:   # strikes that deal no damage apply no poison (the module's poisons hidden for the call)
                saved = {n: mod.spells.pop(n) for n in ("Instant Poison", "Deadly Poison") if n in mod.spells}
                try:
                    orig_swing(fight, spell, outcome, amount, hand)
                finally:
                    mod.spells.update(saved)
            else:
                orig_swing(fight, spell, outcome, amount, hand)
            if outcome == "parry" and fight.t >= self.riposte_until:
                fight.p.buffs.pop("Riposte", None)   # the module arms Riposte when the rogue's own attack is parried (its PvE stand-in)
            if outcome not in ("miss", "dodge", "parry") and hand == self.poison_hand and spell.name not in NO_POISON:
                self.apply_poison(me)

        def on_parry(fight):   # the duel reports the rogue's own parries (Side.defend): Riposte's real trigger
            orig_parry(fight)
            if "Riposte" in mod.spells:
                self.riposte_until = fight.t + 5.0
                fight.p.buffs["Riposte"] = {"until": self.riposte_until}

        mod.on_swing, mod.on_parry = on_swing, on_parry

    def apply_poison(self, me):
        foe, t, mod = me.foe, me.t, me.mod
        if t < foe.immune_until or t < foe.immune_phys_until or foe.p.hp <= 0:
            return
        chance = self.poison_chance + mod.tv("Improved Poisons", 0) / 100
        ven = me.p.buff("Venom", t)
        if ven:
            chance += ven.get("chance", 0.0)
        if me.fight.rng.random() >= chance:
            return
        if self.poison == "Crippling Poison":
            cur = foe.slow if t < foe.slow_until else 0.0
            foe.slow, foe.slow_until = max(cur, self.cripple), max(foe.slow_until, t + self.poison_dur)
            foe.debuffs["Crippling Poison"] = {"until": t + self.poison_dur, "stacks": 1}
        else:
            old = foe.debuffs.get("Wound Poison")
            n = old.get("stacks", 0) if old and old.get("until", 0) > t else 0
            foe.debuffs["Wound Poison"] = {"until": t + self.poison_dur, "stacks": min(T.WOUND_STACKS, n + 1)}

    def effects_for(self, me):
        e = {"Kidney Shot": self.kidney, "Cheap Shot": self.cheap_shot, "Gouge": self.gouge, "Blind": self.blind, "Sap": self.sap,
             "Kick": self.kick, "Vanish": self.vanish, "Sprint": self.sprint, "Evasion": self.plain, "Premeditation": self.premed,
             "Preparation": self.prep, "Slice and Dice": self.plain, "Riposte": self.riposte, "Adrenaline Rush": self.adrenaline,
             "Blade Flurry": self.flurry}
        if not me.mod.sub:   # the Subtlety playstyle's module applies Ghostly Strike's dodge itself
            e["Ghostly Strike"] = self.ghostly
        return e

    def prefight(self, d, me, foe):
        """Undo the module's mob pull (it stalks up to melee and presses Blade Flurry, Adrenaline Rush and, for Subtlety, Premeditation)
        and stand in stealth at the duel's distance with full energy (Poised: out of combat at full energy)."""
        p = me.p
        d.set_dist(self.start_dist)
        for n in ("Blade Flurry", "Adrenaline Rush"):
            if p.buffs.pop(n, None) is not None:
                p.cooldowns.pop(n, None)
        if me.mod.sub and p.cooldowns.pop("Premeditation", None) is not None:
            p.combo = 0
            me.fight.casts.pop("Premeditation", None)
        p.energy = p.energy_max
        if getattr(me.mod, "poised", 0) > 0:
            p.buffs["Poised"] = {"until": 1e18}
        me.stealthed = True

    # ------------------------------------------------------------------ helpers
    def _pre(self, me):
        self._gcd_before, self._was_stealthed = me.p.gcd_until, me.stealthed

    def _after(self, me, spell):
        """Off-GCD spells get their global cooldown back; stealth-safe spells their stealth."""
        if spell.name in OFF_GCD:
            me.p.gcd_until = self._gcd_before
        if spell.name in STEALTH_SAFE and self._was_stealthed:
            me.stealthed = True

    def _resolve(self, me, spell):
        """The fight lab's normal resolution of `spell` (the engine already counted the cast)."""
        amount = FE.Fight.resolve_spell(me.fight, spell)
        me.fight.casts[spell.name] = me.fight.casts.get(spell.name, 1) - 1
        return amount

    def _roll(self, me, spell):
        """The attack table for a strike that deals no damage: the outcome, a miss reported to the module."""
        f = me.fight
        out = f.attack_table(spell, False)
        f._blocked = False
        if out in ("miss", "dodge", "parry"):
            f.note(f"{spell.name} {out.upper()}")
            me.mod.on_swing(f, spell, out, 0.0, "mh")
            me.mod.on_miss(f, spell)
            return None
        return out

    def held_by_me(self, foe, t):
        return t < foe.incap_until and foe.incap_name in MY_CC and foe.incap_name == self.my_cc

    def sappable(self, foe):
        if foe.cls == "druid" and (getattr(foe.mod, "in_cat", False) or getattr(foe.mod, "in_moonkin", False) or getattr(foe.ai, "bear", False)):
            return False   # an animal form is a Beast
        return True

    def evis_kills(self, me, foe):
        ev = me.mod.spells.get("Eviscerate")
        cp = me.p.combo
        return ev is not None and cp > 0 and me.mod.evis_estimate(me.p, ev, cp) >= foe.p.hp

    def foe_immune(self, foe, t):
        return t < foe.immune_until or t < foe.immune_phys_until

    def ff_on(self, me):
        ff = me.debuffs.get("Faerie Fire")
        return bool(ff and ff.get("until", 0) > me.t)

    def kiting_foe(self, foe):
        return foe.ai.keep_range > 0 or foe.intent == "kite"

    # ------------------------------------------------------------------ effects
    def plain(self, d, me, foe, spell):
        amount = self._resolve(me, spell)
        if spell.name == "Evasion":
            me.fight.note("Evasion")   # the fight lab does not log a buff
        self._after(me, spell)
        return amount

    def cheap_shot(self, d, me, foe, spell):
        amount = self._resolve(me, spell)
        t = d.t
        if t < foe.stun_until and t < foe.incap_until and foe.incap_name == "Sap":
            foe.incap_until = t   # the stun replaces the rogue's own Sap
            self.my_cc = None
        return amount

    def kidney(self, d, me, foe, spell):
        f, t = me.fight, d.t
        if self._roll(me, spell) is None:
            return 0.0
        d.combat = True
        cp = max(1, min(5, f.last_combo))
        dur = getattr(spell, "stun_by_points", {}).get(cp, 1.0 + cp)
        got = foe.apply_cc("stun", dur, cat("Kidney Shot"), "Kidney Shot", physical=True)
        if got > 0:
            foe.debuffs["Kidney Shot"] = {"until": t + got, "stacks": 1}   # Improved Kidney Shot reads it
        me.mod.on_hit(f, spell, 0.0, False, False)                        # finisher procs: Ruthlessness, Relentless Strikes
        return 0.0

    def gouge(self, d, me, foe, spell):
        amount = self._resolve(me, dataclasses.replace(spell, stun=0.0))
        if amount <= 0 or foe.p.hp <= 0:
            return amount
        dur = (spell.stun or 4.0) + me.mod.tv("Improved Gouge", 0)
        if foe.apply_cc("incap", dur, cat("Gouge"), "Gouge", physical=True) > 0:
            self.my_cc = "Gouge"
            self.auto_attack = False
        return amount

    def blind(self, d, me, foe, spell):
        landed = foe.apply_cc("incap", 10.0, cat("Blind"), "Blind") > 0
        if landed:
            self.my_cc = "Blind"
            self.auto_attack = False
        self.reset_plan = self.reset_plan and landed
        d.combat = True
        return 0.0

    def sap(self, d, me, foe, spell):
        if d.combat or not self.sappable(foe):
            me.fight.note("Sap fails")
            return 0.0
        if foe.apply_cc("incap", 45.0, cat("Sap"), "Sap") > 0:
            self.my_cc = "Sap"
            self.auto_attack = False
            if me.mod.rank("Quick Getaway"):
                me.speed_bonus["Quick Getaway"] = (me.mod.tv("Quick Getaway", 1) / 100 or 0.3, d.t + 3.0)
        return 0.0

    def kick(self, d, me, foe, spell):
        t = d.t
        casting = foe.is_casting()
        amount = self._resolve(me, dataclasses.replace(spell, interrupt=0.0))
        if amount <= 0 or not casting or not foe.is_casting() or foe.immune(t):
            return amount
        foe.interrupt(spell.interrupt, "Kick")
        me.fight.interrupts += 1
        if me.mod.rank("Improved Kick") and me.fight.rng.random() < me.mod.tv("Improved Kick", 0) / 100:
            foe.apply_cc("silence", me.mod.tv("Improved Kick", 1) or 2.0, cat("Improved Kick"), "Improved Kick")
        return amount

    def vanish(self, d, me, foe, spell):
        t = d.t
        me.root_until = min(me.root_until, t)
        me.slow_until = min(me.slow_until, t)
        me.stealthed = True
        c = foe.cast_spell()
        if c is not None and c.kind not in ("heal", "buff") and c.target not in ("self", "pet"):
            foe.break_cast("target vanished")
        d.set_dist(max(d.dist, T.MELEE + 0.5))   # out of the foe's swing: it cannot attack what it cannot see
        self.reset_plan = False
        me.fight.note("Vanish")
        self._after(me, spell)
        return 0.0

    def sprint(self, d, me, foe, spell):
        t = d.t
        me.speed_bonus["Sprint"] = (0.7, t + 15.0)
        if me.mod.rank("Improved Sprint") and me.fight.rng.random() < me.mod.tv("Improved Sprint", 0) / 100:
            me.root_until = min(me.root_until, t)
            me.slow_until = min(me.slow_until, t)
        me.fight.note("Sprint")
        self._after(me, spell)
        return 0.0

    def premed(self, d, me, foe, spell):
        me.p.combo = min(5, me.p.combo + 2)
        me.fight.note("Premeditation: 2 combo points")
        self._after(me, spell)
        return 0.0

    def prep(self, d, me, foe, spell):
        p = me.p
        for n in list(p.cooldowns):
            if n != "Preparation" and n in me.mod.spells:
                p.cooldowns.pop(n, None)
        me.fight.note("Preparation: cooldowns finished")
        self._after(me, spell)
        return 0.0

    def riposte(self, d, me, foe, spell):
        self.riposte_until = 0.0   # spent: only a new parry arms it again
        amount = self._resolve(me, spell)
        if amount > 0 and foe.p.mh is not None:
            foe.apply_cc("disarm", 6.0, cat("Riposte"), "Riposte", physical=True)
        self._after(me, spell)
        return amount

    def ghostly(self, d, me, foe, spell):
        amount = self._resolve(me, spell)
        if amount > 0:
            me.dodge_buffs["Ghostly Strike"] = (0.15, d.t + 7.0)
        return amount

    def adrenaline(self, d, me, foe, spell):
        me.p.buffs["Adrenaline Rush"] = {"until": d.t + (me.mod.tv("Adrenaline Rush", 1) or 15.0)}
        me.fight.note("Adrenaline Rush")
        self._after(me, spell)
        return 0.0

    def flurry(self, d, me, foe, spell):
        me.p.buffs["Blade Flurry"] = {"until": d.t + (me.mod.tv("Blade Flurry", 1) or 15.0)}
        me.fight.note("Blade Flurry")
        return 0.0

    # ------------------------------------------------------------------ movement
    def intent(self, d, me, foe):
        """Every step: white swings stop while the foe sits in this rogue's breakable control or is immune; Camouflage's stealth speed."""
        t = d.t
        if self.my_cc and not self.held_by_me(foe, t):
            self.my_cc = None
        self.auto_attack = not (self.held_by_me(foe, t) or self.foe_immune(foe, t))
        if me.stealthed and me.mod.rank("Camouflage"):   # "Grants 5% increased movement speed in stealth" a rank
            me.speed_bonus["Camouflage"] = (me.mod.tv("Camouflage", 0) / 100, t + T.DT + 1e-6)
        if me.stealthed and foe.stealthed and me.name == "B" and d.dist <= 12.0:
            me.stealthed = False   # two stealthers: one shows itself (no stealth detection in the engine)
            me.fight.note("leaves stealth (both stealthed)")
        if foe.stealthed and not me.stealthed:
            return "hold"
        return "close"   # always (hanging back from a kiting mage was measured worse: see the docstring)

    def close_to(self, d, me):
        return T.MELEE + 0.4 if me.stealthed else T.MELEE - 0.5   # stealthed: just outside reach, then a step in with the opener

    # ------------------------------------------------------------------ decisions
    def off_gcd(self, d, me, foe):
        self._pre(me)
        t = d.t
        if foe.stealthed or me.stealthed:
            return None
        if self.reset_plan and self.held_by_me(foe, t) and foe.incap_name == "Blind" and self.vanish_ready(me) and not self.ff_on(me) \
                and me.can("Vanish", ignore_gcd=True):
            return "Vanish"   # the reset: Vanish under the Blind, then a new opener
        c = self.foe_cast(d, foe)
        if c is not None and d.dist <= T.MELEE + 0.5 and (c.kind == "heal" or c.name in HEALS or c.cast >= 1.0 or c.kind == "channel") \
                and not self.foe_immune(foe, t) and me.can("Kick"):
            return "Kick"
        melee = self.melee_foe(foe)
        if melee and d.dist <= T.MELEE + 1.0 and not foe.controlled(t) and me.hp_frac() < self.EVASION_HP \
                and not me.p.buff("Evasion", t) and me.can("Evasion", ignore_gcd=True):
            return "Evasion"
        if d.dist > T.MELEE + 1.0:
            rooted = t < me.root_until
            slowed = t < me.slow_until and me.slow >= 0.3
            # Sprint to catch a kiting foe or out of a slow; out of a root only with Improved Sprint's chance (see the docstring)
            frees = me.mod.rank("Improved Sprint") > 0
            chase = d.dist > 12.0 and self.kiting_foe(foe)
            if (rooted and frees and me.root_until - t >= 1.0 or not rooted and (slowed or chase)) \
                    and t >= me.speed_bonus.get("Sprint", (0, 0))[1] and me.can("Sprint", ignore_gcd=True):
                return "Sprint"
            if rooted and me.root_until - t >= 2.0 and d.dist > 10.0 and foe.ai.keep_range > 0 and not self.ff_on(me) \
                    and me.can("Vanish", ignore_gcd=True):
                return "Vanish"
        return None

    def decide(self, d, me, foe):
        self._pre(me)
        t, p = d.t, me.p
        if foe.stealthed:
            return None
        if me.stealthed:
            return self.stealth_play(d, me, foe)
        if self.my_cc and not self.held_by_me(foe, t):
            self.my_cc = None
        if self.held_by_me(foe, t):
            a = self.hold_cc(d, me, foe)
            if a != "resume":
                return a
        if self.foe_immune(foe, t):   # Ice Block, Divine Shield, Blessing of Protection: no attacks, energy pooled
            return None
        free = not foe.controlled(t)
        melee_reach = d.dist <= T.MELEE + 1e-6
        # the reset when losing: Blind, then Vanish under it (hold_cc), then a new opener
        if me.hp_frac() < self.RESET_HP and foe.hp_frac() > me.hp_frac() + 0.1 and free and not foe.dots and d.dist <= 10.0 \
                and me.can("Blind") and (self.vanish_ready(me) or self.prep_ready(me)) and not self.ff_on(me):
            self.reset_plan = True
            return "Blind"
        # interrupts that cost a global cooldown, when Kick cannot
        c = self.foe_cast(d, foe)
        if c is not None and free and (c.kind == "heal" or c.name in HEALS or c.cast >= 2.0) and not me.can("Kick"):
            if melee_reach and me.can("Gouge"):
                return "Gouge"
            if p.combo >= 2 and self.want_kidney(d, me, foe, interrupt=True):
                return "Kidney Shot"
            if (c.kind == "heal" or c.name in HEALS) and d.dist <= 10.0 and me.can("Blind"):
                return "Blind"
        if self.want_kidney(d, me, foe):
            return "Kidney Shot"
        # cooldowns after the opener (Adrenaline Rush goes on in stealth before it), not during a stun
        if melee_reach and foe.hp_frac() > 0.15:
            if (free or foe.stun_until - t < 1.0) and "Adrenaline Rush" in me.mod.spells and me.can("Adrenaline Rush"):
                return "Adrenaline Rush"
            if (free or foe.stun_until - t < 1.0) and "Blade Flurry" in me.mod.spells and me.can("Blade Flurry") and not p.buff("Blade Flurry", t):
                return "Blade Flurry"
            if not me.mod.sub and self.melee_foe(foe) and p.combo < 5 and t >= me.disarm_until and me.can("Ghostly Strike"):
                return "Ghostly Strike"
        if self.vanish_wanted_but_cd(d, me, foe) and me.can("Preparation"):
            return "Preparation"
        if self.reserving(d, me, foe):
            if p.combo >= 5 or not melee_reach:
                return None   # pool energy for the Kidney Shot as the stun ends
            a = self.rotation(d, me, foe, hide=FINISHERS)
            return a
        return self.rotation(d, me, foe)

    def stealth_play(self, d, me, foe):
        """Stealthed: walk in, Sap out of combat, Premeditation, Slice and Dice under a Sap, then step in with the opener."""
        t, p = d.t, me.p
        sp = me.mod.spells
        if d.dist > 20.0:
            return None
        if "Premeditation" in sp and p.combo <= 0 and me.can("Premeditation", ignore_gcd=True):
            return "Premeditation"
        if d.dist > T.MELEE + 0.5 + 1e-6:
            return None
        sapped = self.held_by_me(foe, t) and foe.incap_name == "Sap"
        if not d.combat and not sapped and not foe.controlled(t) and "Sap" in sp and self.sappable(foe) and dr_factor(foe, cat("Sap"), t) >= 1.0 \
                and p.ready("Sap", t) and me.fight.can_afford(sp["Sap"], me.mod.mana_cost(sp["Sap"])):
            return self.step_in(d, me, "Sap")
        if sapped:
            left = foe.incap_until - t
            snd = sp.get("Slice and Dice")
            if snd is not None and p.combo >= 1 and not p.buff("Slice and Dice", t) and left > 1.5 and me.can("Slice and Dice"):
                return "Slice and Dice"
            if p.energy < p.energy_max - 5 and left > 1.0:
                return None   # the energy back before the opener
        if self.held_by_me(foe, t) and foe.incap_name == "Blind":   # after the reset's Vanish: energy, and a full stun when it comes back in time
            left = foe.incap_until - t
            op = sp.get("Cheap Shot")
            need = (me.mod.mana_cost(op) if op else 60.0) + 25.0
            rec = foe.dr.get(cat("Cheap Shot"))
            reset_at = rec[1] + T.DR_RESET if rec else t
            wait_dr = dr_factor(foe, cat("Cheap Shot"), t) < 1.0 and reset_at < foe.incap_until - 0.5 and t < reset_at
            if (p.energy < min(need, p.energy_max - 5) or wait_dr) and left > 0.5:
                return None
        op = self.opener(d, me, foe)
        if op is None:
            return None
        if "Adrenaline Rush" in sp and me.can("Adrenaline Rush"):
            return "Adrenaline Rush"   # in stealth, right before the opener: the energy for the stun's window
        return self.step_in(d, me, op)

    def step_in(self, d, me, name):
        old = d.dist
        d.set_dist(min(d.dist, T.MELEE - 0.5))
        if not me.can(name):
            d.set_dist(old)
            return None
        return name

    def opener(self, d, me, foe):
        """Cheap Shot while a stun lasts at least half, else Ambush (a dagger in the main hand) or Garrote; None while pooling energy."""
        t, p, sp = d.t, me.p, me.mod.spells
        order = ["Cheap Shot", "Ambush", "Garrote"] if dr_factor(foe, cat("Cheap Shot"), t) >= 0.5 and not foe.immune(t) else ["Ambush", "Garrote", "Cheap Shot"]
        for n in order:
            s = sp.get(n)
            if s is None or not p.ready(n, t):
                continue
            if me.fight.can_afford(s, me.mod.mana_cost(s)):
                return n
            return None   # the first choice is known but short of energy: pool
        return None

    def hold_cc(self, d, me, foe):
        """The foe sits in this rogue's Gouge, Blind or Sap: no attacks; Vanish under a reset Blind; resume when the energy is back or the
        control is about to end ("resume")."""
        t, p = d.t, me.p
        self.auto_attack = False
        if self.reset_plan and foe.incap_name == "Blind":
            if self.vanish_ready(me) and not self.ff_on(me):
                return None   # off_gcd vanishes
            if not self.vanish_ready(me) and me.can("Preparation"):
                return "Preparation"
        left = foe.incap_until - t
        if p.energy >= p.energy_max - 10 or left < 0.6:
            foe.incap_until = t   # the next attack breaks it anyway
            self.my_cc = None
            self.auto_attack = True
            return "resume"
        return None

    def vanish_ready(self, me):
        return "Vanish" in me.mod.spells and me.p.ready("Vanish", me.t)

    def prep_ready(self, me):
        return "Preparation" in me.mod.spells and me.p.ready("Preparation", me.t)

    def vanish_wanted_but_cd(self, d, me, foe):
        """Preparation: Vanish is down and the rogue is losing or held at range."""
        if "Preparation" not in me.mod.spells or self.vanish_ready(me) or "Vanish" not in me.mod.spells:
            return False
        t = d.t
        kited = t < me.root_until and me.root_until - t >= 2.0 and d.dist > 10.0 and foe.ai.keep_range > 0
        losing = me.hp_frac() < self.RESET_HP and foe.hp_frac() > me.hp_frac() + 0.1 and not me.p.ready("Blind", t)
        return kited or losing

    def want_kidney(self, d, me, foe, interrupt=False):
        t, p = d.t, me.p
        if p.combo < 1 or "Kidney Shot" not in me.mod.spells or not me.can("Kidney Shot") or foe.immune(t) or t < foe.immune_phys_until:
            return False
        if dr_factor(foe, cat("Kidney Shot"), t) < 0.5:
            return False
        if t < foe.incap_until or t < foe.fear_until or foe.stun_until - t > 0.3:
            return False
        if self.evis_kills(me, foe):
            return False
        return interrupt or p.combo >= self.KIDNEY_CP

    def reserving(self, d, me, foe):
        """A stun runs out within 3 s and Kidney Shot will be ready with enough points: keep them for it."""
        t, p = d.t, me.p
        left = foe.stun_until - t
        if not (0.0 < left <= 3.0) or p.combo < self.KIDNEY_CP or "Kidney Shot" not in me.mod.spells:
            return False
        if p.cooldowns.get("Kidney Shot", -1.0) > foe.stun_until or dr_factor(foe, cat("Kidney Shot"), t) < 0.5:
            return False
        return not self.evis_kills(me, foe)

    def rotation(self, d, me, foe, hide=()):
        """The spec's leveling rotation with this layer's tools hidden from it: the openers out of stealth (Garrote and Ambush stay
        behind Ghostly Strike's opening), Kidney Shot, Evasion and Preparation (this layer decides them), and `hide`."""
        t = d.t
        sp = me.mod.spells
        hidden = {"Kidney Shot", "Evasion", "Preparation", "Cheap Shot", "Sap"} | set(hide)
        if t < me.disarm_until:
            hidden.add("Mutilate")   # both hands strike (the engine's disarm check misses the module's buff-kind wrapper); Shank is the off hand
        if not me.p.buff("Ghostly Opening", t):
            hidden |= {"Garrote", "Ambush"}
        elif not me.behind(t):
            hidden.add("Ambush")
        if not me.stealthed:
            me.mod.opened = True
        saved = {n: sp.pop(n) for n in hidden if n in sp}
        try:
            return super().rotation(d, me, foe)
        finally:
            sp.update(saved)
