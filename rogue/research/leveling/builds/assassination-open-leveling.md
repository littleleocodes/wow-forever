# Assassination — Leveling (open talent search) — 31/20/0

*[Rogue](../../../README.md) · [Leveling and solo play](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 31/20/0 (Assassination / Combat / Subtlety) |
| **Role** | DPS — Leveling |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70753 (2026-11-03 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

The Assassination leveling build the open leveling search found on 2026-11-20: every legal 51-point build with no tree rule, searched at level 60 in the fight lab (this project's solo leveling simulator: same-level mobs, eating, drinking and deaths included) playing the combat-daggers-raid rotation, the winner picked by a race at levels 20-60 among the level-60 finalists (fightlab/fl_open_search.py); the talent order is the stats model's (combat-daggers-raid). 

## Point allocation

### Assassination (31)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Remorseless Attacks** | 2/2 | changed | After killing a non-trivial enemy, gives you a 40% increased critical strike chance on your next Sinister Strike, Backstab, Ambush, Mutilate, or Ghostly Strike. Lasts 20 sec. |
| **Malice** | 5/5 | changed | Increases your critical strike chance with all attacks and Poisons by 5%. |
| **Ruthlessness** | 3/3 | unchanged | Gives your finishing moves a 60% chance to add a Combo Point to your target. |
| **Vigor** | 2/2 | changed | Increases your maximum Energy by 10. |
| **Blood Splatter** | 1/1 | **NEW** | Increases the duration of your Rupture ability by 6 seconds and your Garrote ability by 9 seconds. |
| **Lethality** | 2/2 | changed | Grants 20% increased Critical Strike damage to your Sinister Strike, Gouge, Backstab, Mutilate, Ghostly Strike, and Hemorrhage abilities. |
| **Cold Blood** | 1/1 | changed | When activated, increases the critical strike chance of your next Sinister Strike, Backstab, Ambush, Eviscerate, or Mutilate by 100%. |
| **Improved Poisons** | 5/5 | changed | Increases the chance to apply Poisons to your target by 10%, and gives Poison applications a 50% chance to not consume a charge. |
| **Relentless Strikes** | 5/5 | unchanged | Your finishing moves have a 20% chance per Combo Point to restore 25 Energy. |
| **Venom** | 1/1 | **NEW** | Causes your Shank ability to increase your Poison damage by 30% and your chance to apply Poisons by 20% for 6 seconds. |
| **Seal Fate** | 3/3 | moved | Your critical strikes from abilities that add Combo Points have a 100% chance to add an additional Combo Point. |
| **Mutilate** | 1/1 | **NEW** | Instantly attacks with both weapons for 90% weapon damage plus an additional amount with each weapon (Blizzard: the amount was also increased). Damage increased by 20% against Poisoned targets. Awards 2 Combo Points. |

### Combat (20)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Coup de Grace** | 3/3 | changed | Increases the damage done by your Eviscerate ability by 20%, and the damage and storage rate of your Death Mark ability by 20%. |
| **Lightning Reflexes** | 2/5 | unchanged | Increases your Dodge chance by 2%. |
| **Puncturing Wounds** | 3/3 | **NEW** | Increases the critical strike chance of your Backstab by 30% and your Mutilate by 15%, and gives Backstab a 45% chance to add an additional Combo Point. |
| **Deflection** | 2/3 | changed | Increases your Parry chance by 4%. |
| **Precision** | 3/3 | changed | Improves your chance to hit by 3%. |
| **Composure** | 2/2 | **NEW** | Increases the Energy cost reduction of your Poised ability by 10. |
| **Flawless Execution** | 1/1 | **NEW** | Reduces the Energy cost of your Eviscerate ability by 15. |
| **Weapon Expertise** | 2/2 | changed | Reduces the chance for your attacks to be Dodged or Parried by 2%. |
| **Aggression** | 2/3 | changed | Increases the damage of Sinister Strike and Eviscerate by 10%. |

### Subtlety (0)

*No points.*

## Leveling order

| Levels | Tree | Talent | Pts | Running total |
|---|---|---|---|---|
| 10-14 | Assassination | Malice | 5 | 5/0/0 |
| 15-17 | Assassination | Ruthlessness | 3 | 8/0/0 |
| 18-19 | Assassination | Remorseless Attacks | 2 | 10/0/0 |
| 20-21 | Assassination | Lethality | 2 | 12/0/0 |
| 22-23 | Assassination | Vigor | 2 | 14/0/0 |
| 24 | Assassination | Blood Splatter | 1 | 15/0/0 |
| 25 | Assassination | Cold Blood | 1 | 16/0/0 |
| 26-29 | Assassination | Improved Poisons | 4 | 20/0/0 |
| 30 | Assassination | Venom | 1 | 21/0/0 |
| 31 | Assassination | Relentless Strikes | 1 | 22/0/0 |
| 32 | Assassination | Improved Poisons | 1 | 23/0/0 |
| 33-34 | Assassination | Relentless Strikes | 2 | 25/0/0 |
| 35-37 | Assassination | Seal Fate | 3 | 28/0/0 |
| 38-39 | Assassination | Relentless Strikes | 2 | 30/0/0 |
| 40 | Assassination | Mutilate | 1 | 31/0/0 |
| 41-42 | Combat | Lightning Reflexes | 2 | 31/2/0 |
| 43-45 | Combat | Coup de Grace | 3 | 31/5/0 |
| 46-48 | Combat | Puncturing Wounds | 3 | 31/8/0 |
| 49-51 | Combat | Precision | 3 | 31/11/0 |
| 52-53 | Combat | Deflection | 2 | 31/13/0 |
| 54-55 | Combat | Composure | 2 | 31/15/0 |
| 56 | Combat | Flawless Execution | 1 | 31/16/0 |
| 57-58 | Combat | Aggression | 2 | 31/18/0 |
| 59-60 | Combat | Weapon Expertise | 2 | 31/20/0 |

## Core talents (priority order)

1. **Mutilate** — +2.4 s per kill at level 60 without it (removal, 3,000 fights).
2. **Flawless Execution** — +1.3 s per kill at level 60 without it (removal, 3,000 fights).
3. **Venom** — +1.2 s per kill at level 60 without it (removal, 3,000 fights).
4. **Relentless Strikes** — +1.0 s per kill at level 60 without it (removal, 3,000 fights).
5. **Coup de Grace** — +0.9 s per kill at level 60 without it (removal, 3,000 fights).
6. **Seal Fate** — +0.9 s per kill at level 60 without it (removal, 3,000 fights).
7. **Weapon Expertise** — +0.8 s per kill at level 60 without it (removal, 3,000 fights).
8. **Remorseless Attacks** — +0.8 s per kill at level 60 without it (removal, 3,000 fights).

## Leveling rotation

Not simulated in the fight lab; the class's leveling priority is on the [leveling rotation page](../rotation.md).

## Notes

- 2026-11-16: leveling filler pass (fightlab/fl_filler_pass.py, 1500 fights a level): points that measured nothing, or held a tier open, moved: Vile Poisons to Improved Poisons at 26 (gate: -0.1% seed 3, -0.3% seed 4, level-weighted time per kill).
- +6.4% faster than the hand draft leveling-combat-swords, over the replacement bar: this build is the spec's leveling pick, the hand draft stays as the alternative.
- Race at levels 20-60 (seed 3, 3,000 fights per level; level-weighted seconds per kill, lower is faster): this build 21.16; leveling-combat-swords 22.52, opt-combat-swords-raid-leveling-aoe 22.64, opt-combat-swords-raid-leveling-st 22.91, opt-combat-swords-raid-solo-60 22.94, opt-combat-daggers-raid-leveling-st 23.00. The search simulated 64,876 builds.
- The talent order takes the spec's signature talents at the earliest level their tree allows (the signature rule since 2026-11-06, fl_signature.sig_order), then follows the order the fight lab raced fastest.
- Fight-lab numbers are a model of the beta (the assumptions in fightlab/tables.py), not in-game measurements.

## Open questions (verify in the live game)

- An open-search Assassination leveling build: check it while leveling at launch.

## Sources

- <https://talentsforever.com/rogue>
- <https://talentsforever.com/rogue/60/02530021201551031-30232300020122--12>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
