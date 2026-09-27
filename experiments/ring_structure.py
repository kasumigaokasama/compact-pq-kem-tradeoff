# Copyright 2026 Yusuf Kaya and Jan Moser
# SPDX-License-Identifier: Apache-2.0
"""Elementary Φ_1024 ring identities; no lattice attack is implemented."""
from math import gcd


def mul(a,b,modulus=None):
    out=[0]*4
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            k=i+j
            out[k%4]+=(-1 if k>=4 else 1)*x*y
    return [v%modulus if modulus else v for v in out]


def order(a,m):
    x=a%m
    for d in range(1,m+1):
        if x==1:return d
        x=x*a%m
    raise ValueError('not a unit')


def run():
    one=[1,0,0,0]; w=[1,1,0,0]; t=[1,0,1,0]
    u=[0,0,1,-1]; wi2=[1,-1,1,-1]
    assert mul(w,u)==t
    assert mul(w,wi2)==[2,0,0,0]
    assert mul(t,t)==[0,0,2,0]
    print('identities: w*u=t; w*(1-y+y²-y³)=2; t²=2y²')
    for q in (257,769):
        degree=order(q,1024)
        assert degree==4 and gcd(q,1024)==1
        print(f'q={q}: ord_1024(q)={degree}, irreducible factors={512//degree}, degree each={degree}')
    print('odd-power automorphisms modulo 1024:',sum(gcd(a,1024)==1 for a in range(1024)))


if __name__=='__main__':run()
