# Protection Paladin — Raid (group)

[Paladin](../README.md) > [Raid (group)](README.md) > Protection

**[Protection — Raid tank](../research/raid/builds/protection-ml-tank.md)** (0/35/16) — [open the talent tree](https://talentsforever.com/paladin/60/-05311102513301531-52233000001-12)

> 🔬 Derived build: found by this project's deep search over every legal build of the spec in the community's raid simulator, on tank value (threat and damage taken), then raced against the spec's builds. A model of the beta, to check at launch.

## How to play

**Before the pull:** **Righteous Fury**, **Retribution Aura**, **Seal of the Crusader**.

**Keep up all fight:** **Righteous Fury**, **Retribution Aura**.

**Then press the first one that is ready**, top to bottom:

1. **Judgement**; no global cooldown, so press it alongside the others
2. **Consecration**
3. **Holy Shield**
4. **Holy Strike**
5. **Hammer of Wrath** when the target is below 20% health

Between these, your white swings do the rest.

**Advanced: your cooldowns and extras.** Once the list above feels easy, add these:

- **Seal of Fury**: part of the rotation (about 6 times a fight)
- **Lay on Hands**: when you are about to die: a full heal on a long cooldown that empties your mana
- **Templar's Bulwark**: a cooldown, use it at the start of the fight and again whenever it is ready (about 1 time a fight)
- Use your trinkets and a potion together with your big cooldowns.

*The simulator's full rotation for this build, with every condition: [research rotation page](../research/raid/rotation.md).*

## Why this rotation

Most of your threat is Holy damage, and **Righteous Fury** makes it 90% more threat. Keep **Holy Shield** up, judge **Seal of Righteousness** on cooldown and press **Consecration** and **Holy Strike** whenever they are ready; **Templar's Bulwark** and **Lay on Hands** are your big defensive buttons.

**Why it works**

- Before the pull: **Righteous Fury** (it lasts 30 minutes, and **Improved Righteous Fury** and **Iron Creed** only work while it is up), then **Seal of Righteousness** and **Holy Shield** in the last seconds, so the first hits already meet both.
- **Holy Shield** lasts 10 seconds and comes back every 10, so keep it up all fight: 30% more block for 4 blocks, and every block deals Holy damage with 20% extra threat and can trigger **Redoubt** and **Shield Specialization**'s mana. The simulator measured 1.3% more tank value with it at the top of the list.
- Press **Judgement** on cooldown, whether or not the short list shows it: it is off the global cooldown, judges **Seal of Righteousness** for about a tenth of your threat, and no longer uses up the seal in Forever. Judging every time it is ready, instead of only before the seal runs out, measured 4.3% more tank value; **Swift Judgement** is a second, free **Judgement** on its own 1-minute cooldown: use it whenever it is ready.
- **Consecration** and **Holy Strike** fill the rest: **Consecration** threatens everything standing in it, and **Holy Strike** with **Iron Creed** makes up to 30% more threat and cuts your damage taken by up to 6% for 6 seconds (rank 3). Refresh **Seal of Righteousness** when it has about a second left.
- **Templar's Bulwark** sits at the top because the simulator's 3-minute fight fits one use: it absorbs damage equal to your maximum health for 8 seconds, off the global cooldown, and using it at the pull measured 1.4% more tank value. It applies Forbearance for a minute, which locks you out of **Divine Protection**, **Divine Shield** and **Blessing of Protection**.
- **Lay on Hands** is last in the list with no health condition: in the simulator's fights nobody heals you, and casting it whenever nothing else is ready measured 0.4% more tank value than keeping it for 10% health (8% more than not using it). It heals you for your maximum health but drains all your mana, and its cooldown is 20 minutes: in a raid with healers, keep it for when you are about to die.

**Caveats**

- The simulator tanks with **Seal of Righteousness**. **Seal of Fury** (35 Holy damage a swing, plus an absorb of half of it while you hold a shield) is not part of its tuned rotation, so whether it is better for you was not measured.
- Mana: you run dry for a few seconds of each 3-minute fight in the simulator. **Consecration** is the expensive button (565 mana); blocks give mana back through **Shield Specialization** and judgements through **Sanctified Judgement**.
- The simulator measures one boss. **Consecration** and **Holy Shield** work on everything that hits you; **Holy Strike** and **Judgement** only on your target.

**When to change it**

- To taunt (a tank swap, a loose add), put up **Seal of Fury** and judge: its judgement taunts for 4 seconds. Use **Swift Judgement** if **Judgement** is on cooldown, then go back to **Seal of Righteousness**.
- Hold **Templar's Bulwark** for a known damage spike or a healer death when the fight has one: the simulator spends it at the pull only because its fight fits a single use.
- Undead or Demon packs: **Holy Wrath** (a 2-second cast) hits and stuns every Undead and Demon within 20 yards, and **Exorcism** hits one hard. Neither was measured: the simulator's boss is an Elemental.

## Talents

| Tree | Points | Talents (ranks) |
|---|---|---|
| Protection | 35 | Redoubt 5, Precision 3, Guardian's Favor 1, Sacred Duty 1, Templar's Bulwark 1, Shield Specialization 2, Toughness 5, Swift Judgement 1, Improved Righteous Fury 3, Anticipation 3, Holy Shield 1, Reckoning 5, Iron Creed 3, Shieldsworn 1 |
| Retribution | 16 | Deflection 5, Benediction 2, Improved Judgement 2, Conviction 3, Sanctified Judgement 3, Sacred Arbiter 1 |

## The numbers

Tank value 1.022 (threat and damage taken under a boss, relative to our reference tank build).

**The gear** (average item level: Pre-BiS 62.5; Phase 1 BiS 63.9; chosen in the community simulator on tank value, threat and damage taken, for this build in a full raid. The simulator's item database lists base armor for only about one armor item in five; this project's patch fills in the rest from Classic's values (our assumption: Forever may have changed some); each item opens its Wowhead page, with where it drops and its enchant):

| Slot | Pre-BiS | Phase 1 BiS |
|---|---|---|
| Head | [Stalwart Helm](https://www.wowhead.com/forever/item=250599) · *Blacksmithing*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11647) | [Stalwart Helm](https://www.wowhead.com/forever/item=250599) · *Blacksmithing*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11647) |
| Neck | [Amulet of the Darkmoon](https://www.wowhead.com/forever/item=19491) · *quest: 1200 Tickets - Amulet of the Darkmoon* | [Choker of the Fire Lord](https://www.wowhead.com/forever/item=18814) · *Ragnaros, Molten Core* |
| Shoulders | [Highlander's Lamellar Spaulders](https://www.wowhead.com/forever/item=20058) · *sold by Samuel Hawke* | [Highlander's Lamellar Spaulders](https://www.wowhead.com/forever/item=20058) · *sold by Samuel Hawke* |
| Back | [Shifting Cloak](https://www.wowhead.com/forever/item=18511) · *Leatherworking*<br>+ [Enchant Cloak - Superior Defense](https://www.wowhead.com/forever/spell=20015) | [Shifting Cloak](https://www.wowhead.com/forever/item=18511) · *Leatherworking*<br>+ [Enchant Cloak - Superior Defense](https://www.wowhead.com/forever/spell=20015) |
| Chest | [Breastplate of Heroism](https://www.wowhead.com/forever/item=21997) · *quest: Saving the Best for Last*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) | [Breastplate of Heroism](https://www.wowhead.com/forever/item=21997) · *quest: Saving the Best for Last*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) |
| Wrist | [Deeprock Bracers](https://www.wowhead.com/forever/item=21184) · *quest: Stalwart's Battlegear*<br>+ [Enchant Bracer - Deflection](https://www.wowhead.com/forever/spell=13922) | [Deeprock Bracers](https://www.wowhead.com/forever/item=21184) · *quest: Stalwart's Battlegear*<br>+ [Enchant Bracer - Deflection](https://www.wowhead.com/forever/spell=13922) |
| Hands | [Theramore Gauntlets](https://www.wowhead.com/forever/item=271940)<br>+ [Enchant Gloves - Agility](https://www.wowhead.com/forever/item=273520) | [Theramore Gauntlets](https://www.wowhead.com/forever/item=271940)<br>+ [Enchant Gloves - Agility](https://www.wowhead.com/forever/item=273520) |
| Waist | [Belt of Heroism](https://www.wowhead.com/forever/item=21994) · *quest: Just Compensation* | [Belt of Heroism](https://www.wowhead.com/forever/item=21994) · *quest: Just Compensation* |
| Legs | [Champion's Legplates](https://www.wowhead.com/forever/item=250598) · *Blacksmithing*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11647) | [Champion's Legplates](https://www.wowhead.com/forever/item=250598) · *Blacksmithing*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11647) |
| Feet | [Warder's Sabatons](https://www.wowhead.com/forever/item=250563) · *Blacksmithing*<br>+ [Enchant Boots - Greater Agility](https://www.wowhead.com/forever/item=16245) | [Warder's Sabatons](https://www.wowhead.com/forever/item=250563) · *Blacksmithing*<br>+ [Enchant Boots - Greater Agility](https://www.wowhead.com/forever/item=16245) |
| Finger | [Warden's Signet of Vigilance](https://www.wowhead.com/forever/item=275984) | [Ring of Spell Power](https://www.wowhead.com/forever/item=19147) · *Lucifron, Molten Core* |
| Finger | [Ring of Awareness](https://www.wowhead.com/forever/item=272409) · *sold by Pix Xizzix* | [Warden's Signet of Vigilance](https://www.wowhead.com/forever/item=275984) |
| Trinket | [Defender's Grip Stabilizer](https://www.wowhead.com/forever/item=272440) · *sold by Pix Xizzix* | [Defender's Grip Stabilizer](https://www.wowhead.com/forever/item=272440) · *sold by Pix Xizzix* |
| Trinket | [Frozen Heart of the Mountain](https://www.wowhead.com/forever/item=249469) · *Enchanting* | [Talisman of Ephemeral Power](https://www.wowhead.com/forever/item=18820) · *Magmadar, Molten Core* |
| Main hand | [Sageblade](https://www.wowhead.com/forever/item=22383) · *Blacksmithing*<br>+ [Enchant Weapon - Spell Power](https://www.wowhead.com/forever/spell=22747) | [Sageblade](https://www.wowhead.com/forever/item=22383) · *Blacksmithing*<br>+ [Enchant Weapon - Spell Power](https://www.wowhead.com/forever/spell=22747) |
| Off hand | [Evergreen Shield](https://www.wowhead.com/forever/item=279262) · *Blacksmithing*<br>+ [Enchant Shield - Greater Stamina](https://www.wowhead.com/forever/item=16217) | [Evergreen Shield](https://www.wowhead.com/forever/item=279262) · *Blacksmithing*<br>+ [Enchant Shield - Greater Stamina](https://www.wowhead.com/forever/item=16217) |
| Ranged/relic | [Libram of Fervor](https://www.wowhead.com/forever/item=23203) | [Libram of Fervor](https://www.wowhead.com/forever/item=23203) |

**Open in the simulator** (the community's Forever simulator on the web, loaded with the gear, enchants, talents, rotation, consumables and buffs we simulate): Pre-BiS: [full raid](https://wowsims.com/forever/paladin/protection/#eJzEVV1oHFUU3nPn7syZM02z3rZmelGZDlK3C7PMzHY1zUumfRIEWXzyzYzN1l1Tskt2kfrWCAUfREqeTCyJdBsoqboQFGIwEPypaRX0ofiwYG1rURHFn3dF7ky3q8EHH2z8Hg7nfuee3W++c+DSAwg5sMGBPExADZpwGuBlgDcALgKIXUmVqeooyE0TeY7JWSADv1setm9bxLHzGhDH3jlFfn4W7Ju7ycCfLoH9jUo2l8F+3SADP/osZ3+9mzj+cEnd/DZtN/DD5eGUP/tjjjjOf6HiWhJ/PzdMBv78Nthbe8jA62fus6+rm513wT2Qu1zP316CBTA78Ztx7+jSMqyA9Ur91wdXLsKr9TP1Y5hohwjW2UOeXy4FQeCH5aBU8oNyKfDKYVgq+QrBFuO32KcG7SWUOnF85wq4SDpxL/RbNEKmNCibz+JGxSVC0r1gtFhWBZJIel7Ha4vgmmRQ1guK5ZbogZiImyefaTTbTuiHj3qB75WCMed4LZ5+rjrpNGaceHKyOuk8+6LTrlWdmUY7btcb006rGs8crzn5VrXqNGcaba8dT095/bKXlovPtxrTh+QLNCXq5Isi7SvsQV1kfzMYakoQcb8YtPr0B+zv9JBrkXke1Hd2F4EOFh5GLsyVPiH3rTKBTJjnjT6jrfNM4gDiVxXBJRvLCJKpVd1FEKH0//XPqMPcSxXxmCzTIfEI2YX7URPWOigjDfxkCWSqmKyePuDuZuIIwj+1In68uL015e5mYpdM55XF9zsgTm6fUeD5h//jGaUezV17QviySK50aNgdIusWKhmA781WaGgViDjenHtSsFw20cexe3WgVsPNDghLmoMRTO3AehkySxperogLO7HMER2WIe0vjCAIa4EpFzTsboDyj5ifLrO2bcfD1h2DuhsDg3S8WrG179kW/MLCWS2TYG+0CpwYZdw/mKmIzOkT0f6FeYUr4wdOJPhyPLzBbO6MF9ZY5n9BO+pn9xQH37pn/3MkiU9diI7eIaIJ9ZrMQ3LI3BgvaLg2MsZycOwvD48PoxDB41CBp6EGTTgFp9ifAwCj7kE5); Phase 1 BiS: [full raid](https://wowsims.com/forever/paladin/protection/#eJzEVd9rHFUU3nPn7syZM02z3rZmelGZDlK3C7PMzHY1zUumfRIEWXzyzYzN1l1Tskt2kfrWiAUfRErEh0ZJpOlCSdWFoBCDgeCPmraCPhQfFqxtLSqi+OMPKHJnul0NPvhg4/dwOfc799z55jsHLj2AkAMbHMjDBNSgCScBXgF4G+A8gNiRZJnKjoLcMJHnmJwFMvCHzrB9yyKOt+eAOPbeUuSXp8G+sZMM/OUC2N+pYKMD9psGGfjpFzn7253E8acL6uT3abmBn3SGU/7KG+qe0z/niOPqV2p9+XV18tf3wN7cRQZeO3WffU2dXPoA3H25i/X8rUWYB3MpfifuHV7swDJYr9Z/f3D5PLxWP1U/gol2iGCNPeT55VIQBH5YDkolPyiXAq8chqWSrxBsMn6TXTFoN6HUieP7l8BF0ol7od+iETKlQdl8FtcrLhGS7gWjxbJKkETS8zpeXQDXJIOyXlAst0QPxETcPP5Mo9l2Qj981At8rxSMOUdr8fRz1UmnMePEk5PVSefZF512rerMNNpxu96YdlrVeOZozcm3qlWnOdNoe+14esrrp700XXy+1Zg+IF+gKVEnXxRpT2EX6iL7h8FQU4KI+8Wg1ac/Zn+nh1yLzLOg/rO7ALS/8DByYS73CblnhQlkwjxr9BltjWcSBxC/qQgu2VhGkEyt6i6ACKX/r69Rm7mXKuIxWaYD4hGyC/ejJqw1UEYa+PkiyFQxWT19wN2NxCGEfypF/Gxha2nK3Y3EDpn2K4sfLYE4vrVHgecf/I97lHo0d/UJ4csiudKhYXeIrJuoZAB+OFuhoRUg4nhj7knBctlEH8fu5YFaDTeWQFjSHLRgahvGy5BZ0vBiRZzbjmGO6KAMaW9hBEFY80y5oGF3HZR/xPx0mLUtMx627hjUXR8YpOPliq39yDbhNxbOapkEu6MV4MQo495mpiIyJ49Fe+fPKFwa33cswdfj4XVmc2e8sMoy/wvaUT+6p9j/7j37zqFkfepcdPgOEU2o1+QMJJvM9fGChqsjYywHR/7y8PgwChE8DhV4GmrQhBNwgv05AM8NQOY=).

## Other builds of this spec

- [Protection — Tank](../research/raid/builds/prot-tank.md) (0/33/18) — [open the talent tree](https://talentsforever.com/paladin/60/-15310112513501031-50233300011-12)
- [Protection (optimized)](../research/raid/builds/opt-prot-tank-raid-tank.md) (1/34/16) — [open the talent tree](https://talentsforever.com/paladin/60/01-25300132503501031-50033310001-12)

---
*Generated by `_reference/data/render_modes.py` on 2026-11-10 from this project's builds and simulations of the WoW: Forever beta (talent and spell data: client build 1.60.1.70753; raid numbers: the official wowsims/forever simulator at 16e8542 (client 1.60.1.70790)). Simulations, not in-game measurements. Do not hand-edit.*

