---
name: wow-forever-ml-pipeline
description: "Systematic ML raid optimisation (2026-10-01/02, done): ml_pipeline.py steps, ml_builds.py rules (0.5% to write, 2% to replace, align, parse), gear tier pool rules, results (Frost +13.7%, Destruction +12%), bugs found, what to re-run"
metadata:
  node_type: memory
  type: project
  originSessionId: 1178b215-3b7e-4e8a-a51c-7bba704c0381
  modified: 2026-10-02T16:42:06.400Z
---

User request 2026-10-01: a systematic machine-learning approach to every raid DPS spec + WoWSims-style DPS rankings for pre-BiS and
phase-1 BiS + "the system must be allowed to use every spell". Code under `_reference/data/raidsim/`: `ml_talents.py` (Space rules,
Sim, RF surrogate + GA, successive-halving race, neighbour certificate), `spell_probe.py`, `gear_tiers.py`, `ml_pipeline.py` (steps
targets, gear, spells, talents, rotations, final; records `raidsim/ml/<class>-<spec slug>.json`, resumable; ~15 h for 26 specs, the
rotation step alone 7.7 h), `ml_builds.py` (`--builds`: `-ml-raid` only when 0.5%+ ahead of every build in the comparison race, else
"confirms"; `replaces` at 2% over the best hand draft; `align` moves free points toward the hand draft; `-ml-parse` at 2% over the
dummy winner in a full raid and 0.5% over existing parse builds; `--rank`: `_reference/dps-rankings.md`). See CLAUDE.md "Systematic search".

Done 2026-10-02: new picks Frost mage 21/0/30 (+13.7%), Destruction 10/11/30 Shadow Bolt (+12.0%), Beast-Marks (+2.6%), MM (+2.4%),
Enhancement (+2.0%); Ret ML build an alternative (+1.7%); parse builds BM, MM, Survival, Enhancement; 20 specs confirmed. Then
`rebuild.py --steps raid,adopt` + run.py for the 13 rotation-only entries (rebuild's raid step skips them) + regen; checks all clean.
Private artifact with the rankings: https://claude.ai/artifact/1pQVMKZPb5NkU1jCPLdQSw (generator script lived in the session scratchpad).

Bugs found: `apl_opt.bench` used the dummy rotation for raid-setting calls (fixed; setting_audit.py raid half and fullraid_search.py
results before 2026-10-01 are suspect, re-run is open); apl_opt `--tune` first tuned on the winners alone (now on top of the entry's main
builds); the pipeline must reload specs.json after the rotation step (`reload_specs`); gear_opt kept out-of-pool items and set pieces
(Bloodvine, Sulfuras; fixed); Rhok'delar is epic but sourceless at ilvl 75 -> `PHASE1_QUEST`; Scourge Invasion drops -> `EVENT_NPCS`;
fcntl is Unix-only -> `filelock.py`. Dead talents measure exactly equal under common random numbers, hence `align`.
Deferred user items: do not start without asking (the rotation re-tune and the Venom question are now covered; see HANDOFF.md).
