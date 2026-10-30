# Combat Rogue — Raid (group)

[Rogue](../README.md) > [Raid (group)](README.md) > Combat

**✅ Recommended** for raid (the best rogue spec here, or within 3% of it).

**[Combat — Raid](../research/raid/builds/combat-ml-raid.md)** (16/33/2) — [open the talent tree](https://talentsforever.com/rogue/60/00530310301-30531300001515231-002-7)

> 🔬 Derived build: found by this project's machine-learning search over every legal build of the spec in the community's raid simulator (phase-1 BiS gear, then raced against the spec's builds). A model of the beta, to check at launch.

**Other setups of this spec.** This build is the Daggers setup. The spec's best build for each other setup, in a full raid:

- Swords: [Combat (optimized, swords)](../research/raid/builds/opt-combat-swords-raid-raid-dps.md) (20/31/0, 629 DPS in a full raid) — [open the talent tree](https://talentsforever.com/rogue/60/005323101005-32502300000514231--7)

## How to play

**Keep up all fight:** **Slice and Dice** (put it back up as soon as it drops, even with 1 combo point).

**Then press the first one that is ready**, top to bottom:

1. **Garrote**: keep it on the target
2. **Cold Blood** right before your finisher
3. **Eviscerate** (rank 8) when you have 4 or more combo points and either Slice and Dice is active or you have 79+ energy
4. **Backstab** (rank 8) when Cutthroat is not active
5. **Adrenaline Rush**

Between these, your white swings do the rest.

**Advanced: your cooldowns and extras.** Once the list above feels easy, add these:

- **Blade Flurry**: a cooldown, use it at the start of the fight and again whenever it is ready (about 2 times a fight)
- **Vanish**: a cooldown, use it at the start of the fight and again whenever it is ready (about 1 time a fight)
- Use your trinkets and a potion together with your big cooldowns.

*The simulator's full rotation for this build, with every condition: [research rotation page](../research/raid/rotation.md).*

## Why this rotation

Combat in a raid is an energy rhythm: build combo points with **Backstab**, keep **Slice and Dice** up for its attack speed, and spend everything else on **Eviscerate**. **Adrenaline Rush** and **Blade Flurry** go on cooldown.

**Why it works**

- **Slice and Dice** comes first: 30% more attack speed for the whole fight is worth more than any single hit. Put it back up the moment it drops, even with 1 combo point: it lasts 9 seconds at 1 point and 21 at 5, and **Improved Slice and Dice** makes that 45% longer. Do not refresh it early: while it is up, 4 or more points go into **Eviscerate**, and the simulator found no gain from refreshing it at 5 points before it runs out.
- **Eviscerate** goes at 4 or more combo points, not only at 5: its damage grows by the same amount per point, so the fifth point adds no bonus. A **Backstab** at 4 points often wastes a point, since **Puncturing Wounds** gives it a 45% chance to add a second one, and **Ruthlessness** adds a point after 60% of your finishers, so finishing more often collects more of them. The simulator measured finishing at 4 or more 0.9% better than waiting for 5 with daggers, 0.7% with swords.
- **Cold Blood** spends no combo points. It makes your next attack a sure critical strike, so the rotation times it right before an **Eviscerate** at 4 or more points, your biggest hit.
- **Adrenaline Rush** doubles your energy regeneration for 15 seconds: press it whenever it is ready. The rotation used to hold it for low energy, and pressing it on cooldown measured 1.5% better.
- **Backstab** is your only combo point builder and your filler: everything above it only spends what it builds.

**Caveats**

- **Backstab** needs a dagger in your main hand and you behind the target. If you cannot get behind the boss, or you hold a sword, build with **Sinister Strike** instead (the swords setup on this page plays that way).
- When your energy is nearly full (79 or more) and you hold 4 or more points, **Eviscerate** even if **Slice and Dice** is down so no energy goes to waste, then put **Slice and Dice** back up with the next points.
- **Blade Flurry** copies your hits to a second target for 15 seconds. On a single boss it is still worth pressing on cooldown for its 20% attack speed; with adds, it is your best cleave.

**When to change it**

- In the last 6 seconds of a fight, skip **Slice and Dice** and put every combo point into **Eviscerate**: a buff that outlives the boss does nothing.
- If the boss is about to die and you hold only 1 to 3 points, an **Eviscerate** still beats keeping them.

*This guide was written for the rotation of 2026-10-15; the list above was re-tuned since, so follow the list where the two differ.*

## The numbers

| Setting | DPS |
|---|---|
| Full raid, 3-minute fight (every raid buff and debuff: what this page ranks on) | 683 |

**By gear tier** (the spec's best talents for each tier and setting in its own gear, found by this project's machine-learning search in the community simulator, wowsims/forever 30f67f5 (client 70450); [every spec](../../_reference/dps-rankings.md)):

| Gear | Full raid DPS | Best talents |
|---|---|---|
| Pre-BiS | 685 | [16/33/2](https://talentsforever.com/rogue/60/005303103001-30531300001515231-002-7) |
| Phase 1 BiS | 682 | [17/32/2](https://talentsforever.com/rogue/60/005303103002-30531300001514231-002-7) (ties this build) |

**The gear** (average item level: Pre-BiS 63.7; Phase 1 BiS 63.8; each item opens its Wowhead page, with where it drops and its enchant):

| Slot | Pre-BiS | Phase 1 BiS |
|---|---|---|
| Head | [Darkmantle Cap](https://www.wowhead.com/forever/item=22005)<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11647) | [Darkmantle Cap](https://www.wowhead.com/forever/item=22005)<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11647) |
| Neck | [Beads of Ogre Might](https://www.wowhead.com/forever/item=22150) | [Onyxia Tooth Pendant](https://www.wowhead.com/forever/item=18404) |
| Shoulders | [Theramore Pauldrons](https://www.wowhead.com/forever/item=271955) | [Theramore Pauldrons](https://www.wowhead.com/forever/item=271955) |
| Back | [Howler's Furs](https://www.wowhead.com/forever/item=272414)<br>+ [Enchant Cloak - Lesser Agility](https://www.wowhead.com/forever/spell=13364) | [Howler's Furs](https://www.wowhead.com/forever/item=272414)<br>+ [Enchant Cloak - Lesser Agility](https://www.wowhead.com/forever/spell=13364) |
| Chest | [Dawn Armor](https://www.wowhead.com/forever/item=252483) · *Leatherworking*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) | [Dawn Armor](https://www.wowhead.com/forever/item=252483) · *Leatherworking*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) |
| Wrist | [Forest Stalker's Bracers](https://www.wowhead.com/forever/item=19587)<br>+ [Enchant Bracer - Superior Strength](https://www.wowhead.com/forever/spell=19984) | [Forest Stalker's Bracers](https://www.wowhead.com/forever/item=19587)<br>+ [Enchant Bracer - Superior Strength](https://www.wowhead.com/forever/spell=19984) |
| Hands | [Theramore Gloves](https://www.wowhead.com/forever/item=271948)<br>+ [Enchant Gloves - Agility](https://www.wowhead.com/forever/item=273520) | [Theramore Gloves](https://www.wowhead.com/forever/item=271948)<br>+ [Enchant Gloves - Agility](https://www.wowhead.com/forever/item=273520) |
| Waist | [Assassin's Waistguard](https://www.wowhead.com/forever/item=272395) | [Assassin's Waistguard](https://www.wowhead.com/forever/item=272395) |
| Legs | [Devilsaur Leggings](https://www.wowhead.com/forever/item=15062) · *Leatherworking*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11647) | [Devilsaur Leggings](https://www.wowhead.com/forever/item=15062) · *Leatherworking*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11647) |
| Feet | [Dunestalker's Boots](https://www.wowhead.com/forever/item=20715)<br>+ [Enchant Boots - Greater Agility](https://www.wowhead.com/forever/item=16245) | [Dunestalker's Boots](https://www.wowhead.com/forever/item=20715)<br>+ [Enchant Boots - Greater Agility](https://www.wowhead.com/forever/item=16245) |
| Finger | [Signet Ring of the Bronze Dragonflight](https://www.wowhead.com/forever/item=21205) | [Signet Ring of the Bronze Dragonflight](https://www.wowhead.com/forever/item=21205) |
| Finger | [Ferocious Watcher's Signet](https://www.wowhead.com/forever/item=275981) | [Quick Strike Ring](https://www.wowhead.com/forever/item=18821) · *Magmadar, Molten Core* |
| Trinket | [Adaptive Combat Assistant](https://www.wowhead.com/forever/item=272437) | [Adaptive Combat Assistant](https://www.wowhead.com/forever/item=272437) |
| Trinket | [Rune of the Guard Captain](https://www.wowhead.com/forever/item=19120) | [Rune of the Guard Captain](https://www.wowhead.com/forever/item=19120) |
| Main hand | [Premier High Warlord's Razor](https://www.wowhead.com/forever/item=272596)<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) | [Premier High Warlord's Razor](https://www.wowhead.com/forever/item=272596)<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) |
| Off hand | [Premier High Warlord's Razor](https://www.wowhead.com/forever/item=272596)<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) | [Heartseeker](https://www.wowhead.com/forever/item=12783) · *Blacksmithing*<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) |
| Ranged/relic | [Premier High Warlord's Recurve](https://www.wowhead.com/forever/item=272594) | [Premier High Warlord's Recurve](https://www.wowhead.com/forever/item=272594) |

**Open in the simulator** (the community's Forever simulator on the web, loaded with the gear, enchants, talents, rotation, consumables and buffs we simulate): Pre-BiS: [full raid](https://wowsims.com/forever/rogue/dps/#eJzEVk1sG0UU9ltv7MkkdVajCrarCl6MhBwrLrPrOM3PIU5EBAIOUXvJjWyyY3tbd9faXYeGUygSIPEjigQoOVT8BAkBEVUEKOLAhUuQckgK5AQiUA4R5FAV6ClCaNcOTX84IafvsPP83jfzvvd5ZjT0OAEFVEDIwBRUoAbzAC8BvAPwIQDrjLJSmB0A7fUUkRRZmweaJH99DOqvHVQmLywDlcm36wpNkksbirqZoEny9Wdd6tUUTZLnF0D9MXTW1xX1pxSVycsbCk2QrXo4O0l+fxca4e8/CJd5dVehMvl8I/xefjOs892mou6mbjoyubKppE8oa3Zmp8r3hie2XoPJP6feAGlveBHI++Yn5g+jb53+CKRX7MuwPb4Ku+/BWOfNLovwpZTmvJDneZ3nOddzeV7I63nOOdcLesHI6znOjTVJ/kV6sZNdAHbGrFWfdmsBGtzoz+k8Z/QN4UzFdMrCQtdD07KEhdNzGFQEem5gBrbroC9Mb6aCGV8InHHPTZtBzjLLZeH5Oc+0rdw+MNcAnjjju06PdpR2pNtp0mijcbI4qTUGtn24JDxqszId04pUyaaIzKRnY1qCylTSC7SXZWn7FTlBZbJ0/anbAUaBdqwAaSRVoN3agxEkzuIXIBa2QyF/CySMKXvD7O3bW+SDOWOgZS32UGQPRNQSB6j1UboCSdqWkciNvpAZ+dlhXx0uswn6GBu/CzNde+QguybiX+VPDtKu7BESZ9ITzSn94UCWJtmyxHZgf9vo/VgzywLNumUHOKafHIpIC9OrzqEnSp7wK5gpRFK6WHNtJ/B7se5YwsM8+lgVpaAHPXHOnRVWY+74rO3PCM8MBFZtR/hoTruzAgPzrMCg4vqiuQyWbM8PetF30Q7QEbPCC0PCwozBeznnWLLLlbCcL4SFei+GkDmcrttVC91SVEw4gTc3hLYlnMCeMav46MRpfMYOKm49QDvo0Yq0wPJ36KfTVLrzFv1CtRIH1drPsE8P97SN0gHWT7vSR/bPxR+XjqtAH8p2k7boZB1bke4jwMj1ePiH3ujTmt7Fxv1wcZLV7yTMB1tGOBmV/eIsU7TUQUmHYuzUf2zfwv/YvrN3aU5vWXMkvMjItatPsnYt2dRXje9Ia3BNMp6LxyI7WvwNZCrRWPpvqT0MxOZLxWOLC6F9M9JdimxrxNiWVBlHsqtS7J5YUNz3WmoPL7eszmD0PbVUHG0GilPh62QBoh+x7ZFsnKzeP3bgEcNhAIrwOEzAJFSgBufhvPTPAKhYCfA=); Phase 1 BiS: [full raid](https://wowsims.com/forever/rogue/dps/#eJzEVk1sG0UU9ltv7MkkdVajCrarCl6MhBwrLrPrOM3PIU5EBAIOUXvJjWy8Y3tbd9faXYeGC6UIgQQqKghQcqj4CRICKqoIUMSBC5cg5ZAUyAlEoD1EUImqQE8RQrt2IP3hhBzeYWb2vW/mfe/bmdHQwwQUUAEhAzNQhTqcAXgR4C2A9wFYdxSVwugQaOdSRFJk7RmaJH98COrVLiqTq68AlcnXawpNkgvrirqRoEny5Sc96pUUTZLnFkD9PhysrSnqDykqk5fWFZogm41wdpL88jY03d++Fy7z/Gth++m6QmVy6XWgSfLNhqJeS9EE+bUU9jK5vKGkjyirdma7xndGpzbPwfTvM6+CtDO6CORd8yPzu/E3jn8A0sv2JdiaXIFr78BE9z81FuFzKc15Ic/zOs9zbuTyvJDX85xzrhf0ASOv5zg3ViX5J+mFbnYW2AmzXnvSrQdocGMwp/OcMTCCparpVISFroemZQkLZ+cxqAr03MAMbNdBX5heqYoZXwgsuadmzSBnmZWK8PycZ9pWbheYawKPnPBdp087SLvSnTRpdNA4WZzWmh3b2l8SHrVZhU5oRapkU0Rm0tMxLUFlKukF2s+ytPOynKAyWbrxxO0Ao0C7loE0gyrQXu3+CBJn8bMQC8uhkL8FEvqUnVH25u0l8uGcMdS2Evsosvsiaok91AYoXYYk7chI5OZAyIz86LAv9pfZFH2ETd6Fma49tJddC/G38keHaU/2AIkz6bHWlMGwI0vT7KLEtmF32+iDWDcrAs2GZQc4oR8diUgL06vNoyfKnvCrmClEUrpYd20n8Pux4VjCwzz6WBPloA89ccqdE1Zz7uSc7ZeEZwYCa7YjfDRn3TmBgXlSYFB1fdFaBsu25wf96LtoB+iIOeGFLmFhxuD9nHMs25VqmM4XwkK9H0PIPM427JqFbjlKJpzAmx9B2xJOYJfMGj48dRyfsoOq2wjQDvq0Ii2w/B366TSV7r5Fv1CtxF61diPs4/09beN0iA3SnvSB3XPx24XDKtAHsr2kIzpZh5alewgwciMe/tCbA1prdL55P5yfZo07CfPhthFORmk/O8kULbVX0pEYO/Yv27fwH7bv3F2K09tWHAkvMnL9yuOsU0u29FXj29IqXJeMZ+OxyA4WfwaZSjSW/lPqDB2xM+XiocWF0L4a6y1HtjlmbEmqjGPZFSn2v1hQ3B211R682LY8w1F7bKk43nIUZ8K3yQJEH7GtsWycrNw7secJw2EIivAoTME0VKEOp+G09NcApKoJWA==).

## Other builds of this spec

- [Combat Daggers](../research/raid/builds/combat-daggers-raid.md) (16/33/2, 677 DPS in a full raid) — [open the talent tree](https://talentsforever.com/rogue/60/005323102-30531300001515231-002-7)
- [Combat (optimized, daggers)](../research/raid/builds/opt-combat-daggers-raid-raid-dps.md) (17/32/2, 663 DPS in a full raid) — [open the talent tree](https://talentsforever.com/rogue/60/005323121-30531300000515231-002-7)
- [Combat Swords](../research/raid/builds/combat-swords-raid.md) (19/32/0, 625 DPS in a full raid) — [open the talent tree](https://talentsforever.com/rogue/60/005303125-32403300001515131--7)

---
*Generated by `_reference/data/render_modes.py` on 2026-10-30 from this project's builds and simulations of the WoW: Forever beta (talent and spell data: client build 1.60.1.70425; raid numbers: the official wowsims/forever simulator at 30f67f5 (client 1.60.1.70450)). Simulations, not in-game measurements. Do not hand-edit.*

