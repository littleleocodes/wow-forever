"""Write out what the simulator does with value variables a rotation does not define (2026-10-24 audit).

The rotation search copied lines from the official simulator's rotations without their `valueVariables` (fixed in apl_opt.inline_refs),
so our rotations carry `variableRef`s with nothing to point to. The simulator (sim/core/apl_values_operators.go, apl_action.go) drops a
reference it cannot find: `not` of a dropped value is dropped, `and`/`or`/`min`/`max` drop the branch (none left: dropped; one left: that
one), a comparison or math with a dropped side is dropped, and an action whose condition is dropped casts always. This tool rewrites the
rotation file the same way, so the text says what runs; the simulated rotation does not change (check with --verify).

    python _reference/data/raidsim/apl_prune.py --check                # every rotation of ours with undefined references
    python _reference/data/raidsim/apl_prune.py <class> [--write]      # rewrite the class's rotations
"""
import argparse
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
APLS = HERE / "apls"
LISTS = ("and", "or", "min", "max")


class Gone(Exception):
    pass


def prune(x, var):
    """The value as the simulator builds it; raises Gone for a dropped value."""
    if isinstance(x, list):
        return [prune(v, var) for v in x]
    if not isinstance(x, dict):
        return x
    if set(x) == {"variableRef"}:
        if (x["variableRef"] or {}).get("name") not in var:
            raise Gone
        return x
    if len(x) == 1:
        (k, v), = x.items()
        if k in LISTS and isinstance(v, dict) and isinstance(v.get("vals"), list):
            kept = []
            for it in v["vals"]:
                try:
                    kept.append(prune(it, var))
                except Gone:
                    pass
            if not kept:
                raise Gone
            if len(kept) == 1:
                return kept[0]
            return {k: dict(v, vals=kept)}
    return {k: prune(v, var) for k, v in x.items()}


def prune_apl(apl):
    """(new rotation, number of lines changed)."""
    var = {v.get("name") for v in apl.get("valueVariables") or [] if v.get("name")}
    out, n = [], 0
    for it in apl.get("priorityList") or []:
        act = it.get("action") or {}
        cond = act.get("condition")
        if cond is None:
            out.append(it)
            continue
        try:
            new = prune(cond, var)
        except Gone:
            new = None
        if new != cond:
            n += 1
            act = {k: v for k, v in act.items() if k != "condition"}
            if new is not None:
                act = {"condition": new, **act}
            it = dict(it, action=act)
        out.append(it)
    return dict(apl, priorityList=out), n


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("classes", nargs="*")
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--write", action="store_true")
    a = ap.parse_args()
    dirs = [APLS / c for c in a.classes] if a.classes else sorted(p for p in APLS.iterdir() if p.is_dir())
    for d in dirs:
        for f in sorted(d.glob("*.apl.json")):
            apl = json.load(open(f, encoding="utf-8"))
            new, n = prune_apl(apl)
            if n:
                print(f"{f.relative_to(HERE).as_posix()}: {n} line(s) with undefined variables")
                if a.write and not a.check:
                    f.write_text(json.dumps(new, indent=1) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
