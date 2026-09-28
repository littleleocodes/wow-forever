"""Generated sections of a README: each renderer owns one `## ` section and replaces only that one.

    splice(path, "## Fight lab", text, before=["## Optimizer"], title="# Hunter — leveling")

replaces the section that starts with the heading (up to the next `## ` heading), or inserts it before the first of `before`
that exists, or appends it. A missing file is created with `title`. The section order of each scenario README is fixed in
ORDER, so a renderer only has to name its own heading.
"""
import pathlib
import re

ORDER = {
    "leveling": ["## Builds", "## Guide, rotation and respec plan", "## Fight lab", "## Optimizer"],
    "raid": ["## Builds", "## DPS ranking", "## New spells and builds", "## Raid sim", "## Healer lab", "## Rotation, gear and consumables", "## Optimizer"],
    "pvp": ["## Builds", "## PvP check"],
    "class": ["## Where to find things", "## Raid DPS ranking"],
}


def _span(s, heading):
    """(start, end) of the section whose heading line starts with `heading`, else None."""
    m = re.search(r"^" + re.escape(heading) + r".*$", s, re.M)
    if not m:
        return None
    nxt = re.search(r"^## ", s[m.end():], re.M)
    return m.start(), (m.end() + nxt.start()) if nxt else len(s)


def splice(path, heading, text, before=(), title=None):
    path = pathlib.Path(path)
    text = text.rstrip("\n") + "\n\n"
    s = path.read_text(encoding="utf-8") if path.exists() else ((title.rstrip("\n") + "\n\n") if title else "")
    span = _span(s, heading)
    if span:
        s = s[:span[0]] + text + s[span[1]:]
    else:
        at = None
        for h in before:
            sp = _span(s, h)
            if sp:
                at = sp[0]
                break
        s = (s[:at] + text + s[at:]) if at is not None else (s.rstrip("\n") + "\n\n" + text if s.strip() else text)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(s.rstrip("\n") + "\n", encoding="utf-8")


def splice_ordered(path, kind, heading, text, title=None):
    """splice() with the fixed section order of a scenario README (`kind` = leveling | raid | pvp | class)."""
    order = ORDER[kind]
    later = order[order.index(heading) + 1:] if heading in order else []
    splice(path, heading, text, before=later, title=title)


def drop(path, heading):
    """Remove one section (a section that moved elsewhere)."""
    path = pathlib.Path(path)
    if not path.exists():
        return False
    s = path.read_text(encoding="utf-8")
    span = _span(s, heading)
    if not span:
        return False
    path.write_text((s[:span[0]] + s[span[1]:]).rstrip("\n") + "\n", encoding="utf-8")
    return True


def set_head(path, text):
    """Replace the title and intro (everything before the first `## ` heading), creating the file if needed."""
    path = pathlib.Path(path)
    s = path.read_text(encoding="utf-8") if path.exists() else ""
    m = re.search(r"^## ", s, re.M)
    rest = s[m.start():] if m else ""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.rstrip("\n") + "\n\n" + rest.rstrip("\n") + ("\n" if rest else ""), encoding="utf-8")
