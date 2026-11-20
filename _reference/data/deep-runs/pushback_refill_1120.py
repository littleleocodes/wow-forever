"""The pushback points back (2026-11-20). utility_tags.py's interrupt pattern read "lose .* casting time", which needs a word between
"lose" and "casting time": Forever's wording "to not lose casting time when you take damage" (Improved Channeling, Ice Barrier, Burning
Soul, Spiritual Focus, Twilight Focus, Eye of the Storm, Healing Focus, Fel Concentration, Intensity) read as no tag, so the raid filler
audit (raidsim/filler_audit.py) took their points for free and moved them to survival or range talents, against its own order (pushback
protection first: the user's question of 2026-09-29 was about Improved Channeling). The pattern is fixed; this undoes the utility moves
out of those talents in the six builds whose records hold them, where the build still has the record's final allocation, the result is
legal and it costs nothing (both builds raced in the entry's setting and a full raid, 6,000 fights, seeds 1 and 2: no loss over 0.1%).

    python _reference/data/deep-runs/pushback_refill_1120.py [--apply]
"""
import argparse
import datetime
import json
import pathlib
import sys

DATA = pathlib.Path(__file__).resolve().parents[1]
ROOT = DATA.parents[1]
sys.path[:0] = [str(DATA / "raidsim"), str(DATA)]
import filler_audit as FA  # noqa: E402
import talent_opt as T  # noqa: E402
import paths  # noqa: E402
import validate_builds as VB  # noqa: E402
from filelock import locked  # noqa: E402
from fmt_json import dumps  # noqa: E402

PUSHBACK = {"Improved Channeling", "Burning Soul", "Ice Barrier", "Spiritual Focus", "Twilight Focus", "Eye of the Storm", "Healing Focus",
            "Fel Concentration", "Intensity"}
R, A = FA.R, FA.A
LOSS = 0.001


def flat(al):
    return {n: r for items in (al or {}).values() for n, r in items if r}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--apply-saved", action="store_true", help="apply raidsim/pushback-refill.json as measured, without racing again")
    a = ap.parse_args()
    if a.apply_saved:
        saved = json.load(open(DATA / "raidsim" / "pushback-refill.json", encoding="utf-8"))
        apply_report(saved["builds"], saved["date"])
        return
    R.set_game("forever")
    repo = R.repo_path(argparse.Namespace(repo=None))
    forever = VB.load_forever()
    found = []
    for f in sorted(ROOT.glob("*/research/raid/raidsim/*-fillers-*.json")):
        x = json.load(open(f, encoding="utf-8"))
        back = [m for m in x.get("moves", []) if m.get("from") in PUSHBACK and m.get("to") not in PUSHBACK and m.get("kind") == "utility"]
        if back:
            found.append((f, x, back))
    report = []
    for f, x, back in found:
        cls, spec, bid = x["class"], x["spec"], x["build"]
        data = {b["id"]: b for b in json.load(open(paths.builds_json("forever", cls), encoding="utf-8"))["builds"]}
        b = data.get(bid)
        if not b or flat(b["allocation"]) != flat(x["allocation"]):
            print(f"{cls} {bid}: the build changed since {f.name} or is gone: left", flush=True)
            continue
        new = dict(flat(b["allocation"]))
        undone = True
        for m in back:
            if new.get(m["to"], 0) < 1:
                undone = False
                break
            new[m["to"]] -= 1
            if not new[m["to"]]:
                del new[m["to"]]
            new[m["from"]] = new.get(m["from"], 0) + 1
        trees = forever[cls]
        if not undone or not T.valid(trees, new):
            print(f"{cls} {bid}: the undone moves give no legal build: left", flush=True)
            continue
        entry = R.SPECS[cls][spec]
        sim_trees = R.load_trees(repo, cls)
        res = {}
        for where in sorted({R.setting(entry), "raid"}):
            for seed in (1, 2):
                rows = A.bench(entry, repo, [{"label": "now", "talents": R.talents_string(sim_trees, flat(b["allocation"]))},
                                             {"label": "back", "talents": R.talents_string(sim_trees, new)}], 6000, seed, where, f"pushback-{spec}")
                res[(where, seed)] = (rows["now"]["dps"], rows["back"]["dps"])
        worst = min(v[1] / v[0] - 1 for v in res.values())
        line = (f"{cls} {bid}: {'; '.join(m['to'] + ' -> ' + m['from'] for m in back)}; "
                + ", ".join(f"{w} s{s} {v[0]:.1f} -> {v[1]:.1f}" for (w, s), v in res.items()) + f"; worst {worst:+.2%}")
        print(line, flush=True)
        report.append({"class": cls, "entry": spec, "build": bid, "record": f.name, "moves_undone": [[m["to"], m["from"]] for m in back],
                       "dps": {f"{w} seed {s}": list(v) for (w, s), v in res.items()}, "worst": worst, "ok": worst >= -LOSS,
                       "allocation": {t: [[n, r] for n, r in T.by_tree(trees, new)[t].items()] for t in trees}})
    out = DATA / "raidsim" / "pushback-refill.json"
    out.write_text(json.dumps({"date": datetime.date.today().isoformat(), "builds": report}, indent=1) + "\n", encoding="utf-8")
    if a.apply:
        apply_report(report, datetime.date.today().isoformat())


def apply_report(report, date):
    """Each measured build whose file entry is still the allocation the undo started from gets the undone allocation and a note."""
    for r in report:
        if not r["ok"]:
            print(f"not applied {r['class']} {r['build']} (worst {r['worst']:+.2%})")
            continue
        old = flat(r["allocation"])
        for to, frm in r["moves_undone"]:   # the allocation before the undo: each pushback point back where the audit had put it
            old[frm] -= 1
            if not old[frm]:
                del old[frm]
            old[to] = old.get(to, 0) + 1
        bp = paths.builds_json("forever", r["class"])
        with locked(bp.with_suffix(".lock")):
            data = json.load(open(bp, encoding="utf-8"))
            b = next(y for y in data["builds"] if y["id"] == r["build"])
            if flat(b["allocation"]) == flat(r["allocation"]):
                print(f"already applied {r['class']} {r['build']}")
                continue
            if flat(b["allocation"]) != old:
                print(f"skipped {r['class']} {r['build']}: the build changed since the measurement")
                continue
            b["allocation"] = r["allocation"]
            n = len(r["moves_undone"])
            src = sorted({m[1] for m in r["moves_undone"]})
            b.setdefault("notes", []).append(
                f"{date}: {n} point{'s' if n != 1 else ''} back in {', '.join(src)} (pushback protection): the filler audit of "
                f"{r['record']} had taken {'them' if n != 1 else 'it'} for free because its tags missed Forever's wording (\"to not lose "
                "casting time\"; utility_tags.py fixed the same day). The same damage within 0.1% "
                f"(worst {r['worst']:+.2%} over the entry's setting and a full raid, seeds 1 and 2).")
            bp.write_text(dumps(data) + "\n", encoding="utf-8")
        print(f"applied {r['class']} {r['build']}")


if __name__ == "__main__":
    main()
