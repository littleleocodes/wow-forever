# Restoration — Raid healing (machine-learning search) — 12/1/38

*[Druid](../../../README.md) · [Raids: training dummy, raid and parse](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 12/1/38 (Balance / Feral Combat / Restoration) |
| **Role** | HEALER — Raid |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70707 (2026-10-31 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

The Restoration build the machine-learning talent search found in the healer lab on 2026-11-02 (heallab/deep_heal.py: a random forest guiding a genetic search over every legal build of the spec, the heal-choice policy tuned with it, races on fresh seeds, every build one or two moves from the winner checked). Capacity is the healer lab's model of stated assumptions.

## Point allocation

### Balance (12)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Improved Wrath** | 2/5 | changed | Reduces the cast time of your Wrath spell by 0.2 sec and its Mana cost by 20%. |
| **Genesis** | 5/5 | **NEW** | Increases the periodic damage and healing done by your spells and abilities by 10%. |
| **Improved Moonfire** | 2/2 | changed | Increases the damage and critical strike chance of your Moonfire spell by 10%. |
| **Nature's Majesty** | 2/2 | **NEW** | Increases your critical strike chance with spells and melee attacks by 4%. |
| **Nature's Splendor** | 1/1 | **NEW** | Increases the duration of your Moonfire and Rejuvenation spells by 3 sec, your Regrowth spell by 6 sec, and your Insect Swarm spell by 2 sec. |

### Feral Combat (1)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Furor** | 1/5 | changed | Gives you a 20% chance to gain 10 Rage when shapeshifting into Bear Form or Dire Bear Form. Shapeshifting into Cat Form restores 20% of the Energy you had when last in Cat Form, plus 2 Energy per second spent outside Bear Form or Dire Bear Form, up to 20 Energy. |

### Restoration (38)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Nature's Focus** | 1/5 | changed | Gives your Arcane and Nature spells a 14% chance to not lose casting time when you take damage. |
| **Heart of the Wild** | 5/5 | changed | Increases your Intellect by 10%. In addition, while in Bear Form or Dire Bear Form your Stamina is increased by 20% and while in Cat Form your Strength is increased by 10%. |
| **Naturalist** | 5/5 | **NEW** | Reduces the cast time of your Healing Touch and Wild Growth spells by 0.5 sec and increases all damage you deal by 10%. |
| **Reflection** | 3/3 | changed | Allows 50% of your Mana regeneration to continue while casting. |
| **Natural Shapeshifter** | 1/3 | moved | Reduces the mana cost of all shapeshifting by 10%. |
| **Gift of Nature** | 5/5 | changed | Increases the effect of all your healing spells by 10%. |
| **Tranquil Spirit** | 5/5 | unchanged | Reduces the mana cost of your Healing Touch and Tranquility spells by 10%. |
| **Improved Rejuvenation** | 3/3 | moved | Increases the effect of your Rejuvenation spell by 15%. |
| **Swiftmend** | 1/1 | changed | Instantly heals a target with your active Rejuvenation or Regrowth effect for an amount equal to the full duration of the periodic effect of the consumed spell. |
| **Nature's Swiftness** | 1/1 | unchanged | When activated, your next Nature spell becomes an instant cast spell. |
| **Living Spirit** | 3/3 | **NEW** | Increases your Spirit by 15%. |
| **Improved Regrowth** | 5/5 | unchanged | Increases the critical effect chance of your Regrowth spell by 50%. |

## Rotation

A healer: not in the community simulator, see the healer lab section of the [raid README](../README.md).

## Notes

- +3.6% capacity over the hand draft resto-raid-healer (over the 2% bar: the spec's healing pick; the hand draft stays as the alternative).
- Final race over 400 fresh seeds: capacity 0.662 ± 0.002; resto-raid-healer 0.639, opt-resto-heal-raid-heal 0.639, resto-regrowth-natures-grace 0.604.
- Independent runs agreeing in the last cycle: 2/2; two-move check: 349 one-move and 4,512 two-move builds, none better.
- The healer lab models one healer keeping a five-member group alive (heallab/tables.py); not an in-game measurement.

## Open questions (verify in the live game)

- A machine-searched Restoration build: check it against the community's healing builds at launch.

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
