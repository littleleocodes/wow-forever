"""Legacy points for the character planner (2026-11-10, user: "work on a Legacy talent build", "Yes, both" to builds, challenges and
measured perks for Arcea and Tara; "Arcea is most likely my main, and will be the one that I am leveling most of the time. Tara is my
group character").

Points are earned account-wide from challenges (achievements; `legacy_challenges.json`: the client's TraitCurrencySource rows for currency
4225, build 70888, with Blizzard's static achievement names and criteria; the client lists each challenge under two id ranges, a challenge
counts when either is complete) and each character spends up to 16 of them in its own three trees. The planner reads the account's
progress from the character's achievements (bnet.py's /achievements part; account-wide) and the character's spend order from
character.json "legacy" {"order": [[perk, ranks], ...], "why": text}. Measured values: legacy_value.py (`legacy/<character>.json`).
"""
import json
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent.parent.parent
CAP = 16   # TraitCurrency 4225 SourcedMax: points a character can spend (launch)
CHALLENGES = json.load(open(HERE / "legacy_challenges.json", encoding="utf-8"))["challenges"]


def status(ach, level_of=None):
    """{"points", "done": [names], "next": [(fraction done, text)]} from an achievements document (account-wide progress) and
    {class name: (character, level)} of the account's characters the planner knows (class-level challenges carry no progress)."""
    mine = {}
    for doc in (ach if isinstance(ach, list) else [ach]):   # every character's document: one shows what another lacks
        for a in (doc or {}).get("achievements", []):
            old = mine.get(a["id"])
            if old is None or (a.get("completed_timestamp") and not old.get("completed_timestamp")):
                mine[a["id"]] = a
            elif not old.get("completed_timestamp"):
                ka = {k["id"]: k for k in (a.get("criteria") or {}).get("child_criteria", [])}
                for k in (old.get("criteria") or {}).get("child_criteria", []):
                    if k["id"] in ka:
                        k["amount"] = max(k.get("amount", 0), ka[k["id"]].get("amount", 0))
                        k["is_completed"] = k.get("is_completed") or ka[k["id"]].get("is_completed")
    by_name = {}
    for c in CHALLENGES:
        by_name.setdefault(c["name"], []).append(c)
    done, nxt = [], []
    for name, cs in by_name.items():
        got = [mine.get(c["id"]) for c in cs if mine.get(c["id"])]
        if any(g.get("completed_timestamp") for g in got):
            done.append(name)
            continue
        c = cs[0]
        m = re.match(r"Reach (\d+) skill in (\w+)", c["requirement"])
        if m:
            need, prof = int(m.group(1)), m.group(2)
            have = max([k.get("amount", 0) for g in got for k in (g.get("criteria") or {}).get("child_criteria", [])] or [0])
            if have:
                nxt.append((have / need, f"{name}: {prof} {have}/{need}", prof, need))
            continue
        m = re.match(r"Reach Level (\d+) for the first time on an? (\w+)", c["requirement"])
        if m:
            need, cls = int(m.group(1)), m.group(2)
            who = (level_of or {}).get(cls)
            if who and who[1] < need:
                nxt.append((who[1] / need, f"{name}: {who[0]} {who[1]}/{need}", cls, need))
            continue
        if c["parts"] and "Spelunker" in name:
            ids = {k["id"] for k in c["parts"]}
            crit = {}
            for g in got:
                for k in (g.get("criteria") or {}).get("child_criteria", []):
                    crit[k["id"]] = k.get("is_completed")
            for alt in cs[1:]:   # the other id range's parts, by position
                for k0, k1 in zip(c["parts"], alt["parts"]):
                    if crit.get(k1["id"]):
                        crit[k0["id"]] = True
            left = [k["text"] for k in c["parts"] if not crit.get(k["id"])]
            if len(left) < len(ids):
                nxt.append(((len(ids) - len(left)) / len(ids), f"{name}: {len(ids) - len(left)} of {len(ids)} dungeons; left: {', '.join(left)}", name, 0))
    first = {}
    for x in nxt:   # only the closest open step of each track (Journeyman before Expert, level 25 before 45)
        if x[2] not in first or x[3] < first[x[2]][3]:
            first[x[2]] = x
    nxt = sorted(((f, t) for f, t, _, _ in first.values()), key=lambda x: -x[0])
    return {"points": len(done), "done": sorted(done), "next": nxt}


def spend(points, order):
    """[(perk, ranks)] the first min(points, CAP) points of the order buy."""
    left, out = min(points, CAP), []
    for perk, ranks in order:
        if left <= 0:
            break
        n = min(ranks, left)
        out.append((perk, n, ranks))
        left -= n
    return out


def measured(character):
    p = HERE / "legacy" / f"{character}.json"
    return json.load(open(p, encoding="utf-8")) if p.exists() else None


def section(cfg, ach, level_of):
    """(markdown lines, checklist context) of the character's Legacy points, or ([], None) without an order in character.json."""
    lg = cfg.get("legacy")
    if not lg or not ach:
        return [], None
    st = status(ach, level_of)
    buy = spend(st["points"], lg["order"])
    order_txt = " → ".join(f"{p} {r}" for p, r in lg["order"])
    o = ["## Legacy", "",
         f"**{st['points']} Legacy point{'s' if st['points'] != 1 else ''}** on the account (earned once, every character spends them; up to "
         f"{CAP} each). " + ("Spend them: " + ", ".join(f"**{p}** {n}/{r}" for p, n, r in buy) + "." if buy else ""), "",
         f"Order: {order_txt}. {lg.get('why', '')}".strip(), ""]
    m = measured(cfg["name"])
    if m:
        lv = {int(k): v for k, v in m["levels"].items()}
        rows = [f"{L} {100 * (r['base'] - r['thrill']) / r['base']:.0f}% / {100 * (r['base'] - r['talented']) / r['base']:.0f}%"
                for L, r in sorted(lv.items()) if L >= m["from"] - 3]
        o += [f"Fight lab ({m['date']}, the page build): time per kill saved by Thrill of Adventure 5/5 / Talented 5/5 at level "
              + ", ".join(rows) + f". From {m['from']} to 60: Thrill about {m['minutes_saved']['thrill']:.0f} min of killing, Talented about "
              f"{m['minutes_saved']['talented']:.0f} min if held from {m['from']}, both {m['minutes_saved']['both']:.0f} (of "
              f"{m['killing_minutes']:.0f} min of killing). A model of the beta, not a measurement.", ""]
    if st["next"]:
        o += ["Closest next points: " + "; ".join(t for _, t in st["next"][:5]) + ".", ""]
    return o, {"points": st["points"], "buy": buy, "next": [t for _, t in st["next"][:4]], "order": lg["order"]}
