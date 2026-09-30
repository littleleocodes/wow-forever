# Shockadin — Holy/Retribution (PvP) — 31/0/20

*Paladin · Classic baseline*

| | |
|---|---|
| **Build** | 31/0/20 (Holy / Protection / Retribution) |
| **Role** | HEALER — PvP |
| **Status** | Primary |
| **Data** | Classic Era 1.12-era trees (validated against `_reference/data/classic-era-talents.json`) |
| **Forever** | This is the *baseline*; see the Forever status table below and `../forever/` for the adapted build |

## Summary

Holy Shock burst plus Illumination sustain, Unyielding Faith and Consecration, with Retribution for Improved Blessing of Might, Benediction, Improved Judgement, Improved Seal of the Crusader and Conviction. The classic Classic PvP paladin.

## Point allocation

### Holy (31)

| Talent | Pts | Effect at this rank |
|---|---|---|
| **Divine Strength** | 3/5 | Increases your Strength by 6%. |
| **Divine Intellect** | 5/5 | Increases your total Intellect by 10%. |
| **Spiritual Focus** | 5/5 | Gives your Flash of Light and Holy Light spells a 70% chance to not lose casting time when you take damage. |
| **Healing Light** | 3/3 | Increases the amount healed by your Holy Light and Flash of Light spells by 12%. |
| **Consecration** | 1/1 | Consecrates the land beneath Paladin, doing 64 Holy damage over 8 sec to enemies who enter the area. |
| **Unyielding Faith** | 2/2 | Increases your chance to resist Fear and Disorient effects by an additional 10%. |
| **Illumination** | 5/5 | After getting a critical effect from your Flash of Light, Holy Light, or Holy Shock heal spell, gives you a 100% chance to gain Mana equal to the base cost of the spell. |
| **Divine Favor** | 1/1 | When activated, gives your next Flash of Light, Holy Light, or Holy Shock spell a 100% critical effect chance. |
| **Holy Power** | 5/5 | Increases the critical effect chance of your Holy spells by 5%. |
| **Holy Shock** | 1/1 | Blasts the target with Holy energy, causing 204 to 220 Holy damage to an enemy, or 204 to 220 healing to an ally. |

### Protection (0)

*No points.*

### Retribution (20)

| Talent | Pts | Effect at this rank |
|---|---|---|
| **Improved Blessing of Might** | 5/5 | Increases the melee attack power bonus of your Blessing of Might by 20%. |
| **Benediction** | 5/5 | Reduces the Mana cost of your Judgement and Seal spells by 15%. |
| **Improved Judgement** | 2/2 | Decreases the cooldown of your Judgement spell by 2 sec. |
| **Improved Seal of the Crusader** | 3/3 | Increases the melee attack power bonus of your Seal of the Crusader and the Holy damage increase of your Judgement of the Crusader by 15%. |
| **Conviction** | 5/5 | Increases your chance to get a critical strike with melee weapons by 5%. |

## Core talents (priority order)

1. **Holy Shock** — Instant Holy damage or heal — the burst finisher.
2. **Divine Favor** — Guaranteed crit Holy Shock/Holy Light.
3. **Holy Power** — +5% Holy crit.
4. **Illumination** — Mana back on crits.
5. **Unyielding Faith** — Fear/disorient resistance.
6. **Improved Judgement** — Judgement every 8s.
7. **Conviction** — +5% melee crit.
8. **Consecration** — Breaks stealth, AoE pressure.

## Flex points

| Pts | Default | Alternatives | Why |
|---|---|---|---|
| 3 | Divine Strength | Improved Lay on Hands, Lasting Judgement | Reach 30 points in Holy for Holy Shock. |

## Notes

- Reckoning-bomb builds (Protection-heavy) are the other classic paladin PvP option; this build is the all-rounder.

## Forever status of every point in this build

Talent-by-talent check against the Forever beta-client trees (`../forever/talent-trees.md`).

| Tree | Talent | Pts | In Forever | Detail |
|---|---|---|---|---|
| Holy | Divine Strength | 3 | unchanged | tier 1, max 5 |
| Holy | Divine Intellect | 5 | unchanged | tier 1, max 5 |
| Holy | Spiritual Focus | 5 | changed | tier 2, max 2 — max rank 5 → 2; tooltip changed |
| Holy | Healing Light | 3 | changed | tier 2, max 3 — tooltip changed; was Holy row 3, col 1 |
| Holy | Consecration | 1 | **REMOVED** | removed from Classic |
| Holy | Unyielding Faith | 2 | changed | tier 2, max 2 — tooltip changed; was Holy row 3, col 4 |
| Holy | Illumination | 5 | changed | tier 4, max 5 — tooltip changed |
| Holy | Divine Favor | 1 | moved | tier 4, max 1 — was Holy row 5, col 2 |
| Holy | Holy Power | 5 | changed | tier 6, max 5 — tooltip changed; tooltip changed in build 1.60.1.70009 (ranks 1, 2, 3, 4, 5) |
| Holy | Holy Shock | 1 | changed | tier 5, max 1 — tooltip changed; was Holy row 7, col 2 |
| Retribution | Improved Blessing of Might | 5 | **REMOVED** | removed from Classic |
| Retribution | Benediction | 5 | changed | tier 1, max 5 — tooltip changed |
| Retribution | Improved Judgement | 2 | changed | tier 2, max 2 — tooltip changed |
| Retribution | Improved Seal of the Crusader | 3 | **REMOVED** | removed from Classic |
| Retribution | Conviction | 5 | changed | tier 2, max 5 — tooltip changed; was Retribution row 3, col 2 |

**9 point(s) of this build no longer exist in Forever** and must be re-spent; see `../forever/README.md` for how they were re-spent.

## Sources

- <https://www.wowhead.com/classic/guide/classes/paladin/healer-pvp-arena>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
