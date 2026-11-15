"""Standard errors of the gear add-on's raid and tank stat values (2026-11-14; the user, relayed by the Addons session: "yes, ask them to
measure it": one standard error per raid and tank value, so GearCheck can give raid and tank comparisons the noise band its healer
values already have).

    python -u _reference/data/raidsim/weight_errors.py [--only KEY ...] [--jobs 2] [--repo CHECKOUT] [--bench EXE]
    python -u _reference/data/raidsim/weight_errors.py --study KEY ... --seeds 16    # how the stats' estimates move together

Every raid and tank value of characters/addon/forever-gear-values.json (characters/addon_values.py raid() and tank()) is one simulator
stat-weights run (the bench's `statweights` mode, core.StatWeights). Each is run again here in exactly its configuration with the bench's
`weights_se` (foreverbench since 2026-11-14: weights_stdev / sqrt(sample_counts) per stat and pseudo-stat, the standard deviation of the
per-iteration paired differences over the root of the paired samples behind the weight; tanks also `dtps_se`). The simulator is
deterministic for a configuration and seed, so every mean must come back as stored; an entry whose means do not is marked
(`reproduced: false` and why) and its errors are measured on the closest configuration the records give. Keys:

- ml:<stem>       raidsim/ml/<stem>.json gear.bis.weights (gear_tiers.optimize_set, 3,000 iterations, full raid). The stored weights are
                  the optimizer's second weights() call, measured on the set its first greedy pass made, not on the final BiS set (1-12
                  items differ), so the exact configuration exists only as the bench config that call wrote: <checkout>/bench/
                  gearopt-w-<class>-<slug>-bis.json. A record with a "bis-raid" set has that tag's config overwritten by the later bis-raid
                  set's search; its configuration is replayed (the start talents, the entry's set, its weights, the greedy pass).
- page:<stem>     raidsim/page-stat-weights.json weights (page_stat_weights.py, 6,000; gearopt-psw-<stem>.json).
- hit:<stem>      raidsim/hit-below-cap.json (hit_below_cap.py, 6,000, the set's hit taken off; gearopt-hit-<stem>.json).
- pagehit:<stem>  page-stat-weights.json hit_below_cap (gearopt-psh-<stem>.json).
- tank:<class>    characters/weights/<class>-tank.json raw_weights, tps and dtps (tank_weights.py, 3,000; gearopt-tw-<class>.json, the
                  stat-weights call, and its base run, the same configuration as a race row).
The configs are looked up in every simulator checkout under ~/.wow-forever-tools (the newest file of the tag) and run with --repo/--bench
(default: setup.checkout() and its foreverbench). The first pass (2026-11-14) ran in wowsims-forever-y with this bench built there as
foreverbench-se: the values (2026-11-11 to 11-13) predate the Lacerating Strikes patch, which the main checkout has had since 2026-11-13
18:52 (`simulator.patched_files` in the record lists the checkout's patches). Racials: the raid lanes set WOW_FOREVER_NO_RACIALS=1 (most ML
records' BiS weights, Tara's tank weights); the gear repair's remakes of 2026-11-11 (gear_tiers.py --remake: the mage's Fire, Frost and
Frostfire sets, the druid's Balance set) and the interactive runs of 2026-11-13 (hit under the cap, the page weights, the warrior and bear
tank weights) did not. Each config runs first with the setting that reproduced the last config of its checkout, then the other one if the
means differ (`racials` in the record says which).

Record raidsim/weight-errors.json (date, simulator commit and checkout, per key the configuration, the means, their standard errors and the
check against the stored values). characters/addon_values.py turns them into each raid and tank entry's `errors` (the values' unit).

--study re-runs the named keys on seeds 2..N (run.sim_seed: disjoint iterations) and writes `study`: per stat the spread of the means over
the seeds against the reported standard error (is weights_stdev / sqrt(sample_counts) the right size?), the correlation of the stats'
estimates over the seeds (the add-on treats stats' errors as independent), and real slot swaps (each record's pre-BiS item against its
BiS item, the simulator's item stats): the spread of a swap's score change over the seeds against the independent-errors prediction.
Findings of 2026-11-14 (12 seeds; mage Frost, rogue Combat, hunter Beast Mastery, the paladin tank): where it matters the reported error
is the right size, real slot swaps' score changes spread 0.82-1.10x the independent-errors prediction. Per stat it is 0.6-1.3x the spread
for the stats that change probabilities (crit, haste, hit, expertise, Agility, Intellect; the tank's avoidance 0.5-0.8x) and 1.1-1.8x low
for the smooth ones (spell power, attack power, Strength, weapon DPS: one iteration's low and high runs move together, which the merged
samples' formula ignores; their errors are about 0.1% of the value). The stats' estimates are about uncorrelated on average (mean r -0.01
to 0.18); the strong pairs are stats of one channel (attack power and Strength 1.0, a school's damage and spell damage 0.8-1.0, the tank's
dodge and parry in damage taken 0.99). A tank's threat and damage-taken readings of dodge, parry and block correlate about +0.6, so their
independent share errors are about twice their spread. `swap_noise_all`: every ML entry's pre-BiS -> BiS slot swaps, one standard error
0.074% of the set's item score (median; 0.02-0.17% by spec, at most 0.29%) against a median gain of 1%.
Numbers are the simulator's model of the beta, not measurements.
"""
import argparse
import concurrent.futures
import datetime
import json
import math
import os
import pathlib
import subprocess
import sys
import threading

HERE = pathlib.Path(__file__).resolve().parent
DATA = HERE.parent
ROOT = DATA.parent.parent
CHAR = DATA / "characters"
sys.path[:0] = [str(HERE), str(DATA)]
OUT = HERE / "weight-errors.json"
CLASSES = "druid hunter mage paladin priest rogue shaman warlock warrior".split()
NO_RACIALS = "WOW_FOREVER_NO_RACIALS"
# characters/tank_weights.py KEYS (its raw_weights' names), copied: importing it puts characters/ first on sys.path
TANK_KEYS = {"StatStrength": "strength", "StatAgility": "agility", "StatStamina": "stamina", "StatIntellect": "intellect",
             "StatSpirit": "spirit", "StatSpellDamage": "spell_power", "StatHealingPower": "healing", "StatAttackPower": "attack_power",
             "StatHitRating": "hit", "StatCritRating": "crit", "StatHasteRating": "haste", "StatExpertiseRating": "expertise",
             "StatDefenseRating": "defense", "StatBlockRating": "block", "StatBlockValue": "block_value", "StatDodgeRating": "dodge",
             "StatParryRating": "parry", "StatArmor": "armor", "StatMP5": "mp5", "PseudoStatMainHandDps": "weapon_dps"}
_R = []


def R():
    """raidsim/run.py, loaded once (Forever specs)."""
    if not _R:
        import run
        run.set_game("forever")
        _R.append(run)
    return _R[0]


def load(p, default=None):
    p = pathlib.Path(p)
    return json.loads(p.read_text(encoding="utf-8")) if p.exists() else ({} if default is None else default)


def checkouts():
    import setup
    return sorted(p for p in setup.tools_dir().glob("wowsims-forever*") if (p / "bench").is_dir())


def find_config(tag):
    """The newest bench config gear_opt.run_bench wrote under `tag` in any simulator checkout, or None."""
    hits = [c / "bench" / f"gearopt-{tag}.json" for c in checkouts()]
    hits = [p for p in hits if p.exists()]
    return max(hits, key=lambda p: p.stat().st_mtime) if hits else None


def local_path(p):
    """A config's absolute project path (gear set, rotation), moved onto this worktree when its own worktree no longer has it (the
    interactive runs of 2026-11-13 ran in F:/wow-forever-stats, whose rotations are the same JSON as main's)."""
    if not p or pathlib.Path(p).exists():
        return p
    s = str(p).replace("\\", "/")
    i = s.find("/_reference/")
    q = ROOT / s[i + 1:] if i >= 0 else None
    return str(q) if q is not None and q.exists() else p


def rel(p):
    s = str(p or "").replace("\\", "/")
    i = s.find("/_reference/")
    return s[i + 1:] if i >= 0 else s


# ---------------------------------------------------------------------------------------------------------------------------- targets
def targets():
    """[{key, kind, stored, tag, why, ...}] for every raid and tank value the data file holds (addon_values.raid / tank)."""
    below = load(HERE / "hit-below-cap.json").get("specs", {})
    page = load(HERE / "page-stat-weights.json").get("specs", {})
    out = []
    for cls in CLASSES:
        for f in sorted((HERE / "ml").glob(f"{cls}-*.json")):
            d = load(f)
            bis = (d.get("gear") or {}).get("bis") or {}
            if not isinstance(bis, dict) or not bis.get("weights"):
                continue
            out.append({"key": f"ml:{f.stem}", "kind": "weights", "class": cls, "spec": d.get("spec"), "stem": f.stem,
                        "stored": {k: v for k, v in bis["weights"].items()}, "rounded": 4, "tag": f"w-{cls}-{d['slug']}-bis",
                        "source": f"raidsim/ml/{f.name} gear.bis.weights", "iterations": 3000})
            if f.stem in below and below[f.stem].get("hit_below_cap") is not None:
                h = below[f.stem]
                out.append({"key": f"hit:{f.stem}", "kind": "hit", "class": cls, "spec": d.get("spec"), "stem": f.stem, "rounded": 4,
                            "stored": {"StatHitRating": h["hit_below_cap"], "StatSpellDamage": h.get("spell_damage", 0.0),
                                       "StatAttackPower": h.get("attack_power", 0.0)}, "gear_hit": h.get("gear_hit_rating"),
                            "tag": f"hit-{f.stem}", "source": f"raidsim/hit-below-cap.json specs.{f.stem}", "iterations": 6000})
        for stem, row in sorted(page.items()):
            if row.get("class") != cls:
                continue
            if row.get("weights"):
                out.append({"key": f"page:{stem}", "kind": "weights", "class": cls, "spec": row.get("spec"), "stem": stem,
                            "stored": dict(row["weights"]), "rounded": None, "tag": f"psw-{stem}",
                            "source": f"raidsim/page-stat-weights.json specs.{stem} weights", "iterations": 6000})
            if row.get("hit_below_cap") is not None:
                out.append({"key": f"pagehit:{stem}", "kind": "hit", "class": cls, "spec": row.get("spec"), "stem": stem, "rounded": 4,
                            "stored": {"StatHitRating": row["hit_below_cap"]}, "tag": f"psh-{stem}",
                            "source": f"raidsim/page-stat-weights.json specs.{stem} hit_below_cap", "iterations": 6000})
        tf = CHAR / "weights" / f"{cls}-tank.json"
        if tf.exists():
            w = load(tf)
            out.append({"key": f"tank:{cls}", "kind": "tank", "class": cls, "spec": w.get("spec"), "stem": cls, "rounded": None,
                        "stored": w["raw_weights"], "stored_base": {"tps": w["tps"], "dtps": w["dtps"]}, "tag": f"tw-{cls}",
                        "source": f"characters/weights/{tf.name} raw_weights", "iterations": w.get("iterations", 3000), "tank_file": w})
    return out


# ------------------------------------------------------------------------------------------------------------ the closest configs
def ml_start(rec, trees):
    """The talents the BiS set was chosen for: a remade set (gear_tiers.remake) the bis-dummy winner, else bis-dummy-1's, with talents the
    trees lack left out; ml_pipeline.final the bis-dummy-1 winner or the start its sig_start note names (an open-search winner or a raid
    build of ours). Returns ({talent: rank}, why)."""
    s = rec.get("search", {})
    flat = lambda al: {n: r for items in (al or {}).values() for n, r in items if r}  # noqa: E731
    known = {R().talent_key(t) for tr in trees for t in tr["talents"]}
    if (rec["gear"]["bis"].get("remade") or {}):
        sk = next((k for k in ("bis-dummy", "bis-dummy-1") if k in s), None)
        al = flat(s[sk]["winner"]["allocation"])
        return {n: r for n, r in al.items() if n in known}, f"the {sk} winner (a remade set)"
    note = (s.get("bis-dummy-1") or {}).get("sig_start") or ""
    import re
    m = re.search(r"starts from the (\S+) open-search winner \((\S+)\)", note)
    if m:
        fam = load(HERE / "families" / m.group(2)).get("entries", {}).get(m.group(1)) or {}
        w = ((fam.get("again") or fam.get("first") or {}).get("winner") or {})
        return flat(w.get("allocation")), f"the {m.group(1)} open-search winner (families/{m.group(2)}, as the sig_start note says)"
    m = re.search(r"starts from our raid build (\S+)", note)
    if m:
        bs = {b["id"]: b for b in load(ROOT / rec["class"] / "research/talents/forever/proposed-builds.json")["builds"]}
        if m.group(1) in bs:
            return {n: r for n, r in R().alloc_of(bs[m.group(1)]).items() if r}, f"our raid build {m.group(1)} (the sig_start note)"
    return flat(s["bis-dummy-1"]["winner"]["allocation"]), "the bis-dummy-1 winner"


def replay_ml(t, repo, runner):
    """The ML record's BiS weights configuration made again (gear_tiers.make -> optimize_set up to its second weights() call): the start
    talents, the entry's own set with the role's enchants, its weights, the first greedy pass; returns (config, note)."""
    import gear_tiers as GT
    import fill_enchants as FE
    G, RR = GT.G, GT.R
    rec = load(HERE / "ml" / f"{t['stem']}.json")
    cls, spec, bis = rec["class"], rec["spec"], rec["gear"]["bis"]
    e = RR.SPECS[cls][bis["entry"]]
    trees = RR.load_trees(repo, cls)
    alloc, why = ml_start(rec, trees)
    tal = RR.talents_string(trees, alloc)
    gp = pathlib.Path(RR.sim_path(e["gear"]))
    cur = load(gp if gp.is_absolute() else pathlib.Path(repo) / e["gear"])["items"]
    tmpl = FE.role(GT.set_path(cls, spec, "bis").name)
    if tmpl:
        FE.fill(cur, tmpl)
    db, zones = GT.load_db(repo)
    pool = GT.pool_of("bis", zones)
    cur_items = [dict(x) if x else {} for x in cur] + [{}] * (17 - len(cur))
    cfg0 = G.bench_cfg(e, repo, [{"label": "w", "talents": tal, "gear_json": {"items": [x if x.get("id") in db else {} for x in cur_items]}}],
                       3000, 1, "raid", statweights=True)
    w0 = runner(cfg0, f"{t['key']}-replay0")["row"]["weights"]
    _, _, greedy = G.class_picker(repo, cls, db, pool)
    v1 = greedy(cur_items, w0, False)
    cfg = G.bench_cfg(e, repo, [{"label": "w", "talents": tal, "gear_json": {"items": v1}}], 3000, 1, "raid", statweights=True)
    return cfg, f"replayed: {why}, {bis['entry']}'s set and its weights, the first greedy pass"


def closest(t, repo):
    """The configuration the records give when the bench config is gone or does not reproduce (the final set, not the greedy one)."""
    RR = R()
    import gear_opt as G
    cls = t["class"]
    trees = RR.load_trees(repo, cls)
    builds = {b["id"]: b for b in load(ROOT / cls / "research/talents/forever/proposed-builds.json")["builds"]}
    if t["key"].startswith("ml:") or t["key"].startswith("hit:"):
        rec = load(HERE / "ml" / f"{t['stem']}.json")
        bis = rec["gear"]["bis"]
        e = RR.SPECS[cls][bis.get("entry") or rec["best_entry"]]
        items = load(ROOT / bis["gear"])["items"]
        if t["key"].startswith("ml:"):
            alloc, why = ml_start(rec, trees)
            b = {"label": "w", "talents": RR.talents_string(trees, alloc), "gear_json": {"items": items}}
            return G.bench_cfg(e, repo, [b], 3000, 1, "raid", statweights=True), f"closest: {why} in the final BiS set"
        b = {"label": "w", "talents": RR.talents_string(trees, {n: r for n, r in RR.alloc_of(builds[rec["best"]]).items() if r}),
             "gear_json": {"items": items}}
        hit = t.get("gear_hit")
        if hit:
            b["bonus_stats"] = {"StatHitRating": -float(hit)}
        return G.bench_cfg(e, repo, [b], 6000, 1, "raid", statweights=True), "closest: hit_below_cap.py's configuration"
    if t["key"].startswith(("page:", "pagehit:")):
        row = load(HERE / "page-stat-weights.json")["specs"][t["stem"]]
        e = RR.SPECS[cls][row["entry"]]
        b = {"label": "w", "talents": RR.talents_string(trees, {n: r for n, r in RR.alloc_of(builds[row["build"]]).items() if r}),
             "gear_json": {"items": load(ROOT / row["gear"])["items"]}}
        if t["key"].startswith("pagehit:") and row.get("gear_hit_rating"):
            b["bonus_stats"] = {"StatHitRating": -float(row["gear_hit_rating"])}
        return G.bench_cfg(e, repo, [b], 6000, 1, "raid", statweights=True), "closest: page_stat_weights.py's configuration"
    w = t["tank_file"]
    e = RR.SPECS[cls][w["entry"]]
    b = {"label": "w", "talents": RR.talents_string(trees, {n: r for n, r in RR.alloc_of(builds[w["build"]]).items() if r})}
    return G.bench_cfg(e, repo, [b], w.get("iterations", 3000), 1, RR.setting(e), statweights=True), "closest: tank_weights.py's configuration"


# ------------------------------------------------------------------------------------------------------------------------ running
class Runner:
    def __init__(self, repo, bench):
        self.repo, self.bench = pathlib.Path(repo), pathlib.Path(bench)
        self.lock = threading.Lock()
        self.prefer = {}   # checkout -> the racials setting that reproduced last there ("off" = WOW_FOREVER_NO_RACIALS=1)
        self.runs = 0

    def __call__(self, cfg, name, racials="off", seed=None):
        with self.lock:
            self.runs += 1
        cfg = dict(cfg, gear=local_path(cfg.get("gear")), apl=local_path(cfg.get("apl")))
        if seed is not None:
            cfg["seed"] = R().sim_seed(seed)
        p = self.repo / "bench" / f"weight-errors-{name.replace(':', '-')}{'' if seed is None else f'-s{seed}'}.json"
        p.parent.mkdir(exist_ok=True)
        p.write_text(json.dumps(cfg), encoding="utf-8")
        env = dict(os.environ)
        env.pop(NO_RACIALS, None)
        if racials == "off":
            env[NO_RACIALS] = "1"
        r = subprocess.run([str(self.bench), "--config", str(p), "--root", str(self.repo)], capture_output=True, text=True, env=env)
        if r.returncode:
            raise SystemExit(f"{name}: bench failed: {r.stderr[-800:]}")
        bad = [ln for ln in r.stderr.splitlines() if ln.startswith("spec: the simulator ignores")]
        if bad:
            raise SystemExit(f"{name}: {bad[0]}")
        rows = [json.loads(ln) for ln in r.stdout.splitlines() if ln.startswith("{")]
        row = rows[0]
        if row.get("error"):
            raise SystemExit(f"{name}: {row['error']}")
        return {"row": row, "racials": racials, "config": cfg}


def compare(t, row, base=None):
    """[(stat, stored, new)] that differ: rounded stores within half a unit of the 4th decimal, raw stores within 1e-9 (relative)."""
    bad = []
    tol = (lambda a, b: abs(a - b) <= 0.5e-4 + 1e-9) if t["rounded"] == 4 else (lambda a, b: abs(a - b) <= 1e-9 * max(1.0, abs(a)))
    if t["kind"] == "tank":
        names = {v: k for k, v in TANK_KEYS.items()}
        for key, sd in t["stored"].items():
            n = names.get(key)
            for metric, src in (("tps", row.get("weights") or {}), ("dtps", row.get("dtps_weights") or {})):
                a, b = sd[metric], src.get(n, 0.0)
                if not tol(a, b):
                    bad.append((f"{n} {metric}", a, b))
        if base is not None:
            for k, src in (("tps", "threat"), ("dtps", "dtps")):
                if not tol(t["stored_base"][k], base.get(src, 0.0)):
                    bad.append((f"base {k}", t["stored_base"][k], base.get(src)))
        return bad
    w = row.get("weights") or {}
    for k, a in t["stored"].items():
        if not tol(a, w.get(k, 0.0)):
            bad.append((k, a, w.get(k, 0.0)))
    if t["rounded"] == 4 and t["kind"] == "weights":   # the store drops |v| <= 1e-6: those must be (near) zero here too
        for k, b in w.items():
            if k not in t["stored"] and abs(b) > 1e-6 and abs(b) >= 0.5e-4:
                bad.append((k, None, b))
    return bad


def sig(x, n=7):
    return float(f"{x:.{n}g}") if isinstance(x, (int, float)) else x


def gear_text(items):
    """A gear set as one line: each slot's item id, "/enchant" when it has one, 0 for an empty slot."""
    return " ".join(f"{(x or {}).get('id', 0)}" + (f"/{x['enchant']}" if (x or {}).get("enchant") else "") for x in items)


def config_summary(cfg, path=None):
    b = cfg["builds"][0]
    items = (b.get("gear_json") or {}).get("items")
    return {"file": str(path).replace("\\", "/") if path else None, "apl": rel(cfg.get("apl")), "buffs": cfg.get("buffs"),
            "targetLevel": cfg.get("targetLevel"), "isTank": cfg.get("isTank"), "iterations": cfg.get("iterations"), "seed": cfg.get("seed"),
            "duration": cfg.get("duration"), "talents": b.get("talents"), "bonus_stats": b.get("bonus_stats"),
            "gear": gear_text(items) if items else rel(cfg.get("gear"))}


def candidates(t, runner):
    """The configurations to try, in order: the bench config the run wrote, the replay (ML records), the closest the records give.
    Each a function -> (config, note, checkout name, path or None)."""
    out = []
    path = find_config(t["tag"])
    collided = False
    if t["key"].startswith("ml:"):   # the tag's last config is the later bis-raid set's (gear_tiers.make uses one tag for both)
        collided = "bis-raid" in (load(HERE / "ml" / f"{t['stem']}.json").get("gear") or {})
    if path is not None and not collided:
        def own(path=path):
            cfg = load(path)
            cfg["builds"] = [dict(cfg["builds"][0], label="w")]
            return cfg, f"the bench config the run wrote ({path.parent.parent.name}/bench/{path.name})", path.parent.parent.name, path
        out.append(own)
    if t["key"].startswith("ml:"):
        def rep():
            cfg, note = replay_ml(t, runner.repo, lambda c, n: runner(c, n, "off"))
            if collided:
                note += f" (the tag's bench config, {path.name if path else 'none'}, is the later bis-raid set's)"
            return cfg, note, "replay", None
        out.append(rep)

    def clo():
        cfg, note = closest(t, runner.repo)
        return cfg, note, "closest", None
    out.append(clo)
    return out


def measure(t, runner):
    """One key: each candidate configuration (with the other racials setting when the means differ) until one reproduces the stored
    means; else the run that came closest, marked."""
    out = {"kind": t["kind"], "class": t["class"], "spec": t["spec"], "source": t["source"]}
    tries, best = [], None
    for make in candidates(t, runner):
        try:
            cfg, note, ck, path = make()
        except (Exception, SystemExit) as ex:   # a replay or a closest config the records cannot give: the next candidate
            tries.append({"config": getattr(make, "__name__", "?"), "error": str(ex)[:300]})
            continue
        if t["kind"] == "tank":
            cfg = dict(cfg, statweights=True)
        first = runner.prefer.get(ck, "off")
        for rac in (first, "on" if first == "off" else "off"):
            res = runner(cfg, t["key"], rac)
            base = None
            if t["kind"] == "tank":
                bcfg = dict(cfg, statweights=False, builds=[dict(cfg["builds"][0], label="b")])
                base = runner(bcfg, t["key"] + "-base", rac)["row"]
            bad = compare(t, res["row"], base)
            tries.append({"config": note, "racials": rac, "differences": len(bad)})
            if best is None or len(bad) < len(best[1]):
                best = (res, bad, base, note, path)
            if not bad:
                with runner.lock:
                    runner.prefer[ck] = rac
                break
        if not best[1]:
            break
    if best is None:
        raise SystemExit(f"{t['key']}: no configuration could be run ({tries})")
    res, bad, base, note, path = best
    row = res["row"]
    out.update({"reproduced": not bad, "config_from": note, "racials": res["racials"], "tries": tries,
                "differences": [{"stat": k, "stored": a, "rerun": sig(b)} for k, a, b in bad][:20],
                "config": config_summary(res["config"], path), "seconds": round(row.get("seconds", 0), 1),
                "weights": {k: sig(v) for k, v in sorted(row["weights"].items()) if v or k in (row.get("weights_se") or {})},
                "se": {k: sig(v) for k, v in sorted((row.get("weights_se") or {}).items())}})
    if t["kind"] == "tank":
        out["dtps_weights"] = {k: sig(v) for k, v in sorted(row["dtps_weights"].items()) if v or k in (row.get("dtps_se") or {})}
        out["dtps_se"] = {k: sig(v) for k, v in sorted((row.get("dtps_se") or {}).items())}
        out["base"] = {"threat": sig(base["threat"]), "dtps": sig(base["dtps"]), "dtps_stdev": sig(base.get("dtps_stdev")),
                       "iterations": base.get("iterations")}
    return out


# ---------------------------------------------------------------------------------------------------------------------- the study
SLOT_PSEUDO = {14: "PseudoStatMainHandDps", 15: "PseudoStatOffHandDps", 16: "PseudoStatRangedDps"}
_STAT = {}


def stat_names(repo):
    """{index: proto Stat name} from the checkout's proto/common.proto (the item database keys stats by these indices)."""
    if not _STAT:
        import re
        txt = (pathlib.Path(repo) / "proto" / "common.proto").read_text(encoding="utf-8")
        body = re.search(r"enum Stat \{(.*?)\n\}", txt, re.S).group(1)
        _STAT.update({int(v): n for n, v in re.findall(r"(Stat\w+)\s*=\s*(\d+);", body)})
    return _STAT


def item_stats(db, it, slot, repo):
    """An item's static stats in the simulator's stat names (scalingOptions 0), its weapon DPS as the slot's pseudo-stat."""
    if not it or not it.get("id") or it["id"] not in db:
        return {}
    names = stat_names(repo)
    x = db[it["id"]]
    so = (x.get("scalingOptions") or {}).get("0") or {}
    out = {}
    for k, v in (so.get("stats") or {}).items():
        n = names.get(int(k))
        if n:
            out[n] = out.get(n, 0.0) + v
    if slot in SLOT_PSEUDO and so.get("weaponDamageMax"):
        out[SLOT_PSEUDO[slot]] = (so["weaponDamageMin"] + so["weaponDamageMax"]) / 2 / (x.get("weaponSpeed") or 2.0)
    return out


def swaps_of(stem, db, repo):
    """Real slot swaps for an ML record: each slot's pre-BiS item against its BiS item, [(slot, old stats, new stats)]; and the BiS
    set's summed stats (the score of everything equipped)."""
    rec = load(HERE / "ml" / f"{stem}.json")
    g = rec.get("gear") or {}
    if not (g.get("bis") or {}).get("gear") or not (g.get("prebis") or {}).get("gear"):
        return [], {}
    bis, pre = load(ROOT / g["bis"]["gear"])["items"], load(ROOT / g["prebis"]["gear"])["items"]
    out, tot = [], {}
    for i in range(min(len(bis), len(pre))):
        a, b = item_stats(db, pre[i], i, repo), item_stats(db, bis[i], i, repo)
        for k, v in b.items():
            tot[k] = tot.get(k, 0.0) + v
        if (pre[i] or {}).get("id") != (bis[i] or {}).get("id") and (a or b):
            out.append((i, a, b))
    return out, tot


def study(keys, seeds, runner, rec, jobs):
    import statistics
    tg = {t["key"]: t for t in targets()}
    res = {}
    todo = [(k, s) for k in keys for s in range(2, seeds + 1)]
    cfgs = {}
    for k in keys:
        e = rec["entries"][k]
        cfg = None
        p = find_config(tg[k]["tag"])
        if e.get("config_from", "").startswith("the bench config") and p is not None:
            cfg = load(p)
            cfg["builds"] = [dict(cfg["builds"][0], label="w")]
        if cfg is None:
            raise SystemExit(f"--study {k}: only keys measured from their bench config")
        if tg[k]["kind"] == "tank":
            cfg = dict(cfg, statweights=True)
        cfgs[k] = (cfg, e["racials"])
    with concurrent.futures.ThreadPoolExecutor(jobs) as ex:
        futs = {ex.submit(runner, cfgs[k][0], f"study-{k}", cfgs[k][1], s): (k, s) for k, s in todo}
        for f in concurrent.futures.as_completed(futs):
            k, s = futs[f]
            row = f.result()["row"]
            res.setdefault(k, {})[s] = row
            print(f"  study {k} seed {s}: {row.get('seconds', 0):.0f} s", flush=True)
    db = {it["id"]: it for it in load(pathlib.Path(runner.repo) / "assets/database/db.json")["items"]}
    out = {"seeds": seeds, "what": ("per key: seeds 1-N (run.sim_seed, disjoint iterations). calibration = the spread (standard deviation) of "
                                    "each stat's mean over the seeds over the mean of its reported standard errors (1 = the reported error "
                                    "is the right size); correlation = the stats' estimates over the seeds, standardized, pairwise; swaps = "
                                    "each slot's pre-BiS item against its BiS item (simulator item stats, no enchants): the spread of the "
                                    "score change over the seeds against the independent-errors prediction sqrt(sum (dx * se)^2)"),
           "keys": {}}
    for k in keys:
        e = rec["entries"][k]
        metrics = [("weights", "se")] + ([("dtps_weights", "dtps_se")] if tg[k]["kind"] == "tank" else [])
        rows = {1: {"weights": e["weights"], "weights_se": e["se"], "dtps_weights": e.get("dtps_weights"), "dtps_se": e.get("dtps_se")}}
        rows.update(res.get(k, {}))
        sk = sorted(rows)
        block = {"seeds": len(sk)}
        for wkey, skey in metrics:
            sekey = "weights_se" if skey == "se" else "dtps_se"
            stats = sorted(set.intersection(*[set((rows[s].get(sekey) or {})) for s in sk]))
            stats = [n for n in stats if statistics.mean(rows[s][sekey][n] for s in sk) > 0]
            cal = {}
            z = {}
            for n in stats:
                xs = [rows[s][wkey].get(n, 0.0) for s in sk]
                ses = [rows[s][sekey][n] for s in sk]
                sd = statistics.stdev(xs)
                se = math.sqrt(statistics.mean(v * v for v in ses))
                cal[n] = {"mean": sig(statistics.mean(xs), 5), "spread": sig(sd, 4), "se": sig(se, 4), "ratio": round(sd / se, 3)}
                m = statistics.mean(xs)
                z[n] = [(x - m) / se for x in xs]
            ratios2 = [cal[n]["spread"] ** 2 / cal[n]["se"] ** 2 for n in stats]
            pooled = math.sqrt(statistics.mean(ratios2)) if ratios2 else None
            pairs = []
            for i, a in enumerate(stats):
                for b in stats[i + 1:]:
                    za, zb = z[a], z[b]
                    sa, sb = math.sqrt(sum(v * v for v in za)), math.sqrt(sum(v * v for v in zb))
                    if sa and sb:
                        pairs.append((a, b, sum(x * y for x, y in zip(za, zb)) / (sa * sb)))
            rs = [p[2] for p in pairs]
            null = math.sqrt(2 / math.pi / max(1, len(sk) - 2))   # the mean |r| of independent samples of this size (about)
            block[wkey] = {"stats": len(stats), "pooled_ratio": round(pooled, 3) if pooled else None,
                           "median_ratio": round(statistics.median(math.sqrt(x) for x in ratios2), 3) if ratios2 else None,
                           "calibration": cal,
                           "correlation": {"pairs": len(rs), "mean_r": round(statistics.mean(rs), 3) if rs else None,
                                           "mean_abs_r": round(statistics.mean(abs(x) for x in rs), 3) if rs else None,
                                           "mean_abs_r_if_independent": round(null, 3),
                                           "strongest": [{"a": a, "b": b, "r": round(r, 3)} for a, b, r in sorted(pairs, key=lambda p: -abs(p[2]))[:8]]}}
        if tg[k]["kind"] == "tank":   # tank_weights.py's share: 0.5 t / TPS + 0.25 (-d) / DTPS (+ effective health, exact)
            tw = tg[k]["tank_file"]
            tps, dtps = tw["tps"], tw["dtps"]
            names = sorted(set(TANK_KEYS) & set(block["weights"]["calibration"]) & set(block["dtps_weights"]["calibration"]))
            share = {}
            for n in names:
                xs = [0.5 * rows[s]["weights"].get(n, 0.0) / tps - 0.25 * rows[s]["dtps_weights"].get(n, 0.0) / dtps for s in sk]
                ts = [rows[s]["weights"].get(n, 0.0) for s in sk]
                ds = [rows[s]["dtps_weights"].get(n, 0.0) for s in sk]
                pred = math.sqrt(statistics.mean((0.5 * rows[s]["weights_se"][n] / tps) ** 2 + (0.25 * rows[s]["dtps_se"][n] / dtps) ** 2
                                                 for s in sk))
                sd = statistics.stdev(xs)
                r_td = statistics.correlation(ts, ds) if statistics.stdev(ts) and statistics.stdev(ds) else None
                share[n] = {"spread": sig(sd, 4), "predicted": sig(pred, 4), "ratio": round(sd / pred, 3) if pred else None,
                            "r_threat_damage": round(r_td, 3) if r_td is not None else None}
            rr = [x["ratio"] for x in share.values() if x["ratio"]]
            rt = [x["r_threat_damage"] for x in share.values() if x["r_threat_damage"] is not None]
            block["share"] = {"stats": len(share), "pooled_ratio": round(math.sqrt(statistics.mean(x * x for x in rr)), 3) if rr else None,
                              "mean_r_threat_damage": round(statistics.mean(rt), 3) if rt else None, "per_stat": share}
        else:
            sw, tot = swaps_of(tg[k]["stem"], db, runner.repo)
            rows_sw = []
            for slot, a, b in sw:
                dx = {n: b.get(n, 0.0) - a.get(n, 0.0) for n in set(a) | set(b)}
                per = [sum(v * rows[s]["weights"].get(n, 0.0) for n, v in dx.items()) for s in sk]
                score = [sum(v * rows[s]["weights"].get(n, 0.0) for n, v in tot.items()) for s in sk]
                pred = math.sqrt(statistics.mean(sum((v * rows[s]["weights_se"].get(n, 0.0)) ** 2 for n, v in dx.items()) for s in sk))
                sd = statistics.stdev(per)
                rows_sw.append({"slot": slot, "gain_pct": round(100 * statistics.mean(per) / statistics.mean(score), 3),
                                "spread_pct": round(100 * sd / statistics.mean(score), 4), "predicted_pct": round(100 * pred / statistics.mean(score), 4),
                                "ratio": round(sd / pred, 3) if pred else None})
            if rows_sw:
                rr = [x["ratio"] for x in rows_sw if x["ratio"]]
                block["swaps"] = {"count": len(rows_sw), "pooled_ratio": round(math.sqrt(statistics.mean(x * x for x in rr)), 3) if rr else None,
                                  "median_predicted_pct": statistics.median(x["predicted_pct"] for x in rows_sw),
                                  "median_abs_gain_pct": statistics.median(abs(x["gain_pct"]) for x in rows_sw), "rows": rows_sw}
        out["keys"][k] = block
    # every ML entry's real slot swaps (pre-BiS item -> BiS item) with the full pass's errors, no extra runs: the predicted noise of a
    # swap's score change in percent of the BiS set's score, against the swap's gain
    allsw = {}
    for kk, e in sorted(rec["entries"].items()):
        if not kk.startswith("ml:"):
            continue
        sw, tot = swaps_of(kk[3:], db, runner.repo)
        score = sum(v * e["weights"].get(n, 0.0) for n, v in tot.items())
        if not sw or score <= 0:
            continue
        pr, gn = [], []
        for slot, a, b in sw:
            dx = {n: b.get(n, 0.0) - a.get(n, 0.0) for n in set(a) | set(b)}
            pr.append(100 * math.sqrt(sum((v * e["se"].get(n, 0.0)) ** 2 for n, v in dx.items())) / score)
            gn.append(100 * sum(v * e["weights"].get(n, 0.0) for n, v in dx.items()) / score)
        allsw[kk] = {"swaps": len(sw), "median_noise_pct": round(statistics.median(pr), 4), "max_noise_pct": round(max(pr), 4),
                     "median_abs_gain_pct": round(statistics.median(abs(x) for x in gn), 3),
                     "within_2_errors": sum(1 for p, g in zip(pr, gn) if abs(g) < 2 * p)}
    out["swap_noise_all"] = {"what": ("per ML entry: its pre-BiS -> BiS slot swaps (simulator item stats, no enchants), one standard error "
                                      "of the score change (independent stats, the full pass's errors) and the gain, in percent of the BiS "
                                      "set's item score; within_2_errors: swaps whose gain is inside two errors"), "entries": allsw}
    return out


def sim_state(repo):
    head = subprocess.run(["git", "-C", str(repo), "rev-parse", "HEAD"], capture_output=True, text=True).stdout.strip()
    st = subprocess.run(["git", "-C", str(repo), "status", "--porcelain"], capture_output=True, text=True).stdout.splitlines()
    patched = sorted(ln[3:] for ln in st if ln[3:].startswith("sim/"))
    return {"repo": "wowsims/forever", "commit": head, "checkout": pathlib.Path(repo).name, "patched_files": patched}


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--only", nargs="*", default=[], help="these keys only (ml:<stem>, page:<stem>, hit:<stem>, pagehit:<stem>, tank:<class>)")
    ap.add_argument("--jobs", type=int, default=2, help="configs run side by side (each bench run uses every core already)")
    ap.add_argument("--repo", help="the simulator checkout that runs the configs (default: setup.checkout())")
    ap.add_argument("--bench", help="the bench executable (default: <repo>/foreverbench)")
    ap.add_argument("--study", nargs="*", default=[], help="keys to re-run on seeds 2..--seeds for the error study")
    ap.add_argument("--seeds", type=int, default=3)
    ap.add_argument("--list", action="store_true", help="print the keys and their config files")
    a = ap.parse_args()
    import setup
    repo = pathlib.Path(a.repo) if a.repo else setup.checkout()
    bench = pathlib.Path(a.bench) if a.bench else repo / "foreverbench"
    runner = Runner(repo, bench)
    ts = targets()
    if a.list:
        for t in ts:
            p = find_config(t["tag"])
            print(f"{t['key']:56s} {t['source']:70s} {p if p else 'NO CONFIG'}")
        return
    rec = load(OUT, {"entries": {}})
    rec.setdefault("entries", {})
    if not a.study:
        todo = [t for t in ts if not a.only or t["key"] in a.only]
        print(f"{len(todo)} keys, {a.jobs} at a time, {bench.name} in {repo.name}", flush=True)
        t0 = datetime.datetime.now()
        with concurrent.futures.ThreadPoolExecutor(a.jobs) as ex:
            futs = {ex.submit(measure, t, runner): t for t in todo}
            for f in concurrent.futures.as_completed(futs):
                t = futs[f]
                try:
                    e = f.result()
                except (Exception, SystemExit) as ex:   # one key's failure is reported; the others are kept
                    print(f"{t['key']:56s} FAILED: {str(ex)[:300]}", flush=True)
                    continue
                rec["entries"][t["key"]] = e
                print(f"{t['key']:56s} {'reproduced' if e['reproduced'] else 'NOT REPRODUCED (' + str(len(e['differences'])) + ' stats)'}"
                      f" racials {e['racials']}, {e['seconds']} s; {e['config_from']}", flush=True)
        keep = {t["key"] for t in ts}
        rec["entries"] = {k: rec["entries"][k] for k in sorted(rec["entries"]) if k in keep}
        took = {"runs": runner.runs, "minutes": round((datetime.datetime.now() - t0).total_seconds() / 60, 1), "jobs": a.jobs}
        if a.only:
            rec.setdefault("partial_passes", []).append(dict(took, keys=a.only, date=datetime.date.today().isoformat()))
        else:
            rec["pass"] = took
            rec.pop("partial_passes", None)
        rec.update(date=datetime.date.today().isoformat(), simulator=sim_state(repo), bench=bench.name,
                   unit=("weights: the simulator's DPS per point (tanks: threat per second per point; dtps_weights: damage taken per second per "
                         "point), means as the run printed them; se: one standard error, weights_stdev / sqrt(sample_counts), same unit"))
    else:
        rec["study"] = study(a.study, a.seeds, runner, rec, a.jobs)
    OUT.write_text(json.dumps(rec, indent=1) + "\n", encoding="utf-8", newline="\n")
    print(f"wrote {OUT.relative_to(ROOT).as_posix()}", flush=True)


if __name__ == "__main__":
    main()
