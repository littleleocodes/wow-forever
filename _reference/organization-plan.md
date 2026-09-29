# Organization plan (proposal, 2026-09-29)

Hand-written proposal (user request: "a better organization of the files and folders, basic to understand, uniform, a new player can
follow them, fewer unneeded links"). **Step 1 is done; steps 2-6 wait for approval**, because every script finds its files through
`_reference/data/paths.py` and a half-finished move would break the pipeline.

## The problem

- About 1,000 files in the class folders, 605 Markdown pages in all. A class has ~65 pages; ~15 are builds a player would read, the rest
  is evidence (simulator reports, calibration records, optimizer reports, 326 candidate builds, the Classic baseline).
- Player advice and research evidence sit side by side: `raid/` holds the build pages next to `raidsim/`, `optimizer/`, `heallab/`.
- Names are the pipeline's: build ids (`opt-frost-raid-raid-dps`), spec model ids (`mm-lonewolf-raid`), optimizer build names that are
  damage breakdowns ("Raid dual-wield Fury: white ~50% (MH 35 / OH 15)...").
- Build pages open with how the build was adopted ("Allocation adopted on 2026-09-26 from `cand-bm-r2`...") before what it is.
- Every generated page links to the scripts that wrote it and to several sibling reports; a player has no use for either.

## Target layout

```
START-HERE.md                 player entry point: one line per class (done)
README.md                     short: what the project is, START-HERE for players, docs/ for how it works
docs/                         how the project works (from _reference/: overview, talent system, methodology, sources, glossary)
<class>/
  START-HERE.md               the player guide: leveling, raid, tank/heal, PvP, what to press, talent links (done, generated)
  builds/                     one page per build we recommend or keep as an alternative, all scenarios together,
                              file name = readable slug (frost-fingers-of-frost.md), player part first, evidence below a line
  research/                   everything else, unchanged inside: fightlab/, raidsim/, heallab/, optimizer/, classic-baseline/,
                              talent-trees.md, baseline-audit.md, spells.md, candidates/
reports/                      the cross-class generated pages now in _reference/ (simulator summaries, audits, surveys, checklists)
_reference/data/              scripts and datasets, unchanged (paths.py updated)
```

## Writing rules for every page

1. First line under the title: who the page is for and what it answers, in one sentence.
2. Player pages: no build ids, no script names, no spec model ids; talents by their game names; a talentsforever.com link for every build.
3. One table style: the thing, then its numbers, best first. Percentages with one decimal, DPS as whole numbers.
4. A build page opens with: what it is for, the talents (link), the order (leveling), what to press, then "Why these talents" and
   "Evidence" (the numbers and how they were measured). Adoption history moves to a changelog line at the bottom.
5. Links: a player page links to START-HERE, the build pages and the class README only; research pages keep their cross-links.
6. Dates absolute; the beta client build named once per page.

## Steps

1. **Done (2026-09-29):** `render_start_here.py` writes `START-HERE.md` and `<class>/START-HERE.md` from the same data as every other
   page (in rebuild.py's regen step), readable build names (`display_name`), talentsforever.com links.
2. **Display names in the build JSON:** a `display_name` field per build (set by hand for hand drafts, generated for optimizer builds
   from the lead tree and role, e.g. "Fury dual wield (optimizer)"); ids stay as they are, since scripts, candidates and reports key on them.
3. **Build pages: player part first** (render_builds.py): the order in the writing rules; the long "core/flex/notes" lists stay, below.
4. **Move the evidence into `<class>/research/`** and merge `leveling/builds`, `raid/builds`, `pvp/builds` into `<class>/builds/`:
   one change to `paths.py` (the only place that knows the layout), `git mv` of the folders, a regen, the link check. The scenario READMEs
   (`leveling/README.md`, `raid/README.md`, `pvp/README.md`) become sections of the research index.
5. **`_reference/` split** into `docs/` (hand-written explanations) and `reports/` (generated cross-class pages); `_reference/data/`
   stays where it is (every script path depends on it).
6. **Trim:** keep only the latest candidate files per spec (the rest are in git history), drop the "parse" builds from player pages,
   fold `_reference/notes/` (the local sessions' own notes) into HANDOFF or delete them.

## Questions for you before steps 2-6

- Merge `leveling/`, `raid/` and `pvp/` build pages into one `builds/` folder per class, or keep the scenario folders for builds?
- Delete old candidate builds (326 files; git keeps them) or keep them in `research/candidates/`?
- `forever_ideas.txt` in the root is your own notes file: leave it, or move it to `docs/ideas.md`?
- Should the Legacy perks (account-wide; Talented gives talent points from level 5) get a leveling variant? Only after you have earned
  them, so the default guides assume none.
