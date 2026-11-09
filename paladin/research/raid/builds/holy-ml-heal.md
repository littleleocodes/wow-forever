# Holy — Raid healing (machine-learning search) — 32/5/14

*[Paladin](../../../README.md) · [Raids: training dummy, raid and parse](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 32/5/14 (Holy / Protection / Retribution) |
| **Role** | HEALER — Raid |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70753 (2026-11-03 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

The Holy build the machine-learning talent search found in the healer lab on 2026-11-01 (heallab/deep_heal.py: a random forest guiding a genetic search over every legal build of the spec, the heal-choice policy tuned with it, races on fresh seeds, every build one or two moves from the winner checked). Capacity is the healer lab's model of stated assumptions.

## Point allocation

### Holy (32)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Spiritual Focus** | 5/5 | changed | Gives your Flash of Light, Holy Light, and Light's Vigil spells a 70% chance to not lose casting time when you take damage. |
| **Divine Strength** | 4/5 | unchanged | Increases your Strength by 8%. |
| **Healing Light** | 3/3 | changed | Increases the amount healed by your Holy Light, Flash of Light, and Holy Shock spells by 12%. |
| **Reverence** | 2/2 | **NEW** | Allows 30% of your Mana regeneration to continue while casting. |
| **Purifying Power** | 2/2 | **NEW** | Reduces the mana cost of your Cleanse and Purify spells by 20% and reduces the cooldown of your Exorcism and Holy Wrath spells by 33%. |
| **Divine Favor** | 1/1 | moved | When activated, gives your next Flash of Light, Holy Light, or Holy Shock spell a 100% critical effect chance. |
| **Illumination** | 5/5 | changed | After getting a critical effect from your Flash of Light, Holy Light, Light's Vigil, or Holy Shock heal spell you have a 100% chance to gain Mana equal to 50% of the base cost of the spell. |
| **Infusion of Light** | 1/2 | **NEW** | Your Holy Shock and Flash of Light critical hits reduce the cast time of your next Holy Light cast within 15 sec by 0.5 sec. |
| **Oath of Light** | 1/1 | **NEW** | Swear an Oath to protect target ally for 5 min, increasing the healing of your Holy Light on them by up to 400, your Flash of Light by up to 115, and your Holy Shock by up to 229. Only one Oath of Light may be sworn by the Paladin at any one time. |
| **Holy Shock** | 1/1 | changed | Blasts the target with Holy energy, causing 129 to 139 Holy damage to an enemy, or 110 to 118 healing to an ally. |
| **Boundless Light** | 1/2 | **NEW** | Increases the critical strike chance of your Holy Shock spell by 15% when cast on allies not affected by your Oath of Light. |
| **Holy Power** | 5/5 | changed | Increases the critical strike healing bonus of your Holy spells by 50%. |
| **Light's Vigil** | 1/1 | **NEW** | Applies Light's Vigil to a friendly target for 30 sec. The caster's next Holy Shock on the target incurs no cooldown and heals the target and their party for 325 to 343. Only one Vigil per Paladin may be active in each party. |

### Protection (5)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Divine Intellect** | 5/5 | unchanged | Increases your total Intellect by 10%. |

### Retribution (14)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Deflection** | 2/5 | moved | Increases your Parry chance by 2%. |
| **Benediction** | 5/5 | changed | Reduces the Mana cost of all instant cast spells and abilities by 10%. |
| **Conviction** | 3/3 | changed | Improves your chance to get a critical strike with all spells and attacks by 6%. |
| **Unyielding Faith** | 2/2 | changed | Reduces the duration of Fear and Disorient effects on you by 30%. |
| **Pursuit of Justice** | 2/2 | changed | Increases movement speed and mounted movement speed by 15%. This does not stack with other movement speed increasing effects. |

## Rotation

A healer: not in the community simulator, see the healer lab section of the [raid README](../README.md).

## Notes

- +24.7% capacity over the hand draft holy-raid-healer (over the 2% bar: the spec's healing pick; the hand draft stays as the alternative).
- Final race over 400 fresh seeds: capacity 0.629 ± 0.002; holy-raid-healer 0.505, opt-holy-heal-raid-heal 0.495.
- Independent runs agreeing in the last cycle: 2/2; two-move check: 595 one-move and 7,633 two-move builds, none better.
- The healer lab models one healer keeping a five-member group alive (heallab/tables.py); not an in-game measurement.
- 2026-11-09 page audit: Consecrated Ground 1 -> Holy Power 5/5, Improved Judgement 1 and Sanctified Judgement 1 -> Unyielding Faith 2/2 and Pursuit of Justice 2/2. The three points did nothing for a healer that never casts Consecration or Judgement. Healer lab, 200 runs: capacity 0.6237 -> 0.6242 in the five-minute fight, 0.4823 -> 0.4851 in the ten-minute fight (standard error 0.003 and 0.002). The other healing ranks left (Infusion of Light 2, Boundless Light 2) measured 1.1% lower. Fear and movement are not in the lab.
- 2026-11-09 page audit: Holy Conduit 1 -> Purifying Power 1 (Cleanse and Purify 10% cheaper; the lab has no debuffs). With Consecrated Ground gone the tree had a point to spare before Light's Vigil, so Holy Conduit opened nothing. Healer lab, 200 runs: 0.6242 and 0.4851 either way; Infusion of Light 2/2 measured 0.6184 and 0.4745, Boundless Light 2/2 0.6242 and 0.4834.
- 2026-11-09 page audit: Divine Strength 5 -> 4, Purifying Power 1 -> 2 (Cleanse and Purify 20% cheaper). Holy held 31 points before Light's Vigil, which needs 30, so the fifth Strength rank opened nothing and Strength does nothing for a healer. Healer lab, 60 runs: bit-identical (0.6357, 0.4926 in the ten-minute fight).

## Open questions (verify in the live game)

- A machine-searched Holy build: check it against the community's healing builds at launch.

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
