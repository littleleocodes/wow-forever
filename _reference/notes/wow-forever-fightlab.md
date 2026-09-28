---
name: wow-forever-fightlab
description: "Fight lab Monte Carlo simulator for all nine classes, the one-command rebuild pipeline (adopt, variants incl. AoE for every class, raid, classic, heal steps), the healer lab, mob and gear data from the Classic DBs, caster mobs, runners, multi-mob pulls, second-spec rotations, leveling guides, regression baseline, results of the 2026-09-26 rebuilds"
metadata:
  node_type: memory
  type: project
  originSessionId: 1178b215-3b7e-4e8a-a51c-7bba704c0381
  modified: 2026-09-27T00:03:16.676Z
---

Fight lab = `_reference/data/fightlab/` (engine.py, tables.py, one module per class, run.py, calibrate.py, sensitivity.py,
mob_stats.py, gear_stats.py, summary.py, regression.py) + `_reference/data/rebuild.py`, `render_fightlab_sections.py`,
`render_raidsim_sections.py`, `render_heallab_sections.py`, `render_leveling_guides.py` (`<class>/leveling/README.md`,
generated), `render_sim_presets.py` (`<class>/gear|consumables|rotation/README.md` from the raid sim's presets), the raid
sim ([[wow-forever-raidsim]]) and the healer lab (`_reference/data/heallab/`: engine.py, tables.py, priest/paladin/shaman/
druid.py, run.py, calibrate.py; README there).

**Pipeline:** `python _reference/data/rebuild.py [classes] --jobs 4 [--steps effects,calibrate,race,adopt,report,sensitivity,variants,raid,classic,heal,regen]`
(adopt is opt-in and governs leveling, raid and healer adoption): effects → calibrate ↔ optimize until the opt leveling build
repeats or a quick race says the new build is not 1% faster (candidates `cand-<tag>-rN.json`) → race (level-weighted mean
time per kill, weight = level/10) → adopt (winner ≥2% faster replaces the hand draft; old draft saved as
`cand-<tag>-hand-<date>.json`) → report (`--deltas 30,60 --gear-tiers`; extra reports for second specs play under their own
model via `spec_of_build`, `abs_dps_factor` written) → sensitivity → variants (each module's `PIPELINE["variants"]`; the mage's
`frost-aoe` model with `MOBS_PER_PULL=4`, every other class except the druid runs its main model as an AoE variant
(`MOBS_PER_PULL=3`, rogue 2) with the `leveling-aoe` profile, reported as `<spec>-aoe.md` (`run.py --name`); a new variant
exports its opt build before the first calibration) → raid (DPS and tank models) → classic → heal (the four healer models) →
regen. Log `fightlab/last-rebuild.json` merges per class. Optimizer exports are seeded with the hand drafts (`scorer/run.py
--seed`). Full leveling run with --jobs 5 ≈ 40-75 min; raid ≈ 6 min; classic ≈ 5 min + a 5 min check; heal ≈ 10 min per
class; variants ≈ 15 min per class; regen ≈ 10 min. A crash in one class thread aborts the whole run (ThreadPoolExecutor
re-raises), so re-run the interrupted classes; use distinct log names per run (two runs sharing a log file interleave).

**Multi-mob pulls / AoE:** `MOBS_PER_PULL`, `Fight.mobs`/`others()`/`alive()`/`switch(om)` (dot spreading), `hit_others`
(spell areas), `hit_others_melee` (Whirlwind / Cleave / Swipe roll the attack table per extra mob; Blade Flurry via
`mod.extra_targets`), channel ticks on every mob in the area, `tables.AOE_SPELLS` (reach, target cap, chain falloff,
`center: "target"` for Blizzard / Rain of Fire / Volley / Hurricane / Chain Lightning / Multi-Shot / Flamestrike — the engine
is one-dimensional, so a target-centred area holds mobs whose distance to the player is within the radius of the target's),
`engine.BaseModule.decide_aoe` driven by each module's `AOE` dict (channel/direct area spells when enough mobs are in reach,
then dots on every mob lacking one, else the single-target priority); the mage keeps its own `decide_aoe`. Adds stay on the
player, so classes without control die a lot in pulls (a warlock at 40: 168 deaths per 100 pulls of 3): the variant reports
say whether AoE grinding pays. Mage 4-mob pulls with a real 8 yd Blizzard radius: ~42 s per mob (was 28 s when the radius was
its 30 yd range) — re-measured after the centre fix.

**Healer lab:** one raid healer keeps a tank (9,000 hp, boss melee 2,600 pre-armor every 2 s, crushes, a 2x spike every
30 s) and four raid members (4,500 hp, 700-damage pulses every 20 s) alive for 300 s; beta spellbook heals (downranked to
the deficit, HoTs kept, group heals, cooldowns), spirit regen + FSR + mp5 + potions; talent numbers from parsed tooltips
plus hand-coded mechanics (Illumination, Divine Favor, Inner Focus, Inspiration, Nature's Swiftness, Swiftmend, Mana Tide,
Healing Stream Totem, Prayer of Mending, Penance, Water Shield, Nature's Grace). Capacity = damage multiplier survived in
90% of runs (per-run bisection, common random numbers, mean of the worst fifth: the percentile alone was noisy). Hand builds
2026-09-26: priest 0.49, paladin 0.66, shaman 0.63, druid 0.69; mana talents dominate (Meditation 15%, Illumination 21%,
Mindfulness 18%, Reflection 35% of capacity). `calibrate.py` fits only the module's `SIMULATED` talents (others keep manual
values, marked *); `rebuild.py --steps heal` = calibrate ↔ optimize ↔ race, promotion, opt-in adoption (2%); results:
priest opt 0.592 vs hand 0.494 (+4.2% after promotion; hand stands without adopt), druid opt 0.697 vs hand 0.691.

**Data (Classic 1.12 cmangos DB, raw CSVs under `raw/2026-09-26-cmangos-classic-db-z2815/`):** mob health/dmg/armor/caster
share by level (`mob_stats.json`); gear by level (`gear_stats.json`, spell power and healing from on-equip spells). Mechanics:
caster mobs, gear tiers, druid Bear Form 10-19, runners (`RUNNER_SHARE`), optimizer order rush rule, Elemental / Balance
rotations, talent-created sources (see [[wow-forever-project]]).

**Results (2026-09-26 final leveling rebuild):** all nine classes converged; hand drafts stand everywhere; level-weighted
time per kill: mage 28.0 s, priest 29.9, warlock 44.7, hunter 29.0, warrior 29.0, rogue 30.8, paladin 29.7, shaman 37.2,
druid 26.8. Spec vs spec: Enhancement 11-13% faster than Elemental, cat twice as fast as Balance, Fury ≈ Arms, swords 15%
faster than daggers, BM ≈ MM. The Forever hunter levels fastest as 20/31/0 (hand draft), which leaks into the Classic BM
check (17/31/3) because leveling values are shared across games.

**Melee hunter (2026-09-27):** scorer model `melee-dps` (sources melee/melee_oh/raptor_strike/mongoose_bite/lacerate/counterattack/
strider_kick/serpent/pet; shares are tooltip assumptions), manual effects for Savage Strikes, Predator's Edge (off-hand +10%/rank),
Expose Prey (Mongoose Bite x0.6/rank), Deadly Aspects melee haste, Improved Aspect of the Monkey (leveling only), Lone Wolf (disable
pet + 20%), Deflection/Deterrence -> Counterattack; hunter module `decide_melee` + engine `on_parry`; builds `melee-survival-raid`
(5/15/31) and `leveling-melee` (9/11/31 with order). Fight lab: melee levels like BM until ~35, then 8-10% slower at 40-50 and 24%
slower at 60 (Lone Wolf, no pet, more downtime), no deaths. The community sim has no melee hunter rotation. Scorer rule: a new
model falls back to parsed tooltip values for talents fitted only for other models (`effects_for`).
**Invariant:** `python _reference/data/fightlab/regression.py` (two frozen mage builds; `--update` after intended changes);
stayed IDENTICAL through the multi-mob, cleave and area-centre patches (single-mob fights take the same random draws).
**Gotcha:** never write Python source containing backslash escapes through a bash heredoc here; long heredocs with quotes
break too — write patch scripts with the Write tool. Never edit engine/modules while a rebuild runs; module names clash
between fightlab, heallab and the scorer (`run`, `engine`, `tables`): load by path or order sys.path deliberately.
**Not done:** levels 1-9, druid AoE variant (cats do not AoE-farm), pet-less MM / positional Backstab, Hurricane / Explosive
Trap / Sweeping Strikes mechanics, healer gear from the item database (tables assume phase-1 stats).
**Why:** the user wants the beta refresh + re-tune repeatable in one run; all numbers are simulations of stated assumptions.
**How to apply:** after any sim change run regression.py, then rebuild.py; never hand-edit generated README sections, "Fight
lab (" notes, leveling guides or summary pages. Related: [[wow-forever-project]], [[wow-forever-beta]].

2026-09-27: all three calibrations re-seed an all-zero fit when the lab measures the talent (`splitfx.reseed_zero`; own
other-mode values first, then parsed). Warlock AoE variant re-run: Improved Voidwalker came off zero but is "capped" at
0.9% vs the lab's 21.6% (pet_surv cannot express the Voidwalker holding a 3-mob pull: needs a hand template, open);
Aftermath stays dead in AoE (the AoE rotation casts no Immolate).
