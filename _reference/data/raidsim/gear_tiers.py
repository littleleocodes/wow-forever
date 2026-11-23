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


def pool_of(tier, zones, repo=None):
    """The list's item pool (2026-11-23): raidsim/gear_lists.py's rules, "bis" = True BiS, "prebis" = True Pre-BiS, "dungeon" = Easy
    Pre-BiS (any other name: True Pre-BiS). Until then three tiers with their own rules (Raid BiS, Pre-raid, Quests and dungeons; the
    module docstring and crafted_ok / dungeon_source above, kept for the record)."""
    ctx = rules_ctx(zones, repo)
    lst = tier if tier in GL.LISTS else "prebis"
    return lambda it: GL.in_list(it, lst, ctx)


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
WEAPON_TOP, WEAPON_EFFECTS_FROM, WEAPON_RERACE = 8, 20, 4   # per hand: the best 8 by the weights, any with an effect among the best 20;
WEAPON_DPS_MIN = 0.1   # the main hand raced again on its pass-1 best 4 after the off hand changed; a hand whose dps the weights value
SET_MAX_LOSS, SET_RACE_MAX = 0.10, 10   # a set's pieces raced when they cost at most 10% of the replaced items' value by the weights
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
                passes.append((14, [int(c) for c in first[14] if int(c) != items[15].get("id")]))
    return items, rec


def race_set_pieces(cls, items, w, greedy, race, its, db, pool):
    """G3: each item set the class can wear two or more pieces of from the pool, its pieces put in as a unit and raced in the set on
    seed 1: all of its pieces, and its two cheapest by the weights when it has more; only units that cost at most SET_MAX_LOSS of the
    replaced items' value by the weights, the cheapest SET_RACE_MAX. The best unit is taken when ahead. The bonuses themselves are the
    simulator's (the database lists the pieces, not the bonus). Returns (items, record)."""
    items = norm17(items)
    held = {x.get("id") for x in items if x.get("id")}
    slots_of = {}
    for it in db.values():
        sn = it.get("setName")
        if not sn or not pool(it):
            continue
        for slot in range(17):
            if G.SLOT_TYPE[slot] == 12:
                continue
            shape = db.get(items[slot].get("id")) if items[slot].get("id") else None
            if slot >= 14 and not shape:
                continue
            if greedy.fits(it, slot, shape):
                slots_of.setdefault(sn, {}).setdefault(slot, []).append(it)
    units = []
    for sn, by in slots_of.items():
        if len(by) < 2 or all(any(it["id"] in held for it in v) for v in by.values()):
            continue
        # per slot the piece worth most; a ring or weapon piece fits two slots: each piece once
        pick, used = {}, set()
        for slot, v in sorted(by.items(), key=lambda kv: -max(G.value(it, w, kv[0]) for it in kv[1])):
            v = [it for it in v if it["id"] not in used]
            if v:
                it = max(v, key=lambda it: G.value(it, w, slot))
                pick[slot] = it
                used.add(it["id"])
        if len(pick) < 2:
            continue
        loss = {s: G.value(db[items[s]["id"]], w, s) - G.value(it, w, s) if items[s].get("id") in db else -G.value(it, w, s) for s, it in pick.items()}
        base = {s: G.value(db[items[s]["id"]], w, s) if items[s].get("id") in db else 0.0 for s in pick}
        cands = [tuple(sorted(pick))]
        if len(pick) > 2:
            cands.append(tuple(sorted(sorted(pick, key=lambda s: loss[s])[:2])))
        for ss in cands:
            tot = sum(base[s] for s in ss)
            ls = sum(loss[s] for s in ss)
            if ls <= SET_MAX_LOSS * max(tot, 1e-9) and not all(items[s].get("id") == pick[s]["id"] for s in ss):
                units.append((ls / max(tot, 1e-9), sn, {s: pick[s] for s in ss}))
    units.sort(key=lambda u: u[0])
    units = units[:SET_RACE_MAX]
    if not units:
        return items, []
    sets = {"current": items}
    keyed = {}
    for rel, sn, pk in units:
        x = [dict(y) for y in items]
        ukeys = set()
        for s, it in pk.items():
            ench = x[s].get("enchant")
            x[s] = {"id": it["id"], **({"enchant": ench} if ench else {})}
        for y in x:   # the unit must keep the set legal: unique items and limit categories once
            if y.get("id"):
                k = G.unique_keys(db.get(y["id"]))
                if k & ukeys:
                    break
                ukeys |= k
        else:
            name = f"{sn} ({len(pk)})"
            sets[name] = x
            keyed[name] = (rel, pk)
    if len(sets) < 2:
        return items, []
    r = race(sets, its, 1)
    best = max(r, key=r.get)
    rec = [{"unit": k, "pieces": [p["name"] for p in keyed[k][1].values()], "weights_loss": round(keyed[k][0], 4), "race_seed1": round(r[k], 4)}
           for k in keyed]
    if best != "current" and r[best] > 1.0:
        items = sets[best]
        rec.append({"taken": best})
    return items, rec


def enchants_for(cls, items, w, tier, zones, db, emap=None):
    """The set's enchants within the tier's pool: per slot the enchant of `emap` ({slot: effect id}) when it goes on the item, else the
    slot's own when the tier allows it, else the slot's stat pick by the weights (an enchant the tier does not allow never stays)."""
    items = norm17(items)
    for slot in range(17):
        x = items[slot]
        it = db.get(x.get("id")) if x.get("id") else None
        if not it:
            continue
        pool, _ = slot_enchants(cls, it, slot, tier, zones)
        ids = {e["effectId"] for e in pool}
        want = (emap or {}).get(slot)
        if want in ids:
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
    items, srec = race_set_pieces(cls, items, w, greedy, race, a.iterations, db, pool)
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


def optimize_set(cls, evals, cur_items, pool, repo, db, a, tag, keep_current, weights_fn=None, score=None, extra=None, refine=None,
                 zones=None, tank=False):
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
    enchant race takes absorb, heal and defensive enchants too (tank_gear.py)."""
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
    relic, relic_race = G.race_relics(greedy.relic_candidates(cur_items), vs, race, a.iterations)   # a re-filled relic slot (2026-10-22)
    v1, v2 = vs["v1"], vs["v2"]
    emap = None
    if refine:
        v1, steps["set_pieces"] = race_set_pieces(cls, v1, w, greedy, race, a.iterations, db, pool)
        statmap, emap, steps["enchants"] = choose_enchants(cls, v1, w, refine, zones, race, a.iterations, db, tank=tank)
        steps["enchants"]["map"] = {str(k): v for k, v in emap.items()}
        v1s = enchants_for(cls, v1, w, refine, zones, db, statmap)
        v1, v2 = (enchants_for(cls, x, w, refine, zones, db, emap) for x in (v1, v2))
        cur_items = enchants_for(cls, cur_items, w, refine, zones, db, emap)
        extra = {k: enchants_for(cls, x, w, refine, zones, db, emap) for k, x in (extra or {}).items()} or None
    in_tier = all(x["id"] in db and pool(db[x["id"]]) for x in cur_items if x.get("id"))   # a missing item is out of the pool (2026-10-22)
    keep_current = keep_current and in_tier   # the current set competes only when every item is in the tier's pool
    sets = ({"current": cur_items} if keep_current else {}) | {"all-slots": v1, "keep-sets-and-effects": v2}
    if refine and v1s != v1:
        sets["all-slots, stat enchants"] = v1s
    for name, its in (extra or {}).items():
        its = [dict(x) if x else {} for x in its] + [{}] * (17 - len(its))
        if its == cur_items or not all(x["id"] in db and pool(db[x["id"]]) for x in its if x.get("id")):
            continue
        sets[name] = its
        if all(pair) and (its[12].get("id"), its[13].get("id")) != pair:
            sets[f"{name}+trinkets"] = with_trinkets(its, pair)
    r1 = race(sets, a.iterations, 1)
    lead = max(r1, key=r1.get)
    ref = ("current" if keep_current else "previous" if "previous" in sets
           else ("keep-sets-and-effects" if lead == "all-slots" else "all-slots"))
    r2 = race({ref: sets[ref], lead: sets[lead]}, a.confirm, 2) if lead != ref else {ref: 1.0}
    gain = r2.get(lead, 1.0) - 1
    chosen = lead if (lead != ref and gain > (a.min_gain if ref == "current" else 0.0)) else ref
    items = sets[chosen]
    ilvl = lambda its: round(sum(db[x["id"]]["scalingOptions"]["0"].get("ilvl", 0) for x in its if x.get("id") in db) / max(1, sum(1 for x in its if x.get("id") in db)), 1)  # noqa: E731
    return {"evaluated_on": [f"{n}: {lab}" for n, _, _, _, lab in evals], "weights": {k: round(v, 4) for k, v in w.items() if abs(v) > 1e-6},
            "trinkets": [db[i]["name"] for i in pair if i in db], "trinket_screen": screen, **({"relic_race": relic_race} if relic_race else {}),
            "race_seed1": r1, "confirm_seed2": r2, "chosen": chosen, **steps, **({"enchant_map": emap} if emap is not None else {}),
            "ilvl": ilvl(items), "items": items, "names": [db.get(x.get("id"), {}).get("name") if x.get("id") else None for x in items]}


def set_path(cls, spec, tier):
    return SETS / f"{cls}-{SM.slug(spec)}-{tier}.gear.json"


def make(cls, spec, tier, entry_name, talents, label, repo, db, zones, a, path=None, setting="raid", write=True):
    """The tier's set for one spec: written to its gear file (`path`: another file, e.g. the full-raid winner's set of a spec whose
    full-raid winner plays another entry; ml_pipeline.final), returned as the record. Chosen in a full raid (`setting`, since
    2026-10-31: the pages rank by full-raid DPS; sets chosen on the training dummy, short of mana, had weighed haste below zero for the
    Frostfire mage, and its full-raid set measured +2.7% over the dummy's, confirmed on seed 2). `write=False` (2026-11-23): nothing is
    written, the record is returned (a test of the rules). Since 2026-11-23 the record names the list and its rules (`list`, `rules`:
    raidsim/gear_lists.py) and carries the other faction's alternatives for its one-faction items (`faction_alternatives`)."""
    e = R.SPECS[cls][entry_name]
    cur = json.load(open(R.sim_path(e["gear"]) if pathlib.Path(R.sim_path(e["gear"])).is_absolute() else repo / e["gear"], encoding="utf-8"))["items"]
    pool = pool_of(tier, zones, repo)
    p = path or set_path(cls, spec, tier)
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
        lp = path.parent / path.name.replace(f"-{tier}.gear.json", f"-{lower}.gear.json") if path else set_path(cls, spec, lower)
        if lp.exists() and lp.name != p.name:   # a named set file ("...-bis-raid") has no lower tier of its own
            li = json.load(open(lp, encoding="utf-8"))["items"]
            if tmpl:
                FE.fill(li, tmpl)
            extra[f"the {lower} set"] = li
    r = optimize_set(cls, [(entry_name, e, setting, talents, label)], cur, pool, repo, db, a, f"{cls}-{SM.slug(spec)}-{tier}", keep_current=(tier == "bis"),
                     extra=extra or None, refine=tier, zones=zones)
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
                p.write_text(json.dumps({"items": ref}, indent=1) + "\n", encoding="utf-8")
            return dict(r, items=ref, chosen=what, **list_fields(cls, ref, r["weights"], tier, db, zones, repo, pool),
                        refused={"new_dps": round(nv, 2), "previous_dps": round(ov, 2), "empty_slots": empty, "repaired_slots": out_of_pool,
                                 "new_ilvl": r.get("ilvl"), "new_names": r.get("names")},
                        names=[db.get(x.get("id"), {}).get("name") if x.get("id") else None for x in ref],
                        entry=entry_name, gear=p.relative_to(ROOT).as_posix(), date=TODAY, setting=setting)
        r["guard"] = {"new_dps": round(nv, 2), "previous_dps": round(ov, 2), "repaired_slots": out_of_pool}
    if write:
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(json.dumps({"items": r["items"]}, indent=1) + "\n", encoding="utf-8")
    return dict(r, entry=entry_name, gear=p.relative_to(ROOT).as_posix(), date=TODAY, setting=setting,
                **list_fields(cls, r["items"], r["weights"], tier, db, zones, repo, pool), **({} if write else {"written": False}))


def list_fields(cls, items, w, tier, db, zones, repo, pool):
    """The record's list fields (2026-11-23): the list's name and rules, each item's kinds (why it is in the list) and the other
    faction's alternatives (raidsim/gear_lists.py)."""
    ctx = rules_ctx(zones, repo)
    _, _, greedy = G.class_picker(repo, cls, db, pool)
    kinds = {str(i): [k for k, _ in GL.item_kinds(db[x["id"]], ctx)] for i, x in enumerate(items[:17]) if x and x.get("id") in db}
    return {"list": GL.LABEL.get(tier, tier), "rules": GL.RULES, "kinds": kinds, "marks": GL.marks(items, tier, db, ctx),
            "faction_alternatives": GL.alternatives(cls, items, w, tier, db, ctx, G, greedy.fits),
            "pvp_alternatives": GL.pvp_alternatives(cls, items, w, tier, db, ctx, G, greedy.fits)}


def load_db(repo):
    db, zones = G.load_db(repo)
    G.load_vetted(repo, db)
    load_vetted_pre(repo)
    load_enchants(repo, db)   # (2026-11-22) the enchant pool's data: choose_enchants
    return db, zones


def args_ns(**kw):
    d = dict(iterations=3000, confirm=12000, weight_iterations=3000, min_gain=0.0, max_pairs=28)
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
