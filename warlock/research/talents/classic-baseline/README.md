# Warlock — Classic baseline talent builds

The community-standard WoW Classic Era builds, used as the *starting point* for WoW: Forever. Every allocation below is machine-validated against the Classic tree data (51 points, tier gating, prerequisites, rank caps). Each build page ends with a talent-by-talent check of what survived into the Forever trees.

| Build | Split | Role | Content | Status | File |
|---|---|---|---|---|---|
| DS/Ruin — Demonic Sacrifice + Ruin (raid DPS) | 7/21/23 | DPS | Raid | Primary | [ds-ruin-raid.md](ds-ruin-raid.md) |
| SM/Ruin — Shadow Mastery + Ruin (raid DPS) | 30/0/21 | DPS | Raid | Alternative | [sm-ruin-raid.md](sm-ruin-raid.md) |
| Soul Link / Nightfall (PvP) | 20/31/0 | DPS | PvP | Primary | [pvp-soul-link.md](pvp-soul-link.md) |
| Leveling — Affliction / Demonology (Voidwalker) | 30/21/0 | DPS | Leveling | Primary | [leveling-affliction-demo.md](leveling-affliction-demo.md) |

Classic Era community-standard builds. Raiding is Shadow Bolt spam: DS/Ruin (sacrificed Succubus, +15% shadow damage) is the top damage build, SM/Ruin keeps a pet (Imp for Blood Pact) and is only slightly behind. Allocations validated against the Classic tree data.

Source of truth: `builds.json` in this folder. Regenerate with `python _reference/data/validate_builds.py && python _reference/data/render_builds.py`.
