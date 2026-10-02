#!/usr/bin/env python3
"""
Finite host-reflection witness for the corrected quantum -> N direction.

Construction:
- canonical matrix units on C^3 indexed by {0,1,2} subset N;
- a unitary basis map into a "physical" host Hilbert realization;
- transport matrix units by unitary conjugation;
- choose a second host basis and verify the pulled-back N-shadows differ only by
  unitary conjugacy.

Construction-level only. No claim that bare N intrinsically is quantum.
"""
import argparse, cmath, json, math
from itertools import product

def zero(n):
    return [[0j for _ in range(n)] for _ in range(n)]

def eye(n):
    return [[1+0j if i==j else 0j for j in range(n)] for i in range(n)]

def matmul(A,B):
    return [[sum(A[i][k]*B[k][j] for k in range(len(B)))
             for j in range(len(B[0]))]
            for i in range(len(A))]

def adj(A):
    return [list(row) for row in zip(*[[complex(x).conjugate() for x in row] for row in A])]

def close(A,B,eps=1e-10):
    return all(abs(A[i][j]-B[i][j])<eps
               for i in range(len(A))
               for j in range(len(A[0])))

def trace(A):
    return sum(A[i][i] for i in range(len(A)))

N=3
E={}
for i,j in product(range(N),repeat=2):
    M=zero(N)
    M[i][j]=1+0j
    E[(i,j)]=M

omega=cmath.exp(2j*math.pi/N)
U=[[omega**(i*j)/math.sqrt(N) for j in range(N)] for i in range(N)]

P=[
    [1+0j,0j,0j],
    [0j,0j,1+0j],
    [0j,1+0j,0j],
]
U2=matmul(U,P)

transported={
    ij:matmul(matmul(U,M),adj(U))
    for ij,M in E.items()
}

cols=[
    [U[r][i] for r in range(N)]
    for i in range(N)
]

D=[
    [0j,0j,0j],
    [0j,2+0j,0j],
    [0j,0j,5+0j],
]
Aphys=matmul(matmul(U,D),adj(U))
Ae=matmul(matmul(adj(U),Aphys),U)
Af=matmul(matmul(adj(U2),Aphys),U2)
W=matmul(adj(U),U2)

matrix_law=all(
    close(
        matmul(E[(i,j)],E[(k,l)]),
        E[(i,l)] if j==k else zero(N)
    )
    for i,j,k,l in product(range(N),repeat=4)
)

transported_law=all(
    close(
        matmul(transported[(i,j)],transported[(k,l)]),
        transported[(i,l)] if j==k else zero(N)
    )
    for i,j,k,l in product(range(N),repeat=4)
)

rank_one=all(
    close(
        transported[(i,j)],
        [[cols[i][r]*complex(cols[j][c]).conjugate()
          for c in range(N)]
         for r in range(N)]
    )
    for i,j in product(range(N),repeat=2)
)

checks={
    "canonical_matrix_units_81_products": matrix_law,
    "fourier_basis_change_is_unitary": close(matmul(adj(U),U),eye(N)),
    "host_transport_preserves_matrix_unit_law_81_products": transported_law,
    "transported_matrix_units_are_rank_one_kets_bras": rank_one,
    "transport_preserves_adjoint":
        all(close(adj(transported[(i,j)]),transported[(j,i)])
            for i,j in product(range(N),repeat=2)),
    "second_basis_differs_by_source_unitary_gauge": close(W,P),
    "pulled_back_operator_shadows_are_unitarily_conjugate":
        close(Af,matmul(matmul(adj(W),Ae),W)),
    "trace_invariant_under_host_reflection_and_gauge":
        abs(trace(Aphys)-trace(Ae))<1e-10
        and abs(trace(Af)-trace(Ae))<1e-10,
}

def clean_matrix(A):
    return [[[z.real,z.imag] for z in row] for row in A]

def run():
    return {
        "scope":"finite-dimensional host-reflection witness only",
        "dimension":N,
        "checks":checks,
        "passed":sum(checks.values()),
        "total":len(checks),
        "all_pass":all(checks.values()),
        "host_basis_unitary":clean_matrix(U),
        "gauge_W":clean_matrix(W),
        "pulled_shadow_basis_e":clean_matrix(Ae),
        "pulled_shadow_basis_f":clean_matrix(Af),
        "verdict":"A physically anchored operator structure transported through two orthonormal-basis identifications yields N-indexed matrix presentations related exactly by unitary conjugacy. The matrix-unit law survives transport; basis choice is gauge."
    }

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--output",default="")
    args=ap.parse_args()
    r=run()
    s=json.dumps(r,indent=2,sort_keys=True)
    if args.output:
        with open(args.output,"w",encoding="utf-8") as f:
            f.write(s+"\n")
    print(s)
    raise SystemExit(0 if r["all_pass"] else 1)

if __name__=="__main__":
    main()
