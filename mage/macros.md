# Mage macros (hand-written)

[Mage](README.md) > Macros

Macro ideas for every mage spec, for leveling and raid: what each one does, which keys it replaces and what could go on the keys it frees. **These are theory: none has been tested in Forever's client yet.** The commands are real, though: `/cast`, `/use`, `/castsequence`, `/startattack`, `/stopattack`, `/stopcasting`, `/cancelaura`, `/cancelform` and `/petattack` are all in Forever's own UI code. If a macro misbehaves, go back to the plain spell.

**The rule behind them:** one press only fires two spells if the first is off the global cooldown. In the simulator's data, these mage spells are: Arcane Power, Cold Snap, Combustion, Counterspell and Presence of Mind. A macro can name more than one spell on the global cooldown, but only the first that can go will fire.

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

### Best mana potion in your bags

```
#showtooltip
/use Major Mana Potion
/use Superior Mana Potion
/use Greater Mana Potion
/use Mana Potion
/use Lesser Mana Potion
/use Minor Mana Potion
```

- **Replaces:** clicking a potion in your bags.
- **Frees:** nothing: this fills a free key, Shift+C on your bars. It shares the healing potion's cooldown.

### Quiet the not-ready errors

```
/run UIErrorsFrame:SetMessageTypeEnabled(LE_GAME_ERR_SPELL_COOLDOWN,false)
/run UIErrorsFrame:SetMessageTypeEnabled(LE_GAME_ERR_ABILITY_COOLDOWN,false)
/run for i=569772,569776 do MuteSoundFile(i) end
```

- **Replaces:** nothing. Click it once after each login from a side bar.
- **Why it works:** the first two lines turn off the text, speech and sound of the "not ready" errors only, the way Forever's own error frame does, and useful errors like "Out of range" stay. The last line mutes the spell fizzle sound until you restart the game. These macros press spells on cooldown a lot, so this keeps them quiet.

## Frost

Leveling and raid. Keys below are your [Frost keybinds](leveling/keybinds.md).

### Interrupt mid-cast

```
#showtooltip Counterspell
/stopcasting
/cast Counterspell
```

- **Replaces:** Nothing: a variant for Mouse 4.
- **Frees:** Nothing.
- **Fill it with:** Nothing.
- **Why it works:** Counterspell is off the global cooldown, but a cast in progress blocks it. `/stopcasting` drops your Frostbolt so the interrupt lands on the first press.

### Nova, then Ice Lance

```
#showtooltip Frost Nova
/castsequence reset=8 Frost Nova, Ice Lance
```

- **Replaces:** E, for the freeze that matters.
- **Frees:** Nothing: keep R for Fingers of Frost.
- **Fill it with:** Nothing.
- **Why it works:** E twice: freeze, then shatter it. Ice Lance has an 8-second cooldown, so the sequence resets in time for the next one. Step back between presses if the mob is on you.

### Sheep the same mob again

```
#showtooltip Polymorph
/cast [@focus,harm,nodead][] Polymorph
```

- **Replaces:** Nothing: a variant for 2.
- **Frees:** Nothing.
- **Fill it with:** Set your sheep target with a `/focus` macro on Shift+1.
- **Why it works:** With a focus set, you re-sheep it without losing your real target. For pulls of two.

### A wand that never turns itself off

```
#showtooltip Shoot
/cast !Shoot
```

- **Replaces:** Middle mouse, which holds Shoot.
- **Frees:** Nothing.
- **Fill it with:** Nothing.
- **Why it works:** Plain Shoot is a toggle, so a second press stops the wand, like the Attack button. The `!` keeps it on. A simple swap on the key you already use.

## Arcane and Arcane-Frost

Arcane Blast and Missile Barrage builds.

### Everything at once

```
#showtooltip Arcane Power
/cast Arcane Power
/cast Presence of Mind
/cast Arcane Blast
```

- **Replaces:** Arcane Power and Presence of Mind.
- **Frees:** Two keys.
- **Fill it with:** Cold Snap and Evocation, in a build that has them.
- **Why it works:** Both cooldowns are off the global cooldown. Use it for a burst, not every pull. For Arcane-Frost, use the Presence of Mind macro on your keybinds page.

## Fire

Fireball and Heating Up.

### Combustion with your next nuke

```
#showtooltip Combustion
/cast Combustion
/cast Fireball
```

- **Replaces:** The Combustion key.
- **Frees:** One key.
- **Fill it with:** Blast Wave.
- **Why it works:** Combustion is off the global cooldown.

### Instant Pyroblast

```
#showtooltip Pyroblast
/cast Presence of Mind
/cast Pyroblast
```

- **Replaces:** Presence of Mind and one Pyroblast press, if your build has both.
- **Frees:** One key.
- **Fill it with:** Scorch.
- **Why it works:** Presence of Mind is off the global cooldown. Keep plain Pyroblast for Heating Up, since this one spends the cooldown each press.

## Frostfire

Frostfire Bolt and Ice Lance.

### Interrupt mid-cast

```
#showtooltip Counterspell
/stopcasting
/cast Counterspell
```

- **Replaces:** Nothing: a variant.
- **Frees:** Nothing.
- **Fill it with:** Nothing.
- **Why it works:** The same macro as Frost.
