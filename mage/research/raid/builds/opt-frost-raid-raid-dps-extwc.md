# Optimizer — Raid Frostbolt with Ice Lance on Fingers of Frost charges (the ice_lance source, 2026-09-27) (raid-dps-extwc) — 1/13/37

*[Mage](../../../README.md) · [Raids: training dummy, raid and parse](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 1/13/37 (Arcane / Fire / Frost) |
| **Role** | DPS — Raid |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70291 (2026-10-08 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

Produced by the stats model (`_reference/data/scorer/`) for spec model `frost-raid` and profile `raid-dps-extwc`: score +73.2% (DPS gain vs. no talents). Every number behind it is in the effect files (tooltip-parsed or hand-entered with its arithmetic); change those, not this build.

## Point allocation

### Arcane (1)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Wand Specialization** | 1/2 | moved | Increases your damage with Wands by 13%. |

### Fire (13)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Incineration** | 3/3 | **NEW** | Increases the critical strike chance of your Fire Blast, Ice Lance, Arcane Blast, and Scorch spells by 6%. |
| **Wake of Fire** | 2/2 | **NEW** | Reduces the cooldown of your Fire Blast spell by 2 sec. Killing a non-trivial target increases the critical strike chance of your next Fire Blast cast within 30 sec by 50%. |
| **Improved Fireball** | 3/5 | changed | Reduces the casting time of your Fireball and Frostfire Bolt spells by 0.3 sec. |
| **Flame Throwing** | 2/2 | unchanged | Increases the range of your Fire spells by 6 yards. |
| **Burning Soul** | 3/3 | changed | Gives your Fire spells a 70% chance to not lose casting time when you take damage and reduces the threat caused by your Fire spells by 30%. |

### Frost (37)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Improved Frostbolt** | 5/5 | changed | Reduces the casting time of your Frostbolt spell by 0.5 sec. |
| **Elemental Precision** | 5/5 | changed | Improves your chance to hit with Frost and Fire spells by 5%. |
| **Ice Shards** | 5/5 | unchanged | Increases the critical strike damage bonus of your Frost spells by 100%. |
| **Ice Lance** | 1/1 | **NEW** | Deals 28 to 32 Frost damage to an enemy target. Deals 300% increased damage to Frozen targets. |
| **Piercing Ice** | 3/3 | unchanged | Increases the damage done by your Frost spells by 6%. |
| **Frost Channeling** | 3/3 | moved | Reduces the mana cost of your Frost spells by 15% and reduces the threat caused by your Frost spells by 30%. |
| **Shatter** | 3/3 | changed | Increases the critical strike chance of all your spells against Frozen targets by 50%. |
| **Arctic Reach** | 2/2 | unchanged | Increases the range of your Frostbolt and Blizzard spells and the radius of your Frost Nova and Cone of Cold spells by 20%. |
| **Ice Block** | 1/1 | moved | You become encased in a block of ice, protecting you from all physical attacks and spells for 10 sec, but during that time you cannot attack, move, or cast spells. |
| **Fingers of Frost** | 2/2 | **NEW** | Gives your Chill effects a 15% chance to grant you the Fingers of Frost effect, which treats your next 2 spells cast as if the target were Frozen. Lasts 15 sec. |
| **Cold Snap** | 1/1 | changed | Finishes the remaining cooldown on all your other Frost spells. |
| **Winter's Chill** | 5/5 | changed | Gives your Frost damage spells a 100% chance to apply the Winter's Chill effect, which increases the chance your Ice Lance and Frostbolt spells will critically hit the target by 2% for 15 sec. Stacks up to 5 times. |
| **Ice Barrier** | 1/1 | changed | Instantly shields you, absorbing 447 damage. Lasts 1 min. While the shield holds, your spellcasts will not be interrupted or delayed from taking damage. |

## Core talents (priority order)

1. **Ice Shards** — Removing it costs 23.0 points of score in this model.
2. **Fingers of Frost** — Removing it costs 22.5 points of score in this model.
3. **Ice Lance** — Removing it costs 18.8 points of score in this model.
4. **Improved Frostbolt** — Removing it costs 15.9 points of score in this model.
5. **Shatter** — Removing it costs 12.6 points of score in this model.
6. **Winter's Chill** — Removing it costs 12.5 points of score in this model.
7. **Piercing Ice** — Removing it costs 9.7 points of score in this model.
8. **Elemental Precision** — Removing it costs 9.6 points of score in this model.

## Rank among our builds and the community simulator's

**7 of 13** for `frost-raid` by training-dummy DPS in the community simulator (ElliotWood/Forever 2ce8265); full ranking and the other builds' rotations: [raid README](../README.md), [raid rotations](../rotation.md).

| Rank | Build | By | Split | Dummy DPS | vs best | Raid DPS | vs best in a raid | Out of mana on the dummy |
|---|---|---|---|---|---|---|---|---|
| 1 | [`frost-ml-raid`](frost-ml-raid.md) | ours: hand draft | 21/0/30 | 604 | +0.0% | 684 | -1.1% | 0 s |
| 2 | [`frost-fingers-of-frost-raid`](frost-fingers-of-frost-raid.md) | ours: hand draft | 22/0/29 | 601 | -0.5% | 680 | -1.8% | 0 s |
| 3 | [`opt-frost-raid-raid-dps`](opt-frost-raid-raid-dps.md) | ours: optimizer | 22/0/29 | 600 | -0.8% | 680 | -1.8% | 1 s |
| 4 | [`arcane-frost-open-raid`](arcane-frost-open-raid.md) | ours: hand draft | 28/0/23 | 592 | -2.0% | 692 | +0.0% | 5 s |
| 5 | [`frost-arcane-power-raid`](frost-arcane-power-raid.md) | ours: hand draft | 32/0/19 | 573 | -5.3% | 651 | -6.0% | 0 s |
| 6 | *Frost DPS* | community simulator | - | 561 | -7.2% | 636 | -8.1% | 0 s |
| 7 | **[`opt-frost-raid-raid-dps-extwc`](opt-frost-raid-raid-dps-extwc.md)** | ours: optimizer | 1/13/37 | 550 | -9.0% | 650 | -6.0% | 7 s |
| 8 | [`frost-winters-chill-raid`](frost-winters-chill-raid.md) | ours: hand draft | 21/0/30 | 547 | -9.5% | 619 | -10.6% | 0 s |
| 9 | *Frost 14/0/37* | community simulator | - | 546 | -9.8% | 646 | -6.7% | 8 s |
| 10 | *Arcane 35/0/16* | community simulator | - | 490 | -18.9% | 557 | -19.6% | 0 s |
| 11 | *Arcane DPS* | community simulator | - | 423 | -30.0% | 475 | -31.3% | 0 s |
| 12 | *Fire 0/35/16* | community simulator | - | 392 | -35.2% | 446 | -35.6% | 0 s |
| 13 | *Fire DPS* | community simulator | - | 329 | -45.6% | 368 | -46.8% | 0 s |

## Rotation (community simulator, training dummy)

- **The training dummy:** our tuned rotation (`raidsim/apl_opt.py`, 2026-10-02, 4 passes, the last 2026-10-09, 7 changes to the base rotation; third-seed check: open winner 576 -> 605 DPS (+5.1%), frost-ml-raid 591 -> 604 DPS (+2.2%), sim preset: Frost DPS 551 -> 561 DPS (+1.7%), frost-arcane-power-raid 567 -> 572 DPS (+0.8%), frost-winters-chill-raid 544 -> 547 DPS (+0.6%), frost-fingers-of-frost-raid 588 -> 602 DPS (+2.4%), opt-frost-raid-raid-dps 580 -> 600 DPS (+3.4%), opt-frost-raid-raid-dps-extwc 545 -> 549 DPS (+0.8%)):
  1. drop: if mana % < 20% and time left in the fight > 25s: cast Evocation (+0.3%, pass 1)
  2. move down below 'if Missile Barrage is known and Missile Barrage is up: cast Arcane Missiles': if Fingers of Frost is up: cast Ice Lance (+0.2%, pass 1)
  3. repair: insert before the filler: if mana % < 5% and time left in the fight > 25s: cast Evocation (every frost-raid build raced, 20,000 fights, seed 3: opt-frost-raid-raid-dps-extwc +6.6%, the others -0.02% to +0.00%) (+6.6%, pass 2)
  4. only with 3s or more of the fight left: cast Frostbolt + insert at the end: if (Clearcasting is up or mana % ≥ 10%): cast Fire Blast (+0.6%, pass 3)
  5. threshold 80% -> 60%: if mana % ≤ 80%: cast Mana Ruby (mana gem) (+0.2%, pass 4)
  6. threshold 25s -> 50s: if mana % < 5% and time left in the fight > 25s: cast Evocation (+0.2%, pass 4)
  7. insert at the end: cast Arcane Blast (+0.2%, pass 4)
- **A fully buffed raid:** our tuned rotation (`raidsim/apl_opt.py`, 2026-10-02, 4 passes, the last 2026-10-09, 2 changes to the base rotation; third-seed check: open winner 676 -> 693 DPS (+2.4%), frost-ml-raid 673 -> 683 DPS (+1.5%), sim preset: Frost DPS 631 -> 635 DPS (+0.7%), frost-arcane-power-raid 646 -> 650 DPS (+0.6%), frost-winters-chill-raid 616 -> 620 DPS (+0.6%), frost-fingers-of-frost-raid 669 -> 680 DPS (+1.7%), opt-frost-raid-raid-dps 669 -> 680 DPS (+1.7%), opt-frost-raid-raid-dps-extwc 645 -> 650 DPS (+0.7%)):
  1. move down below 'if Missile Barrage is known and Missile Barrage is up: cast Arcane Missiles': if Fingers of Frost is up: cast Ice Lance (+0.2%, pass 1)
  2. only with 3s or more of the fight left: cast Frostbolt + insert at the end: if mana ≥ (time left in the fight × 110): cast Fire Blast (+0.5%, pass 1)

| # | Priority (the first line whose condition holds is cast) | [`opt-frost-raid-raid-dps-extwc`](opt-frost-raid-raid-dps-extwc.md) casts/min |
|---|---|---|
| 1 | if mana % ≤ 60%: cast Mana Ruby (mana gem) | as ready |
| 2 | use every other cooldown when ready | as ready |
| 3 | if Fingers of Frost is up: cast Ice Lance | 5.1 |
| 4 | if mana % < 5% and time left in the fight > 50s: cast Evocation | 0.3 |
| 5 | if time left in the fight ≥ 3s: cast Frostbolt | 19.9 |
| 6 | if (Clearcasting is up or mana % ≥ 10%): cast Fire Blast | 0.3 |

Lines of the simulator's rotation these builds never cast: cast Arcane Missiles (its condition never held in these fights); cast Arcane Blast (needs the Arcane Blast talent).

Damage by ability:

| Ability | [`opt-frost-raid-raid-dps-extwc`](opt-frost-raid-raid-dps-extwc.md) |
|---|---|
| Frostbolt | 76% |
| Ice Lance | 24% |
| Fire Blast | 1% |

## Notes

- Report: mage/talents/forever/optimizer/frost-raid-raid-dps-extwc.md

## Open questions (verify in the live game)

- Hand-entered effect values (see the manual effect file) are the weakest inputs — verify the ones this build leans on.

## Sources

- <https://warcraftforever.games/talents/mage>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
