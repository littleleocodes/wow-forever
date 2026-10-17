# Restoration — Leveling into the raid build — 0/10/41

*[Shaman](../../../README.md) · [Leveling and solo play](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 0/10/41 (Elemental / Enhancement / Restoration) |
| **Role** | DPS — Leveling |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70425 (2026-10-16 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

Level with the talents of the Restoration raid build (resto-raid-healer) so you arrive at 60 ready to heal; the order is the fastest of three the fight lab raced (stats model's order: 45 s per kill over levels 20-60, the enhancement-dps rotation).

## Point allocation

### Elemental (0)

*No points.*

### Enhancement (10)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Ancestral Knowledge** | 5/5 | changed | Increases your Intellect by 10%. |
| **Thundering Strikes** | 5/5 | changed | Improves your chance to get a critical strike with all spells and attacks by 5%. |

### Restoration (41)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Tidal Focus** | 5/5 | changed | Reduces the Mana cost of your healing spells by 5% and improves your chance to hit by 5%. |
| **Mindfulness** | 3/3 | **NEW** | Allows 50% of your Mana regeneration to continue while casting. |
| **Totemic Focus** | 5/5 | changed | Reduces the Mana cost of your totems and any spells that summon or move them by 25%. |
| **Ancestral Healing** | 3/3 | moved | Increases your target's armor value by 25% for 15 sec after getting a critical effect from one of your healing spells. |
| **Healing Focus** | 3/3 | changed | Gives you a 70% chance to avoid interruption caused by damage while casting any healing spell. |
| **Water Shield** | 1/1 | **NEW** | The caster is surrounded by 3 globes of water. When a spell, melee, or ranged attack hits the caster or when one of the caster's spells gets a critical result, 2% of maximum mana is restored to the caster, expending one water globe. Only one globe will activate every few seconds. Lasts 10 min.  Only one Elemental Shield can be active on the Shaman at any one time. |
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

## Leveling rotation

Not simulated in the fight lab; the class's leveling priority is on the [leveling rotation page](../rotation.md).

## Notes

- 2026-10-15 (raid_path_leveling.py, user decision): healer and tank specs level into their raid build. Orders raced (fight lab, seed 3, 3000 fights per level, level-weighted): stats model's order 45 s; own tree first 46 s; own tree last 45 s. First Restoration point at level 10.
- Fight-lab numbers are a model of the beta, not in-game measurements.
- 2026-10-16 (repair_builds.py, client build 70425 trees): 0/10/41 -> 0/10/41; order dropped (order_repair.py) (refill: the enhancement-dps model, leveling-st).

## Open questions (verify in the live game)

- Check the Restoration leveling pace at launch; the raid build's talents may cost speed early.

## Sources

- <https://warcraftforever.games/talents/shaman>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
