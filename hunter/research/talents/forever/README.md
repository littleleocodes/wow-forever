# Hunter — adapting the Classic builds to WoW: Forever

Data: WoW: Forever beta client build 1.60.1.70009, merged 2026-09-25 (`talent-trees.md`; the 2026-09-13 demo snapshot is archived under `_reference/data/raw/`). Spellbook numbers: `../../spells/README.md`. Point-by-point audit of every
Classic build: `baseline-audit.md`. Proposed builds: `proposed-builds.json` → `builds-README.md`.

## What broke

| Classic talent | Forever | Impact on baselines |
|---|---|---|
| Improved Aspect of the Hawk (BM T1) | **Removed** → *Deadly Aspects* (5): same Hawk proc (2%/rank), plus an Aspect of the Beast melee version | Direct replacement |
| Lethal Shots (MM T2) | **Removed** → *Lethal Attacks* (MM T1, crit with all attacks) | Direct replacement, one tier earlier |
| Aimed Shot (MM T3) | **Removed** as a talent — baseline in the beta (8 ranks from 20, 2s cast, +166 at 60, 6s cooldown shared with Multi-Shot) | Sniper Shot (ranks at 40/48/58) is the new capstone nuke |
| Improved Hunter's Mark | **Removed** | 3 points freed in every raid build |
| Improved Serpent Sting / Scorpid Sting | **Removed** → *Improved Stings* (3) | |
| Mortal Shots | Requires **Careful Aim 5** (new AP-from-Intellect talent) instead of Lethal Shots | Careful Aim is mandatory for MM |
| Trueshot Aura | Tier 7 → **tier 4** (the 16-pt talent); beta ranks +30/40/50/75/50 RAP at 25/32/40/50/60 (rank 5 looks like a data slip) | Cheaper; +75 RAP at 60 |
| Monster Slaying / Humanoid Slaying | **Removed** → *Improved Tracking* (5, +1%/rank vs. tracked type) | Better: works on every tracked type |
| Killer Instinct, Trap Mastery, Improved Feign Death, Wyvern Sting | **Removed** | Survival is now a melee tree (Predator's Edge, Strider Kick, Lacerating Strikes) |
| Thick Hide, Improved Eyes of the Beast | **Removed** | Endurance Training now gives pet armor |
| Intimidation | Requires Bestial Swiftness 1 | BM builds take Bestial Swiftness |
| Surefooted | 3 ranks, 1% hit per rank (Classic 3 ranks = 3%) | Same |
| Efficiency | 3%/rank (Classic 2%/rank) | Better |

## What's new and matters

- **Lone Wolf** (MM T3): +20% damage with no pet — `mm-lone-wolf-raid`.
- **Careful Aim** (AP from Intellect), **Lethal Attacks**, **Sniper Shot**, **Rapid Killing / Rapid Recuperation** (Rapid Fire and mana).
- **Focused Fire** (+2% damage with a pet), **Summon Hawk** (BM 16-pt), **Deadly Aspects**.
- **Improved Tracking**, **Predator's Edge**, **Expose Prey**, **Strider Kick**, **Lacerating Strikes** — melee Survival.

## Decisions made in the proposed builds

1. **BM/MM 20/31/0** keeps the Classic shape with the replacements above; Rapid Killing as the tier-3 filler.
2. **Lone Wolf 0/32/19** is the petless alternative; the launch comparison is Lone Wolf vs. pet damage + Focused Fire.
3. **Survival melee 9/10/32** is a pure test build.
4. **BM solo 31/20/0** adds Summon Hawk; **PvP 0/31/20** adds Survival Tactics and Counterattack.

## To verify at launch

- Aimed Shot is baseline (confirmed); the beta cut its bonus (+166 at 60 vs Classic +600) and made Multi-Shot a single rank with no flat bonus.
- Trueshot Aura rank 5 (+50 at 60 is below rank 4's +75: bug or intended?); Careful Aim is 20%/rank of Intellect; Deadly Aspects 2%/rank confirmed.
- Lone Wolf vs. pet in raid conditions (pet survival on raid bosses was a real problem in Classic).
- Whether melee Survival scales with dual-wield (Predator's Edge off-hand damage).
