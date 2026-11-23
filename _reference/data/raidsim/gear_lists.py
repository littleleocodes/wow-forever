"""The three gear lists (2026-11-22): True BiS, True Pre-BiS and Easy Pre-BiS, for items and for enchants and other modifiers.

The user, 2026-11-22, first-hand to the audit session, after a community Survival list beat our Pre-BiS set by 2.8%:
- "True BiS": "all obtainable items like PvP rewards, raids, dungeons, 0.5 quest chain, etc.";
- "True Pre-BiS": "everything that doesn't include raids";
- "Easy Pre-BiS": "things just like dungeons and quests and doesn't include recipes and using the AH";
- "As for enchants and gear modifiers it should work the same way."; "All BoE's should also count if you can buy off the AH";
  Alterac Valley is open; the Tier 0.5 chain works;
- "Molten Core is not in Forever right now. No raid is. And the only raids coming are the 3 you mentioned. So only use their loot tables
  for now" (The Barrow Deeps, Hyjal Summit, Onyxia's Lair, 2026-12-09).
The audit session's six readings, accepted by the user ("Yes I like it"): (1) raids are those three, world bosses are raids, content
not in the game stays out; (2) PvP rank gear in both true lists, labelled; (3) raid-material crafts and raid quest rewards are raid
items; (4) Easy = dungeon drops, one-time quest rewards (Alterac Valley's included), reputation to Honored; not crafts, the auction
house, Tier 0.5, Exalted or event-currency vendors; (5) Easy enchants = trainer-taught and quest modifiers; (6) one-faction items show
the other faction's alternative.

The internal keys stay the tiers' (gear_tiers, the records, the set files): "bis" = True BiS, "prebis" = True Pre-BiS, "dungeon" =
Easy Pre-BiS. ITEM_KINDS and ENCHANT_KINDS below are the rules: every source of an item (or an enchant) is one kind, an item is in a
list when one of its kinds is, and `--table` prints them as implemented.

    python _reference/data/raidsim/gear_lists.py --table [--counts]
"""
import argparse
import csv
import json
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[2]
sys.path[:0] = [str(HERE)]
import bind_types as BT  # noqa: E402

LISTS = ("bis", "prebis", "dungeon")
LABEL = {"bis": "True BiS", "prebis": "True Pre-BiS", "dungeon": "Easy Pre-BiS"}
RULES = "lists-2026-11-23"   # the rules a set was made under (written into each set's record; the pages label a set by it)
T, P, E = "bis", "prebis", "dungeon"
ALL3, TRUE2, BIS, NONE = frozenset((T, P, E)), frozenset((T, P)), frozenset((T,)), frozenset()

NEW_RAIDS = {"The Barrow Deeps", "Barrow Deeps", "Hyjal Summit"}   # no zone of theirs in the database at the pin of 2026-11-22
LATER_RAIDS = {"Blackwing Lair", "Zul'Gurub", "Ahn'Qiraj", "Ruins of Ahn'Qiraj", "Temple of Ahn'Qiraj", "Gates of Ahn'Qiraj", "Naxxramas"}
MC_ZONE, ONY_ZONE, MC_QUEST_ZONE, ONY_QUEST_ZONE = "Molten Core", "Onyxia's Lair", 2717, 2159
MC_MATS = {17010: "Fiery Core", 17011: "Lava Core", 17012: "Core Leather", 17203: "Sulfuron Ingot"}
ONY_MATS = {15410: "Scale of Onyxia"}
ONY_MADE = {"Onyxia Scale Cloak", "Onyxia Scale Breastplate"}   # gear_opt.PHASE1_RAID_MADE's Onyxia part; the rest is Molten Core's
# battlegrounds (the database's vendors and reputations; the user confirmed Alterac Valley, the database dates Warsong Gulch's and Arathi
# Basin's rewards phase 1, i.e. in the game now)
BG_VENDORS = {"Grunnda Wolfheart": "Alterac Valley", "Jekyll Flandring": "Alterac Valley", "Gaelden Hammersmith": "Alterac Valley",
              "Thanthaldis Snowgleam": "Alterac Valley", "Kelm Hargunth": "Warsong Gulch", "Illiyana Moonblaze": "Warsong Gulch",
              "Samuel Hawke": "Arathi Basin", "Rutherford Twing": "Arathi Basin"}
BG_FACTIONS = {729: "Alterac Valley", 730: "Alterac Valley", 889: "Warsong Gulch", 890: "Warsong Gulch", 509: "Arathi Basin",
               510: "Arathi Basin"}
HONOR_VENDORS = {"Mokvar", "Deliana", "Ironforge Guard", "Kor'kron Elite", "Sergeant Ba'sha", "Master Sergeant Biggins", "Officer Areyn",
                 "Sergeant Major Clate", "Lady Palanseer", "Lieutenant Jackspring", "Sergeant Thunderhorn"}
EVENT_VENDORS = {"Lhara": "the Darkmoon Faire"}
CLIENT_HONORED = 5   # ItemSparse MinReputation: 4 Friendly, 5 Honored, 6 Revered, 7 Exalted
QUEST_REVERED = 21000   # Classic's quest_template RequiredMinRepValue at Revered (3,000 Friendly, 9,000 Honored, 42,000 Exalted)
# Forever's raid materials (2026-11-23, the audit session from Wowhead's Forever pages; the client's tooltips): a craft whose client
# reagents hold one is a raid item (the accepted reading 3), True BiS from 2026-12-09. Only this reagent's tooltip names the new raids.
NEW_RAID_MATS = {274030: "Malleable Essence of Nature (disenchanted from Hyjal Summit and Barrow Deeps items)"}
# The user's answers (2026-11-23, first-hand to the audit session, which put the three questions):
# - "Yes, I don't consider Upper Blackrock Spire a raid. It's within the dungeon and quests realm": its bosses' drops and the quests whose
#   objective is inside it are in Easy Pre-BiS (the user's decision; the switch stays for the record);
UBRS_EASY = True
# - Warsong Gulch and Arathi Basin "Yes they are" open, with their reputation vendors: all three battlegrounds follow one rule (the audit
#   session's reading): rewards up to Honored in Easy (battleground_easy, marked PvP), Revered and Exalted in the True lists, a standing no
#   source gives out of Easy. True open, None as the database dates them (the True lists), False closed (no list);
BG_OPEN = {"Alterac Valley": True, "Warsong Gulch": True, "Arathi Basin": True}
# - which honor ranks and rank gear a player can have now: "Not sure". The rank gear the database dates phase 1 stays in both True lists,
#   marked PvP, with a non-PvP alternative (pvp_alternatives); no rank cap is guessed (the launch checklist asks).

STANDING_FROM = ("the standing, in this order: the client's MinReputation when set (empty on the Alterac Valley rewards that ask "
                 "Honored to Exalted), Classic's item_template RequiredReputationRank, else Classic's vendor condition (npc_vendor "
                 "condition_id, type 5: where the dump keeps the Warsong Gulch gates), the database's rep source, Wowhead's Forever "
                 "tooltip from the archive (bind_types.WOWHEAD_REP; nothing left to pull at this pin)")
# (kind, lists, what it is, where the fact comes from): items
ITEM_KINDS = [
    ("dungeon_drop_easy", ALL3, "a named creature's drop in a dungeon at 5% or more (our reading), Upper Blackrock Spire's bosses "
     "included (the user: \"I don't consider Upper Blackrock Spire a raid\"); the chance must be known (since 2026-11-23, the delegator's "
     "G13: the creature's own row, spawned or summoned, else the item's best row in the dungeon, a chest included)",
     "database drop (zone, creature); cmangos dungeon_loot.csv chance (drop_chance)"),
    ("dungeon_drop", TRUE2, "any other dungeon drop: trash, drops under 5% or of unknown chance (unknown_chances), a class quest's "
     "summon (CLASS_SUMMONS), a rare spawn (a creature a spawn pool can leave out, or one Classic ranks rare that the dump does not "
     "spawn outright or by an event script; ENCOUNTER_RARES aside), a contested spawn (CONTESTED_SPAWNS)",
     "database drop; cmangos dungeon_loot.csv rank and spawn"),
    ("world_drop", TRUE2, "a drop in the open world (one that binds when equipped sells on the auction house)", "database drop"),
    ("quest", ALL3, "a quest reward of the game now (Alterac Valley's included; Forever's own quests count)",
     "database quest; cmangos quests.csv zone"),
    ("quest_ubrs", TRUE2, "a quest whose objective is inside Upper Blackrock Spire, only if UBRS_EASY were off (the user put the Spire "
     "in Easy, so no item takes this kind)", "cmangos quest_geo.csv objectives, quest_item_sources.csv"),
    ("tier05", TRUE2, "Tier 0.5 (the level-58 chain: 10-player Upper Blackrock Spire, the vendors' gold), and the loot of the bosses its "
     "braziers and banner summon (T05_SUMMONS, T05_CHESTS; 2026-11-23, the delegator's G13)", "item set name (gear_tiers.T05_SETS); database drop"),
    ("craft", TRUE2, "a craft whose recipe and materials the game has now (from a trainer, a vendor, a drop or a reputation)",
     "database crafted; client SpellReagents 71037 (Classic's craft_spells.csv where the client has no row)"),
    ("rep_to_honored", ALL3, "a reputation reward at Friendly or Honored", STANDING_FROM),
    ("rep_above_honored", TRUE2, "a reputation reward at Revered or Exalted, or one whose standing no source gives", STANDING_FROM),
    ("battleground_easy", ALL3, "a battleground quartermaster's or reputation's reward that a source puts at Honored or below (Alterac "
     "Valley, Warsong Gulch, Arathi Basin: the user says all three are open), labelled PvP", "database soldBy / rep; " + STANDING_FROM),
    ("battleground", TRUE2, "any other battleground reward: Revered or Exalted, or a standing no source gives, labelled PvP",
     "database soldBy / rep; " + STANDING_FROM),
    ("bg_closed", NONE, "a battleground the user says is closed (none: BG_OPEN)", "BG_OPEN"),
    ("pvp", TRUE2, "honor rank gear the database dates phase 1, labelled PvP, each piece with a non-PvP alternative (the user is not "
     "sure which ranks a player can hold now; no rank cap is guessed)", "database pvp, honor vendors"),
    ("vendor", TRUE2, "a vendor's stock for gold or a currency", "database soldBy"),
    ("dungeon_currency", TRUE2, "a currency vendor's stock whose currency dungeon bosses drop (CURRENCY_VENDORS: Pix Xizzix in Booty Bay, "
     "Tarnished Undermine Reals from the bosses of Blackrock Depths, Blackrock Spire, Scholomance, Stratholme and the Temple of "
     "Atal'Hakkar); the True lists until the Reals a boss drops are known (the delegator, 2026-11-23)",
     "database soldBy; Wowhead Forever's vendor and currency pages, read by the delegator session 2026-11-23"),
    ("auction", TRUE2, "no source in the database, binds when equipped and Classic's world creatures drop it: the auction house",
     "bind type (client ItemSparse, else Classic item_template); cmangos mob_loot.csv"),
    ("vetted", TRUE2, "no source in the database, used by a launch or pre-raid preset of the simulator, item level 70 at most",
     "the simulator's presets"),
    ("onyxia", BIS, "Onyxia's Lair: her quest rewards (Dragonslayer's Signet, Onyxia Tooth Pendant, Onyxia Blood Talisman), her drops "
     "when the database lists them (none at this pin), crafts from Scale of Onyxia", "database quest / drop; cmangos reagents"),
    ("new_raid", BIS, "The Barrow Deeps and Hyjal Summit, from 2026-12-09: their drops (none in the database at this pin) and crafts "
     "from their materials (Malleable Essence of Nature: 97 Forever recipes, the Hyjal vendor's 72 item-level-61 patterns and 25 "
     "item-level-65 epics)", "database drop zone; client SpellReagents 71037; the reagent's tooltip"),
    ("molten_core", NONE, "Molten Core: its drops, its quest rewards (Rhok'delar, Lok'delar), crafts from its materials (Fiery Core, Lava "
     "Core, Core Leather, Sulfuron Ingot: Flarecore, Corehound, Molten, Fiery Chain, Dark Iron, Thorium Brotherhood's weapons)",
     "database drop zone / quest zone; cmangos reagents; gear_opt.PHASE1_RAID_MADE"),
    ("later_raid", NONE, "Blackwing Lair, Zul'Gurub, Ahn'Qiraj, Naxxramas: drops, quest rewards, crafts from their materials",
     "database zone; gear_opt.LATER_PREFIXES"),
    ("world_boss", NONE, "a world boss's drop (Azuregos, Kazzak, the Dragons of Nightmare): a raid, and none is in the game",
     "gear_opt.WORLD_BOSSES"),
    ("event", NONE, "events: the Scourge Invasion's bosses, the Darkmoon Faire's vendors, items the client ties to a holiday",
     "gear_opt.EVENT_NPCS; client RequiredHoliday"),
    ("later", NONE, "later content: the database's phase 2, a later reputation (Brood of Nozdormu), a later quest (Paragons of Power, "
     "A Collection of Heads), a raid's or Silithus's quest, a crafted-only item of item level 65+ no preset uses whose reagents the "
     "client does not give",
     "database phase; gear_opt.LATER_FACTIONS, LATER_QUESTS; gear_tiers.NO_QUEST_ZONES, CRAFTED_MAX_ILVL"),
]
ITEM_LISTS = {k: l for k, l, _, _ in ITEM_KINDS}
# enchants and modifiers (the same rules; the reading (5) for Easy)
ENCHANT_KINDS = [
    ("taught", ALL3, "a recipe a profession trainer teaches", "cmangos trainer_spells.csv, learn_spells.csv"),
    ("quest", ALL3, "a quest's modifier of the game now", "database quest"),
    ("vendor", TRUE2, "a formula or modifier a vendor sells", "database soldBy"),
    ("rep", TRUE2, "a reputation's formula or modifier (any standing)", "database rep"),
    ("drop", TRUE2, "a formula that drops in a dungeon or the open world", "database drop"),
    ("craft", TRUE2, "a crafted modifier (kits, scopes, spurs) not taught by a trainer", "database crafted"),
    ("vetted", TRUE2, "no source in the database, used by a pre-raid preset on that kind of item", "the simulator's presets"),
    ("onyxia", BIS, "a formula from Onyxia's Lair", "database drop zone"),
    ("molten_core", NONE, "Molten Core's formulas (Enchant Weapon - Spell Power 2504, - Healing Power 2505)", "database drop zone"),
    ("later", NONE, "later content (phase 2, Zul'Gurub, Naxxramas, Ahn'Qiraj's formulas: gear_tiers.ENCHANTS_OUT), a creature type's "
     "bonus (the bench's target is an Elemental), the held scope (gear_tiers.ENCHANTS_HELD)", "database phase and zone; our lists"),
    ("event", NONE, "a world boss's or an event's drop", "gear_opt.WORLD_BOSSES, EVENT_NPCS"),
]
ENCHANT_LISTS = {k: l for k, l, _, _ in ENCHANT_KINDS}
_CTX = {}


def context(G, Tm, zones, repo):
    """What the rules read, loaded once per (zones, repo): G = the gear_opt module the pool uses, Tm = gear_tiers."""
    key = (id(zones), str(repo))
    if key in _CTX:
        return _CTX[key]
    raw = json.load(open(pathlib.Path(repo) / "assets" / "database" / "db.json", encoding="utf-8"))
    npcs = {n["id"]: n.get("name") for n in raw.get("npcs", [])}
    cm = Tm.CMANGOS
    # drop chances (2026-11-23, the delegator's G13): dungeon_loot.csv, every creature with loot spawned in a dungeon or spawned nowhere
    # and every chest, by CMaNGOS's rules (dungeon_drops.csv, the planner's, holds spawned creatures at 1% or more only)
    chance, loot_rows, map_best, by_name, rank = {}, set(), {}, {}, {}
    for r in csv.DictReader(open(cm / "dungeon_loot.csv", encoding="utf-8")):
        i, it, ch, m = int(r["id"]), int(r["item"]), float(r["chance"]), int(r["map"])
        if r["source"] == "creature":
            chance[(i, it)] = ch
            loot_rows.add(i)
            loot_rows.add(r["name"])   # a name with rows (drop_chance's same-name fallback)
            by_name[(r["name"], it)] = max(ch, by_name.get((r["name"], it), 0.0))
            rank[i] = rank[r["name"]] = (r["rank"], r.get("spawn") or "")
        if m and ch > map_best.get((m, it), (0.0, None))[0]:
            map_best[(m, it)] = (ch, r["name"])
    loot_rows |= {("classic item", int(r["item"])) for r in csv.DictReader(open(cm / "item_names.csv", encoding="utf-8"))}
    quests = {int(r["quest"]): (int(r["zone_or_sort"] or 0), int(r["quest_level"] or 0), int(r["required_races"] or 0))
              for r in csv.DictReader(open(cm / "quests.csv", encoding="utf-8"))}
    reagents = {}
    for r in csv.DictReader(open(cm / "craft_spells.csv", encoding="utf-8")):
        reagents[int(r["spell"])] = {int(x.split(":")[0]) for x in (r["reagents"] or "").split(";") if x}
    world_loot = {int(r["item"]) for r in csv.DictReader(open(cm / "mob_loot.csv", encoding="utf-8"))}
    quest_rep = {int(r["quest"]): (int(r["rep_faction"]), int(r["rep_min"])) for r in csv.DictReader(open(cm / "quest_rep.csv", encoding="utf-8"))}
    trainer = {int(r["spell"]) for r in csv.DictReader(open(cm / "trainer_spells.csv", encoding="utf-8"))}
    taught = set(trainer) | {int(r["learns"]) for r in csv.DictReader(open(cm / "learn_spells.csv", encoding="utf-8")) if int(r["spell"]) in trainer}
    if not Tm.VETTED_PRE:
        raise SystemExit("gear_lists: gear_tiers.VETTED_PRE is empty: load the database through gear_tiers.load_db first")
    # quests whose objective is inside Upper Blackrock Spire: one of its bosses to kill, or an item one of them drops (Classic's dump)
    cnames = {int(r["id"]): r["name"] for r in csv.DictReader(open(cm / "source_names.csv", encoding="utf-8")) if r["kind"] == "c"}
    ubrs_ids = {i for i, n in cnames.items() if n in Tm.UBRS_BOSSES}
    item_from = {}
    for r in csv.DictReader(open(cm / "quest_item_sources.csv", encoding="utf-8")):
        if r["kind"] == "c":
            item_from.setdefault(int(r["item"]), set()).add(int(r["id"]))
    ubrs_quests = set()
    for r in csv.DictReader(open(cm / "quest_geo.csv", encoding="utf-8")):
        for part in (r["objectives"] or "").split(";"):
            k, _, rest = part.partition(":")
            oid = int(rest.split(":")[0]) if rest else 0
            if (k == "c" and oid in ubrs_ids) or (k == "i" and item_from.get(oid, set()) & ubrs_ids):
                ubrs_quests.add(int(r["quest"]))
    ctx = {"G": G, "T": Tm, "zones": zones, "npcs": npcs, "chance": chance, "loot_rows": loot_rows, "map_best": map_best, "by_name": by_name, "rank": rank,
           "quests": quests, "reagents": reagents,
           "world_loot": world_loot, "quest_rep": quest_rep, "taught": taught, "bind": BT.load(), "client_reagents": BT.reagents(),
           "ubrs_quests": ubrs_quests, "professions": professions(repo)}
    _CTX[key] = ctx
    return ctx


def professions(repo):
    """{number: name} of the simulator proto's Profession enum (as raidsim/gear_links.professions reads it)."""
    import re
    txt = (pathlib.Path(repo) / "proto" / "common.proto").read_text(encoding="utf-8")
    m = re.search(r"enum Profession [{]([^}]*)[}]", txt)
    return {int(n): name for name, n in re.findall(r"([A-Za-z]+) = ([0-9]+);", m.group(1) if m else "")}


RANKS = {0: "Hated", 1: "Hostile", 2: "Unfriendly", 3: "Neutral", 4: "Friendly", 5: "Honored", 6: "Revered", 7: "Exalted"}
# Reagents to watch (the audit session, 2026-11-23): not tied to the raids by any tooltip, but Hyjal by name; an item made with one that
# a True Pre-BiS set takes is named to the audit session before the push (the launch checklist asks where they come from)
WATCH_MATS = {248822: "Death Lotus", 260823: "Dimensional Transporter - Mt. Hyjal"}


def standing(it, b):
    """(faction, rank on the client's scale, source) of the reputation an item asks, in the audit session's order of trust (2026-11-23:
    Don Julio's Band asks Exalted, and the client's MinReputation is empty on it): the client's MinFactionID / MinReputation when set;
    Classic's item_template RequiredReputationFaction / Rank; the database's rep source (its RepLevel is one above the client's scale);
    else (None, None, None): unknown, which never puts an item in Easy."""
    if b.get("min_faction"):
        return b["min_faction"], b.get("min_rep", 0), "client"
    if b.get("classic_rep_faction"):
        return b["classic_rep_faction"], b.get("classic_rep_rank", 0), "Classic"
    if b.get("vendor_rep_faction"):   # Classic's vendor condition (the Warsong Gulch quartermasters' gates live there, not in the item)
        return b["vendor_rep_faction"], b.get("vendor_rep_rank", 0), "Classic vendor"
    reps = [s["rep"] for s in it.get("sources") or [] if s.get("rep") and s["rep"].get("repFactionId")]
    if reps:
        r = max(reps, key=lambda x: int(x.get("repLevel") or 0))
        return r["repFactionId"], int(r.get("repLevel") or 0) - 1, "database"
    if b.get("wowhead_rep_rank") is not None:   # the fourth source: Wowhead's Forever tooltip, archived (bind_types.WOWHEAD_REP)
        return b.get("wowhead_rep_faction"), b["wowhead_rep_rank"], "Wowhead"
    return None, None, None


def bg_kind(bg, to_honored):
    """A battleground reward's kind by the user's answer to question B (BG_OPEN) and the standing it asks."""
    st = BG_OPEN.get(bg)
    if st is False:
        return "bg_closed"
    return "battleground_easy" if st is True and to_honored else "battleground"


def ilvl(it):
    return it.get("scalingOptions", {}).get("0", {}).get("ilvl", 0)


# The dungeons' Classic map ids (cmangos_extract.DUNGEON_MAPS): a drop with no row for its own creature takes the item's best row in its
# dungeon's map (a chest there, such as the Gordok Tribute, or another creature). Forever's own dungeons have no Classic map.
ZONE_MAP = {"Ragefire Chasm": 389, "Wailing Caverns": 43, "The Deadmines": 36, "Shadowfang Keep": 33, "Blackfathom Deeps": 48,
            "The Stockade": 34, "Gnomeregan": 90, "Razorfen Kraul": 47, "Scarlet Monastery": 189, "Razorfen Downs": 129, "Uldaman": 70,
            "Zul'Farrak": 209, "Maraudon": 349, "Sunken Temple": 109, "The Temple of Atal'Hakkar": 109, "Blackrock Depths": 230,
            "Blackrock Spire": 229, "Dire Maul": 429, "Scholomance": 289, "Stratholme": 329}
# Summons that are not plain dungeon content (the delegator's G13, 2026-11-23): the Tier 0.5 chain's (its braziers and the Banner of
# Provocation; Jarien and Sothos's loot is the database's "Sothos and Jarien's Heirlooms") are Tier 0.5, out of Easy by the reading (4);
# a class quest's (the warlock's Dreadsteed, the paladin's Charger) needs that class in the group: True lists only.
T05_SUMMONS = {16042: "Lord Valthalak", 16080: "Mor Grayhoof", 16097: "Isalien", 16118: "Kormok", 16059: "Theldren"}
T05_CHESTS = {"Sothos and Jarien's Heirlooms"}
CLASS_SUMMONS = {14506: "Lord Hel'nurath (the warlock's Dreadsteed quest)", 14516: "Death Knight Darkreaver (the paladin's Charger quest)"}
# Rare spawns (the delegator, 2026-11-23): a creature Classic ranks rare (creature_template Rank 2 rare elite, 4 rare) is no Easy source,
# whatever its chance per kill: the chance per run is not known (Phase Blade, 50% from the Burning Felguard), unless the dump shows it
# is a set encounter (the delegator's test: "a creature in a pool with a chance or with alternatives is a rare spawn; one spawned
# outright is not"; dungeon_loot.csv's spawn column): spawned outright (Edwin VanCleef, Lord Roccor, Pyromancer Loregrain, Warder
# Stilgiss, Verek, Quartermaster Zigris, Razorfen Spearhide, and Hearthsinger Forresten at one of his four spots) or summoned by a db
# script (Urok Doomhowl, the Challenge's event). Timmy the Cruel is summoned by a C++ script the dump does not hold; the delegator
# accepted him as an encounter (ENCOUNTER_RARES). By the same test a creature a spawn pool can leave out is a rare spawn whatever its
# rank (Tsu'zee in Dire Maul, Ragglesnout in Razorfen Downs: Classic ranks them elite).
RARE_RANKS = {"2", "4"}
SET_SPAWNS = {"outright", "event script"}
# Timmy the Cruel: the dump holds no summon of his (a C++ script); the delegator's reading, from its memory of Classic and not a
# source: he appears when the square is entered (2026-11-23)
ENCOUNTER_RARES = {"Timmy the Cruel"}
# Spawns the sources disagree on: not Easy (the delegator, 2026-11-23: "Where sources disagree the item is not Easy"); a third source (a
# Classic sniff, Wowhead Forever's kill counts against a sure boss of the same run) reopens one
CONTESTED_SPAWNS = {"Hearthsinger Forresten": "the dump's pool keeps him up at one of four spots, always; Classic ranks him rare elite "
                                              "and players knew him as not always there"}
# A vendor whose currency dungeon bosses drop (the delegator's read of Wowhead Forever, 2026-11-23: Pix Xizzix sells 54 items, every one
# for currency 3469, Tarnished Undermine Real, which 42 bosses of Blackrock Depths, Blackrock Spire, Scholomance, Stratholme and the
# Temple of Atal'Hakkar drop; how many a boss drops is not shown): {vendor: (currency, where, how you get it)}, prices {item: Reals}
# from his "Sells" list (the delegator's browser read the same day; 272400 and 272412 were not in it; the five flask recipes, 50 each,
# are not gear)
CURRENCY_VENDORS = {"Pix Xizzix": ("Tarnished Undermine Reals", "Pix Xizzix in Booty Bay", "dungeon bosses drop the Reals")}
CURRENCY_PRICES = {**{i: 100 for i in (272393, 272394, 272395, 272396, 272397, 272398, 272399, 272401, 272402, 272403, 272404, 272405,
                                       272410)},   # the belts
                   **{i: 75 for i in (272406, 272407, 272408, 272409, 272411, 272413, 272414, 272415)},   # the rings and the cloaks
                   **{i: 50 for i in range(272427, 272437)},   # the idols, totems and librams
                   **{i: 125 for i in (272437, 272438, 272439, 272440)},   # the trinkets
                   228175: 15, 228176: 15, 17010: 15, 17011: 15, 17012: 10}   # two relics, Fiery Core, Lava Core, Core Leather


def currency_text(iid, vendor):
    """The record's and the page's words for a currency vendor's item: "125 Tarnished Undermine Reals from Pix Xizzix in Booty Bay;
    dungeon bosses drop the Reals" (the delegator's wording)."""
    cur, where, how = CURRENCY_VENDORS[vendor]
    price = CURRENCY_PRICES.get(iid)
    return f"{price} {cur} from {where}; {how}" if price else f"{cur} (the price not read) from {where}; {how}"


def currency_cost(items, db):
    """What a set costs in each vendor currency (the delegator, 2026-11-23: "the page should say what the set costs in Reals"):
    {currency: total} over the set's items a currency vendor sells, and the items whose price is not read."""
    total, unpriced = {}, []
    for x in items[:17]:
        it = db.get((x or {}).get("id"))
        for s in (it or {}).get("sources") or []:
            vn = (s.get("soldBy") or {}).get("npcName")
            if vn in CURRENCY_VENDORS:
                cur = CURRENCY_VENDORS[vn][0]
                if it["id"] in CURRENCY_PRICES:
                    total[cur] = total.get(cur, 0) + CURRENCY_PRICES[it["id"]]
                else:
                    unpriced.append(it["name"])
                break
    return {"total": total, **({"unpriced": unpriced} if unpriced else {})} if total or unpriced else {}
# Drop chances Classic's dump cannot give (Forever's own loot), read from Wowhead's Forever item pages ("Dropped by": count of outof) by
# the delegator session on 2026-11-23 and decided Easy there (its G13 (c) decisions): {item: (creature, count, outof)}
WOWHEAD_READ = "Wowhead Forever, read by the delegator session 2026-11-23"
EASY_DECIDED = {276456: ("Black Guard Swordsmith", 120, 371), 276419: ("Crimson Hammersmith", 158, 484),
                276403: ("Crimson Hammersmith", 158, 484), 276396: ("Ezra Grimm", 131, 443), 276395: ("Ezra Grimm", 118, 443),
                276394: ("Ezra Grimm", 132, 443), 276397: ("Malor the Zealous", 242, 726), 276399: ("Malor the Zealous", 216, 726),
                276398: ("Malor the Zealous", 236, 726), 275864: ("Lord Vyletongue", 247, 1184)}


def drop_chance(iid, npc, z, ctx):
    """(chance, where it comes from) of a dungeon drop, from Classic's dump by CMaNGOS's loot rules (dungeon_loot.csv: creatures spawned
    in a dungeon or nowhere, chests, every equippable green or better at 0.1% or more): the creature's own row; else a row of a creature
    of the same name (the database's 10812 is "Balnazzar", Classic's 10812 is Grand Crusader Dathrohan and its Balnazzar 10813 holds
    the loot); else the item's best row in the dungeon's map (a chest, or another creature: the database names Cho'Rush the Observer for
    the Gordok Tribute's Tarnished Elven Ring); else 0.0 when the creature has rows and none for this item (under 0.1%); else
    (None, None): unknown."""
    if npc and (int(npc), iid) in ctx["chance"]:
        return ctx["chance"][(int(npc), iid)], None
    who = ctx["npcs"].get(npc)
    if who and (who, iid) in ctx["by_name"]:
        return ctx["by_name"][(who, iid)], None
    best = ctx["map_best"].get((ZONE_MAP.get(z), iid))
    if best:
        return best
    # "under 0.1%" only for an item Classic has: Forever's own items on a Classic creature (Idol of the Dream on Hazzas) are unknown
    if npc and (int(npc) in ctx["loot_rows"] or who in ctx["loot_rows"]) and ("classic item", iid) in ctx["loot_rows"]:
        return 0.0, None
    dec = EASY_DECIDED.get(iid)   # Forever's own loot: Wowhead's count, for the creature it names
    if dec and dec[0] == who:
        return dec[1] / dec[2], f"{WOWHEAD_READ}: {dec[1]} of {dec[2]}"
    return None, None


def dungeon_kind(it, npc, z, d, ctx):
    """(kind, detail) of a drop in a dungeon (2026-11-23, the delegator's G13: until then a drop whose chance Classic's dump did not give
    counted as Easy; 463 of the 2,548 Easy items were in by that alone): Easy needs a named creature (the database's) and a known chance
    of DROP_MIN or more; the Tier 0.5 summons' loot is tier05, a class quest's summon is a plain dungeon drop, and an unknown chance is a
    plain dungeon drop (unknown_chances lists them; EASY_DECIDED gives Wowhead's chance for the ones decided); a creature Classic ranks
    rare is no Easy source unless the dump spawns it outright or by an event script (RARE_RANKS, SET_SPAWNS, ENCOUNTER_RARES)."""
    Tm, npcs = ctx["T"], ctx["npcs"]
    who = npcs.get(npc) or d.get("otherName") or "trash"
    if npc in T05_SUMMONS or d.get("otherName") in T05_CHESTS:
        return "tier05", f"{z}, {who} (a Tier 0.5 summon)"
    if npc in CLASS_SUMMONS:
        return "dungeon_drop", f"{z}, {CLASS_SUMMONS[npc]}"
    ch, src = drop_chance(it["id"], npc, z, ctx)
    say = ("chance unknown" if ch is None else "under 0.1%" if ch == 0 else f"{ch:.1%}" + (f" from {src}" if src else ""))
    rk, spawn = ctx["rank"].get(int(npc), ctx["rank"].get(who, ("", ""))) if npc else ("", "")
    if who in CONTESTED_SPAWNS:
        return "dungeon_drop", f"{z}, {who}, {say}, a contested spawn ({CONTESTED_SPAWNS[who]})"
    if spawn == "pool" or (rk in RARE_RANKS and spawn not in SET_SPAWNS and who not in ENCOUNTER_RARES):
        return "dungeon_drop", f"{z}, {who}, {say}, a rare spawn (" + ("a spawn pool can leave it out" if spawn == "pool" else
                                                                       f"Classic's rank; the dump spawns it: {spawn}") + ")"
    easy = bool(npc) and (UBRS_EASY or who not in Tm.UBRS_BOSSES) and ch is not None and ch >= Tm.DROP_MIN
    return ("dungeon_drop_easy" if easy else "dungeon_drop"), f"{z}, {who}, {say}"


def unknown_chances(db, ctx):
    """The dungeon drops a named creature gives whose chance no Classic row gives (the creature has no rows and the dungeon's map has no
    row for the item: Forever's own dungeons, creatures the dump lacks), not Tier 0.5 or a class quest's summon: [(item, name, quality,
    zone, creature)], the list for the G13 decisions."""
    zones, npcs = ctx["zones"], ctx["npcs"]
    out = []
    for iid, it in db.items():
        for s in it.get("sources") or []:
            d = s.get("drop") or {}
            z, npc = zones.get(d.get("zoneId")), d.get("npcId")
            if not npc or z not in ctx["T"].DUNGEONS or npc in T05_SUMMONS or npc in CLASS_SUMMONS:
                continue
            if drop_chance(iid, npc, z, ctx)[0] is None:
                out.append((iid, it.get("name"), it.get("quality"), z, npcs.get(npc)))
    return sorted(set(out), key=lambda x: (x[3], x[4] or "", x[1] or ""))


def item_kinds(it, ctx):
    """[(kind, detail)] for every source of the item (see ITEM_KINDS), the phase gate and the vetoes applied."""
    G, Tm, zones, npcs = ctx["G"], ctx["T"], ctx["zones"], ctx["npcs"]
    name, iid = it.get("name", ""), it["id"]
    b = ctx["bind"].get(iid) or {}
    if b.get("holiday"):
        return [("event", f"holiday {b['holiday']}")]
    out = []
    has_pvp = any("pvp" in s for s in it.get("sources") or [])
    for s in it.get("sources") or []:
        if "drop" in s:
            d = s["drop"]
            z, npc = zones.get(d.get("zoneId")), d.get("npcId")
            if npc in G.WORLD_BOSSES:
                out.append(("world_boss", npcs.get(npc)))
            elif npc in G.EVENT_NPCS:
                out.append(("event", npcs.get(npc)))
            elif z == MC_ZONE:
                out.append(("molten_core", "drop"))
            elif z == ONY_ZONE:
                out.append(("onyxia", "drop"))
            elif z in NEW_RAIDS:
                out.append(("new_raid", z))
            elif z in LATER_RAIDS:
                out.append(("later_raid", z))
            elif z in Tm.DUNGEONS:
                out.append(dungeon_kind(it, npc, z, d, ctx))
            else:
                out.append(("world_drop", z or d.get("otherName") or "world"))
        elif "quest" in s:
            q = s["quest"]
            zone, _, _ = ctx["quests"].get(int(q.get("id") or 0), (0, 0, 0))
            qn = q.get("name", "")
            if zone == MC_QUEST_ZONE:
                out.append(("molten_core", "quest " + qn))
            elif zone == ONY_QUEST_ZONE or name in G.RAID_QUEST:
                out.append(("onyxia", "quest " + qn))
            elif zone in Tm.NO_QUEST_ZONES or qn.startswith(G.LATER_QUESTS):
                out.append(("later", "quest " + qn))
            elif it.get("setName") in Tm.T05_SETS:
                out.append(("tier05", qn))
            elif ctx["quest_rep"].get(int(q.get("id") or 0), (0, 0))[1] >= QUEST_REVERED:
                out.append(("rep_above_honored", f"quest {qn} asks reputation {ctx['quest_rep'][int(q['id'])][0]} at "
                            f"{ctx['quest_rep'][int(q['id'])][1]:,}"))
            elif not UBRS_EASY and int(q.get("id") or 0) in ctx["ubrs_quests"]:
                out.append(("quest_ubrs", qn))
            else:
                out.append(("quest", qn))
        elif "crafted" in s:
            sp = int(s["crafted"].get("spellId") or 0)
            cmats = ctx["client_reagents"][0].get(sp)
            if cmats is None:   # the client's other spells that make the item
                cs = [ctx["client_reagents"][0][x] for x in ctx["client_reagents"][1].get(iid, []) if x in ctx["client_reagents"][0]]
                cmats = set().union(*cs) if cs else None
            mats = cmats if cmats is not None else ctx["reagents"].get(sp, set())
            prof = ctx["professions"].get(int(s["crafted"].get("profession") or 0), "")
            if mats & set(NEW_RAID_MATS):
                out.append(("new_raid", "craft from " + ", ".join(NEW_RAID_MATS[m].split(" (")[0] for m in mats & set(NEW_RAID_MATS))))
            elif mats & set(MC_MATS) or (name in G.PHASE1_RAID_MADE and name not in ONY_MADE):
                out.append(("molten_core", "craft"))
            elif mats & set(ONY_MATS) or name in ONY_MADE:
                out.append(("onyxia", "craft"))
            elif name.startswith(G.LATER_PREFIXES):
                out.append(("later_raid", "craft"))
            elif cmats is None and ilvl(it) > Tm.CRAFTED_MAX_ILVL and iid not in Tm.VETTED_PRE:
                out.append(("later", f"craft, item level {ilvl(it)}, reagents unknown"))
            elif it.get("setName") in Tm.T05_SETS:
                out.append(("tier05", "craft"))
            else:
                out.append(("craft", prof))
        elif "rep" in s:
            fid = s["rep"].get("repFactionId")
            f, rank, src = standing(it, b)   # the client's or Classic's requirement before the database's (the audit's order)
            if fid in G.LATER_FACTIONS:
                out.append(("later", "reputation " + str(fid)))
            elif fid in BG_FACTIONS:
                out.append((bg_kind(BG_FACTIONS[fid], rank is not None and rank <= CLIENT_HONORED),
                            f"{BG_FACTIONS[fid]}, {RANKS.get(rank, 'standing unknown')} ({src})"))
            else:
                out.append(("rep_to_honored" if rank is not None and rank <= CLIENT_HONORED else "rep_above_honored",
                            f"reputation {fid}, {RANKS.get(rank, 'standing unknown')} ({src})"))
        elif "soldBy" in s:
            v = s["soldBy"]
            vn = v.get("npcName")
            f, rank, src = standing(it, b)
            if vn in EVENT_VENDORS:
                out.append(("event", EVENT_VENDORS[vn]))
            elif vn in BG_VENDORS:   # a quartermaster's item: Easy only when a source gives a standing up to Honored
                bg = BG_VENDORS[vn]
                out.append((bg_kind(bg, rank is not None and rank <= CLIENT_HONORED),
                            f"{bg}, {vn}, " + (f"{RANKS.get(rank, rank)} ({src})" if rank is not None else "standing unknown")))
            elif has_pvp or vn in HONOR_VENDORS:
                out.append(("pvp", vn))
            elif f in BG_FACTIONS and rank is not None:
                out.append((bg_kind(BG_FACTIONS[f], rank <= CLIENT_HONORED), f"{BG_FACTIONS[f]}, {RANKS.get(rank, rank)} ({src})"))
            elif f and rank is not None:   # a reputation vendor's item: its standing from the client, Classic or the database
                out.append(("rep_to_honored" if rank <= CLIENT_HONORED else "rep_above_honored",
                            f"reputation {f}, {RANKS.get(rank, rank)} ({src}), vendor {vn}"))
            elif it.get("setName") in Tm.T05_SETS:
                out.append(("tier05", vn))
            elif vn in CURRENCY_VENDORS:
                out.append(("dungeon_currency", currency_text(iid, vn)))
            else:
                out.append(("vendor", vn))
        elif "pvp" in s:
            out.append(("pvp", "honor"))
    if not out:   # no source the database lists
        if name in G.RAID_QUEST:
            out.append(("onyxia", "quest reward (no source listed)"))
        elif name in G.PHASE1_QUEST:
            out.append(("molten_core", "quest reward (no source listed)"))
        elif iid in G.VENDOR_ITEMS:
            out.append(("vendor", "known vendor (gear_opt.VENDOR_ITEMS)"))
        else:
            if b.get("bind") == 2 and iid in ctx["world_loot"] and ilvl(it) <= G.SOURCELESS_MAX_ILVL:
                out.append(("auction", "binds when equipped; Classic's world creatures drop it"))
            if iid in Tm.VETTED_PRE and ilvl(it) <= G.SOURCELESS_MAX_ILVL:
                out.append(("vetted", "a launch or pre-raid preset"))
    if it.get("setName") in Tm.T05_SETS:   # a Tier 0.5 piece is Tier 0.5 whatever entry names it (the database gives some legs a pvp one)
        out = [("tier05", d) if k in ITEM_LISTS and ITEM_LISTS[k] and k not in ("onyxia", "new_raid") else (k, d) for k, d in out]
    if (it.get("phase") or 1) >= 2:   # later content, but for True BiS's raids
        out = [x if x[0] in ("onyxia", "new_raid", "molten_core", "later_raid", "world_boss", "event") else ("later", "phase 2: " + x[0])
               for x in out] or [("later", "phase 2")]
    return out


def lists_of(it, ctx):
    """The lists the item is in (a frozenset of "bis", "prebis", "dungeon")."""
    q = it.get("quality", 0)
    if q < 2 or q >= 5 or it["id"] in ctx["G"].SUSPECT_ITEMS:
        return NONE
    out = set()
    for k, _ in item_kinds(it, ctx):
        out |= ITEM_LISTS[k]
    return frozenset(out)


def in_list(it, lst, ctx):
    return lst in lists_of(it, ctx)


def enchant_kinds(e, ctx):
    G, zones = ctx["G"], ctx["zones"]
    out = []
    if int(e.get("spellId") or 0) in ctx["taught"]:
        out.append(("taught", "trainer"))
    for s in e.get("sources") or []:
        if "drop" in s:
            d = s["drop"]
            z, npc = zones.get(d.get("zoneId")), d.get("npcId")
            if npc in G.WORLD_BOSSES or npc in G.EVENT_NPCS:
                out.append(("event", str(npc)))
            elif z == MC_ZONE:
                out.append(("molten_core", "drop"))
            elif z == ONY_ZONE:
                out.append(("onyxia", "drop"))
            elif z in LATER_RAIDS:
                out.append(("later", z))
            else:
                out.append(("drop", z or d.get("otherName") or "world"))
        elif "quest" in s:
            qn = s["quest"].get("name", "")
            zone = ctx["quests"].get(int(s["quest"].get("id") or 0), (0, 0, 0))[0]
            out.append(("later", "quest " + qn) if zone in ctx["T"].NO_QUEST_ZONES or qn.startswith(G.LATER_QUESTS) else ("quest", qn))
        elif "rep" in s:
            fid = s["rep"].get("repFactionId")
            out.append(("later", f"reputation {fid}") if fid in G.LATER_FACTIONS else ("rep", f"reputation {fid}"))
        elif "soldBy" in s:
            out.append(("vendor", s["soldBy"].get("npcName")))
        elif "crafted" in s:
            out.append(("craft", str(s["crafted"].get("profession") or "")))
    if not e.get("sources") and not out and (e.get("type"), e["effectId"]) in ctx["T"]._ENCH["vetted"]["prebis"]:
        out.append(("vetted", "a pre-raid preset"))
    if (e.get("phase") or 1) >= 2:
        out = [x if x[0] in ("onyxia", "molten_core", "event") else ("later", "phase 2: " + x[0]) for x in out] or [("later", "phase 2")]
    return out


def enchant_lists(e, ctx):
    out = set()
    for k, _ in enchant_kinds(e, ctx):
        out |= ENCHANT_LISTS[k]
    return frozenset(out)


# The rank titles of the honor system's gear (Classic's ranks 4-14 of each side; Forever's rank gear adds "Premier "): the database's
# PvP listing names no side and the client's race mask is -1 on Forever's, so the title is what says who can buy it (2026-11-23, the
# list test: Premier High Warlord's Blade had no Alliance alternative; its twin is Premier Grand Marshal's Longsword, the same stats).
RANK_SIDE = {"Grand Marshal": "Alliance", "Field Marshal": "Alliance", "Marshal": "Alliance", "Lieutenant Commander": "Alliance",
             "Commander": "Alliance", "Knight-Champion": "Alliance", "Knight-Captain": "Alliance", "Knight-Lieutenant": "Alliance",
             "Sergeant Major": "Alliance", "Master Sergeant": "Alliance",
             "High Warlord": "Horde", "Warlord": "Horde", "Lieutenant General": "Horde", "General": "Horde", "Champion": "Horde",
             "Centurion": "Horde", "Legionnaire": "Horde", "Blood Guard": "Horde", "Stone Guard": "Horde", "First Sergeant": "Horde",
             "Senior Sergeant": "Horde"}
RANK_TITLE = re.compile(r"^(?:Premier )?(" + "|".join(sorted(map(re.escape, RANK_SIDE), key=len, reverse=True)) + r")'s ")
# Rank 3 is "Sergeant" on both sides; its items differ by name (the delegator, 2026-11-23)
RANK_NAME_SIDE = {"Sergeant's Cape": "Alliance", "Sergeant's Cloak": "Horde"}


def faction_of(it, ctx):
    """"Alliance" or "Horde" for a one-faction item: the database's factionRestriction (1 Alliance, 2 Horde), else the client's race
    mask, else every source that names a side naming the same one (a quest's or a vendor's faction field, a reputation's factionId;
    a PvP listing and a reputation without a factionId name none and are passed over, so Outrider's Chain Leggings, sold by a Horde
    vendor and listed as PvP, is the Horde's; a drop or a craft makes the item anyone's), else, for rank gear (PvP listings only), the
    rank title in its name (RANK_SIDE) or "of the Alliance" / "of the Horde"; None otherwise (2026-11-23: until then a PvP listing or
    a reputation source made any item anyone's)."""
    fr = it.get("factionRestriction")
    if fr in (1, 2):
        return "Alliance" if fr == 1 else "Horde"
    f = BT.race_faction((ctx["bind"].get(it["id"]) or {}).get("races"))
    if f:
        return f
    fs, srcs = set(), it.get("sources") or []
    for s in srcs:
        if "pvp" in s:
            continue
        if "rep" in s:
            if s["rep"].get("factionId") in (1, 2):
                fs.add(s["rep"]["factionId"])
            continue
        v = (s.get("quest") or s.get("soldBy") or {}).get("faction")
        if v not in (1, 2):
            return None
        fs.add(v)
    if fs:
        return ("Alliance" if fs == {1} else "Horde") if len(fs) == 1 else None
    if srcs and all("pvp" in s for s in srcs):
        name = it.get("name", "")
        if name.removeprefix("Premier ") in RANK_NAME_SIDE:
            return RANK_NAME_SIDE[name.removeprefix("Premier ")]
        m = RANK_TITLE.match(name)
        if m:
            return RANK_SIDE[m.group(1)]
        for side in ("Alliance", "Horde"):
            if name.endswith(f"of the {side}"):
                return side
    return None


def _taken(items, slot, db, G):
    """What the set's other slots use up: each item's id (the set builder never wears one id twice: gear_opt.class_picker's greedy;
    the Easy Frost set wears the Alliance's and the Horde's quest rings, and each side's alternative had been the ring the other slot
    already held) and its unique-equipped keys (gear_opt.unique_keys: its id when unique, its limitCategory)."""
    out = set()
    for j, y in enumerate(items[:17]):
        if j != slot and y and y.get("id") in db:
            out |= {("id", y["id"])} | G.unique_keys(db[y["id"]])
    return out


def _uses(it, G):
    return {("id", it["id"])} | G.unique_keys(it)


def alternatives(cls, items, w, lst, db, ctx, G, fits):
    """The other faction's alternative for every one-faction item of a set (the reading (6)): the client's OppositeFactionItemID when
    that item is in the list, else the best item by the set's weights `w` that fits the slot (`fits(item, slot, current item)`) and the
    other faction can use; not raced. Each side's set is built slot by slot, so an alternative never repeats a unique-equipped item
    (or a limit category) the set already wears, nor one an earlier slot's alternative took (2026-11-23, the list test: a ring's
    alternative was the signet the other ring slot held). [{slot, item, faction, for, how, alternative, alternative_value, value}]."""
    out = []
    for other in ("Horde", "Alliance"):
        f = "Alliance" if other == "Horde" else "Horde"
        work = [dict(x) if x else {} for x in items[:17]]
        for slot, x in enumerate(items[:17]):
            it = db.get((x or {}).get("id"))
            if not it or faction_of(it, ctx) != f:
                continue
            taken = _taken(work, slot, db, G)
            opp = (ctx["bind"].get(it["id"]) or {}).get("opposite")
            alt = db.get(opp) if opp and db.get(opp) and in_list(db[opp], lst, ctx) and not (_uses(db[opp], G) & taken) else None
            how = "the client's other-faction item" if alt else "the best other item by the weights"
            if not alt:
                best = None
                for cand in db.values():
                    if cand["id"] == it["id"] or cand.get("type") != it.get("type") or faction_of(cand, ctx) == f:
                        continue
                    if not fits(cand, slot, it) or _uses(cand, G) & taken:
                        continue
                    v = G.value(cand, w, slot)
                    if best is None or v > best[0]:
                        best = (v, cand)
                alt = best[1] if best else None
            if alt:
                work[slot] = dict(work[slot], id=alt["id"])
            out.append({"slot": slot, "item": it["id"], "name": it.get("name"), "faction": f, "for": other, "how": how,
                        "alternative": alt["id"] if alt else None, "alternative_name": alt.get("name") if alt else None,
                        "value": round(G.value(it, w, slot), 2), "alternative_value": round(G.value(alt, w, slot), 2) if alt else None})
    return sorted(out, key=lambda r: (r["slot"], r["for"]))


PVP_KINDS = {"pvp", "battleground", "battleground_easy"}
NEW_RAID_PAGE_NOTE = "from 2026-12-09 (made with a material from Hyjal Summit or The Barrow Deeps)"   # the audit session's wording


def admitting(it, lst, ctx):
    """The kinds that put the item in the list."""
    return {k for k, _ in item_kinds(it, ctx) if lst in ITEM_LISTS.get(k, NONE)}


def pvp_only(it, lst, ctx):
    a = admitting(it, lst, ctx)
    return bool(a) and a <= PVP_KINDS


def marks(items, lst, db, ctx):
    """{slot: {...}} the page marks a set's items with (the audit session, 2026-11-23): "pvp" for an item only PvP puts in the list (a
    rank or a battleground standing the player may not have yet), "profession" for a crafted-only item that binds when picked up (you
    must have the profession yourself)."""
    out = {}
    for slot, x in enumerate(items[:17]):
        it = db.get((x or {}).get("id"))
        if not it:
            continue
        m = {}
        if pvp_only(it, lst, ctx):
            m["pvp"] = True
        srcs = it.get("sources") or []
        if srcs and all("crafted" in s for s in srcs) and (ctx["bind"].get(it["id"]) or {}).get("bind") == 1:
            m["profession"] = ctx["professions"].get(int(srcs[0]["crafted"].get("profession") or 0), "the profession")
        by_spell, by_item = ctx["client_reagents"]
        watch = sorted({WATCH_MATS[r] for sp in by_item.get(it["id"], []) for r in by_spell.get(sp, set()) if r in WATCH_MATS})
        if watch:
            m["watch"] = watch   # name it to the audit session before the push when a True Pre-BiS set takes it
        if any(k == "new_raid" and d.startswith("craft") for k, d in item_kinds(it, ctx)):
            m["raid_craft"] = NEW_RAID_PAGE_NOTE
        if m:
            out[str(slot)] = m
    return out


def easy_violations(db, ctx):
    """Easy Pre-BiS items that ask more than Honored by any source (the client's, Classic's or the database's standing): the audit
    session's standing check (2026-11-23, 0 at 99ebe62a); gear_tiers.make and refit stop before an Easy set when it is not empty."""
    if "easy_violations" not in ctx:
        ctx["easy_violations"] = [(i, it.get("name"), RANKS.get(r, r), src) for i, it in db.items() if in_list(it, E, ctx)
                                  for _, r, src in [standing(it, ctx["bind"].get(i) or {})] if r is not None and r > CLIENT_HONORED]
    return ctx["easy_violations"]


def pvp_alternatives(cls, items, w, lst, db, ctx, G, fits):
    """For every item of a set that only PvP puts in the list: the best item of the same list by the set's weights `w` that fits the slot
    and that something else puts there (the audit session, 2026-11-23: a list leaning on rank gear the player cannot have yet needs a
    fallback); not raced. The set without PvP is built slot by slot, so an alternative never repeats a unique-equipped item (or a limit
    category) the set already wears or an earlier slot's alternative took (2026-11-23, the list test: Don Julio's Band's alternative was
    the Warden's Signet of Ferocity in the other ring slot, and both hands' was Heartseeker, which is unique).
    [{slot, item, name, alternative, alternative_name, value, alternative_value}]."""
    out = []
    work = [dict(x) if x else {} for x in items[:17]]
    for slot, x in enumerate(items[:17]):
        it = db.get((x or {}).get("id"))
        if not it or not pvp_only(it, lst, ctx):
            continue
        taken = _taken(work, slot, db, G)
        best = None
        for cand in db.values():
            if cand["id"] == it["id"] or cand.get("type") != it.get("type") or not fits(cand, slot, it) or pvp_only(cand, lst, ctx):
                continue
            if _uses(cand, G) & taken:
                continue
            v = G.value(cand, w, slot)
            if best is None or v > best[0]:
                best = (v, cand)
        alt = best[1] if best else None
        if alt:
            work[slot] = dict(work[slot], id=alt["id"])
        out.append({"slot": slot, "item": it["id"], "name": it.get("name"), "alternative": alt["id"] if alt else None,
                    "alternative_name": alt.get("name") if alt else None, "value": round(G.value(it, w, slot), 2),
                    "alternative_value": round(best[0], 2) if best else None})
    return out


def table(counts=None):
    """The rules as implemented (Markdown)."""
    mark = lambda ls, l: "in" if l in ls else "out"   # noqa: E731
    o = ["| Item source kind | True BiS | True Pre-BiS | Easy Pre-BiS | What | From |", "|---|---|---|---|---|---|"]
    o += [f"| {k} | {mark(ls, T)} | {mark(ls, P)} | {mark(ls, E)} | {what} | {src} |" for k, ls, what, src in ITEM_KINDS]
    o += ["", "| Enchant / modifier kind | True BiS | True Pre-BiS | Easy Pre-BiS | What | From |", "|---|---|---|---|---|---|"]
    o += [f"| {k} | {mark(ls, T)} | {mark(ls, P)} | {mark(ls, E)} | {what} | {src} |" for k, ls, what, src in ENCHANT_KINDS]
    if counts:
        o += ["", "Pool sizes (quality 2-4; items any class could wear): " + ", ".join(f"{LABEL[l]} {n}" for l, n in counts.items())]
    return "\n".join(o)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--table", action="store_true")
    ap.add_argument("--counts", action="store_true", help="also load the database and count each list's items and kinds")
    a = ap.parse_args()
    counts = None
    if a.counts:
        import gear_tiers as GT
        repo = GT.R.repo_path(argparse.Namespace(repo=None))
        db, zones = GT.load_db(repo)[:2]
        ctx = context(GT.G, GT, zones, repo)
        counts = {l: sum(1 for it in db.values() if in_list(it, l, ctx)) for l in LISTS}
    if a.table:
        print(table(counts))


if __name__ == "__main__":
    main()
