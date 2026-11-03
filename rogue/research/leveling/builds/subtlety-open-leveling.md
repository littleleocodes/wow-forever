# Subtlety — Leveling (open talent search) — 21/9/21

*[Rogue](../../../README.md) · [Leveling and solo play](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 21/9/21 (Assassination / Combat / Subtlety) |
| **Role** | DPS — Leveling |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70753 (2026-11-03 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

The Subtlety leveling build the open leveling search found on 2026-11-02: every legal 51-point build with no tree rule, searched at level 60 in the fight lab (this project's solo leveling simulator: same-level mobs, eating, drinking and deaths included) playing the subtlety-leveling rotation, the winner picked by a race at levels 20-60 among the level-60 finalists (fightlab/fl_open_search.py); the talent order is the stats model's (combat-swords-raid). +0.9% faster per kill than subtlety-leveling, the fastest of our leveling builds in that race.

## Point allocation

### Assassination (21)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Improved Gouge** | 3/3 | changed | Increases the duration of your Gouge ability by 1.5 sec. |
| **Malice** | 5/5 | changed | Increases your critical strike chance with all attacks and Poisons by 5%. |
| **Remorseless Attacks** | 2/2 | changed | After killing a non-trivial enemy, gives you a 40% increased critical strike chance on your next Sinister Strike, Backstab, Ambush, Mutilate, or Ghostly Strike. Lasts 20 sec. |
| **Improved Slice and Dice** | 2/3 | unchanged | Increases the duration of your Slice and Dice ability by 30%. |
| **Ruthlessness** | 3/3 | unchanged | Gives your finishing moves a 60% chance to add a Combo Point to your target. |
| **Lethality** | 2/2 | changed | Grants 20% increased Critical Strike damage to your Sinister Strike, Gouge, Backstab, Mutilate, Ghostly Strike, and Hemorrhage abilities. |
| **Vigor** | 2/2 | changed | Increases your maximum Energy by 10. |
| **Cold Blood** | 1/1 | changed | When activated, increases the critical strike chance of your next Sinister Strike, Backstab, Ambush, Eviscerate, or Mutilate by 100%. |
| **Relentless Strikes** | 1/5 | unchanged | Your finishing moves have a 4% chance per Combo Point to restore 25 Energy. |

### Combat (9)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Coup de Grace** | 3/3 | changed | Increases the damage done by your Eviscerate ability by 20%, and the damage and storage rate of your Death Mark ability by 20%. |
| **Lightning Reflexes** | 2/5 | unchanged | Increases your Dodge chance by 2%. |
| **Deflection** | 1/3 | changed | Increases your Parry chance by 2%. |
| **Precision** | 3/3 | changed | Improves your chance to hit by 3%. |

### Subtlety (21)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Master of Deception** | 2/3 | changed | Reduces the chance enemies have to detect you while in Stealth mode as if you were 2 levels higher. |
| **Opportunity** | 2/5 | changed | Increases the damage dealt by your Backstab, Garrote, Ambush, and Mutilate abilities by 8%. |
| **Setup** | 3/3 | changed | Gives you a 45% chance to add a Combo Point to your target after Dodging their attack or fully resisting one of their spells. |
| **Camouflage** | 3/3 | changed | Grants 15% increased movement speed in stealth and reduces stealth's cooldown by 6 seconds. |
| **Improved Ambush** | 3/3 | moved | Increases the critical strike chance of your Ambush ability by 45%. |
| **Initiative** | 3/3 | changed | Gives you a 100% chance to add an additional combo point to your target when using your Ambush, Garrote, or Cheap Shot ability. |
| **Premeditation** | 1/1 | changed | Adds 2 Combo Points to your target. You must add to or use those combo points within 20 sec or the combo points are lost. |
| **Serrated Blades** | 3/3 | changed | Causes your attacks to ignore 9% of your target's Armor and increases the damage dealt by your Rupture ability by 30%. |
| **Ghostly Strike** | 1/1 | changed | A strike that deals 125% (180% if a Dagger is equipped in your Main Hand) weapon damage and increases your chance to dodge by 15% for 7 sec. Awards 1 combo point. Also causes your next Ambush or Garrote cast within 7 seconds to not require Stealth. |

## Core talents (priority order)

1. **Setup** — +1.9 s per kill at level 60 without it (removal, 3,000 fights).
2. **Remorseless Attacks** — +1.5 s per kill at level 60 without it (removal, 3,000 fights).
3. **Improved Eviscerate** — +1.4 s per kill at level 60 without it (removal, 3,000 fights).
4. **Improved Ambush** — +1.2 s per kill at level 60 without it (removal, 3,000 fights).
5. **Relentless Strikes** — +1.1 s per kill at level 60 without it (removal, 3,000 fights).
6. **Precision** — +0.9 s per kill at level 60 without it (removal, 3,000 fights).
7. **Initiative** — +0.9 s per kill at level 60 without it (removal, 3,000 fights).
8. **Malice** — +0.8 s per kill at level 60 without it (removal, 3,000 fights).

## Leveling rotation

Not simulated in the fight lab; the class's leveling priority is on the [leveling rotation page](../rotation.md).

## Notes

- Race at levels 20-60 (seed 3, 3,000 fights per level; level-weighted seconds per kill, lower is faster): this build 25.40; subtlety-leveling 25.64. The search simulated 41,965 builds.
- Fight-lab numbers are a model of the beta (the assumptions in fightlab/tables.py), not in-game measurements.
- 2026-11-03 (repair_builds.py, client build 1.60.1.70753 trees): 12/9/30 -> 21/9/21; Murder 2 gone; Improved Eviscerate -> Coup de Grace (renamed); Camouflage 4 -> 3 (rank cap); Improved Distract 2 gone; Cutthroat 1 gone; +1 Malice (tier gating for Relentless Strikes); +1 Vigor (tier gating for Relentless Strikes); +1 Vigor (tier gating for Relentless Strikes); +1 Improved Gouge (tier gating for Relentless Strikes); +1 Improved Gouge (tier gating for Relentless Strikes); +1 Improved Gouge (tier gating for Relentless Strikes); +1 Cold Blood (tier gating for Relentless Strikes); +1 Lethality (tier gating for Relentless Strikes); +1 Improved Slice and Dice (tier gating for Relentless Strikes); +1 Lethality (tier gating for Relentless Strikes); +1 Improved Slice and Dice (tier gating for Relentless Strikes); -1 Dirty Tricks (over 51); -1 Dirty Tricks (over 51); -1 Hemorrhage (over 51); -1 Heightened Senses (over 51); -1 Heightened Senses (over 51); order dropped (order_repair.py) (refill: the combat-daggers-raid model, leveling-st).

## Open questions (verify in the live game)

- An open-search Subtlety leveling build: check it while leveling at launch.

## Sources

- <https://talentsforever.com/rogue>
- <https://talentsforever.com/rogue/60/0243201-302013-422302331221300101-7>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
