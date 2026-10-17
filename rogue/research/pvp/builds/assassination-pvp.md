# Assassination — PvP (derived) — 30/0/21

*[Rogue](../../../README.md) · [PvP](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 30/0/21 (Assassination / Combat / Subtlety) |
| **Role** | DPS — PvP |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70425 (2026-10-16 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

The Assassination PvP build derived on 2026-09-30 (derive_pvp.py): the stats model's PvP optimum with 30+ points in Assassination (model combat-daggers-raid, profile pvp), then, among builds the model scores within 1% of that, the one the most talentsforever.com Assassination builds agree with (6911 builds).

## Point allocation

### Assassination (30)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Improved Gouge** | 3/3 | changed | Increases the duration of your Gouge ability by 1.5 sec. |
| **Malice** | 4/5 | changed | Increases your critical strike chance with all attacks and Poisons by 4%. |
| **Ruthlessness** | 3/3 | unchanged | Gives your finishing moves a 60% chance to add a Combo Point to your target. |
| **Murder** | 2/2 | changed | Increases all damage dealt by 4% against Humanoid and Giant targets. |
| **Improved Slice and Dice** | 2/3 | unchanged | Increases the duration of your Slice and Dice ability by 30%. |
| **Relentless Strikes** | 1/1 | unchanged | Your finishing moves have a 20% chance per Combo Point to restore 25 Energy. |
| **Cold Blood** | 1/1 | changed | When activated, increases the critical strike chance of your next Sinister Strike, Backstab, Ambush, Eviscerate, or Mutilate by 100%. |
| **Improved Poisons** | 4/5 | changed | Increases the chance to apply Poisons to your target by 8%, and gives Poison applications a 40% chance to not consume a charge. |
| **Vigor** | 2/2 | changed | Increases your maximum Energy by 10. |
| **Mutilate** | 1/1 | **NEW** | Instantly attacks with both weapons for 75% weapon damage plus an additional 13 with each weapon. Damage increased by 20% against Poisoned targets. Awards 2 Combo Points. |
| **Improved Kidney Shot** | 2/2 | changed | Enemies Stunned by your Kidney Shot ability take 10% increased damage from your poisons and attacks. |
| **Seal Fate** | 5/5 | moved | Your critical strikes from abilities that add Combo Points have a 100% chance to add an additional Combo Point. |

### Combat (0)

*No points.*

### Subtlety (21)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Master of Deception** | 3/3 | changed | Reduces the chance enemies have to detect you while in Stealth mode as if you were 3 levels higher. |
| **Opportunity** | 2/2 | changed | Increases the damage dealt by your Backstab, Garrote, Ambush, and Mutilate abilities by 10%. |
| **Setup** | 1/3 | changed | Gives you a 33% chance to add a Combo Point to your target after Dodging one of their attacks or fully resisting one of their spells. |
| **Elusiveness** | 2/2 | unchanged | Reduces the cooldown of your Vanish and Blind abilities by 90 sec. |
| **Dirty Tricks** | 2/2 | **NEW** | Reduces the Energy cost of your Sap and Blind abilities by 50%. |
| **Improved Ambush** | 3/3 | moved | Increases the critical strike chance of your Ambush ability by 45%. |
| **Initiative** | 3/3 | changed | Gives you a 100% chance to add an additional combo point to your target when using your Ambush, Garrote, or Cheap Shot ability. |
| **Ghostly Strike** | 1/1 | changed | A strike that deals 125% (180% if a Dagger is equipped in your Main Hand) weapon damage and increases your chance to dodge by 15% for 7 sec. Awards 1 combo point. |
| **Heightened Senses** | 2/2 | changed | Increases your Stealth detection as if you were 3 levels higher and reduces your chance to be hit by spells and ranged attacks by 4%. |
| **Premeditation** | 1/1 | changed | Adds 2 Combo Points to your target. You must add to or use those combo points within 20 sec or the combo points are lost. |
| **Preparation** | 1/1 | unchanged | When activated, this ability immediately finishes the cooldown on your other Rogue abilities. |

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

## Open questions (verify in the live game)

- A derived Assassination PvP build: check it in duels and battlegrounds at launch.

## Sources

- <https://talentsforever.com/rogue>
- <https://talentsforever.com/popular.js>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
