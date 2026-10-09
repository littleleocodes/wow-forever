# Beast-Marks Hunter — Raid (group)

[Hunter](../README.md) > [Raid (group)](README.md) > Beast-Marks

*Marksmanship's shots with Beast Mastery's pet talents: the classic raid hunter split.* (a hybrid: Beast Mastery/Marksmanship).

**[Beast-Marks — Raid](../research/raid/builds/beast-marks-open-raid.md)** (27/21/3) — [open the talent tree](https://talentsforever.com/hunter/60/552100050500022-00530503005-3-6)

> 🔬 Derived build: found by this project's open talent search (every legal build, no tree rule, in the community's raid simulator in a full raid, raced against the rotation's builds); it beat the hand-made build (mm-hawk-raid), which stays below as the alternative. A model of the beta, to check at launch.

**Other setups of this spec.** The spec's best build for each other setup, in a full raid:

- With a pet: [Beast Mastery / Marksmanship](../research/raid/builds/bm-mm-raid.md) (22/29/0), 806 DPS in a full raid — [open the talent tree](https://talentsforever.com/hunter/60/53200005041002-005355010150004--6)

## How to play

**Before the pull:** **Aspect of the Hawk**, **Aimed Shot**.

**Keep up all fight:** **Aspect of the Hawk**.

**Then press the first one that is ready**, top to bottom:

1. **Serpent Sting**: keep it on the target, when you have at least 30% mana
2. **Arcane Shot**
3. **Rapid Fire**
4. **Aimed Shot**

Between these, **Auto Shot** keeps firing on its own.

*The simulator's full rotation for this build, with every condition: [research rotation page](../research/raid/rotation.md).*

## Why this rotation

Beast-Marks puts Beast Mastery's pet talents on a Marksmanship shot core and plays the same short list as Beast Mastery: keep **Serpent Sting** up, fire **Arcane Shot** and **Aimed Shot** each time they are ready, and let **Auto Shot** and the pet do the rest.

**Why it works**

- **Serpent Sting** first so it never drops, 20% stronger with **Improved Stings**. Recast it only as it runs out (a new sting replaces the old one), and the full rotation does so only while you have 30% mana or more.
- **Arcane Shot** every time it is ready: 3 points in **Improved Arcane Shot** bring its cooldown to 5.1 seconds, about 34 casts in a 3-minute fight. **Summon Hawk** would share that timer, and in a full raid the simulator measured **Arcane Shot** as the better use of it, so this build skips the hawk.
- **Rapid Fire** (40% faster attacks for 15 seconds, 5-minute cooldown) once a fight, at the pull. The full rotation presses it just before an **Auto Shot** with **Aimed Shot** about to come off cooldown.
- **Aimed Shot** is listed last but goes out almost every time it can: a 2-second cast, then its 6-second cooldown. The simulator measured it slightly better below the instants; **Multi-Shot** shares its cooldown and never comes up on one target.
- The pet half: **Unleashed Fury** (+15% pet damage), **Ferocity** (+10% pet crit on top of your own crit, which Forever pets inherit), **Frenzy** and **Focused Fire** (+2% to you and the pet while it is out). There is no **Bestial Wrath** here, so there is nothing to time but **Rapid Fire**, trinkets and a potion.

**Caveats**

- Mana: the list assumes a full raid with Blessing of Wisdom and Mana Spring. With only your own buffs the simulator drops **Aimed Shot** (310 mana) and keeps **Arcane Shot** going above 10% mana, so **Aimed Shot** goes first when you run low.
- Keep the pet alive with **Mend Pet**: it is about a quarter of your damage and takes no stat buffs from players in Forever. A faster pet does more damage as modelled here (a 1.2-second cat over a 2.0-second pet; measured by players only at levels 20 and 30).
- Track the boss's creature type: **Improved Tracking** (3 points here) counts only against the tracked type.
- Moving: **Auto Shot** and **Aimed Shot** stop while you move; **Arcane Shot** and **Serpent Sting** are instant. The simulator starts **Aimed Shot** 2.5 seconds before the pull; in a real raid, wait for your tank.

**When to change it**

- Two or more targets close together: **Multi-Shot** instead of **Aimed Shot** on their shared cooldown (up to 3 targets for weapon damage each, against 166 extra on one). For a pack, **Volley**: a 6-second channel with no cooldown in Forever.
- In the last few seconds, skip the **Serpent Sting** refresh: its damage comes over 15 seconds.
- Inside 8 yards your shots and **Auto Shot** stop: step back out at once; the pet keeps attacking meanwhile.

## The numbers

| Setting | DPS |
|---|---|
| Full raid, 3-minute fight (every raid buff and debuff: what this page ranks on) | 855 |

**By gear tier** (the spec's best talents for each tier and setting in its own gear, found by this project's machine-learning search in the community simulator; [every spec](../../_reference/dps-rankings.md)):

| Gear | Full raid DPS | Best talents |
|---|---|---|
| Pre-BiS | 845 | [28/23/0](https://talentsforever.com/hunter/60/522020150510023-0053050200503--6) |
| Phase 1 BiS | 876 | [28/23/0](https://talentsforever.com/hunter/60/522010150510123-0053250000503--6) |

*From the search run of 2026-10-01; a new run is queued and will replace these numbers.*

**The gear** (average item level: Pre-BiS 62.8; Phase 1 BiS 65.6; each item opens its Wowhead page, with where it drops and its enchant):

| Slot | Pre-BiS | Phase 1 BiS |
|---|---|---|
| Head | [Black Dragonscale Helm](https://www.wowhead.com/forever/item=252605) · *Leatherworking*<br>+ [Lesser Arcanum of Voracity](https://www.wowhead.com/forever/item=11647) | [Black Dragonscale Helm](https://www.wowhead.com/forever/item=252605) · *Leatherworking*<br>+ [Lesser Arcanum of Voracity](https://www.wowhead.com/forever/item=11647) |
| Neck | [Mark of Fordring](https://www.wowhead.com/forever/item=15411) · *quest: In Dreams* | [Onyxia Tooth Pendant](https://www.wowhead.com/forever/item=18404) |
| Shoulders | [Theramore Pauldrons](https://www.wowhead.com/forever/item=271955) | [Giantstalker's Epaulets](https://www.wowhead.com/forever/item=16848) · *Sulfuron Harbinger, Molten Core* |
| Back | [Earthweave Cloak](https://www.wowhead.com/forever/item=21187)<br>+ [Enchant Cloak - Lesser Agility](https://www.wowhead.com/forever/spell=13364) | [Earthweave Cloak](https://www.wowhead.com/forever/item=21187)<br>+ [Enchant Cloak - Lesser Agility](https://www.wowhead.com/forever/spell=13364) |
| Chest | [Dawn Armor](https://www.wowhead.com/forever/item=252483) · *Leatherworking*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) | [Dawn Armor](https://www.wowhead.com/forever/item=252483) · *Leatherworking*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) |
| Wrist | [Forest Stalker's Bracers](https://www.wowhead.com/forever/item=19587)<br>+ [Enchant Bracer - Minor Agility](https://www.wowhead.com/forever/spell=7778) | [Giantstalker's Bracers](https://www.wowhead.com/forever/item=16850) · *Molten Core*<br>+ [Enchant Bracer - Minor Agility](https://www.wowhead.com/forever/spell=7778) |
| Hands | [Beaststalker's Gloves](https://www.wowhead.com/forever/item=16676) · *War Master Voone, Blackrock Spire*<br>+ [Enchant Gloves - Agility](https://www.wowhead.com/forever/spell=13823) | [Giantstalker's Gloves](https://www.wowhead.com/forever/item=16852) · *Shazzrah, Molten Core*<br>+ [Enchant Gloves - Agility](https://www.wowhead.com/forever/spell=13823) |
| Waist | [Warpwood Binding](https://www.wowhead.com/forever/item=18393) · *Tendris Warpwood, Dire Maul* | [Giantstalker's Belt](https://www.wowhead.com/forever/item=16851) · *Molten Core* |
| Legs | [Outrider's Chain Leggings](https://www.wowhead.com/forever/item=22673)<br>+ [Lesser Arcanum of Voracity](https://www.wowhead.com/forever/item=11647) | [Dragonstalker's Legguards](https://www.wowhead.com/forever/item=16938) · *Ragnaros, Molten Core*<br>+ [Lesser Arcanum of Voracity](https://www.wowhead.com/forever/item=11647) |
| Feet | [Sorcerer's Boots](https://www.wowhead.com/forever/item=22064)<br>+ [Enchant Boots - Greater Agility](https://www.wowhead.com/forever/spell=13823) | [Giantstalker's Boots](https://www.wowhead.com/forever/item=16849) · *Gehennas, Molten Core*<br>+ [Enchant Boots - Greater Agility](https://www.wowhead.com/forever/spell=13823) |
| Finger | [Signet Ring of the Bronze Dragonflight](https://www.wowhead.com/forever/item=21202) | [Ring of Spell Power](https://www.wowhead.com/forever/item=19147) · *Lucifron, Molten Core* |
| Finger | [Don Julio's Band](https://www.wowhead.com/forever/item=19325) | [Ring of Spell Power](https://www.wowhead.com/forever/item=19147) · *Lucifron, Molten Core* |
| Trinket | [Blackhand's Breadth](https://www.wowhead.com/forever/item=13965) | [Blackhand's Breadth](https://www.wowhead.com/forever/item=13965) |
| Trinket | [Royal Seal of Eldre'Thalas](https://www.wowhead.com/forever/item=18473) · *quest: The Greatest Race of Hunters* | [Royal Seal of Eldre'Thalas](https://www.wowhead.com/forever/item=18473) · *quest: The Greatest Race of Hunters* |
| Main hand | [Barbarous Blade](https://www.wowhead.com/forever/item=18520) · *King Gordok, Dire Maul*<br>+ [Enchant 2H Weapon - Superior Impact](https://www.wowhead.com/forever/spell=20030) | [Barbarous Blade](https://www.wowhead.com/forever/item=18520) · *King Gordok, Dire Maul*<br>+ [Enchant 2H Weapon - Superior Impact](https://www.wowhead.com/forever/spell=20030) |
| Ranged/relic | [Premier High Warlord's Recurve](https://www.wowhead.com/forever/item=272594)<br>+ [Biznicks 247x128 Accurascope](https://www.wowhead.com/forever/item=18283) | [Rhok'delar, Longbow of the Ancient Keepers](https://www.wowhead.com/forever/item=18713)<br>+ [Biznicks 247x128 Accurascope](https://www.wowhead.com/forever/item=18283) |

**Open in the simulator** (the community's Forever simulator on the web, loaded with the gear, enchants, talents, rotation, consumables and buffs we simulate): Pre-BiS: [full raid](https://elliotwood.github.io/Forever/forever/hunter/dps/#eJzMVU9oI2UUnzczybw+S5t+ae10UBkjSjo44cukI21FJu1JPIiCB0/aaZOaKbYJSQ4VL1UrSPFPvVQrhQq12EqFigoiCKIUUog0bVF32cLCbhd62ENuyx4WlpkmLZTdWwP7O73v/eH93u/7+B61I0RABR3iwIE9c3YSOQxCGl6DN2EMclCAOYBPABYBtBoiRiTtfVLwj1871ePHSMKfZ0nGw2qEFPx7HdT9sG/80qne7CAFP1oG9Q6Qgt99COr1DpLx6hf+8cufwK9WcHur4T9YB5Lx3hKQhJ9Nk4ybi37ilUVQTzpIIAUP9iPqtWgsgfNepOKpn3r69ysQP16FBRDnva9hzf0WttwNOBrZhtV1qADU4HNvlM7H/F180rYsbvGkze0k51bK5NxOcZtbnNs8VRHlmog3xD/D1E2ohUnG2g7EkMIkm0leop6Gd2MNYm2kUMi0EnaJLQF7yy28+3a+UNYtbr1gJrnJB4b1iZw78042o+eLupvJZDP6+Ht6OZfVi/myW/byM3op6xYncnq8lM3q49Nm0fUyZjNongYTU6X8TL82QAaLU9TowhAL/SWKGPKJkJgsUZfRiWEmviJoCoVISvKSH8L/777KVi4S40OmNXipxIaJswT1Gb0oMZzyG+/tgBaIwxOWfUZvvEEvxZ/VGllM1sRhgX3VevVsep4Z1GNEz9ULLpUnHkwwRBLu5dlL2otkMU7dBkOpWRhMwRNJUo3HUWJtP0DjRTQjdlB+q5dNtVx8PLvpi718Da0W9NpYA6ZrTz1Ey2Dyw25VOhErUBetDyQhQDy9AD0UpS4MR1CFfiFA3eEQ25TafFuYm0z3fbPsY9d5ejLAf45VF1VFd4yKKDxSKKebVkvx3I+X3mfon2q12j62nR5pONJj/ue+DF6+/vHuG/86Q4FXqDkjfma1ett5/dQ4cgwJf+sdfeL8Pz1dFC8HqyIHBZiFWXZ/AOx3SyY=); Phase 1 BiS: [full raid](https://elliotwood.github.io/Forever/forever/hunter/dps/#eJzMVU9IG2kUnzeTZD7fisYvuo7D7jKbZZc47IRvJs6iLstET8sell3ooafW0cRmpJqQ5GChB4sWivSPFPrHIlgQqUoLHloohUJpESJNMdb+gwqF1oKHHnIrvZUZEwVpbwb6O4SX93uP93u/b/g+rCcQBAkUiAAD+svuP55BJ8ThPzgMfZCCDIwBnAGYApDXCSFBQT6JIrl/p1Ha+g59ZOsCoI+UxgFF8mgepPWAG9xulN41oEiejoP00aWejYP0pgF9ZMOrXJoAt10k69X840tQ+RXIuWH0kcUpt/DVFEjbDcihSKYvgvQ6FI6SCSdYcKSzjnJjBiJbszAJ/IRzFebs63DTXoDNnmWYnYcCQAnOO724t+c9/kfTMJjOdJOZOtONmMaYGTNMxhgzWazA+0o8ecs/CGAzEjngLrYCYYIB9Gk6y2FLJbswB+E6FNGvGVEzRy8DPWJnjh9NZ/KKwYw/NJ1prKNbGUjZI8eSCSWdVexEIplQ+k8o+VRSyabzdt5Jjyi5pJ0dSCmRXDKp9A9rWdtJaFVS2yGjQ7n0SLvcgSqNYEhtIn7qf8jzxO8KQV7PYZPaSAKU/4eTRfSjoLOcS5GXn/6lM/uFsS7N6DxQYd3IaBTb1FYiUDLkDl5bAdkzh0UNc1def0VejP0qV6qoT+a7OXql9u6Z+DtVsUUN7bnnHSqLflmgHwWylqZ/yX+iQRk2q5QI1UZvCxbVUVK/JwKtW4LKF1FlTK/9fSsdqrn5ZPek989yPTRqMGthDqgi//QVL73NN5olYZsvQJk3Tgmch0h8ElowhE0kECQStHMeyhaD8KJQ58bc2GC87dq0i1Xr50EPLyyjzEuiYqkFnvumkI9Xo5rit1sHPqfrSbFYrO9bjvdUEvE+93afBiddPr166LnV5WW5ktXjVhaLH6z/d4JNSxXI3dbeH/bu052X4m/vrUhBBkZhlH4eAGIESoI=).

## Other builds of this spec

- [Beast-Marks — Raid](../research/raid/builds/beast-marks-ml-raid.md) (28/23/0, 833 DPS in a full raid) — [open the talent tree](https://talentsforever.com/hunter/60/532000150510123-0053250000503--6)
- [Marksmanship — Summon Hawk](../research/raid/builds/mm-hawk-raid.md) (22/29/0, 807 DPS in a full raid) — [open the talent tree](https://talentsforever.com/hunter/60/53200005051001-105355000150004--6)
- [Beast Mastery / Marksmanship](../research/raid/builds/bm-mm-raid.md) (22/29/0, 806 DPS in a full raid) — [open the talent tree](https://talentsforever.com/hunter/60/53200005041002-005355010150004--6)
- [Marksmanship raid DPS with a pet](../research/raid/builds/opt-mm-raid-raid-dps.md) (22/29/0, 806 DPS in a full raid) — [open the talent tree](https://talentsforever.com/hunter/60/53200005041002-005355010150004--6)

---
*Generated by `_reference/data/render_modes.py` on 2026-10-09 from this project's builds and simulations of the WoW: Forever beta (client build 1.60.1.70291). Simulations, not in-game measurements. Do not hand-edit.*

