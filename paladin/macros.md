# Paladin macros (hand-written)

[Paladin](README.md) > Macros

Macro ideas for every paladin spec, for leveling and raid: what each one does, which keys it replaces and what could go on the keys it frees. **These are theory: none has been tested in Forever's client yet.** The commands are real, though: `/cast`, `/use`, `/castsequence`, `/startattack`, `/stopattack`, `/stopcasting`, `/cancelaura`, `/cancelform` and `/petattack` are all in Forever's own UI code. If a macro misbehaves, go back to the plain spell.

**The rule behind them:** one press only fires two spells if the first is off the global cooldown. In the simulator's data, these paladin spells are: Judgement, Swift Judgement, Divine Favor, Templar's Bulwark and Voice of Truth. A macro can name more than one spell on the global cooldown, but only the first that can go will fire.

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

## Retribution

Leveling and raid. Keys below are your [Retribution keybinds](leveling/keybinds.md), which already hold two macros: the Holy Strike macro on Q and the seal and Judgement macro on R.

### The whole rotation on one key

```
#showtooltip Holy Strike
/startattack [harm,nodead]
/castsequence reset=target Seal of Righteousness, Judgement, Judgement, Judgement
/cast Holy Strike
```

- **Replaces:** Q and R, from level 6.
- **Frees:** R.
- **Fill it with:** R takes Exorcism from 2, the biggest hit you have on Undead and Demons, and 2 goes free. From 44 Hammer of Wrath can leave Shift+R for 2.
- **Why it works:** Judgement is off the global cooldown, so one press casts both attacks in the fight lab's order. Judgement then fires as soon as it is ready, so press E before Q when you want the doubled hit. Change the seal at level 20.

### Repentance that holds

```
#showtooltip Repentance
/stopattack
/cast Repentance
```

- **Replaces:** Nothing: a variant for Shift+E, from 49 if your build takes it.
- **Frees:** Nothing.
- **Fill it with:** Nothing.
- **Why it works:** Any damage wakes the mob, and your next white swing would do it. Turning your swings off first lets you heal, or set up the doubled Judgement on R. Humanoids only. Your next Q turns the swings back on.

## Protection

Tanking and the Protection leveling page.

### Two Judgements on one press

```
#showtooltip Judgement
/cast Judgement
/cast Swift Judgement
```

- **Replaces:** The Judgement and Swift Judgement keys.
- **Frees:** One key.
- **Fill it with:** Holy Shield, if it sits on a harder reach.
- **Why it works:** Both are off the global cooldown, and the rotation wants Swift Judgement right after a Judgement. Swift Judgement's 1-minute cooldown just makes that line do nothing most presses.

### Absorb, then heal

```
#showtooltip Templar's Bulwark
/cast Templar's Bulwark
/cast [@player] Holy Light
```

- **Replaces:** Templar's Bulwark, when you press it to heal behind it.
- **Frees:** One key.
- **Fill it with:** Divine Protection's key can take Blessing of Protection, since both share Forbearance.
- **Why it works:** Templar's Bulwark is off the global cooldown and applies Forbearance. The rotation heals behind its absorb.

### Seal of Fury and Judgement on one key

```
#showtooltip Judgement
/castsequence reset=target Seal of Fury, Judgement, Judgement, Judgement
```

- **Replaces:** The seal key and the Judgement key.
- **Frees:** One key.
- **Fill it with:** Consecration.
- **Why it works:** The Retribution macro with your tanking seal.

## Holy

Healing, and the Holy leveling page.

### A sure critical heal

```
#showtooltip Divine Favor
/cast Divine Favor
/cast [@mouseover,help,nodead][] Holy Light
```

- **Replaces:** Divine Favor and one heal press.
- **Frees:** One key.
- **Fill it with:** Cleanse on a mouseover.
- **Why it works:** Divine Favor is off the global cooldown.

### Heal whoever your mouse is on

```
#showtooltip
/cast [@mouseover,help,nodead][] Flash of Light
```

- **Replaces:** Clicking raid frames before each heal.
- **Frees:** No key, but every heal gets a click shorter.
- **Fill it with:** Do the same for Holy Light and Cleanse.
- **Why it works:** With no friend under the mouse it casts on your target. Fits any healer key.

### Holy Shock at the mob or yourself

```
#showtooltip Holy Shock
/cast [harm] Holy Shock; [@player] Holy Shock
```

- **Replaces:** Clicking yourself to heal with it while leveling.
- **Frees:** Nothing.
- **Fill it with:** Nothing.
- **Why it works:** A hostile target gets the damage, anything else heals you. Holy leveling uses both sides of it.

## Prot-Ret and Shockadin

The hybrids.

### Holy Shock with Judgement

```
#showtooltip Holy Shock
/cast Judgement
/cast Holy Shock
```

- **Replaces:** The Judgement key, for Shockadin.
- **Frees:** One key.
- **Fill it with:** Exorcism.
- **Why it works:** Judgement is off the global cooldown. Prot-Ret plays Retribution's macros.
