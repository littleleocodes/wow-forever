# Daggers (split) — Leveling (open talent search) — 31/16/4

*[Rogue](../../../README.md) · [Leveling and solo play](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 31/16/4 (Assassination / Combat / Subtlety) |
| **Role** | DPS — Leveling |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70753 (2026-11-03 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

The Daggers (split) (an Assassination/Combat hybrid) leveling build the open leveling search found on 2026-11-02: every legal 51-point build with no tree rule, searched at level 60 in the fight lab (this project's solo leveling simulator: same-level mobs, eating, drinking and deaths included) playing the combat-daggers-raid rotation, the winner picked by a race at levels 20-60 among the level-60 finalists (fightlab/fl_open_search.py); the talent order is the stats model's (combat-daggers-raid). +2.4% faster per kill than opt-combat-swords-raid-leveling-st, the fastest of our leveling builds in that race.

## Point allocation

### Assassination (31)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Improved Gouge** | 3/3 | changed | Increases the duration of your Gouge ability by 1.5 sec. |
| **Malice** | 5/5 | changed | Increases your critical strike chance with all attacks and Poisons by 5%. |
| **Remorseless Attacks** | 2/2 | changed | After killing a non-trivial enemy, gives you a 40% increased critical strike chance on your next Sinister Strike, Backstab, Ambush, Mutilate, or Ghostly Strike. Lasts 20 sec. |
| **Improved Expose Armor** | 1/2 | changed | Reduces the Energy cost of your Expose Armor ability by 5, and refunds 1 Combo Point when cast with 5 Combo Points. |
| **Improved Slice and Dice** | 3/3 | unchanged | Increases the duration of your Slice and Dice ability by 45%. |
| **Ruthlessness** | 3/3 | unchanged | Gives your finishing moves a 60% chance to add a Combo Point to your target. |
| **Lethality** | 2/2 | changed | Grants 20% increased Critical Strike damage to your Sinister Strike, Gouge, Backstab, Mutilate, Ghostly Strike, and Hemorrhage abilities. |
| **Vigor** | 2/2 | changed | Increases your maximum Energy by 10. |
| **Cold Blood** | 1/1 | changed | When activated, increases the critical strike chance of your next Sinister Strike, Backstab, Ambush, Eviscerate, or Mutilate by 100%. |
| **Improved Poisons** | 4/5 | changed | Increases the chance to apply Poisons to your target by 8%, and gives Poison applications a 40% chance to not consume a charge. |
| **Relentless Strikes** | 1/5 | unchanged | Your finishing moves have a 4% chance per Combo Point to restore 25 Energy. |
| **Seal Fate** | 3/3 | moved | Your critical strikes from abilities that add Combo Points have a 100% chance to add an additional Combo Point. |
| **Mutilate** | 1/1 | **NEW** | Instantly attacks with both weapons for 90% weapon damage plus an additional amount with each weapon (Blizzard: the amount was also increased). Damage increased by 20% against Poisoned targets. Awards 2 Combo Points. |

### Combat (16)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Coup de Grace** | 3/3 | changed | Increases the damage done by your Eviscerate ability by 20%, and the damage and storage rate of your Death Mark ability by 20%. |
| **Lightning Reflexes** | 5/5 | unchanged | Increases your Dodge chance by 5%. |
| **Deflection** | 3/3 | changed | Increases your Parry chance by 6%. |
| **Precision** | 3/3 | changed | Improves your chance to hit by 3%. |
| **Riposte** | 1/1 | unchanged | A strike that becomes active after parrying an opponent's attack. This attack deals 150% weapon damage and disarms the target for 6 sec. |
| **Flawless Execution** | 1/1 | **NEW** | Reduces the Energy cost of your Eviscerate ability by 15. |

### Subtlety (4)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Master of Deception** | 2/3 | changed | Reduces the chance enemies have to detect you while in Stealth mode as if you were 2 levels higher. |
| **Opportunity** | 2/5 | changed | Increases the damage dealt by your Backstab, Garrote, Ambush, and Mutilate abilities by 8%. |

## Core talents (priority order)

1. **Setup** — +2.4 s per kill at level 60 without it (removal, 3,000 fights).
2. **Improved Eviscerate** — +1.3 s per kill at level 60 without it (removal, 3,000 fights).
3. **Mutilate** — +1.2 s per kill at level 60 without it (removal, 3,000 fights).
4. **Relentless Strikes** — +1.2 s per kill at level 60 without it (removal, 3,000 fights).
5. **Flawless Execution** — +1.1 s per kill at level 60 without it (removal, 3,000 fights).
6. **Initiative** — +0.9 s per kill at level 60 without it (removal, 3,000 fights).
7. **Precision** — +0.8 s per kill at level 60 without it (removal, 3,000 fights).
8. **Malice** — +0.7 s per kill at level 60 without it (removal, 3,000 fights).

## Leveling rotation

Not simulated in the fight lab; the class's leveling priority is on the [leveling rotation page](../rotation.md).

## Notes

- Race at levels 20-60 (seed 3, 3,000 fights per level; level-weighted seconds per kill, lower is faster): this build 25.94; opt-combat-swords-raid-leveling-st 26.55, opt-combat-swords-raid-solo-60 26.55, leveling-combat-swords 26.89. The search simulated 75,937 builds.
- Fight-lab numbers are a model of the beta (the assumptions in fightlab/tables.py), not in-game measurements.
- 2026-11-03 (repair_builds.py, client build 1.60.1.70753 trees): 22/16/13 -> 31/16/4; Murder 2 gone; Improved Eviscerate -> Coup de Grace (renamed); +1 Dirty Deeds (tier gating for Initiative); +1 Vigor (tier gating for Cold Blood); +1 Improved Gouge (tier gating for Cold Blood); +1 Serrated Blades (tier gating for Elusiveness); +1 Serrated Blades (tier gating for Elusiveness); +1 Improved Gouge (tier gating for Mutilate); +1 Improved Gouge (tier gating for Mutilate); +1 Lethality (tier gating for Mutilate); +1 Improved Slice and Dice (tier gating for Mutilate); +1 Improved Slice and Dice (tier gating for Mutilate); +1 Improved Slice and Dice (tier gating for Mutilate); +1 Seal Fate (tier gating for Mutilate); +1 Seal Fate (tier gating for Mutilate); +1 Seal Fate (tier gating for Mutilate); -1 Elusiveness (over 51); -1 Initiative (over 51); -1 Initiative (over 51); -1 Initiative (over 51); -1 Serrated Blades (over 51); -1 Serrated Blades (over 51); -1 Setup (over 51); -1 Setup (over 51); -1 Setup (over 51); -1 Improved Ambush (over 51); -1 Dirty Deeds (over 51); -1 Master of Deception (over 51); order dropped (order_repair.py) (refill: the combat-daggers-raid model, leveling-st).

## Open questions (verify in the live game)

- An open-search Daggers (split) leveling build: check it while leveling at launch.

## Sources

- <https://talentsforever.com/rogue>
- <https://talentsforever.com/rogue/60/02532011101411-30503301001-03231013-7>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
