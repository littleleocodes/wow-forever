"""Pre-BiS and phase-1 BiS gear for every raid damage spec (2026-10-01, user request: "DPS rankings for pre-BiS as well as best in slot,
like WoWSims does").

    python _reference/data/raidsim/gear_tiers.py --set <class> "<spec>" <tier> --entry <entry> --build <build id | candidate .json>
    python _reference/data/raidsim/gear_tiers.py --remake [--classes ...] [--spec ...] [--fresh]   # every ML record's sets again

(ml_pipeline.py makes every spec's sets through `make`.)

Three tiers, one item pool each (the simulator's item database at the pinned wowsims/forever commit, raidsim/setup.py; the
ElliotWood/Forever fork's until 2026-10-18, `_reference/sim-port.md`). The third, **dungeon** (quests and dungeons, 2026-11-18), is
the strictest: quest rewards of no raid, 5-player dungeon boss drops at 5%+, trainer recipes, reputation to Honored (DUNGEONS below;
made by raidsim/dungeon_tier.py). Tier 0.5 is in neither pre-raid tier since the same day (T05_SETS).
- **bis** (phase 1): `gear_opt.py`'s pool: dungeons, Molten Core, Onyxia, world drops, crafted, quest; items with no listed source only
  when a community phase-0/1, launch or pre-raid preset uses them (the Forever launch items); no BWL, ZG, AQ, Naxxramas, world bosses
  or legendaries; the hunter's Molten Core quest bow and stave (Rhok'delar, Lok'delar) count.
- **prebis** (pre-raid): the same without any raid drop, without the quest rewards of raid bosses and without crafted items made from
  Molten Core or Onyxia materials (`PHASE1_RAID_MADE`, our list: the database has the recipe, not its materials); items with no listed
  source only when a launch or pre-raid preset uses them.
In both tiers a source is a drop, a recipe or a reputation (`gear_opt.dated_sources`, 2026-11-05): the database's quest, vendor and PvP
entries say how an item is obtained, not when, and count as no source listed (`_reference/page-audit.md` J1-J2).
Unlike gear_opt.py, which gives every group of entries sharing a set one compromise set, each spec gets its own set per tier
(a Fire mage wants fire damage, a Frost mage frost damage): the simulator's stat weights for the spec's best build in its entry
(bench `statweights`), the best item per slot by those weights (two variants: every slot, and one keeping set pieces and items with
effects), the weights refreshed once on the new set (hit caps move), the trinkets raced (gear_opt.screen_trinkets: every trinket of the
pool alone, then the best seven in pairs; the class's preset trinket pairs until 2026-10-22), the variants raced on
seed 1 and the choice confirmed on seed 2. The spec's specs.json set competes in the BiS tier; unlike gear_opt.py, which keeps it unless
a new set wins by 0.5%, the tier takes whichever set measures best on both seeds (with the 0.5% margin the first 2026-10-01 run kept an
item-level-33 mace in the Shadow priest's BiS set, 0.3% behind the new set on both seeds). Relics stay as they are.
Sets: `gear_sets/forever/tiers/<class>-<spec>-<tier>.gear.json`; records: the `gear` key of ml_pipeline.py's `raidsim/ml/<class>-<spec>.json`.
The talent search (`ml_talents.py`) and the tier ranking (`ml_pipeline.py`) pass these sets per build (`gear_json`), so specs.json keeps
its gear.
"""
import argparse
import datetime
import importlib.util
import itertools
import json
import os
import pathlib
import sys
import time

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[2]
sys.path[:0] = [str(ROOT / "_reference/data"), str(HERE)]
import paths  # noqa: E402
import spec_modes as SM  # noqa: E402

# One gear_opt for every copy of this module (2026-11-20, search-improvements 0q): each copy had loaded its own, with its own item stat
# map and vetted items, and a copy whose database was loaded through another valued every item at 0 (Frost Med's level-30 set). The
# module registered as "gear_opt" is reused when it is this file; else this one is loaded and registered (when the name is free).
_G = sys.modules.get("gear_opt")
if _G is not None and getattr(_G, "__file__", None) and pathlib.Path(_G.__file__).resolve() == (HERE / "gear_opt.py").resolve():
    G = _G
else:
    _s = importlib.util.spec_from_file_location("gear_opt", HERE / "gear_opt.py")
    G = importlib.util.module_from_spec(_s)
    if _G is None:
        sys.modules["gear_opt"] = G
    _s.loader.exec_module(G)
R = G.R
import gear_lists as GL  # noqa: E402   (the three lists' rules, 2026-11-23)
SETS = HERE / "gear_sets" / "forever" / "tiers"
TIERS = ("prebis", "bis")
TODAY = datetime.date.today().isoformat()

RAID_ZONES = G.RAID_OK | G.RAID_NO
# Crafted items (the database has the recipe, not its materials; our lists, 2026-10-01):
# - made from Molten Core or Onyxia materials (Fiery Core, Lava Core, Core Leather, Sulfuron Ingot, Scale of Onyxia), and the rewards of
#   Onyxia's quest: phase 1, so in bis and not in prebis;
PHASE1_RAID_MADE = G.PHASE1_RAID_MADE   # (both lists live in gear_opt.py since 2026-11-18: its later_phase reads them)
RAID_QUEST = G.RAID_QUEST
# - made from later raids' materials or later reputations (Zul'Gurub's Bloodvine and hides, Ahn'Qiraj's Cenarion Circle recipes and
#   obsidian, Naxxramas's frost-resistance sets): in neither tier. gear_opt.py's pool let them in, so the 2026-09-30 phase-1 sets of the
#   hunter and the Retribution paladin carried Bloodvine pieces (Zul'Gurub);
LATER_PREFIXES = G.LATER_PREFIXES   # gear_opt.py's list (its pool excludes them too since 2026-10-01)
# - any other crafted item of item level 65 or more is a later-phase recipe unless a community preset of the tier uses it.
CRAFTED_MAX_ILVL = 64
VETTED_PRE = G.__dict__.setdefault("TIERS_VETTED_PRE", set())   # item ids in the simulator's launch and pre-raid presets (every class),
# kept on the shared gear_opt module so every copy of this file reads the same set (2026-11-20, 0q)
PRE_NAMES = ("launch", "p0", "prebis", "preraid", "pre-bis", "pre_raid")
# Tier 0.5 (Dungeon Set 2, Season of Discovery's reissue; _reference/tier-0.5-research.md, 2026-11-18): a long gold and group project
# (a level-58 chain that consumes the Tier 0 pieces, 10-player Upper Blackrock Spire, the vendors' gold) whose set bonuses players
# report broken in the game: in neither pre-raid tier (user, the same day: "Go with your recs"). The BiS tier keeps what its presets vet.
T05_SETS = {"Battlegear of Heroism", "Beastmaster Armor", "Darkmantle Armor", "Deathmist Raiment", "Feralheart Raiment", "Sorcerer's Regalia",
            "Soulforge Armor", "The Five Thunders", "Vestments of the Virtuous"}
# The quests-and-dungeons tier ("dungeon", 2026-11-18; user: "a pre-BIS list for the things that can just be obtained through questing or
# doing dungeons and not having to do all of the work to get the 0.5 tier set"; the definitions are Claude's, on the user's "Go with
# your recs"). An item counts when one of its sources does:
# - a quest of no raid (Forever's own quests, unknown to the Classic dump, count; Silithus's are the Ahn'Qiraj war's);
# - a drop of a named mob in a 5-player dungeon (the planner's dungeons, plan.ENTRANCE) at a 5% chance or more where the Classic dump
#   has the pair (boss loot is 14-20%, the rare drops 1-2%); trash drops, world drops and Upper Blackrock Spire's bosses (10 players in
#   Forever) do not;
# - a recipe a trainer teaches (the craft spell, or the spell that teaches it, among the dump's trainer spells): no rare recipe;
# - a reputation reward up to Honored;
# - the vendor items gear_opt vets.
# Never Tier 0.5, the auction house or PvP.
DUNGEONS = {"Ragefire Chasm", "Wailing Caverns", "The Deadmines", "Shadowfang Keep", "Blackfathom Deeps", "The Stockade", "Gnomeregan",
            "Razorfen Kraul", "Scarlet Monastery", "Razorfen Downs", "Uldaman", "Zul'Farrak", "Maraudon", "Sunken Temple",
            "The Temple of Atal'Hakkar", "Blackrock Depths", "Blackrock Spire", "Dire Maul", "Scholomance", "Stratholme", "The Hall of Thanes",
            "Ruins of Lordaeron", "Excavation Site: Wetlands", "City of Dalaran"}
UBRS_BOSSES = {"Pyroguard Emberseer", "Solakar Flamewreath", "Jed Runewatcher", "Goraluk Anvilcrack", "Gyth", "Warchief Rend Blackhand",
               "The Beast", "General Drakkisath", "Lord Valthalak"}
DROP_MIN = 0.05
REP_MAX = 6   # Honored (the simulator's RepLevel)
NO_QUEST_ZONES = {2717, 2159, 2677, 1977, 3429, 3428, 3456, 1377}   # Molten Core, Onyxia, BWL, Zul'Gurub, AQ20, AQ40, Naxxramas, Silithus
CMANGOS = ROOT / "_reference/data/raw/2026-11-09-cmangos-classic-db-c33f90b8e"
_DUNGEON_DATA = {}


def dungeon_data(repo):
    """(npc names, {(creature, item): chance}, trainer-taught craft spells, {quest: (zone, level)}) for the quests-and-dungeons tier."""
    if not _DUNGEON_DATA:
        import csv
        raw = json.load(open(pathlib.Path(repo) / "assets" / "database" / "db.json", encoding="utf-8"))
        npcs = {n["id"]: n.get("name") for n in raw.get("npcs", [])}
        chance = {(int(r["creature"]), int(r["item"])): float(r["chance"]) for r in csv.DictReader(open(CMANGOS / "dungeon_drops.csv", encoding="utf-8"))}
        trainer = {int(r["spell"]) for r in csv.DictReader(open(CMANGOS / "trainer_spells.csv", encoding="utf-8"))}
        taught = set(trainer)
        for r in csv.DictReader(open(CMANGOS / "learn_spells.csv", encoding="utf-8")):   # a trainer teaches the learn spell of a craft
            if int(r["spell"]) in trainer:
                taught.add(int(r["learns"]))
        quests = {int(r["quest"]): (int(r["zone_or_sort"] or 0), int(r["quest_level"] or 0))
                  for r in csv.DictReader(open(CMANGOS / "quests.csv", encoding="utf-8"))}
        _DUNGEON_DATA.update(npcs=npcs, chance=chance, taught=taught, quests=quests)
    d = _DUNGEON_DATA
    return d["npcs"], d["chance"], d["taught"], d["quests"]


def dungeon_source(s, it, zones, data):
    """Whether one source entry counts for the quests-and-dungeons tier (see DUNGEONS above)."""
    npcs, chance, taught, quests = data
    so = it.get("scalingOptions", {}).get("0", {})
    if s.get("quest"):
        zone, level = quests.get(int(s["quest"].get("id") or 0), (0, 0))
        return zone not in NO_QUEST_ZONES and level <= 62 and not G.later_reward(it) and so.get("ilvl", 0) <= G.SOURCELESS_MAX_ILVL
    if s.get("drop"):
        d = s["drop"]
        npc = d.get("npcId")
        if not npc or zones.get(d.get("zoneId")) not in DUNGEONS or npcs.get(npc) in UBRS_BOSSES:
            return False
        c = chance.get((int(npc), int(it["id"])))
        return c is None or c >= DROP_MIN
    if s.get("crafted"):
        return int(s["crafted"].get("spellId") or 0) in taught
    if s.get("rep"):
        return int(s["rep"].get("repLevel") or 0) <= REP_MAX
    return False


def load_vetted_pre(repo):
    for p in G.preset_files(repo):   # the official repository's presets and the fork's vendored ones (2026-10-22)
        if any(k in p.name for k in PRE_NAMES) and "p2" not in p.name:
            VETTED_PRE.update(x["id"] for x in json.load(open(p, encoding="utf-8")).get("items", []) if x and x.get("id"))


def crafted_ok(it, tier):
    """A crafted-only item's tier rule (see the lists above); True for items with any other dated source."""
    srcs = G.dated_sources(it)
    if not srcs or not all(s.get("crafted") for s in srcs):
        return True
    name = it.get("name", "")
    if name in PHASE1_RAID_MADE:
        return tier == "bis"
    if name.startswith(LATER_PREFIXES):   # later raids' materials, whatever a preset says (the fork's launch presets list some)
        return False
    if it["id"] in (G.VETTED if tier == "bis" else VETTED_PRE):
        return True
    return it.get("scalingOptions", {}).get("0", {}).get("ilvl", 0) <= CRAFTED_MAX_ILVL


def rules_ctx(zones, repo=None):
    """raidsim/gear_lists.py's context for this copy of the module (its constants, VETTED_PRE and the enchant data are this copy's)."""
    import types
    t = types.SimpleNamespace(CMANGOS=CMANGOS, VETTED_PRE=VETTED_PRE, DUNGEONS=DUNGEONS, UBRS_BOSSES=UBRS_BOSSES, DROP_MIN=DROP_MIN,
                              NO_QUEST_ZONES=NO_QUEST_ZONES, T05_SETS=T05_SETS, CRAFTED_MAX_ILVL=CRAFTED_MAX_ILVL, REP_MAX=REP_MAX, _ENCH=_ENCH)
    return GL.context(G, t, zones, repo or R.repo_path(argparse.Namespace(repo=None)))


def easy_check(tier, db, zones, repo=None):
    """Stop before an Easy Pre-BiS set when any Easy item asks more than Honored (gear_lists.easy_violations; the audit session's
    check, 2026-11-23)."""
    if tier != "dungeon":
        return
    bad = GL.easy_violations(db, rules_ctx(zones, repo))
    if bad:
        raise SystemExit(f"gear_tiers: {len(bad)} Easy Pre-BiS items ask more than Honored (the standing check): "
                         + "; ".join(f"{n} ({i}, {r}, {s})" for i, n, r, s in bad[:8]))


WITHOUT_PVP = ("honor rank gear and every battleground reward (gear_lists.PVP_KINDS: an item only those put in the list), whatever "
               "its standing")


def pool_of(tier, zones, repo=None, nopvp=False, side=None):
    """The list's item pool (2026-11-23): raidsim/gear_lists.py's rules, "bis" = True BiS, "prebis" = True Pre-BiS, "dungeon" = Easy
    Pre-BiS (any other name: True Pre-BiS). Until then three tiers with their own rules (Raid BiS, Pre-raid, Quests and dungeons; the
    module docstring and crafted_ok / dungeon_source above, kept for the record). `nopvp` (2026-11-23, the audit session's ruling on the
    list test: the no-PvP set is the one most players wear, so it is a made set): without what only PvP puts in the list (WITHOUT_PVP).
    `side` ("Alliance" / "Horde"): without the other side's items (gear_lists.faction_of), the faction check of the same ruling."""
    ctx = rules_ctx(zones, repo)
    lst = tier if tier in GL.LISTS else "prebis"
    if not nopvp and not side:
        return lambda it: GL.in_list(it, lst, ctx)

    def ok(it):
        if not GL.in_list(it, lst, ctx):
            return False
        if nopvp and GL.pvp_only(it, lst, ctx):
            return False
        return not side or GL.faction_of(it, ctx) in (None, side)
    return ok


# ------------------------------------------------------------------------------------------------ weapons, set pieces, enchants (2026-11-22)
# The audit session's gear findings G1-G3 (_reference/audit-1119.md, "Survival's gear sets against a community list": a community Survival
# list beat our Pre-BiS set by 2.8% in the simulator, and our own pre-raid rules with these fixes, put in by hand, by 4.3%). Every set
# maker runs the three steps (optimize_set with `refine`), and `refit` runs them on a set file as it stands:
# - weapons raced per hand (G2): the per-slot pick sees a weapon's dps and stats, not its speed or the hits a fast off hand adds
#   (Distracting Dagger for Heartseeker in Survival's off hand: +1.5%);
# - an item set's pieces raced as a unit (G3): the per-slot pick values no set bonus (the Devilsaur pair's 2% hit: +0.25%);
# - enchants per slot from every enchant the database lists for the item (G1): the role templates (fill_enchants.py) predate Forever's
#   enchants (no necklace enchant at all; Cloak +3 Agility for +5, Bracer +9 Strength for +9 Agility, Gloves +7 for +10: +1.1% together).
#   Stat enchants are chosen by the weights, as items are; an enchant with an effect, a proc, a pseudo-stat or weapon damage (Crusader,
#   the scopes, Arcanum of Rapidity) is raced against the slot's stat pick.
WEAPON_TOP, WEAPON_EFFECTS_FROM, WEAPON_RERACE = 12, 20, 4   # per hand: the best 12 by the weights, any with an effect among the best 20;
WEAPON_DPS_MIN = 0.1   # the main hand raced again on its pass-1 best 4 after the off hand changed; a hand whose dps the weights value
SET_MAX_LOSS, SET_RACE_MAX = 0.10, 80   # (SET_MAX_LOSS is history: since 2026-11-23 every bonus step races; 80 units a round at most)
PAIR_ANY = True   # a two-piece unit races whatever it costs by the weights (the bonus is what the weights cannot see)
# The three rules above as widened on 2026-11-23 (the audit session's ruling on the list test's attribution: Survival's no-PvP True Pre-BiS
# against wowtbc.gg's like-for-like list, the site's choice put into our set one slot or linked group at a time, 6,000 fights, seeds 1/2):
# - WEAPON_TOP 8 -> 12: Distracting Dagger, the site's off hand, ranked 9th by the weights (29.0; the 8th 29.2) and never raced; +0.68% /
#   +0.72% in our set;
# - PAIR_ANY: the Devilsaur pair cost 30% of the replaced items' value by the weights and never raced; the pair +1.07% / +1.08%, its
#   pieces alone +0.42% / +0.52% and -0.31% / -0.23%, so the bonus about +0.9%; SET_RACE_MAX 10 -> 16 for the pairs it admits;
# - REWEIGH (below): hit past the cap.
REWEIGH = True   # the weights measured again at the picked set, and the picks from them (and from the mean of both) race as variants:
# our set carried 135 hit rating from items, 13.5% against the 8% cap of yellow and ranged attacks on raid bosses (_reference/forever-stats.md
# rule 3), where the weights, measured on the first pick, valued hit above agility (1.02 against 0.60); the site's items that trade hit for
# agility or attack power gained 0.3-1.0% each in six slots (head, neck, back, wrist, hands, feet). A linear weight cannot see a cap; the
# simulator's weights at the picked set can, and the race decides.
KNOWN_FILE = pathlib.Path.home() / ".wow-forever-tools" / "gear-research-1122" / "wowtbc_sets.json"   # outside the repository
KNOWN_SOURCE = "wowtbc.gg's Warcraft Forever BiS lists, read by the audit session 2026-11-22 (gear-research)"
KNOWN_ALIASES = {("hunter", "Survival"): ("survival-melee-hunter", "survival-hunter"), ("druid", "Feral Combat"): ("feral-dps-druid",),
                 ("druid", "Feral Bear"): ("feral-tank-druid",), ("paladin", "Hybrid Holy/Retribution"): ("shockadin-paladin",)}
# The enchant pool (the items' rules, applied to enchants; agreed with the audit session on 2026-11-22):
# - what Forever has now: the database's phase 1; the Raid BiS tier also takes Molten Core's and Onyxia's drops, which it marks phase 2
#   (Enchant Weapon - Spell Power, +30, and Healing Power: Molten Core formulas, so in no pre-raid tier);
# - a source: sold, a drop outside later raids, a craft, a quest or a reputation (gear_opt's later-content rules; the quests-and-dungeons
#   tier takes reputation to Honored). The phase field dates an enchant, so a vendor or quest entry counts, unlike an item's;
# - no source: a recipe Classic's trainers teach, or a preset of the tier uses it on that kind of item (the sourceless items' rule);
# - never a creature type's bonus (Beastslayer, Elemental Slayer, Demonslaying): the bench's target is an Elemental.
# Out of every tier whatever the database or a preset says (the audit session, 2026-11-22: "a known later-content source in Classic beats a
# preset's vetting", as LATER_PREFIXES and later_phase do for items; "a tie goes to the enchant with a known source"). Each is still raced
# where it fits and recorded with what it would have gained (`left_out`); the launch checklist asks whether enchanters have them.
ENCHANTS_OUT = {
    (7, 2564): "Enchant Gloves - Superior Agility (+15): Classic's Temple of Ahn'Qiraj formula (the database: phase 1, no source; upstream's "
               "phase-1 rogue presets use it)",
    (7, 2614): "Enchant Gloves - Shadow Power: Classic's Temple of Ahn'Qiraj formula",
    (7, 2615): "Enchant Gloves - Frost Power: Classic's Temple of Ahn'Qiraj formula",
    (7, 2616): "Enchant Gloves - Fire Power: Classic's Temple of Ahn'Qiraj formula",
    (7, 2617): "Enchant Gloves - Healing Power: Classic's Temple of Ahn'Qiraj formula",
    (4, 2622): "Enchant Cloak - Dodge: Classic's Temple of Ahn'Qiraj formula",
    (5, 7645): "Enchant Chest - Living Stats: Forever's, no source; Greater Stats (1891) plus Nature resistance, a tie for damage",
}
# Held until the audit session rules on a trace (2026-11-22): raced and recorded like ENCHANTS_OUT, never taken.
ENCHANTS_HELD = {
    (14, 8720): "SAF-T Ultra Precision Scope (2% ranged crit): the simulator's hunter pet takes the higher of its owner's melee and ranged "
                "crit (sim/hunter/pets.go inheritedCrit, upstream's evidence EV-0070), so the scope raises the pet's crit as well; held "
                "until the audit session's ruling on the trace",
}
SLAYERS = ("Beastslayer", "Elemental Slayer", "Demonslaying")
_ENCH = G.__dict__.setdefault("TIERS_ENCH", {})   # entries, vetted {"bis"|"prebis": {(item type, effect id)}}, taught: on the shared
                                                   # gear_opt module, so every copy of this file reads what load_enchants loaded (0q)


def norm17(items):
    return [dict(x) if x else {} for x in items] + [{}] * max(0, 17 - len(items))


def load_enchants(repo, db):
    """The database's enchants, the ones the tiers' presets use (by item type) and Classic's trainer recipes (load_db calls it)."""
    raw = json.load(open(pathlib.Path(repo) / "assets" / "database" / "db.json", encoding="utf-8"))
    entries = raw["enchants"]
    by = {}
    for e in entries:
        by.setdefault(e["effectId"], []).append(e)
    vet = {"bis": set(), "prebis": set()}
    for p in G.preset_files(repo):
        if "p2" in p.name or "phase_2" in p.name:
            continue
        its = json.load(open(p, encoding="utf-8")).get("items", [])
        ids = [x["id"] for x in its if x and x.get("id")]
        official = G.VENDORED_PRESETS not in p.parents
        tiers = ([] if official and any(db.get(i, {}).get("scalingOptions", {}).get("0", {}).get("ilvl", 0) > G.SOURCELESS_MAX_ILVL for i in ids)
                 else ["bis"]) + (["prebis"] if any(k in p.name for k in PRE_NAMES) else [])   # load_vetted's and load_vetted_pre's rules
        for slot, x in enumerate(its[:17]):
            for e in by.get((x or {}).get("enchant"), []):
                if G.SLOT_TYPE[slot] in enchant_types(e):
                    for t in tiers:
                        vet[t].add((e.get("type"), e["effectId"]))
    _ENCH.update(entries=entries, vetted=vet, taught=dungeon_data(repo)[2])


def enchant_types(e):
    return [e.get("type")] + list(e.get("extraTypes") or [])


def fits_enchant(e, it, slot):
    """Whether the enchant goes on the item in `slot`: the simulator UI's enchantAppliesToItem (ui/sim/proto/items.ts)."""
    if G.SLOT_TYPE[slot] not in enchant_types(e):
        return False
    et, wt, rt = e.get("enchantType") or 0, it.get("weaponType") or 0, it.get("rangedWeaponType") or 0
    if (et == 1 and it.get("handType") != 4) or (et == 4 and wt != 8) or (et == 2 and wt != 7) or ((et == 5) != (wt == 5)):
        return False
    if wt == 7 and et != 2:
        return False
    if e.get("type") == 14 and rt not in (1, 2, 3):
        return False
    return not (rt not in (0, 5) and e.get("type") != 14)


def enchant_ok(e, tier, zones):
    """Whether an enchant is in the tier's pool (see above). ENCHANTS_OUT and ENCHANTS_HELD are not."""
    key = (e.get("type"), e["effectId"])
    if key in ENCHANTS_OUT or key in ENCHANTS_HELD or any(s in e.get("name", "") for s in SLAYERS):
        return False
    # 2026-11-23: the three lists' enchant rules (raidsim/gear_lists.py ENCHANT_KINDS; Easy Pre-BiS: trainer-taught and quest modifiers)
    return (tier if tier in GL.LISTS else "prebis") in GL.enchant_lists(e, rules_ctx(zones))


def enchant_allowed(eid, item_type, tier, zones):
    """Whether an entry of effect `eid` goes on items of `item_type` and is in the tier's enchant pool: heal_gear.py and tank_gear.py
    filter their candidate lists (fill_enchants.HEALER_CANDIDATES, TANK_CANDIDATES) with it."""
    if not _ENCH.get("entries"):
        raise SystemExit("gear_tiers: no enchants loaded (load the database through gear_tiers.load_db first)")
    return any(e["effectId"] == eid and item_type in enchant_types(e) and enchant_ok(e, tier, zones) for e in _ENCH["entries"])


def slot_enchants(cls, it, slot, tier, zones):
    """(pool, out): the enchants the item in `slot` takes, for the class: the tier's pool, and ENCHANTS_OUT / ENCHANTS_HELD (raced for
    the record only). One entry per effect id (an effect id can carry two names on one kind of item: 7656)."""
    if not _ENCH.get("entries"):
        raise SystemExit("gear_tiers: no enchants loaded (load the database through gear_tiers.load_db first)")
    pool, out, seen = [], [], set()
    for e in _ENCH["entries"]:
        if e["effectId"] in seen or not fits_enchant(e, it, slot) or (e.get("classAllowlist") and G.CLASS_ID[cls] not in e["classAllowlist"]):
            continue
        if (e.get("type"), e["effectId"]) in ENCHANTS_OUT or (e.get("type"), e["effectId"]) in ENCHANTS_HELD:
            if not any(s in e.get("name", "") for s in SLAYERS):
                out.append(e)
                seen.add(e["effectId"])
        elif enchant_ok(e, tier, zones):
            pool.append(e)
            seen.add(e["effectId"])
    return pool, out


def static_enchant(e):
    """Stats only (the weights value it whole): no proc, effect, pseudo-stat or weapon damage."""
    return not (e.get("procKind") or e.get("enchantEffects") or any(e.get("pseudoStats") or []) or e.get("weaponDamage"))


def enchant_value(e, w):
    return sum(w.get(G.STAT.get(i), 0.0) * x for i, x in enumerate(e.get("stats") or []) if x)


DEFENSIVE_PSEUDO = {3, 4, 5, 16, 23, 26}   # PseudoStat block value, dodge, parry, block, block per Strength, crit taken


def raced_enchant(e, tank=False):
    """An enchant the weights cannot value, worth racing: an effect, a combat proc, a pseudo-stat or weapon damage; for a damage dealer
    no absorb-or-heal proc and no enchant whose only pseudo-stats are defensive (Arcanum of Protection). Enchants that do nothing in a
    fight (Minor Speed, the gathering ones) are neither raced nor stat picks."""
    if static_enchant(e):
        return False
    if tank:
        return True
    if (e.get("procKind") or 0) == 2:
        return False
    ps = {i for i, v in enumerate(e.get("pseudoStats") or []) if v}
    return not (ps and ps <= DEFENSIVE_PSEUDO and not (e.get("procKind") or e.get("enchantEffects") or e.get("weaponDamage")
                                                       or any(e.get("stats") or [])))


def stat_pick(pool, w, cur=None):
    """The slot's stat enchant worth most by the weights, worth more than 0; the current one when it is worth as much."""
    st = [e for e in pool if static_enchant(e) and enchant_value(e, w) > 1e-9]
    if not st:
        return None
    best = max(st, key=lambda e: enchant_value(e, w))
    c = next((e for e in st if e["effectId"] == cur), None)
    return c if c is not None and enchant_value(c, w) >= enchant_value(best, w) - 1e-9 else best


def racer(evals, repo, sc, tag):
    """race(sets {name: items}, fights, seed) -> {name: score relative to the first set}, averaged over the evaluations."""
    sc = sc or (lambda row: row.get("dps") or 0)

    def race(sets, its, seed):
        out = {k: [] for k in sets}
        for name, e, where, tal, lab in evals:
            rows = G.run_bench(repo, G.bench_cfg(e, repo, [{"label": k, "talents": tal, "gear_json": {"items": v}} for k, v in sets.items()], its, seed, where), f"r-{tag}")
            ref = rows[next(iter(sets))]
            for k in sets:
                out[k].append(sc(rows[k]) / (sc(ref) or 1))
        return {k: sum(v) / len(v) for k, v in out.items()}
    return race


def race_weapons(cls, items, w, greedy, race, its, db):
    """G2: the weapon of each hand whose dps the weights value (and a hunter's ranged weapon) raced in the set on seed 1: the slot's
    best `WEAPON_TOP` items by the weights plus any with an effect among the best `WEAPON_EFFECTS_FROM` (greedy.weapon_candidates), each
    with the slot's enchant; the main hand, then the off hand, then the main hand's pass-1 best `WEAPON_RERACE` again when the off hand
    changed. A candidate is taken when ahead. Returns (items, record)."""
    items = norm17(items)
    rec, first = [], {}
    hands = [(14, "PseudoStatMainHandDps"), (15, "PseudoStatOffHandDps")] + ([(16, "PseudoStatRangedDps")] if cls == "hunter" else [])
    passes = [(s, None) for s, k in hands if w.get(k, 0.0) > WEAPON_DPS_MIN]
    i = 0
    while i < len(passes):
        slot, only = passes[i]
        i += 1
        cur = items[slot].get("id")
        cands = only if only is not None else greedy.weapon_candidates(items, w, slot, WEAPON_TOP, WEAPON_EFFECTS_FROM)
        cands = [c for c in cands if c != cur]
        if not cands:
            continue
        sets = {"current": items}
        for c in cands:
            x = [dict(y) for y in items]
            ench = items[slot].get("enchant")
            x[slot] = {"id": c, **({"enchant": ench} if ench else {})}
            sets[str(c)] = x
        r = race(sets, its, 1)
        best = max(r, key=r.get)
        if only is None:
            first[slot] = sorted((c for c in r if c != "current"), key=lambda c: -r[c])[:WEAPON_RERACE]
        rec.append({"slot": slot, "pass": "again" if only is not None else 1, "from": G.item_name(db, cur),
                    "to": G.item_name(db, int(best)) if best != "current" else G.item_name(db, cur),
                    "race_seed1": {("current" if k == "current" else G.item_name(db, int(k))): round(v, 4) for k, v in sorted(r.items(), key=lambda kv: -kv[1])}})
        if best != "current" and r[best] > 1.0:
            items = sets[best]
            if slot == 15 and 14 in first:   # the off hand changed: the main hand's pass-1 best again, next to it
                again = [int(c) for c in first[14] if int(c) != items[15].get("id")]
                # and the item the off hand gave up, when it fits the main hand (2026-11-23, the audit session's Alliance finding: the
                # greedy pass put the Premier Grand Marshal's Longsword in the Alliance Survival set's off hand, tied by the weights
                # with the Dirk it put in the main hand, so the main hand's race never had it; the off hand took Distracting Dagger,
                # and the Longsword in the main hand is 2.2% ahead of the Dal'Rend's Sacred Charge the set kept, 1000.3 / 999.2
                # against 979.0 / 979.4)
                mh = db.get(items[14].get("id")) if items[14].get("id") else None
                if cur and cur in db and cur != items[14].get("id") and cur not in again and greedy.fits(db[cur], 14, mh):
                    again.append(cur)
                passes.append((14, again))
    return items, rec


_SET_STEPS = {}


def sim_set_steps(repo):
    """{set id: {"name", "steps"}}: the bonus steps the simulator at `repo` registers for each item set (its Go NewItemSet calls and the
    helpers that call it with an id and a name), read once per checkout (2026-11-23). A set the database lists and this does not has no
    simulated bonus."""
    import re
    key = str(repo)
    if key in _SET_STEPS:
        return _SET_STEPS[key]
    sets, helpers, texts = {}, {}, {}
    for f in (pathlib.Path(repo) / "sim").rglob("*.go"):
        texts[f] = f.read_text(encoding="utf-8", errors="replace")
    for f, t in texts.items():
        for m in re.finditer(r"core\.NewItemSet\(core\.ItemSet\{", t):
            i, depth = m.end(), 1
            while depth and i < len(t):
                depth += {"{": 1, "}": -1}.get(t[i], 0)
                i += 1
            block = t[m.end():i]
            keys = []
            bm = re.search(r"Bonuses:\s*map\[int32\][\w.]+\{", block)
            if bm:
                j, d2 = bm.end(), 1
                while d2 and j < len(block):
                    d2 += {"{": 1, "}": -1}.get(block[j], 0)
                    j += 1
                depth2 = 0
                for line in block[bm.end():j].splitlines():
                    km = re.match(r"\s*(\d+):", line) if depth2 == 0 else None
                    if km:
                        keys.append(int(km.group(1)))
                    depth2 += line.count("{") - line.count("}")
            idm, nm = re.search(r"\bID:\s*(\d+)", block), re.search(r'\bName:\s*"([^"]+)"', block)
            if idm:
                sets[int(idm.group(1))] = {"name": nm.group(1) if nm else None, "steps": sorted(set(keys))}
            else:
                fm = list(re.finditer(r"func (\w+)\(id int32, name string\)", t[:m.start()]))
                if fm:
                    helpers[fm[-1].group(1)] = sorted(set(keys))
    for f, t in texts.items():
        for h, keys in helpers.items():
            for m in re.finditer(h + r'\((\d+),\s*"([^"]+)"\)', t):
                sets[int(m.group(1))] = {"name": m.group(2), "steps": keys}
    # the second path (2026-11-23, the audit session's Devilsaur contradiction: Gauntlets and Leggings together were 0.8-0.96% more than
    # apart on two seeds): sets generated from the item-set data, shared.NewParsedItemSet(id, "name", slots, map[int32][]int32{k: {...}})
    # in sim/common/forever/item_sets_auto_gen.go; a step upstream leaves for manual implementation is a comment line ("// 2: {...}")
    for f, t in texts.items():
        for m in re.finditer(r'NewParsedItemSet\((\d+),\s*"([^"]+)"', t):
            mm = re.compile(r"map\[int32\]\[\]int32\{").search(t, m.end())
            if not mm:
                continue
            j, d2 = mm.end(), 1
            while d2 and j < len(t):
                d2 += {"{": 1, "}": -1}.get(t[j], 0)
                j += 1
            keys = []
            for line in t[mm.end():j].splitlines():
                s = line.strip()
                km = None if s.startswith("//") else re.match(r"(\d+):\s*\{", s)
                if km:
                    keys.append(int(km.group(1)))
            sid = int(m.group(1))
            if sid not in sets:   # a hand-written set wins (upstream: "A set written by hand leaves this file on the next db run")
                sets[sid] = {"name": m.group(2), "steps": sorted(set(keys)), "generated": True}
    _SET_STEPS[key] = sets
    return sets


def race_set_pieces(cls, items, w, greedy, race, its, db, pool, repo=None, confirm=None):
    """G3, widened on 2026-11-23 (the user: "fix looking at sets for their bonuses and not just looking at set pieces individually"; the
    audit session's item 2): every bonus step the simulator registers for an item set (sim_set_steps) that the pool's pieces can reach
    races as a unit, whatever it costs by the weights: the pieces of the set the set already wears plus the fewest more to reach the
    step, those that cost least by the weights, with the slots around them kept legal (a two-hander empties the off hand; a piece that
    clashes with another slot's unique item leaves the unit out). Every unit races on seed 1; the best is taken when ahead, and the steps
    are measured once more from it (a step taken can open the next). A pool set the simulator gives no bonus races nothing and the
    record names it (the game may give a bonus the simulator lacks: part of the effects work). Frost's True Pre-BiS had held four
    Sorcerer's Regalia pieces, and the site's Crown and Mantle completing six, each worse alone (-0.5% to -0.8%), were +0.5% / +0.6%
    together; the old rule raced all of a set's pieces or its two cheapest. Trinkets race on their own (screen_trinkets). Returns
    (items, record {units, no_bonus, taken}). A unit is taken only when it is ahead on seed 2 as well (2026-11-23, the audit session: with
    15 to 48 units a class at 1,000 fights, the best of the noise is above 1.0 more often than not when a few units cost almost nothing):
    the top three by seed 1, each ahead there, race the current set on seed 2 at `confirm` fights (the make's confirm; `its` without it),
    and the best of them there is taken when ahead of the current set; those three keep both seeds."""
    steps_of = sim_set_steps(repo) if repo else {}
    rec = {"units": [], "no_bonus": [], "taken": []}
    for rnd in (1, 2):
        items = norm17(items)
        held_ids = {x.get("id") for x in items if x.get("id")}
        by = {}
        for it in db.values():
            sid = it.get("setId")
            if not sid or not pool(it):
                continue
            for slot in range(17):
                if G.SLOT_TYPE[slot] == 12 or G.SLOT_TYPE[slot] != it.get("type"):
                    continue
                shape = db.get(items[slot].get("id")) if items[slot].get("id") else None
                if swap_fits(greedy, it, slot, shape):
                    by.setdefault(sid, {}).setdefault(slot, []).append(it)
        units = []
        for sid, slots in by.items():
            name = next(iter(slots.values()))[0].get("setName") or str(sid)
            wearing = {s for s in range(17) if (db.get(items[s].get("id")) or {}).get("setId") == sid}
            held = len(wearing)
            if len({it["id"] for v in slots.values() for it in v} | {items[s]["id"] for s in wearing}) < 2:
                continue
            st = (steps_of.get(sid) or {}).get("steps") or []
            if sid in steps_of and not st:   # registered, every step left for manual implementation: no simulated bonus
                if rnd == 1 and name not in rec["no_bonus"]:
                    rec["no_bonus"].append(name)
                continue
            if sid not in steps_of:   # the safety net (2026-11-23, the audit session): a set the parser does not know races as before
                # the rewrite, all its pool pieces as one unit and its two cheapest as another; the race judges whether a bonus exists
                free = {s for s in slots if s not in wearing}
                st = sorted({k for k in (2, held + len(free)) if k > held})
                if rnd == 1 and name not in rec.setdefault("unknown_to_parser", []):
                    rec["unknown_to_parser"].append(name)
            for k in st:
                if k <= held:
                    if rnd == 1:
                        rec["units"].append({"set": name, "step": k, "raced": False, "why": f"worn already ({held} pieces)"})
                    continue
                cand = []
                for slot, v in slots.items():
                    if slot in wearing:
                        continue
                    best = max(v, key=lambda it, s=slot: G.value(it, w, s))
                    cur = db.get(items[slot].get("id")) if items[slot].get("id") else None
                    cand.append(((G.value(cur, w, slot) if cur else 0.0) - G.value(best, w, slot), slot, best))
                cand.sort(key=lambda c: c[0])
                pick, used = [], set()
                for loss, slot, it in cand:
                    if it["id"] in used or it["id"] in held_ids or any(s == slot for s, _ in pick):
                        continue
                    pick.append((slot, it))
                    used.add(it["id"])
                    if len(pick) == k - held:
                        break
                if len(pick) < k - held:
                    if rnd == 1:
                        rec["units"].append({"set": name, "step": k, "raced": False, "why": f"the pool reaches {held + len(pick)} pieces"})
                    continue
                x = [dict(y) for y in items]
                for slot, it in pick:
                    ench = x[slot].get("enchant")
                    x[slot] = {"id": it["id"], **({"enchant": ench} if ench else {})}
                if any(s == 14 and it.get("handType") == 4 for s, it in pick):
                    x[15] = {}
                ukeys, clash = set(), False
                for y in x:
                    if y.get("id"):
                        kk = G.unique_keys(db.get(y["id"]))
                        clash = clash or bool(kk & ukeys)
                        ukeys |= kk
                if clash:
                    if rnd == 1:
                        rec["units"].append({"set": name, "step": k, "raced": False, "why": "a piece clashes with a unique item the set wears"})
                    continue
                units.append((name, k, held, x, [it["name"] for _, it in pick], round(sum(l for l, _, _ in cand[:len(pick)]), 2)))
        units = units[:SET_RACE_MAX]
        if not units:
            break
        sets = {"current": items}
        for name, k, held, x, pieces, loss in units:
            sets[f"{name} ({k})"] = x
        r = race(sets, its, 1)
        top = [k for k in sorted((k for k in r if k != "current"), key=lambda k: -r[k])[:3] if r[k] > 1.0]
        r2 = race({"current": items, **{k: sets[k] for k in top}}, confirm or its, 2) if top else {}
        for name, k, held, x, pieces, loss in units:
            lab = f"{name} ({k})"
            rec["units"].append({"set": name, "step": k, "held": held, "pieces": pieces, "weights_loss": loss, "raced": True,
                                 "round": rnd, "race_seed1": round(r[lab], 4), **({"race_seed2": round(r2[lab], 4)} if lab in r2 else {}),
                                 **({"unknown_to_parser": True} if name in rec.get("unknown_to_parser", []) else {})})
        best = max(top, key=lambda k: r2.get(k, 0.0)) if top else None
        if best and r2.get(best, 0.0) > 1.0:
            items = sets[best]
            rec["taken"].append(best)
        else:
            break
    return items, rec


_SBI = {}


def _set_bonus_inventory():
    """{set id: {"set", "bonuses"}} from raidsim/set-bonus-inventory.json (the True BiS list holds every list's sets), or {}."""
    if "x" not in _SBI:
        p = HERE / "set-bonus-inventory.json"
        rows = json.load(open(p, encoding="utf-8"))["lists"]["bis"]["sets"] if p.exists() else []
        _SBI["x"] = {r["id"]: r for r in rows}
    return _SBI["x"]


def set_check(items, db, repo, active):
    """The simulator's sheet against the parser (2026-11-23, the audit session's guard on sim_set_steps): every step the set's pieces
    reach (sim_set_steps) must be active on the sheet (stats_bench's `sets`, "<name> (<k>pc)"), and every active set must be a step the
    parser knows. A miss means the parser reads a step the simulator does not apply, or misses one it does: a warning in the record,
    printed by make_lists at the end of each phase."""
    if active is None:
        return {"warning": "no sheet: the hit report did not run"}
    steps = sim_set_steps(repo)
    worn = {}
    for x in norm17(items):
        sid = (db.get(x.get("id")) or {}).get("setId") if x and x.get("id") else None
        if sid:
            worn[sid] = worn.get(sid, 0) + 1
    expected = sorted(f"{steps[sid]['name']} ({k}pc)" for sid, n in worn.items() if sid in steps for k in steps[sid]["steps"] if k <= n)
    # the worn sets the simulator gives no bonus (2026-11-23, the audit session: transparency in the first pass): each step the pieces
    # reach in game, and a plain-stat step one piece short, from the client's tables (set_bonus_inventory.py's record)
    unsim = []
    inv = _set_bonus_inventory()
    for sid, n in worn.items():
        if sid not in inv:
            continue
        simulated = set((steps.get(sid) or {}).get("steps") or [])   # a step the simulator applies is not "unsimulated" (step by step)
        bs = [b for b in inv[sid]["bonuses"] if b["pieces"] not in simulated]
        if not bs:
            continue
        reached = [{"pieces": b["pieces"], "kind": b["kind"], "text": b["text"]} for b in bs if b["pieces"] <= n]
        short = [{"pieces": b["pieces"], "text": b["text"]} for b in bs if b["kind"] == "plain" and b["pieces"] == n + 1]
        if reached or short:
            unsim.append({"set": inv[sid]["set"], "worn": n, "reached": reached, "one_short": short})
    missing = [s for s in expected if s not in active]
    unexpected = [s for s in active if s not in expected]
    out = {"expected": expected, "active": list(active), **({"unsimulated": unsim} if unsim else {}),
           **({"unknown_to_parser": unexpected} if unexpected else {})}
    if missing or unexpected:
        out["warning"] = ("the sheet lacks " + ", ".join(missing) if missing else "") + ("; " if missing and unexpected else "") + \
                         ("the sheet has steps the parser does not know: " + ", ".join(unexpected) if unexpected else "")
    return out


EFFECT_SLOTS = {"trinket": (12, 13), "ring": (10, 11), "neck": (1,), "back": (3,), "ranged/relic": (16,), "weapon": (14, 15)}
EFFECT_MIN = 0.995   # a screened item races in a make when its screen score is at least this (the screen's set is not the make's)
EFFECT_TOP = {"trinket": 6, "ring": 4, "weapon": 6, "neck": 3, "back": 3, "ranged/relic": 3}
EFFECT_DIR = HERE / "effect-screen"


def effect_variants(it, base, db, greedy):
    """[(label "<id>@<slot>", items)]: the item in each scope slot it fits (both trinket slots, both rings, main hand and off hand), the
    slot's enchant kept when the slot held an item of the same type; a two-hander empties the off hand; none when the set wears the item
    already or a unique item would clash (2026-11-23, 3b: effect_screen.py and race_effect_items)."""
    out = []
    if any(x.get("id") == it["id"] for x in base):
        return out
    for g, slots in EFFECT_SLOTS.items():
        for s in slots:
            if G.SLOT_TYPE[s] != it.get("type"):
                continue
            cur = db.get(base[s].get("id")) if base[s].get("id") else None
            # a weapon or ranged slot swaps only where the set holds an item of that shape (2026-11-23: the Balance screen had put Hand of
            # Edward the Odd in the empty off hand next to a two-handed staff, +8.8% for an impossible set; swap_fits, race_set_pieces' rule)
            if not swap_fits(greedy, it, s, cur):
                continue
            x = [dict(y) for y in base]
            ench = x[s].get("enchant") if cur and cur.get("type") == it.get("type") else None
            x[s] = {"id": it["id"], **({"enchant": ench} if ench else {})}
            if s == 14 and it.get("handType") == 4:
                x[15] = {}
            keys, clash = set(), False
            for y in x:
                if y.get("id"):
                    k = G.unique_keys(db.get(y["id"]))
                    clash = clash or bool(k & keys)
                    keys |= k
            if not clash:
                out.append((f"{it['id']}@{s}", x))
    return out


def effect_screen_of(cls, spec):
    """The spec's 3b screen (raidsim/effect-screen/<class>-<spec slug>.json, effect_screen.py), or None."""
    p = EFFECT_DIR / f"{cls}-{SM.slug(spec)}.json"
    return json.load(open(p, encoding="utf-8")) if p.exists() else None


def race_effect_items(cls, items, greedy, race, its, db, pool, screen, confirm=None):
    """3b in the make (2026-11-23, the user: "correctly test things like trinkets or rings or weapons ... that has proc chances"): the
    screen's items with a modelled proc or on-use (score at least EFFECT_MIN in the screen's set, the best EFFECT_TOP of each slot group,
    in this list's pool) are swapped into this set in every scope slot they fit and raced on seed 1; the top three ahead race the current
    set on seed 2 at the confirm's fights, and the best there is taken when ahead; then once more from it. Returns (items, record)."""
    rec = {"screen": (screen or {}).get("base"), "screen_commit": (screen or {}).get("commit"), "units": [], "taken": []}
    if not screen:
        rec["why"] = "no effect screen for the spec"
        return items, rec
    rows = [r for r in screen.get("rows") or [] if r.get("score", 0) >= EFFECT_MIN and r["id"] in db and pool(db[r["id"]])]
    by = {}
    for r in sorted(rows, key=lambda r: -r["score"]):
        by.setdefault(r["group"], []).append(r)
    pick = [r for g, rs in by.items() for r in rs[:EFFECT_TOP.get(g, 3)]]
    rec["candidates"] = [{"name": r["name"], "group": r["group"], "screen": r["score"]} for r in pick]
    for rnd in (1, 2):
        items = norm17(items)
        sets = {"current": items}
        for r in pick:
            for lab, x in effect_variants(db[r["id"]], items, db, greedy):
                sets[f"{r['name']} @{lab.split('@')[1]}"] = x
        if len(sets) == 1:
            break
        r1 = race(sets, its, 1)
        top = [k for k in sorted((k for k in r1 if k != "current"), key=lambda k: -r1[k])[:3] if r1[k] > 1.0]
        r2 = race({"current": items, **{k: sets[k] for k in top}}, confirm or its, 2) if top else {}
        for k in sets:
            if k != "current":
                rec["units"].append({"swap": k, "round": rnd, "race_seed1": round(r1[k], 4), **({"race_seed2": round(r2[k], 4)} if k in r2 else {})})
        best = max(top, key=lambda k: r2.get(k, 0.0)) if top else None
        if best and r2.get(best, 0.0) > 1.0:
            items = sets[best]
            rec["taken"].append(best)
        else:
            break
    return items, rec


def enchants_for(cls, items, w, tier, zones, db, emap=None, own_first=False):
    """The set's enchants within the tier's pool: per slot the enchant of `emap` ({slot: effect id}) when it goes on the item, else the
    slot's own when the tier allows it, else the slot's stat pick by the weights (an enchant the tier does not allow never stays).
    `own_first` (2026-11-23, the audit session's ruling on the ladder guard: a lower list's set competes as it was made, and a known
    positive as its source lists it): the slot's own enchant first when the tier allows it, then `emap`'s, then the stat pick."""
    items = norm17(items)
    for slot in range(17):
        x = items[slot]
        it = db.get(x.get("id")) if x.get("id") else None
        if not it:
            continue
        pool, _ = slot_enchants(cls, it, slot, tier, zones)
        ids = {e["effectId"] for e in pool}
        want = (emap or {}).get(slot)
        if own_first and x.get("enchant") in ids:
            pass
        elif want in ids:
            x["enchant"] = want
        elif x.get("enchant") in ids:
            pass
        else:
            sp = stat_pick(pool, w)
            if sp:
                x["enchant"] = sp["effectId"]
            else:
                x.pop("enchant", None)
    return items


def choose_enchants(cls, items, w, tier, zones, race, its, db, tank=False):
    """G1: enchant maps for the set ({slot: effect id}). Per slot an anchor: the slot's own enchant when the tier allows it and it is a
    raced kind (raced_enchant: Crusader, a scope, Arcanum of Rapidity), else the stat pick by the weights (stat_pick: ties keep the own
    enchant), else the own enchant when the tier allows it (nothing worth more), else none; the anchors are the stat map. Then every raced
    enchant of the slot and its stat pick, each against the anchors in one bench call on seed 1 (`its` fights); the best per slot is taken
    when ahead (the raced map). Weapon-damage enchants race only the strongest of them. ENCHANTS_OUT and ENCHANTS_HELD that fit are raced
    too and recorded with their gain over the slot's choice, never taken. Returns (stat map, raced map, record); the caller confirms on
    seed 2 (enchants_for puts a map on a set)."""
    items = norm17(items)
    anchor, statmap, cands, outs = {}, {}, {}, {}
    for slot in range(17):
        x = items[slot]
        it = db.get(x.get("id")) if x.get("id") else None
        if not it:
            continue
        pool, out = slot_enchants(cls, it, slot, tier, zones)
        if not pool and not out:
            continue
        by = {e["effectId"]: e for e in pool}
        sp = stat_pick(pool, w, x.get("enchant"))
        own = by.get(x.get("enchant"))
        own_raced = own is not None and raced_enchant(own, tank)
        statmap[slot] = (own["effectId"] if own_raced else sp["effectId"] if sp else own["effectId"] if own else None)
        anchor[slot] = statmap[slot]
        rc = [e for e in pool if raced_enchant(e, tank)]
        wd_only = [e for e in rc if e.get("weaponDamage") and not (e.get("procKind") or e.get("enchantEffects") or any(e.get("pseudoStats") or []))]
        top_wd = max(wd_only, key=lambda e: e["weaponDamage"]) if wd_only else None
        c = [e["effectId"] for e in rc if e not in wd_only or e is top_wd]
        if sp:
            c.append(sp["effectId"])
        cands[slot] = [eid for eid in dict.fromkeys(c) if eid != anchor[slot]]
        outs[slot] = [e for e in out if raced_enchant(e, tank) or enchant_value(e, w) > 1e-9]
    base = [dict(y) for y in items]
    for slot, eid in anchor.items():
        if eid:
            base[slot]["enchant"] = eid
        else:
            base[slot].pop("enchant", None)
    sets = {"anchor": base}
    for slot in anchor:
        for eid in cands[slot] + [e["effectId"] for e in outs[slot]]:
            x = [dict(y) for y in base]
            x[slot]["enchant"] = eid
            sets[f"{slot}:{eid}"] = x
    ename = lambda eid: next((e["name"] for e in _ENCH["entries"] if e["effectId"] == eid), str(eid)) if eid else None  # noqa: E731
    rec = {"slots": {}, "left_out": []}
    raced = dict(anchor)
    r = race(sets, its, 1) if len(sets) > 1 else {"anchor": 1.0}
    for slot in anchor:
        sc = {anchor[slot]: 1.0, **{eid: r[f"{slot}:{eid}"] for eid in cands[slot]}}
        best = max(sc, key=sc.get)
        raced[slot] = best if sc[best] > 1.0 else anchor[slot]
        row = {"item": G.item_name(db, items[slot].get("id")), "own": ename(items[slot].get("enchant")), "stat_pick": ename(statmap[slot]),
               "chosen_seed1": ename(raced[slot])}
        if cands[slot]:
            row["race_seed1"] = {ename(k): round(v, 4) for k, v in sorted(sc.items(), key=lambda kv: -kv[1])}
        rec["slots"][str(slot)] = row
        for e in outs[slot]:
            g = r[f"{slot}:{e['effectId']}"] - sc[raced[slot]]
            key = (e.get("type"), e["effectId"])
            rec["left_out"].append({"slot": slot, "enchant": e["name"], "gain_over_choice_seed1": round(g, 4),
                                    "why": ENCHANTS_OUT.get(key) or ENCHANTS_HELD.get(key)})
    return statmap, raced, rec


def refit(cls, spec, tier, entry_name, talents, label, repo, db, zones, a, path=None, setting="raid", write=True):
    """The three steps on a tier set file as it stands (2026-11-22, the audit session's G1-G3 on the sets made on 2026-11-21/22), much
    cheaper than make(): no greedy pass, no trinket screen. Weights on the filed set, weapons raced, set pieces raced, enchants chosen;
    then four sets raced on seed 2 (`a.confirm` fights): the filed set with its tier's enchants (an enchant its tier does not allow
    replaced by the slot's stat pick, even at a loss), the filed items with the stat picks and with the raced map, and the refit set with
    the raced map. The best is written. Returns the record (make()'s keys plus weapons, set_pieces, enchants, refit)."""
    e = R.SPECS[cls][entry_name]
    easy_check(tier, db, zones, repo)
    p = path or set_path(cls, spec, tier)
    filed = norm17(json.load(open(p, encoding="utf-8"))["items"])
    pool = pool_of(tier, zones, repo)
    _, _, greedy = G.class_picker(repo, cls, db, pool)
    tag = f"refit-{cls}-{SM.slug(spec)}-{tier}"
    race = racer([(entry_name, e, setting, talents, label)], repo, None, tag)
    row = G.run_bench(repo, G.bench_cfg(e, repo, [{"label": "w", "talents": talents, "gear_json": {"items": filed}}], a.weight_iterations, 1,
                                        setting, statweights=True), f"w-{tag}")["w"]
    if row.get("error"):
        raise SystemExit(f"stat weights failed for {tag}: {row['error']}")
    w = row["weights"]
    t0 = time.time()
    items, wrec = race_weapons(cls, filed, w, greedy, race, a.iterations, db)
    items, srec = race_set_pieces(cls, items, w, greedy, race, a.iterations, db, pool, repo=repo, confirm=a.confirm)
    statmap, raced, erec = choose_enchants(cls, items, w, tier, zones, race, a.iterations, db)
    sets = {"filed": enchants_for(cls, filed, w, tier, zones, db)}
    for name, its_, m in (("filed, stat enchants", filed, statmap), ("filed, raced enchants", filed, raced), ("refit", items, raced)):
        x = enchants_for(cls, its_, w, tier, zones, db, m)
        if all(x != v for v in sets.values()):
            sets[name] = x
    r2 = race(sets, a.confirm, 2) if len(sets) > 1 else {"filed": 1.0}
    chosen = max(r2, key=r2.get)
    out = sets[chosen]
    allowed = sets["filed"] == filed
    if out != filed and write:
        p.write_text(json.dumps({"items": out}, indent=1) + "\n", encoding="utf-8")
    ilvl = round(sum(db[x["id"]]["scalingOptions"]["0"].get("ilvl", 0) for x in out if x.get("id") in db)
                 / max(1, sum(1 for x in out if x.get("id") in db)), 1)
    changes = [{"slot": i, "from": G.item_name(db, filed[i].get("id")), "to": G.item_name(db, out[i].get("id")),
                "enchant_from": filed[i].get("enchant"), "enchant_to": out[i].get("enchant")}
               for i in range(17) if filed[i] != out[i]]
    print(f"  refit {p.name}: chosen {chosen} (seed 2: " + ", ".join(f"{k} {v:.4f}" for k, v in r2.items()) + f"); {len(changes)} slots changed"
          + ("" if allowed else "; the filed set held an enchant its tier does not allow") + f"; {(time.time() - t0) / 60:.1f} min", flush=True)
    for c in changes:
        print(f"    slot {c['slot']}: {c['from']} ({c['enchant_from']}) -> {c['to']} ({c['enchant_to']})", flush=True)
    return {"entry": entry_name, "gear": p.relative_to(ROOT).as_posix(), "date": TODAY, "setting": setting, "chosen": chosen, "ilvl": ilvl,
            "items": out, "names": [db.get(x.get("id"), {}).get("name") if x.get("id") else None for x in out],
            "weights": {k: round(v, 4) for k, v in w.items() if abs(v) > 1e-6}, "confirm_seed2": {k: round(v, 4) for k, v in r2.items()},
            "weapons": wrec, "set_pieces": srec, "enchants": erec, "changes": changes,
            **list_fields(cls, out, w, tier, db, zones, repo, pool),
            "refit": {"date": TODAY, "why": "the audit session's gear findings G1-G3 (2026-11-22): weapons raced per hand, item-set pieces "
                      "raced, enchants from the database by the tier's rules", "filed_enchants_allowed": allowed,
                      "iterations": a.iterations, "confirm": a.confirm}}


LADDER_MARGIN = 0.005   # a lower list's set this close to the seed-1 leader races again on seed 2 (optimize_set's ladder guard)
KNOWN_MARGIN = 0.002    # a known positive replaces the picker's best only when this far ahead of it on seed 2 (2026-11-23)
CLOSE_CALL = 0.002      # a make whose chosen set leads the best set that lost on the confirm by less is a close call (2026-11-23)
# the record fields every list's make keeps (2026-11-23: ml_pipeline.gear, dungeon_tier and make_lists read this one tuple)
LIST_RECORD_FIELDS = ("chosen_source", "ladder_case", "ladder", "known_tie", "picker_best", "known_positives", "competitors", "bases",
                      "reweigh", "hit", "set_check", "budget", "confirm_margin", "guard", "refused", "without_pvp", "side", "effect_items",
                      "racials_off", "enchant_consistency")


def known_lists(cls, spec):
    """The known positives of a spec (2026-11-23, the audit session's ruling on the list test's finding 2a: the site's lists compete in
    every make, the same rule as the simulator's presets in the talent races): ({name: {"items", "source"}}, why there is none). Every
    list the site has for the spec (KNOWN_ALIASES, else "<spec slug>-<class>"), from KNOWN_FILE (outside the repository; none when the
    file is not on this machine)."""
    if not KNOWN_FILE.exists():
        return {}, "no known positive (the site's lists are not on this machine)"
    data = json.load(open(KNOWN_FILE, encoding="utf-8"))
    out = {}
    for key in KNOWN_ALIASES.get((cls, spec), (f"{SM.slug(spec)}-{cls}",)):
        for variant, v in (data.get(key) or {}).items():
            if isinstance(v, dict) and v.get("items"):
                out[f"wowtbc {key} {variant}"] = {"items": norm17(v["items"]), "source": v.get("url") or KNOWN_SOURCE}
    return out, (None if out else f"no known positive (the site has no list for {cls} {spec})")


def pool_swap(items, w, greedy, db, pool, base):
    """A known positive inside the list's pool (2026-11-23, the same ruling: only items that pass the list's pool): each item the pool
    does not admit, or the database lacks, replaced by the best item by the weights `w` that fits the slot and the pool (greedy.fits:
    the way gear_lists.pvp_alternatives replaces a PvP item); a trinket by the picker's raced trinket (`base`); an empty slot filled
    from `base`. Unique-equipped items and limit categories once, slot by slot. Returns (items, [{slot, from, to, how}])."""
    work, base = norm17(items), norm17(base)
    swaps = []
    for slot in range(17):
        x = work[slot]
        it = db.get(x.get("id")) if x.get("id") else None
        if slot == 15 and (db.get(work[14].get("id")) or {}).get("handType") == 4:   # no off hand next to a two-hander
            if x.get("id"):
                work[15] = {}
                swaps.append({"slot": 15, "from": it.get("name") if it else x["id"], "to": None, "how": "the main hand is a two-hander"})
            continue
        taken = GL._taken(work, slot, db, G)
        if it is not None and pool(it) and not (GL._uses(it, G) & taken):
            continue
        if not x.get("id") and not base[slot].get("id"):
            continue   # (an empty slot our set leaves empty too)
        alt, how = None, None
        if slot in (12, 13) or not x.get("id"):
            for b in ([base[slot], base[25 - slot]] if slot in (12, 13) else [base[slot]]):
                bi = db.get(b.get("id")) if b.get("id") else None
                if bi is not None and pool(bi) and not (GL._uses(bi, G) & taken):
                    alt, how = bi, ("the picker's trinket" if slot in (12, 13) else "the picker's item (the list leaves the slot empty)")
                    break
        else:
            shape = it or (db.get(base[slot].get("id")) if base[slot].get("id") else None)
            best = None
            for cand in db.values():
                if not greedy.fits(cand, slot, shape) or GL._uses(cand, G) & taken:
                    continue
                v = G.value(cand, w, slot)
                if best is None or v > best[0]:
                    best = (v, cand)
            if best:
                alt, how = best[1], "the best in the pool by the weights"
        frm = it.get("name") if it else (f"item {x['id']} (not in the database)" if x.get("id") else None)
        if alt is None:
            swaps.append({"slot": slot, "from": frm, "to": None, "how": "no item fits"})
            continue
        ench = x.get("enchant")
        work[slot] = {"id": alt["id"], **({"enchant": ench} if ench else {})}
        swaps.append({"slot": slot, "from": frm, "to": alt.get("name"), "how": how})
    return work, swaps


def optimize_set(cls, evals, cur_items, pool, repo, db, a, tag, keep_current, weights_fn=None, score=None, extra=None, refine=None,
                 zones=None, tank=False, ladder=(), known=None, no_known=None, effect_screen=None):
    """The best set for the evaluations [(entry name, entry, setting, talents, label)] from `pool`: the same steps as gear_opt.optimize
    (weights, greedy per slot in two variants, weights again, trinket pairs raced, variants raced, seed-2 confirmation), except that the
    current item of a slot competes only when `keep_current` or the pool admits it (a pre-raid set must not keep raid items).
    `weights_fn(items)` -> {stat name: value per point} and `score(bench row)` -> float replace the simulator's DPS weights and DPS (both
    None for damage specs, unchanged; tank_gear.py passes tank value, 2026-10-15). `extra` {name: items}: sets that compete with the
    variants, each also with the raced trinket pair, when every item is in the pool; one named "previous" (the tier's last set) is the
    reference a new set must beat on seed 2 (2026-10-16: the Expertise re-gear's pre-BiS Enhancement set lost 1.6% to the set it
    replaced, which never raced it). `refine` (a tier name, 2026-11-22, the audit session's G1-G3): the weapons raced per hand after the
    greedy pass, the item-set pieces raced after the trinkets, the enchants chosen from the tier's enchant pool and put on every set
    that competes (race_weapons, race_set_pieces, choose_enchants); the stat picks alone compete as one more variant. `tank`: the
    enchant race takes absorb, heal and defensive enchants too (tank_gear.py).
    2026-11-23 (the audit session's rulings on the list test): a lower list's set (`ladder`) competes as it was made and as the copy
    with this list's enchants, the better on seed 2 stands, ties to the set as made; `known` {name: {"items", "source", "prep"}}: known
    positives (known_lists, or a side's full set), each put inside the pool (pool_swap, after an optional `prep(items, w, greedy)` ->
    (items, notes)), competing with this list's enchants, as listed and with the raced trinkets; one ahead of the chosen set on seed 2
    stands. REWEIGH: the picks from the weights measured at the picked set compete. The picker's best variant and the best known
    positive always race on seed 2, and the record keeps every competitor's scores (`competitors`, relative to `bases`)."""
    main = evals[0]
    cur_items = [dict(x) if x else {} for x in cur_items] + [{}] * (17 - len(cur_items))
    sc = score or (lambda row: row.get("dps") or 0)

    def weights(items):
        if weights_fn:
            return weights_fn(items)
        cfg = G.bench_cfg(main[1], repo, [{"label": "w", "talents": main[3], "gear_json": {"items": items}}], a.weight_iterations, 1, main[2], statweights=True)
        row = G.run_bench(repo, cfg, f"w-{tag}")["w"]
        if row.get("error"):
            raise SystemExit(f"stat weights failed for {tag}: {row['error']}")
        return row["weights"]

    seen, trinkets, greedy = G.class_picker(repo, cls, db, pool)   # gear_opt's per-slot step (shared since 2026-10-22)

    def with_trinkets(items, pair):
        x = [dict(i) for i in items]
        x[12], x[13] = {"id": pair[0]}, {"id": pair[1]}
        return x

    def race(sets, its, seed):
        out = {k: [] for k in sets}
        for name, e, where, tal, lab in evals:
            rows = G.run_bench(repo, G.bench_cfg(e, repo, [{"label": k, "talents": tal, "gear_json": {"items": v}} for k, v in sets.items()], its, seed, where), f"r-{tag}")
            ref = rows[next(iter(sets))]
            for k in sets:
                out[k].append(sc(rows[k]) / (sc(ref) or 1))
        return {k: sum(v) / len(v) for k, v in out.items()}

    w = weights([x if x.get("id") in db else {} for x in cur_items])   # (the bench would drop a missing item itself)
    v1, v2 = greedy(cur_items, w, False), greedy(cur_items, w, True)
    w = weights(v1)
    v1, v2 = greedy(v1, w, False), greedy(v2, w, True)
    steps = {}
    if refine:
        v1, steps["weapons"] = race_weapons(cls, v1, w, greedy, race, a.iterations, db)
    cur_pair = (cur_items[12].get("id"), cur_items[13].get("id"))
    top, screen = G.screen_trinkets(db, trinkets, v1, race, a.iterations)   # the pool's trinkets one at a time, the best paired (2026-10-22)
    pairs = [p for p in itertools.combinations(top, 2) if G.pair_ok(db, p)][: a.max_pairs]
    base_pair = (cur_pair if all(cur_pair) and all(i in db and pool(db[i]) for i in cur_pair) and G.pair_ok(db, cur_pair)
                 else (pairs[0] if pairs else cur_pair))
    v1 = with_trinkets(v1, base_pair) if all(base_pair) else v1
    tsets = {"base": v1, **{f"t{i}": with_trinkets(v1, p) for i, p in enumerate(pairs)}}
    tr = race(tsets, a.iterations, 1)
    tbest = max(tr, key=tr.get)
    pair = base_pair if tbest == "base" else pairs[int(tbest[1:])]
    if all(pair):
        v1, v2 = with_trinkets(v1, pair), with_trinkets(v2, pair)
    vs = {"v1": v1, "v2": v2}
    # a relic outside the list's pool counts as no relic (2026-11-23, the tanks' Easy smoke run: the standard set's Libram of Fervor
    # stayed in the paladin's Easy Pre-BiS set, relic_candidates offering nothing while the old relic is in the database, and list_guard
    # stopped the make): the slot's relics in the presets and the pool race, and with none the slot is left empty
    rc_items = cur_items
    x16 = cur_items[16] if len(cur_items) > 16 and cur_items[16] else {}
    if x16.get("id") in db and not pool(db[x16["id"]]):
        rc_items = [dict(y) if y else {} for y in cur_items]
        rc_items[16] = {}
    relic, relic_race = G.race_relics(greedy.relic_candidates(rc_items), vs, race, a.iterations)   # a re-filled relic slot (2026-10-22)
    for v in vs.values():
        y = v[16] if len(v) > 16 and v[16] else {}
        if y.get("id") in db and db[y["id"]].get("rangedWeaponType") in (6, 7, 8, 9) and not pool(db[y["id"]]):
            v[16] = {}
    v1, v2 = vs["v1"], vs["v2"]
    emap = None
    if refine:
        v1, steps["set_pieces"] = race_set_pieces(cls, v1, w, greedy, race, a.iterations, db, pool, repo=repo, confirm=a.confirm)
        v1, steps["effect_items"] = race_effect_items(cls, v1, greedy, race, a.iterations, db, pool, effect_screen, confirm=a.confirm)
    # REWEIGH (2026-11-23): the weights measured at the picked set, and the picks from them and from the mean of both weights (set pieces
    # and items with effects kept; weapons, ranged and trinkets as raced: the picks re-fill the other slots only)
    rew = {}
    if REWEIGH:
        w3 = weights(v1)
        wm = {k: (w.get(k, 0.0) + w3.get(k, 0.0)) / 2 for k in set(w) | set(w3)}
        for name, ww in (("all-slots, weights at the pick", w3), ("all-slots, mean weights", wm)):
            x = greedy(v1, ww, True)   # keep_special: every item with a setName or an effect stays, so a raced set unit is kept
            for s in (12, 13, 14, 15, 16):
                x[s] = dict(v1[s])
            if x != v1 and x not in rew.values():
                rew[name] = x
        steps["reweigh"] = {"weights_at_pick": {k: round(v, 4) for k, v in w3.items() if abs(v) > 1e-6}, "variants": list(rew)}
    # the known positives (2026-11-23), inside the pool, filled from the picker's set where they leave a slot or a trinket out
    known_sets, known_rec = {}, []
    for name, kp in (known or {}).items():
        its, notes = norm17(kp["items"]), []
        if kp.get("prep"):
            its, notes = kp["prep"](its, w, greedy)
        its, swaps = pool_swap(its, w, greedy, db, pool, v1)
        worn = wear_check(cls, its, db)
        if worn:   # (2026-11-23) a known positive nobody can wear is dropped, never raced as listed
            known_rec.append({"name": name, "source": kp.get("source"), "dropped": "cannot be worn: " + "; ".join(worn)[:300]})
            continue
        known_sets[name] = its
        known_rec.append({"name": name, "source": kp.get("source"), **({"prep": notes} if notes else {}), "swapped": swaps})
    made, kmade = {}, {}
    if refine:
        statmap, emap, steps["enchants"] = choose_enchants(cls, v1, w, refine, zones, race, a.iterations, db, tank=tank)
        steps["enchants"]["map"] = {str(k): v for k, v in emap.items()}
        v1s = enchants_for(cls, v1, w, refine, zones, db, statmap)
        v1, v2 = (enchants_for(cls, x, w, refine, zones, db, emap) for x in (v1, v2))
        rew = {k: enchants_for(cls, x, w, refine, zones, db, emap) for k, x in rew.items()}
        cur_items = enchants_for(cls, cur_items, w, refine, zones, db, emap)
        made = {k: enchants_for(cls, x, w, refine, zones, db, emap, own_first=True) for k, x in (extra or {}).items() if k in (ladder or ())}
        extra = {k: enchants_for(cls, x, w, refine, zones, db, emap) for k, x in (extra or {}).items()} or None
        kmade = {k: enchants_for(cls, x, w, refine, zones, db, emap, own_first=True) for k, x in known_sets.items()}
        known_sets = {k: enchants_for(cls, x, w, refine, zones, db, emap) for k, x in known_sets.items()}
    inpool = lambda its: all(x["id"] in db and pool(db[x["id"]]) for x in its if x.get("id"))   # noqa: E731
    in_tier = inpool(cur_items)   # a missing item is out of the pool (2026-10-22)
    keep_current = keep_current and in_tier   # the current set competes only when every item is in the tier's pool
    sets = ({"current": cur_items} if keep_current else {}) | {"all-slots": v1, "keep-sets-and-effects": v2}
    if refine and v1s != v1:
        sets["all-slots, stat enchants"] = v1s
    sets.update(rew)
    picker = [k for k in sets if k != "current"]   # the picker's own variants
    for name, its in (extra or {}).items():
        its = [dict(x) if x else {} for x in its] + [{}] * (17 - len(its))
        if its == cur_items or not inpool(its):
            continue
        low, m = ((ladder.get(name) if isinstance(ladder, dict) else None) or (None, None)), made.get(name)
        if low[0] and m is not None:
            # a lower list's set (2026-11-23, the re-run for the merge: Survival's True BiS took the True Pre-BiS set with True BiS's
            # main-hand enchant, Agility for Crusader, both in the True Pre-BiS pool: 0.04% ahead on the 3,000-fight confirm and 0.02%
            # behind it at 6,000 on seed 2): it races as made, and with this list's enchants or the raced trinkets only when they bring
            # something its own list could not take (the lower list raced its own enchants and trinkets on these items)
            lt, lpool = low
            new_ench = any(its[s].get("enchant") and its[s].get("enchant") != m[s].get("enchant") and its[s].get("id") in db
                           and not enchant_allowed(its[s]["enchant"], db[its[s]["id"]].get("type"), lt, zones) for s in range(17))
            new_trk = (all(pair) and (m[12].get("id"), m[13].get("id")) != pair
                       and any(not (t in db and lpool(db[t])) for t in pair))
            sets[f"{name} (as made)"] = m
            if new_ench and its != m:
                sets[name] = its
            if new_trk:
                sets[f"{name}+trinkets"] = with_trinkets(its if new_ench else m, pair)
            continue
        sets[name] = its
        if all(pair) and (its[12].get("id"), its[13].get("id")) != pair:
            sets[f"{name}+trinkets"] = with_trinkets(its, pair)
        m = made.get(name)
        if m is not None and m != its:
            sets[f"{name} (as made)"] = m
    for rec in known_rec:
        key, its = f"known: {rec['name']}", known_sets[rec["name"]]
        if not inpool(its):
            rec["left_out"] = "an item no swap could replace stays outside the pool"
            continue
        sets[key] = its
        if all(pair) and (its[12].get("id"), its[13].get("id")) != pair:
            sets[f"{key}+trinkets"] = with_trinkets(its, pair)
        m = kmade.get(rec["name"])
        if m is not None and m != its:
            sets[f"{key} (as listed)"] = m
    r1 = race(sets, a.iterations, 1)
    lead = max(r1, key=r1.get)
    ref = ("current" if keep_current else "previous" if "previous" in sets
           else ("keep-sets-and-effects" if lead == "all-slots" else "all-slots"))
    # the ladder guard (2026-11-23, the audit session's ruling on the list test: Survival's True BiS raced the True Pre-BiS set on seed 1
    # only, 0.08% behind at 1,000 fights, and ended 0.2-0.3% below it at 6,000 on both seeds): every lower list's set within
    # LADDER_MARGIN of the seed-1 leader races in the seed-2 confirm too, and stays unless the chosen set beats it there (ties go to
    # the lower list, whose pool nests in this one). Since the same day each lower list's set races as made and with this list's
    # enchants (the guarded True BiS had chosen the True Pre-BiS set, re-enchanted, 0.12-0.18% below it), ties to the set as made.
    # The known positives within LADDER_MARGIN race on seed 2 too, the best of them always, and the picker's best variant always.
    is_lad = lambda k: any(k in (n, f"{n}+trinkets", f"{n} (as made)") for n in (ladder or ()))   # noqa: E731
    is_known = lambda k: k.startswith("known: ")   # noqa: E731
    near = lambda k: r1[k] >= r1[lead] * (1 - LADDER_MARGIN)   # noqa: E731
    lad = [k for k in sets if k != lead and is_lad(k) and near(k)]
    kn = [k for k in sets if k != lead and is_known(k) and near(k)]
    pbest = max(picker, key=r1.get) if picker else None
    kbest = max((k for k in sets if is_known(k)), key=r1.get, default=None)
    conf = [k for k in dict.fromkeys([ref, lead, pbest, kbest] + lad + kn) if k is not None]
    r2 = race({k: sets[k] for k in conf}, a.confirm, 2) if len(conf) > 1 else {ref: 1.0}
    gain = r2.get(lead, 1.0) - 1
    chosen = lead if (lead != ref and gain > (a.min_gain if ref == "current" else 0.0)) else ref
    kb = max((k for k in r2 if is_known(k)), key=r2.get, default=None)
    if kb is not None and r2[kb] > r2[chosen]:   # a known positive ahead of the chosen set on seed 2 stands
        chosen = kb
    # ... by more than KNOWN_MARGIN against the picker's best (2026-11-23, the audit session: Frost's Easy set took the site's list, 14 of
    # its 17 slots swapped into the pool by our rule, at 1.0150 against the picker's 1.0153 on the confirm); inside that the picker's
    # set stands, and the record says the known positive tied
    known_tie = None
    if is_known(chosen) and pbest in r2 and r2[chosen] <= r2[pbest] * (1 + KNOWN_MARGIN):
        known_tie = {"known": chosen, "seed2": round(r2[chosen], 4), "picker": pbest, "picker_seed2": round(r2[pbest], 4),
                     "margin": KNOWN_MARGIN}
        chosen = pbest if (pbest != ref and r2[pbest] - 1 > (a.min_gain if ref == "current" else 0.0)) else ref
    ladder_case = None
    low = max((k for k in lad if k in r2), key=lambda k: (r2[k], k.endswith(" (as made)")), default=None)
    if low is not None and r2[low] >= r2[chosen]:
        chosen = low
    if is_lad(chosen):
        own = max((k for k in r2 if not is_lad(k)), key=r2.get, default=None)
        ladder_case = (f"{chosen}: no item of the larger pool beat it on seed 2"
                       + (f" ({own} {r2[own]:.4f} against {r2[chosen]:.4f})" if own else ""))
    elif any(sets[chosen] == sets[k] for k in sets if is_lad(k)):
        ladder_case = "the same items as a lower list's set: no item of the larger pool beat it"
    case = ("own make" if not is_lad(chosen) else "the lower list's set as made" if chosen.endswith(" (as made)")
            else "the lower list's set, re-enchanted" + (", with the raced trinkets" if chosen.endswith("+trinkets") else ""))
    for rec in known_rec:
        key = f"known: {rec['name']}"
        rec["scores"] = {k: {"seed1": round(r1[k], 4), **({"seed2": round(r2[k], 4)} if k in r2 else {})}
                         for k in (key, f"{key}+trinkets", f"{key} (as listed)") if k in sets}
    src = ("the current set" if chosen == "current" else "the previous set" + (", with the raced trinkets" if chosen != "previous" else "")
           if chosen.startswith("previous") else "a lower list's set" if is_lad(chosen) else "the picker" if chosen in picker else chosen)
    if is_known(chosen):
        rec = next(x for x in known_rec if chosen.startswith(f"known: {x['name']}"))
        n = sum(1 for s in rec["swapped"] if s.get("to"))
        filled = sum(1 for x in sets[chosen] if x.get("id"))
        if 2 * n > filled:   # mostly our own picks (2026-11-23, the audit session): a page credits the site only when most of the set is its
            src = f"the picker's set: {rec['name']} ({rec['source']}) supplied {filled - n} of its {filled} items, the rest swapped in by our rule"
        else:
            src = (f"a known positive: {rec['name']} ({rec['source']})" + (f", {n} items swapped into the pool by our rule" if n else "")
                   + (", with the picker's raced trinkets" if chosen.endswith("+trinkets") else ""))
    elif known_tie:
        src += f" ({known_tie['known'][7:]} tied: {known_tie['seed2']} against {known_tie['picker_seed2']} on seed 2, inside {KNOWN_MARGIN:.1%})"
    items = sets[chosen]
    # the confirm's margin (2026-11-23, the audit session's budget ruling): the chosen set against the best set that lost to it on seed 2;
    # under CLOSE_CALL, with other items, and neither a ladder tie nor a known-positive tie, the make is a close call: made again at the
    # default budgets in the second pass (make_lists.py lists them)
    losers = [k for k in r2 if k != chosen and k in sets]
    conf_margin = None
    if losers and chosen in r2:
        lk = max(losers, key=r2.get)
        mg = r2[chosen] / r2[lk] - 1 if r2[lk] else 0.0
        canon = lambda its: ([x.get("id") for x in norm17(its)[:10]] + sorted((x.get("id") or 0) for x in norm17(its)[10:12])   # noqa: E731
                             + sorted((x.get("id") or 0) for x in norm17(its)[12:14]) + [x.get("id") for x in norm17(its)[14:]])
        same = canon(sets[chosen]) == canon(sets[lk])   # rings and trinkets in either order are the same set (2026-11-23, the sandbox)
        conf_margin = {"over": lk, "margin": round(mg, 5), "same_items": same,
                       "close_call": bool(mg < CLOSE_CALL and not same and not known_tie and not (is_lad(chosen) or is_lad(lk)))}
    for x in known_rec:   # the known positive as it raced (its best variant), for make_lists' missed-set check (2026-11-23)
        vs = [k for k in sets if k == f"known: {x['name']}" or k.startswith(f"known: {x['name']}+")]
        if vs:
            kb = max(vs, key=lambda k: (r2.get(k, -1.0), r1.get(k, -1.0)))
            x.update(raced_as=kb, items=sets[kb], seed1=round(r1.get(kb, 0.0), 4), **({"seed2": round(r2[kb], 4)} if kb in r2 else {}))
    ilvl = lambda its: round(sum(db[x["id"]]["scalingOptions"]["0"].get("ilvl", 0) for x in its if x.get("id") in db) / max(1, sum(1 for x in its if x.get("id") in db)), 1)  # noqa: E731
    return {"evaluated_on": [f"{n}: {lab}" for n, _, _, _, lab in evals], "weights": {k: round(v, 4) for k, v in w.items() if abs(v) > 1e-6},
            "trinkets": [db[i]["name"] for i in pair if i in db], "trinket_screen": screen, **({"relic_race": relic_race} if relic_race else {}),
            "race_seed1": r1, "confirm_seed2": r2, "chosen": chosen, "chosen_source": src, "ladder_case": case,
            **({"known_tie": known_tie} if known_tie else {}), **({"confirm_margin": conf_margin} if conf_margin else {}),
            **({"ladder": ladder_case} if ladder_case else {}),
            "picker_best": {"name": pbest, "seed1": round(r1[pbest], 4), **({"seed2": round(r2[pbest], 4)} if pbest in r2 else {})} if pbest else None,
            "known_positives": known_rec or (no_known or "no known positive"),
            "competitors": {k: {"seed1": round(r1[k], 4), **({"seed2": round(r2[k], 4)} if k in r2 else {})} for k in sets},
            "bases": {"seed1": next(iter(sets)), "seed2": conf[0] if len(conf) > 1 else ref},
            **steps, **({"enchant_map": emap} if emap is not None else {}),
            "ilvl": ilvl(items), "items": items, "names": [db.get(x.get("id"), {}).get("name") if x.get("id") else None for x in items]}


def set_path(cls, spec, tier, nopvp=False, side=None):
    return SETS / f"{cls}-{SM.slug(spec)}-{tier}{'-nopvp' if nopvp else ''}{'-' + side.lower() if side else ''}.gear.json"


# wearing rules (2026-11-23, the audit session: "A SET NOBODY CAN WEAR"): Classic's weapon proficiencies by the database's WeaponType
# (1 axe, 2 dagger, 3 fist, 4 mace, 5 held in off hand, 6 polearm, 7 shield, 8 staff, 9 sword) and ranged types (1 bow, 2 crossbow,
# 3 gun, 4 thrown, 5 wand, 6 idol, 7 libram, 8 totem); held-in-off-hand items any class; a two-hander's type as its one-handed type
WEAPONS = {"warrior": {1, 2, 3, 4, 5, 6, 7, 8, 9}, "paladin": {1, 4, 5, 6, 7, 9}, "hunter": {1, 2, 3, 5, 6, 8, 9},
           "rogue": {2, 3, 4, 5, 9}, "priest": {2, 4, 5, 8}, "shaman": {1, 2, 3, 4, 5, 7, 8}, "mage": {2, 5, 8, 9},
           "warlock": {2, 5, 8, 9}, "druid": {2, 3, 4, 5, 6, 8}}
RANGED = {"warrior": {1, 2, 3, 4}, "rogue": {1, 2, 3, 4}, "hunter": {1, 2, 3}, "mage": {5}, "priest": {5}, "warlock": {5},
          "paladin": {7}, "shaman": {8}, "druid": {6}}
TWO_HANDERS = {"warrior": {1, 4, 6, 8, 9}, "paladin": {1, 4, 6, 9}, "hunter": {1, 6, 8, 9}, "shaman": {1, 4, 8}, "druid": {4, 6, 8},
               "priest": {8}, "mage": {8}, "warlock": {8}, "rogue": set()}
DUAL_WIELD = {"warrior", "rogue", "hunter"}


def wear_check(cls, items, db):
    """[] or why a character of `cls` at level 60 cannot wear the set: an item's slot type, the class allowlist, the armor type, the
    weapon or ranged type, a two-hander with anything in the off hand, an off-hand weapon for a class that cannot dual-wield, a shield
    for a class without one, a main-hand-only item in the off hand or the reverse, the level, a unique item or limit category twice."""
    bad, keys = [], set()
    x = norm17(items)
    mh = db.get(x[14].get("id")) if x[14].get("id") else None
    for i, y in enumerate(x):
        it = db.get(y.get("id")) if y.get("id") else None
        if not it:
            continue
        n = it.get("name")
        if it.get("type") != G.SLOT_TYPE[i]:
            bad.append(f"slot {i} {n}: its type does not go in this slot")
        if it.get("classAllowlist") and G.CLASS_ID[cls] not in it["classAllowlist"]:
            bad.append(f"slot {i} {n}: not for a {cls}")
        if it.get("armorType", 0) > G.ARMOR_MAX[cls]:
            bad.append(f"slot {i} {n}: armor a {cls} cannot wear")
        if (it.get("requiredLevel") or 0) > 60:
            bad.append(f"slot {i} {n}: needs level {it['requiredLevel']}")
        if it.get("type") == 13:
            wt, ht = it.get("weaponType"), it.get("handType")
            if wt not in WEAPONS[cls]:
                bad.append(f"slot {i} {n}: a {cls} cannot use this weapon type")
            if ht == 4 and wt not in TWO_HANDERS[cls]:
                bad.append(f"slot {i} {n}: a {cls} cannot use this two-hander")
            if i == 15:
                if mh and mh.get("handType") == 4:
                    bad.append(f"slot 15 {n}: beside a two-handed main hand")
                if ht in (1, 4):
                    bad.append(f"slot 15 {n}: a main-hand or two-handed item in the off hand")
                if wt == 7 and cls not in ("warrior", "paladin", "shaman"):
                    bad.append(f"slot 15 {n}: a {cls} cannot use a shield")
                if wt not in (5, 7) and cls not in DUAL_WIELD:
                    bad.append(f"slot 15 {n}: an off-hand weapon, and a {cls} cannot dual-wield")
            if i == 14 and ht == 3:
                bad.append(f"slot 14 {n}: an off-hand item in the main hand")
        if it.get("type") == 14 and it.get("rangedWeaponType") not in RANGED[cls]:
            bad.append(f"slot {i} {n}: a {cls} cannot use this ranged or relic type")
        k = G.unique_keys(it)
        if k & keys:
            bad.append(f"slot {i} {n}: a unique item or limit category twice")
        keys |= k
    return bad


def swap_fits(greedy, it, slot, cur):
    """The one slot rule of the swaps (2026-11-23, the audit session: effect_variants and race_set_pieces had it in two places): a weapon or
    ranged slot takes an item only where the set holds one of that shape (greedy.fits against it); other slots against the item itself."""
    if slot >= 14 and not cur:
        return False
    return greedy.fits(it, slot, cur or it)


def enchant_consistency(r, ref, tier, zones, evals, repo, a, tag):
    """The audit session's item 5 (2026-11-23): a player reading two lists asks which enchant is right when the same item carries another
    one a list below (the enchant race's noise at 1,000 fights). Where the set holds `ref`'s item in a slot with another enchant this list
    allows, the set with `ref`'s enchants there races the chosen set on seed 2 at the confirm's fights; the chosen enchants stay only when
    they beat it. Changes r["items"] in place; returns the record or None."""
    if not ref:
        return None
    items, ref = norm17(r["items"]), norm17(ref)
    slots = [i for i in range(17) if items[i].get("id") and items[i].get("id") == ref[i].get("id") and ref[i].get("enchant")
             and items[i].get("enchant") != ref[i].get("enchant") and enchant_allowed(ref[i]["enchant"], G.SLOT_TYPE[i], tier, zones)]
    if not slots:
        return {"slots": []}
    var = [dict(x) for x in items]
    for i in slots:
        var[i] = dict(var[i], enchant=ref[i]["enchant"])
    res = racer(evals, repo, None, tag + "-ench")({"own": items, "reference": var}, a.confirm, 2)
    own = res["own"] > res["reference"]
    if not own:
        r["items"] = var
    return {"slots": slots, "race_seed2": {k: round(v, 5) for k, v in res.items()}, "fights": a.confirm, "kept": "own" if own else "reference"}


def list_guard(items, tier, db, zones, repo, nopvp=False, side=None, cls=None):
    """The lists' fatal guard (2026-11-23, the audit session: a side's set holding the other side's items should have stopped the run;
    the same day, for Easy Pre-BiS and every list: "every item passes the Easy pool and the Easy enchant rule"): every item of the set
    is in the database and in the list's pool (pool_of, with the no-PvP and the side filters), every enchant is in the list's enchant
    pool for its slot (enchant_allowed), every item of a side's set passes gear_lists.faction_of for that side and every item of a
    no-PvP set has a source besides PvP. Checked when make() returns or writes a set, and by the scan (gear_check.py) on every set
    file made under the lists. [] or the offending items."""
    ctx = rules_ctx(zones, repo)
    lst = tier if tier in GL.LISTS else "prebis"
    pool = pool_of(tier, zones, repo, nopvp=nopvp, side=side)
    bad = []
    for i, x in enumerate(norm17(items)):
        if not x.get("id"):
            continue
        it = db.get(x["id"])
        if it is None:
            bad.append(f"slot {i} item {x['id']}: not in the database")
            continue
        f = GL.faction_of(it, ctx)
        side_bad = bool(side and f not in (None, side))
        pvp_bad = bool(nopvp and GL.pvp_only(it, lst, ctx))
        if side_bad:
            bad.append(f"slot {i} {it.get('name')}: {f} only")
        if pvp_bad:
            bad.append(f"slot {i} {it.get('name')}: only PvP puts it in the list")
        if not (side_bad or pvp_bad) and not pool(it):
            bad.append(f"slot {i} {it.get('name')}: not in {GL.LABEL.get(lst, lst)}")
        e = x.get("enchant")
        if e and not enchant_allowed(e, G.SLOT_TYPE[i], tier, zones):
            bad.append(f"slot {i} {it.get('name')}: enchant {e} is not in {GL.LABEL.get(lst, lst)}'s enchants for the slot")
    if cls:   # (2026-11-23) the set can be worn
        bad += wear_check(cls, items, db)
    return bad


def slot_swap_prep(cls, tier, db, zones, repo, nopvp=False, side=None):
    """prep(items, w, greedy) for a no-PvP or a side make's known positive "the list's full set, slot by slot" (2026-11-23, the audit
    session's ruling on the faction check: rebuilt from the current alternatives, so a side's set is the better of the made set and the
    swap and never below the swap): gear_lists.alternatives for the side (the client's other-faction item when it is in the list, else
    the best other item by the weights), gear_lists.pvp_alternatives without PvP; pool_swap then covers anything left."""
    ctx = rules_ctx(zones, repo)
    lst = tier if tier in GL.LISTS else "prebis"

    def prep(items, w, greedy):
        work, notes = norm17(items), []
        rows = GL.alternatives(cls, work, w, lst, db, ctx, G, greedy.fits) if side else []
        rows = [x for x in rows if x.get("for") == side] + (GL.pvp_alternatives(cls, work, w, lst, db, ctx, G, greedy.fits) if nopvp else [])
        for x in rows:
            if x.get("alternative"):
                work[x["slot"]] = dict(work[x["slot"]], id=x["alternative"])
            notes.append({"slot": x["slot"], "from": x.get("name"), "to": x.get("alternative_name"), "how": x.get("how", "the PvP rule")})
        return work, notes
    return prep


def make(cls, spec, tier, entry_name, talents, label, repo, db, zones, a, path=None, setting="raid", write=True, lower_sets=None,
         nopvp=False, side=None, known_positives=True, full_set=None):
    """The tier's set for one spec: written to its gear file (`path`: another file, e.g. the full-raid winner's set of a spec whose
    full-raid winner plays another entry; ml_pipeline.final), returned as the record. Chosen in a full raid (`setting`, since
    2026-10-31: the pages rank by full-raid DPS; sets chosen on the training dummy, short of mana, had weighed haste below zero for the
    Frostfire mage, and its full-raid set measured +2.7% over the dummy's, confirmed on seed 2). `write=False` (2026-11-23): nothing is
    written, the record is returned (a test of the rules). Since 2026-11-23 the record names the list and its rules (`list`, `rules`:
    raidsim/gear_lists.py) and carries the other faction's alternatives for its one-faction items (`faction_alternatives`).
    Every lower list's set competes (the ladder below), read from its file; so make the lists from the bottom, Easy Pre-BiS, then True
    Pre-BiS, then True BiS (2026-11-23, the list test: Survival's True BiS, made before its True Pre-BiS, raced the old pre-raid set
    and ended 0.2-0.3% below the new True Pre-BiS set on both seeds, though every item of that set is in True BiS). `lower_sets`
    {tier: items}: the lower lists' sets to race instead of their files (a test with write=False writes none). `nopvp`, `side`: the
    list without what only PvP puts in it, or without the other side's items (pool_of); such a set has a file of its own (set_path), so
    neither the guard nor the ladder ever races it against a set holding what it leaves out.
    2026-11-23 (the audit session's rulings on the list test): the spec's known positives compete (`known_positives`: known_lists, the
    site's lists inside the pool; the record says "no known positive" when there is none); a no-PvP or a side make also races the list's
    full set swapped slot by slot (`full_set`, else its file; slot_swap_prep); a lower list's set races as made (no template fill) and
    re-enchanted; a side's or a no-PvP set that fails list_guard stops the run (SystemExit), written or not."""
    e = R.SPECS[cls][entry_name]
    easy_check(tier, db, zones, repo)
    cur = json.load(open(R.sim_path(e["gear"]) if pathlib.Path(R.sim_path(e["gear"])).is_absolute() else repo / e["gear"], encoding="utf-8"))["items"]
    pool = pool_of(tier, zones, repo, nopvp=nopvp, side=side)
    p = path or set_path(cls, spec, tier, nopvp, side)
    # 2026-10-09: empty enchant slots are filled from the role's template before and after the search (fill_enchants.py: a set grown
    # from a preset without enchants kept none, the Balance, feral, Retribution, Arms and Fury sets)
    import fill_enchants as FE
    tmpl = FE.role(p.name)
    if tmpl:
        FE.fill(cur, tmpl)
    prev = json.load(open(p, encoding="utf-8"))["items"] if p.exists() else None   # the tier's last set competes (optimize_set's `extra`)
    if prev and tmpl:
        FE.fill(prev, tmpl)
    extra = {"previous": prev} if prev else {}
    ladder = ("dungeon", "prebis", "bis")   # every lower tier's set competes (2026-11-21, the audit session): the pools nest, so it is
    for lower in ladder[:ladder.index(tier)] if tier in ladder else ():   # legal here; when it wins, this tier's set is that set
        if lower in (lower_sets or {}):   # (as made: no template fill since 2026-11-23; the re-enchanted copy gets this list's enchants)
            extra[f"the {lower} set"] = [dict(x) if x else {} for x in lower_sets[lower]]
            continue
        lp = path.parent / path.name.replace(f"-{tier}.gear.json", f"-{lower}.gear.json") if path else set_path(cls, spec, lower, nopvp, side)
        if lp.exists() and lp.name != p.name:   # a named set file ("...-bis-raid") has no lower tier of its own
            extra[f"the {lower} set"] = json.load(open(lp, encoding="utf-8"))["items"]
    known, no_known = known_lists(cls, spec) if known_positives else ({}, "no known positive (not asked for)")
    if nopvp or side:   # the list's full set, slot by slot (its file unless given): a no-PvP or a side's set is never below that swap
        fp = set_path(cls, spec, tier, nopvp=bool(nopvp and side))   # (a side's set without PvP swaps the no-PvP set)
        full = full_set if full_set is not None else (json.load(open(fp, encoding="utf-8"))["items"] if fp.exists() else None)
        if full:
            what = " and ".join(x for x in (f"for the {side}" if side else "", "without PvP" if nopvp else "") if x)
            known[f"the full {GL.LABEL.get(tier, tier)} set, slot by slot {what}"] = {
                "items": full, "source": "the list's full set, swapped slot by slot (gear_lists.alternatives / pvp_alternatives, current rules)",
                "prep": slot_swap_prep(cls, tier, db, zones, repo, nopvp=nopvp, side=side)}
    r = optimize_set(cls, [(entry_name, e, setting, talents, label)], cur, pool, repo, db, a, f"{cls}-{SM.slug(spec)}-{tier}", keep_current=(tier == "bis"),
                     extra=extra or None, refine=tier, zones=zones, effect_screen=effect_screen_of(cls, spec),
                     ladder={k: (k.split()[1], pool_of(k.split()[1], zones, repo, nopvp=nopvp, side=side))
                             for k in extra if k.startswith("the ") and k.endswith(" set")},
                     known=known or None, no_known=no_known)
    # enchant consistency (2026-11-23, the audit session's item 5): the reference is the list below's set, for a no-PvP or a side's set
    # the list's full set
    eref = (full if (nopvp or side) else extra.get(f"the {dict(prebis='dungeon', bis='prebis').get(tier)} set"))
    r["enchant_consistency"] = enchant_consistency(r, eref, tier, zones, [(entry_name, e, setting, talents, label)], repo, a,
                                                   f"{cls}-{SM.slug(spec)}-{tier}")
    bad = list_guard(r["items"], tier, db, zones, repo, nopvp=nopvp, side=side, cls=cls)
    if bad:
        raise SystemExit(f"FATAL {p.name}: the chosen set ({r.get('chosen')}) breaks its list's rule: " + "; ".join(bad))
    # the hit report (2026-11-23, the user's hit ask, the audit session's item 1): the chosen set's hits from the simulator's own sheet
    # against the caps, flagged past the last useful cap by more than 1% (stats_bench.py; the record says so when it is not built)
    try:
        import stats_bench as SB
        r["hit"] = SB.hit_report(cls, spec, e, repo, talents, norm17(r["items"]), setting, bench_cfg=G.bench_cfg)
    except SystemExit as ex:
        r["hit"] = {"error": str(ex)[:300]}
    r["set_check"] = set_check(r["items"], db, repo, (r.get("hit") or {}).get("sets") if "error" not in (r.get("hit") or {}) else None)
    if r["set_check"].get("unknown_to_parser"):   # (2026-11-23, the audit session) the parser is behind the simulator: every spec's set
        # steps are suspect, so the make stops (make_lists stops with it)
        raise SystemExit(f"FATAL {p.name}: the simulator's sheet has set steps gear_tiers.sim_set_steps does not know: "
                         + ", ".join(r["set_check"]["unknown_to_parser"]))
    r["budget"] = os.environ.get("WOW_FOREVER_GEAR_BUDGET", "default")
    r["racials_off"] = os.environ.get("WOW_FOREVER_NO_RACIALS") == "1"   # (2026-11-23) the pages' numbers are made with racials off
    emap = r.pop("enchant_map", None)   # the tier's enchants are on every set that raced (2026-11-22): no template fill after them
    dropped = G.drop_missing_enchants(r["items"], repo)   # an enchant carried from a set the official database lacks (2026-10-22)
    if dropped:
        r["enchants_dropped"] = dropped
    # The guard (2026-11-20, search-improvements 0q: sets of level-29/30 items had replaced good ones; the previous set leaves
    # optimize_set's race when any of its items is outside the tier's pool, and then nothing compared the new set with it): a new set is
    # written only when it scores at least the set it replaces on the confirmation seed and fills every slot the old one filled; else
    # the old set stays, loudly.
    if p.exists():
        old = json.load(open(p, encoding="utf-8"))["items"]
        old = [dict(x) if x else {} for x in old] + [{}] * (17 - len(old))
        new = [dict(x) if x else {} for x in r["items"]] + [{}] * (17 - len(r["items"]))
        empty = [i for i in range(17) if old[i].get("id") and not new[i].get("id")]
        # the reference (the audit's refinement, same day): the old set when every item is in the tier's pool; else the old set repaired,
        # its out-of-pool slots re-filled with the new set's picks and everything else kept (after a pool change a correct new set may
        # score below the old one); the repaired set also competes: when it wins, it is written
        out_of_pool = [i for i in range(17) if old[i].get("id") and not (old[i]["id"] in db and pool(db[old[i]["id"]]))]
        ref = [dict(new[i]) if i in out_of_pool else dict(old[i]) for i in range(17)]
        if emap is not None:   # (2026-11-22) the old set with the tier's chosen enchants: the guard compares items, and an enchant the
            ref = enchants_for(cls, ref, r["weights"], tier, zones, db, emap)   # tier no longer allows never stays through it
        rows = G.run_bench(repo, G.bench_cfg(e, repo, [{"label": "new", "talents": talents, "gear_json": {"items": new}},
                                                        {"label": "previous", "talents": talents, "gear_json": {"items": ref}}],
                                              a.confirm, 2, setting), f"guard-{cls}-{SM.slug(spec)}-{tier}")
        nv, ov = (rows.get("new") or {}).get("dps") or 0.0, (rows.get("previous") or {}).get("dps") or 0.0
        if nv < ov or empty:
            what = "previous (the guard)" if not out_of_pool else f"previous, repaired in slots {out_of_pool} (the guard)"
            print(f"  REFUSED {p.name}: the new set ({r.get('chosen')}, item level {r.get('ilvl')}) scores {nv:.1f} against the "
                  f"{'repaired ' if out_of_pool else ''}previous set's {ov:.1f} on seed 2" + (f" and empties slots {empty}" if empty else "")
                  + ("; the repaired previous set is written" if out_of_pool else "; the previous set stays"), flush=True)
            if out_of_pool and write:
                bad = list_guard(ref, tier, db, zones, repo, nopvp=nopvp, side=side, cls=cls)
                if bad:
                    raise SystemExit(f"FATAL {p.name}: the repaired previous set breaks its list's rule: " + "; ".join(bad))
                p.write_text(json.dumps({"items": ref, "list": GL.LABEL.get(tier, tier), "rules": GL.RULES, **({"without_pvp": True} if nopvp else {}),
                                         **({"side": side} if side else {})}, indent=1) + "\n", encoding="utf-8")
            return dict(r, items=ref, chosen=what, **list_fields(cls, ref, r["weights"], tier, db, zones, repo, pool, side=side),
                        refused={"new_dps": round(nv, 2), "previous_dps": round(ov, 2), "empty_slots": empty, "repaired_slots": out_of_pool,
                                 "new_ilvl": r.get("ilvl"), "new_names": r.get("names")},
                        names=[db.get(x.get("id"), {}).get("name") if x.get("id") else None for x in ref],
                        entry=entry_name, gear=p.relative_to(ROOT).as_posix(), date=TODAY, setting=setting)
        r["guard"] = {"new_dps": round(nv, 2), "previous_dps": round(ov, 2), "repaired_slots": out_of_pool}
    if write:   # the ladder's case goes in the set's file (the audit session, 2026-11-23): a page says "True BiS is the True Pre-BiS set" once
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(json.dumps({"items": r["items"], "list": GL.LABEL.get(tier, tier), "rules": GL.RULES, **({"without_pvp": True} if nopvp else {}),
                                 **({"side": side} if side else {}), **({"ladder": r["ladder"]} if r.get("ladder") else {})}, indent=1) + "\n",
                     encoding="utf-8")
    return dict(r, entry=entry_name, gear=p.relative_to(ROOT).as_posix(), date=TODAY, setting=setting,
                **list_fields(cls, r["items"], r["weights"], tier, db, zones, repo, pool, side=side), **({} if write else {"written": False}),
                **({"without_pvp": WITHOUT_PVP} if nopvp else {}), **({"side": side} if side else {}))


def list_fields(cls, items, w, tier, db, zones, repo, pool, side=None):
    """The record's list fields (2026-11-23): the list's name and rules, each item's kinds (why it is in the list), the other
    faction's alternatives, and what the set costs in a vendor currency (`currency_cost`: Pix Xizzix's Tarnished Undermine Reals;
    raidsim/gear_lists.py). A side's set (`side`) lists no other-faction alternatives: the other side has its own set (2026-11-23)."""
    ctx = rules_ctx(zones, repo)
    _, _, greedy = G.class_picker(repo, cls, db, pool)
    kinds = {str(i): [k for k, _ in GL.item_kinds(db[x["id"]], ctx)] for i, x in enumerate(items[:17]) if x and x.get("id") in db}
    cost = GL.currency_cost(items, db)
    return {"list": GL.LABEL.get(tier, tier), "rules": GL.RULES, "kinds": kinds, "marks": GL.marks(items, tier, db, ctx),
            "faction_alternatives": [] if side else GL.alternatives(cls, items, w, tier, db, ctx, G, greedy.fits),
            "pvp_alternatives": GL.pvp_alternatives(cls, items, w, tier, db, ctx, G, greedy.fits), **({"currency_cost": cost} if cost else {})}


def load_db(repo):
    db, zones = G.load_db(repo)
    G.load_vetted(repo, db)
    load_vetted_pre(repo)
    load_enchants(repo, db)   # (2026-11-22) the enchant pool's data: choose_enchants
    return db, zones


BUDGETS = {"default": dict(iterations=3000, confirm=12000, weight_iterations=3000, min_gain=0.0, max_pairs=28),
           # the list tests' budgets (2026-11-23, test_lists_1123c-g, whose sets the audit session accepted): about a third of the time
           "tests": dict(iterations=1000, confirm=3000, weight_iterations=1000, min_gain=0.0, max_pairs=12),
           # the first pass of the all-class makes (the audit session's ruling, 2026-11-23): the tests' budgets with the confirm doubled
           # (the one failure seen at the tests' budgets was a confirm at 3,000: 0.04% ahead, 0.02% behind at 6,000); close calls are
           # made again at "default" in the second pass (make_lists.py lists them)
           "first-pass": dict(iterations=1000, confirm=6000, weight_iterations=1000, min_gain=0.0, max_pairs=12)}


def args_ns(**kw):
    """The set maker's budgets: BUDGETS["default"], or the set WOW_FOREVER_GEAR_BUDGET names (make_lists.py's runs, 2026-11-23)."""
    d = dict(BUDGETS[os.environ.get("WOW_FOREVER_GEAR_BUDGET", "default")])
    d.update(kw)
    return argparse.Namespace(**d)


# ------------------------------------------------------------------------------------------------ --remake (2026-10-22)
ML_DIR = HERE / "ml"
# an ML record's gear key -> (tier, the search whose winner the set was made for, label, the "-raid" file); ml_pipeline.py's final step
REMAKE_KEYS = {"bis": ("bis", ("bis-dummy", "bis-dummy-1"), "ml winner", False),
               "prebis": ("prebis", ("bis-dummy", "bis-dummy-1"), "ml winner (bis)", False),
               "bis-raid": ("bis", ("bis-raid",), "ml winner (full raid)", True),
               "prebis-raid": ("prebis", ("bis-raid",), "ml winner (full raid)", True)}


def remake(a, repo, db, zones):
    """Every tier set of the ML records (`raidsim/ml/<class>-<spec slug>.json`, key `gear`) made again, in place: the same entry, the
    record's current winner for that set, the tools' rules. Written for the port to wowsims/forever (2026-10-22): the official database
    lacks 159 items of the fork-era sets. Each record's gear key gets the new result plus `replaced` (slot, old item, new item) and
    `remade`; records are written after every set (resumable: a set already remade is skipped unless --fresh, or named in --sets)."""
    sim = f"wowsims/forever {R.git_commit(repo)}"
    files = sorted(f for f in ML_DIR.glob("*.json") if f.name not in ("rotations.json", "spell-probe.json"))
    for f in files:
        rec = json.load(open(f, encoding="utf-8"))
        if a.classes and rec["class"] not in a.classes:
            continue
        if a.spec and rec["spec"] not in a.spec:
            continue
        cls, trees = rec["class"], R.load_trees(repo, rec["class"])
        for key in [k for k in REMAKE_KEYS if k in (rec.get("gear") or {})]:
            old = rec["gear"][key]
            gname = pathlib.Path(old.get("gear", "")).name
            if a.sets and gname not in a.sets:
                continue
            # resume: a set made on the official database is done whatever the commit (a re-pin alone does not redo every set;
            # --fresh or --sets select what to redo)
            if old.get("remade") and not a.fresh and not a.sets:
                print(f"== {f.name} {key}: done ({old['remade'].get('simulator')})", flush=True)
                continue
            tier, searches, label, raid = REMAKE_KEYS[key]
            sk = next((k for k in searches if k in rec.get("search", {})), None)
            if not sk:
                print(f"== {f.name} {key}: no winner in the record (searches {searches}); skipped", flush=True)
                continue
            alloc = {n: r for items in rec["search"][sk]["winner"]["allocation"].values() for n, r in items}
            # talents the simulator's trees no longer have (records searched on older trees: Wake of Fire, Call of Thunder, Malediction,
            # Shadow Affinity, Improved Fire Nova) are left out: the gear is chosen for the rest of the build (recorded)
            known = {R.talent_key(t) for tr in trees for t in tr["talents"]}
            dropped = sorted(n for n in alloc if n not in known)
            alloc = {n: r for n, r in alloc.items() if n in known}
            entry = old.get("entry") or rec["search"][sk]["entry"]
            path = ROOT / old["gear"] if old.get("gear") else (SETS / f"{cls}-{rec['slug']}-{tier}{'-raid' if raid else ''}.gear.json")
            before = json.load(open(path, encoding="utf-8"))["items"] if path.exists() else []
            print(f"== {f.name} {key}: {tier} in {entry} for the {sk} winner -> {path.relative_to(ROOT).as_posix()}", flush=True)
            t0 = time.time()
            g = make(cls, rec["spec"], tier, entry, R.talents_string(trees, alloc), label, repo, db, zones, a, path=path)
            keep = ("entry", "gear", "date", "chosen", "ilvl", "trinkets", "trinket_screen", "names", "race_seed1", "confirm_seed2", "weights",
                    "evaluated_on", "enchants_dropped", "weapons", "set_pieces", "enchants")
            new = {k: g[k] for k in keep if k in g}
            before = [dict(x) if x else {} for x in before] + [{}] * (17 - len(before))
            new["replaced"] = [{"slot": i, "from": G.item_name(db, before[i].get("id")), "to": G.item_name(db, g["items"][i].get("id"))}
                               for i in range(17) if before[i].get("id") != g["items"][i].get("id")]
            new["remade"] = {"simulator": sim, "why": "port to wowsims/forever (_reference/sim-port.md): the fork-era set held items the "
                             "official database lacks", "missing_before": G.missing_in(before, db), "winner_of": sk,
                             "talents_left_out": dropped,
                             "minutes": round((time.time() - t0) / 60, 1)}
            rec["gear"][key] = new
            f.write_text(json.dumps(rec, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
            print(f"  item level {g['ilvl']}, chosen {g['chosen']}, trinkets {', '.join(g['trinkets'])}; seed 1 "
                  + ", ".join(f"{k} {v:.3f}" for k, v in g["race_seed1"].items()) + "; seed 2 "
                  + ", ".join(f"{k} {v:.3f}" for k, v in g["confirm_seed2"].items()), flush=True)
            for c in new["replaced"]:
                print(f"    slot {c['slot']}: {c['from']} -> {c['to']}", flush=True)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--set", nargs=3, metavar=("CLASS", "SPEC", "TIER"))
    ap.add_argument("--entry")
    ap.add_argument("--build")
    ap.add_argument("--remake", action="store_true", help="make every ML record's tier sets again, in place (see remake)")
    ap.add_argument("--classes", nargs="*", default=[], help="--remake: these classes only")
    ap.add_argument("--spec", action="append", help="--remake: this spec only (repeatable)")
    ap.add_argument("--fresh", action="store_true", help="--remake: redo sets already remade")
    ap.add_argument("--sets", nargs="*", default=[], help="--remake: redo only these gear files (names, e.g. mage-frost-bis.gear.json)")
    ap.add_argument("--iterations", type=int, default=3000)
    ap.add_argument("--confirm", type=int, default=12000)
    ap.add_argument("--weight-iterations", type=int, default=3000)
    ap.add_argument("--min-gain", type=float, default=0.0, help="margin a new set needs over the current one (BiS tier; default: none)")
    ap.add_argument("--max-pairs", type=int, default=28)
    a = ap.parse_args()
    R.set_game("forever")
    repo = R.repo_path(argparse.Namespace(repo=None))
    db, zones = load_db(repo)
    if a.remake:
        return remake(a, repo, db, zones)
    if not (a.set and a.entry and a.build):
        ap.error("--set, --entry and --build (or --remake)")
    cls, spec, tier = a.set
    trees = R.load_trees(repo, cls)
    if a.build.endswith(".json"):
        al = R.alloc_of(json.load(open(a.build, encoding="utf-8")))
    else:
        al = R.alloc_of({b["id"]: b for b in json.load(open(paths.builds_json("forever", cls), encoding="utf-8"))["builds"]}[a.build])
    r = make(cls, spec, tier, a.entry, R.talents_string(trees, al), a.build, repo, db, zones, a)
    print(f"{cls} {spec} {tier}: item level {r['ilvl']}, chosen {r['chosen']}, trinkets {', '.join(r['trinkets'])}")
    print("  " + "; ".join(n for n in r["names"] if n))


if __name__ == "__main__":
    main()
