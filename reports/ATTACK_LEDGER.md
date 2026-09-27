# Attack ledger — no invented estimator outputs

**Estimator:** none downloaded or run. **Commit:** not available. Therefore no credible BKZ block size, numerical classical/quantum time, memory or success rate has been reproduced in this phase. The published DAWN figures of ~140 (α) and ~134 (β) “security level” bits are author estimates, not rows of an independent attack run. BAT's historical category claim is likewise unverified under the correction.

| Target | Candidate attack/weakest success condition | Dimension or structure | Required calculation | Status |
|---|---|---|---|---|
| DAWN α, β | Recover any useful short `(f',g')` with `f'h=g' mod q`, not necessarily original sampled pair | NTRU coefficient lattice nominally 2n=1024 | Pinned primal uSVP/BKZ plus hybrid sparse guessing, distribution and equivalent-key decoder test | **NOT RUN** |
| DAWN α, β | Recover ephemeral message from one ciphertext | Ring-LWE-like mask, `n=512`, one structured sample | Dual/primal and embedding attacks on exact `s,e` and rounding; message support and failures | **NOT RUN** |
| BAT-512 | Find an equivalent short basis that decodes or distinguish trapdoor ratio | NTRU lattice nominally 1024, basis geometry crucial | Short-basis/primal attacks, decoding target, corrected sampling model | **NOT RUN** |
| All | Multi-target/hybrid/automorphism attacks | Shared algebra, potentially many correlated transformed instances | Explicit sample-independence analysis and multi-user cost | **NOT RUN** |
| All | Active reaction and leakage | Decapsulation implementation | Constant-time/fault measurements with valid and invalid inputs | **NOT RUN** |

## Exact structural observation, not an attack

For `n=512`, `x^512+1` is the cyclotomic polynomial `Φ_1024`, irreducible over `Q`. For both `q=257` and `q=769`, `ord_1024(q)=4` (`q²≡513 mod 1024`, `q⁴≡1`). Consequently over `F_q` the polynomial has **128 irreducible quartic factors** (finite-field cyclotomic factor-degree theorem), yielding CRT projections to 4-dimensional fields. This is an exact algebraic property of these prime-modulus rings. It is **not** a key-recovery attack: projected small coefficients are mixed by the factor map; useful shortness, independent samples, message visibility and lifting all need proof. Automorphisms `x -> x^a` for odd `a mod 1024` create correlated views of the **same** sample, not automatically 512 independent samples.

An attacker may only need a projected or equivalent decoding key; exact recovery of the original `f,g` is a stronger and sometimes irrelevant win condition. Whether a 4-dimensional projection permits a useful partial key is **unknown**. A legitimate estimate must test the noise image, secret image, accumulated sample count and the map from projected recovery back to confidentiality.

## Quantum resource ledger

No gate/depth/logical-qubit/QRAM figures are asserted. Grover search of an independent keyspace, quantum enumeration, lattice sieving and nearest-vector subroutines have different prerequisites. A square-root heuristic cannot be applied uniformly to classical BKZ costs. Current quantum costs for these *specific* distributions remain unestimated.
