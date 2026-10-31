# Holy — Raid healing (machine-learning search) — 30/16/5

*[Paladin](../../../README.md) · [Raids: training dummy, raid and parse](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 30/16/5 (Holy / Protection / Retribution) |
| **Role** | HEALER — Raid |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70707 (2026-10-30 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

The Holy build the machine-learning talent search found in the healer lab on 2026-10-21 (heallab/deep_heal.py: a random forest guiding a genetic search over every legal build of the spec, the heal-choice policy tuned with it, races on fresh seeds, every build one or two moves from the winner checked). Capacity is the healer lab's model of stated assumptions.

## Point allocation

### Holy (30)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Divine Strength** | 5/5 | unchanged | Increases your Strength by 10%. |
| **Spiritual Focus** | 5/5 | changed | Gives your Flash of Light, Holy Light, and Light's Vigil spells a 70% chance to not lose casting time when you take damage. |
| **Healing Light** | 3/3 | changed | Increases the amount healed by your Holy Light, Flash of Light, and Holy Shock spells by 12%. |
| **Purifying Power** | 2/2 | **NEW** | Reduces the mana cost of your Cleanse and Purify spells by 20% and reduces the cooldown of your Exorcism and Holy Wrath spells by 33%. |
| **Reverence** | 2/2 | **NEW** | Allows 30% of your Mana regeneration to continue while casting. |
| **Divine Favor** | 1/1 | moved | When activated, gives your next Flash of Light, Holy Light, or Holy Shock spell a 100% critical effect chance. |
| **Illumination** | 5/5 | changed | After getting a critical effect from your Flash of Light, Holy Light, Light's Vigil, or Holy Shock heal spell you have a 100% chance to gain Mana equal to 50% of the base cost of the spell. |
| **Infusion of Light** | 2/2 | **NEW** | Your Holy Shock and Flash of Light critical hits reduce the cast time of your next Holy Light cast within 15 sec by 1.0 sec. |
| **Holy Power** | 5/5 | changed | Increases the critical strike healing bonus of your Holy spells by 50%. |

### Protection (16)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Divine Intellect** | 5/5 | unchanged | Increases your total Intellect by 10%. |
| **Redoubt** | 5/5 | changed | Damaging melee attacks against you have a 10% chance to increase your chance to block by 30%. Lasts 10 sec or 5 blocks. |
| **Guardian's Favor** | 2/2 | changed | Reduces the cooldown of your Blessing of Protection by 2 min and increases the duration of your Blessing of Freedom by 6 sec. |
| **Sacred Duty** | 1/2 | **NEW** | Reduces the cooldown of your Divine Shield, Divine Protection, and Templar's Bulwark spells by 30 sec, and reduces the duration of Forbearance by 5 sec. |
| **Templar's Bulwark** | 1/1 | **NEW** | When activated, this ability grants you an absorb shield equal to 100% of your maximum health for 8 sec. Applies Forbearance for 1 min. Cannot be cast while Forbearance is active. |
| **Toughness** | 1/5 | moved | Increases your armor value from items by 2%. |
| **Improved Righteous Fury** | 1/3 | changed | While Righteous Fury is active, all damage taken is reduced by 3%. |

### Retribution (5)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Benediction** | 5/5 | changed | Reduces the Mana cost of all instant cast spells and abilities by 10%. |

## Rotation

A healer: not in the community simulator, see the healer lab section of the [raid README](../README.md).

## Notes

- +2.0% capacity over the hand draft holy-raid-healer (over the 2% bar: the spec's healing pick; the hand draft stays as the alternative).
- Final race over 400 fresh seeds: capacity 0.586 ± 0.001; holy-raid-healer 0.574, opt-holy-heal-raid-heal 0.574.
- Independent runs agreeing in the last cycle: 2/2; two-move check: 616 one-move and 9,521 two-move builds, none better.
- The healer lab models one healer keeping a five-member group alive (heallab/tables.py); not an in-game measurement.
- 2026-10-31 (repair_builds.py, client build 1.60.1.70707 trees): 33/12/6 -> 30/16/5; Divine Intellect 5 gone (moved to Protection); Unyielding Faith 2 gone (moved to Retribution); Reverence 3 -> 2 (rank cap); Holy Conduit 1 gone (moved to Holy); +1 Divine Intellect (tier gating for Toughness); +1 Divine Intellect (tier gating for Toughness); +1 Divine Intellect (tier gating for Toughness); +1 Divine Intellect (tier gating for Anticipation); +1 Divine Intellect (tier gating for Anticipation); +1 Guardian's Favor (tier gating for Anticipation); +1 Templar's Bulwark (tier gating for Anticipation); +1 Infusion of Light (tier gating for Holy Power); +1 Spiritual Focus (tier gating for Holy Power); +1 Spiritual Focus (tier gating for Holy Power); +1 Spiritual Focus (tier gating for Holy Power); +1 Spiritual Focus (tier gating for Holy Power); -1 Anticipation (over 51); -1 Anticipation (over 51); -1 Anticipation (over 51) (refill: the holy-heal model, raid-heal).

## Open questions (verify in the live game)

- A machine-searched Holy build: check it against the community's healing builds at launch.

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
