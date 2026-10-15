# Paladin — adapting the Classic builds to WoW: Forever

Data: WoW: Forever beta client build 1.60.1.70291, captured 2026-10-08 (`_reference/data/data_build.py`; the trees in
[talent-trees.md](talent-trees.md)). Spellbook numbers: [spells](../../spells/README.md). Point-by-point audit of every Classic build:
[baseline-audit.md](baseline-audit.md). Builds: [proposed-builds.json](proposed-builds.json), one page each under
[leveling/builds](../../leveling/builds/), [raid/builds](../../raid/builds/) and [pvp/builds](../../pvp/builds/). What to play: the
[leveling](../../../leveling/README.md) and [raid](../../../raid/README.md) player pages.

The reasons behind Classic's splits changed: Blessing of Kings and Consecration are baseline, blessings last an hour, and Holy Strike
and Seal of Fury are baseline abilities the trees are built around.

## What broke

| Classic talent | Forever (build 70291) | Impact on Classic builds |
|---|---|---|
| Blessing of Kings, Blessing of Sanctuary | **Removed**; Kings is baseline | The 11-point Protection dip of the Classic healer is pointless |
| Improved Blessing of Might, Improved Blessing of Wisdom | **Removed** | The Retribution dip and Holy's Improved Wisdom are gone |
| Consecration | **Removed**; baseline | Retribution and Protection no longer dip Holy for it |
| Improved Seal of Righteousness, Improved Lay on Hands, Lasting Judgement | **Removed** | Holy's fillers are now Improved Seals, Reverence, Voice of Truth, Purifying Power |
| Improved Seal of the Crusader, Sanctity Aura, Improved Retribution Aura | **Removed** | Retribution loses its raid debuff and aura role; Improved Seals (+15% seals and judgements) takes the damage part |
| Improved Devotion Aura, Improved Concentration Aura | **Removed** | Nothing core lost |
| Holy Shock | **Tier 5** (1 point); Light's Vigil and Divine Precision require it | Deep Holy is built around it, but the healer lab's raid pick skips it |
| Illumination | Requires **Reverence 3** | 3 extra points on the way |
| Holy Shield | Tier 7; requires **Templar's Bulwark** | The tank capstone chain |
| Vengeance | Up to 3 stacks of 3% after non-periodic crits; requires Sanctified Judgement 3 | A Retribution chain |
| Reckoning | 5 ranks: 40% on a block, 100% after a non-periodic crit, once every 1.5 s | |
| Precision | 3 ranks, 3% hit | Retribution builds take a Protection dip for it |

## What's new and matters

- **Twist of Light** (Retribution capstone): seals 20% cheaper, and a replaced seal's Echo rides your next swing: seal twisting.
- **Templar's Bulwark**, **Iron Creed**, **Swift Judgement**, **Improved Seal of Fury**, **Sacred Duty**: a real tank tree.
- **Sanctified Judgement**, **Holy Conduit**, **Sacred Arbiter**, **Champion of the Light**, **Instrument of Law** (Retribution).
- **Light's Vigil** (Holy capstone): a cooldown-free Holy Shock that heals a whole party; **Infusion of Light**, **Reverence**,
  **Divine Precision**, **Voice of Truth**.

## To verify at launch

- Seal twisting: whether every Echo fires on the next swing (the simulator's reading) or only one.
- Judgement of Fury's taunt on raid bosses.
- Holy Strike and Seal of Fury threat values in play.
