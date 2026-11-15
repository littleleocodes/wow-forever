"""Paladin PvP layer (duellab, 2026-11-14): Divine Shield (or Templar's Bulwark, Blessing of Protection against a physical foe, Divine
Protection) when low and Holy Light inside it, Lay on Hands as the last resort, Hammer of Justice on heals and long casts within 10
yards and as a heal window, Repentance as an interrupt or a heal window, Blessing of Freedom and Cleanse against roots and slows when
kited, Cleanse on Devouring Plague, magic dots and poison, Voice of Truth before a heal an interrupt threatens, Holy Shock as an instant
heal and a 20-yard nuke; against a kiting foe Repentance from 8-20 yards and Hammer of Justice inside 10 to catch it, Judgement inside
10 yards (the seal recast at range), Hammer of Wrath at 30. The heals are this layer's (the rotation's are vetoed: they ignore the
foe's interrupts): inside an immunity up to 90%, while the foe is held (Holy 90%, Protection 65%, Retribution 55%), below 55% (Holy)
or 40%. Damage (the seal, Judgement, Holy Strike, Consecration on a foe that stays in it, Holy Shock for the Holy path, Hammer of
Wrath) is the spec's own leveling rotation underneath (ret-dps; holy-leveling with a two-hander for the Holy builds; prot-leveling with
a shield and Seal of Fury), so each spec keeps its own play.

Effects the fight lab does not parse (handlers below): Divine Shield (12 s immune to everything, your damage halved, harmful effects
removed), Divine Protection (8 s immune, no attacks or weapon abilities), Blessing of Protection (10 s immune to physical attacks, no
attacks; Guardian's Favor's -1 min a rank), Forbearance (1 min, Sacred Duty's -5 s a rank; blocks all four), Templar's Bulwark (the
module's absorb with Forbearance), Hammer of Justice (6 s stun, one diminishing-returns application: the module's own on_hit stun would
count it twice), Repentance (6 s incapacitate, broken by damage; auto attack stops while it holds), Blessing of Freedom (roots and slows
removed and refused for 10 s, Guardian's Favor's +3 s a rank), Cleanse (one magic, one poison and one disease effect), Voice of Truth
(6 s immune to silences and interrupts: a trainer spell since client 70753, when it stopped being a talent; the fight lab's
TALENT_SPELLS still drops it), Seal of Justice (2 s stun at 5 procs per minute from melee hits: CMaNGOS Classic's ppmRate for 20164,
the client's 100% proc chance being the aura's; random_stun diminishing returns), the Retribution path's Holy Shock heal, Consecration
as ground (the fight lab's dot on the target ends once the foe is more than 8 yards away).
Talents with a PvP effect (each only when the build has it): Unyielding Faith (-15% a rank fear and disorient duration), Divine
Precision (-10% a rank silence duration; 11-02 notes), Stoicism (-10% a rank stun and charm duration), Improved Hammer of Justice
(the module's cooldown), Sacred Duty, Guardian's Favor, Vindication (the module marks the foe; its attack power cut taken off each of
the foe's weapon hits here: 68 a rank / 14 x weapon speed, after armor).

Assumptions: immunities remove existing harmful effects (Classic's school-immunity auras); Divine Shield halves direct damage only
(dots already ticking keep theirs); Holy Shock's offensive range is 20 yards (Classic; the data lists the friendly 40); slows are magic
when the foe is a mage, priest, shaman or druid; a rogue's slow is a poison; a heal in melee finishes with Spiritual Focus at 3/5 or
more. Seal of Justice is modelled but not chosen (use_soj): swapped in for the damage seal against casters in melee it lost every test
(2026-11-14, 40-100 duels: Retribution against Shadow 20% -> 2% of wins, against the Frost mage 97% -> 95%; Holy against Discipline
70% -> 0%, all draws), so every build keeps its rotation's seal.
Not modelled: Exorcism and Holy Wrath (undead and demons only), Light's Vigil (an expensive party heal), Blessing of Sacrifice, Divine
Intervention, Turn Undead, auras other than Devotion, seal twisting, blocks' on-block effects (the duel engine does not call on_block:
Redoubt's charges, Reckoning and Shield Specialization on blocks).
"""
import copy
import re

import duel  # noqa: F401  (puts the fight lab first on sys.path: engine, tables and the class module are its copies)
import dtables as T
import engine as FE
import tables as FT
from pvp_base import PvPAI, HEALS, HOSTILE

INTERRUPTS = {"Counterspell": 30.0, "Pummel": 5.5, "Shield Bash": 5.5, "Kick": 5.5, "Earth Shock": 20.0, "Silence": 24.0,
              "Spell Lock": 30.0}                       # interrupts and silences (Voice of Truth stops them), by reach in yards
BREAKERS = {"Hammer of Justice": 10.0, "Intimidating Shout": 10.0, "Psychic Scream": 8.0}   # stuns and fears that break a cast
MAGIC_DOTS = {"Shadow Word: Pain", "Immolate", "Corruption", "Siphon Life", "Moonfire", "Insect Swarm", "Flame Shock", "Fireball",
              "Pyroblast", "Holy Fire", "Ignite"}
POISON_DOTS = {"Deadly Poison", "Serpent Sting"}
DISEASES = {"Devouring Plague"}
PHYSICAL_DOTS = {"Rend", "Deep Wounds", "Garrote", "Rupture", "Rake", "Rip", "Lacerate"}
MAGIC_SLOW_CLASSES = {"mage", "priest", "shaman", "druid"}
POISON_SLOW_CLASSES = {"rogue"}
NON_MAGIC_ROOTS = {"Improved Hamstring", "Entrapment", "Improved Wing Clip"}
DISORIENTS = {"Blind", "Scatter Shot"}
CASTERS = {"mage", "priest", "warlock", "druid", "shaman"}     # classes whose casts Seal of Justice's stuns break
SELF_SPELLS = ("Blessing of Freedom", "Blessing of Protection", "Cleanse", "Voice of Truth", "Divine Favor")
IMMUNITY = ("Divine Shield", "Divine Protection", "Blessing of Protection", "Templar's Bulwark")
WEAPON_ABILITIES = ("Holy Strike",)
SOJ_PPM = 5.0               # Seal of Justice procs per minute (CMaNGOS Classic spell_proc_event 20164; the client gives no PPM row)
SOJ_STUN = 2.0
SECS = re.compile(r"for (\d+) sec")


def _secs(spell, default):
    m = SECS.search(getattr(spell, "text", "") or "")
    return float(m.group(1)) if m else default


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


class PaladinPvP(PvPAI):
    keep_range = 0.0
    auto_attack = True
    hostile_buffs = HOSTILE | {"Judgement", "Swift Judgement"}   # the module files them as buffs; they need the foe in 10 yards

    def bind(self, d, me):
        super().bind(d, me)
        m = me.mod
        self.path = getattr(m, "path", "ret")
        self.ds_until = self.dp_until = self.bop_until = 0.0     # Divine Shield, Divine Protection, Blessing of Protection
        self.freedom_until = self.vot_until = self.repent_until = 0.0
        self.persistent_veto = {}
        self.ranges = {"Holy Shock": 20.0}
        # Voice of Truth: a level-20 trainer spell since client 70753 (no longer a talent); the module's TALENT_SPELLS drops it
        vot = m.book.get("Voice of Truth") if hasattr(m, "book") else None
        if vot is not None and "Voice of Truth" not in m.spells:
            m.spells["Voice of Truth"] = vot
        for n in SELF_SPELLS:
            s = m.spells.get(n)
            if s is not None:
                c = copy.copy(s)
                c.target = "self"
                if n == "Blessing of Protection":
                    c.cooldown = max(0.0, s.cooldown - 60.0 * m.tv("Guardian's Favor", 0))
                m.spells[n] = c
        self.durations = {n: _secs(m.spells.get(n), dflt) for n, dflt in (("Divine Shield", 12.0), ("Divine Protection", 8.0),
                                                                          ("Blessing of Protection", 10.0), ("Blessing of Freedom", 10.0),
                                                                          ("Voice of Truth", 6.0), ("Hammer of Justice", 6.0),
                                                                          ("Repentance", 6.0))}
        self.forbearance = 60.0 - m.tv("Sacred Duty", 1)
        # the Retribution path's Holy Shock heal (the Holy and Protection paths have the module's own "Holy Shock (heal)")
        shock = m.spells.get("Holy Shock")
        if shock is not None and "Holy Shock (heal)" not in m.spells and getattr(shock, "shock_heal", (0, 0))[1] > 0:
            c = copy.copy(shock)             # name stays "Holy Shock": one cooldown for both uses
            c.kind, c.target = "heal", "self"
            c.dmg_min = c.dmg_max = 0.0
            c.heal_min, c.heal_max = shock.shock_heal
            c.heal_coef = getattr(shock, "shock_heal_coef", 0.0)
            m.spells["Holy Shock (heal)"] = c
        self._wrap(me)

    # ------------------------------------------------------------------ wrappers on this side's own objects (engine gaps)
    def _wrap(self, me):
        m, ai = me.mod, self
        apply_cc = me.apply_cc

        def cc(kind, dur, cat, name, frozen=False, breaks=None, physical=False):
            """Blessing of Freedom refuses roots; Voice of Truth silences; talents shorten fears, disorients, silences, stuns."""
            t = me.t
            if kind == "root" and t < ai.freedom_until:
                me.fight.note(f"immune to {name or 'root'} (Blessing of Freedom)")
                return 0.0
            if kind == "silence" and t < ai.vot_until:
                me.fight.note(f"immune to {name or 'silence'} (Voice of Truth)")
                return 0.0
            if (kind == "fear" or name in DISORIENTS) and m.rank("Unyielding Faith"):
                dur *= 1 - m.tv("Unyielding Faith", 0) / 100
            if kind == "silence" and m.rank("Divine Precision"):
                dur *= 1 - m.tv("Divine Precision", 1) / 100
            if (kind == "stun" or name in T.CHARM) and m.rank("Stoicism"):
                dur *= 1 - m.tv("Stoicism", 0) / 100
            return apply_cc(kind, dur, cat, name, frozen=frozen, breaks=breaks, physical=physical)
        me.apply_cc = cc

        interrupt = me.interrupt

        def intr(lock, by):
            """Immune (Divine Shield, Divine Protection) or under Voice of Truth: no interrupt."""
            t = me.t
            if t < me.immune_until or t < ai.vot_until:
                me.fight.note(f"{by} has no effect ({'immune' if t < me.immune_until else 'Voice of Truth'})")
                return
            interrupt(lock, by)
        me.interrupt = intr

        deal = me.fight.deal

        def dealt(spell, amount, crit=False, source="player"):
            """Divine Shield: all damage you deal -50% (Forever's tooltip)."""
            if me.t < ai.ds_until:
                amount *= 0.5
            return deal(spell, amount, crit, source)
        me.fight.deal = dealt

        on_swing = m.on_swing

        def swing(fight, spell, outcome, amount, hand):
            on_swing(fight, spell, outcome, amount, hand)
            if outcome in ("miss", "dodge", "parry") or spell.kind != "melee":
                return
            sealb = fight.p.buff("Seal", fight.t)
            w = fight.p.mh
            if sealb and sealb.get("name") == "Seal of Justice" and w is not None and fight.rng.random() < SOJ_PPM * w.speed / 60.0:
                me.foe.apply_cc("stun", SOJ_STUN, T.DR_CATEGORY.get("Seal of Justice", "random_stun"), "Seal of Justice")
        m.on_swing = swing

    # ------------------------------------------------------------------ effects
    def effects_for(self, me):
        return {"Divine Shield": self.divine_shield, "Divine Protection": self.divine_protection,
                "Blessing of Protection": self.protection, "Templar's Bulwark": self.bulwark, "Hammer of Justice": self.hammer,
                "Repentance": self.repentance, "Blessing of Freedom": self.freedom, "Cleanse": self.cleanse, "Voice of Truth": self.voice}

    def _lands(self, me, spell):
        hit = 1.0 - FT.spell_miss(0) + me.mod.hit_bonus(spell) + me.p.spell_hit
        return me.fight.rng.random() <= min(FT.SPELL_HIT_CAP, hit)

    def _forbear(self, me, t):
        me.p.buffs["Forbearance"] = {"until": t + self.forbearance}

    def _purge_harm(self, me, physical_only=False):
        """An immunity's start: harmful effects of the schools it covers go (roots, slows, dots, healing reduction)."""
        t = me.t
        foe = me.foe
        if physical_only:
            me.dots = [x for x in me.dots if x[0] not in PHYSICAL_DOTS]
            if foe.cls not in MAGIC_SLOW_CLASSES:
                me.slow_until = min(me.slow_until, t)
            if me.root_name in NON_MAGIC_ROOTS:
                me.root_until = min(me.root_until, t)
            me.debuffs.pop("Mortal Strike", None)
            return
        me.dots = []
        me.slow_until = min(me.slow_until, t)
        me.root_until = min(me.root_until, t)
        for n in ("Mortal Strike", "Wound Poison", "Vampiric Embrace"):
            me.debuffs.pop(n, None)

    def divine_shield(self, d, me, foe, spell):
        t = d.t
        dur = self.durations["Divine Shield"]
        me.immune_until = max(me.immune_until, t + dur)
        self.ds_until = t + dur
        self._purge_harm(me)
        self._forbear(me, t)
        me.fight.note(f"Divine Shield ({dur:.0f}s)")
        return 0.0

    def divine_protection(self, d, me, foe, spell):
        t = d.t
        dur = self.durations["Divine Protection"]
        me.immune_until = max(me.immune_until, t + dur)
        self.dp_until = t + dur
        me.p.buffs["Divine Protection"] = {"until": t + dur}
        self._purge_harm(me)
        self._forbear(me, t)
        me.fight.note(f"Divine Protection ({dur:.0f}s)")
        return 0.0

    def protection(self, d, me, foe, spell):
        t = d.t
        dur = self.durations["Blessing of Protection"]
        me.immune_phys_until = max(me.immune_phys_until, t + dur)
        self.bop_until = t + dur
        self._purge_harm(me, physical_only=True)
        self._forbear(me, t)
        me.fight.note(f"Blessing of Protection ({dur:.0f}s)")
        return 0.0

    def bulwark(self, d, me, foe, spell):
        """Templar's Bulwark: the module's own effect (an absorb of your maximum health for 8 s), Forbearance with Sacred Duty."""
        t, p, m = d.t, me.p, me.mod
        p.absorb, p.absorb_until = p.hp_max, t + 8.0
        if hasattr(m, "_bulwark_until"):
            m._bulwark_until = t + 8.0
            m._sof_live = False
        self._forbear(me, t)
        me.fight.note(f"Templar's Bulwark ({p.hp_max:.0f})")
        return 0.0

    def hammer(self, d, me, foe, spell):
        if foe.immune(d.t) or not self._lands(me, spell):
            me.fight.note(f"Hammer of Justice {'immune' if foe.immune(d.t) else 'MISS'}")
            return 0.0
        foe.apply_cc("stun", self.durations["Hammer of Justice"], T.DR_CATEGORY.get("Hammer of Justice", "stun"), "Hammer of Justice")
        return 0.0

    def repentance(self, d, me, foe, spell):
        if foe.immune(d.t) or not self._lands(me, spell):
            me.fight.note(f"Repentance {'immune' if foe.immune(d.t) else 'MISS'}")
            return 0.0
        dur = foe.apply_cc("incap", self.durations["Repentance"], T.DR_CATEGORY.get("Repentance", "incap"), "Repentance")
        if dur > 0:
            self.repent_until = d.t + dur
        return 0.0

    def freedom(self, d, me, foe, spell):
        t = d.t
        self.freedom_until = t + self.durations["Blessing of Freedom"] + me.mod.tv("Guardian's Favor", 1)
        me.root_until = min(me.root_until, t)
        me.slow_until = min(me.slow_until, t)
        me.fight.note("Blessing of Freedom")
        return 0.0

    def voice(self, d, me, foe, spell):
        self.vot_until = d.t + self.durations["Voice of Truth"]
        me.fight.note("Voice of Truth")
        return 0.0

    def cleanse(self, d, me, foe, spell):
        """One magic effect (a magic root, a magic slow, then the worst magic dot or Vampiric Embrace), one poison, one disease."""
        t, out = d.t, []
        magic = None
        if t < me.root_until and me.root_name not in NON_MAGIC_ROOTS:
            me.root_until = t
            magic = me.root_name or "root"
        elif t < me.slow_until and foe.cls in MAGIC_SLOW_CLASSES:
            me.slow_until = t
            magic = "slow"
        else:
            dots = sorted((x for x in me.dots if x[0] in MAGIC_DOTS), key=lambda x: -x[1] * x[2])
            ve = me.debuffs.get("Vampiric Embrace")
            if dots:
                me.dots.remove(dots[0])
                magic = dots[0][0]
            elif ve and ve.get("until", 0) > t:
                me.debuffs.pop("Vampiric Embrace")
                magic = "Vampiric Embrace"
        if magic:
            out.append(magic)
        wp = me.debuffs.get("Wound Poison")
        if wp and wp.get("until", 0) > t:
            me.debuffs.pop("Wound Poison")
            out.append("Wound Poison")
        elif t < me.slow_until and foe.cls in POISON_SLOW_CLASSES:
            me.slow_until = t
            out.append("Crippling Poison")
        else:
            for dot in [x for x in me.dots if x[0] in POISON_DOTS][:1]:
                me.dots.remove(dot)
                out.append(dot[0])
        for dot in [x for x in me.dots if x[0] in DISEASES][:1]:
            me.dots.remove(dot)
            out.append(dot[0])
        me.fight.note(f"Cleanse: {', '.join(out) or 'nothing'}")
        return 0.0

    # ------------------------------------------------------------------ helpers
    def _dr_next(self, side, cat, t):
        rec = side.dr.get(cat)
        n = rec[0] if rec and t < rec[1] + T.DR_RESET else 0
        return T.DR_STEPS[min(n, len(T.DR_STEPS) - 1)]

    def _kick_ready(self, d, foe, within=0.0, table=None):
        """Whether the foe has an interrupt (or, with table=BREAKERS, a cast-breaking stun or fear) ready within `within` s, in reach."""
        t = d.t
        if max(self._held(foe, t), foe.inactive_until - t) >= within:
            return False   # held for the whole cast
        for name, reach in (INTERRUPTS if table is None else table).items():
            s = foe.mod.spells.get(name)
            if s is None or d.dist > reach:
                continue
            if foe.silenced(t) and s.kind not in ("melee", "ranged") and foe.silence_until >= t + within:
                continue
            if foe.p.ready(name, t + within):
                return True
        return False

    def _held(self, foe, t):
        """Seconds the foe stays unable to act (stun, incapacitate, fear)."""
        return max(foe.stun_until, foe.incap_until, foe.fear_until) - t

    def _safe(self, d, me, foe, cast):
        """Whether a cast of `cast` seconds should finish: immune, the foe held for all of it, or no interrupt in reach and a melee
        foe still away for most of it."""
        t = d.t
        if t < me.immune_until and me.immune_until - t >= cast:
            return True
        if t < me.immune_phys_until and me.immune_phys_until - t >= cast and self._physical(foe):
            return True
        if self._held(foe, t) >= cast + 0.1 or t < foe.inactive_until:
            return True
        if self._kick_ready(d, foe, cast, BREAKERS):
            return False
        if self._kick_ready(d, foe, cast) and t >= self.vot_until:
            return False
        if self.melee_foe(foe) and d.dist <= T.MELEE + 0.5:
            # pushback: Spiritual Focus ignores it 14% a rank (70% at 5/5); a short heal finishes anyway
            return me.mod.rank("Spiritual Focus") >= 3 or cast <= 1.5
        return True

    def _physical(self, foe):
        """A foe whose damage is physical: Blessing of Protection stops it (warrior, rogue, hunter; a Feral druid in form)."""
        return foe.cls in ("warrior", "rogue", "hunter") or (foe.mod.melee and foe.cls == "druid")

    def _cast_free(self, me, name):
        gcd = me.p.gcd_until
        me.cast(name)
        me.p.gcd_until = gcd

    def _forb(self, me, t):
        return bool(me.p.buff("Forbearance", t))

    def _seal_name(self, me, t):
        b = me.p.buff("Seal", t)
        return b.get("name") if b else None

    # ------------------------------------------------------------------ per step
    def _step(self, d, me, foe):
        t = d.t
        if t < self.freedom_until:
            me.root_until = min(me.root_until, t)
            me.slow_until = min(me.slow_until, t)
        # no swings while Divine Protection or Blessing of Protection holds, or while my Repentance holds a foe I am healing through
        repent = t < self.repent_until and t < foe.incap_until and foe.incap_name == "Repentance" and me.hp_frac() < 0.85
        held = t < self.dp_until or t < self.bop_until or repent
        self.auto_attack = not held
        if t >= self.repent_until or foe.incap_name != "Repentance" or t >= foe.incap_until:
            self.repent_until = min(self.repent_until, t)
        # Consecration is ground: a foe out of its 8 yards takes no more of it
        if d.dist > 8.0 and any(x[0] == "Consecration" for x in foe.dots):
            foe.dots = [x for x in foe.dots if x[0] != "Consecration"]
        veto = {}
        if self._forb(me, t):
            for n in IMMUNITY:
                veto[n] = {"off": True}
        if held:
            for n in WEAPON_ABILITIES:
                veto[n] = {"off": True}
        self.persistent_veto = veto
        me.mod.veto = dict(veto)

    def damage_taken(self, d, me, src, spell, amount):
        """Vindication: the foe's weapon hits lose the attack power the debuff takes away (after armor)."""
        t = d.t
        ap = me.mod.tv("Vindication", 0)
        if ap and amount > 0 and getattr(spell, "kind", "") == "melee" and t < src.dmg_reduction_until and src.dmg_reduction > 0:
            w = src.p.mh
            if w is not None:
                pct = spell.weapon_pct if getattr(spell, "weapon_pct", 0.0) > 0 else (1.0 if spell.name.startswith("Melee") else 0.0)
                cut = ap / 14.0 * w.speed * pct * (1.0 - FT.armor_mitigation(me.armor(), 60))
                amount = max(0.0, amount - cut)
        return amount

    # ------------------------------------------------------------------ hooks
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
        self._step(d, me, foe)
        return None

    def off_gcd(self, d, me, foe):
        self._step(d, me, foe)
        return None

    def intent(self, d, me, foe):
        if foe.stealthed:
            return "hold"
        return "close"

    def decide(self, d, me, foe):
        t = d.t
        if foe.stealthed:
            return None
        # 1. emergencies: an immunity, the Bulwark, Lay on Hands
        a = self._emergency(d, me, foe)
        if a:
            return a
        # 2. heals: inside an immunity, while the foe is held, or when low
        a = self._heal(d, me, foe)
        if a:
            return a
        # 3. control: Hammer of Justice and Repentance on heals and long casts
        a = self._control(d, me, foe)
        if a:
            return a
        # 4. free of roots and slows when kept at range
        a = self._free(d, me, foe)
        if a:
            return a
        # 5. Cleanse a disease, magic dot or poison worth a global cooldown
        a = self._cleanse(d, me, foe)
        if a:
            return a
        if foe.immune(t):
            return self._wait(d, me, foe)
        # 6. at range: Hammer of Wrath on a low foe, Holy Shock
        a = self._ranged(d, me, foe)
        if a:
            return a
        # 7. the seal for this foe
        a = self._seal(d, me, foe)
        if a:
            return a
        return self._rotation(d, me, foe)

    # ------------------------------------------------------------------ decisions
    def _emergency(self, d, me, foe):
        t = d.t
        hp = me.hp_frac()
        if t < me.immune_until or (t < me.immune_phys_until and self._physical(foe)):
            return None
        if foe.hp_frac() < 0.08 and hp > 0.12:
            return None   # finish it instead
        free = not self._forb(me, t)
        if free and hp < 0.40 and me.can("Templar's Bulwark"):
            return "Templar's Bulwark"
        if free and hp < 0.27:
            if me.can("Divine Shield"):
                return "Divine Shield"
            if self._physical(foe) and me.can("Blessing of Protection"):
                return "Blessing of Protection"
            if me.can("Divine Protection"):
                return "Divine Protection"
        if hp < 0.15 and me.can("Lay on Hands") and not (me.p.absorb > 0 and t < me.p.absorb_until):
            return "Lay on Hands"
        return None

    def _heal_name(self, d, me, foe, hp, voice=False):
        """The heal to cast now: Holy Light when it can finish, else Flash of Light; with `voice`, Voice of Truth first when only an
        interrupt stands in the way."""
        hl = "Holy Light" if me.can("Holy Light") else None
        fol = "Flash of Light" if me.can("Flash of Light") else None
        hl_t = me.mod.cast_time(me.mod.spells["Holy Light"]) if hl else 99.0
        fol_t = me.mod.cast_time(me.mod.spells["Flash of Light"]) if fol else 99.0
        if hl and self._safe(d, me, foe, hl_t):
            return hl
        if fol and self._safe(d, me, foe, fol_t):
            return fol
        cast = hl_t if hl else fol_t
        if voice and (hl or fol) and not self._kick_ready(d, foe, cast, BREAKERS) and self._voice(d, me, foe) \
                and self._safe(d, me, foe, cast):
            return hl or fol
        return None

    def _heal(self, d, me, foe):
        """Heals: inside an immunity or while the foe is held, Holy Light up to 90%; below the build's threshold (Holy 55%, the others
        40%), Holy Shock's instant heal, else a heal that can finish (Voice of Truth against a ready interrupt)."""
        t = d.t
        hp = me.hp_frac()
        if hp >= 0.95:
            return None
        protected = t < me.immune_until or (t < me.immune_phys_until and self._physical(foe))
        shock = "Holy Shock (heal)" if (me.can("Holy Shock (heal)") and me.p.ready("Holy Shock", t)) else None
        # inside an immunity every path heals up; a held foe is a heal window for the Holy path, a damage window (the doubled Seal
        # of Command judgement) for the others unless they are hurt
        held_hp = {"holy": 0.9, "prot": 0.65}.get(self.path, 0.55)
        if (protected and hp < 0.9) or (self._held(foe, t) >= 1.6 and hp < held_hp):
            h = self._heal_name(d, me, foe, hp)
            if h:
                if hp < 0.6:
                    self._favor(me)
                return h
        low = 0.55 if self.path == "holy" else 0.40
        if hp < low and not (hp > 0.25 and self._killable(me, foe) and me.can("Holy Shock")):   # a killing shock first
            if shock and (hp < low - 0.1 or not me.can("Holy Light")):
                self._favor(me)
                return shock
            h = self._heal_name(d, me, foe, hp, voice=True)
            if h:
                if hp < 0.35:
                    self._favor(me)
                return h
            if hp < 0.25 and me.can("Flash of Light") and not self._kick_ready(d, foe, 1.5):
                return "Flash of Light"
        return None

    def _favor(self, me):
        """Divine Favor (off the global cooldown: the client's list) before a big heal: the module's own helper on the Holy path."""
        if self.path != "ret" and hasattr(me.mod, "_favor"):
            me.mod._favor(me.fight)

    def _voice(self, d, me, foe):
        """Voice of Truth (off the global cooldown) when an interrupt or silence threatens the heal about to start. Returns whether
        a heal is now safe from interrupts."""
        t = d.t
        if t < self.vot_until:
            return True
        if me.can("Voice of Truth", ignore_gcd=True):
            self._cast_free(me, "Voice of Truth")
            return t < self.vot_until
        return False

    def _control(self, d, me, foe):
        t = d.t
        if foe.immune(t) or foe.controlled(t):
            return None
        hp = me.hp_frac()
        c = self.foe_cast(d, foe)
        casting = c is not None and (c.kind == "heal" or c.name in HEALS or foe.mod.cast_time(c) >= 1.5 or c.kind == "channel")
        stun_ok = self._dr_next(foe, T.DR_CATEGORY.get("Hammer of Justice", "stun"), t) >= 0.5
        if me.can("Hammer of Justice") and stun_ok:
            blink = foe.mod.spells.get("Blink") is not None and foe.p.ready("Blink", t)
            if casting:
                return self._ground_pop(d, me, foe) or "Hammer of Justice"
            if hp < 0.5 and not blink and self._heal_name(d, me, foe, hp) is None:
                return self._ground_pop(d, me, foe) or "Hammer of Justice"   # a heal window: the next decision heals
        if me.can("Repentance") and self._dr_next(foe, T.DR_CATEGORY.get("Repentance", "incap"), t) >= 0.5 \
                and not foe.ai.cc_immune(d, foe, "incap", "Repentance"):   # not into a visible Berserker Rage
            if casting and (c.kind == "heal" or c.name in HEALS or not me.can("Hammer of Justice")):
                return self._ground_pop(d, me, foe) or "Repentance"
            if hp < 0.45 and not me.p.ready("Hammer of Justice", t) and (me.can("Holy Light") or me.can("Flash of Light")):
                return self._ground_pop(d, me, foe) or "Repentance"
        return None

    def _ground_pop(self, d, me, foe):
        """A charged Grounding Totem (pvp_base.grounding) takes the next spell cast at the foe: Holy Shock pops it first when the build
        has it (Judgement is no groundable spell here)."""
        if foe.ai.grounding(d, foe) and me.can("Holy Shock"):
            return "Holy Shock"
        return None

    def _free(self, d, me, foe):
        """Kept at range by a root or a slow: Blessing of Freedom, else Cleanse a magic one."""
        t = d.t
        if d.dist <= T.MELEE + 1.0 or self.melee_foe(foe):
            return None
        rooted = t < me.root_until and me.root_until - t >= 1.0
        slowed = t < me.slow_until and me.slow >= 0.3 and me.slow_until - t >= 1.5
        if not (rooted or slowed):
            return None
        if me.can("Blessing of Freedom"):
            return "Blessing of Freedom"
        magic = (rooted and me.root_name not in NON_MAGIC_ROOTS) or (slowed and not rooted and foe.cls in MAGIC_SLOW_CLASSES)
        if magic and me.can("Cleanse"):
            return "Cleanse"
        return None

    def _cleanse(self, d, me, foe):
        t = d.t
        if not me.can("Cleanse") or me.mana_frac() < 0.15:
            return None
        bad = sum(x[1] * x[2] for x in me.dots if x[0] in MAGIC_DOTS | DISEASES | POISON_DOTS)
        ve = me.debuffs.get("Vampiric Embrace")
        if ve and ve.get("until", 0) > t:
            bad += 400.0
        wp = me.debuffs.get("Wound Poison")
        if wp and wp.get("until", 0) > t and wp.get("stacks", 1) >= 3:
            bad += 300.0
        busy = d.dist <= T.MELEE + 0.5 and self.melee_foe(foe)
        return "Cleanse" if bad >= (700.0 if busy else 450.0) else None

    def _ranged(self, d, me, foe):
        """Out of melee (a kiting foe): Repentance from 8-20 yards and Hammer of Justice inside 10 to catch it (no damage while my
        Repentance holds it), Hammer of Wrath on a low foe, Judgement inside 10 yards, Holy Shock inside 20."""
        t = d.t
        if d.dist <= T.MELEE + 0.5:
            return None
        repented = t < foe.incap_until and foe.incap_name == "Repentance"
        stun_ok = self._dr_next(foe, T.DR_CATEGORY.get("Hammer of Justice", "stun"), t) >= 0.5
        if repented:
            if d.dist <= 10.0 and stun_ok and me.can("Hammer of Justice"):
                return "Hammer of Justice"
            return "advance"
        kiter = not self.melee_foe(foe)
        if kiter and not foe.controlled(t):
            if stun_ok and me.can("Hammer of Justice"):
                return "Hammer of Justice"
            if 8.0 < d.dist and me.can("Repentance") and not foe.dots and not foe.ai.cc_immune(d, foe, "incap", "Repentance") \
                    and self._dr_next(foe, T.DR_CATEGORY.get("Repentance", "incap"), t) >= 0.5:
                return "Repentance"
        if foe.hp_frac() <= 0.2 and me.can("Hammer of Wrath"):
            return "Hammer of Wrath"
        if self._seal_name(me, t) is None:   # the rotation reseals only in melee: a kiting foe would never be judged again
            seal = me.mod.seal() if hasattr(me.mod, "seal") else None
            if seal is not None and me.can(seal.name):
                return seal.name
        if d.dist <= 10.0 and self._seal_name(me, t) and me.can("Judgement") and self._seal_name(me, t) != "Seal of Justice":
            return "Judgement"
        if me.can("Holy Shock") and (me.mana_frac() > 0.3 or self._killable(me, foe)):
            return "Holy Shock"
        return None

    def _killable(self, me, foe):
        """Whether a Holy Shock (or the next big hit) should finish the foe: its health and absorb under one shock's damage."""
        s = me.mod.spells.get("Holy Shock")
        if s is None:
            return foe.hp_frac() < 0.1
        t = me.t
        dmg = ((s.dmg_min + s.dmg_max) / 2 + s.coef * me.p.spell_power) * me.mod.damage_multiplier(s, False)
        return foe.p.hp + (foe.p.absorb if t < foe.p.absorb_until else 0.0) <= 1.1 * dmg

    def _seal(self, d, me, foe):
        """Seal of Justice against a caster or healer once in melee (its stuns break casts), only with use_soj on: off by default, as it
        lost every test against keeping the rotation's damage seal (module docstring)."""
        t = d.t
        if foe.cls not in CASTERS or d.dist > T.MELEE + 0.5 or not me.can("Seal of Justice"):
            return None
        if self._seal_name(me, t) == "Seal of Justice":
            return None
        if self._dr_next(foe, T.DR_CATEGORY.get("Seal of Justice", "random_stun"), t) < 0.5:
            return None
        return "Seal of Justice" if self.use_soj else None

    use_soj = False

    def _wait(self, d, me, foe):
        """The foe is immune (Ice Block, Divine Shield): heal up or wait."""
        hp = me.hp_frac()
        if hp < 0.9:
            h = self._heal_name(d, me, foe, hp)
            if h:
                return h
        return None

    def _rotation(self, d, me, foe):
        """The spec's own rotation with this duel's vetoes: Consecration only on a foe that stays in it, no Judgement on a Seal of
        Justice (it judges no damage), no weapon strikes inside Divine Protection or Blessing of Protection."""
        t = d.t
        veto = dict(self.persistent_veto)
        stays = self.melee_foe(foe) or foe.controlled(t) or foe.body.rooted(t)
        if not stays or d.dist > T.MELEE + 0.5:
            veto["Consecration"] = {"off": True}
        if self._seal_name(me, t) == "Seal of Justice":
            veto["Judgement"] = {"off": True}
        # undead and demons only; the immunities, Lay on Hands and the heals are this layer's (the rotation's Divine Protection at
        # 35% would spend the Forbearance window Divine Shield should get, and its heals do not look at the foe's interrupts)
        for n in ("Exorcism", "Holy Wrath", "Turn Undead", "Lay on Hands", "Holy Light", "Flash of Light", "Holy Shock (heal)") + IMMUNITY:
            veto[n] = {"off": True}
        me.mod.veto = veto
        try:
            return self.rotation(d, me, foe)
        finally:
            me.mod.veto = dict(self.persistent_veto)
