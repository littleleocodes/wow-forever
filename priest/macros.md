# Priest macros (hand-written)

[Priest](README.md) > Macros

Macro ideas for every priest spec, for leveling and raid: what each one does, which keys it replaces and what could go on the keys it frees. **These are theory: none has been tested in Forever's client yet.** The commands are real, though: `/cast`, `/use`, `/castsequence`, `/startattack`, `/stopattack`, `/stopcasting`, `/cancelaura`, `/cancelform` and `/petattack` are all in Forever's own UI code. If a macro misbehaves, go back to the plain spell.

**The rule behind them:** one press only fires two spells if the first is off the global cooldown. In the simulator's data, these priest spells are: Inner Focus and Power Infusion. A macro can name more than one spell on the global cooldown, but only the first that can go will fire.

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

## Shadow

Leveling and raid. Keys below are your [Shadow keybinds](leveling/keybinds.md).

### The pull on one key

```
#showtooltip Shadow Word: Pain
/castsequence reset=target Vampiric Embrace, Shadow Word: Pain
```

- **Replaces:** Mouse 4 and 1.
- **Frees:** 1.
- **Fill it with:** 1 takes Flash Heal from 3, closer to your hand.
- **Why it works:** Both are on the global cooldown, so press Mouse 4 twice. Use it from 39, when Vampiric Embrace arrives. Until then keep plain Shadow Word: Pain.

### Out of Shadowform and heal

```
#showtooltip Flash Heal
/cancelaura Shadowform
/cast [@player] Flash Heal
```

- **Replaces:** Nothing: a variant for 3.
- **Frees:** Nothing.
- **Fill it with:** Nothing.
- **Why it works:** You cannot heal in Shadowform, so this saves the click off the form. Click Shadowform back on afterward.

### Shield yourself, whatever you target

```
#showtooltip Power Word: Shield
/cast [@player] Power Word: Shield
```

- **Replaces:** Nothing: a variant for F.
- **Frees:** Nothing.
- **Fill it with:** Nothing.
- **Why it works:** It never asks for a target and never lands on a friend by mistake.

### A wand that never turns itself off

```
#showtooltip Shoot
/cast !Shoot
```

- **Replaces:** Middle mouse, which holds Shoot.
- **Frees:** Nothing.
- **Fill it with:** Nothing.
- **Why it works:** Plain Shoot is a toggle, so a second press stops the wand, like the Attack button. The `!` keeps it on. A simple swap on the key you already use.

## Discipline

Healing, and the Discipline leveling page.

### Inner Focus into a big heal

```
#showtooltip Inner Focus
/cast Inner Focus
/cast [@mouseover,help,nodead][] Greater Heal
```

- **Replaces:** Inner Focus and one heal press.
- **Frees:** One key.
- **Fill it with:** Power Infusion.
- **Why it works:** Inner Focus is off the global cooldown.

### Power Infusion on whoever your mouse is on

```
#showtooltip Power Infusion
/cast [@mouseover,help,nodead][@player] Power Infusion
```

- **Replaces:** Targeting a friend for it.
- **Frees:** Nothing.
- **Fill it with:** Nothing.
- **Why it works:** Off the global cooldown, so it never costs you a heal.

### Shield whoever your mouse is on

```
#showtooltip
/cast [@mouseover,help,nodead][] Power Word: Shield
```

- **Replaces:** Clicking raid frames.
- **Frees:** Nothing.
- **Fill it with:** Do the same for Penance and Flash Heal.
- **Why it works:** With no friend under the mouse it casts on your target.

## Holy

Healing, and the Holy leveling page.

### Heal whoever your mouse is on

```
#showtooltip
/cast [@mouseover,help,nodead][] Flash Heal
```

- **Replaces:** Clicking raid frames.
- **Frees:** Nothing.
- **Fill it with:** Do the same for Renew and Greater Heal.
- **Why it works:** With no friend under the mouse it casts on your target.

### Inner Focus into a group heal

```
#showtooltip Inner Focus
/cast Inner Focus
/cast Prayer of Healing
```

- **Replaces:** Inner Focus and one group heal.
- **Frees:** One key.
- **Fill it with:** Dispel Magic on a mouseover.
- **Why it works:** Inner Focus is off the global cooldown.

## Smite

The Holy Fire and Smite damage build.

### Smite that opens with Holy Fire

```
#showtooltip Smite
/castsequence reset=target Holy Fire, Shadow Word: Pain, Smite
```

- **Replaces:** The Holy Fire and Shadow Word: Pain keys, at the pull.
- **Frees:** Two keys.
- **Fill it with:** Penance and Mind Blast.
- **Why it works:** Each press casts the next spell, then Smite repeats. It stays on Smite for the rest of the mob. Press Penance and Mind Blast on their own when ready.
