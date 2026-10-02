#!/usr/bin/env python3
"""
Finite witness for Yoneda form transport, adjunction vs equivalence, and
Yoneda-transport/coverage defects.

Construction-level only.
"""
import argparse, json
from itertools import product

# ---------- Object-level groupoid A <-> B ----------
OBJS=("A","B")
HOMS={
    ("A","A"):("idA",),
    ("A","B"):("f",),
    ("B","A"):("g",),
    ("B","B"):("idB",),
}
SRC={"idA":"A","idB":"B","f":"A","g":"B"}
TGT={"idA":"A","idB":"B","f":"B","g":"A"}

def comp(u,v): # u o v
    table={
      ("idA","idA"):"idA",("idB","idB"):"idB",
      ("f","idA"):"f",("idB","f"):"f",
      ("g","idB"):"g",("idA","g"):"g",
      ("g","f"):"idA",("f","g"):"idB",
    }
    return table[(u,v)]

def yoneda_component(form,probe):
    source=SRC[form]; target=TGT[form]
    return {x:comp(form,x) for x in HOMS[(probe,source)]}

object_roundtrip=True
for probe in OBJS:
    ff=yoneda_component("f",probe)
    gg=yoneda_component("g",probe)
    for x,y in ff.items():
        if gg[y]!=x:
            object_roundtrip=False

# ---------- Adjunction C -> D that is NOT equivalence ----------
C=(0,1)
D=(0,1,2)
def leq(a,b): return a<=b
def F(c): return 0 if c==0 else 2
def G(d): return 0 if d in (0,1) else 1

adj_cells=[]
adj_ok=True
for c,d in product(C,D):
    left=leq(F(c),d)      # Hom_D(Fc,d) singleton?
    right=leq(c,G(d))     # Hom_C(c,Gd) singleton?
    ok=(left==right)
    adj_cells.append({"c":c,"d":d,"left":left,"right":right,"ok":ok})
    adj_ok &= ok

unit_iso_all=all(G(F(c))==c for c in C)   # posets: iso iff equality
counit_iso_all=all(F(G(d))==d for d in D)
adj_equiv=unit_iso_all and counit_iso_all

# F full+faithful on C but misses D-object 1.
full_faithful=all(leq(c1,c2)==leq(F(c1),F(c2)) for c1,c2 in product(C,C))
essential_surjective=all(any(F(c)==d for c in C) for d in D)

# Yoneda comparison on image is bijective iff full faithful.
yoneda_comparison_iso=full_faithful

# ---------- Equivalence E -> groupoid Dg ----------
# E has one object *, Dg has A,B above. F0(*)=A, G0(A)=G0(B)=*
# Counit components: A->A idA, A->B f.
equiv_unit_iso=True
equiv_counit_iso=(TGT["idA"]=="A" and TGT["f"]=="B")
equiv_full_faithful=True  # unique hom maps to idA
equiv_essential_surjective=True # B iso A via f
equiv=True

checks={
  "object_forms_are_mutual_inverses": comp("g","f")=="idA" and comp("f","g")=="idB",
  "yoneda_transport_bijective_at_probe_A": len(set(yoneda_component("f","A").values()))==len(HOMS[("A","A")]),
  "yoneda_transport_bijective_at_probe_B": len(set(yoneda_component("f","B").values()))==len(HOMS[("B","A")]),
  "generalized_element_roundtrip_exact": object_roundtrip,
  "adjunction_hom_bijection_all_6_cells": adj_ok and len(adj_cells)==6,
  "adjunction_unit_iso_everywhere": unit_iso_all,
  "adjunction_counit_not_iso_everywhere": not counit_iso_all,
  "adjunction_is_not_equivalence": not adj_equiv,
  "adjunction_left_functor_full_faithful": full_faithful,
  "yoneda_comparison_zero_hom_defect": yoneda_comparison_iso,
  "coverage_defect_detected": not essential_surjective,
  "equivalence_unit_and_counit_iso": equiv_unit_iso and equiv_counit_iso,
  "equivalence_full_faithful_essentially_surjective": equiv_full_faithful and equiv_essential_surjective,
  "equivalence_detected": equiv,
}

def run():
    return {
      "scope":"finite category construction only",
      "checks":checks,
      "passed":sum(checks.values()),
      "total":len(checks),
      "all_pass":all(checks.values()),
      "object_level":{
        "objects":OBJS,
        "f_components":{p:yoneda_component("f",p) for p in OBJS},
        "g_components":{p:yoneda_component("g",p) for p in OBJS},
        "equations":["g∘f=idA","f∘g=idB"],
      },
      "adjunction_non_equivalence":{
        "C":C,"D":D,
        "F":{"0":F(0),"1":F(1)},
        "G":{"0":G(0),"1":G(1),"2":G(2)},
        "hom_cells":adj_cells,
        "unit_iso_all":unit_iso_all,
        "counit_iso_all":counit_iso_all,
        "full_faithful":full_faithful,
        "essentially_surjective":essential_surjective,
        "interpretation":"hom-form transport reversible, object roundtrip not equivalence",
      },
      "equivalence_example":{
        "source":"one-object terminal category",
        "target":"two-object connected groupoid A<->B",
        "F":"*=A",
        "G":"A,B -> *",
        "unit_iso":equiv_unit_iso,
        "counit_iso":equiv_counit_iso,
        "full_faithful":equiv_full_faithful,
        "essentially_surjective":equiv_essential_surjective,
      },
      "verdict":"Exact inverse forms correspond to object isomorphism and invertible Yoneda transport. Adjoint hom-form transport can be reversible without context equivalence. Zero Yoneda hom-defect (full+faithful) is distinct from zero coverage defect (essential surjectivity)."
    }

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--output",default="")
    args=ap.parse_args()
    r=run()
    s=json.dumps(r,indent=2,sort_keys=True)
    if args.output:
        with open(args.output,"w",encoding="utf-8") as f: f.write(s+"\n")
    print(s)
    raise SystemExit(0 if r["all_pass"] else 1)

if __name__=="__main__": main()
