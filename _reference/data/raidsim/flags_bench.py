"""Which casts a rotation may make (2026-11-20 night, the audit session's D12 and its guard a). The simulator's rotation lookup
(sim/core/apl_helpers.go, GetAPLSpell) prefers a spell flagged SpellFlagAPL with the exact id and tag, and otherwise falls back to any
registered spell with that id and tag, flagged or not, without a warning: a rotation can fire an internal sub-action. Our bear rotation
cast Maul's swing-damage spell (9881 tag 1, registered without the flag in sim/druid/maul.go) off the swing timer from 2026-11-16 to
2026-11-20, about seven times the threat.

This builds a second bench, foreverbench-flags.exe, from foreverbench/main.go with one change: its spells mode also lists every spell
the character registers with its tag and whether it carries SpellFlagAPL. The main bench, its build stamp and every race fingerprint stay
as they are (setup.patch_hash hashes foreverbench/main.go and the patches only; this file is neither).

    python _reference/data/raidsim/flags_bench.py --build          # (re)build it in the WOW_FOREVER_SIM checkout
    python _reference/data/raidsim/flags_bench.py [classes] [--write]   # every cast of our rotation files, judged

A cast is "rotation" when a flagged spell has its id and tag, "INTERNAL" when only unflagged spells do (the line fires a sub-action: a
FAIL), "unknown" when the character registers nothing with that id and tag (apl_validate's job). Each rotation is judged on a build with
every talent at full rank (apl_validate --all-talents), so talent spells are registered. Record raidsim/flags-check.json.
"""
import argparse
import datetime
import json
import os
import pathlib
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path[:0] = [str(HERE), str(HERE.parent)]
OUT = HERE / "flags-check.json"
EXE = "foreverbench-flags.exe" if sys.platform.startswith("win") else "foreverbench-flags"

OLD = """				for _, s := range u.Spellbook {
					if id := s.ActionID.SpellID; id != 0 {
						spells = append(spells, id)
					}
				}"""
NEW = """				for _, s := range u.Spellbook {
					if id := s.ActionID.SpellID; id != 0 {
						spells = append(spells, id)
						flagRows[u] = append(flagRows[u], map[string]interface{}{"id": id, "tag": s.ActionID.Tag, "apl": s.Flags.Matches(core.SpellFlagAPL)})
					}
				}"""
OLD2 = """			list := func(u *core.Unit) (spells []int32, auras []map[string]interface{}) {"""
NEW2 = """			flagRows := map[*core.Unit][]map[string]interface{}{}
			list := func(u *core.Unit) (spells []int32, auras []map[string]interface{}) {"""
OLD3 = """			out := map[string]interface{}{"label": b.Label, "spells": sp, "auras": au}"""
NEW3 = """			out := map[string]interface{}{"label": b.Label, "spells": sp, "auras": au}
			out["rotation_flags"] = flagRows[&ch.Unit]"""


def build(repo):
    import setup as S
    src = (HERE / "foreverbench" / "main.go").read_text(encoding="utf-8")
    for o, n in ((OLD, NEW), (OLD2, NEW2), (OLD3, NEW3)):
        if src.count(o) != 1:
            raise SystemExit(f"foreverbench/main.go no longer has the spells-mode text this build edits: {o.strip()[:60]}")
        src = src.replace(o, n, 1)
    tools = pathlib.Path(os.environ.get("WOW_FOREVER_TOOLS", str(pathlib.Path.home() / ".wow-forever-tools")))
    exe = ".exe" if sys.platform.startswith("win") else ""
    go_dir, protoc_dir, gopath = tools / "go", tools / "protoc", tools / "gopath"
    go = go_dir / "bin" / f"go{exe}"
    env = dict(os.environ, GOPATH=str(gopath), GOMODCACHE=str(gopath / "pkg" / "mod"), GOCACHE=str(tools / "gocache"), GOFLAGS="-mod=mod",
               GOTOOLCHAIN=os.environ.get("GOTOOLCHAIN", "auto"),
               PATH=os.pathsep.join([str(go_dir / "bin"), str(protoc_dir / "bin"), str(gopath / "bin"), os.environ.get("PATH", "")]))
    d = repo / "cmd" / "foreverbench-flags"
    d.mkdir(parents=True, exist_ok=True)
    (d / "main.go").write_text(src, encoding="utf-8")
    r = subprocess.run([str(go), "build", "--tags=with_db", "-o", EXE, "./cmd/foreverbench-flags"], cwd=str(repo), env=env,
                       capture_output=True, text=True)
    if r.returncode:
        raise SystemExit(f"build failed:\n{r.stdout[-3000:]}\n{r.stderr[-3000:]}")
    (repo / "foreverbench-flags.json").write_text(json.dumps({"built": datetime.datetime.now().isoformat(timespec="seconds"),
                                                              "patch_hash": S.patch_hash()}) + "\n", encoding="utf-8")
    print(f"built {repo / EXE}")


def registered(entry, repo, builds, setting="raid"):
    """{label: {(id, tag): flagged}} for builds [{label, talents}], the entry's character as the races set it up."""
    import run as R
    exe = repo / EXE
    if not exe.exists():
        raise SystemExit(f"no {EXE} in {repo}: python _reference/data/raidsim/flags_bench.py --build")
    cfg = {"class": entry["sim_class"], "race": entry.get("race", "RaceHuman"), "gear": R.sim_path(entry["gear"]),
           "apl": str(R.apl_path(entry, repo, setting)), "spec": entry.get("spec", {}), **R.setting_cfg(entry, setting),
           "profession1": entry.get("profession1", "Engineering"), "profession2": entry.get("profession2", ""),
           "distanceFromTarget": entry.get("distance", 5), "inFrontOfTarget": entry.get("in_front", False), "reactionTimeMs": 200,
           "iterations": 1, "duration": R.FIGHT, "seed": 1, "isTank": entry.get("tank", False), "builds": builds, "spells": True}
    d = repo / "bench"
    d.mkdir(exist_ok=True)
    p = d / f"flags-{os.getpid()}.json"
    p.write_text(json.dumps(cfg), encoding="utf-8")
    r = subprocess.run([str(exe), "--config", str(p), "--root", str(repo)], capture_output=True, text=True, encoding="utf-8", errors="replace")
    p.unlink(missing_ok=True)
    if r.returncode:
        raise SystemExit(f"flags bench failed: {r.stderr[-1500:]}")
    out = {}
    for line in r.stdout.splitlines():
        if line.startswith("{"):
            x = json.loads(line)
            m = {}
            for s in x.get("rotation_flags") or []:
                k = (int(s["id"]), int(s.get("tag") or 0))
                m[k] = m.get(k, False) or bool(s.get("apl"))
            out[x["label"]] = m
    return out


def casts(apl):
    """[(part, index, id, tag)] of every castSpell / channelSpell in a rotation, nested ones included (groups, sequences)."""
    out = []

    def walk(x, part, i):
        if isinstance(x, dict):
            for k, v in x.items():
                if k in ("castSpell", "channelSpell") and isinstance(v, dict):
                    sid = v.get("spellId") or {}
                    if sid.get("spellId"):
                        out.append((part, i, int(sid["spellId"]), int(sid.get("tag") or 0)))
                walk(v, part, i)
        elif isinstance(x, list):
            for v in x:
                walk(v, part, i)
    for part in ("prepullActions", "priorityList"):
        for i, x in enumerate(apl.get(part) or []):
            walk(x, part, i)
    for g in apl.get("groups") or []:
        for i, x in enumerate(g.get("actions") or []):
            walk(x, f"group {g.get('name', '?')}", i)
    return out


def verdicts(cls, ename, entry, repo, names=None):
    """{rotation file: [(part, i, id, tag, verdict)]} for the entry's raid and dummy rotations, judged on every talent at full rank."""
    import run as R
    trees = R.load_trees(repo, cls)
    full = "-".join("".join(str(t["maxPoints"]) for t in tr["talents"]) for tr in trees)
    out = {}
    for where in ("raid", "dummy"):
        if entry.get("tank") and where == "dummy":
            continue
        path = pathlib.Path(R.apl_path(entry, repo, where))
        if str(path) in out:
            continue
        reg = registered(entry, repo, [{"label": "all-talents", "talents": full}], where).get("all-talents") or {}
        apl = json.loads(path.read_text(encoding="utf-8"))
        rows = []
        for part, i, sid, tag in casts(apl):
            if (sid, tag) not in reg:
                v = "unknown"
            elif reg[(sid, tag)]:
                v = "rotation"
            else:
                v = "INTERNAL"
            rows.append((part, i, sid, tag, v))
        out[str(path)] = rows
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("classes", nargs="*")
    ap.add_argument("--build", action="store_true")
    ap.add_argument("--write", action="store_true")
    a = ap.parse_args()
    import run as R
    R.set_game("forever")
    repo = R.repo_path(argparse.Namespace(repo=None))
    if a.build:
        build(repo)
        return
    rec = {"date": datetime.date.today().isoformat(), "classes": {}}
    bad = 0
    for cls in a.classes or [c for c in R.SPECS if isinstance(R.SPECS[c], dict)]:
        names = R.spell_names(repo, cls)
        for ename, entry in R.SPECS[cls].items():
            if not isinstance(entry, dict) or not entry.get("apl"):
                continue
            res = verdicts(cls, ename, entry, repo)
            for f, rows in res.items():
                internal = [r for r in rows if r[4] == "INTERNAL"]
                bad += len(internal)
                rel = pathlib.Path(f).as_posix().split("_reference/data/")[-1]
                print(f"== {cls} {ename} {rel}: {len(rows)} casts, " + (f"INTERNAL {len(internal)}" if internal else "all rotation casts")
                      + (f", unknown {sum(1 for r in rows if r[4] == 'unknown')}" if any(r[4] == "unknown" for r in rows) else ""), flush=True)
                for part, i, sid, tag, v in rows:
                    if v != "rotation":
                        print(f"   {v}: {part}[{i}] {names.get(sid, sid)} ({sid}{f' tag {tag}' if tag else ''})", flush=True)
                rec["classes"].setdefault(cls, {}).setdefault(ename, {})[rel] = [
                    {"part": p, "index": i, "id": s, "tag": t, "name": names.get(s), "verdict": v} for p, i, s, t, v in rows if v != "rotation"]
    print(f"INTERNAL casts: {bad}")
    if a.write:
        OUT.write_text(json.dumps(rec, indent=1) + "\n", encoding="utf-8")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
