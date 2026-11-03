# Leveling — Combat Swords — 19/32/0

*Rogue · Classic baseline*

| | |
|---|---|
| **Build** | 19/32/0 (Assassination / Combat / Subtlety) |
| **Role** | DPS — Leveling |
| **Status** | Primary |
| **Data** | Classic Era 1.12-era trees (validated against `_reference/data/classic-era-talents.json`) |
| **Forever** | This is the *baseline*; see the Forever status table below and `../forever/` for the adapted build |

## Summary

Combat first for survivability and simple Sinister Strike gameplay (no positioning), Adrenaline Rush at 41, then Assassination. Ends in the exact 19/32/0 raid build so no respec is needed at 60.

## Point allocation

### Assassination (19)

| Talent | Pts | Effect at this rank |
|---|---|---|
| **Improved Eviscerate** | 3/3 | Increases the damage done by your Eviscerate ability by 15%. |
| **Malice** | 5/5 | Increases your critical strike chance by 5%. |
| **Ruthlessness** | 3/3 | Gives your finishing moves a 60% chance to add a combo point to your target. |
| **Murder** | 2/2 | Increases all damage caused against Humanoid, Giant, Beast and Dragonkin targets by 2%. |
| **Improved Slice and Dice** | 3/3 | Increases the duration of your Slice and Dice ability by 45%. |
| **Relentless Strikes** | 1/1 | Your finishing moves have a 20% chance per combo point to restore 25 energy. |
| **Lethality** | 2/5 | Increases the critical strike damage bonus of your Sinister Strike, Gouge, Backstab, Ghostly Strike, and Hemorrhage abilities by 12%. |

### Combat (32)

| Talent | Pts | Effect at this rank |
|---|---|---|
| **Improved Sinister Strike** | 2/2 | Reduces the Energy cost of your Sinister Strike ability by 5. |
| **Lightning Reflexes** | 4/5 | Increases your Dodge chance by 4%. |
| **Precision** | 5/5 | Increases your chance to hit with melee weapons by 5%. |
| **Endurance** | 2/2 | Reduces the cooldown of your Sprint and Evasion abilities by 1.5 min. |
| **Improved Sprint** | 2/2 | Gives a 100% chance to remove all movement impairing effects when you activate your Sprint ability. |
| **Dual Wield Specialization** | 5/5 | Increases the damage done by your offhand weapon by 50%. |
| **Blade Flurry** | 1/1 | Increases your attack speed by 20%. In addition, attacks strike an additional nearby opponent. Lasts 15 sec. |
| **Sword Specialization** | 5/5 | Gives you a 5% chance to get an extra attack on the same target after dealing damage with your Sword. |
| **Weapon Expertise** | 2/2 | Increases your skill with Sword, Fist and Dagger weapons by 5. |
| **Aggression** | 3/3 | Increases the damage of your Sinister Strike and Eviscerate abilities by 6%. |
| **Adrenaline Rush** | 1/1 | Increases your Energy regeneration rate by 100% for 15 sec. |

### Subtlety (0)

*No points.*

## Leveling order

| Levels | Tree | Talent | Pts | Running total |
|---|---|---|---|---|
| 10-11 | Combat | Improved Sinister Strike | 2 | 0/2/0 |
| 12-14 | Combat | Lightning Reflexes | 3 | 0/5/0 |
| 15-19 | Combat | Precision | 5 | 0/10/0 |
| 20 | Combat | Lightning Reflexes | 1 | 0/11/0 |
| 21-22 | Combat | Improved Sprint | 2 | 0/13/0 |
| 23-24 | Combat | Endurance | 2 | 0/15/0 |
| 25-29 | Combat | Dual Wield Specialization | 5 | 0/20/0 |
| 30 | Combat | Blade Flurry | 1 | 0/21/0 |
| 31-35 | Combat | Sword Specialization | 5 | 0/26/0 |
| 36-37 | Combat | Weapon Expertise | 2 | 0/28/0 |
| 38-40 | Combat | Aggression | 3 | 0/31/0 |
| 41 | Combat | Adrenaline Rush | 1 | 0/32/0 |
| 42-46 | Assassination | Malice | 5 | 5/32/0 |
| 47-49 | Assassination | Ruthlessness | 3 | 8/32/0 |
| 50-51 | Assassination | Murder | 2 | 10/32/0 |
| 52-54 | Assassination | Improved Slice and Dice | 3 | 13/32/0 |
| 55 | Assassination | Relentless Strikes | 1 | 14/32/0 |
| 56-58 | Assassination | Improved Eviscerate | 3 | 17/32/0 |
| 59-60 | Assassination | Lethality | 2 | 19/32/0 |

## Core talents (priority order)

1. **Improved Sinister Strike** — Cheaper builder from level 10.
2. **Precision** — Hit is the biggest early damage stat.
3. **Dual Wield Specialization** — Big off-hand damage at 25.
4. **Blade Flurry** — Multi-target leveling cooldown at 30.
5. **Adrenaline Rush** — Energy burst at 41.

## Flex points

| Pts | Default | Alternatives | Why |
|---|---|---|---|
| 5 | Sword Specialization | Dagger Specialization (Backstab leveling), Mace Specialization | Match the weapons you find while leveling; Sword Spec matches the raid end-state. |

## Notes

- Riposte (needs Deflection 5) is a popular leveling alternative to Lightning Reflexes + Endurance; it costs a respec at 60.

## Forever status of every point in this build

Talent-by-talent check against the Forever beta-client trees (`../forever/talent-trees.md`).

| Tree | Talent | Pts | In Forever | Detail |
|---|---|---|---|---|
| Assassination | Improved Eviscerate | 3 | unknown | not found in Forever data |
| Assassination | Malice | 5 | changed | tier 1, max 5 — tooltip changed |
| Assassination | Ruthlessness | 3 | unchanged | tier 2, max 3 |
| Assassination | Murder | 2 | unknown | not found in Forever data |
| Assassination | Improved Slice and Dice | 3 | unchanged | tier 2, max 3 |
| Assassination | Relentless Strikes | 1 | unchanged | tier 5, max 5 — moved in build 1.60.1.70753: was row 3, col 1; max rank 1 -> 5 in build 1.60.1.70753; tooltip changed in build 1.60.1.70753 (ranks 1, 2, 3, 4, 5) |
| Assassination | Lethality | 2 | changed | tier 3, max 2 — tooltip changed; max rank 5 -> 2 in build 1.60.1.70753; tooltip changed in build 1.60.1.70753 (ranks 1, 2) |
| Combat | Improved Sinister Strike | 2 | unknown | not found in Forever data |
| Combat | Lightning Reflexes | 4 | unchanged | tier 1, max 5 |
| Combat | Precision | 5 | changed | tier 2, max 3 — max rank 5 → 3; tooltip changed |
| Combat | Endurance | 2 | changed | tier 3, max 2 — tooltip changed |
| Combat | Improved Sprint | 2 | unchanged | tier 2, max 2 — moved in build 1.60.1.70753: was row 3, col 4 |
| Combat | Dual Wield Specialization | 5 | changed | tier 5, max 2 — tooltip changed; moved in build 1.60.1.70753: was row 4, col 3; max rank 5 -> 2 in build 1.60.1.70753; tooltip changed in build 1.60.1.70753 (ranks 1, 2) |
| Combat | Blade Flurry | 1 | changed | tier 5, max 1 — tooltip changed |
| Combat | Sword Specialization | 5 | **REMOVED** | removed from Classic |
| Combat | Weapon Expertise | 2 | changed | tier 4, max 2 — tooltip changed; moved in build 1.60.1.70753: was row 6, col 2; prerequisite changed in build 1.60.1.70753: was blade flurry |
| Combat | Aggression | 3 | changed | tier 4, max 3 — tooltip changed; moved in build 1.60.1.70753: was row 6, col 3; tooltip changed in build 1.60.1.70753 (ranks 1, 2, 3) |
| Combat | Adrenaline Rush | 1 | unchanged | tier 7, max 1 |

**5 point(s) of this build no longer exist in Forever** and must be re-spent; see `../forever/README.md` for how they were re-spent.

## Sources

- <https://www.wowhead.com/classic/guide/classes/rogue/leveling-talents>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
