# Combat — Leveling (generated) — 21/30/0

*[Rogue](../../../README.md) · [Leveling and solo play](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 21/30/0 (Assassination / Combat / Subtlety) |
| **Role** | DPS — Leveling |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70753 (2026-11-03 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

The best Combat leveling build with at least 30 points in Combat, generated on 2026-09-30 by spec_builds.py: the stats model's optimum (combat-swords-raid, profile leveling-st). No hand draft exists for this spec and mode yet; treat it as a starting point.

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

### Combat (30)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Coup de Grace** | 3/3 | changed | Increases the damage done by your Eviscerate ability by 20%, and the damage and storage rate of your Death Mark ability by 20%. |
| **Efficient Strikes** | 2/2 | unchanged | Reduces the Energy costs of Sinister Strike and Hemorrhage by 5. |
| **Lightning Reflexes** | 5/5 | unchanged | Increases your Dodge chance by 5%. |
| **Deflection** | 3/3 | changed | Increases your Parry chance by 6%. |
| **Precision** | 3/3 | changed | Improves your chance to hit by 3%. |
| **Riposte** | 1/1 | unchanged | A strike that becomes active after parrying an opponent's attack. This attack deals 150% weapon damage and disarms the target for 6 sec. |
| **Aggression** | 3/3 | changed | Increases the damage of Sinister Strike and Eviscerate by 15%. |
| **Flawless Execution** | 1/1 | **NEW** | Reduces the Energy cost of your Eviscerate ability by 15. |
| **Weapon Expertise** | 2/2 | changed | Reduces the chance for your attacks to be Dodged or Parried by 2%. |
| **Blade Flurry** | 1/1 | changed | Increases your melee attack speed by 20% and your melee attacks strike an additional nearby opponent. Lasts 15 sec. |
| **Dual Wield Specialization** | 2/2 | changed | Increases the damage done by your off-hand weapon by 50%. |
| **Hack and Slash** | 4/5 | **NEW** | Gives your melee weapon attacks a benefit depending on the weapon.   Axe/Sword: Your successful  melee attacks have a 4% chance  to trigger an extra attack on the   target.   Dagger/Fist: Increases your  critical strike chance by 4%.   Mace: Your attacks ignore 12% of  your target's armor. |

### Subtlety (0)

*No points.*

## Core talents (priority order)

1. **Riposte** — The scorer's value in this build: +9.0% of its score (model combat-swords-raid).
2. **Weapon Expertise** — The scorer's value in this build: +7.6% of its score (model combat-swords-raid).
3. **Cold Blood** — The scorer's value in this build: +7.5% of its score (model combat-swords-raid).
4. **Malice** — The scorer's value in this build: +7.5% of its score (model combat-swords-raid).
5. **Improved Sinister Strike** — The scorer's value in this build: +5.9% of its score (model combat-swords-raid).
6. **Flawless Execution** — The scorer's value in this build: +5.8% of its score (model combat-swords-raid).

## Leveling rotation

Not simulated in the fight lab; the class's leveling priority is on the [leveling rotation page](../rotation.md).

## Notes

- Generated 2026-09-30 (spec_builds.py) so every spec has a leveling build; model combat-swords-raid, profile leveling-st.
- 2026-11-03 (repair_builds.py, client build 1.60.1.70753 trees): 18/31/2 -> 21/30/0; Murder 2 gone; Lethality 4 -> 2 (rank cap); Improved Eviscerate -> Coup de Grace (renamed); Improved Sinister Strike -> Efficient Strikes (renamed); Dual Wield Specialization 5 -> 2 (rank cap); +1 Improved Gouge (tier gating for Lethality); +1 Improved Gouge (tier gating for Lethality); +1 Vigor (tier gating for Cold Blood); +1 Vigor (tier gating for Cold Blood); +1 Ruthlessness (tier gating for Cold Blood); +1 Improved Poisons (tier gating for Relentless Strikes); +1 Improved Poisons (tier gating for Relentless Strikes); +1 Hack and Slash (tier gating for Adrenaline Rush); +1 Hack and Slash (tier gating for Adrenaline Rush); +1 Hack and Slash (tier gating for Adrenaline Rush); -1 Opportunity (over 51); -1 Opportunity (over 51); -1 Adrenaline Rush (over 51); order dropped (order_repair.py) (refill: the combat-swords-raid model, leveling-st).

## Open questions (verify in the live game)

- A generated Combat build: check it against the community's Combat builds at launch.

## Sources

- <https://talentsforever.com/rogue>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
