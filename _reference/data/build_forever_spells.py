"""Build _reference/data/forever-spells/<class>.json (trainer spellbooks with beta-client numbers) and render
<class>/research/spells/README.md from them.

Source: talentsforever.com's data export (`raw/<pull>/talentsforever-com*/data.json`, CC BY 4.0), whose
`spellbooks` list every trainer spell of every class to level 60 with the level each rank is learned at, and whose
`spell_desc` holds the beta client's level-60 tooltip (no gear) for each rank: cost, range, cast time, cooldown,
effect text, spell-power coefficient and school, plus the Classic Era text where it differs.

Usage (from anywhere):
    python _reference/data/build_forever_spells.py [--raw 2026-10-16-beta-70425] [--captured 2026-10-16] [class ...]
    (default --raw: the newest raw/*-beta-* pull with a talentsforever.com export; --captured: that folder's date)

Writes the JSON, then `<class>/research/spells/README.md` (generated; do not hand-edit). The JSON is what the scorer's spec
models should be checked against (learn levels, cast times, cooldowns, costs, relative base damage).
"""
import argparse
import datetime as dt
import json
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[1]
RAW = HERE / "raw"
OUT = HERE / "forever-spells"
sys.path.insert(0, str(HERE))
CLASSES = ["druid", "hunter", "mage", "paladin", "priest", "rogue", "shaman", "warlock", "warrior"]
STATUS_WORDS = {"new": "new in Forever", "changed": "changed", "same": "as Classic", "removed": "removed"}


def find_raw(raw_dir, sub_prefix, name):
    for d in sorted(raw_dir.iterdir()):
        if d.is_dir() and d.name.startswith(sub_prefix) and (d / name).exists():
            return d / name
    raise SystemExit(f"{name} not found under {raw_dir}/{sub_prefix}*")


def newest_raw():
    """The newest raw/<date>-beta-<build> or <date>-live folder with a talentsforever.com data.json (folder names sort by date; the live
    client's pulls since 2026-10-30 are named <date>-live)."""
    for d in sorted([*RAW.glob("*-beta-*"), *RAW.glob("*-live*")], key=lambda x: x.name, reverse=True):
        if any(x.is_dir() and x.name.startswith("talentsforever-com") and (x / "data.json").exists() for x in d.iterdir()):
            return d.name
    raise SystemExit(f"no *-beta-* folder with a talentsforever.com export under {RAW}")


def lines_to_fields(lines):
    """[['25 Mana','30 yd range'],['1.5 sec cast','8 sec cooldown'],['Requires Daggers','']] -> cost/range/cast/cooldown/requires."""
    f = {"cost": "", "range": "", "cast": "", "cooldown": "", "requires": ""}
    flat = [x for pair in (lines or []) for x in pair if x]
    for x in flat:
        xl = x.lower()
        if "cooldown" in xl:
            f["cooldown"] = x
        elif xl.startswith("requires") or xl.startswith("tools:") or xl.startswith("reagents"):
            f["requires"] = (f["requires"] + "; " + x).strip("; ")
        elif "cast" in xl or xl in ("instant", "channeled", "passive") or "sec" in xl and not f["cast"]:
            f["cast"] = x
        elif "range" in xl or xl == "melee range":
            f["range"] = x
        elif re.search(r"\b(mana|rage|energy|health|% of base mana)\b", xl):
            f["cost"] = x
        elif "scales with" in xl:
            pass
        else:
            f["requires"] = (f["requires"] + "; " + x).strip("; ")
    return f


def build_class(cls, data, captured):
    cname = cls.capitalize()
    book = data["spellbooks"][cname]
    desc = data["spell_desc"]
    levels = book.get("levels", {})
    tabs = []
    counts = {"beta": 0, "demo": 0, "classic": 0}
    status = {}
    for tab in book["tabs"]:
        spells = {}
        for name, rank in tab["spells"]:
            key = f"{cname}|{name}|{rank}"
            d = desc.get(key)
            if d is None:
                continue
            r = {"rank": rank, "id": d.get("id"), "text": d.get("d", ""), "school": d.get("sc"),
                 "coefficient": d.get("co"), "tooltip_source": d.get("s"), "source": d.get("src")}
            r.update(lines_to_fields(d.get("l")))
            m = re.search(r"level (\d+)", d.get("lv") or "")
            if m:
                r["level"] = int(m.group(1))
            elif name in levels and rank.startswith("Rank "):
                i = int(rank.split()[1]) - 1
                if i < len(levels[name]):
                    r["level"] = levels[name][i]
            if d.get("nt"):
                r["not_from_class_trainer"] = {1: "portal trainer", 2: "tome, quest or drop", 3: "talent-taught"}.get(d["nt"], f"not sold by the class trainer ({d['nt']})")
            cs = d.get("cs")
            if cs:
                c = {"status": cs}
                if d.get("cd"):
                    c["text"] = d["cd"]
                if d.get("cl"):
                    c.update({"classic_" + k: v for k, v in lines_to_fields(d["cl"]).items() if v})
                if d.get("cc"):
                    c["coefficient"] = d["cc"]
                if d.get("ck"):
                    c["change_kind"] = {"n": "numbers", "r": "reworded", "b": "both"}.get(d["ck"], d["ck"])
                r["classic"] = c
                status[cs] = status.get(cs, 0) + 1
            counts[d.get("s", "beta")] = counts.get(d.get("s", "beta"), 0) + 1
            spells.setdefault(name, []).append(r)
        tabs.append({"name": tab["name"], "spells": [{"name": n, "ranks": rs} for n, rs in spells.items()]})
    general = []
    for name, rank in book.get("general", []):
        d = desc.get(f"{cname}|{name}|{rank}")
        if d:
            general.append({"name": name, "rank": rank, "text": d.get("d", ""), "tooltip_source": d.get("s")})
    return {"class": cname, "slug": cls, "build": book.get("build"), "captured": captured, "export_generated": data.get("generated"),
            "tooltip_level": book.get("level", 60),
            "source": f"talentsforever.com data export (generated {data.get('generated')}, {data.get('license')}, {data.get('attribution')}): trainer spellbook and level-60 tooltips read from the WoW: Forever beta client build {book.get('build')}; 'classic' blocks quote Classic Era where the tooltip differs.",
            "tooltip_sources": counts, "classic_status_counts": status, "tabs": tabs, "general": general}


def esc(s):
    return (s or "").replace("|", "\\|").replace("\n", " ")


def render_class(cls, obj):
    out = [f"# {obj['class']} spellbook (WoW: Forever beta client {obj['build']})", "",
           f"> Generated by `_reference/data/build_forever_spells.py` from `_reference/data/forever-spells/{cls}.json` "
           f"(captured {obj['captured']}). Do not hand-edit. Tooltips are the beta client's level-{obj['tooltip_level']} values with no gear; "
           f"'vs Classic' quotes Classic Era where the beta text differs. Beta numbers change between builds.", ""]
    sc = obj["classic_status_counts"]
    # 2026-10-15 page audit B16: the tooltip sources were printed as a raw dict ("{'beta': 234, 'demo': 0, 'classic': 0}")
    src_words = {"beta": "the beta client", "demo": "the demo client", "classic": "Classic Era"}
    reads = ", ".join(f"{v} from {src_words.get(k, k)}" for k, v in obj["tooltip_sources"].items() if v)
    out.append("Rank entries: " + ", ".join(f"{v} {STATUS_WORDS.get(k, k)}" for k, v in sorted(sc.items())) +
               (f"; tooltips read: {reads}." if reads else "."))
    out.append("")
    for tab in obj["tabs"]:
        out.append(f"## {tab['name']}")
        out.append("")
        out.append("| Spell | Rank | Level | Cost | Cast / cooldown | Effect (beta) | Coefficient | vs Classic |")
        out.append("|---|---|---|---|---|---|---|---|")
        for sp in tab["spells"]:
            for r in sp["ranks"]:
                cast = " / ".join(x for x in (r.get("cast"), r.get("cooldown")) if x)
                c = r.get("classic") or {}
                vs = STATUS_WORDS.get(c.get("status"), c.get("status", ""))
                if c.get("text") and c.get("status") == "changed":
                    vs += f": {esc(c['text'])}"
                extra = []
                if c.get("classic_cast") and c.get("classic_cast") != r.get("cast"):
                    extra.append(f"cast {c['classic_cast']}")
                if c.get("classic_cooldown") != None and c.get("classic_cooldown") != r.get("cooldown"):
                    extra.append(f"cooldown {c.get('classic_cooldown') or 'none'}")
                if c.get("classic_cost") and c.get("classic_cost") != r.get("cost"):
                    extra.append(f"cost {c['classic_cost']}")
                if c.get("coefficient") and c.get("coefficient") != r.get("coefficient"):
                    extra.append(f"coefficient {c['coefficient']}")
                if extra:
                    vs += " (Classic: " + ", ".join(extra) + ")"
                lvl = r.get("level", "")
                note = f" ({r['not_from_class_trainer']})" if r.get("not_from_class_trainer") else ""
                out.append(f"| {esc(sp['name'])} | {esc(r['rank']) or '-'} | {lvl}{note} | {esc(r.get('cost'))} | {esc(cast)} | {esc(r['text'])} | {esc(r.get('coefficient'))} | {vs} |")
        out.append("")
    if obj["general"]:
        out.append("## General")
        out.append("")
        for g in obj["general"]:
            out.append(f"- **{g['name']}** {g['rank']}: {g['text']}".rstrip(": "))
        out.append("")
    out.append(f"*Generated from `_reference/data/forever-spells/{cls}.json` (beta client {obj['build']}); the source export is CC BY 4.0 talentsforever.com.*")
    return "\n".join(out) + "\n"


def keep_dropped_ranks(cls, obj):
    """Audit 2026-10-18 row 10: the 70425 export lost the mage's Cone of Cold rank 5 (10161, level 58) that every earlier export, wago and
    the raid simulator have. A rank the previous forever-spells/<class>.json had (same spell, rank id) and the new export lacks is kept,
    with its `source` saying where it comes from, and listed in the run's output, so an export error never removes a rank silently. A
    spell missing as a whole is not kept (spells are removed from the game: Tiger's Fury); the output lists it for a check."""
    prev_f = OUT / f"{cls}.json"
    if not prev_f.exists():
        return []
    prev = json.load(open(prev_f, encoding="utf-8"))
    new_spells = {sp["name"]: sp for tab in obj["tabs"] for sp in tab["spells"]}
    kept = []
    for tab in prev.get("tabs", []):
        for sp in tab["spells"]:
            cur = new_spells.get(sp["name"])
            if cur is None:
                print(f"  {cls}: {sp['name']} is in the previous file but not in the export (not kept: check whether it was removed)")
                continue
            have = {r.get("id") for r in cur["ranks"]}
            for r in sp["ranks"]:
                if r.get("id") not in have:
                    r = dict(r)
                    if "missing from" not in (r.get("source") or ""):
                        r["source"] = (f"{r.get('source') or 'previous export'} (missing from the {obj.get('build')} export; kept from the "
                                       f"previous forever-spells file by build_forever_spells.py's guard)")
                    cur["ranks"].append(r)
                    kept.append((sp["name"], r))
                    for key, val in (("tooltip_sources", r.get("tooltip_source")), ("classic_status_counts", (r.get("classic") or {}).get("status"))):
                        if val and isinstance(obj.get(key), dict):
                            obj[key][val] = obj[key].get(val, 0) + 1
            cur["ranks"].sort(key=lambda r: (r.get("level") or 0, str(r.get("rank"))))
    return kept


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("classes", nargs="*")
    # audit 2026-10-18 row 84: the default was a fixed 2026-10-03-beta-70170, so the refresh steps (rebuild.py --refresh, CLAUDE.md,
    # check_beta_build.py's printed command) paired new talents with 70170 spells; now the newest raw/*-beta-* pull that holds a
    # talentsforever.com export, stamped with that folder's date
    ap.add_argument("--raw", default=newest_raw(), help="raw folder (default: the newest *-beta-* with a talentsforever.com export)")
    ap.add_argument("--captured", default=None, help="capture date (default: the raw folder's date)")
    ap.add_argument("--render-only", action="store_true",
                    help="re-render the READMEs from the existing forever-spells/<class>.json (no raw export read; 2026-10-15)")
    a = ap.parse_args()
    if a.render_only:   # 2026-10-15 page audit B16: the default --raw is an older pull, so a plain run would rebuild the JSON from it
        for cls in [c for c in CLASSES if not a.classes or c in a.classes]:
            obj = json.load(open(OUT / f"{cls}.json", encoding="utf-8"))
            (ROOT / cls / "research" / "spells" / "README.md").write_text(render_class(cls, obj), encoding="utf-8")
            print(f"{cls}: research/spells/README.md re-rendered from forever-spells/{cls}.json (build {obj['build']})")
        return
    a.captured = a.captured or a.raw[:10]
    print(f"spellbooks from raw/{a.raw} (captured {a.captured})")
    data = json.load(open(find_raw(RAW / a.raw, "talentsforever-com", "data.json"), encoding="utf-8"))
    OUT.mkdir(exist_ok=True)
    for cls in [c for c in CLASSES if not a.classes or c in a.classes]:
        obj = build_class(cls, data, a.captured)
        for name, r in keep_dropped_ranks(cls, obj):
            print(f"  {cls}: KEPT {name} {r.get('rank')} (id {r.get('id')}, level {r.get('level')}): the export lacks it; "
                  f"the previous file had it ({r.get('source')})")
        import hotfix_text as HT   # live hotfix numbers the export has not read yet (2026-10-30)
        for name in HT.apply_spells(cls, obj):
            print(f"  {cls}: {name}: live hotfix numbers of {HT.DATE} written in (hotfix_text.py)")
        (OUT / f"{cls}.json").write_text(json.dumps(obj, indent=1, ensure_ascii=False), encoding="utf-8")
        d = ROOT / cls / "research" / "spells"
        d.mkdir(exist_ok=True)
        (d / "README.md").write_text(render_class(cls, obj), encoding="utf-8")
        n = sum(len(sp["ranks"]) for tab in obj["tabs"] for sp in tab["spells"])
        print(f"{cls}: {n} rank entries, build {obj['build']}, classic status {obj['classic_status_counts']}, reads {obj['tooltip_sources']} -> {cls}/spells/README.md")


if __name__ == "__main__":
    main()
