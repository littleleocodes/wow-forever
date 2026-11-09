# refresh_keys.py <record under fightlab/open, e.g. rogue.json or pure/rogue-subtlety.json> <rotation>... (2026-11-06; the general form
# of priest_refresh_keys.py). Takes the named rotations of an open leveling record back to the point where their level-60 search has
# ended. fl_open_search.py gates every later stage on its key, so the next plain run (no --fresh; --rotation <rotation>, and --tree for
# a one-tree record) redoes on the current data and rules: the 20-60 race among the stored winner, the level-60 finalists and our
# builds, the 20-60 polish, the order choice and order polish, the talent values, the synergy certificate and the signature check,
# and dates the rotation today. Kept: winner, finalists, families, runs_agree, simulated_builds, important_features, model, trees.
# Use after a rotation's rules changed (rules_retune.py). The committed record (git) is the backup; a copy goes to deep-runs/refresh-backups/.
import json, pathlib, sys
OPEN = pathlib.Path("F:/wow-forever/_reference/data/fightlab/open")
DROP = ["done", "race", "level_polish", "order", "order_label", "order_polish", "order_stats", "order_stats_split", "orders_raced",
        "values", "values_base", "synergy", "signature", "builds", "gain_vs_ours", "ours_best", "minutes", "date", "split", "family", "link"]
if len(sys.argv) < 3:
    sys.exit("usage: refresh_keys.py <record> <rotation>...")
P = OPEN / sys.argv[1]
text = P.read_text(encoding="utf-8")
st = json.loads(text)
todo = sys.argv[2:]
for name in todo:
    r = st["rotations"].get(name)
    # 2026-11-07: a rotation whose level-60 block ended and a later stage crashed (winner and finalists saved, no done) counts as well:
    # warlock Destruction, lane C's process of 11-05 met the fl_levels.py of 11-06 (fl_open_search._load re-reads it per rotation).
    if not r or not r.get("winner") or not (r.get("done") or r.get("finalists")):
        sys.exit(P.name + ": rotation " + name + " is missing, past no level-60 block or has no winner; nothing changed")
BK = pathlib.Path("F:/wow-forever/_reference/data/deep-runs/refresh-backups")   # never next to the record: open_builds.py, render_modes.py
BK.mkdir(exist_ok=True)                                                          # and fl_open_search.write_page glob the open folders
(BK / (sys.argv[1].replace("/", "-")[:-5] + ".pre-refresh.json")).write_text(text, encoding="utf-8")
for name in todo:
    r = st["rotations"][name]
    gone = [k for k in DROP if k in r]
    for k in gone:
        del r[k]
    print(P.name, name, "| winner kept:", r["winner"].get("split"), "| finalists kept:", len(r.get("finalists") or []), "| dropped", len(gone), "keys")
for name in todo:   # 2026-11-06: the refreshed winners are raced under the sibling rotations again (fl_synergy.py <class>, no --rotation)
    (st.get("cross") or {}).pop(name, None)
P.write_text(json.dumps(st, indent=1, ensure_ascii=False) + chr(10), encoding="utf-8")
print(P.name, "written;", len(todo), "rotation(s) to refresh")
