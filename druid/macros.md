# Druid macros (hand-written)

[Druid](README.md) > Macros

Macro ideas for every druid spec, for leveling and raid: what each one does, which keys it replaces and what could go on the keys it frees. **These are theory: none has been tested in Forever's client yet.** The commands are real, though: `/cast`, `/use`, `/castsequence`, `/startattack`, `/stopattack`, `/stopcasting`, `/cancelaura`, `/cancelform` and `/petattack` are all in Forever's own UI code. If a macro misbehaves, go back to the plain spell.

**The rule behind them:** one press only fires two spells if the first is off the global cooldown. In the simulator's data, these druid spells are: Dash, Enrage, Feral Charge, Growl, Maul, Nature's Swiftness and Prowl. A macro can name more than one spell on the global cooldown, but only the first that can go will fire.

To make one: Esc, Macros, New, pick the question-mark icon so the button shows the spell, and drag it onto the key. Your layout is on the [keybinds page](leveling/keybinds.md).

## Every spec

### Best healing potion in your bags

```
#showtooltip
/use item:18253
/use item:13446
/use item:18839
/use item:3928
/use item:241650
/use item:1710
/use item:247242
/use item:929
/use item:247241
/use item:247240
/use item:858
/use item:247239
/use item:118
/use item:4596
```

- **Replaces:** clicking a potion in your bags.
- **Frees:** nothing: this fills a free key, Shift+C on your bars. C stays with Innervate from 40 (the level guides' layout).
- **Why it works:** only the first potion you own goes off, because they share a cooldown.

The numbers are item ids, best first: the 14 names would not fit in a macro's 255 characters (this is 232; with the RestCue add-on, which writes the best potion you carry into the first line, 244). Item ids work in Forever's client: the button shows the potion's icon and how many you carry (tested in game on 2026-11-22). The order is the health you keep. Forever's Discolored potions heal more at once, then take three quarters of it back as a 6-second poison or a 12-second disease (from the client's spell data, not seen in game), so they rank by the quarter you keep; for a last-second save, press a Discolored potion by hand from your bags. Left out: the battleground draughts (they work only inside a battleground); Restored and Perishable Healing Potion, Forever's own (no source found); a second Major Healing Potion (item 223913, not confirmed in Forever).

| Line | Potion: health, level, where from |
|---|---|
| item:18253 | Major Rejuvenation Potion: 1,440-1,760 health and as much mana; level 50; Alchemy, or the auction house. |
| item:13446 | Major Healing Potion: 1,050-1,750; level 45; First Aid, or the auction house. |
| item:18839 | Combat Healing Potion: 700-900; level 35; battleground vendors (Alterac Mountains, Stormwind, the battlegrounds); bind on pickup. |
| item:3928 | Superior Healing Potion: 700-900; level 35; First Aid, or the auction house. |
| item:241650 | Major Discolored Healing Potion: 2,625-2,975 at once, 75% back as a poison or disease: about 700 kept; level 60; Alchemy, or the auction house. |
| item:1710 | Greater Healing Potion: 455-585; level 21; First Aid, or the auction house. |
| item:247242 | Superior Discolored Healing Potion: 1,500-1,700 at once: about 400 kept; level 35; Alchemy, or the auction house. |
| item:929 | Healing Potion: 280-360; level 12; First Aid, or the auction house. |
| item:247241 | Greater Discolored Healing Potion: 975-1,105 at once: about 260 kept; level 21; Alchemy, or the auction house. |
| item:247240 | Discolored Healing Potion: 600-680 at once: about 160 kept; level 12; Alchemy, or the auction house. |
| item:858 | Lesser Healing Potion: 140-180; level 3; First Aid, or the auction house. |
| item:247239 | Lesser Discolored Healing Potion: 300-340 at once: about 80 kept; level 3; Alchemy, or the auction house. |
| item:118 | Minor Healing Potion: 70-90; level 1; First Aid, or the auction house. |
| item:4596 | Minor Discolored Healing Potion: 150-170 at once: about 40 kept; level 5; Alchemy, or the auction house. |

### Best mana potion in your bags

```
#showtooltip
/use item:13444
/use item:18253
/use item:18841
/use item:13443
/use item:6149
/use item:3827
/use item:3385
/use item:2455
/use item:2456
```

- **Replaces:** clicking a potion in your bags.
- **Frees:** nothing: this fills a free key, Shift+X on your bars. It shares the healing potion's cooldown.

The numbers are item ids, best first by the mana they give: the nine names would not fit in 255 characters (this is 151; 162 with RestCue's first line). Major Rejuvenation Potion gives as much health as mana: it is second here and first in the healing macro, so either macro can spend it. Every potion here shares the healing potions' 2-minute cooldown. Left out: the battleground draughts; Restored Mana Potion, Forever's own (no source found).

| Line | Potion: mana, level, where from |
|---|---|
| item:13444 | Major Mana Potion: 1,350-2,250; level 49; Alchemy, or the auction house. |
| item:18253 | Major Rejuvenation Potion: 1,440-1,760 mana and as much health; level 50; Alchemy, or the auction house. |
| item:18841 | Combat Mana Potion: 900-1,500; level 41; battleground vendors (Alterac Mountains, Stormwind, the battlegrounds); bind on pickup. |
| item:13443 | Superior Mana Potion: 900-1,500; level 41; Alchemy, or the auction house. |
| item:6149 | Greater Mana Potion: 700-900; level 31; Alchemy, or the auction house. |
| item:3827 | Mana Potion: 455-585; level 22; Alchemy, or the auction house. |
| item:3385 | Lesser Mana Potion: 280-360; level 14; Alchemy, or the auction house. |
| item:2455 | Minor Mana Potion: 140-180; level 5; Alchemy, or the auction house. |
| item:2456 | Minor Rejuvenation Potion: 90-150 mana and as much health; level 5; Alchemy, or the auction house. |

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
- **Why it works:** Both are off the global cooldown. Enrage just fails while it is on cooldown, so this is safe to use all fight. It also fires on a mob that is nearly dead, where the fight lab skips Enrage (it lowers your armor): press plain Maul then.

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

### No instant Starfire

Nature's Swiftness only makes **Nature** spells instant (Wrath, Healing Touch, Regrowth), and Starfire is an Arcane spell, so there is no instant
Starfire macro. No Balance build here takes Nature's Swiftness either. The keys Balance frees come from the Regrowth macro above (one press less in
an emergency) and from Innervate on a mouseover (the Restoration section has it).

## Restoration

Healing. Restoration levels as a cat, with Feral's macros.

### Instant big heal

For a build with **Nature's Swiftness**: the raid page's 11/0/40 pick takes none (the hand-made build under Other builds does).

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
- **Fill it with:** Do the same for Regrowth and Swiftmend.
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
