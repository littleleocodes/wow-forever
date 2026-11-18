"""Switch the raid's Windfury Totem off for the shaman's enhancement-dps simulator entry (2026-11-17; user: "After eat-and-drink
(Recommended)" to the fix). Forever's Windfury Weapon tooltip (rank 4, 16362): "When applied to main hand, disables any benefit you
personally receive from Windfury Totem"; the simulator's full raid (2e6e77d84) gives the shaman the totem's procs on top of its own
imbue (about 9% of an Enhancement build's damage there). Every build raced in the entry plays Windfury Weapon. A text edit under the
specs lock keeps the file's layout (as apl_opt._point_specs); --dry prints only. Run by wf_enh_1117.sh."""
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
RAIDSIM = HERE.parent / "raidsim"
sys.path.insert(0, str(HERE.parent))
from filelock import locked  # noqa: E402

SP = RAIDSIM / "specs.json"
CLS, ENTRY, BUFF = "shaman", "enhancement-dps", "windfury_totem"

with locked(RAIDSIM / "specs.json.lock"):
    s = SP.read_text(encoding="utf-8")
    data = json.loads(s)
    have = data[CLS][ENTRY].get("buffs_off", [])
    if BUFF in have:
        print(f"{CLS} {ENTRY}: buffs_off already holds {BUFF}")
        sys.exit(0)
    if have:
        sys.exit(f"{CLS} {ENTRY}: buffs_off {have} exists; add {BUFF} by hand")
    i = s.find(f'\n  "{CLS}": {{')
    j = s.find(f'"{ENTRY}": {{\n', i)
    if i < 0 or j < 0:
        sys.exit(f"specs.json: cannot find {CLS} {ENTRY}")
    k = j + len(f'"{ENTRY}": {{\n')
    indent = s[k:len(s[:k]) + len(s[k:]) - len(s[k:].lstrip(" "))]
    new = s[:k] + f'{indent}"buffs_off": ["{BUFF}"],\n' + s[k:]
    d2 = json.loads(new)
    assert d2[CLS][ENTRY]["buffs_off"] == [BUFF]
    assert {c: v for c, v in d2.items() if c != CLS} == {c: v for c, v in data.items() if c != CLS}
    if "--dry" in sys.argv:
        print(f"dry: would add buffs_off [{BUFF}] to {CLS} {ENTRY} (indent {len(indent)})")
        sys.exit(0)
    SP.write_text(new, encoding="utf-8")
    print(f"{CLS} {ENTRY}: buffs_off [{BUFF}] written")
