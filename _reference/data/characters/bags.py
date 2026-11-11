"""What the character owns but does not wear, for the gear planner (2026-11-10, user: "Can you see my bags and what I've purchased?",
then "Yes" to using the purchases now and to a bag snapshot in the add-on).

Two sources, both from the user's own add-on ForeverTape (F:/wow-addons; its saved file WTF/Account/<account>/SavedVariables/
ForeverTape.lua, read only, the account folder's name never printed):
  - its bag and bank snapshot, ForeverTapeDB.inventory["<Name>-<Realm>"] = {t, level, money, items = {{id, name, count, where}, ...},
    bankT} (written by the add-on at logout and when the bags change; the bank only while the bank is open): authoritative at its time;
  - its auction mail record, ForeverTapeDB.mail["<Name>-<Realm>|won|<item>|..."] = {first, count, ...}: what the character won at the
    auction house and took from the mailbox. Until the add-on writes a snapshot, a gear piece won in the last MAIL_DAYS days, not worn
    now and not sold since, counts as in the bags (it may have been sold to a vendor: the page says when it was bought).
owned(cfg, snap) -> {lower-case item name: {"name", "count", "where": "bags"|"bank"|"bought", "when": "YYYY-MM-DD"}} (ids under "id:<n>").
"""
import datetime
import glob
import pathlib
import re
import time

MAIL_DAYS = 30


def saved_files(cfg):
    """ForeverTape's saved files on this PC (one per account folder)."""
    ah = (cfg.get("ah") or {}).get("ahcopy") or ""
    wow = cfg.get("wow_dir") or ah.split("/Interface/")[0]
    if not wow:
        return []
    return sorted(glob.glob(str(pathlib.Path(wow) / "WTF" / "Account" / "*" / "SavedVariables" / "ForeverTape.lua")))


def _day(t):
    return datetime.datetime.fromtimestamp(int(t)).strftime("%Y-%m-%d")


def snapshot(text, name):
    """The add-on's bag and bank snapshot of the character, or None: (time, [{"id", "name", "count", "where"}])."""
    i = text.find('["inventory"] = {')
    if i < 0:
        return None
    m = re.search(r'\["' + re.escape(name) + r'-[^"]*"\] = \{', text[i:])
    if not m:
        return None
    start = i + m.end()
    depth, j = 1, start
    while depth and j < len(text):   # the character's block, by its braces
        c = text[j]
        if c == '"':   # skip a quoted string (an item name may hold a brace)
            j = text.index('"', j + 1)
            while text[j - 1] == "\\":
                j = text.index('"', j + 1)
        elif c == "{":
            depth += 1
        elif c == "}":
            depth -= 1
        j += 1
    block = text[start:j]
    t = re.search(r'\["t"\] = (\d+)', block)
    items, cur = [], None
    for line in block.splitlines():   # WoW writes one field a line and each array entry between "{" and "},"
        ln = line.strip()
        if ln == "{":
            cur = {}
        elif ln in ("},", "}") and cur is not None:
            if cur.get("id") is not None or cur.get("name"):
                items.append({"id": cur.get("id"), "name": cur.get("name"), "count": cur.get("count") or 1, "where": cur.get("where") or "bags"})
            cur = None
        elif cur is not None:
            m = re.match(r'\["(\w+)"\] = (.*?),?$', ln)
            if m:
                v = m.group(2)
                if v.startswith('"') and v.endswith('"'):
                    v = v[1:-1].replace('\\"', '"').replace("\\\\", "\\")
                elif re.fullmatch(r"-?\d+", v):
                    v = int(v)
                cur[m.group(1)] = v
    return (int(t.group(1)) if t else 0), items


def mail_won(text, name, since=0):
    """[(time, item name, count, kind)] of the character's auction mail (won and sold), newer than `since`."""
    out = []
    for m in re.finditer(r'\["' + re.escape(name) + r'-[^|"]*\|(won|sold)\|([^|"]+)\|[^"]*"\] = \{(.*?)\n\}', text, re.S):
        kind, item, body = m.group(1), m.group(2), m.group(3)
        t = re.search(r'\["first"\] = (\d+)', body)
        cnt = re.search(r'\["count"\] = (\d+)', body)
        if t and int(t.group(1)) > since:
            out.append((int(t.group(1)), item, int(cnt.group(1)) if cnt else 1, kind))
    return sorted(out)


def owned(cfg, snap):
    name = snap["profile"]["name"]
    worn = {(it.get("name") or "").lower() for it in (snap.get("equipment") or {}).get("equipped_items") or []}
    out = {}
    for f in saved_files(cfg):
        text = pathlib.Path(f).read_text(encoding="utf-8", errors="replace")
        snapped = snapshot(text, name)
        since = 0
        if snapped:
            since, items = snapped
            for it in items:
                key = (it["name"] or f"id:{it['id']}").lower()
                if key in worn:
                    continue
                o = out.setdefault(key, {"name": it["name"], "id": it["id"], "count": 0, "where": it["where"], "when": _day(since)})
                o["count"] += it["count"]
        cutoff = max(since, time.time() - MAIL_DAYS * 86400)
        sold = {}
        for t, item, cnt, kind in mail_won(text, name, cutoff):
            if kind == "sold":
                sold[item.lower()] = t
        for t, item, cnt, kind in mail_won(text, name, cutoff):
            key = item.lower()
            if kind != "won" or key in worn or sold.get(key, 0) > t:
                continue
            o = out.setdefault(key, {"name": item, "id": None, "count": 0, "where": "bought", "when": _day(t)})
            o["count"] += cnt
    return out


if __name__ == "__main__":
    import json
    import sys
    sys.stdout.reconfigure(encoding="utf-8")
    root = pathlib.Path(__file__).resolve().parents[3]
    who = sys.argv[1] if len(sys.argv) > 1 else "arcea"
    cfg = json.load(open(root / "_characters" / who / "character.json", encoding="utf-8"))
    arm = root / "_characters" / who / "armory"
    snap = {p: json.load(open(arm / f"{p}.json", encoding="utf-8")) for p in ("profile", "equipment")}
    for k, v in sorted(owned(cfg, snap).items(), key=lambda kv: kv[1]["when"]):
        print(v["when"], v["where"], v["count"], v["name"])
