# priest_refresh_keys.py (2026-11-06, page-audit K1; run once by priest_refresh_1103.sh): takes the priest's open leveling record back to
# the point where each rotation's level-60 search has ended. fl_open_search.py gates every later stage on its key, so the next plain
# run (no --fresh) redoes, on the current data: the 20-60 race among the stored winner, the level-60 finalists and our builds, the
# 20-60 polish, the order choice and order polish, the talent values, the synergy certificate and the signature check, and dates
# the rotation today. Kept: winner, finalists, families, runs_agree, simulated_builds, important_features, model, trees.
# The committed record (git) is the backup; a copy goes to deep-runs/refresh-backups/ as well.
import json, pathlib, sys
P = pathlib.Path("F:/wow-forever/_reference/data/fightlab/open/priest.json")
DROP = ["done", "race", "level_polish", "order", "order_label", "order_polish", "order_stats", "order_stats_split", "orders_raced",
        "values", "values_base", "synergy", "signature", "builds", "gain_vs_ours", "ours_best", "minutes", "date", "split", "family", "link"]
text = P.read_text(encoding="utf-8")
st = json.loads(text)
if not all(r.get("done") and r.get("winner") for r in st["rotations"].values()):
    sys.exit("priest.json: a rotation is not done or has no winner; nothing changed")
BK = pathlib.Path("F:/wow-forever/_reference/data/deep-runs/refresh-backups")   # not next to the record: the open folder is globbed
BK.mkdir(exist_ok=True)
(BK / "priest.pre-refresh.json").write_text(text, encoding="utf-8")
for name, r in st["rotations"].items():
    gone = [k for k in DROP if k in r]
    for k in gone:
        del r[k]
    print(name, "| winner kept:", r["winner"].get("split"), "| finalists kept:", len(r.get("finalists") or []), "| dropped:", ", ".join(gone))
st.pop("cross", None)
P.write_text(json.dumps(st, indent=1, ensure_ascii=False) + chr(10), encoding="utf-8")
print("priest.json written;", len(st["rotations"]), "rotations to refresh")
