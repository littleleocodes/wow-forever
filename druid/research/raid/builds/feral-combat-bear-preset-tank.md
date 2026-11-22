# Feral Combat — Raid tank (the simulator's Bear 9/32/10) — 9/32/10

*[Druid](../../../README.md) · [Raids: training dummy, raid and parse](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 9/32/10 (Balance / Feral Combat / Restoration) |
| **Role** | TANK — Raid |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70753 (2026-11-03 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

The official simulator's own Bear preset (9/32/10), raced against our bear builds in a full raid in front of the boss on 2026-11-22: tank value 1.88 against 1.33 for our best and 1.01 for the old pick (threat 2,791 against 1,007 per second, damage taken 438 against 410). It presses **Lacerate** (kept at five stacks) and **Primal Bite** on the global cooldown and queues **Maul** with the rage left over; our bear builds, searched while Maul's damage was cast off the swing timer (fixed on 2026-11-20), took neither talent and pressed only Maul. A short check from it kept two moves for +1.76% tank value; a full search follows in the optimality pass. The simulator's model of the beta, not an in-game measurement.

## Point allocation

### Balance (9)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Genesis** | 5/5 | **NEW** | Increases the periodic damage and healing done by your spells and abilities by 10%. |
| **Nature's Majesty** | 2/2 | **NEW** | Increases your critical strike chance with spells and melee attacks by 4%. |
| **Nature's Reach** | 2/2 | changed | Increases the range of your offensive Balance spells by 20% and improves your chance to hit by 4%. |

### Feral Combat (32)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Ferocity** | 5/5 | changed | Reduces the cost of your Maul, Primal Bite, Swipe, Claw, and Rake abilities by 5 Rage or Energy. |
| **Feral Swiftness** | 2/2 | **NEW** | Increases your movement speed while in Cat Form by 30%, and increases your chance to Dodge by 4%. |
| **Feral Instinct** | 3/3 | changed | Increases damage done by your Swipe ability by 30% and reduces the chance enemies have to detect you while Prowling as if you were 3 levels higher. |
| **Thick Hide** | 3/3 | changed | While in Bear Form, Cat Form, Dire Bear Form, or Moonkin Form, you gain 3 additional base Armor per level and another 2.00 base Armor for each point of defense skill beyond five times your level. This amount can be further increased by multipliers from those forms. |
| **Savage Fury** | 2/2 | changed | Increases the damage caused by your Claw, Rake, Shred, Maul, and Swipe abilities by 10%. |
| **Feral Charge** | 1/1 | changed | Charge an enemy, immobilizing them and interrupting any spell they are casting for 4 sec.  Feral Charge (Cat): 8-25 yd range, Instant, 30 sec cooldown, Requires Cat Form. Leap behind an enemy. |
| **Sharpened Claws** | 2/2 | changed | Increases your critical strike chance while in Bear Form, Dire Bear Form, or Cat Form by 6%. |
| **Predatory Strikes** | 3/3 | changed | Increases your melee Attack Power in Cat Form, Bear Form, and Dire Bear Form by 150% of your level. |
| **Lacerate** | 1/1 | **NEW** | Lacerates the enemy target, making them bleed for 20 damage over 15 sec plus 10% weapon damage per existing application of Lacerate on the target. Causes a high amount of threat. This effect stacks up to 5 times on the same target. |
| **Blood Frenzy** | 1/2 | changed | Gives you a 50% chance to gain an additional 5 Rage any time you get a critical strike while in Bear Form or Dire Bear Form. In addition, your non-periodic critical strikes from Cat Form abilities that generate Combo Points have a 50% chance to add an additional Combo Point. |
| **Leader of the Pack** | 1/1 | changed | While in Cat Form, Bear Form, or Dire Bear Form, the Leader of the Pack increases the Critical Strike chance of all party or raid members within 45 yards by 3%. |
| **Natural Instinct** | 2/2 | **NEW** | Increases the critical strike damage bonus of your melee abilities by 20% and increases your spell healing by 25% of your Intellect. |
| **Rend and Tear** | 5/5 | **NEW** | Increases damage done by your melee abilities on Bleeding targets by 15%. |
| **Primal Bite** | 1/1 | **NEW** | Bite the target, dealing 100% normal damage plus 42 and generating a high amount of threat. |

### Restoration (10)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Heart of the Wild** | 5/5 | changed | Increases your Intellect by 10%. In addition, while in Bear Form or Dire Bear Form your Stamina is increased by 20% and while in Cat Form your Strength is increased by 10%. |
| **Naturalist** | 5/5 | **NEW** | Reduces the cast time of your Healing Touch and Wild Growth spells by 0.5 sec and increases all damage you deal by 10%. |

## Rank among our builds and the community simulator's

**1 of 6** for `feral-bear-tank` by tank value in the community simulator (wowsims/forever 2e6e77d (client 70938)); full ranking and the other builds' rotations: [raid README](../README.md), [raid rotations](../rotation.md).

| Rank | Build | By | Split | Tank value | vs best | Threat/s | Damage taken/s |
|---|---|---|---|---|---|---|---|
| 1 | **[`feral-combat-bear-preset-tank`](feral-combat-bear-preset-tank.md)** | ours: derived (simulator preset) | 9/32/10 | 1.880 | +0.0% | 2791 | 438 |
| 2 | *Bear* | community simulator | - | 1.880 | +0.0% | 2791 | 438 |
| 3 | *Hybrid* | community simulator | - | 1.825 | -2.9% | 2680 | 437 |
| 4 | [`opt-feral-bear-tank-raid-tank`](opt-feral-bear-tank-raid-tank.md) | ours: optimizer | 9/37/5 | 1.329 | -29.3% | 1600 | 395 |
| 5 | [`feral-combat-ml-tank`](feral-combat-ml-tank.md) | ours: derived (ML search) | 9/35/7 | 1.009 | -46.3% | 1007 | 410 |
| 6 | [`feral-bear-tank`](feral-bear-tank.md) | ours: hand draft | 7/35/9 | 1.000 | -46.8% | 988 | 410 |

## Rotation (community simulator, raid setting)

- **A fully buffed raid:** our tuned rotation (`raidsim/apl_opt.py`, 2026-09-28, 14 passes, the last 2026-11-22, 9 changes to the base rotation; third-seed check: opt-feral-bear-tank-raid-tank 364 -> 364 DPS (-0.0%), sim preset: Bear 564 -> 561 DPS (-0.4%), feral-bear-tank 257 -> 257 DPS (+0.0%), feral-combat-ml-tank 263 -> 263 DPS (+0.0%)):
  1. threshold 25 -> 50: if rage ≥ 25: cast Maul (+0.9%, pass 1)
  2. move down below 'if (stacks of Lacerate < 5 or time left on Lacerate ≤ 4.5s): cast Lacerate': cast Primal Bite (+0.6%, pass 1)
  3. insert before the filler: cast Barkskin (+2.2%, pass 3)
  4. only with 20s or more of the fight left: cast Lacerate (+1.2%, pass 11)
  5. drop the condition: if rage ≥ 50: cast Maul (+6.6%, pass 12)
  6. drop: cast Primal Bite (+2.2%, pass 12)
  7. insert before the filler: if rage < 20: cast Enrage (+1.2%, pass 12)
  8. drop 'stacks of Lacerate < 5' from the condition: if (stacks of Lacerate < 5 or time left on Lacerate ≤ 4.5s): cast Lacerate (+0.3%, pass 12)
  9. drop: if unitDistance > 5: move to 5 yd (+0.3%, pass 14)

Before the pull: at -10s: if Furor is taken and rage < 10: cast Dire Bear Form; at -10s: cast Enrage; at -33s: if Manual Crowd Pummeler is known: swap to the Swap1 item set; at -0.01s: if not activeItemSwapSet: swap to the Main item set; at -250ms: if number of targets = 3 and rage ≥ current cost: cast Maul.

| # | Priority (the first line whose condition holds is cast) | [`feral-combat-bear-preset-tank`](feral-combat-bear-preset-tank.md) casts/min |
|---|---|---|
| 1 | if unitDistance > 5: wait until not (unitDistance > 5) | as ready |
| 2 | if unitDistance ≤ 5: cast Manual Crowd Pummeler | as ready |
| 3 | if health % ≤ “Barkskin health threshold”: cast Barkskin | 1.0 |
| 4 | if Goblin Sapper Charge is known: cast Goblin Sapper Charge | as ready |
| 5 | if DefensivePotion is known: cast DefensivePotion | as ready |
| 6 | if “Offensive potion is useful without a defensive potion”: cast OffensivePotion | as ready |
| 7 | if selectedConjured and health % ≤ “Healthstone health threshold”: cast Major Healthstone on self | as ready |
| 8 | if health % < “Frenzied Regeneration health threshold”: cast Frenzied Regeneration | 0.3 |
| 9 | if “Enrage can rescue the next attack”: cast Enrage | 0.9 |
| 10 | if “Ready to return to the main weapon”: swap to the Main item set | as ready |
| 11 | if number of targets = 2 and not druidBleedIsActive and not Lacerate is on the target: cast Lacerate on currenttarget | 26.9 |
| 12 | if number of targets = 2 and “Enough rage to queue Maul in cleave”: cast Maul | 19.9 |
| 13 | if number of targets = 2 and Primal Bite is known: cast Primal Bite (rank 3) | 9.8 |
| 14 | if number of targets = 3 and “Enough rage to queue Maul for three-target Swipe”: cast Maul | 19.9 |
| 15 | if number of targets = 3 and not druidBleedIsActive and not Lacerate is on the target: cast Lacerate on currenttarget | 26.9 |
| 16 | if number of targets = 3 and Primal Bite is known: cast Primal Bite (rank 3) | 9.8 |
| 17 | if not (number of targets = 3) and not (number of targets = 2) and “Five-stack Lacerate is near expiry”: cast Lacerate | 26.9 |
| 18 | if not (number of targets = 3) and not (number of targets = 2) and Primal Bite is known: cast Primal Bite (rank 3) | 9.8 |
| 19 | if not (number of targets = 3) and not (number of targets = 2): cast Lacerate | 26.9 |
| 20 | if not (number of targets = 3) and not (number of targets = 2) and “Enough rage to queue Maul”: cast Maul | 19.9 |

Lines of the simulator's rotation these builds never cast: cast Feral Charge (Bear), cast Elune's Light, cast Faerie Fire, cast Demoralizing Roar, cast Swipe (its condition never held in these fights).

Damage by ability (threat for tanks):

| Ability | [`feral-combat-bear-preset-tank`](feral-combat-bear-preset-tank.md) |
|---|---|
| Lacerate | 39% |
| Maul | 30% |
| Primal Bite | 20% |
| Windfury Totem | 5% |
| Auto Attack | 2% |
| Frenzied Regeneration | 2% |
| Judgement of Light | 1% |
| Retribution Aura | 0% |
| Thorns | 0% |
| OtherActionRageGain | 0% |

## Notes

- 2026-11-22: the simulator's build, the bear's pick by "simulator build first" (the audit session's ruling the same day); the tank lane's parity race: upstream's rotation and ours level on it (1.8832 against 1.8825).

## Open questions (verify in the live game)

- Lacerate's stacking threat and Primal Bite in Forever: check the bear's threat against these numbers at launch.

## Sources

- <https://github.com/wowsims/forever (ui/druid/feralbear/presets.ts: Bear)>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
