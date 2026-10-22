"""Set up the official WoW Forever simulator (github.com/wowsims/forever, since 2026-10-18) for `run.py`: Go and protoc toolchains, a sparse clone, the generated
protobuf code, the simulator CLI and our `foreverbench` tool — everything under %USERPROFILE%/.wow-forever-tools (or --tools).

    python _reference/data/raidsim/setup.py            # first time: ~400 MB of downloads and checkout, a few minutes
    python _reference/data/raidsim/setup.py --update   # pull the simulator's master and rebuild the tools
    python _reference/data/raidsim/setup.py --rebuild  # rebuild the tools only (after editing foreverbench/main.go)

Layout: <tools>/go (Go toolchain), <tools>/protoc, <tools>/gopath (module cache, protoc-gen-go), <tools>/wowsims-forever
(sparse checkout of https://github.com/wowsims/forever: sim, proto, cmd, ui, assets/database, tools) with
`wowsimcli.exe` and `foreverbench.exe` built in it. Nothing is installed system-wide.

2026-10-18: the ElliotWood/Forever fork every number before that date was simulated with was deprecated and its repository deleted
in the night of 2026-10-17/18 ("The official WoW Forever simulator is now live", wowsims.com/forever); the pipeline moved to the
official repository (user decision, audit 2 row 1; `_reference/sim-port.md`). An existing <tools>/forever-repo clone of the fork
(b7083fa) still builds with the archived patches in patches/elliotwood-b7083fa/, but nothing points at it.

A fresh setup checks out the pinned simulator commit (GAMES[...]["commit"]: the one every number in the project was simulated
with), so a new machine or a Claude Code cloud session builds the same simulator; `--update` moves to the fork's latest commit
(then update the pin). Cloud sessions (Linux, no access to go.dev): an existing `go` on PATH is used (GOTOOLCHAIN=auto fetches
the version the simulator's go.mod asks for through the Go module proxy), and when protoc cannot be downloaded from GitHub the
protoc of the `grpcio-tools` Python package is used (2026-09-28).
"""
import argparse
import json
import os
import pathlib
import shutil
import subprocess
import sys
import urllib.request
import zipfile

HERE = pathlib.Path(__file__).resolve().parent
GO_VERSION = "1.27.1"
PROTOC_VERSION = "36.2"
REPO_URL = "https://github.com/wowsims/forever"
SPARSE = ["sim", "proto", "cmd", "ui", "assets/database", "tools"]
GAMES = {"forever": {"url": "https://github.com/wowsims/forever", "dir": "wowsims-forever", "module": "github.com/wowsims/forever", "bench": "foreverbench",
                     # 09e7398 (wowsims/forever master, 2026-10-18 19:55 +0200; spell data and items client 1.60.1.70450). Before 2026-10-18
                     # the ElliotWood/Forever fork: b7083fa (70425) from 2026-10-16, 2ce8265 (70291) from 2026-10-09, b0f0df3 (70205), 40be98e
                     "commit": "09e739807d68a561f01ddb0ba41c2c6a6003d681"},
         "classic": {"url": "https://github.com/wowsims/classic", "dir": "classic-repo", "module": "github.com/wowsims/classic", "bench": "classicbench",
                     "commit": "7779ebbf79dc7f1341e6ab939b28a3402c9a730a"}}


ENV = {"forever": "WOW_FOREVER_SIM", "classic": "WOW_FOREVER_CLASSIC_SIM"}   # an explicit checkout overrides <tools>/<dir>


def tools_dir():
    return pathlib.Path(os.environ.get("WOW_FOREVER_TOOLS", pathlib.Path.home() / ".wow-forever-tools"))


def checkout(game="forever"):
    """The simulator checkout scripts read (2026-10-22, sim-port open item 2): WOW_FOREVER_SIM (Classic: WOW_FOREVER_CLASSIC_SIM), else
    <tools>/<GAMES[game]["dir"]>: the official wowsims/forever clone since 2026-10-18 (the fork's <tools>/forever-repo is an archive).
    No check that the bench is built (run.py's repo_path does that)."""
    return pathlib.Path(os.environ.get(ENV[game]) or tools_dir() / GAMES[game]["dir"])


def sh(args, cwd, env=None, check=True):
    print("  $", " ".join(str(a) for a in args))
    r = subprocess.run([str(a) for a in args], cwd=str(cwd), env=env, text=True, capture_output=True, encoding="utf-8", errors="replace")
    if r.stdout.strip():
        print("   ", r.stdout.strip().splitlines()[-1][:160])
    if r.returncode and check:
        print(r.stderr[-3000:])
        raise SystemExit(f"command failed: {args[0]}")
    return r


def download(url, dest):
    if dest.exists():
        print(f"  have {dest.name}")
        return
    print(f"  downloading {url}")
    urllib.request.urlretrieve(url, dest)


PATCHES = HERE / "patches"


def patch_files(game):
    """Files of the clone the project's patches touch (patches/<game>/: copied files and edits.json targets), repo-relative."""
    d = PATCHES / game
    if not d.exists():
        return []
    out = [f.relative_to(d).as_posix() for f in d.rglob("*.go")]
    edits = d / "edits.json"
    if edits.exists():
        out += [e["file"] for e in json.load(open(edits, encoding="utf-8"))]
    return sorted(set(out))


def apply_patches(game, repo):
    """Copy patches/<game>/**.go over the clone and make the insertions of edits.json (idempotent): our additions to the community
    simulator (patches/README.md), e.g. Frostfire Bolt, which the fork ships as a stub."""
    d = PATCHES / game
    if not d.exists():
        return
    for f in d.rglob("*.go"):
        dst = repo / f.relative_to(d)
        dst.parent.mkdir(parents=True, exist_ok=True)
        dst.write_text(f.read_text(encoding="utf-8"), encoding="utf-8")
        print(f"  patch: {f.relative_to(d).as_posix()}")
    edits = d / "edits.json"
    for e in (json.load(open(edits, encoding="utf-8")) if edits.exists() else []):
        # {"file", "after", "insert"} inserts text after a unique anchor; {"file", "replace", "with"} swaps a unique text for ours
        # (2026-10-08: the demon scaling and the pet hit rule change one expression each). Both are idempotent.
        target = repo / e["file"]
        txt = target.read_text(encoding="utf-8")
        old, new = (e["after"], e["after"] + e["insert"]) if "insert" in e else (e["replace"], e["with"])
        if (e["insert"] if "insert" in e else e["with"]) in txt:
            continue
        if txt.count(old) != 1:
            raise SystemExit(f"patch {e['file']}: anchor not found once: {old!r}")
        target.write_text(txt.replace(old, new), encoding="utf-8")
        print(f"  patch: {e['file']} ({e.get('why', '')})")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--tools", default=os.environ.get("WOW_FOREVER_TOOLS", str(pathlib.Path.home() / ".wow-forever-tools")))
    ap.add_argument("--update", action="store_true", help="git pull the simulator and rebuild")
    ap.add_argument("--rebuild", action="store_true", help="rebuild wowsimcli and foreverbench only")
    ap.add_argument("--game", default="forever", choices=list(GAMES), help="classic: the upstream wowsims/classic simulator for the Classic-era check")
    a = ap.parse_args()
    G = GAMES[a.game]
    tools = pathlib.Path(a.tools)
    tools.mkdir(parents=True, exist_ok=True)
    win = sys.platform.startswith("win")
    exe = ".exe" if win else ""
    go_dir, protoc_dir, gopath, repo = tools / "go", tools / "protoc", tools / "gopath", tools / G["dir"]
    # ---- toolchains
    go = go_dir / "bin" / f"go{exe}"
    if not go.exists():
        system_go = shutil.which("go")
        if system_go:   # a cloud session: go.dev is not reachable, the image has Go, and GOTOOLCHAIN=auto gets go.mod's version
            print(f"  using the system Go at {system_go}")
            go = pathlib.Path(system_go)
        else:
            arch = "windows-amd64.zip" if win else "linux-amd64.tar.gz"
            z = tools / f"go{GO_VERSION}.{arch}"
            download(f"https://go.dev/dl/go{GO_VERSION}.{arch}", z)
            print("  extracting go")
            if win:
                zipfile.ZipFile(z).extractall(tools)
            else:
                sh(["tar", "xzf", z], tools)
    protoc = [protoc_dir / "bin" / f"protoc{exe}"]
    if not protoc[0].exists():
        if shutil.which("protoc"):
            protoc = [pathlib.Path(shutil.which("protoc"))]
        else:
            plat = "win64" if win else "linux-x86_64"
            z = tools / f"protoc-{PROTOC_VERSION}-{plat}.zip"
            try:
                download(f"https://github.com/protocolbuffers/protobuf/releases/download/v{PROTOC_VERSION}/protoc-{PROTOC_VERSION}-{plat}.zip", z)
                protoc_dir.mkdir(exist_ok=True)
                zipfile.ZipFile(z).extractall(protoc_dir)
                if not win:
                    os.chmod(protoc[0], 0o755)
            except Exception as ex:   # GitHub's release host may not be on a cloud session's allowlist: the pip package carries a protoc
                print(f"  protoc download failed ({ex}); using the protoc of grpcio-tools")
                z.unlink(missing_ok=True)
                sh([sys.executable, "-m", "pip", "install", "--quiet", "grpcio-tools"], tools)
                protoc = [sys.executable, "-m", "grpc_tools.protoc"]
    env = dict(os.environ, GOPATH=str(gopath), GOMODCACHE=str(gopath / "pkg" / "mod"), GOCACHE=str(tools / "gocache"), GOFLAGS="-mod=mod",
               GOTOOLCHAIN=os.environ.get("GOTOOLCHAIN", "auto"),
               PATH=os.pathsep.join([str(go_dir / "bin"), str(protoc_dir / "bin"), str(gopath / "bin"), os.environ.get("PATH", "")]))
    sh([go, "version"], tools, env)
    sh([*protoc, "--version"], tools, env)
    # ---- repository
    if not (repo / ".git").exists():
        sh(["git", "clone", "--depth", "1", "--filter=blob:none", "--sparse", G["url"], repo.name], tools)
        sh(["git", "sparse-checkout", "set", *SPARSE], repo)
        if G.get("commit") and not a.update:   # the pinned commit, so a fresh setup builds the simulator the project's numbers came from
            got = sh(["git", "fetch", "--depth", "1", "origin", G["commit"]], repo, check=False)
            if got.returncode == 0:
                sh(["git", "-c", "advice.detachedHead=false", "checkout", G["commit"]], repo)
            else:
                print(f"  WARNING: the pinned commit {G['commit'][:7]} could not be fetched; building the fork's latest commit instead")
    elif a.update:
        patched = patch_files(a.game)
        if patched:   # back to the fork's version so the update stays clean; the patches go on again below
            tracked = [f for f in patched if sh(["git", "ls-files", "--error-unmatch", f], repo, check=False).returncode == 0]
            if tracked:
                sh(["git", "checkout", "--", *tracked], repo)
            for f in set(patched) - set(tracked):   # files the patches add (the fork has none of its own there): removed
                (repo / f).unlink(missing_ok=True)
        # files a since-removed edit changed (2026-10-16: the retired Bear Form edit left sim/druid/forms.go modified and the checkout failed)
        stale = sh(["git", "diff", "--name-only"], repo).stdout.split()
        if stale:
            sh(["git", "checkout", "--", *stale], repo)
        sh(["git", "fetch", "--depth", "1", "origin", "HEAD"], repo)
        sh(["git", "-c", "advice.detachedHead=false", "checkout", "FETCH_HEAD"], repo)
        new = sh(["git", "rev-parse", "HEAD"], repo).stdout.strip()
        if new != G.get("commit"):
            print(f"  updated to {new}: set GAMES[{a.game!r}]['commit'] in setup.py to it so fresh setups build the same simulator")
    apply_patches(a.game, repo)
    # ---- protobuf code + tools
    if not (gopath / "bin" / f"protoc-gen-go{exe}").exists():
        sh([go, "install", "google.golang.org/protobuf/cmd/protoc-gen-go@latest"], repo, env)
    protos = sorted((repo / "proto").glob("*.proto"))
    if a.update or a.rebuild or not (repo / "sim/core/proto/api.pb.go").exists():
        sh([*protoc, "-I=./proto", "--go_opt=Mgoogle/protobuf/descriptor.proto=google.golang.org/protobuf/types/descriptorpb", "--go_out=./sim/core", *[f"./proto/{p.name}" for p in protos]], repo, env)
    bench_src = repo / "cmd" / G["bench"]
    bench_src.mkdir(parents=True, exist_ok=True)
    src = (HERE / "foreverbench" / "main.go").read_text(encoding="utf-8")
    if a.game == "classic":   # the upstream Player carries enum-based `consumes` instead of `consumables`
        src = src.replace("github.com/wowsims/forever", G["module"]).replace("consumables := &proto.ConsumesSpec{}", "consumables := &proto.Consumes{}").replace("player.Consumables = consumables", "player.Consumes = consumables")
        src = src.replace("// foreverbench:", "// classicbench (generated from foreverbench/main.go by setup.py --game classic):")
    (bench_src / "main.go").write_text(src, encoding="utf-8")
    sh([go, "build", "--tags=with_db", "-o", f"wowsimcli{exe}", "./cmd/wowsimcli"], repo, env)
    sh([go, "build", "--tags=with_db", "-o", f"{G['bench']}{exe}", f"./cmd/{G['bench']}"], repo, env)
    commit = sh(["git", "rev-parse", "--short", "HEAD"], repo).stdout.strip()
    print(f"ready: {repo} at {commit}; run.py finds it through WOW_FOREVER_SIM={repo} or the default tools folder")


if __name__ == "__main__":
    main()
