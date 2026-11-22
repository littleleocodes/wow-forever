# Shadow Priest — Raid (group)

[Priest](../README.md) > [Raid (group)](README.md) > Shadow

**✅ Recommended** for raid (the best priest spec here, or within 3% of it).

**[Shadow — Raid](../research/raid/builds/shadow-ml-raid.md)** (16/0/35) — [open the talent tree](https://talentsforever.com/priest/60/005305201--50552001201312251-12)

> 🔬 Derived build: found by this project's machine-learning search over every legal build of the spec in the community's raid simulator (raid BiS gear, then raced against the spec's builds). A model of the beta, to check at launch.

## How to play

**Before the pull, then keep up all fight:** **Shadowform**.

**Talents with no line below:** **Vampiric Embrace**: taken because Shadowform requires it.

**Then press the first one that is ready**, top to bottom:

1. **Mind Blast**
2. **Shadow Word: Pain**: keep it on the target, until the last 10 seconds of the fight
3. **Inner Focus**, then straight away **Devouring Plague**; no global cooldown, so press it alongside the others
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
- **Shadow Word: Death** (9 casts, 9%) and then **Devouring Plague** (7 casts, 11%) each time they are ready: **Shadow Word: Death** is instant on an 18-second cooldown; **Devouring Plague** lasts 24 seconds on a 24-second cooldown, so it is up all fight, and heals you for the damage it deals.
- **Mind Flay** fills every gap and is 40% of your damage (38 casts): 390 damage over 3 seconds for 205 mana (102 in **Shadowform**), each tick 20% stronger than the last with **Improved Mind Flay**, and **Darkness** adds 10% to everything.
- Mana is not your problem in a full raid: the simulator's priest never runs dry with one mana potion and two Demonic Runes a fight.

**Caveats**

- **Shadow Word: Death** hits you for 30% of your maximum health every time the target survives it (the 2026-11-02 patch tripled the backlash), about 9 times in a 3-minute fight: nearly three health bars that your healers pay for. The damage numbers ignore that. **Devouring Plague** heals a little of it back.
- **Mind Blast** causes a lot of threat (its tooltip says so) and leads the list. In the first seconds of a fight or after a tank swap, hold it until the tank is ahead.
- When you must move, **Mind Flay** and **Mind Blast** stop: use the instants, **Shadow Word: Death**, **Devouring Plague** and **Shadow Word: Pain** if it fell off. **Shadow Weaving** drops after 15 seconds without a Shadow spell.
- A 6-minute fight: the simulator's DPS falls from 788 at 3 minutes to 483 at 6 as the mana runs out.

**When to change it**

- If your healers struggle, save **Shadow Word: Death** for the last 20% of the boss's health: fewer casts, and on a kill no backlash for them to heal. You give up a few percent of damage.
- With adds up, keep **Shadow Word: Pain** on the ones that live longest and **Devouring Plague** on one that dies first: **Devouring Contagion** makes the plague jump to two nearby enemies when its target dies. The simulator fights one target.
- **Vampiric Embrace** has no line because the simulator counts only damage: on the boss, for 30 seconds your party heals for 20% of your Shadow damage, for 40 mana and one global cooldown.
- Out of mana in a long fight: **Dark Sacrifice** (an Undead racial spell, so only Undead priests have it) turns 1,600 of your health over 15 seconds into 1,600 mana plus your Spirit, once every 10 minutes; the full list holds it below **Mind Flay**, so it only fires when you cannot afford a **Mind Flay**.

## Talents

| Tree | Points | Talents (ranks) |
|---|---|---|
| Discipline | 16 | Twin Disciplines 5, Mental Strength 5, Inner Focus 1, Martyrdom 2, Silent Resolve 3 |
| Shadow | 35 | Shadow Focus 5, Improved Mind Blast 5, Improved Shadow Word: Pain 2, Mind Flay 1, Improved Mind Flay 2, Vampiric Embrace 1 (needed for Shadowform), Shadow Weaving 3, Devouring Contagion 2, Early Demise 2, Darkness 5, Shadowform 1, Silence 1, Spirit Tap 5 (tier point: needed to reach Devouring Contagion) |

A talent marked as a tier point measures nothing in the simulator's raid fight; the build holds it for the tier it opens (or the talent it is needed for).

## The numbers

**How this pick was checked:** a full search on 2026-11-03 (the talent search that found this build).

| Setting | DPS |
|---|---|
| Full raid, 3-minute fight (every raid buff and debuff: what this page ranks on) | 774 |

**By gear tier** (this build in the best set each tier allows, full raid, 5,000 fights; [every spec](../../_reference/dps-rankings.md)):

| Gear | Full raid DPS | In |
|---|---|---|
| Quests and dungeons | 716 | its own set |
| Pre-BiS | 767 | its own set |
| Raid BiS | 782 | its own set |

*Each tier's number is this build in its own tier set, in a lower tier's set, or in the standard set when every item of it is allowed in the tier, whichever is best. The tier sets were chosen for the builds and rotations of before 2026-11-20 and are being made again for this build.*

**The gear** (each tier's own set; average item level: Quests and dungeons 60.1; Pre-BiS 61.1; Raid BiS 62.6; each item opens its Wowhead page, with where it drops and its enchant):

| Slot | Quests and dungeons | Pre-BiS | Raid BiS |
|---|---|---|---|
| Head | [Crimson Felt Hat](https://www.wowhead.com/forever/item=18727) · *Magistrate Barthilas, Stratholme*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) | [Spellweaver's Turban](https://www.wowhead.com/forever/item=22267) · *General Drakkisath, Blackrock Spire*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) | [Spellweaver's Turban](https://www.wowhead.com/forever/item=22267) · *General Drakkisath, Blackrock Spire*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) |
| Neck | [Nacreous Shell Necklace](https://www.wowhead.com/forever/item=22403) · *Cannon Master Willey, Stratholme* | [Nacreous Shell Necklace](https://www.wowhead.com/forever/item=22403) · *Cannon Master Willey, Stratholme* | [Choker of the Fire Lord](https://www.wowhead.com/forever/item=18814) · *Ragnaros, Molten Core* |
| Shoulders | [Shroud of the Nathrezim](https://www.wowhead.com/forever/item=18720) · *Balnazzar, Stratholme* | [Mantle of the Timbermaw](https://www.wowhead.com/forever/item=19050) · *Tailoring* | [Mantle of the Timbermaw](https://www.wowhead.com/forever/item=19050) · *Tailoring* |
| Back | [Spritecaster Cape](https://www.wowhead.com/forever/item=11623) · *Houndmaster Grebmar, Blackrock Depths* | [Arcanoweave Cloak](https://www.wowhead.com/forever/item=272411) · *sold by Pix Xizzix* | [Arcanoweave Cloak](https://www.wowhead.com/forever/item=272411) · *sold by Pix Xizzix* |
| Chest | [Robe of Everlasting Night](https://www.wowhead.com/forever/item=18385) · *Immol'thar, Dire Maul*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) | [Robe of Winter Night](https://www.wowhead.com/forever/item=14136) · *Tailoring*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) | [Robe of Winter Night](https://www.wowhead.com/forever/item=14136) · *Tailoring*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) |
| Wrist | [Sublime Wristguards](https://www.wowhead.com/forever/item=18497) · *Guard Mol'dar, Dire Maul*<br>+ [Enchant Bracer - Greater Intellect](https://www.wowhead.com/forever/spell=13825) | [Netherpearl Cuffs](https://www.wowhead.com/forever/item=254067) · *Tailoring*<br>+ [Enchant Bracer - Greater Intellect](https://www.wowhead.com/forever/spell=13825) | [Netherpearl Cuffs](https://www.wowhead.com/forever/item=254067) · *Tailoring*<br>+ [Enchant Bracer - Greater Intellect](https://www.wowhead.com/forever/spell=13825) |
| Hands | [Hands of Power](https://www.wowhead.com/forever/item=13253) · *Quartermaster Zigris, Blackrock Spire* | [Gloves of Spell Mastery](https://www.wowhead.com/forever/item=14146) · *Tailoring* | [Gloves of Spell Mastery](https://www.wowhead.com/forever/item=14146) · *Tailoring* |
| Waist | [Highlander's Cloth Girdle](https://www.wowhead.com/forever/item=20047) · *sold by Samuel Hawke* | [Belt of the Archmage](https://www.wowhead.com/forever/item=18405) · *Tailoring* | [Belt of the Archmage](https://www.wowhead.com/forever/item=18405) · *Tailoring* |
| Legs | [Skyshroud Leggings](https://www.wowhead.com/forever/item=13170) · *Highlord Omokk, Blackrock Spire*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) | [Leggings of Torment](https://www.wowhead.com/forever/item=22342) · *Lord Valthalak, Blackrock Spire*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) | [Flarecore Leggings](https://www.wowhead.com/forever/item=19165) · *Tailoring*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) |
| Feet | [Omnicast Boots](https://www.wowhead.com/forever/item=11822) · *Golem Lord Argelmach, Blackrock Depths*<br>+ [Enchant Boots - Minor Speed](https://www.wowhead.com/forever/spell=13889) | [Omnicast Boots](https://www.wowhead.com/forever/item=11822) · *Golem Lord Argelmach, Blackrock Depths*<br>+ [Enchant Boots - Minor Speed](https://www.wowhead.com/forever/spell=13889) | [Omnicast Boots](https://www.wowhead.com/forever/item=11822) · *Golem Lord Argelmach, Blackrock Depths*<br>+ [Enchant Boots - Minor Speed](https://www.wowhead.com/forever/spell=13889) |
| Finger | [Songstone of Ironforge](https://www.wowhead.com/forever/item=12543) · *quest: The Princess's Surprise* | [Warden's Signet of Brilliance](https://www.wowhead.com/forever/item=275982) | [Ring of Spell Power](https://www.wowhead.com/forever/item=19147) · *Lucifron, Molten Core* |
| Finger | [Eye of Orgrimmar](https://www.wowhead.com/forever/item=12545) · *quest: The Princess Saved?* | [Elemental Focus Band](https://www.wowhead.com/forever/item=20682) · *Prince Skaldrenox, Silithus* | [Warden's Signet of Brilliance](https://www.wowhead.com/forever/item=275982) |
| Trinket | [Eye of the Beast](https://www.wowhead.com/forever/item=13968) · *quest: For The Horde!* | [Eye of the Beast](https://www.wowhead.com/forever/item=13968) · *quest: For The Horde!* | [Talisman of Ephemeral Power](https://www.wowhead.com/forever/item=18820) · *Magmadar, Molten Core* |
| Trinket | [Smolderweb's Eye](https://www.wowhead.com/forever/item=13213) · *Mother Smolderweb, Blackrock Spire* | [Weakness Analyzer](https://www.wowhead.com/forever/item=272438) · *sold by Pix Xizzix* | [Weakness Analyzer](https://www.wowhead.com/forever/item=272438) · *sold by Pix Xizzix* |
| Main hand | [Scepter of the Unholy](https://www.wowhead.com/forever/item=13349) · *Baron Rivendare, Stratholme*<br>+ [Enchant Weapon - Spell Power](https://www.wowhead.com/forever/spell=22747) | [Sageclaw](https://www.wowhead.com/forever/item=20070) · *sold by Samuel Hawke*<br>+ [Enchant Weapon - Spell Power](https://www.wowhead.com/forever/spell=22747) | [Sageclaw](https://www.wowhead.com/forever/item=20070) · *sold by Samuel Hawke*<br>+ [Enchant Weapon - Spell Power](https://www.wowhead.com/forever/spell=22747) |
| Off hand | [Spirit of Aquementas](https://www.wowhead.com/forever/item=11904) · *quest: It's Dangerous to Go Alone* | [Obsidian Bauble](https://www.wowhead.com/forever/item=18316) | [Obsidian Bauble](https://www.wowhead.com/forever/item=18316) |
| Ranged/relic | [Skul's Ghastly Touch](https://www.wowhead.com/forever/item=13396) · *Skul, Stratholme* | [Skul's Ghastly Touch](https://www.wowhead.com/forever/item=13396) · *Skul, Stratholme* | [Skul's Ghastly Touch](https://www.wowhead.com/forever/item=13396) · *Skul, Stratholme* |

**Open in the simulator** (the community's Forever simulator on the web, loaded with the gear, enchants, talents, rotation, consumables and buffs we simulate): Quests and dungeons: [full raid](https://wowsims.com/forever/priest/dps/#eJzEk81LFV8Yx+9zztyZ5z5X5TI/fjgeWow3iJsxcmbMMDd3dCVtkkCIKHKuc3VupHNxLmQ7LRcRpHIXgWIkURhBL0tp1xvcNmUQbdpIEbasCN1VzKjQPyB9OBzO83w453s2Dx1AyIEBJhRgGAKowjTANYAVgPsAelNiWWx7QPzkiLm0GCcNV+tgfMmSglcfAym4UgfiuHmGNHw3D8bnFtLw2QIYH1uI46sxUvDtMpCKP0bjWyo+OmvMa8Txt0ccZ0rEcWGcON4aIxXvBUbjP+I4fY44vg/yR3KNSuHNHMit0uCNO3Ad2GylDmyrtARss+8BaKvL8GRgrrIBs5V+TD4MLjxl7VJ2J8uWXZYjHSuuHCltp8vush2n224wWGfZT2yWkU6aSBPH71N5jdLELTvSsyIjNEoXMvhiSFcE603pUnTSQb2dmvNZyjixRJwbolxHC6o6O5ESKinEbCn2lN4mWp3/dx+/HREJJLWg4vpN0JvETqXgy+2Teqh7XvXi+bBaMx3pHLNsacmeXnMk8CbGyr4ZTpqe75d9s3TZrAVlczKsebVKOGFGZW9yJDALUblsRoHnh5csvxpZe97a8Z0XonDi8G7gTnyzyF6BOF/F7ToY/CtrwDfmz/BUwlH3OSiCUSr/i2XiRmp61G1bWox5XWwfTfhQdDaYoZjFjjWW+ifU3L3TvnLo4b7lHE/2U3fdvt2GOxxP4CIkRWqj2MFxrbX/r0GV0AMuDMAgnIYAqjAFU+zPAMDhk9A=); Pre-BiS: [full raid](https://wowsims.com/forever/priest/dps/#eJzEk89r1FoUx+fcZJIzZ9q+kMej6eUh6QgyVlJuUkdqN5N2VdxYhIILwabN1IzoZGgGrLuqXYjoVIoIrQV/IChCqysprqSKjC5kFuLGTVGqIi4UoV0IIklb8B8ofhaHe86He793c+h/BA0MMCEPIxBAFaYALgLcArgPoLcklsW2F/iGhKileUQq/lwEYy1LMl54CCTjl2txvdHUSMHlivGhjVT88fQf410bSbhSIRnXZoBUfLGUXFNw6Zgxo5KM9a8ayfjqNpCEV0+TjI+bGqn4cQGMxr8k4+WZ2LwJcvu0Rjn/ug5ifXToyh24BGy6PAtsfXQe2Kf+B6DeW4BHg/XyKkyXBzD5NrjwhO0SotAjCo5tC9uyCqKn4AhhO8LusR2nYDcYNFn2PZtmpJPK0yTh98mcSmmSLDvSszzDVUrnM/hsWJc560vpgnfTbr2TWnNZyjixRKwPk9bVhorODqW4QjIxW/BtpXfwdue/rcdvRkQcSckr2LwOegvf7GR8vnFYD3XPq546HlZrpiOcA5YtLNHbZ44FXuVEyTfDCdPz/ZJvjp41a0HJnAhrXq0cVsyo5E2MBWY+KpXMKPD88IzlVyNr21ubvvtkFFb2bgVuxrfy7HmI8xXcmAVD+swa8I3556RUwn53BWTOKJX7xTLxIDU17nbMz8W8LHaOJ7wtOqvMkM1i1zJL/RVq7vZpR9mzuGM5B5N65K7bvzVwR+IlnIOkSa0WuyRcbh/4Y1cF9IILgzAERyGAKkzCJPs9AFmLlpo=); Raid BiS: [full raid](https://wowsims.com/forever/priest/dps/#eJzEk8Fr1FoUxufcZJIzZ9q+kMej6eXxSOeBjJWUm9SR2s2kXRU3FqHgQrBpMzUjMhmaAeuuyixEdArVCq0FRQRFqLiS4kqqixFBZiFuRChKVcSFIrSCUCRpC/4DxW9xOOf8OPe7m4/+RdDAABPyMAYBVGEG4CLALYB7AHpbQllM+4H/kBC1NK+Rij+XwVjPkoxbc0Ayfr4W1xstjRRcqRjvO0jF70/+Mt50kISrFZJxfRZIxbfzyZmCD04YsyrJ+GI+Pmx80UjG+tW4f9TSSMUPS2A0/yYZL88CSfgqyB3QmuX8ywaIjfGRK7fhErB6eQ7YxvgisI+D90G9uwQPhxvlNaiXhzD5N7jwmP0nRKFPFBxhC8eyCqKv4AhhO8Lusx2nYDcZtFj2Hasz0knlaZLw23ROpTRJlh3pWZ7hKqXzGXw6qsucDaR0wXvpf72b2nNZyjgxRGyMktbTgYrOjqS4QjIxW/BdpHfxTuefncdvRkQcSckr2LoOehvfnmR8tnlUD3XPq545GVZrpiOcQ5YtLNE/YE4EXuVUyTfDKdPz/ZJvjp8za0HJnAprXq0cVsyo5E1NBGY+KpXMKPD88KzlVyNrl1vbvPd0FFb27xhu27fz7AWI/RXcnAND+sSa8JX556VUooPuKsicUSq3xTLxIjUz6XYtLsR6XuyeTPS66KwxQzaLPSss9UdUc3e7PdW+5T3zOZzUY3fcwZ2FOxancAGSIbVW7JFwpXPot7AK6AcXhmEEjkMAVZiGafZrAPxJlwk=).

**Points that do nothing for this spec:** **Spirit Tap** (5) only counts toward the points the tree needs before **Devouring Contagion**; **Vampiric Embrace** (1) is needed for **Shadowform**.

**Taken for raid utility:** **Martyrdom** (2) changes nothing the raid simulator measures: it is there for its protection from pushback; **Silence** (1) is not in the rotation: it is there for its interrupt, which the raid simulator does not measure; **Silent Resolve** (3) changes nothing the raid simulator measures: it is there for its threat cut.

## Other builds of this spec

- [Shadow (optimized)](../research/raid/builds/opt-shadow-dps-raid-dps.md) (17/3/31) — [open the talent tree](https://talentsforever.com/priest/60/00520520003-3-50152001231302051-12)

---
*Generated by `_reference/data/render_modes.py` on 2026-11-22 from this project's builds and simulations of the WoW: Forever beta (talent data: client build 1.60.1.70753; spell numbers: client 1.60.1.70938; raid numbers: the official wowsims/forever simulator at 2e6e77d (client 1.60.1.70938)). Simulations, not in-game measurements. Spell ranks: trainer ranks only. The class books' ranks (Grimoire of Shadow Bolt X, Tome of Frostbolt XI and the like) are not in Forever on the evidence there is (2026-11-20): in Classic every one drops in the Ruins of Ahn'Qiraj, which Forever's roadmap does not have; Wowhead's Forever pages list no source for them; the simulator's own authors leave them off by default. Checked again when the raids of 2026-12-09 open. Do not hand-edit.*

*The live client is 1.60.1.71037 (2026-11-20); these pages are on 1.60.1.70938; an update follows. Vampiric Embrace heals the party for 10% of your Shadow damage since client 1.60.1.71037 (20% before; you still get 20%); the raid numbers here predate it.*

