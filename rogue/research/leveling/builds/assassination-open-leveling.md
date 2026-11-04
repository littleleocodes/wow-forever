# Assassination — Leveling (open talent search) — 31/20/0

*[Rogue](../../../README.md) · [Leveling and solo play](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 31/20/0 (Assassination / Combat / Subtlety) |
| **Role** | DPS — Leveling |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70753 (2026-11-03 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

The Assassination leveling build the open leveling search found on 2026-11-03: every legal 51-point build with no tree rule, searched at level 60 in the fight lab (this project's solo leveling simulator: same-level mobs, eating, drinking and deaths included) playing the combat-daggers-raid rotation, the winner picked by a race at levels 20-60 among the level-60 finalists (fightlab/fl_open_search.py); the talent order is the stats model's (combat-daggers-raid). +7.4% faster per kill than leveling-combat-swords, the fastest of our leveling builds in that race.

## Point allocation

### Assassination (31)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Remorseless Attacks** | 2/2 | changed | After killing a non-trivial enemy, gives you a 40% increased critical strike chance on your next Sinister Strike, Backstab, Ambush, Mutilate, or Ghostly Strike. Lasts 20 sec. |
| **Malice** | 5/5 | changed | Increases your critical strike chance with all attacks and Poisons by 5%. |
| **Ruthlessness** | 3/3 | unchanged | Gives your finishing moves a 60% chance to add a Combo Point to your target. |
| **Improved Expose Armor** | 1/2 | changed | Reduces the Energy cost of your Expose Armor ability by 5, and refunds 1 Combo Point when cast with 5 Combo Points. |
| **Vigor** | 2/2 | changed | Increases your maximum Energy by 10. |
| **Lethality** | 2/2 | changed | Grants 20% increased Critical Strike damage to your Sinister Strike, Gouge, Backstab, Mutilate, Ghostly Strike, and Hemorrhage abilities. |
| **Vile Poisons** | 1/5 | moved | Increases the damage dealt by your poisons by 4% and gives your poisons an additional 8% chance to resist dispel effects. |
| **Cold Blood** | 1/1 | changed | When activated, increases the critical strike chance of your next Sinister Strike, Backstab, Ambush, Eviscerate, or Mutilate by 100%. |
| **Improved Poisons** | 4/5 | changed | Increases the chance to apply Poisons to your target by 8%, and gives Poison applications a 40% chance to not consume a charge. |
| **Relentless Strikes** | 5/5 | unchanged | Your finishing moves have a 20% chance per Combo Point to restore 25 Energy. |
| **Venom** | 1/1 | **NEW** | Causes your Shank ability to increase your Poison damage by 30% and your chance to apply Poisons by 20% for 6 seconds. |
| **Seal Fate** | 3/3 | moved | Your critical strikes from abilities that add Combo Points have a 100% chance to add an additional Combo Point. |
| **Mutilate** | 1/1 | **NEW** | Instantly attacks with both weapons for 90% weapon damage plus an additional amount with each weapon (Blizzard: the amount was also increased). Damage increased by 20% against Poisoned targets. Awards 2 Combo Points. |

### Combat (20)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Coup de Grace** | 3/3 | changed | Increases the damage done by your Eviscerate ability by 20%, and the damage and storage rate of your Death Mark ability by 20%. |
| **Efficient Strikes** | 2/2 | unchanged | Reduces the Energy costs of Sinister Strike and Hemorrhage by 5. |
| **Lightning Reflexes** | 2/5 | unchanged | Increases your Dodge chance by 2%. |
| **Puncturing Wounds** | 1/3 | **NEW** | Increases the critical strike chance of your Backstab by 10% and your Mutilate by 5%, and gives Backstab a 15% chance to add an additional Combo Point. |
| **Deflection** | 2/3 | changed | Increases your Parry chance by 4%. |
| **Precision** | 3/3 | changed | Improves your chance to hit by 3%. |
| **Composure** | 2/2 | **NEW** | Increases the Energy cost reduction of your Poised ability by 10. |
| **Flawless Execution** | 1/1 | **NEW** | Reduces the Energy cost of your Eviscerate ability by 15. |
| **Aggression** | 2/3 | changed | Increases the damage of Sinister Strike and Eviscerate by 10%. |
| **Weapon Expertise** | 2/2 | changed | Reduces the chance for your attacks to be Dodged or Parried by 2%. |

### Subtlety (0)

*No points.*

## Leveling order

| Levels | Tree | Talent | Pts | Running total |
|---|---|---|---|---|
| 10-11 | Combat | Lightning Reflexes | 2 | 0/2/0 |
| 12-14 | Combat | Coup de Grace | 3 | 0/5/0 |
| 15 | Combat | Puncturing Wounds | 1 | 0/6/0 |
| 16-18 | Combat | Precision | 3 | 0/9/0 |
| 19 | Combat | Efficient Strikes | 1 | 0/10/0 |
| 20-21 | Combat | Deflection | 2 | 0/12/0 |
| 22-23 | Combat | Composure | 2 | 0/14/0 |
| 24 | Combat | Efficient Strikes | 1 | 0/15/0 |
| 25 | Combat | Flawless Execution | 1 | 0/16/0 |
| 26-27 | Combat | Aggression | 2 | 0/18/0 |
| 28-29 | Combat | Weapon Expertise | 2 | 0/20/0 |
| 30-34 | Assassination | Malice | 5 | 5/20/0 |
| 35-37 | Assassination | Ruthlessness | 3 | 8/20/0 |
| 38-39 | Assassination | Remorseless Attacks | 2 | 10/20/0 |
| 40-41 | Assassination | Vigor | 2 | 12/20/0 |
| 42-43 | Assassination | Lethality | 2 | 14/20/0 |
| 44 | Assassination | Improved Expose Armor | 1 | 15/20/0 |
| 45 | Assassination | Cold Blood | 1 | 16/20/0 |
| 46 | Assassination | Vile Poisons | 1 | 17/20/0 |
| 47-50 | Assassination | Improved Poisons | 4 | 21/20/0 |
| 51-54 | Assassination | Relentless Strikes | 4 | 25/20/0 |
| 55-57 | Assassination | Seal Fate | 3 | 28/20/0 |
| 58 | Assassination | Relentless Strikes | 1 | 29/20/0 |
| 59 | Assassination | Venom | 1 | 30/20/0 |
| 60 | Assassination | Mutilate | 1 | 31/20/0 |

## Core talents (priority order)

1. **Flawless Execution** — +1.4 s per kill at level 60 without it (removal, 3,000 fights).
2. **Mutilate** — +1.2 s per kill at level 60 without it (removal, 3,000 fights).
3. **Venom** — +1.1 s per kill at level 60 without it (removal, 3,000 fights).
4. **Relentless Strikes** — +1.1 s per kill at level 60 without it (removal, 3,000 fights).
5. **Coup de Grace** — +1.0 s per kill at level 60 without it (removal, 3,000 fights).
6. **Weapon Expertise** — +0.9 s per kill at level 60 without it (removal, 3,000 fights).
7. **Remorseless Attacks** — +0.9 s per kill at level 60 without it (removal, 3,000 fights).
8. **Vigor** — +0.9 s per kill at level 60 without it (removal, 3,000 fights).

## Leveling rotation

Not simulated in the fight lab; the class's leveling priority is on the [leveling rotation page](../rotation.md).

## Notes

- +7.4% faster than the hand draft leveling-combat-swords, over the replacement bar: this build is the spec's leveling pick, the hand draft stays as the alternative.
- Race at levels 20-60 (seed 3, 3,000 fights per level; level-weighted seconds per kill, lower is faster): this build 22.47; leveling-combat-swords 24.13, assassination-open-leveling 24.64, opt-combat-swords-raid-leveling-st 24.83, opt-combat-swords-raid-solo-60 24.83, opt-combat-daggers-raid-leveling-st 25.10. The search simulated 64,876 builds.
- Fight-lab numbers are a model of the beta (the assumptions in fightlab/tables.py), not in-game measurements.

## Open questions (verify in the live game)

- An open-search Assassination leveling build: check it while leveling at launch.

## Sources

- <https://talentsforever.com/rogue>
- <https://talentsforever.com/rogue/60/02531020211451031-32212300020122--7>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
