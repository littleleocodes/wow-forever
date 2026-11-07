# Hunter macros (hand-written)

[Hunter](README.md) > Macros

Macro ideas for every hunter spec, for leveling and raid: what each one does, which keys it replaces and what could go on the keys it frees. **These are theory: none has been tested in Forever's client yet.** The commands are real, though: `/cast`, `/use`, `/castsequence`, `/startattack`, `/stopattack`, `/stopcasting`, `/cancelaura`, `/cancelform` and `/petattack` are all in Forever's own UI code. If a macro misbehaves, go back to the plain spell.

**The rule behind them:** one press only fires two spells if the first is off the global cooldown. In the simulator's data, these hunter spells are: Auto Shot, Bestial Wrath, Deterrence, Feign Death, Rapid Fire and Raptor Strike. A macro can name more than one spell on the global cooldown, but only the first that can go will fire.

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

## Beast-Survival and Survival

The melee hunter. Keys below are your [Beast-Survival keybinds](leveling/keybinds.md), with the Serpent Sting macro on Mouse 4.

### Send the pet with the sting

```
#showtooltip Serpent Sting
/petattack
/startattack [harm,nodead]
/cast Serpent Sting
```

- **Replaces:** Mouse 4, and the pet bar's attack key.
- **Frees:** The pet attack key.
- **Fill it with:** Keep it as your pet's Growl toggle, or give it to Wing Clip so E can take Freezing Trap.
- **Why it works:** `/petattack` is off the global cooldown. One press sends the pet, arms your swings and stings. It uses your target, so pick the mob first.

### Feign, then trap

```
#showtooltip Feign Death
/castsequence reset=30 Feign Death, Freezing Trap
```

- **Replaces:** F and 2.
- **Frees:** 2.
- **Fill it with:** 2 takes Frost Trap from Shift+1.
- **Why it works:** Traps need you out of combat, and Feign Death gets you there: the classic way to freeze a mob mid-fight. Feign Death can be resisted, so look before the second press.

### Finish, or dodge back

```
#showtooltip Raptor Strike
/cast Mongoose Bite
/cast Raptor Strike
```

- **Replaces:** Q and Mouse 5.
- **Frees:** Mouse 5.
- **Fill it with:** Lacerate from 1, a thumb for your bleed.
- **Why it works:** Raptor Strike is off the global cooldown and replaces your next swing. This spends mana on Raptor Strike all fight, which the tuned rules do not: use it only if you dislike watching for a dodge.

## Beast Mastery

The pet hunter.

### Everything at the pull

```
#showtooltip Bestial Wrath
/cast Bestial Wrath
/cast Rapid Fire
/cast Intimidation
```

- **Replaces:** Bestial Wrath, Rapid Fire and Intimidation.
- **Frees:** Two keys.
- **Fill it with:** Mend Pet and Wing Clip, the keys you reach for when it goes wrong.
- **Why it works:** Bestial Wrath and Rapid Fire are off the global cooldown, so all three go in one press. Intimidation needs the pet in melee: send it first.

### Sting and send

```
#showtooltip Serpent Sting
/petattack
/cast !Auto Shot
/cast Serpent Sting
```

- **Replaces:** The sting key, and the Auto Shot and pet attack keys.
- **Frees:** Two keys.
- **Fill it with:** Hunter's Mark.
- **Why it works:** `!` stops a second press turning Auto Shot off.

## Marksmanship and Beast-Marks

The ranged hunter.

### Aimed Shot that keeps Auto Shot on

```
#showtooltip Aimed Shot
/cast !Auto Shot
/cast Aimed Shot
```

- **Replaces:** Q, and the Auto Shot key.
- **Frees:** One key.
- **Fill it with:** Rapid Fire.
- **Why it works:** Pressing it starts your shooting and never stops it.

### Rapid Fire with your burst

```
#showtooltip Rapid Fire
/cast Rapid Fire
/cast Aimed Shot
```

- **Replaces:** Rapid Fire and one Aimed Shot press.
- **Frees:** Nothing, but the opener is one press.
- **Fill it with:** Nothing.
- **Why it works:** Rapid Fire is off the global cooldown.
