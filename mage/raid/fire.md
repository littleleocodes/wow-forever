# Fire Mage — Raid (group)

[Mage](../README.md) > [Raid (group)](README.md) > Fire

**✅ Recommended** for raid (the best mage spec here, or within 3% of it).

**[Fire — Raid](../research/raid/builds/fire-open-raid.md)** (17/31/3) — [open the talent tree](https://talentsforever.com/mage/60/2032052001002-55500001230123031-003-12)

> 🔬 Derived build: found by this project's open talent search (every legal build, no tree rule, in the community's raid simulator in a full raid, raced against the rotation's builds); it beat the hand-made build (Fire — Ignite / Heating Up), which stays below as the alternative. A model of the beta, to check at launch.

## How to play

**Before the pull:** **Pyroblast**.

**Then press the first one that is ready**, top to bottom:

1. **Pyroblast** when Heating Up has 3 stacks
2. **Fire Blast**
3. **Scorch** when either the target has fewer than 5 stacks of Fire Vulnerability or Fire Vulnerability has under 5 seconds left and the target has fewer than 2 stacks of Fire Vulnerability
4. **Arcane Blast**: keep its buff stacked on you
5. **Arcane Missiles** (rank 7) when Missile Barrage is active
6. **Fireball** (rank 11)

**Fireball** is your filler: cast it whenever nothing above is ready.

**Advanced: your cooldowns and extras.** Once the list above feels easy, add these:

- **Combustion**: a cooldown, use it at the start of the fight and again whenever it is ready (about 1 time a fight)
- Use your trinkets and a potion together with your big cooldowns.

*The simulator's full rotation for this build, with every condition: [research rotation page](../research/raid/rotation.md).*

## Why this rotation

Fire keeps its own **Improved Scorch** debuff at 5 stacks, fires **Fire Blast** every 6 seconds, casts **Pyroblast** whenever three crits have made it a 1.5-second cast, keeps one stack of its **Arcane Blast** buff up, spends **Missile Barrage** procs on free **Arcane Missiles**, and fills with **Fireball** or **Scorch**. The best mage page in the simulator: 869 DPS in a full raid.

**Why it works**

- **Pyroblast** at 3 stacks of **Heating Up** is the first spell on the list (14 casts, 25%; its crits also feed **Ignite**, 10%): crits from **Fireball**, **Fire Blast** and **Scorch** each cut its 6-second cast by 25%, and **Fire Blast** adds a stack on every hit, so three stacks come about every 13 seconds and the cast takes 1.5 seconds. One hard cast before the pull lands as the fight starts.
- **Fire Blast** on cooldown (29 casts, 21%): every 6 seconds with **Improved Fire Blast**, instant, 10% crit from **Incineration** and 6% from **Critical Mass**; its crits start **Ignite** (40% of the hit over 4 seconds) and every hit feeds **Heating Up**.
- **Scorch** keeps Fire Vulnerability at 5 stacks (**Improved Scorch**: 3% more Fire damage per stack for 30 seconds) and refreshes it under 5 seconds left. It is also the short filler (23 casts in all, 11%): when **Fire Blast** will be back before a 3-second **Fireball** could land, the list casts a 1.5-second **Scorch** instead.
- **Fire Power** is why the burns matter: 3% more Fire damage per Fire effect of yours on the target, up to 12%, and Fire Vulnerability, **Ignite**, **Pyroblast**'s burn and **Fireball**'s burn are four. **Fireball** (18 casts, 20%) casts in 3 seconds with all five points of **Accelerant**; the list names rank 11 (rank 12 comes from a tome).
- The 17 Arcane points: one **Arcane Blast** about every 20 seconds (9 casts, 4%) keeps its buff on you (12% of your Intellect as spell damage for 18 seconds) and rolls 40% for **Missile Barrage**, which **Fireball** rolls at 20%; the proc's free, fast **Arcane Missiles** are 9% of the damage (6 casts). **Arcane Concentration** makes one cast in ten free.
- **Combustion** once Fire Vulnerability has 5 stacks (the list holds every cooldown until then; one a fight on its 3-minute cooldown): each Fire hit adds 10% Fire crit until you land 3 crits, which fills **Heating Up** fast.
- Mana: a mana potion whenever it is ready (2 a fight, the list's top line), your mana gem (from **Conjure Mana Ruby**) and a Demonic Rune (about one each), and **Master of Elements**' 20% refund on every Fire crit. The raid list no longer channels **Evocation**: the search dropped that line on 2026-11-10 (+0.4%). Without a raid's mana buffs the simulator's DPS falls 23% from a 3-minute to a 6-minute fight: the mana runs out.

**Caveats**

- Mana without a raid's buffs: the simulator's list for playing alone adds **Evocation** below 10% mana with more than 25 seconds left.
- Several targets: **Flamestrike** (this build has no Blast Wave); **Fire Blast** hits one target only.
- Fire resistance: the simulator's boss resists nothing. Against a target that resists Fire, **Frostbolt** is your fallback and most of this list loses value.
- Threat: this build skips Burning Soul, so only **Arcane Subtlety** lowers your threat, and only for the Arcane spells; the simulator ignores threat.

**When to change it**

- In the last 3 seconds a **Fireball** would land too late: **Scorch** or **Fire Blast**.
- Moving: **Fire Blast** and the 1.5-second **Scorch** keep the stacks and **Heating Up** going; **Pyroblast** and **Fireball** wait.
- The list has no 2-stack **Pyroblast** line (the simulator's own Fire rotation, which this list is built on, dropped it): with 2 stacks and the boss about to die, a **Scorch** and a **Fire Blast** in the same 3 seconds are its choice.

## Talents

| Tree | Points | Talents (ranks) |
|---|---|---|
| Arcane | 17 | Wand Specialization 2, Arcane Subtlety 2, Arcane Concentration 5, Missile Barrage 2, Arcane Blast 1, Arcane Meditation 2, Arcane Resilience 3 |
| Fire | 31 | Incineration 5, Accelerant 5, Ignite 5, Pyroblast 1, Improved Fire Blast 2, Improved Scorch 3, Heating Up 1, Master of Elements 2, Critical Mass 3, Fire Power 3, Combustion 1 |
| Frost | 3 | Precision 3 |

## The numbers

| Setting | DPS |
|---|---|
| Full raid, 3-minute fight (every raid buff and debuff: what this page ranks on) | 887 |

**By gear tier** (the spec's best talents for each tier and setting in its own gear, found by this project's machine-learning search in the community simulator, wowsims/forever 54ceac6 (client 70707); [every spec](../../_reference/dps-rankings.md)):

| Gear | Full raid DPS | Best talents |
|---|---|---|
| Pre-BiS | 885 | this build |
| Phase 1 BiS | 903 | [17/31/3](https://talentsforever.com/mage/60/2032052001002-54500001230133031-003-12) (as good as this build in this gear) |

*Each row is in that tier's own gear set; the DPS at the top of the page is this build in the standard set, so the two do not match.*

**The gear** (average item level: Pre-BiS 62.9; Phase 1 BiS 64.4; each item opens its Wowhead page, with where it drops and its enchant):

| Slot | Pre-BiS | Phase 1 BiS |
|---|---|---|
| Head | [Spellweaver's Turban](https://www.wowhead.com/forever/item=22267) · *General Drakkisath, Blackrock Spire*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) | [Spellweaver's Turban](https://www.wowhead.com/forever/item=22267) · *General Drakkisath, Blackrock Spire*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) |
| Neck | [Nacreous Shell Necklace](https://www.wowhead.com/forever/item=22403) · *Cannon Master Willey, Stratholme* | [Choker of the Fire Lord](https://www.wowhead.com/forever/item=18814) · *Ragnaros, Molten Core* |
| Shoulders | [Mantle of the Timbermaw](https://www.wowhead.com/forever/item=19050) · *Tailoring* | [Mantle of the Timbermaw](https://www.wowhead.com/forever/item=19050) · *Tailoring* |
| Back | [Arcanoweave Cloak](https://www.wowhead.com/forever/item=272411) · *sold by Pix Xizzix* | [Arcanoweave Cloak](https://www.wowhead.com/forever/item=272411) · *sold by Pix Xizzix* |
| Chest | [Robe of the Archmage](https://www.wowhead.com/forever/item=14152) · *Tailoring*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) | [Robe of the Archmage](https://www.wowhead.com/forever/item=14152) · *Tailoring*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) |
| Wrist | [Rockfury Bracers](https://www.wowhead.com/forever/item=21186) · *quest: Stalwart's Battlegear*<br>+ [Enchant Bracer - Greater Intellect](https://www.wowhead.com/forever/spell=13825) | [Rockfury Bracers](https://www.wowhead.com/forever/item=21186) · *quest: Stalwart's Battlegear*<br>+ [Enchant Bracer - Greater Intellect](https://www.wowhead.com/forever/spell=13825) |
| Hands | [Gloves of Spell Mastery](https://www.wowhead.com/forever/item=14146) · *Tailoring* | [Gloves of Spell Mastery](https://www.wowhead.com/forever/item=14146) · *Tailoring* |
| Waist | [Belt of the Archmage](https://www.wowhead.com/forever/item=18405) · *Tailoring* | [Belt of the Archmage](https://www.wowhead.com/forever/item=18405) · *Tailoring* |
| Legs | [Sorcerer's Leggings](https://www.wowhead.com/forever/item=226933) · *sold by Mokvar*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) | [Sorcerer's Leggings](https://www.wowhead.com/forever/item=226933) · *sold by Mokvar*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) |
| Feet | [Fire Striders](https://www.wowhead.com/forever/item=13369) · *Balnazzar, Stratholme*<br>+ [Enchant Boots - Minor Speed](https://www.wowhead.com/forever/spell=13889) | [Fire Striders](https://www.wowhead.com/forever/item=13369) · *Balnazzar, Stratholme*<br>+ [Enchant Boots - Minor Speed](https://www.wowhead.com/forever/spell=13889) |
| Finger | [Warden's Signet of Brilliance](https://www.wowhead.com/forever/item=275982) | [Ring of Spell Power](https://www.wowhead.com/forever/item=19147) · *Lucifron, Molten Core* |
| Finger | [Channeler's Ring](https://www.wowhead.com/forever/item=272406) · *sold by Pix Xizzix* | [Ring of Spell Power](https://www.wowhead.com/forever/item=19147) · *Lucifron, Molten Core* |
| Trinket | [Eye of the Beast](https://www.wowhead.com/forever/item=13968) · *quest: For The Horde!* | [Talisman of Ephemeral Power](https://www.wowhead.com/forever/item=18820) · *Magmadar, Molten Core* |
| Trinket | [Weakness Analyzer](https://www.wowhead.com/forever/item=272438) · *sold by Pix Xizzix* | [Eye of the Beast](https://www.wowhead.com/forever/item=13968) · *quest: For The Horde!* |
| Main hand | [Sageblade](https://www.wowhead.com/forever/item=22383) · *Blacksmithing*<br>+ [Enchant Weapon - Spell Power](https://www.wowhead.com/forever/spell=22747) | [Sageblade](https://www.wowhead.com/forever/item=22383) · *Blacksmithing*<br>+ [Enchant Weapon - Spell Power](https://www.wowhead.com/forever/spell=22747) |
| Off hand | [Obsidian Bauble](https://www.wowhead.com/forever/item=18316) | [Scepter of Interminable Focus](https://www.wowhead.com/forever/item=22329) · *Stratholme* |
| Ranged/relic | [Bonecreeper Stylus](https://www.wowhead.com/forever/item=13938) · *Darkmaster Gandling, Scholomance* | [Bonecreeper Stylus](https://www.wowhead.com/forever/item=13938) · *Darkmaster Gandling, Scholomance* |

**Open in the simulator** (the community's Forever simulator on the web, loaded with the gear, enchants, talents, rotation, consumables and buffs we simulate): Pre-BiS: [full raid](https://wowsims.com/forever/mage/dps/#eJzkV09sG0UX95vd2uOXpPU3/fMtSw7TQEnixMl6HVdJhIhbCQi0yBUnTpC1dx1v2Xgt7wa1t1JyQAgSVCKkpj2gCBRUqa0UJFRH6sVczAEUIZUKOCQCAghVgkQiEkJCaNZOm0PVExUHP8k7M+/p997Mb9688WAnhRgowKEHJqAIZTgH8CbABwAfA7D2wEqEdRjU9YOUxqjqYYT+dRWUjTaU6RvXAWX667z4XlqNYZjWS8oPezFCax+B8t1elGithDLdmAOM0D/udAhYmFaLylwEZTp7J4YyfX81hhJ9dwpl+ulqDCP0t2ug1PejTN+eA5ToltPVF6vbPV/OgradO/XOIrwFZMa+AGQ7twDk52NXILJ0GTaSs/Y6zNjHaTBtyMAKeUzXUrqW1jUtqWl6Ip1Oa5qmJfVU8EslE5qWqhNYJW3fk5/24+NI1TDK9M8L0KUsk4NUYtEF0tQIC5JEkr3KJoyy84pb9rmu6UcTyWRCS47yfNEoTVomdyvcME3L5Lmz3C9avOL6hm+7Je5ZRiVf5D2eZfGCXbESFcM2EzvmRMM8cNpzS71qRN2DUmzGZtcI24ZGGC2RSo4GLt1Cwc7bhsM9e2raMXy30u3xKWPSGjTL3qBRdrxB07LKz9gVa8AoO4FPbvg8PZS3jPzR1DA3TLfsWybvuRveMSa5MW3aPjcKvlUJ4lSsRNkujfI+fWD4CC+4Da1V8itnuz2eszyf56Ztx+R2iRu8MO04XKypvwnwXd43NJBuIG3f447tiaABxuvnSa1f0zResCeLvscDhizT4zo3SiZP9aop7GXdeCh+gAKL1kDsw2ZVEcwgpLCjqw2jW7Brd0TLzrcwYUHW0NtZ9g3cJ0dT/3KOTqPDTuOoOoxqXKES66gBokyvfwKMxIiYCkJ6x7ZyP1u/Gn8AVsf2LkS6BWJRa1kBomtZdqmFN5hjZ1ylwPbVoP0eXQo0CR0Nsc9amJ1xfIo9iX1qL7Z9G6Yo05tVRYFmhkVXglJxs6qozZo+f+vE7iIyf+uE2mzZXAuzeADblkGw94VgT2QW/THLLrcwI4dRiR+iYUavBKXodlalC0T0lhpFaSnb4reOuHXWsooUXwSMPv2amw/myp5Tn8VOpjYO2XJw/FbqL2D0K1l0q5sn9e7mH67q5kl89DwoKNH3Xlb/F99Hw4zkQmoE96A0MnKEPa+OBwc7cHUX3/C8CDvDe0Ee4OsXUoffif66FApkKBPgkVDo+ptEhSp0rpB5ZOGikM/HDhcC+XpMXyeKzMfiN0joPxE/s9N7qPLE1YcWZyT4vvhh5lhTkZkQr42LEAxC62Nxid74//FdjxINhiED43AKXoIilOEMnCH/DABC2j/u); Phase 1 BiS: [full raid](https://wowsims.com/forever/mage/dps/#eJzkV01sG8UX9xu79vilH/5PP/7LksM0UJI4cTLejaskQsStBARa5IoTJ8jau463bLyWd4PaW6lyQEg0KA2Hpj2gCBRUqUEKlzpSL+FihEAVUqmAQyIggBASJBKREFKFZu2kOVQ9UXHwO8zOvKffezO/efNmB9spJEABDl0wBiWowAWAtwDeB/gIgO0NrERaB0FdO0xpgqoexujfN0BZb8MIvTcDGKG/zsr26u0ERmm9rPywH2N05UNQvtuPYbpSxghdnwaM0T9/2ydhUVorKdMxjNDP34OdduoyYJi+O4Ex+vsiKPWDGKG1RanbdDp6EnW768tLILbyZ96Zh7eBTNkzQLbyc0B+PnEdYgvXYD19yV6DKfskDaYNWVgmT2hC10RGEyIthJbKDGSEECKt6SKt60JPp4TQ6wRuk7bvyU8H8UmkahQj9K8Z6FCWyGEaZvE50tRIC5JUmr3OxoyK85pb8bkmtOOpdDol0sO8UDLK45bJ3So3TNMyef4890sWr7q+4dtumXuWUS2UeJdnWbxoV61U1bDN1LY51TD3nfXccrcaU/dgODFls0XCtqARRqT09HDg0i0W7YJtONyzJyYdw3ernR6fMMatfrPi9RsVx+s3LavynF21+oyKE/jkhs8zAwXLKBzXB7lhuhXfMnnXTnjHGOfGpGn73Cj6VjWIU7VSFbs8zHu0vsFjvOg2tFbZr57v9Hje8nyen7Qdk9tlbvDipONwuabeJsB3ec9AX6aBtH2PO7YngwYYr5enRa8Qghft8ZLv8YAhy/S4xo2yyfVuVcdu1olHkocosPgKyH3YqCmSGQQd93W0YXwTdu2O/LKLLUxYkDX0bo59Aw/IUf1fztFJdNhZHFYHUU0qNMz2rQBihH78CTCSIHIqCJlt2/KDbL1q8iFYDfd2INJNkItazUkQXc2xqy28wRzbkyoFdmAF9t6nS4EmocMh9mkLszOKz7CnsUftxrZvoxQj9FZNUaCZYfHloFTcqilqs6bP3jm1u4jM3jmlNr9suoVZPIRtSyDZ+0KyJzOL/phj11qYkaOoJI/QKKPXg1J0N6fSOSJ7C42itJBr8VtH3jqrOSWcnAeMP/uGWwjmyl5Qn8d2pjYO2VJw/JbrL2H8q4js1jZOa53NH67axml8/CIoGKaXX1X/lzxAo4zkQ2oM92B4aOgYe1EdDQ524GoH3/A8D9vD+0Ee4usXUoc/iPZmOBTIQDbAI6HQcY/EpSp0oZh9bO6KlM9GjhYD+XpEWyNKhI8kb5LQfyJ+drv3SOWpG48szlDQvvxB9kRTkR2Tr40rEAxCayPJML35/5O7HiUCBiELo3AGXoESVOAcnCP/DAB+JT/c).

## Other builds of this spec

- [Fire — Ignite / Heating Up](../research/raid/builds/fire-raid.md) (16/32/3, 850 DPS in a full raid) — [open the talent tree](https://talentsforever.com/mage/60/0502152000001-35500201230133031-003-12)
- [Fire (optimized)](../research/raid/builds/opt-fire-raid-raid-dps.md) (18/31/2, 843 DPS in a full raid) — [open the talent tree](https://talentsforever.com/mage/60/0502152000003-35500101230133031-002-12)

---
*Generated by `_reference/data/render_modes.py` on 2026-11-17 from this project's builds and simulations of the WoW: Forever beta (talent and spell data: client build 1.60.1.70753; raid numbers: the official wowsims/forever simulator at 2e6e77d (client 1.60.1.70938)). Simulations, not in-game measurements. Do not hand-edit.*

