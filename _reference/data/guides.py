"""Rotation guides on the player pages (2026-10-09, user request: "I want each of the classes spec sections to have sort of a mini guide on
why the rotation is how it is. And the caveats and when you should use certain spells over another or when you should diverge from the
rotation itself").

    python _reference/data/guides.py --check [--write]     # validate every guide, list missing and outdated ones (_reference/guide-check.md)
    python _reference/data/guides.py --stamp <class> [--spec "<spec>"] [--mode raid|leveling]   # record the rotations a guide was written for

Hand-kept source, one file per class: `_reference/data/guides/<class>.json`
    {"class": "rogue", "guides": {"<spec name as the pages use it>": {"raid": GUIDE, "leveling": GUIDE}}}
    GUIDE = {"written": "YYYY-MM-DD", "rotations": {label: fingerprint, ...},   # filled by --stamp
             "plan": "one or two sentences: the idea of the rotation",
             "why": ["why each part of the list sits where it does", ...],
             "caveats": ["situations that change the picture: several targets, moving, mana, the execute phase", ...],
             "diverge": ["when to leave the list and what to press instead", ...]}
Every **bold** name must be a spell or talent of the class (the beta spellbook and the talent trees), as in leveling-steps.json.
`render_modes.py` prints the guide under "How to play" as "## Why this rotation". The rotation a page shows can change (the searches
re-tune rotations): the page compares the rotation's fingerprint with the one the guide was stamped for and, when they differ, says the
list was re-tuned after the guide was written, so the reasons may lag. --check lists those guides for review (since 2026-10-18 it
compares every stamp with the current fingerprint) and the leveling steps that name a spell the tuned rules switch off.
"""
import argparse
import datetime
import hashlib
import json
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[1]
DIR = HERE / "guides"
PAGE = ROOT / "_reference" / "guide-check.md"
TODAY = datetime.date.today().isoformat()
_CACHE = {}


def load(cls):
    if cls not in _CACHE:
        f = DIR / f"{cls}.json"
        _CACHE[cls] = json.load(open(f, encoding="utf-8")) if f.exists() else {"class": cls, "guides": {}}
    return _CACHE[cls]


def guide(cls, spec, mode):
    return ((load(cls).get("guides") or {}).get(spec) or {}).get(mode)


def _digest(chunks):
    h = hashlib.sha256()
    for c in chunks:
        h.update(c.replace("\r\n", "\n").encode("utf-8") if isinstance(c, str) else c)
    return h.hexdigest()[:12]


def raid_fingerprint(cls, entry):
    """The full-raid rotation of a raid simulator entry (the file the pages' How to play comes from)."""
    specs = json.load(open(HERE / "raidsim" / "specs.json", encoding="utf-8"))
    e = (specs.get(cls) or {}).get(entry) or {}
    rel = e.get("apl_opt_raid") or e.get("apl")
    if not rel:
        return None
    p = ROOT / rel
    if not p.exists():
        return None
    return _digest([p.read_text(encoding="utf-8")])


def leveling_fingerprint(cls, model):
    """The fight lab's leveling rotation of a spec model: the page's hand-kept steps and the tuned rotation rules."""
    steps = json.load(open(HERE / "leveling-steps.json", encoding="utf-8"))
    chunks = [json.dumps(((steps.get(cls) or {}).get(model)), sort_keys=True)]
    rules = HERE / "fightlab" / "rotations" / f"{cls}-{model}.json"
    if rules.exists():
        chunks.append(rules.read_text(encoding="utf-8"))
    return _digest(chunks)


def healer_fingerprint(cls):
    """The healer lab's heal-choice policies of the class (shared by its healing specs)."""
    files = sorted((HERE / "heallab" / "rotations").glob(f"{cls}-*.json"))
    return _digest([f.read_text(encoding="utf-8") for f in files]) if files else None


def bold_names(text):
    return re.findall(r"\*\*(.+?)\*\*", text)


def class_names(cls):
    """Every spell of the class's beta spellbook and every talent name (the names a guide may set in bold)."""
    names = set()
    for tab in json.load(open(HERE / "forever-spells" / f"{cls}.json", encoding="utf-8"))["tabs"]:
        names.update(sp["name"] for sp in tab["spells"])
    for tr in json.load(open(HERE / "forever-talents" / f"{cls}.json", encoding="utf-8")).get("trees", []):
        names.update(t["name"] for t in tr.get("talents", []))
    return names


def render(cls, spec, mode, label, fingerprint, title="Why this rotation"):
    """Markdown lines for a spec page (empty when the spec has no guide for the mode). Healer pages have no rotation list, so their
    guide is the page's "How to heal"."""
    g = guide(cls, spec, mode)
    if not g:
        return []
    o = [f"## {title}", ""]
    if g.get("plan"):
        o += [g["plan"], ""]
    for key, head in (("why", "Why it works"), ("caveats", "Caveats"), ("diverge", "When to change it")):
        if g.get(key):
            o += [f"**{head}**", ""] + [f"- {x}" for x in g[key]] + [""]
    stamped = (g.get("rotations") or {}).get(label)
    if fingerprint and stamped and stamped != fingerprint:
        o += [f"*This guide was written for the rotation of {g.get('written', 'an earlier date')}; the list above was re-tuned since, so "
              "follow the list where the two differ.*", ""]
    return o


def check(write=False):
    """Validate the guides; list the page specs without one and the guides whose rotation changed (needs the pages' own view)."""
    sys.path[:0] = [str(HERE), str(HERE / "scorer")]
    import spec_modes as SM
    rows, problems = [], []
    for cls in SM.CLASSES:
        data = load(cls)
        names = class_names(cls)
        for spec, modes in (data.get("guides") or {}).items():
            for mode, g in modes.items():
                for key in ("plan", "why", "caveats", "diverge"):
                    vals = [g.get(key)] if key == "plan" else (g.get(key) or [])
                    for v in vals:
                        for n in bold_names(v or ""):
                            if n not in names:
                                problems.append(f"{cls} {spec} {mode}: **{n}** is not a spell or talent of the class")
                if not g.get("why"):
                    problems.append(f"{cls} {spec} {mode}: no 'why' bullets")
                rows.append((cls, spec, mode, g.get("written"), sorted((g.get("rotations") or {}).items())))
    stale = stale_guides(rows)
    vetoed = vetoed_steps()
    out = ["# Rotation guide check (generated)", "", f"> Generated by `_reference/data/guides.py --check` on {TODAY}. Do not hand-edit.", ""]
    out += [f"{len(rows)} guides. Problems:", ""] + ([f"- {p}" for p in problems] or ["- none"]) + [""]
    out += [f"Guides whose rotation changed since they were stamped ({len(stale)}; rewrite or confirm, then `--stamp`):", ""]
    out += [f"- {c} {s} {m}: {', '.join(labels)}" for c, s, m, labels in stale] or ["- none"]
    out += ["", f"Leveling steps that name a spell the tuned rules never cast ({len(vetoed)}; `fightlab/rotations/<class>-<model>.json` "
            "veto `off`; rewrite the steps in leveling-steps.json when the rules settle):", ""]
    out += [f"- {c} {m}: **{n}** ({where})" for c, m, n, where in vetoed] or ["- none"]
    out += [""]
    out += ["| Class | Spec | Mode | Written | Rotations stamped |", "|---|---|---|---|---|"]
    out += [f"| {c} | {s} | {m} | {w or '-'} | {', '.join(f'{k} {v}' for k, v in r) or '-'} |" for c, s, m, w, r in rows]
    if write:
        PAGE.write_text("\n".join(out) + "\n", encoding="utf-8")
    print("\n".join(out[:out.index("| Class | Spec | Mode | Written | Rotations stamped |")]))
    return problems


def current_fingerprint(cls, label):
    """The fingerprint a stamp label refers to now: leveling:<model>, healer-policy or a raid simulator entry."""
    if label.startswith("leveling:"):
        return leveling_fingerprint(cls, label.split(":", 1)[1])
    if label == "healer-policy":
        return healer_fingerprint(cls)
    return raid_fingerprint(cls, label)


def stale_guides(rows):
    """Audit 2026-10-18 row 95: --check printed "Problems: none" while 107 of 186 stamps differed from the rotations the pages show.
    [(class, spec, mode, [labels whose fingerprint moved])]; a guide never stamped is listed as "not stamped"."""
    out = []
    for cls, spec, mode, written, stamps in rows:
        moved = [k for k, v in stamps if current_fingerprint(cls, k) != v] if stamps else ["not stamped"]
        if moved:
            out.append((cls, spec, mode, moved))
    return out


def vetoed_steps():
    """Audit 2026-10-18 row 90: the hand-kept leveling steps the pages print verbatim against the tuned rules (rotation_opt.py): every
    bold name in a model's steps that its rules file switches off (veto `off`). [(class, model, name, where)]."""
    steps = json.load(open(HERE / "leveling-steps.json", encoding="utf-8"))
    out = []
    for cls, models in steps.items():
        if not isinstance(models, dict):   # the file's own notes ("_note")
            continue
        for model, st in models.items():
            f = HERE / "fightlab" / "rotations" / f"{cls}-{model}.json"
            if not f.exists() or not isinstance(st, dict):
                continue
            off = {n for n, v in (json.load(open(f, encoding="utf-8")).get("veto") or {}).items() if isinstance(v, dict) and v.get("off")}
            seen = set()
            for key, vals in st.items():
                for v in (vals if isinstance(vals, list) else [vals]):
                    for n in bold_names(v if isinstance(v, str) else ""):
                        # a step that tells the player not to cast it agrees with the veto (2026-11-09: the BM steps' "No other shots
                        # on a single mob: the fight lab levels faster skipping **Arcane Shot** and **Multi-Shot**")
                        lead = v[:v.find(f"**{n}**")].lower()
                        if any(k in lead for k in ("skipping", "skip ", "no other", "without", "never", "not ", "instead of")):
                            continue
                        if n in off and n not in seen:
                            seen.add(n)
                            out.append((cls, model, n, key))
    return out


def stamp(cls, spec=None, mode=None):
    """Record, for each guide of the class, the fingerprints of the rotations it was written for: every raid entry built for the spec
    (spec_modes.RAID_ENTRY_TREES), the leveling models of the spec's leveling pages, the class's healer policies."""
    sys.path[:0] = [str(HERE), str(HERE / "scorer")]
    import spec_modes as SM
    data = load(cls)
    steps = json.load(open(HERE / "leveling-steps.json", encoding="utf-8")).get(cls) or {}
    for sp, modes in (data.get("guides") or {}).items():
        if spec and sp != spec:
            continue
        for md, g in modes.items():
            if mode and md != mode:
                continue
            fp = {}
            if md == "raid":
                for (c, entry), trees in SM.RAID_ENTRY_TREES.items():
                    if c == cls and SM.rotation_allows(sp, trees):
                        x = raid_fingerprint(cls, entry)
                        if x:
                            fp[entry] = x
                h = healer_fingerprint(cls)
                if h and sp in (SM.HEAL_TREES.get(cls) or ()):
                    fp["healer-policy"] = h
            else:
                for model in steps:
                    fp[f"leveling:{model}"] = leveling_fingerprint(cls, model)
            g["rotations"] = fp
            g["written"] = g.get("written") or TODAY
    (DIR / f"{cls}.json").write_text(json.dumps(data, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"stamped {cls}")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--write", action="store_true")
    ap.add_argument("--stamp")
    ap.add_argument("--spec")
    ap.add_argument("--mode")
    a = ap.parse_args()
    if a.stamp:
        stamp(a.stamp, a.spec, a.mode)
    if a.check:
        sys.exit(1 if check(a.write) else 0)


if __name__ == "__main__":
    main()
