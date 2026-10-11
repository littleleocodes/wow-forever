# Beast Mastery Hunter — Raid (group)

[Hunter](../README.md) > [Raid (group)](README.md) > Beast Mastery

**[Beast Mastery — Full raid](../research/raid/builds/beast-mastery-ml-parse.md)** (31/20/0) — [open the talent tree](https://talentsforever.com/hunter/60/5320001505101251-00532500005--6)

> 🔬 Derived build: searched in the community's raid simulator from the spec's best build. A model of the beta, to check at launch.

## How to play

**Before the pull:** **Aspect of the Hawk**, **Aimed Shot**.

**Keep up all fight:** **Aspect of the Hawk**.

**Then press the first one that is ready**, top to bottom:

1. **Serpent Sting**: keep it on the target, when you have at least 30% mana
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

- **Pre-BiS gear** (average item level 63.2): Head: Black Dragonscale Helm; Neck: Mark of Fordring; Shoulders: Theramore Pauldrons; Back: Earthweave Cloak; Chest: Dawn Armor; Wrist: Forest Stalker's Bracers; Hands: Theramore Gloves; Waist: Warpwood Binding; Legs: Outrider's Chain Leggings; Feet: Windreaver Greaves; Finger: Signet Ring of the Bronze Dragonflight; Finger: Don Julio's Band; Trinket: Blackhand's Breadth; Trinket: Royal Seal of Eldre'Thalas; Main hand: Barbarous Blade; Ranged/relic: Premier High Warlord's Recurve
- **Phase 1 BiS gear** (average item level 66.6): Head: Black Dragonscale Helm; Neck: Onyxia Tooth Pendant; Shoulders: Giantstalker's Epaulets; Back: Earthweave Cloak; Chest: Giantstalker's Breastplate; Wrist: Giantstalker's Bracers; Hands: Giantstalker's Gloves; Waist: Giantstalker's Belt; Legs: Dragonstalker's Legguards; Feet: Giantstalker's Boots; Finger: Band of Accuria; Finger: Signet Ring of the Bronze Dragonflight; Trinket: Blackhand's Breadth; Trinket: Royal Seal of Eldre'Thalas; Main hand: Barbarous Blade; Ranged/relic: Rhok'delar, Longbow of the Ancient Keepers

## Other builds of this spec

- [Beast Mastery — Raid](../research/raid/builds/beast-mastery-raid.md) (30/21/0, 810 DPS in a full raid) — [open the talent tree](https://talentsforever.com/hunter/60/522002150510025-00534500013--6)

---
*Generated by `_reference/data/render_modes.py` on 2026-10-11 from this project's builds and simulations of the WoW: Forever beta (client build 1.60.1.70291). Simulations, not in-game measurements. Do not hand-edit.*

