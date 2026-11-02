# Shaman — Classic baseline talent builds

The community-standard WoW Classic Era builds, used as the *starting point* for WoW: Forever. Every allocation below is machine-validated against the Classic tree data (51 points, tier gating, prerequisites, rank caps). Each build page ends with a talent-by-talent check of what survived into the Forever trees.

| Build | Split | Role | Content | Status | File |
|---|---|---|---|---|---|
| Restoration — Raid Healer (0/5/46) | 0/5/46 | HEALER | Raid | Primary | [resto-raid-healer.md](resto-raid-healer.md) |
| Elemental — Raid DPS (31/0/20) | 31/0/20 | DPS | Raid | Alternative | [elemental-raid-dps.md](elemental-raid-dps.md) |
| Enhancement — Windfury Support / Melee (0/31/20) | 0/31/20 | DPS | Raid | Situational | [enhancement-raid-support.md](enhancement-raid-support.md) |
| Elemental / Nature's Swiftness (PvP, 30/0/21) | 30/0/21 | DPS | PvP | Primary | [pvp-elemental-ns.md](pvp-elemental-ns.md) |
| Leveling — Enhancement (two-hander) | 0/31/20 | DPS | Leveling | Primary | [leveling-enhancement.md](leveling-enhancement.md) |

Classic Era community-standard builds (Horde only in Classic; Forever adds Dwarf shamans). Shamans raid as Restoration healers; Elemental becomes a real raid DPS spec with Naxxramas-level gear; Enhancement is a totem-support/melee hybrid. Allocations validated against the Classic tree data.

Source of truth: `builds.json` in this folder. Regenerate with `python _reference/data/validate_builds.py && python _reference/data/render_builds.py`.

## Report index

Reports under this folder that no other page links to (generated):

- [optimizer/elemental-dps-raid-dps.md](optimizer/elemental-dps-raid-dps.md): shaman / classic-era / spec elemental-dps / profile raid-dps
- [optimizer/enhancement-dps-leveling-st.md](optimizer/enhancement-dps-leveling-st.md): shaman / classic-era / spec enhancement-dps / profile leveling-st
- [optimizer/enhancement-dps-raid-dps.md](optimizer/enhancement-dps-raid-dps.md): shaman / classic-era / spec enhancement-dps / profile raid-dps
- [optimizer/resto-heal-raid-heal.md](optimizer/resto-heal-raid-heal.md): shaman / classic-era / spec resto-heal / profile raid-heal
- [raidsim/elemental-dps-environments.md](raidsim/elemental-dps-environments.md): DPS by environment — shaman elemental-dps (Classic Era)
- [raidsim/elemental-dps.md](raidsim/elemental-dps.md): Raid sim — shaman elemental-dps (Classic Era)
- [raidsim/enhancement-dps-environments.md](raidsim/enhancement-dps-environments.md): DPS by environment — shaman enhancement-dps (Classic Era)
- [raidsim/enhancement-dps.md](raidsim/enhancement-dps.md): Raid sim — shaman enhancement-dps (Classic Era)
- [respec-plan.md](respec-plan.md): Shaman / classic-era: respec plan for `leveling-st`
