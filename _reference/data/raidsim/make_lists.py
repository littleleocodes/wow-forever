"""The gear lists for every raid damage spec, made in the order the audit session agreed (2026-11-23): the one place that order lives.

    python -u _reference/data/raidsim/make_lists.py [classes] [--spec "<spec>" ...] [--phases lists,nopvp,sides] [--dry-run] [--fresh]

Each phase runs over every spec before the next one starts (the user's order if time runs short: the three lists, then the lists without
PvP, then the faction sets):
1. lists: Easy Pre-BiS (dungeon_tier.py --fresh), then True Pre-BiS and True BiS (pick_tiers.py --make): the ladder from the bottom,
   each list's make racing the set of the list below it (gear_tiers.make);
2. nopvp: True Pre-BiS, then True BiS, without what only PvP puts in the list (gear_tiers.make nopvp; the no-PvP Pre-BiS set is the BiS
   make's lower rung);
3. sides (see below), then 4. tanks-healers: tank_gear.py and heal_gear.py --fresh (True Pre-BiS and True BiS; what they lack of
   today's rules is in the phase's comment and on their pages). The sides: each list's Alliance and Horde sets (gear_tiers.make side=, the list's full set slot by slot a known positive), made only where
   the list's set holds a one-faction item (skipped, and said, otherwise); then the side feedback, from the bottom list up: the full
   set races its side sets on seeds 1 and 2 (the confirm's fights) and takes a side set that beats it on both (ties stay); a higher
   list's set then races the changed lower set the same way (the ladder). The cause it covers: the weapon passes depend on their order
   (main hand, off hand, ranged, main hand again), and a side's make, whose pool lacks the other side's items, can reach a better set
   (Survival's True Pre-BiS, 2026-11-23: both side sets 1001.8 / 1001.6 against the full set's 998.9 / 999.1). A spec whose full set
   changed has its pick raced again in its sets (pick_tiers.py without --make), for the pages' numbers.
Records: each spec's ML record (raidsim/ml/<class>-<spec slug>.json) gains gear["<tier>-nopvp"], gear["<tier>-alliance"],
gear["<tier>-horde"] and `lists` {rules, made, skipped, side_feedback}. Progress: deep-runs/make-lists-state.json (resumable; a later
phase of a spec is stale when an earlier phase of that spec ran after it; --fresh redoes). --dry-run prints the plan, each step's state
and the makes per spec, and touches nothing. The budgets are gear_tiers.args_ns's (WOW_FOREVER_GEAR_BUDGET selects a set of them).
"""
import argparse
import datetime
import json
import os
import pathlib
import subprocess
import sys
import time

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[2]
sys.path[:0] = [str(HERE), str(HERE.parent)]
import gear_tiers as GT  # noqa: E402
import gear_lists as GL  # noqa: E402

G, R = GT.G, GT.R
ML = HERE / "ml"
STATE = HERE.parent / "deep-runs" / "make-lists-state.json"
LISTS = ("dungeon", "prebis", "bis")
SIDES = ("Alliance", "Horde")
KEEP = ("list", "rules", "entry", "gear", "date", "setting", "chosen", "ilvl", "trinkets", "names", "race_seed1", "confirm_seed2", "weights",
        "weapons", "set_pieces", "enchants", "kinds", "marks", "faction_alternatives", "pvp_alternatives", "currency_cost") + GT.LIST_RECORD_FIELDS
MINUTES = {"hunter": 3.3, "rogue": 2.0, "warrior": 2.0, "shaman": 1.5, "paladin": 1.5, "druid": 1.2, "mage": 0.7, "warlock": 0.7, "priest": 0.7}
# minutes a make at the tests' budgets (the list tests, 2026-11-23, 10 threads beside an Idle lane), scaled to the budget in use: the
# default budgets measured 2.4-2.7x (Survival 6.9 min against 2.6, Frost 1.2 against 0.5); first-pass doubles the confirm only
SCALE = {"tests": 1.0, "first-pass": 1.2, "default": 2.6}
BUDGET = os.environ.get("WOW_FOREVER_GEAR_BUDGET", "default")
FEEDBACK_BAR = 0.001   # a side set replaces the full set only when this far ahead on both seeds (the audit session: 0.05% at 6,000 is noise)


def page_picks(classes):
    """{(class, spec): (build id, entry)}: each raid page's damage pick as the pages show it (render_modes.rank_builds through
    page_stat_weights.py --list, in its own process: the page code and the simulator share the module name `run`)."""
    cls = classes or "druid hunter mage paladin priest rogue shaman warlock warrior".split()
    r = subprocess.run([sys.executable, str(HERE / "page_stat_weights.py"), "--list", *cls], capture_output=True, text=True, cwd=str(ROOT))
    if r.returncode:
        raise SystemExit(f"make_lists: the page picks could not be read: {r.stderr[-800:]}")
    return {(c, s): (b["id"], e) for c, rows in json.loads(r.stdout).items() for s, b, e in rows}


def specs(classes, only):
    """Each damage spec's lists are made for the build and entry its raid page shows (2026-11-23, the audit session: on 2026-11-19 an ML
    record's `best` had not been the page's pick for 17 specs, the bug behind GearCheck's raid values; a re-pin can move picks). A record
    whose best differs is made for the page's pick and says so; a page spec with no record gets one (pick_tiers.py writes it)."""
    picks = page_picks(classes)
    out, seen = [], set()
    for f in sorted(ML.glob("*.json")):
        if f.stem in ("rotations", "spell-probe"):
            continue
        d = json.load(open(f, encoding="utf-8"))
        if not d.get("class") or (classes and d["class"] not in classes) or (only and d["spec"] not in only):
            continue
        pk = picks.get((d["class"], d["spec"]))
        seen.add((d["class"], d["spec"]))
        build, entry = pk if pk else (d["best"], d["best_entry"])
        out.append({"cls": d["class"], "spec": d["spec"], "entry": entry, "build": build, "record": f, "record_best": (d["best"], d["best_entry"]),
                    "page": bool(pk), "mismatch": bool(pk) and (pk[0], pk[1]) != (d["best"], d["best_entry"])})
    for (c, s), (build, entry) in sorted(picks.items()):
        if (c, s) not in seen and (not only or s in only):
            out.append({"cls": c, "spec": s, "entry": entry, "build": build, "record": ML / f"{c}-{GT.SM.slug(s)}.json",
                        "record_best": None, "page": True, "mismatch": True})
    return out


def load_state():
    return json.load(open(STATE, encoding="utf-8")) if STATE.exists() else {}


def save_state(st):
    STATE.parent.mkdir(parents=True, exist_ok=True)
    STATE.write_text(json.dumps(st, indent=1) + "\n", encoding="utf-8")


def key(s, step):
    return f"{s['cls']}|{s['spec']}|{step}"


PHASE_STEPS = {"lists": ["easy", "true"], "nopvp": ["nopvp"], "sides": ["sides"]}
ORDER = ["easy", "true", "nopvp", "sides", "tanks", "healers", "check"]


def done(st, s, step, fresh):
    """A step is done when its state says so under the current rules, and no earlier step of the spec ran after it."""
    if fresh:
        return False
    x = st.get(key(s, step))
    if not x or x.get("rules") != GL.RULES:
        return False
    for earlier in ORDER[:ORDER.index(step)]:
        y = st.get(key(s, earlier))
        if y and y.get("at", "") > x.get("at", ""):
            return False
    return True


def mark(st, s, step, **kw):
    st[key(s, step)] = {"at": datetime.datetime.now().isoformat(timespec="seconds"), "rules": GL.RULES, **kw}
    save_state(st)


def run(cmd, log):
    print(f"  $ {' '.join(cmd)}", flush=True)
    r = subprocess.run([sys.executable, "-u"] + cmd, cwd=str(ROOT))
    if r.returncode:
        raise SystemExit(f"make_lists: {log} failed (exit {r.returncode})")


def one_faction(items, db, ctx):
    return [(i, db[x["id"]]["name"], GL.faction_of(db[x["id"]], ctx)) for i, x in enumerate(GT.norm17(items))
            if x.get("id") in db and GL.faction_of(db[x["id"]], ctx)]


def set_items(p):
    return json.load(open(p, encoding="utf-8"))["items"] if p.exists() else None


def update_record(s, fn):
    rec = json.load(open(s["record"], encoding="utf-8"))
    fn(rec)
    s["record"].write_text(json.dumps(rec, indent=1) + "\n", encoding="utf-8")


def plan(sp, st, fresh, phases, db, ctx):
    total, mins = 0, 0.0
    for s in sp:
        lines, n = [], 0
        if "lists" in phases:
            for step, what in (("easy", "Easy Pre-BiS (dungeon_tier.py --fresh)"), ("true", "True Pre-BiS, then True BiS (pick_tiers.py --make)")):
                lines.append(f"    {'done' if done(st, s, step, fresh) else 'to do'}: {what}")
                n += 0 if done(st, s, step, fresh) else (1 if step == "easy" else 2)
        if "nopvp" in phases:
            d = done(st, s, "nopvp", fresh)
            lines.append(f"    {'done' if d else 'to do'}: True Pre-BiS and True BiS without PvP")
            n += 0 if d else 2
        if "sides" in phases:
            d = done(st, s, "sides", fresh)
            for tier in LISTS:
                its = set_items(GT.set_path(s["cls"], s["spec"], tier))
                of = one_faction(its, db, ctx) if its else []
                cond = (f"the current file holds {len(of)} one-faction items ({', '.join(n_ for _, n_, _ in of[:3])})" if of
                        else ("the current file holds none" if its else "no file yet"))
                lines.append(f"    {'done' if d else 'to do'}: {GL.LABEL[tier]} Alliance and Horde if the new set holds a one-faction item "
                             f"({cond})")
                n += 0 if d else (2 if of or not its else 0)
            lines.append(f"    {'done' if d else 'to do'}: the side feedback, from Easy up (one race per list with sides)")
        total += n
        mins += n * MINUTES.get(s["cls"], 2.0) * SCALE.get(BUDGET, 1.0)
        rb = s.get("record_best")
        print(f"  {s['cls']} {s['spec']}: record best {rb[0] + ' / ' + rb[1] if rb else 'none'} | page pick {s['build']} / {s['entry']}"
              + (" | MISMATCH: made for the page's pick" if s.get("mismatch") else "") + f" | about {n} makes, about "
              f"{n * MINUTES.get(s['cls'], 2.0) * SCALE.get(BUDGET, 1.0):.0f} min at the {BUDGET} budgets", flush=True)
        for ln in lines:
            print(ln, flush=True)
    print(f"== {len(sp)} specs, about {total} makes, about {mins / 60:.1f} h of makes at the {BUDGET} budgets (12 threads, the machine "
          f"to itself); besides: pick_tiers' and dungeon_tier's races about 2.5 h, the side feedback's races about 1 h, tanks and healers "
          f"about 4-6 h, step 4 about 1-2 h", flush=True)


def talents_of(s, repo):
    trees = R.load_trees(repo, s["cls"])
    b = {x["id"]: x for x in json.load(open(ROOT / s["cls"] / "research/talents/forever/proposed-builds.json", encoding="utf-8"))["builds"]}[s["build"]]
    return R.talents_string(trees, R.alloc_of(b))


def keep(r):
    return {k: r[k] for k in KEEP if k in r}


def nopvp(s, repo, db, zones, a, st):
    tal = talents_of(s, repo)
    made = {}
    for tier in ("prebis", "bis"):
        t0 = time.time()
        r = GT.make(s["cls"], s["spec"], tier, s["entry"], tal, s["build"], repo, db, zones, a, nopvp=True)
        made[f"{tier}-nopvp"] = dict(keep(r), minutes=round((time.time() - t0) / 60, 1))
        print(f"  {s['cls']} {s['spec']} {GL.LABEL[tier]} without PvP: {r.get('chosen')} ({r.get('chosen_source')}), "
              f"{made[f'{tier}-nopvp']['minutes']} min", flush=True)
    update_record(s, lambda rec: (rec["gear"].update(made), rec.setdefault("lists", {}).update(rules=GL.RULES)))
    mark(st, s, "nopvp")


def sides(s, repo, db, zones, ctx, a, st):
    tal = talents_of(s, repo)
    entry = R.SPECS[s["cls"]][s["entry"]]
    made, skipped, feedback = {}, {}, {}
    for tier in LISTS:
        p = GT.set_path(s["cls"], s["spec"], tier)
        full = set_items(p)
        if not full:
            skipped[tier] = "no set file"
            continue
        of = one_faction(full, db, ctx)
        if not of:
            skipped[tier] = "the set holds no one-faction item: one set serves both sides"
            print(f"  {s['cls']} {s['spec']} {GL.LABEL[tier]}: no one-faction item, no side sets", flush=True)
            continue
        for side in SIDES:
            t0 = time.time()
            r = GT.make(s["cls"], s["spec"], tier, s["entry"], tal, s["build"], repo, db, zones, a, side=side, full_set=full)
            made[f"{tier}-{side.lower()}"] = dict(keep(r), minutes=round((time.time() - t0) / 60, 1))
            print(f"  {s['cls']} {s['spec']} {GL.LABEL[tier]} {side}: {r.get('chosen')} ({r.get('chosen_source')}), "
                  f"{made[f'{tier}-{side.lower()}']['minutes']} min", flush=True)
    # the side feedback, from the bottom list up
    changed = False
    lower_changed = None
    took = {}
    for tier in LISTS:
        p = GT.set_path(s["cls"], s["spec"], tier)
        full = set_items(p)
        if not full:
            continue
        rivals = {}
        for side in SIDES:
            sp_ = GT.set_path(s["cls"], s["spec"], tier, side=side)
            if f"{tier}-{side.lower()}" in made and sp_.exists():
                rivals[f"the {side} set"] = set_items(sp_)
        if lower_changed:   # the ladder: a changed lower set races this list's set too
            rivals[f"the {GL.LABEL[lower_changed[0]]} set (changed)"] = lower_changed[1]
        if not rivals:
            continue
        sets = {"full": full, **rivals}
        res = {}
        for seed in (1, 2):
            rows = G.run_bench(repo, G.bench_cfg(entry, repo, [{"label": k, "talents": tal, "gear_json": {"items": v}} for k, v in sets.items()],
                                                 a.confirm, seed, "raid"), f"sidefb-{s['cls']}-{GT.SM.slug(s['spec'])}-{tier}-{seed}")
            res[seed] = {k: round((rows.get(k) or {}).get("dps") or 0.0, 2) for k in sets}
        wins = [k for k in rivals if all(res[sd][k] > res[sd]["full"] * (1 + FEEDBACK_BAR) for sd in (1, 2))]
        best = max(wins, key=lambda k: res[1][k] + res[2][k]) if wins else None
        feedback[tier] = {"fights": a.confirm, "dps": res, "taken": best}
        if best:
            new = sets[best]
            bad = GT.list_guard(new, tier, db, zones, repo, cls=s["cls"])
            if bad:
                raise SystemExit(f"make_lists: {best} for {GL.LABEL[tier]} breaks the list's rule: " + "; ".join(bad))
            p.write_text(json.dumps({"items": new, "list": GL.LABEL.get(tier, tier), "rules": GL.RULES,
                                     "feedback": f"{best}, ahead of the list's own set on both seeds ({res[1][best]} / {res[2][best]} "
                                                 f"against {res[1]['full']} / {res[2]['full']}, {a.confirm} fights)"}, indent=1) + "\n",
                         encoding="utf-8")
            changed, lower_changed = True, (tier, new)
            took[tier] = (best, new, {"fights": a.confirm, "dps": {sd: {"full": res[sd]["full"], best: res[sd][best]} for sd in (1, 2)}})
            print(f"  {s['cls']} {s['spec']} {GL.LABEL[tier]}: takes {best} ({res[1][best]} / {res[2][best]} against "
                  f"{res[1]['full']} / {res[2]['full']})", flush=True)
        else:
            lower_changed = None
    def rewrite(rec):
        # after a take the record describes the set in the file (the audit session: pages and gear_links read records); the set before
        # the feedback stays under before_feedback; gear_check checks every list's record against its file
        for tier, (best, new, race) in took.items():
            g = rec["gear"].get(tier) or {}
            pool = GT.pool_of(tier, zones, repo)
            lf = GT.list_fields(s["cls"], new, g.get("weights") or {}, tier, db, zones, repo, pool)
            rec["gear"][tier] = dict({k: v for k, v in g.items() if k not in ("before_feedback",)}, **lf,
                                     names=[db.get(x.get("id"), {}).get("name") if x and x.get("id") else None for x in GT.norm17(new)],
                                     chosen=f"the side feedback: {best}", chosen_source=f"the side feedback: {best}", side_feedback=race,
                                     before_feedback={k: g.get(k) for k in ("chosen", "chosen_source", "names", "ilvl") if k in g})
    update_record(s, lambda rec: (rewrite(rec), rec["gear"].update(made), rec.setdefault("lists", {}).update(
        rules=GL.RULES, skipped=skipped, side_feedback=feedback,
        feedback_cause="the weapon passes depend on their order (main hand, off hand, ranged, main hand again), and a side's make can "
                       "reach a better set than the full list's")))
    if changed:
        run([str(HERE / "pick_tiers.py"), s["cls"], s["spec"], "--entry", s["entry"], "--build", s["build"]], f"{s['spec']}'s race")
    mark(st, s, "sides", changed=changed)


PHASE_KEYS = {"lists": ("dungeon", "prebis", "bis"), "nopvp": ("prebis-nopvp", "bis-nopvp"),
              "sides": tuple(f"{t}-{s}" for t in LISTS for s in ("alliance", "horde"))}


def nopvp_factions(sp, st):
    """The no-PvP sets' one-faction items whose other-side alternative is not a stat twin (the audit session, 2026-11-23: a slot-by-slot
    alternative found by the weights is not a tested set); the count decides whether they get side makes in the second pass."""
    rows = []
    for s in sp:
        rec = json.load(open(s["record"], encoding="utf-8"))
        for k in ("prebis-nopvp", "bis-nopvp"):
            for x in ((rec.get("gear") or {}).get(k) or {}).get("faction_alternatives") or []:
                twin = x.get("alternative") and x.get("value") is not None and abs((x.get("alternative_value") or 0) - x["value"]) < 0.01
                if not twin:   # a stat twin (same stats, so the same value by the weights) is the same set on the other side
                    rows.append({"class": s["cls"], "spec": s["spec"], "list": k, "slot": x.get("slot"), "item": x.get("name"),
                                 "for": x.get("for"), "alternative": x.get("alternative_name"), "how": x.get("how")})
    st["nopvp-factions"] = {"at": datetime.datetime.now().isoformat(timespec="seconds"), "rules": GL.RULES, "rows": rows}
    save_state(st)
    print(f"== no-PvP sets' one-faction items with no stat twin on the other side: {len(rows)}" + "".join(
        f"\n   {r['class']} {r['spec']} {r['list']} slot {r['slot']}: {r['item']} -> {r['for']}: {r['alternative']} ({r['how']})" for r in rows),
        flush=True)
    return rows


PREV_DIR = HERE.parent / "deep-runs" / "lists-prev"
CHECK_ITERS, MISS = 10000, 0.005   # pick_tiers' fights; a shown set this far behind a challenger on both seeds is a miss


def page_files():
    """{path}: every set file a record the pages read names (the ML records' gear entries, the tanks' and healers' records)."""
    out = set()

    def walk(x):
        if isinstance(x, dict):
            for k, v in x.items():
                if k == "gear" and isinstance(v, str) and v.endswith(".gear.json"):
                    out.add((ROOT / v).resolve())
                else:
                    walk(v)
        elif isinstance(x, list):
            for v in x:
                walk(v)
    for f in list(ML.glob("*.json")) + [HERE / "tank-gear.json", HERE.parent / "heallab" / "heal-gear.json"]:
        if f.exists():
            walk(json.load(open(f, encoding="utf-8")))
    return out


def snapshot(st):
    """The page files as they stand before the first make (once per run of the lists: kept across resumes), for the missed-set check."""
    if st.get("prev-snapshot", {}).get("rules") == GL.RULES and PREV_DIR.exists():
        return
    PREV_DIR.mkdir(parents=True, exist_ok=True)
    n = 0
    for p in page_files():
        if p.exists():
            (PREV_DIR / p.name).write_bytes(p.read_bytes())
            n += 1
    st["prev-snapshot"] = {"at": datetime.datetime.now().isoformat(timespec="seconds"), "rules": GL.RULES, "dir": str(PREV_DIR), "files": n}
    save_state(st)
    print(f"== snapshot: {n} page set files copied to {PREV_DIR} before the makes", flush=True)


def missed_sets(s, repo, db, zones, st):
    """Each of the spec's three lists against its best known positive (as its make raced it) and its previous set (the snapshot, when it
    passes the list's rule), on pick_tiers' fights: the page's pick, a full raid, 10,000 fights, seeds 1 and 2. A shown set 0.5% behind
    a challenger on both seeds is a miss: printed, kept in the record (gear[list].miss_check) and the state file."""
    tal = talents_of(s, repo)
    entry = R.SPECS[s["cls"]][s["entry"]]
    rec = json.load(open(s["record"], encoding="utf-8"))
    out, misses = {}, []
    for k in LISTS:
        g = (rec.get("gear") or {}).get(k) or {}
        if not g.get("gear") or not (ROOT / g["gear"]).exists():
            continue
        sets = {"shown": set_items(ROOT / g["gear"])}
        why = {}
        kps = [x for x in (g.get("known_positives") or []) if isinstance(x, dict) and x.get("items")]
        if kps:
            kb = max(kps, key=lambda x: (x.get("seed2") or 0.0, x.get("seed1") or 0.0))
            sets[f"known: {kb['name']}"] = kb["items"]
        else:
            why["known"] = "no known positive raced in the make"
        pp = PREV_DIR / pathlib.Path(g["gear"]).name
        if pp.exists():
            prev = set_items(pp)
            bad = GT.list_guard(GT.norm17(prev), k, db, zones, repo, cls=s["cls"])
            if bad:
                why["previous"] = "breaks the list's rule: " + "; ".join(bad)[:200]
            elif [x.get("id") for x in GT.norm17(prev)] != [x.get("id") for x in GT.norm17(sets["shown"])]:
                sets["previous"] = prev
            else:
                why["previous"] = "the same items as the shown set"
        else:
            why["previous"] = "no previous set"
        res = {}
        if len(sets) > 1:
            for seed in (1, 2):
                rows = G.run_bench(repo, G.bench_cfg(entry, repo, [{"label": x, "talents": tal, "gear_json": {"items": v}} for x, v in sets.items()],
                                                     CHECK_ITERS, seed, "raid"), f"missed-{s['cls']}-{GT.SM.slug(s['spec'])}-{k}-{seed}")
                res[seed] = {x: round((rows.get(x) or {}).get("dps") or 0.0, 1) for x in sets}
            for x in sets:
                if x != "shown" and all(res[sd][x] > res[sd]["shown"] * (1 + MISS) for sd in (1, 2)):
                    misses.append(f"{s['cls']} {s['spec']} {GL.LABEL[k]}: {x} ahead of the shown set, "
                                  + " / ".join(f"{res[sd][x]} against {res[sd]['shown']}" for sd in (1, 2)))
        out[k] = {"fights": CHECK_ITERS, "dps": res, "not_raced": why, "at": datetime.datetime.now().isoformat(timespec="seconds")}
    update_record(s, lambda r: [r["gear"][k].update(miss_check=v) for k, v in out.items()])
    mark(st, s, "check", misses=misses)
    for m in misses:
        print(f"  MISS {m}", flush=True)
    return misses


def close_calls(sp, phase, st, header=True):
    """The phase's close calls (the audit session's budget ruling, 2026-11-23): makes whose chosen set led the best set that lost on the
    confirm by less than gear_tiers.CLOSE_CALL with other items, neither a ladder tie nor a known-positive tie. They, and only they, are made
    again at the default budgets in the second pass. Printed at the end of the phase and kept in the state file."""
    rows, n = [], 0
    for s in sp:
        rec = json.load(open(s["record"], encoding="utf-8"))
        for k in PHASE_KEYS[phase]:
            g = (rec.get("gear") or {}).get(k)
            if not g:
                continue
            n += 1
            cm = g.get("confirm_margin") or {}
            if cm.get("close_call"):
                rows.append({"class": s["cls"], "spec": s["spec"], "list": k, "chosen": g.get("chosen"), "over": cm.get("over"),
                             "margin": cm.get("margin"), "budget": g.get("budget")})
    if not header:
        return rows
    st[f"close-calls|{phase}"] = {"at": datetime.datetime.now().isoformat(timespec="seconds"), "rules": GL.RULES, "makes": n, "rows": rows}
    save_state(st)
    print(f"== close calls after phase {phase}: {len(rows)} of {n} makes" + "".join(
        f"\n   {r['class']} {r['spec']} {r['list']}: {r['chosen']} over {r['over']} by {r['margin']:+.3%}" for r in rows), flush=True)
    warn = []
    for s in sp:   # the set-bonus check (gear_tiers.set_check): the simulator's sheet against the parser, per made set
        rec = json.load(open(s["record"], encoding="utf-8"))
        for k in PHASE_KEYS[phase]:
            sc = ((rec.get("gear") or {}).get(k) or {}).get("set_check") or {}
            if sc.get("warning"):
                warn.append(f"{s['cls']} {s['spec']} {k}: {sc['warning']}")
    st[f"set-check|{phase}"] = {"at": datetime.datetime.now().isoformat(timespec="seconds"), "rules": GL.RULES, "warnings": warn}
    save_state(st)
    print(f"== set-bonus check after phase {phase}: {len(warn)} warnings" + "".join(f"\n   {x}" for x in warn), flush=True)
    near = []
    for s in sp:   # unsimulated set bonuses (2026-11-23): the made sets one piece short of a plain-stat bonus the simulator lacks
        rec = json.load(open(s["record"], encoding="utf-8"))
        for k in PHASE_KEYS[phase]:
            for u in (((rec.get("gear") or {}).get(k) or {}).get("set_check") or {}).get("unsimulated") or []:
                for b in u.get("one_short") or []:
                    near.append(f"{s['cls']} {s['spec']} {k}: {u['set']} ({u['worn']} worn; {b['pieces']} pc: {b['text'][:90]})")
    st[f"one-short|{phase}"] = {"at": datetime.datetime.now().isoformat(timespec="seconds"), "rules": GL.RULES, "rows": near}
    save_state(st)
    print(f"== one piece short of an unsimulated plain-stat set bonus after phase {phase}: {len(near)}"
          + "".join(f"\n   {x}" for x in near), flush=True)
    return rows


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("classes", nargs="*")
    ap.add_argument("--spec", nargs="*", default=[])
    ap.add_argument("--phases", default="lists,nopvp,sides,tanks-healers,check")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--fresh", action="store_true")
    ap.add_argument("--exclude-fails", help="a play gate's play-fails.json (tonight_1123.sh): the specs whose raid page pick fails the play "
                                            "check are left out, the tanks among them too (2026-11-23, the audit session: their lists wait "
                                            "until the FAIL is fixed and read)")
    a0 = ap.parse_args()
    if os.environ.get("WOW_FOREVER_NO_RACIALS") != "1" and not a0.dry_run:   # (2026-11-23) the pages' numbers are made with racials off
        raise SystemExit("make_lists: STOP: WOW_FOREVER_NO_RACIALS is not 1 (the pages' numbers are made with racials off)")
    phases = [p for p in a0.phases.split(",") if p]
    R.set_game("forever")
    repo = R.repo_path(argparse.Namespace(repo=None))
    db, zones = GT.load_db(repo)
    ctx = GT.rules_ctx(zones, repo)
    sp = specs(a0.classes, a0.spec)
    left, tanks_left = set(), set()
    if a0.exclude_fails:
        fails = json.load(open(a0.exclude_fails, encoding="utf-8"))
        for x in fails.get("page_picks") or []:
            (tanks_left.add(x["class"]) if str(x.get("spec", "")).endswith("(tank)") else left.add((x["class"], x["spec"])))
        sp = [s for s in sp if (s["cls"], s["spec"]) not in left]
    print("== left out (raid page picks failing the play check): " + ("; ".join(f"{c} {s}" for c, s in sorted(left)) or "none")
          + ("; tanks: " + ", ".join(sorted(tanks_left)) if tanks_left else ""), flush=True)
    st = load_state()
    print(f"== make_lists: {len(sp)} specs, phases {phases}, rules {GL.RULES}, budgets {vars(GT.args_ns())}"
          + (f" ({os.environ.get('WOW_FOREVER_GEAR_BUDGET')})" if os.environ.get("WOW_FOREVER_GEAR_BUDGET") else ""), flush=True)
    if a0.dry_run:
        plan(sp, st, a0.fresh, phases, db, ctx)
        return
    norec = [f"{s['cls']} {s['spec']}" for s in sp if s.get("record_best") is None]
    if norec:   # dungeon_tier.py makes Easy Pre-BiS from a spec's ML record: a page spec without one stops the run (2026-11-23)
        raise SystemExit("make_lists: STOP: page specs with no ML record (run pick_tiers.py for them first): " + ", ".join(norec))
    a = GT.args_ns()
    if "lists" in phases:
        snapshot(st)
    for phase in ("lists", "nopvp", "sides", "tanks-healers", "check"):
        if phase not in phases:
            continue
        if phase == "check":
            print("== phase check: the shown sets against their best known positive and their previous set (pick_tiers' fights)", flush=True)
            allm = []
            for s in sp:
                if not done(st, s, "check", a0.fresh):
                    allm += missed_sets(s, repo, db, zones, st)
                else:
                    allm += (st.get(key(s, "check")) or {}).get("misses") or []
            st["missed-sets"] = {"at": datetime.datetime.now().isoformat(timespec="seconds"), "rules": GL.RULES, "misses": allm}
            save_state(st)
            print(f"== missed sets: {len(allm)}" + "".join(f"\n   {m}" for m in allm), flush=True)
            continue
        if phase == "tanks-healers":
            # the tanks' and healers' sets (2026-11-23): their own makers, Easy Pre-BiS, True Pre-BiS and True BiS in the list pools,
            # list_guard fatal before a set is written, each list taking the list below's set when its own ends below it; not yet
            # theirs: the no-PvP and side sets, the known positives and the hit report; set steps and REWEIGH neither for the healers
            # (the healer lab's own picker). Their pages say so until the second pass.
            th = {"cls": "tanks", "spec": "healers"}
            if not done(st, th, "tanks", a0.fresh):
                tank_classes = [c for c in ("warrior", "paladin", "druid") if c not in tanks_left]
                if tank_classes:   # (tank_gear.py with no class makes all three)
                    run([str(HERE / "tank_gear.py"), *tank_classes], "the tanks' sets")
                mark(st, th, "tanks", left_out=sorted(tanks_left))
            if not done(st, th, "healers", a0.fresh):
                run([str(HERE.parent / "heallab" / "heal_gear.py"), "--fresh"], "the healers' sets")
                mark(st, th, "healers")
            continue
        print(f"== phase {phase}", flush=True)
        close_calls(sp, phase, st, header=False)
        for s in sp:
            if phase == "lists":
                if not done(st, s, "easy", a0.fresh):
                    run([str(HERE / "dungeon_tier.py"), s["cls"], "--spec", s["spec"], "--fresh", "--build", s["build"], "--entry", s["entry"]],
                        f"{s['spec']}'s Easy Pre-BiS")
                    mark(st, s, "easy")
                if not done(st, s, "true", a0.fresh):
                    run([str(HERE / "pick_tiers.py"), s["cls"], s["spec"], "--entry", s["entry"], "--build", s["build"], "--make"],
                        f"{s['spec']}'s True lists")
                    mark(st, s, "true")
            elif phase == "nopvp" and not done(st, s, "nopvp", a0.fresh):
                nopvp(s, repo, db, zones, a, st)
            elif phase == "sides" and not done(st, s, "sides", a0.fresh):
                sides(s, repo, db, zones, ctx, a, st)
        close_calls(sp, phase, st)
        if phase == "nopvp":
            nopvp_factions(sp, st)
    print("== done", flush=True)


if __name__ == "__main__":
    main()
