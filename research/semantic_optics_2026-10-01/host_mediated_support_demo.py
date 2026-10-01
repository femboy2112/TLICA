#!/usr/bin/env python3
"""
Finite witness for host-mediated support without direct interaction.

Category is the diamond poset:
      U
     / \
    A   B
     \ /
      P

A and B are incomparable: no direct A->B or B->A.
Both embed into U. P is a common probe/overlap object.
The slice C/U contains all four objects as arrows into U.
"""
import argparse, json

OBJS=("P","A","B","U")
LEQ={
 ("P","P"),("A","A"),("B","B"),("U","U"),
 ("P","A"),("P","B"),("P","U"),("A","U"),("B","U"),
}
def hom(x,y): return (x,y) in LEQ

def yoneda_signature(target, probes):
    return [1 if hom(p,target) else 0 for p in probes]

checks={
 "no_direct_A_to_B": not hom("A","B"),
 "no_direct_B_to_A": not hom("B","A"),
 "A_supported_by_host_U": hom("A","U"),
 "B_supported_by_host_U": hom("B","U"),
 "common_probe_P_reaches_A_and_B": hom("P","A") and hom("P","B"),
 "pullback_overlap_is_P": all(
     (not (hom(x,"A") and hom(x,"B"))) or hom(x,"P")
     for x in OBJS
 ) and hom("P","A") and hom("P","B"),
 "A_local_downset_excludes_B": "B" not in [x for x in OBJS if hom(x,"A")],
 "host_slice_probe_profiles_are_comparable": (
     yoneda_signature("A",OBJS) != yoneda_signature("B",OBJS)
     and len(yoneda_signature("A",OBJS))==len(yoneda_signature("B",OBJS))
 ),
}

def run():
    return {
      "scope":"finite poset/category witness only",
      "objects":OBJS,
      "order_relations":sorted([list(x) for x in LEQ]),
      "yoneda_profiles":{
        "A":yoneda_signature("A",OBJS),
        "B":yoneda_signature("B",OBJS),
      },
      "A_local_downset":[x for x in OBJS if hom(x,"A")],
      "U_host_downset":[x for x in OBJS if hom(x,"U")],
      "checks":checks,
      "passed":sum(checks.values()),
      "total":len(checks),
      "all_pass":all(checks.values()),
      "verdict":"A and B have no direct morphisms, yet both are supported in U, share a common probe/overlap P, and have comparable host-relative Yoneda profiles. Direct interaction is strictly stronger than common-host comparability."
    }

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--output",default="")
    args=ap.parse_args()
    r=run()
    s=json.dumps(r,indent=2,sort_keys=True)
    if args.output:
        with open(args.output,"w",encoding="utf-8") as f:f.write(s+"\n")
    print(s)
    raise SystemExit(0 if r["all_pass"] else 1)

if __name__=="__main__":main()
