# Mage — Classic baseline talent builds

The community-standard WoW Classic Era builds, used as the *starting point* for WoW: Forever. Every allocation below is machine-validated against the Classic tree data (51 points, tier gating, prerequisites, rank caps). Each build page ends with a talent-by-talent check of what survived into the Forever trees.

| Build | Split | Role | Content | Status | File |
|---|---|---|---|---|---|
| Frost — Arcane Power / Frostbolt (raid DPS) | 31/0/20 | DPS | Raid | Primary | [frost-arcane-power-raid.md](frost-arcane-power-raid.md) |
| Frost — Winter's Chill (raid support) | 17/0/34 | DPS | Raid | Alternative | [frost-winters-chill-raid.md](frost-winters-chill-raid.md) |
| Fire (raid DPS, AQ40 / Naxxramas) | 17/31/3 | DPS | Raid | Alternative | [fire-raid.md](fire-raid.md) |
| Frost (PvP) | 20/0/31 | DPS | PvP | Primary | [pvp-frost.md](pvp-frost.md) |
| AoE grinding — Frost (Improved Blizzard) | 19/0/32 | DPS | Leveling | Primary | [aoe-grinding-frost.md](aoe-grinding-frost.md) |
| AoE grinding — deep Frost 7/0/44 (Shatter + Winter's Chill) | 7/0/44 | DPS | Leveling | Alternative | [aoe-grinding-frost-deep.md](aoe-grinding-frost-deep.md) |
| Leveling — Frost | 17/0/34 | DPS | Leveling | Primary | [leveling-frost.md](leveling-frost.md) |

Classic Era community-standard builds. Frost is the raid spec while Molten Core and Blackwing Lair are full of fire-immune targets; Fire overtakes it from AQ40/Naxxramas. One mage per raid runs the Winter's Chill support build. Allocations validated against the Classic tree data.

Source of truth: `builds.json` in this folder. Regenerate with `python _reference/data/validate_builds.py && python _reference/data/render_builds.py`.

## Report index

Reports under this folder that no other page links to (generated):

- [optimizer/fire-raid-raid-dps.md](optimizer/fire-raid-raid-dps.md): mage / classic-era / spec fire-raid / profile raid-dps
- [optimizer/frost-aoe-leveling-aoe.md](optimizer/frost-aoe-leveling-aoe.md): mage / classic-era / spec frost-aoe / profile leveling-aoe
- [optimizer/frost-leveling-leveling-st.md](optimizer/frost-leveling-leveling-st.md): mage / classic-era / spec frost-leveling / profile leveling-st
- [optimizer/frost-raid-raid-dps-extwc.md](optimizer/frost-raid-raid-dps-extwc.md): mage / classic-era / spec frost-raid / profile raid-dps-extwc
- [optimizer/frost-raid-raid-dps.md](optimizer/frost-raid-raid-dps.md): mage / classic-era / spec frost-raid / profile raid-dps
- [raidsim/fire-raid-environments.md](raidsim/fire-raid-environments.md): DPS by environment — mage fire-raid (Classic Era)
- [raidsim/fire-raid.md](raidsim/fire-raid.md): Raid sim — mage fire-raid (Classic Era)
- [raidsim/frost-raid-environments.md](raidsim/frost-raid-environments.md): DPS by environment — mage frost-raid (Classic Era)
- [raidsim/frost-raid.md](raidsim/frost-raid.md): Raid sim — mage frost-raid (Classic Era)
- [respec-plan.md](respec-plan.md): Mage / classic-era: respec plan for `leveling-st`
