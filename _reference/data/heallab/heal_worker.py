"""Worker processes for searches that measure many healer builds (deep_heal.py): one build's capacity with its spread.

Kept apart from the search so the spawned processes import only the healer lab, never the raid tools.
"""
import importlib
import math
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import engine as E  # noqa: E402
import tables as T  # noqa: E402

CLASSES = {"priest": "priest", "paladin": "paladin", "shaman": "shaman", "druid": "druid"}
_DEFAULT_GEAR = {k: dict(v) for k, v in T.HEALER_GEAR.items()}   # the lab's assumed gear, restored for jobs without a gear override


def init(cls):
    """Each worker applies the class's tuned heal-choice settings once (heallab/rotations/<class>-<spec>.json)."""
    T.apply_rotation(cls)


def capacity(job):
    """(capacity, spread) of one build: the tail mean engine.capacity uses, and the spread scaled so that spread / sqrt(seeds) is the
    tail mean's standard error (the convention ml_talents' races use)."""
    cls, alloc, seeds, steps = job
    mod = importlib.import_module(CLASSES[cls])
    cs = E.capacities(mod.Healer(alloc), seeds, steps)
    k = max(1, int(round(2 * T.DEATH_RUNS_OK * len(cs))))
    tail = cs[:k]
    mean = sum(tail) / k
    var = sum((x - mean) ** 2 for x in tail) / max(1, k - 1)
    return mean, math.sqrt(var) * math.sqrt(len(seeds) / k)


def seed_caps(job):
    """Per-seed capacities in seed order (unsorted, so two gear sets can be paired seed by seed) with a gear override: (cls, alloc,
    gear stats or None for the lab's assumed gear, seeds, steps). heal_gear.py's stat weights and set checks (2026-10-15)."""
    cls, alloc, gear, seeds, steps = job
    T.HEALER_GEAR[cls] = dict(gear) if gear else dict(_DEFAULT_GEAR[cls])
    mod = importlib.import_module(CLASSES[cls])
    h = mod.Healer(alloc)
    return [E.seed_capacity(h, s, steps=steps) for s in seeds]


def capacity_with(job):
    """capacity() under table overrides set for this job only: (cls, alloc, seeds, steps, {tables name: value}). filler_pass.py's
    mana check runs a longer fight (DURATION) where the five-minute fight leaves a healer's mana talents at zero (2026-11-09)."""
    cls, alloc, seeds, steps, over = job
    old = {k: getattr(T, k) for k in over}
    try:
        for k, v in over.items():
            setattr(T, k, v)
        return capacity((cls, alloc, seeds, steps))
    finally:
        for k, v in old.items():
            setattr(T, k, v)
