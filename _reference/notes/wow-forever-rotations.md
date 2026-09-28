---
name: wow-forever-rotations
description: "Rotation searches (2026-09-27, user \"find an optimal rotation for all classes and talent tree specs\") - raid APL search (raidsim/apl_opt.py), leveling rule search (fightlab/rotation_opt.py), healer heal-choice search (heallab/rotation_opt.py), rotation-only raid targets, where results live"
metadata:
  node_type: memory
  type: project
  originSessionId: 1178b215-3b7e-4e8a-a51c-7bba704c0381
  modified: 2026-09-28T02:53:39.769Z
---

Three searches, all local search with common random numbers + confirmation on a second seed:
- **Raid** `raidsim/apl_opt.py [cls --spec s | --all] [--setting dummy|raid] --write`: edits the simulator's APL (move/drop/show/insert
  from the class's other APLs, drop/loosen conditions, thresholds, mana and fight-time guards, lower spell ranks, 2-edit lookahead);
  tuning builds = our best + the best sim preset; keep only if seed 2 confirms and no build loses >0.1%. Two rotations per DPS spec:
  specs.json `apl_opt` (dummy) and `apl_opt_raid` (raid, max envs); `run.py apl_path(entry, repo, where)`. Files
  `raidsim/apls/<cls>/<spec>[-raid].apl.json`, records `<cls>/raid/raidsim/<spec>-rotation-search.json`. Bench accepts per-build
  `apl`/`apl_json` and absolute paths (main.go rebuilt). A 3000-iteration sim takes ~0.05 s.
- **Rotation-only targets** (`rotation_only`, `preset_names` in specs.json): arcane-dps, smite-dps, demonology-raid, bm-raid,
  melee-dps (our gear set + base APL; sim has only Aspect of the Hawk -> lower bound), assassination-raid (our
  assassination-mutilate-raid moved there), subtlety-raid. rebuild raid_step and calibrate skip them.
- **Leveling** `fightlab/rotation_opt.py --all --write`: engine `veto` rules in `Fight.can_afford` (off / min_mana / min_hp /
  max_hp), drink/eat thresholds, module `ROTATION_KNOBS`; files `fightlab/rotations/<cls>-<spec>.json` applied by `run.make_module`;
  `WOW_FL_ROTATION=default` = hand-written (regression uses it, still IDENTICAL). Frost leveling: never Fire Blast, never Cone of
  Cold, drink below 25%, Frostbolt only >10% mob hp: -5.5% time per kill.
- **Healers** `heallab/rotation_opt.py --all --write`: tables policy (DOWNRANK, HOT_REFRESH_DEFICIT, EMERGENCY, RAID_HEAL_AT,
  GROUP_HEAL_MIN, POTION_*), files `heallab/rotations/<cls>-<spec>.json`, `tables.apply_rotation` in run.py/calibrate.py.
- Pages: render_rotations shows tuned vs simulator rotation, the changes and gains, the raid-setting rotation, leveling "Tuned
  rules"; render_heallab_sections the tuned heal choice.
Early raid results: Fire +6.5% (Scorch to top, Fire Blast unconditional, Arcane Missiles on proc), MM +4.7% dummy, Balance +4.8%,
Frost none (sim's rotation locally optimal). After searches: re-run rebuild raid/adopt (+ leveling calibrate/race, heal) + regen.
Related: [[wow-forever-raidsim]], [[wow-forever-fightlab]].
2026-09-28 additions: apl_opt pools gained explicit cooldown casts (`cooldown_pool`) and the top rank of every spell the beta
spellbook marks new (`new_spell_pool`); a search from our tuned rotation appends a pass to the record (`passes`); entries can
carry our own base rotation (`*.base.apl.json`, `rotation_note`) and `tune_builds`. First finds: Shadow Word: Death +1.1% for
Shadow (no tuned rotation cast it).
New-builds survey done 2026-09-28 (after the potion fix, full rotation pass + raid step + regen): page `_reference/new-builds-survey.md`, notes `_reference/data/new-builds.json`, renderer `render_new_builds.py` (regen step; raid README section "New spells and builds"). New drafts (simulator-searched, no scorer model, rotation-only entries): mm-hawk-raid (hunter best, 469 dummy / 815 raid; rests on the sim's hawk-swing assumption), demonology-pact-raid (warlock best, 622 / 761), arcane-blast-raid, assassination-seal-fate-raid (ties rogue best on the dummy; rotation never casts Mutilate), subtlety-hemo-raid, smite-discipline-raid, destruction-incinerate-raid; frostfire-raid kept. Seal of Fury and Incinerate entries stay on their designed base rotations because the rotation search swaps the new spell out (twist / Shadow Bolt). Wrack probe: loses. Primal Bite is Bear-only. Frostfire leveling report `frostfire-leveling` (mage extra report).
