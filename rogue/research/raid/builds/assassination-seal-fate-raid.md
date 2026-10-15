# Assassination — Seal Fate daggers (raid) — 30/19/2

*[Rogue](../../../README.md) · [Raids: training dummy, raid and parse](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 30/19/2 (Assassination / Combat / Subtlety) |
| **Role** | DPS — Raid |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70291 (2026-10-08 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

Seal Fate daggers: Malice, Cold Blood, Seal Fate and Improved Poisons from Assassination, Puncturing Wounds, Precision and Dual Wield Specialization from Combat, and Backstab as the combo-point builder. The simulator talent search started from our Mutilate draft and moved Mutilate's point elsewhere: in the simulator Backstab, with Puncturing Wounds, builds combo points better than Mutilate, and the tuned rotation casts Backstab first. The best build that keeps Mutilate is on the survey page.

## Point allocation

### Assassination (30)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Malice** | 5/5 | changed | Increases your critical strike chance with all attacks and Poisons by 5%. |
| **Ruthlessness** | 3/3 | unchanged | Gives your finishing moves a 60% chance to add a Combo Point to your target. |
| **Improved Slice and Dice** | 3/3 | unchanged | Increases the duration of your Slice and Dice ability by 45%. |
| **Relentless Strikes** | 1/1 | unchanged | Your finishing moves have a 20% chance per Combo Point to restore 25 Energy. |
| **Lethality** | 3/5 | changed | Increases the critical strike damage bonus of your Sinister Strike, Gouge, Backstab, Mutilate, Ghostly Strike, and Hemorrhage abilities by 12%. |
| **Vile Poisons** | 2/5 | moved | Increases the damage dealt by your poisons by 8% and gives your poisons an additional 16% chance to resist dispel effects. |
| **Cold Blood** | 1/1 | changed | When activated, increases the critical strike chance of your next Sinister Strike, Backstab, Ambush, Eviscerate, or Mutilate by 100%. |
| **Seal Fate** | 5/5 | moved | Your critical strikes from abilities that add Combo Points have a 100% chance to add an additional Combo Point. |
| **Improved Expose Armor** | 2/2 | changed | Reduces the Energy cost of your Expose Armor ability by 10, and refunds 2 Combo Points when cast with 5 Combo Points. |
| **Improved Poisons** | 5/5 | changed | Increases the chance to apply Poisons to your target by 10%, and gives Poison applications a 50% chance to not consume a charge. |

### Combat (19)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Improved Eviscerate** | 3/3 | changed | Increases the damage done by your Eviscerate ability by 20%. |
| **Lightning Reflexes** | 5/5 | unchanged | Increases your Dodge chance by 5%. |
| **Puncturing Wounds** | 3/3 | **NEW** | Increases the critical strike chance of your Backstab by 30% and your Mutilate by 15%, and gives Backstab a 45% chance to add an additional Combo Point. |
| **Precision** | 3/3 | changed | Improves your chance to hit by 3%. |
| **Dual Wield Specialization** | 3/5 | changed | Increases the damage done by your off-hand weapon by 15%. |
| **Flawless Execution** | 1/1 | **NEW** | Reduces the Energy cost of your Eviscerate ability by 10. |
| **Deflection** | 1/3 | changed | Increases your Parry chance by 2%. |

### Subtlety (2)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Opportunity** | 2/2 | changed | Increases the damage dealt by your Backstab, Garrote, Ambush, and Mutilate abilities by 10%. |

## Core talents (priority order)

1. **Puncturing Wounds** — +30% Backstab crit and a 45% chance of an extra combo point. Simulator removal run (2026-09-28): the build loses 23.2% of its DPS on the training dummy without it.
2. **Relentless Strikes** — Energy back from finishers. Simulator removal run (2026-09-28): the build loses 11.4% of its DPS on the training dummy without it.
3. **Seal Fate** — Builder crits add a combo point. Simulator removal run (2026-09-28): the build loses 9.3% of its DPS on the training dummy without it.
4. **Malice** — +5% crit. Simulator removal run (2026-09-28): the build loses 5.1% of its DPS on the training dummy without it.
5. **Ruthlessness** — Finishers can add a combo point. Simulator removal run (2026-09-28): the build loses 4.6% of its DPS on the training dummy without it.
6. **Improved Slice and Dice** — Simulator removal run (2026-09-28): the build loses 4.4% of its DPS on the training dummy without it.
7. **Improved Expose Armor** — Simulator removal run (2026-09-28): the build loses 4.0% of its DPS on the training dummy without it.
8. **Improved Poisons** — +10% poison application, and applications that keep their charge. Simulator removal run (2026-09-28): the build loses 3.5% of its DPS on the training dummy without it.
9. **Precision** — +3% hit. Simulator removal run (2026-09-28): the build loses 3.0% of its DPS on the training dummy without it.

## Flex points

| Pts | Default | Alternatives | Why |
|---|---|---|---|
| 2 | Lightning Reflexes | any talent legal at that tier | Worth 0.0% of the DPS on the training dummy in the simulator: free points (a tier filler, or noise). |
| 2 | Lightning Reflexes | Endurance, any talent legal at that tier | Worth 0.0% of the DPS on the training dummy in the simulator: free points (a tier filler, or noise). |
| 2 | Deflection | Improved Sprint, any talent legal at that tier | Worth 0.0% of the DPS on the training dummy in the simulator: free points (a tier filler, or noise). |

## Rank among our builds and the community simulator's

**1 of 6** for `assassination-raid` by training-dummy DPS in the community simulator (ElliotWood/Forever 2ce8265); full ranking and the other builds' rotations: [raid README](../README.md), [raid rotations](../rotation.md).

| Rank | Build | By | Split | Dummy DPS | vs best | Raid DPS | vs best in a raid | Out of mana on the dummy |
|---|---|---|---|---|---|---|---|---|
| 1 | **[`assassination-seal-fate-raid`](assassination-seal-fate-raid.md)** | ours: hand draft | 30/19/2 | 422 | +0.0% | 702 | -0.7% | 0 s |
| 2 | [`assassination-ml-raid`](assassination-ml-raid.md) | ours: hand draft | 30/19/2 | 410 | -2.7% | 707 | +0.0% | 0 s |
| 3 | [`daggers-split-ml-raid`](daggers-split-ml-raid.md) | ours: hand draft | 30/19/2 | 410 | -2.7% | 707 | +0.0% | 0 s |
| 4 | [`assassination-mutilate-raid`](assassination-mutilate-raid.md) | ours: hand draft | 30/21/0 | 410 | -2.8% | 690 | -2.4% | 0 s |
| 5 | *Mutilate* | community simulator | - | 386 | -8.5% | 672 | -4.9% | 0 s |
| 6 | *Assassination Mutilate 31/20/0* | community simulator | - | 374 | -11.3% | 654 | -7.4% | 0 s |

## Rotation (community simulator, training dummy)

- **The training dummy:** our tuned rotation (`raidsim/apl_opt.py`, 2026-09-28, 9 passes, the last 2026-10-14, 11 changes to the base rotation; third-seed check: ):
  1. insert at the top: if time left on Expose Armor < 3 and combo points ≥ 5 and time left in the fight ≥ 3: cast Expose Armor (+8.6%, pass 1)
  2. threshold 5 -> 3.75: if time left on Expose Armor < 3 and combo points ≥ 5 and time left in the fight ≥ 3: cast Expose Armor (+0.8%, pass 1)
  3. insert at the top: cast Backstab (+1.6%, pass 1)
  4. only with 10s or more of the fight left: if time left on Expose Armor < 3 and combo points ≥ 3.75 and time left in the fight ≥ 3: cast Expose Armor (+0.2%, pass 1)
  5. threshold 6 -> 12: if (combo points ≥ 1 and not Slice and Dice is up and time left in the fight ≥ 6 or combo points ≥ 5 and time left on Slice and Dice < 3 and time left in the fight > 9): cast Slice and Dice (+0.2%, pass 1)
  6. threshold 4 -> 5: if combo points ≥ 4 and Slice and Dice is up: cast Cold Blood + drop 'combo points ≥ 5 and time left on Slice and Dice < 3 and time left in the fight > 9' from the condition: if (combo points ≥ 1 and not Slice and Dice is up and time left in the fight ≥ 12 or combo points ≥ 5 and time left on Slice and Dice < 3 and time left in the fight > 9): cast Slice and Dice (+0.3%, pass 1)
  7. insert at the top: if energy ≤ 29 and timeToNextEnergyTick > 1 and combo points < 5 and not Adrenaline Rush is up: cast Thistle Tea + threshold 29 -> 43.5: if energy ≤ 29 and timeToNextEnergyTick > 1 and combo points < 5 and not Adrenaline Rush is up: cast Thistle Tea (+0.3%, pass 3)
  8. spell probe: insert at the end: cast Hemorrhage (+8.4%, pass 5)
  9. spell probe: insert at the top: if auraIsInactive: cast Ghostly Strike (+2.0%, pass 5)
  10. drop: if energy ≤ 43.5 and timeToNextEnergyTick > 1 and combo points < 5 and not Adrenaline Rush is up: cast Thistle Tea (+2.8%, pass 8)
  11. spell probe: insert at the top: if auraIsInactive: cast Adrenaline Rush (+1.8%, pass 9)
- **A fully buffed raid:** our tuned rotation (`raidsim/apl_opt.py`, 2026-09-28, 11 passes, the last 2026-10-14, 5 changes to the base rotation; third-seed check: ):
  1. insert before the filler: cast Backstab (+0.8%, pass 1)
  2. spell probe: insert at the end: cast Hemorrhage (+9.9%, pass 5)
  3. spell probe: insert in the middle: if auraIsInactive: cast Ghostly Strike (+1.8%, pass 5)
  4. move down below 'cast Mutilate': cast Backstab (+0.2%, pass 9)
  5. spell probe: insert in the middle: if auraIsInactive: cast Adrenaline Rush (+1.4%, pass 11)

| # | Priority (the first line whose condition holds is cast) | [`assassination-seal-fate-raid`](assassination-seal-fate-raid.md) casts/min |
|---|---|---|
| 1 | cast Backstab | 11.6 |
| 2 | if time left on Expose Armor < 3 and combo points ≥ 3.75 and time left in the fight ≥ 3 and time left in the fight ≥ 10s: cast Expose Armor | 1.8 |
| 3 | if combo points ≥ 1 and not Slice and Dice is up and time left in the fight ≥ 12: cast Slice and Dice | 2.9 |
| 4 | if Slice and Dice is up: use every other cooldown when ready | as ready |
| 5 | if combo points ≥ 5 and Slice and Dice is up: cast Cold Blood | 0.3 |
| 6 | if combo points ≥ 4 and (Slice and Dice is up or energy ≥ 79 or time left in the fight < 6): cast Eviscerate | 2.8 |

Lines of the simulator's rotation these builds never cast: cast Adrenaline Rush (needs the Adrenaline Rush talent); cast Ghostly Strike (needs the Ghostly Strike talent); cast Mutilate (needs the Mutilate talent); cast Hemorrhage (needs the Hemorrhage talent).

Damage by ability:

| Ability | [`assassination-seal-fate-raid`](assassination-seal-fate-raid.md) |
|---|---|
| Auto Attack | 40% |
| Backstab | 31% |
| Eviscerate | 12% |
| Deadly Poison | 8% |
| Dense Sharpening Stone | 5% |
| Dragonbreath Chili | 2% |
| Goblin Sapper Charge | 2% |

## Notes

- Talents from the simulator talent search (raidsim/talent_opt.py, 2026-09-28) from `assassination-mutilate-raid`: 2 points Murder -> Improved Expose Armor, 1 point Venom -> Flawless Execution, 2 points Dual Wield Specialization -> Opportunity, 2 points Vigor -> Improved Poisons, 1 point Mutilate -> Improved Poisons, 2 points Lethality -> Improved Poisons.
- New-builds survey (2026-09-28, user request): see _reference/new-builds-survey.md. A simulator-searched build: no scorer model covers it, so it is raced and ranked, not optimized or audited.
- 2026-09-29 filler audit (raidsim/filler_audit.py, user question on zero-value fillers): points the simulator measures at 0 moved, one at a time, to talents that help in a real raid (interrupt protection, threat, mana, range, survival; the simulator cannot see these, so the order is our judgment) or that gain DPS: Endurance -> Lightning Reflexes (survival); Endurance -> Lightning Reflexes (survival); Improved Sprint -> Lightning Reflexes (survival); Improved Sprint -> Deflection (survival). Net +0.00% on a third seed.
- 2026-09-30: renamed from "Assassination/Combat — Seal Fate daggers (raid)" so the name matches the spec the pages file it under (the point split decides the spec, spec_modes.py).

## Open questions (verify in the live game)

- Mutilate against Backstab in the game: the simulator implements Forever's Mutilate from the client (both weapons, more damage on poisoned targets) and still prefers Backstab with this gear.

## Sources

- <https://github.com/ElliotWood/Forever/blob/master/ui/specs/rogue/dps/presets.ts>
- <https://warcraftforever.games/talents/rogue>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
