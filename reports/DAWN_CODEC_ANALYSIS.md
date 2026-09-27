# DAWN codec experiment and representation limit

`experiments/dawn_codec.py` implements an **independent model** of the Phase 2A Table 8 grouped bases. It accepts 512 values in `[0,M)`; α has a single base; β maps every coefficient to residues modulo 3 and 86/43 and reconstructs by CRT. Each group is a fixed-width little-endian field; the final group has its own width. Decode rejects noncanonical group values, nonzero padding, incorrect length and enumerative values outside `[0,M^512)`. It is **not an implementation of the verified official DAWN wire protocol**; bit ordering and coefficient order await a primary specification and test vectors.

| Object | Alphabet M | Entropy `512 log₂ M` | Group bits | Group bytes | Theoretical fixed-byte minimum | Removable bytes in this model |
|---|---:|---:|---:|---:|---:|---:|
| α public key | 769 | 4908.461971 | 4916 | 615 | 614 | **1** |
| α ciphertext | 110 | 3472.056173 | 3482 | 436 | 435 | **1** |
| β public key | 258 | 4101.748355 | 4106 | 514 | 513 | **1** |
| β ciphertext | 129 | 3589.748355 | 3594 | 450 | 449 | **1** |

The lower bound is `ceil(log_256(M^512))`, computed with exact integer `M**512` for the byte count; displayed bit entropies use floating point. The code includes a whole-vector base-M enumerative bijection which **actually emits the minimum fixed byte count** and rejects out-of-range encodings. That is an existence proof for saving one byte per object in this full-alphabet model. For β combined raw communication, 964 -> **962 bytes** (0.2075%); α public key plus ciphertext, 1051 -> **1049 bytes** (0.1903%). If only ciphertext is sent under a cached key, α 436 -> 435 bytes (0.2294%). This is **TRIVIAL ENGINEERING**, not cryptographic novelty.

The model is deliberately conservative about claims: the actual set of valid public keys/ciphertexts may be a strict subset of all coefficient vectors, but exploiting that requires a computable, canonical recognizer and potentially changes security or implementation complexity. Conversely the official codec may include constraints not represented by these four alphabets. These lower bounds therefore apply to the **full coefficient-vector alphabets**, not a theorem about the most compressed representation of valid DAWN objects.

The whole-vector integer uses ~615-byte intermediates and repeated divisions/multiplications, versus ≤64-bit grouped fields in the paper description. Runtime, constant-time behavior, memory, and byte-for-byte interoperability have **not** been benchmarked or established. No claim of a deployable one-byte patch follows. Group slack is mainly a grouping/computational tradeoff plus final byte alignment, not a security margin.

Verification command and outcome on 2026-09-27:

`cd experiments && python3 -m unittest -v test_dawn_codec.py` → 3 tests passed. They cover zero/max/random vectors, final partial groups, selected boundary positions, enumerative round trips, noncanonical group and whole-vector values, truncated/extra inputs, and padding. No official vector was available.
