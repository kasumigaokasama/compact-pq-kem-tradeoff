# DAWN β communication and security bottlenecks

The Phase 2B full-alphabet calculation uses 512 coefficients for each encoded object. The integer lower bounds below assume the same alphabet and no distribution-specific compression or protocol overhead. They are source-model bounds, **not** a theorem that every safe implementation needs these bits.

| Component | Current bits | Full-alphabet entropy / minimum whole bytes | Active constraint known now | What must change for a meaningful reduction |
|---|---:|---:|---|---|
| Public key | `514×8=4112` | `4101.748355` bits / **513 B** | Alphabet capacity; permissible modulus and secret relation set by *unverified* attack margin | Fewer independent coefficients, smaller modulus/alphabet, or new structured public relation, each requiring new attack and correctness analysis |
| Ciphertext | `450×8=3600` | `3589.748355` bits / **449 B** | Alphabet capacity; rounding width and decoder failure under the author model | Coarser rounding or reduced dimension/alphabet plus a decoder/noise theorem and CCA verification |
| Key + one ciphertext | **7712 bits = 964 B** | `7691.496710` bits / **962 B** | Only 20.50329 padding bits remain | Cryptographic change to support smaller alphabets or objects; ordinary enumerative packing saves at most 2 B |

An at-least-5% byte saving needs a pair of at most **915 B** (49 B less); at least 10% needs **867 B** (97 B less). Relative to modeled full-alphabet entropy, the 5% target is 371.49671 fewer bits and the 10% target is 755.49671 fewer bits. Those are reductions in information-bearing representation, not a clever packing of the current alphabets. The theoretical 2-byte saving is 0.2075% of 964 B.

The author DFR surrogate for β changes from log2 `-130.134` under rounding `{0,1}` to `-114.743` under `{-1,0,1}`. This finite difference does not directly model a particular coarser ciphertext format, but makes the rounding/decoding margin a live constraint. Sparse secret changes can improve this *model's* DFR while making key-recovery attacks easier. The security constraint that binds first when dimensions or modulus shrink is **unknown**, because independent compatible attack costs and the corrected BAT proof are absent. The dual roles of the NTRU relation and ephemeral noisy relation must be compared under equivalent-key, recovery and distinguishing goals. An unverified DFR/QROM conversion could itself dominate an otherwise comfortable lattice margin.

CCA framing and deterministic decapsulation may add implementation constraints. No official DAWN wire format or code was located, so the modeled two-byte packing gain is not an interoperability result. For many encapsulations, α has total `615+436k` bytes and β `514+450k`, making α smaller at `k≥8` by simple arithmetic; this is a deployment tradeoff and does not establish secure key reuse.
