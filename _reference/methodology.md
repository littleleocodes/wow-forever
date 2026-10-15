# Methodology — from Classic optimal builds to Forever builds

## Why start from Classic

WoW: Forever is built on the Classic Era class kits and talent structure. The Classic community spent years
converging on optimal builds per spec and role (raid DPS/heal/tank, PvP, leveling). Those builds encode two
things that transfer even when the trees change:

1. **Which talents define the spec** — the capstone and the 2–4 throughput talents everything else feeds
   (e.g. Bloodthirst / Dual Wield Specialization / Flurry for Fury; Ruin / Demonic Sacrifice for warlocks).
2. **The value ranking of filler talents** — which points are mandatory, which are flex, which are junk.

## Pipeline

```
Classic Era tree data  ─┐
                        ├─► builds.json (Classic baseline, validated) ─► baseline-audit.md (vs. Forever)
Community guides       ─┘                                                       │
                                                                                ▼
Forever beta tree data ──────────────────────────────────────► proposed-builds.json (Forever, validated)
```

1. **Capture the Classic baseline** for every spec/role in `<class>/research/talents/classic-baseline/builds.json`,
   with a priority-ordered `core` list (why each talent is there) and explicit `flex` entries.
   Allocations are validated against the real Classic tree data (`validate_builds.py`).
2. **Audit each baseline against Forever** (`baseline-audit.md`, generated): for every point, is the talent
   unchanged, changed (tooltip/rank/position), moved, or removed? Removed points are *orphaned*.
3. **Re-spend into a proposed Forever build** (`proposed-builds.json`):
   - keep every surviving core talent unless its Forever version no longer does the job;
   - spend orphaned points on the closest Forever equivalent (Tactical Mastery → Improved Tactical Mastery,
     Sword Specialization → Weaponmaster), then on new talents that strengthen the spec's core loop;
   - re-check tier gating in the Forever tree (talents moved tiers);
   - record `open_questions` — what must be checked at launch (numbers, procs, whether a new spell is worth a slot).
4. **Validate** the Forever build for point math against the Forever data, render, and mark it `draft`.

## What a proposed Forever build is — and is not

- **Is:** a legal 51-point allocation on the beta-client trees that preserves the Classic spec's logic and uses the
  new talents that obviously fit. A good day-one starting point.
- **Is not:** play-tested. Tooltip numbers are the beta client's level-60 values (the current build is named by
  `_reference/data/data_build.py`: 1.60.1.70291 since 2026-10-08, 70170 from 2026-10-03, 70009 from 2026-09-25; before that level-38 demo values with
  partly extrapolated higher ranks), and Blizzard will retune before launch. Since 2026-09-26 the drafts are also raced in the
  fight lab, the community raid simulator and the healer lab (next section); every number there is a model, not a measurement.
  Treat every build as a hypothesis with a list of things to verify.

## From hand drafts to the builds on the player pages (2026-10-15)

The hand drafts above are the starting answer; the builds the player pages show are decided by simulation. In order:

1. **Stats model** (`scorer/`): tooltip numbers to effects, spec models and profiles; finds legal builds and leveling orders
   (section "Stats model" below). Calibrated to the simulators, never the last word.
2. **Fight lab** (`fightlab/`, leveling, solo): time per kill at levels 20-60; leveling pages rank on it.
3. **Raid simulator** (the ElliotWood/Forever wowsims fork, `raidsim/`, level 60): races, talent values and rotation searches on a
   training dummy; raid pages rank on **full-raid DPS** (user decision 2026-10-02).
4. **Healer lab** (`heallab/`): capacity of a healer keeping a five-member group alive; tanks by tank value in the simulator.
5. **Searches** that write derived builds (🔬 on the pages): derived builds per spec (2026-09-30), the machine-learning raid
   pipeline (2026-10-01), the open talent searches across every split with synergy certificates (2026-10-04 to 10-07), the deep
   searches per class (2026-10-03) and the 70291 sweep (2026-10-09 to 10-15). A derived build replaces a hand draft only when it is
   0.5% better (since 2026-10-07); the hand draft stays as the alternative.
6. **Each spec plays its own rotation** (user rule 2026-10-08): no build is ranked on another spec's rotation because it is faster.

Rules and commands: `CLAUDE.md`; tool overview: `_reference/README.md`; open items: `HANDOFF.md`.

## Priorities when trees conflict

1. Capstone and 16-point talent of the spec's main tree.
2. Flat throughput multipliers (crit, damage %, cast-time, hit) — hit first while gear is weak.
3. Resource talents (mana regen, rage/energy generation).
4. Utility/survival (only what the role needs).
5. Fillers: choose the one that at least does *something* (health, pushback, range).

## Refresh procedure (when new data lands)

1. `python _reference/data/check_beta_build.py` says whether a newer beta client exists and prints the command.
2. `python _reference/data/refresh_forever_talents.py --fetch --raw <date>-beta-<build>`, then `build_forever_spells.py`,
   `scorer/effects.py`, `render_trees.py`, `validate_builds.py` (lists every proposed build the new trees broke) and
   `render_builds.py`; `forever-talents/README.md` (generated) lists what moved.
3. Repair the broken builds in `proposed-builds.json`, then the simulator audits, races and searches listed under
   "Forever-specific rules" in `CLAUDE.md`.

## Leveling orders — how "what to take at what level" is decided

Every leveling build (`leveling-*` in each class's `proposed-builds.json`) carries an `order` list that the
validator simulates level by level. The order is produced with the following rules, in priority order.

### 1. Hard constraints (mechanical, non-negotiable)

| Rule | Consequence |
|---|---|
| 1 talent point per level from 10 → level *L* has *L* − 9 points | 51 points at 60 |
| Tier *n* needs 5 × (*n* − 1) points already in that tree | Earliest tier unlocks: **T2 at 15, T3 at 20, T4 at 25, T5 at 30, T6 at 35, T7 at 40** — only if every earlier point went into that tree |
| Prerequisite arrows | e.g. Bestial Wrath needs Intimidation, which now needs Bestial Swiftness |
| End at 60 in a build you want to keep | Each leveling build ends in (or one filler-swap away from) a proposed 60 build, so no respec is needed |

Because the new **16-point talents** sit in tier 4, every tree now has a real ability available at **level 25**
(Stormstrike, Mangle, Swiftmend, Trueshot Aura, Ice Block, Vampiric Embrace, Restless Blades, Summon Hawk, …).
That is the single biggest structural change from Classic leveling, where the comparable milestones were 30–40.

### 1b. Earlier rows are always candidates

Tier gating only sets a *minimum* below a tier; it never forces the next point into the newest row. So at every
level the candidate set is **every talent in every unlocked tier** of the tree (plus tier 1 of the other trees).
Backfilling a tier-1/2 talent at level 33 is normal when the current row has nothing better — e.g. Hunter
Focused Fire at 33-34, Warrior Improved Heroic Strike at 19, Mage Elemental Precision at 37-47, Druid Ferocity at
24 and 33. The validator does not choose talents; it only proves the chosen order is legal at every level.

### 2. Value ranking for the points that are free to move

1. **Kill speed** — flat damage/crit/haste multipliers, cheaper builders, the spec's main attack.
2. **Downtime** — mana return (Spirit Tap, Improved Life Tap, Shamanistic Focus), self-healing (Vampiric Embrace,
   Siphon Life), rage/energy generation (Improved Charge, Furor).
3. **Survival of the thing that tanks** — the pet for hunters/warlocks (Unleashed Fury, Improved Revive Pet),
   bear Stamina for druids, Ice Block/Ice Barrier for mages.
4. **Milestone timing** — take whatever gating filler is needed so the tier-7 talent lands exactly at 40 (Mortal
   Strike, Adrenaline Rush, Bestial Wrath, Shadowform, Ice Barrier, Rage of the Farseer, Berserk, Drain Hope).
   Exception: Paladin Twist of Light is deliberately delayed to 48 because Improved Seals + Divine Strength in the
   20s are worth more than an unknown capstone.
5. **Utility** last (range, threat, PvP-only effects) unless needed as filler.

### 3. Estimating a talent that did not exist in Classic

| Case | How it is valued | Example |
|---|---|---|
| **Renamed/moved Classic talent** with the same numbers | Exactly as its Classic self | Deadly Aspects = Improved Aspect of the Hawk (2%/rank haste proc) |
| **Replacement with a Classic analogue** | Compare rank-1 number × ranks to the analogue | Hack and Slash sword 1%/rank → 5% = Sword Specialization; Weaponmaster likewise |
| **New flat multiplier** | Rank-1 % × max ranks, treated as "real" (these rarely change) | Focused Fire 1%/rank → +2%; Malediction 1%/rank → +5% DoTs; Nature's Reach 2%/rank → +4% hit |
| **New proc with a rate** | Rate × trigger frequency while leveling; if the trigger is "always on" the talent is rated high | Bloodthrill: Rend is on every mob → 10% Overpower procs = strong; Fingers of Frost: every Frostbolt chills → high |
| **New active ability** | Rated by what it replaces in the rotation, using tooltip numbers only for *relative* size | Ice Lance: instant + 300% vs. Frozen replaces the Nova → Frostbolt burst; Summon Hawk: 53 damage at 38 = "an extra pet", not a burst button |
| **Mechanic we cannot see** (Echoes, Eclipse charges, Maelstrom stacks) | Taken only when nothing better sits in the tier, and listed under `open_questions` | Twist of Light, Rage of the Farseer's uptime |
| **Demo text that looks like a transcription artefact** | Ignored for ranking; flagged | Winter's Chill "stacks up to 1", Shadow Mastery 1%/rank |

Numbers to distrust most, in order: higher-rank values marked *(est.)* (extrapolated), then any flat damage number
(level-60 beta tooltips), then proc rates. Percent-per-rank multipliers are the most trustworthy.

### 4. Where the Classic order was kept vs. changed (summary)

| Class | Kept from Classic | Changed because of Forever |
|---|---|---|
| Warrior | Rend → Deep Wounds → Impale → Sweeping Strikes at 30 → Mortal Strike at 40 | Weaponmaster replaces the weapon spec; Improved Slam and Bloodthrill before 40; Improved Battle Shout gone |
| Rogue | Combat first, Adrenaline Rush at 40, Assassination after | Improved Eviscerate is a tier-1 Combat pick; Restless Blades at 25; Hack and Slash replaces Sword Spec |
| Mage | Improved Frostbolt → Ice Shards → Shatter | Ice Lance at 20, Ice Block at 25, Fingers of Frost at 30, Ice Barrier at 40 (not 43) |
| Warlock | Improved Corruption first, Siphon Life at 30 | Malediction/Pandemic/Malevolence replace the removed drain talents; Drain Hope at 40; Destruction after 40 |
| Priest | Spirit Tap → Mind Flay at 20 → Shadowform at 40 | Vampiric Embrace at 25; Shadow Weaving is a self-buff; Unbreakable Will gone |
| Paladin | Benediction → Seal of Command at 20 | Holy dip at 21-28 for Improved Seals + Divine Strength; Twist of Light at 48 |
| Hunter | Hawk-haste first, pet talents, Bestial Wrath at 40 | Summon Hawk at 25; Bestial Swiftness is now an Intimidation prerequisite; Careful Aim before Mortal Shots |
| Shaman | Thundering Strikes first | Stormstrike at 25 (was 40); Shamanistic Focus at 20; Maelstrom Weapon and Rage of the Farseer replace Weapon Mastery |
| Druid | Sharpened Claws at 20, Leader of the Pack at 30 | Heart of the Wild is now the first five points; Rend and Tear + Berserk at 35-40; Furor/Naturalist after 40 |

## Stats model (supersedes hand ranking where available)

The rules in sections 1–4 describe how the first drafts were made by hand. The **scorer** in
`_reference/data/scorer/` encodes the same reasoning as data and arithmetic: tooltip numbers become effects, a spec
model says where damage, healing or threat comes from, a profile says what "better" means (time per kill saved;
raid DPS; healing throughput + mana; threat + mitigation), and the optimizer searches builds and orders. It is
calibrated by rediscovering the Classic community builds from Classic tooltips (see `scorer/README.md`). All nine
classes are covered, including healer models (Priest, Paladin, Shaman, Druid) and tank models (Warrior, Paladin,
Druid).

### Why the community takes a talent (loops)

Time-to-kill and downtime do not explain every talent: Improved Frost Nova is taken because the AoE cycle needs a
second Nova before the pack closes, not for its damage. `scorer/loop_audit.py` lists every community-taken talent
the model under-values, and `scorer/loops/<class>.json` records the spec's purpose, its loop and, per talent, the
role and the guide's reason with a source. Mechanical reasons become numbers derived from the loop, entered for
both games so the reasoning carries over to Forever (and scales when the talent changed); tier fillers are
documented as fillers rather than inflated. Mage AoE was the first case: two Classic reference builds (Icy Veins
19/0/32 without Shatter, Warcraft Tavern 7/0/44 with it) and a Forever order that now takes Improved Frost Nova at
15-16 and Improved Blizzard at 20-22.

### Buffs and nerfs are preserved, and builds are allowed to change

Both games are encoded from their own tooltips, so a talent that lost half its value (Shadow Mastery 10% → 5%,
Winter's Chill, Dual Wield Specialization) or gained (Arcane Meditation, Meditation, Reflection) carries that
into every build automatically; `scorer/changes/<class>.md` lists the verdict per talent. A Forever build is
therefore *not* required to resemble its Classic ancestor: the report's "Builds that changed" section shows which
Classic core talents each Forever build drops and what it takes instead (e.g. Warlock Shadow Bolt builds trade
DS/Ruin for Conflagrate → Shadow and Flame; Rogue raids move from swords to Mutilate daggers; Shaman Restoration
rebuilds around Water Shield and Riptide).

### Respecs while leveling

A build that is best at 60 is not always best at 25. `scorer/respec.py` builds a plan per (spec, target level
20/30/40/50/60) — the best build for that level, bought in optimizer order, then extended greedily — and a dynamic
programme picks the switching levels that minimise total leveling hours after paying the respec fee (1g, then
+5g each, cap 50g, converted to hours through a gold-per-hour table). The result is
`<class>/research/leveling/respec-plan.md` (and a Classic version for calibration).

Results (2026-09-16 encodings): for every class the Forever answer is "never respec" — the level-20/30/40
optimal build, extended greedily, is within an hour of any schedule and usually *beats* playing toward the
60-build from level 10, because the 60-build's path delays early value for late capstones. Where a class has two
leveling models with unmeasured baselines (Mage Frost/Fire, Warrior 2H/DW, Rogue swords/daggers, Shaman
Enhancement/Elemental, Druid Cat/Balance) the page also gives the best schedule per model, since a switch between
models rests on the assumption that talentless characters of both kill equally fast. The Classic runs reproduce
known patterns — Enhancement until 40 then Elemental for Shaman, a Retribution respec into Protection filler at
50 for Paladin — which is the calibration for the tool.
