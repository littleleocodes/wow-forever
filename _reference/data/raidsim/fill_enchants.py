"""Fill missing permanent enchants in our gear sets from role templates (2026-10-09 audit).

    python _reference/data/raidsim/fill_enchants.py [--write]

The gear tools (gear_opt.py, gear_tiers.py) keep the enchant of the item a slot held before, so a set grown from a simulator preset
without enchants never got any: the Balance, feral cat, Retribution, Arms and Fury sets (standard, pre-BiS and BiS) had none while every
other spec carried 5-10. The templates are the enchants our other sets already use, which come from the community's presets: strength
melee as the Enhancement and hunter sets (Lesser Arcanum of Voracity +8 Strength on head and legs, Cloak +3 Agility, Chest +4 stats,
Bracer +9 Strength, Gloves +7 Strength, Boots +7 Agility, Crusader), agility melee as the rogue set (+8 Agility arcanums, Gloves +7
Agility), casters as the mage and Elemental sets (+8 Intellect arcanums, Chest +4 stats, Bracer +7 Intellect, Boots Minor Speed,
Weapon +30 Spell Power). Only empty enchant slots are filled; an off-hand gets Crusader only when it is a weapon. gear_tiers.make calls
`fill` on every set it writes, so a new set never lacks enchants again.
"""
import argparse
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
SETS = HERE / "gear_sets" / "forever"
DB = pathlib.Path.home() / ".wow-forever-tools" / "forever-repo" / "assets" / "database" / "db.json"

# slot index (the simulator's ItemSlot order) -> enchant effect id
STR_MELEE = {0: 1506, 3: 849, 4: 1891, 5: 1885, 6: 927, 8: 1506, 9: 1887, 14: 1900, 15: 1900}
AGI_MELEE = {0: 1508, 3: 849, 4: 1891, 5: 1885, 6: 1887, 8: 1508, 9: 1887, 14: 1900, 15: 1900}
CASTER = {0: 1509, 4: 1891, 5: 1883, 8: 1509, 9: 911, 14: 2504}
TEMPLATES = {"str-melee": STR_MELEE, "agi-melee": AGI_MELEE, "caster": CASTER}


def role(name):
    """The template for a gear-set file name (class first: warrior-..., druid-feral..., tiers/<class>-<spec slug>-<tier>)."""
    n = pathlib.Path(name).name
    if n.startswith(("warrior-", "paladin-retribution", "shaman-enhancement")):
        return "str-melee"
    if n.startswith(("druid-feral", "rogue-", "hunter-")):
        return "agi-melee"
    if n.startswith(("druid-balance", "mage-", "warlock-", "priest-", "shaman-elemental", "shaman-hybrid-elemental")):
        return "caster"
    return None


_db = {}


def items_db():
    if not _db:
        _db.update({i["id"]: i for i in json.load(open(DB, encoding="utf-8"))["items"]})
    return _db


def fill(items, tmpl):
    """Fill the empty enchant slots of `items` (a gear set's item list) from the template; returns the slots filled."""
    db = items_db()
    done = []
    for slot, ench in TEMPLATES[tmpl].items():
        if slot >= len(items) or not items[slot] or not items[slot].get("id") or items[slot].get("enchant"):
            continue
        it = db.get(items[slot]["id"], {})
        if slot in (14, 15) and it.get("type") != 13:
            continue   # a relic, shield or held-in-off-hand item takes no weapon enchant
        items[slot]["enchant"] = ench
        done.append(slot)
    return done


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--write", action="store_true")
    a = ap.parse_args()
    for f in sorted(list(SETS.glob("*.gear.json")) + list((SETS / "tiers").glob("*.gear.json"))):
        tmpl = role(f.name)
        if not tmpl:
            continue
        d = json.load(open(f, encoding="utf-8"))
        if sum(1 for x in d.get("items", []) if x and x.get("enchant")) >= 4:
            continue   # a set that has its enchants keeps its own choices
        done = fill(d["items"], tmpl)
        if done:
            print(f"{f.relative_to(SETS).as_posix()}: {tmpl}, {len(done)} enchants (slots {done})")
            if a.write:
                f.write_text(json.dumps(d, indent=1) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
