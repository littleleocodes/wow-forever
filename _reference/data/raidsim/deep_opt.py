"""Deep optimisation of one class's raid damage specs: talents, gear and rotation tuned together until none of them moves (2026-10-02,
user request: "a full optimization analysis on Shaman. Find the best talent tree entirely for each spec and the best rotation for each.
Doing a full ML model analysis that 100% finds the best optimization").

    python -u _reference/data/raidsim/deep_opt.py shaman [--spec "<spec>"] [--cycles 3] [--fresh]

No search over a space this size can prove a global optimum, and every simulated number has noise; this one makes a better build very
unlikely. Per spec of the class's machine-learning records (raidsim/ml/<class>-<spec>.json; hybrids keep their tree rule: no tree at
30 points, the two named trees largest), every damage entry of the class screened as the rotation family:
1. cycles, until the winners, the BiS gear and the rotations all repeat (at most --cycles):
   a. BiS gear for the spec's current training-dummy winner (gear_tiers.make; cycle 1 keeps the ML record's set);
   b. the talent search (ml_talents.py: random forest + genetic search; cycle 1 with 6 independent runs of up to 5,000 builds screened at
      1,500 fights, each run stopping after 8 rounds without a gain; later cycles 3 runs of 3,000 seeded with the winners), on the training dummy and in a full raid, races on fresh seeds,
      the one-move and chain-move check;
   c. the rotations of the winners' entries re-tuned on the winners in their gear (apl_opt.py --tune; every build an entry lists stays
      protected), both settings;
2. the two-move check of the BiS winners (ml_talents.two_move_certificate: every build one or two moves away, 30,000 to 50,000 for a
   shaman, simulated on one seed with common random numbers, the best 60 raced, the best 5 again over 100,000 fights);
3. pre-BiS: the gear for the dummy winner, searches seeded with the BiS winners (3 runs), the one-move check;
4. final races over 200,000 fights on a fresh seed: each winner against every build of ours of the spec, in its gear and setting.
The winners replace the ML record's (search, gear, compare), so `ml_builds.py --builds --tidy-winners --rank` writes builds and pages.
Record `raidsim/deep/<class>.json` (resumable step by step), report `<class>/research/raid/deep-optimization.md`.
"""
import argparse
import datetime
import hashlib
import importlib.util
import json
import math
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


MP = _load("ml_pipeline_deep", HERE / "ml_pipeline.py")
MLT, GT, R = MP.MLT, MP.GT, MP.R
OUT = HERE / "deep"
TODAY = datetime.date.today().isoformat()
DEEP = dict(runs=6, budget=5000, screen=1500, patience=8, max_rounds=40, random_init=500, pool=10000, parents=48, finalists=8, screen_budget=800)
QUICK = dict(runs=3, budget=3000, screen=1500, patience=5, max_rounds=20, random_init=300, pool=8000, parents=40, finalists=6, screen_budget=600)
FINAL_FIGHTS = 200000
SMOKE = False
SETTINGS = ("raid",)   # 2026-10-04, user decision: raid and leveling builds only; --dummy adds the training dummy back


def log(m):
    print(m, flush=True)


def flat_of(alloc):
    return {n: r for items in alloc.values() for n, r in items}


def rec_path(cls):
    return OUT / f"{cls}.json"


def load(cls):
    p = rec_path(cls)
    return json.load(open(p, encoding="utf-8")) if p.exists() else {"class": cls, "date": TODAY, "specs": {}, "cycles": []}


def save(st):
    OUT.mkdir(parents=True, exist_ok=True)
    rec_path(st["class"]).write_text(json.dumps(st, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")


def damage_entries(cls):
    """The class's damage entries (the rotation families every spec is screened in)."""
    return [e for e, x in R.SPECS[cls].items() if isinstance(x, dict) and "apl" in x and not x.get("tank")
            and x.get("profile", "raid-dps") == "raid-dps" and (cls, e) not in MP.EXCLUDE]


def apl_hash(cls, entries):
    repo = R.repo_path(argparse.Namespace(repo=None))
    h = hashlib.sha1()
    for e in entries:
        for st in ("dummy", "raid"):
            p = R.apl_path(R.SPECS[cls][e], repo, st)
            h.update(p.read_bytes() if p.exists() else b"")
    return h.hexdigest()[:12]


def search(cls, spec, entries, setting, gear_path, settings, starts, seed, protect=None):
    a = MLT.defaults(**settings, seed=seed)
    rec, win = MLT.run_target(cls, spec, entries, setting, gear_path, a, log, extra_starts=starts, any_split=False, protect=protect)
    return rec


def retune(cls, winners, st):
    """apl_opt.py --tune per entry on the winners in their gear (both settings); True when a rotation file changed."""
    if SMOKE:   # a test never rewrites rotations
        log("== rotations: skipped (smoke test)")
        return False
    per = {}
    for k, w in winners.items():
        spec, setting = k.split("|")
        per.setdefault(w["entry"], []).append({"label": f"deep: {spec} ({setting})", "allocation": w["allocation"], "gear": w["gear"]})
    changed = False
    for entry, builds in sorted(per.items()):
        before = apl_hash(cls, [entry])
        tune = OUT / "tune" / f"{cls}-{entry}.json"
        tune.parent.mkdir(parents=True, exist_ok=True)
        tune.write_text(json.dumps(builds, indent=1), encoding="utf-8")
        log(f"== rotations {cls}/{entry}: tuning on {', '.join(b['label'] for b in builds)} (every build the entry lists protected)")
        t0 = time.time()
        r = subprocess.run([sys.executable, str(HERE / "apl_opt.py"), cls, "--spec", entry, "--tune", str(tune), "--write", "--rounds", "20",
                            *(["--setting", "raid"] if SETTINGS == ("raid",) else [])],
                           capture_output=True, text=True, encoding="utf-8", errors="replace", cwd=str(ROOT))
        for ln in r.stdout.splitlines():
            if ln.strip().startswith(("==", "round", "dummy", "raid", "wrote", "no change")):
                log("  " + ln.strip()[:220])
        if r.returncode:
            log(f"  apl_opt failed: {r.stderr[-800:]}")
        moved = apl_hash(cls, [entry]) != before
        changed = changed or moved
        st.setdefault("rotations", []).append({"entry": entry, "date": TODAY, "rc": r.returncode, "changed": moved, "minutes": round((time.time() - t0) / 60, 1)})
        save(st)
    MP.reload_specs()
    return changed


def winner_of(rec, gear_path):
    w = rec["winner"]
    return {"allocation": w["allocation"], "split": w["split"], "dps": w["dps"], "se": w["se"], "entry": rec["entry"], "gear": gear_path,
            "runs_agree": rec["runs_agree"], "runs": len(rec["runs"]), "simulated_builds": rec["simulated_builds"],
            "certificate": rec.get("certificate"), "runner_up": rec.get("runner_up"), "gap_to_runner_up": rec.get("gap_to_runner_up")}


def same(a, b):
    return a and b and flat_of(a["allocation"]) == flat_of(b["allocation"]) and a["entry"] == b["entry"]


def final_race(cls, spec, w, setting, gear_path, repo):
    """The winner against every build of ours of the spec (each in its own entry), FINAL_FIGHTS on a fresh seed, in the winner's gear."""
    data = {b["id"]: b for b in json.load(open(paths.builds_json("forever", cls), encoding="utf-8"))["builds"]}
    nums = MP.rm().raid_numbers(cls)
    rows = {"deep winner": (w["entry"], flat_of(w["allocation"]))}
    for bid, b in data.items():
        if SM.mode_of(b) == "raid" and SM.spec_of(cls, b) == spec and b.get("role") not in ("healer", "tank") and bid in nums:
            if setting == "dummy" and bid.endswith("-parse"):
                continue
            rows[bid] = (nums[bid]["entry"], R.alloc_of(b))
    gear = json.load(open(ROOT / gear_path, encoding="utf-8"))["items"]
    out = {}
    for label, (entry, al) in rows.items():
        sim = MLT.Sim(cls, entry, setting, gear, repo, f"deep-final-{cls}")
        d, sd = sim.run([al], FINAL_FIGHTS, 41)[0]
        out[label] = {"entry": entry, "dps": round(d, 2), "se": round(sd / math.sqrt(FINAL_FIGHTS), 3)}
    log(f"  final race {spec} ({setting}): " + ", ".join(f"{k} {v['dps']:.1f}" for k, v in sorted(out.items(), key=lambda kv: -kv[1]["dps"])))
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("cls")
    ap.add_argument("--spec", action="append")
    ap.add_argument("--cycles", type=int, default=3)
    ap.add_argument("--fresh", action="store_true")
    ap.add_argument("--smoke", action="store_true", help="tiny budgets, a separate record, no ML records or report written (a test)")
    ap.add_argument("--dummy", action="store_true", help="also search the training dummy (off since 2026-10-04: the pages are raid and leveling only)")
    a = ap.parse_args()
    global OUT, DEEP, QUICK, FINAL_FIGHTS, SMOKE, SETTINGS
    if a.smoke:
        OUT, FINAL_FIGHTS, SMOKE = HERE / "deep-smoke", 4000, True
        DEEP = QUICK = dict(runs=1, budget=150, screen=300, patience=1, max_rounds=1, random_init=40, pool=600, parents=8, finalists=2, screen_budget=60,
                            race_stages=((1000, 2, 2), (2000, 3, 1), (4000, 4, 1)), cert_its=(500, 2000))   # a test: small races too
    if a.dummy:
        SETTINGS = ("dummy", "raid")
    cls = a.cls
    R.set_game("forever")
    repo = R.repo_path(argparse.Namespace(repo=None))
    db, zones = GT.load_db(repo)
    st = {"class": cls, "date": TODAY, "specs": {}, "cycles": []} if a.fresh else load(cls)
    entries = damage_entries(cls)
    recs = {r["spec"]: r for r in (MP.load(cls, t["spec"]) for t in MP.targets(cls)) if r and (not a.spec or r["spec"] in a.spec)}
    log(f"== deep optimisation of {cls}: specs {', '.join(recs)}; entries {', '.join(entries)}")
    t_start = time.time()
    # 1. cycles: gear -> talents (dummy, raid) -> rotations, until nothing moves
    for cyc in range(len(st["cycles"]) + 1, a.cycles + 1):
        prev = st["cycles"][-1] if st["cycles"] else None
        c = st.get("current") or {"cycle": cyc, "winners": {}, "gear": {}}
        st["current"] = c
        settings = DEEP if cyc == 1 else QUICK
        for spec, rec in recs.items():
            sk = SM.slug(spec)
            if spec not in c["gear"]:
                if cyc == 1 or SMOKE:   # (a test never rewrites gear sets)
                    c["gear"][spec] = rec["gear"]["bis"]["gear"]
                else:
                    w0 = prev["winners"].get(f"{spec}|raid") or prev["winners"][f"{spec}|dummy"]
                    g = MP.gear(rec, "bis", flat_of(w0["allocation"]), "deep winner", w0["entry"], repo, db, zones)
                    c["gear"][spec] = g["gear"]
                    c.setdefault("gear_rec", {})[spec] = g
                save(st)
            gear_path = c["gear"][spec]
            # every earlier winner of the spec is a start (the ML record's four, the deep cycles')
            starts = [flat_of(x["winner"]["allocation"]) for x in rec.get("search", {}).values() if x and x.get("winner")]
            starts += [flat_of(w["allocation"]) for cc in st["cycles"] for k, w in cc["winners"].items() if k.startswith(spec + "|")]
            for setting in SETTINGS:
                k = f"{spec}|{setting}"
                if k in c["winners"]:
                    continue
                sr = search(cls, spec, entries, setting, gear_path, settings, starts, seed=100 * cyc + (1 if setting == "dummy" else 2))
                c["winners"][k] = winner_of(sr, gear_path)
                c.setdefault("records", {})[k] = {kk: sr[kk] for kk in ("runs", "runs_agree", "race", "certificate", "entries_screened", "important_features",
                                                                       "simulated_builds", "minutes", "protected") if kk in sr}
                starts.append(flat_of(sr["winner"]["allocation"]))
                save(st)
                log(f"  [{cyc}] {spec} {setting}: {sr['winner']['split']} in {sr['entry']} {sr['winner']['dps']:.1f}")
        if "rotations_changed" not in c:
            c["rotations_before"] = apl_hash(cls, entries)
            c["rotations_changed"] = retune(cls, c["winners"], st)
            c["rotations_after"] = apl_hash(cls, entries)
            save(st)
        st["cycles"].append(c)
        st.pop("current", None)
        save(st)
        moved = [k for k, w in c["winners"].items() if not (prev and same(w, prev["winners"].get(k)))]
        gear_moved = [s for s in recs if prev and c["gear"].get(s) != prev["gear"].get(s)] if prev else list(recs)
        log(f"== cycle {cyc}: winners changed {len(moved)} ({', '.join(moved) or 'none'}), rotations changed {c['rotations_changed']}")
        if prev and not moved and not c["rotations_changed"]:
            st["converged"] = cyc
            save(st)
            break
    last = st["cycles"][-1]
    # 2. the two-move check of the BiS winners
    fin = st.setdefault("final", {})
    for spec, rec in recs.items():
        gear_path = last["gear"][spec]
        gear = json.load(open(ROOT / gear_path, encoding="utf-8"))["items"]
        for setting in SETTINGS:
            k = f"{spec}|{setting}"
            if k in fin.get("two_move", {}):
                continue
            w = last["winners"][k]
            sp = MLT.Space(cls, spec)
            sp.protect = set((last.get("records", {}).get(k) or {}).get("protected") or [])
            sim = MLT.Sim(cls, w["entry"], setting, gear, repo, f"deep-2m-{cls}")
            log(f"== two-move check {spec} ({setting}) from {w['split']} in {w['entry']}")
            new, steps = (MLT.two_move_certificate(sp, sim, flat_of(w["allocation"]), log, screen=200, conf=(2000, 4000), top=5, expand_top=2, rounds=1)
                          if SMOKE else MLT.two_move_certificate(sp, sim, flat_of(w["allocation"]), log))
            moved = flat_of(w["allocation"]) != new
            if moved:
                w = dict(w, allocation=MP.by_tree(sp, new), split=sp.split(new), moved_by_two_move_check=True)
                last["winners"][k] = w
            fin.setdefault("two_move", {})[k] = {"steps": steps, "moved": moved}
            save(st)
    # 3. pre-BiS
    for spec, rec in recs.items():
        if f"{spec}|prebis-gear" not in fin:
            w0 = last["winners"].get(f"{spec}|raid") or last["winners"][f"{spec}|dummy"]
            g = rec["gear"]["prebis"] if SMOKE else MP.gear(rec, "prebis", flat_of(w0["allocation"]), "deep winner (bis)", w0["entry"], repo, db, zones)
            fin[f"{spec}|prebis-gear"] = g
            save(st)
        gear_path = fin[f"{spec}|prebis-gear"]["gear"]
        starts = [flat_of(last["winners"][f"{spec}|{s}"]["allocation"]) for s in SETTINGS]
        starts += [flat_of(x["winner"]["allocation"]) for kk, x in rec.get("search", {}).items() if kk.startswith("prebis") and x]
        for setting in SETTINGS:
            k = f"{spec}|prebis-{setting}"
            if k in fin:
                continue
            sr = search(cls, spec, entries, setting, gear_path, QUICK, starts, seed=900 + (1 if setting == "dummy" else 2))
            fin[k] = winner_of(sr, gear_path)
            save(st)
    # 4. final races and the ML records
    for spec, rec in recs.items():
        for tier, setting in [(t, st) for t in ("bis", "prebis") for st in SETTINGS]:
            k = f"{spec}|{tier}-{setting}-final"
            if k in fin:
                continue
            w = last["winners"][f"{spec}|{setting}"] if tier == "bis" else fin[f"{spec}|prebis-{setting}"]
            fin[k] = final_race(cls, spec, w, setting, w["gear"], repo)
            save(st)
        new = dict(rec)
        new["search"] = dict(rec.get("search", {}))
        for tier, setting in [(t, st) for t in ("bis", "prebis") for st in SETTINGS]:   # a setting not searched keeps the record's earlier winner
            w = last["winners"][f"{spec}|{setting}"] if tier == "bis" else fin[f"{spec}|prebis-{setting}"]
            f = fin[f"{spec}|{tier}-{setting}-final"]["deep winner"]
            new["search"][f"{tier}-{setting}"] = {"entry": w["entry"], "setting": setting, "date": TODAY, "deep": True,
                                                  "winner": {"allocation": w["allocation"], "split": w["split"], "dps": f["dps"], "se": f["se"],
                                                             "iterations": FINAL_FIGHTS},
                                                  "runner_up": w.get("runner_up"), "gap_to_runner_up": w.get("gap_to_runner_up"),
                                                  "runs": [{"run": i + 1} for i in range(w.get("runs", 0))], "runs_agree": w.get("runs_agree"),
                                                  "certificate": w.get("certificate"), "simulated_builds": w.get("simulated_builds"),
                                                  "protected": (last.get("records", {}).get(f"{spec}|{setting}") or {}).get("protected", [])}
        bis_rec = next((cc["gear_rec"][spec] for cc in reversed(st["cycles"]) if spec in cc.get("gear_rec", {})), None) or rec["gear"]["bis"]
        new["gear"] = dict(rec.get("gear", {}), bis=dict(bis_rec, gear=last["gear"][spec]), prebis=dict(fin[f"{spec}|prebis-gear"]))
        for k2 in ("aligned", "tidied", "parse", "builds", "compare"):
            new.pop(k2, None)
        new["deep"] = {"date": TODAY, "cycles": len(st["cycles"]), "converged": st.get("converged")}
        if SMOKE:
            continue
        MP.save(new)
        new["compare"] = MP.compare(new, repo)
        MP.save(new)
    st["minutes"] = round((time.time() - t_start) / 60, 1) + st.get("minutes", 0)
    save(st)
    if not SMOKE:
        report(cls, st, recs)
    log("== done")


def report(cls, st, recs):
    """<class>/research/raid/deep-optimization.md"""
    last = st["cycles"][-1]
    fin = st.get("final", {})
    o = [f"# {cls.capitalize()}: deep optimisation of the raid damage specs (generated)", "",
         f"> Generated by `_reference/data/raidsim/deep_opt.py` on {TODAY}; record `_reference/data/raidsim/deep/{cls}.json`. Do not hand-edit.", "",
         "Talents, gear and rotation were tuned in turns until none of them moved; every winner was then checked against every build one or two "
         "talent moves away and raced against all our builds of its spec over 200,000 fights. The community simulator's model of the beta "
         "(ElliotWood/Forever 40be98e with this project's patches), not in-game measurements. No search over this many builds can prove a "
         "global optimum; what the checks below rule out is a better build near the winner, and the independent runs show how often the "
         "search reaches the same top from different starts.", "",
         f"Cycles: {len(st['cycles'])}" + (f" (converged in cycle {st['converged']})" if st.get("converged") else " (the cycle limit)")
         + f"; rotations changed in cycle " + ", ".join(str(i + 1) for i, c in enumerate(st["cycles"]) if c.get("rotations_changed")) + ".", ""]
    for spec in recs:
        o += [f"## {SM.spec_name(cls, spec)}", "", "| Tier, setting | Talents | Rotation (entry) | DPS (200,000 fights) | Independent runs agreeing | Two-move check |",
              "|---|---|---|---|---|---|"]
        for tier, setting in (("bis", "dummy"), ("bis", "raid"), ("prebis", "dummy"), ("prebis", "raid")):
            w = last["winners"].get(f"{spec}|{setting}") if tier == "bis" else fin.get(f"{spec}|prebis-{setting}")
            f = (fin.get(f"{spec}|{tier}-{setting}-final") or {}).get("deep winner") or {}
            tm = (fin.get("two_move") or {}).get(f"{spec}|{setting}") if tier == "bis" else None
            tms = "-"
            if tm:
                s0 = tm["steps"][-1]
                tms = (f"{s0['one_move'] + s0['two_move']:,} builds; best {s0['confirmed'][0][1]:+.2%}" if s0.get("confirmed") else f"{s0['one_move'] + s0['two_move']:,} builds")
                tms += " (moved)" if tm["moved"] else ""
            if w:
                o.append(f"| {'Phase 1 BiS' if tier == 'bis' else 'Pre-BiS'}, {'training dummy' if setting == 'dummy' else 'full raid'} | "
                         f"[{w['split']}]({__import__('render_start_here').tf_link(cls, flat_of(w['allocation']))}) | {w['entry']} | "
                         f"{f.get('dps', 0):.1f} ± {f.get('se', 0):.2f} | {w.get('runs_agree')}/{w.get('runs')} | {tms} |")
        o.append("")
        for tier, setting in (("bis", "dummy"), ("bis", "raid")):
            race = fin.get(f"{spec}|{tier}-{setting}-final") or {}
            if race:
                o.append(f"Final race, {'training dummy' if setting == 'dummy' else 'full raid'} (BiS): "
                         + ", ".join(f"{k} {v['dps']:.1f}" for k, v in sorted(race.items(), key=lambda kv: -kv[1]["dps"])) + ".")
        o.append("")
    o += ["## Rotations", "", "| Entry | Cycle | Changed | Minutes |", "|---|---|---|---|"]
    for i, r in enumerate(st.get("rotations", []), 1):
        o.append(f"| {r['entry']} | {i} | {'yes' if r['changed'] else 'no'} | {r['minutes']} |")
    o.append("")
    p = paths.scenario_dir(cls, "raid") / "deep-optimization.md"
    p.write_text("\n".join(o) + "\n", encoding="utf-8")
    log(f"wrote {p.relative_to(ROOT).as_posix()}")


if __name__ == "__main__":
    main()
