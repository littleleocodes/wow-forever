# Leveling — Retribution (Seal of Command at 20) — 11/0/40

*Paladin · Classic baseline*

| | |
|---|---|
| **Build** | 11/0/40 (Holy / Protection / Retribution) |
| **Role** | DPS — Leveling |
| **Status** | Primary |
| **Data** | Classic Era 1.12-era trees (validated against `_reference/data/classic-era-talents.json`) |
| **Forever** | This is the *baseline*; see the Forever status table below and `../forever/` for the adapted build |

## Summary

Retribution from 10: Benediction/Improved Judgement early, Seal of Command at 20, Conviction, Two-Handed Weapon Specialization, Sanctity Aura, Vengeance at 39 and Repentance at 40, then Improved Blessing of Might and Holy for Divine Strength/Intellect/Consecration. Ends in the 11/0/40 Ret build.

## Point allocation

### Holy (11)

| Talent | Pts | Effect at this rank |
|---|---|---|
| **Divine Strength** | 5/5 | Increases your Strength by 10%. |
| **Divine Intellect** | 5/5 | Increases your total Intellect by 10%. |
| **Consecration** | 1/1 | Consecrates the land beneath Paladin, doing 64 Holy damage over 8 sec to enemies who enter the area. |

### Protection (0)

*No points.*

### Retribution (40)

| Talent | Pts | Effect at this rank |
|---|---|---|
| **Improved Blessing of Might** | 5/5 | Increases the melee attack power bonus of your Blessing of Might by 20%. |
| **Benediction** | 5/5 | Reduces the Mana cost of your Judgement and Seal spells by 15%. |
| **Improved Judgement** | 2/2 | Decreases the cooldown of your Judgement spell by 2 sec. |
| **Improved Seal of the Crusader** | 3/3 | Increases the melee attack power bonus of your Seal of the Crusader and the Holy damage increase of your Judgement of the Crusader by 15%. |
| **Deflection** | 5/5 | Increases your Parry chance by 5%. |
| **Conviction** | 5/5 | Increases your chance to get a critical strike with melee weapons by 5%. |
| **Seal of Command** | 1/1 | Gives the Paladin a chance to deal additional Holy damage equal to 70% of normal weapon damage. Only one Seal can be active on the Paladin at any one time. Lasts 30 sec.Unleashing this Seal's energy will judge an enemy, instantly causing 90 to 95 Holy damage, 137 to 146 if the target is stunned or incapacitated. |
| **Pursuit of Justice** | 2/2 | Increases movement and mounted movement speed by 8%. This does not stack with other movement speed increasing effects. |
| **Improved Retribution Aura** | 2/2 | Increases the damage done by your Retribution Aura by 50%. |
| **Two-Handed Weapon Specialization** | 3/3 | Increases the damage you deal with two-handed melee weapons by 6%. |
| **Sanctity Aura** | 1/1 | Increases Holy damage done by party members within 30 yards by 10%. Players may only have one Aura on them per Paladin at any one time. |
| **Vengeance** | 5/5 | Gives you a 15% bonus to Physical and Holy damage you deal for 8 sec after dealing a critical strike from a weapon swing, spell, or ability. |
| **Repentance** | 1/1 | Puts the enemy target in a state of meditation, incapacitating them for up to 6 sec. Any damage caused will awaken the target. Only works against Humanoids. |

## Leveling order

| Levels | Tree | Talent | Pts | Running total |
|---|---|---|---|---|
| 10-14 | Retribution | Benediction | 5 | 0/0/5 |
| 15-16 | Retribution | Improved Judgement | 2 | 0/0/7 |
| 17-19 | Retribution | Improved Seal of the Crusader | 3 | 0/0/10 |
| 20 | Retribution | Seal of Command | 1 | 0/0/11 |
| 21-25 | Retribution | Conviction | 5 | 0/0/16 |
| 26-27 | Retribution | Pursuit of Justice | 2 | 0/0/18 |
| 28-29 | Retribution | Improved Retribution Aura | 2 | 0/0/20 |
| 30-32 | Retribution | Two-Handed Weapon Specialization | 3 | 0/0/23 |
| 33 | Retribution | Sanctity Aura | 1 | 0/0/24 |
| 34 | Retribution | Improved Blessing of Might | 1 | 0/0/25 |
| 35-39 | Retribution | Vengeance | 5 | 0/0/30 |
| 40 | Retribution | Repentance | 1 | 0/0/31 |
| 41-44 | Retribution | Improved Blessing of Might | 4 | 0/0/35 |
| 45-49 | Retribution | Deflection | 5 | 0/0/40 |
| 50-54 | Holy | Divine Strength | 5 | 5/0/40 |
| 55-59 | Holy | Divine Intellect | 5 | 10/0/40 |
| 60 | Holy | Consecration | 1 | 11/0/40 |

## Core talents (priority order)

1. **Seal of Command** — The leveling damage engine at 20 — get a slow two-hander.
2. **Conviction** — Crit.
3. **Vengeance** — +15% damage after crits at 39.
4. **Benediction** — Mana efficiency for seals/judgements from level 10.

## Notes

- Seal of Command -> Judgement on cooldown -> auto-attack; heal with Holy Light between pulls, Consecration at 60 for multi-target.

## Forever status of every point in this build

Talent-by-talent check against the Forever beta-client trees (`../forever/talent-trees.md`).

| Tree | Talent | Pts | In Forever | Detail |
|---|---|---|---|---|
| Holy | Divine Strength | 5 | unchanged | tier 1, max 5 — moved in build 1.60.1.70753: was row 1, col 2 |
| Holy | Divine Intellect | 5 | moved-tree | now in Protection, tier 1 |
| Holy | Consecration | 1 | **REMOVED** | removed from Classic |
| Retribution | Improved Blessing of Might | 5 | **REMOVED** | removed from Classic |
| Retribution | Benediction | 5 | changed | tier 1, max 5 — tooltip changed |
| Retribution | Improved Judgement | 2 | changed | tier 2, max 2 — tooltip changed |
| Retribution | Improved Seal of the Crusader | 3 | **REMOVED** | removed from Classic |
| Retribution | Deflection | 5 | moved | tier 1, max 5 — was Retribution row 2, col 3 |
| Retribution | Conviction | 5 | changed | tier 2, max 3 — tooltip changed; was Retribution row 3, col 2; moved in build 1.60.1.70753: was row 2, col 3; max rank 5 -> 3 in build 1.60.1.70753; tooltip changed in build 1.60.1.70753 (ranks 1, 2, 3) |
| Retribution | Seal of Command | 1 | changed | tier 3, max 1 — tooltip changed; tooltip changed in build 1.60.1.70753 (ranks 1) |
| Retribution | Pursuit of Justice | 2 | changed | tier 3, max 2 — tooltip changed |
| Retribution | Improved Retribution Aura | 2 | **REMOVED** | removed from Classic |
| Retribution | Two-Handed Weapon Specialization | 3 | unchanged | tier 4, max 3 — moved in build 1.60.1.70753: was row 5, col 1; tooltip changed in build 1.60.1.70753 (ranks 1, 2, 3) |
| Retribution | Sanctity Aura | 1 | **REMOVED** | removed from Classic |
| Retribution | Vengeance | 5 | changed | tier 5, max 3 — max rank 5 → 3; tooltip changed; was Retribution row 6, col 2; moved in build 1.60.1.70753: was row 5, col 2; tooltip changed in build 1.60.1.70753 (ranks 1, 2, 3); prerequisite changed in build 1.60.1.70753: was sanctified judgement |
| Retribution | Repentance | 1 | moved | tier 5, max 1 — was Retribution row 7, col 2; moved in build 1.60.1.70753: was row 5, col 3 |

**12 point(s) of this build no longer exist in Forever** and must be re-spent; see `../forever/README.md` for how they were re-spent.

## Sources

- <https://www.wowhead.com/classic/guide/classes/paladin/leveling-talents>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
