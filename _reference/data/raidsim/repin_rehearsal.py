"""Re-pin rehearsal (2026-10-16, page audit H2; on the official simulator since 2026-10-22, sim-port open item 2): build the project's
patched bench on another commit of the official wowsims/forever in a separate git worktree, leaving the pinned clone and its bench alone.

    git -C ~/.wow-forever-tools/wowsims-forever fetch --filter=blob:none origin <commit or master>
    git -C ~/.wow-forever-tools/wowsims-forever worktree add --no-checkout --detach ../wowsims-forever-next <commit>
    git -C ~/.wow-forever-tools/wowsims-forever-next sparse-checkout set sim proto cmd ui assets/database tools
    git -C ~/.wow-forever-tools/wowsims-forever-next checkout <commit>
    python _reference/data/raidsim/repin_rehearsal.py [--worktree <dir>]
    python _reference/data/raidsim/run.py <class> --spec <entry> --repo ~/.wow-forever-tools/wowsims-forever-next --iterations 1000   # smoke test

It copies patches/forever/**.go over the worktree and makes the edits of patches/forever/edits.json (the same rule as setup.py's
apply_patches), but reports an edit whose anchor is gone instead of stopping (the commit may have changed or adopted it: retire the edit
then), then generates the protos and builds foreverbench there. At the real re-pin: retire or adapt the reported edits in patches/, then
setup.py --update, the pin, and the steps after a simulator update (CLAUDE.md).

History: until 2026-10-18 this rehearsed upstream commits of the ElliotWood/Forever fork in the worktree ~/.wow-forever-tools/forever-upstream
(the 2026-10-16 run on b7083fa, client 70425: every patch applied but the rage crit (#794) and Bear Form threat (#798) edits, upstream's
own; pet_scaling.go had to add the hunter's ranged-only crit). The fork was deleted on 2026-10-18 (`_reference/sim-port.md`).
"""
import argparse
import json
import os
import pathlib
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[2]
sys.path.insert(0, str(HERE))
import setup as SETUP  # noqa: E402  (the tools folder, the patches folder)

D = SETUP.PATCHES / "forever"
TOOLS = SETUP.tools_dir()


def sh(args, cwd, env):
    r = subprocess.run([str(a) for a in args], cwd=str(cwd), env=env, capture_output=True, text=True, encoding="utf-8", errors="replace")
    print("$", " ".join(str(a) for a in args)[:160], "->", r.returncode)
    if r.returncode:
        print(r.stdout[-2000:], r.stderr[-4000:])
        sys.exit(1)
    return r


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--worktree", default=str(TOOLS / "wowsims-forever-next"), help="the worktree of the commit to rehearse")
    a = ap.parse_args()
    up = pathlib.Path(a.worktree)
    if not (up / "sim").exists():
        raise SystemExit(f"no checkout at {up}: make the worktree first (see the docstring)")
    for f in D.rglob("*.go"):
        dst = up / f.relative_to(D)
        dst.parent.mkdir(parents=True, exist_ok=True)
        dst.write_text(f.read_text(encoding="utf-8"), encoding="utf-8")
        print("patch:", f.relative_to(D).as_posix())
    gone = []
    for e in json.load(open(D / "edits.json", encoding="utf-8")) if (D / "edits.json").exists() else []:
        old = e.get("after") or e.get("replace")
        new = (e["after"] + e["insert"]) if "insert" in e else e["with"]
        t = (up / e["file"]).read_text(encoding="utf-8") if (up / e["file"]).exists() else ""
        if (e.get("insert") or e.get("with")) in t:
            continue
        if t.count(old) != 1:
            gone.append(e["file"])
            print(f"EDIT NOT APPLIED (anchor found {t.count(old)} times): {e['file']}: {old[:80]!r}")
            continue
        (up / e["file"]).write_text(t.replace(old, new), encoding="utf-8")
        print("edit:", e["file"])
    print("patches applied" + (f"; {len(gone)} edits to retire or adapt: {gone}" if gone else ""))
    exe = ".exe" if os.name == "nt" else ""
    env = dict(os.environ, GOPATH=str(TOOLS / "gopath"), GOMODCACHE=str(TOOLS / "gopath/pkg/mod"), GOCACHE=str(TOOLS / "gocache"), GOFLAGS="-mod=mod",
               GOTOOLCHAIN="auto", PATH=os.pathsep.join([str(TOOLS / "go/bin"), str(TOOLS / "protoc/bin"), str(TOOLS / "gopath/bin"), os.environ["PATH"]]))
    protos = sorted(p.name for p in (up / "proto").glob("*.proto"))
    sh([TOOLS / f"protoc/bin/protoc{exe}", "-I=./proto", "--go_opt=Mgoogle/protobuf/descriptor.proto=google.golang.org/protobuf/types/descriptorpb",
        "--go_out=./sim/core", *[f"./proto/{p}" for p in protos]], up, env)
    (up / "cmd/foreverbench").mkdir(parents=True, exist_ok=True)
    (up / "cmd/foreverbench/main.go").write_text((HERE / "foreverbench" / "main.go").read_text(encoding="utf-8"), encoding="utf-8")
    sh([TOOLS / f"go/bin/go{exe}", "build", "--tags=with_db", "-o", f"foreverbench{exe}", "./cmd/foreverbench"], up, env)
    print("built", up / f"foreverbench{exe}")


if __name__ == "__main__":
    main()
