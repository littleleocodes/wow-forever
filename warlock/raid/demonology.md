# Demonology Warlock — Raid (group)

[Warlock](../README.md) > [Raid (group)](README.md) > Demonology

**✅ Recommended** for raid (the best warlock spec here, or within 3% of it).

**[Demonology — Raid](../research/raid/builds/demonology-ml-raid.md)** (2/31/18) — [open the talent tree](https://talentsforever.com/warlock/60/011-0025003031220301351-0550005003-12)

> 🔬 Derived build: found by this project's machine-learning search over every legal build of the spec in the community's raid simulator (phase-1 BiS gear, then raced against the spec's builds). A model of the beta, to check at launch.

## How to play

**Setup, before the pull:** **Summon Succubus** and keep it out all fight. Keep **Demon Armor** on you.

**Then press the first one that is ready**, top to bottom:

1. **Curse of the Elements**: keep it on the target
2. **Life Tap** when your mana is below 5%
3. **Bane of Agony**: keep it on the target
4. **Corruption**: keep it on the target, until the last 10 seconds of the fight
5. **Immolate**: keep it on the target, until the last 20 seconds of the fight
6. **Shadow Bolt** (rank 9)

**Shadow Bolt** is your filler: cast it whenever nothing above is ready.

**Advanced: your cooldowns and extras.** Once the list above feels easy, add these:

- **Searing Pain**: in the last 3.5 seconds of the fight, when there is no time left for another **Shadow Bolt**

*The simulator's full rotation for this build, with every condition: [research rotation page](../research/raid/rotation.md).*

## Why this rotation

Before the pull: summon the Imp, use **Demonic Sacrifice** (+15% Shadow damage for 2 hours, worth about 10% of your damage in the simulator), then summon the Succubus and turn on **Soul Link**. **Demonic Pact** keeps the sacrifice while she fights. In the fight keep **Curse of the Elements** and your dots up and cast **Shadow Bolt**.

**Why it works**

- Put your buffs, wizard oil and Spellstone (**Create Spellstone**) on first: in this project's model a demon copies its share of your spell damage when it is summoned. Then **Summon Imp**, **Demonic Sacrifice**, **Summon Succubus** (6 seconds with **Master Summoner**) and **Soul Link**. **Demonic Pact** keeps the sacrifice while a different demon is out, but summoning the Imp again cancels it.
- The Succubus earns her place: while she is out, **Master Demonologist** gives you and her 10% more Shadow damage, **Soul Link** 3% more damage and **Demonic Knowledge** 60 more spell damage at level 60. She takes 17% of your spell damage as attack power and 10% as spell damage, and her attacks and **Lash of Pain** add to your total.
- **Curse of the Elements** goes up first: 10% more damage from every magic school for 5 minutes, and as a Curse it sits beside your **Bane of Agony**. **Life Tap** waits until you are below 5% mana: every tap is a global cooldown with no damage, and the simulator measured tapping at 5% better than at 10%.
- **Bane of Agony** grows over its 24 seconds, so recast it only once it has run out. **Corruption** (a 1.6-second cast with this build's single point of **Improved Corruption**) goes back up when less time is left on it than its cast, but not in the last 10 seconds.
- **Immolate** is Fire, so the sacrifice and your other Shadow bonuses do not reach it, and it only just pays: the simulator measured this spec better without it when it was recast to the very end, and better with it when you stop 20 seconds before the end. Start it when less than its 1.5-second cast is left on the old one.
- **Shadow Bolt** is the filler because every bonus you stacked is Shadow: the sacrificed Imp, **Master Demonologist** and **Improved Shadow Bolt**'s 20% after your own crits. **Decimation** adds 6% to it once the boss is below 35% health.

**Caveats**

- **Searing Pain** has no cooldown: the rotation casts it only in the last 3.5 seconds, when its 1.5-second cast lands before the boss dies and a **Shadow Bolt** might not. So **Demonic Brand** and the **Soul Fire** half of **Decimation** do nothing here: they are points on the way to deeper talents, and the simulator found **Soul Fire** a loss wherever it tried it.
- If the Succubus dies, summon her again unless the boss is about to die and turn **Soul Link** back on: without a demon you lose **Master Demonologist**, **Soul Link**, **Demonic Knowledge** and her own damage. Never summon the Imp during the fight: that cancels your sacrifice even with **Demonic Pact**.
- Forever lets the Spellstone stack with the oil, and the simulator measured about 3% more damage from it.
- On the move, **Bane of Agony**, **Curse of the Elements** and **Life Tap** are instant; **Corruption** keeps a 1.6-second cast in this build, so put it back when you stand still.

**When to change it**

- In the last 20 seconds start no new **Immolate**, and in the last 10 no **Corruption**: cast **Shadow Bolt**, then **Searing Pain** in the last 3.5 seconds.
- A boss needs only one **Curse of the Elements** (in Classic two never stacked): if another warlock keeps it up, take the curse your raid gives you, such as **Curse of Recklessness** for the physical fighters.

## Talents

| Tree | Points | Talents (ranks) |
|---|---|---|
| Affliction | 2 | Suppression 1, Improved Corruption 1 |
| Demonology | 31 | Demonic Embrace 2, Unholy Power 5, Fel Vitality 3, Improved Sayaad 3, Demonic Sacrifice 1, Master Summoner 2, Decimation 2, Demonic Brand 3, Soul Link 1, Demonic Knowledge 3, Master Demonologist 5, Demonic Pact 1 |
| Destruction | 18 | Improved Shadow Bolt 5, Bane 5, Ruin 5, Agonizing Flames 3 |

## The numbers

| Setting | DPS |
|---|---|
| Full raid, 3-minute fight (every raid buff and debuff: what this page ranks on) | 857 |

**By gear tier** (the spec's best talents for each tier and setting in its own gear, found by this project's machine-learning search in the community simulator, wowsims/forever 16e8542 (client 70790); [every spec](../../_reference/dps-rankings.md)):

| Gear | Full raid DPS | Best talents |
|---|---|---|
| Pre-BiS | 820 | this build |
| Phase 1 BiS | 856 | this build |

*Each row is in that tier's own gear set; the DPS at the top of the page is this build in the standard set, so the two do not match.*

**The gear** (average item level: Pre-BiS 60.8; Phase 1 BiS 62.8; each item opens its Wowhead page, with where it drops and its enchant):

| Slot | Pre-BiS | Phase 1 BiS |
|---|---|---|
| Head | [Felcloth Hood](https://www.wowhead.com/forever/item=14111) · *Tailoring*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) | [Felcloth Hood](https://www.wowhead.com/forever/item=14111) · *Tailoring*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) |
| Neck | [Orb of the Darkmoon](https://www.wowhead.com/forever/item=19426) · *quest: 1200 Tickets - Orb of the Darkmoon* | [Choker of the Fire Lord](https://www.wowhead.com/forever/item=18814) · *Ragnaros, Molten Core* |
| Shoulders | [Mantle of the Timbermaw](https://www.wowhead.com/forever/item=19050) · *Tailoring* | [Mantle of the Timbermaw](https://www.wowhead.com/forever/item=19050) · *Tailoring* |
| Back | [Arcanoweave Cloak](https://www.wowhead.com/forever/item=272411) · *sold by Pix Xizzix* | [Arcanoweave Cloak](https://www.wowhead.com/forever/item=272411) · *sold by Pix Xizzix* |
| Chest | [Robe of the Void](https://www.wowhead.com/forever/item=14153) · *Tailoring*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) | [Robe of the Void](https://www.wowhead.com/forever/item=14153) · *Tailoring*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) |
| Wrist | [Rockfury Bracers](https://www.wowhead.com/forever/item=21186) · *quest: Stalwart's Battlegear*<br>+ [Enchant Bracer - Greater Intellect](https://www.wowhead.com/forever/spell=13825) | [Rockfury Bracers](https://www.wowhead.com/forever/item=21186) · *quest: Stalwart's Battlegear*<br>+ [Enchant Bracer - Greater Intellect](https://www.wowhead.com/forever/spell=13825) |
| Hands | [Gloves of Spell Mastery](https://www.wowhead.com/forever/item=14146) · *Tailoring* | [Gloves of Spell Mastery](https://www.wowhead.com/forever/item=14146) · *Tailoring* |
| Waist | [Belt of the Archmage](https://www.wowhead.com/forever/item=18405) · *Tailoring* | [Belt of the Archmage](https://www.wowhead.com/forever/item=18405) · *Tailoring* |
| Legs | [Magister's Leggings](https://www.wowhead.com/forever/item=16687) · *Baron Rivendare, Stratholme*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) | [Flarecore Leggings](https://www.wowhead.com/forever/item=19165) · *Tailoring*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) |
| Feet | [Sorcerer's Boots](https://www.wowhead.com/forever/item=22064) · *quest: Anthion's Parting Words*<br>+ [Enchant Boots - Minor Speed](https://www.wowhead.com/forever/spell=13889) | [Sorcerer's Boots](https://www.wowhead.com/forever/item=22064) · *quest: Anthion's Parting Words*<br>+ [Enchant Boots - Minor Speed](https://www.wowhead.com/forever/spell=13889) |
| Finger | [Warden's Signet of Brilliance](https://www.wowhead.com/forever/item=275982) | [Ring of Spell Power](https://www.wowhead.com/forever/item=19147) · *Lucifron, Molten Core* |
| Finger | [Elemental Focus Band](https://www.wowhead.com/forever/item=20682) · *Prince Skaldrenox, Silithus* | [Ring of Spell Power](https://www.wowhead.com/forever/item=19147) · *Lucifron, Molten Core* |
| Trinket | [Weakness Analyzer](https://www.wowhead.com/forever/item=272438) · *sold by Pix Xizzix* | [Weakness Analyzer](https://www.wowhead.com/forever/item=272438) · *sold by Pix Xizzix* |
| Trinket | [Frozen Heart of the Mountain](https://www.wowhead.com/forever/item=249469) · *Enchanting* | [Talisman of Ephemeral Power](https://www.wowhead.com/forever/item=18820) · *Magmadar, Molten Core* |
| Main hand | [Sageblade](https://www.wowhead.com/forever/item=22383) · *Blacksmithing*<br>+ [Enchant Weapon - Spell Power](https://www.wowhead.com/forever/spell=22747) | [Sageblade](https://www.wowhead.com/forever/item=22383) · *Blacksmithing*<br>+ [Enchant Weapon - Spell Power](https://www.wowhead.com/forever/spell=22747) |
| Off hand | [Mordresh's Lifeless Skull](https://www.wowhead.com/forever/item=10770) · *Mordresh Fire Eye, Razorfen Downs* | [Mordresh's Lifeless Skull](https://www.wowhead.com/forever/item=10770) · *Mordresh Fire Eye, Razorfen Downs* |
| Ranged/relic | [Brilliant Wand](https://www.wowhead.com/forever/item=249385) · *Enchanting* | [Brilliant Wand](https://www.wowhead.com/forever/item=249385) · *Enchanting* |

**Open in the simulator** (the community's Forever simulator on the web, loaded with the gear, enchants, talents, rotation, consumables and buffs we simulate): Pre-BiS: [full raid](https://wowsims.com/forever/warlock/dps/#eJzElU9II1ccx/N7M8m8/GzN+EpxHFuYBpQ0MPJmwqjxktGTlB6k9FDwUBMTTYLNhCQHvdlqaSmtgi0UU8H+UVpLrVJKkZ5aQYg9FE+9iFQs0mVZ2GUP3nZZZjJhl3UPewl+D2++8/2937zPvBl4+AoFGRTQIAZTkIcyLAJ8DPA1wA8A7AWvStzqMKi/hqkgh9UahuhmSbnsQJFefAko0ttfuONXJzKG6HFJ+a8TJXq4DcppJwr0sIQivVwFlOjeB+C2SXT/J1BWJRTpyh0ZRfrXN27/byeuf7ARQYne/RmUxkso0LW3UaQ7G5GoKTcKsb9XgF9lJj77Fj4BslxYA3KVqUPw/9HNbfgRpO83YH98pbAP3xXPYbkwRj18sOF3EuWGoXNuWpwneMIwTZ7gRsIydG5ZnHM3bhDhhHRckD2Jvar2Ylc0gi/+Aogi/eOjCUbkoBryvalyjLF+7IpHaIiRNwKqhEEUDKvqRSIjGT8asvpUEYmisIRqPGfPIO9TgyjIVxkmqmQk0KRpPrfVlhiwPJqlT4EtAZtJl+fedco1zeTmoM6Tujk8ok3n06XZXFZzKlo6m81ltcyCVsvntIpTS9cKTkmr5tKV6bwWq+ZyWjb3nlNy5pzZBb2SLmT11iS9OWmgWHVKr6s9KMc7qeC9XwhFJJaHSncmWVTVsDv+MhWZVHSjPydVWie+a17Y1tOkBte52RbSEeRsAHvi3VRktOhu1b9HoIbrxLfXvgOvqn7pZjHPHmOeXcc0fcyzI2AfXsM0dD7UFszeFkfrHzWtPpdDXv4cWOUZu5VsCwZ116S7999k6PvTI1CEW6QB94j5vhDwlLTrBJFiiAoasSH6kITdOLA4Y/fU110dp16b8fRPyjwniqil4gckcCOq2S3XVvXvtm2dpDe+tWWP+oE95Z4g6+DdBM5TcYEedI89cdBwGAYbxmEC3oE8lGEe5smjAQBZnFG5); Phase 1 BiS: [full raid](https://wowsims.com/forever/warlock/dps/#eJzElUFII1cYx/O9mWRePlsdXymOYwvTgJIGRt5MGDVeMnqS0oOUHgoeamKiSbCZkOSgN4spLaVV0HowFSyt0lpqK6UU6akVhEiheOpFQqVFWnrZZQ8eZZnJZHdZ97CX4Hf45j//7/vm/ebNwMNXKMiggAZRmIUclGAF4COALwC+AWAveFXiVsdA/SlMBTmsVjFEd4vKVReK9GYDUKT/f+bmz89lDNGzovJPN0r0ZB+Ui24U6EkRRXq1DijR5ha4YxI9+g6UdQlF+vsWPMo/n8so0tqm23nve1AaL6FAN95GkR7s9ERMuZGP/rEG/Do9/emX8DGQWn4DyHW6DsF/J3b34VuQvt6Bo6m1/BF8VbiEWn6Sevhgwy8kwg1D59y0OI/zuGGaPM6NuGXo3LI4567dIMI56fqb/CCxV9UB7I304Is/AqJIf/1wmhE5qIZ8baoco2wIe2M9NMTIGwFVwiAKhlXxLJGRtG+NWoOqiERRWFw1nnNmhA+qQRTk6zQTVTIeaNG0ntseiw9bHs3qJ8BWgc2nSovvOqWqZnJzROcJ3Rwb1+ZyqeJCNqM5ZS2VyWQzWnpZq+ayWtmppqp5p6hVsqnyXE6LVrJZLZN9zyk6i87Csl5O5TN6u0lvNQ0XKk7xdbUf5Vg3Fbz3C6GIxPJQ6cEMi6ga9sVepiKTCq7124xK68RXrQvbe5rU4Do3O0I6jpwNY3+sj4qMFtyt+usU1HCd+PLWd+AV1S/dLWbzMWbzNqbpYzZPgX1wC9PQ+WhHMAfaHO1/1LQGXQ65tgms/IzdSnQEg7pr0sMHbzL09cUpKMJ/pAH3ifm+EPAiYdcJIsUQFTRiQ+SGhF07sDJv99e33ThLvjbvxZ9J85IoopaMHZPAnUTVbquOxtBhx9ZJePmtPXvCN+xZ9wTZBu8mcJmMCfS4b/KJg4bDGNgwBdPwDuSgBEuwRB4OAOLvUU0=).

## Other builds of this spec

- [Demonology — Demonic Pact](../research/raid/builds/demonology-pact-raid.md) (2/31/18, 852 DPS in a full raid) — [open the talent tree](https://talentsforever.com/warlock/60/101-0035003021220301351-0550005003-12)

---
*Generated by `_reference/data/render_modes.py` on 2026-11-10 from this project's builds and simulations of the WoW: Forever beta (talent and spell data: client build 1.60.1.70753; raid numbers: the official wowsims/forever simulator at 16e8542 (client 1.60.1.70790)). Simulations, not in-game measurements. Do not hand-edit.*

