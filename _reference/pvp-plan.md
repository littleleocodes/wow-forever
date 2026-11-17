# PvP builds: work plan

Hand-kept. Started 2026-11-14 (user: "I think we start working on the PvP builds like when we originally started this project. Do
full research and come up with a game plan", then "make it happen, do full research on WoW Forever PvP builds and build whatever is
necessary").
- Research: `_reference/pvp-research.md`.
- The duel lab: `_reference/data/duellab/README.md`.

## Where PvP stood (2026-11-14)

- **Builds:** 34 PvP builds, research pages only (`<class>/research/pvp/`) since the user's 2026-10-04 decision ("raid and
  leveling only"). Ten are hand drafts from 2026-09; 24 are derived by `derive_pvp.py` (the stats model's `pvp` profile plus
  talentsforever pick rates).
- **The model guesses; nothing measures.**
  - The PvP profile's weights (burst 0.4, survival 0.5, mana 0.05, utility 1.5) were tuned so its optimizer lands near Classic's
    community PvP builds: 67% overlap on average, 31% for the Seal Fate rogue (`_reference/pvp-check.md`, last run 2026-10-15,
    before three talent updates).
  - About half of each class's talents have explicit PvP values. Some name talents that no longer exist; new ones (Bloom, Genesis,
    Boot Knife, Death Mark, Bane of Havoc, Bloodthrill) have none.

## The plan

1. **Research** (done 2026-11-14). `pvp-research.md`, and the community's builds as exact allocations in
   `_reference/data/pvp-community-builds.json`.
2. **The duel lab** (in progress), the measurement PvP lacked: level-60 one-against-one duels on the fight lab's class modules. Each
   spec plays its own tuned rotation, under a PvP layer per class (`pvp_<class>.py`), with Forever's PvP rules (`dtables.py`).
   - Done: the engine, all nine class layers, the field and the matchup matrix (`pvp_field.py`), validation pass 1
     (`duel_profile.py`; the log below).
   - In progress: validation. Logs per matchup; the matrix against what the community reports (warlocks strong, as in the level-30
     Forever Open; mages favoured over warriors in the open); mirror matchups near 50%.
3. **Measure the builds.**
   - The field is the community's most-tagged PvP build per class.
   - A build's score is its mean win rate over the nine classes, with the mean health margin as the tie-break.
   - Talent values by removal against the field (`pvp_values.py`).
   - Races of our 34 builds, the community's builds and the stats model's.
4. **Search for the best PvP build per spec** (`pvp_search.py`):
   - Local search over legal builds from our builds and the community's: 1, 2, 3 and 5-point moves and prerequisite chains, common
     random numbers, kept on a second seed, 30+ points in the spec's tree.
   - Where the field cannot tell talents apart (unmodelled effects), the stats model's PvP value, then the community's pick rate.
   - A winner replaces a build only at the replacement bar (0.5%, measured on the field score).
   - **Past expansions' PvP builds** (2026-11-15, user: "searched PvP builds from past Expansion, mainly Classic, TBC, and WotLK, and
     found what talents were taken in those builds and apply them to our builds"): Forever imports many TBC and WotLK talents
     (Penance, Mutilate, Maelstrom Weapon, Fingers of Frost, Frostfire Bolt), on which Classic's builds say nothing.
     `_reference/data/pvp-expansion-builds.json` and `_reference/pvp-expansion-research.md` hold those expansions' arena and
     battleground builds, mapped onto Forever's trees. Their consensus talents seed the search, and a consensus talent the winner
     skips is raced as a swap in the duel lab (as `popular_swaps.py` does for raid and leveling). Evidence, not a template: those
     builds were shaped by arenas and resilience, which Forever lacks.
   - **The blind-spot check, before the report** (2026-11-16, user: "make sure we double check everything like that at the end",
     after the Frost winner, 20/0/31, traded Ice Block for Arcane Concentration and Arcane Meditation). The lab plays Ice Block
     (`pvp_mage.py`: below 22% health, only when it can change the duel), but a duel scores wins, so time bought for help, escapes,
     several attackers and battlegrounds count for nothing. For every tree's winner, after the queue:
     - list what it lacks that real PvP rates highly: the community's Classic builds (`pvp-community-builds.json`), the TBC and
       WotLK consensus (`pvp-expansion-builds.json`), and every talent that grants or improves a defensive, escape or control tool;
       also the abilities the winner holds that its duels never cast;
     - for each, read how the class layer plays it and how often it fires in the winner's duels (`duel_profile.py`), then race the
       winner with it put back (legal, paid from the cheapest points) on the final race's duels;
     - the report gives each one a verdict: the lab's verdict (modelled, and the race shows what it costs), or a blind spot (its
       value lies outside a one-against-one duel, or the layer's use of it is limited), with the build that keeps it and its
       measured cost;
     - with the known items: the Holy paladin winner without Holy Shock (the signature rule), the Beast Mastery hunter's 96% (check
       the pet).
5. **The stats model's PvP profile, calibrated on the duel lab** (as the fight-lab calibration fits leveling), and the PvP values
   brought up to the current trees. It stays the fast screen. `pvp_check.py`'s cases (Classic Era community builds) gain the TBC and
   WotLK builds, restricted to the talents Forever has.
6. **Pages:**
   - PvP player pages again (`<class>/pvp/`, a PvP column in "Pick your spec").
   - Per spec: the build, its talentsforever link, how to play it (opener, control chains, cooldowns, the trinket), the matchups
     from the matrix, PvP keybinds and macros in the user's scheme.
   - The research pages and the matchup matrix.
   - **User decision:** the 2026-10-04 decision removed the PvP player pages, and the user's new request brings PvP back. On
     2026-11-15 the user asked to see the PvP results first ("I want to see the results of PvP before deciding if they go on the page
     or not"): no PvP player pages until then; the results go to the user as a report (the matrix, each spec's best build against
     the community's, how it plays).
7. **Battlegrounds** (after duels):
   - Warsong Gulch flag carrier: survival against two or three attackers with a healer.
   - Healer under focus.
   - Burst against a clump (Darkspear Islands, Arathi Basin nodes).
   - Group scenarios on the same engine.

## Assumptions to revisit

- Open field, no line of sight: kiting classes are favoured. Pillars would move casters against melee.
- No consumables and no racials. Engineering items and Will of the Forsaken matter in real duels.
- Dungeon-blue gear for both sides. A PvP rank set from the simulator's item database is the next gear step.
- Pets cannot be attacked or controlled.
- Warrior stances are not modelled (every ability is usable).
- The AI plays well but not perfectly. A matchup's number is the model's AI against the model's AI.
- The mage wears Ice Armor in every duel (`duel.PVE_KNOBS`, 2026-11-15). Frost Armor's longer chill, or Mage Armor's resistances and
  regeneration, are untested in duels.

## Log

- 2026-11-14:
  - Research done.
  - The duel engine, the mage and warrior layers and the field tools built.
  - The other classes' layers started, four in parallel.
  - First results: Frost mage over Arms warrior 89-92% (open field); the mage mirror 49%.
- 2026-11-14, later:
  - All nine classes have PvP layers. Shaman, warlock, hunter, priest, paladin, rogue and druid were written by agents; the mage
    and warrior drafts are being rewritten to the same standard.
  - Engine additions from the agents' findings:
    - pets that area spells and cleaves hit and control;
    - the defender's dodge, parry and block hooks;
    - Grounding through an engine hook; per-class trinkets that fire only when they free completely;
    - school lockouts on every spell; off-GCD spells (the fight lab ignores spell_gcd.json's off_gcd list);
    - no attacks on stealth; layer-declared immunities and stealth-keeping spells;
    - one DR count per step and spell; Wound Poison as a flat 165 off each heal per stack.
  - Baseline matrix (community builds, 200 duels a matchup), before the mage and warrior rewrite: strongly polarized, many
    matchups near 0% or 100%. Shadow priest and Ret/Prot paladin beat most classes; warlock and druid lose to healers.
    - Reading: each AI plays the same way every duel, so small edges become certainties, and AI quality differs between layers.
    - Next: a validation pass over the most extreme matchups (logs: AI defect or class strength), before any build is judged on
      the field.
- 2026-11-14, validation pass 1 (`duellab/duel_profile.py`, new: per side the time spent idle and the waste in the logs).
  - The matrix after the mage and warrior rewrite was still lopsided: the rogue won 15% of its duels on average, the Shadow priest
    80%. The community rates the rogue specs highly (RankedBoost S tier, Seemeta's Subtlety).
  - Fixed, engine:
    - a bleed's tick counted as a melee strike for Retaliation and Nature's Grasp (Garrote's ticks were answered by Retaliation);
    - Death Coil's horror was blocked as a fear by Berserker Rage and Fear Ward. The client says otherwise: its aura carries
      mechanic 24 (Horror), and both give immunity to mechanic 5 (Fear) only (SpellEffect, client 70938; `dtables.HORROR`).
  - Fixed, layers:
    - the rogue cast Sap into Berserker Rage every second (it now waits it out in stealth);
    - the rogue struck into Retaliation (now Kidney Shot, Gouge or Blind, else it pools energy);
    - the rogue used Evasion against a warrior, whose Overpower each dodge arms;
    - every melee layer struck into a free warrior's Retaliation (it had dealt 455-1,168 a duel to paladins, shamans and druids).
      Now no white swing or weapon strike goes into it while one's own average hit is worth less than 60% of the answer
      (`pvp_base.hold_swings`, `RETALIATION_TRADE`): two weapons and Cat Form hold, a two-hander keeps swinging. Holding every swing
      for 15 s had cost the paladin more than the answers did (94% -> 57% against the warrior), and holding at an even trade cost the
      shaman 9 points (each answer feeds its Lightning Shield);
    - the hunter used Scatter Shot to peel while its own Serpent Sting ticked, which ended it (now the pet's Intimidation first);
    - the mage stood at 22 yards, outside Fire Blast's 20, against a priest that reached it there, and never used Fire Blast
      against ranged foes (the frost leveling rotation keeps it to finish a mob). It now steps in and casts it on cooldown against
      a ranged foe. Its damage against the priest doubled, from 37 to 73 a second.
  - Checked and left as the data say:
    - Shadow Word: Death's backlash (30% of maximum health, Forever's tooltip);
    - Improved Mind Flay's 20% ramp a tick;
    - Garrote out of stealth after Ghostly Strike (a Forever mechanic);
    - Forever's Inner Fire (1,395 armor at rank 6) and Shadowform's 15% physical cut, which with Power Word: Shield explain most of the
      priest's results against melee.
  - Left as modelled trade-offs: a warlock's Fear broken by its own Drain Life (20% a hit), a paladin swinging through its own
    Repentance when above 85% health, a druid's root broken by Thorns in the step before it walks off.
  - Effect on the matrix (200 duels a matchup, `_reference/pvp-matchups.md`):
    - warlock against warrior 48% -> 86% (Death Coil); mage against hunter 8% -> 28% (Fire Blast); druid against warrior 2% -> 10%;
    - the means: priest 80%, paladin 77%, hunter 63%, shaman 60%, warlock 51%, mage 45%, warrior 38% -> 32%, druid 26%, rogue 16%.
    - The matrix stays lopsided. Next: a second pass over the remaining extremes (the rogue's and the druid's losses, the priest's
      and paladin's wins), mirror matchups, then the searches.
- 2026-11-15, the fight-lab issues below fixed (user: "Yes"). Each fix has a switch to the model before, and with every switch off
  every class reproduces the old numbers exactly. The shaman's data change has no switch.
  - Global cooldown: `tables.OFF_GCD`, and the engine keeps a running global cooldown.
  - Stormstrike and Maelstrom Weapon: the 11-10 hotfix through `hotfix_text.SHAMAN_1110`, `shaman.MW_PPM_BY_RANK` and
    `MW_HOTFIX_1110`.
  - Blackout: `priest.BLACKOUT_TICKS`.
  - Hammer of Justice: the duplicate removed; it did not change a number.
  - Voice of Truth: back in the paladin's spellbook; the leveling rotation never casts it.
  - Predator's Edge: `hunter.PE_WHOLE_HIT`.
  - Effect at levels 20-60 before any re-tuning (time per kill):
    - Enhancement shaman +7% to +10% slower;
    - warrior -3% to +2%, paladin up to -2.8%, melee hunter -0.5% to -2.3%;
    - priest +2% to +3% at 20; mage -4.7% to +1.7%; rogue within 1%;
    - warlock and druid unchanged.
  - The seven classes' rules re-tuned and their leveling searches raced again: `deep-runs/fl_fix_1115.sh`.
- 2026-11-15, validation pass 2 (the engine after the same night's fight-lab fixes; field builds, 200 duels a matchup, seed 1, the
  same seeds before and after; one standard error is about 3.5 points).
  - Global cooldown: the fight lab's `tables.OFF_GCD` with its running global cooldown, and the duel lab's own guards, handle each
    spell once. In 360 instrumented duels (15 off-GCD spells, 7 classes) no off-GCD cast moved the global cooldown and none was cut
    short; the guards are no-ops now. The shaman layer's own Maelstrom rate (8 a minute at 5/5) was a constant the fight lab no longer
    reads since its hotfix (10 at 5/5): removed, no duel changed.
  - Fixed, engine: a melee side that holds its strikes into Retaliation (`hold_swings`) and is faster than the warrior now leaves its
    reach (`pvp_base.retaliation_escape`, applied after the layer's intent). Holding in reach had given the warrior its swings for
    free: a cat stood in reach from 3 s to 13 s and lost 1,700 health. Druid against warrior 11.5% -> 24% (attacking through instead:
    6.5%).
  - Fixed, layers:
    - the rogue cast Slice and Dice. All three rogue rotations' tuned rules switch it off, but the duel lab drops a rotation's tuned
      vetoes, so the rotation refreshed it at 1-2 points and the opener spent Premeditation's points on it. Now none in a duel. The
      rotation's: priest 3% -> 37%, mage 12.5% -> 40%; the opener's: paladin 1.5% -> 12%;
    - the rogue Blinded a cast with its own Garrote ticking (0.80 a duel against the warlock, ended within 3 s), and reset with
      Blind and Vanish under the foe's dots (the next tick ended the Vanish);
    - the rogue pooled energy in the warrior's reach for Retaliation's 15 s, ahead 72% to 51% and dead at the end. Now it Sprints and
      leaves: against the warrior 5.5% -> 33%;
    - the rogue Vanished out of roots only; now out of slows too. Against the hunter 0% -> 12%, the mage 35% -> 41%;
    - the hunter used Viper Sting against every mana user, though the damage casters' duels end in 12-21 s with half their mana
      left. Now only when its 1,108 mana is a quarter of the pool or more: priest 0.5% -> 8%, mage 71.5% -> 87%, warlock 1.5% -> 8%;
      paladin, shaman and druid unchanged (without Viper Sting the hunter falls from 41% to 3% against the paladin);
    - the paladin's heal-window Repentance met its own Consecration (broken within a second): rogue against paladin 20% -> 9.5%,
      paladin against warrior 95% -> 97%.
  - Checked and left as the data say:
    - the priest: Darkness, Shadowform and Shadow Weaving (x1.33), Shadowform's doubled crit bonus, Improved Mind Flay's ramp, Power
      Word: Shield, Inner Fire's 20 charges, Vampiric Embrace and Devouring Plague healing;
    - the paladin: Templar's Bulwark (an absorb of 100% of maximum health), Divine Shield, Lay on Hands, Holy damage armor does not
      reduce, 4,322 armor. Without Templar's Bulwark it does as well (Divine Shield takes the Forbearance window);
    - Windfury Weapon (two extra attacks with 433 attack power) and Lightning Shield (178 a ball, 3.5 s apart);
    - the druid's cat, the slowest melee in the fight lab at 60, and Forever's Furor, which gives no energy for shifting.
  - Model limits: the open field (a mage kites a slowed warrior: 0%); the hunter's Flare reveals a stealther within 40 yards at the
    start, and its trap at its feet catches a rogue or cat on the line. Forever's rogue has Detect Traps: a data question.
  - Mirrors sit at 42.5-56.5% with 0-2% draws. The order inside a step decides some: the first-listed side wins 81% of rogue mirrors
    (side B leaves stealth by rule), 72% of warrior mirrors and about 59% of mage mirrors; the alternating start order cancels it in
    every mean.
  - Effect on the means (seven pairs not re-run carry pass 1's values): rogue 16% -> 32%, priest 80% -> 75%, paladin 77% -> 76%,
    hunter 63% -> 66%, shaman 60% -> 59%, warlock 51% -> 48%, mage 45% -> 40%, warrior 32% -> 27%, druid 26% -> 27%.
  - Open before the searches:
    - a full matrix on this code;
    - an audit of the dropped tuned vetoes: the duel lab clears every tuned veto, and Slice and Dice showed one can move a class 6-34
      points a matchup (untested: Retribution's Consecration and Hammer of Wrath, Shadow's Devouring Plague and Smite, Marksmanship's
      Multi-Shot and Arcane Shot, Frost's Cone of Cold and gated bolts, Enhancement's Lightning Bolt, the warlock's Corruption and
      Searing Pain, Feral's Shred). Restore each inside the rotation only and keep what wins on the field;
    - saturated cells (priest against warrior, mage and druid; paladin against mage; mage against warrior; hunter against druid) give
      a search no win-rate signal: the health margin decides there.
- Fight-lab issues found on the way (they affect the leveling and raid pages; for the user to decide):
  - off-GCD spells cost a 1.5 s GCD;
  - the 2026-11-12 Stormstrike and Maelstrom Weapon hotfix is server-side and not in forever-spells;
  - Blackout procs from dot ticks (the client's proc mask has no periodic bit);
  - Hammer of Justice's stun is counted twice;
  - Voice of Truth (a trainer spell since 70753) is dropped;
  - Predator's Edge: the fight lab multiplies only the off-hand weapon's own damage by 1.5. Its aura (A_MOD_OFFHAND_DAMAGE_PCT)
    is a damage modifier on the whole off-hand hit, attack power included, as the raid simulator applies it. The melee Survival
    hunter's off hand is undervalued about 20%. Found 2026-11-14 comparing a guildmate's swords to a two-hander: the staff led by
    1.1% under the lab's rule and tied (±0.2%) under the whole-hit rule.
- 2026-11-15, the full matrix on the current code (`pvp_field.py --matrix --n 200`, `_reference/pvp-matchups.md`; 2 minutes on 2 cores):
  - A first run put the mage at 33%. The mage rules' new `MAGE_ARMOR` knob (Mage Armor from 34, tuned the same day for leveling
    regeneration) reached the duel: `make_module` applies every rules knob, and the side cleared only the vetoes. The duel mage wore
    Mage Armor and lost Ice Armor's armor and its chill on melee attackers: against the druid 62% -> 26%, the shaman 83% -> 76%, the
    rogue 59% -> 53%, the hunter 12% -> 6%. `duel.PVE_KNOBS` now keeps the module's default for such knobs (MAGE_ARMOR), and the
    rerun restores those cells. The other knobs that reach a duel shape the rotation and stay: the priest's WAND_BELOW and
    SHIELD_BELOW, Fire's PYRO_OPENER.
  - Means: paladin 77%, priest 74%, hunter 66%, shaman 59%, warlock 48%, mage 40%, rogue 33%, druid 27%, warrior 26%. Every class is
    within a point of pass 2's means, which had carried pass 1's values for seven pairs.
  - Next: the audit of the dropped tuned vetoes, then the searches.
- 2026-11-15, the dropped-veto audit (`duellab/veto_audit.py`, record `duellab/veto-audit.json`): each field build's tuned leveling
  vetoes restored one at a time inside its spec's rotation only (`duel.restored_vetoes`, `pvp_base.PvPAI.rotation_decide`: a layer's
  own casts of the spell stay free), scored against the field, 200 duels a matchup, the mirror left out. Kept: none.
  - Losses when restored: Devouring Plague -14.6 points of the Shadow priest's mean win rate; Arcane Shot -3.9 and Multi-Shot -1.6
    (Marksmanship); Fire Blast -3.9 (Frost mage); Hammer of Wrath -3.4 and Consecration -2.5 (Retribution); Corruption -0.6
    (warlock).
  - No effect, because the PvP layer already decides these spells: the rogue's Kick, Kidney Shot and Slice and Dice, the hunter's
    Feign Death, the warlock's Searing Pain, the druid's Shred.
  - Within noise: Frostbolt +0.7 (mage, under the 1-point bar), Lightning Bolt +0.1, Smite -0.1, Cone of Cold -0.1. The arms-2h-raid
    rotation has no vetoes.
  - The matrix with the audit's (empty) kept set is unchanged.
- 2026-11-15, the searches set up (step 4):
  - `duellab/pvp_seeds.py`: one seed per tree from the TBC and WotLK PvP builds (26 trees; Demonology has none of its own). The
    seed is our PvP build with the consensus talents (taken by at least half of the tree's expansion builds, Forever's names,
    median rank) added, most-taken first. Each added point is taken back from a talent outside the consensus where the stats model's
    PvP score loses least. A consensus that holds more than 51 points leaves its less-taken talents as "skipped" (Arms: Iron Will 4
    of 5 builds, Death Wish 3 of 5). Renamed talents follow the mapping's note: the expansions' Lightning Mastery is Forever's
    Elemental Alacrity. Same-name talents with another effect (Winter's Chill, Shadow and Flame) are no evidence.
  - `duellab/pvp_search_all.py` (runner `deep-runs/pvp_search_1115.sh`): pvp_search for every tree with a PvP build of ours, from
    our builds, the community's and the seed. The search's last step now races the winner and every start on the same duels
    (seed 3, 240 a matchup, the record's `race`), so the report compares them on equal terms. One tree at a time. The worker count
    is read from `deep-runs/pvp1115/workers` before each tree.
- 2026-11-15 22:52, the search queue stopped and restarted on corrected data. It had run one tree (druid Balance, 21:15-22:41) and
  part of a second when the poison and imbue check (user: "Go full power, go with your recs") found eight spell ranks at Wowhead's
  MaxLevel numbers in forever-spells. The duel lab plays them at 60: Windfury Weapon rank 4 433 extra attack power for the client's
  333, Seal of Command rank 5's judgement +14%, Seal of Fury rank 7's +10%, Holy Nova rank 6's heal +2%. Fixed in
  `live_spells.to_level60` (it brings referenced spells' numbers to 60 now), forever-spells rebuilt. The Balance record moved to
  `deep-runs/pvp1115/stale/`. `deep-runs/pvp_restart_1115.sh` waits for the leveling lane's rules tunes (rogue, shaman, paladin:
  the duel lab plays a rules file's knobs outside `duel.PVE_KNOBS`), runs the matrix, then the queue at Idle on 10 of 12 cores
  (BelowNormal once the lane ends). New PvE knobs kept out of duels: POISONS (pvp_rogue.py puts its own Crippling or Wound Poison
  on the hand the default leaves free), IMBUE_EARLY, IMBUE_LATE, IMBUE_TOP, IMBUE_TOP_FROM (Windfury at 60).
- 2026-11-16 22:01 to 2026-11-17 06:15, the search queue finished all 27 trees (restarted after the 20:17 BrokenProcessPool; records
  `duellab/search/`). Two data changes landed while it ran: Mental Dexterity 150% -> 100% (about 14:00 on 11-16) and the Wrack rework
  (about 13:00). Druid, hunter, mage, paladin and Discipline were searched against the old field shaman. Raced again on today's data,
  every winner's score moved by 0.009 or less, and the field matrix moved only in the shaman's cells (priest against shaman 43% -> 53%).
- 2026-11-17, the blind-spot check (step 4; `duellab/blind_spots.py`, record `duellab/blind-spots.json`, runner
  `deep-runs/pvp_blind_1117.sh`, 06:26-09:53). Per winner:
  - the candidates: the community's builds of the tree, the TBC/WotLK consensus, the class audits' control, escape and defense kinds
    and high ratings, tooltip words, the signature talents;
  - removal costs (40 duels, seed 1); each candidate put back, legal, paid from the cheapest ranks, and raced on the final race's
    duels (seed 3, 240 a matchup); a gain re-raced on seed 4;
  - the casts, damage shares and control on the foe; never-cast abilities; points whose removal changes no duel.
  Findings:
  - Confirmed gains on 14 of 27 trees: the search had not converged (20 steps of 48 random neighbours, no tier-chain moves). Combined
    (scratch improve.py) and raced on seeds 3 and 4, all 14 held: Feral +5.6/+3.6 points (Heart of the Wild, Ferocity, Rend and Tear),
    Holy priest +5.0/+5.2 (Martyrdom, Silent Resolve, Blessed Recovery), Assassination +5.5/+1.6 (Setup, Dirty Tricks), Enhancement
    +2.9/+3.8 (Tidal Focus), Arcane +1.6/+3.8 (Flame Throwing 2 behind 5 Incineration: a 7-point tier chain), and nine more.
  - Pets: the engine never targets a pet (no single-target attack, control or dispel). Lost at 15 s or from the start (scratch
    pet_sensitivity.py), the winners fall: Beast Mastery 95% -> 81% / 48%, Marksmanship 86% / 75% / 59%, the warlocks about 68% -> 23% /
    5% (no AI stall: the demon's damage, Spell Lock and Soul Link go). Hunter and warlock numbers are upper bounds.
  - Ice Block: the check paid it with costly points. The Frost winner's Arcane Shielding read free on 40 duels and costs 1.2 points on
    240, 11 of them against the druid. With the cheapest point (scratch iceblock_pay.py) Ice Block costs Frost 0.6, Arcane 0.0
    and Fire +0.6. A block rule that does not race healers changed nothing (66-68% against the druid either way). Keep it.
  - Holy Shock: `paladin.CASTER_GEAR_FROM` = 0 puts a Holy-path build that has Holy Shock into the caster gear row, and the duels
    reset the knob to that default (`duel.PVE_KNOBS`), so Holy Shock swapped the gear too. In melee gear for both (scratch
    holy_gear.py) Holy Shock costs 2.4 points (75.0% -> 72.6%), not 6.3; the Shockadin start wins 65.8% in melee gear and 58.6% in caster
    gear, so the Holy search ran against Holy Shock. Matchups still swing with it (priest 1% -> 32%, hunter 72% -> 46%). Open: the Holy tree
    searched again with the gear fixed, and the paladin layer's Holy Shock play reviewed.
  - "Never cast" flags that are not: Arcane Power, Presence of Mind and Combustion (applied at the pull), Shadowform, Inner Focus,
    Trueshot Aura, Rage of the Farseer, Soul Link and Amplify Curse (applied without a cast). Real: Fel Domination (a fast re-summon; the lab
    never kills a demon), Bane of Havoc (no use one against one), prerequisites (Sweeping Strikes, Demonic Sacrifice).
  - Payment: a second rule (scratch repay.py: points that changed no duel first, every other at least 0.002 a rank) beat the check's
    payment on few rows (Frost Arcane Resilience -1.1 -> +0.1, Magic Absorption -1.2 -> 0.0, Combat Camouflage, Elemental Reach); the
    report keeps the better of the two.
  - Battleground versions (scratch keepers2.py): the duel build with the talents duels undervalue put back one at a time, the
    high-rated first, each kept while the whole stays within a point of the duel build. Judged by duels only; step 7 measures
    battlegrounds.
- 2026-11-17, the user's decisions on the report (asked for recommendations, then "Go with all your recommendations"):
  1. Pages: the duel lab's results on the research pages now (`<class>/research/pvp/README.md`, a generated "Duel lab" section);
     PvP player pages after round 2. Each player page will carry the duel build and the battleground version, the latter labelled
     as judged by duels only. Battleground scenarios (step 7) are not a precondition.
  2. The signature rule covers PvP in a light form: a PvP build holds its spec's signature talents and casts their spells in its
     duels; no damage-share floor (PvP damage comes in bursts around control).
  3. Round 2, in order:
     - pets targetable: each class's layer answers a pet the way players do (Polymorph, Scare Beast, Hibernate, Fear or Banish on
       a pet, killing a demon), and the warlock re-summons a dead demon (Fel Domination);
     - the Holy paladin's gear row raced both ways in duels (no gear tied to a talent);
     - the search gains tier-chain moves, several payments a move, more steps, and the 14 improved builds as starts;
     - the blind-spot check again, the battleground versions, then the player pages.
     Later: the stats model's calibration (step 5), then battleground scenarios (step 7) as their own project.
  4. CPU order: the night's raid lane and its commit, the eat-and-drink lane (approved the same day), the PvP fixes as code meanwhile,
     PvP round 2 the night after.
- 2026-11-17, round 2's code (the decisions above):
  - Research pages: `duellab/render_pvp_research.py` writes each class's `research/pvp/README.md` "## Duel lab" section (regen step).
  - Pets (`duel.py`, `pvp_base.py`, the druid, hunter and warlock layers):
    - a melee side whose foe stands out of reach swings at the foe's pet in its reach (`PvPAI.swing_at_pet`; not a side that shoots
      or keeps range: a ranged hunter had meleed the Succubus while shooting the warlock);
    - Bestial Wrath makes the pet immune to control; Banish leaves a pet untouchable;
    - Hibernate (druid) and Scare Beast (hunter) on a hunter's pet; Banish on a warlock's demon;
    - the warlock summons a dead demon again through Fel Domination (cast 10 - 5.5 - 2 a Master Summoner rank s; mana -50%, -20% a rank).
    - Tried and dropped: the warlock fearing a hunter's pet cost it 6-9 points against hunters (the Fear belongs on the hunter).
    Effect on the search winners (seed 3, 240): matchups without a pet bit-identical; the warlocks -1 to -9 points against warrior, rogue
    and cat (they kill the demon), +6 to +12 in the mirror (Banish, the re-summon); Marksmanship against the field hunter 95% -> 100%
    (Scare Beast); Beast Mastery unchanged at 96%: Bestial Wrath's 18 s of immunity covers its duels (14-18 s), and no layer switches
    its abilities to the pet (white swings only).
  - The search (`pvp_search.py`): tier-chain moves, the tree's signature talents kept (starts without them skipped), the Holy-path
    paladin with Holy Shock raced in both gear rows, PATIENCE 6; the record carries the winner's signature casts, gear and casts.
    `pvp_search_all.py` adds `duellab/seeds/r2/` (`round2_seeds.py`: the round-1 winner, improved build, battleground version, the
    Holy signature put-back).
  - The blind-spot check races two payments a candidate (the check's costs, and floored: inert points first, every other at least
    0.002 a rank). `duellab/blind_followups.py` (improve, battleground) replaces round 1's scratch scripts; record
    `duellab/results-<date>.json`.
  - Runner `deep-runs/pvp_round2.sh`: waits for the eat-and-drink lane's numbers, then the matrix, the search (--round r2), the check
    (round 1's record kept as `blind-spots-r1.json`), the follow-ups and the research pages. Then the PvP player pages.
