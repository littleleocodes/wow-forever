"""Re-run the Classic-era calibration cases and show whether the model still lands on the community builds.

    python _reference/data/scorer/classic_check.py [--write]

Every `<class>/talents/classic-baseline/optimizer/<spec>-<profile>.md` names the community build it was compared with
("## Comparison with `<id>`: <split> scores +x% vs optimized +y%"). This script re-runs each case (`run.py <class>
--game classic-era --spec <spec> --profile <profile> --compare <id>`), prints the old and new optimized splits and comparison lines and flags a case whose
optimized build moved (scores alone moving means shared spec-model inputs such as the calibrated shares changed). Run it after changing the scorer's model code or a shared effect encoding
(CLAUDE.md); `--write` refreshes the Classic reports. The verdict table in README.md is kept by hand.
"""
import argparse
import pathlib
import re
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[2]
CLASSES = ["druid", "hunter", "mage", "paladin", "priest", "rogue", "shaman", "warlock", "warrior"]
PROFILES = ["leveling-st", "leveling-aoe", "solo-60", "raid-dps-extwc", "raid-dps", "raid-heal", "raid-tank"]
LINE = re.compile(r"^## Comparison with `([^`]+)`: (\S+) scores ([+-][0-9.]+%) vs optimized ([+-][0-9.]+%)", re.M)
SPLIT = re.compile(r"^## Optimized build: (\S+)", re.M)


def cases():
    out = []
    for cls in CLASSES:
        for f in sorted((ROOT / cls / "talents/classic-baseline/optimizer").glob("*.md")):
            spec, profile = None, None
            for p in PROFILES:
                if f.stem.endswith("-" + p):
                    spec, profile = f.stem[: -len(p) - 1], p
                    break
            if not spec:
                continue
            text = f.read_text(encoding="utf-8")
            m = LINE.search(text)
            sp = SPLIT.search(text)
            if m:
                out.append((cls, spec, profile, m.group(1), m.group(0), sp.group(1) if sp else "?"))
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--write", action="store_true")
    ap.add_argument("classes", nargs="*")
    a = ap.parse_args()
    moved = 0
    for cls, spec, profile, ref, old, old_split in cases():
        if a.classes and cls not in a.classes:
            continue
        args = [sys.executable, str(HERE / "run.py"), cls, "--game", "classic-era", "--spec", spec, "--profile", profile, "--compare", ref] + (["--write"] if a.write else [])
        r = subprocess.run(args, capture_output=True, text=True, encoding="utf-8", errors="replace", cwd=str(ROOT))
        m = LINE.search(r.stdout)
        sp = SPLIT.search(r.stdout)
        new_split = sp.group(1) if sp else "?"
        new = m.group(0) if m else f"(no comparison line; rc={r.returncode}) {r.stderr[-300:]}"
        split_moved = new_split != old_split
        score_moved = (m is None) or (m.group(4) != re.search(r"optimized ([+-][0-9.]+%)", old).group(1))
        moved += split_moved
        tag = "SPLIT MOVED" if split_moved else ("score moved" if score_moved else "same")
        print(f"{tag:11} {cls} {spec}/{profile} vs {ref} ({m.group(2) if m else '?'}): optimized {old_split} -> {new_split}")
        if split_moved:
            print("   was:", old[:150])
            print("   now:", new[:150])
    print(f"{moved} case(s) changed their optimized build; scores alone moving means the shared spec-model inputs changed")
    return 0   # a moved build is a finding for the README table, not an error (rebuild.py runs this as its last classic step)


if __name__ == "__main__":
    sys.exit(main())
