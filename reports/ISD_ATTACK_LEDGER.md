# Classical, quantum and structural attack ledger

The attacker goals are distinct: (1) decode one target syndrome/message; (2) find a sparse equivalent private check or low-weight dual; (3) distinguish QC instances; (4) exploit decoding failures; (5) recover partial secret across samples/users. A successful key-recovery relation may be a rotated/equivalent sparse check rather than the generated original. Honest HQC decodes with a **public** RMRS code after secret cancellation; BIKE needs its **private** sparse parity check for a useful syndrome decoder.

| Method | Main idea | Relevant target | Resource uncertainty |
|---|---|---|---|
| Prange | Pick information set free of errors | Baseline generic SD | Repetition exponent computable; poor compared with advanced attacks |
| Stern / Dumer | Split error support and match partial syndromes | Generic and QC SD | Time–memory/list tradeoff |
| MMT / BJMM | Multiple representations and list merging | Generic SD and low-weight dual | Large memory, detailed optimization |
| May–Ozerov / nearest neighbor | Faster partial-syndrome matching | HQC/BIKE security estimates | Memory access assumptions and concrete calibration |
| 2026 improved nearest-neighbor ISD | Combines representation/list tradeoffs with NN | Authors estimate ~0.78–1.47 lower bits for HQC/BIKE vs their chosen previous model | Their extension of the QC DOOM factor is **assumed**, not proved for their algorithm; does not independently set a standard's category |
| QC DOOM/orbit | Exploit cyclically related targets | Both; different gain for MDPC key recovery | Existing HQC analysis cites ~`√n` speedup; avoid double counting |
| Sparse-check search/folding | Find BIKE-style dual or exploit factors | Secret-decoder and hinted candidates | Parameter- and structure-specific; never substitute generic SD alone |

No current estimator was run on the exact 2025 HQC version or on BIKE v5.2; **no independent per-set bit-complexity, peak memory or quantum circuit count is claimed**. Security category is a specification claim subject to cost model. The 2026 [Li–Wang–Pan study](https://link.springer.com/article/10.1186/s42400-025-00469-z) is a published primary attack analysis, not an independently reproduced run. The authors' [HQC Section 6.3](https://pqc-hqc.org/doc/hqc_specifications_2025_08_22.pdf) discusses SD, QC DOOM and low-degree factor attacks.

Quantum options are separate: Groverized Prange speeds its trial selection; quantum walks/list matching can improve Stern/MMT/BJMM and nearest-neighbor subroutines. The 2017 [Kachigar–Tillich](https://arxiv.org/abs/1703.00263) and 2018 [Kirshanova](https://arxiv.org/abs/1808.00714) papers are primary algorithm sources; the 2026 NN study quotes an asymptotic exponent `0.057866 n` in its **unrestricted-memory model**, versus `0.058660 n` for its BJMM comparison. Those are not per-instance HQC exponents. QRAM, logical qubits, depth, coherent memory and multi-target costs have not been determined. A blanket halving of classical bits would be scientifically invalid.

QC-Hamming proposals with new hints also face adaptive reaction/side-channel attacks. [LEDAcrypt cryptanalysis](https://www.nist.gov/publications/cryptanalysis-ledacrypt) and [QC-LDPC reaction work](https://eprint.iacr.org/2017/494) are warnings about sparse private structure; absence of NIST selection for a scheme is not itself a break. Publicly sparse decoding hints should be tested by low-weight dual recovery before any size estimate.
