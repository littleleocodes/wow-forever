# Restoration — Raid Healer (healer lab winner adopted 2026-09-28) — 11/5/35

*[Druid](../../../README.md) · [Raids: training dummy, raid and parse](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 11/5/35 (Balance / Feral Combat / Restoration) |
| **Role** | HEALER — Raid |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70291 (2026-10-08 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |
| **Based on** | Classic baseline `resto-swiftmend-healer` |

## Summary

Allocation adopted on 2026-09-28 from `cand-resto-r2`, the build with the highest healing capacity in the healer lab (+3.2% vs the previous draft; kept under raid/heallab/candidates/). Previous summary: Swiftmend moved to the 16-point slot and Wild Growth is the new capstone; Naturalist replaces Improved Healing Touch, Living Spirit adds Spirit, Gift of the Earthmother speeds up Rejuvenation/Swiftmend/Wild Growth. Balance now has real healer talents in its first three tiers: Genesis (+5% HoT healing), Nature's Majesty (+4% crit), Moonglow (-9% mana) and Nature's Splendor (longer Rejuvenation/Regrowth).

## Point allocation

### Balance (11)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Genesis** | 5/5 | **NEW** | Increases the periodic damage and healing done by your spells and abilities by 5%. |
| **Moonglow** | 3/3 | changed | Reduces the Mana cost of your damaging spells by 25%. |
| **Nature's Majesty** | 2/2 | **NEW** | Increases your critical strike chance with spells and melee attacks by 4%. |
| **Nature's Splendor** | 1/1 | **NEW** | Increases the duration of your Moonfire and Rejuvenation spells by 3 sec, your Regrowth spell by 6 sec, and your Insect Swarm spell by 2 sec. |

### Feral Combat (5)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Heart of the Wild** | 5/5 | changed | Increases your Intellect by 10%. In addition, while in Bear Form or Dire Bear Form your Stamina is increased by 20% and while in Cat Form your Strength is increased by 10%. |

### Restoration (35)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Nature's Focus** | 5/5 | changed | Gives you a 70% chance to avoid interruption caused by damage while casting Arcane and Nature spells. |
| **Naturalist** | 5/5 | **NEW** | Reduces the cast time of your Healing Touch spell by 0.5 sec and increases all damage you deal by 5%. |
| **Reflection** | 3/3 | changed | Allows 50% of your Mana regeneration to continue while casting. |
| **Gift of Nature** | 5/5 | changed | Increases the effect of all your healing spells by 10%. |
| **Gift of the Earthmother** | 1/1 | **NEW** | Reduces the global cooldown by 0.5 seconds on your Rejuvenation, Swiftmend, and Wild Growth spells. |
| **Tranquil Spirit** | 5/5 | unchanged | Reduces the mana cost of your Healing Touch and Tranquility spells by 10%. |
| **Improved Rejuvenation** | 3/3 | moved | Increases the effect of your Rejuvenation spell by 15%. |
| **Swiftmend** | 1/1 | changed | Instantly heals a target with an active Rejuvenation or Regrowth effect for an amount equal to the full duration of the periodic effect of one of those spells. |
| **Nature's Swiftness** | 1/1 | unchanged | When activated, your next Nature spell becomes an instant cast spell. |
| **Living Spirit** | 3/3 | **NEW** | Increases your Spirit by 15%. |
| **Improved Regrowth** | 2/5 | unchanged | Increases the critical effect chance of your Regrowth spell by 20%. |
| **Wild Growth** | 1/1 | **NEW** | Heals the target and their party for 336 over 7 sec. Party members must be within 43 yards of target. The amount healed is applied quickly at first, and slows down as Wild Growth reaches its full duration. |

## Core talents (priority order)

1. **Reflection** — Regen while casting (17%/rank est. 51%). Healer lab (2026-09-28): removing it costs +38% healing capacity.
2. **Moonglow** — -9% mana on all spells (est.). Healer lab (2026-09-28): removing it costs +30% healing capacity.
3. **Tranquil Spirit** — Healer lab (2026-09-28): removing it costs +9% healing capacity.
4. **Gift of Nature** — +10% healing (est.). Healer lab (2026-09-28): removing it costs +6% healing capacity.
5. **Living Spirit** — +15% Spirit (est.); Wild Growth prerequisite. Healer lab (2026-09-28): removing it costs +6% healing capacity.
6. **Nature's Splendor** — +3s Rejuvenation/Moonfire, +6s Regrowth. Healer lab (2026-09-28): removing it costs +2% healing capacity.
7. **Swiftmend** — Now a 16-point talent; per the reveal it no longer consumes the HoT. Healer lab (2026-09-28): removing it costs +2% healing capacity.
8. **Genesis** — New: +5% periodic healing (est.) — Rejuvenation, Regrowth HoT, Wild Growth. Healer lab (2026-09-28): removing it costs +2% healing capacity.

## Flex points

| Pts | Default | Alternatives | Why |
|---|---|---|---|
| 3 | Improved Rejuvenation | any utility talent legal at that tier | Measures +1.0% healing capacity in the healer lab (noise): these points are free to move. |
| 5 | Naturalist | any utility talent legal at that tier | Measures +0.4% healing capacity in the healer lab (noise): these points are free to move. |
| 1 | Nature's Swiftness | any utility talent legal at that tier | Measures +0.1% healing capacity in the healer lab (noise): these points are free to move. |
| 2 | Nature's Majesty | any utility talent legal at that tier | Measures +0.0% healing capacity in the healer lab (noise): these points are free to move. |
| 5 | Nature's Focus | any utility talent legal at that tier | Measures +0.0% healing capacity in the healer lab (noise): these points are free to move. |
| 1 | Wild Growth | any utility talent legal at that tier | Measures +0.0% healing capacity in the healer lab (noise): these points are free to move. |

## Rotation

A healer: not in the community simulator, see the healer lab section of the [raid README](../README.md).

## Notes

- Adopted from the healer lab on 2026-09-28: cand-resto-r2 beat the previous draft by +3.2% healing capacity.
- Improved Mark of the Wild is gone — check whether the buff was raised baseline.
- Insect Swarm moved to Balance tier 4 and is no longer a Gift of Nature prerequisite.

## Open questions (verify in the live game)

- Swiftmend without consuming the HoT: confirmed in the reveal, not visible in the demo tooltip.
- Wild Growth healing at 60 and its target cap (party only?).

## Sources

- <https://warcraftforever.games/talents/druid>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
