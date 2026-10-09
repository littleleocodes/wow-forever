# Fury Warrior — Raid (group)

[Warrior](../README.md) > [Raid (group)](README.md) > Fury

**[Fury — Raid](../research/raid/builds/fury-open-raid.md)** (18/31/2) — [open the talent tree](https://talentsforever.com/warrior/60/04305013002-05053035102010501-2-6)

> 🔬 Derived build: found by this project's open talent search (every legal build, no tree rule, in the community's raid simulator in a full raid, raced against the rotation's builds); it beat the hand-made build (fury-dw-raid), which stays below as the alternative. A model of the beta, to check at launch.

**Other weapons and stances.** This build is the Dual-wield setup. The spec's best build for each other setup, in a full raid:

- Two-handed: [Two-handed Arms/raid or leveling](../research/raid/builds/opt-arms-2h-raid-raid-dps.md) (20/31/0), 898 DPS in a full raid — [open the talent tree](https://talentsforever.com/warrior/60/03305013032-05250030052210501--6)

## How to play

**Then press the first one that is ready**, top to bottom:

1. **Bloodthirst**
2. **Death Wish**: a big cooldown, use it at the start of the fight and again whenever it is ready
3. **Whirlwind**
4. **Execute** when the target is below 20% health
5. **Hamstring**
6. **Bloodrage**
7. **Heroic Strike**

**Heroic Strike** is your filler: cast it whenever nothing above is ready.

**Advanced: your cooldowns and extras.** Once the list above feels easy, add these:

- **Recklessness**: a cooldown, use it at the start of the fight and again whenever it is ready (about 1 time a fight)
- Use your trinkets, your racial and a potion together with your big cooldowns.

*The simulator's full rotation for this build, with every condition: [research rotation page](../research/raid/rotation.md).*

## Why this rotation

Fury in a raid fights in **Berserker Stance** with a weapon in each hand: **Bloodthirst** and **Whirlwind** on cooldown, **Execute** in the gaps below 20%, **Hamstring** in the short gaps and **Heroic Strike** only when rage piles up. **Death Wish** and **Recklessness** wait for the last 45 seconds.

**Why it works**

- **Bloodthirst** (30 rage, 6-second cooldown) and **Whirlwind** (25 rage, 22 with **Raging Blows**, 10-second cooldown) are your main attacks: press them the moment they are ready. **Whirlwind** now always hits with both weapons, and it needs **Berserker Stance**, the stance this list never leaves.
- Below 20%, **Execute** still comes after **Bloodthirst** and **Whirlwind**. It spends all your rage (600 damage plus 15 per extra rage point; 10 rage to cast with **Improved Execute**), so it takes the global cooldowns between them; a full raid gives you enough rage that the simulator measured this order slightly better.
- **Death Wish** (+20% physical damage for 30 seconds, 3-minute cooldown) and **Recklessness** (+100% crit chance for 15 seconds) wait until about 45 seconds are left, so they cover the execute phase; the line above that says to use **Death Wish** at the start does not match the rotation. Crits give double rage in Forever, so the **Recklessness** window also feeds bigger **Execute** hits. The simulator measured 0.7% more damage with **Death Wish** at 45 seconds than at 30, and in fights longer than about 3.5 minutes it presses it at the pull as well.
- **Hamstring** (10 rage) fills a global cooldown only when **Bloodthirst** is more than a second away and **Whirlwind** more than 1.5 seconds: it is a cheap extra main-hand hit that can trigger on-hit effects such as a shaman's Windfury Totem, but it must never delay your main attacks. The simulator measured 1.9% more damage with this rule than with **Hamstring** only above 80 rage.
- **Heroic Strike** is a rage dump, not a filler: queue it only at 67 rage or more on a single target. It replaces a white swing, and white swings are your steady rage (each gives rage in proportion to your weapon's speed, double on a crit), so an early one starves **Bloodthirst** and **Whirlwind**; in Forever it also no longer helps your off-hand hit. The simulator measured 0.9% more damage at 67 rage than at 45.
- **Bloodrage** waits until you are under about 22 rage, so it refills an empty bar instead of topping up a full one. The simulator measured 1% more damage than pressing it whenever you are under 90.

**Caveats**

- The page's numbers assume a **Recklessness** in every fight and two Mighty Rage Potions (one early, one in the last 30 seconds). **Recklessness** has a 30-minute cooldown, so you will not have it on every boss: the simulator measured 11% more damage with it than without.
- With several targets, **Whirlwind** hits up to 4 of them, and above 40 rage **Cleave** replaces **Heroic Strike** (the full list does this).
- The simulator ignores threat. **Heroic Strike** causes a high amount of threat, so it is the first thing to stop if you pull aggro. **Death Wish** and **Recklessness** also make you take 5% and 20% more damage.
- Stand behind the boss: from the front it can parry and block, and a swing that does not land gives you no rage.

**When to change it**

- Alone or in a small group (fewer buffs, less rage), put **Execute** first below 20%, stack **Sunder Armor** to 5 yourself and skip **Hamstring**. That is the simulator's rotation for a warrior alone on a training dummy, where stacking **Sunder Armor** was worth 12%.
- If nobody in your group has **Battle Shout** up, keep it up yourself (3 minutes), and put one **Sunder Armor** on a boss that has none: the list leaves both out because the simulator's raid already had them.
- Before a boss's fear, press **Berserker Rage** (30-second cooldown, 10 seconds of fear immunity); **Death Wish** also makes you immune. The simulator's boss never fears, so the list leaves it out.
- With a two-hander (the page's two-handed option), drop **Heroic Strike** and cast **Hamstring** whenever nothing else is ready: in the simulator's two-handed raid rotation those two changes were worth 5.4% and 6.6%. That rotation also uses **Bloodrage** under 90 rage and puts **Whirlwind** before **Bloodthirst** when **Bloodthirst** is more than 1.5 seconds away.

## The numbers

| Setting | DPS |
|---|---|
| Full raid, 3-minute fight (every raid buff and debuff: what this page ranks on) | 925 |

**By gear tier** (the spec's best talents for each tier and setting in its own gear, found by this project's machine-learning search in the community simulator; [every spec](../../_reference/dps-rankings.md)):

| Gear | Full raid DPS | Best talents |
|---|---|---|
| Pre-BiS | 705 | [13/38/0](https://talentsforever.com/warrior/60/20305012-25050005152010501--6) |
| Phase 1 BiS | 723 | [13/38/0](https://talentsforever.com/warrior/60/20305012-25050005152010501--6) |

**The gear** (average item level: Pre-BiS 62.9; Phase 1 BiS 65.4; each item opens its Wowhead page, with where it drops and its enchant):

| Slot | Pre-BiS | Phase 1 BiS |
|---|---|---|
| Head | [Lionheart Helm](https://www.wowhead.com/forever/item=12640) · *Blacksmithing* | [Lionheart Helm](https://www.wowhead.com/forever/item=12640) · *Blacksmithing* |
| Neck | [Mark of Fordring](https://www.wowhead.com/forever/item=15411) · *quest: In Dreams* | [Onyxia Tooth Pendant](https://www.wowhead.com/forever/item=18404) |
| Shoulders | [Truestrike Shoulders](https://www.wowhead.com/forever/item=12927) · *Pyroguard Emberseer, Blackrock Spire* | [Truestrike Shoulders](https://www.wowhead.com/forever/item=12927) · *Pyroguard Emberseer, Blackrock Spire* |
| Back | [Howler's Furs](https://www.wowhead.com/forever/item=272414) | [Howler's Furs](https://www.wowhead.com/forever/item=272414) |
| Chest | [Timbermaw Tunic](https://www.wowhead.com/forever/item=252484) · *Leatherworking* | [Timbermaw Tunic](https://www.wowhead.com/forever/item=252484) · *Leatherworking* |
| Wrist | [Deeprock Bracers](https://www.wowhead.com/forever/item=21184) | [Deeprock Bracers](https://www.wowhead.com/forever/item=21184) |
| Hands | [Theramore Gauntlets](https://www.wowhead.com/forever/item=271940) | [Flameguard Gauntlets](https://www.wowhead.com/forever/item=19143) · *Molten Core* |
| Waist | [Radiant Girdle of the Dawn](https://www.wowhead.com/forever/item=227814) | [Onslaught Girdle](https://www.wowhead.com/forever/item=19137) · *Ragnaros, Molten Core* |
| Legs | [Titanic Leggings](https://www.wowhead.com/forever/item=22385) · *Blacksmithing* | [Titanic Leggings](https://www.wowhead.com/forever/item=22385) · *Blacksmithing* |
| Feet | [Boots of Heroism](https://www.wowhead.com/forever/item=21995) | [Boots of Heroism](https://www.wowhead.com/forever/item=21995) |
| Finger | [Don Julio's Band](https://www.wowhead.com/forever/item=19325) | [Quick Strike Ring](https://www.wowhead.com/forever/item=18821) · *Magmadar, Molten Core* |
| Finger | [Don Julio's Band](https://www.wowhead.com/forever/item=19325) | [Band of Accuria](https://www.wowhead.com/forever/item=17063) · *Ragnaros, Molten Core* |
| Trinket | [Hand of Justice](https://www.wowhead.com/forever/item=11815) · *Emperor Dagran Thaurissan, Blackrock Depths* | [Hand of Justice](https://www.wowhead.com/forever/item=11815) · *Emperor Dagran Thaurissan, Blackrock Depths* |
| Trinket | [Blackhand's Breadth](https://www.wowhead.com/forever/item=13965) | [Blackhand's Breadth](https://www.wowhead.com/forever/item=13965) |
| Main hand | [Premier High Warlord's Blade](https://www.wowhead.com/forever/item=272452) | [Brutality Blade](https://www.wowhead.com/forever/item=18832) · *Garr, Molten Core* |
| Off hand | [Premier High Warlord's Cleaver](https://www.wowhead.com/forever/item=272592) | [Premier High Warlord's Blade](https://www.wowhead.com/forever/item=272452) |
| Ranged/relic | [Premier High Warlord's Recurve](https://www.wowhead.com/forever/item=272594) | [Striker's Mark](https://www.wowhead.com/forever/item=17069) · *Magmadar, Molten Core* |

**Open in the simulator** (the community's Forever simulator on the web, loaded with the gear, enchants, talents, rotation, consumables and buffs we simulate): Pre-BiS: [full raid](https://elliotwood.github.io/Forever/forever/warrior/dps/#eJzMVl9oW2UUz7l/ktPTtLv92tH0i45rFU2vpH73Jnc2E7zpQPAPoqLgGIK9a1IT0abkRuzAh00QBP9QX4ar4KpSrPUPcw6VIUNUtJMUWsGBsgcZosJ8qPgmyuS7SRbI+hTm8Dx8nJzzO/f3OycnuR/FEQxIgAkpEMCuv/RJETABebgf9sEUlGAODgE8D7AAwL+Jo2YA90nFnw6Qih/Nk4oXC6Th6xsGafjVyR2k4efLIP26jPzyZx9p+McHMnLhXXn+c6R1qvj2I6TiS09KdFi/sSnP7zaN0V3G1+XEi+XUz8fgVXjLX4L3/BX4cfI4HFuGNYC91BZ/Skk6IiNcYTtpxxWuECLj2q6TsYVw7TVFO69sEcvz2ynDbEpaI6iy/i+gl/SUjuv7mWLoXCeVwCY2alD/iWbq9MNhKtbC9fCYxBlHHmTEkUdJMzZfAfYasGl/7olHK3M10xHO7rQt0sLZY06X/NnHigWzUjX9QqFYMA8cNGulolmt1PxauTJrBkW/Ol0yU0GxaM48VT2YLjydrvrlQrqFSDcQ448HldkxnqWb+RgNWDtQY8rdER4jndSsG9CQxTAahoiQoo5tj7uBVIorU2wXAuedVXYz/0kfy3CbxvhNnQhHBMQso/lcpChpdlYEXCMlMcBu5e52YhxxmRg7G4qJkobnloBdy5OdRbtFIEeJF04Dc3lmOzGZbcRkGmXGZ8vdlOGbv3bFdvhk12XPXJ0t2dmpK+sGeyLh4A2rH3WmnodIc90lwARc6GODfID0bxUFQSpP6fjxG9Bacvxwpe2//Pd9LM4pRGl49hSwF67S+t9AI9Yw6qx3FS6RS3mkiKDdyCT3yGa3XN4rJflIGI0ypRppFGZFq2kiNCGl4w9LwPbzfXQvuyf8o+iga/wOxt2AuJVAndEqtJib37jMSRa9zTIhpLyUius59mznsEQu7Uxc+WElw1VUQxGhMMcZd+Uk8OIQuwuB30G3sVzXLcrG8MsFYMN8J8VHifAEyIcvDoYci4MJ9TdlDbYU57AaCW0ov6r0Ug/FDFXAxF8w+o7aI+ORQzP5kcWj0s54182EdtZztpREzPSsNSXyv7JavuX9p3bj+1ecJ7der9fjU8fzk81Afkq+049CubL13JmHvvdyYTSy4U1KZL3+u/dAwznnWSp+Orz3mvYLt3E/uDO8IZRgDuZhnv07ADfbcD0=) · [training dummy](https://elliotwood.github.io/Forever/forever/warrior/dps/#eJzMVF9oHNUXnjt/NjcnTTO9zY8mN7+Wa8C62brpndlMk00fNon0QUVE6oMUwUwyk+5ourPMHbF9s6Dig5X6EmwEG5VgjH+otagEEVEbEtlAorSg9EGKqFAfIr6JotzZ3aTG4EOowfswHM6c851zv/OdCwpR6Fcm1k1EXdDwtyOg4fdOgob/8EDHLy+boOPPL7WAjj+ZRtKuSM/3vzSDjn9+R3puvCm/v0/Uvxp+/WHQ8JkTMjrJX16R3y9XzM595nzQ9lyQ/u48ehG95k6ht9wZ9M3gBXR+Gi0gNKTMqR2WleMOt+ys5VgO5zznWI6dszh3rAVVv64+00JeQmTULY8/EpZjZnP7UNbiWW73s9GiWzrueyyMmOt5vsdGTrG46LMojN04CEtM+G40WmRp4fts7PHoVNZ7Ihu5gZetR2SrEd2PirDURXvgAO2CXZkWrBP1HoU2gAFajyOgNUNwKnEBYEjZltXtCGqAhmeGyW66C4wvVBUjiiGVNvD7ryByBZF5lPTK81k738+GxsPQi4tBJGIW+SIOI99jabfEfDcaD/yo3qsXheWy77EgZskFfE+wuOjGTBRdmXIiFDELYj9K+hfMLXnMsjkTbCw4XozFYTbijj7G3JjFxUAwUQ5lOAsEO2B3526XoG6JBSXPL/slzy/FSQ0Zb/VxJu5kNuec31Shi0JyLx1fnUPkqW0axd6Ec32d81yuu7fG+QfNpJE2SNOcOEqAYpoC3Vx5AZFWSqARGsAYc8eFXw/ehxGlG8dqrYPlqAVd9I6NETYXQDJmbfAYUqBbPVxQHdS2XaSXOpupxeZ/U4vVk6glBTq+NoXIXtqxMekQF/IK+MbHiDg0t1kzuU2ayVXTzI+mt5KGX/1hS9VOX9py2sQ2iedgMplNBZTwmlrntZeLfoWUN/Qld7bv1vfVKGfJED7bXFctfncGrdnP/3Y/SdP90JFpxwZpmkVra1fjUspoDWFum8g8CkfIXWBmdmJEtOtIkVsDyIL/13YqRdSoRqZl89pLuJFmuTcAmKE0xvOXERmkBbDIwQTW+AtsB21PvFXYFOig9tRRaxAG/noKkWP0IbiP3PuPbAHNtGGDwCyq03bTP1nFWK/Sx2WraQ0v5cndGNEjcJjkt4wuMfFnZ6vr3tLZDE0Xk3Gm8OLlBKJqkTNoe6RXVZVGdn6KmsBIG3jpGFFNozpMJ7l54ttD/wc7OgHwRSRfz8ndMgJP7m7TflQX0Kpqn9aU5LQOzKpN8rE1NY76fkWdb2iN0q88OTbQPnlOnsXCbWPJuVqwV9W2BlbILKjKf+rEA3XrXz37377ldfJLlUplx/CFgcGaY2AYPYvQORSEq08vPnilkE+8ynJhUEZWKj8VHqga1woZDX+4Z0g5Sf4cAOqkAho=); Phase 1 BiS: [full raid](https://elliotwood.github.io/Forever/forever/warrior/dps/#eJzMVl9oW2UUz7l/ktPTrLv92tH0i45rFU2vpH73Jnc2E0w6EPyDqCg4hmDTJjURbUpuxA182ISC4L+KKK6Cq0pZrU7mGCpDhn+GZpLCfHCg7EHGQGE+1FcRJt+XZIGsT2UWz8Phyzm/8/1+5+Qk91IUwYIY2JAAAezmq580AeOQg4dhL0xCCebgIMBLAAsAvB5FwwI+RTr+NkUGXnodSMcrBTLwvXMWGXjm5HYy8OtlIAN/eEv6b5T/61PpL38s/fyb0h+dl6VHnyAdX32WDFxQ0TPqlmPzMLLT+r4ce6WcuHQE3oEP80vwSX4Ffp04DkeWoQ6whzrqT2lxT6SEL1wv6fnCF0KkfNf3Uq4QvlvXjIvaOrEcv5tSzKW4M4w66/sWeslMmLi2j2mWyU3SCVxiIxb1nWilTj+uUpE2rodHJM56+1FGHHmYDOunN4C9C2w6P/fMk5W5mu0Jb1fSFUnh7banS/nZp4oFu1K184VCsWBPHbBrpaJdrdTytXJl1g6K+ep0yU4ExaI981z1QLLwfLKaLxeSbUSyiRh7OqjMjvI03c5Hqd/ZjgbT7g/xCJmkp/2ABh2GYRUiQgp7rjvmB1IprkyynQicd1e5rfwX21iKuzTKb+tGeCIg5lite5HCZLhpEXCDtFg/u5P7G4nxxDVi3LQSEyYDLywBu5HHu4t2iUCOEi+fBubz1EZiUhuISTXLrK+WN1OGH/y+KbZDJzdd9sLWbMmObl1pP9gdUoO3nD40mX4RQq11lwAbcGEbG+D9ZP6oaQhSecLEz9+H9pLjZyud82v/PMSinBTKwPOngL28Ret/Cw07Q2iy3lW4Si7lkSaCTiMTPEsuu+PaXinOh1U0zLRqqFmYFu2midCGhIm/LAHbx/fSg+wB9UfRRdf8HYz5AXEnhiajVWgzt75xmZMsZodlXEh5CR3XMuzF7mGJTNIbv/7DiqtV1JUIJczzxnw5CbwyyO5D4PfQXSyz6RZlY/jdArAhvoOiI0R4AuTliwOKY3Egpv+h1WFd8w7pIWWDuVWtl3ooYukCxv+GkY/0HhkPHZzJDS8elnY2e9OMsvNZb12LReysU9dC/yur5dqn/9RuPXbdeTJrjUYjOnk8N9EK5CblQ/0wlCvr82cf+zmbUdHQueyERDYaf2YfaR4uZB0dvxzac0Pngdt8QbhXvSKUYA72w3727wAglW3I) · [training dummy](https://elliotwood.github.io/Forever/forever/warrior/dps/#eJzMVF1oHFUU3js/m5uTtpncRJrc2HINWDdbN70zm22y6cMmkT6oiEh9kCKYSWbSHU13lrkj2jcLRnywGhGLjWCjEhqjlVqKShDxp42JJFDBFpQ+SCko1If4KoJy7+4mNQYfQg3eh7OHs+d855zvnDOQIAn6vYUNC9Fh0PFPw2DgG68g0PGfHhj4rcsWGPjihUYw8BfTCAz8zetSfqnkbx9KefN9Kcdfk/LMuAw98zjo+MRRMPCEsl5UKGfHUcduaz5ofSlI3TiN3kDvulPoA3cG/ThwDp2eRgsIDSbmtHaHZ3mO207Gztk5btvyx8nanOfsBc24rr3QSN5EZMQtjz0RlmPmcGd/xuYZ7vSxkaJbOuJ7LIyY63m+x4aPsbjosyiM3TgIS0z4bjRSZCnh+2z06ehYxnsmE7mBl6l5ZCoeXU+KsNRJu2Ev7YSmdCM2iPZAgtaBCXp3TkBLmuCkMgFgSDq23ZUT1AQdzwyRZtoE5reahhHFkEyZ+OO3EbmCyDxStfJ8xsn3scGxMPTiYhCJmEW+iMPI91jKLTHfjcYCP6rV6kVhuex7LIiZasD3BIuLbsxE0ZUhR0MRsyD2I9WhYG7JY7bDmWCjwZFiLA6wYXfkKebGLC4GgolyKN1ZINhepyt7twR1SywoeX7ZL3l+KVY5pL/dy5m4lzmcc35Lhk4Kqi8DX51D5PktGsUuxbmxxnk229VT5fyT7aSe1knVOnmIAMU0CYb13auItFAC9VAH5qg7Jvya826MKF0/VnsNLEtt6KT3rPdwuACStqqDx5AEw+7mghqgtTaRHprbaFsc/o9tsbvVtiTBwNemENlF29cH7edCtoBvfo5IjmY3Kia7QTHZSpj12fRmwvA7P28q2/ELmw47uUXLs09NZsMFUrwm13jt4aIvQcrr6pI323v766qXs2QIT2yvbS3+aAat6i//8TBJ0T3Qnm7DJmmYRatnV+VSrtEqwtwWkXkIDpL7wErvwIjo11FCXg0gG+6s3lSSaFGVTNvh1S/heprl3QBghlIYz19CZIAWwCb7FKz5N9h22qasFdgkGKB111CrECb+YQqRw/QxeIg8+K9sAU23YpPALKrRdst/Mou5lqWXy1JTOl7Ok/sxogfhAMlvGl1i4q8nKufe2LEdGs6rcSbx4iUFUdHICbQ1q1fZKp3s+Ao1gJky8fJhollmZZg51bmy7aR3wLYOAHweya/nZLP0wJPNrfov2gJa0ZzjekK9lv5ZrUF+bC2do97fUcd7er20J54b7W+bPCXfYuGuUfWuFpwVrbWOFdILWuJ/9eL+mvafvj1nb3ue/PLS0tK2oXP9A1VD/xB6EaFTKAhXxhcfvVLIK2vicmFAei4t/Vp4pKJcK6R1/OnOwcSz5K8BAAr9/5Y=).

## Other builds of this spec

- [Two-handed Arms/raid or leveling](../research/raid/builds/opt-arms-2h-raid-raid-dps.md) (20/31/0, 898 DPS in a full raid) — [open the talent tree](https://talentsforever.com/warrior/60/03305013032-05250030052210501--6)
- [Fury — Two-Handed](../research/raid/builds/arms-2h-raid.md) (19/32/0, 887 DPS in a full raid) — [open the talent tree](https://talentsforever.com/warrior/60/03305013031-55350000052010501--6)
- [Raid dual-wield Fury](../research/raid/builds/opt-fury-dw-raid-raid-dps.md) (19/32/0, 885 DPS in a full raid) — [open the talent tree](https://talentsforever.com/warrior/60/04305013102-25050035102210501--6)
- [Fury — Dual Wield](../research/raid/builds/fury-dw-raid.md) (13/38/0, 884 DPS in a full raid) — [open the talent tree](https://talentsforever.com/warrior/60/20305012-55053005152010501--6)

---
*Generated by `_reference/data/render_modes.py` on 2026-10-09 from this project's builds and simulations of the WoW: Forever beta (client build 1.60.1.70291). Simulations, not in-game measurements. Do not hand-edit.*

