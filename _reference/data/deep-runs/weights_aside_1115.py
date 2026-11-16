"""weights_aside_1115.py <leveling | leveling-best> <class> <spec>... (2026-11-15): move the stat-weights files of these specs' current
page picks to deep-runs/refresh-backups/weights-<folder>-1115/, so stat_weights_all.py measures them again (it redoes only missing or
stale files, and a build whose talents or rules changed keeps its date). Used by fl_mage_armor_1115.sh for the picks whose rotation
rules changed."""
import pathlib
import shutil
import sys

D = pathlib.Path("F:/wow-forever/_reference/data")
sys.path[:0] = [str(D), str(D / "fightlab"), str(D / "scorer")]
import level_guides as LG  # noqa: E402

if len(sys.argv) < 4 or sys.argv[1] not in ("leveling", "leveling-best"):
    sys.exit(__doc__)
folder, cls, specs = sys.argv[1], sys.argv[2], sys.argv[3:]
SA = LG.fightlab_signature_audit()
bk = D / "deep-runs" / "refresh-backups" / f"weights-{folder}-1115"
bk.mkdir(parents=True, exist_ok=True)
seen = set()
for slot in SA.page_slots(cls, signature=True):
    if slot[0] in specs and slot[1]:
        seen.add(slot[0])
        f = D / "characters" / "weights" / folder / f"{cls}-{slot[1][0]['id']}.json"
        if f.exists():
            shutil.move(str(f), str(bk / f.name))
            print(f"moved {folder}/{f.name} to {bk}")
        else:
            print(f"absent: {folder}/{f.name}")
missing = [s for s in specs if s not in seen]
if missing:
    sys.exit(f"no page pick for {missing}")
