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
spellbook(cfg, name) -> the character's spellbook from ForeverTape 0.9.5 (2026-11-14): ForeverTapeDB.spellbook["<Name>-<Realm>"] = {t, level,
class, n, spells = {{id, name, rank, tab}, ...}} (rank absent for spells without ranks; written 5 s after each loading screen and 3 s after
a spell is learned), or None.
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


def _close(text, start):
    """The index just past the brace that closes the table opened before `start` (quoted strings skipped: a name may hold a brace)."""
    depth, j = 1, start
    while depth and j < len(text):
        c = text[j]
        if c == '"':
            j = text.index('"', j + 1)
            while text[j - 1] == "\\":
                j = text.index('"', j + 1)
        elif c == "{":
            depth += 1
        elif c == "}":
            depth -= 1
        j += 1
    return j


def _block(text, table, name):
    """The character's block of ForeverTapeDB.<table> (its "<Name>-<Realm>" key, looked up inside that table only), or None."""
    i = text.find(f'["{table}"] = {{')
    if i < 0:
        return None
    body = text[i:_close(text, i + len(f'["{table}"] = {{'))]
    m = re.search(r'\["' + re.escape(name) + r'-[^"|]*"\] = \{', body)
    if not m:
        return None
    return body[m.end():_close(body, m.end())]


def _entries(block):
    """The array entries of a block, each a dict of its fields: WoW writes one field a line and each entry between "{" and "},"."""
    out, cur = [], None
    for line in block.splitlines():
        ln = re.sub(r"\s*-- \[\d+\]$", "", line.strip())
        if ln == "{":
            cur = {}
        elif ln in ("},", "}") and cur is not None:
            out.append(cur)
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
    return out


def spellbook(cfg, name):
    """The character's spellbook (ForeverTape 0.9.5, 2026-11-14), the newest over the saved files: {"t", "when", "level", "n", "ids":
    {spell id}, "ranks": {spell name: highest rank known, 0 for a spell without ranks}}, or None."""
    best = None
    for f in saved_files(cfg):
        block = _block(pathlib.Path(f).read_text(encoding="utf-8", errors="replace"), "spellbook", name)
        if not block:
            continue
        top = block.split('["spells"] = {')[0]
        t = int((re.search(r'\["t"\] = (\d+)', top) or [0, 0])[1])
        lv = re.search(r'\["level"\] = (\d+)', top)
        spells = [e for e in _entries(block) if e.get("name")]
        if not spells or (best and best["t"] >= t):
            continue
        ranks = {}
        for e in spells:
            r = e.get("rank") if isinstance(e.get("rank"), int) else 0
            ranks[e["name"]] = max(ranks.get(e["name"], 0), r)
        best = {"t": t, "when": datetime.datetime.fromtimestamp(t).strftime("%Y-%m-%d %H:%M"), "level": int(lv.group(1)) if lv else None,
                "n": len(spells), "ids": {e["id"] for e in spells if isinstance(e.get("id"), int)}, "ranks": ranks}
    return best


def snapshot(text, name):
    """The add-on's bag and bank snapshot of the character, or None: (time, [{"id", "name", "count", "where"}])."""
    block = _block(text, "inventory", name)
    if block is None:
        return None
    t = re.search(r'\["t"\] = (\d+)', block)
    items, cur = [], None
    for line in block.splitlines():   # WoW writes one field a line and each array entry between "{" and "},"
        ln = line.strip()
        if ln == "{":
            cur = {}
        elif ln in ("},", "}") and cur is not None:
            link = str(cur.get("link") or "").replace("||", "|")
            name = cur.get("name") or (re.search(r"\|h\[(.*?)\]\|h", link) or [None, None])[1]   # (0.9.3: a name not loaded yet: the link's)
            suffix = cur.get("suffix") if isinstance(cur.get("suffix"), int) and cur.get("suffix") else None
            if suffix is None and link:   # the item string's 7th field: item:id:enchant:gem1:gem2:gem3:gem4:suffix
                f = re.search(r"item:([-\d:]+)", link)
                parts = f.group(1).split(":") if f else []
                suffix = int(parts[6]) if len(parts) > 6 and parts[6].lstrip("-").isdigit() and int(parts[6]) else None
            if cur.get("id") is not None or name:
                items.append({"id": cur.get("id"), "name": name, "count": cur.get("count") or 1, "where": cur.get("where") or "bags",
                              "suffix": suffix})
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
    bt = re.search(r'\["bagsT"\] = (\d+)', block)   # 0.9.4: when the bags were last read successfully (t: the last write)
    return (int(bt.group(1)) if bt else int(t.group(1)) if t else 0), items


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
        partial = bool(snapped) and not any(it["where"] == "bags" for it in snapped[1])   # a snapshot without its bags half (2026-11-11:
        # ForeverTape 0.9.3 wrote Arcea's bank rows only): its bank rows count, the purchase record stands for the bags
        if snapped:
            since, items = snapped
            for it in items:   # by name and by id (a link's name can come without its suffix, or not at all: 2026-11-10,
                if (it["name"] or "").lower() in worn:   # "Geomancer's Bracers" for Geomancer's Bracers of Frozen Wrath)
                    continue
                for key in {(it["name"] or "").lower(), f"id:{it['id']}" if it["id"] else ""} - {""}:
                    o = out.setdefault(key, {"name": it["name"], "id": it["id"], "count": 0, "where": it["where"], "when": _day(since),
                                             "suffix": it.get("suffix")})
                    o["count"] += it["count"]
        if snapped:   # a snapshot name without its random suffix ("Geomancer's Bracers", 2026-11-10: the add-on falls back to the plain
            base = {v["name"].lower(): v for v in list(out.values()) if v.get("name")}   # name when a link is not loaded yet): the
            for t, item, cnt, kind in mail_won(text, name, time.time() - MAIL_DAYS * 86400):   # full name of the piece bought
                key = item.lower()
                if kind == "won" and key not in out and key not in worn:
                    b = next((v for n, v in base.items() if key.startswith(n + " of ")), None)
                    if b:
                        out[key] = dict(b, name=item)
        cutoff = max(0 if partial else since, time.time() - MAIL_DAYS * 86400)
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
