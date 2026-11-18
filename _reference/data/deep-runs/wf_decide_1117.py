"""After the Windfury Totem switch (wf_buffs_off_1117.py) and the entry's re-race: each build's full-raid DPS before (the committed
record, 107eb67c) and after, and whether the talents need a new search. The rule told to the user (2026-11-17): re-search only when the
build order changes by more than 0.5%, i.e. when a build raced in the entry now beats the Enhancement page's pick (enhancement-open-raid)
by 0.5% or more in a full raid. Writes deep-runs/wf1117/search-needed or deep-runs/wf1117/no-search and prints the table."""
import json
import pathlib
import subprocess

ROOT = pathlib.Path(__file__).resolve().parents[3]
REC = "shaman/research/raid/raidsim/enhancement-dps-environments.json"
M = ROOT / "_reference/data/deep-runs/wf1117"
PICK, BAR, BEFORE = "enhancement-open-raid", 0.005, "107eb67c"


def raid(d):
    return {r["label"]: (r.get("split"), r["dps"]["raid"]) for r in d["results"] if r.get("dps", {}).get("raid")}


before = raid(json.loads(subprocess.run(["git", "-C", str(ROOT), "show", f"{BEFORE}:{REC}"], capture_output=True, text=True,
                                        encoding="utf-8", check=True).stdout))
after = raid(json.loads((ROOT / REC).read_text(encoding="utf-8")))
pick = after[PICK][1]
print(f"{'build':45s} {'split':9s} {'before':>8s} {'after':>8s} {'change':>7s} {'vs pick':>8s}")
for lab, (split, dps) in sorted(after.items(), key=lambda kv: -kv[1][1]):
    b = before.get(lab, (None, None))[1]
    ch = f"{dps / b - 1:+.1%}" if b else "-"
    print(f"{lab:45s} {split or '':9s} {b or 0:8.1f} {dps:8.1f} {ch:>7s} {dps / pick - 1:+8.2%}")
lead = max(after.items(), key=lambda kv: kv[1][1])
need = lead[0] != PICK and lead[1][1] >= pick * (1 + BAR)
M.mkdir(parents=True, exist_ok=True)
(M / ("search-needed" if need else "no-search")).write_text(
    f"{lead[0]} {lead[1][1]:.1f} against {PICK} {pick:.1f} ({lead[1][1] / pick - 1:+.2%}; bar {BAR:.1%})\n", encoding="utf-8")
print(f"lead: {lead[0]} {lead[1][1]:.1f} against {PICK} {pick:.1f} ({lead[1][1] / pick - 1:+.2%}) -> "
      f"{'SEARCH: a build beats the page pick by the bar' if need else 'no search: the page pick holds'}")
