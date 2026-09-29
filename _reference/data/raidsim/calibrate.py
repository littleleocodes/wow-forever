"""Calibrate the scorer's raid-mode talent values to the community simulator (the raid counterpart of fightlab/calibrate.py).

    python _reference/data/raidsim/calibrate.py druid --spec feral-cat-dps [--builds id ...] [--iterations 2000] [--write]

1. Runs every listed build (default: the spec's builds in specs.json plus saved raid candidates) through the simulator with each
   of its talents removed in turn (run.py --deltas): a talent's sim value is the DPS lost when it is removed, relative to the
   build without it; the fit target is the mean over the builds it appears in (joint fit: values are in-build marginals).
2. For every talent with a target beyond the noise floor, scales the manual effect values that apply to the raid mode
   (`modes: ["raid"]`, tagged `specs: [<spec>]` so other models keep theirs) until the scorer's value of the same removal, on
   the same scale ((score_with - score_without) / (1 + score_without)), matches the sim (bisection, three passes). Talents the
   scorer already has within tolerance keep their values; a fit that cannot reach the target keeps the cap.
3. With --write, saves the manual file with notes naming the fit and `<class>/research/raid/raidsim/<spec>-calibration.json`.

DPS profiles only (tanks and healers are not calibrated: the sim's tank numbers are DPS and threat, not the tank score).
Caveat: with the simulator's full raid buffs, talents that duplicate a buff someone else brings (Leader of the Pack, Trueshot
Aura, Moonkin Aura) measure zero — right for a buffed raid, wrong for the one who must bring it.
"""
import argparse
import collections
import copy
import datetime
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[2]
sys.path.insert(0, str(ROOT / "_reference/data"))
sys.path.insert(0, str(ROOT / "_reference/data/scorer"))
sys.path.insert(0, str(HERE))
sys.path.append(str(pathlib.Path(__file__).resolve().parents[1]))   # _reference/data: paths.py
import paths  # noqa: E402
from fmt_json import dumps  # noqa: E402
import run as raidrun  # noqa: E402  (this folder's run.py: the raid-sim driver)

# the same fit rules as fightlab/calibrate.py (copied: that module's name clashes with this one)
TOLERANCE = 0.01      # keep an entry whose scorer value is within 1 point of the sim ...
MIN_RATIO = 0.8       # ... or within 80-125% of it
FLOOR = 0.005         # never fit a talent below this value
MAX_VALUE = 1.5       # cap on any fitted effect value
CHANNEL_MAX = {"crit": 0.5, "hit": 0.2}   # tighter caps where the scorer saturates: crit stops at 100% (a +62% Winter's Chill fit capped Frostbolt's
                                          # crit and read 0 in other builds), hit at the miss floor


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

FIT_MODES = ["raid"]
OTHER_MODES = ["leveling-st", "solo-60", "leveling-aoe", "heal", "tank"]
NO_FIT = ("utility", "enable", "disable")   # raid-buff value (buff_value.py) and source switches: never scaled by a fit
NOISE = 0.005


# the mana limit (2026-09-27): on the training dummy nobody brings Blessing of Wisdom or Mana Spring, and every mana user loses 5-30%
# of its damage to mana (the simulator with every mana-only buff on: run.py's "dummy-surplus" setting). The scorer's spec model gets
# `mana_limit` {game: {profiles, loss, cap}}: the mana-bound damage (every source but white attacks and pets) shrinks by
# min(cap, max(0, loss - (sustain - 1))), so a mana talent is worth what it saves only while the build runs short (model.py). The
# sustain unit is the share of the mana-bound damage saved: the talent fit sets the mana talents' values in it from their removal
# runs, and the builds' deficits set only the loss and the cap. (A free slope ran away on the hunter: builds that differ in how much
# mana they spend, which the model does not see, pushed it to the edge of its range.)
MANA_PROFILES = {"raid-dps": ["raid-dps", "raid-dps-extwc"]}   # the profiles raced on the dummy (extwc differs from raid-dps only in Classic)
MANA_MIN_DEFICIT = 0.01   # no build loses 1% to mana: mana never binds, no limit
MANA_TOL = 0.002          # a lower cap must beat the plain ramp's fit by more than this RMS (points of deficit) to be chosen
MANA_CHANNELS = ("mana_cost", "regen", "sustain")   # effects that act on the scorer's sustain only (stat effects also move damage)
PURE_MANA_OK = MANA_CHANNELS + ("threat", "utility", "surv")   # a talent with only these in raid mode changes nothing but mana there


def scale_channels(effects, channels, k):
    out = []
    for e in effects:
        e = dict(e)
        if e.get("channel") in channels:
            if "values" in e:
                e["values"] = [round(v * k, 6) for v in e["values"]]
            if "per_rank" in e:
                e["per_rank"] = round(e["per_rank"] * k, 6)
        out.append(e)
    return out


def fit_mana_limit(pts):
    """(loss, cap, rms) that best reproduce the measured deficits: pts {build: (deficit, model sustain, model mana-bound share)};
    deficit = share x min(cap, max(0, loss - (sustain - 1))). Least squares on a grid for each cap; the highest cap within MANA_TOL
    of the best fit wins (a cap only where the data needs one: a mage's single Evocation costs 8 s and no more)."""
    import numpy as np
    d = np.array([v[0] for v in pts.values()])
    su = np.array([v[1] for v in pts.values()]) - 1.0
    f = np.array([v[2] for v in pts.values()])
    A = np.linspace(0.0, 3.0, 1201)[:, None]   # talent values still in an older unit can put the ramp far out: the fit brings them in
    raw = np.clip(A - su[None, :], 0.0, None)
    per_cap = []
    for ci in range(90, 0, -1):   # a shortfall never costs more than 90% of the mana-bound damage (a talentless build still casts)
        c = ci / 100
        sq = ((d[None, :] - f[None, :] * np.minimum(c, raw)) ** 2).sum(axis=1)
        i = int(np.argmin(sq))
        per_cap.append((c, float(A[i, 0]), float((sq[i] / len(d)) ** 0.5)))
    best = min(x[2] for x in per_cap)
    c, a, r = next(x for x in per_cap if x[2] <= best + MANA_TOL)
    return round(a, 4), c, r


def applies_to_raid(e):
    modes = e.get("modes")
    return not modes or any(m in modes for m in FIT_MODES)


def raid_split(entry, spec_id, other_specs):
    """(effects to fit for spec_id in FIT_MODES, everything else): scorer/splitfx.split, shared with the fight lab and the
    healer lab."""
    import splitfx   # scorer/splitfx.py
    return splitfx.split(expand(entry["effects"]), FIT_MODES, spec_id, other_specs, NO_FIT)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("cls")
    ap.add_argument("--spec", required=True)
    ap.add_argument("--builds", nargs="*")
    ap.add_argument("--iterations", type=int, default=2000)
    ap.add_argument("--repo")
    ap.add_argument("--write", action="store_true")
    ap.add_argument("--game", default="forever", choices=list(raidrun.GAMES))
    ap.add_argument("--shares-only", action="store_true", help="write the damage split only: no removal runs, the manual effect values stay")
    a = ap.parse_args()
    raidrun.set_game(a.game)
    game = a.game
    entry = raidrun.SPECS[a.cls][a.spec]
    profile = entry.get("profile", "raid-dps")
    if profile not in ("raid-dps", "raid-tank"):
        raise SystemExit("raid calibration covers the raid-dps and raid-tank profiles")
    if entry.get("rotation_only"):
        raise SystemExit(f"{a.spec} is a rotation-only target (no scorer spec model to calibrate)")
    if profile == "raid-tank":   # tank values live in the "tank" mode; the removal deltas combine threat and mitigation (run.py)
        FIT_MODES[:] = ["tank"]
        OTHER_MODES[:] = ["raid", "leveling-st", "solo-60", "leveling-aoe", "heal"]
    repo = raidrun.repo_path(a)
    cands = sorted(str(p) for p in (paths.raidsim_dir(a.cls, game) / "candidates").glob(f"cand-{a.spec}-*.json"))
    ids = a.builds or (entry["builds"] + cands)
    # ---- 1. simulate with removals
    args = argparse.Namespace(builds=ids, iterations=a.iterations, duration=120.0, seed=1, repo=a.repo, no_presets=True, write=a.write, deltas=[] if a.shares_only else ["all"])
    out = raidrun.run_spec(a.cls, a.spec, args, repo)
    sim = out["deltas"]   # build -> [{talent, ranks, sim_delta, ...}]
    per_talent = collections.defaultdict(list)
    apl_dep = set()
    unmeasured = set(entry.get("not_measured", {}))   # {talent: why}: values the simulator's standard target cannot show
    for bid, rows in sim.items():
        for r in rows:
            per_talent[r["talent"]].append((bid, r["sim_delta"]))
            if r.get("apl_dependent"):
                apl_dep.add(r["talent"])
    # ---- 1b. what running short of mana costs each build on the training dummy: the same builds with every mana-only buff on
    deficits, out_s = {}, None
    if game == "forever" and profile in MANA_PROFILES and out["sim"].get("setting") == "dummy" and not a.shares_only:
        prev = raidrun.SETTING_OVERRIDE
        raidrun.SETTING_OVERRIDE = "dummy-surplus"
        try:
            out_s = raidrun.run_spec(a.cls, a.spec, argparse.Namespace(builds=ids, iterations=a.iterations, duration=120.0, seed=1, repo=a.repo,
                                                                     no_presets=True, write=False, deltas=[]), repo)
        finally:
            raidrun.SETTING_OVERRIDE = prev
        full = {x["label"]: x["dps"] for x in out_s["results"] if x.get("dps")}
        for x in out["results"]:
            if x.get("dps") and full.get(x["label"]):
                deficits[x["label"]] = {"dps": x["dps"], "surplus": full[x["label"]], "oom_seconds": x.get("oom_seconds") or 0.0,
                                        "deficit": max(0.0, 1.0 - x["dps"] / full[x["label"]])}
        print("  mana deficit on the dummy (damage gained with every mana buff on): " + ", ".join(f"{k} {v['deficit'] * 100:.1f}%" for k, v in deficits.items()))
    # ---- 2. raid damage split from the simulator's actions -> the spec model's base shares (leveling shares live in profile_overrides)
    spec_path = ROOT / "_reference/data/scorer/specs" / f"{a.cls}.json"
    specs = json.load(open(spec_path, encoding="utf-8"), object_pairs_hook=collections.OrderedDict)
    # the split comes from the spec's share build when it names one (the build whose playstyle the rotation expresses: Frost's Ice
    # Lance share exists only with Fingers of Frost), else the first build
    # with a mana limit the split comes from the run with every mana buff on: the model's damage before the limit cuts the mana-bound
    # part (on the dummy a hunter out of mana 25 s of 120 shows fewer shots, and the limit would cut them twice)
    mana_binds = bool(deficits) and max(v["deficit"] for v in deficits.values()) >= MANA_MIN_DEFICIT
    res = out_s["results"] if (mana_binds and out_s) else out["results"]
    main = (next((x for x in res if x.get("source_shares") and x.get("label") == entry.get("share_build")), None)
            or next((x for x in res if x.get("source_shares")), None))
    if main and main["unmatched_share"] < 0.5:
        model = specs["models"][a.spec]
        for s in model["sources"]:
            if s.get("max_level"):
                continue
            share = main["source_shares"].get(s["id"], 0.0)
            if game == "forever":
                s["share"] = share
            else:   # the Classic split lives in the source's game override so the Forever base split stays
                s.setdefault("game_overrides", collections.OrderedDict()).setdefault(game, collections.OrderedDict())["share"] = share
        model["note"] = model.get("note", "").split(" Raid sim shares" if game == "forever" else " Classic raid sim shares")[0] + (
            f" {'Raid' if game == 'forever' else 'Classic raid'} sim shares ({datetime.date.today().isoformat()}, {main['label']} in the {'ElliotWood/Forever' if game == 'forever' else 'wowsims/classic'} simulator {out['sim']['commit']}"
            + (", every mana-only buff on: the split before the mana limit" if res is not out["results"] else "") + "): "
            + ", ".join(f"{k} {v * 100:.0f}%" for k, v in main["source_shares"].items()) + f"; {main['unmatched_share'] * 100:.0f}% of the damage matched no source.")
        if a.write:
            spec_path.write_text(dumps(specs), encoding="utf-8")
        print("  raid shares -> " + ", ".join(f"{k} {v * 100:.0f}%" for k, v in main["source_shares"].items()) + f" (unmatched {main['unmatched_share'] * 100:.0f}%)")
    elif main:
        print(f"  raid shares not written: {main['unmatched_share'] * 100:.0f}% of the damage matched no source")
    if a.shares_only:
        return
    # ---- 3. fit
    from optimize import Optimizer
    man_path = ROOT / "_reference/data/scorer/effects" / game / f"{a.cls}.manual.json"
    manual = json.load(open(man_path, encoding="utf-8"), object_pairs_hook=collections.OrderedDict)
    other_specs = [m for m in specs["models"] if m != a.spec]
    opt = Optimizer(game, a.cls, a.spec, profile)
    allocs = {}
    for bid in ids:
        b = raidrun.alloc_of(json.load(open(bid, encoding="utf-8")) if bid.endswith(".json") else next(x for x in json.load(open(ROOT / a.cls / raidrun.GAMES[game]["builds"], encoding="utf-8"))["builds"] if x["id"] == bid))
        allocs[pathlib.Path(bid).stem if bid.endswith(".json") else bid] = b

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
        entry_m = manual.get(name) or {"note": "Parsed values kept for the other modes; raid values fitted to the community simulator.", "effects": copy.deepcopy(opt.effects[name]["effects"])}
        before = ev_mean(name)
        if before is None:
            continue
        noise = abs(target) < NOISE and before < NOISE   # both say ~0: leave the entry alone
        fit, other = raid_split(entry_m, a.spec, other_specs)
        import splitfx   # scorer/splitfx.py
        fit = splitfx.seed_from_parsed(fit, expand(entry_m["effects"]), expand(opt.effects[name].get("parsed") or []), FIT_MODES, set(FIT_MODES), a.spec, NO_FIT)
        how = "apl" if name in apl_dep else "unmeasured" if name in unmeasured else "noise" if noise else "kept"
        reseeded = False
        if target > NOISE and how == "kept":   # an earlier fit (another setting) left every value at zero: start again from the tooltip
            seeded = splitfx.reseed_zero(fit, expand(entry_m["effects"]), expand(opt.effects[name].get("parsed") or []), FIT_MODES, a.spec, NO_FIT)
            reseeded, fit = seeded is not fit, seeded
        plan[name] = {"fit": fit, "other": other, "entry": entry_m, "target": target, "k": 1.0, "before": before, "how": how,
                      "base": dict(opt.effects[name]), "reseeded": reseeded}

    def fitted(p, k):
        """The raid effects at scale k. A mixed talent (damage and mana, Shadowform's -50% Shadow mana cost) under a mana limit keeps
        its mana part: scaling it with the damage part let the fit inflate every Shadow build's sustain when the limit was flat."""
        if p.get("mixed"):
            return [e if e.get("channel") in MANA_CHANNELS else scaled([e], k)[0] for e in expand(p["fit"])]
        return scaled(p["fit"], k)

    def apply(name, k):
        p = plan[name]
        opt.effects[name] = dict(p["base"], effects=expand(p["other"]) + expand(fitted(p, k)), source="manual")   # keeps parsed, kinds, needs_pet, max
        opt._cache.clear()

    for name in plan:
        apply(name, 1.0)
    ml = None
    if deficits:
        if mana_binds:
            first = not (opt.spec.get("mana_limit") or {}).get(game)
            mw = (opt.spec.get("mana_weight") or {}).get(profile, opt.profile.get("mana_weight", 0.0)) if isinstance(opt.spec.get("mana_weight"), dict) else opt.profile.get("mana_weight", 0.0)
            ml = collections.OrderedDict([("profiles", MANA_PROFILES[profile]), ("loss", 0.0), ("cap", 1.0)])
            opt.spec["mana_limit"] = dict(opt.spec.get("mana_limit") or {}, **{game: ml})
            opt._cache.clear()
            for p in plan.values():
                chans = {e.get("channel") for e in p["fit"]}
                p["mixed"] = bool(chans & set(MANA_CHANNELS)) and bool(chans - set(PURE_MANA_OK))
            if first and mw:
                # the raid values fitted under the linear mana term (weight mw) move to the limit's unit, the share of the mana-bound
                # damage saved: x mw / (mana-bound share), so every talent starts from the value it had (Meditation's regen 1.5 was
                # what a 0.4 weight needed to reach 18%); the fit then refines them
                bounds = [opt.score(allocs[b], 60, detail=True)["bound_frac"] for b in deficits if b in allocs]
                conv = mw / max(0.05, sum(bounds) / max(1, len(bounds)))
                for name, p in plan.items():
                    if any(e.get("channel") in MANA_CHANNELS for e in p["fit"]):
                        p["fit"] = scale_channels(p["fit"], MANA_CHANNELS, conv)
                        p["converted"] = conv
                        apply(name, p["k"])
                print(f"  mana values moved from the linear term (weight {mw}) to the limit's unit: x{conv:.2f}")
        elif opt.spec.get("mana_limit"):
            opt.spec["mana_limit"] = {k: v for k, v in opt.spec["mana_limit"].items() if k != game}
        opt._cache.clear()

    # a pure mana talent's removal run is the same build with less mana: its deficit is 1 - DPS without / the build's DPS with every
    # mana buff on, a point of the mana curve below the build's own (Moonglow's removal costs a Balance druid 27% on the dummy: the
    # builds' deficits alone, 4-20%, would never show how steep the curve gets)
    pure_mana = {name for name, p in plan.items()
                 if any(e.get("channel") in MANA_CHANNELS for e in p["fit"]) and all(e.get("channel") in PURE_MANA_OK for e in p["fit"])
                 and not any(e.get("channel") in ("enable", "disable") for e in p["entry"]["effects"])}

    def mana_points(variants=True):
        pts = {}
        for bid, d in deficits.items():
            if bid in allocs:
                det = opt.score(allocs[bid], 60, detail=True)
                pts[bid] = (d["deficit"], det["sustain"], det["bound_frac"])
        if variants:
            for bid, rws in sim.items():
                if bid not in deficits or bid not in allocs:
                    continue
                for r in rws:
                    if r["talent"] in pure_mana and r.get("dps_without"):
                        det = opt.score({k: v for k, v in allocs[bid].items() if k != r["talent"]}, 60, detail=True)
                        pts[f"{bid} -{r['talent']}"] = (max(0.0, 1.0 - r["dps_without"] / deficits[bid]["surplus"]), det["sustain"], det["bound_frac"])
        return pts

    def refit_mana():
        """The loss and cap that reproduce the builds' measured deficits under the current talent values."""
        ml["loss"], ml["cap"], rms = fit_mana_limit(mana_points())
        ml["rms"] = round(rms, 4)
        opt._cache.clear()

    def fit_talents(passes):
        for _pass in range(passes):
            for name, p in sorted(plan.items(), key=lambda kv: -kv[1]["target"]):
                if p["how"] in ("noise", "apl", "unmeasured"):   # apl: the rotation conditions on this talent, the removal run is not its value;
                    # unmeasured: the standard target cannot show it (specs.json not_measured: Murder's Humanoid and Giant bonus)
                    continue
                target = max(0.0, p["target"])   # the simulator sees every damage / healing channel: no floor
                cur = ev_mean(name)
                tol = TOLERANCE if target >= NOISE else 0.002
                if abs(cur - target) <= tol or (target >= NOISE and MIN_RATIO <= cur / target <= 1 / MIN_RATIO):
                    continue
                mx = opt.tree.info[name][2]   # the talent's ranks: a per_rank expansion runs to 5
                caps = [CHANNEL_MAX.get(e.get("channel"), MAX_VALUE) / abs(v) for e in expand(p["fit"]) for v in e.get("values", [0])[:mx] if v]
                absolute = any(e.get("channel") in ("resource_cost",) for e in expand(p["fit"]))   # energy / rage / mana units, not a multiplier: no cap
                kmax = 64.0 if absolute or not caps else min([64.0] + caps)   # all-zero effects: nothing to scale (64 as before)
                lo, hi = 0.0, min(kmax, max(1.0, p["k"]))
                k_prev = p["k"]
                apply(name, hi)
                while ev_mean(name) < target and hi < kmax:
                    hi = min(kmax, hi * 2)
                    apply(name, hi)
                if ml and ev_mean(name) < target and any(e.get("channel") in MANA_CHANNELS for e in p["fit"]) and not p.get("mixed"):
                    # its builds sit where the mana limit is flat (capped or never short): the removal runs cannot move it; the
                    # next limit fit may put them back on the slope
                    apply(name, k_prev)
                    p["k"], p["how"] = k_prev, "held"
                    continue
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

    if ml:
        refit_mana()
    fit_talents(3)
    if ml:   # the talent values move the builds' sustain and the limit follows: alternate, the talent fit last
        for _ in range(4):
            refit_mana()
            fit_talents(2)
        pts = mana_points()
        ml["rms"] = round((sum((d - f * min(ml["cap"], max(0.0, ml["loss"] - (su - 1.0)))) ** 2 for d, su, f in pts.values()) / max(1, len(pts))) ** 0.5, 4)
        ml["points"] = len(pts)
        print(f"  mana limit: loss {ml['loss']:.3f}, cap {ml['cap']:.2f} (RMS {ml['rms'] * 100:.2f} points of deficit over {len(pts)} points: "
              f"{len(deficits)} builds and the removal runs of the pure mana talents {sorted(pure_mana)})")
        variant_rows = {}
        for key, (d, su, f) in pts.items():
            pred = f * min(ml["cap"], max(0.0, ml["loss"] - (su - 1.0)))
            if key in deficits:
                deficits[key].update({"sustain": round(su, 4), "bound_share": round(f, 4), "model_deficit": round(pred, 4)})
            else:
                variant_rows[key] = {"deficit": round(d, 4), "sustain": round(su, 4), "bound_share": round(f, 4), "model_deficit": round(pred, 4)}
            print(f"    {key[:60]:<60} measured {d * 100:5.1f}%  model {pred * 100:5.1f}%  (sustain {su:.3f}, mana-bound share {f:.2f})")
    # ---- 3. report + write
    print(f"\n{'talent':<28} {'sim':>7} {'EV before':>9} {'EV after':>8} {'scale':>6} {'how':>7}")
    rows = []
    for name, p in sorted(plan.items(), key=lambda kv: -kv[1]["target"]):
        after = ev_mean(name)
        rows.append({"talent": name, "sim": p["target"], "ev_before": p["before"], "ev_after": after, "scale": p["k"], "how": p["how"], "builds": [b for b, _ in per_talent[name]]})
        print(f"{name:<28} {p['target'] * 100:6.1f}% {p['before'] * 100:8.1f}% {after * 100:7.1f}% {p['k']:6.2f} {p['how']:>7}")
    if a.write:
        n = 0
        for name, p in plan.items():
            if p["how"] in ("noise", "apl", "dead", "unmeasured") and not p.get("converted"):
                continue
            e = collections.OrderedDict()
            old_note = p["entry"].get("note", "").split(" Raid sim calibration")[0]
            what = {"fitted": f"raid values scaled x{p['k']:.2f} to match", "kept": "already within tolerance, raid effects split off unchanged",
                    "capped": f"raid values scaled x{p['k']:.2f}, the cap on effect size stops short of the target",
                    "held": f"raid values kept at x{p['k']:.2f}: its builds sit where the mana limit is flat, so the removal runs cannot move it"}.get(
                        p["how"], "raid values otherwise unchanged (" + p["how"] + ")")
            if p.get("reseeded"):
                what = "re-seeded from its tooltip (an earlier fit had left its raid values at zero), " + what
            if p.get("converted"):
                what = f"mana values moved to the mana limit's unit (x{p['converted']:.2f}), " + what
            e["note"] = old_note + (f" Raid sim calibration ({datetime.date.today().isoformat()}, {'ElliotWood/Forever' if game == 'forever' else 'wowsims/classic'} {out['sim']['commit']}, {a.spec}{', training dummy' if out['sim'].get('setting') == 'dummy' else ''}): removing it costs "
                                    f"{p['target'] * 100:.1f}% DPS in the simulator (scorer said {p['before'] * 100:.1f}% on the same scale); {what} ({ev_mean(name) * 100:.1f}%). Other modes unchanged.")
            e["effects"] = expand(p["other"]) + expand(fitted(p, p["k"]))
            manual[name] = e
            n += 1
        man_path.write_text(dumps(manual), encoding="utf-8")
        if deficits:   # the spec model's mana limit (or none when mana never binds)
            specs = json.load(open(spec_path, encoding="utf-8"), object_pairs_hook=collections.OrderedDict)
            model = specs["models"][a.spec]
            lim = collections.OrderedDict((k, v) for k, v in (model.get("mana_limit") or {}).items() if k != game)
            if ml:
                lo_d, hi_d = min(v["deficit"] for v in deficits.values()), max(v["deficit"] for v in deficits.values())
                lim[game] = collections.OrderedDict([("profiles", ml["profiles"]), ("loss", ml["loss"]), ("cap", ml["cap"]), ("rms", ml["rms"]), ("points", ml.get("points")), (
                    "note", f"Raid sim calibration ({datetime.date.today().isoformat()}, ElliotWood/Forever {out['sim']['commit']}, training dummy): the builds "
                            f"lose {lo_d * 100:.0f}-{hi_d * 100:.0f}% of their damage to mana (the same builds gain that much with every mana-only buff on); "
                            "the mana-bound damage (every source but white attacks and pets) shrinks by min(cap, max(0, loss - (sustain - 1))), loss "
                            "and cap fitted to those deficits and to the removal runs of the pure mana talents (the same build with less mana), the mana "
                            "talents' sustain to their removal runs. Re-run the calibration instead of editing.")])
            if lim:
                model["mana_limit"] = lim
            else:
                model.pop("mana_limit", None)
            spec_path.write_text(dumps(specs), encoding="utf-8")
        cal = paths.raidsim_dir(a.cls, game) / f"{a.spec}-calibration.json"
        cal.parent.mkdir(exist_ok=True)
        cal.write_text(json.dumps({"class": a.cls, "spec": a.spec, "profile": profile, "iterations": a.iterations, "builds": ids, "sim": out["sim"], "talents": rows,
                                   "mana": {"limit": dict(ml) if ml else None, "builds": deficits, "removals": variant_rows if ml else {}} if deficits else None}, indent=1), encoding="utf-8")
        print(f"wrote {man_path.relative_to(ROOT)} ({n} entries, {sum(1 for p in plan.values() if p['how'] == 'fitted')} fitted) and {cal.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
