# Priest — adapting the Classic builds to WoW: Forever

Data: WoW: Forever beta client build 1.60.1.70291, captured 2026-10-08 (`_reference/data/data_build.py`; the trees in
[talent-trees.md](talent-trees.md)). Spellbook numbers: [spells](../../spells/README.md). Point-by-point audit of every Classic build:
[baseline-audit.md](baseline-audit.md). Builds: [proposed-builds.json](proposed-builds.json), one page each under
[leveling/builds](../../leveling/builds/), [raid/builds](../../raid/builds/) and [pvp/builds](../../pvp/builds/). What to play: the
[leveling](../../../leveling/README.md) and [raid](../../../raid/README.md) player pages.

## What broke

| Classic talent | Forever (build 70291) | Impact on Classic builds |
|---|---|---|
| Divine Spirit | **Removed**; trained at 30/40/50/60 | The reason every Classic healer put 21 points in Discipline is gone |
| Unbreakable Will, Improved Power Word: Fortitude, Force of Will | **Removed** | Discipline's tier 1-2 fillers are now Twin Disciplines, Power in Light, Holy Precision |
| Healing Focus | **Removed**; Twilight Focus (3 ranks, 70% pushback protection for every spell) takes its place | Same job, one more point |
| Improved Prayer of Healing, Lightwell, Improved Vampiric Embrace | **Removed** | Nothing core lost |
| Spiritual Healing | **3 ranks**, 10% | Cheaper, same total |
| Spiritual Guidance | Up to 25% of Spirit as healing and 8% as spell damage | Also a damage talent |
| Meditation | **3 ranks, up to 50%** | Much stronger |
| Inspiration | 3 ranks, 25% armor | Same |
| Improved Healing | Also covers Penance and Prayer of Mending | |
| Power Infusion | Requires **Penance** | Power Infusion builds are Penance builds |
| Shadow Weaving | A **self-buff**: +2% Shadow damage a stack, 5 stacks, 15 s | No debuff slot needed |
| Improved Psychic Scream | Requires Blackout 5 | Shadow PvP takes Blackout 5/5 |

## What's new and matters

- **Penance** (Discipline tier 5): since 2026-10-08 more mana-efficient than Heal and Greater Heal; both priest raid healers take it.
- **Renewed Hope** (tier 5), **Divine Aegis** (tier 6), **Soul Warding** (tier 4): a shield and crit Discipline healer.
- **Prayer of Mending** (Holy capstone, requires Spirit of Redemption), **Binding Heal** (tier 4), **Litany of Light**: Holy throughput and mana.
- **Improved Mind Flay**, **Devouring Contagion**, **Early Demise**: with Shadow Word: Death and Devouring Plague trained by every priest, Shadow has a full damage kit.

## To verify at launch

- Penance, Prayer of Mending and Binding Heal numbers at 60.
- Shadow Word: Death's backlash in a raid (10% of your health each time the target survives).
- The low-rank penalty on healing ranks (no formula published; this project assumes TBC's).
