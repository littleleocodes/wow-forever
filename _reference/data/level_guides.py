"""Leveling guides by level: the rotation from level 1 to 60 as each spell and talent arrives (2026-11-06, user request: "Can you make a
leveling guide for each class? What the rotation should be throughout the leveling process as more spells are unlocked? Starting with
Mage and Paladin").

    python -u _reference/data/level_guides.py [classes] --measure [--jobs 4]   # the fight lab at each stage's levels (a few minutes)
    python -u _reference/data/level_guides.py [classes] --check                # validate the hand-kept guides against the data
    python -u _reference/data/level_guides.py [classes] --write                # the pages now (render_modes.py writes them at every regen)

A spec's leveling page (render_modes.py) shows one rotation, the level-60 one. This adds the way there. Hand-kept, per class:
`_reference/data/level-guides/<class>.json` = {"guides": [{"spec": the spec page it belongs to, "intro", "stages": [{"from": first
level, "title", "change": one line for the overview table, "press": the priority list of that stretch, "if_hurt": the emergency line, "notes": []}], "between": [],
"other": []}]}. Everything else on the page is read from the data, so it follows the builds and the spellbook:
  * the build is the spec's leveling page pick (fightlab/signature_audit.page_slots, as the pages rank it) with its talent order; a
    pick without an order (a class whose leveling search has not run on the current data) gets the stats model's order with the
    signature talents first (fl_signature.sig_order), and the page says the talents are provisional;
  * per stage: the spells the trainer teaches in those levels and the new ranks of the spells the stage presses
    (forever-spells/<class>.json), the talents the order takes there, and the fight lab's seconds per kill and presses per kill at the
    stage's levels (`--measure`, record `level-guides/<class>.measured.json`, shown only while its fingerprint matches the build, its
    order and the rotation's tuned rules);
  * `--check` (also run by --write): every bold name is a spell or talent of the class; a spell a stage tells you to press is
    trained by the stage's first level, a talent taken by then in the build's order; warnings for a combat spell the lab presses in
    a stage that the stage never names, and for a pressed spell the lab never casts there.
The fight lab is this project's model of stated assumptions (green gear, same-level mobs, one mob per pull), not in-game play. Levels
1-9 are before talents; a rotation whose main spell is trained later (Frostbolt at 4) is not simulated below that level.
Pages: `<class>/leveling/<spec slug>-by-level.md`, linked from the spec's leveling page and the class's leveling index.
"""
import argparse
import datetime
import hashlib
import json
import multiprocessing
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[1]
sys.path[:0] = [str(HERE / "fightlab"), str(HERE / "scorer"), str(HERE)]
import data_build as DB  # noqa: E402
import paths  # noqa: E402
import signature as SG  # noqa: E402
import spec_modes as SM  # noqa: E402

DIR = HERE / "level-guides"
FIGHTS, SEED = 400, 3
BOLD = re.compile(r"\*\*([^*]+)\*\*")
PLAIN = {"wand", "Wand", "Auto Shot", "melee", "Melee"}   # bold words that are no spell of the book
KEYBINDS = "keybinds.md"   # hand-written, in the class's generated leveling folder: render_modes.py's cleanup leaves it (2026-11-07)
NOISE = ("Portal: ", "Teleport: ")                       # trained spells left out of the "you train" lines
TODAY = datetime.date.today().isoformat()


def load(cls):
    p = DIR / f"{cls}.json"
    return json.load(open(p, encoding="utf-8")) if p.exists() else None


def classes():
    return sorted(p.stem for p in DIR.glob("*.json") if not p.stem.endswith(".measured")) if DIR.exists() else []


_BOOK = {}


def book(cls):
    """{spell: sorted trainer levels of its ranks} (forever-spells; a talent's spell keeps the levels its ranks are trained)."""
    if cls not in _BOOK:
        out = {}
        for tab in json.load(open(HERE / "forever-spells" / f"{cls}.json", encoding="utf-8")).get("tabs", []):
            for s in tab.get("spells", []):
                lv = sorted(int(r["level"]) for r in s.get("ranks", []) if r.get("level") is not None)
                if lv:
                    out[s["name"]] = sorted(set(out.get(s["name"], []) + lv))
        _BOOK[cls] = out
    return _BOOK[cls]


_PETS = {}


def racial_spells(cls):
    """{spell: race} for a class's race-only spells: the fight-lab module's RACIAL_SPELLS (the priest's, 2026-10-09)."""
    p = HERE / "fightlab" / f"{cls}.py"
    if not p.exists():
        return {}
    m = re.search(r"^RACIAL_SPELLS = (\{.*?\})\s*$", p.read_text(encoding="utf-8"), re.S | re.M)
    try:
        import ast
        return ast.literal_eval(m.group(1)) if m else {}
    except (ValueError, SyntaxError):
        return {}


def pet_spells(cls):
    """The spells of the class spellbook's "Pets" or "Demons" tab (the hunter's and the warlock's pet abilities): the pet casts them, the player never presses them."""
    if cls not in _PETS:
        _PETS[cls] = {s["name"] for tab in json.load(open(HERE / "forever-spells" / f"{cls}.json", encoding="utf-8")).get("tabs", [])
                      if tab.get("name") in ("Pets", "Demons") for s in tab.get("spells", [])}   # the warlock's tab is "Demons" (2026-11-07)
    return _PETS[cls]


def fightlab_signature_audit():
    """fightlab/signature_audit.py loaded by its path: raidsim/ has a signature_audit.py too, and inside render_modes.py (which puts
    raidsim/ at the front of sys.path for the raid pages) a plain import found that one (2026-11-06: the first regen with the by-level
    hook died on it and left the class's leveling folder without its guide)."""
    import importlib.util
    name = "fightlab_signature_audit"
    if name not in sys.modules:
        spec = importlib.util.spec_from_file_location(name, HERE / "fightlab" / "signature_audit.py")
        mod = importlib.util.module_from_spec(spec)
        sys.modules[name] = mod
        spec.loader.exec_module(mod)
    return sys.modules[name]


def pick(cls, spec):
    """(build, order, provisional, rotation): the spec's leveling page pick; an order-less pick gets the stats model's order."""
    SA = fightlab_signature_audit()
    import fl_signature as FS
    import fl_talent_opt as FT
    import derive_leveling as DL
    slot = next((s for s in SA.page_slots(cls) if s[0] == spec), None)
    if not slot or not slot[1]:
        return None, None, False, None
    b = slot[1][0]
    rot = slot[2][b["id"]]
    if b.get("order"):
        return b, b["order"], False, rot
    model = DL.LEVEL[(cls, spec)][1] if (cls, spec) in DL.LEVEL else rot
    order = FT.order_of(cls, model, FT.flat_of(b))
    sig = getattr(FS, "sig_order", None)   # (the signature-talents-first order of 2026-11-06; a tree without it keeps the stats model's)
    return b, (sig(cls, rot, {"allocation": b["allocation"], "order": order}, spec) if sig else order), True, rot


def fingerprint(cls, b, order, rot):
    import fl_signature as FS
    key = json.dumps([b["id"], sorted(SG.held(b).items()), order, rot, FS.rules_fingerprint(cls, rot), DB.BUILD], sort_keys=True)
    return hashlib.sha1(key.encode("utf-8")).hexdigest()[:12]


def stages(g):
    st = sorted(g["stages"], key=lambda s: s["from"])
    return [dict(s, to=(st[i + 1]["from"] - 1 if i + 1 < len(st) else 60)) for i, s in enumerate(st)]


def stage_levels(s):
    """The levels a stage is measured at: its first, every tenth inside it, its last when it is long."""
    lv = {s["from"]} | {L for L in range(s["from"], s["to"] + 1) if L % 10 == 0}
    if s["to"] - s["from"] >= 5:
        lv.add(s["to"])
    return sorted(lv)


def bold_names(s):
    return [n for txt in [s.get("change", ""), s.get("if_hurt", "")] + s.get("press", []) + s.get("notes", []) for n in BOLD.findall(txt)]


def learned(cls, name, build):
    """The level a build can first use a spell or talent: a talent (or its spell) from the build's order, a trained spell from the
    trainer; None when the build does not take the talent, -1 when the name is no spell or talent of the class."""
    if name in SG.talent_names(cls):
        return SG.learn_level(cls, name, build)
    if name in book(cls):
        return book(cls)[name][0]
    return -1


# ------------------------------------------------------------------------------------------------ measure
def _init():
    import run as FR
    FR.apply_gear("greens")


def _job(a):
    import run as FR
    cls, rot, alloc, level = a
    try:
        r = FR.simulate(cls, alloc, level, rot, FIGHTS, SEED, 0)
    except Exception as e:   # noqa: BLE001
        return {"error": f"{type(e).__name__}: {e}"}
    k = max(1, r.get("kills") or 1)
    return {"seconds": round(r["time_per_kill"], 1), "deaths_per_100": r.get("deaths_per_100"),
            "casts": {s: round(n / k, 2) for s, n in (r.get("casts") or {}).items() if n / k >= 0.05}}


def measure(cls, jobs):
    import run as FR
    data = load(cls)
    rec = {"class": cls, "date": TODAY, "fights": FIGHTS, "seed": SEED, "guides": {}}
    with multiprocessing.Pool(jobs, initializer=_init) as pool:
        for g in data["guides"]:
            b, order, prov, rot = pick(cls, g["spec"])
            if not b:
                print(f"== {cls} {g['spec']}: no leveling build on its page; skipped", flush=True)
                continue
            ob = {"allocation": b["allocation"], "order": order}
            levels = sorted({L for s in stages(g) for L in stage_levels(s)})
            res = pool.map(_job, [(cls, rot, FR.allocation_at(ob, L) if L >= 10 else {}, L) for L in levels], chunksize=1)
            rec["guides"][g["spec"]] = {"build": b["id"], "rotation": rot, "provisional_order": prov, "fingerprint": fingerprint(cls, b, order, rot),
                                        "levels": {str(L): r for L, r in zip(levels, res)}}
            print(f"== {cls} {g['spec']} ({b['id']}, {rot}{', a provisional order' if prov else ''}): "
                  + ", ".join(f"L{L} {r.get('seconds', 'ERR')}" for L, r in zip(levels, res)), flush=True)
    (DIR / f"{cls}.measured.json").write_text(json.dumps(rec, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")


def measured(cls, spec, b, order, rot):
    p = DIR / f"{cls}.measured.json"
    m = (json.load(open(p, encoding="utf-8")).get("guides") or {}).get(spec) if p.exists() else None
    return m if m and m.get("fingerprint") == fingerprint(cls, b, order, rot) else None


# ------------------------------------------------------------------------------------------------ keybinds by level
# 2026-11-06 (user: "help set up keybinds again for mage and paladin but it depends on level ... which spells should be on which
# keybinds dependent on what I currently have unlocked and what the rotation for that level is"). A guide's optional "keys" block:
# {"intro", "slots": [{"key", "role", "binds": [{"from": level, "spell": a spell of the class | "text": anything else, "only": a
# qualifier}]}], "no_key": [spells cast by clicking], "notes": []}. A key keeps its job for the whole climb; the spell on it changes
# as better ones arrive (Q: Fireball, then Frostbolt from 4), so nothing learned has to be unlearned.
def bind_name(b):
    return b.get("spell") or b.get("text") or ""


def key_slots(keys):
    """Every slot of a keys block: its "slots", or the slots of its "bars" ([{"title", "slots"}]: the player's action bars in their
    own slot order; the page prints one table per bar)."""
    return [k for bar in keys.get("bars", []) for k in bar["slots"]] + list(keys.get("slots", []))


def key_cell(slot, lo, hi):
    """What sits on a key during levels lo-hi: the bind in force at lo, then every change inside the stage. A bind that arrives in the
    stage is bold: it is what to set up there."""
    binds = sorted(slot["binds"], key=lambda b: b["from"])
    parts = []
    cur = [b for b in binds if b["from"] <= lo]
    if cur:
        t = bind_name(cur[-1]) + (f" ({cur[-1]['only']})" if cur[-1].get("only") else "")
        parts.append(f"**{t}**" if cur[-1]["from"] == lo else t)
    parts += [f"**{bind_name(b)}** from {b['from']}" + (f" ({b['only']})" if b.get("only") else "") for b in binds if lo < b["from"] <= hi]
    return "; ".join(parts) or "—"


def key_holding(keys, level):
    """{spell: key} for the binds in force at a level."""
    out = {}
    for k in key_slots(keys):
        cur = [b for b in sorted(k["binds"], key=lambda b: b["from"]) if b["from"] <= level]
        if cur and cur[-1].get("spell"):
            out[cur[-1]["spell"]] = k["key"]
    return out


# ------------------------------------------------------------------------------------------------ check
TALENT_AT = re.compile(r"\*\*([^*]+)\*\* \(((?:\d+(?:-\d+)?)(?:, \d+(?:-\d+)?)*)\)")


def _levels(text):
    out = set()
    for part in str(text).split(","):
        a, _, z = part.strip().partition("-")
        out |= set(range(int(a), int(z or a) + 1))
    return out


def stale_levels(cls, g, b, order):
    """Talents a guide text places at levels the build's order does not (2026-11-09 audit W22: the Protection warrior's guide kept the
    levels of the build its page showed before, "**Iron Will** (10)", "**Cruelty** (43-47)", and no check read them): every
    "**Talent** (a-b, c)" with levels 10+ against the order's levels for that talent."""
    out = []
    held = {n for items in b["allocation"].values() for n, r in items if r}
    texts = [g.get("intro", "")] + g.get("between", []) + g.get("other", [])
    for s in g.get("stages", []):
        texts += [s.get("change", ""), s.get("if_hurt", "")] + s.get("press", []) + s.get("notes", [])
    tnames = SG.talent_names(cls)
    for txt in texts:
        for m in TALENT_AT.finditer(txt or ""):
            n, lv = m.group(1), _levels(m.group(2))
            if n not in tnames or min(lv) < 10:
                continue
            if n not in held:
                out.append(f"places **{n}** at {m.group(2)}; the build ({b['id']}) does not take it")
                continue
            want = set()
            for step in order or []:
                if step.get("talent") == n:
                    want |= _levels(step["levels"])
            if want and not lv <= want:   # a stage may name some of the talent's levels (Ice Shards 24, 26-27, then 32-33)
                out.append(f"places **{n}** at {m.group(2)}; the order takes it at {', '.join(str(x) for x in sorted(want))}")
    return out


def check(cls):
    """[(level of the problem: 'error' or 'warning', text)] for a class's guides."""
    out = []
    data = load(cls)
    for g in data["guides"]:
        b, order, prov, rot = pick(cls, g["spec"])
        if not b:
            out.append(("error", f"{g['spec']}: no leveling build on its page"))
            continue
        for t in stale_levels(cls, g, b, order):
            out.append(("error", f"{g['spec']}: the guide {t}"))
        ob = {"allocation": b["allocation"], "order": order}
        m = measured(cls, g["spec"], b, order, rot)
        if not m:
            out.append(("warning", f"{g['spec']}: no fight-lab numbers for the current build, order and rules (run --measure)"))
        for n in sorted({n for txt in [g.get("intro", "")] + g.get("between", []) + g.get("other", []) for n in BOLD.findall(txt)}):
            if n not in PLAIN and learned(cls, n, ob) == -1:
                out.append(("error", f"{g['spec']} (intro, between or other): **{n}** is no spell or talent of the class"))
        keys = g.get("keys")
        for k in (key_slots(keys) if keys else []):   # a bound spell is known at the level its bind starts (a talent: in the build's order)
            for bd in k["binds"]:
                n = bd.get("spell")
                if not n:
                    continue
                lv = learned(cls, n, ob)
                if lv == -1:
                    out.append(("error", f"{g['spec']} key {k['key']}: **{n}** is no spell or talent of the class"))
                elif lv is None:
                    if not bd.get("only"):
                        out.append(("error", f"{g['spec']} key {k['key']}: **{n}** is a talent the build ({b['id']}) does not take"))
                elif lv > bd["from"]:
                    out.append(("error", f"{g['spec']} key {k['key']}: **{n}** arrives at level {lv}, its bind starts at {bd['from']}"))
        for s in stages(g):
            tag = f"{g['spec']} levels {s['from']}-{s['to']}"
            pressed = {n for txt in s.get("press", []) for n in BOLD.findall(txt)}
            if keys:   # every spell the stage presses, in the list or in the emergency line, has a key by then
                held_ = key_holding(keys, s["from"])
                for n in sorted((pressed | set(BOLD.findall(s.get("if_hurt", "")))) & set(book(cls))):
                    if n not in held_ and n not in keys.get("no_key", []):
                        out.append(("warning", f"{tag}: the stage presses **{n}** and no key holds it"))
            hurt = set(BOLD.findall(s.get("if_hurt", "")))   # the emergency line: must be known, need not be cast in the lab
            for n in sorted(set(bold_names(s))):
                if n in PLAIN:
                    continue
                lv = learned(cls, n, ob)
                if lv == -1:
                    out.append(("error", f"{tag}: **{n}** is no spell or talent of the class"))
                elif lv is None:
                    if n in pressed | hurt:
                        out.append(("error", f"{tag}: **{n}** is a talent the build ({b['id']}) does not take"))
                elif n in pressed | hurt and lv > s["from"]:
                    out.append(("error", f"{tag}: **{n}** arrives at level {lv}, after the stage begins"))
            if m:
                cast = {}
                for L in stage_levels(s):
                    for sp, n in ((m["levels"].get(str(L)) or {}).get("casts") or {}).items():
                        cast[sp] = max(cast.get(sp, 0), n)
                named = set(bold_names(s))
                for sp, n in sorted(cast.items()):
                    if n >= 0.2 and sp not in named and sp not in PLAIN and sp in book(cls) and sp not in pet_spells(cls):
                        out.append(("warning", f"{tag}: the fight lab presses {sp} {n:.1f} times a kill and the stage never names it"))
                for n in sorted(pressed):
                    if n in book(cls) and n not in cast and s["from"] >= 10 and not (s.get("unsimulated") and n in s["unsimulated"]):
                        out.append(("warning", f"{tag}: the stage presses **{n}** and the fight lab never casts it there"))
    return out


# ------------------------------------------------------------------------------------------------ render
def page_name(cls, spec):
    return f"{SM.spec_slug(cls, spec)}-by-level.md"


def render(cls, g):
    import render_start_here as RSH
    spec = g["spec"]
    b, order, prov, rot = pick(cls, spec)
    if not b:
        return None
    ob = {"allocation": b["allocation"], "order": order}
    m = measured(cls, spec, b, order, rot)
    split = "/".join(str(x) for x in SM.tree_points(cls, b).values())
    name = SM.spec_name(cls, spec)
    o = [f"# {name} {cls.capitalize()} — leveling, level by level", "",
         f"[{cls.capitalize()}](../README.md) > [Leveling (solo)](README.md) > [{name}]({SM.spec_slug(cls, spec)}.md) > Level by level", "",
         g.get("intro", ""), "",
         f"**The build:** {split} ([open the talent tree]({RSH.tf_link(cls, SG.held(b))})), the one on the [{name} leveling page]({SM.spec_slug(cls, spec)}.md), "
         "which has the full talent table and the reasons behind the level-60 rotation.", ""]
    if prov:
        o += [f"> **Provisional talents.** The {cls}'s leveling search has not run on the current game data yet, so the page's build has no "
              "talent order of its own. The talent levels below follow the stats model's order and will change when the search finishes; "
              "the spells the trainer teaches, and when to press them, will not.", ""]
    st = stages(g)
    o += ["## The short version", "", "| Level | What changes |", "|---|---|"]
    o += [f"| {s['from']}{'' if s['from'] == s['to'] else '-' + str(s['to'])} | {s.get('change', s['title'])} |" for s in st]
    o += [""]
    keys = g.get("keys")
    if keys:   # the keybinds by level (see "keybinds by level" above): one row per key, one column per stage
        o += ["## Keybinds by level", ""] + ([keys["intro"], ""] if keys.get("intro") else [])
        for bar in (keys.get("bars") or [{"title": None, "slots": keys.get("slots", [])}]):
            if bar.get("title"):
                o += [f"**{bar['title']}**", ""]
            o += ["| Key | Its job | " + " | ".join(f"{s['from']}{'' if s['from'] == s['to'] else '-' + str(s['to'])}" for s in st) + " |",
                  "|---|---|" + "---|" * len(st)]
            o += [f"| {k['key']} | {k.get('role', '')} | " + " | ".join(key_cell(k, s["from"], s["to"]) for s in st) + " |" for k in bar["slots"]]
            o += [""]
        o += [f"- {t}" for t in keys.get("notes", [])] + ([""] if keys.get("notes") else [])
    for s in st:
        lo, hi = s["from"], s["to"]
        pressed = {n for txt in s.get("press", []) for n in BOLD.findall(txt)}
        o += [f"## Levels {lo}-{hi}: {s['title']}" if lo != hi else f"## Level {lo}: {s['title']}", ""]
        new = sorted(((lv[0], n) for n, lv in book(cls).items() if lo <= lv[0] <= hi and n not in SG.talent_names(cls)
                      and not n.startswith(NOISE)), key=lambda x: x)
        if new:   # a race-only spell says whose (2026-11-08 full page read PR12: Dark Sacrifice, Starshards ... listed for every priest)
            race = racial_spells(cls)
            o += ["**The trainer teaches:** " + ", ".join(f"{'**' + n + '**' if n in pressed else n} ({lv}" + (f", {race[n]} only" if n in race else "") + ")"
                                                         for lv, n in new) + ".", ""]
        # every spell you press, keep for emergencies or hold on a key gets its new ranks (2026-11-09 audit P16: the paladin's Divine
        # Protection, Blessing of Protection, Lay on Hands and Divine Shield sat on keys and their ranks were never listed)
        buy = pressed | set(BOLD.findall(s.get("if_hurt", "")))
        if keys:
            for L in range(lo, hi + 1):
                buy |= set(key_holding(keys, L))
        ranks = sorted((n, [x for x in book(cls)[n][1:] if lo <= x <= hi]) for n in buy if n in book(cls))
        ranks = [(n, lv) for n, lv in ranks if lv]
        if ranks:
            o += ["**New ranks to buy:** " + "; ".join(f"{n} at {', '.join(map(str, lv))}" for n, lv in ranks) + ".", ""]
        tal = []
        for step in order:
            a, z = int(str(step["levels"]).split("-")[0]), int(str(step["levels"]).split("-")[-1])
            if a <= hi and z >= lo:
                a2, z2 = max(a, lo), min(z, hi)
                tal.append(f"{a2}{'' if a2 == z2 else '-' + str(z2)} {step['talent']}")
        if tal:
            o += ["**Talents:** " + ", ".join(tal) + ".", ""]
        if keys:   # what to put on the bar in this stage, and the key of every spell the list below presses
            slot_no = {k["key"]: i for i, k in enumerate(key_slots(keys))}
            new = sorted(((bd["from"], k["key"], bd) for k in key_slots(keys) for bd in k["binds"] if lo <= bd["from"] <= hi),
                         key=lambda x: (x[0], slot_no[x[1]]))
            if new:
                o += ["**Keys to set:** " + "; ".join(f"{key} = {bind_name(bd)}" + (f" (at {lv})" if lv != lo else "")
                                                        + (f", {bd['only']}" if bd.get("only") else "") for lv, key, bd in new) + ".", ""]
            held_ = key_holding(keys, lo)
            used = sorted(((n, held_[n]) for n in pressed | set(BOLD.findall(s.get("if_hurt", ""))) if n in held_), key=lambda x: slot_no[x[1]])
            if used:
                o += ["**Your keys in this stage:** " + ", ".join(f"{key} {n}" for n, key in used) + ".", ""]
        o += ["**What to press**, top to bottom:", ""] + [f"{i}. {t}" for i, t in enumerate(s.get("press", []), start=1)] + [""]
        if s.get("if_hurt"):
            o += [f"**If the fight goes wrong:** {s['if_hurt']}", ""]
        o += [f"- {t}" for t in s.get("notes", [])] + ([""] if s.get("notes") else [])
        if m:
            rows = [(L, m["levels"].get(str(L)) or {}) for L in stage_levels(s)]
            rows = [(L, r) for L, r in rows if r.get("seconds") and not (s.get("unsimulated") and L < 10)]
            if rows and not s.get("no_numbers"):
                L, r = rows[0]
                casts = ", ".join(f"{sp} {n:.1f}" for sp, n in sorted(r["casts"].items(), key=lambda kv: -kv[1]))
                o += ["*Fight lab, seconds per kill: " + ", ".join(f"{r_['seconds']:.0f} at level {L_}" for L_, r_ in rows)
                      + f". Presses per kill at level {L}: {casts}.*", ""]
    if g.get("between"):
        o += ["## Between fights", ""] + [f"- {t}" for t in g["between"]] + [""]
    if g.get("other"):
        o += ["## Other ways to level this class", ""] + [f"- {t}" for t in g["other"]] + [""]
    o += ["---", f"*Generated by `_reference/data/level_guides.py` on {TODAY}: the stages are hand-kept in "
          f"`_reference/data/level-guides/{cls}.json`; trainer levels, talents and numbers are read from this project's data (client build "
          f"{DB.BUILD}) and its fight lab (green gear, same-level mobs, one mob per pull, {FIGHTS} fights per level). A simulation of stated "
          "assumptions, not in-game measurements. Do not hand-edit.*", ""]
    return "\n".join(o)


def write(cls, folder=None):
    """Write the class's by-level pages into its leveling folder; returns [(spec, file name)] (render_modes.py calls this at a regen)."""
    data = load(cls)
    out = []
    if not data:
        return out
    folder = pathlib.Path(folder) if folder else ROOT / cls / "leveling"
    for g in data["guides"]:
        text = render(cls, g)
        if text:
            (folder / page_name(cls, g["spec"])).write_text(text, encoding="utf-8")
            out.append((g["spec"], page_name(cls, g["spec"])))
    return out


def keybinds_line(cls):
    """The line that points at the class's hand-written keybinds page, else None."""
    if (ROOT / cls / "leveling" / KEYBINDS).exists():
        return f"**Keybinds:** [Your keys and macros]({KEYBINDS}), set out on your two action bars."
    return None


def macros_line(cls):
    """The line that points at the class's hand-written macro page, else None."""
    if (ROOT / cls / "macros.md").exists():
        return "**Macro ideas:** [every spec's macros](../macros.md), with the keys each one frees."
    return None


def link_line(cls, spec):
    """The line a spec's leveling page carries when the class has a by-level guide for it, else None."""
    data = load(cls)
    if data and any(g["spec"] == spec for g in data["guides"]):
        line = (f"**Leveling from level 1?** [The rotation level by level]({page_name(cls, spec)}): what to press as each spell and talent "
                "arrives.")
        return line + (f" [Your keys and macros]({KEYBINDS})." if keybinds_line(cls) else "")
    return None


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("classes", nargs="*")
    ap.add_argument("--measure", action="store_true")
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--write", action="store_true")
    ap.add_argument("--jobs", type=int, default=4)
    a = ap.parse_args()
    bad = 0
    for cls in a.classes or classes():
        if not load(cls):
            print(f"== {cls}: no guide ({DIR / (cls + '.json')})")
            continue
        if a.measure:
            measure(cls, a.jobs)
        if a.check or a.write:
            probs = check(cls)
            for lvl, txt in probs:
                print(f"  {cls} {lvl}: {txt}")
            bad += sum(1 for lvl, _ in probs if lvl == "error")
            print(f"== {cls}: {sum(1 for l, _ in probs if l == 'error')} errors, {sum(1 for l, _ in probs if l == 'warning')} warnings")
        if a.write:
            for spec, name in write(cls):
                print(f"  wrote {cls}/leveling/{name}")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
