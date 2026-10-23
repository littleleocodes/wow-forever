"""Signature spells in the fight lab's leveling searches (user rule 2026-10-22: "make sure that the specs we're testing are actually using
the spells for that spec, or else it's pointless ... The specs should use the spells that make that spec, that spec. Especially the hybrid
ones."; strictness "main damage": the rule in `_reference/data/signature_spells.json`, read through `_reference/data/signature.py`).

What the leveling tools share:
- `spec_for(cls, rot, flat)`: the spec a build plays in a fight-lab rotation (by its split; a rotation built only for one hybrid,
  spec_modes.HYBRID_LEVELING_ROTATION, files the hybrid's trees under the hybrid: a 0/21/30 build in frostfire-leveling is Frostfire);
- `leveling_space(space, cls, rot)`: an ml_talents.Space (any split) restricted to the builds that may level with `rot`
  (spec_modes.leveling_rotation_ok) and keeping, per build, the talents that grant its spec's required leveling spells;
- `check(cls, rot, flat, level, result)`: one fight-lab result against the build's spec rule at one level (required spells cast from
  the level they are learned; the core share only at level 60, where the rule applies);
- `penalty(chk)`: the factor the searches put on a failing build's kills per hour (core share / min_share, halved when a required spell
  goes uncast or its talent is missing), so they look for the fastest build that plays its spec (fl_open_search._ttk);
- `check_build(pool, cls, rot, build)`: levels 20-60 of a build with its order, the record `fl_open_search` keeps as `signature` and
  `open_builds.py` reads; `qualifying(...)` for the race picks.
WOW_FOREVER_SIGNATURE=0 switches the leveling checks off too (as raidsim/raid_signature.py).
"""
import datetime
import os
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
DATA = HERE.parent
sys.path[:0] = [str(HERE), str(DATA)]
import run as FR  # noqa: E402
import signature as SG  # noqa: E402
import spec_modes as SM  # noqa: E402

LEVELS = (20, 30, 40, 50, 60)
CHECK_FIGHTS, CHECK_SEED = 600, 4


def enabled():
    return os.environ.get("WOW_FOREVER_SIGNATURE", "1") not in ("0", "", "off", "false")


def flat_of(x):
    return SG.held(x) if isinstance(x, dict) else {}


def hybrids_of(cls, rot):
    return {h for (c, h), r in SM.HYBRID_LEVELING_ROTATION.items() if c == cls and r == rot}


def hybrid_only(cls, rot):
    """The hybrid a rotation is built for alone (no tree levels with it), else None."""
    hy = hybrids_of(cls, rot)
    return next(iter(hy)) if len(hy) == 1 and not SM.leveling_rotation_trees(cls).get(rot) else None


def classify(cls, flat, two=False):
    pts = {t: 0 for t in SM.trees(cls)}
    tree_of = {}
    import json
    for tr in json.load(open(DATA / "forever-talents" / f"{cls}.json", encoding="utf-8"))["trees"]:
        for t in tr["talents"]:
            tree_of[t["name"]] = tr["name"]
    for n, r in flat.items():
        if n in tree_of:
            pts[tree_of[n]] += r
    top = sorted(pts, key=lambda t: -pts[t])
    pair = "Hybrid " + "/".join(t for t in pts if t in top[:2])
    if two:   # (spec, the hybrid of its two biggest trees)
        return (top[0] if pts[top[0]] >= SM.SPEC_POINTS else pair), pair
    if pts[top[0]] >= SM.SPEC_POINTS:
        return top[0]
    return pair


_CLS = {}


def spec_for(cls, rot, flat):
    key = (cls, rot, tuple(sorted(flat.items())))
    if key not in _CLS:
        spec, pair = classify(cls, flat, two=True)
        h = hybrid_only(cls, rot)
        if h and pair == h:   # the hybrid's rotation files a split of its two trees under it (a 0/21/30 Frostfire), not 17/0/34 Frost
            spec = h
        if len(_CLS) > 50000:
            _CLS.clear()
        _CLS[key] = spec
    return _CLS[key]


def allowed(cls, rot, flat):
    return SM.leveling_rotation_ok(cls, spec_for(cls, rot, flat), rot)


def leveling_space(space, cls, rot):
    """Restrict an any-split Space to the builds that may level with `rot`, with the leveling signature talents per build."""
    trees_ = SM.leveling_rotation_trees(cls).get(rot) or set()
    space.allow_trees = set(trees_) or hybrids_of(cls, rot) or None
    space.sig = {s: set(SG.granting_talents(cls, (SG.rule(cls, s, "leveling") or {}).get("required", []))) for s in SG.specs_of(cls)} if enabled() else {}
    space.sig = {s: t for s, t in space.sig.items() if t}
    base_allowed = type(space).allowed.__get__(space)
    space.spec_for = lambda flat: spec_for(cls, rot, flat)
    space.allowed = lambda flat: base_allowed(flat) and allowed(cls, rot, flat)
    space.signature_rotation = rot
    return space


def check(cls, rot, flat, level, result, order=None, spec=None):
    """One level's result against the rule of the build's spec (`spec`, default spec_for; None when the spec has no rule or the checks
    are off)."""
    if not enabled():
        return None
    spec = spec or spec_for(cls, rot, flat)
    rl = SG.rule(cls, spec, "leveling")
    if not rl:
        return None
    build = {"allocation": flat, "order": order or []}
    per = {int(level): result}
    v = SG.check_levels(cls, spec, build, per, "leveling", rl)
    if int(level) < 60:   # the core share is the level-60 rule
        v["ok"] = not v["missing_talents"] and not v["uncast"]
        v["core_share_checked"] = False
    v["spec"] = spec
    return v


def penalty(v):
    if not v or v.get("ok"):
        return 1.0
    f = 1.0
    if v.get("core_share_checked", True) and v.get("core_share") is not None and v.get("min_share"):
        f = min(1.0, v["core_share"] / v["min_share"])
    if v.get("uncast") or v.get("missing_talents"):
        f *= 0.5
    return max(0.05, f)


def _full(job):
    cls, rot, alloc, level, fights, seed = job
    try:
        r = FR.simulate(cls, alloc, level, rot, fights, seed, 0)
    except Exception as e:   # noqa: BLE001
        print(f"  signature check error {type(e).__name__}: {e}", flush=True)
        return None
    return {k: r.get(k) for k in ("time_per_kill", "kills", "shares", "casts", "pet_sources")}


def summary(cls, rot, build, per, spec=None):
    """The check of a build's levels 20-60 under the rule of `spec` (default: the spec it plays in `rot`, spec_for)."""
    flat = flat_of(build)
    spec = spec or spec_for(cls, rot, flat)
    rl = SG.rule(cls, spec, "leveling")
    v = SG.check_levels(cls, spec, build, per, "leveling", rl) if rl and enabled() else None
    out = {"spec": spec, "rotation": rot, "date": datetime.date.today().isoformat(), "fights": CHECK_FIGHTS,
           "split": "/".join(str(x) for x in SM.tree_points(cls, {"allocation": SG_alloc(cls, flat)}).values())}
    if v is None:
        out.update(ok=True, verdict="no rule")
        return out
    out.update(ok=v["ok"], verdict=SG.verdict_text(v), core_share=round(v["core_share"] or 0.0, 4), min_share=v["min_share"],
               required=rl["required"], core=rl["core"], missing_talents=v["missing_talents"], uncast=v["uncast"],
               casts={s: {str(L): round(SG.casts_per_kill(r, s), 2) for L, r in per.items()} for s in rl["required"]})
    return out


def SG_alloc(cls, flat):
    import json
    out = {}
    for tr in json.load(open(DATA / "forever-talents" / f"{cls}.json", encoding="utf-8"))["trees"]:
        out[tr["name"]] = [[t["name"], flat[t["name"]]] for t in tr["talents"] if flat.get(t["name"])]
    return out


def check_builds(pool, cls, rot, builds, fights=CHECK_FIGHTS, seed=CHECK_SEED, levels=LEVELS, spec=None):
    """[summary] for {allocation, order} builds at levels 20-60 (the allocation at each level from the order)."""
    jobs = [(cls, rot, FR.allocation_at(b, L), L, fights, seed) for b in builds for L in levels]
    res = pool.map(_full, jobs, chunksize=1) if pool is not None else [_full(j) for j in jobs]
    out = []
    for i, b in enumerate(builds):
        per = {L: res[i * len(levels) + k] for k, L in enumerate(levels)}
        if any(v is None for v in per.values()):
            out.append({"ok": False, "verdict": "the fight lab could not run it", "rotation": rot})
            continue
        out.append(summary(cls, rot, b, per, spec))
    return out


def check_build(pool, cls, rot, build, **kw):
    return check_builds(pool, cls, rot, [build], **kw)[0]


def qualifying(pool, cls, rot, builds, **kw):
    """[(ok, summary)] per build: the race picks only among the builds that pass (all of them when the checks are off)."""
    if not enabled():
        return [(True, None) for _ in builds]
    return [(s.get("ok", False), s) for s in check_builds(pool, cls, rot, builds, **kw)]


def rules_fingerprint(cls, rot):
    import hashlib
    p = FR.rotation_file(cls, rot)
    rules = p.read_text(encoding="utf-8") if p.exists() else ""
    return hashlib.sha1(rules.encode("utf-8")).hexdigest()[:12]


def build_fingerprint(cls, build, rot):
    import hashlib
    import json
    key = json.dumps([sorted(flat_of(build).items()), build.get("order") or [], rot, rules_fingerprint(cls, rot)], sort_keys=True)
    return hashlib.sha1(key.encode("utf-8")).hexdigest()[:12]
