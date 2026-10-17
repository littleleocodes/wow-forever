"""Holy priest raid healer for the healer lab: Greater Heal on the tank (downranked to the deficit), Flash Heal when it must
land fast, Renew kept on the tank, Prayer of Healing when the group is hurt, Power Word: Shield on a tank in danger, Penance
on the tank whenever it is ready (and in emergencies) and Prayer of Mending when talented; Inner Focus before a Greater Heal,
Power Infusion on cooldown.

2026-10-09 (beta 70291): Divine Aegis, Renewed Hope and Litany of Light are simulated (they had no effect in the lab); Power
Infusion and Prayer of Mending cost their mana and a global cooldown (both had been free, Power Infusion of mana too); Penance
keeps the healer busy for its 2 s channel (it had taken one global cooldown); Renew's ticks carry the expected critical bonus
(Renew can crit since the 2026-10-08 beta build). Talent numbers come from the 70291 tooltips (forever-talents/priest.json),
spell numbers from the spellbook (forever-spells/priest.json).

2026-10-16 (client 70425): Divine Aegis caps its shield at 1,200 (the tooltip's second number, which the duration had been read from);
Mental Strength is 2%/rank Intellect (parsed). Twin Disciplines' 16 Oct widening to Penance needs no change here (Penance is an instant)."""
import json
import pathlib
import re

import engine as E
import tables as T

PIPELINE = {"spec": "holy-heal", "hand": "holy-raid-healer", "opt": "opt-holy-heal-raid-heal", "tag": "holy"}

DATA = pathlib.Path(__file__).resolve().parents[1]
NUM = re.compile(r"(\d+(?:\.\d+)?)")
_TREES = json.load(open(DATA / "forever-talents" / "priest.json", encoding="utf-8"))["trees"]
TNUM = {t["name"]: [[float(x) for x in NUM.findall((r or "").replace(",", ""))] for r in t["ranks"]] for tr in _TREES for t in tr["talents"]}
_TALENT_TEXT = {t["name"]: (t["ranks"][-1] or "") for tr in _TREES for t in tr["talents"]}
_SPELLS = {sp["name"]: sp for tab in json.load(open(DATA / "forever-spells" / "priest.json", encoding="utf-8"))["tabs"] for sp in tab["spells"]}


def _spell_text(name):
    ranks = (_SPELLS.get(name) or {}).get("ranks") or [{}]
    return (ranks[-1].get("text") or "").replace("\n", " ")


# Renewed Hope's heals, from its tooltip: "Your heals from Flash Heal, Binding Heal, Lesser Heal, Heal, Greater Heal, and Penance gain ..."
_rh = re.search(r"heals from (.+?) gain", _TALENT_TEXT.get("Renewed Hope", ""))
RENEWED_HOPE_HEALS = tuple(x.strip() for x in re.split(r",\s*(?:and\s+)?|\s+and\s+", _rh.group(1)) if x.strip()) if _rh else \
    ("Flash Heal", "Binding Heal", "Lesser Heal", "Heal", "Greater Heal", "Penance")
_m = re.search(r"every \d+ sec for (\d+) sec", _spell_text("Penance"))
PENANCE_CHANNEL = float(_m.group(1)) if _m else 2.0          # "instantly and every 1 sec for 2 sec": a 2 s channel
_m = re.search(r"by (\d+)% for (\d+) sec", _spell_text("Power Infusion"))
PI_BONUS, PI_SECONDS = (float(_m.group(1)) / 100, float(_m.group(2))) if _m else (0.20, 15.0)


class Healer(E.BaseHealer):
    CLASS = "priest"
    SPEC = "holy-heal"
    ROLES = {"big": "Greater Heal", "fast": "Flash Heal", "hot": "Renew", "group": "Prayer of Healing", "shield": "Power Word: Shield", "instant": "Penance"}
    TALENT_SPELLS = {"Penance": "Penance", "Prayer of Mending": "Prayer of Mending", "Inner Focus": "Inner Focus", "Power Infusion": "Power Infusion", "Binding Heal": "Binding Heal"}
    MECHANICS = {
        "Inner Focus": "next Greater Heal free and +25% crit, every 3 min",
        "Power Infusion": "+20% healing for 15 s every 3 min, cast on yourself (20% of base mana and a global cooldown)",
        "Spiritual Guidance": "+5%/rank of Spirit as healing",
        "Inspiration": "a critical heal gives the target +25% armor for 15 s (33%/rank chance)",
        "Improved Power Word: Shield": "+7/14/20% absorb",
        "Soul Warding": "Power Word: Shield without its 4 s cooldown and 15% cheaper",
        "Twin Disciplines": "+1%/rank healing of instant casts",
        "Mental Agility": "-3/7/10% mana cost of instant casts",
        "Penance": "an instant 3-pulse heal on a 12 s cooldown that keeps the healer busy for its 2 s channel: on the tank whenever it is "
                   "ready and he misses 80% of its heal, and the emergency heal",
        "Prayer of Mending": "kept on the tank: heals 413 when he is hit, then jumps (5 charges, 10 s cooldown, a global cooldown to place)",
        "Binding Heal": "never cast: Flash Heal fills its role (its self-heal would be idle, the healer takes no damage here)",
        "Divine Aegis": "a critical non-periodic heal leaves an absorb of 5%/rank of the amount healed on the target for 12 s, the Aegis "
                        "part at most 1,200 (client 70425's cap; it joins the target's shield; a new Power Word: Shield replaces it)",
        "Renewed Hope": "+2%/rank crit for Flash Heal, Binding Heal, Lesser Heal, Heal, Greater Heal and Penance on a target with Weakened "
                        "Soul; each such heal takes 1 s/rank off its Weakened Soul",
        "Litany of Light": "a heal unlike your previous one returns 5%/rank of its base mana cost",
    }
    SIMULATED = {"Inner Focus", "Power Infusion", "Spiritual Guidance", "Inspiration", "Improved Power Word: Shield", "Soul Warding", "Twin Disciplines", "Mental Agility",
                 "Penance", "Prayer of Mending", "Meditation", "Holy Specialization", "Improved Renew", "Improved Healing", "Divine Fury", "Spiritual Healing", "Mental Strength",
                 "Divine Aegis", "Renewed Hope", "Litany of Light"}
    SHARE_SOURCE = {"Greater Heal": "greater_heal", "Flash Heal": "flash_heal", "Renew": "renew", "Prayer of Healing": "prayer_of_healing", "Power Word: Shield": "shield",
                    "Heal": "heal", "Lesser Heal": "heal", "Binding Heal": "flash_heal"}
    # heal-choice policies of this module (heallab/rotation_opt.py tunes tables.py's knobs only, not these). 2026-10-09, 20 seeds and a
    # 40-seed confirmation on fresh seeds: Penance on the tank at 0.8 of its heal +6.4% capacity (Holy) and +4.3% (Discipline) over
    # emergencies only (Blizzard, 2026-10-08: Penance now heals more per mana than Heal and Greater Heal); on the 20 seeds 0.5 gave Holy
    # +9.3% and Discipline +3.4%, 0.8 +9.4% and +5.3%, 1.0 +7.4% and +6.2%: 0.8 is the setting both specs share.
    # The tank shield on every Weakened Soul cost capacity (Holy -5%, Discipline -0.4%: mana runs out first), so it stays off.
    PENANCE_TANK_DEFICIT = 0.8    # Penance on the tank whenever it is ready and he misses this share of its heal (None: emergencies only)
    SHIELD_TANK = False           # Power Word: Shield on the tank whenever Weakened Soul is gone (False: emergencies only)

    def tv(self, name, idx=0):
        """The talent's idx-th number in its tooltip at the rank this build holds (0 when untalented)."""
        r = self.rank(name)
        nums = TNUM.get(name, [])
        return nums[r - 1][idx] if r and r <= len(nums) and idx < len(nums[r - 1]) else 0.0

    def extra_healing(self):
        return 0.05 * self.rank("Spiritual Guidance") * self.spirit

    def heal_mult_hook(self, spell, target, sim):
        m = 1.0
        if "instant" in spell.tags:
            m *= 1 + 0.01 * self.rank("Twin Disciplines")
        if spell.name == "Power Word: Shield":
            m *= 1 + [0, 0.07, 0.14, 0.20][min(3, self.rank("Improved Power Word: Shield"))]
        if sim.t < sim.buffs.get("Power Infusion", 0.0):
            m *= 1 + PI_BONUS
        return m

    def cost_hook(self, spell, sim):
        f = 1.0
        if "instant" in spell.tags and not spell.channel:   # "instant cast spells": not a channel (Penance; 2026-10-17, audit finding 15)
            f *= 1 - [0, 0.03, 0.07, 0.10][min(3, self.rank("Mental Agility"))]
        if spell.name == "Power Word: Shield" and self.rank("Soul Warding"):
            f *= 0.85
        return f

    def crit_hook(self, spell, sim):
        """Renewed Hope: more crit on a target with Weakened Soul (the cast's target: decide() keeps it until the heal lands)."""
        tg = getattr(sim, "priest_target", None)
        if self.rank("Renewed Hope") and spell.name in RENEWED_HOPE_HEALS and tg is not None and sim.t < tg.shield_lock:
            return self.tv("Renewed Hope", 0) / 100
        return 0.0

    def on_fight_start(self, sim):
        sim.priest_target, sim.priest_last_heal, sim.priest_busy = None, None, False

    def decide(self, sim):
        sim.priest_busy = False
        choice = super().decide(sim)
        if sim.priest_busy:   # Power Infusion or Prayer of Mending took this global cooldown
            return None
        sim.priest_target = choice[1] if choice else None
        return choice

    def on_heal(self, sim, spell, target, amount, crit):
        if crit and self.rank("Inspiration") and sim.rng.random() < self.rank("Inspiration") / 3.0:
            target.armor_buff_until = sim.t + 15.0
        # Divine Aegis: an absorb of 15% (3/3) of the amount healed, 12 s. Client 70425: non-periodic crits only (periodic ticks reach
        # on_heal with crit False) and "Shields up to 1,200 damage": the Aegis part of the target's absorb never exceeds the cap (the
        # tooltip's numbers: percentage, cap, seconds; the cap's slot had held the duration before)
        if crit and amount > 0 and self.rank("Divine Aegis"):
            cap, dur = self.tv("Divine Aegis", 1) or 1200.0, self.tv("Divine Aegis", 2) or 12.0
            live = target.absorb > 0 and sim.t < target.absorb_until
            aegis = min(target.absorb, getattr(target, "aegis", 0.0)) if live else 0.0
            add = max(0.0, min(cap, aegis + amount * self.tv("Divine Aegis", 0) / 100) - aegis)
            if live:
                target.absorb += add
                target.absorb_until = max(target.absorb_until, sim.t + dur)
            else:
                target.absorb, target.absorb_until = add, sim.t + dur
            target.aegis = aegis + add

    def on_cast_done(self, sim, spell, target):
        if spell.name == "Power Word: Shield":   # the shield replaces the target's absorb: no Aegis left in it (Divine Aegis' cap)
            target.aegis = 0.0
        if self.rank("Renewed Hope") and spell.name in RENEWED_HOPE_HEALS and sim.t < target.shield_lock:
            target.shield_lock = max(sim.t, target.shield_lock - self.tv("Renewed Hope", 1))
        # Renew's tick crits: the engine's expected bonus for every HoT in tables.HOT_CRIT (2026-10-17; this module had done it for Renew)
        if spell.name == "Penance":   # busy for the whole channel, not just the global cooldown
            sim.gcd_until = max(sim.gcd_until, sim.t + PENANCE_CHANNEL)
        self.litany(sim, spell)

    def litany(self, sim, spell):
        """Litany of Light: a heal unlike your previous one returns 5%/rank of its base mana cost (a shield absorbs, it is no heal)."""
        if spell.heal_min <= 0 and spell.hot <= 0:
            return
        last, sim.priest_last_heal = getattr(sim, "priest_last_heal", None), spell.name
        r = self.tv("Litany of Light", 0)
        if r and last is not None and last != spell.name:
            base = spell.cost * (T.class_base_mana(self.CLASS, T.LEVEL) / 100.0 if spell.cost_pct else 1.0)
            sim.gain_mana(base * r / 100)

    def before_decide(self, sim):
        pi = (self.book.get("Power Infusion") or [None])[-1]
        if pi is not None and self.cooldown_ready(sim, "Power Infusion", pi.cooldown or 180.0) and sim.mana > 0.2 * self.mana_max:
            cost = self.cost(pi, sim)   # 20% of base mana (tooltip); on yourself, a global cooldown
            if cost <= sim.mana:
                sim.mana -= cost
                sim.cd["Power Infusion"] = sim.t
                sim.buffs["Power Infusion"] = sim.t + PI_SECONDS
                sim.gcd_until, sim.last_cast = sim.t + T.GCD, sim.t
                sim.priest_busy = True
                return None
        if "Inner Focus" in self.book and self.cooldown_ready(sim, "Inner Focus", 180.0) and sim.tank.deficit > 0.5 * self.expected(self.book["Greater Heal"][-1]):
            sim.cd["Inner Focus"] = sim.t
            sim.free_cast, sim.temp_crit = True, 0.25
            return (self.book["Greater Heal"][-1], sim.tank)
        if "Prayer of Mending" in self.book and not any(x.mending for x in sim.targets) and self.cooldown_ready(sim, "Prayer of Mending", 10.0) and sim.tank.hp > 0 and sim.tank.deficit > 0:
            pom = self.book["Prayer of Mending"][-1]
            cost = self.cost(pom, sim)
            if cost <= sim.mana:
                sim.cd["Prayer of Mending"] = sim.t
                sim.mana -= cost
                sim.tank.mending = 5
                sim.gcd_until, sim.last_cast = sim.t + T.GCD, sim.t
                sim.priest_busy = True
                self.litany(sim, pom)
                return None
        tank = sim.tank
        pws = (self.book.get("Power Word: Shield") or [None])[-1]
        if self.SHIELD_TANK and pws is not None and tank.hp > 0 and sim.t >= tank.shield_lock and \
                (self.rank("Soul Warding") or self.cooldown_ready(sim, "Power Word: Shield", pws.cooldown or 4.0)):
            return (pws, tank)
        pen = (self.book.get("Penance") or [None])[-1]
        if self.PENANCE_TANK_DEFICIT and pen is not None and tank.hp > 0 and self.cooldown_ready(sim, "Penance", pen.cooldown or 12.0) and \
                tank.deficit >= self.PENANCE_TANK_DEFICIT * self.expected(pen):
            return (pen, tank)
        return None

    def mending_trigger(self, sim, target):
        pom = self.book.get("Prayer of Mending")
        if not pom or target.mending <= 0:
            return
        sim.apply_heal(pom[-1], target, pom[-1].heal_min * self.heal_mult(pom[-1], target, sim), False)
        target.mending -= 1
        if target.mending > 0:
            others = sorted([x for x in sim.targets if x is not target and x.hp > 0], key=lambda x: x.frac)
            if others:
                others[0].mending, target.mending = target.mending, 0

    def emergency_spell(self, sim, role, target):
        if role == "instant" and "Power Word: Shield" in self.book and target.tank and sim.t >= target.shield_lock and \
                (self.rank("Soul Warding") or self.cooldown_ready(sim, "Power Word: Shield", 4.0)):
            return (self.book["Power Word: Shield"][-1], target)
        return super().emergency_spell(sim, role, target)

    def hot_ok(self, sim, target):
        return True
