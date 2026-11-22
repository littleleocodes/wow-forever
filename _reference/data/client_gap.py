"""Is the data behind the live game? (2026-11-21, the audit session's guard, after the project ran four days and two client builds behind
the live game unnoticed: clients 1.60.1.70959 and 71037 against data on 70938, the simulator pin 529 commits behind upstream.)

    python _reference/data/client_gap.py [--write] [--offline]

Asks wago.tools for the newest WoW: Forever client build (product wowf) and the official simulator's upstream for its head (a fetch in the
local clone), and compares them with the data (the talent snapshot's build, data_build.BUILD, and the newest live spell pull, raw/*-live-
<build>) and the simulator pin (raidsim/setup.py). Prints the gap. --write keeps it in client-gap.json; render_modes then puts a line in
every page's footer while the live client is newer than the data, and each known difference of client-gap-known.json (hand-kept: what is
already known to differ until the update) on its class's pages; page_lint lists the gap as a finding. Run it at the start of every lane and
at every regen (rebuild.py's regen step runs it). --offline skips the network and keeps the last record's live side. A failed request keeps
the last record's answer for that side and says so."""
import argparse
import datetime
import json
import os
import pathlib
import re
import subprocess
import sys
import urllib.request

HERE = pathlib.Path(__file__).resolve().parent
OUT = HERE / "client-gap.json"
KNOWN = HERE / "client-gap-known.json"
sys.path.insert(0, str(HERE))


def vkey(v):
    return tuple(int(x) for x in re.findall(r"\d+", v or "0"))


def data_side():
    import data_build
    pulls = sorted((vkey(m.group(1)), "1.60.1." + m.group(1)) for p in (HERE / "raw").glob("*-live-*")
                   for m in [re.search(r"-live-(\d{5,})$", p.name)] if m)
    spells = pulls[-1][1] if pulls else None
    client = max([b for b in (data_build.BUILD, spells) if b], key=vkey)
    return {"talents": data_build.BUILD, "spells": spells, "client": client}


def pin_and_clone():
    s = (HERE / "raidsim" / "setup.py").read_text(encoding="utf-8")
    m = re.search(r'"forever":\s*\{.*?"dir":\s*"([^"]+)".*?"commit":\s*"([0-9a-f]{40})"', s, re.S)
    clone = pathlib.Path(os.environ.get("WOW_FOREVER_SIM") or (pathlib.Path.home() / ".wow-forever-tools" / m.group(1)))
    return m.group(2), clone


def live_client():
    req = urllib.request.Request("https://wago.tools/api/builds", headers={"User-Agent": "forever-tools"})
    with urllib.request.urlopen(req, timeout=60) as r:
        d = json.load(r)
    rows = d.get("wowf") or []
    best = max(rows, key=lambda x: vkey(x.get("version")))
    return {"build": best["version"], "date": (best.get("created_at") or "")[:10]}


def upstream(pin, clone):
    git = ["git", "-C", str(clone)]
    subprocess.run(git + ["fetch", "-q", "origin"], check=True, capture_output=True, timeout=180)
    ref = next((r for r in ("origin/master", "origin/main")
                if subprocess.run(git + ["rev-parse", "-q", "--verify", r], capture_output=True).returncode == 0), None)
    head = subprocess.run(git + ["rev-parse", ref], check=True, capture_output=True, text=True).stdout.strip()
    date = subprocess.run(git + ["log", "-1", "--format=%cd", "--date=short", ref], check=True, capture_output=True, text=True).stdout.strip()
    behind = int(subprocess.run(git + ["rev-list", "--count", f"{pin}..{ref}"], check=True, capture_output=True, text=True).stdout.strip())
    return {"head": head, "date": date, "behind": behind}


def load():
    try:
        return json.load(open(OUT, encoding="utf-8"))
    except (OSError, ValueError):
        return {}


def footer_line(rec=None):
    """The footer line while the live client is newer than the data, else ""."""
    rec = rec if rec is not None else load()
    live, data = (rec.get("live") or {}).get("build"), (rec.get("data") or {}).get("client")
    if not live or not data or vkey(live) <= vkey(data):
        return ""
    when = (rec.get("live") or {}).get("date")
    return f"The live client is {live}" + (f" ({when})" if when else "") + f"; these pages are on {data}; an update follows."


def known(cls, mode):
    """The hand-kept known differences for a class's pages of one mode (client-gap-known.json), while the live client is newer."""
    if not footer_line():
        return []
    try:
        items = json.load(open(KNOWN, encoding="utf-8")).get("items") or []
    except (OSError, ValueError):
        return []
    return [it["text"] for it in items if cls in (it.get("classes") or []) and mode in (it.get("modes") or [])]


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--write", action="store_true")
    ap.add_argument("--offline", action="store_true")
    a = ap.parse_args(argv)
    last = load()
    rec = {"checked": datetime.datetime.now().isoformat(timespec="minutes"), "data": data_side(), "errors": []}
    pin, clone = pin_and_clone()
    rec["sim"] = {"pin": pin}
    if a.offline:
        rec["live"], rec["sim"]["upstream"] = last.get("live"), (last.get("sim") or {}).get("upstream")
        rec["errors"].append("offline: the live side is the last record's")
    else:
        try:
            rec["live"] = live_client()
        except Exception as e:   # noqa: BLE001 - a network failure keeps the last answer
            rec["live"] = last.get("live")
            rec["errors"].append(f"wago.tools: {type(e).__name__}: {e}")
        try:
            rec["sim"]["upstream"] = upstream(pin, clone)
        except Exception as e:   # noqa: BLE001
            rec["sim"]["upstream"] = (last.get("sim") or {}).get("upstream")
            rec["errors"].append(f"upstream: {type(e).__name__}: {e}")
    live, data = (rec.get("live") or {}).get("build"), rec["data"]["client"]
    up = rec["sim"].get("upstream") or {}
    rec["client_behind"] = bool(live and vkey(live) > vkey(data))
    rec["talents_behind"] = bool(live and vkey(live) > vkey(rec["data"]["talents"]))
    print(f"live client {live or '?'} ({(rec.get('live') or {}).get('date', '?')})")
    print(f"  spell numbers on {rec['data']['spells']}{'  << BEHIND' if live and rec['data']['spells'] and vkey(live) > vkey(rec['data']['spells']) else ''}")
    print(f"  talent data on {rec['data']['talents']}{'  << BEHIND (the older of the two; talent_client_diff.py compares the trees)' if rec['talents_behind'] else ''}")
    print(f"simulator pin {pin[:9]}; upstream {up.get('head', '?')[:9]} ({up.get('date', '?')}), {up.get('behind', '?')} commits ahead of the pin"
          + ("  << BEHIND" if up.get("behind") else ""))
    for e in rec["errors"]:
        print("  note:", e)
    if a.write:
        OUT.write_text(json.dumps(rec, indent=1) + "\n", encoding="utf-8")
        print(f"wrote {OUT.relative_to(HERE.parents[1])}")
    return rec


if __name__ == "__main__":
    main()
