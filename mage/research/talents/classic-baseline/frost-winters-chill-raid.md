# Frost — Winter's Chill (raid support) — 17/0/34

*Mage · Classic baseline*

| | |
|---|---|
| **Build** | 17/0/34 (Arcane / Fire / Frost) |
| **Role** | DPS — Raid |
| **Status** | Alternative |
| **Data** | Classic Era 1.12-era trees (validated against `_reference/data/classic-era-talents.json`) |
| **Forever** | This is the *baseline*; see the Forever status table below and `../forever/` for the adapted build |

## Summary

One mage per raid runs this: Winter's Chill stacks +10% Frost crit on the boss for every other mage. It also brings Ice Block, Ice Barrier and Shatter, so it is the safest build for progression. Personal damage is a little below the Arcane Power build.

## Point allocation

### Arcane (17)

| Talent | Pts | Effect at this rank |
|---|---|---|
| **Arcane Subtlety** | 2/2 | Reduces your target's resistance to all your spells by 10 and reduces the threat caused by your Arcane spells by 40%. |
| **Arcane Focus** | 5/5 | Reduces the chance that the opponent can resist your Arcane spells by 10%. |
| **Arcane Concentration** | 5/5 | Gives you a 10% chance of entering a Clearcasting state after any damage spell hits a target. The Clearcasting state reduces the mana cost of your next damage spell by 100%. |
| **Improved Arcane Explosion** | 3/3 | Increases the critical strike chance of your Arcane Explosion spell by an additional 6%. |
| **Arcane Meditation** | 2/3 | Allows 10% of your Mana regeneration to continue while casting. |

### Fire (0)

*No points.*

### Frost (34)

| Talent | Pts | Effect at this rank |
|---|---|---|
| **Improved Frostbolt** | 5/5 | Reduces the casting time of your Frostbolt spell by 0.5 sec. |
| **Elemental Precision** | 3/3 | Reduces the chance that the opponent can resist your Frost and Fire spells by 6%. |
| **Ice Shards** | 5/5 | Increases the critical strike damage bonus of your Frost spells by 100%. |
| **Improved Frost Nova** | 2/2 | Reduces the cooldown of your Frost Nova spell by 4 sec. |
| **Piercing Ice** | 3/3 | Increases the damage done by your Frost spells by 6%. |
| **Cold Snap** | 1/1 | When activated, this spell finishes the cooldown on all of your Frost spells. |
| **Frost Channeling** | 3/3 | Reduces the mana cost of your Frost spells by 15% and reduces the threat caused by your Frost spells by 30%. |
| **Shatter** | 5/5 | Increases the critical strike chance of all your spells against frozen targets by 50%. |
| **Ice Block** | 1/1 | You become encased in a block of ice, protecting you from all physical attacks and spells for 10 sec, but during that time you cannot attack, move or cast spells. |
| **Winter's Chill** | 5/5 | Gives your Frost damage spells a 100% chance to apply the Winter's Chill effect, which increases the chance a Frost spell will critically hit the target by 2% for 15 sec. Stacks up to 5 times. |
| **Ice Barrier** | 1/1 | Instantly shields you, absorbing 455 damage. Lasts 1 min. While the shield holds, spells will not be interrupted. |

## Core talents (priority order)

1. **Winter's Chill** — Stacking +2% Frost crit debuff (to 10%) for the whole raid's frost mages.
2. **Ice Shards** — +100% Frostbolt crit damage — with Winter's Chill up you crit often.
3. **Improved Frostbolt** — Cast time.
4. **Elemental Precision** — +6% hit.
5. **Piercing Ice** — +6% Frost damage.
6. **Ice Block** — Immunity; the progression safety button.
7. **Ice Barrier** — Absorb shield, prevents pushback.
8. **Shatter** — +50% crit on Frozen targets — dungeons and AoE packs.
9. **Arcane Concentration** — Clearcasting.
10. **Frost Channeling** — Mana and threat.

## Flex points

| Pts | Default | Alternatives | Why |
|---|---|---|---|
| 5 | Improved Arcane Explosion 3 + Arcane Meditation 2 | Magic Attunement 2 + Arcane Meditation 3, Magic Absorption | Reach Arcane Meditation any way you like. |
| 2 | Improved Frost Nova | Permafrost, Frostbite | Improved Frost Nova is the prerequisite for Shatter. |

## Notes

- Standard 17/0/34; Wowhead/Icy Veins list minor variants (Arctic Reach, Improved Blizzard for AoE farming).

## Forever status of every point in this build

Talent-by-talent check against the Forever beta-client trees (`../forever/talent-trees.md`).

| Tree | Talent | Pts | In Forever | Detail |
|---|---|---|---|---|
| Arcane | Arcane Subtlety | 2 | changed | tier 2, max 2 — tooltip changed; was Arcane row 1, col 1 |
| Arcane | Arcane Focus | 5 | changed | tier 1, max 5 — tooltip changed |
| Arcane | Arcane Concentration | 5 | unchanged | tier 2, max 5 |
| Arcane | Improved Arcane Explosion | 3 | **REMOVED** | removed from Classic |
| Arcane | Arcane Meditation | 2 | changed | tier 4, max 3 — tooltip changed; was Arcane row 4, col 4 |
| Frost | Improved Frostbolt | 5 | changed | tier 1, max 5 — tooltip changed |
| Frost | Elemental Precision | 3 | changed | tier 1, max 5 — max rank 3 → 5; tooltip changed |
| Frost | Ice Shards | 5 | unchanged | tier 2, max 5 |
| Frost | Improved Frost Nova | 2 | unchanged | tier 2, max 2 |
| Frost | Piercing Ice | 3 | unchanged | tier 3, max 3 |
| Frost | Cold Snap | 1 | changed | tier 5, max 1 — tooltip changed; was Frost row 3, col 2 |
| Frost | Frost Channeling | 3 | moved | tier 3, max 3 — was Frost row 4, col 2 |
| Frost | Shatter | 5 | changed | tier 4, max 3 — max rank 5 → 3; tooltip changed; was Frost row 4, col 3 |
| Frost | Ice Block | 1 | moved | tier 4, max 1 — was Frost row 5, col 2 |
| Frost | Winter's Chill | 5 | changed | tier 6, max 5 — tooltip changed |
| Frost | Ice Barrier | 1 | changed | tier 7, max 1 — tooltip changed; tooltip changed in build 1.60.1.70291 (ranks 1) |

**3 point(s) of this build no longer exist in Forever** and must be re-spent; see `../forever/README.md` for how they were re-spent.

## Sources

- <https://www.icy-veins.com/wow-classic/mage-dps-pve-spec-builds-talents>
- <https://www.warcrafttavern.com/wow-classic/guides/pve-frost-mage-talents-builds/>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
