"""One command for the whole leveling pipeline: (refresh ->) effects -> calibrate <-> optimize (to convergence) -> race -> report
-> sensitivity -> regenerate every derived page.

    python _reference/data/rebuild.py                       # every class, every step (hours: use --jobs)
    python _reference/data/rebuild.py warrior druid --jobs 2
    python _reference/data/rebuild.py --steps report,sensitivity,regen --fights-report 1000
    python _reference/data/rebuild.py --refresh 2026-10-15-beta-1.60.2.70100   # a new beta build first (see CLAUDE.md)
    python _reference/data/rebuild.py --dry-run             # print the commands only

Per class (its module's PIPELINE dict names the scorer model, the hand draft, the optimizer build, the levels and the lookahead):
  effects     scorer/effects.py <class>: re-parse the talent tooltips (cheap, always safe)
  calibrate   fightlab/calibrate.py over the hand draft, the optimizer build and every saved candidate
              (`<class>/research/leveling/fightlab/candidates/cand-<tag>-*.json`), then scorer/run.py for every spec/profile
              pair in `<class>/<scenario>/optimizer/`; if the optimizer's leveling build is new it is saved as the next
              candidate and the pair runs again, up to --rounds times (in-build marginals: one-build fits oscillate)
  race        fightlab/run.py: the hand draft against every candidate at every level (the sim decides; printed and logged)
  report      fightlab/run.py --write with --deltas and --gear-tiers for the optimizer build vs the hand draft (+ extra reports)
  sensitivity fightlab/sensitivity.py --write for the optimizer build and the hand draft
  adopt       (opt-in) if the race winner beats the hand draft by more than RACE_MARGIN (2%, level-weighted mean time per
              kill), the hand draft takes the winner's allocation and order before the report runs (the old draft is saved
              as a candidate; core/flex are rebuilt from the sim's talent values, notes and open questions are kept)
  variants    the module's PIPELINE["variants"] (a spec model run with table overrides, e.g. the mage's AoE grinding profile with
              4 mobs per pull): calibrate <-> optimize for that model and profile, race the candidates, promote the fastest into
              the opt-* build, report and sensitivity, all under the variant's overrides
  raid        (with adopt: a raid winner over 2% ahead of the best hand raid draft is adopted into that draft; the loop also
              stops when a new build is not 1% better in a quick race)
              level-60 raid builds through the community simulator (raidsim/): for every DPS spec model of the class in
              raidsim/specs.json, calibrate the scorer's raid values to the simulator (raidsim/calibrate.py), re-run the
              optimizer for the raid profile, save a changed build as raidsim/candidates/cand-<spec>-rN.json and repeat once,
              then race every build and the simulator's presets (raidsim/run.py --write); an earlier round's build that beats
              the last export in the race is promoted into the opt-* build (the export is the best of its rounds); needs raidsim/setup.py once
  classic     our Classic-era raid builds through the upstream wowsims/classic simulator (raidsim/specs-classic.json from the clone's
              presets; needs raidsim/setup.py --game classic once): the Classic damage split and raid-mode effect fits go into the
              scorer's classic-era game, reports under <class>/research/talents/classic-baseline/raidsim/, then (once) scorer/classic_check.py
              --write asks whether the Classic models still reproduce the community builds
  regen       (once) render_fightlab_sections, render_raidsim_sections, validate_builds, render_builds, render_new_builds, render_modes, render_tier_list, respec, render_optimizer_sections,
              compare_effects, loop_audit, the launch / beta checklists and fightlab/summary.py (the cross-class page)

The race metric is the mean time per kill over the report levels weighted by level (a level-60 bracket counts three
times a level-20 one: an approximation of the time spent per bracket). The calibration loop also stops when a new
optimizer build is not at least RACE_NOISE (1%) faster than the best build so far (a quick race), so builds that differ
by noise do not cycle.

Everything runs as subprocesses of this interpreter from the project root; `--jobs N` runs N classes at once (their files
are disjoint). The outcome per class (rounds, convergence, race winner, kill times) is written to
`_reference/data/fightlab/last-rebuild.json`, which the summary page reads.
"""
import argparse
import concurrent.futures
import datetime
import glob
import json
import os
import pathlib
import re
import subprocess
import sys
import time

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[1]
FL = HERE / "fightlab"
sys.path.insert(0, str(FL))
import paths  # noqa: E402
CLASSES = ["mage", "priest", "warlock", "hunter", "warrior", "rogue", "paladin", "shaman", "druid"]
PROFILES = ["leveling-st", "leveling-aoe", "solo-60", "raid-dps-extwc", "raid-dps", "raid-heal", "raid-tank"]
STEPS = ["effects", "calibrate", "race", "adopt", "report", "sensitivity", "variants", "raid", "classic", "heal", "regen"]
HL = HERE / "heallab"
HEALERS = {"priest": "priest", "paladin": "paladin", "shaman": "shaman", "druid": "druid"}
LOG = FL / "last-rebuild.json"
RACE_MARGIN = 0.02    # adopt the race winner only when it beats the hand draft by more than this (weighted mean time per kill)
RACE_NOISE = 0.01     # calibration stop rule: a new build must beat the best so far by more than this


def weighted_mean(per_level):
    """Level-weighted mean of {level: time per kill}: weight = level / 10 (60 counts 3x a 20)."""
    tot = sum(int(L) / 10 for L in per_level)
    return sum(v * int(L) / 10 for L, v in per_level.items()) / tot if tot else 0.0


def race_table(stdout, hand):
    race = parse_race(stdout)
    means = {(hand if b == "main" else pathlib.Path(b).stem): weighted_mean(v) for b, v in race.items() if v}
    return race, means


def pipeline(cls):
    from run import MODULES
    mod = __import__(MODULES[cls][0])
    return dict(mod.PIPELINE)


def sh(args, dry, log, timeout=None):
    """Run one command from the project root; returns (rc, stdout). Prints a one-line summary."""
    cmd = [sys.executable] + [str(a) for a in args]
    line = " ".join(a if " " not in a else f'"{a}"' for a in cmd[1:])
    if dry:
        print("  $", line)
        return 0, ""
    t = time.time()
    env = dict(os.environ, PYTHONIOENCODING="utf-8")
    r = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace", cwd=str(ROOT), env=env, timeout=timeout)
    dt = time.time() - t
    tail = [l for l in r.stdout.splitlines() if l.strip()][-1:] or [""]
    print(f"  [{dt:5.0f}s rc={r.returncode}] {line[:110]} | {tail[0][:100]}")
    log.append({"cmd": line, "rc": r.returncode, "seconds": round(dt), "tail": r.stdout.splitlines()[-12:], "stderr": r.stderr.splitlines()[-8:] if r.returncode else []})
    if r.returncode:
        print("    stderr:", "\n    ".join(r.stderr.splitlines()[-6:]))
    return r.returncode, r.stdout


def alloc_of(build):
    return {n: r for items in build["allocation"].values() for n, r in items}


def load_build(cls, bid):
    from run import load_build as lb
    return lb(cls, bid)


def candidates(cls, tag):
    return sorted(glob.glob(str(paths.fightlab_dir(cls) / "candidates" / f"cand-{tag}-*.json")))


def optimizer_pairs(cls):
    pairs = []
    for f in sorted(p for sc in paths.SCENARIOS for p in (paths.scenario_dir(cls, sc) / "optimizer").glob("*.md")):
        for p in PROFILES:
            if f.stem.endswith("-" + p):
                pairs.append((f.stem[: -len(p) - 1], p))
                break
    return pairs


def save_candidate(cls, tag, build):
    folder = paths.fightlab_dir(cls) / "candidates"
    folder.mkdir(parents=True, exist_ok=True)
    n = 1
    while (folder / f"cand-{tag}-r{n}.json").exists():
        n += 1
    path = folder / f"cand-{tag}-r{n}.json"
    entry = {"id": path.stem, "allocation": build["allocation"], "order": build.get("order", []),
             "note": f"Optimizer build saved by rebuild.py on {datetime.date.today().isoformat()} (calibration round {n})"}
    path.write_text(json.dumps(entry, indent=1, ensure_ascii=False), encoding="utf-8")
    return path


def parse_race(stdout):
    """time per kill per build per level from run.py's console output."""
    out, level = {}, None
    for line in stdout.splitlines():
        if line.startswith("L") and "time/kill" in line and ":" in line[:5]:
            level = int(line[1:line.index(":")])
            tpk = float(line.split("time/kill ")[1].split("s")[0])
            out.setdefault("main", {})[level] = tpk
        elif line.strip().startswith("vs ") and "time/kill" in line:
            bid = line.strip()[3:].split(":")[0]
            tpk = float(line.split("time/kill ")[1].split("s")[0])
            out.setdefault(bid, {})[level] = tpk
    return out


def run_class(cls, a):
    P = pipeline(cls)
    spec, hand, opt, tag = P["spec"], P["hand"], P["opt"], P["tag"]
    levels, cal_levels = P["levels"], P["calibrate_levels"]
    log, result = [], {"class": cls, "spec": spec, "hand": hand, "opt": opt, "started": datetime.datetime.now().isoformat(timespec="seconds"), "steps": a.steps}
    print(f"== {cls}: {spec} ({hand} vs {opt}), steps {','.join(a.steps)}")
    t0 = time.time()
    if "effects" in a.steps:
        sh([HERE / "scorer/effects.py", cls], a.dry_run, log)
    if "calibrate" in a.steps:
        rounds = []
        for rnd in range(1, a.rounds + 1):
            cands = candidates(cls, tag)
            sh([FL / "calibrate.py", cls, "--spec", spec, "--profile", "leveling-st", "--builds", opt, hand, *cands, "--levels", cal_levels,
                "--fights", a.fights_calibrate, "--write"], a.dry_run, log)
            before = alloc_of(load_build(cls, opt)) if not a.dry_run else {}
            for s, p in optimizer_pairs(cls):
                seeds = ["--seed", hand] if (s, p) == (spec, "leveling-st") else []   # the hand draft seeds the search
                sh([HERE / "scorer/run.py", cls, "--spec", s, "--profile", p, "--write", "--export", "--lookahead", P["lookahead"], *seeds], a.dry_run, log)
            if a.dry_run:
                break
            after = load_build(cls, opt)
            known = [alloc_of(load_build(cls, c)) for c in cands] + [before]
            new = alloc_of(after) not in known
            rounds.append({"round": rnd, "new_build": new, "allocation": after["allocation"]})
            if not new:
                print(f"  round {rnd}: the optimizer's {opt} matches a calibrated build: converged")
                break
            path = save_candidate(cls, tag, after)
            # quick race: stop when the new build is not clearly faster than the best build so far
            rc, out = sh([FL / "run.py", cls, "--spec", spec, "--build", hand, "--compare", *candidates(cls, tag), "--levels", levels,
                          "--fights", max(300, a.fights_race // 2)], a.dry_run, log)
            if rc == 0:
                race, means = race_table(out, hand)
                new_t = means.get(path.stem)
                best_prev = min(v for k, v in means.items() if k != path.stem) if len(means) > 1 else None
                rounds[-1]["quick_race"] = means
                if new_t is not None and best_prev is not None and new_t > best_prev * (1 - RACE_NOISE):
                    print(f"  round {rnd}: new {opt} saved as {path.name} but not {RACE_NOISE:.0%} faster than the best so far "
                          f"({new_t:.1f}s vs {best_prev:.1f}s): converged by noise")
                    rounds[-1]["converged_by_noise"] = True
                    break
            print(f"  round {rnd}: new {opt} saved as {path.name}; calibrating again")
        result["rounds"] = rounds
        result["converged"] = bool(rounds) and (not rounds[-1]["new_build"] or rounds[-1].get("converged_by_noise", False))
    if "race" in a.steps:
        cands = candidates(cls, tag)
        rc, out = sh([FL / "run.py", cls, "--spec", spec, "--build", hand, "--compare", *cands, "--levels", levels, "--fights", a.fights_race], a.dry_run, log)
        if not a.dry_run and rc == 0:
            race, means = race_table(out, hand)
            winner = min(means, key=means.get) if means else None
            hand_t = means.get(hand)
            gain = (hand_t - means[winner]) / hand_t if winner and hand_t else 0.0
            recommended = winner if (winner != hand and gain >= RACE_MARGIN) else hand
            result["race"] = {"time_per_kill": {(hand if b == "main" else pathlib.Path(b).stem): v for b, v in race.items()}, "mean": means,
                              "winner": winner, "gain_vs_hand": round(gain, 4), "recommended": recommended, "margin": RACE_MARGIN,
                              "candidate_files": {pathlib.Path(c).stem: c for c in cands}}
            print(f"  race (level-weighted): " + ", ".join(f"{b} {m:.1f}s" for b, m in sorted(means.items(), key=lambda kv: kv[1]))
                  + f" | recommended: {recommended}" + (f" ({gain:+.1%} vs the hand draft)" if winner != hand else ""))
    if "adopt" in a.steps and not a.dry_run:
        race = result.get("race") or (json.load(open(LOG, encoding="utf-8")).get("classes", {}).get(cls, {}).get("race") if LOG.exists() else None)
        if race and race.get("recommended") and race["recommended"] != hand:
            result["adopted"] = adopt(cls, P, race, a, log)
        else:
            print(f"  adopt: the hand draft {hand} stands" + (f" (winner {race['winner']} is only {race['gain_vs_hand']:+.1%} faster)" if race and race.get("winner") != hand else ""))
    if "report" in a.steps:
        extra = P.get("compare_extra", [])
        sh([FL / "run.py", cls, "--spec", spec, "--build", opt, "--compare", hand, *extra, "--levels", levels, "--fights", a.fights_report,
            "--deltas", ",".join(x for x in cal_levels.split(",") if int(x) >= 30), "--gear-tiers", "--write"], a.dry_run, log)
        for er in P.get("extra_reports", []):
            sh([FL / "run.py", cls, "--spec", er["spec"], "--build", er["build"], *(["--compare", *er["compare"]] if er.get("compare") else []),
                "--levels", levels, "--fights", a.fights_report, "--deltas", "30,60", "--write"], a.dry_run, log)
            if not a.dry_run and er.get("compare"):
                abs_dps_factor(cls, spec, er["spec"], log)
        if not a.dry_run:
            rep = json.load(open(paths.fightlab_dir(cls) / f"{spec}.json", encoding="utf-8"))
            result["time_per_kill"] = {L: round(r["time_per_kill"], 1) for L, r in rep["levels"].items()}
            result["hand_time_per_kill"] = {L: round(r["time_per_kill"], 1) for L, r in rep["compare"].get(hand, {}).items()}
    if "sensitivity" in a.steps:
        sh([FL / "sensitivity.py", cls, "--spec", spec, "--builds", opt, hand, "--levels", "30,60", "--fights", a.fights_sensitivity, "--write"], a.dry_run, log)
    if "variants" in a.steps:
        for V in P.get("variants", []):
            run_variant(cls, V, a, log, result)
    if "raid" in a.steps:
        raid_step(cls, a, log, result)
    if "classic" in a.steps:
        classic_step(cls, a, log, result)
    if "heal" in a.steps and cls in HEALERS:
        heal_step(cls, a, log, result)
    result["seconds"] = round(time.time() - t0)
    result["log"] = log
    result["failed"] = [l["cmd"][:80] for l in log if l["rc"]]
    print(f"== {cls} done in {result['seconds']}s" + (f", FAILED: {result['failed']}" if result["failed"] else ""))
    return result


def adopt(cls, P, race, a, log):
    """Move the race winner's allocation and order into the hand draft; keep the old draft as a candidate; rebuild core/flex
    from the sim's talent values (a fresh --deltas run for the adopted build); keep notes, sources and open questions."""
    hand, tag, spec = P["hand"], P["tag"], P["spec"]
    winner = race["recommended"]
    cand_path = race["candidate_files"].get(winner)
    if cand_path and not pathlib.Path(cand_path).exists():   # a race stored before the 2026-09-27 layout: same file, new folder
        # the file name by either separator: races stored by the Windows sessions keep "F:\\..." paths, which pathlib on Linux reads as one name
        moved = paths.fightlab_dir(cls) / "candidates" / pathlib.PureWindowsPath(cand_path).name
        cand_path = str(moved) if moved.exists() else cand_path
    if not cand_path:
        print(f"  adopt: no candidate file for {winner}")
        return None
    win = json.load(open(cand_path, encoding="utf-8"))
    bp = ROOT / cls / "research/talents/forever/proposed-builds.json"
    data = json.load(open(bp, encoding="utf-8"))
    b = next(x for x in data["builds"] if x["id"] == hand)
    if alloc_of(win) == alloc_of(b):   # a stored race whose winner is already the hand draft: nothing to adopt
        print(f"  adopt: {hand} already has {winner}'s allocation")
        return None
    today = datetime.date.today().isoformat()
    # keep the old draft as a candidate (unless an identical allocation is already saved)
    old_alloc = alloc_of(b)
    folder = paths.fightlab_dir(cls) / "candidates"
    if old_alloc not in [alloc_of(json.load(open(c, encoding="utf-8"))) for c in candidates(cls, tag)]:
        keep = folder / f"cand-{tag}-hand-{today}.json"
        keep.write_text(json.dumps({"id": keep.stem, "allocation": b["allocation"], "order": b.get("order", []),
                                    "note": f"The hand draft {hand} as it was before {winner} was adopted on {today}"}, indent=1, ensure_ascii=False), encoding="utf-8")
        print(f"  adopt: previous draft saved as {keep.name}")
    # sim values of the adopted build at 60 (and 30) for core / flex
    rc, out = sh([FL / "run.py", cls, "--spec", spec, "--build", cand_path, "--levels", "30,60", "--fights", max(500, a.fights_report // 3), "--deltas", "30,60"], False, log)
    vals = {}
    level = None
    for line in out.splitlines():
        if line.startswith("-- talent values at level"):
            level = int(line.split("level ")[1].split()[0])
        elif level and "  sim " in line and line.strip():
            name = line[:27].strip()
            try:
                vals.setdefault(name, {})[level] = float(line.split("sim ")[1].split("%")[0]) / 100
            except ValueError:
                pass
    new_alloc = alloc_of(win)
    old_why = {c["talent"]: c["why"] for c in b.get("core", []) if c.get("talent") in new_alloc}
    ranked = sorted(new_alloc, key=lambda n: -vals.get(n, {}).get(60, 0.0))
    core = []
    for n in ranked[:8]:
        v60, v30 = vals.get(n, {}).get(60), vals.get(n, {}).get(30)
        sim = (f"Fight lab ({today}): removing it costs {v60:+.0%} time per kill at 60" + (f", {v30:+.0%} at 30" if v30 is not None else "") + ".") if v60 is not None else ""
        core.append({"talent": n, "why": (old_why.get(n, "") + " " + sim).strip()})
    flex = []
    for n in ranked:
        v60, v30 = vals.get(n, {}).get(60), vals.get(n, {}).get(30)
        if v60 is not None and abs(v60) < 0.01 and (v30 is None or abs(v30) < 0.01) and n not in ranked[:8]:
            flex.append({"points": new_alloc[n], "default": n, "alternatives": ["any utility talent legal at that tier"],
                         "why": f"Measures {v60:+.1%} time per kill at 60" + (f" and {v30:+.1%} at 30" if v30 is not None else "") + " in the fight lab (noise): these points are free to move."})
    gain = race.get("gain_vs_hand", 0.0)
    b["allocation"] = win["allocation"]
    if win.get("order"):
        b["order"] = win["order"]
    b["core"], b["flex"] = core, flex
    base_name = b["name"].split(" (")[0]
    b["name"] = f"{base_name} (fight-lab winner adopted {today})"
    b["summary"] = (f"Allocation and order adopted on {today} from `{winner}`, the fastest build in the fight-lab race over levels {P['levels'].replace(',', '/')} "
                    f"({gain:+.1%} vs the previous draft, level-weighted time per kill; the previous draft is kept under leveling/fightlab/candidates/). "
                    "Core talents are ranked by the sim's removal cost at 60. Previous summary: " + b["summary"])
    b["notes"] = [f"Adopted from the fight-lab race on {today}: {winner} beat the previous draft by {gain:+.1%} (level-weighted time per kill); "
                  "the rationale below the fight-lab note predates the adoption where it names talents no longer taken."] + b.get("notes", [])
    data["builds"] = [x if x["id"] != hand else b for x in data["builds"]]
    json.dump(data, open(bp, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    subprocess.run([sys.executable, str(HERE / "fmt_json.py"), str(bp)], check=True, capture_output=True)
    print(f"  adopt: {hand} <- {winner} ({gain:+.1%}); core {len(core)}, flex {len(flex)}")
    return {"winner": winner, "gain": gain, "date": today}


def run_variant(cls, V, a, log, result):
    """A spec model run under table overrides (V["sets"]): calibrate <-> optimize, race the candidates, promote the fastest
    into the opt-* build, then report and sensitivity."""
    spec, opt, tag, profile = V["spec"], V["opt"], V["tag"], V["profile"]
    sets = sum([["--set", x] for x in V.get("sets", [])], [])
    levels, cal_levels = V.get("levels", "30,40,50,60"), V.get("calibrate_levels", "40,60")
    print(f"  variant {spec} ({V.get('label', profile)})")
    if not a.dry_run:
        try:
            load_build(cls, opt)
        except (StopIteration, SystemExit, KeyError):   # a new variant: export the optimizer's build first so the calibration has something to fit
            sh([HERE / "scorer/run.py", cls, "--spec", spec, "--profile", profile, "--write", "--export", "--lookahead", V.get("lookahead", 16)], a.dry_run, log)
    rounds = []
    for rnd in range(1, a.rounds + 1):
        cands = candidates(cls, tag)
        before = alloc_of(load_build(cls, opt)) if not a.dry_run else {}
        share = []   # a variant may name the build its damage split is measured on (a pet build when the optimizer's may take Lone Wolf)
        if V.get("share_build"):
            sb = paths.fightlab_dir(cls) / "candidates" / f"{V['share_build']}.json"
            share = ["--share-build", str(sb) if sb.exists() else V["share_build"]]
        sh([FL / "calibrate.py", cls, "--spec", spec, "--profile", profile, "--builds", opt, *cands, "--levels", cal_levels, "--fights", a.fights_calibrate, "--write", *share, *sets], a.dry_run, log)
        sh([HERE / "scorer/run.py", cls, "--spec", spec, "--profile", profile, "--write", "--export", "--lookahead", V.get("lookahead", 16),
            *(["--seed", *V["seeds"]] if V.get("seeds") else [])], a.dry_run, log)
        if a.dry_run:
            break
        after = load_build(cls, opt)
        known = [alloc_of(load_build(cls, c)) for c in cands] + [before]
        new = alloc_of(after) not in known
        rounds.append({"round": rnd, "new_build": new})
        if not new:
            print(f"  {spec}: the optimizer's {opt} matches a calibrated build: converged")
            break
        path = save_candidate(cls, tag, after)
        rc, out = sh([FL / "run.py", cls, "--spec", spec, "--build", opt, "--compare", *cands, "--levels", levels, "--fights", max(300, a.fights_race // 2), *sets], a.dry_run, log)
        if rc == 0:
            race = parse_race(out)
            means = {(opt if b == "main" else pathlib.Path(b).stem): weighted_mean(v) for b, v in race.items() if v}
            new_t = means.get(opt)
            best_prev = min([v for k, v in means.items() if k != opt], default=None)
            rounds[-1]["quick_race"] = means
            if new_t is not None and best_prev is not None and new_t > best_prev * (1 - RACE_NOISE):
                print(f"  {spec}: new {opt} saved as {path.name} but not {RACE_NOISE:.0%} faster than the best so far ({new_t:.1f}s vs {best_prev:.1f}s): converged by noise")
                rounds[-1]["converged_by_noise"] = True
                break
        print(f"  {spec}: new {opt} saved as {path.name}; calibrating again")
    cands = candidates(cls, tag)
    promoted = None
    if cands and not a.dry_run:
        rc, out = sh([FL / "run.py", cls, "--spec", spec, "--build", opt, "--compare", *cands, "--levels", levels, "--fights", a.fights_race, *sets], a.dry_run, log)
        if rc == 0:
            race = parse_race(out)
            means = {(opt if b == "main" else pathlib.Path(b).stem): weighted_mean(v) for b, v in race.items() if v}
            best = min(means, key=means.get)
            if best != opt and means[best] < means[opt] * (1 - RACE_NOISE):
                cand = json.load(open(paths.fightlab_dir(cls) / "candidates" / f"{best}.json", encoding="utf-8"))
                bp = ROOT / cls / "research/talents/forever/proposed-builds.json"
                data = json.load(open(bp, encoding="utf-8"))
                for b in data["builds"]:
                    if b["id"] == opt:
                        b["allocation"] = cand["allocation"]
                        if cand.get("order"):
                            b["order"] = cand["order"]
                        b["notes"] = [f"Allocation and order taken from {best} on {datetime.date.today().isoformat()}: an earlier optimizer round beat the last export in the fight lab "
                                      f"({means[best]:.1f}s vs {means[opt]:.1f}s per kill, level-weighted)."] + [n for n in b.get("notes", []) if not n.startswith("Allocation and order taken from")]
                json.dump(data, open(bp, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
                subprocess.run([sys.executable, str(HERE / "fmt_json.py"), str(bp)], check=True, capture_output=True)
                promoted = best
                print(f"  {spec}: {opt} <- {best} ({means[best]:.1f}s vs {means[opt]:.1f}s)")
            print(f"  {spec} race (level-weighted): " + ", ".join(f"{b} {m:.1f}s" for b, m in sorted(means.items(), key=lambda kv: kv[1])))
    report = V.get("report") or (spec if spec != pipeline(cls)["spec"] else f"{spec}-{tag}")   # a variant of the main model keeps its own report
    sh([FL / "run.py", cls, "--spec", spec, "--build", opt, *(["--compare", *cands[-2:]] if cands else []), "--levels", levels, "--fights", a.fights_report,
        "--deltas", ",".join(x for x in cal_levels.split(",") if int(x) >= 30), "--write", "--name", report, *sets], a.dry_run, log)
    if V.get("sensitivity", spec != pipeline(cls)["spec"]):   # the class's sensitivity page belongs to the main model
        sh([FL / "sensitivity.py", cls, "--spec", spec, "--builds", opt, "--levels", cal_levels, "--fights", a.fights_sensitivity, "--write", *sets], a.dry_run, log)
    result.setdefault("variants", {})[report] = {"spec": spec, "rounds": rounds, "promoted": promoted, "sets": V.get("sets", [])}


def raid_step(cls, a, log, result):
    """Calibrate <-> optimize <-> race for the class's raid DPS spec models in the community simulator."""
    specs = json.load(open(HERE / "raidsim/specs.json", encoding="utf-8")).get(cls, {})
    rs = HERE / "raidsim"
    out = {}
    for spec, entry in specs.items():
        profile = entry.get("profile", "raid-dps")
        if profile not in ("raid-dps", "raid-tank") or entry.get("rotation_only"):   # rotation-only trees: raced by apl_opt.py and run.py only
            continue
        tank = bool(entry.get("tank"))
        unit = "tank value" if tank else "DPS"
        opt_id = f"opt-{spec}-{profile}"
        folder = paths.raidsim_dir(cls) / "candidates"
        folder.mkdir(parents=True, exist_ok=True)
        # the simulator's presets within reach of our best build compete: calibrated with ours, seeding the optimizer, raced, adoptable
        sh([rs / "run.py", cls, "--spec", spec, "--preset-candidates"], a.dry_run, log)
        presets = sorted(str(p) for p in folder.glob(f"cand-{spec}-preset-*.json"))
        rounds = []
        for rnd in range(1, a.raid_rounds + 1):
            cands = sorted(str(p) for p in folder.glob(f"cand-{spec}-*.json"))
            before = alloc_of(load_build(cls, opt_id)) if not a.dry_run else {}
            sh([rs / "calibrate.py", cls, "--spec", spec, "--iterations", a.iterations_calibrate, "--write"], a.dry_run, log)
            hands = [b for b in entry["builds"] if not b.startswith("opt-")]   # the hand raid drafts seed the search
            sh([HERE / "scorer/run.py", cls, "--spec", spec, "--profile", profile, "--write", "--export", *(["--seed", *hands, *presets] if hands or presets else [])], a.dry_run, log)
            if a.dry_run:
                break
            after = load_build(cls, opt_id)
            known = [alloc_of(json.load(open(c, encoding="utf-8"))) for c in cands] + [before]
            new = alloc_of(after) not in known
            rounds.append({"round": rnd, "new_build": new})
            if not new:
                print(f"  {spec}: the optimizer's {opt_id} matches a calibrated build: converged")
                break
            n = 1
            while (folder / f"cand-{spec}-r{n}.json").exists():
                n += 1
            path = folder / f"cand-{spec}-r{n}.json"
            path.write_text(json.dumps({"id": path.stem, "allocation": after["allocation"], "note": f"Optimizer raid build saved by rebuild.py on {datetime.date.today().isoformat()} (raid calibration round {rnd})"}, indent=1, ensure_ascii=False), encoding="utf-8")
            # quick race: stop when the new build is not clearly faster than the best optimizer build so far
            rc, so = sh([rs / "run.py", cls, "--spec", spec, "--builds", opt_id, *cands, "--iterations", max(500, a.iterations_race // 3), "--no-presets"], a.dry_run, log)
            if rc == 0:
                dps = {}
                for line in so.splitlines():
                    m = re.match(r"\s+(\S+)\s+(?:\S+\s+)?DPS\s+([0-9.]+)" + (r".*tank-value\s+([0-9.]+)" if tank else ""), line)
                    if m:
                        dps[m.group(1)] = float(m.group(3) if tank else m.group(2))
                new_d = dps.get(opt_id)
                best_prev = max([v for k, v in dps.items() if k != opt_id], default=None)
                rounds[-1]["quick_race"] = dps
                if new_d is not None and best_prev is not None and new_d < best_prev * (1 + RACE_NOISE):
                    print(f"  {spec}: new {opt_id} saved as {path.name} but not {RACE_NOISE:.0%} better than the best so far ({new_d:.3g} vs {best_prev:.3g} {unit}): converged by noise")
                    rounds[-1]["converged_by_noise"] = True
                    break
            print(f"  {spec}: new {opt_id} saved as {path.name}; calibrating again")
        cands = sorted(str(p) for p in folder.glob(f"cand-{spec}-*.json"))
        rc, so = sh([rs / "run.py", cls, "--spec", spec, "--builds", *entry["builds"], *cands, "--iterations", a.iterations_race, "--write"], a.dry_run, log)
        best, promoted = None, None
        if not a.dry_run and rc == 0:
            rep = json.load(open(paths.raidsim_dir(cls) / f"{spec}.json", encoding="utf-8"))
            key = (lambda x: x.get("value") or 0) if tank else (lambda x: x["dps"])
            ranked = sorted([x for x in rep["results"] if x.get("dps")], key=lambda x: -key(x))
            best = [(x["label"], round(key(x), 3 if tank else 1)) for x in ranked[:4]]
            print(f"  {spec}: " + ", ".join(f"{l} {d}" for l, d in best))
            # the optimizer's exported build is the best of its own rounds: promote an earlier candidate that beat the last export
            mine = [x for x in ranked if x["label"] == opt_id or x["label"].startswith(f"cand-{spec}-r")]   # the optimizer's rounds only
            opt_row = next((x for x in mine if x["label"] == opt_id), None)
            if mine and opt_row and mine[0]["label"] != opt_id and key(mine[0]) > key(opt_row) * 1.005:
                win = mine[0]["label"]
                cand = json.load(open(folder / f"{win}.json", encoding="utf-8"))
                bp = ROOT / cls / "research/talents/forever/proposed-builds.json"
                data = json.load(open(bp, encoding="utf-8"))
                for b in data["builds"]:
                    if b["id"] == opt_id:
                        b["allocation"] = cand["allocation"]
                        b["notes"] = [f"Allocation taken from {win} on {datetime.date.today().isoformat()}: the optimizer's earlier round beat its last export in the community simulator "
                                      f"({key(mine[0]):.3g} vs {key(opt_row):.3g} {unit}; the calibration moved the model past the better build)."] + [n for n in b.get("notes", []) if not n.startswith("Allocation taken from")]
                json.dump(data, open(bp, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
                subprocess.run([sys.executable, str(HERE / "fmt_json.py"), str(bp)], check=True, capture_output=True)
                promoted = win
                print(f"  {spec}: {opt_id} <- {win} ({key(mine[0]):.3g} vs {key(opt_row):.3g} {unit}); racing again")
                sh([rs / "run.py", cls, "--spec", spec, "--builds", *entry["builds"], *cands, "--iterations", a.iterations_race, "--write"], a.dry_run, log)
        adopted = None
        if "adopt" in a.steps and not a.dry_run and rc == 0:
            adopted = adopt_raid(cls, spec, entry, opt_id, folder, a, log)
            if adopted:
                sh([rs / "run.py", cls, "--spec", spec, "--builds", *entry["builds"], *cands, "--iterations", a.iterations_race, "--write"], a.dry_run, log)
        env = None
        if not tank:   # the parse build (personal DPS only) and the DPS-by-environment table: dummy / raid / maximum
            parse_id = f"opt-{spec}-parse"
            sh([HERE / "scorer/run.py", cls, "--spec", spec, "--profile", "parse", "--write", "--export", *(["--seed", *hands] if hands else [])], a.dry_run, log)
            rc2, so2 = sh([rs / "run.py", cls, "--spec", spec, "--env", "environments", "--builds", *entry["builds"], parse_id, "--iterations", a.iterations_race, "--write"], a.dry_run, log)
            if not a.dry_run and rc2 == 0:
                rep_env = paths.raidsim_dir(cls) / f"{spec}-environments.json"
                if rep_env.exists():
                    env = {x["label"]: x["dps"] for x in json.load(open(rep_env, encoding="utf-8"))["results"]}
        out[spec] = {"rounds": rounds, "top": best, "promoted": promoted, "adopted": adopted, "environments": env}
    result["raid"] = out


def adopt_raid(cls, spec, entry, opt_id, folder, a, log):
    """If the best optimizer build (opt or a saved candidate) beats the best hand raid draft of the spec by more than
    RACE_MARGIN in the simulator, the hand draft takes its allocation (old draft saved as a candidate; core/flex from the
    simulator's removal values; notes, sources and open questions kept)."""
    rep_path = paths.raidsim_dir(cls) / f"{spec}.json"
    rep = json.load(open(rep_path, encoding="utf-8"))
    rows = {x["label"]: x for x in rep["results"] if x.get("dps")}
    hands = [b for b in entry["builds"] if not b.startswith("opt-") and b in rows]
    # the simulator's presets saved as candidates (raidsim/run.py --preset-candidates) race under their own "sim preset: X" label
    preset_files = {}
    for f in folder.glob(f"cand-{spec}-preset-*.json"):
        preset_files["sim preset: " + json.load(open(f, encoding="utf-8"))["preset"]] = f
    ours = [k for k in rows if k == opt_id or k.startswith(f"cand-{spec}-r") or k in preset_files]
    if not hands or not ours:
        return None
    key = (lambda x: x.get("value") or 0) if entry.get("tank") else (lambda x: x["dps"])
    unit = "tank value" if entry.get("tank") else "DPS"
    hand = max(hands, key=lambda b: key(rows[b]))
    win = max(ours, key=lambda b: key(rows[b]))
    gain = (key(rows[win]) - key(rows[hand])) / key(rows[hand])
    if gain < RACE_MARGIN:
        print(f"  {spec}: the hand draft {hand} stands ({win} is only {gain:+.1%} ahead)")
        return None
    bp = ROOT / cls / "research/talents/forever/proposed-builds.json"
    data = json.load(open(bp, encoding="utf-8"))
    b = next(x for x in data["builds"] if x["id"] == hand)
    win_file = preset_files.get(win) or (folder / f"{win}.json")
    src = next(x for x in data["builds"] if x["id"] == opt_id) if win == opt_id else json.load(open(win_file, encoding="utf-8"))
    preset = src.get("preset") if win != opt_id else None
    today = datetime.date.today().isoformat()
    keep = folder / f"cand-{spec}-hand-{today}.json"
    if not keep.exists():
        keep.write_text(json.dumps({"id": keep.stem, "allocation": b["allocation"], "note": f"The hand draft {hand} as it was before {win} was adopted on {today}"}, indent=1, ensure_ascii=False), encoding="utf-8")
    # talent values of the adopted allocation in the simulator (removal runs) for core / flex
    rc, so = sh([HERE / "raidsim/run.py", cls, "--spec", spec, "--builds", str(win_file) if win != opt_id else opt_id,
                 "--iterations", max(800, a.iterations_race // 3), "--no-presets", "--deltas", "all"], False, log)
    vals, apl = {}, set()
    for line in so.splitlines():
        m = re.match(r"\s+(.+?)\s+(\d)\s+sim\s+([+-][0-9.]+)%", line)
        if m:
            vals[m.group(1).strip()] = float(m.group(3)) / 100
            if "rotation-dependent" in line:   # the removal run measures a broken rotation (run.py apl_talents), not the talent
                apl.add(m.group(1).strip())
    new_alloc = alloc_of(src)
    old_why = {c["talent"]: c["why"] for c in b.get("core", []) if c.get("talent") in new_alloc}
    ranked = sorted(new_alloc, key=lambda n: -vals.get(n, 0.0))
    def sim_why(n):
        if n in apl:
            return f" Raid sim ({today}): the simulator's rotation reads this talent's own proc, so its removal run breaks the rotation and is not its value."
        return f" Raid sim ({today}): removing it costs {vals[n]:+.0%} {unit}." if n in vals else ""
    core = [{"talent": n, "why": (old_why.get(n, "") + sim_why(n)).strip()} for n in ranked[:8]]
    flex = [{"points": new_alloc[n], "default": n, "alternatives": ["any utility talent legal at that tier"],
             "why": f"Measures {vals[n]:+.1%} DPS in the community simulator (noise): these points are free to move."} for n in ranked[8:] if n in vals and abs(vals[n]) < 0.01]
    b["allocation"] = src["allocation"]
    b["core"], b["flex"] = core, flex
    b["name"] = f"{b['name'].split(' (')[0]} (simulator winner adopted {today})"
    what = f"the community simulator's own preset '{preset}'" if preset else f"`{win}`"
    b["summary"] = (f"Allocation adopted on {today} from {what}, the best build in the community simulator ({gain:+.1%} {unit} vs the previous draft with the simulator's "
                    f"gear, rotation and buffs; the previous draft is kept under raid/raidsim/candidates/). Core talents are ranked by the simulator's removal cost. "
                    "Previous summary: " + b["summary"])
    b["notes"] = [f"Adopted from the community simulator on {today}: {what} beat the previous draft by {gain:+.1%} {unit}; the rationale below predates the adoption where it names talents no longer taken."] + b.get("notes", [])
    if preset:   # credit the preset's source
        url = f"https://github.com/ElliotWood/Forever/blob/master/ui/specs/{entry['sim_spec']}/presets.ts"
        if url not in (b.get("sources") or []):
            b["sources"] = (b.get("sources") or []) + [url]
    data["builds"] = [x if x["id"] != hand else b for x in data["builds"]]
    json.dump(data, open(bp, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    subprocess.run([sys.executable, str(HERE / "fmt_json.py"), str(bp)], check=True, capture_output=True)
    print(f"  {spec}: {hand} <- {win} ({gain:+.1%} {unit}); core {len(core)}, flex {len(flex)}")
    return {"hand": hand, "winner": win, "gain": gain, "date": today}


def abs_dps_factor(cls, main_spec, extra_spec, log):
    """Write the extra spec model's abs_dps_factor from the fight lab: level-weighted kills per hour of its build relative to
    the main spec's optimizer build on the same mobs (the main spec keeps 1.0). respec.py then compares the models on that."""
    rep = paths.fightlab_dir(cls) / f"{extra_spec}.json"
    if not rep.exists():
        return
    r = json.load(open(rep, encoding="utf-8"))
    comp = next(iter(r["compare"].values()), None) if r.get("compare") else None
    if not comp:
        return
    mine = {L: x["time_per_kill"] for L, x in r["levels"].items() if L in comp}
    theirs = {L: comp[L]["time_per_kill"] for L in mine}
    if not mine:
        return
    factor = round(weighted_mean(theirs) / weighted_mean(mine), 3)
    sp = HERE / "scorer/specs" / f"{cls}.json"
    specs = json.load(open(sp, encoding="utf-8"))
    model = specs["models"].get(extra_spec)
    if model is None:
        return
    model["abs_dps_factor"] = factor
    model["note"] = model.get("note", "").split(" Fight lab speed")[0] + (
        f" Fight lab speed ({datetime.date.today().isoformat()}): its leveling build kills {factor:.2f}x as fast as {main_spec}'s optimizer build "
        f"(level-weighted time per kill {weighted_mean(mine):.1f}s vs {weighted_mean(theirs):.1f}s), written as abs_dps_factor so respec.py compares the models on that.")
    sys.path.insert(0, str(HERE))
    from fmt_json import dumps
    sp.write_text(dumps(specs), encoding="utf-8")
    print(f"  {extra_spec}: abs_dps_factor {factor} vs {main_spec}")
    log.append({"cmd": f"abs_dps_factor {cls} {extra_spec}", "rc": 0, "seconds": 0, "tail": [str(factor)], "stderr": []})


def heal_capacities(so):
    """Parse `heallab/run.py` output: build id -> capacity."""
    out = {}
    for line in so.splitlines():
        m = re.match(r"\s+(\S+)\s+\S+\s+capacity ([0-9.]+)", line)
        if m:
            out[m.group(1)] = float(m.group(2))
    return out


def heal_step(cls, a, log, result):
    """Calibrate <-> optimize <-> race for the class's healer model in the healer lab (the raid step's loop with capacity for DPS)."""
    import ast
    src = (HL / f"{HEALERS[cls]}.py").read_text(encoding="utf-8")   # read, not imported: the lab's module names clash with the fight lab's
    P = ast.literal_eval(next(l for l in src.splitlines() if l.startswith("PIPELINE = ")).split("=", 1)[1].strip())
    spec, hand, opt, tag = P["spec"], P["hand"], P["opt"], P["tag"]
    folder = paths.heallab_dir(cls) / "candidates"
    folder.mkdir(parents=True, exist_ok=True)
    rounds = []
    for rnd in range(1, a.raid_rounds + 1):
        cands = sorted(str(p) for p in folder.glob(f"cand-{tag}-*.json"))
        before = alloc_of(load_build(cls, opt)) if not a.dry_run else {}
        sh([HL / "calibrate.py", cls, "--runs", a.runs_heal, "--write"], a.dry_run, log)
        sh([HERE / "scorer/run.py", cls, "--spec", spec, "--profile", "raid-heal", "--write", "--export", "--seed", hand], a.dry_run, log)
        if a.dry_run:
            break
        after = load_build(cls, opt)
        known = [alloc_of(json.load(open(c, encoding="utf-8"))) for c in cands] + [before]
        new = alloc_of(after) not in known
        rounds.append({"round": rnd, "new_build": new})
        if not new:
            print(f"  {spec}: the optimizer's {opt} matches a calibrated build: converged")
            break
        n = 1
        while (folder / f"cand-{tag}-r{n}.json").exists():
            n += 1
        path = folder / f"cand-{tag}-r{n}.json"
        path.write_text(json.dumps({"id": path.stem, "allocation": after["allocation"], "note": f"Optimizer raid-heal build saved by rebuild.py on {datetime.date.today().isoformat()} (healer lab calibration round {rnd})"}, indent=1, ensure_ascii=False), encoding="utf-8")
        rc, so = sh([HL / "run.py", cls, "--build", opt, "--compare", *cands, "--runs", max(20, a.runs_heal // 2)], a.dry_run, log)
        if rc == 0:
            caps = heal_capacities(so)
            new_c = caps.get(opt)
            best_prev = max([v for k, v in caps.items() if k != opt], default=None)
            rounds[-1]["quick_race"] = caps
            if new_c is not None and best_prev is not None and new_c < best_prev * (1 + RACE_NOISE):
                print(f"  {spec}: new {opt} saved as {path.name} but not {RACE_NOISE:.0%} better than the best so far ({new_c:.3f} vs {best_prev:.3f}): converged by noise")
                rounds[-1]["converged_by_noise"] = True
                break
        print(f"  {spec}: new {opt} saved as {path.name}; calibrating again")
    cands = sorted(str(p) for p in folder.glob(f"cand-{tag}-*.json"))
    rc, so = sh([HL / "run.py", cls, "--build", hand, "--compare", opt, *cands, "--deltas", "--runs", a.runs_heal, "--write"], a.dry_run, log)
    out = {"rounds": rounds}
    if not a.dry_run and rc == 0:
        caps = heal_capacities(so)
        out["capacity"] = caps
        ours = [k for k in caps if k == opt or k.startswith(f"cand-{tag}-r")]
        if ours:
            win = max(ours, key=lambda k: caps[k])
            if win != opt and caps[win] > caps.get(opt, 0) * (1 + RACE_NOISE):   # an earlier round's build beats the last export: promote it
                bp = ROOT / cls / "research/talents/forever/proposed-builds.json"
                data = json.load(open(bp, encoding="utf-8"))
                b = next(x for x in data["builds"] if x["id"] == opt)
                b["allocation"] = json.load(open(folder / f"{win}.json", encoding="utf-8"))["allocation"]
                b["notes"] = [n for n in b.get("notes", []) if not n.startswith("Promoted by rebuild.py")] + [f"Promoted by rebuild.py on {datetime.date.today().isoformat()}: {win} had the highest healing capacity in the healer lab ({caps[win]:.3f} vs {caps.get(opt, 0):.3f})."]
                bp.write_text(json.dumps(data, indent=1, ensure_ascii=False), encoding="utf-8")
                subprocess.run([sys.executable, str(HERE / "fmt_json.py"), str(bp)], check=True, capture_output=True)
                print(f"  {spec}: {opt} <- {win} ({caps[win]:.3f} vs {caps.get(opt, 0):.3f})")
                out["promoted"] = win
            print(f"  {spec}: " + ", ".join(f"{k} {v:.3f}" for k, v in sorted(caps.items(), key=lambda kv: -kv[1])))
            if hand in caps:
                gain = (caps[win] - caps[hand]) / caps[hand]
                if "adopt" in a.steps and gain >= RACE_MARGIN:
                    out["adopted"] = adopt_heal(cls, spec, hand, win, opt, folder, caps, gain, log)
                else:
                    print(f"  {spec}: the hand draft {hand} stands ({win} is {gain:+.1%} in healing capacity)")
    result["heal"] = out


def adopt_heal(cls, spec, hand, win, opt, folder, caps, gain, log):
    """The hand healer draft takes the winner's allocation (old draft kept as a candidate; core from the lab's removal values)."""
    bp = ROOT / cls / "research/talents/forever/proposed-builds.json"
    data = json.load(open(bp, encoding="utf-8"))
    b = next(x for x in data["builds"] if x["id"] == hand)
    src = next(x for x in data["builds"] if x["id"] == opt) if win == opt else json.load(open(folder / f"{win}.json", encoding="utf-8"))
    today = datetime.date.today().isoformat()
    keep = folder / f"cand-{spec}-hand-{today}.json"
    if not keep.exists():
        keep.write_text(json.dumps({"id": keep.stem, "allocation": b["allocation"], "note": f"The hand draft {hand} as it was before {win} was adopted on {today}"}, indent=1, ensure_ascii=False), encoding="utf-8")
    rep = json.load(open(paths.heallab_dir(cls) / f"{spec}.json", encoding="utf-8"))
    vals = {r["talent"]: r["sim_delta"] for r in rep.get("deltas", {}).get(hand, [])}
    new_alloc = alloc_of(src)
    old_why = {c["talent"]: c["why"] for c in b.get("core", []) if c.get("talent") in new_alloc}
    ranked = sorted(new_alloc, key=lambda n: -vals.get(n, 0.0))
    b["core"] = [{"talent": n, "why": (old_why.get(n, "") + (f" Healer lab ({today}): removing it costs {vals[n]:+.0%} healing capacity." if n in vals else "")).strip()} for n in ranked[:8]]
    b["flex"] = [{"points": new_alloc[n], "default": n, "alternatives": ["any utility talent legal at that tier"], "why": f"Measures {vals[n]:+.1%} healing capacity in the healer lab (noise): these points are free to move."} for n in ranked[8:] if n in vals and abs(vals[n]) < 0.01]
    b["allocation"] = src["allocation"]
    b["name"] = f"{b['name'].split(' (')[0]} (healer lab winner adopted {today})"
    b["summary"] = f"Allocation adopted on {today} from `{win}`, the build with the highest healing capacity in the healer lab ({gain:+.1%} vs the previous draft; kept under raid/heallab/candidates/). Previous summary: " + b["summary"]
    b["notes"] = [f"Adopted from the healer lab on {today}: {win} beat the previous draft by {gain:+.1%} healing capacity."] + b.get("notes", [])
    bp.write_text(json.dumps(data, indent=1, ensure_ascii=False), encoding="utf-8")
    subprocess.run([sys.executable, str(HERE / "fmt_json.py"), str(bp)], check=True, capture_output=True)
    print(f"  {spec}: {hand} <- {win} ({gain:+.1%} healing capacity)")
    return {"hand": hand, "winner": win, "gain": round(gain, 4)}


def classic_step(cls, a, log, result):
    """Our Classic-era raid builds through the upstream wowsims/classic simulator: the Classic damage split and raid-mode effect
    fits go into the classic-era game of the scorer (main() then re-runs the Classic check against the community builds)."""
    specs = json.load(open(HERE / "raidsim/specs-classic.json", encoding="utf-8")).get(cls, {})
    rs = HERE / "raidsim"
    out = {}
    for spec in specs:
        sh([rs / "calibrate.py", cls, "--spec", spec, "--game", "classic-era", "--iterations", a.iterations_calibrate, "--write"], a.dry_run, log)
        sh([rs / "run.py", cls, "--spec", spec, "--game", "classic-era", "--iterations", a.iterations_race, "--write"], a.dry_run, log)
        sh([rs / "run.py", cls, "--spec", spec, "--game", "classic-era", "--env", "environments", "--iterations", a.iterations_race, "--write"], a.dry_run, log)
        rep = paths.raidsim_dir(cls, "classic-era") / f"{spec}.json"
        if not a.dry_run and rep.exists():
            res = json.load(open(rep, encoding="utf-8"))["results"]
            out[spec] = {r["label"]: round(r["dps"], 1) for r in res if not r.get("error")}
    result["classic"] = out


def regen(a, classes, log):
    for args in ([HERE / "render_fightlab_sections.py", *classes], [HERE / "render_raidsim_sections.py", *classes], [HERE / "render_heallab_sections.py", *classes], [HERE / "render_leveling_guides.py", *classes], [HERE / "render_sim_presets.py", *classes], [HERE / "render_rotations.py", *classes], [HERE / "validate_builds.py"], [HERE / "render_builds.py"], [HERE / "render_new_builds.py", *classes], [HERE / "render_modes.py"], [HERE / "render_tier_list.py"], *[[HERE / "scorer/respec.py", c, "--write"] for c in classes],
                 [HERE / "render_optimizer_sections.py"], [HERE / "scorer/compare_effects.py"], [HERE / "scorer/loop_audit.py"],
                 [HERE / "build_launch_checklist.py"], [HERE / "build_beta_checklist.py"], [FL / "summary.py", "--write"]):
        sh(args, a.dry_run, log)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("classes", nargs="*", default=CLASSES)
    ap.add_argument("--steps", default=",".join(s for s in STEPS if s != "adopt"), help=f"comma-separated subset of {','.join(STEPS)} (adopt is opt-in)")
    ap.add_argument("--rounds", type=int, default=3, help="calibrate/optimize rounds per class (stops early once the optimizer build repeats)")
    ap.add_argument("--fights-calibrate", type=int, default=1500)
    ap.add_argument("--fights-race", type=int, default=1000)
    ap.add_argument("--fights-report", type=int, default=2000)
    ap.add_argument("--fights-sensitivity", type=int, default=1000)
    ap.add_argument("--jobs", type=int, default=1, help="classes run in parallel")
    ap.add_argument("--raid-rounds", type=int, default=2, help="raid calibrate/optimize rounds per spec model")
    ap.add_argument("--iterations-calibrate", type=int, default=1500, help="simulator iterations per removal run (raid step)")
    ap.add_argument("--iterations-race", type=int, default=3000, help="simulator iterations per build in the final raid race")
    ap.add_argument("--runs-heal", type=int, default=60, help="healer lab runs per capacity (heal step)")
    ap.add_argument("--refresh", help="raw folder name for a new beta build: runs refresh_forever_talents.py --fetch --raw <name>, build_forever_spells.py, render_trees.py first")
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    a.steps = [s for s in a.steps.split(",") if s]
    bad = [s for s in a.steps if s not in STEPS] + [c for c in a.classes if c not in CLASSES]
    if bad:
        raise SystemExit(f"unknown: {bad}")
    log = []
    t0 = time.time()
    if a.refresh:
        for args in ([HERE / "refresh_forever_talents.py", "--fetch", "--raw", a.refresh], [HERE / "build_forever_spells.py"], [HERE / "render_trees.py"]):
            sh(args, a.dry_run, log)
    results = []
    class_steps = [s for s in a.steps if s != "regen"]
    if "classic" in a.steps:
        sh([HERE / "raidsim/classic_specs.py"], a.dry_run, log)   # the spec table from the upstream clone's presets (+ our gear sets copied in)
    if class_steps:
        if a.jobs > 1 and not a.dry_run:
            with concurrent.futures.ThreadPoolExecutor(max_workers=a.jobs) as ex:
                results = list(ex.map(lambda c: run_class(c, a), a.classes))
        else:
            results = [run_class(c, a) for c in a.classes]
    if "classic" in a.steps:
        rc, outp = sh([HERE / "scorer/classic_check.py", "--write"], a.dry_run, log)   # do the Classic models still reproduce the community builds?
        if not a.dry_run:
            print("  " + (outp.strip().splitlines() or [""])[-1])
    if "regen" in a.steps:
        print("== regenerate derived pages")
        regen(a, a.classes if a.classes != CLASSES else CLASSES, log)
    if not a.dry_run:
        prev = json.load(open(LOG, encoding="utf-8")) if LOG.exists() else {"classes": {}}
        for r in results:   # merge per class so a partial run (--steps raid) keeps the earlier steps' records
            prev["classes"][r["class"]] = {**prev["classes"].get(r["class"], {}), **r}
        prev["last_run"] = {"date": datetime.datetime.now().isoformat(timespec="seconds"), "classes": a.classes, "steps": a.steps,
                            "fights": {"calibrate": a.fights_calibrate, "race": a.fights_race, "report": a.fights_report, "sensitivity": a.fights_sensitivity},
                            "seconds": round(time.time() - t0), "refresh": a.refresh, "regen_log": log}
        LOG.write_text(json.dumps(prev, indent=1, ensure_ascii=False), encoding="utf-8")
        print(f"wrote {LOG.relative_to(ROOT)}")
    failed = [r["class"] for r in results if r.get("failed")] + [l["cmd"][:60] for l in log if l["rc"]]
    print(f"done in {(time.time() - t0) / 60:.0f} min" + (f"; FAILED: {failed}" if failed else ""))
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
