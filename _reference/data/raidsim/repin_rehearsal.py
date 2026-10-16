"""Re-pin rehearsal (2026-10-16, page audit H2; user decision: re-pin once after the beta ends on 2026-10-22): build the project's patched
bench on an upstream commit in a separate git worktree, leaving the pinned clone and its bench alone.

    git -C ~/.wow-forever-tools/forever-repo fetch origin
    git -C ~/.wow-forever-tools/forever-repo worktree add --no-checkout --detach ../forever-upstream <commit>
    git -C ~/.wow-forever-tools/forever-upstream sparse-checkout set sim proto cmd ui assets/database tools
    git -C ~/.wow-forever-tools/forever-upstream checkout <commit>
    python _reference/data/raidsim/repin_rehearsal.py
    python _reference/data/raidsim/run.py <class> --spec <entry> --repo ~/.wow-forever-tools/forever-upstream --iterations 1000   # smoke test

It copies patches/forever/**.go over the worktree and makes the edits of edits.json, skipping RETIRED (edits upstream made itself) and
adapting pet_scaling.go (ADAPT), then generates the protos and builds foreverbench there. The 2026-10-16 run on b7083fa (client 70425):
every other patch applies; rage crit (#794) and Bear Form threat (#798) are upstream's; upstream's pet crit (a60e356: the hunter's melee
plus ranged-only crit, no Agility crit of the pet's own) would be shadowed by pet_scaling.go, which returns first, so the pet's crit takes
RangedCritPercent too. At the real re-pin make the same three changes in patches/ (drop the two edits, the pet crit line), then
setup.py --update, the pin, fill_armor.py on the new database and the steps after a simulator update (CLAUDE.md)."""
import json
import os
import pathlib
import subprocess
import sys

ROOT = pathlib.Path("F:/wow-forever")
D = ROOT / "_reference/data/raidsim/patches/forever"
TOOLS = pathlib.Path.home() / ".wow-forever-tools"
UP = TOOLS / "forever-upstream"
RETIRED = {   # anchors of edits.json entries upstream now does itself
    "const CritRageMultiplier = 1.75", "const BearFormThreatMultiplier = 1.3"}   # upstream #794 and #798 do these


def sh(args, cwd, env):
    r = subprocess.run([str(a) for a in args], cwd=str(cwd), env=env, capture_output=True, text=True, encoding="utf-8", errors="replace")
    print("$", " ".join(str(a) for a in args)[:160], "->", r.returncode)
    if r.returncode:
        print(r.stdout[-2000:], r.stderr[-4000:])
        sys.exit(1)
    return r


for f in D.rglob("*.go"):
    dst = UP / f.relative_to(D)
    dst.parent.mkdir(parents=True, exist_ok=True)
    txt = f.read_text(encoding="utf-8")
    if f.name == "pet_scaling.go":   # ADAPT   # upstream a60e356: the pet's crit is its master's ranged crit (melee + ranged-only crit)
        old = "\ts[stats.PhysicalCritPercent] = owner[stats.PhysicalCritPercent]\n"
        assert old in txt
        txt = txt.replace(old, "\ts[stats.PhysicalCritPercent] = owner[stats.PhysicalCritPercent] + owner[stats.RangedCritPercent]\n")
    dst.write_text(txt, encoding="utf-8")
for e in json.load(open(D / "edits.json", encoding="utf-8")):
    old = e.get("after") or e.get("replace")
    if old in RETIRED:
        print("skip (upstream has it):", e["file"])
        continue
    t = (UP / e["file"]).read_text(encoding="utf-8")
    new = (e["after"] + e["insert"]) if "insert" in e else e["with"]
    if (e.get("insert") or e.get("with")) in t:
        continue
    assert t.count(old) == 1, e["file"]
    (UP / e["file"]).write_text(t.replace(old, new), encoding="utf-8")
print("patches applied")
env = dict(os.environ, GOPATH=str(TOOLS / "gopath"), GOMODCACHE=str(TOOLS / "gopath/pkg/mod"), GOCACHE=str(TOOLS / "gocache"), GOFLAGS="-mod=mod",
           GOTOOLCHAIN="auto", PATH=os.pathsep.join([str(TOOLS / "go/bin"), str(TOOLS / "protoc/bin"), str(TOOLS / "gopath/bin"), os.environ["PATH"]]))
protos = sorted(p.name for p in (UP / "proto").glob("*.proto"))
sh([TOOLS / "protoc/bin/protoc.exe", "-I=./proto", "--go_opt=Mgoogle/protobuf/descriptor.proto=google.golang.org/protobuf/types/descriptorpb",
    "--go_out=./sim/core", *[f"./proto/{p}" for p in protos]], UP, env)
(UP / "cmd/foreverbench").mkdir(parents=True, exist_ok=True)
(UP / "cmd/foreverbench/main.go").write_text((ROOT / "_reference/data/raidsim/foreverbench/main.go").read_text(encoding="utf-8"), encoding="utf-8")
sh([TOOLS / "go/bin/go.exe", "build", "--tags=with_db", "-o", "foreverbench.exe", "./cmd/foreverbench"], UP, env)
print("built", UP / "foreverbench.exe")
