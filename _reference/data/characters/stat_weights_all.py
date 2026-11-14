"""Every stat of every leveling page pick (2026-11-13, the gear add-on; user: "this is being made for all classes right? And before it's
built I think we should make sure all the stats are scored").

    python _reference/data/characters/stat_weights_all.py [classes...] [--fights 3000] [--jobs 10] [--fresh]

Runs stat_weights.py --full for each class's leveling page picks (fightlab/signature_audit.page_slots: one build per spec page) into
weights/leveling/<class>-<build id>.json; a pick whose file is there with the current steps is skipped unless --fresh, so the same
command resumes (a file made with other steps is redone).
"""
import argparse
import json
import pathlib
import subprocess
import sys
import time

HERE = pathlib.Path(__file__).resolve().parent
DATA = HERE.parent
sys.path[:0] = [str(HERE), str(DATA / "fightlab"), str(DATA / "scorer"), str(DATA)]
import level_guides as LG  # noqa: E402
import stat_weights as SW  # noqa: E402

CLASSES = "druid hunter mage paladin priest rogue shaman warlock warrior".split()


def picks(classes):
    SA = LG.fightlab_signature_audit()
    out = []
    for cls in classes:
        for s in SA.page_slots(cls):
            if s[1]:
                out.append((cls, s[0], s[1][0]["id"]))
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("classes", nargs="*", default=CLASSES)
    ap.add_argument("--fights", type=int, default=3000)
    ap.add_argument("--jobs", type=int, default=10)
    ap.add_argument("--fresh", action="store_true")
    ap.add_argument("--base", choices=("standard", "best"), default="standard")
    a = ap.parse_args()
    todo = picks(a.classes)
    print(f"{len(todo)} leveling picks", flush=True)
    for i, (cls, spec, bid) in enumerate(todo, 1):
        f = HERE / "weights" / ("leveling" if a.base == "standard" else "leveling-best") / f"{cls}-{bid}.json"
        want = {k: SW.FULL_STEPS[k] for k in SW.CLASS_STATS[cls]}
        extra = []
        if f.exists() and not a.fresh:
            have = json.loads(f.read_text(encoding="utf-8")).get("steps") or {}
            if have == want:
                print(f"[{i}/{len(todo)}] {cls} {spec}: done ({f.name})", flush=True)
                continue
            missing = [k for k in want if k not in have]
            if missing and all(have[k] == want[k] for k in have if k in want):   # a stat added since (spell_penetration, 2026-11-13)
                extra = ["--only"] + missing
        t = time.time()
        r = subprocess.run([sys.executable, "-u", str(HERE / "stat_weights.py"), cls, "--spec", spec, "--full", "--base", a.base, "--fights", str(a.fights),
                            "--jobs", str(a.jobs)] + extra)
        print(f"[{i}/{len(todo)}] {cls} {spec} ({bid}): rc={r.returncode}, {(time.time() - t) / 60:.1f} min", flush=True)


if __name__ == "__main__":
    main()
