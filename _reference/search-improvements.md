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

## Changes made (with evidence)

| Date | Change | Why (evidence) | Effect |
|---|---|---|---|
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

1. **Rotations for new playstyles.** A build that needs a rotation nobody wrote is invisible. The spell probe only tries never-cast
   abilities of the winner. Idea: probe the abilities of the top 3-5 families too, and write a base rotation for any family whose
   keystone is an ability the entry never casts. Cost: a probe is minutes per ability.
2. **Leveling early levels.** The main leveling search scores level 60; the 20-60 polish is local. Idea: score the main search's
   finalists, or the top families, on levels 40-60 and polish the best three, not only the race's pick. Cost: about 3x per scored build.
3. **Certificate around the runners-up.** Certificates check pairs around the winner only. A runner-up family within 1% may hide a
   package. Idea: a light certificate (singles only) around the second and third families. Cost: 1-2 min each.
4. **Triples.** The checks are complete for pairs. Idea: combine the pairs with the largest positive interactions that share a talent
   into triples and measure them unpaid. Cost: small (tens of builds).
5. **Gear coupling.** A new family is searched in another spec's gear until it wins. Idea: give the top three families of each entry a
   quick phase-1 set (`gear_tiers.make`) and race them in it. Cost: about 10 min per family.
6. **Fight variety.** Done 2026-10-08: `raidsim/fight_variety.py` races each spec's pick and next builds in five full-raid fights
   (standard, three targets, Undead, 90 s, 300 s) and flags a pick 2% behind; the sweep's last phase runs it for every class.
7. **Model fidelity** (biggest real-game gap, not search): demon scaling and the pet hit rule are patched from the client's text and
   forum logs (2026-10-08) but unmeasured at level 60; the final beta build refresh; comparison with beta logs and real leveling times.
   Open after the 2026-10-09 audit, roughly by size (stacked enchants and the warlock's stones were added the same night): the lower
   proc chance of low ranks; leveling mob health from the client's ExpectedStat table (+7-35% over the lab's Classic medians; unknown
   whether the server uses it: a `MOB_HP_MULT` sensitivity); glancing and crit suppression against bosses (a beta tester's Skills
   panel shows them); negative resistance from debuffs (testable at level 30 with Curse of the Elements rank 2); Forever's Spirit regen;
   leveling gear from Forever's item database. (Crit per stat point by level now follows the client's table, 2026-10-09.)
8. **Weapon variants on the pages.** The rogue's swords entry found 18/33/0 at 746.6 DPS, +1.9% over our swords builds, but the Combat
   page shows one build per spec (the daggers build at 770), so a swords player never sees it. Idea: a weapon line on the page when a
   spec's entries differ in weapon type (swords, daggers, maces), each with its entry's best build. A page change, not a search change.
9. **Skip a sibling's checks when an entry's winner equals a finished entry's.** The rogue's Assassination entry ended on the daggers
   entry's 16/33/2 at the same DPS, and the two rotations are interchangeable for it (cross-rotation race +0.0%), yet both ran the
   certificate and the structural ranking. Saving: about 4 min per such entry; low priority.
10. **Mana-conditional spell ranks.** Retribution's lower Seal of Command rank pays only for mana-hungry builds: a rank line guarded by
   mana would let one rotation serve both.
11. **Spells the models leave out (audit 2026-10-08).** The fork ships five Forever abilities as stubs (Revive, Enchanted Flare,
   Confounding Flash, Contingency Plan, Divine Grace): none deals damage, so no raid number misses them. The healer lab casts neither
   Divine Grace nor Contingency Plan (priest baseline heals on 10-minute cooldowns): every priest build would gain about the same, so
   no talent choice moves. Low priority.

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
