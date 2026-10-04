# Frostfire — Frostfire Bolt / Hot Streak (Fire/Frost hybrid, raid) — 4/31/16

*[Mage](../../../README.md) · [Raids: training dummy, raid and parse](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 4/31/16 (Arcane / Fire / Frost) |
| **Role** | DPS — Raid |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70009 (2026-09-25 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |
| **Based on** | Classic baseline `fire-raid` |

## Summary

A Fire/Frost hybrid built on Frostfire Bolt, new in Forever (trained at 40, 50 and 60; it counts as both Fire and Frost, so Fire Power and Piercing Ice, Critical Mass and Ice Shards all apply to it, and Improved Fireball and Hot Streak name it). Deep Fire for Improved Fireball, Ignite, Improved Scorch, Hot Streak and Critical Mass, and 16 Frost points for Elemental Precision, Ice Shards, Piercing Ice and Frost Channeling. Found by the simulator talent search (raidsim/talent_opt.py) from four starts, on our implementation of Frostfire Bolt (the community simulator ships the spell as a stub: raidsim/patches/). Best Frostfire build found, not a recommendation: Frostfire Bolt rank 3 hits for 270-314 plus 57 over 9 s, against Frostbolt rank 11's 457-493 and Fireball rank 12's 425-541, and the two trees' talents on one spell do not close that gap (see the rank table).

## Point allocation

### Arcane (4)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Improved Channeling** | 4/5 | **NEW** | Gives you a 80% chance to avoid interruption caused by damage while channeling Arcane Missiles and a 56% chance while casting Arcane Blast. |

### Fire (31)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Incineration** | 3/3 | **NEW** | Increases the critical strike chance of your Fire Blast, Ice Lance, Arcane Blast, and Scorch spells by 6%. |
| **Improved Fireball** | 2/5 | changed | Reduces the casting time of your Fireball and Frostfire Bolt spells by 0.2 sec. |
| **Ignite** | 5/5 | unchanged | Your critical strikes from Fire damage spells cause the target to burn for an additional 40% of your spell's damage over 4 sec. |
| **Flame Throwing** | 1/2 | unchanged | Increases the range of your Fire spells by 3 yards. |
| **Burning Soul** | 3/3 | changed | Gives your Fire spells a 70% chance to not lose casting time when you take damage and reduces the threat caused by your Fire spells by 30%. |
| **Pyroblast** | 1/1 | changed | Hurls an immense fiery boulder that causes 101 to 131 Fire damage and an additional 44 Fire damage over 12 sec. |
| **Improved Scorch** | 3/3 | changed | Your Scorch spell has a 100% chance to cause your target to be vulnerable to Fire damage. This vulnerability increases all Fire damage you deal to your target by 3% and lasts 30 sec, stacking up to 5 times. |
| **Heating Up** | 1/1 | **NEW** | Non-periodic critical strikes with Fireball, Frostfire Bolt, Fire Blast, and Scorch reduce the cast time of your next Pyroblast cast within 20 sec by 25%, stacking up to 3 times. |
| **Master of Elements** | 3/3 | changed | Your Fire and Frost critical strikes will refund 30% of their base mana cost. |
| **Critical Mass** | 3/3 | unchanged | Increases the critical strike chance of your Fire spells by 6%. |
| **Fire Power** | 5/5 | unchanged | Increases the damage done by your Fire spells by 10%. |
| **Combustion** | 1/1 | changed | When activated, this spell causes each of your Fire damage spell hits to increase your critical strike chance with Fire damage spells by 10%. This effect lasts until you have caused 3 non-periodic critical strikes with Fire spells. |

### Frost (16)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Elemental Precision** | 5/5 | changed | Improves your chance to hit with Frost and Fire spells by 5%. |
| **Ice Shards** | 5/5 | unchanged | Increases the critical strike damage bonus of your Frost spells by 100%. |
| **Piercing Ice** | 3/3 | unchanged | Increases the damage done by your Frost spells by 6%. |
| **Frost Channeling** | 3/3 | moved | Reduces the mana cost of your Frost spells by 15% and reduces the threat caused by your Frost spells by 30%. |

## Core talents (priority order)

1. **Improved Fireball** — -0.1 s per rank on Fireball and Frostfire Bolt: a 2.5 s bolt at 5/5.
2. **Hot Streak** — Frostfire Bolt crits build Hot Streak: a 1.5 s Pyroblast at three stacks.
3. **Ignite** — Frostfire Bolt counts as Fire: its crits ignite for 40% more.
4. **Critical Mass** — +Fire crit, and Frostfire Bolt is Fire.
5. **Fire Power** — +Fire damage on Frostfire Bolt.
6. **Ice Shards** — +Frost crit damage: Frostfire Bolt is Frost too (the simulator search's first move from the Fire build).
7. **Piercing Ice** — +Frost damage on Frostfire Bolt.
8. **Elemental Precision** — Fire and Frost hit against a level-63 boss.

## Flex points

| Pts | Default | Alternatives | Why |
|---|---|---|---|
| 3 | Frost Channeling | Master of Elements | Mana: Frostfire Bolt costs 370 at rank 3, more than Frostbolt's 290. |
| 5 | Flame Throwing 2 + Burning Soul 2 + Blast Wave 1 | Arcane Focus | Tier fillers on the way to the Fire capstones. |

## Rank among our builds and the community simulator's

**2 of 2** for `frostfire-raid` by training-dummy DPS in the community simulator (ElliotWood/Forever b0f0df3); full ranking and the other builds' rotations: [raid README](../README.md), [raid rotations](../rotation.md).

| Rank | Build | By | Split | Dummy DPS | vs best | Raid DPS | vs best in a raid | Out of mana on the dummy |
|---|---|---|---|---|---|---|---|---|
| 1 | [`frostfire-ml-raid`](frostfire-ml-raid.md) | ours: hand draft | 4/31/16 | 499 | +0.0% | 614 | +0.0% | 2 s |
| 2 | **[`frostfire-raid`](frostfire-raid.md)** | ours: hand draft | 4/31/16 | 479 | -4.0% | 589 | -4.2% | 0 s |

## Rotation (community simulator, training dummy)

- **The training dummy:** our tuned rotation (`raidsim/apl_opt.py`, 2026-09-28, 4 passes, the last 2026-10-02, 13 changes to the base rotation; third-seed check: ml: Hybrid Fire/Frost 557 -> 612 DPS (+10.0%), frostfire-raid 552 -> 616 DPS (+11.7%)):
  1. insert before the filler: cast Fireball (+0.7%, pass 1)
  2. threshold 20% -> 10%: if mana % < 20% and time left in the fight > 25s: cast Evocation (+0.5%, pass 1)
  3. only with 3s or more of the fight left: cast Fireball (+0.3%, pass 1)
  4. insert before the filler: cast Robe of the Archmage (+0.6%, pass 2)
  5. threshold 5s -> 6s: if Fire Vulnerability is known and (stacks of Fire Vulnerability < 5 or time left on Fire Vulnerability ≤ 5s): cast Scorch (+0.4%, pass 2)
  6. insert at the top: cast Berserking (+0.2%, pass 2)
  7. move down below 'if mana % ≥ 10%: cast Frostfire Bolt': cast Fire Blast (+6.4%, pass 4)
  8. only with 6s or more of the fight left: if mana % ≥ 10%: cast Frostfire Bolt (+1.1%, pass 4)
  9. insert in the middle: cast Mana Citrine (+0.5%, pass 4)
  10. threshold 3 -> 2: if stacks of Hot Streak = 3: cast Pyroblast (+0.3%, pass 4)
  11. insert in the middle: if stacks of Hot Streak = 3: cast Pyroblast (+0.6%, pass 4)
  12. only with 20s or more of the fight left: if Fire Vulnerability is known and (stacks of Fire Vulnerability < 5 or time left on Fire Vulnerability ≤ 6s): cast Scorch (+0.3%, pass 4)
  13. insert in the middle: cast Combustion (+0.3%, pass 4)
- **A fully buffed raid:** our tuned rotation (`raidsim/apl_opt.py`, 2026-09-28, 5 passes, the last 2026-10-02, 10 changes to the base rotation; third-seed check: ml: Hybrid Fire/Frost 670 -> 727 DPS (+8.5%), frostfire-raid 664 -> 723 DPS (+8.9%)):
  1. insert at the top: if mana ≥ (time left in the fight × 110): cast Fire Blast (+0.2%, pass 1)
  2. threshold 110 -> 82.5: if mana ≥ (time left in the fight × 110): cast Fire Blast (+0.2%, pass 1)
  3. insert at the top: cast Berserking (+0.3%, pass 3)
  4. drop: cast Fire Blast (+2.5%, pass 5)
  5. threshold 5s -> 10s: if Fire Vulnerability is known and (stacks of Fire Vulnerability < 5 or time left on Fire Vulnerability ≤ 5s): cast Scorch (+2.2%, pass 5)
  6. threshold 82.5 -> 165: if mana ≥ (time left in the fight × 82.5): cast Fire Blast (+1.6%, pass 5)
  7. threshold 10s -> 7.5s: if Fire Vulnerability is known and (stacks of Fire Vulnerability < 5 or time left on Fire Vulnerability ≤ 10s): cast Scorch (+1.0%, pass 5)
  8. threshold 165 -> 330: if mana ≥ (time left in the fight × 165): cast Fire Blast (+0.5%, pass 5)
  9. threshold 3 -> 2: if stacks of Hot Streak = 3: cast Pyroblast (+0.3%, pass 5)
  10. insert in the middle: if stacks of Hot Streak = 3: cast Pyroblast (+0.6%, pass 5)

| # | Priority (the first line whose condition holds is cast) | [`frostfire-raid`](frostfire-raid.md) casts/min |
|---|---|---|
| 1 | cast Berserking | 0.3 |
| 2 | if Fire Vulnerability is known and (stacks of Fire Vulnerability < 5 or time left on Fire Vulnerability ≤ 6s) and time left in the fight ≥ 20s: cast Scorch | 3.6 |
| 3 | if mana % ≤ 80%: cast Mana Ruby (mana gem) | as ready |
| 4 | use every other cooldown when ready | as ready |
| 5 | if mana % < 10% and time left in the fight > 25s: cast Evocation | 0.3 |
| 6 | if stacks of Heating Up = 2: cast Pyroblast | 1.7 |
| 7 | if stacks of Heating Up = 3: cast Pyroblast | 1.7 |
| 8 | cast Combustion | 0.3 |
| 9 | cast Mana Citrine | as ready |
| 10 | if mana % ≥ 10% and time left in the fight ≥ 6s: cast Frostfire Bolt | 16.4 |
| 11 | cast Fire Blast | 0.3 |
| 12 | if time left in the fight ≥ 3s: cast Fireball | 0.1 |
| 13 | cast Robe of the Archmage | as ready |
| 14 | cast Scorch | 0.2 |

Lines of the simulator's rotation these builds never cast: cast Arcane Missiles (its condition never held in these fights).

Damage by ability:

| Ability | [`frostfire-raid`](frostfire-raid.md) |
|---|---|
| Frostfire Bolt | 66% |
| Pyroblast | 13% |
| Ignite | 12% |
| Scorch | 7% |
| Fire Blast | 1% |
| Fireball | 0% |

## Notes

- New-builds survey (2026-09-28, user request): the Frostfire Bolt mage asked for by name. Frostfire Bolt is implemented by this project in the local build of the community simulator (patches/forever/sim/mage/frostfire_bolt.go, from the client's spell data like the simulator's Fireball); its numbers are our model, not the community's.
- The fight lab plays a Frostfire leveling rotation (fightlab/mage.py decide_frostfire: Frostbolt until 40, then Frostfire Bolt, which also slows the mob 40% like Frostbolt).
- Second talent search (2026-09-28, after the bench's potion fix and the rotation's second pass): 1 point Wake of Fire -> Improved Fireball (+0.5%).
- 2026-09-29 filler audit (raidsim/filler_audit.py, user question on zero-value fillers): points the simulator measures at 0 moved, one at a time, to talents that help in a real raid (interrupt protection, threat, mana, range, survival; the simulator cannot see these, so the order is our judgment) or that gain DPS: Burning Soul -> Wake of Fire (+1.6% DPS); Burning Soul -> Wake of Fire (+1.0% DPS); Flame Throwing -> Improved Channeling (interrupt); Flame Throwing -> Improved Channeling (interrupt). Net +2.45% on a third seed.
- 2026-10-02 filler audit (raidsim/filler_audit.py, user question on zero-value fillers; 2026-10-02 user report on talents whose ability the rotation never casts: Blast Wave was never cast here): points the simulator measures at 0 moved, one at a time, to talents that help in a real raid (interrupt protection, threat, mana, range, survival; the simulator cannot see these, so the order is our judgment) or that gain DPS: Blast Wave -> Improved Channeling (interrupt); Wake of Fire -> Improved Channeling (interrupt); Wake of Fire -> Burning Soul (threat); Improved Fireball -> Burning Soul (threat); Improved Fireball -> Burning Soul (threat); Improved Fireball -> Flame Throwing (range). Net -0.04% on a third seed.
- 2026-10-03: repaired for beta build 1.60.1.70170 (talents removed, renamed or moved): Hot Streak 1 out; Heating Up 1 in; to be re-optimized.

## Open questions (verify in the live game)

- Does Frostfire Bolt take both schools' bonuses in the live game (Fire Power and Piercing Ice, Critical Mass and Ice Shards)? The tooltip says it counts as both Frost and Fire damage.
- Are the rank-3 numbers (270-314 + 57 over 9 s, 370 mana) final? A stronger Frostfire Bolt would move this build up the ranking.
- Frostfire Bolt's slow: the tooltip gives 40% without a duration (9 s assumed in the fight lab).

## Sources

- <https://warcraftforever.games/talents/mage>
- <_reference/data/raidsim/patches/README.md>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
