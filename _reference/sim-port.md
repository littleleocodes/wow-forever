# Port to wowsims/forever (2026-10-18)

User decision 2026-10-18 (audit 2 row 1): the raid pipeline moves from the ElliotWood/Forever fork, deprecated and deleted in the night
of 2026-10-17/18 (API 404; its Pages site: "The official WoW Forever simulator is now live ... use wowsims.com/forever"), to the official
github.com/wowsims/forever. Same Go module name and wowsims layout, a different code base (no shared commits, 26,481 commits since the
2022 TBC copy), refactored deeply: data-driven spells and consumables, one registered rank per spell, a new Stat enum, item armor from
the client tables.

**State**: ported and built; smoke-tested (table below); **no raid number of the project is from the official simulator yet** and the
gear sets must be re-made before any is (see "Open").

## Where things are

- Clone: `~/.wow-forever-tools/wowsims-forever` (sparse: sim, proto, cmd, ui, assets/database, tools), pinned at **09e7398**
  (`09e739807d68a561f01ddb0ba41c2c6a6003d681`, master 2026-10-18 19:55 +0200; spell data and items client 1.60.1.70450; UI proto
  version 2, `.deployedprotoversion`). `raidsim/setup.py` and `cloud_setup.py` point there; `run.py`'s default repo is that folder.
- The fork's clone `~/.wow-forever-tools/forever-repo` (b7083fa) is untouched and still builds with the archived patches
  (`raidsim/patches/elliotwood-b7083fa/`); nothing points at it. It is the only copy of the fork's database and presets left.
- The fork's preset files our entries used (21 rotations and gear sets the official repo lacks) are vendored in
  `raidsim/presets/elliotwood-b7083fa/` and `specs.json` points at them.

## What changed

- **Bench** (`raidsim/foreverbench/main.go`): compiles against the official API. Consumables: specs.json keeps the fork's fields;
  `legacyConsumables` maps them onto the official ConsumesSpec (elixirs and the Zanza/Juju/alcohol buffs to `elixir_ids` /
  `extra_ids`, the fork's imbue enchant ids to item ids, each hand's stone or oil and poison/firestone/spellstone apart, the potion to
  the placeholder of its potion class); `legacyAPL` rewrites the fork's `OtherActionPotion` to that placeholder. Dragonbreath Chili is
  not in the official catalogue (dropped with a note). `officialGear` drops items and enchants the official database lacks and reports
  them (`missing_gear`); the simulator panics on an unknown item otherwise. New `"spells": true` mode lists the spell and aura ids a
  character, its pets and the target register. Tanks get `FullTankIndividualBuffs` (no Salvation, audit 2 row 63).
- **Rotations** (`raidsim/apl_remap.py`, record `raidsim/apl-remap.json`): the official simulator registers one rank per spell (the
  trainer's highest: Frostbolt rank 10 10181, not the rank-11 book 25304, cf. audit 2 row 14), so a line naming another rank found no
  spell and never cast (first smoke run: the Frost mage cast only Fire Blast, 70 DPS). 54 id changes in 23 files: each id the class's
  entries do not register (every build plus an all-talents probe) moved to the registered rank of its chain (the nearest rank below,
  else the lowest registered), Missile Barrage's legacy aura 44404 -> 400589. Downranking lines collapse onto the one rank. Unresolved
  (lines that cannot fire): priest Dark Sacrifice 1277328; hunter Intimidation 19577, Counterattack 20910; warrior Blood Fury 20572,
  Diamond Flask 24427, 29602; druid Tiger's Fury 5217 (removed from the game: plan item 16 done by the official data), 13494, 17056,
  23724. Lava Burst 1238300 and 1326047 are both registered (audit 1 #44 needs no rewrite). The vendored fork presets got the same
  remap (Fire 2948/25306, the rogue's AQ Eviscerate 31016 -> 11300, Backstab 25300 -> 11281). A second pass rewrites conditions the
  official simulator reads differently (`condition_rewrites` in the record): Fire Vulnerability (22959) asked without a source unit
  now on the target (the fork looked there, the official simulator on yourself: Fire's Scorch line was always true); Searing and
  Magma Totem as `totemRemainingTime` by type (the fork tracked totems as dots); Furor's `auraIsKnown` dropped (a passive, no aura);
  plain Aspect casts guarded by "while the aura is down" (the fork refused the recast). `raidsim/apl_validate.py [--all-talents]`
  runs the simulator's own rotation checks on every rotation (records `apl-validate*.json`): with every talent known, 16 lines keep a
  warning, all harmless: Summon Hawk and Ghostly Strike conditions on an aura the official code has not (cast on cooldown, as the
  official presets do) and the warriors' Expose Armor check on the dummy (a raid debuff).
- **Patches** (`raidsim/patches/README.md`): ported: no racials, Champion of the Light 10/20/30% (user decision; the official store
  reads 20/40/60%), pet hit inheritance, the unnormalized pet swing; new: Hunter's Mark rank 3 (+98, audit 2 row 13). Retired (the
  official code does it): Aspect of the Beast and melee Deadly Aspects (`sim/hunter/aspects.go`), Lightning Reflexes (store curve
  2/4/6/8/10), Resourcefulness (proc flags 0x110, crits only), pet scaling (`hunter/pets.go makeStatInheritance`: 10% of the higher
  attack power, max(melee, ranged) crit as post 6 says, 30% armor, 2 health per Stamina, expertise), demon scaling (`warlock/pets.go`:
  17% AP, 10% spell damage, 35% armor, 7.5 health per Stamina, spell hit 1:1, spell crit), hit rules (`core/target.go`: 8% melee
  miss at +3 levels without suppression, 17% spell miss, no 1% floor in `spell_result.go`), rage from damage taken (`core/rage.go`:
  the attacker's rage conversion and the 20-40% assumed armor of the 10-08 notes; `PreMitigationDamage` carries the outcome
  multiplier, so crits and crushing blows count: audit 2 row 69), crit rage (`CritRageBonus` 1.0), Bear Form threat (1.5), the
  downranking penalty (one rank per spell), Raptor Strike's queue, stacked imbues (native), Windfury main hand only
  (`buffs/drivers.go`: `trigger.ProcMask &= ProcMaskMeleeMH`), Grace of Air with Windfury ("stacks with it as of 1.60.1.70425":
  audit 2 row 57), armor fill (armor from the client's item-level tables: 5,884 of 6,151 armor items list armor), druid forms on
  potions (cast requirements from the game files' SpellShapeshift masks; audit 2 row 19, not tested).
- **run.py**: reports record `sim.racials` and `sim.pet_normalize` (audit 2 row 96).

## Smoke test

One page build per class, the same build, rotation (ours, remapped), consumables and gear in both benches: the entry's set with the
items the official database lacks taken out and those slots refilled, where it can be, from the official simulator's own preset for the
spec (items both databases have; Elemental and Shadow have no official preset, so 8 and 10 slots stay empty), 1,000 fights, seed 1, 180 s,
dummy = the training dummy (own buffs), raid = the full raid. Script and records: session scratchpad `port_smoke.py`, `smoke/`. Wall time:
20,000 full-raid fights, 12 threads, best of two, process start included (0.1 s both); other jobs shared the machine.

| Entry (build) | Slots lost / refilled | Last committed, fork, own set: dummy / raid | Fork b7083fa, common set: dummy / raid | Official 09e7398, common set: dummy / raid | Change dummy / raid | Wall, 20,000 raid fights: fork / official |
|---|---|---|---|---|---|---|
| mage frost-raid (frost-arcane-power-raid) | 12/17 / 11 | 565.9 / 643.1 (2ce8265) | 482.2 / 549.4 | 560.7 / 635.3 | +16.3% / +15.6% | 0.49 s / 0.70 s |
| warrior fury-dw-raid (fury-dw-raid) | 6/17 / 6 | 498.4 / 839.2 (2ce8265) | 465.9 / 818.3 | 465.0 / 860.8 | -0.2% / +5.2% | 1.57 s / 1.49 s |
| hunter melee-dps (melee-survival-raid) | 13/17 / 12 | 495.7 / 1019.2 (b7083fa) | 342.0 / 794.4 | 337.1 / 813.0 | -1.4% / +2.3% | 1.11 s / 1.19 s |
| paladin ret-dps (ret-raid-dps) | 6/16 / 6 | 507.0 / 924.8 (b7083fa) | 453.6 / 803.5 | 363.9 / 666.1 | -19.8% / -17.1% | 1.63 s / 1.84 s |
| shaman elemental-dps (elemental-raid-dps) | 8/15 / 0 | 375.5 / 515.1 (2ce8265) | 237.3 / 349.5 | 248.2 / 357.6 | +4.6% / +2.3% | 0.76 s / 0.96 s |
| warlock sb-raid (ds-ruin-raid) | 12/17 / 12 | 633.3 / 716.5 (2ce8265) | 512.8 / 573.8 | 542.7 / 630.0 | +5.8% / +9.8% | 0.67 s / 1.36 s |
| rogue combat-swords-raid (combat-swords-raid) | 14/17 / 14 | 408.9 / 667.3 (2ce8265) | 336.9 / 535.8 | 337.4 / 615.5 | +0.1% / +14.9% | 1.52 s / 1.70 s |
| druid feral-cat-dps (feral-cat-dps) | 7/16 / 6 | 359.9 / 637.7 (b7083fa) | 340.1 / 604.7 | 318.9 / 617.2 | -6.2% / +2.1% | 1.73 s / 2.13 s |
| priest shadow-dps (opt-shadow-dps-raid-dps) | 10/17 / 0 | 593.4 / 698.6 (2ce8265) | 457.2 / 559.9 | 403.5 / 586.9 | -11.7% / +4.8% | 0.56 s / 0.79 s |

Reading it: the last committed column is not comparable with the others (full sets, partly an older fork commit); the common-set columns
isolate the two simulators. Found and fixed on the way (before these numbers): the one-rank remap (Frost mage 70 DPS, Fire Blast only),
totem conditions (Elemental 73 -> 248: Searing Totem recast 58 times a fight, out of mana 118 s of 180), the Aspect of the Beast recast
(melee hunter 166 -> 337: 55 casts, out of mana 100 s), debuff conditions without a target (Fire's Scorch line always true). What is left:
the raid column rises for the melee and physical specs (rogue +15%, warrior +5%): Grace of Air now stacks with Windfury Totem in the
official full raid; Frost +16% and the warlock +6-10% are the official spell and talent data (not traced line by line); Retribution
-17-20% is lower damage per seal and judgement hit with the same casts (Seal of Righteousness proc 116 -> 77 DPS, 20924 75 -> 55):
not traced, check the official paladin code and the 70425 tooltips before the paladin re-run; Shadow -12% and Feral -6% on the dummy
(less on the raid): mana and energy models, not traced.

**Speed**: the official engine is not faster. Per 20,000 fights it took 0.95x to 2.0x the fork's time (median about 1.25x: warlock 2.0x,
Frost 1.4x, Shadow 1.4x, warrior 0.95x). Searches and races will take about a quarter longer.

## Open (in order)

1. **Gear.** 159 items of our 98 gear sets (897 slot uses: Blackhand's Breadth, Band of Accuria, the Molten Core tier sets, Hand of
   Justice, Rune Band of Wizardry, Spellweaver's Turban ...) are not in the official database, which comes from Forever's game files
   (`sim/core/item_effects.go`: "Forever's item set is a subset of TBC's"; Wowhead's Forever database does not list them either; Band of
   Sulfuras and Sulfuras are there). The fork's database had 2,180 items the official one lacks. Every set must be re-made from the
   official database (`gear_opt.py`, `gear_tiers.py`, `tank_gear.py`, then `fill_enchants.py`) before any raid number means anything;
   until then a run reports `missing_gear` and plays with empty slots. Those tools hard-code the fork's Stat enum (`gear_opt.py:335`,
   `gear_tiers.py:226`, `tank_gear.py:59`): the official enum merged melee/spell hit, crit and haste into shared ratings
   (17-19) and renumbered everything after Spirit; read it from the clone's `proto/common.proto`. `fill_armor.py` is retired.
2. Paths to the fork's clone outside raidsim/setup.py and run.py: `raidsim/fill_enchants.py:26`, `raidsim/id_names.py:27,59`,
   `raidsim/fill_armor.py:21`, `raidsim/repin_rehearsal.py`, `heallab/heal_gear.py:86`, `fightlab/spell_gcd.py:20`,
   `fightlab/spell_scaling.py:28` (the fight lab reads the fork's spell store; the official store is
   `sim/core/spelldata/spells_auto_gen.go` in the new clone, same format).
3. The simulator's talent presets: the official presets.ts files have none for hunter, rogue and the three shaman specs, so those
   entries race no "sim preset" rows; `preset_names` of rotation-only entries may name presets that no longer exist.
4. Rotations: every tuned rotation was tuned on the fork; after the re-gear, re-tune (`apl_opt.py`) before races. Downranking lines are
   now duplicates of the top line (harmless; prune at the re-tune).
5. Share links: the official UI's proto version is 2 (`option (current_version_number) = 2;`, which `gear_links.py`'s regex reads),
   the site wowsims.com/forever; `gear_links.py` still builds links for elliotwood.github.io and the bench's `link` mode was not tested.
7. The bench's `statweights` and `link` modes run on the official API (Frost mage, 300 fights); the weights come back under the
   official stat names (`StatHitRating`, `StatCritRating`, ...), which the gear tools in item 1 must read; a link opened in the
   official UI was not tried.
8. The unexplained gaps in the smoke table (Retribution, Frost, warlock, Shadow, Feral) before those classes' raid re-runs.
6. Champion of the Light's live value (audit 2 row 2) and the pet swing rule are our readings against the official simulator's.
