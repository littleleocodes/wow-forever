# Protection Paladin — Raid (group)

[Paladin](../README.md) > [Raid (group)](README.md) > Protection

**[Protection — Raid tank](../research/raid/builds/protection-ml-tank.md)** (0/32/19) — [open the talent tree](https://talentsforever.com/paladin/60/-0530513301301151-50222230021-6)

> 🔬 Derived build: found by this project's deep search over every legal build of the spec in the community's raid simulator, on tank value (threat and damage taken), then raced against the spec's builds; it beat the hand-made build (prot-tank), which stays below as the alternative. A model of the beta, to check at launch.

## How to play

**Before the pull:** **Righteous Fury**, **Seal of Righteousness**, **Holy Shield**.

**Keep up all fight:** **Seal of Righteousness**, **Righteous Fury**.

**Then press the first one that is ready**, top to bottom:

1. **Templar's Bulwark**
2. **Holy Shield**
3. **Judgement**
4. **Consecration**
5. **Holy Strike**
6. **Lay on Hands**

Between these, your white swings do the rest.

**Advanced: your cooldowns and extras.** Once the list above feels easy, add these:

- **Swift Judgement**: whenever it is ready: it finishes the cooldown on **Judgement** and makes the next one free, so judge again at once
- Use your trinkets and a potion together with your big cooldowns.

*The simulator's full rotation for this build, with every condition: [research rotation page](../research/raid/rotation.md).*

## Why this rotation

Most of your threat is Holy damage, and **Righteous Fury** makes it 60% more threat. Keep **Holy Shield** up, judge **Seal of Righteousness** on cooldown and press **Consecration** and **Holy Strike** whenever they are ready; **Templar's Bulwark** and **Lay on Hands** are your emergency buttons.

**Why it works**

- Before the pull: **Righteous Fury** (it lasts 30 minutes, and **Improved Righteous Fury** and **Iron Creed** only work while it is up), then **Seal of Righteousness** and **Holy Shield** in the last seconds, so the first hits already meet both.
- **Holy Shield** lasts 10 seconds and comes back every 10, so keep it up all fight: 30% more block for 4 blocks, and every block deals Holy damage with 20% extra threat and can trigger **Redoubt** and **Shield Specialization**'s mana. The simulator measured 1.3% more tank value with it at the top of the list.
- Press **Judgement** on cooldown, whether or not the short list shows it: it is off the global cooldown, judges **Seal of Righteousness** for about a tenth of your threat, and no longer uses up the seal in Forever. Judging every time it is ready, instead of only before the seal runs out, measured 4.3% more tank value; **Swift Judgement** goes right after a **Judgement**, because it finishes the cooldown and makes the next one free.
- **Consecration** and **Holy Strike** fill the rest: **Consecration** threatens everything standing in it, and **Holy Strike** with **Iron Creed** makes 25% more threat and cuts your damage taken by 10% for 6 seconds. Refresh **Seal of Righteousness** when it has about a second left.
- **Templar's Bulwark** sits at the top because the simulator's 3-minute fight fits one use: it absorbs damage equal to your maximum health for 8 seconds, off the global cooldown, and using it at the pull measured 1.4% more tank value. It applies Forbearance for a minute, which locks you out of **Divine Protection**, **Divine Shield** and **Blessing of Protection**.
- **Lay on Hands** below 10% health measured 8% more tank value, but nobody heals you in the simulator's fights. In a raid it is the last resort: it heals you for your maximum health and drains all your mana.

**Caveats**

- The simulator tanks with **Seal of Righteousness**. **Seal of Fury** (35 Holy damage a swing, plus an absorb of half of it while you hold a shield) is not part of its tuned rotation, so whether it is better for you was not measured.
- Mana: you run dry for a few seconds of each 3-minute fight in the simulator. **Consecration** is the expensive button (565 mana before **Holy Conduit**); blocks give mana back through **Shield Specialization** and judgements through **Sanctified Judgement**.
- The simulator measures one boss. **Consecration** and **Holy Shield** work on everything that hits you; **Holy Strike** and **Judgement** only on your target.

**When to change it**

- To taunt (a tank swap, a loose add), put up **Seal of Fury** and judge: its judgement taunts for 4 seconds. Use **Swift Judgement** if **Judgement** is on cooldown, then go back to **Seal of Righteousness**.
- Hold **Templar's Bulwark** for a known damage spike or a healer death when the fight has one: the simulator spends it at the pull only because its fight fits a single use.
- Undead or Demon packs: **Holy Wrath** (a 2-second cast) hits and stuns every Undead and Demon within 20 yards, and **Exorcism** hits one hard. Neither was measured: the simulator's boss is an Elemental.

*This guide was written for the rotation of 2026-10-09; the list above was re-tuned since, so follow the list where the two differ.*

## The numbers

Tank value 1.042 (threat and damage taken under a boss, relative to our reference tank build).

## Other builds of this spec

- [Protection (optimized)](../research/raid/builds/opt-prot-tank-raid-tank.md) (0/32/19) — [open the talent tree](https://talentsforever.com/paladin/60/-0530513301311051-50025330001-6)
- [Protection — Tank](../research/raid/builds/prot-tank.md) (0/23/28) — [open the talent tree](https://talentsforever.com/paladin/60/-0530513101301-502253300110303-6)

---
*Generated by `_reference/data/render_modes.py` on 2026-10-15 from this project's builds and simulations of the WoW: Forever beta (client build 1.60.1.70291). Simulations, not in-game measurements. Do not hand-edit.*

