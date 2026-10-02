#!/usr/bin/env python3
"""Finite witness for self-similar copy transport, orbit entanglement, projective
phase cocycles, and shift-basis distinctions.

Construction-level only; no fundamental-physics inference.
"""
from itertools import product
import argparse, json, math

W=[()]
for n in (1,2):
    W += list(product((0,1),repeat=n))
COPIES=(0,1,2)

def flip(w): return tuple(1-x for x in w)
def gact(g,w): return w if g==0 else flip(w)
def pref(i,w): return (i,)+tuple(w)
def strip(i,x):
    if x[0]!=i: raise ValueError("wrong copy")
    return x[1:]
def T(b,a,g,x): return pref(b,gact(g,strip(a,x)))

def add1(w):
    w=list(w); carry=1
    for i in range(len(w)):
        if carry:
            if w[i]==0: w[i]=1; carry=0
            else: w[i]=0
    return tuple(w)
def rec_add(w):
    if not w:return ()
    return ((1,)+w[1:]) if w[0]==0 else ((0,)+rec_add(w[1:]))
def orbit_zero(n):
    x=(0,)*n; seen=[]
    for _ in range(2**n):
        seen.append(x); x=add1(x)
    return seen,x

def inner(v,w):
    return sum(complex(a).conjugate()*b for a,b in zip(v,w))
def reduced_control_purity(branches,alphas):
    n=len(branches)
    rho=[[alphas[i]*complex(alphas[j]).conjugate()*inner(branches[j],branches[i])
          for j in range(n)] for i in range(n)]
    return sum(abs(rho[i][j])**2 for i in range(n) for j in range(n))

I=((1+0j,0j),(0j,1+0j))
X=((0j,1+0j),(1+0j,0j))
Z=((1+0j,0j),(0j,-1+0j))
def mm(A,B):
    return tuple(tuple(sum(A[i][k]*B[k][j] for k in range(2))
                       for j in range(2)) for i in range(2))
def smul(s,A): return tuple(tuple(s*x for x in row) for row in A)
def mpow(A,n): return I if n%2==0 else A
def U(g): return mm(mpow(X,g[0]),mpow(Z,g[1]))
def gadd(g,h): return ((g[0]+h[0])%2,(g[1]+h[1])%2)
def omega(g,h): return -1 if (g[1]*h[0])%2 else 1
def meq(A,B,eps=1e-12):
    return all(abs(A[i][j]-B[i][j])<eps for i in range(2) for j in range(2))
GS=list(product((0,1),repeat=2))

sqrt2=math.sqrt(2)
bell_purity=reduced_control_purity([(1,0),(0,1)],[1/sqrt2,1/sqrt2])
sep_purity=reduced_control_purity([(1,0),(1,0)],[1/sqrt2,1/sqrt2])

checks={
 "prefix_copy_roundtrip":
    all(strip(i,pref(i,w))==w for i in COPIES for w in W),
 "copy_groupoid_inverse":
    all(T(a,b,g,T(b,a,g,pref(a,w)))==pref(a,w)
        for a,b,g,w in product(COPIES,COPIES,(0,1),W)),
 "copy_groupoid_composition":
    all(T(c,b,h,T(b,a,g,pref(a,w)))==T(c,a,h^g,pref(a,w))
        for a,b,c,g,h,w in product(COPIES,COPIES,COPIES,(0,1),(0,1),W)),
 "internal_morphology_forms_are_distinct":
    all(T(b,a,0,pref(a,(0,)))!=T(b,a,1,pref(a,(0,)))
        for a,b in product(COPIES,COPIES)),
 "binary_adding_machine_wreath_recursion":
    all(add1(w)==rec_add(w)
        for n in range(1,6) for w in product((0,1),repeat=n)),
 "binary_adding_machine_cycles_every_level":
    all(len(set(orbit_zero(n)[0]))==2**n and orbit_zero(n)[1]==(0,)*n
        for n in range(1,6)),
 "orbit_copy_state_has_bell_purity_half":
    abs(bell_purity-.5)<1e-12,
 "collinear_orbit_branches_are_separable":
    abs(sep_purity-1)<1e-12,
 "pauli_forms_are_projective_representation":
    all(meq(mm(U(g),U(h)),smul(omega(g,h),U(gadd(g,h))))
        for g,h in product(GS,GS)),
 "pauli_phase_satisfies_2_cocycle":
    all(omega(g,h)*omega(gadd(g,h),k)==omega(h,k)*omega(g,gadd(h,k))
        for g,h,k in product(GS,GS,GS)),
 "positive_shift_on_N_not_surjective":
    all(n not in {m+3 for m in range(20)} for n in range(3)),
 "bilateral_shift_on_Z_has_inverse":
    all((z+3)-3==z for z in range(-20,21)),
}

def run():
    return {
      "scope":"finite construction-level quantum-copy witness only",
      "checks":checks,
      "passed":sum(checks.values()),
      "total":len(checks),
      "all_pass":all(checks.values()),
      "copy_model":{
        "copies":COPIES,
        "base_words":[list(w) for w in W],
        "internal_group":"C2 bit-flip",
        "hom_interpretation":"Hom(copy_a,copy_b) ~= C2"
      },
      "self_similar":{
        "model":"binary adding machine, little-endian rooted-tree recursion",
        "levels_checked":[1,2,3,4,5]
      },
      "quantum":{
        "bell_orbit_reduced_purity":bell_purity,
        "collinear_orbit_reduced_purity":sep_purity,
        "projective_group":"Z2 x Z2",
        "cocycle":"omega((a,b),(c,d))=(-1)^(b*c)"
      },
      "verdict":"Exact copy-groupoid composition, recursive self-similar action, orbit-state entanglement, and projective phase transport coexist coherently in one finite witness. This establishes compatibility only, not a fundamental quantum mechanism."
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
