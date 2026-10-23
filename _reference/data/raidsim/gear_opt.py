"""Equal-tier raid gear for every damage spec (2026-09-30, user request: the cross-spec raid ranking mixed gear levels).

    python _reference/data/raidsim/gear_opt.py [classes] [--write] [--fresh]   # optimize (and record)
    python _reference/data/raidsim/gear_opt.py --apply                         # a separate call: write the recorded sets and point specs.json at them
    (--apply alone applies the record as it is: never combine it with a fresh optimization in one call)

The simulator's gear presets are not one tier: the warrior's "p1" sets average item level 59, Shadow's pre-raid set 60, the paladin's
default 61, while mage, hunter, warlock and rogue sets are phase-1 raid gear (65-68). So the class ranking partly ranked gear. This
builds, for every group of raid entries sharing a gear set, the best **phase-1** set we can find and keeps it only when the simulator
says it beats the current one:

1. Pool: items that drop in 5-man dungeons, Molten Core, Onyxia's Lair or the open world, plus crafted items and quest rewards;
   items with no source listed (custom, later-phase quest and PvP rewards) only when a phase-1, launch or pre-raid community preset
   uses them (item level 70 at most, except the phase-1 class quest rewards in `PHASE1_QUEST`: the hunter's Molten Core bow and stave);
   no Blackwing Lair, Zul'Gurub, Ahn'Qiraj or Naxxramas, no world-boss drops (Azuregos, Kazzak and the Dragons of Nightmare came in
   phase 2 and later) or Scourge Invasion bosses (`EVENT_NPCS`), no legendaries, no crafted items made from later raids' materials
   (`LATER_PREFIXES`: Zul'Gurub's Bloodvine and hides, Ahn'Qiraj's Cenarion recipes and obsidian, Naxxramas's frost sets) (the item
   database's own `phase` field puts Ahn'Qiraj in phase 1, so the source decides). The class must be allowed (classAllowlist), armor no heavier
   than the class wears at 60, weapons of a type the class's presets use, in the same weapon setup as the current set (two-hander,
   dual wield, one-hander + off-hand or shield, the same ranged or relic type).
2. Stat weights: the simulator's own (bench `statweights`, the entry's rotation and setting, the group's best build of ours);
   an item's value = its stats x weights, weapon DPS x the hand's DPS weight. Recomputed once on the new set (hit caps move).
3. Per slot the best item by that value (two variants: every slot, and every slot but the current set pieces and items with an
   on-use or proc effect, which stat weights cannot value); trinkets are raced in the simulator (since 2026-10-22 every trinket of the
   pool the class may wear, each alone first, then every pair of the best seven: `screen_trinkets`; before, the class's preset
   trinkets in pairs), and relics (idol, libram, totem) stay.
4. Race: the current set and both variants on each entry's best build (seed 1), the leader confirmed on seed 2 with more iterations;
   a new set is kept only when it wins by more than --min-gain on the average of the group's entries. A current item outside the pool
   never competes or stays as a set piece, and a current set holding one does not race (fixed 2026-10-01: the 2026-09-30 sets kept the
   current items of slots where nothing beat them and every current set piece, so the hunter and Retribution sets carried Zul'Gurub's
   Bloodvine pieces and Enhancement Sulfuras).
**The port to wowsims/forever** (2026-10-22, `_reference/sim-port.md`): the item database is the official clone's (db.json and
leftover_db.json, which come from Forever's game files and lack 2,180 of the fork's items: the Molten Core tier sets, Hand of Justice,
Blackhand's Breadth ...); the Stat enum is read from its proto/common.proto (`stat_enum`: one hit, crit and haste rating since then);
the presets that vet sourceless items and name the class's weapon types are the official repository's plus the fork's, vendored under
`raidsim/presets/elliotwood-b7083fa/` (`preset_files`, `load_vetted`); a current item the database lacks is re-filled by its shape (the
fork's record of it, `legacy_item`), an empty armor or jewelry slot is filled and an empty relic slot of a relic class gets a relic
(`class_picker`, shared with gear_tiers.py); enchants the database lacks are dropped (`drop_missing_enchants`).
Enchants stay as the current set has them. Tanks keep their sets (their ranking is relative to their own hand draft); healers are
not in the simulator. Writes `raidsim/gear_sets/forever/<group>.p1opt.gear.json` and a record `raidsim/gear-opt.json`; --apply points
the group's specs.json entries at the new sets (with `gear_note`).
"""
import argparse
import datetime
import importlib.util
import itertools
import json
import pathlib
import re
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[2]
sys.path[:0] = [str(ROOT / "_reference/data"), str(HERE)]
import paths  # noqa: E402
import fill_enchants as FE  # noqa: E402

_s = importlib.util.spec_from_file_location("aplopt", HERE / "apl_opt.py")
A = importlib.util.module_from_spec(_s)
_s.loader.exec_module(A)
R = A.R
OUT = HERE / "gear-opt.json"
SETS = HERE / "gear_sets" / "forever"
TODAY = datetime.date.today().isoformat()

RAID_OK = {"Molten Core", "Onyxia's Lair"}
RAID_NO = {"Blackwing Lair", "Zul'Gurub", "Ahn'Qiraj", "Ruins of Ahn'Qiraj", "Naxxramas", "Temple of Ahn'Qiraj"}
SOURCELESS_MAX_ILVL = 70
WORLD_BOSSES = {6109, 12397, 14887, 14888, 14889, 14890}
# the Scourge Invasion's bosses (Sever, Balzaphon, Lady Falther'ess, Revanchion, Scorn, Lord Blackwood): an event of Classic's last phase that
# no community launch or phase-1 preset uses (2026-10-02: the Staff of Balzaphon had entered the Balance druid's pre-BiS set)
EVENT_NPCS = {14682, 14684, 14686, 14690, 14693, 14695}
ARMOR_MAX = {"warrior": 4, "paladin": 4, "hunter": 3, "shaman": 3, "rogue": 2, "druid": 2, "mage": 1, "priest": 1, "warlock": 1}
CLASS_ID = {"warrior": 1, "paladin": 2, "hunter": 3, "rogue": 4, "priest": 5, "shaman": 7, "mage": 8, "warlock": 9, "druid": 11}
SLOT_TYPE = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 11, 12, 12, 13, 13, 14]   # ItemSlot index -> ItemType
RELIC_TYPE = {"druid": 6, "paladin": 7, "shaman": 8}
SAME_WEAPON_TYPE = {"rogue"}   # classes whose weapon slots keep the current (or missing) item's weapon type (class_picker.fits)   # RangedWeaponType of the class's relic (idol, libram, totem)
STAT = {}   # Stat enum index -> name (load_db fills it from the simulator's proto/common.proto)


def stat_enum(repo):
    """{index: name} of the simulator's Stat enum, read from its proto/common.proto (2026-10-22, the port to wowsims/forever: the official
    enum merged melee and spell hit, crit and haste into StatHitRating 17, StatCritRating 18, StatHasteRating 19 and renumbered everything
    after Spirit; the fork's numbering had been written into this tool, gear_tiers.py and tank_gear.py). Item stats in db.json and an
    enchant's stats array use these indices; the bench's `statweights` mode returns the names."""
    text = (pathlib.Path(repo) / "proto" / "common.proto").read_text(encoding="utf-8")
    body = re.search(r"enum Stat \{(.*?)\n\}", text, re.S).group(1)
    return {int(v): k for k, v in re.findall(r"^\s*(Stat\w+)\s*=\s*(\d+);", body, re.M)}


def stat_names(repo):
    """The Stat enum as a list (index -> name)."""
    e = stat_enum(repo)
    return [e.get(i, f"Stat{i}") for i in range(max(e) + 1)]


def load_db(repo):
    """The simulator's item database: assets/database/db.json plus leftover_db.json (the official loader merges both, loader.go; the
    leftover file holds 1,186 common-quality items, none in any pool). Fills STAT from the clone's proto."""
    d = pathlib.Path(repo) / "assets" / "database"
    db = json.load(open(d / "db.json", encoding="utf-8"))
    items = {i["id"]: i for i in db["items"]}
    if (d / "leftover_db.json").exists():
        for i in json.load(open(d / "leftover_db.json", encoding="utf-8")).get("items", []):
            items.setdefault(i["id"], i)
    zones = {z["id"]: z["name"] for z in db["zones"]}
    STAT.clear()
    STAT.update(stat_enum(repo))
    return items, zones


def enchant_db(repo):
    """{effect id: [enchant, ...]} of the simulator's database (one effect id can serve several slots)."""
    by = {}
    for e in json.load(open(pathlib.Path(repo) / "assets" / "database" / "db.json", encoding="utf-8"))["enchants"]:
        by.setdefault(e["effectId"], []).append(e)
    return by


# The ElliotWood/Forever fork's database (archived clone, 2026-10-18): only to read the shape (item type, hand, weapon and ranged type)
# of a current item the official database lacks, so its slot is re-filled with an item of the same weapon setup (a missing two-hander
# must not turn into a one-hander). Never a candidate; absent on machines without the archive (the slot is then treated as empty).
LEGACY_DB = pathlib.Path.home() / ".wow-forever-tools" / "forever-repo" / "assets" / "database" / "db.json"
_LEGACY = {}


def legacy_item(iid):
    if not _LEGACY and LEGACY_DB.exists():
        _LEGACY.update({i["id"]: {k: i.get(k) for k in ("id", "name", "type", "handType", "weaponType", "rangedWeaponType", "armorType")}
                        for i in json.load(open(LEGACY_DB, encoding="utf-8"))["items"]})
        _LEGACY.setdefault(0, None)
    return _LEGACY.get(iid)


# The fork's gear presets (every ui/specs/*/*/gear_sets file at b7083fa, vendored 2026-10-22: the community's phase-0/1, launch and
# pre-raid picks that vet sourceless items, name the class's weapon types and trinkets) next to the official repository's own presets.
VENDORED_PRESETS = HERE / "presets" / "elliotwood-b7083fa" / "ui" / "specs"


def preset_files(repo, cls="*"):
    return sorted(list((pathlib.Path(repo) / "ui/specs").glob(f"{cls}/*/gear_sets/*.gear.json")) + list(VENDORED_PRESETS.glob(f"{cls}/*/gear_sets/*.gear.json")))


_EDB = {}


def drop_missing_enchants(items, repo):
    """Remove from a gear list the enchants the simulator's database lacks (the bench would drop them); returns them."""
    if not _EDB:
        _EDB.update(enchant_db(repo))
    out = []
    for x in items:
        if x and x.get("enchant") and x["enchant"] not in _EDB:
            out.append(x.pop("enchant"))
    return out


def item_name(db, iid):
    """An item's name; one the database lacks by the fork's record, marked (records of the port, 2026-10-22)."""
    if not iid:
        return None
    if iid in db:
        return db[iid]["name"]
    old = legacy_item(iid)
    return f"{old['name'] if old else iid} (not in the database)"


def missing_in(items, db, edb=None):
    """Items (and enchants, given the enchant database) of a gear list the simulator's database lacks: ["item:<id>", "enchant:<id>"]
    (the bench's `missing_gear` wording)."""
    out = []
    for x in items:
        if x and x.get("id") and x["id"] not in db:
            out.append(f"item:{x['id']}")
        if edb is not None and x and x.get("enchant") and x["enchant"] not in edb:
            out.append(f"enchant:{x['enchant']}")
    return out


# crafted items made from later raids' materials or later reputations (our list, 2026-10-01; the database has the recipe, not its
# materials): Zul'Gurub's Bloodvine and hides, Ahn'Qiraj's Cenarion Circle recipes and obsidian, Naxxramas's frost-resistance sets
LATER_PREFIXES = ("Bloodvine", "Blood Tiger", "Primal Batskin", "Bloodsoul", "Darksoul", "Dreamscale", "Bramblewood", "Ironvine", "Sylvan",
                  "Gaea's Embrace", "Sandstalker", "Spitfire", "Glacial", "Icebane", "Icy Scale", "Polar", "Heavy Obsidian", "Light Obsidian",
                  "Jagged Obsidian", "Obsidian Mail", "Thick Obsidian", "Black Grasp of the Destroyer")
# phase-1 class quest rewards the database lists without a source, above the sourceless item-level cap: the hunter's Molten Core quest
# (Ancient Petrified Leaf from Majordomo's cache, 2026-10-01); every raiding hunter gets one, so they belong in a phase-1 set
PHASE1_QUEST = {"Rhok'delar, Longbow of the Ancient Keepers", "Lok'delar, Stave of the Ancient Keepers"}


def unique_keys(it):
    """What an item uses up of the set's unique-equipped limits (audit 2026-10-18 row 50): its id when it is unique-equipped, its
    `limitCategory` when it has one (one item per category: the Signet Rings of the Bronze Dragonflight 21202/21207/234020/234439 share
    475, Ferocious Watcher's Signet 275981 is 710; the fork's bulk generator allows one per category). Same-id unique checks alone let
    seven pre-BiS sets wear two rings of one group."""
    if not it:
        return set()
    out = {("id", it["id"])} if it.get("unique") else set()
    if it.get("limitCategory"):
        out.add(("cat", it["limitCategory"]))
    return out


def pair_ok(db, pair):
    """A trinket pair one character can wear: not the same item twice, no shared unique id or limit category."""
    a, b = (db.get(x) for x in pair)
    return pair[0] != pair[1] and not (unique_keys(a) & unique_keys(b))


def later_craft(it):
    srcs = it.get("sources") or []
    return bool(srcs) and all(s.get("crafted") for s in srcs) and it.get("name", "").startswith(LATER_PREFIXES)


# Items whose database values look like errors (2026-10-15 page audit): kept out of every gear pool.
SUSPECT_ITEMS = {
    2816: "Death Speaker Scepter (item level 33): +68 healing and +28 Shadow damage in the fork's database (2ce8265), against +11 and +7 in "
          "Classic 1.12 (cmangos spells 7679, 7708); the only item level 33 item with that much; every healer set and the Shadow priest's took it",
    # the 2026-10-15 scan of every item with Classic spell stats (975): spell damage or healing at least twice Classic's and 12 more
    12260: "Searing Golden Blade (item level 39): +39 Fire damage against Classic's +10 (in the Fire and Frostfire pre-BiS sets)",
    7757: "Windweaver Staff (item level 37): +51 Nature damage against Classic's +14 (in the Balance pre-BiS set)",
    15109: "Staff of Soran'ruk (item level 25): +68 school damage against Classic's +18",
    1484: "Witching Stave (item level 22): +27 school damage against Classic's +11",
    15106: "Staff of Dar'Orahil (item level 40): +39 school damage against Classic's +19",
    15105: "Staff of Noh'Orahil (item level 40): +39 school damage against Classic's +19",
    10020: "Stormcloth Vest (item level 45): +58 healing against Classic's +29",
}


# Items the database lists no source for but that are known to be on sale in phase 1 (2026-10-15, from the MythicSim comparison:
# _reference/mythicsim-comparison.md): treated as sourced in both tiers, and trinkets among them join every class's trinket candidates.
VENDOR_ITEMS = {
    272437: "Adaptive Combat Assistant (trinket, +20 Expertise; new in Forever): \"This item can be purchased in Stranglethorn Vale\" "
            "(wowhead.com/forever/item=272437, 2026-10-15; vendor Pix Xizzix, Booty Bay, 125 Tarnished Undermine Reals). Tooltip "
            "(nether.wowhead.com/forever/tooltip/item/272437, 2026-10-16): \"Equip: Reduces chance to be Dodged or Parried by 2.0%.\" \"Use: "
            "Absorbs 450 damage for 15 sec. If this shield expires before 15 sec, 90 to 110 Nature damage will be dealt to all enemies in "
            "melee range.\" (1 min 30 s): a shield, nothing for a damage dealer the boss does not hit; neither the fork nor MythicSim "
            "simulates it",
}


def in_pool(it, zones):
    if it.get("quality", 0) >= 5 or it.get("quality", 0) < 2 or later_craft(it) or it.get("id") in SUSPECT_ITEMS:
        return False
    so = it.get("scalingOptions", {}).get("0", {})
    zs = {zones.get(s.get("drop", {}).get("zoneId")) for s in it.get("sources", []) if s.get("drop")}
    zs.discard(None)
    if zs & RAID_NO and not zs - RAID_NO:
        return False
    npcs = {s.get("drop", {}).get("npcId") for s in it.get("sources", []) if s.get("drop")}
    if npcs and npcs <= WORLD_BOSSES | EVENT_NPCS:   # Classic phase 2 and later (Azuregos, Kazzak, the Dragons of Nightmare; the Scourge Invasion)
        return False
    if it["id"] in VENDOR_ITEMS:
        return True
    if not it.get("sources"):   # no source listed (custom, later-phase quest or PvP rewards): only items a phase-1 community preset uses
        return it["id"] in VETTED and (so.get("ilvl", 0) <= SOURCELESS_MAX_ILVL or it.get("name") in PHASE1_QUEST)
    return True


VETTED = set()   # item ids in the simulator's phase-0/1, launch and pre-raid presets (every class)


def load_vetted(repo, db):
    """VETTED from the presets (preset_files). The official repository's presets (2026-10-22) do not follow Classic's phases in their names
    (its mage "p1Arcane" set is Naxxramas gear, the Balance "p1" set Ahn'Qiraj's Genesis), so one of them vets only when none of its
    items is above SOURCELESS_MAX_ILVL; the fork's vendored presets as before (every name but p2 / phase_2)."""
    for p in preset_files(repo):
        if "p2" in p.name or "phase_2" in p.name:
            continue
        ids = [x["id"] for x in json.load(open(p, encoding="utf-8")).get("items", []) if x and x.get("id")]
        if VENDORED_PRESETS not in p.parents and any(db.get(i, {}).get("scalingOptions", {}).get("0", {}).get("ilvl", 0) > SOURCELESS_MAX_ILVL
                                                      for i in ids):
            continue
        VETTED.update(ids)


def value(it, w, slot):
    so = it.get("scalingOptions", {}).get("0", {})
    v = sum(w.get(STAT.get(int(k)), 0.0) * x for k, x in so.get("stats", {}).items())
    if it.get("type") in (13, 14) and so.get("weaponDamageMax") and it.get("weaponSpeed"):
        dps = (so["weaponDamageMin"] + so["weaponDamageMax"]) / 2 / it["weaponSpeed"]
        key = {14: "PseudoStatMainHandDps", 15: "PseudoStatOffHandDps", 16: "PseudoStatRangedDps"}.get(slot)
        v += w.get(key, 0.0) * dps
    return v


def class_picker(repo, cls, db, pool):
    """The per-slot step both gear tools share (gear_tiers.optimize_set too, since 2026-10-22): (seen, trinkets, greedy).
    `seen`: item ids of the class's presets (the official repository's, the fork's vendored ones, our sets), which name its weapon types,
    ranged types, relics and trinkets; `trinkets`: those trinkets in the pool, plus the known vendor trinkets; `greedy(items, w,
    keep_special)`: per slot the item worth most by the weights `w` in the pool (`pool(item)`), the current item only when the pool
    admits it and the set does not already use up its unique limit; trinkets left for the race; relics kept; a current item the
    database lacks is re-filled by its shape (legacy_item); an empty armor or jewelry slot is filled, an empty weapon or ranged slot
    stays empty."""
    presets = preset_files(repo, cls) + list(SETS.glob(f"{cls}*.gear.json"))
    seen = [x.get("id") for p in presets for x in json.load(open(p, encoding="utf-8")).get("items", []) if x and x.get("id")]
    # weapon and ranged types the presets use (an item the official database lacks still names its type, by the fork's record of it)
    shapes = [db.get(i) or legacy_item(i) for i in seen]
    wtypes = {x.get("weaponType") for x in shapes if x and x.get("type") == 13}
    rtypes = {x.get("rangedWeaponType") for x in shapes if x and x.get("type") == 14}

    def class_ok(it):
        return not (it.get("classAllowlist") and CLASS_ID[cls] not in it["classAllowlist"])

    # trinket candidates: every trinket of the pool the class may wear (2026-10-22). Until the port they were the class's preset trinkets
    # plus the known vendor ones, but the official database lacks most of them (the hunter kept one: Adaptive Combat Assistant); the
    # single-trinket screen (screen_trinkets) picks the pairs to race.
    trinkets = sorted(i for i, it in db.items() if it.get("type") == 12 and pool(it) and class_ok(it))

    def fits(it, slot, curit):
        if it.get("type") != SLOT_TYPE[slot] or not pool(it):
            return False
        if not class_ok(it):
            return False
        if it.get("armorType", 0) > ARMOR_MAX[cls]:
            return False
        if it.get("randomSuffixOptions") or not it.get("scalingOptions", {}).get("0", {}).get("stats") and it.get("type") not in (13, 14):
            return False
        if SLOT_TYPE[slot] == 13:
            if it.get("weaponType") not in wtypes:
                return False
            # a rogue's weapons name its rotation (daggers for Backstab, Ambush and Mutilate; swords, maces): the same weapon type
            # (2026-10-22: the daggers set's missing Perdition's Blade was re-filled with Greenhammer, a mace)
            if cls in SAME_WEAPON_TYPE and curit and curit.get("weaponType") and it.get("weaponType") != curit.get("weaponType"):
                return False
            ch = curit.get("handType") if curit else None
            if slot == 14 and (ch == 4) != (it.get("handType") == 4):
                return False
            if slot == 15:
                if not curit or (it.get("weaponType") in (5, 7)) != (curit.get("weaponType") in (5, 7)):
                    return False
                if (curit.get("weaponType") in (5, 7)) and it.get("weaponType") != curit.get("weaponType"):
                    return False
                if it.get("handType") in (1, 4):
                    return False
            if slot == 14 and it.get("handType") == 3:
                return False
        if SLOT_TYPE[slot] == 14:
            if not curit or it.get("rangedWeaponType") != curit.get("rangedWeaponType") or it.get("rangedWeaponType") not in rtypes:
                return False
        return True

    def relic_for(shape, w, ukeys):
        """A relic for a missing one of its type (idol, libram, totem, sigil): the class's preset relics in the pool first (their
        effects are what the community picked them for; ties by the weights, then item level), else any in the pool by the weights."""
        rt = shape.get("rangedWeaponType")
        ok = [db[i] for i in dict.fromkeys(seen) if i in db and db[i].get("rangedWeaponType") == rt and pool(db[i]) and class_ok(db[i])
              and not (unique_keys(db[i]) & ukeys)]
        if not ok:
            ok = [it for it in db.values() if it.get("type") == 14 and it.get("rangedWeaponType") == rt and pool(it) and class_ok(it)]
        key = lambda it: (value(it, w, 16), it.get("scalingOptions", {}).get("0", {}).get("ilvl", 0))  # noqa: E731
        return {"id": max(ok, key=key)["id"]} if ok else None

    def greedy(items, w, keep_special):
        new = [dict(x) if x else {} for x in items] + [{}] * max(0, 17 - len(items))
        used, ukeys = set(), set()   # ids held, unique ids and limit categories held (unique_keys)

        def hold(iid):
            used.add(iid)
            ukeys.update(unique_keys(db.get(iid)))

        for slot in range(17):
            curx = new[slot]
            curit = db.get(curx.get("id")) if curx.get("id") else None
            # a current item the simulator's database lacks (the port to wowsims/forever, 2026-10-22): the slot is re-filled with an item
            # of the same shape (the fork's record of it: weapon setup, ranged or relic type); the missing item never stays or competes
            shape = curit or (legacy_item(curx["id"]) if curx.get("id") else None)
            if not shape and slot == 16 and cls in RELIC_TYPE:   # an empty relic slot of a class that wears one (the official bear preset)
                shape = {"type": 14, "rangedWeaponType": RELIC_TYPE[cls]}
            if curx.get("id") and not curit:
                new[slot] = curx = {}
            if SLOT_TYPE[slot] == 12:
                if curit:
                    hold(curit["id"])
                continue   # trinkets are raced
            if shape and shape.get("rangedWeaponType", 0) in (6, 7, 8, 9):
                if curit:
                    hold(curit["id"])
                    continue   # relics stay
                new[slot] = relic_for(shape, w, ukeys) or {}
                if new[slot]:
                    hold(new[slot]["id"])
                continue
            if slot == 15 and new[14].get("id") and db.get(new[14]["id"], {}).get("handType") == 4:
                new[15] = {}
                continue
            # never keep an item outside the pool, or one whose unique id or limit category the set already holds
            allowed = curit is not None and pool(curit) and not (unique_keys(curit) & ukeys)
            if keep_special and allowed and (curit.get("setName") or curit.get("itemEffects")):
                hold(curit["id"])
                continue
            if not shape and slot >= 14:   # an empty weapon or ranged slot stays empty (no setup to follow); armor and jewelry slots fill
                continue
            # a unique-equipped item (2026-10-06: the same unique ring twice) or a second item of one limit category (2026-10-18 audit
            # row 50): not twice
            cands = [it for it in db.values() if fits(it, slot, shape) and it["id"] not in used and not (unique_keys(it) & ukeys)]
            if allowed:
                cands.append(curit)
            best = max(cands, key=lambda it: value(it, w, slot)) if cands else (curit if allowed else None)
            if best is None:
                new[slot] = {}
                continue
            if best["id"] != curx.get("id"):
                ench = curx.get("enchant")
                new[slot] = {"id": best["id"], **({"enchant": ench} if ench else {})}
            hold(new[slot].get("id"))
        return new

    def relic_candidates(items):
        """When the set's relic slot was re-filled (the old relic missing from the database, or no relic): the relics of that type in
        the class's presets and the pool, for race_relics; else []. Relic effects are what decides (Idol of Ferocity for a cat, Idol
        of the Moon for Balance) and stat weights cannot see them."""
        x = items[16] if len(items) > 16 else {}
        old = db.get(x.get("id")) if x and x.get("id") else None
        if old:
            return []
        shape = (legacy_item(x["id"]) if x and x.get("id") else None) or ({"rangedWeaponType": RELIC_TYPE[cls]} if cls in RELIC_TYPE else None)
        if not shape or shape.get("rangedWeaponType", 0) not in (6, 7, 8, 9):
            return []
        rt = shape["rangedWeaponType"]
        return [i for i in dict.fromkeys(seen) if i in db and db[i].get("rangedWeaponType") == rt and pool(db[i]) and class_ok(db[i])]

    greedy.relic_candidates = relic_candidates
    return seen, trinkets, greedy


def race_relics(cands, sets, race, its):
    """The relic slot of every set in `sets` ({name: items}) set to the candidate that races best in the first set (seed 1);
    returns (the relic id or None, {id: score})."""
    if len(cands) < 2:
        if cands:
            for v in sets.values():
                v[16] = {"id": cands[0]}
        return (cands[0] if cands else None), {}
    base = next(iter(sets.values()))
    trial = {}
    for i in cands:
        x = [dict(y) if y else {} for y in base]
        x[16] = {"id": i}
        trial[str(i)] = x
    r = race(trial, its, 1)
    best = max(cands, key=lambda i: r[str(i)])
    for v in sets.values():
        v[16] = {"id": best}
    return best, {str(i): round(r[str(i)], 4) for i in cands}


TRINKET_SCREEN = 7   # trinkets kept from the single-trinket screen; their pairs are raced (21 pairs)


def screen_trinkets(db, trinkets, items, race, its, keep=TRINKET_SCREEN):
    """Each candidate trinket alone (the other trinket slot empty) in `items`, raced on seed 1 (`race(sets, its, seed)` -> {name: score
    relative to the first set}); returns (the best `keep` ids, {name: score}). 2026-10-22: the pool's trinkets replace the class's
    preset trinkets as candidates (class_picker), too many to race in pairs (about 50: 1,225 pairs)."""
    if len(trinkets) <= 2:
        return list(trinkets), {}
    sets = {}
    for i in trinkets:
        x = [dict(y) if y else {} for y in items]
        x[12], x[13] = {"id": i}, {}
        sets[str(i)] = x
    r = race(sets, its, 1)
    top = sorted(trinkets, key=lambda i: -r[str(i)])[:keep]
    return top, {db[i]["name"] + f" ({i})": round(r[str(i)], 4) for i in sorted(trinkets, key=lambda i: -r[str(i)])}


def bench_cfg(entry, repo, builds, its, seed, where, **extra):
    return {"class": entry["sim_class"], "race": entry.get("race", "RaceHuman"), "gear": R.sim_path(entry["gear"]), "apl": str(R.apl_path(entry, repo, where)),
            "spec": entry.get("spec", {}), **R.setting_cfg(entry, where), "profession1": entry.get("profession1", "Engineering"),
            "profession2": entry.get("profession2", ""), "distanceFromTarget": entry.get("distance", 5), "inFrontOfTarget": entry.get("in_front", False),
            "reactionTimeMs": 200, "iterations": its, "duration": R.FIGHT, "seed": R.sim_seed(seed), "isTank": entry.get("tank", False),
            "builds": builds, **extra}


def run_bench(repo, cfg, tag):
    p = repo / "bench" / f"gearopt-{tag}.json"
    p.parent.mkdir(exist_ok=True)
    p.write_text(json.dumps(cfg), encoding="utf-8")
    r = subprocess.run([str(repo / "foreverbench"), "--config", str(p), "--root", str(repo)], capture_output=True, text=True)
    if r.returncode:
        raise SystemExit(f"bench failed: {r.stderr[-800:]}")
    return {x["label"]: x for x in (json.loads(ln) for ln in r.stdout.splitlines() if ln.startswith("{"))}


def best_label(cls, spec, entry):
    """The entry's best build of ours in its last race (label, allocation)."""
    data = {b["id"]: b for b in json.load(open(paths.builds_json("forever", cls), encoding="utf-8"))["builds"]}
    f = paths.raidsim_dir(cls) / f"{spec}.json"
    rows = json.load(open(f, encoding="utf-8"))["results"] if f.exists() else []
    ours = [r for r in rows if r["label"] in data and r.get("dps")]
    if ours:
        lab = max(ours, key=lambda r: r["dps"])["label"]
    else:
        lab = next((b for b in entry.get("builds", []) if b in data), None)
    return (lab, R.alloc_of(data[lab])) if lab else (None, None)


def groups():
    """{gear path: [(class, entry name)]} for damage entries (tanks keep their sets)."""
    out = {}
    for cls, es in R.SPECS.items():
        if cls.startswith("_"):
            continue
        for name, e in es.items():
            if isinstance(e, dict) and e.get("gear") and not e.get("tank"):
                out.setdefault(e["gear"], []).append((cls, name))
    return out


def optimize(gear, members, repo, db, zones, a):
    cls = members[0][0]
    evals = []   # (entry name, entry, where, talents string)
    for c, name in members:
        e = R.SPECS[c][name]
        lab, al = best_label(c, name, e)
        if lab:
            evals.append((name, e, R.setting(e), R.talents_string(R.load_trees(repo, c), al), lab))
    if not evals:
        return None
    main = evals[0]
    cur = json.load(open(R.sim_path(gear) if pathlib.Path(R.sim_path(gear)).is_absolute() else repo / R.sim_path(gear), encoding="utf-8"))
    cur_items = cur["items"] + [{}] * (17 - len(cur["items"]))

    def weights(items):
        cfg = bench_cfg(main[1], repo, [{"label": "w", "talents": main[3], "gear_json": {"items": items}}], a.weight_iterations, 1, main[2], statweights=True)
        row = run_bench(repo, cfg, f"w-{cls}")["w"]
        if row.get("error"):
            raise SystemExit(f"stat weights failed for {cls}: {row['error']}")
        return row["weights"]

    seen, trinkets, greedy = class_picker(repo, cls, db, lambda it: in_pool(it, zones))

    def with_trinkets(items, pair):
        x = [dict(i) for i in items]
        x[12], x[13] = {"id": pair[0]}, {"id": pair[1]}
        return x

    def race(sets, its, seed):
        """{set name: average ratio to the first set over the group's entries}."""
        out = {k: [] for k in sets}
        for name, e, where, tal, lab in evals:
            e2 = dict(e, gear=gear)
            rows = run_bench(repo, bench_cfg(e2, repo, [{"label": k, "talents": tal, "gear_json": {"items": v}} for k, v in sets.items()], its, seed, where), f"r-{cls}")
            ref = rows[next(iter(sets))]
            for k in sets:
                out[k].append((rows[k].get("dps") or 0) / (ref.get("dps") or 1))
        return {k: sum(v) / len(v) for k, v in out.items()}

    w = weights([x if x.get("id") in db else {} for x in cur_items])   # (the bench would drop a missing item itself)
    v1, v2 = greedy(cur_items, w, False), greedy(cur_items, w, True)
    w = weights(v1)   # the hit caps move with the new gear: weigh again on it
    v1, v2 = greedy(v1, w, False), greedy(v2, w, True)
    # trinkets: the pool's trinkets screened one at a time, then every pair of the best (screen_trinkets), raced with the first variant
    top, screen = screen_trinkets(db, trinkets, v1, race, a.iterations)
    pairs = [p for p in itertools.combinations(top, 2) if pair_ok(db, p)][: a.max_pairs]
    cur_pair = (cur_items[12].get("id"), cur_items[13].get("id"))
    # the current pair competes only when one character can wear it (audit 2026-10-18 row 50) and the database has both (2026-10-22)
    cur_ok = all(i in db for i in cur_pair if i)
    tsets = ({"cur": v1} if cur_ok and (not all(cur_pair) or pair_ok(db, cur_pair) or not pairs) else {}) | {f"t{i}": with_trinkets(v1, p) for i, p in enumerate(pairs)}
    tr = race(tsets, a.iterations, 1)
    tbest = max(tr, key=tr.get)
    pair = cur_pair if tbest == "cur" else pairs[int(tbest[1:])]
    v1, v2 = with_trinkets(v1, pair), with_trinkets(v2, pair)
    vs = {"v1": v1, "v2": v2}
    relic, relic_race = race_relics(greedy.relic_candidates(cur_items), vs, race, a.iterations)   # a re-filled relic slot (2026-10-22)
    v1, v2 = vs["v1"], vs["v2"]
    in_tier = all(x["id"] in db and in_pool(db[x["id"]], zones) for x in cur_items if x.get("id"))   # a missing item is out of the pool
    sets = ({"current": cur_items} if in_tier else {}) | {"all-slots": v1, "keep-sets-and-effects": v2}
    r1 = race(sets, a.iterations, 1)
    lead = max(r1, key=r1.get)
    ref = "current" if in_tier else ("keep-sets-and-effects" if lead == "all-slots" else "all-slots")
    r2 = race({ref: sets[ref], lead: sets[lead]}, a.confirm, 2) if lead != ref else {ref: 1.0}
    gain = r2.get(lead, 1.0) - 1
    if not in_tier:   # the current set is out of the pool: the better variant replaces it whatever the margin
        lead = lead if gain > 0 else ref
        gain = max(gain, 0.0)
    keep = lead != "current" and (gain > a.min_gain or not in_tier)
    ilvl = lambda items: sum(db[x["id"]]["scalingOptions"]["0"].get("ilvl", 0) for x in items if x.get("id") in db) / max(1, sum(1 for x in items if x.get("id") in db))  # noqa: E731
    return {"gear": gear, "members": [f"{c}/{n}" for c, n in members], "evaluated_on": [f"{n}: {lab}" for n, _, _, _, lab in evals],
            "weights": {k: round(v, 4) for k, v in w.items() if abs(v) > 1e-6}, "trinkets": [db[i]["name"] for i in pair if i in db],
            "trinket_screen": screen, **({"relic_race": relic_race} if relic_race else {}),
            "race_seed1": r1, "confirm_seed2": r2, "chosen": lead if keep else "current", "gain": gain if keep else 0.0,
            "current_in_pool": in_tier,
            "ilvl_before": round(ilvl([x for x in cur_items if x]), 1), "ilvl_after": round(ilvl([x for x in (sets[lead] if keep else cur_items) if x]), 1),
            "items": [x for x in (sets[lead] if keep else cur_items)], "changed": [
                {"slot": s, "from": item_name(db, cur_items[s].get("id")), "to": item_name(db, sets[lead][s].get("id"))}
                for s in range(17) if keep and cur_items[s].get("id") != sets[lead][s].get("id")]}


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("classes", nargs="*")
    ap.add_argument("--iterations", type=int, default=3000)
    ap.add_argument("--confirm", type=int, default=12000)
    ap.add_argument("--weight-iterations", type=int, default=3000)
    ap.add_argument("--min-gain", type=float, default=0.005)
    ap.add_argument("--max-pairs", type=int, default=28)
    ap.add_argument("--write", action="store_true")
    ap.add_argument("--fresh", action="store_true", help="redo groups already in the record")
    ap.add_argument("--apply", action="store_true", help="point specs.json entries at the kept sets")
    a = ap.parse_args()
    R.set_game("forever")
    repo = R.repo_path(argparse.Namespace(repo=None))
    db, zones = load_db(repo)
    load_vetted(repo, db)
    rec = json.load(open(OUT, encoding="utf-8")) if OUT.exists() else {}
    if not a.apply:
        for gear, members in sorted(groups().items()):
            if a.classes and members[0][0] not in a.classes:
                continue
            if gear in rec and not a.fresh:
                print(f"== {members[0][0]} {gear}: done ({rec[gear]['chosen']}, {rec[gear]['gain']:+.2%})", flush=True)
                continue
            print(f"== {members[0][0]} {gear} ({', '.join(n for _, n in members)})", flush=True)
            r = optimize(gear, members, repo, db, zones, a)
            if not r:
                print("  no raced build: skipped", flush=True)
                continue
            print(f"  item level {r['ilvl_before']} -> {r['ilvl_after']}; seed 1 " + ", ".join(f"{k} {v:.3f}" for k, v in r["race_seed1"].items())
                  + f"; kept {r['chosen']} ({r['gain']:+.2%} on seed 2); trinkets {', '.join(r['trinkets'])}", flush=True)
            for c in r["changed"]:
                print(f"    slot {c['slot']}: {c['from']} -> {c['to']}", flush=True)
            rec[gear] = dict(r, date=TODAY)
            if a.write:
                OUT.write_text(json.dumps(rec, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
        return
    # --apply: write the kept sets and point the entries at them (a text edit of specs.json keeps its hand layout)
    sp = HERE / "specs.json"
    text = sp.read_text(encoding="utf-8")
    SETS.mkdir(parents=True, exist_ok=True)
    for gear, r in rec.items():
        if r["chosen"] == "current" or f'"gear": "{gear}"' not in text:   # kept, or a record of a set no entry uses any more
            continue
        cls = r["members"][0].split("/")[0]
        if a.classes and cls not in a.classes:   # 2026-10-15: `--apply priest` had rewritten every class's set from the record
            continue
        gone = [x["id"] for x in r["items"] if x.get("id") and x["id"] not in db]
        if gone:   # 2026-10-06: a record of 2026-10-01 still held the removed Leafre ring (276765) and --apply wrote it into three sets
            print(f"{gear}: NOT applied, its record holds items the simulator no longer has ({gone}); run --write --fresh for it first")
            continue
        gp = pathlib.Path(gear)   # ui/specs/<class>/<spec>/gear_sets/<name>: the spec folder keeps sets of one class apart
        spec_dir = gp.parent.parent.name if gp.parent.name == "gear_sets" else "project"
        name = gp.name if gp.name.endswith(".p1opt.gear.json") else f"{cls}-{spec_dir}-{gp.name.split('.')[0]}.p1opt.gear.json"   # re-runs: in place
        items = [dict(x) for x in r["items"]]
        drop_missing_enchants(items, repo)
        tmpl = FE.role(name)
        if tmpl in FE.TEMPLATES:   # 2026-10-15: a record from before fill_enchants (2026-10-09) wrote sets without enchants (Retribution lost all of them)
            FE.fill(items, tmpl)
        (SETS / name).write_text(json.dumps({"items": items}, indent=1) + "\n", encoding="utf-8")
        new = f"_reference/data/raidsim/gear_sets/forever/{name}"
        text = text.replace(f'"gear": "{gear}"', f'"gear": "{new}"')
        print(f"{gear} -> {new} ({r['gain']:+.2%}, item level {r['ilvl_before']} -> {r['ilvl_after']})")
    sp.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
