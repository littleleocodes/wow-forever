"""The machine-learning pipeline's results as builds and pages (2026-10-01, user request: a systematic machine-learning optimisation of
every raid damage spec, and "DPS ranking for Pre-bis as well as best in slot armor. Similar to what WoWSims does").

    python _reference/data/raidsim/ml_builds.py [classes] --builds     # winners into proposed-builds.json (then validate + render)
    python _reference/data/raidsim/ml_builds.py [classes] --rank       # _reference/dps-rankings.md + "## DPS by gear tier" of the research READMEs

--builds, for every spec whose record (`raidsim/ml/<class>-<spec slug>.json`, written by ml_pipeline.py) is complete:
- the training-dummy winner in the spec's phase-1 BiS set becomes the spec's derived raid build `<spec page slug>-ml-raid` (🔬, `derived:
  raid`) when the record's comparison race (100,000 fights, one fresh seed, BiS set) has it 0.5% or more ahead of every build raced
  there (the spec's current best and its two best hand drafts); otherwise the search confirms the current pick and no build is written
  (the first finished specs tied: Balance exactly, Feral within 0.1%). It carries `replaces` when it beats the spec's best hand draft
  there by 2% or more (the user's rule: the hand draft stays
  as the alternative; the pages enforce the rule on the race numbers, render_modes.DERIVED_BAR). It supersedes the spec's earlier
  derived raid build (derive_raid.py's local search; parse builds stay), which is removed and marked "superseded" in derived-raid.json
  so a later `derive_raid.py --write` does not bring it back. It joins the specs.json builds of the entry it won in.
- when the full-raid winner is another build, beats the dummy winner by 2% or more in a full raid and every existing parse build of the
  spec by 0.5% or more (all raced on one fresh seed, 100,000 fights, the BiS set), it becomes the spec's parse build
  `<spec page slug>-ml-parse` (the Arms lesson: a full raid values talents differently), whether or not a raid build is written.
- before that, points the simulator cannot tell apart follow the hand draft (`align`): a search winner picks arbitrarily among talents
  that do nothing on the dummy (Burning Soul and Magic Absorption measure exactly the same with common random numbers), so every point
  is moved toward the spec's best hand draft (else its current best build) while the build stays legal and within 0.03% of the winner
  on one seed (5,000 fights to screen the moves, the kept move confirmed over 30,000).
Every written build then goes through filler_audit.py (`tidy`: zero-value points and talents whose ability the rotation never casts move
to a DPS gain or a useful talent; 2026-10-02, after the Frost winner kept a never-cast Arcane Blast for tier gating).
The pages need race numbers for the new builds: re-race their entries afterwards (raidsim/run.py, or rebuild.py --steps raid,adopt,regen).
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
import paths  # noqa: E402
import readme_sections as RS  # noqa: E402
import render_start_here as RSH  # noqa: E402
import spec_modes as SM  # noqa: E402
from filelock import locked  # noqa: E402
from fmt_json import dumps  # noqa: E402


def _load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


OUT = HERE / "ml"
PAGE = ROOT / "_reference" / "dps-rankings.md"
DERIVED_RAID = ROOT / "_reference" / "data" / "derived-raid.json"
TODAY = datetime.date.today().isoformat()
MIN_GAIN = 0.02     # the user's replacement bar (hand draft -> derived build; dummy winner -> parse build)
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


def parse_check(r, data):
    """The full-raid winner against the dummy winner and the spec's existing parse builds in the full raid (BiS set, one fresh seed,
    100,000 fights), each in its entry (a parse build's entry: the first specs.json entry listing it, the record's entries first)."""
    MLT, repo = mlt()
    cls = r["class"]
    gear = json.load(open(ROOT / r["gear"]["bis"]["gear"], encoding="utf-8"))["items"]
    rows = {k: (r["search"][k]["entry"], flat_of(r["search"][k]["winner"]["allocation"])) for k in ("bis-dummy", "bis-raid")}
    specs = json.load(open(HERE / "specs.json", encoding="utf-8")).get(cls, {})
    for b in data.values():
        if b["id"].endswith("-parse") and not b["id"].endswith("-ml-parse") and SM.spec_of(cls, b) == r["spec"]:
            ents = [e for e in list(r["entries"]) + sorted(specs) if isinstance(specs.get(e), dict) and b["id"] in specs[e].get("builds", [])]
            if ents:
                rows[b["id"]] = (ents[0], flat_of(b["allocation"]))
    out = {}
    for k, (entry, al) in rows.items():
        sim = MLT.Sim(cls, entry, "raid", gear, repo, f"mlb-{cls}")
        d, sd = sim.run([al], 100000, 9)[0]
        out[k] = {"entry": entry, "dps": round(d, 2), "se": round(sd / math.sqrt(100000), 3)}
    out["gain"] = round(out["bis-raid"]["dps"] / out["bis-dummy"]["dps"] - 1, 4) if out["bis-dummy"]["dps"] else None
    others = [k for k in out if k not in ("bis-dummy", "bis-raid", "gain")]
    out["vs_parse"] = round(out["bis-raid"]["dps"] / max(out[k]["dps"] for k in others) - 1, 4) if others else None
    return out


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


def make_build(r, kind):
    cls, spec = r["class"], r["spec"]
    s = r["search"]
    w = s["bis-dummy" if kind == "raid" else "bis-raid"]
    name = SM.spec_name(cls, spec)
    where = "on the training dummy (only your own buffs)" if kind == "raid" else "in a full raid (every raid buff and debuff)"
    ru = w.get("runner_up")
    b = {"id": f"{SM.spec_slug(cls, spec)}-ml-{'raid' if kind == 'raid' else 'parse'}",
         "name": f"{name} — {'Raid' if kind == 'raid' else 'Full raid (parse)'} (machine-learning search)",
         "role": "dps", "content": "raid", "tier": "draft", "spec": spec, "generated": TODAY, "derived": "raid",
         "summary": (f"The {name} build the machine-learning talent search found {where} on {TODAY} in the community simulator, in the spec's "
                     f"phase-1 BiS gear and the rotation of the entry {w['entry']} (raidsim/ml_talents.py: a random forest trained on simulated "
                     f"builds guides a genetic search over every legal build of the spec; the finalists are raced on fresh seeds and the winner "
                     f"is checked against all its one-move and prerequisite-chain neighbours)."),
         "allocation": (r.get("aligned") or {}).get("allocation") if kind == "raid" and r.get("aligned") else w["winner"]["allocation"],
         "core": [], "flex": [],
         "notes": [f"Search result: {w['winner']['split']} at {w['winner']['dps']:.1f} ± {w['winner']['se']:.2f} DPS over "
                   f"{w['winner']['iterations']:,} fights; runner-up "
                   + (f"{ru['split']} ({w['gap_to_runner_up']:+.2%}; {differs_text(w)})" if ru else "none")
                   + f"; {w['simulated_builds']:,} builds simulated; certificate: {cert_text(w)}.",
                   "Simulator numbers are the community's model of the beta (ElliotWood/Forever 40be98e with this project's patches), not in-game "
                   "measurements; the talents are the simulator's answer for this gear and rotation."],
         "open_questions": [f"A machine-searched {name} build: check it against the community's {name} builds at launch."],
         "sources": ["https://github.com/ElliotWood/Forever"]}
    if kind == "raid":
        c = r["compare"]
        if c.get("gain_vs_hand") is not None:
            over = c["gain_vs_hand"] >= MIN_GAIN
            b["notes"].insert(0, f"Against the best hand draft {c['best_hand']} in the same gear and fights (100,000, one seed): "
                                 f"{c['gain_vs_hand']:+.1%}" + (" (over the 2% bar: this build is the spec's raid pick, the hand draft stays as the "
                                                                "alternative)." if over else " (under the 2% bar: the hand draft stays the pick)."))
            if over:
                b["replaces"] = c["best_hand"]
        al = r.get("aligned") or {}
        if al.get("moves"):
            cost = ("the same DPS as" if al["ratio"] >= 1 else f"within {1 - al['ratio']:.2%} of")
            b["notes"].insert(1, f"Where the simulator measured no difference, the points follow {al['target']}: {moves_text(al)} ({cost} the "
                                 f"search winner {w['winner']['split']} on one seed, 30,000 fights).")
        pre = winner(r, "prebis-dummy")
        same = flat_of(pre["allocation"]) == flat_of(w["winner"]["allocation"])
        b["notes"].append(f"Pre-BiS gear: {pre['split']} at {pre['dps']:.1f} DPS on the dummy"
                          + (" (the same talents)." if same else " (other talents: _reference/dps-rankings.md)."))
    return b


def mlt():
    M = _load("ml_talents", HERE / "ml_talents.py")
    M.R.set_game("forever")
    return M, M.R.repo_path(argparse.Namespace(repo=None))


def align(r, data):
    """The dummy winner with its free points moved toward the spec's best hand draft (else its current best build): one point per step,
    the step that costs least, while the build stays legal and within ALIGN_TOL of the winner on the same seed."""
    MLT, repo = mlt()
    cls = r["class"]
    w = r["search"]["bis-dummy"]
    target = r["compare"].get("best_hand") or r.get("best")
    if target not in data:
        return {"target": None, "moves": [], "allocation": w["winner"]["allocation"]}
    space = MLT.Space(cls, r["spec"], protect=w.get("protected") or (), any_split=r.get("any_split", False))
    H = flat_of(data[target]["allocation"])
    cur = flat_of(w["winner"]["allocation"])
    gear = json.load(open(ROOT / r["gear"]["bis"]["gear"], encoding="utf-8"))["items"]
    sim = MLT.Sim(cls, w["entry"], "dummy", gear, repo, f"mla-{cls}")
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
            c = sim.run([cands[i][2]], 30000, 12)[0][0]
            if c >= base_c * (1 - ALIGN_TOL):
                kept = (i, c)
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


def verdict(r):
    """(write, why): an ML winner is written only GAIN_NEW or more ahead of every other build of its comparison race."""
    c = r["compare"]["dps"]
    w = c["winner"]["dps"]
    others = {k: v["dps"] for k, v in c.items() if k != "winner" and v.get("dps")}
    if not others:
        return True, ""
    k = max(others, key=others.get)
    if w < others[k] * (1 + GAIN_NEW):
        return False, f"confirms {k} ({w / others[k] - 1:+.2%})"
    return True, ""


def write_builds(classes):
    SB = _load("spec_builds_mod", ROOT / "_reference/data/spec_builds.py")
    for cls in sorted({r["class"] for r in records(classes)}):
        bp = paths.builds_json("forever", cls)
        data = json.load(open(bp, encoding="utf-8"))
        changed, dropped = False, set()
        for r in records([cls]):
            if not complete(r):
                print(f"  {cls} {r['spec']}: record not complete, skipped")
                continue
            by_id = {b["id"]: b for b in data["builds"]}
            ok, why = verdict(r)
            new = []
            if ok:
                if "aligned" not in r:
                    r["aligned"] = align(r, by_id)
                    save(r)
                new.append(make_build(r, "raid"))
            if "parse" not in r:
                r["parse"] = parse_check(r, by_id)
                save(r)
            p = r["parse"]
            differs = flat_of(r["search"]["bis-raid"]["winner"]["allocation"]) != flat_of(r["search"]["bis-dummy"]["winner"]["allocation"])
            if differs and (p["gain"] or 0) >= MIN_GAIN and (p.get("vs_parse") is None or p["vs_parse"] >= GAIN_NEW):
                pb = make_build(r, "parse")
                pb["notes"].insert(0, f"In a full raid it does {p['gain']:+.1%} over the training-dummy winner ({p['bis-raid']['dps']:.1f} vs "
                                      f"{p['bis-dummy']['dps']:.1f} DPS, 100,000 fights, one seed, BiS gear)"
                                      + (f" and {p['vs_parse']:+.1%} over the spec's best earlier parse build." if p.get("vs_parse") is not None else "."))
                new.append(pb)
            ids = {b["id"] for b in new}
            # a new raid build supersedes the spec's earlier derived raid builds (derive_raid.py, an earlier ML run); parse builds of
            # other origin stay; an earlier ML build of the spec goes whenever this run did not write its kind again
            old = [x for x in data["builds"] if x["id"] in ids
                   or (ok and x.get("derived") == "raid" and x.get("generated") and x.get("role") != "tank" and SM.spec_of(cls, x) == r["spec"]
                       and not x["id"].endswith("-parse"))
                   or (x["id"].endswith(("-ml-raid", "-ml-parse")) and SM.spec_of(cls, x) == r["spec"])]
            gone = {x["id"] for x in old} - ids
            data["builds"] = [x for x in data["builds"] if x not in old] + new
            dropped |= gone
            if gone and ok:
                supersede(cls, r["spec"], gone, new[0]["id"])
            changed = changed or bool(new or gone)
            r["builds"] = {"written": sorted(ids), "superseded": sorted(gone), "date": TODAY, **({} if ok else {"why": why})}
            save(r)
            print(f"  {cls} {r['spec']}: " + (", ".join(b["id"] for b in new) or "no build") + (f" ({why})" if not ok else "")
                  + (f" (replaces {new[0]['replaces']})" if new and new[0].get("replaces") else "")
                  + (f"; parse: {p['gain']:+.1%} over the dummy winner in a full raid" + (f", {p['vs_parse']:+.1%} over the best parse build" if p.get("vs_parse") is not None else ""))
                  + (f"; removed {', '.join(sorted(gone))}" if gone else ""))
        if changed:
            bp.write_text(dumps(data) + "\n", encoding="utf-8")
            if dropped:
                drop_from_entries(cls, dropped)
            for r in records([cls]):
                for bid in (r.get("builds") or {}).get("written", []):
                    k = "bis-raid" if bid.endswith("-parse") else "bis-dummy"
                    SB.add_to_entry(cls, r["search"][k]["entry"], bid)
                    tidy(cls, r["search"][k]["entry"], bid)


def tidy(cls, entry, bid):
    """filler_audit.py on a written build: a point in a talent whose ability the rotation never casts (Arcane Blast in the Frost search
    winner, 2026-10-02 user report), or in any talent the simulator measures at 0, moves to a DPS gain or a talent that helps in a real raid."""
    import subprocess
    r = subprocess.run([sys.executable, str(HERE / "filler_audit.py"), cls, "--spec", entry, "--build", bid, "--write"],
                       capture_output=True, text=True, encoding="utf-8", errors="replace", cwd=str(ROOT))
    for ln in r.stdout.strip().splitlines()[-4:]:
        print("    " + ln, flush=True)
    FA = _load("filler_audit_mod", HERE / "filler_audit.py")
    rec_path = FA.record_path(cls, entry, bid)
    if r.returncode == 0 and rec_path.exists():
        FA.apply(json.load(open(rec_path, encoding="utf-8")))


# ------------------------------------------------------------------------------------------------ pages
def gear_names(r, tier):
    g = (r.get("gear") or {}).get(tier)
    return [(SLOTS[i] if i < len(SLOTS) else "?", n) for i, n in enumerate((g or {}).get("names") or []) if n]


def gear_text(r, tier):
    return "; ".join(f"{s}: {n}" for s, n in gear_names(r, tier)) or "-"


def shown(r, k):
    """The talents the pages show for a search winner: tidied by filler_audit.py when it moved points (`tidy_winners`), else the
    bis-dummy winner aligned to the hand draft, else the winner itself; {split, allocation}."""
    t = (r.get("tidied") or {}).get(k)
    if t:
        return t
    if k == "bis-dummy" and (r.get("aligned") or {}).get("moves"):
        return r["aligned"]   # the same build with its free points following the hand draft (what the build page shows)
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
            src = (r.get("aligned") or {}).get("allocation") if k == "bis-dummy" and (r.get("aligned") or {}).get("moves") else w["winner"]["allocation"]
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
    return sorted((r for r in rs_ if winner(r, f"{tier}-dummy")), key=lambda r: -winner(r, f"{tier}-dummy")["dps"])


def table(rs_, tier, src):
    rows = tier_rows(rs_, tier)
    if not rows:
        return ["No results yet.", ""]
    best = winner(rows[0], f"{tier}-dummy")["dps"]
    raid = sorted((r for r in rows if winner(r, f"{tier}-raid")), key=lambda r: -winner(r, f"{tier}-raid")["dps"])
    rank = {(r["class"], r["spec"]): i for i, r in enumerate(raid, 1)}
    o = ["| # | Spec | Training dummy | Behind the best | Full raid | Full-raid rank | Talents: dummy / full raid |", "|---|---|---|---|---|---|---|"]
    for i, r in enumerate(rows, 1):
        d = winner(r, f"{tier}-dummy")["dps"]
        page = paths.rel(src, ROOT / r["class"] / "raid" / f"{SM.spec_slug(r['class'], r['spec'])}.md")
        o.append(f"| {i} | [{SM.spec_name(r['class'], r['spec'])} {r['class'].title()}]({page}) | {d:.0f} | {'best' if i == 1 else f'{d / best - 1:+.0%}'} | "
                 f"{num(r, f'{tier}-raid')} | {rank.get((r['class'], r['spec']), '-')} | {tf(r, f'{tier}-dummy')} / {tf(r, f'{tier}-raid')} |")
    return o + ["", "Ranked by training-dummy DPS (the project's ranking setting); *full-raid rank* is the spec's place when every raid buff "
                    "and debuff is up, where the physical specs that live on raid buffs (warriors, hunters, Enhancement, Retribution) climb.", ""]


def intro():
    return ("Every raid damage spec's DPS in two gear tiers, like WoWSims' Pre-BiS and BiS presets: **Pre-BiS** (" + TIER_TEXT["prebis"] + ") and "
            "**Phase 1 BiS** (" + TIER_TEXT["bis"] + "). Each spec gets its own set per tier (raidsim/gear_tiers.py: the simulator's stat "
            "weights for the spec, the best item per slot, set pieces and trinket pairs raced), and its talents are searched separately for "
            "each tier and setting (raidsim/ml_talents.py: a random forest trained on simulated builds guides a genetic search over every legal "
            "build of the spec; the finalists are raced on fresh seeds and the winner is checked against every one-move and prerequisite-chain "
            "neighbour). *Training dummy*: a boss-level dummy with only your own buffs (the project's ranking setting). *Full raid*: every raid "
            "buff and debuff. 3-minute fights; each number is the winner's average over 100,000 fights (standard error about ±0.1 DPS; "
            "differences under 2-3% are within the model's assumptions). These numbers use each spec's own best gear, so they differ a little "
            "from the spec pages' ranking, which races every build in the project's standard set per spec. Simulations of the community's "
            "model of the beta (ElliotWood/Forever 40be98e with this project's patches), not in-game measurements.")


def write_rankings(classes):
    allr = [r for r in records() if r.get("search")]
    o = ["# Raid DPS rankings by gear tier", "",
         f"> Generated by `_reference/data/raidsim/ml_builds.py` on {TODAY} from the machine-learning pipeline's records "
         "(`_reference/data/raidsim/ml/`). Do not hand-edit.", "", intro(), ""]
    for tier in ("bis", "prebis"):
        o += [f"## {TIER_NAME[tier]}", ""] + table(allr, tier, PAGE)
    o += ["## Gear by spec", "", "Relics stay as in the project's standard set. Enchants: the standard set's.", ""]
    for r in sorted(allr, key=lambda r: (r["class"], SM.spec_name(r["class"], r["spec"]))):
        o += [f"**{SM.spec_name(r['class'], r['spec'])} {r['class'].title()}**", ""]
        for tier in ("bis", "prebis"):
            g = (r.get("gear") or {}).get(tier) or {}
            o.append(f"- {TIER_NAME[tier]} (average item level {g.get('ilvl', '-')}): {gear_text(r, tier)}")
        o.append("")
    o += ["---", f"*Generated by `_reference/data/raidsim/ml_builds.py` on {TODAY}. Do not hand-edit.*"]
    PAGE.write_text("\n".join(o).rstrip("\n") + "\n", encoding="utf-8")
    print(f"wrote {PAGE.relative_to(ROOT).as_posix()}")
    for cls in classes or SM.CLASSES:
        readme = paths.scenario_readme(cls, "raid")
        mine = sorted((r for r in allr if r["class"] == cls), key=lambda r: -((winner(r, "bis-dummy") or winner(r, "bis-dummy-1") or {}).get("dps") or 0))
        sec = [HEAD, "", f"Pre-BiS and phase-1 BiS DPS of the class's damage specs, each in its own gear, talents searched for each tier and setting "
                          f"([every class]({paths.rel(readme, PAGE)}); generated by `_reference/data/raidsim/ml_builds.py` on {TODAY}; the "
                          f"records: `_reference/data/raidsim/ml/`).", ""]
        if not mine:
            sec += ["No damage spec of this class has a result yet.", ""]
        else:
            sec += ["| Spec | Pre-BiS dummy | Pre-BiS raid | BiS dummy | BiS raid | Rotation (entry) | Search result |", "|---|---|---|---|---|---|---|"]
            for r in mine:
                e = (r["search"].get("bis-dummy") or r["search"].get("bis-dummy-1") or {}).get("entry", "-")
                built = (r.get("builds") or {}).get("written") or []
                why = (r.get("builds") or {}).get("why")
                sec.append(f"| {SM.spec_name(cls, r['spec'])} | {num(r, 'prebis-dummy')} | {num(r, 'prebis-raid')} | {num(r, 'bis-dummy')} | "
                           f"{num(r, 'bis-raid')} | {e} | {', '.join(f'new build {b}' for b in built) or why or '-'} |")
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
        write_rankings(a.classes)


if __name__ == "__main__":
    main()
