# Optimizer — Raid Combat swords: white ~43% (MH 30 / OH 13), Sinister Strike ~30%, Eviscerate ~12%, poisons ~10%, Rupture ~5% (leveling-st) — 33/16/2

*[Rogue](../../../README.md) · [Leveling and solo play](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 33/16/2 (Assassination / Combat / Subtlety) |
| **Role** | DPS — Leveling |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70753 (2026-11-03 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

Produced by the stats model (`_reference/data/scorer/`) for spec model `combat-swords-raid` and profile `leveling-st`: score +31.9% (time-per-kill saved vs. no talents). Every number behind it is in the effect files (tooltip-parsed or hand-entered with its arithmetic); change those, not this build.

## Point allocation

### Assassination (33)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Improved Gouge** | 3/3 | changed | Increases the duration of your Gouge ability by 1.5 sec. |
| **Malice** | 5/5 | changed | Increases your critical strike chance with all attacks and Poisons by 5%. |
| **Remorseless Attacks** | 2/2 | changed | After killing a non-trivial enemy, gives you a 40% increased critical strike chance on your next Sinister Strike, Backstab, Ambush, Mutilate, or Ghostly Strike. Lasts 20 sec. |
| **Improved Expose Armor** | 1/2 | changed | Reduces the Energy cost of your Expose Armor ability by 5, and refunds 1 Combo Point when cast with 5 Combo Points. |
| **Ruthlessness** | 3/3 | unchanged | Gives your finishing moves a 60% chance to add a Combo Point to your target. |
| **Lethality** | 2/2 | changed | Grants 20% increased Critical Strike damage to your Sinister Strike, Gouge, Backstab, Mutilate, Ghostly Strike, and Hemorrhage abilities. |
| **Vigor** | 2/2 | changed | Increases your maximum Energy by 10. |
| **Cold Blood** | 1/1 | changed | When activated, increases the critical strike chance of your next Sinister Strike, Backstab, Ambush, Eviscerate, or Mutilate by 100%. |
| **Improved Poisons** | 5/5 | changed | Increases the chance to apply Poisons to your target by 10%, and gives Poison applications a 50% chance to not consume a charge. |
| **Vile Poisons** | 5/5 | moved | Increases the damage dealt by your poisons by 20% and gives your poisons an additional 40% chance to resist dispel effects. |
| **Relentless Strikes** | 1/5 | unchanged | Your finishing moves have a 4% chance per Combo Point to restore 25 Energy. |
| **Seal Fate** | 3/3 | moved | Your critical strikes from abilities that add Combo Points have a 100% chance to add an additional Combo Point. |

### Combat (16)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Coup de Grace** | 3/3 | changed | Increases the damage done by your Eviscerate ability by 20%, and the damage and storage rate of your Death Mark ability by 20%. |
| **Efficient Strikes** | 2/2 | unchanged | Reduces the Energy costs of Sinister Strike and Hemorrhage by 5. |
| **Lightning Reflexes** | 3/5 | unchanged | Increases your Dodge chance by 3%. |
| **Deflection** | 3/3 | changed | Increases your Parry chance by 6%. |
| **Precision** | 3/3 | changed | Improves your chance to hit by 3%. |
| **Riposte** | 1/1 | unchanged | A strike that becomes active after parrying an opponent's attack. This attack deals 150% weapon damage and disarms the target for 6 sec. |
| **Flawless Execution** | 1/1 | **NEW** | Reduces the Energy cost of your Eviscerate ability by 15. |

### Subtlety (2)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Opportunity** | 2/5 | changed | Increases the damage dealt by your Backstab, Garrote, Ambush, and Mutilate abilities by 8%. |

## Core talents (priority order)

1. **Seal Fate** — Removing it costs 3.3 points of score in this model.
2. **Riposte** — Removing it costs 3.0 points of score in this model.
3. **Malice** — Removing it costs 2.4 points of score in this model.
4. **Improved Poisons** — Removing it costs 1.9 points of score in this model.
5. **Flawless Execution** — Removing it costs 1.8 points of score in this model.
6. **Improved Sinister Strike** — Removing it costs 1.8 points of score in this model.
7. **Precision** — Removing it costs 1.8 points of score in this model.
8. **Relentless Strikes** — Removing it costs 1.7 points of score in this model.

## Leveling rotation (fight lab)

Single-target leveling fights against normal mobs of your level with two swords (the daggers models: two daggers, still Sinister Strike: the mob faces you after the opener, so no Backstab): open from stealth behind the mob with Cheap Shot (Garrote before 26; the mob turns to face you after the opener, so it can parry from then on; Poised makes the opener 10 energy cheaper), Slice and Dice at 1-2 points when it is down, Shank whenever its energy would not overflow (from 24), Sinister Strike to 5 points, Eviscerate (Kidney Shot instead when below 60% health, stunning for the tooltip's seconds per point), Eviscerate at fewer points when it would kill the mob, Cold Blood right before a 5-point Eviscerate, Riposte after a parry, Blade Flurry and Adrenaline Rush on the pull, Evasion when low; white swings with both hands (19% extra miss on white dual-wield hits), Instant Poison on the main hand and Deadly Poison on the off hand. Between fights: 2 s loot, 6 s travel, a bandage below 60% health (First Aid, 60 s cooldown), food below 65%; a death costs 90 s. The tuned rules (rotations/rogue-<spec>.json) veto spells and move the thresholds on top of this list.

**Tuned rules** (`fightlab/rotation_opt.py`, 2026-10-26, on top of the priority below): never cast Cheap Shot; eat below 40% health; never cast Slice and Dice; never cast Kidney Shot. Together +16.0% time per kill saved for `opt-combat-daggers-raid-leveling-st` (level-weighted, a third seed of 3000 fights per level).

What this build casts per kill ([report](../fightlab/combat-daggers-raid.md), all leveling builds: [leveling rotations](../rotation.md)):

| Ability | L20 casts/kill | L30 casts/kill | L40 casts/kill | L50 casts/kill | L60 casts/kill | Damage at L60 |
|---|---|---|---|---|---|---|
| Melee | 4.4 | 5.4 | 6.5 | 6.8 | 6.8 | 16% |
| Melee (off-hand) | 3.9 | 4.8 | 6.1 | 6.3 | 6.4 | 8% |
| Sinister Strike | 2.9 | 3.5 | 4.2 | 4.6 | 4.7 | 21% |
| Eviscerate | 0.4 | 0.6 | 1.0 | 1.1 | 1.5 | 27% |
| Garrote | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 | 12% |
| Riposte | 0.0 | 0.6 | 0.8 | 0.9 | 0.9 | 4% |
| Cold Blood | 0.0 | 0.0 | 0.0 | 0.1 | 0.1 | 0% |
| Evasion | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0% |

## Notes

- Report: rogue/research/talents/forever/optimizer/combat-swords-raid-leveling-st.md
- 2026-11-03 (repair_builds.py, client build 1.60.1.70753 trees): 33/16/2 -> 33/16/2; Murder 2 gone; Lethality 4 -> 2 (rank cap); Seal Fate 5 -> 3 (rank cap); Improved Sinister Strike -> Efficient Strikes (renamed); Improved Eviscerate -> Coup de Grace (renamed); +1 Improved Gouge (tier gating for Lethality); +1 Improved Gouge (tier gating for Lethality); +1 Ruthlessness (tier gating for Cold Blood); +1 Ruthlessness (back into Assassination); +1 Ruthlessness (back into Assassination); +1 Improved Expose Armor (back into Assassination); order dropped (order_repair.py) (refill: the combat-swords-raid model, leveling-st).

## Open questions (verify in the live game)

- Hand-entered effect values (see the manual effect file) are the weakest inputs — verify the ones this build leans on.

## Sources

- <https://warcraftforever.games/talents/rogue>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
