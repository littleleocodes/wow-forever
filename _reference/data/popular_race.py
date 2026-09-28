"""Race talentsforever.com's most popular builds (popular-builds.json, from popular_builds.py) against ours (2026-09-28, user request).

    python _reference/data/popular_race.py [classes] [--parts raid,heal,level] [--iterations 20000] [--fights 2000] [--runs 60]
    python _reference/data/popular_race.py --report        # only re-render _reference/popular-builds.md from the saved results

Three races, each in the tool that ranks that scenario in this project:

- raid: the community simulator (raidsim/run.py's run_spec, the pinned ElliotWood/Forever commit), every raid entry of the class in
  specs.json (our tuned rotation for the setting, the entry's gear and consumables), once on the boss-level training dummy with your
  own buffs and once in the raid setting (full buffs). Every popular build of the class runs in every DPS entry next to that entry's
  builds of ours and the simulator's presets; a build's number is its best entry (the rotation that suits it best). Tank entries
  (warrior and paladin Protection, the druid's Bear) take the popular builds that lead in that tree, raid setting, tank value.
- heal: the healer lab (heallab/, capacity) for the popular builds that lead in a healing tree, next to our hand and optimizer healers.
- level: the fight lab at levels 20-60. A popular build is a level-60 plan with no leveling order, so it gets one from the scorer
  (Optimizer.order with the leveling-st profile of the spec model it is played as: the same order search our optimizer builds use)
  and runs under every leveling spec model the class has in the fight lab; its number is its best model. Ours: the hand leveling
  draft (main spec) and each model's optimizer build. Compared on level-weighted time per kill (weight level / 10, as rebuild.py).

Each part runs in its own process (the three labs have modules of the same names). Results: `_reference/data/popular-race.json`;
report: `_reference/popular-builds.md` (generated).
"""
import argparse
import datetime
import json
import pathlib
import subprocess
import sys
import tempfile

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[1]
POP = HERE / "popular-builds.json"
OUT = HERE / "popular-race.json"
REPORT = ROOT / "_reference/popular-builds.md"
CLASSES = ["druid", "hunter", "mage", "paladin", "priest", "rogue", "shaman", "warlock", "warrior"]
TANK_LEAD = {"warrior": {"prot-tank": "Protection"}, "paladin": {"prot-tank": "Protection"}, "druid": {"feral-bear-tank": "Feral Combat"}}
HEAL_LEAD = {"priest": ("Discipline", "Holy"), "paladin": ("Holy",), "shaman": ("Restoration",), "druid": ("Restoration",)}
LEVELS = [20, 30, 40, 50, 60]
LOOKAHEAD = {"mage": 12, "warrior": 20}   # the fight lab pipeline's order lookahead (16 otherwise)


def weighted_mean(per_level):
    """Level-weighted mean of {level: time per kill}: weight = level / 10, as rebuild.py's races."""
    tot = sum(int(L) / 10 for L in per_level)
    return sum(v * int(L) / 10 for L, v in per_level.items()) / tot if tot else 0.0


def popular(cls):
    return json.load(open(POP, encoding="utf-8"))["classes"][cls]["top"]


def build_files(cls, folder):
    """Each popular build as a candidate file ({id, allocation}), the form run.py and the labs load."""
    out = []
    for p in popular(cls):
        f = pathlib.Path(folder) / f"{p['id']}.json"
        f.write_text(json.dumps({"id": p["id"], "allocation": p["allocation"]}), encoding="utf-8")
        out.append((p, str(f)))
    return out


# ---------------------------------------------------------------- parts (each in its own process)

def part_raid(cls, a, tmp):
    sys.path.insert(0, str(HERE / "raidsim"))
    import run   # raidsim/run.py
    repo = run.repo_path(argparse.Namespace(repo=None))
    files = build_files(cls, tmp)
    rows = []
    for name, entry in run.SPECS[cls].items():
        if name.startswith("_") or not isinstance(entry, dict) or "apl" not in entry:
            continue
        tank = bool(entry.get("tank"))
        pops = [f for p, f in files if not tank or p["lead"] == TANK_LEAD.get(cls, {}).get(name)]
        if not pops:
            continue
        for setting in (["raid"] if tank else ["dummy", "raid"]):
            run.SETTING_OVERRIDE = setting
            ns = argparse.Namespace(builds=list(entry["builds"]) + pops, iterations=a.iterations, duration=120.0, seed=1, no_presets=False,
                                    deltas=None, write=False)
            out = run.run_spec(cls, name, ns, repo)
            for x in out["results"]:
                kind = "popular" if x["label"].startswith("tf-popular-") else ("ours" if x["ours"] else "preset")
                rows.append({"entry": name, "tank": tank, "rotation_only": bool(entry.get("rotation_only")), "setting": setting, "label": x["label"],
                             "kind": kind, "split": x["split"], "dps": x["dps"], "value": x.get("value"), "threat": x.get("threat"), "dtps": x.get("dtps"),
                             "oom": x.get("oom_seconds"), "error": x.get("error"), "apl": out["sim"]["apl"]})
            commit = out["sim"]["commit"]
    return {"commit": commit, "iterations": a.iterations, "rows": rows}


def part_heal(cls, a, tmp):
    if cls not in HEAL_LEAD:
        return None
    sys.path.insert(0, str(HERE / "heallab"))
    import importlib
    import run   # heallab/run.py
    import tables as T
    files = [(p, f) for p, f in build_files(cls, tmp) if p["lead"] in HEAL_LEAD[cls]]
    if not files:
        return None
    T.apply_rotation(cls)
    mod = importlib.import_module(run.CLASSES[cls])
    pipe = mod.PIPELINE
    ids = [pipe["hand"], pipe["opt"]] + [f for _, f in files]
    rows = []
    for bid in ids:
        b = run.load_build(cls, bid)
        _, cap, summ = run.measure(mod, run.alloc_of(b), list(range(a.runs)), 10)
        rows.append({"label": b["id"], "kind": "popular" if b["id"].startswith("tf-popular-") else "ours", "split": run.split_of(b), "capacity": cap,
                     "hps": summ["hps"], "oom": summ["oom_time"]})
        print(f"  {b['id']:<36} {rows[-1]['split']:>8}  capacity {cap:.3f}")
    return {"spec": pipe["spec"], "runs": a.runs, "rows": rows}


def part_level(cls, a, tmp):
    sys.path.insert(0, str(HERE / "fightlab"))
    import run   # fightlab/run.py (puts scorer/ on the path)
    from optimize import Optimizer
    mod = __import__(run.MODULES[cls][0])
    pipe = mod.PIPELINE
    models_known = json.load(open(HERE / "scorer/specs" / f"{cls}.json", encoding="utf-8"))["models"]
    # every single-target leveling model the class's fight lab plays: the main one, the extra reports, the leveling-st variants
    models = [pipe["spec"]] + [x["spec"] for x in pipe.get("extra_reports", [])] + [v["spec"] for v in pipe.get("variants", []) if v.get("profile") == "leveling-st"]
    models = [m for i, m in enumerate(models) if m in models_known and m not in models[:i] and "frostfire" not in m]
    data = json.load(open(ROOT / cls / "talents/forever/proposed-builds.json", encoding="utf-8"))
    by_id = {b["id"]: b for b in data["builds"]}
    ours = [(pipe["hand"], pipe["spec"])] + [(f"opt-{m}-leveling-st", m) for m in models if f"opt-{m}-leveling-st" in by_id]
    ours += [(x["build"], x["spec"]) for x in pipe.get("extra_reports", []) if x["build"] in by_id and x["spec"] in models and (x["build"], x["spec"]) not in ours]
    look = LOOKAHEAD.get(cls, 16)

    def race(b, spec):
        per = {}
        for L in LEVELS:
            r = run.simulate(cls, run.allocation_at(b, L), L, spec, a.fights, 1, 0)
            per[L] = {"tpk": r["time_per_kill"], "deaths": r["deaths_per_100"], "fight": r["fight_mean"]}
        return per

    rows = []
    for bid, spec in ours:
        per = race(by_id[bid], spec)
        rows.append({"label": bid, "kind": "ours", "spec": spec, "levels": per, "weighted": weighted_mean({L: v["tpk"] for L, v in per.items()})})
        print(f"  {bid:<40} as {spec:<22} {rows[-1]['weighted']:.2f}s per kill (level-weighted)")
    for p in popular(cls):
        target = {n: r for items in p["allocation"].values() for n, r in items}
        for spec in models:
            opt = Optimizer("forever", cls, spec, "leveling-st")
            steps = opt.order(target, lookahead=look)
            order = [{"levels": lv, "tree": t, "talent": n, "points": pts} for lv, t, n, pts in opt.compress_order(steps)]
            b = {"id": p["id"], "allocation": p["allocation"], "order": order}
            per = race(b, spec)
            rows.append({"label": p["id"], "kind": "popular", "spec": spec, "order_label": getattr(opt, "order_label", ""), "levels": per,
                         "weighted": weighted_mean({L: v["tpk"] for L, v in per.items()}), "order": order})
            print(f"  {p['id']:<40} as {spec:<22} {rows[-1]['weighted']:.2f}s per kill (level-weighted, order: {rows[-1]['order_label']})")
    return {"models": models, "fights": a.fights, "levels": LEVELS, "rows": rows}


PARTS = {"raid": part_raid, "heal": part_heal, "level": part_level}


# ---------------------------------------------------------------- report

def pct(x):
    return f"{x * 100:+.1f}%"


def flat(alloc):
    return {n: r for items in alloc.values() for n, r in items if r}


def best_by_label(rows, setting=None, key="dps"):
    """{label: (value, entry)} over the entries: each build's best entry (the rotation that suits it best)."""
    out = {}
    for r in rows:
        if (setting and r["setting"] != setting) or r["tank"] or not r.get(key):
            continue
        if r["label"] not in out or r[key] > out[r["label"]][0]:
            out[r["label"]] = (r[key], r["entry"], r["kind"], r["split"])
    return out


def render(res):
    pop = json.load(open(POP, encoding="utf-8"))
    commit = next((v["raid"]["commit"] for v in res["classes"].values() if v.get("raid")), "?")
    o = ["# Popular builds on talentsforever.com vs ours", "",
         f"> Generated by `_reference/data/popular_race.py` on {res['date']} from `_reference/data/popular-builds.json` (decoded by `popular_builds.py` from "
         f"talentsforever.com's own popularity list, `{pop['raw']}`). Raid numbers: the community's ElliotWood/Forever simulator at {commit} "
         "(simulations of the community's model of the beta, not measurements); leveling: our fight lab; healers: our healer lab (models of stated "
         "assumptions). Do not hand-edit.", "",
         "## What talentsforever.com shows", "",
         "The site publishes a **Popular builds** list per class (the fold under the talent trees on each class page), and it is readable: the page "
         "loads it from a static script, `https://talentsforever.com/popular.js` (`window.POPULAR`), no browser needed. Per class it holds the top 5 "
         "level-60 builds people made, shared, saved or opened on the site, ranked by a score of shares, saves and opens (\"builds within a few points of "
         "each other count as one\"), with the counts, the share of each tree as the lead, and per-talent pick rates. It is what people *planned* on a "
         "talent calculator during the level-20 beta, not what anyone played at 60, and it has no scenario tag: a raid, a leveling and a PvP plan all "
         "count the same. Paladin, shaman and druid count only builds made since the 70009 patch (2026-09-24); the other six count everything since "
         "2026-09-13, earlier codes translated by talent name.", ""]
    # ---- headline
    o += ["## Headline: the most popular build of each class", "",
          "Dummy and raid: the build's best raid DPS entry (its best rotation) against the best of our builds in any entry, same setting. Leveling: "
          "level-weighted time per kill at levels 20-60 against our best leveling build (lower is better, so a positive % means the popular build is "
          "slower). Healer and tank builds are compared in their own labs below.", "",
          "| Class | #1 popular | Split | Dummy DPS | vs our best | Raid DPS | vs our best | Leveling s/kill | vs our best |", "|---|---|---|---|---|---|---|---|---|"]
    for cls in CLASSES:
        c = res["classes"].get(cls)
        if not c:
            continue
        p1 = pop["classes"][cls]["top"][0]
        cells = [cls, f"[{p1['lead']}]({p1['url']})", p1["split"]]
        for s in ("dummy", "raid"):
            rows = (c.get("raid") or {}).get("rows", [])
            bb = best_by_label(rows, s)
            ours = max((v for v in bb.values() if v[2] == "ours"), default=None)
            mine = bb.get(p1["id"])
            cells += [f"{mine[0]:.0f}" if mine else "-", pct(mine[0] / ours[0] - 1) if mine and ours else "-"]
        lv = (c.get("level") or {}).get("rows", [])
        pl = min((r["weighted"] for r in lv if r["label"] == p1["id"]), default=None)
        ol = min((r["weighted"] for r in lv if r["kind"] == "ours"), default=None)
        cells += [f"{pl:.1f}" if pl else "-", pct(pl / ol - 1) if pl and ol else "-"]
        o.append("| " + " | ".join(cells) + " |")
    o.append("")
    # ---- per class
    for cls in CLASSES:
        c = res["classes"].get(cls)
        if not c:
            continue
        pc = pop["classes"][cls]
        o += [f"## {cls.capitalize()}", "",
              f"Popularity window: {pc['window']}; {pc['builds_counted']:,} builds counted, {pc['full_builds']:,} with all 51 points; lead tree shares "
              + ", ".join(f"{k} {v}%" for k, v in pc["spec_share"].items()) + ".", ""]
        rows = (c.get("raid") or {}).get("rows", [])
        bd, br = best_by_label(rows, "dummy"), best_by_label(rows, "raid")
        our_d = max((v for v in bd.values() if v[2] == "ours"), default=None)
        our_r = max((v for v in br.values() if v[2] == "ours"), default=None)
        our_d_lab = next((k for k, v in bd.items() if v is our_d), "-")
        our_r_lab = next((k for k, v in br.items() if v is our_r), "-")
        lv = (c.get("level") or {}).get("rows", [])
        best_l = {}
        for r in lv:
            if r["label"] not in best_l or r["weighted"] < best_l[r["label"]]["weighted"]:
                best_l[r["label"]] = r
        our_l = min((r for r in best_l.values() if r["kind"] == "ours"), key=lambda r: r["weighted"], default=None)
        def ours_in(setting, entry):   # our best build in the same entry and setting: same rotation, talents alone differ
            return max((r["dps"] for r in rows if r["setting"] == setting and r["entry"] == entry and r["kind"] == "ours" and r["dps"]), default=None)

        def ours_as(spec):             # our best leveling build played as the same spec model
            return min((r["weighted"] for r in lv if r["kind"] == "ours" and r["spec"] == spec), default=None)

        def cmp(v, ref):
            return pct(v / ref - 1) if v and ref else "-"
        o += ["Each popular build in its best entry (rotation); *vs best* = against our best build of the class in any entry, *vs same* = against our best "
              "build in that same entry (same rotation and gear: the talents alone differ). Leveling is time per kill, so + means slower.", "",
              "| # | Lead | Split | Popularity (shared / saved / opened) | Dummy DPS (entry) | vs best | vs same | Raid DPS (entry) | vs best | vs same | Leveling s/kill (played as) | vs best | vs same |",
              "|---|---|---|---|---|---|---|---|---|---|---|---|---|"]
        mine = json.load(open(ROOT / cls / "talents/forever/proposed-builds.json", encoding="utf-8"))["builds"]
        for p in pc["top"]:
            d, r_, l_ = bd.get(p["id"]), br.get(p["id"]), best_l.get(p["id"])
            short = "" if p["valid"] else f" ({sum(int(x) for x in p['split'].split('/'))} pts)"
            same = [b["id"] for b in mine if flat(b["allocation"]) == flat(p["allocation"])]
            short += f" (= `{same[0]}`)" if same else ""
            o.append(f"| {p['rank']} | [{p['lead']}]({p['url']}) | {p['split']}{short} | {p['shared']} / {p['saved']} / {p['opened']} | "
                     + (f"{d[0]:.0f} (`{d[1]}`) | {cmp(d[0], our_d and our_d[0])} | {cmp(d[0], ours_in('dummy', d[1]))}" if d else "- | - | -") + " | "
                     + (f"{r_[0]:.0f} (`{r_[1]}`) | {cmp(r_[0], our_r and our_r[0])} | {cmp(r_[0], ours_in('raid', r_[1]))}" if r_ else "- | - | -") + " | "
                     + (f"{l_['weighted']:.1f} (`{l_['spec']}`) | {cmp(l_['weighted'], our_l and our_l['weighted'])} | {cmp(l_['weighted'], ours_as(l_['spec']))}" if l_ else "- | - | -") + " |")
        o += ["", f"Ours: dummy `{our_d_lab}` {our_d[0]:.0f} ({our_d[3]}, `{our_d[1]}`), raid `{our_r_lab}` {our_r[0]:.0f} ({our_r[3]}, `{our_r[1]}`)" if our_d and our_r else "Ours: -"]
        if our_l:
            o[-1] += f", leveling `{our_l['label']}` {our_l['weighted']:.1f} s per kill (as `{our_l['spec']}`)."
        # tanks
        trows = [r for r in rows if r["tank"]]
        if trows:
            o += ["", "Tanks (raid setting, tank value = the raid-tank profile's threat and mitigation weights relative to our hand tank draft; higher is better):", "",
                  "| Build | Split | Tank value | Threat/s | Damage taken/s |", "|---|---|---|---|---|"]
            for r in sorted(trows, key=lambda r: -(r["value"] or 0)):
                if r["kind"] == "preset" and not r["value"]:
                    continue
                o.append(f"| {'`' + r['label'] + '`' if r['kind'] != 'preset' else r['label']}{' (popular)' if r['kind'] == 'popular' else ''} | {r['split'] or '-'} | "
                         f"{(r['value'] or 0):.3f} | {(r['threat'] or 0):.0f} | {(r['dtps'] or 0):.0f} |")
        h = c.get("heal")
        if h:
            o += ["", f"Healers (healer lab, `{h['spec']}` settings, capacity = the incoming-damage multiplier survived in 90% of {h['runs']} runs; higher is better):", "",
                  "| Build | Split | Capacity | HPS | OOM s |", "|---|---|---|---|---|"]
            for r in sorted(h["rows"], key=lambda r: -r["capacity"]):
                o.append(f"| `{r['label']}`{' (popular)' if r['kind'] == 'popular' else ''} | {r['split']} | {r['capacity']:.3f} | {r['hps']:.0f} | {r['oom']:.0f} |")
        o.append("")
    o += ["## How to read this", "",
          "- Every popular build ran in every raid DPS entry of its class (Holy and Protection builds too); the table shows its best entry, so a "
          "Fire build is played by the Fire rotation. Our tuned rotations were searched on our builds and the simulator's presets, not on these: a "
          "popular build that needs a different priority is at a small disadvantage.",
          "- Builds the site shows with fewer than 51 points (its row is a cluster of near-identical builds and the representative can be short) were "
          "raced as published; the split column gives their point count.",
          "- Leveling orders for the popular builds are the scorer's (the same order search our optimizer builds get); people who planned these builds "
          "for level 60 may level differently. Most popular builds are raid or PvP plans, so a leveling gap is expected, not a flaw.",
          "- \"(= `id`)\" marks a popular build identical to one of ours. Builds that differ only in talents the simulator does not model "
          "(e.g. the Survival hunters' Survival Tactics, Clever Traps, Survivalist's Discipline under the melee rotation) read the same DPS: a tie, "
          "not a result.",
          "- Popularity is what visitors of a talent calculator planned during a level-20 beta. It says nothing about what performs.", ""]
    REPORT.write_text("\n".join(o) + "\n", encoding="utf-8")
    print(f"wrote {REPORT.relative_to(ROOT)}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("classes", nargs="*")
    ap.add_argument("--parts", default="raid,heal,level")
    ap.add_argument("--iterations", type=int, default=20000)
    ap.add_argument("--fights", type=int, default=2000)
    ap.add_argument("--runs", type=int, default=60)
    ap.add_argument("--report", action="store_true")
    ap.add_argument("--part", help=argparse.SUPPRESS)       # internal: run one part for one class, JSON to --json
    ap.add_argument("--json", help=argparse.SUPPRESS)
    a = ap.parse_args()
    if a.part:
        with tempfile.TemporaryDirectory() as tmp:
            r = PARTS[a.part](a.classes[0], a, tmp)
        pathlib.Path(a.json).write_text(json.dumps(r), encoding="utf-8")
        return
    res = json.load(open(OUT, encoding="utf-8")) if OUT.exists() else {"classes": {}}
    if not a.report:
        for cls in a.classes or CLASSES:
            for part in a.parts.split(","):
                with tempfile.TemporaryDirectory() as tmp:
                    j = pathlib.Path(tmp) / "out.json"
                    print(f"== {cls} {part}", flush=True)
                    subprocess.run([sys.executable, __file__, cls, "--part", part, "--json", str(j), "--iterations", str(a.iterations),
                                    "--fights", str(a.fights), "--runs", str(a.runs)], check=True)
                    res["classes"].setdefault(cls, {})[part] = json.loads(j.read_text(encoding="utf-8"))
                res["date"] = datetime.date.today().isoformat()
                OUT.write_text(json.dumps(res, indent=1) + "\n", encoding="utf-8")
    render(res)


if __name__ == "__main__":
    main()
