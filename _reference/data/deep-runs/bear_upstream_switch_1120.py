"""feral-bear-tank takes the official simulator's own bear rotation as its base (2026-11-20 night, the audit session's D12). Since the
rotation search of 2026-10-27 our raid rotation's line 4 cast Maul's swing-damage spell (9881 tag 1, registered without the rotation
flag in sim/druid/maul.go) instead of its queue spell (9881 untagged): it fired off the swing timer, 227 Maul hits and all 72 white
swings in a 180 s fight, about seven times the threat and damage. The audit's measurement (tank setting, 3,000 fights, seeds 1 / 2):
feral-combat-ml-tank 6622 / 6612 threat a second as committed, 950 / 947 with the queue spell, 1007 / 1004 under the simulator's own
rotation; opt-feral-bear-tank-raid-tank 8049, 997, 1601. The line is fixed in our file (kept for the record) and the entry's base
becomes upstream/feralbear-adaptive.apl.json (converted by trainer ranks, as tank_upstream_race.py does), its tuned raid pointer goes,
and the tank lane re-tunes and checks the bear from there.

    python _reference/data/deep-runs/bear_upstream_switch_1120.py [--write]
"""
import argparse
import json
import re
import sys

import hunter_upstream_base_1120 as HB

CLS, ENTRY = "druid", "feral-bear-tank"
UP = "_reference/data/raidsim/apls/druid/upstream/feralbear-adaptive.apl.json"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--write", action="store_true")
    a = ap.parse_args()
    from filelock import locked
    with locked(HB.SPECS.with_suffix(".json.lock")):
        text = HB.SPECS.read_text(encoding="utf-8")
        h = text.index(f'"{CLS}": {{')
        hb, he = HB.block(text, text.index("{", h))
        sec = text[hb:he]
        m = re.search(r'\n(\s*)"' + re.escape(ENTRY) + r'": \{', sec)
        b0, b1 = HB.block(sec, sec.index("{", m.start()))
        blk = sec[b0:b1]
        new = re.sub(r'\n\s*"apl_opt_raid": "[^"]*",', "", blk)
        new = re.sub(r'\n\s*"apl_opt": "[^"]*",', "", new)
        new = re.sub(r',(\s*)"apl_opt_raid": "[^"]*"', "", new)
        new = re.sub(r'("apl": )"[^"]*"', lambda mm: f'{mm.group(1)}"{UP}"', new, count=1)
        note = ("2026-11-20 night: base switched to the official simulator's own bear rotation (bear_upstream_switch_1120.py, the audit's "
                "D12): our tuned raid rotation had cast Maul's swing-damage spell (9881 tag 1) since 2026-10-27, about seven times the "
                "threat; with the queue spell it trails the simulator's rotation in every arm. Earlier notes describe the rotation it replaces. ")
        if '"rotation_note"' in new:
            new = re.sub(r'("rotation_note": ")', lambda mm: mm.group(1) + note.replace('"', "'"), new, count=1)
        else:
            new = new[:-1].rstrip() + f',\n      "rotation_note": "{note.strip()}"\n    }}'
        sec = sec[:b0] + new + sec[b1:]
        out = text[:hb] + sec + text[he:]
        e = json.loads(out)[CLS][ENTRY]
        assert e["apl"] == UP and "apl_opt" not in e and "apl_opt_raid" not in e, e
        print(f"{ENTRY}: apl -> {UP}; tuned raid pointer removed")
        if a.write:
            HB.SPECS.write_text(out, encoding="utf-8", newline="")
            print("wrote specs.json")


if __name__ == "__main__":
    sys.exit(main())
