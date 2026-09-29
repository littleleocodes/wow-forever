"""Race the community's consensus talents in our builds (2026-09-29, user request: "did anything come from the community builds that
could help us with our builds?").

    python _reference/data/popular_swaps.py [classes] [--high 70] [--parts raid,level] [--iterations 20000] [--fights 2000]

For each build of ours that a scenario ranks (every build of a raid simulator entry that has a scorer model, dummy and raid settings;
tanks in the raid setting; the leveling hand draft and the main leveling model's optimizer build), every talent that at least --high %
of the talentsforever.com builds leading in the same tree take (popular.js `pickBy`) and the build skips becomes a swap build:
the talent at full ranks, the points taken back one at a time from the talent whose point the scorer values least in the build's
scenario, every step legal (validate_builds.check_state). A swap the tree cannot hold (tier gating) is recorded as such. Then the
swap races the unchanged build in the tool that ranks the scenario: raid sim (common random numbers, same seed) or fight lab
(levels 20-60, level-weighted time per kill; both builds get the scorer's leveling order so only the talents differ).
Results: `_reference/data/popular-swaps.json`; popular_picks.py --write puts them in `_reference/popular-picks.md`.
A swap that wins here is a lead for the usual pipeline (calibrate, optimize, race, adopt), not an adoption.
"""
import argparse
import datetime
import json
import pathlib
import subprocess
import sys
import tempfile

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[1]
OUT = HERE / "popular-swaps.json"
CLASSES = ["druid", "hunter", "mage", "paladin", "priest", "rogue", "shaman", "warlock", "warrior"]
LEVELS = [20, 30, 40, 50, 60]
LOOKAHEAD = {"mage": 12, "warrior": 20}


def weighted_mean(per_level):
    tot = sum(int(L) / 10 for L in per_level)
    return sum(v * int(L) / 10 for L, v in per_level.items()) / tot if tot else 0.0


def flat(alloc):
    return {n: r for items in alloc.values() for n, r in items if r}


def setup_paths():
    sys.path[:0] = [str(HERE / "scorer"), str(HERE)]


def consensus(cls, b, high):
    """Talents >= high % of the site's builds leading in b's lead tree take, that b skips: [(talent, pick %)]."""
    from popular_builds import latest_raw, load_popular
    pop = load_popular(latest_raw() / "popular.js")["classes"][cls.capitalize()]
    data = json.load(open(HERE / "forever-talents" / f"{cls}.json", encoding="utf-8"))
    lead = max(b["allocation"], key=lambda t: sum(r for _, r in b["allocation"][t]))
    if lead not in pop["pickBy"]:
        return lead, []
    al = flat(b["allocation"])
    out = []
    for tr, picks in zip(data["trees"], pop["pickBy"][lead]):
        for t, p in zip(tr["talents"], picks):
            if p >= high and t["name"] not in al:
                out.append((t["name"], p))
    return lead, sorted(out, key=lambda x: -x[1])


def make_swap(cls, b, add, opt, trees):
    """Legal swap build or (None, why)."""
    import validate_builds as vb

    def legal(al):
        state = {t: {n: r for n, r in al.items() if n in tr["talents"] and r} for t, tr in trees.items()}
        errs = []
        vb.check_state(trees, state, "x", errs)
        return not errs
    k = next(t["max"] for tr in trees.values() for n, t in tr["talents"].items() if n == add)
    al = flat(b["allocation"])
    al[add] = k
    removed = {}
    for _ in range(k):   # take the points back where the scorer loses least, keeping every intermediate state legal
        best = None
        for n, r in al.items():
            if n == add or not r:
                continue
            trial = dict(al)
            trial[n] -= 1
            if not legal(trial):
                continue
            v = opt.score(al, 60) - opt.score(trial, 60)
            if best is None or v < best[0]:
                best = (v, n)
        if best is None:
            return None, "not tested: no single point can come out without breaking tier gating or a prerequisite"
        al[best[1]] -= 1
        removed[best[1]] = removed.get(best[1], 0) + 1
    if not legal(al):
        return None, "not tested: the tree lacks the points below it (tier gating)"
    slug = "".join(c for c in add.lower().replace(" ", "-") if c.isalnum() or c == "-")
    alloc = {t: [[n, al[n]] for n in tr["talents"] if al.get(n)] for t, tr in trees.items()}
    return {"id": f"swap-{b['id']}-{slug}", "allocation": alloc,
            "change": f"+{add} {k}; -" + ", ".join(f"{n} {r}" for n, r in removed.items())}, None


def swaps_for(cls, bid, high, scen=None):
    """(build, lead, [(talent, pick, swap or None, why)]) for one build of ours."""
    import scenario_audit as sa
    import validate_builds as vb
    from optimize import Optimizer
    data = json.load(open(ROOT / cls / "research/talents/forever/proposed-builds.json", encoding="utf-8"))
    b = next(x for x in data["builds"] if x["id"] == bid)
    models = list(json.load(open(HERE / "scorer/specs" / f"{cls}.json", encoding="utf-8"))["models"])
    model, profile = scen or sa.model_profile(cls, b, models)
    lead, cons = consensus(cls, b, high)
    if not model or not cons:
        return b, lead, model, []
    opt = Optimizer("forever", cls, model, profile)
    trees = vb.load_forever()[cls]
    out = []
    for n, p in cons:
        sw, why = make_swap(cls, b, n, opt, trees)
        out.append((n, p, sw, why))
    return b, lead, model, out


# ---------------------------------------------------------------- parts

def part_raid(cls, a, tmp):
    sys.path.insert(0, str(HERE / "raidsim"))
    import run   # raidsim/run.py
    setup_paths()
    repo = run.repo_path(argparse.Namespace(repo=None))
    rows = []
    for name, entry in run.SPECS[cls].items():
        if name.startswith("_") or not isinstance(entry, dict) or "apl" not in entry or entry.get("rotation_only"):
            continue
        tank = bool(entry.get("tank"))
        profile = entry.get("profile", "raid-tank" if tank else "raid-dps")
        for bid in entry["builds"]:
            if bid.endswith(".json"):
                continue
            b, lead, model, sw = swaps_for(cls, bid, a.high, (name, profile))
            files = []
            for n, p, s, why in sw:
                if s:
                    f = pathlib.Path(tmp) / f"{s['id']}.json"
                    f.write_text(json.dumps(s), encoding="utf-8")
                    files.append(str(f))
            res = {}
            if files:
                for setting in (["raid"] if tank else ["dummy", "raid"]):
                    run.SETTING_OVERRIDE = setting
                    ns = argparse.Namespace(builds=[bid] + files, iterations=a.iterations, duration=120.0, seed=1, no_presets=True, deltas=None, write=False)
                    out = run.run_spec(cls, name, ns, repo)
                    res[setting] = {x["label"]: (x.get("value") if tank else x["dps"]) for x in out["results"]}
            for n, p, s, why in sw:
                row = {"scenario": "raid", "entry": name, "tank": tank, "build": bid, "lead": lead, "talent": n, "pick": p,
                       "change": s["change"] if s else None, "why": why}
                for setting, r in res.items():
                    base, v = r.get(bid), r.get(s["id"]) if s else None
                    row[setting] = {"base": base, "swap": v, "delta": (v / base - 1) if base and v else None}
                rows.append(row)
    return {"rows": rows}


def part_level(cls, a, tmp):
    sys.path.insert(0, str(HERE / "fightlab"))
    import run   # fightlab/run.py
    setup_paths()
    from optimize import Optimizer
    pipe = __import__(run.MODULES[cls][0]).PIPELINE
    spec = pipe["spec"]
    look = LOOKAHEAD.get(cls, 16)
    opt = Optimizer("forever", cls, spec, "leveling-st")

    def with_order(b):
        steps = opt.order(flat(b["allocation"]), lookahead=look)
        return dict(b, order=[{"levels": lv, "tree": t, "talent": n, "points": pts} for lv, t, n, pts in opt.compress_order(steps)])

    def race(b):
        per = {L: run.simulate(cls, run.allocation_at(b, L), L, spec, a.fights, 1, 0)["time_per_kill"] for L in LEVELS}
        return per, weighted_mean(per)
    rows = []
    for bid in dict.fromkeys([pipe["hand"], f"opt-{spec}-leveling-st"]):
        try:
            b, lead, model, sw = swaps_for(cls, bid, a.high, (spec, "leveling-st"))
        except StopIteration:
            continue
        if not any(s for _, _, s, _ in sw):
            rows += [{"scenario": "leveling", "spec": spec, "build": bid, "lead": lead, "talent": n, "pick": p, "change": None, "why": why}
                     for n, p, s, why in sw]
            continue
        base_per, base_w = race(with_order(b))
        print(f"  {bid:<40} {base_w:.2f}s per kill (level-weighted, scorer order)")
        for n, p, s, why in sw:
            row = {"scenario": "leveling", "spec": spec, "build": bid, "lead": lead, "talent": n, "pick": p, "change": s["change"] if s else None, "why": why}
            if s:
                per, w = race(with_order(s))
                row.update({"base": base_w, "swap": w, "delta": w / base_w - 1, "levels": {L: per[L] / base_per[L] - 1 for L in LEVELS}})
                print(f"    {s['change']:<60} {w:.2f}s ({(w / base_w - 1) * 100:+.1f}%)")
            rows.append(row)
    return {"rows": rows}


PARTS = {"raid": part_raid, "level": part_level}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("classes", nargs="*")
    ap.add_argument("--high", type=int, default=70)
    ap.add_argument("--parts", default="raid,level")
    ap.add_argument("--iterations", type=int, default=20000)
    ap.add_argument("--fights", type=int, default=2000)
    ap.add_argument("--part", help=argparse.SUPPRESS)
    ap.add_argument("--json", help=argparse.SUPPRESS)
    a = ap.parse_args()
    if a.part:
        with tempfile.TemporaryDirectory() as tmp:
            r = PARTS[a.part](a.classes[0], a, tmp)
        pathlib.Path(a.json).write_text(json.dumps(r), encoding="utf-8")
        return
    res = json.load(open(OUT, encoding="utf-8")) if OUT.exists() else {"classes": {}}
    res["high"] = a.high
    for cls in a.classes or CLASSES:
        for part in a.parts.split(","):
            with tempfile.TemporaryDirectory() as tmp:
                j = pathlib.Path(tmp) / "out.json"
                print(f"== {cls} {part}", flush=True)
                subprocess.run([sys.executable, __file__, cls, "--part", part, "--json", str(j), "--high", str(a.high),
                                "--iterations", str(a.iterations), "--fights", str(a.fights)], check=True)
                res["classes"].setdefault(cls, {})[part] = json.loads(j.read_text(encoding="utf-8"))["rows"]
            res["date"] = datetime.date.today().isoformat()
            OUT.write_text(json.dumps(res, indent=1) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
