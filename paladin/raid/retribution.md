# Retribution Paladin — Raid (group)

[Paladin](../README.md) > [Raid (group)](README.md) > Retribution

**✅ Recommended** for raid (the best paladin spec here, or within 3% of it).

**[Retribution — Raid](../research/raid/builds/retribution-open-raid.md)** (16/4/31) — [open the talent tree](https://talentsforever.com/paladin/60/0502510021-4-35233001001301351-7)

> 🔬 Derived build: found by this project's open talent search (every legal build, no tree rule, in the community's raid simulator in a full raid, raced against the rotation's builds). A model of the beta, to check at launch.

## How to play

**Keep up all fight:** **Seal of Command**, **Seal of Righteousness**.

**Talents with no line below:** **Repentance**: taken because Unsealed Wrath requires it.

**Then press the first one that is ready**, top to bottom:

1. **Judgement**
2. **Hammer of Wrath** when the target is below 20% health
3. **Consecration**
4. **Holy Strike**

Between these, your white swings do the rest.

**Advanced: your cooldowns and extras.** Once the list above feels easy, add these:

- **Seal of the Crusader**: a cooldown, use it at the start of the fight and again whenever it is ready (about 1 time a fight)
- **Retribution Aura**: a cooldown, use it at the start of the fight and again whenever it is ready (about 1 time a fight)
- Use your trinkets and a potion together with your big cooldowns.

*The simulator's full rotation for this build, with every condition: [research rotation page](../research/raid/rotation.md).*

## Why this rotation

Retribution in a raid twists seals: you swap between **Seal of Righteousness** and **Seal of Command** around every swing so each hit carries both, judge **Seal of Righteousness** on cooldown, and give the remaining global cooldowns to **Consecration**, **Holy Strike** and, under 20% health, **Hammer of Wrath**.

**Why it works**

- Only one seal can be active, so keeping up two seals means a twist: with **Twist of Light**, replacing a seal leaves an Echo of it that your next melee swing applies. The full rotation casts **Seal of Righteousness** in the last 0.4 seconds before each swing and **Seal of Command** after the swing, in any global cooldown that **Hammer of Wrath**, **Consecration** and **Holy Strike** do not need: about 14 and 12 times a minute. Opening with **Seal of Command** means your very first swing already carries both.
- Press **Judgement** every time it is ready while **Seal of Righteousness** is up, whether or not the short list shows it. It is off the global cooldown, comes back every 8 seconds with **Improved Judgement**, no longer uses up your seal in Forever, and **Sanctified Judgement** returns 60% of the seal's mana cost; in the simulator the judgement of **Seal of Righteousness** is about an eighth of your damage. If it comes off cooldown while **Seal of Command** is up, judge anyway.
- **Hammer of Wrath** goes first once the boss is below 20% health: with 2 points in **Instrument of Law** it is instant, it comes back every 6 seconds, and at about 500 Holy damage plus a share of your spell damage it is your biggest single hit.
- **Consecration** comes before **Holy Strike** while you have at least a quarter of your mana: on a single boss it deals 312 Holy damage over 8 seconds plus a share of your spell damage, about a sixth of your damage in the simulator, and **Holy Conduit** makes it 40% cheaper.
- **Holy Strike** sits last but is not a real filler: it has a 10-second cooldown, so press it whenever it is ready (20 mana, and **Sacred Arbiter** adds 20% to it). The global cooldowns between your other buttons go to the seal swaps.
- **Seal of Command** is always rank 4: every rank adds the same 70% of weapon damage, rank 4 costs 30 mana less, and the simulator measured it 0.3% better than rank 5. When mana runs low the full rotation steps down: **Seal of Righteousness** rank 7 below half mana, **Seal of Command** rank 2 below 30%, a rank 1 **Consecration** below a quarter, and no seal swaps at all below 15%.

**Caveats**

- The twist rests on the simulator's reading of **Twist of Light**: every Echo you have up fires on the next swing, so a swing after both swaps applies **Seal of Righteousness** twice (the seal and its Echo) and **Seal of Command**'s chance once. If the game allows only one Echo per swing, one swap per swing, alternating the two seals, does the same work with half the global cooldowns: check it at launch.
- All those swaps cost mana, even 20% cheaper with **Twist of Light**. The full-raid numbers assume the raid's **Blessing of Wisdom**, Mana Spring and other paladins' judgements of **Seal of Wisdom** and **Seal of the Crusader** on the boss; with only your own buffs the simulator keeps **Seal of Righteousness** up and twists on every swing only while your mana is above about two thirds.
- Forever weakens ranks far below your level, and the simulator applies an assumed formula (TBC's) since 2026-10-09. **Seal of Command** rank 4 and **Seal of Righteousness** rank 7 are close enough to 60 to lose nothing, but rank 1 **Consecration** keeps only a bit over half of its spell damage bonus, so it is a low-mana stopgap only; the game may also lower a low rank's chance to trigger effects, which no simulator models.
- Several targets: only **Consecration** spreads (its bonus damage hits the first four enemies in it); your seals, judgements and **Holy Strike** stay on one target.
- The full rotation also has a **Holy Shock** line (after **Holy Strike**) for builds that take it, worth several percent there in the simulator; this build has no **Holy Shock**, so skip it.

**When to change it**

- If you cannot time your swings (no swing timer, high latency), skip the swaps: keep **Seal of Righteousness** up, judge it on cooldown and press **Consecration** and **Holy Strike**. How much that costs on the current beta build was not measured.
- Against an Undead or Demon boss, add **Exorcism** on cooldown (15 seconds, 40% cheaper with **Holy Conduit**): it hits harder than **Holy Strike**. The simulator's target is an Elemental, so where it fits best was not measured.
- When you have to leave melee range, keep pressing **Judgement** (10 yards) and, under 20%, **Hammer of Wrath** (30 yards); your seals only work on swings.

*This guide was written for the rotation of 2026-10-15; the list above was re-tuned since, so follow the list where the two differ.*

## The numbers

| Setting | DPS |
|---|---|
| Full raid, 3-minute fight (every raid buff and debuff: what this page ranks on) | 876 |

> Note: Retribution's equal-tier set (raidsim/gear_opt.py, 2026-09-30) is caster gear: the simulator's stat weights value spell damage more than Strength for this spec, and the set leans on Forever launch items (Leafre's Ring of Precise Spell Power, +100 spell damage). In a full raid it also gains from both the physical and the spell buffs, and in Forever Curse of the Elements covers Holy (beta tooltip: 'Magic damage taken'). Check the launch items' availability before trusting the full-raid number.

**By gear tier** (the spec's best talents for each tier and setting in its own gear, found by this project's machine-learning search in the community simulator, wowsims/forever d97252f (client 70755); [every spec](../../_reference/dps-rankings.md)):

| Gear | Full raid DPS | Best talents |
|---|---|---|
| Pre-BiS | 983 | [17/3/31](https://talentsforever.com/paladin/60/0501511022-3-35230101201301351-7) |
| Phase 1 BiS | 990 | [17/3/31](https://talentsforever.com/paladin/60/0502510022-3-35233001001301351-7) (ties this build) |

**The gear** (average item level: Pre-BiS 68.9; Phase 1 BiS 68.8; each item opens its Wowhead page, with where it drops and its enchant):

| Slot | Pre-BiS | Phase 1 BiS |
|---|---|---|
| Head | [Lionheart Helm](https://www.wowhead.com/forever/item=12640) · *Blacksmithing*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11645) | [Avenger's Crown](https://www.wowhead.com/forever/item=21387) · *quest: Avenger's Crown*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11645) |
| Neck | [Beads of Ogre Might](https://www.wowhead.com/forever/item=22150) · *quest: Falrin's Vendetta* | [Onyxia Tooth Pendant](https://www.wowhead.com/forever/item=18404) · *quest: For All To See* |
| Shoulders | [Hermit's Pauldron](https://www.wowhead.com/forever/item=275737) | [Avenger's Pauldrons](https://www.wowhead.com/forever/item=21391) · *quest: Avenger's Pauldrons* |
| Back | [Earthweave Cloak](https://www.wowhead.com/forever/item=21187) · *quest: Volunteer's Battlegear*<br>+ [Enchant Cloak - Lesser Agility](https://www.wowhead.com/forever/spell=13364) | [Earthweave Cloak](https://www.wowhead.com/forever/item=21187) · *quest: Volunteer's Battlegear*<br>+ [Enchant Cloak - Lesser Agility](https://www.wowhead.com/forever/spell=13364) |
| Chest | [Darkmantle Tunic](https://www.wowhead.com/forever/item=22009) · *quest: Saving the Best for Last*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) | [Darkmantle Tunic](https://www.wowhead.com/forever/item=22009) · *quest: Saving the Best for Last*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) |
| Wrist | [Rockfury Bracers](https://www.wowhead.com/forever/item=21186) · *quest: Stalwart's Battlegear*<br>+ [Enchant Bracer - Superior Strength](https://www.wowhead.com/forever/spell=19984) | [Rockfury Bracers](https://www.wowhead.com/forever/item=21186) · *quest: Stalwart's Battlegear*<br>+ [Enchant Bracer - Superior Strength](https://www.wowhead.com/forever/spell=19984) |
| Hands | [Storm Gauntlets](https://www.wowhead.com/forever/item=12632) · *Leatherworking*<br>+ [Enchant Gloves - Strength](https://www.wowhead.com/forever/item=273529) | [Storm Gauntlets](https://www.wowhead.com/forever/item=12632) · *Leatherworking*<br>+ [Enchant Gloves - Strength](https://www.wowhead.com/forever/item=273529) |
| Waist | [Belt of Preserved Heads](https://www.wowhead.com/forever/item=20216) · *quest: A Collection of Heads* | [Belt of Preserved Heads](https://www.wowhead.com/forever/item=20216) · *quest: A Collection of Heads* |
| Legs | [Titanic Leggings](https://www.wowhead.com/forever/item=22385) · *Blacksmithing*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11645) | [Avenger's Legguards](https://www.wowhead.com/forever/item=21390) · *quest: Avenger's Legguards*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11645) |
| Feet | [Sorcerer's Boots](https://www.wowhead.com/forever/item=22064) · *quest: Anthion's Parting Words*<br>+ [Enchant Boots - Greater Agility](https://www.wowhead.com/forever/item=16245) | [Sorcerer's Boots](https://www.wowhead.com/forever/item=22064) · *quest: Anthion's Parting Words*<br>+ [Enchant Boots - Greater Agility](https://www.wowhead.com/forever/item=16245) |
| Finger | [Don Julio's Band](https://www.wowhead.com/forever/item=19325) · *sold by Gaelden Hammersmith* | [Ring of the Fallen God](https://www.wowhead.com/forever/item=21709) · *quest: The Savior of Kalimdor* |
| Finger | [Signet Ring of the Bronze Dragonflight](https://www.wowhead.com/forever/item=21205) · *quest: The Qiraji Conqueror* | [Band of Earthen Might](https://www.wowhead.com/forever/item=21182) · *quest: Veteran's Battlegear* |
| Trinket | [Adaptive Combat Assistant](https://www.wowhead.com/forever/item=272437) · *sold by Pix Xizzix* | [Adaptive Combat Assistant](https://www.wowhead.com/forever/item=272437) · *sold by Pix Xizzix* |
| Trinket | [Jewel of the Guard Captain](https://www.wowhead.com/forever/item=270225) | [Talisman of Ascendance](https://www.wowhead.com/forever/item=22678) · *quest: Epic Armaments of Battle - Friend of the Dawn* |
| Main hand | [Grand Marshal's Sunderer](https://www.wowhead.com/forever/item=18830) · *sold by Lieutenant Jackspring*<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) | [Grand Marshal's Sunderer](https://www.wowhead.com/forever/item=18830) · *sold by Lieutenant Jackspring*<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) |
| Ranged/relic | [Libram of Law](https://www.wowhead.com/forever/item=272435) · *sold by Pix Xizzix* | [Libram of Law](https://www.wowhead.com/forever/item=272435) · *sold by Pix Xizzix* |

**Open in the simulator** (the community's Forever simulator on the web, loaded with the gear, enchants, talents, rotation, consumables and buffs we simulate): Pre-BiS: [full raid](https://wowsims.com/forever/paladin/retribution/#eJzEV2tsFNcV3jM7O3t91uvHxY/xxeDpFoO97bozs92KuoAXm7Y8anVr1EKlqmXsHXuXrnfcmbVl/lRuRelDiCqJlAikQMRDQg4EBIqErKBIRJEIv4iSOAiJxNr8iSKiEP9AyUqJopn1eh/4ERRQ7o/V7LlnzuO79/uOBlsJ1IEIEnTAAUjAGEwB/AfgJYDzALTa2eXs3c3AZpsJX8exSRTI3KCY9SFPjlwE5MnxT+rQS944B+LbAnrJly+D+FENesmNcyDeq0GB3BkUT3mRJ1+8COgln78C9ttecvkCiB/WIE++et4O8945+/fV23XIk2det0Meew7E+zXoQp5cvV0X6Kq7meyY/6v8cDA2ewz+B9zh5LPAPRw8AcIZ7YJ2d/s0eI8mp8/DseQcHE72Eqd8iMIM1yZHZCUiy7ISisjhkBpRw2FZVmRFCctKOKLc5Pgsd68RN+HaLIjYtH0ok5zQMrqkWVZyJK3HJW3c1AIEBeRDqmyhhA3TUI+1OaEaMTaeSkmmlh7RSzw2YEsWmrAhZupj0l5dS0nGsNRnjI5q6XjAix50h8IW/hjbstCKrMxrIDmSyOjGuJXWLStQhV70hJSuiIWd2JqFFmzu06xMsbSD4/ERfVRPZ0pc6QYWwJpANeI88aKng5B7sSzUor/fmNCljCGN6ildpy2sGf05AZHs+5U0Mq6ZcSYgTy6dBCfA+mArESjX7WINOaEea3foKe2Q1K8dNEypb4fV7aK9LIo/ZSq2BJsJUN8JjqDQ4SaXroMdCDnZwsbgGuKmnnkvR9zMwUfuUi226EhT9M/aWOovxlhGUmX1ZyFFDoWVbmkoYSMalwxT0uJxPS4NHpIyCV0yjYyWSRppydI1cyghdVi6Lpl6JhQfs0KFzVB+s+ugZaQ7GTrZPOS1M0B/w3ZjD91a0Tb6Az6sOg0L3eO6nMBQ3G0jK5m6lkpao9KYaWT0ITs6K0BK29kPsTknNCDdmzDGU3HJ1IdN3UpIe42+haTXzsBKbgOOGyFvngS6htVnoQar+4y0pQ+ZTpu0lvmzgEh+OWmYQ0lrVHQH25e7odTHqpziPOR6LLhj2ZtCO9kmXJsTRGzaqVlLODhFCeTdkxAcWvoO0z1sF26lv8C2wLoVQ6GYExpxze8tvTJEEaDgWViJA/RfwP4JOEEzq2dbnxPWYktptrJQqLCfYGuALV8V1gb86MsSuzggL5yC4gEFP+ArGfQA2KeAR4H+F1auqzQi9rM9KxQQCEirtrEY7v9TsTzRs5wXPaPGhK7QPxUeGqeBYl1O8KOv3yZ8XqWo3/Rh1TwpUJ0skt4b8KB7hnfRAmPsy1tjlskInQX2DqBF/7Zyw7Y0lEFpV1qJ7SpHUd6YWmhM/a6N5elW2dgUsL9jmCqrX7LyusL014WHx62rooRgvMhzup/9AffQXY6AeqjnBrcooM4wqA/W2uI86LIJj25Fbq8UMafK01AIbvt1CORWLJiskJg/sn1PNtOi3KqB5TCkTvyMOa6rbUsefolD+wpMKHFreWRC0YUhpDaUTum8VY2oDeWn5EE3QkTdUhwLVKZdDipCxQBTrIK5BCy5S7HUI9xSs4B+BvT+E+d9N9uMvrvCIlWxk25C3xUoGsRgE+Gpb6ZoYvmLhFG27VF6/oh2ov+ugAVnMR9BoL4bQJAnd/4dE4E5OCmrzEj11lJADNCrHL3MOdlXa/URrSgrdRvb8pg6vix2jhqUYpc3lGHnmArY/Y799ltIWwmYztsLYEIBzPeLYIZXA7N3+T26MbiB8LRqusBG1niFo4SjVae9BYut6R9zN+EBp/7D7XJWQ3QGeOTQFfiaq7INrqnhaMuJ4/Z6q+cHw86a7VHnOJGXeoLXONf3sjLRwtNTXRsvPrU8P3d+B85Gty8Yogfsb6zj4PxxzfUE3eRac2/Jp5gMmyEKOyEG+yEBYzAJk9w3AwDqrQOG); Phase 1 BiS: [full raid](https://wowsims.com/forever/paladin/retribution/#eJzEV1tsE1ca9j8ej09+x7kccpkcApn1Eki86+zMeL1is0BMwu5y2Wi9Qbuw0mqXSTyJzTqedMaJ4KVKK3pHILVSK5AKFRdBUyooqBKKSh+oKlGkSlStACHRIrcPfaAqygNq/VBVM47jC7kUFdTzYI3/889/+c75vl+DrQTqQAQJOmAXJGAMJgGeB3gD4DQArXZ2OXt3LbAbzYSv49he9JKXToGY9SFPvjoIyJODpwC95IOTIH4ioJd8/xaIX9agl1w+CeLtGhTIzUHxqBd58t3rtuOB/Ntecu4MiF/UIE8+ftMO8/5J+/fda3XIk1ffcTxfAfFuDbqQJxeu1QW66q4kO2b+L98fjF0/AC8Cty/5MnD3Bw+DcFw7o93aOAXe/cmp03AgeQf2JXuJUz9EYZprkyOyEpFlWQlF5HAoHFHDYVlWZFkJy0o4olzh+Cx3uxHX4PIsiNi0cSiTnNAyuqRZVnIkrcclbdzUAgQF5EOqbKGEDVNQj7U5oRoxNp5KSaaWHtFLPFZhSxaasCFm6mPSdl1LScaw1GeMjmrpeMCLHnSHwhb+Ftuy0IqszGsgOZLI6Ma4ldYtK1CFXvSElK6IhZ3YmoUWbO7TrEyxtN3j8RF9VE9nSlzpKhbAmkA14gzxoqeDkNuxLNSiv9+Y0KWMIY3qKV2nLawZ/TkBkez4izQyrplxJiBPzh4BJ8DKYCsRKNftYg05oR5rN+kpba/Ur+02TKlvk9Xtor0sir9nKrYEmwlQ32GOoNDhJmcvgR0IOdnCxuAy4qaeGS9H3MzBR+5SLTbnSFP0v9pY6n/GWEZSZfUPIUUOhZVuaShhIxqXDFPS4nE9Lg3ulTIJXTKNjJZJGmnJ0jVzKCF1WLoumXomFB+zQoXNUH6za7dlpDsZOtk85L3jQP/GtmIPXV/RNvoDPqw6BrPd44qcwFDcaiMrmbqWSlqj0phpZPQhOzorQErb2a+xOSc0IN2eMMZTccnUh03dSkjbjb7ZpBePw2JuA44bIR8eAbqM1WehBqv7jLSlD5lOm7SW+bOASP68xzCHktao6A62L3RDqY9VOcV5yKVYcNOCN4V2sjW4PCeI2LRZs+ZxcIoSyGdHIDg0/x2m29gWXE//hG2BFYuGQjEnNOKyf1p6ZYgiQMETsBgH6DPAngacoJmls63MCcuxpTRbWShU2O+wNcAWrgprA370ZYldHJDXjkLxgIKf85UMugfsG8D9QF+AxesqjYj9bNsiBQQC0pJtzIU7OBnLEz3LedEzakzoCv1P4aFxCijW5QQ/+vptwudVivpNH1bNkALVyRzpvQEPuqd5Fy0wxr68NWaZjNDrwD4FtOgTizdsS0MZlHalldgucRTljamFxtSf21iebpWNTQJ7EsNUWfqSldcVpn8tPDxsXRUlBONFntOd7F+4jW5xBNRDPZe5OQF1hkF9sNYW50GXTXh0K3J7pYg5VR6DQnDbr0MgV2PBZIXE/JvteLSZ5uRWDSyEIXXiZ8xxXW2b9/BLHNoXYUKJW8sDE4rODiG1oXRK561qRG0oPyUPuhEi6rriWKAy7XJQESoGmGIVzCVgyV2KpT7LzTcL6LdA7z5y3neztei7JcxRFTvpGvSdh6JBDDYRnvqmiyaWv0gYZRsepOdvaCf6bwlYcBbzEQTquwwEeXLzuZgIzMFJWWJGqlfnA2KAXuDoOc7JvlSrD2hFWakb2LqH1PEFsXPUoBS7vKEMO8dUwO4f7O8/QdpKwHTengUTCmDeKIIZXgrM3oX36OrgKsLTqqkCG1njeY4SjlYd8xYstqZ/zV2Be5z6lNvlrIboNPDIoSvwA1dlG1yTw9GWw4fs9VHPr4addb1HvcOJvNQTvMi5fpGViRaeHuta/fZjy/NH53fgRHTjrCG6y/7IOgTOH9ednqCbXGzuLfkWk2EtRGEzxGAnJGAM9sAe7scBAH7JAqg=).

## Other builds of this spec

- [Retribution — Raid](../research/raid/builds/retribution-ml-raid.md) (9/14/28, 697 DPS in a full raid) — [open the talent tree](https://talentsforever.com/paladin/60/05013-053020004-1523330100130033-7)

---
*Generated by `_reference/data/render_modes.py` on 2026-11-04 from this project's builds and simulations of the WoW: Forever beta (talent and spell data: client build 1.60.1.70753; raid numbers: the official wowsims/forever simulator at d97252f (client 1.60.1.70707)). Simulations, not in-game measurements. Do not hand-edit.*

