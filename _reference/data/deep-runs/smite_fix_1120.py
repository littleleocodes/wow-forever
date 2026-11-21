"""The three hunter entries whose page builds took their short check's confirmed moves (apply_checks_1120.py) raced again, dummy and
environments, then the hunter play check (2026-11-20 evening). Log deep-runs/smite-fix-1120.log."""
import os
import pathlib
import subprocess
import sys
import time

ROOT = pathlib.Path(__file__).resolve().parents[3]
LOG = ROOT / "_reference/data/deep-runs/smite-fix-1120.log"
R = "_reference/data/raidsim"
STEPS = [["_reference/data/deep-runs/smite_downrank_1120.py", "--apply"],
         [f"{R}/run.py", "priest", "--spec", "smite-dps", "--write"], [f"{R}/run.py", "priest", "--spec", "smite-dps", "--env", "environments", "--write"],
         [f"{R}/play_check.py", "priest", "--write"]]
env = dict(os.environ, PYTHONIOENCODING="utf-8", WOW_FOREVER_NO_RACIALS="1",
           WOW_FOREVER_SIM=str(pathlib.Path.home() / ".wow-forever-tools/wowsims-forever-y"))
with open(LOG, "a", encoding="utf-8") as log:
    for s in STEPS:
        log.write(f"##### {time.strftime('%Y-%m-%d_%H:%M')} {' '.join(s)}\n")
        log.flush()
        rc = subprocess.run([sys.executable, "-u", *s], cwd=ROOT, env=env, stdout=log, stderr=subprocess.STDOUT).returncode
        log.write(f"=== {time.strftime('%Y-%m-%d_%H:%M')} rc={rc}\n")
        log.flush()
    log.write(f"=== {time.strftime('%Y-%m-%d_%H:%M')} all done\n")
