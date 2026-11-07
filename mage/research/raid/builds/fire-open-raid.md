# Fire — Raid (open talent search) — 17/31/3

*[Mage](../../../README.md) · [Raids: training dummy, raid and parse](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 17/31/3 (Arcane / Fire / Frost) |
| **Role** | DPS — Raid |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70753 (2026-11-03 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

The Fire raid build the open talent search found on 2026-11-03: every legal 51-point build with no tree rule, searched in the community simulator's fire-raid rotation in a full raid (every raid buff and debuff: the group setting; raidsim/family_search.py: every pair of keystones polished by a short hill climb first, then the machine-learning search, the winner raced against the rotation's builds over 30,000 fights). +1.9% over fire-open-raid, the best of our builds in that rotation.

## Point allocation

### Arcane (17)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Wand Specialization** | 2/2 | moved | Increases your damage with Wands by 25%. |
| **Arcane Subtlety** | 2/2 | changed | Reduces your target's resistance to all your spells by 15 and reduces the threat caused by your Arcane spells by 30%. |
| **Arcane Concentration** | 5/5 | unchanged | Gives you a 10% chance of entering a Clearcasting state after any damage spell hits a target. The Clearcasting state reduces the mana cost of your next damage spell by 100%. |
| **Missile Barrage** | 2/2 | **NEW** | Gives your Arcane Blast spell a 40% chance, and your Arcane Wrath, Fireball, Frostbolt, and Frostfire Bolt spells a 20% chance to reduce the channeled duration of your next Arcane Missiles spell by 50%, reduce the Mana cost by 100%, and missiles fire every 0.5 sec. |
| **Arcane Blast** | 1/1 | **NEW** | Blasts the target with energy, dealing 34 to 38 Arcane damage. Each time you cast Arcane Blast, you gain 12% of your Intellect as Spell Damage and the mana cost of Arcane Blast is increased by 100%. Effect stacks up to 4 times and lasts 18 sec from time of initial application. |
| **Arcane Meditation** | 2/3 | changed | Allows 33% of your Mana regeneration to continue while casting. |
| **Arcane Resilience** | 3/3 | changed | Increases your Armor by an amount equal to 75% of your Intellect. |

### Fire (31)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Incineration** | 5/5 | **NEW** | Increases the critical strike chance of your Fire Blast, Ice Lance, Arcane Blast, and Scorch spells by 10%. |
| **Accelerant** | 4/5 | changed | Reduces the casting time of your Fireball, Frostfire Bolt, and Arcane Wrath spells by 0.4 sec. |
| **Ignite** | 5/5 | unchanged | Your critical strikes from Fire damage spells cause the target to burn for an additional 40% of your spell's damage over 4 sec. |
| **Pyroblast** | 1/1 | changed | Hurls an immense fiery boulder that causes 101 to 131 Fire damage and an additional 44 Fire damage over 12 sec. |
| **Improved Fire Blast** | 2/2 | **NEW** | Reduces the cooldown of your Fire Blast spell by 2 sec and increases its range by 15 yards. |
| **Improved Scorch** | 3/3 | changed | Your Scorch spell has a 100% chance to cause your target to be vulnerable to Fire damage. This vulnerability increases all Fire damage you deal to your target by 3% and lasts 30 sec, stacking up to 5 times. |
| **Heating Up** | 1/1 | **NEW** | Non-periodic critical strikes with Fireball, Frostfire Bolt, Fire Blast, and Scorch reduce the cast time of your next Pyroblast cast within 20 sec by 25%, stacking up to 3 times. Fire Blast grants an additional stack every time it deals damage. |
| **Master of Elements** | 3/3 | changed | Your Fire and Frost critical strikes will refund 30% of their base mana cost. |
| **Critical Mass** | 3/3 | unchanged | Increases the critical strike chance of your Fire spells by 6%. |
| **Fire Power** | 3/3 | unchanged | Increases the damage done by your Fire spells by 3% per your Fire effects on the target, up to a maximum increase of 12%. Effects which mix multiple schools of magic do not qualify. |
| **Combustion** | 1/1 | changed | When activated, this spell causes each of your Fire damage spell hits to increase your critical strike chance with Fire damage spells by 10%. This effect lasts until you have caused 3 non-periodic critical strikes with Fire spells. |

### Frost (3)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Precision** | 3/3 | changed | Improves your chance to hit with all spells by 6%. |

## Core talents (priority order)

1. **Improved Scorch** — 190 DPS lost without it (23% of the build in a full raid; removal, 12,000 fights).
2. **Pyroblast** — 162 DPS lost without it (20% of the build in a full raid; removal, 12,000 fights).
3. **Heating Up** — 144 DPS lost without it (17% of the build in a full raid; removal, 12,000 fights).
4. **Ignite** — 94 DPS lost without it (11% of the build in a full raid; removal, 12,000 fights).
5. **Precision** — 65 DPS lost without it (8% of the build in a full raid; removal, 12,000 fights).
6. **Fire Power** — 52 DPS lost without it (6% of the build in a full raid; removal, 12,000 fights).
7. **Improved Fire Blast** — 47 DPS lost without it (6% of the build in a full raid; removal, 12,000 fights).
8. **Critical Mass** — 43 DPS lost without it (5% of the build in a full raid; removal, 12,000 fights).

## Rank among our builds and the community simulator's

**1 of 9** for `fire-raid` by training-dummy DPS in the community simulator (wowsims/forever 5ad0894 (client 70707)); full ranking and the other builds' rotations: [raid README](../README.md), [raid rotations](../rotation.md).

| Rank | Build | By | Split | Dummy DPS | vs best | Raid DPS | vs best in a raid | Out of mana on the dummy |
|---|---|---|---|---|---|---|---|---|
| 1 | **[`fire-open-raid`](fire-open-raid.md)** | ours: derived (open search) | 17/31/3 | 553 | +0.0% | 828 | +0.0% | 8 s |
| 2 | *Fire* | community simulator | - | 547 | -1.1% | 827 | -0.1% | 12 s |
| 3 | [`opt-fire-raid-raid-dps`](opt-fire-raid-raid-dps.md) | ours: optimizer | 18/31/2 | 542 | -1.9% | 793 | -4.2% | 7 s |
| 4 | [`fire-raid`](fire-raid.md) | ours: hand draft | 16/32/3 | 538 | -2.7% | 799 | -3.5% | 13 s |
| 5 | *FFB* | community simulator | - | 442 | -20.0% | 694 | -16.2% | 41 s |
| 6 | *Arcane Fire* | community simulator | - | 388 | -29.8% | 615 | -25.8% | 1 s |
| 7 | *Arcane* | community simulator | - | 343 | -38.0% | 414 | -50.0% | 1 s |
| 8 | *Frost Incin* | community simulator | - | 317 | -42.7% | 345 | -58.4% | 0 s |
| 9 | *Frost Med* | community simulator | - | 304 | -45.1% | 377 | -54.5% | 0 s |

## Rotation (community simulator, training dummy)

- **The training dummy:** our tuned rotation (`raidsim/apl_opt.py`, 2026-09-27, 5 passes, the last 2026-10-23, 12 changes to the base rotation; third-seed check: open winner 594 -> 652 DPS (+9.8%), opt-fire-raid-raid-dps 597 -> 648 DPS (+8.4%), sim preset: Fire 584 -> 643 DPS (+10.1%), fire-raid 566 -> 623 DPS (+10.1%)):
  1. move to the top: if (stacks of Fire Vulnerability < 5 or time left on Fire Vulnerability ≤ 5s): cast Scorch (+3.1%, pass 1)
  2. drop the condition: if mana ≥ (time left in the fight × 110): cast Fire Blast (+3.1%, pass 1)
  3. insert before the filler: if Missile Barrage is up: cast Arcane Missiles (+0.2%, pass 1)
  4. threshold 20% -> 10%: if mana % < 20% and time left in the fight > 25s: cast Evocation (+0.5%, pass 2)
  5. insert before the filler: cast Fireball (+0.3%, pass 4)
  6. threshold 5s -> 6s: if (stacks of Fire Vulnerability < 5 or time left on Fire Vulnerability ≤ 5s): cast Scorch (+0.3%, pass 4)
  7. only with 3s or more of the fight left: cast Fireball (+0.2%, pass 4)
  8. always rank 10 instead of rank 11: if mana % ≥ 10%: cast Fireball (rank 11) (+4.2%, pass 5)
  9. insert before the filler: cast Robe of the Archmage (+1.9%, pass 5)
  10. threshold 80% -> 60%: if mana % ≤ 80%: cast Mana Ruby (+1.4%, pass 5)
  11. insert at the end: cast Frost Blast (+0.5%, pass 5)
  12. only above 25% mana: if mana % ≤ 60%: cast Mana Ruby (+0.4%, pass 5)
- **A fully buffed raid:** our tuned rotation (`raidsim/apl_opt.py`, 2026-09-27, 14 passes, the last 2026-11-03, 31 changes to the base rotation; third-seed check: fire-open-raid 672 -> 830 DPS (+23.6%), sim preset: Fire 673 -> 827 DPS (+22.9%), fire-raid 665 -> 799 DPS (+20.2%), opt-fire-raid-raid-dps 656 -> 795 DPS (+21.2%)):
  1. drop the condition: if mana ≥ (time left in the fight × 110): cast Fire Blast (+3.7%, pass 1)
  2. move to the top: if (stacks of Fire Vulnerability < 5 or time left on Fire Vulnerability ≤ 5s): cast Scorch (+2.5%, pass 1)
  3. drop: if mana % < 20% and time left in the fight > 25s: cast Evocation (+0.2%, pass 1)
  4. only with 3s or more of the fight left: if mana % ≥ 10%: cast Fireball (+0.2%, pass 2)
  5. move to the top: cast Fire Blast (+0.2%, pass 2)
  6. threshold 5s -> 7.5s: if (stacks of Fire Vulnerability < 5 or time left on Fire Vulnerability ≤ 5s): cast Scorch (+0.4%, pass 2)
  7. insert before the filler: cast Blast Wave (+0.3%, pass 3)
  8. insert before the filler: cast Cone of Cold (+0.3%, pass 3)
  9. insert before the filler: cast Fireball (+0.3%, pass 4)
  10. insert in the middle: if stacks of Heating Up ≥ 2 and (time left in the fight < 6s or time left on Heating Up < 3.5s): cast Pyroblast (+0.2%, pass 5)
  11. drop: cast Fireball (+1.0%, pass 6)
  12. drop 'mana % ≥ 10%' from the condition: if mana % ≥ 10% and time left in the fight ≥ 3s: cast Fireball (+0.4%, pass 6)
  13. insert in the middle: cast Major Mana Potion (+0.3%, pass 6)
  14. move down below 'use every other cooldown when ready': if mana % ≤ 80%: cast Mana Ruby (mana gem) (+0.2%, pass 6)
  15. insert in the middle: if Missile Barrage is up: cast Arcane Missiles (rank 7) (+3.8%, pass 7)
  16. move to the top: if stacks of Heating Up = 3: cast Pyroblast (+0.9%, pass 7)
  17. insert at the end: cast Evocation (+1.4%, pass 8)
  18. insert before the filler: cast Robe of the Archmage (+0.4%, pass 8)
  19. threshold 80% -> 75%: if mana % ≤ 80%: cast Mana Ruby (+0.3%, pass 8)
  20. only above 10% mana: cast Evocation (+0.2%, pass 8)
  21. drop: if mana % ≥ 10%: cast Evocation (+12.4%, pass 9)
  22. threshold 3s -> 4s: if time left in the fight ≥ 3s: cast Fireball (rank 11) (+0.4%, pass 9)
  23. insert at the top: if (stacks of Fire Vulnerability < 5 or time left on Fire Vulnerability < 5) and (stacks of Fire Vulnerability < 4 or not spellIsCasting): cast Scorch (+2.1%, pass 10)
  24. drop '(stacks of Fire Vulnerability < 5 or time left on Fire Vulnerability < 5)' from the condition: if (stacks of Fire Vulnerability < 5 or time left on Fire Vulnerability < 5) and (stacks of Fire Vulnerability < 4 or not spellIsCasting): cast Scorch (+9.1%, pass 10)
  25. insert at the top: if stacks of Heating Up = 3 and not spellIsCasting: cast Pyroblast (+2.2%, pass 10)
  26. move to the top: cast Fire Blast (+1.2%, pass 10)
  27. drop: cast Robe of the Archmage (+0.6%, pass 10)
  28. insert before the filler: if (not Read Leyline is known or not Read Leyline is ready or Energized is up): channel Evocation (interrupt it when a higher line is ready) (+0.4%, pass 10)
  29. rotation replaced by the official simulator's deepFire.apl.json at 54ceac638 (rotation-lag audit after the re-pin) (+2.8%, pass 11)
  30. insert at the top: cast Major Mana Potion (+0.3%, pass 13)
  31. threshold 4 -> 2: if (stacks of Fire Vulnerability < 5 or time left on Fire Vulnerability < 5) and (stacks of Fire Vulnerability < 4 or not spellIsCasting): cast Scorch (+0.2%, pass 14)

| # | Priority (the first line whose condition holds is cast) | [`fire-open-raid`](fire-open-raid.md) casts/min |
|---|---|---|
| 1 | if (stacks of Fire Vulnerability < 5 or time left on Fire Vulnerability ≤ 6s): cast Scorch | 6.9 |
| 2 | if mana % ≤ 60% and mana % ≥ 25%: cast Mana Ruby | as ready |
| 3 | use every other cooldown when ready | as ready |
| 4 | if mana % < 10% and time left in the fight > 25s: cast Evocation | 0.3 |
| 5 | if stacks of Heating Up = 3: cast Pyroblast | 5.0 |
| 6 | cast Fire Blast | 5.7 |
| 7 | if Missile Barrage is up: cast Arcane Missiles (rank 7) | 0.7 |
| 8 | if time left in the fight ≥ 3s: cast Fireball (rank 11) | 5.4 |
| 9 | cast Robe of the Archmage | as ready |
| 10 | cast Scorch | 6.9 |

Lines of the simulator's rotation these builds never cast: cast Fireball (rank 10), cast spell 1326055 (its condition never held in these fights).

Damage by ability:

| Ability | [`fire-open-raid`](fire-open-raid.md) |
|---|---|
| Pyroblast | 32% |
| Fireball | 24% |
| Fire Blast | 17% |
| Scorch | 13% |
| Ignite | 9% |
| Arcane Missiles | 4% |
| Demonic Rune | 2% |

## Notes

- +3.8% over the best hand draft of the spec, fire-raid, over the replacement bar: this build is the spec's raid pick, the hand draft stays as the alternative.
- Open search result (fire-raid, full raid): 17/31/3 (Fire) at 827.1 DPS; fire-open-raid 811.7, fire-raid 796.8, opt-fire-raid-raid-dps 794.5 in the same fights; 2,396 builds simulated, 1 independent runs reached the top.
- The fire-raid raid rotation was re-tuned on this build (a pass in its rotation-search record); the numbers use it.
- Sibling rotations tried on it (10,000 fights): frost-raid -47.3%, arcane-dps -24.8%, frostfire-raid -9.7%; none adopted.
- Talents the simulator measures at 0 DPS in this build (tier fillers; the filler audit may move them): Wand Specialization, Improved Channeling.
- Simulator numbers are the community's model of the beta (wowsims/forever 5ad0894 (client 70707) with this project's patches), not in-game measurements.
- 2026-11-03 filler audit (raidsim/filler_audit.py, user question on zero-value fillers): points the simulator measures at 0 moved, one at a time, to talents that help in a real raid (interrupt protection, threat, mana, range, survival; the simulator cannot see these, so the order is our judgment) or that gain DPS: Improved Channeling -> Arcane Resilience (survival); Improved Channeling -> Arcane Resilience (survival); Improved Channeling -> Arcane Resilience (survival). Net +0.00% on a third seed.

## Open questions (verify in the live game)

- An open-search Fire build: check it against the community's Fire builds at launch.

## Sources

- <https://github.com/ElliotWood/Forever>
- <https://talentsforever.com/mage/60/2302052001002-54500001230133031-003-12>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
