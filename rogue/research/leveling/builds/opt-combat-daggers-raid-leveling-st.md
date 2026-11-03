# Optimizer — Raid daggers: white ~40%, Backstab (or Mutilate via talent) ~33%, Eviscerate ~12%, poisons ~10%, Rupture ~5% (leveling-st) — 31/18/2

*[Rogue](../../../README.md) · [Leveling and solo play](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 31/18/2 (Assassination / Combat / Subtlety) |
| **Role** | DPS — Leveling |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70753 (2026-11-03 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

Produced by the stats model (`_reference/data/scorer/`) for spec model `combat-daggers-raid` and profile `leveling-st`: score +36.2% (time-per-kill saved vs. no talents). Every number behind it is in the effect files (tooltip-parsed or hand-entered with its arithmetic); change those, not this build.

## Point allocation

### Assassination (31)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Improved Gouge** | 3/3 | changed | Increases the duration of your Gouge ability by 1.5 sec. |
| **Malice** | 5/5 | changed | Increases your critical strike chance with all attacks and Poisons by 5%. |
| **Remorseless Attacks** | 2/2 | changed | After killing a non-trivial enemy, gives you a 40% increased critical strike chance on your next Sinister Strike, Backstab, Ambush, Mutilate, or Ghostly Strike. Lasts 20 sec. |
| **Improved Expose Armor** | 2/2 | changed | Reduces the Energy cost of your Expose Armor ability by 10, and refunds 2 Combo Points when cast with 5 Combo Points. |
| **Improved Slice and Dice** | 3/3 | unchanged | Increases the duration of your Slice and Dice ability by 45%. |
| **Ruthlessness** | 3/3 | unchanged | Gives your finishing moves a 60% chance to add a Combo Point to your target. |
| **Blood Splatter** | 1/1 | **NEW** | Increases the duration of your Rupture ability by 6 seconds and your Garrote ability by 9 seconds. |
| **Lethality** | 2/2 | changed | Grants 20% increased Critical Strike damage to your Sinister Strike, Gouge, Backstab, Mutilate, Ghostly Strike, and Hemorrhage abilities. |
| **Vigor** | 2/2 | changed | Increases your maximum Energy by 10. |
| **Cold Blood** | 1/1 | changed | When activated, increases the critical strike chance of your next Sinister Strike, Backstab, Ambush, Eviscerate, or Mutilate by 100%. |
| **Vile Poisons** | 2/5 | moved | Increases the damage dealt by your poisons by 8% and gives your poisons an additional 16% chance to resist dispel effects. |
| **Relentless Strikes** | 1/5 | unchanged | Your finishing moves have a 4% chance per Combo Point to restore 25 Energy. |
| **Seal Fate** | 3/3 | moved | Your critical strikes from abilities that add Combo Points have a 100% chance to add an additional Combo Point. |
| **Mutilate** | 1/1 | **NEW** | Instantly attacks with both weapons for 90% weapon damage plus an additional amount with each weapon (Blizzard: the amount was also increased). Damage increased by 20% against Poisoned targets. Awards 2 Combo Points. |

### Combat (18)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Lightning Reflexes** | 5/5 | unchanged | Increases your Dodge chance by 5%. |
| **Deflection** | 3/3 | changed | Increases your Parry chance by 6%. |
| **Precision** | 3/3 | changed | Improves your chance to hit by 3%. |
| **Puncturing Wounds** | 3/3 | **NEW** | Increases the critical strike chance of your Backstab by 30% and your Mutilate by 15%, and gives Backstab a 45% chance to add an additional Combo Point. |
| **Riposte** | 1/1 | unchanged | A strike that becomes active after parrying an opponent's attack. This attack deals 150% weapon damage and disarms the target for 6 sec. |
| **Aggression** | 2/3 | changed | Increases the damage of Sinister Strike and Eviscerate by 10%. |
| **Flawless Execution** | 1/1 | **NEW** | Reduces the Energy cost of your Eviscerate ability by 15. |

### Subtlety (2)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Opportunity** | 2/5 | changed | Increases the damage dealt by your Backstab, Garrote, Ambush, and Mutilate abilities by 8%. |

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

Single-target leveling fights against normal mobs of your level with two swords (the daggers models: two daggers, still Sinister Strike: the mob faces you after the opener, so no Backstab): open from stealth behind the mob with Cheap Shot (Garrote before 26; the mob turns to face you after the opener, so it can parry from then on; Poised makes the opener 10 energy cheaper), Slice and Dice at 1-2 points when it is down, Shank whenever its energy would not overflow (from 24), Sinister Strike to 5 points, Eviscerate (Kidney Shot instead when below 60% health, stunning for the tooltip's seconds per point), Eviscerate at fewer points when it would kill the mob, Cold Blood right before a 5-point Eviscerate, Riposte after a parry, Blade Flurry and Adrenaline Rush on the pull, Evasion when low; white swings with both hands (19% extra miss on white dual-wield hits), Instant Poison on the main hand and Deadly Poison on the off hand. Between fights: 2 s loot, 6 s travel, a bandage below 60% health (First Aid, 60 s cooldown), food below 65%; a death costs 90 s. The tuned rules (rotations/rogue-<spec>.json) veto spells and move the thresholds on top of this list.

**Tuned rules** (`fightlab/rotation_opt.py`, 2026-10-26, on top of the priority below): never cast Cheap Shot; eat below 40% health; never cast Slice and Dice; never cast Kidney Shot. Together +16.0% time per kill saved for `opt-combat-daggers-raid-leveling-st` (level-weighted, a third seed of 3000 fights per level).

What this build casts per kill ([report](../fightlab/combat-daggers-raid.md), all leveling builds: [leveling rotations](../rotation.md)):

| Ability | L20 casts/kill | L30 casts/kill | L40 casts/kill | L50 casts/kill | L60 casts/kill | Damage at L60 |
|---|---|---|---|---|---|---|
| Melee | 7.5 | 8.4 | 10.6 | 10.9 | 11.0 | 19% |
| Melee (off-hand) | 6.9 | 7.8 | 10.2 | 10.5 | 10.6 | 10% |
| Mutilate | 0.0 | 0.0 | 0.0 | 3.1 | 3.2 | 15% |
| Eviscerate | 0.6 | 0.6 | 1.0 | 1.5 | 1.6 | 27% |
| Riposte | 0.0 | 0.8 | 1.1 | 1.2 | 1.2 | 4% |
| Garrote | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 | 13% |
| Kick | 0.3 | 0.3 | 0.3 | 0.3 | 0.2 | 0% |
| Cold Blood | 0.0 | 0.0 | 0.0 | 0.1 | 0.2 | 0% |
| Evasion | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0% |
| Sinister Strike | 3.0 | 3.3 | 4.1 | 0.0 | 0.0 | 0% |

## Notes

- Report: rogue/research/talents/forever/optimizer/combat-daggers-raid-leveling-st.md
- 2026-11-03 (repair_builds.py, client build 1.60.1.70753 trees): 21/28/2 -> 31/18/2; Murder 2 gone; Lethality 5 -> 2 (rank cap); +1 Vigor (tier gating for Cold Blood); +1 Vigor (tier gating for Cold Blood); +1 Remorseless Attacks (tier gating for Relentless Strikes); +1 Remorseless Attacks (tier gating for Relentless Strikes); +1 Improved Slice and Dice (tier gating for Relentless Strikes); +1 Improved Slice and Dice (tier gating for Relentless Strikes); +1 Improved Slice and Dice (tier gating for Mutilate); +1 Improved Expose Armor (tier gating for Mutilate); +1 Improved Expose Armor (tier gating for Mutilate); +1 Blood Splatter (tier gating for Mutilate); +1 Seal Fate (tier gating for Mutilate); +1 Seal Fate (tier gating for Mutilate); +1 Seal Fate (tier gating for Mutilate); +1 Vile Poisons (tier gating for Mutilate); +1 Vile Poisons (tier gating for Mutilate); -1 Dual Wield Specialization (over 51); -1 Dual Wield Specialization (over 51); -1 Endurance (over 51); -1 Hack and Slash (over 51); -1 Hack and Slash (over 51); -1 Hack and Slash (over 51); -1 Hack and Slash (over 51); -1 Hack and Slash (over 51); -1 Endurance (over 51); -1 Aggression (over 51); order dropped (order_repair.py) (refill: the combat-daggers-raid model, leveling-st).

## Open questions (verify in the live game)

- Hand-entered effect values (see the manual effect file) are the weakest inputs — verify the ones this build leans on.

## Sources

- <https://warcraftforever.games/talents/rogue>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
