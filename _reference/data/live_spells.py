"""Live client numbers for our spellbook text (2026-11-10, the client 70862 update; user: "Update it and tell me what's different").

Our spell text (forever-spells/<class>.json) comes from talentsforever.com's export plus the hotfix numbers of hotfix_text.py. The launch
client (1.60.1.70790) and the server's hotfixes changed spells that Blizzard's notes of 2 Nov did not list: Lightning Bolt rank 10 went
from 196 to 353 base damage, Chain Lightning rank 4 from 123 to 510, Starfire, Ferocious Bite, Rip and Rake more than doubled, and more.
The raid simulator reads the live data and had them; the fight lab and the stats model read our text. (Holy Strike's "doubled" Holy
damage and Backstab's flat 225 -> 150 were this tool misreading Wowhead, removed on 2026-11-19: see step 4.)

For every rank of our spellbooks:
  1. the live tooltip from Wowhead's Forever tooltip service (the client's wording and numbers, cached in raw/<pull>/live_spells.json);
  2. Wowhead computes a spell's numbers at the spell's highest level (its MaxLevel, up to 65), our text at level 60 (Fireball rank 12:
     437-553 against 425-541, 3 a level for 4 levels): every number that equals an effect's range at that level is brought back to level
     60 with the official simulator's spell data (spell_store_inputs.json at the pinned commit: base points, growth per level, variance,
     the spell's levels; it carries the server's hotfixes too), and the two are checked to agree;
  3. a rank whose corrected live numbers differ from ours takes them when Wowhead's wording matches ours word for word apart from the
     numbers (so the fight lab's parsers keep reading it); else it is listed for review. Each changed rank carries `live` {build,
     before, source};
  4. (2026-11-19, the independent audit's D8 and D9) a change is refused and listed when the strike's new flat number is the old one
     over (or times) its weapon percent ("150% weapon damage plus 225", "140% normal damage plus 161", "435% damage plus 182"): Wowhead
     shows the spell's raw $s1, the client's text the number after the percent, which the game applies to the flat part too. The 70888
     pull had taken 31 such ranks (Holy Strike 1-8, Claw 1-5, Shred 1-5, Ravage 1-4, Backstab 1-9, Counterattack 1-4): every paladin
     leveling pick 2.2-3.0% too fast, the Feral pick far too slow (with Cat Form's 12 attack power for 120, step 2's no-MaxLevel case).
The derived facts are archived in raw/<pull>/; build_forever_spells.py applies them after the hotfix text on every rebuild
(apply_spells), so an export that already carries a number leaves the rank as it is.

    python _reference/data/live_spells.py --pull 2026-11-10-live-70888 --build 1.60.1.70888 --commit <sim commit> [--write]
    python _reference/data/live_spells.py --pull 2026-11-10-live-70888 --regenerate      (an archived pull redone from its own tooltips
        against the text of its day, nothing fetched; then build_forever_spells.py)
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


REFERENCED = re.compile(r"\$(?:/(\d+);)?(\d+)[a-zA-Z]")   # "$16361s1", "$/2;20966s1" (half of it) in a spell's description


def to_level60(text, sid, st):
    """Wowhead's text with every number that is an effect's range at its spell's MaxLevel brought back to level 60: the rank's own
    effects and those of every spell its description takes a number from ($16361s1: Windfury Weapon's extra attack power, $16313s1:
    Rockbiter Weapon's passive, $/2;20966s1: half of Seal of Command's judgement). 2026-11-15: only the rank's own effects were brought
    back, so the 70888 pull took eight ranks' MaxLevel numbers for a change (Windfury Weapon rank 4: 433 extra attack power for the
    client's 333 at level 60; Rockbiter rank 7, Frostbrand rank 5, Seal of Command rank 5, Seal of Fury rank 7, Light's Vigil rank 3,
    Holy Nova rank 6, Dire Bear Form).
    2026-11-19 (the independent audit): three more ways a number Wowhead shows for another level got through, all in the 70888 pull:
    - a periodic total ($o1: a tick times the ticks) at MaxLevel is brought back too (Wild Growth rank 3: 769 for 679, Riptide rank 3:
      953 for 805, Lacerate rank 4: 451 for 406);
    - a number that does not move with the level is never taken for one that does by the one-point fallback (Flame Shock rank 6's
      320 damage over 12 sec had become 292: its direct damage at MaxLevel reads 319);
    - a spell with no MaxLevel (0) scales on with the level, and Wowhead shows its base: Cat Form's 12 attack power is 120 at level 60
      (12 + 2 x (60 - 6)), Stoneclaw Totem rank 1's 50 health 206."""
    srcs = [(int(sid), 1)]
    for m in REFERENCED.finditer(st["Descriptions"].get(str(sid)) or ""):
        r = (int(m.group(2)), int(m.group(1) or 1))
        if r not in srcs:
            srcs.append(r)
    subs, ref_subs, keep = {}, {}, set()
    for i, (s, div) in enumerate(srcs):
        lv = (st["Levels"].get(str(s)) or {})
        top = lv.get("MaxLevel") or 0
        blv = lv.get("BaseLevel") or 60
        eff = st["Effects"].get(str(s))
        eff = eff if isinstance(eff, list) else [eff] if eff else []
        dur = (st["Misc"].get(str(s)) or {}).get("DurationMs") or 0
        out = subs if i == 0 else ref_subs
        for e in eff:
            ppl, base = e.get("PPL") or 0, e.get("BasePoints") or 0
            v = e.get("Variance") or 0
            per = e.get("PeriodMs") or 0
            ticks = dur // per if per and dur else 0
            if not ppl:   # a number that does not move with the level: Wowhead's is already the level-60 one
                for x in {base, base * (1 - v / 2), base * (1 + v / 2)}:
                    for y in ({x, x * ticks} if ticks else {x}):
                        keep.update({round(y / div), int(y / div)})
                continue
            if not base:
                continue
            if top == 0:   # no cap: the game scales on with the level, Wowhead shows the base
                out.setdefault(round(base / div), round((base + ppl * (60 - blv)) / div))
                continue
            if top <= 60:
                continue
            b60 = base + ppl * (60 - blv)
            d = ppl * (top - 60)
            for x60 in {b60, b60 * (1 - v / 2), b60 * (1 + v / 2)}:
                out[round((x60 + d) / div)] = round(x60 / div)
                out[int((x60 + d) / div)] = int(x60 / div)
                if ticks:
                    out[round((x60 + d) * ticks / div)] = round(x60 * ticks / div)
                    out[int((x60 + d) * ticks / div)] = int(x60 * ticks / div)
    for k, v in ref_subs.items():   # the rank's own effects first, as before
        subs.setdefault(k, v)
    if not subs:
        return text

    def fix(m):
        s = m.group(0)
        n = float(s.replace(",", ""))
        if not n.is_integer():
            return s
        n = int(n)
        if n in subs:
            return f"{subs[n]:,}" if "," in s else str(subs[n])
        if n in keep:
            return s
        for k in (n - 1, n + 1):   # (169.5 rounds to 170 on Wowhead and to 169 here: a point either way)
            if k in subs:
                return f"{subs[k]:,}" if "," in s else str(subs[k])
        return s
    return NUM.sub(fix, text)


PCT = re.compile(r"(\d+)% (?:weapon |normal )?damage plus")


def percent_artifact(old, new):
    """Why a change is the strike's number before its weapon percent (step 4 of the docstring), or None: a changed number of the new
    text is the old one over (or times) the strike's percent, compared in the old text's units (its rounding is a point)."""
    ps = [int(p) / 100 for p in PCT.findall(old)]
    if not ps:
        return None
    for x, y in zip(NUM.findall(old), NUM.findall(new)):
        x, y = float(x.replace(",", "")), float(y.replace(",", ""))
        if x == y:
            continue
        for p in ps:
            if p == 1:
                continue
            for z, how in ((y * p, "over"), (y / p, "times")):
                if abs(z - x) <= max(1.0, 0.02 * abs(x)):
                    return f"{y:g} is {x:g} {how} {p:.0%}"
    return None


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


def all_pulls():
    """Every archived pull, oldest first: each records its changes against the text of its day (`before`), so a spellbook rebuilt from
    the export takes them in turn (build_forever_spells.py, since 2026-11-16)."""
    return sorted(p.parent.name for p in (HERE / "raw").glob("*-live-*/live_spells.json"))


def newest_pull():
    ps = sorted(p.parent.name for p in (HERE / "raw").glob("*-live-*/live_spells.json"))
    return ps[-1] if ps else None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--pull", required=True)
    ap.add_argument("--build", default=None, help="the client build the live text stands for (with --regenerate: the archive's)")
    ap.add_argument("--commit", default=None, help="the official simulator commit whose spell data corrects the levels (with "
                                                   "--regenerate: the archive's)")
    ap.add_argument("--cache", default=None, help="a JSON {spell id: Wowhead text} to start from (skips those fetches)")
    ap.add_argument("--regenerate", action="store_true", help="redo the archived pull from its own tooltips against the text of its "
                    "day (each rank it changed back to its live.before), fetching nothing; then run build_forever_spells.py")
    ap.add_argument("--write", action="store_true", help="apply to forever-spells/*.json now (else only archive and report)")
    a = ap.parse_args()
    arch = json.loads((HERE / "raw" / a.pull / "live_spells.json").read_text(encoding="utf-8")) if a.regenerate else {}
    a.build, a.commit = a.build or arch.get("build"), a.commit or arch.get("commit")
    if not a.build or not a.commit:
        ap.error("--build and --commit are required (or --regenerate an archived pull)")
    st = store(a.commit)
    ours = {}
    for f in sorted(SPELLS.glob("*.json")):
        d = json.loads(f.read_text(encoding="utf-8"))
        for tab in d["tabs"]:
            for sp in tab["spells"]:
                for r in sp["ranks"]:
                    if r.get("id"):
                        lv = r.get("live") or {}
                        text = lv.get("before", "") if a.regenerate and lv.get("build") == a.build else r.get("text", "")
                        ours[int(r["id"])] = (f.stem, sp["name"], r.get("rank"), text)
    if a.regenerate:
        tips = dict(arch.get("tooltips") or {})
    else:
        tips = json.loads(pathlib.Path(a.cache).read_text(encoding="utf-8")) if a.cache else {}
        tips = {k: v for k, v in tips.items() if v and not v.startswith("ERROR")}   # (a failed fetch is asked again)
        todo = [s for s in ours if not tips.get(str(s))]
        with ThreadPoolExecutor(6) as pool:
            for sid, t in pool.map(tooltip, todo):
                if t:
                    tips[str(sid)] = t
    take, before, review, refused = {}, {}, [], []
    for sid, (cls, name, rank, text) in sorted(ours.items(), key=lambda kv: kv[1][:3]):
        live = tips.get(str(sid))
        if not live:
            continue
        raw = base_value(live)
        pre = to_level60(raw, sid, st)
        if [m.group(0) for m in ARITH.finditer(raw)] != [m.group(0) for m in ARITH.finditer(pre)]:
            # a MaxLevel number inside Wowhead's arithmetic, "( 3122 / 77 - 1 + 0)" (Flametongue Weapon rank 6's proc at level 64;
            # 2026-11-15): brought to 60 first, then worked out (35 to 112, the client's level-60 text; 40 to 125 had been taken)
            live60 = tidy(evaluate(pre))
        else:
            live60 = to_level60(tidy(evaluate(raw)), sid, st)
        a_, b_ = ([float(x.replace(",", "")) for x in NUM.findall(t)] for t in (text, live60))
        if len(a_) == len(b_) and all(abs(x - y) <= max(1.0, 0.02 * abs(x)) for x, y in zip(a_, b_)):
            continue   # the same numbers, give or take rounding (a point, or 2%)
        new = live_text(text, live60)
        if new is not None and new != text:
            why = percent_artifact(text, new)
            if why:
                refused.append((cls, name, rank, sid, text, new, why))
            else:
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
             f"60 with wowsims/forever {a.commit[:9]}'s spell data. {len(ours)} ranks; {len(take)} take the live numbers; {len(refused)} are "
             f"refused (the strike's number before its weapon percent); {len(review)} differ in wording or hold a formula or a talent switch "
             "(listed, not taken). Do not hand-edit.", "", "## Taken", ""]
    lines += [f"- {ours[int(s)][0]} / {ours[int(s)][1]} {ours[int(s)][2]} ({s}): {before[s]} -> {take[s]}" for s in take]
    lines += ["", "## Refused (Wowhead's number before the strike's weapon percent; the game applies the percent to it too)", ""]
    lines += [f"- {c} / {n} {rk} ({sid}): {why}\n  - ours: {t}\n  - live: {new}" for c, n, rk, sid, t, new, why in refused]
    lines += ["", "## Not taken (wording, formula or talent switch)", ""]
    lines += [f"- {c} / {n} {rk} ({sid}):\n  - ours: {t}\n  - live: {lv}" for c, n, rk, sid, t, lv in review]
    (out / "README.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"{len(ours)} ranks; {len(take)} take live numbers; {len(refused)} refused; {len(review)} not taken -> raw/{a.pull}/README.md")
    if a.regenerate:
        print("regenerated against the text of its day: now run build_forever_spells.py to rebuild the spellbooks from it")
    elif a.write:
        for f in sorted(SPELLS.glob("*.json")):
            d = json.loads(f.read_text(encoding="utf-8"))
            names = apply_spells(f.stem, d, a.pull)
            if names:
                f.write_text(json.dumps(d, indent=1, ensure_ascii=False), encoding="utf-8")
                print(f"  {f.stem}: {', '.join(names)}")
        # the client's mana costs, which the descriptions above never carry (2026-11-21, the audit session: the export's cost field is
        # never refreshed; client_costs.py): the pull's client build against forever-spells, fightlab/client_costs.json rewritten
        if a.build:
            try:
                import client_costs
                client_costs.main(["--build", a.build, "--fetch", "--write"])
            except (Exception, SystemExit) as e:   # noqa: BLE001 - the pull itself is done; the cost check is reported, not fatal
                print(f"WARNING: client_costs.py failed for {a.build}: {e}; run it by hand")


if __name__ == "__main__":
    main()
