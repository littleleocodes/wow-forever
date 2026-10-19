package hunter

// wow-forever patch (2026-09-29): Aspect of the Beast and the melee half of Deadly Aspects. The fork models only Aspect of the Hawk
// (aspects.go: "Nothing a ranged hunter does would pick Beast"), so a melee hunter had no aspect and Deadly Aspects, whose client
// tooltip covers both aspects, could never proc for it. Beta 1.60.1.70009 tooltips: Aspect of the Beast rank 4 "increasing Melee
// Attack Power by 110"; Deadly Aspects "While Aspect of the Beast is active, all melee auto attacks have a 2/4/6/8/10% chance of
// increasing melee attack speed by 30% for 12 sec". Values come from the client rows where the generator carries them, else from
// those tooltips.

import (
	"time"

	"github.com/wowsims/forever/sim/core"
	"github.com/wowsims/forever/sim/core/dbcenums"
	"github.com/wowsims/forever/sim/core/stats"
)

func (hunter *Hunter) registerAspectOfTheBeastSpell() {
	beastRank := spellData.AspectOfTheBeast.Highest()
	actionID := core.ActionID{SpellID: beastRank.ID}

	ap := 110.0
	if e := beastRank.FirstAura(dbcenums.A_MOD_ATTACK_POWER); e != nil && e.Aura != 0 {
		if v := e.Average(core.CharacterLevel); v > 0 {
			ap = v
		}
	}

	// Deadly Aspects, melee half: its own triggered spell (1299448), +30% melee attack speed for 12 sec.
	var beastHaste *core.Aura
	if hunter.Talents.DeadlyAspects > 0 {
		trig := spellData.AspectOfTheBeastTriggered.Highest()
		haste, dur := 1.30, 12*time.Second
		if e := trig.FirstAura(dbcenums.A_MOD_MELEE_HASTE, dbcenums.A_MOD_MELEE_RANGED_HASTE, dbcenums.A_MOD_MELEE_HASTE_2, dbcenums.A_MOD_MELEE_HASTE_3); e != nil && e.Aura != 0 {
			if v := e.Average(core.CharacterLevel); v > 0 {
				haste = 1 + v/100
			}
		}
		if d := trig.Duration(); d > 0 {
			dur = d
		}
		beastHaste = hunter.GetOrRegisterAura(core.Aura{
			Label:    "Deadly Aspects (Beast)",
			ActionID: core.ActionID{SpellID: trig.ID},
			Duration: dur,
			OnGain: func(aura *core.Aura, sim *core.Simulation) {
				aura.Unit.MultiplyMeleeSpeed(sim, haste)
			},
			OnExpire: func(aura *core.Aura, sim *core.Simulation) {
				aura.Unit.MultiplyMeleeSpeed(sim, 1/haste)
			},
		})
	}
	procChance := spellData.DeadlyAspects.EffectAt(1).FractionAt(hunter.Talents.DeadlyAspects)

	beastAura := hunter.GetOrRegisterAura(core.Aura{
		Label:      "Aspect of the Beast",
		ActionID:   actionID,
		Duration:   core.NeverExpires,
		BuildPhase: core.CharacterBuildPhaseNone,
		OnGain: func(aura *core.Aura, sim *core.Simulation) {
			aura.Unit.AddStatDynamic(sim, stats.AttackPower, ap)
		},
		OnExpire: func(aura *core.Aura, sim *core.Simulation) {
			aura.Unit.AddStatDynamic(sim, stats.AttackPower, -ap)
		},
		OnSpellHitDealt: func(aura *core.Aura, sim *core.Simulation, spell *core.Spell, result *core.SpellResult) {
			if beastHaste == nil || !spell.ProcMask.Matches(core.ProcMaskMeleeWhiteHit) || !result.Landed() {
				return
			}
			if sim.Proc(procChance, "Deadly Aspects (Beast)") {
				beastHaste.Activate(sim)
			}
		},
	})
	// one aspect at a time: the same exclusive category as Aspect of the Hawk
	beastAura.NewExclusiveEffect("Aspect", true, core.ExclusiveEffect{})

	hunter.RegisterSpell(core.SpellConfig{
		ActionID:    actionID,
		SpellSchool: beastRank.SpellSchool(),
		DefenseType: beastRank.DefenseTypeCore(),
		ProcMask:    core.ProcMaskEmpty,
		Flags:       core.SpellFlagAPL,
		ManaCost:    core.ManaCostOptions{FlatCost: int32(beastRank.Cost())},
		Cast: core.CastConfig{
			DefaultCast: core.Cast{GCD: beastRank.GCD()},
			IgnoreHaste: true,
		},
		ExtraCastCondition: func(sim *core.Simulation, target *core.Unit) bool {
			return !beastAura.IsActive()
		},
		ApplyEffects: func(sim *core.Simulation, _ *core.Unit, _ *core.Spell) {
			beastAura.Activate(sim)
		},
		RelatedSelfBuff: beastAura,
	})
}
