# Druid macros (hand-written)

[Druid](README.md) > Macros

Macro ideas for every druid spec, for leveling and raid: what each one does, which keys it replaces and what could go on the keys it frees. **These are theory: none has been tested in Forever's client yet.** The commands are real, though: `/cast`, `/use`, `/castsequence`, `/startattack`, `/stopattack`, `/stopcasting`, `/cancelaura`, `/cancelform` and `/petattack` are all in Forever's own UI code. If a macro misbehaves, go back to the plain spell.

**The rule behind them:** one press only fires two spells if the first is off the global cooldown. In the simulator's data, these druid spells are: Dash, Enrage, Feral Charge, Growl, Maul, Nature's Swiftness and Prowl. A macro can name more than one spell on the global cooldown, but only the first that can go will fire.

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

## Feral Combat

Leveling and raid. Keys below are your [Feral Combat keybinds](leveling/keybinds.md), with the Maul and Claw macros on Q of each form's bar.

### Claw or Ravage from one key

```
#showtooltip
/startattack [harm,nodead]
/cast [stealth] Ravage; Claw
```

- **Replaces:** Q (cat), and Q on the Prowl bar.
- **Frees:** The whole Prowl bar: you no longer set it up.
- **Fill it with:** Pounce goes on E (cat): `/cast [stealth] Pounce; Feral Charge`.
- **Why it works:** One key plays both, so bar 1 is a form's bar and nothing more. Before 32, use Claw alone. Ravage needs you behind the mob.

### Cat Form, then Prowl

```
#showtooltip Prowl
/cast [noform:3] Cat Form
/cast [form:3,nostealth] Prowl
```

- **Replaces:** Shift+Q and 1 (cat).
- **Frees:** 1 (cat).
- **Fill it with:** 1 (cat) takes Rake from Mouse 5, and Mouse 5 (cat) goes free.
- **Why it works:** Prowl is off the global cooldown. First press shifts, second prowls. The form number follows the order you learned them, so if the wrong form fires, try 2 or 4.

### Enrage with your first Maul

```
#showtooltip Maul
/startattack [harm,nodead]
/cast Enrage
/cast Maul
```

- **Replaces:** Q (bear) and Mouse 5 (bear).
- **Frees:** Mouse 5 (bear).
- **Fill it with:** Swipe from 1 (bear), for pulls of two.
- **Why it works:** Both are off the global cooldown. Enrage just fails while it is on cooldown, so this is safe to use all fight.

### Out of form and heal

```
#showtooltip Regrowth
/cancelform
/cast [@player] Regrowth
```

- **Replaces:** Shift+Q, then Mouse 5.
- **Frees:** One press in an emergency.
- **Fill it with:** A free slot, Shift+Mouse 5 on your page.
- **Why it works:** Already on your keybinds page. Forever's UI code has `/cancelform`.

## Balance

Moonkin.

### Out of Moonkin and heal

```
#showtooltip Regrowth
/cancelform
/cast [@player] Regrowth
```

- **Replaces:** Clicking off the form, then the heal.
- **Frees:** One press.
- **Fill it with:** Entangling Roots stays next to it.
- **Why it works:** The rotation roots, steps out, then heals. Click Moonkin Form back on afterward, once you have the mana.

### Instant Starfire

```
#showtooltip Starfire
/cast Nature's Swiftness
/cast Starfire
```

- **Replaces:** Nature's Swiftness, used for damage.
- **Frees:** Nothing.
- **Fill it with:** Keep plain Starfire on its key.
- **Why it works:** Off the global cooldown, in a build that has it. A finisher, or an opener on a runner.

## Restoration

Healing. Restoration levels as a cat, with Feral's macros.

### Instant big heal

```
#showtooltip Nature's Swiftness
/cast Nature's Swiftness
/cast [@mouseover,help,nodead][] Healing Touch
```

- **Replaces:** Nature's Swiftness and one heal press.
- **Frees:** One key.
- **Fill it with:** Innervate on a mouseover.
- **Why it works:** Nature's Swiftness is off the global cooldown.

### Heal whoever your mouse is on

```
#showtooltip
/cast [@mouseover,help,nodead][] Rejuvenation
```

- **Replaces:** Clicking raid frames.
- **Frees:** Nothing.
- **Fill it with:** Do the same for Regrowth, Swiftmend and Wild Growth.
- **Why it works:** With no friend under the mouse it casts on your target.

### Innervate on whoever your mouse is on

```
#showtooltip Innervate
/cast [@mouseover,help,nodead][@player] Innervate
```

- **Replaces:** Targeting a friend for it.
- **Frees:** Nothing.
- **Fill it with:** Nothing.
- **Why it works:** With no friend under the mouse, it lands on you.
