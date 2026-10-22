# Frost — Leveling (open talent search) — 18/2/31

*[Mage](../../../README.md) · [Leveling and solo play](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 18/2/31 (Arcane / Fire / Frost) |
| **Role** | DPS — Leveling |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70425 (2026-10-16 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

The Frost leveling build the open leveling search found on 2026-10-20: every legal 51-point build with no tree rule, searched at level 60 in the fight lab (this project's solo leveling simulator: same-level mobs, eating, drinking and deaths included) playing the frost-leveling rotation, the winner picked by a race at levels 20-60 among the level-60 finalists (fightlab/fl_open_search.py); the talent order is the stats model's (frost-leveling). 

## Point allocation

### Arcane (18)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Arcane Focus** | 2/5 | changed | Improves your chance to hit with Arcane spells by 2%. |
| **Improved Channeling** | 2/5 | **NEW** | Gives you a 40% chance to avoid interruption caused by damage while channeling Arcane Missiles and a 28% chance while casting Arcane Blast or Arcane Wrath. |
| **Wand Specialization** | 2/2 | moved | Increases your damage with Wands by 25%. |
| **Arcane Concentration** | 5/5 | unchanged | Gives you a 10% chance of entering a Clearcasting state after any damage spell hits a target. The Clearcasting state reduces the mana cost of your next damage spell by 100%. |
| **Arcane Resilience** | 1/2 | changed | Increases your Armor by an amount equal to 25% of your Intellect. |
| **Arcane Subtlety** | 2/2 | changed | Reduces your target's resistance to all your spells by 15 and reduces the threat caused by your Arcane spells by 30%. |
| **Magic Absorption** | 1/2 | changed | Increases all your resistances by 5 and causes all spells you fully resist to restore 1% of your total mana. Cannot trigger more often than 1 time per sec. |
| **Arcane Meditation** | 3/3 | changed | Allows 50% of your Mana regeneration to continue while casting. |

### Fire (2)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Incineration** | 2/3 | **NEW** | Increases the critical strike chance of your Fire Blast, Ice Lance, Arcane Blast, and Scorch spells by 4%. |

### Frost (31)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Elemental Precision** | 3/3 | changed | Improves your chance to hit with Frost and Fire spells by 6%. |
| **Improved Frostbolt** | 5/5 | changed | Reduces the casting time of your Frostbolt and Frost Blast spells by 0.5 sec. |
| **Frostbite** | 3/3 | moved | Gives your Chill effects a 15% chance to Freeze the target for 5 sec. |
| **Ice Shards** | 5/5 | unchanged | Increases the critical strike damage bonus of your Frost spells by 100%. |
| **Improved Frost Nova** | 1/2 | unchanged | Reduces the cooldown of your Frost Nova spell by 2 sec. |
| **Frost Channeling** | 3/3 | moved | Reduces the mana cost of your Frost spells by 15% and reduces the threat caused by your Frost spells by 30%. |
| **Ice Lance** | 1/1 | **NEW** | Deals 28 to 32 Frost damage to an enemy target. Deals 200% increased damage to Frozen targets. |
| **Arctic Reach** | 2/2 | unchanged | Increases the range of your Frostbolt, Frost Blast, and Blizzard spells and the radius of your Frost Nova and Cone of Cold spells by 20%. |
| **Ice Block** | 1/1 | moved | You become encased in a block of ice, protecting you from all physical attacks and spells for 10 sec, but during that time you cannot attack, move, or cast spells. |
| **Shatter** | 3/3 | changed | Increases the critical strike chance of all your spells against Frozen targets by 50%. |
| **Cold Snap** | 1/1 | changed | Finishes the remaining cooldown on all your other Frost spells. |
| **Fingers of Frost** | 2/2 | **NEW** | Gives your Chill effects a 15% chance to grant you the Fingers of Frost effect, which treats your next 2 spells cast as if the target were Frozen. Lasts 15 sec. |
| **Ice Barrier** | 1/1 | changed | Instantly shields you, absorbing 447 damage. Lasts 1 min. While the shield holds, your spellcasts will not be interrupted or delayed from taking damage. |

## Core talents (priority order)

1. **Ice Lance** — +6.4 s per kill at level 60 without it (removal, 3,000 fights).
2. **Shatter** — +4.6 s per kill at level 60 without it (removal, 3,000 fights).
3. **Ice Shards** — +2.5 s per kill at level 60 without it (removal, 3,000 fights).
4. **Frost Channeling** — +1.6 s per kill at level 60 without it (removal, 3,000 fights).
5. **Fingers of Frost** — +1.4 s per kill at level 60 without it (removal, 3,000 fights).
6. **Arcane Meditation** — +1.3 s per kill at level 60 without it (removal, 3,000 fights).
7. **Piercing Ice** — +1.0 s per kill at level 60 without it (removal, 3,000 fights).
8. **Frostbite** — +0.8 s per kill at level 60 without it (removal, 3,000 fights).

## Leveling rotation

Not simulated in the fight lab; the class's leveling priority is on the [leveling rotation page](../rotation.md).

## Notes

- +3.6% faster than the hand draft leveling-frost, over the replacement bar: this build is the spec's leveling pick, the hand draft stays as the alternative.
- Race at levels 20-60 (seed 3, 3,000 fights per level; level-weighted seconds per kill, lower is faster): this build 29.43; opt-frost-leveling-leveling-st 29.84, leveling-frost 30.48, opt-frost-aoe-leveling-aoe 33.44. The search simulated 103,214 builds.
- Fight-lab numbers are a model of the beta (the assumptions in fightlab/tables.py), not in-game measurements.
- 2026-10-22 (repair_builds.py, client build 70425 trees): 18/2/31 -> 18/2/31; Elemental Precision 4 -> 3 (rank cap); Piercing Ice 3 gone; +1 Ice Block (tier gating for Ice Barrier); +1 Arctic Reach (tier gating for Ice Barrier); +1 Arctic Reach (tier gating for Ice Barrier); +1 Improved Frost Nova (tier gating for Ice Barrier); order dropped (order_repair.py) (refill: the frost-leveling model, leveling-st).

## Open questions (verify in the live game)

- An open-search Frost leveling build: check it while leveling at launch.

## Sources

- <https://talentsforever.com/mage>
- <https://talentsforever.com/mage/60/22202151000003-02-0545003331000301201-7>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
