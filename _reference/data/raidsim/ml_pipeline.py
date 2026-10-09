"""The systematic optimisation of every raid damage spec (2026-10-01, user request: "approach these classes and specs in a more systematic
machine learning model method ... and DPS rankings for pre-BiS as well as best in slot, like WoWSims"): gear tiers, talents by the
machine-learning search (ml_talents.py) and rotations (apl_opt.py), in turns, then the tier ranking.

    python _reference/data/raidsim/ml_pipeline.py [classes] [--spec "<spec>"] [--steps targets,gear,talents,rotations,final] [--fresh]

Steps run step by step over every target (the rotation step needs every spec's first winner), each resuming from the spec's record
`raidsim/ml/<class>-<spec slug>.json` unless --fresh:
1. targets: every raid damage spec of the player pages (spec_modes.py: a tree with 30+ points, a hybrid, or a spec named by a build's
   spec field such as Frostfire), its candidate entries (the simulator entries whose last races hold a build of the spec, plus EXTRA;
   showcase entries whose rotation is kept as designed are left out: EXCLUDE) and its current best build.
2. gear: the spec's phase-1 BiS set (gear_tiers.py) for its current best build.
2b. spells: spell_probe.py in every candidate entry, both settings: every ability a talent grants that the rotation does not cast is
   tried with the spec's build (or its legal neighbours that add the talent), in every guard and spot; lines that pay are written
   into the rotation, so the talent search can value those talents (user request: "allowed to use all spells").
3. talents: ml_talents.py on the training dummy in that set, two independent runs over the candidate entries.
4. rotations: apl_opt.py --tune on each entry's winners in their BiS sets, training dummy and raid (180 s; the rotations had been tuned
   at 120 s on older builds and gear).
5. final: the BiS set again for the winner; ml_talents.py warm-started from it in the new rotations: BiS dummy, BiS raid; the pre-BiS
   set for the BiS winner; pre-BiS dummy and raid; then the winner, the spec's best hand draft and its current pick raced on the same
   fresh seed (100k fights) in the BiS set, for the 2% rule.
Then ml_builds.py writes the winners into the builds and the ranking pages. Simulations of the community's model of the beta.
"""
import argparse
import datetime
import importlib.util
import json
import pathlib
import subprocess
import sys
import time

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[2]
sys.path[:0] = [str(ROOT / "_reference/data"), str(HERE)]
import paths  # noqa: E402
import spec_modes as SM  # noqa: E402


def _load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


MLT = _load("ml_talents", HERE / "ml_talents.py")
GT = _load("gear_tiers", HERE / "gear_tiers.py")
R = MLT.R
OUT = HERE / "ml"
TODAY = datetime.date.today().isoformat()
STEPS = ["targets", "gear", "spells", "talents", "rotations", "final"]
EXCLUDE = {("paladin", "seal-of-fury-raid"), ("paladin", "shockadin-raid")}   # showcase entries: rotations kept as designed
EXTRA = {("warlock", "Destruction"): ["fire-destro-raid", "sb-raid"]}   # 30+ Destruction under the Shadow Bolt rotations too


def rm():
    return _load("render_modes_mod", ROOT / "_reference/data/render_modes.py")


def reload_specs():
    """specs.json again in every loaded copy of run.py: the rotation step's apl_opt.py runs in a subprocess and may add an entry's
    first tuned rotation (`apl_opt` / `apl_opt_raid`), which a copy read at start would not know."""
    seen, todo = set(), [MLT, GT]
    while todo:
        m = todo.pop()
        if id(m) in seen:
            continue
        seen.add(id(m))
        if hasattr(m, "SPECS") and hasattr(m, "set_game") and hasattr(m, "GAMES"):
            m.set_game(getattr(m, "GAME", "forever"))
        todo += [v for v in vars(m).values() if type(v) is type(sys) and str(getattr(v, "__file__", "")).startswith(str(ROOT))]


def log(m):
    print(m, flush=True)


def rec_path(cls, spec):
    return OUT / f"{cls}-{SM.slug(spec)}.json"


def load(cls, spec):
    p = rec_path(cls, spec)
    return json.load(open(p, encoding="utf-8")) if p.exists() else None


def save(rec):
    p = rec_path(rec["class"], rec["spec"])
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(rec, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")


def by_tree(space, flat):
    return {t: [[n, flat[n]] for n in space.by_tree[t] if flat.get(n)] for t in space.tree_names}


def flat_of(alloc):
    return {n: r for items in alloc.values() for n, r in items}


# ------------------------------------------------------------------------------------------------ steps
def targets(cls):
    M = rm()
    builds = {b["id"]: b for b in json.load(open(paths.builds_json("forever", cls), encoding="utf-8"))["builds"]}
    nums = M.raid_numbers(cls)
    held = {}
    for x in M.rs.raid_rows(cls):
        b = builds.get(x["row"]["label"])
        if not x["tank"] and b and b.get("role") not in ("healer", "tank"):
            held.setdefault(SM.spec_of(cls, b), set()).add(x["spec"])
    out = []
    for spec, modes in SM.grid(cls, list(builds.values())).items():
        rows = [b for b in modes["raid"] if b.get("role") not in ("healer", "tank") and not b["id"].endswith("-parse")
                and (nums.get(b["id"]) or {}).get("dps") and not nums[b["id"]].get("tank")]
        if not rows:
            continue
        best = max(rows, key=lambda b: nums[b["id"]]["dps"])
        ents = (held.get(spec, set()) | {nums[best["id"]]["entry"]} | set(EXTRA.get((cls, spec), []))) - {e for c, e in EXCLUDE if c == cls}
        # each spec only in entries built for it (2026-10-08, user decision: no spec takes another spec's rotation)
        ents = {e for e in ents if not SM.RAID_ENTRY_TREES.get((cls, e)) or SM.rotation_allows(spec, SM.RAID_ENTRY_TREES[(cls, e)])}
        if nums[best["id"]]["entry"] not in ents:
            continue
        ents = [nums[best["id"]]["entry"]] + sorted(ents - {nums[best["id"]]["entry"]})
        out.append({"class": cls, "spec": spec, "slug": SM.slug(spec), "entries": ents, "best": best["id"], "best_entry": nums[best["id"]]["entry"],
                    "best_dps": round(nums[best["id"]]["dps"], 2), "any_split": (best.get("spec") or "").startswith("Hybrid")})
    return out


def gear(rec, tier, alloc, label, entry, repo, db, zones):
    trees = R.load_trees(repo, rec["class"])
    g = GT.make(rec["class"], rec["spec"], tier, entry, R.talents_string(trees, alloc), label, repo, db, zones, GT.args_ns())
    keep = ("entry", "gear", "date", "chosen", "ilvl", "trinkets", "names", "race_seed1", "confirm_seed2", "weights", "evaluated_on")
    return {k: g[k] for k in keep if k in g}


QUICK = [1.0]   # --quick: budgets x 0.2 and one run (a smoke test)


def talents(rec, setting, tier, gear_path, extra, runs, budget, entries=None):
    q = QUICK[0]
    a = MLT.defaults(runs=runs if q == 1.0 else 1, budget=int(budget * q), screen_budget=int(600 * q), random_init=int(250 * max(q, 0.4)),
                     seed=1 + len(rec.get("search", {})))
    out, win = MLT.run_target(rec["class"], rec["spec"], entries or rec["entries"], setting, gear_path, a, log, extra_starts=extra, any_split=rec["any_split"])
    return out, win


def rotations(recs, a):
    """apl_opt.py --tune per entry on the first winners in their BiS sets (both settings)."""
    per = {}
    for rec in recs:
        s = rec.get("search", {}).get("bis-dummy-1")
        if s:
            per.setdefault((rec["class"], s["entry"]), []).append({"label": f"ml: {rec['spec']}", "allocation": s["winner"]["allocation"],
                                                                     "gear": rec["gear"]["bis"]["gear"]})
    done = json.load(open(OUT / "rotations.json", encoding="utf-8")) if (OUT / "rotations.json").exists() else {}
    for (cls, entry), builds in sorted(per.items()):
        k = f"{cls}/{entry}"
        if k in done and not a.fresh:
            log(f"== rotations {k}: done")
            continue
        tune = OUT / "tune" / f"{cls}-{entry}.json"
        tune.parent.mkdir(parents=True, exist_ok=True)
        tune.write_text(json.dumps(builds, indent=1), encoding="utf-8")
        log(f"== rotations {k}: tuning on {', '.join(b['label'] for b in builds)}")
        t0 = time.time()
        r = subprocess.run([sys.executable, str(HERE / "apl_opt.py"), cls, "--spec", entry, "--tune", str(tune), "--write"],
                           capture_output=True, text=True, encoding="utf-8", errors="replace", cwd=str(ROOT))
        lines = [ln for ln in r.stdout.splitlines() if ln.strip()]
        for ln in lines:
            if ln.startswith(("==", "  round", "  dummy", "  raid", "  wrote", "  no change")):
                log("  " + ln.strip()[:220])
        done[k] = {"rc": r.returncode, "minutes": round((time.time() - t0) / 60, 1), "date": TODAY, "tail": lines[-6:],
                   "stderr": r.stderr[-600:] if r.returncode else ""}
        (OUT / "rotations.json").write_text(json.dumps(done, indent=1) + "\n", encoding="utf-8")


def compare(rec, repo, setting="dummy"):
    """The winner of the setting (bis-dummy or bis-raid), the spec's two best hand drafts and its current best builds (dummy: the
    target's best; raid: the three best builds of any origin by full-raid DPS), each in its own entry and in the BiS set, on one fresh
    seed. Raid pages rank by full-raid DPS since 2026-10-02 (user decision), so ml_builds.py decides on the raid comparison."""
    cls = rec["class"]
    key = "dps" if setting == "dummy" else "group"
    data = {b["id"]: b for b in json.load(open(paths.builds_json("forever", cls), encoding="utf-8"))["builds"]}
    nums = rm().raid_numbers(cls)
    mine = [b for b in data.values() if SM.mode_of(b) == "raid" and SM.spec_of(cls, b) == rec["spec"] and b.get("role") not in ("healer", "tank")
            and nums.get(b["id"], {}).get(key) and not nums[b["id"]].get("tank")]
    hands = [b for b in mine if not b.get("generated") and not b["id"].startswith("opt-") and (setting == "raid" or not b["id"].endswith("-parse"))]
    gear_items = json.load(open(ROOT / rec["gear"]["bis"]["gear"], encoding="utf-8"))["items"]
    w = rec["search"]["bis-dummy" if setting == "dummy" else "bis-raid"]
    rows = {"winner": (w["entry"], flat_of(w["winner"]["allocation"]))}
    for b in sorted(hands, key=lambda b: -nums[b["id"]][key])[:2]:
        rows[b["id"]] = (nums[b["id"]]["entry"], R.alloc_of(b))
    if setting == "raid":
        for b in sorted(mine, key=lambda b: -nums[b["id"]][key])[:3]:
            rows.setdefault(b["id"], (nums[b["id"]]["entry"], R.alloc_of(b)))
    elif rec["best"] in data:
        rows.setdefault(rec["best"], (rec["best_entry"], R.alloc_of(data[rec["best"]])))
    out = {}
    for label, (entry, al) in rows.items():
        sim = MLT.Sim(cls, entry, setting, gear_items, repo, f"ml-cmp-{cls}")
        d, sd = sim.run([al], 100000, 7)[0]
        out[label] = {"entry": entry, "dps": round(d, 2), "se": round(sd / 316.23, 3)}
    hand_ids = {b["id"] for b in hands}
    hand_best = max((k for k in out if k in hand_ids), key=lambda k: out[k]["dps"], default=None)
    return {"setting": setting, "dps": out, "best_hand": hand_best,
            "gain_vs_hand": round(out["winner"]["dps"] / out[hand_best]["dps"] - 1, 4) if hand_best else None}


def final(rec, repo, db, zones):
    s = rec.setdefault("search", {})
    first = flat_of(s["bis-dummy-1"]["winner"]["allocation"])
    if "bis2" not in rec.get("gear", {}):
        rec["gear"]["bis"] = gear(rec, "bis", first, "ml winner", s["bis-dummy-1"]["entry"], repo, db, zones)
        rec["gear"]["bis2"] = True
        save(rec)
    bis = rec["gear"]["bis"]["gear"]
    if "bis-dummy" not in s:
        s["bis-dummy"], _ = talents(rec, "dummy", "bis", bis, [first], runs=1, budget=1500)
        save(rec)
    w = flat_of(s["bis-dummy"]["winner"]["allocation"])
    if "bis-raid" not in s:
        s["bis-raid"], _ = talents(rec, "raid", "bis", bis, [w, first], runs=1, budget=1500)
        save(rec)
    if "prebis" not in rec["gear"]:
        rec["gear"]["prebis"] = gear(rec, "prebis", w, "ml winner (bis)", s["bis-dummy"]["entry"], repo, db, zones)
        save(rec)
    pre = rec["gear"]["prebis"]["gear"]
    if "prebis-dummy" not in s:
        s["prebis-dummy"], _ = talents(rec, "dummy", "prebis", pre, [w], runs=1, budget=1200)
        save(rec)
    if "prebis-raid" not in s:
        s["prebis-raid"], _ = talents(rec, "raid", "prebis", pre, [flat_of(s["prebis-dummy"]["winner"]["allocation"]), flat_of(s["bis-raid"]["winner"]["allocation"])],
                                      runs=1, budget=1200)
        save(rec)
    if "compare" not in rec:
        rec["compare"] = compare(rec, repo)
        save(rec)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("classes", nargs="*")
    ap.add_argument("--spec")
    ap.add_argument("--steps", default=",".join(STEPS))
    ap.add_argument("--fresh", action="store_true")
    ap.add_argument("--quick", action="store_true", help="small budgets and one run per search (a smoke test)")
    a = ap.parse_args()
    if a.quick:
        QUICK[0] = 0.2
    steps = a.steps.split(",")
    R.set_game("forever")
    repo = R.repo_path(argparse.Namespace(repo=None))
    db, zones = GT.load_db(repo)
    classes = a.classes or SM.CLASSES
    recs = []
    for cls in classes:
        for t in targets(cls):
            if a.spec and t["spec"] != a.spec:
                continue
            rec = load(cls, t["spec"])
            if rec is not None and a.fresh and any(((rec.get("search") or {}).get(k) or {}).get("winner") for k in ("bis-dummy", "prebis-dummy")):
                # keep the finished record (2026-10-08): the pages show its gear tiers until the new run has its own (render_modes.ml_tiers)
                pv = OUT / "prev" / f"{cls}-{rec.get('slug') or t.get('slug')}.json"
                pv.parent.mkdir(parents=True, exist_ok=True)
                pv.write_text(json.dumps(rec, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
            if rec is None or a.fresh:
                rec = dict(t, date=TODAY, gear={}, search={})
            else:
                rec.update({k: v for k, v in t.items() if k not in ("best", "best_entry", "best_dps")})   # entries may change; the start stays
            save(rec)
            recs.append(rec)
    log(f"== {len(recs)} targets: " + "; ".join(f"{r['class']} {r['spec']} ({', '.join(r['entries'])})" for r in recs))
    if "gear" in steps:
        for rec in recs:
            if "bis" in rec["gear"] and not a.fresh:
                continue
            log(f"== gear bis: {rec['class']} {rec['spec']} ({rec['best']} in {rec['best_entry']})")
            data = {b["id"]: b for b in json.load(open(paths.builds_json("forever", rec["class"]), encoding="utf-8"))["builds"]}
            rec["gear"]["bis"] = gear(rec, "bis", R.alloc_of(data[rec["best"]]), rec["best"], rec["best_entry"], repo, db, zones)
            save(rec)
    if "spells" in steps:
        SP = _load("spell_probe", HERE / "spell_probe.py")
        for rec in recs:
            if rec.get("spells_done") and not a.fresh:
                continue
            data = {b["id"]: b for b in json.load(open(paths.builds_json("forever", rec["class"]), encoding="utf-8"))["builds"]}
            items = json.load(open(ROOT / rec["gear"]["bis"]["gear"], encoding="utf-8"))["items"]
            kept = 0
            for entry in rec["entries"]:
                for setting in ("dummy", "raid"):
                    log(f"== spells: {rec['class']} {rec['spec']} in {entry} ({setting})")
                    res, base = SP.probe(rec["class"], rec["spec"], entry, R.alloc_of(data[rec["best"]]), setting, items, rec["any_split"], log)
                    kept += SP.write(rec["class"], entry, setting, res, base)
            rec["spells_done"] = {"date": TODAY, "lines_kept": kept}
            save(rec)
    if "talents" in steps:
        for rec in recs:
            if "bis-dummy-1" in rec["search"] and not a.fresh:
                continue
            rec["search"]["bis-dummy-1"], _ = talents(rec, "dummy", "bis", rec["gear"]["bis"]["gear"], [], runs=2, budget=2500)
            save(rec)
    if "rotations" in steps:
        rotations(recs, a)
        reload_specs()
    if "final" in steps:
        for rec in recs:
            log(f"== final: {rec['class']} {rec['spec']}")
            final(rec, repo, db, zones)
    log("== done")


if __name__ == "__main__":
    main()
