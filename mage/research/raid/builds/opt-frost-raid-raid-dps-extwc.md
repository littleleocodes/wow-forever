# Optimizer — Raid Frostbolt with Ice Lance on Fingers of Frost charges (the ice_lance source, 2026-09-27) (raid-dps-extwc) — 28/1/22

*[Mage](../../../README.md) · [Raids: training dummy, raid and parse](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 28/1/22 (Arcane / Fire / Frost) |
| **Role** | DPS — Raid |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70425 (2026-10-16 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

Produced by the stats model (`_reference/data/scorer/`) for spec model `frost-raid` and profile `raid-dps-extwc`: score +87.5% (DPS gain vs. no talents). Every number behind it is in the effect files (tooltip-parsed or hand-entered with its arithmetic); change those, not this build.

## Point allocation

### Arcane (28)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Missile Barrage** | 2/2 | **NEW** | Gives your Arcane Blast spell a 40% chance, your Arcane Missile hits a 10% chance, and your Arcane Wrath, Fireball, Frostbolt, and Frostfire Bolt spells a 20% chance to reduce the channeled duration of your next Arcane Missiles spell by 50%, reduce the Mana cost by 100%, and missiles fire every 0.5 sec. |
| **Arcane Focus** | 5/5 | changed | Improves your chance to hit with Arcane spells by 5%. |
| **Arcane Concentration** | 5/5 | unchanged | Gives you a 10% chance of entering a Clearcasting state after any damage spell hits a target. The Clearcasting state reduces the mana cost of your next damage spell by 100%. |
| **Arcane Subtlety** | 2/2 | changed | Reduces your target's resistance to all your spells by 15 and reduces the threat caused by your Arcane spells by 30%. |
| **Arcane Blast** | 1/1 | **NEW** | Blasts the target with energy, dealing 34 to 38 Arcane damage. Each time you cast Arcane Blast, you gain 15% of your Intellect as Spell Damage and the mana cost of Arcane Blast is increased by 175%. Effect stacks up to 4 times and lasts 15 sec from time of initial application. |
| **Arcane Impact** | 3/3 | **NEW** | Increases the critical strike chance of your Arcane spells by 6%. |
| **Arcane Wrath** | 1/1 | **NEW** | Launches a projectile of pure Arcane energy at the enemy target, causing 122 to 146 Arcane damage. This spell gains additional Spell Damage equal to 5% of your maximum Mana. |
| **Arcane Meditation** | 1/3 | changed | Allows 17% of your Mana regeneration to continue while casting. |
| **Presence of Mind** | 1/1 | unchanged | When activated, your next Mage spell with a casting time less than 10 sec becomes an instant cast spell. |
| **Arcane Mind** | 4/5 | changed | Increases your Intellect by 8% and increases the critical strike damage bonus of your Arcane spells by 80%. |
| **Arcane Instability** | 3/3 | changed | Increases the damage done by your spells by 3% and your critical strike chance by 3%. |

### Fire (1)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Incineration** | 1/3 | **NEW** | Increases the critical strike chance of your Fire Blast, Ice Lance, Arcane Blast, and Scorch spells by 2%. |

### Frost (22)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Improved Frostbolt** | 5/5 | changed | Reduces the casting time of your Frostbolt and Frost Blast spells by 0.5 sec. |
| **Elemental Precision** | 3/3 | changed | Improves your chance to hit with Frost and Fire spells by 6%. |
| **Ice Shards** | 5/5 | unchanged | Increases the critical strike damage bonus of your Frost spells by 100%. |
| **Ice Lance** | 1/1 | **NEW** | Deals 28 to 32 Frost damage to an enemy target. Deals 200% increased damage to Frozen targets. |
| **Frost Channeling** | 3/3 | moved | Reduces the mana cost of your Frost spells by 15% and reduces the threat caused by your Frost spells by 30%. |
| **Shatter** | 3/3 | changed | Increases the critical strike chance of all your spells against Frozen targets by 50%. |
| **Fingers of Frost** | 2/2 | **NEW** | Gives your Chill effects a 15% chance to grant you the Fingers of Frost effect, which treats your next 2 spells cast as if the target were Frozen. Lasts 15 sec. |

## Core talents (priority order)

1. **Improved Frostbolt** — Removing it costs 22.1 points of score in this model.
2. **Fingers of Frost** — Removing it costs 19.4 points of score in this model.
3. **Ice Shards** — Removing it costs 16.7 points of score in this model.
4. **Ice Lance** — Removing it costs 12.5 points of score in this model.
5. **Missile Barrage** — Removing it costs 12.0 points of score in this model.
6. **Shatter** — Removing it costs 11.3 points of score in this model.
7. **Elemental Precision** — Removing it costs 10.1 points of score in this model.
8. **Arcane Instability** — Removing it costs 9.5 points of score in this model.

## Rank among our builds and the community simulator's

**1 of 11** for `frost-raid` by training-dummy DPS in the community simulator (wowsims/forever 30f67f5 (client 70450)); full ranking and the other builds' rotations: [raid README](../README.md), [raid rotations](../rotation.md).

| Rank | Build | By | Split | Dummy DPS | vs best | Raid DPS | vs best in a raid | Out of mana on the dummy |
|---|---|---|---|---|---|---|---|---|
| 1 | **[`opt-frost-raid-raid-dps-extwc`](opt-frost-raid-raid-dps-extwc.md)** | ours: optimizer | 28/1/22 | 587 | +0.0% | 680 | -1.8% | 9 s |
| 2 | *Arcane Frost* | community simulator | - | 582 | -0.9% | 693 | +0.0% | 8 s |
| 3 | [`frost-arcane-power-raid`](frost-arcane-power-raid.md) | ours: hand draft | 35/0/16 | 577 | -1.7% | 676 | -2.4% | 5 s |
| 4 | [`arcane-frost-open-raid`](arcane-frost-open-raid.md) | ours: derived (open search) | 29/0/22 | 574 | -2.3% | 693 | -0.0% | 7 s |
| 5 | [`opt-frost-raid-raid-dps`](opt-frost-raid-raid-dps.md) | ours: optimizer | 29/0/22 | 546 | -6.9% | 628 | -9.3% | 4 s |
| 6 | *Arcane Fire* | community simulator | - | 521 | -11.2% | 645 | -6.8% | 2 s |
| 7 | [`frost-ml-raid`](frost-ml-raid.md) | ours: derived (ML search) | 21/0/30 | 494 | -15.8% | 588 | -15.1% | 8 s |
| 8 | [`frost-fingers-of-frost-raid`](frost-fingers-of-frost-raid.md) | ours: hand draft | 22/0/29 | 481 | -18.1% | 547 | -21.0% | 0 s |
| 9 | *Fire* | community simulator | - | 439 | -25.2% | 504 | -27.2% | 8 s |
| 10 | [`frost-winters-chill-raid`](frost-winters-chill-raid.md) | ours: hand draft | 21/0/30 | 438 | -25.3% | 501 | -27.7% | 0 s |
| 11 | *FFB* | community simulator | - | 387 | -34.1% | 443 | -36.1% | 2 s |

## Rotation (community simulator, training dummy)

- **The training dummy:** our tuned rotation (`raidsim/apl_opt.py`, 2026-10-02, 5 passes, the last 2026-10-23, 12 changes to the base rotation; third-seed check: open winner 528 -> 577 DPS (+9.3%), opt-frost-raid-raid-dps-extwc 549 -> 586 DPS (+6.8%), sim preset: Arcane Frost 516 -> 582 DPS (+12.8%), frost-arcane-power-raid 515 -> 577 DPS (+12.2%), frost-winters-chill-raid 436 -> 441 DPS (+1.1%), frost-fingers-of-frost-raid 480 -> 484 DPS (+0.8%), opt-frost-raid-raid-dps 532 -> 566 DPS (+6.4%), frost-ml-raid 478 -> 482 DPS (+0.8%), arcane-frost-open-raid 543 -> 576 DPS (+6.2%)):
  1. drop: if mana % < 20% and time left in the fight > 25s: cast Evocation (+0.3%, pass 1)
  2. move down below 'if Missile Barrage is known and Missile Barrage is up: cast Arcane Missiles': if Fingers of Frost is up: cast Ice Lance (+0.2%, pass 1)
  3. repair: insert before the filler: if mana % < 5% and time left in the fight > 25s: cast Evocation (every frost-raid build raced, 20,000 fights, seed 3: opt-frost-raid-raid-dps-extwc +6.6%, the others -0.02% to +0.00%) (+6.6%, pass 2)
  4. only with 3s or more of the fight left: cast Frostbolt + insert at the end: if (Clearcasting is up or mana % ≥ 10%): cast Fire Blast (+0.6%, pass 3)
  5. threshold 80% -> 60%: if mana % ≤ 80%: cast Mana Ruby (mana gem) (+0.2%, pass 4)
  6. threshold 25s -> 50s: if mana % < 5% and time left in the fight > 25s: cast Evocation (+0.2%, pass 4)
  7. insert at the end: cast Arcane Blast (+0.2%, pass 4)
  8. insert in the middle: if (time left on Arcane Blast < cast time of Arcane Blast or stacks of Arcane Blast < 2): cast Arcane Blast (+10.2%, pass 5)
  9. insert at the end: cast Robe of the Archmage (+0.9%, pass 5)
  10. insert in the middle: if Arcane Wrath is ready: cast Presence of Mind (+0.7%, pass 5)
  11. move down below 'if Fingers of Frost is up: cast Ice Lance': if Missile Barrage is known and Missile Barrage is up: cast Arcane Missiles (rank 7) (+0.2%, pass 5)
  12. only above 60% mana: if mana % ≤ 60%: cast Mana Ruby + insert at the end: cast Frost Blast (+0.2%, pass 5)
- **A fully buffed raid:** our tuned rotation (`raidsim/apl_opt.py`, 2026-10-02, 7 passes, the last 2026-10-23, 6 changes to the base rotation; third-seed check: open winner 626 -> 691 DPS (+10.4%), opt-frost-raid-raid-dps-extwc 623 -> 680 DPS (+9.3%), sim preset: Arcane Frost 586 -> 693 DPS (+18.1%), frost-arcane-power-raid 585 -> 676 DPS (+15.6%), frost-winters-chill-raid 497 -> 501 DPS (+0.8%), frost-fingers-of-frost-raid 544 -> 547 DPS (+0.5%), opt-frost-raid-raid-dps 606 -> 663 DPS (+9.3%), frost-ml-raid 542 -> 545 DPS (+0.5%), arcane-frost-open-raid 622 -> 687 DPS (+10.5%)):
  1. move down below 'if Missile Barrage is known and Missile Barrage is up: cast Arcane Missiles': if Fingers of Frost is up: cast Ice Lance (+0.2%, pass 1)
  2. only with 3s or more of the fight left: cast Frostbolt + insert at the end: if mana ≥ (time left in the fight × 110): cast Fire Blast (+0.5%, pass 1)
  3. spell probe: insert in the middle: cast Arcane Wrath (+1.0%, pass 6)
  4. insert at the top: if (time left on Arcane Blast < cast time of Arcane Blast or stacks of Arcane Blast < 2): cast Arcane Blast (+6.1%, pass 7)
  5. move to the top: if Missile Barrage is known and Missile Barrage is up: cast Arcane Missiles (rank 7) (+2.2%, pass 7)
  6. only with 20s or more of the fight left: cast Arcane Wrath (+0.4%, pass 7)

| # | Priority (the first line whose condition holds is cast) | [`opt-frost-raid-raid-dps-extwc`](opt-frost-raid-raid-dps-extwc.md) casts/min |
|---|---|---|
| 1 | if mana % ≤ 60% and mana % ≥ 60%: cast Mana Ruby | as ready |
| 2 | use every other cooldown when ready | as ready |
| 3 | if Fingers of Frost is up: cast Ice Lance | 1.6 |
| 4 | if Missile Barrage is known and Missile Barrage is up: cast Arcane Missiles (rank 7) | 5.5 |
| 5 | if (time left on Arcane Blast < cast time of Arcane Blast or stacks of Arcane Blast < 2): cast Arcane Blast | 7.2 |
| 6 | if Arcane Wrath is ready: cast Presence of Mind | 0.3 |
| 7 | if mana % < 5% and time left in the fight > 50s: cast Evocation | 0.1 |
| 8 | if time left in the fight ≥ 3s: cast Frostbolt (rank 10) | 12.4 |
| 9 | if (Clearcasting is up or mana % ≥ 10%): cast Fire Blast | 0.1 |
| 10 | cast Arcane Blast | 7.2 |
| 11 | cast Robe of the Archmage | as ready |
| 12 | cast Frost Blast | 0.6 |

Damage by ability:

| Ability | [`opt-frost-raid-raid-dps-extwc`](opt-frost-raid-raid-dps-extwc.md) |
|---|---|
| Frostbolt | 43% |
| Arcane Missiles | 35% |
| Arcane Blast | 13% |
| Ice Lance | 6% |
| Demonic Rune | 2% |
| Frost Blast | 1% |
| Fire Blast | 0% |

## Notes

- Report: mage/research/talents/forever/optimizer/frost-raid-raid-dps-extwc.md

## Open questions (verify in the live game)

- Hand-entered effect values (see the manual effect file) are the weakest inputs — verify the ones this build leans on.

## Sources

- <https://warcraftforever.games/talents/mage>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
