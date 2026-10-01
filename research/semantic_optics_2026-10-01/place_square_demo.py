#!/usr/bin/env python3
"""Finite/archimedean place benchmark for the Semantic Optics arithmetic square.

Checks only standard identities / numerical approximations.
No RH or TLICA inference is licensed.
"""
from fractions import Fraction
import argparse, json, math

SAMPLES=[
    Fraction(2,3),
    Fraction(12,35),
    Fraction(-81,50),
    Fraction(1,210),
    Fraction(1001,64),
]

def factor_int(n):
    n=abs(n); out={}; p=2
    while p*p<=n:
        while n%p==0:
            out[p]=out.get(p,0)+1
            n//=p
        p=3 if p==2 else p+2
    if n>1: out[n]=out.get(n,0)+1
    return out

def vp_int(n,p):
    n=abs(n); c=0
    while n and n%p==0:
        c+=1; n//=p
    return c

def padic_norm(x,p):
    v=vp_int(x.numerator,p)-vp_int(x.denominator,p)
    return Fraction(1,p**v) if v>=0 else Fraction(p**(-v),1)

def primes_upto(n):
    sieve=[True]*(n+1)
    sieve[0]=sieve[1]=False
    for i in range(2,int(n**0.5)+1):
        if sieve[i]:
            for j in range(i*i,n+1,i):
                sieve[j]=False
    return [i for i,b in enumerate(sieve) if b]

def completed_zeta_special(s):
    values={
        2: math.pi**2/6,
        -1: -1/12,
        4: math.pi**4/90,
        -3: 1/120,
    }
    return math.pi**(-s/2)*math.gamma(s/2)*values[s]

def run():
    place_rows=[]
    for x in SAMPLES:
        support=sorted(set(factor_int(x.numerator))|set(factor_int(x.denominator)))
        finite=Fraction(1,1)
        norms={}
        for p in support:
            n=padic_norm(x,p)
            norms[str(p)]=str(n)
            finite*=n
        place_rows.append({
            "x":str(x),
            "finite_support":support,
            "finite_norms":norms,
            "archimedean_norm":str(abs(x)),
            "finite_product":str(finite),
            "all_places_product":str(abs(x)*finite),
        })

    target=math.pi**2/6
    euler=[]
    for bound in (10,100,1000,10000):
        prod=1.0
        for p in primes_upto(bound):
            prod /= (1-p**-2)
        euler.append({
            "bound":bound,
            "product":prod,
            "error_to_zeta2":abs(prod-target),
        })

    scaling_samples=[
        (2,3,Fraction(5,4)),
        (5,7,Fraction(1,5)),
        (11,13,Fraction(2,1)),
    ]

    checks={
        "product_formula_all_samples":
            all(row["all_places_product"]=="1" for row in place_rows),
        "finite_norm_is_arch_inverse_all_samples":
            all(Fraction(row["finite_product"])==1/Fraction(row["archimedean_norm"])
                for row in place_rows),
        "finite_place_support_is_finite_all_samples":
            all(len(row["finite_support"])<=4 for row in place_rows),
        "euler_products_monotone_at_s2":
            all(euler[i]["product"]<euler[i+1]["product"] for i in range(len(euler)-1)),
        "euler_product_10000_within_2e_minus5":
            euler[-1]["error_to_zeta2"]<2e-5,
        "completed_zeta_symmetry_2_minus1":
            abs(completed_zeta_special(2)-completed_zeta_special(-1))<1e-12,
        "completed_zeta_symmetry_4_minus3":
            abs(completed_zeta_special(4)-completed_zeta_special(-3))<1e-12,
        "N_multiplicative_scaling_action_associative":
            all(Fraction(m*n)*x==Fraction(m)*(Fraction(n)*x)
                for m,n,x in scaling_samples),
    }

    return {
        "scope":"standard number-theory benchmark only",
        "place_rows":place_rows,
        "euler_product_s2":euler,
        "completed_zeta_special":{
            "Lambda(2)":completed_zeta_special(2),
            "Lambda(-1)":completed_zeta_special(-1),
            "Lambda(4)":completed_zeta_special(4),
            "Lambda(-3)":completed_zeta_special(-3),
        },
        "checks":checks,
        "passed":sum(checks.values()),
        "total":len(checks),
        "all_pass":all(checks.values()),
        "verdict":"Finite and archimedean places are globally coupled, not directly equivalent. On principal rationals the aggregate finite norm is exactly the inverse archimedean norm; finite Euler factors plus the archimedean gamma factor form the completed zeta object."
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

if __name__=="__main__":
    main()
