---
name: wow-forever-beta
description: "WoW Forever beta (2026-09-17 to 2026-10-21) — cap 20 now, 30 later; the project's Forever data is beta client build 1.60.1.70009 since 2026-09-25; which sources and scripts refresh it and what is still unmeasured"
metadata:
  node_type: memory
  type: project
  originSessionId: 1178b215-3b7e-4e8a-a51c-7bba704c0381
  modified: 2026-09-26T01:54:28.240Z
---

The WoW: Forever beta opened 2026-09-17 with a **level-20 cap** (Blizzard raises it to 30 "after a couple of weeks";
not announced as of 2026-09-25) and ends 2026-10-21; no raid or 31-60 testing. Builds: 69876/69893 (09-17), 69913
(09-18), 69977 (09-22), **70009 (09-24, first class tuning; dev notes on the Blizzard forums)**.

On 2026-09-25 the project replaced the demo snapshot with beta-client data (F:\wow-forever, see
`_reference/beta-refresh-2026-09-25.md` for the full analysis). Sources that worked: talentsforever.com `data.json`
(CC BY 4.0; per-rank talent text + class spellbooks with level-60 tooltips and coefficients), thewowdb.com per-class
talent pages (embedded Trait-table JSON per build), warcraftforever.games (Next.js payload; its TLS cert had expired,
the script retries unverified), wowforevertalents.com/beta (what each build changed), the ElliotWood/Forever wowsims
fork (`docs/beta-pass/<class>.md`: per-spell old→new client numbers). Wowhead and Icy Veins pages mostly 403/empty
through WebFetch; Blizzard news works.

**Why:** the user wants demo estimates replaced by concrete beta numbers for talents and spells and the model
re-tuned after each build.

**How to apply:** `python _reference/data/refresh_forever_talents.py --fetch --raw <date>-beta-<build> --previous
<last pull>` then `build_forever_spells.py --raw <same>`, `scorer/effects.py`, the 47 optimizer runs (`run.py`
per `<class>/talents/forever/optimizer/*.md` name), validate/render, compare_effects, respec ×9, loop_audit,
render_optimizer_sections, both checklists; read `forever-talents/README.md` for cut/renamed/moved talents and fix
hand-drafted builds, `loops/*.json` and `*.manual.json` (keys are talent names). Still open: `abs_dps_factor` (all
1.0 except Hunter; sim ratios listed in the refresh report, not adopted), Bastion/Focused Rage swap (notes vs
tables), Nature's Splendor arrow, client data slips (Aspect of the Hawk r6, Trueshot Aura r5, Penance r4).
Related: [[wow-forever-project]].
