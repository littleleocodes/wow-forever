"""Pre-BiS and phase-1 BiS gear for the raid tanks (2026-10-15, user decision 2026-10-14: tanks get real pre-BiS and BiS sets "chosen in
the simulator like the damage specs").

    python -u _reference/data/raidsim/tank_gear.py [warrior paladin druid] [--tiers prebis,bis] [--smoke]

The damage specs' tool (gear_tiers.py) with the tank's measure. Per tank entry of specs.json (warrior and paladin `prot-tank`, druid
`feral-bear-tank`) and tier:
- Pools and filters: gear_tiers.py's (`pool_of`: the prebis and bis rules; class, armor and weapon-type fits, unique items, set pieces,
  relics kept; gear_tiers.optimize_set runs the steps). The standard set is put in the simulator's slot order first (the warrior's and
  the bear's launch presets list the ranged weapon or the idol before the weapons; the simulator equips by item type, the greedy step
  goes by slot).
- Build: the tank's raid page pick (the entry's tank build of ours with the best tank value in the last race, `<entry>.json`; ties go to
  the first listed): warrior opt-prot-tank-raid-tank, paladin protection-ml-tank, druid feral-bear-tank on 2026-10-15.
- Setting: the entry's own (the raid: boss melee, every raid buff; the entry's raid rotation, `run.apl_path(entry, repo, "raid")`).
- Score: run.tank_value (the raid-tank profile's weights on threat per second and on damage avoided) against deep_tank.py's reference
  (the entry's hand draft over 20,000 fights in the standard set, `raidsim/deep/<class>-tank.json`), so every set sits on the tank's one
  scale (1.000 = the hand draft in the standard set).
- Stat weights: the bench's `statweights` mode returns, for a tank config (`isTank`), the simulator's threat per point (`weights`, every
  stat plus weapon DPS) and damage taken per point (`dtps_weights`). Tank value TV = tw T / T_ref + mw D_ref / D, so per point
  dTV = tw / T_ref (dT - (mw / tw) T_ref D_ref / D^2 dD), D the pick's damage taken in the set being weighed (a run next to the weights).
  The weights are kept in threat-per-second equivalents (dT - k dD, k = (mw / tw) T_ref D_ref / D^2): the same order as dTV, readable.
  Stamina and health weigh 0: tank value has no term for them (the simulator's damage taken does not depend on health). The simulator's
  stat weights drop a stat whose runs leave DPS, HPS and TMI unchanged (a hard-cap check; TMI reads 0 in these runs), so armor came back
  at 0 for the warrior and the bear although it lowers damage taken: defensive stats the weights return at 0 are measured by central
  differences on bonus_stats (`FD_STATS`, recorded as `finite_differences`).
- Enchants: fill_enchants.py's tank templates (`tank-plate`, `tank-bear`) fill empty slots before and after the search; then each slot
  takes the `TANK_CANDIDATES` enchant worth most by the final weights (ties keep the template's), and the weapon enchants (no stats to
  weigh: Crusader, +9 weapon damage, +30 spell power) are raced on seed 1 and confirmed on seed 2 against the template's.
- The record compares the pick in each tier set with the entry's standard set (as the races use it: no enchants) on a fresh seed.
- `--armor`: the same search with the base armor the fork's item database lacks filled in from Classic (see ClassicArmor), written as
  `*-classic-armor` sets and the record's `classic_armor` key: a sensitivity, not the simulator's model. Obsolete since the port to
  wowsims/forever (2026-10-22): the official database gives armor from the client's tables (5,884 of 6,151 armor items); the
  `*-classic-armor` sets were removed then (they held items the official database lacks).
- Reference (2026-10-22): deep_tank.py's reference build measured again on the current simulator in the entry's standard set
  (`reference`; the deep record's own numbers are the fork's, kept as `reference_fork`).
Sets `gear_sets/forever/tiers/<class>-<slug>-<tier>.gear.json` (warrior-protection, paladin-protection, druid-feral-combat-tank: the
bear shares the Feral Combat page, whose cat sets hold `druid-feral-combat-<tier>`); record `raidsim/tank-gear.json`. `tier_gear(cls, spec,
tier)` gives a tank's set path for the pages. The simulator's model of the beta (wowsims/forever since 2026-10-22, ElliotWood/Forever
before; the pinned commit with this project's patches), not in-game measurements; it models no threat from other players, taunts or tank swaps, and no tank death.
"""
import argparse
import csv
import datetime
import importlib.util
import json
import pathlib
import sys
import time

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[2]
sys.path[:0] = [str(ROOT / "_reference/data"), str(HERE)]
import paths  # noqa: E402
import spec_modes as SM  # noqa: E402

TANK_ENTRY = {"warrior": "prot-tank", "paladin": "prot-tank", "druid": "feral-bear-tank"}
FILE_SLUG = {"warrior": "protection", "paladin": "protection", "druid": "feral-combat-tank"}
TIERS = ("prebis", "bis")
SETS = HERE / "gear_sets" / "forever" / "tiers"
RECORD = HERE / "tank-gear.json"
SMOKE_DIR = HERE / "deep-smoke" / "tank-gear"   # git-ignored
TODAY = datetime.date.today().isoformat()
STAT_NAMES = []   # the simulator's Stat enum, index -> name (main() reads it from the clone's proto/common.proto: gear_opt.stat_names; an
# enchant's stats array is aligned with it). The fork's numbering had been written in here until the port to wowsims/forever (2026-10-22).
# defensive stats measured by central differences when the simulator's weights return 0 for them (TankWeights): stat -> step (the
# simulator's own steps: 100 for armor, 10 otherwise)
FD_STATS = {"StatArmor": 100, "StatBonusArmor": 100, "StatDefenseRating": 10, "StatDodgeRating": 10, "StatParryRating": 10,
            "StatBlockRating": 10, "StatBlockValue": 10, "StatAgility": 10}


def set_path(cls, tier, smoke=False, armor=False):
    return (SMOKE_DIR if smoke else SETS) / f"{cls}-{FILE_SLUG[cls]}-{tier}{'-classic-armor' if armor else ''}.gear.json"


def tier_gear(cls, spec, tier, armor=False):
    """The tank's set for a tier (absolute path), or None: `spec` the tank page's spec (spec_modes.TANK_TREE: Protection, Feral Combat),
    `tier` prebis or bis; `armor=True` the sensitivity set chosen with Classic base armor filled in (`--armor`). For gear_links.py /
    render_modes.py."""
    if cls not in TANK_ENTRY or SM.TANK_TREE.get(cls) != spec or tier not in TIERS:
        return None
    p = set_path(cls, tier, armor=armor)
    return p if p.exists() else None


# ------------------------------------------------------------------------------------------------ the armor sensitivity (--armor)
# The fork's item database (2ce8265) lists base armor (stat 31) for about one armor item in five (1,338 of 7,277: Legplates of Wrath 749,
# Draconian Deflector 2153; none for Lionheart Helm, the PvP and Forever items, most dungeon pieces), and the simulator gives an item no
# armor it does not list (database.go NewItem). Every tank number of the project carries that gap, and a set chosen in it favours the
# items that list armor. `--armor` fills the gap for this tool only: an item that lists no armor gets its Classic 1.12 armor (cmangos
# classic-db dump, raw/2026-09-26-cmangos-classic-db-z2815/item_stats.csv, by item id), or for ids not in that dump (Forever's new
# items) a linear fit of Classic armor on item level per slot, armor type and quality; the sum goes into each run as bonus armor and
# into the greedy step's item values. Our assumption (Forever may have changed armor), a sensitivity next to the simulator's own sets.
CLASSIC_ITEMS = ROOT / "_reference/data/raw/2026-09-26-cmangos-classic-db-z2815/item_stats.csv"
INV = {1: 1, 3: 3, 4: 16, 5: 5, 6: 9, 7: 10, 8: 6, 9: 7, 10: 8}   # the simulator's ItemType -> Classic InventoryType (robes count as chests)


class ClassicArmor:
    def __init__(self):
        self.by_id, pts = {}, {}
        for r in csv.DictReader(open(CLASSIC_ITEMS, encoding="utf-8")):
            if r["class"] != "4":
                continue
            arm = int(r["armor"])
            self.by_id[int(r["entry"])] = arm
            inv = 5 if r["InventoryType"] == "20" else int(r["InventoryType"])
            if arm > 0:
                pts.setdefault((inv, int(r["subclass"]), int(r["Quality"])), []).append((int(r["ItemLevel"]), arm))
        self.fit = {}
        for k, v in pts.items():
            if len(v) >= 5:
                n = len(v)
                mx, my = sum(x for x, _ in v) / n, sum(y for _, y in v) / n
                sxx = sum((x - mx) ** 2 for x, _ in v)
                b = sum((x - mx) * (y - my) for x, y in v) / sxx if sxx else 0.0
                self.fit[k] = (my - b * mx, b)
        self.cache = {}

    def key(self, it):
        if it.get("type") == 13 and it.get("weaponType") == 7:
            return (14, 6, it.get("quality", 0))
        if it.get("type") in INV and it.get("armorType") in (1, 2, 3, 4):
            return (INV[it["type"]], it["armorType"], it.get("quality", 0))
        return None

    def missing(self, it):
        """The armor the database lacks for an item: 0 when it lists armor or is not armor."""
        i = it["id"]
        if i not in self.cache:
            so = it.get("scalingOptions", {}).get("0", {})
            st = so.get("stats", {})
            k = self.key(it)
            v = 0
            if k and str(STAT_NAMES.index("StatArmor")) not in st and str(STAT_NAMES.index("StatBonusArmor")) not in st:
                if i in self.by_id:
                    v = self.by_id[i]
                elif k in self.fit:
                    a0, b = self.fit[k]
                    v = max(0, round(a0 + b * so.get("ilvl", 0)))
            self.cache[i] = v
        return self.cache[i]


def install_armor(db):
    """Patch this process's gear_opt.run_bench and gear_opt.value (gear_tiers' greedy step calls them) to add the missing armor."""
    ca = ClassicArmor()
    run0, value0 = G.run_bench, G.value

    def run_bench(repo, cfg, tag):
        for b in cfg.get("builds", []):
            items = (b.get("gear_json") or {}).get("items")
            if items is None:
                raise SystemExit("--armor: every run needs its gear list (gear_json)")
            add = sum(ca.missing(db[x["id"]]) for x in items if x and x.get("id") in db)
            if add:
                bs = dict(b.get("bonus_stats") or {})
                bs["StatBonusArmor"] = bs.get("StatBonusArmor", 0) + add
                b["bonus_stats"] = bs
        return run0(repo, cfg, tag)

    def value(it, w, slot):
        return value0(it, w, slot) + w.get("StatBonusArmor", 0.0) * ca.missing(it)
    G.run_bench, G.value = run_bench, value
    global ARMOR
    ARMOR = ca
    return ca


ARMOR = None   # the ClassicArmor of an --armor run


def log(m):
    print(m, flush=True)


def _load(name, path):
    s = importlib.util.spec_from_file_location(name, path)
    m = importlib.util.module_from_spec(s)
    s.loader.exec_module(m)
    return m


def page_pick(cls, entry, builds):
    """The tank page's pick: the entry's tank build of ours with the best tank value in its last race (ties: the first listed)."""
    rows = json.load(open(paths.raidsim_dir(cls) / f"{entry}.json", encoding="utf-8"))["results"]
    val = {r["label"]: r.get("value") or 0 for r in rows}
    ours = [b for b in R.SPECS[cls][entry]["builds"] if b in builds and builds[b].get("role") == "tank" and b in val]
    return max(ours, key=lambda b: (val[b], -ours.index(b)))


def normalize(items, db):
    """A gear list in the simulator's ItemSlot order (0-13 as listed; main hand 14, off hand or shield 15, ranged or relic 16)."""
    items = [dict(x) if x else {} for x in items] + [{}] * max(0, 17 - len(items))
    out = items[:14] + [{}, {}, {}]
    for x in items[14:]:
        # an item the official database lacks keeps its place by the fork's record of it (gear_opt.legacy_item, 2026-10-22), so the
        # greedy step re-fills the slot with the same weapon setup
        it = (db.get(x.get("id")) or G.legacy_item(x.get("id"))) if x.get("id") else None
        if not it:
            continue
        if it.get("type") == 14:
            out[16] = x
        elif it.get("handType") == 3 or it.get("weaponType") == 7 or out[14]:
            out[15] = x
        else:
            out[14] = x
    for i in range(14):
        it = db.get(out[i].get("id")) if out[i].get("id") else None
        if it and it.get("type") != G.SLOT_TYPE[i]:
            raise SystemExit(f"slot {i} holds {it['name']} (item type {it.get('type')}): not a gear list in slot order")
    return out


def bench_rows(entry, repo, builds, its, seed, tag):
    return G.run_bench(repo, G.bench_cfg(entry, repo, builds, its, seed, "raid"), tag)


def measure(entry, repo, talents, items, its, seed, ref, tag):
    """Tank value, threat and damage taken per second of a build in a set (None: the entry's standard set as specs.json names it)."""
    b = {"label": "m", "talents": talents}
    if items is not None:
        b["gear_json"] = {"items": items}
    r = bench_rows(entry, repo, [b], its, seed, tag)["m"]
    if r.get("error"):
        raise SystemExit(f"run failed: {r['error']}")
    return {"value": round(R.tank_value(r, ref), 4), "threat": round(r["threat"], 1), "dtps": round(r["dtps"], 1), "dps": round(r["dps"], 1),
            "tmi": round(r.get("tmi") or 0, 2), "fights": its, "seed": seed}


def gear_stats(items, db, enchants):
    """Stamina, armor and the avoidance ratings of a set (items plus enchants; for the record: tank value gives Stamina no weight)."""
    tot = {}
    for x in items:
        it = db.get(x.get("id")) if x and x.get("id") else None
        if not it:
            continue
        for k, v in it.get("scalingOptions", {}).get("0", {}).get("stats", {}).items():
            tot[int(k)] = tot.get(int(k), 0) + v
        e = enchants.get(x.get("enchant"))
        if e:
            for i, v in enumerate(e[0]["stats"][:len(STAT_NAMES)]):
                tot[i] = tot.get(i, 0) + v
    keep = {"StatStamina", "StatStrength", "StatAgility", "StatArmor", "StatBonusArmor", "StatDefenseRating", "StatDodgeRating",
            "StatParryRating", "StatBlockRating", "StatBlockValue", "StatHitRating", "StatExpertiseRating"}
    out = {STAT_NAMES[i]: round(v, 1) for i, v in sorted(tot.items()) if i < len(STAT_NAMES) and STAT_NAMES[i] in keep and v}
    if ARMOR:   # --armor: the Classic base armor filled in for items that list none
        out["armor_filled_in"] = sum(ARMOR.missing(db[x["id"]]) for x in items if x and x.get("id") in db)
    return out


class TankWeights:
    """weights_fn for gear_tiers.optimize_set: the bench's threat and damage-taken weights combined into threat-per-second equivalents
    of tank value (see the module notes); the raw weights of the last call are kept for the record."""

    def __init__(self, entry, repo, talents, ref, its, tag):
        self.entry, self.repo, self.talents, self.ref, self.its, self.tag = entry, repo, talents, ref, its, tag
        self.tw, self.mw = R.tank_weights()
        self.last = None

    def __call__(self, items):
        b = [{"label": "w", "talents": self.talents, "gear_json": {"items": items}}]
        row = G.run_bench(self.repo, G.bench_cfg(self.entry, self.repo, b, self.its, 1, "raid", statweights=True), f"w-{self.tag}")["w"]
        if row.get("error"):
            raise SystemExit(f"stat weights failed for {self.tag}: {row['error']}")
        wt, wd = dict(row["weights"]), dict(row.get("dtps_weights") or {})
        # the simulator's stat weights skip a stat whose runs leave DPS, HPS and TMI unchanged (its hard-cap check); TMI reads 0 in our
        # tank runs, so a stat that only lowers damage taken (armor: 1,000 armor took a warrior's damage taken 641.7 -> 585.6 per second,
        # DPS and threat unchanged, 2026-10-15) came back at 0. Those defensive stats are measured here by central differences instead
        # (bonus_stats; the same seed, so the runs share their rolls).
        miss = [s for s, m in FD_STATS.items() if abs(wt.get(s, 0.0)) < 1e-12 and abs(wd.get(s, 0.0)) < 1e-12]
        fd = [dict(b[0], label="b")] + [dict(b[0], label=f"{s}{sg}", bonus_stats={s: sg * m}) for s, m in FD_STATS.items() if s in miss
                                        for sg in (1, -1)]
        rows = bench_rows(self.entry, self.repo, fd, self.its, 1, f"b-{self.tag}")
        base = rows["b"]
        for s in miss:
            hi, lo, m = rows[f"{s}1"], rows[f"{s}-1"], FD_STATS[s]
            wt[s] = (hi["threat"] - lo["threat"]) / (2 * m)
            wd[s] = (hi["dtps"] - lo["dtps"]) / (2 * m)
        d = base["dtps"]
        k = (self.mw / self.tw) * self.ref["threat"] * self.ref["dtps"] / d ** 2
        comb = {s: wt.get(s, 0.0) - k * wd.get(s, 0.0) for s in set(wt) | set(wd)}
        self.last = {"k": round(k, 5), "dtps": round(d, 1), "threat": round(base["threat"], 1), "finite_differences": miss,
                     "tps_per_point": {s: round(v, 5) for s, v in wt.items() if abs(v) > 1e-6},
                     "dtps_per_point": {s: round(v, 5) for s, v in wd.items() if abs(v) > 1e-6}}
        return comb


def enchant_db(repo):
    return G.enchant_db(repo)


def reference(cls, e, repo, builds, fork_ref, a):
    """The tank-value reference measured on the current simulator: deep_tank.py's reference build (the entry's hand draft) in the entry's
    standard set, deep_tank's 20,000 fights and seed 77, raid setting. Since the port to wowsims/forever (2026-10-22) the deep record's own
    reference (`raidsim/deep/<class>-tank.json`) is the fork's numbers, so the tank values of this record sit on this one instead."""
    hand = fork_ref["build"]
    talents = R.talents_string(R.load_trees(repo, cls), R.alloc_of(builds[hand]))
    r = bench_rows(e, repo, [{"label": "ref", "talents": talents}], a.ref_fights, 77, f"ref-{cls}")["ref"]
    if r.get("error"):
        raise SystemExit(f"reference run failed: {r['error']}")
    return {"build": hand, "threat": r["threat"], "dtps": r["dtps"], "fights": a.ref_fights, "seed": 77, "gear": e["gear"],
            "simulator": f"wowsims/forever {R.git_commit(repo)}", "missing_gear": r.get("missing_gear", [])}


def ench_value(entries, w):
    st = entries[0]["stats"][:len(STAT_NAMES)]
    return sum(w.get(STAT_NAMES[i], 0.0) * v for i, v in enumerate(st))


def choose_enchants(items, w, db, edb):
    """Each stat slot's TANK_CANDIDATES enchant worth most by the weights (the template's, listed first, wins ties). Returns the changes."""
    changes = {}
    for slot, cands in FE.TANK_CANDIDATES.items():
        if not isinstance(slot, int) or not items[slot].get("id"):
            continue
        cands = [c for c in cands if c in edb]
        if not cands:
            continue
        vals = [(ench_value(edb[c], w), -i, c) for i, c in enumerate(cands)]
        best = max(vals)[2]
        if abs(max(vals)[0] - vals[0][0]) < 1e-9:
            best = cands[0]
        if items[slot].get("enchant") != best:
            changes[slot] = (items[slot].get("enchant"), best)
            items[slot]["enchant"] = best
    sh = items[15]
    it = db.get(sh.get("id")) if sh.get("id") else None
    if it and it.get("weaponType") == 7:
        cands = [c for c in FE.TANK_CANDIDATES["shield"] if c in edb]
        vals = [(ench_value(edb[c], w), -i, c) for i, c in enumerate(cands)]
        best = cands[0] if abs(max(vals)[0] - vals[0][0]) < 1e-9 else max(vals)[2]
        if sh.get("enchant") != best:
            changes[15] = (sh.get("enchant"), best)
            sh["enchant"] = best
    return changes


def race_weapon_enchant(entry, repo, talents, items, db, ref, a, tag):
    """The main hand's enchant: the candidates raced on seed 1, the leader confirmed against the current one on seed 2."""
    it = db.get(items[14].get("id")) if items[14].get("id") else None
    if not it:
        return None
    cands = FE.TANK_CANDIDATES["2h" if it.get("handType") == 4 else "1h"]
    cur = items[14].get("enchant") or cands[0]
    sets = {}
    for c in dict.fromkeys([cur] + cands):
        x = [dict(i) for i in items]
        x[14]["enchant"] = c
        sets[c] = x

    def race(keys, its, seed):
        rows = bench_rows(entry, repo, [{"label": str(k), "talents": talents, "gear_json": {"items": sets[k]}} for k in keys], its, seed, f"e-{tag}")
        return {k: R.tank_value(rows[str(k)], ref) or 0 for k in keys}
    r1 = race(list(sets), a.iterations, 1)
    lead = max(r1, key=r1.get)
    r2 = race([cur, lead], a.confirm, 2) if lead != cur else {cur: r1[cur]}
    pick = lead if lead != cur and r2[lead] > r2[cur] else cur
    items[14]["enchant"] = pick
    return {"candidates": list(sets), "race_seed1": {str(k): round(v, 4) for k, v in r1.items()},
            "confirm_seed2": {str(k): round(v, 4) for k, v in r2.items()}, "chosen": pick}


def run_class(cls, tiers, repo, db, zones, edb, a, rec):
    entry_name = TANK_ENTRY[cls]
    e = R.SPECS[cls][entry_name]
    builds = {b["id"]: b for b in json.load(open(paths.builds_json("forever", cls), encoding="utf-8"))["builds"]}
    pick = a.build.get(cls) or page_pick(cls, entry_name, builds)
    talents = R.talents_string(R.load_trees(repo, cls), R.alloc_of(builds[pick]))
    deep = json.load(open(HERE / "deep" / f"{cls}-tank.json", encoding="utf-8"))
    out0 = rec.setdefault(cls, {})
    sim = f"wowsims/forever {R.git_commit(repo)}"
    if (out0.get("reference") or {}).get("simulator") != sim or (out0.get("reference") or {}).get("gear") != e["gear"] or a.fresh_standard:
        out0["reference"] = reference(cls, e, repo, builds, deep["ref"], a)
        out0.pop("standard", None)   # the standard set is measured again on the new reference
    ref = out0["reference"]
    std_path = R.sim_path(e["gear"])
    std_path = pathlib.Path(std_path) if pathlib.Path(std_path).is_absolute() else repo / e["gear"]
    std = normalize(json.load(open(std_path, encoding="utf-8"))["items"], db)
    t0 = time.time()
    out = rec.setdefault(cls, {})
    if a.armor:
        out = out.setdefault("classic_armor", {})
        out["note"] = ("sensitivity: every item's missing base armor filled in from Classic 1.12 (see tank_gear.py); tank value on the same "
                       "reference as the simulator's sets, so the standard set's value here includes its filled-in armor")
    out.update({"entry": entry_name, "build": pick, "setting": "raid", "rotation": R.apl_label(e, repo, "raid"),
                "reference_fork": dict(deep["ref"], source=f"raidsim/deep/{cls}-tank.json (ElliotWood/Forever)"), "standard_gear": e["gear"]})
    if not a.armor:
        out["reference"] = ref
    log(f"== {cls} {entry_name}: {pick}; reference {ref['build']} (threat {ref['threat']:.1f}/s, damage taken {ref['dtps']:.1f}/s)")
    if "standard" not in out or a.fresh_standard:
        out["standard"] = measure(e, repo, talents, std if a.armor else None, a.final, 3, ref, f"m-{cls}") | {"stats": gear_stats(std, db, edb)}
        log(f"  standard set: tank value {out['standard']['value']:.4f}, threat {out['standard']['threat']}, damage taken {out['standard']['dtps']}")
    for tier in tiers:
        p = set_path(cls, tier, a.smoke, a.armor)
        tmpl = FE.role(p.name)
        cur = [dict(x) for x in std]
        FE.fill(cur, tmpl)
        tag = f"tank-{cls}-{tier}"
        wf = TankWeights(e, repo, talents, ref, a.weight_iterations, tag)
        r = GT.optimize_set(cls, [(entry_name, e, "raid", talents, pick)], cur, GT.pool_of(tier, zones), repo, db, a, tag,
                            keep_current=(tier == "bis"), weights_fn=wf, score=lambda row: R.tank_value(row, ref) or 0)
        items = r["items"]
        FE.fill(items, tmpl)
        ench = choose_enchants(items, r["weights"], db, edb)
        wench = race_weapon_enchant(e, repo, talents, items, db, ref, a, tag)
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(json.dumps({"items": items}, indent=1) + "\n", encoding="utf-8")
        m = measure(e, repo, talents, items, a.final, 3, ref, f"m-{cls}")
        pre = out.get("prebis") if tier == "bis" else None
        if pre and (pre.get("pick") or {}).get("value", 0) > m["value"] and pre.get("items"):
            # the BiS pool holds every pre-BiS item, so the pre-BiS set is a BiS set too: a BiS search that ends below it takes it
            # (2026-11-11: the paladin's BiS search ended at tank value 1.1836, its pre-BiS set measured 1.1917 on the same fights)
            log(f"  bis: the search's set measures {m['value']:.4f}, below the pre-BiS set's {pre['pick']['value']:.4f}: the pre-BiS set is kept")
            items = [dict(x) for x in pre["items"]]
            p.write_text(json.dumps({"items": items}, indent=1) + "\n", encoding="utf-8")
            m = {k: v for k, v in pre["pick"].items() if k != "stats"}
            r = dict(r, items=items, chosen="the pre-BiS set (the BiS search ended below it)", trinkets=pre.get("trinkets") or r.get("trinkets"),
                     ilvl=pre.get("ilvl", r.get("ilvl")))
            ench = {k: v for k, v in (pre.get("enchants_by_weight") or {}).items()}
            wench = pre.get("weapon_enchant")
        s = out["standard"]
        rt = dict(r, names=[db.get(x.get("id"), {}).get("name") if x.get("id") else None for x in items], items=items,
                  weights_unit="threat per second equivalents of tank value (threat weight - k x damage-taken weight)", raw_weights=wf.last,
                  enchants_by_weight={str(k): v for k, v in ench.items()}, weapon_enchant=wench, gear=p.relative_to(ROOT).as_posix(),
                  pick=m | {"stats": gear_stats(items, db, edb)},
                  vs_standard={"value": round(m["value"] / s["value"] - 1, 4), "threat": round(m["threat"] / s["threat"] - 1, 4),
                               "dtps": round(m["dtps"] / s["dtps"] - 1, 4)}, date=TODAY)
        if a.armor and set_path(cls, tier, a.smoke).exists():   # the simulator's own set for the tier, measured with the armor filled in
            simset = json.load(open(set_path(cls, tier, a.smoke), encoding="utf-8"))["items"]
            ms = measure(e, repo, talents, simset, a.final, 3, ref, f"m-{cls}")
            rt["simulator_set_with_armor"] = ms | {"vs_this_set": round(ms["value"] / m["value"] - 1, 4),
                                                   "same_items": sum(1 for x, y in zip(simset, items) if x.get("id") == y.get("id"))}
            log(f"    the simulator's own {tier} set with the armor filled in: tank value {ms['value']:.4f} ({ms['value'] / m['value'] - 1:+.1%}), "
                f"{rt['simulator_set_with_armor']['same_items']} of 17 slots the same")
        out[tier] = rt
        log(f"  {tier}: item level {r['ilvl']}, chosen {r['chosen']}, trinkets {', '.join(r['trinkets'])}; tank value {m['value']:.4f} "
            f"({rt['vs_standard']['value']:+.1%}), threat {m['threat']} ({rt['vs_standard']['threat']:+.1%}), damage taken {m['dtps']} "
            f"({rt['vs_standard']['dtps']:+.1%})")
        log("    " + "; ".join(n for n in rt["names"] if n))
        yield
    out["minutes"] = round((time.time() - t0) / 60, 1)


def main():
    global G, GT, R, FE
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("classes", nargs="*", default=list(TANK_ENTRY), choices=list(TANK_ENTRY))
    ap.add_argument("--tiers", default=",".join(TIERS))
    ap.add_argument("--iterations", type=int, default=3000)
    ap.add_argument("--confirm", type=int, default=12000)
    ap.add_argument("--weight-iterations", type=int, default=6000)
    ap.add_argument("--final", type=int, default=20000, help="fights of the record's comparison with the standard set (seed 3)")
    ap.add_argument("--max-pairs", type=int, default=60, help="trinket pairs raced (60: every pair of the tanks' 4-9 preset trinkets)")
    ap.add_argument("--armor", action="store_true", help="the sensitivity: missing base armor filled in from Classic (sets *-classic-armor)")
    ap.add_argument("--build", action="append", default=[], metavar="CLASS=ID", help="another build than the page's pick")
    ap.add_argument("--fresh-standard", action="store_true", help="measure the reference and the standard set again")
    ap.add_argument("--ref-fights", type=int, default=20000, help="fights of the tank-value reference (deep_tank.py's 20,000)")
    ap.add_argument("--smoke", action="store_true", help="tiny budgets; sets and record under raidsim/deep-smoke/tank-gear/ (a test)")
    a = ap.parse_args()
    a.min_gain = 0.0
    a.build = dict(x.split("=", 1) for x in a.build)
    if a.smoke:
        a.iterations, a.confirm, a.weight_iterations, a.final, a.max_pairs, a.ref_fights = 200, 400, 300, 400, 3, 400
    GT = _load("gear_tiers_tank", HERE / "gear_tiers.py")
    G, R = GT.G, GT.R
    import fill_enchants as FE  # noqa: F811
    R.set_game("forever")
    repo = R.repo_path(argparse.Namespace(repo=None))
    db, zones = GT.load_db(repo)
    STAT_NAMES[:] = G.stat_names(repo)
    edb = enchant_db(repo)
    if a.armor:
        install_armor(db)
    rp = SMOKE_DIR / "tank-gear.json" if a.smoke else RECORD
    rp.parent.mkdir(parents=True, exist_ok=True)
    rec = json.load(open(rp, encoding="utf-8")) if rp.exists() else {}
    rec.update({"simulator": f"wowsims/forever {R.git_commit(repo)} (with this project's patches)", "date": TODAY,
                "budget": {"iterations": a.iterations, "confirm": a.confirm, "weight_iterations": a.weight_iterations, "final": a.final,
                           "max_pairs": a.max_pairs}})
    tiers = [t for t in a.tiers.split(",") if t in TIERS]
    for cls in a.classes:
        for _ in run_class(cls, tiers, repo, db, zones, edb, a, rec):
            rp.write_text(json.dumps(rec, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
        rp.write_text(json.dumps(rec, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    log(f"wrote {rp.relative_to(ROOT).as_posix()}")


if __name__ == "__main__":
    main()
