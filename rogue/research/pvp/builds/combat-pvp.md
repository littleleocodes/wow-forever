# Combat — PvP (derived) — 3/31/17

*[Rogue](../../../README.md) · [PvP](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 3/31/17 (Assassination / Combat / Subtlety) |
| **Role** | DPS — PvP |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70707 (2026-10-30 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

The Combat PvP build derived on 2026-09-30 (derive_pvp.py): the stats model's PvP optimum with 30+ points in Combat (model combat-swords-raid, profile pvp), then, among builds the model scores within 1% of that, the one the most talentsforever.com Combat builds agree with (5835 builds).

## Point allocation

### Assassination (3)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Improved Gouge** | 3/3 | changed | Increases the duration of your Gouge ability by 1.5 sec. |

### Combat (31)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Improved Eviscerate** | 3/3 | changed | Increases the damage done by your Eviscerate ability by 20%. |
| **Improved Sinister Strike** | 2/2 | unchanged | Reduces the Energy cost of your Sinister Strike ability by 5. |
| **Lightning Reflexes** | 5/5 | unchanged | Increases your Dodge chance by 5%. |
| **Deflection** | 3/3 | changed | Increases your Parry chance by 6%. |
| **Precision** | 3/3 | changed | Improves your chance to hit by 3%. |
| **Endurance** | 2/2 | changed | Reduces the cooldown of your Sprint and Evasion abilities by 60%. |
| **Riposte** | 1/1 | unchanged | A strike that becomes active after parrying an opponent's attack. This attack deals 150% weapon damage and disarms the target for 6 sec. |
| **Improved Sprint** | 2/2 | unchanged | Gives a 100% chance to remove all movement impairing effects when you activate your Sprint ability. |
| **Improved Kick** | 2/2 | unchanged | Gives your Kick ability a 100% chance to Silence the target for 2 sec. |
| **Flawless Execution** | 1/1 | **NEW** | Reduces the Energy cost of your Eviscerate ability by 10. |
| **Blade Flurry** | 1/1 | changed | Increases your melee attack speed by 20% and your melee attacks strike an additional nearby opponent. Lasts 15 sec. |
| **Weapon Expertise** | 2/2 | changed | Reduces the chance for your attacks to be Dodged or Parried by 2%. |
| **Aggression** | 3/3 | changed | Increases the damage of your Sinister Strike, Backstab, and Eviscerate abilities by 6%. |
| **Adrenaline Rush** | 1/1 | unchanged | Increases your Energy regeneration rate by 100% for 15 sec. |

### Subtlety (17)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Master of Deception** | 3/3 | changed | Reduces the chance enemies have to detect you while in Stealth mode as if you were 3 levels higher. |
| **Opportunity** | 2/2 | changed | Increases the damage dealt by your Backstab, Garrote, Ambush, and Mutilate abilities by 10%. |
| **Setup** | 3/3 | changed | Gives you a 100% chance to add a Combo Point to your target after Dodging one of their attacks or fully resisting one of their spells. |
| **Elusiveness** | 2/2 | unchanged | Reduces the cooldown of your Vanish and Blind abilities by 90 sec. |
| **Dirty Tricks** | 1/2 | **NEW** | Reduces the Energy cost of your Sap and Blind abilities by 25%. |
| **Initiative** | 3/3 | changed | Gives you a 100% chance to add an additional combo point to your target when using your Ambush, Garrote, or Cheap Shot ability. |
| **Ghostly Strike** | 1/1 | changed | A strike that deals 125% (180% if a Dagger is equipped in your Main Hand) weapon damage and increases your chance to dodge by 15% for 7 sec. Awards 1 combo point. |
| **Heightened Senses** | 1/2 | changed | Increases your Stealth detection as if you were 1 level higher and reduces your chance to be hit by spells and ranged attacks by 2%. |
| **Premeditation** | 1/1 | changed | Adds 2 Combo Points to your target. You must add to or use those combo points within 20 sec or the combo points are lost. |

## Core talents (priority order)

1. **Adrenaline Rush** — The scorer's value in this build: +9.6% of its score (model combat-swords-raid).
2. **Elusiveness** — The scorer's value in this build: +8.9% of its score (model combat-swords-raid).
3. **Premeditation** — The scorer's value in this build: +8.6% of its score (model combat-swords-raid).
4. **Lightning Reflexes** — The scorer's value in this build: +8.2% of its score (model combat-swords-raid).
5. **Endurance** — The scorer's value in this build: +8.2% of its score (model combat-swords-raid).
6. **Improved Gouge** — The scorer's value in this build: +8.2% of its score (model combat-swords-raid).

## Notes

- Community tie-break moves: 3 points Dual Wield Specialization -> Aggression; 1 point Dirty Tricks -> Setup.
- Where we disagree with the community: most Combat builds take Dual Wield Specialization (97% take it), Hack and Slash (97% take it), Malice (92% take it), Lethality (80% take it), Relentless Strikes (77% take it), Ruthlessness (76% take it), Improved Slice and Dice (76% take it), which the model values below this build's weakest point; this build takes Dirty Tricks (4%), Elusiveness (10%), Ghostly Strike (8%), Heightened Senses (3%), Improved Gouge (7%), Improved Kick (11%), Initiative (7%), Master of Deception (11%), Premeditation (5%), Setup (8%), which few Combat builds take (the model values them). Pick rates cover every level-60 build on the site, not PvP builds only.
- PvP values are assumptions: no simulator plays PvP.

## Open questions (verify in the live game)

- A derived Combat PvP build: check it in duels and battlegrounds at launch.

## Sources

- <https://talentsforever.com/rogue>
- <https://talentsforever.com/popular.js>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
