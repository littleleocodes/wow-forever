# Optimizer — Raid Combat swords: white ~43% (MH 30 / OH 13), Sinister Strike ~30%, Eviscerate ~12%, poisons ~10%, Rupture ~5% (leveling-aoe) — 21/27/3

*[Rogue](../../../README.md) · [Leveling and solo play](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 21/27/3 (Assassination / Combat / Subtlety) |
| **Role** | DPS — Leveling |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70753 (2026-11-03 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

Produced by the stats model (`_reference/data/scorer/`) for spec model `combat-swords-raid` and profile `leveling-aoe`: score +49.0% (time-per-kill saved vs. no talents). Every number behind it is in the effect files (tooltip-parsed or hand-entered with its arithmetic); change those, not this build.

## Point allocation

### Assassination (21)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Improved Gouge** | 3/3 | changed | Increases the duration of your Gouge ability by 1.5 sec. |
| **Malice** | 5/5 | changed | Increases your critical strike chance with all attacks and Poisons by 5%. |
| **Remorseless Attacks** | 2/2 | changed | After killing a non-trivial enemy, gives you a 40% increased critical strike chance on your next Sinister Strike, Backstab, Ambush, Mutilate, or Ghostly Strike. Lasts 20 sec. |
| **Ruthlessness** | 1/3 | unchanged | Gives your finishing moves a 20% chance to add a Combo Point to your target. |
| **Lethality** | 2/2 | changed | Grants 20% increased Critical Strike damage to your Sinister Strike, Gouge, Backstab, Mutilate, Ghostly Strike, and Hemorrhage abilities. |
| **Vigor** | 2/2 | changed | Increases your maximum Energy by 10. |
| **Cold Blood** | 1/1 | changed | When activated, increases the critical strike chance of your next Sinister Strike, Backstab, Ambush, Eviscerate, or Mutilate by 100%. |
| **Improved Poisons** | 4/5 | changed | Increases the chance to apply Poisons to your target by 8%, and gives Poison applications a 40% chance to not consume a charge. |
| **Relentless Strikes** | 1/5 | unchanged | Your finishing moves have a 4% chance per Combo Point to restore 25 Energy. |

### Combat (27)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Coup de Grace** | 3/3 | changed | Increases the damage done by your Eviscerate ability by 20%, and the damage and storage rate of your Death Mark ability by 20%. |
| **Efficient Strikes** | 1/2 | unchanged | Reduces the Energy costs of Sinister Strike and Hemorrhage by 3. |
| **Lightning Reflexes** | 2/5 | unchanged | Increases your Dodge chance by 2%. |
| **Deflection** | 3/3 | changed | Increases your Parry chance by 6%. |
| **Precision** | 3/3 | changed | Improves your chance to hit by 3%. |
| **Endurance** | 2/2 | changed | Reduces the cooldown of your Sprint and Evasion abilities by 60%. |
| **Riposte** | 1/1 | unchanged | A strike that becomes active after parrying an opponent's attack. This attack deals 150% weapon damage and disarms the target for 6 sec. |
| **Aggression** | 3/3 | changed | Increases the damage of Sinister Strike and Eviscerate by 15%. |
| **Flawless Execution** | 1/1 | **NEW** | Reduces the Energy cost of your Eviscerate ability by 15. |
| **Weapon Expertise** | 2/2 | changed | Reduces the chance for your attacks to be Dodged or Parried by 2%. |
| **Blade Flurry** | 1/1 | changed | Increases your melee attack speed by 20% and your melee attacks strike an additional nearby opponent. Lasts 15 sec. |
| **Hack and Slash** | 5/5 | **NEW** | Gives your melee weapon attacks a benefit depending on the weapon.   Axe/Sword: Your successful  melee attacks have a 5% chance  to trigger an extra attack on the   target.   Dagger/Fist: Increases your  critical strike chance by 5%.   Mace: Your attacks ignore 15% of  your target's armor. |

### Subtlety (3)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Setup** | 3/3 | changed | Gives you a 45% chance to add a Combo Point to your target after Dodging their attack or fully resisting one of their spells. |

## Core talents (priority order)

1. **Setup** — Removing it costs 4.9 points of score in this model.
2. **Blade Flurry** — Removing it costs 4.0 points of score in this model.
3. **Improved Sinister Strike** — Removing it costs 3.1 points of score in this model.
4. **Relentless Strikes** — Removing it costs 2.7 points of score in this model.
5. **Deflection** — Removing it costs 2.5 points of score in this model.
6. **Precision** — Removing it costs 2.3 points of score in this model.
7. **Flawless Execution** — Removing it costs 2.1 points of score in this model.
8. **Improved Eviscerate** — Removing it costs 2.0 points of score in this model.

## Leveling rotation (fight lab)

Pulls of several mobs: area attacks when enough mobs stand in reach, then damage over time spread over the pull, else the single-target priority below. Single-target leveling fights against normal mobs of your level with two swords (the daggers models: two daggers, still Sinister Strike: the mob faces you after the opener, so no Backstab): open from stealth behind the mob with Cheap Shot (Garrote before 26; the mob turns to face you after the opener, so it can parry from then on; Poised makes the opener 10 energy cheaper), Slice and Dice at 1-2 points when it is down, Shank whenever its energy would not overflow (from 24), Sinister Strike to 5 points, Eviscerate (Kidney Shot instead when below 60% health, stunning for the tooltip's seconds per point), Eviscerate at fewer points when it would kill the mob, Cold Blood right before a 5-point Eviscerate, Riposte after a parry, Blade Flurry and Adrenaline Rush on the pull, Evasion when low; white swings with both hands (19% extra miss on white dual-wield hits), Instant Poison on the main hand and Deadly Poison on the off hand. Between fights: 2 s loot, 6 s travel, a bandage below 60% health (First Aid, 60 s cooldown), food below 65%; a death costs 90 s. The tuned rules (rotations/rogue-<spec>.json) veto spells and move the thresholds on top of this list.

**Tuned rules** (`fightlab/rotation_opt.py`, 2026-10-23, on top of the priority below): never cast Cheap Shot; eat below 40% health; never cast Slice and Dice; never cast Kidney Shot; never cast Kick. Together +15.3% time per kill saved for `leveling-combat-swords` (level-weighted, a third seed of 3000 fights per level).

What this build casts per kill ([report](../fightlab/combat-swords-raid-aoe.md), all leveling builds: [leveling rotations](../rotation.md)):

| Ability | L30 casts/kill | L40 casts/kill | L50 casts/kill | L60 casts/kill | Damage at L60 |
|---|---|---|---|---|---|
| Melee | 5.2 | 6.2 | 6.1 | 6.2 | 17% |
| Melee (off-hand) | 5.0 | 6.0 | 5.9 | 6.0 | 10% |
| Sinister Strike | 3.5 | 3.9 | 4.1 | 4.4 | 23% |
| Eviscerate | 0.9 | 1.4 | 1.5 | 1.6 | 33% |
| Hack and Slash | 0.0 | 0.3 | 0.6 | 0.6 | 2% |
| Riposte | 0.7 | 0.8 | 0.5 | 0.5 | 3% |
| Garrote | 0.5 | 0.5 | 0.5 | 0.5 | 6% |
| Evasion | 0.1 | 0.1 | 0.1 | 0.1 | 0% |

## Notes

- Allocation and order taken from cand-aoe-r7 on 2026-10-19: an earlier optimizer round beat the last export in the fight lab (27.3s vs 27.8s per kill, level-weighted).
- Report: rogue/research/talents/forever/optimizer/combat-swords-raid-leveling-aoe.md
- 2026-11-03 (repair_builds.py, client build 1.60.1.70753 trees): 12/31/8 -> 21/27/3; Murder 2 gone; Improved Sinister Strike -> Efficient Strikes (renamed); Improved Eviscerate -> Coup de Grace (renamed); Dual Wield Specialization 4 -> 2 (rank cap); +1 Improved Gouge (tier gating for Lethality); +1 Improved Gouge (tier gating for Lethality); +1 Vigor (tier gating for Relentless Strikes); +1 Vigor (tier gating for Relentless Strikes); +1 Lethality (tier gating for Relentless Strikes); +1 Ruthlessness (tier gating for Relentless Strikes); +1 Cold Blood (tier gating for Relentless Strikes); +1 Improved Poisons (tier gating for Relentless Strikes); +1 Improved Poisons (tier gating for Relentless Strikes); +1 Improved Poisons (tier gating for Relentless Strikes); +1 Improved Poisons (tier gating for Relentless Strikes); +1 Hack and Slash (tier gating for Adrenaline Rush); +1 Lightning Reflexes (tier gating for Adrenaline Rush); -1 Opportunity (over 51); -1 Opportunity (over 51); -1 Master of Deception (over 51); -1 Master of Deception (over 51); -1 Master of Deception (over 51); -1 Adrenaline Rush (over 51); -1 Efficient Strikes (over 51); -1 Dual Wield Specialization (over 51); -1 Dual Wield Specialization (over 51); order dropped (order_repair.py) (refill: the combat-swords-raid model, leveling-aoe).

## Open questions (verify in the live game)

- Hand-entered effect values (see the manual effect file) are the weakest inputs — verify the ones this build leans on.

## Sources

- <https://warcraftforever.games/talents/rogue>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
