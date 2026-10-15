# Mage — adapting the Classic builds to WoW: Forever

Data: WoW: Forever beta client build 1.60.1.70291, captured 2026-10-08 (`_reference/data/data_build.py`; the trees in
[talent-trees.md](talent-trees.md)). Spellbook numbers: [spells](../../spells/README.md). Point-by-point audit of every Classic build:
[baseline-audit.md](baseline-audit.md). Builds: [proposed-builds.json](proposed-builds.json), one page each under
[leveling/builds](../../leveling/builds/), [raid/builds](../../raid/builds/) and [pvp/builds](../../pvp/builds/). What to play: the
[leveling](../../../leveling/README.md) and [raid](../../../raid/README.md) player pages.

## What broke

| Classic talent | Forever (build 70291) | Impact on Classic builds |
|---|---|---|
| Improved Arcane Explosion, Magic Attunement, Improved Mana Shield | **Removed** | The Arcane fillers on the way to Arcane Meditation are gone; tier 3 now offers Arcane Geometry, Arcane Impact and Arcane Blast |
| Improved Arcane Missiles | Renamed **Improved Channeling** (5 ranks; also 70% protection for Arcane Blast) | Same role |
| Incinerate, Improved Fire Blast | Incinerate is **Incineration** (crit for Fire Blast, Scorch, Ice Lance, Arcane Blast); Improved Fire Blast removed (Wake of Fire takes 2 s off Fire Blast's cooldown) | Fire's tier 1 changes |
| Elemental Precision | **5 ranks, 1% hit each** | Hit costs 2 more points |
| Arcane Meditation | **3 ranks, up to 50%**; requires Arcane Concentration 5 | More regen for 3 points |
| Ice Block, Cold Snap | Ice Block at tier 4; Cold Snap at tier 5, the Ice Barrier prerequisite | Deep Frost reaches Ice Block cheaper |
| Shatter | **3 ranks, up to +50%** crit against frozen targets; no prerequisite | 2 points cheaper |
| Winter's Chill | Raises only your own Frostbolt and Ice Lance crit (+2% a stack, 5 stacks) | A crit self-buff, not a raid debuff |
| Improved Scorch | Your own Fire damage +3% a stack, 5 stacks | A personal debuff |
| Improved Counterspell | 2 ranks, 4 s silence | Unchanged role |
| Arcane Power | +30% damage, +30% mana cost; requires Presence of Mind | Same burst |

## What's new and matters

- **Ice Lance** (Frost tier 3) and **Fingers of Frost** (tier 5): Shatter crits without a freeze; every Frost build takes them.
- **Heating Up** (Fire tier 4; Hot Streak until build 70170): each crit takes 25% off the next Pyroblast's cast, 3 stacks.
- **Arcane Blast** (tier 3) and **Missile Barrage** (tier 4): the Arcane spec, and free Arcane Missiles for Frost builds too.
- **Frostfire Bolt** (trained at 40, 50, 60): Fire and Frost at once; the Frostfire hybrid is built on it.
- **Arcane Mind** adds +100% Arcane crit damage.

## To verify at launch

- Fingers of Frost on bosses (15% per chill, 2 spells); Ice Lance's spell-power coefficient (the client row has none; the simulator uses 0.10).
- Arcane Missiles' bonus per Arcane Blast stack (tooltip 10%, beta logs 15%).
- Whether Presence of Mind shares Combustion's cooldown in play (client data says so).
- Fire immunity in The Barrow Deeps and Hyjal Summit.
