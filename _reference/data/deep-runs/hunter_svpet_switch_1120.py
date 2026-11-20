"""survival-pet-raid takes the official melee rotation (2026-11-20 evening, the hunter parity race with Hunter's Mark fixed,
deep-runs/hunter_parity_1120b.py, raidsim/hunter-parity-1120b.json): full raid, 10,000 fights, seeds 1 / 2, our options:
survival-raptor-raid 915.6 / 915.3 under the official melee rotation against 879.7 / 879.8 under ours with both mark lines (+4.06%);
melee-survival-raid 824.3 / 824.2 against 765.2 / 765.0. In the morning's race (both sides without a working mark) ours had led by
0.9%. The entry's base becomes upstream/melee.apl.json and its tuned pointers go, as hunter_upstream_base_1120.py did for the other four.

    python _reference/data/deep-runs/hunter_svpet_switch_1120.py [--write]
"""
import argparse
import json
import re
import sys

import hunter_upstream_base_1120 as HB

ENTRY, ROT = "survival-pet-raid", "melee"
GAINS = "survival-raptor-raid +4.06% (915.6 / 915.3 against 879.7 / 879.8), melee-survival-raid +7.7%"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--write", action="store_true")
    a = ap.parse_args()
    from filelock import locked
    with locked(HB.SPECS.with_suffix(".json.lock")):
        text = HB.SPECS.read_text(encoding="utf-8")
        h = text.index('"hunter": {')
        hb, he = HB.block(text, text.index("{", h))
        sec = text[hb:he]
        m = re.search(r'\n(\s*)"' + re.escape(ENTRY) + r'": \{', sec)
        b0, b1 = HB.block(sec, sec.index("{", m.start()))
        blk = sec[b0:b1]
        new = re.sub(r'\n\s*"apl_opt_raid": "[^"]*",', "", blk)
        new = re.sub(r'\n\s*"apl_opt": "[^"]*",', "", new)
        new = re.sub(r'("apl": )"[^"]*"', lambda mm: f'{mm.group(1)}"{HB.UP}{ROT}.apl.json"', new, count=1)
        note = (f"2026-11-20 evening: base switched to the official simulator's own {ROT} rotation (hunter_svpet_switch_1120.py): the parity "
                f"race with Hunter's Mark fixed, full raid, 10,000 fights, seeds 1 / 2, our options: {GAINS} under it. Earlier notes describe "
                "the rotation it replaces. ")
        new = re.sub(r'("rotation_note": ")', lambda mm: mm.group(1) + note.replace('"', "'"), new, count=1)
        if '"rotation_note"' not in new:
            new = new[:-1].rstrip() + f',\n      "rotation_note": "{note.strip()}"\n    }}'
        sec = sec[:b0] + new + sec[b1:]
        out = text[:hb] + sec + text[he:]
        e = json.loads(out)["hunter"][ENTRY]
        assert e["apl"].endswith(f"upstream/{ROT}.apl.json") and "apl_opt" not in e and "apl_opt_raid" not in e
        print(f"{ENTRY}: apl -> {HB.UP}{ROT}.apl.json; tuned pointers removed")
        if a.write:
            HB.SPECS.write_text(out, encoding="utf-8", newline="")
            print("wrote specs.json")


if __name__ == "__main__":
    sys.exit(main())
