"""Open talent search: every legal build, no tree rule, in every damage rotation of a class (2026-10-04, user request: "Hybrid builds
across the classes might be the best performing specs ... theoretically each spec could be 17/17/17 ... we need to possibly do a ranking
of each specific talent and its weight and how much it brings to each build ... that also requires looking at different rotations").

    python -u _reference/data/raidsim/family_search.py <class> [--entry <entry>] [--fresh] [--smoke]
    python -u _reference/data/raidsim/family_search.py --report          # the cross-class page only

Why: every other search keeps a spec's tree rule (30+ points in the tree, or a named hybrid's two largest trees), so a build outside
every family is never tried, however long a search runs (2026-10-03: the 16/11/24 Summon Hawk + Lone Wolf melee hunter, 7% ahead of the
Survival pick in the simulator, was found by hand). Here the search space is all 51-point builds the trees allow (ml_talents.Space with
any_split), per damage entry of the class (each entry is a rotation and gear set; the showcase entries too), in a full raid:
1. the machine-learning search (random forest + genetic search, races, the one-move and chain-move check) from every build of ours,
   the entry's simulator presets and talentsforever.com's popular builds;
2. when the winner is a family the entry was not built for, or beats our best build there by 0.5%, the entry's rotation is re-tuned on
   it (apl_opt.py --tune; every build the entry lists stays protected) and the search runs once more, seeded with the winner;
3. a race over 30,000 fights: the winner against every build of ours the entry races;
4. talent values: every talent of the winner and of our best build there removed in turn (12,000 fights, common random numbers): DPS
   lost, per point, and the share of the build's DPS, plus the search's own feature importances (which talents its model leaned on).
The family of a build is spec_modes' rule: a tree with 30+ points, else "Hybrid A/B" of its two largest trees. A winner in a family no
machine-learning record covers is a lead for a deep search (deep_opt.py with a record for that family). Record raidsim/families/<class>.json
(resumable per entry), reports <class>/research/raid/family-search.md and _reference/family-search.md. The simulator's model of the beta
(and our patches), not in-game measurements; a family that wins on a mechanic the simulator may have wrong says so in the report.
"""
import argparse
import datetime
import importlib.util
import json
import math
import pathlib
import subprocess
import sys
import time

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[2]
sys.path[:0] = [str(ROOT / "_reference/data"), str(HERE)]
import paths  # noqa: E402
import render_start_here as RSH  # noqa: E402
import spec_modes as SM  # noqa: E402


def _load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


MLT = _load("ml_talents_family", HERE / "ml_talents.py")
A, R = MLT.A, MLT.R
SP = _load("spell_probe_family", HERE / "spell_probe.py")
GT = _load("gear_tiers_family", HERE / "gear_tiers.py")
FA = _load("filler_audit_family", HERE / "filler_audit.py")
KNOWN = HERE / "known-positives.json"
OUT = HERE / "families"
PAGE = ROOT / "_reference" / "family-search.md"
TODAY = datetime.date.today().isoformat()
POLISH = dict(fights=300, rounds=24, per_pair=1, top=5, full_fights=800)   # 2026-10-05: one draw; 2026-10-07: batched climbs (ml_talents.polish) take
                                                                            # small cheap steps, so the cap is 24 steps and a climb ends on a full pass without gain
SEARCH = dict(runs=3, budget=3000, screen=1500, patience=5, max_rounds=20, random_init=400, pool=10000, parents=48, finalists=6, screen_budget=600)
AGAIN = dict(SEARCH, runs=2, budget=2000)
RACE, VALUES = 30000, 12000
SMOKE = False


def log(m):
    print(m, flush=True)


def flat_of(alloc):
    return {n: r for items in alloc.values() for n, r in items if r}


def resolve(path):
    p = pathlib.Path(path)
    return p if p.is_absolute() else ROOT / p


def by_tree(space, flat):
    return {t: [[n, flat[n]] for n in space.by_tree[t] if flat.get(n)] for t in space.tree_names}


def entries(cls):
    """Every damage rotation of the class (tanks and healers have their own searches)."""
    return [e for e, x in R.SPECS[cls].items() if isinstance(x, dict) and "apl" in x and not x.get("tank")
            and x.get("profile", "raid-dps") == "raid-dps"]


def known_positives(cls, kind="raid"):
    """The known positives of a class (known-positives.json): flat allocations."""
    if not KNOWN.exists():
        return []
    data = {b["id"]: b for b in json.load(open(paths.builds_json("forever", cls), encoding="utf-8"))["builds"]}
    out = []
    for p in json.load(open(KNOWN, encoding="utf-8")).get("positives", []):
        if p.get("class") != cls or p.get("kind", "raid") != kind:
            continue
        if p.get("build") and p["build"] in data:
            out.append(R.alloc_of(data[p["build"]]))
        elif p.get("allocation"):
            out.append({n: r for n, r in p["allocation"].items() if r})
    return out


def uncast_abilities(cls, entry, repo, flat):
    """Ability talents the build holds whose spell the entry's raid rotation never casts (a line for it was never tried for this family)."""
    book = FA.spell_ids(cls)
    path = R.apl_path(R.SPECS[cls][entry], repo, "raid")
    ids = FA.apl_spell_ids(path, "priorityList") | FA.apl_spell_ids(path, "prepullActions")
    auto = set()   # abilities the simulator applies without a cast (Trueshot Aura, Demonic Sacrifice, Soul Link: unused_abilities.py)
    ua = HERE / "unused-abilities.json"
    if ua.exists():
        auto = {r["talent"] for r in json.load(open(ua, encoding="utf-8")).get("rows", []) if r.get("kind") == "automatic"}
    return [talent for talent, name, sid, text in SP.talent_abilities(cls)
            if flat.get(talent) and name in book and talent not in auto and not (book[name][0] & ids)]


def ours(cls):
    data = {b["id"]: b for b in json.load(open(paths.builds_json("forever", cls), encoding="utf-8"))["builds"]}
    return {bid: b for bid, b in data.items() if SM.mode_of(b) == "raid" and b.get("role") not in ("healer", "tank")}


def family_cache(cls, entry):
    return OUT / "cache" / f"{cls}-{entry}.families.json"


def run_search(cls, entry, repo, settings, starts, seed, protect=None, reuse=False):
    space = MLT.Space(cls, "any", any_split=True)
    starts = [s for s in starts if s and space.valid(s)]
    space.protect = set(protect) if protect is not None else MLT.protected(cls, [entry], repo, "raid", starts)
    space.start_splits = [space.split(s) for s in starts]
    import random
    t0 = time.time()
    psim = MLT.Sim(cls, entry, "raid", None, repo, f"family-polish-{cls}-{entry}")
    fp = family_cache(cls, entry)
    fam = None
    if reuse and fp.exists():   # 2026-10-07 audit: a re-search (after a re-tune or a certificate lead) repeated the 40-minute polish
        try:
            fam = [(d["score"], d["build"], d["label"]) for d in json.load(open(fp, encoding="utf-8")) if space.valid(d["build"])]
            log(f"== {cls} {entry}: {len(fam)} polished families reused from {fp.name} (the first search's; the rotation may have moved since)")
        except (ValueError, KeyError, TypeError):
            fam = None
    if fam is None:
        log(f"== {cls} {entry}: family polish over every pair of {len(space.keystones(damage_only=True))} damage keystones from different trees")
        fam = MLT.family_polish(space, psim, random.Random(seed), log, **POLISH)
        fp.parent.mkdir(parents=True, exist_ok=True)
        fp.write_text(json.dumps([{"score": sc, "build": x, "label": lab} for sc, x, lab in fam]) + "\n", encoding="utf-8")
    log(f"   polish: {len(fam)} families, {psim.n:,} builds simulated ({psim.hits:,} cache hits), {(time.time() - t0) / 60:.1f} min")
    starts = starts + [x for _, x, _ in fam]
    log(f"== {cls} {entry}: open search (any split, full raid), {len(starts)} valid starts; kept: {', '.join(sorted(space.protect)) or 'none'}")
    t1 = time.time()
    a = MLT.defaults(**settings, seed=seed)
    sim = MLT.Sim(cls, entry, "raid", None, repo, f"family-{cls}-{entry}")
    rec, win = MLT.optimize(space, {entry: sim}, starts, a, log)
    log(f"   search: {sim.n:,} builds simulated ({sim.hits:,} cache hits), {(time.time() - t1) / 60:.1f} min")
    rec["families"] = [{"keystones": lab, "split": space.split(x), "family": space.classify(x), "score": round(sc, 1)} for sc, x, lab in fam[:15]]
    rec["timing"] = {"polish_min": round((time.time() - t0) / 60 - (time.time() - t1) / 60, 1), "search_min": round((time.time() - t1) / 60, 1),
                     "polish_builds": psim.n, "search_builds": sim.n, "cache_hits": psim.hits + sim.hits}
    return space, rec


def values(cls, entry, repo, flat):
    """{talent: {ranks, lost, per_point, share}}: DPS lost when each talent is removed (common random numbers)."""
    trees = R.load_trees(repo, cls)
    builds = [{"label": "base", "talents": R.talents_string(trees, flat)}]
    for n in flat:
        builds.append({"label": n, "talents": R.talents_string(trees, {k: v for k, v in flat.items() if k != n})})
    rows = A.bench(R.SPECS[cls][entry], repo, builds, VALUES, 5, "raid", f"family-values-{cls}")
    base = (rows.get("base") or {}).get("dps") or 0.0
    out = {}
    for n, r in flat.items():
        d = (rows.get(n) or {}).get("dps")
        if d is None or not base:
            continue
        lost = base - d
        out[n] = {"ranks": r, "lost": round(lost, 1), "per_point": round(lost / r, 1), "share": round(lost / base, 4)}
    return dict(sorted(out.items(), key=lambda kv: -kv[1]["lost"])), round(base, 1)


def race(cls, entry, repo, flat, mine):
    rows = {"open winner": flat} | {bid: R.alloc_of(b) for bid, b in mine.items()}
    sim = MLT.Sim(cls, entry, "raid", None, repo, f"family-race-{cls}")
    res = sim.run(list(rows.values()), RACE, 43)
    return {k: {"dps": round(d, 1), "se": round(sd / math.sqrt(RACE), 2)} for k, (d, sd) in zip(rows, res)}


def signature(cls, entry, repo):
    """What a search of an entry depends on: its raid rotation's actions (notes stripped), gear set, race, options, consumables and
    buff switches; two entries with the same signature search the same thing."""
    import hashlib
    E = R.SPECS[cls][entry]
    try:
        apl = json.load(open(R.apl_path(E, repo, "raid"), encoding="utf-8"))
    except (OSError, ValueError):
        apl = {}
    acts = [{k: v for k, v in it.items() if k != "notes"} for it in apl.get("priorityList", [])]
    body = [acts, apl.get("prepullActions", []), E.get("gear"), E.get("race"), E.get("spec"), E.get("consumables"), E.get("self_buffs"),
            E.get("self_debuffs"), E.get("buffs_off"), E.get("debuffs_off"), E.get("profession1"), E.get("profession2"), E.get("distance")]
    return hashlib.md5(json.dumps(body, sort_keys=True, default=str).encode("utf-8")).hexdigest()[:12]


def retune(cls, entry, flat, quick=False):
    """apl_opt --tune on a build (the entry's listed builds protected). quick (2026-10-07, the certificates' re-searches): the raid setting
    only, 8 rounds, no two-edit lookahead; a full re-tune of a 16-line rotation took over three hours on a shared CPU."""
    tune = OUT / "tune" / f"{cls}-{entry}.json"
    tune.parent.mkdir(parents=True, exist_ok=True)
    tune.write_text(json.dumps([{"label": "open winner", "allocation": flat}], indent=1), encoding="utf-8")
    log(f"== rotation {cls}/{entry}: tuning on the open winner (every build the entry lists protected){' (quick: raid setting, 8 rounds, no lookahead)' if quick else ''}")
    args = [sys.executable, str(HERE / "apl_opt.py"), cls, "--spec", entry, "--tune", str(tune), "--write"]
    args += ["--rounds", "8", "--lookahead", "0", "--setting", "raid"] if quick else ["--rounds", "20"]
    r = subprocess.run(args, capture_output=True, text=True, encoding="utf-8", errors="replace", cwd=str(ROOT))
    for ln in r.stdout.splitlines():
        if ln.strip().startswith(("==", "round", "raid", "wrote", "no change")):
            log("  " + ln.strip()[:220])
    R.set_game("forever")
    return "wrote" in r.stdout


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("cls", nargs="?")
    ap.add_argument("--entry", action="append")
    ap.add_argument("--fresh", action="store_true")
    ap.add_argument("--smoke", action="store_true", help="tiny budgets, a separate record, nothing else written (a test)")
    ap.add_argument("--report", action="store_true", help="write the cross-class page from the records and stop")
    ap.add_argument("--no-known", action="store_true", help="leave out the known builds (candidate files, earlier winners): a clean test of the search")
    a = ap.parse_args()
    global OUT, SEARCH, AGAIN, RACE, VALUES, SMOKE, POLISH
    if a.report:
        write_page()
        return
    if a.smoke:
        OUT, SMOKE, RACE, VALUES = HERE / "families-smoke", True, 2000, 1000
        POLISH = dict(fights=60, rounds=1, per_pair=1, top=1, full_fights=100)
        SEARCH = AGAIN = dict(runs=1, budget=150, screen=300, patience=1, max_rounds=1, random_init=40, pool=600, parents=8, finalists=2,
                              screen_budget=60, race_stages=((1000, 2, 2), (2000, 3, 1), (4000, 4, 1)), cert_its=(500, 2000))
    cls = a.cls
    R.set_game("forever")
    repo = R.repo_path(argparse.Namespace(repo=None))
    OUT.mkdir(parents=True, exist_ok=True)
    rp = OUT / f"{cls}.json"
    prev = rp.with_suffix(".prev.json")
    if a.fresh and rp.exists() and not SMOKE:
        rp.replace(prev)   # warm start (2026-10-05): the last run's winners seed the new search after a beta update
    st = json.load(open(rp, encoding="utf-8")) if rp.exists() and not a.fresh else {"class": cls, "date": TODAY, "entries": {}}
    warm = []
    if prev.exists():
        for e in json.load(open(prev, encoding="utf-8")).get("entries", {}).values():
            for k in ("again", "first"):
                if (e.get(k) or {}).get("winner"):
                    warm.append(flat_of(e[k]["winner"]["allocation"]))

    def save():
        rp.write_text(json.dumps(st, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")

    log(f"=== {cls} open raid search started {datetime.datetime.now():%Y-%m-%d %H:%M}" + (" (--fresh)" if a.fresh else "")
        + f"; record {rp.name} ({len([e for e in st['entries'].values() if e.get('done')])} entries done)")   # the log is cumulative
    mine_all = ours(cls)
    starts = [R.alloc_of(b) for b in mine_all.values()] + MLT.popular_allocs(cls)
    if not a.no_known:   # known good builds: the known positives, the last run's winners, the archived first pass, the saved raid candidates
        starts += known_positives(cls) + warm
        v1 = OUT / "v1" / f"{cls}.json"
        if v1.exists():
            for e in json.load(open(v1, encoding="utf-8")).get("entries", {}).values():
                for k in ("again", "first"):
                    if (e.get(k) or {}).get("winner"):
                        starts.append(flat_of(e[k]["winner"]["allocation"]))
        for f in sorted((paths.scenario_dir(cls, "raid") / "raidsim" / "candidates").glob("*.json")):
            try:
                x = json.load(open(f, encoding="utf-8"))
                al = x.get("allocation") or {}
                starts.append(flat_of(al) if al and isinstance(next(iter(al.values())), list) else {n: r for n, r in al.items() if r})
            except (ValueError, StopIteration, AttributeError):
                pass
    for entry in a.entry or entries(cls):
        if entry in st["entries"] and st["entries"][entry].get("done"):
            continue
        t0 = time.time()
        e = st["entries"].setdefault(entry, {})
        here = {bid: mine_all[bid] for bid in R.SPECS[cls][entry].get("builds", []) if bid in mine_all}
        e["signature"] = signature(cls, entry, repo)
        twin = next((e2 for e2, v in st["entries"].items() if e2 != entry and v.get("done") and v.get("signature") == e["signature"]), None)
        if twin:   # 2026-10-07 (user decision): an entry whose raid rotation, gear and options equal a finished entry's is a duplicate
            log(f"== {cls} {entry}: the same raid rotation, gear and options as {twin}: its results copied, nothing searched twice")
            e.update({k: v for k, v in st["entries"][twin].items() if k not in ("signature", "minutes", "builds")}, same_as=twin, minutes=0.0, done=True)
            save()
            continue
        if "first" not in e:
            sp, rec = run_search(cls, entry, repo, SEARCH, starts + MLT.preset_allocs(cls, R.SPECS[cls][entry], repo), 71)
            e["first"] = {"winner": rec["winner"], "family": sp.classify(flat_of(rec["winner"]["allocation"])), "runs_agree": rec["runs_agree"],
                          "important_features": rec.get("important_features"), "simulated_builds": rec["simulated_builds"], "protected": sorted(sp.protect),
                          "families": rec.get("families")}
            save()
        w = flat_of(e["first"]["winner"]["allocation"])
        if "race_first" not in e:
            e["race_first"] = race(cls, entry, repo, w, here)
            save()
        best_ours = max((v["dps"] for k, v in e["race_first"].items() if k != "open winner"), default=0.0)
        new_family = e["first"]["family"] not in {SM.spec_of(cls, b) for b in here.values()}
        if "probe" not in e:
            # an ability talent the winner holds but the rotation never casts: give it a line (spell_probe: every line and spot, kept at
            # 0.2% on a second seed), so the re-search can value it (2026-10-05: the talent search cannot see an ability without a line)
            miss = uncast_abilities(cls, entry, repo, w)
            if miss and not SMOKE:
                log(f"== {cls} {entry}: the open winner holds {', '.join(miss)} and the rotation never casts them: probing lines")
                res, base_apl = SP.probe(cls, "any", entry, w, "raid", None, any_split=True, log=log, only=set(miss))
                n = SP.write(cls, entry, "raid", res, base_apl)
                e["probe"] = {"talents": miss, "lines_kept": n}
                if n:
                    R.set_game("forever")
            else:
                e["probe"] = {"talents": miss, "lines_kept": 0} if miss else None
            save()
        if "again" not in e:
            if (new_family or e["race_first"]["open winner"]["dps"] > best_ours * 1.005 or (e.get("probe") or {}).get("lines_kept")) and not SMOKE:
                e["rotation_changed"] = retune(cls, entry, w)
                sp, rec = run_search(cls, entry, repo, AGAIN, [w] + starts, 72, protect=e["first"]["protected"], reuse=True)
                e["again"] = {"winner": rec["winner"], "family": sp.classify(flat_of(rec["winner"]["allocation"])), "runs_agree": rec["runs_agree"],
                              "important_features": rec.get("important_features"), "simulated_builds": rec["simulated_builds"]}
            else:
                e["again"] = None
            save()
        fin = e["again"] or e["first"]
        w = flat_of(fin["winner"]["allocation"])
        if "race" not in e:
            e["race"] = race(cls, entry, repo, w, here) if e["again"] else e["race_first"]
            save()
        if "values" not in e:
            e["values"], e["values_base"] = values(cls, entry, repo, w)
            best = max((k for k in e["race"] if k != "open winner"), key=lambda k: e["race"][k]["dps"], default=None)
            if best:
                e["values_ours"], e["values_ours_base"] = values(cls, entry, repo, R.alloc_of(mine_all[best]))
                e["ours_best"] = best
            save()
        if "synergy" not in e and not SMOKE:
            # the synergy certificate (2026-10-06, raidsim/synergy.py): every pair of relevant talents measured around the winner; a lead
            # 0.5% ahead re-tunes the rotation, searches again from it and redoes the race and values (a missed package: Shatter +
            # Fingers of Frost + Ice Lance on the Frostfire mage)
            SY = importlib.util.module_from_spec(importlib.util.spec_from_file_location("synergy_fs", HERE / "synergy.py"))
            SY.__spec__.loader.exec_module(SY)
            SY.certificate(cls, entry, e, repo, st, save, argparse.Namespace(no_search=False))
            R.set_game("forever")   # the certificate's re-tune may have pointed the entry at a new rotation file
            if (e.get("synergy") or {}).get("researched"):   # a new winner: measure around it again for the structural ranking
                e["synergy_first"] = e["synergy"]
                e.pop("synergy")
                SY.certificate(cls, entry, e, repo, st, save, argparse.Namespace(no_search=True))
            w = flat_of((e.get("again") or e["first"])["winner"]["allocation"])
        if "structural" not in e and not SMOKE and (e.get("synergy") or {}).get("singles_all"):
            # the exhaustive structural ranking (2026-10-07, raidsim/structural.py): a quadratic model fitted to the certificate's
            # measurements ranks every legal structure; the model's top 300 are simulated and raced; a lead re-searches like the certificate's
            ST = importlib.util.module_from_spec(importlib.util.spec_from_file_location("structural_fs", HERE / "structural.py"))
            ST.__spec__.loader.exec_module(ST)
            ST.structural(cls, entry, e, repo, save, argparse.Namespace(top=300, race=20, no_search=False))
            R.set_game("forever")
            w = flat_of((e.get("again") or e["first"])["winner"]["allocation"])
        sp = MLT.Space(cls, "any", any_split=True)
        e.update({"family": sp.classify(w), "split": sp.split(w), "dps": e["race"]["open winner"]["dps"], "link": RSH.tf_link(cls, w),
                  "gap_vs_ours": round(e["race"]["open winner"]["dps"] / max(1e-9, max((v["dps"] for k, v in e["race"].items() if k != "open winner"),
                                                                                    default=1e-9)) - 1, 4) if len(e["race"]) > 1 else None,
                  "minutes": round((time.time() - t0) / 60, 1), "done": True})
        save()
        log(f"  {cls} {entry}: open winner {e['split']} ({e['family']}) {e['dps']:.1f} DPS"
            + (f", {e['gap_vs_ours']:+.1%} vs our best there ({e.get('ours_best')})" if e.get("gap_vs_ours") is not None else ""))
    if not SMOKE:
        cross_rotations(cls, st, repo, save, mine_all)
        own_gear(cls, st, repo, save)
        write_class(cls, st)
        write_page()
    log("== done")


def cross_rotations(cls, st, repo, save, mine_all):
    """Every entry's builds under each sibling entry's raid rotation, in the entry's own gear (2026-10-06, the hunter's lesson: the +2%
    Retribution rotation came from a sibling entry's re-tune). A sibling rotation 0.5% ahead for the entry's best build on 10,000 fights
    and again on 30,000 (another seed), costing no listed build 1%, replaces the entry's raid rotation (a pass in its rotation-search
    record; apl_opt.py --tune then polishes it) and the entry's race and talent values are redone under it."""
    done = st.setdefault("cross", {})
    ents = [e for e, v in st["entries"].items() if v.get("done")]
    trees = R.load_trees(repo, cls)
    for entry in ents:
        if entry in done:
            continue
        e = st["entries"][entry]
        E = R.SPECS[cls][entry]
        here = {bid: mine_all[bid] for bid in E.get("builds", []) if bid in mine_all}
        if not here:   # 2026-10-07 audit: a showcase entry with none of our builds (Shockadin) spent an hour adopting and re-tuning a sibling rotation
            log(f"  cross-rotations {entry}: no build of ours in the entry, skipped")
            done[entry] = {"tested": {}, "adopted": None, "skipped": "no builds of ours"}
            save()
            continue
        w = flat_of((e.get("again") or e["first"])["winner"]["allocation"])
        builds = {"open winner": w} | {bid: R.alloc_of(b) for bid, b in here.items()}
        own_apl = json.load(open(R.apl_path(E, repo, "raid"), encoding="utf-8"))
        rec = {"tested": {}, "adopted": None}
        base = A.bench(E, repo, [{"label": k, "talents": R.talents_string(trees, v), "apl_json": own_apl} for k, v in builds.items()], 10000, 1, "raid", f"cross-{cls}")
        best_label = max(base, key=lambda k: base[k].get("dps") or 0)
        for sib in ents:
            if sib == entry:
                continue
            apl = json.load(open(R.apl_path(R.SPECS[cls][sib], repo, "raid"), encoding="utf-8"))
            rows = A.bench(E, repo, [{"label": k, "talents": R.talents_string(trees, v), "apl_json": apl} for k, v in builds.items()], 10000, 1, "raid", f"cross-{cls}")
            gains = {k: round((rows[k].get("dps") or 0) / (base[k].get("dps") or 1) - 1, 4) for k in builds if rows.get(k) and base.get(k)}
            rec["tested"][sib] = gains
            g = gains.get(best_label, -1)
            if g >= 0.005:
                c = A.bench(E, repo, [{"label": "own", "talents": R.talents_string(trees, builds[best_label]), "apl_json": own_apl},
                                     {"label": "sib", "talents": R.talents_string(trees, builds[best_label]), "apl_json": apl}], 30000, 2, "raid", f"cross-{cls}")
                g2 = (c["sib"].get("dps") or 0) / (c["own"].get("dps") or 1) - 1
                rec["tested"][sib]["confirm_seed2"] = round(g2, 4)
                if g2 >= 0.005 and min(gains.values()) > -0.01 and (rec["adopted"] is None or g2 > rec["adopted"]["gain"]):
                    rec["adopted"] = {"from": sib, "gain": round(g2, 4), "build": best_label}
        log(f"  cross-rotations {entry}: " + ", ".join(f"{sib} {v.get(best_label, 0):+.1%}" for sib, v in rec["tested"].items())
            + (f" -> adopting {rec['adopted']['from']}'s rotation ({rec['adopted']['gain']:+.1%})" if rec["adopted"] else ""))
        if rec["adopted"]:
            adopt_rotation(cls, entry, rec["adopted"]["from"], rec["adopted"]["gain"], repo)
            retune(cls, entry, w)
            e["race"] = race(cls, entry, repo, w, here)
            e["values"], e["values_base"] = values(cls, entry, repo, w)
            best = max((k for k in e["race"] if k != "open winner"), key=lambda k: e["race"][k]["dps"], default=None)
            e.update({"dps": e["race"]["open winner"]["dps"], "ours_best": best,
                      "gap_vs_ours": round(e["race"]["open winner"]["dps"] / e["race"][best]["dps"] - 1, 4) if best else None, "rotation_changed": True})
        done[entry] = rec
        save()


def adopt_rotation(cls, entry, sib, gain, repo):
    """Copy a sibling entry's raid rotation over the entry's, with a note per line and a pass in the entry's rotation-search record."""
    E, S = R.SPECS[cls][entry], R.SPECS[cls][sib]
    dst = R.apl_path(E, repo, "raid")
    apl = json.load(open(R.apl_path(S, repo, "raid"), encoding="utf-8"))
    for it in apl.get("priorityList", []):
        it["notes"] = (f"{TODAY}: {sib}'s raid rotation adopted by the open search's cross-race ({gain:+.1%} for the entry's best build); "
                       + (it.get("notes") or "")).rstrip("; ")
    if not str(dst).startswith(str(ROOT)):   # the entry still ran the simulator's own rotation: give it a file of ours
        dst = HERE / "apls" / cls / f"{entry}-raid.apl.json"
        dst.parent.mkdir(parents=True, exist_ok=True)
    dst.write_text(json.dumps(apl, indent=1) + "\n", encoding="utf-8")
    rp = paths.scenario_dir(cls, "raid") / "raidsim" / f"{entry}-rotation-search.json"
    rec = json.load(open(rp, encoding="utf-8")) if rp.exists() else {}
    if "changes" in rec:
        rec = {rec.get("setting", "dummy"): rec}
    r = rec.setdefault("raid", {"class": cls, "spec": entry, "setting": "raid", "changes": [], "passes": 0, "start": "cross-race"})
    r["passes"] = r.get("passes", 1) + 1
    r.setdefault("changes", []).append({"round": len(r.get("changes", [])) + 1, "pass": r["passes"], "date": TODAY,
                                         "change": f"rotation replaced by {sib}'s raid rotation (the open search's cross-race of every build under every sibling rotation)",
                                         "gain_seed1": None, "gain_seed2": round(gain, 4), "candidates": 1})
    rp.write_text(json.dumps(rec, indent=1) + "\n", encoding="utf-8")
    with A.specs_lock():
        A._point_specs(HERE / "specs.json", cls, entry, "apl_opt_raid", dst)
    R.set_game("forever")


def own_gear(cls, st, repo, save):
    """A phase-1 BiS set of its own for every open winner in a family no machine-learning record covers (2026-10-06: the Hawk hunter
    was scored in pure melee gear while its hawks scale with ranged attack power); the winner raced in it against the entry's standard
    set, both recorded. gear_tiers.make writes raidsim/gear_sets/forever/tiers/<class>-<family slug>-bis.gear.json."""
    done = st.setdefault("own_gear", {})
    ml = {json.load(open(p, encoding="utf-8")).get("spec") for p in (HERE / "ml").glob(f"{cls}-*.json")}
    db = zones = None
    trees = R.load_trees(repo, cls)
    for entry, e in st["entries"].items():
        if not e.get("done") or entry in done:
            continue
        fam = e.get("family")
        if fam in ml:
            done[entry] = None
            continue
        if db is None:
            db, zones = GT.load_db(repo)
        w = flat_of((e.get("again") or e["first"])["winner"]["allocation"])
        log(f"== {cls} {entry}: BiS set for the open winner's family ({fam}: no machine-learning record)")
        try:
            g = GT.make(cls, fam, "bis", entry, R.talents_string(trees, w), "open winner", repo, db, zones, GT.args_ns())
        except Exception as ex:   # noqa: BLE001
            log(f"  gear: failed ({type(ex).__name__}: {ex})")
            done[entry] = {"error": str(ex)[:200]}
            save()
            continue
        items = json.load(open(resolve(g["gear"]), encoding="utf-8"))["items"]
        E = R.SPECS[cls][entry]
        rows = A.bench(E, repo, [{"label": "standard", "talents": R.talents_string(trees, w)},
                                {"label": "own BiS", "talents": R.talents_string(trees, w), "gear_json": {"items": items}}], 30000, 5, "raid", f"owngear-{cls}")
        done[entry] = {"gear": g["gear"], "ilvl": g.get("ilvl"), "names": g.get("names"), "dps_standard": round(rows["standard"].get("dps") or 0, 1),
                       "dps_own_bis": round(rows["own BiS"].get("dps") or 0, 1)}
        log(f"  gear: standard set {done[entry]['dps_standard']} -> own BiS {done[entry]['dps_own_bis']} DPS")
        save()


def table(vals, base):
    o = ["| Talent | Ranks | DPS lost without it | Per point | Share of the build |", "|---|---|---|---|---|"]
    o += [f"| {n} | {v['ranks']} | {v['lost']:+.1f} | {v['per_point']:+.1f} | {v['share']:+.1%} |" for n, v in vals.items()]
    return o + ["", f"(the build: {base:.1f} DPS in a full raid; removal values do not add up to the build: talents interact)", ""]


def write_class(cls, st):
    o = [f"# {cls.capitalize()}: open talent search (generated)", "",
         f"> Generated by `_reference/data/raidsim/family_search.py` on {TODAY}; record `_reference/data/raidsim/families/{cls}.json`. Do not hand-edit.", "",
         "Every legal 51-point build, no tree rule, searched in each damage rotation of the class in a full raid (the community simulator's "
         "model of the beta with this project's patches). The family is a tree with 30+ points, else the two largest trees. Talent values: "
         "DPS lost when the talent is removed from the build, 12,000 fights, common random numbers.", "",
         "| Rotation (entry) | Open winner | Family | DPS | vs our best build there | Rotation re-tuned |", "|---|---|---|---|---|---|"]
    for entry, e in st["entries"].items():
        if not e.get("done"):
            continue
        o.append(f"| {entry} | [{e['split']}]({e['link']}) | {e['family']} | {e['dps']:.1f} | "
                 + (f"{e['gap_vs_ours']:+.1%} ({e.get('ours_best')})" if e.get("gap_vs_ours") is not None else "-")
                 + f" | {'yes' if e.get('rotation_changed') else 'no'} |")
    o.append("")
    for entry, e in st["entries"].items():
        if not e.get("done"):
            continue
        o += [f"## {entry}", ""]
        fam = (e.get("first") or {}).get("families") or []
        if fam:
            o += ["**Best family per pair of keystones** (each polished by a short hill climb that keeps the pair; DPS on 800 fights, before "
                  "the main search):", "", "| Keystones | Build | Family | DPS |", "|---|---|---|---|"]
            o += [f"| {f['keystones']} | {f['split']} | {f['family']} | {f['score']:.1f} |" for f in fam[:10]] + [""]
        o += [f"**Open winner {e['split']}** ({e['family']}):", ""] + table(e["values"], e["values_base"])
        if e.get("values_ours"):
            o += [f"**Our best build there, {e['ours_best']}:**", ""] + table(e["values_ours"], e["values_ours_base"])
        cr = (st.get("cross") or {}).get(entry)
        if cr and cr.get("tested"):
            lab = (cr.get("adopted") or {}).get("build") or "open winner"
            o += ["Sibling rotations (the entry's best build under each, 10,000 fights): " + ", ".join(f"{sib} {v.get(lab, 0):+.1%}" for sib, v in cr["tested"].items())
                  + (f"; **adopted {cr['adopted']['from']}'s rotation ({cr['adopted']['gain']:+.1%} on 30,000 fights)**" if cr.get("adopted") else "; none adopted") + ".", ""]
        og = (st.get("own_gear") or {}).get(entry)
        if og and og.get("gear"):
            o += [f"Own phase-1 BiS set for this family (`{og['gear']}`, item level {og.get('ilvl')}): {og['dps_own_bis']:.1f} DPS against "
                  f"{og['dps_standard']:.1f} in the entry's standard set.", ""]
        imp = (e.get("again") or e.get("first") or {}).get("important_features") or []
        if imp:
            o += ["The search model's most important talents (random-forest importance): "
                  + ", ".join(f"{x['feature']} {x['importance']:.2f}" for x in imp[:10]) + ".", ""]
        sy = e.get("synergy")
        if sy:   # synergy.py: every pair of relevant talents measured around the winner
            o += [f"**Synergy certificate** ({sy['date']}, raidsim/synergy.py): {sy['relevant']} relevant talents, {sy['missing']} the winner lacks; "
                  f"{sy['pairs']} pairs measured around {sy['winner']} on {sy['screen_fights']} fights. Largest interactions (DPS of both against the "
                  "two alone): " + ", ".join(f"{x['pair']} {x['interaction']:+.1%} (build {x['gain']:+.1%})" for x in sy.get("top_interactions", [])[:6]) + ". "
                  + (("Leads polished and raced: " + ", ".join(f"{ld['pair']} -> {ld['split']} {ld['gain']:+.1%}" for ld in sy["leads"]) + ". ") if sy.get("leads") else "No pair build within 1% of the winner. ")
                  + (f"**The search had missed it: searched again from the lead {sy['researched']['lead']}, winner now {sy['researched']['winner']} at {sy['researched']['dps']:.1f} DPS.**"
                     if sy.get("researched") else "The certificate confirms the winner."), ""]
        bw = e.get("builds")
        if bw:   # open_builds.py's verdict: a derived build on the pages, or the build it confirms
            o += [f"Build ({bw['date']}, open_builds.py): " + (", ".join(f"`{b}`" for b in bw["written"]) if bw.get("written") else bw.get("why") or "none") + ".", ""]
    p = paths.scenario_dir(cls, "raid") / "family-search.md"
    p.write_text("\n".join(o) + "\n", encoding="utf-8")
    log(f"wrote {p.relative_to(ROOT).as_posix()}")


def write_page():
    rows = []
    for f in sorted(OUT.glob("*.json")):
        if f.name.endswith(".prev.json"):   # a warm-start record of an earlier pass (2026-10-06: it had put the pass's rows on the page)
            continue
        st = json.load(open(f, encoding="utf-8"))
        for entry, e in st.get("entries", {}).items():
            if e.get("done"):
                rows.append((st["class"], entry, e))
    o = ["# Open talent search across the classes (generated)", "",
         f"> Generated by `_reference/data/raidsim/family_search.py` on {TODAY}. Do not hand-edit.", "",
         "The best build found with no tree rule in each damage rotation, in a full raid, against our best build in that rotation. A winner "
         "in a family no search covered before (a hybrid such as 16/11/24) is a lead for a deep search. The community simulator's model of "
         "the beta with this project's patches; not in-game measurements.", "",
         "| Class | Rotation (entry) | Open winner | Family | DPS | vs our best there |", "|---|---|---|---|---|---|"]
    for cls, entry, e in sorted(rows, key=lambda x: -x[2]["dps"]):
        o.append(f"| [{cls}]({paths.rel(PAGE, paths.scenario_dir(cls, 'raid') / 'family-search.md')}) | {entry} | [{e['split']}]({e['link']}) | "
                 f"{e['family']} | {e['dps']:.1f} | " + (f"{e['gap_vs_ours']:+.1%}" if e.get("gap_vs_ours") is not None else "-") + " |")
    PAGE.write_text("\n".join(o) + "\n", encoding="utf-8")
    log(f"wrote {PAGE.relative_to(ROOT).as_posix()}")


if __name__ == "__main__":
    main()
