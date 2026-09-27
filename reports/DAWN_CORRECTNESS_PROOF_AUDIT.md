# DAWN correctness audit: proven skeleton and undecided decoder

**Classification: AMBIGUOUS BUT RESOLVABLE at the algebraic-message level; full canonical specification undecided.** This is a conditional audit of the Phase 2A-transcribed formula, not a certification of the published KEM.

Write `A=Z[x]/(x^n+1)`, `n=4k`, `y=x^k`, `t=1+y²`, `w=1+y`. In `A`, `y⁴=-1`, `w(y²-y³)=t` and `w(1-y+y²-y³)=2`. For odd `q`, `w` is a unit in `R_q=A/qA`; define `u=t*w^-1=y²-y³` in `R_q`, with the displayed **integral** representative. In `A/(t)`, `u=y-1=w-2`; in `A/(2,t)`, `u=w`.

Assume the transcribed encryption equation `a ≡ h s + e + w^-1 m (mod q)` in `R_q`, `h≡gf^-1 (mod q)`, and a ciphertext `c` which decompresses to integer polynomial `C`. Define the *actual deterministic* rounding residue `ρ` by `C ≡ a+ρ (mod q)`. The distribution of `ρ` is not assumed uniform in this identity. In `R_q`:

`t f C ≡ t g s + t f(e+ρ) + u f m`.

Take the coefficientwise centered lift `L_q(t f C)` to `[-(q-1)/2,(q-1)/2]^n`, and choose integral representatives for the right-hand products in `A`. There is then a unique integer polynomial `K` (for those choices) with

`L_q(t f C) = t[g s+f(e+ρ)] + u f m - q K` **in `A`**.

Reduce this *integer equality* in `A/(2,t)`. The `t[...]` term vanishes; `u=w` and odd `q=1 mod 2`. Thus the residue is `w f m + K` (minus equals plus modulo 2). A direct map `R_q -> R_2` would be invalid; the centered lift and `qK` are precisely the missing transition. The decoder's task is to infer/correct `K` modulo `(2,t)`. The authors describe a single-error correction mechanism, but its exact sufficient conditions and branch selection require the full canonical manuscript and code.

If `K=0`, and `f2 f=1+w v` in `A/(2,t)` for some `v`, then multiplying by `f2` gives `f2·w f m = w m + w² v m = w m (mod 2,t)`, because `w²=t` **modulo 2**. Since `m` has degree `<k`, `w m=m+y m` has two equal coefficient blocks, so one block recovers `m`. This proves **failure-free message recovery under the stated equations and invertibility condition**, even though `w^-1` and generic `t^-1w` do not produce equal ciphertexts in `R_q`.

Unresolved obligations: exact definition of `C`, rounding direction and coefficients of `ρ`; sampled `f,g,s,e,m`; center-lift/decoder handling of `K` when it has one or more nonzero entries; invertibility and stored `f2`; algebra of reencrypt-and-compare. The paper's DFR estimate concerns the probability and geometry of `K`, not the failure-free identity alone. No violating valid input or actual specification error has been demonstrated.
