"""The blind-spot check's follow-ups (2026-11-17; round 1 ran them as scratch scripts, pvp-plan.md's log; round 2 runs this):

    python _reference/data/duellab/blind_followups.py improve [--workers 10]       # -> results-<date>.json "improved"
    python _reference/data/duellab/blind_followups.py battleground [--workers 10]  # -> "battleground"

improve: per tree of duellab/blind-spots.json with rows that beat the winner on seed 3 and again on seed 4 (`confirmed`), those
put-backs applied together, the largest seed-3 gain first, each paid from the current build's cheapest ranks (blind_spots.put_back
with the winner's removal costs; one that would undo an earlier one is skipped); every prefix raced on seeds 3 and 4 (240 a matchup).
The best prefix by the two seeds' mean J is adopted when it beats the winner on both by the bar (0.005).

battleground: per tree, from its duel build (the adopted improved build, else the winner), the talents whose value lies outside a duel
(an escape, a defensive cooldown, control, mobility, control resistance, stealth, a dispel, anti-healing, avoidance: the class audits'
kinds, or a high rating) that cost at most 2 points alone, the high-rated first, then medium, then the rest by their own cost, put back
one at a time: each step races every tree's next candidate together in two payments (the check's costs, the floored ones) on seed 3
(240 a matchup); a candidate stays when the whole version is within BUDGET of the duel build. Judged by duels only.

The record: duellab/results-<date>.json (the newest one is the research pages' and the report's).
"""
import argparse
import concurrent.futures as CF
import datetime
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import blind_spots as B  # noqa: E402

sys.path.insert(0, str(HERE.parent))
import render_start_here as RS  # noqa: E402

BUDGET = 0.010
ALONE = -0.020
STEPS = 6
OUTSIDE = {"escape", "defensive", "stun", "kite", "stick", "move", "resist", "stealth", "dispel", "antiheal", "avoid"}
TIER = {"high": 0, "medium": 1, "low": 2, "": 3}


def record_path(date=None):
    return HERE / f"results-{date or datetime.date.today().isoformat()}.json"


def load_out(p):
    return json.loads(p.read_text(encoding="utf-8")) if p.exists() else {"date": datetime.date.today().isoformat()}


def save_out(p, d):
    tmp = p.with_name(p.name + ".tmp")
    tmp.write_text(json.dumps(d, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    tmp.replace(p)


def info(r):
    kinds, tier = set(), ""
    for s in r["sources"]:
        if s.startswith("stats model:"):
            for w in (x.strip() for x in s.split(":", 1)[1].split(",")):
                if w in TIER and w:
                    tier = tier or w
                elif w:
                    kinds.add(w)
    return kinds, tier


# ------------------------------------------------------------------------------------------------ improve
def chain(e):
    cls, tree = e["class"], e["tree"]
    T = B.Trees(cls)
    protect = B.signature_talents(cls, tree, T)
    gains = sorted([r for r in e["rows"] if r.get("confirmed")], key=lambda r: -r["dJ"])
    cur, steps, added = dict(e["winner"]), [], []
    for r in gains:
        n, rank = r["talent"], r["rank"]
        if cur.get(n, 0) >= rank:
            continue
        pb, why = B.put_back(T, cur, n, rank, e["costs"], tree, protect=[p for p in protect if p != n] + [x[0] for x in added], prefer=set())
        pb = [(desc, al) for desc, al in pb if all(al.get(t, 0) >= k for t, k in added)]
        if not pb:
            continue
        cur = pb[0][1]
        added.append((n, rank))
        steps.append((f"{n} {rank}", dict(cur)))
    return steps


def improve(d, pool):
    plan = {k: (e, st) for k, e in d.items() if (st := chain(e))}
    out = {}
    if not plan:
        return out
    seeds = {}
    for seed in (3, 4):
        cands = []
        for k, (e, st) in plan.items():
            cands.append((f"{k}|winner", e["class"], e["winner"]))
            cands += [(f"{k}|{i}", e["class"], al) for i, (lab, al) in enumerate(st)]
        seeds[seed] = B.evaluate(cands, 240, seed, pool)
    for k, (e, st) in plan.items():
        s3, s4 = seeds[3], seeds[4]
        means = [(s3[f"{k}|{i}"]["J"] + s4[f"{k}|{i}"]["J"]) / 2 for i in range(len(st))]
        i = max(range(len(st)), key=lambda j: means[j])
        ok = s3[f"{k}|{i}"]["J"] - s3[f"{k}|winner"]["J"] > B.BAR and s4[f"{k}|{i}"]["J"] - s4[f"{k}|winner"]["J"] > B.BAR
        al = st[i][1]
        out[k] = {"steps": [lab for lab, _ in st], "best": i, "adopt": ok, "added": [lab for lab, _ in st[:i + 1]], "allocation": al,
                  "link": RS.tf_link(e["class"], al), "J3": round(s3[f"{k}|{i}"]["J"], 4), "win3": round(s3[f"{k}|{i}"]["win"], 4),
                  "win4": round(s4[f"{k}|{i}"]["win"], 4), "dwin3": round(s3[f"{k}|{i}"]["win"] - s3[f"{k}|winner"]["win"], 4),
                  "dwin4": round(s4[f"{k}|{i}"]["win"] - s4[f"{k}|winner"]["win"], 4), "by": s3[f"{k}|{i}"]["by"]}
        print(f"{k}: {' + '.join(out[k]['added'])}: win {out[k]['win3']:.1%} ({out[k]['dwin3'] * 100:+.1f}) seed 3, "
              f"{out[k]['win4']:.1%} ({out[k]['dwin4'] * 100:+.1f}) seed 4 -> {'ADOPT' if ok else 'keep the winner'}", flush=True)
    return out


# ------------------------------------------------------------------------------------------------ battleground
def candidates(e):
    out = []
    for r in e["rows"]:
        kinds, tier = info(r)
        if not (kinds & OUTSIDE or tier == "high") or r["dwin"] < ALONE:
            continue
        out.append((TIER[tier], -r["dwin"], r["talent"], r["rank"]))
    return [(t, rk) for _, _, t, rk in sorted(out)]


def battleground(d, imp, pool):
    st = {}
    for k, e in d.items():
        im = imp.get(k) if (imp.get(k) or {}).get("adopt") else None
        T = B.Trees(e["class"])
        st[k] = {"e": e, "T": T, "cur": dict(im["allocation"] if im else e["winner"]),
                 "base": (im["J3"], im["win3"]) if im else (e["J"], e["win"]), "added": [], "skipped": [], "todo": candidates(e),
                 "protect": B.signature_talents(e["class"], e["tree"], T) + ([x.rsplit(" ", 1)[0] for x in im["added"]] if im else []),
                 "from": "improved" if im else "winner", "win": None, "J": None, "by": None}
    for step in range(STEPS):
        builds, meta = [], {}
        for k, s in st.items():
            while s["todo"]:
                n, rank = s["todo"].pop(0)
                if s["cur"].get(n, 0) >= rank:
                    continue
                prot = [p for p in s["protect"] if p != n] + [a.rsplit(" ", 1)[0] for a in s["added"]]
                opts, seen = [], set()
                for costs in (s["e"]["costs"], B.floored_costs(s["e"]["costs"], s["e"].get("inert", []), s["cur"])):
                    pb, _ = B.put_back(s["T"], s["cur"], n, rank, costs, s["e"]["tree"], protect=prot, prefer=set())
                    for _, al in pb[:1]:
                        key = tuple(sorted(al.items()))
                        if key not in seen:
                            seen.add(key)
                            opts.append(al)
                if not opts:
                    s["skipped"].append(f"{n} (no legal payment)")
                    continue
                for i, al in enumerate(opts):
                    builds.append((f"{k}|{n}|{i}", s["e"]["class"], al))
                    meta[f"{k}|{n}|{i}"] = (k, n, rank, al)
                break
        if not builds:
            break
        res = B.evaluate(builds, B.RACE[0], B.RACE[1], pool)
        best = {}
        for lb, (k, n, rank, al) in meta.items():
            if k not in best or res[lb]["J"] > res[best[k]]["J"]:
                best[k] = lb
        for k, lb in best.items():
            s, x = st[k], res[lb]
            _, n, rank, al = meta[lb]
            if s["base"][1] - x["win"] <= BUDGET:
                s.update(cur=al, win=x["win"], J=x["J"], by=x["by"])
                s["added"].append(f"{n} {rank}")
            else:
                s["skipped"].append(f"{n} ({(x['win'] - s['base'][1]) * 100:+.1f} with the others)")
    out = {}
    for k, s in st.items():
        if not s["added"]:
            continue
        out[k] = {"added": s["added"], "skipped": s["skipped"], "allocation": s["cur"], "link": RS.tf_link(s["e"]["class"], s["cur"]),
                  "win": round(s["win"], 4), "dwin": round(s["win"] - s["base"][1], 4), "J": round(s["J"], 4),
                  "dJ": round(s["J"] - s["base"][0], 4), "by": s["by"], "from": s["from"]}
        print(f"{k}: + {', '.join(s['added'])}: win {s['win']:.1%} ({out[k]['dwin'] * 100:+.1f})", flush=True)
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("step", choices=("improve", "battleground"))
    ap.add_argument("--workers", type=int, default=10)
    ap.add_argument("--date", help="the record's date (default today)")
    ap.add_argument("--only", nargs="*", default=[], help="class:tree keys to redo; the record keeps the other trees' results")
    a = ap.parse_args()
    d = json.loads(B.RECORD.read_text(encoding="utf-8"))["trees"]
    if a.only:   # 2026-11-18: one tree again (the Holy paladin after the check's gear fix) without the other 26
        d = {k: v for k, v in d.items() if k in a.only}
    p = record_path(a.date)
    out = load_out(p)
    key = "improved" if a.step == "improve" else "battleground"
    keep = {k: v for k, v in (out.get(key) or {}).items() if a.only and k not in a.only}
    with CF.ProcessPoolExecutor(max_workers=a.workers) as pool:
        if a.step == "improve":
            new = improve(d, pool)
        else:
            new = battleground(d, out.get("improved") or {}, pool)
    out[key] = dict(sorted({**keep, **new}.items()))
    save_out(p, out)
    print(f"wrote {p}")


if __name__ == "__main__":
    main()
