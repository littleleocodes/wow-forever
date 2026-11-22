"""Leveling filler pass (2026-11-08, user: "the resto druid talent spec says to take Improved Wrath. Why would that ever be a thing?
Theres not a single other better place to spend that talent? Check thinks like that constantly"; page-audit-1108 S14).

A leveling page's build can spend points on talents that do nothing in its rotation: an old hand draft the open search's polish never
touched (the Retribution pick, 2026-09-26: Vindication 3, Purifying Power 2, Sacred Duty while Improved Seals sits at 3/5), or a gate
filled with a talent nobody presses. For the spec page's pick (level_guides.pick: its build, order and rotation):

1. every talent's value at level 60 by removal (one rank less; common random numbers);
2. the zero points: a removal that costs less than the noise floor, removable while every prefix of the order stays a legal build;
3. every move of a zero point (its last rank in the order) to any other talent at the same level, legal along the whole order, raced at
   the levels from that point on (20-60 by fives, weighted level / 10 as every leveling race) on seed 3; the best that gains --bar
   (0.3%, fl_levels' bar) is checked on seed 4 and kept when it holds there, then the pass starts over;
4. else a tie-break (the best of the top moves that is faster on both seeds), else a "no loss" move (2026-11-09: one that costs at most
   NO_LOSS, 0.1%, on each seed), always into a talent that is not itself a zero point: a point that does nothing never stays;
5. then the tier-gate points (2026-11-09): a point the build cannot drop is moved to any talent legal along the order when that is
   faster on both seeds (`--no-gates` skips it). A gate that does nothing by mechanics (Redoubt's block without a shield) and costs
   nothing to move is a judgment call the pass leaves to the reader: its swap measures 0.00%.
5b. (2026-11-21, the audit session's rule on gates) a gate point that does nothing (a talent ability the build never presses, a talent
   that improves only spells it never casts, or one whose last rank's removal leaves the time per kill the same to 0.01 s at every race
   level it is held) is not excused by being a gate when the gate is a tier point: any legal talent of the rows below can hold it
   (Frost's Arcane Blast at 56, never pressed, the fifteenth point Arcane Meditation's tier needs). With no home faster on both seeds it
   moves at no loss (NO_LOSS on each seed) into a legal talent that changes the fight (times not bit for bit the build's), never a talent
   ability nor a dead talent. At bit-identical times a talent ability never pressed, or a talent dead by its tooltip, goes to the legal
   home highest in the leveling utility order (survival first), if that home stands higher than its own talent and is neither a talent
   ability nor dead (the audit session's refinement, the same night: Frost's Arcane Blast to Magic Absorption). Else the record keeps
   the homes it tried (`gates_checked`, and `no_better_home`, which the leveling play check's Lc reads; zero points that found no home
   in steps 3-4 are listed there too). A prerequisite (another held talent requires it
   by name, gate_kind.py) has no legal home. `--dead-gates-only` runs only this step, a correction after a pass; `--no-dead-gates`
   skips it.
Dead destinations (2026-11-18, page_lint's dead check after the eat-and-drink regen): a tie-break or "no loss" move never goes into a
talent that only improves spells or forms the rotation never casts (page_lint's tooltip reading, against the spells the build casts at
20-60 in the lab; talent abilities are not judged this way, Cold Snap being a module note rather than a cast). An unheld talent was
never measured, so "not a zero point" let the 2026-11-17 Frost pass move Incineration's third point into Accelerant (Fireball, Frostfire
Bolt and Arcane Wrath only). A dead talent's last points may move again, where "no loss" otherwise never moves a talent twice: the
Balance pass had moved two Ferocity points to Vengeance and left the third.

    python _reference/data/fightlab/fl_filler_pass.py <class> --spec "<Spec>" [--fights 1500] [--jobs 10] [--write]

Record `fightlab/filler/<class>-<spec slug>.json`; `--write` applies the kept moves to the build and its order in proposed-builds.json
with a note. Then: `level_guides.py <class> --measure`, regenerate the pages. Fight-lab numbers are a model of the beta.
"""
import argparse
import datetime
import json
import multiprocessing
import pathlib
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[2]
sys.path[:0] = [str(HERE), str(ROOT / "_reference/data/scorer"), str(ROOT / "_reference/data"), str(ROOT / "_reference/data/raidsim")]
import fl_levels as FL  # noqa: E402
import fl_open_search as FO  # noqa: E402
import fl_talent_opt as FT  # noqa: E402
import level_guides as LG  # noqa: E402
import signature as SG  # noqa: E402  (signature spells, user rule 2026-10-22)
import gate_kind as GK  # noqa: E402
import utility_tags as UT  # noqa: E402
import validate_builds as VB  # noqa: E402

LEVELS = [20, 25, 30, 35, 40, 45, 50, 55, 60]
# step 5b's worth-nothing test is the play check's Lc (fightlab/play_check.zero_talents): seed 1, at 60 and every level of 20-50 by tens
# it is held (2026-11-21: on seed 3 and every 5 levels the two had disagreed at the margin)
LC_SEED, LC_LEVELS = 1, [20, 30, 40, 50]
OUT = HERE / "filler"
NO_LOSS = 0.001   # a "no loss" move may cost at most 0.1% of the level-weighted time per kill on each seed (2026-11-09)
DEAD_GATES = True   # step 5b by default (2026-11-21)
# The stats model's kinds the fight lab cannot see (2026-11-21; scorer/kinds.json): the lab keeps travel fixed at 6 s a kill (move),
# never presses a control ability (stun), has no runners by default (stick) and no stealth movement or escapes. A talent with one of
# them never moves in this pass, in any step: the lab's times do not weigh its value (the Retribution pick's Pursuit of Justice had
# gone to Deflection at 21 and 22, Repentance at 49). Its record says so ("kept: utility (<kinds>) ..."), which the play check reads.
# Two exceptions (the audit session's ruling, the same night): a point may move between talents of the same unseen kind (Pathfinding to
# Bestial Swiftness), and a talent dead by its own condition is not protected whatever its kind (Improved Sayaad in a Voidwalker build:
# dead_talents, its tooltip's spells or forms never cast).
UNSEEN_KINDS = {"move", "stun", "stick", "stealth", "escape"}


# A talent ability is a home for a point only when it helps the player live or get away (2026-11-21, the audit session: a root, a
# stun, an escape, a defensive; the stats model's kinds) or when the build presses it; never a damage ability the build does not
# press. Such a talent stands with survival in the leveling utility order.
LIVE_KINDS = {"kite", "stun", "stick", "escape", "move", "stealth"}


def _kinds_of(cls, talent):
    if not hasattr(unseen_kinds, "_k"):
        unseen_kinds._k = json.load(open(ROOT / "_reference/data/scorer/kinds.json", encoding="utf-8")).get("talents") or {}
    e = (unseen_kinds._k.get(cls) or {}).get(talent) or {}
    if e.get("games") and "forever" not in e["games"]:
        return {}
    return {k: v for k, v in e.items() if k in ("utility", "surv", "sustain")}


def lives(cls, talent):
    """Whether a talent helps the player live or get away: a control, escape or movement kind, or a survival kind."""
    k = _kinds_of(cls, talent)
    return bool(set(k.values()) & LIVE_KINDS) or "surv" in k


def lev_rank(cls, talent, use):
    """A talent's place in the leveling utility order (0 best): utility_tags' tag, survival first; a talent that helps the player
    live or get away stands with survival."""
    r = use.get(talent, UT.NONE)
    return min(r, 0) if lives(cls, talent) else r


def unseen_kinds(cls, talent):
    """The kinds of `talent` (scorer/kinds.json, this game) that the fight lab cannot see."""
    if not hasattr(unseen_kinds, "_k"):
        unseen_kinds._k = json.load(open(ROOT / "_reference/data/scorer/kinds.json", encoding="utf-8")).get("talents") or {}
    e = (unseen_kinds._k.get(cls) or {}).get(talent) or {}
    if e.get("games") and "forever" not in e["games"]:
        return set()
    return {v for k, v in e.items() if k in ("utility", "surv", "sustain")} & UNSEEN_KINDS


def flat_of(pts):
    out = {}
    for _, n in pts:
        out[n] = out.get(n, 0) + 1
    return out


def per_level(pool, cls, rot, space, builds, levels, fights, seed):
    """{level: time per kill} for each per-point order in `builds` (the allocation at each level from the order)."""
    jobs = []
    for pts in builds:
        order = FL.compress(pts)
        b = {"allocation": FL.alloc_of(space, flat_of(pts)), "order": order}
        jobs += [(cls, rot, FL.FR.allocation_at(b, L), L, fights, seed, True, (flat_of(pts), order)) for L in levels]
    res = pool.map(FO._ttk, jobs, chunksize=1)
    return [{L: res[i * len(levels) + k][0] for k, L in enumerate(levels)} for i in range(len(builds))]


# A cast that needs stealth: the stealth spell is used though the lab never counts it as a cast (2026-11-21: Feral's Ravage, Prowl)
STEALTH_OPENERS = {"druid": ({"Ravage", "Pounce"}, "Prowl"), "rogue": ({"Ambush", "Garrote", "Cheap Shot"}, "Stealth")}


def _casts(job):
    """The spells an allocation uses at a level, as the fight lab reports them (2026-11-21, the audit session: the tooltip reading had
    called live talents dead because what they improve never appears as a cast): the casts; the damage sources (Thorns deals damage
    and is never cast); the standing effect (the lab's armor_spell: a form, stance, aura, aspect or armor; a cat starts in Cat Form);
    the stealth a cast opener needs (Prowl for Ravage); and, when the build heals between fights (heal_per_kill), every heal of its
    spellbook (the downtime heals are not counted by spell: Feral's Nature's Splendor, Rejuvenation and Regrowth between fights, is
    2.9% of the time per kill at 60). It errs on the side of calling a talent live."""
    cls, rot, alloc, level, fights, seed = job
    o = FL.FR.simulate(cls, alloc, level, rot, fights, seed, 0)
    used = {s for s, n in (o.get("casts") or {}).items() if n}
    used |= {s for s, v in (o.get("shares") or {}).items() if v}
    used |= {s for s, v in (o.get("healing_per_kill") or {}).items() if v}
    if o.get("armor_spell"):
        used.add(o["armor_spell"])
    op = STEALTH_OPENERS.get(cls)
    if op and used & op[0]:
        used.add(op[1])
    if (o.get("heal_per_kill") or 0) > 0:   # a heal a talent grants counts only with its talent (2026-11-22, the audit session: Shadow,
        tal = talent_names(cls)             # healing between fights at 20-30, had Penance in its "used" and Power in Light read as live)
        used |= {s for s in heal_spells(cls) if s not in tal or alloc.get(s)}
    used |= passive_spells(cls)
    return used


def talent_names(cls):
    """Every talent's name in the class's Forever trees (a talent ability carries its talent's name)."""
    import page_lint as PL
    return {t["name"] for tr in PL.talents(cls) for t in tr["talents"]}


def passive_spells(cls):
    """The class spellbook's passives (no cast time, no cost: the rogue's Poised, which Composure improves): always in use, never a cast."""
    out = set()
    for tab in json.load(open(ROOT / "_reference/data/forever-spells" / f"{cls}.json", encoding="utf-8")).get("tabs", []):
        for sp in tab.get("spells", []):
            r = (sp.get("ranks") or [{}])[-1]
            if not (r.get("cast") or "").strip() and not (r.get("cost") or "").strip():
                out.add(sp["name"])
    return out


def heal_spells(cls):
    """The class spellbook's heals (a rank's tooltip says it heals), for the downtime heals the lab does not count by spell."""
    import re
    out = set()
    for tab in json.load(open(ROOT / "_reference/data/forever-spells" / f"{cls}.json", encoding="utf-8")).get("tabs", []):
        for sp in tab.get("spells", []):
            tip = " ".join(str(r.get("text") or r.get("tooltip") or "") for r in (sp.get("ranks") or [])[-1:])
            if re.search(r"\bheal(?:s|ing)?\b", tip, re.I):
                out.add(sp["name"])
    return out


def dead_talents(cls, used):
    """{talent: the spells it improves}: the class's talents that only improve spells or forms of which `used` holds none, read from
    the tooltips as page_lint.dead_talents reads them (a family word, "your Shock spells", or a general effect makes a talent live).
    Talent abilities are left out (a module can play one without a cast: the mage's Cold Snap is a note)."""
    import re
    import page_lint as PL
    book = set(LG.book(cls)) | PL.FORMS
    out = {}
    for tr in PL.talents(cls):
        for t in tr["talents"]:
            if t["name"] in book:
                continue
            tip = PL.rank_text(t)
            names = {n for n in book if re.search(rf"\b{re.escape(n)}\b", tip)}
            names -= {n for n in names if any(n != o and n in o for o in names)}   # "Bear Form" inside "Dire Bear Form"
            rest = tip
            for n in names:
                rest = rest.replace(n, " ")
            trig = PL.trigger_names(tip, names)   # its effect needs a spell the build never uses (page_lint.TRIGGER, 2026-11-22)
            if trig and not (trig & used):
                out[t["name"]] = sorted(trig)
                continue
            imp = PL.improved_names(tip, names)   # a spell named only as the effect's condition is not what it improves (2026-11-22)
            if imp and not PL.FAMILY.search(rest) and not PL.GENERIC.search(rest) and not (imp & used):
                out[t["name"]] = sorted(imp)
    return out


def dead_from_levels(cls, used_at, level):
    """The talents dead for a point taken at `level` (2026-11-22): judged by what the build uses at the race levels from that level's
    five on, not at every level. The Affliction pass had put points in Improved Shadow Bolt (51) and Nightfall (58) on the Shadow Bolts
    its build casts only at 20-35."""
    L0 = level - level % 5
    lv = [L for L in LEVELS if L >= L0] or [LEVELS[-1]]
    return dead_talents(cls, set().union(*[used_at[L] for L in lv]))


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("cls")
    ap.add_argument("--spec", required=True)
    ap.add_argument("--fights", type=int, default=1500)
    ap.add_argument("--jobs", type=int, default=10)
    ap.add_argument("--bar", type=float, default=0.003)
    ap.add_argument("--max-moves", type=int, default=6)
    ap.add_argument("--write", action="store_true")
    ap.add_argument("--no-gates", dest="gates", action="store_false", help="skip step 5, the tier-gate points")
    ap.add_argument("--dead-only", action="store_true",
                    help="move only the points of talents that do nothing for what the build casts (a correction after a pass: 2026-11-18, "
                         "a full re-run of the Frost pass also moved Cold Snap and Permafrost on 0.1-0.2%% of noise, at Arcea's next "
                         "levels); of the gates only those that do nothing (step 5b)")
    ap.add_argument("--no-dead-gates", dest="dead_gates", action="store_false", help="skip step 5b, the gate points that do nothing")
    ap.add_argument("--dead-gates-only", action="store_true", help="run only step 5b (a correction after a pass)")
    ap.add_argument("--from-dry", action="store_true", help="start from the dry run's result (<record>.dry.json) and write <record>.dry2.json: "
                    "the second of two passes, to check that a pass over a settled build moves nothing (2026-11-21); never with --write")
    ap.set_defaults(dead_gates=DEAD_GATES)
    a = ap.parse_args()
    if a.dead_only:
        a.gates = False
    if a.dead_gates_only:
        a.gates, a.dead_gates = False, True
    cls = a.cls
    b, order, prov, rot = LG.pick(cls, a.spec)
    if not b:
        sys.exit(f"{cls} {a.spec}: no leveling pick")
    slug0 = a.spec.lower().replace("/", "-").replace(" ", "-")
    main_rec = OUT / f"{cls}-{slug0}.json"
    dry_rec = None
    if a.from_dry:
        if a.write:
            sys.exit("--from-dry never writes")
        dry_rec = json.load(open(OUT / f"{cls}-{slug0}.dry.json", encoding="utf-8"))
        order = dry_rec["final_order"]
    # the build's record chain (2026-11-21): the moves its record applied; a move that is not above the bar never reverses one.
    # 2026-11-22 (the audit session, after four reversals across the redos of 2026-11-20 and 2026-11-22): the chain belongs to the lab's
    # model, not to the build's order. A record made under the same model fingerprint (fl_open_search.sim_fingerprint: engine, tables,
    # class modules, rules, talent and spell data, the lab's tables) binds whatever the order; a change of model starts a new chain, and
    # the first pass on the new model is then held by its own moves. A record from before the fingerprint was stored binds only on the
    # build's order, as it did. Until then the chain loaded only on the order, so a redo that re-raced the order reset it unannounced.
    model = FO.sim_fingerprint(cls, rot)
    chain, chain_state = set(), "none (no record)"
    if main_rec.exists():
        r0 = json.load(open(main_rec, encoding="utf-8"))
        same_order = r0.get("final_order") == b.get("order") or (r0.get("written") or {}).get("order") == b.get("order")
        if r0.get("model") == model or (not r0.get("model") and same_order):
            chain |= {(m["from"], m["to"]) for m in r0.get("moves") or []}
            chain_state = "kept: the same model" if r0.get("model") == model else "kept: no model recorded, the same order"
        else:
            chain_state = "new: the model changed since the last pass" if r0.get("model") else "new: no model recorded and the order changed"
    print(f"  record chain: {chain_state} ({len(chain)} moves)", flush=True)
    if dry_rec:
        chain |= {(m["from"], m["to"]) for m in dry_rec.get("moves") or []}
    MLT = FO._load("ml_talents_open", ROOT / "_reference/data/raidsim/ml_talents.py")   # as fl_levels.main loads it
    space = MLT.Space(cls, "any", any_split=True)
    pts = FL.expand(order)
    total = len(pts)
    # The spec's signature talents never move (2026-11-16): the talents that grant its required spells (signature.py, the user's rule of
    # 2026-10-22: a spec plays its signature spells). The Shockadin's first pass moved Holy Shock to Deflection, its removal 3.8% faster in
    # the melee gear the Holy rules had just taken, and the points that only serve it (Divine Favor, Infusion of Light, Oath of Light)
    # followed: a Shockadin without Holy Shock. The build's own spec, as the pages judge it.
    keep = set(SG.granting_talents(cls, (SG.rule(cls, b.get("spec") or a.spec, "leveling") or {}).get("required") or []))
    rec = {"class": cls, "spec": a.spec, "build": b["id"], "rotation": rot, "date": datetime.date.today().isoformat(), "fights": a.fights,
           "start_order": FL.compress(pts), "steps": [], "moves": [], "kept_signature": sorted(keep), "model": model, "chain": chain_state}
    if keep:
        print(f"  signature talents kept where they are: {', '.join(sorted(keep))}", flush=True)
    unseen = {}
    print(f"== {cls} {a.spec}: {b['id']} ({rot}), {total} points", flush=True)
    gates_checked, no_home = {}, {}   # step 5b's record and the dead points that found no home (steps 3-4 and 5b)
    with multiprocessing.Pool(a.jobs, initializer=FT._init, initargs=("greens",)) as pool:
        # the unseen kinds (see UNSEEN_KINDS): a talent dead by its own condition is not protected
        cand0 = {n: unseen_kinds(cls, n) for n in flat_of(pts) if unseen_kinds(cls, n)}
        if cand0:
            b0 = {"allocation": FL.alloc_of(space, flat_of(pts)), "order": FL.compress(pts)}
            used0 = set().union(*pool.map(_casts, [(cls, rot, FL.FR.allocation_at(b0, L), L, a.fights, 3) for L in LEVELS], chunksize=1))
            dead0 = dead_talents(cls, used0)
            unseen.update({n: k for n, k in cand0.items() if n not in dead0})
            if set(cand0) - set(unseen):
                print("  dead by its own condition, so not protected: " + ", ".join(sorted(set(cand0) - set(unseen))), flush=True)
        if unseen:
            print("  a value the lab cannot see (moves only to a talent of the same kind): "
                  + ", ".join(f"{n} ({', '.join(sorted(k))})" for n, k in sorted(unseen.items())), flush=True)
        for _ in range(0 if a.dead_gates_only else a.max_moves):
            base = per_level(pool, cls, rot, space, [pts], LEVELS, a.fights, 3)[0]
            w0 = FL.weighted_at(base, LEVELS)
            # 1-2: removal values at 60 and the zero points (the last rank of each talent, legal along the order without it)
            held = sorted(flat_of(pts))
            drops = []
            for n in held:
                if n in keep:
                    continue
                i = max(k for k, (_, x) in enumerate(pts) if x == n)
                rest = pts[:i] + pts[i + 1:]
                if FL.legal_order(space, rest, total - 1):
                    drops.append((n, i, rest))
            r60 = per_level(pool, cls, rot, space, [rest for _, _, rest in drops], [60], a.fights, 3)
            value = {n: base[60] - r[60] for (n, _, _), r in zip(drops, r60)}   # negative: the build is slower without it
            floor = 0.003 * base[60]
            zero = [(n, i) for n, i, _ in drops if value[n] > -floor]
            # the talents that do nothing for what this build casts (2026-11-18): never a tie-break or "no loss" destination
            bb = {"allocation": FL.alloc_of(space, flat_of(pts)), "order": FL.compress(pts)}
            used_l = pool.map(_casts, [(cls, rot, FL.FR.allocation_at(bb, L), L, a.fights, 3) for L in LEVELS], chunksize=1)
            used_at, used = dict(zip(LEVELS, used_l)), set().union(*used_l)
            dead = dead_talents(cls, used)
            dead_by = {}

            def dead_at(i, used_at=used_at, dead_by=dead_by):   # dead for a point at order index i, by the build's use from that
                if i not in dead_by:                              # level on (dead_from_levels, 2026-11-22)
                    dead_by[i] = dead_from_levels(cls, used_at, 10 + i)
                return dead_by[i]
            zero_all = {z for z, _ in zero}   # no destination is a zero point, dead or not
            if a.dead_only:
                zero = [(n, i) for n, i in zero if n in dead_at(i)]
            print(f"  weighted {w0:.2f} s; zero points{' (dead only)' if a.dead_only else ''}: {', '.join(n for n, _ in zero) or 'none'}"
                  + (f"; dead talents held: {', '.join(n for n in held if n in dead)}" if any(n in dead for n in held) else ""), flush=True)
            rec["steps"].append({"weighted": round(w0, 3), "values_at_60": {n: round(v, 3) for n, v in value.items()}, "zero": [n for n, _ in zero],
                                 "dead_held": [n for n in held if n in dead]})
            if not zero:
                break
            # 3: every move of a zero point to another talent at the same level
            cand = []
            for n, i in zero:
                tree = pts[i][0]
                for tname in space.tree_names:
                    for d in space.by_tree[tname]:
                        if d == n or (n in unseen and not (unseen_kinds(cls, d) & unseen[n])):
                            continue
                        new = pts[:i] + [(tname, d)] + pts[i + 1:]
                        if FL.legal_order(space, new, total):
                            cand.append((n, d, i, new))
            if not cand:
                for n, _ in zero:
                    no_home[n] = {"kind": "zero point", "exact": abs(value[n]) < 0.005, "why": f"time per kill at 60 without its last rank: {-value[n]:+.2f} s (seed 3)", "homes": 0}
                break
            scored = []
            for i in sorted({c[2] for c in cand}):   # a move changes the build from its level on: race only those levels
                group = [c for c in cand if c[2] == i]
                lv = [L for L in LEVELS if L >= 10 + i] or [60]
                for (n, d, _, new), res in zip(group, per_level(pool, cls, rot, space, [c[3] for c in group], lv, a.fights, 3)):
                    scored.append((FL.weighted_at({**base, **res}, LEVELS), n, d, i, new, all(res[L] == base[L] for L in res)))
            scored.sort(key=lambda s: s[0])
            w1, n, d, i, new, _ = scored[0]
            if w1 <= w0 * (1 - a.bar):
                b2, n2 = per_level(pool, cls, rot, space, [pts, new], LEVELS, a.fights, 4)
                g2 = FL.weighted_at(n2, LEVELS) / FL.weighted_at(b2, LEVELS) - 1
                print(f"  move {n} (level {10 + i}) -> {d}: {w0:.2f} -> {w1:.2f} s ({w1 / w0 - 1:+.2%}); seed 4 {g2:+.2%}", flush=True)
                if g2 <= -a.bar:
                    rec["moves"].append({"from": n, "to": d, "level": 10 + i, "seed3": round(w1 / w0 - 1, 4), "seed4": round(g2, 4), "why": "measured"})
                    pts = new
                    continue
            # no move clears the bar: the point measures nothing where it is, so it goes where it at least costs nothing and is no
            # dead weight (2026-11-08, user: "There's not a single other better place to spend that talent?"): the best few moves of
            # seed 3 that also cost no time on seed 4, a talent that is not itself a zero point
            tie = None
            moved = {m['from'] for m in rec['moves']}   # never move a point back into a talent it left
            use_l = UT.usefulness(cls, True)
            back = chain | {(m["from"], m["to"]) for m in rec["moves"]}
            # 2026-11-21 (the audit session, after Balance's ping-pong at 60): a tie-break goes strictly up the leveling utility order,
            # never between talents of equal rank, and no move under the bar reverses one in the build's record chain
            for w1, n, d, i, new, _ in [s for s in scored if s[0] < w0 and s[2] not in zero_all and s[2] not in moved
                                        and s[2] not in dead_at(s[3]) and lev_rank(cls, s[2], use_l) < lev_rank(cls, s[1], use_l)
                                        and (s[2], s[1]) not in back][:4]:
                b2, n2 = per_level(pool, cls, rot, space, [pts, new], LEVELS, a.fights, 4)
                g2 = FL.weighted_at(n2, LEVELS) / FL.weighted_at(b2, LEVELS) - 1
                if g2 < -0.0005 and (tie is None or (w1 / w0 - 1) + g2 < (tie[0] / w0 - 1) + tie[5]):   # faster on both seeds: the best
                    tie = (w1, n, d, i, new, g2)
            why = "tie-break"
            if not tie:
                # 2026-11-09: no move is faster on both seeds, so noise kept a dead point where it was (the Affliction pick's Improved
                # Sayaad, a Succubus talent in a Voidwalker build). A zero point still goes to a talent that measured something, when the
                # move costs no time beyond NO_LOSS on either seed: a point that does nothing is never better than one that does
                done = {m["from"] for m in rec["moves"]} | {m["to"] for m in rec["moves"]}
                # 2026-11-21 (the two-pass test on Balance: Gift of Nature to Bloom, then Bloom to Genesis, all within noise): a no-loss
                # move starts only from a point whose removal leaves the time per kill the same to 0.01 s, and lands only where the move
                # changes the fight, so the next pass cannot take the point on again
                for w1, n, d, i, new, _ in [s for s in scored if s[0] <= w0 * (1 + NO_LOSS) and s[2] not in zero_all
                                            and s[2] not in moved and s[2] not in dead_at(s[3]) and (s[1] not in done or s[1] in dead_at(s[3]))
                                            and (s[2], s[1]) not in back and abs(value.get(s[1], 1.0)) < 0.005 and not s[5]][:4]:
                    b2, n2 = per_level(pool, cls, rot, space, [pts, new], LEVELS, a.fights, 4)
                    g2 = FL.weighted_at(n2, LEVELS) / FL.weighted_at(b2, LEVELS) - 1
                    if g2 <= NO_LOSS and (tie is None or (w1 / w0 - 1) + g2 < (tie[0] / w0 - 1) + tie[5]):
                        tie = (w1, n, d, i, new, g2)
                why = "no loss"
            if not tie:
                for n, _ in zero:   # every legal home raced on seed 3, the best confirmed on seed 4: none faster, none at no loss
                    no_home[n] = {"kind": "zero point", "exact": abs(value[n]) < 0.005, "why": f"time per kill at 60 without its last rank: {-value[n]:+.2f} s (seed 3)",
                                  "homes": sum(1 for s in scored if s[1] == n)}
                print(f"  best move {scored[0][1]} -> {scored[0][2]}: {w0:.2f} -> {scored[0][0]:.2f} s: under the bar, no tie-break", flush=True)
                break
            w1, n, d, i, new, g2 = tie
            print(f"  {why} {n} (level {10 + i}) -> {d}: {w0:.2f} -> {w1:.2f} s; seed 4 {g2:+.2%}", flush=True)
            rec["moves"].append({"from": n, "to": d, "level": 10 + i, "seed3": round(w1 / w0 - 1, 4), "seed4": round(g2, 4), "why": why})
            pts = new
        # 5 (2026-11-09): tier-gate points. A point the build cannot drop (it holds a deeper talent's tier open) never reads as a zero
        # point above, so a gate filled with a talent that does little stays unmeasured: the Prot-Ret leveling build's Toughness, 2 of
        # the 15 Protection points Swift Judgement needs, was 0.15% slower on both seeds than Improved Hammer of Justice. Each such
        # point (its last rank) moved to any talent legal along the order, raced as in step 3, kept when faster on both seeds (the
        # tie-break rule; no "no loss" move here: a gate point's own value is unknown).
        # 5b (2026-11-21): a gate point that does nothing is measured as what it is (its last rank's removal, the plain time with the
        # build as given, at every race level it is held) and, as a tier point, moves at no loss into a legal talent that does something
        # (see the docstring); the record keeps every gate's kind, the homes tried and the verdict.
        trees_cls = VB.load_forever()[cls]
        book = LG.book(cls)
        for _ in range(a.max_moves if (a.gates or a.dead_gates) else 0):
            base = per_level(pool, cls, rot, space, [pts], LEVELS, a.fights, 3)[0]
            w0 = FL.weighted_at(base, LEVELS)
            left = {m["from"] for m in rec["moves"]}
            filled = {m["to"] for m in rec["moves"]}
            gates = []
            for n in sorted(flat_of(pts)):
                if n in keep:
                    continue
                i = max(k for k, (_, x) in enumerate(pts) if x == n)
                if n not in filled and not FL.legal_order(space, pts[:i] + pts[i + 1:], total - 1):
                    gates.append((n, i))
            bb = {"allocation": FL.alloc_of(space, flat_of(pts)), "order": FL.compress(pts)}
            st = {t: {x: r for x, r in v if r} for t, v in bb["allocation"].items()}
            dead_g, used, dead5, used_at5 = {}, set(), {}, {}
            if a.dead_gates and gates:
                used_l5 = pool.map(_casts, [(cls, rot, FL.FR.allocation_at(bb, L), L, a.fights, 3) for L in LEVELS], chunksize=1)
                used_at5, used = dict(zip(LEVELS, used_l5)), set().union(*used_l5)
                dead5 = dead_talents(cls, used)

                def less_of(al, n):
                    x = dict(al)
                    x[n] = x.get(n, 0) - 1
                    if x[n] <= 0:
                        x.pop(n)
                    return x
                # worth nothing, as the play check's Lc: at 60 first, then at every lower race level it is held (the plain time: no
                # signature penalty, the build as given; a talent ability the module plays without a cast, Cold Snap, measures here)
                a60 = FL.FR.allocation_at(bb, 60)
                rr = pool.map(FO._ttk, [(cls, rot, a60, 60, a.fights, LC_SEED, False)]
                              + [(cls, rot, less_of(a60, n), 60, a.fights, LC_SEED, False) for n, _ in gates], chunksize=1)
                nil60 = {n for (n, _), r in zip(gates, rr[1:]) if abs(r[0] - rr[0][0]) < 0.005}
                lower = [(n, L) for n, i in gates if n in nil60 for L in LC_LEVELS if 10 + i <= L < 60]
                lv_need = sorted({L for _, L in lower})
                rl = pool.map(FO._ttk, [(cls, rot, FL.FR.allocation_at(bb, L), L, a.fights, LC_SEED, False) for L in lv_need]
                              + [(cls, rot, less_of(FL.FR.allocation_at(bb, L), n), L, a.fights, LC_SEED, False) for n, L in lower],
                              chunksize=1) if lower else []
                b0 = {L: rl[k][0] for k, L in enumerate(lv_need)}
                fails = {n for k, (n, L) in enumerate(lower) if abs(rl[len(lv_need) + k][0] - b0[L]) >= 0.005}
                for n, i in gates:
                    if n not in nil60 or n in fails:
                        continue
                    lv_txt = ", ".join(map(str, sorted([L for m, L in lower if m == n] + [60])))
                    if n in book and n not in used:
                        dead_g[n] = f"a talent ability the build never presses (its removal changes nothing at {lv_txt})"
                    elif n in dead_from_levels(cls, used_at5, 10 + i):   # (2026-11-22: at the levels it holds the point)
                        dead_g[n] = (f"improves only {', '.join(dead_from_levels(cls, used_at5, 10 + i)[n])}, which the build never casts from "
                                     f"level {10 + i} on (its removal changes nothing at {lv_txt})")
                    else:
                        dead_g[n] = f"worth nothing: its last rank's removal leaves the time per kill the same to 0.01 s at {lv_txt}"
            plain = a.gates   # the plain gate moves (faster on both seeds); --dead-only and --dead-gates-only look at 5b's gates alone
            gates = [(n, i) for n, i in gates if plain or n in dead_g]
            cand = []
            for n, i in gates:
                for tname in space.tree_names:
                    for d in space.by_tree[tname]:
                        if d == n or d in left or (n in unseen and not (unseen_kinds(cls, d) & unseen[n])):
                            continue
                        new = pts[:i] + [(tname, d)] + pts[i + 1:]
                        if FL.legal_order(space, new, total):
                            cand.append((n, d, i, new))
            print(f"  gates: {', '.join(n + (' (does nothing)' if n in dead_g else '') for n, _ in gates) or 'none'}; {len(cand)} legal moves", flush=True)
            scored = []
            for i in sorted({c[2] for c in cand}):
                group = [c for c in cand if c[2] == i]
                lv = [L for L in LEVELS if L >= 10 + i] or [60]
                for (n, d, _, new), res in zip(group, per_level(pool, cls, rot, space, [c[3] for c in group], lv, a.fights, 3)):
                    scored.append((FL.weighted_at({**base, **res}, LEVELS), n, d, i, new, all(res[L] == base[L] for L in res)))
            scored.sort(key=lambda s: s[0])
            for n, i in gates:
                gates_checked[n] = {"level": 10 + i, "kind": GK.gate_kind(trees_cls, st, n, 1)
                                    or "order point (the finished build is legal without it; a later point of the order comes a level too soon)",
                                    "does_nothing": dead_g.get(n),
                                    "homes": [{"to": d, "seed3": round(w1 / w0 - 1, 4), **({"same_times": True} if same_t else {})}
                                              for w1, nn, d, _, _, same_t in scored if nn == n]}
            if not cand:
                for n, _ in gates:
                    gates_checked[n]["verdict"] = "no legal home"
                    if n in dead_g:
                        no_home[n] = {"kind": gates_checked[n]["kind"], "exact": True, "why": dead_g[n], "homes": 0}
                break
            best, why = None, "gate"
            if plain:
                # a gate point's measured move reverses no move in the chain unless it clears the bar on both seeds (2026-11-22, the audit
                # session: Arcane's level-10 point had gone back from Wand Specialization at -0.36% / -0.23%; this path never read the chain)
                back = chain | {(m["from"], m["to"]) for m in rec["moves"]}
                for w1, n, d, i, new, _ in [s for s in scored if s[0] < w0 * (1 - 0.0005)
                                            and ((s[2], s[1]) not in back or s[0] <= w0 * (1 - a.bar))][:4]:
                    b2, n2 = per_level(pool, cls, rot, space, [pts, new], LEVELS, a.fights, 4)
                    g2 = FL.weighted_at(n2, LEVELS) / FL.weighted_at(b2, LEVELS) - 1
                    if (d, n) in back and g2 > -a.bar:
                        continue
                    if g2 < -0.0005 and (best is None or (w1 / w0 - 1) + g2 < (best[0] / w0 - 1) + best[5]):
                        best = (w1, n, d, i, new, g2)
            use = UT.usefulness(cls, True)   # leveling: the character is hit, survival first
            base4 = None
            if not best and dead_g:
                why = "gate that did nothing, no loss"
                # by measured time, then by the leveling utility kinds (the audit session's "more useful"): a tie never takes a point
                # from a talent with a utility tag the lab does not measure (range, an interrupt) to one lower in the utility order
                back = chain | {(m["from"], m["to"]) for m in rec["moves"]}
                home_ok = lambda d, i: ((d not in book or d in used or lives(cls, d)) and d not in dead_from_levels(cls, used_at5, 10 + i)   # noqa: E731
                                        and d not in dead_g)   # (2026-11-22: a home dead at the levels the point is held is no home)
                picks = [s for s in scored if s[1] in dead_g and s[0] <= w0 * (1 + NO_LOSS) and not s[5] and home_ok(s[2], s[3])
                         and lev_rank(cls, s[2], use) <= lev_rank(cls, s[1], use) and (s[2], s[1]) not in back][:4]
                if picks:   # seed 4 at the levels a move changes (the levels before it are the build's own)
                    base4 = per_level(pool, cls, rot, space, [pts], LEVELS, a.fights, 4)[0]
                    for i in sorted({s[3] for s in picks}):
                        group = [s for s in picks if s[3] == i]
                        lv = [L for L in LEVELS if L >= 10 + i] or [60]
                        for (w1, n, d, _, new, _), r4 in zip(group, per_level(pool, cls, rot, space, [s[4] for s in group], lv, a.fights, 4)):
                            g2 = FL.weighted_at({**base4, **r4}, LEVELS) / FL.weighted_at(base4, LEVELS) - 1
                            same4 = all(r4[L] == base4[L] for L in r4)
                            for h in gates_checked[n]["homes"]:
                                if h["to"] == d:
                                    h["seed4"] = round(g2, 4)
                                    if same4:
                                        h["same_times_seed4"] = True
                            print(f"    5b {n} -> {d}: seed 3 {w1 / w0 - 1:+.2%}, seed 4 {g2:+.2%}" + (" (the same times)" if same4 else ""), flush=True)
                            if g2 <= NO_LOSS and not same4 and (best is None or (w1 / w0 - 1) + g2 < (best[0] / w0 - 1) + best[5]):
                                best = (w1, n, d, i, new, g2)
            if not best and dead_g:
                # 2026-11-21 (the audit session's second refinement): at bit-identical times a talent ability the build never presses, or a
                # talent dead by its tooltip, goes to the legal home highest in the leveling utility order (survival, then pushback,
                # threat, mana, range), a home that is neither a talent ability nor dead by its tooltip and stands higher than the point's
                # own talent. The page would otherwise show a spell the player is told never to press (Frost's Arcane Blast) where a
                # home that helps exists. A point the lab measures as nothing for another reason (Winter's Chill, its spell vetoed;
                # Frostbite, Fingers of Frost's roll; Missile Barrage, never procced in Frost's own rotation) keeps "no better home".
                back = chain | {(m["from"], m["to"]) for m in rec["moves"]}
                home_ok = lambda d, i: ((d not in book or d in used or lives(cls, d)) and d not in dead_from_levels(cls, used_at5, 10 + i)   # noqa: E731
                                        and d not in dead_g)   # (2026-11-22: a home dead at the levels the point is held is no home)
                tie = sorted([s for s in scored if s[1] in dead_g and s[5] and (dead_g[s[1]].startswith("a talent ability") or s[1] in dead_from_levels(cls, used_at5, 10 + s[3]))
                              and home_ok(s[2], s[3]) and lev_rank(cls, s[2], use) < min(UT.NONE, lev_rank(cls, s[1], use))
                              and (s[2], s[1]) not in back],
                             key=lambda s: (lev_rank(cls, s[2], use), s[0]))
                for w1, n, d, i, new, _ in tie[:3]:   # confirmed bit for bit the same on seed 4 too, else it is a measured move
                    if base4 is None:
                        base4 = per_level(pool, cls, rot, space, [pts], LEVELS, a.fights, 4)[0]
                    lv = [L for L in LEVELS if L >= 10 + i] or [60]
                    r4 = per_level(pool, cls, rot, space, [new], lv, a.fights, 4)[0]
                    if all(r4[L] == base4[L] for L in r4):
                        tag = ["survival"] + [t for t, _ in UT.TAGS if t != "survival"]
                        best, why = (w1, n, d, i, new, 0.0), f"gate that did nothing, tie-break by utility ({tag[lev_rank(cls, d, use)]})"
                        for h in gates_checked[n]["homes"]:
                            if h["to"] == d:
                                h["seed4"] = 0.0
                                h["same_times_seed4"] = True
                        break
            if not best:
                for n, _ in gates:
                    gates_checked[n]["verdict"] = (("no better home" if gates_checked[n]["homes"] else "no legal home") if n in dead_g
                                                   else "kept: no home faster on both seeds")
                    if n in dead_g:
                        no_home[n] = {"kind": gates_checked[n]["kind"], "exact": True, "why": dead_g[n], "homes": len(gates_checked[n]["homes"])}
                print(f"  gates: best move {scored[0][1]} -> {scored[0][2]}: {w0:.2f} -> {scored[0][0]:.2f} s, not faster on both seeds"
                      + (f"; no legal home that does something at no loss for {', '.join(sorted(dead_g))}" if dead_g else ""), flush=True)
                break
            w1, n, d, i, new, g2 = best
            print(f"  {why} {n} (level {10 + i}) -> {d}: {w0:.2f} -> {w1:.2f} s; seed 4 {g2:+.2%}", flush=True)
            rec["moves"].append({"from": n, "to": d, "level": 10 + i, "seed3": round(w1 / w0 - 1, 4), "seed4": round(g2, 4), "why": why})
            gates_checked[n]["verdict"] = f"moved to {d}"
            no_home.pop(n, None)
            pts = new
    trees_cls = VB.load_forever()[cls]
    st_end = {t: {x: r for x, r in v if r} for t, v in FL.alloc_of(space, flat_of(pts)).items()}
    left_all = {m["from"] for m in rec["moves"]}
    for n, k in sorted(unseen.items()):
        if n in flat_of(pts) and n not in left_all:
            no_home.pop(n, None)
            gates_checked[n] = {"kind": GK.gate_kind(trees_cls, st_end, n) or "not a gate", "does_nothing": None, "homes": [],
                                "verdict": f"kept: utility ({', '.join(sorted(k))}), a value the fight lab cannot see"}
    if gates_checked:
        rec["gates_checked"] = gates_checked
    rec["no_better_home"] = no_home
    OUT.mkdir(exist_ok=True)
    slug = a.spec.lower().replace("/", "-").replace(" ", "-")
    rec["final_order"] = FL.compress(pts)
    out = OUT / f"{cls}-{slug}.json"
    prev = json.load(open(out, encoding="utf-8")) if out.exists() else None
    # 2026-11-09: a dry run after a written pass must not replace its record: open_builds.py re-applies the pass from that record's
    # "written" and "start_order" (a dry run starts from the moved build and has neither), so the dry run gets a file of its own.
    # 2026-11-21: nor any other record (the leveling play check reads both files, the one made on the build as it stands)
    if not a.write and out.exists():
        out = OUT / f"{cls}-{slug}.dry.json"
    if a.from_dry:
        out = OUT / f"{cls}-{slug}.dry2.json"
    moved = bool(rec["moves"])
    if prev:   # the history of a record (undone moves, earlier no-move runs) stays with it (2026-11-21)
        for k in ("undone", "reruns"):
            if prev.get(k) and k not in rec:
                rec[k] = prev[k]
    if a.dead_gates_only and prev and prev.get("steps"):   # the last full pass's removal values stay with the record (2026-11-21)
        rec["steps"] = prev["steps"]
    # 2026-11-21: a written run that moves nothing keeps the pass it found applied (start_order, moves and written, which open_builds.py
    # re-applies a pass from): the lane of 2026-11-20 had dropped them from four records whose builds still carried the moves
    if a.write and not moved and prev and prev.get("written") and prev["written"].get("order") == rec["start_order"]:
        rec["start_order"], rec["moves"], rec["written"] = prev.get("start_order", rec["start_order"]), prev.get("moves", []), prev["written"]
        rec["reruns"] = (prev.get("reruns") or []) + [{"date": rec["date"], "moves": 0}]
    out.write_text(json.dumps(rec, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"record {out.name}")
    print(json.dumps(rec["moves"], indent=1))
    if a.write and moved:
        path = ROOT / cls / "research/talents/forever/proposed-builds.json"
        data = json.load(open(path, encoding="utf-8"))
        bb = next(x for x in data["builds"] if x["id"] == b["id"])
        bb["allocation"] = FL.alloc_of(space, flat_of(pts))
        bb["order"] = FL.compress(pts)
        text = "; ".join(f"{m['from']} to {m['to']} at {m['level']} ({m['why']}: {m['seed3']:+.1%} seed 3, {m['seed4']:+.1%} seed 4, level-weighted time per kill)"
                         for m in rec["moves"])
        bb.setdefault("notes", []).insert(0, f"{rec['date']}: leveling filler pass (fightlab/fl_filler_pass.py, {a.fights} fights a level): points that "
                                             f"measured nothing, or held a tier open, moved: {text}.")
        # formatted as fmt_json.py does (talent pairs on one line) and written whole or not at all (2026-11-22: a running tail's
        # validate_builds.py reads without the lock; the old write and the fmt_json.py pass were two in-place writes)
        import builds_io as _BIO
        from fmt_json import dumps as _fmt_dumps
        _BIO._write_atomic(path, _fmt_dumps(data) + "\n")
        print(f"wrote {path}")
        # open_builds.py rewrites an -open-leveling build from its search record on every run: it re-applies a written pass whose
        # start_order is still the record's order (2026-11-09), from these two fields
        rec["written"] = {"allocation": bb["allocation"], "order": bb["order"], "note": bb["notes"][0]}
        # a second write on a build that still carries the previous written pass (2026-11-09): chain onto that record, so its
        # start_order stays the search record's order open_builds.py compares, and its moves and note stay with this one
        if prev and prev.get("written") and prev["written"].get("order") == rec["start_order"]:
            rec["start_order"] = prev.get("start_order", rec["start_order"])
            rec["moves"] = prev.get("moves", []) + rec["moves"]
            rec["written"]["note"] += " Earlier: " + prev["written"]["note"]
        (OUT / f"{cls}-{slug}.json").write_text(json.dumps(rec, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
