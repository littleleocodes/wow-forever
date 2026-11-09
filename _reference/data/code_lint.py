"""Static checks of the project's own scripts (2026-11-09: `heallab/calibrate.py` had stopped with an UnboundLocalError on every run
since 2026-10-18, because an "import splitfx" inside main() made the name local to the whole function and an earlier line read it;
no lane ran the healer calibration, so nothing noticed for three weeks).

    python _reference/data/code_lint.py          # prints every finding, exit 1 when there is one

Checks: a function that imports a name the module already imports at the top and uses that name before the local import (an
UnboundLocalError when the earlier line runs). Run it at every lane boundary and after editing a script.
"""
import ast
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[1]


def shadowed_imports(path):
    tree = ast.parse(path.read_text(encoding="utf-8"))
    top = {a.asname or a.name.split(".")[0] for n in tree.body if isinstance(n, (ast.Import, ast.ImportFrom)) for a in n.names}
    out = []
    for fn in ast.walk(tree):
        if not isinstance(fn, (ast.FunctionDef, ast.AsyncFunctionDef)):
            continue
        local = {}
        for n in ast.walk(fn):
            if isinstance(n, (ast.Import, ast.ImportFrom)):
                for a in n.names:
                    nm = a.asname or a.name.split(".")[0]
                    if nm in top:
                        local.setdefault(nm, n.lineno)
        for nm, ln in local.items():
            early = sorted(n.lineno for n in ast.walk(fn) if isinstance(n, ast.Name) and n.id == nm and n.lineno < ln)
            if early:
                out.append(f"{path.relative_to(ROOT)}:{early[0]}: {fn.name}() reads {nm} before its local import at line {ln} "
                           "(UnboundLocalError); drop the local import, the module imports it at the top")
    return out


def main():
    found = []
    for p in sorted(HERE.rglob("*.py")):
        if "raw" in p.parts or "__pycache__" in p.parts:
            continue
        try:
            found += shadowed_imports(p)
        except SyntaxError as e:
            found.append(f"{p.relative_to(ROOT)}: does not parse ({e})")
    print("\n".join(found) or "code lint: no findings")
    sys.exit(1 if found else 0)


if __name__ == "__main__":
    main()
