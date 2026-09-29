# Assassination — Mutilate / Venom (raid DPS) — 31/20/0

*[Rogue](../../../README.md) · [Raids: training dummy, raid and parse](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 31/20/0 (Assassination / Combat / Subtlety) |
| **Role** | DPS — Raid |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70009 (2026-09-25 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

A genuinely new spec: Mutilate (both weapons, 2 combo points, +20% vs. poisoned targets) at Assassination tier 5, Seal Fate (100% extra combo point on crits at max rank), Vigor and the Venom capstone (+30% poison damage), with Puncturing Wounds, Precision and Dual Wield Specialization from Combat. No Classic baseline — built from the demo tree.

## Point allocation

### Assassination (31)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Malice** | 5/5 | changed | Increases your critical strike chance with all attacks and Poisons by 5%. |
| **Ruthlessness** | 3/3 | unchanged | Gives your finishing moves a 60% chance to add a Combo Point to your target. |
| **Murder** | 2/2 | changed | Increases all damage dealt by 4% against Humanoid and Giant targets. |
| **Improved Slice and Dice** | 3/3 | unchanged | Increases the duration of your Slice and Dice ability by 45%. |
| **Relentless Strikes** | 1/1 | unchanged | Your finishing moves have a 20% chance per Combo Point to restore 25 Energy. |
| **Lethality** | 5/5 | changed | Increases the critical strike damage bonus of your Sinister Strike, Gouge, Backstab, Mutilate, Ghostly Strike, and Hemorrhage abilities by 20%. |
| **Vile Poisons** | 2/5 | moved | Increases the damage dealt by your poisons by 8% and gives your poisons an additional 16% chance to resist dispel effects. |
| **Cold Blood** | 1/1 | changed | When activated, increases the critical strike chance of your next Sinister Strike, Backstab, Ambush, Eviscerate, or Mutilate by 100%. |
| **Vigor** | 2/2 | changed | Increases your maximum Energy by 10. |
| **Mutilate** | 1/1 | **NEW** | Instantly attacks with both weapons for 75% weapon damage plus an additional 13 with each weapon. Damage increased by 20% against Poisoned targets. Awards 2 Combo Points. |
| **Seal Fate** | 5/5 | moved | Your critical strikes from abilities that add Combo Points have a 100% chance to add an additional Combo Point. |
| **Venom** | 1/1 | **NEW** | Finishing move that increases the damage of your Poisons by 30% and your chance to apply Poisons by 10%. Lasts longer per combo point:  1 point : 9 seconds  2 points: 12 seconds  3 points: 15 seconds  4 points: 18 seconds  5 points: 21 seconds |

### Combat (20)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Improved Eviscerate** | 3/3 | changed | Increases the damage done by your Eviscerate ability by 20%. |
| **Lightning Reflexes** | 2/5 | unchanged | Increases your Dodge chance by 2%. |
| **Puncturing Wounds** | 3/3 | **NEW** | Increases the critical strike chance of your Backstab by 30% and your Mutilate by 15%, and gives Backstab a 45% chance to add an additional Combo Point. |
| **Precision** | 3/3 | changed | Improves your chance to hit by 3%. |
| **Endurance** | 2/2 | changed | Reduces the cooldown of your Sprint and Evasion abilities by 60%. |
| **Improved Sprint** | 2/2 | unchanged | Gives a 100% chance to remove all movement impairing effects when you activate your Sprint ability. |
| **Dual Wield Specialization** | 5/5 | changed | Increases the damage done by your off-hand weapon by 25%. |

### Subtlety (0)

*No points.*

## Core talents (priority order)

1. **Mutilate** — Both weapons, 2 combo points, +20% vs. poisoned targets, no positional requirement.
2. **Seal Fate** — Every crit from a combo-point builder adds a combo point at max rank — with Mutilate's two hits, 5-point finishers every other global.
3. **Venom** — Capstone finisher: +30% poison damage and +10% poison application for up to 21s.
4. **Puncturing Wounds** — +15% Mutilate crit.
5. **Lethality** — +30% crit damage on Mutilate.
6. **Malice** — +5% crit with attacks and poisons.
7. **Dual Wield Specialization** — Mutilate hits with both weapons.
8. **Precision** — +3% hit with attacks and poisons.
9. **Vigor** — +10 max energy — Mutilate costs 60.
10. **Cold Blood** — Guaranteed Mutilate/Eviscerate crit (tier 4 now).
11. **Improved Slice and Dice** — Slice and Dice uptime.

## Flex points

| Pts | Default | Alternatives | Why |
|---|---|---|---|
| 2 | Vile Poisons | Improved Poisons, Improved Kidney Shot | Two points needed to reach Seal Fate; poison damage vs. poison application. |
| 4 | Endurance 2 + Improved Sprint 2 | Improved Kick, Deflection | Tier-3 Combat filler on the way to Dual Wield Specialization. |

## Rank among our builds and the community simulator's

**3 of 4** for `assassination-raid` by training-dummy DPS in the community simulator (ElliotWood/Forever 40be98e); full ranking and the other builds' rotations: [raid README](../README.md), [raid rotations](../rotation.md).

| Rank | Build | By | Split | Dummy DPS | vs best | Raid DPS | vs best in a raid | Out of mana on the dummy |
|---|---|---|---|---|---|---|---|---|
| 1 | [`assassination-seal-fate-raid`](assassination-seal-fate-raid.md) | ours: hand draft | 30/19/2 | 407 | +0.0% | 682 | +0.0% | 0 s |
| 2 | *Mutilate* | community simulator | - | 371 | -8.8% | 648 | -5.0% | 0 s |
| 3 | **[`assassination-mutilate-raid`](assassination-mutilate-raid.md)** | ours: hand draft | 31/20/0 | 369 | -9.2% | 647 | -5.1% | 0 s |
| 4 | *Assassination Mutilate 31/20/0* | community simulator | - | 359 | -11.7% | 630 | -7.7% | 0 s |

## Rotation (community simulator, training dummy)

- **The training dummy:** our tuned rotation (`raidsim/apl_opt.py`, 2026-09-28, 4 passes, the last 2026-09-29, 7 changes to the base rotation; third-seed check: assassination-seal-fate-raid 148 -> 413 DPS (+179.2%), sim preset: Mutilate 335 -> 377 DPS (+12.4%)):
  1. insert at the top: if time left on Expose Armor < 3 and combo points ≥ 5 and time left in the fight ≥ 3: cast Expose Armor (+8.6%, pass 1)
  2. threshold 5 -> 3.75: if time left on Expose Armor < 3 and combo points ≥ 5 and time left in the fight ≥ 3: cast Expose Armor (+0.8%, pass 1)
  3. insert at the top: cast Backstab (+1.6%, pass 1)
  4. only with 10s or more of the fight left: if time left on Expose Armor < 3 and combo points ≥ 3.75 and time left in the fight ≥ 3: cast Expose Armor (+0.2%, pass 1)
  5. threshold 6 -> 12: if (combo points ≥ 1 and not Slice and Dice is up and time left in the fight ≥ 6 or combo points ≥ 5 and time left on Slice and Dice < 3 and time left in the fight > 9): cast Slice and Dice (+0.2%, pass 1)
  6. threshold 4 -> 5: if combo points ≥ 4 and Slice and Dice is up: cast Cold Blood + drop 'combo points ≥ 5 and time left on Slice and Dice < 3 and time left in the fight > 9' from the condition: if (combo points ≥ 1 and not Slice and Dice is up and time left in the fight ≥ 12 or combo points ≥ 5 and time left on Slice and Dice < 3 and time left in the fight > 9): cast Slice and Dice (+0.3%, pass 1)
  7. insert at the top: if energy ≤ 29 and timeToNextEnergyTick > 1 and combo points < 5 and not Adrenaline Rush is up: cast Thistle Tea + threshold 29 -> 43.5: if energy ≤ 29 and timeToNextEnergyTick > 1 and combo points < 5 and not Adrenaline Rush is up: cast Thistle Tea (+0.3%, pass 3)
- **A fully buffed raid:** our tuned rotation (`raidsim/apl_opt.py`, 2026-09-28, 4 passes, the last 2026-09-29, 1 changes to the base rotation; third-seed check: assassination-seal-fate-raid 294 -> 693 DPS (+135.8%), sim preset: Mutilate 652 -> 659 DPS (+1.1%)):
  1. insert before the filler: cast Backstab (+0.8%, pass 1)

| # | Priority (the first line whose condition holds is cast) | [`assassination-mutilate-raid`](assassination-mutilate-raid.md) casts/min |
|---|---|---|
| 1 | if energy ≤ 43.5 and timeToNextEnergyTick > 1 and combo points < 5 and not Adrenaline Rush is up: cast Thistle Tea | as ready |
| 2 | cast Backstab | 10.9 |
| 3 | if time left on Expose Armor < 3 and combo points ≥ 3.75 and time left in the fight ≥ 3 and time left in the fight ≥ 10s: cast Expose Armor | 1.8 |
| 4 | if combo points ≥ 1 and not Slice and Dice is up and time left in the fight ≥ 12: cast Slice and Dice | 2.8 |
| 5 | if Slice and Dice is up: use every other cooldown when ready | as ready |
| 6 | if combo points ≥ 5 and Slice and Dice is up: cast Cold Blood | 0.3 |
| 7 | if combo points ≥ 4 and (Slice and Dice is up or energy ≥ 79 or time left in the fight < 6): cast Eviscerate | 1.9 |

Lines of the simulator's rotation these builds never cast: cast Mutilate (its condition never held in these fights).

Damage by ability:

| Ability | [`assassination-mutilate-raid`](assassination-mutilate-raid.md) |
|---|---|
| Auto Attack | 45% |
| Backstab | 31% |
| Eviscerate | 9% |
| Deadly Poison | 7% |
| Dense Sharpening Stone | 4% |
| Dragonbreath Chili | 2% |
| item 10646 | 2% |

## Notes

- Rotation hypothesis: Slice and Dice -> Mutilate to 4-5 points -> Venom (keep up) -> Eviscerate/Rupture; poisons on both weapons.
- Gives up Blade Flurry, Adrenaline Rush, Hack and Slash and Restless Blades — the comparison with Combat daggers is the key launch test.
- Mutilate in the simulator (new-builds survey, 2026-09-28): the tuned Assassination rotation casts Backstab before Mutilate (Backstab out-damages it with the simulator's daggers), so this draft plays as a Backstab build there; the simulator talent search's version is assassination-seal-fate-raid (Mutilate's point moved to Improved Poisons).

## Open questions (verify in the live game)

- Mutilate damage at level 60 (demo shows level-38 numbers) and whether Venom's poison bonus makes poison builds the top damage.
- Whether poisons still consume charges / how Improved Poisons interacts with Windfury Totem for Horde.

## Sources

- <https://warcraftforever.games/talents/rogue>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
