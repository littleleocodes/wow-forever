"""Hunter PvP layer (duellab, 2026-11-14): range kept against melee (the 8-yard dead zone where neither a bow nor a melee weapon reaches,
stutter-step kiting that stands only for Auto Shot), Concussive Shot, Wing Clip, Freezing and Frost Traps placed at the hunter's feet,
Scatter Shot, the pet's Intimidation, Counterattack, Deterrence, Feign Death against control casts, Viper Sting against mana users,
Bestial Wrath, Flare against stealth, the PvP trinket against stuns, roots and slows. Damage (Auto Shot, Hunter's Mark, Serpent Sting,
Arcane Shot, Summon Hawk, Multi-Shot, Aimed Shot; the melee build's Raptor Strike, Mongoose Bite, Strider Kick, Lacerate, Immolation
Trap) is the spec's own leveling rotation underneath. The ranged builds (Beast Mastery, Marksmanship) keep their distance; the Survival
build plays the fight lab's melee hunter (dual wield, Aspect of the Beast) and closes in like a warrior, slowing with Wing Clip and
Concussive Shot. Aspect of the Hawk (or the melee build's Aspect of the Beast) is up all duel, as in the fight lab's make_player.

Traps (wowsims/forever sim/hunter/traps.go at ff9babba5: "Forever lets traps be placed in combat; a trap lies where the hunter stood and
springs on a target within this radius once armed": a 5-yard trigger radius and a 0.5 s arming time, both marked "in-game testing
required"; TRAPS_IN_COMBAT = False makes a trap need Feign Death first, Classic Era's rule). The duel is a line, so the layer keeps the
hunter's own position (its movement each step) and the trap's; the opponent springs a trap when it comes within 5 yards of it. Freezing
Trap: an incapacitate of up to 20 s (Clever Traps +15% a rank; capped at 10 s on a player), broken by any damage (the hunter's own dots
and hawks included). Frost Trap: a 10-yard ice slick for 30 s (Clever Traps), 60% slower inside it. Immolation Trap: its burn (the melee
rotation casts it). Entrapment roots for 1 s a rank on every trap. Traps hit as spells (4% miss against a same-level player, less
Survival Tactics). All traps share one 30 s cooldown (the fight lab's after_cast).

Effects the fight lab does not parse, handled here: the traps; Scatter Shot (4 s disorient, broken by damage; usable inside the dead zone
as in the game: Classic's 15-yard shot has no minimum range); Feign Death (the opponent's cast at the hunter fails; 4% resisted less
Survival Tactics; off the global cooldown); Viper Sting (1,108 mana drained over 8 s in four ticks; one sting per hunter, so it
replaces Serpent Sting); Counterattack's 5 s root; Strider Kick's +30% run speed for 3 s; Intimidation and Bestial Wrath re-cast in the
duel (the fight lab casts them once, on the pull); Flare (reveals a stealthed opponent within 40 yards: a 30-yard cast and a 10-yard
area); Surefooted (movement impairing effects on the hunter 30% shorter: the slow or root is cut when it lands). The defender's dodge and
parry hooks never run in a duel (only the fight lab's mob swing calls them), so the opponent's attack table is wrapped for the duel: a
dodge opens Mongoose Bite and a parry Counterattack, as in the fight lab. Improved Concussive Shot's stun and Improved Wing Clip's root
keep their own names and diminishing-returns categories (random stun, random root), and so does the pet's Intimidation stun (a
controlled stun). The pet holds its swings and the hunter its Auto Shot and melee swings while its own Freezing Trap or Scatter Shot
holds the opponent; a held opponent gets the hunter's Aimed Shot as the control ends. The first Auto Shot waits for the 0.5 s
stand-still from the duel's start (Blizzard's 16 Oct notes), so it does not open combat before a warrior's Charge.

Decisions (ranged builds): against a free melee, Counterattack's root after a parry, Wing Clip, then a trap at the hunter's feet within
15 yards (Freezing Trap while the incapacitate category is fresh, else Frost Trap), Scatter Shot and Intimidation only when the hunter
cannot outrun it (rooted, or no faster), Concussive Shot on one coming in; kiting out of the dead zone, away from a held melee, and
stutter-stepping from a slowed one; no Aimed or Sniper Shot cast with a free melee closer than 22 yards (12 when it is slowed); Deterrence
below half health with a melee on the hunter; the trinket on a root or slow with a melee close and no other answer ready. Against any
opponent: Feign Death on a seen control cast, Scatter Shot (15 yards) or Intimidation on a control or heal cast; Viper Sting on a mana
user above 30% mana when Serpent Sting is not running and its drain is a quarter of the foe's pool or more (the self-healers with small
pools; validation pass 2, want_viper); Bestial Wrath on cooldown. The Survival build closes in, Wing Clips a free
opponent and Concussive Shots one that runs; its rotation does the rest.

Not modelled: the opponent cannot attack, slow, control or dispel the pet (the engine never targets pets); aspect swaps (Aspect of the
Monkey in melee, Cheetah); Disengage (a threat drop in Forever) and Distracting Shot; Explosive Trap and Volley; Scorpid Sting; Hunter's
Mark's sight through stealth; Hawk Eye's extra range (Auto Shot reaches 35 yards in the engine); Feign Death's loss of target for the
opponent's auto attacks; Counterattack can still be dodged or parried here; a trap the opponent walks around.
"""
import copy
import re

import dtables as T
import engine as FE
import tables as FT
from pvp_base import PvPAI, HEALS

EPS = 1e-9
TRAPS_IN_COMBAT = True       # wowsims/forever's reading; False = Classic Era (a trap needs Feign Death to drop combat first)
TRAP_RADIUS = 5.0            # yards (wowsims/forever traps.go)
TRAP_ARM = 0.5               # seconds (wowsims/forever traps.go)
TRAP_LIFE = 60.0             # "Trap will exist for 1 min"
SLICK_RADIUS = 10.0          # Frost Trap: "All enemies within 10 yards will be slowed"
FD_WINDOW = 2.0              # seconds after Feign Death in which combat counts as dropped (TRAPS_IN_COMBAT off)
KEEP = 30.0                  # the ranged builds' distance (Auto Shot reaches 35)
FREEZE = {"Freezing Trap", "Scatter Shot"}   # this layer's controls that damage breaks
OFF_GCD = {"Feign Death", "Deterrence", "Bestial Wrath", "Rapid Fire"}   # the client's own (fightlab/spell_gcd.json off_gcd)
CC_CASTS = {"Polymorph", "Fear", "Howl of Terror", "Seduction", "Hibernate", "Mind Control", "Entangling Roots", "Scare Beast"}
MANA_FOES = {"mage", "priest", "warlock", "druid", "shaman", "paladin", "hunter"}
VIPER_SHARE = 0.25           # Viper Sting only on a pool its drain cuts by this share or more (validation pass 2: want_viper)


def dr_factor(side, cat, t):
    if not cat:
        return 1.0
    rec = side.dr.get(cat)
    n = rec[0] if rec and t < rec[1] + T.DR_RESET else 0
    return T.DR_STEPS[min(n, len(T.DR_STEPS) - 1)]


def _num(rx, text, default):
    m = re.search(rx, text or "")
    return float(m.group(1).replace(",", "")) if m else default


class HunterPvP(PvPAI):
    keep_range = KEEP
    auto_attack = True
    ranges = {"Scatter Shot": 15.0, "Freezing Trap": 1e9, "Frost Trap": 1e9, "Immolation Trap": 1e9, "Explosive Trap": 1e9,
              "Flare": 1e9, "Enchanted Flare": 1e9}

    def bind(self, d, me):
        super().bind(d, me)
        mod = me.mod
        self.melee_spec = mod.is_melee()
        self.keep_range = 0.0 if self.melee_spec else KEEP
        self.last_step = -1.0
        self.gcd_before = 0.0
        self.x = 0.0                 # my position on the line (the opponent stands at x + distance)
        self.trap = None             # the trap on the ground: {name, spell, x, armed, expires, sprung, slick_until}
        self.viper = None            # {next, ticks, per}
        self.feigned = -99.0
        self.seen_slow = self.seen_root = 0.0
        self.surefooted = mod.tv("Surefooted", 1) / 100
        sp = mod.spells
        for name in ("Freezing Trap", "Frost Trap", "Immolation Trap", "Explosive Trap", "Flare", "Enchanted Flare"):
            if name in sp:   # placed at the hunter's feet or on an area: no target needed (a stealthed opponent included)
                sp[name] = copy.copy(sp[name])
                sp[name].target = "self"
        if "Scatter Shot" in sp:   # a 15-yard shot with no minimum range (the engine's ranged attacks need 8 yards)
            s = copy.copy(sp["Scatter Shot"])
            s.kind = "spell"
            sp["Scatter Shot"] = s
        if "Viper Sting" in sp:   # Improved Stings: "reduces the cooldown of your Viper Sting ability by 6 sec" at 3/3
            s = copy.copy(sp["Viper Sting"])
            s.cooldown = max(0.0, s.cooldown - mod.tv("Improved Stings", 1))
            sp["Viper Sting"] = s

    def effects_for(self, me):
        fx = {name: self.place_trap for name in ("Freezing Trap", "Frost Trap", "Immolation Trap")}
        fx.update({"Feign Death": self.feign, "Scatter Shot": self.scatter, "Viper Sting": self.viper_sting, "Counterattack": self.counter,
                   "Wing Clip": self.wing_clip, "Concussive Shot": self.concussive, "Intimidation": self.intimidation,
                   "Bestial Wrath": self.wrath, "Deterrence": self.deterrence, "Strider Kick": self.strider, "Flare": self.flare,
                   "Enchanted Flare": self.flare})
        return fx

    def prefight(self, d, me, foe):
        """The first Auto Shot waits for the 0.5 s stand-still from the duel's start (the engine's attack phase would fire it at 0.00,
        before either side decides, and start combat, which ends a warrior's Charge before it is cast). The opponent's attack table,
        wrapped for the duel: my dodges and parries reach my module (Mongoose Bite, Counterattack)."""
        me.p.shot_at = max(me.p.shot_at, FT.AUTO_SHOT_STAND_STILL)
        # (the engine calls my module's on_dodge / on_parry itself since 2026-11-14: Side.defend; the wrapper that did it is gone)

    # ------------------------------------------------------------------ helpers
    def lands(self, me, bonus=0.0):
        hit = 1.0 - FT.spell_miss(0) + me.p.spell_hit + bonus
        return me.fight.rng.random() <= min(FT.SPELL_HIT_CAP, hit)

    def held_by_me(self, foe, t):
        """My Freezing Trap or Scatter Shot holds the opponent (damage would end it)."""
        return t < foe.incap_until and foe.incap_breaks and foe.incap_name in FREEZE

    def slowed(self, foe, t, at_least=0.3, left=0.5):
        return t + left < foe.slow_until and foe.slow >= at_least

    def restore_gcd(self, me, spell):
        if spell.name in OFF_GCD:
            me.p.gcd_until = self.gcd_before

    def trap_ready(self, d, me, name):
        if name not in me.mod.spells or self.trap is not None and not self.trap["sprung"]:
            return False
        if not TRAPS_IN_COMBAT and d.combat and d.t - self.feigned > FD_WINDOW:
            return False
        return me.can(name)

    def foe_x(self, d):
        return self.x + d.dist

    # ------------------------------------------------------------------ effects
    def place_trap(self, d, me, foe, spell):
        self.trap = {"name": spell.name, "spell": spell, "x": self.x, "armed": d.t + TRAP_ARM, "expires": d.t + TRAP_LIFE,
                     "sprung": False, "slick_until": 0.0}
        me.fight.note(f"{spell.name} placed")
        return 0.0

    def spring(self, d, me, foe):
        tr, t, mod = self.trap, d.t, me.mod
        tr["sprung"] = True
        name, spell = tr["name"], tr["spell"]
        foe.stealthed = False
        if not self.lands(me, mod.tv("Survival Tactics", 0) / 100):
            me.fight.note(f"{name} resisted")
            return
        me.fight.note(f"{name} springs")
        if mod.rank("Entrapment"):
            foe.apply_cc("root", mod.tv("Entrapment", 0), T.DR_CATEGORY.get("Entrapment"), "Entrapment")
        clever = 1 + mod.tv("Clever Traps", 0) / 100
        if name == "Freezing Trap":
            foe.apply_cc("incap", _num(r"for up to (\d+) sec", spell.text, 20.0) * clever, T.DR_CATEGORY.get(name, "incap"), name)
        elif name == "Frost Trap":
            tr["slick_until"] = t + _num(r"around itself for (\d+) sec", spell.text, 30.0) * clever
            tr["expires"] = tr["slick_until"]
        elif name == "Immolation Trap":
            me.fight.apply_periodic(spell)

    def trap_step(self, d, me, foe, t):
        tr = self.trap
        if tr is None:
            return
        if t >= tr["expires"]:
            self.trap = None
            return
        gap = abs(self.foe_x(d) - tr["x"])
        if not tr["sprung"]:
            if t + EPS >= tr["armed"] and gap <= TRAP_RADIUS:
                self.spring(d, me, foe)
            return
        if t < tr["slick_until"] and gap <= SLICK_RADIUS and t >= foe.immune_until:   # Frost Trap's ice slick
            slow = _num(r"slowed by (\d+)%", tr["spell"].text, 60.0) / 100
            if t >= foe.slow_until or slow >= foe.slow:
                foe.slow = slow
            foe.slow_until = max(foe.slow_until, t + 2 * T.DT)

    def feign(self, d, me, foe, spell):
        self.restore_gcd(me, spell)
        if not self.lands(me, me.mod.tv("Survival Tactics", 0) / 100):
            me.fight.note("Feign Death resisted")
            return 0.0
        self.feigned = d.t
        c = foe.cast_spell()
        if c is not None and c.kind not in ("heal", "buff") and c.target not in ("self", "pet"):
            foe.break_cast("Feign Death")
        me.fight.note("Feign Death")
        return 0.0

    def scatter(self, d, me, foe, spell):
        shot = copy.copy(spell)
        shot.kind = "ranged"
        if me.fight.resolve_attack(shot) > 0:
            foe.apply_cc("incap", _num(r"disorients the target for (\d+) sec", spell.text, 4.0), T.DR_CATEGORY.get("Scatter Shot", "incap"),
                         "Scatter Shot", physical=True)
        return 0.0

    def viper_sting(self, d, me, foe, spell):
        if me.fight.attack_table(spell, False) in ("miss", "dodge", "parry"):
            me.fight.note("Viper Sting MISS")
            return 0.0
        foe.dots = [x for x in foe.dots if x[0] != "Serpent Sting"]   # one sting per hunter
        total = _num(r"draining (\d[\d,]*) mana", spell.text, 1108.0)
        ticks = 4
        self.viper = {"next": d.t + 2.0, "ticks": ticks, "per": total / ticks, "until": d.t + 8.0}
        me.fight.note(f"Viper Sting ({total:.0f} mana over 8s)")
        return 0.0

    def viper_step(self, d, me, foe, t):
        v = self.viper
        if v is None:
            return
        while v["ticks"] > 0 and t + EPS >= v["next"]:
            got = min(foe.p.mana, v["per"]) if foe.p.mana_max > 0 else 0.0
            foe.p.mana -= got
            v["ticks"] -= 1
            v["next"] += 2.0
            me.fight.note(f"Viper Sting drains {got:.0f} mana")
        if v["ticks"] <= 0:
            self.viper = None

    def counter(self, d, me, foe, spell):
        me.p.buffs.pop("Counterattack", None)
        amount = FE.Fight.resolve_spell(me.fight, spell)
        if amount > 0:
            foe.apply_cc("root", _num(r"immobilizes the target for (\d+) sec", spell.text, 5.0), T.DR_CATEGORY.get("Counterattack", "root"),
                         "Counterattack", physical=True)
        return amount

    def wing_clip(self, d, me, foe, spell):
        foe.cc_hint = "Improved Wing Clip"   # the talent's root (the module's on_hit) keeps its own name and category
        return FE.Fight.resolve_spell(me.fight, spell)

    def concussive(self, d, me, foe, spell):
        foe.cc_hint = "Improved Concussive Shot"
        return FE.Fight.resolve_spell(me.fight, spell)

    def intimidation(self, d, me, foe, spell):
        pet = me.p.pet
        if pet is not None and pet.alive:   # as the fight lab's pull: the pet's next landed attack stuns 3 s and is a sure crit
            me.p.buffs["Intimidation"] = {"until": d.t + 15.0}
            pet.crit = me.mod.pet_base_crit + 1.0
            me.fight.note("Intimidation")
        return 0.0

    def wrath(self, d, me, foe, spell):
        self.restore_gcd(me, spell)
        pet = me.p.pet
        if pet is not None and pet.alive and not me.p.buff("Bestial Wrath", d.t):
            pet.dmg_mult *= 1.5
            me.p.buffs["Bestial Wrath"] = {"until": d.t + 18.0}
            me.fight.note("Bestial Wrath")
        return 0.0

    def deterrence(self, d, me, foe, spell):
        self.restore_gcd(me, spell)
        me.mod.on_hit(me.fight, spell, 0.0, False, False)   # the module's buff: +25% dodge and parry for 10 s
        me.fight.note("Deterrence")
        return 0.0

    def strider(self, d, me, foe, spell):
        amount = FE.Fight.resolve_spell(me.fight, spell)
        me.speed_bonus["Strider Kick"] = (_num(r"movement speed by (\d+)%", spell.text, 30.0) / 100, d.t + 3.0)
        return amount

    def flare(self, d, me, foe, spell):
        if foe.stealthed and d.dist <= 40.0:
            foe.stealthed = False
            me.fight.note(f"{spell.name} reveals the opponent")
        return 0.0

    # ------------------------------------------------------------------ every step
    def step(self, d, me, foe):
        t = d.t
        if self.last_step == t:
            return
        self.last_step = t
        if abs(me.fight.last_move - t) < EPS:   # I moved in this step's movement: follow my position
            v = d.velocity(me, t)
            if v == 0.0:   # the state changed after the move (a cast, a control): the run it had
                v = T.RUN_SPEED * (1 - (me.slow if t < me.slow_until else 0.0))
                v = v if (me.intent == "kite" or t < me.fear_until) else -v
            self.x -= v * T.DT
        if self.surefooted > 0:   # movement impairing effects on me are 30% shorter
            if me.slow_until > self.seen_slow + EPS and me.slow_until > t:
                me.slow_until = t + (me.slow_until - t) * (1 - self.surefooted)
            self.seen_slow = me.slow_until
            if me.root_until > self.seen_root + EPS and me.root_until > t:
                me.root_until = t + (me.root_until - t) * (1 - self.surefooted)
            self.seen_root = me.root_until
        me.mod._expire_wrath(me.fight)
        self.trap_step(d, me, foe, t)
        self.viper_step(d, me, foe, t)
        if self.held_by_me(foe, t):   # my own Auto Shot and swings wait for my control to end
            end = foe.incap_until
            me.p.shot_at = max(me.p.shot_at, end)
            me.p.swing_mh = max(me.p.swing_mh, end)
            if me.p.oh is not None:
                me.p.swing_oh = max(me.p.swing_oh, end)

    def pet_held(self, d, me, t):
        foe = me.foe
        if self.held_by_me(foe, t):
            return True
        if me.p.buff("Intimidation", t):   # the stun the pet's next hit brings: its name and category, not the last shot's
            foe.cc_hint = "Intimidation"
        return False

    def while_inactive(self, d, me, foe):
        self.step(d, me, foe)
        return None

    def while_casting(self, d, me, foe):
        self.step(d, me, foe)
        return None

    def while_controlled(self, d, me, foe):
        self.step(d, me, foe)
        return super().while_controlled(d, me, foe)

    # ------------------------------------------------------------------ movement
    def intent(self, d, me, foe):
        t = d.t
        if foe.stealthed:
            return "hold"
        if self.melee_spec:
            return super().intent(d, me, foe)
        dist = d.dist
        if dist < T.MIN_RANGED:
            return "kite"   # out of the dead zone
        if not self.melee_foe(foe):
            return "close" if dist > self.keep_range + 0.5 else "hold"
        stuck = foe.controlled(t) or t < foe.root_until
        if stuck:
            return "kite" if dist < KEEP + 2.0 else "hold"
        if self.slowed(foe, t):   # stutter-step: stand only for the next Auto Shot, else run; never closer than 15 yards
            if dist < 15.0:
                return "kite"
            if me.p.shot_at - t <= FT.AUTO_SHOT_STAND_STILL + 0.1:
                return "hold"
            return "kite" if dist < KEEP else "hold"
        return "hold"   # a free melee at full speed: stand and shoot (Concussive Shot slows it)

    # ------------------------------------------------------------------ off the global cooldown
    def off_gcd(self, d, me, foe):
        self.step(d, me, foe)
        self.gcd_before = me.p.gcd_until
        t = d.t
        c = self.foe_cast(d, foe)
        if c is not None and c.name in CC_CASTS and me.can("Feign Death", ignore_gcd=True):
            return "Feign Death"
        melee_on_me = self.melee_foe(foe) and d.dist <= T.MELEE + 0.5 and not foe.controlled(t)
        if melee_on_me and me.hp_frac() < 0.5 and me.can("Deterrence", ignore_gcd=True) and not me.p.buff("Deterrence", t):
            return "Deterrence"
        pet = me.p.pet
        if pet is not None and pet.alive and pet.engaged and not self.held_by_me(foe, t) and me.can("Bestial Wrath", ignore_gcd=True):
            return "Bestial Wrath"
        if self.melee_spec:
            return self.kited(d, me, foe)
        # a melee on me while I am rooted or slowed, and none of my own answers ready: the trinket
        if melee_on_me or (self.melee_foe(foe) and d.dist <= 8.0 and not foe.controlled(t)):
            frees = me.trinket_frees(t)
            rooted = "root" in frees and me.root_until - t >= 1.5
            slowed = "slow" in frees and me.slow >= 0.4 and me.slow_until - t >= 2.5
            answers = me.can("Scatter Shot", ignore_gcd=True) or self.trap_ready(d, me, "Freezing Trap") \
                or me.can("Intimidation", ignore_gcd=True)
            if (rooted or slowed) and not answers and me.hp_frac() < 0.8:
                return "trinket"
        return None

    # ------------------------------------------------------------------ decisions
    def decide(self, d, me, foe):
        t = d.t
        self.gcd_before = me.p.gcd_until
        if foe.stealthed:
            for name in ("Enchanted Flare", "Flare"):
                if d.dist <= 40.0 and me.can(name):
                    return name
            return None
        c = self.foe_cast(d, foe)
        if c is not None and (c.name in CC_CASTS or c.kind == "heal" or c.name in HEALS):   # a control or a heal: stop the cast
            if d.dist <= self.ranges["Scatter Shot"] and dr_factor(foe, "incap", t) >= 0.5 and me.can("Scatter Shot"):
                return "Scatter Shot"
            if me.can("Intimidation"):
                return "Intimidation"
        if self.melee_spec:
            return self.decide_melee(d, me, foe)
        if self.held_by_me(foe, t):
            return self.while_held(d, me, foe)
        dist = d.dist
        if self.melee_foe(foe) and not foe.controlled(t) and t >= foe.root_until:
            a = self.peel(d, me, foe)
            if a is not None:
                return a
        if dist >= T.MIN_RANGED and self.want_viper(d, me, foe) and me.can("Viper Sting"):
            return "Viper Sting"
        return self.rot(d, me, foe)

    def peel(self, d, me, foe):
        """A free melee coming at me or on me: Counterattack's root, Wing Clip, then a trap at my feet (it springs as the melee
        follows me); Scatter Shot and the pet's Intimidation only when I cannot outrun it (rooted, or no faster than it)."""
        t, dist = d.t, d.dist
        if dist <= T.MELEE + 0.5:
            if me.p.buff("Counterattack", t) and me.can("Counterattack"):
                return "Counterattack"
            if not self.slowed(foe, t, 0.5, 2.0) and me.can("Wing Clip"):
                return "Wing Clip"
        if dist <= 15.0:
            trap = "Freezing Trap" if dr_factor(foe, "incap", t) >= 1.0 else "Frost Trap"
            if self.trap_ready(d, me, trap):
                return trap
            if not TRAPS_IN_COMBAT and d.combat and t - self.feigned > FD_WINDOW and trap in me.mod.spells \
                    and me.p.ready(trap, t) and me.can("Feign Death", ignore_gcd=True):
                return "Feign Death"   # Classic's "FD trap": Feign Death drops combat, the trap follows
        stuck = t < me.root_until or me.speed(t) <= foe.speed(t) + 0.5
        if dist <= 8.0 and stuck:
            dotted = bool(foe.dots)   # my sting's next tick would end a Scatter Shot (it did, 2026-11-14): the pet's stun first
            if not dotted and dr_factor(foe, "incap", t) >= 0.5 and me.can("Scatter Shot"):
                return "Scatter Shot"
            if me.can("Intimidation"):
                return "Intimidation"
            if dotted and dr_factor(foe, "incap", t) >= 0.5 and me.can("Scatter Shot"):
                return "Scatter Shot"
        if dist >= T.MIN_RANGED and not self.slowed(foe, t) and me.can("Concussive Shot"):
            return "Concussive Shot"
        return None

    def while_held(self, d, me, foe):
        """My Freezing Trap or Scatter Shot holds the opponent: nothing that deals damage; Aimed Shot to land as it ends."""
        t = d.t
        left = foe.incap_until - t
        if not me.p.buff("Hunter's Mark", t) and me.can("Hunter's Mark"):
            return "Hunter's Mark"
        if d.dist >= KEEP - 2.0 or not self.melee_foe(foe):
            aimed = me.mod.spells.get("Aimed Shot")
            if aimed is not None and me.can("Aimed Shot") and left <= me.mod.cast_time(aimed) + 0.1:
                return "Aimed Shot"
            if self.want_viper(d, me, foe) and me.can("Viper Sting"):
                return "Viper Sting"   # no damage: the freeze holds
        return None

    def want_viper(self, d, me, foe):
        """Viper Sting in Serpent Sting's place: on a mana user above 30% mana whose pool the drain cuts by VIPER_SHARE or more.
        Validation pass 2 (2026-11-15): against every mana user it had cost the damage casters' duels, which end in 12-21 s with half
        their mana left (no Viper Sting, field builds, 200 duels: the priest 0.5% -> 8%, the mage 71.5% -> 87%, the warlock 1.5% ->
        8%), and it decides the duels against the self-healers with small pools (paladin 41% -> 3% without it, shaman 97.5% -> 92%).
        The drain, 1,108 mana, is 32% of the field paladin's pool, 27% of the shaman's, 31% of the druid's and 19-20% of the priest's,
        mage's and warlock's."""
        sp = me.mod.spells.get("Viper Sting")
        if sp is None or self.viper is not None or foe.cls not in MANA_FOES or foe.p.mana_max <= 0:
            return False
        if foe.mana_frac() < 0.3:
            return False
        if _num(r"draining (\d[\d,]*) mana", sp.text, 1108.0) < VIPER_SHARE * foe.p.mana_max:
            return False
        serpent = next((x for x in foe.dots if x[0] == "Serpent Sting"), None)
        return serpent is None or serpent[2] * serpent[4] <= 3.0

    def rot(self, d, me, foe):
        """The spec's rotation, with this layer's Feign Death; no Aimed or Sniper Shot cast with a free melee closing in, no Serpent Sting
        over my Viper Sting."""
        t = d.t
        veto = me.mod.veto
        saved = dict(veto)
        veto["Feign Death"] = {"off": True}
        if self.melee_foe(foe) and not foe.controlled(t) and t >= foe.root_until \
                and d.dist < (12.0 if self.slowed(foe, t) else 22.0):
            veto["Aimed Shot"] = {"off": True}
            veto["Sniper Shot"] = {"off": True}
        if self.viper is not None:
            veto["Serpent Sting"] = {"off": True}
        try:
            return self.rotation(d, me, foe)
        finally:
            veto.clear()
            veto.update(saved)

    def decide_melee(self, d, me, foe):
        """The Survival build plays the fight lab's melee hunter: close in, Wing Clip to keep the opponent slowed, Concussive Shot on one
        that runs; the rotation does the rest (Raptor Strike, Counterattack, Mongoose Bite, Strider Kick, Lacerate, Immolation Trap,
        Deterrence)."""
        t, dist = d.t, d.dist
        free = not foe.controlled(t)
        if dist > T.MELEE + 0.5:
            if dist >= T.MIN_RANGED and free and not self.slowed(foe, t) and me.can("Concussive Shot"):
                return "Concussive Shot"
            return self.rot(d, me, foe)
        if free and not self.slowed(foe, t, 0.5, 2.0) and me.can("Wing Clip"):
            return "Wing Clip"
        return self.rot(d, me, foe)
