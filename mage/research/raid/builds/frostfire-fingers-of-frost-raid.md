# Frostfire — Fingers of Frost / Ice Lance (user build) — 0/29/22

*[Mage](../../../README.md) · [Raids: training dummy, raid and parse](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 0/29/22 (Arcane / Fire / Frost) |
| **Role** | DPS — Raid |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70753 (2026-11-03 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

A Frostfire Bolt build the user brought on 2026-10-06 (talentsforever.com link): 29 Fire points for Ignite, Heating Up, Pyroblast, Master of Elements, Critical Mass and Fire Power, 22 Frost points for Elemental Precision, Ice Shards, Piercing Ice, Frost Channeling, Shatter, Ice Lance and Fingers of Frost. On 2026-10-06, in the Frostfire rotation in a full raid on the ElliotWood/Forever fork's simulator, it beat that day's open search winner, a 0/34/17, by 2.1% (698 against 684 DPS, 30,000 fights, seed 2), which that search had missed; an Ice Lance line on Fingers of Frost procs adds about 0.9% more.

## Point allocation

### Arcane (0)

*No points.*

### Fire (29)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Accelerant** | 5/5 | changed | Reduces the casting time of your Fireball, Frostfire Bolt, and Arcane Wrath spells by 0.5 sec. |
| **Incineration** | 3/5 | **NEW** | Increases the critical strike chance of your Fire Blast, Ice Lance, Arcane Blast, and Scorch spells by 6%. |
| **Ignite** | 5/5 | unchanged | Your critical strikes from Fire damage spells cause the target to burn for an additional 40% of your spell's damage over 4 sec. |
| **Improved Fire Blast** | 1/2 | **NEW** | Reduces the cooldown of your Fire Blast spell by 1 sec and increases its range by 8 yards. |
| **Pyroblast** | 1/1 | changed | Hurls an immense fiery boulder that causes 101 to 131 Fire damage and an additional 44 Fire damage over 12 sec. |
| **Heating Up** | 1/1 | **NEW** | Non-periodic critical strikes with Fireball, Frostfire Bolt, Fire Blast, and Scorch reduce the cast time of your next Pyroblast cast within 20 sec by 25%, stacking up to 3 times. Fire Blast grants an additional stack every time it deals damage. |
| **Improved Scorch** | 3/3 | changed | Your Scorch spell has a 100% chance to cause your target to be vulnerable to Fire damage. This vulnerability increases all Fire damage you deal to your target by 3% and lasts 30 sec, stacking up to 5 times. |
| **Master of Elements** | 3/3 | changed | Your Fire and Frost critical strikes will refund 30% of their base mana cost. |
| **Critical Mass** | 3/3 | unchanged | Increases the critical strike chance of your Fire spells by 6%. |
| **Fire Power** | 3/3 | unchanged | Increases the damage done by your Fire spells by 3% per your Fire effects on the target, up to a maximum increase of 12%. Effects which mix multiple schools of magic do not qualify. |
| **Burning Soul** | 1/3 | changed | Gives your Fire spells a 23% chance to not lose casting time when you take damage and reduces the threat caused by your Fire spells by 10%. |

### Frost (22)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Frost Warding** | 2/2 | changed | Increases the Armor and resistances granted by your Frost Armor and Ice Armor spells by 30%, gives your Frost Ward a 20% chance to negate the warded damage spell, and increases the amount absorbed by your Ice Barrier and Frost Ward by 20%. |
| **Improved Frostbolt** | 1/5 | changed | Reduces the casting time of your Frostbolt spell by 0.1 sec. |
| **Precision** | 3/3 | changed | Improves your chance to hit with all spells by 6%. |
| **Ice Shards** | 5/5 | unchanged | Increases the critical strike damage bonus of your Frost spells by 100%. |
| **Frost Channeling** | 3/3 | moved | Reduces the mana cost of your Frost spells by 15% and reduces the threat caused by your Frost spells by 30%. |
| **Ice Lance** | 1/1 | **NEW** | Deals 28 to 32 Frost damage to an enemy target. Deals 300% increased damage to Frozen targets. |
| **Arctic Reach** | 1/2 | unchanged | Increases the range of your Frostbolt, Ice Lance, and Blizzard spells and the radius of your Frost Nova and Cone of Cold spells by 10%. |
| **Ice Block** | 1/1 | moved | You become encased in a block of ice, protecting you from all physical attacks and spells for 10 sec, but during that time you cannot attack, move, or cast spells. |
| **Shatter** | 3/3 | changed | Increases the critical strike chance of all your spells against Frozen targets by 50%. |
| **Fingers of Frost** | 2/2 | **NEW** | Gives your Chill effects a 15% chance to grant you the Fingers of Frost effect, which treats your next 2 spells cast as if the target were Frozen. Lasts 15 sec. |

## Core talents (priority order)

1. **Fingers of Frost** — Frostfire Bolt chills, so its procs let Ice Lance and Shatter crit; the 22 Frost points exist for this.
2. **Shatter** — Crit against frozen targets for Frostfire Bolt, Ice Lance and the Fire spells alike.
3. **Ignite** — The Fire half: crits burn for 40% more.
4. **Heating Up** — Instant Pyroblasts off crit streaks.
5. **Master of Elements** — Mana back from crits; the build has no Arcane mana talents.

## Rank among our builds and the community simulator's

**1 of 5** for `frostfire-raid` by training-dummy DPS in the community simulator (wowsims/forever 2e6e77d (client 70938)); full ranking and the other builds' rotations: [raid README](../README.md), [raid rotations](../rotation.md).

| Rank | Build | By | Split | Dummy DPS | vs best | Raid DPS | vs best in a raid | Out of mana on the dummy |
|---|---|---|---|---|---|---|---|---|
| 1 | **[`frostfire-fingers-of-frost-raid`](frostfire-fingers-of-frost-raid.md)** | ours: hand draft | 0/29/22 | 532 | +0.0% | 768 | -1.8% | 38 s |
| 2 | [`frostfire-ml-raid`](frostfire-ml-raid.md) | ours: derived (ML search) | 0/29/22 | 527 | -0.9% | 778 | -0.4% | 42 s |
| 3 | [`frostfire-raid`](frostfire-raid.md) | ours: hand draft | 7/31/13 | 505 | -5.1% | 704 | -9.9% | 35 s |
| 4 | [`frostfire-ffb-raid`](frostfire-ffb-raid.md) | ours: derived (simulator preset) | 0/29/22 | 501 | -5.9% | 781 | +0.0% | 50 s |
| 5 | *FFB* | community simulator | - | 501 | -5.9% | 781 | +0.0% | 50 s |

## Rotation (community simulator, training dummy)

- **The training dummy:** the entry's base rotation (`_reference/data/raidsim/apls/mage/upstream/ffb.apl.json`), untuned. The rotation search of 2026-09-28 to 2026-10-24 (18 changes, `frostfire-raid-rotation-search.json`) tuned an earlier base that this entry no longer plays.
- **A fully buffed raid:** the entry's base rotation (`_reference/data/raidsim/apls/mage/upstream/ffb.apl.json`), untuned. The rotation search of 2026-09-28 to 2026-10-31 (37 changes, `frostfire-raid-rotation-search.json`) tuned an earlier base that this entry no longer plays.

Before the pull: cast Pyroblast.

| # | Priority (the first line whose condition holds is cast) | [`frostfire-fingers-of-frost-raid`](frostfire-fingers-of-frost-raid.md) casts/min |
|---|---|---|
| 1 | if mana < current cost and (not Read Leyline is known or not Read Leyline is ready or Energized is up): channel Evocation (stop it when mana % ≥ 99%) | as ready |
| 2 | if (stacks of Fire Vulnerability on the target < 5 or time left on Fire Vulnerability < 5) and (stacks of Fire Vulnerability on the target < 4 or not Scorch is being cast): cast Scorch | 4.3 |
| 3 | if stacks of Fire Vulnerability on the target = 5: use every other cooldown when ready | as ready |
| 4 | if stacks of Heating Up on you = 3 and not Pyroblast is being cast: cast Pyroblast | 2.9 |
| 5 | if stacks of Fingers of Frost on you < 2: cast Fire Blast | 4.8 |
| 6 | cast Frostfire Bolt | 11.3 |

Lines of the simulator's rotation these builds never cast: strict sequence: cast Read Leyline; channel Evocation (stop it when mana % ≥ 99%) (its condition never held in these fights).

Damage by ability:

| Ability | [`frostfire-fingers-of-frost-raid`](frostfire-fingers-of-frost-raid.md) |
|---|---|
| Frostfire Bolt | 44% |
| Pyroblast | 21% |
| Fire Blast | 15% |
| Ignite | 12% |
| Scorch | 8% |
| Demonic Rune | 1% |

## Notes

- Added 2026-10-06 from the user's link; the open talent search of the same day found 0/34/17 at 684 DPS in the Frostfire rotation and missed this build (698): recorded in raidsim/known-positives.json so later searches start from it.
- Alone on a training dummy (own buffs only) it is 2% behind the 0/34/17 build; in a full raid 2% ahead. Simulator numbers are the community's model of the beta (ElliotWood/Forever b0f0df3 with this project's patches), not in-game measurements.
- 2026-10-15: the 70291 machine-learning search (ElliotWood/Forever 2ce8265 with this project's patches, ml_pipeline.py --fresh) confirms this build for Hybrid Fire/Frost: its full-raid winner is +0.07% against it, under the 0.5% bar for a new build.
- 2026-10-16 (repair_builds.py, client build 70425 trees): 0/29/22 -> 0/29/22; Fire Power 4 -> 3 (rank cap); refill +1 Improved Fire Blast (refill: the fire-raid model, raid-dps).
- 2026-10-22 (repair_builds.py, client build 70425 trees): 0/29/22 -> 0/29/22; Elemental Precision 5 -> 3 (rank cap); Piercing Ice 3 gone; +1 Frost Warding (tier gating for Ice Shards); +1 Frost Warding (tier gating for Ice Shards); +1 Improved Frostbolt (tier gating for Shatter); +1 Ice Block (tier gating for Fingers of Frost); +1 Arctic Reach (tier gating for Fingers of Frost) (refill: the fire-raid model, raid-dps).
- 2026-10-30 (repair_builds.py, client build 1.60.1.70707 trees): 0/29/22 -> 0/29/22; Improved Fireball -> Accelerant (renamed); Elemental Precision -> Precision (renamed) (refill: the fire-raid model, raid-dps).
- 2026-11-20: filler points moved (1 point from Flame Throwing to Burning Soul): the same DPS bit for bit in a full raid and on the training dummy. The new talents follow the utility order (interrupt protection, threat, mana, range, survival; dodge, parry and block count for nothing in a damage dealer's raid), which the simulator cannot measure (deep-runs/credited_fillers_1120.py; the user's rule of 2026-11-08 that a page pick holds no talent that does nothing).

## Open questions (verify in the live game)

- Does Frostfire Bolt's chill proc Fingers of Frost in the live game as the simulator assumes?

## Sources

- <https://talentsforever.com/mage/60/-0355100013013304-00550003310003002-TUV4WaVbdeflmqrswzh-6>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
