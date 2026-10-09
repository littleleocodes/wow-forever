package hunter

// wow-forever patch (2026-10-03, sources and the hit rule 2026-10-08): Forever's hunter pet scaling. Blizzard's class deep dive
// ("World of Warcraft: Forever Class Deep Dives — Hunter and Druid", news.blizzard.com/en-us/article/24301515): "Pets now get
// increased stats based on their Hunter's gear. Pets can no longer receive player buffs that increase their stats" (the fork gives
// pets no raid buffs: Pet.AddRaidBuffs and AddPartyBuffs do nothing). The numbers are the Forever client's own (build 1.60.1.70291,
// the same since 69893): GlobalStrings "Increased by 10% of Master's Attack Power from whichever is higher: Melee or Ranged",
// "Increased by 100% of Master's Critical Strike Chance", "Every 1 Stamina adds 2 Health", and Camelot/PaperDollFrame.lua
// HUNTER_PET_BONUS PET_BONUS_ARMOR 0.3 (github.com/Gethe/wow-ui-source, forever branch); the community's Forever Beta Changes page
// (github.com/classic-hunter/forever-hunter/wiki, 2026-10-01) copies them. The fork (40be98e, and 2ce8265 on 2026-10-09) gives the
// pet nothing from its owner (makeStatInheritance returns empty stats). WOW_FOREVER_PET_SCALING=0 turns the stats off (comparisons).

import (
	"os"

	"github.com/wowsims/forever/sim/core/stats"
)

// Read once at program start: the dynamic pet inherits on every owner stat change, a hot path.
var petScalingOff = os.Getenv("WOW_FOREVER_PET_SCALING") == "0"
var petNormalize = os.Getenv("WOW_FOREVER_PET_NORMALIZE") == "1"

func foreverPetScaling(owner stats.Stats) stats.Stats {
	if petScalingOff {
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

// foreverPetHitSpeed is the swing time a pet's base damage per hit is computed for. Forever does not normalize pet damage by attack
// speed: the client's Faster Attack I-VII passives (spells 1263099-1263114, build 70291) raise a 2.0 s base speed by 17-100% and
// change nothing else, and forum measurements at levels 20 and 30 (us.forums.blizzard.com/en/wow/t/2354844/37, /t/2375768) put a
// 1.2 s cat 42% and a faster wolf 26-30% ahead of a 2.0 s pet with the same attack power: damage per hit = a fixed base + attack power
// / 14 x swing time. So every pet's base hit is the fork's 2.0 s value and a faster pet does more damage; the fork scales the base hit
// with the pet's own speed (equal damage at every speed). Nobody has measured it at level 60. WOW_FOREVER_PET_NORMALIZE=1 restores
// the fork's rule (comparisons).
func foreverPetHitSpeed(attackSpeed float64) float64 {
	if petNormalize {
		return attackSpeed
	}
	return 2.0
}
