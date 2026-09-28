# Mage — adapting the Classic builds to WoW: Forever

Data: WoW: Forever beta client build 1.60.1.70009, merged 2026-09-25 (`talent-trees.md`; the 2026-09-13 demo snapshot is archived under `_reference/data/raw/`). Spellbook numbers: `../../spells/README.md`. Point-by-point audit of every
Classic build: `baseline-audit.md`. Proposed builds: `proposed-builds.json` → `builds-README.md`.

## What broke

| Classic talent | Forever | Impact on baselines |
|---|---|---|
| Improved Arcane Explosion, Magic Attunement, Improved Arcane Missiles, Improved Mana Shield | **Removed** | The Arcane fillers every build used to reach Arcane Meditation are gone; tier 3 now offers Arcane Geometry / Arcane Impact / Arcane Blast |
| Incinerate, Improved Fire Blast | **Removed** | Fire tier 2–3 fillers change (Flame Throwing, Impact, Burning Soul 3 ranks) |
| Elemental Precision | 3 ranks (6%) → **5 ranks (1%/rank)** | Hit costs 2 more points; every raid build pays it |
| Arcane Meditation | 5%/rank → **17/33/50%** and now requires Arcane Concentration 5 | Much stronger regen for the same 3 points |
| Ice Block / Cold Snap | Ice Block moved to tier 4 (the 16-pt talent), Cold Snap to tier 5 and is now the Ice Barrier prerequisite | Deep Frost gets Ice Block cheaper |
| Shatter | 5 ranks (+50%) → 3 ranks (+17/33/50%); no longer requires Improved Frost Nova | 2 points cheaper |
| Winter's Chill | Now only buffs Frostbolt/Ice Lance crit (+2% per stack, 5 stacks in the beta client) | A 10% crit self-buff for Frost |
| Improved Counterspell | 4s silence (the demo transcription read 2s) | Unchanged |
| Arcane Power | +30% damage / +30% mana cost, requires Presence of Mind | Same burst, more mana |
| Arcane Focus | Arcane-only hit (1%/rank), moved to tier 1 | Pure filler for Frost/Fire |

## What's new and matters

- **Ice Lance** (Frost T3) + **Fingers of Frost** (T5): a Shatter-crit rotation against unfreezable bosses — `frost-fingers-of-frost-raid`.
- **Hot Streak** (Fire 16-pt): three crits → a 1.5s Pyroblast; possibly a rotation change for Fire.
- **Arcane Blast** (T3) + **Missile Barrage** (Arcane 16-pt): the seed of an Arcane DPS spec (AB stacks +10% to *other* spells per cast until another spell is cast). Not drafted yet — needs numbers.
- **Incineration** (Fire T1): crit for Scorch/Fire Blast/Ice Lance/Arcane Blast.
- **Arcane Mind** now also +100% Arcane crit damage; **Arcane Instability** unchanged shape.

## Decisions made in the proposed builds

1. **Frost AP 31/0/20** and **Winter's Chill 17/0/34** keep their Classic shapes; fillers re-routed through the new tier-3 Arcane talents; Elemental Precision 5/5 in both.
2. **Fingers of Frost 12/0/39** added as the speculative deep-Frost alternative.
3. **Fire 15/31/5**: Hot Streak replaces Incinerate; Elemental Precision 5/5 instead of Arcane Meditation (flex noted).
4. **PvP Frost 20/0/31**: Ice Lance + Fingers of Frost added; Frostbite recommended over Piercing Ice.

## To verify at launch

- Whether Winter's Chill (5 stacks confirmed) still affects other mages' Frostbolts.
- Fingers of Frost on bosses (15% chance, 2 spells at rank 2); Ice Lance rank 6 is 136-161 at 60.
- Hot Streak Pyroblast (1.5s) vs. Fireball.
- Arcane Blast numbers — an Arcane raid build may exist.
- Fire immunity in The Barrow Deeps / Hyjal Summit.
