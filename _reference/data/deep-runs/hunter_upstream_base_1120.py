"""The hunter parity race's decisions (2026-11-20, deep-runs/siml_upstream_race.py after the Hunter's Mark rank fix, search-improvements
0p; the rule of "Simulator build first": an entry takes the official simulator's rotation as its base unless ours leads by 0.5% on both
seeds for the entry's page pick, with our options). Full raid, 10,000 fights, seeds 1 / 2, our options:
- bm-raid -> upstream turret_hawk: beast-mastery-ml-raid (Beast Mastery's pick) +2.15% / +2.13%, beast-marks-ml-raid (Beast-Marks's)
  +2.13% / +2.10%, every build of the entry +2.1-2.4%;
- mm-raid -> upstream turret: marksmanship-ml-raid (Marksmanship's pick) +0.78% / +0.71%, the others +1.3-1.8%;
- mm-lonewolf-raid -> upstream turret: mm-lone-wolf-raid +0.02% / +0.01% (ours does not lead), the others +0.1-1.7%;
- melee-dps -> upstream melee: melee-survival-raid (Survival's) +3.16% / +3.11%, beast-survival-open-raid (Beast-Survival's) +2.20% /
  +2.21%, the others +2.5-4.3%;
- survival-pet-raid keeps ours: survival-raptor-raid (the simulator's SV Melee with its Raptor) -0.90% / -0.86% under upstream's.
Each entry's base (`apl`) becomes the upstream file and its tuned pointers (`apl_opt`, `apl_opt_raid`) go, so both settings run it until a
tune writes new ones; the old tuned files stay on disk. A text edit under specs.json's lock (apl_opt.py's convention).

    python _reference/data/deep-runs/hunter_upstream_base_1120.py [--write]
"""
import argparse
import json
import pathlib
import re
import sys

DATA = pathlib.Path(__file__).resolve().parents[1]
sys.path[:0] = [str(DATA), str(DATA / "raidsim")]
SPECS = DATA / "raidsim" / "specs.json"
UP = "_reference/data/raidsim/apls/hunter/upstream/"
SWITCH = {
    "bm-raid": ("turret_hawk", "beast-mastery-ml-raid +2.15% / +2.13%, beast-marks-ml-raid +2.13% / +2.10%"),
    "mm-raid": ("turret", "marksmanship-ml-raid +0.78% / +0.71%"),
    "mm-lonewolf-raid": ("turret", "mm-lone-wolf-raid +0.02% / +0.01%, the entry's other builds +0.1-1.7%"),
    "melee-dps": ("melee", "melee-survival-raid +3.16% / +3.11%, beast-survival-open-raid +2.20% / +2.21%"),
}


def block(text, start):
    """(begin, end) of the JSON object that starts at `start` (its opening brace)."""
    depth, i, instr, esc = 0, start, False, False
    while i < len(text):
        c = text[i]
        if instr:
            if esc:
                esc = False
            elif c == "\\":
                esc = True
            elif c == '"':
                instr = False
        elif c == '"':
            instr = True
        elif c == "{":
            depth += 1
        elif c == "}":
            depth -= 1
            if depth == 0:
                return start, i + 1
        i += 1
    raise SystemExit("unbalanced braces")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--write", action="store_true")
    a = ap.parse_args()
    from filelock import locked
    with locked(SPECS.with_suffix(".json.lock")):
        text = SPECS.read_text(encoding="utf-8")
        h = text.index('"hunter": {')
        hb, he = block(text, text.index("{", h))
        sec = text[hb:he]
        for entry, (rot, gains) in SWITCH.items():
            m = re.search(r'\n(\s*)"' + re.escape(entry) + r'": \{', sec)
            b0, b1 = block(sec, sec.index("{", m.start()))
            blk = sec[b0:b1]
            new = re.sub(r'\n\s*"apl_opt_raid": "[^"]*",', "", blk)
            new = re.sub(r'\n\s*"apl_opt": "[^"]*",', "", new)
            new = re.sub(r'("apl": )"[^"]*"', lambda mm: f'{mm.group(1)}"{UP}{rot}.apl.json"', new, count=1)
            note = (f"2026-11-20: base switched to the official simulator's own {rot} rotation (SIML, trainer ranks, Hunter's Mark mapped to "
                    f"our patch's rank 3; deep-runs/hunter_upstream_base_1120.py): the parity race in a full raid, 10,000 fights, seeds 1 / 2, "
                    f"our options: {gains} under it. Earlier notes describe the rotation it replaces. ")
            new = re.sub(r'("rotation_note": ")', lambda mm: mm.group(1) + note.replace('"', "'"), new, count=1)
            if '"rotation_note"' not in new:
                new = new[:-1].rstrip() + f',\n      "rotation_note": "{note.strip()}"\n    }}'
            sec = sec[:b0] + new + sec[b1:]
            print(f"{entry}: apl -> {UP}{rot}.apl.json; tuned pointers removed")
        out = text[:hb] + sec + text[he:]
        d = json.loads(out)   # still valid JSON
        for entry, (rot, _) in SWITCH.items():
            e = d["hunter"][entry]
            assert e["apl"].endswith(f"upstream/{rot}.apl.json") and "apl_opt" not in e and "apl_opt_raid" not in e, entry
        if a.write:
            SPECS.write_text(out, encoding="utf-8", newline="")
            print("wrote specs.json")


if __name__ == "__main__":
    main()
