# Evidence, confidence and reproduction ledger

## Interpretation

**ESTABLISHED** = specified count, documented revision, theorem/attack under its stated hypotheses, or exact arithmetic. **STRONGLY SUPPORTED** = multiple sources support a conditional assessment. **PROJECT-REPRODUCED** = our code recalculated a specified model, never by itself validated a real cryptosystem. **PLAUSIBLE** = reasoned inference. **SPECULATIVE** = unvalidated design path. **UNKNOWN** = no defensible determination. External source labels: STANDARD, PEER-REVIEWED, EPRINT/PREPRINT, AUTHOR CLAIM, PROJECT EXPERIMENT. The substantive claim and its limitation travel together.

| Claim | Evidence and source class | Confidence | Unresolved issue |
|---|---|---|---|
| ML-KEM FIPS 203 final and level-1 PK+CT 800+768=1568 B | [FIPS 203](https://csrc.nist.gov/pubs/fips/203/final), STANDARD | ESTABLISHED count/status | computational hardness remains conditional; standard lists planned erratum |
| HQC selected, not described as final FIPS | [NIST PQC status](https://csrc.nist.gov/projects/post-quantum-cryptography), STANDARDIZATION NOTICE | ESTABLISHED as of cutoff | future publication |
| HQC-1 current-project PK+CT 2241+4433=6674 B | [team spec 2025-08-22](https://pqc-hqc.org/doc/hqc_specifications_2025_08_22.pdf), AUTHOR SPECIFICATION; [HQC_BYTE_LEDGER.md](HQC_BYTE_LEDGER.md), PROJECT arithmetic | ESTABLISHED encoding in version | spec may change during standardization |
| BIKE-L1 1541+1573=3114 B | [OQS table](https://openquantumsafe.org/liboqs/algorithms/kem/bike.html), implementation documentation; [HQC_VS_BIKE.md](HQC_VS_BIKE.md) | ESTABLISHED for cited encoding | OQS implementation labels v5.1 and IND-CPA; do not silently transfer v5.2 proof |
| DAWN-β modeled 514+450=964 B | [DAWN abstract](https://eprint.iacr.org/2025/1520), AUTHOR CLAIM; [DAWN_CODEC_ANALYSIS.md](DAWN_CODEC_ANALYSIS.md) and [experiments/dawn_codec.py](../experiments/dawn_codec.py), PROJECT EXPERIMENT | PROJECT-REPRODUCED packing *from Phase 2A transcription* | official wire vectors/full canonical spec unavailable |
| DAWN same-alphabet one-byte-per-object slack, 964→962 B | exact \(\lceil512\log_2M\rceil\) bounds and constructive bijection, [DAWN_CODEC_ANALYSIS.md](DAWN_CODEC_ANALYSIS.md) | PROJECT-REPRODUCED conditional full-alphabet result | distribution-specific compressor, constant-time cost and official compatibility |
| DAWN author α/β DFR model log2 -132.676946974 / -130.133613254 | pinned author notebook plus [experiments/reproduce_dawn_dfr_model.py](../experiments/reproduce_dawn_dfr_model.py), PROJECT EXPERIMENT | PROJECT-REPRODUCED **model** | actual correlated/key-conditioned/CCA failure probability UNKNOWN |
| Paired-noise β surrogate joint/product ~9.67×10^5 | [experiments/paired_noise_check.py](../experiments/paired_noise_check.py), restricted iid surrogate | PROJECT-REPRODUCED *surrogate* | omitted encoding/fixed-weight and real decoder; cannot substitute into real DFR |
| DAWN quotient identity \(w(y^2-y^3)=t\) and full decryption undecided | [DAWN_CORRECTNESS_PROOF_AUDIT.md](DAWN_CORRECTNESS_PROOF_AUDIT.md), ring calculation | PROJECT-REPRODUCED conditional skeleton | canonical centered-lift decoder and actual code |
| DAWN ring modulo 257/769 factors into 128 quartics | [DAWN_RING_STRUCTURE_ANALYSIS.md](DAWN_RING_STRUCTURE_ANALYSIS.md), [experiments/ring_structure.py](../experiments/ring_structure.py) | PROJECT-REPRODUCED algebra | no projected key-recovery advantage shown |
| BAT 12 April 2026 proof-error correction | [BAT ePrint revision](https://eprint.iacr.org/2022/031), author metadata | ESTABLISHED revision; exact theorem UNKNOWN | two immutable versions and proof diff missing |
| No new ≥5% defensible NTRU mechanism | [PHASE_2C_FINAL.md](PHASE_2C_FINAL.md), local falsification | STRONGLY SUPPORTED scoped project judgment | missing primary validation/estimator could change it |
| HQC \(u\) and \(v\) are dense, functionally distinct | [HQC spec](https://pqc-hqc.org/doc/hqc_specifications_2025_08_22.pdf), [HQC_BYTE_LEDGER.md](HQC_BYTE_LEDGER.md) | ESTABLISHED design equation | new mathematical encoding not universally ruled out |
| HQC-1 secret/ephemeral support entropy 622.952/694.542 bits | [experiments/qc_entropy_frontier.py](../experiments/qc_entropy_frontier.py), exact binomial integer | PROJECT-REPRODUCED arithmetic | support not transmitted, hence no direct network saving |
| BIKE shorter CT substitutes private decoder for public noisy codeword | [HQC_VS_BIKE.md](HQC_VS_BIKE.md), specs, [NIST IR 8545](https://nvlpubs.nist.gov/nistpubs/ir/2025/NIST.IR.8545.pdf) | STRONGLY SUPPORTED architectural comparison | precise v5.2 worst-key DFR/CCA remains model-dependent |
| QC branch no novel ≤2 KB pair path passed | [PHASE_3_REPORT.md](PHASE_3_REPORT.md), [QC_RESEARCH_MECHANISMS.md](QC_RESEARCH_MECHANISMS.md) | STRONGLY SUPPORTED scoped screen | not a lower bound on all code KEMs |
| CSIDH-512 hidden-shift vectors and enlarged fields | [Bonnetain–Schrottenloher](https://zhengxuisogeny.github.io/Isogeny-Based-Cryptography/index/quantumcsidh.pdf), PEER-REVIEWED; [CSIDH response](https://csidh.isogeny.org/analysis.html), AUTHOR ANALYSIS | ESTABLISHED that models/paper exist; concrete PQ margin contested | coherent oracle cost, depth, physical RAM/qubits |
| MIKE 64 B public Level-1 object, <5 ms full exchange on named CPU | [Robert 2024](https://eprint.iacr.org/2024/1556.pdf), PREPRINT; [team announcement](https://mailarchive.ietf.org/arch/msg/cfrg/QM3t6di1bsgla6iIJ3gN6BbDoVk/), AUTHOR CLAIM | ESTABLISHED as a *claim*; independent performance UNKNOWN | full code/paper benchmark and new assumption analysis |
| MIKE ~128 B raw two-object exchange | 64+64 inferred from symmetric curve-object description, [GROUP_ACTION_BYTE_LEDGER.md](GROUP_ACTION_BYTE_LEDGER.md) | PLAUSIBLE raw inference | exact encapsulation syntax; complete CCA CT UNKNOWN |
| No verified MIKE IND-CCA CT size in project evidence | [GROUP_ACTION_KEM_TRANSFORMS.md](GROUP_ACTION_KEM_TRANSFORMS.md), scoped audit | STRONGLY SUPPORTED negative *search result*, not nonexistence theorem | future publication could resolve |
| 2026 McEliece preprint: provable distinguisher; heuristic recovery; not practical parameter break established | [Ghoshal et al.](https://eprint.iacr.org/2026/1630), PREPRINT abstract | ESTABLISHED author claim/scope; independent concrete validation UNKNOWN | full independent cryptanalysis and impact |
| Entire search found no build-worthy new KEM | all four phase decisions and falsification ledgers | STRONGLY SUPPORTED **project judgment** | not a universal impossibility theorem |

## Reproduction manifest and boundaries

| Project artifact | Input/method | Reproduced result | Explicit non-result |
|---|---|---|---|
| `experiments/dawn_codec.py`, `test_dawn_codec.py` | Phase 2A-transcribed groups, exact integer radices, canonical local unpack rejection | 615/436/514/450 B; three unit tests; full-vector one-byte-per-object bound | no official wire vectors, reference code or constant-time audit |
| `experiments/reproduce_dawn_dfr_model.py` | author notebook parameters and positive float64 convolution | α/β nine-decimal log2 model agreement | not actual correlated failure bound |
| `experiments/paired_noise_check.py` | restricted iid paired-transform surrogate at n=512 | joint dependence anomaly; β ~9.67×10^5 ratio | not a corrected DAWN DFR |
| `experiments/toy_correlation.py` | exhaustive small fixed-weight negacyclic toy | all 3136 stated pairs, binomial-independence counterexample | toy is not DAWN parameters |
| `experiments/ring_structure.py` | polynomial ring identities / finite-field factor-degree checks | 128 quartics for each modulus, lift identity | no lattice attack |
| `experiments/qc_entropy_frontier.py` | exact \(\binom nw\), Hamming-ball sums, dense-byte ledger | 622.952/694.542 and BIKE 1196.018 support bits at level 1 | no public compressor or ISD estimate |

**Unrun gate:** [ATTACK_ESTIMATOR_RESULTS.md](ATTACK_ESTIMATOR_RESULTS.md) pinned `malb/lattice-estimator` commit `53da5982597709ba0fdf94ea37a84d822310fd84`, but Sage was unavailable. There are **no** independent full classical/quantum attack-cost numbers for DAWN/BAT from this project. [DAWN_SOURCE_MANIFEST.md](DAWN_SOURCE_MANIFEST.md) and [DAWN_CANONICAL_DIFF.md](DAWN_CANONICAL_DIFF.md) document missing full-source hashes and code.
