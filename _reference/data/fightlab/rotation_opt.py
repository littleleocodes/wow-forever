"""Tune the leveling rotations in the fight lab: rules on top of each class module's hand-written priority list.

    python _reference/data/fightlab/rotation_opt.py mage [--spec frost-leveling] [--write]
    python _reference/data/fightlab/rotation_opt.py --all [--write] [--jobs 10]

The rules are the engine's `veto` (engine.Fight.can_afford: outside them the spell counts as unaffordable, so the priority list
falls through to its next choice) plus the rest thresholds and the module's own `ROTATION_KNOBS`:
  * never cast a spell;
  * cast it only above a share of mana (keep mana for what matters);
  * cast it only while the mob has more than a share of its health left (no expensive casts on a dying mob), or only below one;
  * drink below / eat below (the downtime thresholds: rest earlier or later);
  * a module knob (the priest's wand-below and shield-below).
Local search like raidsim/apl_opt.py: every candidate plays the spec's leveling build (the class pipeline's hand draft for the
main spec model, the extra reports' builds for the others) at the pipeline's levels with common random numbers (seed 1,
`--fights`); the best candidates run again on seed 2 with `--confirm` fights, and a rule is kept only when it wins there by more
than `--min-gain` of the level-weighted time per kill (weights level / 10, as the races). With --write the rules go to
`fightlab/rotations/<class>-<spec>.json`, which `run.make_module` applies to every fight-lab run of that spec model
(WOW_FL_ROTATION=default switches them off; the mage regression runs without them).
"""
import argparse
import copy
import datetime
import json
import multiprocessing
import os
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[2]
sys.path.insert(0, str(ROOT / "_reference/data"))
sys.path.insert(0, str(ROOT / "_reference/data/scorer"))
sys.path.insert(0, str(HERE))
import run as FR  # noqa: E402  (fightlab/run.py)
import tables  # noqa: E402
import signature as SG  # noqa: E402  (signature spells, user rule 2026-10-22)
import fl_signature as FS  # noqa: E402

MIN_MANA = (0.15, 0.3, 0.5)
MIN_HP = (0.1, 0.2, 0.35)
MAX_HP = (0.2, 0.35)
DRINK = (0.15, 0.25, 0.45, 0.6, 0.8)
EAT = (0.4, 0.5, 0.8, 0.9)


def targets(cls):
    """[(spec model, build id)] the fight lab plays for a class: the main spec's hand draft and every extra report's build."""
    P = getattr(FR.class_module(cls), "PIPELINE", {})
    out, seen = [], set()
    for spec, bid in [(P.get("spec"), P.get("hand"))] + [(x.get("spec"), x.get("build") or x.get("hand")) for x in P.get("extra_reports", [])]:
        if spec and bid and spec not in seen:
            seen.add(spec)
            out.append((spec, bid))
    return out, [int(x) for x in str(P.get("levels", "20,30,40,50,60")).split(",") if x]


def _init():
    import engine
    # a hopeless candidate (a Balance druid told not to cast Starfire on a wounded mob) times out after 3 minutes of fight time instead
    # of 10: no leveling fight here lasts a minute and a half, and 600 ten-minute fights per level stalled the search for hours (2026-09-28)
    engine.Fight.run.__defaults__ = (180.0,)
    orig = engine.Fight.run

    def run(self, max_time=180.0):   # a candidate that times out 20 fights is hopeless: stop it there (_run scores it as never killing)
        r = orig(self, max_time)
        if r == "timeout":
            _TIMEOUTS[0] += 1
            if _TIMEOUTS[0] > 20:
                raise _Hopeless()
        return r
    engine.Fight.run = run
    FR.apply_gear("greens")
    os.environ["WOW_FL_ROTATION"] = "default"   # the candidate's rules are passed explicitly


class _Hopeless(Exception):
    pass


_TIMEOUTS = [0]


def _run(job):
    cls, spec, bid, level, fights, seed, rot = job
    build = FR.load_build(cls, bid)
    _TIMEOUTS[0] = 0
    try:
        r = FR.simulate(cls, FR.allocation_at(build, level), level, spec, fights, seed, 0, rot=rot)
    except _Hopeless:
        return {"time_per_kill": 1e9, "deaths_per_100": 0.0, "casts": {}, "mana_per_kill": 0.0, "shares": {}}
    return {"time_per_kill": r["time_per_kill"], "deaths_per_100": r["deaths_per_100"], "casts": r["casts"], "mana_per_kill": r["mana_per_kill"],
            "shares": r.get("shares", {}), "kills": r.get("kills"), "pet_sources": r.get("pet_sources", [])}


def weighted(per_level):
    tot = sum(L / 10 for L in per_level)
    return sum(v * L / 10 for L, v in per_level.items()) / tot


def evaluate(pool, cls, spec, bid, levels, rots, fights, seed):
    """[{level: result}] for each rule set in rots."""
    jobs = [(cls, spec, bid, L, fights, seed, rot) for rot in rots for L in levels]
    res = pool.map(_run, jobs, chunksize=1)
    out = []
    k = 0
    for _ in rots:
        out.append({L: res[k + i] for i, L in enumerate(levels)})
        k += len(levels)
    return out


def describe(change):
    kind, spell, val = change
    return {"off": lambda: f"never cast {spell}", "min_mana": lambda: f"{spell} only above {val:.0%} mana",
            "min_hp": lambda: f"{spell} only while the mob has more than {val:.0%} health",
            "max_hp": lambda: f"{spell} only when the mob is below {val:.0%} health", "drink_below": lambda: f"drink below {val:.0%} mana",
            "eat_below": lambda: f"eat below {val:.0%} health", "knob": lambda: f"{spell} = {val}",
            "clear": lambda: f"drop the rules on {spell}"}[kind]()   # (lazy: a "clear" change has no value to format)


def apply_change(rot, change):
    rot = copy.deepcopy(rot)
    kind, spell, val = change
    if kind in ("drink_below", "eat_below"):
        rot[kind] = val
    elif kind == "knob":
        rot.setdefault("knobs", {})[spell] = val
    elif kind == "clear":
        rot.get("veto", {}).pop(spell, None)
    else:
        rot.setdefault("veto", {}).setdefault(spell, {})[kind] = True if kind == "off" else val
    return rot


MAIN_SHARE = 0.30   # a spell dealing this share of the damage at some level is the build's main attack: never switched off or starved
CAST_KEEP = 0.5     # signature rule (2026-10-22): a rule may not cut a required spell's casts per kill below this share of the current rules'
SHARE_TOL = 0.01    # nor lower the tuning build's core share at 60 below min(min_share, current) - this (a point: the share's noise)


def required_spells(cls, spec):
    """{required spell: [specs]} of every spec that levels with the rotation (signature.rotation_required: the trees of
    derive_leveling.LEVEL and the hybrids of spec_modes.HYBRID_LEVELING_ROTATION); {} with WOW_FOREVER_SIGNATURE=0."""
    return SG.rotation_required(cls, spec) if FS.enabled() else {}


def sanitize(rot, required):
    """Drop the rules that switch off or starve a required spell ("off", "max_hp", a mana gate above the lowest); returns the list of
    dropped rules. A rules file holding one was tuned before the signature rule (2026-10-22): re-tune it with --fresh."""
    dropped = []
    for sp in required:
        v = (rot.get("veto") or {}).get(sp)
        if not v:
            continue
        for k in ("off", "max_hp"):
            if v.pop(k, None) is not None:
                dropped.append(f"{sp} {k}")
        if v.get("min_mana") and v["min_mana"] > MIN_MANA[0]:
            dropped.append(f"{sp} min_mana {v['min_mana']}")
            v["min_mana"] = MIN_MANA[0]
        if not v:
            rot["veto"].pop(sp)
    return dropped


def signature_bad(levels, cur, cand, required, rl):
    """Why a candidate breaks the signature rule against the current rules (None when it keeps it): a required spell's casts per kill
    at a level fall under CAST_KEEP of the current ones (or to none), or the tuning build's core share at 60 (its spec's rule `rl`)
    drops under min(min_share, current) - SHARE_TOL."""
    for sp in required:
        for L in levels:
            c0, c1 = SG.casts_per_kill(cur[L], sp), SG.casts_per_kill(cand[L], sp)
            if c0 > 0.05 and c1 < CAST_KEEP * c0:
                return f"{sp} {c0:.2f} -> {c1:.2f} casts per kill at {L}"
    if rl and 60 in cur:
        s0 = SG.core_share(cur[60].get("shares"), rl, cur[60].get("pet_sources") or ())
        s1 = SG.core_share(cand[60].get("shares"), rl, cand[60].get("pet_sources") or ())
        # the floor is absolute (coordinator, 2026-10-22: "main damage" is the user's choice): at or above min_share a candidate may not
        # drop below it; below it (the floor phase could not reach it) it may not lower the share by more than the noise
        if (s0 >= rl["min_share"] and s1 < rl["min_share"]) or (s0 < rl["min_share"] and s1 < s0 - SHARE_TOL):
            return f"core share {s0:.0%} -> {s1:.0%} at 60 (floor {rl['min_share']:.0%})"
    return None


def core_share_of(res, rl):
    if not rl or 60 not in res:
        return None
    return SG.core_share(res[60].get("shares"), rl, res[60].get("pet_sources") or ())


SHARE_STEP = 0.01   # the floor phase: a rule must raise the core share at 60 by this much (both seeds) to count as raising it


def floor_phase(pool, cls, spec, bid, levels, a, rot, base1, spells, mod_cls, main, req, rl, log):
    """Below a spec's min_share (the tuning build's spec), before any speed search: accept only rules that raise the core share at 60
    (by SHARE_STEP on seed 1 and on seed 2), the fastest such rule first, until the floor is met (2026-10-22, coordinator decision: the
    floor is absolute; a share above it earns nothing, the Frostfire lesson). A main attack that is not a core source may be gated
    here (the MAIN_SHARE protection is for the speed search). Returns (rules, base results, reached)."""
    floor = rl["min_share"]
    core = set(rl["core"])

    def is_core(sp):
        src = SG.source_of(sp)
        return src in core or any(src.startswith(c + " ") for c in core if c not in ("melee", "pet", "wand"))
    keep_main = {sp for sp in main if sp in req or is_core(sp)}
    for rnd in range(1, a.rounds + 1):
        s0 = core_share_of(base1, rl)
        if s0 is None or s0 >= floor:
            break
        cands = candidates(rot, spells, mod_cls, keep_main)
        res = evaluate(pool, cls, spec, bid, levels, [apply_change(rot, c) for c in cands], a.fights, 1)
        up = [i for i, r in enumerate(res) if (core_share_of(r, rl) or 0) >= s0 + SHARE_STEP and not cast_bad(levels, base1, r, req)]
        if not up:
            print(f"  floor round {rnd}: no rule raises {rl.get('note') or 'the'} core share above {s0:.0%} (floor {floor:.0%})", flush=True)
            break
        up.sort(key=lambda i: weighted({L: res[i][L]["time_per_kill"] for L in levels}))
        top = up[: a.top]
        conf = evaluate(pool, cls, spec, bid, levels, [rot] + [apply_change(rot, cands[i]) for i in top], a.confirm, 2)
        c0 = core_share_of(conf[0], rl) or 0
        ok = [(weighted({L: conf[k][L]["time_per_kill"] for L in levels}), i, k) for k, i in enumerate(top, start=1)
              if (core_share_of(conf[k], rl) or 0) >= c0 + SHARE_STEP and not cast_bad(levels, conf[0], conf[k], req)]
        if not ok:
            print(f"  floor round {rnd}: {len(top)} rules raised the share on seed 1, none on seed 2", flush=True)
            break
        t2, i, k = min(ok)
        ch = cands[i]
        s1, s2 = core_share_of(res[i], rl), core_share_of(conf[k], rl)
        log.append({"round": rnd, "phase": "floor", "change": describe(ch), "rule": list(ch), "share_seed1": round(s1, 4), "share_seed2": round(s2, 4),
                    "seconds_seed2": round(t2, 2), "seconds_before_seed2": round(weighted({L: conf[0][L]["time_per_kill"] for L in levels}), 2)})
        print(f"  floor round {rnd}: {describe(ch)}  (core share {s0:.0%} -> {s1:.0%} seed 1, {c0:.0%} -> {s2:.0%} seed 2; "
              f"{log[-1]['seconds_before_seed2']:.2f} -> {t2:.2f} s per kill)", flush=True)
        rot = apply_change(rot, ch)
        base1 = res[i]
    reached = (core_share_of(base1, rl) or 0) >= floor
    return rot, base1, reached


def cast_bad(levels, cur, cand, required):
    """The cast-floor half of signature_bad: a required spell's casts per kill falling under CAST_KEEP of the current rules'."""
    for sp in required:
        for L in levels:
            c0, c1 = SG.casts_per_kill(cur[L], sp), SG.casts_per_kill(cand[L], sp)
            if c0 > 0.05 and c1 < CAST_KEEP * c0:
                return True
    return False


def sig_factor(res, rl, build=None, spec_b=None, cls=None):
    """The tuning build's signature factor (2026-10-22): 0.5 while a required spell it can cast goes uncast at a level (signature.
    check_levels: under 0.5 casts per kill, or half what its cooldown allows), else 1, so the search prefers rules that cast the spec's
    required spells. The core share is a floor only (signature_bad): rewarding a higher share made the search cripple the rotation
    around the signature spell (Frostfire: never Fire Blast, Ice Lance gated, 20% slower for 7 points of share; a smoke test of
    2026-10-22). A build short of min_share is the build search's problem (fl_open_search's penalty), not the rotation's."""
    if not rl or not FS.enabled() or build is None or not cls:
        return 1.0
    v = SG.check_levels(cls, spec_b, build, res, "leveling", rl)
    return 0.5 if (v["uncast"] or v["missing_talents"]) else 1.0


def candidates(rot, spells, mod_cls, main=()):
    """Rule candidates. The main attacks (MAIN_SHARE) are never switched off, limited to a dying mob or held above more than the
    lowest mana share: a Balance druid without Starfire could not kill, and every fight ran to the timeout (a 9-hour search, 2026-09-28)."""
    out = []
    veto = rot.get("veto", {})
    for s in spells:
        if veto.get(s):
            out.append(("clear", s, None))
        if s not in main and not veto.get(s, {}).get("off"):
            out.append(("off", s, True))
        out += [("min_mana", s, x) for x in (MIN_MANA[:1] if s in main else MIN_MANA) if veto.get(s, {}).get("min_mana") != x]
        out += [("min_hp", s, x) for x in MIN_HP if veto.get(s, {}).get("min_hp") != x]
        if s not in main:
            out += [("max_hp", s, x) for x in MAX_HP if veto.get(s, {}).get("max_hp") != x]
    cur_d = rot.get("drink_below", mod_cls.drink_below or tables.DRINK_BELOW)
    cur_e = rot.get("eat_below", mod_cls.eat_below or tables.EAT_BELOW)
    out += [("drink_below", None, x) for x in DRINK if abs(x - cur_d) > 1e-9]
    out += [("eat_below", None, x) for x in EAT if abs(x - cur_e) > 1e-9]
    for k, vals in (getattr(mod_cls, "ROTATION_KNOBS", {}) or {}).items():
        cur = rot.get("knobs", {}).get(k, getattr(mod_cls, k, None))
        out += [("knob", k, v) for v in vals if v != cur]
    return out


def search(pool, cls, spec, bid, levels, a):
    mod_cls = getattr(__import__(FR.MODULES[cls][0]), FR.MODULES[cls][1])
    rot0 = {}
    if not a.fresh and FR.rotation_file(cls, spec).exists():
        rot0 = {k: v for k, v in json.load(open(FR.rotation_file(cls, spec), encoding="utf-8")).items() if k in ("veto", "drink_below", "eat_below", "knobs")}
    req = required_spells(cls, spec)
    b_ = FR.load_build(cls, bid)
    spec_b = FS.spec_for(cls, spec, FS.flat_of(b_))
    rl = SG.rule(cls, spec_b, "leveling") if FS.enabled() else None

    def wsig(res, levels, rl):
        return weighted({L: res[L]["time_per_kill"] for L in levels}) / sig_factor(res, rl, b_, spec_b, cls)
    flagged = sanitize(rot0, req)
    if flagged:
        print(f"  signature rule: the saved rules switched off or starved required spells ({', '.join(flagged)}): dropped (re-tune with --fresh)", flush=True)
    rot = copy.deepcopy(rot0)
    base1 = evaluate(pool, cls, spec, bid, levels, [rot], a.fights, 1)[0]
    spells = sorted({s for L in levels for s, n in base1[L]["casts"].items() if n and s not in ("wand", "Wand", "Melee", "Auto Shot", "Melee (off-hand)")})
    # the main attacks and the required signature spells of every spec that levels with this rotation (2026-10-22) are never switched
    # off, limited to a dying mob or held above more than the lowest mana share
    main = {s for L in levels for s, sh in base1[L].get("shares", {}).items() if sh >= MAIN_SHARE} | set(req)
    if req:
        print(f"  signature spells kept: " + ", ".join(f"{s} ({'/'.join(v)})" for s, v in sorted(req.items())), flush=True)
    print(f"== {cls} {spec} ({bid}): levels {levels}, {len(spells)} spells cast; time/kill " + ", ".join(f"L{L} {base1[L]['time_per_kill']:.1f}s" for L in levels)
          + f" (weighted {weighted({L: base1[L]['time_per_kill'] for L in levels}):.2f}s)", flush=True)
    log = []
    reached = None
    if rl and rl.get("min_share") and (core_share_of(base1, rl) or 0) < rl["min_share"]:
        print(f"  core share at 60 {core_share_of(base1, rl):.0%} under {spec_b}'s floor {rl['min_share']:.0%} ({', '.join(rl['core'])}): floor phase first", flush=True)
        rot, base1, reached = floor_phase(pool, cls, spec, bid, levels, a, rot, base1, spells, mod_cls, main, req, rl, log)
        print(f"  floor phase: " + ("floor reached" if reached else f"floor NOT reached ({core_share_of(base1, rl):.0%})"), flush=True)
    for rnd in range(1, a.rounds + 1):
        cands = candidates(rot, spells, mod_cls, main)
        res = evaluate(pool, cls, spec, bid, levels, [apply_change(rot, c) for c in cands], a.fights, 1)
        w0 = wsig(base1, levels, rl)
        bad = {i: signature_bad(levels, base1, r, req, rl) for i, r in enumerate(res)} if FS.enabled() else {}
        nbad = sum(1 for v in bad.values() if v)
        if nbad:
            print(f"  round {rnd}: {nbad} candidates break the signature rule (e.g. {describe(cands[next(i for i, v in bad.items() if v)])}: "
                  f"{next(v for v in bad.values() if v)})", flush=True)
        scored = sorted(((wsig(r, levels, rl) / w0, i) for i, r in enumerate(res) if not bad.get(i)), key=lambda x: x[0])
        top = [(sc, i) for sc, i in scored if sc < 1 - a.screen_gain][: a.top]
        if not top:
            print(f"  round {rnd}: {len(cands)} candidates, none ahead on seed 1 (best {1 - scored[0][0]:+.2%}: {describe(cands[scored[0][1]])})" if scored else "  no candidates", flush=True)
            break
        rots = [rot] + [apply_change(rot, cands[i]) for _, i in top]
        conf = evaluate(pool, cls, spec, bid, levels, rots, a.confirm, 2)
        w2 = wsig(conf[0], levels, rl)
        best = None
        for k, (sc1, i) in enumerate(top, start=1):
            sc2 = wsig(conf[k], levels, rl) / w2
            if FS.enabled() and signature_bad(levels, conf[0], conf[k], req, rl):
                continue   # it broke the signature rule on seed 2
            if best is None or sc2 < best[0]:
                best = (sc2, sc1, i)
        if best is None or best[0] > 1 - a.min_gain:
            if best is None:
                print(f"  round {rnd}: every candidate ahead on seed 1 broke the signature rule on seed 2", flush=True)
                break
            print(f"  round {rnd}: {len(cands)} candidates, {len(top)} ahead on seed 1, none confirmed on seed 2 (best {1 - best[0]:+.2%}: {describe(cands[best[2]])})", flush=True)
            break
        sc2, sc1, i = best
        ch = cands[i]
        log.append({"round": rnd, "change": describe(ch), "rule": list(ch), "gain_seed1": 1 - sc1, "gain_seed2": 1 - sc2})
        print(f"  round {rnd}: {describe(ch)}  ({1 - sc1:+.2%} seed 1, {1 - sc2:+.2%} seed 2 faster per kill"
              + (", signature-weighted" if FS.enabled() and rl else "") + f"; {len(cands)} candidates)", flush=True)
        rot = apply_change(rot, ch)
        base1 = res[i]
    # final check on a third seed
    saved = None
    if a.fresh and FR.rotation_file(cls, spec).exists():   # 2026-10-27 audit (unrestricted mage Fire: a --fresh re-tune that found nothing
        saved = {k: v for k, v in json.load(open(FR.rotation_file(cls, spec), encoding="utf-8")).items() if k in ("veto", "drink_below", "eat_below", "knobs")}
        if sanitize(saved, req):   # wrote the hand-written rotation over rules 2.5% faster): the saved rules compete in the final check
            saved = None
    fin = evaluate(pool, cls, spec, bid, levels, [rot0, rot] + ([saved] if saved is not None else []), a.confirm, 3)
    wb, wa = weighted({L: fin[0][L]["time_per_kill"] for L in levels}), weighted({L: fin[1][L]["time_per_kill"] for L in levels})
    if saved is not None:
        ws = weighted({L: fin[2][L]["time_per_kill"] for L in levels})
        if ws < wa:
            print(f"  the saved rules are faster on seed 3 ({ws:.2f}s against {wa:.2f}s): kept", flush=True)
            rot, wa, fin = saved, ws, [fin[0], fin[2]]
            log.append({"round": "final", "change": "kept the saved rules (faster on seed 3 than the fresh re-tune)", "rule": [], "gain_seed1": None, "gain_seed2": None})
    per_level = {L: {"before": fin[0][L]["time_per_kill"], "after": fin[1][L]["time_per_kill"], "deaths_before": fin[0][L]["deaths_per_100"],
                     "deaths_after": fin[1][L]["deaths_per_100"]} for L in levels}
    print(f"  final (seed 3, {a.confirm} fights): weighted time/kill {wb:.2f}s -> {wa:.2f}s ({1 - wa / wb:+.2%} faster); "
          + ", ".join(f"L{L} {v['before']:.1f}->{v['after']:.1f}s" for L, v in per_level.items()), flush=True)
    sig = {"required": sorted(req), "build_spec": spec_b, "dropped_saved_rules": flagged,
           "core_share_before": core_share_of(fin[0], rl), "core_share_after": core_share_of(fin[1], rl),
           "min_share": (rl or {}).get("min_share"), "floor_reached": reached} if req or rl else None
    if rl:
        print(f"  core share at 60 (seed 3): {core_share_of(fin[0], rl):.0%} -> {core_share_of(fin[1], rl):.0%} (floor {rl['min_share']:.0%})", flush=True)
    return dict(rot, **{"class": cls, "spec": spec, "build": bid, "levels": levels, "date": datetime.date.today().isoformat(), "signature": sig,
                        "fights": a.fights, "confirm": a.confirm, "changes": log, "weighted_before": wb, "weighted_after": wa, "per_level": per_level})


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("cls", nargs="?")
    ap.add_argument("--spec")
    ap.add_argument("--build", help="with --spec: tune on this build (a spec model no pipeline names yet, e.g. the healer leveling specs)")
    ap.add_argument("--all", action="store_true")
    ap.add_argument("--rounds", type=int, default=12)
    ap.add_argument("--fights", type=int, default=600, help="fights per level and candidate on seed 1")
    ap.add_argument("--confirm", type=int, default=3000, help="fights per level on the confirmation seed 2 (and the final check on seed 3)")
    ap.add_argument("--top", type=int, default=5)
    ap.add_argument("--screen-gain", type=float, default=0.003)
    ap.add_argument("--min-gain", type=float, default=0.004, help="time per kill a rule must save on seed 2 to be kept")
    ap.add_argument("--jobs", type=int, default=max(1, (os.cpu_count() or 4) - 2))
    ap.add_argument("--fresh", action="store_true", help="start from the hand-written rotation, not the saved rules")
    ap.add_argument("--write", action="store_true")
    ap.add_argument("--check-rules", action="store_true", help="list the saved rules files that switch off or starve a required "
                    "signature spell (signature_spells.json) and exit: those need a re-tune with --fresh")
    a = ap.parse_args()
    if a.check_rules:
        for p in sorted(FR.ROTATIONS.glob("*.json")):
            rec = json.load(open(p, encoding="utf-8"))
            cls_, spec_ = rec.get("class"), rec.get("spec")
            if not cls_ or not spec_ or (a.cls and cls_ != a.cls):
                continue
            req = required_spells(cls_, spec_)
            bad = sanitize(copy.deepcopy({"veto": rec.get("veto") or {}}), req)
            print(f"{p.name}: " + (f"RE-TUNE (--fresh): {', '.join(bad)}" if bad else "ok") + (f"  [required: {', '.join(sorted(req))}]" if req else ""))
        return
    classes = list(FR.MODULES) if a.all else [a.cls]
    with multiprocessing.Pool(a.jobs, initializer=_init) as pool:
        for cls in classes:
            tl, levels = targets(cls)
            if a.build and a.spec:   # a spec string outside the class pipeline (2026-09-30: the new leveling rotations)
                tl = [(a.spec, a.build)]
            for spec, bid in tl:
                if a.spec and spec != a.spec:
                    continue
                rec = search(pool, cls, spec, bid, levels, a)
                if a.write:
                    FR.ROTATIONS.mkdir(exist_ok=True)
                    p = FR.rotation_file(cls, spec)
                    if not rec["changes"] and not p.exists():
                        print(f"  no rule beat the hand-written rotation: nothing written", flush=True)
                        continue
                    p.write_text(json.dumps(rec, indent=1), encoding="utf-8")
                    print(f"  wrote {p.relative_to(ROOT)}", flush=True)


if __name__ == "__main__":
    main()
