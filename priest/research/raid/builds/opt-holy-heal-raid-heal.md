# Optimizer — Raid healing mix: Greater Heal 35%, Flash Heal 20%, Renew 20%, Prayer of Healing 15%, Power Word: Shield 6%, Heal 4% (raid-heal) — 22/29/0

*[Priest](../../../README.md) · [Raids: training dummy, raid and parse](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 22/29/0 (Discipline / Holy / Shadow) |
| **Role** | HEALER — Raid |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70009 (2026-09-25 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

Produced by the stats model (`_reference/data/scorer/`) for spec model `holy-heal` and profile `raid-heal`: score +93.7% (healing score: 0.6 x HPS gain + 0.5 x mana gain vs. no talents). Every number behind it is in the effect files (tooltip-parsed or hand-entered with its arithmetic); change those, not this build.

## Point allocation

### Discipline (22)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Twin Disciplines** | 5/5 | **NEW** | Increases the damage and healing of your instant cast spells by 5%. |
| **Power in Light** | 2/5 | **NEW** | Your Smite and Penance spells deal 4% increased damage to targets afflicted with your Holy Fire. |
| **Improved Power Word: Shield** | 3/3 | changed | Increases the damage absorbed by your Power Word: Shield by 20%. |
| **Meditation** | 3/3 | changed | Allows 50% of your Mana regeneration to continue while casting. |
| **Inner Focus** | 1/1 | unchanged | When activated, reduces the Mana cost of your next spell by 100% and increases its critical effect chance by 25% if it is capable of a critical effect. |
| **Mental Agility** | 1/3 | changed | Reduces the mana cost of your Smite, Holy Fire, and instant cast spells by 3%. |
| **Mental Strength** | 5/5 | changed | Increases your total Intellect by 15%. |
| **Soul Warding** | 1/1 | **NEW** | Reduces the cooldown on your Power Word: Shield spell by 4 sec and reduces its mana cost by 15%. |
| **Penance** | 1/1 | **NEW** | Launches a volley of holy light at the target, causing 81 Holy damage to an enemy, or 184 healing to an ally, instantly and every 1 sec for 2 sec. |

### Holy (29)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Holy Specialization** | 5/5 | unchanged | Increases the critical effect chance of your Holy spells by 5%. |
| **Twilight Focus** | 3/3 | **NEW** | Gives you a 70% chance to avoid interruption caused by damage while casting any spell. |
| **Improved Renew** | 3/3 | unchanged | Increases the amount healed by your Renew spell by 15%. |
| **Divine Fury** | 1/5 | changed | Reduces the casting time of your Smite, Holy Fire, Heal, and Greater Heal spells by 0.1 sec. |
| **Inspiration** | 3/3 | changed | Your non-periodic critical heals increase your target's Armor by 25% for 15 sec. |
| **Holy Nova** | 1/1 | changed | Causes an explosion of holy light around the caster, causing 26 to 30 Holy damage to all enemy targets within 10 yards and healing all party members within 10 yards for 49 to 57. These effects cause no threat. |
| **Improved Healing** | 3/3 | changed | Reduces the Mana cost of your Lesser Heal, Heal, Greater Heal, Penance, and Prayer of Mending spells by 15%. |
| **Binding Heal** | 1/1 | **NEW** | Heals a friendly target and the caster for 236 to 284. Low threat. |
| **Litany of Light** | 2/2 | **NEW** | When you cast a healing spell, gain Mana equal to 10% of the base cost of the spell if your previous heal was a different spell. |
| **Spiritual Guidance** | 4/5 | changed | Increases your spell healing by up to 20% of your total Spirit and your spell damage by up to 6% of your total Spirit. |
| **Spiritual Healing** | 3/3 | changed | Increases the amount healed by your spells by 10%. |

### Shadow (0)

*No points.*

## Core talents (priority order)

1. **Meditation** — Removing it costs 34.5 points of score in this model.
2. **Improved Healing** — Removing it costs 13.1 points of score in this model.
3. **Penance** — Removing it costs 10.5 points of score in this model.
4. **Spiritual Healing** — Removing it costs 10.3 points of score in this model.
5. **Spiritual Guidance** — Removing it costs 6.4 points of score in this model.
6. **Mental Strength** — Removing it costs 5.1 points of score in this model.
7. **Inspiration** — Removing it costs 4.0 points of score in this model.
8. **Inner Focus** — Removing it costs 3.8 points of score in this model.

## Rotation

A healer: not in the community simulator, see the healer lab section of the [raid README](../README.md).

## Notes

- Report: priest/talents/forever/optimizer/holy-heal-raid-heal.md
- Promoted by rebuild.py on 2026-09-28: cand-holy-r1 had the highest healing capacity in the healer lab (0.623 vs 0.608).

## Open questions (verify in the live game)

- Hand-entered effect values (see the manual effect file) are the weakest inputs — verify the ones this build leans on.

## Sources

- <https://warcraftforever.games/talents/priest>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
