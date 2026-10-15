# Balance — Moonkin / Nature's Grace (simulator winner adopted 2026-09-26) — 33/5/13

*[Druid](../../../README.md) · [Raids: training dummy, raid and parse](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 33/5/13 (Balance / Feral Combat / Restoration) |
| **Role** | DPS — Raid |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70291 (2026-10-08 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |
| **Based on** | Classic baseline `balance-moonkin-raid` |

## Summary

Allocation adopted on 2026-09-26 from `opt-balance-dps-raid-dps`, the best build in the community simulator (+6.3% DPS vs the previous draft with the simulator's gear, rotation and buffs; the previous draft is kept under raid/raidsim/candidates/). Core talents are ranked by the simulator's removal cost. Previous summary: Balance finally has enough good talents to go deep: Genesis, Moonglow, Nature's Majesty (crit), Nature's Reach (hit), Nature's Splendor, Balance of Nature (alternate Arcane/Nature for +5%), Insect Swarm, Vengeance, Improved Starfire, Nature's Grace, Eclipse (Wrath makes Starfire faster), Moonfury and Moonkin Form (now a 45-yard aura). Restoration only for Nature's Focus.

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
| **Moonkin Form** | 1/1 | changed | Shapeshift into Moonkin Form, increasing Omen of Clarity's chance to trigger by 100%, Armor contribution from items by 360%, and all party members within 45 yards have their Critical Strike chance increased by 3%, exclusive with Leader of the Pack. Also protects the caster from Polymorph effects and prevents the use of healing spells.  The act of shapeshifting frees the caster of Polymorph and Movement Impairing effects. |

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

1. **Improved Starfire** — -0.5s Starfire (est.) and stun procs. Raid sim (2026-09-26): removing it costs +11% DPS.
2. **Vengeance** — +100% crit damage on Arcane/Nature (est.). Raid sim (2026-09-26): removing it costs +11% DPS.
3. **Moonfury** — Arcane/Nature damage (demo rank 1 = 1%; Classic was 2%/rank — verify). Raid sim (2026-09-26): removing it costs +10% DPS.
4. **Insect Swarm** — DoT and -2% hit on the target. Raid sim (2026-09-26): removing it costs +8% DPS.
5. **Naturalist** — Raid sim (2026-09-26): removing it costs +5% DPS.
6. **Nature's Reach** — +4% spell hit (est.). Raid sim (2026-09-26): removing it costs +4% DPS.
7. **Nature's Majesty** — +4% crit (est.). Raid sim (2026-09-26): removing it costs +4% DPS.
8. **Improved Moonfire** — Raid sim (2026-09-26): removing it costs +3% DPS.

## Flex points

| Pts | Default | Alternatives | Why |
|---|---|---|---|
| 3 | Moonglow | any utility talent legal at that tier | Measures +0.8% DPS in the community simulator (noise): these points are free to move. |
| 1 | Moonkin Form | any utility talent legal at that tier | Measures +0.4% DPS in the community simulator (noise): these points are free to move. |
| 2 | Heart of the Wild | any utility talent legal at that tier | Measures +0.2% DPS in the community simulator (noise): these points are free to move. |
| 5 | Nature's Focus | any utility talent legal at that tier | Measures +0.0% DPS in the community simulator (noise): these points are free to move. |
| 2 | Heart of the Wild | Subtlety, any utility talent legal at that tier | Measures +0.0% DPS in the community simulator (noise): these points are free to move. |

## Rank among our builds and the community simulator's

**1 of 4** for `balance-dps` by training-dummy DPS in the community simulator (ElliotWood/Forever 2ce8265); full ranking and the other builds' rotations: [raid README](../README.md), [raid rotations](../rotation.md).

| Rank | Build | By | Split | Dummy DPS | vs best | Raid DPS | vs best in a raid | Out of mana on the dummy |
|---|---|---|---|---|---|---|---|---|
| 1 | **[`balance-moonkin-raid`](balance-moonkin-raid.md)** | ours: hand draft | 33/5/13 | 508 | +0.0% | 586 | +0.0% | 4 s |
| 2 | [`opt-balance-dps-raid-dps`](opt-balance-dps-raid-dps.md) | ours: optimizer | 33/5/13 | 508 | +0.0% | 586 | +0.0% | 4 s |
| 3 | *Balance* | community simulator | - | 464 | -8.6% | 521 | -11.2% | 0 s |
| 4 | *Moonkin 38/0/13* | community simulator | - | 406 | -20.1% | 579 | -1.2% | 37 s |

## Rotation (community simulator, training dummy)

- **The training dummy:** our tuned rotation (`raidsim/apl_opt.py`, 2026-09-28, 5 passes, the last 2026-10-01, 6 changes to the base rotation; third-seed check: ml: Balance 516 -> 535 DPS (+3.8%), sim preset: Balance 475 -> 485 DPS (+2.1%)):
  1. move down below 'keep Insect Swarm on up to 1 targets (refresh under 0ms)': keep Moonfire on up to 1 targets (refresh under 0ms) (+1.8%, pass 1)
  2. rank 3 below 15% mana, above: cast Starfire (+0.7%, pass 1)
  3. always rank 1 instead of rank 3: if mana % < 15%: cast Starfire (+0.5%, pass 1)
  4. move down below 'cast Starfire': if mana % < 15%: cast Starfire (+0.3%, pass 1)
  5. only with 10s or more of the fight left: keep Insect Swarm on up to 1 targets (refresh under 0ms) (+0.2%, pass 2)
  6. insert at the end: cast Wrath (+0.2%, pass 5)
- **A fully buffed raid:** our tuned rotation (`raidsim/apl_opt.py`, 2026-10-01, 2 passes, the last 2026-10-09, 1 changes to the base rotation; third-seed check: balance-moonkin-raid 590 -> 591 DPS (+0.2%), sim preset: Balance 527 -> 526 DPS (-0.3%)):
  1. move down below 'keep Insect Swarm on up to 1 targets (refresh under 0ms)': keep Moonfire on up to 1 targets (refresh under 0ms) (+0.3%, pass 1)

Before the pull: at -10s: activate Moonkin Form.

| # | Priority (the first line whose condition holds is cast) | [`balance-moonkin-raid`](balance-moonkin-raid.md) casts/min |
|---|---|---|
| 1 | use every other cooldown when ready | as ready |
| 2 | if mana % ≤ 30%: cast Innervate | 0.3 |
| 3 | if time left in the fight ≥ 10s: keep Insect Swarm on up to 1 targets (refresh under 0ms) | 4.3 |
| 4 | keep Moonfire on up to 1 targets (refresh under 0ms) | 3.9 |
| 5 | cast Starfire | 15.0 |
| 6 | if mana % < 15%: cast Starfire (rank 1) | 1.0 |

Lines of the simulator's rotation these builds never cast: cast Wrath (its condition never held in these fights).

Damage by ability:

| Ability | [`balance-moonkin-raid`](balance-moonkin-raid.md) |
|---|---|
| Starfire | 64% |
| Moonfire | 18% |
| Insect Swarm | 18% |

## Notes

- Adopted from the community simulator on 2026-09-26: opt-balance-dps-raid-dps beat the previous draft by +6.3% DPS; the rationale below predates the adoption where it names talents no longer taken.
- Rotation hypothesis: Insect Swarm + Moonfire up, then Wrath -> Starfire x2 (Eclipse) alternating Nature/Arcane for Balance of Nature.
- Beta client 1.60.1.69893 removed Balance of Nature (5 points): re-spent as Improved Entangling Roots 3 + Overgrowth 2 (control utility; the optimizer build says where the model would put them).
- 2026-09-27 scenario audit: Swiftmend 1 -> Heart of the Wild 1. Swiftmend is an instant heal that consumes a Rejuvenation or Regrowth: a Moonkin in a raid casts neither. Heart of the Wild's Intellect is mana and spell crit (scorer +0.2 points; the simulator does not separate a single rank).
- 2026-09-29 filler audit (raidsim/filler_audit.py, user question on zero-value fillers): points the simulator measures at 0 moved, one at a time, to talents that help in a real raid (interrupt protection, threat, mana, range, survival; the simulator cannot see these, so the order is our judgment) or that gain DPS: Subtlety -> Heart of the Wild (+0.4% DPS); Subtlety -> Heart of the Wild (+0.4% DPS). Net +0.84% on a third seed.

## Open questions (verify in the live game)

- Moonfury per-rank value; Eclipse charge behaviour; whether Moonkin's crit aura stacks with Leader of the Pack (demo says exclusive).

## Sources

- <https://warcraftforever.games/talents/druid>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
