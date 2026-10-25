# Optimizer — Single-target Fireball leveling: Fireball ~60%, Fire Blast, Scorch (22+), wand (leveling-st) — 2/33/16

*[Mage](../../../README.md) · [Leveling and solo play](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 2/33/16 (Arcane / Fire / Frost) |
| **Role** | DPS — Leveling |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70425 (2026-10-16 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

Produced by the stats model (`_reference/data/scorer/`) for spec model `fire-leveling` and profile `leveling-st`: score +68.9% (time-per-kill saved vs. no talents). Every number behind it is in the effect files (tooltip-parsed or hand-entered with its arithmetic); change those, not this build.

## Point allocation

### Arcane (2)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Missile Barrage** | 2/2 | **NEW** | Gives your Arcane Blast spell a 40% chance, your Arcane Missile hits a 10% chance, and your Arcane Wrath, Fireball, Frostbolt, and Frostfire Bolt spells a 20% chance to reduce the channeled duration of your next Arcane Missiles spell by 50%, reduce the Mana cost by 100%, and missiles fire every 0.5 sec. |

### Fire (33)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Improved Fire Blast** | 2/2 | **NEW** | Reduces the cooldown of your Fire Blast spell by 2 sec and increases its range by 15 yards. |
| **Improved Fireball** | 3/5 | changed | Reduces the casting time of your Fireball and Frostfire Bolt spells by 0.3 sec. |
| **Ignite** | 5/5 | unchanged | Your critical strikes from Fire damage spells cause the target to burn for an additional 40% of your spell's damage over 4 sec. |
| **Impact** | 3/3 | changed | Gives your Fire spells a 10% chance to stun the target for 2 sec. |
| **Flame Throwing** | 2/2 | unchanged | Increases the range of your Fire spells by 6 yards. |
| **Burning Soul** | 3/3 | changed | Gives your Fire spells a 70% chance to not lose casting time when you take damage and reduces the threat caused by your Fire spells by 30%. |
| **Pyroblast** | 1/1 | changed | Hurls an immense fiery boulder that causes 101 to 131 Fire damage and an additional 44 Fire damage over 12 sec. |
| **Heating Up** | 1/1 | **NEW** | Non-periodic critical strikes with Fireball, Frostfire Bolt, Fire Blast, and Scorch reduce the cast time of your next Pyroblast cast within 20 sec by 25%, stacking up to 3 times. Fire Blast grants an additional stack every time it deals damage. |
| **Improved Scorch** | 3/3 | changed | Your Scorch spell has a 100% chance to cause your target to be vulnerable to Fire damage. This vulnerability increases all Fire damage you deal to your target by 3% and lasts 30 sec, stacking up to 5 times. |
| **Critical Mass** | 5/5 | unchanged | Increases the critical strike chance of your Fire spells by 10%. |
| **Blast Wave** | 1/1 | changed | A wave of flame radiates outward from the caster, damaging all enemies caught within the blast for 154 to 184 Fire damage, and Dazing them for 50% reduced movement speed for 6 sec. |
| **Fire Power** | 3/3 | unchanged | Increases the damage done by your Fire spells by 3% per your Fire effects on the target, up to a maximum increase of 12%. Effects which mix multiple schools of magic do not qualify. |
| **Combustion** | 1/1 | changed | When activated, this spell causes each of your Fire damage spell hits to increase your critical strike chance with Fire damage spells by 10%. This effect lasts until you have caused 3 non-periodic critical strikes with Fire spells. |

### Frost (16)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Elemental Precision** | 3/3 | changed | Improves your chance to hit with Frost and Fire spells by 6%. |
| **Frost Warding** | 2/2 | changed | Increases the Armor and resistance given by your Frost Armor and Ice Armor spells by 30%. In addition, gives your Frost Ward a 20% chance to reflect Frost spells and effects while active. |
| **Permafrost** | 3/3 | changed | Increases the duration of your Chill effects by 33% and reduces the target's speed by an additional 10%. |
| **Frostbite** | 3/3 | moved | Gives your Chill effects a 15% chance to Freeze the target for 5 sec. |
| **Ice Lance** | 1/1 | **NEW** | Deals 28 to 32 Frost damage to an enemy target. Deals 200% increased damage to Frozen targets. |
| **Frost Channeling** | 3/3 | moved | Reduces the mana cost of your Frost spells by 15% and reduces the threat caused by your Frost spells by 30%. |
| **Ice Block** | 1/1 | moved | You become encased in a block of ice, protecting you from all physical attacks and spells for 10 sec, but during that time you cannot attack, move, or cast spells. |

## Leveling order

| Levels | Tree | Talent | Pts | Running total |
|---|---|---|---|---|
| 10-11 | Fire | Improved Fire Blast | 2 | 0/2/0 |
| 12-14 | Fire | Improved Fireball | 3 | 0/5/0 |
| 15-18 | Fire | Ignite | 4 | 0/9/0 |
| 19-21 | Frost | Elemental Precision | 3 | 0/9/3 |
| 22-23 | Frost | Frost Warding | 2 | 0/9/5 |
| 24-26 | Frost | Permafrost | 3 | 0/9/8 |
| 27-28 | Frost | Frostbite | 2 | 0/9/10 |
| 29 | Frost | Ice Lance | 1 | 0/9/11 |
| 30 | Fire | Ignite | 1 | 0/10/11 |
| 31-33 | Fire | Burning Soul | 3 | 0/13/11 |
| 34 | Fire | Impact | 1 | 0/14/11 |
| 35 | Fire | Pyroblast | 1 | 0/15/11 |
| 36 | Fire | Heating Up | 1 | 0/16/11 |
| 37 | Arcane | Missile Barrage | 1 | 1/16/11 |
| 38-39 | Fire | Impact | 2 | 1/18/11 |
| 40-41 | Fire | Flame Throwing | 2 | 1/20/11 |
| 42 | Fire | Blast Wave | 1 | 1/21/11 |
| 43-44 | Fire | Critical Mass | 2 | 1/23/11 |
| 45-46 | Fire | Improved Scorch | 2 | 1/25/11 |
| 47-48 | Fire | Fire Power | 2 | 1/27/11 |
| 49-51 | Fire | Critical Mass | 3 | 1/30/11 |
| 52 | Fire | Combustion | 1 | 1/31/11 |
| 53 | Fire | Fire Power | 1 | 1/32/11 |
| 54 | Arcane | Missile Barrage | 1 | 2/32/11 |
| 55 | Frost | Frostbite | 1 | 2/32/12 |
| 56-58 | Frost | Frost Channeling | 3 | 2/32/15 |
| 59 | Frost | Ice Block | 1 | 2/32/16 |
| 60 | Fire | Improved Scorch | 1 | 2/33/16 |

## Core talents (priority order)

1. **Ice Lance** — Removing it costs 20.9 points of score in this model.
2. **Ignite** — Removing it costs 5.1 points of score in this model.
3. **Pyroblast** — Removing it costs 2.6 points of score in this model.
4. **Heating Up** — Removing it costs 2.5 points of score in this model.
5. **Improved Fire Blast** — Removing it costs 2.3 points of score in this model.
6. **Combustion** — Removing it costs 2.1 points of score in this model.
7. **Fire Power** — Removing it costs 1.8 points of score in this model.
8. **Elemental Precision** — Removing it costs 1.4 points of score in this model.

## Leveling rotation (fight lab)

Single-target leveling fights against normal mobs of your level: pull at max range, the mob walks in at 7 yd/s (slowed by chills), swings every 2 s once in melee (pushing casts back), Frost Nova when it arrives, a 2-second step back, Ice Lance/Frostbolt into the freeze, Fire Blast and wand to finish without overkill. Between fights: 2 s loot, 6 s travel, Evocation when low, conjured water below 35% mana, food below 65% health; a death costs 90 s. Every hit, miss, crit, partial resist, chill, freeze, proc and pushback is rolled.

**Tuned rules** (`fightlab/rotation_opt.py`, 2026-10-22, on top of the priority below): Fireball only while the mob has more than 35% health; Scorch only while the mob has more than 35% health. Together +2.3% time per kill saved for `opt-fire-leveling-leveling-st` (level-weighted, a third seed of 3000 fights per level).

What this build casts per kill ([report](../fightlab/fire-leveling.md), all leveling builds: [leveling rotations](../rotation.md)):

| Ability | L20 casts/kill | L30 casts/kill | L40 casts/kill | L50 casts/kill | L60 casts/kill | Damage at L60 |
|---|---|---|---|---|---|---|
| Ice Lance | 0.0 | 2.8 | 3.1 | 2.5 | 2.2 | 24% |
| Fire Blast | 2.0 | 2.3 | 2.6 | 2.1 | 1.9 | 27% |
| Fireball | 3.1 | 1.1 | 1.2 | 1.4 | 1.4 | 21% |
| Frost Nova | 0.8 | 0.9 | 0.9 | 0.8 | 0.7 | 1% |
| Pyroblast | 0.0 | 0.0 | 0.7 | 0.6 | 0.6 | 12% |
| Wand | 1.8 | 1.0 | 1.6 | 0.8 | 0.6 | 1% |
| Blast Wave | 0.0 | 0.0 | 0.0 | 0.3 | 0.3 | 4% |
| Scorch | 0.0 | 1.0 | 0.7 | 0.2 | 0.1 | 1% |
| Counterspell | 0.0 | 0.2 | 0.1 | 0.1 | 0.1 | 0% |

## Notes

- Report: mage/research/talents/forever/optimizer/fire-leveling-leveling-st.md

## Open questions (verify in the live game)

- Hand-entered effect values (see the manual effect file) are the weakest inputs — verify the ones this build leans on.

## Sources

- <https://warcraftforever.games/talents/mage>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
