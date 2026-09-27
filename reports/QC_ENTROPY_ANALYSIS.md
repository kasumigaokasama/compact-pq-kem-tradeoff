# Sparse supports, dense ciphertexts and entropy limits

`experiments/qc_entropy_frontier.py` computes `log₂ binomial(n,w)` with Python exact integers, and `log₂ V(n,t)` from the exact integer sum `Σᵢ≤t binomial(n,i)`. The Hamming-ball example with `t=ωe` is **not** the HQC decoder's correction radius. It illustrates the rapid growth of candidate errors.

| Set | HQC `log₂ C(n,ω)` per secret `x/y` | HQC `log₂ C(n,ωr)` per `r₁/r₂/e` | BIKE `log₂ C(r,w/2)` per secret block | BIKE `log₂ C(2r,t)` joint error |
|---|---:|---:|---:|---:|
| Level 1 | 622.952 | 694.542 | 625.929 | 1196.018 |
| Level 3 | 988.008 | 1105.304 | 957.662 | 1864.062 |
| Level 5 | 1334.285 | 1490.485 | 1319.182 | 2560.301 |

HQC sparse supports are **not transmitted**. `x,y` reside in the secret seed; `r₁,r₂,e` are deterministically derived from FO randomness. Sending position lists for `u` or `v` would be invalid: both are dense ring/codeword masks. The public key's `s` also behaves as a dense syndrome under the decisional QCSD assumption. Ideal combinatorial coding of untransmitted support therefore saves **zero** packet bytes. Secret-key seed storage already uses 32 B; a raw support list would be larger. For BIKE, the transmitted `h=h₁/h₀` and `c₀=e₀+h·e₁` are dense; its `e` is not sent as a support list.

There is a crucial distinction between *distributional Shannon entropy* and *efficient public encoding*. At fixed HQC PK, encapsulation chooses `k`-bit `m` and 128-bit salt, then computes the rest deterministically. Thus **the entire generated ciphertext has entropy at most `k+128` bits**, namely at most 256/320/384 bits at levels 1/3/5, even though its byte representation is 35464/71824/115368 bits. The same upper bound applies separately to `u` and `v`. This is not an available short ciphertext: transmitting `(m,salt)` reveals `m` and the shared secret, and finding a short *public, efficiently invertible without learning `m`* encoding of a pseudorandom dense image would itself change the cryptography. A conditional distribution or random-oracle image may have enormous computational encoding hardness despite small Shannon support. The *full-alphabet* size is therefore a conditional representation floor, **not an information-theoretic lower bound for the KEM**.

In the PKE before FO determinization, ideal independent source-support upper bounds are `3 log₂ C(n,ωr)` plus `k` and public-key conditioning; multiplication/addition collisions lower the true entropy. With FO, correlations among `(u,v,salt)` are strong but no safe joint compressor is known. Measuring an empirical entropy on a tractable sample cannot resolve image inversion at `2^128` scale. Computing `H(u,v)` by adding marginal entropies would be false. If an actual ≤20% joint encoding is ever proposed, canonical CCA re-encryption, malformed-input handling, constant-time implementation and attack cost must be established.

For a uniform bitstring `s` or a pseudorandom-looking `u`, the full-vector packed representation has at most 7 padding bits per object; HQC-1 `s` and `u` have three each, and `v` none. Fixed-weight enumerative coding, run length and position lists can only help when the *transmitted object* is known to be sparse. Seeded public `h` is already represented by a 32-byte seed. Seeded `e` cannot be exposed via its seed: the attacker would regenerate the error and often recover the message.
