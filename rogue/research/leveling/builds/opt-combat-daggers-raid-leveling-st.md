# Optimizer — Raid daggers: white ~40%, Backstab (or Mutilate via talent) ~33%, Eviscerate ~12%, poisons ~10%, Rupture ~5% (leveling-st) — 21/28/2

*[Rogue](../../../README.md) · [Leveling and solo play](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 21/28/2 (Assassination / Combat / Subtlety) |
| **Role** | DPS — Leveling |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70425 (2026-10-16 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

Produced by the stats model (`_reference/data/scorer/`) for spec model `combat-daggers-raid` and profile `leveling-st`: score +36.2% (time-per-kill saved vs. no talents). Every number behind it is in the effect files (tooltip-parsed or hand-entered with its arithmetic); change those, not this build.

## Point allocation

### Assassination (21)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Malice** | 5/5 | changed | Increases your critical strike chance with all attacks and Poisons by 5%. |
| **Improved Gouge** | 3/3 | changed | Increases the duration of your Gouge ability by 1.5 sec. |
| **Ruthlessness** | 3/3 | unchanged | Gives your finishing moves a 60% chance to add a Combo Point to your target. |
| **Murder** | 2/2 | changed | Increases all damage dealt by 4% against Humanoid and Giant targets. |
| **Relentless Strikes** | 1/1 | unchanged | Your finishing moves have a 20% chance per Combo Point to restore 25 Energy. |
| **Lethality** | 5/5 | changed | Increases the critical strike damage bonus of your Sinister Strike, Gouge, Backstab, Mutilate, Ghostly Strike, and Hemorrhage abilities by 20%. |
| **Cold Blood** | 1/1 | changed | When activated, increases the critical strike chance of your next Sinister Strike, Backstab, Ambush, Eviscerate, or Mutilate by 100%. |
| **Mutilate** | 1/1 | **NEW** | Instantly attacks with both weapons for 75% weapon damage plus an additional 13 with each weapon. Damage increased by 20% against Poisoned targets. Awards 2 Combo Points. |

### Combat (28)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Lightning Reflexes** | 5/5 | unchanged | Increases your Dodge chance by 5%. |
| **Puncturing Wounds** | 3/3 | **NEW** | Increases the critical strike chance of your Backstab by 30% and your Mutilate by 15%, and gives Backstab a 45% chance to add an additional Combo Point. |
| **Precision** | 3/3 | changed | Improves your chance to hit by 3%. |
| **Deflection** | 3/3 | changed | Increases your Parry chance by 6%. |
| **Endurance** | 2/2 | changed | Reduces the cooldown of your Sprint and Evasion abilities by 60%. |
| **Riposte** | 1/1 | unchanged | A strike that becomes active after parrying an opponent's attack. This attack deals 150% weapon damage and disarms the target for 6 sec. |
| **Flawless Execution** | 1/1 | **NEW** | Reduces the Energy cost of your Eviscerate ability by 10. |
| **Dual Wield Specialization** | 2/5 | changed | Increases the damage done by your off-hand weapon by 10%. |
| **Hack and Slash** | 5/5 | **NEW** | Gives your melee weapon attacks a benefit depending on the weapon.   Axe/Sword: Your successful  melee attacks have a 5% chance  to trigger an extra attack on the   target.   Dagger/Fist: Increases your  critical strike chance by 5%.   Mace: Your attacks ignore 15% of  your target's armor. |
| **Aggression** | 3/3 | changed | Increases the damage of your Sinister Strike, Backstab, and Eviscerate abilities by 6%. |

### Subtlety (2)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Opportunity** | 2/2 | changed | Increases the damage dealt by your Backstab, Garrote, Ambush, and Mutilate abilities by 10%. |

## Leveling order

| Levels | Tree | Talent | Pts | Running total |
|---|---|---|---|---|
| 10-11 | Subtlety | Opportunity | 2 | 0/0/2 |
| 12-16 | Combat | Lightning Reflexes | 5 | 0/5/2 |
| 17-19 | Combat | Puncturing Wounds | 3 | 0/8/2 |
| 20-22 | Combat | Deflection | 3 | 0/11/2 |
| 23 | Combat | Riposte | 1 | 0/12/2 |
| 24-26 | Combat | Precision | 3 | 0/15/2 |
| 27 | Combat | Flawless Execution | 1 | 0/16/2 |
| 28-32 | Assassination | Malice | 5 | 5/16/2 |
| 33-35 | Assassination | Ruthlessness | 3 | 8/16/2 |
| 36-37 | Assassination | Murder | 2 | 10/16/2 |
| 38 | Assassination | Relentless Strikes | 1 | 11/16/2 |
| 39-43 | Assassination | Lethality | 5 | 16/16/2 |
| 44 | Assassination | Cold Blood | 1 | 17/16/2 |
| 45-47 | Assassination | Improved Gouge | 3 | 20/16/2 |
| 48 | Assassination | Mutilate | 1 | 21/16/2 |
| 49-50 | Combat | Endurance | 2 | 21/18/2 |
| 51-52 | Combat | Dual Wield Specialization | 2 | 21/20/2 |
| 53-57 | Combat | Hack and Slash | 5 | 21/25/2 |
| 58-60 | Combat | Aggression | 3 | 21/28/2 |

## Core talents (priority order)

1. **Puncturing Wounds** — Removing it costs 7.6 points of score in this model.
2. **Mutilate** — Removing it costs 4.4 points of score in this model.
3. **Opportunity** — Removing it costs 2.3 points of score in this model.
4. **Flawless Execution** — Removing it costs 1.6 points of score in this model.
5. **Lethality** — Removing it costs 1.5 points of score in this model.
6. **Malice** — Removing it costs 1.4 points of score in this model.
7. **Ruthlessness** — Removing it costs 1.4 points of score in this model.
8. **Relentless Strikes** — Removing it costs 1.4 points of score in this model.

## Leveling rotation (fight lab)

Single-target leveling fights against normal mobs of your level with two swords (the daggers models: two daggers, still Sinister Strike: the mob faces you after the opener, so no Backstab): open from stealth behind the mob with Cheap Shot (Garrote before 26; the mob turns to face you after the opener, so it can parry from then on), Slice and Dice at 1-2 points when it is down, Sinister Strike to 5 points, Eviscerate (Kidney Shot instead when below 60% health, stunning for the tooltip's seconds per point), Eviscerate at fewer points when it would kill the mob, Cold Blood right before a 5-point Eviscerate, Riposte after a parry, Blade Flurry and Adrenaline Rush on the pull, Evasion when low; white swings with both hands (19% extra miss on white dual-wield hits), Instant Poison on the main hand and Deadly Poison on the off hand. Between fights: 2 s loot, 6 s travel, a bandage below 60% health (First Aid, 60 s cooldown), food below 65%; a death costs 90 s. The tuned rules (rotations/rogue-<spec>.json) veto spells and move the thresholds on top of this list.

**Tuned rules** (`fightlab/rotation_opt.py`, 2026-10-23, on top of the priority below): never cast Cheap Shot; eat below 40% health. Together +14.0% time per kill saved for `opt-combat-daggers-raid-leveling-st` (level-weighted, a third seed of 3000 fights per level).

What this build casts per kill ([report](../fightlab/combat-daggers-raid.md), all leveling builds: [leveling rotations](../rotation.md)):

| Ability | L20 casts/kill | L30 casts/kill | L40 casts/kill | L50 casts/kill | L60 casts/kill | Damage at L60 |
|---|---|---|---|---|---|---|
| Melee | 8.1 | 9.2 | 12.0 | 13.9 | 14.7 | 25% |
| Melee (off-hand) | 7.6 | 8.8 | 11.5 | 13.5 | 14.3 | 14% |
| Sinister Strike | 2.5 | 2.9 | 3.7 | 4.0 | 4.3 | 15% |
| Riposte | 0.0 | 0.9 | 1.2 | 1.4 | 1.4 | 4% |
| Slice and Dice | 1.0 | 1.1 | 1.3 | 1.3 | 1.4 | 0% |
| Garrote | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 | 14% |
| Eviscerate | 0.4 | 0.4 | 0.8 | 0.9 | 1.0 | 14% |
| Kick | 0.2 | 0.2 | 0.3 | 0.3 | 0.2 | 0% |
| Cold Blood | 0.0 | 0.0 | 0.0 | 0.1 | 0.1 | 0% |
| Evasion | 0.0 | 0.0 | 0.0 | 0.1 | 0.1 | 0% |
| Kidney Shot | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0% |

## Notes

- Report: rogue/research/talents/forever/optimizer/combat-daggers-raid-leveling-st.md

## Open questions (verify in the live game)

- Hand-entered effect values (see the manual effect file) are the weakest inputs — verify the ones this build leans on.

## Sources

- <https://warcraftforever.games/talents/rogue>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
