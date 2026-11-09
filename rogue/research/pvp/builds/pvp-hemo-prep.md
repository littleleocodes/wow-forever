# Hemorrhage / Preparation / Thousand Cuts (PvP) — 21/0/30

*[Rogue](../../../README.md) · [PvP](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 21/0/30 (Assassination / Combat / Subtlety) |
| **Role** | DPS — PvP |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70753 (2026-11-03 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |
| **Based on** | Classic baseline `pvp-hemo-prep` |

## Summary

Subtlety went deeper: Preparation now sits at tier 5 with Thousand Cuts (cheaper Hemorrhage/Backstab while Rupture ticks) as the capstone, Premeditation is the 16-point talent, Hemorrhage hits harder with a dagger (145%) and boosts Rupture, and Quietus adds execute damage. Cold Blood and Lethality still come from Assassination.

## Point allocation

### Assassination (21)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Improved Gouge** | 3/3 | changed | Increases the duration of your Gouge ability by 1.5 sec. |
| **Malice** | 5/5 | changed | Increases your critical strike chance with all attacks and Poisons by 5%. |
| **Remorseless Attacks** | 1/2 | changed | After killing a non-trivial enemy, gives you a 20% increased critical strike chance on your next Sinister Strike, Backstab, Ambush, Mutilate, or Ghostly Strike. Lasts 20 sec. |
| **Ruthlessness** | 3/3 | unchanged | Gives your finishing moves a 60% chance to add a Combo Point to your target. |
| **Lethality** | 2/2 | changed | Grants 20% increased Critical Strike damage to your Sinister Strike, Gouge, Backstab, Mutilate, Ghostly Strike, and Hemorrhage abilities. |
| **Vigor** | 2/2 | changed | Increases your maximum Energy by 10. |
| **Cold Blood** | 1/1 | changed | When activated, increases the critical strike chance of your next Sinister Strike, Backstab, Ambush, Eviscerate, or Mutilate by 100%. |
| **Improved Poisons** | 3/5 | changed | Increases the chance to apply Poisons to your target by 6%, and gives Poison applications a 30% chance to not consume a charge. |
| **Relentless Strikes** | 1/5 | unchanged | Your finishing moves have a 4% chance per Combo Point to restore 25 Energy. |

### Combat (0)

*No points.*

### Subtlety (30)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Master of Deception** | 3/3 | changed | Reduces the chance enemies have to detect you while in Stealth mode as if you were 3 levels higher. |
| **Opportunity** | 2/5 | changed | Increases the damage dealt by your Backstab, Garrote, Ambush, and Mutilate abilities by 8%. |
| **Setup** | 3/3 | changed | Gives you a 45% chance to add a Combo Point to your target after Dodging their attack or fully resisting one of their spells. |
| **Camouflage** | 1/3 | changed | Grants 5% increased movement speed in stealth and reduces stealth's cooldown by 2 seconds. |
| **Dirty Deeds** | 2/2 | changed | Reduces the Energy cost of your Cheap Shot and Garrote abilities by 20, and your Garrote ability no longer requires you to be behind your target. |
| **Dirty Tricks** | 2/2 | **NEW** | Reduces the Energy cost of your Sap and Blind abilities by 50%. |
| **Improved Ambush** | 3/3 | moved | Increases the critical strike chance of your Ambush ability by 45%. |
| **Initiative** | 3/3 | changed | Gives you a 100% chance to add an additional combo point to your target when using your Ambush, Garrote, or Cheap Shot ability. |
| **Premeditation** | 1/1 | changed | Adds 2 Combo Points to your target. You must add to or use those combo points within 20 sec or the combo points are lost. |
| **Serrated Blades** | 3/3 | changed | Causes your attacks to ignore 9% of your target's Armor and increases the damage dealt by your Rupture ability by 30%. |
| **Elusiveness** | 2/2 | unchanged | Reduces the cooldown of your Vanish and Blind abilities by 90 sec. |
| **Ghostly Strike** | 1/1 | changed | A strike that deals 125% (180% if a Dagger is equipped in your Main Hand) weapon damage and increases your chance to dodge by 15% for 7 sec. Awards 1 combo point. Also causes your next Ambush or Garrote cast within 7 seconds to not require Stealth. |
| **Heightened Senses** | 2/2 | changed | Increases your Stealth detection as if you were 3 levels higher and reduces your chance to be hit by spells and ranged attacks by 4%. |
| **Hemorrhage** | 1/1 | changed | An instant strike that deals 100% weapon damage (145% if a Dagger is equipped) and increases the damage of the caster's Rupture and Garrote abilities by 15%. Lasts 15 sec. Awards 1 Combo Point. |
| **Preparation** | 1/1 | unchanged | When activated, this ability immediately finishes the cooldown on your other Rogue abilities. |

## Core talents (priority order)

1. **Preparation** — Resets every rogue cooldown (10-minute cooldown in the demo).
2. **Hemorrhage** — 145% weapon damage with a dagger and +15% Rupture damage.
3. **Premeditation** — New 16-point talent for Subtlety: 2 free combo points from stealth.
4. **Cold Blood** — Guaranteed crit.
5. **Improved Ambush** — Ambush crit.
6. **Initiative** — Extra combo point on openers.
7. **Serrated Blades** — Armor ignore and Rupture damage; prerequisite for Hemorrhage.
8. **Dirty Deeds** — Cheaper Cheap Shot/Garrote, Garrote from the front.

## Flex points

| Pts | Default | Alternatives | Why |
|---|---|---|---|
| 3 | Improved Poisons | Vile Poisons, Improved Slice and Dice | Filler to reach Cold Blood. |

## Notes

- Cutthroat (Backstab makes Ambush usable out of stealth) is the alternative tier-6 sink for a dagger-heavy version.
- 2026-11-03 (repair_builds.py, client build 1.60.1.70753 trees): 20/0/31 -> 21/0/30; Murder 2 gone; Lethality 5 -> 2 (rank cap); Improved Distract 1 gone; Quietus 5 gone; Thousand Cuts 1 gone; +1 Improved Gouge (tier gating for Lethality); +1 Improved Gouge (tier gating for Lethality); +1 Improved Gouge (tier gating for Cold Blood); +1 Vigor (tier gating for Cold Blood); +1 Vigor (tier gating for Cold Blood); +1 Remorseless Attacks (tier gating for Relentless Strikes); +1 Dirty Tricks (back into Subtlety); +1 Dirty Tricks (back into Subtlety); +1 Setup (back into Subtlety); +1 Setup (back into Subtlety); +1 Setup (back into Subtlety); +1 Camouflage (back into Subtlety) (refill: the combat-daggers-raid model, pvp).
- 2026-11-09 page audit: core entries for talents the allocation no longer holds removed (Thousand Cuts, Quietus; a tree change or a repair took them out).

## Open questions (verify in the live game)

- Preparation's 10-minute demo cooldown vs. Classic's 10 minutes — confirm; and whether it still resets Cold Blood.

## Sources

- <https://warcraftforever.games/talents/rogue>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
