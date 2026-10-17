# Optimizer — Raid Combat swords: white ~43% (MH 30 / OH 13), Sinister Strike ~30%, Eviscerate ~12%, poisons ~10%, Rupture ~5% (leveling-aoe) — 11/32/8

*[Rogue](../../../README.md) · [Leveling and solo play](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 11/32/8 (Assassination / Combat / Subtlety) |
| **Role** | DPS — Leveling |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70425 (2026-10-16 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

Produced by the stats model (`_reference/data/scorer/`) for spec model `combat-swords-raid` and profile `leveling-aoe`: score +52.2% (time-per-kill saved vs. no talents). Every number behind it is in the effect files (tooltip-parsed or hand-entered with its arithmetic); change those, not this build.

## Point allocation

### Assassination (11)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Malice** | 5/5 | changed | Increases your critical strike chance with all attacks and Poisons by 5%. |
| **Remorseless Attacks** | 2/2 | changed | After killing a non-trivial enemy, gives you a 40% increased critical strike chance on your next Sinister Strike, Backstab, Ambush, Mutilate, or Ghostly Strike. Lasts 20 sec. |
| **Improved Gouge** | 1/3 | changed | Increases the duration of your Gouge ability by 0.5 sec. |
| **Murder** | 2/2 | changed | Increases all damage dealt by 4% against Humanoid and Giant targets. |
| **Relentless Strikes** | 1/1 | unchanged | Your finishing moves have a 20% chance per Combo Point to restore 25 Energy. |

### Combat (32)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Lightning Reflexes** | 2/5 | unchanged | Increases your Dodge chance by 2%. |
| **Improved Sinister Strike** | 2/2 | unchanged | Reduces the Energy cost of your Sinister Strike ability by 5. |
| **Improved Eviscerate** | 3/3 | changed | Increases the damage done by your Eviscerate ability by 20%. |
| **Precision** | 3/3 | changed | Improves your chance to hit by 3%. |
| **Deflection** | 3/3 | changed | Increases your Parry chance by 6%. |
| **Endurance** | 2/2 | changed | Reduces the cooldown of your Sprint and Evasion abilities by 60%. |
| **Riposte** | 1/1 | unchanged | A strike that becomes active after parrying an opponent's attack. This attack deals 150% weapon damage and disarms the target for 6 sec. |
| **Flawless Execution** | 1/1 | **NEW** | Reduces the Energy cost of your Eviscerate ability by 10. |
| **Dual Wield Specialization** | 5/5 | changed | Increases the damage done by your off-hand weapon by 25%. |
| **Blade Flurry** | 1/1 | changed | Increases your melee attack speed by 20% and your melee attacks strike an additional nearby opponent. Lasts 15 sec. |
| **Hack and Slash** | 3/5 | **NEW** | Gives your melee weapon attacks a benefit depending on the weapon.   Axe/Sword: Your successful  melee attacks have a 3% chance  to trigger an extra attack on the   target.   Dagger/Fist: Increases your  critical strike chance by 3%.   Mace: Your attacks ignore 9% of  your target's armor. |
| **Weapon Expertise** | 2/2 | changed | Reduces the chance for your attacks to be Dodged or Parried by 2%. |
| **Aggression** | 3/3 | changed | Increases the damage of your Sinister Strike, Backstab, and Eviscerate abilities by 6%. |
| **Adrenaline Rush** | 1/1 | unchanged | Increases your Energy regeneration rate by 100% for 15 sec. |

### Subtlety (8)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Master of Deception** | 3/3 | changed | Reduces the chance enemies have to detect you while in Stealth mode as if you were 3 levels higher. |
| **Opportunity** | 2/2 | changed | Increases the damage dealt by your Backstab, Garrote, Ambush, and Mutilate abilities by 10%. |
| **Setup** | 3/3 | changed | Gives you a 100% chance to add a Combo Point to your target after Dodging one of their attacks or fully resisting one of their spells. |

## Leveling order

| Levels | Tree | Talent | Pts | Running total |
|---|---|---|---|---|
| 10 | Combat | Lightning Reflexes | 1 | 0/1/0 |
| 11-12 | Combat | Improved Sinister Strike | 2 | 0/3/0 |
| 13 | Combat | Lightning Reflexes | 1 | 0/4/0 |
| 14 | Combat | Improved Eviscerate | 1 | 0/5/0 |
| 15-17 | Combat | Precision | 3 | 0/8/0 |
| 18 | Combat | Deflection | 1 | 0/9/0 |
| 19-20 | Combat | Improved Eviscerate | 2 | 0/11/0 |
| 21-22 | Combat | Endurance | 2 | 0/13/0 |
| 23-24 | Combat | Deflection | 2 | 0/15/0 |
| 25 | Combat | Flawless Execution | 1 | 0/16/0 |
| 26 | Combat | Riposte | 1 | 0/17/0 |
| 27-29 | Combat | Dual Wield Specialization | 3 | 0/20/0 |
| 30 | Combat | Blade Flurry | 1 | 0/21/0 |
| 31-33 | Subtlety | Master of Deception | 3 | 0/21/3 |
| 34-35 | Subtlety | Opportunity | 2 | 0/21/5 |
| 36-38 | Subtlety | Setup | 3 | 0/21/8 |
| 39-40 | Combat | Dual Wield Specialization | 2 | 0/23/8 |
| 41-42 | Combat | Hack and Slash | 2 | 0/25/8 |
| 43-44 | Combat | Weapon Expertise | 2 | 0/27/8 |
| 45-49 | Assassination | Malice | 5 | 5/27/8 |
| 50-51 | Assassination | Murder | 2 | 7/27/8 |
| 52-53 | Assassination | Remorseless Attacks | 2 | 9/27/8 |
| 54 | Assassination | Improved Gouge | 1 | 10/27/8 |
| 55 | Assassination | Relentless Strikes | 1 | 11/27/8 |
| 56-58 | Combat | Aggression | 3 | 11/30/8 |
| 59 | Combat | Adrenaline Rush | 1 | 11/31/8 |
| 60 | Combat | Hack and Slash | 1 | 11/32/8 |

## Core talents (priority order)

1. **Setup** — Removing it costs 6.0 points of score in this model.
2. **Blade Flurry** — Removing it costs 3.5 points of score in this model.
3. **Relentless Strikes** — Removing it costs 2.5 points of score in this model.
4. **Precision** — Removing it costs 2.2 points of score in this model.
5. **Improved Sinister Strike** — Removing it costs 2.1 points of score in this model.
6. **Improved Eviscerate** — Removing it costs 2.0 points of score in this model.
7. **Weapon Expertise** — Removing it costs 2.0 points of score in this model.
8. **Flawless Execution** — Removing it costs 2.0 points of score in this model.

## Leveling rotation (fight lab)

Pulls of several mobs: area attacks when enough mobs stand in reach, then damage over time spread over the pull, else the single-target priority below. Single-target leveling fights against normal mobs of your level with two swords (the daggers models: two daggers, still Sinister Strike: the mob faces you after the opener, so no Backstab): open from stealth behind the mob with Cheap Shot (Garrote before 26; the mob turns to face you after the opener, so it can parry from then on), Slice and Dice at 1-2 points when it is down, Sinister Strike to 5 points, Eviscerate (Kidney Shot instead when below 60% health, stunning for the tooltip's seconds per point), Eviscerate at fewer points when it would kill the mob, Cold Blood right before a 5-point Eviscerate, Riposte after a parry, Blade Flurry and Adrenaline Rush on the pull, Evasion when low; white swings with both hands (19% extra miss on white dual-wield hits), Instant Poison on the main hand and Deadly Poison on the off hand. Between fights: 2 s loot, 6 s travel, a bandage below 60% health (First Aid, 60 s cooldown), food below 65%; a death costs 90 s. The tuned rules (rotations/rogue-<spec>.json) veto spells and move the thresholds on top of this list.

**Tuned rules** (`fightlab/rotation_opt.py`, 2026-10-09, on top of the priority below): never cast Cheap Shot; eat below 40% health; never cast Slice and Dice; never cast Kidney Shot; never cast Kick. Together +15.6% time per kill saved for `leveling-combat-swords` (level-weighted, a third seed of 3000 fights per level).

What this build casts per kill ([report](../fightlab/combat-swords-raid-aoe.md), all leveling builds: [leveling rotations](../rotation.md)):

| Ability | L30 casts/kill | L40 casts/kill | L50 casts/kill | L60 casts/kill | Damage at L60 |
|---|---|---|---|---|---|
| Melee | 5.3 | 6.1 | 6.0 | 6.0 | 17% |
| Melee (off-hand) | 5.0 | 5.9 | 5.9 | 5.8 | 10% |
| Sinister Strike | 3.6 | 3.7 | 3.8 | 4.2 | 22% |
| Eviscerate | 0.9 | 1.6 | 1.6 | 1.7 | 36% |
| Riposte | 0.6 | 0.8 | 0.5 | 0.5 | 3% |
| Garrote | 0.5 | 0.5 | 0.5 | 0.5 | 6% |
| Hack and Slash | 0.0 | 0.0 | 0.3 | 0.4 | 1% |
| Evasion | 0.1 | 0.1 | 0.1 | 0.1 | 0% |

## Notes

- Report: rogue/research/talents/forever/optimizer/combat-swords-raid-leveling-aoe.md

## Open questions (verify in the live game)

- Hand-entered effect values (see the manual effect file) are the weakest inputs — verify the ones this build leans on.

## Sources

- <https://warcraftforever.games/talents/rogue>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
