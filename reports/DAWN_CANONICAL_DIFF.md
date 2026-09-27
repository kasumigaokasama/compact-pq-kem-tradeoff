# DAWN primary-source comparison — 27 September 2026

## Source acquisition record

| Source | Identity | Access result |
|---|---|---|
| [IACR ePrint 2025/1520](https://eprint.iacr.org/2025/1520) | Received 2025-08-25; four revisions; last 2025-10-27 | Author/title/version metadata and abstract accessible; versioned PDF endpoint restricted; **no full-text SHA-256** |
| [ASIACRYPT chapter](https://doi.org/10.1007/978-981-95-5099-9_13) | Springer LNCS 16247, pp. 396–427, first online 2025-12-08 | Abstract and bibliography accessible; theorem/algorithm pages behind subscription; no full-text SHA-256 |
| [Authors' CFRG slides](https://datatracker.ietf.org/meeting/125/materials/slides-125-cfrg-ntru-based-public-key-encryption-01) | Lu and Liu, 2026-03-19, 11-page PDF | Primary author presentation accessible; confirms 615/436 α values and DFR claim around 2^-133, but omits full algorithms and proof |
| [Authors' DFR repository](https://github.com/Icarid-Liu/lattice-KEM-DFR-estimator) | commit `3c2602c30e13ce15ed7094ef97d9e4ed2dde01f6` dated 2025-10-27 | README, Sage utility and notebook retrieved through repository API; parameters and numerical DFR model available; not encryption/reference implementation |
| Phase 2A transcription | user-provided earlier audit, 2026-09-27 | Secondary transcription for comparison; cannot substitute for full primary manuscript |

The DFR utility blob is Git SHA `05b13ac42042f1a0ed0105110e6714b101a41043`; notebook blob `5fd4022734676680348344a814dc083612eb3a43`. These are Git blob identities, **not** invented SHA-256 hashes of the missing PDF.

## Security-relevant comparison that can be made

1. Phase 2A rounded the α-512 DFR as `2^-133`; the authors' notebook computes `log2(P)=-132.676946973757`, which rounds to -133. β computes `-130.133613253826`, rounding to -130. This is a precision difference, not a disagreement. The independent reconstruction in `experiments/reproduce_dawn_dfr_model.py` matches both values under the authors' assumptions.
2. Phase 2A noted generic `t^-1 w` versus concrete `w^-1` notation. The algebra audit explains why their recovered *message residues* can agree while their big-ring ciphertext contributions differ. Whether the canonical proof explicitly handles centered lifts and decoder errors **cannot** be checked from the accessible primary excerpts.
3. The authors' slides report α key/ciphertext `615/436` and a security column `139` for secret key/plaintext, while Phase 2A's transcribed comparison quoted `140` for a security-level column. Their meaning/cost-model distinction requires the full paper; this is **not evidence of an attack**.

**NO OFFICIAL IMPLEMENTATION LOCATED.** Searches by title, ePrint number, authors, “DAWN NTRU”, paper artifact and GitHub code returned an authors' DFR analysis repository but no author-maintained key-generation/encapsulation/decapsulation implementation, serialized test vectors or parameter source. Absence from those searches is not proof none exists. The Phase 2B codec has never been claimed wire-compatible.

**Diff status:** A complete canonical-vs-Phase-2A mathematical diff is impossible without ePrint 2025/1520's 2025-10-27 full PDF or the ASIACRYPT chapter. The exact missing external artifact is that 32-page publication-authoritative full text (pages 396–427 in proceedings), with algorithms, Theorems 1–2, Sections 4–6 and encoding table. A real SHA-256 and every security-relevant discrepancy must be recorded only after obtaining its bytes.
