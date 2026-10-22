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
(melee hunter 166 -> 337: 55 casts, out of mana 100 s), debuff conditions without a target (Fire's Scorch line always true). What is left was
traced on 2026-10-22 (Open, item 8): the harness's remapped rotations and lost weapon oil (Frost +16%, part of Shadow), a bench bug
that dropped the warlock's Demonic Sacrifice option, Grace of Air with Windfury Totem (rogue, warrior raid), and otherwise the fork's
stale or wrong data (Seal of Righteousness, Consecration and judgement coefficients, level-based resistance, caster-weapon spell power,
Dark Sacrifice on every race, Tiger's Fury). No simulator patch was needed; Holy Strike's spell-power share is open.

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
