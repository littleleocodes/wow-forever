"""The filler pass for the credited simulator builds and six of ours (2026-11-20, the audit session's request after the user's question on Deflection in
the Survival Raptor build; the user's rule of 2026-11-08: a page pick holds no talent that does nothing).

raidsim/filler_audit.py's search, made exact:
- a point is free only when removing its talent leaves the full-raid DPS bit for bit the same (common random numbers);
- a move is taken only when the new build's DPS is bit for bit the same on seeds 1 and 2 (no gain moves: the build stays the
  simulator's) and the new talent ranks higher in the utility order (raidsim/utility_tags.py);
- never into a talent ability the build would not cast (unless defensive: an absorb, a dodge, a heal), nor into a talent that improves
  only spells the build never casts (page_lint's dead rule: 2026-11-20, the first try moved a Frost Med point into Arcane Blast);
- the final build is checked on the training dummy too: a move whose prefix changes the dummy's DPS is banned and the pass runs again.
Applied builds keep their preset credit and name and get one note.

    python _reference/data/deep-runs/credited_fillers_1120.py [--apply]
"""
import argparse
import datetime
import json
import pathlib
import re
import sys

DATA = pathlib.Path(__file__).resolve().parents[1]
ROOT = DATA.parents[1]
sys.path[:0] = [str(DATA / "raidsim"), str(DATA)]
import filler_audit as FA  # noqa: E402
import page_lint as PL  # noqa: E402
import paths  # noqa: E402
from fmt_json import dumps  # noqa: E402
from filelock import locked  # noqa: E402

BUILDS = [("mage", "frost-raid", "frost-med-raid"), ("mage", "arcane-dps", "arcane-fire-raid"), ("mage", "frostfire-raid", "frostfire-ffb-raid"),
          ("warlock", "destro-raid", "destruction-succubus-raid"), ("warlock", "affliction-wrack-raid", "affliction-wrack-raid"),
          ("hunter", "survival-pet-raid", "survival-raptor-raid"), ("paladin", "ret-dps", "retribution-unsealed-wrath-raid"),
          ("paladin", "shockadin-raid", "shockadin-holy-shock-raid"), ("hunter", "mm-lonewolf-raid", "marksmanship-lone-wolf-sim-raid"),
          # ours: builds whose filler audit had moved points into avoidance talents (Deflection, Lightning Reflexes), which give a damage
          # dealer the boss never attacks nothing (utility_tags.SURVIVAL_DPS, the same day)
          ("hunter", "melee-dps", "beast-survival-open-raid"), ("paladin", "ret-dps", "prot-ret-ml-raid"), ("paladin", "ret-dps", "retribution-open-raid"),
          ("paladin", "shockadin-raid", "shockadin-open-raid"), ("rogue", "assassination-raid", "assassination-open-raid"),
          ("rogue", "combat-daggers-raid", "daggers-split-open-raid")]
OUT = DATA / "raidsim" / "credited-fillers.json"
R, A = FA.R, FA.A
CTX = {"used": set(), "banned": set(), "tal": {}, "names": set()}


# --- exactness: a run's value is 1 when its DPS is bit for bit the reference's, else 0 (removal effect 0 or 1; a move 0 or -1)
_orig_value = A.value


def exact_value(row, ref, tank=False):
    if not row or not ref or row.get("error") or ref.get("error"):
        return _orig_value(row, ref, tank)
    return 1.0 if row.get("dps") == ref.get("dps") else 0.0


# --- the utility order without dead destinations
_orig_utility = FA.utility


def improves_only_unused(t, used):
    tip = PL.rank_text(t)
    names = {n for n in CTX["names"] if re.search(rf"\b{re.escape(n)}\b", tip)}
    names -= {n for n in names if any(n != o and n in o for o in names)}
    rest = tip
    for n in names:
        rest = rest.replace(n, " ")
    if PL.FAMILY.search(rest):
        return False
    return bool(names) and not PL.GENERIC.search(rest) and not (names & used)


def utility(cls, tank=False):
    use = dict(_orig_utility(cls, tank))
    book = FA.spell_ids(cls)
    for n in list(use):
        if n in CTX["banned"]:
            use[n] = FA.NONE
        elif n in book:   # a talent that grants an ability: a destination only when the build casts it or it is defensive
            txt = book[n][1]
            if n not in CTX["used"] and (FA.TRIGGERED.search(txt) or not FA.DEFENSIVE.search(txt)):
                use[n] = FA.NONE
        elif n in CTX["tal"] and improves_only_unused(CTX["tal"][n], CTX["used"]):
            use[n] = FA.NONE
    return use


def flat(alloc_by_tree):
    return {n: r for items in alloc_by_tree.values() for n, r in items if r}


def setup(cls, spec, bid):
    """The spells the build uses (cast in a full raid or on the dummy, or in the rotations' pre-pull lists) and the class's talents."""
    repo = R.repo_path(argparse.Namespace(repo=None))
    entry = R.SPECS[cls][spec]
    sim_trees = R.load_trees(repo, cls)
    data = {b["id"]: b for b in json.load(open(paths.builds_json("forever", cls), encoding="utf-8"))["builds"]}
    cur = R.alloc_of(data[bid])
    book = FA.spell_ids(cls)
    ids = set()
    for where in ("raid", "dummy"):
        row = A.bench(entry, repo, [{"label": "b", "talents": R.talents_string(sim_trees, cur)}], 3000, 1, where, f"credfill-{spec}").get("b") or {}
        ids |= {a.get("spellId") for a in row.get("actions") or [] if (a.get("casts") or 0) > 0}
        ids |= FA.apl_spell_ids(R.apl_path(entry, repo, where), "prepullActions")
    CTX["used"] = {n for n, (s, _) in book.items() if s & ids}
    CTX["names"] = {n for n in book if n} | PL.FORMS
    CTX["tal"] = {t["name"]: t for tr in json.load(open(DATA / "forever-talents" / f"{cls}.json", encoding="utf-8"))["trees"] for t in tr["talents"]}
    CTX["banned"] = set()


def dummy_prefixes(cls, spec, start, moves):
    """The dummy's DPS for the start and after each move (the moves' own order: every prefix is legal)."""
    repo = R.repo_path(argparse.Namespace(repo=None))
    entry = R.SPECS[cls][spec]
    sim_trees = R.load_trees(repo, cls)
    allocs, cur = [dict(start)], dict(start)
    for m in moves:
        cur[m["from"]] -= 1
        if not cur[m["from"]]:
            del cur[m["from"]]
        cur[m["to"]] = cur.get(m["to"], 0) + 1
        allocs.append(dict(cur))
    rows = A.bench(entry, repo, [{"label": str(i), "talents": R.talents_string(sim_trees, al)} for i, al in enumerate(allocs)],
                   6000, 1, "dummy", f"credfill-{spec}")
    return [rows[str(i)]["dps"] for i in range(len(allocs))]


def verify(rec):
    """Each record with moves: the start and the final build raced in a full raid, 10,000 fights, seeds 1 and 2 (the numbers the list
    gives); `ok` stays only when both seeds are bit for bit the same."""
    R.set_game("forever")
    repo = R.repo_path(argparse.Namespace(repo=None))
    for key, x in rec.items():
        if not x.get("moves") or x.get("check"):
            continue
        cls = key.split("/")[0]
        entry = R.SPECS[cls][x["entry"]]
        sim_trees = R.load_trees(repo, cls)
        chk = {}
        for seed in (1, 2):
            rows = A.bench(entry, repo, [{"label": "start", "talents": R.talents_string(sim_trees, flat(x["start"]))},
                                         {"label": "final", "talents": R.talents_string(sim_trees, flat(x["allocation"]))}],
                           10000, seed, "raid", f"credfill-{x['entry']}")
            chk[f"raid seed {seed}"] = [rows["start"]["dps"], rows["final"]["dps"]]
        x["check"] = chk
        x["ok"] = bool(x.get("ok")) and all(a == b for a, b in chk.values())
        print(f"  {key}: " + ", ".join(f"{k} {v[0]:.2f} -> {v[1]:.2f}" for k, v in chk.items()) + ("" if x["ok"] else "  NOT the same"), flush=True)
        OUT.write_text(json.dumps(rec, indent=1) + "\n", encoding="utf-8")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--verify", action="store_true", help="race each record's moves at 10,000 fights, seeds 1 and 2, before --apply")
    a = ap.parse_args()
    if a.verify:
        verify(json.loads(OUT.read_text(encoding="utf-8")))
        return
    FA.ZERO, FA.GAIN, FA.LOSS = 0.5, 1e9, 0.0   # with exact_value: free = bit for bit; no gain moves; a move must be bit for bit
    A.value = exact_value
    FA.utility = utility
    rec = json.loads(OUT.read_text(encoding="utf-8")) if OUT.exists() else {}
    for cls, spec, bid in BUILDS:
        key = f"{cls}/{bid}"
        if key in rec:
            print(f"== {key}: done before", flush=True)
            continue
        print(f"== {cls} {bid} in {spec} (full raid, exact)", flush=True)
        R.set_game("forever")
        setup(cls, spec, bid)
        print(f"   spells used: {', '.join(sorted(CTX['used']))}", flush=True)
        for attempt in range(4):
            r = FA.audit(cls, spec, bid, 3000, 12000, setting="raid")
            out = {"entry": spec, "date": datetime.date.today().isoformat(), "free": r["free"], "moves": r["moves"],
                   "final_seed3_same": r["final_seed3"] == 0.0, "start": r["start"], "allocation": r["allocation"],
                   "kept_for_rotation": r["kept_for_rotation"], "banned": sorted(CTX["banned"])}
            if not r["moves"]:
                break
            dps = dummy_prefixes(cls, spec, flat(r["start"]), r["moves"])
            out["dummy"] = dps
            bad = next((i for i in range(1, len(dps)) if dps[i] != dps[0]), None)
            if bad is None:
                print(f"   dummy: {dps[0]:.2f}, the same after every move", flush=True)
                break
            m = r["moves"][bad - 1]
            print(f"   dummy: move {bad} ({m['from']} -> {m['to']}) changes it ({dps[0]:.2f} -> {dps[bad]:.2f}): {m['to']} banned, again", flush=True)
            CTX["banned"].add(m["to"])
        out["ok"] = bool(out["moves"]) and out["final_seed3_same"] and all(d == out["dummy"][0] for d in out.get("dummy", [0]))
        rec[key] = out
        OUT.write_text(json.dumps(rec, indent=1) + "\n", encoding="utf-8")
    print("\nsummary:")
    for key, x in rec.items():
        mv = x["moves"]
        txt = "; ".join(f"{m['from']} -> {m['to']}" for m in mv) or "nothing moved"
        print(f"  {key}: free {', '.join(x['free']) or '-'}; {txt}" + ("" if not mv else (" (ok)" if x.get("ok") else " (NOT ok: left as shipped)")))
    if not a.apply:
        return
    for key, x in rec.items():
        if not x.get("ok") or not x.get("check"):   # measured and verified (--verify) first
            continue
        cls, bid = key.split("/")
        bp = paths.builds_json("forever", cls)
        with locked(bp.with_suffix(".lock")):   # the lanes write this file too (builds_io's lock); edited in place, order kept
            data = json.load(open(bp, encoding="utf-8"))
            b = next(y for y in data["builds"] if y["id"] == bid)
            if flat(b["allocation"]) != flat(x["start"]):
                print(f"skipped {key}: the build changed since the pass")
                continue
            b["allocation"] = x["allocation"]
            moved = {}
            for m in x["moves"]:
                moved[(m["from"], m["to"])] = moved.get((m["from"], m["to"]), 0) + 1
            txt = "; ".join(f"{n} point{'s' if n != 1 else ''} from {f} to {t}" for (f, t), n in moved.items())
            whose = "the simulator's build with its filler points moved" if b.get("preset") else "filler points moved"
            b.setdefault("notes", []).append(
                f"{x['date']}: {whose} ({txt}): the same DPS bit for bit in a full raid and on the training dummy. The new talents follow "
                "the utility order (interrupt protection, threat, mana, range, survival; dodge, parry and block count for nothing in a damage "
                "dealer's raid), which the simulator cannot measure (deep-runs/credited_fillers_1120.py; the user's rule of 2026-11-08 that a "
                "page pick holds no talent that does nothing).")
            gone = {m["from"] for m in x["moves"]} - set(flat(x["allocation"]))
            b["core"] = [c for c in b.get("core", []) if c.get("talent") not in gone]
            bp.write_text(dumps(data) + "\n", encoding="utf-8")
        print(f"applied {key}")


if __name__ == "__main__":
    main()
