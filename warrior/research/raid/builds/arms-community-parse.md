# Arms — Full raid (the community's #2 Arms build) — 37/14/0

*[Warrior](../../../README.md) · [Raids: training dummy, raid and parse](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 37/14/0 (Arms / Fury / Protection) |
| **Role** | DPS — Raid |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70707 (2026-10-16 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

Arms for a full raid: talentsforever.com's #2 most popular Arms build (37/14/0, 2026-09-30 snapshot). In the community simulator's full-raid setting (every raid buff and debuff, the equal-tier phase-1 gear) it does 13.9% more than our best Arms build (704 vs 618 DPS, 20,000 iterations, seed 3); on the training dummy it ties it (-0.9%). A talent search from it found no better build.

## Point allocation

### Arms (37)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Improved Heroic Strike** | 3/3 | changed | Reduces the cost of your Heroic Strike ability by 3 Rage. |
| **Improved Rend** | 3/3 | changed | Increases the Bleed damage done by your Rend ability by 35%. |
| **Improved Tactical Mastery** | 5/5 | **NEW** | Tactical Mastery lets you retain up to an additional 15 Rage when you change stances. |
| **Improved Overpower** | 2/2 | moved | Increases the critical strike chance of your Overpower ability by 50%. |
| **Anger Management** | 1/1 | changed | Generates 1 Rage every 3 sec while in combat, and reduces Rage loss while out of combat by 30%. |
| **Deep Wounds** | 3/3 | changed | Your critical strikes cause your opponent to Bleed, dealing 60% of your melee weapon's average damage over 12 sec. |
| **Spearing Strike** | 1/1 | **NEW** | A brutal attack that deals 40% weapon damage. Deals an additional 80% weapon damage against Giants, Dragonkin, and mounted targets. Mounted targets are dismounted. |
| **Two-Handed Weapon Specialization** | 3/3 | changed | Increases the damage you deal with two-handed melee weapons by 3%. |
| **Impale** | 2/2 | changed | Increases the critical strike damage bonus of your abilities by 20%. |
| **Bloodthrill** | 5/5 | **NEW** | Grants your Main Hand melee attacks against enemies afflicted by your Rend a 20% chance to allow an activation of Overpower. |
| **Sweeping Strikes** | 1/1 | unchanged | Your next 5 melee attacks strike an additional nearby opponent. |
| **Weaponmaster** | 5/5 | **NEW** | Gives your melee weapon attacks a benefit depending on the weapon.   Axe/Polearm: Increases your  critical strike chance by 5%.   Mace/Staff: Your attacks ignore  15% of your target's armor.   Sword: Your successful melee   attacks have a 5% chance to   trigger an extra attack on the   target. |
| **Improved Slam** | 2/2 | changed | Reduces the global cooldown and cast time of your Slam ability by 0.50 sec. In addition, Slam no longer interrupts or delays your melee swing and Slam's cooldown is reduced by 3.0 sec. |
| **Mortal Strike** | 1/1 | unchanged | A vicious strike that deals weapon damage plus 85 and wounds the target, reducing the effectiveness of any healing by 50% for 10 sec. |

### Fury (14)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Booming Voice** | 3/5 | changed | Increases the area of effect of your Shouts by 30% and reduces their Rage cost by 15%. |
| **Cruelty** | 5/5 | changed | Improves your chance to get a critical strike with melee attacks by 5%. |
| **Unbridled Wrath** | 5/5 | changed | Gives you a 60% chance to generate 1 additional Rage when you deal melee damage with a weapon. |
| **Piercing Howl** | 1/1 | changed | Causes all enemies within 10 yds to be Dazed, reducing movement speed by 50% for 6 sec. |

### Protection (0)

*No points.*

## Rank among our builds and the community simulator's

**4 of 4** for `arms-battle-raid` by training-dummy DPS in the community simulator (wowsims/forever 30f67f5 (client 70450)); full ranking and the other builds' rotations: [raid README](../README.md), [raid rotations](../rotation.md).

| Rank | Build | By | Split | Dummy DPS | vs best | Raid DPS | vs best in a raid | Out of mana on the dummy |
|---|---|---|---|---|---|---|---|---|
| 1 | [`arms-battle-raid`](arms-battle-raid.md) | ours: hand draft | 34/17/0 | 372 | +0.0% | 799 | +0.0% | 0 s |
| 2 | [`arms-ml-raid`](arms-ml-raid.md) | ours: derived (ML search) | 39/10/2 | 369 | -0.8% | 797 | -0.2% | 0 s |
| 3 | *Arms* | community simulator | - | 369 | -0.8% | 796 | -0.3% | 0 s |
| 4 | **[`arms-community-parse`](arms-community-parse.md)** | ours: derived (simulator search) | 37/14/0 | 368 | -1.1% | 790 | -1.0% | 0 s |

## Rotation (community simulator, training dummy)

- **The training dummy:** our tuned rotation (`raidsim/apl_opt.py`, 2026-09-29, 2 passes, the last 2026-10-02, 12 changes to the base rotation; third-seed check: ml: Arms 363 -> 404 DPS (+11.3%), sim preset: Arms 39/12/0 353 -> 380 DPS (+7.6%)):
  1. insert before the filler: if not Berserker Stance is up: cast Berserker Stance (+6.0%, pass 1)
  2. insert at the end: cast Sunder Armor (+3.4%, pass 1)
  3. drop: cast Whirlwind (+1.5%, pass 1)
  4. move to the top: cast Overpower (+0.8%, pass 1)
  5. drop: cast Spearing Strike (+0.8%, pass 1)
  6. threshold 25.5s -> 24.5s: if (time left in the fight ≤ 25.5s or time left in the fight ≥ 140s): use every other cooldown when ready (+0.4%, pass 1)
  7. insert before the filler: cast Spearing Strike (+0.3%, pass 1)
  8. drop 'time left in the fight ≥ 140s' from the condition: if (time left in the fight ≤ 24.5s or time left in the fight ≥ 140s): use every other cooldown when ready (+1.9%, pass 2)
  9. insert in the middle: if rage < 90: cast Bloodrage (+0.6%, pass 2)
  10. insert before the filler: if time until Bloodthirst is ready > 1.5s: cast Whirlwind (+0.5%, pass 2)
  11. move to the top: if not Battle Stance is up: cast Battle Stance (+0.2%, pass 2)
  12. threshold 24.5s -> 36.75s: if time left in the fight ≤ 24.5s: use every other cooldown when ready (+0.3%, pass 2)
- **A fully buffed raid:** our tuned rotation (`raidsim/apl_opt.py`, 2026-09-29, 4 passes, the last 2026-10-27, 14 changes to the base rotation; third-seed check: arms-community-parse 719 -> 792 DPS (+10.2%), sim preset: Arms 39/12/0 717 -> 788 DPS (+9.8%), arms-battle-raid 723 -> 796 DPS (+10.1%)):
  1. move to the top: cast Overpower (+2.0%, pass 1)
  2. drop: if (time left in the fight ≤ 30s or time left in the fight ≥ 140s): use every other cooldown when ready (+1.2%, pass 1)
  3. drop 'time until Whirlwind is ready > 1.5s' from the condition: if time until Bloodthirst is ready > 1.5s and time until Whirlwind is ready > 1.5s and rage > 80: cast Hamstring (+0.4%, pass 1)
  4. insert before the filler: cast Mocking Blow (+0.2%, pass 1)
  5. move to the top: cast Slam (+0.3%, pass 1)
  6. threshold 80 -> 40: if time until Bloodthirst is ready > 1.5s and rage > 80: cast Hamstring (+0.5%, pass 1)
  7. move down below 'cast Overpower': cast Slam (+0.4%, pass 1)
  8. move down below 'if not Rend is on the target: cast Rend': cast Mortal Strike (+0.3%, pass 1)
  9. move down below 'if not Rend is on the target: cast Rend': if execute phase (E20): cast Execute (+0.6%, pass 2)
  10. drop the condition: if time until Bloodthirst is ready > 1.5s and rage > 40: cast Hamstring (+0.4%, pass 2)
  11. move down below 'cast Mortal Strike': if execute phase (E20): cast Execute (+0.7%, pass 3)
  12. insert before the filler: cast Mighty Rage Potion (+0.3%, pass 3)
  13. insert before the filler: cast Everlook Pathcarver (+0.4%, pass 4)
  14. only with 6s or more of the fight left: if not Rend is on the target: cast Rend (+0.3%, pass 4)

Before the pull: at -1s: cast Battle Stance.

| # | Priority (the first line whose condition holds is cast) | [`arms-community-parse`](arms-community-parse.md) casts/min |
|---|---|---|
| 1 | if not Battle Stance is up: cast Battle Stance | 26.7 |
| 2 | cast Overpower | 3.4 |
| 3 | if execute phase (E20): cast Execute | 3.7 |
| 4 | cast Goblin Sapper Charge | as ready |
| 5 | cast Dense Dynamite | as ready |
| 6 | if (time left in the fight ≤ 20s or time left in the fight ≥ 140s): cast Potion | as ready |
| 7 | if (time left in the fight ≤ 30s or time left in the fight ≥ 130s): cast Earthstrike | as ready |
| 8 | if (time left in the fight ≤ 30s or time left in the fight ≥ 130s): cast Slayer's Crest | as ready |
| 9 | if (time left in the fight ≤ 30s or time left in the fight ≥ 130s): cast Slayer's Crest | as ready |
| 10 | if time left in the fight ≤ 36.75s: use every other cooldown when ready | as ready |
| 11 | if rage < 90: cast Bloodrage | 1.0 |
| 12 | if number of targets > 1: cast Whirlwind | 1.0 |
| 13 | cast Mortal Strike | 2.4 |
| 14 | if not Rend is on the target: cast Rend | 2.3 |
| 15 | cast Slam | 2.7 |
| 16 | if not Battle Shout is up: cast Battle Shout | 0.3 |
| 17 | if stacks of Sunder Armor < 5: cast Sunder Armor | 5.9 |
| 18 | if not Berserker Stance is up: cast Berserker Stance | 26.5 |
| 19 | cast Spearing Strike | 1.3 |
| 20 | if time until Bloodthirst is ready > 1.5s: cast Whirlwind | 1.0 |
| 21 | cast Sunder Armor | 5.9 |

Lines of the simulator's rotation these builds never cast: cast Death Wish (needs the Death Wish talent); cast Blood Fury, cast Diamond Flask, cast Jom Gabbar, cast Cleave, cast Hamstring (its condition never held in these fights); cast Bloodthirst (needs the Bloodthirst talent).

Damage by ability:

| Ability | [`arms-community-parse`](arms-community-parse.md) |
|---|---|
| Auto Attack | 38% |
| Execute | 16% |
| Overpower | 13% |
| Slam | 8% |
| Mortal Strike | 7% |
| Rend | 7% |
| Deep Wound | 6% |
| Whirlwind | 3% |
| Spearing Strike | 1% |
| item 274759 | 1% |

## Notes

- 2026-09-30: found by the popular-builds race (popular_race.py) and confirmed by a full-raid talent search (raidsim/talent_opt.py --setting raid --min-tree Arms=30) and a head-to-head race. Simulator numbers are the community's model of the beta.
- 2026-10-03: repaired for beta build 1.60.1.70170 (talents removed, renamed or moved): Boundless Rage 3 out; Booming Voice 3 in; to be re-optimized.
- 2026-10-15: the 70291 machine-learning search (ElliotWood/Forever 2ce8265 with this project's patches, ml_pipeline.py --fresh) confirms this build for Arms: its full-raid winner is +0.40% against it, under the 0.5% bar for a new build.

## Open questions (verify in the live game)

- Why does our dummy-picked Arms build lose 14% in a full raid? The talents that pay off on a buffed, debuffed target should be fitted into the raid-mode model.

## Sources

- <https://talentsforever.com/warrior/60/30305213132515201-05050103--4>
- <https://talentsforever.com/popular.js>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
