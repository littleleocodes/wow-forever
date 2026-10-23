"""Signature-spell audit of the leveling pages (user rule 2026-10-22: "make sure that the specs we're testing are actually using the spells
for that spec, or else it's pointless"; strictness "main damage": signature_spells.json, read by signature.py / fl_signature.py).

    python _reference/data/fightlab/signature_audit.py [classes] [--fights 300] [--jobs 3] [--write] [--no-default]

For every leveling spec and hybrid on the player pages, every leveling build of its slot (render_modes' grid after own_rotation_only)
in the rotation the page shows it with (render_modes.LEVEL_MODEL): whether that rotation's tuned rules (fightlab/rotations/<class>-
<rotation>.json) switch off or gate a required spell, and a fight-lab run (greens, seed 4, `--fights` per level, levels 20-60) with
casts per kill of every required spell from the level it is learned and the core sources' share of the damage at level 60 against
min_share. A hybrid whose page rotation is not its spec_modes.HYBRID_LEVELING_ROTATION is also run in that one ("mapped"); a failing
page pick once more with the hand-written rotation ("default", no tuned rules) unless --no-default, which tells a rule problem from a
rotation or build problem. --write: `_reference/signature-audit.md` and `fightlab/signature-audit.json`, which render_modes reads (a
build's check counts while its fingerprint, fl_signature.build_fingerprint: allocation, order, rotation and rules, still matches).
rebuild.py's regen step runs it with --write --no-default before render_modes.
"""
import argparse
import datetime
import json
import multiprocessing
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
DATA = HERE.parent
ROOT = HERE.parents[2]
sys.path[:0] = [str(HERE), str(DATA), str(DATA / "scorer")]
import run as FR  # noqa: E402
import signature as SG  # noqa: E402
import fl_signature as FS  # noqa: E402
import spec_modes as SM  # noqa: E402

OUT_MD = ROOT / "_reference" / "signature-audit.md"
OUT_JSON = HERE / "signature-audit.json"


def _init():
    FR.apply_gear("greens")


def _job(job):
    cls, rot, alloc, level, fights, seed, rules = job
    r = FR.simulate(cls, alloc, level, rot, fights, seed, 0, rot=({} if rules == "default" else None))
    return {k: r.get(k) for k in ("time_per_kill", "kills", "shares", "casts", "pet_sources")}


def rules_issues(cls, rot, required):
    """The tuned rules of `rot` that switch off or gate a required spell."""
    p = FR.rotation_file(cls, rot)
    if not p.exists():
        return []
    veto = json.load(open(p, encoding="utf-8")).get("veto") or {}
    out = []
    for s in required:
        v = veto.get(s) or {}
        if v.get("off"):
            out.append(f"{s} off")
        if v.get("max_hp"):
            out.append(f"{s} only below {v['max_hp']:.0%} mob health")
        if v.get("min_mana") and v["min_mana"] > 0.15:
            out.append(f"{s} only above {v['min_mana']:.0%} mana")
        if v.get("min_hp") and v["min_hp"] > 0.35:
            out.append(f"{s} only above {v['min_hp']:.0%} mob health")
    return out


def page_slots(cls):
    """[(spec, [builds best first], {build id: page rotation}, level_as)] as the leveling pages see them (before the signature rule)."""
    import render_modes as RM
    import render_rotations as rr
    import render_start_here as rs
    B = rr.builds(cls)
    nums = (RM.raid_numbers(cls), RM.leveling_numbers(cls), RM.healer_numbers(cls))
    before = SM.grid(cls, list(B.values()))
    before = {s: list(m.get("leveling") or []) for s, m in before.items()}
    g = RM.own_rotation_only(cls, SM.grid(cls, list(B.values())), nums)
    specs = SM.trees(cls) + sorted(s for s in g if s.startswith("Hybrid") and (g[s].get("leveling") or before.get(s)))
    out = []
    for spec in specs:
        ranked = RM.rank_builds(cls, "leveling", g.get(spec, {}).get("leveling") or [], nums, signature=False)
        gone = [] if ranked else RM.rank_builds(cls, "leveling", before.get(spec) or [], nums, signature=False)[:1]
        rots = {b["id"]: RM.level_rotation(cls, b) for b in ranked + gone}
        out.append((spec, ranked, rots, gone, SM.LEVEL_AS.get((cls, spec))))
    return out


def weighted(per):
    tot = sum(L / 10 for L in per)
    return round(sum(per[L]["time_per_kill"] * L / 10 for L in per) / tot, 2)


def pct(x):
    return "-" if x is None else f"{x:.0%}"


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("classes", nargs="*")
    ap.add_argument("--fights", type=int, default=300)
    ap.add_argument("--jobs", type=int, default=3)
    ap.add_argument("--write", action="store_true")
    ap.add_argument("--no-default", action="store_true", help="skip the hand-written-rotation reruns of failing page picks")
    a = ap.parse_args()
    classes = a.classes or SM.CLASSES
    plan = []   # (cls, spec, build, rotation, rules, kind) kind: page (the pick), slot (another build of the slot), mapped, default
    slots = {}
    for cls in classes:
        slots[cls] = page_slots(cls)
        for spec, ranked, rots, gone, _ in slots[cls]:
            for i, b in enumerate(ranked):
                plan.append((cls, spec, b, rots[b["id"]], "tuned", "page" if i == 0 else "slot"))
            want = SM.HYBRID_LEVELING_ROTATION.get((cls, spec))
            if ranked and want and want != rots[ranked[0]["id"]]:
                plan.append((cls, spec, ranked[0], want, "tuned", "mapped"))
            for b in gone:   # a hybrid whose page build left with the rotation rule (shown with another spec's rotation): where it stood, and
                plan.append((cls, spec, b, rots[b["id"]], "tuned", "was"))   # in its own rotation
                if want and want != rots[b["id"]]:
                    plan.append((cls, spec, b, want, "tuned", "mapped"))
    res = {}

    def run_plan(pl):
        jobs = [(cls, rot, FR.allocation_at(b, L), L, a.fights, FS.CHECK_SEED, rules) for cls, spec, b, rot, rules, _ in pl for L in FS.LEVELS]
        with multiprocessing.Pool(a.jobs, initializer=_init) as pool:
            out = pool.map(_job, jobs, chunksize=1)
        k = 0
        for cls, spec, b, rot, rules, kind in pl:
            res[(cls, spec, b["id"], rot, rules)] = {L: out[k + i] for i, L in enumerate(FS.LEVELS)}
            k += len(FS.LEVELS)

    def verdict(cls, spec, b, per):
        return SG.check_levels(cls, spec, b, per, "leveling") if FS.enabled() else {"ok": True, "rule": None, "missing_talents": [], "uncast": [],
                                                                                   "core_share": None, "min_share": None}
    run_plan(plan)
    again = []
    for cls, spec, b, rot, rules, kind in plan:
        if kind == "page" and not verdict(cls, spec, b, res[(cls, spec, b["id"], rot, rules)])["ok"] and FR.rotation_file(cls, rot).exists() \
                and not a.no_default:
            again.append((cls, spec, b, rot, "default", "default"))
    if again:
        run_plan(again)
    table, builds = {}, {}
    for cls, spec, b, rot, rules, kind in plan + again:
        per = res[(cls, spec, b["id"], rot, rules)]
        v = verdict(cls, spec, b, per)
        rl = v["rule"] or {}
        row = {"spec": spec, "name": SM.spec_name(cls, spec), "build": b["id"], "split": "/".join(str(x) for x in SM.tree_points(cls, b).values()),
               "rotation": rot, "rules": rules, "kind": kind, "required": rl.get("required", []), "core": rl.get("core", []),
               "rule_issues": rules_issues(cls, rot, rl.get("required", [])) if rules == "tuned" else [],
               "casts_60": {s: round(SG.casts_per_kill(per[60], s), 2) for s in rl.get("required", [])},
               "core_share": None if v["core_share"] is None else round(v["core_share"], 4), "min_share": v["min_share"],
               "weighted": weighted(per), "verdict": SG.verdict_text(v), "ok": v["ok"],
               "missing_talents": v["missing_talents"], "uncast": v["uncast"],
               "top_shares": {k: round(x, 3) for k, x in list((per[60].get("shares") or {}).items())[:6]}}
        table.setdefault(cls, []).append(row)
        if kind in ("page", "slot"):
            builds.setdefault(cls, {})[b["id"]] = dict({k: row[k] for k in ("spec", "rotation", "ok", "verdict", "core_share", "min_share", "required",
                                                                            "core", "casts_60", "missing_talents", "uncast")},
                                                       fingerprint=FS.build_fingerprint(cls, b, rot), date=datetime.date.today().isoformat(),
                                                       fights=a.fights)
    for cls in classes:
        for spec, ranked, rots, gone, la in slots[cls]:
            if not ranked and not gone:
                table.setdefault(cls, []).append({"spec": spec, "name": SM.spec_name(cls, spec), "build": None, "level_as": la})
    print_table(table)
    if a.write:
        old = json.load(open(OUT_JSON, encoding="utf-8")) if OUT_JSON.exists() else {}
        st = {"date": datetime.date.today().isoformat(), "fights": a.fights, "levels": list(FS.LEVELS),
              "builds": dict(old.get("builds") or {}), "rows": dict(old.get("rows") or {})}
        for cls in classes:
            st["builds"][cls] = builds.get(cls, {})
            st["rows"][cls] = table.get(cls, [])
        OUT_JSON.write_text(json.dumps(st, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
        write_md(st)
        print(f"wrote {OUT_JSON.relative_to(ROOT)}")


def print_table(table):
    for cls, rs_ in table.items():
        print(f"== {cls}")
        for r in rs_:
            if not r.get("build"):
                print(f"  {r['name']}: no leveling build (levels as {r.get('level_as')})")
                continue
            print(f"  {r['name']} [{r['kind']}: {r['build']} {r['split']}] {r['rotation']} ({r['rules']}): casts/kill at 60 {r['casts_60']}, "
                  f"core {pct(r['core_share'])} (min {pct(r['min_share'])}), {r['weighted']:.1f} s/kill; rules: {', '.join(r['rule_issues']) or '-'}; "
                  f"{r['verdict']}\n      shares at 60: {r['top_shares']}")


def write_md(st):
    o = ["# Signature-spell audit of the leveling pages", "",
         f"Generated by `_reference/data/fightlab/signature_audit.py` on {st['date']} (fight lab, greens, seed {FS.CHECK_SEED}, {st['fights']} "
         "fights per level at levels 20-60). The rule (user, 2026-10-22: \"The specs should use the spells that make that spec, that spec. "
         "Especially the hybrid ones\"; strictness \"main damage\") is `_reference/data/signature_spells.json`: every `required` spell cast from "
         "the level it is learned (at least 0.5 casts per kill, or half what its cooldown allows), never switched off or gated by a tuned rule, "
         "and the `core` sources carrying `min_share` of the damage at level 60.", "",
         "Rows: **page** = the build the leveling page shows (before the rule), in the rotation the page shows it with (tuned rules); "
         "**slot** = the slot's other leveling builds; **mapped** = a hybrid's page build in its `spec_modes.HYBRID_LEVELING_ROTATION` when "
         "the page shows another rotation; **default** = a failing page build once more with the hand-written rotation (no tuned rules); **was** = a hybrid's page build "
         "that left its page with the rule (shown until 2026-10-22 with a rotation that is not the hybrid's own), in that rotation.", ""]
    for cls, rs_ in st["rows"].items():
        o += [f"## {cls.capitalize()}", "", "| Spec | Row | Build | Rotation | Rules on required spells | Required casts per kill at 60 | Core share at 60 | s/kill (20-60) | Verdict |",
              "|---|---|---|---|---|---|---|---|---|"]
        for r in rs_:
            if not r.get("build"):
                o.append(f"| {r['name']} | - | none | levels as {r.get('level_as') or '-'} | | | | | not checked |")
                continue
            casts = ", ".join(f"{s} {n:.2f}" for s, n in r["casts_60"].items()) or "-"
            o.append(f"| {r['name']} | {r['kind']} | {r['build']} ({r['split']}) | {r['rotation']}{' (no rules)' if r['rules'] == 'default' else ''} | "
                     f"{', '.join(r['rule_issues']) or '-'} | {casts} | {pct(r['core_share'])} (min {pct(r['min_share'])}) | {r['weighted']:.1f} | {r['verdict']} |")
        o.append("")
    OUT_MD.write_text("\n".join(o) + "\n", encoding="utf-8")
    print(f"wrote {OUT_MD.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
