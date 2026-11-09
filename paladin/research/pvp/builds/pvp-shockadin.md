# Shockadin — Holy/Retribution (PvP) — 31/0/20

*[Paladin](../../../README.md) · [PvP](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 31/0/20 (Holy / Protection / Retribution) |
| **Role** | HEALER — PvP |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70753 (2026-11-03 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |
| **Based on** | Classic baseline `pvp-shockadin` |

## Summary

Holy Shock (tier 5) with Holy Power's +15% Holy Shock crit, Divine Favor, Light's Vigil, Voice of Truth (silence immunity) and Unyielding Faith; Retribution for Benediction, Improved Judgement, Conviction, Seal of Command, Sanctified Judgement and Crusade. Consecration is baseline, so nothing is lost there.

## Point allocation

### Holy (31)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Divine Strength** | 1/5 | unchanged | Increases your Strength by 2%. |
| **Spiritual Focus** | 5/5 | changed | Gives your Flash of Light, Holy Light, and Light's Vigil spells a 70% chance to not lose casting time when you take damage. |
| **Healing Light** | 3/3 | changed | Increases the amount healed by your Holy Light, Flash of Light, and Holy Shock spells by 12%. |
| **Purifying Power** | 2/2 | **NEW** | Reduces the mana cost of your Cleanse and Purify spells by 20% and reduces the cooldown of your Exorcism and Holy Wrath spells by 33%. |
| **Reverence** | 2/2 | **NEW** | Allows 30% of your Mana regeneration to continue while casting. |
| **Divine Favor** | 1/1 | moved | When activated, gives your next Flash of Light, Holy Light, or Holy Shock spell a 100% critical effect chance. |
| **Illumination** | 5/5 | changed | After getting a critical effect from your Flash of Light, Holy Light, Light's Vigil, or Holy Shock heal spell you have a 100% chance to gain Mana equal to 50% of the base cost of the spell. |
| **Divine Precision** | 1/2 | **NEW** | Improves your chance to hit with Holy spells by 4%, and reduces the duration of Silence effects on you by 10%. |
| **Infusion of Light** | 2/2 | **NEW** | Your Holy Shock and Flash of Light critical hits reduce the cast time of your next Holy Light cast within 15 sec by 1.0 sec. |
| **Boundless Light** | 2/2 | **NEW** | Increases the critical strike chance of your Holy Shock spell by 30% when cast on allies not affected by your Oath of Light. |
| **Holy Shock** | 1/1 | changed | Blasts the target with Holy energy, causing 129 to 139 Holy damage to an enemy, or 110 to 118 healing to an ally. |
| **Holy Power** | 5/5 | changed | Increases the critical strike healing bonus of your Holy spells by 50%. |
| **Light's Vigil** | 1/1 | **NEW** | Applies Light's Vigil to a friendly target for 30 sec. The caster's next Holy Shock on the target incurs no cooldown and heals the target and their party for 325 to 343. Only one Vigil per Paladin may be active in each party. |

### Protection (0)

*No points.*

### Retribution (20)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Benediction** | 5/5 | changed | Reduces the Mana cost of all instant cast spells and abilities by 10%. |
| **Conviction** | 3/3 | changed | Improves your chance to get a critical strike with all spells and attacks by 6%. |
| **Improved Judgement** | 2/2 | changed | Decreases the cooldown of your Judgement ability by 2 sec. |
| **Sanctified Judgement** | 3/3 | **NEW** | Gives your Judgement ability a 100% chance to return 60% of the Mana cost of the judged seal. |
| **Pursuit of Justice** | 2/2 | changed | Increases movement speed and mounted movement speed by 15%. This does not stack with other movement speed increasing effects. |
| **Seal of Command** | 1/1 | changed | Gives the Paladin a chance to deal additional Holy damage equal to 70% of normal weapon damage. Only one Seal can be active on the Paladin at any one time. Lasts 30 sec.  Unleashing this Seal's energy will judge an enemy, instantly causing 68 to 73 Holy damage, 137 to 145 if the target is stunned or incapacitated. |
| **Unyielding Faith** | 2/2 | changed | Reduces the duration of Fear and Disorient effects on you by 30%. |
| **Vindication** | 2/3 | changed | Gives your damaging melee attacks a chance to reduce the target's Attack Power by 136 for 30 sec. |

## Core talents (priority order)

1. **Holy Shock** — Instant Holy burst/heal.
2. **Holy Power** — +15% Holy Shock crit (est.).
3. **Divine Favor** — Guaranteed crit Holy Shock.
4. **Light's Vigil** — Cooldown-free Holy Shock on a marked target.
5. **Illumination** — Mana on crits.
6. **Unyielding Faith** — Shorter fears/disorients.
7. **Seal of Command** — Melee pressure.
8. **Improved Judgement** — Faster Judgements.
9. **Pursuit of Justice** — +8% movement (est. 16%).

## Flex points

| Pts | Default | Alternatives | Why |
|---|---|---|---|
| 3 | Sanctified Judgement 2 + Vindication 1 | Holy Conduit, Sanctified Judgement 3 | Tier-2/3 Retribution fillers. |

## Notes

- Divine Precision (Holy hit, requires Holy Shock) may be worth 2-3 points if Holy Shock misses are common in PvP.
- Build 1.60.1.70009 removed Crusade: Sanctified Judgement 3 and Vindication 2 instead.
- 2026-10-31 (repair_builds.py, client build 1.60.1.70707 trees): 31/0/20 -> 31/0/20; Divine Intellect 5 gone (moved to Protection); Unyielding Faith 2 gone (moved to Retribution); Voice of Truth 1 gone; Reverence 3 -> 2 (rank cap); Conviction 5 -> 3 (rank cap); +1 Spiritual Focus (tier gating for Healing Light); +1 Spiritual Focus (tier gating for Healing Light); +1 Spiritual Focus (tier gating for Healing Light); +1 Divine Precision (tier gating for Holy Shock); +1 Purifying Power (tier gating for Holy Shock); +1 Purifying Power (tier gating for Holy Power); +1 Boundless Light (tier gating for Holy Power); +1 Boundless Light (tier gating for Holy Power); +1 Divine Strength (tier gating for Holy Power); refill +2 Unyielding Faith (refill: the holy-heal model, pvp).
- 2026-11-09 page audit: core entries for talents the allocation no longer holds removed (Voice of Truth; a tree change or a repair took them out).

## Open questions (verify in the live game)

- Holy Shock damage at 60 (demo: 129-139 at level 38).

## Sources

- <https://warcraftforever.games/talents/paladin>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
