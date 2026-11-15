"""Shaman PvP layer (duellab, 2026-11-14): Earth Shock on heals, crowd control and long casts; Grounding Totem against crowd control and
big casts; Purge on absorb shields; Frost Shock and Earthbind Totem to stick to a kiting foe or to keep a melee away; Ghost Wolf to close
in or get away; Tremor Totem against fear; Lightning Shield kept up; self-healing (Riptide, Healing Wave, Lesser Healing Wave, Nature's
Swiftness off the global cooldown) for the Restoration build, emergencies and free windows for the others. The damage is the spec's own
leveling rotation underneath (Enhancement: Stormstrike, shocks, Maelstrom Lightning Bolts; Elemental: Lightning Bolt and shocks;
Restoration plays Enhancement's, the project's rule).

The 2026-11-12 live hotfix (Stormstrike 150% -> 100% weapon damage, cooldown 6 -> 8 s; Maelstrom Weapon 20 -> 6-10 procs a minute;
the 2026-11-14 PvP research, _reference/pvp-research.md) is in neither our spell data (talentsforever's 70753 export: "150% normalized weapon damage", 6 s) nor the fight lab (shaman.py:
MW_PPM_PER_POINT 4, 20 a minute at 5/5); client 70938's tables still carry 150% and 6 s, so the change is server-side. HOTFIX_1112 applies
it to this side's own copy of Stormstrike and, through a wrapper, to its Maelstrom rolls. Switch it off to measure the old numbers.

Effects the fight lab does not parse, or parses for creatures only (each one this layer's handler):
- Totems stand where they were dropped: the duel's line keeps this side's position (`x`, its own movement integrated each step) and the
  foe's (x + distance). Earthbind Totem: 50% slow for 5 s, pulsing every 3 s within 10 yd (Earth's Grasp +10% radius a rank); Earthbound
  adds a 5 s root on enemies within reach when it is dropped (DR category root). Tremor Totem: every 4 s, removes fear (not Death Coil's
  horror), Seduction, Hibernate and Wyvern Sting from the shaman within 30 yd. Grounding Totem: one hostile single-target spell cast at
  the shaman within 30 yd is redirected to it every 10 s for 45 s; a damaging spell kills it (5 health), a spell without damage (Polymorph,
  Counterspell, Fear) leaves it to re-arm at the next pulse; a channel at the shaman is broken on the totem. Mana Tide Totem: its mana
  every 3 s for 12 s within 30 yd. Searing Totem: the fight lab's periodic shots, held while the foe is beyond 20 yd of the totem;
  re-dropped (at most every SEARING_EVERY s) where the fight stands still. Fire Nova: only on a foe within 10 yd of the active Fire
  totem. Stoneclaw Totem: its taunt holds an engaged pet for the totem's health over the pet's damage (at most 15 s); players are not
  taunted (the fight lab's 4 s mob stun is never applied to them). A foe's area spell (Frost Nova, Cone of Cold, Arcane Explosion,
  Blizzard, Whirlwind, Thunder Clap, Cleave, Multi-Shot ...) destroys the totems within its reach.
- Pre-duel (the countdown, Call of the Elements): Tremor against a foe that fears; Grounding against a caster without a spell interrupt
  (against Counterspell, Earth Shock or Silence it is kept for the first cast); mana paid, cooldowns from 3 s before the start; the fight
  lab's own pull (Lightning Shield, Searing Totem, Rage of the Farseer) as it is.
- Purge: an absorb shield (Ice Barrier, Power Word: Shield) and Blessing of Protection, with a spell hit roll.
- Ghost Wolf: +40% run speed, cast time less Improved Ghost Wolf (instant at 2/2: only then is it used), no attacks or spells in the form,
  cancelled by the shaman's next action.
- Lightning Shield and Water Shield re-cast in the fight (the fight lab puts one up at the pull only); neither fires on periodic damage
  (the duel engine calls the fight lab's on_hit_taken for dot ticks too).
- Nature's Swiftness off the global cooldown (client 70888 SpellCooldowns: StartRecoveryTime 0; fightlab/spell_gcd.json lists it as
  off_gcd, but tables.spell_gcd reads only the gcd table): the instant Healing Wave in the same step; the Elemental builds also use it for
  an instant Chain Lightning or Lightning Bolt that kills. Its buff is spent by a damage spell too (the fight lab spends it on heals only).
- Elemental Warding: Fire, Frost and Nature damage taken -3/7/10% (the fight lab has no caster mobs).

Decisions:
- Interrupts: Earth Shock on a seen cast worth it (a heal, crowd control, a channel, a damage cast of 1.4 s or more); against a caster
  the shocks wait up to SHOCK_HOLD for such a cast before the rotation spends them on damage. Grounding Totem on a groundable
  crowd-control cast, or a damage cast below GROUND_HP health.
- The foe's interrupts (their cooldowns are visible, as players track them): no cast-time damage spell beside a ready Pummel, Kick or
  Shield Bash, or into a ready Counterspell, Earth Shock or Silence unless a Grounding Totem stands or goes down first (it is dropped
  before the cast); no cast-time heal into any of these or a Felhunter's ready Spell Lock above KICKED_HEAL_AT health.
- A melee shaman closing on a ranged foe does not stop for a cast-time spell while it gains ground, Frost Shocks a kiting foe (or any
  ranged foe without casts worth the shock, a hunter), rides Ghost Wolf beyond WOLF_FROM yards, and drops Stoneclaw on an engaged pet.
- An Elemental shaman holds at 20 yd (shock range) against a ranged foe and plays its rotation's engaged branch (the pull's "mob walks
  in" timing does not hold for a foe that stands still); against a melee it drops Earthbind (Earthbound) and Frost Shock, kites when it
  is faster, starts no cast the melee would reach (or Intercept, in reach and not rooted) before it ends, uses Ghost Wolf when both slows
  are spent, and fights in melee when it cannot get away.
- Healing: the Restoration build keeps Riptide up below RIPTIDE_AT, Healing Wave below HEAL_AT when the cast is safe, Lesser Healing Wave
  below LHW_AT, Nature's Swiftness + Healing Wave below NS_HEAL_AT_HEALER; the others the rotation's emergencies, Lesser Healing Wave below
  EMERGENCY_AT when losing the race, and heals while the foe is held for the cast or sits in Ice Block.
- The trinket (stun, root, slow): stuns as the base layer; a root (a reaction time after it lands) or a 50% slow that holds a melee
  shaman off a kiting foe; a rooted or slowed Elemental with a melee 6-15 yd away when it can keep the distance afterwards.

Not modelled: Strength of Earth, Grace of Air, Windfury Totem (the fight lab counts none of them; Windfury Totem would not stack with the
Windfury Weapon imbue), Stoneskin, Windwall, Healing Stream (11 health a tick), Poison and Disease Cleansing totems, Totemic Call and
Totemic Recall, Chain Heal (on one target, even with Riptide's +25%, it heals less than Healing Wave), Reincarnation (a duel ends at
death), Frostbrand Weapon, Purge of other buffs (Arcane Power, Power Infusion ...), Grounding against Spell Lock (the warlock layer
applies it outside the spell's resolution), a foe that kills totems with single-target attacks (only its area spells do), fake casts,
line of sight.

Assumptions: Grounding's 10 s re-arm (the tooltip) and a damaging spell killing it; the first Earthbind and Tremor pulse when dropped;
SHOCK_HOLD, GROUND_HP and the healing thresholds below are judgment, not measured; Maelstrom's post-hotfix rate 8 a minute at 5/5 (the
middle of the reported 6-10, by rank as the fight lab's). Foe layers do not see totems: a mage casts Counterspell into a standing
Grounding Totem and a warlock Fear, which flatters the shaman against casters.
"""
import collections
import copy
import json
import pathlib
import re
import sys

import dtables as T
import engine as FE
from pvp_base import PvPAI, HEALS

HERE = pathlib.Path(__file__).resolve().parent
TREE_OF = {t["name"]: tr["name"] for tr in json.load(open(HERE.parent / "forever-talents" / "shaman.json", encoding="utf-8"))["trees"]
           for t in tr["talents"]}

# the 2026-11-12 live hotfix (see the docstring)
HOTFIX_1112 = True
SS_WEAPON = 1.00          # Stormstrike's weapon damage, was 1.50
SS_COOLDOWN = 8.0         # was 6 s
MW_PPM_PER_POINT = 1.6    # Maelstrom Weapon procs a minute per talent point: 8 at 5/5 (was 4 per point, 20 at 5/5)

# totems, client 1.60.1.70938 (SpellEffect, SpellMisc, SpellDuration, SpellCooldowns)
EARTHBIND_RADIUS = 10.0   # Earthbind (3600): -50% speed, 5 s, radius index 13; the totem's passive (6474) pulses every 3 s
EARTHBIND_SLOW = 0.5
EARTHBIND_PULSE = 3.0
EARTHBIND_DEBUFF = 5.0
EARTHBOUND_ROOT = 5.0     # Earthbound (1238289): root, 5 s, radius index 13, on the totem's summon
TREMOR_RADIUS = 30.0      # Tremor Totem Effect (8146): dispel charm, fear, sleep, radius index 10; the passive (8145) pulses every 4 s
TREMOR_PULSE = 4.0
GROUND_RADIUS = 30.0      # Grounding Totem (8178): spell magnet, party area aura, radius index 10; "every 10 seconds" (tooltip)
GROUND_PULSE = 10.0
TOTEM_RADIUS = 30.0       # Mana Tide Totem: "within 30 yards"
MANA_TIDE_PULSE = 3.0
SEARING_REACH = 20.0      # "attacks an enemy within 20 yards"
FIRE_NOVA_RADIUS = 10.0   # "within 10 yd of your active Fire totem"
PREDUEL = -3.0            # totems dropped during the duel's countdown (Call of the Elements, a 3 s cast)
WOLF_SPEED = 0.40         # Ghost Wolf: "increasing speed by 40%"

# decisions (judgment)
ELE_RANGE = 20.0          # an Elemental shaman holds here against a ranged foe: Earth and Frost Shock reach 20 yd
SHOCK_HOLD = 2.0          # against a caster, the shocks wait this long for a cast to interrupt before the rotation spends them on damage
GROUND_HP = 0.60          # below this health, Grounding Totem also answers a damage cast (always: crowd control)
PURGE_MIN = 200.0         # an absorb shield worth a Purge
HEAL_AT = 0.55            # Restoration: Healing Wave below this health when the foe cannot punish the cast
LHW_AT = 0.45             # Restoration: Lesser Healing Wave below this
RIPTIDE_AT = 0.85         # Restoration: Riptide below this when its heal over time is not running
NS_HEAL_AT = 0.30         # Nature's Swiftness + Healing Wave below this (the fight lab's emergency line)
NS_HEAL_AT_HEALER = 0.35
FREE_HEAL_AT = 0.50       # any build: a heal below this when the foe is held long enough for the cast
DOWNTIME_HEAL_AT = 0.85   # ... and below this while the foe sits in Ice Block
FINISH_AT = 0.12          # the foe below this share: no heal unless in danger
MANA_TIDE_AT = 0.35
TOTEM_MANA = 0.15         # no utility totem below this share of mana
SHIELD_MANA = 0.25        # Lightning Shield re-cast above this share of mana
WATER_AT = 0.40           # Water Shield instead below this
FIRE_NOVA_MANA = 0.40
WOLF_FROM, WOLF_TO = 14.0, 7.0   # a melee shaman rides Ghost Wolf from this distance until this one
SEARING_EVERY = 12.0      # a new Searing Totem at most this often, and only where the fight stands still
EMERGENCY_AT = 0.35       # any build: Lesser Healing Wave below this when losing the race and no interrupt is ready
KICKED_HEAL_AT = 0.30     # a cast-time heal into a ready melee interrupt only below this health
KITE_FROM = 8.0           # an Elemental starts no cast within this distance of a melee it can outrun

HEALS_ALL = set(HEALS) | {"Riptide", "Holy Shock", "Rejuvenation", "Renew"}
CC_CASTS = {"Polymorph", "Fear", "Seduction", "Hibernate", "Entangling Roots", "Mind Control", "Howl of Terror", "Banish", "Scare Beast"}
GROUND_CC = {"Polymorph", "Fear", "Death Coil", "Hammer of Justice", "Repentance", "Entangling Roots", "Hibernate", "Counterspell",
             "Silence", "Spell Lock", "Mana Burn", "Dispel Magic", "Purge", "Seduction", "Earth Shock", "Frost Shock", "Mind Control",
             "Curse of Tongues", "Curse of Exhaustion", "Curse of Weakness", "Curse of Recklessness", "Faerie Fire", "Banish"}
AREA = {"Frost Nova", "Cone of Cold", "Arcane Explosion", "Blizzard", "Flamestrike", "Blast Wave", "Psychic Scream", "Howl of Terror",
        "Intimidating Shout", "Hellfire", "Rain of Fire", "Holy Nova", "Consecration", "Hurricane", "Volley", "Multi-Shot", "Thunder Clap",
        "Whirlwind", "Cleave", "War Stomp", "Piercing Howl", "Fire Nova", "Magma Totem", "Challenging Shout", "Demoralizing Shout",
        "Demoralizing Roar", "Swipe", "Frost Trap", "Explosive Trap", "Immolation Trap", "Holy Wrath", "Shadowfury"}
FEARS = {"Fear", "Psychic Scream", "Howl of Terror", "Intimidating Shout", "Seduction", "Hibernate", "Wyvern Sting"}
NO_TREMOR = {"Death Coil"}                       # a horror, not a fear
TREMOR_INCAPS = {"Seduction", "Hibernate", "Wyvern Sting"}   # charm and sleep
CASTER_CLASSES = {"mage", "warlock", "priest", "druid", "shaman", "paladin"}   # foes with spells worth grounding and interrupting
MELEE_KICKS = {"Pummel": 0.0, "Kick": 0.0, "Shield Bash": 0.0}                # the foe's interrupts: name -> reach (0: melee)
RANGED_KICKS = {"Counterspell": 30.0, "Earth Shock": 20.0, "Silence": 30.0}   # all groundable
TOTEM_SPELLS = ("Grounding Totem", "Tremor Totem", "Earthbind Totem", "Stoneclaw Totem", "Searing Totem", "Mana Tide Totem")
MANA_TIDE_RX = re.compile(r"restores (\d+) mana every (\d+) sec")


class ShamanPvP(PvPAI):
    keep_range = 0.0
    auto_attack = True

    # ------------------------------------------------------------------ setup
    def bind(self, d, me):
        pts = collections.Counter()
        for n, r in me.alloc.items():
            pts[TREE_OF.get(n)] += r
        self.caster = me.spec.startswith("elemental")
        self.healer = pts["Restoration"] >= 30
        self.keep_range = ELE_RANGE if self.caster else 0.0
        self.auto_attack = True
        self.ranges = {}
        self.x = 0.0                    # this side's position on the line; the foe stands at x + distance
        self._t = -1.0
        self.totems = {}                # slot -> {"name", "x", "until", "next", "every", ...}
        self.wolf = False
        self.ns_plan = None
        self._gcd_saved = (-1.0, 0.0)
        self._periodic = False
        self._casts = {}
        self._fear_until = 0.0
        self.fear_src = None
        self._root_until = 0.0
        self.root_at = -1.0             # when the current root on this side began (the trinket waits a reaction time)
        self.searing_at = -99.0         # this layer's last Searing Totem (the fight lab's at the pull does not count)
        self.shock_ready_at = None
        self.vs_fear = self.vs_casts = self.vs_kick = False
        self.hotfix = []
        self.copy_spells(me)
        self.wrap_module(me)
        self.earthbind_radius = EARTHBIND_RADIUS * (1 + me.mod.tv("Earth's Grasp", 1) / 100)
        wolf = me.mod.spells.get("Ghost Wolf")
        self.wolf_instant = wolf is not None and wolf.cast <= 0
        for k in ("grounded", "tremor", "purged", "es_interrupts", "totems_lost"):
            me.stats.setdefault(k, 0)
        super().bind(d, me)

    def copy_spells(self, me):
        """This side's own copies of the spells it changes (the module's spell objects are shared with every module of the process)."""
        mod, sp = me.mod, me.mod.spells

        def repl(name, **kw):
            s = sp.get(name)
            if s is None:
                return None
            s = copy.copy(s)
            for k, v in kw.items():
                setattr(s, k, v)
            sp[name] = s
            return s

        for name in TOTEM_SPELLS:   # dropped at the feet: no target, no range, no hit roll
            repl(name, target="self", kind="buff")
        g = sp.get("Grounding Totem")
        if g is not None:           # Guardian Totems: "reduces the cooldown of your Grounding Totem by 2 sec" at 2/2
            repl("Grounding Totem", cooldown=max(0.0, g.cooldown - mod.tv("Guardian Totems", 1)))
        w = sp.get("Ghost Wolf")
        if w is not None:           # Improved Ghost Wolf: -1 / -3 s cast (the fight lab: "travel only")
            repl("Ghost Wolf", cast=max(0.0, w.cast - mod.tv("Improved Ghost Wolf", 0)), target="self")
        ss = sp.get("Stormstrike")
        if HOTFIX_1112 and ss is not None and (ss.weapon_pct > SS_WEAPON + 1e-9 or ss.cooldown < SS_COOLDOWN - 1e-9):
            old = ss.weapon_pct or 1.0
            repl("Stormstrike", weapon_pct=SS_WEAPON, coef=ss.coef * SS_WEAPON / old, cooldown=SS_COOLDOWN)
            self.hotfix.append(f"Stormstrike {old:.0%} -> {SS_WEAPON:.0%}, {ss.cooldown:.0f} -> {SS_COOLDOWN:.0f} s")

    def wrap_module(self, me):
        """Instance-level wrappers on this side's own module: the hotfixed Maelstrom rate, no shield charge spent on a dot's tick,
        Nature's Swiftness spent by a damage spell."""
        mod = me.mod
        fsm = sys.modules[type(mod).__module__]
        if HOTFIX_1112 and mod.rank("Maelstrom Weapon") and getattr(fsm, "MW_PPM_PER_POINT", None) != MW_PPM_PER_POINT:
            orig_swing = mod.on_swing
            self.hotfix.append(f"Maelstrom Weapon {fsm.MW_PPM_PER_POINT * 5:.0f} -> {MW_PPM_PER_POINT * 5:.0f} a minute at 5/5")

            def on_swing(fight, spell, outcome, amount, hand):
                old = fsm.MW_PPM_PER_POINT
                fsm.MW_PPM_PER_POINT = MW_PPM_PER_POINT
                try:
                    orig_swing(fight, spell, outcome, amount, hand)
                finally:
                    fsm.MW_PPM_PER_POINT = old
            mod.on_swing = on_swing
        orig_taken = mod.on_hit_taken

        def on_hit_taken(fight, dmg, crit=False):
            if not self._periodic:
                orig_taken(fight, dmg, crit)
        mod.on_hit_taken = on_hit_taken
        if "Nature's Swiftness" in mod.spells:
            orig_after = mod.after_cast

            def after_cast(fight, spell):
                if spell.kind == "spell" and spell.cast > 0 and spell.school == "nature" and fight.p.buff("Nature's Swiftness", fight.t):
                    del fight.p.buffs["Nature's Swiftness"]
                orig_after(fight, spell)
            mod.after_cast = after_cast

    def effects_for(self, me):
        return {"Grounding Totem": self.e_totem, "Tremor Totem": self.e_totem, "Earthbind Totem": self.e_totem,
                "Mana Tide Totem": self.e_totem, "Stoneclaw Totem": self.e_stoneclaw, "Searing Totem": self.e_searing,
                "Fire Nova": self.e_fire_nova, "Purge": self.e_purge, "Ghost Wolf": self.e_wolf,
                "Lightning Shield": self.e_shield, "Water Shield": self.e_shield, "Nature's Swiftness": self.e_ns}

    def prefight(self, d, me, foe):
        self.install_grounding(d, me, foe)
        self._casts = dict(foe.fight.casts)
        if me.mod.fire_totem:   # the fight lab's Searing Totem of the pull
            self.totems["fire"] = {"name": "Searing Totem", "x": self.x, "until": me.mod.fire_totem["until"]}
        self.vs_fear = any(n in foe.mod.spells or n in foe.ai.effects for n in FEARS)
        self.vs_casts = foe.cls in CASTER_CLASSES
        self.vs_kick = any(n in foe.mod.spells for n in RANGED_KICKS)   # a spell interrupt: Grounding is kept for the first cast
        if self.vs_fear:
            self.preplace(d, me, foe, "Tremor Totem")
        if self.vs_casts and not self.vs_kick:
            self.preplace(d, me, foe, "Grounding Totem")
        for h in self.hotfix:
            me.fight.note(f"hotfix 2026-11-12: {h}")

    def preplace(self, d, me, foe, name):
        s = me.mod.spells.get(name)
        if s is None:
            return
        cost = me.mod.mana_cost(s)
        if me.p.mana < cost:
            return
        me.p.mana -= cost
        if s.cooldown:
            me.p.cooldowns[name] = PREDUEL + s.cooldown
        me.fight.casts[name] = me.fight.casts.get(name, 0) + 1
        self.place(d, me, foe, name, PREDUEL)
        me.fight.note(f"{name} placed before the duel")

    # ------------------------------------------------------------------ geometry and totems
    def foe_x(self, d):
        return self.x + d.dist

    def totem(self, slot, t=None):
        tot = self.totems.get(slot)
        t = self.d.t if t is None else t
        return tot if tot is not None and t < tot["until"] else None

    def place(self, d, me, foe, name, t0):
        """A totem at this side's feet (one per element: the old one goes); its first pulse at once."""
        slot = {"Grounding Totem": "air", "Tremor Totem": "earth", "Earthbind Totem": "earth", "Stoneclaw Totem": "earth",
                "Searing Totem": "fire", "Mana Tide Totem": "water"}[name]
        old = self.totem(slot)
        if old is not None:
            self.kill(d, me, foe, slot, f"replaced by {name}", lost=False)
        s = me.mod.spells[name]
        tot = {"name": name, "x": self.x, "until": t0 + (s.totem_dur if name == "Searing Totem" else 45.0)}
        if name == "Grounding Totem":
            tot.update(charge=True, next=t0 + GROUND_PULSE, every=GROUND_PULSE)
        elif name == "Tremor Totem":
            tot.update(until=t0 + 300.0, next=t0, every=TREMOR_PULSE)
        elif name == "Earthbind Totem":
            tot.update(next=t0, every=EARTHBIND_PULSE)
        elif name == "Stoneclaw Totem":
            tot.update(until=t0 + 15.0)
        elif name == "Mana Tide Totem":
            m = MANA_TIDE_RX.search(getattr(s, "text", "") or "")
            tot.update(until=t0 + 12.0, next=t0 + MANA_TIDE_PULSE, every=MANA_TIDE_PULSE, amount=float(m.group(1)) if m else 0.0)
        self.totems[slot] = tot
        if t0 >= d.t - 1e-9:
            self.run_pulses(d, me, foe, slot)
        return tot

    def kill(self, d, me, foe, slot, why, lost=True):
        tot = self.totems.pop(slot, None)
        if tot is None:
            return
        if lost:
            me.stats["totems_lost"] += 1
        me.fight.note(f"{tot['name']} gone ({why})")
        if slot == "fire":
            foe.dots = [x for x in foe.dots if x[0] != "Searing Totem"]
            me.mod.fire_totem = None

    def run_pulses(self, d, me, foe, slot):
        tot = self.totems.get(slot)
        while tot is not None and tot.get("every") and tot["next"] <= min(d.t, tot["until"]) + 1e-9:
            tot["next"] += tot["every"]
            self.pulse(d, me, foe, tot)

    def pulse(self, d, me, foe, tot):
        t, name = d.t, tot["name"]
        if name == "Earthbind Totem":
            if abs(self.foe_x(d) - tot["x"]) <= self.earthbind_radius + 0.5 and t >= foe.immune_until:
                if t >= foe.slow_until or foe.slow <= EARTHBIND_SLOW:
                    foe.slow = EARTHBIND_SLOW
                foe.slow_until = max(foe.slow_until, t + EARTHBIND_DEBUFF)
        elif name == "Tremor Totem":
            if abs(self.x - tot["x"]) <= TREMOR_RADIUS + 0.5:
                freed = []
                if t < me.fear_until and self.fear_src not in NO_TREMOR:
                    me.fear_until = t
                    freed.append(self.fear_src or "fear")
                if t < me.incap_until and me.incap_name in TREMOR_INCAPS:
                    me.incap_until = t
                    freed.append(me.incap_name)
                if freed:
                    me.stats["tremor"] += 1
                    me.fight.note(f"Tremor Totem removes {', '.join(freed)}")
        elif name == "Grounding Totem":
            tot["charge"] = True
        elif name == "Mana Tide Totem":
            if abs(self.x - tot["x"]) <= TOTEM_RADIUS + 0.5:
                me.p.mana = min(me.p.mana_max, me.p.mana + tot["amount"])

    def track(self, d, me, foe):
        """Once a step, whichever hook runs: this side's position, the foe's new casts (area spells on totems, channels on Grounding),
        totem pulses and lifetimes, the Searing Totem's reach, what feared me, the shock's readiness."""
        t = d.t
        if t <= self._t + 1e-9:
            return
        self._t = t
        self.x -= d.velocity(me, t) * T.DT
        if me.fear_until > self._fear_until + 1e-9:
            self.fear_src = me.cc_hint
        self._fear_until = me.fear_until
        if me.root_until > self._root_until + 1e-9 and self._root_until <= t:
            self.root_at = t
        self._root_until = me.root_until
        casts = foe.fight.casts
        for name, n in casts.items():
            if n > self._casts.get(name, 0):
                self.foe_cast_event(d, me, foe, name)
        self._casts = dict(casts)
        for slot in list(self.totems):
            self.run_pulses(d, me, foe, slot)
            tot = self.totems.get(slot)
            if tot is not None and t >= tot["until"]:
                self.kill(d, me, foe, slot, "expired", lost=False)
        self.gate_searing(d, me, foe)
        if me.p.ready("Earth Shock", t):
            if self.shock_ready_at is None:
                self.shock_ready_at = t
        else:
            self.shock_ready_at = None

    def foe_cast_event(self, d, me, foe, name):
        s = foe.mod.spells.get(name)
        if s is None:
            return
        ch = foe.fight.channel
        if s.kind == "channel" and ch and ch[0].name == name and self.ground(d, me, foe, s):
            foe.break_cast("Grounding Totem")
        deals = s.dmg_max > 0 or s.dot > 0 or s.kind in ("melee", "ranged")
        if (s.aoe or name in AREA) and deals:
            r = s.aoe_range or (s.range if s.range > T.MELEE else 10.0)
            cx = self.x if s.aoe_center == "target" else self.foe_x(d)
            for slot, tot in list(self.totems.items()):
                if abs(tot["x"] - cx) <= r + 0.5:
                    self.kill(d, me, foe, slot, name)

    def gate_searing(self, d, me, foe):
        """The fight lab's Searing Totem is a periodic effect on the target: hold its shots while the foe is beyond its reach."""
        dots = [x for x in foe.dots if x[0] == "Searing Totem"]
        if not dots:
            return
        tot = self.totem("fire")
        if tot is None or tot["name"] != "Searing Totem":
            foe.dots = [x for x in foe.dots if x[0] != "Searing Totem"]
            return
        if abs(self.foe_x(d) - tot["x"]) > SEARING_REACH + 0.5:
            for x in dots:
                x[3] = max(x[3], d.t + T.DT + 1e-6)

    # ------------------------------------------------------------------ Grounding Totem
    def install_grounding(self, d, me, foe):
        """Kept for the call in prefight: Grounding now goes through the engine's hook (intercepts, 2026-11-14), not a wrapper."""
        return None

    def intercepts(self, d, me, src, spell):
        """The engine asks before the foe's spell resolves: a groundable spell meets the Grounding Totem instead of the shaman."""
        return self.ground(d, me, src, spell)

    def after_intercept(self, d, me, src, spell):
        self._casts[spell.name] = src.fight.casts.get(spell.name, 0)

    def grounding(self, d, me):
        return bool(self.ground_charged())

    def groundable(self, foe, s):
        if s.kind not in ("spell", "channel") or s.target in ("self", "pet") or s.name in AREA or (s.aoe and s.name != "Chain Lightning"):
            return False
        if s.name in GROUND_CC:
            return True
        return (s.dmg_max > 0 or s.dot > 0 or s.interrupt > 0 or s.stun > 0 or s.fear > 0 or s.root > 0 or s.chill > 0 or s.daze > 0
                or s.name in getattr(foe.ai, "hostile_buffs", ()))

    def ground(self, d, me, foe, s):
        g = self.totem("air")
        if g is None or g["name"] != "Grounding Totem" or not g.get("charge") or abs(self.x - g["x"]) > GROUND_RADIUS + 0.5:
            return False
        if not self.groundable(foe, s):
            return False
        g["charge"] = False
        me.stats["grounded"] += 1
        me.fight.note(f"Grounding Totem takes {s.name}")
        if s.dmg_max > 0 or s.dot > 0:
            self.kill(d, me, foe, "air", s.name)
        return True

    def ground_charged(self):
        g = self.totem("air")
        return g is not None and g["name"] == "Grounding Totem" and g.get("charge") and abs(self.x - g["x"]) <= GROUND_RADIUS

    # ------------------------------------------------------------------ effects
    def e_totem(self, d, me, foe, spell):
        me.fight.note(f"{spell.name} dropped")
        self.place(d, me, foe, spell.name, d.t)
        if spell.name == "Earthbind Totem" and me.mod.rank("Earthbound") and abs(d.dist) <= self.earthbind_radius + 0.5:
            foe.apply_cc("root", EARTHBOUND_ROOT, "root", "Earthbound")
        return 0.0

    def e_stoneclaw(self, d, me, foe, spell):
        """Its taunt works on creatures: a pet in reach turns on the totem until it breaks; a player does not."""
        self.place(d, me, foe, spell.name, d.t)
        pet = foe.p.pet
        if pet is not None and pet.alive and pet.engaged:   # an engaged pet fights at this side's feet (pets have no position)
            hp = getattr(spell, "claw_hp", 0.0) * (1 + me.mod.tv("Earth's Grasp", 0) / 100)
            hit = max(1.0, (pet.dmg_min + pet.dmg_max) / 2 + pet.attack_power / 14.0 * pet.speed) * pet.dmg_mult
            hold = min(getattr(spell, "claw_dur", 15.0), hp / hit * pet.speed)
            pet.swing_at = max(pet.swing_at, d.t + hold)
            me.fight.note(f"Stoneclaw Totem holds {pet.name} {hold:.1f}s")
        else:
            me.fight.note("Stoneclaw Totem: no creature to taunt")
        return 0.0

    def e_searing(self, d, me, foe, spell):
        """A new Searing Totem at the feet, shooting as the fight lab's (on_fight_start's numbers)."""
        fsm = sys.modules[type(me.mod).__module__]
        p, t = me.p, d.t
        self.searing_at = t
        me.fight.note("Searing Totem dropped")
        self.place(d, me, foe, "Searing Totem", t)
        ticks = int(spell.totem_dur / fsm.SEARING_INTERVAL)
        per = ((spell.totem_min + spell.totem_max) / 2 + spell.coef * p.spell_power) * me.mod.damage_multiplier(spell, False)
        crit, mult = p.spell_crit, 1.5 + me.mod.crit_damage_bonus(spell)
        me.fight.refresh_dot("Searing Totem", per * ticks, ticks, fsm.SEARING_INTERVAL, crit, mult)
        me.mod.fire_totem = {"name": "Searing Totem", "until": t + spell.totem_dur, "per": per, "crit": crit, "mult": mult}
        return 0.0

    def e_fire_nova(self, d, me, foe, spell):
        ft = self.totem("fire")
        if ft is None or abs(self.foe_x(d) - ft["x"]) > FIRE_NOVA_RADIUS + 0.5:
            me.fight.note("Fire Nova: no foe by the Fire totem")
            return 0.0
        me.fight.casts[spell.name] -= 1   # counted once already by the duel's resolve_spell
        return FE.Fight.resolve_spell(me.fight, spell)

    def e_purge(self, d, me, foe, spell):
        hit = 1.0 - FE.spell_miss(0) + me.mod.hit_bonus(spell) + me.p.spell_hit
        if d.rng.random() > min(FE.SPELL_HIT_CAP, hit):
            me.fight.note("Purge resisted")
            return 0.0
        gone = []
        if foe.purge_shields():
            gone.append("absorb")
        if d.t < foe.immune_phys_until:
            foe.immune_phys_until = d.t
            gone.append("Blessing of Protection")
        if gone:
            me.stats["purged"] += 1
        else:
            me.fight.note("Purge: nothing to remove")
        return 0.0

    def e_wolf(self, d, me, foe, spell):
        self.wolf = True
        me.speed_bonus["Ghost Wolf"] = (WOLF_SPEED, 1e18)
        self.auto_attack = False
        me.fight.note("Ghost Wolf")
        return 0.0

    def cancel_wolf(self, d, me):
        if self.wolf:
            self.wolf = False
            me.speed_bonus.pop("Ghost Wolf", None)
            self.auto_attack = True
            me.fight.note("Ghost Wolf cancelled")

    def e_shield(self, d, me, foe, spell):
        p = me.p
        me.fight.note(f"{spell.name} up")
        if spell.name == "Water Shield":
            p.buffs["Shield"] = {"until": d.t + 600.0, "charges": 3, "kind": "water", "icd": 0.0}
        else:
            p.buffs["Shield"] = {"until": d.t + 600.0, "charges": 3, "kind": "lightning", "icd": 0.0,
                                 "dmg": spell.shield_dmg + spell.coef * p.spell_power}
        return 0.0

    def e_ns(self, d, me, foe, spell):
        """Nature's Swiftness: the buff (the fight lab's on_hit) and no global cooldown (client: StartRecoveryTime 0)."""
        me.p.buffs["Nature's Swiftness"] = {"until": d.t + 60.0}
        at, gcd = self._gcd_saved
        if abs(at - d.t) < 1e-9:
            me.p.gcd_until = gcd
        else:   # the rotation's own emergency Nature's Swiftness (on its global cooldown, now free): a heal
            me.p.gcd_until, self.ns_plan = d.t, "heal"
        me.fight.note(f"Nature's Swiftness ({self.ns_plan})")
        return 0.0

    # ------------------------------------------------------------------ helpers
    def heal_kicked(self, d, me, foe):
        """A cast-time heal started now would be interrupted: a melee interrupt ready beside this side, or a spell interrupt ready
        with no Grounding Totem standing or castable to take it."""
        if self.foe_kick(d, foe, ranged=False, pet=True):
            return True
        return self.foe_kick(d, foe, melee=False) is not None and not self.ground_charged() and not me.can("Grounding Totem")

    def stoneclaw_ok(self, d, foe):
        """Stoneclaw Totem is worth its Earth slot: a live pet engaged on this side, and no Tremor Totem standing against a foe that
        fears."""
        pet, tr = foe.p.pet, self.totem("earth")
        if pet is None or not pet.alive or not pet.engaged or pet.swing_at > d.t + 1.0:
            return False
        return not (self.vs_fear and tr is not None and tr["name"] == "Tremor Totem")

    def foe_busy(self, d, me, foe):
        """Seconds the foe cannot hurt this side: held by control, inside Ice Block, or a melee rooted out of reach."""
        t = d.t
        if t < foe.inactive_until:
            return foe.inactive_until - t
        cc = max(foe.stun_until, foe.incap_until, foe.fear_until) - t
        if cc > 0:
            return cc
        if self.melee_foe(foe) and foe.body.rooted(t) and d.dist > T.MELEE + 1.0:
            return foe.root_until - t
        return 0.0

    def cast_time(self, me, name):
        s = me.mod.spells.get(name)
        return me.mod.cast_time(s) if s is not None else 99.0

    def foe_kick(self, d, foe, ranged=True, melee=True, pet=False):
        """An interrupt the foe could put on this side's next cast now (cooldowns are visible: players watch for them). melee: Pummel,
        Kick, Shield Bash beside this side; ranged: the spell interrupts Grounding Totem can take; pet: a Felhunter's Spell Lock (the
        warlock layer applies it outside the spell's resolution, so Grounding does not see it)."""
        t = d.t
        if foe.controlled(t) or t < foe.inactive_until:
            return None
        for name, reach in (list(MELEE_KICKS.items()) if melee else []) + (list(RANGED_KICKS.items()) if ranged else []):
            s = foe.mod.spells.get(name)
            if s is None or not foe.p.ready(name, t) or (name == "Shield Bash" and foe.p.block <= 0):
                continue
            if reach > 0 and (d.dist > reach or foe.silenced(t) or foe.school_locked(s.school, t)):
                continue
            if reach <= 0 and (d.dist > T.MELEE + 0.5 or t < foe.disarm_until):
                continue
            return name
        p = foe.p.pet
        if pet and p is not None and p.alive and p.name == "Felhunter" and "Spell Lock" in foe.mod.spells \
                and p.cooldowns.get("Spell Lock", -1.0) <= t:
            return "Spell Lock"
        return None

    def arrival(self, d, foe):
        """Seconds until a melee foe can swing at this side: its control left, then the walk at its speed (a charge in reach: at once).
        Charges follow the game's rule, not usable while rooted (the engine allows it)."""
        t = d.t
        held = max(0.0, max(foe.root_until, foe.stun_until, foe.incap_until, foe.fear_until) - t)
        if not held and 8.0 <= d.dist <= 25.0 and any(n in foe.mod.spells and foe.p.ready(n, t)
                                                      for n in getattr(foe.ai, "charges", ()) if n != "Charge"):
            return 0.5
        slow = foe.slow if t + held < foe.slow_until else 0.0
        return held + max(0.0, d.dist - T.MELEE) / max(0.1, T.RUN_SPEED * (1.0 - slow))

    def casting_spell(self, me, a):
        """The Spell an action would start as a cast (None for instants and movement)."""
        s = me.mod.spells.get(a) if isinstance(a, str) else a
        if s is None or not hasattr(s, "kind") or s.kind in ("melee", "ranged"):
            return None
        return s if me.mod.cast_time(s) > 0 else None

    def worth_interrupt(self, c):
        if c.kind == "heal" or c.name in HEALS_ALL or c.name in CC_CASTS or c.kind == "channel":
            return True
        return c.cast >= 1.4 and (c.dmg_max > 0 or c.dot > 0)

    def burst_damage(self, me, name):
        s = me.mod.spells.get(name)
        if s is None:
            return 0.0
        p = me.p
        avg = (s.dmg_min + s.dmg_max) / 2 + s.coef * p.spell_power
        crit = min(1.0, p.spell_crit + me.mod.crit_bonus(s, False))
        return avg * me.mod.damage_multiplier(s, False) * (1 + crit * (0.5 + me.mod.crit_damage_bonus(s)))

    def vetoed(self, me, off, fn):
        """Run fn with the named spells counted as unaffordable (the fight lab's veto rule): the rotation takes its next choice."""
        mod = me.mod
        old = mod.veto
        if off:
            mod.veto = {n: {"off": True} for n in off}
        try:
            return fn()
        finally:
            mod.veto = old

    # ------------------------------------------------------------------ hooks
    def damage_taken(self, d, me, src, spell, amount):
        self._periodic = any(x[0] == spell.name and x[3] <= d.t + 1e-6 for x in me.dots)
        school = getattr(spell, "school", "") or ""
        if me.mod.rank("Elemental Warding") and any(k in school for k in ("fire", "frost", "nature")):
            amount *= 1 - me.mod.tv("Elemental Warding", 0) / 100
        return amount

    def intent(self, d, me, foe):
        t = d.t
        if foe.stealthed and not me.stealthed:
            return "hold"
        if not self.caster:
            return "close"
        if self.melee_foe(foe):
            stuck = foe.body.rooted(t) or foe.controlled(t)
            if self.wolf or (stuck and d.dist < 22.0):
                return "kite"
            if d.dist < 10.0 and me.speed(t) > foe.speed(t) * 1.05:
                return "kite"
            return "hold"
        return "close" if d.dist > ELE_RANGE else "hold"

    def while_inactive(self, d, me, foe):
        self.track(d, me, foe)
        return None

    def while_casting(self, d, me, foe):
        self.track(d, me, foe)
        return None

    def while_controlled(self, d, me, foe):
        self.track(d, me, foe)
        if self.wolf and d.t < me.incap_until:
            self.cancel_wolf(d, me)
        if not me.controlled(d.t):   # Tremor freed this side in this step
            return None
        return super().while_controlled(d, me, foe)

    def off_gcd(self, d, me, foe):
        self.track(d, me, foe)
        t = d.t
        k = self.trinket_choice(d, me, foe)
        if k:
            return k
        if "Nature's Swiftness" in me.mod.spells and not me.p.buff("Nature's Swiftness", t) and me.p.gcd_until <= t + 1e-6 \
                and me.can("Nature's Swiftness", ignore_gcd=True):   # with the global cooldown free: its spell follows in this step
            plan = self.ns_wanted(d, me, foe)
            if plan:
                self.ns_plan = plan
                self._gcd_saved = (t, me.p.gcd_until)
                self.cancel_wolf(d, me)
                return "Nature's Swiftness"
        return None

    def trinket_choice(self, d, me, foe):
        """Roots and slows (stuns: the base layer's while_controlled). A reaction time after the root lands."""
        t = d.t
        frees = me.trinket_frees(t)
        if not frees or t < foe.immune_until:
            return None
        rooted = "root" in frees and t - self.root_at >= T.REACTION
        if not self.caster:   # held off a ranged or fleeing foe
            if self.melee_foe(foe) and foe.intent != "kite":
                return None
            if rooted and me.root_until - t >= 2.5 and d.dist > 8.0:
                return "trinket"
            if "slow" in frees and me.slow >= 0.5 and me.slow_until - t >= 2.5 and d.dist > 15.0 and foe.intent == "kite" \
                    and me.speed(t) <= foe.speed(t) and me.hp_frac() < 0.8:
                return "trinket"
            return None
        # Elemental: held near a melee that is coming (not one already beside it: it would hold it again), with a way to keep the gap
        if not self.melee_foe(foe) or not T.MELEE + 1.0 < d.dist <= 15.0 or me.hp_frac() > 0.75:
            return None
        held = (rooted and me.root_until - t >= 2.0) or ("slow" in frees and me.slow >= 0.5 and me.slow_until - t >= 3.0)
        foe_free = not foe.controlled(t) and not foe.body.rooted(t) and not (t < foe.slow_until and foe.slow >= 0.45)
        can_keep = any(me.can(n, ignore_gcd=True) for n in ("Frost Shock", "Earthbind Totem")) \
            or (self.wolf_instant and me.can("Ghost Wolf", ignore_gcd=True))
        return "trinket" if held and foe_free and can_keep else None

    def ns_wanted(self, d, me, foe):
        t, hp = d.t, me.hp_frac()
        if t < foe.immune_until:
            return None
        at = NS_HEAL_AT_HEALER if self.healer else NS_HEAL_AT
        if hp < at and foe.hp_frac() > FINISH_AT and me.can("Healing Wave", ignore_gcd=True):
            return "heal"
        if self.caster and hp > 0.35:
            for n in ("Chain Lightning", "Lightning Bolt"):
                if me.can(n, ignore_gcd=True) and foe.p.hp <= self.burst_damage(me, n):
                    return "burst"
        return None

    def decide(self, d, me, foe):
        self.track(d, me, foe)
        if foe.stealthed:
            return self.shield_choice(d, me, foe)
        must = self.urgent(d, me, foe)
        if self.wolf:
            if must is None and self.keep_wolf(d, me, foe):
                return None
            self.cancel_wolf(d, me)
        if must is not None:
            return must
        for step in (self.heal_choice, self.gap_choice, self.totem_choice, self.shield_choice, self.wolf_choice, self.rotation_choice,
                     self.filler):
            a = step(d, me, foe)
            if a is not None:
                return self.before_cast(d, me, foe, a)
        return None

    def before_cast(self, d, me, foe, a):
        """A cast-time spell while the foe holds a spell interrupt that Grounding Totem can take (Counterspell, Earth Shock, Silence):
        the totem first."""
        if self.casting_spell(me, a) is None:
            return a
        kick = self.foe_kick(d, foe, melee=False)
        if kick is not None and not self.ground_charged() and me.can("Grounding Totem"):
            return "Grounding Totem"
        return a

    # ------------------------------------------------------------------ decisions
    def urgent(self, d, me, foe):
        """What cannot wait: Nature's Swiftness' instant spell, an interrupt, Grounding against a cast, a Purge."""
        t = d.t
        if me.p.buff("Nature's Swiftness", t):
            if self.ns_plan == "burst":
                for n in ("Chain Lightning", "Lightning Bolt"):
                    if me.can(n):
                        return n
            if me.hp_frac() < 0.9:
                for n in ("Healing Wave", "Lesser Healing Wave"):
                    if me.can(n):
                        return n
        if t < foe.immune_until:
            return None
        c = self.foe_cast(d, foe)
        if c is not None:
            if self.worth_interrupt(c) and me.can("Earth Shock"):
                me.stats["es_interrupts"] += 1
                return "Earth Shock"
            left = foe.cast_end() - t if foe.fight.casting else 1.0
            if self.groundable(foe, c) and left > 0.1 and not self.ground_charged() and me.can("Grounding Totem") \
                    and (c.name in GROUND_CC or me.hp_frac() < GROUND_HP):
                return "Grounding Totem"
        if me.can("Purge") and ((t < foe.p.absorb_until and foe.p.absorb >= PURGE_MIN)
                                or (t < foe.immune_phys_until and not self.caster)):
            return "Purge"
        return None

    def heal_choice(self, d, me, foe):
        t, hp = d.t, me.hp_frac()
        if foe.hp_frac() < FINISH_AT and hp > 0.25 and t >= foe.immune_until:
            return None
        busy = self.foe_busy(d, me, foe)
        if t < foe.inactive_until:   # Ice Block: top up while it lasts (the mage may leave it early)
            for n in ("Healing Wave", "Lesser Healing Wave"):
                if hp < DOWNTIME_HEAL_AT and self.cast_time(me, n) <= busy and me.can(n):
                    return n
        kicked = self.heal_kicked(d, me, foe)
        if not self.healer and hp < EMERGENCY_AT and foe.hp_frac() > hp + 0.10 and not kicked:
            for n in ("Lesser Healing Wave", "Healing Wave"):
                if me.can(n):
                    return n
        if self.healer:
            if hp < RIPTIDE_AT and not any(h[0] == "Riptide" for h in me.p.hots) and me.can("Riptide"):
                return "Riptide"
            if hp >= KICKED_HEAL_AT and kicked:
                return None   # a cast now would be interrupted (and lock Nature): only below KICKED_HEAL_AT
            close = self.melee_foe(foe) and d.dist <= 8.0 and not foe.controlled(t)
            if hp < LHW_AT and close and me.can("Lesser Healing Wave"):
                return "Lesser Healing Wave"
            if hp < HEAL_AT and (busy >= self.cast_time(me, "Healing Wave") or not close or me.mod.rank("Healing Focus") >= 2) \
                    and me.can("Healing Wave"):
                return "Healing Wave"
            if hp < LHW_AT and me.can("Lesser Healing Wave"):
                return "Lesser Healing Wave"
            return None
        if hp < FREE_HEAL_AT and busy > 0:
            for n in ("Healing Wave", "Lesser Healing Wave"):
                if self.cast_time(me, n) <= busy + 0.2 and me.can(n):
                    return n
        return None

    def gap_choice(self, d, me, foe):
        """Slows and roots: an Elemental keeps a melee away; a melee shaman keeps a kiting foe in reach."""
        t = d.t
        if t < foe.immune_until:
            return None
        free = not foe.controlled(t) and not foe.body.rooted(t)
        slowed = t < foe.slow_until and foe.slow >= 0.45 and foe.slow_until - t > 1.0
        if self.caster:
            if not self.melee_foe(foe) or not free:
                return None
            if d.dist <= self.earthbind_radius and (me.mod.rank("Earthbound") or not slowed) and me.can("Earthbind Totem"):
                return "Earthbind Totem"
            if not slowed and d.dist <= 20.0 and me.can("Frost Shock"):
                return "Frost Shock"
            return None
        if not free or self.melee_foe(foe):
            return None
        if d.dist <= T.MELEE + 0.5:
            if me.mod.rank("Earthbound") and me.can("Earthbind Totem"):
                return "Earthbind Totem"
            return None
        # a kiting foe, or a ranged one with no casts worth keeping the shock for (a hunter)
        if (foe.intent == "kite" or not self.vs_casts) and not slowed and me.speed(t) > 0 and me.can("Frost Shock"):
            return "Frost Shock"
        return None

    def totem_choice(self, d, me, foe):
        t, mana = d.t, me.mana_frac()
        if mana < MANA_TIDE_AT and me.can("Mana Tide Totem"):
            return "Mana Tide Totem"
        if mana < TOTEM_MANA:
            return None
        tr = self.totem("earth")
        if self.vs_fear:   # a Tremor Totem within reach; an Earthbind in the slot stays until it is gone
            if (tr is None or (tr["name"] == "Tremor Totem" and abs(self.x - tr["x"]) > TREMOR_RADIUS - 2.0)) and me.can("Tremor Totem"):
                return "Tremor Totem"
        if self.stoneclaw_ok(d, foe) and me.can("Stoneclaw Totem"):   # a pet on this side: the totem takes it
            return "Stoneclaw Totem"
        # a Searing Totem where the fight stands: a melee foe at hand, or a foe held near this side (not one kiting away)
        ft = self.totem("fire")
        reach = ft is not None and ft["name"] == "Searing Totem" and abs(self.foe_x(d) - ft["x"]) <= SEARING_REACH
        held = foe.controlled(t) or foe.body.rooted(t) or t < foe.inactive_until
        still = (self.melee_foe(foe) and d.dist <= 8.0) or (held and d.dist <= SEARING_REACH - 2.0) \
            or (self.caster and not self.melee_foe(foe) and foe.intent != "kite" and d.dist <= SEARING_REACH)
        if not reach and still and t - self.searing_at >= SEARING_EVERY and foe.hp_frac() > 0.25 and me.can("Searing Totem"):
            return "Searing Totem"
        return None

    def shield_choice(self, d, me, foe):
        sh = me.p.buffs.get("Shield")
        if sh is not None and sh.get("charges", 0) > 0:
            return None
        mana = me.mana_frac()
        if "Water Shield" in me.mod.spells and mana < WATER_AT and me.can("Water Shield"):
            return "Water Shield"
        if mana > SHIELD_MANA and me.can("Lightning Shield"):
            return "Lightning Shield"
        return None

    def wolf_choice(self, d, me, foe):
        t = d.t
        if self.wolf or not self.wolf_instant or me.speed(t) <= 0 or me.hp_frac() < 0.3 or t < foe.immune_until:
            return None
        if not self.caster:
            if not self.melee_foe(foe) and d.dist > WOLF_FROM and me.can("Ghost Wolf"):
                return "Ghost Wolf"
            return None
        if self.melee_foe(foe) and d.dist < 12.0 and not foe.controlled(t) and not foe.body.rooted(t) \
                and not (t < foe.slow_until and foe.slow >= 0.45) and not me.p.ready("Frost Shock", t) \
                and not me.p.ready("Earthbind Totem", t) and me.can("Ghost Wolf"):
            return "Ghost Wolf"
        return None

    def keep_wolf(self, d, me, foe):
        t = d.t
        if me.hp_frac() < 0.35:
            return False
        if not self.caster:
            return not self.melee_foe(foe) and d.dist > WOLF_TO
        return self.melee_foe(foe) and d.dist < ELE_RANGE and not foe.controlled(t) and not foe.body.rooted(t)

    def hold_shock(self, d, me, foe):
        """Against a caster, keep the shared shock cooldown for an interrupt a little while (the interrupt itself is urgent())."""
        t = d.t
        if not self.vs_casts or self.shock_ready_at is None or t - self.shock_ready_at >= SHOCK_HOLD or foe.hp_frac() < 0.25:
            return False
        ss = me.p.buff("Stormstrike", t)
        return not (ss and ss["until"] - t < SHOCK_HOLD)

    def rotation_choice(self, d, me, foe):
        t = d.t
        if t < foe.immune_until:
            return None
        off = set()
        if not self.stoneclaw_ok(d, foe):   # the rotation's emergency Stoneclaw: players are not taunted
            off.add("Stoneclaw Totem")
        if self.hold_shock(d, me, foe):
            off |= {"Earth Shock", "Flame Shock", "Frost Shock"}
        moving = me.speed(t) > 0
        melee_foe = self.melee_foe(foe)
        gaining = foe.intent != "kite" or me.speed(t) > foe.speed(t) * 1.05
        no_cast = (not self.caster and not melee_foe and d.dist > T.MELEE + 0.5 and moving and gaining)   # closing on a ranged foe
        if self.caster and melee_foe and d.dist < KITE_FROM and moving and (me.speed(t) > foe.speed(t) * 1.05 or not foe.speed(t)):
            no_cast = True   # an Elemental beside a melee it can outrun: walk first
        if self.caster and melee_foe and d.dist > T.MELEE + 0.5 and any(n in foe.mod.spells for n in MELEE_KICKS):
            for n in ("Lightning Bolt", "Chain Lightning"):   # a melee that would arrive before the cast ends interrupts it
                if 0 < self.cast_time(me, n) and self.arrival(d, foe) < self.cast_time(me, n) + T.REACTION:
                    off.add(n)
        if self.foe_kick(d, foe, ranged=False):
            no_cast = True   # a melee interrupt ready beside this side: instants only
        if self.foe_kick(d, foe, melee=False) and not self.ground_charged() and not me.can("Grounding Totem", ignore_gcd=True):
            no_cast = True   # a spell interrupt ready and no Grounding Totem to take it: instants until one of them changes
        if self.heal_kicked(d, me, foe) and me.hp_frac() >= KICKED_HEAL_AT:
            off |= {"Healing Wave", "Lesser Healing Wave", "Chain Heal"}   # the rotation's own emergency heals too
        if no_cast:
            for n in ("Lightning Bolt", "Chain Lightning"):
                if self.cast_time(me, n) > 0:
                    off.add(n)
        a = self.vetoed(me, off, lambda: self.rotation(d, me, foe))
        if a is None and self.caster and not self.melee_foe(foe):
            if d.dist > 20.0:
                off |= {"Earth Shock", "Flame Shock", "Frost Shock"}
            a = self.vetoed(me, off, lambda: self.engaged(d, me, foe))
        return a

    def engaged(self, d, me, foe):
        """Elemental against a foe that stands at range: its rotation's engaged branch (the pull's walk-in timing does not apply)."""
        mod, f, p, t = me.mod, me.fight, me.p, d.t

        def can(s):
            return s is not None and p.ready(s.name, t) and f.can_afford(s, mod.mana_cost(s))
        a = mod.decide_elemental(f, can, True)
        name = getattr(a, "name", a)
        return a if name and me.can(name) else None

    def filler(self, d, me, foe):
        t = d.t
        if t < foe.immune_until:
            return None
        ft = self.totem("fire")
        if ft is not None and abs(self.foe_x(d) - ft["x"]) <= FIRE_NOVA_RADIUS and me.mana_frac() > FIRE_NOVA_MANA and me.can("Fire Nova"):
            return "Fire Nova"
        if not self.caster and t < me.disarm_until and d.dist <= T.MELEE + 0.5 and not self.foe_kick(d, foe, ranged=False):
            if me.hp_frac() < 0.6 and me.can("Lesser Healing Wave"):   # disarmed, no interrupt ready: a heal or a bolt
                return "Lesser Healing Wave"
            if me.mana_frac() > 0.4 and me.can("Lightning Bolt"):
                return "Lightning Bolt"
        if self.caster and self.melee_foe(foe) and d.dist < 15.0 and me.speed(t) > foe.speed(t) * 1.05:
            return "retreat"
        return None
