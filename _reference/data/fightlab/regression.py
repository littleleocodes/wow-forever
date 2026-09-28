"""Engine regression check: the mage Frost run must reproduce `regression/mage-frost.txt` bit for bit.

    python _reference/data/fightlab/regression.py            # compare (exit 1 on any difference)
    python _reference/data/fightlab/regression.py --update   # rewrite the baseline after an intended change of tables or mechanics

The run: 500 fights, seed 1, levels 30 and 60, two frozen builds (`regression/leveling-frost.json`, a copy of the hand draft, vs
`regression/cand-frost-23-0-28.json`), so a re-exported optimizer build never moves the check. Engine refactors,
new hooks and new class modules must leave it unchanged; a changed mob table, gear tier or mechanic changes it on purpose
(say so in the commit / notes and update the baseline).
"""
import pathlib
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[2]
BASE = HERE / "regression" / "mage-frost.txt"
CMD = [sys.executable, str(HERE / "run.py"), "mage", "--spec", "frost-leveling", "--build", str(HERE / "regression/leveling-frost.json"),
       "--compare", str(HERE / "regression/cand-frost-23-0-28.json"), "--levels", "30,60", "--fights", "500", "--seed", "1"]


def current():
    import os
    env = dict(os.environ, WOW_FL_ROTATION="default")   # the hand-written rotation: tuned rotation files are intended changes elsewhere
    r = subprocess.run(CMD, capture_output=True, text=True, encoding="utf-8", errors="replace", cwd=str(ROOT), env=env)
    if r.returncode:
        raise SystemExit(r.stderr[-2000:])
    return "\n".join(l for l in r.stdout.splitlines() if not l.startswith("done in") and not l.startswith("==")) + "\n"


def main():
    out = current()
    if "--update" in sys.argv:
        BASE.parent.mkdir(exist_ok=True)
        BASE.write_text(out, encoding="utf-8")
        print(f"baseline written: {BASE.relative_to(ROOT)}")
        return 0
    if not BASE.exists():
        raise SystemExit(f"no baseline at {BASE}: run with --update")
    base = BASE.read_text(encoding="utf-8")
    if out == base:
        print("mage regression IDENTICAL")
        return 0
    print("mage regression DIFFERS from the baseline:")
    for a, b in zip(base.splitlines(), out.splitlines()):
        if a != b:
            print("  baseline:", a[:150])
            print("  now:     ", b[:150])
    return 1


if __name__ == "__main__":
    sys.exit(main())
