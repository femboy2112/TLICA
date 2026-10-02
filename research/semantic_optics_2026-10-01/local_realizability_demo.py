#!/usr/bin/env python3
"""
Finite construction-level witness for scale/locality naturality and local/global
distinctions used in the Semantic Optics nested-host notes.

No empirical inference is licensed.
"""
from itertools import product
import argparse, json, math

VALS=(0,1,2)
RICH_GLOBAL=list(product(VALS,VALS))

def restrict_rich(v): return v[0]
def coarse_global(v): return (v[0]%2,v[1]%2)
def coarse_local(a): return a%2
def restrict_coarse(v): return v[0]
def mutant_coarse_global(v): return ((v[0]+v[1])%2,v[1]%2)

BETA=.6
GAMMA=1/math.sqrt(1-BETA**2)
POINTS=[(0.,0.),(1.,.2),(2.,.4),(3.,.6)]

def lorentz(p):
    t,x=p
    return (GAMMA*(t-BETA*x),GAMMA*(x-BETA*t))

def invlorentz(p):
    t,x=p
    return (GAMMA*(t+BETA*x),GAMMA*(x+BETA*t))

def interval2(p,q):
    dt=q[0]-p[0]; dx=q[1]-p[1]
    return dt*dt-dx*dx

CORR={(0,0):.5,(1,1):.5}
ANTI={(0,1):.5,(1,0):.5}

def marginal(dist,idx):
    out={0:0.,1:0.}
    for state,p in dist.items():
        out[state[idx]]+=p
    return out

CONTEXTS={
    "AB":[(a,b) for a,b in product((0,1),repeat=2) if a!=b],
    "BC":[(b,c) for b,c in product((0,1),repeat=2) if b!=c],
    "CA":[(c,a) for c,a in product((0,1),repeat=2) if c!=a],
}

def run():
    naturality=[
        restrict_coarse(coarse_global(v))==coarse_local(restrict_rich(v))
        for v in RICH_GLOBAL
    ]
    mutant=[
        restrict_coarse(mutant_coarse_global(v))==coarse_local(restrict_rich(v))
        for v in RICH_GLOBAL
    ]
    inverse_ok=all(
        abs(a-b)<1e-12
        for p in POINTS
        for a,b in zip(p,invlorentz(lorentz(p)))
    )
    interval_ok=all(
        abs(interval2(POINTS[i],POINTS[i+1])
            -interval2(lorentz(POINTS[i]),lorentz(POINTS[i+1])))<1e-12
        for i in range(len(POINTS)-1)
    )
    local_same=(
        marginal(CORR,0)==marginal(ANTI,0)
        and marginal(CORR,1)==marginal(ANTI,1)
    )
    global_solutions=[
        (a,b,c)
        for a,b,c in product((0,1),repeat=3)
        if a!=b and b!=c and c!=a
    ]

    checks={
        "scale_locality_square_commutes_all_9_states": all(naturality),
        "non_natural_mutant_is_detected": not all(mutant),
        "lorentz_inverse_recovers_all_worldline_points": inverse_ok,
        "minkowski_interval_preserved_on_all_segments": interval_ok,
        "distinct_global_correlations_have_same_local_marginals": local_same,
        "global_correlation_models_are_distinct": CORR!=ANTI,
        "every_pair_context_has_local_solutions": all(CONTEXTS.values()),
        "odd_cycle_constraints_have_no_global_section": len(global_solutions)==0,
    }
    return {
        "scope":"finite construction-level witness only",
        "checks":checks,
        "passed":sum(checks.values()),
        "total":len(checks),
        "all_pass":all(checks.values()),
        "naturality":{
            "states":[list(v) for v in RICH_GLOBAL],
            "commuting":naturality,
            "mutant_commuting":mutant,
            "mutant_mismatch_count":sum(not x for x in mutant),
        },
        "lorentz":{
            "beta":BETA,
            "gamma":GAMMA,
            "points":[list(p) for p in POINTS],
            "transformed":[list(lorentz(p)) for p in POINTS],
            "segment_intervals":[interval2(POINTS[i],POINTS[i+1]) for i in range(3)],
        },
        "local_global":{
            "correlated_global":{str(k):v for k,v in CORR.items()},
            "anticorrelated_global":{str(k):v for k,v in ANTI.items()},
            "marginal_A":marginal(CORR,0),
            "marginal_B":marginal(CORR,1),
        },
        "contextuality_shape":{
            "contexts":CONTEXTS,
            "global_solutions":global_solutions,
        },
    }

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--output",default="")
    args=parser.parse_args()
    result=run()
    text=json.dumps(result,indent=2,sort_keys=True)
    if args.output:
        with open(args.output,"w",encoding="utf-8") as f:
            f.write(text+"\n")
    print(text)
    raise SystemExit(0 if result["all_pass"] else 1)

if __name__=="__main__":
    main()
