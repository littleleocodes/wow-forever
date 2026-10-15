# Elemental-Enhancement Shaman — Raid (group)

[Shaman](../README.md) > [Raid (group)](README.md) > Elemental-Enhancement

*A Lightning Bolt caster that dips Enhancement for its passive bonuses.* (a hybrid: Elemental/Enhancement).

**[Elemental-Enhancement — Raid](../research/raid/builds/elemental-enhancement-ml-raid.md)** (17/26/8) — [open the talent tree](https://talentsforever.com/shaman/60/500333102-0550300210051022-05201-6)

> 🔬 Derived build: found by this project's machine-learning search over every legal build of the spec in the community's raid simulator (phase-1 BiS gear, then raced against the spec's builds); it beat the hand-made build (elemental-raid-dps), which stays below as the alternative. A model of the beta, to check at launch.

## How to play

**Before the pull, then keep up all fight:** **Strength of Earth Totem**, **Grace of Air Totem**, **Searing Totem**.

**Then press the first one that is ready**, top to bottom:

1. **Stormstrike**
2. **Flame Shock**: keep it on the target, until the last 10 seconds of the fight
3. **Earth Shock**
4. **Fire Nova**

Between these, your white swings do the rest.

*The simulator's full rotation for this build, with every condition: [research rotation page](../research/raid/rotation.md).*

## Why this rotation

This hybrid is a melee shaman, not a caster: it plays the Enhancement list, and its 22 Elemental points make your shocks and **Fire Nova** cheaper, more frequent and harder hitting. Your weapon and **Windfury Weapon** still do about half the damage; spells fill the gaps between swings.

**Why it works**

- The order is Enhancement's: **Stormstrike** first (125 mana, a weapon hit, 20% more on your next **Lightning Bolt** or **Earth Shock**, and **Improved Stormstrike**'s mana regeneration while casting), then **Flame Shock** whenever the burn is off, a 5-stack **Lightning Bolt**, **Searing Totem** when it expires, **Earth Shock**, and **Fire Nova**.
- Your Elemental points shape the shocks: **Reverberation** brings the shared shock cooldown to 5 seconds, **Convection** and **Shamanistic Focus** cut their cost, and **Call of Flame** adds 15% to **Flame Shock**, **Fire Nova** and **Searing Totem**.
- You have 4 of 5 points in **Maelstrom Weapon**, so 5 stacks leave the bolt a half-second cast at a fifth of its mana. Still wait for 5 stacks: the rotation's condition is above 4.2 stacks, and the simulator measured waiting for 5 about 5% better than casting at 3 with this list.
- **Fire Nova** erupts around your Fire totem, so keep **Searing Totem** within 10 yards of the boss; **Improved Fire Nova** makes it 20% stronger on a 6-second cooldown. Adding Fire Nova to this list measured 7% more damage.
- **Elemental Devastation** turns every spell crit into 9% more melee crit chance for 10 seconds, which feeds **Flurry**: another reason to keep a spell going between swings.
- Put **Windfury Weapon** on your weapon with a sharpening stone on top: in Forever an imbue and a stone stack.

**Caveats**

- No **Rage of the Farseer**: it needs 30 Enhancement points and this build has 29. Use your trinkets and potion at the pull instead.
- Mana is tighter than for Enhancement: the simulator has this build out of mana for about 34 seconds of a 3-minute fight. Clearcasting from **Elemental Focus** makes your next damage spell free; use a mana potion when you are low, and do not hold shocks back.
- Several targets: **Fire Nova** hits every enemy within 10 yards of your Fire totem.
- A caster split of these trees (29/22/0) was the search's best only on the training dummy; in a full raid this melee build measured 22% ahead of the hand-made caster draft. For a Lightning Bolt caster, play Elemental.

**When to change it**

- In the last 10 seconds, skip **Flame Shock** (its burn would not finish) and use **Earth Shock**.
- In a party of warriors and rogues, ask whether they want **Windfury Totem** instead of **Grace of Air Totem**: a party gets only one, and it does nothing for you while you use **Windfury Weapon**.

## The numbers

| Setting | DPS |
|---|---|
| Full raid, 3-minute fight (every raid buff and debuff: what this page ranks on) | 690 |

**By gear tier** (the spec's best talents for each tier and setting in its own gear, found by this project's machine-learning search in the community simulator; [every spec](../../_reference/dps-rankings.md)):

| Gear | Full raid DPS | Best talents |
|---|---|---|
| Pre-BiS | 691 | [17/25/9](https://talentsforever.com/shaman/60/500333102-0540300210051022-05301-6) |
| Phase 1 BiS | 719 | this build |

**The gear** (average item level: Pre-BiS 63.0; Phase 1 BiS 65.7; each item opens its Wowhead page, with where it drops and its enchant):

| Slot | Pre-BiS | Phase 1 BiS |
|---|---|---|
| Head | [Black Dragonscale Helm](https://www.wowhead.com/forever/item=252605) · *Leatherworking*<br>+ [Lesser Arcanum of Voracity](https://www.wowhead.com/forever/item=11645) | [Black Dragonscale Helm](https://www.wowhead.com/forever/item=252605) · *Leatherworking*<br>+ [Lesser Arcanum of Voracity](https://www.wowhead.com/forever/item=11645) |
| Neck | [Beads of Ogre Might](https://www.wowhead.com/forever/item=22150) | [Choker of the Fire Lord](https://www.wowhead.com/forever/item=18814) · *Ragnaros, Molten Core* |
| Shoulders | [Truestrike Shoulders](https://www.wowhead.com/forever/item=12927) · *Pyroguard Emberseer, Blackrock Spire* | [Rugged Mantle of the Timbermaw](https://www.wowhead.com/forever/item=227808) |
| Back | [Arcanoweave Cloak](https://www.wowhead.com/forever/item=272411)<br>+ [Enchant Cloak - Lesser Agility](https://www.wowhead.com/forever/spell=13364) | [Arcanoweave Cloak](https://www.wowhead.com/forever/item=272411)<br>+ [Enchant Cloak - Lesser Agility](https://www.wowhead.com/forever/spell=13364) |
| Chest | [Timbermaw Tunic](https://www.wowhead.com/forever/item=252484) · *Leatherworking*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) | [Timbermaw Tunic](https://www.wowhead.com/forever/item=252484) · *Leatherworking*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) |
| Wrist | [Rockfury Bracers](https://www.wowhead.com/forever/item=21186)<br>+ [Enchant Bracer - Superior Strength](https://www.wowhead.com/forever/spell=19984) | [Rockfury Bracers](https://www.wowhead.com/forever/item=21186)<br>+ [Enchant Bracer - Superior Strength](https://www.wowhead.com/forever/spell=19984) |
| Hands | [Blood Guard's Mail Vices](https://www.wowhead.com/forever/item=227159)<br>+ [Enchant Gloves - Strength](https://www.wowhead.com/forever/spell=13828) | [Blood Guard's Mail Vices](https://www.wowhead.com/forever/item=227159)<br>+ [Enchant Gloves - Strength](https://www.wowhead.com/forever/spell=13828) |
| Waist | [Knowledge of the Timbermaw](https://www.wowhead.com/forever/item=228190) | [Knowledge of the Timbermaw](https://www.wowhead.com/forever/item=228190) |
| Legs | [Pristine Scorpid Leggings](https://www.wowhead.com/forever/item=252606) · *Leatherworking*<br>+ [Lesser Arcanum of Voracity](https://www.wowhead.com/forever/item=11645) | [Ironfeather Leggings](https://www.wowhead.com/forever/item=252486) · *Leatherworking*<br>+ [Lesser Arcanum of Voracity](https://www.wowhead.com/forever/item=11645) |
| Feet | [Bloodmail Boots](https://www.wowhead.com/forever/item=14616) · *Scholomance*<br>+ [Enchant Boots - Minor Speed](https://www.wowhead.com/forever/spell=13889) | [Bloodmail Boots](https://www.wowhead.com/forever/item=14616) · *Scholomance*<br>+ [Enchant Boots - Minor Speed](https://www.wowhead.com/forever/spell=13889) |
| Finger | [Signet Ring of the Bronze Dragonflight](https://www.wowhead.com/forever/item=234020) | [Band of Accuria](https://www.wowhead.com/forever/item=17063) · *Ragnaros, Molten Core* |
| Finger | [Signet Ring of the Bronze Dragonflight](https://www.wowhead.com/forever/item=234021) | [Signet Ring of the Bronze Dragonflight](https://www.wowhead.com/forever/item=234020) |
| Trinket | [Briarwood Reed](https://www.wowhead.com/forever/item=12930) · *Jed Runewatcher, Blackrock Spire* | [Hand of Justice](https://www.wowhead.com/forever/item=11815) · *Emperor Dagran Thaurissan, Blackrock Depths* |
| Trinket | [Blackhand's Breadth](https://www.wowhead.com/forever/item=13965) | [Blackhand's Breadth](https://www.wowhead.com/forever/item=13965) |
| Main hand | [Fist of Cenarius](https://www.wowhead.com/forever/item=21188)<br>+ [Enchant 2H Weapon - Lesser Strength](https://www.wowhead.com/forever/spell=23793) | [Spinal Reaper](https://www.wowhead.com/forever/item=17104) · *Ragnaros, Molten Core*<br>+ [Enchant 2H Weapon - Lesser Strength](https://www.wowhead.com/forever/spell=23793) |

**Open in the simulator** (the community's Forever simulator on the web, loaded with the gear, enchants, talents, rotation, consumables and buffs we simulate): Pre-BiS: [full raid](https://elliotwood.github.io/Forever/forever/shaman/enhancement/#eJzMVE1oE1sUnnMnydyc15902sebDn04TUFqYMKdSSNNN0m7ElcNuOjOjs3URG0SMkHqRqrWKsVaXNmqoGCLCq0oKFRBF0VCKlEi+AOiLmqFLkSKiwpulEnSVru2xW917sd37/nuOYeDVRQ8IIECrcBAbFw/EQbtEIFu6IE0DAHIzwXq8ghyBgX66H6ttPgPOujILCBPf8RQoJeLHumFCwX65F6t9LEGBTo/DdJ7O3jzpVq6KqCDflitRoE+Lt920YmMNG7TU1M16KDTUzXI05Mm8nRswH5nGqRTDcgh5w3Q4YQnn5DOJZQbV6D16+HupbvQM3p8FMhwYgKuG9dgxrgJbzvn4JOWByjC+UQXbnzsIVGCjAUCAY3pKgu2sQBjusZYUGO6TQSYlidQJPwieerEf5HKLnTQCznwulFAp9rmD1pYX6HHc+AV0Im8GrCwAQXZiTzNRStSzR+0xB3y/1jvq6MO0TnKEwr2PSTMWnt2s4D8JhjPgeiQSQcnolxO+fIMiBdB7DfSR/an0llFZ/pulYVUvb1D6YsbyYNmTEllFCMWM2PKgWNKNm4qmVTWyCZSScUyjUxfXGm1TFMxk3Ej2WcOmMmsGktb6ppILYv8h6xUcpesYovYjFVeRKrb6WeWAOt8tdQlkr2cXPq7VvE6swTi2GZnGlNZaEuctaDsk6hLdM+DbezBN0kulb3Nr2vtpUYsHxVHtq9STb92kV/vom0kFxXdcnk4bkfFzLZZKk/M5Kok8cskDytEP8FzJTREvgPKFAkFDy+B9xbvtmluqD/SeGnSxkK4ub+E12F9hUgOJezLE+6vQjayFm0pds7+8TyhZ4VCoar3TqSzQkR64SzAJCRSK6cX9r0Kh0osVwx32spC4XM4Wg7ehX08nfuvq2ljo5WX857Seo5DGgZhUPw5AIABLl0=); Phase 1 BiS: [full raid](https://elliotwood.github.io/Forever/forever/shaman/enhancement/#eJzMVF1oE1kUnnMnydyc7U867bLToctOU1i6gQl3Js3S9CVpn5Z9amAf+rCwnW2mm6w2CZkg9UUqtirFWvTFVgUFK1WoolChCr4UCalEjOAPiIrUCn0QKQoVfBCZSdpqn23xezr347v3fPecw8EaCj6QQIF2YCA2b54Ig06IQS/0QRZGAOT7AvX4BNlCgd6+US8t/4Au+ukkoIu+fF+LAj1T9kkPPCjQO/P10qs6FOjiRZCe28GTt7XSOQFd9MW6rSzMO9c9dConTdr07Jj9zMxMHfJ09m/k6cQQCrQ8BtKhJuSQ84foaMpXTEnHUsrsWWh/t6d35Tr0jR8YBzKamoILxnmYMy7B0+4FeK0VAcpwPNWDWz+7RZQwY6FQSGO6ysJhFmJM1xgLa0y3CZ1pRQJlwi+Tu278EansQRc9UQC/FwV0qx3BsIWNVXqyAH4B3cirIQubUJDdyNNCvCrVgmFL/EX+GRsDDdQlusd5QsG+h4RZG89uF5CvBJMFEF0y6eJElCspHx4B8RSIg0Z27z+ZbF7Rmf67yiKq3tmlDCSN9H9mQsnkFCORMBPKv/uVfNJUcpm8kU9l0oplGrmBpNJumaZippNGesAcMtN5NZG11A2RWhEF/7cy6d9kFdvEVqzxI1LdTj+3AtgQqKcekfzJyc7ftarXuRUQJ7Y705jKIjvirA3lgEQ9oncRbGM3P0iyU/aOoK51Oo1Y3Sce3r1KtXzZRX6zi7aRQlz0ypXhuBoXc7tmqTIx0+uSxK+SIqwR/SDPOWiKfQSUKRIKPl4C/2Xea9PcyGCs+fS0jaVo66CDx1F9jUguJRooEu67Qj62Ee0ofr3yzfNE7pVKpZr+a7HuKhHrh6MA05DKrI0t/fUoGnFYrhzttpWl0ptovBI8iwZ4uvBTT8vWRqts5z+c/ZyELAzDsPh5AMYHLx8=).

## Other builds of this spec

- [Elemental — Lava Burst / Lightning Overload](../research/raid/builds/elemental-raid-dps.md) (29/22/0, 515 DPS in a full raid) — [open the talent tree](https://talentsforever.com/shaman/60/550230130210304-255000001340002--6)

---
*Generated by `_reference/data/render_modes.py` on 2026-10-15 from this project's builds and simulations of the WoW: Forever beta (client build 1.60.1.70291). Simulations, not in-game measurements. Do not hand-edit.*

