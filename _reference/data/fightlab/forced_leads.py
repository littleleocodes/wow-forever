"""The forced-run leads beside the tuned rules (2026-11-22, the audit session's ruling on the held leveling picks: "keep the forced run's
number beside the tuned result in the record").

For every rotation whose class module names forced lines (engine.BaseModule.FORCE_SPELLS) and every such spell:
- the forced run's verdict (never-tried.json, fightlab/force_run.py);
- the window the installed rules force it at (the rules knob FORCE_<SLUG>_LEVELS), or none;
- an A/B on the rules' own build at the rules' levels, seeds 1 and 2: the installed rules against the same rules with the spell's
  window changed (on from the forced run's first lead level when the rules leave it off; off when they keep it).
Verdicts:
- kept: the tune installed a window.
- agrees: the tune left it off and the A/B agrees (the window is not BAR faster on both seeds).
- missed: the tune left it off but the window is BAR or more faster on both seeds: the tune's screening missed it (the Rockbiter case,
  search-improvements 0j). With --install the window goes into the rules by hand and the record says so; the signature check runs on
  the new rules (fl_signature.check_levels at the rules' levels).
Record fightlab/forced-leads.json; fightlab/play_check.py's Lg rule reads it (a lead whose verdict is "agrees" is a note with both
numbers; "missed" stays a fail). Usage: forced_leads.py [classes] [--fights N] [--jobs N] [--install] [--write].
"""
import argparse
import copy
import datetime
import json
import multiprocessing
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path[:0] = [str(HERE), str(HERE.parent)]
import engine as E  # noqa: E402
import rotation_opt as RO  # noqa: E402
import run as FR  # noqa: E402

RECORD = HERE / "forced-leads.json"
VERDICTS = HERE / "never-tried.json"
BAR = 0.005   # the audit session's bar (2026-11-22): 0.5% faster on both seeds
LEAD = re.compile(r"(top|filler) at (\d+): ([+-]?\d+(?:\.\d+)?)%")
STARTS = sorted({w[0] for w in E.FORCE_WINDOWS if w})


def window_for(verdict):
    """The window the forced run led at: from the first level it was faster (rounded down to a window start) to 60."""
    levels = [int(L) for _, L, g in LEAD.findall(verdict or "") if float(g) < 0]
    if not levels:
        return None
    first = min(levels)
    start = max([s for s in STARTS if s <= first] or [STARTS[0]])
    return [start, 61]


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("classes", nargs="*")
    ap.add_argument("--fights", type=int, default=3000)
    ap.add_argument("--jobs", type=int, default=8)
    ap.add_argument("--install", action="store_true", help="install a missed window into the rules by hand")
    ap.add_argument("--write", action="store_true")
    a = ap.parse_args()
    verdicts = json.load(open(VERDICTS, encoding="utf-8")) if VERDICTS.exists() else {}
    rec = json.load(open(RECORD, encoding="utf-8")) if RECORD.exists() else {}
    rec["_note"] = __doc__.split("\n\n")[0].replace("\n", " ")
    today = datetime.date.today().isoformat()
    classes = a.classes or [c for c in FR.MODULES]
    with multiprocessing.Pool(a.jobs, initializer=RO._init) as pool:
        for cls in classes:
            mod_cls = getattr(__import__(FR.MODULES[cls][0]), FR.MODULES[cls][1])
            for rot, names in (getattr(mod_cls, "FORCE_SPELLS", {}) or {}).items():
                p = FR.rotation_file(cls, rot)
                if not p.exists():
                    print(f"{cls} {rot}: no rules file, skipped", flush=True)
                    continue
                rules = json.load(open(p, encoding="utf-8"))
                bid, levels = rules.get("build"), rules.get("levels") or [20, 30, 40, 50, 60]
                base = {k: copy.deepcopy(rules[k]) for k in ("veto", "drink_below", "eat_below", "knobs") if k in rules}
                for n in names:
                    knob = f"FORCE_{E.force_slug(n)}_LEVELS"
                    verdict = ((verdicts.get(cls) or {}).get(rot) or {}).get(n)
                    installed = (base.get("knobs") or {}).get(knob)
                    alt = copy.deepcopy(base)
                    if installed:
                        alt.setdefault("knobs", {})[knob] = None
                        window = installed
                    else:
                        window = window_for(verdict) or [STARTS[0], 61]
                        alt.setdefault("knobs", {})[knob] = window
                    gains, weighted = [], {}
                    for seed in (1, 2):
                        r0, r1 = RO.evaluate(pool, cls, rot, bid, levels, [base, alt], a.fights, seed)
                        w0 = RO.weighted({L: r0[L]["time_per_kill"] for L in levels})
                        w1 = RO.weighted({L: r1[L]["time_per_kill"] for L in levels})
                        # the gain of the window: off -> on
                        g = (1 - w0 / w1) if installed else (1 - w1 / w0)
                        gains.append(round(g, 5))
                        weighted[f"seed {seed}"] = {"rules": round(w0, 3), "changed": round(w1, 3)}
                    if installed:
                        v = "kept"
                        text = (f"the rules force it at levels {installed[0]}-{installed[1] - 1}; without that window "
                                f"{-gains[0]:+.2%} seed 1, {-gains[1]:+.2%} seed 2 per kill")
                    elif min(gains) >= BAR:
                        v = "missed"
                        text = (f"the tune left it off, but forced at levels {window[0]}-{window[1] - 1} on the installed rules it is "
                                f"{gains[0]:.2%} (seed 1) and {gains[1]:.2%} (seed 2) faster per kill: the screening missed it")
                    else:
                        v = "agrees"
                        text = (f"the tune compared it as a rules knob ({knob}) and left it off; forced at levels {window[0]}-{window[1] - 1} "
                                f"on the installed rules: {gains[0]:+.2%} seed 1, {gains[1]:+.2%} seed 2 per kill (faster is +)")
                    entry = {"forced": verdict, "knob": knob, "window": window, "installed": installed, "verdict": v, "text": text,
                             "ab": {"gains": gains, "weighted": weighted, "levels": levels, "fights": a.fights, "build": bid},
                             "rules_date": rules.get("date"), "date": today}
                    if v == "missed" and a.install and a.write:
                        rules.setdefault("knobs", {})[knob] = window
                        rules.setdefault("changes", []).append({"round": "by hand", "change": f"{knob} = {window}", "rule": ["knob", knob, window],
                                                                "gain_seed1": gains[0], "gain_seed2": gains[1],
                                                                "why": "forced_leads.py: the tune's screening missed it (A/B on seeds 1 and 2)"})
                        p.write_text(json.dumps(rules, indent=1), encoding="utf-8")
                        base.setdefault("knobs", {})[knob] = window
                        entry["by_hand"] = today
                        entry["text"] += "; installed by hand"
                        # the signature check on the new rules, as rotation_opt's search runs it (seed 3)
                        res = RO.evaluate(pool, cls, rot, bid, levels, [base], a.fights, 3)[0]
                        b_ = FR.load_build(cls, bid)
                        spec_b = b_.get("spec") or RO.FS.spec_for(cls, rot, RO.FS.flat_of(b_))
                        rl = RO.SG.rule(cls, spec_b, "leveling")
                        sig = RO.SG.check_levels(cls, spec_b, b_, res, "leveling", rl) if rl else {"ok": True}
                        entry["signature"] = {"ok": bool(sig.get("ok")), "uncast": sig.get("uncast"), "core_share": sig.get("core_share")}
                        entry["text"] += "; signature check " + ("passes" if sig.get("ok") else f"FAILS ({sig.get('uncast')})")
                    print(f"{cls} {rot} {n}: {v}: {entry['text']}", flush=True)
                    rec.setdefault(cls, {}).setdefault(rot, {})[n] = entry
    if a.write:   # merged under a lock: the lanes run one class each in parallel
        import filelock
        with filelock.locked(str(RECORD) + ".lock"):
            cur = json.load(open(RECORD, encoding="utf-8")) if RECORD.exists() else {}
            cur["_note"] = rec["_note"]
            for cls in classes:
                for rot, v in (rec.get(cls) or {}).items():
                    cur.setdefault(cls, {}).setdefault(rot, {}).update(v)
            RECORD.write_text(json.dumps(cur, indent=1), encoding="utf-8")
        print(f"wrote {RECORD}", flush=True)


if __name__ == "__main__":
    main()
