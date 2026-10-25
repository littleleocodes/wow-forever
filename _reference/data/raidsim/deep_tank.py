"""Deep optimisation of a class's tank (2026-10-03, user request "go with next steps": the deep runs ready for every class; Protection
warrior, Protection paladin and the bear druid are scored on tank value, not DPS).

    python -u _reference/data/raidsim/deep_tank.py <class> [--cycles 3] [--fresh] [--smoke]

Tank value is run.py's (tank_value: the raid-tank profile's weights on threat per second and on damage avoided) against one fixed
reference, the entry's hand draft over 20,000 fights, so every build sits on one scale; a build's per-fight spread combines damage
taken's and threat's (the bench reports no spread for threat, so threat takes damage's relative spread). The class's tank entry (warrior
and paladin prot-tank, druid feral-bear-tank) runs in its own setting (the raid: boss melee, every raid buff) and its own gear (tanks
keep their sets: the gear tiers cover damage specs). Like deep_opt.py:
1. cycles until the winner and the rotation repeat (at most --cycles): the talent search (ml_talents.py: random forest + genetic search;
   cycle 1 with 6 runs of up to 5,000 builds at 1,500 fights, later cycles 3 runs of 3,000 seeded with the winners; races on fresh
   seeds; the one-move and chain-move check), then the entry's rotation re-tuned on the winner (apl_opt.py --tune; every build the entry
   lists stays protected);
2. the two-move check of the winner (ml_talents.two_move_certificate);
3. a final race over 100,000 fights on a fresh seed: the winner against every tank build of ours of the spec;
4. the winner becomes `<spec slug>-ml-tank` (derived, tank) when it is 0.5% or more ahead of all of them, with `replaces` at 2% or more
   over the hand draft (the user's rule; the hand draft stays as the alternative); the filler audit moves its free points (ml_builds.tidy)
   and it joins the entry's builds, so the race and the pages see it.
Record raidsim/deep/<class>-tank.json, report <class>/research/raid/deep-optimization-tank.md. Simulations of the community's model of
the beta, not in-game measurements; no search over this many builds proves a global optimum.
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
import sim_info as SI  # noqa: E402  (which simulator a record ran on)
import render_start_here as RSH  # noqa: E402
import spec_modes as SM  # noqa: E402


def _load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


MLT = _load("ml_talents_tank", HERE / "ml_talents.py")
A, R = MLT.A, MLT.R
OUT = HERE / "deep"
TODAY = datetime.date.today().isoformat()
TANK_ENTRY = {"warrior": "prot-tank", "paladin": "prot-tank", "druid": "feral-bear-tank"}
# 2026-10-24 audit: the six runs agreed 6/6 in every tank search and later runs never gained: three
DEEP = dict(runs=3, budget=5000, screen=1500, patience=8, max_rounds=40, random_init=500, pool=10000, parents=48, finalists=8, screen_budget=800)
QUICK = dict(runs=3, budget=3000, screen=1500, patience=5, max_rounds=20, random_init=300, pool=8000, parents=40, finalists=6, screen_budget=600)
FINAL_FIGHTS = 100000
REF_FIGHTS = 20000
SMOKE = False


def log(m):
    print(m, flush=True)


def flat_of(alloc):
    return {n: r for items in alloc.values() for n, r in items if r}


def by_tree(space, flat):
    return {t: [[n, flat[n]] for n in space.by_tree[t] if flat.get(n)] for t in space.tree_names}


class TankSim(MLT.Sim):
    """ml_talents.Sim's interface on tank value: run(allocs, iterations, seed) -> [(value, per-fight spread)]."""

    def __init__(self, cls, entry, repo, tag, ref):
        super().__init__(cls, entry, "raid", None, repo, tag)
        self.ref = ref
        self.tw, self.mw = R.tank_weights()

    def run(self, allocs, iterations, seed):
        out = []
        for i0 in range(0, len(allocs), 400):
            chunk = allocs[i0:i0 + 400]
            bl = [{"label": str(i), "talents": R.talents_string(self.sim_trees, al)} for i, al in enumerate(chunk)]
            rows = A.bench(self.entry, self.repo, bl, iterations, seed, self.setting, self.tag)
            out += [self.value(rows.get(str(i)) or {}) for i in range(len(chunk))]
            self.n += len(chunk)
            self.fights += len(chunk) * iterations
        return out

    def value(self, r):
        v = R.tank_value(r, self.ref)
        if v is None:
            return (0.0, 0.0)
        thr_sd = (r.get("threat") or 0.0) * (r.get("dps_stdev") or 0.0) / max(r.get("dps") or 0.0, 1e-9)
        sd = math.hypot(self.tw * thr_sd / self.ref["threat"], self.mw * self.ref["dtps"] * (r.get("dtps_stdev") or 0.0) / r["dtps"] ** 2)
        return (float(v), float(sd))


def apl_hash(cls, entry, repo):
    h = hashlib.sha1()
    for st in ("dummy", "raid"):
        p = R.apl_path(R.SPECS[cls][entry], repo, st)
        h.update(p.read_bytes() if p.exists() else b"")
    return h.hexdigest()[:12]


def retune(cls, entry, win, repo):
    """apl_opt.py --tune on the winner (every build the entry lists stays protected); True when the rotation changed."""
    before = apl_hash(cls, entry, repo)
    tune = OUT / "tune" / f"{cls}-{entry}.json"
    tune.parent.mkdir(parents=True, exist_ok=True)
    tune.write_text(json.dumps([{"label": "deep: tank", "allocation": win}], indent=1), encoding="utf-8")
    log(f"== rotation {cls}/{entry}: tuning on the winner (every build the entry lists protected)")
    r = subprocess.run([sys.executable, str(HERE / "apl_opt.py"), cls, "--spec", entry, "--tune", str(tune), "--write", "--rounds", "20"],
                       capture_output=True, text=True, encoding="utf-8", errors="replace", cwd=str(ROOT))
    for ln in r.stdout.splitlines():
        if ln.strip().startswith(("==", "round", "raid", "wrote", "no change")):
            log("  " + ln.strip()[:220])
    if r.returncode:
        log(f"  apl_opt failed: {r.stderr[-800:]}")
    R.set_game("forever")   # specs.json again: a first tuned rotation adds a key this process would not know
    return apl_hash(cls, entry, repo) != before


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("cls", choices=sorted(TANK_ENTRY))
    ap.add_argument("--cycles", type=int, default=3)
    ap.add_argument("--fresh", action="store_true")
    ap.add_argument("--smoke", action="store_true", help="tiny budgets, a separate record, nothing else written (a test)")
    a = ap.parse_args()
    global OUT, DEEP, QUICK, FINAL_FIGHTS, REF_FIGHTS, SMOKE
    if a.smoke:
        OUT, FINAL_FIGHTS, REF_FIGHTS, SMOKE = HERE / "deep-smoke", 2000, 1000, True
        DEEP = QUICK = dict(runs=1, budget=150, screen=300, patience=1, max_rounds=1, random_init=40, pool=600, parents=8, finalists=2, screen_budget=60,
                            race_stages=((1000, 2, 2), (2000, 3, 1), (4000, 4, 1)), cert_its=(500, 2000))   # a test: small races too
    cls, entry, spec = a.cls, TANK_ENTRY[a.cls], SM.TANK_TREE[a.cls]
    R.set_game("forever")
    repo = R.repo_path(argparse.Namespace(repo=None))
    OUT.mkdir(parents=True, exist_ok=True)
    rp = OUT / f"{cls}-tank.json"
    st = json.load(open(rp, encoding="utf-8")) if rp.exists() and not a.fresh else {"class": cls, "spec": spec, "entry": entry, "date": TODAY, "cycles": []}

    def save():
        rp.write_text(json.dumps(st, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")

    data = {b["id"]: b for b in json.load(open(paths.builds_json("forever", cls), encoding="utf-8"))["builds"]}
    ours = [bid for bid, b in data.items() if b.get("role") == "tank" and SM.mode_of(b) == "raid" and SM.spec_of(cls, b) == spec]
    hand = R.SPECS[cls][entry]["builds"][0]   # run.py's reference: the first of the entry's builds, the hand draft
    trees = R.load_trees(repo, cls)
    if "ref" not in st:
        row = A.bench(R.SPECS[cls][entry], repo, [{"label": "ref", "talents": R.talents_string(trees, R.alloc_of(data[hand]))}], REF_FIGHTS, 77,
                      "raid", f"deeptank-ref-{cls}").get("ref") or {}
        if not (row.get("threat") and row.get("dtps")):
            raise SystemExit(f"no reference run for {hand}: {row.get('error', 'no output')}")
        st["ref"] = {"build": hand, "threat": row["threat"], "dtps": row["dtps"], "fights": REF_FIGHTS}
        save()
    ref = st["ref"]
    space = MLT.Space(cls, spec)
    starts = [R.alloc_of(data[b]) for b in ours] + MLT.preset_allocs(cls, R.SPECS[cls][entry], repo) + MLT.popular_allocs(cls)
    starts = [x for x in starts if space.valid(x)]
    space.protect = MLT.protected(cls, [entry], repo, "raid", starts)
    space.start_splits = [space.split(x) for x in starts]
    log(f"== deep optimisation of the {cls} tank ({spec}, {entry}): {len(starts)} valid starts; our builds {', '.join(ours)}; "
        f"reference {hand} (threat {ref['threat']:.1f}/s, damage taken {ref['dtps']:.1f}/s); kept: {', '.join(sorted(space.protect)) or 'none'}")
    t0 = time.time()
    for cyc in range(len(st["cycles"]) + 1, a.cycles + 1):
        prev = st["cycles"][-1] if st["cycles"] else None
        sim = TankSim(cls, entry, repo, f"deeptank-{cls}", ref)
        opts = MLT.defaults(**(DEEP if cyc == 1 else QUICK), seed=300 + cyc)
        extra = [flat_of(c["winner"]["allocation"]) for c in st["cycles"]]
        rec, win = MLT.optimize(space, {entry: sim}, starts + extra, opts, log)
        c = {"cycle": cyc, "winner": rec["winner"], "runner_up": rec.get("runner_up"), "gap_to_runner_up": rec.get("gap_to_runner_up"),
             "runs": [{k: v for k, v in r.items() if k != "trace"} for r in rec["runs"]], "runs_agree": rec["runs_agree"], "race": rec["race"],
             "certificate": rec["certificate"], "important_features": rec.get("important_features"), "simulated_builds": rec["simulated_builds"],
             "minutes": rec["minutes"]}
        log(f"  [{cyc}] winner {rec['winner']['split']} tank value {rec['winner']['dps']:.4f}; runs agreeing {rec['runs_agree']}/{len(rec['runs'])}")
        c["rotation_changed"] = False if SMOKE else retune(cls, entry, flat_of(rec["winner"]["allocation"]), repo)
        st["cycles"].append(c)
        save()
        if prev and flat_of(prev["winner"]["allocation"]) == flat_of(rec["winner"]["allocation"]) and not c["rotation_changed"]:
            st["converged"] = cyc
            save()
            break
    win = flat_of(st["cycles"][-1]["winner"]["allocation"])
    sim = TankSim(cls, entry, repo, f"deeptank-{cls}", ref)
    if "two_move" not in st:
        log(f"== two-move check from {space.split(win)}")
        new, steps = (MLT.two_move_certificate(space, sim, win, log, screen=200, conf=(1000, 2000), top=5, expand_top=2, rounds=1)
                      if SMOKE else MLT.two_move_certificate(space, sim, win, log))
        st["two_move"] = {"steps": steps, "moved": new != win}
        if new != win:
            win = new
            st["cycles"][-1]["winner"] = dict(st["cycles"][-1]["winner"], allocation=by_tree(space, new), split=space.split(new), moved_by_two_move_check=True)
        save()
    if "final" not in st:
        rows = {"deep winner": win} | {bid: R.alloc_of(data[bid]) for bid in ours}
        res = sim.run(list(rows.values()), FINAL_FIGHTS, 41)
        st["final"] = {k: {"value": round(v, 4), "se": round(sd / math.sqrt(FINAL_FIGHTS), 4)} for k, (v, sd) in zip(rows, res)}
        save()
        log("  final race: " + ", ".join(f"{k} {v['value']:.4f}" for k, v in sorted(st["final"].items(), key=lambda kv: -kv[1]["value"])))
    st["minutes"] = round((time.time() - t0) / 60, 1) + st.get("minutes", 0)
    save()
    if SMOKE:
        log("== done (smoke test)")
        return
    write_build(cls, spec, entry, hand, st, data, ours, space)
    save()
    report(cls, spec, entry, st)
    log("== done")


def write_build(cls, spec, entry, hand, st, data, ours, space):
    """The winner as `<spec slug>-ml-tank` when 0.5% or more ahead of every tank build of ours of the spec (else the search confirms the
    best of them), `replaces` at 2% or more over the hand draft; tidied by the filler audit and added to the entry's builds."""
    from fmt_json import dumps  # noqa: E402
    fin = st["final"]
    w = fin["deep winner"]["value"]
    others = {k: v["value"] for k, v in fin.items() if k != "deep winner"}
    bid = f"{SM.slug(spec)}-ml-tank"
    best = max((k for k in others if k != bid), key=others.get, default=None)
    if best and w < others[best] * 1.005:
        st["build"] = {"written": None, "why": f"confirms {best} ({w / others[best] - 1:+.2%})"}
        log(f"  no build: the search confirms {best} ({w / others[best] - 1:+.2%})")
        return
    gain = w / fin[hand]["value"] - 1 if hand in fin else None
    win = st["cycles"][-1]["winner"]
    tm = (st.get("two_move", {}).get("steps") or [{}])[-1]
    b = {"id": bid, "name": f"{SM.spec_name(cls, spec)} — Raid tank (machine-learning search)", "role": "tank", "content": "raid", "tier": "draft",
         "spec": spec, "generated": TODAY, "derived": "raid",
         "summary": (f"The {SM.spec_name(cls, spec)} tank build the machine-learning talent search found in the community simulator on {TODAY} "
                     f"(raidsim/deep_tank.py: a random forest guiding a genetic search over every legal build of the spec, scored on tank "
                     f"value: threat per second and damage taken under boss melee; the rotation tuned with it; races on fresh seeds; every "
                     f"build one or two moves from the winner checked). The simulator's model of the beta, not an in-game measurement."),
         "allocation": by_tree(space, flat_of(win["allocation"])), "core": [], "flex": [],
         "notes": [f"Final race over {FINAL_FIGHTS:,} fights: tank value {w:.3f} ± {fin['deep winner']['se']:.3f} (relative to {hand} over "
                   f"{st['ref']['fights']:,} fights); " + ", ".join(f"{k} {v:.3f}" for k, v in sorted(others.items(), key=lambda kv: -kv[1])) + ".",
                   f"Independent runs agreeing in the last cycle: {st['cycles'][-1]['runs_agree']}/{len(st['cycles'][-1]['runs'])}; two-move check: "
                   f"{tm.get('one_move', 0)} one-move and {tm.get('two_move', 0):,} two-move builds, none better."],
         "open_questions": [f"A machine-searched {SM.spec_name(cls, spec)} tank build: check its threat and survival against the community's "
                            f"tank builds at launch (the simulator models no threat from other players, taunts or tank swaps)."],
         "sources": []}
    if gain is not None and gain >= 0.02:
        b["replaces"] = hand
        b["notes"].insert(0, f"{gain:+.1%} tank value over the hand draft {hand} (over the 2% bar: the spec's tank pick; the hand draft stays as the alternative).")
    bp = paths.builds_json("forever", cls)
    d = json.load(open(bp, encoding="utf-8"))
    d["builds"] = [x for x in d["builds"] if x["id"] != bid] + [b]
    bp.write_text(dumps(d) + "\n", encoding="utf-8")
    SB = _load("spec_builds_tank", ROOT / "_reference/data/spec_builds.py")
    SB.add_to_entry(cls, entry, bid)
    MB = _load("ml_builds_tank", HERE / "ml_builds.py")
    MB.tidy(cls, entry, bid, setting="raid")
    st["build"] = {"written": bid, "gain_vs_hand": gain}
    log(f"  wrote {bid}" + (f" ({gain:+.1%} vs {hand})" if gain is not None else ""))


def report(cls, spec, entry, st):
    """<class>/research/raid/deep-optimization-tank.md"""
    fin = st["final"]
    w = st["cycles"][-1]["winner"]
    tm = (st.get("two_move", {}).get("steps") or [{}])[-1]
    o = [f"# {cls.capitalize()} {SM.spec_name(cls, spec)}: deep optimisation of the tank (generated)", "",
         f"> Generated by `_reference/data/raidsim/deep_tank.py` on {TODAY}; record `_reference/data/raidsim/deep/{cls}-tank.json`. Do not hand-edit.", "",
         f"Talents and rotation were tuned in turns until neither moved, in the `{entry}` entry's raid setting and gear; the winner was checked "
         "against every build one or two talent moves away and raced against our tank builds over "
         f"{FINAL_FIGHTS:,} fights. Tank value: the raid-tank profile's weights on threat per second and on damage avoided, relative to the "
         f"hand draft {st['ref']['build']} (1.000). The community simulator's model of the beta ({SI.label(st.get('commit') or R.git_commit(R.repo_path(argparse.Namespace(repo=None))), short=True)} with this "
         "project's patches), not in-game measurements; it models no threat from other players, taunts or tank swaps.", "",
         f"**Winner:** [{w['split']}]({RSH.tf_link(cls, flat_of(w['allocation']))}), tank value {fin['deep winner']['value']:.4f} ± "
         f"{fin['deep winner']['se']:.4f}; cycles {len(st['cycles'])}" + (f" (converged in cycle {st['converged']})" if st.get("converged") else "")
         + f"; independent runs agreeing in the last cycle {st['cycles'][-1]['runs_agree']}/{len(st['cycles'][-1]['runs'])}."
         + (f" Build: `{st['build']['written']}`." if (st.get("build") or {}).get("written") else f" {(st.get('build') or {}).get('why', '')}."), "",
         f"| Build | Tank value ({FINAL_FIGHTS:,} fights) |", "|---|---|"]
    o += [f"| {k} | {v['value']:.4f} ± {v['se']:.4f} |" for k, v in sorted(fin.items(), key=lambda kv: -kv[1]["value"])]
    o += ["", f"Two-move check: {tm.get('one_move', 0)} one-move and {tm.get('two_move', 0):,} two-move builds"
          + (f"; best {tm['confirmed'][0][1]:+.2%} ({tm['confirmed'][0][0]})" if tm.get("confirmed") else "") + ".", "",
          "| Cycle | Winner | Tank value (race) | Runs agreeing | Rotation changed |", "|---|---|---|---|---|"]
    o += [f"| {c['cycle']} | {c['winner']['split']} | {c['winner']['dps']:.4f} | {c['runs_agree']}/{len(c['runs'])} | {'yes' if c.get('rotation_changed') else 'no'} |"
          for c in st["cycles"]]
    p = paths.scenario_dir(cls, "raid") / "deep-optimization-tank.md"
    p.write_text("\n".join(o) + "\n", encoding="utf-8")
    log(f"wrote {p.relative_to(ROOT).as_posix()}")


if __name__ == "__main__":
    main()
