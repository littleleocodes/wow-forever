# Combat — PvP (derived) — 2/31/18

*[Rogue](../../../README.md) · [PvP](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 2/31/18 (Assassination / Combat / Subtlety) |
| **Role** | DPS — PvP |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70753 (2026-11-03 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

The Combat PvP build derived on 2026-09-30 (derive_pvp.py): the stats model's PvP optimum with 30+ points in Combat (model combat-swords-raid, profile pvp), then, among builds the model scores within 1% of that, the one the most talentsforever.com Combat builds agree with (5835 builds).

## Point allocation

### Assassination (2)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Improved Gouge** | 2/3 | changed | Increases the duration of your Gouge ability by 1 sec. |

### Combat (31)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Coup de Grace** | 3/3 | changed | Increases the damage done by your Eviscerate ability by 20%, and the damage and storage rate of your Death Mark ability by 20%. |
| **Efficient Strikes** | 2/2 | unchanged | Reduces the Energy costs of Sinister Strike and Hemorrhage by 5. |
| **Lightning Reflexes** | 5/5 | unchanged | Increases your Dodge chance by 5%. |
| **Deflection** | 3/3 | changed | Increases your Parry chance by 6%. |
| **Improved Sprint** | 2/2 | unchanged | Gives a 100% chance to remove all movement impairing effects when you activate your Sprint ability. |
| **Precision** | 3/3 | changed | Improves your chance to hit by 3%. |
| **Endurance** | 2/2 | changed | Reduces the cooldown of your Sprint and Evasion abilities by 60%. |
| **Riposte** | 1/1 | unchanged | A strike that becomes active after parrying an opponent's attack. This attack deals 150% weapon damage and disarms the target for 6 sec. |
| **Aggression** | 3/3 | changed | Increases the damage of Sinister Strike and Eviscerate by 15%. |
| **Flawless Execution** | 1/1 | **NEW** | Reduces the Energy cost of your Eviscerate ability by 15. |
| **Improved Kick** | 2/2 | unchanged | Gives your Kick ability a 100% chance to Silence the target for 2 sec. |
| **Weapon Expertise** | 2/2 | changed | Reduces the chance for your attacks to be Dodged or Parried by 2%. |
| **Blade Flurry** | 1/1 | changed | Increases your melee attack speed by 20% and your melee attacks strike an additional nearby opponent. Lasts 15 sec. |
| **Adrenaline Rush** | 1/1 | unchanged | Increases your Energy regeneration rate by 100% for 15 sec. |

### Subtlety (18)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Master of Deception** | 3/3 | changed | Reduces the chance enemies have to detect you while in Stealth mode as if you were 3 levels higher. |
| **Setup** | 3/3 | changed | Gives you a 45% chance to add a Combo Point to your target after Dodging their attack or fully resisting one of their spells. |
| **Dirty Deeds** | 2/2 | changed | Reduces the Energy cost of your Cheap Shot and Garrote abilities by 20, and your Garrote ability no longer requires you to be behind your target. |
| **Dirty Tricks** | 2/2 | **NEW** | Reduces the Energy cost of your Sap and Blind abilities by 50%. |
| **Improved Ambush** | 1/3 | moved | Increases the critical strike chance of your Ambush ability by 15%. |
| **Initiative** | 3/3 | changed | Gives you a 100% chance to add an additional combo point to your target when using your Ambush, Garrote, or Cheap Shot ability. |
| **Premeditation** | 1/1 | changed | Adds 2 Combo Points to your target. You must add to or use those combo points within 20 sec or the combo points are lost. |
| **Elusiveness** | 2/2 | unchanged | Reduces the cooldown of your Vanish and Blind abilities by 90 sec. |
| **Ghostly Strike** | 1/1 | changed | A strike that deals 125% (180% if a Dagger is equipped in your Main Hand) weapon damage and increases your chance to dodge by 15% for 7 sec. Awards 1 combo point. Also causes your next Ambush or Garrote cast within 7 seconds to not require Stealth. |

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
- 2026-11-03 (repair_builds.py, client build 1.60.1.70753 trees): 3/31/17 -> 2/31/18; Improved Eviscerate -> Coup de Grace (renamed); Improved Sinister Strike -> Efficient Strikes (renamed); +1 Dirty Deeds (tier gating for Initiative); +1 Dirty Deeds (tier gating for Elusiveness); +1 Dirty Tricks (tier gating for Heightened Senses); +1 Improved Ambush (tier gating for Heightened Senses); -1 Heightened Senses (over 51); -1 Opportunity (over 51); -1 Opportunity (over 51); -1 Improved Gouge (over 51) (refill: the combat-swords-raid model, pvp).

## Open questions (verify in the live game)

- A derived Combat PvP build: check it in duels and battlegrounds at launch.

## Sources

- <https://talentsforever.com/rogue>
- <https://talentsforever.com/popular.js>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
