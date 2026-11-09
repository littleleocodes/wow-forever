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
- **Frees:** nothing: this fills a free key, Shift+3 on your bars in every spec's by-level guide (C holds Healing Wave from 20).
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
- **Frees:** nothing: this fills a free key, Shift+4 on your bars. It shares the healing potion's cooldown.

### Quiet the not-ready errors

```
/run UIErrorsFrame:SetMessageTypeEnabled(LE_GAME_ERR_SPELL_COOLDOWN,false)
/run UIErrorsFrame:SetMessageTypeEnabled(LE_GAME_ERR_ABILITY_COOLDOWN,false)
/run for i=569772,569776 do MuteSoundFile(i) end
```

- **Replaces:** nothing. Click it once after each login from a side bar.
- **Why it works:** the first two lines turn off the text, speech and sound of the "not ready" errors only, the way Forever's own error frame does, and useful errors like "Out of range" stay. The last line mutes the spell fizzle sound until you restart the game. These macros press spells on cooldown a lot, so this keeps them quiet.

## Enhancement

Leveling and raid. Keys below are the [Enhancement layout](leveling/keybinds.md), with the Earth Shock macro on Q; the other specs' keys are in their by-level guides.

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

Raid only: Lightning Mastery is a talent of the Elemental raid build (a level-40 talent, 3-minute cooldown). Neither Elemental leveling build takes it.

```
#showtooltip Lightning Mastery
/castsequence reset=15 Lightning Mastery, Lightning Bolt
```

- **Replaces:** nothing in the leveling layouts. It goes on key 4, which the Elemental level-by-level guide leaves free.
- **Frees:** Nothing.
- **Fill it with:** Nothing.
- **Why it works:** The first press starts the 15-second window (bolts cast 0.5 s faster, Chain Lightning has no cooldown) and the next casts the first bolt. Lightning Mastery is not in the list of spells that skip the global cooldown, so it costs a cast and the sequence needs two presses.

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

Healing. Restoration levels with the Enhancement rotation (without Stormstrike, Maelstrom Weapon and Rage of the Farseer).

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

- **Replaces:** Nature's Swiftness (key 3 from level 35) and Healing Wave (C); put the macro on C.
- **Frees:** 3.
- **Fill it with:** Nothing yet; Mana Tide Totem is already on 4.
- **Why it works:** Nature's Swiftness is off the global cooldown, so one press is a full Healing Wave with no cast. Only the Restoration build takes the talent.
