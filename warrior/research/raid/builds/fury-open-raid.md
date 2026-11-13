# Fury — Raid (open talent search) — 20/31/0

*[Warrior](../../../README.md) · [Raids: training dummy, raid and parse](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 20/31/0 (Arms / Fury / Protection) |
| **Role** | DPS — Raid |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70753 (2026-11-03 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

The Fury raid build the open talent search found on 2026-11-08: every legal 51-point build with no tree rule, searched in the community simulator's arms-2h-raid rotation in a full raid (every raid buff and debuff: the group setting; raidsim/family_search.py: every pair of keystones polished by a short hill climb first, then the machine-learning search, the winner raced against the rotation's builds over 30,000 fights). +1.0% over opt-arms-2h-raid-raid-dps, the best of our builds in that rotation.

## Point allocation

### Arms (20)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Improved Heroic Strike** | 3/3 | changed | Reduces the cost of your Heroic Strike ability by 3 Rage. |
| **Deflection** | 2/5 | unchanged | Increases your Parry chance by 2%. |
| **Improved Rend** | 3/3 | changed | Increases the Bleed damage done by your Rend ability by 35%. |
| **Improved Tactical Mastery** | 3/3 | **NEW** | Tactical Mastery lets you retain up to an additional 15 Rage when you change stances. |
| **Anger Management** | 1/1 | changed | Generates 1 Rage every 3 sec while in combat, and reduces Rage loss while out of combat by 30%. |
| **Deep Wounds** | 3/3 | changed | Your critical strikes cause your opponent to Bleed, dealing 60% of your melee weapon's average damage over 12 sec. |
| **Two-Handed Weapon Specialization** | 3/3 | changed | Increases the damage you deal with two-handed melee weapons by 6%. |
| **Impale** | 2/2 | changed | Increases the critical strike damage bonus of your abilities by 20%. |

### Fury (31)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Cruelty** | 5/5 | changed | Improves your chance to get a critical strike with melee attacks by 5%. |
| **Unbridled Wrath** | 5/5 | changed | Gives you a 60% chance to generate 1 additional Rage when you deal melee damage with a weapon. |
| **Furious Precision** | 3/3 | changed | Increases your chance to hit with off-hand attacks by 10%. |
| **Blood Craze** | 3/3 | changed | Regenerates 3% of your total Health over 6 sec after being the victim of a critical strike or suffering more than 20% of your maximum Health from a single attack. |
| **Enrage** | 1/5 | changed | Gives you a 30% chance to deal 2% increased Physical damage for 12 sec after being the victim of any damaging attack. |
| **Reckless Swings** | 1/1 | **NEW** | Your next 4 melee attacks generate 5 additional Rage. Lasts 8 seconds. |
| **Improved Execute** | 2/2 | changed | Reduces the Rage cost of your Execute ability by 5. |
| **Improved Berserker Rage** | 2/2 | changed | Your Berserker Rage ability will instantly generate 10 Rage and has a 100% chance to remove all movement impairing effects when activated. |
| **Death Wish** | 1/1 | changed | When activated, increases your Physical damage done by 20% and makes you immune to Fear effects, but increases all damage you take by 5%. Lasts 30 sec. |
| **Gore Drinker** | 2/2 | **NEW** | Your Enrage, Berserker Rage, Bloodrage, Death Wish, and Bloodthirst abilities cause your next 3 melee attacks to restore 1.0% of your maximum Health. |
| **Improved Whirlwind** | 2/2 | **NEW** | Reduces the cooldown of your Whirlwind ability by 2 seconds and increases the damage it deals to the closest enemy by 30%. |
| **Flurry** | 3/3 | changed | Increases your melee attack speed by 30% for your next 3 swings after dealing a melee critical strike. |
| **Bloodthirst** | 1/1 | changed | Instantly attack the target causing damage equal to 45% of your Attack Power plus 30 and increasing your movement speed by 10% for 10 sec. |

### Protection (0)

*No points.*

## Core talents (priority order)

1. **Flurry** — 136 DPS lost without it (15% of the build in a full raid; removal, 12,000 fights).
2. **Bloodthirst** — 90 DPS lost without it (10% of the build in a full raid; removal, 12,000 fights).
3. **Deep Wounds** — 70 DPS lost without it (8% of the build in a full raid; removal, 12,000 fights).
4. **Two-Handed Weapon Specialization** — 51 DPS lost without it (6% of the build in a full raid; removal, 12,000 fights).
5. **Cruelty** — 46 DPS lost without it (5% of the build in a full raid; removal, 12,000 fights).
6. **Death Wish** — 39 DPS lost without it (4% of the build in a full raid; removal, 12,000 fights).
7. **Improved Whirlwind** — 33 DPS lost without it (4% of the build in a full raid; removal, 12,000 fights).
8. **Impale** — 28 DPS lost without it (3% of the build in a full raid; removal, 12,000 fights).

## Rank among our builds and the community simulator's

**2 of 5** for `arms-2h-raid` by training-dummy DPS in the community simulator (wowsims/forever ff9babb (client 70888)); full ranking and the other builds' rotations: [raid README](../README.md), [raid rotations](../rotation.md).

| Rank | Build | By | Split | Dummy DPS | vs best | Raid DPS | vs best in a raid | Out of mana on the dummy |
|---|---|---|---|---|---|---|---|---|
| 1 | [`opt-arms-2h-raid-raid-dps`](opt-arms-2h-raid-raid-dps.md) | ours: optimizer | 20/31/0 | 420 | +0.0% | 845 | -1.2% | 0 s |
| 2 | **[`fury-open-raid`](fury-open-raid.md)** | ours: derived (open search) | 20/31/0 | 419 | -0.1% | 856 | +0.0% | 0 s |
| 3 | [`arms-2h-raid`](arms-2h-raid.md) | ours: hand draft | 19/32/0 | 407 | -3.0% | 833 | -2.7% | 0 s |
| 4 | *Fury* | community simulator | - | 398 | -5.3% | 811 | -5.2% | 0 s |
| 5 | *Arms* | community simulator | - | 334 | -20.3% | 703 | -17.8% | 0 s |

## Rotation (community simulator, training dummy)

- **The training dummy:** our tuned rotation (`raidsim/apl_opt.py`, 2026-09-28, 6 passes, the last 2026-10-08, 18 changes to the base rotation; third-seed check: open winner 302 -> 367 DPS (+21.3%), opt-arms-2h-raid-raid-dps 299 -> 372 DPS (+24.5%), sim preset: DPS 280 -> 341 DPS (+22.0%), arms-2h-raid 296 -> 357 DPS (+20.7%)):
  1. drop: if false: cast Recklessness (+16.4%, pass 1)
  2. insert before the filler: if stacks of Sunder Armor < 5: cast Sunder Armor (+5.8%, pass 1)
  3. drop: if rage < 90: cast Bloodrage (+1.7%, pass 1)
  4. drop the condition: if time until Bloodthirst is ready > 1.5s: cast Whirlwind (+3.2%, pass 1)
  5. drop: if stacks of Sunder Armor < 1 and not Expose Armor is up: cast Sunder Armor (+2.2%, pass 1)
  6. threshold 30s -> 22.5s: if (time left in the fight ≤ 30s or time left in the fight ≥ 140s): use every other cooldown when ready (+1.3%, pass 1)
  7. drop: if number of targets = 1 and (rage ≥ 40 or execute phase (E20)): cast Heroic Strike (+0.9%, pass 1)
  8. move to the top: if execute phase (E20): cast Execute (+0.4%, pass 1)
  9. threshold 22.5s -> 23.5s: if (time left in the fight ≤ 22.5s or time left in the fight ≥ 140s): use every other cooldown when ready (+0.3%, pass 1)
  10. threshold 23.5s -> 24.5s: if (time left in the fight ≤ 23.5s or time left in the fight ≥ 140s): use every other cooldown when ready (+0.9%, pass 1)
  11. threshold 24.5s -> 25.5s: if (time left in the fight ≤ 24.5s or time left in the fight ≥ 140s): use every other cooldown when ready (+0.5%, pass 1)
  12. show the hidden: if time until Bloodthirst is ready > 1.5s and time until Whirlwind is ready > 1.5s: cast Berserker Rage (+0.8%, pass 5)
  13. threshold 140s -> 70s: if (time left in the fight ≤ 25.5s or time left in the fight ≥ 140s): use every other cooldown when ready (+0.7%, pass 5)
  14. drop the condition: if number of targets > 1: cast Whirlwind (+0.2%, pass 5)
  15. drop the condition: if time until Bloodthirst is ready > 1.5s and time until Whirlwind is ready > 1.5s: cast Berserker Rage (+0.4%, pass 5)
  16. move to the top: if not Battle Shout is up: cast Battle Shout + move to the top: cast Berserker Rage (+0.5%, pass 5)
  17. insert in the middle: if stacks of Sunder Armor < 1 and not Expose Armor is up: cast Sunder Armor + threshold 1 -> 3: if stacks of Sunder Armor < 1 and not Expose Armor is up: cast Sunder Armor (+2.0%, pass 5)
  18. threshold 3 -> 4: if stacks of Sunder Armor < 3 and not Expose Armor is up: cast Sunder Armor (+0.5%, pass 5)
- **A fully buffed raid:** our tuned rotation (`raidsim/apl_opt.py`, 2026-09-28, 12 passes, the last 2026-11-08, 17 changes to the base rotation; third-seed check: open winner 685 -> 911 DPS (+32.9%), opt-arms-2h-raid-raid-dps 680 -> 902 DPS (+32.7%), sim preset: Fury 648 -> 862 DPS (+33.0%), arms-2h-raid 668 -> 888 DPS (+32.9%)):
  1. drop: if false: cast Recklessness (+12.7%, pass 1)
  2. drop: if number of targets = 1 and (rage ≥ 40 or execute phase (E20)): cast Heroic Strike (+5.3%, pass 1)
  3. drop: if not Battle Shout is up: cast Battle Shout (+1.0%, pass 1)
  4. drop the condition: if time until Bloodthirst is ready > 1.5s: cast Whirlwind (+0.4%, pass 1)
  5. drop the condition: if time until Bloodthirst is ready > 1.5s and time until Whirlwind is ready > 1.5s and rage > 80: cast Hamstring (+6.8%, pass 5)
  6. drop 'time left in the fight ≥ 140s' from the condition: if (time left in the fight ≤ 30s or time left in the fight ≥ 140s): use every other cooldown when ready (+1.0%, pass 5)
  7. threshold 30s -> 45s: if (time left in the fight ≤ 30s or time left in the fight ≥ 211.5s): cast Death Wish (+0.7%, pass 5)
  8. threshold 30s -> 45s: if time left in the fight ≤ 30s: use every other cooldown when ready (+0.3%, pass 5)
  9. move to the top: cast Bloodthirst (+0.3%, pass 5)
  10. insert before the filler: cast Mighty Rage Potion (+0.5%, pass 7)
  11. insert at the top: if time until Bloodthirst is ready > 1.5s: cast Whirlwind (+0.2%, pass 7)
  12. threshold 45s -> 33.75s: if time left in the fight ≤ 45s: use every other cooldown when ready (+0.2%, pass 7)
  13. insert before the filler: if time until Bloodthirst is ready ≥ 1.5s and time until Whirlwind is ready ≥ 1.5s and (Improved Berserker Rage is known or Improved Berserker Rage is known): cast Berserker Rage (+0.4%, pass 8)
  14. insert in the middle: if not execute phase (E20) and rage ≥ 90 and not talentIsKnown: cast Heroic Strike (+0.2%, pass 9)
  15. insert before the filler: cast Reckless Swings (+0.5%, pass 10)
  16. insert at the top: if execute phase (E20): cast Recklessness (+0.2%, pass 11)
  17. move down below 'cast Mighty Rage Potion': if rage < 90: cast Bloodrage (+0.2%, pass 11)

| # | Priority (the first line whose condition holds is cast) | [`fury-open-raid`](fury-open-raid.md) casts/min |
|---|---|---|
| 1 | cast Berserker Rage | 2.0 |
| 2 | if not Battle Shout is up: cast Battle Shout | 0.3 |
| 3 | if execute phase (E20): cast Execute | 5.2 |
| 4 | cast Goblin Sapper Charge | as ready |
| 5 | cast Dense Dynamite | as ready |
| 6 | if (time left in the fight ≤ 30s or time left in the fight ≥ 211.5s): cast Death Wish | 0.3 |
| 7 | if (time left in the fight ≤ 20s or time left in the fight ≥ 140s): cast Potion | as ready |
| 8 | if (time left in the fight ≤ 30s or time left in the fight ≥ 130s): cast Earthstrike | as ready |
| 9 | if (time left in the fight ≤ 30s or time left in the fight ≥ 130s): cast Slayer's Crest | as ready |
| 10 | if stacks of Sunder Armor < 4 and not Expose Armor is up: cast Sunder Armor | 7.2 |
| 11 | if (time left in the fight ≤ 30s or time left in the fight ≥ 130s): cast Slayer's Crest | as ready |
| 12 | if (time left in the fight ≤ 25.5s or time left in the fight ≥ 70s): use every other cooldown when ready | as ready |
| 13 | cast Whirlwind | 4.8 |
| 14 | cast Bloodthirst | 5.5 |
| 15 | cast Death Wish | 0.3 |
| 16 | cast Whirlwind | 4.8 |
| 17 | if time until Bloodthirst is ready > 1.5s and time until Whirlwind is ready > 1.5s and rage > 80: cast Hamstring | 1.3 |
| 18 | if stacks of Sunder Armor < 5: cast Sunder Armor | 7.2 |

Lines of the simulator's rotation these builds never cast: cast Blood Fury, cast Diamond Flask, cast Jom Gabbar, cast Cleave, cast Berserker Stance (its condition never held in these fights); cast Mortal Strike (needs the Mortal Strike talent); cast Spearing Strike (needs the Spearing Strike talent).

Damage by ability:

| Ability | [`fury-open-raid`](fury-open-raid.md) |
|---|---|
| Auto Attack | 44% |
| Bloodthirst | 17% |
| Execute | 17% |
| Whirlwind | 15% |
| Deep Wound | 7% |
| Hamstring | 0% |

## Notes

- +2.5% over the best hand draft of the spec, arms-2h-raid, over the replacement bar: this build is the spec's raid pick, the hand draft stays as the alternative.
- Open search result (arms-2h-raid, full raid): 20/31/0 (Fury) at 910.3 DPS; opt-arms-2h-raid-raid-dps 901.2, arms-2h-raid 887.8 in the same fights; 2,133 builds simulated, 1 independent runs reached the top.
- The spec's other builds on the pages (their best entry, full raid): opt-fury-dw-raid-raid-dps 856.5, fury-dw-raid 817.2.
- The arms-2h-raid raid rotation was re-tuned on this build (a pass in its rotation-search record); the numbers use it.
- Sibling rotations tried on it (10,000 fights): fury-dw-raid -2.2%, arms-battle-raid -16.9%; none adopted.
- Talents the simulator measures at 0 DPS in this build (tier fillers; the filler audit may move them): Deflection, Improved Rend, Improved Tactical Mastery, Furious Precision, Blood Craze, Enrage, Improved Berserker Rage, Gore Drinker.
- Simulator numbers are the community's model of the beta (wowsims/forever 16e8542 (client 70790) with this project's patches), not in-game measurements.
- 2026-11-08 filler audit (raidsim/filler_audit.py, user question on zero-value fillers): points the simulator measures at 0 moved, one at a time, to talents that help in a real raid (interrupt protection, threat, mana, range, survival; the simulator cannot see these, so the order is our judgment) or that gain DPS: Enrage -> Gore Drinker (survival). Net +0.00% on a third seed.

## Open questions (verify in the live game)

- An open-search Fury build: check it against the community's Fury builds at launch.

## Sources

- <https://github.com/ElliotWood/Forever>
- <https://talentsforever.com/warrior/60/32303013032-050530320122110231--12>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
