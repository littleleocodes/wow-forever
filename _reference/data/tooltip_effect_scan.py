"""A first scan for the Ice Barrier failure pattern, every class (2026-11-19): a talent, or a spell a talent teaches, whose Forever tooltip raises damage,
healing, crit, haste or power, where (a) the fight lab's module never reads it or marks it not used, or (b) no raid rotation of ours
casts the spell it teaches. Read-only: tooltips, module sources, rotation files.

    python _reference/data/tooltip_effect_scan.py

Its limit, shown by the case it was written for: it would not have flagged Ice Barrier before 2026-11-19, because the mage module
named the talent (as a shield) and a name match cannot tell a fully modelled effect from a partly modelled one. A flag here is a
lead for a hand review; no flag proves nothing. The audit brief (_reference/audit-brief-1119.md) asks for the measured checks."""
import glob
import importlib.util
import json
import pathlib
import re
import sys

ROOT = pathlib.Path("F:/wow-forever")
DATA = ROOT / "_reference" / "data"
FL = DATA / "fightlab"
sys.path[:0] = [str(FL), str(DATA)]
CLASSES = ["druid", "hunter", "mage", "paladin", "priest", "rogue", "shaman", "warlock", "warrior"]
BOOST = re.compile(r"(increas\w*|raises?|improv\w*|bonus|additional|empower\w*|amplif\w*)[^.;]{0,60}?"
                   r"(damage|healing|critical|haste|spell power|attack power|attack speed|casting speed|crit)", re.I)
OFF = re.compile(r"not used|not modell?ed|not simulated|unused|no effect in|travel|outside combat", re.I)


def module_info(cls):
    src = (FL / f"{cls}.py").read_text(encoding="utf-8")
    spec = importlib.util.spec_from_file_location(f"scan_{cls}", FL / f"{cls}.py")
    m = importlib.util.module_from_spec(spec)
    try:
        spec.loader.exec_module(m)
    except Exception as e:  # noqa: BLE001
        return src, {}, {}, str(e)
    return src, getattr(m, "MECHANICS", {}) or {}, getattr(m, "TALENT_SPELLS", {}) or {}, None


def apl_text(cls):
    return "\n".join(pathlib.Path(f).read_text(encoding="utf-8") for f in glob.glob(str(DATA / "raidsim" / "apls" / cls / "*.json")))


out = {}
for cls in CLASSES:
    trees = json.load(open(DATA / "forever-talents" / f"{cls}.json", encoding="utf-8"))["trees"]
    book = json.load(open(DATA / "forever-spells" / f"{cls}.json", encoding="utf-8"))
    spells = {}
    for tab in book.get("tabs", []):
        for sp in tab.get("spells", []):
            spells[sp["name"]] = sp
    src, mech, tspells, err = module_info(cls)
    apls = apl_text(cls)
    rows = []
    for tr in trees:
        for t in tr["talents"]:
            name = t["name"]
            texts = [r if isinstance(r, str) else json.dumps(r) for r in t.get("ranks", [])]
            top = texts[-1] if texts else ""
            sp = spells.get(name) or spells.get(tspells.get(name, "")) if isinstance(tspells, dict) else spells.get(name)
            sp_text = ""
            ids = []
            if sp:
                rk = sp.get("ranks") or []
                sp_text = (rk[-1].get("text") if rk else "") or ""
                ids = [str(x.get("id")) for x in rk if x.get("id")]
            boost_t = BOOST.search(top)
            boost_s = BOOST.search(sp_text) if sp else None
            if not (boost_t or boost_s):
                continue
            mtext = str(mech.get(name, ""))
            in_src = (f'"{name}"' in src) or (f"'{name}'" in src)
            lab = "absent" if not in_src else ("marked off: " + mtext[:70] if OFF.search(mtext) else "read")
            raid = None
            if sp and ids:   # an ability the talent teaches: does any raid rotation of ours cast it?
                raid = "cast" if any(re.search(rf"\b{i}\b", apls) for i in ids) else "never cast"
            if lab != "read" or raid == "never cast":
                rows.append({"tree": tr["name"], "talent": name, "row": t.get("row"), "lab": lab, "raid": raid,
                             "clause": (boost_s.group(0) if boost_s else boost_t.group(0))[:90]})
    out[cls] = {"rows": rows, "module_error": err}
for cls, v in out.items():
    print(f"== {cls}: {len(v['rows'])} flagged" + (f" (module did not load: {v['module_error']})" if v["module_error"] else ""))
    for r in v["rows"]:
        print(f"   {r['tree'][:12]:12s} r{r['row']} {r['talent'][:28]:28s} lab: {r['lab'][:46]:46s} raid: {str(r['raid']):10s} | {r['clause']}")

