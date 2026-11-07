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
- **Frees:** nothing: this fills a free key, C on your bars.
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
- **Fill it with:** R takes Execute from 2, the payoff key. Mouse 4 takes Overpower from Mouse 5, and Mouse 5 stays free for Victory Rush from 1.
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
- **Fill it with:** C takes Hamstring from 3, so a runner is one finger away.
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

Leveling and raid.

### Bloodthirst that starts your swings

```
#showtooltip Bloodthirst
/startattack [harm,nodead]
/cast Bloodthirst
```

- **Replaces:** Bloodthirst on Q from 40 (the opening key holds a start-attack macro, so no key needs Attack).
- **Frees:** nothing.
- **Fill it with:** nothing needed.
- **Why it works:** The same idea as the Arms and Holy Strike macros.

### Whirlwind from any stance

```
#showtooltip Whirlwind
/cast [nostance:3] Berserker Stance
/cast Whirlwind
```

- **Replaces:** Berserker Stance on a side key, and R.
- **Frees:** One stance key.
- **Fill it with:** Battle Stance's Overpower, the same way: `/cast [nostance:1] Battle Stance`, then `/cast Overpower`.
- **Why it works:** Stances are off the global cooldown. Stance 3 is Berserker in Classic's order: if the wrong stance fires, swap the number.

### Cooldowns before the Charge

```
#showtooltip Death Wish
/cast Bloodrage
/cast Death Wish
```

- **Replaces:** Bloodrage and Death Wish.
- **Frees:** One key.
- **Fill it with:** Intercept, for mobs that run.
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
- **Fill it with:** Revenge, the reaction it should have been sharing a thumb with.
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
- **Why it works:** Tactical Mastery keeps some rage through the swap. With Vanguard you can skip the stance line.

### Last Stand with a heal

```
#showtooltip Last Stand
/cast Last Stand
/use Major Healthstone
/use Major Healing Potion
```

- **Replaces:** Last Stand and the potion key.
- **Frees:** One key.
- **Fill it with:** Shield Wall.
- **Why it works:** Last Stand is off the global cooldown. Use your own potion's name, or the potion macro's whole list.
