"""Fight-variety check of the raid picks (2026-10-08, the improvement log's "fight variety"; user: "Do all of them").

    python -u _reference/data/raidsim/fight_variety.py [classes] [--fights 8000] [--top 4] [--write]

Every raid number on the pages is one fight: a single Elemental boss, 180 s, a full raid. A pick that wins only there can lose where
fights differ. For every raid damage spec of the pages, the pick and the next builds of the spec (up to --top, each in its own entry's
rotation and gear) are raced in the full raid under five fights: the standard one, three targets (cleave and area damage), an Undead
target (Exorcism, Holy Wrath and the anti-undead items), 90 s (cooldowns weigh more) and 300 s (mana and sustained damage weigh more).
A pick more than 2% behind another build of its spec in any fight is flagged. Record raidsim/fight-variety.json, page
_reference/fight-variety.md (generated). The several-target fights need the bench's `numTargets` (foreverbench main.go, 2026-10-08);
until the main bench is rebuilt the check uses foreverbench-variety.exe when it exists. Simulations of the community's model of the
beta, not in-game measurements.
"""
import argparse
import datetime
import json
import os
import pathlib
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[2]
sys.path[:0] = [str(HERE), str(ROOT / "_reference/data"), str(ROOT / "_reference/data/scorer")]
import run as R  # noqa: E402
import apl_opt as AO  # noqa: E402

OUT = HERE / "fight-variety.json"
PAGE = ROOT / "_reference" / "fight-variety.md"
TODAY = datetime.date.today().isoformat()
FIGHTS = [("standard", {}), ("three targets", {"numTargets": 3}), ("Undead target", {"mobType": "Undead"}),
          ("90 s", {"duration": 90}), ("300 s", {"duration": 300})]
FLAG = 0.02


def use_variety_bench(repo):
    """Run the bench calls through foreverbench-variety.exe when the main bench predates numTargets."""
    alt = repo / "foreverbench-variety.exe"
    if not alt.exists():
        return
    real = subprocess.run

    def _run(args, **kw):
        if args and str(args[0]).endswith(("foreverbench.exe", "foreverbench")):
            args = [str(alt)] + list(args[1:])
        return real(args, **kw)
    AO.subprocess.run = _run


SPEC_ROWS = r"""
import json, sys
sys.path[:0] = [sys.argv[1] + "/_reference/data", sys.argv[1] + "/_reference/data/scorer"]
import render_modes as RM, render_rotations as rr, spec_modes as SM
out = {}
for cls in sys.argv[3].split(","):
    B = rr.builds(cls)
    g = SM.grid(cls, list(B.values()))
    nums = (RM.raid_numbers(cls), RM.leveling_numbers(cls), RM.healer_numbers(cls))
    for spec, modes in g.items():
        ranked = [b for b in RM.rank_builds(cls, "raid", modes.get("raid") or [], nums)
                  if b.get("role", "dps") == "dps" and (nums[0].get(b["id"]) or {}).get("raid") and not (nums[0].get(b["id"]) or {}).get("tank")]
        if len(ranked) >= 2:
            out.setdefault(cls, {})[spec] = [[b["id"], nums[0][b["id"]]["entry"]] for b in ranked[: int(sys.argv[2])]]
print(json.dumps(out))
"""


def spec_rows_all(classes, top):
    """{class: {spec: [[build id, entry]]}}: the page's raid pick first, then the next builds of the spec with a full-raid number. Read in a
    separate process: the page renderer imports the fight lab's run.py as `run`, the race tool here is raidsim's run.py under the same name."""
    r = subprocess.run([sys.executable, "-c", SPEC_ROWS, str(ROOT), str(top), ",".join(classes)], capture_output=True, text=True,
                       encoding="utf-8", errors="replace", cwd=str(ROOT))
    if r.returncode:
        raise SystemExit(f"reading the pages' raid builds failed: {r.stderr[-1500:]}")
    return json.loads(r.stdout.strip().splitlines()[-1])


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("classes", nargs="*")
    ap.add_argument("--fights", type=int, default=8000)
    ap.add_argument("--top", type=int, default=4)
    ap.add_argument("--write", action="store_true")
    a = ap.parse_args()
    R.set_game("forever")
    repo = R.repo_path(argparse.Namespace(repo=None))
    use_variety_bench(repo)
    import spec_modes as SM
    classes = a.classes or [c for c in SM.CLASSES]
    rec = json.load(open(OUT, encoding="utf-8")) if OUT.exists() and a.classes else {}
    rows_all = spec_rows_all(classes, a.top)
    for cls in classes:
        trees = R.load_trees(repo, cls)
        data = {b["id"]: b for b in json.load(open(ROOT / cls / "research/talents/forever/proposed-builds.json", encoding="utf-8"))["builds"]}
        for spec, rows in (rows_all.get(cls) or {}).items():
            res = {}
            for fname, extra in FIGHTS:
                per = {}
                for bid, entry in rows:
                    E = R.SPECS[cls][entry]
                    b = {"label": bid, "talents": R.talents_string(trees, R.alloc_of(data[bid]))}
                    r = AO.bench(E, repo, [b], a.fights, 1, "raid", f"variety-{cls}", extra=dict(extra))
                    per[bid] = round((r.get(bid) or {}).get("dps") or 0.0, 1)
                res[fname] = per
            pick = rows[0][0]
            flags = []
            for fname, per in res.items():
                best = max(per, key=per.get)
                if best != pick and per[pick] < per[best] * (1 - FLAG):
                    flags.append({"fight": fname, "best": best, "gap": round(per[pick] / per[best] - 1, 4)})
            rec.setdefault(cls, {})[spec] = {"date": TODAY, "builds": [r[0] for r in rows], "entries": [r[1] for r in rows], "dps": res,
                                             "flags": flags}
            print(f"{cls} {spec}: pick {pick}" + ("; " + "; ".join(f"{f['fight']}: {f['best']} {-f['gap']:.1%} ahead" for f in flags)
                                                  if flags else ": best or within 2% in every fight"), flush=True)
            if a.write:
                OUT.write_text(json.dumps(rec, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    if a.write:
        write_page(rec)


def write_page(rec):
    import spec_modes as SM
    o = ["# Fight variety of the raid picks (generated)", "",
         f"> Generated by `_reference/data/raidsim/fight_variety.py` on {TODAY}. Do not hand-edit.", "",
         "Every raid number on the pages is one fight: a single Elemental boss, 180 s, a full raid. Here each damage spec's pick and its next "
         "builds race in five fights (full raid each): the standard one, three targets, an Undead target, 90 s and 300 s. A pick more than "
         "2% behind another build of its spec in some fight is flagged. Simulations of the community's model of the beta, not in-game "
         "measurements.", ""]
    for cls in sorted(rec):
        o += [f"## {cls.capitalize()}", "", "| Spec | Pick | " + " | ".join(f for f, _ in FIGHTS) + " | Flags |",
              "|---|---|" + "---|" * len(FIGHTS) + "---|"]
        for spec, r in rec[cls].items():
            pick = r["builds"][0]
            cells = []
            for fname, _ in FIGHTS:
                per = r["dps"].get(fname) or {}
                best = max(per, key=per.get) if per else None
                cells.append(f"{per.get(pick, 0):.0f}" + ("" if best in (None, pick) else f" ({best} {per[best]:.0f})"))
            fl = "; ".join(f"{f['fight']}: {f['best']} {-f['gap']:.1%} ahead" for f in r["flags"]) or "none"
            o.append(f"| {SM.spec_name(cls, spec)} | `{pick}` | " + " | ".join(cells) + f" | {fl} |")
        o.append("")
    PAGE.write_text("\n".join(o) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
