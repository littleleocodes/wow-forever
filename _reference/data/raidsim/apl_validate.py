"""The official simulator's own rotation checks for every rotation of ours (2026-10-18, the port to wowsims/forever).

    python _reference/data/raidsim/apl_validate.py [classes] [--write]

For every entry of specs.json and each rotation it runs (base, dummy, raid), the bench's `validate` mode (ComputeStats: the rotation is
parsed against the character the entry's first build makes) lists the simulator's validation messages per priority-list and prepull
line: an unknown spell or aura, a condition it cannot resolve and drops or treats as always true. The fork resolved conditions the
official simulator does not (a totem as a dot: the Elemental rotation's Searing Totem line lost its guard and recast 58 times a fight).
Record `raidsim/apl-validate.json`; the lines it lists need a rewrite before their numbers mean anything.
"""
import argparse
import json
import os
import pathlib
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import run as R  # noqa: E402

ROOT = HERE.parents[2]


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("classes", nargs="*")
    ap.add_argument("--repo", default=os.environ.get("WOW_FOREVER_SIM", str(pathlib.Path.home() / ".wow-forever-tools/wowsims-forever")))
    ap.add_argument("--write", action="store_true")
    ap.add_argument("--all-talents", action="store_true", help="validate with every talent at full rank (not a legal build): what is left "
                    "is not a talent the build lacks but a spell or aura the simulator does not have")
    a = ap.parse_args()
    repo = pathlib.Path(a.repo)
    exe = repo / ("foreverbench.exe" if (repo / "foreverbench.exe").exists() else "foreverbench")
    record = {}
    for cls in a.classes or [c for c in R.SPECS if isinstance(R.SPECS[c], dict)]:
        trees = R.load_trees(repo, cls)
        data = json.load(open(ROOT / cls / R.GAMES["forever"]["builds"], encoding="utf-8"))
        by_id = {b["id"]: b for b in data["builds"]}
        for spec, entry in R.SPECS[cls].items():
            bid = next((b for b in entry.get("builds", []) if b in by_id), None)
            if not bid:
                continue
            talents = R.talents_string(trees, R.alloc_of(by_id[bid]))
            if a.all_talents:
                talents = "-".join("".join(str(t["maxPoints"]) for t in tr["talents"]) for tr in trees)
            files = {}
            for where in ("dummy", "raid"):
                files.setdefault(str(R.apl_path(entry, repo, where)), where)
            base = R.sim_path(entry["apl"])
            files.setdefault(base if pathlib.Path(base).is_absolute() else str(repo / entry["apl"]), "dummy")
            for apl, where in files.items():
                cfg = {"class": entry["sim_class"], "race": entry.get("race", "RaceHuman"), "gear": R.sim_path(entry["gear"]), "apl": apl,
                       "spec": entry.get("spec", {}), **R.setting_cfg(entry, where), "iterations": 1, "duration": R.FIGHT, "seed": 1,
                       "isTank": entry.get("tank", False), "validate": True, "builds": [{"label": bid, "talents": talents}]}
                path = repo / "bench" / f"validate-{cls}-{spec}.json"
                path.parent.mkdir(exist_ok=True)
                path.write_text(json.dumps(cfg), encoding="utf-8")
                r = subprocess.run([str(exe), "--config", str(path), "--root", str(repo)], capture_output=True, text=True,
                                   encoding="utf-8", errors="replace", cwd=str(repo))
                rows = [json.loads(x) for x in r.stdout.splitlines() if x.startswith("{")]
                name = pathlib.Path(apl).name
                if r.returncode or not rows:
                    print(f"  {cls} {spec} {name}: bench failed {r.stderr[-300:]}")
                    continue
                d = rows[0]
                prio = json.load(open(apl, encoding="utf-8")).get("priorityList", [])
                bad = {}
                for kind in ("priority", "prepull"):
                    for i, msgs in (d.get(kind) or {}).items():
                        msgs = [m for m in msgs if not m.startswith("Information")]
                        if msgs:
                            line = json.dumps(prio[int(i)].get("action", {}))[:220] if kind == "priority" and int(i) < len(prio) else ""
                            bad[f"{kind}[{i}]"] = {"messages": sorted(set(msgs)), "line": line}
                record.setdefault(cls, {})[f"{spec}:{name}"] = bad
                print(f"== {cls} {spec} {name}: {len(bad)} lines with warnings")
                for k, v in bad.items():
                    print(f"    {k}: {'; '.join(v['messages'])[:160]} | {v['line'][:150]}")
    if a.write:
        out = HERE / ("apl-validate-all-talents.json" if a.all_talents else "apl-validate.json")
        out.write_text(json.dumps(record, indent=1) + "\n", encoding="utf-8")
        print(f"wrote {out}")


if __name__ == "__main__":
    main()
