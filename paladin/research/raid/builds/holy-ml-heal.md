# Holy — Raid healing (machine-learning search) — 33/12/6

*[Paladin](../../../README.md) · [Raids: training dummy, raid and parse](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 33/12/6 (Holy / Protection / Retribution) |
| **Role** | HEALER — Raid |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70707 (2026-10-16 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

The Holy build the machine-learning talent search found in the healer lab on 2026-10-21 (heallab/deep_heal.py: a random forest guiding a genetic search over every legal build of the spec, the heal-choice policy tuned with it, races on fresh seeds, every build one or two moves from the winner checked). Capacity is the healer lab's model of stated assumptions.

## Point allocation

### Holy (33)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Divine Strength** | 5/5 | unchanged | Increases your Strength by 10%. |
| **Divine Intellect** | 5/5 | unchanged | Increases your total Intellect by 10%. |
| **Healing Light** | 3/3 | changed | Increases the amount healed by your Holy Light, Flash of Light, and Holy Shock spells by 12%. |
| **Spiritual Focus** | 1/2 | changed | Gives your Flash of Light, Holy Light, and Light's Vigil spells a 35% chance to not lose casting time when you take damage. |
| **Unyielding Faith** | 2/2 | changed | Reduces the duration of Fear and Disorient effects on you by 30%. |
| **Reverence** | 3/3 | **NEW** | Allows 30% of your Mana regeneration to continue while casting. |
| **Purifying Power** | 2/2 | **NEW** | Reduces the mana cost of your Cleanse and Purify spells by 20% and reduces the cooldown of your Exorcism and Holy Wrath spells by 33%. |
| **Infusion of Light** | 1/2 | **NEW** | Your Holy Shock and Flash of Light critical hits reduce the cast time of your next Holy Light cast within 15 sec by 0.5 sec. |
| **Illumination** | 5/5 | changed | After getting a critical effect from your Flash of Light, Holy Light, Light's Vigil, or Holy Shock heal spell you have a 100% chance to gain Mana equal to 50% of the base cost of the spell. |
| **Divine Favor** | 1/1 | moved | When activated, gives your next Flash of Light, Holy Light, or Holy Shock spell a 100% critical effect chance. |
| **Holy Power** | 5/5 | changed | Increases the critical strike chance of your Holy Shock and Holy Strike spells by 15%, and all other spells by 5%. |

### Protection (12)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Toughness** | 1/5 | moved | Increases your armor value from items by 2%. |
| **Redoubt** | 5/5 | changed | Damaging melee attacks against you have a 10% chance to increase your chance to block by 20%. Lasts 10 sec or 5 blocks. |
| **Guardian's Favor** | 1/2 | changed | Reduces the cooldown of your Blessing of Protection by 1 min and increases the duration of your Blessing of Freedom by 3 sec. |
| **Anticipation** | 3/5 | changed | Increases your Defense Skill by 12. |
| **Improved Righteous Fury** | 1/3 | changed | While Righteous Fury is active, all damage taken is reduced by 2%. |
| **Sacred Duty** | 1/2 | **NEW** | Increases your total Stamina by 2% and reduces the cooldown of your Divine Shield, Divine Protection, and Templar's Bulwark spells by 30 sec. |

### Retribution (6)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Benediction** | 5/5 | changed | Reduces the Mana cost of all instant cast spells and abilities by 10%. |
| **Holy Conduit** | 1/2 | **NEW** | Reduces the mana cost of your Consecration, Holy Wrath, Exorcism, and Hammer of Wrath spells by 20%. |

## Rotation

A healer: not in the community simulator, see the healer lab section of the [raid README](../README.md).

## Notes

- +2.0% capacity over the hand draft holy-raid-healer (over the 2% bar: the spec's healing pick; the hand draft stays as the alternative).
- Final race over 400 fresh seeds: capacity 0.586 ± 0.001; holy-raid-healer 0.574, opt-holy-heal-raid-heal 0.574.
- Independent runs agreeing in the last cycle: 2/2; two-move check: 616 one-move and 9,521 two-move builds, none better.
- The healer lab models one healer keeping a five-member group alive (heallab/tables.py); not an in-game measurement.

## Open questions (verify in the live game)

- A machine-searched Holy build: check it against the community's healing builds at launch.

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
