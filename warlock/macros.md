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
- **Frees:** nothing: this fills a free key, Shift+C on your bars (C holds your Healthstone).
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
- **Frees:** nothing: this fills a free key, Shift+X on your bars. It shares the healing potion's cooldown.

### Quiet the not-ready errors

```
/run UIErrorsFrame:SetMessageTypeEnabled(LE_GAME_ERR_SPELL_COOLDOWN,false)
/run UIErrorsFrame:SetMessageTypeEnabled(LE_GAME_ERR_ABILITY_COOLDOWN,false)
/run for i=569772,569776 do MuteSoundFile(i) end
```

- **Replaces:** nothing. Click it once after each login from a side bar.
- **Why it works:** the first two lines turn off the text, speech and sound of the "not ready" errors only, the way Forever's own error frame does, and useful errors like "Out of range" stay. The last line mutes the spell fizzle sound until you restart the game. These macros press spells on cooldown a lot, so this keeps them quiet.

## Affliction

Leveling and raid. The keys below are those of the [keybinds page](leveling/keybinds.md).

### Every dot on one key

```
#showtooltip Corruption
/petattack
/castsequence reset=target Corruption, Bane of Agony, Siphon Life
```

- **Replaces:** The pull macro on Mouse 4, Bane of Agony on 1 and Siphon Life on 3.
- **Frees:** Keys 1 and 3.
- **Fill it with:** Nothing needed: Fear, Drain Life and Death Coil, the keys for when a mob reaches you, already sit on E, R and F.
- **Why it works:** One press each: three presses put every dot up, and the pet goes in with the first. The sequence loops, so stop pressing once they are up. Before you learn Siphon Life, drop it from the list.

### Amplified curse

```
#showtooltip Bane of Agony
/cast Amplify Curse
/cast Bane of Agony
```

- **Replaces:** Plain Bane of Agony on 1: the keybinds page puts this macro there once you have the talent.
- **Frees:** The key Amplify Curse would need of its own.
- **Fill it with:** Nothing: Life Tap already has 4.
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

- **Replaces:** Clicking Fel Domination and the summon on your side bar.
- **Frees:** Nothing on your bars: summons have no key. Put it on the side bar, or on a free Shift key if you summon in a fight.
- **Fill it with:** Nothing: Health Funnel already has Shift+R.
- **Why it works:** Fel Domination is off the global cooldown and makes the next summon fast. Swap the demon's name as you like.

### Dots and the brand

```
#showtooltip Searing Pain
/petattack
/cast Searing Pain
```

- **Replaces:** Searing Pain on Mouse 5, if you would rather send the pet with the brand than with the Corruption pull on Mouse 4.
- **Frees:** Nothing: the pull macro on Mouse 4 already sends the pet.
- **Fill it with:** Nothing: Fear has E.
- **Why it works:** The pet goes in with your Searing Pain. The fight lab opens with Corruption instead (the pull macro on Mouse 4), so this is for players who would rather open with the brand.

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

- **Replaces:** Immolate on 2 and Conflagrate on R.
- **Frees:** Key 2.
- **Fill it with:** Nothing needed: Shadowburn already sits on Mouse 5.
- **Why it works:** First press burns the mob, the next one consumes or refreshes it, depending on your talents. On a new target it starts over.

### Pet and fire

```
#showtooltip Immolate
/petattack
/cast Immolate
```

- **Replaces:** Immolate on 2. The keybinds page's Destruction pull macro on Mouse 4 opens with Shadow Bolt instead, as the fight lab does from level 10.
- **Frees:** Key 2, if you pull with this macro.
- **Fill it with:** Nothing: Fear has E.
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
