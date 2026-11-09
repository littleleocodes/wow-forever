"""Healer lab: a Monte Carlo model of one raid healer keeping a five-member group alive through a boss fight.

The group is one tank taking boss melee (swings, crushing blows, a periodic spike) and four raid members taking periodic raid
damage (`tables.py`). The healer casts from the beta spellbook (ranks, costs, cast times, coefficients from
`forever-spells/<class>.json`), with talent numbers from the beta tooltips (`scorer/effects/forever/<class>.parsed.json`: heal,
mana_cost, crit, cast_time, regen and stat effects) plus the mechanics each class module hand-codes (Illumination, Nature's
Swiftness, Swiftmend, Mana Tide, Inspiration ...). Heals that exceed the deficit overheal; mana follows the five-second rule
and spirit regen; a death ends the run as a failure.

The figure of merit is the **healing capacity**: the multiplier on all incoming damage at which the healer still keeps the
group alive in 90% of runs over the whole fight (bisection with common random numbers). A talent's value is the capacity lost
when it is removed, which combines throughput and mana in one number the way a boss fight does. One module per class
(`priest.py`, `paladin.py`, `shaman.py`, `druid.py`) subclasses `BaseHealer`.
"""
import json
import pathlib
import random
import re

import tables as T

DAMAGE_ONLY = re.compile(r"damage spell|offensive spell", re.I)   # tooltips of talents that cannot touch a heal

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[2]

NUM = re.compile(r"(\d[\d,]*)")
HEAL = re.compile(r"(?:[Hh]eals?|heal)(?: yourself and)?(?: a| the| your)? (?:friendly |single )?target(?: and (?:their|the) party| and the caster)? for (\d[\d,]*) to (\d[\d,]*)")
# (?![\d,]): without it "Heals the target for 776 over 12 sec." backtracked a digit and read a direct heal of 77 on every Rejuvenation
# rank (audit 2026-10-18 row 29); "Heal yourself and a friendly target" (Binding Heal ranks 2-6) had matched neither pattern (row 35)
HEAL1 = re.compile(r"(?:[Hh]eals?|heal) (?:a friendly target|the friendly target|the target|your target) for (\d[\d,]*)(?![\d,])(?! to| over)")
HOT = re.compile(r"(?:heals? the target (?:of|for)|another|an additional) (\d[\d,]*)(?: damage)? over (\d+) sec", re.I)
GROUP_HOT = re.compile(r"heals the target and their party for (\d[\d,]*) over (\d+) sec", re.I)
TICK = re.compile(r"for (\d[\d,]*) every (\d+) sec(?:onds)?(?: for (\d+) sec)?", re.I)
ALLY = re.compile(r"or (\d[\d,]*)(?: to (\d[\d,]*))? healing to an ally")
HEAL2 = re.compile(r"heals them for (\d[\d,]*)")   # Prayer of Mending
ABSORB = re.compile(r"absorbing (\d[\d,]*) damage")
COEF = re.compile(r"([\d.]+)% of spell power \((heal|per tick|direct)\)")


def _num(s):
    return float(s.replace(",", ""))


def _seconds(s):
    m = re.search(r"([\d.]+)\s*(sec|min)", s or "")
    return float(m.group(1)) * (60 if m.group(2) == "min" else 1) if m else 0.0


class Heal:
    """One rank of a healing spell."""

    def __init__(self, name, rank, level, cost, cast, cooldown, school, text, coefs, cost_pct=False):
        self.name, self.rank, self.level, self.cost, self.cast, self.cooldown, self.school, self.text = name, rank, level, cost, cast, cooldown, school, text
        self.cost_pct = cost_pct
        self.heal_min = self.heal_max = 0.0
        self.hot = 0.0          # total periodic healing
        self.hot_dur = 0.0
        self.tick_every = 3.0
        self.absorb = 0.0
        self.group = False
        self.jumps = 0          # Chain Heal: extra targets
        self.jump_falloff = 0.5
        self.channel = "channel" in (cast if isinstance(cast, str) else "")
        self.coef = coefs.get("heal", 0.0)
        self.hot_coef = coefs.get("per tick", 0.0)
        m = HEAL.search(text) or None
        if m:
            self.heal_min, self.heal_max = _num(m.group(1)), _num(m.group(2))
            if "their party" in text:
                self.group = True
        elif HEAL1.search(text):
            self.heal_min = self.heal_max = _num(HEAL1.search(text).group(1))
        elif HEAL2.search(text):
            self.heal_min = self.heal_max = _num(HEAL2.search(text).group(1))
        elif ALLY.search(text):   # Holy Shock, Penance: "... damage to an enemy, or X to Y healing to an ally"
            a = ALLY.search(text)
            self.heal_min, self.heal_max = _num(a.group(1)), _num(a.group(2) or a.group(1))
            if "every 1 sec for 2 sec" in text:   # Penance: three pulses
                self.heal_min, self.heal_max = self.heal_min * 3, self.heal_max * 3
                self.coef *= 3
        gh = GROUP_HOT.search(text)
        h = HOT.search(text)
        if gh:
            self.hot, self.hot_dur, self.group = _num(gh.group(1)), float(gh.group(2)), True
            self.tick_every = 1.0
        elif h:
            self.hot, self.hot_dur = _num(h.group(1)), float(h.group(2))
        tk = TICK.search(text)
        if tk and not self.hot and self.heal_min == 0:
            per, every = _num(tk.group(1)), float(tk.group(2))
            dur = float(tk.group(3)) if tk.group(3) else 0.0
            self.hot, self.hot_dur, self.tick_every = per * (dur / every if dur else 1), dur or every, every
            self.group = "party members" in text or "group members" in text
        ab = ABSORB.search(text)
        if ab:
            self.absorb = _num(ab.group(1))
        if "jumps to heal" in text:
            jm = re.search(r"Heals (\d+) total targets", text)
            self.jumps = (int(jm.group(1)) - 1) if jm else 2
        self.tags = ["type:spell", "heal", f"school:{school}", f"ability:{name}"] + (["instant"] if cast == 0 else []) + \
                    (["direct"] if self.heal_min else []) + (["hot"] if self.hot else []) + (["group"] if self.group else [])

    @property
    def is_heal(self):
        return self.heal_min > 0 or self.hot > 0 or self.absorb > 0

    def avg(self):
        return (self.heal_min + self.heal_max) / 2


def load_book(cls):
    """Every healing spell rank of the class from the beta spellbook, by name (ranks sorted)."""
    data = json.load(open(ROOT / "_reference/data/forever-spells" / f"{cls}.json", encoding="utf-8"))
    book = {}
    for tab in data["tabs"]:
        for sp in tab["spells"]:
            for r in sp["ranks"]:
                text = (r.get("text") or "").replace("\n", " ")
                cost_txt = r.get("cost") or ""
                cost = _num(NUM.search(cost_txt).group(1)) if NUM.search(cost_txt) else 0.0
                cast_txt = (r.get("cast") or "").lower()
                cast = 0.0 if ("instant" in cast_txt or "channel" in cast_txt) else _seconds(cast_txt)
                coefs = {k: float(v) / 100 for v, k in COEF.findall(r.get("coefficient") or "")}
                h = Heal(sp["name"], int(NUM.search(r.get("rank") or "1").group(1)) if NUM.search(r.get("rank") or "") else 1,
                         int(r.get("level") or 1), cost, cast, _seconds(r.get("cooldown")), (r.get("school") or "holy").lower(), text, coefs,
                         cost_pct="base mana" in cost_txt)
                h.channel = "channel" in cast_txt
                if h.is_heal or sp["name"] in ("Nature's Swiftness", "Divine Favor", "Inner Focus", "Power Infusion", "Innervate", "Mana Tide Totem", "Lay on Hands", "Swiftmend", "Water Shield"):
                    book.setdefault(sp["name"], []).append(h)
    for n in book:
        book[n].sort(key=lambda x: (x.level, x.rank))
    if T.DOWNRANK_PENALTY:
        for n, ranks in book.items():
            for i, h in enumerate(ranks):
                nxt = next((r.level for r in ranks[i + 1:] if r.level > h.level), None)
                if nxt is None and DOWNRANK_FAMILY.get(n) in book:
                    nxt = book[DOWNRANK_FAMILY[n]][0].level
                m = downrank_multiplier(h.level, nxt)
                h.coef *= m
                h.hot_coef *= m
    return book


# Forever's downranking penalty (2026-10-09), the raid simulator's rule (raidsim/patches/forever/sim/core/spelldata/downrank.go): Blizzard's
# beta notes (2026-10-01): "spells cast using spell ranks vastly below your current level receive less benefit from your Spell Damage
# and Spell Healing"; no formula published, so TBC's rule for the same wording: a rank keeps (L + 6) / 60 of its coefficient at level
# 60, L being the level before the next rank is taught, when L + 5 is below 60; Classic Era's below-20 rule on top (1 - (20 - taught
# level) x 0.0375) for ranks below a higher one. The priest's Lesser Heal, Heal and Greater Heal are one ladder in Classic, so the
# next rank of Lesser Heal's top is Heal's first and of Heal's top Greater Heal's first (Heal rank 4, taught at 34, keeps 75%).
DOWNRANK_FAMILY = {"Lesser Heal": "Heal", "Heal": "Greater Heal"}


def downrank_multiplier(level, next_level, player_level=60):
    if not next_level or next_level <= level:
        return 1.0
    m = 1.0
    last = next_level - 1
    if last + 5 < player_level:
        m *= (last + 6) / player_level
    if 0 < level < 20:
        m *= 1 - (20 - level) * 0.0375
    return m


def load_parsed(cls):
    return json.load(open(ROOT / "_reference/data/scorer/effects/forever" / f"{cls}.parsed.json", encoding="utf-8"))


def matches(scope, tags):
    return any(s == "all" or s in tags for s in scope)


class Target:
    def __init__(self, name, hp, tank=False):
        self.name, self.hp_max, self.hp, self.tank = name, hp, hp, tank
        self.hots = {}          # spell name -> [per_tick, ticks_left, next_tick_time, total_remaining]
        self.absorb = 0.0
        self.absorb_until = 0.0
        self.shield_lock = 0.0
        self.armor_buff_until = 0.0   # Inspiration / Ancestral Healing
        self.hw_stacks, self.hw_until = 0, 0.0
        self.mending = 0             # Prayer of Mending charges
        self.received = 0.0
        self.dead_at = None

    @property
    def deficit(self):
        return self.hp_max - self.hp

    @property
    def frac(self):
        return self.hp / self.hp_max


class BaseHealer:
    """One class module: spell roles, mechanics and hooks. `SPEC` is the scorer model id."""
    CLASS = ""
    SPEC = ""
    ROLES = {}              # big / fast / hot / group / instant / shield
    MECHANICS = {}          # talent -> description (hand-coded in the hooks below)
    TALENT_SPELLS = {}      # spell name -> talent that teaches it (the spell is not cast without the talent)
    SHARE_SOURCE = {}       # spell name -> scorer source id
    SIMULATED = set()       # talents whose value the lab measures (fits touch only these)
    PIPELINE = {}

    def __init__(self, allocation, game="forever"):
        self.alloc = {k: v for k, v in allocation.items() if v > 0}
        self.book = load_book(self.CLASS)
        for spell, talent in self.TALENT_SPELLS.items():
            if not self.alloc.get(talent):
                self.book.pop(spell, None)
        self.parsed = load_parsed(self.CLASS)
        self.effects = []
        for name, rank in self.alloc.items():
            if name in self.MECHANICS:
                continue   # hand-coded below; the parsed numbers are not applied twice
            text = self.parsed.get(name, {}).get("text", "")
            if DAMAGE_ONLY.search(text) and not re.search(r"heal", text, re.I):
                continue   # a damage-spell talent does nothing for heals (2026-10-02: Elemental Focus's clearcasting proc had parsed as
                #            a permanent -100% mana cost on every spell, so the shaman's deep talent search found "free" heals)
            for e in self.parsed.get(name, {}).get("effects", []):
                vals = e.get("values") or [e.get("per_rank", 0.0) * r for r in range(1, 6)]
                v = vals[min(rank, len(vals)) - 1] if vals else 0.0
                if v:
                    self.effects.append((e["channel"], e["scope"], v))
        self.setup_stats()

    # ---------------------------------------------------------------- stats
    def rank(self, name):
        return self.alloc.get(name, 0)

    def setup_stats(self):
        g = T.HEALER_GEAR[self.CLASS]
        base = T.class_base_stats(self.CLASS, T.LEVEL)
        intellect = (base["intellect"] + g["intellect"] + T.RAID_BUFF_INT + T.RAID_BUFF_STATS) * T.KINGS
        spirit = (base["spirit"] + g["spirit"] + T.RAID_BUFF_SPIRIT + T.RAID_BUFF_STATS) * T.KINGS
        for ch, scope, v in self.effects:
            if ch == "stat" and scope and scope[0] == "stat:intellect":
                intellect *= 1 + v
            elif ch == "stat" and scope and scope[0] == "stat:spirit":
                spirit *= 1 + v
        self.intellect, self.spirit = intellect, spirit
        self.healing = g["healing"] + self.extra_healing()
        self.mp5 = g["mp5"] + T.WISDOM_MP5 + self.extra_mp5()
        self.mana_max = T.class_base_mana(self.CLASS, T.LEVEL) + intellect * T.MANA_PER_INT
        self.mana_max *= 1 + self.max_mana_bonus()
        self.crit_base = T.class_spell_crit(self.CLASS, T.LEVEL, intellect) + g["crit_gear"]
        self.regen_tick = T.class_mana_regen_tick(self.CLASS, spirit)
        self.regen_casting = min(1.0, sum(v for ch, scope, v in self.effects if ch == "regen") + self.extra_regen_casting())

    def extra_healing(self):
        return 0.0

    def extra_mp5(self):
        return 0.0

    def max_mana_bonus(self):
        return 0.0

    def extra_regen_casting(self):
        return 0.0

    # ---------------------------------------------------------------- per-spell numbers (the generic layer + hooks)
    def heal_mult(self, spell, target, sim):
        m = 1.0
        for ch, scope, v in self.effects:
            if ch == "heal" and matches(scope, spell.tags):
                m *= 1 + v
        return m * self.heal_mult_hook(spell, target, sim)

    def heal_mult_hook(self, spell, target, sim):
        return 1.0

    def crit_chance(self, spell, sim, target=None):
        c = self.crit_base
        for ch, scope, v in self.effects:
            if ch == "crit" and matches(scope, spell.tags):
                c += v
        return min(1.0, c + self.crit_hook(spell, sim) + self.crit_target_hook(spell, sim, target))

    def crit_hook(self, spell, sim):
        return 0.0

    def crit_target_hook(self, spell, sim, target):
        """Crit that depends on the heal's target (2026-10-31: the paladin's Boundless Light); 0 without a target."""
        return 0.0

    def crit_mult(self, spell):
        """A critical heal's multiplier (2026-10-31: the paladin's Holy Power raises it)."""
        return T.CRIT_MULT

    def cost(self, spell, sim):
        c = spell.cost * (T.class_base_mana(self.CLASS, T.LEVEL) / 100.0 if spell.cost_pct else 1.0)
        red = 0.0
        for ch, scope, v in self.effects:
            if ch == "mana_cost" and matches(scope, spell.tags):
                red += v
        return max(0.0, c * (1 - min(red, 0.9))) * self.cost_hook(spell, sim)

    def cost_hook(self, spell, sim):
        return 1.0

    def cast_time(self, spell, sim):
        if spell.cast <= 0:
            return 0.0
        t = spell.cast
        for ch, scope, v in self.effects:
            if ch == "cast_time" and matches(scope, spell.tags):
                t -= v
        haste = sum(v for ch, scope, v in self.effects if ch == "haste" and matches(scope, spell.tags))
        return max(0.5, t / (1 + haste)) * self.cast_hook(spell, sim)

    def cast_hook(self, spell, sim):
        return 1.0

    # ---------------------------------------------------------------- hooks
    def on_fight_start(self, sim):
        pass

    def on_heal(self, sim, spell, target, amount, crit):
        pass

    def on_cast_done(self, sim, spell, target):
        pass

    def on_tick(self, sim):
        """Every 2 s (totems, shields)."""
        pass

    def on_hot_expire(self, sim, name, target):
        """A heal over time ran its full duration (not refreshed, not on a dead target): the druid's Bloom (2026-11-08)."""
        pass

    def mending_trigger(self, sim, target):
        pass

    def before_decide(self, sim):
        """Cooldown abilities (Inner Focus, Divine Favor, Nature's Swiftness, Mana Tide, Innervate): return a spell to cast or None."""
        return None

    def cooldown_ready(self, sim, name, cd):
        return sim.t >= sim.cd.get(name, -1e9) + cd

    # ---------------------------------------------------------------- rank choice
    def expected(self, spell, target=None, sim=None):
        """Average healing of one cast (direct + periodic + absorb) before crit and talents."""
        return spell.avg() + spell.coef * self.healing + spell.hot + spell.hot_coef * self.healing * (spell.hot_dur / spell.tick_every if spell.tick_every else 0) + spell.absorb

    def choice(self, name, deficit, target, sim, max_rank=False):
        s = self.pick(name, deficit, sim, max_rank)
        return (s, target) if s else None

    def pick(self, name, deficit, sim, max_rank=False):
        ranks = self.book.get(name)
        if not ranks:
            return None
        if max_rank or not T.DOWNRANK:
            return ranks[-1]
        for r in ranks:
            if self.expected(r) >= deficit * 0.9:
                return r
        return ranks[-1]

    # ---------------------------------------------------------------- policy
    def decide(self, sim):
        """Generic raid-healer priority: emergency > tank > tank HoT > raid member > group heal > nothing."""
        cd_spell = self.before_decide(sim)
        if cd_spell:
            return cd_spell
        tank = sim.tank
        raid = [x for x in sim.targets if not x.tank]
        hurt = sorted([x for x in sim.targets if x.hp > 0 and x.deficit > 0], key=lambda x: x.frac)
        if not hurt:
            return None
        worst = hurt[0]
        R = self.ROLES
        # emergency: the fastest big heal
        if worst.frac < T.EMERGENCY:
            for role in ("instant", "fast", "big"):
                s = self.emergency_spell(sim, role, worst)
                if s:
                    return s
        # the tank
        big = self.book.get(R.get("big"), [None])[-1]
        fast = self.book.get(R.get("fast"), [None])[-1]
        hot = self.book.get(R.get("hot"), [None])[-1]
        if tank.hp > 0 and tank.deficit > 0:
            if big and tank.deficit >= 0.45 * self.expected(big) and sim.incoming_soon(tank):
                return self.choice(R["big"], tank.deficit, tank, sim)
            if hot and tank.frac < 1 - T.HOT_REFRESH_DEFICIT and R["hot"] not in tank.hots and self.hot_ok(sim, tank):
                return self.choice(R["hot"], tank.deficit, tank, sim, max_rank=True)
            if fast and tank.deficit >= 0.8 * self.expected(fast):
                return self.choice(R["fast"], tank.deficit, tank, sim)
        # raid members
        hurt_raid = [x for x in raid if x.hp > 0 and x.frac < T.RAID_HEAL_AT]
        if len(hurt_raid) >= T.GROUP_HEAL_MIN and R.get("group") in self.book:
            g = self.group_spell(sim, hurt_raid)
            if g:
                return g
        if hurt_raid:
            x = hurt_raid[0]
            if hot and R["hot"] not in x.hots and x.deficit > 0.5 * self.expected(hot) and self.hot_ok(sim, x):
                return self.choice(R["hot"], x.deficit, x, sim, max_rank=True)
            return self.choice(R.get("fast") if fast else R.get("big"), x.deficit, x, sim)
        if tank.hp > 0 and tank.deficit > 0.25 * tank.hp_max and (fast or big):
            return self.choice(R.get("fast") if fast else R.get("big"), tank.deficit, tank, sim)
        return None

    def hot_ok(self, sim, target):
        return True

    def emergency_spell(self, sim, role, target):
        name = self.ROLES.get(role)
        if not name or name not in self.book:
            return None
        s = self.book[name][-1]
        if s.cooldown and not self.cooldown_ready(sim, name, s.cooldown):
            return None
        if role == "instant" and not self.instant_ok(sim, s, target):
            return None
        return (s, target)

    def instant_ok(self, sim, spell, target):
        return True

    def group_spell(self, sim, hurt):
        name = self.ROLES.get("group")
        s = self.book[name][-1]
        if s.cooldown and not self.cooldown_ready(sim, name, s.cooldown):
            return None
        return (s, hurt[0])


class Sim:
    """One run of the encounter with one healer."""

    def __init__(self, healer, mult, seed, log=None):
        self.h = healer
        self.m = mult * T.HEALER_SHARE
        self.rng = random.Random(seed)
        self.t = 0.0
        self.tank = Target("tank", T.TANK_HP, tank=True)
        self.targets = [self.tank] + [Target(f"raid{i}", T.RAID_HP) for i in range(1, 5)]
        self.mana = healer.mana_max
        self.cast = None            # (spell, target, end_time)
        self.gcd_until = 0.0
        self.last_cast = -10.0
        self.cd = {}
        self.buffs = {}             # name -> until
        self.next_swing = T.BOSS_SWING
        self.next_spike = T.SPIKE_EVERY
        self.next_pulse = T.RAID_PULSE_EVERY + self.rng.uniform(-T.RAID_PULSE_JITTER, T.RAID_PULSE_JITTER)
        self.next_regen = T.REGEN_TICK
        self.next_potion = T.POTION_FIRST
        self.healed = {}            # spell -> effective healing
        self.overheal = 0.0
        self.oom_time = 0.0
        self.deaths = 0
        self.death_at = None
        self.log = log
        self.temp_crit = 0.0        # Inner Focus / Divine Favor
        self.free_cast = False
        self.instant_next = False   # Nature's Swiftness
        self.events = []            # (time, mana) scheduled mana gains (Mana Tide)
        healer.on_fight_start(self)

    def note(self, msg):
        if self.log is not None:
            self.log.append(f"{self.t:6.1f}s {msg}")

    # ------------------------------------------------------------ damage
    def damage(self, target, amount):
        if target.hp <= 0:
            return
        if target.absorb > 0 and self.t < target.absorb_until:
            used = min(target.absorb, amount)
            target.absorb -= used
            amount -= used
            self.healed["Power Word: Shield"] = self.healed.get("Power Word: Shield", 0.0) + used
        if target.mending > 0 and amount > 0:
            self.h.mending_trigger(self, target)
        target.hp -= amount
        if target.hp <= 0:
            target.hp = 0
            target.dead_at = self.t
            self.deaths += 1
            if self.death_at is None:
                self.death_at = self.t
            self.note(f"{target.name} dies")

    def incoming_soon(self, target):
        return True

    def boss_swing(self):
        tank = self.tank
        if tank.hp <= 0:
            return
        if self.rng.random() < T.TANK_AVOID:
            return
        dmg = T.BOSS_DMG * self.rng.uniform(1 - T.BOSS_DMG_SPREAD, 1 + T.BOSS_DMG_SPREAD)
        if self.rng.random() < T.CRUSH_CHANCE:
            dmg *= T.CRUSH_MULT
        mit = T.TANK_ARMOR_MIT
        if self.t < tank.armor_buff_until:   # +25% armor: A/(A+C) with A -> 1.25A
            a_over_c = mit / (1 - mit)
            mit = 1.25 * a_over_c / (1.25 * a_over_c + 1)
        self.damage(tank, dmg * (1 - mit) * self.m)

    def spike(self):
        if self.tank.hp > 0:
            self.damage(self.tank, T.BOSS_DMG * (1 - T.TANK_ARMOR_MIT) * T.SPIKE_MULT * self.m)

    def pulse(self):
        for x in self.targets:
            if not x.tank and x.hp > 0:
                self.damage(x, T.RAID_PULSE_DMG * self.rng.uniform(1 - T.RAID_PULSE_SPREAD, 1 + T.RAID_PULSE_SPREAD) * self.m)

    # ------------------------------------------------------------ healing
    def apply_heal(self, spell, target, amount, crit=False, label=None):
        if target.hp <= 0:
            return 0.0
        eff = min(target.deficit, amount)
        target.hp += eff
        self.overheal += amount - eff
        key = label or spell.name
        self.healed[key] = self.healed.get(key, 0.0) + eff
        target.received += eff
        self.h.on_heal(self, spell, target, eff, crit)
        return eff

    def land(self, spell, target):
        """A cast completes (or an instant is used)."""
        h = self.h
        crit_c = h.crit_chance(spell, self, target) + self.temp_crit
        self.temp_crit = 0.0
        mult = h.heal_mult(spell, target, self)
        targets = [target]
        if spell.group:
            targets = [x for x in self.targets if x.hp > 0]
        if spell.jumps:
            others = sorted([x for x in self.targets if x is not target and x.hp > 0], key=lambda x: -x.deficit)[:spell.jumps]
            targets = [target] + others
        for i, tg in enumerate(targets):
            f = mult * (spell.jump_falloff ** i if spell.jumps else 1.0)
            if spell.heal_min > 0:
                amt = self.rng.uniform(spell.heal_min, spell.heal_max) + spell.coef * h.healing
                crit = self.rng.random() < crit_c
                amt *= f * (h.crit_mult(spell) if crit else 1.0)
                self.apply_heal(spell, tg, amt, crit)
            if spell.hot > 0:
                ticks = max(1, int(round(spell.hot_dur / spell.tick_every)))
                per = (spell.hot + spell.hot_coef * h.healing * ticks) / ticks * f
                # the expected crit bonus of a HoT whose ticks can crit (T.HOT_CRIT), from the crit chance at the cast (no temporary crit:
                # Inner Focus no longer reaches periodic effects, notes post 4); kept apart from per so Swiftmend and the deficit
                # forecasts read the plain tick
                fc = 1 + min(1.0, h.crit_chance(spell, self)) * (h.crit_mult(spell) - 1) if spell.name in T.HOT_CRIT else 1.0
                tg.hots[spell.name] = [per, ticks, self.t + spell.tick_every, per * ticks, fc]
            if spell.absorb > 0:
                tg.absorb = spell.absorb * f
                tg.absorb_until = self.t + 30.0
                tg.shield_lock = self.t + 15.0
        h.on_cast_done(self, spell, target)

    def tick_hots(self):
        for x in self.targets:
            if x.hp <= 0:
                x.hots.clear()
                continue
            for name in list(x.hots):
                per, left, nxt, _, *rest = x.hots[name]
                fc = rest[0] if rest else 1.0
                if self.t + 1e-9 >= nxt:
                    self.apply_heal(self.h.book[name][-1], x, per * fc, False, label=name)
                    left -= 1
                    if left <= 0:
                        del x.hots[name]
                        self.h.on_hot_expire(self, name, x)
                    else:
                        x.hots[name] = [per, left, nxt + self.h.book[name][-1].tick_every, per * left, fc]

    # ------------------------------------------------------------ mana
    def regen(self):
        casting_recently = self.t - self.last_cast < T.FSR
        # Innervate: "Increases the target's Mana regeneration by 400% and allows 100% of the target's Mana regeneration to continue while
        # casting" (70425): the full regeneration x5 inside the five-second rule too (until 2026-10-17 the casting fraction applied)
        innervate = self.t < self.buffs.get("Innervate", 0.0)
        tick = self.h.regen_tick * (self.h.regen_casting if casting_recently and not innervate else 1.0) * self.buffs_regen_mult()
        self.mana = min(self.h.mana_max, self.mana + tick + self.h.mp5 * T.REGEN_TICK / 5.0)

    def buffs_regen_mult(self):
        return 5.0 if self.t < self.buffs.get("Innervate", 0.0) else 1.0

    def gain_mana(self, amount, why=""):
        self.mana = min(self.h.mana_max, self.mana + amount)

    # ------------------------------------------------------------ main loop
    def run(self):
        h = self.h
        while self.t < T.DURATION:
            # boss and raid damage
            if self.t + 1e-9 >= self.next_swing:
                self.boss_swing()
                self.next_swing += T.BOSS_SWING
            if self.t + 1e-9 >= self.next_spike:
                self.spike()
                self.next_spike += T.SPIKE_EVERY
            if self.t + 1e-9 >= self.next_pulse:
                self.pulse()
                self.next_pulse += T.RAID_PULSE_EVERY + self.rng.uniform(-T.RAID_PULSE_JITTER, T.RAID_PULSE_JITTER)
            if self.tank.hp <= 0 or self.deaths >= 2:
                break
            self.tick_hots()
            if self.t + 1e-9 >= self.next_regen:
                self.regen()
                h.on_tick(self)
                self.next_regen += T.REGEN_TICK
            if self.events and self.t + 1e-9 >= self.events[0][0]:
                self.gain_mana(self.events.pop(0)[1])
            if T.POTIONS and self.t >= self.next_potion and self.mana < T.POTION_BELOW * h.mana_max:
                self.gain_mana(T.POTION_MANA, "potion")
                self.next_potion = self.t + T.POTION_EVERY
            # the healer
            if self.cast is not None:
                spell, target, end = self.cast
                if self.t + 1e-9 >= end:
                    self.cast = None
                    self.last_cast = self.t
                    self.land(spell, target)
            elif self.t + 1e-9 >= self.gcd_until:
                choice = h.decide(self)
                if choice:
                    spell, target = choice
                    cost = 0.0 if self.free_cast else h.cost(spell, self)
                    if cost <= self.mana:
                        self.mana -= cost
                        self.free_cast = False
                        ct = 0.0 if self.instant_next else h.cast_time(spell, self)
                        if ct == 0.0 and spell.cast > 0:
                            self.instant_next = False
                        self.last_cast = self.t
                        self.gcd_until = self.t + T.GCD
                        if spell.cooldown:
                            self.cd[spell.name] = self.t
                        if ct > 0:
                            self.cast = (spell, target, self.t + ct)
                        else:
                            self.land(spell, target)
                            if spell.channel and spell.hot_dur:
                                self.gcd_until = self.t + spell.hot_dur   # channelled: busy for the duration
                    else:
                        self.oom_time += T.DT
            self.t += T.DT
        return self.result()

    def result(self):
        return {"survived": self.death_at is None, "death_at": self.death_at, "healed": self.healed, "overheal": self.overheal,
                "mana_left": self.mana, "oom_time": self.oom_time, "duration": min(self.t, T.DURATION)}


def run_many(healer, mult, seeds):
    return [Sim(healer, mult, s).run() for s in seeds]


def survival(healer, mult, seeds):
    return sum(1 for r in run_many(healer, mult, seeds) if r["survived"]) / len(seeds)


def seed_capacity(healer, seed, lo=0.1, hi=4.0, steps=10):
    """The largest damage multiplier this run (its random draws fixed by the seed) survives: bisection, 0.4% resolution."""
    if Sim(healer, hi, seed).run()["survived"]:
        return hi
    if not Sim(healer, lo, seed).run()["survived"]:
        return lo
    for _ in range(steps):
        mid = (lo + hi) / 2
        if Sim(healer, mid, seed).run()["survived"]:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def capacities(healer, seeds, steps=10):
    return sorted(seed_capacity(healer, s, steps=steps) for s in seeds)


def capacity(healer, seeds, steps=10, need=None):
    """The damage multiplier the healer survives in (1 - DEATH_RUNS_OK) of the runs: that percentile of the per-run capacities
    (common random numbers: the same seeds for every build and talent removal, so differences are paired)."""
    need = need if need is not None else 1.0 - T.DEATH_RUNS_OK
    cs = capacities(healer, seeds, steps)
    # the mean of the worst (1 - need) x 2 runs: a tail mean is a much steadier statistic than the percentile itself
    k = max(1, int(round(2 * (1.0 - need) * len(cs))))
    return sum(cs[:k]) / k


def summarise(healer, mult, seeds):
    """Healing split, overheal and mana at the reference multiplier."""
    rs = run_many(healer, mult, seeds)
    healed = {}
    for r in rs:
        for k, v in r["healed"].items():
            healed[k] = healed.get(k, 0.0) + v / len(rs)
    tot = sum(healed.values()) or 1.0
    over = sum(r["overheal"] for r in rs) / len(rs)
    return {"multiplier": mult, "shares": {k: v / tot for k, v in sorted(healed.items(), key=lambda kv: -kv[1])}, "hps": tot / T.DURATION,
            "overheal_share": over / (tot + over) if tot + over else 0.0, "oom_time": sum(r["oom_time"] for r in rs) / len(rs),
            "mana_left": sum(r["mana_left"] for r in rs) / len(rs), "survival": sum(1 for r in rs if r["survived"]) / len(rs)}
