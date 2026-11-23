"""The item-set parser's guard (2026-11-23, the audit session's read of race_set_pieces): gear_tiers.sim_set_steps reads the simulator's
Go source by regex (core.NewItemSet and the helpers that call it), and a re-pin changes that source. A parser that silently finds no
sets turns the set steps off for every spec, so this prints how many sets and steps it reads on the checkout and compares them with
the baseline recorded on the last good pin.

    python _reference/data/raidsim/set_steps_check.py            # exit 1 when sets or steps dropped by more than the tolerance
    python _reference/data/raidsim/set_steps_check.py --write    # record the baseline (raidsim/set-steps-baseline.json)

The re-pin's checks run it after the new pin is built and stop the chain on a failure; the per-set check on every made set is
gear_tiers.set_check (the simulator's own sheet against the parser).
"""
import argparse
import datetime
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path[:0] = [str(HERE), str(HERE.parent)]
import gear_tiers as GT  # noqa: E402

BASELINE = HERE / "set-steps-baseline.json"
TOL_SETS, TOL_STEPS = 3, 6   # "a drop of more than a few" (the audit session)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--write", action="store_true")
    a = ap.parse_args()
    R = GT.R
    R.set_game("forever")
    repo = R.repo_path(argparse.Namespace(repo=None))
    steps = GT.sim_set_steps(repo)
    names = {str(k): {"name": v["name"], "steps": v["steps"], "path": "generated" if v.get("generated") else "hand"} for k, v in sorted(steps.items())}
    n_sets, n_steps = len(names), sum(len(v["steps"]) for v in names.values())
    by_path = {p: {"sets": sum(1 for v in names.values() if v["path"] == p), "steps": sum(len(v["steps"]) for v in names.values() if v["path"] == p)}
               for p in ("hand", "generated")}
    commit = R.git_commit(repo)
    print(f"set steps on {repo} ({commit}): {n_sets} sets, {n_steps} steps; hand-written {by_path['hand']['sets']} / {by_path['hand']['steps']}, "
          f"generated {by_path['generated']['sets']} / {by_path['generated']['steps']}")
    if a.write:
        BASELINE.write_text(json.dumps({"commit": commit, "date": datetime.date.today().isoformat(), "sets": n_sets, "steps": n_steps,
                                        "by_path": by_path, "by_id": names}, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
        print(f"wrote {BASELINE.name}")
        return 0
    if not BASELINE.exists():
        print("no baseline: run with --write on a good pin")
        return 1
    b = json.load(open(BASELINE, encoding="utf-8"))
    gone = [f"{v['name']} ({k})" for k, v in b["by_id"].items() if k not in names]
    new = [f"{v['name']} ({k})" for k, v in names.items() if k not in b["by_id"]]
    moved = [f"{v['name']} ({k}): {b['by_id'][k]['steps']} -> {v['steps']}" for k, v in names.items() if k in b["by_id"] and b["by_id"][k]["steps"] != v["steps"]]
    print(f"baseline {b['commit']} ({b['date']}): {b['sets']} sets, {b['steps']} steps")
    for label, xs in (("gone", gone), ("new", new), ("steps changed", moved)):
        if xs:
            print(f"  {label}: " + "; ".join(xs))
    bad = n_sets < b["sets"] - TOL_SETS or n_steps < b["steps"] - TOL_STEPS
    for p, v in (b.get("by_path") or {}).items():   # (2026-11-23, the audit session) each parser path apart: a drop in either fails
        now = by_path.get(p) or {"sets": 0, "steps": 0}
        if now["sets"] < v["sets"] - TOL_SETS or now["steps"] < v["steps"] - TOL_STEPS:
            print(f"FAIL: the {p} path reads {now['sets']} sets / {now['steps']} steps against the baseline's {v['sets']} / {v['steps']}")
            bad = True
    print("FAIL: the parser reads fewer sets or steps than the baseline allows" if bad else "ok")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
