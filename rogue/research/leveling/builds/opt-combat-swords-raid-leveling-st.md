# Optimizer — Raid Combat swords: white ~43% (MH 30 / OH 13), Sinister Strike ~30%, Eviscerate ~12%, poisons ~10%, Rupture ~5% (leveling-st) — 33/16/2

*[Rogue](../../../README.md) · [Leveling and solo play](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 33/16/2 (Assassination / Combat / Subtlety) |
| **Role** | DPS — Leveling |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70291 (2026-10-08 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

Produced by the stats model (`_reference/data/scorer/`) for spec model `combat-swords-raid` and profile `leveling-st`: score +32.5% (time-per-kill saved vs. no talents). Every number behind it is in the effect files (tooltip-parsed or hand-entered with its arithmetic); change those, not this build.

## Point allocation

### Assassination (33)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Remorseless Attacks** | 2/2 | changed | After killing a non-trivial enemy, gives you a 40% increased critical strike chance on your next Sinister Strike, Backstab, Ambush, Mutilate, or Ghostly Strike. Lasts 20 sec. |
| **Malice** | 5/5 | changed | Increases your critical strike chance with all attacks and Poisons by 5%. |
| **Improved Gouge** | 1/3 | changed | Increases the duration of your Gouge ability by 0.5 sec. |
| **Murder** | 2/2 | changed | Increases all damage dealt by 4% against Humanoid and Giant targets. |
| **Relentless Strikes** | 1/1 | unchanged | Your finishing moves have a 20% chance per Combo Point to restore 25 Energy. |
| **Lethality** | 4/5 | changed | Increases the critical strike damage bonus of your Sinister Strike, Gouge, Backstab, Mutilate, Ghostly Strike, and Hemorrhage abilities by 16%. |
| **Cold Blood** | 1/1 | changed | When activated, increases the critical strike chance of your next Sinister Strike, Backstab, Ambush, Eviscerate, or Mutilate by 100%. |
| **Improved Poisons** | 5/5 | changed | Increases the chance to apply Poisons to your target by 10%, and gives Poison applications a 50% chance to not consume a charge. |
| **Vile Poisons** | 5/5 | moved | Increases the damage dealt by your poisons by 20% and gives your poisons an additional 40% chance to resist dispel effects. |
| **Vigor** | 2/2 | changed | Increases your maximum Energy by 10. |
| **Seal Fate** | 5/5 | moved | Your critical strikes from abilities that add Combo Points have a 100% chance to add an additional Combo Point. |

### Combat (16)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Improved Sinister Strike** | 2/2 | unchanged | Reduces the Energy cost of your Sinister Strike ability by 5. |
| **Improved Eviscerate** | 3/3 | changed | Increases the damage done by your Eviscerate ability by 20%. |
| **Lightning Reflexes** | 3/5 | unchanged | Increases your Dodge chance by 3%. |
| **Deflection** | 3/3 | changed | Increases your Parry chance by 6%. |
| **Precision** | 3/3 | changed | Improves your chance to hit by 3%. |
| **Riposte** | 1/1 | unchanged | A strike that becomes active after parrying an opponent's attack. This attack deals 150% weapon damage and disarms the target for 6 sec. |
| **Flawless Execution** | 1/1 | **NEW** | Reduces the Energy cost of your Eviscerate ability by 10. |

### Subtlety (2)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Opportunity** | 2/2 | changed | Increases the damage dealt by your Backstab, Garrote, Ambush, and Mutilate abilities by 10%. |

## Leveling order

| Levels | Tree | Talent | Pts | Running total |
|---|---|---|---|---|
| 10-11 | Combat | Improved Sinister Strike | 2 | 0/2/0 |
| 12-13 | Combat | Improved Eviscerate | 2 | 0/4/0 |
| 14-15 | Assassination | Remorseless Attacks | 2 | 2/4/0 |
| 16 | Combat | Improved Eviscerate | 1 | 2/5/0 |
| 17 | Combat | Deflection | 1 | 2/6/0 |
| 18-19 | Combat | Precision | 2 | 2/8/0 |
| 20-21 | Combat | Deflection | 2 | 2/10/0 |
| 22 | Combat | Riposte | 1 | 2/11/0 |
| 23 | Combat | Precision | 1 | 2/12/0 |
| 24-26 | Combat | Lightning Reflexes | 3 | 2/15/0 |
| 27 | Combat | Flawless Execution | 1 | 2/16/0 |
| 28-32 | Assassination | Malice | 5 | 7/16/0 |
| 33-34 | Assassination | Murder | 2 | 9/16/0 |
| 35 | Assassination | Improved Gouge | 1 | 10/16/0 |
| 36 | Assassination | Relentless Strikes | 1 | 11/16/0 |
| 37-40 | Assassination | Lethality | 4 | 15/16/0 |
| 41 | Assassination | Cold Blood | 1 | 16/16/0 |
| 42-45 | Assassination | Improved Poisons | 4 | 20/16/0 |
| 46-47 | Assassination | Vigor | 2 | 22/16/0 |
| 48 | Assassination | Improved Poisons | 1 | 23/16/0 |
| 49-50 | Assassination | Vile Poisons | 2 | 25/16/0 |
| 51-55 | Assassination | Seal Fate | 5 | 30/16/0 |
| 56-57 | Subtlety | Opportunity | 2 | 30/16/2 |
| 58-60 | Assassination | Vile Poisons | 3 | 33/16/2 |

## Core talents (priority order)

1. **Seal Fate** — Removing it costs 3.3 points of score in this model.
2. **Riposte** — Removing it costs 2.9 points of score in this model.
3. **Cold Blood** — Removing it costs 2.4 points of score in this model.
4. **Malice** — Removing it costs 2.3 points of score in this model.
5. **Improved Sinister Strike** — Removing it costs 1.9 points of score in this model.
6. **Flawless Execution** — Removing it costs 1.8 points of score in this model.
7. **Precision** — Removing it costs 1.8 points of score in this model.
8. **Remorseless Attacks** — Removing it costs 1.7 points of score in this model.

## Leveling rotation (fight lab)

Single-target leveling fights against normal mobs of your level with two swords (the daggers models: two daggers, still Sinister Strike: the mob faces you after the opener, so no Backstab): open from stealth behind the mob with Cheap Shot (Garrote before 26; the mob turns to face you after the opener, so it can parry from then on), Slice and Dice at 1-2 points when it is down, Sinister Strike to 5 points, Eviscerate (Kidney Shot instead when below 60% health, stunning for the tooltip's seconds per point), Eviscerate at fewer points when it would kill the mob, Cold Blood right before a 5-point Eviscerate, Riposte after a parry, Blade Flurry and Adrenaline Rush on the pull, Evasion when low; white swings with both hands (19% extra miss on white dual-wield hits), Instant Poison on the main hand and Deadly Poison on the off hand. Between fights: 2 s loot, 6 s travel, a bandage below 60% health (First Aid, 60 s cooldown), food below 65%; a death costs 90 s. The tuned rules (rotations/rogue-<spec>.json) veto spells and move the thresholds on top of this list.

**Tuned rules** (`fightlab/rotation_opt.py`, 2026-09-28, on top of the priority below): never cast Cheap Shot; eat below 40% health; never cast Slice and Dice; never cast Kidney Shot. Together +17.1% time per kill saved for `opt-combat-daggers-raid-leveling-st` (level-weighted, a third seed of 3000 fights per level).

What this build casts per kill ([report](../fightlab/combat-daggers-raid.md), all leveling builds: [leveling rotations](../rotation.md)):

| Ability | L20 casts/kill | L30 casts/kill | L40 casts/kill | L50 casts/kill | L60 casts/kill | Damage at L60 |
|---|---|---|---|---|---|---|
| Melee | 4.4 | 5.4 | 6.6 | 6.8 | 6.9 | 16% |
| Melee (off-hand) | 3.8 | 4.8 | 6.2 | 6.4 | 6.5 | 8% |
| Sinister Strike | 2.9 | 3.5 | 4.3 | 4.7 | 4.8 | 23% |
| Eviscerate | 0.4 | 0.7 | 0.9 | 1.0 | 1.4 | 26% |
| Garrote | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 | 11% |
| Riposte | 0.0 | 0.6 | 0.8 | 0.8 | 0.9 | 4% |
| Evasion | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0% |

## Notes

- Report: rogue/talents/forever/optimizer/combat-swords-raid-leveling-st.md

## Open questions (verify in the live game)

- Hand-entered effect values (see the manual effect file) are the weakest inputs — verify the ones this build leans on.

## Sources

- <https://warcraftforever.games/talents/rogue>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
