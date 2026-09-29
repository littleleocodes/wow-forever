# Frost (PvP) — 20/0/31

*Mage · Classic baseline*

| | |
|---|---|
| **Build** | 20/0/31 (Arcane / Fire / Frost) |
| **Role** | DPS — PvP |
| **Status** | Primary |
| **Data** | Classic Era 1.12-era trees (validated against `_reference/data/classic-era-talents.json`) |
| **Forever** | This is the *baseline*; see the Forever status table below and `../forever/` for the adapted build |

## Summary

The standard Classic PvP mage: Shatter combos, Ice Block, Ice Barrier, Improved Cone of Cold, Permafrost, Cold Snap and Improved Counterspell, with Arcane taken to Arcane Meditation for regen.

## Point allocation

### Arcane (20)

| Talent | Pts | Effect at this rank |
|---|---|---|
| **Arcane Subtlety** | 2/2 | Reduces your target's resistance to all your spells by 10 and reduces the threat caused by your Arcane spells by 40%. |
| **Arcane Focus** | 5/5 | Reduces the chance that the opponent can resist your Arcane spells by 10%. |
| **Arcane Concentration** | 5/5 | Gives you a 10% chance of entering a Clearcasting state after any damage spell hits a target. The Clearcasting state reduces the mana cost of your next damage spell by 100%. |
| **Improved Arcane Explosion** | 3/3 | Increases the critical strike chance of your Arcane Explosion spell by an additional 6%. |
| **Magic Attunement** | 2/2 | Increases the effect of your Amplify Magic and Dampen Magic spells by 50%. |
| **Improved Counterspell** | 2/2 | Gives your Counterspell a 100% chance to silence the target for 4 sec. |
| **Arcane Meditation** | 1/3 | Allows 5% of your Mana regeneration to continue while casting. |

### Fire (0)

*No points.*

### Frost (31)

| Talent | Pts | Effect at this rank |
|---|---|---|
| **Improved Frostbolt** | 5/5 | Reduces the casting time of your Frostbolt spell by 0.5 sec. |
| **Ice Shards** | 5/5 | Increases the critical strike damage bonus of your Frost spells by 100%. |
| **Improved Frost Nova** | 2/2 | Reduces the cooldown of your Frost Nova spell by 4 sec. |
| **Permafrost** | 3/3 | Increases the duration of your Chill effects by 3 sec and reduces the target's speed by an additional 10%. |
| **Piercing Ice** | 3/3 | Increases the damage done by your Frost spells by 6%. |
| **Cold Snap** | 1/1 | When activated, this spell finishes the cooldown on all of your Frost spells. |
| **Arctic Reach** | 2/2 | Increases the range of your Frostbolt and Blizzard spells and the radius of your Frost Nova and Cone of Cold spells by 20%. |
| **Shatter** | 5/5 | Increases the critical strike chance of all your spells against frozen targets by 50%. |
| **Ice Block** | 1/1 | You become encased in a block of ice, protecting you from all physical attacks and spells for 10 sec, but during that time you cannot attack, move or cast spells. |
| **Improved Cone of Cold** | 3/3 | Increases the damage dealt by your Cone of Cold spell by 35%. |
| **Ice Barrier** | 1/1 | Instantly shields you, absorbing 455 damage. Lasts 1 min. While the shield holds, spells will not be interrupted. |

## Core talents (priority order)

1. **Shatter** — +50% crit against Frozen targets: Frost Nova -> Frostbolt/Cone of Cold crits.
2. **Ice Block** — Immunity.
3. **Ice Barrier** — Shield that stops pushback.
4. **Improved Counterspell** — 4s silence on Counterspell.
5. **Cold Snap** — Second Ice Block / Frost Nova.
6. **Permafrost** — Longer, stronger chills.
7. **Improved Cone of Cold** — +35% Cone of Cold damage — the Shatter finisher.
8. **Arctic Reach** — +20% range on Frostbolt/Blizzard and Frost Nova/Cone of Cold radius.
9. **Ice Shards** — Frost crit damage.

## Flex points

| Pts | Default | Alternatives | Why |
|---|---|---|---|
| 3 | Piercing Ice | Frostbite | Flat damage vs. random freeze procs. |
| 6 | Improved Arcane Explosion 3 + Magic Attunement 2 + Arcane Meditation 1 | Magic Absorption, Arcane Resilience | Filler on the way to Improved Counterspell. |

## Notes

- Some PvP mages prefer 0/0/51-style deep frost or the PoM/Pyro (Arcane/Fire) burst build; this is the all-round choice.

## Forever status of every point in this build

Talent-by-talent check against the Forever beta-client trees (`../forever/talent-trees.md`).

| Tree | Talent | Pts | In Forever | Detail |
|---|---|---|---|---|
| Arcane | Arcane Subtlety | 2 | changed | tier 2, max 2 — tooltip changed; was Arcane row 1, col 1 |
| Arcane | Arcane Focus | 5 | changed | tier 1, max 5 — tooltip changed |
| Arcane | Arcane Concentration | 5 | unchanged | tier 2, max 5 |
| Arcane | Improved Arcane Explosion | 3 | **REMOVED** | removed from Classic |
| Arcane | Magic Attunement | 2 | **REMOVED** | removed from Classic |
| Arcane | Improved Counterspell | 2 | changed | tier 4, max 2 — tooltip changed |
| Arcane | Arcane Meditation | 1 | changed | tier 4, max 3 — tooltip changed; was Arcane row 4, col 4 |
| Frost | Improved Frostbolt | 5 | changed | tier 1, max 5 — tooltip changed |
| Frost | Ice Shards | 5 | unchanged | tier 2, max 5 |
| Frost | Improved Frost Nova | 2 | unchanged | tier 2, max 2 |
| Frost | Permafrost | 3 | changed | tier 2, max 3 — tooltip changed; was Frost row 2, col 4 |
| Frost | Piercing Ice | 3 | unchanged | tier 3, max 3 |
| Frost | Cold Snap | 1 | changed | tier 5, max 1 — tooltip changed; was Frost row 3, col 2 |
| Frost | Arctic Reach | 2 | unchanged | tier 4, max 2 |
| Frost | Shatter | 5 | changed | tier 4, max 3 — max rank 5 → 3; tooltip changed; was Frost row 4, col 3 |
| Frost | Ice Block | 1 | moved | tier 4, max 1 — was Frost row 5, col 2 |
| Frost | Improved Cone of Cold | 3 | changed | tier 5, max 3 — tooltip changed; was Frost row 5, col 3 |
| Frost | Ice Barrier | 1 | changed | tier 7, max 1 — tooltip changed; tooltip changed in build 1.60.1.70009 (ranks 1) |

**5 point(s) of this build no longer exist in Forever** and must be re-spent; see `../forever/README.md` for how they were re-spent.

## Sources

- <https://www.wowhead.com/classic/guide/classes/mage/dps-pvp-arena>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
