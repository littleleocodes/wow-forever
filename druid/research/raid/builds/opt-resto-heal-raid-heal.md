# Optimizer — Healing Touch 35%, Regrowth 30%, Rejuvenation 30%, Tranquility 5% (raid-heal) — 11/0/40

*[Druid](../../../README.md) · [Raids: training dummy, raid and parse](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 11/0/40 (Balance / Feral Combat / Restoration) |
| **Role** | HEALER — Raid |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70707 (2026-10-16 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

Produced by the stats model (`_reference/data/scorer/`) for spec model `resto-heal` and profile `raid-heal`: score +190.2% (healing score: 0.6 x HPS gain + 0.5 x mana gain vs. no talents). Every number behind it is in the effect files (tooltip-parsed or hand-entered with its arithmetic); change those, not this build.

## Point allocation

### Balance (11)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Genesis** | 5/5 | **NEW** | Increases the periodic damage and healing done by your spells and abilities by 10%. |
| **Moonglow** | 3/3 | changed | Reduces the Mana cost of your damaging spells by 25%. |
| **Nature's Majesty** | 2/2 | **NEW** | Increases your critical strike chance with spells and melee attacks by 4%. |
| **Nature's Splendor** | 1/1 | **NEW** | Increases the duration of your Moonfire and Rejuvenation spells by 3 sec, your Regrowth spell by 6 sec, and your Insect Swarm spell by 2 sec. |

### Feral Combat (0)

*No points.*

### Restoration (40)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Heart of the Wild** | 5/5 | changed | Increases your Intellect by 10%. In addition, while in Bear Form or Dire Bear Form your Stamina is increased by 20% and while in Cat Form your Strength is increased by 10%. |
| **Nature's Focus** | 5/5 | changed | Gives your Arcane and Nature spells a 70% chance to not lose casting time when you take damage. |
| **Naturalist** | 5/5 | **NEW** | Reduces the cast time of your Healing Touch and Wild Growth spells by 0.5 sec and increases all damage you deal by 10%. |
| **Reflection** | 3/3 | changed | Allows 50% of your Mana regeneration to continue while casting. |
| **Gift of Nature** | 5/5 | changed | Increases the effect of all your healing spells by 10%. |
| **Improved Rejuvenation** | 3/3 | moved | Increases the effect of your Rejuvenation spell by 15%. |
| **Swiftmend** | 1/1 | changed | Instantly heals a target with an active Rejuvenation or Regrowth effect for an amount equal to the full duration of the periodic effect of one of those spells. |
| **Tranquil Spirit** | 5/5 | unchanged | Reduces the mana cost of your Healing Touch and Tranquility spells by 10%. |
| **Living Spirit** | 3/3 | **NEW** | Increases your Spirit by 15%. |
| **Nature's Swiftness** | 1/1 | unchanged | When activated, your next Nature spell becomes an instant cast spell. |
| **Improved Regrowth** | 3/5 | unchanged | Increases the critical effect chance of your Regrowth spell by 30%. |
| **Wild Growth** | 1/1 | **NEW** | Heals the target and their party for 336 over 7 sec. Party members must be within 43 yards of target. The amount healed is applied quickly at first, and slows down as Wild Growth reaches its full duration. |

## Core talents (priority order)

1. **Moonglow** — Removing it costs 62.9 points of score in this model.
2. **Reflection** — Removing it costs 33.7 points of score in this model.
3. **Tranquil Spirit** — Removing it costs 24.4 points of score in this model.
4. **Gift of Nature** — Removing it costs 19.2 points of score in this model.
5. **Living Spirit** — Removing it costs 16.4 points of score in this model.
6. **Heart of the Wild** — Removing it costs 12.7 points of score in this model.
7. **Improved Rejuvenation** — Removing it costs 5.5 points of score in this model.
8. **Nature's Majesty** — Removing it costs 4.2 points of score in this model.

## Rotation

A healer: not in the community simulator, see the healer lab section of the [raid README](../README.md).

## Notes

- Report: druid/research/talents/forever/optimizer/resto-heal-raid-heal.md
- 2026-10-30 (repair_builds.py, client build 1.60.1.70707 trees): 11/5/35 -> 11/0/40; Gift of the Earthmother 1 gone; refill +1 Improved Regrowth (refill: the resto-heal model, raid-heal).

## Open questions (verify in the live game)

- Hand-entered effect values (see the manual effect file) are the weakest inputs — verify the ones this build leans on.

## Sources

- <https://warcraftforever.games/talents/druid>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
