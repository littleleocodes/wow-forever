# Seal Fate / Mutilate Daggers (PvP) — 31/8/12

*[Rogue](../../../README.md) · [PvP](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 31/8/12 (Assassination / Combat / Subtlety) |
| **Role** | DPS — PvP |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70753 (2026-11-03 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |
| **Based on** | Classic baseline `pvp-seal-fate-daggers` |

## Summary

The Classic 30/8/13 maps almost one-to-one: Seal Fate, Cold Blood and Improved Kidney Shot are all still in Assassination, Mutilate slots in as the builder, Puncturing Wounds replaces Improved Backstab, and Subtlety still provides Master of Deception, Opportunity, Elusiveness, Improved Ambush and Initiative.

## Point allocation

### Assassination (31)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Improved Gouge** | 3/3 | changed | Increases the duration of your Gouge ability by 1.5 sec. |
| **Malice** | 5/5 | changed | Increases your critical strike chance with all attacks and Poisons by 5%. |
| **Remorseless Attacks** | 2/2 | changed | After killing a non-trivial enemy, gives you a 40% increased critical strike chance on your next Sinister Strike, Backstab, Ambush, Mutilate, or Ghostly Strike. Lasts 20 sec. |
| **Ruthlessness** | 3/3 | unchanged | Gives your finishing moves a 60% chance to add a Combo Point to your target. |
| **Lethality** | 2/2 | changed | Grants 20% increased Critical Strike damage to your Sinister Strike, Gouge, Backstab, Mutilate, Ghostly Strike, and Hemorrhage abilities. |
| **Vigor** | 2/2 | changed | Increases your maximum Energy by 10. |
| **Cold Blood** | 1/1 | changed | When activated, increases the critical strike chance of your next Sinister Strike, Backstab, Ambush, Eviscerate, or Mutilate by 100%. |
| **Improved Poisons** | 1/5 | changed | Increases the chance to apply Poisons to your target by 2%, and gives Poison applications a 10% chance to not consume a charge. |
| **Vile Poisons** | 1/5 | moved | Increases the damage dealt by your poisons by 4% and gives your poisons an additional 8% chance to resist dispel effects. |
| **Improved Kidney Shot** | 2/2 | changed | Enemies Stunned by your Kidney Shot ability take 10% increased damage from your poisons and attacks. |
| **Relentless Strikes** | 5/5 | unchanged | Your finishing moves have a 20% chance per Combo Point to restore 25 Energy. |
| **Seal Fate** | 3/3 | moved | Your critical strikes from abilities that add Combo Points have a 100% chance to add an additional Combo Point. |
| **Mutilate** | 1/1 | **NEW** | Instantly attacks with both weapons for 90% weapon damage plus an additional amount with each weapon (Blizzard: the amount was also increased). Damage increased by 20% against Poisoned targets. Awards 2 Combo Points. |

### Combat (8)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Coup de Grace** | 3/3 | changed | Increases the damage done by your Eviscerate ability by 20%, and the damage and storage rate of your Death Mark ability by 20%. |
| **Lightning Reflexes** | 2/5 | unchanged | Increases your Dodge chance by 2%. |
| **Puncturing Wounds** | 3/3 | **NEW** | Increases the critical strike chance of your Backstab by 30% and your Mutilate by 15%, and gives Backstab a 45% chance to add an additional Combo Point. |

### Subtlety (12)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Master of Deception** | 3/3 | changed | Reduces the chance enemies have to detect you while in Stealth mode as if you were 3 levels higher. |
| **Opportunity** | 2/5 | changed | Increases the damage dealt by your Backstab, Garrote, Ambush, and Mutilate abilities by 8%. |
| **Dirty Deeds** | 1/2 | changed | Reduces the Energy cost of your Cheap Shot and Garrote abilities by 10, and your Garrote ability no longer requires you to be behind your target. |
| **Dirty Tricks** | 1/2 | **NEW** | Reduces the Energy cost of your Sap and Blind abilities by 25%. |
| **Improved Ambush** | 3/3 | moved | Increases the critical strike chance of your Ambush ability by 45%. |
| **Initiative** | 1/3 | changed | Gives you a 33% chance to add an additional combo point to your target when using your Ambush, Garrote, or Cheap Shot ability. |
| **Premeditation** | 1/1 | changed | Adds 2 Combo Points to your target. You must add to or use those combo points within 20 sec or the combo points are lost. |

## Core talents (priority order)

1. **Seal Fate** — 100% extra combo point on builder crits at max rank.
2. **Cold Blood** — Guaranteed crit Ambush/Mutilate/Eviscerate.
3. **Improved Kidney Shot** — +10% damage taken during Kidney Shot.
4. **Mutilate** — 2 combo points per use, no positional requirement.
5. **Puncturing Wounds** — Backstab/Mutilate crit.
6. **Lethality** — +30% crit damage.
7. **Improved Ambush** — Ambush crit (now Subtlety tier 2).
8. **Initiative** — Extra combo point on openers.
9. **Elusiveness** — Vanish/Blind cooldowns.

## Flex points

| Pts | Default | Alternatives | Why |
|---|---|---|---|
| 1 | Improved Poisons | Vile Poisons, Improved Expose Armor | Twentieth Assassination point to unlock tier 5. |
| 2 | Remorseless Attacks | Improved Gouge (now Assassination tier 1) | Tier-1 Assassination filler. |

## Notes

- Vigor moved from the Assassination capstone to tier 5 (2 ranks) — cheap +10 energy for every deep-Assassination build.
- 2026-11-03 (repair_builds.py, client build 1.60.1.70753 trees): 30/8/13 -> 31/8/12; Murder 2 gone; Lethality 5 -> 2 (rank cap); Seal Fate 5 -> 3 (rank cap); Improved Eviscerate -> Coup de Grace (renamed); +1 Dirty Deeds (tier gating for Initiative); +1 Dirty Deeds (tier gating for Initiative); +1 Improved Gouge (tier gating for Cold Blood); +1 Premeditation (tier gating for Elusiveness); +1 Dirty Tricks (tier gating for Elusiveness); +1 Improved Gouge (tier gating for Improved Kidney Shot); +1 Improved Gouge (tier gating for Improved Kidney Shot); +1 Vile Poisons (tier gating for Improved Kidney Shot); +1 Relentless Strikes (tier gating for Seal Fate); +1 Relentless Strikes (tier gating for Seal Fate); +1 Relentless Strikes (tier gating for Mutilate); +1 Relentless Strikes (tier gating for Mutilate); -1 Elusiveness (over 51); -1 Elusiveness (over 51); -1 Dirty Deeds (over 51); -1 Initiative (over 51); -1 Initiative (over 51) (refill: the combat-daggers-raid model, pvp).

## Open questions (verify in the live game)

- Whether Venom (capstone) is worth 31 Assassination points in PvP over the Subtlety opener talents.

## Sources

- <https://warcraftforever.games/talents/rogue>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
