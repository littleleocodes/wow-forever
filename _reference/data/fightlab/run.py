"""Run the fight lab for a class/spec/build and write a report.

    python _reference/data/fightlab/run.py mage --spec frost-leveling --build opt-frost-leveling-leveling-st
        [--compare leveling-frost ...] [--levels 20,30,40,50,60] [--fights 800] [--deltas 30,60] [--seed 1]
        [--mob-level +0] [--log] [--write]

Outputs (with --write): <class>/research/leveling/fightlab/<spec>.md and .json. For every level: the distribution of
fight times, mana per kill, downtime, deaths and kills per hour, plus the measured damage shares (to compare with the
spec model's assumed shares). With --deltas: the value of every talent in the build at those levels, measured as the
change in time per kill when the talent is removed (common random numbers), next to the expected-value scorer's
value of the same removal.
"""
import argparse
import json
import os
import pathlib
import statistics
import sys
import time

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[2]
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(ROOT / "_reference/data/scorer"))
sys.path.append(str(pathlib.Path(__file__).resolve().parents[1]))   # _reference/data: paths.py
import paths  # noqa: E402
from data_build import BUILD as DATA_BUILD  # noqa: E402

from engine import Session, paired_delta  # noqa: E402
import tables  # noqa: E402

MODULES = {"mage": ("mage", "MageModule"), "priest": ("priest", "PriestModule"), "warlock": ("warlock", "WarlockModule"),
           "hunter": ("hunter", "HunterModule"), "warrior": ("warrior", "WarriorModule"), "rogue": ("rogue", "RogueModule"),
           "paladin": ("paladin", "PaladinModule"), "shaman": ("shaman", "ShamanModule"), "druid": ("druid", "DruidModule")}
PROFILE_FOR_SPEC = {"frost-leveling": "leveling-st", "frost-aoe": "leveling-aoe"}   # default: leveling-st


def class_module(cls):
    return __import__(MODULES[cls][0])


def load_build(cls, build_id):
    if build_id.endswith(".json"):   # a candidate build in a file: {"id", "allocation", "order"} like a proposed-builds.json entry
        b = json.load(open(build_id, encoding="utf-8"))
        b.setdefault("id", pathlib.Path(build_id).stem)
        return b
    data = json.load(open(ROOT / cls / "research/talents/forever/proposed-builds.json", encoding="utf-8"))
    for b in data["builds"]:
        if b["id"] == build_id:
            return b
    raise SystemExit(f"build {build_id} not found")


def allocation_at(build, level):
    """Talents held at `level`: the leveling order's first level-9 points, or the full allocation at 60."""
    if level >= 60 or not build.get("order"):
        return {n: r for items in build["allocation"].values() for n, r in items}
    alloc = {}
    for step in build["order"]:
        lo = int(step["levels"].split("-")[0])
        hi = int(step["levels"].split("-")[-1])
        if hi <= level:
            alloc[step["talent"]] = alloc.get(step["talent"], 0) + step["points"]
        elif lo <= level:
            alloc[step["talent"]] = alloc.get(step["talent"], 0) + (level - lo + 1)
    return alloc


PROFILE_SUFFIXES = ("leveling-st", "leveling-aoe", "solo-60", "raid-dps-extwc", "raid-dps", "raid-heal", "raid-tank")


def spec_of_build(cls, build_id, default):
    """`opt-<spec>-<profile>` builds carry their spec model in the id; other builds use the run's spec."""
    if build_id.startswith("opt-"):
        for suf in PROFILE_SUFFIXES:
            if build_id.endswith("-" + suf):
                spec = build_id[4: -len(suf) - 1]
                models = json.load(open(ROOT / "_reference/data/scorer/specs" / f"{cls}.json", encoding="utf-8"))["models"]
                if spec in models:
                    return spec
    return default


ROTATIONS = pathlib.Path(__file__).resolve().parent / "rotations"


def rotation_file(cls, spec):
    return ROTATIONS / f"{cls}-{spec}.json"


def apply_rotation(mod, cls, spec, rot=None):
    """Tuned rotation rules for this class and spec model (fightlab/rotation_opt.py): spell vetoes, the rest thresholds and the
    module's own rotation knobs. WOW_FL_ROTATION=default runs the hand-written rotation alone (the regression check)."""
    if rot is None:
        if os.environ.get("WOW_FL_ROTATION") == "default":
            return mod
        p = rotation_file(cls, spec)
        if not p.exists():
            return mod
        rot = json.load(open(p, encoding="utf-8"))
    mod.veto = {k: dict(v) for k, v in (rot.get("veto") or {}).items()}
    for k in ("drink_below", "eat_below"):
        if rot.get(k) is not None:
            setattr(mod, k, rot[k])
    for k, v in (rot.get("knobs") or {}).items():
        setattr(mod, k, v)
    return mod


def make_module(cls, talents, level, spec, rot=None):
    modname, clsname = MODULES[cls]
    mod = __import__(modname)
    return apply_rotation(getattr(mod, clsname)(talents, level, spec=spec), cls, spec, rot)


def simulate(cls, talents, level, spec, fights, seed, mob_off, log_first=0, rot=None):
    mod = make_module(cls, talents, level, spec, rot)
    s = Session(mod, level=level, fights=fights, seed=seed, mob_level_offset=mob_off, log_first=log_first)
    out = s.run()
    out["not_simulated"] = mod.not_simulated()
    out["armor_spell"] = mod.armor_spell_used
    out["player"] = {k: round(v, 4) for k, v in vars(mod.make_player(level)).items() if isinstance(v, (int, float))}
    return out


def ev_scores(cls, spec, level, alloc):
    """Expected-value scorer: score of the allocation and of each single-talent removal (fraction of time per kill saved)."""
    try:
        from optimize import Optimizer
    except Exception as e:  # pragma: no cover
        print("scorer unavailable:", e)
        return None
    try:
        opt = Optimizer("forever", cls, spec, PROFILE_FOR_SPEC.get(spec, "leveling-st"))
    except KeyError:   # a fight-lab rotation with no stats model of its own (the mage's frostfire-leveling check, 2026-10-09)
        return None
    base = opt.score(alloc, level)
    out = {"base": base, "removals": {}}
    for name in alloc:
        trial = {k: v for k, v in alloc.items() if k != name}
        # same scale as the sim: relative to the build's own time per kill (the score is relative to a talentless character)
        out["removals"][name] = (base - opt.score(trial, level)) / max(1e-9, 1.0 - base)
    return out


def apply_gear(tier):
    apply_overrides([f"{k}={v}" for k, v in tables.GEAR_TIERS[tier].items()])


def apply_overrides(pairs):
    """--set KEY=VALUE: set on tables (functions read module globals at call time) and on engine's imported copies."""
    import engine
    for pair in pairs:
        key, val = pair.split("=", 1)
        try:
            val = float(val)
        except ValueError:
            pass   # string constants (GEAR_TIER=blues)
        if not hasattr(tables, key):
            raise SystemExit(f"unknown tables constant {key}")
        setattr(tables, key, val)
        if hasattr(engine, key):
            setattr(engine, key, val)


def fmt_pct(x):
    return f"{x * 100:+.1f}%"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("cls")
    ap.add_argument("--spec", default="frost-leveling")
    ap.add_argument("--build", required=True)
    ap.add_argument("--compare", nargs="*", default=[])
    ap.add_argument("--levels", default="20,30,40,50,60")
    ap.add_argument("--fights", type=int, default=800)
    ap.add_argument("--deltas", default="")
    ap.add_argument("--seed", type=int, default=1)
    ap.add_argument("--mob-level", type=int, default=0)
    ap.add_argument("--log", action="store_true")
    ap.add_argument("--write", action="store_true")
    ap.add_argument("--name", default=None, help="report file stem (default: the spec id); a variant of the same model uses <spec>-<tag>")
    ap.add_argument("--set", action="append", default=[], help="override a tables.py constant, e.g. --set ROOT_BREAK_CHANCE=0.4 --set MOB_HP_MULT=1.2")
    ap.add_argument("--gear", default="greens", choices=sorted(tables.GEAR_TIERS), help="gear tier for every run (tables.GEAR_TIERS)")
    ap.add_argument("--gear-tiers", action="store_true", help="also run the main build in the other gear tiers at every level (report section)")
    a = ap.parse_args()
    apply_gear(a.gear)
    apply_overrides(a.set)
    levels = [int(x) for x in a.levels.split(",") if x]
    delta_levels = [int(x) for x in a.deltas.split(",") if x]
    build = load_build(a.cls, a.build)
    others = [load_build(a.cls, b) for b in a.compare]
    t0 = time.time()
    results = {"class": a.cls, "spec": a.spec, "build": a.build, "fights": a.fights, "seed": a.seed, "mob_level_offset": a.mob_level,
               "gear": a.gear, "levels": {}, "compare": {}, "deltas": {}, "gear_tiers": {}}

    print(f"== {a.cls} {a.spec} {a.build}: {a.fights} fights per level, seed {a.seed}")
    for L in levels:
        alloc = allocation_at(build, L)
        r = simulate(a.cls, alloc, L, a.spec, a.fights, a.seed, a.mob_level, log_first=1 if a.log else 0)
        r["allocation"] = alloc
        results["levels"][L] = r
        print(f"L{L}: fight {r['fight_mean']:.1f}s (median {r['fight_median']:.1f}, p90 {r['fight_p90']:.1f}), downtime {r['downtime_per_kill']:.1f}s, "
              f"deaths/100 {r['deaths_per_100']:.1f}, time/kill {r['time_per_kill']:.1f}s, {r['kills_per_hour']:.0f} kills/h, mana/kill {r['mana_per_kill']:.0f}, "
              f"shares " + ", ".join(f"{k} {v * 100:.0f}%" for k, v in list(r["shares"].items())[:5]))
        if a.log and r["logs"]:
            res, lines = r["logs"][0]
            print(f"   first fight ({res}):")
            for line in lines:
                print("     " + line)
        for ob in others:
            oalloc = allocation_at(ob, L)
            ospec = spec_of_build(a.cls, ob["id"], a.spec)   # an optimizer build of another spec model plays with that model's rotation
            orr = simulate(a.cls, oalloc, L, ospec, a.fights, a.seed, a.mob_level)
            orr["allocation"] = oalloc
            orr["spec"] = ospec
            results["compare"].setdefault(ob["id"], {})[L] = orr
            d = (orr["time_per_kill"] - r["time_per_kill"]) / r["time_per_kill"]
            print(f"   vs {ob['id']}{' as ' + ospec if ospec != a.spec else ''}: time/kill {orr['time_per_kill']:.1f}s ({fmt_pct(d)}), fight {orr['fight_mean']:.1f}s, deaths/100 {orr['deaths_per_100']:.1f}")

    if a.gear_tiers:
        for tier in sorted(tables.GEAR_TIERS):
            if tier == a.gear:
                continue
            apply_gear(tier)
            apply_overrides(a.set)
            for L in levels:
                r = simulate(a.cls, allocation_at(build, L), L, a.spec, a.fights, a.seed, a.mob_level)
                results["gear_tiers"].setdefault(tier, {})[L] = {k: r[k] for k in ("time_per_kill", "fight_mean", "deaths_per_100", "downtime_per_kill", "kills_per_hour")}
                base = results["levels"][L]
                print(f"   {tier} L{L}: time/kill {r['time_per_kill']:.1f}s ({fmt_pct((r['time_per_kill'] - base['time_per_kill']) / base['time_per_kill'])}), fight {r['fight_mean']:.1f}s, deaths/100 {r['deaths_per_100']:.1f}")
            apply_gear(a.gear)
            apply_overrides(a.set)
    for L in delta_levels:
        alloc = allocation_at(build, L)
        base = results["levels"].get(L) or simulate(a.cls, alloc, L, a.spec, a.fights, a.seed, a.mob_level)
        ev = ev_scores(a.cls, a.spec, L, alloc)
        rows = []
        print(f"-- talent values at level {L} (time per kill without the talent vs with; EV = scorer's value of the same removal)")
        for name, ranks in sorted(alloc.items()):
            trial = {k: v for k, v in alloc.items() if k != name}
            rr = simulate(a.cls, trial, L, a.spec, a.fights, a.seed, a.mob_level)
            d = (rr["time_per_kill"] - base["time_per_kill"]) / base["time_per_kill"]
            dm, se = paired_delta(base["fight_times"], rr["fight_times"])
            se_rel = se / base["fight_mean"] if base["fight_mean"] else 0.0
            evv = ev["removals"].get(name) if ev else None
            rows.append({"talent": name, "ranks": ranks, "sim_delta": d, "sim_delta_per_point": d / ranks, "fight_se": se_rel,
                         "ev_delta": evv, "sim_fight_delta": dm / base["fight_mean"] if base["fight_mean"] else 0.0,
                         "deaths_with": base["deaths_per_100"], "deaths_without": rr["deaths_per_100"]})
            print(f"   {name:<24} {ranks}  sim {fmt_pct(d):>7} (fight {fmt_pct(rows[-1]['sim_fight_delta']):>7} +-{se_rel * 100:.1f})  EV {fmt_pct(evv) if evv is not None else 'n/a':>7}")
        results["deltas"][L] = {"rows": rows, "ev_base": ev["base"] if ev else None}
    print(f"done in {time.time() - t0:.0f}s")
    if a.write:
        write_report(results, a.name)


def write_report(res, name=None):
    cls, spec = res["class"], res["spec"]
    out_dir = paths.fightlab_dir(cls)
    out_dir.mkdir(parents=True, exist_ok=True)
    slim = json.loads(json.dumps(res, default=str))
    for L, r in slim["levels"].items():
        r.pop("fight_times", None); r.pop("logs", None)
    for b in slim["compare"].values():
        for r in b.values():
            r.pop("fight_times", None); r.pop("logs", None)
    slim["mob_stats"] = {str(L): {"health": tables.mob_health(int(L) + res["mob_level_offset"]), "dmg": tables.mob_melee_damage(int(L) + res["mob_level_offset"]),
                                  "armor": tables.mob_armor(int(L) + res["mob_level_offset"])} for L in slim["levels"]}
    name = name or spec
    (out_dir / f"{name}.json").write_text(json.dumps(slim, indent=1), encoding="utf-8")
    specs = json.load(open(ROOT / "_reference/data/scorer/specs" / f"{cls}.json", encoding="utf-8"))["models"].get(spec, {})
    model_shares = {s["id"]: s["share"] for s in specs.get("sources", [])}
    cm = class_module(cls)
    modcls = getattr(cm, MODULES[cls][1])
    resource = getattr(modcls, "resource", "mana")
    special = getattr(modcls, "special_stat", None)
    o = [f"# Fight lab — {cls} {spec} ({res['build']})", "",
         f"> Generated by `_reference/data/fightlab/run.py` (Monte Carlo fight simulator; {res['fights']} fights per configuration, seed {res['seed']}, "
         f"mobs at player level {res['mob_level_offset']:+d}, gear tier `{res.get('gear', 'greens')}`). Spell numbers: beta client {DATA_BUILD} (`_reference/data/forever-spells/{cls}.json`); "
         "talent numbers: the beta tooltips; mob health, damage, armor and the caster share by level: the Classic 1.12 creature database "
         "(`_reference/data/fightlab/mob_stats.json`, unverified for Forever); everything else (gear, Classic combat formulas, drink rates) is an "
         "assumption listed in `_reference/data/fightlab/tables.py`. Do not hand-edit.", ""]
    o += ["## What was simulated", "", cm.DESCRIPTION, ""]
    levels = sorted(res["levels"], key=int)
    if any(r.get("mobs_per_pull", 1) > 1.05 for r in res["levels"].values()):
        o += [f"Pulls of {max(r.get('mobs_per_pull', 1) for r in res['levels'].values()):.1f} mobs on average (`MOBS_PER_PULL`): a kill is one mob, a fight is the whole pull.", ""]
    o += ["## Results by level", "",
          f"| Level | Talents | Fight mean | median | p90 | Downtime/kill | Deaths/100 kills | Time/kill | Kills/hour | {resource.title()}/kill | Pushbacks/kill |" + (f" {special[0]} |" if special else ""),
          "|---|---|---|---|---|---|---|---|---|---|---|" + ("---|" if special else "")]
    for L in levels:
        r = res["levels"][L]
        pts = sum(r["allocation"].values())
        o.append(f"| {L} | {pts} | {r['fight_mean']:.1f}s | {r['fight_median']:.1f}s | {r['fight_p90']:.1f}s | {r['downtime_per_kill']:.1f}s | {r['deaths_per_100']:.1f} | "
                 f"{r['time_per_kill']:.1f}s | {r['kills_per_hour']:.0f} | {r['mana_per_kill']:.0f} | {r['pushbacks_per_kill']:.2f} |" + (f" {r[special[1]] * 100:.0f}% |" if special else ""))
    o.append("")
    o += ["## Measured damage shares (vs. the spec model's assumed shares)", ""]
    header = "| Level | " + " | ".join(sorted({k for L in levels for k in res["levels"][L]["shares"]})) + " |"
    keys = sorted({k for L in levels for k in res["levels"][L]["shares"]})
    o.append(header)
    o.append("|---|" + "---|" * len(keys))
    for L in levels:
        sh = res["levels"][L]["shares"]
        o.append(f"| {L} | " + " | ".join(f"{sh.get(k, 0) * 100:.0f}%" for k in keys) + " |")
    o.append("")
    if model_shares:
        o.append("Spec model (`_reference/data/scorer/specs`) assumes: " + ", ".join(f"{k} {v * 100:.0f}%" for k, v in model_shares.items()) + ".")
        o.append("")
    o += ["## Realized crit rates and player at each level", ""]
    for L in levels:
        r = res["levels"][L]
        cr = ", ".join(f"{k} {v * 100:.0f}%" for k, v in r["crit_rate"].items())
        pl = r["player"]
        melee = f"{pl.get('strength', 0):.0f} Str, {pl.get('agility', 0):.0f} Agi, {pl.get('attack_power', 0):.0f} AP, melee crit {pl.get('melee_crit', 0) * 100:.1f}%, " if pl.get('attack_power', 0) > 0 else ""
        o.append(f"- **Level {L}**: {pl.get('hp_max', 0):.0f} health, {pl.get('mana_max', 0):.0f} mana, {pl.get('intellect', 0):.0f} Int, {pl.get('spirit', 0):.0f} Spirit, {melee}"
                 f"{pl.get('spell_power', 0):.0f} spell power, base spell crit {pl.get('spell_crit', 0) * 100:.1f}%, armor {pl.get('armor', 0):.0f} ({r['armor_spell']}); "
                 f"mob {tables.mob_health(L + res['mob_level_offset']):.0f} health, hits for {tables.mob_melee_damage(L + res['mob_level_offset']):.0f}, "
                 f"casters {r.get('caster_share', 0) * 100:.0f}% of pulls ({r.get('interrupts_per_kill', 0):.2f} interrupts per kill). Crit rates: {cr}. "
                 f"Health after a fight {r['hp_after_mean'] * 100:.0f}%, mana {r['mana_after_mean'] * 100:.0f}%." +
                 (f" Not simulated: {', '.join(r['not_simulated'])}." if r["not_simulated"] else ""))
    o.append("")
    if res["compare"]:
        o += ["## Other builds (same mobs, same seeds)", "", "| Level | Build | Time/kill | vs. main | Fight mean | Deaths/100 | Downtime/kill |", "|---|---|---|---|---|---|---|"]
        for L in levels:
            r = res["levels"][L]
            o.append(f"| {L} | {res['build']} | {r['time_per_kill']:.1f}s | - | {r['fight_mean']:.1f}s | {r['deaths_per_100']:.1f} | {r['downtime_per_kill']:.1f}s |")
            for bid, per in res["compare"].items():
                rr = per.get(L) or per.get(str(L))
                if rr:
                    d = (rr["time_per_kill"] - r["time_per_kill"]) / r["time_per_kill"]
                    tag = f" (played as `{rr['spec']}`)" if rr.get("spec") and rr["spec"] != spec else ""
                    o.append(f"| {L} | {bid}{tag} | {rr['time_per_kill']:.1f}s | {fmt_pct(d)} | {rr['fight_mean']:.1f}s | {rr['deaths_per_100']:.1f} | {rr['downtime_per_kill']:.1f}s |")
        o.append("")
    if res.get("gear_tiers"):
        o += ["## Gear tiers (main build)", "",
              "`greens` = the fixed-stat green items (mostly quest rewards) and `blues` = the blue items of the Classic 1.12 item database, every slot the class's "
              "typical good pick 2-7 levels below the character (`_reference/data/fightlab/gear_stats.json`; Classic data, unverified for Forever).", "",
              "| Level | Gear | Time/kill | vs. greens | Fight mean | Deaths/100 | Downtime/kill | Kills/hour |", "|---|---|---|---|---|---|---|---|"]
        for L in levels:
            r = res["levels"][L]
            o.append(f"| {L} | {res.get('gear', 'greens')} | {r['time_per_kill']:.1f}s | - | {r['fight_mean']:.1f}s | {r['deaths_per_100']:.1f} | {r['downtime_per_kill']:.1f}s | {r['kills_per_hour']:.0f} |")
            for tier, per in res["gear_tiers"].items():
                rr = per.get(L) or per.get(str(L))
                if rr:
                    d = (rr["time_per_kill"] - r["time_per_kill"]) / r["time_per_kill"]
                    o.append(f"| {L} | {tier} | {rr['time_per_kill']:.1f}s | {fmt_pct(d)} | {rr['fight_mean']:.1f}s | {rr['deaths_per_100']:.1f} | {rr['downtime_per_kill']:.1f}s | {rr['kills_per_hour']:.0f} |")
        o.append("")
    for L, d in sorted(res["deltas"].items(), key=lambda kv: int(kv[0])):
        o += [f"## Talent values at level {L}", "",
              "Sim: how much longer each kill takes (fight + downtime + deaths) when the talent is removed from the build, so positive = the talent helps; "
              "'fight' is the same for fight time alone with its standard error (paired by mob). EV: the expected-value scorer's value of the same removal "
              "converted to the same scale (its scores are relative to a talentless character), the number the optimizer builds are ranked by.", "",
              "| Talent | Ranks | Sim time/kill | Sim fight time | per point | EV scorer | Deaths/100 without |", "|---|---|---|---|---|---|---|"]
        for row in sorted(d["rows"], key=lambda x: -x["sim_delta"]):
            o.append(f"| {row['talent']} | {row['ranks']} | {fmt_pct(row['sim_delta'])} | {fmt_pct(row['sim_fight_delta'])} ± {row['fight_se'] * 100:.1f} | {fmt_pct(row['sim_delta_per_point'])} | "
                     f"{fmt_pct(row['ev_delta']) if row['ev_delta'] is not None else 'n/a'} | {row['deaths_without']:.1f} |")
        o.append("")
    o += ["## Assumptions (edit `tables.py` to change them)", "",
          f"- Mob health {tables.mob_health.__doc__.strip()}", f"- Mob melee {tables.mob_melee_damage.__doc__.strip()}",
          f"- Caster mobs: {'the creature database share by level (' + tables.mob_caster_share.__doc__.strip() + ')' if tables.MOB_CASTER_SHARE is None else f'{tables.MOB_CASTER_SHARE * 100:.0f}% of pulls'}; "
          f"a caster stands at up to {tables.MOB_CAST_RANGE:.0f} yd and casts a bolt every {tables.MOB_CAST_TIME + tables.MOB_CAST_GAP:.1f} s for {tables.MOB_CAST_DMG_MULT:.1f}x its melee swing "
          f"(spell damage, no armor) until interrupted or stunned, then runs in and melees until the lockout ends; {tables.mob_caster_health.__doc__.strip()}",
          f"- Runners: {tables.RUNNER_SHARE * 100:.0f}% of pulls flee at {tables.RUNNER_HP * 100:.0f}% health for {tables.RUNNER_TIME:.0f} s (roots and stuns hold them; `RUNNER_SHARE`, 0 = not simulated, see sensitivity.md).",
          f"- Spell miss: {tables.spell_miss.__doc__.strip()} Partial resists cost {tables.PARTIAL_RESIST_LOSS * 100:.1f}% on average.",
          f"- Spell crit: {tables.SPELL_CRIT_BASE * 100:.2f}% base plus Intellect / ({tables.int_per_spell_crit.__doc__.strip()})",
          f"- Pushback: {tables.PUSHBACK_FIRST}s for the first melee hit taken during a cast, {tables.PUSHBACK_NEXT}s per further hit; a direct hit breaks a freeze with {tables.ROOT_BREAK_CHANCE * 100:.0f}% chance.",
          f"- Gear: {tables.gear_stats.__doc__.strip()} Wand: {tables.wand_dps.__doc__.strip()}",
          f"- Regen: {tables.mana_regen_tick.__doc__.strip()} Drinking: {tables.drink_rate.__doc__.strip()}",
          f"- Between fights: loot {tables.LOOT_TIME:.0f}s, travel {tables.TRAVEL_TIME:.0f}s, drink below {tables.DRINK_BELOW * 100:.0f}% mana, eat below {tables.EAT_BELOW * 100:.0f}% health, a death costs {tables.DEATH_TIME:.0f}s.",
          "- Not modelled yet: " + cm.NOT_MODELLED, ""]
    (out_dir / f"{name}.md").write_text("\n".join(o) + "\n", encoding="utf-8")
    print(f"wrote {out_dir / f'{name}.md'}")


if __name__ == "__main__":
    main()
