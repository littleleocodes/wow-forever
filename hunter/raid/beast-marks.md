# Beast-Marks Hunter — Raid (group)

[Hunter](../README.md) > [Raid (group)](README.md) > Beast-Marks

*Marksmanship's shots with Beast Mastery's pet talents: the classic raid hunter split.* (a hybrid: Beast Mastery/Marksmanship).

**[Beast-Marks — Raid](../research/raid/builds/beast-marks-open-raid.md)** (27/21/3) — [open the talent tree](https://talentsforever.com/hunter/60/552100050500022-00530503005-3-6)

> 🔬 Derived build: found by this project's open talent search (every legal build, no tree rule, in the community's raid simulator in a full raid, raced against the rotation's builds); it beat the hand-made build (mm-hawk-raid), which stays below as the alternative. A model of the beta, to check at launch.

**Other setups of this spec.** The spec's best build for each other setup, in a full raid:

- With a pet: [Beast Mastery / Marksmanship](../research/raid/builds/bm-mm-raid.md) (22/29/0), 806 DPS in a full raid — [open the talent tree](https://talentsforever.com/hunter/60/53200005041002-005355010150004--6)

## How to play

**Before the pull:** **Aspect of the Hawk**, **Aimed Shot**.

**Keep up all fight:** **Aspect of the Hawk**.

**Then press the first one that is ready**, top to bottom:

1. **Serpent Sting**: keep it on the target, when you have at least 30% mana
2. **Arcane Shot**
3. **Rapid Fire**
4. **Aimed Shot**

Between these, **Auto Shot** keeps firing on its own.

*The simulator's full rotation for this build, with every condition: [research rotation page](../research/raid/rotation.md).*

## Why this rotation

Beast-Marks puts Beast Mastery's pet talents on a Marksmanship shot core and plays the same short list as Beast Mastery: keep **Serpent Sting** up, fire **Arcane Shot** and **Aimed Shot** each time they are ready, and let **Auto Shot** and the pet do the rest.

**Why it works**

- **Serpent Sting** first so it never drops, 20% stronger with **Improved Stings**. Recast it only as it runs out (a new sting replaces the old one), and the full rotation does so only while you have 30% mana or more.
- **Arcane Shot** every time it is ready: 3 points in **Improved Arcane Shot** bring its cooldown to 5.1 seconds, about 34 casts in a 3-minute fight. **Summon Hawk** would share that timer, and in a full raid the simulator measured **Arcane Shot** as the better use of it, so this build skips the hawk.
- **Rapid Fire** (40% faster attacks for 15 seconds, 5-minute cooldown) once a fight, at the pull. The full rotation presses it just before an **Auto Shot** with **Aimed Shot** about to come off cooldown.
- **Aimed Shot** is listed last but goes out almost every time it can: a 2-second cast, then its 6-second cooldown. The simulator measured it slightly better below the instants; **Multi-Shot** shares its cooldown and never comes up on one target.
- The pet half: **Unleashed Fury** (+15% pet damage), **Ferocity** (+10% pet crit on top of your own crit, which Forever pets inherit), **Frenzy** and **Focused Fire** (+2% to you and the pet while it is out). There is no **Bestial Wrath** here, so there is nothing to time but **Rapid Fire**, trinkets and a potion.

**Caveats**

- Mana: the list assumes a full raid with Blessing of Wisdom and Mana Spring. With only your own buffs the simulator drops **Aimed Shot** (310 mana) and keeps **Arcane Shot** going above 10% mana, so **Aimed Shot** goes first when you run low.
- Keep the pet alive with **Mend Pet**: it is about a quarter of your damage and takes no stat buffs from players in Forever. A faster pet does more damage as modelled here (a 1.2-second cat over a 2.0-second pet; measured by players only at levels 20 and 30).
- Track the boss's creature type: **Improved Tracking** (3 points here) counts only against the tracked type.
- Moving: **Auto Shot** and **Aimed Shot** stop while you move; **Arcane Shot** and **Serpent Sting** are instant. The simulator starts **Aimed Shot** 2.5 seconds before the pull; in a real raid, wait for your tank.

**When to change it**

- Two or more targets close together: **Multi-Shot** instead of **Aimed Shot** on their shared cooldown (up to 3 targets for weapon damage each, against 166 extra on one). For a pack, **Volley**: a 6-second channel with no cooldown in Forever.
- In the last few seconds, skip the **Serpent Sting** refresh: its damage comes over 15 seconds.
- Inside 8 yards your shots and **Auto Shot** stop: step back out at once; the pet keeps attacking meanwhile.

## The numbers

| Setting | DPS |
|---|---|
| Full raid, 3-minute fight (every raid buff and debuff: what this page ranks on) | 855 |

**By gear tier** (the spec's best talents for each tier and setting in its own gear, found by this project's machine-learning search in the community simulator; [every spec](../../_reference/dps-rankings.md)):

| Gear | Full raid DPS | Best talents |
|---|---|---|
| Pre-BiS | 845 | [28/23/0](https://talentsforever.com/hunter/60/522020150510023-0053050200503--6) |
| Phase 1 BiS | 876 | [28/23/0](https://talentsforever.com/hunter/60/522010150510123-0053250000503--6) |

*From the search run of 2026-10-01; a new run is queued and will replace these numbers.*

- **Pre-BiS gear** (average item level 62.8): Head: Black Dragonscale Helm; Neck: Mark of Fordring; Shoulders: Theramore Pauldrons; Back: Earthweave Cloak; Chest: Dawn Armor; Wrist: Forest Stalker's Bracers; Hands: Beaststalker's Gloves; Waist: Warpwood Binding; Legs: Outrider's Chain Leggings; Feet: Sorcerer's Boots; Finger: Signet Ring of the Bronze Dragonflight; Finger: Don Julio's Band; Trinket: Blackhand's Breadth; Trinket: Royal Seal of Eldre'Thalas; Main hand: Barbarous Blade; Ranged/relic: Premier High Warlord's Recurve
- **Phase 1 BiS gear** (average item level 65.6): Head: Black Dragonscale Helm; Neck: Onyxia Tooth Pendant; Shoulders: Giantstalker's Epaulets; Back: Earthweave Cloak; Chest: Dawn Armor; Wrist: Giantstalker's Bracers; Hands: Giantstalker's Gloves; Waist: Giantstalker's Belt; Legs: Dragonstalker's Legguards; Feet: Giantstalker's Boots; Finger: Ring of Spell Power; Finger: Ring of Spell Power; Trinket: Blackhand's Breadth; Trinket: Royal Seal of Eldre'Thalas; Main hand: Barbarous Blade; Ranged/relic: Rhok'delar, Longbow of the Ancient Keepers

## Other builds of this spec

- [Beast-Marks — Raid](../research/raid/builds/beast-marks-ml-raid.md) (28/23/0, 833 DPS in a full raid) — [open the talent tree](https://talentsforever.com/hunter/60/532000150510123-0053250000503--6)
- [Marksmanship — Summon Hawk](../research/raid/builds/mm-hawk-raid.md) (22/29/0, 807 DPS in a full raid) — [open the talent tree](https://talentsforever.com/hunter/60/53200005051001-105355000150004--6)
- [Beast Mastery / Marksmanship](../research/raid/builds/bm-mm-raid.md) (22/29/0, 806 DPS in a full raid) — [open the talent tree](https://talentsforever.com/hunter/60/53200005041002-005355010150004--6)

---
*Generated by `_reference/data/render_modes.py` on 2026-10-10 from this project's builds and simulations of the WoW: Forever beta (client build 1.60.1.70291). Simulations, not in-game measurements. Do not hand-edit.*

