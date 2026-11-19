# Warrior — Classic baseline talent builds

The community-standard WoW Classic Era builds, used as the *starting point* for WoW: Forever. Every allocation below is machine-validated against the Classic tree data (51 points, tier gating, prerequisites, rank caps). Each build page ends with a talent-by-talent check of what survived into the Forever trees.

| Build | Split | Role | Content | Status | File |
|---|---|---|---|---|---|
| Fury — Dual Wield (raid DPS) | 17/34/0 | DPS | Raid | Primary | [fury-dw-raid.md](fury-dw-raid.md) |
| Fury — Two-Handed / Improved Slam (raid DPS) | 17/34/0 | DPS | Raid | Alternative | [fury-2h-raid.md](fury-2h-raid.md) |
| Protection — Raid Tank (11/5/35) | 11/5/35 | TANK | Raid | Primary | [prot-raid-tank.md](prot-raid-tank.md) |
| Arms — Mortal Strike (PvP) | 31/20/0 | DPS | PvP | Primary | [arms-pvp.md](arms-pvp.md) |
| Leveling — Arms (Mortal Strike at 40) | 31/20/0 | DPS | Leveling | Primary | [leveling-arms.md](leveling-arms.md) |

Classic Era (1.12-era talent trees) community-standard builds. Point allocations are validated by _reference/data/validate_builds.py against the Classic tree data. Flex points are marked; everything else is the consensus core.

Source of truth: `builds.json` in this folder. Regenerate with `python _reference/data/validate_builds.py && python _reference/data/render_builds.py`.

## Report index

Reports under this folder that no other page links to (generated):

- [optimizer/arms-2h-raid-leveling-st.md](optimizer/arms-2h-raid-leveling-st.md): warrior / classic-era / spec arms-2h-raid / profile leveling-st
- [optimizer/fury-dw-raid-raid-dps.md](optimizer/fury-dw-raid-raid-dps.md): warrior / classic-era / spec fury-dw-raid / profile raid-dps
- [optimizer/prot-tank-raid-tank.md](optimizer/prot-tank-raid-tank.md): warrior / classic-era / spec prot-tank / profile raid-tank
- [raidsim/fury-dw-raid-environments.md](raidsim/fury-dw-raid-environments.md): DPS by environment — warrior fury-dw-raid (Classic Era)
- [raidsim/fury-dw-raid.md](raidsim/fury-dw-raid.md): Raid sim — warrior fury-dw-raid (Classic Era)
- [respec-plan.md](respec-plan.md): Warrior / classic-era: respec plan for `leveling-st`
