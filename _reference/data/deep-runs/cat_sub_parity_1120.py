"""Upstream parity for the cat and Subtlety (2026-11-20 night, the audit session's first condition for the raid push: "simulator rotation
first" cuts both ways; the play check's c2 rows showed the official rotation level or ahead on page builds of feral-cat-dps and
subtlety-raid). Our raid rotation against the official one (the cat: upstream/adaptive.apl.json, trainer ranks; Subtlety: the official
default, trainer ranks, written to upstream/default.apl.json), every build of the entry, full raid, 10,000 fights, seeds 1 and 2, with the
spec's raid signature rule read under the official rotation (required spells cast, the core share of the character's own damage, one
point of tolerance). An entry takes the official rotation unless ours leads by 0.5% on both seeds on its page pick (the best build of the
entry by our raid number), and only when the pick keeps its signature under it. With --apply the switch is written like the hunters'
(the base points at the official copy, the tuned pointers go, a rotation_note).

    python _reference/data/deep-runs/cat_sub_parity_1120.py [--fights 10000] [--apply]
Record raidsim/cat-sub-parity-1120.json.
"""
import argparse
import json
import pathlib
import re
import sys

DATA = pathlib.Path(__file__).resolve().parents[1]
sys.path[:0] = [str(DATA / "raidsim"), str(DATA), str(DATA / "deep-runs")]
import run as R  # noqa: E402
import apl_opt as A  # noqa: E402
import paths  # noqa: E402
import trainer_ranks as TR  # noqa: E402

OUT = DATA / "raidsim" / "cat-sub-parity-1120.json"
UPREL = "_reference/data/raidsim/apls/{cls}/upstream/{name}.apl.json"
CASES = [("druid", "feral-cat-dps", "Feral Combat", "ui/specs/druid/feralcat/apls/adaptive.apl.json", "adaptive"),
         ("rogue", "subtlety-raid", "Subtlety", "ui/specs/rogue/dps/apls/default.apl.json", "default")]
MARGIN, TOL = 0.005, 0.01


def official(repo, cls, src, name):
    """Our trainer-rank copy of the official rotation under apls/<class>/upstream/ (written when missing or different)."""
    rot = json.loads((repo / src).read_text(encoding="utf-8"))
    fwd = {b: (v["trainer"], v["trainer_rank"]) for b, v in TR.load_map().items()}
    txt = TR.swap_text(json.dumps(rot, indent=1) + "\n", fwd)
    dst = R.ROOT / UPREL.format(cls=cls, name=name)
    if not dst.exists() or dst.read_text(encoding="utf-8") != txt:
        dst.parent.mkdir(parents=True, exist_ok=True)
        dst.write_text(txt, encoding="utf-8", newline="")
    return json.loads(txt), dst


def shares(row, names):
    dmg, casts = {}, {}
    for x in row.get("actions") or []:
        if x.get("pet"):
            continue
        nm = "melee" if x.get("other") == "OtherActionAttack" else names.get(x.get("spellId"), str(x.get("spellId") or x.get("other")))
        dmg[nm] = dmg.get(nm, 0) + (x.get("damage") or 0)
        casts[nm] = casts.get(nm, 0) + (x.get("casts") or 0)
    tot = sum(dmg.values()) or 1
    return {n: v / tot for n, v in dmg.items()}, casts


def signature(cls, spec, sh, casts):
    s = (json.load(open(DATA / "signature_spells.json", encoding="utf-8")).get(cls) or {}).get(spec) or {}
    s = {**s, **((s.get("modes") or {}).get("raid") or {})}
    req = s.get("required") or []
    core = s.get("core") or []
    floor = s.get("min_share") or 0
    share = sum(sh.get(c, 0) for c in core)
    missing = [r for r in req if not casts.get(r)]
    ok = not missing and share >= floor - TOL
    return ok, {"required_missing": missing, "core_share": round(share, 3), "floor": floor}


def switch(cls, ename, up_rel, gains):
    import hunter_upstream_base_1120 as HB
    from filelock import locked
    with locked(HB.SPECS.with_suffix(".json.lock")):
        text = HB.SPECS.read_text(encoding="utf-8")
        h = text.index(f'"{cls}": {{')
        hb, he = HB.block(text, text.index("{", h))
        sec = text[hb:he]
        m = re.search(r'\n(\s*)"' + re.escape(ename) + r'": \{', sec)
        b0, b1 = HB.block(sec, sec.index("{", m.start()))
        blk = sec[b0:b1]
        new = re.sub(r'\n\s*"apl_opt_raid": "[^"]*",', "", blk)
        new = re.sub(r'\n\s*"apl_opt": "[^"]*",', "", new)
        new = re.sub(r',(\s*)"apl_opt(_raid)?": "[^"]*"', "", new)
        new = re.sub(r'("apl": )"[^"]*"', lambda mm: f'{mm.group(1)}"{up_rel}"', new, count=1)
        note = (f"2026-11-20 night: base switched to the official simulator's own rotation (cat_sub_parity_1120.py, the audit session's "
                f"condition for the raid push): {gains}. Earlier notes describe the rotation it replaces. ")
        if '"rotation_note"' in new:
            new = re.sub(r'("rotation_note": ")', lambda mm: mm.group(1) + note.replace('"', "'"), new, count=1)
        else:
            new = new[:-1].rstrip() + f',\n      "rotation_note": "{note.strip()}"\n    }}'
        sec = sec[:b0] + new + sec[b1:]
        out = text[:hb] + sec + text[he:]
        e = json.loads(out)[cls][ename]
        assert e["apl"] == up_rel and "apl_opt" not in e and "apl_opt_raid" not in e, e
        HB.SPECS.write_text(out, encoding="utf-8", newline="")
        print(f"{cls} {ename}: base -> {up_rel}; tuned pointers removed", flush=True)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--fights", type=int, default=10000)
    ap.add_argument("--apply", action="store_true")
    a = ap.parse_args()
    R.set_game("forever")
    repo = R.repo_path(argparse.Namespace(repo=None))
    rec = {"fights": a.fights, "entries": {}}
    for cls, ename, spec, src, name in CASES:
        entry = R.SPECS[cls][ename]
        names = R.spell_names(repo, cls)
        ours = json.load(open(R.apl_path(entry, repo, "raid"), encoding="utf-8"))
        up, up_path = official(repo, cls, src, name)
        data = {b["id"]: b for b in json.load(open(paths.builds_json("forever", cls), encoding="utf-8"))["builds"]}
        trees = R.load_trees(repo, cls)
        bids = [b for b in entry.get("builds", []) if b in data and data[b].get("player_page", True) is not False]
        res = {"official": up_path.name, "ours": pathlib.Path(R.apl_path(entry, repo, "raid")).name, "builds": {}}
        for seed in (1, 2):
            bl = [{"label": f"{k}|{b}", "talents": R.talents_string(trees, R.alloc_of(data[b])), "apl_json": r}
                  for k, r in (("ours", ours), ("official", up)) for b in bids]
            rows = A.bench(entry, repo, bl, a.fights, seed, "raid", f"csparity-{seed}")
            for b in bids:
                o, u = rows.get(f"ours|{b}") or {}, rows.get(f"official|{b}") or {}
                d = res["builds"].setdefault(b, {})
                d[f"seed {seed}"] = {"ours": round(o.get("dps") or 0, 2), "official": round(u.get("dps") or 0, 2)}
                if seed == 1:
                    sh, cs = shares(u, names)
                    ok, info = signature(cls, spec, sh, cs)
                    d["official_signature"] = {"ok": ok, **info}
                    sho, cso = shares(o, names)
                    d["ours_signature"] = dict(zip(("ok", "info"), signature(cls, spec, sho, cso)))
        pick = max(bids, key=lambda b: res["builds"][b]["seed 1"]["ours"])
        leads = [res["builds"][pick][f"seed {s}"]["ours"] / res["builds"][pick][f"seed {s}"]["official"] - 1 for s in (1, 2)]
        keep = all(x >= MARGIN for x in leads)
        sig_ok = res["builds"][pick]["official_signature"]["ok"]
        res["pick"], res["ours_lead_on_pick"] = pick, [round(x, 4) for x in leads]
        res["decision"] = ("ours stays: it leads by 0.5% or more on both seeds" if keep else
                           ("official: ours does not lead by 0.5% on both seeds" if sig_ok else
                            "ours stays: the official rotation breaks the pick's signature"))
        for b in bids:
            d = res["builds"][b]
            print(f"   {cls} {ename} {b}: ours {d['seed 1']['ours']}/{d['seed 2']['ours']}, official {d['seed 1']['official']}/"
                  f"{d['seed 2']['official']} ({d['seed 1']['official'] / d['seed 1']['ours'] - 1:+.2%}/{d['seed 2']['official'] / d['seed 2']['ours'] - 1:+.2%}); "
                  f"official signature {d['official_signature']}", flush=True)
        print(f"== {cls} {ename}: pick {pick}, ours' lead {leads[0]:+.2%}/{leads[1]:+.2%} -> {res['decision']}", flush=True)
        rec["entries"][f"{cls}:{ename}"] = res
        if a.apply and res["decision"].startswith("official"):
            gains = "; ".join(f"{b} {res['builds'][b]['seed 1']['official']} / {res['builds'][b]['seed 2']['official']} against ours "
                              f"{res['builds'][b]['seed 1']['ours']} / {res['builds'][b]['seed 2']['ours']}" for b in bids)
            switch(cls, ename, UPREL.format(cls=cls, name=name), f"full raid, {a.fights} fights, seeds 1 / 2: {gains}")
            res["applied"] = True
    OUT.write_text(json.dumps(rec, indent=1) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
