# Destruction Warlock — Raid (group)

[Warlock](../README.md) > [Raid (group)](README.md) > Destruction

**[Destruction — Raid](../research/raid/builds/destruction-ml-raid.md)** (9/11/31) — [open the talent tree](https://talentsforever.com/warlock/60/252-0050203001-055031500310035-12)

> 🔬 Derived build: found by this project's machine-learning search over every legal build of the spec in the community's raid simulator (raid BiS gear, then raced against the spec's builds); it beat the hand-made build (Destruction — Incinerate), which stays below as the alternative. A model of the beta, to check at launch.

**Other setups of this spec.** This build is the Shadow Bolt setup. The spec's best build for each other setup, in a full raid:

- Incinerate: [Destruction — Incinerate](../research/raid/builds/destruction-incinerate-open-raid.md) (10/11/30, 785 DPS in a full raid) — [open the talent tree](https://talentsforever.com/warlock/60/253-0050203001-055030500310035-12)

## How to play

**Setup, before the pull:** **Summon Imp**, then **Demonic Sacrifice** it: you fight with its buff and no demon, which the rotation below assumes. Keep **Demon Armor** on you.

**Before the pull:** **Life Tap**.

**Talents with no line below:** **Demonic Sacrifice**: before the pull, summon your Imp and sacrifice it (+15% Shadow damage for 2 hours; summoning any demon cancels it).

**Then press the first one that is ready**, top to bottom:

1. **Curse of the Elements**: keep it on the target
2. **Life Tap** when your mana is below 5%
3. **Bane of Agony**: keep it on the target
4. **Corruption**: keep it on the target, until the last 10 seconds of the fight
5. **Immolate**: keep it on the target, until the last 20 seconds of the fight
6. **Conflagrate**
7. **Shadow Bolt** (rank 9)

**Shadow Bolt** is your filler: cast it whenever nothing above is ready.

**Advanced: your cooldowns and extras.** Once the list above feels easy, add these:

- **Searing Pain**: in the last 3.5 seconds of the fight, when there is no time left for another **Shadow Bolt**

*The simulator's full rotation for this build, with every condition: [research rotation page](../research/raid/rotation.md).*

## Why this rotation

Before the pull: put on **Demon Armor**, summon the Imp, use **Demonic Sacrifice** (+15% Shadow damage for 2 hours, worth about 10% of your damage in the simulator) and **Life Tap** once so you start full. In the fight Destruction is still a **Shadow Bolt** spec: keep **Immolate** on the boss so **Conflagrate** can go out every 10 seconds, and let **Shadow and Flame** turn each **Conflagrate** into 20% more Shadow damage for 20 seconds.

**Why it works**

- Before the pull: summon the Imp and use **Demonic Sacrifice** (summoning any demon ends it), then **Life Tap** once. Put a Spellstone (**Create Spellstone**) on your weapon on top of your wizard oil: Forever lets them stack, and the simulator measured about 3% more damage. **Demonic Embrace**, **Demonic Aegis** and **Fel Vitality** are the points that reach the sacrifice: **Demonic Aegis** makes **Demon Armor** 30% stronger and **Fel Vitality** adds 15% to your maximum mana. This build has no **Amplify Curse**.
- **Curse of the Elements** goes up first: 10% more damage from every magic school, Fire and Shadow alike, and as a Curse it sits beside your **Bane of Agony**. **Life Tap** waits until you are below 5% mana, and **Improved Life Tap** adds 20% to each tap.
- **Bane of Agony** grows over its 24 seconds, so recast it only once it has run out. **Corruption** (a 1.2-second cast with this build's 2 points in **Improved Corruption**) goes back up when it is about to run out, but not in the last 10 seconds.
- **Immolate** matters as much for **Conflagrate**, which needs it on the target, as for its own damage: start a new one when less than its cast (1.5 seconds with the **Bane** talent) is left on the old one, but not in the last 20 seconds.
- **Conflagrate** goes out whenever it is ready. With 5 points in **Shadow and Flame** it no longer eats your **Immolate** (each rank is a 20% chance not to), and each hit gives you 20% more Shadow damage for 20 seconds, twice its cooldown; **Fire and Brimstone** and **Ruin** make its crits frequent and big.
- **Shadow Bolt** is the filler: the sacrificed Imp, **Improved Shadow Bolt**, **Ruin** and **Shadow and Flame** all raise Shadow damage, so the filler is the one spell they all feed.

**Caveats**

- The last seconds belong to quick spells: with 3.5 seconds left the rotation casts **Searing Pain** (a 1.5-second cast) because a **Shadow Bolt** still casting when the boss dies does nothing. It does not belong earlier in the fight.
- With the Imp sacrificed you play without a demon: any summon ends the buff, so if you die, summon the Imp and sacrifice it again before the next pull.
- On the move, **Bane of Agony**, **Curse of the Elements**, **Conflagrate** and **Life Tap** are instant; **Corruption** still has a 1.2-second cast in this build.

**When to change it**

- In the last 20 seconds start no new **Immolate**, and in the last 10 no **Corruption**: cast **Shadow Bolt**, then **Searing Pain** in the last 3.5 seconds.
- The other setup listed on this page plays a different rotation: follow the list on its own page, not this one.
- A boss needs only one **Curse of the Elements** (in Classic two never stacked): if another warlock keeps it up, take the curse your raid gives you, such as **Curse of Recklessness** for the physical fighters.

## Talents

| Tree | Points | Talents (ranks) |
|---|---|---|
| Affliction | 9 | Improved Life Tap 2, Suppression 5, Improved Corruption 2 |
| Demonology | 11 | Demonic Embrace 5, Demonic Aegis 2, Fel Vitality 3, Demonic Sacrifice 1 |
| Destruction | 31 | Improved Shadow Bolt 5, Bane 5, Cataclysm 3, Aftermath 1, Ruin 5, Agonizing Flames 3, Conflagrate 1, Fire and Brimstone 3, Shadow and Flame 5 |

## The numbers

| Setting | DPS |
|---|---|
| Full raid, 3-minute fight (every raid buff and debuff: what this page ranks on) | 806 |

**By gear tier** (the spec's best talents for each tier and setting in its own gear, found by this project's machine-learning search in the community simulator, wowsims/forever 2e6e77d (client 70938); [every spec](../../_reference/dps-rankings.md)):

| Gear | Full raid DPS | Best talents |
|---|---|---|
| Quests and dungeons | 702 | this build |
| Pre-BiS | 778 | [10/11/30](https://talentsforever.com/warlock/60/253-0050203001-055030500310035-12) |
| Raid BiS | 808 | this build |

*Each row is in that tier's own gear set; the DPS at the top of the page is this build in the standard set, so the two do not match.*

**The gear** (average item level: Quests and dungeons 60.2; Pre-BiS 62.2; Raid BiS 63.9; each item opens its Wowhead page, with where it drops and its enchant):

| Slot | Quests and dungeons | Pre-BiS | Raid BiS |
|---|---|---|---|
| Head | [Crimson Felt Hat](https://www.wowhead.com/forever/item=18727) · *Magistrate Barthilas, Stratholme*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) | [Spellweaver's Turban](https://www.wowhead.com/forever/item=22267) · *General Drakkisath, Blackrock Spire*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) | [Spellweaver's Turban](https://www.wowhead.com/forever/item=22267) · *General Drakkisath, Blackrock Spire*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) |
| Neck | [Nacreous Shell Necklace](https://www.wowhead.com/forever/item=22403) · *Cannon Master Willey, Stratholme* | [Nacreous Shell Necklace](https://www.wowhead.com/forever/item=22403) · *Cannon Master Willey, Stratholme* | [Choker of the Fire Lord](https://www.wowhead.com/forever/item=18814) · *Ragnaros, Molten Core* |
| Shoulders | [Shroud of the Nathrezim](https://www.wowhead.com/forever/item=18720) · *Balnazzar, Stratholme* | [Mantle of the Timbermaw](https://www.wowhead.com/forever/item=19050) · *Tailoring* | [Mantle of the Timbermaw](https://www.wowhead.com/forever/item=19050) · *Tailoring* |
| Back | [Spritecaster Cape](https://www.wowhead.com/forever/item=11623) · *Houndmaster Grebmar, Blackrock Depths* | [Arcanoweave Cloak](https://www.wowhead.com/forever/item=272411) · *sold by Pix Xizzix* | [Arcanoweave Cloak](https://www.wowhead.com/forever/item=272411) · *sold by Pix Xizzix* |
| Chest | [Robe of Everlasting Night](https://www.wowhead.com/forever/item=18385) · *Immol'thar, Dire Maul*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) | [Robe of the Void](https://www.wowhead.com/forever/item=14153) · *Tailoring*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) | [Robe of the Void](https://www.wowhead.com/forever/item=14153) · *Tailoring*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) |
| Wrist | [Sublime Wristguards](https://www.wowhead.com/forever/item=18497) · *Guard Mol'dar, Dire Maul*<br>+ [Enchant Bracer - Greater Intellect](https://www.wowhead.com/forever/spell=13825) | [Sublime Wristguards](https://www.wowhead.com/forever/item=18497) · *Guard Mol'dar, Dire Maul*<br>+ [Enchant Bracer - Greater Intellect](https://www.wowhead.com/forever/spell=13825) | [Sublime Wristguards](https://www.wowhead.com/forever/item=18497) · *Guard Mol'dar, Dire Maul*<br>+ [Enchant Bracer - Greater Intellect](https://www.wowhead.com/forever/spell=13825) |
| Hands | [Hands of Power](https://www.wowhead.com/forever/item=13253) · *Quartermaster Zigris, Blackrock Spire* | [Gloves of Spell Mastery](https://www.wowhead.com/forever/item=14146) · *Tailoring* | [Gloves of Spell Mastery](https://www.wowhead.com/forever/item=14146) · *Tailoring* |
| Waist | [Highlander's Cloth Girdle](https://www.wowhead.com/forever/item=20047) · *sold by Samuel Hawke* | [Belt of the Archmage](https://www.wowhead.com/forever/item=18405) · *Tailoring* | [Belt of the Archmage](https://www.wowhead.com/forever/item=18405) · *Tailoring* |
| Legs | [Skyshroud Leggings](https://www.wowhead.com/forever/item=13170) · *Highlord Omokk, Blackrock Spire*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) | [Skyshroud Leggings](https://www.wowhead.com/forever/item=13170) · *Highlord Omokk, Blackrock Spire*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) | [Flarecore Leggings](https://www.wowhead.com/forever/item=19165) · *Tailoring*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) |
| Feet | [Omnicast Boots](https://www.wowhead.com/forever/item=11822) · *Golem Lord Argelmach, Blackrock Depths*<br>+ [Enchant Boots - Minor Speed](https://www.wowhead.com/forever/spell=13889) | [Omnicast Boots](https://www.wowhead.com/forever/item=11822) · *Golem Lord Argelmach, Blackrock Depths*<br>+ [Enchant Boots - Minor Speed](https://www.wowhead.com/forever/spell=13889) | [Omnicast Boots](https://www.wowhead.com/forever/item=11822) · *Golem Lord Argelmach, Blackrock Depths*<br>+ [Enchant Boots - Minor Speed](https://www.wowhead.com/forever/spell=13889) |
| Finger | [Songstone of Ironforge](https://www.wowhead.com/forever/item=12543) · *quest: The Princess's Surprise* | [Warden's Signet of Brilliance](https://www.wowhead.com/forever/item=275982) | [Ring of Spell Power](https://www.wowhead.com/forever/item=19147) · *Lucifron, Molten Core* |
| Finger | [Eye of Orgrimmar](https://www.wowhead.com/forever/item=12545) · *quest: The Princess Saved?* | [Elemental Focus Band](https://www.wowhead.com/forever/item=20682) · *Prince Skaldrenox, Silithus* | [Ring of Spell Power](https://www.wowhead.com/forever/item=19147) · *Lucifron, Molten Core* |
| Trinket | [Eye of the Beast](https://www.wowhead.com/forever/item=13968) · *quest: For The Horde!* | [Weakness Analyzer](https://www.wowhead.com/forever/item=272438) · *sold by Pix Xizzix* | [Talisman of Ephemeral Power](https://www.wowhead.com/forever/item=18820) · *Magmadar, Molten Core* |
| Trinket | [Royal Seal of Eldre'Thalas](https://www.wowhead.com/forever/item=18467) · *quest: Harnessing Shadows* | [Eye of the Beast](https://www.wowhead.com/forever/item=13968) · *quest: For The Horde!* | [Eye of the Beast](https://www.wowhead.com/forever/item=13968) · *quest: For The Horde!* |
| Main hand | [Witchblade](https://www.wowhead.com/forever/item=13964) · *Darkmaster Gandling, Scholomance*<br>+ [Enchant Weapon - Spell Power](https://www.wowhead.com/forever/spell=22747) | [Sageblade](https://www.wowhead.com/forever/item=22383) · *Blacksmithing*<br>+ [Enchant Weapon - Spell Power](https://www.wowhead.com/forever/spell=22747) | [Sageblade](https://www.wowhead.com/forever/item=22383) · *Blacksmithing*<br>+ [Enchant Weapon - Spell Power](https://www.wowhead.com/forever/spell=22747) |
| Off hand | [Spirit of Aquementas](https://www.wowhead.com/forever/item=11904) · *quest: It's Dangerous to Go Alone* | [Obsidian Bauble](https://www.wowhead.com/forever/item=18316) | [Obsidian Bauble](https://www.wowhead.com/forever/item=18316) |
| Ranged/relic | [Bonecreeper Stylus](https://www.wowhead.com/forever/item=13938) · *Darkmaster Gandling, Scholomance* | [Bonecreeper Stylus](https://www.wowhead.com/forever/item=13938) · *Darkmaster Gandling, Scholomance* | [Bonecreeper Stylus](https://www.wowhead.com/forever/item=13938) · *Darkmaster Gandling, Scholomance* |

**Open in the simulator** (the community's Forever simulator on the web, loaded with the gear, enchants, talents, rotation, consumables and buffs we simulate): Quests and dungeons: [full raid](https://wowsims.com/forever/warlock/dps/#eJzElU9oK1UUxnPuTDI3p9o37z6l03kqYyCPGJhwZ8LYtJvMe6uHq+JKfP5p0qRNQpuETBYVEVpaUKS2pVk1FKxWaRXU4kKLK7sIxI3WjZtSLIrUZSnSpcpMJlXSLlykeBbJyfly5/y+e+5w8SkKMiigQQwmoABVmAd4B2ALYBeAPeapxFVToH4wQAU5rJZRojvroPw2gCJd/AJQpFvrgAI9fRkl+uMqKL8OokQP1kA5GkSBtqZRpD9sAobo+ZS7KkQ/f0VZlVCgf2VQoAtZFOjaLIp0e8390/Ks0r6DAp1/FQV6PhMx5XYx9v0K8Ivs+HsfwrtAlorrQC6yTQie3n//Y/gUpJ1N2Hu4UtyD7dIJLBUfUA8cbPiGPGNaps65xU2e5NzQuWXxpGFxnjQ4T1ptIhySgV/IbhjvIFVDKNKzFYhIGERBtxx8AiU1iAL95FEkjBIGdSNhOexp9S7ejtzCx78ERJF++/Y4I3LQW+3mpsoxxu7h7fgtGmLkhYDqPc+wHK8kMpL1SyNWVBWRKAprAHstU515vVKtayY3n9cNrnNzTJssZMrT+ZxWqWmZXC6f07JvaPVCXqtV6pl6sVLWnHymNlnQYk4+rzlZvZYp5vSuqHfERMmplJ9Tjf8IleJR17N8kWWiSsYCHbsd8MtlCcuz+3UDrpOTvry4DOzNHmN8VDdH+mpsGOX4IBW8bQ2hiMSK+kNjqF4OlUVUDYfiT1KRSSVXPnik0ibxs84X2+wdg0ub6ivtGHKWwOH4EBUZLblwP7dADTeJn16ZEHdUX7oeb+SG8Y7/wTu+imf6eMctYKUeOvcMG32l60zzjwawt3p7GTrv707c7VrtvhimFXXby0uNa6z2vb1nVf7qUL48xEctUITfSRvOiLkgBLwYtZuEYghFjdgQ+ZOE3WJgfsoebm648V362SkvfkqbJ0QRtXR8nwT+l6jb3exG495nN9Zn1Pt88SP7vl+wJ9zrcgO8H4GTdFyg+0MP/nWrckiBDQ9hHF6CAlRhDubI3wMAiJaLhQ==); Pre-BiS: [full raid](https://wowsims.com/forever/warlock/dps/#eJzElU9oI2UYxvN+8yXz5a12Z79VOp1VGQNZYmDCNxPGpr1kdk+Lp+JJWNFNNqlJWJOQyWFFhJUtKLKmi/GyseDfYhVai4daPFmhkHqQnLyUYlGKIoKlSC+CyEwmVdIePKTse5i8eR/evL9n3i98+BgDBVTQIQHXoQR1uA3wJsAHAMsA/CFfJZ6aAW1pjElKVGugzP5aAXV/DCm78wUgZb+96z3f6ykYYdtV9edxlNnmPVB3xlFi31aRsv0FwAg7nPO6Imz1eXVBRspavytI2Xcfet3rPQUldu9llNkfq6B2LyBldxcAJXZ4M2Yp3XLi+xaIo/zs2x/BW0Dmy+8AOcp3IPzL5feX4HOQP12Etaut8hp8XNmD+fIV5sODA1+TJyw7bQhhC0ukhTANYdsiLWwh0qYQabtLpB4Z+4ksR/ECMi2ClB20ICZjGCXDdvERlLUwSuyza7Eoyhg2zJTt8se1i3g+dg4f/hIQKfvmjVlOlLDf7eWWJjDBL+H55DkW4eSZkOb/nmm7folykg9KU3Zco0hUlbeBv5Cr33yxVm/qlrCeNkxhCGtGv1HKVV8qFvRaQ88VCsWCnn9Fb5aKeqPWzDXLtaruFnONGyU94RaLups3GrlywRiIRl9MVdxa9SnN/J9QGRH3PCtHeU41MhPq2+2DH7elbN/uV204TU4H8p27wF8dMiamDWtqpMYmUUmOM8l/rRGkSOx4sDSO2vFSeUzTcSL5KKNcrnjy5jWNdUiQ9T/44vAaPNrMSGlnUPAUTiYnGOWs4sH9uAVatEOC9MSGhKsF0ul4U2eMt/sv3u5JPCvA290CXhmi886wOVK6/jb/bAN/bXiWaYjRvomLA6uDP4Zlx73xynz7FKsjH+9bVdZ7yvEh3tkCVfqVdOGAWK9LIT+mnQ5hGEGqEwdif5OoVwzdnnMmO/e92M4+OefHD1lrj6hUzyY3SOiBRNMZZGcal1bObM60/3z2E+dyUHCue1fmffC/hPaySYltTFz5z80qIAMOXIVZeA5KUIdbcIv8MwAPtY5i); Raid BiS: [full raid](https://wowsims.com/forever/warlock/dps/#eJzElU9oK1UUxnPuTDI3p9o37z6l03kqYyCPGJhwZ8LYtJvMe6uHq+JKeKIvaVKTUJOQyaIiQsWAIrUtjV00FhT/VqGluNDiygqFFEG6clOCRSmKG4tIN0KRmUyipF24SHlncXNyPm7O77vnhouPUZBBAQ1icB8KUIUFgLcAPgDYBGAPeSpx1RSon45QQQ6rDkr07y1QTkZQpOergCL9/V13fe9QxhA9KCu/jKJE91ZAORpFgX5XRpGeLANKtLPmbQvR7eeVZQlF+v0a9NdGE1CgKy+jRP/YBqV9A0W6uOzW/pyLmHK7GPthCfhZdvqdD+FtII3iKpCzbAuCv95+/xP4AqTPNmDn7lJxBz4qHUOjeId69GDDN+QJ0zJ1zi1u8iTnhs4tiycNi/OkwXnSahPhkIz8TDbDeAOpGkKRni5BRMIgCrrl4CMoqUEU6Of3ImGUMKgbCcthj6s38XrkGj78JSCK9Ns3pxmRg95uNzdVjjF2C6/Hr9EQI88EVO/3DMvxSiIjWb80YUVVEYmisCawFzLVuRcr1bpmcvNp3eA6N6e0mUKm/FI+p1VqWiaXy+e07CtavZDXapV6pl6slDUnn6nNFLSYk89rTlavZYo5vSfqXTFRcirlp1Tjf0KleNT1LJ9lmaiSqUDXbhe8vy1heXa/bsJlctKX31gE9uqAMT6pmxNDNTaOcnyUCt6xhlBEYkX9oTFU+0NlEVXDsfijVGRSyZX37qm0Rfys+8E2Bsfg0qaGSjuFnCVwPD5GRUZLLtxP+6CGW8RPL0yIO6ovXY43ccV4nX/xOhfxTB+vsw+sNEDn3mFjqHTdaf7VBPbaYC9D58M9iZs9q70/hmlF3fZyo3mJ1aG396zKXx3K/Ut8tA+K8BtpwykxXxcCXkzaLUIxhKJGbIick7BbDCzM2uOtdTcO0k/OevFj2jwmiqil47sk8ECibveyK41bW1fWZ9Jbn/3Yvu0X7Pvum7kO3pfAcTou0N2xO/95WjmkwIa7MA3PQQGqMA/z5J8BAM3njiw=).

## Other builds of this spec

- [Destruction — Incinerate](../research/raid/builds/destruction-incinerate-raid.md) (9/11/31, 746 DPS in a full raid) — [open the talent tree](https://talentsforever.com/warlock/60/153-0050203001-0050245103101351-12)

---
*Generated by `_reference/data/render_modes.py` on 2026-11-19 from this project's builds and simulations of the WoW: Forever beta (talent and spell data: client build 1.60.1.70753; raid numbers: the official wowsims/forever simulator at 2e6e77d (client 1.60.1.70938)). Simulations, not in-game measurements. Do not hand-edit.*

