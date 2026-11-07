# Shadow Priest — Raid (group)

[Priest](../README.md) > [Raid (group)](README.md) > Shadow

**✅ Recommended** for raid (the best priest spec here, or within 3% of it).

**[Shadow — Raid](../research/raid/builds/shadow-ml-raid.md)** (16/0/35) — [open the talent tree](https://talentsforever.com/priest/60/005305201--50552001201312251-12)

> 🔬 Derived build: found by this project's machine-learning search over every legal build of the spec in the community's raid simulator (phase-1 BiS gear, then raced against the spec's builds). A model of the beta, to check at launch.

## How to play

**Before the pull, then keep up all fight:** **Shadowform**.

**Then press the first one that is ready**, top to bottom:

1. **Mind Blast**
2. **Shadow Word: Pain**: keep it on the target, until the last 10 seconds of the fight
3. **Inner Focus**, then straight away **Devouring Plague**
4. **Shadow Word: Death**
5. **Devouring Plague**
6. **Mind Flay**

**Mind Flay** is your filler: cast it whenever nothing above is ready.

*The simulator's full rotation for this build, with every condition: [research rotation page](../research/raid/rotation.md).*

## Why this rotation

Shadow in a raid is **Shadowform** before the pull, **Mind Blast** every time it is ready, **Shadow Word: Pain** kept on the boss, **Devouring Plague** and **Shadow Word: Death** on cooldown, and **Mind Flay** in every gap. The best priest damage page: 788 DPS in a full raid.

**Why it works**

- **Shadowform** is what makes the spec work: 10% more Shadow damage, half the mana cost on every Shadow spell, a doubled critical strike bonus and 15% less physical damage taken. You cannot cast heals in it.
- **Mind Blast** comes first (22 casts, 19%): 477-503 damage in a 1.5-second cast every 5.5 seconds with **Improved Mind Blast**. The latest re-tune (2026-11-02) moved it to the top, ahead of **Shadow Word: Death** and the dots, for +0.3%.
- **Shadow Word: Pain** (8 casts, 20%): 762 damage over 24 seconds with **Improved Shadow Word: Pain**, for one global cooldown. Recast it when it falls off, not in the last 10 seconds. Every Shadow spell also stacks **Shadow Weaving** on the target (2% more Shadow damage from you per stack, up to 5, for 15 seconds), so steady casting keeps it full.
- **Inner Focus** makes your next spell free, and the list spends it on the first **Devouring Plague**: its 985 mana is halved by **Devouring Contagion** but it is still the dearest spell you have; the 25% crit bonus does not apply to a damage-over-time spell, so the pair only saves mana.
- **Shadow Word: Death** (9 casts, 9%) and then **Devouring Plague** (7 casts, 11%) each time they are ready: **Shadow Word: Death** is instant on an 18-second cooldown and crits 30% more often below 20% of the boss's health with **Early Demise**; **Devouring Plague** lasts 24 seconds on a 24-second cooldown, so it is up all fight, and heals you for the damage it deals.
- **Mind Flay** fills every gap and is 40% of your damage (38 casts): 390 damage over 3 seconds for 205 mana (102 in **Shadowform**), each tick 20% stronger than the last with **Improved Mind Flay**, and **Darkness** adds 10% to everything.
- Mana is not your problem in a full raid: the simulator's priest never runs dry with one mana potion and two Demonic Runes a fight. **Spirit Tap** does nothing on a boss: it needs a kill.

**Caveats**

- **Shadow Word: Death** hits you for 30% of your maximum health every time the target survives it (the 2026-11-02 patch tripled the backlash), about 9 times in a 3-minute fight: nearly three health bars that your healers pay for. The damage numbers ignore that. **Devouring Plague** heals a little of it back.
- **Mind Blast** causes a lot of threat (its tooltip says so) and leads the list. In the first seconds of a fight or after a tank swap, hold it until the tank is ahead; **Silent Resolve** cuts the threat of your spells by 30%.
- When you must move, **Mind Flay** and **Mind Blast** stop: use the instants, **Shadow Word: Death**, **Devouring Plague** and **Shadow Word: Pain** if it fell off. **Shadow Weaving** drops after 15 seconds without a Shadow spell.
- A 6-minute fight: the simulator's DPS falls from 788 at 3 minutes to 483 at 6 as the mana runs out.

**When to change it**

- If your healers struggle, cast **Shadow Word: Death** only in the last 20% of the boss's health, where **Early Demise** makes it crit: fewer casts, each more likely to kill (no backlash on a kill). You give up a few percent of damage.
- With adds up, keep **Shadow Word: Pain** on the ones that live longest and **Devouring Plague** on one that dies first: **Devouring Contagion** makes the plague jump to two nearby enemies when its target dies. The simulator fights one target.
- **Vampiric Embrace** has no line because the simulator counts only damage: on the boss, for 30 seconds your party heals for 20% of your Shadow damage, for 40 mana and one global cooldown. **Silence** stops a casting add.
- Out of mana in a long fight: **Dark Sacrifice** turns 1,600 of your health over 15 seconds into 1,600 mana plus your Spirit, once every 10 minutes; the full list holds it below **Mind Flay**, so it only fires when you cannot afford a **Mind Flay**.

## The numbers

| Setting | DPS |
|---|---|
| Full raid, 3-minute fight (every raid buff and debuff: what this page ranks on) | 788 |

**By gear tier** (the spec's best talents for each tier and setting in its own gear, found by this project's machine-learning search in the community simulator, wowsims/forever bac92db (client 70707); [every spec](../../_reference/dps-rankings.md)):

| Gear | Full raid DPS | Best talents |
|---|---|---|
| Pre-BiS | 837 | [17/0/34](https://talentsforever.com/priest/60/0053050010102--50252101221311251-12) |
| Phase 1 BiS | 850 | [18/0/33](https://talentsforever.com/priest/60/525005001--50052101231302251-12) |

**The gear** (average item level: Pre-BiS 71.4; Phase 1 BiS 70.6; each item opens its Wowhead page, with where it drops and its enchant):

| Slot | Pre-BiS | Phase 1 BiS |
|---|---|---|
| Head | [Tiara of the Oracle](https://www.wowhead.com/forever/item=21348) · *quest: Tiara of the Oracle*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) | [Tiara of the Oracle](https://www.wowhead.com/forever/item=21348) · *quest: Tiara of the Oracle*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) |
| Neck | [Charm of the Shifting Sands](https://www.wowhead.com/forever/item=21504) · *quest: The Fall of Ossirian* | [Choker of the Fire Lord](https://www.wowhead.com/forever/item=18814) · *Ragnaros, Molten Core* |
| Shoulders | [Mantle of the Timbermaw](https://www.wowhead.com/forever/item=19050) · *Tailoring* | [Mantle of the Timbermaw](https://www.wowhead.com/forever/item=19050) · *Tailoring* |
| Back | [Hide of the Wild](https://www.wowhead.com/forever/item=18510) · *Leatherworking* | [Fel Cape](https://www.wowhead.com/forever/item=279269) · *Tailoring* |
| Chest | [Vestments of the Oracle](https://www.wowhead.com/forever/item=21351) · *quest: Vestments of the Oracle*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) | [Vestments of the Oracle](https://www.wowhead.com/forever/item=21351) · *quest: Vestments of the Oracle*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) |
| Wrist | [Rockfury Bracers](https://www.wowhead.com/forever/item=21186) · *quest: Stalwart's Battlegear*<br>+ [Enchant Bracer - Greater Intellect](https://www.wowhead.com/forever/spell=13825) | [Rockfury Bracers](https://www.wowhead.com/forever/item=21186) · *quest: Stalwart's Battlegear*<br>+ [Enchant Bracer - Greater Intellect](https://www.wowhead.com/forever/spell=13825) |
| Hands | [Gloves of Spell Mastery](https://www.wowhead.com/forever/item=14146) · *Tailoring* | [Gloves of Spell Mastery](https://www.wowhead.com/forever/item=14146) · *Tailoring* |
| Waist | [Belt of the Archmage](https://www.wowhead.com/forever/item=18405) · *Tailoring* | [Belt of the Archmage](https://www.wowhead.com/forever/item=18405) · *Tailoring* |
| Legs | [Trousers of the Oracle](https://www.wowhead.com/forever/item=21352) · *quest: Trousers of the Oracle*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) | [Flarecore Leggings](https://www.wowhead.com/forever/item=19165) · *Tailoring*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) |
| Feet | [Marshal's Satin Sandals](https://www.wowhead.com/forever/item=17607) · *sold by Sergeant Major Clate*<br>+ [Enchant Boots - Minor Speed](https://www.wowhead.com/forever/spell=13889) | [Marshal's Satin Sandals](https://www.wowhead.com/forever/item=17607) · *sold by Sergeant Major Clate*<br>+ [Enchant Boots - Minor Speed](https://www.wowhead.com/forever/spell=13889) |
| Finger | [Ring of the Fallen God](https://www.wowhead.com/forever/item=21709) · *quest: The Savior of Kalimdor* | [Ring of the Fallen God](https://www.wowhead.com/forever/item=21709) · *quest: The Savior of Kalimdor* |
| Finger | [Signet Ring of the Bronze Dragonflight](https://www.wowhead.com/forever/item=21210) · *quest: The Grand Invoker* | [Ring of Spell Power](https://www.wowhead.com/forever/item=19147) · *Lucifron, Molten Core* |
| Trinket | [Talisman of Ascendance](https://www.wowhead.com/forever/item=22678) · *quest: Epic Armaments of Battle - Friend of the Dawn* | [Talisman of Ascendance](https://www.wowhead.com/forever/item=22678) · *quest: Epic Armaments of Battle - Friend of the Dawn* |
| Trinket | [Weakness Analyzer](https://www.wowhead.com/forever/item=272438) · *sold by Pix Xizzix* | [Weakness Analyzer](https://www.wowhead.com/forever/item=272438) · *sold by Pix Xizzix* |
| Main hand | [Grand Marshal's Mageblade](https://www.wowhead.com/forever/item=23451) · *sold by Lieutenant Jackspring*<br>+ [Enchant Weapon - Spell Power](https://www.wowhead.com/forever/spell=22747) | [Grand Marshal's Mageblade](https://www.wowhead.com/forever/item=23451) · *sold by Lieutenant Jackspring*<br>+ [Enchant Weapon - Spell Power](https://www.wowhead.com/forever/spell=22747) |
| Off hand | [Master Dragonslayer's Orb](https://www.wowhead.com/forever/item=19366) · *quest: The Lord of Blackrock* | [Master Dragonslayer's Orb](https://www.wowhead.com/forever/item=19366) · *quest: The Lord of Blackrock* |
| Ranged/relic | [Brilliant Wand](https://www.wowhead.com/forever/item=249385) · *Enchanting* | [Brilliant Wand](https://www.wowhead.com/forever/item=249385) · *Enchanting* |

**Open in the simulator** (the community's Forever simulator on the web, loaded with the gear, enchants, talents, rotation, consumables and buffs we simulate): Pre-BiS: [full raid](https://wowsims.com/forever/priest/dps/#eJzElMFLVF8Ux+fceTPvzBn1N7wf4fPS4jpBTMaT+55NmJt5upIgkkBol09nbCZq3uAb0HYWLipIRcLQhCLSNAhqU9LSgqZF4qpFbaQSJVoUgS6CiDuj0D9gfRdf7jkfzv1eLtxLBxESYIKAFPRBHkowCnAN4B7AIoBRV6VM0XbgXzXERIQPk46fF8DciJOGo4tAGn65pXx1EkjHzQUwPzWQjivzYH5ooDCuFEnDjQkFt2pzOr6+DuaEThq+XVKj7+eVTz9V/mwtQTreeQ5m5X/ScOG2ai7N/Zc8mqgUUqvjILf7e27ehxvAxgpTwLb7Z4Ftdj4C/eEcPOkeL6zDWKELq0cHF14wIWW6TaaltKUtHctKSyft2NJ2HLvNtp20XWGwxuIf2Q9GBuk8QmH8PpLUKUJhyw6MOI9xnSKpGL7sNTTOOkKG5K10yGim+mScYo6CiOO9lGhpwKjBToZ4lDRituR7yGjijc6B3c3vBkQcKZqK4to0GHW8Vmn4aue04RueV7p4zi+VhSOd45YtLdneIQbyXvF8Liv8IeFls7ms6L8syvmcGPLLXrngF0WQ84YG8iIV5HIiyHtZf9jKlgJrj1s13noh8ItHdgNr8fU8fhVUfhR3psC49DfyUV0QTv48ZYa3WAW+MedKOFTVMXcFNM4olPzFYqoRGh10m2ZnlN5kmgerepdx1pmpiUzLMgv9E5XdvdW+6vDjfcs5UfUzD9zO3Ybbp17+DFSL0HqmJYzLjV1/fBAS2sGFbuiBs5CHEozACPs9AAEUvH8=); Phase 1 BiS: [full raid](https://wowsims.com/forever/priest/dps/#eJzElNFLFF8Ux+fcnd05e1b97W8iHC8+jBvEZozcGdswX3b0SYJIAqG3HN213aidxVnQ3iwMKkhD0tCEIsoyCOqlpEcL2ojCp14ikEqUnopAHwKJOyr0D1jfhy/nnA9nvsOFe6kRIQkGmJCGXihAGUYALgPcAXgIoNeElEnaBnxNRUxG+RBp+HUOjJUEqbg5AaTitxvSVy79TxquzoHxpY40XLwPxsc6iuBiScJxIA0/TYZ7Gr6+Asa4Riq+m5erbyelTz2V/mwpSRreeg5GdQ+pOHdTDudn/0sdTFaL6fdjINb7uq/dhavARosTwNb7ZoCtdjwC7cEsPOkaKy7DaLETw18HF16wxoyTESIjhG1ZsnBsYTutdqtwnIxdZbDEEp/ZT0Y6aTxKEfwxnNIoShHLDvQEj3ONouk4vuzRVc7aFV3wFtqnN1FtKkFxR0LEsR5KNtdhTGdHFR4jlZgt+A7SG3i9s3f747cDIo4US8dwaQr0Gr7Vqfhq47ju655XPnvKL1dMRziHLVtYoq3d7C94pdP5nOkPml4ul8+ZfefNSiFvDvoVr1L0S2aQ9wb7C2Y6yOfNoODl/CErVw6sHW5t8ZYzgV86sB24FV/LExdB5sdwYwL0c38jH+UB4fVfx4zIGqvCd+ZciCihDrmLoHJGSmqTxeVAGRlwG2ampd5kmwZCfcg6y8xQzWzzAlP+iSruTrWr2v9413KOhH7intuxPXB75a2fhrBRlrPNEVyo7/zjcRDQBi50QTechAKUYRiG2e8BAK3YvAA=).

## Other builds of this spec

- [Shadow (optimized)](../research/raid/builds/opt-shadow-dps-raid-dps.md) (20/0/31, 783 DPS in a full raid) — [open the talent tree](https://talentsforever.com/priest/60/52500500003--50052101231302051-12)

---
*Generated by `_reference/data/render_modes.py` on 2026-11-04 from this project's builds and simulations of the WoW: Forever beta (talent and spell data: client build 1.60.1.70753; raid numbers: the official wowsims/forever simulator at bac92db (client 1.60.1.70707)). Simulations, not in-game measurements. Do not hand-edit.*

