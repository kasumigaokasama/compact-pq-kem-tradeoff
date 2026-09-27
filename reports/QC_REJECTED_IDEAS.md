# Immediate compression falsifications

| Idea | Arithmetic temptation | Specific first failure | Outcome |
|---|---|---|---|
| Send seed for HQC `r₁,r₂,e` instead of `u,v` | 32-byte seed vs 4417-byte PKE ciphertext | Publicly regenerate all errors; in particular `v−s r₂−e=C(m)` and decode `m` | **REJECTED** |
| Send `(m,salt)` or index ciphertext in generated image | Only 256 bits of encapsulation entropy at level 1 | Explicitly gives away shared-secret preimage; a computable trapdoor inversion/index is a new primitive, not a codec | **REJECTED** |
| Enumerative support coding of `u` or `v` | Sparse-input entropy ~695 bits each | Actual transmitted objects are dense; support rank is not an encoding of them | **REJECTED** |
| Delete one of `r₁,r₂,e` by correlation | Eliminate a random source | Security reduction relies on specific noisy QC distribution; correlation can expose relation or permit direct message cancellation | **UNCLEAR mathematically, REJECTED as ready mechanism** |
| Drop `v` and decode syndrome privately | Saves 2208 B at HQC-1 | This is the existing BIKE/Niederreiter secret-decoder point, with key-dependent DFR/low-weight dual exposure | **REJECTED as novel HQC compression** |
| Partial sparse parity-check hint | Might shrink public codeword | Public low-weight dual recovery; if hint is secret, new key-conditioned DFR and reaction attack | **UNCLEAR, no survival evidence** |
| Remove salt | 16 B saved (0.36% of CT) | 2025 salted FO multi-ciphertext security changes; far below meaningful threshold | **REJECTED** |
| Send sparse support positions/run lengths | Dense output cannot use them | If applied to actual sparse error, reveals it; ordering, duplicate and malformed encoding risks | **REJECTED** |
| Truncate `u`/`v` | Direct byte saving | Loses cancellation or correction information; creates alternative decoding/QC projection target | **REJECTED pending a new proof** |

Novelty check: [HQC original framework](https://arxiv.org/abs/1612.05572) already publicizes the public-code point; [BIKE v5.2](https://bikesuite.org/files/v5.2/BIKE_Spec.2024.10.10.1.pdf) and [Classic McEliece](https://classic.mceliece.org/nist.html) occupy known secret-decoder/syndrome points; [LEDAcrypt cryptanalysis](https://www.nist.gov/publications/cryptanalysis-ledacrypt) warns against exposed QC-LDPC structure. [CRYPTO 2026 QC-MDPC DFR work](https://eprint.iacr.org/2025/1043) already explores compact syndrome ciphertexts with a specified iterative-decoder model; [2026 semi-MDPC work](https://link.springer.com/article/10.1186/s42400-026-00576-5) claims another intermediate check distribution, requiring independent scrutiny. A modified encoding of the same syndrome is not a new mathematical mechanism.
