# Warrior macros (hand-written)

[Warrior](README.md) > Macros

Macro ideas for every warrior spec, for leveling and raid: what each one does, which keys it replaces and what could go on the keys it frees. **These are theory: none has been tested in Forever's client yet.** The commands are real, though: `/cast`, `/use`, `/castsequence`, `/startattack`, `/stopattack`, `/stopcasting`, `/cancelaura`, `/cancelform` and `/petattack` are all in Forever's own UI code. If a macro misbehaves, go back to the plain spell.

**The rule behind them:** one press only fires two spells if the first is off the global cooldown. In the simulator's data, these warrior spells are: Bloodrage, Charge, Cleave, Concussion Blow, Heroic Strike, Intercept, Last Stand, Shield Block, Sweeping Strikes, Taunt and the stances. A macro can name more than one spell on the global cooldown, but only the first that can go will fire.

To make one: Esc, Macros, New, pick the question-mark icon so the button shows the spell, and drag it onto the key. Your layout is on the [keybinds page](leveling/keybinds.md).

## Every spec

### Best healing potion in your bags

```
#showtooltip
/use Major Healing Potion
/use Superior Healing Potion
/use Greater Healing Potion
/use Healing Potion
/use Lesser Healing Potion
/use Minor Healing Potion
```

- **Replaces:** clicking a potion in your bags.
- **Frees:** nothing: this fills a free key. Put it on Shift+C, which none of the three level-by-level guides uses (C holds Heroic Strike from level 40).
- **Why it works:** only the first potion you own goes off, because they share a cooldown.

### Quiet the not-ready errors

```
/run UIErrorsFrame:SetMessageTypeEnabled(LE_GAME_ERR_SPELL_COOLDOWN,false)
/run UIErrorsFrame:SetMessageTypeEnabled(LE_GAME_ERR_ABILITY_COOLDOWN,false)
/run for i=569772,569776 do MuteSoundFile(i) end
```

- **Replaces:** nothing. Click it once after each login from a side bar.
- **Why it works:** the first two lines turn off the text, speech and sound of the "not ready" errors only, the way Forever's own error frame does, and useful errors like "Out of range" stay. The last line mutes the spell fizzle sound until you restart the game. These macros press spells on cooldown a lot, so this keeps them quiet.

## Arms

Leveling and raid. Keys below are your [Arms keybinds](leveling/keybinds.md).

### Charge, then Rend, on one key

```
#showtooltip Charge
/cast Bloodrage
/cast Charge
/cast Rend
```

- **Replaces:** E (Charge), Mouse 4 (Bloodrage) and R (Rend).
- **Frees:** R and Mouse 4.
- **Fill it with:** this macro moves keys away from the layout on the [keybinds page](leveling/keybinds.md) and in the by-level tables, so use it only if you accept that. Execute moves from 2 to R, Overpower from Mouse 5 to Mouse 4 and Victory Rush from 1 to Mouse 5; keys 1 and 2 are then free.
- **Why it works:** Bloodrage and Charge are off the global cooldown, so the first press does both. Rend is out of range on that press, so press E once more when you land. Bloodrage costs health: the lab skips it below 45% of your health, so press plain Charge from a side key if you pull while hurt.

### Mortal Strike with a spare-rage Heroic Strike

```
#showtooltip Mortal Strike
/startattack [harm,nodead]
/cast Mortal Strike
/cast [mod:ctrl] Heroic Strike
```

- **Replaces:** Q and C from level 40.
- **Frees:** C.
- **Fill it with:** nothing needed: Hamstring is already on 3, so a runner is one finger away, and C stays free.
- **Why it works:** Heroic Strike is off the global cooldown. Hold Ctrl only when you have rage to spare: without it the macro is plain Mortal Strike, so it never starves the next one.

### Sweeping Strikes into Cleave

```
#showtooltip Cleave
/cast Sweeping Strikes
/cast Cleave
```

- **Replaces:** Shift+R and Shift+Mouse 5.
- **Frees:** Shift+R.
- **Fill it with:** Shift+R stays free, or takes Thunder Clap so both pack keys sit together.
- **Why it works:** Both are off the global cooldown. For pulls of two or more.

## Fury

Leveling and raid. The Fury leveling page fights in Battle Stance and the Fury raid page never leaves Berserker Stance, so neither rotation needs a stance macro.

### Bloodthirst that starts your swings

```
#showtooltip Bloodthirst
/startattack [harm,nodead]
/cast Bloodthirst
```

- **Replaces:** Bloodthirst on Q from 40 (the opening key holds a start-attack macro, so no key needs Attack).
- **Frees:** nothing.
- **Fill it with:** nothing needed.
- **Why it works:** The same idea as the Arms macro.

### Whirlwind from any stance (not in either rotation)

```
#showtooltip Whirlwind
/cast [nostance:3] Berserker Stance
/cast Whirlwind
```

- **Replaces:** Berserker Stance on a side key, and a key for Whirlwind.
- **Frees:** One stance key.
- **Fill it with:** nothing needed. The fight lab's Fury rotation stays in Battle Stance and never casts Whirlwind, and the raid rotation stays in Berserker Stance; this is for pressing one Whirlwind on a pack from Battle Stance (it leaves you in Berserker Stance, so swap back, and Overpower is lost until you do).
- **Why it works:** Stances are off the global cooldown. Stance 3 is Berserker in Classic's order: if the wrong stance fires, swap the number.

### Cooldowns before the Charge

```
#showtooltip Death Wish
/cast Bloodrage
/cast Death Wish
```

- **Replaces:** Bloodrage and Death Wish.
- **Frees:** One key.
- **Fill it with:** nothing needed; Hamstring is already on 3 for mobs that run (Intercept needs Berserker Stance, which the Fury leveling page does not use).
- **Why it works:** Bloodrage is off the global cooldown. Press this before Charge at the pull. Death Wish is on the global cooldown, so it comes last in the macro.

## Protection

Tanking and leveling.

### Shield Block on your main strike

```
#showtooltip Shield Slam
/startattack [harm,nodead]
/cast Shield Block
/cast Shield Slam
```

- **Replaces:** Q and the Shield Block key.
- **Frees:** One key.
- **Fill it with:** nothing needed: Revenge is already on Mouse 5. Mouse 4 (Defensive Stance bar) stays free, or takes Taunt from Shift+Mouse 4 if you tank groups.
- **Why it works:** Shield Block is off the global cooldown, and the rotation wants it whenever the mob is hitting you. It spends rage: drop that line when you are short.

### Charge from any stance

```
#showtooltip Charge
/cast [nostance:1] Battle Stance
/cast Charge
```

- **Replaces:** Battle Stance and Charge.
- **Frees:** One key.
- **Fill it with:** Taunt from any stance, the same way with `[nostance:2] Defensive Stance`.
- **Why it works:** Tactical Mastery keeps 10 rage through the swap (more with Improved Tactical Mastery). With Vanguard you can skip the stance line; the Protection leveling build does not take it.

### Last Stand: no macro

No Protection leveling or raid build takes Last Stand (the Protection PvP draft does), and Shield Wall (60% less damage for 12 seconds) has a 15-minute cooldown, so a potion tied to it would fire when the wall is down. Press the potion macro above on Shift+C instead.
