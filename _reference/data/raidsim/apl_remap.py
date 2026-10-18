"""Remap the spell ids of our rotations (raidsim/apls/**) onto the spells the official simulator registers (2026-10-18, the port from
the deleted ElliotWood/Forever fork to wowsims/forever).

    python _reference/data/raidsim/apl_remap.py [classes] [--write]

The official simulator registers one rank of each spell (the trainer's highest, e.g. Frostbolt rank 10, 10181: the rank-11 book
25304 is not taught in Forever), where the fork registered every rank; a rotation line naming another rank finds no spell and never
casts (the first smoke run of the Frost mage cast Fire Blast only). For every class: the bench's `spells` mode lists the spell and
aura ids each of the class's entries registers (every build of the entry, player and pets); every ActionID in the class's rotation
files whose spell id is not registered is moved to the registered member of its rank chain (`spelldata.Ranked(...)` in the
official clone's sim/<class>/spell_data_auto_gen.go, and the fork's when the old clone is present), or to `LEGACY` (ids the fork
registered under another id: proc auras, renumbered spells). Downranking lines therefore collapse onto the one rank (the official
simulator has no lower ranks to cast). What stays unresolved is listed; `--write` rewrites the files and the record
`raidsim/apl-remap.json`.
"""
import argparse
import json
import os
import pathlib
import re
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[2]
sys.path.insert(0, str(HERE))
import run as R  # noqa: E402

TOOLS = pathlib.Path(os.environ.get("WOW_FOREVER_TOOLS", pathlib.Path.home() / ".wow-forever-tools"))
OLD = TOOLS / "forever-repo"
# ids the fork used that are no rank of a chain in the official data (checked by hand, 2026-10-18)
LEGACY = {
    44404: 400589,   # Missile Barrage proc aura: the fork's legacy id, the official aura id
}


def families(repo):
    """id -> (chain name, [ids]) from every sim/<class>/spell_data_auto_gen.go of a clone."""
    out = {}
    for p in (repo / "sim").glob("*/spell_data_auto_gen.go"):
        for m in re.finditer(r"^\s*(\w+):\s*spelldata\.Ranked\(([^)]*)\)", p.read_text(encoding="utf-8"), re.M):
            ids = [int(i) for i in re.findall(r"\d+", m.group(2))]
            for i in ids:
                out.setdefault(i, (f"{p.parent.name}.{m.group(1)}", ids))
    return out


def registered(cls, repo):
    """{spell ids}, {aura spell ids} the class's entries register (bench `spells` mode, every build of every entry)."""
    trees = R.load_trees(repo, cls)
    data = json.load(open(ROOT / cls / R.GAMES["forever"]["builds"], encoding="utf-8"))
    by_id = {b["id"]: b for b in data["builds"]}
    spells, auras = set(), set()
    for spec, entry in R.SPECS[cls].items():
        builds = []
        for bid in entry.get("builds", []):
            b = by_id.get(bid) if not bid.endswith(".json") else json.load(open(ROOT / bid if not os.path.isabs(bid) else bid, encoding="utf-8"))
            if b:
                builds.append({"label": b.get("id", bid), "talents": R.talents_string(trees, R.alloc_of(b))})
        if not builds:
            continue
        # every talent at its full rank (not a legal build, but the simulator takes the string): registers every talent's spell, so
        # a rotation line for a talent none of the entry's builds holds still resolves
        builds.append({"label": "all-talents", "talents": "-".join("".join(str(t["maxPoints"]) for t in tr["talents"]) for tr in trees)})
        for where in ("dummy", "raid"):
            cfg = {"class": entry["sim_class"], "race": entry.get("race", "RaceHuman"), "gear": R.sim_path(entry["gear"]),
                   "spec": entry.get("spec", {}), **R.setting_cfg(entry, where), "iterations": 1, "duration": 10, "seed": 1,
                   "isTank": entry.get("tank", False), "spells": True, "builds": builds}
            path = repo / "bench" / f"spells-{cls}-{spec}.json"
            path.parent.mkdir(exist_ok=True)
            path.write_text(json.dumps(cfg), encoding="utf-8")
            r = subprocess.run([str(repo / "foreverbench.exe" if (repo / "foreverbench.exe").exists() else repo / "foreverbench"),
                                "--config", str(path), "--root", str(repo)], capture_output=True, text=True, encoding="utf-8", errors="replace", cwd=str(repo))
            if r.returncode:
                print(f"  {cls} {spec}: bench failed: {r.stderr[-500:]}")
                continue
            for line in r.stdout.splitlines():
                if not line.startswith("{"):
                    continue
                d = json.loads(line)
                units = [d] + (d.get("pets") or [])
                auras.update(a["spellId"] for a in d.get("target_auras") or [] if a.get("spellId"))
                for u in units:
                    spells.update(u.get("spells") or [])
                    auras.update(a["spellId"] for a in u.get("auras") or [] if a.get("spellId"))
    return spells, auras


def walk(o, fn, path=""):
    if isinstance(o, dict):
        for k, v in o.items():
            if isinstance(v, dict) and set(v) & {"spellId"} and isinstance(v.get("spellId"), int):
                fn(v, f"{path}.{k}")
            walk(v, fn, f"{path}.{k}")
    elif isinstance(o, list):
        for i, v in enumerate(o):
            walk(v, fn, f"{path}[{i}]")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("classes", nargs="*")
    ap.add_argument("--repo", default=os.environ.get("WOW_FOREVER_SIM", str(TOOLS / "wowsims-forever")))
    ap.add_argument("--write", action="store_true")
    a = ap.parse_args()
    repo = pathlib.Path(a.repo)
    fam = families(repo)
    if OLD.exists():
        for i, f in families(OLD).items():   # the fork's chains: ids the official data renumbered join by chain name
            fam.setdefault(i, f)
    by_name = {}
    for i, (n, ids) in fam.items():
        by_name.setdefault(n.split(".", 1)[1], set()).update(ids)
    record_path = HERE / "apl-remap.json"
    record = json.load(open(record_path, encoding="utf-8")) if record_path.exists() else {}
    for cls in a.classes or [c for c in R.SPECS if isinstance(R.SPECS[c], dict)]:
        spells, auras = registered(cls, repo)
        known = spells | auras
        changes, unresolved = {}, {}
        for f in sorted((HERE / "apls" / cls).glob("*.json")):
            data = json.load(open(f, encoding="utf-8"))
            fc = []

            def fix(aid, where):
                sid = aid["spellId"]
                if sid in known:
                    return
                if sid in LEGACY and LEGACY[sid] in known:
                    new = LEGACY[sid]
                else:
                    order = fam[sid][1] if sid in fam else []
                    chain = by_name.get(fam[sid][0].split(".", 1)[1], set()) if sid in fam else set()
                    hits = [i for i in order if i in known] + sorted((chain - set(order)) & known)
                    if not hits:
                        unresolved.setdefault(f.name, set()).add(sid)
                        return
                    # the registered rank nearest below the line's rank (a downranking line keeps the lowest the simulator has),
                    # else the lowest registered
                    pos = order.index(sid) if sid in order else len(order)
                    below = [i for i in hits if i in order and order.index(i) <= pos]
                    new = below[-1] if below else hits[0]
                fc.append((sid, new))
                aid["spellId"] = new
            walk(data, fix)
            if fc:
                changes[f.name] = sorted(set(fc))
                if a.write:
                    f.write_text(json.dumps(data, indent=1) + "\n", encoding="utf-8")
        print(f"== {cls}: {len(spells)} spells, {len(auras)} auras registered")
        for fn, ch in changes.items():
            print(f"  {fn}: " + ", ".join(f"{o}->{n}" for o, n in ch))
        for fn, ids in unresolved.items():
            print(f"  UNRESOLVED {fn}: {sorted(ids)}")
        record[cls] = {"changes": changes, "unresolved": {k: sorted(v) for k, v in unresolved.items()}, "sim": R.git_commit(repo)}
    if a.write:
        record_path.write_text(json.dumps(record, indent=1) + "\n", encoding="utf-8")
        print(f"wrote {record_path}")


if __name__ == "__main__":
    main()
