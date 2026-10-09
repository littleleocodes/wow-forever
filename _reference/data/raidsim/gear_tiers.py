"""Pre-BiS and phase-1 BiS gear for every raid damage spec (2026-10-01, user request: "DPS rankings for pre-BiS as well as best in slot,
like WoWSims does").

    python _reference/data/raidsim/gear_tiers.py --set <class> "<spec>" <tier> --entry <entry> --build <build id | candidate .json>

(ml_pipeline.py makes every spec's sets through `make`.)

Two tiers, one item pool each (the simulator's item database, ElliotWood/Forever 40be98e):
- **bis** (phase 1): `gear_opt.py`'s pool: dungeons, Molten Core, Onyxia, world drops, crafted, quest; items with no listed source only
  when a community phase-0/1, launch or pre-raid preset uses them (the Forever launch items); no BWL, ZG, AQ, Naxxramas, world bosses
  or legendaries; the hunter's Molten Core quest bow and stave (Rhok'delar, Lok'delar) count.
- **prebis** (pre-raid): the same without any raid drop, without the quest rewards of raid bosses and without crafted items made from
  Molten Core or Onyxia materials (`PHASE1_RAID_MADE`, our list: the database has the recipe, not its materials); items with no listed
  source only when a launch or pre-raid preset uses them.
Unlike gear_opt.py, which gives every group of entries sharing a set one compromise set, each spec gets its own set per tier
(a Fire mage wants fire damage, a Frost mage frost damage): the simulator's stat weights for the spec's best build in its entry
(bench `statweights`), the best item per slot by those weights (two variants: every slot, and one keeping set pieces and items with
effects), the weights refreshed once on the new set (hit caps move), the class's preset trinket pairs raced, the variants raced on
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
    for p in (repo / "ui/specs").glob("*/*/gear_sets/*.gear.json"):
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
        if it.get("quality", 0) >= 5 or it.get("quality", 0) < 2 or it.get("name") in RAID_QUEST or not crafted_ok(it, "prebis"):
            return False
        srcs = it.get("sources") or []
        drops = [s["drop"] for s in srcs if s.get("drop")]
        zs = {zones.get(d.get("zoneId")) for d in drops} - {None}
        if drops and len(drops) == len(srcs) and zs and zs <= RAID_ZONES:
            return False   # dropped only in raids
        npcs = {d.get("npcId") for d in drops}
        if npcs and npcs <= G.WORLD_BOSSES | G.EVENT_NPCS:
            return False
        if not srcs:
            so = it.get("scalingOptions", {}).get("0", {})
            return it["id"] in VETTED_PRE and so.get("ilvl", 0) <= G.SOURCELESS_MAX_ILVL
        return True
    return bis if tier == "bis" else prebis


def optimize_set(cls, evals, cur_items, pool, repo, db, a, tag, keep_current):
    """The best set for the evaluations [(entry name, entry, setting, talents, label)] from `pool`: the same steps as gear_opt.optimize
    (weights, greedy per slot in two variants, weights again, trinket pairs raced, variants raced, seed-2 confirmation), except that the
    current item of a slot competes only when `keep_current` or the pool admits it (a pre-raid set must not keep raid items)."""
    main = evals[0]
    cur_items = [dict(x) if x else {} for x in cur_items] + [{}] * (17 - len(cur_items))

    def weights(items):
        cfg = G.bench_cfg(main[1], repo, [{"label": "w", "talents": main[3], "gear_json": {"items": items}}], a.weight_iterations, 1, main[2], statweights=True)
        row = G.run_bench(repo, cfg, f"w-{tag}")["w"]
        if row.get("error"):
            raise SystemExit(f"stat weights failed for {tag}: {row['error']}")
        return row["weights"]

    presets = list((repo / "ui/specs").glob(f"{cls}/*/gear_sets/*.gear.json")) + list(G.SETS.glob(f"{cls}*.gear.json"))
    seen = [x.get("id") for p in presets for x in json.load(open(p, encoding="utf-8")).get("items", []) if x and x.get("id")]
    wtypes = {db[i].get("weaponType") for i in seen if i in db and db[i].get("type") == 13}
    rtypes = {db[i].get("rangedWeaponType") for i in seen if i in db and db[i].get("type") == 14}
    trinkets = sorted({i for i in seen if i in db and db[i].get("type") == 12 and pool(db[i])})

    def fits(it, slot, curit):
        if it.get("type") != G.SLOT_TYPE[slot] or not pool(it):
            return False
        if it.get("classAllowlist") and G.CLASS_ID[cls] not in it["classAllowlist"]:
            return False
        if it.get("armorType", 0) > G.ARMOR_MAX[cls]:
            return False
        if it.get("randomSuffixOptions") or not it.get("scalingOptions", {}).get("0", {}).get("stats") and it.get("type") not in (13, 14):
            return False
        if G.SLOT_TYPE[slot] == 13:
            if it.get("weaponType") not in wtypes:
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
        if G.SLOT_TYPE[slot] == 14:
            if not curit or it.get("rangedWeaponType") != curit.get("rangedWeaponType") or it.get("rangedWeaponType") not in rtypes:
                return False
        return True

    def greedy(items, w, keep_special):
        new = [dict(x) if x else {} for x in items]
        used = set()
        for slot in range(17):
            curx = new[slot]
            curit = db.get(curx.get("id")) if curx.get("id") else None
            if G.SLOT_TYPE[slot] == 12 or (curit and curit.get("rangedWeaponType", 0) in (6, 7, 8, 9)):
                used.add(curx.get("id"))
                continue   # trinkets are raced; relics stay
            if slot == 15 and new[14].get("id") and db.get(new[14]["id"], {}).get("handType") == 4:
                new[15] = {}
                continue
            allowed = curit is not None and pool(curit)   # never keep an item outside the tier's pool
            if keep_special and allowed and (curit.get("setName") or curit.get("itemEffects")):
                used.add(curx.get("id"))
                continue
            if not curit and slot not in (15,):
                continue
            cands = [it for it in db.values() if fits(it, slot, curit) and it["id"] not in used]
            if allowed and not (curit["id"] in used and curit.get("unique")):   # a unique-equipped item held earlier in the set: not twice (2026-10-06)
                cands.append(curit)
            best = max(cands, key=lambda it: G.value(it, w, slot)) if cands else (curit if allowed else None)
            if best is None:
                new[slot] = {}
                continue
            if best["id"] != curx.get("id"):
                ench = curx.get("enchant")
                new[slot] = {"id": best["id"], **({"enchant": ench} if ench else {})}
            used.add(new[slot].get("id"))
        return new

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
                out[k].append((rows[k].get("dps") or 0) / (ref.get("dps") or 1))
        return {k: sum(v) / len(v) for k, v in out.items()}

    w = weights(cur_items)
    if not G.STAT:
        G.STAT.update(enumerate(["StatStrength", "StatAgility", "StatStamina", "StatIntellect", "StatHealingPower", "StatSpellDamage",
                                 "StatArcaneDamage", "StatFireDamage", "StatFrostDamage", "StatHolyDamage", "StatNatureDamage", "StatShadowDamage",
                                 "StatSpellHitRating", "StatSpellCritRating", "StatSpellHasteRating", "StatSpellPiercing", "StatSpirit",
                                 "StatAttackPower", "StatRangedAttackPower", "StatFeralAttackPower", "StatMeleeHitRating", "StatMeleeCritRating",
                                 "StatMeleeHasteRating", "StatArmorPenetration", "StatExpertiseRating", "StatDefenseRating", "StatBlockRating",
                                 "StatBlockValue", "StatDodgeRating", "StatParryRating", "StatArmor", "StatBonusArmor", "StatHealth", "StatMana",
                                 "StatMP5"]))
    v1, v2 = greedy(cur_items, w, False), greedy(cur_items, w, True)
    w = weights(v1)
    v1, v2 = greedy(v1, w, False), greedy(v2, w, True)
    cur_pair = (cur_items[12].get("id"), cur_items[13].get("id"))
    pairs = [p for p in itertools.combinations(trinkets, 2)][: a.max_pairs]
    base_pair = cur_pair if all(cur_pair) and all(pool(db[i]) for i in cur_pair if i in db) else (pairs[0] if pairs else cur_pair)
    v1 = with_trinkets(v1, base_pair) if all(base_pair) else v1
    tsets = {"base": v1, **{f"t{i}": with_trinkets(v1, p) for i, p in enumerate(pairs)}}
    tr = race(tsets, a.iterations, 1)
    tbest = max(tr, key=tr.get)
    pair = base_pair if tbest == "base" else pairs[int(tbest[1:])]
    if all(pair):
        v1, v2 = with_trinkets(v1, pair), with_trinkets(v2, pair)
    in_tier = all(pool(db[x["id"]]) for x in cur_items if x.get("id") in db)
    keep_current = keep_current and in_tier   # the current set competes only when every item is in the tier's pool
    sets = ({"current": cur_items} if keep_current else {}) | {"all-slots": v1, "keep-sets-and-effects": v2}
    r1 = race(sets, a.iterations, 1)
    lead = max(r1, key=r1.get)
    ref = "current" if keep_current else ("keep-sets-and-effects" if lead == "all-slots" else "all-slots")
    r2 = race({ref: sets[ref], lead: sets[lead]}, a.confirm, 2) if lead != ref else {ref: 1.0}
    gain = r2.get(lead, 1.0) - 1
    chosen = lead if (lead != ref and gain > (a.min_gain if keep_current else 0.0)) else ref
    items = sets[chosen]
    ilvl = lambda its: round(sum(db[x["id"]]["scalingOptions"]["0"].get("ilvl", 0) for x in its if x.get("id") in db) / max(1, sum(1 for x in its if x.get("id") in db)), 1)  # noqa: E731
    return {"evaluated_on": [f"{n}: {lab}" for n, _, _, _, lab in evals], "weights": {k: round(v, 4) for k, v in w.items() if abs(v) > 1e-6},
            "trinkets": [db[i]["name"] for i in pair if i in db], "race_seed1": r1, "confirm_seed2": r2, "chosen": chosen,
            "ilvl": ilvl(items), "items": items, "names": [db.get(x.get("id"), {}).get("name") if x.get("id") else None for x in items]}


def set_path(cls, spec, tier):
    return SETS / f"{cls}-{SM.slug(spec)}-{tier}.gear.json"


def make(cls, spec, tier, entry_name, talents, label, repo, db, zones, a):
    """The tier's set for one spec: written to its gear file, returned as the record."""
    e = R.SPECS[cls][entry_name]
    cur = json.load(open(R.sim_path(e["gear"]) if pathlib.Path(R.sim_path(e["gear"])).is_absolute() else repo / e["gear"], encoding="utf-8"))["items"]
    pool = pool_of(tier, zones)
    p = set_path(cls, spec, tier)
    # 2026-10-09: empty enchant slots are filled from the role's template before and after the search (fill_enchants.py: a set grown
    # from a preset without enchants kept none, the Balance, feral, Retribution, Arms and Fury sets)
    import fill_enchants as FE
    tmpl = FE.role(p.name)
    if tmpl:
        FE.fill(cur, tmpl)
    r = optimize_set(cls, [(entry_name, e, "dummy", talents, label)], cur, pool, repo, db, a, f"{cls}-{SM.slug(spec)}-{tier}", keep_current=(tier == "bis"))
    if tmpl:
        FE.fill(r["items"], tmpl)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps({"items": r["items"]}, indent=1) + "\n", encoding="utf-8")
    return dict(r, entry=entry_name, gear=p.relative_to(ROOT).as_posix(), date=TODAY)


def load_db(repo):
    db, zones = G.load_db(repo)
    G.load_vetted(repo)
    load_vetted_pre(repo)
    return db, zones


def args_ns(**kw):
    d = dict(iterations=3000, confirm=12000, weight_iterations=3000, min_gain=0.0, max_pairs=28)
    d.update(kw)
    return argparse.Namespace(**d)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--set", nargs=3, metavar=("CLASS", "SPEC", "TIER"), required=True)
    ap.add_argument("--entry", required=True)
    ap.add_argument("--build", required=True)
    ap.add_argument("--iterations", type=int, default=3000)
    ap.add_argument("--confirm", type=int, default=12000)
    ap.add_argument("--weight-iterations", type=int, default=3000)
    ap.add_argument("--min-gain", type=float, default=0.0, help="margin a new set needs over the current one (BiS tier; default: none)")
    ap.add_argument("--max-pairs", type=int, default=28)
    a = ap.parse_args()
    R.set_game("forever")
    repo = R.repo_path(argparse.Namespace(repo=None))
    db, zones = load_db(repo)
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
