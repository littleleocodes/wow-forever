"""What a held talent keeps legal (2026-11-21, the audit session's rule for the play checks and the filler passes).

A gate is a talent the build cannot drop. There are two kinds, and they are judged differently:
- a PREREQUISITE: another held talent requires this one by name (Bane of Havoc for Incinerate). It can be nowhere else, so its point is
  the price of the talent that needs it;
- a TIER POINT: one of the points a deeper talent's tier needs in the rows below it. Any legal talent in those rows can hold it, so a
  point that does nothing there is not excused by "gate": it must be the most useful legal holder of that tier point (the filler
  pass's record of the homes it tried: "no better home"), or move.

    gate_kind(trees, state, talent, ranks=None) -> None | "prerequisite of X[, Y]" | "tier point for X (tier N)" | another error
"""
import re

import validate_builds as VB

_REQ = re.compile(r": (.+?) requires (.+?) \d+, have \d+")
_TIER = re.compile(r": (.+?) \(tier (\d+)\) needs \d+ points in (.+?) below it")


def gate_kind(trees, state, talent, ranks=None):
    """state {tree: {talent: rank}}; `ranks` of the talent's ranks go (default all). None when the build stays legal without them."""
    st = {t: dict(v) for t, v in state.items()}
    for t, v in st.items():
        if talent in v:
            left = v[talent] - (ranks if ranks else v[talent])
            if left > 0:
                v[talent] = left
            else:
                del v[talent]
    errors = []
    VB.check_state(trees, st, "x", errors)
    if not errors:
        return None
    req = sorted({m.group(1) for e in errors for m in [_REQ.search(e)] if m and m.group(2) == talent})
    if req:
        return "prerequisite of " + ", ".join(req)
    tier = [m.groups() for e in errors for m in [_TIER.search(e)] if m]
    if tier:
        return f"tier point for {tier[0][0]} (tier {tier[0][1]})"
    return errors[0].split(": ", 1)[-1]


def state_of(allocation):
    """{tree: {talent: rank}} from a builds-JSON allocation {tree: [[talent, rank], ...]}."""
    return {t: {n: r for n, r in v if r} for t, v in allocation.items()}


def is_tier(kind):
    return bool(kind) and kind.startswith("tier point")


def is_prerequisite(kind):
    return bool(kind) and kind.startswith("prerequisite")
