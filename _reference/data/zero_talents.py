"""The one source for a page's "points that do nothing" (2026-11-21, the audit session's B13: the Marksmanship page listed Trueshot Aura as
doing nothing while its removal changes the result; the line had come from page_lint.dead_talents, a reading of the tooltips against
the page's text). A talent does nothing only when a removal run says so:
- raid builds: the raid play check's zero talents (raidsim/play-check.json: the talent's removal leaves the full-raid DPS the same to
  the cent), with the check's reason for each (a gate's kind, a recorded filler, a utility tag, the raid's own buff);
- leveling builds: the leveling filler pass's record made on the build's own order (fightlab/filler/<class>-<slug>.json, its
  `no_better_home` entries whose removal is exact, with the gate's kind).

    raid(cls, bid, entry=None) -> {talent: why}
    leveling(cls, slug, order) -> {talent: why}
"""
import json
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent


def raid(cls, bid, entry=None):
    p = HERE / "raidsim" / "play-check.json"
    try:
        rec = json.load(open(p, encoding="utf-8")).get(cls) or {}
    except (OSError, ValueError):
        return {}
    ents = [entry] if entry in rec else list(rec)
    out = {}
    for e in ents:
        for line in ((rec.get(e) or {}).get("builds") or {}).get(bid, {}).get("zero_talents") or []:
            t, _, why = line.partition(": ")
            out.setdefault(re.sub(r" \d+$", "", t), why)
        if out and entry in rec:
            break
    return out


def filler_paths(cls, spec=None, slug=None, dry=False):
    """The leveling filler pass's record files that can hold a spec's record: fl_filler_pass.py names them after the spec's tree name
    ("hybrid-protection-retribution"); a page slug ("prot-ret") is tried too. With dry, the dry run's records instead."""
    names = []
    if spec:
        names.append(spec.lower().replace("/", "-").replace(" ", "-"))
        try:
            import spec_modes as SM
            names.append(SM.spec_slug(cls, spec))
        except Exception:   # noqa: BLE001
            pass
    if slug:
        names.append(slug)
    ext = ".dry.json" if dry else ".json"
    out = []
    for n in names:
        p = HERE / "fightlab" / "filler" / f"{cls}-{n}{ext}"
        if p not in out:
            out.append(p)
    return out


def filler_record(cls, order, spec=None, slug=None, build=None, dry=False):
    """The filler record made on this order: by the spec's names, else (a page slug that names no record) the one whose build is
    `build`. None when there is none."""
    paths = filler_paths(cls, spec, slug, dry)
    if build:
        paths += sorted(p for p in (HERE / "fightlab" / "filler").glob(f"{cls}-*{'.dry.json' if dry else '.json'}")
                        if p not in paths and (dry or not p.name.endswith(".dry.json")) and not p.name.endswith(".dry2.json"))
    for p in paths:
        try:
            x = json.load(open(p, encoding="utf-8"))
        except (OSError, ValueError):
            continue
        if x.get("final_order") != order:
            continue
        if build and x.get("build") not in (None, build):
            continue
        return x
    return None


def leveling(cls, slug, order, spec=None, build=None):
    out = {}
    if not (slug or spec or build):
        return out
    for x in [filler_record(cls, order, spec=spec, slug=slug, build=build)]:
        if not x:
            continue
        for t, e in (x.get("no_better_home") or {}).items():
            if e.get("exact", e.get("kind") != "zero point"):
                out[t] = e.get("kind") or "zero point"
    return out
