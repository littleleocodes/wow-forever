"""Zero-value talent points in our raid builds, moved to talents that help in the real game (2026-09-29, user question: "why Wand
Specialization as a filler when Improved Channeling protects Arcane Missiles from damage?").

    python _reference/data/raidsim/filler_audit.py <class> --spec <entry> --build <id> [--iterations 3000] [--confirm 12000] [--write]
    python _reference/data/raidsim/filler_audit.py --all [--jobs 3] [--apply]

1. Every talent of the build is removed once in the simulator (the entry's rotation and setting, 180 s): a talent whose removal moves
   DPS (tanks: tank value) by less than ZERO is a free point here. Talents the rotation conditions on (run.apl_talents) never count
   as free: their removal run measures a broken rotation, not the talent.
2. Local search, one point at a time: move a point out of a free talent into any other talent (legal: validate_builds.check_state).
   A move is taken when it gains DPS (above GAIN on seed 1 and confirmed on an independent seed 2), or else when it costs nothing
   (no worse than -LOSS on both seeds) and the new talent is more useful in a real raid than the old one by UTILITY, a tag read
   from the beta tooltip: interrupt/pushback protection first, then threat reduction, mana cost, range, survival (tanks: survival
   first). A talent with none of these tags ranks last, so a point never moves into another dead talent.
3. It stops when no move is taken. --write saves the record under research/raid/raidsim/<entry>-fillers-<build>.json; --apply puts
   the final allocation into proposed-builds.json with a note naming every move.

The simulator models no pushback, range, threat limits or incoming damage for DPS builds: those talents measure 0 here, so the
utility order is our judgment, not a measurement. What the simulator does measure (DPS, mana) decides first.
"""
import argparse
import datetime
import json
import pathlib
import re
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[2]
sys.path.insert(0, str(ROOT / "_reference/data"))
sys.path.insert(0, str(HERE))
import paths  # noqa: E402
import talent_opt as T  # noqa: E402  (valid, by_tree, the run/apl_opt loaders)
import validate_builds as VB  # noqa: E402
from fmt_json import dumps  # noqa: E402

R, A = T.R, T.A
ZERO = 0.002    # |removal effect| under 0.2%: a free point
GAIN = 0.0015   # a real DPS gain
LOSS = 0.001    # a utility move may cost at most 0.1%
from utility_tags import TAGS, NONE, usefulness  # noqa: E402  (shared with the scorer's raid tie-break)


def utility(cls, tank=False):
    return usefulness(cls, tank)


def audit(cls, spec, bid, iterations, confirm):
    R.set_game("forever")
    repo = R.repo_path(argparse.Namespace(repo=None))
    entry = R.SPECS[cls][spec]
    where = R.setting(entry)
    tank = bool(entry.get("tank"))
    trees = VB.load_forever()[cls]
    sim_trees = R.load_trees(repo, cls)
    data = {b["id"]: b for b in json.load(open(paths.builds_json("forever", cls), encoding="utf-8"))["builds"]}
    cur = R.alloc_of(data[bid])
    names = {(t.get("fancyName") or t.get("fieldName")): (R.talent_key(t) or t.get("fieldName")) for tr in sim_trees for t in tr["talents"]}
    protect = {names.get(n, n) for n in R.apl_talents(repo, entry, sim_trees, where)} & set(cur)
    protect |= set(entry.get("not_measured", {})) & set(cur)   # values the standard target cannot show (Murder: Humanoids and Giants)
    # a talent that grants an ability is never free: if it measures 0, the rotation does not cast it (a rotation question, flagged)
    book = {sp["name"] for t in json.load(open(ROOT / "_reference/data/forever-spells" / f"{cls}.json", encoding="utf-8"))["tabs"] for sp in t["spells"]}
    active = set(cur) & book
    use = utility(cls, tank)
    tag = f"fillers-{cls}-{spec}"

    def run(allocs, its, seed):
        bl = [{"label": str(i), "talents": R.talents_string(sim_trees, al)} for i, al in enumerate(allocs)]
        rows = A.bench(entry, repo, bl, its, seed, where, tag)
        return [rows.get(str(i)) for i in range(len(allocs))]

    def val(row, ref):
        return (A.value(row, ref, tank) or 0.0) - 1.0

    # 1. removal effects
    held = sorted(cur)
    rows = run([cur] + [{k: v for k, v in cur.items() if k != n} for n in held], iterations, 1)
    base = rows[0]
    effect = {n: -val(r, base) for n, r in zip(held, rows[1:])}   # DPS lost when the talent goes
    free = {n for n, e in effect.items() if abs(e) < ZERO and n not in protect and n not in active}
    flags = sorted(n for n, e in effect.items() if abs(e) < ZERO and n in active)
    print(f"== {cls} {spec} {bid} ({where}): {base['dps']:.1f} DPS; free: " + (", ".join(f"{n} {cur[n]}" for n in sorted(free)) or "none"), flush=True)
    start = dict(cur)
    moves = []
    for rnd in range(1, 40):
        cands = []
        for a in sorted(free & set(cur)):
            for b in use:
                if b == a:
                    continue
                new = dict(cur)
                new[a] -= 1
                if not new[a]:
                    del new[a]
                new[b] = new.get(b, 0) + 1
                if T.valid(trees, new):
                    cands.append((a, b, new))
        if not cands:
            break
        rows = run([cur] + [c[2] for c in cands], iterations, 1)
        ref = rows[0]
        scored = [(val(r, ref), a, b, new) for r, (a, b, new) in zip(rows[1:], cands) if r and not r.get("error")]
        gains = sorted([s for s in scored if s[0] > GAIN], key=lambda s: -s[0])[:5]
        # utility moves: no loss, into a strictly more useful talent (a lower rank of usefulness than the point's old talent)
        utils = sorted([s for s in scored if s[0] >= -LOSS and use.get(s[2], NONE) < use.get(s[1], NONE)],
                       key=lambda s: (use.get(s[2], NONE), -s[0]))[:5]
        took = None
        for kind, pool in (("gain", gains), ("utility", utils)):
            if not pool:
                continue
            conf = run([cur] + [s[3] for s in pool], confirm, 2)
            for s, r in zip(pool, conf[1:]):
                v2 = val(r, conf[0])
                if (kind == "gain" and v2 > GAIN) or (kind == "utility" and v2 >= -LOSS):
                    took = (kind, s, v2)
                    break
            if took:
                break
        if not took:
            break
        kind, (v1, a, b, new), v2 = took
        cur = new
        moves.append({"round": rnd, "kind": kind, "from": a, "to": b, "seed1": v1, "seed2": v2, "utility": [t for t, _ in TAGS][use[b]] if use[b] < NONE else None})
        if b not in free and kind == "utility":
            pass
        print(f"  {rnd}: 1 point {a} -> {b} ({kind}; {v1:+.2%} seed 1, {v2:+.2%} seed 2)", flush=True)
    fin = run([start, cur], confirm, 3)
    total = val(fin[1], fin[0])
    print(f"  final (seed 3): {total:+.2%}", flush=True)
    return {"class": cls, "spec": spec, "build": bid, "setting": where, "date": datetime.date.today().isoformat(), "tank": tank,
            "removal": effect, "free": sorted(free), "kept_for_rotation": sorted(protect), "active_never_worth": flags, "moves": moves, "final_seed3": total,
            "start": {t: [[n, r] for n, r in T.by_tree(trees, start)[t].items()] for t in trees},
            "allocation": {t: [[n, r] for n, r in T.by_tree(trees, cur)[t].items()] for t in trees}}


def targets():
    """(class, entry, build) for every hand raid DPS or tank build of ours, in the entry that races it."""
    R.set_game("forever")
    out = []
    for cls, es in R.SPECS.items():
        if cls.startswith("_"):
            continue
        builds = {b["id"]: b for b in json.load(open(paths.builds_json("forever", cls), encoding="utf-8"))["builds"]}
        seen = set()
        for spec, e in es.items():
            if not isinstance(e, dict):
                continue
            for bid in e.get("builds", []):
                b = builds.get(bid)
                if b and not bid.startswith("opt-") and b.get("content") == "raid" and b.get("role") != "healer" and bid not in seen:
                    seen.add(bid)
                    out.append((cls, spec, bid))
    return out


def record_path(cls, spec, bid):
    return paths.raidsim_dir(cls) / f"{spec}-fillers-{bid}.json"


def apply(rec):
    """Put a record's allocation into proposed-builds.json with a note (only when it moved points)."""
    if not rec["moves"]:
        return False
    bp = paths.builds_json("forever", rec["class"])
    data = json.load(open(bp, encoding="utf-8"))
    b = next(x for x in data["builds"] if x["id"] == rec["build"])
    b["allocation"] = rec["allocation"]
    mv = "; ".join(f"{m['from']} -> {m['to']}" + (f" ({m['utility']})" if m["kind"] == "utility" and m["utility"] else f" ({m['seed2']:+.1%} DPS)") for m in rec["moves"])
    b.setdefault("notes", []).append(
        f"{rec['date']} filler audit (raidsim/filler_audit.py, user question on zero-value fillers): points the simulator measures at 0 moved, one at a "
        f"time, to talents that help in a real raid (interrupt protection, threat, mana, range, survival; the simulator cannot see these, so the order is "
        f"our judgment) or that gain DPS: {mv}. Net {rec['final_seed3']:+.2%} on a third seed.")
    for fx in b.get("flex", []):   # flex entries naming a talent that left the build now name its replacement
        gone = [m for m in rec["moves"] if m["from"] == fx.get("default") and not any(n == m["from"] for it in rec["allocation"].values() for n, _ in it)]
        if gone:
            fx["alternatives"] = sorted(set(fx.get("alternatives", [])) | {fx["default"]})
            fx["default"] = gone[-1]["to"]
    bp.write_text(dumps(data) + "\n", encoding="utf-8")
    return True


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("cls", nargs="?")
    ap.add_argument("--spec")
    ap.add_argument("--build")
    ap.add_argument("--all", action="store_true")
    ap.add_argument("--jobs", type=int, default=3)
    ap.add_argument("--iterations", type=int, default=3000)
    ap.add_argument("--confirm", type=int, default=12000)
    ap.add_argument("--write", action="store_true")
    ap.add_argument("--apply", action="store_true", help="with --all: apply the written records to proposed-builds.json")
    a = ap.parse_args()
    if a.all:
        todo = targets()
        if a.apply:
            for cls, spec, bid in todo:
                p = record_path(cls, spec, bid)
                if p.exists() and apply(json.load(open(p, encoding="utf-8"))):
                    print(f"applied {cls} {bid}")
            return
        procs = []
        for cls, spec, bid in todo:
            if record_path(cls, spec, bid).exists():
                continue
            while len([p for p in procs if p.poll() is None]) >= a.jobs:
                procs[0].wait() if procs[0].poll() is None else procs.pop(0)
                procs = [p for p in procs if p.poll() is None]
            procs.append(subprocess.Popen([sys.executable, __file__, cls, "--spec", spec, "--build", bid, "--iterations", str(a.iterations),
                                           "--confirm", str(a.confirm), "--write"]))
        for p in procs:
            p.wait()
        return
    rec = audit(a.cls, a.spec, a.build, a.iterations, a.confirm)
    if a.write:
        p = record_path(a.cls, a.spec, a.build)
        p.write_text(json.dumps(rec, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
        print(f"  wrote {p.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
