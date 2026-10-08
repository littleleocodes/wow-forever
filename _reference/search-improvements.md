# Search improvement log

> Hand-kept (not generated). User request 2026-10-07: "Make sure we're taking notes of any improvements and changes we can make so we
> can further fine tune the process to find the true best builds." Every self-audit adds to it: what changed and why, what was tested
> and rejected, and the open ideas ranked by what they could still find. Newest entries first in each section. Numbers are the
> community simulator's (ElliotWood/Forever at b0f0df3) or our fight lab's, never in-game measurements.

## How close the process gets (assessment of 2026-10-07)

- Within the models: raid builds probably within about 0.5% of the best build a spec's rotation and gear allow; leveling within 1-2%.
  Races separate builds to about 0.3%, so the "best build" is a handful of tied builds.
- Against the real game the models limit us, not the search: a few percent within a spec, more between specs. Lowest confidence:
  warlock (demon scaling unknown), hunter (our pet-scaling patch, the Summon Hawk model), tanks and healers (our own weights and lab),
  leveling everywhere (Classic mob and gear data, assumed pulls, drinking and eating).
- Blind spots of the search itself: builds that need a rotation nobody wrote; gear coupling (a family is searched in another spec's gear
  until it wins); three-talent packages that pay nothing in any pair; leveling builds strong early but weaker at 60 (the main search
  scores level 60); one fight type (single target, 180 s, full raid, an Elemental target).

## Changes made (with evidence)

| Date | Change | Why (evidence) | Effect |
|---|---|---|---|
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
6. **Fight variety.** Every raid number is one fight. Idea: race the top builds of each spec in two more settings (two to three targets;
   an Undead or Demon target; 90 s and 300 s) and flag a pick that is not robust.
7. **Model fidelity** (biggest real-game gap, not search): warlock demon scaling (a beta tester's pet pane), the hunter pet attack-speed
   question, the final beta build refresh, comparison with beta logs and real leveling times.
8. **Mana-conditional spell ranks.** Retribution's lower Seal of Command rank pays only for mana-hungry builds: a rank line guarded by
   mana would let one rotation serve both.

## Efficiency (measured)

- 2026-10-07 night: during a rogue family polish the machine ran at about 80% CPU (12 logical processors). A bench call costs about
  0.2 s to start; a batch of 120 builds at 300 fights about 4-5 s; neighbour generation about 0.07 s. The idle fifth is the gap between
  batches (Python work, the batch tail). Idea: climb two pairs at once in threads (each pair's climb is independent and uses its own
  random stream, so results stay identical; the bench config file name needs the thread id). Expected: the polish, the largest step,
  about 20% faster. Test: identical outputs against the sequential polish on a few pairs.
- Polish cost per pair is about 10 improving steps of 120 builds plus a final pass of about 160: the climb, not the final pass, is the
  cost. Cheaper climbs must not change where they end (the warm-start test above).

## Self-audit checklist (after every class)

- Step timings in the logs (polish, search, certificate, structural ranking, re-tunes) against earlier classes.
- Every lead: its cause (search gap, rotation, gear, bench bug) and whether a known positive should be added.
- Winners holding abilities the rotation never casts; "Not in this build" notes on the leveling pages.
- Builds written or confirmed; pages regenerated; link check clean; commit and push.
