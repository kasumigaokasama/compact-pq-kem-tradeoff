# Research-gap decision after limited reproduction

| Phase 2A hypothesis | Assessment | Evidence and limiting test |
|---|---|---|
| H1 alternate small quotient/code | **STILL OPEN** | Algebraic message residue can be reconstructed in a model, but no canonical theorem/DFR or alternative code has survived attack analysis |
| H2 improved grouping | **SUPPORTED as trivial serialization only** | Whole-vector enumerative codec saves **1 byte per DAWN object** in full-alphabet model; ≤0.23% for a single ciphertext, ~0.21% for β pair; no official interoperability or constant-time proof |
| H3 changed rounding/noise | **STILL OPEN** | A nominally smaller alphabet can worsen DFR or attack costs; no valid 512-level correlated tail or estimator run |
| H4 amortized α use | **SUPPORTED as a deployment arithmetic question only** | α repeated use costs `615+436k`; β costs `514+450k`. α is smaller for `k≥8` (`101≤14k`); key reuse/security and framing are not evaluated |

Thresholds from the supplied brief: <1% trivial engineering, 1–5% minor, 5–10% significant, >10% or qualitatively better tradeoff potential cryptographic contribution. The one-byte result is **TRIVIAL ENGINEERING**. It should not motivate a new KEM. No cryptographic research gap has been established. Lack of found independent DAWN cryptanalysis in targeted searches is **INSUFFICIENT EXTERNAL SCRUTINY**, not evidence of security.

Phase 1's fallback map names C1 structured/module noisy relations with C2 rounding as a control; C5 quasi-cyclic Hamming decoding; C7 class-group actions. If compact NTRU becomes a **NO** after proper validation, C5 provides the cleanest non-lattice attack agenda, though its existing ciphertext sizes are larger; C1 is a standardized baseline and C7 a high-risk size investigation. These are investigation directions, not candidate KEM recommendations.
