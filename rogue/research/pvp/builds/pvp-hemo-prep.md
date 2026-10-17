# Hemorrhage / Preparation / Thousand Cuts (PvP) — 20/0/31

*[Rogue](../../../README.md) · [PvP](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 20/0/31 (Assassination / Combat / Subtlety) |
| **Role** | DPS — PvP |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70425 (2026-10-16 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |
| **Based on** | Classic baseline `pvp-hemo-prep` |

## Summary

Subtlety went deeper: Preparation now sits at tier 5 with Thousand Cuts (cheaper Hemorrhage/Backstab while Rupture ticks) as the capstone, Premeditation is the 16-point talent, Hemorrhage hits harder with a dagger (145%) and boosts Rupture, and Quietus adds execute damage. Cold Blood and Lethality still come from Assassination.

## Point allocation

### Assassination (20)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Malice** | 5/5 | changed | Increases your critical strike chance with all attacks and Poisons by 5%. |
| **Ruthlessness** | 3/3 | unchanged | Gives your finishing moves a 60% chance to add a Combo Point to your target. |
| **Murder** | 2/2 | changed | Increases all damage dealt by 4% against Humanoid and Giant targets. |
| **Relentless Strikes** | 1/1 | unchanged | Your finishing moves have a 20% chance per Combo Point to restore 25 Energy. |
| **Lethality** | 5/5 | changed | Increases the critical strike damage bonus of your Sinister Strike, Gouge, Backstab, Mutilate, Ghostly Strike, and Hemorrhage abilities by 20%. |
| **Improved Poisons** | 3/5 | changed | Increases the chance to apply Poisons to your target by 6%, and gives Poison applications a 30% chance to not consume a charge. |
| **Cold Blood** | 1/1 | changed | When activated, increases the critical strike chance of your next Sinister Strike, Backstab, Ambush, Eviscerate, or Mutilate by 100%. |

### Combat (0)

*No points.*

### Subtlety (31)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Master of Deception** | 3/3 | changed | Reduces the chance enemies have to detect you while in Stealth mode as if you were 3 levels higher. |
| **Opportunity** | 2/2 | changed | Increases the damage dealt by your Backstab, Garrote, Ambush, and Mutilate abilities by 10%. |
| **Elusiveness** | 2/2 | unchanged | Reduces the cooldown of your Vanish and Blind abilities by 90 sec. |
| **Improved Ambush** | 3/3 | moved | Increases the critical strike chance of your Ambush ability by 45%. |
| **Initiative** | 3/3 | changed | Gives you a 100% chance to add an additional combo point to your target when using your Ambush, Garrote, or Cheap Shot ability. |
| **Ghostly Strike** | 1/1 | changed | A strike that deals 125% (180% if a Dagger is equipped in your Main Hand) weapon damage and increases your chance to dodge by 15% for 7 sec. Awards 1 combo point. |
| **Improved Distract** | 1/2 | **NEW** | Increases the radius of your Distract ability by 3 yds, and further reduces the Stealth detection of distracted enemies as though they were an additional 1 level lower. |
| **Premeditation** | 1/1 | changed | Adds 2 Combo Points to your target. You must add to or use those combo points within 20 sec or the combo points are lost. |
| **Serrated Blades** | 3/3 | changed | Causes your attacks to ignore 9% of your target's Armor and increases the damage dealt by your Rupture ability by 30%. |
| **Heightened Senses** | 2/2 | changed | Increases your Stealth detection as if you were 3 levels higher and reduces your chance to be hit by spells and ranged attacks by 4%. |
| **Dirty Deeds** | 2/2 | changed | Reduces the Energy cost of your Cheap Shot and Garrote abilities by 20, and your Garrote ability no longer requires you to be behind your target. |
| **Preparation** | 1/1 | unchanged | When activated, this ability immediately finishes the cooldown on your other Rogue abilities. |
| **Hemorrhage** | 1/1 | changed | An instant strike that deals 100% weapon damage (145% if a Dagger is equipped) and causes the target to take 15% increased Rupture damage from the Rogue. Lasts 15 sec. Awards 1 Combo Point. |
| **Quietus** | 5/5 | **NEW** | Your Sinister Strike, Ghostly Strike, and Hemorrhage abilities cause 10% more damage against targets below 35% health. |
| **Thousand Cuts** | 1/1 | **NEW** | When your Rupture ability deals periodic damage, the Energy cost of your next Hemorrhage or Backstab ability within 10 sec is reduced by 3, stacking up to 5 times. |

## Core talents (priority order)

1. **Preparation** — Resets every rogue cooldown (10-minute cooldown in the demo).
2. **Thousand Cuts** — New capstone: Rupture ticks make Hemorrhage/Backstab up to 15 energy cheaper.
3. **Hemorrhage** — 145% weapon damage with a dagger and +15% Rupture damage.
4. **Premeditation** — New 16-point talent for Subtlety: 2 free combo points from stealth.
5. **Cold Blood** — Guaranteed crit.
6. **Improved Ambush** — Ambush crit.
7. **Initiative** — Extra combo point on openers.
8. **Serrated Blades** — Armor ignore and Rupture damage; prerequisite for Hemorrhage.
9. **Dirty Deeds** — Cheaper Cheap Shot/Garrote, Garrote from the front.
10. **Quietus** — +10% Hemorrhage/Sinister Strike/Ghostly Strike damage below 35% (only path to 30 points).

## Flex points

| Pts | Default | Alternatives | Why |
|---|---|---|---|
| 3 | Improved Poisons | Vile Poisons, Improved Slice and Dice | Filler to reach Cold Blood. |
| 3 | Improved Distract 1 + Heightened Senses 2 | Dirty Tricks, Camouflage | Gating fillers in Subtlety tiers 3-4. |

## Notes

- Cutthroat (Backstab makes Ambush usable out of stealth) is the alternative tier-6 sink for a dagger-heavy version.

## Open questions (verify in the live game)

- Preparation's 10-minute demo cooldown vs. Classic's 10 minutes — confirm; and whether it still resets Cold Blood.

## Sources

- <https://warcraftforever.games/talents/rogue>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
