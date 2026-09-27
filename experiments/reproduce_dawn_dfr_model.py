# Copyright 2026 Yusuf Kaya and Jan Moser
# SPDX-License-Identifier: Apache-2.0
"""Independent numerical reproduction of the *author's independence model*.

Primary model: Icarid-Liu/lattice-KEM-DFR-estimator, commit
3c2602c30e13ce15ed7094ef97d9e4ed2dde01f6, notebook cells for DAWN.
This script does not validate actual DAWN DFR or key-conditioned tails.

We combine per-coordinate product distributions, then convolve an n-fold
kernel with nonnegative float64 weights. No subtraction of close numbers is
used for tails. Values around 1e-40 remain representable in float64.
"""
from __future__ import annotations

import math
import numpy as np


def law(pairs):
    out = {}
    for value, weight in pairs:
        out[value] = out.get(value, 0.0) + float(weight)
    return out


def ternary(n, weight):
    return {-1: weight/n, 0: 1-2*weight/n, 1: weight/n}


def product(a, b):
    return law((x*y, px*py) for x, px in a.items() for y, py in b.items())


def addition(a, b):
    return law((x+y, px*py) for x, px in a.items() for y, py in b.items())


def vector(a):
    lo, hi = min(a), max(a)
    return np.array([a.get(i, 0.0) for i in range(lo, hi+1)]), lo


def run(n, q, kg, kf, ks, ke, rounding):
    g, f, s, e = [ternary(n, w) for w in (kg, kf, ks, ke)]
    m = {0: .75, 1: .25}
    r = {x: 1/len(rounding) for x in rounding}
    gs, fe, fm = product(g,s), product(f,addition(e,r)), product(f,m)
    # The author's Dz is two independent draws of Dgs+Dfe, plus Dfm.
    kernel = {0: 1.0}
    for factor in (gs,gs,fe,fe,fm):
        kernel = addition(kernel, factor)
    a, a0 = vector(kernel)
    dist = np.array([1.0]); lo = 0
    for _ in range(n):
        dist = np.convolve(dist, a)
        lo += a0
    assert abs(float(dist.sum())-1)<1e-11
    coords = np.arange(lo, lo+len(dist))
    # Author calculate_DRF doubles the positive tail, even when its input is
    # the already nonnegative |Dz|+|Dz| distribution.
    p1 = 2*float(dist[coords>q//2].sum())
    p1total = math.fsum(math.comb(n,k)*p1**k*(1-p1)**(n-k)
                        for k in range(2, min(n,10)+1))
    ab = np.zeros(int(max(abs(coords)))+1)
    np.add.at(ab, np.abs(coords), dist)
    aa = np.convolve(ab,ab)
    p2 = 2*float(aa[q+1:].sum())
    p2total = -math.expm1(3*n*math.log1p(-p2))
    total = p1total+p2total
    print(f'n={n} q={q} rounding={rounding}')
    for label, value in [('P1',p1total),('P2',p2total),('DFR_model',total)]:
        print(f' {label}={value:.12e}, log2={math.log2(value):.9f}')
    return total


if __name__ == '__main__':
    run(512,769,160,64,96,160,range(-3,4))
    run(512,257,64,32,48,64,range(0,2))
