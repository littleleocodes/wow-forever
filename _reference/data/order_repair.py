"""Give leveling builds without a talent order one (2026-10-15, page audit C1).

    python _reference/data/order_repair.py [classes] [--fights 3000] [--jobs 6] [--write]

The 2026-10-03 repair of the builds the 70170 trees broke rewrote allocations and dropped the `order` of nine leveling builds (warrior
Arms and Fury optimizer builds and `leveling-arms`, druid `leveling-feral` and `opt-feral-cat-dps-leveling-st`, mage Fire...). The fight
lab plays a build without an order with all 51 points from level 10 (`run.allocation_at`), so those builds read 5-10% fast at low levels
and beat builds raced with orders on the pages. This keeps each allocation and races three orders to it, the way raid_path_leveling.py
does for the healer and tank trees: the stats model's leveling order (Optimizer.order under the build's scorer model and profile),
own tree first, own tree last (moving whole trees keeps every tier legal); the fight lab plays each at levels 20-60 (the build's leveling
rotation, seed 3, --fights per level), the fastest by level-weighted time per kill is written with `order_label` and a note.
Skipped: builds with `raid_path` (raid_path_leveling.py writes those), solo builds (level 60, no order; since 2026-11-06 a solo build whose
order a repair dropped gets the stats model's leveling-st order back without a race: page-audit K2) and AoE builds (`-leveling-aoe`,
which get the stats model's order under their own profile without a race: the race plays single mobs).
"""
import argparse
import datetime
import json
import multiprocessing
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path[:0] = [str(HERE / "fightlab"), str(HERE / "scorer"), str(HERE)]
import run as FR  # noqa: E402  (fightlab/run.py)
import paths  # noqa: E402
import spec_modes as SM  # noqa: E402
import derive_leveling as DL  # noqa: E402
import raid_path_leveling as RP  # noqa: E402
import fl_signature as FS  # noqa: E402  (fightlab/fl_signature.py: signature talents as early as the tree allows)
from fmt_json import dumps  # noqa: E402

TODAY = datetime.date.today().isoformat()
CLASSES = ["druid", "hunter", "mage", "paladin", "priest", "rogue", "shaman", "warlock", "warrior"]


def models(cls, b, tree):
    """(fight-lab rotation, scorer model, profile) for a build: an optimizer build names its model and profile in its id."""
    spec, model = DL.LEVEL[(cls, tree)]
    profile = "leveling-st"
    if b["id"].startswith("opt-"):
        m = FR.spec_of_build(cls, b["id"], None)
        if m:
            spec = model = m
            profile = b["id"][4 + len(m) + 1:]
    return spec, model, profile


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("classes", nargs="*")
    ap.add_argument("--fights", type=int, default=3000)
    ap.add_argument("--jobs", type=int, default=6)
    ap.add_argument("--write", action="store_true")
    a = ap.parse_args()
    from optimize import Optimizer
    FR.apply_gear("greens")
    pool = multiprocessing.Pool(a.jobs)
    for cls in a.classes or CLASSES:
        bp = paths.builds_json("forever", cls)
        data = json.load(open(bp, encoding="utf-8"))
        changed = False
        for b in data["builds"]:
            # 2026-11-06 (page-audit K2): a solo build that had an order until a repair dropped it gets one back. The repairs' notes say
            # "order dropped (order_repair.py)", and this tool skipped every solo build: opt-feral-cat-dps-solo-60, the druid's recommended
            # leveling page build, had no talent table from 2026-10-30 on. Its page number is the open search's race row, raced with
            # the stats model's leveling-st order (fl_talent_opt.order_of), so that order is the one written, without a race.
            # 2026-11-06 (user decision on page-audit K5: a spec takes its signature talent as early as the tree allows): a hand draft or
            # an optimizer export whose order takes one later (the Fire draft took Pyroblast at 39, a Shadow export Mind Flay at 50) gets
            # the same order with those talents moved forward (fl_signature.sig_order; no race: the page numbers are measured again by
            # the race and report steps). Builds an open record or raid_path_leveling.py wrote carry that tool's order: redo it there.
            if b.get("order") and SM.mode_of(b) == "leveling" and not b.get("raid_path"):
                spec_b = SM.spec_of(cls, b)
                rot_b = SM.own_leveling_rotation(cls, spec_b, b["allocation"])
                rl = FS.order_rule(cls, rot_b, b, spec_b) if rot_b else None
                late = FS.SG.late_talents(cls, rl, {"allocation": FS.flat_of(b), "order": b["order"]}) if rl else []
                if late and b.get("derived") == "leveling" and b["id"].endswith("-open-leveling"):
                    print(f"== {cls} {b['id']}: " + "; ".join(f"{s} at {g} (its tree allows {e})" for s, g, e in late)
                          + ": an open record's build, redo the record's order (fl_open_search.py from the race on), then open_builds.py", flush=True)
                elif late:
                    new = FS.sig_order(cls, rot_b, b, spec_b)
                    if new != b["order"]:
                        what = "; ".join(f"{s} at {e} (was {g})" for s, g, e in late)
                        print(f"== {cls} {b['id']}: signature talents as early as the tree allows: {what}", flush=True)
                        b["order"] = new
                        b.setdefault("notes", []).append(
                            f"{TODAY} (order_repair.py, page audit K5, user decision: a spec takes its signature talent as early as its tree "
                            f"allows): {what}; the tree's points above it come forward in the order they had, every other point keeps its "
                            "place in line. Not raced here.")
                        changed = True
            solo = b.get("content") == "solo" and any("order dropped" in n for n in b.get("notes") or [])
            if not (b.get("content") == "leveling" or solo) or b.get("order") or b.get("raid_path"):
                continue
            tree = SM.spec_of(cls, b)
            if tree.startswith("Hybrid "):   # a hybrid levels with its lead tree's rotation (SM.own_leveling_rotation); 2026-10-17 KeyError
                pts = {t: sum(k for _, k in items) for t, items in b["allocation"].items()}
                tree = max(tree[len("Hybrid "):].split("/"), key=lambda t: pts.get(t, 0))
            spec, model, profile = models(cls, b, tree)
            flat = {n: r for items in b["allocation"].values() for n, r in items if r}
            opt = Optimizer("forever", cls, model, "leveling-st" if solo else profile)
            steps = opt.order(flat, lookahead=DL.SB.LOOKAHEAD.get(cls, 16))
            scorer = [{"levels": lv, "tree": t, "talent": n, "points": p} for lv, t, n, p in opt.compress_order(steps)]
            spec_o = SM.spec_of(cls, b)   # 2026-11-06 (page-audit K5): every order made here takes the signature talents as early as
            rot_o = SM.own_leveling_rotation(cls, spec_o, b["allocation"]) or spec   # their tree allows (fl_signature.sig_order)
            scorer = FS.sig_order(cls, rot_o, {"allocation": b["allocation"], "order": scorer}, spec_o)
            split = "/".join(str(sum(r for _, r in v)) for v in b["allocation"].values())
            if solo:
                print(f"== {cls} {b['id']} ({split}): a solo build on a leveling slot, the stats model's leveling-st order ({model}) without a race", flush=True)
                b["order"], b["order_label"] = scorer, "stats model"
                b.setdefault("notes", []).append(f"{TODAY} (order_repair.py, page audit K2): the order a repair dropped is the stats model's "
                                                 f"leveling order ({model}, leveling-st), the order the open leveling search races an "
                                                 "order-less build with; not raced here.")
                changed = True
                continue
            if profile != "leveling-st":
                print(f"== {cls} {b['id']} ({split}): {profile}, the stats model's order without a race", flush=True)
                b["order"], b["order_label"] = scorer, "stats model"
                b.setdefault("notes", []).append(f"{TODAY} (order_repair.py, page audit C1): the order lost in the 2026-10-03 repair is the "
                                                 f"stats model's {profile} order (not raced: the race plays single mobs).")
                changed = True
                continue
            pts = RP.expand(scorer)
            orders = {"stats model": scorer,
                      "own tree first": RP.compress([p for p in pts if p[0] == tree] + [p for p in pts if p[0] != tree]),
                      "own tree last": RP.compress([p for p in pts if p[0] != tree] + [p for p in pts if p[0] == tree])}
            orders = {k: FS.sig_order(cls, rot_o, {"allocation": b["allocation"], "order": o}, spec_o) for k, o in orders.items()}
            res = {}
            for name, order in orders.items():
                ob = {"allocation": b["allocation"], "order": order}
                times = pool.map(RP._run, [(cls, spec, FR.allocation_at(ob, L), L, a.fights) for L in RP.LEVELS])
                res[name] = dict(zip(RP.LEVELS, times))
            full = pool.map(RP._run, [(cls, spec, flat, L, a.fights) for L in RP.LEVELS])
            best = min(res, key=lambda k: RP.weighted(res[k]))
            print(f"== {cls} {b['id']} ({split}, {spec}): " + ", ".join(f"{k} {RP.weighted(v):.2f}s" for k, v in res.items())
                  + f" -> {best}; without an order (51 points from level 10) {RP.weighted(dict(zip(RP.LEVELS, full))):.2f}s", flush=True)
            b["order"], b["order_label"] = orders[best], best
            others = "; ".join(f"{k} {RP.weighted(v):.1f} s" for k, v in res.items() if k != best)
            b.setdefault("notes", []).append(
                f"{TODAY} (order_repair.py, page audit C1): the order lost in the 2026-10-03 repair is the fastest of three the fight lab "
                f"raced (the {spec} rotation, seed 3, {a.fights} fights per level, levels 20-60 weighted by level): {best} "
                f"{RP.weighted(res[best]):.1f} s per kill; {others}.")
            changed = True
        if changed and a.write:
            bp.write_text(dumps(data) + "\n", encoding="utf-8")
            print(f"wrote {bp}", flush=True)


if __name__ == "__main__":
    main()
