# Frost — Arcane Power / Frostbolt (raid DPS) — 31/0/20

*Mage · Classic baseline*

| | |
|---|---|
| **Build** | 31/0/20 (Arcane / Fire / Frost) |
| **Role** | DPS — Raid |
| **Status** | Primary |
| **Data** | Classic Era 1.12-era trees (validated against `_reference/data/classic-era-talents.json`) |
| **Forever** | This is the *baseline*; see the Forever status table below and `../forever/` for the adapted build |

## Summary

Highest personal Frostbolt damage in Classic: Arcane Power + Presence of Mind + Arcane Instability from a 31-point Arcane tree, with 20 points in Frost for Improved Frostbolt, Ice Shards, Piercing Ice, Elemental Precision and Frost Channeling. The build to run while fire-immune bosses dominate (MC/BWL).

## Point allocation

### Arcane (31)

| Talent | Pts | Effect at this rank |
|---|---|---|
| **Arcane Subtlety** | 2/2 | Reduces your target's resistance to all your spells by 10 and reduces the threat caused by your Arcane spells by 40%. |
| **Arcane Focus** | 5/5 | Reduces the chance that the opponent can resist your Arcane spells by 10%. |
| **Magic Absorption** | 2/5 | Increases all resistances by 4 and causes all spells you fully resist to restore 2% of your total mana. 1 sec. cooldown. |
| **Arcane Concentration** | 5/5 | Gives you a 10% chance of entering a Clearcasting state after any damage spell hits a target. The Clearcasting state reduces the mana cost of your next damage spell by 100%. |
| **Improved Arcane Explosion** | 3/3 | Increases the critical strike chance of your Arcane Explosion spell by an additional 6%. |
| **Arcane Resilience** | 1/1 | Increases your armor by an amount equal to 50% of your Intellect. |
| **Arcane Meditation** | 3/3 | Allows 15% of your Mana regeneration to continue while casting. |
| **Presence of Mind** | 1/1 | When activated, your next Mage spell with a casting time less than 10 sec becomes an instant cast spell. |
| **Arcane Mind** | 5/5 | Increases your maximum Mana by 10%. |
| **Arcane Instability** | 3/3 | Increases your spell damage and critical strike chance by 3%. |
| **Arcane Power** | 1/1 | When activated, your spells deal 30% more damage while costing 30% more mana to cast. This effect lasts 15 sec. |

### Fire (0)

*No points.*

### Frost (20)

| Talent | Pts | Effect at this rank |
|---|---|---|
| **Improved Frostbolt** | 5/5 | Reduces the casting time of your Frostbolt spell by 0.5 sec. |
| **Elemental Precision** | 3/3 | Reduces the chance that the opponent can resist your Frost and Fire spells by 6%. |
| **Ice Shards** | 5/5 | Increases the critical strike damage bonus of your Frost spells by 100%. |
| **Piercing Ice** | 3/3 | Increases the damage done by your Frost spells by 6%. |
| **Cold Snap** | 1/1 | When activated, this spell finishes the cooldown on all of your Frost spells. |
| **Frost Channeling** | 3/3 | Reduces the mana cost of your Frost spells by 15% and reduces the threat caused by your Frost spells by 30%. |

## Core talents (priority order)

1. **Arcane Power** — +30% spell damage for 15s every 3 minutes; stacks with trinkets for huge burst windows.
2. **Presence of Mind** — Instant Frostbolt; combined with Arcane Power for burst.
3. **Arcane Instability** — +3% damage and +3% crit to everything.
4. **Ice Shards** — +100% Frostbolt crit damage.
5. **Improved Frostbolt** — -0.5s cast time on the only spell you cast.
6. **Elemental Precision** — +6% hit for Frost/Fire — the most valuable points in the tree.
7. **Piercing Ice** — +6% Frost damage.
8. **Arcane Concentration** — Clearcasting procs = free Frostbolts and better mana.
9. **Frost Channeling** — -15% Frost mana cost, -30% Frost threat.
10. **Arcane Mind** — +10% Intellect — mana and crit.
11. **Arcane Meditation** — +15% mana regen while casting.

## Flex points

| Pts | Default | Alternatives | Why |
|---|---|---|---|
| 5 | Magic Absorption 2 + Improved Arcane Explosion 3 | Magic Attunement, Wand Specialization, Improved Counterspell | Pure filler to reach the tier requirements in Arcane. |
| 1 | Cold Snap | Arctic Reach, Frost Warding | Twentieth Frost point; Cold Snap is nice for Ice Block if you have it (you don't here), so Arctic Reach is a fair alternative. |

## Notes

- Frostbolt spam; Arcane Power + Presence of Mind + trinkets on the pull or during burn phases.
- No Ice Block or Ice Barrier — this is a pure damage build.

## Forever status of every point in this build

Talent-by-talent check against the Forever beta-client trees (`../forever/talent-trees.md`).

| Tree | Talent | Pts | In Forever | Detail |
|---|---|---|---|---|
| Arcane | Arcane Subtlety | 2 | changed | tier 2, max 2 — tooltip changed; was Arcane row 1, col 1 |
| Arcane | Arcane Focus | 5 | unknown | not found in Forever data |
| Arcane | Magic Absorption | 2 | changed | tier 2, max 2 — max rank 5 → 2; tooltip changed |
| Arcane | Arcane Concentration | 5 | unchanged | tier 2, max 5 |
| Arcane | Improved Arcane Explosion | 3 | **REMOVED** | removed from Classic |
| Arcane | Arcane Resilience | 1 | changed | tier 1, max 3 — max rank 1 → 2; tooltip changed; was Arcane row 3, col 3; moved in build 1.60.1.70707: was row 2, col 4; max rank 2 -> 3 in build 1.60.1.70707; tooltip changed in build 1.60.1.70707 (ranks 1, 2, 3) |
| Arcane | Arcane Meditation | 3 | changed | tier 4, max 3 — tooltip changed; was Arcane row 4, col 4 |
| Arcane | Presence of Mind | 1 | unchanged | tier 5, max 1 |
| Arcane | Arcane Mind | 5 | changed | tier 5, max 5 — tooltip changed |
| Arcane | Arcane Instability | 3 | changed | tier 6, max 3 — tooltip changed; was Arcane row 6, col 2 |
| Arcane | Arcane Power | 1 | changed | tier 7, max 1 — tooltip changed |
| Frost | Improved Frostbolt | 5 | changed | tier 1, max 5 — tooltip changed; tooltip changed in build 1.60.1.70707 (ranks 1, 2, 3, 4, 5) |
| Frost | Elemental Precision | 3 | unknown | not found in Forever data |
| Frost | Ice Shards | 5 | unchanged | tier 2, max 5 |
| Frost | Piercing Ice | 3 | unknown | not found in Forever data |
| Frost | Cold Snap | 1 | changed | tier 5, max 1 — tooltip changed; was Frost row 3, col 2 |
| Frost | Frost Channeling | 3 | moved | tier 3, max 3 — was Frost row 4, col 2; moved in build 1.60.1.70707: was row 3, col 2 |

**3 point(s) of this build no longer exist in Forever** and must be re-spent; see `../forever/README.md` for how they were re-spent.

## Sources

- <https://www.icy-veins.com/wow-classic/mage-dps-pve-spec-builds-talents>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
