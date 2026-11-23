"""A set's final hit, from the simulator's own character sheet (2026-11-23, the user's hit ask, the audit session's item 1: "Things like hit
chance will be capped at 8%, but for dual wield, hit is still relevant past 8%"). The set makers judge hit by the race; this shows it.

This builds a third bench, foreverbench-stats.exe, from foreverbench/main.go with one change: its validate mode also prints the player's
final pseudo-stats (core.ComputeStats: the character sheet's melee, off-hand, ranged and spell hit percents, school hit, crit) and the set
bonuses the gear turns on. The main bench, its build stamp and every race fingerprint stay as they are (setup.patch_hash hashes
foreverbench/main.go and the patches only; this file is neither), as with flags_bench.py.

    python _reference/data/raidsim/stats_bench.py --build                # (re)build it in the WOW_FOREVER_SIM checkout

gear_tiers.make calls hit_report() on the chosen set: the hits against the caps of _reference/forever-stats.md rule 3 (raid bosses:
yellow melee and ranged 8%, white dual-wield swings 27%, spells 17%), and a flag when a hit the spec uses is past its last useful cap by
more than 1% (the audit session's rule).
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
EXE = "foreverbench-stats.exe" if sys.platform.startswith("win") else "foreverbench-stats"
CAPS = {"melee": 8.0, "dual_wield_white": 27.0, "ranged": 8.0, "spell": 17.0}
FLAG_OVER = 1.0
# the hit kinds each spec's damage uses (the ML records' specs, 2026-11-23). Hit is one stat for melee, ranged and spells
# (_reference/forever-stats.md rule 2; talents add to one kind), so a point of hit is wasted only when every kind the spec uses is past
# its cap: Enhancement's shocks and a Retribution paladin's spells keep spell hit useful to 17% after melee passes 8%. A hunter's
# shots use ranged hit; its melee counts only where the spec plays the melee rotation.
MELEE = {"warrior": None, "rogue": None, "druid": {"Feral Combat"}, "shaman": {"Enhancement", "Hybrid Elemental/Enhancement"},
         "paladin": {"Retribution", "Hybrid Protection/Retribution", "Hybrid Holy/Retribution"},
         "hunter": {"Survival", "Hybrid Beast Mastery/Survival"}}
SPELL = {"mage": None, "warlock": None, "priest": None, "druid": {"Balance"}, "shaman": {"Elemental", "Enhancement", "Hybrid Elemental/Enhancement"},
         "paladin": {"Retribution", "Hybrid Protection/Retribution", "Hybrid Holy/Retribution"}}
RANGED = {"hunter": None}


def uses_of(cls, spec):
    """[hit kind] the spec's damage uses: "melee", "ranged", "spell"."""
    on = lambda table: cls in table and (table[cls] is None or spec in table[cls])   # noqa: E731
    return [k for k, table in (("melee", MELEE), ("ranged", RANGED), ("spell", SPELL)) if on(table)]


OLD = """			res := core.ComputeStats(&proto.ComputeStatsRequest{Raid: raid, Encounter: encounter})
			out := map[string]interface{}{"label": b.Label}"""
NEW = """			res := core.ComputeStats(&proto.ComputeStatsRequest{Raid: raid, Encounter: encounter})
			out := map[string]interface{}{"label": b.Label}
			if res.ErrorResult == "" && res.RaidStats != nil && len(res.RaidStats.Parties) > 0 && len(res.RaidStats.Parties[0].Players) > 0 {
				if pl := res.RaidStats.Parties[0].Players[0]; pl != nil && pl.FinalStats != nil {
					ps := map[string]float64{}
					for i, v := range pl.FinalStats.PseudoStats {
						ps[proto.PseudoStat(i).String()] = v
					}
					out["pseudo_stats"] = ps
					out["sets"] = pl.Sets
				}
			}"""


def _raidrun():
    import importlib.util
    want = (HERE / "run.py").resolve()
    for name in ("raidrun", "run"):
        m = sys.modules.get(name)
        if m is not None and getattr(m, "__file__", None) and pathlib.Path(m.__file__).resolve() == want:
            return m
    spec = importlib.util.spec_from_file_location("raidrun", want)
    m = importlib.util.module_from_spec(spec)
    sys.modules["raidrun"] = m
    spec.loader.exec_module(m)
    return m


def build(repo):
    import setup as S
    src = (HERE / "foreverbench" / "main.go").read_text(encoding="utf-8")
    if src.count(OLD) != 1:
        raise SystemExit("foreverbench/main.go no longer has the validate-mode text this build edits")
    src = src.replace(OLD, NEW, 1)
    tools = pathlib.Path(os.environ.get("WOW_FOREVER_TOOLS", str(pathlib.Path.home() / ".wow-forever-tools")))
    exe = ".exe" if sys.platform.startswith("win") else ""
    go_dir, protoc_dir, gopath = tools / "go", tools / "protoc", tools / "gopath"
    go = go_dir / "bin" / f"go{exe}"
    env = dict(os.environ, GOPATH=str(gopath), GOMODCACHE=str(gopath / "pkg" / "mod"), GOCACHE=str(tools / "gocache"), GOFLAGS="-mod=mod",
               GOTOOLCHAIN=os.environ.get("GOTOOLCHAIN", "auto"),
               PATH=os.pathsep.join([str(go_dir / "bin"), str(protoc_dir / "bin"), str(gopath / "bin"), os.environ.get("PATH", "")]))
    d = repo / "cmd" / "foreverbench-stats"
    d.mkdir(parents=True, exist_ok=True)
    (d / "main.go").write_text(src, encoding="utf-8")
    r = subprocess.run([str(go), "build", "--tags=with_db", "-o", EXE, "./cmd/foreverbench-stats"], cwd=str(repo), env=env,
                       capture_output=True, text=True)
    if r.returncode:
        raise SystemExit(f"build failed:\n{r.stdout[-3000:]}\n{r.stderr[-3000:]}")
    (repo / "foreverbench-stats.json").write_text(json.dumps({"built": datetime.datetime.now().isoformat(timespec="seconds"),
                                                              "patch_hash": S.patch_hash()}) + "\n", encoding="utf-8")
    print(f"built {repo / EXE}")


def final_stats(entry, repo, builds, setting="raid", bench_cfg=None):
    """{label: {"pseudo_stats": {name: value}, "sets": [...]}} for builds [{label, talents, gear_json?}], the entry's character as the
    races set it up (validate mode: one ComputeStats, no fights). `bench_cfg`: the caller's gear_opt.bench_cfg, so the character is
    the races' own (gear_tiers passes its copy's); without it the same fields are built here."""
    exe = repo / EXE
    if not exe.exists():
        raise SystemExit(f"no {EXE} in {repo}: python _reference/data/raidsim/stats_bench.py --build")
    if bench_cfg is not None:
        cfg = bench_cfg(entry, repo, builds, 1, 1, setting, validate=True)
    else:
        R = _raidrun()
        cfg = {"class": entry["sim_class"], "race": entry.get("race", "RaceHuman"), "gear": R.sim_path(entry["gear"]),
               "apl": str(R.apl_path(entry, repo, setting)), "spec": entry.get("spec", {}), **R.setting_cfg(entry, setting),
               "profession1": entry.get("profession1", "Engineering"), "profession2": entry.get("profession2", ""),
               "distanceFromTarget": entry.get("distance", 5), "inFrontOfTarget": entry.get("in_front", False), "reactionTimeMs": 200,
               "iterations": 1, "duration": R.FIGHT, "seed": R.sim_seed(1), "isTank": entry.get("tank", False), "builds": builds,
               "validate": True}
    d = repo / "bench"
    d.mkdir(exist_ok=True)
    p = d / f"stats-{os.getpid()}.json"
    p.write_text(json.dumps(cfg), encoding="utf-8")
    r = subprocess.run([str(exe), "--config", str(p), "--root", str(repo)], capture_output=True, text=True, encoding="utf-8", errors="replace")
    p.unlink(missing_ok=True)
    if r.returncode:
        raise SystemExit(f"stats bench failed: {r.stderr[-1500:]}")
    out = {}
    for line in r.stdout.splitlines():
        if line.startswith("{"):
            x = json.loads(line)
            out[x["label"]] = {"pseudo_stats": x.get("pseudo_stats") or {}, "sets": x.get("sets") or []}
    return out


def hit_report(cls, spec, entry, repo, talents, items, setting="raid", bench_cfg=None):
    """The set's hits against the caps, and the flags: a hit the spec uses past its last useful cap by more than FLAG_OVER. A dual
    wielder's melee hit is useful to the white swings' cap, a two-hander's or a bow's to the yellow cap, a caster's spell hit to 17%."""
    fs = final_stats(entry, repo, [{"label": "set", "talents": talents, "gear_json": {"items": items}}], setting, bench_cfg).get("set") or {}
    ps = fs.get("pseudo_stats") or {}
    g = lambda k: round(ps.get(k, 0.0), 2)   # noqa: E731
    hits = {"melee_main_hand": g("PseudoStatMeleeHitPercent"), "melee_off_hand": g("PseudoStatOffHandHitPercent"),
            "ranged": g("PseudoStatRangedHitPercent"), "spell": g("PseudoStatSpellHitPercent")}
    od = items[15] if len(items) > 15 and isinstance(items[15], dict) else {}
    dual = bool(od.get("id")) and hits["melee_off_hand"] > 0
    uses = []
    for k in uses_of(cls, spec):
        if k == "melee" and dual:
            uses += [("melee_main_hand", hits["melee_main_hand"], CAPS["dual_wield_white"]), ("melee_off_hand", hits["melee_off_hand"], CAPS["dual_wield_white"])]
        elif k == "melee":
            uses.append(("melee_main_hand", hits["melee_main_hand"], CAPS["melee"]))
        elif k == "ranged":
            uses.append(("ranged", hits["ranged"], CAPS["ranged"]))
        else:
            uses.append(("spell", hits["spell"], CAPS["spell"]))
    past = [(k, v, cap) for k, v, cap in uses if v > cap + FLAG_OVER]
    under = [(k, v, cap) for k, v, cap in uses if v <= cap]
    flags = ["hit past its last useful cap: " + "; ".join(f"{k} {v:.2f}% against {cap:.0f}%" for k, v, cap in uses)] if uses and len(past) == len(uses) else []
    notes = [f"{k} {v:.2f}% is past its cap {cap:.0f}%; the hit still counts for " + ", ".join(f"{k2} {v2:.2f}% of {c2:.0f}%" for k2, v2, c2 in under)
             for k, v, cap in past if under]
    return {"hits": hits, "caps": CAPS, "used": [{"hit": k, "value": v, "cap": cap} for k, v, cap in uses], "dual_wield": dual,
            "flags": flags, "notes": notes, "sets": fs.get("sets") or [],
            "source": "the simulator's character sheet (stats_bench.py, core.ComputeStats), raid setting; caps: _reference/forever-stats.md rule 3"}


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--build", action="store_true")
    a = ap.parse_args()
    R = _raidrun()
    R.set_game("forever")
    repo = R.repo_path(argparse.Namespace(repo=None))
    if a.build:
        build(repo)


if __name__ == "__main__":
    main()
