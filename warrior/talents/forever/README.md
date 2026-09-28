# Warrior — adapting the Classic builds to WoW: Forever

Data: WoW: Forever beta client build 1.60.1.70009, merged 2026-09-25 (`talent-trees.md`; the 2026-09-13 demo snapshot is archived under `_reference/data/raw/`). Spellbook numbers: `../../spells/README.md`. Point-by-point audit of every
Classic build: `baseline-audit.md`. Proposed builds: `proposed-builds.json` → `builds-README.md`.

## What broke

| Classic talent | Forever | Impact on baselines |
|---|---|---|
| Tactical Mastery (Arms T2, 5) | **Removed** — base rage retention is presumably baseline; new *Improved Tactical Mastery* (5) in the same slot and still the prerequisite for Anger Management | Every build that dipped Arms for TM/AM keeps the same shape with the new talent |
| Axe/Mace/Sword/Polearm Specialization | **Removed** — replaced by *Weaponmaster* (5, Arms T5): axe/polearm crit, mace armor ignore, sword extra attacks | Arms builds pick Weaponmaster; still unreachable for Bloodthirst builds |
| Improved Battle Shout (Fury T3, 5) | **Removed** | 5 orphaned points in both Fury raid builds; tier 3 now holds Boundless Rage / Piercing Howl / Blood Craze / Improved Cleave |
| Improved Demoralizing Shout | **Removed** | Nothing in the baselines used it |
| Improved Slam | **Moved** Fury T5 → Arms T6, now 2 ranks, and Slam no longer interrupts the swing timer | The 2H Fury/Bloodthirst build cannot reach it; the 2H build becomes an Arms/Mortal Strike build |
| Improved Shield Block, Improved Taunt, One-Handed Weapon Specialization | **Removed** | 7 orphaned points in the tank build; Bastion (+10% damage with shield) is the new threat multiplier |
| Iron Will | Moved Prot T2 → Fury T2 | PvP alternative to Unbridled Wrath |
| Improved Thunder Clap | Moved Arms T2 → Prot T2 | Dungeon tank option |

## What's new and matters

- **Raging Blows** (Fury 16-pt): Whirlwind hits with the off-hand, cheaper Cleave — a clear pick for dual wield.
- **Precision** (Fury T5, 3): +1% hit per rank. Hit was the scarcest stat for Classic warriors.
- **Bloodthrill** (Arms T5, 5): Overpower procs while Rend is on the target — makes Rend part of an Arms rotation.
- **Spearing Strike** (Arms 16-pt): bonus damage vs. Giants/Dragonkin (many raid bosses) and dismounts — check the numbers.
- **Bastion / Master of Defense / Vanguard / Focused Rage** (Protection): more threat, rage on avoidance, Charge in Defensive Stance; Vitality was cut in beta build 69893.
- **Boundless Rage** (Fury T3): +max rage; a sensible filler where Improved Battle Shout used to be.

## Decisions made in the proposed builds

1. **Fury DW 17/34/0** keeps the Classic skeleton; the freed 5 points go to tier-3 fillers (needed for gating), Raging Blows and 1 point of Precision.
2. **2H raid** is now **Arms 34/17/0** (Mortal Strike + Weaponmaster + Bloodthrill + Improved Slam) instead of 2H Fury.
3. **Prot tank** drops the Classic Arms dip (Vanguard removes the stance-dance reason) and goes **5/5/41** for Bastion, Focused Rage and Improved Revenge (Vitality's 5 points); the 11/5/35 shape with Improved Tactical Mastery + Anger Management is listed as the alternative.
4. **PvP Arms** takes Weaponmaster over Improved Overpower/Bloodthrill.

## To verify at launch

- Confirmed by the beta client: Flurry 5-25%, Unbridled Wrath 12-60%, Dual Wield Specialization 5-25% damage / 2-10% hit, Enrage a flat 30% chance for 2-10% damage, Weaponmaster 1-5%, Bastion 2-10%.
- Tactical Mastery is a baseline passive learned at 14 (10 Rage retained).
- Shield Block blocks 2 attacks for 7s on a 5s cooldown (beta spellbook).
- Slam has an 18s cooldown in the beta (Improved Slam -1.5/3s), so Slam-weaving is gone; the model now rates Arms 38/13/0 above Fury for a two-hander on Bloodthrill and Mortal Strike instead.
