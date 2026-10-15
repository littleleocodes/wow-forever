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
Healers (2026-10-15, heallab/heal_gear.py): `HEALER_CANDIDATES` lists, per slot, the Classic phase-1 enchants a healer chooses from (the
same availability as the caster template: Dire Maul's lesser arcanums, Greater Stats, the Argent Dawn bracers, Molten Core's weapon
formulas); heal_gear.py takes the one worth most by the healer lab's stat weights, `HEALER` is the fallback `fill` uses. Forever's new
enchants (necklace, held-in-off-hand, the shield's Law of Nature, the 2H Mighty Healing Power) are left out: their source and phase are
unknown.
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
HEALER = {0: 1509, 4: 1891, 5: 2566, 8: 1509, 9: 851, 14: 2505}
# slot -> candidate enchant effect ids ("1h"/"2h"/"shield" for the hands): +8 Int / +8 Spirit / Arcanum of Focus (+8 healing); Greater Stats /
# Major Intellect; bracer +7 Int / +9 Spirit / +4 mp5 / +24 healing; boots +5 Spirit / Minor Speed; weapon +55 healing / +30 spell power /
# +22 Int / +22 Spirit (2H also +9 Int / +9 Spirit); shield +9 / +7 Spirit
HEALER_CANDIDATES = {0: [1509, 1510, 2544], 4: [1891, 1893], 5: [1883, 1884, 2565, 2566], 8: [1509, 1510, 2544], 9: [851, 911],
                     "1h": [2505, 2504, 2568, 2567], "2h": [2505, 2504, 2568, 2567, 1904, 1903], "shield": [1890, 907]}
HEALER_FILES = ("priest-holy-", "priest-discipline-", "paladin-holy-", "druid-restoration-", "shaman-restoration-")
# Tanks (2026-10-15, raidsim/tank_gear.py): the Classic phase-1 tank enchants (Dire Maul's +8 Stamina / +8 Agility arcanums, Cloak +70 armor /
# +3 Agility, Greater Stats, bracer +9 Stamina, gloves +7 Agility, boots +7 Stamina / +7 Agility, Crusader, shield +9 Stamina: effect 1886
# is "Enchant Shield - Greater Stamina" in the fork's database). Slot 15 of a tank template is the shield's (filled only on a shield).
# `TANK_CANDIDATES` lists, per slot, what tank_gear.py chooses from by the tank's stat weights (the template's pick first: it wins ties);
# weapons ("1h"/"2h") are raced in the simulator (Crusader, +9 weapon damage and +30 spell power carry no stats to weigh).
TANK_PLATE = {0: 1507, 3: 1889, 4: 1891, 5: 1886, 6: 1887, 8: 1507, 9: 929, 14: 1900, 15: 1886}
TANK_BEAR = {0: 1508, 3: 849, 4: 1891, 5: 1886, 6: 1887, 8: 1508, 9: 1887, 14: 1900}
TANK_CANDIDATES = {0: [1507, 1508, 1506], 3: [1889, 849], 4: [1891, 1892], 5: [1886, 1885, 923], 6: [1887, 927], 8: [1507, 1508, 1506],
                   9: [929, 1887], "1h": [1900, 2504], "2h": [1900, 1896], "shield": [1886, 929]}
TANK_FILES = ("warrior-protection-", "paladin-protection-", "druid-feral-combat-tank-")
TEMPLATES = {"str-melee": STR_MELEE, "agi-melee": AGI_MELEE, "caster": CASTER, "healer": HEALER, "tank-plate": TANK_PLATE, "tank-bear": TANK_BEAR}


def role(name):
    """The template for a gear-set file name (class first: warrior-..., druid-feral..., tiers/<class>-<spec slug>-<tier>)."""
    n = pathlib.Path(name).name
    if n.startswith(HEALER_FILES):   # healer tier sets (heal_gear.py); no damage set has these names
        return "healer"
    if n.startswith(TANK_FILES):   # tank tier sets (tank_gear.py); no damage set has these names
        return "tank-bear" if n.startswith("druid-") else "tank-plate"
    if n.startswith(("warrior-","paladin-retribution", "shaman-enhancement")):
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
        if tmpl.startswith("tank-") and slot == 15 and it.get("weaponType") != 7:
            continue   # a tank template's slot 15 is the shield's
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
