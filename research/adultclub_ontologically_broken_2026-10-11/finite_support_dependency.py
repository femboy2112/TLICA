#!/usr/bin/env python3
"""Finite counterexample: premise dependence is not mere graph degree.

Construction-level truth-maintenance toy; not a model of actual cognition.
"""
from __future__ import annotations
import json

PREMISES = {
    'rule_legitimacy_bridge', 'past_cost', 'peer_norm',
    'domain_expertise', 'independent_reason', 'rent_fact', 'dress_rule',
}
# A claim is supported if any listed sufficient set is entirely present.
SUPPORTS = {
    'deference_defines_maturity': [{'rule_legitimacy_bridge'}],
    'past_suffering_was_necessary': [{'rule_legitimacy_bridge', 'past_cost'}],
    'questioning_is_irresponsible': [{'rule_legitimacy_bridge', 'peer_norm'}],
    'accountant_is_credible': [{'rule_legitimacy_bridge'}, {'domain_expertise'}],
    'a_rule_might_be_justified': [{'rule_legitimacy_bridge'}, {'independent_reason'}],
    'rent_is_due': [{'rent_fact'}],
    'dress_rule_applies': [{'dress_rule'}],
}
SELF_RELATED = {
    'deference_defines_maturity', 'past_suffering_was_necessary',
    'questioning_is_irresponsible', 'a_rule_might_be_justified',
}

def warranted(claim: str, available: set[str]) -> bool:
    return any(derivation <= available for derivation in SUPPORTS[claim])

def lost_when_removed(premise: str, available: set[str] | None = None) -> set[str]:
    available = set(PREMISES if available is None else available)
    prior = {name for name in SUPPORTS if warranted(name, available)}
    after = {name for name in SUPPORTS if warranted(name, available - {premise})}
    return prior - after

def run() -> dict[str, object]:
    checks: dict[str, bool] = {}
    def check(label: str, ok: bool) -> None:
        checks[label] = bool(ok)
        assert ok, label
    core = lost_when_removed('rule_legitimacy_bridge')
    peripheral = lost_when_removed('dress_rule')
    check('all_seven_claims_initially_supported', all(warranted(c, PREMISES) for c in SUPPORTS))
    check('three_claims_depend_without_alt', core == {
        'deference_defines_maturity', 'past_suffering_was_necessary', 'questioning_is_irresponsible'
    })
    check('peripheral_removal_only_one', peripheral == {'dress_rule_applies'})
    check('backup_expertise_protects_claim', 'accountant_is_credible' not in core)
    check('backup_reason_protects_claim', 'a_rule_might_be_justified' not in core)
    check('breadth_not_simple_edge_degree',
          sum(any('rule_legitimacy_bridge' in s for s in options)
              for options in SUPPORTS.values()) == 5 and len(core) == 3)
    check('backup_source_removal_alone_no_loss',
          not lost_when_removed('domain_expertise') and
          not lost_when_removed('independent_reason'))
    reduced = PREMISES - {'domain_expertise', 'independent_reason'}
    check('removing_independent_support_increases_burden',
          len(lost_when_removed('rule_legitimacy_bridge', reduced)) == 5)
    check('nondependent_rent_preserved', 'rent_is_due' not in core and
          'rent_is_due' not in peripheral)
    check('core_subset_of_self_related_in_this_constructed_case', core <= SELF_RELATED)
    return {
       'verdict': 'PASS', 'checks': len(checks),
       'root_lost': sorted(core),
       'peripheral_lost': sorted(peripheral),
       'lost_without_backups': sorted(lost_when_removed('rule_legitimacy_bridge', reduced)),
       'check_names': list(checks),
       'scope': 'chosen finite support sets, not human cognition',
    }

if __name__ == '__main__':
    print(json.dumps(run(), indent=2, sort_keys=True))
