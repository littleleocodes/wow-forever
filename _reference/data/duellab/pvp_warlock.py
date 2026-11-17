"""Warlock PvP layer (duellab, 2026-11-14): the demon chosen for the opponent, Fear, Death Coil and Howl of Terror to keep a melee
off, the curse that fits the opponent, one Healthstone, Shadow Ward against shadow damage, the PvP trinket against fear, charm and
Polymorph. Damage (Corruption, Bane of Agony, Siphon Life, Drain Life, Life Tap, Shadow Bolt, Immolate, Conflagrate, Shadowburn) is the
spec's own leveling rotation underneath; Soul Link's 30% split and Molten Skin are the fight lab's own (warlock.split_damage_taken).

The demon (the fight lab gives every level-60 build a Voidwalker, the leveling tank; nobody duels with one): a Felhunter against the
classes that win by casting (mage, priest, warlock, shaman, druid, paladin), a Succubus against weapon users (warrior, rogue, hunter).
That is Classic's standard duel choice (Spell Lock and Devour Magic against casters, Seduction against melee), and the Forever Open's
winners (the level-30 beta duel tournament, 2026-10-17/18) were warlocks whose Soul Link and Seduction were called decisive. Soul Link
builds keep their demon all duel (Demonic Sacrifice is never used; the destruction build has neither talent). Demon stats: the official
simulator's level-60 models (wowsims/forever sim/warlock/pets.go at ff9babba5, 2026-11-11: Succubus health 0.699 and armor 0.630 of the
level-60 creature values, attack power 186, a 2.0 s swing of 0.698 of the creature melee dps +-21.5%; Felhunter health 9.5 per point of
its 234 Stamina, no armor of its own, attack power 2 per Strength, a 70-97 swing at 0.8 damage), plus what a demon takes from the
warlock as in the fight lab's make_pet (2 health per Stamina, 35% of the armor, 17% of the spell damage as attack power, 10% as spell
damage, the spell crit), Fel Vitality, Unholy Power and Soul Link's +3%.

Effects the fight lab does not parse, handled here: Curse of Exhaustion (30% slow 12 s, +20 points under Amplify Curse), Curse of
Tongues (+60% cast time on the opponent for 30 s: the opponent's module's cast_time is wrapped for the duel), Howl of Terror (a fear
only within 10 yards when it lands), Shadow Ward (absorbs shadow damage only), the Healthstone (one per duel, an item: no global
cooldown, healing taken reduced by Mortal Strike). The demon acts on its own timer, also while the warlock casts or is controlled:
- Felhunter: Spell Lock (the cast countered, its school locked 8 s, a 3 s silence; 30 s cooldown, the demon's mana) on heals, control
  casts, channels and casts of 2 s or more; Devour Magic (8 s cooldown) on the warlock's Polymorph, Seduction, Repentance, Freezing
  Trap or a magic fear (not a warrior's shout), else on the opponent's absorb shield; the felhunter heals 618 when it devours.
- Succubus: Seduction (the demon's 1.5 s cast; up to 15 s, capped at 10 in PvP; any damage breaks it; diminishing returns with Fear;
  the trinket mechanic is a charm) to stop a heal or a long cast, or to peel a melee within 8 yards when Death Coil and Fear cannot;
  onto the warlock's ticking dots only below 40% health (the next tick ends it). Lash of Pain on cooldown. While a Seduction is on its
  way the warlock uses only damage done before it lands; while it holds, Life Tap, curses and wards until its last 3.5 s, then the
  rotation's spells whose first damage lands as it ends (instant dots, a Shadow Bolt), and it walks away from a melee.
The demon holds its swings while the opponent is under the warlock's fear or Seduction (damage would break them).
Fear and Death Coil are this layer's decisions (vetoed inside the rotation, which would cast them on every approach): Death Coil on a
free melee within 8 yards, as a heal below 40% health, and against a control or heal cast once Spell Lock is down; Fear on a free melee
within 20 yards or a held one (inside Death Coil's horror) when the opponent cannot answer the cast (Pummel, Shield Bash, Kick,
Counterspell, Earth Shock or Silence ready and in reach), on a caster in the same case; Howl of Terror in melee reach. Berserker Rage
and Feign Death are baited: out of melee reach, above half health and with the fear category at full or half duration, the Fear goes
out and the opponent spends its cooldown (it uses them only on a seen fear). Diminishing returns are read before a cast (no fear into
the quarter step or immunity). The curse: Exhaustion on a melee, Tongues on a caster, the rotation's Curse of the Elements on a hunter.

Not modelled: the opponent cannot attack, slow, control or dispel the demon (the engine never targets pets), so the demon never dies
except through Soul Link; a dead demon is not re-summoned (Fel Domination unused); Drain Mana, Banish, Curse of Weakness and
Recklessness, Soothing Kiss, Lesser Invisibility, Tainted Blood and Paranoia; Spell Lock and Seduction cannot be interrupted; Death
Coil's horror moves like a fear but is no fear (Berserker Rage and Fear Ward do not stop it: dtables.HORROR, from the client's
mechanics; 2026-11-14); Shadow Ward absorbs after Soul Link's split; Bane of Havoc does nothing one against one; Seduction works on every opponent but a druid in an animal form.
"""
import re

import dtables as T
import engine as FE
import tables as FT
import warlock as FW
from pvp_base import PvPAI, HEALS

EPS = 1e-9

# --- the demon ---------------------------------------------------------------------------------------------------------------
DEMON_FOR = {"warrior": "Succubus", "rogue": "Succubus", "hunter": "Succubus"}   # every other class: the Felhunter
CREATURE_HP, CREATURE_ARMOR, CREATURE_DPS = 4365.0, 3566.0, 60.45291519165039   # wowsims/forever core/base_stats_auto_gen.go, level 60
_SAYAAD = 0.698 * CREATURE_DPS * 2.0
DEMONS = {   # wowsims/forever sim/warlock/pets.go (ff9babba5): base health, own armor, attack power, swing range, damage multiplier, mana
    "Succubus": dict(hp=0.699 * CREATURE_HP, armor=0.630 * CREATURE_ARMOR, ap=186.0, dmg=(_SAYAAD * 0.785, _SAYAAD * 1.215), mult=1.0,
                     mana=1066.0 + 70 * 11.5),
    "Felhunter": dict(hp=234 * 9.5, armor=0.0, ap=129 * 2.0, dmg=(70.0, 97.0), mult=0.8, mana=1066.0 + 70 * 11.55),
}
DEMON_BASE_MANA = 1066.0                      # Seduction costs 24% of it
DEMON_MANA_REGEN = (15 + 150 / 5) / 2.0       # per second: the fight lab's demon formula (warlock.make_pet) at the demon's 150 Spirit
ANIMAL_FORMS = ("cat", "bear", "moonkin", "travel", "aquatic")   # Seduction "only works against Humanoids"

# --- what answers a cast -----------------------------------------------------------------------------------------------------
# an opponent ability that would stop a Fear, Howl or Seduction cast if it is ready (name -> reach in yards). Berserker Rage gives
# immunity to fear (the warrior layer casts it on a seen Fear); Feign Death cancels the cast (the hunter layer)
ANSWERS = {"Pummel": 5.5, "Shield Bash": 5.5, "Kick": 5.5, "Counterspell": 30.0, "Earth Shock": 20.0, "Silence": 30.0,
           "Feign Death": 100.0, "Berserker Rage": 100.0}
BAITED = {"Berserker Rage", "Feign Death"}   # answers worth drawing out with a Fear (a cooldown spent, nothing of mine locked)
CC_CASTS = {"Polymorph", "Fear", "Howl of Terror", "Seduction", "Hibernate", "Mind Control", "Entangling Roots", "Scare Beast"}
SHADOW_FOES = {"warlock", "priest"}           # Shadow Ward is worth a global cooldown against these
MAGIC_INCAP = {"Polymorph", "Seduction", "Repentance", "Freezing Trap"}   # what Devour Magic removes (duel.Side.dispel_cc)
MY_CURSES = ("Curse of Exhaustion", "Curse of Tongues", "Curse of the Elements", "Curse of Weakness", "Curse of Recklessness")

PEEL = 8.0           # a free melee this close is "on me"
DIRTY_SEDUCE_BELOW = 0.40   # a Seduction onto my ticking dots only below this share of health (it lasts until the next tick)
STONE_AT = 0.35      # the Healthstone below this share of health (the fight lab's rotation uses the same)
COIL_HEAL_AT = 0.40  # Death Coil as a heal below this share
TONGUES = 0.60       # Curse of Tongues: +60% casting time (its tooltip)


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


class WarlockPvP(PvPAI):
    keep_range = 25.0
    auto_attack = False
    ranges = {"Howl of Terror": 10.0}

    def bind(self, d, me):
        super().bind(d, me)
        self.last_step = -1.0
        self.gcd_before = 0.0
        self.pet_cast = None          # ("Seduction", end time) while the Succubus casts
        self.ward = None             # [absorb left, until]: Shadow Ward
        self.cc_since = None          # when the current control on me began (the felhunter's reaction)
        self.md_shadow = self.md_magic = 0.0
        self.coex_slow = 0.30
        self.fear_target = None       # round 2: "pet" when the next Fear goes to a hunter's pet
        self.pet_fear_until = 0.0
        self.player_fear_until = 0.0
        self.fel_dom = False          # Fel Domination's next summon
        self.resummons = 0
        self.demon_name = None

    def effects_for(self, me):
        fx = {"Curse of Exhaustion": self.exhaustion, "Curse of Tongues": self.tongues, "Howl of Terror": self.howl,
              "Shadow Ward": self.shadow_ward, "Create Healthstone": self.healthstone}
        # round 2 (2026-11-17): a hunter's pet feared, a warlock's demon banished, my own demon summoned again (Fel Domination)
        if me.foe.cls == "warlock":
            fx["Banish"] = self.banish
        if me.p.pet is not None:
            fx["Fel Domination"] = self.fel_domination
            fx.update({f"Summon {n}": self.summon for n in ("Felhunter", "Succubus", "Imp", "Voidwalker")})
        return fx

    def fear(self, d, me, foe, spell):
        """Fear against a hunter: on its pet when this layer chose the pet (fear_target), else the fight lab's own Fear on the hunter;
        one target feared at a time. NOT USED (2026-11-17): fearing a hunter's pet cost the warlock 6-9 points against hunters (the
        Demonology winner 90% -> 84%, the field warlock against the Marksmanship winner 39% -> 0%); the Fear stays on the hunter."""
        t = d.t
        if self.fear_target == "pet":
            self.fear_target = None
            import pvp_druid as PD
            if t < self.player_fear_until:
                foe.fear_until = min(foe.fear_until, t)   # my fear on the hunter ends
                self.player_fear_until = t
            if not PD.pet_open(d, foe) or not PD.spell_lands(me, spell):
                me.fight.note("Fear: MISS or no pet")
                return 0.0
            self.pet_fear_until = t + d.pet_cc(foe, "fear", T.PVP_CC_CAP)
            return 0.0
        if t < self.pet_fear_until:
            foe.pet_body.fear_until = min(foe.pet_body.fear_until, t)   # the pet's fear ends
            self.pet_fear_until = t
        amount = me.fight._splashing(FE.Fight.resolve_spell, me.fight, spell)
        me.fight.casts[spell.name] = me.fight.casts.get(spell.name, 1) - 1   # counted once already (SideFight.resolve_spell)
        if foe.fear_until > t:
            self.player_fear_until = foe.fear_until
        return amount

    def banish(self, d, me, foe, spell):
        """Banish on the other warlock's demon (round 2): it does nothing and takes nothing for up to 30 s (the engine's PvP cap)."""
        import pvp_druid as PD
        if not PD.pet_open(d, foe, ("warlock",)) or not PD.spell_lands(me, spell):
            me.fight.note("Banish: MISS or no demon")
            return 0.0
        d.pet_cc(foe, "incap", T.PVP_CC_CAP, banish=True)
        return 0.0

    def fel_domination(self, d, me, foe, spell):
        """"Your next ... Summon spell has its casting time reduced by 5.5 sec and its Mana cost reduced by 50%" (round 2)."""
        self.fel_dom = True
        return 0.0

    def summon(self, d, me, foe, spell):
        """My demon again (round 2: until then a dead demon stayed dead), the one this foe calls for (DEMON_FOR), full health."""
        name = spell.name.replace("Summon ", "")
        me.p.pet = self.make_demon(me, name)
        self.pet_arrives = d.t + d.dist / 14.0   # it runs to the foe as at the start
        self.fel_dom = False
        self.resummons += 1
        me.fight.note(f"{name} summoned again ({me.p.pet.hp_max:.0f} health)")
        return 0.0

    def summon_cost(self, me, base):
        """Fel Domination's -50% and Master Summoner's -20% a rank of a summon's mana cost."""
        return base * (0.5 if self.fel_dom else 1.0) * (1.0 - 0.2 * me.mod.rank("Master Summoner"))

    def dead_demon(self, me):
        pet = me.p.pet
        return self.demon_name is not None and (pet is None or not pet.alive)

    # ------------------------------------------------------------------ set-up
    def prefight(self, d, me, foe):
        if me.p.pet is not None:
            me.p.pet = self.make_demon(me, DEMON_FOR.get(foe.cls, "Felhunter"))
            me.fight.note(f"{me.p.pet.name} out ({me.p.pet.hp_max:.0f} health)")
            self.demon_name = me.p.pet.name
            # round 2: a summon's cast with Fel Domination (-5.5 s) and Master Summoner (-2 s a rank), and its mana
            base_ct, base_cost = me.mod.cast_time, me.mod.mana_cost

            def cast_time(s, _base=base_ct, _me=me, _ai=self):
                if s.name.startswith("Summon "):
                    return max(0.5, 10.0 - (5.5 if _ai.fel_dom else 0.0) - 2.0 * _me.mod.rank("Master Summoner"))
                return _base(s)

            def mana_cost(s, _base=base_cost, _me=me, _ai=self):
                c = _base(s)
                return _ai.summon_cost(_me, c) if s.name.startswith("Summon ") else c
            me.mod.cast_time, me.mod.mana_cost = cast_time, mana_cost
        if me.mod.rank("Master Demonologist") and me.p.pet is not None:   # the tooltip's numbers by demon: Imp, Voidwalker, Succubus, Felhunter
            if me.p.pet.name == "Succubus":
                self.md_shadow = me.mod.tv("Master Demonologist", 2) / 100
                base = me.mod.damage_multiplier

                def damage_multiplier(spell, frozen, _base=base, _me=me, _ai=self):   # +10% Shadow damage while the Succubus lives
                    m = _base(spell, frozen)
                    pet = _me.p.pet
                    if spell.school == "shadow" and pet is not None and pet.alive:
                        m *= 1 + _ai.md_shadow
                    return m
                me.mod.damage_multiplier = damage_multiplier
            elif me.p.pet.name == "Felhunter":
                self.md_magic = me.mod.tv("Master Demonologist", 3) / 100
        s = me.mod.spells.get("Curse of Exhaustion")
        self.coex_slow = _num(r"speed by (\d+)%", getattr(s, "text", ""), 30.0) / 100

    def make_demon(self, me, name):
        """The PvP demon at level 60 (DEMONS) with what it takes from the warlock (the fight lab's make_pet rules)."""
        mod, p, cfg = me.mod, me.p, DEMONS[name]
        base, g = FT.class_base_stats("warlock", 60), FT.gear_stats(60, mod.gear, "warlock")
        stamina = (base["stamina"] + g["stamina"]) * (1 + mod.tv("Demonic Embrace", 0) / 100)
        k, vit = FT.PET_SCALING, 1 + mod.tv("Fel Vitality", 0) / 100
        hp = (cfg["hp"] + k * FW.DEMON_HP_PER_STAMINA * stamina) * vit
        pet = FE.Pet(name=name, hp_max=hp, hp=hp, armor=cfg["armor"] + k * 0.35 * p.armor, dmg_min=cfg["dmg"][0], dmg_max=cfg["dmg"][1],
                     speed=2.0, attack_power=cfg["ap"] + k * 0.17 * p.spell_power, crit=k * p.spell_crit, focus=0.0, focus_max=0.0,
                     focus_regen=0.0, mana=cfg["mana"] * vit, mana_max=cfg["mana"] * vit, mana_regen=DEMON_MANA_REGEN, threat_mult=1.0)
        pet.dmg_mult = cfg["mult"] * (1 + mod.tv("Unholy Power", 0) / 100) * (1.03 if mod.rank("Soul Link") else 1.0)
        pet.spell_power = k * 0.10 * p.spell_power
        pet.hit_bonus = k * mod.hit_bonus(None) * 8 / 17   # the warlock's spell hit, 8/17 of it as melee hit (the simulator's rule)
        return pet

    # ------------------------------------------------------------------ effects
    def lands(self, me, spell=None, bonus=0.0):
        """A spell hit roll against a same-level player (the fight lab's rule: 4% miss, less the hit bonuses)."""
        hit = 1.0 - FT.spell_miss(0) + me.mod.hit_bonus(spell) + me.p.spell_hit + bonus
        return me.fight.rng.random() <= min(FT.SPELL_HIT_CAP, hit)

    def set_curse(self, foe, name, until):
        for c in MY_CURSES:
            if c != name:
                foe.debuffs.pop(c, None)
        foe.debuffs[name] = {"until": until, "stacks": 1}

    def exhaustion(self, d, me, foe, spell):
        t = d.t
        if not self.lands(me, spell):
            me.fight.note("Curse of Exhaustion MISS")
            return 0.0
        slow = self.coex_slow
        if me.p.buff("Amplify Curse", t):   # "your next Curse of Exhaustion by 20%": 30% -> 50%
            slow += 0.20
            del me.p.buffs["Amplify Curse"]
        self.set_curse(foe, "Curse of Exhaustion", t + 12.0)
        if t >= foe.slow_until or slow >= foe.slow:
            foe.slow = slow
        foe.slow_until = max(foe.slow_until, t + 12.0)
        me.fight.note(f"Curse of Exhaustion: {slow:.0%} slow 12s")
        return 0.0

    def tongues(self, d, me, foe, spell):
        t = d.t
        if not self.lands(me, spell):
            me.fight.note("Curse of Tongues MISS")
            return 0.0
        self.set_curse(foe, "Curse of Tongues", t + 30.0)
        if not getattr(foe.mod, "_tongues", False):   # the opponent's casts take 60% longer while the curse holds
            base = foe.mod.cast_time

            def cast_time(s, _base=base, _foe=foe):
                c = _base(s)
                cur = _foe.debuffs.get("Curse of Tongues")
                return c * (1 + TONGUES) if c > 0 and cur and cur.get("until", 0) > _foe.t else c
            foe.mod.cast_time = cast_time
            foe.mod._tongues = True
        me.fight.note("Curse of Tongues: casts +60% for 30s")
        return 0.0

    def howl(self, d, me, foe, spell):
        if d.dist > self.ranges["Howl of Terror"] + 0.5:
            me.fight.note("Howl of Terror: out of reach")
            return 0.0
        if not self.lands(me, spell):
            me.fight.note("Howl of Terror MISS")
            return 0.0
        foe.apply_cc("fear", spell.fear or 15.0, T.DR_CATEGORY.get("Howl of Terror", "fear"), "Howl of Terror")
        return 0.0

    def shadow_ward(self, d, me, foe, spell):
        self.ward = [spell.absorb or _num(r"Absorbs (\d[\d,]*)", spell.text, 920.0), d.t + 30.0]
        me.fight.note(f"Shadow Ward ({self.ward[0]:.0f} shadow)")
        return 0.0

    def healthstone(self, d, me, foe, spell):
        got = me.fight.heal(spell, spell.heal_max or 1440.0)
        me.fight.note(f"Healthstone +{got:.0f}")
        me.mod.spells.pop("Create Healthstone", None)   # one per duel
        me.p.gcd_until = self.gcd_before                # an item: no global cooldown
        return 0.0

    # ------------------------------------------------------------------ incoming damage
    def damage_taken(self, d, me, src, spell, amount):
        school = getattr(spell, "school", None) or "physical"
        pet = me.p.pet
        if self.md_magic and school != "physical" and pet is not None and pet.alive:   # Master Demonologist with the Felhunter
            amount *= 1 - self.md_magic
        w = self.ward
        if w is not None and amount > 0 and school == "shadow" and d.t < w[1] and w[0] > 0:
            a = min(w[0], amount)
            w[0] -= a
            amount -= a
            me.fight.note(f"Shadow Ward absorbs {a:.0f}")
        return amount

    # ------------------------------------------------------------------ the opponent's state
    def seduced(self, foe, t):
        return t < foe.incap_until and foe.incap_name == "Seduction" and foe.incap_breaks

    def my_breakable(self, foe, t):
        """The opponent is under my fear, horror or Seduction (damage would end it)."""
        return t < foe.fear_until or self.seduced(foe, t)

    def fear_ok(self, d, foe):
        t = d.t
        return t >= foe.fear_immune_until and not foe.immune(t) and dr_factor(foe, "fear", t) >= 0.5

    def answers(self, d, foe, lands_in=1.5, me=None):
        """Whether the opponent could stop a fear cast landing in `lands_in` seconds: an answer ready and in reach, the opponent free
        before the cast ends. Berserker Rage and Feign Death are baited (they cost the opponent a cooldown and lock nothing of mine)
        when the opponent is out of melee reach, my health is at half or more and the fear category is fresh: the next Fear sticks."""
        t = d.t
        if t + lands_in <= max(foe.stun_until, foe.incap_until, foe.fear_until, foe.silence_until) + T.DT + EPS:
            return False   # still held when it lands (a cast ending in the step the control ends lands before the foe acts)
        bait = me is not None and d.dist > T.MELEE + 1.0 and me.hp_frac() >= 0.5 and dr_factor(foe, "fear", t) >= 0.5
        for name, reach in ANSWERS.items():
            if bait and name in BAITED:
                continue
            s = foe.mod.spells.get(name)
            if s is not None and foe.p.ready(name, t) and d.dist <= reach:
                if name in ("Pummel", "Shield Bash") and foe.p.rage < (s.cost or 10.0):
                    continue
                if name == "Kick" and foe.p.energy < (s.cost or 25.0):
                    continue
                return True
        return False

    def humanoid(self, foe):
        form = str(getattr(foe.p, "form", "") or "").lower()
        return not any(k in form for k in ANIMAL_FORMS)

    def curse_for(self, foe):
        if foe.cls == "hunter" and foe.ai.keep_range > 0:
            return None                      # the rotation's Curse of the Elements
        if self.melee_foe(foe):
            return "Curse of Exhaustion"
        return "Curse of Tongues"

    def curse_up(self, foe, name, t, margin=0.0):
        c = foe.debuffs.get(name)
        return bool(c and c.get("until", 0) > t + margin)

    # ------------------------------------------------------------------ the demon
    def step(self, d, me, foe):
        """Once per duel step, whatever the warlock is doing: the demon's own actions."""
        t = d.t
        if self.last_step == t:
            return
        self.last_step = t
        if me.controlled(t):
            if self.cc_since is None:
                self.cc_since = t
        else:
            self.cc_since = None
        pet = me.p.pet
        if pet is None or not pet.alive or not pet.engaged or foe.stealthed:
            self.pet_cast = None
            return
        if self.pet_cast is not None:
            name, end = self.pet_cast
            if t + EPS >= end:
                self.pet_cast = None
                self.seduction_lands(d, me, foe)
            return
        if pet.name == "Felhunter":
            self.felhunter(d, me, foe, pet, t)
        elif pet.name == "Succubus":
            self.succubus(d, me, foe, pet, t)

    def devourable(self, me, foe, t):
        """The magic control on me Devour Magic would remove first ("polymorph" covers Polymorph, Seduction, Repentance, Freezing Trap)."""
        if t < me.incap_until and me.incap_name in MAGIC_INCAP:
            return "polymorph"
        if t < me.fear_until and foe.cls != "warrior":   # Intimidating Shout is no magic
            return "fear"
        return None

    def devour_ready(self, pet, t, s):
        return s is not None and pet.cooldowns.get(s.name, -1.0) <= t and pet.mana >= s.cost

    def felhunter(self, d, me, foe, pet, t):
        dev = me.mod.spells.get("Devour Magic")
        if self.devour_ready(pet, t, dev):
            kind = self.devourable(me, foe, t)
            removed = None
            if kind and self.cc_since is not None and t - self.cc_since >= T.REACTION:
                removed = me.dispel_cc(kinds=(kind,)) and kind
            elif foe.p.absorb > 0 and t < foe.p.absorb_until:   # the opponent's Ice Barrier or Power Word: Shield
                removed = foe.purge_shields() and "shield"
            if removed:
                heal = _num(r"healed for (\d[\d,]*)", dev.text, 618.0) * (1 + me.mod.tv("Improved Felhunter", 0) / 100)
                pet.hp = min(pet.hp_max, pet.hp + heal)
                pet.mana -= dev.cost
                pet.cooldowns[dev.name] = t + dev.cooldown
                me.fight.note(f"Felhunter: Devour Magic ({removed})")
                return
        lock = me.mod.spells.get("Spell Lock")
        if lock is None or pet.cooldowns.get(lock.name, -1.0) > t or pet.mana < lock.cost or foe.silenced(t):
            return
        c = self.foe_cast(d, foe)
        if c is None or not (c.kind in ("heal", "channel") or c.name in HEALS or c.name in CC_CASTS or c.cast >= 2.0):
            return
        foe.interrupt(lock.interrupt or 8.0, "Spell Lock")
        foe.apply_cc("silence", _num(r"Silences the enemy for (\d+) sec", lock.text, 3.0), T.DR_CATEGORY.get("Spell Lock"), "Spell Lock")
        pet.mana -= lock.cost
        pet.cooldowns[lock.name] = t + max(0.0, lock.cooldown - me.mod.tv("Improved Felhunter", 1))
        me.fight.note(f"Felhunter: Spell Lock on {c.name}")

    def succubus(self, d, me, foe, pet, t):
        sed = me.mod.spells.get("Seduction")
        cost = (sed.cost / 100 * DEMON_BASE_MANA) if (sed is not None and "cost_pct" in sed.tags) else (sed.cost if sed else 0.0)
        if sed is not None and pet.mana >= cost and self.want_seduction(d, me, foe, t):
            pet.mana -= cost
            self.pet_cast = ("Seduction", t + (sed.cast or 1.5))
            me.fight.note("Succubus casts Seduction")
            return
        lash = me.mod.spells.get("Lash of Pain")
        if lash is not None and pet.cooldowns.get(lash.name, -1.0) <= t and pet.mana >= lash.cost + cost and not self.my_breakable(foe, t) \
                and not foe.immune(t):
            pet.mana -= lash.cost
            pet.cooldowns[lash.name] = t + lash.cooldown
            if not self.lands(me):
                me.fight.note("Lash of Pain MISS")
                return
            dmg = (_num(r"causing (\d+) Shadow damage", lash.text, 50.0) + lash.coef * pet.spell_power) * pet.dmg_mult \
                * (1 + me.mod.tv("Improved Sayaad", 0) / 100)
            crit = me.fight.rng.random() < pet.crit
            me.fight.deal(FE.Spell("Lash of Pain", "shadow"), dmg * (1.5 if crit else 1.0), crit, source="pet")

    def want_seduction(self, d, me, foe, t):
        if foe.immune(t) or foe.controlled(t) or foe.stealthed or not self.humanoid(foe) or d.dist > 30.0:
            return False
        own = me.cast_spell()
        if own is not None and own.name in ("Fear", "Howl of Terror"):
            return False   # the warlock's own fear is on its way (one diminishing-returns category)
        if dr_factor(foe, "fear", t) < 0.5:
            return False
        c = self.foe_cast(d, foe)
        if c is not None and (c.kind == "heal" or c.name in HEALS or c.name in CC_CASTS or c.cast >= 2.0) and foe.fight.casting \
                and foe.cast_end() - t > 1.6:
            return True   # lands before the cast ends
        if self.melee_foe(foe) and d.dist <= PEEL:
            if foe.dots and me.hp_frac() >= DIRTY_SEDUCE_BELOW:
                return False   # my dots would break it at their next tick: not worth the diminishing returns it shares with Fear
            if me.can("Death Coil", ignore_gcd=True) and not me.controlled(t):
                return False   # the warlock's Death Coil first
            if self.fear_ok(d, foe) and not self.answers(d, foe, me=me) and me.can("Fear", ignore_gcd=True) and foe.dots:
                return False   # then its Fear (a clean Seduction comes first: no dot breaks it)
            return True
        return False

    def seduction_lands(self, d, me, foe):
        if d.dist > 30.0 or not self.humanoid(foe):
            return
        if not self.lands(me):
            me.fight.note("Seduction MISS")
            return
        dur = _num(r"for up to (\d+) sec", me.mod.spells["Seduction"].text, 15.0) * (1 + me.mod.tv("Improved Sayaad", 1) / 100)
        foe.apply_cc("incap", dur, T.DR_CATEGORY.get("Seduction", "fear"), "Seduction")

    def pet_held(self, d, me, t):
        return self.pet_cast is not None or self.my_breakable(me.foe, t)

    # ------------------------------------------------------------------ decisions
    def while_inactive(self, d, me, foe):
        self.step(d, me, foe)
        return None

    def while_casting(self, d, me, foe):
        self.step(d, me, foe)
        return None

    def while_controlled(self, d, me, foe):
        self.step(d, me, foe)
        t = d.t
        pet = me.p.pet
        dev = me.mod.spells.get("Devour Magic")
        if pet is not None and pet.alive and pet.engaged and pet.name == "Felhunter" and self.devourable(me, foe, t) \
                and self.devour_ready(pet, t + T.REACTION + 0.1, dev):
            return None   # the felhunter devours it: keep the trinket
        return super().while_controlled(d, me, foe)

    def off_gcd(self, d, me, foe):
        self.step(d, me, foe)
        self.gcd_before = me.p.gcd_until
        if me.hp_frac() < STONE_AT and me.can("Create Healthstone", ignore_gcd=True):
            return "Create Healthstone"
        if self.dead_demon(me) and not self.fel_dom and me.mod.rank("Fel Domination") and me.can("Fel Domination", ignore_gcd=True):
            return "Fel Domination"   # round 2: the demon died; the next summon comes fast
        return None

    def intent(self, d, me, foe):
        t = d.t
        if foe.stealthed:
            return "hold"
        if self.melee_foe(foe):
            held = t < foe.stun_until or t < foe.incap_until or t < foe.root_until
            if held and d.dist < 30.0:
                return "kite"
            if t < foe.fear_until:
                return "hold"   # it runs off on its own: stand and cast
            if d.dist <= PEEL:
                return "kite"   # instants on the move
            return "hold" if d.dist <= self.keep_range else "close"
        return "close" if d.dist > self.close_to(d, me) + 0.5 else "hold"

    def close_to(self, d, me):
        return self.keep_range if self.melee_foe(me.foe) else 19.0   # inside the 20 yards of Fear and Drain Life

    def decide(self, d, me, foe):
        t = d.t
        self.gcd_before = me.p.gcd_until
        if foe.stealthed:
            return None
        hp = me.hp_frac()
        melee = self.melee_foe(foe)
        dist = d.dist
        free = not foe.controlled(t) and not foe.immune(t)
        seducing = self.pet_cast is not None   # the Succubus's Seduction is on its way: no Fear on top (one category)
        # round 2 (2026-11-17): my demon dead and Fel Domination's fast summon ready
        if self.dead_demon(me) and self.fel_dom and me.can(f"Summon {self.demon_name}"):
            return f"Summon {self.demon_name}"
        # round 2: the other warlock's demon on me: Banish it
        if foe.cls == "warlock" and "Banish" in me.mod.spells:
            import pvp_druid as PD
            if PD.pet_open(d, foe, ("warlock",)) and PD.can_at_pet(me, self, "Banish"):
                return "Banish"
        # a free melee on me: Death Coil, then Fear or Howl of Terror when the cast cannot be answered
        if melee and free and dist <= PEEL:
            if me.can("Death Coil"):
                return "Death Coil"
            if self.fear_ok(d, foe) and not self.answers(d, foe, me=me) and not seducing:
                if me.can("Fear"):
                    return "Fear"
                if dist <= self.ranges["Howl of Terror"] and me.can("Howl of Terror"):
                    return "Howl of Terror"
        # a free melee on its way in: Fear it before it arrives (a Berserker Rage drawn out now is not there for the next one)
        if melee and free and PEEL < dist <= 20.0 and not seducing and self.fear_ok(d, foe) and not self.answers(d, foe, me=me) \
                and me.can("Fear"):
            return "Fear"
        # a melee held by a short control in reach (Death Coil's horror, a stun): Fear lands before it can answer
        if melee and not free and not self.seduced(foe, t) and not seducing and dist <= 20.0 and self.fear_ok(d, foe) and me.can("Fear"):
            left = max(foe.stun_until, foe.fear_until, foe.incap_until) - t
            if 0.9 <= left <= 4.0 and not self.answers(d, foe, lands_in=me.mod.cast_time(me.mod.spells["Fear"]), me=me):
                return "Fear"
        clean = self.seduced(foe, t)   # any Seduction of mine: no direct damage until its last 3.5 s (my dots may end it sooner)
        if hp < COIL_HEAL_AT and me.can("Death Coil") and not clean:
            return "Death Coil"
        c = self.foe_cast(d, foe)
        lock = me.mod.spells.get("Spell Lock")
        pet = me.p.pet
        lock_ready = lock is not None and pet is not None and pet.alive and pet.name == "Felhunter" and pet.cooldowns.get(lock.name, -1.0) <= t
        if c is not None and (c.name in CC_CASTS or c.kind == "heal") and not lock_ready and me.can("Death Coil"):
            return "Death Coil"
        # a caster whose answers are down: Fear opens a window for the dots
        if not melee and free and not seducing and dist <= 20.0 and self.fear_ok(d, foe) and not self.answers(d, foe, me=me) and me.can("Fear"):
            return "Fear"
        # my Seduction on its way: only damage that is done before it lands (no dot, channel or cast still running then)
        if seducing:
            a = self.rot(d, me, foe)
            s = me.mod.spells.get(a) if isinstance(a, str) else a
            if a == "wand" or (s is not None and self.last_hit_in(me, s) >= self.pet_cast[1] - t):
                return self.setup(d, me, foe)
            return a
        # my Seduction holds: set-up only, then the rotation's spells whose first damage lands as it ends
        if clean:
            left = foe.incap_until - t
            if left > 3.5:
                return self.setup(d, me, foe)
            a = self.rot(d, me, foe)
            s = me.mod.spells.get(a) if isinstance(a, str) else a
            first = 0.5 if a == "wand" else (self.first_hit_in(me, s) if s is not None else 1e9)
            if first < left - 0.15:
                return self.setup(d, me, foe)
            return a
        curse = self.curse_for(foe)
        if curse and not self.curse_up(foe, curse, t, 1.0) and me.can(curse):
            return curse
        if foe.cls in SHADOW_FOES and me.can("Shadow Ward") and (self.ward is None or t >= self.ward[1] or self.ward[0] <= 0):
            return "Shadow Ward"
        return self.rot(d, me, foe)

    def last_hit_in(self, me, s):
        """Seconds until a spell's last damage (a dot's or channel's last tick); the cast time for a direct hit or no damage."""
        if s.kind in ("buff", "heal"):
            return 0.0
        cast = me.mod.cast_time(s)
        if s.kind == "channel" or s.dot > 0:
            return cast + (s.channel or s.dot_dur or 3.0)
        return cast

    def first_hit_in(self, me, s):
        """Seconds until a spell's first damage: the cast, then a channel's first tick or a dot's first tick when it has no direct hit."""
        if s.kind in ("buff", "heal"):
            return 1e9
        cast = me.mod.cast_time(s)
        if s.kind == "channel":
            return s.channel / max(1, s.dot_ticks)
        if s.dmg_max > 0 or s.kind in ("melee", "ranged"):
            return cast
        if s.dot > 0:
            return cast + (s.dot_dur / max(1, s.dot_ticks) if s.dot_dur else 3.0)
        return 1e9

    def setup(self, d, me, foe):
        """While my Seduction is on its way or holds: nothing that deals damage."""
        if me.mana_frac() < 0.85 and me.hp_frac() > 0.55 and me.can("Life Tap"):
            return "Life Tap"
        curse = self.curse_for(foe)
        if curse and not self.curse_up(foe, curse, d.t, 4.0) and me.can(curse):
            return curse
        if foe.cls in SHADOW_FOES and me.can("Shadow Ward"):
            return "Shadow Ward"
        return None

    def rot(self, d, me, foe):
        """The spec's rotation, without Fear and Death Coil (this layer's) and with this layer's curse in place of Curse of the
        Elements (except against a hunter)."""
        veto = me.mod.veto
        saved = dict(veto)
        veto["Fear"] = {"off": True}
        veto["Death Coil"] = {"off": True}
        if self.curse_for(foe) is not None:
            veto["Curse of the Elements"] = {"off": True}
        try:
            return self.rotation(d, me, foe)
        finally:
            veto.clear()
            veto.update(saved)
