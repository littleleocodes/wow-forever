# Survival Hunter — Raid (group)

[Hunter](../README.md) > [Raid (group)](README.md) > Survival

**[Melee Survival — Lone Wolf](../research/raid/builds/melee-survival-raid.md)** (5/11/35) — [open the talent tree](https://talentsforever.com/hunter/60/5-005005001-500230230250222151-12)

## How to play

**Setup, before the pull:** **Dismiss Pet**: **Lone Wolf** only works while you have no pet out.

**Before the pull:** **Hunter's Mark**.

**Keep up all fight:** **Aspect of the Beast**.

**Then press the first one that is ready**, top to bottom:

1. **Explosive Trap** when you have at least 60% mana, until the last 20 seconds of the fight
2. **Raptor Strike**; no global cooldown, so press it alongside the others
3. **Mongoose Bite** after you dodge
4. **Strider Kick**
5. **Immolation Trap**
6. **Wing Clip**

**Wing Clip** is your filler: cast it whenever nothing above is ready.

**Advanced: your cooldowns and extras.** Once the list above feels easy, add these:

- **Rapid Fire**: a cooldown, use it at the start of the fight and again whenever it is ready (about 1 time a fight)
- Use your trinkets and a potion together with your big cooldowns.

*The simulator's full rotation for this build, with every condition: [research rotation page](../research/raid/rotation.md).*

## Why this rotation

Melee Survival fights at the boss with two one-handers and no pet. **Raptor Strike** replaces a swing every 6 seconds, **Explosive Trap** goes down under the boss whenever its cooldown allows and you have the mana, **Mongoose Bite** goes whenever it lights up, **Strider Kick** on cooldown, and **Wing Clip** fills every other global cooldown.

**Why it works**

- **Hunter's Mark** before the pull is for **Expose Prey**: each of your hits on a marked target has a 10% chance to light up **Mongoose Bite** for 10 seconds. Otherwise **Mongoose Bite** lights up only after you dodge (not the boss), and in a raid the boss hits your tank, so nearly all your bites, about 39 a fight, come from **Expose Prey**. The mark lasts 2 minutes: put it back when it drops.
- **Aspect of the Beast** adds 110 melee attack power, and with **Deadly Aspects** each melee auto attack has a 10% chance to speed your swings by 30% for 12 seconds. **Rapid Fire** speeds up melee too in Forever (40% for 15 seconds): press it at the pull.
- **Raptor Strike** is first and never waits: it replaces your next main-hand swing and costs no global cooldown, so queue it every time its 6-second cooldown ends.
- **Mongoose Bite** next, as soon as it lights up: weapon damage plus 57, and **Lacerating Strikes** adds a bleed worth 40% of the bite over 21 seconds. Using it at once frees its 5-second cooldown for the next one.
- **Explosive Trap** now sits at the top of the list while you have 60% mana or more and 20 seconds of the fight left: traps work in combat in Forever but land at your own feet, so standing at the boss puts it under the boss, 30% stronger with **Clever Traps**. The 2026-11-10 search measured the move to the top about 0.6% better in a full raid, and the mana and time guards about 0.2% each. Below 60% mana the shared fire-trap cooldown goes to **Immolation Trap**. **Strider Kick** (full weapon damage, 8-second cooldown) goes on cooldown.
- **Wing Clip** is the filler. Its own hit is small (50 damage), but every hit on your marked target is another chance at **Mongoose Bite**, and the simulator measured about 10% more damage in a full raid with **Wing Clip** in every empty global cooldown.

**Caveats**

- No pet: **Lone Wolf**'s 20% needs no active pet, so **Dismiss Pet** before the pull. Track the boss's creature type too: **Improved Tracking** adds 5% only against the type you are tracking.
- Mana: **Resourcefulness** cuts the cost of traps and melee abilities by 60%, and in a full raid that is enough. With only your own buffs the hunter runs short; then spend the mana on **Mongoose Bite**, **Strider Kick** and the trap before **Wing Clip**.
- Blizzard's notes say **Expose Prey** works on the target of your own **Hunter's Mark**. With several hunters in the raid, make sure the mark on the boss is yours (the simulator accepts any).
- **Explosive Trap** and **Immolation Trap** share the fire-trap cooldown. The list gives it to **Explosive Trap** above 60% mana and to **Immolation Trap** below; on a long fight with a raid's mana that is mostly **Explosive Trap**.
- Watch your ranks: in the beta client (build 70753) the top ranks are the strongest. **Hunter's Mark** rank 4 gives +143 ranged attack power (rank 3 +98) and **Aspect of the Beast** rank 4 +110 melee attack power (rank 3 +90). Cast the highest rank you have.

**When to change it**

- Adds around you: keep **Explosive Trap** going even below 60% mana while they live; it hits everything within 10 yards.
- When you must leave the boss, make **Strider Kick** your last hit: it adds 30% movement speed for 3 seconds.
- If you pull threat, **Feign Death** (30-second cooldown; **Survival Tactics** makes it more likely to land).
- The list stops placing **Explosive Trap** in the last 20 seconds, when most of its damage would come after the boss dies.

## Talents

| Tree | Points | Talents (ranks) |
|---|---|---|
| Beast Mastery | 5 | Deadly Aspects 5 |
| Marksmanship | 11 | Lethal Attacks 5, Careful Aim 5, Lone Wolf 1 |
| Survival | 35 | Improved Tracking 5, Savage Strikes 2, Survivalist 3, Clever Traps 2, Surefooted 3, Survival Tactics 2, Predator's Edge 5, Resourcefulness 2, Expose Prey 2, Survivalist's Discipline 2, Strider Kick 1, Lightning Reflexes 5, Lacerating Strikes 1 |

## The numbers

| Setting | DPS |
|---|---|
| Full raid, 3-minute fight (every raid buff and debuff: what this page ranks on) | 737 |

**By gear tier** (the spec's best talents for each tier and setting in its own gear, found by this project's machine-learning search in the community simulator, wowsims/forever 2e6e77d (client 70938); [every spec](../../_reference/dps-rankings.md)):

| Gear | Full raid DPS | Best talents |
|---|---|---|
| Quests and dungeons | 672 | [7/11/33](https://talentsforever.com/hunter/60/52-005005001-500230230250022151-12) |
| Pre-BiS | 764 | [7/11/33](https://talentsforever.com/hunter/60/52-005005001-500230230250022151-12) |
| Raid BiS | 742 | [5/12/34](https://talentsforever.com/hunter/60/5-005015001-503210230250022151-12) (as good as this build in this gear) |

*Each row is in that tier's own gear set; the DPS at the top of the page is this build in the standard set, so the two do not match.*

**The gear** (average item level: Quests and dungeons 61.5; Pre-BiS 62.5; Raid BiS 64.3; each item opens its Wowhead page, with where it drops and its enchant):

| Slot | Quests and dungeons | Pre-BiS | Raid BiS |
|---|---|---|---|
| Head | [Backwood Helm](https://www.wowhead.com/forever/item=18421) · *quest: The Treasure of the Shen'dralar*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11647) | [Black Dragonscale Helm](https://www.wowhead.com/forever/item=252605) · *Leatherworking*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11647) | [Black Dragonscale Helm](https://www.wowhead.com/forever/item=252605) · *Leatherworking*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11647) |
| Neck | [Mark of Fordring](https://www.wowhead.com/forever/item=15411) · *quest: In Dreams* | [Mark of Fordring](https://www.wowhead.com/forever/item=15411) · *quest: In Dreams* | [Onyxia Tooth Pendant](https://www.wowhead.com/forever/item=18404) · *quest: For All To See* |
| Shoulders | [Death's Clutch](https://www.wowhead.com/forever/item=14503) · *Ras Frostwhisper, Scholomance* | [Theramore Pauldrons](https://www.wowhead.com/forever/item=271955) | [Theramore Pauldrons](https://www.wowhead.com/forever/item=271955) |
| Back | [Cape of the Black Baron](https://www.wowhead.com/forever/item=13340) · *Baron Rivendare, Stratholme*<br>+ [Enchant Cloak - Lesser Agility](https://www.wowhead.com/forever/spell=13364) | [Cape of the Black Baron](https://www.wowhead.com/forever/item=13340) · *Baron Rivendare, Stratholme*<br>+ [Enchant Cloak - Lesser Agility](https://www.wowhead.com/forever/spell=13364) | [Howler's Furs](https://www.wowhead.com/forever/item=272414) · *sold by Pix Xizzix*<br>+ [Enchant Cloak - Lesser Agility](https://www.wowhead.com/forever/spell=13364) |
| Chest | [Savage Gladiator Chain](https://www.wowhead.com/forever/item=11726) · *Gorosh the Dervish, Blackrock Depths*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) | [Dawn Armor](https://www.wowhead.com/forever/item=252483) · *Leatherworking*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) | [Dawn Armor](https://www.wowhead.com/forever/item=252483) · *Leatherworking*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) |
| Wrist | [Bracers of the Eclipse](https://www.wowhead.com/forever/item=18375) · *Prince Tortheldrin, Dire Maul*<br>+ [Enchant Bracer - Superior Strength](https://www.wowhead.com/forever/spell=19984) | [Bracers of the Eclipse](https://www.wowhead.com/forever/item=18375) · *Prince Tortheldrin, Dire Maul*<br>+ [Enchant Bracer - Superior Strength](https://www.wowhead.com/forever/spell=19984) | [Bracers of the Eclipse](https://www.wowhead.com/forever/item=18375) · *Prince Tortheldrin, Dire Maul*<br>+ [Enchant Bracer - Superior Strength](https://www.wowhead.com/forever/spell=19984) |
| Hands | [Gordok's Gloves](https://www.wowhead.com/forever/item=18368) · *quest: Unfinished Gordok Business*<br>+ [Enchant Gloves - Agility](https://www.wowhead.com/forever/item=273520) | [Theramore Gloves](https://www.wowhead.com/forever/item=271948)<br>+ [Enchant Gloves - Agility](https://www.wowhead.com/forever/item=273520) | [Theramore Gloves](https://www.wowhead.com/forever/item=271948)<br>+ [Enchant Gloves - Agility](https://www.wowhead.com/forever/item=273520) |
| Waist | [Marksman's Girdle](https://www.wowhead.com/forever/item=22232) · *Urok Doomhowl, Blackrock Spire* | [Highlander's Chain Girdle](https://www.wowhead.com/forever/item=20043) · *sold by Samuel Hawke* | [Highlander's Chain Girdle](https://www.wowhead.com/forever/item=20043) · *sold by Samuel Hawke* |
| Legs | [Legguards of the Chromatic Defier](https://www.wowhead.com/forever/item=12903) · *quest: Legplates of the Chromatic Defier*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11647) | [Plaguehound Leggings](https://www.wowhead.com/forever/item=18736) · *Stratholme*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11647) | [Plaguehound Leggings](https://www.wowhead.com/forever/item=18736) · *Stratholme*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11647) |
| Feet | [Windreaver Greaves](https://www.wowhead.com/forever/item=13967) · *Kirtonos the Herald, Scholomance*<br>+ [Enchant Boots - Greater Agility](https://www.wowhead.com/forever/item=16245) | [Windreaver Greaves](https://www.wowhead.com/forever/item=13967) · *Kirtonos the Herald, Scholomance*<br>+ [Enchant Boots - Greater Agility](https://www.wowhead.com/forever/item=16245) | [Windreaver Greaves](https://www.wowhead.com/forever/item=13967) · *Kirtonos the Herald, Scholomance*<br>+ [Enchant Boots - Greater Agility](https://www.wowhead.com/forever/item=16245) |
| Finger | [Tracker's Signet of Ferocity](https://www.wowhead.com/forever/item=275972) | [Warden's Signet of Ferocity](https://www.wowhead.com/forever/item=275981) | [Quick Strike Ring](https://www.wowhead.com/forever/item=18821) · *Magmadar, Molten Core* |
| Finger | [Tarnished Elven Ring](https://www.wowhead.com/forever/item=18500) · *Tribute, Dire Maul* | [Cutthroat's Signet](https://www.wowhead.com/forever/item=272408) · *sold by Pix Xizzix* | [Warden's Signet of Ferocity](https://www.wowhead.com/forever/item=275981) |
| Trinket | [Blackhand's Breadth](https://www.wowhead.com/forever/item=13965) · *quest: For The Horde!* | [Blackhand's Breadth](https://www.wowhead.com/forever/item=13965) · *quest: For The Horde!* | [Blackhand's Breadth](https://www.wowhead.com/forever/item=13965) · *quest: For The Horde!* |
| Trinket | [Hand of Justice](https://www.wowhead.com/forever/item=11815) · *Emperor Dagran Thaurissan, Blackrock Depths* | [Hand of Justice](https://www.wowhead.com/forever/item=11815) · *Emperor Dagran Thaurissan, Blackrock Depths* | [Hand of Justice](https://www.wowhead.com/forever/item=11815) · *Emperor Dagran Thaurissan, Blackrock Depths* |
| Main hand | [Bonescraper](https://www.wowhead.com/forever/item=13368) · *Baron Rivendare, Stratholme*<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) | [Ironwood Blade](https://www.wowhead.com/forever/item=279259) · *Blacksmithing*<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) | [Blackguard](https://www.wowhead.com/forever/item=19168) · *Blacksmithing*<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) |
| Off hand | [Distracting Dagger](https://www.wowhead.com/forever/item=18392) · *Prince Tortheldrin, Dire Maul*<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) | [Heartseeker](https://www.wowhead.com/forever/item=12783) · *Blacksmithing*<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) | [Ironwood Blade](https://www.wowhead.com/forever/item=279259) · *Blacksmithing*<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) |
| Ranged/relic | [Satyr's Bow](https://www.wowhead.com/forever/item=18323) · *Zevrim Thornhoof, Dire Maul* | [Satyr's Bow](https://www.wowhead.com/forever/item=18323) · *Zevrim Thornhoof, Dire Maul* | [Rhok'delar, Longbow of the Ancient Keepers](https://www.wowhead.com/forever/item=18713) |

**Open in the simulator** (the community's Forever simulator on the web, loaded with the gear, enchants, talents, rotation, consumables and buffs we simulate): Quests and dungeons: [full raid](https://wowsims.com/forever/hunter/dps/#eJzEVEFIFGEU3vfPOPv2abb9BI5D0J+QbMLE7MiKetnRU3Qo6SQUtKM7NlvqbO4eNroYeCgxN4oOimBgYUR28SIS1CHILlEXkyiyEupg0EGROkTMrLtEXZU+HsM338f73/cujw4gREEFATFIgQtZGAa4CnAH4D4Arwlc5rutoG1VIUYlrUBh3CyCulZNEs4XSMLZi6TglKu+VkjBl6fVz7UUxudFUN/75GkR1A+1JOPKHJCCX9J+p4LFgZI6sh4lGZ/dAJLw+oD/2hlScMFV1/3mlSL4RMZbRWjQo0uZ2No0dC2PQ/dGahTYSGYSIjP2Q/tdx/Q9eADhsczsFIxnVmEk04lBerBgkR1MmLphJIKK6wnDMJuD8pkZT8SXmPyK4Se2IRGnsFZFEm56DWGqIklvzvHbwFN2tv+sl80L0zBb9LihN8fbRa9rD55z0sIbEnY67aRFzyWRdx0x5OXtfMYbFDnHHup1RSznOGLA6XccPZ3N6WVbL9lHz+e8wSNanGK8kfY17UWFs56QFkxvMQ6XpePbkmnkgoDfPF6tRXxNAC56vF6roz1vFSIZt2ZPchaVNWWbyxprD3HSMFAezQCPaKUtn3gV+dp8F7/8757GTu9ZSfnmx4lKSp+XM330+IW/chhtutm2wzlKwx57qvSVLcF3Zl6RQgH2W6NQQ0SIkzch+nMMGn6xiG+Ehvus+skJHy+Sh/oCLCfNVabKItm0wEL/BXmrzHYVjXO7Nqct+J66a3VsC1bKP0ITEPyEVpNNEi7Udf5xqwxoBQuOQRd0gwtZKECB/R4AvV3p8Q==); Pre-BiS: [full raid](https://wowsims.com/forever/hunter/dps/#eJzEVE9IFHEU3vebcebt03QcAsch6JeQbMLE7MiKetnRU3Qo6eQhaEd3bLfUWdw9GF4MDEr8A0aQIhhYGFERWCBSdOiQkQcjMOgPWXnoYNTBiDxEzKy7RF2VPh4z33wfw/u+y6N9CApowCECCUhBBgYBLgJcA7gJoJYFLvPdRtC3ShAVQR8gGR89qNDWS0nA+X4S8eWyQhJOp7QXEsn45H6F9qmcZHw6Dto7nywvK9r7chLx+TSQjPcmwP9ZwvGevDy6oZCIV1cUEnC0hwScO0kyvrlQqW2Uk4RfO/23iJfHocZQltKR9RloWx2D9s3EMLCh9BSEZ53bztuWmRtwC+SR9Nw0jKXXYCjdikEBsGGR7Y9ZhmnGgokaMdO06oPxmRWNRZeYuMLwI9sUSCVZLyEBv3s1MpWQYNRn1SugJpxM9ykvk+OWaTUYUdOojzbzzpTTe9pNcq+PO8mkm+Qd53gu5fI+L+fk0l4vz7pOX2eKR7Kuy3vcbtc1kpmsUbCNvH34TNbrPaRHKaLWUmVdBUoq6wjpwfYG82BBOrotWWY2CPjFU0v1sK9xwEVPrdaraM9riUjEH3PHVaaIurTNRZ01h1TSMVDuzoIa1vMtH3tF+dJ8mzrwb09zp3sWU776eayY0ueFTB889exfOcwmw2ra4Rz5ZQ89TfjMluAbs84LoQB77WEoIyLEqQlQtkag5hcL+0ZosMuunpr08Sx+oCvAatxaY5rI43ULLPRfkLMLbFdRe2fX9jQFzxPX7ZZtwU74d2gSgo/QWrxOwIWq1j/OlQmNYMMRaIN2SEEG+qGf/R4A4uHrgw==); Raid BiS: [full raid](https://wowsims.com/forever/hunter/dps/#eJzEVE9IFH0Y3vc34867r346Dh84Dh8fk5BswsRvZllRLzt6ig4lnTwE7eiO7ZY6i7sHIwgDhRL/gOFBkQwsjKgIKhApOnTIyIMRGPSHtvLQwaCDEUVEzKwrUVel5zA88zy8v/d5Li/9hyCDCjpEIQlpyMIgwDmASwBXAZSKwGW+2wTa9zJEWdDOkIT371ap6+Uk4voEkIjPVmSS8OKqrD4Nk4QP71Sp7ytJwkcToL72ycqKrL6pJBGfzAJJeGsS/PEwTvQW5eEL/jNjGzIJONZLAi4cJQkLU6Bu+OMvh6t9IuL0JNQZ8nImuj4H7Wvj0LGZHAE2lJmByLxz3XnVOncFroE0mlmYhfFMAYYybRh0ABuW2P9xg/M4N+Ocm0acxyyTWzFuxTm3LDNuLjNxleE7timQQpJWRgJ+9uokKiPBiOWUKVCSTrbnmJfN6xa3Gg2TGzGzRe9KO33H3ZTu9etOKuWm9M5Tej7t6v1e3slnvD495zr9XWk9mnNdvdftcV0jlc0ZJdso2vtP5Ly+fZpJUaWeqhuqMKywzpAWbG/ke0vSwS3J4rkg4EdPKdcivqYDLnlKrVZD/7wIE4n4ZeGwwmRRC29xUWMtIYU0DJSb86BEtGLLB962fP52u3L6z558p3tup3z+9dB2Sp+XMr31lJO/5eDNhtW8wzmKy+55qvCBLcMnZp0VQgH+tUeggogQZyZB/jYKdT9YxDdCg9127cy0j8eJPd0B1hJWgaminmhYZKG/grxdYruK+hu7tqc5+B65bLduCXbSv0TTEPyECokGARdr2n45WByawIYD0A4dkIYsDMAA+zkA4bHr6w==).

## Other builds of this spec

- [Survival — Raid](../research/raid/builds/survival-raid.md) (5/16/30, 711 DPS in a full raid) — [open the talent tree](https://talentsforever.com/hunter/60/5-005055001-50023023005022213-12)
- [Survival (optimized)](../research/raid/builds/opt-melee-dps-raid-dps.md) (5/15/31, 694 DPS in a full raid) — [open the talent tree](https://talentsforever.com/hunter/60/5-005045001-500250030050220151-12)
- [Survival — Melee](../research/raid/builds/survival-melee.md) (9/11/31) — [open the talent tree](https://talentsforever.com/hunter/60/522-005015-500230131050220151-12)

---
*Generated by `_reference/data/render_modes.py` on 2026-11-19 from this project's builds and simulations of the WoW: Forever beta (talent and spell data: client build 1.60.1.70753; raid numbers: the official wowsims/forever simulator at 2e6e77d (client 1.60.1.70938)). Simulations, not in-game measurements. Do not hand-edit.*

