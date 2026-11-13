"""Healer stat values at 60 for the gear add-on (2026-11-13; user: "I want the add-on to be usable across all classes and specs").

    python -u _reference/data/heallab/heal_values.py [classes] [--jobs 10] [--smoke]

Per healer spec of heallab/heal-gear.json (heal_gear.py: priest Holy and Discipline, paladin Holy, druid and shaman Restoration): the
spec's raid pick (heal_gear.raid_pick) in its phase-1 BiS set with the set's own haste counted (tables.HEALER_GEAR "haste_gear", 10
rating = 1%), every gear stat moved +-delta on common seeds (heal_gear.measure_weights: central differences of the capacity's tail mean,
paired-bootstrap errors): healing power, Intellect, Spirit, mp5, crit and haste; haste once more with the global cooldown hasted too
(tables.HASTE_GCD, open: forever-stats.md row 7). Record heallab/heal-values.json, values in healing-power units (1 healing = 1) and per
rating point. Stamina, armor and resistances read 0 (the lab never damages the healer); spell damage 0 (no healer in the lab heals by
dealing damage). Capacity is the healer lab's model of stated assumptions, not a measurement.
"""
import argparse
import datetime
import json
import os
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import heal_gear as HG  # noqa: E402

RECORD = HERE / "heal-values.json"
HASTE_DELTA = 0.03      # 30 haste rating
RATING = {"crit_gear": 14.0, "haste_gear": 10.0}   # rating per 1% (forever-stats.md: the same at every level)


def lab_stats(path):
    st = HG.gear_stats(path)
    g = HG.lab_gear(st)
    g["haste_gear"] = round(st["ignored"]["haste_rating"] / 10.0 / 100.0, 6)
    return g, st


def clean(w):
    out = {}
    for k, v in w.items():
        name = {"crit_gear": "crit_rating", "haste_gear": "haste_rating"}.get(k, k)
        f = 0.01 / RATING[k] if k in RATING else 1.0     # per rating point for crit and haste
        out[name] = {"healing_eq": round((v["hp_eq"] or 0.0) * f, 4), "healing_eq_se": round((v["hp_eq_se"] or 0.0) * f, 4),
                     "z": round(v["z"], 2) if v.get("z") is not None else None}
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("classes", nargs="*")
    ap.add_argument("--jobs", type=int, default=10)
    ap.add_argument("--smoke", action="store_true")
    a = ap.parse_args()
    B = dict(weight_seeds=40, weight_steps=4, boot=50) if a.smoke else dict(weight_seeds=800, weight_steps=12, boot=400)
    rec = json.loads(HG.RECORD.read_text(encoding="utf-8"))
    out = {"date": datetime.date.today().isoformat(), "budgets": B, "deltas": dict(HG.DELTA, haste_gear=HASTE_DELTA),
           "unit": "healing power per point (crit and haste: per rating point)", "specs": {}}
    seeds = list(range(HG.WEIGHT_SEED0, HG.WEIGHT_SEED0 + B["weight_seeds"]))
    HG.DELTA["haste_gear"] = HASTE_DELTA
    for key, r in rec["specs"].items():
        cls, spec = r["class"], r["spec"]
        if a.classes and cls not in a.classes:
            continue
        bid, alloc, _ = HG.raid_pick(cls, spec)
        gear, st = lab_stats(r["sets"]["bis"]["gear"])
        row = {"class": cls, "spec": spec, "build": bid, "gear": r["sets"]["bis"]["gear"], "stats": gear}
        for gcd in (False, True):
            os.environ["WOW_HL_HASTE_GCD"] = "1" if gcd else "0"
            lab = HG.Lab(cls, alloc, a.jobs)
            try:
                if not gcd:
                    w, c, cse = HG.measure_weights(lab, gear, seeds, B["weight_steps"], B["boot"])
                    row.update(capacity=round(c, 4), capacity_se=round(cse, 4), values=clean(w))
                else:
                    keep = dict(HG.DELTA)
                    HG.DELTA.clear(); HG.DELTA.update(healing=keep["healing"], haste_gear=HASTE_DELTA)
                    try:
                        w, c, _ = HG.measure_weights(lab, gear, seeds, B["weight_steps"], B["boot"])
                    finally:
                        HG.DELTA.clear(); HG.DELTA.update(keep)
                    row["haste_if_gcd_hasted"] = clean(w)["haste_rating"]
            finally:
                lab.close()
        os.environ.pop("WOW_HL_HASTE_GCD", None)
        out["specs"][key] = row
        v = row["values"]
        print(f"{cls:8s} {spec:12s} {bid}: capacity {row['capacity']:.4f}; " + ", ".join(f"{k} {x['healing_eq']:.3f}±{x['healing_eq_se']:.3f}" for k, x in v.items())
              + f"; haste with a hasted GCD {row['haste_if_gcd_hasted']['healing_eq']:.3f}", flush=True)
    if not a.smoke:
        RECORD.write_text(json.dumps(out, indent=1) + "\n", encoding="utf-8", newline="\n")
        print(f"wrote {RECORD.relative_to(HG.ROOT).as_posix()}")


if __name__ == "__main__":
    main()
