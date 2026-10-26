package core

// wow-forever patch (2026-10-26 audit): a rotation condition on an aura, a dot or a spell the character does not have (a talent the
// build lacks) reads as absent: aura active / dot active / spell ready / can cast false, aura inactive true, stacks 0, remaining time 0.
// Upstream returns nil for such a value, and an action whose condition is nil casts always (apl_action.go: "Condition could not be
// resolved and will be treated as always true"): the shaman 15/24/12 without Maelstrom Weapon cast Lightning Bolt every GCD in the
// Enhancement rotation (437 DPS in a full raid). WOW_FOREVER_UNKNOWN_AURA_DROP=1 restores upstream's behaviour. Variable references
// the rotation does not define are still dropped (raidsim/apl_prune.py relies on that).

import (
	"os"

	"github.com/wowsims/forever/sim/core/proto"
)

var foreverUnknownAuraDrop = os.Getenv("WOW_FOREVER_UNKNOWN_AURA_DROP") == "1"

// foreverAbsent is the constant an absent aura, dot or spell reads as; nil (upstream's drop) when the patch is switched off.
func (rot *APLRotation) foreverAbsent(val string) APLValue {
	if foreverUnknownAuraDrop {
		return nil
	}
	return rot.newValueConst(&proto.APLValueConst{Val: val}, nil)
}
