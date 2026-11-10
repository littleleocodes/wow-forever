"""The town checklist page: what to do on a visit to town, drawn from the character's plan (2026-11-09, user: "an easy to look at
almost to-do list of every time I'm in a city, what spells I need to train, what my current keybind should be, what I need to level my
professions to, what recipes I need to learn, what I need to craft, what I need to buy, any upgrades ... A sort of step-by-step guide,
but an easy-to-read page").

plan.py fills plan.CTX while it writes the README and calls write(); this module adds the by-level guide's keys and fight stage
(`_reference/data/level-guides/<class>.json`) and writes `_characters/<name>/checklist.html`, a self-contained page published as a claude.ai
Artifact (its link: character.json "checklist_url"; republish the same file after every refresh). Ticks are kept in the viewer's
browser per refresh, so a new refresh starts a clean list.
"""
import hashlib
import html
import json
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent
DATA = HERE.parent
SHORT_WORD = "faster"   # "better" for a tank (render sets it from the plan)
KIND = {"dungeon": "Dungeon", "quest": "Quest", "craft": "Craft", "auction": "Auction House", "market": "Auction House", "vendor": "Vendor"}


def esc(t):
    return html.escape(str(t), quote=True)


def md(t):
    """The guides' and the plan's light markdown: **bold** and [text](link) (the link is dropped: the page stands alone)."""
    t = esc(t)
    t = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", t)
    return re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", t)


def coins(c):
    if c is None:
        return '<span class="muted">no price</span>'
    c = int(round(c))
    g, s, cp = c // 10000, c // 100 % 100, c % 100
    parts, words = [], []
    for v, cls, w in ((g, "cg", "gold"), (s, "cs", "silver"), (cp, "cc", "copper")):
        if v or (cls == "cc" and not parts):
            parts.append(f'<span class="coin {cls}">{v}</span>')
            words.append(f"{v} {w}")
    return f'<span class="money" aria-label="{" ".join(words)}">' + "".join(parts) + "</span>"


def net(c):
    """A net cost in coins, or what it makes when that is below zero."""
    return coins(c) if c is None or c >= 0 else f'<span class="gain">makes {coins(-c)}</span>'


def tid(*parts):
    return "t" + hashlib.sha1("|".join(map(str, parts)).encode("utf-8")).hexdigest()[:10]


def todo(key, body, sub=None):
    i = tid(key)
    return (f'<li class="todo"><input type="checkbox" id="{i}"><label for="{i}"><span class="box" aria-hidden="true"></span>'
            f'<span class="txt">{body}{f"<span class=sub>{sub}</span>" if sub else ""}</span></label></li>')


def info(body, sub=None):
    return f'<li class="info"><span class="txt">{body}{f"<span class=sub>{sub}</span>" if sub else ""}</span></li>'


def item(r):
    return f'<span class="q q{min(max(r.get("quality") or 2, 1), 5)}">{esc(r["item"])}</span>'


def upgrade_line(r, lv, why=True):
    when = "now" if r["level"] <= lv else f"wear at {r['level']}"
    head = f'{item(r)} <span class="slot">{esc(r["slot"])}</span> <span class="pct">{esc(r["pct"])} {esc(SHORT_WORD)}</span>'
    bits = [f"{when}", f"saves about {r['minutes']} min"]
    if r.get("until"):
        bits.append(f"until {r['until']}")
    sub = " · ".join(bits)
    if r.get("price"):
        sub += f" · {coins(r['price'])}" + (f" · {esc(r['budget'])}" if r.get("budget") else "")
    if r["kind"] == "market":
        sub += " · usually listed, not this hour" if "not this hour" in r["where"] else ""
    if r["kind"] in ("quest", "dungeon", "craft", "vendor"):
        sub += f'<br>{md(r["where"])}'
    if r.get("mats"):
        sub += f"<br>Materials: {md(r['mats'])}"
    if r.get("fallback"):
        sub += f'<br><span class="alt">{esc(r["miss"])}: {md(r["fallback"])}</span>'
    if r.get("wait"):
        sub += f'<br><strong>{md(r["wait"])}</strong>'
    if r.get("off_route"):
        sub += f'<br><span class="why">{md(r["off_route"])}</span>'
    if r.get("on_route"):
        sub += f'<br><span class="why">{md(r["on_route"])}</span>'
    if why and r.get("why"):
        sub += f'<br><span class="why">Kept long because: {md(r["why"])}</span>'
    return head, sub


def guide(cls, spec):
    p = DATA / "level-guides" / f"{cls}.json"
    if not p.exists():
        return None
    return next((g for g in json.load(open(p, encoding="utf-8"))["guides"] if g.get("spec") == spec), None)


def bars_html(g, lv):
    """The guide's keys at this level, and what arrives on them in the next six levels."""
    if not g or not g.get("keys"):
        return "", []
    out, coming = [], []
    for bar in g["keys"].get("bars") or []:
        cells = []
        for sl in bar.get("slots") or []:
            binds = sorted(sl.get("binds") or [], key=lambda b: b["from"])
            now = [b for b in binds if b["from"] <= lv]
            nxt = [b for b in binds if lv < b["from"] <= lv + 6]
            cur = now[-1] if now else None
            label = (cur.get("spell") or md(cur.get("text", ""))) if cur else ""
            new = any(b["from"] == lv or b["from"] == lv - 1 for b in now[-1:])
            cells.append(f'<div class="key{" empty" if not cur else ""}{" fresh" if new else ""}" title="{esc(sl.get("role", ""))}">'
                         f'<span class="cap">{esc(sl["key"])}</span><span class="spell">{label if cur else "free"}</span></div>')
            for b in nxt:
                coming.append((b["from"], sl["key"], b.get("spell") or re.sub(r"\*\*|\[|\]\([^)]*\)", "", b.get("text", ""))))
        out.append(f'<div class="bar"><h4>{md(bar.get("title", ""))}</h4><div class="keys">{"".join(cells)}</div></div>')
    return "".join(out), sorted(coming)


def stage_html(g, lv):
    if not g:
        return ""
    st = [s for s in g.get("stages") or [] if s["from"] <= lv]
    if not st:
        return ""
    s = st[-1]
    nxt = next((x for x in g["stages"] if x["from"] > lv), None)
    press = "".join(f"<li>{md(x)}</li>" for x in s.get("press") or [])
    notes = "".join(f"<li>{md(x)}</li>" for x in (s.get("notes") or [])[:3])
    return (f'<p class="stage-title">{md(s["title"])} <span class="muted">from level {s["from"]}</span></p><ol class="press">{press}</ol>'
            + (f'<ul class="notes">{notes}</ul>' if notes else "")
            + (f'<p class="muted small">Next change at {nxt["from"]}: {md(nxt["title"])}.</p>' if nxt else ""))


def steps_html(C, lv):
    """The town visit as numbered steps in the order you walk them (2026-11-09, user: "a to do list of almost a step by step guide. Like
    1. Make this gear 2. Do X on the auction house 3. Start working towards this piece of gear via quest or dungeon"): buy, learn,
    craft, sell, gear up, train, pick up quests, then what to work toward. A step with nothing to do is left out."""
    soon, later = C.get("soon") or [], C.get("later") or []
    profs = C.get("professions") or []
    steps = []

    # the craft steps worth doing now: those that make money (the rest is listed as the way on)
    craft_steps = [(pp, st) for pp in profs for st in pp["steps"] if st["cost"] < 0]
    mats = {}
    for pp, st in craft_steps:
        for n, k in st.get("mats") or []:
            mats[n] = mats.get(n, 0) + k
    can = {cr["item"]: cr["known"] or (cr.get("skill") or 0) <= cr["have"] for cr in C.get("crafts") or []}   # a recipe her skill
    gear_crafts = [r for r in soon if r["kind"] == "craft" and r["level"] <= lv + 3 and can.get(r["item"], True)]   # allows now

    # 1. buy
    items = []
    for r in soon:
        if r["kind"] in ("auction", "market") and r["get_at"] <= lv:
            head, sub = upgrade_line(r, lv, why=False)
            items.append(todo(f"buy{r['item']}{r['slot']}", f"Buy {head}", sub))
    for cn in C.get("consumables") or []:
        if cn["best"] and cn.get("worth") and cn.get("qty"):
            tr = C.get("trip") or {}
            items.append(todo(f"cons{cn['item']}", f"Buy ×{cn['qty']} {esc(cn['item'])} <span class=\"slot\">{esc(cn['kind'].lower())}</span>",
                              f"{coins(cn['total'])} · keeps it up for about {tr.get('minutes', 0) / 60:.1f} h of play · {esc(cn['effect'])}"))
    if mats:   # what the materials cost: the step's net cost plus what selling its products brings back
        cost = sum(st["cost"] + (st["sell"][0] * min(st["crafts"], st["sell"][1] or st["crafts"]) if st.get("sell") else 0)
                   for pp, st in craft_steps)
        gold = (C.get("gold") or {}).get("gold")
        short = gold is not None and cost > gold
        items.append(todo("mats", f"Buy the materials for your crafts below, about {coins(cost)} (less what is in your bags)",
                          ", ".join(f"{esc(n)} ×{k}" for n, k in sorted(mats.items(), key=lambda kv: -kv[1]))
                          + ("<br><strong>More than your gold:</strong> craft what your bags allow, sell it, then buy the rest" if short else "")))
    steps.append(("Auction House", "Buy", items))

    # 2. learn
    items = []
    for cr in C.get("crafts") or []:   # only what your skill lets you learn now (a higher one is a goal under Work toward)
        if not cr["known"] and cr["level"] <= lv + 8 and (cr.get("skill") or 0) <= cr["have"]:
            items.append(todo(f"learn{cr['item']}", f"Learn {esc(cr['item'])}",
                              f"{esc(cr['profession'])} {cr.get('skill') or '?'} (you have {cr['have']}) · {esc(cr.get('learn') or 'source unknown')} · "
                              f"for your {esc(cr['slot'])} at {cr['level']}"))
    for pp in profs:
        if pp.get("capped"):
            items.append(todo(f"rank{pp['name']}{pp['cap']}", f"Train the next {esc(pp['name'])} rank", f"you are at its cap, {pp['skill']}/{pp['cap']}"))
    steps.append(("Profession trainer", "Learn", items))

    # 3. craft
    items = []
    for pp, st in craft_steps:
        items.append(todo(f"skill{pp['name']}{st['from']}", f"Craft {esc(st['recipe'])} ×{st['crafts']}",
                          f"{esc(pp['name'])} {st['from']}–{st['to']} · {net(st['cost'])} after selling them"))
    for r in gear_crafts:
        head, sub = upgrade_line(r, lv, why=False)
        items.append(todo(f"craft{r['item']}", f"Craft {head}", sub))
    for pp in profs:
        rest = [st for st in pp["steps"] if st["cost"] >= 0]
        if rest:
            more = sum(st["cost"] for st in rest)
            items.append(info(f"To keep raising {esc(pp['name'])}",
                              f"next {esc(rest[0]['recipe'])} ×{rest[0]['crafts']} ({coins(rest[0]['cost'])}); "
                              f"about {coins(more)} more to reach {pp['stop']}"))
    if C.get("timeline") is not None:   # (with a route: the goals sit here, the road list holds only what leaves the guide)
        for cr in C.get("crafts") or []:
            if not cr["known"] and cr["level"] <= lv + 8 and (cr.get("skill") or 0) > cr["have"]:
                items.append(info(f"Goal: {esc(cr['profession'])} {cr['skill']} (you have {cr['have']})",
                                  f"for {esc(cr['item'])} ({esc(cr['slot'])}, level {cr['level']}) · Classic's skill; Forever often asks less"))
    steps.append(("Workbench", "Craft", items))

    # 4. sell
    items = []
    for pp, st in craft_steps:
        if st.get("product") and st.get("sell"):
            each, limit = st["sell"]
            n = min(st["crafts"], limit) if limit else st["crafts"]
            items.append(todo(f"sell{st['product']}{st['from']}", f"Sell {esc(st['product'])} ×{n}",
                              f"about {coins(each)} each after the auction house's cut (undercut today's cheapest listing) · list the rest later if they do not all sell"))
    steps.append(("Auction House", "Sell", items))

    # 5. gear up: wear and enchant
    items = []
    for r in soon:
        if r["kind"] in ("auction", "market", "craft", "vendor") and r["get_at"] <= lv:
            when = "Wear" if r["level"] <= lv else f"Keep for level {r['level']}:"
            items.append(todo(f"wear{r['item']}", f"{when} {item(r)} <span class=\"slot\">{esc(r['slot'])}</span>"))
    for e in C.get("enchants") or []:
        tx = e[2:] if e.startswith("- ") else e
        if ": skip," not in tx:
            items.append(todo(f"ench{tx[:60]}", md(tx)))
    steps.append(("Bags", "Gear up", items))

    # 6. train
    items = []
    gold = C.get("gold") or {}
    if gold.get("gold") is not None and gold.get("reserve") and gold["gold"] < gold["reserve"]:
        items.append(info(f'<strong>You are {coins(gold["reserve"] - gold["gold"])} short of your next training</strong>',
                          "sell your crafts (the Sell step) before you buy anything else"))
    tr = C.get("training") or []
    here = next((x for x in tr if x["level"] == lv), None)
    if here and here["need"]:
        items.append(todo(f"train{lv}", f"Train {', '.join(esc(n) for n in here['need'])}", f"{coins(here['cost'])} · skip what you already have"))
    nxt = next((x for x in tr if x["level"] > lv and x["need"]), None)
    if nxt:
        items.append(info(f"Keep {coins(nxt['cost'])} for level {nxt['level']}", ", ".join(esc(n) for n in nxt["need"])))
    tal = C.get("talents") or {}
    if tal.get("respec"):   # points that follow another build: respec, then the order's points so far
        items.append(todo(f"respec{lv}", "Respec at a trainer, then take " + ", ".join(f"{esc(t)} {n}" for t, n in tal["respec"]),
                          "in this order · next: " + " · ".join(f"{L} {esc(n)}" for L, n in tal["path"][:4])))
    elif tal.get("path"):
        path = " · ".join(f"{L} {esc(n)}" for L, n in tal["path"][:4])
        if tal.get("have", 0) < tal.get("want", 0):
            items.append(todo(f"talent{lv}", "Spend your talent point", path))
        else:
            items.append(info("Next talents", path))
    steps.append(("Class trainer", "Train", items))

    # 7. pick up quests before you leave (without a RestedXP route on this PC; with one, the road list below says when)
    items = []
    for r in (soon if C.get("timeline") is None else []):
        if r["kind"] == "quest":
            head, sub = upgrade_line(r, lv, why=False)
            items.append(todo(f"quest{r['item']}", f"Quest for {head}", sub))
    for dg in (C.get("dungeons") or []) if C.get("timeline") is None else []:
        if dg["run"] <= lv + 3 and dg.get("verdict") != "skip":
            qs = [q for q in dg["quests"] if not q["grey"] and not q["log"] and not q.get("route")]   # the guide picks up the rest
            if qs:
                items.append(todo(f"dq{dg['zone']}", f"Pick up the quests for {esc(dg['zone'])}"
                                  + (" your guide does not" if any(q.get("route") for q in dg["quests"]) else ""),
                                  "; ".join(f"{esc(q['title'])} ({q['level']}{', ' + esc(q['start']) if q['start'] else ''})" for q in qs)))
    steps.append(("Before you leave", "Pick up quests", items))

    # 8. work toward
    items = []
    skipped = []
    tl = C.get("timeline")
    for dg in C.get("dungeons") or []:
        if dg["run"] > lv + 3:
            continue
        if dg.get("verdict") == "skip":
            skipped.append(f"{esc(dg['zone'])} ({esc(dg['why'])})")
            continue
        if tl is None:   # (no RestedXP route on this PC: the dungeon list by level)
            items.append(todo(f"dg{dg['zone']}", f'Run <strong>{esc(dg["zone"])}</strong> at level {dg["run"]} <span class="muted">({dg["lo"]}–{dg["hi"]})</span>',
                              "once, with its quests · " + esc(dg.get("why", "")) + "".join(f"<br>Drop: {md(x)}" for x in dg["drops"])))
    for r in tl or []:   # when to leave the guide, in the route's order (plan.timeline, 2026-11-10): what, when, the facts, what to pick up
        if r["level"] <= lv + 4 or r["kind"] == "catchup":   # (a catch-up whatever its level: it keeps you in step with the guide)
            sub = (f'Level {r["level"]}, step {r["step"]} ({r["lo"]}–{r["hi"]} part): {md(r["anchor"])}<br>{md(r["facts"])}'
                   + (f' · {md(r["where"])}' if r["where"] else "")
                   + "".join(f"<br>• {md(x)}" for x in r["pickups"]))
            items.append(todo(r["key"], f'<strong>{esc(r["title"])}</strong> <span class="tag">{esc(r["tag"])}</span>', sub))
    if skipped:
        items.append(info("Skip", "; ".join(skipped)))
    for r in (soon if tl is None else []):
        if r["kind"] in ("auction", "market") and r["get_at"] > lv:
            head, sub = upgrade_line(r, lv, why=False)
            items.append(todo(f"watch{r['item']}", f"At {r['get_at']}: buy {head}", sub))
    for cr in (C.get("crafts") or []) if tl is None else []:
        if not cr["known"] and cr["level"] <= lv + 8 and (cr.get("skill") or 0) > cr["have"]:
            items.append(todo(f"goal{cr['item']}", f"Raise {esc(cr['profession'])} to {cr['skill']} (you have {cr['have']})",
                              f"to learn {esc(cr['item'])} for your {esc(cr['slot'])} at level {cr['level']} · "
                              f"{esc(cr.get('learn') or 'source unknown')} · Classic's skill; Forever is often lower, so check the trainer"))
    for r in (later[:4] if tl is None else []):
        head, sub = upgrade_line(r, lv, why=False)
        items.append(info(f"At {r['get_at']}: {KIND[r['kind']].lower()} {head}", sub))
    steps.append(("On the road", "Leave the guide for", items) if tl is not None else ("Next levels", "Work toward", items))

    out, n = [], 0
    for where, title, its in steps:
        if not its:
            continue
        n += 1
        out.append(f'<section class="card step"><h3><span class="num">{n}</span><span class="where">{esc(where)}</span>{esc(title)}</h3>'
                   f'<ul class="list">{"".join(its)}</ul></section>')
    return "".join(out)


def render(cfg, C):
    global SHORT_WORD
    h = C["head"]
    SHORT_WORD = h.get("short", "faster")
    lv = h["level"]
    g = (json.load(open(DATA.parent.parent / cfg["guide"], encoding="utf-8")) if cfg.get("guide") and (DATA.parent.parent / cfg["guide"]).exists()
         else guide(cfg["class"], h["spec"]))
    soon, later = C.get("soon") or [], C.get("later") or []
    gold = C.get("gold") or {}
    town = steps_html(C, lv)

    # right column: bars, fight, judging, gold
    bars, coming = bars_html(g, lv)
    coming_html = "".join(f"<li><strong>{L}</strong>: {esc(s)} on <span class='kbd'>{esc(k)}</span></li>" for L, k, s in coming[:6])
    judge = C.get("judge") or []
    rates = C.get("rates") or {}
    jrows = "".join(f"<tr><td>{esc(j['slot'])}</td><td>{esc(j['item'])}</td><td class='n'>{j['have']}</td><td class='n'><strong>{j['need']}</strong></td></tr>"
                    for j in judge if j["slot"] not in ("trinket1", "trinket2") or j["have"])
    by40, mount = gold.get("by40") or 0, gold.get("mount") or 1
    mbar = min(100, 100 * max(0, by40) / mount)
    ch = C.get("changes")
    if ch:
        lines = []
        if ch.get("gold_then") is not None and h.get("gold") is not None:
            lines.append(f"Gold {coins(ch['gold_then'])} then, {coins(h['gold'])} now.")
        lines.append("New in the plan: " + esc(", ".join(ch["new"])) + "." if ch["new"] else "Nothing new in the plan.")
        if ch["gone"]:
            lines.append("Left the plan: " + esc(", ".join(ch["gone"])) + ".")
        if ch["moved"]:
            lines.append("Moved: " + esc(", ".join(ch["moved"])) + ".")
        changes = f'<section class="changes"><h3>Since {esc(ch["time"])} (level {ch["level"]})</h3><p>{" ".join(lines)}</p></section>'
    else:
        changes = ""

    # coming up: the plan past the next few levels
    by_level = {}
    for r in later:
        by_level.setdefault(r["get_at"], []).append(r)
    runs_at, road_at = {}, {}
    tl = C.get("timeline")
    for dg in (C.get("dungeons") or []) if tl is None else []:
        if dg["run"] > lv + 3 and dg.get("verdict") != "skip":
            runs_at.setdefault(dg["run"], []).append(dg)
            by_level.setdefault(dg["run"], [])
    for r in tl or []:   # past the road list: the guide-leaving moments at their level
        if r["level"] > lv + 4:
            road_at.setdefault(r["level"], []).append(r)
            by_level.setdefault(r["level"], [])
    ahead = []
    for L in sorted(by_level)[:8]:
        rows = []
        for r in by_level[L]:
            price = f" · {coins(r['price'])}" if r.get("price") else ""
            rows.append(f'<li><span class="tag">{KIND[r["kind"]]}</span> {item(r)} <span class="slot">{esc(r["slot"])}</span> '
                        f'<span class="pct">{esc(r["pct"])}</span>{price}<span class="sub">{md(r["where"])}</span></li>')
        for dg in runs_at.get(L, []):
            n = len([q for q in dg["quests"] if not q["grey"] and not q.get("route")])   # the guide picks up the rest
            rows.append(f'<li><span class="tag">Dungeon</span> Run <strong>{esc(dg["zone"])}</strong>'
                        f'<span class="sub">{esc(dg.get("why", ""))} · '
                        + (f'{n} quest{"s" if n != 1 else ""} to pick up first' if n or not any(q.get("route") for q in dg["quests"])
                           else "your guide picks up its quests")
                        + "".join(f"<br>Drop: {md(x)}" for x in dg["drops"]) + "</span></li>")
        for r in road_at.get(L, []):
            rows.append(f'<li><span class="tag">{"Dungeon" if r["kind"] == "dungeon" else "Detour"}</span> <strong>{esc(r["title"])}</strong>'
                        f'<span class="sub">{esc(r["tag"])} · {md(r["facts"])}</span></li>')
        ahead.append(f'<div class="lvl"><div class="lvl-n">{L}</div><ul>{"".join(rows)}</ul></div>')

    refresh = esc(h["fetched"])
    ah = f" · auction prices {h['ah_age']:.1f} h old" if h.get("ah_age") is not None else ""
    profs = " · ".join(f"{esc(k)} {v[0]}" for k, v in h["professions"].items())
    return TEMPLATE.format(
        title=esc(f"{h['name'].split()[0]}'s Town Checklist"), refresh=refresh, name=esc(h["name"]), lv=lv,
        who=esc(f"{h['race']} {h['class']} · {h['spec']}"), gold=coins(h.get("gold")) if h.get("gold") is not None else '<span class="muted">log in for gold</span>',
        free=coins(gold.get("spend")) if gold.get("spend") is not None else "?", reserve=coins(gold.get("reserve")),
        ah=ah, profs=profs, changes=changes, town=town, bars=bars or '<p class="muted">No keybind plan for this spec yet.</p>',
        coming=f'<h4>Coming to your bars</h4><ul class="coming">{coming_html}</ul>' if coming_html else "",
        stage=stage_html(g, lv), jrows=jrows,
        rates=esc(", ".join(f"1 {k.replace('mp5', 'mana per 5 sec')} = {v}" for k, v in rates.items() if k != "armor")),
        unit=esc(C.get("unit", "spell power")),
        by40=coins(by40), mount=coins(mount), mlevel=gold.get("mount_level", 40), mbar=f"{mbar:.0f}",
        mount_at=(f"enough at level {gold['mount_at']}" if gold.get("mount_at") else "not enough on income alone"),
        share=f"{100 * (gold.get('gear_share') or 0):.0f}%", gear40=coins(gold.get("gear_before40")), at60=coins(max(0, gold.get("at60") or 0)),
        ahead="".join(ahead) or '<p class="muted">Nothing planned past the next few levels yet.</p>')


TEMPLATE = """<title>{title}</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@500;600;700&family=Atkinson+Hyperlegible:ital,wght@0,400;0,700;1,400&display=swap">
<style>
/* Layout: a sticky character bar over a town board; left the errands in the order you walk them (trainer, auction house, profession
   trainer, workbench, then the world), right your bars, your fight and the drop check; the plan past the next few levels below. */
:root {{
  --bg: #edf1f4; --panel: #ffffff; --ink: #16212b; --muted: #5b6a78; --line: #d3dbe2; --accent: #1d6aa3; --accent-soft: #e3eef7;
  --q1: #3d4853; --q2: #1d7f10; --q3: #0a5fbd; --q4: #7a2fc0; --q5: #b85a00;
  --gold: #c9a227; --silver: #a3acb6; --copper: #b06a3b; --tick: #2c7a3a; --why: #6b5a2e;
  --display: "Barlow Condensed", "Arial Narrow", "Roboto Condensed", sans-serif;
  --body: "Atkinson Hyperlegible", "Segoe UI", system-ui, sans-serif;
}}
@media (prefers-color-scheme: dark) {{ :root:not([data-theme="light"]) {{
  --bg: #0d1318; --panel: #141c23; --ink: #e3eaf0; --muted: #8e9ba8; --line: #243140; --accent: #6db4e8; --accent-soft: #15283a;
  --q1: #cfd6dd; --q2: #3fd92c; --q3: #4ea6ff; --q4: #b583ff; --q5: #ff9a3c;
  --gold: #e6c44a; --silver: #c3cad2; --copper: #d68955; --tick: #6cc77a; --why: #d9c38a; color-scheme: dark; }} }}
:root[data-theme="dark"] {{
  --bg: #0d1318; --panel: #141c23; --ink: #e3eaf0; --muted: #8e9ba8; --line: #243140; --accent: #6db4e8; --accent-soft: #15283a;
  --q1: #cfd6dd; --q2: #3fd92c; --q3: #4ea6ff; --q4: #b583ff; --q5: #ff9a3c;
  --gold: #e6c44a; --silver: #c3cad2; --copper: #d68955; --tick: #6cc77a; --why: #d9c38a; color-scheme: dark; }}
* {{ box-sizing: border-box; }}
body {{ background: var(--bg); color: var(--ink); font: 15px/1.5 var(--body); }}
body::before {{ content: ""; position: fixed; inset: 0 0 auto; height: env(safe-area-inset-top, 0px); z-index: 10; background: var(--panel); }}
.wrap {{ max-width: 1180px; margin: 0 auto; padding-block: 0 48px; padding-left: max(16px, env(safe-area-inset-left, 0px)); padding-right: max(16px, env(safe-area-inset-right, 0px)); }}
header.bar {{ position: sticky; top: env(safe-area-inset-top, 0px); z-index: 5; background: var(--panel); border-bottom: 1px solid var(--line); }}
header.bar .wrap {{ display: flex; flex-wrap: wrap; gap: 6px 22px; align-items: baseline; padding-block: 10px 10px; }}
.name {{ font: 700 1.6rem/1.1 var(--display); letter-spacing: .01em; }}
.lvl-badge {{ font: 700 1.05rem var(--display); color: var(--accent); }}
.meta {{ color: var(--muted); font-size: .86rem; }}
.stat {{ display: flex; gap: 6px; align-items: baseline; font-size: .9rem; }}
.stat b {{ font: 600 .78rem var(--display); text-transform: uppercase; letter-spacing: .08em; color: var(--muted); }}
.money {{ font-variant-numeric: tabular-nums; white-space: nowrap; }}
.coin {{ margin-right: 4px; }}
.coin::after {{ content: ""; display: inline-block; width: .58em; height: .58em; border-radius: 50%; margin-left: 2px; vertical-align: .02em; }}
.cg::after {{ background: var(--gold); }} .cs::after {{ background: var(--silver); }} .cc::after {{ background: var(--copper); }}
h2 {{ font: 700 1.05rem var(--display); text-transform: uppercase; letter-spacing: .12em; color: var(--muted); margin: 26px 0 10px; }}
.board {{ display: grid; grid-template-columns: minmax(0, 1.25fr) minmax(0, 1fr); gap: 18px; align-items: start; }}
@media (max-width: 880px) {{ .board {{ grid-template-columns: minmax(0, 1fr); }} }}
.col {{ display: grid; gap: 14px; min-width: 0; }}
.card {{ background: var(--panel); border: 1px solid var(--line); border-radius: 10px; padding: 14px 16px; min-width: 0; }}
.card h3 {{ margin: 0 0 8px; font: 700 1.2rem/1.2 var(--display); display: flex; flex-wrap: wrap; gap: 4px 10px; align-items: baseline; }}
.num {{ font: 700 1.35rem/1 var(--display); color: var(--panel); background: var(--accent); border-radius: 50%; width: 1.6em; height: 1.6em; display: inline-grid; place-items: center; flex: none; }}
.card h3:has(.num) {{ align-items: center; }}
.where {{ font: 600 .74rem var(--display); text-transform: uppercase; letter-spacing: .12em; color: var(--accent); background: var(--accent-soft); padding: 2px 7px; border-radius: 4px; }}
h4 {{ margin: 12px 0 6px; font: 600 .82rem var(--display); text-transform: uppercase; letter-spacing: .1em; color: var(--muted); }}
ul.list {{ list-style: none; margin: 0; padding: 0; display: grid; gap: 2px; }}
.todo label, .info {{ display: flex; gap: 10px; padding: 7px 4px; border-radius: 6px; }}
.todo label {{ cursor: pointer; }}
.todo label:hover {{ background: var(--accent-soft); }}
.todo input {{ position: absolute; opacity: 0; width: 1px; height: 1px; }}
.box {{ flex: none; width: 18px; height: 18px; margin-top: 2px; border: 2px solid var(--muted); border-radius: 4px; display: grid; place-items: center; }}
.todo input:checked + label .box {{ background: var(--tick); border-color: var(--tick); }}
.todo input:checked + label .box::after {{ content: ""; width: 5px; height: 9px; border: solid var(--panel); border-width: 0 2px 2px 0; transform: rotate(45deg) translate(-1px, -1px); }}
.todo input:checked + label .txt {{ opacity: .5; text-decoration: line-through; text-decoration-thickness: 1px; }}
.todo input:focus-visible + label {{ outline: 2px solid var(--accent); outline-offset: 2px; }}
.info {{ padding-left: 32px; }}
.txt {{ min-width: 0; overflow-wrap: anywhere; }}
.sub {{ display: block; color: var(--muted); font-size: .86rem; margin-top: 1px; }}
.alt {{ color: var(--ink); }}
.why {{ color: var(--why); }}
.q {{ font-weight: 700; }} .q1 {{ color: var(--q1); }} .q2 {{ color: var(--q2); }} .q3 {{ color: var(--q3); }} .q4 {{ color: var(--q4); }} .q5 {{ color: var(--q5); }}
.slot, .tag {{ font: 600 .72rem var(--display); text-transform: uppercase; letter-spacing: .08em; color: var(--muted); border: 1px solid var(--line); border-radius: 4px; padding: 0 5px; white-space: nowrap; }}
.pct {{ font: 600 .92rem var(--display); color: var(--accent); white-space: nowrap; }}
.gain {{ color: var(--tick); font-weight: 700; }}
.muted {{ color: var(--muted); }} .small {{ font-size: .85rem; }}
.skill {{ display: inline-block; width: 90px; height: 7px; border-radius: 4px; background: var(--line); vertical-align: middle; margin-left: 6px; overflow: hidden; }}
.skill span {{ display: block; height: 100%; background: var(--accent); }}
.changes {{ margin-top: 16px; border: 1px solid var(--line); border-left: 4px solid var(--accent); border-radius: 8px; background: var(--panel); padding: 10px 14px; }}
.changes h3 {{ margin: 0 0 4px; font: 700 1rem var(--display); text-transform: uppercase; letter-spacing: .08em; }}
.changes p {{ margin: 0; }}
.keys {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(96px, 1fr)); gap: 6px; }}
.key {{ border: 1px solid var(--line); border-radius: 7px; padding: 6px 7px; min-width: 0; background: var(--bg); }}
.key.fresh {{ border-color: var(--accent); box-shadow: inset 0 0 0 1px var(--accent); }}
.key.empty .spell {{ color: var(--muted); font-style: italic; }}
.cap, .kbd {{ display: inline-block; font: 700 .78rem var(--display); min-width: 1.6em; text-align: center; padding: 0 4px; border-radius: 4px; background: var(--ink); color: var(--panel); }}
.spell {{ display: block; font-size: .84rem; line-height: 1.25; margin-top: 4px; overflow-wrap: anywhere; }}
ul.coming {{ margin: 0; padding-left: 18px; }}
.stage-title {{ font: 700 1.1rem var(--display); margin: 0 0 6px; }}
ol.press {{ margin: 0; padding-left: 20px; display: grid; gap: 4px; }}
ul.notes {{ margin: 10px 0 0; padding-left: 18px; color: var(--muted); font-size: .88rem; }}
.tablewrap {{ overflow-x: auto; }}
table {{ border-collapse: collapse; width: 100%; font-size: .86rem; }}
td, th {{ text-align: left; padding: 4px 6px; border-bottom: 1px solid var(--line); }}
th {{ font: 600 .72rem var(--display); text-transform: uppercase; letter-spacing: .08em; color: var(--muted); }}
td.n, th.n {{ text-align: right; font-variant-numeric: tabular-nums; }}
.meter {{ height: 10px; border-radius: 6px; background: var(--line); overflow: hidden; margin: 6px 0; }}
.meter span {{ display: block; height: 100%; background: var(--gold); }}
.ahead {{ display: grid; gap: 10px; }}
.lvl {{ display: grid; grid-template-columns: 48px minmax(0, 1fr); gap: 10px; background: var(--panel); border: 1px solid var(--line); border-radius: 10px; padding: 10px 12px; }}
.lvl-n {{ font: 700 1.6rem/1 var(--display); color: var(--accent); }}
.lvl ul {{ list-style: none; margin: 0; padding: 0; display: grid; gap: 6px; }}
button.reset {{ font: 600 .8rem var(--display); text-transform: uppercase; letter-spacing: .08em; color: var(--accent); background: none; border: 1px solid var(--line); border-radius: 6px; padding: 4px 10px; cursor: pointer; }}
button.reset:focus-visible {{ outline: 2px solid var(--accent); }}
footer {{ color: var(--muted); font-size: .8rem; margin-top: 28px; }}
@media (prefers-reduced-motion: no-preference) {{ .todo label {{ transition: background .15s; }} }}
</style>
<header class="bar"><div class="wrap">
  <span class="name">{name}</span><span class="lvl-badge">Level {lv}</span><span class="meta">{who}</span>
  <span class="stat"><b>Gold</b>{gold}</span><span class="stat"><b>Free for gear</b>{free}</span>
  <span class="stat"><b>Keep for training</b>{reserve}</span>
</div></header>
<main class="wrap" data-refresh="{refresh}">
  {changes}
  <h2>Your steps this visit</h2>
  <div class="board">
    <div class="col">{town}</div>
    <div class="col">
      <section class="card"><h3><span class="where">Your bars</span>Keys at level {lv}</h3>{bars}{coming}</section>
      <section class="card"><h3><span class="where">The fight</span>What to press</h3>{stage}</section>
      <section class="card"><h3><span class="where">Loot check</span>Is this drop better?</h3>
        <p class="small muted">Add up a piece's stats in {unit}: {rates}. Wear it when it reaches the bold number.</p>
        <div class="tablewrap"><table><thead><tr><th>Slot</th><th>You wear</th><th class="n">Worth</th><th class="n">Beat with</th></tr></thead><tbody>{jrows}</tbody></table></div>
      </section>
      <section class="card"><h3><span class="where">Gold</span>Mount at {mlevel}</h3>
        <div class="meter" role="img" aria-label="{mbar}% of the mount by level {mlevel}"><span style="width:{mbar}%"></span></div>
        <p class="small">About {by40} by level {mlevel} of the {mount} the mount costs: {mount_at}. Gear gets {share} of each level's income after training; the plan spends {gear40} on gear before {mlevel} and reaches 60 with about {at60}.</p>
      </section>
    </div>
  </div>
  <h2>Coming up</h2>
  <div class="ahead">{ahead}</div>
  <footer><p>Refreshed {refresh}{ah} · {profs}. Generated by the character planner; numbers are the fight lab's estimates for this build, not measurements. Ticks stay in this browser until the next refresh.
  <button class="reset" type="button" id="reset">Clear ticks</button></p></footer>
</main>
<script>
(function () {{
  var root = document.querySelector("main"), key = "town-" + (root && root.dataset.refresh || "");
  var state = {{}};
  try {{ state = JSON.parse(localStorage.getItem(key) || "{{}}"); }} catch (e) {{ state = {{}}; }}
  var boxes = document.querySelectorAll(".todo input");
  boxes.forEach(function (b) {{
    b.checked = !!state[b.id];
    b.addEventListener("change", function () {{
      state[b.id] = b.checked;
      try {{ localStorage.setItem(key, JSON.stringify(state)); }} catch (e) {{}}
    }});
  }});
  var r = document.getElementById("reset");
  if (r) r.addEventListener("click", function () {{
    state = {{}};
    boxes.forEach(function (b) {{ b.checked = false; }});
    try {{ localStorage.removeItem(key); }} catch (e) {{}}
  }});
}})();
</script>
"""


def write(cfg, d, ctx):
    p = pathlib.Path(d) / "checklist.html"
    p.write_text(render(cfg, ctx), encoding="utf-8")
    return p
