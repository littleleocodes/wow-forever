"""The machine-learning pipeline's results as builds and pages (2026-10-01, user request: a systematic machine-learning optimisation of
every raid damage spec, and "DPS ranking for Pre-bis as well as best in slot armor. Similar to what WoWSims does").

    python _reference/data/raidsim/ml_builds.py [classes] --builds     # winners into proposed-builds.json (then validate + render)
    python _reference/data/raidsim/ml_builds.py [classes] --rank       # _reference/dps-rankings.md + "## DPS by gear tier" of the research READMEs

--builds, for every spec whose record (`raidsim/ml/<class>-<spec slug>.json`, written by ml_pipeline.py or deep_opt.py) is complete
(raid-first since 2026-10-02, user decision: "the recommendations should always be what offers the highest dps in a raid/group setting"):
- the full-raid winner in the spec's phase-1 BiS set becomes the spec's derived raid build `<spec page slug>-ml-raid` (🔬, `derived:
  raid`) when the record's full-raid comparison race (`compare_raid`: ml_pipeline.compare(..., "raid"), 100,000 fights, one fresh seed,
  BiS set) has it 0.5% or more ahead of every build raced there (the spec's three best builds by full-raid DPS and its two best hand
  drafts); otherwise the search confirms the current pick and no build is written. It carries `replaces` when it beats the spec's best
  hand draft there by the replacement bar (0.5% since 2026-10-07, 2% before; the hand draft stays as the alternative; the pages enforce the rule on the race
  numbers, render_modes.DERIVED_BAR). It supersedes the spec's earlier derived raid builds (derive_raid.py's local search, earlier ML
  builds, the old training-dummy `-ml-raid` and full-raid `-ml-parse` pair), removed and marked "superseded" in derived-raid.json so a
  later `derive_raid.py --write` does not bring them back. It joins the specs.json builds of the entry it won in.
- before that, points the simulator cannot tell apart follow the hand draft (`align`, in the full raid): a search winner picks
  arbitrarily among talents that do nothing (Burning Soul and Magic Absorption measure exactly the same with common random numbers), so
  every point is moved toward the spec's best hand draft (else its current best build) while the build stays legal and within 0.03% of
  the winner on one seed (5,000 fights to screen the moves, the kept move confirmed over 30,000).
Every written build then goes through filler_audit.py in the full raid (`tidy`: zero-value points and talents whose ability the rotation
never casts move to a DPS gain or a useful talent; 2026-10-02, after the Frost winner kept a never-cast Arcane Blast for tier gating).
The pages need race numbers for the new builds: re-race their entries afterwards (raidsim/run.py with --env environments, or rebuild.py
--steps raid,adopt,regen).
--rank: every spec's pre-BiS and BiS DPS, training dummy and full raid, from the records (each a search winner raced over 100,000
fights; talents searched separately for each tier and setting, gear per spec and tier by gear_tiers.py).
"""
import argparse
import datetime
import importlib.util
import json
import math
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[2]
sys.path[:0] = [str(ROOT / "_reference/data"), str(HERE)]
import gear_tables as GTAB  # noqa: E402


def sim_of(r):
    """The simulator commit a search record ran on: its own `commit` (ml_pipeline.py writes it since 2026-10-09), else the pin of the
    record's date (40be98e until 2026-10-03, b0f0df3 until 2026-10-08, then setup.py's pin)."""
    c = (r.get("compare") or {}).get("commit") or ((r.get("search") or {}).get("bis-dummy") or {}).get("commit") or r.get("commit")
    if c:   # the comparison race's (the numbers the pages show; audit 2026-10-18 row 81), else the final search's, else the record's
        return c[:7]
    return SI.commit_of_date(   # the pin of the record's date (2026-10-22: 2ce8265 and b7083fa added; after the port, setup.py's pin)
        r.get("date"))
import paths  # noqa: E402
import readme_sections as RS  # noqa: E402
import render_start_here as RSH  # noqa: E402
import spec_modes as SM  # noqa: E402
import sim_info as SI  # noqa: E402  (which simulator a record ran on)
from filelock import locked  # noqa: E402
from fmt_json import dumps  # noqa: E402
import builds_io as BIO  # noqa: E402  (locked writes of proposed-builds.json, 2026-10-24)


def _load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


OUT = HERE / "ml"
PAGE = ROOT / "_reference" / "dps-rankings.md"
DERIVED_RAID = ROOT / "_reference" / "data" / "derived-raid.json"
TODAY = datetime.date.today().isoformat()
MIN_GAIN = 0.005    # the replacement bar (hand draft -> derived build): 0.5% since 2026-10-07 (2% before; a rule Claude set, not the user)
GAIN_NEW = 0.005    # an ML winner becomes a build only this far ahead of every build in its comparison race (else it confirms them)
ALIGN_TOL = 0.0003  # alignment: moves toward the hand draft keep the build within this of the winner (same seed)
KEYS = ("bis-dummy", "bis-raid", "prebis-dummy", "prebis-raid")
SLOTS = ["Head", "Neck", "Shoulders", "Back", "Chest", "Wrist", "Hands", "Waist", "Legs", "Feet", "Finger", "Finger", "Trinket", "Trinket",
         "Main hand", "Off hand", "Ranged/relic"]
HEAD = "## DPS by gear tier"
TIER_NAME = {"prebis": "Pre-BiS", "bis": "Phase 1 BiS"}
TIER_TEXT = {"prebis": "dungeons, crafted, quest, world drops and reputation; no raid items",
             "bis": "adds Molten Core, Onyxia and the Forever launch items"}


def records(classes=None):
    out = []
    for p in sorted(OUT.glob("*.json")):
        if p.name in ("spell-probe.json", "rotations.json"):
            continue
        r = json.load(open(p, encoding="utf-8"))
        if r.get("class") and (not classes or r["class"] in classes):
            out.append(r)
    return out


def save(r):
    (OUT / f"{r['class']}-{r['slug']}.json").write_text(json.dumps(r, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")


def complete(r):
    return all(k in r.get("search", {}) for k in KEYS) and "compare" in r


def flat_of(alloc):
    return {n: rk for items in alloc.values() for n, rk in items}


def winner(r, k):
    return (r.get("search", {}).get(k) or {}).get("winner")


# ------------------------------------------------------------------------------------------------ builds
def drop_from_entries(cls, ids):
    """Remove build ids from the class's specs.json `builds` lists by a text edit (the file's hand layout stays; spec_builds.add_to_entry
    is the counterpart)."""
    sp = HERE / "specs.json"
    specs = json.load(open(sp, encoding="utf-8"))
    t = sp.read_text(encoding="utf-8")
    c = t.index(f'"{cls}": {{')
    for entry, e in specs.get(cls, {}).items():
        if not isinstance(e, dict) or not set(e.get("builds", [])) & set(ids):
            continue
        s0 = t.index(f'"{entry}": {{', c)
        b0 = t.index('"builds": [', s0) + len('"builds": [')
        end = t.index("]", b0)
        items = [x.strip() for x in t[b0:end].split(",") if x.strip() and x.strip().strip('"') not in ids]
        t = t[:b0] + ", ".join(items) + t[end:]
    sp.write_text(t, encoding="utf-8")
    left = json.load(open(sp, encoding="utf-8"))[cls]
    assert not any(b in ids for e in left.values() if isinstance(e, dict) for b in e.get("builds", []))


def supersede(cls, spec, old_ids, by):
    """Mark derive_raid.py's records of the removed builds, so its --write does not bring them back."""
    if not DERIVED_RAID.exists():
        return
    with locked(DERIVED_RAID.with_suffix(".lock")):
        d = json.load(open(DERIVED_RAID, encoding="utf-8"))
        hit = False
        for rec in (d.get(cls) or {}).values():
            if rec.get("tree") == spec and rec.get("role") == "dps" and rec.get("verdict") in ("replaces", "new"):
                rec.update(verdict="superseded", superseded_by=by, superseded_on=TODAY, removed=sorted(old_ids))
                hit = True
        if hit:
            DERIVED_RAID.write_text(json.dumps(d, indent=1) + "\n", encoding="utf-8")


def cert_text(w):
    cert = w.get("certificate") or []
    if not cert:
        return "not run"
    last = cert[-1]
    moved = sum(1 for c in cert if c.get("raced") and (c.get("confirmed_gap") or 0) > 0.001)
    head = f"{moved} confirmed move{'s' if moved != 1 else ''} first, then " if moved else ""
    if not last.get("raced"):
        return head + f"none of its {last['neighbours']} one-move and chain-move neighbours was 0.1% ahead"
    if (last.get("confirmed_gap") or 0) <= 0.001:
        return head + f"the neighbours ahead on the short run (of {last['neighbours']}) did not hold on the longer one"
    return f"stopped after {moved} confirmed moves (the limit)"


def differs_text(w):
    """How the race's runner-up differs from the winner (the record keeps the symmetric difference of their (talent, rank) pairs)."""
    win = {(n, k) for items in w["winner"]["allocation"].values() for n, k in items}
    d = [tuple(x) for x in (w.get("runner_up") or {}).get("differs") or []]
    mine = [f"{n} {k}" for n, k in d if (n, k) in win]
    theirs = [f"{n} {k}" for n, k in d if (n, k) not in win]
    parts = ([f"the winner takes {', '.join(mine)}"] if mine else []) + ([f"the runner-up {', '.join(theirs)}"] if theirs else [])
    return "; ".join(parts) or "the same talents"


def make_build(r):
    """The spec's full-raid winner as a derived raid build (raid pages rank by full-raid DPS since 2026-10-02)."""
    cls, spec = r["class"], r["spec"]
    w = r["search"]["bis-raid"]
    name = SM.spec_name(cls, spec)
    ru = w.get("runner_up")
    al = r.get("aligned_raid") or {}
    b = {"id": f"{SM.spec_slug(cls, spec)}-ml-raid", "name": f"{name} — Raid (machine-learning search)",
         "role": "dps", "content": "raid", "tier": "draft", "spec": spec, "generated": TODAY, "derived": "raid",
         "summary": (f"The {name} build the machine-learning talent search found in a full raid (every raid buff and debuff: the group setting) "
                     f"on {TODAY} in the community simulator, in the spec's phase-1 BiS gear and the raid rotation of the entry {w['entry']} "
                     f"(raidsim/ml_talents.py: a random forest trained on simulated builds guides a genetic search over every legal build of the "
                     f"spec; the finalists are raced on fresh seeds and the winner is checked against all its one-move and prerequisite-chain "
                     f"neighbours)."),
         "allocation": al.get("allocation") if al.get("moves") else w["winner"]["allocation"],
         "core": [], "flex": [],
         "notes": [f"Search result (full raid): {w['winner']['split']} at {w['winner']['dps']:.1f} ± {w['winner']['se']:.2f} DPS over "
                   f"{w['winner']['iterations']:,} fights; runner-up "
                   + (f"{ru['split']} ({w['gap_to_runner_up']:+.2%}; {differs_text(w)})" if ru and w.get("gap_to_runner_up") is not None else "none")
                   + f"; {w.get('simulated_builds') or 0:,} builds simulated; certificate: {cert_text(w)}.",
                   f"Simulator numbers are the community's model of the beta ({SI.label(sim_of(r), short=True)} with this project's patches), not in-game "
                   "measurements; the talents are the simulator's answer for this gear and rotation."],
         "open_questions": [f"A machine-searched {name} build: check it against the community's {name} builds at launch."],
         "sources": [SI.URL[SI.kind(sim_of(r))].split(" ")[0]]}
    c = r["compare_raid"]
    if c.get("gain_vs_hand") is not None:
        over = c["gain_vs_hand"] >= MIN_GAIN
        b["notes"].insert(0, f"Against the best hand draft {c['best_hand']} in a full raid, same gear and fights (100,000, one seed): "
                             f"{c['gain_vs_hand']:+.1%}" + (" (over the replacement bar: this build is the spec's raid pick, the hand draft stays as the "
                                                            "alternative)." if over else " (under the replacement bar: the hand draft stays the pick)."))
        if over:
            b["replaces"] = c["best_hand"]
    if al.get("moves"):
        cost = ("the same DPS as" if al["ratio"] >= 1 else f"within {1 - al['ratio']:.2%} of")
        b["notes"].insert(1, f"Where the simulator measured no difference, the points follow {al['target']}: {moves_text(al)} ({cost} the "
                             f"search winner {w['winner']['split']} on one seed, 30,000 fights).")
    pre = winner(r, "prebis-raid")
    if pre:
        same = flat_of(pre["allocation"]) == flat_of(w["winner"]["allocation"])
        b["notes"].append(f"Pre-BiS gear: {pre['split']} at {pre['dps']:.1f} DPS in a full raid"
                          + (" (the same talents)." if same else " (other talents: _reference/dps-rankings.md)."))
    dum = winner(r, "bis-dummy")
    if dum:
        b["notes"].append(f"Alone on the training dummy (only your own buffs) the search's best is {dum['split']} at {dum['dps']:.1f} DPS.")
    return b


def mlt():
    M = _load("ml_talents", HERE / "ml_talents.py")
    M.R.set_game("forever")
    return M, M.R.repo_path(argparse.Namespace(repo=None))


def align(r, data):
    """The full-raid winner with its free points moved toward the spec's best hand draft (else its current best build): one point per step,
    the step that costs least, while the build stays legal and within ALIGN_TOL of the winner on the same seed (full raid)."""
    MLT, repo = mlt()
    cls = r["class"]
    w = r["search"]["bis-raid"]
    c = r.get("compare_raid") or {}
    target = c.get("best_hand") or max(((k, v["dps"]) for k, v in (c.get("dps") or {}).items() if k != "winner"), key=lambda kv: kv[1], default=(None, 0))[0]
    if target not in data:
        return {"target": None, "moves": [], "allocation": w["winner"]["allocation"]}
    space = MLT.Space(cls, r["spec"], protect=w.get("protected") or (), any_split=r.get("any_split", False) and not r.get("deep"))
    H = flat_of(data[target]["allocation"])
    cur = flat_of(w["winner"]["allocation"])
    gear = json.load(open(ROOT / page_gear(r, "bis")["gear"], encoding="utf-8"))["items"]   # the full-raid winner's set
    sim = MLT.Sim(cls, w["entry"], "raid", gear, repo, f"mla-{cls}")
    base_s = sim.run([cur], 5000, 11)[0][0]
    base_c = sim.run([cur], 30000, 12)[0][0]
    moves = []
    for _ in range(51):
        give = [t for t in cur if cur[t] > H.get(t, 0)]
        take = [u for u in H if H[u] > cur.get(u, 0)]
        cands = []
        for t in give:
            for u in take:
                f = dict(cur)
                f[t] -= 1
                f[u] = f.get(u, 0) + 1
                if not f[t]:
                    del f[t]
                if space.valid(f):
                    cands.append((t, u, f))
        if not cands:
            break
        res = sim.run([f for _, _, f in cands], 5000, 11)
        order = sorted(range(len(cands)), key=lambda i: -res[i][0])
        kept = None
        for i in order[:3]:
            if res[i][0] < base_s * (1 - ALIGN_TOL):
                break
            cc = sim.run([cands[i][2]], 30000, 12)[0][0]
            if cc >= base_c * (1 - ALIGN_TOL):
                kept = (i, cc)
                break
        if kept is None:
            break
        t, u, f = cands[kept[0]]
        moves.append({"from": t, "to": u, "ratio": round(kept[1] / base_c, 5)})
        cur = f
    alloc = {tr: [[n, cur[n]] for n in space.by_tree[tr] if cur.get(n)] for tr in space.tree_names}
    return {"target": target, "moves": moves, "allocation": alloc, "split": space.split(cur),
            "ratio": moves[-1]["ratio"] if moves else 1.0}


def moves_text(al):
    """'Burning Soul 2 -> Magic Absorption 2' style: the alignment moves grouped by talent pair."""
    pairs = {}
    for m in al["moves"]:
        pairs[(m["from"], m["to"])] = pairs.get((m["from"], m["to"]), 0) + 1
    return ", ".join(f"{a} → {b}" + (f" ({k} points)" if k > 1 else "") for (a, b), k in pairs.items())


def not_split(r, k="bis-raid"):
    """Why a hybrid's search winner for k is not a split ('' when it is one, or the record is no hybrid's).
    2026-10-15 page audit: the Assassination/Combat hybrid's search reached 30/19/2, the Assassination ML build with two free points
    moved, and replaced the genuine split; the same day the BM/MM hybrid's 7/39/5 replaced the 27/21/3 split. A hybrid's winner with 30
    points in the tree its entry's rotation is built for is that tree's build in that tree's rotation: that tree's search covers it."""
    s = (r.get("search") or {}).get(k) or {}
    if not r["spec"].startswith("Hybrid") or not s.get("winner"):
        return ""
    alloc = s["winner"]["allocation"]
    own = SM.RAID_ENTRY_TREES.get((r["class"], s.get("entry")), set())
    deep = [t for t, v in alloc.items() if sum(r_ for _, r_ in v) >= 30 and t in own]
    return (f"the winner ({'/'.join(str(sum(r_ for _, r_ in v)) for v in alloc.values())}) has 30 points in {deep[0]}, "
            f"the tree of its rotation ({s.get('entry')}): not a split") if deep else ""


def sig_check(r):
    """The full-raid winner's signature-spell check (user rule 2026-10-22, signature_spells.json): the search's own check when its Sim
    kept one for the record's spec, else measured now in the winner's BiS set (raid_signature.measure, 6,000 fights) and kept in the
    record (`signature_check`). None when the check is switched off."""
    import sys as _sys
    _sys.path.insert(0, str(HERE))
    import raid_signature as RSG
    if not RSG.enabled():
        return None
    w = r["search"]["bis-raid"]
    al = (r.get("aligned_raid") or {}).get("allocation") or w["winner"]["allocation"]
    chk = r.get("signature_check")
    if chk and chk.get("spec") == r["spec"] and chk.get("allocation") == al:
        return chk
    MLT, repo = mlt()
    g = page_gear(r, "bis") or {}
    gear = {"items": json.load(open(ROOT / g["gear"], encoding="utf-8"))["items"]} if g.get("gear") else None
    chk, _ = RSG.measure(r["class"], w["entry"], al, repo, MLT.R, MLT.A, iterations=6000, seed=9, gear_json=gear)
    if chk.get("spec") != r["spec"]:   # the record's spec decides (a hybrid's search keeps its pair of trees)
        chk = RSG.recheck(r["class"], r["spec"], chk, al) or chk
    r["signature_check"] = dict(chk, allocation=al)
    save(r)
    return r["signature_check"]


def verdict(r):
    """(write, why): the full-raid winner is written only GAIN_NEW or more ahead of every other build of its full-raid comparison race,
    and (2026-10-22) only when it plays its spec's signature spells in a full raid (sig_check)."""
    why = not_split(r)
    if why:
        return False, why
    chk = sig_check(r)
    if chk is not None and not chk.get("ok"):
        return False, f"fails {SM.spec_name(r['class'], r['spec'])}'s signature-spell check in a full raid ({chk.get('why')}; signature_spells.json)"
    c = r["compare_raid"]["dps"]
    w = c["winner"]["dps"]
    others = {k: v["dps"] for k, v in c.items() if k != "winner" and v.get("dps")}
    # 2026-10-24 audit: a build of ours without its spec's signature talents (the Assassination builds without Mutilate) is no bar
    import raid_signature as RSG
    pb = ROOT / r["class"] / "research/talents/forever/proposed-builds.json"
    byid = {b["id"]: b for b in json.load(open(pb, encoding="utf-8"))["builds"]} if pb.exists() else {}
    others = {k: v for k, v in others.items() if k not in byid or RSG.talents_ok(r["class"], r["spec"], byid[k]["allocation"])}
    if not others:
        return True, ""
    k = max(others, key=others.get)
    if w < others[k] * (1 + GAIN_NEW):
        return False, f"confirms {k} ({w / others[k] - 1:+.2%} in a full raid)"
    return True, ""


def write_builds(classes):
    SB = _load("spec_builds_mod", ROOT / "_reference/data/spec_builds.py")
    MP = None
    for cls in sorted({r["class"] for r in records(classes)}):
        bp = paths.builds_json("forever", cls)
        data = json.load(open(bp, encoding="utf-8"))
        changed, dropped, written = False, set(), []
        removed, added = set(), []   # the change, applied to the file under a lock at the end (builds_io)
        for r in records([cls]):
            if not complete(r):
                print(f"  {cls} {r['spec']}: record not complete, skipped")
                continue
            if "compare_raid" not in r:
                if MP is None:
                    MP = _load("ml_pipeline_mlb", HERE / "ml_pipeline.py")
                    MP.R.set_game("forever")
                r["compare_raid"] = MP.compare(r, MP.R.repo_path(argparse.Namespace(repo=None)), "raid")
                save(r)
            by_id = {b["id"]: b for b in data["builds"]}
            ok, why = verdict(r)
            new = []
            if ok:
                if "aligned_raid" not in r:
                    r["aligned_raid"] = align(r, by_id)
                    if r["aligned_raid"].get("moves"):
                        (r.get("tidied") or {}).pop("bis-raid", None)   # tidy_winners re-checks the aligned build the page shows
                    save(r)
                new.append(make_build(r))
            ids = {b["id"] for b in new}
            # a new raid build supersedes the spec's earlier derived raid builds (derive_raid.py, earlier ML builds of either kind);
            # parse builds of other origin stay
            old = [x for x in data["builds"] if x["id"] in ids
                   or (ok and x.get("derived") == "raid" and x.get("generated") and x.get("role") not in ("tank", "healer")
                       and SM.spec_of(cls, x) == r["spec"] and (not x["id"].endswith("-parse") or x["id"].endswith("-ml-parse")))]
            gone = {x["id"] for x in old} - ids
            data["builds"] = [x for x in data["builds"] if x not in old] + new
            removed |= {x["id"] for x in old}
            added = [x for x in added if x["id"] not in {y["id"] for y in old}] + new
            dropped |= gone
            if gone and ok:
                supersede(cls, r["spec"], gone, new[0]["id"])
            changed = changed or bool(new or gone)
            r["builds"] = {"written": sorted(ids), "superseded": sorted(gone), "date": TODAY, "setting": "raid", **({} if ok else {"why": why})}
            save(r)
            written += [(b["id"], r["search"]["bis-raid"]["entry"]) for b in new]
            print(f"  {cls} {r['spec']}: " + (", ".join(b["id"] for b in new) or "no build") + (f" ({why})" if not ok else "")
                  + (f" (replaces {new[0]['replaces']})" if new and new[0].get("replaces") else "")
                  + (f"; removed {', '.join(sorted(gone))}" if gone else ""))
        if changed:
            BIO.update(cls, remove=removed, add=added)   # locked, on the file as it is now (2026-10-24 audit)
            if dropped:
                drop_from_entries(cls, dropped)
            for bid, entry in written:
                SB.add_to_entry(cls, entry, bid)
                tidy(cls, entry, bid)


def tidy(cls, entry, bid, setting="raid"):
    """filler_audit.py on a written build, in the full raid: a point in a talent whose ability the rotation never casts (Arcane Blast in
    the Frost search winner, 2026-10-02 user report), or in any talent the simulator measures at 0, moves to a DPS gain or a talent that
    helps in a real raid."""
    import subprocess
    r = subprocess.run([sys.executable, str(HERE / "filler_audit.py"), cls, "--spec", entry, "--build", bid, "--setting", setting, "--write"],
                       capture_output=True, text=True, encoding="utf-8", errors="replace", cwd=str(ROOT))
    for ln in r.stdout.strip().splitlines()[-4:]:
        print("    " + ln, flush=True)
    FA = _load("filler_audit_mod", HERE / "filler_audit.py")
    rec_path = FA.record_path(cls, entry, bid)
    if r.returncode == 0 and rec_path.exists():
        FA.apply(json.load(open(rec_path, encoding="utf-8")))


# ------------------------------------------------------------------------------------------------ pages
def page_gear(r, tier):
    """The set the pages show for a tier: the full-raid winner's own set when it plays another entry (ml_pipeline.final, 2026-10-14),
    else the tier's set."""
    g = r.get("gear") or {}
    return g.get(f"{tier}-raid") or g.get(tier)


def gear_names(r, tier):
    g = page_gear(r, tier)
    return [(SLOTS[i] if i < len(SLOTS) else "?", n) for i, n in enumerate((g or {}).get("names") or []) if n]


def gear_text(r, tier):
    return "; ".join(f"{s}: {n}" for s, n in gear_names(r, tier)) or "-"


def shown(r, k):
    """The talents the pages show for a search winner: tidied by filler_audit.py when it moved points (`tidy_winners`), else the
    bis-dummy winner aligned to the hand draft, else the winner itself; {split, allocation}."""
    t = (r.get("tidied") or {}).get(k)
    if t:
        return t
    if k == "bis-raid" and (r.get("aligned_raid") or {}).get("moves"):
        return r["aligned_raid"]   # the same build with its free points following the hand draft (what the build page shows)
    return winner(r, k)


def tf(r, k):
    w = shown(r, k)
    return f"[{w['split']}]({RSH.tf_link(r['class'], flat_of(w['allocation']))})" if w else "-"


def tidy_winners(classes):
    """filler_audit.py on every search winner that holds a talent whose ability it never casts (dummy and full raid, 1,500 fights each);
    the tidied talents are what the rankings and the raid pages show (record key `tidied`; 2026-10-02 user report on unused abilities)."""
    FA = _load("filler_audit_mod", HERE / "filler_audit.py")
    SPm = _load("spell_probe_mod", HERE / "spell_probe.py")
    FA.R.set_game("forever")
    repo = FA.R.repo_path(argparse.Namespace(repo=None))
    for r in records(classes):
        if not complete(r):
            continue
        cls = r["class"]
        abil = {t for t, _, _, _ in SPm.talent_abilities(cls)}
        book = FA.spell_ids(cls)
        trees = FA.R.load_trees(repo, cls)
        done = r.setdefault("tidied", {})
        for k in KEYS:
            if k in done:
                continue
            w = r["search"][k]
            src = (r.get("aligned_raid") or {}).get("allocation") if k == "bis-raid" and (r.get("aligned_raid") or {}).get("moves") else w["winner"]["allocation"]
            al = flat_of(src)
            held = [t for t in al if t in abil]
            setting = "raid" if k.endswith("-raid") else "dummy"
            e = FA.R.SPECS[cls][w["entry"]]
            never = []
            if held:
                cast = {t: 0.0 for t in held}
                for st in ("dummy", "raid"):
                    row = FA.A.bench(e, repo, [{"label": "x", "talents": FA.R.talents_string(trees, al)}], 1500, 1, st, f"tw-{cls}").get("x") or {}
                    for act in row.get("actions") or []:
                        for t in held:
                            if act.get("spellId") in book[t][0]:
                                cast[t] += act.get("casts") or 0
                never = [t for t in held if not cast[t]]
            if not never:
                done[k] = None
                save(r)
                continue
            rec = FA.audit(cls, w["entry"], f"{r['slug']}-{k}", 3000, 12000, alloc=al, setting=setting)
            moved = rec["moves"]
            pts = {t: sum(n for _, n in items) for t, items in rec["allocation"].items()}
            done[k] = ({"allocation": rec["allocation"], "split": "/".join(str(v) for v in pts.values()), "moves": moved,
                        "abilities_never_cast": rec["abilities_never_cast"], "final_seed3": rec["final_seed3"]} if moved else None)
            save(r)
            print(f"  {cls} {r['spec']} {k}: never cast {', '.join(never)}; " + ("; ".join(f"{m['from']} -> {m['to']}" for m in moved) or "no move"), flush=True)


def num(r, k):
    w = winner(r, k)
    return f"{w['dps']:.0f}" if w else "-"


def tier_rows(rs_, tier):
    """Records with a full-raid winner in the tier, best first; a hybrid whose winner is not a split (not_split) is left out: its row
    would show another spec's build under the hybrid's name."""
    return sorted((r for r in rs_ if winner(r, f"{tier}-raid") and not not_split(r, f"{tier}-raid")),
                  key=lambda r: -winner(r, f"{tier}-raid")["dps"])


def table(rs_, tier, src):
    rows = tier_rows(rs_, tier)
    if not rows:
        return ["No results yet.", ""]
    gone = [r for r in rs_ if not_split(r, f"{tier}-raid")]
    best = winner(rows[0], f"{tier}-raid")["dps"]
    dummy = sorted((r for r in rows if winner(r, f"{tier}-dummy")), key=lambda r: -winner(r, f"{tier}-dummy")["dps"])
    rank = {(r["class"], r["spec"]): i for i, r in enumerate(dummy, 1)}
    o = ["| # | Spec | Full raid DPS | Behind the best | Talents |", "|---|---|---|---|---|"]
    for i, r in enumerate(rows, 1):
        d = winner(r, f"{tier}-raid")["dps"]
        pf = ROOT / r["class"] / "raid" / f"{SM.spec_slug(r['class'], r['spec'])}.md"
        nm = f"{SM.spec_name(r['class'], r['spec'])} {r['class'].title()}"
        nm = f"[{nm}]({paths.rel(src, pf)})" if pf.exists() else nm   # 2026-10-25: a spec whose raid page is gone (Beast-Survival) has no link
        o.append(f"| {i} | {nm} | {d:.0f} | {'best' if i == 1 else f'{d / best - 1:+.0%}'} | "
                 f"{tf(r, f'{tier}-raid')} |")
    o += ["", "Ranked by DPS in a full raid (every raid buff and debuff: the group setting the raid pages recommend on)."]
    if gone:
        o += ["", "Not listed: " + "; ".join(
            f"[{SM.spec_name(r['class'], r['spec'])} {r['class'].title()}]({paths.rel(src, ROOT / r['class'] / 'raid' / (SM.spec_slug(r['class'], r['spec']) + '.md'))}) "
            f"(its search in this tier ended at {winner(r, f'{tier}-raid')['split']}, 30 points in the tree its rotation is built for: that "
            "tree's build, not a split; the spec page shows the split)" for r in gone) + "."]
    return o + [""]


def intro():
    return ("Every raid damage spec's DPS in two gear tiers, like WoWSims' Pre-BiS and BiS presets: **Pre-BiS** (" + TIER_TEXT["prebis"] + ") and "
            "**Phase 1 BiS** (" + TIER_TEXT["bis"] + "). Each spec gets its own set per tier (raidsim/gear_tiers.py: the simulator's stat "
            "weights for the spec, the best item per slot, set pieces and trinket pairs raced), and its talents are searched separately for "
            "each tier and setting (raidsim/ml_talents.py: a random forest trained on simulated builds guides a genetic search over every legal "
            "build of the spec; the finalists are raced on fresh seeds and the winner is checked against every one-move and prerequisite-chain "
            "neighbour). *Full raid*: every raid "
            "buff and debuff. 3-minute fights; each number is the winner's average over 100,000 fights (standard error about ±0.1 DPS; "
            "differences under 2-3% are within the model's assumptions). These numbers use each spec's own best gear, so they differ a little "
            "from the spec pages' ranking, which races every build in the project's standard set per spec. Simulations of the community's "
            "model of the beta (with this project's patches; the ElliotWood/Forever fork for searches before 2026-10-18, the official "
            "wowsims/forever since; each spec's record names the commit its search ran on), "
            "not in-game measurements.")


def write_rankings(classes):
    allr = [r for r in records() if r.get("search")]
    o = ["# Raid DPS rankings by gear tier", "",
         f"> Generated by `_reference/data/raidsim/ml_builds.py` on {TODAY} from the machine-learning pipeline's records "
         "(`_reference/data/raidsim/ml/`). Do not hand-edit.", "", intro(), ""]
    for tier in ("bis", "prebis"):
        o += [f"## {TIER_NAME[tier]}", ""] + table(allr, tier, PAGE)
    o += ["## Gear by spec", "", "Each item opens its Wowhead Forever page (with where it drops: the boss and zone, the profession, the quest or "
          "the vendor, when the simulator's item database says) and its enchant; *Open in the simulator* loads the whole character "
          "(gear, enchants, talents, rotation, consumables, buffs) in the community's Forever simulator on the web "
          "(raidsim/gear_links.py). Relics stay as in the project's standard set. Enchants: the standard set's.", ""]
    for r in sorted(allr, key=lambda r: (r["class"], SM.spec_name(r["class"], r["spec"]))):
        o += [f"**{SM.spec_name(r['class'], r['spec'])} {r['class'].title()}**", ""]
        gt = GTAB.table(r["class"], r["spec"])
        if gt:
            sl = GTAB.sim_line(r["class"], r["spec"])
            o += gt + [""] + ([sl, ""] if sl else [])
            continue
        for tier in ("bis", "prebis"):
            g = page_gear(r, tier) or {}
            o.append(f"- {TIER_NAME[tier]} (average item level {g.get('ilvl', '-')}): {gear_text(r, tier)}")
        o.append("")
    o += ["---", f"*Generated by `_reference/data/raidsim/ml_builds.py` on {TODAY}. Do not hand-edit.*"]
    PAGE.write_text("\n".join(o).rstrip("\n") + "\n", encoding="utf-8")
    print(f"wrote {PAGE.relative_to(ROOT).as_posix()}")
    for cls in classes or SM.CLASSES:
        readme = paths.scenario_readme(cls, "raid")
        mine = sorted((r for r in allr if r["class"] == cls), key=lambda r: -((winner(r, "bis-raid") or {}).get("dps") or 0))
        sec = [HEAD, "", f"Pre-BiS and phase-1 BiS DPS of the class's damage specs, each in its own gear, talents searched for each tier and setting "
                          f"([every class]({paths.rel(readme, PAGE)}); generated by `_reference/data/raidsim/ml_builds.py` on {TODAY}; the "
                          f"records: `_reference/data/raidsim/ml/`).", ""]
        if not mine:
            sec += ["No damage spec of this class has a result yet.", ""]
        else:
            sec += ["| Spec | Pre-BiS raid | Pre-BiS dummy | BiS raid | BiS dummy | Rotation (entry) | Search result |", "|---|---|---|---|---|---|---|"]
            for r in mine:
                e = (r["search"].get("bis-raid") or {}).get("entry", "-")
                built = (r.get("builds") or {}).get("written") or []
                why = (r.get("builds") or {}).get("why")
                sec.append(f"| {SM.spec_name(cls, r['spec'])} | {num(r, 'prebis-raid')} | {num(r, 'prebis-dummy')} | {num(r, 'bis-raid')} | "
                           f"{num(r, 'bis-dummy')} | {e} | {', '.join(f'new build {b}' for b in built) or why or '-'} |")
            sec.append("")
        RS.splice_ordered(readme, "raid", HEAD, "\n".join(sec))
    print(f"wrote the '{HEAD[3:]}' section of {len(classes or SM.CLASSES)} research raid READMEs")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("classes", nargs="*")
    ap.add_argument("--builds", action="store_true")
    ap.add_argument("--rank", action="store_true")
    ap.add_argument("--tidy-winners", action="store_true", help="filler_audit.py on the search winners that hold an ability they never cast")
    a = ap.parse_args()
    if a.builds:
        write_builds(a.classes)
    if a.tidy_winners:
        tidy_winners(a.classes)
    if a.rank or not (a.builds or a.tidy_winners):
        # the gear's Wowhead links and the simulator share links first (they need the bench); a failure keeps the last file
        import subprocess
        g = subprocess.run([sys.executable, str(HERE / "gear_links.py"), *a.classes, "--write"], capture_output=True, text=True,
                           encoding="utf-8", errors="replace", cwd=str(ROOT))
        print((g.stdout.strip().splitlines() or ["gear_links.py: no output"])[-1] if not g.returncode else f"gear_links.py failed: {g.stderr[-400:]}")
        write_rankings(a.classes)


if __name__ == "__main__":
    main()
