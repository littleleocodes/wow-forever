# Port to wowsims/forever (2026-10-18)

User decision 2026-10-18 (audit 2 row 1): the raid pipeline moves from the ElliotWood/Forever fork, deprecated and deleted in the night
of 2026-10-17/18 (API 404; its Pages site: "The official WoW Forever simulator is now live ... use wowsims.com/forever"), to the official
github.com/wowsims/forever. Same Go module name and wowsims layout, a different code base (no shared commits, 26,481 commits since the
2022 TBC copy), refactored deeply: data-driven spells and consumables, one registered rank per spell, a new Stat enum, item armor from
the client tables.

**State**: ported and built; smoke-tested (table below); every gear set re-made from the official database (2026-10-22, "Gear" below);
**no raid number of the project is from the official simulator yet** (no build was raced in the new sets).

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
(melee hunter 166 -> 337: 55 casts, out of mana 100 s), debuff conditions without a target (Fire's Scorch line always true). What is left was
traced on 2026-10-22 (Open, item 8): the harness's remapped rotations and lost weapon oil (Frost +16%, part of Shadow), a bench bug
that dropped the warlock's Demonic Sacrifice option, Grace of Air with Windfury Totem (rogue, warrior raid), and otherwise the fork's
stale or wrong data (Seal of Righteousness, Consecration and judgement coefficients, level-based resistance, caster-weapon spell power,
Dark Sacrifice on every race, Tiger's Fury). No simulator patch was needed; Holy Strike's spell-power share is open.

**Speed**: the official engine is not faster. Per 20,000 fights it took 0.95x to 2.0x the fork's time (median about 1.25x: warlock 2.0x,
Frost 1.4x, Shadow 1.4x, warrior 0.95x). Searches and races will take about a quarter longer.

## Gear (2026-10-22, open items 1 and 7)

Every gear set of the project was made again from the official database. Standard sets (specs.json), tank sets and the damage tier sets
for paladin, shaman, warlock, warrior, druid and hunter were chosen on **09e7398** (the bench of that pin); after the re-pin to
**30f67f5** the mage (2026-10-20 hotfix: Piercing Ice removed, Elemental Precision 3 x 2%) and priest (new `self_buffs`: Prayer of
Fortitude and Prayer of Spirit on shadow-dps and smite-dps, the gap agent's finding) standard groups and tier sets were made again, and
the rogue's (weapon-type fix below). A diff of the two pins' databases (db.json, leftover_db.json, enchants, the Stat enum) found 0
items changed or removed, 0 enchants changed and an unchanged enum, 8 items added (Cloudkeeper Legplates, Idol of the Dream, Wall of the
Dead, Pendulum of Doom, Changuk Smasher, Dusty Mail Boots, Axe of Inevitable Ruin, Rog'mar Trainee Shoulderpads): no other set needed
redoing. Final check: 93 sets (`gear_sets/forever/*.gear.json`, `tiers/`, and the official presets specs.json names), **0 items or
enchants the official database lacks**, no empty slot in head to trinkets; the empty slots left are the off hand behind a two-hander and
the relic slot of the healer sets whose class has no relic with static healing stats (heal_gear.py's rule). fill_enchants.py had nothing
left to fill (the tools fill the templates themselves).

**Tools ported** (`raidsim/gear_opt.py`, `gear_tiers.py`, `tank_gear.py`, `fill_enchants.py`, `heallab/heal_gear.py`):
- Item database: the official clone's `assets/database/db.json` plus `leftover_db.json` (the official loader merges both; 1,186
  common-quality items, none in a pool); `fill_enchants.py` and `heal_gear.py` no longer read the fork's clone.
- Stat enum: read from the clone's `proto/common.proto` (`gear_opt.stat_enum` / `stat_names`; heal_gear by name: Spirit 13, MP5 31,
  one StatCritRating 18 and StatHasteRating 19); the bench's `statweights` names (StatHitRating, StatCritRating ...) key the weights.
  No numbering is written into the tools any more.
- Presets that vet sourceless items and name a class's weapon and ranged types: the official repository's plus every fork gear preset
  (vendored 2026-10-22 under `raidsim/presets/elliotwood-b7083fa/ui/specs/*/*/gear_sets/`, 55 files; the official repo has 27 and none
  for shaman). An official preset vets only when none of its items is above item level 70: its "p1" names do not follow Classic's phases
  (mage `p1Arcane` is Naxxramas gear, Balance `p1` Ahn'Qiraj's Genesis, the hunter `p1` sets hold an item-level-71 neck).
- A current item the database lacks is re-filled by its shape (the fork's record of it in the archived clone, `gear_opt.legacy_item`:
  type, hand, weapon and ranged type), so a missing two-hander stays a two-hander; an empty armor or jewelry slot is filled; an empty or
  missing relic of a relic class (idol, libram, totem) is raced among the class's preset relics (`race_relics`); a rogue's weapons keep
  their weapon type (`SAME_WEAPON_TYPE`: the first pass re-filled the daggers set's missing Perdition's Blade with Greenhammer, a mace);
  enchants the database lacks are dropped (`drop_missing_enchants`; none were).
- Trinkets: the official database lacks most of the class presets' trinkets (the hunter kept one, Adaptive Combat Assistant), so the
  candidates are every trinket of the tier's pool the class may wear (about 50), each raced alone (other slot empty, seed 1), then every
  pair of the best seven (`screen_trinkets`; the race and seed-2 confirmation as before). The per-trinket screen is in the records
  (`trinket_screen`).
- `gear_tiers.py --remake [--classes] [--spec] [--sets] [--fresh]`: every ML record's tier set again, in place, for the record's winner
  of that set (bis and prebis: the bis-dummy winner; the "-raid" sets: the bis-raid winner); talents the official trees lack are left out
  of the build the gear is chosen for (`talents_left_out`: Wake of Fire for mage Arcane/Fire/Frostfire, Shadow Affinity for Shadow, Call
  of Thunder and Improved Fire Nova for the shaman, Malediction for Affliction); the record's gear key gets `replaced` (slot, old, new)
  and `remade`. Resume: a set already remade is skipped whatever the commit (a re-pin alone does not redo everything); `--fresh` or
  `--sets` select what to redo.
- tank_gear.py: the tank-value reference is measured again on the current simulator (deep_tank's reference build in the entry's standard
  set, 20,000 fights, seed 77; the fork's numbers stay as `reference_fork`): warrior 1147.8 threat / 326.6 damage taken per second (fork
  677.5 / 672.9), paladin 780.1 / 366.8 (472.0 / 566.1), bear 2859.0 / 360.5 (1223.7 / 634.9). The `--armor` sensitivity is obsolete
  (official armor from the client tables); its six `*-classic-armor` sets were removed.
- Rules kept unchanged: the pools (phase-1 sources, `PHASE1_RAID_MADE`, `RAID_QUEST`, `PHASE1_QUEST`, `LATER_PREFIXES`, `EVENT_NPCS`,
  `WORLD_BOSSES`, `SUSPECT_ITEMS`, `VENDOR_ITEMS`), the greedy variants, the races and the seed-2 confirmation.

**Item-id lists against the official database**: `SUSPECT_ITEMS` (Death Speaker Scepter, Searing Golden Blade, Windweaver Staff, the
Soran'ruk / Dar'Orahil / Noh'Orahil staves, Witching Stave, Stormcloth Vest) are all present with the **same** values as the fork's
(+68 healing on the scepter, +39 Fire on the blade ...): the official database comes from Forever's game files, so these may be Forever's
real numbers rather than errors; they stay excluded (rule kept), to be checked in game. `VENDOR_ITEMS` (Adaptive Combat Assistant):
present. `PHASE1_RAID_MADE`: all present but Lavashard Axe (absent from the fork too). `RAID_QUEST`, `PHASE1_QUEST`: present. Of the
Molten Core and Onyxia loot the official database keeps only 10 items with a raid source (Earthshaker, The Eye of Divinity, Choker of the
Fire Lord, Essence of the Pure Flame, Talisman of Ephemeral Power, Quick Strike Ring, Heavy Dark Iron Ring, Band of Sulfuras, Cauterizing
Band, Ring of Spell Power) plus the Molten Core crafts; no tier-set piece (Netherwind, Felheart, Giantstalker, Nightslayer, Earthfury,
Lawbringer, Might, Arcanist, Cenarion, Prophecy), no Hand of Justice, Blackhand's Breadth, Band of Accuria, Royal Seal of Eldre'Thalas,
Briarwood Reed, Eye of the Beast, Rune Band of Wizardry, Spellweaver's Turban, Azuresong Mageblade or Staff of Dominance. The world bosses
have no source entries at all.

**What replaced them** (typical picks; per slot in the records): casters: Living Crown / Felcloth Hood / Dreadmist Mask, Mantle of the
Timbermaw, Arcanoweave Cloak, Robe of the Archmage / Earthpower Vest / Robe of the Void, Gloves of Spell Mastery, Belt of the Archmage,
Flarecore Leggings, Ring of Spell Power, Sageblade + Therazane's Touch or Ironbark Staff, trinkets Talisman of Ephemeral Power + Weakness
Analyzer (Serenity Field, Alchemist's Stone for some); melee: Darkmantle and Theramore pieces, Dawn Armor, Forest Stalker's Bracers,
Chromatic Gauntlets, Belt of Preserved Heads (vetted by the official warrior pre-BiS preset), Outrider's Chain Leggings, Signet Ring of the
Bronze Dragonflight, Don Julio's Band, Band of the Better Half, Fist of Cenarius (two-hand), Premier High Warlord's PvP weapons,
Blackguard, trinkets Adaptive Combat Assistant with Rune of the Guard Captain, Molten Heart of the Mountain or Everlook Pathcarver;
Hand of Justice's slot went to Adaptive Combat Assistant or Rune of the Guard Captain. Item levels fell 1-3 (65-67 -> 63-64).

**Tank standard sets**: specs.json now names the official presets (warrior `ui/specs/warrior/protection/gear_sets/prebis.gear.json`, the
"Pre-BiS (Defense Cap)" set; bear `ui/specs/druid/feralbear/gear_sets/default.gear.json`, which has no idol); the fork's launch presets
lost 6 and 5 items. The paladin keeps the official `default` preset (complete).

### Standard sets (gear_opt.py; record raidsim/gear-opt.json)

Seed 1 3,000 fights per set and entry, seed 2 12,000; "current" competes only when every item is in the database and the pool.

| Standard set (entries) | Item level | Seed 2 (12,000 fights) | Trinkets | Slots changed (of them missing) |
|---|---|---|---|---|
| druid-balance-p1.p1opt.gear.json (balance-dps) | 65.0 -> 63.5 | all-slots +3.1% | Serenity Field, Talisman of Ephemeral Power | 11 (8) |
| druid-feralcat-launch.p1opt.gear.json (feral-cat-dps) | 63.3 -> 63.8 | keep-sets-and-effects +0.0% | Adaptive Combat Assistant, Molten Heart of the Mountain | 9 (7) |
| hunter-dps-p1.p1opt.gear.json (mm-raid, mm-lonewolf-raid, bm-raid) | 66.5 -> 64.2 | all-slots +0.0% | Rune of the Guard Captain, Everlook Delivery Bot | 10 (8) |
| hunter-project-hunter_melee_p1.p1opt.gear.json (melee-dps) | 65.5 -> 64.7 | all-slots +0.3% | Adaptive Combat Assistant, Molten Heart of the Mountain | 15 (13) |
| mage-dps-p1.p1opt.gear.json (frost-raid, fire-raid, arcane-dps, frostfire-raid) | 63.5 -> 63.5 | current kept | Alchemist's Stone, Talisman of Ephemeral Power | 0 (0) |
| paladin-retribution-default.p1opt.gear.json (ret-dps) | 64.5 -> 63.2 | keep-sets-and-effects +1.4% | Talisman of Ephemeral Power, Weakness Analyzer | 12 (6) |
| priest-dps-p0.p1opt.gear.json (shadow-dps, smite-dps) | 67.0 -> 64.2 | all-slots +0.3% | Talisman of Ephemeral Power, Weakness Analyzer | 12 (10) |
| rogue-dps-combat_sinister_strike_p1_bis.p1opt.gear.json (combat-swords-raid, subtlety-raid) | 65.7 -> 63.6 | all-slots +0.9% | Adaptive Combat Assistant, Rune of the Guard Captain | 15 (14) |
| shaman-elemental-phase_1.p1opt.gear.json (elemental-dps, stormcaller-dps) | 61.6 -> 65.4 | keep-sets-and-effects +0.0% | Talisman of Ephemeral Power, Weakness Analyzer | 11 (8) |
| shaman-enhancement-phase_1.p1opt.gear.json (enhancement-dps) | 62.9 -> 62.8 | keep-sets-and-effects +1.9% | Adaptive Combat Assistant, Talisman of Ephemeral Power | 13 (8) |
| warlock-dps-mc.p1opt.gear.json (affliction-raid, fire-destro-raid, sb-raid, demonology-raid, incinerate-raid) | 66.4 -> 63.9 | keep-sets-and-effects +0.0% | Talisman of Ephemeral Power, Weakness Analyzer | 12 (12) |
| warrior-dps-p1_arms.p1opt.gear.json (arms-2h-raid, arms-battle-raid) | 63.1 -> 63.9 | keep-sets-and-effects +0.1% | Adaptive Combat Assistant, Everlook Pathcarver | 12 (8) |
| warrior-dps-p1_fury.p1opt.gear.json (fury-dw-raid) | 62.8 -> 63.9 | keep-sets-and-effects +0.0% | Adaptive Combat Assistant, Rune of the Guard Captain | 10 (6) |
| combat_backstab_p1_bis.gear.json (combat-daggers-raid, assassination-raid) | 60.4 -> 63.8 | all-slots +1.3% | Adaptive Combat Assistant, Molten Heart of the Mountain | 15 (10) |

### Tier sets (gear_tiers.py --remake; records: the `gear` key of raidsim/ml/<class>-<spec>.json)

The commit is the pin the set was chosen on. For the mage, priest and rogue sets made twice, "slots changed" counts against the first
remake (the fork-era replacements are in git history); "-" = the leader was the reference (no seed-2 race).

| Tier set (entry) | Item level | Chosen, seed 2 | Trinkets | Slots changed (missing before) |
|---|---|---|---|---|
| druid-balance-bis.gear.json (balance-dps, 09e7398) | 65.0 | all-slots +0.6% vs current | Talisman of Ephemeral Power, Weakness Analyzer | 11 (8) |
| druid-balance-prebis.gear.json (balance-dps, 09e7398) | 63.2 | keep-sets-and-effects +0.0% vs all-slots | Weakness Analyzer, Jewel of the Guard Captain | 11 (7) |
| druid-feral-combat-bis.gear.json (feral-cat-dps, 09e7398) | 63.5 | all-slots +0.0% vs current | Adaptive Combat Assistant, Rune of the Guard Captain | 10 (8) |
| druid-feral-combat-prebis.gear.json (feral-cat-dps, 09e7398) | 63.9 | keep-sets-and-effects +0.0% vs all-slots | Adaptive Combat Assistant, Molten Heart of the Mountain | 9 (7) |
| hunter-beast-mastery-bis.gear.json (bm-raid, 09e7398) | 65.2 | all-slots +0.3% vs keep-sets-and-effects | Shard of the Splithooves, Adaptive Combat Assistant | 11 (9) |
| hunter-beast-mastery-prebis.gear.json (bm-raid, 09e7398) | 62.9 | keep-sets-and-effects +0.1% vs all-slots | Rune of the Guard Captain, Adaptive Combat Assistant | 10 (6) |
| hunter-hybrid-beast-mastery-marksmanship-bis.gear.json (bm-raid, 09e7398) | 63.8 | keep-sets-and-effects +0.1% vs all-slots | Rune of the Guard Captain, Everlook Delivery Bot | 11 (10) |
| hunter-hybrid-beast-mastery-marksmanship-prebis.gear.json (bm-raid, 09e7398) | 62.4 | keep-sets-and-effects +0.0% vs all-slots | Rune of the Guard Captain, Everlook Delivery Bot | 11 (6) |
| hunter-hybrid-beast-mastery-survival-bis.gear.json (melee-dps, 09e7398) | 64.6 | all-slots +0.1% vs keep-sets-and-effects | Adaptive Combat Assistant, Rune of the Guard Captain | 15 (13) |
| hunter-hybrid-beast-mastery-survival-prebis.gear.json (melee-dps, 09e7398) | 63.9 | keep-sets-and-effects +0.1% vs all-slots | Adaptive Combat Assistant, Molten Heart of the Mountain | 7 (4) |
| hunter-marksmanship-bis.gear.json (mm-raid, 09e7398) | 64.8 | keep-sets-and-effects +0.0% vs all-slots | Adaptive Combat Assistant, Jewel of the Guard Captain | 11 (9) |
| hunter-marksmanship-bis-raid.gear.json (mm-lonewolf-raid, 09e7398) | 64.6 | keep-sets-and-effects +0.0% vs all-slots | Shard of the Splithooves, Enriched Seal | 13 (11) |
| hunter-marksmanship-prebis.gear.json (mm-raid, 09e7398) | 62.8 | keep-sets-and-effects +0.0% vs all-slots | Everlook Delivery Bot, Shard of the Splithooves | 9 (6) |
| hunter-marksmanship-prebis-raid.gear.json (mm-lonewolf-raid, 09e7398) | 62.8 | keep-sets-and-effects +0.0% vs all-slots | Rune of the Guard Captain, Everlook Delivery Bot | 12 (6) |
| hunter-survival-bis.gear.json (melee-dps, 09e7398) | 64.6 | all-slots +0.1% vs keep-sets-and-effects | Adaptive Combat Assistant, Rune of the Guard Captain | 15 (13) |
| hunter-survival-prebis.gear.json (melee-dps, 09e7398) | 63.9 | keep-sets-and-effects +0.1% vs all-slots | Adaptive Combat Assistant, Molten Heart of the Mountain | 7 (4) |
| mage-arcane-bis.gear.json (arcane-dps, 30f67f5) | 63.3 | keep-sets-and-effects +1.3% vs current | Serenity Field, Alchemist's Stone | 0 (0) |
| mage-arcane-prebis.gear.json (arcane-dps, 30f67f5) | 62.0 | - | Serenity Field, Alchemist's Stone | 0 (0) |
| mage-fire-bis.gear.json (fire-raid, 30f67f5) | 64.4 | all-slots +5.4% vs current | Talisman of Ephemeral Power, Weakness Analyzer | 0 (0) |
| mage-fire-prebis.gear.json (fire-raid, 30f67f5) | 62.7 | previous +0.0% vs all-slots | Weakness Analyzer, Alchemist's Stone | 0 (0) |
| mage-frost-bis.gear.json (frost-raid, 30f67f5) | 64.4 | keep-sets-and-effects +1.4% vs current | Talisman of Ephemeral Power, Weakness Analyzer | 11 (10) |
| mage-frost-prebis.gear.json (frost-raid, 30f67f5) | 62.5 | all-slots +0.3% vs keep-sets-and-effects | Weakness Analyzer, Frozen Heart of the Mountain | 14 (13) |
| mage-hybrid-arcane-frost-bis.gear.json (frost-raid, 30f67f5) | 64.4 | keep-sets-and-effects +1.2% vs current | Talisman of Ephemeral Power, Weakness Analyzer | 11 (10) |
| mage-hybrid-arcane-frost-prebis.gear.json (frost-raid, 30f67f5) | 63.2 | keep-sets-and-effects +0.3% vs all-slots | Weakness Analyzer, Frozen Heart of the Mountain | 14 (13) |
| mage-hybrid-fire-frost-bis.gear.json (frostfire-raid, 30f67f5) | 62.5 | all-slots +4.0% vs current | Alchemist's Stone, Talisman of Ephemeral Power | 14 (13) |
| mage-hybrid-fire-frost-prebis.gear.json (frostfire-raid, 30f67f5) | 61.6 | keep-sets-and-effects +0.0% vs all-slots | Alchemist's Stone, Weakness Analyzer | 14 (10) |
| paladin-retribution-bis.gear.json (ret-dps, 09e7398) | 64.7 | all-slots +12.4% vs current | Talisman of Ephemeral Power, Weakness Analyzer | 11 (6) |
| paladin-retribution-prebis.gear.json (ret-dps, 09e7398) | 62.8 | keep-sets-and-effects +2.8% vs all-slots | Weakness Analyzer, Shard of the Splithooves | 10 (4) |
| priest-hybrid-discipline-holy-bis.gear.json (smite-dps, 30f67f5) | 65.4 | all-slots +10.3% vs current | Talisman of Ephemeral Power, Weakness Analyzer | 12 (9) |
| priest-hybrid-discipline-holy-prebis.gear.json (smite-dps, 30f67f5) | 63.0 | keep-sets-and-effects +0.3% vs all-slots | Weakness Analyzer, Alchemist's Stone | 13 (10) |
| priest-shadow-bis.gear.json (shadow-dps, 30f67f5) | 64.2 | - | Weakness Analyzer, Talisman of Ephemeral Power | 12 (10) |
| priest-shadow-prebis.gear.json (shadow-dps, 30f67f5) | 62.2 | all-slots +0.9% vs keep-sets-and-effects | Weakness Analyzer, Jewel of the Guard Captain | 14 (12) |
| rogue-assassination-bis.gear.json (assassination-raid, 30f67f5) | 64.0 | previous +1.6% vs current | Adaptive Combat Assistant, Rune of the Guard Captain | 0 (0) |
| rogue-assassination-prebis.gear.json (assassination-raid, 30f67f5) | 63.3 | - | Adaptive Combat Assistant, Rune of the Guard Captain | 0 (0) |
| rogue-combat-bis.gear.json (combat-daggers-raid, 30f67f5) | 63.8 | all-slots +0.2% vs current | Adaptive Combat Assistant, Rune of the Guard Captain | 6 (0) |
| rogue-combat-prebis.gear.json (combat-daggers-raid, 30f67f5) | 63.7 | previous+trinkets +0.2% vs previous | Adaptive Combat Assistant, Rune of the Guard Captain | 2 (0) |
| rogue-hybrid-assassination-combat-bis.gear.json (assassination-raid, 30f67f5) | 64.0 | previous +1.5% vs current | Adaptive Combat Assistant, Rune of the Guard Captain | 0 (0) |
| rogue-hybrid-assassination-combat-prebis.gear.json (assassination-raid, 30f67f5) | 63.3 | - | Adaptive Combat Assistant, Rune of the Guard Captain | 0 (0) |
| rogue-subtlety-bis.gear.json (subtlety-raid, 30f67f5) | 63.6 | previous +2.2% vs current | Adaptive Combat Assistant, Rune of the Guard Captain | 0 (0) |
| rogue-subtlety-prebis.gear.json (subtlety-raid, 30f67f5) | 63.2 | - | Adaptive Combat Assistant, Rune of the Guard Captain | 0 (0) |
| shaman-elemental-bis.gear.json (elemental-dps, 09e7398) | 65.4 | all-slots +0.9% vs current | Talisman of Ephemeral Power, Weakness Analyzer | 10 (8) |
| shaman-elemental-prebis.gear.json (elemental-dps, 09e7398) | 63.3 | keep-sets-and-effects +0.0% vs all-slots | Weakness Analyzer, Alchemist's Stone | 10 (6) |
| shaman-enhancement-bis.gear.json (enhancement-dps, 09e7398) | 62.8 | - | Adaptive Combat Assistant, Talisman of Ephemeral Power | 13 (9) |
| shaman-enhancement-prebis.gear.json (enhancement-dps, 09e7398) | 62.4 | keep-sets-and-effects +3.3% vs all-slots | Adaptive Combat Assistant, Jewel of the Guard Captain | 13 (6) |
| shaman-hybrid-elemental-enhancement-bis.gear.json (elemental-dps, 09e7398) | 65.3 | keep-sets-and-effects +0.1% vs current | Talisman of Ephemeral Power, Weakness Analyzer | 11 (7) |
| shaman-hybrid-elemental-enhancement-prebis.gear.json (elemental-dps, 09e7398) | 63.4 | keep-sets-and-effects +0.0% vs all-slots | Weakness Analyzer, Jewel of the Guard Captain | 12 (7) |
| shaman-hybrid-elemental-enhancement-bis-raid.gear.json (enhancement-dps, 09e7398) | 62.8 | - | Adaptive Combat Assistant, Talisman of Ephemeral Power | 13 (9) |
| shaman-hybrid-elemental-enhancement-prebis-raid.gear.json (enhancement-dps, 09e7398) | 61.7 | keep-sets-and-effects +0.3% vs all-slots | Adaptive Combat Assistant, Jewel of the Guard Captain | 10 (6) |
| warlock-affliction-bis.gear.json (affliction-raid, 09e7398) | 63.9 | - | Talisman of Ephemeral Power, Weakness Analyzer | 12 (11) |
| warlock-affliction-prebis.gear.json (affliction-raid, 09e7398) | 62.4 | keep-sets-and-effects +0.0% vs all-slots | Weakness Analyzer, Jewel of the Guard Captain | 13 (11) |
| warlock-demonology-bis.gear.json (demonology-raid, 09e7398) | 63.9 | all-slots +0.1% vs current | Weakness Analyzer, Talisman of Ephemeral Power | 12 (11) |
| warlock-demonology-prebis.gear.json (demonology-raid, 09e7398) | 62.4 | keep-sets-and-effects +0.0% vs all-slots | Weakness Analyzer, Jewel of the Guard Captain | 14 (14) |
| warlock-destruction-bis.gear.json (sb-raid, 09e7398) | 64.2 | all-slots +0.2% vs current | Talisman of Ephemeral Power, Weakness Analyzer | 12 (11) |
| warlock-destruction-prebis.gear.json (sb-raid, 09e7398) | 62.4 | all-slots +0.1% vs keep-sets-and-effects | Weakness Analyzer, Jewel of the Guard Captain | 14 (13) |
| warlock-hybrid-affliction-destruction-bis.gear.json (sb-raid, 09e7398) | 63.9 | - | Talisman of Ephemeral Power, Weakness Analyzer | 11 (10) |
| warlock-hybrid-affliction-destruction-prebis.gear.json (sb-raid, 09e7398) | 62.4 | keep-sets-and-effects +0.0% vs all-slots | Weakness Analyzer, Jewel of the Guard Captain | 13 (11) |
| warrior-arms-bis.gear.json (arms-battle-raid, 09e7398) | 62.6 | keep-sets-and-effects +0.9% vs all-slots | Everlook Pathcarver, Jewel of the Guard Captain | 11 (9) |
| warrior-arms-prebis.gear.json (arms-battle-raid, 09e7398) | 62.3 | keep-sets-and-effects +1.3% vs all-slots | Everlook Pathcarver, Rune of the Guard Captain | 10 (6) |
| warrior-fury-bis.gear.json (fury-dw-raid, 09e7398) | 62.9 | keep-sets-and-effects +0.4% vs all-slots | Adaptive Combat Assistant, Rune of the Guard Captain | 9 (5) |
| warrior-fury-prebis.gear.json (fury-dw-raid, 09e7398) | 63.0 | keep-sets-and-effects +0.0% vs all-slots | Adaptive Combat Assistant, Rune of the Guard Captain | 10 (6) |

### Tanks (tank_gear.py, 09e7398; record raidsim/tank-gear.json)

Tank value against the reference above (1.000 = deep_tank's hand draft in the standard set), 20,000 fights, seed 3:

| Tank (page pick) | Standard set | Pre-BiS | BiS |
|---|---|---|---|
| warrior (protection-ml-tank) | 1.015 | 1.132 (+11.5%; threat +16.6%, damage taken -5.8%), item level 63.7 | 1.134 (+11.7%; +13.6%, -8.8%), 63.7 |
| paladin (protection-ml-tank) | 1.079 | 1.272 (+17.9%; +5.8%, -22.6%), 62.8 | 1.274 (+18.0%; +2.7%, -24.5%), 63.2 |
| druid bear (feral-bear-tank) | 1.000 | 1.141 (+14.1%; +21.9%, -5.8%), 63.5 | 1.183 (+18.3%; +25.7%, -9.8%), 64.3 |

The bear's idol race read the same for all three preset idols (Idol of the Moon, Swarming Idol, Howling Idol: no effect on a bear in the
simulator), so the first, Idol of the Moon, stands.

### Healers (heal_gear.py; healer lab, no simulator; record heallab/heal-gear.json)

All five healer specs re-made from the official database (the 2026-10-15 sets held 5-10 fork-only items each: Amulet of the Redeemed,
Hands of the Exalted Herald, the Prophecy and Transcendence pieces, Staff of Dominance ...). Capacity against the lab's assumed gear
(fresh seeds, paired; the healer lab's model, not a measurement):

| Spec (raid pick) | Pre-BiS | BiS |
|---|---|---|
| priest Holy (holy-raid-healer) | x0.984, item level 60.4 | x0.989, 60.8 |
| priest Discipline (discipline-ml-heal) | x0.976, 60.1 | x0.990, 61.6 |
| paladin Holy (holy-ml-heal) | x1.021, 62.3 | x1.058, 64.4 |
| druid Restoration (restoration-ml-heal) | x1.002, 59.1 | x1.020, 62.8 |
| shaman Restoration (resto-raid-healer) | x1.003, 60.6 | x1.034, 63.5 |

Removed (orphans holding fork-only items, git history keeps them): `gear_sets/forever/hunter_melee_p1.gear.json` (the melee hunter's raw
input, replaced by its p1opt set since 2026-09-30), `tiers/hunter-hybrid-beast-mastery-marksmanship-{bis,prebis}-raid.gear.json` (named
only by `raidsim/ml/prev/`), the six `*-classic-armor` tank sets.

Not done here (other agents or later steps): no build was raced in the new sets, no rotation re-tuned; gear_links.py and the pages
still show what their last regen wrote. Idol of the Dream (new on 30f67f5, a sourced item-level-60 idol) is in no preset, so the relic
races never tried it.

## Open (in order)

1. ~~Gear.~~ Done 2026-10-22 (section "Gear"): every set re-made from the official database, 0 missing items or enchants; the tools
   read the Stat enum from the proto. Left: race the builds in the new sets before any raid number is quoted.
2. Paths to the fork's clone outside raidsim/setup.py and run.py (fill_enchants.py and heal_gear.py ported 2026-10-22; gear_opt.py reads
   the archived fork database only for the shape of a missing item, `legacy_item`): `raidsim/id_names.py:27,59`,
   `raidsim/fill_armor.py:21`, `raidsim/repin_rehearsal.py`, `fightlab/spell_gcd.py:20`,
   `fightlab/spell_scaling.py:28` (the fight lab reads the fork's spell store; the official store is
   `sim/core/spelldata/spells_auto_gen.go` in the new clone, same format).
3. The simulator's talent presets: the official presets.ts files have none for hunter, rogue and the three shaman specs, so those
   entries race no "sim preset" rows; `preset_names` of rotation-only entries may name presets that no longer exist.
4. Rotations: every tuned rotation was tuned on the fork; after the re-gear, re-tune (`apl_opt.py`) before races. Downranking lines are
   now duplicates of the top line (harmless; prune at the re-tune).
5. Share links: the official UI's proto version is 2 (`option (current_version_number) = 2;`, which `gear_links.py`'s regex reads),
   the site wowsims.com/forever; `gear_links.py` still builds links for elliotwood.github.io and the bench's `link` mode was not tested.
7. The bench's `statweights` and `link` modes run on the official API; the gear tools read the weights under the official stat names
   (`StatHitRating`, `StatCritRating`, ...) since 2026-10-22 (done). A link opened in the official UI was not tried.
8. **Smoke-table gaps, traced 2026-10-22** (diagnostic benches of both simulators with a final-stats and mana/energy-ledger mode,
   per-action damage per hit, talent removal deltas in both; 1,000-1,500 fights, seed 1; scratchpad `wfdiag/`). No gap needed a
   simulator patch. Two came from the smoke harness, one from the bench, the rest are the fork being wrong: its pin b7083fa carries the
   70374 spell store (audit 1 #43), and some of its rules were never Forever's.
   - **Harness**: the fork ran our *remapped* rotations. Missile Barrage's aura is 44404 in the fork and 400589 in the remap, so the
     fork never cast Arcane Missiles; the rogue's AQ Eviscerate 31016 was remapped to 11300. With its own pre-remap rotations the fork
     gives Frost 586.0 / 664.4 (official 560.7 / 635.3) and combat rogue 358.6 / 596.4 (official 337.4 / 615.5). Shadow's common set
     lost its weapon, and the fork put Brilliant Wizard Oil on the empty hand (+36 spell power). Dragonbreath Chili is not in the
     official catalogue at 09e7398: Retribution lost 16.3 DPS on the dummy, combat rogue 9.5 and Feral 2.6. Upstream added the chili
     on 2026-10-19 (cfdf4944b).
   - **Bench, fixed**: the bench reads the spec fragment with DiscardUnknown, so the fork-only warlock options `sacrificeSummon` /
     `pactSacrifice` were dropped without a word. Every Demonic Sacrifice entry ran with no sacrifice and the Imp out (the smoke run's
     Firebolt rows). `foreverbench/main.go legacySpec` now maps them onto the official `sacrificedDemon` and prints any other field the
     protos do not know (the Enhancement entry's `imbueOh` and `syncType`: its sets hold no off-hand). Warlock sb-raid: 542.7 -> 591.0
     on the dummy, 630.0 -> 664.2 in the raid; the other smoke rows are bit-identical. This is in `foreverbench-next.exe`, not swapped in.
   - **Retribution -17-20%: the official simulator is right.** The "20924 75 -> 55" in the table is Consecration rank 5, not the
     judgement. Seal of Righteousness proc 116.3 -> 76.6 DPS (313.9 -> 217.4 a hit): the official spell-power coefficient is 0.12
     with a two-hander and 0.1 with a one-hander, outside the weapon-speed term. That is the 70425 seal tooltip's description variable
     ($2h = 0.12 x SPH), and the official commits 49f94c932 and b4c8a43f2 measured it on 70425 at level 30. The fork used 0.185 x 1.2
     = 0.222 from pre-70425 logs. Consecration 75.1 -> 54.5: the bonus tick's coefficient is 0.042, which is the 70425 tooltip's
     "4.2% of spell power (per tick)"; the fork read 0.095 from the stale store. Judgement of Righteousness 61.2 -> 58.9: 0.429 is
     the tooltip's 42.9%, and the fork read 0.5.
     **Unknown, Holy Strike 54.9 -> 43.4.** Its 0.429 spell-power coefficient goes through the 50% weapon percent in the official
     code (0.21 a point) and in full in the fork. The 70425 tooltip ("50% weapon damage plus an additional 40 to 53") states no
     spell-power share. A Holy Strike hit logged at two spell-power values settles it.
   - **Frost +16%: harness (above).** With the fork's own rotation the official simulator is 4.3% lower. The cause is Missile
     Barrage: two ranks of 10/20% for Frostbolt in the 70425 data (official), one rank of 20% in the fork. The smoke build had 1
     point; at 2 points the official simulator gives 591.4 against the fork's 586.0. The page build already takes 2 (d3bfea75).
   - **Warlock +6-10% (+15/16% once the sacrifice works): the official simulator is right.** (a) Clever Expeditionary's Spellblade
     (271928) carries +72 spell power in the official database: Forever's caster-weapon rule, with reduced weapon damage and spell
     power added. The fork's database lists none. (b) The official simulator has no level-based resistance against the level-63
     target (ed4b4e93e: "Forever's combat logs show no partial resist that comes from the target's level", logs of mobs 1-9 levels
     above the caster at levels 20-31). The fork took Classic's 2% a level, 6% against a boss. Naked and talentless, Shadow Bolt does
     373.6 -> 393.5 a hit against level 63 and 402.4 -> 403.8 against level 60. This lifts every caster about 5% on the bench's
     target; a level-60 log against a raid boss would confirm it. The 15 talents' removal values agree within 0.8 points in both
     simulators.
   - **Shadow -12% dummy: the official simulator is right, plus a dummy-setting gap.** (a) Dark Sacrifice (1,766 mana a fight in the
     fork's ledger) is the Undead racial in the official code. The smoke character is a Troll; the fork gave it to every race.
     (b) The fork's priest code added Prayer of Fortitude, Spirit and Shadow Protection to the dummy setting (`AddRaidBuffs`); the
     official priest code adds none. That costs 70 Stamina and 40 Spirit, about 1.2% here. Fix it in data: `"self_buffs":
     {"prayer_of_fortitude": true, "prayer_of_spirit": true}` on the priest's shadow-dps and smite-dps entries. specs.json was left
     alone while the gear search writes it. (c) The common set's lost oil (harness). With (b) and (c) restored the official simulator
     gives 419.7 against 457.2; Dark Sacrifice and 6 Intellect / 90 mana of race base stats make up the rest. Upstream reworked the
     race stat offsets after the pin (6296e8546, 6fc22306b). The raid +4.8% comes from Devouring Plague's 24 s cooldown (70425; the
     fork had 60 s: 3 -> 7 casts) and the missing level resistance.
   - **Feral -6% dummy: mostly the official simulator is right.** Tiger's Fury was removed from the game (1 Oct notes; the 70425
     spellbook lacks it) and the fork cast it 7 times; without it the fork gives 330.3. The chili costs 0.8%. The last 3.5% is two
     Shreds fewer for the same energy (an average of 37.7 energy a Shred against 35.9), not traced. The talents' removal values agree
     within 0.3 points.
   - **Rogue and warrior raid: confirmed, Grace of Air.** Turning Grace of Air off in both simulators: warrior 860.8 -> 826.5 (fork
     818.3 either way), combat rogue 615.5 -> 577.6 (fork 596.4 either way with its own rotation). The fork never applied Grace of
     Air next to Windfury Totem. The rogue dummy is -5.9% with the fork's own rotation: chili 2.8 points, Eviscerate rank 9 (an AQ
     book, not registered) about 0.7, and Thistle Tea (conjured 7676) never used by the official bench, about 0.5. The rest is
     talent values that differ (Improved Sinister Strike 7.7% -> 6.2%, Blade Flurry 2.0% -> 0.5%, Adrenaline Rush 2.8% -> 4.8%,
     Hack and Slash 3.7% -> 4.7%), not traced; re-tune before reading them.
   - **Bench note**: `actionRows` sums each action's damage over every target, the caster included, so Demonic Rune's self-damage
     shows as an action of about 5-11 DPS (`12662` tag 1). The reported DPS excludes it (`IsOpponent`), but damage splits built from
     the action rows count it.
6. **Champion of the Light and the pet swing rule (checked 2026-10-22)**: both edits apply cleanly to a pristine 09e7398 checkout
   (`setup.apply_patches`, every patched file identical to the live clone's). The Retribution smoke character reads 609.8 spell power,
   61.8 of it 30% of 206 Intellect: the patch is live. At upstream master (fbf5d98e8, 2026-10-22) the store still reads 20/40/60 and
   both anchors still exist. The pet hit edit must go at the next re-pin: master inherits hit itself (a20507783, then 9ce48b6ab: melee
   hit 1:1 and spell hit 17/8 from the owner's ranged hit), and our edit's anchor is still there, so it would apply and count hit twice.
9. **Mage hotfix of 2026-10-20 (d3bfea75)**: 09e7398 does not have it. Its mage tree still lists Piercing Ice, Elemental Precision
   at 5 ranks of 1%, and Frost Channeling and Improved Blizzard at their old places. Upstream has it in 983ea6fcc ("mage hotfix and
   talent shift", merged as #594, 12f3f1db0, 2026-10-20). That commit moves the proto field numbers, removes Piercing Ice, sets
   Elemental Precision to 2/4/6, adds Frost Warding's absorb and a Frigid Power buff (1326891, +3% Frost, from Ice Barrier), and its
   tree matches `forever-talents/mage.json` exactly (positions and ranks; 0 differences). Until a re-pin, run.py's talent strings for
   the new trees resolve by name on the old tree: Elemental Precision 3 reads 3% hit, not 6%. No patch: the change spans the proto,
   the store and the mage code. The fix is a re-pin to master, once the gear agent's queue is done (also bringing the chili, the race
   offsets and the pet hit rule; retire our pet hit edit then).
10. **Fork-era option names dropped silently (found 2026-11-04, fixed in specs.json)**: the bench reads an entry's spec fragment with
   DiscardUnknown and only printed what the protos do not know (stderr, shown by the callers only when a bench died). The hunter
   entries sent the fork's `petAttackSpeed: "OneTwo"` (official enum: PetAttackSpeedNone, SlowerAttackIII-II, FasterAttackI-VII at
   +17/25/33/43/54/67/100% on the 2 s base) and `quiverBonus: "Speed15"` (official: the quiver item; Ancient Sinew Wrapped Lamina
   15%, Quickdraw 13, Heavy 12, Night Watch 11, Hunting 10), the Enhancement entry two stray fields (`imbueOh`, `syncType`; no
   official equivalent, the set has no off-hand). So every hunter raid number from the port (2026-10-18) to 2026-11-04 11:05 ran a
   2 s pet with no Faster Attack passive (bm-raid, mm-raid) and no quiver haste (all four entries): the races, re-tunes, family and
   synergy records, ML records, gear tiers' stat weights and the pages' hunter rankings of that period. Now `FasterAttackVI` (the
   1.2 s cat) and `AncientSinewWrappedLamina` (15%, the fork setting's intent; the Lamina needs the Molten Core quest chain, so the
   pre-BiS tier is 2 points optimistic against a Quickdraw Quiver: keep or give the tiers their own quiver). Safeguards:
   `raidsim/spec_check.py [--all-checkouts]` (static: every entry's fragment against the proto files; clean on all six checkouts
   on 2026-11-04) and `run.check_bench_stderr` (a `spec:` warning is fatal in run.py, apl_opt.bench and buff_value). To redo once
   runs resume: the hunter raid lane from its races (markers `r1103/hun-*` removed on 2026-11-04).
