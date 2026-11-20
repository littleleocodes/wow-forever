"""2026-11-20, the audit's decision (a): every warlock entry carries upstream's 32 Soul Shards (DefaultOptions; its build files).
Text edits under the specs.json lock, one entry at a time: python add_shards.py <entry> [<entry> ...]"""
import json
import pathlib
import re
import sys

DATA = pathlib.Path("F:/wow-forever/_reference/data")
sys.path.insert(0, str(DATA))
from filelock import locked  # noqa: E402

sp = DATA / "raidsim/specs.json"
with locked(DATA / "raidsim/specs.json.lock"):
    s = sp.read_text(encoding="utf-8")
    for e in sys.argv[1:]:
        i = s.index(f'"{e}": {{')
        j = s.index("\n    }", i)
        sub = s[i:j]
        m = re.search(r'"classOptions": \{([^{}]*)\}', sub)
        assert m, e
        if '"soulShards"' in m.group(1):
            print(e, "has shards already")
            continue
        sub = sub[: m.end(1)] + ', "soulShards": 32' + sub[m.end(1):]
        s = s[:i] + sub + s[j:]
        print(e, "->", json.loads("{" + sub[sub.index('"classOptions"'):].split("}", 1)[0] + "}}"))
    json.loads(s)
    sp.write_text(s, encoding="utf-8")
