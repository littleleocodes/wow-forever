# Destruction — Incinerate, Succubus out (the simulator's own build) — 18/0/33

*[Warlock](../../../README.md) · [Raids: training dummy, raid and parse](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 18/0/33 (Affliction / Demonology / Destruction) |
| **Role** | DPS — Raid |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70753 (2026-11-03 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

The official wowsims/forever simulator's own Destruction build (its destro build file): 18/0/33 around Incinerate and Conflagrate with Shadow and Flame (Shadowburn: +20% Fire damage for 20 sec and its Soul Shard refunded; Conflagrate: +20% Shadow damage for 20 sec and Immolate kept), Ruin and Agonizing Flames; the Succubus out, Demon Armor, Curse of the Elements and 32 Soul Shards carried in, as the build file ships. Added on 2026-11-20 from the independent audit's step-2 decision (4). The same day showed our warlock entries had carried no Soul Shard into a fight, so Shadowburn could never be cast and every Destruction search valued it at nothing (upstream's package: 800 DPS with none, 881 with its 32, in a full raid).

## Point allocation

### Affliction (18)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Improved Life Tap** | 2/2 | moved | Increases the amount of Mana awarded by your Life Tap spell by 20%. |
| **Suppression** | 5/5 | changed | Improves your chance to hit by 5% and reduces all threat you generate by 20%. |
| **Improved Corruption** | 5/5 | changed | Reduces the casting time of your Corruption spell by 2 sec and increases the damage it deals by 10%. |
| **Improved Bane of Agony** | 2/2 | **NEW** | Increases the damage done by your Bane of Agony by 10%. |
| **Amplify Curse** | 1/1 | changed | Increases the effect of your next Curse of Weakness or Bane of Agony by 50%, or your next Curse of Exhaustion by 20%. Lasts 30 sec. |
| **Pandemic** | 3/3 | **NEW** | Increases the critical strike damage bonus of your Corruption, Bane of Agony, Bane of Doom, Drain Soul, Drain Life, Siphon Life, and Wrack spells by 100%. |

### Demonology (0)

*No points.*

### Destruction (33)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Bane** | 5/5 | changed | Reduces the casting time of your Shadow Bolt, Immolate, and Incinerate spells by 0.5 sec and your Soul Fire spell by 2 sec. |
| **Cataclysm** | 3/3 | changed | Reduces the Mana cost of your Destruction spells by 10%. |
| **Aftermath** | 5/5 | changed | Increases the initial damage of your Immolate spell by 50% and your Conflagrate spell has a 100% chance to Daze the target, reducing the target's movement speed by 50% for 5 sec. |
| **Ruin** | 5/5 | changed | Increases the critical strike damage bonus of your Destruction spells by 100%. |
| **Shadowburn** | 1/1 | changed | Instantly blasts the target for 65 to 73 Shadow damage. If a non-trivial target dies within 8 sec of being hit with Shadowburn, the caster gains a Soul Shard. |
| **Agonizing Flames** | 3/3 | **NEW** | Increases the critical strike chance of your Searing Pain spell by 10% and the damage done by all your Destruction spells by 10%. |
| **Conflagrate** | 1/1 | changed | Ignites a target that is already afflicted by your Immolate spell, dealing 88 to 110 Fire damage and consuming your Immolate effect. |
| **Bane of Havoc** | 1/1 | **NEW** | Afflicts the target for 5 min, causing 15% of all damage done by the Warlock to other targets to also be dealt to the cursed target. Bane of Havoc is limited to 1 target, and only one Bane per Warlock can be active on any one target. |
| **Fire and Brimstone** | 3/3 | **NEW** | Increases the critical strike chance of your Conflagrate spell by 25%. |
| **Shadow and Flame** | 5/5 | **NEW** | Hitting an enemy with Conflagrate increases all Shadow damage you deal by 20% for 20 sec, and hitting an enemy with Shadowburn increases all Fire damage you deal by 20% for 20 sec. In addition, Conflagrate has a 100% chance not to consume Immolate, and Shadowburn has a 100% chance to instantly refund a Soul Shard. |
| **Incinerate** | 1/1 | **NEW** | Deals 99 to 113 Fire damage to your target and an additional 25% damage if the target is afflicted by Immolate. |

## Core talents (priority order)

1. **Shadow and Flame** — Shadowburn gives +20% Fire damage for 20 sec and refunds its Soul Shard; Conflagrate gives +20% Shadow damage for 20 sec and keeps Immolate
2. **Incinerate** — the 31-point filler: +25% damage while Immolate is on the target
3. **Shadowburn** — cast for Shadow and Flame's Fire bonus (needs a Soul Shard in your bags; the talent gives it back)
4. **Conflagrate** — Shadow and Flame's Shadow bonus without losing Immolate
5. **Ruin** — +100% critical strike damage bonus on Destruction spells
6. **Agonizing Flames** — +10% damage on every Destruction spell

## Rank among our builds and the community simulator's

**1 of 2** for `destro-raid` by training-dummy DPS in the community simulator (wowsims/forever 2e6e77d (client 70938)); full ranking and the other builds' rotations: [raid README](../README.md), [raid rotations](../rotation.md).

| Rank | Build | By | Split | Dummy DPS | vs best | Raid DPS | vs best in a raid | Out of mana on the dummy |
|---|---|---|---|---|---|---|---|---|
| 1 | **[`destruction-succubus-raid`](destruction-succubus-raid.md)** | ours: derived (simulator preset) | 18/0/33 | 782 | +0.0% | 882 | +0.0% | 0 s |
| 2 | *Destro* | community simulator | - | 782 | +0.0% | 882 | +0.0% | 0 s |

## Rotation (community simulator, training dummy)

- **The training dummy:** the simulator's own rotation (no rotation search recorded).
- **A fully buffed raid:** the simulator's own rotation: no single change (and no pair of changes) beat it on two seeds (`raidsim/apl_opt.py`, 2026-11-20).

Before the pull: cast Soul Fire; at -1s: petAttack; at -0.1s: cast Immolate (rank 7).

| # | Priority (the first line whose condition holds is cast) | [`destruction-succubus-raid`](destruction-succubus-raid.md) casts/min |
|---|---|---|
| 1 | use every other cooldown when ready | as ready |
| 2 | if not warlockAssignedCurseIsActive and not warlockIsAssignedCurse: castWarlockAssignedCurse | as ready |
| 3 | if warlockAssignedCurseIsActive and not warlockAssignedCurseIsActiveOnAllTargets and number of targets > 1: change target | as ready |
| 4 | if number of targets ≥ 3 and unitDistance > 5 and not unitIsMoving: move to 5 yd | as ready |
| 5 | if time left in the fight > “Doom tick”: cast Bane of Doom | 0.7 |
| 6 | if Bane of Havoc is on the target: change target | as ready |
| 7 | if number of targets = 1 and not Bane of Doom is on the target and (not Bane of Doom is ready or time left in the fight < “Doom tick”) and not Bane of Agony is on the target and time left in the fight > dotBaseDuration: cast Amplify Curse | 0.3 |
| 8 | if number of targets = 1 and not Bane of Doom is on the target and not Bane of Agony is on the target and time left in the fight > dotBaseDuration: cast Bane of Agony | 0.9 |
| 9 | if number of targets = 1 and not Immolate is on the target and time left in the fight > dotBaseDuration: cast Immolate (rank 7) | 4.0 |
| 10 | if number of targets = 1 and not Corruption is on the target and time left in the fight > dotBaseDuration: cast Corruption (rank 6) | 3.2 |
| 11 | if number of targets > 1 and not Bane of Doom is on the target and (not Bane of Doom is ready or time left in the fight < “Doom tick”) and not Bane of Agony is on the target and not Bane of Havoc is on the target and number of targets < 5: cast Amplify Curse | 0.3 |
| 12 | if number of targets > 1 and not Bane of Doom is on the target and not Bane of Agony is on the target and not Bane of Havoc is on the target and number of targets < 5: cast Bane of Agony | 0.9 |
| 13 | if number of targets > 1 and (Bane of Agony is on the target or Bane of Doom is on the target or Bane of Havoc is on the target) and (warlockAssignedCurseIsActive or warlockIsAssignedCurse) and not warlockBaneIsActiveOnAllTargets and number of targets < 5: change target | as ready |
| 14 | if number of targets > 1 and not Immolate is on the target and time left in the fight > dotBaseDuration and not “in 5y range of 3T”: cast Immolate (rank 7) | 4.0 |
| 15 | if number of targets > 1 and Immolate is on the target and not dotIsActiveOnAllTargets and (warlockAssignedCurseIsActive or warlockIsAssignedCurse) and ((Bane of Agony is on the target or Bane of Doom is on the target) or not (number of targets < 5)) and time left in the fight > dotBaseDuration and not “in 5y range of 3T”: change target | as ready |
| 16 | if number of targets > 1 and not Corruption is on the target and time left in the fight > dotBaseDuration and not “in 5y range of 3T”: cast Corruption (rank 6) | 3.2 |
| 17 | if number of targets > 1 and Corruption is on the target and not dotIsActiveOnAllTargets and (warlockAssignedCurseIsActive or warlockIsAssignedCurse) and ((Bane of Agony is on the target or Bane of Doom is on the target) or not (number of targets < 5)) and Immolate is on the target and time left in the fight > dotBaseDuration and not “in 5y range of 3T”: change target | as ready |
| 18 | if number of targets > 1 and (warlockAssignedCurseIsActiveOnAllTargets or warlockIsAssignedCurse) and (warlockBaneIsActiveOnAllTargets or not (number of targets < 5)) and (dotIsActiveOnAllTargets or not (time left in the fight > dotBaseDuration and not “in 5y range of 3T”)) and (dotIsActiveOnAllTargets or not (time left in the fight > dotBaseDuration and not “in 5y range of 3T”)): change target | as ready |
| 19 | if (Immolate is on the target or not Shadow is up): cast Conflagrate | 5.2 |
| 20 | cast Shadowburn | 3.6 |
| 21 | if (“Amount of Dooms left” < 1 and not Bane of Doom is on the target or (Bane of Doom is on the target or “in 5y range of 3T”)) and (time left on Bane of Doom < 15s and Bane of Doom is on the target or not Bane of Doom is on the target): cast Frozen Heart of the Mountain | as ready |
| 22 | if (“Amount of Dooms left” < 1 and not Bane of Doom is on the target or (Bane of Doom is on the target or “in 5y range of 3T”)) and (time left on Bane of Doom < 30s and Bane of Doom is on the target or not Bane of Doom is on the target): cast Major Spellblasting Potion | as ready |
| 23 | if (“Amount of Dooms left” < 1 and not Bane of Doom is on the target or (Bane of Doom is on the target or “in 5y range of 3T”)) and time left on Bane of Doom < 15s and Bane of Doom is on the target and number of targets = 1 and time left on Immolate < cast time of Incinerate: cast Immolate (rank 7) | 4.0 |
| 24 | if (cast time of Incinerate + spellTravelTime) > time left in the fight: cast Searing Pain | 0.2 |
| 25 | if mana % < 35% and time left in the fight > 60s: cast Life Tap | 7.1 |
| 26 | if time left on Immolate < cast time of Incinerate: cast Immolate (rank 7) | 4.0 |
| 27 | cast Incinerate | 11.4 |
| 28 | cast Life Tap | 7.1 |

Lines of the simulator's rotation these builds never cast: cast Bane of Havoc, cast Eureka!, cast Blood Fury, cast Berserking, cast Hellfire, cast Death Coil (its condition never held in these fights).

Damage by ability:

| Ability | [`destruction-succubus-raid`](destruction-succubus-raid.md) |
|---|---|
| Incinerate | 32% |
| Immolate | 14% |
| Corruption | 13% |
| Conflagrate | 12% |
| Bane of Doom | 10% |
| Shadowburn | 7% |
| Bane of Agony | 6% |
| Pet: Auto Attack | 4% |
| Demonic Rune | 1% |
| Pet: Lash of Pain | 1% |

## Notes

- Upstream's package: its rotation (2e6e77d84, trainer ranks), its talents and its options; its own entry (destro-raid, sb-raid's gear and consumables) because each upstream rotation is built for its own build.
- On the raid page only if it ends 0.5% ahead of Destruction's best on both seeds after its tune and search (the audit's decision of 2026-11-19).
- Simulator numbers are the community's model of the game, not in-game measurements.

## Open questions (verify in the live game)

- Bane of Havoc copies damage done to other targets: worth nothing on a single boss (a filler here).

## Sources

- <https://github.com/wowsims/forever/blob/2e6e77d84/ui/specs/warlock/dps/builds/destro.build.json>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
