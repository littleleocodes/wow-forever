# Fury — Dual Wield (simulator winner adopted 2026-09-26) — 13/38/0

*[Warrior](../../../README.md) · [Raids: training dummy, raid and parse](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 13/38/0 (Arms / Fury / Protection) |
| **Role** | DPS — Raid |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70009 (2026-09-25 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |
| **Based on** | Classic baseline `fury-dw-raid` |

## Summary

Allocation adopted on 2026-09-26 from `opt-fury-dw-raid-raid-dps`, the best build in the community simulator (+5.5% DPS vs the previous draft with the simulator's gear, rotation and buffs; the previous draft is kept under raid/raidsim/candidates/). Core talents are ranked by the simulator's removal cost. Previous summary: The Classic 17/34/0 survives almost intact: Improved Tactical Mastery stands in for Tactical Mastery (still the gate to Anger Management), and the five orphaned Improved Battle Shout points become the new tier-3 fillers (Boundless Rage, Piercing Howl) plus Raging Blows (off-hand Whirlwind) and a point of Precision (hit).

## Point allocation

### Arms (13)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Improved Rend** | 3/3 | changed | Increases the Bleed damage done by your Rend ability by 35%. |
| **Improved Heroic Strike** | 2/3 | changed | Reduces the cost of your Heroic Strike ability by 2 Rage. |
| **Improved Tactical Mastery** | 5/5 | **NEW** | Tactical Mastery lets you retain up to an additional 15 Rage when you change stances. |
| **Anger Management** | 1/1 | changed | Generates 1 Rage every 3 sec while in combat, and reduces Rage loss while out of combat by 30%. |
| **Deep Wounds** | 2/3 | changed | Your critical strikes cause your opponent to Bleed, dealing 40% of your melee weapon's average damage over 12 sec. |

### Fury (38)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Cruelty** | 5/5 | changed | Improves your chance to get a critical strike with melee attacks by 5%. |
| **Booming Voice** | 5/5 | changed | Increases the radius of your Battle Shout and Demoralizing Shout abilities by 50%. |
| **Unbridled Wrath** | 5/5 | changed | Gives you a 60% chance to generate 1 additional Rage when you deal melee damage with a weapon. This effect is increased to 2 Rage for two-handed weapons. |
| **Raging Blows** | 1/1 | **NEW** | Causes your Whirlwind to also strike with your off-hand weapon, and reduces the Rage cost of your Cleave ability by 2. |
| **Dual Wield Specialization** | 5/5 | changed | Increases your off-hand weapon damage by 25%, off-hand Rage generation by 100%, and chance to hit with off-hand attacks by 10%. |
| **Improved Execute** | 2/2 | changed | Reduces the Rage cost of your Execute ability by 5. |
| **Enrage** | 5/5 | changed | Gives you a 30% chance to deal 10% increased Physical damage for 12 sec after being the victim of any damaging attack. |
| **Death Wish** | 1/1 | changed | When activated, increases your Physical damage done by 20% and makes you immune to Fear effects, but increases all damage you take by 5%. Lasts 30 sec. |
| **Precision** | 3/3 | **NEW** | Improves your chance to hit by 3%. |
| **Flurry** | 5/5 | changed | Increases your melee attack speed by 25% for your next 3 swings after dealing a melee critical strike. |
| **Bloodthirst** | 1/1 | changed | Instantly attack the target causing damage equal to 35% of your Attack Power plus 30 and increasing your movement speed by 10% for 10 sec. |

### Protection (0)

*No points.*

## Core talents (priority order)

1. **Dual Wield Specialization** — Reworked: off-hand damage, off-hand rage generation and off-hand hit per rank — still the dual-wield engine. Raid sim (2026-09-26): removing it costs +18% DPS.
2. **Flurry** — Haste after crits (demo rank 1 = 5%; max rank estimated 25%, down from Classic's 30%). Raid sim (2026-09-26): removing it costs +11% DPS.
3. **Cruelty** — +5% crit. Raid sim (2026-09-26): removing it costs +8% DPS.
4. **Death Wish** — +20% damage cooldown; now increases damage taken by 5% instead of dropping armor. Raid sim (2026-09-26): removing it costs +6% DPS.
5. **Improved Execute** — Raid sim (2026-09-26): removing it costs +4% DPS.
6. **Precision** — Raid sim (2026-09-26): removing it costs +4% DPS.
7. **Bloodthirst** — Still the capstone; demo text: 35% AP + flat damage and a movement-speed buff. Raid sim (2026-09-26): removing it costs +3% DPS.
8. **Unbridled Wrath** — Reworked to 12% per rank (est. 60% at max) chance for extra rage — better than Classic. Raid sim (2026-09-26): removing it costs +3% DPS.

## Flex points

| Pts | Default | Alternatives | Why |
|---|---|---|---|
| 2 | Improved Heroic Strike | any utility talent legal at that tier | Measures +0.3% DPS in the community simulator (noise): these points are free to move. |
| 3 | Improved Rend | any utility talent legal at that tier | Measures +0.0% DPS in the community simulator (noise): these points are free to move. |
| 5 | Improved Tactical Mastery | any utility talent legal at that tier | Measures +0.0% DPS in the community simulator (noise): these points are free to move. |
| 2 | Booming Voice | any utility talent legal at that tier | Measures +0.0% DPS in the community simulator (noise): these points are free to move. |
| 3 | Booming Voice | Boundless Rage, any utility talent legal at that tier | Measures +0.0% DPS in the community simulator (noise): these points are free to move. |
| 5 | Enrage | any utility talent legal at that tier | Measures +0.0% DPS in the community simulator (noise): these points are free to move. |

## Rank among our builds and the community simulator's

**1 of 5** for `fury-dw-raid` by training-dummy DPS in the community simulator (ElliotWood/Forever 40be98e); full ranking and the other builds' rotations: [raid README](../README.md), [raid rotations](../rotation.md).

| Rank | Build | By | Split | Dummy DPS | vs best | Raid DPS | vs best in a raid | Out of mana on the dummy |
|---|---|---|---|---|---|---|---|---|
| 1 | **[`fury-dw-raid`](fury-dw-raid.md)** | ours: hand draft | 13/38/0 | 221 | +0.0% | 401 | -0.1% | 0 s |
| 2 | [`opt-fury-dw-raid-raid-dps`](opt-fury-dw-raid-raid-dps.md) | ours: optimizer | 13/38/0 | 221 | +0.0% | 402 | +0.0% | 0 s |
| 3 | *DPS* | community simulator | - | 212 | -4.4% | 391 | -2.6% | 0 s |
| 4 | *Fury 17/34/0* | community simulator | - | 197 | -10.9% | 364 | -9.4% | 0 s |
| 5 | *Arms 39/12/0* | community simulator | - | 136 | -38.6% | 264 | -34.3% | 0 s |

## Rotation (community simulator, training dummy)

- **The training dummy:** our tuned rotation (`raidsim/apl_opt.py`, 2026-09-28, 4 passes, the last 2026-09-29, 15 changes to the base rotation; third-seed check: opt-fury-dw-raid-raid-dps 183 -> 256 DPS (+40.2%), sim preset: DPS 171 -> 240 DPS (+40.4%)):
  1. insert at the top: if time left in the fight ≤ 15s: cast Recklessness (+14.7%, pass 1)
  2. insert before the filler: if stacks of Sunder Armor < 5: cast Sunder Armor (+12.1%, pass 1)
  3. threshold 15s -> 22.5s: if time left in the fight ≤ 15s: cast Recklessness (+1.5%, pass 1)
  4. only with 20s or more of the fight left: if number of targets = 1 and (rage ≥ 40 or execute phase (E20)): cast Heroic Strike (+0.9%, pass 1)
  5. threshold 20s -> 40s: if number of targets = 1 and (rage ≥ 40 or execute phase (E20)) and time left in the fight ≥ 20s: cast Heroic Strike (+0.5%, pass 1)
  6. drop: cast Bloodthirst (+0.4%, pass 1)
  7. only with 20s or more of the fight left: if stacks of Sunder Armor < 1 and not Expose Armor is up: cast Sunder Armor (+0.7%, pass 1)
  8. threshold 1 -> 3: if stacks of Sunder Armor < 1 and not Expose Armor is up and time left in the fight ≥ 20s: cast Sunder Armor (+0.2%, pass 1)
  9. drop: if rage < 90: cast Bloodrage (+0.3%, pass 1)
  10. threshold 30s -> 22.5s: if (time left in the fight ≤ 30s or time left in the fight ≥ 140s): use every other cooldown when ready (+1.6%, pass 1)
  11. threshold 140s -> 70s: if (time left in the fight ≤ 22.5s or time left in the fight ≥ 140s): use every other cooldown when ready (+1.2%, pass 1)
  12. move to the top: if execute phase (E20): cast Execute (+0.6%, pass 1)
  13. threshold 40 -> 60: if number of targets = 1 and (rage ≥ 40 or execute phase (E20)) and time left in the fight ≥ 40s: cast Heroic Strike (+0.2%, pass 1)
  14. drop the condition: if number of targets > 1: cast Whirlwind (+0.4%, pass 1)
  15. threshold 3 -> 4: if stacks of Sunder Armor < 3 and not Expose Armor is up and time left in the fight ≥ 20s: cast Sunder Armor + move to the top: if (time left in the fight ≤ 30s or time left in the fight ≥ 211.5s): cast Death Wish (+0.2%, pass 1)
- **A fully buffed raid:** our tuned rotation (`raidsim/apl_opt.py`, 2026-09-28, 4 passes, the last 2026-09-29, 5 changes to the base rotation; third-seed check: opt-fury-dw-raid-raid-dps 383 -> 441 DPS (+15.2%), sim preset: DPS 378 -> 439 DPS (+16.2%)):
  1. drop: if false: cast Recklessness (+11.1%, pass 1)
  2. drop: if number of targets = 1 and (rage ≥ 40 or execute phase (E20)): cast Heroic Strike (+2.5%, pass 1)
  3. threshold 90 -> 45: if rage < 90: cast Bloodrage (+0.7%, pass 1)
  4. drop: if not Battle Shout is up: cast Battle Shout (+0.6%, pass 1)
  5. threshold 45 -> 22.5: if rage < 45: cast Bloodrage (+0.3%, pass 1)

| # | Priority (the first line whose condition holds is cast) | [`fury-dw-raid`](fury-dw-raid.md) casts/min |
|---|---|---|
| 1 | if (time left in the fight ≤ 30s or time left in the fight ≥ 211.5s): cast Death Wish | 0.3 |
| 2 | if execute phase (E20): cast Execute | 5.8 |
| 3 | cast Bloodthirst | 4.6 |
| 4 | if time left in the fight ≤ 22.5s: cast Recklessness | 0.3 |
| 5 | if stacks of Sunder Armor < 4 and not Expose Armor is up and time left in the fight ≥ 20s: cast Sunder Armor | 7.6 |
| 6 | cast Goblin Sapper Charge | as ready |
| 7 | cast Dense Dynamite | as ready |
| 8 | if false: cast Recklessness | 0.3 |
| 9 | if (time left in the fight ≤ 20s or time left in the fight ≥ 140s): cast Potion | as ready |
| 10 | if (time left in the fight ≤ 30s or time left in the fight ≥ 130s): cast Earthstrike | as ready |
| 11 | if (time left in the fight ≤ 30s or time left in the fight ≥ 130s): cast Slayer's Crest | as ready |
| 12 | if (time left in the fight ≤ 30s or time left in the fight ≥ 130s): cast Slayer's Crest | as ready |
| 13 | if (time left in the fight ≤ 22.5s or time left in the fight ≥ 70s): use every other cooldown when ready | as ready |
| 14 | cast Whirlwind | 3.3 |
| 15 | if time until Bloodthirst is ready > 1.5s: cast Whirlwind | 3.3 |
| 16 | if number of targets = 1 and (rage ≥ 60 or execute phase (E20)) and time left in the fight ≥ 40s: cast Heroic Strike | 0.3 |
| 17 | if not Battle Shout is up: cast Battle Shout | 0.3 |
| 18 | if stacks of Sunder Armor < 5: cast Sunder Armor | 7.6 |

Lines of the simulator's rotation these builds never cast: cast Blood Fury, cast spell 24427, cast spell 29602, cast Cleave, cast Hamstring, cast Berserker Stance (its condition never held in these fights); cast Mortal Strike (needs the Mortal Strike talent); cast Spearing Strike (needs the Spearing Strike talent).

Damage by ability:

| Ability | [`fury-dw-raid`](fury-dw-raid.md) |
|---|---|
| Auto Attack | 46% |
| Execute | 33% |
| Bloodthirst | 10% |
| Whirlwind | 7% |
| Deep Wound | 2% |
| Dragonbreath Chili | 1% |
| Heroic Strike | 1% |
| Hamstring | 0% |

## Notes

- Adopted from the community simulator on 2026-09-26: opt-fury-dw-raid-raid-dps beat the previous draft by +5.5% DPS; the rationale below predates the adoption where it names talents no longer taken.
- Weaponmaster (the Sword/Axe Specialization replacement) sits at Arms tier 5 (20 points) — unreachable without dropping Bloodthirst, exactly like Classic.
- Improved Battle Shout and Improved Demoralizing Shout are gone: raid Battle Shout is no longer a talent responsibility.
- 2026-09-29 filler audit (raidsim/filler_audit.py, user question on zero-value fillers): points the simulator measures at 0 moved, one at a time, to talents that help in a real raid (interrupt protection, threat, mana, range, survival; the simulator cannot see these, so the order is our judgment) or that gain DPS: Boundless Rage -> Booming Voice (range); Boundless Rage -> Booming Voice (range); Boundless Rage -> Booming Voice (range). Net +0.00% on a third seed.

## Open questions (verify in the live game)

- Enrage uptime for a DPS warrior who rarely takes damage — is 5/5 still the best path to Flurry?
- Real max-rank values for Flurry, Unbridled Wrath and Dual Wield Specialization (demo shows rank 1 only).
- Does Raging Blows' off-hand Whirlwind beat 2 more points of Precision?

## Sources

- <https://warcraftforever.games/talents/warrior>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
