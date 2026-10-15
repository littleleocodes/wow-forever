# Combat — Swords (open talent search) — 18/33/0

*[Rogue](../../../README.md) · [Raids: training dummy, raid and parse](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 18/33/0 (Assassination / Combat / Subtlety) |
| **Role** | DPS — Raid |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70291 (2026-10-08 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

The Combat raid build the open talent search found on 2026-10-10: every legal 51-point build with no tree rule, searched in the community simulator's combat-swords-raid rotation in a full raid (every raid buff and debuff: the group setting; raidsim/family_search.py: every pair of keystones polished by a short hill climb first, then the machine-learning search, the winner raced against the rotation's builds over 30,000 fights). +1.8% over opt-combat-swords-raid-raid-dps, the best of our builds in that rotation.

## Point allocation

### Assassination (18)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Malice** | 5/5 | changed | Increases your critical strike chance with all attacks and Poisons by 5%. |
| **Ruthlessness** | 3/3 | unchanged | Gives your finishing moves a 60% chance to add a Combo Point to your target. |
| **Improved Slice and Dice** | 3/3 | unchanged | Increases the duration of your Slice and Dice ability by 45%. |
| **Relentless Strikes** | 1/1 | unchanged | Your finishing moves have a 20% chance per Combo Point to restore 25 Energy. |
| **Lethality** | 3/5 | changed | Increases the critical strike damage bonus of your Sinister Strike, Gouge, Backstab, Mutilate, Ghostly Strike, and Hemorrhage abilities by 12%. |
| **Improved Poisons** | 3/5 | changed | Increases the chance to apply Poisons to your target by 6%, and gives Poison applications a 30% chance to not consume a charge. |

### Combat (33)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Improved Eviscerate** | 3/3 | changed | Increases the damage done by your Eviscerate ability by 20%. |
| **Improved Sinister Strike** | 2/2 | unchanged | Reduces the Energy cost of your Sinister Strike ability by 5. |
| **Lightning Reflexes** | 4/5 | unchanged | Increases your Dodge chance by 4%. |
| **Deflection** | 3/3 | changed | Increases your Parry chance by 6%. |
| **Precision** | 3/3 | changed | Improves your chance to hit by 3%. |
| **Flawless Execution** | 1/1 | **NEW** | Reduces the Energy cost of your Eviscerate ability by 10. |
| **Dual Wield Specialization** | 5/5 | changed | Increases the damage done by your off-hand weapon by 25%. |
| **Blade Flurry** | 1/1 | changed | Increases your melee attack speed by 20% and your melee attacks strike an additional nearby opponent. Lasts 15 sec. |
| **Hack and Slash** | 5/5 | **NEW** | Gives your melee weapon attacks a benefit depending on the weapon.   Axe/Sword: Your successful  melee attacks have a 5% chance  to trigger an extra attack on the   target.   Dagger/Fist: Increases your  critical strike chance by 5%.   Mace: Your attacks ignore 15% of  your target's armor. |
| **Weapon Expertise** | 2/2 | changed | Reduces the chance for your attacks to be Dodged or Parried by 2%. |
| **Aggression** | 3/3 | changed | Increases the damage of your Sinister Strike, Backstab, and Eviscerate abilities by 6%. |
| **Adrenaline Rush** | 1/1 | unchanged | Increases your Energy regeneration rate by 100% for 15 sec. |

### Subtlety (0)

*No points.*

## Core talents (priority order)

1. **Relentless Strikes** — 38 DPS lost without it (5% of the build in a full raid; removal, 12,000 fights).
2. **Improved Sinister Strike** — 33 DPS lost without it (5% of the build in a full raid; removal, 12,000 fights).
3. **Malice** — 31 DPS lost without it (4% of the build in a full raid; removal, 12,000 fights).
4. **Improved Slice and Dice** — 25 DPS lost without it (3% of the build in a full raid; removal, 12,000 fights).
5. **Adrenaline Rush** — 25 DPS lost without it (3% of the build in a full raid; removal, 12,000 fights).
6. **Dual Wield Specialization** — 25 DPS lost without it (3% of the build in a full raid; removal, 12,000 fights).
7. **Ruthlessness** — 21 DPS lost without it (3% of the build in a full raid; removal, 12,000 fights).
8. **Precision** — 20 DPS lost without it (3% of the build in a full raid; removal, 12,000 fights).

## Rank among our builds and the community simulator's

**3 of 10** for `combat-swords-raid` by training-dummy DPS in the community simulator (ElliotWood/Forever 2ce8265); full ranking and the other builds' rotations: [raid README](../README.md), [raid rotations](../rotation.md).

| Rank | Build | By | Split | Dummy DPS | vs best | Raid DPS | vs best in a raid | Out of mana on the dummy |
|---|---|---|---|---|---|---|---|---|
| 1 | [`combat-swords-raid`](combat-swords-raid.md) | ours: hand draft | 19/32/0 | 409 | +0.0% | 667 | -1.7% | 0 s |
| 2 | *Improved Expose Armor (SS)* | community simulator | - | 409 | +0.0% | 667 | -1.7% | 0 s |
| 3 | **[`combat-swords-open-raid`](combat-swords-open-raid.md)** | ours: derived (open search) | 18/33/0 | 392 | -4.2% | 679 | +0.0% | 0 s |
| 4 | [`opt-combat-swords-raid-raid-dps`](opt-combat-swords-raid-raid-dps.md) | ours: optimizer | 20/31/0 | 391 | -4.4% | 666 | -2.0% | 0 s |
| 5 | *Sinister Strike* | community simulator | - | 387 | -5.4% | 675 | -0.5% | 0 s |
| 6 | *Combat Dual-Wield 15/33/3* | community simulator | - | 380 | -7.1% | 662 | -2.6% | 0 s |
| 7 | *Assassination Mutilate 31/20/0* | community simulator | - | 356 | -13.1% | 610 | -10.2% | 0 s |
| 8 | *Mutilate* | community simulator | - | 344 | -15.8% | 597 | -12.1% | 0 s |
| 9 | *Backstab* | community simulator | - | 331 | -18.9% | 602 | -11.4% | 0 s |
| 10 | *Subtlety Hemo 15/0/36* | community simulator | - | 315 | -22.9% | 527 | -22.4% | 0 s |

## Rotation (community simulator, training dummy)

- **The training dummy:** our tuned rotation (`raidsim/apl_opt.py`, 2026-09-28, 6 passes, the last 2026-10-10, 9 changes to the base rotation; third-seed check: open winner 353 -> 392 DPS (+11.1%), combat-swords-raid 343 -> 409 DPS (+19.3%), sim preset: Improved Expose Armor (SS) 343 -> 409 DPS (+19.3%), opt-combat-swords-raid-raid-dps 349 -> 391 DPS (+12.0%)):
  1. insert at the top: if time left on Expose Armor < 3 and combo points ≥ 5 and time left in the fight ≥ 3: cast Expose Armor (+9.7%, pass 1)
  2. only with 10s or more of the fight left: if time left on Expose Armor < 3 and combo points ≥ 5 and time left in the fight ≥ 3: cast Expose Armor (+0.3%, pass 1)
  3. only with 20s or more of the fight left: if (combo points ≥ 1 and not Slice and Dice is up and time left in the fight ≥ 6 or combo points ≥ 5 and time left on Slice and Dice < 3 and time left in the fight > 9): cast Slice and Dice (+0.4%, pass 1)
  4. threshold 3 -> 6: if time left on Expose Armor < 3 and combo points ≥ 5 and time left in the fight ≥ 3 and time left in the fight ≥ 10s: cast Expose Armor (+0.8%, pass 2)
  5. threshold 6 -> 12: if time left on Expose Armor < 6 and combo points ≥ 5 and time left in the fight ≥ 3 and time left in the fight ≥ 10s: cast Expose Armor (+0.9%, pass 2)
  6. spell probe: insert before the filler: cast Hemorrhage (+13.1%, pass 4)
  7. spell probe: insert in the middle: cast Mutilate (+1.2%, pass 4)
  8. spell probe: insert at the top: if auraIsInactive: cast Ghostly Strike (+2.2%, pass 4)
  9. move to the top: if Slice and Dice is up: use every other cooldown when ready (+0.2%, pass 5)
- **A fully buffed raid:** our tuned rotation (`raidsim/apl_opt.py`, 2026-09-28, 8 passes, the last 2026-10-10, 5 changes to the base rotation; third-seed check: open winner 715 -> 717 DPS (+0.2%), opt-combat-swords-raid-raid-dps 706 -> 704 DPS (-0.3%), sim preset: Sinister Strike 710 -> 711 DPS (+0.1%), combat-swords-raid 702 -> 703 DPS (+0.1%)):
  1. threshold 5 -> 2.5: if combo points ≥ 5 and (Slice and Dice is up or energy ≥ 79 or time left in the fight < 6): cast Eviscerate (+0.5%, pass 1)
  2. spell probe: insert before the filler: cast Mutilate (+0.6%, pass 4)
  3. spell probe: insert at the top: if auraIsInactive: cast Ghostly Strike (+1.8%, pass 4)
  4. spell probe: insert at the top: cast Hemorrhage (+8.6%, pass 4)
  5. threshold 2.5 -> 3.75: if combo points ≥ 2.5 and (Slice and Dice is up or energy ≥ 79 or time left in the fight < 6): cast Eviscerate (+0.2%, pass 5)

| # | Priority (the first line whose condition holds is cast) | [`combat-swords-open-raid`](combat-swords-open-raid.md) casts/min |
|---|---|---|
| 1 | if Slice and Dice is up: use every other cooldown when ready | as ready |
| 2 | if time left on Expose Armor < 12 and combo points ≥ 5 and time left in the fight ≥ 3 and time left in the fight ≥ 10s: cast Expose Armor | 1.9 |
| 3 | if (combo points ≥ 1 and not Slice and Dice is up and time left in the fight ≥ 6 or combo points ≥ 5 and time left on Slice and Dice < 3 and time left in the fight > 9) and time left in the fight ≥ 20s: cast Slice and Dice | 2.8 |
| 4 | if energy < 59 and timeToNextEnergyTick < 1: cast Adrenaline Rush | 0.3 |
| 5 | if combo points ≥ 5 and (Slice and Dice is up or energy ≥ 79 or time left in the fight < 6): cast Eviscerate | 0.6 |
| 6 | cast Sinister Strike | 17.1 |

Lines of the simulator's rotation these builds never cast: cast Ghostly Strike (needs the Ghostly Strike talent); cast Mutilate (needs the Mutilate talent); cast Hemorrhage (needs the Hemorrhage talent).

Damage by ability:

| Ability | [`combat-swords-open-raid`](combat-swords-open-raid.md) |
|---|---|
| Auto Attack | 55% |
| Sinister Strike | 29% |
| Deadly Poison | 6% |
| Dense Sharpening Stone | 4% |
| Eviscerate | 3% |
| Dragonbreath Chili | 2% |
| Goblin Sapper Charge | 2% |

## Notes

- The best swords build: +1.8% over opt-combat-swords-raid-raid-dps, the best of our builds in combat-swords-raid. The spec's raid pick may be another variant; the page lists this one among the spec's other builds.
- Open search result (combat-swords-raid, full raid): 18/33/0 (Combat) at 716.1 DPS; opt-combat-swords-raid-raid-dps 703.7, combat-swords-raid 702.6 in the same fights; 5,806 builds simulated, 2 independent runs reached the top.
- The combat-swords-raid raid rotation was re-tuned on this build (a pass in its rotation-search record); the numbers use it.
- Sibling rotations tried on it (10,000 fights): combat-daggers-raid -53.6%, assassination-raid -53.6%, subtlety-raid -53.6%; none adopted.
- Talents the simulator measures at 0 DPS in this build (tier fillers; the filler audit may move them): Lightning Reflexes, Deflection.
- Simulator numbers are the community's model of the beta (ElliotWood/Forever 2ce8265 with this project's patches), not in-game measurements.

## Open questions (verify in the live game)

- An open-search Combat build: check it against the community's Combat builds at launch.

## Sources

- <https://github.com/ElliotWood/Forever>
- <https://talentsforever.com/rogue/60/005303103003-32403300001515231--6>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
