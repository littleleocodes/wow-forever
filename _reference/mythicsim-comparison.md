# MythicSim's WoW: Forever rankings compared with ours (2026-10-15)

Hand-kept. User request (2026-10-15): "do a look into the website mythicsim and their rankings and listings and everything for WoW:
Forever. Compare to ours and see if we can learn anything from that site or if ours is better." A web review; their ranking, build and
audit pages render by JavaScript and could not be read, so their talent strings, gear lists and rotations are unverified.

## What it is

[mythicsim.com/wow-forever](https://mythicsim.com/wow-forever) (mostly a retail SimulationCraft site): a DPS
[tier list](https://mythicsim.com/wow-forever/tier-list), a trinket board per spec (`/wow-forever/best-trinkets/<spec>`, 117 trinkets),
[race rankings](https://mythicsim.com/wow-forever/races), community builds, a rotation-editor guide, a per-spec audit log, and a Quick Sim /
Best Gear tool fed by its addon (CurseForge "MythicSim - Forever Sim Exporter"). Engine: their fork of ElliotWood/Forever
([sage3648/mythicsim-forever-engine-go](https://github.com/sage3648/mythicsim-forever-engine-go)); its tier-list commit 944a791 is 164
commits ahead of our pin 2ce8265 and 0 behind (upstream through client 70338 plus their patches).

Their method: 10,000 iterations (simmed 2026-10-13); one level-63 boss, 120 ± 15 s; full raid buffs, debuffs and consumables; racials on
(best race per spec); fixed reference gear (dungeon and crafted, no raid items, no trinkets); talents from published guides and Discord (no
optimization); no target creature type; healers not ranked; tanks ranked by damage only.

## Shared specs (full-raid DPS; rank and share of the top: theirs Shockadin 995, ours Beast-Survival 1051)

| Spec | MythicSim | Ours | Builds |
|---|---|---|---|
| Survival | 783, #5, 79% | 1042, #2, 99% | same 5/11/35 |
| Fury | 860, #2, 86% | 917, #5, 87% | same |
| Demonology | 854, #3, 86% | 822, #9, 78% | same |
| Retribution | 810, #4, 81% | 979, #3, 93% | same |
| Arms | 782, #6, 79% | 964, #4, 92% | 39/10/2 vs 37/14/0 |
| Marksmanship | 761 (melee weave), 76% | 893, 85% | 5/31/15 vs 5/41/5 |
| Beast Mastery | 662 (melee weave), 67% | 847, 81% | same |
| Arcane / Frostfire | 739 / 733 | 689 / 675 | same |
| Fire / Frost | 709 / 680 | 685 / 680 | different |
| Shadow / Destruction / Affliction | 710 / 709 / 734 | 696 / 705 / 752 | about the same |
| Enhancement / Feral / Balance | 716 / 734 / 648 | 727 / 694 / 586 | close |
| Combat / Assassination / Subtlety | 642 / 607 / 620 | 735 / 707 / 673 | different |
| Elemental / Smite | 513 / 574 | 515 / 579 | close |

Same broad shape (casters behind melee, Elemental last); casters and warlocks within about ±7%; our physical specs 13-33% higher.

## Why they differ (likely)

1. Gear: our tier list is phase-1 BiS with trinkets; theirs dungeon/crafted without trinkets (a trinket pair is 4-7% on their boards).
   Our pre-BiS numbers close much of it (Survival 840, Arms 824, Retribution 945).
2. Our hunter patches: pets scale with the hunter's gear, 2.0 s pet hit, an Elemental target (+5% Improved Tracking). Their engine gives
   pets nothing from the owner and no creature type: about 20% on Beast Mastery. Their demon scaling matches ours.
3. Windfury Totem: their 2026-10-12 patch procs it from main-hand hits only (the 70291 tooltip: "Each main hand hit has a 20% chance");
   in our pin the trigger comes from spell data (`sim/core/buffs/drivers.go`, `spelldata.ProcTrigger` on 10612): unverified whether the
   off hand procs it. If it does, our dual-wield specs (both top melee hunters, Fury, rogues, Enhancement) are high.
4. Newer engine and their patches: caster-weapon spell power (2026-10-11), Seal of Righteousness weapon coefficient, hard casts reset the
   swing, crit rage without the two-hander factor, Deep Wounds ticks.
5. Fight length (their 120 s favours burst and mana-limited casters; ours 180 s) and racials (theirs on, about 1%).
6. Talents and rotations: ours ML-searched and tuned (the Survival Wing Clip filler, about +10%); theirs guide presets.

## Leads for us (ranked)

1. Windfury Totem's hand rule: test whether off-hand hits proc it in our pin; patch (`raidsim/patches/`) and re-race dual-wield specs.
2. Re-pin to upstream (client 70338): caster-weapon spell power is a likely gap; diff their patch list against `raidsim/patches/README.md`.
3. Adaptive Combat Assistant (item 272437, +20 Expertise, sold by Pix Xizzix): their best physical trinket (+2.67% Survival, +2.06% Arms);
   our db.json lists no source, so `gear_tiers.py` / `gear_opt.py` drop it unless a preset uses it (`gear-opt.json` swapped it out).
4. Ranged hunters weaving melee: they measure +5% Marksmanship, +11% Beast Mastery over shoot-only; we do not model weaving.
5. Features: a per-spec trinket board; race rankings with 95% confidence intervals; a tier list with a trinkets on/off toggle and a
   dungeon-gear view; a public per-spec audit log; Battle Squawk; hybrid tanks (Ret-prot, Holy-prot, Fury-prot).
6. Say on the tier list that pet scaling is the largest single disagreement between the two (their engine denies it).

## Verdict

Ours is stronger at finding the best build (ML search, synergy certificates, tuned rotations with reasons), healers (healer lab), tank
threat and mitigation, leveling (fight lab) and linked gear tiers. Theirs is stronger at simming your own character, trinket and race
choices, engine freshness and showing uncertainty. Their tier list is closer to a fresh level 60 in dungeon gear with guide talents; ours
models an optimized phase-1 raider. Neither is a measurement in the game.
