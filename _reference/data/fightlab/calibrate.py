"""Calibrate the expected-value scorer's leveling inputs to the fight lab.

    python _reference/data/fightlab/calibrate.py mage --spec frost-leveling --profile leveling-st \
        --builds opt-frost-leveling-leveling-st leveling-frost --levels 30,60 --fights 2000 --write

What it does
1. Simulates each build at every level in `--levels`: the full build and the build minus each talent (common random
   numbers). A talent's sim value at a level is the relative increase in time per kill when it is removed
   (fight + downtime + deaths); the fit target is the mean over the levels.
2. Writes the measured damage shares into the leveling profiles' `profile_overrides` of the spec model (the base share is
   the raid split, fitted by raidsim/calibrate.py) and the leveling time split (fight / downtime / death) from what the first
   build's rotation produced at the highest level.
   Pass several builds (the hand draft, the optimizer's current build and its earlier candidates, saved as
   `<class>/research/leveling/fightlab/candidates/*.json`; a build id ending in .json is read from that file): the fit
   then averages each talent's marginal over builds instead of chasing one build's interactions.
3. For the talents in FIT, scales the manual effect values that apply to the leveling profiles
   (`modes: [leveling-st, solo-60]`) until the scorer's value of the same removal, on the same relative-to-the-build
   scale, matches the sim (bisection, two passes for interactions). Effects for raid / AoE modes are left as they
   were (split off into their own `modes` where an effect used to apply to every mode). Talents whose scorer value is
   already within tolerance are restructured but not scaled; talents whose sim value is inside the noise floor are
   left alone; a fit that cannot reach the target (the model's channel saturates, e.g. hit) keeps its values.
4. Prints sim vs scorer before/after per level and, with --write, saves the spec and manual files with notes naming
   the fit, plus `<class>/research/leveling/fightlab/<spec>-calibration.json`.

Scale: the scorer's score is the fraction of time per kill saved against a talentless character, so its value of a
removal on the sim's scale is (score_with - score_without) / (1 - score_with).
"""
import argparse
import datetime
import collections
import copy
import json
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[2]
sys.path.insert(0, str(ROOT / "_reference/data"))
sys.path.insert(0, str(ROOT / "_reference/data/scorer"))
sys.path.insert(0, str(HERE))   # last so that `run` is the fight lab runner, not the scorer's
sys.path.append(str(pathlib.Path(__file__).resolve().parents[1]))   # _reference/data: paths.py
import paths  # noqa: E402
import splitfx  # noqa: E402  (scorer/splitfx.py: the shared split of effect entries)

from run import MODULES, allocation_at, apply_overrides, load_build, simulate  # noqa: E402
from fmt_json import dumps  # noqa: E402

LEVELING_MODES = ["leveling-st", "solo-60"]
OTHER_MODES = ["raid", "leveling-aoe", "heal", "tank"]

TOLERANCE = 0.01      # keep an entry whose scorer value is within 1 point of the sim ...
MIN_RATIO = 0.8       # ... or within 80-125% of it
NOISE = 0.01          # sim values below this are noise: the entry is left alone
FLOOR = 0.005         # never fit a talent below this value (utility the sim cannot see)
MAX_VALUE = 1.5       # cap on any fitted effect value (a dmg of 1.5 = +150%); beyond it the fit is reported as capped
CHANNEL_MAX = {"crit": 0.5, "hit": 0.2}   # tighter caps where the scorer saturates (crit stops at 100%; see raidsim/calibrate.py)


def ev_relative(with_score, without_score):
    return (with_score - without_score) / max(1e-9, 1.0 - with_score)


def expand(effects):
    out = []
    for e in effects:
        e = dict(e)
        if "per_rank" in e and "values" not in e:
            e["values"] = [round(e["per_rank"] * r, 6) for r in range(1, 6)]
        out.append(e)
    return out


def applies_to_leveling(e):
    modes = e.get("modes")
    return not modes or "leveling" in modes or any(m in modes for m in LEVELING_MODES)


NOT_SIMULATED = re.compile(r"\bnot (used|modell?ed|simulated)\b|travel", re.I)


def leveling_split(entry, how, spec_id, other_specs, with_utility=False):
    """Split an entry into (effects to fit for spec_id in LEVELING_MODES, everything else): scorer/splitfx.split, which keeps
    every other model's values and this model's other modes, and merges overlapping copies. Utility (raid-buff values) and
    source switches are never scaled."""
    lev_fit, rest = splitfx.split(expand(entry["effects"]), LEVELING_MODES, spec_id, other_specs,
                                  ("enable", "disable") if with_utility else splitfx.NO_FIT)   # a simulated talent's utility is part of what the lab measures
    if isinstance(how, tuple) and how[0] == "replace":
        lev_fit = [dict(x, modes=list(LEVELING_MODES), specs=[spec_id]) for x in expand(how[1])]
    return lev_fit, rest


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


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("cls")
    ap.add_argument("--spec", default="frost-leveling")
    ap.add_argument("--profile", default="leveling-st")
    ap.add_argument("--builds", nargs="+", required=True)
    ap.add_argument("--levels", default="30,60")
    ap.add_argument("--fights", type=int, default=2000)
    ap.add_argument("--seed", type=int, default=1)
    ap.add_argument("--write", action="store_true")
    ap.add_argument("--set", action="append", default=[], help="tables.py overrides for every simulation (MOBS_PER_PULL=4 for the AoE profile)")
    ap.add_argument("--share-build", help="build whose measured damage split becomes the model's leveling shares (default: the first of --builds); "
                                         "use one that keeps every source, e.g. a pet build for a model whose builds may take Lone Wolf")
    a = ap.parse_args()
    if a.share_build and a.share_build not in a.builds:
        a.builds.append(a.share_build)   # the share build is simulated like the others
    apply_overrides(a.set)
    if a.profile == "leveling-aoe":   # fit the AoE profile's own mode; every other mode keeps its values
        globals()["LEVELING_MODES"] = ["leveling-aoe"]
        globals()["OTHER_MODES"] = ["raid", "leveling-st", "solo-60", "heal", "tank"]
    levels = [int(x) for x in a.levels.split(",")]
    import importlib
    class_module = importlib.import_module(MODULES[a.cls][0])   # per-class calibration metadata: which sources the shares map to, what to fit
    SHARE_SOURCE, NEW_SOURCES, FIT = class_module.SHARE_SOURCE, class_module.NEW_SOURCES, class_module.FIT
    SHARE_SOURCE = getattr(class_module, "SHARE_SOURCE_BY_SPEC", {}).get(a.spec, SHARE_SOURCE)   # a second playstyle maps its damage differently

    # ---------------------------------------------------------------- 1. simulate
    sim = {L: {} for L in levels}
    for L in levels:
        for bid in a.builds:
            alloc = allocation_at(load_build(a.cls, bid), L)
            base = simulate(a.cls, alloc, L, a.spec, a.fights, a.seed, 0)
            removed = {name: simulate(a.cls, {k: v for k, v in alloc.items() if k != name}, L, a.spec, a.fights, a.seed, 0) for name in alloc}
            sim[L][bid] = {"alloc": alloc, "base": base, "removed": removed}
            print(f"sim L{L} {bid}: {base['time_per_kill']:.1f}s per kill, fight {base['fight_mean']:.1f}s, downtime {base['downtime_per_kill']:.1f}s, deaths/100 {base['deaths_per_100']:.1f}")

    def sim_value(L, name):
        for bid in a.builds:
            d = sim[L][bid]
            if name in d["removed"]:
                r, b = d["removed"][name], d["base"]
                return (r["time_per_kill"] - b["time_per_kill"]) / b["time_per_kill"], bid
        return None, None

    def sim_target(name):
        vals = [sim_value(L, name)[0] for L in levels]
        vals = [v for v in vals if v is not None]
        return (sum(vals) / len(vals)) if vals else None

    # ---------------------------------------------------------------- 2. spec model from the measured rotation
    spec_path = ROOT / "_reference/data/scorer/specs" / f"{a.cls}.json"
    specs = json.load(open(spec_path, encoding="utf-8"), object_pairs_hook=collections.OrderedDict)
    model = specs["models"][a.spec]
    top = max(levels)
    share_bid = a.share_build or a.builds[0]
    main_base = sim[top][share_bid]["base"]
    shares = main_base["shares"]
    by_id = {s["id"]: s for s in model["sources"]}
    for spell, sid in SHARE_SOURCE.items():
        if sid not in by_id and sid in NEW_SOURCES and shares.get(spell, 0) > 0.005:
            model["sources"].append(collections.OrderedDict(NEW_SOURCES[sid]))
            by_id[sid] = model["sources"][-1]
    # leveling shares go into the leveling profiles' overrides; the base share (the raid split, fitted by raidsim/calibrate.py) stays
    lev = {}
    for sid, s in by_id.items():
        spell = next((sp for sp, i in SHARE_SOURCE.items() if i == sid), None)
        if not s.get("max_level"):
            lev[sid] = shares.get(spell, 0.0) if spell is not None else s.get("profile_overrides", {}).get(LEVELING_MODES[0], {}).get("share", s["share"])
    tot = sum(lev.values()) or 1.0
    for s in model["sources"]:
        if s["id"] in lev:
            for pid in LEVELING_MODES:
                s.setdefault("profile_overrides", collections.OrderedDict())
                s["profile_overrides"].setdefault(pid, collections.OrderedDict())["share"] = round(lev[s["id"]] / tot, 3)
    fight, down, death = main_base["fight_mean"], main_base["downtime_per_kill"], main_base["death_time_per_kill"]
    drink = main_base.get("drink_per_kill", 0.0)
    eat = main_base.get("eat_per_kill", 0.0) + main_base.get("heal_per_kill", 0.0)   # health back: food, bandages, self-heals
    other = max(0.0, down - drink - eat)                                              # loot, travel, pet care
    tot_t = fight + down + death
    split = {"fight": fight / tot_t, "drink": drink / tot_t, "eat": eat / tot_t, "other": other / tot_t, "death": max(0.05, death / tot_t)}
    s_tot = sum(split.values())
    split = {k: round(v / s_tot, 3) for k, v in split.items()}
    model.setdefault("time", collections.OrderedDict())
    for pid in LEVELING_MODES:
        model["time"][pid] = split
    # fight-length coupling: how much downtime + death time move with fight time, from the removal experiments
    # (talents that change fight time by more than 5%): alpha = ln(other_wo / other_w) / ln(fight_wo / fight_w)
    import math
    alphas = []
    for bid in a.builds:
        d = sim[top][bid]
        b = d["base"]
        for name, r in d["removed"].items():
            fw, fwo = b["fight_mean"], r["fight_mean"]
            ow = b["downtime_per_kill"] + b["death_time_per_kill"]
            owo = r["downtime_per_kill"] + r["death_time_per_kill"]
            if fwo / fw > 1.05 and ow > 0 and owo > 0:
                alphas.append(math.log(owo / ow) / math.log(fwo / fw))
    alphas.sort()
    alpha = round(alphas[len(alphas) // 2], 2) if alphas else 0.0
    alpha = max(0.0, min(1.0, alpha))
    model["fight_coupling"] = collections.OrderedDict((pid, alpha) for pid in LEVELING_MODES)
    print(f"fight coupling alpha = {alpha} (median of {len(alphas)} removal experiments: {', '.join(f'{x:.2f}' for x in alphas)})")
    model["note"] = model.get("note", "").split(" Fight lab calibration")[0] + (
        f" Fight lab calibration ({datetime.date.today().isoformat()}, beta client 1.60.1.70009, build {pathlib.Path(share_bid).stem} at level {top}, {a.fights} fights): shares are the measured damage split "
        f"({', '.join(f'{k} {v * 100:.0f}%' for k, v in shares.items())}) and the leveling time split is fight {split['fight']:.0%} / drink {split['drink']:.0%} / eat {split['eat']:.0%} / other {split['other']:.0%} / death {split['death']:.0%} "
        f"of talent-affected time with fight_coupling {alpha} (downtime and deaths scale with fight length)."
        + (" Ice Lance is a source so Frost crit/damage talents scale with the Frozen-target loop." if a.cls == "mage" else ""))
    if a.write:
        spec_path.write_text(dumps(specs), encoding="utf-8")
        print(f"wrote {spec_path.relative_to(ROOT)}: time split {split}")

    # ---------------------------------------------------------------- 3. fit the manual entries
    from optimize import Optimizer  # noqa: E402  (reads the spec file just written)
    man_path = ROOT / "_reference/data/scorer/effects/forever" / f"{a.cls}.manual.json"
    manual = json.load(open(man_path, encoding="utf-8"), object_pairs_hook=collections.OrderedDict)
    opt = Optimizer("forever", a.cls, a.spec, a.profile)
    other_specs = [m for m in specs["models"] if m != a.spec]

    def ev_value(L, bid, name):
        alloc = sim[L][bid]["alloc"]
        opt._cache.clear()
        with_s = opt.score(alloc, L)
        return ev_relative(with_s, opt.score({k: v for k, v in alloc.items() if k != name}, L))

    def ev_mean(name):
        vals = []
        for L in levels:
            sv, bid = sim_value(L, name)
            if sv is not None:
                vals.append(ev_value(L, bid, name))
        return sum(vals) / len(vals) if vals else None

    plan = {}
    for name, how in FIT.items():
        target = sim_target(name)
        if target is None:
            continue
        entry = manual.get(name) or {"note": "Parsed values kept for the other modes; leveling values fitted to the fight lab.", "effects": copy.deepcopy(opt.effects[name]["effects"])}
        before = ev_mean(name)
        mech = getattr(class_module, "MECHANICS", {}).get(name)
        sim_ok = mech is not None and not NOT_SIMULATED.search(mech)   # the lab plays this talent: what it measures is its value, zero included
        noise = (not sim_ok) and abs(target) < NOISE and before < 2 * NOISE   # the lab cannot see it and the scorer's value is small: keep the entry as it is
        lev, other = leveling_split(entry, "scale" if noise else how, a.spec, other_specs, with_utility=sim_ok)   # (never swap a template in for a noise talent)
        lev = splitfx.seed_from_parsed(lev, expand(entry["effects"]), expand(opt.effects[name].get("parsed") or []), LEVELING_MODES,
                                       set(LEVELING_MODES) | {"leveling"}, a.spec)   # a new model valued through the tooltip fallback
        reseeded = False
        if not noise and target > NOISE:   # an earlier fit left every value at zero but the lab measures it: start again from the tooltip
            seeded = splitfx.reseed_zero(lev, expand(entry["effects"]), expand(opt.effects[name].get("parsed") or []), LEVELING_MODES, a.spec)
            reseeded, lev = seeded is not lev, seeded
        plan[name] = {"lev": lev, "other": other, "entry": entry, "target": target, "k": 1.0, "before": before, "how": "noise" if noise else "kept",
                      "base": dict(opt.effects[name]), "sim_ok": sim_ok, "reseeded": reseeded}

    def apply(name, k):
        p = plan[name]
        opt.effects[name] = dict(p["base"], effects=expand(p["other"]) + expand(scaled(p["lev"], k)), source="manual")   # keeps parsed, kinds, needs_pet, max
        opt._cache.clear()

    for name in plan:
        apply(name, 1.0)
    for _pass in range(3):
        for name, p in sorted(plan.items(), key=lambda kv: -kv[1]["target"]):
            target = p["target"]
            if p["how"] == "noise":
                continue
            target = max(0.0, target) if p["sim_ok"] else max(FLOOR, target)   # the floor is for value the lab cannot see
            cur = ev_mean(name)
            tol = TOLERANCE if (not p["sim_ok"] or target >= NOISE) else 0.002
            if abs(cur - target) <= tol or (target >= NOISE and MIN_RATIO <= cur / target <= 1 / MIN_RATIO):
                continue
            mx = opt.tree.info[name][2]   # the talent's ranks: a per_rank expansion runs to 5
            caps = [CHANNEL_MAX.get(e.get("channel"), MAX_VALUE) / abs(v) for e in expand(p["lev"]) for v in e.get("values", [0])[:mx] if v]
            absolute = any(e.get("channel") in ("resource_cost",) for e in expand(p["lev"]))   # energy / rage / mana units, not a multiplier: no cap
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
                p["k"] = hi
                p["how"] = "capped"
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

    # ---------------------------------------------------------------- 4. report + write
    head = f"{'talent':<22} {'sim mean':>8} {'EV before':>9} {'EV after':>8} {'scale':>6} {'how':>9}" + "".join(f" | L{L} sim   EV" for L in levels)
    print("\n" + head)
    rows = []
    for name, p in sorted(plan.items(), key=lambda kv: -kv[1]["target"]):
        after = ev_mean(name)
        per = []
        for L in levels:
            sv, bid = sim_value(L, name)
            per.append((L, sv, ev_value(L, bid, name) if sv is not None else None))
        rows.append({"talent": name, "sim": p["target"], "ev_before": p["before"], "ev_after": after, "scale": p["k"], "how": p["how"],
                     "per_level": [{"level": L, "sim": sv, "ev": ev} for L, sv, ev in per]})
        line = f"{name:<22} {p['target'] * 100:7.1f}% {p['before'] * 100:8.1f}% {after * 100:7.1f}% {p['k']:6.2f} {p['how']:>9}"
        for L, sv, ev in per:
            line += f" | {(sv * 100 if sv is not None else float('nan')):6.1f}% {(ev * 100 if ev is not None else float('nan')):5.1f}%"
        print(line)
    if a.write:
        n_written = 0
        for name, p in plan.items():
            if p["how"] in ("noise", "dead"):
                continue
            entry = collections.OrderedDict()
            old_note = p["entry"].get("note", "").split(" Fight lab calibration")[0]
            what = {"fitted": f"leveling-st/solo-60 values scaled x{p['k']:.2f} to match",
                    "approx": f"leveling-st/solo-60 values scaled x{p['k']:.2f} (the channel saturates before the target)",
                    "kept": "already within tolerance, leveling-st/solo-60 effects split off unchanged",
                    "capped": f"leveling-st/solo-60 values scaled x{p['k']:.2f}, the cap on effect size stops short of the target"}[p["how"]]
            if p.get("reseeded"):
                what = "re-seeded from its tooltip (an earlier fit had left its values at zero), " + what
            entry["note"] = old_note + (f" Fight lab calibration ({datetime.date.today().isoformat()}, levels {a.levels}): removing it costs {p['target'] * 100:.1f}% time per kill in the simulator "
                                        f"(scorer said {p['before'] * 100:.1f}% on the same scale); {what} ({ev_mean(name) * 100:.1f}%). Other modes unchanged.")
            entry["effects"] = expand(p["other"]) + expand(scaled(p["lev"], p["k"]))
            manual[name] = entry
            n_written += 1
        man_path.write_text(dumps(manual), encoding="utf-8")
        print(f"wrote {man_path.relative_to(ROOT)} ({n_written} entries written, {sum(1 for p in plan.values() if p['how'] == 'fitted')} fitted)")
        out = {"class": a.cls, "spec": a.spec, "profile": a.profile, "levels": levels, "fights": a.fights, "builds": a.builds, "shares": shares, "time_split": split, "talents": rows}
        cal_path = paths.fightlab_dir(a.cls) / f"{a.spec}-calibration.json"
        cal_path.write_text(json.dumps(out, indent=1), encoding="utf-8")
        print(f"wrote {cal_path.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
