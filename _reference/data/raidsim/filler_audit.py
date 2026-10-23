"""Zero-value talent points in our raid builds, moved to talents that help in the real game (2026-09-29, user question: "why Wand
Specialization as a filler when Improved Channeling protects Arcane Missiles from damage?").

    python _reference/data/raidsim/filler_audit.py <class> --spec <entry> --build <id> [--iterations 3000] [--confirm 12000] [--write]
    python _reference/data/raidsim/filler_audit.py --all [--jobs 3] [--apply]

1. Every talent of the build is removed once in the simulator (the entry's rotation and setting, 180 s): a talent whose removal moves
   DPS (tanks: tank value) by less than ZERO is a free point here. Talents the rotation conditions on (run.apl_talents) never count
   as free: their removal run measures a broken rotation, not the talent.
2. Local search, one point at a time: move a point out of a free talent into any other talent (legal: validate_builds.check_state).
   A move is taken when it gains DPS (above GAIN on seed 1 and confirmed on an independent seed 2), or else when it costs nothing
   (no worse than -LOSS on both seeds) and the new talent is more useful in a real raid than the old one by UTILITY, a tag read
   from the beta tooltip: interrupt/pushback protection first, then threat reduction, mana cost, range, survival (tanks: survival
   first). A talent with none of these tags ranks last, so a point never moves into another dead talent.
3. It stops when no move is taken. --write saves the record under research/raid/raidsim/<entry>-fillers-<build>.json; --apply puts
   the final allocation into proposed-builds.json with a note naming every move.
A talent that grants an ability is free only when the build never casts it (no cast in the base run nor in a run in the other setting,
not a pre-pull action) and casting it was shown not to pay: the spell probe tried it at every rotation spot in this entry
and kept no line (`raidsim/ml/spell-probe.json`), it is in VERIFIED_UNUSED, the rotation has a line for it that never fires (the
rotation search left it there), or it needs a trigger a raid boss never gives a damage dealer
(Riposte and Counterattack after a parry). Such a point counts as useless unless the ability is defensive (an absorb, a dodge cooldown,
damage taken reduced, a heal), which a player casts when needed: 2026-10-02, user report "the new Frost mage spec takes Arcane Blast but
never uses the ability in its rotation ... a wasted talent point". Before that date such points were only flagged, never moved.

The simulator models no pushback, range, threat limits or incoming damage for DPS builds: those talents measure 0 here, so the
utility order is our judgment, not a measurement. What the simulator does measure (DPS, mana) decides first.
"""
import argparse
import datetime
import json
import pathlib
import re
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[2]
sys.path.insert(0, str(ROOT / "_reference/data"))
sys.path.insert(0, str(HERE))
import paths  # noqa: E402
import talent_opt as T  # noqa: E402  (valid, by_tree, the run/apl_opt loaders)
import validate_builds as VB  # noqa: E402
from fmt_json import dumps  # noqa: E402

R, A = T.R, T.A
ZERO = 0.002    # |removal effect| under 0.2%: a free point
GAIN = 0.0015   # a real DPS gain
LOSS = 0.001    # a utility move may cost at most 0.1%
from utility_tags import TAGS, NONE, usefulness  # noqa: E402  (shared with the scorer's raid tie-break)


def utility(cls, tank=False):
    return usefulness(cls, tank)


# abilities from talents that were inserted at every spot of their rotations and never gained (2026-09-29, 20000 iterations, independent
# seeds): their points are free like any other zero-value point
VERIFIED_UNUSED = {"hunter": {"Sniper Shot"}, "rogue": {"Venom", "Ghostly Strike"}}
TRIGGERED = re.compile(r"after (?:you |the caster )?(?:parry|parries|parrying|block|blocking)", re.I)   # a raid boss attacks the tank, not you
DEFENSIVE = re.compile(r"absorb|dodge|damage taken|reduces? (?:all )?(?:physical )?damage|heal", re.I)


def spell_ids(cls):
    """{spell name: (every rank's id, the top rank's tooltip)} from the beta spellbook."""
    out = {}
    for tab in json.load(open(ROOT / "_reference/data/forever-spells" / f"{cls}.json", encoding="utf-8")).get("tabs", []):
        for sp in tab.get("spells", []):
            ranks = [r for r in sp.get("ranks", []) if r.get("id")]
            ids, text = out.get(sp.get("name", ""), (set(), ""))
            out[sp.get("name", "")] = (ids | {int(r["id"]) for r in ranks}, (str(ranks[-1].get("text", "")) if ranks else "") or text)
    return out


def apl_spell_ids(path, key):
    """Spell ids named anywhere in one part of a rotation file (priorityList or prepullActions)."""
    try:
        apl = json.load(open(path, encoding="utf-8"))
    except (OSError, ValueError):
        return set()
    acc, todo = set(), [apl.get(key, [])]
    while todo:
        x = todo.pop()
        if isinstance(x, dict):
            for k, v in x.items():
                if k == "spellId" and isinstance(v, int):
                    acc.add(v)
                else:
                    todo.append(v)
        elif isinstance(x, list):
            todo += x
    return acc


def probe_not_worth(cls, spec):
    """Abilities the spell probe tried in this entry without keeping a line (any setting), minus any it kept."""
    p = HERE / "ml" / "spell-probe.json"
    tried, kept = set(), set()
    if p.exists():
        for rec in json.load(open(p, encoding="utf-8")).values():
            if rec.get("class") == cls and rec.get("entry") == spec:
                for ab in rec.get("abilities", []):
                    if ab.get("best") is not None or ab.get("kept"):
                        (kept if ab.get("kept") else tried).add(ab["ability"])
    return tried - kept


def audit(cls, spec, bid, iterations, confirm, alloc=None, setting=None):
    """`alloc` ({talent: rank}) audits an allocation that is not a build of ours (ml_builds.py: the search winners on the rankings page),
    `setting` overrides the entry's (a parse build is played in a full raid)."""
    R.set_game("forever")
    repo = R.repo_path(argparse.Namespace(repo=None))
    entry = R.SPECS[cls][spec]
    where = setting or ("raid" if bid.endswith("-parse") else R.setting(entry))
    tank = bool(entry.get("tank"))
    trees = VB.load_forever()[cls]
    sim_trees = R.load_trees(repo, cls)
    if alloc is None:
        data = {b["id"]: b for b in json.load(open(paths.builds_json("forever", cls), encoding="utf-8"))["builds"]}
        cur = R.alloc_of(data[bid])
    else:
        cur = dict(alloc)
    names = {(t.get("fancyName") or t.get("fieldName")): (R.talent_key(t) or t.get("fieldName")) for tr in sim_trees for t in tr["talents"]}
    protect = {names.get(n, n) for n in R.apl_talents(repo, entry, sim_trees, where)} & set(cur)
    protect |= set(entry.get("not_measured", {})) & set(cur)   # values the standard target cannot show (Murder: Humanoids and Giants)
    # the talents that grant the build's spec its required signature spells never count as free (user rule 2026-10-22, signature_spells.json)
    import raid_signature as SIG
    bd = None
    if alloc is None:
        bd = data.get(bid)
    protect |= SIG.required_talents(cls, SIG.entry_spec(cls, spec, cur, bd)) & set(cur)
    # a talent that grants an ability is free only when the build never casts it and casting it was shown not to pay (see the docstring)
    book = spell_ids(cls)
    active = (set(cur) & set(book)) - VERIFIED_UNUSED.get(cls, set())
    other = "raid" if where != "raid" else "dummy"
    around = apl_spell_ids(R.apl_path(entry, repo, where), "prepullActions") | apl_spell_ids(R.apl_path(entry, repo, other), "prepullActions")
    not_worth = probe_not_worth(cls, spec) | VERIFIED_UNUSED.get(cls, set())
    # a line the rotation search left where it never fires: moving it up was one of its edits, so casting it does not pay either
    listed = apl_spell_ids(R.apl_path(entry, repo, where), "priorityList")
    use = dict(utility(cls, tank))
    tag = f"fillers-{cls}-{spec}"

    def run(allocs, its, seed):
        bl = [{"label": str(i), "talents": R.talents_string(sim_trees, al)} for i, al in enumerate(allocs)]
        rows = A.bench(entry, repo, bl, its, seed, where, tag)
        return [rows.get(str(i)) for i in range(len(allocs))]

    def val(row, ref):
        return (A.value(row, ref, tank) or 0.0) - 1.0

    # 1. removal effects
    held = sorted(cur)
    rows = run([cur] + [{k: v for k, v in cur.items() if k != n} for n in held], iterations, 1)
    base = rows[0]
    effect = {n: -val(r, base) for n, r in zip(held, rows[1:])}   # DPS lost when the talent goes
    cast = {}
    other_row = A.bench(entry, repo, [{"label": "o", "talents": R.talents_string(sim_trees, cur)}], iterations, 1, other, tag).get("o") or {}
    for row in (base, other_row):   # casts in this setting and in the other one (a raid-only cooldown is used)
        for act in row.get("actions") or []:
            for n in active:
                if act.get("spellId") in book[n][0]:
                    cast[n] = cast.get(n, 0) + (act.get("casts") or 0)
    unused = {n for n in active if not cast.get(n) and not (book[n][0] & around)
              and (n in not_worth or TRIGGERED.search(book[n][1]) or book[n][0] & listed)}
    for n in unused:   # never cast: its tooltip's tags say nothing about the fight, unless a player casts it when needed (a defensive)
        if TRIGGERED.search(book[n][1]) or not DEFENSIVE.search(book[n][1]):
            use[n] = NONE
    free = {n for n, e in effect.items() if abs(e) < ZERO and n not in protect and (n not in active or n in unused)}
    flags = sorted(n for n, e in effect.items() if abs(e) < ZERO and n in active and n not in unused)
    print(f"== {cls} {spec} {bid} ({where}): {base['dps']:.1f} DPS; free: " + (", ".join(f"{n} {cur[n]}" for n in sorted(free)) or "none"), flush=True)
    start = dict(cur)
    moves = []
    for rnd in range(1, 40):
        cands = []
        for a in sorted(free & set(cur)):
            for b in use:
                if b == a:
                    continue
                new = dict(cur)
                new[a] -= 1
                if not new[a]:
                    del new[a]
                new[b] = new.get(b, 0) + 1
                if T.valid(trees, new):
                    cands.append((a, b, new))
        if not cands:
            break
        rows = run([cur] + [c[2] for c in cands], iterations, 1)
        ref = rows[0]
        scored = [(val(r, ref), a, b, new) for r, (a, b, new) in zip(rows[1:], cands) if r and not r.get("error")]
        gains = sorted([s for s in scored if s[0] > GAIN], key=lambda s: -s[0])[:5]
        # utility moves: no loss, into a strictly more useful talent (a lower rank of usefulness than the point's old talent)
        utils = sorted([s for s in scored if s[0] >= -LOSS and use.get(s[2], NONE) < use.get(s[1], NONE)],
                       key=lambda s: (use.get(s[2], NONE), -s[0]))[:5]
        took = None
        for kind, pool in (("gain", gains), ("utility", utils)):
            if not pool:
                continue
            conf = run([cur] + [s[3] for s in pool], confirm, 2)
            for s, r in zip(pool, conf[1:]):
                v2 = val(r, conf[0])
                if (kind == "gain" and v2 > GAIN) or (kind == "utility" and v2 >= -LOSS):
                    took = (kind, s, v2)
                    break
            if took:
                break
        if not took:
            break
        kind, (v1, a, b, new), v2 = took
        cur = new
        moves.append({"round": rnd, "kind": kind, "from": a, "to": b, "seed1": v1, "seed2": v2, "utility": [t for t, _ in TAGS][use[b]] if use[b] < NONE else None})
        if b not in free and kind == "utility":
            pass
        print(f"  {rnd}: 1 point {a} -> {b} ({kind}; {v1:+.2%} seed 1, {v2:+.2%} seed 2)", flush=True)
    fin = run([start, cur], confirm, 3)
    total = val(fin[1], fin[0])
    print(f"  final (seed 3): {total:+.2%}", flush=True)
    return {"class": cls, "spec": spec, "build": bid, "setting": where, "date": datetime.date.today().isoformat(), "tank": tank,
            "removal": effect, "free": sorted(free), "kept_for_rotation": sorted(protect), "active_never_worth": flags,
            "abilities_never_cast": sorted(unused), "moves": moves, "final_seed3": total,
            "start": {t: [[n, r] for n, r in T.by_tree(trees, start)[t].items()] for t in trees},
            "allocation": {t: [[n, r] for n, r in T.by_tree(trees, cur)[t].items()] for t in trees}}


def targets():
    """(class, entry, build) for every hand raid DPS or tank build of ours, in the entry that races it."""
    R.set_game("forever")
    out = []
    for cls, es in R.SPECS.items():
        if cls.startswith("_"):
            continue
        builds = {b["id"]: b for b in json.load(open(paths.builds_json("forever", cls), encoding="utf-8"))["builds"]}
        seen = set()
        for spec, e in es.items():
            if not isinstance(e, dict):
                continue
            for bid in e.get("builds", []):
                b = builds.get(bid)
                if b and not bid.startswith("opt-") and b.get("content") == "raid" and b.get("role") != "healer" and bid not in seen:
                    seen.add(bid)
                    out.append((cls, spec, bid))
    return out


def record_path(cls, spec, bid):
    return paths.raidsim_dir(cls) / f"{spec}-fillers-{bid}.json"


def apply(rec):
    """Put a record's allocation into proposed-builds.json with a note (only when it moved points)."""
    if not rec["moves"]:
        return False
    bp = paths.builds_json("forever", rec["class"])
    data = json.load(open(bp, encoding="utf-8"))
    b = next(x for x in data["builds"] if x["id"] == rec["build"])
    b["allocation"] = rec["allocation"]
    mv = "; ".join(f"{m['from']} -> {m['to']}" + (f" ({m['utility']})" if m["kind"] == "utility" and m["utility"] else f" ({m['seed2']:+.1%} DPS)") for m in rec["moves"])
    never = sorted({m["from"] for m in rec["moves"]} & set(rec.get("abilities_never_cast", [])))
    b.setdefault("notes", []).append(
        f"{rec['date']} filler audit (raidsim/filler_audit.py, user question on zero-value fillers"
        + (f"; 2026-10-02 user report on talents whose ability the rotation never casts: {', '.join(never)} was never cast here" if never else "")
        + f"): points the simulator measures at 0 moved, one at a "
        f"time, to talents that help in a real raid (interrupt protection, threat, mana, range, survival; the simulator cannot see these, so the order is "
        f"our judgment) or that gain DPS: {mv}. Net {rec['final_seed3']:+.2%} on a third seed.")
    gone_all = {m["from"] for m in rec["moves"]} - {n for it in rec["allocation"].values() for n, _ in it}
    b["core"] = [c for c in b.get("core", []) if c.get("talent") not in gone_all]   # a core talent the audit took out is no longer core
    for fx in b.get("flex", []):   # flex entries naming a talent that left the build now name its replacement
        gone = [m for m in rec["moves"] if m["from"] == fx.get("default") and not any(n == m["from"] for it in rec["allocation"].values() for n, _ in it)]
        if gone:
            fx["alternatives"] = sorted(set(fx.get("alternatives", [])) | {fx["default"]})
            fx["default"] = gone[-1]["to"]
    bp.write_text(dumps(data) + "\n", encoding="utf-8")
    return True


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("cls", nargs="?")
    ap.add_argument("--spec")
    ap.add_argument("--build")
    ap.add_argument("--all", action="store_true")
    ap.add_argument("--jobs", type=int, default=3)
    ap.add_argument("--iterations", type=int, default=3000)
    ap.add_argument("--confirm", type=int, default=12000)
    ap.add_argument("--setting", choices=["dummy", "raid"], help="the setting to audit in (default: the entry's; a -parse build: the raid)")
    ap.add_argument("--write", action="store_true")
    ap.add_argument("--apply", action="store_true", help="with --all: apply the written records to proposed-builds.json")
    a = ap.parse_args()
    if a.all:
        todo = targets()
        if a.apply:
            for cls, spec, bid in todo:
                p = record_path(cls, spec, bid)
                if p.exists() and apply(json.load(open(p, encoding="utf-8"))):
                    print(f"applied {cls} {bid}")
            return
        procs = []
        for cls, spec, bid in todo:
            if record_path(cls, spec, bid).exists():
                continue
            while len([p for p in procs if p.poll() is None]) >= a.jobs:
                procs[0].wait() if procs[0].poll() is None else procs.pop(0)
                procs = [p for p in procs if p.poll() is None]
            procs.append(subprocess.Popen([sys.executable, __file__, cls, "--spec", spec, "--build", bid, "--iterations", str(a.iterations),
                                           "--confirm", str(a.confirm), "--write"]))
        for p in procs:
            p.wait()
        return
    rec = audit(a.cls, a.spec, a.build, a.iterations, a.confirm, setting=a.setting)
    if a.write:
        p = record_path(a.cls, a.spec, a.build)
        p.write_text(json.dumps(rec, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
        print(f"  wrote {p.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
