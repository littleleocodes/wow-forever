"""Fill missing permanent enchants in our gear sets from role templates (2026-10-09 audit).

    python _reference/data/raidsim/fill_enchants.py [--write]

The gear tools (gear_opt.py, gear_tiers.py) keep the enchant of the item a slot held before, so a set grown from a simulator preset
without enchants never got any: the Balance, feral cat, Retribution, Arms and Fury sets (standard, pre-BiS and BiS) had none while every
other spec carried 5-10. The templates are the enchants our other sets already use, which come from the community's presets: strength
melee as the Enhancement and hunter sets (Lesser Arcanum of Voracity +8 Strength on head and legs, Cloak +3 Agility, Chest +4 stats,
Bracer +9 Strength, Gloves +7 Strength, Boots +7 Agility, Crusader), agility melee as the rogue set (+8 Agility arcanums, Gloves +7
Agility), casters as the mage and Elemental sets (+8 Intellect arcanums, Chest +4 stats, Bracer +7 Intellect, Boots Minor Speed,
Weapon +30 Spell Power). Only empty enchant slots are filled (plus the weak enchants in `UPGRADE`), in every set since 2026-10-18 (sets
with 4+ enchants had been skipped); an off-hand gets Crusader only when it is a weapon. gear_tiers.make calls
`fill` on every set it writes, so a new set never lacks enchants again.
Healers (2026-10-15, heallab/heal_gear.py): `HEALER_CANDIDATES` lists, per slot, the Classic phase-1 enchants a healer chooses from (the
same availability as the caster template: Dire Maul's lesser arcanums, Greater Stats, the Argent Dawn bracers, Molten Core's weapon
formulas); heal_gear.py takes the one worth most by the healer lab's stat weights, `HEALER` is the fallback `fill` uses. Forever's new
enchants (necklace, held-in-off-hand, the shield's Law of Nature, the 2H Mighty Healing Power) were left out until 2026-11-22: their
source and phase were unknown.
Since 2026-11-22 (the audit session's gear finding G1: a community Survival list carried Forever's enchants, +1.1% from four of them):
the damage specs' sets take their enchants from the simulator's database by the tier's rules (gear_tiers.choose_enchants: the stat
enchants by the weights, the others raced; the templates below only fill a starting set). The healer and tank lists gained Forever's
vendor-sold enchants (the necklaces, Bracer - Greater Spellpower and Superior Deflection, Gloves - Superior Strength, the 2H Spellblasting
and Mighty Healing Power, Off-Hand - Wisdom) and the stronger Classic ones; heal_gear.py and tank_gear.py keep only the candidates the
tier's enchant pool allows (gear_tiers.enchant_allowed: Molten Core's Spell Power and Healing Power weapon formulas are no pre-raid
enchant, Classic's Ahn'Qiraj formulas none at all).
"""
import argparse
import json
import os
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
SETS = HERE / "gear_sets" / "forever"
# the simulator's item database: the official wowsims/forever clone since 2026-10-22 (run.py's default repository; WOW_FOREVER_SIM overrides)
DB = pathlib.Path(os.environ.get("WOW_FOREVER_SIM", pathlib.Path.home() / ".wow-forever-tools" / "wowsims-forever")) / "assets" / "database" / "db.json"

# slot index (the simulator's ItemSlot order) -> enchant effect id
STR_MELEE = {0: 1506, 3: 849, 4: 1891, 5: 1885, 6: 927, 8: 1506, 9: 1887, 14: 1900, 15: 1900}
AGI_MELEE = {0: 1508, 3: 849, 4: 1891, 5: 1885, 6: 1887, 8: 1508, 9: 1887, 14: 1900, 15: 1900}
CASTER = {0: 1509, 4: 1891, 5: 1883, 8: 1509, 9: 911, 14: 2504}
HEALER = {0: 1509, 4: 1891, 5: 2566, 8: 1509, 9: 851, 14: 2505}
# slot -> candidate enchant effect ids ("1h"/"2h"/"shield" for the hands): +8 Int / +8 Spirit / Arcanum of Focus (+8 healing); Greater Stats /
# Major Intellect; bracer +7 Int / +9 Spirit / +4 mp5 / +24 healing; boots +5 Spirit / Minor Speed; weapon +55 healing / +30 spell power /
# +22 Int / +22 Spirit (2H also +9 Int / +9 Spirit); shield +9 / +7 Spirit
HEALER_CANDIDATES = {0: [1509, 1510, 2544], 1: [8219, 8218], 4: [1891, 1893, 8492], 5: [1883, 1884, 2565, 2566, 7665, 8209, 1901],
                     6: [8492], 8: [1509, 1510, 2544], 9: [851, 911, 8492],
                     "1h": [2505, 2504, 2568, 2567], "2h": [2505, 2504, 2568, 2567, 1904, 1903, 8212, 7662, 8211], "shield": [1890, 907],
                     "offhand": [7661]}   # (2026-11-22: 1 the necklaces, 8492 Mystic Rugged Armor Kit, 7665 / 8209 / 1901 bracers, 8212 /
                                          # 7662 / 8211 the 2H spell power and healing, 7661 Off-Hand - Wisdom)
HEALER_FILES = ("priest-holy-", "priest-discipline-", "paladin-holy-", "druid-restoration-", "shaman-restoration-")
# Tanks (2026-10-15, raidsim/tank_gear.py): the Classic phase-1 tank enchants (Dire Maul's +8 Stamina / +8 Agility arcanums, Cloak +70 armor /
# +3 Agility, Greater Stats, bracer +9 Stamina, gloves +7 Agility, boots +7 Stamina / +7 Agility, Crusader, shield +9 Stamina: effect 1886
# is "Enchant Shield - Greater Stamina" in the fork's database and "Enchant Bracer - Superior Stamina" in the official one: one effect id,
# both enchants). Slot 15 of a tank template is the shield's (filled only on a shield).
# `TANK_CANDIDATES` lists, per slot, what tank_gear.py chooses from by the tank's stat weights (the template's pick first: it wins ties);
# weapons ("1h"/"2h") are raced in the simulator (Crusader, +9 weapon damage and +30 spell power carry no stats to weigh).
TANK_PLATE = {0: 1507, 3: 1889, 4: 1891, 5: 1886, 6: 1887, 8: 1507, 9: 929, 14: 1900, 15: 1886}
TANK_BEAR = {0: 1508, 3: 849, 4: 1891, 5: 1886, 6: 1887, 8: 1508, 9: 1887, 14: 1900}
TANK_CANDIDATES = {0: [1507, 1508, 1506], 1: [925, 856, 904], 3: [1889, 849, 7667], 4: [1891, 1892], 5: [1886, 1885, 923, 8214, 7656],
                   6: [1887, 927, 8206, 8207, 2563], 8: [1507, 1508, 1506], 9: [929, 1887],
                   "1h": [1900, 2504, 2564, 2563], "2h": [1900, 1896, 2646], "shield": [1886, 929]}   # (2026-11-22: 1 the necklaces,
                   # 7667 Cloak - Agility, 8214 Superior Deflection, 7656 Bracer +9 Agility, 8206 / 8207 / 2563 gloves, 2564 / 2563 / 2646 weapons)
TANK_FILES = ("warrior-protection-", "paladin-protection-", "druid-feral-combat-tank-")
# weaker enchants a set carried from a preset, replaced by the template's (audit 2026-10-18 row 52: the standard warlock set had Chest +3
# stats, effect 928, where every template has Greater Stats 1891)
UPGRADE = {4: {928: 1891}}
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
        if slot >= len(items) or not items[slot] or not items[slot].get("id"):
            continue
        if items[slot].get("enchant") in UPGRADE.get(slot, {}) and UPGRADE[slot][items[slot]["enchant"]] == ench:
            items[slot]["enchant"] = ench
            done.append(slot)
            continue
        if items[slot].get("enchant"):
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
        # every set: only empty slots are filled (and UPGRADE's weak enchants replaced), so a set's own choices stay. Until 2026-10-18 a
        # set with 4+ enchants was skipped, and the standard warlock set kept empty head and leg slots (audit 2026-10-18 row 52)
        done = fill(d["items"], tmpl)
        if done:
            print(f"{f.relative_to(SETS).as_posix()}: {tmpl}, {len(done)} enchants (slots {done})")
            if a.write:
                f.write_text(json.dumps(d, indent=1) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
