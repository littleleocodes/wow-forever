"""Splitting a talent's effect entries for a calibration without losing or duplicating values.

A calibration (fightlab/calibrate.py, raidsim/calibrate.py, heallab/calibrate.py) fits one spec model's values in some
modes (`fit_modes`: the leveling profiles, raid, tank or heal). Every effect that applies to that model in those modes is split
into
  * the fitted copy: modes = fit_modes, specs = [model]; copies of the same channel, scope and conditions are merged into one,
  * what the effect keeps for that model in its other modes (its modes minus fit_modes, specs = [model]),
  * what it keeps for every other model: its original modes (an untagged effect keeps an untagged copy for the other modes
    and a copy tagged with the other models for the fitted modes).
Nothing that applied before the split stops applying afterwards, except the fitted model's values in the fitted modes, which
the fitted copy replaces. Until 2026-09-27 the three calibrations each had their own split that dropped the fitted model's
other modes, narrowed a generic "leveling" effect to the fitted leveling profile, and appended the same copy more than once
(Flurry lost its leveling-st value for every warrior model; 110 duplicate entries). `dedupe` repairs such entries.
"""
import json

# every concrete mode an untagged effect applies to (profile ids of the leveling mode, plus the other modes)
ALL_MODES = ["raid", "leveling-st", "solo-60", "leveling-aoe", "heal", "tank", "pvp"]
LEVELING = ["leveling-st", "solo-60", "leveling-aoe"]
MULTIPLICATIVE = ("dmg", "heal", "threat_up")   # the scorer multiplies these per effect; everything else adds
NO_FIT = ("utility", "enable", "disable")         # raid-buff values and source switches are never scaled by a fit
CONDITIONS = ("requires", "requires_not", "kind")


def expand_modes(modes):
    """Concrete modes of an effect: none = all; "leveling" = the three leveling profiles; "raid-heal" = heal."""
    if not modes:
        return list(ALL_MODES)
    out = []
    for m in modes:
        for x in (LEVELING if m == "leveling" else ["heal"] if m == "raid-heal" else [m]):
            if x not in out:
                out.append(x)
    return out


def applies(e, fit_modes, spec_id, no_fit=NO_FIT):
    return (e.get("channel") not in no_fit and (not e.get("specs") or spec_id in e["specs"])
            and any(m in fit_modes for m in expand_modes(e.get("modes"))))


def _untagged(e):
    return {k: v for k, v in e.items() if k != "specs"}


def _values(e):
    if e.get("values") is not None:
        return list(e["values"])
    if "per_rank" in e:
        return [round(e["per_rank"] * r, 6) for r in range(1, 6)]
    return []


def _key(e):
    """Effects with the same key apply in exactly the same situations and can be merged."""
    return json.dumps([e.get("channel"), e.get("scope"), sorted(e.get("modes") or []), sorted(e.get("specs") or [])]
                      + [e.get(c) for c in CONDITIONS], sort_keys=True)


def _combine(channel, a, b):
    n = max(len(a), len(b))
    a = a + [a[-1]] * (n - len(a)) if a else [0.0] * n
    b = b + [b[-1]] * (n - len(b)) if b else [0.0] * n
    if channel in MULTIPLICATIVE:
        return [round((1 + x) * (1 + y) - 1, 6) for x, y in zip(a, b)]
    return [round(x + y, 6) for x, y in zip(a, b)]


def merge_same(effects):
    """One effect per key: values combined the way the scorer would have applied the separate copies."""
    out, index = [], {}
    for e in effects:
        k = _key(e)
        if k in index:
            first = out[index[k]]
            first["values"] = _combine(first.get("channel"), _values(first), _values(e))
            first.pop("per_rank", None)
        else:
            index[k] = len(out)
            out.append(dict(e))
    return out


def split(effects, fit_modes, spec_id, other_specs, no_fit=NO_FIT):
    """(fit, rest) for one calibration. `effects` are the entry's effects (per_rank or values)."""
    fit_modes = list(fit_modes)
    fit, rest = [], []
    for e in effects:
        e = dict(e)
        if not applies(e, fit_modes, spec_id, no_fit):
            rest.append(e)
            continue
        modes = expand_modes(e.get("modes"))
        remaining = [m for m in modes if m not in fit_modes]
        fit.append(dict(e, modes=fit_modes, specs=[spec_id]))
        if e.get("specs"):
            others = [s for s in e["specs"] if s != spec_id]
            if others:
                rest.append(dict(e, specs=others))                        # other models: unchanged
            if remaining:
                rest.append(dict(e, modes=remaining, specs=[spec_id]))    # this model, other modes
        else:
            if remaining:
                rest.append(_untagged(dict(e, modes=remaining)))          # everyone, other modes
            fitted_here = [m for m in modes if m in fit_modes]
            if other_specs and fitted_here:
                rest.append(dict(e, modes=fitted_here, specs=list(other_specs)))   # other models, fitted modes
    return merge_same(fit), merge_same(rest)


def uses_fallback(effects, tokens, spec_id):
    """True when model.effects_for would score this talent for spec_id from its parsed tooltip effects in these modes: some effect
    applies in the modes, none of them to this model."""
    def mode_ok(e):
        m = e.get("modes")
        return not m or any(t in m for t in tokens)
    return any(mode_ok(e) for e in effects) and not any(mode_ok(e) and (not e.get("specs") or spec_id in e["specs"]) for e in effects)


def seed_from_parsed(fit, effects, parsed, fit_modes, tokens, spec_id, no_fit=NO_FIT):
    """The effects to fit: `fit` from split(), or, when it is empty because the model scores the talent through the parsed
    fallback, the parsed effects tagged for this model and these modes."""
    if fit or not parsed or not uses_fallback(effects, tokens, spec_id):
        return fit
    return merge_same([dict(e, modes=list(fit_modes), specs=[spec_id]) for e in parsed if e.get("channel") not in no_fit])


def reseed_zero(fit, effects, parsed, fit_modes, spec_id, no_fit=NO_FIT):
    """The effects to fit when every fitted value is zero but the lab measures the talent. A fit scales values (0 x k = 0), so a
    talent zeroed once (the fully buffed raid fit left Frost Channeling, Arcane Meditation and Inner Focus at 0 for their raid
    models; on the training dummy the simulator measures 2-7% for them, 2026-09-27) could never come back. The seed is the talent's
    own non-zero values for this model in its other modes (hand-entered or fitted: Arcane Concentration's 2% per rank, where the
    parser read the free spell's 100% at every rank), else the parsed tooltip effects; one copy per channel and scope (not summed),
    tagged for the fitted modes and this model. The fit then scales it to the measurement."""
    if any(v for e in fit for v in _values(e)):
        return fit
    for src in ([e for e in effects if not e.get("specs") or spec_id in e["specs"]], parsed or []):
        seeds, seen = [], set()
        for e in src:
            if e.get("channel") in no_fit or not any(_values(e)):
                continue
            k = json.dumps([e.get("channel"), e.get("scope")] + [e.get(c) for c in CONDITIONS], sort_keys=True)
            if k in seen:
                continue
            seen.add(k)
            seeds.append(dict(e, modes=list(fit_modes), specs=[spec_id]))
        if seeds:
            return merge_same(seeds)
    return fit


def dedupe(effects):
    """Repair an entry written by the old splits: exact duplicates of a single-model copy were fitted together (a calibration
    scaled every copy it saw), so they merge into one with the combined value; exact duplicates of a copy for several models
    or none were never fitted as a pair, so the extra copies are dropped. Returns (effects, merged, dropped)."""
    out, seen, merged, dropped = [], {}, 0, 0
    for e in effects:
        sig = json.dumps({k: v for k, v in e.items() if k not in ("source",)}, sort_keys=True)
        if sig not in seen:
            seen[sig] = len(out)
            out.append(dict(e))
            continue
        first = out[seen[sig]]   # keyed by the original signature, so a third copy merges too
        if first.get("specs") and len(first["specs"]) == 1:
            first["values"] = _combine(first.get("channel"), _values(first), _values(e))
            first.pop("per_rank", None)
            merged += 1
        else:
            dropped += 1
    return out, merged, dropped


# ------------------------------------------------------------------ provenance sentences in notes (audit 2026-10-18, row 44)
# Each calibration appends one sentence to an entry's or a model's note. Until 2026-10-18 every writer kept only the note text before
# its own marker, so a fit dropped every sentence after its marker (other models' raid fits, the "Raid sim shares" sentence after a
# fight-lab one: 110 entries lost a "Raid sim calibration" line), and the leveling-aoe fit overwrote the leveling-st one. Sentences
# now carry a tag naming what they fit ("Fight lab calibration [shadow-dps, leveling-aoe] (...)"), and a writer replaces only the
# sentences with its own marker and tag.
NOTE_MARKERS = (" Fight lab calibration", " Fight lab speed", " Raid sim calibration", " Raid sim shares", " Classic raid sim calibration",
                " Classic raid sim shares", " Healer lab calibration", " Healer lab shares")


def _segments(note):
    """note -> (head, [segment, ...]): the text before the first marker and each marker's sentence up to the next marker."""
    import re
    rx = re.compile("|".join(re.escape(m) for m in NOTE_MARKERS))
    pos = [m.start() for m in rx.finditer(note)]
    if not pos:
        return note, []
    return note[:pos[0]], [note[a:b] for a, b in zip(pos, pos[1:] + [len(note)])]


def segment_key(seg):
    """(marker, tag or None) of a segment."""
    import re
    mk = max((m for m in NOTE_MARKERS if seg.startswith(m)), key=len)
    m = re.match(re.escape(mk) + r" \[([^\]]+)\]", seg)
    return mk, (m.group(1) if m else None)


def set_sentence(note, marker, text, tag=None, drop_untagged=None):
    """The note with every sentence of `marker` and `tag` replaced by `text` (a full sentence starting with the marker, appended at the
    end). Untagged old sentences of the marker are dropped when `drop_untagged(segment)` says they describe the same fit (None: drop
    them when no tag is given)."""
    head, segs = _segments(note or "")
    keep = []
    for s in segs:
        mk, tg = segment_key(s)
        if mk == marker and (tg == tag or (tg is None and (drop_untagged(s) if drop_untagged else tag is None))):
            continue
        keep.append(s)
    return (head.rstrip() + "".join(keep) + " " + text.strip()).strip()


# ------------------------------------------------------------------ dead scopes (audit 2026-10-18, row 47)
SOURCE_CHANNELS = ("dmg", "heal", "crit", "crit_bonus", "hit", "haste", "cast_time", "cooldown", "resource_cost", "threat_up")


def dead_scopes(effects, model):
    """Effects that can never score for this spec model: a source-scoped channel whose scope matches no source's tags (Blade Flurry's
    dmg ["aoe"] had been fitted to 1.5 with no source tagged aoe), or a mana_cost scope with no `mana_share` key. A fit scales them
    without moving the score, so the calibrations refuse them."""
    tags = set()
    for s in model.get("sources", []):
        tags |= set(s.get("tags", []))
        if "pet" not in s.get("tags", []):
            tags.add("all")
    ms = set(model.get("mana_share", {}))
    out = []
    for e in effects:
        ch, scope = e.get("channel"), e.get("scope") or []
        if not any(_values(e)):
            continue
        if ch in SOURCE_CHANNELS and not any(t in tags for t in scope):
            out.append(e)
        elif ch == "mana_cost" and not any(t in ms or t == "all" and "all" in ms for t in scope):
            out.append(e)
    return out
