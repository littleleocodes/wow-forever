"""Build the bench under another name while the pipeline runs (2026-10-09).

    python _reference/data/raidsim/build_next_bench.py [--out foreverbench-next.exe]

`setup.py --rebuild` writes foreverbench.exe, which Windows locks while any bench process runs, so a long queue had to stop for a
simulator patch. This applies the project's patches to the clone (setup.apply_patches), copies foreverbench/main.go into it and builds
the bench to --out with setup.py's Go environment. Running benches keep their own binary. Swap the new one in by renaming (Windows lets
a running executable be renamed; calls already started finish on the old one):
    mv foreverbench.exe foreverbench-old.exe && mv foreverbench-next.exe foreverbench.exe
A process that already loaded specs.json keeps its configs: only add config keys the old binary rejects after the swap.
"""
import argparse
import os
import pathlib
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import setup as S  # noqa: E402


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--out", default="foreverbench-next.exe" if sys.platform.startswith("win") else "foreverbench-next")
    ap.add_argument("--tools", default=os.environ.get("WOW_FOREVER_TOOLS", str(pathlib.Path.home() / ".wow-forever-tools")))
    a = ap.parse_args()
    tools = pathlib.Path(a.tools)
    G = S.GAMES["forever"]
    repo = tools / G["dir"]
    exe = ".exe" if sys.platform.startswith("win") else ""
    go_dir, protoc_dir, gopath = tools / "go", tools / "protoc", tools / "gopath"
    go = go_dir / "bin" / f"go{exe}"
    if not go.exists():
        go = pathlib.Path(subprocess.run(["which", "go"], capture_output=True, text=True).stdout.strip() or "go")
    env = dict(os.environ, GOPATH=str(gopath), GOMODCACHE=str(gopath / "pkg" / "mod"), GOCACHE=str(tools / "gocache"), GOFLAGS="-mod=mod",
               GOTOOLCHAIN=os.environ.get("GOTOOLCHAIN", "auto"),
               PATH=os.pathsep.join([str(go_dir / "bin"), str(protoc_dir / "bin"), str(gopath / "bin"), os.environ.get("PATH", "")]))
    S.apply_patches("forever", repo)
    bench_src = repo / "cmd" / G["bench"]
    bench_src.mkdir(parents=True, exist_ok=True)
    (bench_src / "main.go").write_text((HERE / "foreverbench" / "main.go").read_text(encoding="utf-8"), encoding="utf-8")
    r = subprocess.run([str(go), "build", "--tags=with_db", "-o", a.out, f"./cmd/{G['bench']}"], cwd=str(repo), env=env, capture_output=True, text=True)
    if r.returncode:
        raise SystemExit(f"build failed:\n{r.stdout[-3000:]}\n{r.stderr[-3000:]}")
    print(f"built {repo / a.out}")


if __name__ == "__main__":
    main()
