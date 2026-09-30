# Optimizer — Raid healing: Chain Heal 45%, Healing Wave 35%, Lesser Healing Wave 15%, Healing Stream Totem 5% (raid-heal) — 0/10/41

*[Shaman](../../../README.md) · [Raids: training dummy, raid and parse](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 0/10/41 (Elemental / Enhancement / Restoration) |
| **Role** | HEALER — Raid |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70009 (2026-09-25 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

Produced by the stats model (`_reference/data/scorer/`) for spec model `resto-heal` and profile `raid-heal`: score +154.8% (healing score: 0.6 x HPS gain + 0.5 x mana gain vs. no talents). Every number behind it is in the effect files (tooltip-parsed or hand-entered with its arithmetic); change those, not this build.

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

1. **Mindfulness** — Removing it costs 37.5 points of score in this model.
2. **Healing Way** — Removing it costs 30.6 points of score in this model.
3. **Water Shield** — Removing it costs 15.4 points of score in this model.
4. **Purification** — Removing it costs 14.4 points of score in this model.
5. **Mana Tide Totem** — Removing it costs 11.3 points of score in this model.
6. **Tidal Focus** — Removing it costs 11.2 points of score in this model.
7. **Thundering Strikes** — Removing it costs 11.0 points of score in this model.
8. **Riptide** — Removing it costs 8.2 points of score in this model.

## Rotation

A healer: not in the community simulator, see the healer lab section of the [raid README](../README.md).

## Notes

- Report: shaman/research/talents/forever/optimizer/resto-heal-raid-heal.md

## Open questions (verify in the live game)

- Hand-entered effect values (see the manual effect file) are the weakest inputs — verify the ones this build leans on.

## Sources

- <https://warcraftforever.games/talents/shaman>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
