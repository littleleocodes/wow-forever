"""Leveling page builds raced with their own spec's rotation (2026-10-08).

    python -u _reference/data/fightlab/own_rotation_race.py [classes] [--jobs 8] [--fresh]

User decision 2026-10-08: "I don't want classes specs taking other specs rotations or builds or anything just because it's faster." A
leveling build on a spec's page may only be played with a rotation built for that spec's tree (a hybrid: either of its two trees;
spec_modes.leveling_rotation_trees). Some page builds carried numbers from another rotation: hand drafts and optimizer builds whose points
put them in another spec than the rotation they were made for (the hunter's leveling-beast-mastery has 30+ Marksmanship points and played
the Beast Mastery rotation), and open-search winners shown with a faster sibling rotation. This races each such build at levels 20-60
(weights level / 10, seed 3, 3,000 fights per level, the open search's race) with its own spec's rotation (spec_modes.own_leveling_rotation:
the tree's derive_leveling.LEVEL rotation; a hybrid's spec_modes.HYBRID_LEVELING_ROTATION since 2026-10-22, the rotation that plays its
signature spells, before that its lead tree's) and its own talent order (the stats model's for that tree when it has
none). Record fightlab/own-rotation.json ({class: {build id: {rotation, levels, weighted, was, date}}}), which render_modes reads last.
The fight lab is this project's model of stated assumptions, not an in-game measurement.
"""
import argparse
import datetime
import json
import multiprocessing
import os
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[2]
sys.path[:0] = [str(HERE), str(ROOT / "_reference/data/scorer"), str(ROOT / "_reference/data")]
import fl_talent_opt as FT  # noqa: E402

OUT = HERE / "own-rotation.json"
TODAY = datetime.date.today().isoformat()
FIGHTS, SEED = 3000, 3


def mismatched(cls):
    """[(build, spec, current rotation, own rotation)] for the class's leveling page builds played with another spec's rotation."""
    import render_modes as RM
    import render_rotations as rr
    import spec_modes as SM
    B = rr.builds(cls)
    g = SM.grid(cls, list(B.values()))
    L = RM.leveling_numbers(cls)
    trees_of = SM.leveling_rotation_trees(cls)
    out = []
    for spec, modes in g.items():
        for b in modes.get("leveling") or []:
            rot = RM.LEVEL_MODEL.get((cls, b["id"]))
            if not RM.weighted(L.get(b["id"]) or {}) or rot is None:
                continue
            if SM.leveling_rotation_ok(cls, spec, rot, trees_of.get(rot)):   # (2026-10-22: a hybrid only with its HYBRID_LEVELING_ROTATION)
                continue
            own = SM.own_leveling_rotation(cls, spec, b["allocation"])
            if own:
                out.append((b, spec, rot, own))
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("classes", nargs="*")
    ap.add_argument("--jobs", type=int, default=max(1, (os.cpu_count() or 4) - 2))
    ap.add_argument("--fresh", action="store_true", help="race again builds the record already holds")
    a = ap.parse_args()
    import derive_leveling as DL
    import spec_modes as SM
    st = json.load(open(OUT, encoding="utf-8")) if OUT.exists() else {}
    classes = a.classes or SM.CLASSES
    with multiprocessing.Pool(a.jobs, initializer=FT._init, initargs=("greens",)) as pool:
        for cls in classes:
            todo = [x for x in mismatched(cls) if a.fresh or x[0]["id"] not in (st.get(cls) or {})]
            if not todo:
                print(f"== {cls}: every leveling page build plays its own spec's rotation", flush=True)
                continue
            print(f"== {cls}: {len(todo)} page builds played with another spec's rotation", flush=True)
            for b, spec, rot, own in todo:
                tree = spec if not spec.startswith("Hybrid ") else max(spec[len("Hybrid "):].split("/"),
                                                                       key=lambda t: sum(k for _, k in b["allocation"].get(t, [])))
                model = (DL.LEVEL.get((cls, tree)) or (own, own))[1]
                order = b.get("order") or FT.order_of(cls, model, FT.flat_of(b))
                if not b.get("order"):   # 2026-11-06 (page-audit L3): an order made here takes the signature talents as early as the tree allows
                    order = FT.FS.sig_order(cls, own, {"allocation": b["allocation"], "order": order})
                w, per = FT.race(pool, cls, own, [{"id": b["id"], "allocation": b["allocation"], "order": order}], FIGHTS, SEED)[0]
                st.setdefault(cls, {})[b["id"]] = {"rotation": own, "levels": {str(L): round(v, 2) for L, v in per.items()},
                                                   "weighted": round(w, 2), "was": rot, "spec": spec, "date": TODAY}
                OUT.write_text(json.dumps(st, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
                print(f"  {cls} {spec}: {b['id']} with {own} (its own) {w:.2f} s per kill at 20-60 (it had played {rot})", flush=True)
    print("== done", flush=True)


if __name__ == "__main__":
    main()
