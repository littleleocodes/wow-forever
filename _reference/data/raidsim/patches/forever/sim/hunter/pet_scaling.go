package hunter

// wow-forever patch (2026-10-03): Forever's hunter pet scaling. Blizzard's class deep dive ("World of Warcraft: Forever Class Deep
// Dives — Hunter and Druid", news.blizzard.com/en-us/article/24301515): "Pets now get increased stats based on their Hunter's gear";
// the numbers as the community's Forever Beta Changes page states them (github.com/classic-hunter/forever-hunter/wiki, 2026-10-01):
// 1 player Stamina gives the pet 2 Health, the pet gains 30% of the player's Armor, 10% of the player's highest Attack Power source
// and 100% of the player's Crit chance. The fork (40be98e, and master on 2026-10-03) gives the pet nothing from its owner
// (makeStatInheritance returns empty stats). WOW_FOREVER_PET_SCALING=0 turns the patch off (comparisons).

import (
	"os"

	"github.com/wowsims/forever/sim/core/stats"
)

func foreverPetScaling(owner stats.Stats) stats.Stats {
	if os.Getenv("WOW_FOREVER_PET_SCALING") == "0" {
		return stats.Stats{}
	}
	ap := owner[stats.AttackPower]
	if owner[stats.RangedAttackPower] > ap {
		ap = owner[stats.RangedAttackPower]
	}
	var s stats.Stats
	s[stats.AttackPower] = 0.10 * ap
	s[stats.PhysicalCritPercent] = owner[stats.PhysicalCritPercent]
	s[stats.Armor] = 0.30 * owner[stats.Armor]
	s[stats.Health] = 2 * owner[stats.Stamina]
	return s
}
