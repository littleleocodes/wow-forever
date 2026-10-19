"""Make a fresh machine or a Claude Code cloud session ready for this project (2026-09-28).

    python _reference/data/cloud_setup.py              # Python packages + the Forever simulator + checks
    python _reference/data/cloud_setup.py --classic    # also the upstream wowsims/classic simulator (Classic-era checks)
    python _reference/data/cloud_setup.py --skip-sim   # Python packages and the quick checks only

1. `pip install -r requirements.txt` (numpy: the raid calibration's mana-limit fit).
2. `raidsim/setup.py`: Go, protoc, a sparse clone of the official simulator (github.com/wowsims/forever since 2026-10-18: the
   ElliotWood/Forever fork it replaced was deleted) at the pinned commit (`GAMES["forever"]["commit"]` in setup.py: 09e7398, client
   70450), our patches (raidsim/patches/README.md) and the `foreverbench` tool, under ~/.wow-forever-tools/wowsims-forever.
   Several minutes the first time. In a cloud session the container (and the tools with it) goes away when the session ends,
   so run this at the start of every session that needs the raid simulator; the fight lab, the scorer, the healer lab and
   the page renderers need only step 1.
3. Checks: `validate_builds.py`, the fight-lab mage regression (must print IDENTICAL) and, with the simulator, a short raid run.

Nothing in the project changes. Commit and push before a cloud session ends: files left in the container are lost.
"""
import argparse
import pathlib
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[1]


def run(args, timeout=None):
    print("$", " ".join(str(a) for a in args), flush=True)
    r = subprocess.run([str(a) for a in args], cwd=str(ROOT), text=True, capture_output=True, encoding="utf-8", errors="replace", timeout=timeout)
    tail = (r.stdout.strip().splitlines() or [""])[-3:]
    for line in tail:
        print("   ", line[:200])
    if r.returncode:
        print(r.stderr[-3000:])
    return r.returncode


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--classic", action="store_true", help="also build the upstream wowsims/classic simulator")
    ap.add_argument("--skip-sim", action="store_true", help="Python packages and the quick checks only")
    a = ap.parse_args()
    py = sys.executable
    failed = []
    if run([py, "-m", "pip", "install", "--quiet", "-r", ROOT / "requirements.txt"]):
        failed.append("pip install")
    if not a.skip_sim:
        if run([py, HERE / "raidsim/setup.py"]):
            failed.append("raidsim/setup.py")
        if a.classic and run([py, HERE / "raidsim/setup.py", "--game", "classic"]):
            failed.append("raidsim/setup.py --game classic")
    if run([py, HERE / "validate_builds.py"]):
        failed.append("validate_builds.py")
    if run([py, HERE / "fightlab/regression.py"]):
        failed.append("fightlab/regression.py (not IDENTICAL)")
    if not a.skip_sim and "raidsim/setup.py" not in failed:
        if run([py, HERE / "raidsim/run.py", "mage", "--spec", "frost-raid", "--iterations", "300"]):
            failed.append("raidsim/run.py (short raid run)")
    print("\nready" if not failed else "\nFAILED: " + "; ".join(failed))
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
