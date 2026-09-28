"""Fit the scorer's healer model to the healer lab.

    python _reference/data/heallab/calibrate.py <class> [--builds <ids or .json files>] [--runs 60] [--write]

1. Runs the lab with removals over the builds (the hand draft, the optimizer export and saved candidates by default) and
   takes every talent's capacity loss as its value; the fit target is the mean over the builds it appears in (a joint fit:
   values are in-build marginals).
2. Writes the lab's healing split into the healer model's source shares (`scorer/specs/<class>.json`).
3. Scales each simulated talent's heal-mode effects (`modes: ["heal"]`, tagged `specs: [<model>]`) until the scorer's removal
   value matches the lab's, within tolerance; talents whose mechanics the lab does not simulate keep their manual values.
   With --write, saves the manual file (notes name the fit) and `<class>/raid/heallab/<spec>-calibration.json`.
"""
import argparse
import collections
import copy
import datetime
import importlib
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[2]
sys.path.insert(0, str(ROOT / "_reference/data"))
sys.path.insert(0, str(ROOT / "_reference/data/scorer"))
sys.path.insert(0, str(HERE))   # first: the lab's run.py, not the scorer's
sys.path.append(str(pathlib.Path(__file__).resolve().parents[1]))   # _reference/data: paths.py
import paths  # noqa: E402
import engine as E  # noqa: E402
import run as labrun  # noqa: E402
from fmt_json import dumps  # noqa: E402

TOLERANCE = 0.01
MIN_RATIO = 0.8
FLOOR = 0.005
MAX_VALUE = 1.5
CHANNEL_MAX = {"crit": 0.5, "hit": 0.2}   # tighter caps where the scorer saturates (crit stops at 100%; see raidsim/calibrate.py)
NOISE = 0.005
FIT_MODES = ["heal"]
OTHER_MODES = ["raid", "leveling-st", "solo-60", "leveling-aoe", "tank"]
NO_FIT = ("utility", "enable", "disable")


def expand(effects):
    out = []
    for e in effects:
        e = dict(e)
        if "per_rank" in e and "values" not in e:
            e["values"] = [round(e["per_rank"] * r, 6) for r in range(1, 6)]
        out.append(e)
    return out


def scaled(effects, k):
    out = []
    for e in effects:
        e = dict(e)
        if "values" in e:
            e["values"] = [round(v * k, 6) for v in e["values"]]
        if "per_rank" in e:
            e["per_rank"] = round(e["per_rank"] * k, 6)
        out.append(e)
    return out


def applies_to_heal(e):
    modes = e.get("modes")
    return not modes or "heal" in modes or "raid-heal" in modes


def heal_split(entry, spec_id, other_specs):
    """(effects to fit for spec_id in heal mode, everything else): scorer/splitfx.split, shared with the fight lab and the
    raid sim."""
    import splitfx   # scorer/splitfx.py
    return splitfx.split(expand(entry["effects"]), FIT_MODES, spec_id, other_specs, NO_FIT)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("cls", choices=list(labrun.CLASSES))
    ap.add_argument("--builds", nargs="*")
    ap.add_argument("--runs", type=int, default=60)
    ap.add_argument("--steps", type=int, default=10)
    ap.add_argument("--write", action="store_true")
    a = ap.parse_args()
    labrun.T.apply_rotation(a.cls)   # the class's tuned heal-choice settings (rotation_opt.py)
    mod = importlib.import_module(labrun.CLASSES[a.cls])
    P = mod.PIPELINE
    spec = P["spec"]
    folder = paths.heallab_dir(a.cls) / "candidates"
    cands = sorted(str(p) for p in folder.glob(f"cand-{P['tag']}-*.json")) if folder.exists() else []
    ids = a.builds or [P["hand"], P["opt"]] + cands
    seeds = list(range(a.runs))
    # ---- 1. the lab with removals
    allocs, caps, per_talent, summaries = {}, {}, collections.defaultdict(list), {}
    for ref in ids:
        try:
            b = labrun.load_build(a.cls, ref)
        except StopIteration:
            print(f"  no build {ref}: skipped")
            continue
        al = labrun.alloc_of(b)
        allocs[b["id"]] = al
        h, cap, summ = labrun.measure(mod, al, seeds, a.steps)
        caps[b["id"]], summaries[b["id"]] = cap, summ
        print(f"  {b['id']:<36} capacity {cap:.3f}  HPS {summ['hps']:.0f}  overheal {summ['overheal_share'] * 100:.0f}%")
        for name in sorted(al):
            if name not in mod.Healer.SIMULATED:
                continue
            _, cap_wo, _ = labrun.measure(mod, {k: v for k, v in al.items() if k != name}, seeds, a.steps)
            per_talent[name].append((b["id"], (cap - cap_wo) / cap_wo if cap_wo else 0.0))
    # ---- 2. healing split -> the model's source shares
    spec_path = ROOT / "_reference/data/scorer/specs" / f"{a.cls}.json"
    specs = json.load(open(spec_path, encoding="utf-8"), object_pairs_hook=collections.OrderedDict)
    model = specs["models"][spec]
    main_id = next(iter(summaries))
    shares = summaries[main_id]["shares"]
    by_source = collections.defaultdict(float)
    unmatched = 0.0
    for spell, v in shares.items():
        sid = mod.Healer.SHARE_SOURCE.get(spell)
        if sid:
            by_source[sid] += v
        else:
            unmatched += v
    tot = sum(by_source.values()) or 1.0
    for s in model["sources"]:
        if s.get("max_level"):
            continue
        s["share"] = round(by_source.get(s["id"], 0.0) / tot, 4)
    model["note"] = model.get("note", "").split(" Healer lab shares")[0].rstrip() + (
        f" Healer lab shares ({datetime.date.today().isoformat()}, {main_id}): " + ", ".join(f"{k} {v / tot * 100:.0f}%" for k, v in sorted(by_source.items(), key=lambda kv: -kv[1]))
        + f"; {unmatched * 100:.0f}% of the healing came from talent-taught spells the model carries as talent effects.")
    print("  healing shares -> " + ", ".join(f"{k} {v / tot * 100:.0f}%" for k, v in by_source.items()) + f" (unmatched {unmatched * 100:.0f}%)")
    if a.write:
        spec_path.write_text(dumps(specs), encoding="utf-8")
    # ---- 3. fit
    from optimize import Optimizer
    man_path = ROOT / "_reference/data/scorer/effects/forever" / f"{a.cls}.manual.json"
    manual = json.load(open(man_path, encoding="utf-8"), object_pairs_hook=collections.OrderedDict)
    other_specs = [m for m in specs["models"] if m != spec]
    opt = Optimizer("forever", a.cls, spec, "raid-heal")

    def ev_value(bid, name):
        al = allocs[bid]
        opt._cache.clear()
        with_s = opt.score(al, 60)
        wo = opt.score({k: v for k, v in al.items() if k != name}, 60)
        return (with_s - wo) / (1.0 + wo)

    def ev_mean(name):
        vals = [ev_value(bid, name) for bid, _ in per_talent[name] if bid in allocs]
        return sum(vals) / len(vals) if vals else None

    plan = {}
    for name, obs in per_talent.items():
        target = sum(v for _, v in obs) / len(obs)
        entry_m = manual.get(name) or {"note": "Parsed values kept for the other modes; heal values fitted to the healer lab.", "effects": copy.deepcopy(opt.effects[name]["effects"])}
        before = ev_mean(name)
        if before is None:
            continue
        noise = abs(target) < NOISE and before < NOISE   # both say ~0: leave the entry alone
        fit, other = heal_split(entry_m, spec, other_specs)
        import splitfx   # scorer/splitfx.py
        fit = splitfx.seed_from_parsed(fit, expand(entry_m["effects"]), expand(opt.effects[name].get("parsed") or []), FIT_MODES, set(FIT_MODES) | {"raid-heal"}, spec, NO_FIT)
        reseeded = False
        if not noise and target > NOISE:   # an earlier fit left every value at zero but the lab measures it: start again from the tooltip
            seeded = splitfx.reseed_zero(fit, expand(entry_m["effects"]), expand(opt.effects[name].get("parsed") or []), FIT_MODES, spec, NO_FIT)
            reseeded, fit = seeded is not fit, seeded
        plan[name] = {"fit": fit, "other": other, "entry": entry_m, "target": target, "k": 1.0, "before": before, "how": "noise" if noise else "kept",
                      "base": dict(opt.effects[name]), "reseeded": reseeded}

    def apply(name, k):
        p = plan[name]
        opt.effects[name] = dict(p["base"], effects=expand(p["other"]) + expand(scaled(p["fit"], k)), source="manual")   # keeps parsed, kinds, needs_pet, max
        opt._cache.clear()

    for name in plan:
        apply(name, 1.0)
    for _pass in range(3):
        for name, p in sorted(plan.items(), key=lambda kv: -kv[1]["target"]):
            if p["how"] == "noise":
                continue
            target = max(0.0, p["target"])   # the simulator sees every damage / healing channel: no floor
            cur = ev_mean(name)
            tol = TOLERANCE if target >= NOISE else 0.002
            if abs(cur - target) <= tol or (target >= NOISE and MIN_RATIO <= cur / target <= 1 / MIN_RATIO):
                continue
            mx = opt.tree.info[name][2]   # the talent's ranks: a per_rank expansion runs to 5
            caps = [CHANNEL_MAX.get(e.get("channel"), MAX_VALUE) / abs(v) for e in expand(p["fit"]) for v in e.get("values", [0])[:mx] if v]
            absolute = any(e.get("channel") in ("resource_cost",) for e in expand(p["fit"]))
            kmax = 64.0 if absolute or not caps else min([64.0] + caps)   # all-zero effects: nothing to scale (64 as before)
            lo, hi = 0.0, min(kmax, max(1.0, p["k"]))
            apply(name, hi)
            while ev_mean(name) < target and hi < kmax:
                hi = min(kmax, hi * 2)
                apply(name, hi)
            if ev_mean(name) < 1e-9:   # the playstyle weights this kind of value to zero: nothing to fit, nothing to write
                apply(name, 1.0)
                p["k"], p["how"] = 1.0, "dead"
                if p["target"] > 2 * NOISE:
                    print(f"WARNING {name}: the simulator measures {p['target'] * 100:.1f}% but the model gives it no value for this playstyle (scorer/kinds.json weights)")
                continue
            if ev_mean(name) < target:
                p["k"], p["how"] = hi, "capped"
                continue
            for _ in range(30):
                mid = (lo + hi) / 2
                apply(name, mid)
                if ev_mean(name) < target:
                    lo = mid
                else:
                    hi = mid
            p["k"] = (lo + hi) / 2
            apply(name, p["k"])
            p["how"] = "fitted"
    print(f"\n{'talent':<28} {'lab':>7} {'EV before':>9} {'EV after':>8} {'scale':>6} {'how':>7}")
    rows = []
    for name, p in sorted(plan.items(), key=lambda kv: -kv[1]["target"]):
        after = ev_mean(name)
        rows.append({"talent": name, "lab": p["target"], "ev_before": p["before"], "ev_after": after, "scale": p["k"], "how": p["how"], "builds": [b for b, _ in per_talent[name]]})
        print(f"{name:<28} {p['target'] * 100:6.1f}% {p['before'] * 100:8.1f}% {after * 100:7.1f}% {p['k']:6.2f} {p['how']:>7}")
    if a.write:
        n = 0
        for name, p in plan.items():
            if p["how"] in ("noise", "dead"):
                continue
            e = collections.OrderedDict()
            old_note = p["entry"].get("note", "").split(" Healer lab calibration")[0]
            what = {"fitted": f"heal values scaled x{p['k']:.2f} to match", "kept": "already within tolerance, heal effects split off unchanged",
                    "capped": f"heal values scaled x{p['k']:.2f}, the cap on effect size stops short of the target"}[p["how"]]
            if p.get("reseeded"):
                what = "re-seeded from its tooltip (an earlier fit had left its heal values at zero), " + what
            e["note"] = old_note + (f" Healer lab calibration ({datetime.date.today().isoformat()}, {spec}): removing it costs {p['target'] * 100:.1f}% healing capacity in the lab "
                                    f"(scorer said {p['before'] * 100:.1f}% on the same scale); {what} ({ev_mean(name) * 100:.1f}%). Other modes unchanged.")
            e["effects"] = expand(p["other"]) + expand(scaled(p["fit"], p["k"]))
            manual[name] = e
            n += 1
        man_path.write_text(dumps(manual), encoding="utf-8")
        cal = paths.heallab_dir(a.cls) / f"{spec}-calibration.json"
        cal.parent.mkdir(parents=True, exist_ok=True)
        cal.write_text(json.dumps({"class": a.cls, "spec": spec, "runs": a.runs, "builds": list(allocs), "capacity": caps, "talents": rows, "shares": shares}, indent=1), encoding="utf-8")
        print(f"wrote {man_path.relative_to(ROOT)} ({n} entries, {sum(1 for p in plan.values() if p['how'] == 'fitted')} fitted) and {cal.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
