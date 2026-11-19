# Audit brief (2026-11-19)

For a fresh Claude Code session (Fable 5.2, `claude-fable-5-2`), running locally on this PC in `F:\wow-forever`. The user, on
2026-11-19: "I think we're going to need to do a full audit session with a fresh session on a Fable 5.2 model. To look at issues like
these and any others we might have missed." The lane session (Opus 5.5) keeps running the queue below; this session audits.

Read `CLAUDE.md` (loaded automatically) and `_reference/README.md` first, then this page.

## Why: the Ice Barrier miss

Forever's Ice Barrier is the 31-point Frost talent. Its tooltip: "absorbing 447 damage and increasing your Frost damage by 15% for
1 min. While shielded, your Frost damage is increased by an additional 5%", on a 30 s cooldown, so it can stay up all fight. Every
Frost build skipped it until the user asked "how is Ice Barrier not worth it?" Three gaps lined up:

1. **The fight lab modelled the shield only.** `fightlab/mage.py` coded Classic's Ice Barrier (an absorb, no pushback). The checks
   after a data change (`fightlab/module_lint.py`) look for damage numbers on damage spells. Nothing compared a spell the module
   already handled with every clause of its Forever tooltip.
2. **The raid rotations never cast it, and no raid build held it.** The official simulator models the bonus
   (`sim/mage/ice_barrier.go`, Frigid Power). But no rotation of ours had an Ice Barrier line, so every talent search valued it at 0.
   No build held the talent, so no rotation search could value a line for it: each search waited on the other. The Frost builds sat
   at exactly 30 Frost points. `raidsim/unused_abilities.py` checks only abilities a build already holds.
3. **The duel lab found it and the finding stopped there.** On 2026-11-17 the duel lab modelled the damage (`duellab/pvp_mage.py`
   `ICE_BARRIER_DAMAGE`, with a note that the fight lab omits it). The fight lab was never fixed and nobody was told.

Measured on 2026-11-19, with one Arcane point moved into Ice Barrier:

- raid, full raid: the Frost page build 523 -> 597 DPS (+14%), the best Frost build 614 -> 664 (+8%);
- leveling: the Frost leveling page build 6-8% faster per kill at levels 50-60.

Fixed the same day (commit 6463e0d2): the fight lab models Frigid Power, and the Frost raid rotations cast it. Still owed: the mage
leveling redo.

The user's concern, verbatim: "now the remaining builds and talent trees could also have missed something that crucial."

## The goal

Find the modelling, rotation, search and process gaps that make a page recommend the wrong build, rotation, talent order or gear, or
give a player a wrong instruction. Rank them by their effect on what players see:
1. the raid and leveling picks;
2. the PvP picks;
3. the by-level guides and keybind pages;
4. GearCheck's values (`characters/addon/forever-gear-values.json`, read by the add-on);
5. the user's own characters (`_characters/arcea`, `_characters/tara`).

Report each finding with:
- its evidence: the tooltip text, the line of code, a measured number;
- how large it is;
- the fix;
- the check that would have caught it.

## Failure patterns to hunt

Known patterns, to start from. Look for new ones too.

1. **Partly modelled tooltips.** Ice Barrier's case. Compare every talent's and every spell's Forever tooltip clause with what each
   model implements:
   - the fight lab: `fightlab/<class>.py` (MECHANICS, the hooks) and `fightlab/engine.py`;
   - the healer lab: `heallab/<class>.py`;
   - the duel lab: `duellab/pvp_<class>.py`;
   - the stats model: `scorer/effects/forever/<class>.manual.json`.
   A `classic.status` of "changed" in `forever-spells/<class>.json` marks Forever's rewrites.
2. **Abilities no page build holds whose value shows only with a cast line.** Rotations are in `raidsim/apls/<class>/`. The spell
   probe (`raidsim/spell_probe.py`, the ML pipeline's spells step) last ran on 2026-10-01, on the fork's simulator, before the port to
   the official one.
3. **A gap known in one lab and missing from another.** Each duel layer's docstring lists "Effects the fight lab does not parse"
   (`duellab/pvp_*.py`). Most are PvP-only, such as control and immunities. Check each one for a PvE effect. Then check the healer lab's
   notes the same way.
4. **Deep talents just out of reach.** A 31-point talent one point away, a prerequisite chain, a talent behind a tier the build almost
   fills. Measure what adding each missing talent is worth (below).
5. **Filters that keep spells out of a search:**
   - `apl_opt` (the non-combat filter, `COMBAT_ALLOW`, `cooldown_pool`, `new_spell_pool`);
   - `filler_audit.VERIFIED_UNUSED`;
   - the vetoes in the leveling rules files (`fightlab/rotations/`);
   - the signature rule's lists (`signature_spells.json`);
   - the own-rotation rule (`spec_modes`).
6. **Classic behaviour coded by hand that Forever changed.** For each module, compare its MECHANICS text and hooks with the
   tooltips.
7. **Numbers that silently read 0.** A regex that stops matching a changed wording (the lint covers part), a number referenced from
   another spell (`$NNNs1`, `live_spells.to_level60`), a server value missing from the client tooltip.
8. **Rules that hide better builds.** In PvP, the signature rule's Death Mark cost Subtlety 10 points of duels (2026-11-18; dropped
   for PvP). Also check: one build per spec page, the hybrid keep rules, the 0.5% bars, the variant rules.
9. **Stale data and stale records.** Records from before the current data or simulator pin. Gear pools: the phase rule was fixed on
   2026-11-18.
10. **The models disagree.** A talent's value in the raid simulator, the fight lab and the stats model. A large disagreement points
    at a model gap: Ice Barrier was worth about 0 in the fight lab and +8-14% in the simulator once cast.

## Measured checks the lane session proposed

Adopt them or improve on them:

1. **Raid add-values.** For every damage entry and its page build, take every talent the build lacks, one at a time. Pay for it
   from the build's cheapest points by removal value, and keep it legal (tier gating, prerequisites). A talent that teaches an ability
   gets a cast line: on cooldown, or kept up through its aura, guarded by `auraIsKnown`. Race in a full raid, 3,000-6,000 fights.
   Flag anything over 1%.
2. **Leveling add-values.** The same in the fight lab, at levels 40, 50 and 60, for each leveling page build.
3. **A cross-model value table.** Each talent's value in the raid simulator, the fight lab and the stats model. Review the large
   disagreements by hand.
4. **The leads.** `python _reference/data/tooltip_effect_scan.py` lists 15 leads (2026-11-19). It is a first scan; see its stated
   limit. The leads:
   - druid: Improved Entangling Roots, Feral Instinct, Improved Regrowth;
   - hunter: Bestial Wrath, Trueshot Aura (both may be cast automatically);
   - mage: Arcane Mind, Improved Flamestrike;
   - paladin: Oath of Light;
   - rogue: Hemorrhage;
   - shaman: Guardian Totems, Rage of the Farseer, Restorative Totems;
   - warlock: Demonic Sacrifice, Improved Felhunter;
   - warrior: Improved Whirlwind.

Existing audits to reuse, read or extend:

| Area | Tools and reports |
|---|---|
| Fight lab, simulator, labs | `fightlab/module_lint.py` (`_reference/fightlab-lint.md`), `raidsim/sim_value_audit.py` (`_reference/sim-value-audit.md`), `raidsim/unused_abilities.py`, `raidsim/filler_audit.py`, `raidsim/setting_audit.py` |
| Signature rule and searches | `fightlab/signature_audit.py` and `raidsim/signature_audit.py`, `raidsim/search_check.py` (known positives), `hybrid_check.py` |
| Stats model | `scorer/scenario_audit.py`, `scorer/loop_audit.py` |
| Pages and rotations | `page_lint.py`, `guides.py --check`, `level_guides.py --check`, `raidsim/apl_validate.py`, `raidsim/spec_check.py`, `raidsim/gear_check.py` |
| Logs | `_reference/search-improvements.md`: every past fix and the self-audit checklist |

## The machine and the queue (2026-11-19, 13:00)

- **Running: the gear night.**
  - Script `_reference/data/deep-runs/gear_phase_1118.sh`, log `deep-runs/gear-phase-1118.log`. It belongs to the lane session.
  - It writes:
    - the gear sets: `raidsim/gear_sets/forever/**`, `raidsim/gear-opt.json`, `raidsim/tank-gear.json`, `heallab/heal-gear.json`;
    - the records and builds: `raidsim/specs.json`, `raidsim/ml/*.json`, the classes' `proposed-builds.json`;
    - the race reports and environments;
    - the stat weights and `characters/addon/*.json`;
    - every page (its last step).
  - It ends around 04:00-06:00 Friday 2026-11-20.
  - Until then, do not edit any of those files, the rotation files (`raidsim/apls/**`), or a module it imports. The lane session did
    exactly that today, mid-run, and had to stop the run and redo the Frost record. Reading is fine.
- **CPU.** The night uses 10 of the 12 logical processors at BelowNormal. The user's rule: never more than 10 of 12. "Low power" means
  Idle priority on 2 processors. Run an audit job at Idle on the same processors (`deep-runs/throttle.ps1 -ProcId <pid> -Reserve 2
  -Priority Idle`), or wait for the night to end.
- **Queued after it, in the lane session:**
  1. the gear night's review, commit and push, and a message to the Addons session;
  2. the Beast-Survival raid page (`open_builds.py hunter --kept-only --only raid --write --race --regen`);
  3. the mage leveling redo for Ice Barrier;
  4. the user's no-rules search: worktrees `F:/wow-forever-unrestricted` and `F:/wow-forever-unrestricted-raid`, and
     `duellab/pvp_unrestricted.py`.
  The audit's findings may come before item 4: the no-rules search needs correct models.
- **Uncommitted on purpose:** the gear night's outputs (about 80 files), `gearcheck*.jpg` and `_characters/*/level-said.json`.

## Working alongside the lane session

- One working tree, two sessions.
  - Write findings to `_reference/audit-1119.md` (new).
  - Code fixes: after the gear night, agreed with the user. Two sessions editing the same file is how work gets lost.
  - Stage only your own files (`git add -- <paths>`, never `git add -A` or `.`). Ask the user before pushing.
- Messages: `ListAgents` lists the local sessions, and `SendMessage` reaches the lane session; or go through the user. The Addons
  session (`F:/wow-addons`) owns the GearCheck and RestCue add-ons and reads both add-on files from origin/main.
- Standing rules from the user (CLAUDE.md has the rest):
  - privacy: never print RestedXP guide text or the account folder's name; the Blizzard key and tokens stay in
    `~/.wow-forever-tools`; the user's email address stays private;
  - lanes: stop a lane's bash processes with Stop-Process, never TaskStop; never edit a running bash script; never change a rules or
    rotation file while its search runs;
  - ask before starting a new queue over the classes;
  - each spec plays its own rotation and its signature spells (CLAUDE.md, Structure rules);
  - write tersely and factually, with absolute dates.

## Start

    cd F:\wow-forever
    claude --model claude-fable-5-2

First prompt: "Read _reference/audit-brief-1119.md and run the audit it describes. Start read-only: the gear night is running."
