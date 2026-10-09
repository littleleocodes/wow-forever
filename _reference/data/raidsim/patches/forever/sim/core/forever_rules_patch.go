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

import "os"

func foreverHitSuppression() float64 {
	if os.Getenv("WOW_FOREVER_CLASSIC_HIT") == "1" {
		return 0.01
	}
	return 0
}

func foreverSpellMissFloor() float64 {
	if os.Getenv("WOW_FOREVER_CLASSIC_HIT") == "1" {
		return 0.01
	}
	return 0
}

// ExpectedStat CreatureHealth by level (client build 1.60.1.70291, ExpansionID -2 rows), for the levels a player character has
// in the simulator.
var foreverExpectedCreatureHealth = map[int32]float64{60: 4365}

func foreverRageHealth(unit *Unit) float64 {
	if os.Getenv("WOW_FOREVER_RAGE_PLAYER_HEALTH") == "1" {
		return unit.MaxHealth()
	}
	if h, ok := foreverExpectedCreatureHealth[unit.Level]; ok {
		return h
	}
	return unit.MaxHealth()
}
