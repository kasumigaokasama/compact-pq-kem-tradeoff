# Copyright 2026 Yusuf Kaya and Jan Moser
# SPDX-License-Identifier: Apache-2.0
"""Exact (float64 positive-sum) paired transform analysis within an iid surrogate.

For t=1+x^(n/2), b_i=A_i-A_(i+n/2) and b_(i+n/2)=A_i+A_(i+n/2).
This script uses the author's *per-coordinate independent* model for A=gs+f(e+r),
but omits encoding f*m and all fixed-weight / secret-sharing dependencies.
It is a falsification of joint independence in a restricted surrogate, not DFR.
"""
import numpy as np
from reproduce_dawn_dfr_model import addition, product, ternary, vector


def check(n,q,kg,kf,ks,ke,rounding):
    g,f,s,e=[ternary(n,w) for w in (kg,kf,ks,ke)]
    r={x:1/len(rounding) for x in rounding}
    atom=addition(product(g,s),product(f,addition(e,r)))
    a,a0=vector(atom)
    D=np.array([1.0]);lo=0
    for _ in range(n):
        D=np.convolve(D,a);lo+=a0
    vals=np.arange(lo,lo+len(D)); bound=q//2
    # Uses symmetry of A for these alphabets. Compute both events by 1D mask
    # dot products, avoiding large outer arrays.
    single=both=0.0
    for i,x in enumerate(vals):
        py=D[i]
        if py<1e-300: continue
        minus=np.abs(x-vals)>bound
        plus=np.abs(x+vals)>bound
        single+=py*float(D[minus].sum())
        both+=py*float(D[minus & plus].sum())
    print(f'n={n} q={q} |A_i-A_j|>{bound}: {single:.9e}')
    print(f'paired exceed probability={both:.9e}; iid product={single*single:.9e}')
    print(f'pair/iid ratio={both/(single*single):.9g}')


if __name__=='__main__':
    check(512,257,64,32,48,64,range(0,2))
    check(512,769,160,64,96,160,range(-3,4))
