# Demonology Warlock — Raid (group)

[Warlock](../README.md) > [Raid (group)](README.md) > Demonology

**[Demonology — Raid](../research/raid/builds/demonology-ml-raid.md)** (2/31/18) — [open the talent tree](https://talentsforever.com/warlock/60/011-0025003031220301351-0550005003-12)

> 🔬 Derived build: found by this project's machine-learning search over every legal build of the spec in the community's raid simulator (raid BiS gear, then raced against the spec's builds). A model of the beta, to check at launch.

## How to play

**Setup, before the pull:** **Summon Succubus** and keep it out all fight. Keep **Demon Armor** on you.

**Before the pull:** **Shadow Bolt**.

**Talents with no line below:** **Demonic Sacrifice**: before the pull, summon your Imp and sacrifice it (+15% Shadow damage: Forever swapped Classic's aspects, so the Imp, not the Succubus, is the Shadow sacrifice), then summon your Succubus: Demonic Pact keeps the Imp's buff while another demon is out; **Soul Link**: turn it on with your demon out (it lasts while the demon lives).

**Then press the first one that is ready**, top to bottom:

1. **Bane of Doom** (timing: see below)
2. **Searing Pain** (timing: see below)
3. **Bane of Agony**, **Corruption** and **Immolate**: keep them on the target
4. **Shadow Bolt** when spell 1323392 is active (timing: see below)
5. **Life Tap** when your mana is below 50%, until the last 60 seconds of the fight
6. **Shadow Bolt**

**Shadow Bolt** is your filler: cast it whenever nothing above is ready.

**Advanced: your cooldowns and extras.** Once the list above feels easy, add these:

- **Death Coil**: in the last 3 seconds of the fight, when there is no time left for another **Shadow Bolt**
- **Searing Pain**: in the last 3 seconds of the fight, when there is no time left for another **Shadow Bolt**
- **Curse of the Elements**: about 1 time a fight

*The simulator's full rotation for this build, with every condition: [research rotation page](../research/raid/rotation.md).*


**The timing** (the simulator's own named conditions, in its words, until this page's guide is rewritten):

- “Doom tick”: dotBaseDuration
- “Searing Pain for Brand”: (not Demonic Brand is up or time left on Demonic Brand < 2.5s) and not spellIsCasting and not “in 5y range of 3T”
- “Improved Shadow Bolt Known”: spell 17794 is known

## Why this rotation

*Guide being rewritten for the new rotation (2026-11-20).*

## Talents

| Tree | Points | Talents (ranks) |
|---|---|---|
| Affliction | 2 | Suppression 1, Improved Corruption 1 |
| Demonology | 31 | Demonic Embrace 2, Unholy Power 5, Fel Vitality 3, Improved Sayaad 3, Demonic Sacrifice 1, Master Summoner 2, Decimation 2, Demonic Brand 3, Soul Link 1, Demonic Knowledge 3, Master Demonologist 5, Demonic Pact 1 |
| Destruction | 18 | Improved Shadow Bolt 5, Bane 5, Ruin 5, Agonizing Flames 3 |

## The numbers

**How this pick was checked:** a full search on 2026-10-03 (the talent search that found this build).

| Setting | DPS |
|---|---|
| Full raid, 3-minute fight (every raid buff and debuff: what this page ranks on) | 909 |

**By gear tier** (the spec's best talents for each tier and setting in its own gear, found by this project's machine-learning search in the community simulator, wowsims/forever 2e6e77d (client 70938); [every spec](../../_reference/dps-rankings.md)):

| Gear | Full raid DPS | Best talents |
|---|---|---|
| Pre-BiS | 884 | this build |
| Raid BiS | 916 | this build |

*Each row is in that tier's own gear set; the DPS at the top of the page is this build in the standard set, so the two do not match.*

**The gear** (average item level: Pre-BiS 62.4; Raid BiS 63.9; each item opens its Wowhead page, with where it drops and its enchant):

| Slot | Pre-BiS | Raid BiS |
|---|---|---|
| Head | [Spellweaver's Turban](https://www.wowhead.com/forever/item=22267) · *General Drakkisath, Blackrock Spire*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) | [Spellweaver's Turban](https://www.wowhead.com/forever/item=22267) · *General Drakkisath, Blackrock Spire*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) |
| Neck | [Nacreous Shell Necklace](https://www.wowhead.com/forever/item=22403) · *Cannon Master Willey, Stratholme* | [Choker of the Fire Lord](https://www.wowhead.com/forever/item=18814) · *Ragnaros, Molten Core* |
| Shoulders | [Mantle of the Timbermaw](https://www.wowhead.com/forever/item=19050) · *Tailoring* | [Mantle of the Timbermaw](https://www.wowhead.com/forever/item=19050) · *Tailoring* |
| Back | [Arcanoweave Cloak](https://www.wowhead.com/forever/item=272411) · *sold by Pix Xizzix* | [Arcanoweave Cloak](https://www.wowhead.com/forever/item=272411) · *sold by Pix Xizzix* |
| Chest | [Robe of the Void](https://www.wowhead.com/forever/item=14153) · *Tailoring*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) | [Robe of the Void](https://www.wowhead.com/forever/item=14153) · *Tailoring*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) |
| Wrist | [Sublime Wristguards](https://www.wowhead.com/forever/item=18497) · *Guard Mol'dar, Dire Maul*<br>+ [Enchant Bracer - Greater Intellect](https://www.wowhead.com/forever/spell=13825) | [Sublime Wristguards](https://www.wowhead.com/forever/item=18497) · *Guard Mol'dar, Dire Maul*<br>+ [Enchant Bracer - Greater Intellect](https://www.wowhead.com/forever/spell=13825) |
| Hands | [Gloves of Spell Mastery](https://www.wowhead.com/forever/item=14146) · *Tailoring* | [Gloves of Spell Mastery](https://www.wowhead.com/forever/item=14146) · *Tailoring* |
| Waist | [Belt of the Archmage](https://www.wowhead.com/forever/item=18405) · *Tailoring* | [Belt of the Archmage](https://www.wowhead.com/forever/item=18405) · *Tailoring* |
| Legs | [Leggings of Torment](https://www.wowhead.com/forever/item=22342) · *Lord Valthalak, Blackrock Spire*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) | [Flarecore Leggings](https://www.wowhead.com/forever/item=19165) · *Tailoring*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) |
| Feet | [Omnicast Boots](https://www.wowhead.com/forever/item=11822) · *Golem Lord Argelmach, Blackrock Depths*<br>+ [Enchant Boots - Minor Speed](https://www.wowhead.com/forever/spell=13889) | [Omnicast Boots](https://www.wowhead.com/forever/item=11822) · *Golem Lord Argelmach, Blackrock Depths*<br>+ [Enchant Boots - Minor Speed](https://www.wowhead.com/forever/spell=13889) |
| Finger | [Warden's Signet of Brilliance](https://www.wowhead.com/forever/item=275982) | [Ring of Spell Power](https://www.wowhead.com/forever/item=19147) · *Lucifron, Molten Core* |
| Finger | [Channeler's Ring](https://www.wowhead.com/forever/item=272406) · *sold by Pix Xizzix* | [Ring of Spell Power](https://www.wowhead.com/forever/item=19147) · *Lucifron, Molten Core* |
| Trinket | [Eye of the Beast](https://www.wowhead.com/forever/item=13968) · *quest: For The Horde!* | [Talisman of Ephemeral Power](https://www.wowhead.com/forever/item=18820) · *Magmadar, Molten Core* |
| Trinket | [Weakness Analyzer](https://www.wowhead.com/forever/item=272438) · *sold by Pix Xizzix* | [Eye of the Beast](https://www.wowhead.com/forever/item=13968) · *quest: For The Horde!* |
| Main hand | [Sageblade](https://www.wowhead.com/forever/item=22383) · *Blacksmithing*<br>+ [Enchant Weapon - Spell Power](https://www.wowhead.com/forever/spell=22747) | [Sageblade](https://www.wowhead.com/forever/item=22383) · *Blacksmithing*<br>+ [Enchant Weapon - Spell Power](https://www.wowhead.com/forever/spell=22747) |
| Off hand | [Obsidian Bauble](https://www.wowhead.com/forever/item=18316) | [Obsidian Bauble](https://www.wowhead.com/forever/item=18316) |
| Ranged/relic | [Bonecreeper Stylus](https://www.wowhead.com/forever/item=13938) · *Darkmaster Gandling, Scholomance* | [Bonecreeper Stylus](https://www.wowhead.com/forever/item=13938) · *Darkmaster Gandling, Scholomance* |

**Open in the simulator** (the community's Forever simulator on the web, loaded with the gear, enchants, talents, rotation, consumables and buffs we simulate): Pre-BiS: [full raid](https://wowsims.com/forever/warlock/dps/#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); Raid BiS: [full raid](https://wowsims.com/forever/warlock/dps/#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).

**Points that do nothing for this spec:** **Improved Sayaad** (3) only counts toward the points the tree needs before **Demonic Pact** and **Master Demonologist**.

## Other builds of this spec

- [Demonology — Demonic Pact](../research/raid/builds/demonology-pact-raid.md) (2/31/18, 902 DPS in a full raid) — [open the talent tree](https://talentsforever.com/warlock/60/101-0035003021220301351-0550005003-12)

---
*Generated by `_reference/data/render_modes.py` on 2026-11-20 from this project's builds and simulations of the WoW: Forever beta (talent and spell data: client build 1.60.1.70753; raid numbers: the official wowsims/forever simulator at 2e6e77d (client 1.60.1.70938)). Simulations, not in-game measurements. Spell ranks: trainer ranks only. The class books' ranks (Grimoire of Shadow Bolt X, Tome of Frostbolt XI and the like) are not in Forever on the evidence there is (2026-11-20): in Classic every one drops in the Ruins of Ahn'Qiraj, which Forever's roadmap does not have; Wowhead's Forever pages list no source for them; the simulator's own authors leave them off by default. Checked again when the raids of 2026-12-09 open. Do not hand-edit.*

