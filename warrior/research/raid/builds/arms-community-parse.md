# Arms — Full raid (the community's #2 Arms build) — 37/14/0

*[Warrior](../../../README.md) · [Raids: training dummy, raid and parse](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 37/14/0 (Arms / Fury / Protection) |
| **Role** | DPS — Raid |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70009 (2026-09-25 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

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
| **Bloodthrill** | 5/5 | **NEW** | Your Main Hand melee attacks against enemies afflicted by your Rend have a 20% chance to allow the use of your Overpower ability on the target. Lasts 6 sec. |
| **Sweeping Strikes** | 1/1 | unchanged | Your next 5 melee attacks strike an additional nearby opponent. |
| **Weaponmaster** | 5/5 | **NEW** | Gives your melee weapon attacks a benefit depending on the weapon.   Axe/Polearm: Increases your  critical strike chance by 5%.   Mace/Staff: Your attacks ignore  15% of your target's armor.   Sword: Your successful melee   attacks have a 5% chance to   trigger an extra attack on the   target. |
| **Improved Slam** | 2/2 | changed | Reduces the global cooldown and cast time of your Slam ability by 0.50 sec. In addition, Slam no longer interrupts or delays your melee swing and Slam's cooldown is reduced by 3 sec. |
| **Mortal Strike** | 1/1 | unchanged | A vicious strike that deals weapon damage plus 85 and wounds the target, reducing the effectiveness of any healing by 50% for 10 sec. |

### Fury (14)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Cruelty** | 5/5 | changed | Improves your chance to get a critical strike with melee attacks by 5%. |
| **Unbridled Wrath** | 5/5 | changed | Gives you a 60% chance to generate 1 additional Rage when you deal melee damage with a weapon. This effect is increased to 2 Rage for two-handed weapons. |
| **Piercing Howl** | 1/1 | changed | Causes all nearby enemies to be Dazed, reducing movement speed by 50% for 6 sec. |
| **Boundless Rage** | 3/3 | **NEW** | Increases your maximum Rage by 30. |

### Protection (0)

*No points.*

## Rank among our builds and the community simulator's

**2 of 3** for `arms-battle-raid` by training-dummy DPS in the community simulator (ElliotWood/Forever 40be98e); full ranking and the other builds' rotations: [raid README](../README.md), [raid rotations](../rotation.md).

| Rank | Build | By | Split | Dummy DPS | vs best | Raid DPS | vs best in a raid | Out of mana on the dummy |
|---|---|---|---|---|---|---|---|---|
| 1 | [`arms-battle-raid`](arms-battle-raid.md) | ours: hand draft | 34/17/0 | 378 | +0.0% | 729 | -7.3% | 0 s |
| 2 | **[`arms-community-parse`](arms-community-parse.md)** | ours: parse build | 37/14/0 | 375 | -0.6% | 786 | +0.0% | 0 s |
| 3 | *Arms 39/12/0* | community simulator | - | 369 | -2.2% | 774 | -1.6% | 0 s |

## Rotation (community simulator, training dummy)

- **The training dummy:** our tuned rotation (`raidsim/apl_opt.py`, 2026-09-29, 7 changes to the base rotation; third-seed check: arms-battle-raid 210 -> 236 DPS (+12.7%), sim preset: Arms 39/12/0 198 -> 227 DPS (+15.0%)):
  1. insert before the filler: if not Berserker Stance is up: cast Berserker Stance (+6.0%)
  2. insert at the end: cast Sunder Armor (+3.4%)
  3. drop: cast Whirlwind (+1.5%)
  4. move to the top: cast Overpower (+0.8%)
  5. drop: cast Spearing Strike (+0.8%)
  6. threshold 25.5s -> 24.5s: if (time left in the fight ≤ 25.5s or time left in the fight ≥ 140s): use every other cooldown when ready (+0.4%)
  7. insert before the filler: cast Spearing Strike (+0.3%)
- **A fully buffed raid:** our tuned rotation (`raidsim/apl_opt.py`, 2026-09-29, 8 changes to the base rotation; third-seed check: arms-battle-raid 460 -> 487 DPS (+5.8%), sim preset: Arms 39/12/0 454 -> 476 DPS (+4.9%)):
  1. move to the top: cast Overpower (+2.0%)
  2. drop: if (time left in the fight ≤ 30s or time left in the fight ≥ 140s): use every other cooldown when ready (+1.2%)
  3. drop 'time until Whirlwind is ready > 1.5s' from the condition: if time until Bloodthirst is ready > 1.5s and time until Whirlwind is ready > 1.5s and rage > 80: cast Hamstring (+0.4%)
  4. insert before the filler: cast Mocking Blow (+0.2%)
  5. move to the top: cast Slam (+0.3%)
  6. threshold 80 -> 40: if time until Bloodthirst is ready > 1.5s and rage > 80: cast Hamstring (+0.5%)
  7. move down below 'cast Overpower': cast Slam (+0.4%)
  8. move down below 'if not Rend is on the target: cast Rend': cast Mortal Strike (+0.3%)

Before the pull: at -1s: cast Battle Stance.

| # | Priority (the first line whose condition holds is cast) | [`arms-community-parse`](arms-community-parse.md) casts/min |
|---|---|---|
| 1 | cast Overpower | 6.2 |
| 2 | if execute phase (E20): cast Execute | 3.4 |
| 3 | cast Goblin Sapper Charge | as ready |
| 4 | cast Dense Dynamite | as ready |
| 5 | if (time left in the fight ≤ 20s or time left in the fight ≥ 140s): cast Potion | as ready |
| 6 | if (time left in the fight ≤ 30s or time left in the fight ≥ 130s): cast Earthstrike | as ready |
| 7 | if (time left in the fight ≤ 30s or time left in the fight ≥ 130s): cast Slayer's Crest | as ready |
| 8 | if (time left in the fight ≤ 30s or time left in the fight ≥ 130s): cast Slayer's Crest | as ready |
| 9 | if (time left in the fight ≤ 24.5s or time left in the fight ≥ 140s): use every other cooldown when ready | as ready |
| 10 | cast Mortal Strike | 0.6 |
| 11 | if not Rend is on the target: cast Rend | 2.7 |
| 12 | cast Slam | 2.8 |
| 13 | if not Battle Shout is up: cast Battle Shout | 0.3 |
| 14 | if stacks of Sunder Armor < 5: cast Sunder Armor | 8.2 |
| 15 | if not Berserker Stance is up: cast Berserker Stance | 25.1 |
| 16 | if not Battle Stance is up: cast Battle Stance | 25.3 |
| 17 | cast Spearing Strike | 1.8 |
| 18 | cast Sunder Armor | 8.2 |

Lines of the simulator's rotation these builds never cast: cast Death Wish (needs the Death Wish talent); cast Blood Fury, cast Diamond Flask, cast Jom Gabbar, cast Whirlwind, cast Cleave, cast Hamstring (its condition never held in these fights); cast Bloodthirst (needs the Bloodthirst talent).

Damage by ability:

| Ability | [`arms-community-parse`](arms-community-parse.md) |
|---|---|
| Auto Attack | 43% |
| Overpower | 26% |
| Execute | 10% |
| Slam | 9% |
| Deep Wound | 5% |
| Rend | 3% |
| Mortal Strike | 2% |
| Spearing Strike | 2% |
| Dragonbreath Chili | 0% |

## Notes

- 2026-09-30: found by the popular-builds race (popular_race.py) and confirmed by a full-raid talent search (raidsim/talent_opt.py --setting raid --min-tree Arms=30) and a head-to-head race. Simulator numbers are the community's model of the beta.

## Open questions (verify in the live game)

- Why does our dummy-picked Arms build lose 14% in a full raid? The talents that pay off on a buffed, debuffed target should be fitted into the raid-mode model.

## Sources

- <https://talentsforever.com/warrior/60/30305213132515201-05050103--4>
- <https://talentsforever.com/popular.js>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
