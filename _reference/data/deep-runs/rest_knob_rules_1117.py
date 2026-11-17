"""Set the REST_TOGETHER rules knob in the 21 leveling rules files of the seven mana classes (2026-11-17; user: "Yes, all classes"; run
by Claude right before fl_rest_1117.sh starts, after the night of 2026-11-16 is committed). Each file keeps its format (indent, line
endings, final newline); the knob goes into "knobs". --dry checks only."""
import json
import os
import pathlib
import sys

FL = pathlib.Path("F:/wow-forever/_reference/data/fightlab/rotations")
FILES = ["druid-balance-dps", "druid-feral-cat-dps", "hunter-bm-leveling", "hunter-melee-dps", "hunter-mm-raid", "mage-arcane-leveling",
         "mage-barrage-frost-leveling", "mage-fire-leveling", "mage-frost-leveling", "mage-frostfire-leveling", "paladin-holy-leveling",
         "paladin-prot-leveling", "paladin-ret-dps", "priest-discipline-leveling", "priest-holy-leveling", "priest-shadow-dps",
         "shaman-elemental-dps", "shaman-enhancement-dps", "warlock-affliction-leveling", "warlock-demonology-leveling",
         "warlock-destruction-leveling"]
DRY = "--dry" in sys.argv
for name in FILES:
    p = FL / f"{name}.json"
    raw = p.read_bytes().decode("utf-8")
    crlf, nl = "\r\n" in raw, raw.endswith("\n")
    data = json.loads(raw)
    ind = next((i for i in (1, 2, None) if ((json.dumps(data, indent=i, ensure_ascii=False) + ("\n" if nl else ""))
                                            .replace("\n", "\r\n" if crlf else "\n")) == raw), "?")
    if ind == "?":
        sys.exit(f"{name}: no json.dumps indent reproduces the file; not written")
    data.setdefault("knobs", {})["REST_TOGETHER"] = True
    t = json.dumps(data, indent=ind, ensure_ascii=False) + ("\n" if nl else "")
    if crlf:
        t = t.replace("\n", "\r\n")
    if DRY:
        print(f"{name}: ok (indent {ind}, crlf {crlf}, final newline {nl})")
        continue
    tmp = p.with_name(p.name + ".tmp")
    tmp.write_bytes(t.encode("utf-8"))
    os.replace(tmp, p)
    print(f"{name}: REST_TOGETHER true")
