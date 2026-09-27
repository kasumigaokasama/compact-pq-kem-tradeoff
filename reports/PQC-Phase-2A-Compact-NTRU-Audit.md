# Phase 2A — Compact NTRU KEM research audit

**Status:** substantive research audit, 27 September 2026. **Scope:** published NTRU-family KEMs and the engineering/security tradeoffs behind short public keys and ciphertexts. This is not a new KEM proposal or an independent security proof. A precise audit of the 12 April 2026 BAT proof correction remains open because the corrected full text could not be inspected reliably; the ePrint record confirms the revision and describes it as fixing an error in the earlier security proof [2].

## A. Decision-oriented summary

At the claimed NIST category I level, DAWN-α-512 reports a **436-byte ciphertext** and **615-byte public key**. DAWN-β-512 reports **450 + 514 = 964 bytes** for ciphertext plus public key. Both use a 512-coefficient negacyclic ring and a message space of 128 bits. These are paper parameter claims, not standardization or independent validation [1].

The byte results are not unexplained constants. DAWN uses a small quotient for the message, a polynomial multiplier that allows a restricted error decoder, rounding, and mixed-radix coefficient packing. Its CPA argument is conditional on *both* decisional NTRU and decisional Ring-LWE for the specified small-polynomial distributions; the KEM adds an FO-style reencryption check and implicit rejection. The quoted decryption-failure probabilities are estimates using coefficient-independence approximations, not exact exhaustive probabilities [1].

BAT-512 is a different compactness route: a short NTRU trapdoor basis and two-equation decoding, with a reported 521-byte public key and 473-byte ciphertext in the DAWN comparison [1,2]. Its key generation is comparatively costly. A correction to BAT's security proof dated 12 April 2026 is a real version gate, so older theorem statements must not silently be treated as the corrected theorem [2].

**Research priority:** establish a version-locked baseline for DAWN and BAT, independently reproduce packing and decryption-failure tails, and rerun current attack estimators against the actual distributions. Do not select a variant by ciphertext length alone.

## B. Sources, versions, and evidence rule

| Item | Version/date used | Evidence used here | Caveat |
|---|---|---|---|
| DAWN, Liu et al. | ASIACRYPT 2025; ePrint 2025/1520 | Accessible manuscript reproduction, including algorithms, Tables 1, 6, 8, 9 and proof sketches [1] | Reproduction is not the canonical version; check against authors' immutable PDF before formal claims |
| BAT, Fouque et al. | TCHES 2022 and ePrint 2022/031, revised 2026-04-12 | ePrint metadata and historical paper [2,3] | Corrected proof's precise changed game, hypothesis and bound unverified |
| ML-KEM | NIST FIPS 203, 2024 | Normative standard [4] | Different hardness family and validation status |
| NTRU HPS/HRSS | Round-three submission specification, 2020 | Scheme specification [5] | Historical candidate, not FIPS 203 |
| NTRU Prime | Round-three specification, 2020 | Scheme submission [6] | Different ring and threat tradeoffs |
| CTRU/CNTR | 2022 paper | Author preprint [7] | Paper estimates and implementations need version matching |
| NTRU+ | 2026 competition specification | Project's current specification [8] | Version has changed over time; pin exact download for reproducibility |

An exact packet budget includes framing, parameter identifiers, negotiation, authentication, retransmissions and hybrid components only if the protocol actually transmits them. The tables here compare raw KEM API objects; the 32-byte shared secret is derived locally and does **not** get added to on-wire ciphertext size. A stored expanded secret key, a seed, and a transmitted public key are three different metrics.

## C. Common mathematical model

Let \(R_q=\mathbb Z_q[x]/\Phi(x)\), with \(n=\deg\Phi\), and let a NTRU public key be \(h=g f^{-1}\bmod(q,\Phi)\) for suitably small and invertible \(f,g\). A public relation \(fh-g\equiv0\pmod q\) defines a structured lattice. One convenient coefficient-lattice representation is the integer span of the rows of \(\begin{pmatrix}I&H\\0&qI\end{pmatrix}\), with \(H\) the convolution matrix for multiplication by \(h\); transpose and sign conventions vary. The secret pair supplies a short vector or, for BAT, a short basis. A lattice estimator is meaningful only with the actual ring, distributions, embeddings, dimensions, success criterion and available samples.

Security claims must separate: (i) recovering \(f,g\) or an equivalent secret, (ii) distinguishing the public ratio from uniform, (iii) recovering an ephemeral message from one ciphertext, (iv) chosen-ciphertext manipulation and reaction attacks, and (v) implementation leakage. A bound for one goal is not automatically a bound for another.

## D. DAWN mechanism and a proof-reading question

DAWN uses \(\Phi=x^n+1\), \(n\) a power of two, a small quotient modulo \((t,p)=(x^{n/2}+1,2)\), and \(w=x^{n/4}+1\). In characteristic two, \(t=w^2\); the message has \(n/4\) binary coefficients. Encryption samples short \(s,e\) and rounds a polynomial of the form

\[
c=\left\lfloor hs+e+w^{-1}m\pmod{(q,x^n+1)}\right\rceil_{d_c}.
\]

The receiver scales the rounded ciphertext, multiplies by \(tf\), reduces in the appropriate quotient, and applies a decoder designed to tolerate at most one residual error of the advertised form. The KEM derives randomness from the message and public-key hash, then reencrypts and compares the ciphertext; on failure it derives the fallback key from secret fallback material and the ciphertext [1]. **Implementation gate:** check canonical encodings, a constant-time comparison, the exact failure path, and the hash/domain-separation inputs.

The generic double-encoding derivation and instantiated encryption formula use notation that merits direct algebraic reconciliation: the general identity is expressed using \(t^{-1}w\), whereas the displayed instantiation encrypts \(w^{-1}m\) and decrypts after multiplying by \(t\). Because \(t=w^2\) modulo 2 but not necessarily as a polynomial identity over \(\mathbb Z_q\), a careful lift and reduction argument is required. This is a **proof-reading question**, not a demonstrated vulnerability. The reproduced text contains conversion artifacts, so resolve it against the canonical manuscript and reference code before drawing stronger conclusions [1].

The CPA game hops replace the NTRU public ratio by a uniform element and the Ring-LWE mask by a uniform element. The FO conversion adds a QROM reduction with a correctness/failure term. Such a theorem is conditional: the decisional distributions and the random-oracle model are part of the statement, and numerical attack costs are separate from it [1].

## E. Exact DAWN byte ledger

The paper's Table 8 groups five base-769 coefficients into 48 bits for α public keys and five base-110 coefficients into 34 bits for α ciphertexts. For β it factors 258 = 3·86 for the public key and 129 = 3·43 for the ciphertext, groups the base-3 stream in blocks of 17 (27 bits), and the other stream in blocks of 7 (45 or 38 bits). Final partial blocks account for the nonintegral group counts [1]. The following independently recomputes the **bit budget implied by those grouping rules**; it does not independently verify canonical serialization or implementation interoperability.

| Object | Full groups and remainder | Bits | Bytes |
|---|---|---:|---:|
| α-512 public key, base 769 | 102×48 + 2 coefficients requiring ⌈log₂(769²)⌉=20 | 4,916 | **615** |
| α-512 ciphertext, base 110 | 102×34 + 2 coefficients requiring ⌈log₂(110²)⌉=14 | 3,482 | **436** |
| β-512 public key, base 3 and 86 | 30×27 + 2×2; 73×45 + 1×7 | 4,106 | **514** |
| β-512 ciphertext, base 3 and 43 | 30×27 + 2×2; 73×38 + 1×6 | 3,594 | **450** |

For example, \(\lceil3482/8\rceil=436\). The β sum is \(514+450=964\) bytes. A common accounting mistake would use \(\lceil\log_2 769\rceil=10\) bits independently for every coefficient and miss mixed-radix packing. Another would call β's 964 bytes a ciphertext length; its ciphertext is 450 bytes. Table 9 also reports expanded private-key lengths of 1,319 bytes for α-512 and 1,154 bytes for β-512 [1].

| Comparator, category-I-oriented | Public key | Ciphertext | Sum | Status/qualification |
|---|---:|---:|---:|---|
| DAWN-α-512 | 615 | 436 | 1,051 | Paper claim; DFR estimate ≈2⁻¹³³ |
| DAWN-β-512 | 514 | 450 | **964** | Paper claim; DFR estimate ≈2⁻¹³⁰ |
| BAT-512 | 521 | 473 | 994 | Historical comparison; corrected proof gate |
| CTRU-512 / CNTR-512 | 768 | 640 | 1,408 | Author-paper comparison, distinct security estimates |
| NTRU-HPS-677-2048 | 930 | 930 | 1,860 | Historical NTRU submission |
| NTRU-HRSS-701 | 1,138 | 1,138 | 2,276 | Historical NTRU submission |
| ML-KEM-512 | 800 | 768 | 1,568 | NIST standardized |

The comparative DAWN table supplies the NTRU figures [1]; FIPS 203 supplies ML-KEM [4]. A category label or one paper's security estimate does not establish equal real-world confidence across designs. For reference, ML-KEM-768 is 1,184-byte public key and 1,088-byte ciphertext; ML-KEM-1024 is 1,568 and 1,568 bytes [4].

## F. Other compact NTRU routes

**Classical NTRU HPS/HRSS.** A power-of-two \(q\), ternary secrets and carefully designed encodings permit reliable decapsulation without DAWN's aggressive ciphertext rounding. Larger raw objects buy a different correctness/security margin. HPS and HRSS differ in distributions and transforms; avoid treating the family as one parameter set [5].

**NTRU Prime / sntrup.** Uses a different polynomial quotient, notably avoiding the power-of-two cyclotomic structure DAWN deliberately exploits. This changes algebraic attack exposure and arithmetic cost. Published sntrup761 raw key/ciphertext lengths and secret-key layout should be taken from its precise submission version; a seed-only private key is not the same measure as an expanded API key [6].

**BAT.** BAT employs a full short NTRU basis \((f,g,F,G)\), with \(gF-fG=q\) under one convention, to solve two equations for message and error. A smaller modulus and decoder help the ciphertext budget; sampling a suitable trapdoor basis makes key generation much costlier. The published comparison gives 521/473 bytes for BAT-512. Its old security argument and the corrected 2026 version must be diffed before using any theorem-level guarantee [1–3].

**CTRU/CNTR.** These encode and compress a single ciphertext polynomial; the authors report 768/640 bytes at their 512 sets and 1,152/960 at their 768 sets. They involve their own coding and failure analyses and are neither aliases for DAWN nor for BAT [1,7].

**NTRU+.** The competition specification uses a distinct ring and code construction. Parameter, implementation and proof claims must be pinned to its final 2026 version [8]. It is a comparison candidate, not evidence that any particular DAWN or BAT bound transfers.

## G. Decryption failure, FO conversion and chosen-ciphertext exposure

DAWN's paper separates two decoder events: more than one out-of-range residual coefficient, and selecting the wrong one of four candidate positions when a single error is corrected. Its estimate builds a coefficient distribution for the effective noise, assumes independent coefficients for a binomial tail, and sums the two event estimates. It reports approximately 2⁻¹³³ for α-512 and 2⁻¹³⁰ for β-512 [1]. The independence model deserves independent evaluation because negacyclic products, fixed-weight sampling and rounding produce correlations. A million successful trials cannot establish a 2⁻¹³⁰ tail.

If the KEM reduction contains a term proportional to an adversary's number of quantum hash queries times \(\sqrt\delta\), substitute the **actual** correctness bound and the intended query budget. For example, a bound based on \(\delta=2^{-130}\) has \(\sqrt\delta=2^{-65}\); that is a very different exponent from the bare failure probability. This arithmetic illustrates the proof term, not an attack cost or a final security estimate. Compare the exact theorem's constants, query domains and failure conventions [1].

FO reencryption must compare exact serialized ciphertexts and use secret-dependent rejection without an externally visible signal. Timing, malformed encodings, cache behavior, and decapsulation response differences may turn tiny nominal failure probabilities into exploitable reaction channels. Perform constant-time and fault-injection analysis separately from the mathematical DFR estimate.

## H. Attacks and quantum assessment

The baseline review should include primal and dual lattice attacks on the specific NTRU/RLWE distributions, hybrid guessing of sparse positions, subfield/automorphism and algebraic attacks for the chosen ring, decoding/message-recovery attacks, multi-target reuse, and active decapsulation attacks. Recompute estimates with a pinned estimator revision and published cost model, reporting classical and quantum costs, memory, block size and success probability. A single “security bits” column conceals assumptions and cost-model uncertainty.

Grover search gives a generic square-root search effect under its oracle model; it does not simply halve every lattice-attack exponent. Quantum sieving, enumeration, memory and circuit-depth assumptions require explicit models. The generic statement “based on NTRU” does not prove resistance to a specific future quantum algorithm. Ring choice and small secret distributions can change both attack and reduction behavior [1,5–7].

## I. Implementation and reproducibility gates

1. Obtain a canonical, hash-pinned DAWN manuscript and matching code revision. Reconcile Algorithm 4's inverse, the general encoding identity, all sign/quotient conventions and the exact wire format.
2. Diff BAT ePrint versions immediately before and after 12 April 2026. Identify the erroneous lemma/game hop, the corrected assumption, the new advantage loss and any changed parameters. Until then, label its security proof **unverified under the correction**.
3. Implement an independent pack/unpack oracle for all four 512 DAWN objects. Test last partial groups, rejection of noncanonical values and full round trips; compare bytes against reference vectors.
4. Reproduce DAWN's full effective-noise distribution including fixed-weight dependencies and rounding. Use analytical bounds or importance sampling for ultra-rare tails; report confidence and any independence gap.
5. Pin lattice-estimator code, hardware, compiler and hash primitives for benchmark comparisons. Separate one-time key generation from repeated encapsulation, and compare protocol packet budgets only after including the actual framing.

## J. Research hypotheses, with disproof tests

| Hypothesis | Possible gain | Fastest decisive challenge |
|---|---|---|
| Alternative small quotient/code within DAWN's double-encoding framework | Better error tolerance at equal ciphertext alphabet | Derive exact decoding radius, check lift/algebra, then show a lower total byte budget *after* metadata and failure bound; reject if reduction changes or decoding ceases to be constant time |
| Improved coefficient grouping and canonical codec | Recover a few packing bits without touching algebra | Exhaustive group counting, round-trip/reference vectors and time/memory measurements; reject if saved bytes vanish at packet boundary or noncanonical decodings appear |
| Carefully adjusted rounding or noise weights | Lower ciphertext size | Recompute both lattice and decoder distributions, QROM failure term and chosen-ciphertext behavior; reject if any bound or cost model worsens |
| Batched/ephemeral-key deployment of α | Amortize a 615-byte public key over multiple encapsulations | Model actual protocol reuse, multi-target attacks, authentication and replay; reject if reuse changes threat model or β wins under realistic session count |

These are research questions, not parameter recommendations. No conjectured saving should be advertised before an independently reproducible attack and correctness review.

## K. Stop conditions and practical choice

Stop a line of optimization if it needs an unexamined stronger hardness assumption, if its DFR rests only on unvalidated coefficient independence, if canonical ciphertext validation is ambiguous, if current attacks fall below the declared category in any reasonable cost model, or if the claimed byte saving depends on omitting a required protocol field. BAT's proof-correction gate and DAWN's exact algebra/codec gate are immediate blockers for a formal recommendation.

For an application requiring a standardized, deployable baseline, use FIPS 203 ML-KEM as the reference point [4]. For research into raw lattice KEM size, prioritize DAWN's independently checkable 436-byte ciphertext and β's 964-byte combined objects. Treat BAT as a serious comparator once the corrected proof has been audited. Neither conclusion equates a short encoding with a completed security review.

## L. References and provenance

1. Y. Liu, Y. Zhang, X. Lu, Y. Cheng, Y. Yin, *DAWN: Smaller and Faster NTRU Encryption via Double Encoding*, ASIACRYPT 2025, pp. 396–427; ePrint 2025/1520. [DOI](https://doi.org/10.1007/978-981-95-5099-9_13); [ePrint](https://eprint.iacr.org/2025/1520); [accessible manuscript reproduction](https://www.scribd.com/document/1043726511/DAWN-Smaller-and-Faster-NTRU-Encryption-via-Double-Encoding). Tables and algorithms in this report were checked against the accessible reproduction; verify transcription against the official version.
2. P.-A. Fouque, P. Kirchner, T. Pornin, Y. Yu, *BAT: Small and Fast KEM over NTRU Lattices*, ePrint 2022/031. [Version record](https://eprint.iacr.org/2022/031), showing 12 April 2026 revision and proof-fix note.
3. Same authors, historical [BAT manuscript](https://eprint.iacr.org/2022/031.pdf), TCHES 2022. The version served by a mutable PDF URL may change; use the version history for theorem comparisons.
4. NIST, [FIPS 203: Module-Lattice-Based Key-Encapsulation Mechanism Standard](https://nvlpubs.nist.gov/nistpubs/fips/nist.fips.203.pdf), 2024.
5. NTRU team, [NTRU Algorithm Specifications and Supporting Documentation](https://www.ntru.org/f/ntru-20190330.pdf), round-three submission.
6. NTRU Prime team, [NTRU Prime round-three specification](https://ntruprime.cr.yp.to/nist/ntruprime-20201007/Supporting_Documentation/doc.pdf), 2020.
7. *Compact and Efficient KEMs over NTRU Lattices*, [ePrint 2022/579](https://eprint.iacr.org/2022/579), CTRU/CNTR.
8. NTRU+ project, [official specification and versioned releases](https://www.ntruplus.org/).

**Verification ledger:** The four 512-level DAWN object sizes were recalculated above from the published coefficient grouping; β's sum is arithmetically exact. Other published security levels, benchmarks and failure probabilities are attributed claims. The BAT corrected theorem, DAWN's canonical PDF/code consistency, DFR independence model, and fresh attack-estimator results are unresolved. This report therefore closes the literature-and-accounting stage of Phase 2A while explicitly leaving a cryptographic validation stage open.
