"""Which raid simulator a record's numbers came from, and how the pages name it (2026-10-22, sim-port: `_reference/sim-port.md`).

Until 2026-10-18 every raid number was simulated with the ElliotWood/Forever fork of wowsims (deleted in the night of 2026-10-17/18);
since then the pipeline runs the official github.com/wowsims/forever. A record's `sim` block (raidsim/run.py) names the checkout it ran
in (`repo`) and the `commit`; records written since 2026-10-22 also carry `simulator` and `client` (the game client the simulator's
spell and item data come from). Older records are read through the commit table below. The renderers print what each record says, so
a page whose numbers are still the fork's says so, and a footer names the client build of the simulation, not only the talent data's.

    import sim_info as SI
    SI.label(rec["sim"])              # "the ElliotWood/Forever fork (deleted 2026-10-18) at 2ce8265 (client 1.60.1.70291)"
    SI.summary([r["sim"] for r in records])
"""
import functools
import os
import pathlib
import re
import subprocess

OFFICIAL, FORK, CLASSIC = "official", "fork", "classic"
NAME = {OFFICIAL: "the official wowsims/forever simulator", FORK: "the ElliotWood/Forever fork (deleted 2026-10-18)",
        CLASSIC: "the upstream wowsims/classic simulator (Classic Era)"}
SHORT = {OFFICIAL: "wowsims/forever", FORK: "ElliotWood/Forever fork", CLASSIC: "wowsims/classic"}
URL = {OFFICIAL: "https://github.com/wowsims/forever", FORK: "https://github.com/ElliotWood/Forever (deleted 2026-10-18)",
       CLASSIC: "https://github.com/wowsims/classic"}
SITE = {OFFICIAL: "https://wowsims.com/forever", FORK: "https://elliotwood.github.io/Forever/forever (gone)", CLASSIC: "https://wowsims.github.io/classic"}
PORT_DATE = "2026-10-18"
# The fork's commits our records name and the client build of their data (setup.py's pin history; CLAUDE.md). b7083fa was marked
# 70425 but carried the 14-15 Oct spell store (audit 2026-10-17 finding 43). 40be98e predates the project's client tracking.
FORK_COMMITS = {"40be98e": None, "b0f0df3": "1.60.1.70205", "2ce8265": "1.60.1.70291", "b7083fa": "1.60.1.70425"}
CLIENT_NOTE = {"b7083fa": "its spell data of 14-15 Oct"}
OFFICIAL_COMMITS = {"09e7398": "1.60.1.70450", "30f67f5": "1.60.1.70450",   # 30f67f5: 2026-10-22 master (mage hotfix of 10-20, items of 10-22)
                    "b90e2b9": "1.60.1.70707",   # b90e2b9: 2026-10-30 master (live client, hotfix pushes 113531/113554; paladin, priest not yet)
                    "54ceac6": "1.60.1.70707",   # 54ceac6: 2026-10-31 master (the paladin and priest ports of push 113554, items of 10-31)
                    "bac92db": "1.60.1.70707"}   # bac92db: 2026-11-02 master (same game data; book ranks registered, raid buffs as rank selects at the trainer's rank, Ferocious Bite attack power, Seal of Command, hunter pet attack power, Omen per Hurricane tick)
# Racials of records written before run.py recorded them (audit 2026-10-18 rows 79 and 96): the final 2ce8265 races of 2026-10-15/16 ran
# race-neutral (WOW_FOREVER_NO_RACIALS=1, HANDOFF.md), the b7083fa confirm runs of 2026-10-16/17 did not (sweep_70425.sh).
RACIALS_BY_COMMIT = {"2ce8265": ("2026-10-15", "off"), "b7083fa": ("2026-10-16", "on")}
DIRS = {"wowsims-forever": OFFICIAL, "wowsims-forever-next": OFFICIAL, "forever-repo": FORK, "forever-upstream": FORK, "classic-repo": CLASSIC}


def _tools():
    return pathlib.Path(os.environ.get("WOW_FOREVER_TOOLS", pathlib.Path.home() / ".wow-forever-tools"))


def _git(repo, *args):
    try:
        r = subprocess.run(["git", "-C", str(repo), *args], capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=20)
        return r.stdout.strip() if r.returncode == 0 else ""
    except Exception:   # noqa: BLE001 - no git or no clone: fall back to the tables
        return ""


def pin():
    """The pinned simulator commit (raidsim/setup.py GAMES["forever"]["commit"], 7 characters)."""
    m = re.search(r'"forever":\s*\{.*?"commit":\s*"([0-9a-f]{7})', (pathlib.Path(__file__).resolve().parent / "raidsim" / "setup.py")
                  .read_text(encoding="utf-8"), re.S)
    return m.group(1) if m else "?"


def commit_of_date(date):
    """The pin a record of that date ran on when it names no commit (setup.py's pin history): 40be98e until 2026-10-03, b0f0df3 until
    2026-10-08, 2ce8265 until 2026-10-16, b7083fa until the port on 2026-10-18, then the current pin."""
    d = (date or "")[:10]
    for until, c in (("2026-10-03", "40be98e"), ("2026-10-08", "b0f0df3"), ("2026-10-16", "2ce8265"), (PORT_DATE, "b7083fa")):
        if d and d < until:
            return c
    return pin()


@functools.lru_cache(maxsize=None)
def _in_official(commit):
    return bool(commit) and bool(_git(_tools() / "wowsims-forever", "rev-parse", "--verify", "--quiet", f"{commit}^{{commit}}"))


def kind(sim, game=None):
    """official, fork or classic for a record's `sim` block (a dict, or a bare commit string)."""
    sim = sim if isinstance(sim, dict) else {"commit": sim}
    if (game or sim.get("game")) in ("classic-era", "classic"):
        return CLASSIC
    s = (sim.get("simulator") or "").lower()
    if s:
        return OFFICIAL if s.startswith("wowsims/forever") else CLASSIC if "classic" in s else FORK
    d = pathlib.Path(str(sim.get("repo") or "")).name
    if d in DIRS:
        return DIRS[d]
    c = (sim.get("commit") or "")[:7]
    if c in FORK_COMMITS:
        return FORK
    if c in OFFICIAL_COMMITS or _in_official(c):
        return OFFICIAL
    return FORK if (sim.get("date") or "9999")[:10] < PORT_DATE else OFFICIAL


@functools.lru_cache(maxsize=None)
def client_of_checkout(repo):
    """The game client of a checkout's data: the official clone's last spell-store regeneration ("[Spells] Regenerate spelldata from
    1.60.1.70450"), else the fork's assets/db_inputs/forever_client_build.txt; None when neither says."""
    repo = pathlib.Path(repo)
    for rel in ("sim/core/spelldata/spells_auto_gen.go", "assets/database/db.json"):
        m = re.search(r"\b1\.60\.1\.\d{5}\b", _git(repo, "log", "-20", "--format=%s", "--", rel))
        if m:
            return m.group(0)
    f = repo / "assets" / "db_inputs" / "forever_client_build.txt"
    if f.exists():
        m = re.search(r"\b1\.60\.1\.\d{5}\b", f.read_text(encoding="utf-8", errors="replace"))
        if m:
            return m.group(0)
    return None


def client(sim):
    """The client build of a record's simulation, or None."""
    sim = sim if isinstance(sim, dict) else {"commit": sim}
    if sim.get("client"):
        return sim["client"]
    c = (sim.get("commit") or "")[:7]
    if c in FORK_COMMITS:
        return FORK_COMMITS[c]
    if c in OFFICIAL_COMMITS:
        return OFFICIAL_COMMITS[c]
    return None


def client_text(sim, short=False):
    cl = client(sim)
    c = ((sim if isinstance(sim, dict) else {"commit": sim}).get("commit") or "")[:7]
    if not cl:
        return "client not recorded"
    note = CLIENT_NOTE.get(c)
    return f"client {cl[-5:] if short else cl}" + (f", {note}" if note and not short else "")


def racials(sim, date=None):
    """"on", "off" or None (not recorded): the record's own switch (run.py, since 2026-10-18), else RACIALS_BY_COMMIT by date."""
    sim = sim if isinstance(sim, dict) else {"commit": sim}
    if sim.get("racials") in ("on", "off"):
        return sim["racials"]
    c = (sim.get("commit") or "")[:7]
    since, val = RACIALS_BY_COMMIT.get(c, ("9999", None))
    d = (date or sim.get("date") or "")[:10]
    return val if d and d >= since else None


def name(sim, short=False):
    return (SHORT if short else NAME)[kind(sim)]


def label(sim, short=False):
    """"the official wowsims/forever simulator at 09e7398 (client 1.60.1.70450)"; short: "wowsims/forever 09e7398 (client 70450)"."""
    sim = sim if isinstance(sim, dict) else {"commit": sim}
    c = (sim.get("commit") or "?")[:7]
    if short:
        return f"{name(sim, True)} {c} ({client_text(sim, True)})"
    return f"{name(sim)} at {c} ({client_text(sim)})"


def summary(sims, short=False):
    """One phrase for the simulators behind a page's numbers: identical labels once, several joined ("... at 2ce8265 (client ...) and
    at b7083fa (client ...)" when they share a simulator)."""
    seen, by = [], {}
    for s in sims:
        if not s:
            continue
        s = s if isinstance(s, dict) else {"commit": s}
        k = kind(s)
        c = (s.get("commit") or "?")[:7]
        if (k, c) in seen:
            continue
        seen.append((k, c))
        by.setdefault(k, []).append(s)
    if not seen:
        return None
    parts = []
    for k, ss in by.items():
        commits = [f"{(s.get('commit') or '?')[:7]} ({client_text(s, short)})" for s in ss]
        parts.append(f"{SHORT[k] if short else NAME[k]} at " + (", ".join(commits[:-1]) + " and " + commits[-1] if len(commits) > 1 else commits[0]))
    return "; ".join(parts)


def clients(sims):
    """The distinct client builds of a set of records (None for unrecorded ones left out), in order."""
    out = []
    for s in sims:
        cl = client(s) if s else None
        if cl and cl not in out:
            out.append(cl)
    return out


def identity(repo):
    """What run.py records next to the commit (2026-10-22): the simulator and the client build of its data."""
    k = DIRS.get(pathlib.Path(str(repo)).name)
    if not k:
        url = _git(repo, "remote", "get-url", "origin").lower()
        k = OFFICIAL if "wowsims/forever" in url else CLASSIC if "wowsims/classic" in url else FORK
    return {"simulator": {OFFICIAL: "wowsims/forever", FORK: "ElliotWood/Forever", CLASSIC: "wowsims/classic"}[k],
            "client": client_of_checkout(str(repo))}
