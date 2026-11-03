# Assassination — PvP (derived) — 31/0/20

*[Rogue](../../../README.md) · [PvP](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 31/0/20 (Assassination / Combat / Subtlety) |
| **Role** | DPS — PvP |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70753 (2026-11-03 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

The Assassination PvP build derived on 2026-09-30 (derive_pvp.py): the stats model's PvP optimum with 30+ points in Assassination (model combat-daggers-raid, profile pvp), then, among builds the model scores within 1% of that, the one the most talentsforever.com Assassination builds agree with (6911 builds).

## Point allocation

### Assassination (31)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Improved Gouge** | 3/3 | changed | Increases the duration of your Gouge ability by 1.5 sec. |
| **Malice** | 4/5 | changed | Increases your critical strike chance with all attacks and Poisons by 4%. |
| **Remorseless Attacks** | 1/2 | changed | After killing a non-trivial enemy, gives you a 20% increased critical strike chance on your next Sinister Strike, Backstab, Ambush, Mutilate, or Ghostly Strike. Lasts 20 sec. |
| **Improved Slice and Dice** | 2/3 | unchanged | Increases the duration of your Slice and Dice ability by 30%. |
| **Ruthlessness** | 3/3 | unchanged | Gives your finishing moves a 60% chance to add a Combo Point to your target. |
| **Vigor** | 2/2 | changed | Increases your maximum Energy by 10. |
| **Cold Blood** | 1/1 | changed | When activated, increases the critical strike chance of your next Sinister Strike, Backstab, Ambush, Eviscerate, or Mutilate by 100%. |
| **Improved Poisons** | 4/5 | changed | Increases the chance to apply Poisons to your target by 8%, and gives Poison applications a 40% chance to not consume a charge. |
| **Improved Kidney Shot** | 2/2 | changed | Enemies Stunned by your Kidney Shot ability take 10% increased damage from your poisons and attacks. |
| **Relentless Strikes** | 5/5 | unchanged | Your finishing moves have a 20% chance per Combo Point to restore 25 Energy. |
| **Seal Fate** | 3/3 | moved | Your critical strikes from abilities that add Combo Points have a 100% chance to add an additional Combo Point. |
| **Mutilate** | 1/1 | **NEW** | Instantly attacks with both weapons for 90% weapon damage plus an additional amount with each weapon (Blizzard: the amount was also increased). Damage increased by 20% against Poisoned targets. Awards 2 Combo Points. |

### Combat (0)

*No points.*

### Subtlety (20)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Master of Deception** | 3/3 | changed | Reduces the chance enemies have to detect you while in Stealth mode as if you were 3 levels higher. |
| **Opportunity** | 2/5 | changed | Increases the damage dealt by your Backstab, Garrote, Ambush, and Mutilate abilities by 8%. |
| **Setup** | 1/3 | changed | Gives you a 15% chance to add a Combo Point to your target after Dodging their attack or fully resisting one of their spells. |
| **Dirty Deeds** | 2/2 | changed | Reduces the Energy cost of your Cheap Shot and Garrote abilities by 20, and your Garrote ability no longer requires you to be behind your target. |
| **Dirty Tricks** | 2/2 | **NEW** | Reduces the Energy cost of your Sap and Blind abilities by 50%. |
| **Improved Ambush** | 3/3 | moved | Increases the critical strike chance of your Ambush ability by 45%. |
| **Initiative** | 3/3 | changed | Gives you a 100% chance to add an additional combo point to your target when using your Ambush, Garrote, or Cheap Shot ability. |
| **Premeditation** | 1/1 | changed | Adds 2 Combo Points to your target. You must add to or use those combo points within 20 sec or the combo points are lost. |
| **Elusiveness** | 2/2 | unchanged | Reduces the cooldown of your Vanish and Blind abilities by 90 sec. |
| **Ghostly Strike** | 1/1 | changed | A strike that deals 125% (180% if a Dagger is equipped in your Main Hand) weapon damage and increases your chance to dodge by 15% for 7 sec. Awards 1 combo point. Also causes your next Ambush or Garrote cast within 7 seconds to not require Stealth. |

## Core talents (priority order)

1. **Mutilate** — The scorer's value in this build: +9.1% of its score (model combat-daggers-raid).
2. **Preparation** — The scorer's value in this build: +8.9% of its score (model combat-daggers-raid).
3. **Seal Fate** — The scorer's value in this build: +7.9% of its score (model combat-daggers-raid).
4. **Elusiveness** — The scorer's value in this build: +7.7% of its score (model combat-daggers-raid).
5. **Premeditation** — The scorer's value in this build: +7.5% of its score (model combat-daggers-raid).
6. **Cold Blood** — The scorer's value in this build: +7.5% of its score (model combat-daggers-raid).

## Notes

- Scores +18.6% of the optimum's talent value above the hand draft pvp-seal-fate-daggers, over the 2% replacement bar: this build is the spec's PvP pick, the hand draft stays as the alternative.
- Community tie-break moves: 2 points Remorseless Attacks -> Improved Slice and Dice; 1 point Improved Poisons -> Vigor.
- Where we disagree with the community: most Assassination builds take Lethality (96% take it), Puncturing Wounds (72% take it), Vile Poisons (71% take it), which the model values below this build's weakest point; this build takes Dirty Tricks (19%), Ghostly Strike (13%), Heightened Senses (14%), Improved Ambush (16%), Preparation (16%), Setup (9%), which few Assassination builds take (the model values them). Pick rates cover every level-60 build on the site, not PvP builds only.
- PvP values are assumptions: no simulator plays PvP.
- 2026-11-03 (repair_builds.py, client build 1.60.1.70753 trees): 30/0/21 -> 31/0/20; Murder 2 gone; Seal Fate 5 -> 3 (rank cap); +1 Remorseless Attacks (tier gating for Cold Blood); +1 Dirty Deeds (tier gating for Heightened Senses); +1 Dirty Deeds (tier gating for Heightened Senses); +1 Relentless Strikes (tier gating for Seal Fate); +1 Relentless Strikes (tier gating for Seal Fate); +1 Relentless Strikes (tier gating for Mutilate); +1 Relentless Strikes (tier gating for Mutilate); -1 Heightened Senses (over 51); -1 Heightened Senses (over 51); -1 Preparation (over 51) (refill: the combat-daggers-raid model, pvp).

## Open questions (verify in the live game)

- A derived Assassination PvP build: check it in duels and battlegrounds at launch.

## Sources

- <https://talentsforever.com/rogue>
- <https://talentsforever.com/popular.js>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
