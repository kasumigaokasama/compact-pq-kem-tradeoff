# DAWN algebra: independent quotient calculation and remaining gate

Let `n=4k` (512 in the targeted sets), `y=x^k`, and work in `A=Z[x]/(x^n+1)`, so `y^4=-1`. Set `w=1+y`, `t=1+y²`. The following are **exact integral polynomial identities in A**:

1. `w*(y²-y³) = y²-y⁴ = 1+y² = t`.
2. `w*(1-y+y²-y³) = 1-y⁴ = 2`.
3. `t² = (1+y²)² = 2y²`.

For odd `q`, 2 and `y` are units in `R_q=A/qA`, so `w` and `t` are invertible there. Consequently `t*w^{-1}=y²-y³` **in `R_q`**, with the right-hand side also an integral representative. In the smaller quotient `A/(2,t)`, we have `y²=-1=1`; thus `y³=y` and

`t*w^{-1} = y²-y³ = 1+y = w` **only after reducing modulo `(2,t)`**.

More precisely, reduce first modulo `t` over the integers: `y²-y³ = -1+y = w-2`. Then reduce modulo 2 to obtain `w`. Hence the instantiated encryption term `w^{-1}m` followed by decryption multiplication by `t` can yield the same *message residue* as an abstract `t^{-1}wm`, but these are not equal ciphertext contributions in `R_q`: `w^{-1}` and `t^{-1}w` differ, and the lifted integer noise can differ. There is no ring homomorphism `R_q -> R_2` for odd `q`; one must center-lift after a `q`-modular operation and account for wraps before taking parity. This is the precise step requiring the canonical correctness proof.

The map to `A/(2,t)` is meaningful for the **integral representative** `y²-y³`; applying it directly to an arbitrary class of `R_q` would be invalid. The identity above resolves the elementary `t/w` residue question but **does not prove DAWN correctness, its failure probability, or equivalence of the paper's generic and instantiated ciphertext distributions**.

Phase 2A's wording implied `t=w²` might hold in `R_q`. The actual identity is `w²=t+2y` in `A`; the equality `w²=t` holds after reducing modulo 2. Its transcription therefore requires this quotient qualification.

| Component to reconstruct | Current evidence/status |
|---|---|
| Ring, `n,q,t,w`, message set | Paper-record abstract only confirms family; α `q=769`, β `q=257`, `n=512` and binary `n/4` message from noncanonical transcription; await canonical PDF |
| `h=g/f`, short samplers, rounding `d_c` | Phase 2A transcription only; unverified against canonical PDF/code |
| Decoder's chosen error position and FO reencryption | Phase 2A transcription only; no official vector check |

**Classification:** independently proven quotient identity; canonical algorithm consistency **unresolved**. No counterexample to the actual DAWN construction has been established.
