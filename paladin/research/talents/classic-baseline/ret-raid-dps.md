# Retribution — DPS (11/0/40) — 11/0/40

*Paladin · Classic baseline*

| | |
|---|---|
| **Build** | 11/0/40 (Holy / Protection / Retribution) |
| **Role** | DPS — Raid |
| **Status** | Alternative |
| **Data** | Classic Era 1.12-era trees (validated against `_reference/data/classic-era-talents.json`) |
| **Forever** | This is the *baseline*; see the Forever status table below and `../forever/` for the adapted build |

## Summary

Seal of Command two-hander DPS with Vengeance, Sanctity Aura and Repentance, Divine Strength/Intellect and Consecration from Holy. Brings Improved Blessing of Might, Sanctity Aura and Judgements to a melee group; personal DPS is mid-pack in Classic Era.

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

## Core talents (priority order)

1. **Seal of Command** — Proc-based Holy damage on hits — the entire Ret damage model with a slow two-hander.
2. **Vengeance** — +15% damage after a crit.
3. **Sanctity Aura** — +10% Holy damage for the group.
4. **Conviction** — +5% melee crit.
5. **Two-Handed Weapon Specialization** — +3% two-hander damage.
6. **Divine Strength** — +10% Strength.
7. **Improved Seal of the Crusader** — +15% to Judgement of the Crusader — the raid's Holy damage debuff.
8. **Improved Judgement** — 8s Judgement cooldown.
9. **Benediction** — -15% Seal/Judgement mana.
10. **Repentance** — Incapacitate on a 1-minute cooldown.
11. **Consecration** — AoE damage/threat and free extra damage on single targets when mana allows.

## Flex points

| Pts | Default | Alternatives | Why |
|---|---|---|---|
| 5 | Deflection | Vindication 3 + Eye for an Eye 2 | Filler; Deflection is survivability, the alternatives are PvP-only (bosses are immune to Vindication). |
| 2 | Improved Retribution Aura | Pursuit of Justice (already 2/2), Eye for an Eye | Reflect damage on the melee group. |

## Notes

- Seal of Command + Judgement of the Crusader (kept up by one paladin) with Consecration when mana allows; auto-attack does most of the work — a slow 3.6+ two-hander is required.
- Consider 0/8/43 with Precision (+3% hit) only if hit is your problem and you can drop Divine Strength/Intellect.

## Forever status of every point in this build

Talent-by-talent check against the Forever beta-client trees (`../forever/talent-trees.md`).

| Tree | Talent | Pts | In Forever | Detail |
|---|---|---|---|---|
| Holy | Divine Strength | 5 | unchanged | tier 1, max 5 — moved in build 1.60.1.70707: was row 1, col 2 |
| Holy | Divine Intellect | 5 | moved-tree | now in Protection, tier 1 |
| Holy | Consecration | 1 | **REMOVED** | removed from Classic |
| Retribution | Improved Blessing of Might | 5 | **REMOVED** | removed from Classic |
| Retribution | Benediction | 5 | changed | tier 1, max 5 — tooltip changed |
| Retribution | Improved Judgement | 2 | changed | tier 2, max 2 — tooltip changed |
| Retribution | Improved Seal of the Crusader | 3 | **REMOVED** | removed from Classic |
| Retribution | Deflection | 5 | moved | tier 1, max 5 — was Retribution row 2, col 3 |
| Retribution | Conviction | 5 | changed | tier 2, max 3 — tooltip changed; was Retribution row 3, col 2; moved in build 1.60.1.70707: was row 2, col 3; max rank 5 -> 3 in build 1.60.1.70707; tooltip changed in build 1.60.1.70707 (ranks 1, 2, 3) |
| Retribution | Seal of Command | 1 | changed | tier 3, max 1 — tooltip changed; tooltip changed in build 1.60.1.70707 (ranks 1) |
| Retribution | Pursuit of Justice | 2 | changed | tier 3, max 2 — tooltip changed |
| Retribution | Improved Retribution Aura | 2 | **REMOVED** | removed from Classic |
| Retribution | Two-Handed Weapon Specialization | 3 | unchanged | tier 4, max 3 — moved in build 1.60.1.70707: was row 5, col 1; tooltip changed in build 1.60.1.70707 (ranks 1, 2, 3) |
| Retribution | Sanctity Aura | 1 | **REMOVED** | removed from Classic |
| Retribution | Vengeance | 5 | changed | tier 5, max 3 — max rank 5 → 3; tooltip changed; was Retribution row 6, col 2; moved in build 1.60.1.70707: was row 5, col 2; prerequisite changed in build 1.60.1.70707: was sanctified judgement |
| Retribution | Repentance | 1 | moved | tier 5, max 1 — was Retribution row 7, col 2; moved in build 1.60.1.70707: was row 5, col 3 |

**12 point(s) of this build no longer exist in Forever** and must be re-spent; see `../forever/README.md` for how they were re-spent.

## Sources

- <https://www.wowhead.com/classic/guide/classes/paladin/retribution/dps-talent-builds-pve>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
