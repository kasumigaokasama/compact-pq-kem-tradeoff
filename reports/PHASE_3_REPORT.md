# Phase 3 — QC-Hamming compactness audit

27 September 2026. Research question: is there a **new, defensible** quasi-cyclic Hamming mechanism that substantially shrinks HQC communication without a hidden correctness or security cost? No final KEM is designed. Reproducible arithmetic is in `experiments/qc_entropy_frontier.py`; the nine companion reports separate byte accounting, geometry, attacks, DFR and falsified ideas.

## Source and status register

| System | Authoritative basis used | September 2026 status | Level-1 raw PK + CT |
|---|---|---|---:|
| HQC | [author specification 2025-08-22](https://pqc-hqc.org/doc/hqc_specifications_2025_08_22.pdf), 51 pages, Tables 5–6 | [NIST-selected for standardization](https://www.nist.gov/news-events/news/2025/03/nist-pqc-standardization-process-hqc-announced-4th-round-selection), final FIPS publication not established by the current source check | `2241+4433=6674 B` |
| BIKE | [author v5.2 specification 2024-10-10](https://bikesuite.org/files/v5.2/BIKE_Spec.2024.10.10.1.pdf); indexed tables and [NIST IR 8545](https://nvlpubs.nist.gov/nistpubs/ir/2025/NIST.IR.8545.pdf) | Research candidate, **not selected** in Round 4; not thereby broken | `1541+1573=3114 B` |
| Classic McEliece | [team specification index](https://classic.mceliece.org/nist.html), `mceliece-spec-20221023.pdf` listed; [NIST IR 8545](https://nvlpubs.nist.gov/nistpubs/ir/2025/NIST.IR.8545.pdf) size/correctness comparison | Not selected by NIST in that round; not thereby broken | `261120+96=261216 B` |
| ML-KEM-512 | [NIST FIPS 203 final, 2024-08-13](https://csrc.nist.gov/pubs/fips/203/final) | Standardized control | `800+768=1568 B` |

The older March 2025 NIST table reports HQC `2249+4497 B`. The August author revision changes KEM details and sizes; all Phase 3 HQC byte calculations use the **later** `2241+4433 B` version. The full BIKE v5.2 PDF timed out via the research interface, but indexed primary excerpts supplied its algorithms, parameters and size table, cross-checked against NIST. No independent ISD estimator, decoder rare-tail proof, memory benchmark or new KEM was run.

## Mathematical compression map

HQC's public random double-circulant matrix is cheap because `h` is seeded; the public `s=x+h y` is a dense `n`-bit syndrome. Its ciphertext `u=r₁+h r₂` is another dense `n`-bit mask; `v=C(m)+Truncate(s r₂+e,ℓ)` is a dense `n₁n₂`-bit noisy public codeword. For level 1, this yields PK `32+2209`, CT `2209+2208+16` bytes. The public RMRS code carries **17536 redundancy bits** for a 128-bit message, permitting decoding of composite noise. The separate dense `u` lets the receiver cancel `r₂ h y`, leaving `x r₂+r₁ y+e`. The 16-byte KEM salt addresses FO security. Small error supports are **inputs**, not transmitted ciphertext components.

BIKE instead uses one dense QC syndrome `c₀=e₀+h e₁` and a 32-byte masked message, and privately decodes `c₀h₀=e₀h₀+e₁h₁`. The 2860-byte CT difference at level 1 is exactly `668 B` from shorter dense ring element, `2176 B` from replacing HQC's `v` by a 32-byte mask, plus `16 B` salt/mask difference. BIKE's design has a difficult key-dependent iterative DFR; HQC's larger public-code construction avoids that exact secret-decoder dependence. NIST identified DFR analysis as the decisive reason for choosing HQC. Neither nonselection nor one weak-key result proves that all BIKE parameters are broken. [A 2026 CRYPTO paper](https://eprint.iacr.org/2025/1043) already studies shorter QC-MDPC syndrome systems with a closed-form decoder DFR **model**, so that direction is not an unoccupied invention.

Exact fixed-weight support entropies at level 1 are 622.952 bits for each HQC secret support and 694.542 for each ephemeral/error support; BIKE's total weight-134 error on length 24646 has support entropy 1196.018 bits. Since none of these raw supports is sent, ideal position coding gives no network saving. The generated HQC-1 ciphertext's Shannon entropy conditional on a fixed PK is at most 256 bits (`m` 128 + salt 128), owing to deterministic FO generation. That mathematical upper bound **does not provide a public short encoding**: sending the message/seed reveals the KEM secret, while publicly decoding an index of the dense image is the missing cryptographic mechanism. Full-alphabet padding slack is only a few bits; neither observation alone is a lower bound on all possible code-based KEMs.

The known QC representation has already reduced a systematic `r×r` binary matrix from about `r²` bits to one `r`-bit circulant description. Cyclic rotations also give attackers related targets; HQC's Section 6.3 accounts for a roughly `√n` DOOM gain in applicable ISD models. Key recovery, message decoding, low-weight dual search, distinguishing, rotation/folding and multi-user/reaction attacks must be evaluated separately. No new projection/orbit shortcut beyond known QC considerations is shown in this phase.

## Falsification outcome

The easiest arithmetic ≥20% saving would delete most/all of `v`; the resulting **secret-decoder syndrome architecture is BIKE-like**. An intermediate private hint may be interesting in the abstract, but no exact decoder, parameter set, key-conditioned DFR bound, attack estimate, or novel security reduction survives scrutiny. A publicly sent seed for the secret error immediately reveals it and allows decoding of `v`; an index of generated ciphertexts reveals `m` if it is just `(m,salt)`. The 16-byte salt and sparse-list coding do not reach a meaningful threshold. [QC-LDPC cryptanalysis](https://www.nist.gov/publications/cryptanalysis-ledacrypt) and [reaction attacks](https://eprint.iacr.org/2017/494) show why exposing or using secret sparse checks demands attack-first treatment.

This supports a **NO-GO on Phase 4 construction of a new QC-Hamming candidate**, not a claim that code-based cryptography is unpromising: the existing HQC selection has real hardness-family diversity from ML-KEM, and BIKE/2026 MDPC studies show smaller research systems at a correctness cost. `≤2 KB` total PK+CT is already below HQC-1's PK alone and below the current BIKE pair; no defensible path to it was identified. Investigating C7 class-group actions would require a separate, high-risk premise and cannot be justified merely by this pivot's failure. Under the original compact, mature and low-bloat objective, stop the search for a *new* primitive and compare/deploy existing standards and research systems appropriately.

## Verdict

**NO-GO — NO COMPELLING COMPACT QC-HAMMING MECHANISM**

### What mathematically causes HQC's large ciphertext?

Two approximately 17.7-Kbit dense terms: `u` for masking/cancellation and `v` for a very low-rate public RMRS code that corrects the composite error; the salt adds only 128 bits.

### How much is fundamental entropy versus current construction overhead?

Only a few bits are literal packing slack. The public-code redundancy is 17536 bits at level 1 and essential to this **decoder choice**, not a universal code-based lower bound. Generated ciphertext Shannon entropy is at most 256 bits conditional on PK, but no safe efficient public short encoding follows.

### Why is BIKE smaller?

It sends one dense QC element plus a 32-byte masked message and lets a **secret sparse-check decoder** recover the error, eliminating HQC's 2208-byte public codeword and using a shorter ring.

### What security/correctness cost does BIKE pay?

Key-dependent bit-flipping failures, weak keys/near-codeword error floors, reaction leakage, sparse dual recovery exposure and harder rare-tail/CCA analysis. NIST's decision was driven by DFR confidence, not proof of a universal BIKE break.

### What parameter first blocks aggressive HQC compression?

At fixed parameters, either dense component plus salt already exceeds 2 KB CT; removing code bits threatens decoder tolerance, while shortening the ring threatens QCSD margins. Which cryptographic bound fails first requires a particular proposed change.

### How close is current HQC to its information-theoretic representation bound?

For **full arbitrary `u,v` alphabets**, within at most a byte of padding per ring object. For the **generated ciphertext distribution**, very far in Shannon bits, but exploiting that gap efficiently without disclosing `m` is unresolved and is not a mere codec improvement.

### Did any seeded or implicit representation survive?

**No.** Public seed for the secret error reveals the mask. The existing seed for public `h` is already used. No invertible confidential image index was constructed.

### Did any message-embedding mechanism survive?

**No new one.** Syndrome/coset embeddings are established Niederreiter/BIKE territory, and no distinct secure public/secret split was proved.

### Did any decoder modification survive?

**No new one.** Published 2026 QC-MDPC decoder modeling is relevant prior art, but an independently validated new decoder with a per-key tail and advantage over it is absent.

### What is the best surviving attack against each mechanism?

M1: sparse parity-check/low-weight dual recovery and weak-key reaction attacks (plus ISD). M2: hint-based dual search and key-conditioned reactions, including multi-sample accumulation. M3: linearization/message exposure or generic syndrome ISD, depending on what is made public. Quantum ISD/list attacks require explicit memory assumptions.

### Is there a plausible <=2 KB total PK+CT code-based design direction?

**None established.** HQC-1 PK alone is 2241 B; BIKE-1 pair is 3114 B. The target requires a separately validated construction and attack model.

### Is there a >=20% improvement over current HQC communication?

**Yes in existing systems:** BIKE-1's raw pair is 53.3% smaller than HQC-1's, with a different DFR/security burden. **No new mechanism** meeting the audit's confidence and novelty conditions was identified.

### Should Phase 4 construct a concrete QC-Hamming candidate?

**NO.** Terminate the search for a new compact primitive under the present objective rather than pivot automatically to high-risk C7 class-group actions. Use standardized ML-KEM and follow the selected HQC standardization for hardness diversity; treat BIKE/MDPC advances as comparative research, not a ready replacement.
