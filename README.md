# WoW: Forever — Gameplay Optimization

Working notes and validated data for optimizing every class in **World of Warcraft: Forever**
(Blizzard's Classic+ release, launching **November 4, 2026**). The project is organized **by class**, and
each class folder by scenario: `leveling/`, `raid/` (training dummy, raid, parse) and `pvp/`.

## Working assumption

WoW: Forever uses the Classic talent system (9 classes, 3 trees each, **51 points**, 7 tiers, gold-medal
talents at 11/21/31 points plus a **new 1-point talent at the 16-point mark**), but the trees themselves
are **revamped**: ~145 new talents, ~108 Classic talents removed, and many reworded. So:

1. **Classic Era optimal builds are the baseline** — they encode which talents matter for each spec.
2. **The Forever trees are read from the beta client** (build 1.60.1.70009 of 2026-09-24: 467 talents with tiers,
   every rank's tooltip, prerequisites and a diff against Classic; the BlizzCon demo snapshot is archived).
3. **Each Classic build is audited** talent-by-talent against the Forever tree, and re-spent into a
   **proposed Forever build** that is validated for point math but *not yet* for performance.
4. Everything Forever-specific is a hypothesis until it is checked in the live game.

## Folder layout

```
wow-forever/
├── README.md                ← this file
├── CLAUDE.md                ← conventions for working in this repo
├── _reference/              ← cross-class facts, data and tooling (underscore = not a class)
│   ├── wow-forever-overview.md   what we know about Forever (release, races, raids, systems)
│   ├── talent-system.md          how talents work (Classic rules + Forever differences)
│   ├── methodology.md            how Classic baselines become Forever builds
│   ├── sources.md                every external source used
│   ├── launch-checklist.md       everything talents still need from the live game (generated)
│   ├── beta-checklist.md         what the beta (cap 20, later 30) can verify (generated)
│   ├── beta-refresh-2026-09-25.md  analysis of the first beta data refresh: what changed, what the model now says
│   ├── fightlab-summary.md       every class's fight-lab results on one page: kill times, deaths, top talents (generated)
│   ├── raidsim-summary.md        every class's raid builds through the community simulator, one page (generated)
│   ├── heallab-summary.md        every healer's raid-heal builds through the healer lab, one page (generated)
│   ├── scenario-audit.md         every build scored in its own scenario: talents worth nothing there (generated)
│   ├── pvp-check.md              the PvP profile against the Classic community and Forever PvP builds (generated)
│   ├── raid-buff-values.md       what each raid buff a talent provides is worth to the specs that receive it (generated)
│   └── data/                     datasets + scripts (see "Tooling"); `paths.py` says where every class file lives
├── _templates/              ← templates for new class docs / builds
└── <class>/                 ← druid, hunter, mage, paladin, priest, rogue, shaman, warlock, warrior
    ├── README.md                 class overview, roles, Forever headline changes (hand-written) + "Where to find things" (generated)
    ├── leveling/                 leveling and solo play
    │   ├── README.md                 builds, guide / rotation / respec links, fight lab, optimizer (generated)
    │   ├── guide.md                  the recommended build level by level, each bracket, the talents that carry it (generated)
    │   ├── rotation.md               the fight lab's priority and what each leveling build casts, level by level (generated)
    │   ├── respec-plan.md            when a respec while leveling pays for itself (generated)
    │   ├── builds/<build-id>.md      leveling and solo builds (generated from proposed-builds.json)
    │   ├── fightlab/                 fight-lab reports, calibration, candidates (generated)
    │   └── optimizer/                stats-model reports for leveling-st, leveling-aoe, solo-60 (generated)
    ├── raid/                     raids: training dummy, raid setting and parse
    │   ├── README.md                 builds, DPS ranking (ours vs the simulator's), raid sim, healer lab, optimizer (generated)
    │   ├── rotation.md               what each raid build casts: ours and the simulator's own (generated)
    │   ├── gear.md  consumables.md   the community simulator's presets (generated)
    │   ├── builds/<build-id>.md      raid DPS, tank and healer builds (generated)
    │   ├── raidsim/                  simulator reports, environments, calibration, candidates (generated)
    │   ├── heallab/                  healer-lab reports (healers, generated)
    │   └── optimizer/                stats-model reports for raid-dps, parse, raid-tank, raid-heal (generated)
    ├── pvp/                      PvP talent builds; no rotation page (PvP play depends on the fight)
    │   ├── README.md                 builds and the PvP check (generated)
    │   └── builds/<build-id>.md
    ├── spells/README.md          beta-client spellbook: every trainer spell and rank with numbers (generated)
    └── talents/
        ├── forever/              proposed-builds.json (source of truth for every Forever build), talent-trees.md and
        │                         baseline-audit.md (generated), README.md (adaptation notes: what broke, what's new, decisions)
        └── classic-baseline/     builds.json (source of truth) + one page per Classic Era community build, optimizer/ and raidsim/ (generated)
```

Every page under `leveling/`, `raid/` and `pvp/` is generated: edit `proposed-builds.json`, the effect files or the scripts, then
regenerate (`python _reference/data/rebuild.py --steps regen`). A build's scenario comes from its `content` field: leveling and solo
go to `leveling/`, raid and dungeon to `raid/`, pvp to `pvp/`. Planned per-class addition: `professions/`.

## Classes

| Class | Classic baseline builds | Forever tree (beta client 1.60.1.70009) | Forever builds | Scenario folders |
|---|---|---|---|---|
| [Druid](druid/README.md) | 7 | 51 talents | 7 hand drafts + 9 optimizer builds | [leveling](druid/leveling/README.md) · [raid](druid/raid/README.md) · [pvp](druid/pvp/README.md) |
| [Hunter](hunter/README.md) | 5 | 50 talents | 10 hand drafts + 11 optimizer builds | [leveling](hunter/leveling/README.md) · [raid](hunter/raid/README.md) · [pvp](hunter/pvp/README.md) |
| [Mage](mage/README.md) | 7 | 54 talents | 8 hand drafts + 8 optimizer builds | [leveling](mage/leveling/README.md) · [raid](mage/raid/README.md) · [pvp](mage/pvp/README.md) |
| [Paladin](paladin/README.md) | 5 | 50 talents | 6 hand drafts + 7 optimizer builds | [leveling](paladin/leveling/README.md) · [raid](paladin/raid/README.md) · [pvp](paladin/pvp/README.md) |
| [Priest](priest/README.md) | 4 | 53 talents | 5 hand drafts + 6 optimizer builds | [leveling](priest/leveling/README.md) · [raid](priest/raid/README.md) · [pvp](priest/pvp/README.md) |
| [Rogue](rogue/README.md) | 5 | 53 talents | 8 hand drafts + 8 optimizer builds | [leveling](rogue/leveling/README.md) · [raid](rogue/raid/README.md) · [pvp](rogue/pvp/README.md) |
| [Shaman](shaman/README.md) | 5 | 50 talents | 5 hand drafts + 9 optimizer builds | [leveling](shaman/leveling/README.md) · [raid](shaman/raid/README.md) · [pvp](shaman/pvp/README.md) |
| [Warlock](warlock/README.md) | 4 | 52 talents | 7 hand drafts + 9 optimizer builds | [leveling](warlock/leveling/README.md) · [raid](warlock/raid/README.md) · [pvp](warlock/pvp/README.md) |
| [Warrior](warrior/README.md) | 5 | 53 talents | 5 hand drafts + 9 optimizer builds | [leveling](warrior/leveling/README.md) · [raid](warrior/raid/README.md) · [pvp](warrior/pvp/README.md) |

Generated by `_reference/data/render_builds.py`.

## Tooling (`_reference/data/`)

All build docs are **generated from JSON** so the numbers can never drift from the text.

```
python _reference/data/validate_builds.py             # check every build: 51 pts, tiers, prereqs, ranks, leveling order
python _reference/data/render_builds.py               # regenerate build pages + indexes from the JSON
python _reference/data/render_trees.py                # regenerate <class>/talents/forever/talent-trees.md
python _reference/data/show_tree.py warrior           # print a class's Forever tree compactly in the terminal
python _reference/data/refresh_forever_talents.py --fetch --raw 2026-10-01-beta-NNNNN   # pull a new beta build and merge it (then re-run the three above)
python _reference/data/build_forever_spells.py --raw 2026-10-01-beta-NNNNN                 # rebuild the spellbook data + <class>/spells/README.md
python _reference/data/build_launch_checklist.py      # regenerate _reference/launch-checklist.md from the builds' open questions
python _reference/data/build_beta_checklist.py        # regenerate _reference/beta-checklist.md: what a level-30 beta character can verify
python _reference/data/scorer/run.py hunter --spec bm-leveling --profile leveling-st --write --export   # stats model: score, optimize, order (see scorer/README.md)
python _reference/data/scorer/respec.py mage --write                                                    # when to respec while leveling -> <class>/leveling/respec-plan.md
python _reference/data/scorer/compare_effects.py                                                         # Classic -> Forever buff/nerf report -> scorer/changes/
python _reference/data/render_optimizer_sections.py                                                      # refresh the "Optimizer" section of every scenario README (leveling/, raid/)
python _reference/data/fightlab/run.py mage --spec frost-leveling --build opt-frost-leveling-leveling-st --compare leveling-frost --deltas 30,60 --write   # Monte Carlo fight simulator (see fightlab/README.md)
python _reference/data/rebuild.py --jobs 4                                                                # the whole leveling pipeline: calibrate <-> optimize, race, report, sensitivity, regenerate every page
python _reference/data/fightlab/summary.py --write                                                        # _reference/fightlab-summary.md (every class at a glance)
python _reference/data/raidsim/setup.py && python _reference/data/raidsim/run.py --all --write   # level-60 raid builds through the community simulator (see raidsim/README.md)
```
All scripts accept optional class names (`... warrior druid`) and run from any directory.

| File | What it is |
|---|---|
| `classic-era-talents.json` | Classic Era trees: 432 talents, tiers, ranks, prerequisites, per-rank tooltips (Wowhead Classic data via the `wow-forever-talent-calc` project) |
| `forever-talents/<class>.json` | Forever beta-client trees (build 1.60.1.70009, merged 2026-09-25): 467 talents with status vs. Classic (`new` / `changed` / `moved` / `same`), every rank's tooltip, prerequisites, removed-talent lists, `ranks_prev` where a beta build changed the text; provenance in `forever-talents/README.md` |
| `forever-spells/<class>.json` | Beta-client spellbooks (build 1.60.1.70009): every trainer spell and rank with learn level, cost, cast, cooldown, level-60 tooltip, coefficient and the Classic text where it differs; rendered to `<class>/spells/README.md` |
| `raw/<pull>/` | The datamines each refresh was merged from (warcraftforever.games, talentsforever.com, thewowdb.com) plus the archived demo snapshot |
| `refresh_forever_talents.py` | Merges the three beta datamines into `forever-talents/` (`--fetch` downloads a new pull); `extract_forever_talents.py` is the warcraftforever.games payload reader it uses |
| `build_forever_spells.py` | Builds `forever-spells/` from the talentsforever.com export and renders `<class>/spells/README.md` |
| `show_tree.py` | Compact terminal view of a class's Forever tree (tiers, ranks, prerequisites, status, rank-1 text) |
| `validate_builds.py` | Build validator + Classic-vs-Forever audit generator |
| `render_builds.py`, `render_trees.py`, `fmt_json.py` | Doc generators and JSON formatter |
| `build_launch_checklist.py` | Collects every build's `open_questions` into `_reference/launch-checklist.md` |
| `build_beta_checklist.py` | Per class, what the level-30 beta can verify: extrapolated talent ranks, estimated mechanics, demo spell numbers, the 10-30 leveling order, assumed unlock levels — `_reference/beta-checklist.md` |
| `scorer/` | **Stats model**: tooltip → numeric effects, spec/profile models (DPS, healer, tank), build optimizer, level-order planner, respec planner, Classic→Forever buff/nerf report. All nine classes encoded and calibrated against Classic. See `scorer/README.md` |
| `render_optimizer_sections.py` | Writes the "Optimizer (stats model)" section of each class's `leveling/README.md` and `raid/README.md` from the `opt-*` builds |
| `fightlab/` | **Monte Carlo fight simulator** for leveling/solo play: same-level mobs, rolled hits/crits/procs/pushback, downtime and deaths; measures time per kill, damage shares and talent values to check the scorer's leveling profiles. Mage (Frost) so far; reports in `<class>/leveling/fightlab/`. See `fightlab/README.md` |
| `rebuild.py` | One command for the leveling pipeline: (new beta build →) effects → calibrate ↔ optimize to convergence → race → report → sensitivity → regenerate pages (`fightlab/last-rebuild.json` records the outcome) |
| `render_fightlab_sections.py` | Writes the "Fight lab" section of each class's `leveling/README.md` and the hand draft's fight-lab note from the reports |
| `heallab/` | **Healer lab**: a Monte Carlo model of one raid healer keeping a five-member group alive for five minutes (beta spellbook heals, tooltip talent numbers, hand-coded mechanics); `run.py` measures a build's healing capacity and talent values, `calibrate.py` fits the healer models, `rebuild.py --steps heal` runs the loop; see `heallab/README.md` |
| `raidsim/run.py --env environments` | DPS of the same builds on a training dummy, in the raid and at the theoretical maximum (best gear preset, everything on), plus the scorer's `parse` profile build (personal DPS only) next to the raid build; per class README and in `_reference/raidsim-summary.md` |
| `raidsim/buff_value.py` | Measures what each raid buff or debuff a talent provides (Trueshot Aura, Leader of the Pack, Moonkin Aura, Sanctity Aura, Winter's Chill, Improved Shadow Bolt, Improved Scorch, Improved Battle Shout) is worth to the specs that receive it, in the simulators; writes `_reference/raid-buff-values.md` and the provider talents' raid `utility` (`--write`) |
| `check_beta_build.py` | Asks the datamines whether a newer beta client than ours exists and prints the `rebuild.py --refresh` command when it does |
| `scorer/classic_check.py` | Re-runs every Classic-era calibration case and reports which optimized builds moved (`rebuild.py --steps classic` first measures the Classic damage split and talent values in the upstream wowsims/classic simulator: `raidsim/setup.py --game classic`, `classic_specs.py`, `run.py`/`calibrate.py --game classic-era`) |
| `render_leveling_guides.py` | Writes `<class>/leveling/guide.md` from the fight-lab report, the hand draft's order and the respec plan |
| `render_sim_presets.py` | Writes `<class>/gear/`, `consumables/` and `rotation/` README pages from the community simulator's presets and APL files |
| `raidsim/` | **Raid sim**: our level-60 raid builds through the ElliotWood/Forever (wowsims) simulator with its own gear, rotation and buff presets; `setup.py` fetches and builds the toolchain, `run.py` races the builds, `render_raidsim_sections.py` writes the README sections and `_reference/raidsim-summary.md` |

## Stats model (scorer)

Hand-drafted builds are the *starting* answer; the **scorer** (`_reference/data/scorer/`) is the intended way to
decide talents: it parses every tooltip into numbers, values hand-entered procs with their arithmetic written down,
scores each talent for a spec model and use-case (leveling single-target, AoE grinding, solo at 60, raid DPS, raid
healing, raid tanking), finds the best legal 51-point build and orders it level by level. It reproduces the
known-optimal Classic builds (calibration table in `scorer/README.md`); its Forever results are exported as `opt-*`
builds next to the hand drafts, summarised in the "Optimizer" section of each scenario README (`leveling/`, `raid/`). Two companion reports:
`scorer/changes/<class>.md` lists every talent's Classic→Forever buff/nerf verdict and which Classic core talents
each Forever build drops (some specs — Warlock's DS/Ruin, Rogue swords, Shaman Restoration — change entirely, which
is expected), and `<class>/leveling/respec-plan.md` says whether a mid-leveling respec pays for itself.

## Fight lab (Monte Carlo fight simulator)

The scorer is an expected-value model; the **fight lab** (`_reference/data/fightlab/`) plays leveling fights out in time with
dice for every class (same-level mobs from the Classic 1.12 creature database, including caster mobs; beta-client ability
numbers; gear from the Classic item database, greens or dungeon blues) and measures time per kill, deaths, downtime and the value of each talent when it is
removed. It calibrates the scorer's leveling values, races the hand drafts against the optimizer's candidates, and writes the
"Fight lab" section of each class's `leveling/README.md`, `<class>/leveling/fightlab/`, and [`_reference/fightlab-summary.md`](_reference/fightlab-summary.md).
`python _reference/data/rebuild.py` runs the whole chain; every number is a simulation of stated assumptions, not a beta measurement.

## Raid sim (community simulator)

For level 60 the community's simulator (the ElliotWood/Forever wowsims fork) already models the beta's spells, items, buffs
and rotations. `_reference/data/raidsim/run.py` runs every raid build through it next to the simulator's own preset talents,
with the same gear, rotation and buffs per spec, and writes `<class>/raid/raidsim/`, the "Raid sim" section of each class's `raid/README.md` and [`_reference/raidsim-summary.md`](_reference/raidsim-summary.md). Simulations of the community's model, not measurements.

## Editing rules (short version)

- Edit `builds.json` / `proposed-builds.json`, never the generated `.md` pages; then run validate + render.
- Talent names must match the datasets exactly (the validator will tell you).
- Anything about Forever must say which beta build it is based on; beta numbers change between builds.
- Keep the class folders identical in shape — a new optimization category gets the same sub-folder name in every class.

See `CLAUDE.md` for the full conventions and `_reference/methodology.md` for how builds are derived.
