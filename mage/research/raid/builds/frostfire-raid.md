# Frostfire — Frostfire Bolt (Fire/Frost hybrid, raid) — 7/31/13

*[Mage](../../../README.md) · [Raids: training dummy, raid and parse](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 7/31/13 (Arcane / Fire / Frost) |
| **Role** | DPS — Raid |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70707 (2026-10-16 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |
| **Based on** | Classic baseline `fire-raid` |

## Summary

A Fire/Frost hybrid built on Frostfire Bolt, new in Forever (trained at 40, 50 and 60; it counts as both Fire and Frost, so Fire Power and Piercing Ice, Critical Mass and Ice Shards all apply to it, and Improved Fireball names it). Deep Fire for Improved Fireball, Ignite, Improved Scorch and Critical Mass, and 16 Frost points for Elemental Precision, Ice Shards, Piercing Ice and Frost Channeling. Found by the simulator talent search (raidsim/talent_opt.py) from four starts, on our implementation of Frostfire Bolt (the community simulator ships the spell as a stub: raidsim/patches/). Best Frostfire build found, not a recommendation: Frostfire Bolt rank 3 hits for 270-314 plus 57 over 9 s, against Frostbolt rank 11's 457-493 and Fireball rank 12's 425-541, and the two trees' talents on one spell do not close that gap (see the rank table).

## Point allocation

### Arcane (7)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Arcane Resilience** | 1/3 | changed | Increases your Armor by an amount equal to 25% of your Intellect. |
| **Improved Channeling** | 4/5 | **NEW** | Gives your Arcane Missiles spell a 80% chance and your Arcane Blast and Arcane Wrath spells a 56% chance to not lose casting time when you take damage. |
| **Arcane Concentration** | 1/5 | unchanged | Gives you a 2% chance of entering a Clearcasting state after any damage spell hits a target. The Clearcasting state reduces the mana cost of your next damage spell by 100%. |
| **Missile Barrage** | 1/2 | **NEW** | Gives your Arcane Blast spell a 20% chance, and your Arcane Wrath, Fireball, Frostbolt, Frost Blast, and Frostfire Bolt spells a 10% chance to reduce the channeled duration of your next Arcane Missiles spell by 50%, reduce the Mana cost by 100%, and missiles fire every 0.5 sec. |

### Fire (31)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Accelerant** | 2/5 | changed | Reduces the casting time of your Fireball, Frostfire Bolt, and Arcane Wrath spells by 0.2 sec. |
| **Incineration** | 3/5 | **NEW** | Increases the critical strike chance of your Fire Blast, Ice Lance, Arcane Blast, and Scorch spells by 6%. |
| **Flame Throwing** | 1/2 | unchanged | Increases the range of your Fire spells by 3 yards. |
| **Ignite** | 5/5 | unchanged | Your critical strikes from Fire damage spells cause the target to burn for an additional 40% of your spell's damage over 4 sec. |
| **Burning Soul** | 3/3 | changed | Gives your Fire spells a 70% chance to not lose casting time when you take damage and reduces the threat caused by your Fire spells by 30%. |
| **Improved Fire Blast** | 2/2 | **NEW** | Reduces the cooldown of your Fire Blast spell by 2 sec and increases its range by 15 yards. |
| **Pyroblast** | 1/1 | changed | Hurls an immense fiery boulder that causes 101 to 131 Fire damage and an additional 44 Fire damage over 12 sec. |
| **Heating Up** | 1/1 | **NEW** | Non-periodic critical strikes with Fireball, Frostfire Bolt, Fire Blast, and Scorch reduce the cast time of your next Pyroblast cast within 20 sec by 25%, stacking up to 3 times. Fire Blast grants an additional stack every time it deals damage. |
| **Improved Scorch** | 3/3 | changed | Your Scorch spell has a 100% chance to cause your target to be vulnerable to Fire damage. This vulnerability increases all Fire damage you deal to your target by 3% and lasts 30 sec, stacking up to 5 times. |
| **Master of Elements** | 3/3 | changed | Your Fire and Frost critical strikes will refund 30% of their base mana cost. |
| **Critical Mass** | 3/3 | unchanged | Increases the critical strike chance of your Fire spells by 6%. |
| **Fire Power** | 3/3 | unchanged | Increases the damage done by your Fire spells by 3% per your Fire effects on the target, up to a maximum increase of 12%. Effects which mix multiple schools of magic do not qualify. |
| **Combustion** | 1/1 | changed | When activated, this spell causes each of your Fire damage spell hits to increase your critical strike chance with Fire damage spells by 10%. This effect lasts until you have caused 3 non-periodic critical strikes with Fire spells. |

### Frost (13)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Frost Warding** | 2/2 | changed | Increases the Armor and resistances granted by your Frost Armor and Ice Armor spells by 30%, gives your Frost Ward a 20% chance to negate the warded damage spell, and increases the amount absorbed by your Ice Barrier and Frost Ward by 20%. |
| **Precision** | 3/3 | changed | Improves your chance to hit with all spells by 6%. |
| **Ice Shards** | 5/5 | unchanged | Increases the critical strike damage bonus of your Frost spells by 100%. |
| **Frost Channeling** | 3/3 | moved | Reduces the mana cost of your Frost spells by 15% and reduces the threat caused by your Frost spells by 30%. |

## Core talents (priority order)

1. **Improved Fireball** — -0.1 s per rank on Fireball and Frostfire Bolt: a 2.5 s bolt at 5/5.
2. **Ignite** — Frostfire Bolt counts as Fire: its crits ignite for 40% more.
3. **Critical Mass** — +Fire crit, and Frostfire Bolt is Fire.
4. **Fire Power** — +Fire damage on Frostfire Bolt.
5. **Ice Shards** — +Frost crit damage: Frostfire Bolt is Frost too (the simulator search's first move from the Fire build).
6. **Piercing Ice** — +Frost damage on Frostfire Bolt.
7. **Elemental Precision** — Fire and Frost hit against a level-63 boss.

## Flex points

| Pts | Default | Alternatives | Why |
|---|---|---|---|
| 3 | Frost Channeling | Master of Elements | Mana: Frostfire Bolt costs 370 at rank 3, more than Frostbolt's 290. |
| 5 | Flame Throwing 2 + Burning Soul 2 + Blast Wave 1 | Arcane Focus | Tier fillers on the way to the Fire capstones. |

## Rank among our builds and the community simulator's

**1 of 4** for `frostfire-raid` by training-dummy DPS in the community simulator (wowsims/forever b90e2b9 (client 70707)); full ranking and the other builds' rotations: [raid README](../README.md), [raid rotations](../rotation.md).

| Rank | Build | By | Split | Dummy DPS | vs best | Raid DPS | vs best in a raid | Out of mana on the dummy |
|---|---|---|---|---|---|---|---|---|
| 1 | **[`frostfire-raid`](frostfire-raid.md)** | ours: hand draft | 7/31/13 | 446 | +0.0% | 599 | -4.0% | 33 s |
| 2 | [`frostfire-fingers-of-frost-raid`](frostfire-fingers-of-frost-raid.md) | ours: hand draft | 0/29/22 | 437 | -2.1% | 618 | -0.9% | 40 s |
| 3 | [`frostfire-ml-raid`](frostfire-ml-raid.md) | ours: derived (ML search) | 0/29/22 | 434 | -2.8% | 618 | -1.0% | 41 s |
| 4 | *FFB* | community simulator | - | 423 | -5.3% | 624 | +0.0% | 47 s |

## Rotation (community simulator, training dummy)

- **The training dummy:** our tuned rotation (`raidsim/apl_opt.py`, 2026-09-28, 10 passes, the last 2026-10-24, 18 changes to the base rotation; third-seed check: open winner 496 -> 469 DPS (-5.4%), frostfire-raid 506 -> 515 DPS (+1.8%), sim preset: FFB 485 -> 463 DPS (-4.5%), frostfire-ml-raid 477 -> 488 DPS (+2.3%), frostfire-fingers-of-frost-raid 494 -> 463 DPS (-6.3%)):
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
  14. only above 25% mana: if mana % ≥ 10% and time left in the fight ≥ 6s: cast Frostfire Bolt (+0.7%, pass 5)
  15. move to the top: cast Fire Blast (+3.8%, pass 5)
  16. insert at the top: if (stacks of Fire Vulnerability < 5 or time left on Fire Vulnerability ≤ 5s): cast Scorch (+0.5%, pass 5)
  17. spell probe: insert in the middle: cast Arcane Blast (+1.8%, pass 9)
  18. spell probe: insert at the top: cast Arcane Power (+1.2%, pass 9)
- **A fully buffed raid:** our tuned rotation (`raidsim/apl_opt.py`, 2026-09-28, 18 passes, the last 2026-10-31, 32 changes to the base rotation; third-seed check: open winner 629 -> 732 DPS (+16.3%), frostfire-fingers-of-frost-raid 628 -> 730 DPS (+16.2%), sim preset: FFB 639 -> 733 DPS (+14.8%), frostfire-raid 600 -> 681 DPS (+13.4%), frostfire-ml-raid 633 -> 742 DPS (+17.2%)):
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
  11. drop the condition: if mana ≥ (time left in the fight × 330): cast Fire Blast (+4.9%, pass 6)
  12. threshold 25s -> 50s: if mana % < 20% and time left in the fight > 25s: cast Evocation (+0.6%, pass 6)
  13. drop: if stacks of Heating Up = 2: cast Pyroblast (+0.3%, pass 6)
  14. drop: cast Berserking (+0.3%, pass 6)
  15. move down below 'if mana % ≥ 10%: cast Frostfire Bolt': if mana % < 20% and time left in the fight > 50s: cast Evocation (+0.2%, pass 6)
  16. move to the top: if stacks of Heating Up = 3: cast Pyroblast (+0.2%, pass 6)
  17. insert at the top: if Fingers of Frost is up: cast Ice Lance (+0.2%, pass 8)
  18. threshold 7.5s -> 15s: if Fire Vulnerability is known and (stacks of Fire Vulnerability < 5 or time left on Fire Vulnerability ≤ 7.5s): cast Scorch + insert before the filler: cast Fireball (+0.2%, pass 8)
  19. drop: if mana % < 20% and time left in the fight > 50s: cast Evocation (+0.4%, pass 8)
  20. insert in the middle: cast Mana Citrine (+0.2%, pass 8)
  21. rank 2 below 30% mana, above: if mana % ≥ 10%: cast Frostfire Bolt (+1.4%, pass 12)
  22. drop 'mana % ≥ 10%' from the condition: if mana % ≥ 10% and mana % < 30%: cast Frostfire Bolt (+0.9%, pass 12)
  23. spell probe: insert at the top: cast Arcane Power (+0.3%, pass 13)
  24. drop: if Fingers of Frost is up: cast Ice Lance (+217.8%, pass 14)
  25. insert at the top: cast Demonic Rune (+0.4%, pass 14)
  26. insert before the filler: cast Robe of the Archmage (+0.3%, pass 14)
  27. threshold 15s -> 7.5s: if Fire Vulnerability is known and (stacks of Fire Vulnerability < 5 or time left on Fire Vulnerability ≤ 15s): cast Scorch (+0.4%, pass 15)
  28. insert at the top: if (stacks of Fire Vulnerability < 5 or time left on Fire Vulnerability < 5) and (stacks of Fire Vulnerability < 4 or not spellIsCasting): cast Scorch (+0.3%, pass 17)
  29. move down below 'cast Fire Blast': if stacks of Heating Up = 3: cast Pyroblast (+1.4%, pass 18)
  30. insert at the top: if stacks of Heating Up = 3 and not spellIsCasting: cast Pyroblast (+1.9%, pass 18)
  31. drop: if stacks of Heating Up = 3: cast Pyroblast (+10.1%, pass 18)
  32. drop: if (stacks of Fire Vulnerability < 5 or time left on Fire Vulnerability < 5) and (stacks of Fire Vulnerability < 4 or not spellIsCasting): cast Scorch (+0.5%, pass 18)

| # | Priority (the first line whose condition holds is cast) | [`frostfire-raid`](frostfire-raid.md) casts/min |
|---|---|---|
| 1 | if (stacks of Fire Vulnerability < 5 or time left on Fire Vulnerability ≤ 5s): cast Scorch | 7.2 |
| 2 | cast Fire Blast | 5.1 |
| 3 | if Fire Vulnerability is known and (stacks of Fire Vulnerability < 5 or time left on Fire Vulnerability ≤ 6s) and time left in the fight ≥ 20s: cast Scorch | 7.2 |
| 4 | if mana % ≤ 80%: cast Mana Ruby | as ready |
| 5 | use every other cooldown when ready | as ready |
| 6 | if mana % < 10% and time left in the fight > 25s: cast Evocation | 0.3 |
| 7 | if stacks of Heating Up = 2: cast Pyroblast | 5.1 |
| 8 | if stacks of Heating Up = 3: cast Pyroblast | 5.1 |
| 9 | cast Combustion | 0.3 |
| 10 | cast Mana Citrine | as ready |
| 11 | if mana % ≥ 10% and time left in the fight ≥ 6s and mana % ≥ 25%: cast Frostfire Bolt | 2.4 |
| 12 | if Missile Barrage is up: cast Arcane Missiles (rank 7) | 0.1 |
| 13 | if time left in the fight ≥ 3s: cast Fireball (rank 11) | 1.1 |
| 14 | cast Robe of the Archmage | as ready |
| 15 | cast Scorch | 7.2 |

Lines of the simulator's rotation these builds never cast: cast Arcane Power (needs the Arcane Power talent); cast Berserking (its condition never held in these fights); cast Arcane Blast (needs the Arcane Blast talent).

Damage by ability:

| Ability | [`frostfire-raid`](frostfire-raid.md) |
|---|---|
| Pyroblast | 39% |
| Fire Blast | 18% |
| Scorch | 16% |
| Frostfire Bolt | 10% |
| Ignite | 10% |
| Fireball | 6% |
| Arcane Missiles | 1% |
| Demonic Rune | 0% |

## Notes

- New-builds survey (2026-09-28, user request): the Frostfire Bolt mage asked for by name. Frostfire Bolt is implemented by this project in the local build of the community simulator (patches/forever/sim/mage/frostfire_bolt.go, from the client's spell data like the simulator's Fireball); its numbers are our model, not the community's.
- The fight lab plays a Frostfire leveling rotation (fightlab/mage.py decide_frostfire: Frostbolt until 40, then Frostfire Bolt, which also slows the mob 40% like Frostbolt).
- Second talent search (2026-09-28, after the bench's potion fix and the rotation's second pass): 1 point Wake of Fire -> Improved Fireball (+0.5%).
- 2026-09-29 filler audit (raidsim/filler_audit.py, user question on zero-value fillers): points the simulator measures at 0 moved, one at a time, to talents that help in a real raid (interrupt protection, threat, mana, range, survival; the simulator cannot see these, so the order is our judgment) or that gain DPS: Burning Soul -> Wake of Fire (+1.6% DPS); Burning Soul -> Wake of Fire (+1.0% DPS); Flame Throwing -> Improved Channeling (interrupt); Flame Throwing -> Improved Channeling (interrupt). Net +2.45% on a third seed.
- 2026-10-02 filler audit (raidsim/filler_audit.py, user question on zero-value fillers; 2026-10-02 user report on talents whose ability the rotation never casts: Blast Wave was never cast here): points the simulator measures at 0 moved, one at a time, to talents that help in a real raid (interrupt protection, threat, mana, range, survival; the simulator cannot see these, so the order is our judgment) or that gain DPS: Blast Wave -> Improved Channeling (interrupt); Wake of Fire -> Improved Channeling (interrupt); Wake of Fire -> Burning Soul (threat); Improved Fireball -> Burning Soul (threat); Improved Fireball -> Burning Soul (threat); Improved Fireball -> Flame Throwing (range). Net -0.04% on a third seed.
- 2026-10-03: repaired for beta build 1.60.1.70170 (talents removed, renamed or moved): Hot Streak 1 out; Heating Up 1 in; to be re-optimized.
- 2026-10-16 (repair_builds.py, client build 70425 trees): 4/31/16 -> 4/32/15; Fire Power 5 -> 3 (rank cap); +1 Improved Fire Blast (tier gating for Combustion); +1 Improved Fire Blast (tier gating for Combustion); +1 Critical Mass (prerequisite of Combustion); +1 Critical Mass (prerequisite of Combustion); -1 Heating Up (over 51); -1 Piercing Ice (over 51) (refill: the fire-raid model, raid-dps).
- 2026-10-17 (audit of 2026-10-17, finding 26): core Heating Up dropped and the name changed: the allocation has not held Heating Up since the simulator searches of 2026-10 (Hot Streak was renamed Heating Up in 70170).
- 2026-10-22 (repair_builds.py, client build 70425 trees): 4/32/15 -> 5/33/13; Elemental Precision 5 -> 3 (rank cap); Piercing Ice 2 gone; +1 Frost Warding (tier gating for Ice Shards); +1 Frost Warding (tier gating for Ice Shards); refill +1 Heating Up, +1 Missile Barrage (refill: the fire-raid model, raid-dps).
- 2026-10-30 (repair_builds.py, client build 1.60.1.70707 trees): 5/33/13 -> 7/31/13; Improved Fireball -> Accelerant (renamed); Critical Mass 5 -> 3 (rank cap); Elemental Precision -> Precision (renamed); +1 Arcane Resilience (tier gating for Missile Barrage); refill +1 Arcane Concentration (refill: the fire-raid model, raid-dps).

## Open questions (verify in the live game)

- Does Frostfire Bolt take both schools' bonuses in the live game (Fire Power and Piercing Ice, Critical Mass and Ice Shards)? The tooltip says it counts as both Frost and Fire damage.
- Are the rank-3 numbers (270-314 + 57 over 9 s, 370 mana) final? A stronger Frostfire Bolt would move this build up the ranking.
- Frostfire Bolt's slow: the tooltip gives 40% without a duration (9 s assumed in the fight lab).

## Sources

- <https://warcraftforever.games/talents/mage>
- <_reference/data/raidsim/patches/README.md>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
