# Melee Survival — Lone Wolf (dual wield, raid) — 5/15/31

*[Hunter](../../README.md) · [Raids: training dummy, raid and parse](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 5/15/31 (Beast Mastery / Marksmanship / Survival) |
| **Role** | DPS — Raid |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70009 (2026-09-25 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

Forever's melee hunter for raids: Survival's melee package (Predator's Edge with dual wield, Savage Strikes, Expose Prey, Lacerating Strikes, Strider Kick, Lightning Reflexes, Improved Tracking, Surefooted, Resourcefulness) with Marksmanship's Lethal Attacks, Careful Aim, Efficiency and Lone Wolf, and Deadly Aspects for the Aspect of the Beast haste proc. No parry or dodge talents: a raid melee stands behind the boss and is never attacked. The scorer's optimum for the melee-dps model under the raid profile (2026-09-27); the model's damage split is a tooltip assumption until a melee rotation exists in a simulator.

## Point allocation

### Beast Mastery (5)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Deadly Aspects** | 5/5 | **NEW** | While Aspect of the Hawk is active, Auto Shot has a 10% chance of increasing ranged attack speed by 30% for 12 sec. While Aspect of the Beast is active, all melee auto attacks have a 10% chance of increasing melee attack speed by 30% for 12 sec. |

### Marksmanship (15)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Lethal Attacks** | 5/5 | **NEW** | Increases your critical strike chance with all attacks by 5%. |
| **Careful Aim** | 5/5 | **NEW** | Increases your Attack Power by 100% of your Intellect. |
| **Efficiency** | 4/5 | changed | Reduces the Mana cost of your Shots, Stings, and melee abilities by 12%. |
| **Lone Wolf** | 1/1 | **NEW** | You deal 20% increased damage with all attacks while you do not have an active pet. |

### Survival (31)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Improved Tracking** | 5/5 | **NEW** | While tracking Beasts, Demons, Dragonkin, Elementals, Giants, Humanoids, or Undead, all damage you deal to the tracked creature type is increased by 5%. |
| **Savage Strikes** | 2/2 | changed | Increases the critical strike chance of all your melee abilities by 4%. |
| **Survivalist** | 5/5 | changed | Increases your total Health by 10%. |
| **Surefooted** | 3/3 | changed | Increases your hit chance by 3% and reduces the duration of movement impairing effects on you by 30%. |
| **Predator's Edge** | 5/5 | **NEW** | Increases your melee critical strike damage by 30% and your offhand weapon damage by 50%. |
| **Expose Prey** | 2/2 | **NEW** | Your attacks against targets with Hunter's Mark have a 10% chance to activate your Mongoose Bite for 5 sec. |
| **Resourcefulness** | 2/2 | **NEW** | Reduces the mana cost of your Trap abilities and melee abilities by 60%. In addition, your critical strikes have a 60% chance to allow 50% of your Mana regeneration to continue while casting for 30 sec. |
| **Strider Kick** | 1/1 | **NEW** | A powerful kick that deals 100% melee weapon damage and increases movement speed by 30% for 3 sec. |
| **Lightning Reflexes** | 5/5 | changed | Increases your Agility by 15%. |
| **Lacerating Strikes** | 1/1 | **NEW** | Your Mongoose Bite also causes the target to Bleed for damage over 21 sec equal to 40% of the damage done by Mongoose Bite. |

## Core talents (priority order)

1. **Predator's Edge** — +30% melee critical damage and +50% off-hand weapon damage: the reason to dual-wield; the biggest single multiplier of the build.
2. **Lone Wolf** — +20% on every attack with no pet; a melee hunter fights beside the mob anyway, so the pet's threat matters less than the damage.
3. **Expose Prey** — Attacks against a marked target activate Mongoose Bite (10% chance at 2/2): Mongoose Bite every few seconds instead of only after a dodge, and Lacerating Strikes needs it.
4. **Lacerating Strikes** — Every Mongoose Bite also bleeds for 40% of its damage over 21 s: the 31-point capstone of the melee tree.
5. **Lethal Attacks** — +5% critical strike chance with all attacks, doubled in value by Predator's Edge's crit damage.
6. **Savage Strikes** — +4% crit on Raptor Strike, Mongoose Bite, Counterattack and Strider Kick.
7. **Deadly Aspects** — Under Aspect of the Beast every melee swing has a 10% chance of +30% attack speed for 12 s.
8. **Strider Kick** — 100% weapon damage every 8 s for a trivial mana cost, plus a sprint.
9. **Improved Tracking** — +5% damage against the tracked creature type: every raid boss is a beast, demon, dragon, elemental, giant, humanoid or undead.
10. **Efficiency** — -15% mana on melee abilities and stings: a melee hunter's mana goes to Raptor Strike and Mongoose Bite.
11. **Lightning Reflexes** — +15% Agility: attack power and crit.
12. **Resourcefulness** — -60% mana on melee abilities and regen on crits: a raid melee hunter's mana goes to Raptor Strike and Mongoose Bite.
13. **Careful Aim** — Attack power from Intellect.

## Flex points

| Pts | Default | Alternatives | Why |
|---|---|---|---|
| 5 | Survivalist | Deflection | Survival points on the way to Lacerating Strikes: +10% health against raid damage. Deflection, Deterrence and Counterattack need the boss to attack you, which it does not behind its back. |
| 3 | Surefooted | Survivalist | +3% hit against a level-63 boss. |

## Rank among our builds and the community simulator's

**1 of 2** for `melee-dps` by training-dummy DPS in the community simulator (ElliotWood/Forever 40be98e); full ranking and the other builds' rotations: [raid README](../README.md), [raid rotations](../rotation.md).

| Rank | Build | By | Split | Dummy DPS | vs best | Raid DPS | vs best in a raid | Out of mana on the dummy |
|---|---|---|---|---|---|---|---|---|
| 1 | **[`melee-survival-raid`](melee-survival-raid.md)** | ours: hand draft | 5/15/31 | 325 | +0.0% | 729 | +0.0% | 0 s |
| 2 | [`opt-melee-dps-raid-dps`](opt-melee-dps-raid-dps.md) | ours: optimizer | 5/15/31 | 325 | +0.0% | 729 | +0.0% | 0 s |

## Rotation (community simulator, training dummy)

- **The training dummy:** the simulator's own rotation: no single change (and no pair of changes) beat it on two seeds (`raidsim/apl_opt.py`, 2026-09-28).
- **A fully buffed raid:** the simulator's own rotation: no single change (and no pair of changes) beat it on two seeds (`raidsim/apl_opt.py`, 2026-09-28).

Before the pull: at -3s: cast Hunter's Mark.

| # | Priority (the first line whose condition holds is cast) | [`melee-survival-raid`](melee-survival-raid.md) casts/min |
|---|---|---|
| 1 | use every other cooldown when ready | as ready |
| 2 | cast Mongoose Bite | 9.9 |
| 3 | cast Strider Kick | 7.5 |
| 4 | cast Raptor Strike | 20.0 |

Lines of the simulator's rotation these builds never cast: cast Counterattack (needs the Counterattack talent).

Damage by ability:

| Ability | [`melee-survival-raid`](melee-survival-raid.md) |
|---|---|
| Auto Attack | 48% |
| Raptor Strike | 21% |
| Mongoose Bite | 15% |
| Strider Kick | 12% |
| Dragonbreath Chili | 3% |

## Notes

- Dual wield two fast one-handers; Aspect of the Beast on; Hunter's Mark and Serpent Sting from range on the pull, then Mongoose Bite when active, Strider Kick on cooldown, Raptor Strike on the next swing.
- No pet: Lone Wolf's +20% beats the pet's damage once the hunter melees (the model's raid pet share is 12%, the break-even 16.7%). Beast Mastery's pet talents are absent for that reason.
- 2026-09-27 scenario audit: Deflection 5, Deterrence 1, Counterattack 1, Hawk Eye 1 and Improved Stings 3 -> Survivalist 5, Resourcefulness 2, Careful Aim 5 (Efficiency 5 -> 4). Parry and dodge only matter when the boss attacks you, Hawk Eye extends shots a melee does not fire, and Serpent Sting is one cast per pull.
- The fight lab's melee rotation (hunter module, spec model melee-dps) plays this loop for the leveling comparison; the community simulator has no melee hunter, so this build has no raid-sim DPS yet.

## Open questions (verify in the live game)

- Melee hunter numbers are the scorer's assumptions and the fight lab's rotation, not measurements: the community simulator has no melee hunter rotation, so the raid build has no simulator DPS.
- Expose Prey's proc rate against a marked target (5%/rank per attack assumed) decides how often Mongoose Bite is available; check the actual rate in the beta.
- Whether Aspect of the Beast (+110 melee attack power) and the Deadly Aspects melee haste proc work as the tooltips read.
- Lacerating Strikes: 40% of Mongoose Bite over 21 s; whether the bleed can crit or stack.

## Sources

- <https://warcraftforever.games/talents/hunter>
- <beta client 1.60.1.70009 tooltips (_reference/data/forever-talents/hunter.json)>
- <hunter/raid/optimizer/melee-dps-raid-dps.md>
- <hunter/leveling/optimizer/melee-dps-leveling-st.md>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
