#!/usr/bin/env python3
"""
Finite context-atlas witness.

Three context categories are finite chains:
  C0 = {0<1}
  C1 = {0<1<2}
  C2 = {0<1<2<3}

Forward context transports are order embeddings:
  F01: C0 -> C1, 0|->0, 1|->2
  F12: C1 -> C2, 0|->0, 1|->1, 2|->3
  F02 = F12 o F01

Each has the canonical right adjoint (floor projection):
  G10, G21, G20.

The script checks:
- forward and backward composition;
- every adjunction hom-bijection cell;
- unit/counit behavior;
- triangle identities;
- full/faithful vs essential-surjectivity classification;
- Yoneda comparison on every forward embedding;
- lossy downward transport failing fullness;
- composite adjunction coherence.

Construction-level only.
"""
import argparse, json
from itertools import product

C0=(0,1)
C1=(0,1,2)
C2=(0,1,2,3)

def leq(a,b): return a<=b

def F01(x): return {0:0,1:2}[x]
def G10(y): return 0 if y<2 else 1

def F12(x): return {0:0,1:1,2:3}[x]
def G21(y): return {0:0,1:1,2:1,3:2}[y]

def F02(x): return F12(F01(x))
def G20(y): return G10(G21(y))

def adjunction_cells(C,D,F,G):
    cells=[]
    ok=True
    for c,d in product(C,D):
        left=leq(F(c),d)
        right=leq(c,G(d))
        same=(left==right)
        cells.append({"c":c,"d":d,"left":left,"right":right,"ok":same})
        ok &= same
    return ok,cells

def full_faithful(C,D,F):
    return all(leq(a,b)==leq(F(a),F(b)) for a,b in product(C,C))

def essentially_surjective(C,D,F):
    # In a poset, isomorphism is equality.
    return all(any(F(c)==d for c in C) for d in D)

def unit_iso(C,F,G):
    return all(G(F(c))==c for c in C)

def counit_iso(D,F,G):
    return all(F(G(d))==d for d in D)

def triangle_left(C,F,G):
    # epsilon_{F c} o F eta_c = id; in posets existence/equality reduces
    # to both endpoints being the same after unit is equality.
    return all(F(G(F(c)))==F(c) for c in C)

def triangle_right(D,F,G):
    # G epsilon_d o eta_{G d} = id
    return all(G(F(G(d)))==G(d) for d in D)

def yoneda_comparison_iso(C,F):
    # pointwise hom comparison on all probe/target pairs in C
    return all(leq(p,x)==leq(F(p),F(x)) for p,x in product(C,C))

def functor_full(C,D,F):
    # posets: check every target hom between image endpoints lifts
    for a,b in product(C,C):
        if leq(F(a),F(b)) and not leq(a,b):
            return False
    return True

def functor_faithful(C,D,F):
    # any functor out of a poset is faithful because hom-sets have <=1 element
    return True

ok01,cells01=adjunction_cells(C0,C1,F01,G10)
ok12,cells12=adjunction_cells(C1,C2,F12,G21)
ok02,cells02=adjunction_cells(C0,C2,F02,G20)

checks={
  "forward_composition_F02_equals_F12_after_F01": all(F02(x)==F12(F01(x)) for x in C0),
  "backward_composition_G20_equals_G10_after_G21": all(G20(x)==G10(G21(x)) for x in C2),
  "adjunction_F01_G10_all_6_cells": ok01 and len(cells01)==6,
  "adjunction_F12_G21_all_12_cells": ok12 and len(cells12)==12,
  "adjunction_F02_G20_all_8_cells": ok02 and len(cells02)==8,
  "all_forward_units_are_iso": unit_iso(C0,F01,G10) and unit_iso(C1,F12,G21) and unit_iso(C0,F02,G20),
  "forward_counits_detect_target_coverage_defect": (not counit_iso(C1,F01,G10)) and (not counit_iso(C2,F12,G21)) and (not counit_iso(C2,F02,G20)),
  "triangle_identities_F01_G10": triangle_left(C0,F01,G10) and triangle_right(C1,F01,G10),
  "triangle_identities_F12_G21": triangle_left(C1,F12,G21) and triangle_right(C2,F12,G21),
  "triangle_identities_F02_G20": triangle_left(C0,F02,G20) and triangle_right(C2,F02,G20),
  "all_forward_transports_full_faithful": full_faithful(C0,C1,F01) and full_faithful(C1,C2,F12) and full_faithful(C0,C2,F02),
  "all_forward_yoneda_comparisons_iso": yoneda_comparison_iso(C0,F01) and yoneda_comparison_iso(C1,F12) and yoneda_comparison_iso(C0,F02),
  "forward_transports_not_essentially_surjective": (not essentially_surjective(C0,C1,F01)) and (not essentially_surjective(C1,C2,F12)) and (not essentially_surjective(C0,C2,F02)),
  "downward_G10_is_faithful_but_not_full": functor_faithful(C1,C0,G10) and (not functor_full(C1,C0,G10)),
  "downward_G21_is_faithful_but_not_full": functor_faithful(C2,C1,G21) and (not functor_full(C2,C1,G21)),
  "downward_G20_is_faithful_but_not_full": functor_faithful(C2,C0,G20) and (not functor_full(C2,C0,G20)),
}

def run():
    return {
      "scope":"finite poset context atlas; construction-level only",
      "contexts":{"C0":C0,"C1":C1,"C2":C2},
      "forward_maps":{
        "F01":{str(x):F01(x) for x in C0},
        "F12":{str(x):F12(x) for x in C1},
        "F02":{str(x):F02(x) for x in C0},
      },
      "backward_maps":{
        "G10":{str(x):G10(x) for x in C1},
        "G21":{str(x):G21(x) for x in C2},
        "G20":{str(x):G20(x) for x in C2},
      },
      "adjunction_cells":{"01":cells01,"12":cells12,"02":cells02},
      "checks":checks,
      "passed":sum(checks.values()),
      "total":len(checks),
      "all_pass":all(checks.values()),
      "verdict":"The forward context transports form a compositional chain of full-faithful left adjoints with zero Yoneda hom-defect but nonzero target coverage defect. Their right adjoints provide lawful lossy return maps and compose contravariantly. This is a finite context-atlas witness for adjoint transport without context equivalence."
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
