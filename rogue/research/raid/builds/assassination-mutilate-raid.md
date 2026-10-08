# Assassination — Seal Fate / Vigor (raid DPS; formerly the Mutilate draft) — 30/21/0

*[Rogue](../../../README.md) · [Raids: training dummy, raid and parse](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 30/21/0 (Assassination / Combat / Subtlety) |
| **Role** | DPS — Raid |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70009 (2026-09-25 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

Seal Fate daggers with Vigor and Lethality: an Assassination Backstab build. It began as the Mutilate / Venom draft (a new Forever spec built from the demo tree), but the simulator's tuned rotation never casts Mutilate (Backstab out-damages it in the simulator), so its Mutilate point moved to Improved Poisons on 2026-10-02 (+0.7% DPS) and Venom left on 2026-09-29. Mutilate and Venom are launch questions, not part of this build; assassination-seal-fate-raid is the simulator search's sibling.

## Point allocation

### Assassination (30)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Malice** | 5/5 | changed | Increases your critical strike chance with all attacks and Poisons by 5%. |
| **Ruthlessness** | 3/3 | unchanged | Gives your finishing moves a 60% chance to add a Combo Point to your target. |
| **Improved Slice and Dice** | 3/3 | unchanged | Increases the duration of your Slice and Dice ability by 45%. |
| **Relentless Strikes** | 1/1 | unchanged | Your finishing moves have a 20% chance per Combo Point to restore 25 Energy. |
| **Lethality** | 5/5 | changed | Increases the critical strike damage bonus of your Sinister Strike, Gouge, Backstab, Mutilate, Ghostly Strike, and Hemorrhage abilities by 20%. |
| **Vile Poisons** | 2/5 | moved | Increases the damage dealt by your poisons by 8% and gives your poisons an additional 16% chance to resist dispel effects. |
| **Cold Blood** | 1/1 | changed | When activated, increases the critical strike chance of your next Sinister Strike, Backstab, Ambush, Eviscerate, or Mutilate by 100%. |
| **Vigor** | 2/2 | changed | Increases your maximum Energy by 10. |
| **Seal Fate** | 5/5 | moved | Your critical strikes from abilities that add Combo Points have a 100% chance to add an additional Combo Point. |
| **Improved Expose Armor** | 2/2 | changed | Reduces the Energy cost of your Expose Armor ability by 10, and refunds 2 Combo Points when cast with 5 Combo Points. |
| **Improved Poisons** | 1/5 | changed | Increases the chance to apply Poisons to your target by 2%, and gives Poison applications a 10% chance to not consume a charge. |

### Combat (21)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Improved Eviscerate** | 3/3 | changed | Increases the damage done by your Eviscerate ability by 20%. |
| **Lightning Reflexes** | 5/5 | unchanged | Increases your Dodge chance by 5%. |
| **Puncturing Wounds** | 3/3 | **NEW** | Increases the critical strike chance of your Backstab by 30% and your Mutilate by 15%, and gives Backstab a 45% chance to add an additional Combo Point. |
| **Precision** | 3/3 | changed | Improves your chance to hit by 3%. |
| **Dual Wield Specialization** | 5/5 | changed | Increases the damage done by your off-hand weapon by 25%. |
| **Flawless Execution** | 1/1 | **NEW** | Reduces the Energy cost of your Eviscerate ability by 10. |
| **Deflection** | 1/3 | changed | Increases your Parry chance by 2%. |

### Subtlety (0)

*No points.*

## Core talents (priority order)

1. **Seal Fate** — Every crit from a combo-point builder adds a combo point: with Backstab's crit talents, frequent 5-point finishers.
2. **Venom** — Capstone finisher: +30% poison damage and +10% poison application for up to 21s.
3. **Puncturing Wounds** — +30% Backstab crit and a 45% chance for Backstab to add a combo point (beta tooltip).
4. **Lethality** — +20% crit damage bonus on Backstab (beta tooltip).
5. **Malice** — +5% crit with attacks and poisons.
6. **Dual Wield Specialization** — +25% off-hand damage (beta tooltip).
7. **Precision** — +3% hit with attacks and poisons.
8. **Vigor** — +10 maximum energy (pools energy for Backstab and finishers).
9. **Cold Blood** — A guaranteed Backstab or Eviscerate crit once per cooldown.
10. **Improved Slice and Dice** — Slice and Dice uptime.

## Flex points

| Pts | Default | Alternatives | Why |
|---|---|---|---|
| 2 | Vile Poisons | Improved Poisons, Improved Kidney Shot | Two points needed to reach Seal Fate; poison damage vs. poison application. |
| 4 | Endurance 2 + Improved Sprint 2 | Improved Kick, Deflection | Tier-3 Combat filler on the way to Dual Wield Specialization. |

## Rank among our builds and the community simulator's

**3 of 5** for `assassination-raid` by training-dummy DPS in the community simulator (ElliotWood/Forever b0f0df3); full ranking and the other builds' rotations: [raid README](../README.md), [raid rotations](../rotation.md).

| Rank | Build | By | Split | Dummy DPS | vs best | Raid DPS | vs best in a raid | Out of mana on the dummy |
|---|---|---|---|---|---|---|---|---|
| 1 | [`assassination-seal-fate-raid`](assassination-seal-fate-raid.md) | ours: hand draft | 30/19/2 | 407 | +0.0% | 728 | -0.7% | 0 s |
| 2 | [`assassination-ml-raid`](assassination-ml-raid.md) | ours: hand draft | 30/19/2 | 394 | -3.1% | 734 | +0.0% | 0 s |
| 3 | **[`assassination-mutilate-raid`](assassination-mutilate-raid.md)** | ours: hand draft | 30/21/0 | 394 | -3.2% | 714 | -2.7% | 0 s |
| 4 | *Mutilate* | community simulator | - | 371 | -8.9% | 692 | -5.7% | 0 s |
| 5 | *Assassination Mutilate 31/20/0* | community simulator | - | 359 | -11.8% | 674 | -8.1% | 0 s |

## Rotation (community simulator, training dummy)

- **The training dummy:** our tuned rotation (`raidsim/apl_opt.py`, 2026-09-28, 7 passes, the last 2026-10-07, 9 changes to the base rotation; third-seed check: open winner 149 -> 401 DPS (+169.4%), assassination-seal-fate-raid 148 -> 406 DPS (+173.7%), sim preset: Mutilate 335 -> 371 DPS (+10.8%), assassination-mutilate-raid 143 -> 394 DPS (+175.2%), assassination-ml-raid 148 -> 394 DPS (+165.5%)):
  1. insert at the top: if time left on Expose Armor < 3 and combo points ≥ 5 and time left in the fight ≥ 3: cast Expose Armor (+8.6%, pass 1)
  2. threshold 5 -> 3.75: if time left on Expose Armor < 3 and combo points ≥ 5 and time left in the fight ≥ 3: cast Expose Armor (+0.8%, pass 1)
  3. insert at the top: cast Backstab (+1.6%, pass 1)
  4. only with 10s or more of the fight left: if time left on Expose Armor < 3 and combo points ≥ 3.75 and time left in the fight ≥ 3: cast Expose Armor (+0.2%, pass 1)
  5. threshold 6 -> 12: if (combo points ≥ 1 and not Slice and Dice is up and time left in the fight ≥ 6 or combo points ≥ 5 and time left on Slice and Dice < 3 and time left in the fight > 9): cast Slice and Dice (+0.2%, pass 1)
  6. threshold 4 -> 5: if combo points ≥ 4 and Slice and Dice is up: cast Cold Blood + drop 'combo points ≥ 5 and time left on Slice and Dice < 3 and time left in the fight > 9' from the condition: if (combo points ≥ 1 and not Slice and Dice is up and time left in the fight ≥ 12 or combo points ≥ 5 and time left on Slice and Dice < 3 and time left in the fight > 9): cast Slice and Dice (+0.3%, pass 1)
  7. insert at the top: if energy ≤ 29 and timeToNextEnergyTick > 1 and combo points < 5 and not Adrenaline Rush is up: cast Thistle Tea + threshold 29 -> 43.5: if energy ≤ 29 and timeToNextEnergyTick > 1 and combo points < 5 and not Adrenaline Rush is up: cast Thistle Tea (+0.3%, pass 3)
  8. spell probe: insert at the end: cast Hemorrhage (+8.4%, pass 5)
  9. spell probe: insert at the top: if auraIsInactive: cast Ghostly Strike (+2.0%, pass 5)
- **A fully buffed raid:** our tuned rotation (`raidsim/apl_opt.py`, 2026-09-28, 7 passes, the last 2026-10-07, 3 changes to the base rotation; third-seed check: open winner 337 -> 771 DPS (+128.9%), assassination-seal-fate-raid 322 -> 728 DPS (+126.4%), sim preset: Mutilate 701 -> 693 DPS (-1.2%), assassination-mutilate-raid 318 -> 713 DPS (+124.3%), assassination-ml-raid 322 -> 734 DPS (+128.1%)):
  1. insert before the filler: cast Backstab (+0.8%, pass 1)
  2. spell probe: insert at the end: cast Hemorrhage (+9.9%, pass 5)
  3. spell probe: insert in the middle: if auraIsInactive: cast Ghostly Strike (+1.8%, pass 5)

| # | Priority (the first line whose condition holds is cast) | [`assassination-mutilate-raid`](assassination-mutilate-raid.md) casts/min |
|---|---|---|
| 1 | if energy ≤ 43.5 and timeToNextEnergyTick > 1 and combo points < 5 and not Adrenaline Rush is up: cast Thistle Tea | as ready |
| 2 | cast Backstab | 11.5 |
| 3 | if time left on Expose Armor < 3 and combo points ≥ 3.75 and time left in the fight ≥ 3 and time left in the fight ≥ 10s: cast Expose Armor | 1.8 |
| 4 | if combo points ≥ 1 and not Slice and Dice is up and time left in the fight ≥ 12: cast Slice and Dice | 2.8 |
| 5 | if Slice and Dice is up: use every other cooldown when ready | as ready |
| 6 | if combo points ≥ 5 and Slice and Dice is up: cast Cold Blood | 0.3 |
| 7 | if combo points ≥ 4 and (Slice and Dice is up or energy ≥ 79 or time left in the fight < 6): cast Eviscerate | 2.7 |

Lines of the simulator's rotation these builds never cast: cast Ghostly Strike (needs the Ghostly Strike talent); cast Mutilate (needs the Mutilate talent); cast Hemorrhage (needs the Hemorrhage talent).

Damage by ability:

| Ability | [`assassination-mutilate-raid`](assassination-mutilate-raid.md) |
|---|---|
| Auto Attack | 43% |
| Backstab | 30% |
| Eviscerate | 13% |
| Deadly Poison | 7% |
| Dense Sharpening Stone | 4% |
| Dragonbreath Chili | 2% |
| Goblin Sapper Charge | 2% |

## Notes

- Original rotation hypothesis (Mutilate draft): Slice and Dice -> Mutilate to 4-5 points -> Venom (keep up) -> Eviscerate/Rupture; the simulator plays Backstab instead.
- Gives up Blade Flurry, Adrenaline Rush, Hack and Slash and Restless Blades — the comparison with Combat daggers is the key launch test.
- Mutilate in the simulator (new-builds survey, 2026-09-28): the tuned Assassination rotation casts Backstab before Mutilate (Backstab out-damages it with the simulator's daggers), so this draft plays as a Backstab build there; the simulator talent search's version is assassination-seal-fate-raid (Mutilate's point moved to Improved Poisons).
- 2026-09-29 filler audit (raidsim/filler_audit.py, user question on zero-value fillers): points the simulator measures at 0 moved, one at a time, to talents that help in a real raid (interrupt protection, threat, mana, range, survival; the simulator cannot see these, so the order is our judgment) or that gain DPS: Murder -> Improved Expose Armor (+1.9% DPS); Murder -> Improved Expose Armor (+1.9% DPS); Venom -> Flawless Execution (+2.1% DPS); Endurance -> Lightning Reflexes (survival); Endurance -> Lightning Reflexes (survival); Improved Sprint -> Lightning Reflexes (survival); Improved Sprint -> Deflection (survival). Net +5.97% on a third seed.
- 2026-10-02 filler audit (raidsim/filler_audit.py, user question on zero-value fillers; 2026-10-02 user report on talents whose ability the rotation never casts: Mutilate was never cast here): points the simulator measures at 0 moved, one at a time, to talents that help in a real raid (interrupt protection, threat, mana, range, survival; the simulator cannot see these, so the order is our judgment) or that gain DPS: Mutilate -> Improved Poisons (+0.8% DPS). Net +0.67% on a third seed.

## Open questions (verify in the live game)

- At launch: does Mutilate beat Backstab for a dagger Assassination rogue? If it does, put a point back into Mutilate (it replaced Improved Poisons 1 of 5) and play it as the builder.
- Mutilate damage at level 60 (demo shows level-38 numbers) and whether Venom's poison bonus makes poison builds the top damage.
- Whether poisons still consume charges / how Improved Poisons interacts with Windfury Totem for Horde.

## Sources

- <https://warcraftforever.games/talents/rogue>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
