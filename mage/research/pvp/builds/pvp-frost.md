# Frost (PvP) — 20/0/31

*[Mage](../../../README.md) · [PvP](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 20/0/31 (Arcane / Fire / Frost) |
| **Role** | DPS — PvP |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70009 (2026-09-25 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |
| **Based on** | Classic baseline `pvp-frost` |

## Summary

Shatter (3 ranks), Ice Lance + Fingers of Frost, Frostbite, Permafrost, Improved Cone of Cold, Ice Block (tier 4), Cold Snap and Ice Barrier, with Improved Counterspell and Arcane Meditation from Arcane. Same 20/0/31 shape as Classic with Ice Lance replacing a Piercing Ice/Arctic Reach point.

## Point allocation

### Arcane (20)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Wand Specialization** | 2/2 | moved | Increases your damage with Wands by 25%. |
| **Arcane Focus** | 3/5 | changed | Improves your chance to hit with Arcane spells by 3%. |
| **Arcane Subtlety** | 2/2 | changed | Reduces your target's resistance to all your spells by 15 and reduces the threat caused by your Arcane spells by 30%. |
| **Arcane Concentration** | 5/5 | unchanged | Gives you a 10% chance of entering a Clearcasting state after any damage spell hits a target. The Clearcasting state reduces the mana cost of your next damage spell by 100%. |
| **Arcane Resilience** | 2/2 | changed | Increases your Armor by an amount equal to 50% of your Intellect. |
| **Arcane Blast** | 1/1 | **NEW** | Blasts the target with energy, dealing 57 to 65 Arcane damage. Each time you cast Arcane Blast, the damage of all your other spells is increased by 10% and the mana cost of Arcane Blast is increased by 175%. Effect stacks up to 4 times and lasts 8 sec or until any other damage spell is cast. |
| **Improved Counterspell** | 2/2 | changed | Your Counterspell also Silences the target for 4 sec. |
| **Arcane Meditation** | 3/3 | changed | Allows 50% of your Mana regeneration to continue while casting. |

### Fire (0)

*No points.*

### Frost (31)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Improved Frostbolt** | 5/5 | changed | Reduces the casting time of your Frostbolt spell by 0.5 sec. |
| **Ice Shards** | 5/5 | unchanged | Increases the critical strike damage bonus of your Frost spells by 100%. |
| **Improved Frost Nova** | 2/2 | unchanged | Reduces the cooldown of your Frost Nova spell by 4 sec. |
| **Permafrost** | 3/3 | changed | Increases the duration of your Chill effects by 33% and reduces the target's speed by an additional 10%. |
| **Piercing Ice** | 3/3 | unchanged | Increases the damage done by your Frost spells by 6%. |
| **Ice Lance** | 1/1 | **NEW** | Deals 28 to 32 Frost damage to an enemy target. Deals 300% increased damage to Frozen targets. |
| **Arctic Reach** | 1/2 | unchanged | Increases the range of your Frostbolt and Blizzard spells and the radius of your Frost Nova and Cone of Cold spells by 10%. |
| **Shatter** | 3/3 | changed | Increases the critical strike chance of all your spells against Frozen targets by 50%. |
| **Ice Block** | 1/1 | moved | You become encased in a block of ice, protecting you from all physical attacks and spells for 10 sec, but during that time you cannot attack, move, or cast spells. |
| **Improved Cone of Cold** | 3/3 | changed | Increases the damage dealt by your Cone of Cold spell by 35%. |
| **Cold Snap** | 1/1 | changed | Finishes the remaining cooldown on all your other Frost spells. |
| **Fingers of Frost** | 2/2 | **NEW** | Gives your Chill effects a 15% chance to grant you the Fingers of Frost effect, which treats your next 2 spells cast as if the target were Frozen. Lasts 15 sec. |
| **Ice Barrier** | 1/1 | changed | Instantly shields you, absorbing 447 damage. Lasts 1 min. While the shield holds, your spellcasts will not be interrupted or delayed from taking damage. |

## Core talents (priority order)

1. **Shatter** — Crit vs. Frozen — Frost Nova/Frostbite/Fingers of Frost setups.
2. **Ice Lance** — Instant 300% damage on Frozen targets — the PvP finisher.
3. **Fingers of Frost** — Chills grant a free Shatter cast.
4. **Ice Block** — Immunity, now at 15 points.
5. **Ice Barrier** — Shield; requires Cold Snap.
6. **Cold Snap** — Second Ice Block/Nova; now tier 5.
7. **Improved Counterspell** — 2s silence on Counterspell (demo).
8. **Permafrost** — Chill duration/slow.
9. **Improved Cone of Cold** — Cone of Cold damage.

## Flex points

| Pts | Default | Alternatives | Why |
|---|---|---|---|
| 3 | Piercing Ice | Frostbite 3 | Flat damage vs. random freezes (Frostbite is stronger with Fingers of Frost/Shatter in PvP). |
| 3 | Arcane Resilience 2 + Arcane Blast 1 | Magic Absorption, Arcane Geometry | Arcane gating filler. |

## Notes

- Frostbite 3 in place of Piercing Ice is probably the better PvP choice now that freezes feed Fingers of Frost + Shatter + Ice Lance.

## Open questions (verify in the live game)

- Improved Counterspell's demo silence is 2s (Classic 4s) — check the final value.

## Sources

- <https://warcraftforever.games/talents/mage>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
