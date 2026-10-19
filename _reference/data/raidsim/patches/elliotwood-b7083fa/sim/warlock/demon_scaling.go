package warlock

// wow-forever patch (2026-10-08): Forever's demon scaling. The fork (2ce8265) gives demons nothing from the warlock ("Forever's
// demons inherit nothing from the warlock"); Blizzard's Rogue and Warlock deep dive (2026-10-07,
// worldofwarcraft.blizzard.com/en-us/news/24310968): "Pets now scale from their summoner's stats". The numbers are the Forever
// client's own, build 1.60.1.70291: Camelot/PaperDollFrame.lua (github.com/Gethe/wow-ui-source, forever branch) WARLOCK_PET_BONUS
// PET_BONUS_SPELLDMG_TO_AP 0.17, PET_BONUS_SPELLDMG_TO_SPELLDMG 0.1, PET_BONUS_ARMOR 0.35, PET_BONUS_STAM 0 ("Pets no longer have
// primary attributes"), and its GlobalStrings: "Increased by 100% of Master's Spell Critical Strike Chance", "Every 1 Stamina adds
// 7.5 Health". Our readings, not in the client text: the spell damage is the warlock's generic bonus plus the higher of its Fire and
// Shadow bonus (the character-sheet code the table comes from takes the higher school); the crit applies to the demon's melee as
// well as its spells; hit: Blizzard's known issues (2026-09-18, us.forums.blizzard.com/en/wow/t/2352687) say the pet's hit does not
// display "the master's scaling coefficient", so it is inherited at a rate nobody published: we assume 100% of the warlock's spell
// hit. Not measured in game yet. The demons inherit once, when summoned (the fork's demons are not dynamic pets).
// WOW_FOREVER_DEMON_SCALING=0 turns the patch off (comparisons).

import (
	"os"

	"github.com/wowsims/forever/sim/core/stats"
)

var demonScalingOff = os.Getenv("WOW_FOREVER_DEMON_SCALING") == "0" // read once at program start

func foreverDemonScaling(owner stats.Stats) stats.Stats {
	if demonScalingOff {
		return stats.Stats{}
	}
	school := owner[stats.FireDamage]
	if owner[stats.ShadowDamage] > school {
		school = owner[stats.ShadowDamage]
	}
	sd := owner[stats.SpellDamage] + school
	var s stats.Stats
	s[stats.AttackPower] = 0.17 * sd
	s[stats.SpellDamage] = 0.10 * sd
	s[stats.Armor] = 0.35 * owner[stats.Armor]
	s[stats.Health] = 7.5 * owner[stats.Stamina]
	s[stats.SpellCritPercent] = owner[stats.SpellCritPercent]
	s[stats.PhysicalCritPercent] = owner[stats.SpellCritPercent]
	s[stats.SpellHitPercent] = owner[stats.SpellHitPercent]
	s[stats.PhysicalHitPercent] = owner[stats.SpellHitPercent]
	return s
}
