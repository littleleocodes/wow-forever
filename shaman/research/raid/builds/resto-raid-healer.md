# Restoration — Raid Healer (healer lab winner adopted 2026-09-26) — 0/10/41

*[Shaman](../../../README.md) · [Raids: training dummy, raid and parse](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 0/10/41 (Elemental / Enhancement / Restoration) |
| **Role** | HEALER — Raid |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70291 (2026-10-08 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |
| **Based on** | Classic baseline `resto-raid-healer` |

## Summary

Allocation adopted on 2026-09-26 from `cand-resto-r1`, the build with the highest healing capacity in the healer lab (+4.4% vs the previous draft; kept under raid/heallab/candidates/). Previous summary: Same 0/5/46 shape: Improved Healing Wave, Tidal Mastery (now tier 1), Tidal Focus (mana and 5% hit), Mindfulness (the new regen-while-casting talent), Ancestral Healing, Healing Focus, Water Shield, Totemic Focus, Restorative Totems, Mana Tide (now tier 4), Healing Way, Nature's Swiftness, Purification and the Riptide capstone, with Ancestral Knowledge from Enhancement.

## Point allocation

### Elemental (0)

*No points.*

### Enhancement (10)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Thundering Strikes** | 5/5 | changed | Improves your chance to get a critical strike with all spells and attacks by 5%. |
| **Ancestral Knowledge** | 5/5 | changed | Increases your Intellect by 10%. |

### Restoration (41)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Totemic Focus** | 5/5 | changed | Reduces the Mana cost of your totems and any spells that summon or move them by 25%. |
| **Mindfulness** | 3/3 | **NEW** | Allows 50% of your Mana regeneration to continue while casting. |
| **Tidal Focus** | 5/5 | changed | Reduces the Mana cost of your healing spells by 5% and improves your chance to hit by 5%. |
| **Water Shield** | 1/1 | **NEW** | The caster is surrounded by 3 globes of water. When a spell, melee, or ranged attack hits the caster or when one of the caster's healing spells gets a critical result, 2% of maximum mana is restored to the caster, expending one water globe. Only one globe will activate every few seconds. Lasts 10 min.  Only one Elemental Shield can be active on the Shaman at any one time. |
| **Ancestral Healing** | 3/3 | moved | Increases your target's armor value by 25% for 15 sec after getting a critical effect from one of your healing spells. |
| **Healing Focus** | 3/3 | changed | Gives you a 70% chance to avoid interruption caused by damage while casting any healing spell. |
| **Mana Tide Totem** | 1/1 | changed | Summons a Mana Tide Totem with 5 health at the feet of the caster for 12 sec that restores 88 mana every 3 seconds to group members within 30 yards. |
| **Restorative Totems** | 5/5 | changed | Increases the effect of your Mana Spring Totem by 25% and increases the effect of your Healing Stream Totem by 50%. |
| **Tidal Mastery** | 5/5 | changed | Increases the critical effect chance of your healing spells by 5%. |
| **Healing Way** | 3/3 | changed | Increases the amount healed by your Healing Wave spell by 25%. |
| **Nature's Swiftness** | 1/1 | unchanged | When activated, your next Nature spell with a casting time less than 10 sec. becomes an instant cast spell. |
| **Purification** | 5/5 | unchanged | Increases the effectiveness of your healing spells by 10%. |
| **Riptide** | 1/1 | **NEW** | Heals a friendly target for 485 to 533, an additional 445 over 15 sec, and increases the effectiveness of your Chain Heal casts directly on that target by 25%. |

## Core talents (priority order)

1. **Mindfulness** — New: 17%/rank regen while casting (est. 51%). Healer lab (2026-09-26): removing it costs +16% healing capacity.
2. **Healing Way** — +24% Healing Wave (est.); Riptide prerequisite. Healer lab (2026-09-26): removing it costs +8% healing capacity.
3. **Purification** — +10% healing. Healer lab (2026-09-26): removing it costs +5% healing capacity.
4. **Tidal Focus** — Cheaper heals plus 5% spell hit (est.). Healer lab (2026-09-26): removing it costs +5% healing capacity.
5. **Water Shield** — New: mana on being hit or on crit heals. Healer lab (2026-09-26): removing it costs +4% healing capacity.
6. **Mana Tide Totem** — Now a 16-point talent. Healer lab (2026-09-26): removing it costs +3% healing capacity.
7. **Ancestral Knowledge** — +10% Intellect (est.). Healer lab (2026-09-26): removing it costs +2% healing capacity.
8. **Ancestral Healing** — Armor on crit heals (8%/rank est. 24%). Healer lab (2026-09-26): removing it costs +2% healing capacity.

## Flex points

| Pts | Default | Alternatives | Why |
|---|---|---|---|
| 1 | Riptide | any utility talent legal at that tier | Measures +0.5% healing capacity in the healer lab (noise): these points are free to move. |
| 1 | Nature's Swiftness | any utility talent legal at that tier | Measures +0.5% healing capacity in the healer lab (noise): these points are free to move. |
| 5 | Totemic Focus | any utility talent legal at that tier | Measures +0.0% healing capacity in the healer lab (noise): these points are free to move. |
| 3 | Healing Focus | any utility talent legal at that tier | Measures +0.0% healing capacity in the healer lab (noise): these points are free to move. |

## Rotation

A healer: not in the community simulator, see the healer lab section of the [raid README](../README.md).

## Notes

- Adopted from the healer lab on 2026-09-26: cand-resto-r1 beat the previous draft by +4.4% healing capacity.
- Totemic Mastery (30-yard totems) is gone — check whether totem radius was raised baseline.

## Open questions (verify in the live game)

- Riptide numbers at 60; Water Shield mana per globe; Thundering Strikes vs. Ancestral Knowledge for a healer.

## Sources

- <https://warcraftforever.games/talents/shaman>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
