"""The open talent searches' winners as builds (2026-10-06; HANDOFF: "write the open winners as builds ... -open-raid / -open-leveling
derived builds with replaces under the replacement bar").

    python _reference/data/open_builds.py [classes] [--write] [--no-tidy] [--partial]

Raid, from `raidsim/families/<class>.json` (family_search.py: every legal 51-point build, no tree rule, per damage rotation, in a full
raid): each done entry's winner (after the rotation re-tune when one happened) is compared with every build of ours of its spec
(spec_modes.spec_of: a tree with 30+ points, else the hybrid of its two largest trees): the builds raced with it in the entry's race
(30,000 fights, common random numbers) and the spec's other raid builds at their full-raid numbers on the pages
(render_modes.raid_numbers: each build's best entry). It becomes `<spec slug>-open-raid` (🔬, `derived: raid`) when GAIN_NEW (0.5%)
ahead of all of them, else the record says which build it confirms; `replaces` names the spec's best hand draft when the winner is
MIN_GAIN (0.5% since 2026-10-07, 2% before) ahead of it (the hand draft stays as the alternative; the pages enforce the bar on race numbers,
render_modes.DERIVED_BAR). One build per spec: the best winner across entries. The build joins its entry's `builds` in specs.json and
goes through filler_audit.py in the full raid (ml_builds.tidy) unless --no-tidy; re-race the entry afterwards (raidsim/run.py --spec
<entry> --write and --env environments --write) for the pages' numbers.
Leveling, from `fightlab/open/<class>.json` (fl_open_search.py): each done rotation's winner (picked by the 20-60 race among the
level-60 finalists, with the stats model's talent order) is compared with our leveling builds in that race (the trees that level with
the rotation) and the spec's other leveling builds at their numbers on the pages (render_modes.leveling_numbers), on level-weighted
seconds per kill; `<spec slug>-open-leveling` (`derived: leveling`, the record's order) under the same bars; one per spec (the fastest
across rotations). The pages take its numbers from the record (render_modes.leveling_numbers reads the rotation's `builds.written`).
Every `-open-raid` / `-open-leveling` build of a class is rewritten from its records on each run (a winner that no longer qualifies
goes); a class whose record has an entry or rotation still running is skipped unless --partial. Records: the `builds` key of each
entry / rotation ({written, why, spec, date}). A new hybrid family needs a player name in spec_modes.HYBRID_NAMES (the pages name
hybrids by it; the slug is the build id's prefix).
"""
import argparse
import datetime
import importlib.util
import json
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[1]
sys.path[:0] = [str(HERE / "scorer"), str(HERE)]
import paths  # noqa: E402
import spec_modes as SM  # noqa: E402
import spec_builds as SB  # noqa: E402
import render_start_here as RSH  # noqa: E402
from filelock import locked  # noqa: E402
from fmt_json import dumps  # noqa: E402

FAMILIES = HERE / "raidsim" / "families"
OPEN = HERE / "fightlab" / "open"
TODAY = datetime.date.today().isoformat()
GAIN_NEW = 0.005    # a winner becomes a build only this far ahead of every build of ours it is compared with (ml_builds.GAIN_NEW)
MIN_GAIN = 0.005    # the replacement bar (hand draft -> derived build): 0.5% since 2026-10-07 (2% before; a rule Claude set, not the user)
CORE_SHARE = 0.02   # raid: a talent worth this share of the build's full-raid DPS is core
CORE_SECONDS = 0.3  # leveling: a talent saving this many seconds per kill at 60 is core
CORE_MAX = 8


def _load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def sim_commit():
    """The pinned simulator commit (raidsim/setup.py GAMES["forever"]["commit"]), short."""
    t = (HERE / "raidsim" / "setup.py").read_text(encoding="utf-8")
    m = re.search(r'"forever":\s*\{.*?"commit":\s*"([0-9a-f]{7})', t, re.S)
    return m.group(1) if m else "?"


def hand(b):
    return not b.get("generated") and not b["id"].startswith("opt-")


def flat_of(alloc):
    return {n: r for items in alloc.values() for n, r in items if r}


def is_open(b):
    return b["id"].endswith(("-open-raid", "-open-leveling"))


def load_record(p):
    try:
        return json.load(open(p, encoding="utf-8")) if p.exists() else None
    except ValueError:   # a record a running search is writing
        return None


def save_record(p, st):
    p.write_text(json.dumps(st, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")


def spec_of_alloc(cls, alloc):
    return SM.spec_of(cls, {"allocation": alloc, "role": "dps"})


def entry_hybrid(cls, entry, data):
    """The hybrid spec an entry's rotation showcases (its builds carry a `spec` override: Frostfire's frostfire-raid, Shockadin's
    shockadin-raid), or None. A winner found in such a rotation is filed under that hybrid whatever its split: a build played around
    Frostfire Bolt is Frostfire although one tree has 30 points (spec_modes, 2026-09-29)."""
    specs = json.load(open(HERE / "raidsim" / "specs.json", encoding="utf-8"))
    ids = ((specs.get(cls) or {}).get(entry) or {}).get("builds") or []
    by = {b["id"]: b for b in data["builds"]}
    found = {SM.spec_of(cls, by[i]) for i in ids if i in by and not is_open(by[i])}   # every build of ours in the entry
    one = next(iter(found)) if len(found) == 1 else None
    return one if one and one.startswith("Hybrid") else None   # frost-raid hosts Frost and Arcane-Frost builds: by split there


def raid_spec(cls, entry, alloc, data):
    """The spec a raid winner belongs to: the entry's hybrid when the rotation showcases one and the split sits in its trees, else by split."""
    spec = spec_of_alloc(cls, alloc)
    hyb = entry_hybrid(cls, entry, data)
    if hyb and (spec == hyb or spec in hyb.replace("Hybrid ", "").split("/")):
        return hyb
    return spec


def family_text(cls, spec):
    """'Beast-Survival (a Beast Mastery/Survival hybrid)' or the tree name."""
    name = SM.spec_name(cls, spec)
    return f"{name} (a {spec.split(' ', 1)[1]} hybrid)" if spec.startswith("Hybrid") else name


# ------------------------------------------------------------------------------------------------ raid
def raid_candidates(cls, st, data, RM):
    """Per done entry: (entry, spec, dps, build or None, why). The build is made only for winners that qualify."""
    nums = RM.raid_numbers(cls)
    out = []
    for entry, e in st["entries"].items():
        if not e.get("done"):
            continue
        w = (e.get("again") or e["first"])["winner"]
        spec = raid_spec(cls, entry, w["allocation"], data)
        race = e["race"]
        wd = race["open winner"]["dps"]
        rivals = {k: v["dps"] for k, v in race.items() if k != "open winner" and v.get("dps")}   # raced with it: the same fights
        same = [b for b in data["builds"] if SM.mode_of(b) == "raid" and b.get("role", "dps") == "dps" and not is_open(b)
                and SM.spec_of(cls, b) == spec]
        pages = {b["id"]: nums[b["id"]]["group"] for b in same if b["id"] not in rivals and (nums.get(b["id"]) or {}).get("group")}
        allr = {**rivals, **pages}
        best = max(allr, key=allr.get) if allr else None
        why = None
        if best is not None and wd < allr[best] * (1 + GAIN_NEW):
            why = (f"confirms {best} ({wd / allr[best] - 1:+.2%} in a full raid, "
                   + ("raced together" if best in rivals else "against the pages' number") + ")")
        hands = {b["id"]: allr[b["id"]] for b in same if hand(b) and b["id"] in allr}
        bh = max(hands, key=hands.get) if hands else None
        replaces = bh if bh and wd >= hands[bh] * (1 + MIN_GAIN) else None
        b = None if why else make_raid_build(cls, entry, e, st, spec, w, allr, best, rivals, bh, hands.get(bh), replaces)
        out.append((entry, spec, wd, b, why))
    # one build per spec: the best winner across the class's rotations
    for i, (entry, spec, wd, b, why) in enumerate(out):
        if b is None:
            continue
        better = [(e2, d2) for e2, s2, d2, b2, w2 in out if b2 is not None and s2 == spec and d2 > wd]
        if better:
            e2, d2 = max(better, key=lambda x: x[1])
            out[i] = (entry, spec, wd, None, f"the {e2} rotation's winner of the same spec is better ({d2:.1f} against {wd:.1f} DPS)")
    return out


def core_raid(vals):
    core = []
    for n, v in vals.items():
        if v.get("share", 0) >= CORE_SHARE and len(core) < CORE_MAX:
            core.append({"talent": n, "why": f"{v['lost']:.0f} DPS lost without it ({v['share']:.0%} of the build in a full raid; removal, 12,000 fights)."})
    return core


def make_raid_build(cls, entry, e, st, spec, w, allr, best, rivals, best_hand, hand_dps, replaces):
    name = SM.spec_name(cls, spec)
    run = e.get("again") or e["first"]
    wd = e["race"]["open winner"]["dps"]
    ob = e.get("ours_best")
    vals = e.get("values") or {}
    zero = [n for n, v in vals.items() if abs(v.get("lost", 0)) < 0.05]
    b = {"id": f"{SM.spec_slug(cls, spec)}-open-raid", "name": f"{name} — Raid (open talent search)",
         "role": "dps", "content": "raid", "tier": "draft", "spec": spec, "generated": TODAY, "derived": "raid",
         "summary": (f"The {family_text(cls, spec)} raid build the open talent search found on {TODAY}: every legal 51-point build with no "
                     f"tree rule, searched in the community simulator's {entry} rotation in a full raid (every raid buff and debuff: the group "
                     f"setting; raidsim/family_search.py: every pair of keystones polished by a short hill climb first, then the machine-learning "
                     f"search, the winner raced against the rotation's builds over 30,000 fights). "
                     + (f"{wd / allr[ob] - 1:+.1%} over {ob}, the best of our builds in that rotation." if ob in allr else "")),
         "allocation": w["allocation"], "core": core_raid(vals), "flex": [],
         "notes": [f"Open search result ({entry}, full raid): {w['split']} ({family_text(cls, spec)}) at {wd:.1f} DPS; "
                   + ", ".join(f"{k} {v:.1f}" for k, v in sorted(rivals.items(), key=lambda kv: -kv[1])) + " in the same fights"
                   + (f"; {run.get('simulated_builds', 0):,} builds simulated, {run.get('runs_agree', 0)} independent runs reached the top" if run.get("simulated_builds") else "")
                   + "."],
         "open_questions": [f"An open-search {name} build: check it against the community's {name} builds at launch."],
         "sources": ["https://github.com/ElliotWood/Forever", e.get("link") or RSH.tf_link(cls, flat_of(w["allocation"]))]}
    pages = {k: v for k, v in allr.items() if k not in rivals}
    if pages:
        b["notes"].append("The spec's other builds on the pages (their best entry, full raid): " + ", ".join(f"{k} {v:.1f}" for k, v in sorted(pages.items(), key=lambda kv: -kv[1])) + ".")
    if replaces:
        b["replaces"] = replaces
        b["notes"].insert(0, f"{wd / hand_dps - 1:+.1%} over the best hand draft of the spec, {replaces}, over the replacement bar: this build is the "
                             f"spec's raid pick, the hand draft stays as the alternative.")
    elif best_hand:
        b["notes"].append(f"Against the spec's best hand draft {best_hand}: {wd / hand_dps - 1:+.1%} (under the replacement bar: the hand draft stays the pick "
                          f"unless the re-race says otherwise).")
    if e.get("rotation_changed"):
        b["notes"].append(f"The {entry} raid rotation was re-tuned on this build (a pass in its rotation-search record); the numbers use it.")
    cr = (st.get("cross") or {}).get(entry)
    if cr and cr.get("tested"):
        lab = (cr.get("adopted") or {}).get("build") or "open winner"
        b["notes"].append("Sibling rotations tried on it (10,000 fights): " + ", ".join(f"{sib} {v.get(lab, 0):+.1%}" for sib, v in cr["tested"].items())
                          + (f"; {cr['adopted']['from']}'s rotation adopted ({cr['adopted']['gain']:+.1%})" if cr.get("adopted") else "; none adopted") + ".")
    og = (st.get("own_gear") or {}).get(entry)
    if og and og.get("gear"):
        better = og["dps_own_bis"] > og["dps_standard"]
        b["notes"].append(f"A phase-1 BiS set picked for this family ({og['gear']}, item level {og.get('ilvl')}): {og['dps_own_bis']:.1f} DPS against "
                          f"{og['dps_standard']:.1f} in the rotation's standard set" + (": a lead for the gear sets (not applied)." if better else ": the standard set stays."))
    if cls == "hunter" and "Improved Tracking" in zero:   # a search run before the bench's target had a creature type (2026-10-06)
        zero.remove("Improved Tracking")
        b["notes"].append("The search ran before 2026-10-06, when the bench's target got a creature type (an Elemental): Improved Tracking measured 0 "
                          "in it and is +5% damage against every raid creature type but Mechanical since (+4.9% for this build in a full raid). The "
                          "search's numbers above are from that run; the page's numbers come from the re-race. Re-run the search (family_search.py "
                          "--fresh) to value the talent in the search itself.")
    if zero:
        b["notes"].append("Talents the simulator measures at 0 DPS in this build (tier fillers; the filler audit may move them): " + ", ".join(zero) + ".")
    b["notes"].append(f"Simulator numbers are the community's model of the beta (ElliotWood/Forever {sim_commit()} with this project's patches), "
                      "not in-game measurements.")
    return b


# ------------------------------------------------------------------------------------------------ leveling
def leveling_candidates(cls, st, data, RM):
    """Per done rotation: (rotation, spec, weighted seconds, build or None, why)."""
    nums = RM.leveling_numbers(cls)
    out = []
    for spec_rot, r in st["rotations"].items():
        if not r.get("done"):
            continue
        spec = spec_of_alloc(cls, r["winner"]["allocation"])
        race = r["race"]
        wt = race["open winner"]["weighted"]
        rivals = {k: v["weighted"] for k, v in race.items() if k != "open winner" and not k.startswith("finalist ") and v.get("weighted")}
        same = [b for b in data["builds"] if SM.mode_of(b) == "leveling" and not is_open(b) and SM.spec_of(cls, b) == spec]
        pages = {}
        for b in same:
            if b["id"] in rivals:
                continue
            wv = RM.weighted(nums.get(b["id"]) or {})
            if wv:
                pages[b["id"]] = wv
        allr = {**rivals, **pages}
        best = min(allr, key=allr.get) if allr else None   # the fastest: the fewest seconds per kill
        why = None
        if best is not None and allr[best] / wt - 1 < GAIN_NEW:
            why = (f"confirms {best} ({allr[best] / wt - 1:+.2%} faster per kill, levels 20-60, "
                   + ("raced together" if best in rivals else "against the pages' number") + ")")
        hands = {b["id"]: allr[b["id"]] for b in same if hand(b) and b["id"] in allr}
        bh = min(hands, key=hands.get) if hands else None
        replaces = bh if bh and hands[bh] / wt - 1 >= MIN_GAIN else None
        b = None if why else make_leveling_build(cls, spec_rot, r, spec, allr, rivals, bh, hands.get(bh), replaces)
        out.append((spec_rot, spec, wt, b, why))
    for i, (rot, spec, wt, b, why) in enumerate(out):
        if b is None:
            continue
        better = [(r2, t2) for r2, s2, t2, b2, w2 in out if b2 is not None and s2 == spec and t2 < wt]
        if better:
            r2, t2 = min(better, key=lambda x: x[1])
            out[i] = (rot, spec, wt, None, f"the {r2} rotation's winner of the same spec is faster ({t2:.2f} against {wt:.2f} s per kill)")
    return out


def core_leveling(vals):
    core = []
    for n, v in vals.items():
        if v.get("seconds", 0) >= CORE_SECONDS and len(core) < CORE_MAX:
            core.append({"talent": n, "why": f"{v['seconds']:+.1f} s per kill at level 60 without it (removal, 3,000 fights)."})
    return core


def make_leveling_build(cls, rot, r, spec, allr, rivals, best_hand, hand_t, replaces):
    name = SM.spec_name(cls, spec)
    wt = r["race"]["open winner"]["weighted"]
    ob = r.get("ours_best")
    b = {"id": f"{SM.spec_slug(cls, spec)}-open-leveling", "name": f"{name} — Leveling (open talent search)",
         "role": "dps", "content": "leveling", "tier": "draft", "spec": spec, "generated": TODAY, "derived": "leveling",
         "summary": (f"The {family_text(cls, spec)} leveling build the open leveling search found on {TODAY}: every legal 51-point build with no tree "
                     f"rule, searched at level 60 in the fight lab (this project's solo leveling simulator: same-level mobs, eating, drinking and "
                     f"deaths included) playing the {rot} rotation, the winner picked by a race at levels 20-60 among the level-60 finalists "
                     f"(fightlab/fl_open_search.py); the talent order is the stats model's ({r.get('model')}). "
                     + (f"{allr[ob] / wt - 1:+.1%} faster per kill than {ob}, the fastest of our leveling builds in that race." if ob in allr else "")),
         "allocation": r["winner"]["allocation"], "order": r["order"], "core": core_leveling(r.get("values") or {}), "flex": [],
         "notes": [f"Race at levels 20-60 (seed 3, 3,000 fights per level; level-weighted seconds per kill, lower is faster): this build {wt:.2f}; "
                   + ", ".join(f"{k} {v:.2f}" for k, v in sorted(rivals.items(), key=lambda kv: kv[1])) + "."
                   + (f" The search simulated {r['simulated_builds']:,} builds." if r.get("simulated_builds") else "")],
         "open_questions": [f"An open-search {name} leveling build: check it while leveling at launch."],
         "sources": ["https://talentsforever.com/" + cls, r.get("link") or RSH.tf_link(cls, flat_of(r["winner"]["allocation"]))]}
    pages = {k: v for k, v in allr.items() if k not in rivals}
    if pages:
        b["notes"].append("The spec's other leveling builds on the pages: " + ", ".join(f"{k} {v:.2f} s" for k, v in sorted(pages.items(), key=lambda kv: kv[1])) + ".")
    if replaces:
        b["replaces"] = replaces
        b["notes"].insert(0, f"{hand_t / wt - 1:+.1%} faster than the hand draft {replaces}, over the replacement bar: this build is the spec's "
                             f"leveling pick, the hand draft stays as the alternative.")
    elif best_hand:
        b["notes"].append(f"Against the spec's fastest hand draft {best_hand}: {hand_t / wt - 1:+.1%} (under the replacement bar: the hand draft stays the pick).")
    b["notes"].append("Fight-lab numbers are a model of the beta (the assumptions in fightlab/tables.py), not in-game measurements.")
    return b


# ------------------------------------------------------------------------------------------------ main
def complete(st, key):
    return all(v.get("done") for v in (st or {}).get(key, {}).values()) and bool((st or {}).get(key))


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("classes", nargs="*")
    ap.add_argument("--write", action="store_true", help="write the builds (else print the verdicts)")
    ap.add_argument("--no-tidy", action="store_true", help="skip filler_audit.py on the written raid builds")
    ap.add_argument("--partial", action="store_true", help="use a record whose search is still running (its done entries only)")
    ap.add_argument("--only", choices=["raid", "leveling"], help="one kind of record only (raid while the class's leveling search still runs)")
    ap.add_argument("--race", action="store_true", help="re-race the entries that got a build (raidsim/run.py --write and --env environments --write)")
    ap.add_argument("--regen", action="store_true", help="rebuild.py <class> --steps regen afterwards (the pages)")
    a = ap.parse_args()
    import render_modes as RM
    ML = _load("ml_builds_open", HERE / "raidsim" / "ml_builds.py")
    for cls in a.classes or SM.CLASSES:
        fam = load_record(FAMILIES / f"{cls}.json") if a.only != "leveling" else None
        lvl = load_record(OPEN / f"{cls}.json") if a.only != "raid" else None
        use_fam = fam and (complete(fam, "entries") or (a.partial and fam.get("entries")))
        use_lvl = lvl and (complete(lvl, "rotations") or (a.partial and lvl.get("rotations")))
        if not use_fam and not use_lvl:
            if fam or lvl:
                print(f"== {cls}: record not complete (an entry or rotation still running); --partial uses the done ones")
            continue
        bp = paths.builds_json("forever", cls)
        data = json.load(open(bp, encoding="utf-8"))
        rc = raid_candidates(cls, fam, data, RM) if use_fam else []
        lc = leveling_candidates(cls, lvl, data, RM) if use_lvl else []
        print(f"== {cls}")
        for entry, spec, wd, b, why in rc:
            print(f"  raid {entry}: {SM.spec_name(cls, spec)} {wd:.1f} DPS -> " + (f"new build {b['id']}" + (f" (replaces {b['replaces']})" if b.get("replaces") else "") if b else why))
        for rot, spec, wt, b, why in lc:
            print(f"  leveling {rot}: {SM.spec_name(cls, spec)} {wt:.2f} s per kill -> " + (f"new build {b['id']}" + (f" (replaces {b['replaces']})" if b.get("replaces") else "") if b else why))
        if not a.write:
            continue
        new = [b for *_, b, _ in rc if b] + [b for *_, b, _ in lc if b]
        kinds = ("-open-raid",) if a.only == "raid" else ("-open-leveling",) if a.only == "leveling" else ("-open-raid", "-open-leveling")
        old = [b["id"] for b in data["builds"] if b["id"].endswith(kinds)]   # rewritten from the records (the other kind stays with --only)
        data["builds"] = [b for b in data["builds"] if not b["id"].endswith(kinds)] + new
        bp.write_text(dumps(data) + "\n", encoding="utf-8")
        with locked(HERE / "raidsim" / "specs.json.lock"):   # a running search of another class may point an entry at a new rotation
            if old:
                ML.drop_from_entries(cls, set(old))
            if use_fam:
                for entry, spec, wd, b, why in rc:
                    if b:
                        SB.add_to_entry(cls, entry, b["id"])
        gone = sorted(set(old) - {b["id"] for b in new})
        print(f"  wrote {bp.relative_to(ROOT).as_posix()}: {', '.join(b['id'] for b in new) or 'no open build'}" + (f"; removed {', '.join(gone)}" if gone else ""))
        raced = []
        if use_fam:
            for entry, spec, wd, b, why in rc:
                fam["entries"][entry]["builds"] = {"written": [b["id"]] if b else [], "why": why, "spec": spec, "date": TODAY}
            save_record(FAMILIES / f"{cls}.json", fam)
            for entry, spec, wd, b, why in rc:
                if b:
                    raced.append(entry)
                    if not a.no_tidy:
                        ML.tidy(cls, entry, b["id"])
        if use_lvl:
            for rot, spec, wt, b, why in lc:
                lvl["rotations"][rot]["builds"] = {"written": [b["id"]] if b else [], "why": why, "spec": spec, "date": TODAY}
            save_record(OPEN / f"{cls}.json", lvl)
        if a.race or a.regen:
            import subprocess
            steps = [[sys.executable, str(HERE / "validate_builds.py"), cls]]
            if a.race:
                for entry in raced:
                    steps += [[sys.executable, str(HERE / "raidsim" / "run.py"), cls, "--spec", entry, "--write"],
                              [sys.executable, str(HERE / "raidsim" / "run.py"), cls, "--spec", entry, "--env", "environments", "--write"]]
            if a.regen:
                steps.append([sys.executable, str(HERE / "rebuild.py"), cls, "--steps", "regen"])
            for args in steps:
                r = subprocess.run(args, capture_output=True, text=True, encoding="utf-8", errors="replace", cwd=str(ROOT))
                last = (r.stdout.strip().splitlines() or [""])[-1]
                print(f"  [rc={r.returncode}] {' '.join(pathlib.Path(x).name if '/' in x or chr(92) in x else x for x in args[1:])} | {last[:160]}", flush=True)
                if r.returncode:
                    print("    " + r.stderr[-600:].replace("\n", "\n    "), flush=True)
    if a.write and not (a.race and a.regen):
        print("next: validate_builds.py and render_builds.py; re-race the entries that got a build (raidsim/run.py --spec <entry> --write and "
              "--env environments --write); rebuild.py --steps regen (or --race --regen here)")


if __name__ == "__main__":
    main()
