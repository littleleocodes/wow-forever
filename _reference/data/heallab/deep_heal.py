"""Deep optimisation of a healer spec in the healer lab: talents and heal-choice policy tuned in turns until neither moves (2026-10-02,
user request: "a full optimization analysis on Shaman ... the best talent tree entirely for each spec and the best rotation for each";
Restoration heals, so its score is the healer lab's capacity, not DPS).

    python -u _reference/data/heallab/deep_heal.py shaman [--cycles 3] [--fresh] [--jobs 10]

Capacity (the damage multiplier at which the build keeps a five-member group alive in 90% of the runs, a tail mean over seeds:
engine.capacity) is a model of stated assumptions (heallab/tables.py), not a measurement. The search is raidsim/ml_talents.py's
(random forest + genetic search, races, the one-move and chain-move check, the two-move check) on a healer-lab adapter: builds are
measured in parallel processes (heal_worker.py) with common random numbers, and a search's "iterations" are seeds (runs) here.
1. cycles until the winner and the policy repeat (at most --cycles): the talent search (cycle 1: 4 independent runs of up to 2,500
   builds screened on 24 seeds with 8 bisection steps; later cycles 2 runs of 1,500 seeded with the winners; races on 60, 120 and 240
   fresh seeds; the one-move check on 40 and 160 seeds), then the heal-choice policy re-tuned on the winner and the hand draft
   (rotation_opt.py --build; neither may lose more than 0.3%);
2. the two-move check with the 25 best one-move neighbours expanded a second time;
3. a final race over 400 fresh seeds: the winner against every Restoration raid build of ours.
Record `heallab/deep/<class>.json`, report `<class>/research/raid/heallab/deep-optimization.md`.
"""
import argparse
import datetime
import importlib.util
import json
import math
import multiprocessing
import os
import pathlib
import subprocess
import sys
import time

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[2]
sys.path[:0] = [str(HERE), str(ROOT / "_reference/data")]
import heal_worker as W  # noqa: E402

OUT = HERE / "deep"
TODAY = datetime.date.today().isoformat()
HEAL_SPEC = {"shaman": "Restoration", "priest": "Holy", "paladin": "Holy", "druid": "Restoration"}
DEEP = dict(runs=4, budget=2500, screen=24, patience=5, max_rounds=20, random_init=300, pool=8000, parents=40, finalists=6,
            race_stages=((60, 2, 5), (120, 3, 2), (240, 4, 2)), cert_its=(40, 160))
QUICK = dict(DEEP, runs=2, budget=1500, random_init=150)
FINAL_SEEDS = 400


def log(m):
    print(m, flush=True)


class HealSim:
    """ml_talents.Sim's interface for the healer lab: run(allocs, seeds, seed) -> [(capacity, spread)]."""

    def __init__(self, cls, pool, procs, steps=8):
        self.cls, self.pool, self.procs, self.steps = cls, pool, procs, steps
        self.setting = "heal"
        self.n = 0
        self.fights = 0

    def run(self, allocs, iterations, seed):
        seeds = list(range(seed * 100000, seed * 100000 + iterations))
        jobs = [(self.cls, al, seeds, self.steps) for al in allocs]
        out = self.pool.map(W.capacity, jobs, chunksize=max(1, len(jobs) // (self.procs * 4)))
        self.n += len(allocs)
        self.fights += len(allocs) * iterations
        return out


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("cls", choices=list(HEAL_SPEC))
    ap.add_argument("--cycles", type=int, default=3)
    ap.add_argument("--fresh", action="store_true")
    ap.add_argument("--jobs", type=int, default=max(1, (os.cpu_count() or 4) - 2))
    ap.add_argument("--smoke", action="store_true", help="tiny budgets, a separate record, nothing else written (a test)")
    a = ap.parse_args()
    global OUT
    s = importlib.util.spec_from_file_location("ml_talents_heal", ROOT / "_reference/data/raidsim/ml_talents.py")
    MLT = importlib.util.module_from_spec(s)
    s.loader.exec_module(MLT)
    import paths  # noqa: E402
    import spec_modes as SM  # noqa: E402
    import render_start_here as RSH  # noqa: E402
    cls, spec = a.cls, HEAL_SPEC[a.cls]
    deep, quick = DEEP, QUICK
    if a.smoke:
        OUT = HERE / "deep-smoke"
        deep = quick = dict(DEEP, runs=1, budget=60, screen=6, patience=1, max_rounds=1, random_init=20, pool=300, parents=6, finalists=2,
                            race_stages=((8, 2, 2), (12, 3, 1), (16, 4, 1)), cert_its=(6, 8))
    OUT.mkdir(parents=True, exist_ok=True)
    rp = OUT / f"{cls}.json"
    st = json.load(open(rp, encoding="utf-8")) if rp.exists() and not a.fresh else {"class": cls, "spec": spec, "date": TODAY, "cycles": []}

    def save():
        rp.write_text(json.dumps(st, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")

    data = {b["id"]: b for b in json.load(open(paths.builds_json("forever", cls), encoding="utf-8"))["builds"]}
    flat = lambda al: {n: r for items in al.values() for n, r in items if r}   # noqa: E731
    space = MLT.Space(cls, spec)
    ours = [bid for bid, b in data.items() if b.get("role") == "healer" and SM.spec_of(cls, b) == spec]
    starts = [flat(data[bid]["allocation"]) for bid in ours]
    starts += MLT.popular_allocs(cls)
    starts = [x for x in starts if space.valid(x)]
    log(f"== deep optimisation of {cls} {spec} (healer lab): {len(starts)} valid starts; our builds {', '.join(ours)}")
    t0 = time.time()
    for cyc in range(len(st["cycles"]) + 1, a.cycles + 1):
        prev = st["cycles"][-1] if st["cycles"] else None
        settings = deep if cyc == 1 else quick
        with multiprocessing.Pool(a.jobs, initializer=W.init, initargs=(cls,)) as pool:
            sim = HealSim(cls, pool, a.jobs)
            opts = MLT.defaults(**{k: v for k, v in settings.items()}, seed=500 + cyc)
            extra = [flat(c["winner"]["allocation"]) for c in st["cycles"]]
            rec, win = MLT.optimize(space, {"heal": sim}, starts + extra, opts, log)
        c = {"cycle": cyc, "winner": rec["winner"], "runner_up": rec.get("runner_up"), "gap_to_runner_up": rec.get("gap_to_runner_up"),
             "runs": [{k: v for k, v in r.items() if k != "trace"} for r in rec["runs"]], "runs_agree": rec["runs_agree"], "race": rec["race"],
             "certificate": rec["certificate"], "important_features": rec.get("important_features"), "simulated_builds": rec["simulated_builds"],
             "minutes": rec["minutes"]}
        log(f"  [{cyc}] winner {rec['winner']['split']} capacity {rec['winner']['dps']:.4f}; runs agreeing {rec['runs_agree']}/{len(rec['runs'])}")
        # the heal-choice policy, tuned on the winner and the hand draft
        pol = OUT / f"{cls}-winner-{cyc}.json"
        pol.write_text(json.dumps({"allocation": rec["winner"]["allocation"]}, indent=1), encoding="utf-8")
        rot = HERE / "rotations" / f"{cls}-{importlib.import_module(cls).PIPELINE['spec']}.json"
        before = rot.read_text(encoding="utf-8") if rot.exists() else ""
        if not a.smoke:
            r = subprocess.run([sys.executable, str(HERE / "rotation_opt.py"), cls, "--build", str(pol), "--write", "--jobs", str(a.jobs)],
                               capture_output=True, text=True, encoding="utf-8", errors="replace", cwd=str(ROOT))
            for ln in r.stdout.splitlines():
                log("  " + ln.strip()[:220])
        after = rot.read_text(encoding="utf-8") if rot.exists() else ""
        c["policy_changed"] = before != after
        st["cycles"].append(c)
        save()
        if prev and flat(prev["winner"]["allocation"]) == flat(rec["winner"]["allocation"]) and not c["policy_changed"]:
            st["converged"] = cyc
            save()
            break
    win = flat(st["cycles"][-1]["winner"]["allocation"])
    with multiprocessing.Pool(a.jobs, initializer=W.init, initargs=(cls,)) as pool:
        sim = HealSim(cls, pool, a.jobs)
        if "two_move" not in st:
            new, steps = (MLT.two_move_certificate(space, sim, win, log, screen=24, seed=61, conf=(120, 400), top=30, expand_top=25)
                          if not a.smoke else MLT.two_move_certificate(space, sim, win, log, screen=6, seed=61, conf=(8, 12), top=3, expand_top=2, rounds=1))
            st["two_move"] = {"steps": steps, "moved": new != win}
            if new != win:
                win = new
                st["cycles"][-1]["winner"] = dict(st["cycles"][-1]["winner"], allocation=MLT.by_tree(space, new) if hasattr(MLT, "by_tree") else
                                                  {t: [[n, new[n]] for n in space.by_tree[t] if new.get(n)] for t in space.tree_names}, split=space.split(new))
            save()
        if "final" not in st:
            rows = {"deep winner": win} | {bid: flat(data[bid]["allocation"]) for bid in ours if data[bid].get("content") == "raid"}
            n = FINAL_SEEDS if not a.smoke else 12
            res = sim.run(list(rows.values()), n, 71)
            st["final"] = {k: {"capacity": round(c0, 4), "se": round(sd / math.sqrt(n), 4)} for k, (c0, sd) in zip(rows, res)}
            save()
            log("  final race: " + ", ".join(f"{k} {v['capacity']:.4f}" for k, v in sorted(st["final"].items(), key=lambda kv: -kv[1]["capacity"])))
    st["minutes"] = round((time.time() - t0) / 60, 1) + st.get("minutes", 0)
    save()
    if a.smoke:
        log("== done (smoke test)")
        return
    # the report
    w = st["cycles"][-1]["winner"]
    o = [f"# {cls.capitalize()} {spec}: deep optimisation in the healer lab (generated)", "",
         f"> Generated by `_reference/data/heallab/deep_heal.py` on {TODAY}; record `_reference/data/heallab/deep/{cls}.json`. Do not hand-edit.", "",
         "Talents and the heal-choice policy were tuned in turns until neither moved; the winner was then checked against its one-move "
         "neighbours and the two-move builds around its 25 best neighbours, and raced against our builds on 400 fresh seeds. Capacity is "
         "the healer lab's model of stated assumptions (heallab/tables.py), not a measurement.", "",
         f"**Winner:** [{w['split']}]({RSH.tf_link(cls, flat(w['allocation']))}), capacity {st['final']['deep winner']['capacity']:.4f} "
         f"± {st['final']['deep winner']['se']:.4f}; cycles {len(st['cycles'])}" + (f" (converged in cycle {st['converged']})" if st.get("converged") else "")
         + f"; independent runs agreeing in the last cycle {st['cycles'][-1]['runs_agree']}/{len(st['cycles'][-1]['runs'])}.", "",
         "| Build | Capacity (400 seeds) |", "|---|---|"]
    o += [f"| {k} | {v['capacity']:.4f} ± {v['se']:.4f} |" for k, v in sorted(st["final"].items(), key=lambda kv: -kv[1]["capacity"])]
    tm = st.get("two_move", {}).get("steps", [{}])[-1]
    o += ["", f"Two-move check: {tm.get('one_move', 0)} one-move and {tm.get('two_move', 0):,} two-move builds"
          + (f"; best {tm['confirmed'][0][1]:+.2%} ({tm['confirmed'][0][0]})" if tm.get("confirmed") else "") + ".", ""]
    o += ["| Cycle | Winner | Capacity (race) | Runs agreeing | Policy changed |", "|---|---|---|---|---|"]
    o += [f"| {c['cycle']} | {c['winner']['split']} | {c['winner']['dps']:.4f} | {c['runs_agree']}/{len(c['runs'])} | {'yes' if c['policy_changed'] else 'no'} |"
          for c in st["cycles"]]
    p = paths.scenario_dir(cls, "raid") / "heallab" / "deep-optimization.md"
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text("\n".join(o) + "\n", encoding="utf-8")
    log(f"wrote {p.relative_to(ROOT).as_posix()}")
    write_build(cls, spec, st, data, ours, flat, paths, SM)
    save()
    log("== done")


def write_build(cls, spec, st, data, ours, flat, paths, SM):
    """The winner as `<spec slug>-ml-heal` (derived, healer) when the final race has it 0.5% or more ahead of every Restoration raid build
    of ours (else the search confirms them), with `replaces` at 2% or more over the hand draft (the user's rule; the hand draft stays as
    the alternative). An earlier such build of the spec is replaced."""
    sys.path.insert(0, str(ROOT / "_reference/data"))
    from fmt_json import dumps   # noqa: E402
    fin = st["final"]
    w = fin["deep winner"]["capacity"]
    others = {k: v["capacity"] for k, v in fin.items() if k != "deep winner"}
    best = max(others, key=others.get) if others else None
    bid = f"{SM.slug(spec)}-ml-heal"
    if best and w < others[best] * 1.005:
        st["build"] = {"written": None, "why": f"confirms {best} ({w / others[best] - 1:+.2%})"}
        log(f"  no build: the search confirms {best} ({w / others[best] - 1:+.2%})")
        return
    hand = importlib.import_module(cls).PIPELINE["hand"]
    gain = w / fin[hand]["capacity"] - 1 if hand in fin else None
    win = st["cycles"][-1]["winner"]
    tm = (st.get("two_move", {}).get("steps") or [{}])[-1]
    b = {"id": bid, "name": f"{spec} — Raid healing (machine-learning search)", "role": "healer", "content": "raid", "tier": "draft", "spec": spec,
         "generated": TODAY, "derived": "raid",
         "summary": (f"The {spec} build the machine-learning talent search found in the healer lab on {TODAY} (heallab/deep_heal.py: a random "
                     f"forest guiding a genetic search over every legal build of the spec, the heal-choice policy tuned with it, races on fresh "
                     f"seeds, every build one or two moves from the winner checked). Capacity is the healer lab's model of stated assumptions."),
         "allocation": win["allocation"], "core": [], "flex": [],
         "notes": [f"Final race over {FINAL_SEEDS} fresh seeds: capacity {w:.3f} ± {fin['deep winner']['se']:.3f}; "
                   + ", ".join(f"{k} {v:.3f}" for k, v in sorted(others.items(), key=lambda kv: -kv[1])) + ".",
                   f"Independent runs agreeing in the last cycle: {st['cycles'][-1]['runs_agree']}/{len(st['cycles'][-1]['runs'])}; two-move check: "
                   f"{tm.get('one_move', 0)} one-move and {tm.get('two_move', 0):,} two-move builds, none better.",
                   "The healer lab models one healer keeping a five-member group alive (heallab/tables.py); not an in-game measurement."],
         "open_questions": [f"A machine-searched {spec} build: check it against the community's healing builds at launch."],
         "sources": []}
    if gain is not None and gain >= 0.02:
        b["replaces"] = hand
        b["notes"].insert(0, f"{gain:+.1%} capacity over the hand draft {hand} (over the 2% bar: the spec's healing pick; the hand draft stays as the alternative).")
    bp = paths.builds_json("forever", cls)
    d = json.load(open(bp, encoding="utf-8"))
    d["builds"] = [x for x in d["builds"] if x["id"] != bid] + [b]
    bp.write_text(dumps(d) + "\n", encoding="utf-8")
    st["build"] = {"written": bid, "gain_vs_hand": gain}
    log(f"  wrote {bid}" + (f" ({gain:+.1%} vs {hand})" if gain is not None else ""))
    # the healer-lab report with the new build, so the pages show its capacity
    r = subprocess.run([sys.executable, str(HERE / "run.py"), cls, "--build", hand, "--compare", bid, *[x for x in ours if x != hand and data[x].get("content") == "raid"],
                        "--write"], capture_output=True, text=True, encoding="utf-8", errors="replace", cwd=str(ROOT))
    log("  " + (r.stdout.strip().splitlines() or ["(no output)"])[-1])


if __name__ == "__main__":
    main()
