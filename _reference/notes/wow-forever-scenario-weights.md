---
name: wow-forever-scenario-weights
description: "2026-09-27 scenario/playstyle overhaul after the user's 'melee hunter takes Improved Wing Clip' complaint: kinds + scenario weights, PvP profile (tuned), calibration fixes (proc-aura APL flags, crit caps, share_build, not_measured), repairs applied to hand drafts with races; what is still open"
metadata:
  node_type: memory
  type: project
  originSessionId: 1178b215-3b7e-4e8a-a51c-7bba704c0381
  modified: 2026-09-27T18:51:22.304Z
---

The user asked on 2026-09-27 that every build be judged by how the class plays in its scenario (PvP, PvE, raids, leveling), after
the melee hunter's leveling draft took Improved Wing Clip.

**Done (in the repo):**
- Model: kinds (scorer/kinds.json) weighted per profile and per spec playstyle; needs_pet; pet_tank; 5-part leveling time split.
- PvP: `pvp` profile tuned by pvp_check.py --grid (burst 0.4, surv 0.5, utility 1.5, mana 0.05; 65% overlap Classic, 57% Forever),
  re-tuned after fixing effects.load_effects: a manual entry holding only PvP effects now keeps its parsed effects elsewhere
  (apply_pvp had created such entries for 4 talents, which silently lost their tooltip values in every mode).
- Raid calibration: proc-aura APL detection in raidsim/run.py (FoF, Hot Streak, Maelstrom, Redoubt), `not_measured` (Murder),
  `share_build` (Frost: FoF build), CHANNEL_MAX crit 0.5 (raid, heal and fight lab calibrations). Frost raid model got an
  ice_lance source; FoF/Hot Streak/WC/Shatter/Redoubt/Murder values reset with derivations. optimize.py `_ensure` breaks synergy cycles.
- Hand drafts repaired (scratchpad/repair.py + apply_repairs.py; leveling ones raced in the fight lab first): leveling-melee <- pet-kept
  optimizer build (no Wing Clip/Monkey/Lone Wolf, ~20% faster at 40-60), melee-survival-raid (no parry talents), survival-melee,
  mm-lone-wolf-raid, balance-moonkin-raid, holy-raid-healer (paladin), ret-raid-dps, enhancement-raid-dps, ds-ruin-raid, three mage
  raid drafts, leveling-beast-mastery, leveling-retribution, leveling-combat-swords (Venom only), pvp-resto, shadow-pvp.

**Rejected / left alone (with reasons):** warlock leveling repair (Wrack is +14% at 40 in the lab; calibration levels 30/60 miss it),
shaman leveling (race tie; enhancement leveling-st scorer values for Elemental Weapons/Spirit Weapons look broken), druid resto Improved
Regrowth (heal-fit crit saturation), Shockadin and Hemo PvP (model cannot express hybrid/burst), Murder kept in rogue raid drafts.

**Open:** heal-lab refit with the crit cap; enhancement leveling-st calibration; warlock calibrate_levels (add 40/50); rogue
Mutilate usable with swords? (tooltip names no dagger); Hemorrhage/Rupture sources; Arms APL, Conflagrate loop, moonkin Wrath weaving,
Champion of the Light heal mechanic, Sniper Shot PvP.

**Why:** the user wants scenario-appropriate builds. **How to apply:** leveling changes must win a fight-lab race; raid changes are
checked in the raid sim; PvP numbers are assumptions.

Related: [[wow-forever-project]], [[wow-forever-fightlab]], [[wow-forever-raidsim]].
