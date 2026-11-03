# Holy — PvP (derived) — 31/18/2

*[Paladin](../../../README.md) · [PvP](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 31/18/2 (Holy / Protection / Retribution) |
| **Role** | HEALER — PvP |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70753 (2026-11-03 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

The Holy PvP build derived on 2026-09-30 (derive_pvp.py): the stats model's PvP optimum with 30+ points in Holy (model holy-heal, profile pvp), then, among builds the model scores within 1% of that, the one the most talentsforever.com Holy builds agree with (2602 builds).

## Point allocation

### Holy (31)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Spiritual Focus** | 5/5 | changed | Gives your Flash of Light, Holy Light, and Light's Vigil spells a 70% chance to not lose casting time when you take damage. |
| **Healing Light** | 3/3 | changed | Increases the amount healed by your Holy Light, Flash of Light, and Holy Shock spells by 12%. |
| **Purifying Power** | 2/2 | **NEW** | Reduces the mana cost of your Cleanse and Purify spells by 20% and reduces the cooldown of your Exorcism and Holy Wrath spells by 33%. |
| **Reverence** | 2/2 | **NEW** | Allows 30% of your Mana regeneration to continue while casting. |
| **Divine Favor** | 1/1 | moved | When activated, gives your next Flash of Light, Holy Light, or Holy Shock spell a 100% critical effect chance. |
| **Illumination** | 5/5 | changed | After getting a critical effect from your Flash of Light, Holy Light, Light's Vigil, or Holy Shock heal spell you have a 100% chance to gain Mana equal to 50% of the base cost of the spell. |
| **Divine Precision** | 2/2 | **NEW** | Improves your chance to hit with Holy spells by 8%, and reduces the duration of Silence effects on you by 20%. |
| **Infusion of Light** | 2/2 | **NEW** | Your Holy Shock and Flash of Light critical hits reduce the cast time of your next Holy Light cast within 15 sec by 1.0 sec. |
| **Boundless Light** | 2/2 | **NEW** | Increases the critical strike chance of your Holy Shock spell by 30% when cast on allies not affected by your Oath of Light. |
| **Holy Shock** | 1/1 | changed | Blasts the target with Holy energy, causing 129 to 139 Holy damage to an enemy, or 110 to 118 healing to an ally. |
| **Holy Power** | 5/5 | changed | Increases the critical strike healing bonus of your Holy spells by 50%. |
| **Light's Vigil** | 1/1 | **NEW** | Applies Light's Vigil to a friendly target for 30 sec. The caster's next Holy Shock on the target incurs no cooldown and heals the target and their party for 325 to 343. Only one Vigil per Paladin may be active in each party. |

### Protection (18)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Divine Intellect** | 5/5 | unchanged | Increases your total Intellect by 10%. |
| **Guardian's Favor** | 2/2 | changed | Reduces the cooldown of your Blessing of Protection by 2 min and increases the duration of your Blessing of Freedom by 6 sec. |
| **Precision** | 1/3 | changed | Improves your chance to hit by 1%. |
| **Sacred Duty** | 2/2 | **NEW** | Reduces the cooldown of your Divine Shield, Divine Protection, and Templar's Bulwark spells by 60 sec, and reduces the duration of Forbearance by 10 sec. |
| **Improved Hammer of Justice** | 3/3 | moved | Decreases the cooldown of your Hammer of Justice spell by 15 sec. |
| **Toughness** | 2/5 | moved | Increases your armor value from items by 4%. |
| **Improved Righteous Fury** | 3/3 | changed | While Righteous Fury is active, all damage taken is reduced by 9%. |

### Retribution (2)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Deflection** | 2/5 | moved | Increases your Parry chance by 2%. |

## Core talents (priority order)

1. **Light's Vigil** — The scorer's value in this build: +11.6% of its score (model holy-heal).
2. **Holy Shock** — The scorer's value in this build: +9.5% of its score (model holy-heal).
3. **Spiritual Focus** — The scorer's value in this build: +8.8% of its score (model holy-heal).
4. **Divine Favor** — The scorer's value in this build: +8.2% of its score (model holy-heal).
5. **Unyielding Faith** — The scorer's value in this build: +8.0% of its score (model holy-heal).
6. **Voice of Truth** — The scorer's value in this build: +7.4% of its score (model holy-heal).

## Notes

- Community tie-break moves: 3 points Anticipation -> Precision; 1 point Illumination -> Divine Precision.
- Where we disagree with the community: most Holy builds take Illumination (78% take it), Benediction (77% take it), which the model values below this build's weakest point; this build takes Deflection (17%), Improved Hammer of Justice (10%), Improved Righteous Fury (16%), which few Holy builds take (the model values them). Pick rates cover every level-60 build on the site, not PvP builds only.
- PvP values are assumptions: no simulator plays PvP.
- 2026-10-31 (repair_builds.py, client build 1.60.1.70707 trees): 31/18/2 -> 31/18/2; Divine Intellect 5 gone (moved to Protection); Unyielding Faith 2 gone (moved to Retribution); Voice of Truth 1 gone; Reverence 3 -> 2 (rank cap); Divine Precision 3 -> 2 (rank cap); +1 Divine Intellect (tier gating for Guardian's Favor); +1 Divine Intellect (tier gating for Guardian's Favor); +1 Divine Intellect (tier gating for Guardian's Favor); +1 Divine Intellect (tier gating for Guardian's Favor); +1 Divine Intellect (tier gating for Guardian's Favor); +1 Spiritual Focus (tier gating for Healing Light); +1 Spiritual Focus (tier gating for Healing Light); +1 Spiritual Focus (tier gating for Healing Light); +1 Illumination (tier gating for Divine Precision); +1 Illumination (tier gating for Divine Precision); +1 Illumination (tier gating for Holy Shock); +1 Illumination (tier gating for Holy Power); +1 Illumination (tier gating for Holy Power); +1 Boundless Light (tier gating for Holy Power); +1 Boundless Light (tier gating for Holy Power); -1 Precision (over 51); -1 Precision (over 51); -1 Toughness (over 51); -1 Toughness (over 51); -1 Toughness (over 51) (refill: the holy-heal model, pvp).

## Open questions (verify in the live game)

- A derived Holy PvP build: check it in duels and battlegrounds at launch.

## Sources

- <https://talentsforever.com/paladin>
- <https://talentsforever.com/popular.js>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
