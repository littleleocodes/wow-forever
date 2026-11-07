"""Page audit (2026-11-07, user: "constantly be auditing the GitHub pages for the classes ... make sure that any talent tree calculator links
are up to date with the builds"). Reads the class pages the way a player does and lists what would mislead one:

    python _reference/data/page_lint.py [classes] [--pushed] [--live] [--write]

  links      a relative link on a player page that leads nowhere;
  talents    a talentsforever.com link whose version label is not the one our talent order follows, whose digits make no legal build, or
             that differs from the link of the build the same line names (the page is behind its build);
  guide      a by-level guide whose build is not the one its spec page leads with;
  keys       a key whose spell on the hand-written keybinds page differs from the guide's keys block at 60;
  steps      a "How to play" line of a leveling page that leveling-steps.json no longer holds;
  macros     a macro on a keybinds or macro page that casts something the class cannot have;
  names      a bold name on a player page that is no spell, talent or known word of any class (a removed talent keeps turning up here);
  coverage   a recommended leveling spec without a by-level guide or a class without a keybinds page.

--pushed reads origin/main instead of the working tree: what the player sees on GitHub. --live also asks the outside world:
talentsforever.com's code version and talent order against render_start_here.TF_CODE_VERSION and our data, the simulator's upstream
master against the pin, and the client build of Blizzard's UI mirror against our data build (a new patch shows up here first).
--write puts the report in _reference/page-lint.md (generated). rebuild.py's regen step runs it. Exit code 0 always: it reports.

Why --live matters: the site moved from code version 7 to 12 between 2026-10-17 and 11-04 and our label stayed at 7; the site read our
digits in the old order and 216 of 330 links opened other talents, among them every mage, paladin and rogue link.
"""
import argparse
import datetime
import json
import pathlib
import re
import subprocess
import sys
import urllib.request

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[1]
sys.path[:0] = [str(HERE / "fightlab"), str(HERE / "scorer"), str(HERE)]
import level_guides as LG  # noqa: E402
import render_start_here as RS  # noqa: E402
import spec_modes as SM  # noqa: E402
import data_build as DB  # noqa: E402

TF = re.compile(r"https://talentsforever\.com/([a-z]+)/60/([0-9-]*?)-(\d+)(?![0-9-])")
LINK = re.compile(r"\]\(([^)#\s]+?\.md)(#[^)]*)?\)")
BOLD = re.compile(r"\*\*([A-Z][A-Za-z':-]+(?: (?:of|the|and|on|to|in|[A-Z][A-Za-z':-]+)){0,4})\*\*")
WORDS = {"Keys to set", "Your keys in this stage", "The trainer teaches", "New ranks to buy", "Talents", "What to press", "If the fight goes wrong", "The build",
         "Recommended", "Level by level", "Keybinds", "Signature spells", "Bar", "Rank", "Spec", "Note", "Open", "Advanced", "How to play", "Rotation", "Build",
         "Caveats", "Damage", "Tanking", "Healing", "Wand", "Melee", "Attack", "Auto Shot", "Shadow Trance", "Clearcasting"}
USER_AGENT = {"User-Agent": "wow-forever-page-lint"}


class Tree:
    """The pages: the working tree, or origin/main with --pushed."""

    def __init__(self, pushed):
        self.ref = "origin/main" if pushed else None
        if pushed:
            names = subprocess.run(["git", "ls-tree", "-r", "--name-only", "origin/main"], cwd=ROOT, capture_output=True, text=True, encoding="utf-8").stdout
            self.names = set(names.splitlines())

    def exists(self, p):
        return p in self.names if self.ref else (ROOT / p).exists()

    def list(self, folder):
        if self.ref:
            return sorted(n for n in self.names if n.startswith(folder + "/") and n.count("/") == folder.count("/") + 1 and n.endswith(".md"))
        return sorted(q.relative_to(ROOT).as_posix() for q in (ROOT / folder).glob("*.md"))

    def text(self, p):
        if self.ref:
            return subprocess.run(["git", "show", f"{self.ref}:{p}"], cwd=ROOT, capture_output=True).stdout.decode("utf-8", "replace")
        return (ROOT / p).read_text(encoding="utf-8")


def talents(cls):
    return json.load(open(HERE / "forever-talents" / f"{cls}.json", encoding="utf-8"))["trees"]


def legal(cls, body):
    """None, or why the digits are no legal build in today's order."""
    total = 0
    trees = talents(cls)
    parts = body.split("-")
    if len(parts) > len(trees):
        return f"{len(parts)} segments"
    for s, tr in zip(parts, trees):
        ts = tr["talents"]
        if len(s) > len(ts):
            return f"more digits than the {tr['name']} tree has talents"
        per = {}
        for c, t in zip(s, ts):
            d = int(c)
            if d > t["maxRank"]:
                return f"{t['name']} {d} over its {t['maxRank']} ranks"
            per[t["row"]] = per.get(t["row"], 0) + d
            total += d
        for c, t in zip(s, ts):
            if int(c) and sum(v for r, v in per.items() if r < t["row"]) < 5 * t["row"]:
                return f"{t['name']} above its tier"
    return f"{total} points" if total > 51 else None


def builds(tree, cls):
    d = json.loads(tree.text(f"{cls}/research/talents/forever/proposed-builds.json"))
    return {b["id"]: b for b in (d["builds"] if isinstance(d, dict) else d)}


def body_of(cls, b):
    return TF.match(RS.tf_link(cls, RS.flat(b))).group(2)


def known_names():
    names = set(WORDS)
    for cls in SM.CLASSES:
        names |= set(LG.book(cls))
        names |= {t["name"] for tr in talents(cls) for t in tr["talents"]}
        names |= {tr["name"] for tr in talents(cls)}
    for v in SM.HYBRID_NAMES.values():
        names |= {x for x in (v if isinstance(v, tuple) else (v,)) if isinstance(x, str)}
        for x in (v if isinstance(v, tuple) else (v,)):
            if isinstance(x, dict):
                names |= {y for y in x.values() if isinstance(y, str) and len(y) < 30}
    return names


def check_links(tree, cls, out):
    pages = tree.list(f"{cls}/leveling") + tree.list(f"{cls}/raid") + [f"{cls}/README.md"]
    for p in pages:
        for m in LINK.finditer(tree.text(p)):
            link = m.group(1)
            if link.startswith("http"):
                continue
            target = pathlib.PurePosixPath(p).parent / link
            parts = []
            for seg in target.parts:
                if seg == "..":
                    parts.pop()
                else:
                    parts.append(seg)
            if not tree.exists("/".join(parts)):
                out.append(("links", cls, f"{p}: `{link}` leads nowhere"))
    return pages


def check_talents(tree, cls, pages, out):
    bs = builds(tree, cls)
    n = 0
    for p in pages:
        for line in tree.text(p).splitlines():
            for m in TF.finditer(line):
                c, body, ver = m.group(1), m.group(2), m.group(3)
                n += 1
                if c not in SM.CLASSES:
                    continue
                if ver != RS.TF_CODE_VERSION:
                    out.append(("talents", cls, f"{p}: a link says version {ver}, our order is version {RS.TF_CODE_VERSION}"))
                    continue
                why = legal(c, body)
                if why:
                    out.append(("talents", cls, f"{p}: `{body}`: {why}"))
                ids = re.findall(r"builds/([a-z0-9-]+)\.md", line)
                if len(ids) == 1 and ids[0] in bs and c == cls and body_of(cls, bs[ids[0]]) != body:
                    out.append(("talents", cls, f"{p}: the link beside {ids[0]} is not that build's (`{body}`, the build `{body_of(cls, bs[ids[0]])}`)"))
    return n


def check_guides(tree, cls, out):
    data = LG.load(cls)
    if not data:
        out.append(("coverage", cls, "no by-level guide yet"))
        return
    if not tree.exists(f"{cls}/leveling/keybinds.md"):
        out.append(("coverage", cls, "no keybinds page"))
    for g in data["guides"]:
        slug = SM.spec_slug(cls, g["spec"])
        page, guide = f"{cls}/leveling/{slug}.md", f"{cls}/leveling/{LG.page_name(cls, g['spec'])}"
        if not tree.exists(guide):
            out.append(("coverage", cls, f"{guide} is missing"))
            continue
        lead = re.search(r"\*\*\[[^\]]*\]\([^)]*builds/([a-z0-9-]+)\.md\)\*\*.*?(https://talentsforever\.com/\S+?)\)", tree.text(page)) if tree.exists(page) else None
        mine = TF.search(tree.text(guide))
        if lead and mine and TF.search(lead.group(2)) and TF.search(lead.group(2)).group(2) != mine.group(2):
            out.append(("guide", cls, f"{guide} teaches `{mine.group(2)}`, {page} leads with {lead.group(1)} `{TF.search(lead.group(2)).group(2)}`"))
        check_keys(tree, cls, g, out)


def check_keys(tree, cls, g, out):
    p = f"{cls}/leveling/keybinds.md"
    if not tree.exists(p) or not g.get("keys"):
        return
    rows, suffix = {}, ""
    bar = False
    for line in tree.text(p).splitlines():
        if line.startswith("## "):
            bar = line.startswith("## Bar")
            suffix = " (prowling)" if "prowling" in line else " (bear)" if "Bear Form" in line else " (cat)" if "Cat Form" in line else ""
        m = re.match(r"\| ([^|]+?) \| ([^|]*?) \|", line)
        if bar and m and m.group(1) not in ("Key", "---"):
            for k in re.split(r", ", m.group(1)):
                k = re.sub(r" \(.*side button\)", "", k).strip()
                rows[k + suffix if not k.startswith("Shift") else k] = m.group(2)
    for k in LG.key_slots(g["keys"]):
        key = k["key"]
        if key not in rows:
            continue
        have = rows[key]
        binds = sorted(k["binds"], key=lambda b: b["from"])
        if not binds:
            if have.strip() and not have.strip().startswith("Free"):
                out.append(("keys", cls, f"{key}: free in the guide, `{have[:50]}` on the keybinds page"))
            continue
        last = binds[-1].get("spell") or binds[-1].get("text")
        if have.strip() == "Free":
            out.append(("keys", cls, f"{key}: {last} in the guide, free on the keybinds page"))
        elif binds[-1].get("spell") and last not in have and not any((b.get("spell") or "") in have for b in binds):
            out.append(("keys", cls, f"{key}: {last} in the guide, `{have[:50]}` on the keybinds page"))


def check_macros(tree, cls, out):
    for p in (f"{cls}/leveling/keybinds.md", f"{cls}/macros.md"):
        if tree.exists(p):
            check_macro_page(tree, cls, p, out)
    if not tree.exists(f"{cls}/macros.md"):
        out.append(("coverage", cls, "no macro page"))


def check_macro_page(tree, cls, p, out):
    book = set(LG.book(cls)) | {t["name"] for tr in talents(cls) for t in tr["talents"]} | {"Attack", "Shoot", "Auto Shot"}
    fence = False
    for line in tree.text(p).splitlines():
        if line.startswith("```"):
            fence = not fence
            continue
        if not fence:
            continue
        m = re.match(r"(/cast|/castsequence|#showtooltip)\s+(.*)", line)
        if not m or not m.group(2):
            continue
        text = re.sub(r"\[[^\]]*\]", "", re.sub(r"reset=\S+", "", m.group(2))).replace("!", "")
        for name in (x.strip() for x in re.split(r"[,;]", text)):
            if name and name not in book:
                out.append(("macros", cls, f"`{line}`: {name} is no {cls} spell or talent"))


def check_steps(tree, cls, pages, out):
    """The "How to play" list of a leveling page against leveling-steps.json: a page left behind by a corrected rotation."""
    steps = json.load(open(HERE / "leveling-steps.json", encoding="utf-8")).get(cls, {})
    allowed = {x for v in steps.values() for k in ("before", "steps", "between") for x in v.get(k) or []}
    for p in pages:
        if "/leveling/" not in p or p.endswith(("README.md", "keybinds.md", "-by-level.md")):
            continue
        m = re.search(r"## How to play(.*?)(?=\n## )", tree.text(p), re.S)
        for ln in (m.group(1).splitlines() if m else []):
            line = re.sub(r"^(\d+\.|-)\s+", "", ln).strip()
            if re.match(r"^(\d+\.|-)\s", ln) and len(line) > 25 and line not in allowed:
                out.append(("steps", cls, f"{p}: `{line[:90]}` is not in leveling-steps.json"))


def check_names(tree, cls, pages, known, out):
    seen = {}
    for p in pages:
        if p.endswith("keybinds.md"):
            continue
        for n in BOLD.findall(tree.text(p)):
            if n not in known and not n.endswith(("s:", ":")) and n.rstrip(":") not in known:
                seen[n] = seen.get(n, 0) + 1
    for n, c in sorted(seen.items(), key=lambda kv: -kv[1])[:12]:
        out.append(("names", cls, f"**{n}** ({c}x) is no spell or talent"))


def fetch(url):
    try:
        return urllib.request.urlopen(urllib.request.Request(url, headers=USER_AGENT), timeout=30).read().decode("utf-8", "replace")
    except OSError:   # Windows' certificate store refuses some sites to urllib; popular_builds.py met the same
        return subprocess.run(["curl", "-s", "-A", "Mozilla/5.0", url], capture_output=True, timeout=60).stdout.decode("utf-8", "replace")


def live(out):
    notes = []
    try:
        pop = fetch("https://talentsforever.com/popular.js")
        vers = sorted({int(v) for v in re.findall(r"[a-z]+/60/[0-9-]*-(\d+)\"", pop)})
        site = str(vers[-1]) if vers else "?"
        js = fetch("https://talentsforever.com/talents.js")
        i = js.index("window.TALENT_DATA = ") + len("window.TALENT_DATA = ")
        data = json.JSONDecoder().raw_decode(js[i:])[0]
        same = all([[t["name"] for t in tr["talents"]] for tr in data[c.capitalize()]["trees"]] == [[t["name"] for t in tr["talents"]] for tr in talents(c)] for c in SM.CLASSES)
        notes.append(f"talentsforever.com: code version {site}, its talent order {'equals' if same else 'DIFFERS from'} ours; our label {RS.TF_CODE_VERSION}")
        if same and site != RS.TF_CODE_VERSION:
            out.append(("talents", "all", f"the site is on version {site} with our order: set render_start_here.TF_CODE_VERSION to {site} and regenerate"))
        if not same:
            out.append(("talents", "all", f"the site's talent order moved past our data (version {site}): keep the label on the version our order follows, refresh the data"))
    except Exception as e:   # noqa: BLE001
        notes.append(f"talentsforever.com: no answer ({type(e).__name__})")
    try:
        sys.path.insert(0, str(HERE / "raidsim"))
        import setup as ST
        repo = ST.checkout()
        subprocess.run(["git", "-C", str(repo), "fetch", "-q", "--filter=blob:none", "origin", "master"], capture_output=True, timeout=120)
        pin = ST.GAMES["forever"]["commit"]
        n = subprocess.run(["git", "-C", str(repo), "rev-list", "--count", f"{pin}..FETCH_HEAD"], capture_output=True, text=True).stdout.strip()
        notes.append(f"wowsims/forever: {n} commits past our pin {pin[:9]}")
        if n and int(n) > 0:
            subj = subprocess.run(["git", "-C", str(repo), "log", "--no-merges", "--format=%s", f"{pin}..FETCH_HEAD", "--", "sim", "assets/database"], capture_output=True, text=True).stdout
            db = [s for s in subj.splitlines() if s.startswith("[DB]")]
            if db:
                out.append(("patch", "all", f"the simulator has new game data past the pin: {db[0][:90]}"))
    except Exception as e:   # noqa: BLE001
        notes.append(f"wowsims/forever: no answer ({type(e).__name__})")
    try:
        msg = json.loads(fetch("https://api.github.com/repos/Gethe/wow-ui-source/branches/forever"))["commit"]["commit"]
        notes.append(f"Blizzard's UI mirror, branch forever: {msg['message'][:24]} ({msg['author']['date'][:10]}); our data {DB.BUILD}")
        m = re.search(r"\((\d{5})\)", msg["message"])
        if m and m.group(1) not in str(DB.BUILD):
            out.append(("patch", "all", f"the client is on build {m.group(1)}, our data on {DB.BUILD}: look for new notes and a data refresh"))
    except Exception as e:   # noqa: BLE001
        notes.append(f"Blizzard's UI mirror: no answer ({type(e).__name__})")
    return notes


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("classes", nargs="*")
    ap.add_argument("--pushed", action="store_true")
    ap.add_argument("--live", action="store_true")
    ap.add_argument("--write", action="store_true")
    a = ap.parse_args()
    classes = [c for c in a.classes if c in SM.CLASSES] or SM.CLASSES
    tree = Tree(a.pushed)
    known = known_names()
    out, links = [], 0
    for cls in classes:
        pages = check_links(tree, cls, out)
        links += check_talents(tree, cls, pages, out)
        check_guides(tree, cls, out)
        check_macros(tree, cls, out)
        check_steps(tree, cls, pages, out)
        check_names(tree, cls, pages, known, out)
    notes = live(out) if a.live else []
    order = ["patch", "talents", "links", "guide", "keys", "steps", "macros", "coverage", "names"]
    src = "origin/main" if a.pushed else "the working tree"
    o = ["# Page audit", "", f"> Generated by `_reference/data/page_lint.py` on {datetime.date.today().isoformat()} from {src}: {len(classes)} classes, {links} talent links. Do not hand-edit.", ""]
    o += [f"- {n}" for n in notes] + ([""] if notes else [])
    o += ["| Check | Findings |", "|---|---|"] + [f"| {k} | {sum(1 for f in out if f[0] == k)} |" for k in order] + [""]
    for k in order:
        rows = [f for f in out if f[0] == k]
        if rows:
            o += [f"## {k}", ""] + [f"- {c}: {t}" for _, c, t in rows[:80]] + ([f"- and {len(rows) - 80} more"] if len(rows) > 80 else []) + [""]
    text = "\n".join(o) + "\n"
    if a.write:
        (ROOT / "_reference" / "page-lint.md").write_text(text, encoding="utf-8", newline="\n")
    print(text)


if __name__ == "__main__":
    main()
