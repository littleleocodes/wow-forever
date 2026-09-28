# Handoff — continuing this project in a Claude Code cloud session (2026-09-28)

This knowledge base was built in local Claude Code sessions on Windows (project in `F:\wow-forever`, simulator tools in
`%USERPROFILE%\.wow-forever-tools`) and moved to GitHub on 2026-09-28 so the work can continue in Claude Code cloud sessions.
Read `CLAUDE.md` (the conventions, loaded automatically) and `README.md`, then this page.

## Start of every cloud session

1. **Only if the task needs the raid simulator** (`raidsim/run.py`, `apl_opt.py`, `talent_opt.py`, `calibrate.py`, `rebuild.py`
   with the raid step): `python _reference/data/cloud_setup.py` (add `--classic` for the Classic-era checks). It pip-installs
   `requirements.txt` (numpy), builds the ElliotWood/Forever simulator at the pinned commit **40be98e** with our patches and the
   `foreverbench` tool under `~/.wow-forever-tools`, and runs the checks. It takes several minutes: run it in the background (or
   with the 10-minute timeout) and read its output. The container is thrown away after the session, so the tools are rebuilt
   each session that needs them.
2. Everything else (fight lab, scorer, healer lab, renderers, validation) needs only Python 3 and numpy:
   `python -m pip install -r requirements.txt`.
3. **Commit and push before the session ends**: files left in the container are lost. Commit to a branch and open a pull
   request, or push to `main` if the user says so.

Cloud notes:

- Linux paths and tools: the scripts handle both platforms (the bench is `foreverbench` there, `foreverbench.exe` on Windows).
  `raidsim/setup.py` uses the container's Go (with `GOTOOLCHAIN=auto` the Go module proxy supplies the version the simulator's
  `go.mod` asks for) because go.dev is not on the default network allowlist, and falls back to the `grpcio-tools` protoc if the
  GitHub release download is blocked.
- Network: the default "Trusted" access reaches GitHub, the Go module proxy and PyPI, which is enough for `cloud_setup.py`. The
  data sites (talentsforever.com, warcraftforever.games, thewowdb.com, wago.tools, wowforevertalents.com) are not on it: the beta
  data refresh (`refresh_forever_talents.py --fetch`, `check_beta_build.py`) and the talentsforever comparison below need the
  cloud environment's network access set to Full, or Custom with those domains.
- Long jobs: shell commands stop at 10 minutes. Run `rebuild.py`, `apl_opt.py --all`, `talent_opt.py` and big races in the
  background and poll their logs. Timings from the local machine (12 threads): full raid step with `--jobs 3` about 20 minutes,
  a rotation pass over every entry about 2 hours, a talent search 1 to 5 minutes, regen about 15 minutes.
- The repository stores LF line endings (`.gitattributes`). The local sessions' notes are in `_reference/notes/` (below).

## Where things stand (2026-09-28)

Everything below is generated and current as of this date; the pages are the source, not this summary.

- **Nine classes, three scenarios each** (leveling, raid, PvP): hand drafts and optimizer builds in each
  `<class>/talents/forever/proposed-builds.json`, rendered to `<class>/<scenario>/builds/`. Beta data: client build 1.60.1.70009.
- **Leveling**: the fight lab (`_reference/data/fightlab/`) with tuned rotation rules; `_reference/fightlab-summary.md`.
- **Raid DPS**: ranked on a boss-level training dummy with your own buffs and consumables (the user's method), raid column
  next to it, in the community simulator; tuned rotations per spec and setting; `_reference/raidsim-summary.md` and each
  `<class>/raid/README.md`. Healers: the healer lab; tanks: tank value in the raid setting.
- **New-builds survey** (the last request): `_reference/new-builds-survey.md` (every new Forever spell, its measured use, and
  the builds searched around new spells).
- **Checks at handoff**: all builds valid; fight-lab mage regression IDENTICAL; Classic check 0 changed cases; 2050 relative
  links, 0 broken (`_reference/data/linkcheck.py`).

Best raid DPS build per class on 2026-09-28 (training dummy / fully buffed raid, community simulator 40be98e):

| Class | Best on the training dummy | DPS | Best in a raid | DPS |
|---|---|---|---|---|
| Druid | `opt-balance-dps-raid-dps` | 462 | `opt-feral-cat-dps-raid-dps` | 566 |
| Hunter | `mm-hawk-raid` (Summon Hawk; rests on the simulator's hawk model) | 469 | `mm-hawk-raid` | 815 |
| Mage | `frost-fingers-of-frost-raid` | 588 | `frost-fingers-of-frost-raid` | 667 |
| Paladin | `opt-ret-dps-raid-dps` | 368 | `ret-full-buffs-raid` | 805 |
| Priest | `opt-shadow-dps-raid-dps` | 554 | `opt-shadow-dps-raid-dps` | 636 |
| Rogue | `opt-combat-daggers-raid-raid-dps` | 414 | `opt-combat-daggers-raid-raid-dps` | 742 |
| Shaman | `opt-enhancement-dps-raid-dps` | 415 | `opt-enhancement-dps-raid-dps` | 774 |
| Warlock | `demonology-pact-raid` (Demonic Pact) | 622 | `demonology-pact-raid` | 761 |
| Warrior | `opt-fury-dw-raid-raid-dps` | 257 | `opt-arms-2h-raid-raid-dps` | 457 |

### What the last local session did (2026-09-27/28)

- Raid rotation search (`raidsim/apl_opt.py`), leveling rule search (`fightlab/rotation_opt.py`), healer heal-choice search
  (`heallab/rotation_opt.py`); the search pool now also offers each cooldown on its own and every new Forever spell, and later
  passes accumulate in `<class>/raid/raidsim/<spec>-rotation-search.json`.
- Mana limit model (running out of mana is lost damage on the dummy), the simulator's presets compete in the raid step,
  re-seeding of zeroed fits.
- **Bench bug fixed**: the simulator only used a potion, Demonic Rune or Thistle Tea when they were in the lists its UI sends;
  our configs never were, so no raid number before 2026-09-28 includes them. Everything was re-run afterwards.
- Simulator talent search (`raidsim/talent_opt.py`) for builds without a scorer model; Frostfire Bolt implemented in the
  simulator by us (`raidsim/patches/`); the new-builds survey and its builds (`mm-hawk-raid`, `demonology-pact-raid`,
  `arcane-blast-raid`, `assassination-seal-fate-raid`, `subtlety-hemo-raid`, `smite-discipline-raid`,
  `destruction-incinerate-raid`, plus `frostfire-raid`); `raidsim/add_survey_builds.py` writes such builds from a config.

## Open items

1. **Done 2026-09-28 (cloud session): popular builds on talentsforever.com vs ours.** The site exposes its popularity list as a
   static script, `https://talentsforever.com/popular.js` (top 5 level-60 builds per class; mage #1 is the user's 0/29/22).
   `popular_builds.py` archives and decodes it, `popular_race.py` races the 45 builds in the raid sim (dummy and raid), the tank
   and healer tools and the fight lab; report `_reference/popular-builds.md`. Re-run both after the site's list changes
   (`popular_builds.py --fetch`, then `popular_race.py`). The cloud session reached talentsforever.com with the default network.
2. Model caveats to keep in mind: the Summon Hawk builds rest on the simulator's guess of the hawks' follow-up swings (the client
   does not describe them); Frostfire Bolt is our own implementation; talent searches are local and run on the dummy only.
3. From the notes in `_reference/notes/`: `abs_dps_factor` still 1.0 for most classes; Bastion / Focused Rage (tables vs notes);
   a druid AoE variant; healer gear from the item database; `professions/` not started; Improved Voidwalker needs a hand template
   in the warlock AoE model; Penance's healer sustain leaks into Shadow's mana limit; the heal-lab refit with the crit cap;
   enhancement leveling calibration; warlock `calibrate_levels`; Mutilate with swords; Arms APL; moonkin Wrath weaving.
4. Beta: the beta runs 2026-09-17 to 2026-10-21 (level cap 20, 30 later). When a new client build appears
   (`check_beta_build.py`), follow CLAUDE.md's "When a new beta build lands".

## Notes from the local sessions

`_reference/notes/` holds the notes the local Claude Code sessions kept for themselves (project layout, beta data sources,
fight lab, raid sim, scenario weights, rotations and the survey). They are dated background, written as the work happened:
check a note against the code before relying on it.

## Commands used most

```
python _reference/data/rebuild.py [classes] --jobs 3                  # everything (hours)
python _reference/data/rebuild.py --steps raid,adopt,regen --jobs 3   # the raid step for every scorer model, then the pages
python _reference/data/rebuild.py --steps regen                       # only the generated pages
python _reference/data/raidsim/apl_opt.py <class> --spec <entry> --write     # rotation search (or --all)
python _reference/data/raidsim/talent_opt.py <class> --spec <entry> --start <build id | candidate .json | "sim preset: X"> --write <candidate .json>
python _reference/data/raidsim/run.py <class> --spec <entry> --iterations 20000 --write      # race (+ --env environments)
python _reference/data/validate_builds.py && python _reference/data/render_builds.py
python _reference/data/fightlab/regression.py             # must print IDENTICAL
python _reference/data/scorer/classic_check.py            # Classic calibration cases
python _reference/data/scorer/scenario_audit.py --write
python _reference/data/scorer/pvp_check.py --write
python _reference/data/linkcheck.py
```
