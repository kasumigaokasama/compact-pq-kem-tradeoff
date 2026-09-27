# Copyright 2026 Yusuf Kaya and Jan Moser
# SPDX-License-Identifier: Apache-2.0
"""Exact toy fixed-weight negacyclic-product dependency demonstration.

Not a DAWN decryption-failure estimate. Enumerates independent g,s, each
with one +1 and one -1 among n=8 positions, then compares a joint event to
an i.i.d. binomial model with the exact single-coefficient marginal.
"""
from fractions import Fraction
from itertools import permutations
from math import comb


def vectors(n):
    for pos, neg in permutations(range(n), 2):
        x = [0] * n
        x[pos] = 1
        x[neg] = -1
        yield x


def negacyclic(a, b):
    n = len(a)
    out = [0] * n
    for i, x in enumerate(a):
        if not x:
            continue
        for j, y in enumerate(b):
            k = i + j
            out[k % n] += (-1 if k >= n else 1) * x * y
    return out


def run(n=8, threshold=1):
    pool = list(vectors(n))
    total = len(pool)**2
    first = multi = 0
    counts = [0] * (n + 1)
    for a in pool:
        for b in pool:
            product = negacyclic(a, b)
            num = sum(abs(x) > threshold for x in product)
            counts[num] += 1
            first += abs(product[0]) > threshold
            multi += num >= 2
    p = Fraction(first, total)
    observed = Fraction(multi, total)
    independent = 1 - (1 - p)**n - n*p*(1 - p)**(n-1)
    print(f"n={n}, weight=(+1,-1), threshold={threshold}, total={total}")
    print(f"P(single exceed)={p} ({float(p):.8f})")
    print(f"P(at least 2), exact={observed} ({float(observed):.8f})")
    print(f"P(at least 2), iid={independent} ({float(independent):.8f})")
    print(f"event-count histogram={counts}")


if __name__ == "__main__":
    run()
