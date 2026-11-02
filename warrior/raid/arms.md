# Arms Warrior — Raid (group)

[Warrior](../README.md) > [Raid (group)](README.md) > Arms

**[Arms — Raid](../research/raid/builds/arms-ml-raid.md)** (39/10/2) — [open the talent tree](https://talentsforever.com/warrior/60/04305213132515211-0505-2-7)

> 🔬 Derived build: found by this project's machine-learning search over every legal build of the spec in the community's raid simulator (phase-1 BiS gear, then raced against the spec's builds); it beat the hand-made build (Arms — Battle Stance), which stays below as the alternative. A model of the beta, to check at launch.

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
8. **Bloodrage** when you have less than 45 rage

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
| Full raid, 3-minute fight (every raid buff and debuff: what this page ranks on) | 779 |

**By gear tier** (the spec's best talents for each tier and setting in its own gear, found by this project's machine-learning search in the community simulator, wowsims/forever 54ceac6 (client 70707); [every spec](../../_reference/dps-rankings.md)):

| Gear | Full raid DPS | Best talents |
|---|---|---|
| Pre-BiS | 879 | [39/10/2](https://talentsforever.com/warrior/60/30325213132515201-0505-2-7) |
| Phase 1 BiS | 886 | [39/9/3](https://talentsforever.com/warrior/60/30325213132515201-0504-21-7) (ties this build) |

**The gear** (average item level: Pre-BiS 65.4; Phase 1 BiS 64.7; each item opens its Wowhead page, with where it drops and its enchant):

| Slot | Pre-BiS | Phase 1 BiS |
|---|---|---|
| Head | [Lionheart Helm](https://www.wowhead.com/forever/item=12640) · *Blacksmithing*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11645) | [Lionheart Helm](https://www.wowhead.com/forever/item=12640) · *Blacksmithing*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11645) |
| Neck | [Beads of Ogre Might](https://www.wowhead.com/forever/item=22150) | [Onyxia Tooth Pendant](https://www.wowhead.com/forever/item=18404) |
| Shoulders | [Field Marshal's Plate Shoulderguards](https://www.wowhead.com/forever/item=16480) | [Field Marshal's Plate Shoulderguards](https://www.wowhead.com/forever/item=16480) |
| Back | [Earthweave Cloak](https://www.wowhead.com/forever/item=21187)<br>+ [Enchant Cloak - Lesser Agility](https://www.wowhead.com/forever/spell=13364) | [Earthweave Cloak](https://www.wowhead.com/forever/item=21187)<br>+ [Enchant Cloak - Lesser Agility](https://www.wowhead.com/forever/spell=13364) |
| Chest | [Darkmantle Tunic](https://www.wowhead.com/forever/item=22009)<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) | [Darkmantle Tunic](https://www.wowhead.com/forever/item=22009)<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) |
| Wrist | [Forest Stalker's Bracers](https://www.wowhead.com/forever/item=19587)<br>+ [Enchant Bracer - Superior Strength](https://www.wowhead.com/forever/spell=19984) | [Forest Stalker's Bracers](https://www.wowhead.com/forever/item=19587)<br>+ [Enchant Bracer - Superior Strength](https://www.wowhead.com/forever/spell=19984) |
| Hands | [Stormshroud Gloves](https://www.wowhead.com/forever/item=21278) · *Leatherworking*<br>+ [Enchant Gloves - Strength](https://www.wowhead.com/forever/item=273529) | [Stormshroud Gloves](https://www.wowhead.com/forever/item=21278) · *Leatherworking*<br>+ [Enchant Gloves - Strength](https://www.wowhead.com/forever/item=273529) |
| Waist | [Belt of Preserved Heads](https://www.wowhead.com/forever/item=20216) | [Belt of Preserved Heads](https://www.wowhead.com/forever/item=20216) |
| Legs | [Titanic Leggings](https://www.wowhead.com/forever/item=22385) · *Blacksmithing*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11645) | [Titanic Leggings](https://www.wowhead.com/forever/item=22385) · *Blacksmithing*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11645) |
| Feet | [Marshal's Plate Boots](https://www.wowhead.com/forever/item=16483)<br>+ [Enchant Boots - Greater Agility](https://www.wowhead.com/forever/item=16245) | [Marshal's Plate Boots](https://www.wowhead.com/forever/item=16483)<br>+ [Enchant Boots - Greater Agility](https://www.wowhead.com/forever/item=16245) |
| Finger | [Don Julio's Band](https://www.wowhead.com/forever/item=19325) | [Don Julio's Band](https://www.wowhead.com/forever/item=19325) |
| Finger | [Signet Ring of the Bronze Dragonflight](https://www.wowhead.com/forever/item=21205) | [Band of Earthen Might](https://www.wowhead.com/forever/item=21182) |
| Trinket | [Adaptive Combat Assistant](https://www.wowhead.com/forever/item=272437) | [Adaptive Combat Assistant](https://www.wowhead.com/forever/item=272437) |
| Trinket | [Jewel of the Guard Captain](https://www.wowhead.com/forever/item=270225) | [Jewel of the Guard Captain](https://www.wowhead.com/forever/item=270225) |
| Main hand | [Grand Marshal's Sunderer](https://www.wowhead.com/forever/item=18830)<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) | [Grand Marshal's Sunderer](https://www.wowhead.com/forever/item=18830)<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) |
| Ranged/relic | [Premier High Warlord's Recurve](https://www.wowhead.com/forever/item=272594) | [Premier High Warlord's Recurve](https://www.wowhead.com/forever/item=272594) |

**Open in the simulator** (the community's Forever simulator on the web, loaded with the gear, enchants, talents, rotation, consumables and buffs we simulate): Pre-BiS: [full raid](https://wowsims.com/forever/warrior/dps/#eJzEVl1oHFUU3jM/O2dPmu30JtLJjT/TRetm68T5yaRJFbMpCuqLRR+UvJhJsu2u1CTs7EP7lkQREQktYmEDmvgTCdEqFo2lSEULWoVCIzTgH4ZUUNSH+qaiVu7sblKT4ENg9T4MZ+85557vO9+5s0PXI+hggAlp6Ic8jMIYwNMAMwBzAGxb5JWEtwv4V9tR0YEfpTguDxgrDaTgUyeBFFweA9Lw3CwYi3HS8LfXwbicJA2fKIPxjTBefA2MaY0U/PUFEfnLmyDSNbw8Bsa3SVLwzxPinEuz4vnuRZ0UPP6BThpOPgfGz0mKkYKfL+qpW/SPC+nvpuHA0iQ8A9JEYQoSrwRvBF/2Ts/CPEjPFq7ARGE/RrAhC2ckw7M913cdz/Fc3/Fd27Fs3/Yt97ykrEg/NhIjjaskY7kppZFKsuWELMErex/2rZqX+liW30Uec6g104IyS34EDaSmVbzQxyRdFUEEDrGUTslTVdfZhyOXVourHqafeIgRRx4nRV88DqyTd9Ae3kY7MttRYdL9MR4h8eyQmjMM49EWEVLcdZx2PxS1cK6f3YjA+fosp+p/r5F53KE2fuv6CNcOiWX06rlIcVKcDjvkCkkGZ3u5vxkYdyMYpyMCEycFv54BdgNvXZ/UaYeCJP50FpjPvc3AeJuA8Spp+vuzW0nDl7/fUrXxd7ac9hawQ8Ho4UdHRkuma7udlmNbnrPPHMwHw4dyQ+ZI0QyGhnJD5sBRs5TPmcWRUlAqjAybYS4oDubNdJjLmUHx8dAaCEqlwzmrGBSGrFqUVYlqfywcGW7jd9OdbB/t5jcTTaFGsn51j85r9vhta/ZEQeekZ5Ki28WYwEqS41dVFmIJn8rkFYhVh1coYibxWCN7fhNC7t76EMrQLnYTNaQSpLlisBf6ItSVgYhQd1YmeqGvdmvw7TlgTXwHqZ9JEoJQJK3iwkuwGjD5xwNsG6fIo+DSGWCjbPAfjOxuy+3aCiM3/29sEmtN7OU95LDbN/aZWnlLjWNNmQ67RoYITUir+MUMsNJGGWy3PjJEwNMyXuhmT/6H41xphHxNI/xI7KvN7D4Efg/dwbqjN67KGuZhVc7qJWz3Q+IZA1VG81Br/JpPnIjnjgEL1xES4nfXh1D0WseLMxuL1vEORUX1T1Z0tpNfR9tSRHgKRBvLTdU/N0P+QToPVyR3XI5Fqzk7LzVQgjSU02D/Dqm/pITYj40dzLZMlcX6tGfXwWgt9bjLkqGYPZnTUux/WaVszarr2n2ybnW6o+eDr2Z7qxvZfvGhVYboR2y5JyPj6Z37r/kes6ELsnAvHIBHIA+jcASOSH8PAC763Kg=); Phase 1 BiS: [full raid](https://wowsims.com/forever/warrior/dps/#eJzEVl1oHFUU3jM/O2dPku30JtLJjT/TRetm68T5yaRJFbMpCuqLRR+UvJhJsu2u1CTs7EP7lkQfRCS2iIUENPEnEuIfFo2lSEQLWoVCIxhQKoa0oKgP9U1FrdzZ3aQmwYfA2vswnL3nnHu+73znzg7diKCDASakoQ/yMAKjAM8AzADMAbD6yCsJbyfwiztQ0YEfoziu9BurdaTg5eeBFFwZBdLw7CwYS3HS8Pc3wbiUJA2fmgTjO2G8/AYY0xop+NtLIvLXd0Cka3hpFIzvk6TgXyfFOYuz4vnBBZ0UPPGxThpOvADGL0mKkYJfLemp2/TPCunL03BweQKeBWm8MAWJ14K3gm97pmdhHqTnCldgvHAAI9iQhTNSs2d7ru86nuO5vuO7tmPZvt1uuc45SVmVfmogRhpXScbJxpRGKsmWE7IEL+990rtmft3Lsvwe8phDLZlmlFnyU6gjNa3i+V4m6aoIInCIpXRKnqq4Fh+NXFo1rnKYfvIRRhx5nBR96QSwDt5Oe3kr7czsQIVJD8Z4hMSzQ2rKMIxHW0RIcddx2vxQ1MK5PnYzAucbs5yK/8MG5nGHWvntGyNcOySW0SvnIsVJcdrtkCskGZzt4/5WYNzNYJz2CEycFLw4A+wm3rIxqcMOBUn8eRGYz72twHhbgPHKafpHs9tJw1d/2Fa1sfe3nfYusMPByJHHh0dKpmu7HZZjW56z3xzIB0OHc4PmcNEMBgdzg2b/MbOUz5nF4VJQKgwPmWEuKA7kzXSYy5lB8cnQ6g9KpSM5qxgUBq1qlFWOansiHB5q5ffS3Ww/7eG3Ek2hRrJ+da/Oq/bYHev2eEHnpGeSotvFmMBKkuNXVBZiCZ/K5FWIVYZXKGIm8XgDe3ELQu6+2hDK0G52C9WlEqS5YrAXeiPU5YGIUHeUJ3qht3pr8L05YI18J6lfShKCUCSt4sIrsBYw8edDrJ5T5FFw+QywETbwL0Z2l+V2boeRm/8vNon1JvbwbnLYnZv7TC28ucqxqky7XSVDhCakVfxmBlhpswy2WxsZIuBpGc93saf/x3EuN0K+phF+JPbVJvYAAr+P7mJd0RtXZXXzsCZn5RK2+SHxjIEqo3moNn7dJ07Es8eBhRsICfG7akMoeq3jhZnNRWt4h6Ki+uerOtvFb6D6FBGeAtHGycbKn5sh/yidgyuSOybHotWUnZfqKEEaymmw/4DU31JC7MdGD2WbpybF+qJ796FoLXe7K5KhmN2Z01LsuqxStmrVdO15u2Z1uqLnw69neyob2T7xpTUJ0Y/YSndGxtO7DlzzQWZDJ2ThfjgIj0EeRuAoHJX+GQCqB90D).

## Other builds of this spec

- [Arms — Battle Stance](../research/raid/builds/arms-battle-raid.md) (34/17/0, 775 DPS in a full raid) — [open the talent tree](https://talentsforever.com/warrior/60/02305213132514101-55050000002--7)

---
*Generated by `_reference/data/render_modes.py` on 2026-11-02 from this project's builds and simulations of the WoW: Forever beta (talent and spell data: client build 1.60.1.70707; raid numbers: the official wowsims/forever simulator at 54ceac6 (client 1.60.1.70707)). Simulations, not in-game measurements. Do not hand-edit.*

