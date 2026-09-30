# Optimizer — Starfire 55%, Wrath 20%, Moonfire 20% (8% direct, 12% DoT), Insect Swarm arrives as a talent effect (raid-dps) — 33/5/13

*[Druid](../../../README.md) · [Raids: training dummy, raid and parse](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 33/5/13 (Balance / Feral Combat / Restoration) |
| **Role** | DPS — Raid |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70009 (2026-09-25 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

Produced by the stats model (`_reference/data/scorer/`) for spec model `balance-dps` and profile `raid-dps`: score +128.1% (DPS gain vs. no talents). Every number behind it is in the effect files (tooltip-parsed or hand-entered with its arithmetic); change those, not this build.

## Point allocation

### Balance (33)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Genesis** | 5/5 | **NEW** | Increases the periodic damage and healing done by your spells and abilities by 5%. |
| **Nature's Reach** | 2/2 | changed | Increases the range of your offensive Balance spells by 20% and improves your chance to hit by 4%. |
| **Improved Moonfire** | 2/2 | changed | Increases the damage and critical strike chance of your Moonfire spell by 10%. |
| **Nature's Majesty** | 2/2 | **NEW** | Increases your critical strike chance with spells and melee attacks by 4%. |
| **Moonglow** | 3/3 | changed | Reduces the Mana cost of your damaging spells by 25%. |
| **Nature's Splendor** | 1/1 | **NEW** | Increases the duration of your Moonfire and Rejuvenation spells by 3 sec, your Regrowth spell by 6 sec, and your Insect Swarm spell by 2 sec. |
| **Insect Swarm** | 1/1 | changed | The enemy target is swarmed by insects, decreasing their chance to hit with attacks by 2% and causing 48 Nature damage over 12 sec. |
| **Vengeance** | 5/5 | changed | Increases the critical strike damage bonus of your Arcane and Nature spells by 100%. |
| **Improved Starfire** | 5/5 | changed | Reduces the cast time of Starfire by 0.5 sec and Starfire has a 15% chance to stun its target for 3 sec. |
| **Nature's Grace** | 1/1 | changed | All non-periodic spell criticals grace you with a blessing of nature, increasing your spellcasting speed and reducing your global cooldown by 10% for 3 sec. |
| **Moonfury** | 5/5 | changed | Increases the damage done by your Arcane and Nature spells by 10%. |
| **Moonkin Form** | 1/1 | changed | Transforms the Druid into Moonkin Form. While in this form, the armor contribution from items is increased by 360%, Omen of Clarity gains 100% increased chance to trigger, and all party members within 45 yards have their critical strike chance increased by 3%, exclusive with Leader of the Pack. The Moonkin cannot cast healing spells while shapeshifted.  The act of shapeshifting frees the caster of Polymorph and Movement Impairing effects. |

### Feral Combat (5)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Heart of the Wild** | 5/5 | changed | Increases your Intellect by 10%. In addition, while in Bear Form or Dire Bear Form your Stamina is increased by 20% and while in Cat Form your Strength is increased by 10%. |

### Restoration (13)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Nature's Focus** | 5/5 | changed | Gives you a 70% chance to avoid interruption caused by damage while casting Arcane and Nature spells. |
| **Naturalist** | 5/5 | **NEW** | Reduces the cast time of your Healing Touch spell by 0.5 sec and increases all damage you deal by 5%. |
| **Reflection** | 3/3 | changed | Allows 50% of your Mana regeneration to continue while casting. |

## Core talents (priority order)

1. **Moonglow** — Removing it costs 49.8 points of score in this model.
2. **Vengeance** — Removing it costs 23.9 points of score in this model.
3. **Moonfury** — Removing it costs 20.7 points of score in this model.
4. **Insect Swarm** — Removing it costs 20.5 points of score in this model.
5. **Reflection** — Removing it costs 19.8 points of score in this model.
6. **Moonkin Form** — Removing it costs 16.8 points of score in this model.
7. **Naturalist** — Removing it costs 10.9 points of score in this model.
8. **Nature's Reach** — Removing it costs 10.6 points of score in this model.

## Rank among our builds and the community simulator's

**2 of 4** for `balance-dps` by training-dummy DPS in the community simulator (ElliotWood/Forever 40be98e); full ranking and the other builds' rotations: [raid README](../README.md), [raid rotations](../rotation.md).

| Rank | Build | By | Split | Dummy DPS | vs best | Raid DPS | vs best in a raid | Out of mana on the dummy |
|---|---|---|---|---|---|---|---|---|
| 1 | [`balance-moonkin-raid`](balance-moonkin-raid.md) | ours: hand draft | 33/5/13 | 438 | +0.0% | 511 | +0.0% | 4 s |
| 2 | **[`opt-balance-dps-raid-dps`](opt-balance-dps-raid-dps.md)** | ours: optimizer | 33/5/13 | 438 | +0.0% | 511 | +0.0% | 4 s |
| 3 | *Balance* | community simulator | - | 400 | -8.7% | 457 | -10.6% | 2 s |
| 4 | *Moonkin 38/0/13* | community simulator | - | 353 | -19.4% | 506 | -1.0% | 31 s |

## Rotation (community simulator, training dummy)

- **The training dummy:** our tuned rotation (`raidsim/apl_opt.py`, 2026-09-28, 3 passes, the last 2026-09-29, 5 changes to the base rotation; third-seed check: opt-balance-dps-raid-dps 458 -> 462 DPS (+1.0%), sim preset: Balance 411 -> 411 DPS (-0.1%)):
  1. move down below 'keep Insect Swarm on up to 1 targets (refresh under 0ms)': keep Moonfire on up to 1 targets (refresh under 0ms) (+1.8%, pass 1)
  2. rank 3 below 15% mana, above: cast Starfire (+0.7%, pass 1)
  3. always rank 1 instead of rank 3: if mana % < 15%: cast Starfire (+0.5%, pass 1)
  4. move down below 'cast Starfire': if mana % < 15%: cast Starfire (+0.3%, pass 1)
  5. only with 10s or more of the fight left: keep Insect Swarm on up to 1 targets (refresh under 0ms) (+0.2%, pass 2)
- **A fully buffed raid:** the simulator's own rotation: no single change (and no pair of changes) beat it on two seeds (`raidsim/apl_opt.py`, 2026-09-29).

Before the pull: at -10s: activate Moonkin Form.

| # | Priority (the first line whose condition holds is cast) | [`opt-balance-dps-raid-dps`](opt-balance-dps-raid-dps.md) casts/min |
|---|---|---|
| 1 | use every other cooldown when ready | as ready |
| 2 | if mana % ≤ 30%: cast Innervate | 0.3 |
| 3 | if time left in the fight ≥ 10s: keep Insect Swarm on up to 1 targets (refresh under 0ms) | 4.3 |
| 4 | keep Moonfire on up to 1 targets (refresh under 0ms) | 3.9 |
| 5 | cast Starfire | 14.0 |
| 6 | if mana % < 15%: cast Starfire | 1.8 |

Damage by ability:

| Ability | [`opt-balance-dps-raid-dps`](opt-balance-dps-raid-dps.md) |
|---|---|
| Starfire | 63% |
| Moonfire | 19% |
| Insect Swarm | 18% |

## Notes

- Report: druid/research/talents/forever/optimizer/balance-dps-raid-dps.md

## Open questions (verify in the live game)

- Hand-entered effect values (see the manual effect file) are the weakest inputs — verify the ones this build leans on.

## Sources

- <https://warcraftforever.games/talents/druid>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
