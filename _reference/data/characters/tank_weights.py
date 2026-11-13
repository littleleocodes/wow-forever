"""Stat values for a group tank character, in the planner's format (2026-11-09, Tara: a Protection paladin who tanks for a group with a
healer; user: "a protection build that works in a group or a build order that leads into the level 60 protection build").

The character planner (plan.py) values gear in seconds per kill from the solo fight lab. A tank in a group is worth what it adds to the
group's tanking, so this takes the raid simulator's own stat weights for the spec's tank build (bench `statweights` with the entry's tank
setting: threat per second and damage taken per second per point of each stat, in the entry's gear and rotation) and combines them the
way the simulator scores a tank (run.tank_value: half the threat gain, half the mitigation), with the mitigation half split between the
damage avoided over a fight (the simulator's damage taken per second) and effective health, which the simulator does not score (damage
taken per second does not change with your health, so Stamina measured 0.003% a point against Defense's 0.10%, 2026-11-09):

    value per point = 0.5 x TPS weight / TPS + 0.25 x (-DTPS weight) / DTPS + 0.25 x EHP gain per point     (a share of tank value)
    EHP gain: Stamina 10 / health, Armor 1 / (armor + 400 + 85 x 63), Agility twice the Armor's (2 armor a point); health and armor of
    the entry's gear set at 60 plus the class's base (--hp-base, --sta-base, --agi-base) and Toughness' 10% on the items' armor (an
    estimate without raid buffs)

The planner counts a share of tank value as the same share of faster play (an assumption the page states: a better tank pulls more and
the healer drinks less), so the shares are written as seconds per kill at each level, from the spec's measured solo kill times
(level-guides/<class>.measured.json). One measurement at 60 stands for every level: the stat values of a level-60 raid tank in its gear.

    python -u _reference/data/characters/tank_weights.py paladin prot-tank protection-ml-tank Protection [--iterations 3000]
"""
import argparse
import datetime
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
DATA = HERE.parent
sys.path.insert(0, str(DATA / "raidsim"))
sys.path.insert(0, str(DATA))
sys.path.insert(0, str(HERE))
import run as R  # noqa: E402
import gear_opt as GO  # noqa: E402
import setup  # noqa: E402

KEYS = {"StatStrength": "strength", "StatAgility": "agility", "StatStamina": "stamina", "StatIntellect": "intellect",
        "StatSpirit": "spirit", "StatSpellDamage": "spell_power", "StatHealingPower": "healing", "StatAttackPower": "attack_power",
        "StatHitRating": "hit", "StatCritRating": "crit", "StatHasteRating": "haste", "StatExpertiseRating": "expertise",
        "StatDefenseRating": "defense", "StatBlockRating": "block", "StatBlockValue": "block_value", "StatDodgeRating": "dodge",
        "StatParryRating": "parry", "StatArmor": "armor", "StatMP5": "mp5", "PseudoStatMainHandDps": "weapon_dps"}


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("cls")
    ap.add_argument("entry")
    ap.add_argument("build")
    ap.add_argument("spec", help="the spec's by-level guide, for its measured kill times")
    ap.add_argument("--iterations", type=int, default=3000)
    ap.add_argument("--hp-base", type=float, default=1381, help="the class's base health at 60 (paladin 1381)")
    ap.add_argument("--sta-base", type=float, default=105, help="the race and class's base Stamina at 60 (Human paladin about 105)")
    ap.add_argument("--agi-base", type=float, default=65, help="base Agility at 60 (Human paladin about 65)")
    ap.add_argument("--armor-mult", type=float, default=1.10, help="Toughness' bonus on the items' armor (5/5: 10%%)")
    a = ap.parse_args()
    repo = setup.checkout()
    entry = R.SPECS[a.cls][a.entry]
    b = next(x for x in json.load(open(DATA.parent.parent / a.cls / "research" / "talents" / "forever" / "proposed-builds.json", encoding="utf-8"))["builds"]
             if x["id"] == a.build)
    flat = {n: r for items in b["allocation"].values() for n, r in items if r}
    tal = R.talents_string(R.load_trees(repo, a.cls), flat)
    where = R.setting(entry)
    base = GO.run_bench(repo, GO.bench_cfg(entry, repo, [{"label": "b", "talents": tal}], a.iterations, 1, where), f"tw-{a.cls}")["b"]
    sw = GO.run_bench(repo, GO.bench_cfg(entry, repo, [{"label": "w", "talents": tal}], a.iterations, 1, where, statweights=True),
                      f"tw-{a.cls}")["w"]
    if sw.get("error") or not base.get("threat") or not base.get("dtps"):
        raise SystemExit(f"stat weights failed: {sw.get('error') or base}")
    tps, dtps = base["threat"], base["dtps"]
    import item_pool as IP
    db = {it["id"]: it for it in IP.sim_db()["items"]}
    gear = {}
    gp = pathlib.Path(R.sim_path(entry["gear"]))   # a project set, or one of the simulator's own (warrior and bear tanks, 2026-11-13)
    for x in json.load(open(gp if gp.is_absolute() else pathlib.Path(repo) / entry["gear"], encoding="utf-8"))["items"]:
        for k, v in IP.lab_stats(db.get(x.get("id")) or {}, {}).items():
            gear[k] = gear.get(k, 0) + v
    hp = a.hp_base + 10 * (gear.get("stamina", 0) + a.sta_base - 20) + 20
    armor = a.armor_mult * gear.get("armor", 0) + 2 * (gear.get("agility", 0) + a.agi_base)
    k = 400 + 85 * 63
    ehp = {"stamina": 10 / hp, "armor": 1 / (armor + k), "agility": 2 / (armor + k)}
    share, raw = {}, {}
    for name, key in KEYS.items():
        t = (sw.get("weights") or {}).get(name, 0.0)
        d = (sw.get("dtps_weights") or {}).get(name, 0.0)
        raw[key] = {"tps": t, "dtps": d}
        v = 0.5 * t / tps + 0.25 * (-d) / dtps + 0.25 * ehp.get(key, 0.0)
        share[key] = share.get(key, 0.0) + v
    m = json.load(open(DATA / "level-guides" / f"{a.cls}.measured.json", encoding="utf-8"))["guides"][a.spec]["levels"]
    times = {int(k): v["seconds"] for k, v in m.items() if v.get("seconds")}
    lv = sorted(times)

    def t_at(L):
        lo = max([x for x in lv if x <= L], default=lv[0])
        hi = min([x for x in lv if x >= L], default=lv[-1])
        return times[lo] if hi == lo else times[lo] + (times[hi] - times[lo]) * (L - lo) / (hi - lo)

    levels = {str(L): {"time_per_kill": round(t_at(L), 3), "weights": {k: round(v * t_at(L), 6) for k, v in share.items()}}
              for L in range(10, 61)}
    out = {"class": a.cls, "spec": a.spec, "build": a.build, "entry": a.entry, "kind": "tank", "date": datetime.date.today().isoformat(),
           "iterations": a.iterations, "tps": tps, "dtps": dtps, "health": round(hp), "armor": round(armor),
           "share_per_point": {k: round(v, 7) for k, v in share.items()}, "raw_weights": raw,
           "unit": "seconds per kill per point: the share of tank value it adds (raid simulator, level-60 tank build in its gear) times the "
                   "spec's measured solo seconds per kill at that level",
           "levels": levels}
    p = HERE / "weights" / f"{a.cls}-tank.json"
    p.write_text(json.dumps(out, indent=1) + "\n", encoding="utf-8")
    print(f"wrote {p}: TPS {tps:.0f}, DTPS {dtps:.0f}, health about {hp:.0f}, armor about {armor:.0f}")
    for k, v in sorted(share.items(), key=lambda kv: -abs(kv[1])):
        print(f"  {k:13} {100 * v:+.4f}% tank value per point")


if __name__ == "__main__":
    main()
