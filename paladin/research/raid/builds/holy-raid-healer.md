# Holy — Raid Healer (31/0/20) — 33/0/18

*[Paladin](../../../README.md) · [Raids: training dummy, raid and parse](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 33/0/18 (Holy / Protection / Retribution) |
| **Role** | HEALER — Raid |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70009 (2026-09-25 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |
| **Based on** | Classic baseline `holy-raid-healer` |

## Summary

Illumination (now requiring Reverence, the new regen-while-casting talent), Divine Favor, Healing Light, Holy Power, Infusion of Light and the Light's Vigil capstone in Holy; with Kings baseline and Improved Wisdom/Might gone, the remaining 20 points go to Retribution for Benediction (cheaper instants), Improved Judgement, Sanctified Judgement (mana on Judgement) and Pursuit of Justice.

## Point allocation

### Holy (33)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Divine Intellect** | 5/5 | unchanged | Increases your total Intellect by 10%. |
| **Healing Light** | 3/3 | changed | Increases the amount healed by your Holy Light, Flash of Light, and Holy Shock spells by 12%. |
| **Spiritual Focus** | 2/2 | changed | Gives your Flash of Light, Holy Light, and Light's Vigil spells a 70% chance to not lose casting time when you take damage. |
| **Unyielding Faith** | 2/2 | changed | Reduces the duration of Fear and Disorient effects on you by 30%. |
| **Voice of Truth** | 1/1 | **NEW** | Grants you immunity to Silence and Interrupt effects for 6 sec. |
| **Reverence** | 3/3 | **NEW** | Allows 30% of your Mana regeneration to continue while casting. |
| **Purifying Power** | 2/2 | **NEW** | Reduces the mana cost of your Cleanse and Purify spells by 20% and reduces the cooldown of your Exorcism and Holy Wrath spells by 33%. |
| **Infusion of Light** | 2/2 | **NEW** | Your Holy Shock and Flash of Light critical hits reduce the cast time of your next Holy Light cast within 15 sec by 1 sec. |
| **Illumination** | 5/5 | changed | After getting a critical effect from your Flash of Light, Holy Light, Light's Vigil, or Holy Shock heal spell you have a 100% chance to gain Mana equal to 50% of the base cost of the spell. |
| **Divine Favor** | 1/1 | moved | When activated, gives your next Flash of Light, Holy Light, or Holy Shock spell a 100% critical effect chance. |
| **Holy Shock** | 1/1 | changed | Blasts the target with Holy energy, causing 129 to 139 Holy damage to an enemy, or 110 to 118 healing to an ally. |
| **Holy Power** | 5/5 | changed | Increases the critical strike chance of your Holy Shock and Holy Strike spells by 15%, and all other spells by 5%. |
| **Light's Vigil** | 1/1 | **NEW** | Applies Light's Vigil to the target for 30 sec. Your next Holy Shock cast on them triggers no cooldown and causes enemy targets to suffer 175 to 189 Holy damage and refund 75% of Light's Vigil's Mana cost, or allied targets to heal their party for 325 to 343. You may only have one Light's Vigil active per party. |

### Protection (0)

*No points.*

### Retribution (18)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Deflection** | 3/5 | moved | Increases your Parry chance by 3%. |
| **Benediction** | 5/5 | changed | Reduces the Mana cost of all instant cast spells and abilities by 10%. |
| **Improved Judgement** | 2/2 | changed | Decreases the cooldown of your Judgement ability by 2 sec. |
| **Conviction** | 3/5 | changed | Improves your chance to get a critical strike with melee attacks by 3%. |
| **Sanctified Judgement** | 3/3 | **NEW** | Gives your Judgement ability a 100% chance to return 60% of the Mana cost of the judged seal. |
| **Pursuit of Justice** | 2/2 | changed | Increases movement speed and mounted movement speed by 15%. This does not stack with other movement speed increasing effects. |

## Core talents (priority order)

1. **Illumination** — Mana back on crit heals (20%/rank chance for 50% of base cost — est. 100% at 5/5); now requires Reverence 3.
2. **Light's Vigil** — New capstone: marks a target so the next Holy Shock on them has no cooldown and heals their party.
3. **Holy Shock** — Instant heal/damage; moved to tier 5 and prerequisite for Light's Vigil and Divine Precision.
4. **Holy Power** — +15% Holy Shock crit and +5% other spell crit (est.).
5. **Divine Favor** — Guaranteed crit Flash of Light/Holy Light/Holy Shock.
6. **Infusion of Light** — New: Holy Shock/Flash of Light crits shorten the next Holy Light by 0.5s per rank (est. 1.0s).
7. **Healing Light** — +12% Holy Light/Flash of Light/Holy Shock (est.).
8. **Reverence** — New: 10%/rank mana regen while casting (est. 30%).
9. **Divine Intellect** — Intellect.
10. **Benediction** — Now -2%/rank mana on all instant spells (est. 10%): Holy Shock, Judgements, blessings.
11. **Sanctified Judgement** — New: 33%/rank chance (est. 99%) to refund 20% of the judged seal's cost — Judgement of Light/Wisdom for free.
12. **Improved Judgement** — -2s Judgement cooldown (est.).
13. **Purifying Power** — -20% mana on Cleanse (and Purify): a raid healer dispels in most boss fights.

## Flex points

| Pts | Default | Alternatives | Why |
|---|---|---|---|
| 3 | Deflection | Toughness 5 + Guardian's Favor 2 + Sacred Duty (Protection dip instead of Retribution) | Tier-1 Retribution filler; a Protection dip (Guardian's Favor, Sacred Duty's -30s Divine Shield) is the survivability alternative. |
| 3 | Holy Conduit 2 + Conviction 1 | Vindication | Tier-2/3 Retribution gating fillers. |
| 2 | Crusade | Eye for an Eye | Tier-4 Retribution filler. |
| 3 | Unyielding Faith 2 + Voice of Truth 1 | Purifying Power, Improved Seals | Holy gating fillers; Voice of Truth (silence immunity) is a real cooldown. |

## Rotation

A healer: not in the community simulator, see the healer lab section of the [raid README](../README.md).

## Notes

- Blessing of Kings is baseline and blessings last 1 hour in Forever — no paladin needs to spec for raid buffs.
- Divine Precision (+6% Holy hit at rank 1?) only matters if Forever lets heals miss; not taken.
- Build 1.60.1.70009 removed Crusade: its 2 points go to Conviction (3/5).
- 2026-09-27 scenario audit: Holy Conduit 2 -> Purifying Power 2. Holy Conduit returns mana on Consecration, Exorcism, Holy Wrath and Hammer of Wrath, none of which a raid healer casts. Purifying Power's cheaper Cleanse is mana spent on dispels every raid fight (scorer +0.5 points).

## Open questions (verify in the live game)

- Light's Vigil healing numbers and whether the party heal makes Holy Shock a raid-heal tool.
- Champion of the Light (Retribution tier 6, +33% of Intellect as healing) is unreachable with 31 Holy — a 21/0/30 'Champion' healer may be worth testing.
- Illumination rank scaling (20% per rank read at rank 1).

## Sources

- <https://warcraftforever.games/talents/paladin>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
