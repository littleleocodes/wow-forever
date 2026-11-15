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
