"""Pre-BiS and phase-1 BiS gear for every healer spec, chosen by stat weights measured in the healer lab (2026-10-15, user decision
2026-10-14: healers get real gear sets "like the DPS pages"; healers are in no community simulator, so the weights come from our lab).

    python -u _reference/data/heallab/heal_gear.py [classes] [--spec Holy] [--fresh] [--jobs 6] [--smoke]

Per healer spec (spec_modes.HEAL_TREES: priest Holy and Discipline, paladin Holy, druid and shaman Restoration):
1. **The build**: the spec's raid pick as the raid page ranks it (render_modes.rank_builds: the spec's raid healer builds by the healer
   lab's capacity in `<class>/research/raid/heallab/*.json`, file order on ties); printed and recorded.
2. **Stat weights**: the lab's gear model is one stats dict per class (`tables.HEALER_GEAR`: Intellect, Spirit, healing power, mp5, gear
   crit; raid buffs, Kings and talents are applied on top by `engine.Healer.setup_stats`). Each stat is moved by +-delta (`DELTA`) and the
   capacity measured on the same seeds (common random numbers; `heal_worker.seed_caps`, at most --jobs processes); weight = central
   difference / (2 delta), capacity per unit of gear stat. Standard errors by a paired bootstrap over seeds (the capacity is a tail mean,
   so differences are not per-seed averages). Healing-power equivalents (weight / healing weight) with their bootstrap errors.
   Stamina, armor, resistances, haste and hit are worth 0 here: the lab never damages the healer and has no gear haste (stated, not
   measured). Spell damage without healing power (database stat 5 alone) is worth 0: the simulator heals with its HealingPower stat only.
3. **Sets**: the item pools of the damage tiers (raidsim/gear_tiers.py `pool_of`: bis = phase-1 pool, prebis = no raid drops, no raid-boss
   quest rewards, no crafts from Molten Core or Onyxia materials; gear_opt's class allowlist and armor limit; no random-suffix items),
   items from the simulator's `assets/database/db.json`. Per slot the item worth most by the weights (static stats only), each armor and
   weapon slot with the healer enchant worth most (raidsim/fill_enchants.py `HEALER_CANDIDATES`); main hand + off-hand or shield against a
   two-hander by the class's Classic weapon skills (`PROFICIENCY`); two different rings and two different trinkets by static stats; the
   relic or wand by static stats (left empty when none has any). Then the weights are measured again at that set's stats and the slots
   re-chosen; when the second set differs, both are raced (paired) and the better is kept.
   Not valued (the lab has no model for them; stated on the report): set bonuses, on-use and proc effects (most healing trinkets and
   relics: Hibernation Crystal, Talisman of Ephemeral Power, the totems and librams with spell effects score only their static stats),
   items that need a profession (Truefaith Vestments) or a faction.
4. **Check**: capacity of the build in the lab's assumed gear, the pre-BiS set and the BiS set on the same fresh seeds (paired ratios with
   bootstrap errors), and on the lab's standard seeds (run.py: 60 runs, 10 steps, the pages' convention).
Writes `raidsim/gear_sets/forever/tiers/<class>-<spec slug>-<prebis|bis>.gear.json` (the damage tiers' format; healer spec slugs do not
clash with any damage set), the record `heallab/heal-gear.json` (resumable per spec; --fresh redoes) and `<class>/research/raid/heallab/
gear.md`. `--smoke` runs tiny budgets into `heallab/deep-smoke/heal-gear/` (git-ignored) and writes nothing else.
Other tools: `tier_gear(cls, spec)` returns the page sets ({tier: {gear, ilvl, names, ...}}, the shape of ml_builds.page_gear) and
`gear_path(cls, spec, tier)` the file; `gear_stats(path)` sums a set for the lab (run.py --gear-json, tables.use_gear).
Capacity is the healer lab's model of stated assumptions (heallab/tables.py), not a measurement.
"""
import argparse
import datetime
import json
import math
import os
import pathlib
import re
import sys
import time

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[2]
DATA = ROOT / "_reference" / "data"
for _p in (str(DATA), str(HERE)):
    if _p not in sys.path:
        sys.path.insert(0, _p)

TIERS = ("prebis", "bis")
SETS = DATA / "raidsim" / "gear_sets" / "forever" / "tiers"
RECORD = HERE / "heal-gear.json"
SMOKE_DIR = HERE / "deep-smoke" / "heal-gear"
TODAY = datetime.date.today().isoformat()
LAB_KEYS = ("intellect", "spirit", "healing", "mp5", "crit_gear")
DELTA = {"healing": 50.0, "intellect": 25.0, "spirit": 25.0, "mp5": 8.0, "crit_gear": 0.02}
CRIT_RATING = 14.0   # rating per 1% crit at level 60 (simulator: SpellCritRatingPerCritPercent = PhysicalCritRatingPerCritPercent = 14)
FULL = dict(weight_seeds=800, weight_steps=12, verify_seeds=1000, verify_steps=10, boot=400)
SMOKE = dict(weight_seeds=24, weight_steps=8, verify_seeds=24, verify_steps=8, boot=50)
WEIGHT_SEED0, VERIFY_SEED0 = 1_000_000, 2_000_000   # disjoint from deep_heal.py's seeds and the lab's standard 0..59
SLOTS = ["Head", "Neck", "Shoulder", "Back", "Chest", "Wrist", "Hands", "Waist", "Legs", "Feet", "Finger 1", "Finger 2", "Trinket 1",
         "Trinket 2", "Main hand", "Off hand", "Ranged / relic"]
SLOT_TYPE = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 11, 12, 12, 13, 13, 14]
ARMOR_MAX = {"paladin": 4, "shaman": 3, "druid": 2, "priest": 1}
CLASS_ID = {"paladin": 2, "priest": 5, "shaman": 7, "druid": 11}
# Classic weapon skills (WeaponType: 1 axe, 2 dagger, 3 fist, 4 mace, 6 polearm, 8 staff, 9 sword); off-hands (5) for all, shields (7) for
# paladins and shamans; the ranged slot holds a wand (5) or the class's relic (6 idol, 7 libram, 8 totem)
PROFICIENCY = {"priest": {"one": {2, 4}, "two": {8}, "shield": False, "ranged": 5},
               "druid": {"one": {2, 3, 4}, "two": {4, 8}, "shield": False, "ranged": 6},
               "shaman": {"one": {1, 2, 3, 4}, "two": {1, 4, 8}, "shield": True, "ranged": 8},
               "paladin": {"one": {1, 4, 9}, "two": {1, 4, 6, 9}, "shield": True, "ranged": 7}}


def log(m):
    print(m, flush=True)


# ------------------------------------------------------------------------------------------------ the simulator's item database
_DB = {}


def repo():
    """The simulator's clone: the official wowsims/forever since 2026-10-22 (the port, `_reference/sim-port.md`; the ElliotWood/Forever
    fork's `forever-repo` before), as run.py's default; WOW_FOREVER_SIM overrides."""
    return pathlib.Path(os.environ.get("WOW_FOREVER_SIM", pathlib.Path.home() / ".wow-forever-tools" / "wowsims-forever"))


def _proto_stats():
    """{name: index} of the simulator's Stat enum (proto/common.proto). The official enum (2026-10-22) has one StatCritRating (18) and one
    StatHasteRating (19) for every kind of attack and renumbered Spirit (13) and MP5 (31); the fork's numbers (Spirit 16, MP5 34, spell and
    melee crit 13 and 21) had been written in here."""
    text = (repo() / "proto" / "common.proto").read_text(encoding="utf-8")
    body = re.search(r"enum Stat \{(.*?)\n\}", text, re.S).group(1)
    return {k: int(v) for k, v in re.findall(r"^\s*(Stat\w+)\s*=\s*(\d+);", body, re.M)}


_S = _proto_stats()
STAT_ID = {"intellect": _S["StatIntellect"], "spirit": _S["StatSpirit"], "healing": _S["StatHealingPower"], "mp5": _S["StatMP5"]}
# gear crit: Forever pays it to every kind of attack (one rating in the official enum; the fork's spell and melee ratings both counted)
CRIT_IDS = tuple(_S[k] for k in ("StatCritRating", "StatSpellCritRating", "StatMeleeCritRating") if k in _S)
HASTE_IDS = tuple(_S[k] for k in ("StatHasteRating", "StatSpellHasteRating", "StatMeleeHasteRating") if k in _S)


def sim_db():
    """{"items": {id: item}, "enchants": {effect id: enchant}, "npcs": {id: npc}, "zones": {id: name}} from the simulator's db.json."""
    if not _DB:
        d = json.load(open(repo() / "assets" / "database" / "db.json", encoding="utf-8"))
        _DB["items"] = {i["id"]: i for i in d["items"]}
        _DB["enchants"] = {}
        for e in d["enchants"]:   # one effect id can serve several slots (a bracer and a boots enchant): same stats, other names
            _DB["enchants"].setdefault(e["effectId"], []).append(e)
        _DB["npcs"] = {n["id"]: n for n in d.get("npcs", [])}
        _DB["zones"] = {z["id"]: z["name"] for z in d.get("zones", [])}
    return _DB


def item_stats(it):
    return {int(k): v for k, v in ((it.get("scalingOptions") or {}).get("0") or {}).get("stats", {}).items()}


def enchant_stats(eid):
    e = sim_db()["enchants"].get(eid)
    return {i: v for i, v in enumerate(e[0]["stats"]) if v} if e else {}


def enchant_name(eid, it):
    """The enchant's name for the item's slot (gear_links.DB.enchant's rule: the item type, a two-hander's 2H enchant)."""
    cands = sim_db()["enchants"].get(eid) or []
    fit = [e for e in cands if it.get("type") in [e.get("type"), *(e.get("extraTypes") or [])]] or cands
    fit = [e for e in fit if ("2H" in e.get("name", "")) == (it.get("handType") == 4)] or fit
    return fit[0]["name"] if fit else None


def gear_stats(items):
    """A gear set's summed item and enchant stats in the lab's keys (tables.HEALER_GEAR) plus what the lab ignores (stamina, spell damage,
    haste), for a gear.json path or its item list."""
    if isinstance(items, (str, pathlib.Path)):
        p = pathlib.Path(items)
        items = json.load(open(p if p.is_absolute() else ROOT / p, encoding="utf-8"))["items"]
    tot = {}
    db = sim_db()["items"]
    for x in items:
        if not x or not x.get("id"):
            continue
        for k, v in item_stats(db.get(x["id"], {})).items():
            tot[k] = tot.get(k, 0) + v
        for k, v in enchant_stats(x.get("enchant")).items() if x.get("enchant") else ():
            tot[k] = tot.get(k, 0) + v
    out = {k: tot.get(i, 0) for k, i in STAT_ID.items()}
    out["crit_gear"] = round(sum(tot.get(i, 0) for i in CRIT_IDS) / CRIT_RATING / 100, 6)
    out["ignored"] = {"stamina": tot.get(_S["StatStamina"], 0), "spell_damage": tot.get(_S["StatSpellDamage"], 0),
                      "haste_rating": sum(tot.get(i, 0) for i in HASTE_IDS)}
    return out


def value(stats, w):
    """Capacity an item's (or enchant's) stats add by the weights {lab key: capacity per unit}."""
    v = sum(w.get(k, 0.0) * stats.get(i, 0) for k, i in STAT_ID.items())
    v += w.get("crit_gear", 0.0) / 100 / CRIT_RATING * sum(stats.get(i, 0) for i in CRIT_IDS)
    return v


def source(it):
    """Where an item comes from, in a few words (the first source the database lists)."""
    db = sim_db()
    for s in it.get("sources") or []:
        if "drop" in s:
            x = s["drop"]
            npc = db["npcs"].get(x.get("npcId")) or {}
            zone = db["zones"].get(x.get("zoneId") or npc.get("zoneId"))
            return ", ".join(v for v in (npc.get("name"), zone) if v) or "world drop"
        if "crafted" in s:
            return "crafted"
        if "quest" in s:
            return "quest: " + (s["quest"].get("name") or "?")
        if "soldBy" in s:
            return "sold by " + s["soldBy"].get("npcName", "a vendor")
    return ""


# ------------------------------------------------------------------------------------------------ paths and the API for other tools
def spec_slug(cls, spec):
    import spec_modes as SM
    return SM.spec_slug(cls, spec)


def gear_path(cls, spec, tier, smoke=False):
    """raidsim/gear_sets/forever/tiers/<class>-<spec slug>-<tier>.gear.json (smoke runs: heallab/deep-smoke/heal-gear/)."""
    return (SMOKE_DIR if smoke else SETS) / f"{cls}-{spec_slug(cls, spec)}-{tier}.gear.json"


def tier_gear(cls, spec):
    """The healer spec's page sets: {tier: {"gear": path relative to the project root, "ilvl", "names", "capacity", "build"}} for the
    tiers whose file exists ({} when heal_gear.py has not run for the spec); the shape of raidsim/ml_builds.page_gear's sets."""
    rec = json.load(open(RECORD, encoding="utf-8")) if RECORD.exists() else {}
    r = (rec.get("specs") or {}).get(f"{cls}|{spec}") or {}
    out = {}
    for t in TIERS:
        s = (r.get("sets") or {}).get(t)
        if s and (ROOT / s["gear"]).exists():
            out[t] = {"gear": s["gear"], "ilvl": s.get("ilvl"), "names": s.get("names"), "capacity": (r.get("check") or {}).get(t, {}).get("capacity"),
                      "build": r.get("build")}
    return out


# ------------------------------------------------------------------------------------------------ the build the raid page shows
def raid_pick(cls, spec):
    """(build id, allocation, capacities) of the spec's raid pick: render_modes.rank_builds for healers (the spec's raid healer builds by
    the healer lab's capacity, generated builds last on ties, file order otherwise)."""
    import paths
    import spec_modes as SM
    builds = json.load(open(paths.builds_json("forever", cls), encoding="utf-8"))["builds"]
    ids = {b["id"] for b in builds}
    cap = {}
    d = paths.heallab_dir(cls)
    for f in sorted(d.glob("*.json")) if d.exists() else []:
        if f.name.endswith("-calibration.json"):
            continue
        for bid, r in (json.load(open(f, encoding="utf-8")).get("results") or {}).items():
            if bid in ids:
                cap[bid] = r["capacity"]
    mine = [b for b in builds if b.get("role") == "healer" and SM.mode_of(b) == "raid" and SM.spec_of(cls, b) == spec]
    if not mine:
        raise SystemExit(f"{cls} {spec}: no raid healer build")
    mine.sort(key=lambda b: (-(cap.get(b["id"]) or 0), 1 if b.get("generated") else 0))
    top = mine[0]
    al = {n: r for lst in top["allocation"].values() for n, r in lst if r}
    return top["id"], al, {b["id"]: cap.get(b["id"]) for b in mine}


# ------------------------------------------------------------------------------------------------ measuring in the healer lab
class Lab:
    """Per-seed capacities of one build under several gear dicts, in at most `jobs` processes (heal_worker.seed_caps)."""

    def __init__(self, cls, alloc, jobs):
        import multiprocessing
        import heal_worker as W
        self.cls, self.alloc = cls, alloc
        self.W = W
        self.pool = multiprocessing.get_context("spawn").Pool(jobs, initializer=W.init, initargs=(cls,))
        self.jobs = jobs

    def close(self):
        self.pool.close()
        self.pool.join()

    def caps(self, gears, seeds, steps):
        """{name: [capacity per seed]} for {name: gear dict or None (the lab's assumed gear)}."""
        chunk = max(1, min(25, math.ceil(len(seeds) * len(gears) / (self.jobs * 6))))
        jobs, keys = [], []
        for name, g in gears.items():
            for i in range(0, len(seeds), chunk):
                jobs.append((self.cls, self.alloc, g, seeds[i:i + chunk], steps))
                keys.append(name)
        out = {k: [] for k in gears}
        for k, res in zip(keys, self.pool.map(self.W.seed_caps, jobs, chunksize=1)):
            out[k].extend(res)
        return out


def tail_k(n):
    import tables as T
    return max(1, int(round(2 * T.DEATH_RUNS_OK * n)))


def tail_mean(xs):
    """engine.capacity's statistic: the mean of the worst 2 x DEATH_RUNS_OK of the per-seed capacities."""
    s = sorted(xs)
    k = tail_k(len(s))
    return sum(s[:k]) / k


def boot_tails(caps, B, seed=0):
    """Paired bootstrap: {name: array of B tail means}, every name resampled with the same seed indices."""
    import numpy as np
    n = len(next(iter(caps.values())))
    idx = np.random.default_rng(seed).integers(0, n, size=(B, n))
    k = tail_k(n)
    return {name: np.sort(np.asarray(v)[idx], axis=1)[:, :k].mean(axis=1) for name, v in caps.items()}


def lab_gear(stats):
    return {k: float(stats[k]) for k in LAB_KEYS}


def measure_weights(lab, gear, seeds, steps, B):
    """{stat: {w, se, z, pct_per_unit, hp_eq, hp_eq_se}} at `gear` (the lab keys) and the base capacity: central differences of the tail
    mean on common seeds, bootstrap errors."""
    import numpy as np
    gears = {"base": gear}
    for k, d in DELTA.items():
        gears[f"{k}+"] = dict(gear, **{k: gear[k] + d})
        gears[f"{k}-"] = dict(gear, **{k: max(0.0, gear[k] - d)})
    caps = lab.caps(gears, seeds, steps)
    tails = {k: tail_mean(v) for k, v in caps.items()}
    bt = boot_tails(caps, B)
    out = {}
    wb = {}
    for k in DELTA:
        span = gears[f"{k}+"][k] - gears[f"{k}-"][k]
        w = (tails[f"{k}+"] - tails[f"{k}-"]) / span
        wb[k] = (bt[f"{k}+"] - bt[f"{k}-"]) / span
        se = float(np.std(wb[k], ddof=1))
        out[k] = {"w": w, "se": se, "z": w / se if se else None, "pct_per_unit": 100 * w / tails["base"]}
    for k in DELTA:
        ratio = wb[k] / np.where(wb["healing"] == 0, np.nan, wb["healing"])
        out[k]["hp_eq"] = out[k]["w"] / out["healing"]["w"] if out["healing"]["w"] else None
        out[k]["hp_eq_se"] = float(np.nanstd(ratio, ddof=1))
    return out, tails["base"], float(np.std(bt["base"], ddof=1))


# ------------------------------------------------------------------------------------------------ choosing a set
def admissible(cls, tier, pool):
    """Items of the tier's pool the class can wear, with static stats (gear_opt's class and armor rules; no random suffixes, no
    profession or faction items)."""
    db = sim_db()["items"]

    def ok(it):
        if it.get("type") not in SLOT_TYPE or not pool(it):
            return False
        if it.get("classAllowlist") and CLASS_ID[cls] not in it["classAllowlist"]:
            return False
        if it.get("armorType", 0) > ARMOR_MAX[cls]:
            return False
        if it.get("randomSuffixOptions") or it.get("requiredProfession") or it.get("factionRestriction"):
            return False
        return bool(item_stats(it))
    return [it for it in db.values() if ok(it)]


def best_enchant(cands, w):
    """(effect id, value) of the candidate worth most (None when none adds anything)."""
    scored = [(value(enchant_stats(e), w), e) for e in cands if e in sim_db()["enchants"]]
    scored = [x for x in scored if x[0] > 0]
    if not scored:
        return None, 0.0
    v, e = max(scored)
    return e, v


def choose(cls, items, w):
    """The set worth most by the weights: [17 slot dicts {id, enchant?}] and a note per decision."""
    import fill_enchants as FE
    P = PROFICIENCY[cls]
    C = FE.HEALER_CANDIDATES

    def rank(lst):
        return sorted(lst, key=lambda it: (-value(item_stats(it), w), -((it.get("scalingOptions") or {}).get("0") or {}).get("ilvl", 0), it["id"]))

    by_type = {}
    for it in items:
        by_type.setdefault(it["type"], []).append(it)
    out = [{} for _ in range(17)]
    notes = []
    for slot in range(10):
        r = rank(by_type.get(SLOT_TYPE[slot], []))
        if r:
            out[slot] = {"id": r[0]["id"]}
            e, _ = best_enchant(C.get(slot, []), w)
            if e:
                out[slot]["enchant"] = e
    for slots, t in (((10, 11), 11), ((12, 13), 12)):
        r = [it for it in rank(by_type.get(t, [])) if value(item_stats(it), w) > 0]
        if r:   # two different items, not two of one unique-equip category (the Bronze Dragonflight signets share one)
            sec = [it for it in r[1:] if not (it.get("limitCategory") and it.get("limitCategory") == r[0].get("limitCategory"))]
            for s, it in zip(slots, [r[0]] + sec[:1]):
                out[s] = {"id": it["id"]}
    weapons = by_type.get(13, [])
    one = rank([it for it in weapons if it.get("handType") in (1, 2) and it.get("weaponType") in P["one"]])
    off = rank([it for it in weapons if it.get("handType") == 3 and (it.get("weaponType") == 5 or (P["shield"] and it.get("weaponType") == 7))])
    two = rank([it for it in weapons if it.get("handType") == 4 and it.get("weaponType") in P["two"]])
    e1, v1 = best_enchant(C["1h"], w)
    e2, v2 = best_enchant(C["2h"], w)
    es, vs = best_enchant(C["shield"], w)
    opt_one = None
    if one:
        oh = off[0] if off else None
        ohe, ohv = (es, vs) if oh and oh.get("weaponType") == 7 else (None, 0.0)
        opt_one = (value(item_stats(one[0]), w) + v1 + (value(item_stats(oh), w) + ohv if oh else 0.0), one[0], oh, ohe)
    opt_two = (value(item_stats(two[0]), w) + v2, two[0]) if two else None
    if opt_two and (not opt_one or opt_two[0] > opt_one[0]):
        out[14] = {"id": opt_two[1]["id"], **({"enchant": e2} if e2 else {})}
        notes.append(f"two-hander ({opt_two[0]:.4f}) over main hand + off-hand ({opt_one[0] if opt_one else 0:.4f})")
    elif opt_one:
        out[14] = {"id": opt_one[1]["id"], **({"enchant": e1} if e1 else {})}
        if opt_one[2]:
            out[15] = {"id": opt_one[2]["id"], **({"enchant": opt_one[3]} if opt_one[3] else {})}
        notes.append(f"main hand + off-hand ({opt_one[0]:.4f}) over a two-hander ({opt_two[0] if opt_two else 0:.4f})")
    rel = [it for it in rank(by_type.get(14, [])) if it.get("rangedWeaponType") == P["ranged"] and value(item_stats(it), w) > 0]
    if rel:
        out[16] = {"id": rel[0]["id"]}
    else:
        notes.append("no wand or relic with static healing stats in the pool: ranged slot left empty (relic effects are not modelled)")
    return out, notes


def describe(items):
    db = sim_db()["items"]
    names, ilvls, rows = [], [], []
    for i, x in enumerate(items):
        it = db.get(x.get("id")) if x and x.get("id") else None
        names.append(it["name"] if it else None)
        if it:
            lv = ((it.get("scalingOptions") or {}).get("0") or {}).get("ilvl", 0)
            ilvls.append(lv)
            rows.append({"slot": SLOTS[i], "id": it["id"], "name": it["name"], "ilvl": lv, "source": source(it),
                         "effects": bool(it.get("itemEffects")), "set": it.get("setName"),
                         "enchant": enchant_name(x["enchant"], it) if x.get("enchant") else None})
    return names, round(sum(ilvls) / max(1, len(ilvls)), 1), rows


# ------------------------------------------------------------------------------------------------ one spec
def run_spec(cls, spec, a, B, rec, out_dir):
    import numpy as np
    import tables as T
    t0 = time.time()
    bid, alloc, caps = raid_pick(cls, spec)
    log(f"== {cls} {spec}: raid pick {bid} (healer-lab capacities of the spec's raid builds: "
        + ", ".join(f"{k} {v:.3f}" if v else f"{k} -" for k, v in caps.items()) + ")")
    default = dict(T.HEALER_GEAR[cls])
    wseeds = list(range(WEIGHT_SEED0, WEIGHT_SEED0 + B["weight_seeds"]))
    vseeds = list(range(VERIFY_SEED0, VERIFY_SEED0 + B["verify_seeds"]))
    lab = Lab(cls, alloc, a.jobs)
    try:
        w0, c0, c0se = measure_weights(lab, lab_gear(default), wseeds, B["weight_steps"], B["boot"])
        log("  weights at the lab's assumed gear (capacity per unit; healing-power equivalents): "
            + ", ".join(f"{k} {v['w']:.2e}±{v['se']:.1e} ({v['hp_eq']:.2f})" for k, v in w0.items()))
        weights = {"default": {"gear": lab_gear(default), "capacity": c0, "capacity_se": c0se, "weights": w0}}
        sets = {}
        gs = GT.load_db(repo())
        for tier in TIERS:
            pool = GT.pool_of(tier, gs[1])
            items = admissible(cls, tier, pool)
            wd = {k: v["w"] for k, v in w0.items()}
            s1, n1 = choose(cls, items, wd)
            st1 = gear_stats(s1)
            w1, c1, c1se = measure_weights(lab, lab_gear(st1), wseeds, B["weight_steps"], B["boot"])
            log(f"  {tier}: first set " + ", ".join(f"{k} {st1[k]:g}" for k in LAB_KEYS) + f"; capacity {c1:.4f}; weights there: "
                + ", ".join(f"{k} {v['w']:.2e}±{v['se']:.1e}" for k, v in w1.items()))
            s2, n2 = choose(cls, items, {k: v["w"] for k, v in w1.items()})
            race = None
            chosen, notes = s1, n1
            if s2 != s1:
                st2 = gear_stats(s2)
                rc = lab.caps({"first": lab_gear(st1), "refreshed": lab_gear(st2)}, vseeds, B["verify_steps"])
                bt = boot_tails(rc, B["boot"], seed=1)
                ratio = tail_mean(rc["refreshed"]) / tail_mean(rc["first"])
                race = {"first": tail_mean(rc["first"]), "refreshed": tail_mean(rc["refreshed"]), "ratio": ratio,
                        "ratio_se": float(np.std(bt["refreshed"] / bt["first"], ddof=1))}
                if ratio > 1.0:
                    chosen, notes = s2, n2
                log(f"  {tier}: refreshed set differs ({sum(1 for x, y in zip(s1, s2) if x != y)} slots): ratio {ratio:.4f}±{race['ratio_se']:.4f} -> "
                    + ("refreshed" if chosen is s2 else "first"))
            else:
                log(f"  {tier}: the refreshed weights choose the same set")
            names, ilvl, rows = describe(chosen)
            p = out_dir / f"{cls}-{spec_slug(cls, spec)}-{tier}.gear.json"
            p.parent.mkdir(parents=True, exist_ok=True)
            p.write_text(json.dumps({"items": chosen}, indent=1) + "\n", encoding="utf-8")
            weights[tier] = {"gear": lab_gear(st1), "capacity": c1, "capacity_se": c1se, "weights": w1}
            sets[tier] = {"gear": p.relative_to(ROOT).as_posix(), "items": chosen, "names": names, "ilvl": ilvl, "rows": rows,
                          "stats": gear_stats(chosen), "notes": notes, "refresh_race": race, "pool_items": len(items)}
            log(f"  {tier}: wrote {p.relative_to(ROOT).as_posix()} (item level {ilvl}): " + "; ".join(n for n in names if n))
        # the check: the build in the lab's assumed gear and in both sets, on fresh seeds and on the lab's standard seeds
        gears = {"default": lab_gear(default), **{t: lab_gear(sets[t]["stats"]) for t in TIERS}}
        vc = lab.caps(gears, vseeds, B["verify_steps"])
        bt = boot_tails(vc, B["boot"], seed=2)
        std = lab.caps(gears, list(range(60)), 10) if not a.smoke else {k: [0.0] for k in gears}
        check = {}
        for k in gears:
            check[k] = {"capacity": tail_mean(vc[k]), "capacity_se": float(np.std(bt[k], ddof=1)), "vs_default": tail_mean(vc[k]) / tail_mean(vc["default"]),
                        "vs_default_se": float(np.std(bt[k] / bt["default"], ddof=1)), "standard_seeds": tail_mean(std[k]), "stats": gears[k]}
            log(f"  check {k:<8} capacity {check[k]['capacity']:.4f}±{check[k]['capacity_se']:.4f}  x{check[k]['vs_default']:.3f}±{check[k]['vs_default_se']:.3f} "
                f"vs assumed gear; standard seeds {check[k]['standard_seeds']:.3f}")
    finally:
        lab.close()
    rec.setdefault("specs", {})[f"{cls}|{spec}"] = {
        "class": cls, "spec": spec, "slug": spec_slug(cls, spec), "build": bid, "build_reason": "the raid page's pick: the spec's raid healer "
        "builds ranked by healer-lab capacity (render_modes.rank_builds)", "capacities_of_spec_builds": caps, "date": TODAY,
        "budgets": B, "weights": weights, "sets": sets, "check": check, "seconds": round(time.time() - t0)}
    log(f"  {cls} {spec} done in {time.time() - t0:.0f}s")


# ------------------------------------------------------------------------------------------------ report
def fmt_w(v):
    return f"{v['w'] * 1000:.4f} ± {v['se'] * 1000:.4f}"


def render(cls, rec):
    import tables as T
    specs = [r for r in rec["specs"].values() if r["class"] == cls]
    o = [f"# Healer gear — {cls}", "",
         f"> Generated by `_reference/data/heallab/heal_gear.py` on {max(r['date'] for r in specs)}. Healers are in no community simulator, so "
         "the stat weights come from this project's healer lab (a model of stated assumptions, `heallab/tables.py`, not a measurement): the "
         "capacity (the raid damage multiplier the build heals through in 90% of runs) gained per point of each gear stat, measured by moving "
         "the lab's assumed gear stats up and down on common random seeds, errors by a paired bootstrap. Items from the community "
         "simulator's item database in the damage tiers' pools (`raidsim/gear_tiers.py`: pre-BiS = no raid drops; BiS = phase 1: dungeons, "
         "Molten Core, Onyxia, world, crafted, quest), best item per slot by the weights, healer enchants from `raidsim/fill_enchants.py`. "
         "Not valued: set bonuses, on-use and proc effects (most healing trinkets and relics count only their static stats), Stamina "
         "(the lab never damages the healer), haste. Do not hand-edit.", ""]
    for r in specs:
        o += [f"## {r['spec']} (`{r['build']}`)", "",
              f"The build is the raid page's pick (healer-lab capacity {max(v for v in r['capacities_of_spec_builds'].values() if v):.3f} in the lab's assumed gear).", "",
              "### Stat weights", "",
              "Capacity per point of gear stat x 1000 (± standard error); in brackets the healing-power equivalent (weight / healing weight). "
              f"Crit is per 1% ({CRIT_RATING:g} rating). {r['budgets']['weight_seeds']} seeds, {r['budgets']['weight_steps']} bisection steps per point.", "",
              "| Gear | Healing | Intellect | Spirit | mp5 | Crit (per 1%) | Capacity |", "|---|---|---|---|---|---|---|"]
        for k, lab in (("default", "the lab's assumed gear"), ("prebis", "the first pre-BiS set"), ("bis", "the first BiS set")):
            x = r["weights"].get(k)
            if not x:
                continue
            ww = x["weights"]
            crit = {"w": ww["crit_gear"]["w"] / 100, "se": ww["crit_gear"]["se"] / 100}
            cells = [f"{fmt_w(ww[s])} ({ww[s]['hp_eq']:.2f})" for s in ("healing", "intellect", "spirit", "mp5")]
            cells.append(f"{fmt_w(crit)} ({ww['crit_gear']['hp_eq'] / 100:.2f})")
            o.append(f"| {lab} | " + " | ".join(cells) + f" | {x['capacity']:.3f} |")
        o += ["", "### Sets", "", "| Tier | Capacity | vs the lab's assumed gear | Healing | Intellect | Spirit | mp5 | Crit | Item level |", "|---|---|---|---|---|---|---|---|---|"]
        for k, lab in (("default", "the lab's assumed gear"), ("prebis", "pre-BiS"), ("bis", "BiS (phase 1)")):
            c = r["check"][k]
            st = c["stats"]
            il = r["sets"][k]["ilvl"] if k in r["sets"] else "-"
            o.append(f"| {lab} | {c['capacity']:.3f} ± {c['capacity_se']:.3f} | x{c['vs_default']:.3f} ± {c['vs_default_se']:.3f} | {st['healing']:g} | "
                     f"{st['intellect']:g} | {st['spirit']:g} | {st['mp5']:g} | {st['crit_gear'] * 100:.1f}% | {il} |")
        o += ["", f"Capacities on {r['budgets']['verify_seeds']} fresh seeds (common to the three rows); the lab's standard 60 seeds (the "
              "pages' convention): " + ", ".join(f"{k} {v['standard_seeds']:.3f}" for k, v in r["check"].items()) + ".", ""]
        for t in TIERS:
            s = r["sets"][t]
            o += [f"#### {'Pre-BiS' if t == 'prebis' else 'BiS (phase 1)'}: `{s['gear']}`", "", "| Slot | Item | Item level | Source | Enchant |", "|---|---|---|---|---|"]
            for row in s["rows"]:
                tag = (" (effect not valued)" if row["effects"] else "") + (f" ({row['set']}: set bonus not valued)" if row["set"] else "")
                o.append(f"| {row['slot']} | [{row['name']}](https://www.wowhead.com/forever/item={row['id']}){tag} | {row['ilvl']} | {row['source'] or '-'} | {row['enchant'] or '-'} |")
            ign = s["stats"]["ignored"]
            o += ["", f"Not valued by the lab: Stamina {ign['stamina']:g}, spell damage without healing {ign['spell_damage']:g}, haste rating {ign['haste_rating']:g}."
                  + ("" if not s["notes"] else " " + "; ".join(n[0].upper() + n[1:] for n in s["notes"]) + "."), ""]
            if s.get("refresh_race"):
                rr = s["refresh_race"]
                o += [f"Weights refreshed at the first set's stats chose a different set: refreshed / first = {rr['ratio']:.4f} ± {rr['ratio_se']:.4f} "
                      f"(the better one is kept).", ""]
    o += ["## Assumptions", "",
          f"- The lab's assumed gear (tables.HEALER_GEAR, {cls}): " + ", ".join(f"{k} {v:g}" for k, v in T.HEALER_GEAR[cls].items()) + "; raid buffs, Kings and "
          "talents on top (engine.Healer.setup_stats), as for every lab report.",
          "- Perturbations: " + ", ".join(f"{k} ±{v:g}" for k, v in DELTA.items()) + "; weights are local slopes, refreshed once at the chosen set.",
          "- Item stats are the database's level-60 scaling; generic crit rating counts for heals (Forever pays gear crit to every attack, "
          "sim/core/forever_rules.go); spell damage without healing power heals for nothing (the simulator's HealingPower stat).",
          "- Weapon skills are Classic's (`PROFICIENCY`); items needing a profession or a faction are left out; rings and trinkets are two "
          "different items, not of one unique-equip category.", "", "_Generated by `_reference/data/heallab/heal_gear.py`. Do not hand-edit._", ""]
    return "\n".join(o)


GT = None


def main():
    global GT
    import importlib.util
    import spec_modes as SM
    import tables  # noqa: F401  the healer lab's modules first: the raid tools below put other directories ahead on sys.path
    import heal_worker  # noqa: F401
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("classes", nargs="*", default=[])
    ap.add_argument("--spec", action="append", help="one healer spec (repeatable; default: every healer spec of the classes)")
    ap.add_argument("--fresh", action="store_true", help="redo specs the record already has")
    ap.add_argument("--jobs", type=int, default=6)
    ap.add_argument("--smoke", action="store_true", help="tiny budgets; sets, record and reports under heallab/deep-smoke/heal-gear/")
    a = ap.parse_args()
    a.jobs = max(1, min(a.jobs, 6))   # the CPU is shared with the fight lab's runs (2026-10-15)
    s = importlib.util.spec_from_file_location("gear_tiers", DATA / "raidsim" / "gear_tiers.py")
    GT = importlib.util.module_from_spec(s)
    s.loader.exec_module(GT)
    sys.path.insert(0, str(DATA / "raidsim"))   # fill_enchants
    B = SMOKE if a.smoke else FULL
    out_dir = SMOKE_DIR if a.smoke else SETS
    rec_path = SMOKE_DIR / "heal-gear.json" if a.smoke else RECORD
    rec = json.load(open(rec_path, encoding="utf-8")) if rec_path.exists() else {}
    classes = a.classes or [c for c in ("priest", "paladin", "druid", "shaman")]
    t0 = time.time()
    for cls in classes:
        for spec in a.spec or SM.HEAL_TREES[cls]:
            if spec not in SM.HEAL_TREES[cls]:
                raise SystemExit(f"{cls} has no healer spec {spec!r}")
            if f"{cls}|{spec}" in rec.get("specs", {}) and not a.fresh:
                log(f"{cls} {spec}: in the record (--fresh redoes)")
                continue
            run_spec(cls, spec, a, B, rec, out_dir)
            rec.update({"date": TODAY, "tool": "_reference/data/heallab/heal_gear.py", "deltas": DELTA, "crit_rating_per_percent": CRIT_RATING,
                        "note": "capacity is the healer lab's model of stated assumptions (heallab/tables.py), not a measurement"})
            rec_path.parent.mkdir(parents=True, exist_ok=True)
            rec_path.write_text(json.dumps(rec, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
        if any(r["class"] == cls for r in rec.get("specs", {}).values()):
            import paths
            p = (SMOKE_DIR / f"{cls}-gear.md") if a.smoke else paths.heallab_dir(cls) / "gear.md"
            p.parent.mkdir(parents=True, exist_ok=True)
            p.write_text(render(cls, rec), encoding="utf-8")
            log(f"wrote {p.relative_to(ROOT).as_posix()}")
    log(f"done in {time.time() - t0:.0f}s")


if __name__ == "__main__":
    main()
