package core

// wow-forever patch (2026-10-09): Forever mechanics the fork (2ce8265) does not have yet, from Blizzard's own text.
//
// Hit against raid bosses: the client's hit-cap tooltips (GlobalStrings CR_<CLASS>_HIT_CAP_TOOLTIP, build 70291) say "To never miss
// Raid Bosses: 8.00% Melee/Ranged, 17.00% Spells, 27.00% Dual Wielding" (5% / 4% / 24% against your own level). Classic's 1% hit
// suppression against a level 63 target (9% melee) and its 1% spell-miss floor (16% useful spell hit) are not in those numbers, so
// both are off here. WOW_FOREVER_CLASSIC_HIT=1 restores them (comparisons).
//
// Rage from damage taken: the beta development notes of 2026-10-08 (us.forums.blizzard.com/en/wow/t/2360696, post 5): "Fixed a bug
// where the Rage calculation was incorrectly using the player's health to determine Rage gained, instead of an expected creature's
// health." The fork divides by the player's maximum health; here it divides by the client's expected creature health for the
// player's level (ExpectedStat, build 70291: 4365 at level 60). The same notes rebalance the formula's armor assumption ("in the 20%
// to 40% range", was 50%) without a number: not modelled. WOW_FOREVER_RAGE_PLAYER_HEALTH=1 restores the fork's rule.

import (
	"os"
	"strconv"
	"strings"

	"github.com/wowsims/forever/sim/core/stats"
)

// foreverExtraImbues: a second temporary enchant per weapon. Forever lets temporary enchants stack with other weapon effects: rogue
// deep dive (2026-10-07, worldofwarcraft.blizzard.com/en-us/news/24310968) "Poisons can now be applied to weapons at the same time
// as temporary enchantments like Weightstones and Sharpening Stones"; warlock (same article) "Firestone and Spellstone now apply
// Weapon Imbues, that can be stacked with other temporary enchantments like Wizard Oil". The simulator has one consumable enchant
// per hand (poisons fill the rogue's), so the bench passes the extra one as WOW_FOREVER_EXTRA_IMBUES="mh:<id>,oh:<id>"
// (foreverbench: "extraMhImbueId" / "extraOhImbueId" in a config's consumables). Stones and oils use the simulator's own effects;
// the warlock's stones are ours, from the beta tooltips (build 70291): Major Firestone (13701) +2% spell crit and +21 Fire spell
// damage, Major Spellstone (13603) +2% spell haste and +21 Shadow spell damage.
func foreverExtraImbues(agent Agent) {
	env := os.Getenv("WOW_FOREVER_EXTRA_IMBUES")
	if env == "" {
		return
	}
	character := agent.GetCharacter()
	for _, part := range strings.Split(env, ",") {
		hand, idText, ok := strings.Cut(strings.TrimSpace(part), ":")
		if !ok {
			continue
		}
		id, err := strconv.Atoi(strings.TrimSpace(idText))
		if err != nil || id == 0 {
			continue
		}
		switch id {
		case 13701: // Major Firestone
			character.AddStat(stats.SpellCritPercent, 2)
			character.AddStat(stats.FireDamage, 21)
		case 13603: // Major Spellstone
			character.AddStat(stats.ShadowDamage, 21)
			MakePermanent(character.RegisterAura(Aura{
				Label:    "Major Spellstone",
				ActionID: ActionID{ItemID: 13603},
				OnGain: func(aura *Aura, sim *Simulation) {
					aura.Unit.MultiplyCastSpeed(sim, 1.02)
				},
				OnExpire: func(aura *Aura, sim *Simulation) {
					aura.Unit.MultiplyCastSpeed(sim, 1/1.02)
				},
			}))
		default:
			weapon := character.AutoAttacks.MH()
			if hand == "oh" {
				weapon = character.AutoAttacks.OH()
			}
			registerStaticImbue(agent, int32(id), weapon)
		}
	}
}

// The switches are read once at program start: os.Getenv in a hot path (every spell's hit roll) made the bench 3x slower on Windows.
var foreverClassicHit = os.Getenv("WOW_FOREVER_CLASSIC_HIT") == "1"
var foreverRagePlayerHealth = os.Getenv("WOW_FOREVER_RAGE_PLAYER_HEALTH") == "1"

func foreverHitSuppression() float64 {
	if foreverClassicHit {
		return 0.01
	}
	return 0
}

func foreverSpellMissFloor() float64 {
	if foreverClassicHit {
		return 0.01
	}
	return 0
}

// ExpectedStat CreatureHealth by level (client build 1.60.1.70291, ExpansionID -2 rows), for the levels a player character has
// in the simulator.
var foreverExpectedCreatureHealth = map[int32]float64{60: 4365}

func foreverRageHealth(unit *Unit) float64 {
	if foreverRagePlayerHealth {
		return unit.MaxHealth()
	}
	if h, ok := foreverExpectedCreatureHealth[unit.Level]; ok {
		return h
	}
	return unit.MaxHealth()
}
