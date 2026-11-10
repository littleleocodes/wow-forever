"""The auction house over time, from the user's ForeverTape add-on database (2026-11-09, user: "I want this to utilize the auction house
... a refresh every couple levels, finding upgrades that make meaningful impacts"): how often each item and random-suffix version is
listed and at what price, so the plan can count on gear that is usually for sale at a level although nobody lists it this hour.

READ ONLY: duckdb read_only, one short connection, never between :25 and :30 (the add-on's hourly writer and import). Two series: the add-on's
in-game scans (`auctions`, variant "b<suffix>", the usable ones) and Blizzard's hourly API files (`api_auctions`, bonus "<suffix>", house
110: the alliance house AHCopy.lua reads). A window is one scan or one API file; an item's share is the windows it was listed in. Price:
the median over its windows of the cheapest unit price. Cached in cache/market-<house>.json for a refresh while the database is busy.
"""
import datetime
import json
import pathlib
import statistics

HERE = pathlib.Path(__file__).resolve().parent


def history(duckdb_path, house=110):
    """{"windows": n, "from": iso, "to": iso, "items": {"<item>:<variant>": [windows listed, median cheapest unit price]}}."""
    cache = HERE / "cache" / f"market-{house}.json"
    if duckdb_path and pathlib.Path(duckdb_path).exists() and not 25 <= datetime.datetime.now().minute <= 30:
        try:
            import duckdb
            con = duckdb.connect(str(duckdb_path), read_only=True)
            try:
                scans = con.execute(
                    "select a.item_id, coalesce(a.variant, ''), a.snapshot_id, min(a.buyout * 1.0 / a.count) from auctions a "
                    "join snapshot_status s using (snapshot_id) where s.usable and a.buyout > 0 and a.count > 0 group by 1, 2, 3").fetchall()
                t_scan = con.execute("select count(*), min(n.t_local), max(n.t_local) from snapshots n join snapshot_status s "
                                     "using (snapshot_id) where s.usable").fetchone()
                api = con.execute(
                    "select a.item_id, case when a.bonus is null or a.bonus = '' then '' else 'b' || a.bonus end, a.file_id, "
                    "min(a.unit_price) from api_auctions a join api_files f using (file_id) where f.house = ? and f.kind = 'auctions' "
                    "and a.unit_price > 0 group by 1, 2, 3", [house]).fetchall()
                t_api = con.execute("select count(*), min(lm_t), max(lm_t) from api_files where house = ? and kind = 'auctions'",
                                    [house]).fetchone()
            finally:
                con.close()
            seen = {}
            for item, variant, _, price in list(scans) + list(api):
                seen.setdefault(f"{item}:{variant}", []).append(price)
            ts = [t for t in (t_scan[1], t_scan[2], t_api[1], t_api[2]) if t]
            out = {"windows": int(t_scan[0] or 0) + int(t_api[0] or 0),
                   "from": datetime.datetime.fromtimestamp(min(ts)).isoformat(timespec="minutes") if ts else None,
                   "to": datetime.datetime.fromtimestamp(max(ts)).isoformat(timespec="minutes") if ts else None,
                   "items": {k: [len(v), round(statistics.median(v))] for k, v in seen.items()}}
            cache.parent.mkdir(exist_ok=True)
            cache.write_text(json.dumps(out, separators=(",", ":")) + "\n", encoding="utf-8")
            return out
        except Exception as e:   # noqa: BLE001   (a lock held by the add-on's writer: the last copy)
            print(f"  market: the add-on database could not be read ({type(e).__name__}); using the last copy")
    return json.loads(cache.read_text(encoding="utf-8")) if cache.exists() else {"windows": 0, "items": {}}


if __name__ == "__main__":
    import sys
    h = history(sys.argv[1] if len(sys.argv) > 1 else "F:/wow-addons/data/forever_ah.duckdb")
    print(h["windows"], "windows", h.get("from"), "to", h.get("to"), len(h["items"]), "item versions")
