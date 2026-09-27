# HQC ciphertext compression frontier

For level 1 in the August 2025 specification: `PK=2241 B`, `CT=2209 B(u)+2208 B(v)+16 B(salt)=4433 B`, total **6674 B**. The table is arithmetic at unchanged lengths; it is **not an impossibility theorem** for new code-based cryptography.

| CT target | Bytes that must disappear | First unchanged-component obstruction | What a credible construction must replace |
|---|---:|---|---|
| 2 KB = 2048 B | 2385 | Even one whole dense `v` plus salt is 2224 B; `u` plus salt 2225 B | More than one whole present component, or a shorter ambient code and new decoder/security parameters |
| 1.5 KB = 1536 B | 2897 | Either dense component alone exceeds target | New compact syndrome/error recovery architecture, likely secret decoding |
| 1 KB = 1024 B | 3409 | Ditto | A new parameter/security regime far from HQC's public-code model |
| 750 B | 3683 | Ditto | Ditto; no supported candidate |
| 500 B | 3933 | Ditto | Ditto; no supported candidate |

PK+CT ≤2 KB cannot retain even the current HQC-1 PK (2241 B). A ≥20% reduction of the 6674-byte pair requires ≤5339 B, saving at least 1335 B; a 20% CT-only reduction requires ≤3546 B, saving at least 887 B. Removing the entire `v` would save 2208 B but requires a receiver to recover the error from a syndrome: the BIKE/Niederreiter **secret sparse decoder** architecture already does this. It changes the hardness assumptions and DFR story. A few byte-saving codecs or the 16-byte salt cannot reach 20%.

At unchanged HQC dimensions, shrinking `v` discards parity checks needed to decode `x·r₂+r₁·y+e`, raising DFR; shortening `u` loses information required to cancel `r₂·h·y`, changing the residual noise and potentially revealing a low-dimensional QC instance. Jointly decreasing `n` and `n₁n₂` attacks both ciphertext terms, but reduces QC syndrome-decoding work factor and code redundancy before any safe byte claim. Under the author's DFR model, `n` is selected to meet level-specific failure/security requirements; its correlation assumption and proof margins must be reassessed under any change. The first *arithmetic* obstruction is the pair of dense components; the first *cryptographic* obstruction depends on the proposed modification and cannot be identified from lengths alone.

Hamming geometry: `log₂ V(17664,75)=694.517` bits for a ball of radius 75 (not HQC's actual RMRS radius). A generic `[N,k]` code has about `N−k` syndrome bits and at most `2^(N−k)` distinguishable cosets; unique decoding of radius `t` requires `V(N,t)≤2^(N−k)` (sphere-packing necessary condition), while an efficient decoder and DFR margin are stronger demands. Raising public code rate shrinks redundancy but usually narrows the correctable region; lowering error weights can improve correctness but harms decoding-hardness margins. These inequalities alone do not select parameters.
