# References and provenance — cutoff 27 September 2026

Publication type, version and evidence limits accompany each URL. A paper's existence does not independently validate its concrete parameters.

## Standards and official evaluations

1. **NIST, STANDARD.** [FIPS 203, ML-KEM](https://csrc.nist.gov/pubs/fips/203/final), 13 August 2024; exact sizes, normative algorithms and status. A future erratum is noted.
2. **NIST, OFFICIAL STATUS.** [PQC project](https://csrc.nist.gov/projects/post-quantum-cryptography), updated August 2026; HQC selected for ongoing standardization.
3. **NIST, OFFICIAL EVALUATION.** [IR 8545, Fourth Round status](https://nvlpubs.nist.gov/nistpubs/ir/2025/NIST.IR.8545.pdf), March 2025; BIKE DFR concerns and HQC choice. Its older HQC size table is superseded by the later team spec in this project.

## Lattice and NTRU

4. **Regev, PEER-REVIEWED.** [On lattices, learning with errors, random linear codes, and cryptography](https://doi.org/10.1145/1060590.1060603), STOC 2005. Reduction context, not a proof for every concrete instance.
5. **Langlois–Stehlé, EPRINT.** [Module-lattice reductions](https://eprint.iacr.org/2012/090).
6. **FrodoKEM authors, AUTHOR DRAFT.** [CFRG draft-03](https://datatracker.ietf.org/doc/draft-longa-cfrg-frodokem/), June 2026; exact FrodoKEM-640 sizes.
7. **NTRU team, AUTHOR SPEC.** [Round-three documentation](https://www.ntru.org/f/ntru-20190330.pdf), HPS/HRSS context.
8. **NTRU Prime team, AUTHOR SPEC.** [Round-three documentation](https://ntruprime.cr.yp.to/nist/ntruprime-20201007/Supporting_Documentation/doc.pdf).
9. **Liu et al., PEER-REVIEWED/EPRINT.** [DAWN](https://eprint.iacr.org/2025/1520), ASIACRYPT 2025; ePrint revised 27 October 2025. Full canonical text inaccessible in project workflow; abstract supports attributed size/assumption claims.
10. **DAWN authors, AUTHOR REPOSITORY.** [DFR estimator](https://github.com/Icarid-Liu/lattice-KEM-DFR-estimator), project-pinned commit 3c2602c30e13ce15ed7094ef97d9e4ed2dde01f6. Arithmetic model, not encryption reference implementation.
11. **Fouque et al., PEER-REVIEWED/EPRINT.** [BAT](https://eprint.iacr.org/2022/031), TCHES 2022; ePrint revised 12 April 2026 with proof-error correction. Mathematical diff unverified.
12. **CTRU/CNTR authors, EPRINT.** [Compact and Efficient KEMs over NTRU Lattices](https://eprint.iacr.org/2022/579).
13. **NTRU+ team, AUTHOR SPEC.** [NTRU+](https://www.ntruplus.org/); use version-specific claims only.
14. **Hofheinz–Hövelmanns–Kiltz, PEER-REVIEWED/EPRINT.** [Modular analysis of Fujisaki–Okamoto](https://eprint.iacr.org/2017/604); transform hypotheses are not automatically met by bare NIKE.

## Codes and recent structural cryptanalysis

15. **HQC team, AUTHOR SPEC.** [HQC, 22 August 2025](https://pqc-hqc.org/doc/hqc_specifications_2025_08_22.pdf), Tables 5–6; the project uses 2241/4433 B at level 1.
16. **BIKE team, AUTHOR SPEC.** [BIKE v5.2](https://bikesuite.org/files/v5.2/BIKE_Spec.2024.10.10.1.pdf), 10 October 2024. Full PDF timed out in the earlier audit; avoid unsupported theorem attribution.
17. **Open Quantum Safe, IMPLEMENTATION DOC.** [BIKE table](https://openquantumsafe.org/liboqs/algorithms/kem/bike.html), L1 1541/1573 B; its page labels implemented spec v5.1 and IND-CPA.
18. **Classic McEliece team, AUTHOR DOC.** [Implementation sizes](https://classic.mceliece.org/impl.html), [specification](https://classic.mceliece.org/spec.html).
19. **Annechini et al., EPRINT/CRYPTO 2026 line.** [QC-MDPC DFR](https://eprint.iacr.org/2025/1043), an analytic decoder model.
20. **Ghoshal et al., EPRINT/PREPRINT.** [Quasipolynomial cryptanalysis of McEliece](https://eprint.iacr.org/2026/1630), revised 27 August 2026: provable distinguisher and heuristic recovery extensions; concrete attacks described as not yet practical.
21. **Briaud et al., EPRINT/PREPRINT.** [Heuristic subexponential McEliece attack](https://eprint.iacr.org/2026/1232), revised 17 September 2026: challenges and heuristic extrapolation, not a practical Classic McEliece level-1 break.

## Historical failures and group actions

22. **Castryck–Decru, PEER-REVIEWED/EPRINT.** [SIDH key recovery](https://eprint.iacr.org/2022/975), EUROCRYPT 2023; public torsion images essential.
23. **Beullens, PEER-REVIEWED/EPRINT.** [Breaking Rainbow Takes a Weekend on a Laptop](https://eprint.iacr.org/2022/214), CRYPTO 2022.
24. **Tao–Petzoldt–Ding, PEER-REVIEWED.** [HFE variant attacks](https://csrc.nist.gov/CSRC/media/Events/third-pqc-standardization-conference/documents/accepted-papers/petzoldt-efficient-key-pqc2021.pdf), CRYPTO 2021.
25. **Shamir, PEER-REVIEWED.** [Basic Merkle–Hellman break](https://www-igm.univ-mlv.fr/~jyt/Crypto/crack_merkle_hellman.pdf), IEEE IT 1984.
26. **Hart et al., EPRINT/PKC.** [Practical cryptanalysis of WalnutDSA](https://eprint.iacr.org/2017/1160).
27. **Castryck et al., PEER-REVIEWED/EPRINT.** [CSIDH](https://eprint.iacr.org/2018/383), ASIACRYPT 2018; historical compact exchange.
28. **Bonnetain–Schrottenloher, PEER-REVIEWED.** [Quantum Security Analysis of CSIDH](https://zhengxuisogeny.github.io/Isogeny-Based-Cryptography/index/quantumcsidh.pdf), EUROCRYPT 2020, Table 4 and field-size tradeoffs.
29. **CSIDH team, AUTHOR ANALYSIS.** [Quantum-security response](https://csidh.isogeny.org/analysis.html); disputes oracle estimates.
30. **Frixons et al., EPRINT.** [Shifted-input vectorization quantum attack](https://eprint.iacr.org/2025/376.pdf), 2025; multiple public curves/QRAM.
31. **Banegas et al., EPRINT.** [dCTIDH](https://eprint.iacr.org/2025/107.pdf), 2025; platform-specific cycles.
32. **Banegas et al., PREPRINT.** [Hardened CTIDH](https://arxiv.org/abs/2509.12877), 2025; dummy-free evaluation.
33. **Robert, EPRINT/PREPRINT.** [Module action](https://eprint.iacr.org/2024/1556.pdf), October 2024; mathematical MIKE proposal.
34. **Robert/MIKE team, AUTHOR ANNOUNCEMENT.** [July 2026 mailing-list claims](https://mailarchive.ietf.org/arch/msg/cfrg/QM3t6di1bsgla6iIJ3gN6BbDoVk/); 64 B, speed and algebraic-model claims, not independent full CCA evidence.
35. **Årdal–Basso–Riepel, PEER-REVIEWED/EPRINT.** [Algebraic Isogeny Model](https://eprint.iacr.org/2026/032), EUROCRYPT 2026; model results are not automatically standard-model KEM proofs.
36. **Qi, PEER-REVIEWED.** [CSIDH KEM / CSIKE](https://doi.org/10.1515/jmc-2022-0007), 2022; modern parameter and QROM audit still needed.
37. **Dartois et al., PEER-REVIEWED/EPRINT.** [PEGASIS](https://eprint.iacr.org/2025/401), CRYPTO 2025.

## Project primary evidence

Phase 1: PQC-Phase-1-Research-Report.md, resolved separately in the project's persistent files. Local phases: [PQC-Phase-2A-Compact-NTRU-Audit.md](PQC-Phase-2A-Compact-NTRU-Audit.md), [PHASE_2B_REPORT.md](PHASE_2B_REPORT.md), [PHASE_2C_FINAL.md](PHASE_2C_FINAL.md), [PHASE_3_REPORT.md](PHASE_3_REPORT.md), [PHASE_4A_REPORT.md](PHASE_4A_REPORT.md). Detailed ledgers and scripts are inventoried in [EVIDENCE_LEDGER.md](EVIDENCE_LEDGER.md).
