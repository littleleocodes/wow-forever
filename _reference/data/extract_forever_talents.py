"""Refresh _reference/data/forever-talents/<class>.json from warcraftforever.games.

Usage (from anywhere): python _reference/data/extract_forever_talents.py [class ...]

The calculator pages embed their full talent data as JSON inside the Next.js
payload; this script downloads each page, unescapes the payload and saves the
object that holds "trees". Re-run after the site updates its demo/datamine and
then run render_trees.py + validate_builds.py + render_builds.py.
"""
import json, sys, pathlib, urllib.request

CLASSES = ["warrior", "paladin", "hunter", "rogue", "priest", "shaman", "mage", "warlock", "druid"]
OUT = pathlib.Path(__file__).resolve().parent / "forever-talents"
URL = "https://warcraftforever.games/talents/{cls}"
dec = json.JSONDecoder()
MARK = 'self.__next_f.push([1,"'


def chunks(html):
    """Yield the unescaped JS string of each RSC push chunk."""
    pos = 0
    while True:
        i = html.find(MARK, pos)
        if i == -1:
            return
        j = i + len(MARK)
        # scan to the closing unescaped quote
        k = j
        while True:
            c = html[k]
            if c == "\\":
                k += 2
                continue
            if c == '"':
                break
            k += 1
        raw = html[j:k]
        pos = k
        try:
            yield json.loads('"' + raw + '"')
        except json.JSONDecodeError as e:
            print("  chunk decode error:", e, file=sys.stderr)


def fetch(cls) -> str:
    req = urllib.request.Request(URL.format(cls=cls), headers={"User-Agent": "Mozilla/5.0 (wow-forever notes; talent data refresh)"})
    with urllib.request.urlopen(req, timeout=60) as r:
        return r.read().decode("utf-8", errors="replace")


def extract(cls, html=None):
    html = html if html is not None else fetch(cls)
    for s in chunks(html):
        i = s.find('"trees":')
        if i == -1:
            continue
        # walk back to the enclosing object start
        j = s.rfind('{"meta":', 0, i)
        if j == -1:
            j = s.rfind("{", 0, i)
        while j != -1:
            try:
                obj, _ = dec.raw_decode(s, j)
                if isinstance(obj, dict) and "trees" in obj:
                    return obj
            except json.JSONDecodeError:
                pass
            j = s.rfind("{", 0, j)
    return None


if __name__ == "__main__":
    for cls in [c for c in CLASSES if not sys.argv[1:] or c in sys.argv[1:]]:
        obj = extract(cls)
        if not obj:
            print(f"{cls}: NOT FOUND", file=sys.stderr)
            continue
        out = OUT / f"{cls}.json"
        out.write_text(json.dumps(obj, indent=2, ensure_ascii=False), encoding="utf-8")
        trees = obj["trees"]
        n = sum(len(t["talents"]) for t in trees)
        print(f"{cls}: {len(trees)} trees, {n} talents -> {out.name}; keys: {list(obj.keys())}")
