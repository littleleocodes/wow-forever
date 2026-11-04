# Smite Priest — Raid (group)

[Priest](../README.md) > [Raid (group)](README.md) > Smite

*Damage from Smite and Holy Fire, carried by Discipline talents.* (a hybrid: Discipline/Holy).

**[Smite — Raid](../research/raid/builds/smite-open-raid.md)** (17/17/17) — [open the talent tree](https://talentsforever.com/priest/60/50203003103-00515121002-502520010002-7)

> 🔬 Derived build: found by this project's open talent search (every legal build, no tree rule, in the community's raid simulator in a full raid, raced against the rotation's builds); it beat the hand-made build (Discipline/Holy — Smite), which stays below as the alternative. A model of the beta, to check at launch.

## How to play

**Before the pull:** **Holy Fire**.

**Then press the first one that is ready**, top to bottom:

1. **Shadow Word: Pain**: keep it on the target, until the last 10 seconds of the fight
2. **Mind Blast**
3. **Inner Focus**, then straight away **Devouring Plague**
4. **Holy Fire**: keep it on the target, when you have at least 40% mana
5. **Inner Focus**, then straight away **Smite**
6. **Shadow Word: Death** (rank 3)
7. **Smite** when you have at least 25% mana
8. **Smite** when you have at least 20% mana

*The simulator's full rotation for this build, with every condition: [research rotation page](../research/raid/rotation.md).*

## Why this rotation

Smite in a raid keeps two burns up, **Shadow Word: Pain** and **Holy Fire**, fires **Penance** whenever it is ready and casts **Smite** in every gap. **Holy Fire** counts for more than its own damage: with **Power in Light** your **Smite** and **Penance** deal 10% more while it burns.

**Why it works**

- **Holy Fire** starts 3 seconds before the pull (a 3-second cast with **Divine Fury**), so it lands as the fight begins. Recast it when its burn has about 1.5 seconds left, roughly every 12 seconds: the new one lands just after the old burn ends, and the simulator measured that 0.5% ahead of starting 3 seconds early.
- **Penance** is on top: three Holy bolts in 2 seconds on a 12-second cooldown, about a quarter of your damage, and the simulator measured 3.1% more damage with it first. The full list casts rank 3 (from the community simulator's rotation): a little less damage than rank 4 for 30% less mana, and high enough that our downranking model leaves it its full spell power.
- **Shadow Word: Pain** is about 30% of this build's damage for one global cooldown every 18 seconds. Recast it when it falls off, but not in the last 10 seconds of the fight.
- **Inner Focus** goes into **Devouring Plague** to make it free (its 3-minute cooldown allows one in a 3-minute fight; the list's second **Inner Focus** line, into **Smite**, only comes up in longer fights); the simulator measured about 1% more damage with that pair. Paid for, the plague costs this build about 890 mana (no **Shadowform** or **Devouring Contagion** to cut it), and the simulator measured 2.0% more damage after dropping the plain **Devouring Plague** line.
- **Shadow Word: Death** and **Power Infusion** go out on cooldown, then **Smite** fills everything else. **Mind Blast** is left out: none of your Holy talents help it and it costs more mana than **Smite**, and the simulator measured about 5% more damage casting **Smite** in its place.

**Caveats**

- This build runs short of mana even in a full raid: the simulator's priest also uses two mana potions and two Demonic Runes a fight. **Meditation** keeps half your regeneration going while you cast, and the cheaper ranks the full list picks (rank 3 **Penance**, rank 3 **Shadow Word: Death**, the latter measured 0.5% better than rank 4) are part of the mana plan; neither is far enough below your level to lose spell power in our downranking model.
- The full list still holds a rank 2 **Smite** for 20-50% mana, measured before 2026-10-09; it now sits under the top-rank **Smite** and never fires. Ranks far below your level get much less from your spell power (a beta change; our model leaves rank 2 a small fraction of it), so do not downrank **Smite**.
- **Shadow Word: Death** hits you for 10% of your maximum health each time the boss survives it, about 10 times a fight: your healers pay for that.
- The full list also holds **Mind Blast**, **Shadowform** and **Mind Flay** lines below the unconditional **Smite**: they never fire for this build.

**When to change it**

- When the boss has under 3 seconds to live, cast **Smite** (2 seconds) rather than a new **Holy Fire** (3 seconds): only a spell that finishes casting does damage.
- If healing is tight, cast **Shadow Word: Death** only in the last 20% of the boss's health, as the simulator's rotation for fighting alone does. You give up a little damage.
- When you must move, use the instants: **Shadow Word: Death**, and **Shadow Word: Pain** if it fell off. **Holy Fire**, **Smite** and **Penance** all need you to stand still.

*This guide was written for the rotation of 2026-10-15; the list above was re-tuned since, so follow the list where the two differ.*

## The numbers

| Setting | DPS |
|---|---|
| Full raid, 3-minute fight (every raid buff and debuff: what this page ranks on) | 602 |

**By gear tier** (the spec's best talents for each tier and setting in its own gear, found by this project's machine-learning search in the community simulator, wowsims/forever bac92db (client 70707); [every spec](../../_reference/dps-rankings.md)):

| Gear | Full raid DPS | Best talents |
|---|---|---|
| Pre-BiS | 679 | [17/17/17](https://talentsforever.com/priest/60/50503000103-20515101002-502521000002-7) |
| Phase 1 BiS | 685 | [17/17/17](https://talentsforever.com/priest/60/50503000103-20515101002-500520012002-7) (ties this build) |

**The gear** (average item level: Pre-BiS 72.4; Phase 1 BiS 70.9; each item opens its Wowhead page, with where it drops and its enchant):

| Slot | Pre-BiS | Phase 1 BiS |
|---|---|---|
| Head | [Tiara of the Oracle](https://www.wowhead.com/forever/item=21348) · *quest: Tiara of the Oracle*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) | [Field Marshal's Headdress](https://www.wowhead.com/forever/item=17602) · *sold by Sergeant Major Clate*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) |
| Neck | [Charm of the Shifting Sands](https://www.wowhead.com/forever/item=21504) · *quest: The Fall of Ossirian* | [Choker of the Fire Lord](https://www.wowhead.com/forever/item=18814) · *Ragnaros, Molten Core* |
| Shoulders | [Field Marshal's Satin Mantle](https://www.wowhead.com/forever/item=17604) · *sold by Sergeant Major Clate* | [Field Marshal's Satin Mantle](https://www.wowhead.com/forever/item=17604) · *sold by Sergeant Major Clate* |
| Back | [Hide of the Wild](https://www.wowhead.com/forever/item=18510) · *Leatherworking* | [Hide of the Wild](https://www.wowhead.com/forever/item=18510) · *Leatherworking* |
| Chest | [Vestments of the Oracle](https://www.wowhead.com/forever/item=21351) · *quest: Vestments of the Oracle*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) | [Vestments of the Oracle](https://www.wowhead.com/forever/item=21351) · *quest: Vestments of the Oracle*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) |
| Wrist | [Rockfury Bracers](https://www.wowhead.com/forever/item=21186) · *quest: Stalwart's Battlegear*<br>+ [Enchant Bracer - Greater Intellect](https://www.wowhead.com/forever/spell=13825) | [Rockfury Bracers](https://www.wowhead.com/forever/item=21186) · *quest: Stalwart's Battlegear*<br>+ [Enchant Bracer - Greater Intellect](https://www.wowhead.com/forever/spell=13825) |
| Hands | [Sandworm Skin Gloves](https://www.wowhead.com/forever/item=20716) · *quest: Armaments of War* | [Sandworm Skin Gloves](https://www.wowhead.com/forever/item=20716) · *quest: Armaments of War* |
| Waist | [Belt of the Archmage](https://www.wowhead.com/forever/item=18405) · *Tailoring* | [Belt of the Archmage](https://www.wowhead.com/forever/item=18405) · *Tailoring* |
| Legs | [Trousers of the Oracle](https://www.wowhead.com/forever/item=21352) · *quest: Trousers of the Oracle*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) | [Flarecore Leggings](https://www.wowhead.com/forever/item=19165) · *Tailoring*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) |
| Feet | [Marshal's Satin Sandals](https://www.wowhead.com/forever/item=17607) · *sold by Sergeant Major Clate*<br>+ [Enchant Boots - Minor Speed](https://www.wowhead.com/forever/spell=13889) | [Marshal's Satin Sandals](https://www.wowhead.com/forever/item=17607) · *sold by Sergeant Major Clate*<br>+ [Enchant Boots - Minor Speed](https://www.wowhead.com/forever/spell=13889) |
| Finger | [Ring of the Fallen God](https://www.wowhead.com/forever/item=21709) · *quest: The Savior of Kalimdor* | [Ring of the Fallen God](https://www.wowhead.com/forever/item=21709) · *quest: The Savior of Kalimdor* |
| Finger | [Signet Ring of the Bronze Dragonflight](https://www.wowhead.com/forever/item=21210) · *quest: The Grand Invoker* | [Ring of Spell Power](https://www.wowhead.com/forever/item=19147) · *Lucifron, Molten Core* |
| Trinket | [Talisman of Ascendance](https://www.wowhead.com/forever/item=22678) · *quest: Epic Armaments of Battle - Friend of the Dawn* | [Talisman of Ascendance](https://www.wowhead.com/forever/item=22678) · *quest: Epic Armaments of Battle - Friend of the Dawn* |
| Trinket | [Zandalarian Hero Charm](https://www.wowhead.com/forever/item=19950) · *quest: The Heart of Hakkar* | [Talisman of Ephemeral Power](https://www.wowhead.com/forever/item=18820) · *Magmadar, Molten Core* |
| Main hand | [Grand Marshal's Mageblade](https://www.wowhead.com/forever/item=23451) · *sold by Lieutenant Jackspring*<br>+ [Enchant Weapon - Spell Power](https://www.wowhead.com/forever/spell=22747) | [Grand Marshal's Mageblade](https://www.wowhead.com/forever/item=23451) · *sold by Lieutenant Jackspring*<br>+ [Enchant Weapon - Spell Power](https://www.wowhead.com/forever/spell=22747) |
| Off hand | [Master Dragonslayer's Orb](https://www.wowhead.com/forever/item=19366) · *quest: The Lord of Blackrock* | [Master Dragonslayer's Orb](https://www.wowhead.com/forever/item=19366) · *quest: The Lord of Blackrock* |
| Ranged/relic | [Brilliant Wand](https://www.wowhead.com/forever/item=249385) · *Enchanting* | [Brilliant Wand](https://www.wowhead.com/forever/item=249385) · *Enchanting* |

**Open in the simulator** (the community's Forever simulator on the web, loaded with the gear, enchants, talents, rotation, consumables and buffs we simulate): Pre-BiS: [full raid](https://wowsims.com/forever/priest/dps/#eJzEVk1sG0UU3je79o6fg2uG0mxXFdqagozRmtlxFiXlYLenqhJQIa3Ejdi1i11a28pawsDFSD1QJNwqh6L+oAKioUVCggOh4pggYSQIOXGAixWIkgNCcEkOSAiN1w7IydEx7/A8nm9H3/e+93Y1eIRCHAywIAmzUIY6tADeAngf4C4Am+ihRKLTYHZjlMZDZhN1+usCGOtR1GjrLqBGv74s88pVQJ1uLIDxSwx1unQHjJ9jqNHfPpDo+hWJbgYHdfrNZTCu6KjR7+9J9Kc7Ml/7XObfb8onb34JRuch1OjCu3Lz3q0DiSfjnUpypQ18q3DmnQ/hbSCXKvNAtgo3gGyc+AT0j2/BZ6falS5cqpykPe2Qg6/IMZe7PMM5d3jGFtx1XIc7nAvb5cIVDpchOgRWSXSNrE3gQYyYOoaSlL73akLHEKp2xmfzwGbz9Qsv1eoNS3DxtM1nbDF93DpbzldfLhWt2pyVLxZLRavwmtUol6y5WiPfqNSqll/Kz50tW0m/VLL8i5VGyS7WfXsA2wGcPu/Xqk+YaXyUHcUHElGMiEBC28N4KkbDjJxWzDBqSBzeV9f22MUxaArMiNBlj70xBrpJ8TDqZghVettHNCmGk2G6eg2YZpLjCrs93AaH22JmxBqeQc7SeDg1SVUWOT+YBakFNZ52fXwwdUC2pKBIb1Cd4o/tTAwzzEPi4L8lDGZp0WPVMdgXOKbS5e3n2Su7reKj5gvq/O451hpHY44MOy/cgfOLHnPMp/AYSwy/P0NHMjvNantjVn26L8HhvlwkCf1BY4/sUdWOxEWPRc1ghHT6hccujKGlVH5n6NW/nt1zgJwRswUD9GdzN5lj88x+kMW3Cuz13ZU5UyMmO4QTCUQqpJvb82D2fw11k3TgDyLeVJVeTOWWQDMJKom/SURuKK1zucM3rsv4Nnv0XC9+zIouMTQrm7pPlP8lGrnBal/j8U/3jWeml1/4KHeiv5Gblbed69D7o3SzKZXenzz5n0sRh2nIwSk4Ay9CGerQhCb5ZwBMjTNB); Phase 1 BiS: [full raid](https://wowsims.com/forever/priest/dps/#eJzEVk1sG0UU3je79o6fg2uG0mxXFdqagozRmtlxFiXlYLenqhJQIa3Ejdi1i11a28pawsAlSDkQJNzKqEUtRQUEgSAhwYEQcUyQMAJCTlwQkhUUhQMHuCQHpAiNfwJycnTcd3gezzej73vfe7YGT1CIggEWxGEailCFWYA3AN4H+BSAjXVQItFJMNsRSqMBs446XZkHYzOMGt1tAmr023mZ164D6nRrAYzfI/LMx2D8GkGN/vmBRDevSfS3G52LOv1uHoxrOmr0p0WJ/nBD5ptfyjz3tjz57tdgtB5AjS68IzcX7xyJPR5tleJrDeDbuQtvfQhvApkrNYFs524D2TrzGeif3IEvzjVKbZgrnaUd7ZCBb8gpl7s8xTl3eMoW3HVchzucC9vl3BWcO4Jz0SKwTsIbZGMMj2LI1DEQp/S9l2M6BlC1Uz5rApvOVq+8UKnWLMHFkzafssXkaetiMVt+sZC3KjNWNp8v5K3cK1atWLBmKrVsrVQpW34hO3OxaMX9QsHyr5ZqBTtf9e0+bHfh5GW/Un7MTOLD7CTeFwtjSHQlNDyMJiI0yMh5xQyihsThPXUNj10dgaauGSG66rHXRkA3Lh5E3QygSu/6iCbFYDxI128C00xyWmF3B9vgcFtMDVnDU8hZEo8nxqnKQpf7syC1oMaTro/3J47IluQU6Q2qE/yRvYlhhnlMHP2vhP4sLXmsPAL7uo6pdHXnWfbSfqv4sPm6df74DJsdRWNODDov3L7zSx5zzCfwFIsN/n4GrqT2mtXwRqz6fE+Cw325iBP6s8YeOqCqPYlLHgub3RHS6VceuzKCllL5P0Ov//P0gQPkDJmtO0B/1/eTOTZPHQZZdDvHXt1fmTMxZLJjOBZDpEK6udMEs/dpqH+QFvxFxOuq0omJzApoJkEltktCckOZvZQ5fvuWjO/TJy914pe0aBNDs9KJZaLck6hl+qtDjUc/PzSeqU5+7qPMmd5GZlq+dm5B54vSTidUujx+9n+PIg6TkIFzcAGehyJUoQ518u8A3+kyvQ==).

## Other builds of this spec

- [Discipline/Holy — Smite](../research/raid/builds/smite-discipline-raid.md) (31/17/3, 582 DPS in a full raid) — [open the talent tree](https://talentsforever.com/priest/60/505235231030001001-30505101002-3-7)

---
*Generated by `_reference/data/render_modes.py` on 2026-11-04 from this project's builds and simulations of the WoW: Forever beta (talent and spell data: client build 1.60.1.70753; raid numbers: the official wowsims/forever simulator at bac92db (client 1.60.1.70707)). Simulations, not in-game measurements. Do not hand-edit.*

