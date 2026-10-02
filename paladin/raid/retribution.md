# Retribution Paladin — Raid (training dummy and parse)

[Paladin](../README.md) > [Raid (training dummy and parse)](README.md) > Retribution

**✅ Recommended** for raid (the best paladin spec here, or within 3% of it).

**[Two-handed Retribution](../research/raid/builds/opt-ret-dps-raid-dps.md)** (12/8/31) — [open the talent tree](https://talentsforever.com/paladin/60/25003002-503-05225131001230321-4)

## How to play

**Before the pull:** **Seal of Command**.

**Keep up all fight:** **Seal of Command**.

**Then press the first one that is ready**, top to bottom:

1. **Hammer of Wrath** when the target is below 20% health
2. **Holy Strike**
3. **Consecration**

**Consecration** is your filler: cast it whenever nothing above is ready.

**Advanced: your cooldowns and extras.** Once the list above feels easy, add these:

- **Seal of Righteousness**: part of the rotation (about 16 times a fight)
- Use your trinkets, your racial and a potion together with your big cooldowns.

*The simulator's full rotation for this build, with every condition: [research rotation page](../research/raid/rotation.md).*

## The numbers

| Setting | DPS |
|---|---|
| Training dummy, 3-minute fight (only your own buffs) | 544 |
| Parse (a full raid: every raid buff and debuff) | 1011 |

> Note: Retribution's equal-tier set (raidsim/gear_opt.py, 2026-09-30) is caster gear: the simulator's stat weights value spell damage more than Strength for this spec, and the set leans on Forever launch items (Leafre's Ring of Precise Spell Power, +100 spell damage). In a full raid it also gains from both the physical and the spell buffs, and in Forever Curse of the Elements covers Holy (beta tooltip: 'Magic damage taken'). Check the launch items' availability before trusting the full-raid number.

**By gear tier** (the spec's best talents for each tier and setting in its own gear, found by this project's machine-learning search in the community simulator; [every spec](../../_reference/dps-rankings.md)):

| Gear | Training dummy | Full raid | Best talents (dummy) |
|---|---|---|---|
| Pre-BiS | 520 | 969 | this build |
| Phase 1 BiS | 555 | 1042 | [11/8/32](https://talentsforever.com/paladin/60/25003001-503-05225131001330321-4) |

- **Pre-BiS gear** (average item level 61.8): Head: Black Dragonscale Helm; Neck: Nacreous Shell Necklace; Shoulders: Rugged Mantle of the Timbermaw; Back: Hide of the Wild; Chest: Soulforge Breastplate; Wrist: Rockfury Bracers; Hands: Gloves of Earthen Power; Waist: Knowledge of the Timbermaw; Legs: Ironfeather Leggings; Feet: Sorcerer's Boots; Finger: Leafre's Ring of Precise Spell Power; Finger: Songstone of Ironforge; Trinket: Blackhand's Breadth; Trinket: Rune of the Guard Captain; Main hand: The Unstoppable Force; Ranged/relic: Libram of Law
- **Phase 1 BiS gear** (average item level 66.1): Head: Black Dragonscale Helm; Neck: Choker of the Fire Lord; Shoulders: Rugged Mantle of the Timbermaw; Back: Sapphiron Drape; Chest: Soulforge Breastplate; Wrist: Rockfury Bracers; Hands: Gloves of the Hypnotic Flame; Waist: Knowledge of the Timbermaw; Legs: Ironfeather Leggings; Feet: Sorcerer's Boots; Finger: Leafre's Ring of Precise Spell Power; Finger: Band of Sulfuras; Trinket: Blackhand's Breadth; Trinket: Frozen Heart of the Mountain; Main hand: Bonereaver's Edge; Ranged/relic: Libram of Law

**Where the raid damage comes from** (the same build, adding the raid's buffs one group at a time; percent of the dummy DPS):

Dummy 544 → mana +3% → armor +8% → physical +32% → spell +25% → everything else +19% → raid 1011

(*mana*: Blessing of Wisdom, Mana Spring; *armor*: Sunder Armor, Faerie Fire, Curse of Recklessness; *physical*: Battle Shout, Blessing of Might, Windfury, Leader of the Pack, Trueshot Aura; *spell*: Curse of the Elements, Arcane Brilliance, Moonkin Aura; *everything else*: Kings, stamina, spirit, auras and the raid rotation.)

**DPS by fight length** (training dummy; your average DPS if the fight lasts this long):

| 1 min | 2 min | 3 min | 4 min | 6 min |
|---|---|---|---|---|
| 542 | 520 | 512 | 502 | 479 |

Falling numbers mean cooldowns used at the pull, or mana running out in long fights.

**Parse build** (personal damage in a full raid, where the raid brings the buffs): [Two-handed Retribution](../research/raid/builds/opt-ret-dps-parse.md) (9/8/34) — [open the talent tree](https://talentsforever.com/paladin/60/51003-503-05225331001330321-4).

## Other builds of this spec

- [Retribution — Raid](../research/raid/builds/retribution-ml-raid.md) (11/8/32, 546 DPS on the dummy) — [open the talent tree](https://talentsforever.com/paladin/60/25003001-503-05225131001330321-4)
- [Retribution — Seal of Command / Twist of Light](../research/raid/builds/ret-full-buffs-raid.md) (10/8/33, 536 DPS on the dummy) — [open the talent tree](https://talentsforever.com/paladin/60/52003-503-05225231001330321-4)
- [Retribution — Seal of Command / Twist of Light](../research/raid/builds/ret-raid-dps.md) (17/0/34, 529 DPS on the dummy) — [open the talent tree](https://talentsforever.com/paladin/60/550030030001--05225331001330321-4)

---
*Generated by `_reference/data/render_modes.py` on 2026-10-02 from this project's builds and simulations of the WoW: Forever beta (client build 1.60.1.70009). Simulations, not in-game measurements. Do not hand-edit.*

