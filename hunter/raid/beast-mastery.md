# Beast Mastery Hunter — Raid (group)

[Hunter](../README.md) > [Raid (group)](README.md) > Beast Mastery

**[Beast Mastery — Raid](../research/raid/builds/beast-mastery-ml-raid.md)** (31/20/0) — [open the talent tree](https://talentsforever.com/hunter/60/5320001505101251-00530502005--7)

> 🔬 Derived build: found by this project's machine-learning search over every legal build of the spec in the community's raid simulator (phase-1 BiS gear, then raced against the spec's builds). A model of the beta, to check at launch.

## How to play

**Before the pull:** **Aspect of the Hawk**, **Aimed Shot**.

**Keep up all fight:** **Aspect of the Hawk**.

**Then press the first one that is ready**, top to bottom:

1. **Serpent Sting**: keep it on the target
2. **Arcane Shot**
3. **Rapid Fire**
4. **Aimed Shot**

Between these, **Auto Shot** keeps firing on its own.

**Advanced: your cooldowns and extras.** Once the list above feels easy, add these:

- **Bestial Wrath**: a cooldown, use it at the start of the fight and again whenever it is ready (about 2 times a fight)
- Use your trinkets and a potion together with your big cooldowns.

*The simulator's full rotation for this build, with every condition: [research rotation page](../research/raid/rotation.md).*

## Why this rotation

Beast Mastery in a raid is **Auto Shot** and your pet with a short list on top: keep **Serpent Sting** ticking, fire **Arcane Shot** and **Aimed Shot** each time their cooldowns end, and send **Bestial Wrath** whenever it is ready.

**Why it works**

- **Serpent Sting** comes first so it never drops: on the training dummy it is about 15% of this build's damage, 20% more with **Improved Stings**. Recast it only as it runs out, since a new sting replaces the old one and its last ticks; the full-raid rotation recasts it only while you have 30% mana or more.
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
- Watch your ranks: in the beta client (build 70425) **Hunter's Mark** rank 4 gives +71 ranged attack power against rank 3's +98, and **Trueshot Aura** rank 5 +50 against rank 4's +75 (if your build has it); cast the stronger lower rank from your spellbook until Blizzard fixes the numbers. **Aspect of the Hawk** rank 7 (+120) is the best at 60. The simulator's numbers use **Hunter's Mark** rank 4, so they read about 0.3% low (estimate).

**When to change it**

- Two or more targets close together: **Multi-Shot** instead of **Aimed Shot** on their shared cooldown, since it hits up to 3 targets for weapon damage each while **Aimed Shot** adds 166 to one. For a pack, **Volley**: a 6-second channel with no cooldown in Forever, which holds **Auto Shot** while you channel.
- In the last few seconds, skip the **Serpent Sting** refresh: its damage comes over 15 seconds. The simulator's other hunter rotations stop refreshing it 3 to 6 seconds before the end.
- Inside 8 yards your shots and **Auto Shot** stop. Step back out; if you cannot, **Summon Hawk** still works, as it has no minimum range.

*This guide was written for the rotation of 2026-10-15; the list above was re-tuned since, so follow the list where the two differ.*

## The numbers

| Setting | DPS |
|---|---|
| Full raid, 3-minute fight (every raid buff and debuff: what this page ranks on) | 768 |

**By gear tier** (the spec's best talents for each tier and setting in its own gear, found by this project's machine-learning search in the community simulator, wowsims/forever 30f67f5 (client 70450); [every spec](../../_reference/dps-rankings.md)):

| Gear | Full raid DPS | Best talents |
|---|---|---|
| Pre-BiS | 746 | [31/20/0](https://talentsforever.com/hunter/60/5321001505001251-00500505005--7) |
| Phase 1 BiS | 770 | [31/20/0](https://talentsforever.com/hunter/60/5320001505101251-00520503005--7) |

**The gear** (average item level: Pre-BiS 63.4; Phase 1 BiS 65.2; each item opens its Wowhead page, with where it drops and its enchant):

| Slot | Pre-BiS | Phase 1 BiS |
|---|---|---|
| Head | [Black Dragonscale Helm](https://www.wowhead.com/forever/item=252605) · *Leatherworking*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11647) | [Black Dragonscale Helm](https://www.wowhead.com/forever/item=252605) · *Leatherworking*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11647) |
| Neck | [Amulet of the Darkmoon](https://www.wowhead.com/forever/item=19491) | [Onyxia Tooth Pendant](https://www.wowhead.com/forever/item=18404) |
| Shoulders | [Theramore Pauldrons](https://www.wowhead.com/forever/item=271955) | [Theramore Pauldrons](https://www.wowhead.com/forever/item=271955) |
| Back | [Expeditionary's Cape](https://www.wowhead.com/forever/item=271907)<br>+ [Enchant Cloak - Lesser Agility](https://www.wowhead.com/forever/spell=13364) | [Earthweave Cloak](https://www.wowhead.com/forever/item=21187)<br>+ [Enchant Cloak - Lesser Agility](https://www.wowhead.com/forever/spell=13364) |
| Chest | [Dawn Armor](https://www.wowhead.com/forever/item=252483) · *Leatherworking*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) | [Dawn Armor](https://www.wowhead.com/forever/item=252483) · *Leatherworking*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) |
| Wrist | [Forest Stalker's Bracers](https://www.wowhead.com/forever/item=19587)<br>+ [Enchant Bracer - Superior Strength](https://www.wowhead.com/forever/spell=19984) | [Forest Stalker's Bracers](https://www.wowhead.com/forever/item=19587)<br>+ [Enchant Bracer - Superior Strength](https://www.wowhead.com/forever/spell=19984) |
| Hands | [Theramore Handwraps](https://www.wowhead.com/forever/item=271945)<br>+ [Enchant Gloves - Agility](https://www.wowhead.com/forever/item=273520) | [Theramore Handwraps](https://www.wowhead.com/forever/item=271945)<br>+ [Enchant Gloves - Agility](https://www.wowhead.com/forever/item=273520) |
| Waist | [Highlander's Mail Girdle](https://www.wowhead.com/forever/item=20044) | [Highlander's Mail Girdle](https://www.wowhead.com/forever/item=20044) |
| Legs | [Outrider's Chain Leggings](https://www.wowhead.com/forever/item=22673)<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11647) | [Outrider's Chain Leggings](https://www.wowhead.com/forever/item=22673)<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11647) |
| Feet | [Beaststalker's Boots](https://www.wowhead.com/forever/item=16675) · *Nerub'enkan, Stratholme*<br>+ [Enchant Boots - Greater Agility](https://www.wowhead.com/forever/item=16245) | [Beaststalker's Boots](https://www.wowhead.com/forever/item=16675) · *Nerub'enkan, Stratholme*<br>+ [Enchant Boots - Greater Agility](https://www.wowhead.com/forever/item=16245) |
| Finger | [Signet Ring of the Bronze Dragonflight](https://www.wowhead.com/forever/item=21205) | [Signet Ring of the Bronze Dragonflight](https://www.wowhead.com/forever/item=21205) |
| Finger | [Channeler's Ring](https://www.wowhead.com/forever/item=272406) | [Band of Sulfuras](https://www.wowhead.com/forever/item=19138) · *Ragnaros, Molten Core* |
| Trinket | [Rune of the Guard Captain](https://www.wowhead.com/forever/item=19120) | [Shard of the Splithooves](https://www.wowhead.com/forever/item=10659) |
| Trinket | [Adaptive Combat Assistant](https://www.wowhead.com/forever/item=272437) | [Adaptive Combat Assistant](https://www.wowhead.com/forever/item=272437) |
| Main hand | [Thorium Poleaxe](https://www.wowhead.com/forever/item=250615) · *Blacksmithing*<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) | [Thorium Poleaxe](https://www.wowhead.com/forever/item=250615) · *Blacksmithing*<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) |
| Ranged/relic | [Premier High Warlord's Recurve](https://www.wowhead.com/forever/item=272594)<br>+ [Biznicks 247x128 Accurascope](https://www.wowhead.com/forever/item=18283) | [Rhok'delar, Longbow of the Ancient Keepers](https://www.wowhead.com/forever/item=18713)<br>+ [Biznicks 247x128 Accurascope](https://www.wowhead.com/forever/item=18283) |

**Open in the simulator** (the community's Forever simulator on the web, loaded with the gear, enchants, talents, rotation, consumables and buffs we simulate): Pre-BiS: [full raid](https://wowsims.com/forever/hunter/dps/#eJzEVEFIFF8c3t+b2Z23v79/d/6j/nccJKYNZF2Y5c3UiBqxq6dOIZ06laO7tiPlLjt70ENgZRAiQYciRTDYJJGCggQJuhiCwoJrUkEZSSl06OAt6hAx4y5FdlT6DsP3fh/zvu+beTxsoiCCDCpEoQcykIMRgOsAdwFmAaQaTyWu2gbKtkCpyCmXUKDP5kPy1j/I0+IdQJ6ul0QUaLEkymsBFOjzJyH5Yy0K9OoEyO9cslIS5fe1yNPSFKBAbz4G93WBFq/A7vzljLvP7bKIPH10y+XzZXfPLzMh+XMt+lCgL9ZE+W1dpFlctqNb0zAGZNSehGDRemBtdE7PwBwI4/b9Kbhhb8Ko3VXzs1kSnpIm86ihM6abzGRMN0xdYy7zluYy4cuEfiAbfqxHqgSQp+UliFAMIK/pzMGGynS2CJEgCujXjLjpSNdAOmvlLpzL5gqqwYxWTWea3tqh9mWswfPplJrNq1YqlU6pvcNqIZNW89mCVbCzg6qTtvJ9GTXqpNNq70Utb9kprSpqu2J8wMkOtihHsDEWppxEB9xUq0ugeP4sbpiOUhlJvEI6fJK9Nwxr39cwguJHjq5mpeE/9D62r1Zh/PdNAJGniyPdEhF5r6vLTyjH0ZAY1sckykn+RUKoXxHQjxyL6yjH/qecFJyDyt+qKqaXfDssDfyWnLVrRtu+Jt89Ka+/ntrjpTONGQfgNVsESVUOYUOsjvqrn8Q7vCxuOl7z9XqZ+0SWYYcYlzmfh2hyDOrwPwyJ38ZBDrT4POwkIt9J0GW+kf5k4+SEi5XE4X4PrxLGJpF5NRFbIL6/gkKyyg4UzQ8PzKfde56+l+ysDJI97pU7Ad7Ct5mIcXQh3PXLzcygDZJwErrhDGQgB0MwRH4MAD8fLQs=); Phase 1 BiS: [full raid](https://wowsims.com/forever/hunter/dps/#eJzEVEFoE1sUzX0zybzc39/kv7Y/06F85udDSQMT3kz/lLYiSbtyJUU3rrTTJjVTtAlJFi24iFpBSlEUXKQUKsRgKboQLBTBTaXQQqGVooJWLBrBhYvuRBciM01QrMsWz2K4cw/zzjnzLhfbKARBBhUiMAhpyEIR4CrAbYB5ANbgssRhu0GpSpQGBeUCSvTxYkCu/oEirV4HFOnWehAl+qQC8lOfUzwMyO8aUaKXSyC/doq19aD8phFFuj4LKNEbD8D5XKLlS7DXf1Zxzlm+BSjQ8kkU6eKmc+SnSkD+2IgelGjpJsivmsLtwVU7Up2DKSCT9gz4y9Y9a7tvrgILIE3bd2fhmr0Dk3Z/w/dgCXhE2sxOg3Oum9zUuW6Yusa5aXCTd3JurhJxk9C3ZNuLzUgVH4p0cwXCFH0oajrPY0utO1+GsB8l9GpGzMyzK8BOW9lzZzLZgmpwo0vTuaZ39arDaWvsbCqpZnKqlUymkurQhFpIp9RcpmAV7MyYmk9ZueG0GsmnUurQeS1n2UmtTmp7ZGw0nxnrUP7D1miICoyOOq42VkBx9XnMMPNKrcVEhfR6mL3fDO85UDOS4kWBbmTYxC9y/3+gUiH886UPnZEoDjASFN2sy8UBdlQ5ggbj2BxlVGDeZUKoV5HQiwKP6ShH/6YC8y9A7bbqjOk6fx9ioz855z2a0X2gzvcm5cXn4/u0dK5x4xC05svAVOUfbIk2UW/9l7jDy2Nm3k2+1SwLH8gq7BLjouBxEUlMQRP+hYHgl2mQfR0eF7vx8FfidypPcSTROlNysBb/d8TF87ixQ2RRjUeXiOe3oJCoV4eK9vuHptPjPk/cSfTVGolBZ+OWwH3x7MSjAl0K9f+wmDl0QwKOwQCcgjRkYRzGybcBAOkCLDU=).

## Other builds of this spec

- [Beast Mastery (optimized, with a pet)](../research/raid/builds/opt-mm-raid-raid-dps.md) (31/16/4) — [open the talent tree](https://talentsforever.com/hunter/60/5420001505001251-0050550001-4-7)

---
*Generated by `_reference/data/render_modes.py` on 2026-10-26 from this project's builds and simulations of the WoW: Forever beta (talent and spell data: client build 1.60.1.70425; raid numbers: the official wowsims/forever simulator at 30f67f5 (client 1.60.1.70450)). Simulations, not in-game measurements. Do not hand-edit.*

