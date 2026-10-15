# Sources

## WoW: Forever — beta client data (the current snapshot, build 1.60.1.70291, refreshed 2026-10-08)

The build every page names comes from `_reference/data/data_build.py`. Earlier pulls (70009 of 2026-09-25, 70170 of 2026-10-03) are
archived under `_reference/data/raw/` (`raw/README.md` lists them).

| Source | Used for | Notes |
|---|---|---|
| [talentsforever.com data export](https://talentsforever.com/data.json) (`/data.json`, per class `/data/<class>.json`) | **Per-rank talent tooltips, rank caps and positions** (70291 export generated 2026-10-08) and the **class spellbooks**: every trainer spell and rank with learn level, cost, cast, cooldown, level-60 tooltip, coefficient and the Classic text where it differs → `_reference/data/forever-talents/`, `_reference/data/forever-spells/`, `<class>/research/spells/README.md` | CC BY 4.0; read from the beta client's data files. Archived under `raw/2026-10-08-beta-70291/talentsforever-com/` (earlier: `raw/2026-09-25-beta-70009/`, `raw/2026-10-03-beta-70170/`) |
| [thewowdb.com — WoW Forever talents](https://thewowdb.com/wow-forever/talents/) (`/wow-forever/talents/<class>/`) | Trait-table snapshot of the build embedded in each class page (rows, columns, rank caps, prerequisite arrows, spell ids): cross-check of positions and prerequisites | Evidence: wago.tools TraitNode/TraitEdge tables for the build |
| [warcraftforever.games — talent calculator](https://warcraftforever.games/talents) (`/talents/<class>`) | Talent ids, icons, Classic status/diff/tooltips and removed-Classic-talent lists that the merged JSON keeps (current read: beta client 1.60.1.70205, captured 2026-10-04; first read 69893, 2026-09-18); before that, the BlizzCon demo transcription (2026-09-13, archived under `raw/2026-09-13-demo/`) | Site certificate had expired on 2026-09-25; the refresh script retries unverified |
| [wago.tools DB2 browser](https://wago.tools/db2/) (`/db2/<Table>?build=1.60.1.70291`) | Client tables of build 70291: ExpectedStat (creature health for rage from damage taken), PlayerExpectedStat (crit per Agility and Intellect by level, `fightlab/player_expected_stat.json`), GlobalStrings rows (hit caps, pet bonuses) | Read by the 2026-10-09 audit; archived under `raw/2026-10-08-beta-70291/client-tables/` |
| [wowforevertalents.com — beta changes](https://wowforevertalents.com/beta/) and [talentsforever.com — beta builds](https://talentsforever.com/builds) | What each beta build changed (build by build, with Blizzard's notes checked against the tables): 536 changes since BlizzCon as of 2026-09-25 | Text of 2026-09-25 archived under `raw/2026-09-25-beta-70009/` |
| [ElliotWood/Forever (GitHub)](https://github.com/ElliotWood/Forever) — `docs/beta-pass/<class>.md`, `docs/data-changes/` | A wowsims fork read against the beta client: per-spell old → new numbers (base damage, coefficients, cooldowns, threat values such as Sunder Armor's 1013), talent curves, row-level diffs per build | Cross-check of the spellbook data and the spec-model notes; the simulator itself is listed below |
| [WoW Forever Beta Development Notes – updated September 24](https://us.forums.blizzard.com/en/wow/t/wow-forever-beta-development-notes-%E2%80%93-updated-september-24/2360696/1) (Blizzard forums; mirrored by [Warcraft Tavern](https://www.warcrafttavern.com/forever/news/wow-forever-beta-update-bug-fixes-class-changes-gamepad-support/) and [Icy Veins](https://www.icy-veins.com/wow-forever/news/class-and-race-changes-gamepad-support-and-more-wow-forever-beta-development-notes-september-24th/)) | The official class, racial, item, respec and UI changes of build 70009; later beta notes (2026-10-01, 10-02, 10-08) are quoted with their dates in `_reference/data/raidsim/patches/README.md` | |
| Blizzard class deep dives (Rogue and Warlock, 2026-10-07) | "Pets now scale from their summoner's stats" (demon scaling patch) | Quoted in `raidsim/patches/README.md`; URL not recorded |
| [The World of Warcraft: Forever Beta Now Live](https://news.blizzard.com/en-us/article/24304160/the-world-of-warcraft-forever-beta-now-live) (Blizzard) | Beta dates, level-cap schedule (20, later 30), week-1 content | |
| [Wowhead — Forever beta class tuning datamine](https://www.wowhead.com/forever/news/wrath-lightning-bolt-and-holy-strike-buffs-wow-forever-beta-class-tuning-changes-383092), [Legacy system explained](https://www.wowhead.com/forever/news/warcraft-forever-legacy-system-explained-382842) | Cross-check of the tuning; the Legacy system | |
| [Icy Veins — Legacy system guide](https://www.icy-veins.com/wow-forever/legacy-system), [Warcraft Tavern — beta phases](https://www.warcrafttavern.com/forever/guides/beta/) | Legacy perks, beta phases | |
| [talentsforever.com popularity list](https://talentsforever.com/popular.js) | The top 5 level-60 builds per class and per-talent pick rates (`popular_builds.py`, `popular_picks.py`) | Archived per pull under `raw/<date>-talentsforever-popular/`; popularity, not performance |

## Simulators and game databases

| Source | Used for | Notes |
|---|---|---|
| [ElliotWood/Forever (GitHub)](https://github.com/ElliotWood/Forever), live UI at [elliotwood.github.io/Forever](https://elliotwood.github.io/Forever/) | The level-60 raid simulator (wowsims fork): every raid race, rotation and talent search, gear tiers; the pages' "Open in the simulator" links | Pinned commit in `_reference/data/raidsim/setup.py` (2ce8265, client 70291, since 2026-10-09); our patches in `raidsim/patches/README.md` |
| [wowsims/classic (GitHub)](https://github.com/wowsims/classic) | Classic Era calibration of the stats model (`rebuild.py --steps classic`) | Pinned commit in `raidsim/setup.py` |
| [Wowhead Forever item database](https://www.wowhead.com/forever/) (`/forever/item=<id>`) | Item links on the gear tables (`raidsim/gear_links.py`); conjured food and water values (`raw/2026-09-26-beta-70009-tables/`) | The database the simulator's UI uses |
| [cmangos/classic-db (GitHub)](https://github.com/cmangos/classic-db) (`Full_DB/ClassicDB_1_12_1_z2815.sql.gz`) | Mob health, damage, armor and caster share by level; leveling gear by level (fight lab) | Classic 1.12 data, a Forever assumption; extract archived under `raw/2026-09-26-cmangos-classic-db-z2815/` |

## WoW: Forever — reveal-era sources (still cited for facts the beta has not changed)

| Source | Used for | Notes |
|---|---|---|
| [warcraftforever.games — classes](https://warcraftforever.games/classes) and per-class pages (`/classes/<class>`) | New / changed / removed talent lists per class | Fan site |
| [Deradon/wow-forever-talent-calc (GitHub)](https://github.com/Deradon/wow-forever-talent-calc) | Independent second demo dataset and the **Classic Era prior** dataset | MIT code; talent text is Blizzard's |
| [Wowhead — Forever talent calculator](https://www.wowhead.com/forever/talent-calc) and [Forever talents list](https://www.wowhead.com/forever/spells/talents) | Cross-check | JS-rendered; not scraped |
| [Icy Veins — Forever talent calculator announcement](https://www.icy-veins.com/wow-forever/news/start-planning-your-wow-forever-character-with-our-new-talent-calculator/) | 51 points, 7 rows, gold-medal talents at 11/21/31 + new 16-point talent, launch date Nov 4 | |
| [wowtbc.gg — WoW Forever: what we know](https://wowtbc.gg/warcraftforever/news/what-we-know/) | Raids, zones, dungeons, races, class headline changes | |
| [Game Rant — WoW Forever revealed](https://gamerant.com/world-of-warcraft-forever-wow/) | Reveal coverage | |

## Classic Era (baseline builds)

| Source | Used for |
|---|---|
| Classic Era tree data (`_reference/data/classic-era-talents.json`) — Wowhead Classic calculator structure + melv-n/wow-talent-calculator tooltip text, packaged by the Deradon project | Validation of every baseline build (tiers, ranks, prerequisites, tooltips) |
| [Icy Veins — Classic class guides](https://www.icy-veins.com/wow-classic/) (warrior-dps, hunter-dps, rogue-dps, mage-dps, warlock-dps, priest-healer, holy-paladin-healer, restoration-shaman-healer, elemental/enhancement-shaman, restoration-druid-healer, feral-druid-tank `…-pve-spec-builds-talents`) | Mandatory vs. flex talents and build rationale |
| [Wowhead — Classic class guides](https://www.wowhead.com/classic/guides/classes) | Build splits and rotations |
| [Warcraft Tavern — Classic talent guides](https://www.warcrafttavern.com/wow-classic/guides/) | Cross-check of variants |

Per-build sources are listed in each `builds.json` entry.

## Caveats

- Beta data changes between builds; the merged talent JSON names its build and keeps the previous build's text
  (`ranks_prev`) where a tooltip changed. Tooltip numbers are level-60 values with no gear.
- The three talent datamines agreed on every position, rank cap and prerequisite of build 70009 except one arrow
  (Nature's Splendor ← Nature's Majesty, absent from the Trait-edge snapshot, kept because two client reads have it); where the
  sources disagree on a later build, `refresh_forever_talents.py` takes the talentsforever.com export's positions and prerequisites
  and lists the merge notes in `forever-talents/README.md`.
- Wowhead/Icy Veins guide pages render builds through embedded calculators, so their exact point splits
  were reconstructed from the text and validated against the tree data rather than copied.
