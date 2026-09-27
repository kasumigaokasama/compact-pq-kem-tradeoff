# The compact post-quantum KEM trade-off: a falsification-led synthesis

**Final technical assessment · Evidence cutoff 27 September 2026**

## Abstract

We investigated why a post-quantum key-encapsulation mechanism (KEM) with substantially less communication than mature alternatives, modest computation and memory, simple constant-time implementation, and a credible chosen-ciphertext security argument is difficult to obtain simultaneously. A broad initial survey was followed by compact-NTRU, quasi-cyclic Hamming-decoding, and class-group/isogeny-action audits. The project reproduced selected DAWN packing and failure-*model* arithmetic, calculated representation bounds and QC support entropies, and attempted to falsify candidate compression mechanisms. Its decisive negative result is scoped: **no investigated mechanism passed all project gates for constructing a new compact KEM**. Existing compact designs exploit considerable obvious encoding slack; larger gains generally alter the decoder, assumption stack, quantum attack surface, or proof and validation burden. This is an empirical conclusion about the investigated families through the cutoff date, not an optimality theorem or a claim that future compact KEMs are impossible. The scientifically appropriate outcome is to terminate candidate construction while recording precise triggers for reopening the question.

## 1. Research question and original objective

The initial goal was a public-key primitive with approximately 128-bit post-quantum strength, short **public key and ciphertext together**, low CPU/RAM/stack cost, manageable constant-time implementation, and a defensible IND-CCA path based on a well-articulated average-case hard problem. The earlier informal ambition of being “unbreakable after quantum computers” cannot be a cryptographic guarantee. Security instead means resistance to specified classical and quantum attacks at explicit time, memory, query, depth and circuit costs under a stated assumption, security game and parameter distribution.

The central question is why this conjunction resists straightforward construction. A short encoding is only one coordinate; an attack may exploit the very algebra that made it short. An efficient secret decoder may make rare failures and chosen-ciphertext behavior the dominant issue. A one-curve key exchange is not automatically an IND-CCA KEM.

## 2. Methodology and evidence categories

**PROJECT-DERIVED RESULT** denotes calculations, experiments or branch decisions made in this project. **EXTERNAL LITERATURE RESULT** denotes a standard, paper, specification or attack with its actual scope. **INFERENCE** denotes an argument that combines those pieces but was not proved. **OPEN QUESTION** marks a missing theorem, source, estimator run or measurement. Confidence labels are **ESTABLISHED** for definitions, exact standard byte encodings or documented theorem/attack within their hypotheses; **STRONGLY SUPPORTED** for convergent but conditional evidence; **PROJECT-REPRODUCED** for our model calculations; **PLAUSIBLE** for argued extrapolations; **SPECULATIVE** for proposed mechanisms; and **UNKNOWN** where the required evidence is absent.

The project sequence was landscape triage → compact NTRU review → reproducibility and falsification → NTRU decision → QC-Hamming audit → group-action audit → this synthesis. Phase 2B explicitly recorded a *partial* validation, not a completed source freeze. Phase 2C formally returned **INSUFFICIENT EVIDENCE — PRIMARY VALIDATION STILL IMPOSSIBLE**, while also answering **NO** to constructing a new NTRU candidate. Phase 3 and 4A returned NO-GO under their respective construction gates. These distinct verdicts must not be flattened into “we broke every candidate.” Internal source anchors are listed in Appendix D and [PROJECT_TIMELINE.md](PROJECT_TIMELINE.md).

External time-sensitive facts were checked against NIST, author specifications, ePrint records and author communications through the cutoff date. An author's size or speed claim is attributed rather than silently upgraded to independent verification. We did not run a fresh full lattice or quantum ISD estimator.

## 3. Threat model and terminology

An adversary can see many public keys and encapsulations, select targets, query a decapsulation oracle in an IND-CCA game except on the challenge ciphertext, and exploit malformed inputs if validation is incomplete. The “post-quantum” evaluation includes classical algebraic and statistical attacks, quantum lattice/ISD/search/hidden-shift algorithms, precomputation and multi-target effects. Implementation attacks on timing, cache, power and faults are a separate but necessary deployment dimension. The NIST category labels are benchmarks and claim classes, not one universal number of quantum gates.

Decryption-failure probability (DFR) must be indexed by experiment: average over keys and encapsulations, conditioned on a particular key, conditioned on messages, or adversarial chosen inputs. An analytical upper bound, an approximation model and an empirical zero-failure observation are different evidence. A KEM's shared 32-byte output is locally derived and is **not** added to ciphertext network bytes.

## 4. What “compact” and “no bloat” mean

Use the vector

\[
B=(|PK|,|CT|,|SK|,T_{keygen},T_{enc},T_{dec},RAM,stack,C_{implementation},C_{validation},C_{proof},A_{assumptions},DFR).
\]

Report its coordinates, hardware and threat assumptions; never collapse it into a universal score. A small ciphertext with a quarter-megabyte public key is a different engineering point from moderate values for both. Public-key reuse changes the amortized network cost but not storage, certificate distribution, multi-user analysis or the first handshake. Decoder iterations, side-channel countermeasures, rejection paths and source-code audit surface are part of “bloat.” Neither theoretical communication entropy nor a seed for a secret-dependent object gives an efficient, publicly usable short representation for free.

## 5. Current PQC baselines

**EXTERNAL LITERATURE RESULT · STANDARD · ESTABLISHED:** NIST's [FIPS 203](https://csrc.nist.gov/pubs/fips/203/final) (August 2024) specifies ML-KEM-512/768/1024. Their (PK, CT, expanded DK, PK+CT), in bytes, are (800,768,1632,1568), (1184,1088,2400,2272), and (1568,1568,3168,3136). Module-LWE's noisy polynomial-module relation is compressed with a seeded public matrix and coefficient bit packing. At level 768, the public key is three 256-coefficient 12-bit polynomials plus a 32-byte seed: \(3\cdot256\cdot12/8+32=1184\) B. The ciphertext stores three 10-bit polynomials and one 4-bit polynomial: 1088 B. Encapsulation uses a carefully specified CCA transform with ciphertext validation and implicit rejection. This is a *standardized conditional-security design*, not mathematical optimality or immunity to leakage. NIST lists a future erratum, which does not erase the final-standard status.

**EXTERNAL LITERATURE RESULT · STANDARDIZATION STATUS · ESTABLISHED:** [NIST's project page](https://csrc.nist.gov/projects/post-quantum-cryptography) says HQC was selected for ongoing standardization; no final HQC FIPS is claimed here. [HQC's 22 August 2025 specification](https://pqc-hqc.org/doc/hqc_specifications_2025_08_22.pdf) gives level-1 2241 B PK, 4433 B CT, 6674 B combined, superseding older March 2025 figures. BIKE and Classic McEliece were not selected in that fourth-round outcome; nonselection is not a proof of insecurity.

FrodoKEM is a useful plain-LWE contrast: the June 2026 [CFRG draft](https://datatracker.ietf.org/doc/draft-longa-cfrg-frodokem/) gives FrodoKEM-640 PK 9616 B, CT 9752 B, combined 19368 B. Seeding its random matrix does not compress the remaining large noisy product. Classic McEliece's team [implementation table](https://classic.mceliece.org/impl.html) gives 261120 B PK and 96 B CT for mceliece348864, combined 261216 B: a tiny ciphertext paired with a large disguised decoder public key. The comparison is architectural, not a same-status contest.

## 6. Search space from Phase 1

The separately preserved Phase 1 project report, PQC-Phase-1-Research-Report.md, surveyed plain/ring/module LWE, LWR, NTRU, Hamming and rank decoding, multivariate trapdoors, group actions and isogenies, tensor isomorphism, graph/CSP, subset-sum, non-commutative algebra, hash/proof-system constructions and hybrids. It advanced C3 NTRU short relations, C5 quasi-cyclic Hamming decoding and C7 group actions to focused falsification, while retaining Module-LWE as a mature control. Tensor isomorphism was an exploratory control with no convincing compact KEM route.

The deciding filter was **UNKNOWN ≠ HARD**. NP-hard worst-case decision problems do not imply that a cryptographic *sampled public instance* is hard on average, that a secret can recover a hidden value efficiently, or that a clean CCA KEM follows. Graph planting can leak its planting, rank-metric algebra can reduce dimension, and an exotic non-commutative vocabulary can hide ordinary linear equations. A small public seed is useful only if it does not also regenerate the secret witness.

## 7. Failure patterns in historical cryptography

**Auxiliary public data exposes a trapdoor.** Castryck–Decru's [SIDH/SIKE attack](https://eprint.iacr.org/2022/975) uses transported auxiliary torsion-point images and known starting endomorphism structure with Kani's criterion; it is not an attack on every isogeny scheme. **Layered algebra leaks equivalent structure.** [Rainbow key recovery](https://eprint.iacr.org/2022/214) exploited oil/vinegar trapdoor structure. [HFEv−/GeMSS analyses](https://csrc.nist.gov/CSRC/media/Events/third-pqc-standardization-conference/documents/accepted-papers/petzoldt-efficient-key-pqc2021.pdf) illustrate reductions in claimed security, without equating them to Rainbow's practical laptop demonstration. **Average-case distributions fail to inherit generic hardness.** Rank-metric support/minor attacks repeatedly revise parameter estimates; basic [Merkle–Hellman](https://www-igm.univ-mlv.fr/~jyt/Crypto/crack_merkle_hellman.pdf) was broken by recovering disguised structure. **New language can conceal old attacks.** WalnutDSA and other non-commutative proposals require concrete representations and cryptanalysis rather than “non-commutative” as an assumption. **Failures create active channels.** A rare or key-dependent decoder failure can become a reaction oracle if decapsulation behavior leaks.

These are design warnings, not a statement that the modern families below inherit each historical break.

## 8. Compact NTRU investigation

**EXTERNAL LITERATURE RESULT:** Classical NTRU publishes a compact modular polynomial ratio, often \(h=g/f\pmod q\), making the secret pair a short lattice relation. NTRU HPS/HRSS, NTRU Prime (with a different quotient), CTRU/CNTR, NTRU+, BAT and DAWN use materially different samplers, rings, decoders or transforms; their byte counts and proofs cannot be interchanged. A polynomial public object and mature arithmetic initially made this branch compelling. NTRU Prime reduces selected ring attack surfaces, while BAT and DAWN show that sub-kilobyte combined raw API objects already existed in research.

The investigation evaluated key-relation recovery, equivalent short pairs, primal/dual and hybrid lattice attacks, automorphisms and CRT projection, ephemeral-message attacks, CCA behavior, DFR and quantum-assisted lattice/search models. No fresh comparable numerical estimator run was possible: the pinned lattice-estimator commit was identified but Sage was unavailable. The exact factorization of the 512-degree DAWN cyclotomic polynomial into 128 quartics at both \(q=257\) and \(769\) is **PROJECT-REPRODUCED**, not a projected key-recovery attack.

## 9. DAWN and BAT case studies

**DAWN · EXTERNAL LITERATURE RESULT · EPRINT/ASIACRYPT:** [Liu et al.](https://eprint.iacr.org/2025/1520) advertise double encoding, a zero-divisor/message quotient, rounding and mixed-radix packing. Their latest located ePrint revision is 27 October 2025. They claim IND-CPA under a specified NTRU *and* Ring-LWE assumption stack and an FO-derived IND-CCA KEM. DAWN-α-512 is reported at 615 B PK, 436 B CT (1051 B pair); DAWN-β-512 at 514 B PK, 450 B CT (964 B pair). These are scheme-paper claimed security levels, not ML-KEM-equivalent confidence.

**PROJECT-REPRODUCED:** An independent model of Phase 2A-transcribed Table 8 grouping reproduced the four object lengths 615, 436, 514 and 450 B. Exact integer \(\lceil512\log_2 M/8\rceil\)-type full-alphabet bounds leave *one byte per object*; an experimental bijective whole-vector codec makes β 513+449=962 B under the same alphabet, saving 2/964=0.2075%. Official wire compatibility was **not** tested because no authoritative vectors/code or canonical full text were available. This is serialization engineering, not a new hardness result. A ≥5% pair reduction would need about 49 B, far outside the modeled 2 B.

The limited algebraic skeleton was also checked: for \(y=x^{n/4},w=1+y,t=1+y^2\), \(w(y^2-y^3)=t\) in the integral negacyclic ring and \(t/w=y^2-y^3\) modulo odd \(q\). Reduction modulo \((2,t)\) reconciles a message residue, but centered lifts and a carry polynomial govern actual decryption. No full single-error decoder/correctness theorem or specification flaw was established. See [DAWN_CORRECTNESS_PROOF_AUDIT.md](DAWN_CORRECTNESS_PROOF_AUDIT.md).

**BAT · EXTERNAL LITERATURE RESULT:** [Fouque et al.](https://eprint.iacr.org/2022/031) use a short NTRU basis, small modulus and a distinct two-equation secret decoder; historical comparison gives 521 B PK and 473 B CT for BAT-512, with more involved key generation. The ePrint record explicitly notes a 12 April 2026 correction to a previous security-proof error. **OPEN QUESTION:** neither immutable full version required for a mathematical diff was accessible in the project. The changed lemma, reduction loss, assumption and parameter effect are **UNKNOWN**; we neither claim the corrected proof invalid nor manufacture its content.

## 10. DFR as a design constraint

**PROJECT-REPRODUCED:** A positive-convolution implementation of the DAWN authors' *independence model* matched their α and β log2 outputs to nine decimals: \(-132.676946974\) and \(-130.133613254\). A restricted paired \(n=512\) surrogate showed strong joint-tail dependence relative to a product-of-marginals approximation. The surrogate omits actual encoding, full fixed-weight dependencies and decoder behavior, so it is **not** a corrected DAWN DFR or an exploit. Actual average, per-key and adversarial-input tails remain **UNKNOWN**. Ordinary simulation cannot directly establish a \(2^{-130}\) event. [DAWN_DFR_FINAL.md](DAWN_DFR_FINAL.md) states the exact model and exclusions.

BIKE's sparse private iterative decoder has a different DFR problem: weak secret keys, error floors, decoder thresholds and reaction feedback can make an average number a poor bound for a target user. [NIST IR 8545](https://nvlpubs.nist.gov/nistpubs/ir/2025/NIST.IR.8545.pdf) records these concerns and why HQC was selected. HQC's public-code analysis is more stable by this comparison, while its own coefficient-independence simplification remains a limitation. Neither “modeled \(2^{-130}\)” nor “one million successful decapsulations” is a proven per-key \(2^{-130}\) bound. FO/QROM loss terms can amplify a correctness term; their exact constants must be checked for each transform.

## 11. NTRU falsification result

The research did **not** establish a ≥5% defensible new compact-NTRU mechanism. Pure packing left ~0.2% modeled β slack. Changing the quotient, rounding, decoder, alphabet or noise to gain meaningful bytes changes the error geometry, lattice instance, assumptions, and CCA reduction together. The missing DAWN canonical full text/reference implementation and BAT proof versions prevented theorem-level validation. Hence the formal Phase 2C status is **INSUFFICIENT EVIDENCE**, with **NO** construction recommendation. This is **STRONGLY SUPPORTED design-space saturation evidence for obvious local changes**, not a universal NTRU optimality proof or a claim that NTRU is poor.

## 12. QC-Hamming investigation

The next branch was chosen for assumption diversity: hard low-weight syndrome recovery, with quasi-cyclic (QC) representation replacing a generic quadratic-size matrix by circulant blocks. The audit covered HQC, BIKE/QC-MDPC and Classic McEliece, support entropy, ciphertext anatomy, quantum/classical ISD, rotations, low-weight dual search, decoder weak keys and failures.

**EXTERNAL SPECIFICATION RESULT:** For HQC-1 the 2025 public key consists of a 32 B seed for public \(h\) plus a dense 2209 B syndrome \(s=x+h y\). Its 4433 B ciphertext is a dense 2209 B \(u=r_1+h r_2\), a dense 2208 B noisy public-code word \(v=C(m)+\mathrm{Truncate}(s r_2+e)\), and a 16 B salt. The codeword carries 17536 redundant bits for a 128-bit message; this redundancy supports reliable decoding of compound noise. The large ciphertext is chiefly a functional representation choice, not byte padding. Only a few padding bits remain in its packed dense fields.

**PROJECT-REPRODUCED:** Exact fixed-weight combinatorics give \(\log_2\binom{17669}{\omega}\approx622.952\) bits for each HQC-1 secret support and ~694.542 bits for each ephemeral support; BIKE's joint weight-134 error support has ~1196.018 bits. Those supports are *not sent*. Compressing them does not shrink dense \(s,u,v\). At fixed HQC PK, the deterministic encapsulation image has at most \(128+128=256\) bits of entropy in message plus salt; sending their seed/preimage would disclose the secret. Shannon entropy alone does not furnish an efficient public inversion-free encoder. [QC_ENTROPY_ANALYSIS.md](QC_ENTROPY_ANALYSIS.md).

## 13. HQC versus BIKE and QC-Hamming verdict

BIKE's level-1 research encoding is 1541 B PK + 1573 B CT = 3114 B. Its ciphertext sends one dense syndrome and a 32 B masked message; the private sparse QC-MDPC structure performs iterative decoding. The 2860 B CT difference from HQC comprises 668 B shorter first dense object, 2176 B replacing HQC's 2208 B \(v\) by a 32 B mask, and 16 B salt/mask difference. That is a concrete bandwidth gain with a more difficult per-key DFR and reaction analysis, not the absence of a CCA transform. [HQC_VS_BIKE.md](HQC_VS_BIKE.md), [BIKE implementation table](https://openquantumsafe.org/liboqs/algorithms/kem/bike.html) (table notes an older 5.1 implementation/security-model label; do not equate it automatically to all v5.2 proof claims).

The attempted ≥20% HQC saving by removing \(v\) led back toward existing secret-decoder/BIKE territory. Publicly sending the sparse-error seed exposes it; replacing \(u,v\) by \((m,salt)\) exposes the KEM preimage; a partial secret hint introduces a new structural and weak-key burden. No novel ≤2 KB PK+CT code-based direction with the demanded evidence survived. The Phase 3 outcome was **NO-GO**, not a rejection of code-based cryptography. The [2026 QC-MDPC DFR work](https://eprint.iacr.org/2025/1043) further shows this is active prior art, not an empty novelty slot.

## 14. Group-action investigation

Class-group actions offered the most dramatic *mathematical public-object* compactness, so Phase 4A examined CSIDH, CSURF, CTIDH/dCTIDH, oriented actions/PEGASIS and the newer module-action MIKE proposal. For a regular abelian action \(G\curvearrowright X\), vectorisation recovers an action from \(x,a\cdot x\); parallelisation computes \((ab)\cdot x\) from \(x,a\cdot x,b\cdot x\). A key exchange relies on the latter and does not inherit its hardness from vectorisation alone. CSIDH's historical 512-bit field gives a 64 B curve encoding; that fact does not settle PQ128 security.

Castryck–Decru's SIDH prerequisites—the public transported torsion basis and known starting structure—are absent from a bare CSIDH coefficient and the 2024 MIKE single \(j\)-invariant proposal. The attack thus does not mechanically transfer. The broader lesson is that small public objects can hide large security assumptions; adding helpful auxiliary curves may itself become an attack input.

## 15. CSIDH quantum trade-offs

Regular abelian actions admit a hidden-shift/dihedral-hidden-subgroup formulation. Kuperberg-family algorithms give resource vectors, not one agreed “security bits” figure. [Bonnetain–Schrottenloher](https://zhengxuisogeny.github.io/Isogeny-Based-Cryptography/index/quantumcsidh.pdf) model CSIDH-512 trade-offs (log2 oracle queries, T gates, classical time, quantum memory) of (33,85.6,33,31), (19,71.6,86,<15.3) and (24,76.6,63,<15.3). Their ~52.6-log coherent oracle T-gate contribution is included; an oracle implementation discussion cites ~40,000 logical qubits separately. The [CSIDH team's response](https://csidh.isogeny.org/analysis.html) disputes some oracle accounting. These are attack-model estimates, not a demonstrated physical break. A [2025 shifted-input analysis](https://eprint.iacr.org/2025/376) finds much lower modeled costs when thousands of related curves are public; those numbers must **not** be pasted onto ordinary two-object CSIDH.

The same paper's illustrative aggressive ~2260-bit and conservative ~5280-bit fields yield ~283 and ~660 B per raw curve, or ~566 and ~1320 B for two exchanged curves before CCA fields; these parameter choices depend on different attack-resource metrics. Larger fields increase honest arithmetic and validation costs. [dCTIDH](https://eprint.iacr.org/2025/107) reports 1.695 billion cycles per action at 2048-bit scale; a [hardened variant](https://arxiv.org/abs/2509.12877) reports ~1.59–1.60 billion cycles and ~357k–362k field multiplications under its benchmark. These are neither matching PQ128 certifications nor complete KEM times. Phase 4A therefore rejected a straightforward new regular-action KEM under the project gates.

## 16. MIKE as a future research signal

[Robert's 2024 module-action paper](https://eprint.iacr.org/2024/1556) extends ideal actions to Hermitian-module actions; ⊗-MIKE sends only a supersingular \(\mathbb F_{p^2}\) curve's \(j\)-invariant (claimed 64 B at level 1), avoids SIDH torsion images, and computes a shared dimension-four variety. Its argument that the ordinary Kuperberg formulation *presumably* does not apply is a structural observation, not a concrete quantum lower bound. The [July 2026 MIKE team announcement](https://mailarchive.ietf.org/arch/msg/cfrg/QM3t6di1bsgla6iIJ3gN6BbDoVk/) claims 64 B Level-1 keys, <1 ms keygen and <5 ms full key exchange including \(\mathbb F_{p^2}\) supersingularity validation on a named Ryzen laptop, constant-time Rust code, an active NIKE result, and an algebraic-isogeny-model reduction for passive NIKE/KEM from a supersingular endomorphism-ring problem. These are **AUTHOR CLAIMS** where no independent matching benchmark/full team KEM audit was available.

The 64+64=128 B raw two-object exchange is an **INFERENCE**, not a complete IND-CCA byte count. Independent quantum cryptanalysis, assumption history, full IND-CCA algorithms/reduction and QROM losses, and exact CT serialization remain **OPEN QUESTIONS**. MIKE is a **PROMISING RESEARCH SIGNAL**, neither demonstrated insecure nor deployment-ready.

## 17. Why NIKE is not an IND-CCA KEM

A passive exchange can derive a shared invariant from recipient public \(a\cdot x\) and encapsulator public \(b\cdot x\); an adaptive adversary can submit arbitrary malicious objects to decapsulation. The implementation must check canonical curve/object membership and any supersingularity/orientation/endomorphism conditions, bind recipient/context/ciphertext, use a suitable implicit-rejection behavior, and prove indistinguishability under chosen-ciphertext queries. FO-style transforms generally require a correct PKE with decryptable seed/message and deterministic reencryption from derived coins, not merely a bare hashed NIKE. ROM and QROM are distinct proof settings; reduction losses and failures can dominate.

**OPEN QUESTION:** No project-audited MIKE construction supplies complete IND-CCA bytes and proof. A 2022 [CSIKE paper](https://doi.org/10.1515/jmc-2022-0007) already claims a CSIDH-based CCA KEM with an extra tag, so “apply FO to CSIDH” is not novel; its modern PQ128 matched parameter, complete byte and QROM evidence were not verified in this project. Short key exchange therefore does not by itself establish compact, defensible KEM communication.

## 18. Implementation surfaces

ML-KEM demands modular polynomial arithmetic, sampling, hashing, compression, canonical parsing, constant-time decapsulation and side-channel engineering. QC systems demand binary polynomial operations, decoders, failure control and constant-time rejection; sparse private decoders add key-specific timing/reaction risk. Group actions demand large-field arithmetic, isogeny chains, torsion computations, supersingularity/orientation/domain validation, and fault resistance. [Disorientation-fault work](https://ir.cwi.nl/pub/33834) and hardened CTIDH show that “constant time” alone is not the full fault story. No equal-platform peak RAM/stack and audited code-complexity dataset was produced for all rows, so these are implementation surfaces, not a numeric winner ranking.

## 19. Cross-family map

| System | Communication region | Assumption / quantum analysis maturity | Correctness burden | Implementation surface |
|---|---|---|---|---|
| ML-KEM | moderate PK and CT | standardized Module-LWE, extensive analysis | specified negligible failure and CCA handling | polynomial arithmetic, side-channel controls |
| FrodoKEM | large PK and CT | relatively conservative plain LWE | decoder/reconciliation proof | large matrix arithmetic and RAM |
| DAWN | ~1 KB pair claim at α/β level 1 | newer NTRU+Ring-LWE design, incomplete independent validation | rare correlated DFR unresolved | compact codec and decoder |
| BAT | ~1 KB pair historical | NTRU proof corrected 2026; theorem diff unknown | distinct secret basis decoder | complex keygen |
| HQC | ~6.7 KB pair in 2025 spec | NIST selected, code/ISD analysis | public-code DFR model | dense binary algebra/code decoder |
| BIKE | ~3.1 KB pair research | QC-MDPC, weak-key scrutiny | private iterative decoder and rare tails | decoder/fault control |
| Classic McEliece | huge PK, tiny CT | long study plus 2026 new structural preprints | valid ciphertext decoding without DFR | expensive key handling |
| CSIDH/CTIDH | ~128 B historical raw; enlarged raw ~566–1320 B | regular-action hidden shift disputed concretely | validation and CCA route unknown | expensive actions |
| MIKE | ~128 B raw inference; CCA unknown | new module action, independent quantum margin unknown | domain validation; CCA unspecified | author-reported fast high-dimensional actions |

Sizes refer to *different status levels* and may be raw NIKE rather than complete KEM. The complete numeric ledger with exact source versions and unknown cells is [CROSS_FAMILY_COMPARISON.md](CROSS_FAMILY_COMPARISON.md). There is no global ranking.

## 20. The compact post-quantum trade-off

**INFERENCE · STRONGLY SUPPORTED AS AN OBSERVED PATTERN, NOT A THEOREM:** The investigated families expose recurrent exchanges between exploitable structure, representation length, decoder complexity, assumption maturity, quantum analysis and CCA implementation. More regularity can make honest multiplication and representation cheap while giving attackers automorphisms, projections or hidden shifts. Less algebraic structure can cost bandwidth, as in FrodoKEM or Classic McEliece. Stronger secret-assisted decoding can eliminate a transmitted public codeword while creating weak-key and failure tails, as HQC versus BIKE illustrates. Tiny curve objects can shift cost into expensive evaluation, validation or novel hardness assumptions. A zero-byte “CCA overhead” cannot be inferred where no complete KEM exists.

This is a map of *mechanisms* and evidence costs, not a monotonic security/size law. It does not assert that every future compact design must fail. [COMPACT_PQ_TRADEOFF.md](COMPACT_PQ_TRADEOFF.md) formalizes the vector and the boundaries.

## 21. Why no new primitive was proposed

Inventing a cipher to satisfy an output target would invite parameter cherry-picking, concatenating unproved assumptions, overlooking DFR and treating an unfamiliar group or tensor as proof of hardness. Each apparent shortcut failed an immediate falsification: a two-byte DAWN codec gain is engineering; HQC sparse supports are not transmitted; BIKE-like removal of a codeword is already researched and correctness-sensitive; historical 64 B CSIDH parameters have quantum-resource controversy; MIKE's full CCA KEM and concrete quantum story remain immature. Terminating these branches is the research contribution. It prevents a construction with impressive bytes but a missing security case.

## 22. What a future breakthrough would need

A genuinely better KEM would need an efficiently samplable *average-case* public relation with a compact description, an efficient secret-assisted recovery operation, no cheaply exploitable symmetry or helper-data leakage, low/zero and preferably per-key bounded failure, credible classical and fault-tolerant quantum resource estimates, practical constant-time validation, low RAM/runtime, and a clean IND-CCA reduction with measured complete objects. Worst-case reductions would help where applicable, but only under distributions and parameters that actually match the scheme. No investigated new problem was shown to meet this conjunction. A mathematical advance could be a new hard-instance distribution/decoder theorem, an unexpectedly tight quantum bound for a non-regular action, or a compact CCA conversion proven without costly auxiliary data; these are requirements, not designs.

## 23. Open questions

Can a short public instance encode a secret-recoverable hard relation without useful attacker symmetry? Can BIKE-like communication coexist with a rigorous rare per-key DFR and reaction-resistant decoder? Can DAWN's real correlated tail be bounded beyond the author's independence model? What exactly changes in BAT's corrected game sequence? Can MIKE gain independent concrete quantum cryptanalysis and an exact compact IND-CCA/QROM construction? Can family-specific lower bounds relate encoding, ciphertext correctness and attack structure? Can quantum ISD and hidden-shift models be reconciled with hardware-relevant depth/memory? See [OPEN_RESEARCH_QUESTIONS.md](OPEN_RESEARCH_QUESTIONS.md).

## 24. Future trigger conditions

Reopen only for new evidence that could change a specific gate: independent MIKE security and complete CCA specification, a new group-action quantum attack, canonical DAWN implementation/full-text plus correlation-aware DFR bounds, the versioned BAT proof diff, a rigorously bounded QC decoder at BIKE-like cost, major revised lattice/ISD cost estimates, or a fundamentally new average-case problem with an asymmetric recovery theorem. New NIST status alone affects engineering guidance but does not retroactively prove a speculative construction. [FUTURE_TRIGGER_CONDITIONS.md](FUTURE_TRIGGER_CONDITIONS.md) assigns each trigger to the affected conclusion.

## 25. Limitations

The Phase 1 survey is targeted rather than exhaustive. Full primary texts were inaccessible in some earlier phases, notably canonical DAWN and version-paired BAT proof files. Phase 2A used a noncanonical manuscript transcription for specific DAWN grouping and algebra; later code reproduced its arithmetic, not official wire compatibility. An author's DFR approximation was reproduced, not the real correlated distribution. No full independently executed lattice estimator, quantum ISD run, physical quantum hardware experiment, formal proof, or complete measured RAM/stack comparison exists. The 2026 McEliece preprints contain provable distinguisher and heuristic recovery claims of different scope; neither is shown to practically break Classic McEliece's deployed parameters here. MIKE's speed and proof statements are author communications, not independently benchmarked complete CCA KEM results. BAT's theorem-level correction is unknown, and concrete MIKE quantum margin is unknown. These limits constrain the verdict; they do not justify a positive construction by default.

## 26. Conclusion and engineering recommendation

**No new KEM was identified as worth constructing under the project's requirements.** Within the investigated design space and evidence through 27 September 2026, no new mechanism combined a material PK+CT gain, credible PQ security, adequate assumption maturity, practical implementation and a defensible CCA path. The generalizable result is a recurring compactness/security/maturity trade-off, not an impossibility theorem and not proof that ML-KEM is optimal. For systems requiring PQ key encapsulation now, use standardized, reviewed constructions such as FIPS 203 ML-KEM, with normal protocol, validation and side-channel controls; [FIPS 203](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.203.pdf) recommends ML-KEM-768 as a default, while this paper often uses ML-KEM-512 only as a level-1 size control. HQC is a selected code-based diversification candidate in an ongoing standardization process; DAWN, BAT, BIKE and group-action work retain their research qualifications. The project's stop rule closes new-primitive construction until a concrete trigger changes the evidence.

## 27. References

The numbered, source-classified bibliography and version notes are in [REFERENCES.md](REFERENCES.md). Every cited external result above is linked to a primary standard, author paper, specification, repository or author communication. Project files are internal evidence rather than independent literature.

## Appendix A. Byte accounting

[CROSS_FAMILY_COMPARISON.md](CROSS_FAMILY_COMPARISON.md) lists PK, CT, combined and unknown overhead with source/version. [GROUP_ACTION_BYTE_LEDGER.md](GROUP_ACTION_BYTE_LEDGER.md), [HQC_BYTE_LEDGER.md](HQC_BYTE_LEDGER.md), and [DAWN_CODEC_ANALYSIS.md](DAWN_CODEC_ANALYSIS.md) give component equations.

## Appendix B. Attack ledgers

[ATTACK_ESTIMATOR_RESULTS.md](ATTACK_ESTIMATOR_RESULTS.md) records the unrun lattice-estimator gate; [ISD_ATTACK_LEDGER.md](ISD_ATTACK_LEDGER.md) distinguishes code attacks; [QUANTUM_HIDDEN_SHIFT_LEDGER.md](QUANTUM_HIDDEN_SHIFT_LEDGER.md) holds vector costs and oracle caveats.

## Appendix C. Evidence and confidence

[EVIDENCE_LEDGER.md](EVIDENCE_LEDGER.md) maps every decisive claim to project/source, confidence and unresolved issue, including model-versus-real-DFR boundaries.

## Appendix D. Reproduction notes

The original scripts are `experiments/dawn_codec.py`, `test_dawn_codec.py`, `reproduce_dawn_dfr_model.py`, `paired_noise_check.py`, `toy_correlation.py`, `ring_structure.py` and `qc_entropy_frontier.py`. [EVIDENCE_LEDGER.md](EVIDENCE_LEDGER.md) records their inputs, observed outputs and limitations. The script bundle is project evidence, not a reference KEM implementation.

## Appendix E. Falsified mechanisms

[NTRU_RESEARCH_MECHANISMS.md](NTRU_RESEARCH_MECHANISMS.md), [QC_RESEARCH_MECHANISMS.md](QC_RESEARCH_MECHANISMS.md), [GROUP_ACTION_RESEARCH_MECHANISMS.md](GROUP_ACTION_RESEARCH_MECHANISMS.md), and their rejected-ideas ledgers document disproof tests. No mechanism is promoted to a KEM proposal.
