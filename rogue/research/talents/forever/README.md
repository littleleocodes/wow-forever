# Rogue — adapting the Classic builds to WoW: Forever

Data: WoW: Forever beta client build 1.60.1.70291, captured 2026-10-08 (`_reference/data/data_build.py`; the trees in
[talent-trees.md](talent-trees.md)). Spellbook numbers: [../../spells/README.md](../../spells/README.md). Point-by-point audit of
every Classic build: [baseline-audit.md](baseline-audit.md). Builds: [proposed-builds.json](proposed-builds.json), one page each under
[../../leveling/builds/](../../leveling/builds/), [../../raid/builds/](../../raid/builds/) and [../../pvp/builds/](../../pvp/builds/).

## What broke

| Classic talent | Forever | Impact on baselines |
|---|---|---|
| Sword/Dagger/Mace/Fist Weapon Specialization (Combat) | **Removed** → *Hack and Slash* (5 ranks, Combat tier 5): swords and axes 5% extra attacks, daggers and fists 5% crit, maces armor ignored | Same slot, same role |
| Improved Backstab | **Removed** → *Puncturing Wounds* (3 ranks, Combat tier 2): Backstab +30% crit and a 45% chance of an extra combo point, Mutilate +15% crit | Better than what it replaces |
| Improved Eviscerate | Moved Assassination tier 1 → Combat tier 1 | The Assassination dip shrinks by 3 points |
| Improved Gouge | Moved Combat tier 1 → Assassination tier 1 | A tier-1 Assassination filler |
| Opportunity | 5 ranks → 2 ranks (+10%, now also Mutilate) | Dagger builds save 3 points for 10% less Backstab damage |
| Master of Deception, Precision, Deflection | 5 ranks → 3 ranks | Cheaper |
| Weapon Expertise | +weapon skill → 1% less chance to be dodged or parried per rank (2 ranks) | No longer fixes glancing blows |
| Vigor | Assassination tier 7 → tier 5, 2 ranks (+10 energy) | Cheap for any deep Assassination build |
| Lethality | 6% → 4% crit damage a rank (20% at 5); now also Mutilate, Ghostly Strike and Hemorrhage | Weaker, wider |
| Sleight of Hand, Improved Sap, Deadliness | **Removed** | No baseline used them |

## What's new and matters

- **Mutilate** (Assassination tier 5) and **Venom** (the capstone) with **Seal Fate** at 100%: the dagger spec Blizzard built
  Assassination around. Neither is in the simulator's best Assassination raid build (2026-10-15): a launch question.
- **Flawless Execution** (Combat 16-point): Eviscerate costs 10 less energy; it replaced Restless Blades in beta build 69893.
- **Premeditation** is the Subtlety 16-point talent, **Thousand Cuts** the capstone (Rupture ticks cheapen Hemorrhage and
  Backstab), **Quietus** and **Cutthroat** fill tier 6.

## Builds

The current picks per spec and mode are on the player pages: [leveling](../../../leveling/README.md) and
[raid](../../../raid/README.md); the research behind them is under [../../leveling/](../../leveling/) and [../../raid/](../../raid/).

## To verify at launch

- Glancing blows and weapon skill: with Weapon Expertise reworked, nothing in the trees replaces +weapon skill.
- Mutilate and Venom damage at 60, and whether Mutilate needs a dagger in each hand (Blizzard says so; the tooltip does not).
- Poison charges and proc rates with Improved Poisons.
