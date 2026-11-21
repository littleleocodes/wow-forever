"""Fire's pick holds three Improved Channeling points (no channel in the Fire rotation) that the 2026-11-11 filler audit moved to Arcane
Resilience (survival) at exactly no loss; the page lint's free check listed them at the raid regen of 2026-11-20 night. The audited exact
filler pass on the current build (credited_fillers_1120.py --extra), its two-seed verification and the apply, then fire-raid raced again
(dummy and environments) and play-checked. Log deep-runs/fire-fillers-1120.log."""
import os
import pathlib
import subprocess
import sys
import time

ROOT = pathlib.Path(__file__).resolve().parents[3]
LOG = ROOT / "_reference/data/deep-runs/fire-fillers-1120.log"
D, R = "_reference/data/deep-runs", "_reference/data/raidsim"
OUT = "_reference/data/raidsim/credited-fillers-fire.json"
STEPS = [[f"{D}/credited_fillers_1120.py", "--extra", "mage:fire-raid:fire-open-raid", "--only", "fire-open-raid", "--out", OUT],
         [f"{D}/credited_fillers_1120.py", "--verify", "--out", OUT], [f"{D}/credited_fillers_1120.py", "--apply", "--out", OUT],
         [f"{R}/run.py", "mage", "--spec", "fire-raid", "--write"], [f"{R}/run.py", "mage", "--spec", "fire-raid", "--env", "environments", "--write"],
         [f"{R}/play_check.py", "mage", "--entry", "fire-raid", "--write"]]
env = dict(os.environ, PYTHONIOENCODING="utf-8", WOW_FOREVER_NO_RACIALS="1",
           WOW_FOREVER_SIM=str(pathlib.Path.home() / ".wow-forever-tools/wowsims-forever-y"))
with open(LOG, "a", encoding="utf-8") as log:
    for s in STEPS:
        log.write(f"##### {time.strftime('%Y-%m-%d_%H:%M')} {' '.join(s)}\n")
        log.flush()
        rc = subprocess.run([sys.executable, "-u", *s], cwd=ROOT, env=env, stdout=log, stderr=subprocess.STDOUT).returncode
        log.write(f"=== {time.strftime('%Y-%m-%d_%H:%M')} rc={rc}\n")
        log.flush()
        if rc:
            break
    log.write(f"=== {time.strftime('%Y-%m-%d_%H:%M')} all done\n")
