"""Healer lab driver: capacity, healing split and talent values of a healer build.

    python _reference/data/heallab/run.py <class> --build <id> [--compare <ids or .json files>] [--deltas] [--runs 60] [--write]
                                          [--set KEY=VALUE ...]

Capacity = the multiplier on the encounter's damage at which the build keeps the group alive in 90% of runs (bisection with
common random numbers, `tables.DEATH_RUNS_OK`); the healing split, overheal and mana are reported at that multiplier.
`--deltas` removes every talent of the build in turn and re-measures the capacity (the value of the talent, on the scale
`scorer/run.py` uses for its raid-heal score); `--write` saves `<class>/research/raid/heallab/<spec>.md` and `.json`.
"""
import argparse
import datetime
import importlib
import json
import pathlib
import sys
import time

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[2]
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(ROOT / "_reference/data/scorer"))
sys.path.append(str(pathlib.Path(__file__).resolve().parents[1]))   # _reference/data: paths.py
import paths  # noqa: E402
import engine as E  # noqa: E402
import tables as T  # noqa: E402

CLASSES = {"priest": "priest", "paladin": "paladin", "shaman": "shaman", "druid": "druid"}


def alloc_of(build):
    out = {}
    for tree, lst in build["allocation"].items():
        for name, r in lst:
            if r > 0:
                out[name] = r
    return out


def load_build(cls, ref):
    if ref.endswith(".json"):
        b = json.load(open(ref, encoding="utf-8"))
        b.setdefault("id", pathlib.Path(ref).stem)
        return b
    data = json.load(open(ROOT / cls / "research/talents/forever/proposed-builds.json", encoding="utf-8"))
    return next(b for b in data["builds"] if b["id"] == ref)


def apply_overrides(sets):
    for kv in sets or []:
        k, v = kv.split("=", 1)
        cur = getattr(T, k)
        setattr(T, k, type(cur)(v) if not isinstance(cur, bool) else v.lower() in ("1", "true", "yes"))


def split_of(build):
    return "/".join(str(sum(r for _, r in lst)) for lst in build["allocation"].values())


def measure(mod, alloc, seeds, steps):
    h = mod.Healer(alloc)
    cap = E.capacity(h, seeds, steps=steps)
    summ = E.summarise(h, cap, seeds)
    return h, cap, summ


def scorer_values(cls, spec, allocs):
    """The scorer's removal value of every talent on the lab's scale: (score_with - score_without) / (1 + score_without)."""
    try:
        from optimize import Optimizer
        opt = Optimizer("forever", cls, spec, "raid-heal")
    except Exception as e:
        print(f"  (scorer unavailable: {e})")
        return {}
    out = {}
    for bid, al in allocs.items():
        with_s = opt.score(al, 60)
        out[bid] = {}
        for name in al:
            wo = opt.score({k: v for k, v in al.items() if k != name}, 60)
            out[bid][name] = (with_s - wo) / (1.0 + wo)
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("cls", choices=list(CLASSES))
    ap.add_argument("--build", required=True)
    ap.add_argument("--compare", nargs="*", default=[])
    ap.add_argument("--deltas", action="store_true")
    ap.add_argument("--runs", type=int, default=60)
    ap.add_argument("--steps", type=int, default=10)
    ap.add_argument("--set", nargs="*", default=[])
    ap.add_argument("--write", action="store_true")
    a = ap.parse_args()
    T.apply_rotation(a.cls)   # the class's tuned heal-choice settings (rotation_opt.py); --set still overrides
    apply_overrides(a.set)
    mod = importlib.import_module(CLASSES[a.cls])
    spec = mod.PIPELINE["spec"]
    seeds = list(range(a.runs))
    t0 = time.time()
    builds = [load_build(a.cls, a.build)] + [load_build(a.cls, c) for c in a.compare]
    results = {}
    allocs = {}
    for b in builds:
        al = alloc_of(b)
        allocs[b["id"]] = al
        h, cap, summ = measure(mod, al, seeds, a.steps)
        results[b["id"]] = {"split": split_of(b), "capacity": cap, "summary": summ, "stats": {"intellect": round(h.intellect), "spirit": round(h.spirit), "healing": round(h.healing), "mp5": round(h.mp5), "mana": round(h.mana_max), "crit": round(h.crit_base, 4)}}
        print(f"  {b['id']:<36} {split_of(b):>8}  capacity {cap:.3f}  HPS {summ['hps']:.0f}  overheal {summ['overheal_share'] * 100:.0f}%  oom {summ['oom_time']:.0f}s  survival {summ['survival']:.2f}")
        print("     split: " + ", ".join(f"{k} {v * 100:.0f}%" for k, v in list(summ["shares"].items())[:8]))
    deltas = {}
    if a.deltas:
        ev = scorer_values(a.cls, spec, {b["id"]: allocs[b["id"]] for b in builds[:1]})
        for b in builds[:1]:
            al = allocs[b["id"]]
            base = results[b["id"]]["capacity"]
            rows = []
            for name in sorted(al):
                trial = {k: v for k, v in al.items() if k != name}
                _, cap, _ = measure(mod, trial, seeds, a.steps)
                rows.append({"talent": name, "ranks": al[name], "sim_delta": (base - cap) / cap if cap else 0.0, "cap_with": base, "cap_without": cap,
                             "ev_delta": ev.get(b["id"], {}).get(name), "simulated": name in mod.Healer.SIMULATED})
            deltas[b["id"]] = rows
            print(f"  talent values for {b['id']} (capacity lost when removed; EV = scorer on the same scale; * = mechanics not simulated):")
            for r in sorted(rows, key=lambda r: -r["sim_delta"]):
                print(f"    {r['talent']:<30} {r['ranks']}  lab {r['sim_delta'] * 100:+6.1f}%   EV {(r['ev_delta'] * 100 if r['ev_delta'] is not None else float('nan')):+6.1f}%{'' if r['simulated'] else ' *'}")
    out = {"class": a.cls, "spec": spec, "date": datetime.date.today().isoformat(), "runs": a.runs, "steps": a.steps, "seconds": round(time.time() - t0),
           "assumptions": {k: getattr(T, k) for k in ("DURATION", "TANK_HP", "RAID_HP", "TANK_ARMOR_MIT", "TANK_AVOID", "BOSS_SWING", "BOSS_DMG", "CRUSH_CHANCE", "SPIKE_EVERY", "SPIKE_MULT", "RAID_PULSE_EVERY", "RAID_PULSE_DMG", "POTIONS", "DOWNRANK", "KINGS")},
           "gear": T.HEALER_GEAR[a.cls], "results": results, "deltas": deltas, "mechanics": mod.Healer.MECHANICS, "simulated": sorted(mod.Healer.SIMULATED)}
    if a.write:
        d = paths.heallab_dir(a.cls)
        d.mkdir(parents=True, exist_ok=True)
        (d / f"{spec}.json").write_text(json.dumps(out, indent=1), encoding="utf-8")
        (d / f"{spec}.md").write_text(render(out), encoding="utf-8")
        print(f"wrote {(d / f'{spec}.md').relative_to(ROOT)}")
    print(f"done in {time.time() - t0:.0f}s")


def render(out):
    cls, spec = out["class"], out["spec"]
    A = out["assumptions"]
    o = [f"# Healer lab — {cls} {spec}", "",
         f"> Generated by `_reference/data/heallab/run.py` on {out['date']}: a Monte Carlo model of one raid healer keeping a five-member group "
         f"(a {A['TANK_HP']:.0f}-health tank taking boss melee, four {A['RAID_HP']:.0f}-health raid members taking periodic raid damage) alive for {A['DURATION']:.0f} s, "
         f"{out['runs']} runs per point with common random numbers. Spell ranks, costs, cast times and coefficients from the beta spellbook; talent numbers from the beta tooltips "
         f"plus the mechanics listed below. **Capacity** = the multiplier on all incoming damage the build survives in 90% of runs: a model of stated assumptions "
         f"(`heallab/tables.py`), not a measurement. Do not hand-edit.", "",
         f"Healer stats assumed (phase-1 raid gear, raid buffed): " + ", ".join(f"{k} {v}" for k, v in next(iter(out["results"].values()))["stats"].items()) + ".", "",
         "| Build | Split | Capacity | Effective HPS at capacity | Overheal | Time out of mana | Healing split |", "|---|---|---|---|---|---|---|"]
    for bid, r in sorted(out["results"].items(), key=lambda kv: -kv[1]["capacity"]):
        s = r["summary"]
        o.append(f"| `{bid}` | {r['split']} | {r['capacity']:.3f} | {s['hps']:.0f} | {s['overheal_share'] * 100:.0f}% | {s['oom_time']:.0f} s | " + ", ".join(f"{k} {v * 100:.0f}%" for k, v in list(s["shares"].items())[:7]) + " |")
    o.append("")
    for bid, rows in out["deltas"].items():
        o += [f"## Talent values of `{bid}`", "", "Capacity lost when the talent is removed (relative to the build without it); EV = the scorer's raid-heal value on the same scale. "
              "Talents marked * have no mechanics in the lab (their manual value stands).", "",
              "| Talent | Ranks | Lab | Scorer |", "|---|---|---|---|"]
        for r in sorted(rows, key=lambda r: -r["sim_delta"]):
            o.append(f"| {r['talent']}{'' if r['simulated'] else ' *'} | {r['ranks']} | {r['sim_delta'] * 100:+.1f}% | {(r['ev_delta'] * 100 if r['ev_delta'] is not None else float('nan')):+.1f}% |")
        o.append("")
    o += ["## Mechanics simulated", ""] + [f"- **{k}**: {v}" for k, v in out["mechanics"].items()] + ["",
          "Everything else the build takes is either a plain tooltip number the lab applies (healing, mana cost, crit, cast time, regen, stats) or not simulated.", "",
          "## Encounter assumptions", ""] + [f"- {k} = {v}" for k, v in A.items()] + [""]
    return "\n".join(o) + "\n"


if __name__ == "__main__":
    main()
