"""The raid half of the regen step for the split raid push (2026-11-20 night, the audit session's GO): rebuild.py's regen without its
leveling parts (render_fightlab_sections, render_leveling_guides, the fight lab's signature audit, respec, the scorer reports and the
fight lab summary), which would read or write the running leveling lane's records. Only raid paths are pushed from it. Log
deep-runs/raid-regen-1120.log.

    python _reference/data/deep-runs/raid_regen_1120.py
"""
import os
import pathlib
import subprocess
import sys
import time

ROOT = pathlib.Path(__file__).resolve().parents[3]
D = "_reference/data"
LOG = ROOT / D / "deep-runs" / "raid-regen-1120.log"
CLASSES = ["mage", "priest", "warlock", "hunter", "warrior", "rogue", "paladin", "shaman", "druid"]
STEPS = [[f"{D}/validate_builds.py"], [f"{D}/render_builds.py"], [f"{D}/render_raidsim_sections.py", *CLASSES],
         [f"{D}/render_heallab_sections.py", *CLASSES], [f"{D}/render_sim_presets.py", *CLASSES], [f"{D}/render_rotations.py", *CLASSES],
         [f"{D}/render_new_builds.py", *CLASSES], [f"{D}/render_modes.py"], [f"{D}/render_tier_list.py"], [f"{D}/render_report_index.py"],
         [f"{D}/page_lint.py", "--write"]]
env = dict(os.environ, PYTHONIOENCODING="utf-8", WOW_FOREVER_SIM=str(pathlib.Path.home() / ".wow-forever-tools/wowsims-forever-y"))
with open(LOG, "a", encoding="utf-8") as log:
    for s in STEPS:
        log.write(f"##### {time.strftime('%Y-%m-%d_%H:%M')} {' '.join(s)}\n")
        log.flush()
        rc = subprocess.run([sys.executable, "-u", *s], cwd=ROOT, env=env, stdout=log, stderr=subprocess.STDOUT).returncode
        log.write(f"=== {time.strftime('%Y-%m-%d_%H:%M')} rc={rc}\n")
        log.flush()
    log.write(f"=== {time.strftime('%Y-%m-%d_%H:%M')} all done\n")
