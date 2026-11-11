# Beast Mastery Hunter — Raid (group)

[Hunter](../README.md) > [Raid (group)](README.md) > Beast Mastery

**✅ Recommended** for raid (the best hunter spec here, or within 3% of it).

**[Beast Mastery — Raid](../research/raid/builds/beast-mastery-ml-raid.md)** (31/20/0) — [open the talent tree](https://talentsforever.com/hunter/60/5320001505101251-00530502005--12)

> 🔬 Derived build: found by this project's machine-learning search over every legal build of the spec in the community's raid simulator (phase-1 BiS gear, then raced against the spec's builds). A model of the beta, to check at launch.

## How to play

**Before the pull:** **Aspect of the Hawk**, **Aimed Shot**.

**Keep up all fight:** **Aspect of the Hawk**.

**Then press the first one that is ready**, top to bottom:

1. **Serpent Sting**: keep it on the target
2. **Arcane Shot**
3. **Rapid Fire**; no global cooldown, so press it alongside the others
4. **Aimed Shot**

Between these, **Auto Shot** keeps firing on its own.

**Advanced: your cooldowns and extras.** Once the list above feels easy, add these:

- **Bestial Wrath**: a cooldown, use it at the start of the fight and again whenever it is ready (about 2 times a fight)
- Use your trinkets and a potion together with your big cooldowns.

*The simulator's full rotation for this build, with every condition: [research rotation page](../research/raid/rotation.md).*

## Why this rotation

Beast Mastery in a raid is **Auto Shot** and your pet with a short list on top: keep **Serpent Sting** ticking, fire **Arcane Shot** and **Aimed Shot** each time their cooldowns end, and send **Bestial Wrath** whenever it is ready.

**Why it works**

- **Serpent Sting** comes first so it never drops: on the training dummy it is about 15% of this build's damage, 20% more with **Improved Stings**. Recast it only as it runs out, since a new sting replaces the old one and its last ticks. The full-raid rotation recasts it whatever your mana: the search of 2026-11-10 dropped the old 30% mana guard (about 0.2% better).
- **Arcane Shot** goes out every time its cooldown ends: 5.4 seconds with 2 points in **Improved Arcane Shot**, about 33 times in a 3-minute fight. **Summon Hawk** shares that cooldown, and the full-raid rotation gives all of it to **Arcane Shot**, so the build's **Summon Hawk** point is never cast.
- **Rapid Fire** (40% faster attacks for 15 seconds, 5-minute cooldown) goes once a fight, at the pull. The full rotation presses it just before an **Auto Shot** with **Aimed Shot** about to come off cooldown, so the next **Aimed Shot** is cast under it.
- **Aimed Shot** is last on the list but it is not a spam filler: it goes out almost every time it can, a 2-second cast and then its 6-second cooldown, about 23 times a fight. The instants above it cost only a global cooldown.
- **Bestial Wrath** (+50% pet damage for 18 seconds) goes at the pull and on every 2-minute cooldown, twice a fight. **Intimidation** is in the build only because **Bestial Wrath** requires it; the full-raid list never presses it.
- Your pet is about a quarter of your damage on the training dummy. It takes 10% of your attack power and all of your crit (this project's model of Forever's pet scaling), so **Ferocity** and **Frenzy** keep it critting and attacking faster, and **Focused Fire** adds 2% to you both while it is out.

**Caveats**

- Mana: the list assumes a full raid with Blessing of Wisdom and Mana Spring. With only your own buffs the simulator's best rotation never casts **Aimed Shot** (310 mana) and keeps **Arcane Shot** going above 10% mana, so **Aimed Shot** is the first thing to drop when you run low.
- Keep the pet alive with **Mend Pet**: Forever pets take no stat buffs from players, and a dead pet takes **Focused Fire** with it. A faster pet does more damage as modelled here (a 1.2-second cat over a 2.0-second pet; players have measured this only at levels 20 and 30).
- Moving: **Auto Shot** and **Aimed Shot** stop while you move; **Arcane Shot** and **Serpent Sting** are instant, so keep pressing them.
- The simulator starts **Aimed Shot** 2.5 seconds before the pull so it lands as the fight begins; in a real raid, start it once your tank has the boss.
- Watch your ranks: in the beta client (build 70753) the top ranks are the strongest. **Hunter's Mark** rank 4 gives +143 ranged attack power (rank 3 +98), **Trueshot Aura** rank 5 +100 (rank 4 +75; if your build has it) and **Aspect of the Hawk** rank 7 +120 (rank 6 +110). Cast the highest rank you have.

**When to change it**

- Two or more targets close together: **Multi-Shot** instead of **Aimed Shot** on their shared cooldown, since it hits up to 3 targets for weapon damage each while **Aimed Shot** adds 350 to one. For a pack, **Volley**: a 6-second channel with no cooldown in Forever, which holds **Auto Shot** while you channel.
- In the last few seconds, skip the **Serpent Sting** refresh: its damage comes over 15 seconds. The simulator's other hunter rotations stop refreshing it 3 to 6 seconds before the end.
- Inside 8 yards your shots and **Auto Shot** stop. Step back out; if you cannot, **Summon Hawk** still works, as it has no minimum range.

## Talents

| Tree | Points | Talents (ranks) |
|---|---|---|
| Beast Mastery | 31 | Deadly Aspects 5, Endurance Training 3, Focused Fire 2, Bestial Swiftness 1, Unleashed Fury 5, Ferocity 5, Summon Hawk 1, Intimidation 1, Bestial Discipline 2, Frenzy 5, Bestial Wrath 1 |
| Marksmanship | 20 | Lethal Attacks 5, Improved Stings 3, Careful Aim 5, Improved Arcane Shot 2, Mortal Shots 5 |

## The numbers

| Setting | DPS |
|---|---|
| Full raid, 3-minute fight (every raid buff and debuff: what this page ranks on) | 1009 |

**By gear tier** (the spec's best talents for each tier and setting in its own gear, found by this project's machine-learning search in the community simulator, wowsims/forever 16e8542 (client 70790); [every spec](../../_reference/dps-rankings.md)):

| Gear | Full raid DPS | Best talents |
|---|---|---|
| Pre-BiS | 954 | [31/20/0](https://talentsforever.com/hunter/60/5122001505011251-00530504003--12) |
| Phase 1 BiS | 990 | this build |

*Each row is in that tier's own gear set; the DPS at the top of the page is this build in the standard set, so the two do not match.*

**The gear** (average item level: Pre-BiS 62.5; Phase 1 BiS 63.8; each item opens its Wowhead page, with where it drops and its enchant):

| Slot | Pre-BiS | Phase 1 BiS |
|---|---|---|
| Head | [Black Dragonscale Helm](https://www.wowhead.com/forever/item=252605) · *Leatherworking*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11647) | [Black Dragonscale Helm](https://www.wowhead.com/forever/item=252605) · *Leatherworking*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11647) |
| Neck | [Amulet of the Darkmoon](https://www.wowhead.com/forever/item=19491) · *quest: 1200 Tickets - Amulet of the Darkmoon* | [Onyxia Tooth Pendant](https://www.wowhead.com/forever/item=18404) · *quest: For All To See* |
| Shoulders | [Theramore Pauldrons](https://www.wowhead.com/forever/item=271955) | [Theramore Pauldrons](https://www.wowhead.com/forever/item=271955) |
| Back | [Earthweave Cloak](https://www.wowhead.com/forever/item=21187) · *quest: Volunteer's Battlegear*<br>+ [Enchant Cloak - Lesser Agility](https://www.wowhead.com/forever/spell=13364) | [Earthweave Cloak](https://www.wowhead.com/forever/item=21187) · *quest: Volunteer's Battlegear*<br>+ [Enchant Cloak - Lesser Agility](https://www.wowhead.com/forever/spell=13364) |
| Chest | [Dawn Armor](https://www.wowhead.com/forever/item=252483) · *Leatherworking*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) | [Dawn Armor](https://www.wowhead.com/forever/item=252483) · *Leatherworking*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) |
| Wrist | [Beaststalker's Bindings](https://www.wowhead.com/forever/item=16681) · *Blackrock Spire*<br>+ [Enchant Bracer - Superior Strength](https://www.wowhead.com/forever/spell=19984) | [Beaststalker's Bindings](https://www.wowhead.com/forever/item=16681) · *Blackrock Spire*<br>+ [Enchant Bracer - Superior Strength](https://www.wowhead.com/forever/spell=19984) |
| Hands | [Theramore Gloves](https://www.wowhead.com/forever/item=271948)<br>+ [Enchant Gloves - Agility](https://www.wowhead.com/forever/item=273520) | [Theramore Gloves](https://www.wowhead.com/forever/item=271948)<br>+ [Enchant Gloves - Agility](https://www.wowhead.com/forever/item=273520) |
| Waist | [Highlander's Mail Girdle](https://www.wowhead.com/forever/item=20044) · *sold by Samuel Hawke* | [Molten Belt](https://www.wowhead.com/forever/item=19163) · *Leatherworking* |
| Legs | [Beaststalker's Pants](https://www.wowhead.com/forever/item=16678) · *Baron Rivendare, Stratholme*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11647) | [Beaststalker's Pants](https://www.wowhead.com/forever/item=16678) · *Baron Rivendare, Stratholme*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11647) |
| Feet | [Shadowcraft Boots](https://www.wowhead.com/forever/item=16711) · *Rattlegore, Scholomance*<br>+ [Enchant Boots - Greater Agility](https://www.wowhead.com/forever/item=16245) | [Shadowcraft Boots](https://www.wowhead.com/forever/item=16711) · *Rattlegore, Scholomance*<br>+ [Enchant Boots - Greater Agility](https://www.wowhead.com/forever/item=16245) |
| Finger | [Cutthroat's Signet](https://www.wowhead.com/forever/item=272408) · *sold by Pix Xizzix* | [Cutthroat's Signet](https://www.wowhead.com/forever/item=272408) · *sold by Pix Xizzix* |
| Finger | [Channeler's Ring](https://www.wowhead.com/forever/item=272406) · *sold by Pix Xizzix* | [Band of Earthen Might](https://www.wowhead.com/forever/item=21182) · *quest: Veteran's Battlegear* |
| Trinket | [Blackhand's Breadth](https://www.wowhead.com/forever/item=13965) · *quest: For The Horde!* | [Blackhand's Breadth](https://www.wowhead.com/forever/item=13965) · *quest: For The Horde!* |
| Trinket | [Counterattack Lodestone](https://www.wowhead.com/forever/item=18537) · *Tribute, Dire Maul* | [Counterattack Lodestone](https://www.wowhead.com/forever/item=18537) · *Tribute, Dire Maul* |
| Main hand | [Legionite Glaive](https://www.wowhead.com/forever/item=250619) · *Blacksmithing*<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) | [Legionite Glaive](https://www.wowhead.com/forever/item=250619) · *Blacksmithing*<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) |
| Ranged/relic | [Gorewood Bow](https://www.wowhead.com/forever/item=16996) · *quest: The Scarlet Oracle, Demetria*<br>+ [Biznicks 247x128 Accurascope](https://www.wowhead.com/forever/item=18283) | [Rhok'delar, Longbow of the Ancient Keepers](https://www.wowhead.com/forever/item=18713)<br>+ [Biznicks 247x128 Accurascope](https://www.wowhead.com/forever/item=18283) |

**Open in the simulator** (the community's Forever simulator on the web, loaded with the gear, enchants, talents, rotation, consumables and buffs we simulate): Pre-BiS: [full raid](https://wowsims.com/forever/hunter/dps/#eJzEVEFIG2kYzffPJPPl210dRt2MgyyzWZAYmPDP6Ii6LIme9rTInva062jiZmQ1IclBYQ+uuLCIW0oPRUWwkNpaaW8tSKEXi9RCwBShhdZSaW1poQevbaGUGRMotUel7zC8eW+G976Zn4/aEGRQQYcYDEEW8jAN8B/ABYA1AOVr32We2wPaCwlRFrS/ScJbNxrVg69IxPICkIi7FZkkvL0K6r2QR643qs8aSMIrM6A+9kilIqtPGkjEyjKQhJdmwHtdwjszcKQvVGUS8XxVJgH/HycRX531Hny32qi+bqAASXgwC+qjpmi7vO3GDlZgDtisuwThsnPV2etfWYV1kObdy8twxt2HWXcA/eqQgpuszTYti3PT5jY3Tcs2Dc7tTm7zLs47t5lYZfiU7QWpmVALkYjVLYgihUg0TF6klpq6VoZomCQKGlbCLir/gvK7k//rj1y+pFvc6jZMbpjdffpI1pn4M5PWcwXdSaczaX14Si9lM3ohV3JKbm5CL2acwkhWjxUzGX143Cg4btqom8aRmRgr5iY6tB+oNR5BQcExr9XOFmh+Pk9YdlGrSYqosb6A4h4vw3tPtIykBUnAnZwy9Zm5u040KkLfPAwRibg5PagwWfRn9fhP2o9kKZya4woKSnCTMQxqEgVJ4AmT1Pi3KCjhdaj9rbpj+82fR5SxT5rzXsPqOdHmRyflwZtfjmWZ3ODWKWStlUHRte+oJd6Ewfon8Q8vT9hFf/LdZlV4ybbhkFn/CAEfsdQctFKEWnDpHMhv50ENdQR8HCaHMPqehT0emB5NtS4terib/H7Ux/2ktc9UUU/GN1jgi6CUqrNTRfu1U8vp9a+/Xkz114TUkLdzF8G/Cewn4wJuRAY+Ws0ceiAFP8Mg/AZZyMMkTLIPAwCi0C3B); Phase 1 BiS: [full raid](https://wowsims.com/forever/hunter/dps/#eJzEVE9IG3kYzfebSebLt7s6jLoZB1lmsyAxMOE3446oy5LoaU+L7GlPu44mNiPVhCQHhR6sWChi/yAUqhQs2LRW2lsLUmgPFqkFQYvQQrVUWlta6MFrWyhlxgRK7VHpOwxv3pvhvW/mx0dNCDKooEMMeiELeRgDOA1wGWABQPnRd5nntoP2WkKUBe0ESXj3dq26+wOJuHsOSMTNNZkkvF8G9VHII7dq1Zc1JOH1cVCfeWRtTVaf15CIWxeAJLw6Dt7rEj4Yh3394oZMIt4rAwl4ZohEfHvee/BjuVZ9V0MBknBmGtStumizvOrGdudgEtiEOwvheeeGs901V4ZFkKbca5fgrLsDE243+tUhBXdYk91qcc5Nm9smNy3bNDi3W7nNLc7tVSZuMHzBtoNUT6iFSMSNFYgihUg0TF6khoq6MA/RMEkUNKyEXVROgfKfkz/+fy5f0i1utRkmN8y2Tr0/6wwfy6T1XEF30ulMWu8b1UvZjF7IlZySmxvWixmn0J/VY8VMRu8bMgqOmzaqprFvJgaLueEW7TdqjEdQUHDQa7W+ApqfzxOWXdQqkiJqrDOguAfL8I5DLSNpQRJwPaeMfmPu3w81KkI/PQ0Ribg81qMwWfRn9fif2h9kKZzq4woKSnCZMQxqEgVJ4AmT1PjPKCjhRaj8rapj+81fRZTBr5rzDsNqP9Tm+yflyfu/D2SZ3ODWEWQtzIOia79QQ7wOg9VP4h9enrCL/uSb9arwhq3CHrNOCgEfsdQkNFKEGnB2GuQPU6CGWgI+9pK9GP3Ewh4PjA2kGmdnPDxM/jrg43HS2mGqqCfjSyzwXVBKVdmRovnmkeV0+Nd/rqS6KkKq19u5M+DfBHaScQGXIt1frGYO7ZCCv6AH/oUs5GEERtjnAQBuMi2y).

## Other builds of this spec

- [Beast Mastery (optimized, with a pet)](../research/raid/builds/opt-mm-raid-raid-dps.md) (31/16/4) — [open the talent tree](https://talentsforever.com/hunter/60/5420001505001251-0050550001-4-12)

---
*Generated by `_reference/data/render_modes.py` on 2026-11-11 from this project's builds and simulations of the WoW: Forever beta (talent and spell data: client build 1.60.1.70753; raid numbers: the official wowsims/forever simulator at ff9babb (client 1.60.1.70888)). Simulations, not in-game measurements. Do not hand-edit.*

