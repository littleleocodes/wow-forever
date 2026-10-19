package spelldata

// wow-forever patch (2026-10-09): Forever's downranking penalty. Blizzard's beta development notes (2026-10-01,
// us.forums.blizzard.com/en/wow/t/2360696): "spells cast using spell ranks vastly below your current level receive less benefit
// from your Spell Damage and Spell Healing and have a reduced chance to activate your Class abilities and Talents"; the client's
// STAT_SPELLPOWER_TOOLTIP says the same (build 70291). No formula is published. Ours is TBC's rule for the same wording: a rank keeps
// (L + 6) / 60 of its spell power coefficient at level 60, L being the last level the rank is current (the level before the next
// rank of the same name is taught), when L + 5 is below 60; the top rank and unranked spells keep everything. Classic Era's rule for
// spells taught below level 20, which the fork never applied, comes on top for ranks below a higher one: 1 - (20 - taught level) x
// 0.0375 (top ranks are left alone because triggered spells carry odd taught levels: Flametongue Attack's are 1). The level window is
// taken from the rank chain, not the effect's MaxLevel column, because some Forever effects carry a template's (Consecration's top
// ranks list 25). Not modelled: the lower chance to trigger talents (Blizzard: "Using a Rank 1 Frostbolt at level 60 will result in
// a 0% chance to get a Frostbite activation"). WOW_FOREVER_DOWNRANK=0 turns the patch off (comparisons).

import (
	"os"
	"sort"
	"sync"
)

const downrankLevel = 60

var downrankOff = os.Getenv("WOW_FOREVER_DOWNRANK") == "0" // read once at program start (not in the hot path)
var downrankOnce sync.Once
var downrankNext map[int32]int16 // spell id -> the level the next higher rank of the same name is taught at
var downrankTaught map[int32]int16

func buildDownrank() {
	levels := map[string][]int16{}
	for i := range spells {
		s := &spells[i]
		if s.Rank != "" && s.Name != "" {
			levels[s.Name] = append(levels[s.Name], s.SpellLevel)
		}
	}
	for name, ls := range levels {
		sort.Slice(ls, func(a, b int) bool { return ls[a] < ls[b] })
		levels[name] = ls
	}
	downrankNext = map[int32]int16{}
	downrankTaught = map[int32]int16{}
	for i := range spells {
		s := &spells[i]
		if s.Rank == "" || s.Name == "" {
			continue
		}
		downrankTaught[s.ID] = s.SpellLevel
		for _, l := range levels[s.Name] {
			if l > s.SpellLevel {
				downrankNext[s.ID] = l
				break
			}
		}
	}
}

// DownrankMultiplier is the share of its spell power coefficient a ranked spell keeps at level 60 (1 for the top rank).
func DownrankMultiplier(spellID int32) float64 {
	if downrankOff {
		return 1
	}
	downrankOnce.Do(buildDownrank)
	next, ok := downrankNext[spellID]
	if !ok {
		return 1 // the top rank, or an unranked spell; triggered spells carry odd taught levels (Flametongue Attack's at 1), so
		// Classic's below-20 rule is only applied below a higher rank as well
	}
	m := 1.0
	last := float64(next) - 1
	if last+5 < downrankLevel {
		m *= (last + 6) / downrankLevel
	}
	if taught := downrankTaught[spellID]; taught > 0 && taught < 20 {
		m *= 1 - float64(20-taught)*0.0375
	}
	return m
}
