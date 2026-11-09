"""Restoration shaman raid healer for the healer lab: Healing Wave on the tank (downranked to the deficit), Lesser Healing Wave
when it must land fast, Chain Heal when the group is hurt, Riptide (a heal over time, 12 s cooldown) when talented, Healing Stream
Totem ticking on the group, Nature's Swiftness for an instant Healing Wave, Mana Tide when mana runs low; Ancestral Healing armors the
tank after a crit."""
import json
import pathlib
import re

import engine as E
import tables as T

PIPELINE = {"spec": "resto-heal", "hand": "resto-raid-healer", "opt": "opt-resto-heal-raid-heal", "tag": "resto"}

_DATA = pathlib.Path(__file__).resolve().parent.parent


def _riptide_chain_heal_bonus():
    """Riptide: "increases the effectiveness of your Chain Heal casts directly on that target by 25%" (the beta spellbook)."""
    for tab in json.load(open(_DATA / "forever-spells" / "shaman.json", encoding="utf-8"))["tabs"]:
        for sp in tab["spells"]:
            if sp["name"] == "Riptide":
                m = re.search(r"Chain Heal casts directly on that target by (\d+)%", sp["ranks"][-1].get("text") or "")
                if m:
                    return float(m.group(1)) / 100
    return 0.25


def _ancestral_healing_armor():
    """Ancestral Healing's armor bonus per rank ("Increases your target's armor value by 8/17/25% for 15 sec after getting a critical
    effect from one of your healing spells")."""
    for tr in json.load(open(_DATA / "forever-talents" / "shaman.json", encoding="utf-8"))["trees"]:
        for tl in tr["talents"]:
            if tl["name"] == "Ancestral Healing":
                return [float(re.search(r"armor value by (\d+)%", r).group(1)) / 100 for r in tl["ranks"]]
    return [0.08, 0.17, 0.25]


def _water_shield():
    """(globes, mana share a globe) from the beta spellbook: "surrounded by 3 globes of water ... 2% of maximum mana is restored to the
    caster, expending one water globe. Only one globe will activate every few seconds. Lasts 10 min."""
    for tab in json.load(open(_DATA / "forever-spells" / "shaman.json", encoding="utf-8"))["tabs"]:
        for sp in tab["spells"]:
            if sp["name"] == "Water Shield":
                t = sp["ranks"][-1].get("text") or ""
                g, m = re.search(r"(\d+) globes", t), re.search(r"(\d+(?:\.\d+)?)% of maximum mana", t)
                return (int(g.group(1)) if g else 3), (float(m.group(1)) / 100 if m else 0.02)
    return 3, 0.02


def _riptide_ranks():
    """Riptide's ranks as heals over time. Blizzard's notes of 2026-11-02 (client 70753): "Riptide: Mana cost reduced by about 40%. Cooldown
    increased to 12 seconds from 6 seconds. Riptide no longer deals any initial healing, just healing over time." The 2026-11-03 export has
    the new text ("Heals a friendly target for 805 over 15 sec, and increases ...") and cooldown, which the engine's heal patterns do not
    read (engine.HOT wants "heals the target for N over T sec"; the spell fell out of the book), and the old mana (245/300/385): a rank whose
    cost is still the pre-notes one pays RIPTIDE_MANA of it (147/180/231). Ticks every RIPTIDE_TICK s (the client's 3 s, as Renew; the
    tooltip names none), 10% of healing a tick by the export's coefficient field (its 21.4% direct part went with the direct heal)."""
    out = []
    for tab in json.load(open(_DATA / "forever-spells" / "shaman.json", encoding="utf-8"))["tabs"]:
        for sp in tab["spells"]:
            if sp["name"] != "Riptide":
                continue
            for r in sp["ranks"]:
                text = (r.get("text") or "").replace("\n", " ")
                m = re.search(r"Heals a friendly target for (\d[\d,]*) over (\d+) sec", text)
                if not m:
                    continue
                cost = float(re.search(r"(\d[\d,]*)", r.get("cost") or "0").group(1).replace(",", ""))
                if cost in RIPTIDE_OLD_COST:
                    cost = round(cost * RIPTIDE_MANA)
                cd = re.search(r"(\d+) sec cooldown", r.get("cooldown") or "")
                coefs = {k: float(v) / 100 for v, k in re.findall(r"([\d.]+)% of spell power \((heal|per tick|direct)\)", r.get("coefficient") or "")}
                h = E.Heal("Riptide", int(re.search(r"(\d+)", r.get("rank") or "1").group(1)) if re.search(r"\d", r.get("rank") or "") else 1,
                           int(r.get("level") or 1), cost, 0.0, float(cd.group(1)) if cd else 12.0, "nature", text, {})
                h.heal_min = h.heal_max = 0.0
                h.coef = 0.0
                h.hot, h.hot_dur, h.tick_every = float(m.group(1).replace(",", "")), float(m.group(2)), RIPTIDE_TICK
                h.hot_coef = coefs.get("per tick", 0.0)
                h.tags = ["type:spell", "heal", "school:nature", "ability:Riptide", "instant", "hot"]
                out.append(h)
    out.sort(key=lambda x: (x.level, x.rank))
    if T.DOWNRANK_PENALTY:   # as engine.load_book
        for i, h in enumerate(out):
            nxt = next((x.level for x in out[i + 1:] if x.level > h.level), None)
            h.hot_coef *= E.downrank_multiplier(h.level, nxt)
    return out


RIPTIDE_OLD_COST = (245.0, 300.0, 385.0)   # the export's Riptide mana before and after the notes of 2026-11-02 (ranks 1-3)
RIPTIDE_MANA = 0.6                         # "Mana cost reduced by about 40%"
RIPTIDE_TICK = 3.0
RIPTIDE_CHAIN_HEAL = _riptide_chain_heal_bonus()
WATER_SHIELD_GLOBES, WATER_SHIELD_MANA = _water_shield()
# "every few seconds": 3.5 s, the client value the community simulator pins for spell 408510 (sim/shaman/shields.go at db4d14a; one timer
# for hits taken and spell crits). The healer takes no damage in the lab, so only its own critical heals spend globes.
WATER_SHIELD_ICD = 3.5
ANCESTRAL_HEALING_ARMOR = _ancestral_healing_armor()
ENGINE_ARMOR_BUFF = 0.25   # engine.Sim.boss_swing gives the tank +25% armor while `armor_buff_until` runs (Inspiration, Ancestral Healing)


class Healer(E.BaseHealer):
    CLASS = "shaman"
    SPEC = "resto-heal"
    # Riptide heals over time only since 2026-11-02 (no initial heal): the tank's HoT, no longer the emergency heal ("instant" until then)
    ROLES = {"big": "Healing Wave", "fast": "Lesser Healing Wave", "group": "Chain Heal", "hot": "Riptide"}
    TALENT_SPELLS = {"Riptide": "Riptide", "Mana Tide Totem": "Mana Tide Totem", "Nature's Swiftness": "Nature's Swiftness", "Water Shield": "Water Shield"}
    MECHANICS = {
        "Nature's Swiftness": "instant Healing Wave on a tank under 35%, every 3 min",
        "Mana Tide Totem": "290 mana every 3 s for 12 s when mana is under 50%, every 5 min",
        "Ancestral Healing": "every critical heal: +8/17/25% armor on the target for 15 s (the engine's armor buff is a fixed +25%, so ranks 1-2 "
                             "apply it on 32%/68% of crits: the same average armor)",
        "Water Shield": "3 globes, cast before the pull: a critical direct heal spends one for 2% of maximum mana (one globe every 3.5 s; client "
                        "70425: any spell crit, and the lab casts only heals); recast (a global cooldown, no mana) when the globes run out "
                        "and the tank is not in danger (2026-10-17: the lab had unlimited globes every 3 s)",
        "Totemic Focus": "totem mana only: nothing for heals",
        "Elemental Focus": "clearcasting from damage spells, for the next damage spell: nothing for heals",
        "Riptide": "a 15 s HoT (805 at rank 3, a tick every 3 s) on a 12 s cooldown for 231 mana (70753: no initial heal, about 40% less mana, "
                   "6 s before): the tank's HoT, kept up while the cooldown allows; a Chain Heal cast on a target with your Riptide heals 25% more "
                   "(every jump: the cast's effectiveness), and Chain Heal starts on a hurt member with your Riptide",
        "Healing Stream Totem": "placed at the pull: 11 (+Restorative Totems) every 2 s on the group",
    }
    SIMULATED = {"Nature's Swiftness", "Mana Tide Totem", "Ancestral Healing", "Water Shield", "Riptide", "Healing Way", "Improved Healing Wave", "Tidal Mastery", "Purification",
                 "Tidal Focus", "Restorative Totems", "Ancestral Knowledge", "Mindfulness", "Thundering Strikes"}
    # talents with raid value the lab leaves out, which heallab/filler_pass.py never moves (2026-11-09: the pass had moved Totemic Focus to
    # Natural Grace): a raid shaman keeps the group's totems up all fight and recasts them; the lab charges Healing Stream Totem once
    KEEP = {"Totemic Focus": "the group's totems are recast all fight; the lab charges one totem at the pull"}
    SHARE_SOURCE = {"Chain Heal": "chain_heal", "Healing Wave": "healing_wave", "Lesser Healing Wave": "lesser_hw", "Healing Stream Totem": "healing_stream"}

    def __init__(self, allocation, game="forever"):
        super().__init__(allocation, game)
        if self.alloc.get("Riptide") and "Riptide" not in self.book:   # the engine's patterns miss the HoT-only text (_riptide_ranks)
            ranks = _riptide_ranks()
            if ranks:
                self.book["Riptide"] = ranks

    def hot_ok(self, sim, target):
        """Riptide's 12 s cooldown (engine.BaseHealer.decide's HoT branch checks no cooldown: with the 6 s one Riptide went out on every
        GCD a target lacked it until 2026-11-03)."""
        s = self.book.get("Riptide", [None])[-1]
        return s is None or not s.cooldown or self.cooldown_ready(sim, "Riptide", s.cooldown)

    def on_fight_start(self, sim):
        sim.mana -= 80.0   # Healing Stream Totem
        sim.water_globe = -10.0
        sim.water_globes = WATER_SHIELD_GLOBES if "Water Shield" in self.book else 0   # cast before the pull

    def on_tick(self, sim):
        hst = self.book.get("Healing Stream Totem")
        if hst:
            per = hst[-1].hot / max(1.0, hst[-1].hot_dur / hst[-1].tick_every) if hst[-1].hot else 11.0
            mult = self.heal_mult(hst[-1], None, sim)
            for x in sim.targets:
                if x.hp > 0:
                    sim.apply_heal(hst[-1], x, per * mult, False, label="Healing Stream Totem")

    def heal_mult_hook(self, spell, target, sim):
        """Riptide: "increases the effectiveness of your Chain Heal casts directly on that target by 25%": a Chain Heal aimed at a target
        with your Riptide on it. Read as the cast's effectiveness, so every jump gains (engine.Sim.land applies one multiplier to the
        chain; healing the primary target alone more would need an engine change)."""
        if spell.name == "Chain Heal" and target is not None and "Riptide" in target.hots:
            return 1.0 + RIPTIDE_CHAIN_HEAL
        return 1.0

    def group_spell(self, sim, hurt):
        """Chain Heal starts on a target with your Riptide when there is one worth it: the tank (the lab keeps Riptide there) when it misses
        at least as much as the most hurt raid member, else the most hurt raid member with Riptide, else the most hurt (the generic choice).
        The jumps go to the most hurt others either way (engine.Sim.land)."""
        g = super().group_spell(sim, hurt)
        if not g:
            return g
        tank = sim.tank
        if tank.hp > 0 and "Riptide" in tank.hots and tank.deficit >= (hurt[0].deficit if hurt else 0.0):
            return (g[0], tank)
        rt = [x for x in hurt if "Riptide" in x.hots]
        return (g[0], rt[0]) if rt else g

    def on_heal(self, sim, spell, target, amount, crit):
        # Ancestral Healing: the tooltip's armor on every critical heal; the engine's fixed +25% stands in, on armor/25% of the crits
        rank = self.rank("Ancestral Healing")
        if crit and rank and sim.rng.random() < ANCESTRAL_HEALING_ARMOR[min(rank, len(ANCESTRAL_HEALING_ARMOR)) - 1] / ENGINE_ARMOR_BUFF:
            target.armor_buff_until = sim.t + 15.0
        if crit and sim.water_globes > 0 and sim.t >= sim.water_globe + WATER_SHIELD_ICD:
            sim.water_globe = sim.t
            sim.water_globes -= 1
            sim.gain_mana(WATER_SHIELD_MANA * self.mana_max, "Water Shield")

    def before_decide(self, sim):
        tank = sim.tank
        if "Mana Tide Totem" in self.book and sim.mana < 0.5 * self.mana_max and self.cooldown_ready(sim, "Mana Tide Totem", 300.0):
            sim.cd["Mana Tide Totem"] = sim.t
            sim.mana -= 60.0
            sim.events += [(sim.t + 3.0 * i, 290.0) for i in range(1, 5)]
            sim.gcd_until = sim.t + T.GCD
            return None
        if "Nature's Swiftness" in self.book and tank.hp > 0 and tank.frac < T.EMERGENCY and self.cooldown_ready(sim, "Nature's Swiftness", 180.0):
            sim.cd["Nature's Swiftness"] = sim.t
            sim.instant_next = True
            return (self.book["Healing Wave"][-1], tank)
        if "Water Shield" in self.book and sim.water_globes <= 0 and (tank.hp <= 0 or tank.frac >= T.EMERGENCY):
            sim.water_globes = WATER_SHIELD_GLOBES   # recast: a global cooldown, no mana
            sim.water_shield_casts = getattr(sim, "water_shield_casts", 0) + 1
            sim.gcd_until = sim.t + T.GCD
            return None
        return None

    def instant_ok(self, sim, spell, target):
        return spell.name != "Riptide" or "Riptide" not in target.hots
