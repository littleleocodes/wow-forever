# Frost (PvP) — 20/0/31

*[Mage](../../../README.md) · [PvP](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 20/0/31 (Arcane / Fire / Frost) |
| **Role** | DPS — PvP |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70707 (2026-10-16 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |
| **Based on** | Classic baseline `pvp-frost` |

## Summary

Shatter (3 ranks), Ice Lance + Fingers of Frost, Frostbite, Permafrost, Improved Cone of Cold, Ice Block (tier 4), Cold Snap and Ice Barrier, with Improved Counterspell and Arcane Meditation from Arcane. Same 20/0/31 shape as Classic with Ice Lance replacing a Piercing Ice/Arctic Reach point.

## Point allocation

### Arcane (20)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Arcane Resilience** | 2/3 | changed | Increases your Armor by an amount equal to 50% of your Intellect. |
| **Improved Channeling** | 1/5 | **NEW** | Gives your Arcane Missiles spell a 20% chance and your Arcane Blast and Arcane Wrath spells a 14% chance to not lose casting time when you take damage. |
| **Wand Specialization** | 2/2 | moved | Increases your damage with Wands by 25%. |
| **Arcane Concentration** | 5/5 | unchanged | Gives you a 10% chance of entering a Clearcasting state after any damage spell hits a target. The Clearcasting state reduces the mana cost of your next damage spell by 100%. |
| **Arcane Subtlety** | 2/2 | changed | Reduces your target's resistance to all your spells by 15 and reduces the threat caused by your Arcane spells by 30%. |
| **Missile Barrage** | 2/2 | **NEW** | Gives your Arcane Blast spell a 40% chance, and your Arcane Wrath, Fireball, Frostbolt, Frost Blast, and Frostfire Bolt spells a 20% chance to reduce the channeled duration of your next Arcane Missiles spell by 50%, reduce the Mana cost by 100%, and missiles fire every 0.5 sec. |
| **Arcane Blast** | 1/1 | **NEW** | Blasts the target with energy, dealing 34 to 38 Arcane damage. Each time you cast Arcane Blast, you gain 15% of your Intellect as Spell Damage and the mana cost of Arcane Blast is increased by 175%. Effect stacks up to 4 times and lasts 15 sec from time of initial application. |
| **Arcane Meditation** | 3/3 | changed | Allows 50% of your Mana regeneration to continue while casting. |
| **Improved Counterspell** | 2/2 | changed | Your Counterspell also Silences the target for 4 sec. |

### Fire (0)

*No points.*

### Frost (31)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Improved Frostbolt** | 5/5 | changed | Reduces the casting time of your Frostbolt and Frost Blast spells by 0.5 sec. |
| **Frostbite** | 3/3 | moved | Gives your Chill effects a 15% chance to Freeze the target for 5 sec. |
| **Ice Shards** | 5/5 | unchanged | Increases the critical strike damage bonus of your Frost spells by 100%. |
| **Improved Frost Nova** | 2/2 | unchanged | Reduces the cooldown of your Frost Nova spell by 4 sec. |
| **Permafrost** | 3/3 | changed | Increases the duration of your Chill effects by 33% and reduces the target's speed by an additional 10%. |
| **Ice Lance** | 1/1 | **NEW** | Deals 28 to 32 Frost damage to an enemy target. Deals 200% increased damage to Frozen targets. |
| **Arctic Reach** | 1/2 | unchanged | Increases the range of your Frostbolt, Frost Blast, Ice Lance and Blizzard spells and the radius of your Frost Nova and Cone of Cold spells by 10%. |
| **Ice Block** | 1/1 | moved | You become encased in a block of ice, protecting you from all physical attacks and spells for 10 sec, but during that time you cannot attack, move, or cast spells. |
| **Shatter** | 3/3 | changed | Increases the critical strike chance of all your spells against Frozen targets by 50%. |
| **Cold Snap** | 1/1 | changed | Finishes the remaining cooldown on all your other Frost spells. |
| **Fingers of Frost** | 2/2 | **NEW** | Gives your Chill effects a 15% chance to grant you the Fingers of Frost effect, which treats your next 2 spells cast as if the target were Frozen. Lasts 15 sec. |
| **Improved Cone of Cold** | 3/3 | changed | Increases the damage dealt by your Cone of Cold spell by 35%. |
| **Ice Barrier** | 1/1 | changed | Shield yourself, absorbing 447 damage and increasing your Frost damage by 15% for 1 min. While shielded, your Frost damage is increased by an additional 5% and you do not lose casting time when you take damage. |

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
- 2026-10-22 (repair_builds.py, client build 70425 trees): 20/0/31 -> 20/0/31; Piercing Ice 3 gone; +1 Frostbite (tier gating for Ice Barrier); +1 Frostbite (tier gating for Ice Barrier); +1 Frostbite (tier gating for Ice Barrier) (refill: the frost-raid model, pvp).
- 2026-10-30 (repair_builds.py, client build 1.60.1.70707 trees): 20/0/31 -> 20/0/31; Arcane Focus 3 gone; +1 Improved Channeling (tier gating for Arcane Concentration); +1 Missile Barrage (tier gating for Arcane Meditation); +1 Missile Barrage (tier gating for Arcane Meditation) (refill: the frost-raid model, pvp).

## Open questions (verify in the live game)

- Improved Counterspell's demo silence is 2s (Classic 4s) — check the final value.

## Sources

- <https://warcraftforever.games/talents/mage>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
