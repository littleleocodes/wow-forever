"""Live client numbers for our spellbook text (2026-11-10, the client 70862 update; user: "Update it and tell me what's different").

Our spell text (forever-spells/<class>.json) comes from talentsforever.com's export plus the hotfix numbers of hotfix_text.py. The launch
client (1.60.1.70790) and the server's hotfixes changed spells that Blizzard's notes of 2 Nov did not list: Lightning Bolt rank 10 went
from 196 to 353 base damage, Chain Lightning rank 4 from 123 to 510, Starfire, Ferocious Bite, Rip, Rake and Holy Strike's Holy damage
more than doubled, and more. The raid simulator reads the live data and had them; the fight lab and the stats model read our text.

For every rank of our spellbooks:
  1. the live tooltip from Wowhead's Forever tooltip service (the client's wording and numbers, cached in raw/<pull>/live_spells.json);
  2. Wowhead computes a spell's numbers at the spell's highest level (its MaxLevel, up to 65), our text at level 60 (Fireball rank 12:
     437-553 against 425-541, 3 a level for 4 levels): every number that equals an effect's range at that level is brought back to level
     60 with the official simulator's spell data (spell_store_inputs.json at the pinned commit: base points, growth per level, variance,
     the spell's levels; it carries the server's hotfixes too), and the two are checked to agree;
  3. a rank whose corrected live numbers differ from ours takes them when Wowhead's wording matches ours word for word apart from the
     numbers (so the fight lab's parsers keep reading it); else it is listed for review. Each changed rank carries `live` {build,
     before, source}.
The derived facts are archived in raw/<pull>/; build_forever_spells.py applies them after the hotfix text on every rebuild
(apply_spells), so an export that already carries a number leaves the rank as it is.

    python _reference/data/live_spells.py --pull 2026-11-10-live-70888 --build 1.60.1.70888 --commit <sim commit> [--write]
"""
import argparse
import gzip
import html
import json
import pathlib
import re
import subprocess
import urllib.request
from concurrent.futures import ThreadPoolExecutor

HERE = pathlib.Path(__file__).resolve().parent
SPELLS = HERE / "forever-spells"
SIM = pathlib.Path.home() / ".wow-forever-tools" / "wowsims-forever-next"   # a clone holding the commit (repin_rehearsal's worktree)
NUM = re.compile(r"\d[\d,]*(?:\.\d+)?")


def tooltip(sid):
    req = urllib.request.Request(f"https://nether.wowhead.com/forever/tooltip/spell/{sid}", headers={"User-Agent": "wow-forever-planner"})
    try:
        js = json.loads(urllib.request.urlopen(req, timeout=25).read())
    except Exception:  # noqa: BLE001
        return sid, None
    tip = js.get("tooltip") or ""
    m = re.findall(r'<div class="q">(.*?)</div>', tip, re.S)
    text = html.unescape(re.sub(r"<br\s*/?>", "\n", m[-1]) if m else "")
    text = re.sub(r"<[^>]+>", " ", text)
    return sid, re.sub(r"[ \t]+", " ", text).strip()


def store(commit):
    raw = subprocess.run(["git", "-C", str(SIM), "show", f"{commit}:assets/db_inputs/spell_store_inputs.json"], capture_output=True).stdout
    return json.loads(gzip.decompress(raw))


def tidy(t):
    """One space between words, none before a stop or comma (Wowhead writes "by 30% ." where we write "by 30%.")."""
    return re.sub(r"\s+([.,;:])", lambda m: m.group(1), re.sub(r"\s+", " ", t or "")).strip()


ARITH = re.compile(r"[\[(]\s*([0-9.+\-*/ ]+?)\s*[\])]")


SWITCH = re.compile(r"\[\s*[A-Z][A-Za-z' ]+\s*:\s*[^/\]]+?/\s*([^\]]+?)\s*\]")


def base_value(t):
    """Wowhead shows a talent's effect inline, "[ Unholy Power : ( 18 * 1.1) to ( 22 * 1.1) / 18 to 22]": our text is the base, the part
    after the slash."""
    return SWITCH.sub(lambda m: m.group(1), t)


def evaluate(t):
    """Wowhead writes some numbers as arithmetic ("( 332.929 * 1 )", "[ 169.5 * ( ( ( 1 ) ) ) ]", "( 3122 / 77 - 1 + 0)"): every bracket
    that holds only numbers and + - * / is worked out, innermost first, and rounded to a whole number (a tooltip's own rounding)."""
    for _ in range(8):
        def calc(m):
            try:
                v = eval(m.group(1), {"__builtins__": {}}, {})   # digits, dots, spaces and + - * / only (ARITH)
            except Exception:  # noqa: BLE001
                return m.group(0)
            return str(int(v)) if abs(v - round(v)) < 1e-9 else (str(round(v)) if abs(v) >= 10 else f"{v:.1f}")
        new = ARITH.sub(calc, t)
        if new == t:
            break
        t = new
    return t


def skeleton(t):
    return NUM.sub("#", tidy(t)).rstrip(".")


def to_level60(text, sid, st):
    """Wowhead's text with every number that is an effect's range at the spell's MaxLevel brought back to level 60."""
    lv = (st["Levels"].get(str(sid)) or {})
    eff = st["Effects"].get(str(sid))
    eff = eff if isinstance(eff, list) else [eff] if eff else []
    top = lv.get("MaxLevel") or 0
    if top <= 60:
        return text
    subs = {}
    for e in eff:
        ppl, base = e.get("PPL") or 0, e.get("BasePoints") or 0
        if not ppl or not base:
            continue
        v = e.get("Variance") or 0
        b60 = base + ppl * (60 - (lv.get("BaseLevel") or 60))
        d = ppl * (top - 60)
        for x60 in {b60, b60 * (1 - v / 2), b60 * (1 + v / 2)}:
            subs[round(x60 + d)] = round(x60)
            subs[int(x60 + d)] = int(x60)
    if not subs:
        return text

    def fix(m):
        s = m.group(0)
        n = float(s.replace(",", ""))
        for k in (int(n), int(n) - 1, int(n) + 1):   # (169.5 rounds to 170 on Wowhead and to 169 here: a point either way)
            if n.is_integer() and k in subs:
                return f"{subs[k]:,}" if "," in s else str(subs[k])
        return s
    return NUM.sub(fix, text)


def live_text(ours, live):
    """Our wording with the live numbers, or None when the wording differs (or the live text holds a formula or a talent's switch)."""
    if not live or re.search(r"[()*$\[\]]", live) or skeleton(ours) != skeleton(live):
        return None
    a, b = NUM.findall(ours), NUM.findall(live)
    if any(float(y.replace(",", "")) == 0 and float(x.replace(",", "")) != 0 for x, y in zip(a, b)):
        return None   # a 0 where ours has a number: a server-side value the client's tooltip lacks (Oath of Light's 400/115/230)
    it = iter(NUM.findall(live))
    return NUM.sub(lambda m: next(it), ours)


def apply_spells(cls, obj, pull=None):
    """Write the archived live numbers into a forever-spells object (build_forever_spells.py calls it after hotfix_text); returns the
    spells changed."""
    p = HERE / "raw" / (pull or newest_pull() or "-") / "live_spells.json"
    if not p.is_file():
        return []
    data = json.loads(p.read_text(encoding="utf-8"))
    out = []
    for tab in obj.get("tabs", []):
        for sp in tab["spells"]:
            hit = False
            for r in sp["ranks"]:
                new = data["take"].get(str(r.get("id") or ""))
                if new and new != r.get("text") and r.get("text") == data["before"].get(str(r["id"])):
                    r["live"] = {"build": data["build"], "before": r.get("text", ""),
                                 "source": f"Wowhead's Forever tooltip, brought to level 60 with wowsims/forever {data['commit'][:9]}'s spell data "
                                           f"(https://www.wowhead.com/forever/spell={r['id']})"}
                    r["text"] = new
                    hit = True
            if hit:
                out.append(sp["name"])
    return out


def newest_pull():
    ps = sorted(p.parent.name for p in (HERE / "raw").glob("*-live-*/live_spells.json"))
    return ps[-1] if ps else None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--pull", required=True)
    ap.add_argument("--build", required=True, help="the client build the live text stands for")
    ap.add_argument("--commit", required=True, help="the official simulator commit whose spell data corrects the levels")
    ap.add_argument("--cache", default=None, help="a JSON {spell id: Wowhead text} to start from (skips those fetches)")
    ap.add_argument("--write", action="store_true", help="apply to forever-spells/*.json now (else only archive and report)")
    a = ap.parse_args()
    st = store(a.commit)
    ours = {}
    for f in sorted(SPELLS.glob("*.json")):
        d = json.loads(f.read_text(encoding="utf-8"))
        for tab in d["tabs"]:
            for sp in tab["spells"]:
                for r in sp["ranks"]:
                    if r.get("id"):
                        ours[int(r["id"])] = (f.stem, sp["name"], r.get("rank"), r.get("text", ""))
    tips = json.loads(pathlib.Path(a.cache).read_text(encoding="utf-8")) if a.cache else {}
    tips = {k: v for k, v in tips.items() if v and not v.startswith("ERROR")}   # (a failed fetch is asked again)
    todo = [s for s in ours if not tips.get(str(s))]
    with ThreadPoolExecutor(6) as pool:
        for sid, t in pool.map(tooltip, todo):
            if t:
                tips[str(sid)] = t
    take, before, review = {}, {}, []
    for sid, (cls, name, rank, text) in sorted(ours.items(), key=lambda kv: kv[1][:3]):
        live = tips.get(str(sid))
        if not live:
            continue
        live60 = to_level60(tidy(evaluate(base_value(live))), sid, st)
        a_, b_ = ([float(x.replace(",", "")) for x in NUM.findall(t)] for t in (text, live60))
        if len(a_) == len(b_) and all(abs(x - y) <= max(1.0, 0.02 * abs(x)) for x, y in zip(a_, b_)):
            continue   # the same numbers, give or take rounding (a point, or 2%)
        new = live_text(text, live60)
        if new is not None and new != text:
            take[str(sid)], before[str(sid)] = new, text
        elif new is None:
            review.append((cls, name, rank, sid, text, live60))
    out = HERE / "raw" / a.pull
    out.mkdir(parents=True, exist_ok=True)
    (out / "live_spells.json").write_text(json.dumps({"build": a.build, "commit": a.commit, "take": take, "before": before,
                                                      "tooltips": {k: tips[k] for k in sorted(tips, key=int)}}, indent=1, ensure_ascii=False) + "\n",
                                          encoding="utf-8")
    lines = [f"# Live spell numbers (client {a.build})", "",
             f"> Generated by `_reference/data/live_spells.py`: every rank of our spellbooks against Wowhead's Forever tooltip, brought to level "
             f"60 with wowsims/forever {a.commit[:9]}'s spell data. {len(ours)} ranks; {len(take)} take the live numbers; {len(review)} differ "
             "in wording or hold a formula or a talent switch (listed, not taken). Do not hand-edit.", "", "## Taken", ""]
    lines += [f"- {ours[int(s)][0]} / {ours[int(s)][1]} {ours[int(s)][2]} ({s}): {before[s]} -> {take[s]}" for s in take]
    lines += ["", "## Not taken (wording, formula or talent switch)", ""]
    lines += [f"- {c} / {n} {rk} ({sid}):\n  - ours: {t}\n  - live: {lv}" for c, n, rk, sid, t, lv in review]
    (out / "README.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"{len(ours)} ranks; {len(take)} take live numbers; {len(review)} not taken -> raw/{a.pull}/README.md")
    if a.write:
        for f in sorted(SPELLS.glob("*.json")):
            d = json.loads(f.read_text(encoding="utf-8"))
            names = apply_spells(f.stem, d, a.pull)
            if names:
                f.write_text(json.dumps(d, indent=1, ensure_ascii=False), encoding="utf-8")
                print(f"  {f.stem}: {', '.join(names)}")


if __name__ == "__main__":
    main()
