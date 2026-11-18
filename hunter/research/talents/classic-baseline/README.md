# Hunter — Classic baseline talent builds

The community-standard WoW Classic Era builds, used as the *starting point* for WoW: Forever. Every allocation below is machine-validated against the Classic tree data (51 points, tier gating, prerequisites, rank caps). Each build page ends with a talent-by-talent check of what survived into the Forever trees.

| Build | Split | Role | Content | Status | File |
|---|---|---|---|---|---|
| Beast Mastery / Marksmanship (raid DPS, 20/31/0) | 20/31/0 | DPS | Raid | Primary | [bm-mm-raid.md](bm-mm-raid.md) |
| Marksmanship / Survival — Surefooted (raid DPS, 0/31/20) | 0/31/20 | DPS | Raid | Alternative | [mm-surv-hit-raid.md](mm-surv-hit-raid.md) |
| Beast Mastery (solo / farming / pre-raid, 31/20/0) | 31/20/0 | DPS | Solo/farming | Situational | [bm-solo-farm.md](bm-solo-farm.md) |
| Marksmanship / Survival (PvP, 0/31/20) | 0/31/20 | DPS | PvP | Primary | [pvp-mm-surv.md](pvp-mm-surv.md) |
| Leveling — Beast Mastery | 31/20/0 | DPS | Leveling | Primary | [leveling-beast-mastery.md](leveling-beast-mastery.md) |

Classic Era community-standard builds. The raid build is Beast Mastery/Marksmanship (Improved Aspect of the Hawk + Trueshot Aura); Marksmanship/Survival with Surefooted is the low-hit variant. Allocations validated against the Classic tree data.

Source of truth: `builds.json` in this folder. Regenerate with `python _reference/data/validate_builds.py && python _reference/data/render_builds.py`.
