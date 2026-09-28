# Classic 1.12 creature stats (cmangos classic-db, z2815) — pulled 2026-09-26

`creature_stats.csv` is the part of the CMaNGOS Classic world database that the fight lab uses for mob health, melee damage,
armor and the caster share by level (`_reference/data/fightlab/mob_stats.py --extract <dump.sql>` wrote it; `mob_stats.py --write`
turns it into `_reference/data/fightlab/mob_stats.json`, which `tables.py` reads).

- Source: https://github.com/cmangos/classic-db — `Full_DB/ClassicDB_1_12_1_z2815.sql.gz` (13 MB, 73 MB unpacked; not archived here).
- Tables used: `creature_template` (one row per creature template: `MinLevel`/`MaxLevel`, `MinLevelHealth`/`MaxLevelHealth`,
  `MinMeleeDmg`/`MaxMeleeDmg` (the sniffed 1.12 client values; base attack power included), `DamageMultiplier`, `Armor`,
  `MeleeBaseAttackTime`, `UnitClass`, `Rank`, `CreatureType`, `NpcFlags`, `UnitFlags`, `Civilian`, `Faction`) and `creature`
  (world spawns; `Spawns` is the count per template).
- Rows: 10,384 templates, 66,310 spawns. The fight lab's filter (normal rank, combat creature types, attackable, no NPC flags,
  not civilian, melee damage > 0, spawned at least once) keeps 2,262 templates / 43,198 spawns.
- Checks made on 2026-09-26: `MinLevelHealth` already includes `HealthMultiplier` (Flesh Eater 664 = classlevelstats 651 × 1.02);
  99% of the kept templates have `DamageMultiplier` 1.0, so applying it to the explicit damage columns changes the medians
  by nothing; damage examples: Plaguehound (55-56) 97-120 per 2.0 s, Ghostpaw Runner (19-20) 28-36, Kobold Vermin (1-2) 0-1.
- `item_stats.csv` (8,024 green-or-better armor pieces and weapons with their fixed stats, armor, damage, speed, quality, slot,
  class mask and required level) and `quest_rewards.csv` (2,948 quest → reward item links) feed `gear_stats.py` → `gear_stats.json`
  (gear by level and tier). World-drop greens with random suffixes carry their stats in client DBCs and are not in the pool.
- Caveat: these are Classic Era numbers. WoW: Forever creature stats are server side and the beta client does not carry them;
  the Wowhead Forever NPC tooltips list level and type only. Treat the derived tables as the prior until beta measurements exist.
