"""Search talents directly in the community simulator: local search over an allocation, no scorer model needed.

    python _reference/data/raidsim/talent_opt.py mage --spec frostfire-raid --start <build id | candidate .json | "sim preset: X" | talent string>
           [--setting dummy|raid] [--rounds 25] [--write <candidate .json>]

For new builds and hybrids no scorer spec model covers yet (a Frostfire Bolt mage). Moves keep the 51 points and every rule of the
validator (tier gating, prerequisites, rank caps; validate_builds.check_state): move 1, 2, 3 or 5 points from one talent to another, in
any tree. Every candidate plays the spec's rotation for the setting (run.py apl_path: our tuned one when it exists) in the ElliotWood/
Forever simulator with common random numbers (seed 1, --iterations); the best few are confirmed on seed 2 (--confirm), and a move is
kept only when it wins there by more than --min-gain. The loop stops when no move wins. The result is written as a candidate file
({"id", "allocation", "note", "search"}) that a proposed build can take over; run raidsim/apl_opt.py on the new build afterwards (the
rotation and the talents are tuned in turns).

A talent the rotation conditions on (run.py apl_talents: its spell, or a proc aura named after it) is never taken to 0 ranks: without it
the condition reads an unknown aura and the rotation changes shape (2026-09-28: the Arcane search dropped the 1-point Arcane Blast
talent, after which the tuned rotation's 'Frostbolt at 1.5 Arcane Blast stacks' line fired on every cast and the simulator's own
rotation cast nothing). A build without such a talent is another family with its own rotation: give it its own specs.json entry.
--allow-drop lifts the rule; --keep names further talents that must stay.
"""
import argparse
import copy
import datetime
import importlib.util
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[2]
sys.path.insert(0, str(ROOT / "_reference/data"))
import paths  # noqa: E402
import validate_builds as VB  # noqa: E402


def _load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


R = _load("raidrun", HERE / "run.py")
A = _load("aplopt", HERE / "apl_opt.py")
KS = (1, 2, 3, 5)


def by_tree(trees, flat):
    """{talent: rank} -> {tree: {talent: rank}} (the validator's state)."""
    out = {t: {} for t in trees}
    for name, r in flat.items():
        for t, tree in trees.items():
            if name in tree["talents"]:
                out[t][name] = r
                break
    return out


def valid(trees, flat):
    if sum(flat.values()) != VB.TOTAL_POINTS:
        return False
    for tname, need in MIN_TREE.items():   # --min-tree: keep the build a spec of that tree (2026-09-29, the spec pages)
        if sum(flat.get(n, 0) for n in trees[tname]["talents"]) < need:
            return False
    errors = []
    VB.check_state(trees, by_tree(trees, flat), "candidate", errors)
    return not errors


MIN_TREE = {}   # tree name -> minimum points (--min-tree "Beast Mastery=30")


def neighbors(trees, flat, protect=()):
    """[(description, allocation)] one valid move away; talents in `protect` keep at least one rank."""
    names = [n for t in trees.values() for n in t["talents"]]
    cap = {n: t["talents"][n]["max"] for t in trees.values() for n in t["talents"]}
    out, seen = [], set()
    for a, ra in flat.items():
        if ra <= 0:
            continue
        for b in names:
            if b == a:
                continue
            free = cap[b] - flat.get(b, 0)
            for k in KS:
                if k > ra or k > free:
                    continue
                new = dict(flat)
                new[a] = ra - k
                if new[a] == 0:
                    if a in protect:
                        continue
                    del new[a]
                new[b] = new.get(b, 0) + k
                key = tuple(sorted(new.items()))
                if key in seen or not valid(trees, new):
                    continue
                seen.add(key)
                out.append((f"{k} point{'s' if k > 1 else ''} {a} -> {b}", new))
    return out


def start_alloc(cls, entry, repo, start):
    """An allocation from a build id, a candidate file, a simulator preset label or a raw talent string."""
    if start.endswith(".json"):
        return R.alloc_of(json.load(open(start, encoding="utf-8")))
    data = {b["id"]: b for b in json.load(open(ROOT / cls / "research/talents/forever/proposed-builds.json", encoding="utf-8"))["builds"]}
    if start in data:
        return R.alloc_of(data[start])
    sim_trees = R.load_trees(repo, cls)
    if start.startswith("sim preset: "):
        pr = {p["label"]: p["talents"] for p in R.sim_presets(repo, dict(entry, **{"preset_names": [start[len("sim preset: "):]]}))}
        start = pr[start]
    return {n: r for items in R.preset_allocation(sim_trees, start).values() for n, r in items}


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("cls")
    ap.add_argument("--spec", required=True)
    ap.add_argument("--start", required=True)
    ap.add_argument("--setting", choices=["dummy", "raid"])
    ap.add_argument("--rounds", type=int, default=25)
    ap.add_argument("--iterations", type=int, default=3000)
    ap.add_argument("--confirm", type=int, default=20000)
    ap.add_argument("--top", type=int, default=6)
    ap.add_argument("--screen-gain", type=float, default=0.001)
    ap.add_argument("--min-gain", type=float, default=0.0015)
    ap.add_argument("--repo")
    ap.add_argument("--write", help="candidate file to write the result to")
    ap.add_argument("--keep", default="", help="comma-separated talents that must keep at least one rank")
    ap.add_argument("--min-tree", default="", help='keep at least N points in a tree, e.g. "Beast Mastery=30" (a spec build of that tree)')
    ap.add_argument("--allow-drop", action="store_true", help="let moves remove talents the rotation conditions on")
    a = ap.parse_args()
    for part in filter(None, (x.strip() for x in a.min_tree.split(","))):
        tname, need = part.rsplit("=", 1)
        MIN_TREE[tname.strip()] = int(need)
    R.set_game("forever")
    repo = R.repo_path(argparse.Namespace(repo=a.repo))
    entry = R.SPECS[a.cls][a.spec]
    where = a.setting or R.setting(entry)
    trees = VB.load_forever()[a.cls]
    sim_trees = R.load_trees(repo, a.cls)
    tank = bool(entry.get("tank"))
    cur = start_alloc(a.cls, entry, repo, a.start)
    if not valid(trees, cur):
        errors = []
        VB.check_state(trees, by_tree(trees, cur), "start", errors)
        raise SystemExit(f"the start allocation is not valid: {errors[:5]} ({sum(cur.values())} points)")
    tag = f"talent-{a.cls}-{a.spec}"
    names = {(t.get("fancyName") or t.get("fieldName")): (R.talent_key(t) or t.get("fieldName")) for tr in sim_trees for t in tr["talents"]}
    protect = set() if a.allow_drop else {names.get(n, n) for n in R.apl_talents(repo, entry, sim_trees, where)} & set(cur)
    protect |= {n.strip() for n in a.keep.split(",") if n.strip()}

    def run(allocs, iterations, seed):
        bl = [{"label": str(i), "talents": R.talents_string(sim_trees, al)} for i, al in enumerate(allocs)]
        rows = A.bench(entry, repo, bl, iterations, seed, where, tag)
        return [rows.get(str(i)) for i in range(len(allocs))]

    def value(row, ref):
        return A.value(row, ref, tank)

    split = lambda al: "/".join(str(sum(r for n, r in al.items() if n in t["talents"])) for t in trees.values())   # noqa: E731
    base = run([cur], a.iterations, 1)[0]
    start_dps = base.get("dps")
    print(f"== {a.cls} {a.spec} ({where}): start {split(cur)}, {start_dps:.1f} DPS" + (f"; kept: {', '.join(sorted(protect))}" if protect else ""), flush=True)
    log = []
    for rnd in range(1, a.rounds + 1):
        cands = neighbors(trees, cur, protect)
        rows = run([al for _, al in cands], a.iterations, 1)
        scored = sorted(((value(r, base) or 0.0, i) for i, r in enumerate(rows) if r and not r.get("error")), key=lambda x: -x[0])
        top = [(sc, i) for sc, i in scored if sc > 1 + a.screen_gain][: a.top]
        if not top:
            print(f"  round {rnd}: {len(cands)} moves, none ahead on seed 1 (best {scored[0][0] - 1:+.2%}: {cands[scored[0][1]][0]})" if scored else "  no moves", flush=True)
            break
        conf = run([cur] + [cands[i][1] for _, i in top], a.confirm, 2)
        best = max(((value(conf[k], conf[0]) or 0.0, sc1, i) for k, (sc1, i) in enumerate(top, start=1)), key=lambda x: x[0])
        if best[0] <= 1 + a.min_gain:
            print(f"  round {rnd}: {len(cands)} moves, {len(top)} ahead on seed 1, none confirmed on seed 2 (best {best[0] - 1:+.2%})", flush=True)
            break
        sc2, sc1, i = best
        d, cur = cands[i]
        log.append({"round": rnd, "move": d, "gain_seed1": sc1 - 1, "gain_seed2": sc2 - 1, "split": split(cur)})
        print(f"  round {rnd}: {d}  ({sc1 - 1:+.2%} seed 1, {sc2 - 1:+.2%} seed 2; {len(cands)} moves) -> {split(cur)}", flush=True)
        base = rows[i]
    fin = run([start_alloc(a.cls, entry, repo, a.start), cur], a.confirm, 3)
    print(f"  final (seed 3, {a.confirm} iterations): {fin[0]['dps']:.1f} -> {fin[1]['dps']:.1f} DPS ({fin[1]['dps'] / fin[0]['dps'] - 1:+.2%}), {split(cur)}", flush=True)
    if a.write:
        out = pathlib.Path(a.write)
        out.parent.mkdir(parents=True, exist_ok=True)
        alloc = {t: [[n, r] for n, r in by_tree(trees, cur)[t].items()] for t in trees}
        out.write_text(json.dumps({"id": out.stem, "allocation": alloc, "note": f"Simulator talent search (raidsim/talent_opt.py, {datetime.date.today().isoformat()}) "
                                   f"for {a.spec} from {a.start} in the {where} setting: {fin[0]['dps']:.1f} -> {fin[1]['dps']:.1f} DPS on a third seed.",
                                   "search": {"start": a.start, "setting": where, "kept": sorted(protect), "moves": log, "dps_start": fin[0]["dps"], "dps_end": fin[1]["dps"],
                                              "gain": (value(fin[1], fin[0]) or 1.0) - 1, "tank": tank}},
                                  indent=1, ensure_ascii=False), encoding="utf-8")
        print(f"  wrote {out}", flush=True)


if __name__ == "__main__":
    main()
