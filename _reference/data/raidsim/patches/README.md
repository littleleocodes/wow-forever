# Local patches to the official simulator

`setup.py` builds the official WoW Forever simulator (github.com/wowsims/forever, since 2026-10-18) unchanged except for the files in
`patches/forever/`, which it copies over the clone before every build (`--rebuild`, `--update`, first setup), and the edits listed in
`patches/forever/edits.json`: insertions after a unique anchor (`after` + `insert`) and replacements of a unique text (`replace` +
`with`). An update (`--update`) resets the patched files to the simulator's version first, so `git pull` stays clean, and applies the
patches again. Until 2026-10-18 the pipeline ran the ElliotWood/Forever fork, which was deprecated and deleted that night; its patches
are archived in `patches/elliotwood-b7083fa/` (README there) and are not applied. The port and what became of each patch:
`_reference/sim-port.md`.

| Patch | Why | Since |
|---|---|---|
| `sim/core/no_racials.go` + the `noRacials()` check at the top of `applyRaceEffects` in `sim/core/racials.go` | Off by default. `WOW_FOREVER_NO_RACIALS=1` skips every racial effect (passives and on-use cooldowns), so specs and classes compare without the preset's race; the race's base stats stay. User preference 2026-10-07: as unbiased as possible. Reports record the switch (`run.py sim_switches`, `sim.racials`). | 2026-10-08 (ported 2026-10-18) |
| `AddStatDependency(Intellect, SpellDamage, 0.10 x rank)` in place of the spell-data parse in `applyChampionOfTheLight` (`sim/paladin/talents_retribution.go`) | Client 70425's tooltip and Blizzard's 16 Oct notes: 10/20/30% of Intellect as spell damage; the official spell store's curve for 1311084 reads 20/40/60%, which a 70450 hotfix may have restored (audit 2 row 2). User decision 2026-10-18: 10/20/30%, flagged for launch. | 2026-10-16 (ported 2026-10-18) |
| `huntersMarkSpell = spelldata.MustFind(14324)` in `sim/core/buffs/debuffs_auto_gen.go` | The client data gives Hunter's Mark rank 3 +98 ranged attack power and rank 4 +71 (both rows in the official store); the raid debuff and the hunter's own mark took rank 4. A hunter can cast rank 3 (audit 2 row 13). | 2026-10-18 |
| `sim/hunter/forever_pet_rule.go` + the `foreverPetNormalize()` guard on the swing normalization in `sim/hunter/pets.go` | The official simulator divides a faster pet's swing damage by its speed gain ("a faster swing deals less a swing, the damage a second unchanged"). Forever does not normalize: the client's Faster Attack passives (1263099-1263114, build 70291) change only the speed, and forum measurements at levels 20 and 30 put a 1.2 s cat 42% and a faster wolf 26-30% ahead of a 2.0 s pet with the same attack power. Nobody has measured it at 60. `WOW_FOREVER_PET_NORMALIZE=1` restores the simulator's rule. | 2026-10-08 (ported 2026-10-18) |
| `sim/core/forever_absent.go` + `rot.foreverAbsent(...)` in place of `return nil` in the aura, dot and spell value constructors (`apl_values_aura.go`: aura active/inactive/remaining/stacks; `apl_values_dot.go`: dot active/remaining; `apl_values_spell.go`: spell ready/can cast) | Upstream returns no value for an aura, dot or spell the character lacks (a talent the build does not hold), and an action whose condition has no value casts always (`apl_action.go`: "Condition could not be resolved and will be treated as always true"). The shaman's 15/24/12 hybrid without Maelstrom Weapon cast Lightning Bolt every GCD in the Enhancement rotation (443 DPS in a full raid; 664 patched); removal runs over-valued every talent a rotation conditions on (Maelstrom Weapon 40% lost when removed against 6.5%, Fingers of Frost 45% against 3.7%). Builds that hold every talent their rotation names are bit-identical (every page build and search winner of hunter, mage, rogue and shaman, 3,000 fights). Absent reads false / 0 / 0 s (aura inactive: true). `WOW_FOREVER_UNKNOWN_AURA_DROP=1` restores upstream's rule; undefined variable references are still dropped (`apl_prune.py`). | 2026-10-26 |

Retired at the port (the official simulator does it, with the evidence in `_reference/sim-port.md`): Aspect of the Beast and the melee
half of Deadly Aspects, Lightning Reflexes 2%, Resourcefulness on ability crits, the hunter pet scaling (10% of the higher attack
power, the higher crit, 30% armor, 2 health per Stamina, expertise), the demon scaling (17% attack power, 10% spell damage, 35% armor,
7.5 health per Stamina, the warlock's spell hit and crit), the hit rules (no 1% suppression against a level-63 target, no spell-miss
floor, 17% spell miss), rage from damage taken (now the attacker's rage conversion with the 20-40% assumed armor, crits and crushing
blows included), crit rage x2.0, Bear Form threat +50%, the downranking penalty (the official simulator registers one rank per spell),
Raptor Strike's queue (a swing replacement, no off-hand hit bonus), the stacked temporary enchants (native: a stone or oil and a
poison/firestone/spellstone per hand), Windfury Totem on main-hand hits only, Grace of Air stacking with Windfury Totem, and the armor
fill (the official database computes every item's armor from the client's item-level tables).

Numbers from a patched spell or mechanic are **our** model of the beta, not the community's: reports name the patch where a build depends
on it.

**Bench configuration, not a patch** (`foreverbench/main.go`): the full raid leaves out the four Atiesh party auras the simulator's
`core.FullPartyBuffs` carries (Naxxramas's legendary, in no announced Forever phase; `"atiesh": true` restores them); tanks get
`core.FullTankIndividualBuffs` (no Blessing of Salvation, audit 2 row 63; until 2026-10-18 tank threat was 30% low in absolute terms);
consumables keep the fork's field names in specs.json and are translated to the official ConsumesSpec, and the fork's
`OtherActionPotion` in rotations to the potion-class placeholder; gear the official database does not have is dropped and reported
(`missing_gear`). Spec options go through `legacySpec` (2026-10-22). The warlock's fork-only `sacrificeSummon` / `pactSacrifice`
become the official `sacrificedDemon`; until then they were dropped without a word, and Demonic Sacrifice entries ran with the Imp out
and no sacrifice. Any other option the official protos lack is reported on stderr (sim-port.md, Open item 8).

Checked 2026-10-22 (sim-port.md, Open items 6 and 8): every patch above applies cleanly to a pristine 09e7398. No smoke-test gap
needed a new patch. At the next re-pin to upstream master, retire the pet hit edit: master inherits hit itself (a20507783, 9ce48b6ab),
and our anchor still matches there, so the edit would count hit twice.

**Retired 2026-10-22 at the re-pin to 30f67f5** (master): the hunter pet hit edit (`stats.PhysicalHitPercent` in the hunter pet's `makeStatInheritance` (`sim/hunter/pets.go`); ported 2026-10-18). Upstream inherits hit itself since a20507783 and 9ce48b6ab ("Hunter pets and demons take hit at the 17:8 ratio"); with both, the build failed on a duplicate index in `makeStatInheritance`.
