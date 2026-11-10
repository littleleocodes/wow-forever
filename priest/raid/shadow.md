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
- Out of mana in a long fight: **Dark Sacrifice** (an Undead racial spell, so only Undead priests have it) turns 1,600 of your health over 15 seconds into 1,600 mana plus your Spirit, once every 10 minutes; the full list holds it below **Mind Flay**, so it only fires when you cannot afford a **Mind Flay**.

## Talents

| Tree | Points | Talents (ranks) |
|---|---|---|
| Discipline | 16 | Twin Disciplines 5, Mental Strength 5, Inner Focus 1, Martyrdom 2, Silent Resolve 3 |
| Shadow | 35 | Shadow Focus 5, Improved Mind Blast 5, Improved Shadow Word: Pain 2, Mind Flay 1, Improved Mind Flay 2, Vampiric Embrace 1, Shadow Weaving 3, Devouring Contagion 2, Early Demise 2, Darkness 5, Shadowform 1, Silence 1, Spirit Tap 5 |

## The numbers

| Setting | DPS |
|---|---|
| Full raid, 3-minute fight (every raid buff and debuff: what this page ranks on) | 796 |

**By gear tier** (the spec's best talents for each tier and setting in its own gear, found by this project's machine-learning search in the community simulator, wowsims/forever 16e8542 (client 70790); [every spec](../../_reference/dps-rankings.md)):

| Gear | Full raid DPS | Best talents |
|---|---|---|
| Pre-BiS | 772 | [18/0/33](https://talentsforever.com/priest/60/00530520102--50352001201312251-12) |
| Phase 1 BiS | 795 | [18/0/33](https://talentsforever.com/priest/60/00530520102--50352001201312251-12) (as good as this build in this gear) |

*Each row is in that tier's own gear set; the DPS at the top of the page is this build in the standard set, so the two do not match.*

**The gear** (average item level: Pre-BiS 60.2; Phase 1 BiS 62.8; each item opens its Wowhead page, with where it drops and its enchant):

| Slot | Pre-BiS | Phase 1 BiS |
|---|---|---|
| Head | [Felcloth Hood](https://www.wowhead.com/forever/item=14111) · *Tailoring*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) | [Felcloth Hood](https://www.wowhead.com/forever/item=14111) · *Tailoring*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) |
| Neck | [Orb of the Darkmoon](https://www.wowhead.com/forever/item=19426) · *quest: 1200 Tickets - Orb of the Darkmoon* | [Choker of the Fire Lord](https://www.wowhead.com/forever/item=18814) · *Ragnaros, Molten Core* |
| Shoulders | [Mantle of the Timbermaw](https://www.wowhead.com/forever/item=19050) · *Tailoring* | [Mantle of the Timbermaw](https://www.wowhead.com/forever/item=19050) · *Tailoring* |
| Back | [Arcanoweave Cloak](https://www.wowhead.com/forever/item=272411) · *sold by Pix Xizzix* | [Arcanoweave Cloak](https://www.wowhead.com/forever/item=272411) · *sold by Pix Xizzix* |
| Chest | [Earthpower Vest](https://www.wowhead.com/forever/item=21183) · *quest: Veteran's Battlegear*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) | [Earthpower Vest](https://www.wowhead.com/forever/item=21183) · *quest: Veteran's Battlegear*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) |
| Wrist | [Rockfury Bracers](https://www.wowhead.com/forever/item=21186) · *quest: Stalwart's Battlegear*<br>+ [Enchant Bracer - Greater Intellect](https://www.wowhead.com/forever/spell=13825) | [Rockfury Bracers](https://www.wowhead.com/forever/item=21186) · *quest: Stalwart's Battlegear*<br>+ [Enchant Bracer - Greater Intellect](https://www.wowhead.com/forever/spell=13825) |
| Hands | [Gloves of Spell Mastery](https://www.wowhead.com/forever/item=14146) · *Tailoring* | [Gloves of Spell Mastery](https://www.wowhead.com/forever/item=14146) · *Tailoring* |
| Waist | [Belt of the Archmage](https://www.wowhead.com/forever/item=18405) · *Tailoring* | [Belt of the Archmage](https://www.wowhead.com/forever/item=18405) · *Tailoring* |
| Legs | [Felcloth Pants](https://www.wowhead.com/forever/item=14107) · *Tailoring*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) | [Flarecore Leggings](https://www.wowhead.com/forever/item=19165) · *Tailoring*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) |
| Feet | [Sorcerer's Boots](https://www.wowhead.com/forever/item=22064) · *quest: Anthion's Parting Words*<br>+ [Enchant Boots - Minor Speed](https://www.wowhead.com/forever/spell=13889) | [Sorcerer's Boots](https://www.wowhead.com/forever/item=22064) · *quest: Anthion's Parting Words*<br>+ [Enchant Boots - Minor Speed](https://www.wowhead.com/forever/spell=13889) |
| Finger | [Warden's Signet of Brilliance](https://www.wowhead.com/forever/item=275982) | [Ring of Spell Power](https://www.wowhead.com/forever/item=19147) · *Lucifron, Molten Core* |
| Finger | [Elemental Focus Band](https://www.wowhead.com/forever/item=20682) · *Prince Skaldrenox, Silithus* | [Warden's Signet of Brilliance](https://www.wowhead.com/forever/item=275982) |
| Trinket | [Weakness Analyzer](https://www.wowhead.com/forever/item=272438) · *sold by Pix Xizzix* | [Talisman of Ephemeral Power](https://www.wowhead.com/forever/item=18820) · *Magmadar, Molten Core* |
| Trinket | [Jewel of the Guard Captain](https://www.wowhead.com/forever/item=270225) | [Weakness Analyzer](https://www.wowhead.com/forever/item=272438) · *sold by Pix Xizzix* |
| Main hand | [Sageclaw](https://www.wowhead.com/forever/item=20070) · *sold by Samuel Hawke*<br>+ [Enchant Weapon - Spell Power](https://www.wowhead.com/forever/spell=22747) | [Sageclaw](https://www.wowhead.com/forever/item=20070) · *sold by Samuel Hawke*<br>+ [Enchant Weapon - Spell Power](https://www.wowhead.com/forever/spell=22747) |
| Off hand | [Mordresh's Lifeless Skull](https://www.wowhead.com/forever/item=10770) · *Mordresh Fire Eye, Razorfen Downs* | [Mordresh's Lifeless Skull](https://www.wowhead.com/forever/item=10770) · *Mordresh Fire Eye, Razorfen Downs* |
| Ranged/relic | [Brilliant Wand](https://www.wowhead.com/forever/item=249385) · *Enchanting* | [Brilliant Wand](https://www.wowhead.com/forever/item=249385) · *Enchanting* |

**Open in the simulator** (the community's Forever simulator on the web, loaded with the gear, enchants, talents, rotation, consumables and buffs we simulate): Pre-BiS: [full raid](https://wowsims.com/forever/priest/dps/#eJzElN9LFFEUx+fcmZ05e1ZtmQjHS8S4QWzGyJ2xDfNlR58kiCQSesvRXduN2lmchezNwocIWkui8AdYkfSDAp9CehGsh62H2KdeehHDjOihCPQhiJhRoX/A+j4czjkfzvleLtxL+xGSYIAJaRiAApRhDOA6wH2AJwB6Q0RZSDuBryuIyRivkIpzJWMtQQqu3gNS8OudMM7Uk6Th0jwYn5pIw+V5MD42kYzLJVJwbQJIxZloTMOF52BMaKRg9VuSFHz3IJx/WQ/z20vhls+zYNT2koyTZ0jBp7N7UkeStWL6fRXExmDfzYdwA9h4cRLYxuA0sPXuZ6A9noWF3mpxBcaLPRidG1x4xQ4IkekQGUfYwrGsjOjIOELYjrA7bMfJ2DUGdZZYZT8Z6aTxGMn4YzSlUYxkyw70BI9zjWLpOL7u1xXOuiRd8HY6qLdSYypBcSeEiNV+SrY1oaqzExJXSSFmC76D9Bbe7OzbXj4XEHEkNa1i/S7oDXyrUvDN5ind1z2vfPGcX66YjnCOWbawRGeXOVTwSufzOdMfMb1cLp8zB6+YlULeHPErXqXol8wg740MFcx0kM+bQcHL+ZetXDmwdri1xdsvBH7p8Lbhln0jT1yD0F/FzUnQL/0LfwwvCG/9OmnIX1gNvjPnqixFOuoug8IZSanfLB42pLFht2V6KtTbbOtwpA9ZZ4UZipltW2TSf1HF3cl2VYde7JrP8SiefuR2bzfcgfDRT0FUSCvZNhkXm3v++hsEdIILvdAHZ6EAZRiFUfZnAOVqu00=); Phase 1 BiS: [full raid](https://wowsims.com/forever/priest/dps/#eJzElN9LFFEUx+fcmd05e1ZtmQjHS8S4QWzGyJ2xDfNlR58kiCQSesvRXZuN2lmcjezNwocIWmPLQBOMSPpBgU8hvQTWw0YQPvUSgRSWRA9FoA+BxIwK/QPW9+Fwzvlwzvdy4V7ai5ACHQzIwAB4UIYxgGsA9wAeAWgNEWUh7QS+qiCmYvwixXG2pK8kScGNGpCC326H8e5SilR8OQf65yZScXEO9A9NJONiiRRcmQBS8eMkhHMqzj8FfUIlBd9OhqPV7ylScPxWmD+P1nyZAb2+m2SsnSIFH8/sSh9K1YuZd1UQa4N9N+7DdWDjxRqwtcFpYF+7n4D6cAbme6vFZRgv9mB0cHDgBdsnRLZDZG1hCds0s6Ijawth2cLqsGw7a9UZLLHkJ/aLkUYqj5GMP0fTKsVINq1AS/IEVymWSeCrfk3hrEvSBG+n/VorNaaTlLBDiFjtp1RbE8Y1dkzicVKIWYJvI62FN9t7tpbPBkQcKZ6J49Id0Br4ZqXg6/UTmq+5bvn8Gb9cMWxhHzEtYYrOLmPIc0tnC3nDHzHcfL6QNwYvGxWvYIz4FbdS9EtGUHBHhjwjExQKRuC5ef+SmS8H5jY3N3n7ucAvHdwy3LRv5MmrEPrHcb0G2oV/4Y/hBeHN38d1eZXV4Qezr8hSpMPOIiickZTeYImwIY0NOy3TU6He5FqHI73P2ctMV4xc2wKT/osqzna2ozrwbMd8jkbx5AOne6vhDISvfgqiQlrOtcm40Nzz1+cgoBMc6IU+OA0elGEURtmfAQDCsLt+).

## Other builds of this spec

- [Shadow (optimized)](../research/raid/builds/opt-shadow-dps-raid-dps.md) (20/0/31, 791 DPS in a full raid) — [open the talent tree](https://talentsforever.com/priest/60/52500500003--50052101231302051-12)

---
*Generated by `_reference/data/render_modes.py` on 2026-11-10 from this project's builds and simulations of the WoW: Forever beta (talent and spell data: client build 1.60.1.70753; raid numbers: the official wowsims/forever simulator at 16e8542 (client 1.60.1.70790)). Simulations, not in-game measurements. Do not hand-edit.*

