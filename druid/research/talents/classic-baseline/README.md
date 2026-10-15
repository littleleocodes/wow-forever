# Druid — Classic baseline talent builds

The community-standard WoW Classic Era builds, used as the *starting point* for WoW: Forever. Every allocation below is machine-validated against the Classic tree data (51 points, tier gating, prerequisites, rank caps). Each build page ends with a talent-by-talent check of what survived into the Forever trees.

| Build | Split | Role | Content | Status | File |
|---|---|---|---|---|---|
| Restoration — Swiftmend Healer (5/0/46) | 5/0/46 | HEALER | Raid | Primary | [resto-swiftmend-healer.md](resto-swiftmend-healer.md) |
| Restoration — Regrowth / Nature's Grace (21/0/30) | 21/0/30 | HEALER | Raid | Alternative | [resto-regrowth-natures-grace.md](resto-regrowth-natures-grace.md) |
| Feral — Cat DPS / Powershift (14/32/5) | 14/32/5 | DPS | Raid | Alternative | [feral-cat-dps.md](feral-cat-dps.md) |
| Feral — Bear Tank (14/32/5) | 14/32/5 | TANK | Raid | Alternative | [feral-bear-tank.md](feral-bear-tank.md) |
| Balance — Moonkin (raid DPS, 35/0/16) | 35/0/16 | DPS | Raid | Situational | [balance-moonkin-raid.md](balance-moonkin-raid.md) |
| Restoration / Balance — PvP Healer (14/0/37) | 14/0/37 | HEALER | PvP | Primary | [pvp-resto-feral-hybrid.md](pvp-resto-feral-hybrid.md) |
| Leveling — Feral (Cat) | 14/32/5 | DPS | Leveling | Primary | [leveling-feral.md](leveling-feral.md) |

Classic Era community-standard builds. Druids raid as Restoration healers (Swiftmend build early, Nature's Grace/Improved Regrowth build late), Feral is a strong off-tank/dungeon tank and a powershifting cat, Balance is a one-per-raid Moonkin. Allocations validated against the Classic tree data.

Source of truth: `builds.json` in this folder. Regenerate with `python _reference/data/validate_builds.py && python _reference/data/render_builds.py`.

## Report index

Reports under this folder that no other page links to (generated):

- [optimizer/balance-dps-raid-dps.md](optimizer/balance-dps-raid-dps.md): druid / classic-era / spec balance-dps / profile raid-dps
- [optimizer/feral-bear-tank-raid-tank.md](optimizer/feral-bear-tank-raid-tank.md): druid / classic-era / spec feral-bear-tank / profile raid-tank
- [optimizer/feral-cat-dps-leveling-st.md](optimizer/feral-cat-dps-leveling-st.md): druid / classic-era / spec feral-cat-dps / profile leveling-st
- [optimizer/feral-cat-dps-raid-dps.md](optimizer/feral-cat-dps-raid-dps.md): druid / classic-era / spec feral-cat-dps / profile raid-dps
- [optimizer/resto-heal-raid-heal.md](optimizer/resto-heal-raid-heal.md): druid / classic-era / spec resto-heal / profile raid-heal
- [raidsim/balance-dps-environments.md](raidsim/balance-dps-environments.md): DPS by environment — druid balance-dps (Classic Era)
- [raidsim/balance-dps.md](raidsim/balance-dps.md): Raid sim — druid balance-dps (Classic Era)
- [raidsim/feral-cat-dps-environments.md](raidsim/feral-cat-dps-environments.md): DPS by environment — druid feral-cat-dps (Classic Era)
- [raidsim/feral-cat-dps.md](raidsim/feral-cat-dps.md): Raid sim — druid feral-cat-dps (Classic Era)
- [respec-plan.md](respec-plan.md): Druid / classic-era: respec plan for `leveling-st`
