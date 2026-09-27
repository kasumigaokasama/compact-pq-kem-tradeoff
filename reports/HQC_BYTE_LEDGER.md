# HQC byte ledger (author specification 2025-08-22)

Primary source: [HQC specification, 22 August 2025](https://pqc-hqc.org/doc/hqc_specifications_2025_08_22.pdf), Sections 3.4–3.6, Tables 3–6. This **supersedes the older sizes** in [NIST IR 8545 (March 2025)](https://nvlpubs.nist.gov/nistpubs/ir/2025/NIST.IR.8545.pdf): the August update changed the FO transform, key formats and lengths. HQC is selected for standardization, not a final published FIPS as of the status check; ML-KEM is standardized in [FIPS 203](https://csrc.nist.gov/pubs/fips/203/final). BIKE and Classic McEliece were not selected in NIST Round 4; nonselection does not mean broken.

Let `R=F₂[X]/(X^n−1)`. `x,y∈R` each have weight `ω`; `h∈R` is derived from the 32-byte public seed; `s=x+h·y`. The public key serializes `(seed_ek,s)`. With a message of `k` bits, the sender draws `r₁,r₂,e∈R`, each of weight `ωr=ωe`, from FO randomness and forms `u=r₁+h·r₂`, `v=C.Encode(m)+Truncate(s·r₂+e,ℓ)`, `ℓ=n−n₁n₂`. `C` is the public concatenation of shortened Reed–Solomon over GF(256) and duplicated `[128,8,64]` Reed–Muller code. The receiver computes `v−Truncate(u·y,ℓ)=C.Encode(m)+Truncate(x·r₂−r₁·y+e,ℓ)` and decodes. The KEM adds a 16-byte salt, derives `θ` and `K` from `H(ek)||m||salt`, and reencrypts on decapsulation with implicit rejection. This is a two-dense-object ciphertext, although its *inputs* include sparse vectors.

| Set | `n`; `n₁n₂`; `k` | PK `32+ceil(n/8)` | `u=ceil(n/8)` | `v=n₁n₂/8` | Salt | CT total | DK default / seed form | Shared |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| HQC-1 | 17669; 17664; 128 | **2241 B** | 2209 | 2208 | 16 | **4433 B** | 2321 / 32 B | 32 B |
| HQC-3 | 35851; 35840; 192 | **4514 B** | 4482 | 4480 | 16 | **8978 B** | 4602 / 32 B | 32 B |
| HQC-5 | 57637; 57600; 256 | **7237 B** | 7205 | 7200 | 16 | **14421 B** | 7333 / 32 B | 32 B |

The default DK embeds the PK, a 32-byte PKE secret seed, `ceil(k/8)`-byte fallback value and a 32-byte KEM seed. The 32-byte compressed DK regenerates the pair at computation cost. These sizes are raw objects; transport framing is outside scope. The public seed is needed to regenerate `h`; `s` cannot be recomputed without the secret. `u` is the fresh public mask and `v` is the noisy codeword needed by the public decoder. Neither is a low-weight vector. The salt is FO domain separation/multi-ciphertext binding; it is **128 bits**, not a 2-KB CCA tag. Only 3/5/3 unused bits in the `n`-bit packed objects and zero bits in `v` are ordinary byte padding for HQC-1/3/5.

The public code rate `k/(n₁n₂)` is 0.007246, 0.005357 and 0.004444; redundancy is 17536, 35648 and 57344 bits. This very low rate buys tolerance of the composite error `x·r₂+r₁·y+e`, not a direct transmission of 17-Kbit secret data. At level 1, `n₁=46`, inner multiplicity 3, `46×384=17664`; levels 3/5 use `56×640`, `90×640`. The five/eleven/thirty-seven ambient tail positions are excluded from `v` to match code length while `u` stays length `n`.

For comparison, BIKE v5.2 has PK/CT `1541/1573`, `3083/3115`, `5122/5154` bytes; Classic McEliece's level-1 `mceliece348864` has `261120/96` bytes (NIST IR 8545); ML-KEM-512 has `800/768` bytes (FIPS 203). These are different assumptions and correctness profiles.
