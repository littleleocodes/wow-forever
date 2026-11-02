# Shadow Priest — Raid (group)

[Priest](../README.md) > [Raid (group)](README.md) > Shadow

**✅ Recommended** for raid (the best priest spec here, or within 3% of it).

**[Shadow (optimized)](../research/raid/builds/opt-shadow-dps-raid-dps.md)** (20/0/31) — [open the talent tree](https://talentsforever.com/priest/60/52500500003--50052101231302051-7)

## How to play

**Before the pull, then keep up all fight:** **Shadowform**.

**Talents with no line below:** **Vampiric Embrace**: taken because Shadowform requires it.

**Then press the first one that is ready**, top to bottom:

1. **Shadow Word: Pain**: keep it on the target, until the last 10 seconds of the fight
2. **Inner Focus**, then straight away **Devouring Plague**
3. **Shadow Word: Death**
4. **Mind Blast**
5. **Devouring Plague**
6. **Mind Flay**

**Mind Flay** is your filler: cast it whenever nothing above is ready.

*The simulator's full rotation for this build, with every condition: [research rotation page](../research/raid/rotation.md).*

## Why this rotation

Shadow in a raid keeps **Shadow Word: Pain** on the boss, casts **Devouring Plague**, **Shadow Word: Death** and **Mind Blast** each time they come off cooldown, and channels **Mind Flay** in every gap. **Shadowform** goes up before the pull and stays up all fight.

**Why it works**

- **Shadowform** is what makes the spec work: 10% more Shadow damage, half the mana cost on every Shadow spell and a doubled critical strike bonus. You cannot cast heals while in it.
- **Shadow Word: Pain** is first because it does about a fifth of your damage for one global cooldown every 24 seconds (18, plus 6 from **Improved Shadow Word: Pain**). Recast it only after it falls off, and not in the last 10 seconds of the fight, when a new one gets only a few ticks.
- **Inner Focus** makes your next spell free, and the list spends it on **Devouring Plague** at the pull (it comes back every 3 minutes, so once in a 3-minute fight). Its 25% crit bonus does not apply to a damage-over-time spell (beta notes of 2026-10-01), so the pair only saves mana; it comes from the community simulator's own rotation.
- After that, **Devouring Plague** goes out each time its 24-second cooldown ends, as soon as **Shadow Word: Death** and **Mind Blast** are both cooling down: its disease lasts 24 seconds, so it is up almost all fight (the simulator's 2.5% gain from casting it on cooldown was measured on the old 1-minute cooldown). **Devouring Contagion** halves its cost, and it heals you for the damage it deals.
- **Shadow Word: Death** comes before **Mind Blast** because its cooldown is longer (15 seconds against 5.5 with **Improved Mind Blast**), so waiting costs it more; the simulator measured 0.4% more damage in this order. Below 20% of the boss's health, **Early Demise** adds 30% to its crit chance.
- **Mind Flay** fills every gap and does almost half your damage: a 3-second channel that **Improved Mind Flay** makes 20% stronger. Every Shadow damage spell also stacks **Shadow Weaving** on the target (it takes 2% more Shadow damage from you a stack, up to 5, for 15 seconds), so while you keep casting it stays at 5 by itself.

**Caveats**

- **Shadow Word: Death** hits you for 10% of your maximum health every time the target survives it, about 11 times in a 3-minute fight. The damage numbers ignore that; your healers do not. **Devouring Plague** heals some of it back.
- **Mind Blast** causes a lot of threat (its tooltip says so). In the first seconds of a fight or after a tank swap, hold it until the tank is ahead; **Silent Resolve** in this build cuts the threat of your spells by 30% (Shadow Affinity, which did the same for Shadow spells, is gone since client 70425).
- When you must move, **Mind Flay** and **Mind Blast** stop: use your instants, **Shadow Word: Death**, **Devouring Plague** and **Shadow Word: Pain** if it fell off. **Shadow Weaving** drops after 15 seconds without a Shadow spell.
- Mana is not your problem in a full raid: the simulator's priest never runs dry, with one mana potion and two Demonic Runes a fight.

**When to change it**

- With adds up, keep **Shadow Word: Pain** on the ones that live longest and put **Devouring Plague** on one that dies first: **Devouring Contagion** makes the plague jump to a nearby enemy when its target dies. The simulator fights one target, so this is not measured.
- **Silence** is in this build but not in the list: use it to stop a casting add. It costs one global cooldown.
- **Vampiric Embrace** has no line because the simulator counts only damage. If your group takes damage, cast it on the boss: for 30 seconds your party heals for 20% of your Shadow damage, for 40 mana and one global cooldown a minute.
- If your healers struggle, save **Shadow Word: Death** for the last 20% of the boss's health, where **Early Demise** makes it crit more. You give up some damage to stop the backlash.

## The numbers

| Setting | DPS |
|---|---|
| Full raid, 3-minute fight (every raid buff and debuff: what this page ranks on) | 796 |

**By gear tier** (the spec's best talents for each tier and setting in its own gear, found by this project's machine-learning search in the community simulator, wowsims/forever 30f67f5 (client 70450); [every spec](../../_reference/dps-rankings.md)):

| Gear | Full raid DPS | Best talents |
|---|---|---|
| Pre-BiS | 780 | [15/3/33](https://talentsforever.com/priest/60/0053052-3-50552001201310251-7) |
| Phase 1 BiS | 800 | [15/3/33](https://talentsforever.com/priest/60/0053052-3-50552001201310251-7) (ties this build) |

**The gear** (average item level: Pre-BiS 62.2; Phase 1 BiS 64.2; each item opens its Wowhead page, with where it drops and its enchant):

| Slot | Pre-BiS | Phase 1 BiS |
|---|---|---|
| Head | [Felcloth Hood](https://www.wowhead.com/forever/item=14111) · *Tailoring*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) | [Felcloth Hood](https://www.wowhead.com/forever/item=14111) · *Tailoring*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) |
| Neck | [Orb of the Darkmoon](https://www.wowhead.com/forever/item=19426) | [Choker of the Fire Lord](https://www.wowhead.com/forever/item=18814) · *Ragnaros, Molten Core* |
| Shoulders | [Mantle of the Timbermaw](https://www.wowhead.com/forever/item=19050) · *Tailoring* | [Mantle of the Timbermaw](https://www.wowhead.com/forever/item=19050) · *Tailoring* |
| Back | [item 272411](https://www.wowhead.com/forever/item=272411) | [item 272411](https://www.wowhead.com/forever/item=272411) |
| Chest | [Earthpower Vest](https://www.wowhead.com/forever/item=21183)<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) | [Robe of Winter Night](https://www.wowhead.com/forever/item=14136) · *Tailoring*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) |
| Wrist | [Rockfury Bracers](https://www.wowhead.com/forever/item=21186)<br>+ [Enchant Bracer - Greater Intellect](https://www.wowhead.com/forever/spell=13825) | [Rockfury Bracers](https://www.wowhead.com/forever/item=21186)<br>+ [Enchant Bracer - Greater Intellect](https://www.wowhead.com/forever/spell=13825) |
| Hands | [Gloves of Spell Mastery](https://www.wowhead.com/forever/item=14146) · *Tailoring* | [Gloves of Spell Mastery](https://www.wowhead.com/forever/item=14146) · *Tailoring* |
| Waist | [Belt of the Archmage](https://www.wowhead.com/forever/item=18405) · *Tailoring* | [Belt of the Archmage](https://www.wowhead.com/forever/item=18405) · *Tailoring* |
| Legs | [Felcloth Pants](https://www.wowhead.com/forever/item=14107) · *Tailoring*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) | [Flarecore Leggings](https://www.wowhead.com/forever/item=19165) · *Tailoring*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) |
| Feet | [Sorcerer's Boots](https://www.wowhead.com/forever/item=22064)<br>+ [Enchant Boots - Minor Speed](https://www.wowhead.com/forever/spell=13889) | [Sorcerer's Boots](https://www.wowhead.com/forever/item=22064)<br>+ [Enchant Boots - Minor Speed](https://www.wowhead.com/forever/spell=13889) |
| Finger | [Warden's Signet of Brilliance](https://www.wowhead.com/forever/item=275982) | [Ring of Spell Power](https://www.wowhead.com/forever/item=19147) · *Lucifron, Molten Core* |
| Finger | [Signet Ring of the Bronze Dragonflight](https://www.wowhead.com/forever/item=21210) | [Signet Ring of the Bronze Dragonflight](https://www.wowhead.com/forever/item=21210) |
| Trinket | [Weakness Analyzer](https://www.wowhead.com/forever/item=272438) | [Talisman of Ephemeral Power](https://www.wowhead.com/forever/item=18820) · *Magmadar, Molten Core* |
| Trinket | [Jewel of the Guard Captain](https://www.wowhead.com/forever/item=270225) | [Weakness Analyzer](https://www.wowhead.com/forever/item=272438) |
| Main hand | [Sageclaw](https://www.wowhead.com/forever/item=20070)<br>+ [Enchant Weapon - Spell Power](https://www.wowhead.com/forever/spell=22747) | [Sageclaw](https://www.wowhead.com/forever/item=20070)<br>+ [Enchant Weapon - Spell Power](https://www.wowhead.com/forever/spell=22747) |
| Off hand | [Tome of Shadow Force](https://www.wowhead.com/forever/item=19309) | [Tome of Shadow Force](https://www.wowhead.com/forever/item=19309) |
| Ranged/relic | [Brilliant Wand](https://www.wowhead.com/forever/item=249385) · *Enchanting* | [Brilliant Wand](https://www.wowhead.com/forever/item=249385) · *Enchanting* |

**Open in the simulator** (the community's Forever simulator on the web, loaded with the gear, enchants, talents, rotation, consumables and buffs we simulate): Pre-BiS: [full raid](https://wowsims.com/forever/priest/dps/#eJzElN9LFFEUx+fcnZ05e1ZtmQjHWw/jBrEZI3fGNsyXHX2SIJJA6C1Hd202amdzFrI3Cx8iaC0JQxOMSPpBgU8hvQjWw/YSPvVQL2ZYEQVFoA9BxIwu9A9Y34fLOefDOefLhXtpH0IKdDAgAwPgQRnGAK4C3AV4CKA1RJSFtBP4exkxFecXSMG5kr6eJBnXbgPJ+OUWkEQqLs2D/qGJVFyeB/1dE8VwuUQyrk8AKXgnalFx4QnoEyrJWP2aIhnfzocTnq2E8c2lFKn4cRb02m6S8dtUiB7N7kofStWKmddVEBuDfdfvwTVg48VJYBuDM8A+dT8G9cEsLPRWi6swXuzByDQ48JztFSLbIbK22WFmRTZrC2HZwuqwhJ21agxWWHKN/WSkkcrjFMMfo2mV4hQzrUCTOeuSNMHbab/WSo3pJCVsleIZxGo/pdqaUNHYMYkrJBOzBK8jrYU323u2580FRBxJySi4MgVaA9/KZHy5eUJL8kTUlcAX/ZqvuW753Gm/XDFsYR8xLWGKzi5jyHNLZwp5wx8x3Hy+kDcGLxkVr2CM+BW3UvRLRlBwR4Y8IxMUCkbguXn/opkvB2adm1u8/Wzglw5ub9/y0siTVyA0o+DmJGjn/8V+DG8Lb/w6rsc+sxp8Z/blmBTpsLMMMmckpX+zRFiQxoadlpnpUK9yrcOR3uTsVabLRq5tkUn/RRWnHu2oDjzdsT1Ho/Pkfad7u+AMhM99GqJEWs21xXCxueevX0FAJzjQC31wCjwowyiMsj8DAJz7ud0=); Phase 1 BiS: [full raid](https://wowsims.com/forever/priest/dps/#eJzEVN9LFF0Ynvfs7My776rfMh/heOriuEFsxsiZsQ3zZkevJIgkELrL0V3bjdrZnIXszsKLCNKwFBTBiKQfFHgV0qV1sRGEV10UgRVWBEER6EUgMaML/QPWc/Ey7/PwzPNw4Bzah5ACEwRkYACKUIExgKsAtwHuAxgNkcpCtRP4exUxFecXSMOFsrmeJBW3poBU/HoLSCENl8vmxybScWURzLdNFMOVMqm4Pgmk47tpCC06Lj0Cc1InFV9Oh943i+EcvxnOJ6sp0vHTPJi1/0nFbzMh+WD+v/ShVK2UeTUBcmOw7/oduAZsvDQFbGNwDtjn7oeg35uHpd6J0hqMl3owKg0uPGV7pcx2yKxjdVhZmc06UtqOtDts6WTtGoNVlvzAfjIySOdxiuGP0bROcYpZdmConHUphuTttN9opcZ0khKOTvEM4kQ/pdqaUDPYMYVrpBKzJa9LRgtvdvbs/G8hIOJIWkbD1RkwGvj2puLzzRNGkiciVwKf9Ru+4XmVc6f9SlU40jli2dKSnV1iqOiVzxTywh8RXj5fyIvBS6JaLIgRv+pVS35ZBAVvZKgoMkGhIIKil/cvWvlKYNV1a1tvPxv45YM76dtdGnnyCoRlNNycAuP838jH8LTwxq/jZuwLq8F35lyOKREOuyugckZKeoslQkIZG3Zb5mZDvMi1Dkd4nXPWmKmKXNsyU/4Jqm79a1dx4PGu5RyN5sm7bvcO4Q6E130WokVZy7XFcLm5549XQUInuNALfXAKilCBURhlvwcA+Zy5rg==).

---
*Generated by `_reference/data/render_modes.py` on 2026-11-02 from this project's builds and simulations of the WoW: Forever beta (talent and spell data: client build 1.60.1.70707; raid numbers: the official wowsims/forever simulator at 30f67f5 (client 1.60.1.70450)). Simulations, not in-game measurements. Do not hand-edit.*

