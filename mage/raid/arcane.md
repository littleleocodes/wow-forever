# Arcane Mage — Raid (group)

[Mage](../README.md) > [Raid (group)](README.md) > Arcane

**[Arcane — Raid](../research/raid/builds/arcane-open-raid.md)** (31/17/3) — [open the talent tree](https://talentsforever.com/mage/60/023205203100211531-554000011001-003-12)

> 🔬 Derived build: found by this project's open talent search (every legal build, no tree rule, in the community's raid simulator in a full raid, raced against the rotation's builds); it beat the hand-made build (Arcane — Arcane Blast), which stays below as the alternative. A model of the beta, to check at launch.

## How to play

**Press the first one that is ready**, top to bottom:

1. **Arcane Missiles** (rank 7) when Missile Barrage is active
2. **Arcane Wrath** until the last 10 seconds of the fight
3. **Arcane Blast**: keep its buff stacked on you
4. **Pyroblast** when Heating Up has 3 stacks
5. **Fire Blast**
6. **Arcane Blast** when you have at least 25% mana
7. **Fireball** (rank 11)

**Fireball** is your filler: cast it whenever nothing above is ready.

**Advanced: your cooldowns and extras.** Once the list above feels easy, add these:

- **Presence of Mind**: a cooldown, use it at the start of the fight and again whenever it is ready (about 1 time a fight)
- **Arcane Power**: a cooldown, use it at the start of the fight and again whenever it is ready (about 1 time a fight)
- **Evocation**: when you run out of mana (needed in about 9 of 10 fights)
- Use your trinkets and a potion together with your big cooldowns.

*The simulator's full rotation for this build, with every condition: [research rotation page](../research/raid/rotation.md).*

## Why this rotation

Arcane in a raid keeps its own **Arcane Blast** buff stacked (each cast gives you 12% of your Intellect as spell damage for 18 seconds, up to 4 stacks, at a doubling mana cost), fires **Arcane Wrath** every 6 seconds and **Fire Blast** every 7, spends every **Missile Barrage** proc on a free, fast **Arcane Missiles**, and casts **Pyroblast** once three crits have made it a 1.5-second cast. It is the hungriest mage list: even with a raid's mana buffs the simulator needs **Evocation** in 9 fights of 10. 756 DPS in a full raid.

**Why it works**

- **Arcane Missiles** on **Missile Barrage** first (about 15 casts, 29%): **Arcane Blast** procs it 40% of the time, **Arcane Wrath** 20%; the proc makes the next Missiles free, 2.5 seconds long and twice as dense. **Arcane Impact** adds 6% crit, **Arcane Mind** 10% Intellect and a doubled Arcane crit bonus, **Arcane Instability** 3% damage and crit. The list names rank 7, as the simulator's rotation does; a free cast costs the same at any rank.
- **Arcane Wrath** whenever it is ready (17 casts, 28%): 3 seconds with **Accelerant**, a 6-second cooldown, 406-496 damage plus 5% of your maximum mana as spell damage, and a proc roll. Moving it to the top of the list was the search's biggest single gain (+8.9%). Not in the last 10 seconds.
- **Arcane Blast** (37 casts, 22%): keep its buff stacked on you. Cast it when the buff is gone or about to expire and until it has 3 stacks (the full list's conditions), then only while you have more than 25% mana, because the cost doubles with every stack. 1.5 seconds a cast, 10% crit from **Incineration**, and each one rolls 40% for a **Missile Barrage**.
- **Fire Blast** on cooldown (14 casts, 10%): instant, every 7 seconds with one point of **Improved Fire Blast**, 10% crit from **Incineration**, and every hit adds a **Heating Up** stack.
- **Pyroblast** at 3 stacks of **Heating Up** (4 casts, 7%, plus **Ignite**'s 2%): crits from **Fire Blast** and **Fireball** cut its 6-second cast by 25% each, and **Fire Blast** adds a stack on every hit, so three stacks come about every 45 seconds and the cast takes 1.5 seconds. Never hard-cast it otherwise.
- **Arcane Power** and **Presence of Mind** at the pull: 30% more damage for 15 seconds at 30% more mana, and one instant **Arcane Wrath**; both have 3-minute cooldowns.
- Mana: **Evocation** when nearly dry (0.9 casts a fight in the simulator), a mana potion about every 2 minutes, your mana gem (from **Conjure Mana Ruby**) and a Demonic Rune; **Arcane Concentration** makes one cast in ten free, **Arcane Meditation** at 2 points keeps a third of your regeneration going. When nothing above is affordable, **Fireball** rank 11 fills, about once a fight.

**Caveats**

- A 6-minute fight is a different list: the simulator's DPS falls from 756 at 3 minutes to 412 at 6, because the mana runs out. Longer fights want fewer **Arcane Blast** stacks and an earlier **Evocation**.
- Moving: **Arcane Blast**, **Arcane Wrath** and **Arcane Missiles** all need you to stand. **Fire Blast** is your instant, and **Presence of Mind** makes one cast instant.
- Threat: **Arcane Subtlety** cuts Arcane threat by 30%, but the simulator ignores threat, and **Arcane Power** at the pull is when you are most likely to pull the boss.
- Several targets: **Arcane Explosion** hits everything within 10 yards; **Flamestrike** and **Blizzard** are the rest.

**When to change it**

- In the last 10 seconds no **Arcane Wrath**, in the last 3 no **Arcane Blast**: **Fire Blast**, and a free **Arcane Missiles** if you have one.
- Without a raid's mana buffs the simulator's list for playing alone spends two **Arcane Blast** stacks on a **Frostbolt** instead of a fourth cast and casts **Fire Blast** only on cooldown: cheaper and slower.
- In a fight longer than 3 minutes, use **Arcane Power** and **Presence of Mind** again when they are back, and channel **Evocation** below 15% mana while more than 20 seconds remain.

## Talents

| Tree | Points | Talents (ranks) |
|---|---|---|
| Arcane | 31 | Improved Channeling 2, Arcane Resilience 3, Arcane Subtlety 2, Arcane Concentration 5, Missile Barrage 2, Arcane Impact 3, Arcane Blast 1, Arcane Meditation 2, Arcane Wrath 1, Presence of Mind 1, Arcane Mind 5, Arcane Instability 3, Arcane Power 1 |
| Fire | 17 | Incineration 5, Accelerant 5, Ignite 4, Pyroblast 1, Improved Fire Blast 1, Heating Up 1 |
| Frost | 3 | Precision 3 |

## The numbers

| Setting | DPS |
|---|---|
| Full raid, 3-minute fight (every raid buff and debuff: what this page ranks on) | 773 |

**By gear tier** (the spec's best talents for each tier and setting in its own gear, found by this project's machine-learning search in the community simulator, wowsims/forever ff9babb (client 70888); [every spec](../../_reference/dps-rankings.md)):

| Gear | Full raid DPS | Best talents |
|---|---|---|
| Pre-BiS | 773 | [32/16/3](https://talentsforever.com/mage/60/041205203100311531-553000011001-003-12) |
| Phase 1 BiS | 787 | [32/16/3](https://talentsforever.com/mage/60/041205203100311531-553000011001-003-12) (as good as this build in this gear) |

*Each row is in that tier's own gear set; the DPS at the top of the page is this build in the standard set, so the two do not match.*

**The gear** (average item level: Pre-BiS 62.3; Phase 1 BiS 63.5; each item opens its Wowhead page, with where it drops and its enchant):

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
| Feet | [Kayser's Boots of Precision](https://www.wowhead.com/forever/item=22231) · *War Master Voone, Blackrock Spire*<br>+ [Enchant Boots - Minor Speed](https://www.wowhead.com/forever/spell=13889) | [Kayser's Boots of Precision](https://www.wowhead.com/forever/item=22231) · *War Master Voone, Blackrock Spire*<br>+ [Enchant Boots - Minor Speed](https://www.wowhead.com/forever/spell=13889) |
| Finger | [Elemental Focus Band](https://www.wowhead.com/forever/item=20682) · *Prince Skaldrenox, Silithus* | [Ring of Spell Power](https://www.wowhead.com/forever/item=19147) · *Lucifron, Molten Core* |
| Finger | [Channeler's Ring](https://www.wowhead.com/forever/item=272406) · *sold by Pix Xizzix* | [Ring of Spell Power](https://www.wowhead.com/forever/item=19147) · *Lucifron, Molten Core* |
| Trinket | [Weakness Analyzer](https://www.wowhead.com/forever/item=272438) · *sold by Pix Xizzix* | [Talisman of Ephemeral Power](https://www.wowhead.com/forever/item=18820) · *Magmadar, Molten Core* |
| Trinket | [Eye of the Beast](https://www.wowhead.com/forever/item=13968) · *quest: For The Horde!* | [Eye of the Beast](https://www.wowhead.com/forever/item=13968) · *quest: For The Horde!* |
| Main hand | [Sageblade](https://www.wowhead.com/forever/item=22383) · *Blacksmithing*<br>+ [Enchant Weapon - Spell Power](https://www.wowhead.com/forever/spell=22747) | [Sageblade](https://www.wowhead.com/forever/item=22383) · *Blacksmithing*<br>+ [Enchant Weapon - Spell Power](https://www.wowhead.com/forever/spell=22747) |
| Off hand | [Spellbound Tome](https://www.wowhead.com/forever/item=18695) · *Ras Frostwhisper, Scholomance* | [Cloud Stone](https://www.wowhead.com/forever/item=17737) · *Landslide, Maraudon* |
| Ranged/relic | [Brilliant Wand](https://www.wowhead.com/forever/item=249385) · *Enchanting* | [Brilliant Wand](https://www.wowhead.com/forever/item=249385) · *Enchanting* |

**Open in the simulator** (the community's Forever simulator on the web, loaded with the gear, enchants, talents, rotation, consumables and buffs we simulate): Pre-BiS: [full raid](https://wowsims.com/forever/mage/dps/#eJzElU9ME1kcx/t7M7Svv7LQfUt2Z2f3MMsuC3S35s1MS5BLCxf/HWj04k2mtNgaaJu2B7yhkqgYwTSESOWgRIMa0cSDARIunKqJphcl0QtRCcaLygH1YsyMLRIlxgPU7+G9N++bl/nMd94vP/yTghskUKAJuiAGKRgAOAVwEeAqAKu2XGK6rSCfqabUTeUsOuhUDqRlF4r0xC1Akb4cNccLRTfaaSEhPatBB124AtKTGhToQgJFujwCaKerPeYpB12cBmnEgSK9d8k8OFZ0o0jvFN0o0HN96KCvboJU+AVFejJn+tcmauv/dxfiTQ+Gga+FQ2cnYQjIYDwHZC2cB7LSfh3o1ATcGILh+BIMxjuoBQ5BmCN/c5+qcb/GdZVzXVX9uur1+3XOOVdVzlUv53qBQJG4npIRZKJM2mysTmbovA12FOn9WUmuQoE+72QDwAwj1XsomcoqGtdavCr3ar42pTtmJA5HI0oyrRiRSDSihI8q2VhUSSezRjaeTCiZqJHujilNmWhUMdLdRiLqjaQy3rLv/eTvOJJJJprlP/BnTy21M7LXJjuwCgWVZ2ST5Pi7EMtXBMGP/8nN6HpspyjS+VlJApQ9EhWYc87KZH5Wkp15Yi5HH+6TSzM7vQmcrm413D/fxTJTEZYDuIftwhbZ9y0m/NVTR0XmXFj3qlBA0PCnehc6V+FL9PMVQdexmTVaaFBGe1NG0zeivc+BXJpZ79dkvHWryRwmBF3sZGMVuewqNrIGdHtqSjVnRxGJnilXYbhUhZq/Yf0POT8zbpKIpm9PIlOdrK8SgVDrO1fehiThBSnAa6IdE2yWfMFJ87YioVD/gTjNLdtAT/D3/Lipu4G/eiw9CmhLRBKVgGeG2H6IssHyalv17/S2vWenNe6/HGwvbQS7zMY8DtaDbSngEejMbx0b+jeHVgjCbgjBQYhBCvqhn3wcAKqS1qs=); Phase 1 BiS: [full raid](https://wowsims.com/forever/mage/dps/#eJzElU9ME1kcx/t7M3Ref2Wh+5bszs7uYZZdFuhuN29mWsJyaeGyqx5o9OJNprTYGmibtiZ4Q8NBiYKpYKRyMESDGvHgCUi4cCoxGi5KojEhKsF48c8B9ULMjC0SJcYD1O/h9968bybzme97vzz8lYIHZFChCbogDmkYADgJcAngKgCrtl1iua2gnK6m1EOVoyjRqTzIq24U6UYeUKTPR616ccmDTlpMyk9qUKILV0B+WIMCXUiiSFdHACX6aMx+TaLL0yCPSCjS22OwWQfPAQr0bB9K9MVNkIs/oEgXhyzn2kRt/d+eYqLp7jDw9Uj4zCQMARlM5IGsRwpA1tqvA52agBtDMJxYgcFEB7XJIQRz5Hfu13Qe0LmhcW5oWsDQfIGAwTnnmsa55uPcKBJYIu7HZASZqJA2B6tTGLpugRNFemdWVqpQoE872QAw00z3Hkqlc6rO9Rafxn26v03tjpvJw7GomsqoZjQai6qRY2ouHlMzqZyZS6SSajZmZrrjalM2FlPNTLeZjPmi6ayv7Ps++P8cyaaSzcov+L23ljoZ2etQJKxCQeNZxSI58TbMChVBCOBfSjO6HzgpinR+VpYBFa9MBeaaszOZn5UVV4FY09F7+5TSyE5tA2doOw33x1exzFSE5QDuYf9hi+L/EhP+6K2jInMtbHpVKCDo+F29G12v4VP0CxVBN7CZNdpoUEZ7VUYztqK9y4NSGlnv52S8dafJJAuCLney8xU57Bo2sgb0eGtKPedEEYmRLXdhpNSFeqBhc4dcHxm3SUQ3dieRqU7WV4lAqP2fa2/CsvCMFOEl0Y8LDlv+0KR1WpFQqN8gLmvJMdAT+rkwbmkx+FuPrftBfYXIohr0zhDHN1EuVJ7tqv6c3rXv/GvX/ZdD7aWFUJd1M4+D/eBYCXoFOvNTx5YLnEMrhOB/CMNBiEMa+qGfvB8Ai+zWww==).

## Other builds of this spec

- [Arcane — Arcane Blast](../research/raid/builds/arcane-blast-raid.md) (31/13/7, 692 DPS in a full raid) — [open the talent tree](https://talentsforever.com/mage/60/050205203100301531-505001002-043-12)

---
*Generated by `_reference/data/render_modes.py` on 2026-11-11 from this project's builds and simulations of the WoW: Forever beta (talent and spell data: client build 1.60.1.70753; raid numbers: the official wowsims/forever simulator at ff9babb (client 1.60.1.70888)). Simulations, not in-game measurements. Do not hand-edit.*

