# Assassination — Seal Fate / Vigor (raid DPS; formerly the Mutilate draft) — 29/22/0

*[Rogue](../../../README.md) · [Raids: training dummy, raid and parse](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 29/22/0 (Assassination / Combat / Subtlety) |
| **Role** | DPS — Raid |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70753 (2026-11-03 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

Seal Fate daggers with Vigor and Lethality: an Assassination Backstab build. It began as the Mutilate / Venom draft (a new Forever spec built from the demo tree), but the simulator's tuned rotation never casts Mutilate (Backstab out-damages it in the simulator), so its Mutilate point moved to Improved Poisons on 2026-10-02 (+0.7% DPS) and Venom left on 2026-09-29. Mutilate and Venom are launch questions, not part of this build; assassination-seal-fate-raid is the simulator search's sibling.

## Point allocation

### Assassination (29)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Improved Gouge** | 3/3 | changed | Increases the duration of your Gouge ability by 1.5 sec. |
| **Malice** | 5/5 | changed | Increases your critical strike chance with all attacks and Poisons by 5%. |
| **Remorseless Attacks** | 1/2 | changed | After killing a non-trivial enemy, gives you a 20% increased critical strike chance on your next Sinister Strike, Backstab, Ambush, Mutilate, or Ghostly Strike. Lasts 20 sec. |
| **Improved Expose Armor** | 2/2 | changed | Reduces the Energy cost of your Expose Armor ability by 10, and refunds 2 Combo Points when cast with 5 Combo Points. |
| **Improved Slice and Dice** | 3/3 | unchanged | Increases the duration of your Slice and Dice ability by 45%. |
| **Ruthlessness** | 3/3 | unchanged | Gives your finishing moves a 60% chance to add a Combo Point to your target. |
| **Lethality** | 2/2 | changed | Grants 20% increased Critical Strike damage to your Sinister Strike, Gouge, Backstab, Mutilate, Ghostly Strike, and Hemorrhage abilities. |
| **Vigor** | 2/2 | changed | Increases your maximum Energy by 10. |
| **Cold Blood** | 1/1 | changed | When activated, increases the critical strike chance of your next Sinister Strike, Backstab, Ambush, Eviscerate, or Mutilate by 100%. |
| **Improved Poisons** | 1/5 | changed | Increases the chance to apply Poisons to your target by 2%, and gives Poison applications a 10% chance to not consume a charge. |
| **Vile Poisons** | 2/5 | moved | Increases the damage dealt by your poisons by 8% and gives your poisons an additional 16% chance to resist dispel effects. |
| **Relentless Strikes** | 1/5 | unchanged | Your finishing moves have a 4% chance per Combo Point to restore 25 Energy. |
| **Seal Fate** | 3/3 | moved | Your critical strikes from abilities that add Combo Points have a 100% chance to add an additional Combo Point. |

### Combat (22)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Coup de Grace** | 3/3 | changed | Increases the damage done by your Eviscerate ability by 20%, and the damage and storage rate of your Death Mark ability by 20%. |
| **Lightning Reflexes** | 5/5 | unchanged | Increases your Dodge chance by 5%. |
| **Deflection** | 1/3 | changed | Increases your Parry chance by 2%. |
| **Precision** | 3/3 | changed | Improves your chance to hit by 3%. |
| **Puncturing Wounds** | 3/3 | **NEW** | Increases the critical strike chance of your Backstab by 30% and your Mutilate by 15%, and gives Backstab a 45% chance to add an additional Combo Point. |
| **Aggression** | 2/3 | changed | Increases the damage of Sinister Strike and Eviscerate by 10%. |
| **Flawless Execution** | 1/1 | **NEW** | Reduces the Energy cost of your Eviscerate ability by 15. |
| **Weapon Expertise** | 2/2 | changed | Reduces the chance for your attacks to be Dodged or Parried by 2%. |
| **Dual Wield Specialization** | 2/2 | changed | Increases the damage done by your off-hand weapon by 50%. |

### Subtlety (0)

*No points.*

## Core talents (priority order)

1. **Seal Fate** — Every crit from a combo-point builder adds a combo point: with Backstab's crit talents, frequent 5-point finishers.
2. **Puncturing Wounds** — +30% Backstab crit and a 45% chance for Backstab to add a combo point (beta tooltip).
3. **Lethality** — +20% crit damage bonus on Backstab (beta tooltip).
4. **Malice** — +5% crit with attacks and poisons.
5. **Dual Wield Specialization** — +25% off-hand damage (beta tooltip).
6. **Precision** — +3% hit with attacks and poisons.
7. **Vigor** — +10 maximum energy (pools energy for Backstab and finishers).
8. **Cold Blood** — A guaranteed Backstab or Eviscerate crit once per cooldown.
9. **Improved Slice and Dice** — Slice and Dice uptime.

## Flex points

| Pts | Default | Alternatives | Why |
|---|---|---|---|
| 2 | Vile Poisons | Improved Poisons, Improved Kidney Shot | Two points needed to reach Seal Fate; poison damage vs. poison application. |
| 4 | Endurance 2 + Improved Sprint 2 | Improved Kick, Deflection | Tier-3 Combat filler on the way to Dual Wield Specialization. |

## Rank among our builds and the community simulator's

**5 of 5** for `assassination-raid` by training-dummy DPS in the community simulator (wowsims/forever 92c4c35 (client 70755)); full ranking and the other builds' rotations: [raid README](../README.md), [raid rotations](../rotation.md).

| Rank | Build | By | Split | Dummy DPS | vs best | Raid DPS | vs best in a raid | Out of mana on the dummy |
|---|---|---|---|---|---|---|---|---|
| 1 | *Asn Muti* | community simulator | - | 434 | +0.0% | 793 | +0.0% | 0 s |
| 2 | [`assassination-ml-raid`](assassination-ml-raid.md) | ours: derived (ML search) | 29/22/0 | 316 | -27.1% | 619 | -21.9% | 0 s |
| 3 | [`assassination-seal-fate-raid`](assassination-seal-fate-raid.md) | ours: hand draft | 28/21/2 | 307 | -29.2% | 599 | -24.4% | 0 s |
| 4 | [`daggers-split-open-raid`](daggers-split-open-raid.md) | ours: derived (open search) | 28/21/2 | 305 | -29.7% | 598 | -24.6% | 0 s |
| 5 | **[`assassination-mutilate-raid`](assassination-mutilate-raid.md)** | ours: hand draft | 29/22/0 | 303 | -30.1% | 603 | -24.0% | 0 s |

## Rotation (community simulator, training dummy)

- **The training dummy:** our tuned rotation (`raidsim/apl_opt.py`, 2026-09-28, 9 passes, the last 2026-10-14, 11 changes to the base rotation; third-seed check: ):
  1. insert at the top: if time left on Expose Armor < 3 and combo points ≥ 5 and time left in the fight ≥ 3: cast Expose Armor (+8.6%, pass 1)
  2. threshold 5 -> 3.75: if time left on Expose Armor < 3 and combo points ≥ 5 and time left in the fight ≥ 3: cast Expose Armor (+0.8%, pass 1)
  3. insert at the top: cast Backstab (+1.6%, pass 1)
  4. only with 10s or more of the fight left: if time left on Expose Armor < 3 and combo points ≥ 3.75 and time left in the fight ≥ 3: cast Expose Armor (+0.2%, pass 1)
  5. threshold 6 -> 12: if (combo points ≥ 1 and not Slice and Dice is up and time left in the fight ≥ 6 or combo points ≥ 5 and time left on Slice and Dice < 3 and time left in the fight > 9): cast Slice and Dice (+0.2%, pass 1)
  6. threshold 4 -> 5: if combo points ≥ 4 and Slice and Dice is up: cast Cold Blood + drop 'combo points ≥ 5 and time left on Slice and Dice < 3 and time left in the fight > 9' from the condition: if (combo points ≥ 1 and not Slice and Dice is up and time left in the fight ≥ 12 or combo points ≥ 5 and time left on Slice and Dice < 3 and time left in the fight > 9): cast Slice and Dice (+0.3%, pass 1)
  7. insert at the top: if energy ≤ 29 and timeToNextEnergyTick > 1 and combo points < 5 and not Adrenaline Rush is up: cast Thistle Tea + threshold 29 -> 43.5: if energy ≤ 29 and timeToNextEnergyTick > 1 and combo points < 5 and not Adrenaline Rush is up: cast Thistle Tea (+0.3%, pass 3)
  8. spell probe: insert at the end: cast Hemorrhage (+8.4%, pass 5)
  9. spell probe: insert at the top: if auraIsInactive: cast Ghostly Strike (+2.0%, pass 5)
  10. drop: if energy ≤ 43.5 and timeToNextEnergyTick > 1 and combo points < 5 and not Adrenaline Rush is up: cast Thistle Tea (+2.8%, pass 8)
  11. spell probe: insert at the top: if auraIsInactive: cast Adrenaline Rush (+1.8%, pass 9)
- **A fully buffed raid:** our tuned rotation (`raidsim/apl_opt.py`, 2026-09-28, 13 passes, the last 2026-11-02, 8 changes to the base rotation; third-seed check: daggers-split-open-raid 611 -> 631 DPS (+3.3%), sim preset: Asn Muti 597 -> 617 DPS (+3.3%), assassination-mutilate-raid 262 -> 607 DPS (+132.1%), assassination-seal-fate-raid 267 -> 622 DPS (+132.6%), assassination-ml-raid 611 -> 631 DPS (+3.3%)):
  1. insert before the filler: cast Backstab (+0.8%, pass 1)
  2. spell probe: insert at the end: cast Hemorrhage (+9.9%, pass 5)
  3. spell probe: insert in the middle: if auraIsInactive: cast Ghostly Strike (+1.8%, pass 5)
  4. move down below 'cast Mutilate': cast Backstab (+0.2%, pass 9)
  5. spell probe: insert in the middle: if auraIsInactive: cast Adrenaline Rush (+1.4%, pass 11)
  6. insert at the top: if (energy ≤ 15 or Eureka! is known and energy ≤ 25 and Eureka! is up) and (combo points < 3 or variableRef or Eureka! is up): cast Thistle Tea (+1.3%, pass 12)
  7. insert at the top: if not variableRef and variableRef and variableRef and not Garrote is on the target: cast Garrote (+0.2%, pass 12)
  8. insert in the middle: if (combo points ≥ 5 or combo points = 4 and Mutilate is known or combo points ≥ 4 and time left on Slice and Dice ≤ 6s and not time left on Slice and Dice ≤ 2s or combo points ≥ 3 and time left in the fight ≤ 6s) and (not talentIsKnown or time left on Rupture ≥ 4 or energy ≥ 75 or time left in the fight ≤ 6s) and not false and false and (not Expose Armor is up or time left on Expose Armor ≤ 16s): cast Eviscerate (rank 8) (+0.3%, pass 13)

Before the pull: at -3: cast Blade Flurry; at -2s: cast Premeditation; at -1s: if variableRef: cast Stealth.

| # | Priority (the first line whose condition holds is cast) | [`assassination-mutilate-raid`](assassination-mutilate-raid.md) casts/min |
|---|---|---|
| 1 | if variableRef: groupReference | as ready |
| 2 | if not variableRef and variableRef and variableRef and not Garrote is on the target: cast Garrote | 0.3 |
| 3 | if not Garrote is on the target and energy ≥ current cost and not variableRef and variableRef and variableRef and not variableRef and time into the fight ≥ 1s: cast Vanish | 0.3 |
| 4 | if energy ≥ current cost and variableRef and variableRef and variableRef and not variableRef and time into the fight ≥ 1s: cast Vanish | 0.3 |
| 5 | if Slice and Dice is up: use every other cooldown when ready | as ready |
| 6 | groupReference | as ready |
| 7 | if (variableRef and combo points ≤ 3 and energy ≤ 80 or not variableRef and energy ≤ 80): cast spell 1329549 | 6.0 |
| 8 | if (not Blade Flurry is known or Blade Flurry is up): cast OffensivePotion | as ready |
| 9 | if (energy ≤ 15 and not talentIsKnown or Eureka! is known and energy ≤ 25 and energy ≤ 25 or energy ≤ 25 and spell 1325758 is on the target) and (combo points < 3 or variableRef or Eureka! is up): cast Thistle Tea | as ready |
| 10 | if variableRef and variableRef and not variableRef and not variableRef: cast Slice and Dice | 3.2 |
| 11 | if combo points = 5 and not variableRef and energy ≥ current cost and not variableRef and not Elune's Light is up: cast Cold Blood | 0.3 |
| 12 | if (combo points ≥ 5 or combo points = 4 and Mutilate is known or combo points ≥ 4 and time left on Slice and Dice ≤ 6s and not variableRef or combo points ≥ 3 and variableRef) and not variableRef and not talentIsKnown: cast Eviscerate (rank 8) | 3.5 |
| 13 | if not Mutilate is known and not Hemorrhage is known and not variableRef and variableRef and (not variableRef or energy > (current cost + current cost) and not variableRef or not variableRef or variableRef or variableRef) and variableRef: cast Sinister Strike | 14.6 |

Lines of the simulator's rotation these builds never cast: cast Ambush, cast Blood Fury, strict sequence: cast Blood Fury; cast Blade Flurry, cast Elune's Light, cast Eureka!, cast spell 1325758, cast Rupture, cast Backstab (rank 8) (its condition never held in these fights); cast Preparation (needs the Preparation talent); cast Adrenaline Rush, strict sequence: cast Blood Fury; cast Adrenaline Rush, strict sequence: cast Elune's Light; cast Adrenaline Rush (needs the Adrenaline Rush talent); cast Premeditation (needs the Premeditation talent); cast Ghostly Strike (needs the Ghostly Strike talent); cast Hemorrhage (needs the Hemorrhage talent); cast Mutilate (needs the Mutilate talent).

Damage by ability:

| Ability | [`assassination-mutilate-raid`](assassination-mutilate-raid.md) |
|---|---|
| Auto Attack | 43% |
| Eviscerate | 18% |
| Sinister Strike | 18% |
| spell 25349 | 10% |
| spell 11337 | 6% |
| Goblin Sapper Charge | 2% |
| Garrote | 2% |
| Shank | 1% |

## Notes

- Original rotation hypothesis (Mutilate draft): Slice and Dice -> Mutilate to 4-5 points -> Venom (keep up) -> Eviscerate/Rupture; the simulator plays Backstab instead.
- Gives up Blade Flurry, Adrenaline Rush, Hack and Slash and Restless Blades — the comparison with Combat daggers is the key launch test.
- Mutilate in the simulator (new-builds survey, 2026-09-28): the tuned Assassination rotation casts Backstab before Mutilate (Backstab out-damages it with the simulator's daggers), so this draft plays as a Backstab build there; the simulator talent search's version is assassination-seal-fate-raid (Mutilate's point moved to Improved Poisons).
- 2026-09-29 filler audit (raidsim/filler_audit.py, user question on zero-value fillers): points the simulator measures at 0 moved, one at a time, to talents that help in a real raid (interrupt protection, threat, mana, range, survival; the simulator cannot see these, so the order is our judgment) or that gain DPS: Murder -> Improved Expose Armor (+1.9% DPS); Murder -> Improved Expose Armor (+1.9% DPS); Venom -> Flawless Execution (+2.1% DPS); Endurance -> Lightning Reflexes (survival); Endurance -> Lightning Reflexes (survival); Improved Sprint -> Lightning Reflexes (survival); Improved Sprint -> Deflection (survival). Net +5.97% on a third seed.
- 2026-10-02 filler audit (raidsim/filler_audit.py, user question on zero-value fillers; 2026-10-02 user report on talents whose ability the rotation never casts: Mutilate was never cast here): points the simulator measures at 0 moved, one at a time, to talents that help in a real raid (interrupt protection, threat, mana, range, survival; the simulator cannot see these, so the order is our judgment) or that gain DPS: Mutilate -> Improved Poisons (+0.8% DPS). Net +0.67% on a third seed.
- 2026-11-03 (repair_builds.py, client build 1.60.1.70753 trees): 30/21/0 -> 29/22/0; Lethality 5 -> 2 (rank cap); Seal Fate 5 -> 3 (rank cap); Improved Eviscerate -> Coup de Grace (renamed); Dual Wield Specialization 5 -> 2 (rank cap); +1 Weapon Expertise (tier gating for Dual Wield Specialization); +1 Weapon Expertise (tier gating for Dual Wield Specialization); +1 Aggression (tier gating for Dual Wield Specialization); +1 Aggression (tier gating for Dual Wield Specialization); +1 Improved Gouge (tier gating for Seal Fate); +1 Improved Gouge (tier gating for Seal Fate); +1 Improved Gouge (tier gating for Seal Fate); +1 Remorseless Attacks (back into Assassination) (refill: the combat-daggers-raid model, raid-dps).

## Open questions (verify in the live game)

- At launch: does Mutilate beat Backstab for a dagger Assassination rogue? If it does, put a point back into Mutilate (it replaced Improved Poisons 1 of 5) and play it as the builder.
- Mutilate damage at level 60 (demo shows level-38 numbers) and whether Venom's poison bonus makes poison builds the top damage.
- Whether poisons still consume charges / how Improved Poisons interacts with Windfury Totem for Horde.

## Sources

- <https://warcraftforever.games/talents/rogue>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
