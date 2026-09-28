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

To pull a new beta build: `python _reference/data/refresh_forever_talents.py --fetch --raw <date>-beta-<build>`
(then `build_forever_spells.py --raw <same>`; see `_reference/data/forever-talents/README.md` for what changed).
