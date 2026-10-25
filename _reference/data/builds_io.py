"""Locked edits of a class's proposed-builds.json (2026-10-24 audit: open_builds.py, ml_builds.py and raid_path_leveling.py read the file,
spent minutes simulating, then wrote it back whole; the raid and leveling queues run them for the same class at overlapping times, and the
later write would drop the other's builds). `update(cls, remove, add)` re-reads the file under a lock and applies only the change: the
builds whose ids are in `remove` or among `add`'s ids go, `add` is appended."""
import json

import paths
from filelock import locked
from fmt_json import dumps


def update(cls, remove=(), add=()):
    """Apply the change to the current file and return the data written."""
    bp = paths.builds_json("forever", cls)
    with locked(bp.with_suffix(".lock")):
        data = json.load(open(bp, encoding="utf-8"))
        drop = set(remove) | {b["id"] for b in add}
        data["builds"] = [b for b in data["builds"] if b["id"] not in drop] + list(add)
        bp.write_text(dumps(data) + "\n", encoding="utf-8")
    return data
