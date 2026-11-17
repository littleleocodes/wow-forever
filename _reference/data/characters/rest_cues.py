"""Out-of-combat rest cues for an in-game add-on, every class and leveling spec (2026-11-16, user: "I want the addon to not proc during
combat. Also, I just want to be eat/drink/evocation for now. Also I want it to work across all different classes and specs").

    python _reference/data/characters/rest_cues.py      -> _reference/data/characters/addon/forever-rest-cues.json

For each leveling page pick (signature_audit.page_slots(<class>, signature=True), as the gear values): the fight lab's module with its
spec's tuned rules (run.make_module, the rules file fightlab/rotations/<class>-<rotation>.json) gives the thresholds the leveling pages
play by, between fights:
  - drink_below: drink when mana is under this share of the maximum (the rules' drink_below, else the module's, else tables.DRINK_BELOW);
    null for a class without mana;
  - eat_below: eat when health is under this share (likewise, tables.EAT_BELOW);
  - the class's own mana tools between fights, checked against the module's behaviour each run (the file fails to write when a module's
    rule moved): the mage's Evocation (from level 20, when it is ready and mana is under the rules' EVO_BELOW, one value for every mage
    spec since the add-on's cue is one per class: 15% since 2026-11-16, 40% before; mage.evocation) and the warlock's Life Tap
    (back to 70% mana while health stays above 60%: warlock.after_fight). Other classes' tools the leveling rules do not play
    (Innervate, mana gems, potions) are not listed.
The lab drinks and eats back to full once a cue fires. The add-on is the Addons session's (it matches a character to the nearest build
by talents, as GearCheck does). Numbers are the fight lab's model of the game, not measurements.
"""
import datetime
import json
import os
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
DATA = HERE.parent
sys.path[:0] = [str(DATA / "fightlab"), str(DATA), str(DATA / "scorer")]
import run as FR  # noqa: E402
import tables  # noqa: E402
import level_guides as LG  # noqa: E402

OUT = HERE / "addon" / "forever-rest-cues.json"
CLASSES = ["druid", "hunter", "mage", "paladin", "priest", "rogue", "shaman", "warlock", "warrior"]
def evocation_tool(thr):
    """The mage's cue at the rules' EVO_BELOW (the same in every mage spec's rules; main() checks it)."""
    return {"spell": "Evocation", "min_level": 20, "mana_below": round(thr, 3), "needs_ready": True,
            "note": f"between fights, before drinking: Evocation when it is ready and mana is under {thr:.0%} (fightlab/mage.py, evocation; "
                    "the rules' EVO_BELOW)"}


TOOLS = {
    "warlock": [{"spell": "Life Tap", "min_level": 6, "mana_below": 0.70, "health_above": 0.60, "repeat": True,
                 "note": "between fights, instead of drinking: Life Tap back to 70% mana while health stays above 60% "
                         "(fightlab/warlock.py, after_fight); eat afterwards when health is under eat_below"}],
}


def check_tools(cls, mod):
    """The module still plays the listed tool as written (a rule that moved stops the file from being written). Returns the mage's
    Evocation threshold."""
    p = mod.make_player(60)
    if cls == "mage":
        thr = float(mod.EVO_BELOW)
        p.mana = (thr - 0.01) * p.mana_max
        assert mod.evocation(p, 0.0) > 0, f"mage: Evocation no longer fires under {thr:.0%} mana"
        p2 = mod.make_player(60)
        p2.mana = (thr + 0.01) * p2.mana_max
        assert mod.evocation(p2, 0.0) == 0, f"mage: Evocation fires above {thr:.0%} mana"
        return thr
    elif cls == "warlock":
        p.mana, p.hp = 0.50 * p.mana_max, p.hp_max
        assert mod.after_fight(p, 0.0) > 0 and p.mana >= 0.70 * p.mana_max - 1e-6 or p.hp <= 0.60 * p.hp_max + mod.mana_cost(mod.spells["Life Tap"]), \
            "warlock: Life Tap no longer taps back to 70%"
        p2 = mod.make_player(60)
        p2.mana, p2.hp = 0.75 * p2.mana_max, p2.hp_max
        assert mod.after_fight(p2, 0.0) == 0 or p2.mana == 0.75 * p2.mana_max, "warlock: Life Tap above 70% mana"


def main():
    SA = LG.fightlab_signature_audit()
    out = {"made": datetime.datetime.now().astimezone().isoformat(timespec="seconds"),
           "about": __doc__.split("\n\n")[0].replace("\n", " "),
           "rules": "Out of combat only. drink_below / eat_below: shares of maximum mana / health; tools: the class's own mana tools between "
                    "fights, in order (a tool's cue comes before drinking). The fight lab drinks and eats back to full once a cue fires.",
           "classes": {}}
    for cls in CLASSES:
        specs = {}
        checked = False
        evo = {}
        for slot in SA.page_slots(cls, signature=True):
            spec = slot[0]
            b, order, prov, rot = LG.pick(cls, spec)
            if not b or not rot:
                continue
            talents = FR.allocation_at(b, 60)
            mod = FR.make_module(cls, talents, 60, rot)
            p = mod.make_player(60)
            has_mana = p.mana_max > 0
            drink = (mod.drink_below or tables.DRINK_BELOW) if has_mana else None
            eat = mod.eat_below or tables.EAT_BELOW
            if cls == "mage":   # every spec: its own rules set the threshold
                evo[spec] = check_tools(cls, mod)
            elif not checked and cls in TOOLS:
                check_tools(cls, mod)
                checked = True
            specs[spec] = {"build": b["id"], "rotation": rot, "drink_below": round(drink, 3) if drink is not None else None,
                           "eat_below": round(eat, 3), "talents": {k: v for k, v in sorted(talents.items()) if v}}
            dtxt = "-" if drink is None else f"{drink:.0%}"
            print(f"  {cls:8s} {spec:34s} {b['id']:38s} drink {dtxt:>5}  eat {eat:.0%}", flush=True)
        tools = TOOLS.get(cls, [])
        if cls == "mage" and evo:
            assert len(set(evo.values())) == 1, (f"mage: the specs' rules differ in EVO_BELOW {evo}; the add-on's Evocation cue is one per "
                                                 "class: agree a per-spec field with the Addons session first")
            tools = [evocation_tool(next(iter(evo.values())))]
        out["classes"][cls] = {"tools": tools, "specs": specs}
    OUT.parent.mkdir(parents=True, exist_ok=True)
    tmp = OUT.with_name(OUT.name + ".tmp")
    tmp.write_bytes((json.dumps(out, indent=1, ensure_ascii=False) + "\n").encode("utf-8"))
    os.replace(tmp, OUT)
    print(f"wrote {OUT}")


if __name__ == "__main__":
    main()
