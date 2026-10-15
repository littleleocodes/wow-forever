# Raw datamine pulls

Each folder is one pull of the sources `refresh_forever_talents.py` and `build_forever_spells.py` merge, kept so a
refresh can be reproduced or diffed later. Never edit these files.

| Folder | Contents |
|---|---|
| `2026-09-13-demo/` | The BlizzCon 2026 demo transcription the project started from (warcraftforever.games, captured 2026-09-13): rank-1 tooltips read from footage, higher ranks extrapolated (`estimated`), level-38 numbers. Replaced by the beta data on 2026-09-25. |
| `2026-09-25-beta-70009/warcraftforever-games-69893/` | warcraftforever.games Next.js payload per class: beta client 1.60.1.69893 read (captured 2026-09-18) — ids, icons, Classic status/diff/tooltips, removed-talent lists. |
| `2026-09-25-beta-70009/talentsforever-com-70009/data.json` | talentsforever.com export (generated 2026-09-24, CC BY 4.0): talents with every rank's tooltip at build 1.60.1.70009, class spellbooks with learn levels, level-60 spell tooltips with coefficients, racials, Legacy perks. |
| `2026-09-25-beta-70009/thewowdb-com-70009/` | thewowdb.com Trait-table snapshots of build 1.60.1.70009 per class: rows, columns, rank caps, prerequisite edges, spell ids. |
| `2026-09-26-beta-70009-tables/wowhead-items/` | Wowhead Forever item tooltips (`nether.wowhead.com/forever/tooltip/item/<id>`) for the seven conjured waters and seven conjured foods: mana/health restored per rank in the beta (feeds `fightlab/tables.py`). |
| `2026-09-25-beta-70009/*.txt` | Text of the wowforevertalents.com "beta changes" page (536 changes since BlizzCon, read 2026-09-25) and the talentsforever.com "beta builds" page (what each build changed). |
| `2026-09-26-cmangos-classic-db-z2815/` | Classic 1.12 creature stats extracted from the cmangos classic-db dump for the fight lab's mobs ([README](2026-09-26-cmangos-classic-db-z2815/README.md)). |
| `2026-10-03-beta-70170/` | The 70170 pull: talentsforever.com export (talents and spellbooks, with the warrior hotfixes of 1-2 October), thewowdb.com Trait snapshots for the six classes it answered, warcraftforever.games payloads. |
| `2026-10-08-beta-70291/` | The 70291 pull (the current data, `../data_build.py`): talentsforever.com export (generated 2026-10-08), thewowdb.com Trait snapshots, warcraftforever.games payloads (client 70205, captured 2026-10-04), and the client tables the 2026-10-09 audit read from wago.tools ([client-tables/README](2026-10-08-beta-70291/client-tables/README.md)). |
| `<date>-talentsforever-popular/popular.js` | talentsforever.com's popularity list and pick rates as pulled on 2026-09-28, 2026-09-30 and 2026-10-09 (`../popular_builds.py`). |

To pull a new beta build: `python _reference/data/refresh_forever_talents.py --fetch --raw <date>-beta-<build>`
(then `build_forever_spells.py --raw <same>`; see `_reference/data/forever-talents/README.md` for what changed).
