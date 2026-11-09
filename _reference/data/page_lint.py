"""Page audit (2026-11-07, user: "constantly be auditing the GitHub pages for the classes ... make sure that any talent tree calculator links
are up to date with the builds"). Reads the class pages the way a player does and lists what would mislead one:

    python _reference/data/page_lint.py [classes] [--pushed] [--live] [--write]

  links      a relative link on a player page that leads nowhere;
  talents    a talentsforever.com link whose version label is not the one our talent order follows, whose digits make no legal build, or
             that differs from the link of the build the same line names (the page is behind its build);
  guide      a by-level guide whose build is not the one its spec page leads with;
  build      a talent a spec page's guide names that the page's lead build does not take (a guide left behind by its build);
  dead       a talent of a spec page's build that only improves spells or forms the page never uses, with no word on why it is there;
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
        if g is data["guides"][0]:   # the keybinds page is written for the class's first guide; other specs keep their own keys (2026-11-07)
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


# Racials a macro may cast (the class books hold none). Names as the check reads them, "!" removed: Eureka! is the Gnome's
# (2026-11-08, user: a macro so they use it more).
RACIALS = {"Eureka", "Stoneform", "Blood Fury", "Berserking"}


def check_macro_page(tree, cls, p, out):
    book = set(LG.book(cls)) | {t["name"] for tr in talents(cls) for t in tr["talents"]} | {"Attack", "Shoot", "Auto Shot"} | RACIALS
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
    steps = json.loads(tree.text("_reference/data/leveling-steps.json") or "{}").get(cls, {})   # the same tree as the pages (--pushed)
    allowed = {x for v in steps.values() for k in ("before", "steps", "between") for x in v.get(k) or []}
    for p in pages:
        if "/leveling/" not in p or p.endswith(("README.md", "keybinds.md", "-by-level.md")):
            continue
        m = re.search(r"## How to play(.*?)(?=\n## )", tree.text(p), re.S)
        for ln in (m.group(1).splitlines() if m else []):
            line = re.sub(r"^(\d+\.|-)\s+", "", ln).strip()
            if re.match(r"^(\d+\.|-)\s", ln) and len(line) > 25 and line not in allowed:
                out.append(("steps", cls, f"{p}: `{line[:90]}` is not in leveling-steps.json"))


NEGATE = ("no ", "without", "not ", "lacks", "skip", "instead of", "unlike", "never", "nor ", "other builds", "drop",
          # another player's talent ("a feral druid's Leader of the Pack", 2026-11-09)
          "druid's ", "shaman's ", "paladin's ", "priest's ", "mage's ", "warrior's ", "rogue's ", "hunter's ", "warlock's ")
NEGATE_AFTER = ("is not in", "are not in", "isn't", "aren't", "not taken", "lacks", "does not take", "doesn't take", "is missing",
                "are missing", "not in this build", "not in the build", "the build skips", "this build skips", "a build that takes",
                "builds that take", "if your build has")


WORDNUM = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5"}
# "**Holy Power** (five ranks)", "**Totemic Focus** (5 points, ...)", "this build's 5 points in **Naturalist**", "two ranks of **X**"
# (a level path, "(1 rank at 23, all 3 by 53)", is no claim about the build at 60)
RANK_SAID = re.compile(r"\*\*(?P<n1>[^*]+)\*\* \((?P<k1>\d|one|two|three|four|five) (?:points?|ranks?)\b(?! at \d)"
                       r"|\b(?P<k2>\d|one|two|three|four|five) (?:points?|ranks?) (?:in|of) \*\*(?P<n2>[^*]+)\*\*", re.I)


def check_build(tree, cls, pages, out):
    """A talent the spec page's guide ("Why this rotation" / "How to heal") names in bold that the page's lead build does not take,
    unless the words before it say so (no, without, not, lacks, never ...). Found 2026-11-07: the Retribution leveling guide of 10-25
    still taught Holy Conduit and talent levels of an older build while the page led with 12/9/30."""
    trees = talents(cls)
    tnames = {t["name"] for tr in trees for t in tr["talents"]}
    for p in pages:
        if not re.match(rf"{cls}/(leveling|raid)/[a-z0-9-]+\.md$", p) or p.endswith(("README.md", "keybinds.md", "-by-level.md")):
            continue
        text = tree.text(p)
        m = TF.search(text)
        sec = re.search(r"## (Why this rotation|How to heal)(.*?)(?=\n## |\Z)", text, re.S)
        if not m or not sec:
            continue
        have = {t["name"] for s, tr in zip(m.group(2).split("-"), trees) for c, t in zip(s, tr["talents"]) if c.isdigit() and int(c)}
        body = sec.group(2)
        def negated(b):
            if any(k in body[max(0, b.start() - 40):b.start()].lower() for k in NEGATE):
                return True
            # or after it: "Riposte is not in this build", "Setup, which this build lacks" (2026-11-08)
            if any(k in body[b.end():b.end() + 45].lower() for k in NEGATE_AFTER):
                return True
            # 2026-11-09: the sentence it stands in. A list after "has no" / "takes no" / "without" ("This build has no **Riposte**,
            # **Preparation** ... or **Relentless Strikes**"), and a build-membership phrase later in the sentence ("**Eclipse** (each
            # **Wrath** ...) is not in the raid build")
            s0 = max(body.rfind(". ", 0, b.start()), body.rfind("\n", 0, b.start())) + 1
            e = [x for x in (body.find(". ", b.end()), body.find("\n", b.end())) if x >= 0]
            s1 = min(e) if e else len(body)
            before, after = body[s0:b.start()], body[b.end():s1].lower()
            nm = re.search(r"\b(?:has|have|takes|take|with) no\b|\bwithout\b|\bgives up\b|\btakes neither\b", before, re.I)
            if nm and re.fullmatch(r"(?:\s*\*\*[^*]+\*\*\s*(?:,|\bor\b|\band\b)?)*\s*", before[nm.end():]):
                return True
            return any(k in after for k in NEGATE_AFTER + ("never uses", "this rotation never", "not in the raid build", "does not apply",
                                                          "not been simulated"))
        miss = sorted({b.group(1) for b in BOLD.finditer(body) if b.group(1) in tnames and b.group(1) not in have and not negated(b)})
        if miss:
            out.append(("build", cls, f"{p}: the guide names {', '.join(miss)}, which the page's build does not take"))
        # the reverse (2026-11-09): the guide says the build lacks a talent it takes. The Holy paladin raid guide said "This build takes
        # no **Holy Shock**" and "takes neither **Holy Shock** nor **Light's Vigil**" after the deep search's new winner took both
        def says_lacks(b):
            s0 = max(body.rfind(". ", 0, b.start()), body.rfind("\n", 0, b.start())) + 1
            e = [x for x in (body.find(". ", b.end()), body.find("\n", b.end())) if x >= 0]
            before, after = body[s0:b.start()], body[b.end():min(e) if e else len(body)].lower()
            # a condition ("if your build has no ...", "Before 25 you have no **Stormstrike**") is no claim
            if re.search(r"\bif\b|\bwhen\b|\bunless\b|\bbefore\b|\buntil\b", before, re.I):
                return False
            nm = re.search(r"\b(?:takes|take|has|have) (?:no|neither)\b|\bdoes not take\b|\bskips\b", before, re.I)
            if nm and re.fullmatch(r"(?:\s*\*\*[^*]+\*\*\s*(?:,|\bor\b|\band\b|\bnor\b)?)*\s*", before[nm.end():]):
                return True
            return bool(re.match(r"\s*(?:\([^)]*\)\s*)?(?:is|are) not (?:in|taken)|\s*(?:,\s*)?which (?:this|the) build (?:lacks|skips)", after))
        wrong = sorted({b.group(1) for b in BOLD.finditer(body) if b.group(1) in have and says_lacks(b)})
        if wrong:
            out.append(("build", cls, f"{p}: the guide says the build lacks {', '.join(wrong)}, which the page's build takes"))
        # and the points it gives a talent (2026-11-09: a guide that says "four ranks" after the build went to five)
        ranks = {t["name"]: int(c) for s, tr in zip(m.group(2).split("-"), trees) for c, t in zip(s, tr["talents"]) if c.isdigit() and int(c)}
        said = []
        for q in RANK_SAID.finditer(body):
            n, k = (q.group("n1"), q.group("k1")) if q.group("n1") else (q.group("n2"), q.group("k2"))
            k = WORDNUM.get(k.lower(), k)
            if n in ranks and k.isdigit() and int(k) != ranks[n]:
                said.append(f"{n} ({k} said, {ranks[n]} taken)")
        if said:
            out.append(("build", cls, f"{p}: the guide gives {', '.join(sorted(set(said)))}"))


FORMS = {"Bear Form", "Dire Bear Form", "Cat Form", "Moonkin Form", "Travel Form", "Aquatic Form", "Ghost Wolf", "Battle Stance", "Defensive Stance",
         "Berserker Stance", "Stealth", "Shadowform"}
EXPLAINED = ("gate", "filler", "tier point", "to reach", "for the tier")
# a tooltip that also does something general (a stat, every spell, all damage) is no dead talent for a page that skips its named spells
GENERIC = re.compile(r"\ball\b|\byour (?:spells|attacks|abilities|melee|ranged|healing|damage)|\b(?:Intellect|Stamina|Spirit|Strength|Agility|armor|Armor)\b|"
                     r"attack power|spell power|chance to (?:dodge|parry|hit|be hit)|movement speed|damage (?:you deal|done by you|taken)|maximum (?:health|mana)|"
                     r"\binstant(?: cast)? spells\b",   # Mental Agility: "your Smite, Holy Fire, and instant cast spells" (2026-11-09)
                     re.I)


def rank_text(t):
    r = (t.get("ranks") or [""])[-1]
    return r if isinstance(r, str) else (r.get("text") or r.get("description") or "")


# a tooltip naming a family of spells by its last word (Shock, Sting, Totem ...) is about every member: never read it as dead
FAMILY = re.compile(r"\b(?:Shocks?|Stings?|Totems?|Seals?|Blessings?|Curses?|Banes?|Aspects?|Shouts?|Traps?|Wards?|Poisons?|Shots?|Strikes?|Judgements?)\b")
IDLE_LINE = "**Points that do nothing for this spec:**"   # the note render_modes writes (2026-11-08); the check reads around it


def dead_talents(cls, text, body):
    """The lead build's talents (digits `body`) that do nothing on a page (`text`): [(talent, ranks, tree, spells or None)], spells None
    for a talent ability the page never uses, else the only spells or forms it improves, none of which the page uses. The tooltip's spell
    names are matched with every non-spell talent name cut out first ("Improved Wrath" is no mention of Wrath); a tooltip that also does
    something general (a stat, all spells) is never dead. The page's own note on such points is left out of the reading."""
    trees = talents(cls)
    book = set(LG.book(cls)) | FORMS
    tnames = sorted({t["name"] for tr in trees for t in tr["talents"]} - book, key=len, reverse=True)
    lead = text[:text.find("\n## Other builds")] if "\n## Other builds" in text else text
    lead = "\n".join(ln for ln in lead.splitlines() if IDLE_LINE not in ln and not ln.startswith("**Taken for raid utility:**"))
    # the talent tables list every talent the build takes (2026-11-09: raid pages got one, S16): a listing is no use of a spell
    lead = re.sub(r"\n## Talents(?: while leveling)?\n.*?(?=\n## |\Z)", "\n", lead, flags=re.S)
    cut = lead
    for n in tnames:
        cut = cut.replace(n, " ")
    prose = "\n".join(ln for ln in lead.splitlines() if "|" not in ln)
    found = []
    for s, tr in zip(body.split("-"), trees):
        for c, t in zip(s, tr["talents"]):
            if not (c.isdigit() and int(c)):
                continue
            if t["name"] in book:   # a talent that grants an ability: the page must use the ability
                if not re.search(rf"\b{re.escape(t['name'])}\b", prose):
                    found.append((t["name"], int(c), tr["name"], None))
                continue
            tip = rank_text(t)
            names = {n for n in book if re.search(rf"\b{re.escape(n)}\b", tip)}
            names -= {n for n in names if any(n != o and n in o for o in names)}   # "Bear Form" inside "Dire Bear Form"
            rest = tip
            for n in names:
                rest = rest.replace(n, " ")
            if FAMILY.search(rest):   # "your Shock and Lightning Shield spells": every shock counts (the shaman audit, 2026-11-08)
                continue
            if names and not GENERIC.search(rest) and not any(re.search(rf"\b{re.escape(n)}\b", cut) for n in names):
                found.append((t["name"], int(c), tr["name"], sorted(names)))
    return found


def classify_dead(cls, body, dead):
    """Why each dead talent is there: {talent: {"free": points removable at no loss of legality, "gate": points that open a deeper talent,
    "opens": the deeper talents}}. Points come off the dead talents one at a time, deepest row first, while the build stays legal (tier
    gating and prerequisites, validate_builds.check_state); the talent a failed removal would break is what the rest opens."""
    import validate_builds as VB
    trees = talents(cls)
    vb = VB.load_forever()[cls]
    state = {tr["name"]: {t["name"]: int(c) for c, t in zip(s, tr["talents"]) if c.isdigit() and int(c)}
             for s, tr in zip(body.split("-"), trees)}
    row = {t["name"]: t["row"] for tr in trees for t in tr["talents"]}
    out = {n: {"free": 0, "gate": r, "opens": set()} for n, r, _, _ in dead}
    tree_of = {n: tr for n, _, tr, _ in dead}
    for n in sorted(out, key=lambda x: -row.get(x, 0)):
        while state[tree_of[n]].get(n, 0) > 0:
            state[tree_of[n]][n] -= 1
            errors = []
            VB.check_state(vb, {t: {k: v for k, v in a.items() if v} for t, a in state.items()}, "x", errors)
            if errors:
                state[tree_of[n]][n] += 1
                for e in errors:
                    m = re.search(r": (.+?) \(tier \d+\) needs", e) or re.search(r": (.+?) requires ", e)
                    if m:
                        out[n]["opens"].add(m.group(1))
                break
            out[n]["free"] += 1
            out[n]["gate"] -= 1
    return out


def raid_utility(cls, name):
    """Why a raid build keeps a talent its rotation never uses, when the raid filler audit's utility tags give one (2026-11-09: the feral
    raid page called Feral Charge, the filler audit's interrupt, a point that does nothing): its interrupt, or its threat cut."""
    t = next((x for tr in talents(cls) for x in tr["talents"] if x["name"] == name), None)
    txt = rank_text(t) if t else ""
    if re.search(r"\binterrupt", txt, re.I):
        return "its interrupt"
    if re.search(r"threat generated by your", txt, re.I):
        return "its threat cut"
    return None


def check_dead(tree, cls, pages, out):
    """A talent of a spec page's lead build that only improves spells or forms the page never uses, or a talent ability it never uses
    (2026-11-08, user: "the resto druid talent spec says to take Improved Wrath. Why would that ever be a thing? ... Check things like that
    constantly"). Gate points (they open a deeper talent) pass when the page's "Points that do nothing" note names them; free points are
    always a finding: the build should spend them on something."""
    bs = builds(tree, cls)
    for p in pages:
        if not re.match(rf"{cls}/(leveling|raid)/[a-z0-9-]+\.md$", p) or p.endswith(("README.md", "keybinds.md", "-by-level.md")):
            continue
        text = tree.text(p)
        m = TF.search(text)
        if not m:
            continue
        lead = text[:text.find("\n## Other builds")] if "\n## Other builds" in text else text
        lead_id = next(iter(re.findall(r"builds/([a-z0-9-]+)\.md", lead)), None)
        if "/leveling/" in p and lead_id and any("raid_path_leveling" in n for n in (bs.get(lead_id) or {}).get("notes", [])):
            continue   # a healer's or tank's leveling page levels in its raid build (user decision 2026-09-30): its raid page is checked
        dead = dead_talents(cls, text, m.group(2))
        if not dead:
            continue
        why = classify_dead(cls, m.group(2), dead)
        noted = IDLE_LINE in lead
        for n, r, _, names in dead:
            w = why[n]
            what = "is a talent ability the page never uses" if names is None else f"improves only {', '.join(names)}, which the page never uses"
            if w["free"] and "/raid/" in p and raid_utility(cls, n) and f"**{n}** ({r}) is not in the rotation" in lead:
                continue   # the raid filler audit's utility, and the page says so (render_modes.idle_note)
            if w["free"]:
                out.append(("dead", cls, f"{p}: {n} ({r}) {what}; {w['free']} of its points could go elsewhere"))
            elif not noted:
                out.append(("dead", cls, f"{p}: {n} ({r}) {what}; it opens {', '.join(sorted(w['opens'])) or 'a deeper talent'}, and the page does not say so"))


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
        check_build(tree, cls, pages, out)
        check_dead(tree, cls, pages, out)
        check_names(tree, cls, pages, known, out)
    notes = live(out) if a.live else []
    order = ["patch", "talents", "links", "guide", "build", "dead", "keys", "steps", "macros", "coverage", "names"]
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
