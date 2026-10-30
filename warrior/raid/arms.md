# Arms Warrior — Raid (group)

[Warrior](../README.md) > [Raid (group)](README.md) > Arms

**[Arms — Battle Stance](../research/raid/builds/arms-battle-raid.md)** (34/17/0) — [open the talent tree](https://talentsforever.com/warrior/60/02305213132514101-55050000002--7)

## How to play

**Before the pull, then keep up all fight:** **Battle Stance**.

**Then press the first one that is ready**, top to bottom:

1. **Overpower** when it lights up (after the target dodges)
2. **Slam**
3. **Rend**: keep it on the target
4. **Mortal Strike**
5. **Execute** when the target is below 20% health
6. **Spearing Strike**
7. **Hamstring**
8. **Bloodrage** when you have less than 90 rage

Between these, your white swings do the rest.

*The simulator's full rotation for this build, with every condition: [research rotation page](../research/raid/rotation.md).*

## Why this rotation

Arms in a raid stays in **Battle Stance** and lives off **Overpower**. Keep **Rend** on the boss so **Bloodthrill** keeps lighting up **Overpower**, use **Slam** and **Mortal Strike** on cooldown, let **Execute** take the leftover rage below 20%, and fill every gap with **Hamstring**.

**Why it works**

- **Overpower** is at the top: 5 rage for a full weapon hit with 50% more crit chance (**Improved Overpower**), and it stays lit for only 5 to 6 seconds. Most of yours come from **Bloodthrill**, not from dodges: each main-hand hit on a target with your **Rend** has a 20% chance to light it up. The simulator measured 2% more damage with **Overpower** first.
- **Slam** comes next. With **Improved Slam** it is a 1-second cast on a 15-second cooldown that no longer delays your swing, so it costs only 15 rage and a short global cooldown; the simulator measured it best right under **Overpower**.
- **Rend** goes before **Mortal Strike** because **Bloodthrill** only works while it ticks: without it, **Overpower** lights up on dodges alone. It lasts 21 seconds, about 9 casts a fight.
- **Execute** stays below **Mortal Strike** even under 20%. It spends all your rage (600 damage plus 15 per extra rage point), so the rotation uses **Overpower**, **Slam**, **Rend** and **Mortal Strike** whenever they are ready and lets **Execute** take what is left; the simulator measured 1.3% more damage than with **Execute** at the top.
- **Spearing Strike** (15 rage, 20-second cooldown) deals only 40% of your weapon damage against most bosses, so it sits under your main attacks and above the filler.
- **Hamstring**, not **Bloodrage**, is your real filler. For 10 rage it is another main-hand hit that can light up **Overpower** through **Bloodthrill** and, in a raid, trigger a shaman's Windfury Totem; the simulator measured about 1% more damage casting it freely than only above 80 rage. **Bloodrage** is a 1-minute rage cooldown for when you run short: the rotation uses it under 90 rage when nothing else is ready, once or twice a fight.

**Caveats**

- This list is for a full raid. With fewer buffs you will not have the rage for free **Hamstring** casts: the simulator's rotation for a warrior alone on a training dummy never casts it and stacks **Sunder Armor** instead.
- Several targets: **Whirlwind** needs **Berserker Stance**, so this list never uses it. With a second target in reach, press **Sweeping Strikes** (30 rage, 30-second cooldown: your next 5 melee attacks also hit a second target), and above 40 rage use **Cleave** in place of **Hamstring**.
- The simulator's full list keeps a **Mocking Blow** line near the bottom that never fires. Never use it on a boss: it forces the boss to attack you for 6 seconds.
- Stand behind the boss: from the front it can parry and block, and a swing that does not land gives you no rage.

**When to change it**

- If nobody in your group has **Battle Shout** up, cast it before the pull and again every 3 minutes: the list leaves it out because the simulator's raid already had one.
- If the boss has no **Sunder Armor** and no Expose Armor, put one **Sunder Armor** on it. That is the full list's only **Sunder Armor** line; it never fired because the simulator's raid already carries the tank's 5 stacks.
- Against Giants and Dragonkin, **Spearing Strike** deals an extra 80% of weapon damage (three times as much), so press it right after **Mortal Strike**. The simulator's boss is neither, so that order is untested.

*This guide was written for the rotation of 2026-10-09; the list above was re-tuned since, so follow the list where the two differ.*

## The numbers

| Setting | DPS |
|---|---|
| Full raid, 3-minute fight (every raid buff and debuff: what this page ranks on) | 799 |

**By gear tier** (the spec's best talents for each tier and setting in its own gear, found by this project's machine-learning search in the community simulator, wowsims/forever 30f67f5 (client 70450); [every spec](../../_reference/dps-rankings.md)):

| Gear | Full raid DPS | Best talents |
|---|---|---|
| Pre-BiS | 786 | [38/10/3](https://talentsforever.com/warrior/60/20325213132515201-0505-201-7) |
| Phase 1 BiS | 793 | [37/12/2](https://talentsforever.com/warrior/60/02305213132515211-2505-2-7) |

**The gear** (average item level: Pre-BiS 62.3; Phase 1 BiS 62.1; each item opens its Wowhead page, with where it drops and its enchant):

| Slot | Pre-BiS | Phase 1 BiS |
|---|---|---|
| Head | [Lionheart Helm](https://www.wowhead.com/forever/item=12640) · *Blacksmithing*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11645) | [Lionheart Helm](https://www.wowhead.com/forever/item=12640) · *Blacksmithing*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11645) |
| Neck | [Beads of Ogre Might](https://www.wowhead.com/forever/item=22150) | [Onyxia Tooth Pendant](https://www.wowhead.com/forever/item=18404) |
| Shoulders | [Highlander's Plate Spaulders](https://www.wowhead.com/forever/item=20057) | [Highlander's Plate Spaulders](https://www.wowhead.com/forever/item=20057) |
| Back | [Howler's Furs](https://www.wowhead.com/forever/item=272414)<br>+ [Enchant Cloak - Lesser Agility](https://www.wowhead.com/forever/spell=13364) | [Howler's Furs](https://www.wowhead.com/forever/item=272414)<br>+ [Enchant Cloak - Lesser Agility](https://www.wowhead.com/forever/spell=13364) |
| Chest | [Darkmantle Tunic](https://www.wowhead.com/forever/item=22009)<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) | [Darkmantle Tunic](https://www.wowhead.com/forever/item=22009)<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) |
| Wrist | [Deeprock Bracers](https://www.wowhead.com/forever/item=21184)<br>+ [Enchant Bracer - Superior Strength](https://www.wowhead.com/forever/spell=19984) | [Deeprock Bracers](https://www.wowhead.com/forever/item=21184)<br>+ [Enchant Bracer - Superior Strength](https://www.wowhead.com/forever/spell=19984) |
| Hands | [Theramore Gauntlets](https://www.wowhead.com/forever/item=271940)<br>+ [Enchant Gloves - Strength](https://www.wowhead.com/forever/item=273529) | [Stormshroud Gloves](https://www.wowhead.com/forever/item=21278) · *Leatherworking*<br>+ [Enchant Gloves - Strength](https://www.wowhead.com/forever/item=273529) |
| Waist | [Belt of Preserved Heads](https://www.wowhead.com/forever/item=20216) | [Highlander's Chain Girdle](https://www.wowhead.com/forever/item=20043) |
| Legs | [Titanic Leggings](https://www.wowhead.com/forever/item=22385) · *Blacksmithing*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11645) | [Titanic Leggings](https://www.wowhead.com/forever/item=22385) · *Blacksmithing*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11645) |
| Feet | [Boots of Heroism](https://www.wowhead.com/forever/item=21995)<br>+ [Enchant Boots - Greater Agility](https://www.wowhead.com/forever/item=16245) | [Boots of Heroism](https://www.wowhead.com/forever/item=21995)<br>+ [Enchant Boots - Greater Agility](https://www.wowhead.com/forever/item=16245) |
| Finger | [Band of the Better Half](https://www.wowhead.com/forever/item=284716) | [Don Julio's Band](https://www.wowhead.com/forever/item=19325) |
| Finger | [Don Julio's Band](https://www.wowhead.com/forever/item=19325) | [Band of the Better Half](https://www.wowhead.com/forever/item=284716) |
| Trinket | [Everlook Pathcarver](https://www.wowhead.com/forever/item=274759) | [Everlook Delivery Bot](https://www.wowhead.com/forever/item=274760) |
| Trinket | [Jewel of the Guard Captain](https://www.wowhead.com/forever/item=270225) | [Jewel of the Guard Captain](https://www.wowhead.com/forever/item=270225) |
| Main hand | [Premier High Warlord's Pulverizer](https://www.wowhead.com/forever/item=272601)<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) | [Nightfall](https://www.wowhead.com/forever/item=19169) · *Blacksmithing*<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) |
| Ranged/relic | [Premier High Warlord's Recurve](https://www.wowhead.com/forever/item=272594) | [Premier High Warlord's Recurve](https://www.wowhead.com/forever/item=272594) |

**Open in the simulator** (the community's Forever simulator on the web, loaded with the gear, enchants, talents, rotation, consumables and buffs we simulate): Pre-BiS: [full raid](https://wowsims.com/forever/warrior/dps/#eJzEVl9oW2UUz/nuvbknp1m8/VrZ7Vf/3AXUNHLrvTdN1yiYdCCoLw59UPJib5tsicwm5OZhe9v6ICIytgcHHWrrn0LpNtEhdQ6ZOsVNcbAKFiqKJQoK82G+qfiPe5O02hYfCnHnIXw5f3+/c06+fHQLggY6GJCAMShBFQ4DPAswCzAPwKOBlfnWERDvxlDWQByiMK6O640ukvGZM0AyrrwIpOLLVzV9KUwq/noK9O9ipOIHc6B/4x8+/lzTZ1SS8ZeXfM+f3wA/XMVrp0D/NkYynn6zm2T844Sf7VJDIxmPv6+RiitLmv5TjEIk4xdLWvwO7ZNy4vsZ2Lt8FJ4DNlU+CZHX3NPuV6Mzc7AA7PnydZgq74muk8rBeSYcK+WkHTtlp5y0nXYs27TSVtp0LPsykxvsYpQ4qUIhCad74iopJJm2xyOiqfswv3b8Ms9z4n5KcZv6k30o8dhF6CIloeCVPGea4jsR2MTjGsXOtkwXHg9MatuvlUw78RgngSJMsrZ0HPiwGKK7xQB1J29CmbOHQyJAkrI86k1yDAcqIqSwY9uDac+vhfNj/DYEITZG2S37Ozt4Stg0IO7a6OFYHvGk1sqLFCbZHrI8IRPTBd8t0luBcTaDsYcCMGGS8etZ4LeK/o1Bw5bnk8RrF4CnRWorMKktwKSaYdp7c9sJw1d/2Fa1I29vO8ynriVjqHCpAaHWKvj8DMBjO/gLwPe71QNPVqp1w7GcYdO2TGf3vcZEyZ3cXywYlZrhFgrFgjF+yKiXikatUnfr5cqk4RXd2kTJSHjFouHWnvbMcbdeP1A0a265YLa9zKbX4FNeZXJAJGkXv5264hFSHX9NFvMBsmZ7wyQTG27ux2K+vYP41jzwHtFNymeMIfj8EgouvgJrDkd/f4RHBQUWGZfPA6/yiX8xsjKmM7IdRk7pv9hE1ps4KrJk83s295n6RV+bY63FcchqkyFCAxIKrswCr28eg+V0ZgwB8ISEVzK8DU9ah5exghH81csfQhAP0H08E9wqCu9agLUmtxZtMO2RSOqocFqAdjvWbX5G/OgYcG8DO38kmc6wC64uvDoLvLZFSztUtHl1TpW59//9mgKi2qWGxneKmykaJ8Kz4I9uuqf1p6FLP7LLcJ05R6RQIL25BdZFEVJRSoD1G8T/ZBFfHzq8L9d3ctqXT7O79gWynHVWmS4b2eQ5FrohUs+1Tx2VO890rE4m+Hz09dxoS5Eb858x0xB8Ca1mkxKe27nnH68dC0YgBw/CXngCSlCFg3CQ/T0ANMex5A==); Phase 1 BiS: [full raid](https://wowsims.com/forever/warrior/dps/#eJzEVl9oW2UUz/nuvbknp1m8/VrZ7Vf/3AXUNHLrvTdN1yiYdCCoLw59UPJib5tsicwm5OZhe9v6JCJze9igQ9b6p1K6KTqkG0OmTtCqDFbBwkSxxoHCfJiPiv+4N0mrbfGhEHcewpfz9/c75+TLR3cgaKCDAQkYgxJU4TDACwCzAPMAPBpYmW8dAXE+hrIG4hCFcXVcb3SRjNdfBpLx2itAKp6+qunLYVLx1zOg/xAjFT+cA/1b/3D6TdBnVJLxi8Dzl7fBD1fxxhnQv4uRjH+c9POcfaebZFxqaCTj8Q80UvH7E6D/HKMQyfjlsha/R/uknLg+A3tXjsKLwKbKpyDyunvW/Xp0Zg4WgL1UvglT5T3RdVI5uMh0y0lZacdO2Sknbacd2zadtJU2nSUmN9jlKHFShUISTvfEVVJIMm2PR0RT91F+7fhVnufEw5TiNvUn+1DiscvQRUpCwSt5zjTFdyKwicc1ip1rmS49HZjUtl8rmXbyKU4CRZhkbfk48GExRPeLAepO3oYyZ4+HRIAkZXnUm+QYDlRESGHHtgfTnl8L58f4XQhCbIyyW/bzO3hK2DQg7tvo4Vge8aTWyosUJtkesjwhE9MF3y3SW4FxNoOxhwIwYZLxm1ngd4r+jUHDlueTxBuXgKdFaiswqS3ApJph2vtz2wnD137cVrUj7207zKeuJWOocKkBodYq+PwMwGM7+Ang+93qgWcr1brhWM6waVums/tBY6LkTu4vFoxKzXALhWLBGD9k1EtFo1apu/VyZdLwim5tomQkvGLRcGvPe+a4W68fKJo1t1ww215m02vwOa8yOSCStIvfTV3xCKmOvyaL+QBZs71hkokNN/djMd/eQXx3HniP6Cblc8YQfH4JBRdfhTWHo78/waOCAouMKxeBV/nEvxhZGdMZ2Q4jp/RfbCLrTRwVWbL5A5v7TP2ir82x1uI4ZLXJEKEBCQWvzQKvbx6D5XRmDAHwhIRXMrwNT1qHl7GCEfzVyx9DEI/QQzwT3CoK71qAtSa3Fm0w7ZFI6qhwWoB2O9Ztfkb8+BhwbwM7fySZzrALri68Ogu8tkVLO1S0eXVOlbn3//2aAqLapw2N7xS3UzROhOfAH910T+tPQ5d+YktwkzlHpFAgvbkF1kURUlFKgPUbxP9kEV8fOrwv13dq2pfPsrv2BbKSdVaZLhvZ5AUWuiVSz7VPHZV73+pYnUzw+eQbudGWIjfmP2KmIfgSWs0mJbywc88/3joWjEAOHoW98AyUoAoH4SD7ewD6trD1).

## Other builds of this spec

- [Arms — Raid](../research/raid/builds/arms-ml-raid.md) (39/10/2, 797 DPS in a full raid) — [open the talent tree](https://talentsforever.com/warrior/60/04305213132515211-0505-2-7)

---
*Generated by `_reference/data/render_modes.py` on 2026-10-30 from this project's builds and simulations of the WoW: Forever beta (talent and spell data: client build 1.60.1.70425; raid numbers: the official wowsims/forever simulator at 30f67f5 (client 1.60.1.70450)). Simulations, not in-game measurements. Do not hand-edit.*

