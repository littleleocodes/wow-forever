# Frost — Winter's Chill (raid support) — 17/0/34

*[Mage](../../README.md) · [Raids: training dummy, raid and parse](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 17/0/34 (Arcane / Fire / Frost) |
| **Role** | DPS — Raid |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70009 (2026-09-25 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |
| **Based on** | Classic baseline `frost-winters-chill-raid` |

## Summary

Winter's Chill now buffs Frostbolt and Ice Lance crit (demo text says it stacks once — likely a transcription artefact; Classic stacked to 5), Ice Block moved to tier 4 and Cold Snap to tier 5, Shatter is 3 ranks. The 17/0/34 shape still fits with Elemental Precision at 5 ranks.

## Point allocation

### Arcane (17)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Wand Specialization** | 2/2 | moved | Increases your damage with Wands by 25%. |
| **Arcane Focus** | 3/5 | changed | Improves your chance to hit with Arcane spells by 3%. |
| **Arcane Subtlety** | 2/2 | changed | Reduces your target's resistance to all your spells by 15 and reduces the threat caused by your Arcane spells by 30%. |
| **Arcane Concentration** | 5/5 | unchanged | Gives you a 10% chance of entering a Clearcasting state after any damage spell hits a target. The Clearcasting state reduces the mana cost of your next damage spell by 100%. |
| **Arcane Geometry** | 2/2 | **NEW** | Increases the range of your Arcane spells by 6 yards. |
| **Arcane Blast** | 1/1 | **NEW** | Blasts the target with energy, dealing 57 to 65 Arcane damage. Each time you cast Arcane Blast, the damage of all your other spells is increased by 10% and the mana cost of Arcane Blast is increased by 175%. Effect stacks up to 4 times and lasts 8 sec or until any other damage spell is cast. |
| **Arcane Meditation** | 2/3 | changed | Allows 33% of your Mana regeneration to continue while casting. |

### Fire (0)

*No points.*

### Frost (34)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Improved Frostbolt** | 5/5 | changed | Reduces the casting time of your Frostbolt spell by 0.5 sec. |
| **Elemental Precision** | 5/5 | changed | Improves your chance to hit with Frost and Fire spells by 5%. |
| **Ice Shards** | 5/5 | unchanged | Increases the critical strike damage bonus of your Frost spells by 100%. |
| **Piercing Ice** | 3/3 | unchanged | Increases the damage done by your Frost spells by 6%. |
| **Frost Channeling** | 3/3 | moved | Reduces the mana cost of your Frost spells by 15% and reduces the threat caused by your Frost spells by 30%. |
| **Shatter** | 3/3 | changed | Increases the critical strike chance of all your spells against Frozen targets by 50%. |
| **Ice Block** | 1/1 | moved | You become encased in a block of ice, protecting you from all physical attacks and spells for 10 sec, but during that time you cannot attack, move, or cast spells. |
| **Arctic Reach** | 2/2 | unchanged | Increases the range of your Frostbolt and Blizzard spells and the radius of your Frost Nova and Cone of Cold spells by 20%. |
| **Cold Snap** | 1/1 | changed | Finishes the remaining cooldown on all your other Frost spells. |
| **Winter's Chill** | 5/5 | changed | Gives your Frost damage spells a 100% chance to apply the Winter's Chill effect, which increases the chance your Ice Lance and Frostbolt spells will critically hit the target by 2% for 15 sec. Stacks up to 5 times. |
| **Ice Barrier** | 1/1 | changed | Instantly shields you, absorbing 447 damage. Lasts 1 min. While the shield holds, your spellcasts will not be interrupted or delayed from taking damage. |

## Core talents (priority order)

1. **Winter's Chill** — 100% chance at max rank to apply the crit debuff for Frostbolt/Ice Lance — the raid-support reason for the build.
2. **Ice Shards** — Frostbolt crit damage.
3. **Elemental Precision** — 5% hit.
4. **Improved Frostbolt** — Cast time.
5. **Piercing Ice** — Frost damage.
6. **Ice Block** — Now the 16-point Frost talent — cheap immunity.
7. **Ice Barrier** — Capstone shield; requires Cold Snap.
8. **Shatter** — 3 ranks, est. +51% crit vs. Frozen — AoE/dungeon value and Fingers of Frost synergy later.
9. **Frost Channeling** — Mana and threat.
10. **Arcane Meditation** — Regen while casting (2/3).

## Flex points

| Pts | Default | Alternatives | Why |
|---|---|---|---|
| 2 | Arcane Meditation 2 | Arcane Meditation 3 with Arcane Blast 0 | Regen vs. filler. |

## Rank among our builds and the community simulator's

**7 of 11** for `frost-raid` by training-dummy DPS in the community simulator (ElliotWood/Forever 40be98e); full ranking and the other builds' rotations: [raid README](../README.md), [raid rotations](../rotation.md).

| Rank | Build | By | Split | Dummy DPS | vs best | Raid DPS | vs best in a raid | Out of mana on the dummy |
|---|---|---|---|---|---|---|---|---|
| 1 | [`frost-fingers-of-frost-raid`](frost-fingers-of-frost-raid.md) | ours: hand draft | 22/0/29 | 587 | +0.0% | 668 | +0.0% | 0 s |
| 2 | [`opt-frost-raid-raid-dps`](opt-frost-raid-raid-dps.md) | ours: optimizer | 22/0/29 | 587 | +0.0% | 668 | +0.0% | 0 s |
| 3 | [`opt-frost-raid-raid-dps-extwc`](opt-frost-raid-raid-dps-extwc.md) | ours: optimizer | 1/13/37 | 570 | -3.0% | 649 | -2.8% | 0 s |
| 4 | *Frost 14/0/37* | community simulator | - | 559 | -4.9% | 644 | -3.5% | 3 s |
| 5 | *Frost DPS* | community simulator | - | 557 | -5.2% | 636 | -4.7% | 0 s |
| 6 | [`frost-arcane-power-raid`](frost-arcane-power-raid.md) | ours: hand draft | 31/0/20 | 548 | -6.7% | 627 | -6.1% | 0 s |
| 7 | **[`frost-winters-chill-raid`](frost-winters-chill-raid.md)** | ours: hand draft | 17/0/34 | 490 | -16.6% | 559 | -16.3% | 0 s |
| 8 | *Arcane 35/0/16* | community simulator | - | 479 | -18.6% | 547 | -18.0% | 0 s |
| 9 | *Arcane DPS* | community simulator | - | 418 | -28.8% | 474 | -29.1% | 0 s |
| 10 | *Fire 0/35/16* | community simulator | - | 378 | -35.7% | 432 | -35.2% | 0 s |
| 11 | *Fire DPS* | community simulator | - | 318 | -45.9% | 357 | -46.5% | 0 s |

## Rotation (community simulator, training dummy)

- **The training dummy:** the simulator's own rotation: no single change (and no pair of changes) beat it on two seeds (`raidsim/apl_opt.py`, 2026-09-29).
- **A fully buffed raid:** the simulator's own rotation: no single change (and no pair of changes) beat it on two seeds (`raidsim/apl_opt.py`, 2026-09-29).

| # | Priority (the first line whose condition holds is cast) | [`frost-winters-chill-raid`](frost-winters-chill-raid.md) casts/min |
|---|---|---|
| 1 | if mana % ≤ 80%: cast item 8008 | as ready |
| 2 | use every other cooldown when ready | as ready |
| 3 | cast Frostbolt | 24.0 |

Lines of the simulator's rotation these builds never cast: cast Evocation, cast Arcane Missiles (its condition never held in these fights); cast Ice Lance (needs the Ice Lance talent).

Damage by ability:

| Ability | [`frost-winters-chill-raid`](frost-winters-chill-raid.md) |
|---|---|
| Frostbolt | 100% |

## Notes

- Ice Lance + Fingers of Frost are not taken here; they need 3 more Frost points (see the Fingers of Frost build).
- 2026-09-27 scenario audit: Improved Frost Nova 2 -> Arctic Reach 2. Improved Frost Nova shortens a root's cooldown: control a raid boss ignores (simulator 0.0%). Arctic Reach 2/2 adds range. This draft is superseded in Forever: the beta Winter's Chill raises only your own Frostbolt and Ice Lance crit, so the raid-support reason for skipping Fingers of Frost is gone, and frost-fingers-of-frost-raid simulates about 14% higher (645 vs 559 DPS).

## Open questions (verify in the live game)

- Winter's Chill stack count (demo says 1; Classic was 5) — decides whether one dedicated WC mage is still worth it.

## Sources

- <https://warcraftforever.games/talents/mage>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
