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
| 2026-11-19 | `apl_opt.py --fresh` starts from the entry's base wherever it lives | The condition read `not entry["apl"].startswith("_reference/")`, so a fresh tune of an entry whose base is our own file (the warlock entries' new bases under `apls/warlock/upstream/`) started from the old tuned rotation instead; caught when affliction-raid's fresh tune logged "15 actions from affliction-raid-raid.apl.json". Lane stopped, fixed, resumed | No earlier `--fresh` tune of an entry with a base of ours is in the run logs or scripts (frost, frostfire, incinerate, melee hunter, arms-battle: their records start from their tuned files as ordinary continued passes), so nothing earlier is stale |
| 2026-11-19 | Each upstream build file races as its own rotation family (`deep-runs/warlock_upstream_race.py`, `raidsim/upstream_race.py`) | The independent audit's D1/D2/D4: the simulator now ships its rotations inside build files, and our tools raced its talents under our rotations. Each upstream rotation only works for its own build (our 30/0/21 Affliction builds 316 DPS under aff_wrack; the Wrack build 675 under ours): the same package effect the certificates cannot see | Wrack build +16.1% in its own entry; Demonology +8.0% from the rotation alone; Affliction's own builds +1.4% under sm_ruin |
| 2026-11-19 | Ice Barrier's Frost damage modelled in the fight lab and cast in the Frost raid rotations; a fresh audit session (`_reference/audit-brief-1119.md`) | The user asked why Frost skipped a talent that adds 15-20% Frost damage. Three gaps lined up: the fight lab coded the shield alone; no raid rotation cast it, so no search valued it and every Frost build stopped at 30 points; the duel lab had modelled it on 11-17 and the fix was never carried over | Frost raid page 533 -> 652 DPS; the leveling redo is owed. Any lab that models an effect another lab lacks must fix the other lab or log it in the work list the same day |
| 2026-11-19 | Lesson: an edit to a file a running lane reads (the Frost raid rotations, during the gear night) | The lane reached the mage hours before my estimate and the edit landed mid-way through its Frost searches; the run was stopped, the record cleared and resumed | Check the lane's exact position immediately before editing anything it reads, or wait for it to end |
| 2026-11-18 | The gear pools read the simulator database's `phase` field (`gear_opt.later_phase`): the pre-raid tiers take phase 1 only, Raid BiS takes phase-2 items only from Molten Core and Onyxia; Tier 0.5 is in neither pre-raid tier; Onyxia's quest rewards count unvetted; a third tier, Quests and dungeons (`gear_tiers.DUNGEONS`, `raidsim/dungeon_tier.py`) | The user's "our BiS list is a bit outdated" (Tier 0.5): the research found 15 later items in our sets, mostly Silithus-war quest rewards that presets vetted (Rockfury Bracers in 41 of 99 sets), and a rank-14 PvP mace in a BiS set. The pools had trusted community presets for items with no dated source, and those presets are not all phase 1 | Every set re-made by the gear night `deep-runs/gear_phase_1118.sh` (page-audit Q10-Q12). After a re-pin, compare the database's phase counts and check that no set holds a phase-2 item outside Molten Core and Onyxia |
| 2026-11-18 | `fightlab/fl_filler_pass.py`: a tie-break or "no loss" move never goes into a talent that only improves spells the build never casts in the lab (`dead_talents`: page_lint's tooltip reading against the lab's casts at 20-60; talent abilities are not judged that way), a dead talent's last points may move again, and `--dead-only` moves only dead points | page_lint's dead check after the eat-and-drink regen: the 2026-11-17 passes had moved Frost's last point into Accelerant (Fireball, Frostfire Bolt and Arcane Wrath only) and left Balance one Ferocity point. "Not a zero point" passed any talent the build did not hold, which was never measured, and "no loss" never moved a talent twice. A full re-run of the Frost pass also moved Cold Snap and Permafrost on 0.1-0.2% of noise at the user's main's next levels | Frost Accelerant -> Incineration (tie-break), Balance Ferocity -> Genesis (no loss); page_lint dead 0 |
| 2026-11-18 | `fl_open_search.py`: a rotation's 20-60 race also races the builds of the hybrids that level with it (`spec_modes.HYBRID_LEVELING_ROTATION`); `open_builds.py`: a hybrid whose rotation another spec's build won keeps its open build (its own race row, the signature check, 0.5% over the hybrid's other builds; `builds.kept`), and a chained leveling filler pass carries over when the record's winner is a state its one-point moves went through (`filler_applies`) | The eat-and-drink refresh of 2026-11-17 left the hunter's Beast-Survival page without its build: the melee rotation's race had raced Survival's builds only, and once our Survival build won, nothing was written for the hybrid (the fallback, an optimizer export, was 5.3% slower with 22 guide mismatches). Rewriting the hunter's open builds would also have dropped four of Survival's filler moves: the race had picked that build after the first of two chained passes | 22/4/25 kept at 21.00 s per kill (Survival 20.98); the hunter's rewrite changed no talents or orders |
| 2026-11-18 | A tool run for some classes keeps the other classes' rows of a shared record, each with the date of its own run: `raidsim/hit_below_cap.py`, `raidsim/unused_abilities.py`, `raidsim/apl_validate.py` (a failed bench is a `bench` row, not a missing one), `raidsim/pawn_raid_compare.py`, `characters/pawn_compare.py` (rows by class and level); the fourth to eighth tool after `heallab/heal_values.py` (2026-11-16) | The Windfury lane's `hit_below_cap.py shaman` wrote hit-below-cap.json with three specs (24 dropped), so weight_errors.py left 24 `hit:` keys out and the 06:14 GearCheck file lost their hit values; `unused_abilities.py <class> --write` had left its record with one class's rows after every lane since 2026-11-04 (32 rows on 11-02, then mage 2, paladin 2, hunter 8, warrior 1, none, none, paladin 2, warlock 15): the raid pages' "Talents with no line below" showed for one class at a time. A subagent read the other 30 tools that take classes and write JSON: three more cut their record (no lane ran them for a subset), the rest merge, write per class or always run every class | Records restored the same day (hit and its 24 error entries from 107eb67c, inputs checked unchanged; the unused audit re-run for every class); GearCheck's file made again. Lesser hazards (no lock, read before hours of measuring, never pruned) in page-audit Q5 |
| 2026-11-16 | `mage.EVO_BELOW`: the between-fight Evocation threshold is a rules knob (default 0.4, the regression); 0.15 in the five mage leveling rules files (`fl_evo_1116.sh`: continued tunes, records from the race on, filler, weights, GearCheck, rest cues 0.40 -> 0.15) | The user asked why 40%: a literal no tune compared. Evocation restores 70-118% of the pool by level; an A/B of every mage leveling pick (20,000 fights, seeds 1-2, levels 20-60) put 0.15 ahead of 0.40 by 0.6-1.1% per kill, 0.10 behind | Frost's tune also took eat_below 0.40 (+0.4%; it had none, so 65%). Level-weighted: Arcane/Frost 28.3 -> 27.8 s, Frost 29.5 -> 28.9, Arcane 29.4 -> 29.1, Frostfire 33.8 -> 33.4, Fire 36.0. Builds moved a point or an order step: Fire's order shifted a level from 30 (Heating Up 45, Combustion 60) |
| 2026-11-16 | Character planner: an item with no required level in the Forever database or Classic's takes Blizzard's static item API's (cached); an item Blizzard does not know is left out | The re-pin to 2e6e77d84 brought 192 such items with sources, read as wearable from level 0: Arcea's level-37 plan bought the Sorcerer's Regalia, an item-level-60 epic set (Blizzard: 404) | GearCheck's pool needs a required level and takes greens and blues only: unaffected |
| 2026-11-16 | `heallab/heal_values.py <classes>` keeps the other specs' rows, each with its own date; `addon_values.py` skips a page-stat-weights row whose build the spec's ML record measured | `heal_values.py druid` had written the druid's row alone, so the 19:07 add-on file had no paladin, priest or shaman heal entry (restored 19:30); the Addons session found two raid entries listed twice (paladin ret-full-buffs-raid, rogue hybrid-assassination-subtlety-open-raid) | Nothing changes in game; the duplicates leave with the next add-on file |
| 2026-11-16 | Two server hotfixes into our text (`hotfix_text.SHAMAN_PUSH_114027`, `DRUID_PUSH_114015`): Mental Dexterity 50/100/150% -> 33/66/100% of Intellect as attack power, Wild Growth's coefficient 3.3% -> 6.6% a tick; the shaman's leveling redone (`fl_hotfix_1116.sh`: rules, records from the race on, filler, guides, GearCheck values) and the Restoration druid's healer search (`fl_druid_1116.sh`) | Found at the re-pin to 2e6e77d84: `sim_value_audit` listed Mental Dexterity (tooltip 150, curve 100), then the spell-data diff of the two pins showed Wild Growth's SPCoef. Blizzard's written 11-10 notes list neither; the simulator took them from hotfix pushes 114027 and 114015 on 2026-11-12. In the fight lab the shaman's picks were 0.4-2.5% too fast | Elemental's rules kept; Enhancement's put Rockbiter back from 40 (was 54: +0.4% at 40, +1.2% at 50); builds unchanged but one late filler point each; Intellect's leveling value 20-30% lower for Enhancement. Druid: running |
| 2026-11-16 | No marking point for the Restoration shaman's leveling path (rejected) | GearCheck's pick ties Restoration's path with Elemental's pick at 10-22 (identical talents, different rotations: caster values for a melee player) | Thundering Strikes first was 0.1-0.8% slower at 10-14 and 2.7-3.9% at 16-20 (Mindfulness at 15 matters); both builds' fastest start is the same, so GearCheck's one-time tie note (v0.2.4) covers it |
| 2026-11-16 | `fightlab/warlock.py` plays the reworked **Wrack** (Blizzard's hotfix of 2026-11-10, `hotfix_text.WARLOCK_1110`): a 6 s channel of 60 Shadow damage a second at 60 (25.2 + 1.75 a level from 40, `WRACK_PER_LEVEL_1110`), 20% of spell power a tick; while it channels, Corruption, Siphon Life and Bane of Agony also tick on their half points, each a full tick, expiry kept (`_wrack_half_ticks`, as upstream's wrack.go); `TICK_FOR` reads the duration-first wording | The 70938 live pull showed the new wording; the raid simulator had it since our pin ff9babba5, while the fight lab, the duel lab and our text kept the 70753 Wrack (86 a second and +10% to the other dots) | The old text plays bit-identically. Affliction's rules re-tuned (continued installed): Shadow Bolt and Fear never, Wrack only above 30% mana, the rest kept; 34.08 -> 30.61 s weighted (20: 30.6 -> 23.5, 30: 38.8 -> 28.6, 60: 32.2 -> 31.7). Without bolts a kill costs a third of the mana and the 7-10 s of drinking a kill at 20-30 go (scratchpad wl1116/why_no_bolt.py); the open search kept its build; the filler pass made it 40/10/1. Wrack and Siphon Life are now the build's most valuable talents (3.5 and 3.4 s a kill at 60) |
| 2026-11-16 | `build_forever_spells.py` applies every live pull, oldest first (`live_spells.all_pulls`), not only the newest | A pull holds the changes against the text of its own day: the 70938 pull took nothing, so applying it alone would have dropped the 70888 pull's 116 changes at the next rebuild | Today's data unchanged |
| 2026-11-16 | `paladin.py` rule knobs (idea 0h): `CASTER_GEAR_FROM` (the Holy path's gear row: caster gear from a level; 0 = from Holy Shock on, as before; 61 = never) and `SOR_FROM` (Seal of Righteousness over Seal of Command from a level; 61 = never, as before); both in `duel.PVE_KNOBS` | The 0h measurement of the same day: melee gear 6.3-6.5% faster per kill over 30-60 for the Holy rotation's two page picks; Seal of Command's edge depends on the gear | `holy-leveling` re-tuned on the Shockadin (from scratch installed): melee gear at every level (+5.3% and +5.1% on the two seeds), Holy Shock only while the mob has more than 35% health, eat below 80% (drinking back at the module's quarter of the mana); 31.13 -> 28.90 s weighted; Seal of Command kept. Protection and Retribution kept their saved rules. Records redone from the race on (`fl_paladin_1116.sh`): Shockadin 21/0/30 28.90 s, Protection 29.21 s, Prot-Ret 25.88 s |
| 2026-11-16 | The paladin's seal judgements at the character's level (idea 0i): `spell_scaling.REFERENCED["paladin"]` (Seal of Command, of Righteousness, of Fury) writes "judgement" rows from the direct effects of the referenced "Judgement of <seal>" spells; `paladin._level_judgement` scales `judge`, `judge_stunned` and `fury_judge` by amount(level) / amount(60) | The 0i scan: Seal of Command rank 1's judgement read 45% high at 20 (the scan's 44% for Seal of Fury had read a dummy effect) | Bit-identical with the scaling off; identical at 60 and in duels; 0-6.5% slower per kill below 60 (Retribution 19.0 -> 20.0 s at 20, 25.7 -> 26.6 s at 40) |
| 2026-11-16 | `fl_filler_pass.py` keeps signature talents (`signature.granting_talents` of the spec's required spells; record key `kept_signature`) | The Shockadin's first pass moved **Holy Shock** to Deflection (3.8% faster per kill in melee gear, two seeds), after which Divine Favor, Infusion of Light and Oath of Light read "no loss"; `level_guides --check` listed 23 errors | Lane stopped before any weight file was written, the record deleted, the build restored by `open_builds.py --only leveling` and `order_repair.py`; a scan of every filler record found no other signature move |
| 2026-11-15 | `live_spells.to_level60` brings the numbers a rank's description takes from another spell (`$16361s1`, `$/2;20966s1`) back to level 60, not only its own effects; the 70888 pull's archive regenerated offline against the pre-live text (`raw/2026-11-10-live-70888/`), forever-spells rebuilt | The poison and imbue check (user, 2026-11-15: "go with your recs"): Windfury Weapon rank 4 read 433 extra attack power, the beta client's level-60 text and the raid simulator 333 (Wowhead's number at the spell's MaxLevel 68). A scan of the pull's 125 taken ranks against the referenced spells' level rows found eight such: Windfury 4, Rockbiter 7 (686 for 653), Frostbrand 5 (203 for 169), Seal of Command 5 (+14%), Seal of Fury 7 (+10%), Light's Vigil 3, Holy Nova 6 (heal, +2%), Dire Bear Form; and a ninth where Wowhead wrote the level-64 number inside its arithmetic, Flametongue Weapon rank 6 ("( 3122 / 77 - 1 + 0)": 40 to 125 for the client's 35 to 112; such a number is brought to 60 before the arithmetic is worked out) | 116 taken ranks unchanged, exactly those 9 back to the client's numbers (the shaman's file swapped in by rename, as the lane and the duel lab were reading it). The duel lab plays them at 60 (the shaman's Windfury, the paladin's judgements): the PvP search queue was stopped and restarts on the corrected data (`pvp_restart_1115.sh`) |
| 2026-11-15 | The shaman's weapon imbues at the character's level: `spell_scaling.py --referenced-only` writes rows for the ranks whose numbers live in referenced spells (Rockbiter's passive and Windfury's proc aura: attack power; Flametongue's proc: the per-swing amount; Frostbrand's attack: damage) from the official simulator's store; `tables.rank_amounts`; `shaman.level_imbue` | The same check: spell_scaling.json (2026-10-18 row 8) holds a rank's own effects only, and an imbue's cast has none, so each rank read its top number from the level it is trained (Rockbiter rank 5: 355 against the client's 212 at 34; Windfury rank 1: 103 against 46 at 30) | The default shaman unchanged at 60, slower or faster below it by the imbue's share; the knob comparison fair (with it: Rockbiter best at 12-28, Windfury at 30-48, Rockbiter again at 50-60 by 1-2% per kill on the Enhancement page build; Elemental within 1%) |
| 2026-11-15 | Rule knobs for two more player choices (idea 0h): `rogue.POISONS` (the poison on each hand: Instant/Deadly as before, Instant on both, the off hand Instant until 30, Deadly on both, Deadly main hand) and `shaman.IMBUE_EARLY` / `IMBUE_LATE` / `IMBUE_TOP` / `IMBUE_TOP_FROM` (the imbue before 30, from 30, and from a level: Rockbiter, Windfury, Flametongue, Frostbrand; picked in make_player, so a rules file reaches it). Flametongue's damage follows the weapon's speed (the simulator's rule; it was a roll over the tooltip's range), rolled like a spell; Frostbrand at 9 procs a minute (an assumption: Classic's, as the simulator carries it). All in `duel.PVE_KNOBS` | The user: "Go full power, go with your recs" (the recommendation: rogue poisons and the shaman's imbue first). A 300-fight look: Instant Poison on both hands 1-1.6% faster per kill at 24, 40 and 60 on the Combat page build | Defaults bit-identical (rogue: 36 fight-lab rows and 18 duel matchups against HEAD copies). Lane `deep-runs/fl_knobs_1115.sh`: every rogue leveling rotation took POISONS = 1, Instant Poison on both hands (Assassination +1.4-1.7% per kill, Combat +0.9-1.1%, Subtlety +0.8-1.0%; Assassination's rules also dropped Kick, +0.4-1.0%); the shaman's and the paladin's tunes kept their saved rules. A direct A/B (3000 fights, two seeds) then put Rockbiter back from 54 in the Enhancement rules by hand (0j). Records from the race on, pages, GearCheck values. The final records (2026-11-16 00:48) moved two pages: the shaman's Elemental winner is pure Elemental 32/11/8 (the 26/22/3 Elemental-Enhancement hybrid 2.6% behind: no hybrid leveling page now), and the paladin's Holy winner is the Shockadin 22/0/29, 6% ahead of the Holy-Prot 21/16/14 it replaces (new guide; its caster gear and seal measured, 0h) |
| 2026-11-15 | `rebuild.py`'s regen step writes the report index of every class, not only the classes it was given | Review of the Mage Armor lane before its commit: `render_builds.py` (no class argument) rewrites every class's classic-baseline README whole, which drops its "Report index" section, and `render_report_index.py` ran only for the regen's classes, so a mage-only regen took the index off the other eight classes' pages (93 lines; the diff showed them as deletions) | Restored before the commit (`render_report_index.py` for all nine classes, the eight READMEs back to their committed text); a class-filtered regen costs about a minute more |
| 2026-11-15 | `mage.py`: the armor is a rule knob (`MAGE_ARMOR` in `ROTATION_KNOBS`: Mage Armor from 34, Ice Armor or Frost Armor before; Mage Armor's share of regeneration while casting read from the rank's text, 50% at every rank in Forever). `rules_retune.py --continued-only` skips the from-scratch half (a new knob on mechanics the saved rules were tuned on the same day) | The user asked "Mage armor or ice armor?" for a level-34 mage: the module had always worn Ice Armor and no search had compared the two. An A/B on the Arcane-Frost page build: Mage Armor 2.5-4.8% faster per kill at 34-40 (drinking 6.5 -> 3.4 s a kill, eating 1.8 -> 3.1 s). A choice the module makes for the player belongs in the rules search (as `PYRO_OPENER` does) | Continued tunes (deep-runs/fl_mage_armor_1115.sh) took it for Frost (+1.8%), Arcane (+2.1%, with drink 15% / eat 40% where the defaults had stood), Arcane-Frost (+0.4%) and Frostfire (+1.4%, plus Frostfire Bolt only above 15% mana); Fire kept Ice Armor. On the final builds, same fights (600 x 2): 0-5% faster per kill at 34-60 on single pulls (most at 34-40; Arcane-Frost even from 50, with Arcane Meditation complete); 9-20% slower in pulls of four, so the AoE variant (no rules file) keeps Ice Armor. Filler passes moved points that fed only Ice Armor (Frost Warding) and four others; records re-raced from the 20-60 race on, guides, steps and GearCheck values redone |
| 2026-11-15 | `paladin.py`: no module hold on offensive Holy Shock (`shock_mana` 0.70 -> 0; the tuned rules may still gate it at 15% mana, the signature rule's cap) | The Holy page's leveling build cast Holy Shock 0.19 per kill at 30 and 0.28 at 40 against the signature rule's 0.5 (FAIL in the signature audit since at least 2026-11-09, with tuned rules and without), and the open search's Holy winner failed the same way, so it was never written: the module's 70% hold (a 2026-09-30 hand sweep) sat outside the rules, whose mana gates on a required spell are capped at 15% | A/B on the page build under the saved rules (60 fights, seed 1): Holy Shock 0.17 -> 2.12 per kill at 30 (31.5 -> 33.2 s per kill), 0.25 -> 2.30 at 40 (36.3 -> 39.5 s). The paladin's holy-leveling rotation is redone before the queue's tail (`deep-runs/fl_redo_pal_1115.sh`: rules tune, record from the 20-60 race on, finish) |
| 2026-11-15 | `rotation_opt.search`: the signature floor a rules tune enforces comes from the tuning build's `spec` field when it has one (`spec_modes.spec_of`, as the pages and the signature audit judge it), else from its points (`fl_signature.spec_for`) | The fl_fix_1115 queue re-tuned priest `discipline-leveling` on the Discipline page's raid-path build (29/22/0 since a point moved on 2026-11-09; `spec` Discipline). Judged by its points as the Smite hybrid, it was tuned to that floor (Smite and Holy Fire 50% of the damage; Discipline's own floor is Penance, Smite, Holy Fire and Mind Blast at 40%): Devouring Plague never cast, Penance and Mind Blast held back, 46.17 -> 57.58 s per kill on the build (the saved rules had Smite and Holy Fire at 8%). Of the saved rule files only priest Discipline and Holy differ between the two judgments | The queue stopped at 05:50 during its priest Shadow tune; the Discipline rules restored to the committed ones and re-tuned under the fix (`deep-runs/retune_priest_1115.sh`), then the queue resumed. The Holy rules stay as the queue tuned them: `holy-leveling` also plays the Smite page's build, whose 50% floor is the stricter (future tunes of it: on `smite-open-leveling`) |
| 2026-11-15 | `fl_levels.order_polish`: after a kept step, a move that failed its confirmation is skipped when it changes the same builds at the same levels (`delta_key`: the levels where it differs from the current order, with both builds there) and its stored seed-14 difference still fails against the current order's seed-14 score; record `repeats_skipped` | Self-audit after the twins fix: of the logs' 422 unconfirmed order-polish rounds, 91 repeated an earlier failure's exact numbers after a kept step (the kept step changed other levels, so the move came back under a new `at_levels` key and the twins check, keyed on absolute scores, missed it); the redo's mage Arcane polish did it again at 04:39. The time at a level depends only on that level's build (the full build is the same for every order, and `FS.order_ok` keeps every candidate's signature timing legal), so the difference is exact | Fake objective (112 runs on the warlock, mage, paladin and rogue records): 110 bit-identical, 2 replaced a doomed re-test with a fresh candidate; repeated failures 1 -> 0, kept steps and final quality equal. Real-lab smoke with a lenient bar ran the kept and failed branches. Applied mid-queue at 04:44 (the queue's later rotations and the redo's paladin, rogue and hunter runs; the redo's running mage process keeps the carry version) |
| 2026-11-15 | `fl_levels.polish`: when the race's pick plays an order of its own (the previous record's winner, our build), each neighbour carries that order through the move (`carry_order`: the points the move takes away free their slots, a talent's last ranks first; the added points take them, the shallowest row first; a list schedule then gives each slot the first point of that wish list that keeps the build legal) instead of the stats model's order for it; records `level_polish.neighbour_orders`, a kept carried order's `order_label` "carried" (pick_order then computes the stats model's order for the new build) | Self-audit during `fl_fix_1115.sh`: the reference played its own order and every neighbour the stats model's, so each neighbour started behind by the gap between the two orders. The 12 polishes in the logs from such a pick kept no step (75 of 169 from the stats model's order did); their best neighbour read a median 2.4% slower against a median gap of 2.3% at 20-60 (warlock Destruction 8.2% against 7.2%, Demonology 6.1% against 5.5%). The pick plays its own order more often than the order lines showed (an own order equal to one of the three variants races under that variant's name): in tonight's queue all five mage rotations, rogue Combat (swords) and the hunter's melee rotation started that way, their best neighbour 1.0-2.5% slower | On every record, 5,801 sampled neighbours all carried to a legal path that spends the neighbour's points (3,746 in place, 2,055 repaired by the schedule; a first version without the schedule left 32% uncarried). Fake objective with an order-sensitive time (44 own-order runs on the warlock, mage and paladin records): kept steps 77 -> 149, true gain summed 73% -> 128%, new better in 31 runs, worse in 11 (path dependence); from the stats model's order 44 of 44 runs bit-identical. Real lab: mage Arcane's first carried round kept 33/0/18 (-0.86% on seed 12) where the queue's polish had found nothing. Applied mid-queue at 04:33 through `fl_open_search._load` (priest, warrior and the rogue and hunter one-tree records use it); `deep-runs/fl_redo_1115.sh` redoes mage, rogue and hunter (and paladin's old order polishes) before the queue's tail |
| 2026-11-15 | `fl_levels`: the order polish scores each set of builds at levels 30/40/50 once (`at_levels`, `order_moves(skip=)`); in both polishes the batch's best that fails its confirmation stays out with every candidate of exactly its seed-1 score (twins), and the rest of each batch waits in `pending` until a step is kept | Self-audit during `fl_fix_1115.sh`: the logs' order polishes had 414 unconfirmed rounds, 323 of them with an earlier round's exact numbers (the same order drawn again, another with the same builds at the scored levels, or a point moved between talents the lab never uses); 73 of 208 order polishes ended on such a repeat, the batch's runner-up never confirmed. The 20-60 polish: 38 of 259 | On a fake objective with dead talents (24 order polishes, 12 polishes; old against new): order-polish confirmations 45 -> 19, repeats 34 -> 0, kept steps 3 -> 4; one batch of 30 moves had held 11 distinct builds; the 20-60 polish unchanged where nothing blocks (43 kept steps both). Applied mid-queue (02:21) through `fl_open_search._load`: paladin Holy and Protection, mage Arcane, Fire, Frost and Barrage-Frost ran the old polish |
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
| 2026-10-31 | `apl_opt` drops a tuning build the simulator rejects, and says so | A stale race report named an old-tree paladin preset: every candidate scored None, three rotation searches tried nothing ("no candidates") | Searches after a tree rework tune on real builds |
| 2026-10-31 | Rotation-lag audit after a re-pin: our tuned rotation raced against every upstream rotation of the spec folder (full raid, two seeds) | Upstream's new rotations beat ours: Fire +2.8-4.5%, Frostfire +1.1-2.2%, Feral Cat to +1.0%, Combat daggers +0.6-0.8%, paladin 5-6% | Adopted as the entries' base, re-tuned as a pass |
| 2026-10-31 | `repair_builds` drops a talent that moved trees instead of following it | Following Holy Conduit into Holy bought 9 useless Holy points in the paladin tank build | Repaired builds stay in their trees |
| 2026-10-31 | Simulator talent comments as a tooltip source (`refresh_forever_talents --sim-text`) | The paladin export's rank texts were estimates (Spiritual Focus 175%, Champion "100%"); a fight-lab regex read Sacred Duty as +30% Stamina | Per-rank numbers match what the simulator plays |
| 2026-10-31 | `family_search --reuse-polish`: a restarted first search reuses the entry's polished families when the cache is newer than its raid rotation | The pause at 20:33 stopped the melee hunter search after its 168-minute polish | Saves the polish on a resume |
| 2026-10-31 | Pausing a queue: stop the bash wrappers and their subshells before the python and simulator processes | Stopped searches returned an error and the scripts ran the next step (the warrior's open builds before its structural ranking) | Steps run in order after a pause |
| 2026-11-01 | Structural ranking pads short splits to 51 with dead talents when the exact splits give fewer than `--top` legal structures (`structural._pad`, `MAX_PAD` 30) | Every druid ranking since the first raid pass ended "no legal structure": the live talents plus the minimum tier fillers never summed to 51 (Balance entry: 12 live in Balance, 2 in Restoration, 0 in Feral), so neither druid entry was ever checked | Balance: 300 legal structures, model-simulation correlation +0.92, confirms 33/0/18 (85 min); classes that reached `--top` at 51 are unchanged |
| 2026-11-02 | `deep_heal.py`, `deep_tank.py` and `deep_opt.py --fresh` move the old record to `<record>.prev.json` at start, not at the first save | The queues' `fresh()` gives `--fresh` once and resumes without it; the druid's Restoration search, started fresh on 10-31 and killed by the pause inside its first cycle, had never saved, so the resume loaded the 10-21 record as done and rewrote its stale build (old tree layout: Heart of the Wild in Feral Combat, Furor in Restoration), which failed validation and replaced the repaired 11/4/36 | Druid files reverted, search re-run fresh; the paladin's Holy search had saved a cycle before the pause and resumed correctly; `deep_opt.py` had the same load and gets the same fix |
| 2026-11-02 | Open item (not fixed): the shaman's open search loses a seeded 29/22/0 lead | Sweep on 54ceac638: the synergy certificate's lead 29/22/0 (Stormstrike + Mental Quickness) raced +2.2% (Elemental entry) and +2.6% (Stormcaller) over the winner; the re-search seeded with it ended at 31/11/9 (554.1) and 32/11/8 (541.6) again, and the confirm pass's certificates found the same lead (+1.95%, +2.42%). The page build elemental-raid-dps is 29/22/0 already (564.4 in a full raid), so no page is wrong; the search's own winner is 1.8% short | Check whether the lead survives `ml_talents` start validation (protected-talent rule, `kept: Elemental Focus`) and the first race stage; a seeded lead should at least reach the finalists |
| 2026-11-02 | Status check after the 70707 sweep: three gaps, queued in `deep-runs/tonight_1102.sh` | (1) The sweep's leveling half ran only certificates around the open leveling records of mage, druid and hunter, which date from 2026-10-19..24 (trees before the 10-30 hotfix); its open-builds step then wrote six illegal leveling builds (Arcane Focus, Improved Fireball, Berserk, Critical Mass at 5 ranks) and the page regen failed validation. A class whose trees changed needs `fl_open_search --fresh`, not a certificate. (2) The priest was in neither the sweep's FULL nor its CONFIRM list and never ran after its 10-30 port. (3) `paladin_stage2.sh` ran `raid_path_leveling.py` without `--write`: the paladin's healer and tank leveling builds still follow the old raid picks | Illegal builds reverted to the committed ones; the queue runs the fresh leveling searches, the priest's full pass and `raid_path_leveling --write` for druid, priest and paladin. Lesson: a sweep's class lists must cover all nine classes, and every record a step reads must postdate the data refresh |
| 2026-11-02 | `deep_heal.py` and `deep_tank.py` write the builds file through `builds_io.update` (locked) | They read and wrote `proposed-builds.json` unlocked; tonight's queue runs the priest's healer search next to its raid steps, which write the same file | No measurement |
| 2026-11-02 | The bench reads both buff names across upstream's 2026-11-01 rank work (`foreverbench/main.go` `fieldAliases`; a rank select takes true as 1, a bool field takes a number) | bac92dbd5 renamed four raid buffs (Gift of the Wild -> mark_of_the_wild ...) and made four rank selects (0 off, 1 trainer rank, 2+ book): our configs died with `no raid, party or individual buff field "gift_of_the_wild"` | Rehearsal on bac92dbd5: feral smoke race runs; apl_validate: no new warning |
| 2026-11-04 | Entry options use the official protos' names (hunter `petAttackSpeed` FasterAttackVI, `quiverBonus` AncientSinewWrappedLamina; two stray Enhancement fields removed); `raidsim/spec_check.py` checks every entry's spec fragment against the proto files statically; `run.check_bench_stderr` makes the bench's `spec:` warning fatal in every caller | The bench dropped the fork's `OneTwo` and `Speed15` silently (DiscardUnknown; the warning only reached a log when a bench was killed at the 11-04 reboot): every hunter raid number since the port (2026-10-18) had a 2 s pet without its Faster Attack passive and no quiver haste | Hunter raid lane redone from its races; nothing of the kind can pass unseen again |
| 2026-11-04 | Capped queue runs pin processes by type: `deep-runs/rebalance.ps1` (benches and every other queue python BelowNormal on 6 of the run's 8 cores; fight-lab and healer-lab python and their workers Idle on all 8) applied every 60 s by `deep-runs/balance_1104.ps1` next to `resume_1104.sh` (throttle.ps1 keeps the whole tree off the desktop's 4 processors) | Under one shared mask and priority the two Go benches had 0.3 of the 8 cores and the 12 fight-lab python workers 7.3 (the hunter rotation re-tune's bench: 0.1 CPU-seconds per 8 s, 2.7% of its work in 62 min; with the workers at Idle for 12 s it took 5.2 cores): on Windows the simulator's threads lose to CPU-bound python at equal priority | Benches 5.3 cores, fight lab 2.6, total CPU unchanged at 71-75%: the raid lanes run at near the cap's full speed and the leveling lanes take what they leave plus 2 cores of their own; the fight lab gets every run core once the raid lanes are done |
| 2026-11-06 | Priest leveling refresh lane next to the patch queue (`deep-runs/priest_refresh_1103.sh`, `priest_refresh_keys.py`): the open record taken back to the end of each level-60 search, then the search tool's own stages from the 20-60 race on, the open builds, orders, races and reports | Self-audit at the warrior and druid boundaries: no priest leveling number on any page since the 2026-11-02 checkpoint (records of 2026-10-23, older than the capture date; the patch queue lists the eight changed classes). Its rules (2026-11-02) and winners (certificate of 2026-11-03) were already checked on its current data, so no new level-60 search. `fl_open_search.py` gates every stage on its key, so "refresh from the race on" is a reset of those keys and a plain run (`page-audit.md` K1) |
| 2026-11-06 | `order_repair.py`: a solo build whose order a repair dropped gets the stats model's leveling-st order back (no race). `render_modes.weighted`: levels 20-60 only. `spec_modes.HYBRID_NAMES`: the druid's "Cat (split)" | The druid's recommended leveling page had no talent table since 2026-10-30 (`opt-feral-cat-dps-solo-60`) and six other solo builds were order-less; the druid's level-15 report row put report builds and race-row builds on different level sets (23.6 against 23.07 s for one build); the cat rotation's 11/29/11 winner carried the fallback hybrid name (`page-audit.md` K2-K4) |
| 2026-11-06 | `fightlab/rules_retune.py <class> <rotation> <build>`: one rotation's rules from scratch and continued from the saved file, the fastest set installed only when it beats the saved rules by 0.3% on the tuner's final check. `deep-runs/rules_repair_1103.sh` runs it for the rotations the rules step skipped (rogue Subtlety, paladin Holy and Protection, mage Arcane and Arcane-Frost, warrior Protection, warlock Demonology once lane C has saved it); `deep-runs/refresh_keys.py` takes a record's rotation back to the end of its level-60 search for the re-races | Open idea 0e: eight rule files predated their class's patch port. The tool also closes the open item of 2026-10-27 on main (a from-scratch run wrote its result even when the saved rules were faster). Smoke-tested on Subtlety (tiny budgets, dry run) |
| 2026-11-06 | Warlock Destruction leveling rules replaced at 07:21, before the patch queue started that rotation's open search (07:16: the Demonology rotation was in its order polish): the first six rounds of a from-scratch tune on `destruction-open-leveling` (never cast Fear, Drain Life, Searing Pain or Incinerate; Shadow Bolt only above 35% mob health; eat below 40%) | Seed 3, 3,000 fights per level, levels 20-60: hand-written 49.47 s, the rules of 2026-10-24 45.60 s, the six rules 41.48 s (9.0% faster than the old file; 6.5% at level 60, where the search scores). The old rules still cast Incinerate and Fear, so the search would have valued talents for a rotation the tuned rules never play. The tune was stopped after round 6 (the search was minutes away and a rules file must not change under a running search); after the search: `rules_retune.py warlock destruction-leveling <winner>` and, if it gains, the record from the 20-60 race on |
| 2026-11-06 | `fl_open_search.py`: the 20-60 race's eligible picks now include the previous record's winner of the rotation (`<record>.prev.json`) and our raced builds of the rotation's specs, each with the order it carries (`picked_by` says so; `order_label` "previous"; the stats model's order is computed for the order choice). Not with `--no-known` | Self-audit at the warlock's Demonology save. The fresh Affliction search of 2026-11-04 ended on 38/11/2 at 36.78 s while `affliction-open-leveling` (37/14/0, the winner it replaced, with its polished order) ran 36.20 s in the same race, and `open_builds.py` would have rewritten that build from the slower record at the lane's builds step (its "confirms the spec's open build" branch; dry run: "Affliction 36.78 s per kill -> new build"). The note of 2026-10-28 called this harmless on main; it is not when the faster build is the spec's own open build. Smoke test on a copy of the record: the previous winner is picked (35.90 against 37.49-37.53 s at 200 fights) and its order beats the three standard ones (stats model 37.14, own tree first 36.69, own tree last 38.11). Lane C's warlock process had loaded the old code: `deep-runs/rules_refresh_1103.sh` races the warlock's three rotations again after its class steps. Every other finished rotation checked the same day (`deep-runs/fightlab/prev_check.py`: the previous winner with its order on the race's seed and fights): 10 previous winners still legal, none both 0.5% faster than the new winner and passing its check (druid Balance -0.8%, cat -0.3%, Marksmanship -0.5%, melee hunter -0.1%, priest Holy -3.4%, Shadow -0.5%, Enhancement -0.2%, warrior Protection -1.1%, Survival-only -0.7%; Beast-Mastery-only +0.7% but at a core share of 34% against 35%), 14 no longer legal after the patch |
| 2026-11-06 | **Signature talents as early as the tree allows** (user decision, page-audit L3): `signature.late_talents` (check), `signature.signature_first` and `fl_signature.sig_order` (the order every leveling tool starts from), `fl_signature.order_ok` (the order polish keeps only such moves), `order_repair.py` (hand drafts and exports). The stored verdicts carry the check's version and rules (`build_fingerprint`), and `open_builds.py --write` measures the class's audit first | The checks counted a talent spell from the level the order takes it and orders were picked on speed, so Assassination took Mutilate at 60, Subtlety Hemorrhage at 54, Beast Mastery Bestial Wrath at 56, Discipline Penance at 51, the Holy paladin hybrid Holy Shock at 60. Cost of the rule where measured: Assassination 1.8% (22.46 against 22.06 s), Discipline about 4% on a small test |
| 2026-11-06 | **A path's level is judged as the build's own** (page-audit L12): `fl_open_search._ttk` takes the build's full allocation and order as an 8th job element, `fl_levels.evaluate` passes it | The 20-60 polish and the order polish read a level before the signature talent as "talent missing" (x0.45) and filed a hybrid's partial build under another spec: a Subtlety order move scored 22% faster and lost the plain 20-60 race; after the fix the same polish kept a move worth 1.3% that held (21.18 -> 21.09 s) |
| 2026-11-06 | **Save points for the level-60 block** (open idea 0c, user decision): `fl_open_search.SimCache`, `sim_fingerprint`, `LabSim(cache=)`. Every `LabSim.run` result is appended to `open/cache/<class>-<rotation>.simcache.jsonl` (first line: a hash of the engine, tables, class modules, signature rules, tuned rules and data); deleted when the winner is saved; `WOW_FL_SAVEPOINT=0` off | Four blocks of 5-20 h were lost to pauses on 2026-11-04/05. Test: a small search (8,307 simulated builds) run twice with the file kept: the second run read 8,360 results back, simulated none and ended on the same winner and numbers; the polish and the search are deterministic from their seeds, so the replay is complete |
| 2026-11-06 | **Fire's Pyroblast opener** (user decision, page-audit L2): `mage.PYRO_OPENER`, a rule knob; `rules_retune.py` and `rotation_opt.search` record whether the tuning build casts every required spell (`played_before`, `played_after`) and a set that plays wins over a faster one that does not | The saved Fire rules never cast Pyroblast before Heating Up and were 0.4% faster than the same rules with the opener: a comparison on speed alone would have kept them |
| 2026-11-06 | **Gear repair wired into the raid lanes** (user decision, page-audit L7-L8): `deep-runs/gear_repair_1103.sh`, `gear_redo_1103.sh`, `raid_rest_1103.sh`, `ml_clear.py`; `raidsim/gear_check.py` (static: items and enchants a set lists that the database lacks, tier-set items outside the pool); `run.check_bench_stderr` stops a run that reports `missing_gear`; `gear_opt.LATER_FACTIONS` | 14 entry sets listed dropped items on every checkout (gear_check, 2026-11-06). A dry run of the shaman's sets on tiny budgets replaced the dropped items and the Signet Ring and wrote nothing |

## Tested and rejected

| Date | Idea | Test | Result | Decision |
|---|---|---|---|---|
| 2026-10-07 | Warm-start each pair's polish from the sibling entries' polished family | Shaman Stormcaller, 8 pairs, 150 fights, same random draws, separate caches | 80% fewer builds, same best family; 4 of 8 families 5-9% worse, 3 better (a climb from a sibling's optimum stops there) | Rejected as a polish start; the sibling families became extra search starts instead |
| 2026-10-07 | Rank-3 Seal of Command on Retribution's twist line | Rotation search | Best for mana-hungry builds, but costs the hand draft 0.6% | Rejected by the protection rule; a mana-conditional rank line stays open (below) |

## Open ideas, ranked by what they could still find

1e. **The filler pass's ping-pong guard had two holes (2026-11-22; the audit session's question on Arcane's level-10 point; fixed the
    same day)**. The record chain (2026-11-21) loaded only when the record's order was the build's order, so every redo that re-raced the
    order (the mechanics pass of 2026-11-20, the rest-rule redo of 2026-11-22) started a new chain without saying so; and the gate path (a
    gate point's measured move, 0.05% on both seeds) never read the chain at all. Four reversals in today's records, each undoing a move
    made on an earlier model: Arcane's level 10 (Arcane Resilience -> Wand Specialization on 2026-11-20 at -0.13% / -0.33%, back today at
    -0.36% / -0.23%), Shadow's 52 (Twilight Focus <-> Early Demise) and 56 (Power in Light <-> Mental Strength), Elemental's Concussion and
    Reverberation (43, 53). The rule now, as the audit session put it: a change of model resets the chain, and the first pass on the new
    model is then held by its own moves. fl_filler_pass.py stores the model fingerprint (fl_open_search.sim_fingerprint) and the chain's
    state in the record ("model", "chain"); a record with the same fingerprint binds whatever the order, an older record without one
    binds on the order as before; within a chain the gate path, like the others, reverses no move unless it clears the bar (0.3%) on
    both seeds. Today's four stand: each is the first pass on a new model. Found on the way and fixed the same day (the audit session's
    "(a), fix it now"): Shadow's 56 sat in Power in Light, which only improves Smite and Penance. Two readings had called it live:
    `dead_talents` took Shadow Word: Pain, named as the condition ("targets afflicted with your Holy Fire or Shadow Word: Pain"), for an
    improved spell (now `page_lint.improved_names`: a spell after "afflicted with", "affected by" or "targets with" is a condition, unless
    every named spell is in such a clause: Overgrowth's extended spell, Rapid Recuperation's trigger); and the filler pass's probe
    counted every heal of the spellbook when a build heals between fights, Penance included though Shadow lacks its talent (now a
    talent's heal counts only with the talent). Over every leveling pick (read as the pass reads them) and every raid page build, the
    only flip is that one; Shadow's pass then moved the point to Silent Resolve by utility at bit-identical times on both seeds. The
    leveling play check had already failed it (Lc, 2026-11-21): the measured rule caught what the tooltip reading missed.

1d. **A raid guide can describe a rotation its entry left (2026-11-22; found on the audit session's read of the tank pages)**. The
    Protection paladin raid guide of 2026-10-15 described a Seal of Righteousness rotation; on 2026-10-31 the entry moved to the official
    simulator's own Protection rotation (Seal of the Crusader judged first, Seal of Fury kept up, Seal of Righteousness switched off), and
    the guide was never rewritten. Its stamp had been refreshed at some point without a rewrite (and once more on 2026-11-22 after a
    one-line edit), so guides.py --check stayed quiet, while the pushed page's own Advanced list said "Seal of Fury: part of the rotation".
    A stamp says the text was read against the rotation; refresh it only after reading the whole guide. Open: a guides.py --check warning
    for a raid guide whose plan or reasons name a spell the page's build never casts in its play-check row, unless the sentence says so
    (page_lint's `negated`): "judge **Seal of Righteousness**" against 0 casts would have read as wrong on 2026-10-31.

1c. **The rotation search inserted class-book ranks (2026-11-22; fixed the same day)**. The warrior tank tune of 2026-11-21 put Revenge
    rank 6 (25288, round 1, +1.0%) and Heroic Strike rank 9 (25286, round 2, +0.3%) at the top of its rotation, both class books. apl_opt's
    insertion pool takes every line of the class's rotations in the simulator's checkout (`class_pool`), which cast book ranks; only
    `new_spell_pool` left them out (the H18 switch of 2026-11-19). The play check missed them: rule e looked only for book ranks the
    simulator does not register. Now apl_opt maps book ranks in the pool to the trainer's rank (casts and conditions, `trainer_pool`) and
    refuses a base that names one (`book_casts`), and the play check fails any book-rank cast (rule a). The warrior tank lane runs again.
    Checked the same day: no committed rotation file since the switch (97dc22be) names a book rank, and no committed play-check record
    has a book-rank cast, so no pushed page's numbers had one. Also from the play check's first read (one of its own D12-style faults): a
    tune's insert above an old line of the same spell left the old line dead (the trainer's Revenge rank 5 under the book's rank 6).

1b. **A spell cast more often than its cooldown allows reads as a fault until a talent is found (2026-11-22)**. The paladin tank cast Holy
    Strike 29 times in a 180-second fight against its 10-second cooldown (at most 19); no reset or modifier showed in sim/paladin's code,
    because Shieldsworn's 4 seconds come from its spell row through ParseStatic (the audit session found it). The play check now carries
    a cooldown-bound row (b4): each spell's casts against one at the pull and one each cooldown after, with the build's cooldown talents
    read from their tooltips ("Reduces the cooldown of your Holy Strike ability by 4 sec"; lists and spell families split); more casts than
    that is "explain", never a fail. A 60-second probe confirmed the 6-second cooldown (9.97 Holy Strikes). Related, in the play check's
    by-name counts: a seal's judgement books two ids (damage and taunt), so "Judgement of Fury 49.9" is about 25 judgements.

1a. **Three raid rotation leads for the optimality pass (2026-11-21, the audit session's C18-C20 from its player read of the raid
    pages; noted, not run)**. C18: the alternative that loses 2.7% to the official rotation. C19: the Demonology dummy rotation, below
    its base. C20: the Arcane-Frost dummy rotation, without Arcane Wrath. Each wants the parity race of the 2026-11-20 rule (ours and
    the official rotation x our builds and theirs, full raid, 10,000 fights, seeds 1 / 2) or, for a dummy rotation, a search from the
    file's own base; the pages are unaffected until then (the dummy rotations rank nothing on a player page).

0z. **The raid filler audit's tags missed Forever's pushback wording (2026-11-20; found on the audit session's Deflection question,
    fixed the same day)**. utility_tags.py's interrupt pattern read `lose .* casting time`, which needs a word between "lose" and "casting
    time"; Forever's tooltips say "to not lose casting time when you take damage" (Improved Channeling, Ice Barrier, Burning Soul, Spiritual
    Focus, Twilight Focus, Eye of the Storm, Healing Focus, Fel Concentration, Intensity). The nine read as no tag, so the filler audit and
    the scorer's raid tie-breaks counted their points as free, against the order the user's question of 2026-09-29 set (pushback
    protection first; that day's records still moved points into Improved Channeling, so the wording changed under the pattern later).
    Since 2026-11-03 six records had moved points out of them, all applied: Improved Channeling into Arcane Resilience in arcane-open-raid
    (2), fire-open-raid (3), arcane-frost-open-raid (1) and frost-ml-raid (2); smite-open-raid's Twilight Focus into Spell Warding;
    elemental-ml-raid's Eye of the Storm into Natural Grace and Elemental Reach. Fixed: `lose (?:.* )?casting time`;
    deep-runs/pushback_refill_1120.py put the ten points back (each build the same damage to the decimal in its entry's setting and a full
    raid, seeds 1 and 2; record raidsim/pushback-refill.json). The same day the credited simulator builds got the filler pass with exact
    thresholds (deep-runs/credited_fillers_1120.py: a move only at bit-identical damage in a full raid and on the dummy, never into a talent
    ability the build does not cast or a talent that improves only spells it never casts; record raidsim/credited-fillers.json), and
    page_lint.py a `free` check (a raid page's build holding points a measured filler pass moved, not applied). Open: a check after each
    data refresh listing the talents whose utility tag changed, so a reworded tooltip cannot drop out of the order silently again.
    The same pass found two more tag faults, fixed with the audit session's agreement (raid tags only, tanks unchanged): "survival" matched
    dodge, parry and block, so Deflection tied Survivalist and the pass moved nothing out of the simulator's Survival build (the user:
    "Why is Deflection taken? ... Wouldn't that be a wasted talent if your tank has agro?"); for a damage dealer avoidance alone is no tag
    now (utility_tags.SURVIVAL_DPS, 18 talents), nor is damage returned to an attacker (Eye for an Eye, which "damage taken" had matched:
    the pass had traded Retribution's Unyielding Faith, fear and disorient, for it). Six of our builds' filler audits had moved points into
    Deflection or Lightning Reflexes (2026-11-10 to 11-19). The exact pass then moved, each verified bit for bit in a full raid (10,000
    fights, seeds 1 and 2) and on the dummy: survival-raptor-raid Deflection 3 -> Survivalist 3 (861.74 both seeds), beast-survival-open-raid
    Deflection 3 -> Survivalist 3 and Expose Prey 1 -> Hawk Eye 1 (818.29 / 819.09), prot-ret-ml-raid Redoubt 2 -> Templar's Bulwark 1 and
    Toughness 1 (654.12 / 654.17). The other twelve builds hold free points with no more useful legal talent at bit-identical damage and
    stay as they are. Open: crowd-control resistance has no tag (Unyielding Faith, Stoicism, Iron Will: fears and stuns in Molten Core and
    Onyxia), so its points count as free; the 11-10 audit's Unyielding Faith -> Deflection moves in retribution-open-raid and
    shockadin-open-raid stay until the order says where it ranks.

0y. **A rotation search's round as one bench run filled the memory (2026-11-20; open, for the optimality pass)**. Feral's fresh raid
    tune (apl_opt.py druid --spec feral-cat-dps --fresh: 19 actions, 132 pool actions) sent its first round's candidates as one config:
    the bench held 10.5 GB and apl_opt 5.5 GB, the machine fell to 1.3 GB free of 32, and Claude Code reaped the session's background
    shells (the jobs themselves ran on). Batch a round's candidates (a fixed number of rotations per bench run) before the optimality
    pass's rotation tunes, which run many such rounds.

0x. **Two simulators and two racial settings had run under one name (2026-11-20; found on a number the audit session could not
    reproduce, closed the same day)**. Every lane exports WOW_FOREVER_SIM=<tools>/wowsims-forever-y and WOW_FOREVER_NO_RACIALS=1; a run
    without them (a hand command) fell back to setup.checkout()'s default clone, whose bench dated from 2026-11-16 (before H15's pet
    rule and the clip-delay key), with racials on. survival-raptor-raid read 899.5 there against the lanes' 861.6 (the old pet rule
    +4.4%, Berserking +0.7%). Runs it touched, from the checkouts' bench folders: the first hunter parity race (12:00-12:29, run again
    in the lanes' setup), the 11:15 measurement behind the SM/Ruin move (the audit's own measurement agrees), the H5 Balance A/B (no pet,
    no channel: its relative gain stands, its absolute numbers are racials-on) and two probes; the morning SIML race, the warlock and mage
    upstream races, the hand tier runs, the picks and the checks ran in the -y checkout. Closed: setup.py stamps each bench with its
    patch set (bench-build.json: a hash of raidsim/patches/forever and foreverbench/main.go); run.repo_path refuses a bench whose stamp
    is not the current set (unstamped: older than the patch files); run.py makes racials off the default (race_sweep.py sets them on
    for itself); the environments, pick, check and parity records carry the patch hash and the switches (sim_switches; the pet rule's
    flag now reads H15's default); render_modes leaves out a full-raid row whose record names another patch set. The default checkout
    was rebuilt and both are stamped: they now give the same 868.0 on survival-raptor-raid with racials on, and the lanes' 861.6 with
    them off. The hand-run mage tier records were made again in the lanes' setup.

0w. **A Wrath weave for Eclipse in the Balance rotations (2026-11-20, the independent audit's H5)**. Forever's Eclipse ("Your Wrath
    spell reduces the cast time of your next 2 Starfire spells by 0.50 sec. Stores up to 4 charges") needs Wrath, which no Balance
    rotation of ours cast: every search read the talent at 0. deep-runs/eclipse_weave_1120.py puts one line before the Starfire filler of
    both Balance rotations: Wrath (rank 8) while fewer than 2 Eclipse charges are stored, guarded by the Eclipse aura being known (the
    absent rule would otherwise read the stacks as 0 and cast Wrath forever; apl_validate's "No aura found" on the line is that guard
    for a build without the talent). Full raid, 6,000 fights, seeds 1 and 2: the page pick (no Eclipse) bit-identical; the pick with
    Eclipse 3/3 and Improved Wrath 5/5 added unpaid +7.2% / +7.5% (below 1 charge +6.7-6.9%, below 3 +6.0-6.1%). The Balance search
    that pays the 8 points (they come out of its 18 Restoration points) is the optimality pass's; the line is in place for it.

0v. **Oath of Light, Illumination and Reckoning (2026-11-20, the independent audit's H11 and H12)**. Three switches whose defaults keep
    the labs before (bit-identical), flipped with the healer and paladin re-runs of the optimality pass:
    - `heallab.tables.OATH_CRITS` (H11): Oath of Light's bonus healing crits with the heal it rides on (the simulator adds it to the base
      heal; the lab dealt it as a separate heal that never crits). holy-ml-heal, 60 runs: capacity 0.641 -> 0.629, overheal 13% -> 18%:
      within the noise, the extra crits land on a full tank;
    - `heallab.tables.ILLUM_VIGIL` False (H12): no Illumination refund on a Light's Vigil party heal (the client's spell mask, which the
      simulator follows). holy-ml-heal: capacity 0.641 -> 0.588 (-8.3%), out of mana 24 -> 35 s. The Holy paladin's healer tier may
      move when the healer pass runs;
    - `paladin.RECK_SEAL` (H12): Reckoning's extra attacks are auto attacks, so the seal procs on them. The Protection leveling pick: 0.5%
      faster per kill level-weighted (1.4% at 50).
    The Holy Power reading (the simulator's x1.5 on the whole crit, 225% at 5/5; a literal reading gives 175%) stays as the simulator
    has it: a judgment call the audit left open.

0u. **Shieldsworn's shield strike in the fight lab (2026-11-20, the independent audit's H10)**. Only Shieldsworn's 4-second Holy
    Strike cut was modelled. `paladin.SHIELDSWORN_STRIKE` (a mechanic switch, not a rules knob; False = the lab before, bit-identical): a
    landed Holy Strike deals one Holy Shield hit without spending a charge and rolls Shield Specialization's mana without its 3-second
    lock, and a caster mob's spells can be blocked for 6 s. The Protection leveling pick (500 fights x seeds 1 and 2, the saved rules):
    16.0% faster per kill at level 60, the only level where its order holds the talent (5.0% level-weighted). Off for the pages of
    2026-11-20/21 (their Protection numbers were raced without it); on with the Protection re-races and rules re-tune of the optimality
    pass, where the order search can also move Shieldsworn earlier.

0t. **Unsealed Wrath and seal twisting in the fight lab (2026-11-20, the independent audit's H3)**. The lab kept one seal up, so
    Unsealed Wrath ("your melee attacks store a copy of your active Seal for 15 sec, stacking up to 3 times; landing an attack with a
    different Seal consumes all stacks, giving the stored Seal its normal chance to activate once per stack") read 0, and the Retribution
    leveling pick stops a point short of it. Modelled on the Retribution path: landed swings store copies, a swing with the other seal
    pays them (Seal of Command at its 7 a minute, Seal of Righteousness every hit); `TWIST` (a rules knob, in duel.PVE_KNOBS; 0 = one seal,
    the lab before, bit-identical even with the talent: the copies never pay) switches Command and Righteousness once three copies are
    stored, above `TWIST_MANA`. Forever's Judgement does not consume the seal, so each switch is a global cooldown and about 200 mana. At
    level 60 (1,500 fights x seeds 1 and 2) the pick with the talent added (a 52nd point; the A/B could not pay it legally) and TWIST 1:
    4.2% faster per kill at a 20% mana gate, 1.4% at 40%, 0.7% at 60% (1.9 seal casts a kill against 1.0). Open for the optimality pass:
    the Retribution leveling search with TWIST in its rules tune (a 31-point build that pays for the talent).

0s. **Berserker Stance in the fight lab (2026-11-20, the independent audit's H7, the warrior half; the warlock's demon choice waits
    for the leveling lane to leave the warlock module)**. The module chose Battle Stance for Arms and Fury, so Whirlwind, Berserker Rage
    and Improved Whirlwind were blind. `BERSERKER_FROM` (a rules knob, in duel.PVE_KNOBS; 61 = never, the lab before, bit-identical):
    Charge from Battle Stance, then Berserker Stance (+3% crit, 10% more damage taken) once the rage above what Tactical Mastery keeps is
    spent, Whirlwind after Mortal Strike and Bloodthirst (both weapons for a dual wielder, the off hand with its own penalty). Measured
    on the leveling picks (400 fights x seeds 1 and 2, levels 20-60, the saved rules): slower from every level tried, Arms +8.8% to
    +11.3% time per kill (Overpower and Rend need Battle Stance), Fury +1.2% to +1.6% (0.8% faster at 50, 3.9% slower at 60). The
    knob stays off; the next rules tune can take it (Fury's 50s are the place to look).

0r. **Single-target Fire Nova in the fight lab (2026-11-20, the independent audit's H4; the optimality pass's mechanics, done early)**.
    "single targets never use Fire Nova" was hard-coded in fightlab/shaman.py. It is a rules knob now (`FIRE_NOVA_SINGLE` 0/1 with
    `FIRE_NOVA_MANA`, in duel.PVE_KNOBS; 0 is the lab before, bit-identical): Fire Nova after the shocks while a Fire totem stands and
    the mob is within its 10 yards. Measured on both leveling picks (400 fights x seeds 1 and 2, levels 20-60, the saved rules): slower
    at every mana gate, Enhancement +1.8% to +3.5% time per kill, Elemental +2.9% to +3.7% (most at 40-60: its 520 mana per cast becomes
    drinking). The knob stays off; the next rules tune may still take it. Trial by Fire stays nearly blind on single pulls: the lab
    measures it as a choice now, not as an omission.

0q. **gear_tiers.make chose sets of level-29/30 items (2026-11-20; cause found and fixed the same day)**. Twice that morning, both
    through pick_tiers.py: its first Frost Med run at 10:34 wrote mage-frost-bis (528.9 DPS in a full raid against 795 in the entry's
    gear) and then failed on its race, and its first Arcane-Frost run at 10:37 wrote the hybrid's two sets (average required level 29.4
    against 47.8 / 54.0). The cause: gear_tiers.py runs a private copy of gear_opt.py, and the item stat map (STAT) and the vetted launch
    items (VETTED) live in each copy, filled by that copy's load_db. pick_tiers loaded the database through its own gear_tiers copy and
    then called ml_pipeline.gear, which runs make() in ml_pipeline's copy: there both were empty, every item was worth 0 by any weights,
    no launch item was in the pool, and the picker took each slot's first item in the database (Embalmed Shroud, Stygian Bone Amulet,
    Feline Mantle ... Cookie's Stirring Rod: one list for Frost and the hybrid, whatever their weights). An offline replay of the per-slot
    step (no simulator run) gives that list exactly, and the same step after ml_pipeline's own load_db gives the proper set (item level
    62.6). Fixed: pick_tiers loads the database through ml_pipeline's copy; gear_opt.value and in_pool's sourceless branch stop with an
    error on an empty map or list (both had been silent); make() writes a new set only when it scores at least the old set (or the old
    set repaired, when it holds items outside the pool) on the confirmation seed and empties no slot; pick_tiers' kept record describes
    the file as it is (it had carried the level-30 set's names after the restore; the two mage records corrected). The Shockadin's Raid
    BiS set of 2026-11-19 (item level 42.9, no off hand; removed in de50ed2f, the Shockadin measured in Retribution's set since) had
    the same cause through another caller: deep-runs/gear_fix_1119.py loaded the database with the plain `gear_opt.load_db` (and never
    called load_vetted), then ran gear_tiers.make, whose private copy had neither. Every standing caller loads the database through the
    copy whose picker it uses (ml_pipeline, deep_opt, dungeon_tier, family_search, tank_gear, weight_errors, page_stat_weights;
    pawn_raid_compare supplies its own values and the tier copy's pool). The trap itself is gone since the same day (the audit
    session's first step of the optimality pass, done early): gear_tiers.py reuses the gear_opt module registered under that name, or
    registers its own, so every copy of gear_tiers (ml_pipeline's, family_search's, tank_gear's, heal_gear's) shares one stat map and one
    vetted list, and its pre-raid vetted list lives on that module too (the replay's broken path then gives item level 63.0); the stops
    in gear_opt.value, in_pool and the pre-raid pool are the backstop. The 105 tier sets on disk:
    mean item level 59.3 or more, none affected. The stopped ML Arcane-Frost run's 246-258 DPS on the dummy at 10:05 is not this (its
    path replays clean): the hybrid's builds under the Frost entry's rotation (0o).

0p. **The simulator's hunter rotations collapsed in our bench (2026-11-20, H6; found and fixed the same day: our own patch)**. Read from
    SIML with the bench's -siml2json (deep-runs/siml_upstream_race.py), every upstream hunter rotation scored 360-500 DPS on every build
    and option set against 800-960 under ours. The cause: our simulator patch makes Hunter's Mark rank 3 (14324: +98 ranged attack power
    against rank 4's +71 in the client data; raidsim/patches/README.md), and upstream's rotations keep the mark up with "not auraIsActive
    (CurrentTarget, 14325)": that aura never appears in our simulator, so they cast the mark on every global cooldown (121 casts a
    fight) and nothing else but white swings and Raptor Strike. siml_upstream_race.py maps the ranks our patches move (`PATCH_RANKS`,
    14325 -> 14324 with the trainer-rank swap). Probe (full raid, 2,000 fights): melee-survival-raid in melee-dps 745.1 under our raid
    rotation, 766.7 under upstream's melee rotation (+2.9%: Serpent Sting from range past the dead zone, 12% of the damage, and
    Immolation Trap kept up, 12%). The hunter parity race was run again the same day (record raidsim/siml-upstream-race.json). Our own
    rotations cast 14325 only before the pull, with no aura check, so they were never caught; a rotation from the unpatched simulator
    needs the same mapping whenever it names a rank a patch moves. The race (10,000 fights, seeds 1 / 2, full raid, our options) and its
    decisions (deep-runs/hunter_upstream_base_1120.py): bm-raid, mm-raid, mm-lonewolf-raid and melee-dps take upstream's rotation as
    their base (the page picks +2.1%, +0.7-0.8%, a tie, +3.1% / +2.2%); survival-pet-raid keeps ours (its Raptor build 0.9% ahead under
    ours on both seeds). Left: on the training dummy the converted rotations cast no Hunter's Mark (the hunter knows rank 4's id
    only); the full raid's debuff covers it, so only dummy numbers lack the mark (BM on the dummy still 545 against 529 under ours).

0o. **A search may target an entry that was never raced (2026-11-20, ML Arcane-Frost)**. ml_pipeline's targets step picks the entries
    from the race reports: arcane-frost-raid, new that morning and not raced yet, was invisible, and ML Arcane-Frost targeted frost-raid,
    whose upstream rotation the hybrid collapses under (stopped after 15 minutes). The same family as 0n (a step choosing from a report
    that does not exist yet or was made under other conditions). Open, for the next change to ml_pipeline.py: a new entry (no race
    report, or a report older than its builds list or base) is raced before any target step may choose; until then the lanes race
    each new entry first (audit_raid_1120d.sh).

0n. **A fresh tune after a base change picks its tuning builds from the race of the old rotation (2026-11-20, frost-raid)**.
    apl_opt.main_builds reads the entry's last race and environments report. frost-raid's fresh tune on upstream's frost rotation
    (deep-runs/audit_raid_1120c.sh, 08:25) read the race made under our old rotation and tuned on opt-frost-raid-raid-dps and the
    simulator's Arcane preset, not on frost-ml-raid (718 under the new rotation) and Frost Med (795); it kept nothing, so the rotation
    is upstream's as adopted until ML Frost's rotations step tunes it on its winners. Fixed by procedure the same morning: frost-raid
    and arcane-dps raced on their new bases first (deep-runs/base_race_1120.sh; arcane-dps's tuned raid pointer removed, as frost-raid's
    had been). Then in code (the audit's request): apl_opt --fresh races every listed build and the entry's presets on the base rotation
    itself (race_on_base, 3,000 fights, the tune's setting) and picks the tuning builds from that race; a non-fresh run is unchanged.
    Checked the night's other tunes: affliction-raid, demonology-raid, bm-raid and affliction-wrack-raid were tuned on the best build
    under their new conditions; the three old Destruction entries (fresh, with shards) on the old report's best, which was not the best
    at their bases, but sb-raid's and fire-destro-raid's ended best after the tune, and incinerate-raid's best build gets its re-tune in
    ML Destruction's rotations step.

0m. **The order polish can accept a dead decade (2026-11-20, the independent audit's note on the mage redo)**. The Frostfire pick
    (1/27/23) has a trough at 40: 42.8 s per kill against 32.8 at 30 and 35.6 at 50 (fights of 23 s for 18 at 30; 13 deaths in 600
    fights), and its order spends 31-40 on Accelerant, Ignite and Wand Specialization, taking Pyroblast, Impact, Heating Up and Master
    of Elements only after 40. Fire has the same shape at 30-40 (40-41 s; its 21-40 points go to Frost talents). The order polish
    (fl_levels.py) looks every ten levels (the race's levels) and scores the level-weighted time, so a decade between two race levels
    can be played badly at no cost to the score. Check: each mage order at 35 and 45 as well, or an order move that brings the Fire
    talents forward, raced at 35, 40 and 45; if the trough is the polish's, race the orders at every fifth level (or score the
    intermediate levels in the order polish).

0l. **One eat line for every level hides a loss at 20-23 (2026-11-17, the eat-and-drink re-tune)**.
    The Enhancement rules took eating below 90% of your health (80% before): 0.95% faster on the level-weighted score. A direct check
    on the page pick (scratchpad `shaman_eat_levels.py`, 3,000 fights, seeds 1-2, everything else as the rules file has it) had the
    90% line 8.7% slower at 20 and 10.2% at 22 (the shaman sits down to eat after almost every kill: 4.5-5.4 s a kill against 0.1),
    even at 24, 0.9-3.6% faster at 26-40. Restoration, on the same rules: even at 20, 2.9% slower at 22, 2.4-3.2% faster at 24-40;
    Elemental 1.1-2.5% faster at every level from 20. The Enhancement guides say "under 80% until 24" by hand. Open: a rest line by
    level (`eat_below` / `drink_below` as {from level: share}, the engine reading the level's value, the tune choosing the switch
    level as it does `IMBUE_TOP_FROM`); first check every class's rest lines level by level the same way (cheap: two lines x seven
    levels x two seeds per page pick).

0k. **The warlock's in-fight Life Tap reserve counts spells the rules switch off (2026-11-16, the Affliction re-tune)**.
    `warlock.decide` taps in a fight when the mana left after a **Shadow Bolt** is under the cost of **Fear** plus **Drain Life**, and
    only while the mob has more health than one bolt takes. The 2026-11-16 Affliction rules never cast **Shadow Bolt** or **Fear**,
    so the line still fires at about 15% of the mana (10% at 12, 18% at 60), sized by two spells the build never casts. A knob for the
    reserve as a share of the mana would let the tune choose it; a 0.2-0.35 taps a kill question at 50-60, small.

0j. **A knob that acts on a few levels reads as noise in the rules tune's screening (2026-11-15, the shaman's imbue)**.
    rotation_opt screens each move on 600 fights a level (seed 1) and confirms only the leaders. `IMBUE_TOP = rockbiter` was the best
    Enhancement candidate in every round and read +0.16% on the level-weighted score, never confirmed; a direct A/B on the page build
    (3000 fights, seeds 21 and 22, the same fights for both imbues) had Rockbiter 0.8-1.8% faster per kill at 54-60 (0.5% at 50), about
    0.5% on the weighted score, over the 0.3% install bar. Installed by hand with the evidence in the rules file's `changes`.
    Open: confirm knob moves (few, cheap) on the confirmation seed whenever they lead at all, or screen them with --confirm fights;
    and a knob whose effect starts at a level the tune does not visit (54 here: the tune looks at 20/30/40/50/60) needs a check at its
    own levels.

0i. **Numbers a rank takes from another spell, read at their level-60 value at every level (scan of 2026-11-15, after the imbues)**.
    spell_scaling.json scales a rank's own effects only; a description's `$<id>s1` from a referenced spell (a seal's judgement, a
    totem's or pet's attack) keeps the level-60 number from the level the rank is trained, too high until the rank's cap. Scan
    (scratchpad `ref_scaling_scan.py`, the official store; shortfall of the referenced amount at the rank's first level against 60):
    paladin Seal of Command's judgement 15-32%, Seal of Fury's per-hit damage and judgement 5-44%, Seal of Righteousness's judgement
    (its per-hit damage already follows the client's rows, `SOR_PER_HIT`); hunter Intimidation 42% (check what number it is);
    priest Penance 5-6%; shaman Fire Nova 3-6%; warlock Devour Magic, Inferno, Rain of Fire 1-9%; mage Blizzard and druid Hurricane
    1-2%. The druid's forms scale already (`form_ap * level / 60`). The general fix: each rank's numbers at the character's level from
    the client rows, the referenced spells included (the imbues' `referenced` rows and `tables.rank_amounts` are its first piece),
    then the paladin's leveling rules re-tuned from scratch and its records redone (the others' shares are small). Ask before a queue.
    **2026-11-16: the paladin's seals done (Changes made). The small ones (Intimidation, Penance, Fire Nova, the warlock's, mage's
    and druid's area spells) stay open.**

0h. **Player choices the class modules make that no search compares (inventory of 2026-11-15, agent, read-only; after the mage's
    Mage Armor, which the module had always left off: 0-5% per kill)**. A veto acts only through `can_afford`: it can switch a spell off
    or gate it on mana or the mob's health, never swap one buff for another, loosen a hard-coded gate, use the player's own health or
    reach casts made in `on_fight_start` / `after_fight`; such a choice needs a `ROTATION_KNOBS` entry. The inventory's five most likely to
    move time per kill by 1% or more, not yet verified by us:
    1. Rogue poisons (rogue.py 664-677): Instant main hand, Deadly off hand, no off-hand poison at 20-29; never compared with Instant or
       Deadly on both hands.
    2. Shaman imbue (shaman.py 296, 325-336): Rockbiter below 30, Windfury from 30, Elemental too; Flametongue and Frostbrand never
       compared. Chosen in `__init__`, so a file knob would be ignored: move the pick into `make_player` as the mage's `armor_choice` is.
    3. Arms and Fury stance (warrior.py 357-358): Battle Stance only; Berserker Stance (+3% crit, Whirlwind) never modelled.
    4. Hunter pet family (hunter.py 309, 441-464): a cat only; the other families' stats are not in the spell data.
    5. Enhancement totems (shaman.py 543-552): Searing Totem at the pull; Strength of Earth and Mana Spring never compared (new modelling).
    Also: the warlock's pet (Voidwalker from 10; the Imp is modelled, a cheap test), `THREAT_CARE`, the Protection warrior's stance, the
    druid's heal-or-eat thresholds, the paladin's blessing, aura and seal (it has no `ROTATION_KNOBS`; the Holy and Protection attributes
    were measured 2026-09-30, the blessings within about 2%), cooldowns spent on every pull (Blade Flurry, Adrenaline Rush, Berserk,
    Bestial Wrath, Death Wish). The warrior's `prot_off` comment calls it a knob, but it is not in `ROTATION_KNOBS`. Each one needs the
    class's leveling rules re-tuned and its records redone from the 20-60 race on, as the mage lane did: ask the user before a queue.
    **2026-11-15 22:40 (user: "Go full power, go with your recs"): items 1 and 2 done as knobs (Changes made); the lane
    `fl_knobs_1115.sh` tunes them. Items 3-5 and the rest stay open: ask before a queue.**
    **2026-11-16, the paladin's gear and seal, measured** (the module patched in-process, scratchpad `pal_gear_seal.py`: the Holy
    rotation's two page picks, the Shockadin 22/0/29 and Holy, on their tuned rules, levels 30-60, 2,000 fights, seeds 1 and 2, common
    random numbers):
    - **Gear, the larger one.** `_make_player_alt` dresses every Holy-path build with **Holy Shock** in caster gear (the `paladin-caster`
      row, audit 2026-10-18 row 65) from the level it has the talent, never compared with the melee row. The melee row kills faster at
      every level measured, both seeds within a point: 6-10% at 30-45, 4-7% at 50-55, 2-5% at 60; level-weighted over 30-60, 6.5% for
      the Shockadin and 6.3% for Holy. The 30-level jump on both guides (23.6 -> 31.2 s at 27-30 for the Shockadin) is mostly this.
    - **Seal.** The module switches to **Seal of Command** whenever the build has it (41 for the Shockadin). In caster gear, Seal of
      Righteousness instead costs 6-7% at 41, 1% at 45-50 and gains 1-2% at 55 and 3% at 60 (0.7 s per kill by removal at 60, 3,000
      fights); in melee gear Seal of Command is as fast or faster at every level. The Prot-Ret 11/16/24 (melee gear) gains 1.0 s from
      it at 60. 0i (Seal of Command's judgement read at its level-60 number from 41) moves these numbers below 60.
    - What it takes: paladin `ROTATION_KNOBS` (the Holy path's gear row, caster or melee, from a level; the seal, from a level), in
      `duel.PVE_KNOBS` too; 0i's seal scaling in the same queue; the `holy-leveling` rules re-tuned (from scratch and continued); the
      Holy rotation's open search redone from the race on (every finalist with Holy Shock ran in caster gear, so the winner may change);
      then records, builds, guides, stat values and GearCheck values. Ask before a queue.
    **Done 2026-11-16 (user: "Go with your rec"): both are knobs (Changes made); the Holy rules took melee gear at every level
    and kept Seal of Command. Items 3-5 and the rest stay open.**

0g. **A long search can mix two versions of the code (found 2026-11-07, the tripwire on lane C)**. `fl_open_search.py warlock`, started
    2026-11-05 10:20, crashed on 11-07 02:19 at Destruction's 20-60 polish: `module 'fl_signature' has no attribute 'sig_order'`. `_load`
    re-reads `fl_levels.py` from disk for every rotation, while `fl_signature` stays what the process imported at its start, so the
    process met the fl_levels.py of 11-06 12:22 with the fl_signature of before 12:14. Affliction and Demonology had finished before the
    edit. Nothing searched was lost: the level-60 block (36,382 builds) was saved before the crash, the winner 7/12/32 and two finalists
    stand. Three follow-ups, the first done:
    - done: `refresh_keys.py` refused a rotation without `done`, so `fix-keys-warlock` would have failed, `fix-open-warlock` and
      `after warlock` would have been skipped, and the fixes lane would have ended with "fixes lane done" and no warlock. It now takes a
      rotation with a winner and finalists. Tested on copies of the record. `open-warlock` touched by hand (patch-1103.log).
    - open: `patch_1103.sh`'s `run` returns 0 on every failure by design, so builds, orders and the race ran on a failed search
      (harmless here: `open_builds.py` wrote nothing, "record not complete"). A later step should stop or say so when its class's search failed.
    - open: load `fl_levels.py` once at the start of `fl_open_search.py`, so a process runs one version from end to end. Until then, an
      edit to a module the search loads per rotation reaches every search already running.
0f. **After the decisions of 2026-11-06 (user: "Go with your recs"; `_reference/page-audit.md` L)**: what is still open.
   - **Mobs notice on the first hit, for every class.** The lab's mob runs in from the pull's first second, so every opener is cast
     under approach; in the game a mob aggros when the first spell lands. Fire's Pyroblast opener (6 s) is modelled under the lab's
     convention and costs 0.4%; a faithful opener would favour every long first cast (Pyroblast, Starfire, Aimed Shot, Shadow Bolt).
     A tables knob for all classes, then every leveling rule and record again: for the next full pass, not a patch for one spec.
   - **A fresh one-tree Survival search.** Its level-60 search ran while every pure Survival build paid the old rule's penalty
     (melee share 34% against 50%: time divided by 0.61), so the search weighed melee share against speed. The record is redone
     from the 20-60 race on (polish and certificate under the new rule); a fresh search (5-11 h at 4 processors) is the full answer.
     The cat rotation and the Beast Mastery one-tree search sat on their floors (80% and 35%) and are redone the same way.
   - **Which later-phase items a community preset vets** (page-audit L15): Zul'Gurub quest rewards and battleground vendor items of
     item level 70 or less. The user's knowledge of Forever's launch content decides.
   - **The cost of the early-talent rule per spec** is measured by the fixes lane's records (`order_signature_first` and the race
     rows "signature talents late"): report it per spec when the lane ends.
   - **Mage specs outside the raid lane's ML final** (Fire, Frost, Frostfire) keep talent winners searched in tier sets that held a
     rank-14 weapon; their sets are re-made, their searches are not.
0e. **Queue shape and class lists (self-audit 2026-11-06, at the end of lane A of the patch queue)**:
   - **A fixed class list per lane leaves the machine idle at the end.** Lanes A (rogue, warrior, druid) and B (shaman, mage) ended on
     2026-11-06 at 05:45 and 00:57. Lane C (hunter, warlock, paladin) holds the two longest classes and the paladin after them, and the
     one-tree lane waits for `race-warlock`. From 05:45 one search ran: 4 workers on 12 logical processors while the user had asked for
     full power, and the leveling half now ends when lane C does (the rest of the warlock, then the paladin's three rotations, one after
     the other). Ideas: one shared class queue with per-class markers from which any free lane takes the next class, or lanes balanced by
     the hours of the previous run (`minutes` in the records; the warlock's and the hunter's blocks are the longest), and a search's
     worker count taken from the processors free when it starts.
   - **Class lists: nine classes, or a line saying why not, and a page check before and after.** The priest was left out twice (the
     70707 sweep, lesson of 2026-11-02; the patch queue, because the patch did not change it), and both times the capture date had moved
     for every class, so its pages lost their numbers (`page-audit.md` K1). The check that finds it needs no simulation: for every class,
     the pick of every leveling slot has current numbers and an order, read from the renderer itself (`render_modes` grid after
     `own_rotation_only`, `rank_builds`, `leveling_numbers`; 40 lines, this audit's scratch script).
   - **A one-tree search is bounded by the any-split winner.** When a spec's best build is within the write bar (0.5%) of its rotation's
     any-split winner, the one-tree search cannot write a build: skip it (druid cat rotation: 22.86 s for the 11/29/11 winner, 22.98 for
     the Feral page build, so no one-tree Feral search was queued). The same bound says when one is worth its hours: the Assassination
     page build was at 22.47 s, its one-tree winner came out at 22.06.
   - **The rules step runs before the orders step**, so a class whose builds lost their orders in a repair has its rules tuned on
     builds that hold all 51 points from level 10. Measured on the druid with the orders present (dry run, nothing written): the cat's
     rules come out the same (never cast Shred; 23.74 -> 23.61 s), Balance takes "eat below 50%" where the saved file has 40% (+0.08%
     between the two). For Fire it flips one knob worth 0.3-0.7% (0d). Small, but free to avoid: orders before rules, or the tuner gives an
     order-less build the stats model's order as the search's race does.
   - **The rules step covers a class's pipeline rotations only.** `rotation_opt.py <class> --fresh --write` tunes the pipeline's spec
     and its extra reports; every other rotation needs `--spec <rotation> --build <build>`. The patch queue's `rules-<class>` step
     therefore left eight rule files as they were before their class's module was ported to the patch (2026-11-03; the priest
     2026-10-31): mage `arcane-leveling` and `barrage-frost-leveling` (2026-10-22/23; the port corrected Missile Barrage's numbers),
     rogue `subtlety-leveling` (10-23: before the rework and before Death Mark became a required spell), warlock
     `demonology-leveling` and `destruction-leveling` (10-24), paladin `holy-leveling` (10-23), priest `discipline-leveling` and
     `holy-leveling` (10-23); the warrior's and the paladin's `prot-leveling` have no rule file and were not tried again either. The
     open searches of this queue ran under those rules. Measured on Subtlety (a continued tune from the saved rules on
     `subtlety-open-leveling`, nothing written): one new rule, `DEATH_MARK_CP = 1`, 22.44 -> 22.28 s at levels 20-60 (+0.7%) and
     21.9 -> 21.4 s at 60 (+2.3%, the level the search scores). The priest is the mild case: Shadow's rules from scratch on 2026-11-02
     gave the time of before its port (25.48 against 25.46 s). Remedy as on 2026-10-15 (`page-audit.md` B24): each file from scratch on
     its rotation's page pick, the result installed only when it beats the saved rules on the same build (seed 3, 3,000 fights: a
     from-scratch run can end on a slower set, 2026-10-27), then the open record from the 20-60 race on, builds, races and reports;
     the rotations whose search has not started first. What was done is in the changes table. Check for every queue: each file under
     `fightlab/rotations/` of a changed class is newer than the class's last module or data change, or a line says why not.
0d. **The signature rule is enforced on talents, not on rules and orders (self-audit 2026-11-06, at the mage and hunter class boundaries
   of the patch queue)**: of the 34 leveling winners on record two fail their spec's signature check, and the talent search that made
   them could not have fixed either. Three gaps:
   - **Rules are floor-checked for one spec only.** `rotation_opt` checks the signature floor on its tuning build's spec, and the saved
     rules apply to every spec of the rotation. The 11-02 patch repair moved the hunter's `leveling-melee` from 9/10/32 to 12/10/29,
     one point short of Survival, so the 11-03 re-tune of `melee-dps` ran under the Beast-Survival rule (the pet counts: 62%, no floor
     phase) and dropped the floor rules of 2026-10-24 (never cast Serpent Sting, Immolation Trap above half mana). Pure Survival (the
     pet does not count) under them: the one-tree winner 8/13/30 at a melee share of 34.0% (Serpent Sting 21%, the cat 26%, the trap
     10%; 400 fights, level 60, seed 4), 35.4% without the new Raptor Strike rule, 36.5% with no rules, 48.9% with the 10-24 rules
     (27.57 against 25.11 s per kill). Every pure Survival build pays about the same penalty, so the search optimized speed: the
     one-tree Survival search (15 h on 11-05/06, after three lost attempts) ended on a refused winner, and the Survival leveling page
     still shows a build that fails (28%).
   - **Orders are chosen on speed alone.** `fl_levels.pick_order`, the order polish and `order_repair.py` take the fastest order; only
     the old pick's win-back asks the signature check. The Fire winner 0/31/20 fails under all three orders, each at the first check
     level that holds Pyroblast (stats model: 20 and 30; own tree first: 20; own tree last, the chosen one: 40).
   - **A required spell the lab casts only with a second talent.** The mage module casts Pyroblast on a full Heating Up only
     (`PYRO_HARDCAST` is 0; the opener is not modelled), so every level that holds Pyroblast without Heating Up fails "cast in every
     fight", whatever the order. The Fire page builds passed on 11-04 only because the patch repair of 11-02 had dropped their orders
     (the check then plays the full build at every level); the lane's orders-mage step of 11-06 (00:45-00:57) wrote orders (Pyroblast
     at 39 and Heating Up at 44 for `fire-leveling`; 20 and 25 for `opt-fire-leveling-leveling-st`) under which both fail, so the
     next regen would show the Fire page failing. The Fire rules of 11-03 were tuned on those order-less builds: the floor phase never
     saw the levels in between.
   Ideas, none applied (the queue was running, and how strict the two rules are is the user's call): (1) run the floor phase on one
   build of every spec that levels with the rotation, or give a pure spec its own rule file, then re-run the Survival one-tree search
   under it; (2) qualify the orders as the finalists are (the fastest order that passes at 20-60, plus a move that takes a required
   talent next to the talent that makes the lab cast it) in `pick_order`, the order polish and `order_repair.py`; (3) Fire: the
   hard-cast opener where Heating Up is missing, or count Pyroblast from the level the build can cast it; (4) never tune rules on a
   build without an order, and stop a doomed search early: when no polished family passes its spec's check, say so and skip the three
   search runs. Checks to add after every class: the verdict of every winner in the class's records, and the signature check of every
   page build with the orders its orders step wrote.
   Added 2026-11-06 at the warrior, druid and rogue one-tree boundaries (tiny sims: 600 fights per level, seed 4; nothing applied):
   - **The Fire module already has the hard cast, as a rule knob** (`mage.PYRO_HARDCAST` in `ROTATION_KNOBS`; the 11-03 rules left it
     at 0, tuned on order-less builds, which hold Heating Up at every level). Under real orders the knob at 1 is slightly faster for
     four of five builds (the winner under its chosen order 35.23 -> 35.10 s, own tree first 37.02 -> 36.76, `fire-leveling` 37.00 ->
     36.83, `opt-fire-leveling-leveling-st` 39.79 -> 39.58; the stats model order 37.44 -> 37.55) and changes no verdict: the lab
     hard-casts only when the whole cast ends before the mob arrives, which never happens at the first check level that holds Pyroblast
     (0.00 casts per kill at 20 under own tree first and at 40 under own tree last; 1.08 at 30 with more Fire points). Idea (3) therefore
     needs either an opener the arriving mob may hit (a new knob value: always open with Pyroblast) or the rule change.
   - **The other side of the order gap: a signature talent taken last passes with nothing checked.** `assassination-open-leveling` takes
     Mutilate at 60 (0.0 casts per kill at 20-50, 2.91 at 60), `subtlety-open-leveling` Hemorrhage at 54 and Death Mark at 60,
     `beast-mastery-open-leveling` Bestial Wrath at 56; the warrior's three winners take theirs at 40. The Assassination winner with its
     own tree first (Mutilate at 40) is 1.8% slower (22.46 against 22.06 s). Whether a pure spec's order must take its signature talent
     as early as its tree allows belongs to the same decision (`page-audit.md` K5).
   - **A rule with one point of margin**: every cat build is at 80.5-81% against the Feral floor of 80%, because Ravage (16% of a cat's
     damage at 60) is outside the core list (`page-audit.md` K6).
0c. **A paused leveling search loses its whole polish-and-search block (found 2026-11-05, progress check of the patch queue)**:
   `fl_open_search.py` saves a rotation only once its winner is known. The family polish and the three search runs before it live in
   memory, and a restart redoes even a polish that had finished: the family cache of the rotation is written and never read back (the
   raid side has `family_search --reuse-polish` since 2026-10-31). Evidence: the Fury (warrior), Frostfire (mage), Demonology
   (warlock) and Survival one-tree (hunter) blocks were each restarted from zero four times between 2026-11-04 11:05 and 2026-11-05
   10:20 (a reboot and three pauses: run windows of 5-6 h against blocks of 6-9 h at night speed and 11-20 h on four logical
   processors), about 15 h lost per search, and the leveling half has completed no search since 2026-11-04 08:16. The Fury polish
   that finished on 11-05 at 05:46 was redone from 10:20 with identical progress lines. Idea: persist the lab results per build
   (build, fights, seed, plus a fingerprint of the lab code, the class data and the rotation rules; common random numbers make a
   stored result exact), so a restarted polish and search replay from disk; or read the finished family cache back as the raid side
   does and journal the polish per pair. A replay is only as fast as the search repeats itself: the Survival polish drew other start
   builds after the raid lane rewrote the class builds (the starts set the random splits). Until then: change the cores with the
   balancer alone (`balance_1104.ps1 -Run/-Bench`: no restart, nothing lost) and pause only after a block has logged its winner.

0b. **The hunter's simulator presets are not read (found 2026-11-03)**: `run.sim_presets` finds no preset in `ui/specs/hunter/dps/presets.ts`
   (bac92dbd5 and later: one `Builds` list of preset builds, `Builds.map(build => build.talents!)`), so no hunter entry races or seeds from
   the simulator's builds. Add that form (and the SIML builds the paladin moved to with #812, read since 2026-11-03).

0. **The any-split leveling search loses to its own one-tree search (2026-11-03, patch_1103.sh)**: the shaman's fresh open search in the
   Elemental rotation (warm start, 70753) picked the 26/22/3 hybrid at 29.48 s per kill (20-60); the one-tree Elemental search run right
   after (`fl_open_search.py shaman --tree Elemental`) found 32/11/8 at 28.99 s, 1.7% faster, a build the any-split space contains. Same
   pattern as the shaman's lost 29/22/0 lead (2026-11-02). Lead: seed the any-split search with each one-tree winner (or run the one-tree
   searches first) and race them in its finalists. Also fixed the same day: one-tree records older than the talent data were used by
   `open_builds.py` (a Lava Burst build after the 11-02 patch); they are now skipped and re-run (deep-runs/pure_1103.sh).

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

- (2026-11-18) After a lane that ran a tool for some classes: every shared record it wrote still holds every class (`git diff --stat` and a count of classes against HEAD: hit-below-cap.json, unused-abilities.json, weight-errors.json, heal-values.json, page-stat-weights.json, pawn-raid-compare.json). A new tool that takes classes and writes one record for every class merges from the start.
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
- (2026-11-06) After every class of a leveling queue: `fightlab/signature_audit.py <class>` without `--write` (six classes in a minute): no page row fails; and the pick of every leveling slot has an order and current numbers, read from the renderer itself (`render_modes` grid after `own_rotation_only`, `rank_builds`, `leveling_numbers`; no simulation). Found that way: a class without numbers, a recommended page without a talent table, a hybrid page showing another model's AoE export (`page-audit.md` K1, K2, K7).
- (2026-11-06) The jump of every leveling winner against the previous record, with its cause named, and the old winner run once on today's data when the jump is unexplained (druid 2026-11-06: Feral 27.6 -> 22.9 s and Balance 42.2 -> 37.3 s, the 11-02 patch as ported on 11-03: Rip, Rake, Ferocious Bite and Pounce +25%, attack-power coefficients, Starfire +40%; warrior Arms -4.7%, Fury -1.2%; Protection +6.6%: the 10-19 winner 0/20/31 takes 30.0 s at 60 today against 27.5 then, so the data or the module moved, not the search; which number moved is not identified). Also the level at which each page build takes its signature talent.

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
- **ML records outlive their target** (2026-10-31, hunter audit): `ml_pipeline.py --steps final` only runs specs `targets(cls)` still lists, so
  a record whose family lost its build (the hunter's Beast-Survival, `beast-survival-open-raid` dropped when melee Survival passed it) passes
  with rc=0 in seconds and nothing searched, while `ml_builds --rank` and `gear_links` keep rendering its old gear section. Moved to
  `raidsim/ml/retired/`. Check at every audit: an `ml-<class>-<spec>` marker written within a minute of the previous one is a no-op.
- **On-next-swing attacks cast as instant extra attacks** (2026-10-31, warrior audit: a Fury rotation edit read +17.17% on both seeds).
  The simulator casts Heroic Strike, Cleave, Maul and Raptor Strike through their tag 1 spell (the queue); an untagged id falls back to
  the plain spell (`core/apl_helpers.go`), an instant attack on top of the swings with no validation warning. Two ways in: the rotation
  search's lower-rank edit rebuilt the spell id without its tag (Heroic Strike rank 8 untagged: 32.6 casts a fight instead of 14, 809 ->
  956 DPS; the search was stopped before it wrote), and the melee hunter rotations (our base rotation of 2026-09-28, written for the fork)
  cast Raptor Strike untagged, which the official simulator has queued since the port: melee Survival 819 -> 735 (-10%), the Beast
  Mastery pick in the melee entry 496 -> 438, in a full raid. Every melee hunter raid number from 2026-10-18 to 2026-10-31 is inflated by
  about 11%. Fixed: `run.QUEUE_SPELLS` / `queue_tag` (the spellbook pool tags them, the rank edit keeps the id's fields), the three
  melee hunter rotation files tagged, the entry re-tuned, raced and searched again (`deep-runs/queue_tag_redo.sh`). Check at every audit:
  a single rotation edit worth more than 5%, or the same gain to the hundredth on two seeds, is a mechanics hole until shown otherwise;
  `queue_tag` over `raidsim/apls/` must change nothing. Open: the unrestricted worktrees hold their own copies of the hunter files.
- **Rotation lines the simulator update orphaned** (2026-10-31, same audit). b90e2b9 gives Whirlwind's strikes their hand as the action tag
  (main hand 14, off hand 15; `ActionID.WithHand`), so every warrior rotation's `1680 tag 1` line named a spell that no longer exists and
  the simulator dropped it with a warning: no Whirlwind since the re-pin (fury-open-raid 813 -> 861, arms-2h-raid 754 -> 786 in a full
  raid once re-tagged; the Arms re-tune's +4.8% "insert Whirlwind" was the search finding its way back). `raidsim/apl_validate.py
  --all-talents --write` lists exactly this, but no re-pin step ran it. Now in the re-pin checklist (CLAUDE.md): run it right after the
  pin, diff against the committed record and act on every new warning before any search. Left as they are: Frost Blast (1326055, gone
  from the live spell data: dead lines), racials (race-neutral runs), the archived fork preset `dps_no_reck`, paladin's Holy Shock 20930
  (stage 2).
- **The gear pool followed the database's source entries** (2026-11-05, hunter audit at the end of its raid lane: the new Marksmanship
  ML build scored 943 in its entry's own race against 1004 and 1008 for the builds it replaced, and its tier sets averaged item level
  78-80 against 66-68). Three upstream database updates changed gear results with no check (`_reference/page-audit.md` J1-J4): b90e2b9
  (2026-10-30) dropped a third of the items, and all 14 standard sets have run with one or two empty slots since (the bench reports
  `missing_gear`, `run.py` never read it); 54ceac6 (10-31) listed `pvp` sources and bac92db (11-02) `quest` and vendor sources, and
  `gear_opt.in_pool` admitted every item with a source entry: rank-14 weapons in 49 tier sets, Naxxramas and Ahn'Qiraj quest rewards in
  19, each new set +5% to +22% over the set it replaced. Fixed: only drops, recipes and reputations count as sources
  (`gear_opt.dated_sources`). Open: the standard sets, every tier set and the searches made in them (the user decides when). Check at
  every audit and after every re-pin: the database's item count and source kinds against the previous pin (a new kind or a shrinking
  database is a pool change), a tier set's average item level against the set it replaces (a jump above 3 levels, or a set worth more
  than 5% over its predecessor, is a pool change until shown otherwise), and `missing_gear` in one bench row per standard set.
- (2026-11-09) Free points and guides, after every lane: `page_lint.py` dead and build checks clean, which now include a guide that says the
  build lacks a talent it takes ("This build takes no **Holy Shock**" on a build with it) and a guide that gives a talent other points
  than the build ("**Frenzy** (2 points)" on 3). A healer or leveling page whose idle note says "opens nothing" gets a filler pass
  (`heallab/filler_pass.py`, `fightlab/fl_filler_pass.py`): the leveling pass now moves a zero point into a live talent when the move
  costs at most 0.1% on each seed (noise had kept Improved Sayaad in a Voidwalker build), and `open_builds.py` re-applies a written pass.
  A healer report's * marks (not simulated) must agree with what the lab applies (Conviction read * at +7.3%).
- (2026-11-09) Tier-gate points and the rotation guides' levels, after the paladin Vindication lane. (1) `fightlab/fl_filler_pass.py` reads
  only points the build can drop and stay legal, so a point that holds a tier open is never measured: the Prot-Ret leveling build kept
  2 **Redoubt** (block, which needs a shield, on a two-hander) and 2 of 3 **Toughness** as the 15 Protection points **Swift Judgement**
  needs. Moved by hand and recorded in the pass's record (`fightlab/filler/paladin-hybrid-protection-retribution.json`, so
  `open_builds.py` keeps them): Redoubt to **Sacred Duty** (0.00% on both seeds, a shorter bubble cooldown) and 2 Toughness to
  **Improved Hammer of Justice** 3/3 (-0.17% / -0.15%). Done the same morning: step 5 of the pass (each point the build cannot drop, moved to any
  talent legal along the order, kept when faster on both seeds; on the Prot-Ret build after the hand moves: 14 gates, 27 legal moves,
  none faster), and two record fixes (a dry run beside a written record goes to `<record>.dry.json`; a second `--write` chains onto the
  written record so `open_builds.py` still re-applies it). A dry run over the 27 leveling page picks that are no raid build followed.
  (2) `level_guides.py --check` now also reads each leveling spec's rotation guide (guides/<class>.json) for talent levels against the
  build's order, with the forms those guides use ("(level 30;", "(levels 24 and 26)", "(18, 30 seconds a rank"), a group's one range
  ("**Lethal Attacks** and **Careful Aim** (levels 10-19)") and a span ("**Relentless Strikes** (31-39)" for ranks at 31-39). Its first run:
  41 stale paladin levels and talents the builds no longer take (Holy Conduit, Consecrated Ground, Sacred Duty, Eye for an Eye), every
  other class clean but one druid line ("Before **Moonkin Form** (levels 10-39)", reworded).
- (2026-11-09) A tool no lane runs can break unseen. `heallab/calibrate.py` stopped with an UnboundLocalError on every run from
  2026-10-18 (c90090d6) to today: an `import splitfx` inside `main()` made the name local, and the shares sentence earlier in `main()`
  read it unbound. The four healer calibration records date from 2026-10-01, so the stats model's heal-mode values for Holy paladin,
  Holy and Discipline priest, Restoration shaman and Restoration druid predate every healer-lab mechanic since (Oath of Light and
  Conviction scored 0). The raid sim's calibrate.py had the same bug on 2026-10-23 and was fixed then; nobody looked for its twin.
  Fixed, the four calibrations re-run, and `_reference/data/code_lint.py` (static: a name a function reads before its own local import
  of a module-level name) finds no other case. Run it at every lane boundary, next to page_lint.
- (2026-11-09) Stale candidates and stale hand-entered effects. (1) About 300 saved candidates under the classes' `candidates/` folders
  held talents later beta builds removed (druid Berserk and Gift of the Earthmother, mage Arcane Focus, Elemental Precision and Improved
  Fireball, paladin Instrument of Law, Twist of Light and Voice of Truth, rogue Murder and Improved Eviscerate, shaman Lava Burst, warlock
  Malediction, warrior Raging Blows); `repair_builds.py` repairs proposed-builds.json only. The calibrations fit over them and the races
  list them, measuring builds a point or more short (this morning's paladin leveling race still ranked cand-ret-r1..r8). Since today
  `validate_builds.live_candidates` keeps them out of rebuild.py's fight-lab, raid and heal steps and of the raid and healer
  calibrations, each skip logged. **Open**: repair or retire the files (rogue after its lane). (2) A hand-entered effect replaces the
  parsed one, so a talent the client reworked keeps its old shape: paladin Conviction's heal entries were 5 ranks of melee crit
  (now 3 ranks, 2% to every spell and attack), so no heal matched it and the lab's +7.3% could not be fitted; fixed for holy-heal, and Oath
  of Light (no parsed effect) got a template the calibration scales. **Open**: 178 manual entries in nine classes carry values for another
  rank count than the talent has now (a scan: `len(values)` against the tree's maxRank); most are fits that keep five values for any
  talent, but each one a client rework touched needs the check Conviction failed. The healer calibration had also measured only the
  hand draft, the optimizer export and candidates, never the page's ML build (holy-ml-heal, the one with Oath of Light): pass it with
  `--builds` until the default includes the spec's `-ml-heal` build.
- (2026-11-09, user: "is Wild Growth not taken because the simulator and tests are looking at single target healing numbers where Wild
  Growth is meant to be used for parties and raids?") The healer lab heals one party (tank and four raid members, a raid-wide hit of
  700 +-30% every 20 +-6 s), which is Wild Growth's reach, so not single target. Light damage was not the cause either: with the old
  model Wild Growth cost -2.1% to -3.7% at the lab's damage, twice the damage, 2100-damage bursts and twice as often. The cause was the
  lab: the druid had one group-heal role, Wild Growth when the build has it, else Tranquility, so taking Wild Growth meant never casting
  Tranquility. Fixed (engine "big_group" role, tried first when ready; only the druid with Wild Growth has one, every other build is
  bit-identical): Wild Growth on top of the page build -0.7% / +0.4% / -0.5% / +0.3% in those four settings, in the hand draft -0.1% /
  +0.2% / +0.9% / +1.0%. The Restoration deep search ran with the old penalty: re-run fresh (deep_heal.py druid --fresh). Check every
  healer module for roles that exclude each other the same way when a spec gets a second spell of a kind.
- 2026-11-10 (mage raid guide rewrite after the patch queue): the `raid_casts` field of `<entry>-environments.json` sums casts by spell
  name, and Arcane Missiles has two ids with that name (10212 the channel, 10274 its missiles), so it reads twice the casts; the
  per-id `raid_spell_casts` and the dummy's casts per minute in rotation.md count once. The Frost, Arcane-Frost and Arcane raid guides
  had quoted the doubled number (fixed: about 10, 14 and 15 a fight). Quote `raid_spell_casts` in guides; open: make `raid_casts` skip a
  spell's triggered missile id (it sums ranks of one spell correctly, so not a blanket max).
