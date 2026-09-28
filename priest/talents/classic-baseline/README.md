# Priest — Classic baseline talent builds

The community-standard WoW Classic Era builds, used as the *starting point* for WoW: Forever. Every allocation below is machine-validated against the Classic tree data (51 points, tier gating, prerequisites, rank caps). Each build page ends with a talent-by-talent check of what survived into the Forever trees.

| Build | Split | Role | Content | Status | File |
|---|---|---|---|---|---|
| Holy — Raid Healer (21/30/0) | 21/30/0 | HEALER | Raid | Primary | [holy-raid-healer.md](holy-raid-healer.md) |
| Discipline / Holy — Power Infusion (raid healer) | 31/20/0 | HEALER | Raid | Alternative | [disc-power-infusion-healer.md](disc-power-infusion-healer.md) |
| Shadow (PvP) | 7/0/44 | DPS | PvP | Primary | [pvp-shadow.md](pvp-shadow.md) |
| Leveling — Shadow | 7/0/44 | DPS | Leveling | Primary | [leveling-shadow.md](leveling-shadow.md) |

Classic Era community-standard builds. Priests raid as Holy healers (Discipline for Divine Spirit, Inner Focus and Mental Agility); Discipline/Holy with Power Infusion is the late-game alternative; Shadow is for PvP and leveling. Allocations validated against the Classic tree data.

Source of truth: `builds.json` in this folder. Regenerate with `python _reference/data/validate_builds.py && python _reference/data/render_builds.py`.
