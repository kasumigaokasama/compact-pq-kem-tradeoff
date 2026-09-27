# Phase 2B — reproducibility and cryptanalysis checkpoint

**27 September 2026. Decision: NOT YET.** This is an experimentally backed *partial* Phase 2B result, not the completed validation specified in the research brief. Security-critical gates remain because the canonical DAWN PDF, official vectors/code and both BAT proof versions were not available for inspection. Calling the phase complete would violate its primary-source rule.

## What was actually reproduced

1. An independent model of four 512-level DAWN Table 8 packing alphabets/groups yields lengths **615, 436, 514, 450 bytes** for α public key/ciphertext and β public key/ciphertext. These numbers match the primary DAWN abstract's α ciphertext 436 and β pair 964, but the grouping itself was taken from Phase 2A's noncanonical transcription. Byte-for-byte official compatibility was **not** established. See `DAWN_CODEC_ANALYSIS.md` and `experiments/dawn_codec.py`.
2. Exact integer lower bounds for *all* `M^512` coefficient vectors show **one byte per object** of representation slack. A whole-vector base-M bijection emits one byte less for each object and rejects invalid encodings. The β pair's modeled 964 B can become 962 B, a **0.2075%** saving, before implementation costs. This is serialization engineering only.
3. In the integral negacyclic ring, with `y=x^(n/4)`, `w=1+y`, `t=1+y²`, **`t/w=y²-y³`** for odd `q`; modulo `(2,t)` this maps to `w`. That resolves a *limited residue identity* underlying Phase 2A's question. It does not establish a full correctness theorem after center lifting and rounding. See `DAWN_ALGEBRA.md`.
4. An exhaustive toy fixed-weight negacyclic calculation shows a binomial independence estimate can differ sharply from the joint distribution. This illustrates the need for correlated DFR work; it is **not DAWN's DFR**. See `DAWN_DFR_ANALYSIS.md` and `experiments/toy_correlation.py`.
5. For both DAWN moduli `q=257,769`, the 512-degree cyclotomic polynomial factors over `F_q` into **128 quartics**. This creates CRT projections but is not by itself an attack; projected secret/noise and useful lift are unexamined. See `ATTACK_LEDGER.md`.

**Test evidence:** `python3 -m unittest -v test_dawn_codec.py`: 3 tests passed, including round trips, boundary coefficients/last groups and malformed inputs. Toy enumeration covers all 3,136 stated pairs. No attack estimator, reference implementation, BAT PDF diff, rare-event model or side-channel measurement was run. Do not interpret blank attack rows as successful security checks.

## Blockers and research outcome

The primary ePrint records confirm DAWN 2025/1520's 2025-10-27 last revision and BAT 2022/031's 2026-04-12 revision with a proof-error note. The available PDF endpoints/version history could not be retrieved for hashing and comparison. A targeted search did not locate an official DAWN implementation or independent cryptanalysis establishing these exact questions. The outcome is closest to **C: substantial caution around proof and DFR validation**, with a narrowly demonstrated **E: small modeled serialization slack**. There is no evidence for D (a concrete cryptanalytic break). A and B remain undecidable here.

| Gate | Result | Required next evidence |
|---|---|---|
| Canonical DAWN source freeze | **BLOCKED** | Full official PDF checksum, version and official code/vectors if released |
| Algebra/correctness | **PARTIAL** | Canonical identities, center-lift/wrap argument and code check |
| Codec wire compatibility | **PARTIAL** | Official byte vectors, exact field ordering and constant-time evaluation |
| DFR average/per-key/adversarial | **BLOCKED** | Exact distributions or validated rare-event bounds including correlations |
| BAT corrected proof | **BLOCKED** | Both immutable versioned PDFs, mathematical diff and theorem-level review |
| Classical/quantum attacks | **BLOCKED** | Pinned estimator and cost models for actual distributions and weakest winning goals |

The linked supporting files are `DAWN_SOURCE_MANIFEST.md`, `DAWN_ALGEBRA.md`, `DAWN_CODEC_ANALYSIS.md`, `DAWN_DFR_ANALYSIS.md`, `BAT_PROOF_DIFF.md`, `BAT_ANALYSIS.md`, `ATTACK_LEDGER.md`, and `RESEARCH_GAPS.md`. Experimental code is under `experiments/`. Primary records: [DAWN ePrint](https://eprint.iacr.org/2025/1520), [BAT ePrint](https://eprint.iacr.org/2022/031), [BAT author repository](https://github.com/pornin/BAT). Numerical results from the independent model are reproducible with Python's standard library.

## Is DAWN's mathematical description internally consistent?

**Not established, medium confidence in the narrow algebraic identity.** `t*w^-1=y²-y³` in the large odd-modulus ring and its residue equals `w` in the small `(2,t)` quotient. Generic and instantiated ciphertexts are not identical in the large ring. Without the canonical source and a center-lift correctness argument, the full description remains unverified. No actual failing input was found.

## Are DAWN's quoted DFR values sufficiently justified for further research use?

**No as independently validated inputs; low confidence in either quoted exponent.** Values near `2^-133` and `2^-130` are author estimates. The effective noise, correlations, key-conditioned tails and decoder index event were not reproduced at `n=512`; the exact toy counterexample concerns only an independence model, not those exponents.

## What exactly changed in BAT's April 2026 proof correction?

**Unknown.** Primary metadata says the 12 April 2026 revision fixes an earlier security-proof error, but both versioned full texts were unavailable for the required diff. The affected lemma, assumptions, bound and parameters cannot be stated responsibly.

## Does BAT remain a useful compact-NTRU research baseline?

**Yes as a mechanism/size comparator, not yet as a proof-validated baseline.** Historical 521-byte public key and 473-byte ciphertext need matching canonical codec vectors; any theorem-level reliance awaits the corrected proof.

## Is there measurable representation slack remaining?

**Yes, exactly one byte for each modeled full-alphabet object.** α public key 615→614, α ciphertext 436→435, β public key 514→513, β ciphertext 450→449. β pair 964→962 bytes (0.2075%). The result is an information-theoretic full-alphabet bound and constructive experimental codec, **not an official DAWN wire-format patch**. Time, memory and constant-time feasibility were not measured.

## Is there a cryptographic research gap rather than merely a codec optimization?

**Not demonstrated.** The only reproduced saving is under 1% and purely representational. Alternatives involving quotient/code or rounding remain open until correctness, DFR, proof and attack gates are passed.

## Should Phase 3 design a new NTRU-family construction?

**NOT YET — unresolved validation blockers remain.** A negative result after primary-source validation would be scientifically useful; there is no basis to invent a new scheme now.

## If NO, which mathematical family should Phase 3 investigate instead?

This decision is conditional because the preceding answer is **NOT YET**. If a completed NTRU audit yields **NO**, Phase 1's **C5 quasi-cyclic Hamming decoding** is the clearest non-lattice comparison workstream. Keep **C1 module noisy relations** as the mature control and **C7 class-group actions** as a high-risk compactness study; none is a ready new KEM proposal.
