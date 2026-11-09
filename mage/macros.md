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
- **Frees:** nothing: this fills a free key, Shift+C on your bars. Fire and Frostfire put it on Shift+X: their Shift+C holds Cone of Cold (Fire, from 49) or Blast Wave (Frostfire, from 55). On the other specs' bars Cone of Cold is on C from 26; Fire's C becomes Blast Wave at 49.
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
- **Frees:** nothing: this fills a free key, Shift+X on your bars, Shift+4 for Fire and Frostfire. It shares the healing potion's cooldown.

### Quiet the not-ready errors

```
/run UIErrorsFrame:SetMessageTypeEnabled(LE_GAME_ERR_SPELL_COOLDOWN,false)
/run UIErrorsFrame:SetMessageTypeEnabled(LE_GAME_ERR_ABILITY_COOLDOWN,false)
/run for i=569772,569776 do MuteSoundFile(i) end
```

- **Replaces:** nothing. Click it once after each login from a side bar.
- **Why it works:** the first two lines turn off the text, speech and sound of the "not ready" errors only, the way Forever's own error frame does, and useful errors like "Out of range" stay. The last line mutes the spell fizzle sound until you restart the game. These macros press spells on cooldown a lot, so this keeps them quiet.

### Gnome: Eureka! with your bolt

```
#showtooltip Frostbolt
/cast Eureka!
/cast Frostbolt
```

- **Replaces:** Q, your bolt, the spell you press most and the bulk of your damage. Fire puts Fireball in both places, Frostfire its Frostfire Bolt from 40, and the Arcane spec (not Arcane-Frost, whose Q is Frostbolt) its Arcane Missiles from 8.
- **Frees:** Eureka! never needs a key of its own.
- **Fill it with:** Nothing.
- **Why it works:** Eureka! has no global cooldown, so one press fires it and starts the bolt. For the next 2 minutes the Eureka! line fails and the bolt still casts: use the macro above to quiet the "not ready" errors. Q is your most-pressed key, so Eureka! goes out on the first bolt after it is ready.
- **What it boosts:** for 8 seconds every mage attack spell costs 10% less mana and its direct damage is 10% higher (the simulator's spell data, 2026-11-06; it names Frostbolt, Ice Lance, Frost Nova, Fire Blast, Cone of Cold, Blizzard, Arcane Missiles and Fireball). An earlier beta text (build 70291) read "your next 3 non-periodic damaging abilities" instead, so read the tooltip in your own client before you trust either.
- **Timing:** the bonus counts when a bolt finishes, so the bolt you start with Eureka! gets it, and starting Eureka! at a cast's start or at its end boosts the same number of bolts. Pressed alone in the last moment of a Frostbolt's cast it would boost one bolt more, since the simulator works a bolt's damage out when its cast ends: untested, the game may not let Eureka! go out while you cast, and on a key of its own it is easy to forget again. Once the bolt is flying it is too late for it.
- **No macro can time it:** a macro's lines all run in the same instant, so Frostbolt first and Eureka! second still fires Eureka! as the cast starts, and a `/castsequence` moves to its next spell only when the cast finishes (the client's CastSequenceManager.lua steps on UNIT_SPELLCAST_SUCCEEDED).

## Frost

Leveling and raid. Keys below are the keys of the [keybinds page](leveling/keybinds.md), whose layout is the Arcane-Frost one; the Frost build uses the same keys.

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
/cast Arcane Wrath
```

- **Replaces:** Arcane Power and Presence of Mind, in a build that takes both (Arcane Power needs Presence of Mind). The leveling Arcane and Arcane-Frost builds take no Arcane Power, so this is for a raid build that does; check yours.
- **Frees:** Two keys.
- **Fill it with:** Nothing: Evocation already has 4.
- **Why it works:** Arcane Power and Presence of Mind are both off the global cooldown, so one press starts them and the Arcane Wrath, which Presence of Mind makes instant. Use it for a burst, not every pull. For Arcane-Frost, use the Presence of Mind macro on your keybinds page; for the Arcane leveling spec, Shift+Q holds Presence of Mind and Arcane Wrath.

## Fire

Fireball and Heating Up.

### Combustion with your opening Pyroblast

```
#showtooltip Pyroblast
/cast Combustion
/cast Pyroblast
```

- **Replaces:** The Combustion key (Combustion is a talent, level 59 on the Fire leveling page).
- **Frees:** One key.
- **Fill it with:** Nothing: the Fire guide puts this macro on Shift+Q and keeps Blast Wave on C. Fire opens every pull with a hard-cast Pyroblast, so that is the spell the macro casts; with no Combustion ready, the second line still opens the pull.
- **Why it works:** Combustion is off the global cooldown.

### Instant Pyroblast

```
#showtooltip Pyroblast
/cast Presence of Mind
/cast Pyroblast
```

- **Replaces:** Presence of Mind and one Pyroblast press, if your build has the Presence of Mind talent (none of the current Fire or Frostfire leveling pages' builds does).
- **Frees:** One key.
- **Fill it with:** Nothing.
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
