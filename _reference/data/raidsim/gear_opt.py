"""Equal-tier raid gear for every damage spec (2026-09-30, user request: the cross-spec raid ranking mixed gear levels).

    python _reference/data/raidsim/gear_opt.py [classes] [--write] [--apply]

The simulator's gear presets are not one tier: the warrior's "p1" sets average item level 59, Shadow's pre-raid set 60, the paladin's
default 61, while mage, hunter, warlock and rogue sets are phase-1 raid gear (65-68). So the class ranking partly ranked gear. This
builds, for every group of raid entries sharing a gear set, the best **phase-1** set we can find and keeps it only when the simulator
says it beats the current one:

1. Pool: items that drop in 5-man dungeons, Molten Core, Onyxia's Lair or the open world, plus crafted items and quest rewards;
   items with no source listed (custom, later-phase quest and PvP rewards) only when a phase-1, launch or pre-raid community preset
   uses them; no Blackwing Lair, Zul'Gurub, Ahn'Qiraj or Naxxramas, no world-boss drops (Azuregos, Kazzak and the Dragons of Nightmare came in phase 2 and later), no legendaries (the item database's own
   `phase` field puts Ahn'Qiraj in phase 1, so the source decides). The class must be allowed (classAllowlist), armor no heavier
   than the class wears at 60, weapons of a type the class's presets use, in the same weapon setup as the current set (two-hander,
   dual wield, one-hander + off-hand or shield, the same ranged or relic type).
2. Stat weights: the simulator's own (bench `statweights`, the entry's rotation and setting, the group's best build of ours);
   an item's value = its stats x weights, weapon DPS x the hand's DPS weight. Recomputed once on the new set (hit caps move).
3. Per slot the best item by that value (two variants: every slot, and every slot but the current set pieces and items with an
   on-use or proc effect, which stat weights cannot value); trinkets are raced in the simulator from every trinket in the class's
   presets, and relics (idol, libram, totem) stay.
4. Race: the current set and both variants on each entry's best build (seed 1), the leader confirmed on seed 2 with more iterations;
   a new set is kept only when it wins by more than --min-gain on the average of the group's entries.
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
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[2]
sys.path[:0] = [str(ROOT / "_reference/data"), str(HERE)]
import paths  # noqa: E402

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
ARMOR_MAX = {"warrior": 4, "paladin": 4, "hunter": 3, "shaman": 3, "rogue": 2, "druid": 2, "mage": 1, "priest": 1, "warlock": 1}
CLASS_ID = {"warrior": 1, "paladin": 2, "hunter": 3, "rogue": 4, "priest": 5, "shaman": 7, "mage": 8, "warlock": 9, "druid": 11}
SLOT_TYPE = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 11, 12, 12, 13, 13, 14]   # ItemSlot index -> ItemType
STAT = {}   # Stat enum index -> name (filled from a weights row)


def load_db(repo):
    db = json.load(open(repo / "assets/database/db.json", encoding="utf-8"))
    zones = {z["id"]: z["name"] for z in db["zones"]}
    return {i["id"]: i for i in db["items"]}, zones


def in_pool(it, zones):
    if it.get("quality", 0) >= 5 or it.get("quality", 0) < 2:
        return False
    so = it.get("scalingOptions", {}).get("0", {})
    zs = {zones.get(s.get("drop", {}).get("zoneId")) for s in it.get("sources", []) if s.get("drop")}
    zs.discard(None)
    if zs & RAID_NO and not zs - RAID_NO:
        return False
    npcs = {s.get("drop", {}).get("npcId") for s in it.get("sources", []) if s.get("drop")}
    if npcs and npcs <= WORLD_BOSSES:   # Classic phase 2 and later (Azuregos, Kazzak, the Dragons of Nightmare)
        return False
    if not it.get("sources"):   # no source listed (custom, later-phase quest or PvP rewards): only items a phase-1 community preset uses
        return it["id"] in VETTED and so.get("ilvl", 0) <= SOURCELESS_MAX_ILVL
    return True


VETTED = set()   # item ids in the simulator's phase-0/1, launch and pre-raid presets (every class)


def load_vetted(repo):
    for p in (repo / "ui/specs").glob("*/*/gear_sets/*.gear.json"):
        if "p2" in p.name or "phase_2" in p.name:
            continue
        VETTED.update(x["id"] for x in json.load(open(p, encoding="utf-8")).get("items", []) if x and x.get("id"))


def value(it, w, slot):
    so = it.get("scalingOptions", {}).get("0", {})
    v = sum(w.get(STAT.get(int(k)), 0.0) * x for k, x in so.get("stats", {}).items())
    if it.get("type") in (13, 14) and so.get("weaponDamageMax") and it.get("weaponSpeed"):
        dps = (so["weaponDamageMin"] + so["weaponDamageMax"]) / 2 / it["weaponSpeed"]
        key = {14: "PseudoStatMainHandDps", 15: "PseudoStatOffHandDps", 16: "PseudoStatRangedDps"}.get(slot)
        v += w.get(key, 0.0) * dps
    return v


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

    # the class's weapon types and trinkets, from every preset of the class (the community's picks)
    presets = list((repo / "ui/specs").glob(f"{cls}/*/gear_sets/*.gear.json")) + list(SETS.glob(f"{cls}*.gear.json"))
    seen = [x.get("id") for p in presets for x in json.load(open(p, encoding="utf-8")).get("items", []) if x and x.get("id")]
    wtypes = {db[i].get("weaponType") for i in seen if i in db and db[i].get("type") == 13}
    rtypes = {db[i].get("rangedWeaponType") for i in seen if i in db and db[i].get("type") == 14}
    trinkets = sorted({i for i in seen if i in db and db[i].get("type") == 12 and in_pool(db[i], zones)})

    def fits(it, slot, curit):
        if it.get("type") != SLOT_TYPE[slot] or not in_pool(it, zones):
            return False
        if it.get("classAllowlist") and CLASS_ID[cls] not in it["classAllowlist"]:
            return False
        if it.get("armorType", 0) > ARMOR_MAX[cls]:
            return False
        if it.get("randomSuffixOptions") or not it.get("scalingOptions", {}).get("0", {}).get("stats") and it.get("type") not in (13, 14):
            return False
        if SLOT_TYPE[slot] == 13:
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
        if SLOT_TYPE[slot] == 14:
            if not curit or it.get("rangedWeaponType") != curit.get("rangedWeaponType") or it.get("rangedWeaponType") not in rtypes:
                return False
        return True

    def greedy(items, w, keep_special):
        new = [dict(x) if x else {} for x in items]
        used = set()
        for slot in range(17):
            curx = new[slot]
            curit = db.get(curx.get("id")) if curx.get("id") else None
            if SLOT_TYPE[slot] == 12 or (curit and curit.get("rangedWeaponType", 0) in (6, 7, 8, 9)):
                used.add(curx.get("id"))
                continue   # trinkets are raced; relics stay
            if slot == 15 and new[14].get("id") and db.get(new[14]["id"], {}).get("handType") == 4:
                new[15] = {}
                continue
            if keep_special and curit and (curit.get("setName") or curit.get("itemEffects")):
                used.add(curx.get("id"))
                continue
            if not curit and slot not in (15,):
                continue
            cands = [it for it in db.values() if fits(it, slot, curit) and it["id"] not in used]
            if curit:
                cands.append(curit)
            best = max(cands, key=lambda it: value(it, w, slot)) if cands else curit
            if best and best["id"] != curx.get("id"):
                ench = curx.get("enchant")
                new[slot] = {"id": best["id"], **({"enchant": ench} if ench else {})}
            used.add(new[slot].get("id"))
        return new

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

    w = weights(cur_items)
    if not STAT:
        order = ["StatStrength", "StatAgility", "StatStamina", "StatIntellect", "StatHealingPower", "StatSpellDamage", "StatArcaneDamage",
                 "StatFireDamage", "StatFrostDamage", "StatHolyDamage", "StatNatureDamage", "StatShadowDamage", "StatSpellHitRating",
                 "StatSpellCritRating", "StatSpellHasteRating", "StatSpellPiercing", "StatSpirit", "StatAttackPower", "StatRangedAttackPower",
                 "StatFeralAttackPower", "StatMeleeHitRating", "StatMeleeCritRating", "StatMeleeHasteRating", "StatArmorPenetration",
                 "StatExpertiseRating", "StatDefenseRating", "StatBlockRating", "StatBlockValue", "StatDodgeRating", "StatParryRating", "StatArmor",
                 "StatBonusArmor", "StatHealth", "StatMana", "StatMP5"]
        STAT.update(enumerate(order))
    v1, v2 = greedy(cur_items, w, False), greedy(cur_items, w, True)
    w = weights(v1)   # the hit caps move with the new gear: weigh again on it
    v1, v2 = greedy(v1, w, False), greedy(v2, w, True)
    # trinkets: every pair of the class's preset trinkets, raced on the main entry with the first variant
    pairs = [p for p in itertools.combinations(trinkets, 2)][: a.max_pairs]
    cur_pair = (cur_items[12].get("id"), cur_items[13].get("id"))
    tsets = {"cur": v1, **{f"t{i}": with_trinkets(v1, p) for i, p in enumerate(pairs)}}
    tr = race(tsets, a.iterations, 1)
    tbest = max(tr, key=tr.get)
    pair = cur_pair if tbest == "cur" else pairs[int(tbest[1:])]
    v1, v2 = with_trinkets(v1, pair), with_trinkets(v2, pair)
    sets = {"current": cur_items, "all-slots": v1, "keep-sets-and-effects": v2}
    r1 = race(sets, a.iterations, 1)
    lead = max(r1, key=r1.get)
    r2 = race({"current": cur_items, lead: sets[lead]}, a.confirm, 2) if lead != "current" else {"current": 1.0}
    gain = r2.get(lead, 1.0) - 1
    keep = lead != "current" and gain > a.min_gain
    ilvl = lambda items: sum(db[x["id"]]["scalingOptions"]["0"].get("ilvl", 0) for x in items if x.get("id") in db) / max(1, sum(1 for x in items if x.get("id") in db))  # noqa: E731
    return {"gear": gear, "members": [f"{c}/{n}" for c, n in members], "evaluated_on": [f"{n}: {lab}" for n, _, _, _, lab in evals],
            "weights": {k: round(v, 4) for k, v in w.items() if abs(v) > 1e-6}, "trinkets": [db[i]["name"] for i in pair if i in db],
            "race_seed1": r1, "confirm_seed2": r2, "chosen": lead if keep else "current", "gain": gain if keep else 0.0,
            "ilvl_before": round(ilvl([x for x in cur_items if x]), 1), "ilvl_after": round(ilvl([x for x in (sets[lead] if keep else cur_items) if x]), 1),
            "items": [x for x in (sets[lead] if keep else cur_items)], "changed": [
                {"slot": s, "from": db.get(cur_items[s].get("id"), {}).get("name"), "to": db.get(sets[lead][s].get("id"), {}).get("name")}
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
    load_vetted(repo)
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
        if r["chosen"] == "current":
            continue
        cls = r["members"][0].split("/")[0]
        gp = pathlib.Path(gear)   # ui/specs/<class>/<spec>/gear_sets/<name>: the spec folder keeps sets of one class apart
        spec_dir = gp.parent.parent.name if gp.parent.name == "gear_sets" else "project"
        name = f"{cls}-{spec_dir}-{gp.name.split('.')[0]}.p1opt.gear.json"
        (SETS / name).write_text(json.dumps({"items": r["items"]}, indent=1) + "\n", encoding="utf-8")
        new = f"_reference/data/raidsim/gear_sets/forever/{name}"
        text = text.replace(f'"gear": "{gear}"', f'"gear": "{new}"')
        print(f"{gear} -> {new} ({r['gain']:+.2%}, item level {r['ilvl_before']} -> {r['ilvl_after']})")
    sp.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
