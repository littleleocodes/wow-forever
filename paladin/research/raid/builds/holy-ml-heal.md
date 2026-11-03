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
| **Divine Strength** | 5/5 | unchanged | Increases your Strength by 10%. |
| **Healing Light** | 3/3 | changed | Increases the amount healed by your Holy Light, Flash of Light, and Holy Shock spells by 12%. |
| **Reverence** | 2/2 | **NEW** | Allows 30% of your Mana regeneration to continue while casting. |
| **Divine Favor** | 1/1 | moved | When activated, gives your next Flash of Light, Holy Light, or Holy Shock spell a 100% critical effect chance. |
| **Illumination** | 5/5 | changed | After getting a critical effect from your Flash of Light, Holy Light, Light's Vigil, or Holy Shock heal spell you have a 100% chance to gain Mana equal to 50% of the base cost of the spell. |
| **Holy Conduit** | 1/2 | **NEW** | Reduces the mana cost of your Consecration, Holy Wrath, Exorcism, and Hammer of Wrath spells by 20%. |
| **Infusion of Light** | 1/2 | **NEW** | Your Holy Shock and Flash of Light critical hits reduce the cast time of your next Holy Light cast within 15 sec by 0.5 sec. |
| **Oath of Light** | 1/1 | **NEW** | Swear an Oath to protect target ally for 5 min, increasing the healing of your Holy Light on them by up to 400, your Flash of Light by up to 115, and your Holy Shock by up to 229. Only one Oath of Light may be sworn by the Paladin at any one time. |
| **Consecrated Ground** | 1/2 | **NEW** | Gives your Holy spells 5% increased damage against the first 4 enemies that enter your Consecration. |
| **Holy Shock** | 1/1 | changed | Blasts the target with Holy energy, causing 129 to 139 Holy damage to an enemy, or 110 to 118 healing to an ally. |
| **Boundless Light** | 1/2 | **NEW** | Increases the critical strike chance of your Holy Shock spell by 15% when cast on allies not affected by your Oath of Light. |
| **Holy Power** | 4/5 | changed | Increases the critical strike healing bonus of your Holy spells by 40%. |
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
| **Improved Judgement** | 1/2 | changed | Decreases the cooldown of your Judgement ability by 1 sec. |
| **Conviction** | 3/3 | changed | Improves your chance to get a critical strike with all spells and attacks by 6%. |
| **Sanctified Judgement** | 1/3 | **NEW** | Gives your Judgement ability a 33% chance to return 20% of the Mana cost of the judged seal. |
| **Unyielding Faith** | 1/2 | changed | Reduces the duration of Fear and Disorient effects on you by 15%. |
| **Pursuit of Justice** | 1/2 | changed | Increases movement speed and mounted movement speed by 8%. This does not stack with other movement speed increasing effects. |

## Rotation

A healer: not in the community simulator, see the healer lab section of the [raid README](../README.md).

## Notes

- +24.7% capacity over the hand draft holy-raid-healer (over the 2% bar: the spec's healing pick; the hand draft stays as the alternative).
- Final race over 400 fresh seeds: capacity 0.629 ± 0.002; holy-raid-healer 0.505, opt-holy-heal-raid-heal 0.495.
- Independent runs agreeing in the last cycle: 2/2; two-move check: 595 one-move and 7,633 two-move builds, none better.
- The healer lab models one healer keeping a five-member group alive (heallab/tables.py); not an in-game measurement.

## Open questions (verify in the live game)

- A machine-searched Holy build: check it against the community's healing builds at launch.

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
