"""Rotation lines that never fire, removed from our rotation files (2026-11-20, the play check's (a): a page built from them would print
them). Each removal is behaviour-neutral: the simulator cannot cast the line, so no build ever did.
- frost-raid (raid and dummy): the official Frost rotation's pre-pull Blink, timed at minus Blink's own aura; the simulator's Blink only
  moves the mage toward the boss, and our entry stands at 10 yards for Cone of Cold (a deliberate difference), so it never fires.
- spells the game no longer has, by the client's own tables (SpellName 70938; the shaman's skill line had Lava Burst in 70753 and
  70755, not from 70790 on): Lava Burst (1238300, 1326047) in the Elemental and Stormcaller rotations, Frost Blast (1326055) in three
  mage dummy rotations; Classic's Tiger's Fury rank 1 (5217) in the cat's dummy rotation (Forever's ranks have other ids).
- Diamond Flask's spell (24427) cast as a spell in the warrior rotations: a trinket's use is cast by its item id, and no warrior gear
  set holds the flask.
- Arms in Battle Stance's raid rotation: Whirlwind needs Berserker Stance, which the rotation never takes, and its unconditional
  Mocking Blow never fired in any build of the entry.
The converted official copies (apls/<class>/upstream/) keep every line: they must equal a fresh conversion (play_check.py's (e)).

    python _reference/data/deep-runs/dead_lines_1120.py [--write]
"""
import argparse
import json
import pathlib

DATA = pathlib.Path(__file__).resolve().parents[1]
NAMES = {1953: "Blink", 1238300: "Lava Burst", 1326047: "Lava Burst", 1326055: "Frost Blast", 5217: "Tiger's Fury rank 1",
         24427: "Diamond Flask (spell)", 1680: "Whirlwind", 20560: "Mocking Blow"}
DEAD = {"raidsim/apls/mage/frost-raid-raid.apl.json": [1953], "raidsim/apls/mage/frost-raid.apl.json": [1953],
        "raidsim/apls/shaman/elemental-dps-raid.apl.json": [1238300, 1326047], "raidsim/apls/shaman/elemental-dps.apl.json": [1238300, 1326047],
        "raidsim/apls/shaman/stormcaller-dps-raid.apl.json": [1238300, 1326047], "raidsim/apls/shaman/stormcaller-dps.apl.json": [1238300, 1326047],
        "raidsim/apls/mage/arcane-dps.apl.json": [1326055], "raidsim/apls/mage/arcane-frost-raid.apl.json": [1326055],
        "raidsim/apls/mage/fire-raid.apl.json": [1326055], "raidsim/apls/druid/feral-cat-dps.apl.json": [5217],
        **{f"raidsim/apls/warrior/{n}.apl.json": [24427] for n in ("arms-2h-raid-raid", "arms-2h-raid", "arms-battle-raid-raid",
                                                                    "arms-battle-raid", "arms-battle-raid.base", "fury-dw-raid-raid",
                                                                    "fury-dw-raid")},
        # Arms in Battle Stance never leaves it (no Berserker Stance in the file): its two Whirlwind lines can never fire, and its
        # unconditional Mocking Blow never fired in any build of the entry (the play check, full raid)
        "raidsim/apls/warrior/arms-battle-raid-raid.apl.json": [24427, 1680, 20560]}


def cast_of(x):
    act = (x or {}).get("action") or {}
    for k in ("castSpell", "channelSpell"):
        sid = ((act.get(k) or {}).get("spellId") or {}).get("spellId")
        if sid:
            return sid
    return None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--write", action="store_true")
    a = ap.parse_args()
    for rel, ids in DEAD.items():
        p = DATA / rel
        text = p.read_text(encoding="utf-8")
        d = json.loads(text)
        notes = []
        for part in ("prepullActions", "priorityList"):
            keep = []
            for x in d.get(part) or []:
                if cast_of(x) in ids:
                    notes.append(f"{part}: removed {NAMES[cast_of(x)]}")
                else:
                    keep.append(x)
            d[part] = keep
        print(f"{rel}: {'; '.join(notes) or 'nothing to do'}")
        if a.write and notes:
            indent = 2 if text.startswith("{\n  ") or text.startswith("{\r\n  ") else 1
            p.write_text(json.dumps(d, indent=indent) + "\n", encoding="utf-8", newline="\r\n" if "\r\n" in text else "")


if __name__ == "__main__":
    main()
