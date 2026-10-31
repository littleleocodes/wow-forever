"""Pre-BiS and phase-1 BiS gear for every raid damage spec (2026-10-01, user request: "DPS rankings for pre-BiS as well as best in slot,
like WoWSims does").

    python _reference/data/raidsim/gear_tiers.py --set <class> "<spec>" <tier> --entry <entry> --build <build id | candidate .json>
    python _reference/data/raidsim/gear_tiers.py --remake [--classes ...] [--spec ...] [--fresh]   # every ML record's sets again

(ml_pipeline.py makes every spec's sets through `make`.)

Two tiers, one item pool each (the simulator's item database at the pinned wowsims/forever commit, raidsim/setup.py; the
ElliotWood/Forever fork's until 2026-10-18, `_reference/sim-port.md`):
- **bis** (phase 1): `gear_opt.py`'s pool: dungeons, Molten Core, Onyxia, world drops, crafted, quest; items with no listed source only
  when a community phase-0/1, launch or pre-raid preset uses them (the Forever launch items); no BWL, ZG, AQ, Naxxramas, world bosses
  or legendaries; the hunter's Molten Core quest bow and stave (Rhok'delar, Lok'delar) count.
- **prebis** (pre-raid): the same without any raid drop, without the quest rewards of raid bosses and without crafted items made from
  Molten Core or Onyxia materials (`PHASE1_RAID_MADE`, our list: the database has the recipe, not its materials); items with no listed
  source only when a launch or pre-raid preset uses them.
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

_s = importlib.util.spec_from_file_location("gear_opt", HERE / "gear_opt.py")
G = importlib.util.module_from_spec(_s)
_s.loader.exec_module(G)
R = G.R
SETS = HERE / "gear_sets" / "forever" / "tiers"
TIERS = ("prebis", "bis")
TODAY = datetime.date.today().isoformat()

RAID_ZONES = G.RAID_OK | G.RAID_NO
# Crafted items (the database has the recipe, not its materials; our lists, 2026-10-01):
# - made from Molten Core or Onyxia materials (Fiery Core, Lava Core, Core Leather, Sulfuron Ingot, Scale of Onyxia), and the rewards of
#   Onyxia's quest: phase 1, so in bis and not in prebis;
PHASE1_RAID_MADE = {"Flarecore Gloves", "Flarecore Mantle", "Flarecore Wraps", "Flarecore Robe", "Flarecore Leggings", "Corehound Boots",
                    "Corehound Belt", "Molten Helm", "Molten Belt", "Fiery Chain Girdle", "Fiery Chain Shoulders", "Core Marksman Rifle",
                    "Sulfuron Hammer", "Onyxia Scale Cloak", "Onyxia Scale Breastplate", "Dark Iron Leggings", "Dark Iron Helm",
                    "Dark Iron Gauntlets", "Dark Iron Boots", "Dark Iron Reaver", "Dark Iron Destroyer", "Lavashard Axe", "Lava Belt",
                    "Blackguard", "Ebon Hand", "Nightfall", "Black Amnesty", "Blackfury"}
RAID_QUEST = {"Dragonslayer's Signet", "Onyxia Tooth Pendant", "Onyxia Blood Talisman"}
# - made from later raids' materials or later reputations (Zul'Gurub's Bloodvine and hides, Ahn'Qiraj's Cenarion Circle recipes and
#   obsidian, Naxxramas's frost-resistance sets): in neither tier. gear_opt.py's pool let them in, so the 2026-09-30 phase-1 sets of the
#   hunter and the Retribution paladin carried Bloodvine pieces (Zul'Gurub);
LATER_PREFIXES = G.LATER_PREFIXES   # gear_opt.py's list (its pool excludes them too since 2026-10-01)
# - any other crafted item of item level 65 or more is a later-phase recipe unless a community preset of the tier uses it.
CRAFTED_MAX_ILVL = 64
VETTED_PRE = set()   # item ids in the simulator's launch and pre-raid presets (every class)
PRE_NAMES = ("launch", "p0", "prebis", "preraid", "pre-bis", "pre_raid")


def load_vetted_pre(repo):
    for p in G.preset_files(repo):   # the official repository's presets and the fork's vendored ones (2026-10-22)
        if any(k in p.name for k in PRE_NAMES) and "p2" not in p.name:
            VETTED_PRE.update(x["id"] for x in json.load(open(p, encoding="utf-8")).get("items", []) if x and x.get("id"))


def crafted_ok(it, tier):
    """A crafted-only item's tier rule (see the lists above); True for items with any other source."""
    srcs = it.get("sources") or []
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


def pool_of(tier, zones):
    def bis(it):
        return G.in_pool(it, zones) and crafted_ok(it, "bis")

    def prebis(it):
        if it.get("quality", 0) >= 5 or it.get("quality", 0) < 2 or it.get("name") in RAID_QUEST or not crafted_ok(it, "prebis")                 or it.get("id") in G.SUSPECT_ITEMS:
            return False
        srcs = it.get("sources") or []
        drops = [s["drop"] for s in srcs if s.get("drop")]
        zs = {zones.get(d.get("zoneId")) for d in drops} - {None}
        if drops and len(drops) == len(srcs) and zs and zs <= RAID_ZONES:
            return False   # dropped only in raids
        npcs = {d.get("npcId") for d in drops}
        if npcs and npcs <= G.WORLD_BOSSES | G.EVENT_NPCS:
            return False
        if it["id"] in G.VENDOR_ITEMS:
            return True
        if not srcs:
            so = it.get("scalingOptions", {}).get("0", {})
            return it["id"] in VETTED_PRE and so.get("ilvl", 0) <= G.SOURCELESS_MAX_ILVL
        return True
    return bis if tier == "bis" else prebis


def optimize_set(cls, evals, cur_items, pool, repo, db, a, tag, keep_current, weights_fn=None, score=None, extra=None):
    """The best set for the evaluations [(entry name, entry, setting, talents, label)] from `pool`: the same steps as gear_opt.optimize
    (weights, greedy per slot in two variants, weights again, trinket pairs raced, variants raced, seed-2 confirmation), except that the
    current item of a slot competes only when `keep_current` or the pool admits it (a pre-raid set must not keep raid items).
    `weights_fn(items)` -> {stat name: value per point} and `score(bench row)` -> float replace the simulator's DPS weights and DPS (both
    None for damage specs, unchanged; tank_gear.py passes tank value, 2026-10-15). `extra` {name: items}: sets that compete with the
    variants, each also with the raced trinket pair, when every item is in the pool; one named "previous" (the tier's last set) is the
    reference a new set must beat on seed 2 (2026-10-16: the Expertise re-gear's pre-BiS Enhancement set lost 1.6% to the set it
    replaced, which never raced it)."""
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
    in_tier = all(x["id"] in db and pool(db[x["id"]]) for x in cur_items if x.get("id"))   # a missing item is out of the pool (2026-10-22)
    keep_current = keep_current and in_tier   # the current set competes only when every item is in the tier's pool
    sets = ({"current": cur_items} if keep_current else {}) | {"all-slots": v1, "keep-sets-and-effects": v2}
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
            "race_seed1": r1, "confirm_seed2": r2, "chosen": chosen,
            "ilvl": ilvl(items), "items": items, "names": [db.get(x.get("id"), {}).get("name") if x.get("id") else None for x in items]}


def set_path(cls, spec, tier):
    return SETS / f"{cls}-{SM.slug(spec)}-{tier}.gear.json"


def make(cls, spec, tier, entry_name, talents, label, repo, db, zones, a, path=None, setting="raid"):
    """The tier's set for one spec: written to its gear file (`path`: another file, e.g. the full-raid winner's set of a spec whose
    full-raid winner plays another entry; ml_pipeline.final), returned as the record. Chosen in a full raid (`setting`, since
    2026-10-31: the pages rank by full-raid DPS; sets chosen on the training dummy, short of mana, had weighed haste below zero for the
    Frostfire mage, and its full-raid set measured +2.7% over the dummy's, confirmed on seed 2)."""
    e = R.SPECS[cls][entry_name]
    cur = json.load(open(R.sim_path(e["gear"]) if pathlib.Path(R.sim_path(e["gear"])).is_absolute() else repo / e["gear"], encoding="utf-8"))["items"]
    pool = pool_of(tier, zones)
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
    r = optimize_set(cls, [(entry_name, e, setting, talents, label)], cur, pool, repo, db, a, f"{cls}-{SM.slug(spec)}-{tier}", keep_current=(tier == "bis"),
                     extra={"previous": prev} if prev else None)
    if tmpl:
        FE.fill(r["items"], tmpl)
    dropped = G.drop_missing_enchants(r["items"], repo)   # an enchant carried from a set the official database lacks (2026-10-22)
    if dropped:
        r["enchants_dropped"] = dropped
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps({"items": r["items"]}, indent=1) + "\n", encoding="utf-8")
    return dict(r, entry=entry_name, gear=p.relative_to(ROOT).as_posix(), date=TODAY, setting=setting)


def load_db(repo):
    db, zones = G.load_db(repo)
    G.load_vetted(repo, db)
    load_vetted_pre(repo)
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
                    "evaluated_on", "enchants_dropped")
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
