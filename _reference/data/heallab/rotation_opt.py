"""Tune the healers' heal choice in the healer lab: the policy settings of heallab/tables.py, per healer spec.

    python _reference/data/heallab/rotation_opt.py priest [--write]
    python _reference/data/heallab/rotation_opt.py --all [--write] [--jobs 6]

The healer lab's heal choice (engine.BaseHealer.decide and the class modules) reads a few policy settings: cast the lowest rank
that covers the deficit or always the highest (DOWNRANK), when to keep a HoT on the tank (HOT_REFRESH_DEFICIT), when a target gets
the fastest big heal (EMERGENCY), when a raid member gets healed (RAID_HEAL_AT), how many hurt raid members justify a group heal
(GROUP_HEAL_MIN) and when to drink a mana potion (POTION_BELOW, POTION_FIRST). Local search like the raid and fight-lab rotation
searches: every candidate measures the class pipeline's hand-draft healer's capacity (the damage multiplier it survives in 90% of
the runs) with common random numbers (seeds 0..runs-1); the best candidates run again on other seeds with more runs, and a
setting is kept only when it raises capacity there by more than --min-gain. With --write the settings go to
`heallab/rotations/<class>-<spec>.json`, which tables.apply_rotation applies to every healer-lab run of the class
(WOW_HL_ROTATION=default switches them off; --set still overrides).
"""
import argparse
import copy
import datetime
import importlib
import json
import multiprocessing
import os
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[2]
sys.path.insert(0, str(ROOT / "_reference/data"))
sys.path.insert(0, str(HERE))
import engine as E  # noqa: E402
import tables as T  # noqa: E402

CLASSES = {"priest": "priest", "paladin": "paladin", "shaman": "shaman", "druid": "druid"}
KNOBS = {
    "DOWNRANK": [True, False],
    "HOT_REFRESH_DEFICIT": [0.0, 0.05, 0.1, 0.2, 0.3],
    "EMERGENCY": [0.2, 0.25, 0.35, 0.45, 0.55],
    "RAID_HEAL_AT": [0.5, 0.6, 0.7, 0.8, 0.9],
    "GROUP_HEAL_MIN": [2, 3, 4, 5],
    "POTION_BELOW": [0.4, 0.5, 0.65, 0.8],
    "POTION_FIRST": [0.0, 20.0, 45.0, 90.0],
}


def _init():
    os.environ["WOW_HL_ROTATION"] = "default"   # every candidate sets its settings explicitly


def _cap(job):
    cls, alloc, settings, seeds, steps = job
    for k, v in settings.items():
        setattr(T, k, v)
    mod = importlib.import_module(CLASSES[cls])
    return E.capacity(mod.Healer(alloc), seeds, steps=steps)


def alloc_of(build):
    return {n: r for lst in build["allocation"].values() for n, r in lst if r > 0}


def tuning_builds(cls, P, extra):
    """[(label, alloc)]: the class pipeline's hand draft, plus --build ids or allocation .json files ({talent: rank} or by tree, or a
    build with `allocation`): the policy is shared by every healer build of the spec, so it is tuned on several and may cost none of
    them more than --max-loss (2026-10-02: deep_heal.py tunes it on the talent search's winner and the hand draft)."""
    data = {b["id"]: b for b in json.load(open(ROOT / cls / "research/talents/forever/proposed-builds.json", encoding="utf-8"))["builds"]}
    out = [(P["hand"], alloc_of(data[P["hand"]]))]
    for ref in extra or []:
        if ref in data:
            al = alloc_of(data[ref])
        else:
            x = json.load(open(ref, encoding="utf-8"))
            al = x.get("allocation", x)
            if al and all(isinstance(v, list) for v in al.values()):
                al = {n: r for lst in al.values() for n, r in lst if r > 0}
        if al not in [a2 for _, a2 in out]:
            out.append((pathlib.Path(ref).stem, al))
    return out


def search(pool, cls, a):
    mod = importlib.import_module(CLASSES[cls])
    P = mod.PIPELINE
    builds = tuning_builds(cls, P, getattr(a, "build", None))
    rot_path = HERE / "rotations" / f"{cls}-{P['spec']}.json"
    defaults = {k: getattr(T, k) for k in KNOBS}
    start = dict(defaults, **((json.load(open(rot_path, encoding="utf-8")).get("tables") or {}) if rot_path.exists() and not a.fresh else {}))
    cur = dict(start)
    seeds1 = list(range(a.runs))
    seeds2 = list(range(1000, 1000 + a.confirm))

    def caps(settings_list, seeds):
        """[[capacity per tuning build] per settings]."""
        flat = pool.map(_cap, [(cls, al, s, seeds, a.steps) for s in settings_list for _, al in builds], chunksize=1)
        n = len(builds)
        return [flat[i * n:(i + 1) * n] for i in range(len(settings_list))]

    def ratio(row, ref):
        rs = [c / r for c, r in zip(row, ref)]
        return sum(rs) / len(rs), min(rs)

    base1 = caps([cur], seeds1)[0]
    print(f"== {cls} {P['spec']} ({', '.join(lb for lb, _ in builds)}): capacity {', '.join(f'{c:.3f}' for c in base1)} with "
          + ", ".join(f"{k} {v}" for k, v in cur.items()), flush=True)
    log = []
    for rnd in range(1, a.rounds + 1):
        cands = [(k, v) for k, vals in KNOBS.items() for v in vals if v != cur[k]]
        res = caps([dict(cur, **{k: v}) for k, v in cands], seeds1)
        scored = sorted(((ratio(c, base1), i) for i, c in enumerate(res)), key=lambda x: -x[0][0])
        top = [(sc, i) for sc, i in scored if sc[0] > 1 + a.screen_gain and sc[1] >= 1 - a.max_loss][: a.top]
        if not top:
            print(f"  round {rnd}: {len(cands)} candidates, none ahead (best {scored[0][0][0] - 1:+.2%}: {cands[scored[0][1]][0]} = {cands[scored[0][1]][1]})", flush=True)
            break
        conf = caps([cur] + [dict(cur, **{cands[i][0]: cands[i][1]}) for _, i in top], seeds2)
        rated = [(ratio(conf[k], conf[0]), sc1, i) for k, (sc1, i) in enumerate(top, start=1)]
        ok = [x for x in rated if x[0][1] >= 1 - a.max_loss]
        best = max(ok, key=lambda x: x[0][0]) if ok else None
        if not best or best[0][0] <= 1 + a.min_gain:
            print(f"  round {rnd}: {len(top)} ahead on the first seeds, none confirmed" + (f" (best {best[0][0] - 1:+.2%})" if best else ""), flush=True)
            break
        sc2, sc1, i = best
        k, v = cands[i]
        log.append({"round": rnd, "change": f"{k} {cur[k]} -> {v}", "gain_seeds1": sc1[0] - 1, "gain_seeds2": sc2[0] - 1, "worst_build_seeds2": sc2[1] - 1})
        print(f"  round {rnd}: {k} {cur[k]} -> {v}  ({sc1[0] - 1:+.2%} first seeds, {sc2[0] - 1:+.2%} confirmation seeds, worst build {sc2[1] - 1:+.2%})", flush=True)
        cur[k] = v
        base1 = res[i]
    fin = caps([start, cur], list(range(5000, 5000 + a.confirm)))
    print(f"  final (other seeds, {a.confirm} runs): capacity " + "; ".join(f"{lb} {b:.3f} -> {c:.3f} ({c / b - 1:+.2%})" for (lb, _), b, c in zip(builds, fin[0], fin[1])), flush=True)
    return {"class": cls, "spec": P["spec"], "build": P["hand"], "builds": [lb for lb, _ in builds], "date": datetime.date.today().isoformat(),
            "runs": a.runs, "confirm": a.confirm, "tables": {k: v for k, v in cur.items() if v != defaults[k]}, "defaults": defaults, "changes": log,
            "capacity_before": fin[0][0], "capacity_after": fin[1][0], "capacity_by_build": {lb: [b, c] for (lb, _), b, c in zip(builds, fin[0], fin[1])}}


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("cls", nargs="?", choices=list(CLASSES))
    ap.add_argument("--all", action="store_true")
    ap.add_argument("--rounds", type=int, default=8)
    ap.add_argument("--runs", type=int, default=60)
    ap.add_argument("--confirm", type=int, default=200)
    ap.add_argument("--steps", type=int, default=10)
    ap.add_argument("--top", type=int, default=4)
    ap.add_argument("--screen-gain", type=float, default=0.005)
    ap.add_argument("--min-gain", type=float, default=0.005)
    ap.add_argument("--jobs", type=int, default=max(1, (os.cpu_count() or 4) - 2))
    ap.add_argument("--fresh", action="store_true")
    ap.add_argument("--build", action="append", help="also tune on this build (id or allocation .json); repeatable")
    ap.add_argument("--max-loss", type=float, default=0.003, help="a setting may cost no tuning build more than this")
    ap.add_argument("--write", action="store_true")
    a = ap.parse_args()
    with multiprocessing.Pool(a.jobs, initializer=_init) as pool:
        for cls in (list(CLASSES) if a.all else [a.cls]):
            rec = search(pool, cls, a)
            if a.write:
                p = HERE / "rotations" / f"{cls}-{rec['spec']}.json"
                if not rec["changes"] and not p.exists():
                    print("  no setting beat the defaults: nothing written", flush=True)
                    continue
                p.parent.mkdir(exist_ok=True)
                p.write_text(json.dumps(rec, indent=1), encoding="utf-8")
                print(f"  wrote {p.relative_to(ROOT)}", flush=True)


if __name__ == "__main__":
    main()
