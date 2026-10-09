# Beast Mastery Hunter — Raid (group)

[Hunter](../README.md) > [Raid (group)](README.md) > Beast Mastery

**[Beast Mastery — Full raid](../research/raid/builds/beast-mastery-ml-parse.md)** (31/20/0) — [open the talent tree](https://talentsforever.com/hunter/60/5320001505101251-00532500005--6)

> 🔬 Derived build: searched in the community's raid simulator from the spec's best build. A model of the beta, to check at launch.

## How to play

**Before the pull:** **Aspect of the Hawk**, **Aimed Shot**.

**Then press the first one that is ready**, top to bottom:

1. **Serpent Sting**: keep it on the target
2. **Arcane Shot**
3. **Rapid Fire**
4. **Aimed Shot**

**Aimed Shot** is your filler: cast it whenever nothing above is ready.

**Advanced: your cooldowns and extras.** Once the list above feels easy, add these:

- **Bestial Wrath**: a cooldown, use it at the start of the fight and again whenever it is ready (about 2 times a fight)
- Use your trinkets, your racial and a potion together with your big cooldowns.

*The simulator's full rotation for this build, with every condition: [research rotation page](../research/raid/rotation.md).*

## Why this rotation

Beast Mastery in a raid is **Auto Shot** and your pet with a short list on top: keep **Serpent Sting** ticking, fire **Arcane Shot** and **Aimed Shot** each time their cooldowns end, and send **Bestial Wrath** whenever it is ready.

**Why it works**

- **Serpent Sting** comes first so it never drops: it is about a fifth of your damage in the simulator, 20% more with **Improved Stings**. Recast it only as it runs out, since a new sting replaces the old one and its last ticks; the full rotation recasts it only while you have 30% mana or more.
- **Arcane Shot** goes out every time its 6-second cooldown ends, about 29 times in a 3-minute fight. **Summon Hawk** shares that cooldown, and in a full raid the simulator measured about 1.4% more damage giving all of it to **Arcane Shot**, so this build no longer sends the hawk there.
- **Rapid Fire** (40% faster attacks for 15 seconds, 5-minute cooldown) goes once a fight, at the pull. The full rotation presses it just before an **Auto Shot** with **Aimed Shot** about to come off cooldown, so the next **Aimed Shot** is cast under it.
- **Aimed Shot** is last on the list but it is not a spam filler: it goes out almost every time it can, a 2-second cast and then its 6-second cooldown, about 23 times a fight. The instants above it cost only a global cooldown, and the simulator measured **Aimed Shot** slightly better below them.
- **Bestial Wrath** (+50% pet damage for 18 seconds) goes at the pull and on every 2-minute cooldown, about twice a fight. **Intimidation** is in the build only because **Bestial Wrath** requires it; the full-raid list never presses it.
- Your pet is about a quarter of your damage. It takes 10% of your attack power and all of your crit (this project's model of Forever's pet scaling), so **Ferocity** and **Frenzy** keep it critting and attacking faster, and **Focused Fire** adds 2% to you both while it is out.

**Caveats**

- Mana: the list assumes a full raid with Blessing of Wisdom and Mana Spring. With only your own buffs the simulator's best rotation never casts **Aimed Shot** (310 mana) and keeps **Arcane Shot** going above 10% mana, so **Aimed Shot** is the first thing to drop when you run low.
- Keep the pet alive with **Mend Pet**: Forever pets take no stat buffs from players, and a dead pet takes **Focused Fire** with it. A faster pet does more damage as modelled here (a 1.2-second cat over a 2.0-second pet; players have measured this only at levels 20 and 30).
- Moving: **Auto Shot** and **Aimed Shot** stop while you move; **Arcane Shot** and **Serpent Sting** are instant, so keep pressing them.
- The simulator starts **Aimed Shot** 2.5 seconds before the pull so it lands as the fight begins; in a real raid, start it once your tank has the boss.

**When to change it**

- Two or more targets close together: **Multi-Shot** instead of **Aimed Shot** on their shared cooldown, since it hits up to 3 targets for weapon damage each while **Aimed Shot** adds 166 to one. For a pack, **Volley**: a 6-second channel with no cooldown in Forever, which holds **Auto Shot** while you channel.
- In the last few seconds, skip the **Serpent Sting** refresh: its damage comes over 15 seconds. The simulator's other hunter rotations stop refreshing it 3 to 6 seconds before the end.
- Inside 8 yards your shots and **Auto Shot** stop. Step back out; if you cannot, **Summon Hawk** still works, as it has no minimum range.

## The numbers

| Setting | DPS |
|---|---|
| Full raid, 3-minute fight (every raid buff and debuff: what this page ranks on) | 843 |

**By gear tier** (the spec's best talents for each tier and setting in its own gear, found by this project's machine-learning search in the community simulator; [every spec](../../_reference/dps-rankings.md)):

| Gear | Full raid DPS | Best talents |
|---|---|---|
| Pre-BiS | 865 | [31/20/0](https://talentsforever.com/hunter/60/5320001505101251-00531501005--6) |
| Phase 1 BiS | 889 | this build |

*From the search run of 2026-10-01; a new run is queued and will replace these numbers.*

**The gear** (average item level: Pre-BiS 63.2; Phase 1 BiS 66.6; each item opens its Wowhead page, with where it drops and its enchant):

| Slot | Pre-BiS | Phase 1 BiS |
|---|---|---|
| Head | [Black Dragonscale Helm](https://www.wowhead.com/forever/item=252605) · *Leatherworking*<br>+ [Lesser Arcanum of Voracity](https://www.wowhead.com/forever/item=11647) | [Black Dragonscale Helm](https://www.wowhead.com/forever/item=252605) · *Leatherworking*<br>+ [Lesser Arcanum of Voracity](https://www.wowhead.com/forever/item=11647) |
| Neck | [Mark of Fordring](https://www.wowhead.com/forever/item=15411) · *quest: In Dreams* | [Onyxia Tooth Pendant](https://www.wowhead.com/forever/item=18404) |
| Shoulders | [Theramore Pauldrons](https://www.wowhead.com/forever/item=271955) | [Giantstalker's Epaulets](https://www.wowhead.com/forever/item=16848) · *Sulfuron Harbinger, Molten Core* |
| Back | [Earthweave Cloak](https://www.wowhead.com/forever/item=21187)<br>+ [Enchant Cloak - Lesser Agility](https://www.wowhead.com/forever/spell=13364) | [Earthweave Cloak](https://www.wowhead.com/forever/item=21187)<br>+ [Enchant Cloak - Lesser Agility](https://www.wowhead.com/forever/spell=13364) |
| Chest | [Dawn Armor](https://www.wowhead.com/forever/item=252483) · *Leatherworking*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) | [Giantstalker's Breastplate](https://www.wowhead.com/forever/item=16845) · *Golemagg the Incinerator, Molten Core*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) |
| Wrist | [Forest Stalker's Bracers](https://www.wowhead.com/forever/item=19587)<br>+ [Enchant Bracer - Minor Agility](https://www.wowhead.com/forever/spell=7778) | [Giantstalker's Bracers](https://www.wowhead.com/forever/item=16850) · *Molten Core*<br>+ [Enchant Bracer - Minor Agility](https://www.wowhead.com/forever/spell=7778) |
| Hands | [Theramore Gloves](https://www.wowhead.com/forever/item=271948)<br>+ [Enchant Gloves - Agility](https://www.wowhead.com/forever/spell=13823) | [Giantstalker's Gloves](https://www.wowhead.com/forever/item=16852) · *Shazzrah, Molten Core*<br>+ [Enchant Gloves - Agility](https://www.wowhead.com/forever/spell=13823) |
| Waist | [Warpwood Binding](https://www.wowhead.com/forever/item=18393) · *Tendris Warpwood, Dire Maul* | [Giantstalker's Belt](https://www.wowhead.com/forever/item=16851) · *Molten Core* |
| Legs | [Outrider's Chain Leggings](https://www.wowhead.com/forever/item=22673)<br>+ [Lesser Arcanum of Voracity](https://www.wowhead.com/forever/item=11647) | [Dragonstalker's Legguards](https://www.wowhead.com/forever/item=16938) · *Ragnaros, Molten Core*<br>+ [Lesser Arcanum of Voracity](https://www.wowhead.com/forever/item=11647) |
| Feet | [Windreaver Greaves](https://www.wowhead.com/forever/item=13967) · *Kirtonos the Herald, Scholomance*<br>+ [Enchant Boots - Greater Agility](https://www.wowhead.com/forever/spell=13823) | [Giantstalker's Boots](https://www.wowhead.com/forever/item=16849) · *Gehennas, Molten Core*<br>+ [Enchant Boots - Greater Agility](https://www.wowhead.com/forever/spell=13823) |
| Finger | [Signet Ring of the Bronze Dragonflight](https://www.wowhead.com/forever/item=21202) | [Band of Accuria](https://www.wowhead.com/forever/item=17063) · *Ragnaros, Molten Core* |
| Finger | [Don Julio's Band](https://www.wowhead.com/forever/item=19325) | [Signet Ring of the Bronze Dragonflight](https://www.wowhead.com/forever/item=21202) |
| Trinket | [Blackhand's Breadth](https://www.wowhead.com/forever/item=13965) | [Blackhand's Breadth](https://www.wowhead.com/forever/item=13965) |
| Trinket | [Royal Seal of Eldre'Thalas](https://www.wowhead.com/forever/item=18473) · *quest: The Greatest Race of Hunters* | [Royal Seal of Eldre'Thalas](https://www.wowhead.com/forever/item=18473) · *quest: The Greatest Race of Hunters* |
| Main hand | [Barbarous Blade](https://www.wowhead.com/forever/item=18520) · *King Gordok, Dire Maul*<br>+ [Enchant 2H Weapon - Superior Impact](https://www.wowhead.com/forever/spell=20030) | [Barbarous Blade](https://www.wowhead.com/forever/item=18520) · *King Gordok, Dire Maul*<br>+ [Enchant 2H Weapon - Superior Impact](https://www.wowhead.com/forever/spell=20030) |
| Ranged/relic | [Premier High Warlord's Recurve](https://www.wowhead.com/forever/item=272594)<br>+ [Biznicks 247x128 Accurascope](https://www.wowhead.com/forever/item=18283) | [Rhok'delar, Longbow of the Ancient Keepers](https://www.wowhead.com/forever/item=18713)<br>+ [Biznicks 247x128 Accurascope](https://www.wowhead.com/forever/item=18283) |

**Open in the simulator** (the community's Forever simulator on the web, loaded with the gear, enchants, talents, rotation, consumables and buffs we simulate): Pre-BiS: [full raid](https://elliotwood.github.io/Forever/forever/hunter/dps/#eJzMVV9IPFUUnjMzu3M8/dD1ruY4SEwbxTo0y53RCTViVp+ihyjooadydNd2JN1ldx+sJyODkEp7sQzBQCSNAqOCCIIohBWmXJX+kRCUgQ897Fv0EMTM7ipIvbnQ93Tu+cP5zncv99AdhASooEMaOLD7rk4ihzHIwhPwNExDAUqwDPAqwDqA9i0iJiTtRVLwi0971Iu7SMKPl0jGsyBBCn69C+pJPDQ+6VF/6yYFX94E9U8gBYMgof7STTL+tBYe3/wIwuo4ri003ae7QDL+vQEk4esLJOP+epj34zqol90kkIKnJwn152Qqgyt+ouarr/n6e1uQvtiGVRBX/Ldhx3sXPvD24HzyALZ3oQZQhzf8Kbqe8nNxyBmxOeeWwx2LW7ZjmZw7I5bDLc6dmijXRfxV/DJOfYRanGSsH0IKKU6yafEK9be8ezuQ6iKFYqadcSpsA9gzXun5Z4ulqm5z+yHT4iYfndBnC97ic/mcXizrXi6Xz+kzL+jVQl4vF6te1S8u6pW8V54t6OlKPq/PLJhlz8+Z7aDZDGbmK8XFYW2UDJampNGLMRb7ShQxFhIh0apQr9GDcSY+JmgKxUiyeCUM4Q9/Pc62bhLj46Y9dqvEJoizDA0aAygxnA8bHx+CFonDM7ZzRW+mRW+E36+1spisiRMCe6vz6jn0IDOo30heqxddKs/8O8EYSXhcZI9oD5PNOPUZDKV2YTQFz1ikGnejxLreh9aLaEecqPz3ATbfcfHx6qZv9go1tDvQa28HmK7d8x9aRpOf9anSpViDhmi/JAkR0tlV6Kck9WI8gSoMCxEaLofUvtQV2sLyXHbwnc0QR+69cxG+d+2GqCq6a9RE4X+FarZtdRQPfHjrfca/CYLgzvRBdrLlyE6HX/sm+MXGK0dPfeeOR16h7k6GmUHwh/tk0zh3DQk/G5gauv5Om2vi0WhRFKAES7DE/hkAOyxLEQ==) · [training dummy](https://elliotwood.github.io/Forever/forever/hunter/dps/#eJzMkc9LHGcYx+d5Z3bm8Wmr6+uv6dDDdGmLLszyzui01VJm9Q8oFHpuHd21jlRXdvdgc8oPA0GSaC5BQ8CASDQkYEgCIZBLgrDChKyGJCYRAokBDznsLXgIhNldLzkr5HP6vt/neXi+Dy9JXDJ2VMS4bBwjDe/fadJ3vyIZb02Rgk/COGn4cBn0TTUSt5v0t42k4akF0D8AaRiGcf11Iyn4YjZ6XrgJ0bSKs+M1e2sZSMGPF4FkPDdOCq7ORX3bc6DvNZJEGm5txvVXLYkUTgfxUqCfDcyrl6FzdxFmgE0H87DkX4Hr/grs9K/B4jKUAMpwPhiQ7rHv3G5HCGG7wrWF7bi2JYTb7bqRZ5eYUmb4hm0r1EpoqKRgeR0SSCopli0K1FZ3V5Yg0UAaxSwn5Rb478Zv5HBBrUmOMo89YAxjhkYxkkXKJj3ZjjJvuAb1yYOKa8RIxncdfIz/7U/+909usmg6wvnZEr2W82ufOTzqT/ybzZi5vOlnMtmMOfS/WRzNmvlc0S8GuQmzkPXzw6NmZyGbNYfGrbwfZKyDolUrpsYKuYkuo5b6+f4fPHPku1ifxE/Cka8xqT3ZijLHsei0x+sQnUisp2DU33zu8xC2sETPoYZI0Q88Qd+8VIkU3J8HzuIKNSebUOVsSKp99C/ix2qk/XnQ5T1WggpzTshSlc70DLRRCzWjGkcduqQqFU9AYlVuiLR0fCT97aWFiA3v+5EqzzynwnTN9JIlJn1RFNMH6kj56cah7+l9FIbh14Nr6f66kR6EMwALEOQqpzf+eur1Vl2p7PVHnWH43vuzJna8pIx3OwYYwhT/NADyhhD1); Phase 1 BiS: [full raid](https://elliotwood.github.io/Forever/forever/hunter/dps/#eJzMVU1IK1cUnjOTZI6novFG6zhImaa0xKET7oxOUUuZ6Kp0UVrooqvW0cRmpJqQZGGhC0sUivRHumhrESyI+EMLbgqlUCgtQoSIUfsHFQrv+cDFW2T3eLvHjImCvLcz8L7VyfnOyfnOd4d7qR0hCgpokAAO7IWrXyKHYUjBW/AuTEAW8rAA8CnACoBaQ8SopH5MMv76U6dy/gyF8PxLoBDWykAy/rEJynGEZDwsg3K3g2Q8KYPywKf+LIPyfweF8DSo3F0Ev13G42Z+a8n/n5NNIAk/n6UQ7qz4hf+ugHLRQQLJuPoVKP/F4klc9KIVT/nM07bWIHG+DssgLnrfwob7PfzgbsPZ2B6sb0IFoAZfeON0vecvYr89aHHOTZvbJjct2zQ4twctm3PO7YoYqol4R/wtQt2EasTfax/iSBEKGSYvUk8ju70B8TaSKWxYSbvIvgb2npv/8P1cvqRZ3HrFMLnBh0a1qaw790EmreUKmptOZ9La5EdaKZvRCrmSW/Jyc1ox4xamslqimMlok7NGwfXSRpM0LsnkTDE3N6AOkc4SFNO7MMzCv4sihn0hJJpF6tI7McLENwRVpjBJJi/6FP7z8E22dlMYHzGs4VsVNkqcJalP70WJ4Yw/+Ggf1MAcnrTsK3mTDXmD/EW1UcVCqjgqsG9a755NLzOdevTYtXvBofLk4wWGScKjHHtNfZUsxqlbZyg1G4MteNIkRX8WJda2C40vosnYQfu9XjbTcvPx6qRvzvI9tFowa3sDmKY+9wQvg81PuxXpQqxAXbQ+kYQAidQy9FCMujASRQUGhAB1h0N8R2rzY2FhOtX33aqPA+f56QB/O1ZdVGTN0Sui8FShlGpGLcVLP976nJHDarXaPrGXGmskUhP+5b4KXq6+dPDOX85IkBVqzphfWa3ed96+DM4cXcKfe8f7r6/Ty4fi9eCpyEIe5mGePRoANNZJ/g==) · [training dummy](https://elliotwood.github.io/Forever/forever/hunter/dps/#eJzMkctLHFkUxuvcqu46npnR9vqqKWZR08wM2lDNrdKaGQ2hWv+AQCDrxNJuY0m0pbsXCWSRpBWC5CFZaQgYEPFBAm4CIZBNgtBCS1rzkkQSSAy4yKJ3wV2ofmyyVshvder7zqnzHS5JXNI/hBEjsn6ZVHz6qEnb/4UU3L8NpGApD6Ti8yXQtsOk4lYetM+NpOJOHrRvgfUqD9rHRlLwZaVzbQqCcRW36/rydPCfnSUgGW+Ok4Krs0Hj7ixoB40kkYrzd0B73xKN45QfKfjaDd9Yvged+wswA2zKn4NF7z488FZgr38dFpagAFCCW/6A9IT94XTbQgjLEY4lLNuxTCGcbscJNKvAlBLDT2xXoVZCPRxcswFRpDAppiWy1FZTVxYh2kAqhUw77mT5Sf0E2VxQa4yjzEPPGMOQrlKIZBG3SIu1o8wb1qA2WXccPUQyfungY/ysN3nhXHoyZ9jC/tcUvab9f58xPOpNnE8ljXTG8JLJVNIYumTkRlNGJp3zcn56wsimvMzwqNGZTaWMoXEz4/lJs26aVTM+lk1PdOnV1G8PT/Hkse9ifRK/Bse+xqD2WCvKHMeC015sQHAisZ6sXvvmsz+GsIQpeo40RJz+4lH67V2YSMHDOeAsolBzrAnDnA1J1Yf+T/xdiXQ4B5p8wApQZvZVWarQmZiBNmqhZgxHUIMuqULZFRBdlRuCWroykvj97nzApvvnSIU3rl1mmmq4sQKTfipyiXp1rPzz8Mj39G4Vi8VfB9cT/TUhMQjXAebBT5enN8+8dnsrqlRy+4POYvGre7pa7LkxGR93DDCEi/z7AAE1D+I=).

## Other builds of this spec

- [Beast Mastery — Raid](../research/raid/builds/beast-mastery-raid.md) (30/21/0, 810 DPS in a full raid) — [open the talent tree](https://talentsforever.com/hunter/60/522002150510025-00534500013--6)

---
*Generated by `_reference/data/render_modes.py` on 2026-10-09 from this project's builds and simulations of the WoW: Forever beta (client build 1.60.1.70291). Simulations, not in-game measurements. Do not hand-edit.*

