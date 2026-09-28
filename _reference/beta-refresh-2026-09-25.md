# Beta data refresh, 2026-09-25: what was released, what changed, what the model now says

Written 2026-09-25, eight days into the WoW: Forever beta. Everything Forever-specific in this project now rests on
beta client build **1.60.1.70009** (2026-09-24) instead of the BlizzCon demo transcription of 2026-09-13.

## Summary

- The beta opened 2026-09-17 with a **level-20 cap** (30 "after a couple of weeks", not yet announced); five client
  builds shipped, and build 70009 (2026-09-24) carried the first class tuning.
- The talent trees were re-read from the beta client: **467 talents** (demo 469/470), every rank's tooltip real (the
  demo had ~280 talents with extrapolated ranks), two trees renamed, six talents cut or replaced, four moved.
- Every class spellbook was pulled from the client (1,753 rank tooltips with learn level, cost, cast, cooldown and
  coefficient): most direct-damage spells deal about half their Classic damage at 60; several cast times, cooldowns
  and learn levels differ from Classic.
- The scorer was re-tuned: the parser learned the beta's "improves your chance to hit" wording, 37 hand-entered
  talent effects were corrected against the real tooltips, 11 spec models took the beta's cast times, cooldowns,
  learn levels and damage shares, and every optimizer report, respec plan, audit and checklist was regenerated.
- Builds that moved the most: Warrior two-hander (Arms 38/13/0 now beats Fury), Rogue daggers (Combat/Mutilate
  21/28/2 instead of 33/16/2), Paladin Retribution (20/0/31 instead of 10/8/33), Shaman Enhancement (1/34/16 instead
  of 20/31/0), Warlock Shadow Bolt (10/11/30, Demonic Sacrifice is back), Druid Balance (36/2/13), Mage AoE grinding
  (19/0/32) and lone-mage Frost (21/0/30 with Winter's Chill at 5 stacks).

## 1. What was released between 2026-09-17 and 2026-09-25

| Date | Event |
|---|---|
| 2026-09-17 | Beta opens (builds 1.60.1.69876 and 69893). Level cap 20; Skyborne, Zephras Isle, Hall of Thanes (13-18), Ruins of Lordaeron (15-20), all zone content to 20. Beta runs to 2026-10-21. |
| 2026-09-18 | Build 69913: client fixes only (no talent, spell, racial or Legacy table changed). |
| 2026-09-22 | Build 69977: client fixes only. |
| 2026-09-24 | Build 70009 + development notes: first class tuning (Druid, Hunter, Mage, Paladin, Priest, Shaman, Warlock, Warrior), racial and item changes (Eureka! 10%, wands no spell-damage scaling, Wizard Oils reverted), respecs at 1 silver (beta only), Cooldown Manager and gamepad testing. |

The tuning is summarised in `wow-forever-overview.md`; the talent-affecting parts: Improved Holy Strike and Crusade
removed (Paladin), Elemental Alacrity/Elemental Fury rows swapped with new prerequisites (Shaman), Mangle → Primal Bite
and Primal Fury → Blood Frenzy (Druid), Holy Strike/Holy Power/Sacred Arbiter/Vengeance/Two-Handed Weapon
Specialization/Twist of Light retuned (Paladin), Bloodthrill and Improved Slam retuned (Warrior), Strider Kick (Hunter),
Wake of Fire and Hot Streak windows (Mage), Rage of the Farseer and Lava Burst (Shaman), Wrath +50% (Druid).

## 2. Data pulled

Three independent reads of the beta client were merged by `_reference/data/refresh_forever_talents.py` (raw pulls
archived under `_reference/data/raw/2026-09-25-beta-70009/`):

| Source | Build | Gave |
|---|---|---|
| talentsforever.com `data.json` (CC BY 4.0) | 70009 | Every rank's tooltip, rank caps, positions; class spellbooks; level-60 spell tooltips |
| thewowdb.com trait snapshots | 70009 | Rows, columns, rank caps, prerequisite arrows straight from the Trait tables |
| warcraftforever.games payload | 69893 | Talent ids, icons, Classic status/diff/tooltips, removed-Classic-talent lists |

Cross-checks: the two 70009 sources agree on every position, rank cap and prerequisite except one arrow (Nature's
Splendor ← Nature's Majesty, missing from the trait-edge snapshot, kept because two client reads carry it). The 69893
and 70009 tooltips agree on 1,238 of 1,315 ranks; the 77 differences are exactly the 2026-09-24 tuning plus rounding
("1.0 sec" vs "1 sec"), and the older text is kept in `ranks_prev` for those talents.

Against the demo snapshot (`_reference/data/forever-talents/README.md` has the per-talent lists):

| Class | Talents | Cut / replaced | Moved | Text of previously real ranks changed | Extrapolated ranks now real |
|---|---|---|---|---|---|
| Druid | 51 | Balance of Nature cut; Mangle → Primal Bite; Primal Fury → Blood Frenzy | — | 21 | 32 |
| Hunter | 50 | — | — | 18 | 29 |
| Mage | 54 | — | — | 30 | 25 |
| Paladin | 50 | Improved Holy Strike, Crusade cut (70009) | — | 24 | 28 |
| Priest | 53 | — (tree "Shadow Magic" → "Shadow") | — | 27 | 29 |
| Rogue | 53 | Restless Blades → Flawless Execution | — | 22 | 28 |
| Shaman | 50 | — (tree "Elemental Combat" → "Elemental") | Elemental Alacrity 6→3, Elemental Fury 3→6 (70009); Tidal Mastery 1→4, Totemic Focus 4→1 | 21 | 28 |
| Warlock | 52 | Drain Hope → Wrack | — | 23 | 35 |
| Warrior | 53 | Vitality cut | Bastion 6→5 | 19 | 35 |

Spellbooks: `_reference/data/forever-spells/<class>.json` (built by `build_forever_spells.py`), rendered to
`<class>/spells/README.md`. Cross-checked against the ElliotWood/Forever simulator's beta pass, which read the same
client tables and lists old → new per spell.

## 3. Model changes

**Parser.** The beta client writes "Improves your chance to hit by 3%" without a subject; the parser now reads it as
hit with everything (Paladin/Rogue/Warrior Precision, Warlock Suppression, Druid Nature's Reach had lost their hit
values on re-parse).

**Hand-entered effects corrected against the real tooltips** (each entry's note carries the arithmetic):

- Druid: King of the Jungle (Tiger's Fury grants 20/40/60 Energy, not 20), Furor (100% Energy kept at 5/5), Moonkin
  Form (Omen of Clarity procs doubled); Primal Bite and Blood Frenzy renamed; Balance of Nature removed.
- Hunter: Focused Fire (also buffs the pet), Improved Stings (6/13/20), Trueshot Aura (+75 RAP at 60, not +100),
  Sniper Shot and Summon Hawk (ranked spells), Strider Kick (+speed).
- Mage: Winter's Chill (5 stacks: +10% Frostbolt/Ice Lance crit at 5/5 instead of +2%), Shatter (17/33/50), Fingers of
  Frost (15% for 1/2 spells), Improved Counterspell (4s), Impact (3/7/10).
- Paladin: Holy Power (+Holy Strike crit), Sacred Arbiter (20%), Vengeance (3 stacks), Twist of Light (-20% Seal
  mana), Redoubt (6%/rank block at 2%/rank chance); Improved Holy Strike removed.
- Priest: Improved Power Word: Shield (7/14/20), Mental Agility (3/7/10), Searing Light (2/5), Vampiric Embrace
  (1 min cooldown → half uptime), Penance ranks.
- Rogue: Flawless Execution replaces Restless Blades (Eviscerate -10 Energy ≈ +7% Energy-bound damage); Hack and
  Slash dagger crit confirmed 1-5%.
- Shaman: Mental Dexterity (100% of Intellect as AP at 3/3, three times the demo read), Mental Quickness (30%),
  Stormstrike (+20% on the next Lightning Bolt/Chain Lightning/Earth Shock, not all Nature damage), Rage of the
  Farseer (attack speed only), Lightning Overload (3/7/10), Lava Burst (ranked, 1.3× a Lightning Bolt in 2.5s).
- Warlock: Wrack replaces Drain Hope; Improved Drains (flat 7/13/20) and Soul Siphon (4/8/12% per Affliction effect)
  reworked; Demonic Knowledge (also the pet); Incinerate (ranked, +20% on the filler slot); Agonizing Flames (3/7/10);
  Fire and Brimstone (8/17/25).
- Warrior: Bloodthrill (4-20% main-hand only: doubled), Improved Slam (Slam is an 18s-cooldown hit, not a rage dump);
  Vitality removed.

**Spec models** (`_reference/data/scorer/specs/`; every change is in the model's note with the beta numbers):
Hunter Multi-Shot 6s cooldown and smaller yellow-shot shares (Multi-Shot lost its flat +150, Aimed Shot rank 6 is +166
vs Classic +600, Arcane Shot up); Paladin Holy Strike from level 6 on a 10s cooldown, Consecration 8s, Lay on Hands
20 min, Protection shares (Holy Strike 18%, Consecration 27%); Priest Power Word: Shield 4s cooldown; Rogue Rupture
and poison shares down (both ~30% weaker than Classic); Shaman Lightning Bolt 2.5s, Chain Lightning 2s, shocks up
(Lightning Bolt 52%, Earth Shock 16%, Flame Shock 12%); Warrior Protection threat shares (Sunder Armor 35% on its
explicit 1013 threat, Revenge 17%), Thunder Clap 6s; Druid and Warlock notes record the halved base damage (shares
stand because everything moved together).

**Builds.** Nine hand-drafted builds lost points to cut talents and were re-spent (each notes the change): Druid
Moonkin (Balance of Nature → Improved Entangling Roots/Overgrowth) and Regrowth healer (→ Improved Wrath), Shaman
Elemental/Enhancement/leveling (Restoration re-laid around Totemic Focus and Restorative Totems) and PvP Elemental
(Alacrity 3 for Call of Thunder), Paladin healer/Ret/Shockadin/leveling (Crusade → Conviction/Vindication) and tank
(Improved Holy Strike → Divine Strength), Warrior tank (Vitality → Focused Rage/Improved Revenge). Renamed talents and
trees were replaced everywhere. All 96 builds validate.

## 4. Results: optimizer builds before → after

Scores are each model's gain over its own talentless baseline; compare within a row only.

| Class / model | Demo snapshot (2026-09-18 runs) | Beta 70009 (2026-09-25) | Why |
|---|---|---|---|
| Hunter mm-raid / raid-dps | 20/31/0-style, 17/31/3 | 9/37/5 (+61%) | Yellow-shot talents worth less after the Aimed/Multi-Shot cuts; deep Marksmanship for Sniper Shot |
| Hunter mm-lonewolf / raid-dps | abs index 1.96 vs 1.88 pet | 7/39/5 (+98%) | Same shape; Lone Wolf's +20% intact |
| Mage frost-raid / raid-dps | 28/0/23 (Fingers of Frost, no Winter's Chill) | 21/0/30 (+119%) | Winter's Chill stacks to 5 (+10% crit) |
| Mage frost-aoe / leveling-aoe | 10/0/41 | 19/0/32 (+51%) | Arcane Meditation/Concentration worth more with the real mana numbers |
| Mage fire-raid / raid-dps | 17/31/3 | 14/32/5 (+91%) | Elemental Precision 5/5 in Frost |
| Warrior arms-2h / raid-dps | Fury 19/32/0 (+81%) beat Arms (+73%) | **Arms 38/13/0 (+87%)** beats Fury (+82%) | Bloodthrill doubled and main-hand only; Slam an 18s hit |
| Warrior prot-tank / raid-tank | 8/5/38 (+88%) | 8/5/38 (+87%) | Same core; Vitality gone, Focused Rage in |
| Rogue daggers / raid-dps | 33/16/2 Mutilate (+92%) | 21/28/2 (+91%) | Flawless Execution + Hack and Slash crit pull points into Combat |
| Rogue swords / raid-dps | 19/32/0 (+57%) | 18/33/0 (+58%) | Same |
| Priest holy-heal / raid-heal | 23/28/0 (+64%) | 22/29/0 (+85%) | Improved PW:S 20% and Mental Agility 10% |
| Priest shadow / raid-dps | 18/0/33 (+101%) | 20/0/31 (+111%) | Same core |
| Paladin ret / raid-dps | 10/8/33 (+115%) | 20/0/31 (+102%) | Crusade gone, Vengeance 3 stacks; Holy Power's Holy Strike crit and Improved Seals pull 20 into Holy |
| Paladin prot / raid-tank | 2/31/18 (+62%) | 4/31/16 (+56%) | Redoubt re-valued; Righteous Fury 60% |
| Paladin holy / raid-heal | 23/0/28 (+44%) | 23/0/28 (+44%) | Unchanged |
| Shaman elemental / raid-dps | 31/7/13 (+87%) | 31/6/14 (+99%) | 2.5s Lightning Bolt, Alacrity at tier 3, Lava Burst |
| Shaman enhancement / raid-dps | 20/31/0 (+95%) | 1/34/16 (+105%) | Mental Dexterity (100% Int → AP), Water Shield; Elemental shock talents dropped |
| Shaman resto / raid-heal | 0/10/41 (+73%) | 0/10/41 (+73%) | Unchanged |
| Warlock sb-raid / raid-dps | 21/0/30 (+135%) | 10/11/30 (+147%) | Demonic Sacrifice (Imp: +15% Shadow) plus Shadow and Flame |
| Warlock affliction / raid-dps | 31/0/20 (+118%) | 21/0/30 (+110%) | Wrack weaker than the Drain Hope estimate; Destruction's Shadow and Flame worth more |
| Warlock fire-destro / raid-dps | 9/11/31 (+162%) | 9/11/31 (+170%) | Incinerate's real numbers |
| Warlock affliction-leveling / leveling-st | 31/16/4 | 25/24/2 (+36%) | Demonology pet talents (Demonic Knowledge on the pet) |
| Druid balance / raid-dps | 38/0/13 (+126%) | 36/2/13 (+157%) | Balance of Nature gone; Moonfury 2%/rank |
| Druid cat / raid-dps | 9/35/7 (+104%) | 9/35/7 (+113%) | King of the Jungle's 60 Energy |
| Druid bear / raid-tank | 9/40/2 (+83%) | 9/40/2 (+83%) | Unchanged |
| Druid resto / raid-heal | 11/5/35 (+94%) | 11/5/35 (+102%) | Unchanged shape |
| Druid cat / leveling-st | 0/35/16 | 12/31/8 (+42%) | Balance's Nature's Majesty/Reach and Insect Swarm for leveling |

Respec plans (`<class>/talents/forever/respec-plan.md`), the buff/nerf reports (`_reference/data/scorer/changes/`),
the loop audit (222 flags; 26 open) and both checklists were regenerated from the same run.

## 5. Still open

- **The beta cap is 20**, so `_reference/beta-checklist.md` (written for the announced cap of 30) is only testable
  through rows 1-3 and the first 11 points until Blizzard raises it.
- **Cross-spec baselines** (`abs_dps_factor`) are still 1.0 except Hunter. The ElliotWood/Forever simulator's beta
  pass gives per-spec average DPS in its own presets (some "naked"), so only within-class ratios are informative:
  Mage Frost 277 / Arcane 275 / Fire 190; Druid Cat 304 / Bear 231 / Balance 177; Hunter BM 447 / MM 330 / Survival 300;
  Shaman Enhancement 174 / Elemental 121; Warlock Affliction 234 / Destruction 174; Rogue Assassination 326 / Combat
  320 / Subtlety 284; Warrior Fury 314 / Arms 253 / Protection 235; Paladin Retribution 429 / Protection 281; Priest
  Shadow 339 / Smite 156. Not adopted: the sim's rotations, gear presets and talent choices differ from the
  models' baselines; measure time-to-kill in the beta instead.
- **Trait-table vs notes disagreements:** Bastion/Focused Rage (the notes say swapped; tables say not), Nature's
  Splendor's arrow (two reads have it, one does not).
- **Client data slips:** Aspect of the Hawk rank 6 (55 RAP, below rank 5), Trueshot Aura rank 5 (+50, below rank 4's
  +75), Penance rank 4's bolt (131) smaller than rank 3's (180), Holy Fire's non-monotone dot.
- **Mechanics the tables cannot settle:** Wrack's practical uptime, Fingers of Frost charge consumption mid-cast,
  Maelstrom Weapon's proc rate, Venom's interaction with a running Deadly Poison, Twist of Light Echo damage, whether
  melee-table Holy damage partially resists.
- **Spec models** still use fixed shares; the halved base damage across casters changes spell-power scaling
  (coefficients rose at low ranks), which the model does not see.

## 6. Repeating the refresh for the next beta build

```
python _reference/data/refresh_forever_talents.py --fetch --raw 2026-10-DD-beta-NNNNN --previous 2026-09-25-beta-70009
python _reference/data/build_forever_spells.py --raw 2026-10-DD-beta-NNNNN
python _reference/data/scorer/effects.py
# read _reference/data/forever-talents/README.md; fix builds/manual entries it lists; then
python _reference/data/scorer/run.py <class> --spec <model> --profile <profile> --write --export   # every report in <class>/talents/forever/optimizer/
python _reference/data/validate_builds.py && python _reference/data/render_builds.py && python _reference/data/render_trees.py
python _reference/data/scorer/compare_effects.py; python _reference/data/scorer/respec.py <class> --write; python _reference/data/scorer/loop_audit.py
python _reference/data/render_optimizer_sections.py; python _reference/data/build_launch_checklist.py; python _reference/data/build_beta_checklist.py
```
