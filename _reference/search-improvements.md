# Search improvement log

> Hand-kept (not generated). User request 2026-10-07: "Make sure we're taking notes of any improvements and changes we can make so we
> can further fine tune the process to find the true best builds." Every self-audit adds to it: what changed and why, what was tested
> and rejected, and the open ideas ranked by what they could still find. Newest entries first in each section. Numbers are the
> community simulator's (ElliotWood/Forever at b0f0df3) or our fight lab's, never in-game measurements.

## How close the process gets (assessment of 2026-10-07)

- Within the models: raid builds probably within about 0.5% of the best build a spec's rotation and gear allow; leveling within 1-2%.
  Races separate builds to about 0.3%, so the "best build" is a handful of tied builds.
- Against the real game the models limit us, not the search: a few percent within a spec, more between specs. Lowest confidence:
  warlock (demon scaling from the client's UI since 2026-10-08; hit rate, school and melee crit are our readings), hunter (our
  pet patches: stats and the unnormalized hit, unmeasured at level 60; the Summon Hawk model), tanks and healers (our own weights and lab),
  leveling everywhere (Classic mob and gear data, assumed pulls, drinking and eating).
- Blind spots of the search itself: builds that need a rotation nobody wrote; gear coupling (a family is searched in another spec's gear
  until it wins); three-talent packages that pay nothing in any pair; leveling builds strong early but weaker at 60 (the main search
  scores level 60); one fight type (single target, 180 s, full raid, an Elemental target).

## Patterns from the 70291 sweep (self-audit of 2026-10-13)

Read from the records of the sweep's open searches (`raidsim/families/*.json`: 28 raid entries; `fightlab/open/*.json`: 26 leveling
rotations; `fightlab/rotations/*.json`: the re-tuned leveling rules) and the three finished healer deep searches
(`heallab/deep/priest-holy.json`, `priest-discipline.json`, `paladin-holy.json`).

- **The raid talent search has converged.** Synergy certificate and structural ranking: 0 leads in 28 entries. The re-search after a
  rotation re-tune (`again`): 12 entries, 11 identical winners, one moved a point (Beast Mastery 27/20/4 -> 27/21/3). Cross-rotation
  races: none adopted. What is left for raid is rotations and model fidelity, not talent search.
- **Hybrids win often**: 11 of 28 raid winners and 15 of 26 leveling winners are hybrids. The same shallow picks recur: Bane and Demonic
  Sacrifice (warlock), Relentless Strikes and Malice (rogue), Careful Aim and Lethal Attacks (hunter), Arcane's mana talents and Missile
  Barrage in Frost. Deep capstones rarely pay for their row. A player-facing note for the class pages.
- **Leveling rotations are weaker than the raid ones.** The cross-rotation race (`cross` in the leveling records) runs several winners
  faster under a sibling rotation: Affliction 39.7 -> 35.0 s per kill under Demonology's (12%), Arcane 31.8 -> 29.0 and Fire 32.4 -> 29.4
  under Frost's (9%), Discipline 42.9 -> 39.1 and Holy 43.1 -> 40.7 under Shadow's (6-9%), Combat daggers 25.9 -> 24.6 under swords'
  (5%). The own-rotation rule keeps those off the pages, but the gaps say our own rotations leave time on the table. Cause:
  `fightlab/rotation_opt.py` can only veto spells and move drink/eat thresholds and knobs; it cannot reorder the priority or add a line
  (the raid's `apl_opt` can). 23 of the learned rules are "never cast X" (Holy Fire for Holy and Discipline priests, Hammer of Wrath for
  Holy paladins, Slice and Dice and Kidney Shot for rogues, Arcane Shot and Multi-Shot for hunters, Cone of Cold and Fire Blast for
  Frost): a veto is the only repair available for a spell in the wrong place.
- **Level 60 is the wrong target for leveling.** The 20-60 polish changed the level-60 winner in 10 of 26 rotations and the order
  polish changed the talent order in 8.
- **Healer cycles repeat**: in all three healer searches every cycle returned the same winner, but the heal-choice policy moved every
  cycle, so the loop never stopped before `--cycles` (3). Paladin Holy cycles took 255, 227 and 228 min against 21-67 min for the
  priests (unexplained: profile it). The two-move check still found +0.37% (Discipline) and +0.50% then +0.47% (paladin Holy): the
  healer landscape is flat (runs agreeing 1 of 4, 1 of 2) and the genetic search ends short of the local optimum.
- **Entries that always find the same build**: the warlock's Fire Destruction, Shadow Bolt and Incinerate entries all end on 20/11/20
  (the Shadow Bolt hybrid); Stormcaller ends on Elemental's 29/22/0. Their own rotations never win, yet each is a full search per sweep.
- **Zero-value points**: raid winners carry 0-23 points under 0.1% each (warrior two-hander 23, Stormcaller 18, Shadow 16, Subtlety
  14), mostly tier fillers the filler audit turns into utility. Surprise: Improved Heroic Strike reads 0 in the 20/31/0 two-hander
  (check the simulator's rank handling, as with Lightning Reflexes).
- **Spell probe**: kept no line this sweep (Berserk, Arcane Power, Combustion, Vampiric Embrace, Holy Nova, Blade Flurry, Riposte,
  Stormstrike in the caster hybrid, Rage of the Farseer); the rotation searches' pools already cover these spells.

## Changes made (with evidence)

| Date | Change | Why (evidence) | Effect |
|---|---|---|---|
| 2026-10-24 | `apl_opt.class_pool` inlines the official rotations' `valueVariables` and expands their `groups` (`inline_refs`); `apl_prune.py` rewrites the rotations already carrying undefined references to what the simulator runs | Self-audit (agent): the pool copied lines without their variables; the simulator drops an undefined reference and the and/or branch holding it, so the rogue's new Garrote line read "not V and V and V and not Garrote" and ran as "Garrote not on the target"; druid feral (22-55 variables), Fury, Protection warrior and paladin rotations would have been next | Pool lines are now the official logic (druid 61, warrior 90 pool lines, none unresolved); the four rogue rotations prune to identical DPS (500 fights, bit-identical), applied after the rogue raid steps |
| 2026-10-24 | Signature-failing builds are no bar and no tuning build (`raid_signature.talents_ok` in `apl_opt.main_builds`, `open_builds.raid_candidates`, `ml_builds.verdict`) | Self-audit: the three Assassination raid builds lack Mutilate; the Assassination rotation had been tuned on one of them, and a Mutilate winner below their 662 DPS would only have "confirmed" them | Assassination now tunes on daggers-split-open-raid (casts Mutilate) and the Mutilate preset; the three stay protected |
| 2026-10-25 00:10 | Bench runs the builds of a call side by side, one per thread (`foreverbench` `simJob`, `core.RunRaidSim`); one build alone still splits over every thread; `WOW_FOREVER_BENCH_SPLIT=1` restores the old way | Speed audit (agent): each build was split 12 ways and waited for its slowest split (12 one-fight splits 12-83 ms under load, one fight 3 ms) | A 114-build x 300-fight polish batch 26.0/19.6 s -> 11.2/10.4 s under the queues' load; DPS identical to 1e-13, the same action rows (order and the last float digit aside); swapped in by rename while the queues ran |
| 2026-10-24 | Raid open search: 2 runs for the first search, 1 for a re-search (were 3 and 2); `family_search.retune` tunes the raid rotation only; tank deep search 3 runs (was 6); the family polish retries a pair's draw up to 20 times and logs how many pairs have a legal build | Speed audit: in 101 raid open searches a later run beat run 1 by 0.1%+ once; runs agreed 3/3 in 24 of 25 and 2/2 in 10 of 10; tank runs agreed 6/6 every time; the dummy half was ~60% of a re-tune; one failed draw dropped 3 of 94 rogue swords pairs and 5 of 50 Enhancement pairs that have legal builds | About 25-45 min per raid entry and 1 h per tank class; leveling keeps three runs (a later run won 0.3%+ in 28 of 107) |
| 2026-10-24 | `ml_pipeline.sig_start`: the ML final step starts from a build with its spec's signature talents (the class's best open-search winner of the spec, else our raid build of it) when the stored winner lacks them | Self-audit: rogue-assassination.json's winner is a Backstab build without Mutilate (made before the rule); its BiS set would have been chosen for it | The rogue ML step (after family-rogue, which gives an Assassination winner under the rule) gears and searches a Mutilate build |
| 2026-10-24 | Follow-up queue `sweep_raid2.sh` (the raid final steps moved into it) | Self-audit: the hunter melee-dps search ran under the old Beast-Survival rule (Raptor Strike, Mongoose Bite, Summon Hawk required), and the Shockadin entry was planned but in no queue | hunter melee-dps re-searched under the relaxed rule, paladin shockadin-raid tuned, raced and searched, then the final steps once |
| 2026-10-24 | `builds_io.update`: proposed-builds.json written under a lock, re-read inside it, only the change applied (open_builds, ml_builds, raid_path_leveling) | Self-audit: each read the file, simulated for minutes, wrote it back whole; the raid and leveling queues can run them for the same class at once | No lost builds when the queues overlap (filler_audit, spec_builds and the derive scripts still write unlocked: short read-write windows) |
| 2026-10-24 | Stale talents in `families/<class>.json` winners repaired (Call of Thunder, Improved Fire Nova -> Trial by Fire, Malediction) | `ml_talents.ok_partial` drops a start holding a removed talent silently: shaman and warlock entries would lose their warm start | 9 winners repaired to the current trees with a `repair_note` |
| 2026-10-25 | One-tree leveling searches (`fl_open_search.py --tree <tree> --rotation <rot>`, records `fightlab/open/pure/<class>-<tree>.json`, read by open_builds and render_modes.leveling_numbers; queue `sweep_pure_lev.sh`); the leveling bar skips signature-failing builds (open_builds, as raid's sig_ok); fl_synergy's re-search picks no candidate outside the search space | Self-audit after the leveling queue: the open search keeps one winner per rotation, and in 7 rotations a hybrid won (Subtlety, Assassination, Destruction, Demonology, Elemental, Beast Mastery, Survival), so those pure specs never had a search; three of their pages showed hand drafts failing the signature rule (Subtlety 5/16/30 without Hemorrhage, Assassination 33/16/2 without Mutilate, Destruction 21/0/30 at 59.6% core share) | Each of the seven gets its own search (~3-5 h each), written when 0.5% ahead of the spec's passing builds |
| 2026-10-25 | `ml_pipeline.sig_start` falls back to the simulator's presets raced in the class's entries (race reports' `sim preset:` rows) | Self-audit of the rogue raid search: the assassination-raid winner is the 28/21/2 Daggers split (663 DPS) and no Assassination build of ours holds Mutilate, so the ML final step would have started from the Backstab winner its space rejects | The rogue ML step starts from the Asn Muti preset (51 points, Mutilate) |
| 2026-10-25 | The fight lab's rogue daggers rotation casts **Mutilate** (both hands, 75% weapon + flat each, +20% under Deadly Poison, 2 combo points; daggers builds with the talent only, Sinister Strike otherwise); `sweep_rogue_mutilate.sh` re-tunes combat-daggers-raid's rules from scratch, redoes its open search and the Assassination one-tree search (old entries archived as `*.pre-mutilate.json`, family caches dropped), then race, report, open_builds, signature audit | Self-audit of the first one-tree results: the Assassination winner 30/13/8 held Mutilate and cast it 0 times; the module's only builder was Sinister Strike, so every Assassination leveling build failed the signature rule and the daggers open search never saw Mutilate | Builds without the talent bit-identical (14 of 18 checks; the other 4 hold Mutilate), mage regression identical, lint clean; 31/20/0 casts 3.0 Mutilates per kill at 60 (13% of its damage), the 21/28/2 daggers build 5% faster at 60 |
| 2026-10-26 | `fl_open_search.py`'s finalists race checks `space.valid` (the known positives had joined it unchecked); `open_builds.py` takes only a one-tree record's own tree; `sweep_survival_fix.sh` redoes the Survival one-tree search (families cache reused) | Self-audit of the one-tree queue: the `--tree Survival` search's 20-60 race picked the 17/10/24 Beast-Survival known positive (filed as the hybrid) | The other six one-tree winners are of their tree (Subtlety 12/9/30, Destruction 6/11/34, Demonology 21/30/0, Elemental 31/12/8, Beast Mastery 31/16/4 with Bestial Wrath; Assassination re-runs after the Mutilate fix) |
| 2026-10-26 | (1) A hybrid ML search in pure-spec entries keeps to splits classified as the hybrid (`ml_talents.run_target`); (2) `render_modes.raid_numbers` skips a race row whose split differs from the build's current talents; (3) simulator patch `forever_absent.go` (an aura, dot or spell the build lacks reads absent; upstream dropped the condition and the action cast always, `apl_action.go`: "Condition could not be resolved and will be treated as always true"), swapped into the queue's bench by rename 2026-10-26 11:46 (druid's family search mid-way; old binary `foreverbench-preabsent.exe`); the shaman hybrid's final step re-runs in sweep_raid2.sh before ml-builds | Self-audit of the shaman raid pages: the Elemental/Enhancement hybrid's ML searches all won 17/31/3 (an Enhancement build, rejected by `not_split`); its page paired the repaired 15/24/12 with the 17/26/8 build's 713 from 2026-10-16; today's 437 is the Maelstrom Weapon Lightning Bolt line casting always (51 casts) for a build without the talent | Spaces: shaman, rogue and warlock hybrids restricted, Frostfire and Smite (hybrid entries) unchanged. Patch: every page build and search winner of hunter, mage, rogue and shaman bit-identical at 3,000 fights except the hybrid 15/24/12 (443 -> 664) and the simulator's FFB preset in fire-raid (547 -> 623); no finished ranking flips. Removal values of rotation-conditioned talents were inflated (Maelstrom Weapon 40% -> 6.5%, Fingers of Frost 45% -> 3.7%): the synergy certificates and value tables of finished classes over-rate them |
| 2026-10-26 | `fl_signature.penalty` and `raid_signature.penalty`: a failing build pays `FAIL_STEP` (x0.9) on top of its core-share ratio (raid: steps started after 16:00, druid ML onward); the Survival one-tree record's post-race steps (polish, orders, values, certificate, signature) redone under it; `fl_levels.pick_order`: the race's old pick wins back over a polished build only when it passes its signature check too or the polished one fails (the first redo polished to a passing 10/11/30 at 23.82 s and the failing pick at 23.65 won back; in the second redo the polished build also failed the 600-fight check: the 10/11/30 family sits on the 50% line, the page keeps 9/10/32 at 24.14 s) | Self-audit of the Survival re-run: the search, race and polish all picked 10/11/30 (2.1% faster than the page's 9/10/32) with a melee share of 49.5% against the 50% rule; the ratio penalty (x0.99) was smaller than its speed edge, the race's pick falls back to the fastest failing finalist when none passes, and open_builds then writes nothing: 2.5 h for no page | Finished leveling records unaffected (the penalty only steers searches) |
| 2026-10-26 | `fl_signature.leveling_space` lifts the own-rotation tree rule with `WOW_FOREVER_UNRESTRICTED=1` (set by `sweep_unrestricted_lev.sh`) | Audit before starting the unrestricted leveling search: `WOW_FOREVER_SIGNATURE=0` turned off the signature talents and penalty but left `allow_trees` and `leveling_rotation_ok`, so each rotation would still have searched only its own specs' builds (priest Discipline: 6 of 21 builds valid; 21 with the switch) | Raid half: `ml_talents.run_target` and `family_search` need the same switch before the unrestricted raid search |
| 2026-10-13 | `heallab/deep_heal.py`: the cycles stop when the winner repeats (the policy re-tune still runs every cycle) | Every cycle after the first returned the same winner in priest Holy, Discipline and paladin Holy, but the policy moved a little each cycle, so the old rule (winner and policy both unchanged) never fired | One cycle saved per healer spec whose winner repeats: about 4 h for the paladin, 0.5-1 h for a priest; applies from the druid on (the paladin's three cycles were already done) |
| 2026-10-09 day | `apl_opt.main_builds`: a full-raid rotation is tuned on the entry's best build in a full raid among the builds the entry still lists | The 70291 re-baseline picked the training dummy's best from the previous race report: the Frostfire raid rotation was tuned on frostfire-open-raid, removed days before, and kept a rank-2 Fireball fallback the downranking penalty had made weak; 13 entries were tuned on a build other than their full-raid best | Frostfire's 0/29/22 page build 663.8 -> 678.9 (+2.3%, Frostfire Bolt rank 2 below 30% mana); the nine other entries re-tuned: Beast-Survival +0.6%, the rest unchanged |
| 2026-10-09 day | Simulator presets against our builds in a full raid, every entry | The druid's review: our Feral builds, optimized on the training dummy, skipped Shifting Power, which the raid rotation's powershifting pays for | The simulator's Feral Cat 9/35/7 preset 691 against our 594 (+16.4%), written as a derived build (`preset` field on the page); Combat swords +1.1% (a variant entry), nothing else ahead |
| 2026-10-09 day | Fight-lab class modules reviewed against the 70291 tooltips (one agent per class) | Rotation-guide review: the mage asked for "Hot Streak" (Heating Up since 70170: never simulated); crit damage talents added to a spell crit's 50% bonus as if it were 100% (mage Ice Shards / Arcane Mind, shaman Elemental Fury: x2.5); Fire Nova, Magma Totem and Summon Hawk parsed to 0 damage; Kidney Shot stunned for 0 s; Lava Burst had Wrath's guaranteed crit; Holy Shield 20% block written in (30%); Cold Blood buffed every Sinister Strike; healer-lab Illumination returned full cost | Mage Frost leveling 25.4 -> 27.2 s per kill at 60 (crits, Ice Lance 0.10); every class module edited with smoke runs; paladin Holy capacity 0.645 -> 0.570; the leveling rules re-tuned where the mechanics moved (rogue: same rules) |
| 2026-10-09 day | `fightlab/module_lint.py` (new) | Two of the day's bug classes are mechanical: a module asking for a talent the current trees lack reads 0 for ever; a tooltip whose wording the parser misses casts for nothing | Found the druid's King of the Jungle, the warrior's Boundless Rage / Precision / Toughness / Improved Cleave, Fire Nova and Magma Totem; run it after every data refresh (`_reference/fightlab-lint.md`) |
| 2026-10-09 day | `render_raidsim_sections` / `render_heallab_sections` build their cross-class summaries over every class; `open_builds` measures a winner against its own spec's builds | A one-class regen had cut `_reference/raidsim-summary.md` to one class; the Beast-Survival open winner "confirmed" a Survival hand draft and the hybrid's raid page went empty | Summaries whole; the hunter's Beast-Survival raid build kept |
| 2026-10-09 01:46 | The patches read their environment switches once at program start | The audited bench ran 20,000 Fire fights in 5.5 s against 0.9 s before: `os.Getenv` in hot paths (every spell's hit roll; the dynamic pet's inheritance) is a system call on Windows | 6x faster again, results identical (same DPS and actions); swapped in by rename at 01:46 while the rotation pass ran (01:00-01:46 ran slow) |
| 2026-10-09 night | Stacked temporary enchants (rogues' stones over poisons, the warlock's Spellstone over Wizard Oil) through a second enchant slot; the bench built under another name and swapped in by rename while the queue ran (`build_next_bench.py`) | Forever's rogue and warlock deep dive; a simulator patch used to mean stopping the queue | Combat +2.1%, warlocks +2.8% to +3.2%; no queue stop |
| 2026-10-09 night | Configuration audit: Atiesh out of the full raid; enchants on 15 gear sets (`fill_enchants.py`, also inside `gear_tiers.make`); feral weapon and idol in their slots; oils, stones and Mighty Rage Potion added | A research pass and a check of every gear set and consumable list: the fork's full party carries Naxxramas's Atiesh, the gear tools never add an enchant a preset lacked, one preset is misaligned | Full raid: casters -4% to -7%; Arms +7.4%, Fury +8.5%, Retribution +4.4%, Balance +3.5%, feral +6.2% (enchants); warlock +4.4%, Elemental +3.8% (oil); Arms +5.8% (stone and potion). Larger than most search gains |
| 2026-10-09 night | Mechanics from Blizzard's notes and the client: crit rage x2.0, Bear Form threat +50%, rage from damage taken over the expected creature health, no 1% hit suppression or spell floor, downranking penalty, Raptor Strike queue; the fight lab's rage rules; the healer lab's penalty | Each statement quoted in `patches/README.md` | Warriors +1.8% to +2.8%, melee +0.5% to +0.8%; Smite -10.9% and Fire -4.0% until their rotations are re-tuned; Arms leveling up to 7% faster; Holy paladin capacity -5% |
| 2026-10-08 night | Demon scaling and the pet hit rule patched into the simulator (`patches/README.md`) | The client's own UI text (build 70291) gives the demon percentages; the Faster Attack passives and two forum logs show pet damage is not normalized by attack speed, which the fork does | Full raid, 3,000 fights: demon-keeping warlocks +3.6-4.2%, hunters with a pet +3.0-3.9%; sacrifice and Lone Wolf builds unchanged |
| 2026-10-08 night | The fight lab's pets follow the same rules (`tables.PET_SCALING`, `HUNTER_PET_SPEED`; engine pets get a spell power) | Its hunter pet and demons inherited nothing and the cat swung at 2.0 s, the leveling half of the same gap | Hunter leveling 4-11% faster per kill, warlock 2-5% (400 fights, levels 20-60); the mage regression is identical with and without the change; its baseline moved with the 70291 spell ranks (identical before that commit) |
| 2026-10-08 night | `apl_opt --skip-commit <sha>` skips entries whose rotation record was written on that simulator commit | A restarted `--all` pass redoes every finished entry (no resume) | The re-baseline restart after the pet patches kept the mage rotations already tuned on 2ce8265 |
| 2026-10-08 | `apl_opt` without `--tune`: our best build and the best preset are the tuning builds, every other listed build protected | An `--all` pass scored every candidate on 6 to 8 builds an entry (the commit message's "40 minutes" was a misread clock: the first run had been going 4 minutes) | Several times less work per round; the same protection |
| 2026-10-08 | Open searches only try builds that may use their rotation (`Space.allow_trees`) | Six searches had spent their time on another spec's build (the priest's Discipline rotation found a 31-point Shadow build), which the own-rotation rule cannot show | Every winner is writable; pairs from two other trees are skipped in the polish (cheaper); the six get restricted re-runs after the queue |
| 2026-10-08 | Each spec plays its own rotation (user decision): no sibling-rotation numbers or adoptions; writer, pages and the raid cross step changed; four page builds re-raced with their own rotation | "I don't want classes specs taking other specs rotations or builds or anything just because it's faster" | Pages show each build with its spec's play; some leveling numbers got slower (druid Balance 37.9 -> 52.0 s as a caster) |
| 2026-10-08 | `ml_pipeline --fresh` keeps a finished record in `raidsim/ml/prev/`; the pages fall back to it, flagged, while a re-run is in progress (`render_modes.ml_tiers`) | The hunter's interrupted re-run had replaced its records, and the regen dropped the hunter raid pages' gear-tier and gear tables | The hunter pages show the 2026-10-01 tables with a note until the queued re-run ends |
| 2026-10-07 night | Family polish climbs two pairs at once in threads (`family_polish(workers=2)`, raid search; threaded bench calls get their own config file) | The machine ran at about 80% CPU during a polish: the gap between one climb's batches | Identical families in a test (shaman, 3 pairs: same scores and builds), 22% faster under load; from the druid on |
| 2026-10-07 night | Sibling entries' polished families join each search's starts (raid `family_search.sibling_starts`, leveling `fl_open_search.sibling_starts`; leveling family caches written) | Families another rotation found are free starts | One evaluation per build; from the druid on |
| 2026-10-07 | Family polish logs progress every 20 pairs | A 94-136 pair polish was an hour of silence | Hangs can be told from slow steps |
| 2026-10-07 | `fl_levels.py`: 20-60 polish, three talent orders raced, order polish (block moves), explicit stats order | Shaman Elemental's level-60 winner was 2.1% faster at 60, 5.7% slower at 50 | Leveling picks moved 2-6% (mage Fire 5.5%, paladin Protection 5.6% by order alone, shaman Elemental 2.9%, hunter 2.9%) |
| 2026-10-07 | `apl_opt`: candidates scored on the tuning builds only, protected builds checked in the seed-2 confirmation | One re-tune round of 365 candidates on 6 builds took 2 h 17 min; a gain on the tuned build was diluted 6x | About 6x cheaper re-tunes; real gains no longer averaged away |
| 2026-10-07 | Replacement bar 0.5% (was 2%) | The 2% bar was set without a reason (misattributed to the user); 0.5% is above the noise between separate races | Better builds reach the pages |
| 2026-10-07 | Duplicate entries skipped (`signature`, `same_as`); paladin Seal of Fury and Shockadin entries retired | Three entries ran the same rotation at 1.5 h a pass | Saves a pass per duplicate |
| 2026-10-07 | Structural ranking re-measures around the current winner | It had re-found a lead against an outdated winner and re-searched for nothing | No wasted re-search |
| 2026-10-07 | Certificate singles and pairs measured unpaid; present talents also at one and two ranks less | Paying from cheap points double-counted and mixed partial ranks | Clean marginals ("Fire Power 4" expressible) |
| 2026-10-06/07 | Synergy certificate and exhaustive structural ranking after every search; multi-rank proc talents as keystones; tier-chain moves | Every miss was a package worth nothing alone (the user's 0/29/22 Frostfire) | All known misses are found from the old winners |
| 2026-10-06 | Bench target is an Elemental | Creature-type effects read 0 (Improved Tracking, +4.9% for the melee hunter) | Hunter records re-run |
| 2026-10-07 | `low_priority.py` for side jobs; never stop a waiter with TaskStop alone | A stopped waiter's child fired a 3-hour pipeline that halved the queue's speed | The queue keeps the CPU |

## Tested and rejected

| Date | Idea | Test | Result | Decision |
|---|---|---|---|---|
| 2026-10-07 | Warm-start each pair's polish from the sibling entries' polished family | Shaman Stormcaller, 8 pairs, 150 fights, same random draws, separate caches | 80% fewer builds, same best family; 4 of 8 families 5-9% worse, 3 better (a climb from a sibling's optimum stops there) | Rejected as a polish start; the sibling families became extra search starts instead |
| 2026-10-07 | Rank-3 Seal of Command on Retribution's twist line | Rotation search | Best for mana-hungry builds, but costs the hand draft 0.6% | Rejected by the protection rule; a mana-conditional rank line stays open (below) |

## Open ideas, ranked by what they could still find

0a. **Fight-lab cast-path audit (2026-10-25, agent; read-only)**: spells a spec's leveling rotation never presses, so no search can value
   their talents. Being fixed: rogue Venom, hunter Sniper Shot, mage Pyroblast hard-cast (only Heating Up casts it), mage Frost Blast.
   Done the same day (cast paths, knobs off by default: every number unchanged, mage regression identical): Venom (`VENOM_HP`/`VENOM_CP`:
   +2.4% to +9.2% slower per kill on a 31/20/0 Mutilate+Venom build at 60: an Eviscerate is worth more), Rupture (`RUPTURE_HP`), Sniper Shot
   (`SNIPER_SHOT`; its damage had parsed to 0; +1.8% to +11% slower on the Beast Mastery slot build, -0.7% to +4.9% Marksmanship),
   Pyroblast hard cast inside a root, stun or the run-in (`PYRO_HARDCAST`: +0.4% to +1.5% slower; the pre-pull opener needs an engine
   pre-pull model), Frost Blast (`FROST_BLAST`: never pays). Next re-tunes test the knobs (the hunter's mm-raid and bm-leveling tuning
   builds hold Sniper Shot; rogue's combat-daggers-raid tuning build lacks Venom). Open: Fire's signature requirement should count Heating
   Up with Pyroblast (only Heating Up casts it; the hand draft holds Pyroblast alone and casts 0); a Presence of Mind Pyroblast line for Arcane.
   Open: rogue Rupture's cast is now a knob, hunter Wing Clip in `decide_melee`, priest Mind Flay in `decide_holy` (the Holy/Shadow hybrid),
   warlock Drain Soul, paladin Exorcism (Undead and Demons only), mage Flamestrike in `decide_aoe`, shaman single-target Chain Lightning.
   Rules: `enhancement-dps.json` vetoes Lightning Bolt above 35% health, the Elemental-Enhancement hybrid's required spell (`--check-rules`
   misses it: the hybrid maps to `elemental-dps`); the signature audit ran the melee Beast-Survival `opt-melee-dps-solo-60` in `bm-leveling`;
   the druid, shaman and warrior rules files carry no `signature` block (tuned before the rule).

0. **From the 2026-10-24 speed audit (agent), after the queues** (evidence in its report, summarized here):
   - Gear is chosen on the training dummy (`gear_tiers.make` races in the dummy setting, `-raid` sets too): give `make` a setting, gear
     the full-raid winner in `ml_pipeline.final` and drop the two dummy searches (~40% of the ML final step, and the gear-talent coupling).
   - Rotation-talent coupling: the mage re-tunes on the open winners gained 8.9-13% (Frost's Arcane Blast refresh line); before the
     polish, a quick re-tune on a build for each damage keystone whose ability the rotation never casts; after a re-tune that moves a
     build 3%+, re-polish the top 10 families instead of reusing the cache.
   - A result cache on disk (`ml_talents.Sim.run`, `fl_open_search.LabSim.run`; key: build, fights, seed, setting, hashes of rotation,
     gear, bench binary and switches): a paused step replays to its kill point in seconds (pauses lost ~4 h in two days); the fight lab
     has no cache at all.
   - `apl_opt` screening: each round's 290-600 candidates at 750 fights, the top 40 at 3,000 (~60% of a rotation tune; A/B one recorded
     round first).
   - Distinct finalists: the races raced near-copies (rogue 641.4 x5); merge identical stage-1 results, pick finalists by distinct
     family, and put the top 5 distinct polished families into the leveling 20-60 race (the 20-60 polish changed 10 of 26 winners).
   - Polish pruning: log each climb's score per step, then replay one entry with "4 steps for all, finish the top half" (the family
     nearest each winner was always within 2.1% of the best family; the median family ends 5-12% behind).
   - Unrestricted raid search: skip entries 10-12%+ behind the class's best (about 11 of 25), keeping the margin wide.

1. **Leveling rotation moves (2026-10-13, the sweep's largest gap).** Give `fightlab/rotation_opt.py` the raid `apl_opt` move set:
   move a priority line up or down, insert a line from the class's other leveling rotations, and conditional rules ("only as the
   opener", "only below 20% mob health", "only above N% mana") where it now has only vetoes. Each spec still plays only its own
   rotation; the sibling lines are search material. Evidence: the cross-rotation gaps of 5-12% and the 23 "never cast" rules above.
   Measure each new rule as now (common random numbers, seed-2 confirmation, level-weighted time per kill), then re-run the class's
   leveling half: the winners were searched under the weaker rotations.
2. **Rotations for new playstyles.** A build that needs a rotation nobody wrote is invisible. The spell probe only tries never-cast
   abilities of the winner. Idea: probe the abilities of the top 3-5 families too, and write a base rotation for any family whose
   keystone is an ability the entry never casts. Cost: a probe is minutes per ability.
3. **Leveling early levels.** The main leveling search scores level 60; the 20-60 polish is local. 2026-10-13: the polish changed the
   winner in 10 of 26 rotations and the order in 8. Idea: score the main search on levels 40, 50 and 60 from the start (fewer fights
   per level), or at least score its finalists and top families there and polish the best three. Cost: about 3x per scored build.
4. **Certificate around the runners-up.** Certificates check pairs around the winner only. A runner-up family within 1% may hide a
   package. Idea: a light certificate (singles only) around the second and third families. Cost: 1-2 min each.
5. **Triples.** The checks are complete for pairs. Idea: combine the pairs with the largest positive interactions that share a talent
   into triples and measure them unpaid. Cost: small (tens of builds).
6. **Gear coupling.** A new family is searched in another spec's gear until it wins. Idea: give the top three families of each entry a
   quick phase-1 set (`gear_tiers.make`) and race them in it. Cost: about 10 min per family.
7. **Fight variety.** Done 2026-10-08: `raidsim/fight_variety.py` races each spec's pick and next builds in five full-raid fights
   (standard, three targets, Undead, 90 s, 300 s) and flags a pick 2% behind; the sweep's last phase runs it for every class.
8. **Model fidelity** (biggest real-game gap, not search): demon scaling and the pet hit rule are patched from the client's text and
   forum logs (2026-10-08) but unmeasured at level 60; the final beta build refresh; comparison with beta logs and real leveling times.
   Open after the 2026-10-09 audit, roughly by size (stacked enchants and the warlock's stones were added the same night): the lower
   proc chance of low ranks; leveling mob health from the client's ExpectedStat table (+7-35% over the lab's Classic medians; unknown
   whether the server uses it: a `MOB_HP_MULT` sensitivity); glancing and crit suppression against bosses (a beta tester's Skills
   panel shows them); negative resistance from debuffs (testable at level 30 with Curse of the Elements rank 2); Forever's Spirit regen;
   leveling gear from Forever's item database. (Crit per stat point by level now follows the client's table, 2026-10-09.)
9. **Weapon variants on the pages.** The rogue's swords entry found 18/33/0 at 746.6 DPS, +1.9% over our swords builds, but the Combat
   page shows one build per spec (the daggers build at 770), so a swords player never sees it. Idea: a weapon line on the page when a
   spec's entries differ in weapon type (swords, daggers, maces), each with its entry's best build. A page change, not a search change.
10. **Skip a sibling's checks when an entry's winner equals a finished entry's.** The rogue's Assassination entry ended on the daggers
   entry's 16/33/2 at the same DPS, and the two rotations are interchangeable for it (cross-rotation race +0.0%), yet both ran the
   certificate and the structural ranking. Saving: about 4 min per such entry; low priority.
11. **Mana-conditional spell ranks.** Retribution's lower Seal of Command rank pays only for mana-hungry builds: a rank line guarded by
   mana would let one rotation serve both.
12. **Spells the models leave out (audit 2026-10-08).** The fork ships five Forever abilities as stubs (Revive, Enchanted Flare,
   Confounding Flash, Contingency Plan, Divine Grace): none deals damage, so no raid number misses them. The healer lab casts neither
   Divine Grace nor Contingency Plan (priest baseline heals on 10-minute cooldowns): every priest build would gain about the same, so
   no talent choice moves. Low priority.
13. **Skip the re-search after a rotation re-tune (2026-10-13).** `family_search`'s `again` search changed no winner in 11 of 12
   entries (one point in the 12th). Idea: replace it with a polish of the winner (and the top two families) under the new rotation,
   keeping the full re-search only when the polish moves. Saving: 20-40 min per re-tuned entry.
14. **Search converged showcase entries once (2026-10-13).** The warlock's Fire Destruction, Shadow Bolt and Incinerate entries end on
   the same 20/11/20, Stormcaller on Elemental's 29/22/0. Idea: after a sweep confirms an entry's winner equals a sibling's and its
   rotation never wins, mark it `confirmed_by` and skip its search until its rotation or the data changes. Saving: 1-3 h per sweep.
15. **Improved Heroic Strike reads 0** in the warrior's 20/31/0 two-hander (and Enrage 5/5, expected without boss melee on the warrior).
   Check the simulator's rank values and whether the rotation's Heroic Strike line is rage-capped; add to the sim value audit if wrong.
16. **Why paladin healer-lab cycles take 4 h** (priest 21-67 min, 2026-10-13). Profile `heal_worker` for the paladin module (Holy
   Light's cast time, Illumination, the bisection steps) before the next healer sweep.

## Efficiency (measured)

- 2026-10-07 night: during a rogue family polish the machine ran at about 80% CPU (12 logical processors). A bench call costs about
  0.2 s to start; a batch of 120 builds at 300 fights about 4-5 s; neighbour generation about 0.07 s. The idle fifth is the gap between
  batches (Python work, the batch tail). Done the same night: two climbs at once in threads, identical outputs against the sequential
  polish (shaman Stormcaller, 3 pairs, 6,204 builds each way), 128 s -> 99 s at low priority next to the running queue. The leveling
  polish too (2026-10-08 00:3x: shaman Enhancement, 3 pairs, 5,247 builds each way, identical, 169 s -> 150 s under load; both threads
  share the fight-lab pool), from the rogue's leveling half on.
- 2026-10-08: a full re-tune of both Assassination rotations (rogue) took 5 minutes after the apl_opt fix; one round of the hunter's
  bm-raid re-tune had taken 2 h 17 min before it.
- Polish cost per pair is about 10 improving steps of 120 builds plus a final pass of about 160: the climb, not the final pass, is the
  cost. Cheaper climbs must not change where they end (the warm-start test above).

## Overnight measurements (2026-10-08)

| Step | Before | After | Note |
|---|---|---|---|
| Raid family polish, rogue entry (94 pairs) | 49-60 min, 113-132k builds, sequential, CPU to itself | | the rogue ran the old code |
| Raid family polish, druid Balance (59 pairs) | | 13 min, 81k builds | two threads; caster simulations are faster than melee |
| Leveling family polish, rogue rotation (94 pairs) | | 42-45 min | two threads |
| Full re-tune, both Assassination rotations | one round 2 h 17 min (hunter, before the fix) | 5 min | tuning builds only |
| Sibling starts in a leveling search | | 81 of 186 starts (rogue Combat swords) | free |

First in-loop runs of the 20-60 steps (rogue): the order choice made the daggers pick 1.5% faster (own tree last), and the order
polish kept two block moves for the Combat-Subtlety pick (-0.3% and -0.8% at levels 30-50, 25.64 -> 25.52 s at 20-60).

## Self-audit checklist (after every class)

- After a re-baseline or a simulator update: every entry's best simulator preset against our best build in a full raid (2026-10-09: Feral's preset was 16% ahead, our builds dummy-optimized), and the build each raid rotation was tuned on (`tuned_on` in the rotation record) against the entry's full-raid best.
- After a data refresh: `fightlab/module_lint.py` (renamed or removed talents, tooltips that parse to no damage), and a crit-damage talent's semantics ("increases the critical strike damage bonus by X%": X% of the 50% spell bonus, of the 100% melee bonus).
- After a fight-lab mechanics fix: the class's leveling rules re-tuned from scratch (`rotation_opt.py <class> --fresh --write`) and its fight-lab races and reports re-run (`rebuild.py <class> --steps race,report,regen`), or the pages mix numbers from both sides.
- A new bench binary: time it against the previous one on a fixed config (20,000 fights, the machine otherwise idle or both under the
  same load) and compare the outputs before swapping it in (2026-10-09: a 6x slowdown went unnoticed for 45 minutes).
- Configuration, not only the search (2026-10-09: four configuration errors moved specs 4-8%, more than most search gains): the full
  raid's buff list against the current phase, an enchant in every enchantable slot of every gear set, each spec's consumables (oil,
  stone, potion), items in the slots their type allows.
- Step timings in the logs (polish, search, certificate, structural ranking, re-tunes) against earlier classes.
- Every lead: its cause (search gap, rotation, gear, bench bug) and whether a known positive should be added.
- Winners holding abilities the rotation never casts; "Not in this build" notes on the leveling pages.
- Builds written or confirmed; pages regenerated; link check clean; commit and push.
- (2026-10-24) Before/after jumps in a rotation record: `final.*.before` is the record's `start` (the simulator's preset), not the previous
  tuned file; a 285 -> 662 "gain" was a Mutilate-only preset run on builds without Mutilate. Compare against the log's previous-file line.
- (2026-10-24) Every build an entry tunes on or counts as a bar holds its spec's signature talents (`raid_signature.talents_ok`);
  `apl_prune.py --check` lists no rotation; the stored records hold no removed talent (the warm starts drop them silently).
- (2026-10-25) After a leveling queue: every pure spec has a winner filed under it in some record (main or `open/pure/`), not only a
  hybrid that won its shared rotation; the signature audit's page rows show no FAIL (`_reference/signature-audit.md`).
- (2026-10-25) Every signature spell a leveling rotation requires (`rotations/<class>-<spec>.json` `signature.required`) has a cast path in its fight-lab module's priority for that rotation: a talent the module never presses (Mutilate until 2026-10-25) fails every build of the spec however long the search runs.

- 2026-10-26 (druid self-audit): `raid_signature.entry_spec` filed the unlabelled builds of a tank entry (a search's "deep: tank", the
  simulator's presets) by split, so the bear rotation search held them to the cat's Feral Combat rule (core share 18-27% against 80%) and
  rejected Enrage and Maul edits. Now every build of a `"tank": true` entry is the tank (the druid's "Feral Combat (Bear)", no rule;
  paladin and warrior tanks unchanged: their split already reads Protection). The talent search was unaffected (tank values unpenalized).
  Bear rotation re-tuned afterwards (`bear-retune.log`). Also: never run `unr_cands.py` from main; it writes start files into the
  candidates folder of the folder it runs in, and main's races pick up every candidate.
- 2026-10-27 (unrestricted mage audit): `rotation_opt.py --fresh` wrote its result even when the saved rules were faster (mage Fire's
  pass-2 re-tune found nothing and wrote the hand-written rotation, about 2.5% slower than pass 1's rules on the same build). In the
  `unrestricted` worktree a --fresh run now races the saved rules in the seed-3 check and keeps them when faster; Fire re-run with
  main's tuned rules as the saved file (`unr-fire-fix.log`). Open: the same guard on main (there a --fresh after a mechanics fix is
  meant to forget the old rules, so it must race them under the new mechanics, which this does).
- 2026-10-27: bear rotation re-tuned after the entry_spec fix: +11-12% tank value for every bear build (Maul ungated +6.7%, Primal Bite
  dropped +2.2%, Enrage below 20 rage +1.3%, Lacerate +0.3%). Raid queue 2 searches the tank talents again (`druid-tank-2`). Also fixed
  in sweep_raid2.sh before it ran: the shaman-hybrid-clear block had a literal line break inside a Python string (a SyntaxError: the
  record would not have been cleared). Check every queued heredoc with `compile()` before a queue starts.
- 2026-10-28 (self-audit, unrestricted leveling): three rotations' no-rules winners are slower at 20-60 than a build of ours the same
  race ran (mage Fire 34.24 against fire-open-leveling 33.87, priest Shadow 24.53 against shadow-open-leveling 24.27, warlock Affliction
  36.24 against 36.14). The level-60 screen cannot tell them apart (priest 177.5 against 177.4 kills/h) and the winner's order is
  polished from the stats model's, while our build carries an order polished by an earlier run. Harmless on main (open_builds.py
  writes a winner only 0.5% ahead of ours), but the no-rules summary must take, per rotation, the faster of the winner and the race's
  builds of ours (it changes the priest's no-rules best: 13/3/35 at 24.27 s, not 15/3/33). Lead for fl_open_search: our raced builds
  as finalists of the 20-60 race.
- 2026-10-29 (raid queue 2): the shockadin-entry heredoc wrote specs.json with `json.dumps(indent=1)`; apl_opt's `_point_specs` edits the
  file as text and expects the fmt_json layout (class blocks closing at two spaces), so the next rotation write raised IndexError
  (shockadin-apl rc=1; it had no builds to tune on, so nothing was lost). Repaired with `fmt_json.py` under the specs lock before the
  family search's re-tune. Rule: a script that writes specs.json goes through `fmt_json.py` (or run.py's writer), never a bare dump.
- 2026-10-29 (raid queue 2, Shockadin under the signature rule): the winner sits at the rule's edge (Holy Shock core share 12%, needs
  12%), so the same build passed at one race stage and failed at the next (759.0 on 30,000 fights, 682.5 = x0.9 on 100,000), and the
  first search's "certificate +10.92%" was a build leaving the penalty, not DPS. The written build (24/0/27, 759.1, passes the final
  check) is right; the higher 23/0/28 (792.4) fails the rule. Open idea: measure the core share once per build on the check seed
  (or with a small hysteresis) so the race's stages agree.
- 2026-10-29 (raid queue 2, ml-builds): the filler audit's local search took any legal move and never checked the signature rule, so
  its tidy of the new `frost-ml-raid` (21/0/30, spec Frost) moved seven Frost points into Arcane (Winter's Chill and Frost Channeling
  into Arcane Mind and Arcane Instability, +17% in a full raid), leaving a 28/0/23 Arcane/Frost hybrid under the Frost spec field;
  with the tree fix alone, its second pass took Missile Barrage's second point (+5.7%), which puts Frostbolt and the Frost spells at 52%
  of the damage (the rule: 60%; the ML search had penalized it, it did not miss it). Fixed in `filler_audit.audit`: a move may not
  change the spec the points make (`spec_modes.spec_of` without the `spec` field), and a candidate whose run fails the signature check
  (`raid_signature.check` on its own casts, seed 1 and seed 2) is dropped. frost-ml-raid restored and tidied again (utility moves only,
  -0.02%) and frost-raid re-raced (the queue had raced it mid-repair). No other filler record changed its build's spec; the queue's
  sig-audit step re-checks every build's signature share. Rule: every step that edits a build keeps both the tree rule and the
  signature rule, not only the searches.
- 2026-10-30 (raid queue 2 done, page audit by a read-only subagent): (1) `search_check.py` exited rc=1: the Frostfire known positive
  (0/29/22) still held Piercing Ice (removed in 70425) and run.py stops on an unknown talent. The positive now names the page build it
  became (`build: frostfire-fingers-of-frost-raid`, repaired by repair_builds.py), and a positive holding talents the trees lack reports
  STALE instead of stopping the check; all four pass (Frostfire's winner +5.0% over it). Rule: after a tree refresh, repair
  known-positives.json with the builds. (2) The new Shockadin page recommended `opt-ret-dps-parse` (a Retribution export filed under
  Shockadin by its 24/0/27 split, no full-raid number, no signature check) over the measured `shockadin-open-raid`: render_modes'
  raid ranking now puts builds without a full-raid number after the measured ones. (3) `shockadin-open-raid` fails the signature check
  at 11.8% Holy Shock against 12% since the 2026-10-29 rotation re-tune (Weakness Analyzer used at the top: +1.8% DPS, a stat buff that
  dilutes Holy Shock's share; Holy Shock is still cast on every cooldown, 18 casts in 180 s). The 12% is our stand-in for "Holy Shock on
  every cooldown" (signature_spells.json note): open question to the user (a cast-based rule for one-cooldown signatures, or keep 12%
  and re-search Shockadin under the new rotation). "12% under 12%" now prints one decimal. (4) Cosmetic: `arms-ml-raid` and
  `survival-raid` carry `replaces` flags though the replaced build leads its page (the pages enforce the bar; the flag does not). (5)
  Lead: Subtlety's pre-BiS full-raid DPS (641) is above its BiS (618): gear_tiers' BiS search should race the pre-BiS set as a
  candidate (every pre-BiS item is in the BiS pool). (6) The Assassination hand draft (no Mutilate) fails the signature rule and is
  hidden, while Shockadin's failing build is listed with a note: both follow render_modes (missing required talent = not the spec).
- 2026-10-30 (live-client re-pin to b90e2b9): upstream turned the raid's Battle Shout into a rank number (`RaidBuffs.battle_shout` int32:
  1 trainer rank 6, 2 book rank 7, 3 book rank plus the T2 bonus; "Fold the raid's Battle Shout rank into one four-state input"), so the
  buff ladder's `"battle_shout": "TristateEffectRegular"` failed every environments run ("buff battle_shout: not a number"; the mage's
  four races rc=1, the searches unaffected: the full raid clones the simulator's own FullRaidBuffs, rank 6). The ladder now sends 1, as the
  full raid. The pre-queue smoke test ran only the dummy race: after a re-pin, smoke-test `--env environments` too.
- 2026-10-31 (stage 1, mage): the ML `final` step starts from the record's stored talent-search winner (`bis-dummy-1`), made on the old
  trees; all five mage final steps stopped at once ("talents unknown to the simulator: Arcane Focus, Improved Fireball, Elemental
  Precision"). `ml_pipeline.sig_start` now also rejects a stored winner the current trees do not allow (unknown talent or illegal
  gating) and takes the same fallbacks (the spec's best open-search winner, else our raid build of the spec with the best full-raid
  number; that fallback used to take the first build listed). Audit the same day: every confirm class's (hunter, warrior, warlock, rogue,
  shaman) open winners are legal on the live trees; the druid's Feral winner is not (Berserk, Improved Shifting Power), but the druid
  runs a fresh search, which skips illegal starts. Lesson: after a tree change, check every stored start a later step reads (ML records,
  family winners, known positives), not only the builds the validator sees.
- 2026-10-31 (stage 1, druid): b90e2b9 renamed the feral rotations (`ui/specs/druid/feral{cat,bear}/apls/default.apl.json` ->
  `adaptive.apl.json`); our tuned rotations hid it until the bear's environments run fell back to the entry's `apl` ("cannot read ...
  default.apl.json"). specs.json points at the new files; the bear race was re-run by hand. After a re-pin, check that every path in
  specs.json exists in the clone (a two-line script found exactly these two).
- 2026-10-31 (stage 1, mage audit): the ML records' gear tier sets were chosen on the training dummy (`gear_tiers.make` passed "dummy"
  to optimize_set) while the pages rank by full-raid DPS; on the dummy a caster runs short of mana, so its stat weights differ (the
  Frostfire BiS set weighed haste at -0.14). Symptom: pre-BiS beat BiS in a full raid (Frostfire 742.9 vs 729.1, Arcane 728.0 vs 725.4).
  Test: the Frostfire BiS set chosen in a full raid measured +2.7% over the dummy's set (seed 2 confirmed) and +1.4% over the pre-BiS set
  competing in the same pick. `make` now chooses in the raid setting (`setting="raid"`, recorded in the gear record); the five mage and
  the druid Balance final steps run again (`deep-runs/ml_gear_raid_redo.sh`). Every class after them picks its sets in a full raid.
  Check at every audit: a pre-BiS number above the BiS number for the same build means the BiS set was chosen in the wrong setting.
  Open (same cause, larger scope): the entries' standard sets (`gear_opt.py`, the `p1opt` sets in specs.json, the gear of every race,
  search and the pages' main full-raid number) are chosen in `R.setting(e)`, the training dummy for damage entries. Re-choosing them in
  a full raid would move casters' page numbers by up to ~3% (the Frostfire test) but changes the gear every search of this sweep ran in;
  candidate for the launch-data run (gear_opt.py with the raid setting, then the searches), not mid-sweep.
