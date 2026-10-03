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
