"""Profile duels to find AI defects (duellab validation, 2026-11-14): what each side does, where its time goes, and what it wastes.

    python _reference/data/duellab/duel_profile.py rogue:warrior priest:mage [--n 20] [--seed 1] [--builds field|<cls>=<ref>,...]

A pair is two classes; each plays its field build (pvp_field.FIELD) unless --builds names another (`rogue=community:tf-hemo`). Per side
it prints:
- damage and healing per duel, by spell, and casts per duel;
- seconds per duel controlled, casting, on the global cooldown, and idle with the global cooldown free and nothing chosen. Idle time
  is split by state: wanding, swinging in melee, out of reach (30+ yards), out of mana (under 5%), or other. "Other" holds energy
  and rage starvation and a stealthed approach, so it is a lead, not a verdict;
- control taken by name, trinket uses, interrupts taken.
Waste found in the logs:
- control cast into an immunity ("immune to X") or into diminishing returns;
- damage into an immunity;
- the side's own control broken by its own damage ("X broken by Y"). In a duel every hit on a side comes from the other one, so a
  broken Blind is the rogue's own doing. Some breaks are meant: a Frost Nova shattered, a fear with dots up.
Use it on the matrix's most lopsided matchups (pvp_field.py --matrix), then read a log of the worst (duel_run.py --log 1).
"""
import argparse
import collections
import concurrent.futures as CF
import pathlib
import re
import statistics
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import duel_run as DR  # noqa: E402  (first: it sets the path)
import duel as D  # noqa: E402
import pvp_field as PF  # noqa: E402

EPS = 1e-9
LINE = re.compile(r"^\s*([\d.]+)s ([AB]) (.*)$")
IMMUNE_CC = re.compile(r"^immune to (.+?)( \(diminishing returns\))?$")
BROKEN = re.compile(r"^(.+?) broken by (.+)$")
IMMUNE_DMG = re.compile(r"^(.+?) immune$")


def _prof():
    return {"inactive": 0.0, "controlled": 0.0, "casting": 0.0, "gcd": 0.0, "idle_wanding": 0.0, "idle_swinging": 0.0,
            "idle_far": 0.0, "idle_oom": 0.0, "idle_other": 0.0}


def profiled_decide(self, s, t):
    """Duel.decide with the time bookkeeping (the same decisions, in the same order)."""
    f, st = s.fight, s._prof
    if t < s.inactive_until:
        st["inactive"] += D.T.DT
        self.act(s, s.ai.while_inactive(self, s, s.foe))
        return
    if s.controlled(t):
        st["controlled"] += D.T.DT
        self.act(s, s.ai.while_controlled(self, s, s.foe))
        return
    if f.casting or f.channel:
        st["casting"] += D.T.DT
        self.act(s, s.ai.while_casting(self, s, s.foe))
        return
    self.act(s, s.ai.off_gcd(self, s, s.foe))
    if s.controlled(t) or f.casting or f.channel:
        return
    if t + EPS < s.p.gcd_until:
        st["gcd"] += D.T.DT
        return
    a = s.ai.decide(self, s, s.foe)
    if a is None:
        if s.wanding:
            st["idle_wanding"] += D.T.DT
        elif s.mod.melee and s.ai.auto_attack and self.dist <= D.T.MELEE + 1e-6:
            st["idle_swinging"] += D.T.DT
        elif self.dist > 30.0:
            st["idle_far"] += D.T.DT
        elif s.p.mana_max > 0 and s.mana_frac() < 0.05:
            st["idle_oom"] += D.T.DT
        else:
            st["idle_other"] += D.T.DT
    self.act(s, a)


def waste(log, me):
    """{kind: Counter} of what side `me` ("A" or "B") wasted, read from a duel's log."""
    out = {"cc_into_immunity": collections.Counter(), "dmg_into_immunity": collections.Counter(), "own_cc_broken": collections.Counter()}
    for line in log:
        m = LINE.match(line)
        if not m:
            continue
        side, msg = m.group(2), m.group(3)
        if side != me:   # the foe noted it: control or damage of mine that hit its immunity, or my control on it broken
            c = IMMUNE_CC.match(msg)
            if c:
                out["cc_into_immunity"][c.group(1) + (" (DR)" if c.group(2) else "")] += 1
                continue
            b = BROKEN.match(msg)
            if b:
                out["own_cc_broken"][f"{b.group(1)} by {b.group(2)}"] += 1
        else:            # I noted it: my damage that hit its immunity
            i = IMMUNE_DMG.match(msg)
            if i and not msg.startswith("immune to"):
                out["dmg_into_immunity"][i.group(1)] += 1
    return out


def run(args):
    (ca, ra), (cb, rb), n, seed = args
    D.Duel.decide = profiled_decide
    orig = D.Side.__init__

    def init(self, *a, **k):
        orig(self, *a, **k)
        self._prof = _prof()
    D.Side.__init__ = init
    a = DR.side(ca, DR.load_build(ca, ra)[1])
    b = DR.side(cb, DR.load_build(cb, rb)[1])
    recs = []
    for i in range(n):
        r, d = DR.duel(a, b, seed * 100_003 + i, log=True, swap=bool(i % 2))
        me, foe = (d.b, d.a) if i % 2 else (d.a, d.b)
        rec = {"result": {"A": "win", "B": "loss"}.get(r, "draw"), "t": d.t}
        for tag, s in (("a", me), ("b", foe)):
            rec[tag] = {"dmg": dict(s.fight.damage), "heal": dict(s.fight.healing), "casts": dict(s.fight.casts),
                        "hp": max(0.0, s.p.hp) / s.p.hp_max, "mana": s.mana_frac() if s.p.mana_max > 0 else None,
                        "cc": dict(s.stats["cc_taken"]), "trinket": s.stats["trinket"], "interrupted": s.stats["interrupted"],
                        "waste": {k: dict(v) for k, v in waste(d.log, s.name).items()}, **s._prof}
        recs.append(rec)
    D.Side.__init__ = orig
    return recs


def report(ca, cb, recs):
    n = len(recs)
    res = collections.Counter(r["result"] for r in recs)
    T = statistics.mean(r["t"] for r in recs)
    print(f"\n=== {ca} vs {cb}: {n} duels, {ca} wins {res['win'] / n:.0%}, loses {res['loss'] / n:.0%}, draws {res['draw'] / n:.0%}; "
          f"{T:.1f} s a duel")
    for tag, cls in (("a", ca), ("b", cb)):
        sides = [r[tag] for r in recs]
        sums = {k: collections.Counter() for k in ("dmg", "heal", "casts", "cc")}
        wst = collections.defaultdict(collections.Counter)
        for s in sides:
            for k in sums:
                sums[k].update(s[k])
            for k, v in s["waste"].items():
                wst[k].update(v)
        tot = sum(sums["dmg"].values()) / n
        mana = [s["mana"] for s in sides if s["mana"] is not None]
        print(f"  {cls}: {tot:.0f} damage a duel ({tot / T:.0f} a second), {sum(sums['heal'].values()) / n:.0f} healing, "
              f"{statistics.mean(s['hp'] for s in sides):.0%} health left" + (f", {statistics.mean(mana):.0%} mana left" if mana else ""))
        print("    damage: " + ", ".join(f"{k} {v / n:.0f}" for k, v in sums["dmg"].most_common(10)))
        if sums["heal"]:
            print("    healing: " + ", ".join(f"{k} {v / n:.0f}" for k, v in sums["heal"].most_common(6)))
        print("    casts: " + ", ".join(f"{k} {v / n:.1f}" for k, v in sums["casts"].most_common(16)))
        keys = ("controlled", "casting", "gcd", "idle_swinging", "idle_wanding", "idle_far", "idle_oom", "idle_other", "inactive")
        print("    seconds: " + ", ".join(f"{k} {statistics.mean(s[k] for s in sides):.1f}" for k in keys))
        print("    control taken (s): " + (", ".join(f"{k} {v / n:.1f}" for k, v in sums["cc"].most_common(8)) or "none")
              + f"; trinket {statistics.mean(s['trinket'] for s in sides):.2f}, interrupted {statistics.mean(s['interrupted'] for s in sides):.2f}")
        for k, label in (("cc_into_immunity", "control into immunity"), ("dmg_into_immunity", "damage into immunity"),
                         ("own_cc_broken", "own control broken")):
            if wst[k]:
                print(f"    WASTE {label} (a duel): " + ", ".join(f"{x} {v / n:.2f}" for x, v in wst[k].most_common(6)))


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("pairs", nargs="+", help="class:class pairs")
    ap.add_argument("--n", type=int, default=20)
    ap.add_argument("--seed", type=int, default=1)
    ap.add_argument("--builds", default="", help="cls=ref,... in place of the field builds")
    ap.add_argument("--workers", type=int, default=6)
    a = ap.parse_args()
    refs = dict(PF.FIELD)
    for item in filter(None, a.builds.split(",")):
        c, r = item.split("=", 1)
        refs[c] = r
    pairs = [tuple(p.split(":")) for p in a.pairs]
    jobs = [((ca, refs[ca]), (cb, refs[cb]), a.n, a.seed) for ca, cb in pairs]
    with CF.ProcessPoolExecutor(max_workers=max(1, min(a.workers, len(jobs)))) as ex:
        for (ca, cb), recs in zip(pairs, ex.map(run, jobs)):
            report(ca, cb, recs)


if __name__ == "__main__":
    main()
