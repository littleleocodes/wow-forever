# Holy — Raid Healer (33/0/18) — 31/2/18

*[Paladin](../../../README.md) · [Raids: training dummy, raid and parse](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 31/2/18 (Holy / Protection / Retribution) |
| **Role** | HEALER — Raid |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70753 (2026-11-03 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |
| **Based on** | Classic baseline `holy-raid-healer` |

## Summary

Illumination (now requiring Reverence, the new regen-while-casting talent), Divine Favor, Healing Light, Holy Power, Infusion of Light and the Light's Vigil capstone in Holy; with Kings baseline and Improved Wisdom/Might gone, the remaining 20 points go to Retribution for Benediction (cheaper instants), Improved Judgement, Sanctified Judgement (mana on Judgement) and Pursuit of Justice.

## Point allocation

### Holy (31)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Divine Strength** | 3/5 | unchanged | Increases your Strength by 6%. |
| **Spiritual Focus** | 5/5 | changed | Gives your Flash of Light, Holy Light, and Light's Vigil spells a 70% chance to not lose casting time when you take damage. |
| **Healing Light** | 3/3 | changed | Increases the amount healed by your Holy Light, Flash of Light, and Holy Shock spells by 12%. |
| **Purifying Power** | 2/2 | **NEW** | Reduces the mana cost of your Cleanse and Purify spells by 20% and reduces the cooldown of your Exorcism and Holy Wrath spells by 33%. |
| **Reverence** | 2/2 | **NEW** | Allows 30% of your Mana regeneration to continue while casting. |
| **Divine Favor** | 1/1 | moved | When activated, gives your next Flash of Light, Holy Light, or Holy Shock spell a 100% critical effect chance. |
| **Illumination** | 5/5 | changed | After getting a critical effect from your Flash of Light, Holy Light, Light's Vigil, or Holy Shock heal spell you have a 100% chance to gain Mana equal to 50% of the base cost of the spell. |
| **Infusion of Light** | 2/2 | **NEW** | Your Holy Shock and Flash of Light critical hits reduce the cast time of your next Holy Light cast within 15 sec by 1.0 sec. |
| **Boundless Light** | 1/2 | **NEW** | Increases the critical strike chance of your Holy Shock spell by 15% when cast on allies not affected by your Oath of Light. |
| **Holy Shock** | 1/1 | changed | Blasts the target with Holy energy, causing 129 to 139 Holy damage to an enemy, or 110 to 118 healing to an ally. |
| **Holy Power** | 5/5 | changed | Increases the critical strike healing bonus of your Holy spells by 50%. |
| **Light's Vigil** | 1/1 | **NEW** | Applies Light's Vigil to a friendly target for 30 sec. The caster's next Holy Shock on the target incurs no cooldown and heals the target and their party for 325 to 343. Only one Vigil per Paladin may be active in each party. |

### Protection (2)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Divine Intellect** | 2/5 | unchanged | Increases your total Intellect by 4%. |

### Retribution (18)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Benediction** | 5/5 | changed | Reduces the Mana cost of all instant cast spells and abilities by 10%. |
| **Deflection** | 3/5 | moved | Increases your Parry chance by 3%. |
| **Conviction** | 3/3 | changed | Improves your chance to get a critical strike with all spells and attacks by 6%. |
| **Improved Judgement** | 2/2 | changed | Decreases the cooldown of your Judgement ability by 2 sec. |
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
11. **Sanctified Judgement** — New: Judgement returns 60% of the judged seal's mana cost at 3/3 (70291 tooltip: a 100% chance) — Judgement of Light/Wisdom for free.
12. **Improved Judgement** — -2s Judgement cooldown (est.).
13. **Purifying Power** — -20% mana on Cleanse (and Purify): a raid healer dispels in most boss fights.

## Flex points

| Pts | Default | Alternatives | Why |
|---|---|---|---|
| 3 | Deflection | Toughness 5 + Guardian's Favor 2 + Sacred Duty (Protection dip instead of Retribution) | Tier-1 Retribution filler; a Protection dip (Guardian's Favor, Sacred Duty's -30s Divine Shield) is the survivability alternative. |

## Rotation

A healer: not in the community simulator, see the healer lab section of the [raid README](../README.md).

## Notes

- Blessing of Kings is baseline and blessings last 1 hour in Forever — no paladin needs to spec for raid buffs.
- Divine Precision (+6% Holy hit at rank 1?) only matters if Forever lets heals miss; not taken.
- Build 1.60.1.70009 removed Crusade: its 2 points go to Conviction (3/5).
- 2026-09-27 scenario audit: Holy Conduit 2 -> Purifying Power 2. Holy Conduit returns mana on Consecration, Exorcism, Holy Wrath and Hammer of Wrath, none of which a raid healer casts. Purifying Power's cheaper Cleanse is mana spent on dispels every raid fight (scorer +0.5 points).
- 2026-10-31 (repair_builds.py, client build 1.60.1.70707 trees): 33/0/18 -> 31/2/18; Divine Intellect 5 gone (moved to Protection); Unyielding Faith 2 gone (moved to Retribution); Voice of Truth 1 gone; Reverence 3 -> 2 (rank cap); +1 Spiritual Focus (tier gating for Healing Light); +1 Spiritual Focus (tier gating for Healing Light); +1 Spiritual Focus (tier gating for Healing Light); +1 Boundless Light (tier gating for Holy Power); +1 Divine Strength (tier gating for Holy Power); +1 Divine Strength (tier gating for Holy Power); +1 Divine Strength (tier gating for Holy Power); refill +2 Divine Intellect (refill: the holy-heal model, raid-heal).

## Open questions (verify in the live game)

- Light's Vigil healing numbers and whether the party heal makes Holy Shock a raid-heal tool.
- Champion of the Light (Retribution tier 6, +33% of Intellect as healing) is unreachable with 31 Holy — a 21/0/30 'Champion' healer may be worth testing.
- Illumination rank scaling (20% per rank read at rank 1).

## Sources

- <https://warcraftforever.games/talents/paladin>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
