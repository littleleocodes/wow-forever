"""Record preparation for gear_phase_1118.sh (2026-11-18, the phase fix of the gear pools):

    python _reference/data/deep-runs/ml_prep_1118.py [classes]

Every ML record (raidsim/ml/<class>-<spec slug>.json) loses its tier sets and the searches made in them, as wf_prep_1117.py did for
the shaman: `ml_pipeline.py <class> --steps final` then makes the Raid BiS and Pre-BiS sets again from the fixed pools (gear_opt.later_phase,
gear_tiers.pool_of: no item the game holds back for a later phase, no Tier 0.5 in the pre-raid tiers), searches the talents in them and
races the comparison again; dungeon_tier.py then makes the quests-and-dungeons tier. The record's starting searches (`bis-dummy-1`), its
spell probe and rotations stay. Backups go to deep-runs/g1118/ (never next to the records: the tools read every file in that folder).
"""
import json
import pathlib
import sys

DATA = pathlib.Path(__file__).resolve().parents[1]
M = DATA / "deep-runs" / "g1118"
M.mkdir(parents=True, exist_ok=True)
classes = sys.argv[1:]
n = 0
for p in sorted((DATA / "raidsim" / "ml").glob("*.json")):
    if p.name in ("rotations.json", "spell-probe.json"):
        continue
    r = json.loads(p.read_text(encoding="utf-8"))
    if classes and r.get("class") not in classes:
        continue
    bk = M / f"ml-{p.name}"
    if not bk.exists():   # the first preparation's copy is the one to keep (a resumed lane runs this step once: its marker)
        bk.write_text(json.dumps(r, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    for k in ("bis2", "prebis", "bis-raid", "prebis-raid", "dungeon"):
        (r.get("gear") or {}).pop(k, None)
    for k in ("bis-dummy", "bis-raid", "prebis-dummy", "prebis-raid", "dungeon-raid"):
        (r.get("search") or {}).pop(k, None)
    for k in ("compare", "compare_raid", "builds", "tidied", "aligned_raid", "signature_check"):
        r.pop(k, None)
    p.write_text(json.dumps(r, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    n += 1
print(f"cleared {n} ML records (backups in deep-runs/g1118/)")
