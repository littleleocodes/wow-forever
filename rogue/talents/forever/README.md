# Rogue — adapting the Classic builds to WoW: Forever

Data: WoW: Forever beta client build 1.60.1.70009, merged 2026-09-25 (`talent-trees.md`; the 2026-09-13 demo snapshot is archived under `_reference/data/raw/`). Spellbook numbers: `../../spells/README.md`. Point-by-point audit of every
Classic build: `baseline-audit.md`. Proposed builds: `proposed-builds.json` → `builds-README.md`.

## What broke

| Classic talent | Forever | Impact on baselines |
|---|---|---|
| Sword/Dagger/Mace/Fist Weapon Specialization (Combat T5) | **Removed** → *Hack and Slash* (5): sword/axe 5% extra attacks, dagger/fist crit, mace armor ignore | Same slot, same role; dagger/fist crit is 1%/rank (5% at 5/5), mace 15% armor |
| Improved Backstab (Combat T2) | **Removed** → *Puncturing Wounds* (3): +30% Backstab crit, +15% Mutilate crit, 45% extra combo point on Backstab | Better than what it replaces |
| Improved Eviscerate | Moved Assassination T1 → Combat T1 | Assassination dip shrinks by 3; Combat tier 1 is now all useful |
| Improved Gouge | Moved Combat T1 → Assassination T1 | Tier-1 Assassination filler |
| Opportunity | 5 ranks → 2 ranks (+10% total instead of +20%) | Dagger builds lose 10% Backstab damage but save 3 points |
| Master of Deception | 5 → 3 ranks | Cheaper stealth |
| Weapon Expertise | +5 weapon skill → -1% dodge/parry per rank | No longer solves glancing blows — biggest unknown for raid rogues |
| Vigor | Capstone (T7) → T5, 2 ranks (+10 energy) | Now cheap for any deep-Assassination build |
| Precision | 5 ranks → 3 ranks (1%/rank, 3% total) | 2 points cheaper |
| Sleight of Hand, Improved Sap, Deadliness | **Removed** | No baseline used them |

## What's new and matters

- **Mutilate** (Assassination T5) + **Venom** (capstone) + Seal Fate at 100% — a complete dagger raid spec that never
  existed in Classic. `assassination-mutilate-raid` is the draft.
- **Flawless Execution** (Combat 16-pt): Eviscerate costs 10 less Energy. It replaced Restless Blades (cooldown reduction on finishers) in beta build 69893.
- **Puncturing Wounds**, **Hack and Slash** — the replacements above.
- **Premeditation** is now the Subtlety 16-point talent; **Thousand Cuts** is the Subtlety capstone; **Quietus** / **Cutthroat** fill tier 6.
- **Lethality** buffed to 6% per rank and now covers Mutilate, Hemorrhage and Ghostly Strike.

## Decisions made in the proposed builds

1. **Combat Swords 18/33/0**: Combat needs 33 to hold everything (Improved Eviscerate, Precision, Flawless Execution, Hack and Slash, Weapon Expertise, Aggression, Adrenaline Rush); Assassination drops Murder to 1.
2. **Combat Daggers 16/33/2**: conservative dagger adaptation (Puncturing Wounds + Hack and Slash + Opportunity 2).
3. **Assassination Mutilate 31/20/0**: the speculative new dagger spec — compare against Combat daggers at launch.
4. **PvP Seal Fate 30/8/13** maps one-to-one; **PvP Hemo/Prep 20/0/31** goes deeper for Thousand Cuts.

## To verify at launch

- Glancing blows / weapon skill: with Weapon Expertise reworked, does anything replace +5 weapon skill? (Edgemaster's Handguards-style gear may become mandatory.)
- Hack and Slash dagger/fist crit 1-5% (confirmed by the client curve).
- Mutilate and Venom damage at 60; poison charge mechanics.
- Adrenaline Rush stays at 5 minutes (Restless Blades is gone).
