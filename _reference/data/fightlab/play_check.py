"""The leveling play check (2026-11-20; the user's decision on the audit session's recommendations after D11: the raid play check's
leveling counterpart, before the leveling pages are pushed; its rules drafted with the audit session, La-Lf by this session, Lg-Ll by
the audit's). For every leveling page pick (level_guides.pick: its build, order and tuned rotation), on level_guides' measured record of
it (standard gear, single pulls, the guide's stage levels; `level_guides.py <class> --measure`, current by its fingerprint):

 La  a spell a stage names (bold in its text) that the lab presses 0 times at every measured level of the stage (level_guides --check's
     warning): FAIL.
 Lb  a spell a stage presses before its trainer level or before the order takes its talent (level_guides --check's error): FAIL.
 Lc  a talent worth exactly nothing (time per kill the same to 0.01 s, seed 1) at 60 and at every level of 20-60 by tens the order holds
     it: FAIL unless a gate, a leveling utility tag (utility_tags.usefulness with avoidance counted: the character is hit) or a recorded
     filler (fightlab/filler/<class>-<slug>.json). Measured at 60 first; only talents worth nothing there are measured lower.
 Ld  a tuned rule (fightlab/rotations/<class>-<rotation>.json `veto`) that takes off a spell a stage names or a required signature spell
     (signature_spells.json, leveling): FAIL, naming the rule.
 Le  the lab presses a spell at least 0.5 times a kill in a stage that never names it (level_guides --check's warning): FAIL.
 Lf  a key bound to a spell the build cannot have at that level (level_guides --check's error): FAIL.
 Lg  never tried: a damaging, absorbing or resource ability the character has (the class's spellbook by trainer level, the build's talent
     abilities by its order) that the lab presses 0 times at every measured level from the one it arrives and no rule vetoes: FAIL "never
     tried" unless fightlab/never-tried.json records a verdict for the class and rotation ("forced into the priority on <date>: slower by
     X%"). Area spells are left to the AoE variants (tables.AOE_SPELLS), the class's pet tab to the pet.
 Lh  a jump: time per kill rising more than 5% from one measured level to the next (levels at 10 and up): FAIL until
     fightlab/play-check-notes.json explains it or the order is repaired.
 Li  survival and idle: more than 2 deaths per 100 kills, or more than 40% of the time per kill out of the fight (drinking, eating,
     waiting), at a measured level: FAIL for a look (the audit session's thresholds, to tune on the spread).
 Lj  the pet: at a measured level where the build keeps one (pet sources in the damage shares), the pet under 5% of the damage, or dead in
     more than 10 of 100 pulls: FAIL.
 Lk  what is kept up (the class's armor, aspect, seal, imbue, poisons, stance or form, self buffs): not built yet (each module applies
     them its own way); listed as open.
 Ll  parsing: fightlab/module_lint.py's rows for the class (a name the data lacks, a tooltip number that parses to 0): FAIL.
The record (fightlab/play-check.json) carries each pick's presses per kill by measured level (its cast list, for the audit's reading) and a
fingerprint of what the numbers depend on (the class module, engine, tables, run.py, the rules file, the class's talent and spell data,
the data build): a page row from another fingerprint is refused.

    python _reference/data/fightlab/play_check.py [classes] [--fights 1500] [--jobs 8] [--skip-removal] [--write]
"""
import argparse
import datetime
import hashlib
import json
import multiprocessing
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
DATA = HERE.parent
ROOT = DATA.parents[1]
sys.path[:0] = [str(HERE), str(DATA)]
import run as FR  # noqa: E402
import level_guides as LG  # noqa: E402
import signature as SG  # noqa: E402
import utility_tags as UT  # noqa: E402
import validate_builds as VB  # noqa: E402
import spec_modes as SM  # noqa: E402

OUT = HERE / "play-check.json"
VERDICTS = HERE / "never-tried.json"
NOTES = HERE / "play-check-notes.json"
DAMAGE = re.compile(r"\d+ (?:to \d+ )?(?:\w+ ){0,2}damage|\babsorb|restores? [^.]*\b(?:mana|rage|energy)\b|\bgains? \d+ (?:rage|energy|mana)",
                    re.I)
CHECK_LEVELS = [20, 30, 40, 50, 60]
# module_lint rows that read a retired mechanism behind a switch that is off (not a misread): Ll records them as notes
LINT_RETIRED = {"mage": {"MB_MISSILE": "the 70425 wording of Missile Barrage's missile procs, hotfixed out (mage.MB_MISSILE_PROCS False)"}}
JUMP, DEATHS, IDLE, PET_SHARE, PET_DEATHS, LE_MIN = 0.05, 2.0, 0.40, 0.05, 10.0, 0.5


def code_fingerprint(cls, rot):
    files = [HERE / "engine.py", HERE / "tables.py", HERE / "run.py", FR.rotation_file(cls, rot), DATA / "forever-talents" / f"{cls}.json",
             DATA / "forever-spells" / f"{cls}.json", DATA / "signature_spells.json"]
    mod = (FR.MODULES.get(cls) or (None,))[0] if isinstance(FR.MODULES, dict) else None
    if mod:
        files.append(HERE / f"{mod}.py")
    h = hashlib.sha1()
    for f in files:
        f = pathlib.Path(f)
        h.update(f.name.encode("utf-8"))
        h.update(f.read_bytes() if f.exists() else b"-")
    import data_build as DB
    h.update(str(DB.BUILD).encode("utf-8"))
    return h.hexdigest()[:16]


def book_levels(cls):
    """{spell: (trainer level of its first rank, the top rank's tooltip)} of the class's spellbook, the pet tab left out."""
    out = {}
    for tab in json.load(open(DATA / "forever-spells" / f"{cls}.json", encoding="utf-8")).get("tabs", []):
        if str(tab.get("name", "")).lower().startswith("pet"):
            continue
        for sp in tab.get("spells", []):
            rk = [r for r in sp.get("ranks", []) if r.get("id")]
            if not rk:
                continue
            lv = min(int(r.get("level") or 1) for r in rk)
            out[sp["name"]] = (lv, str(rk[-1].get("text", "")))
    return out


def aoe_names():
    try:
        import tables as T
        return set(getattr(T, "AOE_SPELLS", {}) or {})
    except Exception:   # noqa: BLE001
        return set()


def _init():
    FR.apply_gear("greens")


def _ttk(job):
    cls, rot, alloc, level, fights = job
    try:
        return FR.simulate(cls, alloc, level, rot, fights, 1, 0)["time_per_kill"]
    except Exception as e:   # noqa: BLE001
        return f"error {type(e).__name__}: {e}"


def held_at(b, level):
    return {n for n, r in FR.allocation_at(b, level).items() if r} if level < 60 else {n for v in b["allocation"].values() for n, r in v if r}


def zero_talents(cls, rot, b, pool, fights):
    """Lc: {talent: levels} of the talents whose removal leaves time per kill the same to 0.01 s at 60 and at every level of 20-60 by
    tens the order holds them."""
    a60 = FR.allocation_at(b, 60)
    names = [n for n, r in a60.items() if r]
    jobs = [(cls, rot, a60, 60, fights)] + [(cls, rot, {k: v for k, v in a60.items() if k != n}, 60, fights) for n in names]
    res = pool.map(_ttk, jobs, chunksize=1)
    if isinstance(res[0], str):
        return {"_error": res[0]}
    zero = [n for n, r in zip(names, res[1:]) if not isinstance(r, str) and abs(r - res[0]) < 0.005]
    out = {}
    for n in zero:
        lv = [L for L in CHECK_LEVELS[:-1] if n in held_at(b, L)]
        if not lv:
            out[n] = [60]
            continue
        jl = []
        for L in lv:
            aL = FR.allocation_at(b, L)
            jl += [(cls, rot, aL, L, fights), (cls, rot, {k: v for k, v in aL.items() if k != n}, L, fights)]
        rl = pool.map(_ttk, jl, chunksize=1)
        if all(not isinstance(rl[2 * i], str) and abs(rl[2 * i] - rl[2 * i + 1]) < 0.005 for i in range(len(lv))):
            out[n] = lv + [60]
    return out


def is_gate(cls, b, talent):
    st = {t: {n: r for n, r in v if r and n != talent} for t, v in b["allocation"].items()}
    errors = []
    VB.check_state(VB.load_forever()[cls], st, "x", errors)
    return errors[0] if errors else None


def filler_recorded(cls, spec):
    p = HERE / "filler" / f"{cls}-{SM.spec_slug(cls, spec)}.json"
    if not p.exists():
        return set()
    try:
        x = json.load(open(p, encoding="utf-8"))
    except ValueError:
        return set()
    out = set()
    for k in ("zero", "zero_points", "kept", "free", "gates"):
        v = x.get(k)
        if isinstance(v, dict):
            out |= set(v)
        elif isinstance(v, list):
            out |= {(e[0] if isinstance(e, (list, tuple)) else e.get("talent") if isinstance(e, dict) else e) for e in v}
    return {n for n in out if isinstance(n, str)}


def check_class(cls, pool, fights, removal):
    data = LG.load(cls)
    if not data:
        return {}
    rows = LG.check(cls)
    verdicts = (json.load(open(VERDICTS, encoding="utf-8")).get(cls) or {}) if VERDICTS.exists() else {}
    notes = (json.load(open(NOTES, encoding="utf-8")).get(cls) or {}) if NOTES.exists() else {}
    use = UT.usefulness(cls, True)   # leveling: the character is hit, avoidance counts (the tank order)
    book = book_levels(cls)
    aoe = aoe_names()
    try:
        import module_lint as ML
        bad, zero_parse, fields, patterns = ML.lint(cls)
        lint_rows = [f"unknown name {x}" for x in (bad or [])] + [f"parses to 0: {x}" for x in (zero_parse or [])] \
            + [str(x) for x in (fields or [])] + [str(x) for x in (patterns or [])]
    except Exception as e:   # noqa: BLE001
        lint_rows = [f"module_lint failed: {type(e).__name__}: {e}"]
    out = {}
    for g in data["guides"]:
        spec = g["spec"]
        b, order, prov, rot = LG.pick(cls, spec)
        if not b:
            continue
        bb = dict(b, order=order)
        f = {"build": b["id"], "rotation": rot, "provisional_order": prov, "fingerprint": code_fingerprint(cls, rot),
             "guide_fingerprint": LG.fingerprint(cls, b, order, rot), "fail": [], "notes": [], "levels": {}}
        out[spec] = f
        m = LG.measured(cls, spec, b, order, rot)
        if not m:
            f["fail"].append("the guide's fight-lab numbers are not current: run level_guides.py <class> --measure first")
            continue
        lv = {int(L): r for L, r in m["levels"].items() if isinstance(r, dict) and r.get("seconds")}
        f["levels"] = {str(L): {k: r.get(k) for k in ("seconds", "deaths_per_100", "idle_share", "casts", "shares")} for L, r in sorted(lv.items())}
        # La, Lb, Le, Lf: level_guides' own check of the guide against the measured record
        for level, txt in rows:
            if not (txt.startswith(f"{spec}:") or txt.startswith(f"{spec} ")):
                continue
            if level == "error":
                f["fail"].append(f"Lb/Lf: {txt}")
            elif "never casts it there" in txt:
                f["fail"].append(f"La: {txt}")
            elif "never names it" in txt:
                n = re.search(r"presses .+? ([0-9.]+) times a kill", txt)
                (f["fail"] if n and float(n.group(1)) >= LE_MIN else f["notes"]).append(f"Le: {txt}")
            elif "no fight-lab numbers" in txt:
                f["fail"].append(f"La: {txt}")
            else:
                f["notes"].append(txt)
        # Ld: a rule that takes off a named or signature spell
        named = {n for s in LG.stages(g) for n in LG.bold_names(s)}
        rl = SG.rule(cls, spec, "leveling") or {}
        try:
            veto = json.load(open(FR.rotation_file(cls, rot), encoding="utf-8")).get("veto") or {}
        except (OSError, ValueError):
            veto = {}
        for sp, v in sorted(veto.items()):
            if v.get("off") and (sp in named or sp in rl.get("required", [])):
                f["fail"].append(f"Ld: the rules file's veto takes {sp} off ({json.dumps(v)}) and "
                                 + ("it is a required signature spell" if sp in rl.get("required", []) else "the guide names it"))
        # Lh: a jump between measured levels
        ls = sorted(L for L in lv if L >= 10)
        for a, c in zip(ls, ls[1:]):
            s0, s1 = lv[a]["seconds"], lv[c]["seconds"]
            if s0 and s1 / s0 - 1 > JUMP:
                why = ((notes.get(spec) or {}).get("jump") or {}).get(f"{a}-{c}")
                (f["notes"] if why else f["fail"]).append(f"Lh: {s0} s a kill at {a}, {s1} at {c} (+{s1 / s0 - 1:.0%})" + (f": {why}" if why else ""))
        # Li: survival and idle
        for L, r in sorted(lv.items()):
            if L < 10:
                continue
            if (r.get("deaths_per_100") or 0) > DEATHS:
                f["fail"].append(f"Li: {r['deaths_per_100']} deaths per 100 kills at {L}")
            if r.get("idle_share") is not None and r["idle_share"] > IDLE:
                f["fail"].append(f"Li: {r['idle_share']:.0%} of the time out of the fight at {L}")
        # Lj: the pet
        for L, r in sorted(lv.items()):
            ps = set(r.get("pet_sources") or [])
            if not ps or L < 10:
                continue
            share = sum(v for k, v in (r.get("shares") or {}).items() if k in ps)
            if share < PET_SHARE:
                f["fail"].append(f"Lj: the pet deals {share:.0%} of the damage at {L}")
            if (r.get("pet_deaths_per_100") or 0) > PET_DEATHS:
                f["fail"].append(f"Lj: the pet dies in {r['pet_deaths_per_100']} of 100 pulls at {L}")
        if "idle_share" not in next(iter(lv.values()), {}):
            f["notes"].append("Li/Lj: the measured record predates the idle and pet fields (level_guides --measure again)")
        # Lg: never tried
        pressed = {sp for r in lv.values() for sp, n in (r.get("casts") or {}).items() if n}
        tal_abil = {t for t in held_at(bb, 60) if t in book}
        ver = (verdicts.get(rot) or {})
        for sp, (lv0, tip) in sorted(book.items()):
            arrive = SG.learn_level(cls, sp, bb) if sp in SG.talent_names(cls) else lv0
            if arrive is None or sp in pressed or (sp in veto) or sp in aoe or not DAMAGE.search(tip):
                continue
            if sp in SG.talent_names(cls) and sp not in tal_abil:
                continue
            if not any(L >= arrive for L in lv):
                continue
            if ver.get(sp):
                f["notes"].append(f"Lg: {sp} never pressed: {ver[sp]}")
            else:
                f["fail"].append(f"Lg: {sp} (from level {arrive}) is never pressed, no rule vetoes it, and no verdict says it was tried")
        # Ll: parsing (a retired mechanism behind an off switch is a note, with its reason)
        for x in lint_rows:
            why = next((w for k, w in (LINT_RETIRED.get(cls) or {}).items() if f"`{k}`" in x), None)
            (f["notes"] if why else f["fail"]).append(f"Ll: {x}" + (f" ({why})" if why else ""))
        f["notes"].append("Lk (what is kept up) is not built yet")
        # Lc: talents worth nothing at every level held
        if removal:
            zt = zero_talents(cls, rot, bb, pool, fights)
            if "_error" in zt:
                f["fail"].append(f"Lc: the removal runs failed: {zt['_error']}")
            else:
                rec = filler_recorded(cls, spec)
                for t, levels in sorted(zt.items()):
                    g_ = is_gate(cls, b, t)
                    why = ("gate: " + g_.split(": ", 1)[-1][:80]) if g_ else ("utility: " + [x for x, _ in UT.TAGS][use[t]]
                                                                              if use.get(t, UT.NONE) < UT.NONE else ("recorded filler" if t in rec else None))
                    (f["notes"] if why else f["fail"]).append(f"Lc: {t} worth nothing at {', '.join(map(str, levels))}" + (f" ({why})" if why else ""))
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("classes", nargs="*")
    ap.add_argument("--fights", type=int, default=1500)
    ap.add_argument("--jobs", type=int, default=8)
    ap.add_argument("--skip-removal", action="store_true", help="leave Lc out (its removal runs are the slow part)")
    ap.add_argument("--write", action="store_true")
    a = ap.parse_args()
    rec = json.loads(OUT.read_text(encoding="utf-8")) if OUT.exists() else {}
    classes = a.classes or [c for c in SM.CLASSES if LG.load(c)]
    with multiprocessing.Pool(a.jobs, initializer=_init) as pool:
        for cls in classes:
            res = check_class(cls, pool, a.fights, not a.skip_removal)
            for spec, f in res.items():
                print(f"== {cls} {spec} ({f['build']}, {f['rotation']}): " + ("FAIL" if f["fail"] else "pass"), flush=True)
                for x in f["fail"]:
                    print(f"   FAIL {x}", flush=True)
                for x in f["notes"]:
                    print(f"   note {x}", flush=True)
                for L, r in f["levels"].items():
                    casts = ", ".join(f"{sp} {n}" for sp, n in sorted((r.get("casts") or {}).items(), key=lambda kv: -kv[1]))
                    print(f"   L{L}: {r.get('seconds')} s; {casts}", flush=True)
            if a.write:
                rec[cls] = {"date": datetime.date.today().isoformat(), "specs": res}
                OUT.write_text(json.dumps(rec, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
