"""Signature-spell audit of the raid side (user rule 2026-10-22: the specs we test must play the spells that make the spec; see
signature.py and _reference/data/signature_spells.json).

    python -u _reference/data/raidsim/signature_audit.py [classes] [--measure] [--iterations 1500] [--write]

Per raid entry of specs.json (damage and tank entries): the specs its rotation must serve (spec_modes.RAID_ENTRY_TREES and the specs of
the builds it lists), the raid rotation's lines for every required spell (shown lines, and lines at or above the filler: a line below
the filler never fires), then per build the entry lists and per raid page build (render_modes.raid_numbers: a build's best entry):
- the last race record's numbers (the training dummy: damage shares and casts; the environments run's full-raid casts), with the
  simulator commit they ran on (the old ElliotWood/Forever fork until the 2026-10-22 re-run lands);
- with --measure: the build run now in the full raid (the entry's raid rotation, phase-1 gear, --iterations fights, the default
  simulator clone), its full-raid damage shares and casts checked against the rule: every required spell the build can cast is cast,
  and the core sources carry min_share of its damage.
Writes `_reference/signature-audit-raid.md` and `raidsim/signature-audit.json` (the pages read the measured checks from it when the
environments record has no full-raid shares) with --write.
"""
import argparse
import datetime
import importlib.util
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[2]
sys.path[:0] = [str(ROOT / "_reference/data"), str(HERE)]
import paths  # noqa: E402
import spec_modes as SM  # noqa: E402
import raid_signature as SIG  # noqa: E402  (raidsim/raid_signature.py; _reference/data/signature.py is the fight lab's)

PAGE = ROOT / "_reference" / "signature-audit-raid.md"
JSON = HERE / "signature-audit.json"
TODAY = datetime.date.today().isoformat()


def _load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


A = _load("aplopt_sigaudit", HERE / "apl_opt.py")
R = A.R




def page_builds(cls):
    """{build id: best entry} of the raid page builds (render_modes.raid_numbers), {} when the renderer cannot load."""
    try:
        RM = _load("render_modes_sigaudit", ROOT / "_reference/data/render_modes.py")
        return {bid: r["entry"] for bid, r in RM.raid_numbers(cls).items()}
    except Exception as ex:   # noqa: BLE001
        print(f"  (render_modes.raid_numbers failed for {cls}: {type(ex).__name__}: {ex})")
        return {}


def load(p):
    try:
        return json.load(open(p, encoding="utf-8")) if p.exists() else None
    except ValueError:
        return None


def audit_class(cls, repo, a, names):
    data = {b["id"]: b for b in json.load(open(paths.builds_json("forever", cls), encoding="utf-8"))["builds"]}
    specs = R.SPECS.get(cls) or {}
    pages = page_builds(cls)
    known, cds = SIG.book_ids(cls)
    out = {"entries": {}, "pages": pages}
    for entry, E in specs.items():
        if not isinstance(E, dict) or "apl" not in E:
            continue
        listed = [b for b in E.get("builds", []) if b in data]
        on_page = [b for b, e in pages.items() if e == entry and b in data and b not in listed]
        ids = listed + on_page
        ents = SIG.entry_specs(cls, entry, [data[b] for b in listed])
        req = SIG.required_ids(cls, sorted(ents), names)
        apl_p = R.apl_path(E, repo, "raid")
        apl = load(pathlib.Path(apl_p)) or {}
        lines = SIG.line_counts(apl, req, cds, known)
        rep = load(paths.raidsim_dir(cls) / f"{entry}.json") or {}
        env = load(paths.raidsim_dir(cls) / f"{entry}-environments.json") or {}
        rrow = {x["label"]: x for x in rep.get("results", [])}
        erow = {x["label"]: x for x in env.get("results", [])}
        er = {"trees": sorted(SM.RAID_ENTRY_TREES.get((cls, entry)) or []), "specs": sorted(ents), "tank": bool(E.get("tank")),
              "rotation": R.apl_label(E, repo, "raid"), "lines": {k: list(v) for k, v in lines.items()},
              "record_commit": (rep.get("sim") or {}).get("commit"), "record_date": rep.get("date"),
              "env_commit": (env.get("sim") or {}).get("commit"), "builds": {}}
        measured = {}
        if a.measure and ids:
            trees = R.load_trees(repo, cls)
            bl = [{"label": b, "talents": R.talents_string(trees, R.alloc_of(data[b]))} for b in ids]
            try:
                measured = A.bench(E, repo, bl, a.iterations, 7, "raid", f"sigaudit-{cls}-{entry}")
            except SystemExit as ex:
                print(f"  {entry}: bench failed ({ex})")
            er["measured_commit"] = R.git_commit(repo)
        for b in ids:
            bd = data[b]
            flat = SIG.flat_of(R.alloc_of(bd))
            spec = SIG.entry_spec(cls, entry, flat, bd)
            x = {"spec": spec, "listed": b in listed, "page_entry": pages.get(b), "role": bd.get("role", "dps")}
            r0 = rrow.get(b) or {}
            if r0.get("shares") and not E.get("tank"):
                x["dummy"] = SIG.check_shares(cls, spec, r0["shares"], r0.get("casts"), flat)
            e0 = erow.get(b) or {}
            if e0.get("raid_shares") or e0.get("raid_casts"):
                # the full-raid casts; damage shares from the full raid when the environments run kept them (since 2026-10-22), else the dummy's
                sh = e0.get("raid_shares") or (r0.get("shares") if not E.get("tank") else None) or {}
                x["raid_record"] = SIG.check_shares(cls, spec, sh, e0.get("raid_casts"), flat)
                x["raid_record_shares"] = "full raid" if e0.get("raid_shares") else ("training dummy" if sh else "none")
            m = measured.get(b)
            if m and m.get("actions"):
                x["raid_measured"] = SIG.check(cls, spec, m["actions"], names, flat)
                x["raid_measured_dps"] = round(m.get("dps") or 0.0, 1)
                x["raid_measured_top"] = {k: round(v, 3) for k, v in list(SIG.shares_of(m["actions"], names).items())[:6]}
                # the shares and casts themselves, so a reader re-checks them against the rule as it is then (render_modes.raid_sig_check)
                x["raid_measured_shares"] = {k: round(v, 4) for k, v in SIG.shares_of(m["actions"], names).items()}
                x["raid_measured_casts"] = {k: round(v, 2) for k, v in SIG.casts_of(m["actions"], names).items()}
            er["builds"][b] = x
        out["entries"][entry] = er
        miss = [s for s, (n, up) in lines.items() if not up]
        print(f"  {cls} {entry}: specs {', '.join(sorted(ents)) or '-'}; rotation lines " + ", ".join(f"{s} {n}/{up}" for s, (n, up) in lines.items())
              + (f"  NO LIVE LINE: {', '.join(miss)}" if miss else ""), flush=True)
        for b, x in er["builds"].items():
            c = x.get("raid_measured") or x.get("raid_record") or x.get("dummy")
            if c:
                print(f"      {b:<40} {x['spec']:<32} {'ok ' if c['ok'] else 'FAIL'} core {c['core_share'] if c['core_share'] is not None else float('nan'):.2f}"
                      f"/{c['min_share']:.2f} {c['why']}", flush=True)
    return out


def verdict(x):
    c = x.get("raid_measured") or x.get("raid_record")
    src = "full raid, measured now" if x.get("raid_measured") else (
        f"last record (casts: full raid; shares: {x.get('raid_record_shares')})" if x.get("raid_record") else "")
    if not c and x.get("dummy"):
        c, src = x["dummy"], "training dummy, last record"
    return c, src


def write(res):
    JSON.write_text(json.dumps({"date": TODAY, "classes": res}, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    o = ["# Signature-spell audit, raid (generated)", "",
         f"> Generated by `_reference/data/raidsim/signature_audit.py` on {TODAY}. Do not hand-edit. The rule: "
         "`_reference/data/signature_spells.json` (user rule 2026-10-22: a spec's signature spells are the core of its rotation; strictness "
         "\"main damage\"). Record `raidsim/signature-audit.json`.", "",
         "Per raid entry: the specs its raid rotation serves, the lines casting each required spell (shown / at or above the filler; a line "
         "below the filler never fires), then each build the entry lists or the raid pages show from it: its spec, the core share (the core "
         "sources' share of its damage) against min_share, and what fails. \"Measured now\" is a full-raid run on the official "
         "wowsims/forever clone at the audit's date (the entry's current raid rotation); \"last record\" is the entry's last race (the "
         "training dummy) or environments run, on the simulator commit the column names.", ""]
    fails = []
    for cls, r in res.items():
        o += [f"## {cls.capitalize()}", ""]
        for entry, er in r["entries"].items():
            line = ", ".join(f"{s} {n}/{up}" for s, (n, up) in er["lines"].items()) or "no required spell"
            dead = [s for s, (n, up) in er["lines"].items() if not up]
            o += [f"### {entry}" + (" (tank)" if er["tank"] else ""), "",
                  f"Built for {', '.join(er['trees']) or '-'}; serves {', '.join(er['specs']) or '-'}. Raid rotation `{er['rotation']}`: {line}"
                  + (f". **No live line for {', '.join(dead)}.**" if dead else "."), "",
                  f"Records: race {er.get('record_date') or '-'} on {er.get('record_commit') or '-'}, environments on {er.get('env_commit') or '-'}"
                  + (f"; measured now on {er['measured_commit']}" if er.get("measured_commit") else "") + ".", ""]
            if er["builds"]:
                o += ["| Build | Spec | On page | Check | Core share | Where | Fails |", "|---|---|---|---|---|---|---|"]
                for b, x in er["builds"].items():
                    c, src = verdict(x)
                    if not c:
                        o.append(f"| `{b}` | {x['spec']} | {x.get('page_entry') or '-'} | no rule or no data | - | - | - |")
                        continue
                    ok = "ok" if c["ok"] else "**FAIL**"
                    cs = f"{c['core_share']:.0%} / {c['min_share']:.0%}" if c.get("core_share") is not None else "-"
                    if c.get("cd_use") is not None:
                        cs = f"cooldowns used {c['cd_use']:.0%} / {c['min_cd_use']:.0%}"
                    o.append(f"| `{b}` | {x['spec']} | {x.get('page_entry') or '-'} | {ok} | {cs} | {src} | {c['why'] or '-'} |")
                    if not c["ok"]:
                        fails.append((cls, entry, b, x["spec"], c, src, x.get("page_entry") == entry))
                o.append("")
    head = ["## Summary", "", f"{len(fails)} build checks fail (" + str(sum(1 for f in fails if f[6])) + " of them a raid page build in its page entry).", "",
            "| Class | Entry | Build | Spec | Page build | Fails | Where |", "|---|---|---|---|---|---|---|"]
    head += [f"| {c} | {e} | `{b}` | {s} | {'yes' if pg else 'no'} | {k['why']} | {src} |" for c, e, b, s, k, src, pg in fails]
    o[6:6] = head + [""]
    PAGE.write_text("\n".join(o) + "\n", encoding="utf-8")
    print(f"wrote {PAGE.relative_to(ROOT)} and {JSON.relative_to(ROOT)}")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("classes", nargs="*")
    ap.add_argument("--measure", action="store_true")
    ap.add_argument("--iterations", type=int, default=1500)
    ap.add_argument("--repo")
    ap.add_argument("--write", action="store_true")
    a = ap.parse_args()
    R.set_game("forever")
    repo = R.repo_path(argparse.Namespace(repo=a.repo))
    res = {}
    for cls in a.classes or SM.CLASSES:
        res[cls] = audit_class(cls, repo, a, R.spell_names(repo, cls))
    if a.write:
        if not a.classes and JSON.exists():
            pass
        elif JSON.exists():   # a partial run keeps the other classes' rows
            old = (load(JSON) or {}).get("classes", {})
            res = {**old, **res}
        write(res)


if __name__ == "__main__":
    main()
