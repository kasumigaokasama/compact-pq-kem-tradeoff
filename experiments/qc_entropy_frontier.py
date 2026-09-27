# Copyright 2026 Yusuf Kaya and Jan Moser
# SPDX-License-Identifier: Apache-2.0
"""Exact combinatorial bit counts and representation-only HQC/BIKE ledger.

Input numbers: HQC specification 2025-08-22 Tables 5–6; BIKE v5.2 Table 4.
No cryptographic security, DFR, or compression claim follows from these counts.
"""
from math import ceil, comb, log2

HQC = [("HQC-1", 17669, 46*384, 128, 66, 75),
       ("HQC-3", 35851, 56*640, 192, 100, 114),
       ("HQC-5", 57637, 90*640, 256, 131, 149)]
BIKE = [("BIKE-1", 12323, 142, 134),
        ("BIKE-3", 24659, 206, 199),
        ("BIKE-5", 40973, 274, 264)]

def support_bits(n, w):
    return log2(comb(n, w))

def ball_bits(n, t):
    return log2(sum(comb(n, i) for i in range(t+1)))

def main():
    for name, n, L, k, w, e in HQC:
        pk = 32 + ceil(n/8)
        u = ceil(n/8)
        v = ceil(L/8)
        ct = u+v+16
        print(f"{name}: n={n} L={L} k={k} rate={k/L:.8f}, redundancy={L-k}")
        print(f"  PK={pk}; CT={ct} [u={u}, v={v}, salt=16]; DK={pk+32+ceil(k/8)+32} / seed=32; K=32")
        print(f"  padding PK_s={8*u-n}, CT_u={8*u-n}, CT_v={8*v-L} bits")
        print(f"  support entropy each x/y={support_bits(n,w):.3f}, r1/r2/e={support_bits(n,e):.3f} bits")
        print(f"  Hamming ball log2 V(L,{e})={ball_bits(L,e):.3f} bits (illustrative, not decoder radius)")
    for name, r, w, t in BIKE:
        pk=ceil(r/8); ct=pk+32
        print(f"{name}: r={r} d={w//2} t={t}; PK={pk} CT={ct} pair={pk+ct}")
        print(f"  entropy secret pair={2*support_bits(r,w//2):.3f}; error pair={support_bits(2*r,t):.3f} bits")
        print(f"  Hamming ball log2 V({2*r},{t})={ball_bits(2*r,t):.3f} bits")
    name,n,L,k,w,e=HQC[0]
    pk=32+ceil(n/8)
    ct=ceil(n/8)+ceil(L/8)+16
    print(f"HQC-1 pair={pk+ct}; 20% target <= {int((pk+ct)*.8)} bytes; ML-KEM-512 pair=1568")
    for goal in (2048,1536,1024,750,500):
        print(f"  CT <= {goal} requires >= {ct-goal} bytes removed; either dense component alone plus salt >= {min(ceil(n/8),ceil(L/8))+16}")

if __name__ == '__main__':
    main()
