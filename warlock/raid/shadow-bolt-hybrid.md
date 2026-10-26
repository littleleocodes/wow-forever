# Shadow Bolt hybrid Warlock — Raid (group)

[Warlock](../README.md) > [Raid (group)](README.md) > Shadow Bolt hybrid

*Shadow Bolt with Affliction's Malevolence and Destruction's Agonizing Flames, points in all three trees.* (a hybrid: Affliction/Destruction).

**[Shadow Bolt hybrid — Raid](../research/raid/builds/shadow-bolt-hybrid-open-raid.md)** (20/11/20) — [open the talent tree](https://talentsforever.com/warlock/60/25300020035-0050203001-0550105103-7)

> 🔬 Derived build: found by this project's open talent search (every legal build, no tree rule, in the community's raid simulator in a full raid, raced against the rotation's builds); it beat the hand-made build (DS/Ruin — Demonic Sacrifice + Ruin), which stays below as the alternative. A model of the beta, to check at launch.

**Other setups of this spec.** This build is the Shadow Bolt setup. The spec's best build for each other setup, in a full raid:

- Fire: [Shadow Bolt hybrid — Fire](../research/raid/builds/shadow-bolt-hybrid-fire-open-raid.md) (20/11/20, 700 DPS in a full raid) — [open the talent tree](https://talentsforever.com/warlock/60/25300020035-0050203001-0550205003-7)

## How to play

**Before the pull:** **Life Tap**.

**Talents with no line below:** **Demonic Sacrifice**: before the pull, summon your Imp and sacrifice it (+15% Shadow damage for 2 hours; summoning any demon cancels it).

**Then press the first one that is ready**, top to bottom:

1. **Curse of the Elements**: keep it on the target
2. **Life Tap** when your mana is below 5%
3. **Bane of Agony**: keep it on the target
4. **Corruption**: keep it on the target, until the last 10 seconds of the fight
5. **Immolate**: keep it on the target, until the last 20 seconds of the fight
6. **Shadow Bolt**

**Shadow Bolt** is your filler: cast it whenever nothing above is ready.

**Advanced: your cooldowns and extras.** Once the list above feels easy, add these:

- **Shadowburn**: in the last 1.5 seconds of the fight, when there is no time left for another **Shadow Bolt**
- **Searing Pain**: in the last 3.5 seconds of the fight, when there is no time left for another **Shadow Bolt**

*The simulator's full rotation for this build, with every condition: [research rotation page](../research/raid/rotation.md).*

## Why this rotation

The Shadow Bolt hybrid is the classic DS/Ruin warlock (**Demonic Sacrifice** plus **Ruin**): the Imp sacrificed for 15% more Shadow damage, Affliction's crit and hit talents, and Destruction's **Bane**, **Improved Shadow Bolt** and **Ruin**. You keep **Curse of the Elements** and three dots up and cast **Shadow Bolt** the rest of the time.

**Why it works**

- Before the pull: summon the Imp, use **Demonic Sacrifice** (+15% Shadow damage for 2 hours; summoning any demon ends it), then **Life Tap** once so you start full. This build has no **Amplify Curse**; the simulator measured about 11% less damage without the sacrifice.
- **Curse of the Elements** goes up first: one cast lasts 5 minutes and makes the boss take 10% more damage from every magic school (Curse of Shadow is gone in Forever). As a Curse it sits beside your **Bane of Agony**, and the simulator measured it 0.3% better at the top of the list.
- **Life Tap** waits until you are below 5% mana: every tap is a global cooldown with no damage, and the simulator measured tapping at 5% about 0.4% better than at 10%. **Improved Life Tap** adds 20% to each tap, and the list uses a mana potion below 75% mana and a Demonic Rune below 80%, never in the last 15 seconds.
- **Bane of Agony** grows over its 24 seconds, so recast it only once it has run out. **Corruption** (a 1.2-second cast with 2 points in **Improved Corruption**) goes back up when it drops, except in the last 10 seconds.
- Start a new **Immolate** when less time is left on the old one than its cast (1.5 seconds with the **Bane** talent), so it lands as the old one ends, but start none in the last 20 seconds: it would not run long enough to beat a **Shadow Bolt**. Both end-of-fight cut-offs measured small gains.
- **Shadow Bolt** is the filler: its crits trigger **Improved Shadow Bolt** (20% more Shadow damage from you for 12 seconds, your dots included), **Malevolence** makes them more frequent and **Ruin** doubles their bonus. **Pandemic** does the same for your dots' crits.

**Caveats**

- **Searing Pain** has no cooldown: the rotation casts it only in the last 3.5 seconds, and **Shadowburn** (instant) in the last 1.5, when a **Shadow Bolt** would not finish before the boss dies. Never use them as fillers.
- With the Imp sacrificed you play without a demon: any summon ends the buff, so if you die, summon the Imp and sacrifice it again before the next pull.
- Put a Spellstone (**Create Spellstone**) on your weapon on top of your wizard oil: Forever lets them stack, and the simulator measured about 3% more damage.
- On the move, use the instants: **Bane of Agony**, **Curse of the Elements**, **Shadowburn** and **Life Tap**.

**When to change it**

- In the last 20 seconds start no new **Immolate**, and in the last 10 no **Corruption**: cast **Shadow Bolt**, then **Searing Pain** in the last 3.5 seconds.
- A boss needs only one **Curse of the Elements** (in Classic two never stacked): if another warlock keeps it up, take the curse your raid gives you, such as **Curse of Recklessness** for the physical fighters.
- When healing is tight, each **Life Tap** costs health someone must heal: use your mana potion and Demonic Rune before you tap.

## The numbers

| Setting | DPS |
|---|---|
| Full raid, 3-minute fight (every raid buff and debuff: what this page ranks on) | 723 |

**By gear tier** (the spec's best talents for each tier and setting in its own gear, found by this project's machine-learning search in the community simulator, ElliotWood/Forever fork 2ce8265 (client 70291); [every spec](../../_reference/dps-rankings.md)):

| Gear | Full raid DPS | Best talents |
|---|---|---|
| Pre-BiS | 696 | this build |
| Phase 1 BiS | 739 | this build |

**The gear** (average item level: Pre-BiS 62.4; Phase 1 BiS 63.9; each item opens its Wowhead page, with where it drops and its enchant):

| Slot | Pre-BiS | Phase 1 BiS |
|---|---|---|
| Head | [Felcloth Hood](https://www.wowhead.com/forever/item=14111) · *Tailoring*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) | [Felcloth Hood](https://www.wowhead.com/forever/item=14111) · *Tailoring*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) |
| Neck | [Orb of the Darkmoon](https://www.wowhead.com/forever/item=19426) | [Choker of the Fire Lord](https://www.wowhead.com/forever/item=18814) · *Ragnaros, Molten Core* |
| Shoulders | [Mantle of the Timbermaw](https://www.wowhead.com/forever/item=19050) · *Tailoring* | [Mantle of the Timbermaw](https://www.wowhead.com/forever/item=19050) · *Tailoring* |
| Back | [Arcanoweave Cloak](https://www.wowhead.com/forever/item=272411) | [Arcanoweave Cloak](https://www.wowhead.com/forever/item=272411) |
| Chest | [Robe of the Void](https://www.wowhead.com/forever/item=14153) · *Tailoring*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) | [Robe of the Void](https://www.wowhead.com/forever/item=14153) · *Tailoring*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) |
| Wrist | [Rockfury Bracers](https://www.wowhead.com/forever/item=21186)<br>+ [Enchant Bracer - Greater Intellect](https://www.wowhead.com/forever/spell=13825) | [Rockfury Bracers](https://www.wowhead.com/forever/item=21186)<br>+ [Enchant Bracer - Greater Intellect](https://www.wowhead.com/forever/spell=13825) |
| Hands | [Gloves of Spell Mastery](https://www.wowhead.com/forever/item=14146) · *Tailoring* | [Gloves of Spell Mastery](https://www.wowhead.com/forever/item=14146) · *Tailoring* |
| Waist | [Belt of the Archmage](https://www.wowhead.com/forever/item=18405) · *Tailoring* | [Belt of the Archmage](https://www.wowhead.com/forever/item=18405) · *Tailoring* |
| Legs | [Ghostweave Pants](https://www.wowhead.com/forever/item=14144) · *Tailoring*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) | [Flarecore Leggings](https://www.wowhead.com/forever/item=19165) · *Tailoring*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) |
| Feet | [Sorcerer's Boots](https://www.wowhead.com/forever/item=22064)<br>+ [Enchant Boots - Minor Speed](https://www.wowhead.com/forever/spell=13889) | [Sorcerer's Boots](https://www.wowhead.com/forever/item=22064)<br>+ [Enchant Boots - Minor Speed](https://www.wowhead.com/forever/spell=13889) |
| Finger | [Signet Ring of the Bronze Dragonflight](https://www.wowhead.com/forever/item=21210) | [Ring of Spell Power](https://www.wowhead.com/forever/item=19147) · *Lucifron, Molten Core* |
| Finger | [Brilliant Watcher's Signet](https://www.wowhead.com/forever/item=275982) | [Ring of Spell Power](https://www.wowhead.com/forever/item=19147) · *Lucifron, Molten Core* |
| Trinket | [Weakness Analyzer](https://www.wowhead.com/forever/item=272438) | [Talisman of Ephemeral Power](https://www.wowhead.com/forever/item=18820) · *Magmadar, Molten Core* |
| Trinket | [Jewel of the Guard Captain](https://www.wowhead.com/forever/item=270225) | [Weakness Analyzer](https://www.wowhead.com/forever/item=272438) |
| Main hand | [Sageblade](https://www.wowhead.com/forever/item=22383) · *Blacksmithing*<br>+ [Enchant Weapon - Spell Power](https://www.wowhead.com/forever/spell=22747) | [Sageblade](https://www.wowhead.com/forever/item=22383) · *Blacksmithing*<br>+ [Enchant Weapon - Spell Power](https://www.wowhead.com/forever/spell=22747) |
| Off hand | [Therazane's Touch](https://www.wowhead.com/forever/item=19315) | [Therazane's Touch](https://www.wowhead.com/forever/item=19315) |
| Ranged/relic | [Brilliant Wand](https://www.wowhead.com/forever/item=249385) · *Enchanting* | [Brilliant Wand](https://www.wowhead.com/forever/item=249385) · *Enchanting* |

**Open in the simulator** (the community's Forever simulator on the web, loaded with the gear, enchants, talents, rotation, consumables and buffs we simulate): Pre-BiS: [full raid](https://wowsims.com/forever/warlock/dps/#eJzElU9oK1UUxnPu3GRuznu28+5TOh0V5gX6iIEJdyaMTbrJtKviqrgSCtqkSU2CJCGTRcVNxYIimqIRpbFQUYtW/FNcaHFjLRTSjXTlwlIslaKIYEHpUmQm01baLlykeBY3J+ebM/f3zblw8REGCqigQxxmoAR1WAB4BeA9gI8B+G1fJZ6aBu0LZJIS1ZoYYatV9fgWUnb0DiBlv73lre/uKRhhu1X15wGU2fYaqPsDKLHtKlJ2vAQYYVt+l8w2PgV1SUbKflzzGlu/K0jZV3ve+sa3Csrsj89B7d5Fyv5823tgfWUwZindcvz7FojT/NTr78OrQBbLbwI5zXcg/Mv46hp8AvJHK7Ax2SpvwAeVQ1gsT9y+MOfAN+SeZaeEEJYQKdsQwhaWSAlhGsK2hSlsU6S6RNojt47IOsO7yLQIUnbSgpiMYZQM28UHUdbCKLH16VgUZQwbZtJ2+aPaw3gnNogPfAmIlG29PMWJEva7vdzSBMb5fbyTGGQRTp4Iaf77TNv1S5STfFAatUc0ikRVeRv407n6c8/U6k3dEtbjhikMYY3ps6Vc9dliQa819FyhUCzo+ef1ZqmoN2rNXLNcq+puMdeYLelxt1jU3bzRyJULxplo9MRkxa1VH9PM/wiVFiOeZ+U0z6lGxkI9uz3w87ak7dv9ug3XyalAfuk14C9cMiYyhjXaV2PDqCQGmOR/1ghSJPZIMDSO2vlQeUzTcSjxEKNcrnjyd9Ma65Ag6/3wlctj8GjTfaUdQ8GTOJwYYpSzigf30w5o0Q4J0isTEq4WSNfjjd4w3sEF3sFVPCvAO9gBXrlE551hs690vWn+1b5+r0z/91IW23B+ivZ3QJV+JV04IdaLUsiPjNMhDCNIdeJA7G8S9YqhhTlnuLPsxW723pwfP2StQ6JSPZvYJKH/JZrOWXajcf+zG9sn469PfuiMBwVnxru8lsH/EzrMJiS2OTTxrztOQBocmIQpeApKUId5mCf/DADWZGsg); Phase 1 BiS: [full raid](https://wowsims.com/forever/warlock/dps/#eJzElUFoM0UUx/NmN9nJ+z7b/eZTul0VtoGWGNgwu2Ft0ku2PRVPxZNQ0CZNahIkCdkIFS8VA4poC40VGgsVtWhFJXjQ4kkLhRRBevJSgkUpihcLSo9FdrNNpe3BQ4rv8Pbt+zM7v/++gcEnKMiggAZRWIACVGEF4E2ADwA+BWD3PZW4ahLUNlJBDqsvY4hul5XTeyjSi3VAkf7xrpvfP5IxRA/Lyq9DKNH9HVCOh1Cg+2UU6ekaoES7G+Auk2j7c1DWJBTpDxvQz42mm78+klGif34JSuchivSv99zm7tZwxJQ7xeiPq8DPs3PvfAhvAWkU14GcZ1sQ/G16ewc+A+mTLWjPrhbb8FHpBBrFmftX7mz4loyZVoJzbnKesHTOLW7yBOeGzi2LG9wyeKJDhCNy7xeyS/EhUjWEIj1bhYiEQRR0y8FHUVKDKNDd+UgYJQzqRtxy2JPq4/ggMoyPfAWIIv3ujTlG5KC32q1NlWOUTeCD2DANMfJMQPW+Z1iO1xIZyfqtSWtcFZEoCmsCez5TfemFSrWumdx8Wje4zs0pbbGQKb+Yz2mVmpbJ5fI5LfuKVi/ktVqlnqkXK2XNyWdqiwUt6uTzmpPVa5liTr8U9Z4YLzmV8lOq8R+hknzc9SyfZ5mokqlAz24PvL8sbnl2v2nCbXLCl19/G9ir14zxlG5ODtTYKMqxISp4vzWEIhJr3B8aQ7U/VBZRNRyJPUZFJpVc+ft5lbaIX/UebOv6GFza5EBpp5CzOI7GRqjIaMmF+/kA1HCL+OWNCXFH9aXb8SbvGK97hde9iWf6eN0DYKVrdO4ZNgZK15vm383b90oNfi+50YT+KTo+AEX4nXTgjJivCQEvUnaLUAyhqBEbIhck7DYDK0v2aGvTjcP02JIXP6XNE6KIWjq2RwL/S9Tty+pOY+KLO9sn5eVnP7an/Ya94N5em+C9BE7SMYHujcz865LjkAQbZmEOnoMCVGEZlsk/AwC8Tmrv).

## Other builds of this spec

- [DS/Ruin — Demonic Sacrifice + Ruin](../research/raid/builds/ds-ruin-raid.md) (22/11/18, 716 DPS in a full raid) — [open the talent tree](https://talentsforever.com/warlock/60/15500020135-0050203001-0550005003-7)
- [Affliction/Destruction — Shadow Bolt / Ruin / Shadowburn](../research/raid/builds/destruction-fire-raid.md) (22/11/18, 689 DPS in a full raid) — [open the talent tree](https://talentsforever.com/warlock/60/25500010135-0050203001-0550004103-7)

---
*Generated by `_reference/data/render_modes.py` on 2026-10-26 from this project's builds and simulations of the WoW: Forever beta (talent and spell data: client build 1.60.1.70425; raid numbers: the ElliotWood/Forever fork (deleted 2026-10-18) at 2ce8265 (client 1.60.1.70291)). Simulations, not in-game measurements. Do not hand-edit.*

