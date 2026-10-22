"""Render builds.json / proposed-builds.json into markdown build docs.

Usage (from the project root):
    python _reference/data/render_builds.py            # all classes
    python _reference/data/render_builds.py warrior    # one class

Writes, per class (layout in paths.py):
    <class>/research/talents/classic-baseline/<build-id>.md   (+ README.md index)
    <class>/<scenario>/builds/<build-id>.md          Forever builds by scenario (leveling, raid, pvp), plus the title and the
                                                     "Builds" section of <class>/<scenario>/README.md and the "Where to find
                                                     things" section of <class>/README.md

Run validate_builds.py first; this script does not re-check the point math.
"""
import json
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from validate_builds import (CLASSES, ROOT, load_classic, load_forever, find_talent,  # noqa: E402
                             split_string, forever_status)
import paths  # noqa: E402
import readme_sections as rs  # noqa: E402
from data_build import BUILD as DATA_BUILD, CAPTURED as DATA_CAPTURED  # noqa: E402

TIER_LABEL = {"primary": "Primary", "alternative": "Alternative", "situational": "Situational", "draft": "Draft"}
CONTENT_LABEL = {"raid": "Raid", "dungeon": "Dungeon", "pvp": "PvP", "leveling": "Leveling", "solo": "Solo/farming"}


def esc(s) -> str:
    return str(s).replace("|", "\\|").replace("\n", " ").strip() if s else ""


def rank_text(tree: dict, name: str, pts: int) -> str:
    key, t = find_talent(tree, name)
    if t is None or pts <= 0:
        return ""
    ranks = t.get("ranks", [])
    if len(ranks) >= pts and ranks[pts - 1]:
        text = esc(ranks[pts - 1])
        if (pts - 1) in t.get("estimated", []):
            text += " *(est. — extrapolated from rank 1)*"
        return text
    if ranks and ranks[0]:
        return esc(ranks[0]) + f" *(rank 1 shown; rank {pts} text not captured)*"
    return ""


def render_build(cls: str, game: str, build: dict, trees: dict, forever_trees: dict) -> str:
    split = split_string(trees, build)
    tree_names = sorted(trees, key=lambda t: trees[t].get("order", 0)) if game == "classic-era" else list(trees)
    o = []
    label = "Classic baseline" if game == "classic-era" else "WoW: Forever — proposed"
    o.append(f"# {build['name']} — {split}\n")
    if game == "forever":
        page = paths.build_page(game, cls, build)
        sc = paths.scenario_of(build)
        o.append(f"*[{cls.title()}]({paths.rel(page, ROOT / cls / 'README.md')}) · [{paths.SCENARIO_TITLE[sc]}]({paths.rel(page, paths.scenario_readme(cls, sc))}) · {label}*\n")
    else:
        o.append(f"*{cls.title()} · {label}*\n")
    o.append("| | |")
    o.append("|---|---|")
    o.append(f"| **Build** | {split} ({' / '.join(tree_names)}) |")
    o.append(f"| **Role** | {build.get('role', '').upper()} — {CONTENT_LABEL.get(build.get('content', ''), build.get('content', ''))} |")
    o.append(f"| **Status** | {TIER_LABEL.get(build.get('tier', ''), build.get('tier', ''))} |")
    if game == "classic-era":
        o.append("| **Data** | Classic Era 1.12-era trees (validated against `_reference/data/classic-era-talents.json`) |")
        o.append("| **Forever** | This is the *baseline*; see the Forever status table below and `../forever/` for the adapted build |")
    else:
        o.append(f"| **Data** | WoW: Forever beta client build {DATA_BUILD} ({DATA_CAPTURED} snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |")
        if build.get("based_on"):
            o.append(f"| **Based on** | Classic baseline `{build['based_on']}` |")
    o.append("")
    o.append("## Summary\n")
    o.append(build.get("summary", "") + "\n")

    o.append("## Point allocation\n")
    for tname in tree_names:
        items = build["allocation"].get(tname, [])
        pts = sum(p for _, p in items)
        o.append(f"### {tname} ({pts})\n")
        if not items:
            o.append("*No points.*\n")
            continue
        if game == "forever":
            o.append("| Talent | Pts | vs Classic | Effect at this rank |")
            o.append("|---|---|---|---|")
        else:
            o.append("| Talent | Pts | Effect at this rank |")
            o.append("|---|---|---|")
        tree = trees[tname]
        for name, p in items:
            key, t = find_talent(tree, name)
            mx = t["max"] if t else "?"
            eff = rank_text(tree, name, p)
            if game == "forever":
                st = t.get("status", "?") if t else "?"
                st = {"same": "unchanged", "new": "**NEW**"}.get(st, st)
                o.append(f"| **{esc(name)}** | {p}/{mx} | {st} | {eff} |")
            else:
                o.append(f"| **{esc(name)}** | {p}/{mx} | {eff} |")
        o.append("")

    if build.get("order"):
        o.append("## Leveling order\n")
        o.append("| Levels | Tree | Talent | Pts | Running total |")
        o.append("|---|---|---|---|---|")
        running = {}
        for step in build["order"]:
            running[step["tree"]] = running.get(step["tree"], 0) + step["points"]
            tot = "/".join(str(running.get(t, 0)) for t in tree_names)
            o.append(f"| {step['levels']} | {step['tree']} | {esc(step['talent'])} | {step['points']} | {tot} |")
        o.append("")

    if build.get("core"):
        o.append("## Core talents (priority order)\n")
        for i, c in enumerate(build["core"], 1):
            o.append(f"{i}. **{esc(c['talent'])}** — {c.get('why', '')}")
        o.append("")

    if build.get("flex"):
        o.append("## Flex points\n")
        o.append("| Pts | Default | Alternatives | Why |")
        o.append("|---|---|---|---|")
        for f in build["flex"]:
            o.append(f"| {f['points']} | {esc(f['default'])} | {esc(', '.join(f.get('alternatives', [])))} | {esc(f.get('why', ''))} |")
        o.append("")

    if game == "forever":
        import render_rotations
        sec = render_rotations.build_sections(cls, build)
        if sec:
            o.append(sec)
    if build.get("notes"):
        o.append("## Notes\n")
        for n in build["notes"]:
            o.append(f"- {n}")
        o.append("")

    if build.get("open_questions"):
        o.append("## Open questions (verify in the live game)\n")
        for n in build["open_questions"]:
            o.append(f"- {n}")
        o.append("")

    if game == "classic-era":
        o.append("## Forever status of every point in this build\n")
        o.append("Talent-by-talent check against the Forever beta-client trees (`../forever/talent-trees.md`).\n")
        o.append("| Tree | Talent | Pts | In Forever | Detail |")
        o.append("|---|---|---|---|---|")
        orphan = 0
        for tname, items in build["allocation"].items():
            for name, p in items:
                st, detail = forever_status(forever_trees, tname, name)
                if st == "removed":
                    orphan += p
                    st = "**REMOVED**"
                elif st == "same":
                    st = "unchanged"
                o.append(f"| {tname} | {esc(name)} | {p} | {st} | {esc(detail)} |")
        o.append("")
        o.append(f"**{orphan} point(s) of this build no longer exist in Forever** and must be re-spent; "
                 "see `../forever/README.md` for how they were re-spent.\n")

    if build.get("sources"):
        o.append("## Sources\n")
        for s in build["sources"]:
            o.append(f"- <{s}>")
        o.append("")
    o.append("---")
    o.append("*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*")
    return "\n".join(o) + "\n"


def render_index(cls: str, game: str, data: dict, trees: dict) -> str:
    o = []
    if game == "classic-era":
        o.append(f"# {data['class']} — Classic baseline talent builds\n")
        o.append("The community-standard WoW Classic Era builds, used as the *starting point* for WoW: Forever. "
                 "Every allocation below is machine-validated against the Classic tree data (51 points, tier gating, "
                 "prerequisites, rank caps). Each build page ends with a talent-by-talent check of what survived into "
                 "the Forever trees.\n")
    else:
        o.append(f"# {data['class']} — WoW: Forever proposed builds\n")
        o.append("Draft builds for WoW: Forever, derived from the Classic baseline and re-spent onto the Forever beta-client "
                 "trees (build " + DATA_BUILD + "). Validated against the beta tree data for point math, **not** for performance — nothing has "
                 "been simulated or play-tested yet. Treat every one as a hypothesis to confirm at launch.\n")
    o.append("| Build | Split | Role | Content | Status | File |")
    o.append("|---|---|---|---|---|---|")
    for b in data["builds"]:
        split = split_string(trees, b)
        o.append(f"| {esc(b['name'])} | {split} | {b.get('role', '').upper()} | "
                 f"{CONTENT_LABEL.get(b.get('content', ''), b.get('content', ''))} | "
                 f"{TIER_LABEL.get(b.get('tier', ''), b.get('tier', ''))} | [{b['id']}.md]({b['id']}.md) |")
    o.append("")
    if data.get("notes"):
        o.append(data["notes"] + "\n")
    o.append("Source of truth: `builds.json` in this folder. Regenerate with "
             "`python _reference/data/validate_builds.py && python _reference/data/render_builds.py`.")
    return "\n".join(o) + "\n"


SCENARIO_INTRO = {
    "leveling": ("Leveling and solo farming builds with their leveling orders, the leveling guide and rotation the fight lab plays, "
                 "and the respec plan. Numbers come from the fight lab (a Monte Carlo fight simulator of stated assumptions) and the "
                 "stats model; every build is a hypothesis for the beta client " + DATA_BUILD + "."),
    "raid": ("Raid DPS, tank and healer builds. DPS builds are ranked on a boss-level training dummy with only your own buffs in the "
             "community's raid simulator (each report names its simulator and commit: the ElliotWood/Forever fork, deleted 2026-10-18, for runs before the port to the official wowsims/forever); the raid setting and the parse build are shown next to it. Tanks are measured "
             "in the raid setting and healers in the healer lab. Simulations of the community's model of the beta, not measurements."),
    "pvp": ("PvP talent builds. There is no rotation page: PvP play depends on the fight. PvP values in the stats model are assumptions "
            "tuned on the Classic community PvP builds; no simulator plays PvP."),
}


def opt_profile(bid):
    for p in sorted(paths.PROFILE_SCENARIO, key=len, reverse=True):
        if bid.endswith("-" + p):
            return p
    return ""


def is_hand(b):
    """A hand draft: not an optimizer export, not a derived build (a search's winner, 🔬) and not a generated one (⚗) (2026-10-09: the
    hand-drafts lists had counted the searches' builds as hand drafts)."""
    return not b["id"].startswith("opt-") and not b.get("derived") and not b.get("generated")


def scenario_builds_section(cls, sc, data, trees, classic_data):
    readme = paths.scenario_readme(cls, sc)
    hand = [b for b in data["builds"] if paths.scenario_of(b) == sc and is_hand(b)]
    found = [b for b in data["builds"] if paths.scenario_of(b) == sc and not is_hand(b) and not b["id"].startswith("opt-")]
    opt = [b for b in data["builds"] if paths.scenario_of(b) == sc and b["id"].startswith("opt-")]
    o = ["## Builds", ""]
    if hand:
        o += ["Hand drafts (the recommendations; each is a hypothesis to check at launch):", "",
              "| Build | Split | Role | Classic baseline |", "|---|---|---|---|"]
        for b in hand:
            page = paths.build_page("forever", cls, b)
            base = b.get("based_on")
            bpage = paths.build_page_by_id("classic-era", cls, base) if base else None
            base_cell = f"[{base}]({paths.rel(readme, bpage)})" if bpage else (base or "—")
            o.append(f"| [{esc(b['name'])}]({paths.rel(readme, page)}) | {split_string(trees, b)} | {b.get('role', '').upper()} | {base_cell} |")
        o.append("")
    if found:
        o += ["Derived and generated builds (🔬 found by this project's searches in the simulators, ⚗ generated where no hand draft "
              "exists; the pages pick between them and the hand drafts on the numbers):", "", "| Build | Split | Role |", "|---|---|---|"]
        for b in found:
            page = paths.build_page("forever", cls, b)
            o.append(f"| [{esc(b['name'])}]({paths.rel(readme, page)}) {'🔬' if b.get('derived') else '⚗'} | {split_string(trees, b)} | "
                     f"{b.get('role', '').upper()} |")
        o.append("")
    if opt:
        o += ["Optimizer builds (the stats model's optimum per use-case, see the Optimizer section):", "",
              "| Build | Split | Profile |", "|---|---|---|"]
        for b in opt:
            o.append(f"| [{b['id']}]({paths.rel(readme, paths.build_page('forever', cls, b))}) | {split_string(trees, b)} | {opt_profile(b['id']) or '—'} |")
        o.append("")
    if classic_data:
        cl = [b for b in classic_data["builds"] if paths.scenario_of(b) == sc]
        if cl:
            o.append("Classic Era reference builds: " + ", ".join(f"[{b['id']}]({paths.rel(readme, paths.build_page('classic-era', cls, b))})" for b in cl) + ".")
            o.append("")
    if not hand and not opt:
        o += ["No Forever builds for this scenario yet.", ""]
    return "\n".join(o)


def class_index_section(cls, data, classic_data):
    readme = ROOT / cls / "README.md"
    counts = {sc: [b for b in data["builds"] if paths.scenario_of(b) == sc] for sc in paths.SCENARIOS}
    what = {"leveling": "leveling and solo builds, the leveling guide, rotation and respec plan, fight-lab reports",
            "raid": "raid DPS, tank and healer builds, training-dummy and raid-sim rankings, rotation, gear, consumables",
            "pvp": "PvP builds (no rotation: PvP play depends on the fight)"}
    o = ["## Research files", "",
         "The research behind the pages above: every build, report and simulation.", "",
         "| Folder | What is in it | Hand drafts |", "|---|---|---|"]
    for sc in paths.SCENARIOS:
        hand = [b for b in counts[sc] if is_hand(b)]
        cell = ", ".join(f"[{b['id']}]({paths.rel(readme, paths.build_page('forever', cls, b))})" for b in hand) or "—"
        n = len(counts[sc])
        o.append(f"| [research/{sc}/]({paths.rel(readme, paths.scenario_readme(cls, sc))}) | {what[sc][:1].upper() + what[sc][1:]} ({n} build{'s' if n != 1 else ''}) | {cell} |")
    o.append(f"| [research/spells/]({paths.rel(readme, ROOT / cls / paths.RESEARCH / 'spells' / 'README.md')}) | Spell ranks and numbers from the beta client | |")
    o.append(f"| [research/talents/forever/]({paths.rel(readme, paths.talents_dir('forever', cls) / 'talent-trees.md')}) | Talent trees, the baseline audit, "
             f"[adaptation notes]({paths.rel(readme, paths.talents_dir('forever', cls) / 'README.md')}) and `proposed-builds.json` (the source of truth for every build above) | |")
    if classic_data:
        o.append(f"| [research/talents/classic-baseline/]({paths.rel(readme, paths.talents_dir('classic-era', cls) / 'README.md')}) | Classic Era community builds used as the baseline | |")
    o += ["", "Generated by `_reference/data/render_builds.py` from the build JSON; the sections above it are hand-written."]
    return "\n".join(o)


def classes_section(forever, classic):
    """The "Classes" table of the top-level README.md: build counts and links to each class's scenario folders."""
    o = ["## Classes", "",
         f"| Class | Classic baseline builds | Forever tree (beta client {DATA_BUILD}) | Forever builds | Scenario folders |", "|---|---|---|---|---|"]
    for cls in sorted(CLASSES):
        fp, cp = paths.builds_json("forever", cls), paths.builds_json("classic-era", cls)
        fb = json.load(open(fp, encoding="utf-8"))["builds"] if fp.exists() else []
        cb = json.load(open(cp, encoding="utf-8"))["builds"] if cp.exists() else []
        n_tal = sum(len(t.get("talents", {})) for t in forever.get(cls, {}).values()) if cls in forever else 0
        hand = sum(1 for b in fb if is_hand(b))
        opt = sum(1 for b in fb if b["id"].startswith("opt-"))
        found = len(fb) - hand - opt
        doc = ROOT / "_reference" / "README.md"
        links = " · ".join(f"[{sc}]({paths.rel(doc, paths.scenario_readme(cls, sc))})" for sc in paths.SCENARIOS)
        o.append(f"| [{cls.title()}]({paths.rel(doc, ROOT / cls / 'README.md')}) | {len(cb)} | {n_tal} talents | {hand} hand drafts + {found} derived + {opt} optimizer builds | {links} |")
    o += ["", "Generated by `_reference/data/render_builds.py`."]
    return "\n".join(o)


def main(argv):
    classes = [c for c in CLASSES if not argv or c in argv]
    classic = load_classic()
    forever = load_forever()
    for cls in classes:
        classic_data = None
        cpath = paths.builds_json("classic-era", cls)
        if cpath.exists():
            classic_data = json.load(open(cpath, encoding="utf-8"))
            trees = classic[cls]
            for old in cpath.parent.glob("*.md"):
                if old.read_text(encoding="utf-8").rstrip().endswith("edit the JSON, not this file.*"):
                    old.unlink()
            for b in classic_data["builds"]:
                (cpath.parent / f"{b['id']}.md").write_text(render_build(cls, "classic-era", b, trees, forever[cls]), encoding="utf-8")
            (cpath.parent / "README.md").write_text(render_index(cls, "classic-era", classic_data, trees), encoding="utf-8")
            print(f"{cls}/classic-baseline: {len(classic_data['builds'])} build pages + README.md")
        fpath = paths.builds_json("forever", cls)
        if not fpath.exists():
            continue
        data = json.load(open(fpath, encoding="utf-8"))
        trees = forever[cls]
        # remove stale generated pages: the old flat talents/forever/ layout and every scenario's builds/ folder
        stale = list(fpath.parent.glob("*.md")) + [p for sc in paths.SCENARIOS for p in (paths.scenario_dir(cls, sc) / "builds").glob("*.md")]
        for old in stale:
            if old.read_text(encoding="utf-8").rstrip().endswith("edit the JSON, not this file.*"):
                old.unlink()
        old_index = fpath.parent / "builds-README.md"
        if old_index.exists():
            old_index.unlink()
        for b in data["builds"]:
            out = paths.build_page("forever", cls, b)
            out.parent.mkdir(parents=True, exist_ok=True)
            out.write_text(render_build(cls, "forever", b, trees, forever[cls]), encoding="utf-8")
        for sc in paths.SCENARIOS:
            readme = paths.scenario_readme(cls, sc)
            title = f"# {cls.title()} — " + ("leveling and solo play" if sc == "leveling" else "raids" if sc == "raid" else "PvP")
            rs.set_head(readme, f"{title}\n\n[{cls.title()}]({paths.rel(readme, ROOT / cls / 'README.md')}) · this page is generated by "
                                f"`_reference/data/` (do not hand-edit; the reasoning lives in the build notes).\n\n{SCENARIO_INTRO[sc]}")
            rs.splice_ordered(readme, sc, "## Builds", scenario_builds_section(cls, sc, data, trees, classic_data))
        rs.drop(ROOT / cls / "README.md", "## Where to find things")   # renamed "## Research files" (2026-09-29)
        rs.splice_ordered(ROOT / cls / "README.md", "class", "## Research files", class_index_section(cls, data, classic_data))
        print(f"{cls}: {len(data['builds'])} Forever build pages in " + ", ".join(f"{sc}/builds" for sc in paths.SCENARIOS) + " + scenario READMEs")
    if not argv:
        rs.splice(ROOT / "_reference" / "README.md", "## Classes", classes_section(forever, classic), before=["## Tooling"])


if __name__ == "__main__":
    main(sys.argv[1:])
