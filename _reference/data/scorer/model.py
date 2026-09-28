"""Convert a set of talent effects into one comparable number for a spec model + usage profile.

Units
  leveling profiles : score = fraction of time-per-kill saved (fight time / downtime / death time model)
  raid profiles     : score = fractional DPS gain (+ a small weight on mana sustain for casters)

The spec model (specs/<class>.json) says where the damage comes from (sources with shares and tags), the base
stats per gear tier, and how mana/resources map to downtime. The profile (profiles.json) says how time is split
and which gear tier / miss chances apply. Nothing here is class-specific code: everything is data.
"""
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent

DEFAULT_CRIT_BONUS = {"type:spell": 0.5, "type:melee": 1.0, "type:ranged": 1.0, "pet": 1.0}

# Soft values (utility, survival, sustain) carry a kind so that each scenario (profile `kind_weights`) and each playstyle
# (spec model `kind_weights`, `kind_weights_by_profile`) can say how much that kind of value counts. Kinds (scorer/kinds.json):
#   kite    roots, slows and knockbacks used to open distance and keep fighting from range
#   stun    stuns, incapacitates, fears, silences, interrupts, disarms: incoming damage or a cast stops for a moment
#   stick   snares that keep a fleeing target in reach (runners, a player running away)
#   move    your own movement: travel speed, gap closers, sprints
#   range   longer spell or shot range
#   stealth stealth level, stealth speed, opener utility
#   avoid   dodge, parry, block and armor talents: they only matter while something hits you in melee
#   resist  shorter stuns, fears and silences on you
SOFT_CHANNELS = ("utility", "surv", "sustain")
KIND_FROM_SCOPE = {"surv:parry": "avoid", "surv:dodge": "avoid", "surv:block": "avoid", "surv:armor": "avoid", "surv:defense": "avoid"}


def load_profiles():
    return json.load(open(HERE / "profiles.json", encoding="utf-8"))


def profile_modes(profile):
    """Tokens an effect's `modes` (and a utility scope's mode:/profile:) may name to apply under this profile: its mode and id, plus
    the mode and id of the profile it takes its effects from (`effects_as`; the PvP profile plays like solo-60 with its own weights)."""
    toks = {profile.get("mode", "leveling"), profile.get("id", "")}
    base = profile.get("effects_as")
    if base:
        bp = load_profiles()[base]
        toks |= {bp.get("mode", "leveling"), base}
    toks.discard("")
    return toks


def load_specs(cls: str):
    return json.load(open(HERE / "specs" / f"{cls}.json", encoding="utf-8"))["models"]


def _type_key(tags):
    for t in tags:
        if t in ("type:melee", "type:ranged", "type:spell", "pet"):
            return t
    return "type:spell"


def _matches(scope, tags, is_pet):
    for s in scope:
        if s == "all" and not is_pet:
            return True
        if s in tags:
            return True
    return False


class Evaluator:
    """Scores effect sets for one (spec model, profile). Build once, call score() many times."""

    def __init__(self, spec: dict, profile: dict, level: int = 60, game: str = "forever", talents=None):
        self.spec = spec
        self.profile = profile
        self.level = level
        self.game = game
        self.talents = set(talents) if talents is not None else None   # this game's talent names (gates `enabled_by`)
        gear = profile.get("gear", "leveling")
        self.base = spec["base"][gear] if gear in spec["base"] else spec["base"]["leveling"]
        self.miss = profile["miss"]
        self.mode = profile.get("mode", "leveling")
        self.modes_ok = profile_modes(profile)
        self.time = spec.get("time", {}).get(profile.get("id", ""), profile.get("time", {"fight": 1.0, "downtime": 0.0, "death": 0.0}))
        # active sources at this level
        self.sources = []
        for s in spec["sources"]:
            if s.get("min_level", 0) > level or s.get("max_level", 99) < level:
                continue
            s = {**s, **(s.get("game_overrides", {}).get(game, {}))}
            po = s.get("profile_overrides", {})
            s = {**s, **(po.get(profile.get("id", "")) or po.get(profile.get("effects_as", ""), {}))}   # PvP takes the solo split (Overpower, Rend)
            tags = list(s["tags"])
            is_pet = "pet" in tags
            if not is_pet:
                tags.append("all")
            # talent-created source: `enabled_by` names the talent(s) that add it (a string, a list, or {game: ...} when the
            # ability is a talent in one game only); a name missing from this game's tree cannot gate it
            eb = s.get("enabled_by")
            if isinstance(eb, dict):
                eb = eb.get(game)
            if isinstance(eb, str):
                eb = [eb]
            eb = [t for t in (eb or []) if self.talents is None or t in self.talents]
            self.sources.append({**s, "tags": tags, "is_pet": is_pet, "type": _type_key(tags), "is_heal": "heal" in tags, "_enabled_by": eb})
        total = sum(s["share"] for s in self.sources) or 1.0
        for s in self.sources:
            s["share"] = s["share"] / total
        self.extra = [(x["channel"], x["scope"], x["value"]) for x in profile.get("extra_effects", []) if not x.get("games") or game in x["games"]]   # profile extras may be game-specific
        self.kind_w = self._kind_weights()
        self.baseline, self.baseline_bound = self._dps(list(self.extra), {}, split=True)

    def _kind_weights(self):
        """Weight of each kind of soft value here: the scenario's (profile `kind_weights`) times the playstyle's (spec model
        `kind_weights`, overridden per profile by `kind_weights_by_profile`). A kind missing from both counts fully."""
        pw = {k: v for k, v in self.profile.get("kind_weights", {}).items() if isinstance(v, (int, float))}
        sw = {k: v for k, v in self.spec.get("kind_weights", {}).items() if isinstance(v, (int, float))}
        sw.update({k: v for k, v in self.spec.get("kind_weights_by_profile", {}).get(self.profile.get("id", ""), {}).items() if isinstance(v, (int, float))})
        return {k: pw.get(k, 1.0) * sw.get(k, 1.0) for k in set(pw) | set(sw)}

    def pet_active(self, effects, allocation=None, name=None):
        """True when a pet source is out with this allocation: some pet source has a share and no `disable` effect
        (Lone Wolf, Demonic Sacrifice) switches it off. `name` asks for one pet (a source tagged `ability:<name>`)."""
        disabled = [scope for ch, scope, v in effects if ch == "disable"]
        enabled = [scope for ch, scope, v in effects if ch == "enable"]
        shares = self._active_shares(allocation or {})
        for src in self.sources:
            if not src["is_pet"] or shares[src["id"]] <= 0.0:
                continue
            if name and f"ability:{name}" not in src["tags"]:
                continue
            if any(_matches(sc, src["tags"], True) for sc in disabled) and not any(_matches(sc, src["tags"], True) for sc in enabled):
                continue
            return True
        return False

    # ---------------------------------------------------------------- damage
    def _active_shares(self, allocation):
        """Effective share per source id: a talent-created source counts only when its talent is allocated (rank-scaled when
        `enabled_ranks` is set, Ignite's burn grows with rank); the inactive part of its share goes to the sources it
        `displaces` (the rage, mana or casts return there) or is lost when nothing is listed."""
        share = {}
        extra = {}
        for src in self.sources:
            f = 1.0
            if src["_enabled_by"]:
                r = max((allocation.get(t, 0) for t in src["_enabled_by"]), default=0) if allocation else 0
                n = src.get("enabled_ranks")
                f = min(r / n, 1.0) if n else (1.0 if r > 0 else 0.0)
            share[src["id"]] = src["share"] * f
            if f < 1.0 and src.get("displaces"):
                lost = src["share"] * (1 - f)
                tot = sum(s2["share"] for s2 in self.sources if s2["id"] in src["displaces"])
                if tot > 0:
                    for s2 in self.sources:
                        if s2["id"] in src["displaces"]:
                            extra[s2["id"]] = extra.get(s2["id"], 0.0) + lost * s2["share"] / tot
        return {k: v + extra.get(k, 0.0) for k, v in share.items()}

    def _dps(self, effects, allocation=None, split=False):
        """The damage model: relative output of the sources. split=True also returns the part that needs mana (every source but
        white attacks and pets), which a mana limit cuts when the budget runs short."""
        total = 0.0
        bound = 0.0
        stat_mult = 1.0
        shares = self._active_shares(allocation or {})
        for ch, scope, v in effects:
            if ch == "stat":
                stat = scope[0].split(":", 1)[1]
                form_ok = True
                for t in scope[1:]:
                    if t.startswith("form:") and t.split(":")[1] != self.spec.get("form"):
                        form_ok = False
                if form_ok:
                    stat_mult *= 1 + v * self.spec.get("stat_to_dps", {}).get(stat, 0.0)
            if ch == "ap_from_int":
                stat_mult *= 1 + v * self.spec.get("int_to_ap_dps", 0.0)
        # "disable" turns matching sources off (a sacrificed pet); "enable" turns them back on (Demonic Pact)
        disabled = [scope for ch, scope, v in effects if ch == "disable"]
        enabled = [scope for ch, scope, v in effects if ch == "enable"]
        for src in self.sources:
            if any(_matches(sc, src["tags"], src["is_pet"]) for sc in disabled) and not any(_matches(sc, src["tags"], src["is_pet"]) for sc in enabled):
                continue
            if shares[src["id"]] <= 0.0:
                continue
            tk = src["type"]
            mult = 1.0
            crit = self.base["crit"].get(tk, 0.0) if (src.get("can_crit", True) or src.get("scales_with_crit")) else 0.0
            cb = src.get("crit_bonus", DEFAULT_CRIT_BONUS.get(tk, 0.5))
            hit = 0.0
            haste = 0.0
            cast_red = 0.0
            cd_red = 0.0
            for ch, scope, v in effects:
                if not _matches(scope, src["tags"], src["is_pet"]):
                    continue
                if ch == "dmg" and not src["is_heal"]:
                    mult *= 1 + v
                elif ch == "heal" and src["is_heal"]:
                    mult *= 1 + v
                elif ch == "threat_up" and "threat" in src["tags"]:
                    mult *= 1 + v
                elif ch == "crit" and src.get("can_crit", True):
                    crit += v
                elif ch == "crit_bonus" and src.get("can_crit", True):
                    cb += v
                elif ch == "hit":
                    hit += v
                elif ch == "haste":
                    haste += v
                elif ch == "cast_time" and src.get("cast"):
                    cast_red += v
                elif ch == "cooldown" and src.get("cooldown"):
                    cd_red += v
                elif ch == "resource_cost" and src.get("cost"):
                    # cheaper ability -> more uses; only ~half of the saved resource turns into extra uses
                    mult *= 1 + 0.5 * (src["cost"] / max(src["cost"] - v, 1) - 1)
            crit = min(crit, 1.0)
            if src.get("scales_with_crit"):   # a burn made of crits (Ignite): its size follows the crit chance of the spells that feed it
                base_crit = self.base["crit"].get(tk, 0.0)
                if base_crit > 0:
                    mult *= crit / base_crit
            miss = max(0.0, self.miss.get(tk, 0.0) + src.get("miss_extra", 0.0) - hit)
            cast_f = 1.0
            if src.get("cast"):
                new_cast = max(src["cast"] - cast_red, src.get("min_cast", 1.5))
                cast_f = src["cast"] / new_cast
            cd_f = 1.0
            if src.get("cooldown") and cd_red:
                cd_f = min(src["cooldown"] / max(src["cooldown"] - cd_red, 1.0), 2.0)
            crit_f = (1 + crit * cb) if src.get("can_crit", True) else 1.0
            part = shares[src["id"]] * mult * (1 - miss) * crit_f * (1 + haste) * cast_f * cd_f
            total += part
            if not src["is_pet"] and "white" not in src["tags"]:
                bound += part
        if split:
            return total * stat_mult, bound * stat_mult
        return total * stat_mult

    def mana_limit(self):
        """The spec model's mana limit in this game and profile (raidsim/calibrate.py fits it to the simulator's training dummy), or
        None: {"loss": the share of the mana-bound damage a build without mana talents loses to mana, "cap": the largest share a
        shortfall can cost (a mage's single Evocation), "profiles": [...]}. Sustain above 1 saves its own amount: the mana talents'
        values are fitted in that unit (the share of the mana-bound damage they save)."""
        ml = (self.spec.get("mana_limit") or {}).get(self.game)
        if ml and self.profile.get("id") in ml.get("profiles", []):
            return ml
        return None

    def mana_lost(self, ml, sus):
        """Share of the mana-bound damage lost to mana: loss - (sustain - 1), between 0 and the cap."""
        return min(ml.get("cap", 1.0), max(0.0, ml["loss"] - ml.get("slope", 1.0) * (sus - 1.0)))

    # ---------------------------------------------------------------- sustain / survival
    def _sustain(self, effects):
        m = 0.0
        mana_share = self.spec.get("mana_share", {})
        for ch, scope, v in effects:
            if ch == "mana_cost":
                share = max([mana_share.get(t, 0.0) for t in scope] + [mana_share.get("all", 0.0) if "all" in scope else 0.0])
                m += v * share
            elif ch == "regen":
                m += v * self.spec.get("regen_share", 0.0)
            elif ch == "sustain":
                m += v
            elif ch == "pet_surv":
                m += v * self.spec.get("pet_surv_to_sustain", 0.0)
            elif ch == "stat":
                stat = scope[0].split(":", 1)[1]
                m += v * self.spec.get("stat_to_sustain", {}).get(stat, 0.0)
        return 1 + m

    def _surv(self, effects):
        m = 0.0
        pet_link = self.spec.get("pet_dmg_to_surv", 0.0)
        for ch, scope, v in effects:
            if ch == "surv":
                m += v
            elif ch == "dmg" and pet_link and any(s == "pet" or s.startswith("ability:") and any(s in src["tags"] for src in self.sources if src["is_pet"]) for s in scope):
                # pet threat: a pet that hits harder keeps the mobs on itself
                m += v * pet_link
            elif ch == "stat":
                stat = scope[0].split(":", 1)[1]
                form_ok = all(not t.startswith("form:") or t.split(":")[1] == self.spec.get("form") for t in scope[1:])
                if form_ok:
                    m += v * self.spec.get("stat_to_surv", {}).get(stat, 0.0)
        return 1 + m

    def _utility(self, effects):
        u = 0.0
        nu = self.profile.get("no_utility")   # a parse profile: personal output only; a list names the games it applies to
        if nu is True or (isinstance(nu, list) and self.game in nu):
            return 0.0
        own = {self.mode, self.profile.get("id", "")}   # utility is scenario-specific: PvP does not inherit solo-60's control utility
        ok = {f"profile:{t}" for t in own} | {f"mode:{t}" for t in own}
        for ch, scope, v in effects:
            if ch == "utility":
                if not scope or "all" in scope or any(s in ok for s in scope):
                    u += v
        return u

    # ---------------------------------------------------------------- score
    def score(self, effects, detail=False, allocation=None):
        sid = self.spec.get("id")
        kept = [e for e in effects
                if (len(e) < 4 or not e[3] or any(m in self.modes_ok for m in e[3]))
                and (len(e) < 5 or not e[4] or sid in e[4])]
        needs = {e[6] for e in kept if len(e) > 6 and e[6]}
        if needs:   # a pet talent does nothing without its pet out (True = any pet, a name = that pet)
            base3 = [e[:3] for e in kept]
            out_ok = {n: self.pet_active(base3, allocation, None if n is True else n) for n in needs}
            kept = [e for e in kept if not (len(e) > 6 and e[6]) or out_ok[e[6]]]
        effects = [(e[0], e[1], e[2] * self.kind_w.get(e[5], 1.0)) if len(e) > 5 and e[5] and e[0] in SOFT_CHANNELS else e[:3] for e in kept]
        effects = effects + list(self.extra)
        ml = self.mana_limit() if self.mode == "raid" else None
        if ml:   # running out of mana is lost damage: the mana-bound part shrinks by the budget's shortfall (talentless build = 1)
            tot, bound = self._dps(effects, allocation, split=True)
            base_eff = max(1e-6, self.baseline - self.baseline_bound * self.mana_lost(ml, self._sustain(list(self.extra))))
            mana_cut = bound * self.mana_lost(ml, self._sustain(effects))
            dps = (tot - mana_cut) / base_eff
        else:
            dps = self._dps(effects, allocation) / self.baseline
            mana_cut = 0.0
        sus = self._sustain(effects)
        surv = self._surv(effects)
        util = self._utility(effects)
        if self.mode == "leveling":
            # fight_coupling (per spec model, per profile): downtime and death time also shrink when fights get shorter
            # (fewer casts -> less mana, fewer hits taken -> less eating and dying). 0 = independent (the old model);
            # the fight lab measures ~0.3-0.5 for a kiting caster.
            fc = self.spec.get("fight_coupling", 0.0)
            if isinstance(fc, dict):
                fc = fc.get(self.profile["id"], 0.0)
            link = dps ** fc if fc else 1.0
            # pet_tank (per spec model, per profile): while the pet is out it takes the hits; without it (Lone Wolf) downtime and death
            # time grow by the factor the fight lab measures between a pet build and its Lone Wolf twin
            pt = self.spec.get("pet_tank", {}).get(self.profile["id"]) if isinstance(self.spec.get("pet_tank"), dict) else None
            down_m = eat_m = death_m = 1.0
            if isinstance(pt, dict) and not self.pet_active(effects, allocation):
                down_m = 1.0 / max(0.05, 1.0 - pt.get("downtime", 0.0))
                eat_m = 1.0 / max(0.05, 1.0 - pt.get("eat", pt.get("downtime", 0.0)))
                death_m = 1.0 / max(0.05, 1.0 - pt.get("death", 0.0))
            tm = self.time
            if "eat" in tm or "drink" in tm:
                # drinking shrinks with mana sustain; eating, self-healing and dying with survival (fewer hits taken, more health);
                # loot and travel ("other") stay fixed (travel speed is utility of kind move)
                t = (tm["fight"] / dps + tm.get("drink", 0.0) / (sus * link) + tm.get("eat", 0.0) * eat_m / (surv * link)
                     + tm.get("other", 0.0) + tm.get("death", 0.0) * death_m / (surv * link))
            else:   # the older fight / downtime / death split: all downtime shrinks with sustain
                t = tm["fight"] / dps + tm["downtime"] * down_m / (sus * link) + tm["death"] * death_m / (surv * link)
            s = (1 - t) + util
        elif self.mode == "heal":
            # dps here is healing throughput (heal sources); mana is usually the binding constraint in long fights
            s = self.profile.get("hps_weight", 0.6) * (dps - 1) + self.profile.get("mana_weight", 0.5) * (sus - 1) + self.profile.get("surv_weight", 0.0) * (surv - 1) + util
        elif self.mode == "pvp":
            # PvP: burst (the damage or healing model), survival and mana with the profile's weights; control, escape and stealth arrive
            # through the utility term, already scaled by the profile's (high) kind weights
            w = self.profile.get("pvp_weights", {})
            s = w.get("burst", 0.5) * (dps - 1) + w.get("surv", 0.5) * (surv - 1) + w.get("mana", 0.1) * (sus - 1) + w.get("utility", 1.0) * util
        elif self.mode == "tank":
            # dps here is threat output on tank sources
            mw = self.spec.get("mana_weight", {}).get(self.profile["id"], self.profile.get("mana_weight", 0.1)) if isinstance(self.spec.get("mana_weight"), dict) else self.profile.get("mana_weight", 0.1)
            s = self.profile.get("threat_weight", 0.5) * (dps - 1) + self.profile.get("mit_weight", 0.5) * (surv - 1) + mw * (sus - 1) + util
        else:
            # a spec model may override the profile's mana weight (a hunter or elemental shaman is mana-bound in long fights)
            mw = self.spec.get("mana_weight", {}).get(self.profile["id"], self.profile.get("mana_weight", 0.0)) if isinstance(self.spec.get("mana_weight"), dict) else self.profile.get("mana_weight", 0.0)
            if ml:   # mana counts through the limit above, not as a separate term
                mw = 0.0
            s = (dps - 1) + mw * (sus - 1) + self.profile.get("surv_weight", 0.0) * (surv - 1) + util
        if detail:
            tot_b, bound_b = self._dps(effects, allocation, split=True)
            return {"score": s, "dps": dps, "sustain": sus, "surv": surv, "utility": util, "mana_cut": mana_cut / self.baseline if ml else 0.0,
                    "bound_frac": bound_b / tot_b if tot_b else 0.0}
        return s


def effects_for(allocation, merged_effects, spec_id=None, mode=None, profile_id=None):
    """allocation {talent: rank} + merged effects -> flat list of (channel, scope, value). A talent whose fitted (manual) effects
    are tagged for other spec models only falls back to its parsed tooltip numbers for this model: a new model starts from
    the tooltips instead of from nothing."""
    out = []
    for name, rank in allocation.items():
        if rank <= 0 or name not in merged_effects:
            continue
        entry = merged_effects[name]
        effs = entry["effects"]
        kinds = entry.get("kinds") or {}   # talent-level kinds by channel (scorer/kinds.json)
        needs_pet = entry.get("needs_pet") or False   # True (any pet) or the pet's name
        if spec_id is not None and effs and entry.get("parsed"):
            toks = set(mode) if isinstance(mode, (set, frozenset, list, tuple)) else {mode, profile_id}   # a profile's mode tokens (profile_modes) or mode + id

            def mode_ok(e):
                m = e.get("modes")
                return not m or any(t in m for t in toks)
            if any(mode_ok(e) for e in effs) and not any(mode_ok(e) and (not e.get("specs") or spec_id in e["specs"]) for e in effs):
                effs = entry["parsed"]
        for e in effs:
            req = e.get("requires") or {}
            if any(allocation.get(t, 0) < r for t, r in req.items()):
                continue
            # requires_not: the effect is lost when a conflicting talent is taken (e.g. a pet buff vs Demonic Sacrifice)
            if any(allocation.get(t, 0) >= r for t, r in (e.get("requires_not") or {}).items()):
                continue
            vals = e["values"]
            v = vals[min(rank, len(vals)) - 1] if vals else 0.0
            if v:
                kind = e.get("kind") or kinds.get(e["channel"]) or (KIND_FROM_SCOPE.get(e["scope"][0]) if e["scope"] else None)
                out.append((e["channel"], e["scope"], v, e.get("modes"), e.get("specs"), kind, needs_pet))
    return out
