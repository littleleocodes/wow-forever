# Holy — Raid Healer (31/11/9) — 31/11/9

*Paladin · Classic baseline*

| | |
|---|---|
| **Build** | 31/11/9 (Holy / Protection / Retribution) |
| **Role** | HEALER — Raid |
| **Status** | Primary |
| **Data** | Classic Era 1.12-era trees (validated against `_reference/data/classic-era-talents.json`) |
| **Forever** | This is the *baseline*; see the Forever status table below and `../forever/` for the adapted build |

## Summary

Holy to Holy Shock for Illumination, Divine Favor, Holy Power and Improved Blessing of Wisdom, then Blessing of Kings from Protection and Improved Blessing of Might from Retribution so the raid's blessings are covered. The Icy Veins/Wowhead standard.

## Point allocation

### Holy (31)

| Talent | Pts | Effect at this rank |
|---|---|---|
| **Divine Intellect** | 5/5 | Increases your total Intellect by 10%. |
| **Spiritual Focus** | 5/5 | Gives your Flash of Light and Holy Light spells a 70% chance to not lose casting time when you take damage. |
| **Healing Light** | 3/3 | Increases the amount healed by your Holy Light and Flash of Light spells by 12%. |
| **Improved Lay on Hands** | 2/2 | Gives the target of your Lay on Hands spell a 30% bonus to their armor value from items for 2 min. In addition, the cooldown for your Lay on Hands spell is reduced by 20 min. |
| **Unyielding Faith** | 2/2 | Increases your chance to resist Fear and Disorient effects by an additional 10%. |
| **Illumination** | 5/5 | After getting a critical effect from your Flash of Light, Holy Light, or Holy Shock heal spell, gives you a 100% chance to gain Mana equal to the base cost of the spell. |
| **Improved Blessing of Wisdom** | 2/2 | Increases the effect of your Blessing of Wisdom spell by 20%. |
| **Divine Favor** | 1/1 | When activated, gives your next Flash of Light, Holy Light, or Holy Shock spell a 100% critical effect chance. |
| **Holy Power** | 5/5 | Increases the critical effect chance of your Holy spells by 5%. |
| **Holy Shock** | 1/1 | Blasts the target with Holy energy, causing 204 to 220 Holy damage to an enemy, or 204 to 220 healing to an ally. |

### Protection (11)

| Talent | Pts | Effect at this rank |
|---|---|---|
| **Improved Devotion Aura** | 5/5 | Increases the armor bonus of your Devotion Aura by 25%. |
| **Guardian's Favor** | 2/2 | Reduces the cooldown of your Blessing of Protection by 120 sec and increases the duration of your Blessing of Freedom by 6 sec. |
| **Toughness** | 3/5 | Increases your armor value from items by 6%. |
| **Blessing of Kings** | 1/1 | Places a Blessing on the friendly target, increasing total stats by 10% for 5 min. Players may only have one Blessing on them per Paladin at any one time. |

### Retribution (9)

| Talent | Pts | Effect at this rank |
|---|---|---|
| **Improved Blessing of Might** | 5/5 | Increases the melee attack power bonus of your Blessing of Might by 20%. |
| **Benediction** | 4/5 | Reduces the Mana cost of your Judgement and Seal spells by 12%. |

## Core talents (priority order)

1. **Illumination** — Crit heals refund their mana — the engine of paladin healing.
2. **Divine Favor** — Guaranteed crit Holy Light every 2 minutes (with Illumination, a free big heal).
3. **Holy Power** — +5% Holy crit.
4. **Healing Light** — +12% Holy Light / Flash of Light.
5. **Divine Intellect** — +10% Intellect: mana and crit.
6. **Spiritual Focus** — 70% pushback resistance on Flash of Light/Holy Light.
7. **Blessing of Kings** — +10% all stats raid buff; one paladin must have it.
8. **Improved Blessing of Wisdom** — +20% Wisdom for the casters.
9. **Improved Blessing of Might** — +20% Might for the melee.
10. **Guardian's Favor** — Shorter Blessing of Protection cooldown, longer Freedom.
11. **Holy Shock** — Instant emergency heal (weak, but a 1-point instant).

## Flex points

| Pts | Default | Alternatives | Why |
|---|---|---|---|
| 2 | Unyielding Faith | Lasting Judgement, Consecration 1 + Improved Seal of Righteousness 1 | Fear/disorient resistance vs. utility; these are the 29th/30th Holy points. |
| 2 | Improved Lay on Hands | Consecration + Lasting Judgement | Makes Lay on Hands a real tank cooldown (armor + shorter cooldown). |
| 4 | Benediction | Toughness (to 5) + Deflection | Pure filler: cheaper Seals/Judgements. |
| 8 | Improved Devotion Aura 5 + Toughness 3 | Redoubt, Precision | Filler to reach Blessing of Kings. |

## Notes

- Flash of Light spam with Holy Light (Divine Favor) for big hits; Judgement of Light/Wisdom on the boss if a Ret paladin is not doing it.
- If another paladin covers Kings and Might, move those 11+9 points into Improved Concentration Aura / Improved Hammer of Justice (PvP-friendly variant).

## Forever status of every point in this build

Talent-by-talent check against the Forever beta-client trees (`../forever/talent-trees.md`).

| Tree | Talent | Pts | In Forever | Detail |
|---|---|---|---|---|
| Holy | Divine Intellect | 5 | unchanged | tier 1, max 5 |
| Holy | Spiritual Focus | 5 | changed | tier 2, max 2 — max rank 5 → 2; tooltip changed |
| Holy | Healing Light | 3 | changed | tier 2, max 3 — tooltip changed; was Holy row 3, col 1 |
| Holy | Improved Lay on Hands | 2 | **REMOVED** | removed from Classic |
| Holy | Unyielding Faith | 2 | changed | tier 2, max 2 — tooltip changed; was Holy row 3, col 4 |
| Holy | Illumination | 5 | changed | tier 4, max 5 — tooltip changed |
| Holy | Improved Blessing of Wisdom | 2 | **REMOVED** | removed from Classic |
| Holy | Divine Favor | 1 | moved | tier 4, max 1 — was Holy row 5, col 2 |
| Holy | Holy Power | 5 | changed | tier 6, max 5 — tooltip changed; tooltip changed in build 1.60.1.70009 (ranks 1, 2, 3, 4, 5) |
| Holy | Holy Shock | 1 | changed | tier 5, max 1 — tooltip changed; was Holy row 7, col 2 |
| Protection | Improved Devotion Aura | 5 | **REMOVED** | removed from Classic |
| Protection | Guardian's Favor | 2 | changed | tier 2, max 2 — tooltip changed |
| Protection | Toughness | 3 | moved | tier 1, max 5 — was Protection row 2, col 4 |
| Protection | Blessing of Kings | 1 | **REMOVED** | removed from Classic |
| Retribution | Improved Blessing of Might | 5 | **REMOVED** | removed from Classic |
| Retribution | Benediction | 4 | changed | tier 1, max 5 — tooltip changed |

**15 point(s) of this build no longer exist in Forever** and must be re-spent; see `../forever/README.md` for how they were re-spent.

## Sources

- <https://www.icy-veins.com/wow-classic/holy-paladin-healer-pve-spec-builds-talents>
- <https://www.wowhead.com/classic/guide/classes/paladin/healer-talent-builds-pve>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
