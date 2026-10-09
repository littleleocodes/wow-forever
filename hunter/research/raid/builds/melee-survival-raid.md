# Melee Survival — Lone Wolf (dual wield, raid) — 5/11/35

*[Hunter](../../../README.md) · [Raids: training dummy, raid and parse](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 5/11/35 (Beast Mastery / Marksmanship / Survival) |
| **Role** | DPS — Raid |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70009 (2026-09-25 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

Forever's melee hunter for raids, built around traps: Survival's melee package (Predator's Edge with dual wield, Savage Strikes, Expose Prey, Lacerating Strikes, Strider Kick, Lightning Reflexes, Improved Tracking, Surefooted, Resourcefulness) plus the trap talents (Survivalist's Discipline, Clever Traps, Survival Tactics) for an Immolation Trap every 18 s under the boss, with Marksmanship's Lethal Attacks, Careful Aim and Lone Wolf, and Deadly Aspects for the Aspect of the Beast haste proc. The most popular hunter build on talentsforever.com (2026-09-28); the simulator's talent search from our previous draft found the same trap talents and nothing better.

## Point allocation

### Beast Mastery (5)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Deadly Aspects** | 5/5 | **NEW** | While Aspect of the Hawk is active, Auto Shot has a 10% chance of increasing ranged attack speed by 30% for 12 sec. While Aspect of the Beast is active, all melee auto attacks have a 10% chance of increasing melee attack speed by 30% for 12 sec. |

### Marksmanship (11)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Lethal Attacks** | 5/5 | **NEW** | Increases your critical strike chance with all attacks by 5%. |
| **Careful Aim** | 5/5 | **NEW** | Increases your Attack Power by 100% of your Intellect. |
| **Lone Wolf** | 1/1 | **NEW** | You deal 20% increased damage with all attacks while you do not have an active pet. |

### Survival (35)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Improved Tracking** | 5/5 | **NEW** | While tracking Beasts, Demons, Dragonkin, Elementals, Giants, Humanoids, or Undead, all damage you deal to the tracked creature type is increased by 5%. |
| **Savage Strikes** | 2/2 | changed | Increases the critical strike chance of all your melee abilities by 4%. |
| **Survivalist** | 3/5 | changed | Increases your total Health by 6%. |
| **Clever Traps** | 2/2 | unchanged | Increases the duration of Freezing and Frost trap effects by 30% and the damage of Immolation and Explosive trap effects by 30%. |
| **Surefooted** | 3/3 | changed | Increases your hit chance by 3% and reduces the duration of movement impairing effects on you by 30%. |
| **Survival Tactics** | 2/2 | **NEW** | Increases your chance to hit with your Trap and Feign Death abilities by 10%. |
| **Predator's Edge** | 5/5 | **NEW** | Increases your melee critical strike damage by 30% and your Off Hand weapon damage by 50%. |
| **Resourcefulness** | 2/2 | **NEW** | Reduces the mana cost of your Trap abilities and melee abilities by 60%. In addition, your critical strikes have a 60% chance to allow 50% of your Mana regeneration to continue while casting for 30 sec. |
| **Expose Prey** | 2/2 | **NEW** | Your attacks against targets with Hunter's Mark have a 10% chance to activate your Mongoose Bite for 10 sec. |
| **Survivalist's Discipline** | 2/2 | **NEW** | Reduces the cooldown of your Trap and Deterrence abilities by 40%. |
| **Strider Kick** | 1/1 | **NEW** | A powerful kick that deals 100% melee weapon damage and increases movement speed by 30% for 3 sec. |
| **Lightning Reflexes** | 5/5 | changed | Increases your Agility by 10%. |
| **Lacerating Strikes** | 1/1 | **NEW** | Your Mongoose Bite also causes the target to Bleed for damage equal to 40% of the damage done by Mongoose Bite over 21 sec |

## Core talents (priority order)

1. **Predator's Edge** — +30% melee critical damage and +50% off-hand weapon damage: the reason to dual-wield; the biggest single multiplier of the build.
2. **Lone Wolf** — +20% on every attack with no pet; a melee hunter fights beside the mob anyway, so the pet's threat matters less than the damage.
3. **Expose Prey** — Attacks against a marked target activate Mongoose Bite (10% chance at 2/2): Mongoose Bite every few seconds instead of only after a dodge, and Lacerating Strikes needs it.
4. **Survivalist's Discipline** — -40% trap cooldown: Immolation Trap every 18 s instead of 30 s. The largest single move of the talent search (+4.3% on the dummy).
5. **Clever Traps** — +30% Immolation and Explosive Trap damage (+3.1% on the dummy in the talent search).
6. **Survival Tactics** — +10% chance to hit with traps: a trap that misses a level-63 boss is 18 s of nothing (+1.1% on the dummy).
7. **Lacerating Strikes** — Every Mongoose Bite also bleeds for 40% of its damage over 21 s: the 31-point capstone of the melee tree.
8. **Lethal Attacks** — +5% critical strike chance with all attacks, doubled in value by Predator's Edge's crit damage.
9. **Savage Strikes** — +4% crit on Raptor Strike, Mongoose Bite, Counterattack and Strider Kick.
10. **Deadly Aspects** — Under Aspect of the Beast every melee swing has a 10% chance of +30% attack speed for 12 s.
11. **Strider Kick** — 100% weapon damage every 8 s for a trivial mana cost, plus a sprint.
12. **Improved Tracking** — +5% damage against the tracked creature type: every raid boss is a beast, demon, dragon, elemental, giant, humanoid or undead.
13. **Lightning Reflexes** — +15% Agility: attack power and crit.
14. **Resourcefulness** — -60% mana on traps and melee abilities and regen on crits: the build never runs out of mana, which is why Efficiency measures zero.
15. **Careful Aim** — Attack power from Intellect.

## Flex points

| Pts | Default | Alternatives | Why |
|---|---|---|---|
| 3 | Survivalist | Deflection, Efficiency | Survival points on the way to the deeper talents: +6% health. Efficiency measures zero here (Resourcefulness already covers the mana), Deflection needs the boss to attack you. |
| 3 | Surefooted | Survivalist | +3% hit against a level-63 boss. |

## Rank among our builds and the community simulator's

**2 of 5** for `melee-dps` by training-dummy DPS in the community simulator (ElliotWood/Forever 2ce8265); full ranking and the other builds' rotations: [raid README](../README.md), [raid rotations](../rotation.md).

| Rank | Build | By | Split | Dummy DPS | vs best | Raid DPS | vs best in a raid | Out of mana on the dummy |
|---|---|---|---|---|---|---|---|---|
| 1 | [`survival-raid`](survival-raid.md) | ours: hand draft | 5/16/30 | 486 | +0.0% | 1028 | -2.1% | 9 s |
| 2 | **[`melee-survival-raid`](melee-survival-raid.md)** | ours: hand draft | 5/11/35 | 464 | -4.6% | 1048 | -0.1% | 44 s |
| 3 | [`opt-melee-dps-raid-dps`](opt-melee-dps-raid-dps.md) | ours: optimizer | 5/15/31 | 463 | -4.7% | 1016 | -3.2% | 8 s |
| 4 | [`beast-survival-open-raid`](beast-survival-open-raid.md) | ours: hand draft | 16/11/24 | 360 | -25.8% | 1049 | +0.0% | 126 s |
| 5 | [`survival-ml-parse`](survival-ml-parse.md) | ours: parse build | 5/14/32 | 359 | -26.2% | 999 | -4.8% | 117 s |

## Rotation (community simulator, training dummy)

- **The training dummy:** our tuned rotation (`raidsim/apl_opt.py`, 2026-09-29, 8 passes, the last 2026-10-05, 9 changes to the base rotation; third-seed check: open winner 298 -> 363 DPS (+21.9%), survival-raid 313 -> 445 DPS (+42.1%), melee-survival-raid 319 -> 423 DPS (+32.5%), opt-melee-dps-raid-dps 319 -> 426 DPS (+33.2%)):
  1. insert before the filler: cast Wing Clip (+7.4%, pass 1)
  2. spell probe: insert at the top: if auraIsInactive: cast Summon Hawk (+14.3%, pass 2)
  3. insert in the middle: cast Major Mana Potion (+0.4%, pass 3)
  4. move to the top: cast Immolation Trap (+0.5%, pass 3)
  5. move to the top: cast Raptor Strike (+0.3%, pass 3)
  6. move down below 'cast Strider Kick': cast Major Mana Potion (+0.4%, pass 4)
  7. move to the top: cast Mongoose Bite (+0.2%, pass 4)
  8. move to the top: cast Aspect of the Beast (+0.2%, pass 4)
  9. move to the top: if auraIsInactive: cast Summon Hawk (+0.3%, pass 7)
- **A fully buffed raid:** our tuned rotation (`raidsim/apl_opt.py`, 2026-09-29, 9 passes, the last 2026-10-09, 2 changes to the base rotation; third-seed check: survival-raid 749 -> 1027 DPS (+37.1%), melee-survival-raid 764 -> 1047 DPS (+37.0%), opt-melee-dps-raid-dps 764 -> 1017 DPS (+33.0%), survival-ml-parse 729 -> 998 DPS (+37.0%), beast-survival-open-raid 736 -> 1051 DPS (+42.7%)):
  1. insert before the filler: cast Wing Clip (+10.3%, pass 1)
  2. spell probe: insert in the middle: if auraIsInactive: cast Summon Hawk (+15.0%, pass 2)

Before the pull: at -3s: cast Hunter's Mark.

| # | Priority (the first line whose condition holds is cast) | [`melee-survival-raid`](melee-survival-raid.md) casts/min |
|---|---|---|
| 1 | cast Aspect of the Beast | 0.3 |
| 2 | cast Mongoose Bite | 10.9 |
| 3 | cast Raptor Strike | 18.4 |
| 4 | cast Immolation Trap | 3.0 |
| 5 | use every other cooldown when ready | as ready |
| 6 | cast Strider Kick | 5.1 |
| 7 | cast Major Mana Potion | as ready |
| 8 | cast Wing Clip | 19.6 |

Lines of the simulator's rotation these builds never cast: cast Summon Hawk (needs the Summon Hawk talent); cast Counterattack (needs the Counterattack talent); cast Explosive Trap (its condition never held in these fights).

Damage by ability:

| Ability | [`melee-survival-raid`](melee-survival-raid.md) |
|---|---|
| Auto Attack | 45% |
| Raptor Strike | 15% |
| Mongoose Bite | 13% |
| Immolation Trap | 12% |
| Strider Kick | 7% |
| Wing Clip | 5% |
| Dragonbreath Chili | 3% |

## Notes

- Adopted 2026-09-29 (user request): the talentsforever.com #1 hunter build (5/11/35) beat the previous draft by +8.7% on the training dummy (380.1 vs 349.9) and +4.6% in the raid setting (791.7 vs 757.2) with the trap rotation, on two independent seeds (community simulator 40be98e). raidsim/talent_opt.py from both builds, dummy and raid: from the old draft it took exactly Survivalist's Discipline, Clever Traps and Survival Tactics (it paid with Deadly Aspects, which the simulator scores at zero because it lacks the melee haste proc); from this build no move wins. The old draft is kept as raidsim/candidates/cand-melee-dps-hand-2026-09-29.json.
- Rotation: dual wield two fast one-handers; Aspect of the Beast on; Hunter's Mark and Serpent Sting from range on the pull, then Mongoose Bite when active, Strider Kick on cooldown, Raptor Strike on the next swing, and Immolation Trap under the boss whenever it is off cooldown (fire traps share a cooldown; Explosive Trap instead on packs).
- No pet: Lone Wolf's +20% beats the pet's damage once the hunter melees (the model's raid pet share is 12%, the break-even 16.7%). Beast Mastery's pet talents are absent for that reason.
- The community simulator plays this build on our own melee rotation (raidsim/specs.json melee-dps); it models only Aspect of the Hawk, so Aspect of the Beast's attack power and Deadly Aspects' haste are missing and the DPS is a lower bound. The fight lab's melee rotation has no traps yet, so the leveling numbers leave the trap talents at zero.
- 2026-09-29 filler audit, undone 2026-10-06: it had moved Improved Tracking 5 -> Deflection because the simulator measured Improved Tracking at 0, but that was the bench's blind spot: its target had no creature type, and Improved Tracking is +5% damage against every raid creature type but Mechanical (the bench's target is an Elemental since 2026-10-06; it reads +4.9% in a full raid now). The 5 points are back in Improved Tracking.

## Open questions (verify in the live game)

- Whether traps can be placed in combat and trigger at once under a boss, as the simulator assumes.
- Fire traps sharing one cooldown (the user's reading, and the simulator's model): with separate cooldowns Explosive Trap adds about 5% more on the dummy.
- Survival Tactics' +10% trap hit: whether traps can miss a boss at all.
- Expose Prey's proc rate against a marked target (5%/rank per attack assumed) decides how often Mongoose Bite is available; check the actual rate in the beta.
- Whether Aspect of the Beast (+110 melee attack power) and the Deadly Aspects melee haste proc work as the tooltips read.
- Lacerating Strikes: 40% of Mongoose Bite over 21 s; whether the bleed can crit or stack.

## Sources

- <https://talentsforever.com/hunter/60/5-005005001-500230230250222151-4>
- <https://warcraftforever.games/talents/hunter>
- <beta client 1.60.1.70009 tooltips (_reference/data/forever-talents/hunter.json)>
- <hunter/raid/raidsim/melee-dps.md>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
