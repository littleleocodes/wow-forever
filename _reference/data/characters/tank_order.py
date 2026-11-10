"""A tank-first talent order to a level-60 tank build (2026-11-09, user, for Tara: "I want her to be a Protection Paladin. But I don't
think the build should follow the solo protection build. It needs to follow a protection build that works in a group or a build order
that leads into the level 60 protection build"; answers: a group with a healer, tank-first, raid tank at 60).

The leveling pages order a tank's raid build for solo kill speed (the fight lab), which put the Protection paladin's threat talent at 49.
This orders the same build for tanking: the spec's own tree first, then the rest, and within that, the next point always goes to the
legal talent with the most tank value per point. Tank value per talent: the raid simulator's removal measurement for that build (the
filler audit's record, `raid/raidsim/<entry>-fillers-<build>.json` "removal": the share of tank value, threat and damage taken, lost
without the talent); a talent that measured zero is taken only when a tier needs it.

    python _reference/data/characters/tank_order.py paladin protection-ml-tank prot-tank Protection
"""
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
DATA = HERE.parent
ROOT = DATA.parent.parent
sys.path.insert(0, str(DATA))
import validate_builds as VB  # noqa: E402


def build_of(cls, build_id):
    d = json.load(open(ROOT / cls / "research" / "talents" / "forever" / "proposed-builds.json", encoding="utf-8"))
    return next(b for b in (d["builds"] if isinstance(d, dict) else d) if b["id"] == build_id)


def removal(cls, entry, build_id):
    p = ROOT / cls / "research" / "raid" / "raidsim" / f"{entry}-fillers-{build_id}.json"
    return json.load(open(p, encoding="utf-8"))["removal"] if p.exists() else {}


def order(cls, build_id, entry, own_tree):
    """[{levels, tree, talent, points}] from level 10: own tree first, then the others; each point to the legal talent with the most
    tank value per point (ties: the lower tier first)."""
    trees = VB.load_forever()[cls]
    b = build_of(cls, build_id)
    target = {t: dict(items) for t, items in b["allocation"].items()}
    val = removal(cls, entry, build_id)
    have = {t: {} for t in target}
    points = []
    trees_order = [own_tree] + [t for t in target if t != own_tree]
    for _ in range(sum(sum(v.values()) for v in target.values())):
        best = None
        for tname in trees_order:
            for name, cap in target[tname].items():
                if have[tname].get(name, 0) >= cap:
                    continue
                trial = {k: dict(v) for k, v in have.items()}
                trial[tname][name] = trial[tname].get(name, 0) + 1
                errors = []
                VB.check_state(trees, {k: v for k, v in trial.items() if v}, "order", errors)
                if errors:
                    continue
                per = val.get(name, 0.0) / max(1, cap)
                row = trees[tname]["talents"][VB.find_talent(trees[tname], name)[0]]["row"]
                key = (per, -row)
                if best is None or key > best[0]:
                    best = (key, tname, name)
            if best:   # the own tree until it is done, then the next
                break
        if best is None:
            raise RuntimeError(f"no legal point after {len(points)}")
        _, tname, name = best
        have[tname][name] = have[tname].get(name, 0) + 1
        points.append((tname, name))
    out = []
    for i, (tree, name) in enumerate(points):
        lv = 10 + i
        if out and out[-1]["talent"] == name:
            out[-1]["points"] += 1
            out[-1]["levels"] = f"{out[-1]['levels'].split('-')[0]}-{lv}"
        else:
            out.append({"levels": str(lv), "tree": tree, "talent": name, "points": 1})
    return out


if __name__ == "__main__":
    cls, build_id, entry, tree = sys.argv[1:5]
    for x in order(cls, build_id, entry, tree):
        print(f"{x['levels']:>6}  {x['tree']:12} {x['talent']} ({x['points']})")
