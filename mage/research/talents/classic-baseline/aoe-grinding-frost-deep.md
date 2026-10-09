# AoE grinding — deep Frost 7/0/44 (Shatter + Winter's Chill) — 7/0/44

*Mage · Classic baseline*

| | |
|---|---|
| **Build** | 7/0/44 (Arcane / Fire / Frost) |
| **Role** | DPS — Leveling |
| **Status** | Alternative |
| **Data** | Classic Era 1.12-era trees (validated against `_reference/data/classic-era-talents.json`) |
| **Forever** | This is the *baseline*; see the Forever status table below and `../forever/` for the adapted build |

## Summary

Warcraft Tavern's AoE build, decoded from the guide's talent-calculator link (the prose names only a few talents): the same control core as the Icy Veins build (Improved Frost Nova, Permafrost, Improved Blizzard 2/3 so the Cone of Cold snare is not overwritten, Arctic Reach, Cold Snap, Ice Block, Ice Barrier, no Frostbite) but the Arcane mana points go into Frost instead: Shatter 5/5 for crits during the Nova window, Winter's Chill 5/5, Improved Frostbolt 5 as the tier-1 filler.

## Point allocation

### Arcane (7)

| Talent | Pts | Effect at this rank |
|---|---|---|
| **Arcane Subtlety** | 2/2 | Reduces your target's resistance to all your spells by 10 and reduces the threat caused by your Arcane spells by 40%. |
| **Arcane Focus** | 3/5 | Reduces the chance that the opponent can resist your Arcane spells by 6%. |
| **Arcane Concentration** | 2/5 | Gives you a 4% chance of entering a Clearcasting state after any damage spell hits a target. The Clearcasting state reduces the mana cost of your next damage spell by 100%. |

### Fire (0)

*No points.*

### Frost (44)

| Talent | Pts | Effect at this rank |
|---|---|---|
| **Improved Frostbolt** | 5/5 | Reduces the casting time of your Frostbolt spell by 0.5 sec. |
| **Elemental Precision** | 3/3 | Reduces the chance that the opponent can resist your Frost and Fire spells by 6%. |
| **Ice Shards** | 5/5 | Increases the critical strike damage bonus of your Frost spells by 100%. |
| **Improved Frost Nova** | 2/2 | Reduces the cooldown of your Frost Nova spell by 4 sec. |
| **Permafrost** | 3/3 | Increases the duration of your Chill effects by 3 sec and reduces the target's speed by an additional 10%. |
| **Piercing Ice** | 3/3 | Increases the damage done by your Frost spells by 6%. |
| **Cold Snap** | 1/1 | When activated, this spell finishes the cooldown on all of your Frost spells. |
| **Improved Blizzard** | 2/3 | Adds a chill effect to your Blizzard spell. This effect lowers the target's movement speed by 50%. Lasts 1.50 sec. |
| **Arctic Reach** | 2/2 | Increases the range of your Frostbolt and Blizzard spells and the radius of your Frost Nova and Cone of Cold spells by 20%. |
| **Frost Channeling** | 3/3 | Reduces the mana cost of your Frost spells by 15% and reduces the threat caused by your Frost spells by 30%. |
| **Shatter** | 5/5 | Increases the critical strike chance of all your spells against frozen targets by 50%. |
| **Ice Block** | 1/1 | You become encased in a block of ice, protecting you from all physical attacks and spells for 10 sec, but during that time you cannot attack, move or cast spells. |
| **Improved Cone of Cold** | 3/3 | Increases the damage dealt by your Cone of Cold spell by 35%. |
| **Winter's Chill** | 5/5 | Gives your Frost damage spells a 100% chance to apply the Winter's Chill effect, which increases the chance a Frost spell will critically hit the target by 2% for 15 sec. Stacks up to 5 times. |
| **Ice Barrier** | 1/1 | Instantly shields you, absorbing 455 damage. Lasts 1 min. While the shield holds, spells will not be interrupted. |

## Core talents (priority order)

1. **Improved Blizzard** — 2/3 on purpose: 'otherwise it will cancel out your snare from Cone of Cold'.
2. **Shatter** — Crits on the Nova-frozen pack (the guide's link takes 5/5; Icy Veins' build does not take it).
3. **Improved Cone of Cold** — 'You will be using Cone of Cold rather frequently and the 35% increase in damage is very helpful.'
4. **Ice Barrier** — 'One of the easiest ways to round up mobs' - run through them shielded until they are grouped for Frost Nova.

## Flex points

| Pts | Default | Alternatives | Why |
|---|---|---|---|
| 5 | Winter's Chill 5 | Arcane Meditation 3 + Wand Specialization 2 (the Icy Veins split) | Winter's Chill stacks slowly on a pack that dies in 30s; the Arcane split trades it for regen. |

## Notes

- Loop per the guide: Cone of Cold, Frost Nova, Blink to max range, two Blizzards, Cone of Cold again as they close, Nova and repeat.
- Frostbite: 'Do NOT put points into this talent, as it will cause issues with being able to properly clump the mobs together.'

## Forever status of every point in this build

Talent-by-talent check against the Forever beta-client trees (`../forever/talent-trees.md`).

| Tree | Talent | Pts | In Forever | Detail |
|---|---|---|---|---|
| Arcane | Arcane Subtlety | 2 | changed | tier 2, max 2 — tooltip changed; was Arcane row 1, col 1 |
| Arcane | Arcane Focus | 3 | changed | tier 1, max 5 — tooltip changed |
| Arcane | Arcane Concentration | 2 | unchanged | tier 2, max 5 |
| Frost | Improved Frostbolt | 5 | changed | tier 1, max 5 — tooltip changed |
| Frost | Elemental Precision | 3 | changed | tier 1, max 5 — max rank 3 → 5; tooltip changed |
| Frost | Ice Shards | 5 | unchanged | tier 2, max 5 |
| Frost | Improved Frost Nova | 2 | unchanged | tier 2, max 2 |
| Frost | Permafrost | 3 | changed | tier 2, max 3 — tooltip changed; was Frost row 2, col 4 |
| Frost | Piercing Ice | 3 | unchanged | tier 3, max 3 |
| Frost | Cold Snap | 1 | changed | tier 5, max 1 — tooltip changed; was Frost row 3, col 2 |
| Frost | Improved Blizzard | 2 | changed | tier 3, max 3 — tooltip changed |
| Frost | Arctic Reach | 2 | unchanged | tier 4, max 2 |
| Frost | Frost Channeling | 3 | moved | tier 3, max 3 — was Frost row 4, col 2 |
| Frost | Shatter | 5 | changed | tier 4, max 3 — max rank 5 → 3; tooltip changed; was Frost row 4, col 3 |
| Frost | Ice Block | 1 | moved | tier 4, max 1 — was Frost row 5, col 2 |
| Frost | Improved Cone of Cold | 3 | changed | tier 5, max 3 — tooltip changed; was Frost row 5, col 3 |
| Frost | Winter's Chill | 5 | changed | tier 6, max 5 — tooltip changed |
| Frost | Ice Barrier | 1 | changed | tier 7, max 1 — tooltip changed; tooltip changed in build 1.60.1.70291 (ranks 1) |

**0 point(s) of this build no longer exist in Forever** and must be re-spent; see `../forever/README.md` for how they were re-spent.

## Sources

- <https://www.warcrafttavern.com/wow-classic/guides/frost-mage-aoe/>
- <https://www.warcrafttavern.com/tools/talent-calculator/mage?t=A0011166C1111122244444667778889bbccdddeeeeehiiimmmmmp>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
