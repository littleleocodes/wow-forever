# Retribution Paladin — Raid (group)

[Paladin](../README.md) > [Raid (group)](README.md) > Retribution

**✅ Recommended** for raid (the best paladin spec here, or within 3% of it).

**[Retribution — Raid](../research/raid/builds/retribution-open-raid.md)** (16/4/31) — [open the talent tree](https://talentsforever.com/paladin/60/0502510021-4-34232001201301351-12)

> 🔬 Derived build: found by this project's open talent search (every legal build, no tree rule, in the community's raid simulator in a full raid, raced against the rotation's builds). A model of the beta, to check at launch.

## How to play

**Keep up all fight:** **Seal of Command**, **Seal of Righteousness**.

**Then press the first one that is ready**, top to bottom:

1. **Judgement**; no global cooldown, so press it alongside the others
2. **Hammer of Wrath** when the target is below 20% health
3. **Consecration**
4. **Holy Strike**

Between these, your white swings do the rest.

**Advanced: your cooldowns and extras.** Once the list above feels easy, add these:

- **Seal of the Crusader**: put it up at the start and keep it up
- **Retribution Aura**: put it up at the start and keep it up

*The simulator's full rotation for this build, with every condition: [research rotation page](../research/raid/rotation.md).*

## Why this rotation

Retribution in a raid twists seals: you swap between **Seal of Righteousness** and **Seal of Command** around every swing so each hit carries both, judge **Seal of Righteousness** on cooldown, and give the remaining global cooldowns to **Consecration**, **Holy Strike** and, under 20% health, **Hammer of Wrath**.

**Why it works**

- Only one seal can be active, so keeping up two seals means a twist: with **Unsealed Wrath**, your swings store a copy of your active seal, and landing a swing under a different seal spends the copies. The full rotation casts **Seal of Righteousness** in the last 0.4 seconds before each swing and **Seal of Command** after the swing, in any global cooldown that **Hammer of Wrath**, **Consecration** and **Holy Strike** do not need: about 14 and 12 times a minute. Opening with **Seal of Command** means your very first swing already carries both.
- Press **Judgement** every time it is ready while **Seal of Righteousness** is up, whether or not the short list shows it. It is off the global cooldown, comes back every 8 seconds with **Improved Judgement**, no longer uses up your seal in Forever, and **Sanctified Judgement** returns 60% of the seal's mana cost; in the simulator the judgement of **Seal of Righteousness** is about an eighth of your damage. If it comes off cooldown while **Seal of Command** is up, judge anyway.
- **Hammer of Wrath** goes first once the boss is below 20% health: it takes 1 second to cast, it comes back every 6 seconds, and at about 500 Holy damage plus a share of your spell damage it is your biggest single hit.
- **Consecration** comes before **Holy Strike** while you have at least a quarter of your mana: on a single boss it deals 312 Holy damage over 8 seconds plus a share of your spell damage, about a sixth of your damage in the simulator, and **Holy Conduit** makes it 40% cheaper.
- **Holy Strike** sits last but is not a real filler: it has a 10-second cooldown, so press it whenever it is ready (20 mana, and **Sacred Arbiter** adds 20% to it). The global cooldowns between your other buttons go to the seal swaps.
- **Seal of Command** is always rank 4: every rank adds the same 70% of weapon damage, rank 4 costs 30 mana less, and the simulator measured it 0.3% better than rank 5. When mana runs low the full rotation steps down: **Seal of Righteousness** rank 7 below half mana, **Seal of Command** rank 2 below 30%, a rank 1 **Consecration** below a quarter, and no seal swaps at all below 15%.

**Caveats**

- The twist rests on the simulator's reading of **Unsealed Wrath**: your swings store up to 3 copies of your active seal for 15 seconds, and landing a swing under a different seal spends them. This rotation dates from before that talent replaced Twist of Light, and the raid runs test it again.
- All those swaps cost mana. The full-raid numbers assume the raid's **Blessing of Wisdom**, Mana Spring and other paladins' judgements of **Seal of Wisdom** and **Seal of the Crusader** on the boss; with only your own buffs the simulator keeps **Seal of Righteousness** up and twists on every swing only while your mana is above about two thirds.
- Forever weakens ranks far below your level, and the simulator applies an assumed formula (TBC's) since 2026-10-09. **Seal of Command** rank 4 and **Seal of Righteousness** rank 7 are close enough to 60 to lose nothing, but rank 1 **Consecration** keeps only a bit over half of its spell damage bonus, so it is a low-mana stopgap only; the game may also lower a low rank's chance to trigger effects, which no simulator models.
- Several targets: only **Consecration** spreads (its bonus damage hits the first four enemies in it); your seals, judgements and **Holy Strike** stay on one target.
- The full rotation also has a **Holy Shock** line (after **Holy Strike**) for builds that take it, worth several percent there in the simulator; this build has no **Holy Shock**, so skip it.

**When to change it**

- If you cannot time your swings (no swing timer, high latency), skip the swaps: keep **Seal of Righteousness** up, judge it on cooldown and press **Consecration** and **Holy Strike**. How much that costs on the current beta build was not measured.
- Against an Undead or Demon boss, add **Exorcism** on cooldown (15 seconds, 40% cheaper with **Holy Conduit**): it hits harder than **Holy Strike**. The simulator's target is an Elemental, so where it fits best was not measured.
- When you have to leave melee range, keep pressing **Judgement** (10 yards) and, under 20%, **Hammer of Wrath** (30 yards); your seals only work on swings.

## Talents

| Tree | Points | Talents (ranks) |
|---|---|---|
| Holy | 16 | Divine Strength 5, Reverence 2, Improved Seals 5, Holy Conduit 2, Divine Precision 1, Purifying Power 1 |
| Protection | 4 | Divine Intellect 4 |
| Retribution | 31 | Deflection 3, Benediction 4, Improved Judgement 2, Conviction 3, Sanctified Judgement 2, Seal of Command 1, Pursuit of Justice 2, Sacred Arbiter 1, Two-Handed Weapon Specialization 3, Repentance 1, Vengeance 3, Champion of the Light 5, Unsealed Wrath 1 |

## The numbers

| Setting | DPS |
|---|---|
| Full raid, 3-minute fight (every raid buff and debuff: what this page ranks on) | 823 |

> Note: Retribution's equal-tier set (raidsim/gear_opt.py, 2026-09-30) is caster gear: the simulator's stat weights value spell damage more than Strength for this spec, and the set leans on Forever launch items (Leafre's Ring of Precise Spell Power, +100 spell damage). In a full raid it also gains from both the physical and the spell buffs, and in Forever Curse of the Elements covers Holy (beta tooltip: 'Magic damage taken'). Check the launch items' availability before trusting the full-raid number.

**By gear tier** (the spec's best talents for each tier and setting in its own gear, found by this project's machine-learning search in the community simulator, wowsims/forever 16e8542 (client 70790); [every spec](../../_reference/dps-rankings.md)):

| Gear | Full raid DPS | Best talents |
|---|---|---|
| Pre-BiS | 886 | [17/3/31](https://talentsforever.com/paladin/60/0502501022-3-15233001021301351-12) |
| Phase 1 BiS | 900 | [17/3/31](https://talentsforever.com/paladin/60/0502510022-3-25232001021301351-12) (as good as this build in this gear) |

*Each row is in that tier's own gear set; the DPS at the top of the page is this build in the standard set, so the two do not match.*

**The gear** (average item level: Pre-BiS 62.9; Phase 1 BiS 63.2; each item opens its Wowhead page, with where it drops and its enchant):

| Slot | Pre-BiS | Phase 1 BiS |
|---|---|---|
| Head | [Lionheart Helm](https://www.wowhead.com/forever/item=12640) · *Blacksmithing*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11645) | [Lionheart Helm](https://www.wowhead.com/forever/item=12640) · *Blacksmithing*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11645) |
| Neck | [Star of Mystaria](https://www.wowhead.com/forever/item=12103) · *Balnazzar, Stratholme* | [Onyxia Tooth Pendant](https://www.wowhead.com/forever/item=18404) · *quest: For All To See* |
| Shoulders | [Highlander's Lamellar Spaulders](https://www.wowhead.com/forever/item=20058) · *sold by Samuel Hawke* | [Highlander's Lamellar Spaulders](https://www.wowhead.com/forever/item=20058) · *sold by Samuel Hawke* |
| Back | [Arcanoweave Cloak](https://www.wowhead.com/forever/item=272411) · *sold by Pix Xizzix*<br>+ [Enchant Cloak - Lesser Agility](https://www.wowhead.com/forever/spell=13364) | [Arcanoweave Cloak](https://www.wowhead.com/forever/item=272411) · *sold by Pix Xizzix*<br>+ [Enchant Cloak - Lesser Agility](https://www.wowhead.com/forever/spell=13364) |
| Chest | [Dawn Armor](https://www.wowhead.com/forever/item=252483) · *Leatherworking*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) | [Dawn Armor](https://www.wowhead.com/forever/item=252483) · *Leatherworking*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) |
| Wrist | [Rockfury Bracers](https://www.wowhead.com/forever/item=21186) · *quest: Stalwart's Battlegear*<br>+ [Enchant Bracer - Superior Strength](https://www.wowhead.com/forever/spell=19984) | [Rockfury Bracers](https://www.wowhead.com/forever/item=21186) · *quest: Stalwart's Battlegear*<br>+ [Enchant Bracer - Superior Strength](https://www.wowhead.com/forever/spell=19984) |
| Hands | [Stormshroud Gloves](https://www.wowhead.com/forever/item=21278) · *Leatherworking*<br>+ [Enchant Gloves - Strength](https://www.wowhead.com/forever/item=273529) | [Stormshroud Gloves](https://www.wowhead.com/forever/item=21278) · *Leatherworking*<br>+ [Enchant Gloves - Strength](https://www.wowhead.com/forever/item=273529) |
| Waist | [Marksman's Girdle](https://www.wowhead.com/forever/item=22232) · *Urok Doomhowl, Blackrock Spire* | [Marksman's Girdle](https://www.wowhead.com/forever/item=22232) · *Urok Doomhowl, Blackrock Spire* |
| Legs | [Titanic Leggings](https://www.wowhead.com/forever/item=22385) · *Blacksmithing*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11645) | [Titanic Leggings](https://www.wowhead.com/forever/item=22385) · *Blacksmithing*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11645) |
| Feet | [Highlander's Lamellar Greaves](https://www.wowhead.com/forever/item=20049) · *sold by Samuel Hawke*<br>+ [Enchant Boots - Greater Agility](https://www.wowhead.com/forever/item=16245) | [Highlander's Lamellar Greaves](https://www.wowhead.com/forever/item=20049) · *sold by Samuel Hawke*<br>+ [Enchant Boots - Greater Agility](https://www.wowhead.com/forever/item=16245) |
| Finger | [Warden's Signet of Ferocity](https://www.wowhead.com/forever/item=275981) | [Band of Earthen Might](https://www.wowhead.com/forever/item=21182) · *quest: Veteran's Battlegear* |
| Finger | [Cutthroat's Signet](https://www.wowhead.com/forever/item=272408) · *sold by Pix Xizzix* | [Warden's Signet of Ferocity](https://www.wowhead.com/forever/item=275981) |
| Trinket | [Hand of Justice](https://www.wowhead.com/forever/item=11815) · *Emperor Dagran Thaurissan, Blackrock Depths* | [Hand of Justice](https://www.wowhead.com/forever/item=11815) · *Emperor Dagran Thaurissan, Blackrock Depths* |
| Trinket | [Adaptive Combat Assistant](https://www.wowhead.com/forever/item=272437) · *sold by Pix Xizzix* | [Talisman of Ephemeral Power](https://www.wowhead.com/forever/item=18820) · *Magmadar, Molten Core* |
| Main hand | [Fist of Cenarius](https://www.wowhead.com/forever/item=21188) · *quest: Champion's Battlegear*<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) | [Fist of Cenarius](https://www.wowhead.com/forever/item=21188) · *quest: Champion's Battlegear*<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) |
| Ranged/relic | [Libram of Law](https://www.wowhead.com/forever/item=272435) · *sold by Pix Xizzix* | [Libram of Law](https://www.wowhead.com/forever/item=272435) · *sold by Pix Xizzix* |

**Open in the simulator** (the community's Forever simulator on the web, loaded with the gear, enchants, talents, rotation, consumables and buffs we simulate): Pre-BiS: [full raid](https://wowsims.com/forever/paladin/retribution/#eJzEV11sE1cW9hmPxzfHceJc8jO5BJj1Eki86+x4vFmxWSAmYXf52Wi9QVuohCiTeBKbOp50xknhpUor+itKpb60UBQqfloUlVJBK6GovNBWpTwFFdEqEm3kvvSBqjQPPPihqmYcxz/kp6ig3gfrzrlnzj3nu/f7jgebCPhABAlaYD/EYRjGAF4CeBvgHACttFc5a3UDsJsNhPdx7GkUyEyfmPGgk3y+D3kyfQLQTd6a8ok3BHSTTz6sFr+rQje5ehbE29Zk/B0QT7qRJ1+ftzx/eh+st93kxgkQv61Cnrx6x4c8eXPKh07y7l7kyUdTPnSTT8+CeKcKHciTS1M+f5vvWqJl9kn5Xl/01lF4BbjDideBu9d3HITT6nvq9JYJcB9JTJyDo4kZOJzoInb2EIFJbrXcLivtckhWlGA4GGpXwmHZegqF5VC4PXSN4zPc7TpcjyszIGL9lv50YlRNa5JqmonBlBaT1BFD9RMUkA8qsokS1k5ADVZnhUrE6EgyKRlqalAr8liLjRmox9qooQ1LuzQ1KekDUrc+NKSmYn43utAZDJv4Z1yTgSZkJV69icF4WtNHzJRmmv4KdKMrGGprN7EVmzLQiA3dqpkupHZgJDaoDWmpdJErXcv8WOWvRJwlbnS1EHI7moFq9Pboo5qU1qUhLalptJE1oDcrIJLd/5IGR1QjxgTkyYVxsAOsDjQRgXIdDlabFWqwequWVA9JPeoB3ZC6t5odDtrFIvhXpmBjoIEA9RznCAotTnLhCliBkJNNrAusIE7qmnVzxMlsfOQ2xWTzjjRJ96nDySf04bSkyMrfgiE5GA51SP1xC9GYpBuSGotpManvkJSOa5Khp9V0Qk9JpqYa/XGpxdQ0ydDSwdiwGcwvBnOLbQdMPdXK0N7NRT4+DfQ/bAd20k1lZaPX78GKUzBXPa7KCgzFHRaykqGpyYQ5JA0belrrt6KzPKS0mf0RG7JCLdJdcX0kGZMMbcDQzLi0S++e2/TyaVjKrdd2I+SzcaArWE0GqrCyW0+ZWr9hl0mrmTcDiOSfB3WjP2EOic5A82I3lHpYhZ2ci1yJBrYuelNoK1uPK7OCiPXbVHMBBzspgdwch0D/wneY7mTbcRP9B67xr1oyFIpZoQ5X/N/UykMUAAqcgaU4QJ8H9hzgKE0vv9vqrLASG4t3KwmFIfYXbPKzxbPCar8XPRliJQfkjZNQOKDAN3w5g+4C+wHwCNCXYem8iiNiD9u5RAJ+v7RsGfPhXhuL5oie4dzoGtJHtRDdm5/UTQBFX1bwoqfHInxOpajX8GDFLMlTncyT3u13oXOSd9A8Y6zLW2WUyAi9BexLQJM+tXTBljSUQGllWo7tMkdRWpiSL0z5rYXl6FZe2BiwZzBMQ8tfstK8wvTf+cmD5lWWQiBW4Dndwx7DnXS7LaAu6rrKzQuo3QxqAtWWOPc5LMKjMyQ3l4uYneUpyAe3/FoEcj0aSJRJzONs98PdaV5uFf9iGFI7ftoY0ZQ1Cx5+kUPzEkwocmu8r0PRuSak1BZ36ZxVaVdqS0/JhU6EdmVjoS1QmbbZqAhlDSxk5s1FYMltIVN5gVuoF9Afgd556LzvYBvQMy3MUxVb6Xr0XISCQQzUE556JgsmlrtIGGGb76fnn2greqcFzDuLuQgC9VwFYv1/ezEqArNxCi3TI5XrCwHRSy9x9APO3n25Uu/TipJUN7OND6jji2Jnq0ExdjlDCXa2KY/d/9h/f4W0FYFpvz0HJuTB/KoAZng5MLsWX6PrAmsJTysm8mxkdRc5Sjhaccqdt1ia/j13De5yyrNOhz1qI5PAI4cO/89chWVwjA1EGo8fs8YXnX8YsMetTmWGE3mpM3CZc/wuIx3Jzx7pWHf+ke3zd/u390xky5whst/6wjoG9oNjpjPgJJcbuoo+xGTYABHYBlHYA3EYhoNwkPtlANMHAwI=); Phase 1 BiS: [full raid](https://wowsims.com/forever/paladin/retribution/#eJzEV1tsFGUb3nd2dvbru90ePnqYfhSYf38K7f7/9p+d/WuwAl1aVA42riUKJkSZdqfdxe1Ondk25cZUg8cgJHphQFIMByWNiAEvSCNeoCbIFURF0wRtVi+8wIi94GIvjJnZbvdADxIhfhfN1/d79z083/c87y42EqgCESRohj0QgyEYA3gN4D2A0wC03D7lrNN1wL6tJ3wVx0ZRINO9YtqDPPn5ECBPpo4Cusm7V6vEawK6yeefVIo/VaCbXDoF4g1rM/4+iMfcyJPvz1iev38E1sfd5NpREH+sQJ58dsqK8+bNKnSSD3YjT/a/bTl+cQrEmxXoQJ6cv1rla626HG+eeU6+3Ru5fhDeAG5//C3gbvceAeGE+qE6tWkC3AfiE6fhYHwa9sc7iV0+hGGSWym3yUpbUJYVJRAKKG1KSJHloKwEQ3Iw1Ba8zPFp7kYtrsXlaRCxblNfKj6ipjRJNc34QFKLSuqwofoICsgHFNlECWsmoBorM0I5YmQ4kZAMNTmgFXisxoY01GFNxNCGpB2ampD0fqlLHxxUk1GfG13oDIRM/C+uSkMjsiKvnvhALKXpw2ZSM01fGbrRFQi2tpnYgo1paMD6LtVM5UvbOxwd0Aa1ZKrAla5mPqzwlSPOEDe6mgm5EUlDJXq79RFNSunSoJbQNNrA6tGbERDJzkekgWHViDIBeXJ2HOwAK/2NRKBcu4PVZIRqrNysJdR9Ure6Vzekrs1mu4N2sjD+nynY4K8nQD1HOIJCs5OcvQhWIORkE2v9y4iTumbcHHEyGx+5VTHZnCNN0GfUocSz+lBKUmTlgUBQDoSC7VJfzEI0KumGpEajWlTq3SelYppk6Ck1FdeTkqmpRl9MajY1TTK0VCA6ZAZyh4HsYeteU0+2MLSzucinJ4A+xrZhB91Q0jZ6fR4sOw6z3eOKjMBQ3GYhKxmamoibg9KQoae0Pis6y0FKm9i/sT4j1CDdEdOHE1HJ0PoNzYxJO/Su2aQXTsBibj22GyFfjgNdxqrTUIHlXXrS1PoMu01aybxpQCQPj+pGX9wcFJ3+poVeKPWwMrs4F7kY8W9e8KXQFrYWl2cEEeu2qOY8DnZRAvlmHPx9879hup1txQ30IVzlW7FoKBQzQi0ue9LUSkPkAfKfhMU4QF8G9hLgCE0tnW1lRliODYXZikJhkP0PG31s4aqw0udFT5pYxQF55xjkL8j/A1/KoFvAfgU8APR1WLyuwojYzbYvUoDPJy3Zxly4Q2ORLNHTnBtdg/qIFqS7c5vaCaBYlRG86Om2CJ9VKeo1PFg2Q3JUJ3Okd/tc6JzkHTTHGOvxVhhFMkKvA/sa0KTPL96wJQ1FUFqVlmK7xFUUN6bkGlP+bmNZupU2NgbsBQzR4NKPrLiuEH00t7nbukpK8EfzPKe72FO4nW61BdRFXZe4OQG1h0G1v9IS516HRXh0BuWmUhGzqzwOueCWX7NArkT88RKJeZrtvLeZ5uRW8S2EIbXjp4xhTVk17+UXODQtwoQCt4Y7JhSdHUJKTeGUzlqVNqWm+JZc6ERoU9bnxwKVaauNilAywIJmzlwAltwaNJVXuPlmAf0N6M17zvt2tg49U8IcVbGFrkXPOcgbRH8d4alnMm9i2YeEYbbxTnr+h7agd0rAnLOYjSBQzyUg1ve3VyMiMBun4BIzUrkyHxA99DxHP+bs7Eu1eodWFJW6ka2/Sx1fEDtbDQqxyxqKsLNNOeyeYI//BWkrANP+9CyYkAPzuzyYoaXA7Fz4jK7xryY8LZvIsZHVnuMo4WjZcXfOYmn6L9xluMUpLzod9qoJTwKPHDp8f3BllsEx1h9uOHLYWl91/KvfXtc7lGlO5KUO/wXO8Y+sVDi3u69rzZn7ludB+2/PyfCmWUN4j/UT6zDY/zimO/xOcqG+s+CXmAzrIAxbIAK7IAZDMAqj3J8DAMFjAsM=).

**Points that do nothing for this spec:** **Repentance** (1) only counts toward the points the tree needs before **Champion of the Light** and **Unsealed Wrath**.

## Other builds of this spec

- [Retribution — Raid](../research/raid/builds/retribution-ml-raid.md) (9/14/28, 657 DPS in a full raid) — [open the talent tree](https://talentsforever.com/paladin/60/05013-053020004-1523330100130033-12)

---
*Generated by `_reference/data/render_modes.py` on 2026-11-11 from this project's builds and simulations of the WoW: Forever beta (talent and spell data: client build 1.60.1.70753; raid numbers: the official wowsims/forever simulator at ff9babb (client 1.60.1.70888)). Simulations, not in-game measurements. Do not hand-edit.*

