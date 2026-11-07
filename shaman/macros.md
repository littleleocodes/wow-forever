# Shaman macros (hand-written)

[Shaman](README.md) > Macros

Macro ideas for every shaman spec, for leveling and raid: what each one does, which keys it replaces and what could go on the keys it frees. **These are theory: none has been tested in Forever's client yet.** The commands are real, though: `/cast`, `/use`, `/castsequence`, `/startattack`, `/stopattack`, `/stopcasting`, `/cancelaura`, `/cancelform` and `/petattack` are all in Forever's own UI code. If a macro misbehaves, go back to the plain spell.

**The rule behind them:** one press only fires two spells if the first is off the global cooldown. In the simulator's data, these shaman spells are: Nature's Swiftness and Rage of the Farseer. A macro can name more than one spell on the global cooldown, but only the first that can go will fire.

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

## Enhancement

Leveling and raid. Keys below are your [Enhancement keybinds](leveling/keybinds.md), with the Earth Shock macro on Q.

### Rage of the Farseer with Stormstrike

```
#showtooltip Stormstrike
/startattack [harm,nodead]
/cast Rage of the Farseer
/cast Stormstrike
```

- **Replaces:** R and 4, from level 40.
- **Frees:** 4.
- **Fill it with:** 4 takes Healing Stream Totem from Shift+Mouse 5.
- **Why it works:** Rage of the Farseer is off the global cooldown, and the rotation wants it at the start of a fight. Stormstrike is first in your fight anyway.

### Instant heal

```
#showtooltip Nature's Swiftness
/cast Nature's Swiftness
/cast [@player] Healing Wave
```

- **Replaces:** C, in a build that has Nature's Swiftness.
- **Frees:** Nothing.
- **Fill it with:** Nothing.
- **Why it works:** Nature's Swiftness is off the global cooldown, so one press is a full heal with no cast.

### Stop the cast, then shock

```
#showtooltip Earth Shock
/stopcasting
/startattack [harm,nodead]
/cast Earth Shock
```

- **Replaces:** Nothing: a variant for Q.
- **Frees:** Nothing.
- **Fill it with:** Nothing.
- **Why it works:** Drops a Lightning Bolt in progress so the interrupt lands on the first press.

## Elemental

Leveling and raid.

### Lightning Mastery into your first bolt

```
#showtooltip Lightning Mastery
/castsequence reset=15 Lightning Mastery, Lightning Bolt
```

- **Replaces:** The Lightning Mastery key.
- **Frees:** One key.
- **Fill it with:** Chain Lightning, if it sits on a harder reach.
- **Why it works:** The first press starts the window and the next casts faster bolts. It may share the global cooldown, so a sequence is the safe form.

### Instant big hit

```
#showtooltip Lightning Bolt
/cast Nature's Swiftness
/cast Lightning Bolt
```

- **Replaces:** Nature's Swiftness, used for damage.
- **Frees:** Nothing.
- **Fill it with:** Keep plain Lightning Bolt on its key.
- **Why it works:** Off the global cooldown. A finisher for a mob you need dead now.

### Stop the cast, then shock

```
#showtooltip Earth Shock
/stopcasting
/cast Earth Shock
```

- **Replaces:** Nothing: a variant.
- **Frees:** Nothing.
- **Fill it with:** Nothing.
- **Why it works:** The same macro as Enhancement, without the swings.

## Restoration

Healing. Restoration levels with the Enhancement rotation.

### Heal whoever your mouse is on

```
#showtooltip
/cast [@mouseover,help,nodead][] Lesser Healing Wave
```

- **Replaces:** Clicking raid frames.
- **Frees:** Nothing.
- **Fill it with:** Do the same for Healing Wave, Chain Heal and Riptide.
- **Why it works:** With no friend under the mouse it casts on your target.

### Instant big heal

```
#showtooltip Nature's Swiftness
/cast Nature's Swiftness
/cast [@mouseover,help,nodead][] Healing Wave
```

- **Replaces:** Nature's Swiftness and one heal press.
- **Frees:** One key.
- **Fill it with:** Mana Tide Totem.
- **Why it works:** Nature's Swiftness is off the global cooldown.
