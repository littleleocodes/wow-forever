package mage

// Frostfire Bolt, implemented by the wow-forever project (2026-09-28): the ElliotWood/Forever fork ships this file as a stub
// ("To be implemented", not wired into Initialize). _reference/data/raidsim/setup.py copies this file over the stub and wires
// registerFrostfireBolt into Initialize before every build; see _reference/data/raidsim/patches/README.md.
//
// The spell is read from the client's spell store like every other mage spell (spellData.FrostfireBolt, three ranks: 401502,
// 1237312, 1237313, trained at 40/50/60): cost, cast time, missile speed, the direct damage and its coefficient, the periodic part,
// and the spell school, which the store gives as frostfire (frost and fire at once: the core applies the school mechanics for a
// multi-school spell, e.g. the lower of the two resistances as the tooltip says). ClassSpellMask MageSpellFrostfireBolt is what
// Improved Fireball, Hot Streak and Missile Barrage already test for, so their Forever tooltips ("Fireball and Frostfire Bolt")
// apply as written. Modelled on registerFireballRank (fireball.go): the same build of a missile with a periodic tail. The 40%
// movement slow is not modelled (the training dummy does not move).
import (
	"fmt"

	"github.com/wowsims/forever/sim/core"
	"github.com/wowsims/forever/sim/core/spelldata"
)

// Every rank is registered: a rotation can drop to a cheaper rank when mana runs short.
func (mage *Mage) registerFrostfireBolt() {
	spellData.FrostfireBolt.Each(func(_ int32, rank *spelldata.Spell) { mage.registerFrostfireBoltRank(rank) })
}

func (mage *Mage) registerFrostfireBoltRank(row *spelldata.Spell) {
	tick := row.PeriodicEffect()
	tickLength := tick.Period()

	mage.RegisterSpell(core.SpellConfig{
		ActionID:       core.ActionID{SpellID: row.ID},
		SpellSchool:    row.SpellSchool(),
		DefenseType:    row.DefenseTypeCore(),
		ProcMask:       core.ProcMaskSpellDamage,
		Flags:          core.SpellFlagAPL,
		ClassSpellMask: MageSpellFrostfireBolt,
		Rank:           row.RankNumber(),
		MissileSpeed:   float64(row.Speed),

		ManaCost: core.ManaCostOptions{
			FlatCost: int32(row.Cost()),
		},
		Cast: core.CastConfig{
			DefaultCast: core.Cast{
				GCD:      row.GCD(),
				CastTime: row.CastTime(),
			},
		},

		Dot: core.DotConfig{
			Aura: core.Aura{
				Label: fmt.Sprintf("FrostfireBoltDoT-%d", row.RankNumber()),
			},
			NumberOfTicks:    int32(row.Duration() / tickLength),
			TickLength:       tickLength,
			BonusCoefficient: tick.Coeff(),
			OnSnapshot: func(sim *core.Simulation, target *core.Unit, dot *core.Dot) {
				dot.Snapshot(target, tick.Average(core.CharacterLevel))
			},
			OnTick: func(sim *core.Simulation, target *core.Unit, dot *core.Dot) {
				dot.CalcAndDealPeriodicSnapshotDamage(sim, target, periodicTickOutcome(row, dot))
			},
		},

		DamageMultiplier: 1,
		BonusCoefficient: row.DamageEffect().Coeff(),
		ThreatMultiplier: 1,

		ApplyEffects: func(sim *core.Simulation, target *core.Unit, spell *core.Spell) {
			result := spell.CalcDamage(sim, target, row.DamageEffect().Average(core.CharacterLevel), spell.OutcomeMagicHitAndCrit)
			spell.WaitTravelTime(sim, func(sim *core.Simulation) {
				spell.DealDamage(sim, result)
				if result.Landed() {
					spell.Dot(target).Apply(sim)
				}
			})
		},
	})
}
