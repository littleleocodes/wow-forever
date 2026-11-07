# Warlock macros (hand-written)

[Warlock](README.md) > Macros

Macro ideas for every warlock spec, for leveling and raid: what each one does, which keys it replaces and what could go on the keys it frees. **These are theory: none has been tested in Forever's client yet.** The commands are real, though: `/cast`, `/use`, `/castsequence`, `/startattack`, `/stopattack`, `/stopcasting`, `/cancelaura`, `/cancelform` and `/petattack` are all in Forever's own UI code. If a macro misbehaves, go back to the plain spell.

**The rule behind them:** one press only fires two spells if the first is off the global cooldown. In the simulator's data, these warlock spells are: Amplify Curse, Demonic Sacrifice and Fel Domination. A macro can name more than one spell on the global cooldown, but only the first that can go will fire.

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

## Affliction

Leveling and raid. No keybinds page yet: the warlock's results are still running, so keys below are by job.

### Every dot on one key

```
#showtooltip Corruption
/petattack
/castsequence reset=target Corruption, Bane of Agony, Siphon Life
```

- **Replaces:** Your Corruption, Bane of Agony and Siphon Life keys, and the pet attack key.
- **Frees:** Three keys.
- **Fill it with:** Fear, Death Coil and Drain Life, the keys for when a mob reaches you.
- **Why it works:** One press each: three presses put every dot up, and the pet goes in with the first. The sequence loops, so stop pressing once they are up. Before you learn Siphon Life, drop it from the list.

### Amplified curse

```
#showtooltip Bane of Agony
/cast Amplify Curse
/cast Bane of Agony
```

- **Replaces:** Amplify Curse's key.
- **Frees:** One key.
- **Fill it with:** Life Tap.
- **Why it works:** Amplify Curse is off the global cooldown.

### A wand that never turns itself off

```
#showtooltip Shoot
/cast !Shoot
```

- **Replaces:** Middle mouse, which holds Shoot.
- **Frees:** Nothing.
- **Fill it with:** Nothing.
- **Why it works:** Plain Shoot is a toggle, so a second press stops the wand, like the Attack button. The `!` keeps it on. A simple swap on the key you already use.

## Demonology

Demon builds.

### Summon in a hurry

```
#showtooltip Summon Voidwalker
/cast Fel Domination
/cast Summon Voidwalker
```

- **Replaces:** Fel Domination and the summon key.
- **Frees:** One key.
- **Fill it with:** Health Funnel.
- **Why it works:** Fel Domination is off the global cooldown and makes the next summon fast. Swap the demon's name as you like.

### Dots and the brand

```
#showtooltip Searing Pain
/petattack
/cast Searing Pain
```

- **Replaces:** The Searing Pain key, and the pet attack key.
- **Frees:** One key.
- **Fill it with:** Fear.
- **Why it works:** With Demonic Brand, Searing Pain is your opener, so the pet goes in with it.

### A wand that never turns itself off

```
#showtooltip Shoot
/cast !Shoot
```

- **Replaces:** Middle mouse, which holds Shoot.
- **Frees:** Nothing.
- **Fill it with:** Nothing.
- **Why it works:** Plain Shoot is a toggle, so a second press stops the wand, like the Attack button. The `!` keeps it on. A simple swap on the key you already use.

## Destruction

Immolate and Conflagrate.

### Immolate, then Conflagrate

```
#showtooltip Conflagrate
/castsequence reset=target Immolate, Conflagrate
```

- **Replaces:** The Immolate and Conflagrate keys.
- **Frees:** One key.
- **Fill it with:** Shadowburn, right next to it.
- **Why it works:** First press burns the mob, the next one consumes or refreshes it, depending on your talents. On a new target it starts over.

### Pet and fire

```
#showtooltip Immolate
/petattack
/cast Immolate
```

- **Replaces:** The Immolate key, and the pet attack key.
- **Frees:** One key.
- **Fill it with:** Fear.
- **Why it works:** The pet goes in with your opener.

### A wand that never turns itself off

```
#showtooltip Shoot
/cast !Shoot
```

- **Replaces:** Middle mouse, which holds Shoot.
- **Frees:** Nothing.
- **Fill it with:** Nothing.
- **Why it works:** Plain Shoot is a toggle, so a second press stops the wand, like the Attack button. The `!` keeps it on. A simple swap on the key you already use.
