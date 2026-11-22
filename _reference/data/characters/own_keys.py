"""A character's own key layout (2026-11-22, Arcea: one layout for questing and for fighting players).

The user, to the audit session: "I want the keybinds to be both practical for Arcea questing and PvP. This doesn't need tyo be the
default for everything, just specific for this case", then "I think X, C, and V can be utlized more."

character.json `keys` holds the layout in the by-level guides' shape: bars of slots, each slot's binds by level ({"from", "spell"} or
{"from", "text"}; no bind yet = a free key). It adds what the guides' keys lack:
- per slot: `kind` (how it is pressed), `why` (why this key), `was` (its key on the old bars, for the rebind list) and, for a
  slot macro such as /use 13, `item_slot` (its label names the item worn there: plan.py passes the worn trinkets);
- `intro`, `source`, `ranking` (how fast each key is while strafing: an assumption the user's reach test overrides), `ahead` (what
  changes as the character levels), `setup`, `macros`, `options`, `no_key` (the active spells with no key, and why) and `needs`
  (clicked spells the keys rely on, for the training list).

For that character it replaces the guide's keys on the checklist (checklist.py) and gets a "Your keys" section in the README (plan.py).
The by-level guides, the class keybinds pages and every other character are untouched.
"""
import re


def block(cfg):
    """The character's own key layout, or None."""
    k = cfg.get("keys")
    return k if isinstance(k, dict) and k.get("bars") else None


def bind_at(slot, lv):
    """The bind a slot holds at level lv, or None (a free key)."""
    now = [b for b in sorted(slot.get("binds") or [], key=lambda b: b["from"]) if b["from"] <= lv]
    return now[-1] if now else None


def label(b):
    return b.get("spell") or re.sub(r"\*\*", "", b.get("text", ""))


def spells(cfg):
    """Spell names the layout uses: each bind's spell, the bold names of its text, and the clicked spells it relies on."""
    k = block(cfg)
    if not k:
        return set()
    out = set(k.get("needs") or [])
    for bar in k["bars"]:
        for s in bar.get("slots") or []:
            for b in s.get("binds") or []:
                if b.get("spell"):
                    out.add(b["spell"])
                out |= set(re.findall(r"\*\*([^*]+)\*\*", b.get("text", "")))
    return out


def resolved(k, worn):
    """The layout with each item-slot key (a slot macro such as /use 13: `item_slot` "trinket1") naming what is worn there now."""
    import copy
    k = copy.deepcopy(k)
    for bar in k["bars"]:
        for s in bar.get("slots") or []:
            if s.get("item_slot"):
                name = (worn or {}).get(s["item_slot"])
                for b in s.get("binds") or []:
                    b["text"] = f"{label(b)}: {name or 'nothing worn'}"
                    b.pop("spell", None)
    return k


def _cell(t):
    return str(t).replace("|", "/").replace("\n", " ")


def readme(cfg, lv, worn=None):
    """The README section: the bars at this level, what changes ahead, the rebind list, the set-up, the macros, the options and the
    spells with no key. `worn`: {item slot: name} for the item-slot keys."""
    k = block(cfg)
    if not k:
        return []
    k = resolved(k, worn)
    o = ["## Your keys: questing and PvP", ""]
    o += [k["intro"], ""] if k.get("intro") else []
    for bar in k["bars"]:
        o += [f"**{bar['title']}**", "", f"| Key | At level {lv} | How you press it | Why here |", "|---|---|---|---|"]
        for s in bar.get("slots") or []:
            b = bind_at(s, lv)
            held = label(b) if b else "free" + (f" ({s['free']})" if s.get("free") else "")
            o.append(f"| {s['key']} | {_cell(held)} | {_cell(s.get('kind', ''))} | {_cell(s.get('why', ''))} |")
        o.append("")
    later = [a for a in k.get("ahead") or [] if a[0] is None or a[0] > lv]
    if later:
        o += ["**As you level** (each key keeps its job):", ""]
        o += [f"- {'Level ' + str(L) if L else 'Any time'}: {t}" for L, t in later] + [""]
    if not k.get("rebound"):
        moved = [s for bar in k["bars"] for s in bar.get("slots") or [] if s.get("was")]
        if moved:
            o += ["**Rebind once** (your old bars to this layout):", ""]
            o += [f"- {s['key']}: {s['was']}" for s in moved]
            o += [f"- {x}" for x in k.get("rebind_extra") or []] + [""]
    if k.get("setup"):
        o += ["**Set up once:**", ""] + [f"{i}. {x}" for i, x in enumerate(k["setup"], 1)] + [""]
    if k.get("macros"):
        o += ["**Macros** (Esc, Macros, New; pick the question-mark icon so the button shows the spell; none is tested in game yet):", ""]
        for m in k["macros"]:
            o += [f"**{m['key']}**: {m['name']}", "", "```"] + m["lines"] + ["```", ""]
            o += [m["note"], ""] if m.get("note") else []
    if k.get("options"):
        o += ["**Options:**", ""] + [f"- {x}" for x in k["options"]] + [""]
    if k.get("no_key"):
        o += ["**No key, and why:**", ""] + [f"- **{n}**: {w}" for n, w in k["no_key"]] + [""]
    if k.get("ranking"):
        o += [k["ranking"], ""]
    if k.get("source"):
        o += [f"*{k['source']}*", ""]
    return o
