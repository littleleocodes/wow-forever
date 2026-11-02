# Elemental-Enhancement Shaman — Raid (group)

[Shaman](../README.md) > [Raid (group)](README.md) > Elemental-Enhancement

*A melee shaman: Enhancement's Stormstrike and Flurry with Elemental's shock and Fire Nova talents.* (a hybrid: Elemental/Enhancement).

**[Elemental-Enhancement — Raid](../research/raid/builds/elemental-enhancement-ml-raid.md)** (17/29/5) — [open the talent tree](https://talentsforever.com/shaman/60/503303102-05303003100510224-05-7)

> 🔬 Derived build: found by this project's machine-learning search over every legal build of the spec in the community's raid simulator (phase-1 BiS gear, then raced against the spec's builds). A model of the beta, to check at launch.

## How to play

**Before the pull:** **Strength of Earth Totem**, **Grace of Air Totem**, **Searing Totem**.

**Keep up all fight:** **Strength of Earth Totem**, **Grace of Air Totem**, **Magma Totem**, **Searing Totem**.

**Then press the first one that is ready**, top to bottom:

1. **Stormstrike**
2. **Flame Shock**: keep it on the target, until the last 10 seconds of the fight
3. **Lightning Bolt** when Maelstrom Weapon has 5 or more stacks
4. **Earth Shock**
5. **Fire Nova**
6. **Rockbiter Weapon**

**Rockbiter Weapon** is your filler: cast it whenever nothing above is ready.

*The simulator's full rotation for this build, with every condition: [research rotation page](../research/raid/rotation.md).*

## Why this rotation

This hybrid is a melee shaman: Enhancement's **Stormstrike** and **Flurry** with Elemental's shock and **Fire Nova** talents. It plays the Enhancement raid list without its **Maelstrom Weapon** bolt: **Stormstrike**, **Flame Shock**, **Earth Shock** and **Fire Nova** between your swings, which with **Windfury Weapon** do about half the damage.

**Why it works**

- Before the pull, drop **Strength of Earth Totem**, **Grace of Air Totem** and **Searing Totem**; the first two last 5 minutes, so one cast covers the fight.
- **Stormstrike** first: 125 mana, a weapon hit and 20% more on your next **Earth Shock**; with **Improved Stormstrike** each one keeps half your mana regeneration going while you cast for 15 seconds.
- **Flame Shock** whenever the burn is off the target, **Earth Shock** on every other free shock. Your Elemental points shape them: 3 points in **Reverberation** bring the shared cooldown to 5.4 seconds, **Convection** and **Shamanistic Focus** cut their cost, and **Call of Flame** adds 15% to **Flame Shock**, **Fire Nova** and **Searing Totem**.
- **Fire Nova** last: it erupts around your Fire totem, so keep **Searing Totem** within 10 yards of the boss and replace it when it expires. **Trial by Fire** makes it 20% stronger on a 6-second cooldown; adding Fire Nova to this list measured about 7% more damage in the rotation search.
- **Elemental Devastation** turns every spell crit into 9% more melee crit chance for 10 seconds, which feeds **Flurry**: another reason to keep a shock going between swings.
- Put **Windfury Weapon** on your weapon with a sharpening stone on top: in Forever an imbue and a stone stack.

**Caveats**

- No **Maelstrom Weapon** and no **Rage of the Farseer** (26 Enhancement points): the list's **Lightning Bolt** line never fires for this build. Use your trinkets and potion at the pull.
- Mana: **Improved Stormstrike**, **Mindfulness** and **Totemic Focus** pay for the shocks; with only your own buffs the simulator's build is out of mana for about 12 seconds of a 3-minute fight. Use a mana potion when low, and do not hold shocks back.
- Several targets: **Fire Nova** hits every enemy within 10 yards of your Fire totem.
- For a **Lightning Bolt** caster, play Elemental: this split is a melee build.

**When to change it**

- In the last 10 seconds, skip **Flame Shock** (its burn would not finish) and use **Earth Shock**.
- In a party of warriors and rogues, ask whether they want **Windfury Totem** instead of **Grace of Air Totem**: a party gets only one, and it does nothing for you while you use **Windfury Weapon**.

*This guide was written for the rotation of 2026-10-15; the list above was re-tuned since, so follow the list where the two differ.*

## The numbers

| Setting | DPS |
|---|---|
| Full raid, 3-minute fight (every raid buff and debuff: what this page ranks on) | 682 |

**By gear tier** (the spec's best talents for each tier and setting in its own gear, found by this project's machine-learning search in the community simulator, wowsims/forever 54ceac6 (client 70707); [every spec](../../_reference/dps-rankings.md)):

| Gear | Full raid DPS | Best talents |
|---|---|---|
| Pre-BiS | 726 | this build |
| Phase 1 BiS | 755 | [17/29/5](https://talentsforever.com/shaman/60/053303102-05303003100510224-05-7) (ties this build) |

**The gear** (average item level: Pre-BiS 65.8; Phase 1 BiS 65.2; each item opens its Wowhead page, with where it drops and its enchant):

| Slot | Pre-BiS | Phase 1 BiS |
|---|---|---|
| Head | [Black Dragonscale Helm](https://www.wowhead.com/forever/item=252605) · *Leatherworking*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11645) | [Black Dragonscale Helm](https://www.wowhead.com/forever/item=252605) · *Leatherworking*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11645) |
| Neck | [Beads of Ogre Might](https://www.wowhead.com/forever/item=22150) | [Onyxia Tooth Pendant](https://www.wowhead.com/forever/item=18404) |
| Shoulders | [Warlord's Mail Spaulders](https://www.wowhead.com/forever/item=16580) | [Warlord's Mail Spaulders](https://www.wowhead.com/forever/item=16580) |
| Back | [Earthweave Cloak](https://www.wowhead.com/forever/item=21187) | [Sergeant Major's Cape](https://www.wowhead.com/forever/item=16337) |
| Chest | [Darkmantle Tunic](https://www.wowhead.com/forever/item=22009)<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) | [Onyxia Scale Breastplate](https://www.wowhead.com/forever/item=15141) · *Leatherworking*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) |
| Wrist | [Rockfury Bracers](https://www.wowhead.com/forever/item=21186)<br>+ [Enchant Bracer - Superior Strength](https://www.wowhead.com/forever/spell=19984) | [Rockfury Bracers](https://www.wowhead.com/forever/item=21186)<br>+ [Enchant Bracer - Superior Strength](https://www.wowhead.com/forever/spell=19984) |
| Hands | [General's Mail Gauntlets](https://www.wowhead.com/forever/item=16574)<br>+ [Enchant Gloves - Strength](https://www.wowhead.com/forever/item=273529) | [General's Mail Gauntlets](https://www.wowhead.com/forever/item=16574)<br>+ [Enchant Gloves - Strength](https://www.wowhead.com/forever/item=273529) |
| Waist | [Belt of Preserved Heads](https://www.wowhead.com/forever/item=20216) | [Belt of the Archmage](https://www.wowhead.com/forever/item=18405) · *Tailoring* |
| Legs | [Outrider's Chain Leggings](https://www.wowhead.com/forever/item=22673)<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11645) | [Ironfeather Leggings](https://www.wowhead.com/forever/item=252486) · *Leatherworking*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11645) |
| Feet | [Premier Centurion's Mail Boots](https://www.wowhead.com/forever/item=273336)<br>+ [Enchant Boots - Greater Agility](https://www.wowhead.com/forever/item=16245) | [Premier Centurion's Mail Boots](https://www.wowhead.com/forever/item=273336)<br>+ [Enchant Boots - Greater Agility](https://www.wowhead.com/forever/item=16245) |
| Finger | [Don Julio's Band](https://www.wowhead.com/forever/item=19325) | [Quick Strike Ring](https://www.wowhead.com/forever/item=18821) · *Magmadar, Molten Core* |
| Finger | [Signet Ring of the Bronze Dragonflight](https://www.wowhead.com/forever/item=21205) | [Don Julio's Band](https://www.wowhead.com/forever/item=19325) |
| Trinket | [Adaptive Combat Assistant](https://www.wowhead.com/forever/item=272437) | [Adaptive Combat Assistant](https://www.wowhead.com/forever/item=272437) |
| Trinket | [Jewel of the Guard Captain](https://www.wowhead.com/forever/item=270225) | [Talisman of Ephemeral Power](https://www.wowhead.com/forever/item=18820) · *Magmadar, Molten Core* |
| Main hand | [Grand Marshal's Demolisher](https://www.wowhead.com/forever/item=23455)<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) | [Grand Marshal's Demolisher](https://www.wowhead.com/forever/item=23455)<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) |
| Ranged/relic | [Totem of the Storm](https://www.wowhead.com/forever/item=23199) | [Totem of the Storm](https://www.wowhead.com/forever/item=23199) |

**Open in the simulator** (the community's Forever simulator on the web, loaded with the gear, enchants, talents, rotation, consumables and buffs we simulate): Pre-BiS: [full raid](https://wowsims.com/forever/shaman/enhancement/#eJzElU1IW1kUx3Pue8m7OSMar8q8eTgzz8gMTmZeeHkxEt0kuhpmpa7cjU/znGQ+kpAXZpyVCuIMMqO4cVBmcKCVllYLXUhtsS3YEuzORWtBkYq14KKLUkq/oKXcl6RY6Tb2LC4n5/5Pzu+++4eLjRR8IIMKLdAPScjCKMCfAP8DnAVgVc4u4btRUHa91OOTlN9QoldXauT9j1CkE8uAIr05xtcbi4ASfXEe5PvVKNH1RZB3eXJtDOQFCUX6/D8umLkIvFeiq3d98r1qFOmrWd5+Z5GvK5s+FOnMdR9KdOESyA+r0YUiXVgB/9e+jVTL45+6t6ag70n/JJDx1Dx4TplL5nbnOfD+lTrzLzwITaX2YDzVRR10iMMV8llED4f1cEg3ND0S1sM6z/VISDeMVk2PbBDYJMI+OZCwAani4eML4PeihG6tNRixsa5Uni6AX0I3ClrYxnqUFDcKtNBTkoaCEZt9rnyKdYFaKjL3pEAo8D4kul3+2+MC8o5gugBMVEiHi6FSHHn7D2D/ABsysz9/n8nmVUM32jS9XTOiHepg0kz/YCXUTE41EwkroQ78ruaTlprL5M18KpNWbcvMDSbVFtuyVCudNNOD1i9WOq8lsrZWFmlFUfBHO5P+StGwmTVhlR+RGnz80gFgbaCGehj5zqU4Zw+VWJcOgM0eJwvpmtFWEbJvimTbHi8KdKeXEZ9YJhsokRmRL5wb2ellf78HTG+vCFgzKgGZeph3HfgXu/xMVhw/tAaNUNThOfyVTZzcFTYetZfw1l4cpNDDvErRtRd6WO7EkIpWnnsqs5ET80tD2StrI9wrzqHXRmThkGzAI2KMCS4n6uMvwaOISCj4XxMvL7lGh+KfzM/xuBVrGnJiK2bsEVlUY4FV4vogkY+Xs4rGl8sVm9PurL2n452lQryfPzVz4Pxw7cUCAl39uOvIi6RDFOLwLXRDHyQhC8MwTN4MAK5NbmQ=); Phase 1 BiS: [full raid](https://wowsims.com/forever/shaman/enhancement/#eJzElV9IG1kUxnPuTGZuzorGq7Kzg7s7RnZxszthMjESfUn0adkn9cm3dTTjJvsnCZmsuE9RcHeLtIYiWJSChVZaiu1TpbbYPkgJ9s1CsaCUio3gQx9KKS0UWspMkmKlr7Hn4XLm3O/e87tzP7jYSsELEijQAcOQgAxMApwCuABwBYDVObPEno2AvOuhgleU/0aR3lltkPa/QJ6WCoA8vTcFyNEHeRTo8rj0tB5FurEM0mM7uTsF0pKIPD0oAIq0eMNZKdK1R17pST3y9N85e4u38/a4uuVFnk7P2cqlmyA9q0cX8nRpFXw/ejeTHS/+6N+ehaGXwzNAppOLIFw0Voyd3qvgOZ28fB4OgrPJPZhO9lEHHGJwm3yjhUMhLRTUdFULh7SQZudaOKjpeqeqhTcJbBFun5REbEEqC8jTs0XweVBEt9oZCFvYVCkXiuAT0Y2cGrKwGUXZjRwtDlSkwUDYYt/KX2OTv5HyzD3DEQr2OiSaVd32uIB8JCgUgfEy6XExlMstH/4P7BywMSPz56/pTE7RNb1L1bpVPdKjjCaM1G9mXElnFSMeN+PKyD9KLmEq2XTOyCXTKcUyjexoQumwTFMxUwkjNWr+ZaZyajxjqVWRWhYFfrfSqR9kFdtZG9b5EKlut18pATb6G6jAyC8u2Tl7sMK6UgI2f5wsqKl6V03IfiqT7Qge5OjuICNevko2UiHTw985N7I7yM58AkzrrglYO8p+iQrMswH2H7v1WpIdP3QG9GDE4TkcZ/+d3BW2HrUX98FeNkhxgHnksmuvD7DsiSGVrbzwSmL5E/NLS9Ur63nbK86h1/MSd0g24TnRpziXE82xNyDIPBIKvnfEY5dck2OxrxYX7LgfbRtzYjuq7xGJV6L+NeL6LJGLVbOaxvfXatan2xkHL8V6K4XYsP3QLIDz4dqL+jm69mXfkfdIgwjE4GfohyFIQAYmYIK8HwDKBG12).

---
*Generated by `_reference/data/render_modes.py` on 2026-11-02 from this project's builds and simulations of the WoW: Forever beta (talent and spell data: client build 1.60.1.70707; raid numbers: the official wowsims/forever simulator at 54ceac6 (client 1.60.1.70707)). Simulations, not in-game measurements. Do not hand-edit.*

