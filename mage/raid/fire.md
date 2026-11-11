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
| Full raid, 3-minute fight (every raid buff and debuff: what this page ranks on) | 855 |

**By gear tier** (the spec's best talents for each tier and setting in its own gear, found by this project's machine-learning search in the community simulator, wowsims/forever 54ceac6 (client 70707); [every spec](../../_reference/dps-rankings.md)):

| Gear | Full raid DPS | Best talents |
|---|---|---|
| Pre-BiS | 885 | this build |
| Phase 1 BiS | 903 | [17/31/3](https://talentsforever.com/mage/60/2032052001002-54500001230133031-003-12) (as good as this build in this gear) |

*Each row is in that tier's own gear set; the DPS at the top of the page is this build in the standard set, so the two do not match.*

**The gear** (average item level: Pre-BiS 61.5; Phase 1 BiS 63.2; each item opens its Wowhead page, with where it drops and its enchant):

| Slot | Pre-BiS | Phase 1 BiS |
|---|---|---|
| Head | [Crimson Felt Hat](https://www.wowhead.com/forever/item=18727) · *Magistrate Barthilas, Stratholme*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) | [Crimson Felt Hat](https://www.wowhead.com/forever/item=18727) · *Magistrate Barthilas, Stratholme*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) |
| Neck | [Nacreous Shell Necklace](https://www.wowhead.com/forever/item=22403) · *Cannon Master Willey, Stratholme* | [Choker of the Fire Lord](https://www.wowhead.com/forever/item=18814) · *Ragnaros, Molten Core* |
| Shoulders | [Mantle of the Timbermaw](https://www.wowhead.com/forever/item=19050) · *Tailoring* | [Mantle of the Timbermaw](https://www.wowhead.com/forever/item=19050) · *Tailoring* |
| Back | [Arcanoweave Cloak](https://www.wowhead.com/forever/item=272411) · *sold by Pix Xizzix* | [Arcanoweave Cloak](https://www.wowhead.com/forever/item=272411) · *sold by Pix Xizzix* |
| Chest | [Robe of the Archmage](https://www.wowhead.com/forever/item=14152) · *Tailoring*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) | [Robe of the Archmage](https://www.wowhead.com/forever/item=14152) · *Tailoring*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) |
| Wrist | [Rockfury Bracers](https://www.wowhead.com/forever/item=21186) · *quest: Stalwart's Battlegear*<br>+ [Enchant Bracer - Greater Intellect](https://www.wowhead.com/forever/spell=13825) | [Rockfury Bracers](https://www.wowhead.com/forever/item=21186) · *quest: Stalwart's Battlegear*<br>+ [Enchant Bracer - Greater Intellect](https://www.wowhead.com/forever/spell=13825) |
| Hands | [Gloves of Spell Mastery](https://www.wowhead.com/forever/item=14146) · *Tailoring* | [Gloves of Spell Mastery](https://www.wowhead.com/forever/item=14146) · *Tailoring* |
| Waist | [Belt of the Archmage](https://www.wowhead.com/forever/item=18405) · *Tailoring* | [Belt of the Archmage](https://www.wowhead.com/forever/item=18405) · *Tailoring* |
| Legs | [Skyshroud Leggings](https://www.wowhead.com/forever/item=13170) · *Highlord Omokk, Blackrock Spire*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) | [Flarecore Leggings](https://www.wowhead.com/forever/item=19165) · *Tailoring*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) |
| Feet | [Fire Striders](https://www.wowhead.com/forever/item=13369) · *Balnazzar, Stratholme*<br>+ [Enchant Boots - Minor Speed](https://www.wowhead.com/forever/spell=13889) | [Fire Striders](https://www.wowhead.com/forever/item=13369) · *Balnazzar, Stratholme*<br>+ [Enchant Boots - Minor Speed](https://www.wowhead.com/forever/spell=13889) |
| Finger | [Warden's Signet of Brilliance](https://www.wowhead.com/forever/item=275982) | [Ring of Spell Power](https://www.wowhead.com/forever/item=19147) · *Lucifron, Molten Core* |
| Finger | [Elemental Focus Band](https://www.wowhead.com/forever/item=20682) · *Prince Skaldrenox, Silithus* | [Ring of Spell Power](https://www.wowhead.com/forever/item=19147) · *Lucifron, Molten Core* |
| Trinket | [Eye of the Beast](https://www.wowhead.com/forever/item=13968) · *quest: For The Horde!* | [Talisman of Ephemeral Power](https://www.wowhead.com/forever/item=18820) · *Magmadar, Molten Core* |
| Trinket | [Weakness Analyzer](https://www.wowhead.com/forever/item=272438) · *sold by Pix Xizzix* | [Eye of the Beast](https://www.wowhead.com/forever/item=13968) · *quest: For The Horde!* |
| Main hand | [Sageblade](https://www.wowhead.com/forever/item=22383) · *Blacksmithing*<br>+ [Enchant Weapon - Spell Power](https://www.wowhead.com/forever/spell=22747) | [Sageblade](https://www.wowhead.com/forever/item=22383) · *Blacksmithing*<br>+ [Enchant Weapon - Spell Power](https://www.wowhead.com/forever/spell=22747) |
| Off hand | [Cloud Stone](https://www.wowhead.com/forever/item=17737) · *Landslide, Maraudon* | [Cloud Stone](https://www.wowhead.com/forever/item=17737) · *Landslide, Maraudon* |
| Ranged/relic | [Pyric Caduceus](https://www.wowhead.com/forever/item=11748) · *Pyromancer Loregrain, Blackrock Depths* | [Pyric Caduceus](https://www.wowhead.com/forever/item=11748) · *Pyromancer Loregrain, Blackrock Depths* |

**Open in the simulator** (the community's Forever simulator on the web, loaded with the gear, enchants, talents, rotation, consumables and buffs we simulate): Pre-BiS: [full raid](https://wowsims.com/forever/mage/dps/#eJzkV09sG8UX9htv7fFL2vo3/fNblhymgZLEiZP1Oq6SCBG3EhBokStOSEiQtXcdb9l4rd0Nam+l5IAqkaCQS9MeIAIFVaKVgoTqSL2Yi4sEipBKBRwSQQMIIUFyiMQFoVk7bQ5VT1Qc/CTvzr5P33uz37x568EOCnGQgUM3jEMJKnAe4B2ADwA+AWDtAUoEOgTK2iFK41RxMUqX5kDeaEOJvn0dUKK/zYvr5dU4Rmi9LP+0D6O09jHIP+zDMK2VUaIbs4ARulUUrAitluTZKEp05vc4SvTLDwHD9L1JlOjnq3GM0j+ugVw/gBK9dVEgd1/t7I3Xre6vZ0Ddzp9+dxEuApm25oBs5xeA/HL8KkSXrsBGasZah2nrBA1mDVlYIU9oalpTM5qqplRVS2YyGVVV1ZSWDn7pVFJV03UCq6TtR/LzAXwSqRJBif41B53yMjlEwyy2QJoegSBJptgbbFyv2K87FZ9rqnYsmUol1dQIL5T08oRpcMflumGYBs+f437J5K7j677llLln6m6hxLs90+RFyzWTrm4ZyR042YD7z3hOuUeJKnswHJ+22DXCtqGRRk2mUyNBSKdYtAqWbnPPmpyydd9xuzw+qU+YA0bFG9ArtjdgmGblOcs1+/WKHcTkus8zgwVTLxxLD3HdcCq+afDue+ltfYLrU4blc73om26QxzWTFas8wnu1/qGjvOg0vGbZd891eTxvej7PT1m2wa0y13lxyra5eKe+JsF3eO9gf6bBtHyP25YnkgYcr4+n1D5VVXnRmij5Hg8UMg2Pa1wvGzzdo6Sxh3Xh4cRBCixWA7EOm1VZKIOQxr2dbRjbgl2rI+7sQgsLFlQNvZNj38EDajT9L9foFNrsDI4oQ6gkZBpme2uAKNHrnwEjcSKmgpDZwVYehPUpiYdwNWzvRKRbIF5qLSdIdC3HLrfwAnPsSCgU2P4atN+XS4amoCMh9kULqzOGz7CnsVfpwbbvIxQlerMqy9CssNhK0CpuVmWl2dPnb5/c3UTmb59Umnc228IqHsS2ZRDqfSXUE5VF7+bYlRZW5AjKicM0wujVoBXdySl0gYjRUqMpLeVa/KsjvjprOTmcWASMPfumUwjmyl5QnscOpjQ22XKw/VbqL2HsG0kMq5untK7mH67q5il8/ALIGKbvv6b8L7GfRhjJh5Qo7sHw8PBR9qIyFmzsINQ9fiPyIuw83k/ykFi/kjr8SbS3wqHABrMBHwmFzr9JTLhC54vZxxYuCbs1eqQY2Lej2jqRJT6auEFC/4n52Z3RI7WnPn1keYaD68sfZY83Hdlxcdi4BMFDaH00EaY3/n9i15lEhSHIwhichlegBBU4C2fJPwMAIPw+9Q==); Phase 1 BiS: [full raid](https://wowsims.com/forever/mage/dps/#eJzkV09sG0UX9xu79vglbf1N/3zLksM0UJI4cTLejaskQsStBARa5IoTEhJk7V3HWzZey7tB7a1UOaBKNChND017QBEoqBJFCpc6Ui/h4gqBKqRSAUKJoAHEBdJDJC4VmrWT5lD1RMXB7zA7855+78385s2bHeygkAAFOHTDOJSgAmcB3gf4COBTANYeWIm0DoG6doDSBFU9jNHFWVDW2zBCH8wCRugfc7K9cjuBUVovK7/swRhd+QSUH/dgmK6UMULXZwBj9KdLASxKayVlJoYR+tUl2G6nLwKG6YeTGKN/Xgelvg8j9NZ5qbv3Zmdvom53f3MBxGb+5AcLcB7ItD0LZDM/D+S3o9cgtngV1tMX7DWYto/RYNqQhWXyjCZ0TWQ0IdJCaKnMYEYIIdKaLtK6LvR0Sgi9TuA2afuZ/LoPn0WqRjFC/56FTmWJHKBhFp8nTY20IEml2Tts3Kg4b7sVn2tCO5JKp1MiPcILJaM8YZncrXLDNC2T589wv2Txqusbvu2WuWcZ1UKJd3uWxYt21UpVDdtMbZlTDXP/Kc8t96gxdReGE9M2u07YJjTCiJSeHglcusWiXbANh3v25JRj+G61y+OTxoQ1YFa8AaPieAOmZVVesqtWv1FxAp/c8HlmsGAZhSP6EDdMt+JbJu/eDu8YE9yYMm2fG0XfqgZxqlaqYpdHeK/WP3SYF92G1ir71TNdHs9bns/zU7ZjcrvMDV6cchwu19TXBPgu7x3szzSQtu9xx/Zk0ADj9fG06BNC8KI9UfI9HjBkmR7XuFE2ud6j6tjDuvBgcj8FFl8BuQ8bNUUyg6Dj7s42jN+HHbsjv+xcCxMWZA29m2PfwyNyVP+Xc3QKHXYKR9QhVJMKDbPdK4AYoZ9/AYwkiJwKQmbLtvwoW5+afAxWw/ZORHof5KJWcxJEV3PsSgtvMMeOpEqB7V2B9od0KdAkdCTEvmxhdsbwBfY89qo92PZDlGKE3qwpCjQzLL4clIqbNUVt1vS5O8d3FpG5O8fV5pfNtDCL+7FtCSR7X0v2ZGbRezl2tYUZOYRK8iCNMnotKEV3cyqdJ7K32ChKi7kWv3XkrbOaU8LJBcD4i++6hWCu7BX1ZexgauOQLQXHb7n+Gsa/jchubeOE1tX84aptnMCnz4GCYXrxLfV/yb00ykg+pMZwF4aHhw+zV9Wx4GAHrrbxDc8LsDV8GOQxvn4ndfiLaO+FQ4EMZgM8EgqdD0hcqkJni9mn5i9LuTV6qBjId6PaGlEifDR5g4T+E/GzW70nKs999sTiDAft6x9njzYV2XH52rgMwSC0NpoM0xv/P7bjUSJgCLIwBifhDShBBU7DafLPAMbIPr8=).

## Other builds of this spec

- [Fire — Ignite / Heating Up](../research/raid/builds/fire-raid.md) (16/32/3, 819 DPS in a full raid) — [open the talent tree](https://talentsforever.com/mage/60/0502152000001-35500201230133031-003-12)
- [Fire (optimized)](../research/raid/builds/opt-fire-raid-raid-dps.md) (18/31/2, 812 DPS in a full raid) — [open the talent tree](https://talentsforever.com/mage/60/0502152000003-35500101230133031-002-12)

---
*Generated by `_reference/data/render_modes.py` on 2026-11-11 from this project's builds and simulations of the WoW: Forever beta (talent and spell data: client build 1.60.1.70753; raid numbers: the official wowsims/forever simulator at ff9babb (client 1.60.1.70888)). Simulations, not in-game measurements. Do not hand-edit.*

