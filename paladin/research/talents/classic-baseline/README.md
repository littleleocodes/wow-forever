# Paladin — Classic baseline talent builds

The community-standard WoW Classic Era builds, used as the *starting point* for WoW: Forever. Every allocation below is machine-validated against the Classic tree data (51 points, tier gating, prerequisites, rank caps). Each build page ends with a talent-by-talent check of what survived into the Forever trees.

| Build | Split | Role | Content | Status | File |
|---|---|---|---|---|---|
| Holy — Raid Healer (31/11/9) | 31/11/9 | HEALER | Raid | Primary | [holy-raid-healer.md](holy-raid-healer.md) |
| Retribution — DPS (11/0/40) | 11/0/40 | DPS | Raid | Alternative | [ret-raid-dps.md](ret-raid-dps.md) |
| Protection — Dungeon/AoE Tank (11/40/0) | 11/40/0 | TANK | Dungeon | Situational | [prot-tank.md](prot-tank.md) |
| Shockadin — Holy/Retribution (PvP) | 31/0/20 | HEALER | PvP | Primary | [pvp-shockadin.md](pvp-shockadin.md) |
| Leveling — Retribution (Seal of Command at 20) | 11/0/40 | DPS | Leveling | Primary | [leveling-retribution.md](leveling-retribution.md) |

Classic Era community-standard builds. Paladins raid as Holy healers (Alliance only in Classic; Forever adds Undead paladins). Retribution DPS and Protection tanking are viable in dungeons and late raids but are not mainstream raid roles in Classic Era. Allocations validated against the Classic tree data.

Source of truth: `builds.json` in this folder. Regenerate with `python _reference/data/validate_builds.py && python _reference/data/render_builds.py`.
