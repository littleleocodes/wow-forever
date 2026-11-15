"""Priest PvP layer (duellab, 2026-11-14): Power Word: Shield on cooldown, Psychic Scream against a melee foe in reach, Silence on heals
and long casts (a Mind Flay channel is cut for it; never into Voice of Truth), offensive Dispel Magic on absorb shields, Shadow Word:
Death only when it should kill or the 30% backlash is safe, Mana Burn against a healing class (Shadow, in Mind Flay's place) or any mana
user (the healing trees), Shadow Word: Pain and Devouring Plague rested 15 s after the foe dispels one; the healing trees (Discipline,
Holy) also heal themselves: Renew, Penance on yourself, Flash Heal under pressure, Greater Heal in a safe window (the foe feared, stunned
or out of reach, or a shield against pushback, and no interrupt ready), Inner Focus and Power Infusion saved for those heals, Prayer of
Mending, the fear used to heal, 35% of the mana kept for heals (the wand does the damage below it). Damage (Shadow Word: Pain, Vampiric
Embrace, Devouring Plague, Mind Blast, Mind Flay and its slow, Smite, Holy Fire, offensive Penance, the wand) is the spec's own
leveling rotation underneath (shadow-dps, discipline-leveling, holy-leveling); each spec keeps its own play.

Effects the fight lab does not parse (handlers below): Silence (the talent's tooltip: 5 s silence and a 3 s school lockout of the cast it
interrupts), Mana Burn (746-788 mana drained, half of it as Shadow damage; Improved Mana Burn's -0.5 s a rank), Dispel Magic (on the foe:
its absorb shield and Blessing of Protection, then Power Infusion, Divine Favor, Arcane Power, Presence of Mind; on yourself: two magic
dots or Vampiric Embrace, then a magic root or slow), Abolish / Cure Disease (Devouring Plague), Inner Fire recast (charges back),
Inner Focus and Power Infusion as spells (the module spends them at the pull; healers keep them), Prayer of Mending on yourself (one heal
the next time you take damage: solo, it has no one to jump to), Fear Ward (cast during the countdown against a class with a fear), the
Penance heal on yourself ("Penance (heal)": 3 x 425 + 19% of spell power over the 2 s channel, sharing Penance's cooldown).
Psychic Scream is the fight lab's parsed fear (8 s), here limited to 8 yards. Talents with a PvP effect (each only when the build has it):
Silent Resolve (-5% a rank stun, fear and silence duration), Martyrdom (Focused Casting: 20% chance to resist an interrupt),
Spell Warding (-2% a rank spell damage taken), Divine Aegis (15% of a critical heal as an absorb, at most 1,200, 12 s),
Inspiration (+25% armor for 15 s after a critical heal), Improved Mana Burn, Shadow Reach and Holy Reach (ranges), Blackout from direct
Shadow spells only (the client's proc mask for every rank, SpellAuraOptions ProcTypeMask 87376 in build 70938, has no periodic-damage
bit; the fight lab also rolls it on Shadow Word: Pain, Devouring Plague and Mind Flay ticks, which here would stun every few seconds).

Assumptions: Shadowform stays up all duel (the fight lab's rule; leaving it to heal is not modelled), so Shadow casts no heals but
Power Word: Shield ("you may not cast healing spells", Forever's tooltip); Power Word: Shield and Fear Ward are cast during the
countdown; Penance can heal its caster (WotLK's rule; Forever's tooltip says "an ally"); Mana Burn's damage takes no damage modifiers;
dispels never miss; a slow is magic when the foe is a mage, priest, shaman or druid; Inspiration, Divine Aegis and Prayer of Mending
heal or absorb as their tooltips say, with one absorb pool shared with Power Word: Shield. Racial spells (Desperate Prayer, Chastise,
Divine Grace, Dark Sacrifice, Contingency Plan, Confounding Flash ...) are off (the fight lab's RACIAL_SPELLS, no racials in the lab).
Not modelled: Fade (useless one against one), Mind Control, Holy Nova, party-only effects (Holy Binding, Litany of Light, Spirit of
Redemption), Shadowguard and the other racials, mana potions.
"""
import copy
import re

import duel  # noqa: F401  (puts the fight lab first on sys.path: engine, tables and the class module are its copies)
import dtables as T
import engine as FE
import priest as PM
import tables as FT
from pvp_base import PvPAI, HEALS

# foe interrupts (and stuns or fears that break a cast) by reach in yards: a long heal waits while one is ready
INTERRUPTS = {"Counterspell": 30.0, "Pummel": 5.5, "Shield Bash": 5.5, "Kick": 5.5, "Earth Shock": 20.0, "Silence": 24.0,
              "Spell Lock": 30.0, "Hammer of Justice": 10.0, "Intimidating Shout": 10.0, "Repentance": 20.0}
HEALER_CLASSES = {"paladin", "priest", "druid", "shaman"}  # Shadow Mana Burns these: their mana is their heals
MAGIC_DOTS = {"Shadow Word: Pain", "Immolate", "Corruption", "Siphon Life", "Moonfire", "Insect Swarm", "Flame Shock", "Fireball",
              "Pyroblast", "Holy Fire", "Ignite"}
DISEASES = {"Devouring Plague"}
MAGIC_SLOW_CLASSES = {"mage", "priest", "shaman", "druid"}      # their slows are magic (Frostbolt, Mind Flay, Frost Shock ...)
NON_MAGIC_ROOTS = {"Improved Hamstring", "Entrapment", "Improved Wing Clip"}
FEAR_CLASSES = {"warrior", "warlock", "priest"}                   # Fear Ward is worth its countdown cast against these
PURGE_BUFFS = ("Power Infusion", "Divine Favor", "Arcane Power", "Presence of Mind")
HEALER_RESERVE = 0.35      # Discipline and Holy stop spending mana on damage below this share (heals keep it); an assumption
MY_DOTS = ("Shadow Word: Pain", "Devouring Plague", "Holy Fire")
RESTED_DOTS = ("Shadow Word: Pain", "Devouring Plague")   # held back for a while once the foe dispels one
DISPELLERS = {"paladin", "priest", "shaman", "druid"}      # classes that remove a dot from themselves (Cleanse, Dispel, Purify ...)
DAMAGE_SPELLS = ("Holy Fire", "Smite", "Mind Blast", "Shadow Word: Pain", "Devouring Plague", "Mind Flay", "Penance", "Mana Burn",
                 "Shadow Word: Death", "Holy Nova")
SELF_SPELLS = ("Inner Focus", "Power Infusion", "Prayer of Mending", "Fear Ward", "Abolish Disease", "Cure Disease")
SILENCE_RX = re.compile(r"casting spells for (\d+) sec and interrupting their spellcasts for (\d+) sec")
BURN_RX = re.compile(r"Drains (\d[\d,]*) to (\d[\d,]*) mana")
PENANCE_HEAL_RX = re.compile(r"or (\d[\d,]*) healing to an ally")
MENDING_RX = re.compile(r"heals them for (\d[\d,]*)")


def _num(s):
    return float(s.replace(",", ""))


def _trinket_wasted(me, t):
    """Whether the PvP trinket would leave me held: an incapacitate it does not break and damage does not end, or a stun or fear
    outside its list, running on for more than a second (pvp_base's rule trinkets when any part is freed)."""
    frees = me.trinket_frees(t)
    if not frees:
        return False
    rest = 0.0
    if t < me.incap_until and not me.incap_breaks and not (("polymorph" in frees and me.incap_name == "Polymorph")
                                                          or ("charm" in frees and me.incap_name in T.CHARM)):
        rest = max(rest, me.incap_until - t)   # an incapacitate damage breaks (Repentance, Sap, Blind) ends at the foe's next hit
    if t < me.stun_until and "stun" not in frees:
        rest = max(rest, me.stun_until - t)
    if t < me.fear_until and "fear" not in frees:
        rest = max(rest, me.fear_until - t)
    return rest > 1.0


class PriestPvP(PvPAI):
    auto_attack = False
    keep_range = 26.0

    def bind(self, d, me):
        super().bind(d, me)
        m = me.mod
        self.shadow = m.in_shadowform()
        self.healer = bool(getattr(m, "holy", False)) and not self.shadow
        self.fear_ward = False
        self.pom = None             # (heal, until): Prayer of Mending on yourself
        self.pom_pending = 0.0      # a mending heal to land on the next step (after the hit that triggered it)
        self.burn = (0.0, 0.0)
        self.inspired_until = 0.0
        self.dot_seen, self.dot_rest = {}, {}
        self.persistent_veto = {}
        reach = 1 + m.tv("Shadow Reach", 0) / 100
        holy_reach = 1 + m.tv("Holy Reach", 0) / 100
        self.ranges = {"Psychic Scream": 8.0, "Penance": 30.0}
        for n in ("Mind Blast", "Shadow Word: Pain", "Shadow Word: Death", "Vampiric Embrace", "Devouring Plague", "Mana Burn", "Silence"):
            s = m.spells.get(n)
            if s is not None:
                self.ranges[n] = (s.range or 30.0) * reach
        for n in ("Smite", "Holy Fire"):
            s = m.spells.get(n)
            if s is not None:
                self.ranges[n] = (s.range or 30.0) * holy_reach
        if "Mind Flay" in m.spells:
            self.ranges["Mind Flay"] = m.flay_range(m.spells["Mind Flay"])
        # hold where the rotation's main spells reach (Mind Flay for Shadow, Smite / Penance / Mind Blast for the healers)
        if self.shadow and "Mind Flay" in self.ranges:
            self.keep_range = self.ranges["Mind Flay"] - 2.0
        else:
            self.keep_range = min(self.ranges.get(n, 30.0) for n in ("Smite", "Mind Blast", "Penance")) - 2.0
        # the other school when an interrupt locks the rotation's (Smite is no healing spell: Shadowform allows it in Forever)
        self.fillers = ("Smite",) if self.shadow else ("Mind Blast", "Mind Flay", "Smite")
        # spells cast on yourself: a copy with target "self" (the data's range is the friendly one)
        for n in SELF_SPELLS:
            s = m.spells.get(n)
            if s is not None:
                c = copy.copy(s)
                c.target = "self"
                m.spells[n] = c
        dm = m.spells.get("Dispel Magic")
        if dm is not None:
            c = copy.copy(dm)
            c.target = "self"
            m.spells["Dispel Magic (self)"] = c
        mb = m.spells.get("Mana Burn")
        if mb is not None:
            c = copy.copy(mb)
            c.cast = max(0.0, mb.cast - m.tv("Improved Mana Burn", 0))
            mm = BURN_RX.search(mb.text or "")
            self.burn = (_num(mm.group(1)), _num(mm.group(2))) if mm else (0.0, 0.0)
            m.spells["Mana Burn"] = c
        sil = m.spells.get("Silence")
        sm = SILENCE_RX.search(getattr(sil, "text", "") or "") if sil is not None else None
        self.silence_secs = (float(sm.group(1)), float(sm.group(2))) if sm else (5.0, 3.0)
        pen = m.spells.get("Penance")
        if pen is not None and not self.shadow:
            pm = PENANCE_HEAL_RX.search(pen.text or "")
            if pm:
                c = copy.copy(pen)           # name stays "Penance": one cooldown for both uses
                c.kind, c.target = "channel", "self"
                c.dot, c.dmg_min, c.dmg_max = 0.0, 0.0, 0.0
                c.hot, c.heal_coef = 3 * _num(pm.group(1)), pen.dot_coef
                c.dot_ticks, c.channel = 3, 2.0
                m.spells["Penance (heal)"] = c
        pom = m.spells.get("Prayer of Mending")
        mm = MENDING_RX.search(getattr(pom, "text", "") or "") if pom is not None else None
        self.mending = _num(mm.group(1)) if mm else 0.0
        self._wrap(me)

    # ------------------------------------------------------------------ wrappers on this side's own objects (engine gaps)
    def _wrap(self, me):
        m, ai = me.mod, self
        apply_cc = me.apply_cc

        def cc(kind, dur, cat, name, frozen=False, breaks=None, physical=False):
            """Silent Resolve shortens stuns, fears and silences; Fear Ward eats the next fear."""
            t = me.t
            if kind == "fear" and name not in T.HORROR and ai.fear_ward and t >= me.immune_until:   # Death Coil's horror is no fear
                ai.fear_ward = False
                me.fight.note(f"Fear Ward absorbs {name or 'fear'}")
                return 0.0
            if kind in ("stun", "fear", "silence") and m.rank("Silent Resolve"):
                dur *= 1 - m.tv("Silent Resolve", 1) / 100
            return apply_cc(kind, dur, cat, name, frozen=frozen, breaks=breaks, physical=physical)
        me.apply_cc = cc

        interrupt = me.interrupt

        def intr(lock, by):
            """Martyrdom's Focused Casting: 20% resistance to interrupts."""
            if m.rank("Martyrdom") and me.p.buff("Focused Casting", me.t) and me.fight.rng.random() < m.tv("Martyrdom", 2) / 100:
                me.fight.note(f"{by} resisted (Focused Casting)")
                return
            interrupt(lock, by)
        me.interrupt = intr

        if m.rank("Divine Aegis") or m.rank("Inspiration"):
            heal = me.fight.heal

            def healed(spell, amount, target="player", crit=False):
                got = heal(spell, amount, target, crit)
                if crit and target != "pet" and got > 0:
                    t = me.t
                    if m.rank("Divine Aegis"):
                        cap = m.tv("Divine Aegis", 1) or 1200.0
                        a = min(cap, got * m.tv("Divine Aegis", 0) / 100)
                        live = me.p.absorb if t < me.p.absorb_until else 0.0
                        me.p.absorb = live + a   # one absorb pool with Power Word: Shield (an assumption)
                        me.p.absorb_until = max(me.p.absorb_until if live > 0 else 0.0, t + (m.tv("Divine Aegis", 2) or 12.0))
                        me.fight.note(f"Divine Aegis {a:.0f}")
                    if m.rank("Inspiration"):
                        ai.inspired_until = t + (m.tv("Inspiration", 1) or 15.0)
                return got
            me.fight.heal = healed

        on_hit = m.on_hit

        def hit(fight, spell, amount, crit, frozen):
            """Remember when my dot should end, so a dispel that removes it in the same step is still seen (_step)."""
            on_hit(fight, spell, amount, crit, frozen)
            if spell.name in MY_DOTS and spell.dot > 0:
                ai.dot_seen[spell.name] = me.t + (spell.dot_dur or 15.0)
        m.on_hit = hit

        if m.rank("Blackout"):
            on_tick = m.on_tick

            def tick(fight, spell, amount, crit):
                """Blackout procs from direct Shadow spells only: the client's proc mask for every rank (SpellAuraOptions 15268-15326,
                ProcTypeMask 87376, build 70938) holds harmful spells and abilities but not periodic damage (0x40000), so Shadow Word:
                Pain, Devouring Plague and Mind Flay ticks do not stun. The fight lab's shadow_hit rolls it on ticks too: the talent
                is taken out of the tick's roll here (Shadow Weaving and the heals stay)."""
                ranks = m.t.pop("Blackout", None)
                try:
                    on_tick(fight, spell, amount, crit)
                finally:
                    if ranks:
                        m.t["Blackout"] = ranks
            m.on_tick = tick

        if m.rank("Inspiration"):
            armor_bonus = m.armor_bonus

            def armor():
                b = armor_bonus()
                if me.t < ai.inspired_until:
                    b += me.p.armor * m.tv("Inspiration", 0) / 100
                return b
            m.armor_bonus = armor

    # ------------------------------------------------------------------ effects
    def effects_for(self, me):
        return {"Silence": self.silence, "Mana Burn": self.mana_burn, "Dispel Magic": self.dispel, "Inner Fire": self.inner_fire,
                "Inner Focus": self.inner_focus, "Power Infusion": self.power_infusion, "Prayer of Mending": self.prayer_of_mending,
                "Abolish Disease": self.cure, "Cure Disease": self.cure, "Fear Ward": self.ward}

    def _lands(self, me, spell):
        """A spell's hit roll against a same-level player (the fight lab's spell table)."""
        if spell.name in FE.NO_MISS:
            return True
        hit = 1.0 - FT.spell_miss(0) + me.mod.hit_bonus(spell) + me.p.spell_hit
        return me.fight.rng.random() <= min(FT.SPELL_HIT_CAP, hit)

    def silence(self, d, me, foe, spell):
        if foe.immune(d.t) or not self._lands(me, spell):
            me.fight.note(f"Silence {'immune' if foe.immune(d.t) else 'MISS'}")
            return 0.0
        secs, lock = self.silence_secs
        if foe.is_casting():
            foe.interrupt(lock, "Silence")
            me.fight.interrupts += 1
        foe.apply_cc("silence", secs, "silence", "Silence")
        return 0.0

    def mana_burn(self, d, me, foe, spell):
        if foe.immune(d.t) or foe.p.mana_max <= 0:
            me.fight.note("Mana Burn immune")
            return 0.0
        if not self._lands(me, spell):
            me.fight.note("Mana Burn MISS")
            return 0.0
        drained = min(foe.p.mana, me.fight.rng.uniform(*self.burn))
        foe.p.mana -= drained
        me.fight.note(f"Mana Burn drains {drained:.0f} mana")
        dmg = 0.5 * drained
        if dmg > 0:
            me.fight.deal(spell, dmg)
            me.mod.on_hit(me.fight, spell, dmg, False, False)   # a Shadow hit: Shadow Weaving, Blackout, Vampiric Embrace
        return dmg

    def dispel(self, d, me, foe, spell):
        t, out = d.t, []
        if spell.target == "self":
            mine = sorted((x for x in me.dots if x[0] in MAGIC_DOTS), key=lambda x: -x[1] * x[2])
            for dot in mine[:2]:
                me.dots.remove(dot)
                out.append(dot[0])
            ve = me.debuffs.get("Vampiric Embrace")
            if len(out) < 2 and ve and ve.get("until", 0) > t:
                me.debuffs.pop("Vampiric Embrace")
                out.append("Vampiric Embrace")
            if len(out) < 2 and t < me.root_until and me.root_name not in NON_MAGIC_ROOTS:
                out += me.dispel_cc(kinds=("root",))
            if len(out) < 2 and t < me.slow_until and foe.cls in MAGIC_SLOW_CLASSES:
                out += me.dispel_cc(kinds=("slow",))
            me.fight.note(f"Dispel Magic on yourself: {', '.join(out) or 'nothing'}")
            return 0.0
        if foe.immune(t):
            me.fight.note("Dispel Magic immune")
            return 0.0
        if foe.p.absorb > 0 and t < foe.p.absorb_until:
            foe.purge_shields()
            out.append("absorb")
        if t < foe.immune_phys_until:
            foe.immune_phys_until = t
            out.append("Blessing of Protection")
        for name in PURGE_BUFFS:
            if len(out) < 2 and foe.p.buff(name, t):
                foe.p.buffs.pop(name, None)
                out.append(name)
        me.fight.note(f"Dispel Magic on {foe.name}: {', '.join(out) or 'nothing'}")
        return 0.0

    def inner_fire(self, d, me, foe, spell):
        me.p.buffs["Inner Fire"] = {"until": 1e18, "charges": me.mod.inner_fire_charges}
        return 0.0

    def inner_focus(self, d, me, foe, spell):
        me.p.buffs["Inner Focus"] = {"until": d.t + 30.0}
        return 0.0

    def power_infusion(self, d, me, foe, spell):
        me.p.buffs["Power Infusion"] = {"until": d.t + 15.0}
        return 0.0

    def prayer_of_mending(self, d, me, foe, spell):
        heal = self.mending * me.mod.heal_multiplier(spell)
        self.pom = (heal, d.t + 30.0)
        me.fight.note(f"Prayer of Mending on yourself ({heal:.0f})")
        return 0.0

    def cure(self, d, me, foe, spell):
        for dot in [x for x in me.dots if x[0] in DISEASES][:1]:
            me.dots.remove(dot)
            me.fight.note(f"{spell.name}: {dot[0]} removed")
        return 0.0

    def ward(self, d, me, foe, spell):
        self.fear_ward = True
        return 0.0

    # ------------------------------------------------------------------ helpers
    def _dr_next(self, side, cat, t):
        """The duration factor the next control of category `cat` gets on `side` (1, 0.5, 0.25, 0: immune)."""
        rec = side.dr.get(cat)
        n = rec[0] if rec and t < rec[1] + T.DR_RESET else 0
        return T.DR_STEPS[min(n, len(T.DR_STEPS) - 1)]

    def _kick_ready(self, d, foe, within=0.0):
        """Whether the foe has an interrupt (or a cast-breaking stun or fear) ready now or within `within` seconds, in reach."""
        t = d.t
        if max(max(foe.stun_until, foe.incap_until, foe.fear_until), foe.inactive_until) - t >= within:
            return False   # held for the whole cast
        for name, reach in INTERRUPTS.items():
            s = foe.mod.spells.get(name)
            if s is None or d.dist > reach:
                continue
            if foe.silenced(t) and s.kind not in ("melee", "ranged") and foe.silence_until >= t + within:
                continue
            if foe.p.ready(name, t + within):
                return True
        return False

    def _safe(self, d, me, foe, cast):
        """Whether a cast of `cast` seconds can finish: the foe controlled for all of it, or no interrupt ready and a melee foe still
        out of reach for most of it."""
        t = d.t
        left = max(foe.stun_until, foe.incap_until, foe.fear_until) - t
        if left >= cast + 0.1:
            return True
        if t < foe.inactive_until:
            return True
        if self._kick_ready(d, foe, cast):
            return False
        if self.melee_foe(foe):
            if d.dist <= T.MELEE + 0.5:
                # in reach: only Power Word: Shield keeps the cast from being pushed back ("while the shield holds, spellcasting
                # will not be interrupted by damage")
                return me.p.absorb >= 300.0 and t < me.p.absorb_until
            sp = foe.speed(t)
            reach = (d.dist - T.MELEE) / sp if sp > 0 else (foe.root_until - t if t < foe.root_until else 99.0)
            return reach >= 0.6 * cast
        return True

    def _cast_free(self, me, name):
        """Cast an off-global-cooldown spell (Inner Focus, Power Infusion: the client's off-GCD list) without starting the GCD."""
        gcd = me.p.gcd_until
        me.cast(name)
        me.p.gcd_until = gcd

    def _focus(self, d, me, burst=False):
        """Inner Focus (and Power Infusion) right before a big heal: free and +25% crit, +20% healing."""
        t = d.t
        if me.can("Inner Focus", ignore_gcd=True) and not me.p.buff("Inner Focus", t):
            self._cast_free(me, "Inner Focus")
        if me.can("Power Infusion", ignore_gcd=True) and not me.p.buff("Power Infusion", t):
            self._cast_free(me, "Power Infusion")

    def _shielded(self, me, t):
        return me.p.absorb > 0 and t < me.p.absorb_until

    def _heal_spell(self, me, name):
        return name if me.can(name) else None

    # ------------------------------------------------------------------ per step
    def _step(self, d, me, foe):
        t = d.t
        if self.pom_pending > 0:
            got = me.fight.heal(FE.Spell("Prayer of Mending", "holy"), self.pom_pending)
            me.fight.note(f"Prayer of Mending heals {got:.0f}")
            self.pom_pending = 0.0
        # my dots the foe dispels: one that vanishes with ticks left was removed (Cleanse, Dispel Magic, a cure). Shadow Word: Pain
        # and Devouring Plague both rest 15 s after each removal (re-dotting into every Cleanse spends a global cooldown and mana each
        # time for nothing; Devouring Plague costs 985 mana without Devouring Contagion); Holy Fire's direct hit is its value
        live = {x[0]: x[3] + (x[2] - 1) * x[4] for x in foe.dots if x[0] in MY_DOTS}
        for name, end in self.dot_seen.items():
            if name not in live and end - t > 1.0 and foe.cls in DISPELLERS and name in RESTED_DOTS:
                for n in RESTED_DOTS:
                    self.dot_rest[n] = t + 15.0
                me.fight.note(f"{name} dispelled: dots held for 15 s")
        self.dot_seen = live

    def damage_taken(self, d, me, src, spell, amount):
        sw = me.mod.tv("Spell Warding", 0)
        school = getattr(spell, "school", None) or "physical"
        if sw and amount > 0 and school != "physical" and getattr(spell, "kind", "") not in ("melee", "ranged"):
            amount *= 1 - sw / 100
        if amount > 0 and self.pom is not None:
            if d.t < self.pom[1]:
                self.pom_pending += self.pom[0]
            self.pom = None
        return amount

    # ------------------------------------------------------------------ hooks
    def prefight(self, d, me, foe):
        """The countdown: Power Word: Shield (and Fear Ward against a fear class); healers keep Inner Focus and Power Infusion (the module
        spends them at the pull) for their heals."""
        p, m, t = me.p, me.mod, d.t
        pws = m.spells.get("Power Word: Shield")
        if pws is not None and p.ready("Power Word: Shield", t) and not self._shielded(me, t):
            m.cast_shield(me.fight, pws)
        fw = m.spells.get("Fear Ward")
        if fw is not None and foe.cls in FEAR_CLASSES and p.ready("Fear Ward", t):
            p.mana -= m.mana_cost(fw)
            p.cooldowns["Fear Ward"] = t + fw.cooldown
            self.fear_ward = True
            me.fight.note("Fear Ward")
        if self.healer:
            if p.buffs.pop("Inner Focus", None) is not None:
                p.cooldowns["Inner Focus"] = t
            if p.buffs.pop("Power Infusion", None) is not None:
                p.cooldowns["Power Infusion"] = t
                p.mana = min(p.mana_max, p.mana + m.mana_cost(m.spells["Power Infusion"]))
                me.fight.casts["Power Infusion"] = max(0, me.fight.casts.get("Power Infusion", 1) - 1)

    def intent(self, d, me, foe):
        t = d.t
        if foe.stealthed:
            return "hold"
        if self.melee_foe(foe):
            stuck = foe.controlled(t) or foe.body.rooted(t)
            if stuck and d.dist < min(self.keep_range, 18.0):
                return "kite"   # walk out of reach during the global cooldowns while it cannot follow
            return "close" if d.dist > self.keep_range + 4.0 else "hold"
        return super().intent(d, me, foe)

    def while_controlled(self, d, me, foe):
        """The base trinket rule, except when a control the trinket cannot break (Repentance, Sap, Blind) would still hold me."""
        self._step(d, me, foe)
        if _trinket_wasted(me, d.t):
            return None
        return super().while_controlled(d, me, foe)

    def while_inactive(self, d, me, foe):
        self._step(d, me, foe)
        return None

    def while_casting(self, d, me, foe):
        """A Mind Flay channel is cut short to Silence a heal or a long cast (players do that)."""
        self._step(d, me, foe)
        s, t = me.cast_spell(), d.t
        if s is not None and s.kind == "channel" and s.name == "Mind Flay" and "Silence" in me.mod.spells \
                and me.p.ready("Silence", t) and t + FE.EPS >= me.p.gcd_until:
            c = self.foe_cast(d, foe)
            if c is not None and self._silence_worth(c, foe) and d.dist <= self.ranges.get("Silence", 20.0) and not foe.immune(t):
                me.break_cast("Silence")
                if me.can("Silence"):
                    return "Silence"
        return None

    def off_gcd(self, d, me, foe):
        self._step(d, me, foe)
        return None

    def _silence_worth(self, c, foe):
        if foe.t < getattr(foe.ai, "vot_until", 0.0):
            return False   # a paladin's Voice of Truth (a visible buff) makes it immune
        heals = any(n in foe.mod.spells for n in HEALS)
        if c.kind == "heal" or c.name in HEALS:
            return True
        return not heals and (foe.mod.cast_time(c) >= 1.5 or c.kind == "channel")

    def decide(self, d, me, foe):
        t = d.t
        if foe.stealthed:
            return "Power Word: Shield" if self._shield_ok(d, me) else None
        hp = me.hp_frac()
        # 1. a melee foe next to me: Psychic Scream
        a = self._scream(d, me, foe)
        if a:
            return a
        # 2. Silence a heal or a long cast (a charged Grounding Totem is popped with a cheap instant first)
        c = self.foe_cast(d, foe)
        if c is not None and me.can("Silence") and self._silence_worth(c, foe) and not foe.immune(t):
            return self._ground_pop(d, me, foe) or "Silence"
        # 3. Power Word: Shield on cooldown
        if self._shield_ok(d, me):
            return "Power Word: Shield"
        # 4. heals (Discipline, Holy)
        a = self._heal(d, me, foe)
        if a:
            return a
        # 5. dispels: the foe's absorb shield, magic on me
        a = self._dispel(d, me, foe)
        if a:
            return a
        if foe.immune(t):
            # Ice Block, Divine Shield: nothing lands; top up instead
            if not self.shadow and hp < 0.95 and me.can("Renew") and not any(h[0] == "Renew" for h in me.p.hots):
                return "Renew"
            if not self.shadow and hp < 0.8:
                for n in ("Greater Heal", "Flash Heal"):
                    if me.can(n):
                        return n
            return None
        # 6. a healer uses the fear to heal (damage would break it); with nothing to heal with, or the foe nearly dead, it attacks
        if self.healer and t < foe.fear_until and hp < 0.85 and foe.hp_frac() > 0.25:
            a = self._top_up(d, me, foe)
            if a:
                return a
        # 7. Mana Burn: the healing trees against a mana user, Shadow against a class that heals
        a = self._burn(d, me, foe)
        if a:
            return self._ground_pop(d, me, foe) or a
        # 8. Inner Fire back on when its charges are gone
        b = me.p.buffs.get("Inner Fire")
        if self.melee_foe(foe) and (b is None or b.get("charges", 0) <= 0) and me.can("Inner Fire") and hp > 0.5:
            return "Inner Fire"
        # 9. Power Infusion (off the global cooldown) for the kill when no heal needed it: the foe below 60%, mana to spend
        if foe.hp_frac() < 0.6 and me.mana_frac() > 0.35 and me.can("Power Infusion", ignore_gcd=True) \
                and not me.p.buff("Power Infusion", t):
            self._cast_free(me, "Power Infusion")
        return self._rotation(d, me, foe)

    # ------------------------------------------------------------------ decisions
    def _ground_pop(self, d, me, foe):
        """A charged Grounding Totem (pvp_base.grounding) takes the next spell cast at the foe: a cheap instant pops it first."""
        if not foe.ai.grounding(d, foe):
            return None
        for n in ("Shadow Word: Pain", "Mind Blast"):
            if me.can(n):
                return n
        return None

    def _shield_ok(self, d, me):
        t = d.t
        if self._shielded(me, t) or not me.can("Power Word: Shield"):
            return False
        return d.combat or d.dist <= 30.0

    def _scream(self, d, me, foe):
        t = d.t
        if not me.can("Psychic Scream") or d.dist > self.ranges["Psychic Scream"] or foe.controlled(t) or foe.immune(t) \
                or t < foe.fear_immune_until or self._dr_next(foe, "fear", t) < 0.5:
            return None
        c = foe.cast_spell()
        if self.melee_foe(foe) or (c is not None and (c.kind == "heal" or foe.mod.cast_time(c) >= 1.5)):
            return "Psychic Scream"
        return None

    def _heal(self, d, me, foe):
        """Discipline and Holy: Renew, Penance, Flash Heal and Greater Heal by health and the foe's threat."""
        if not self.healer:
            return None
        p, t = me.p, d.t
        hp = me.hp_frac()
        if hp >= 0.92:
            return None
        renew_up = any(h[0] == "Renew" for h in p.hots)
        renew = "Renew" if not renew_up and me.can("Renew") else None
        pen = "Penance (heal)" if me.can("Penance (heal)") else None
        fh = self._heal_spell(me, "Flash Heal")
        gh = self._heal_spell(me, "Greater Heal") or self._heal_spell(me, "Heal")
        gh_t = me.mod.cast_time(me.mod.spells[gh]) if gh else 99.0
        safe_gh = gh is not None and self._safe(d, me, foe, gh_t)
        safe_fh = fh is not None and self._safe(d, me, foe, me.mod.cast_time(me.mod.spells["Flash Heal"]))
        if hp < 0.35:
            if pen:
                return pen
            if safe_gh:
                self._focus(d, me)
                return gh
            if fh and (safe_fh or not self._kick_ready(d, foe)):
                self._focus(d, me)
                return fh
            if renew:
                return renew
            return fh
        if hp < 0.6:
            if renew and d.combat:
                return renew
            if pen:
                return pen
            if safe_gh:
                if hp < 0.45:
                    self._focus(d, me)
                return gh
            if hp < 0.5 and safe_fh:
                return fh
        if hp < 0.85 and d.combat:
            if renew:
                return renew
            if safe_gh and hp < 0.7 and max(foe.stun_until, foe.incap_until, foe.fear_until) - t >= gh_t:
                return gh
            if self.pom is None and me.can("Prayer of Mending") and me.mana_frac() > 0.5:   # 390 mana for one 413 heal solo
                return "Prayer of Mending"
        return None

    def _top_up(self, d, me, foe):
        """While my fear holds a melee foe: heal without breaking it, else wait (or wand from range would break it too)."""
        a = self._heal(d, me, foe)
        if a:
            return a
        t = d.t
        hp = me.hp_frac()
        for n in ("Greater Heal", "Heal", "Flash Heal"):
            if me.can(n) and self._safe(d, me, foe, me.mod.cast_time(me.mod.spells[n])) and hp < 0.85:
                return n
        return None

    def _dispel(self, d, me, foe):
        t = d.t
        if me.can("Dispel Magic") and not foe.immune(t):
            absorb = foe.p.absorb if t < foe.p.absorb_until else 0.0
            if absorb >= 300.0 or (t < foe.immune_phys_until and me.mana_frac() > 0.2):
                return self._ground_pop(d, me, foe) or "Dispel Magic"
        if me.can("Dispel Magic (self)"):
            bad = sum(x[1] * x[2] for x in me.dots if x[0] in MAGIC_DOTS)
            ve = me.debuffs.get("Vampiric Embrace")
            if ve and ve.get("until", 0) > t:
                bad += 300.0
            if bad >= 500.0 and me.hp_frac() < 0.9:
                return "Dispel Magic (self)"
        if any(x[0] in DISEASES and x[1] * x[2] >= 300.0 for x in me.dots):
            for n in ("Abolish Disease", "Cure Disease"):
                if me.can(n):
                    return n
        return None

    def _saving(self, me, foe):
        """A healer below its mana reserve keeps the rest for heals, unless the foe is nearly dead."""
        return me.mana_frac() < HEALER_RESERVE and foe.hp_frac() > 0.25

    def _burn(self, d, me, foe):
        """Mana Burn against a mana user with mana left, when the cast can finish: the healing trees against any mana user, Shadow
        against a class that heals (its mana is its heals; Mind Flay would deal more damage now)."""
        if foe.p.mana_max <= 0 or not me.can("Mana Burn"):
            return None
        if self.shadow and (foe.cls not in HEALER_CLASSES or foe.mana_frac() < 0.25 or foe.hp_frac() < 0.4
                            or me.can("Mind Blast")):
            return None   # Shadow: Mind Blast first; Mana Burn takes Mind Flay's place
        if not self.shadow and not self.healer:
            return None
        if foe.mana_frac() < 0.10 or (self.healer and self._saving(me, foe)) or me.hp_frac() < 0.6:
            return None
        if not self._safe(d, me, foe, me.mod.cast_time(me.mod.spells["Mana Burn"])):
            return None
        return "Mana Burn"

    def _swd_ok(self, d, me, foe, swd):
        """Shadow Word: Death only when it should kill (no backlash) or when its 30% backlash leaves me above half health."""
        t = d.t
        if foe.immune(t):
            return False
        p = me.p
        dmg = ((swd.dmg_min + swd.dmg_max) / 2 + swd.coef * p.spell_power) * me.mod.damage_multiplier(swd, False)
        ehp = foe.p.hp + (foe.p.absorb if t < foe.p.absorb_until else 0.0)
        if ehp <= 0.95 * dmg:
            return True
        back = PM.SWD_BACKLASH * p.hp_max
        crit_dmg = dmg * (1.5 + me.mod.crit_damage_bonus(swd))
        return p.hp - back > 0.5 * p.hp_max and ehp <= 0.95 * crit_dmg

    def _rotation(self, d, me, foe):
        """The spec's own rotation, with this duel's vetoes (the fight lab's veto rule: a vetoed spell counts as unaffordable, so the
        priority list falls through to its next choice)."""
        t = d.t
        veto = dict(self.persistent_veto)
        for name, until in self.dot_rest.items():
            if t < until:
                veto[name] = {"off": True}
        swd = me.mod.spells.get("Shadow Word: Death")
        if swd is not None and not self._swd_ok(d, me, foe, swd):
            veto["Shadow Word: Death"] = {"off": True}
        if self.shadow:   # Shadowform: no healing spells (Forever's tooltip); the rotation's Flash Heal line is already gated
            for n in ("Flash Heal", "Lesser Heal", "Heal", "Greater Heal", "Renew"):
                veto[n] = {"off": True}
        elif self.healer and self._saving(me, foe):
            for n in DAMAGE_SPELLS:   # the healing trees keep their last mana for heals; the wand does the damage
                veto[n] = {"off": True}
        me.mod.veto = veto
        try:
            return self.rotation(d, me, foe)
        finally:
            me.mod.veto = dict(self.persistent_veto)
