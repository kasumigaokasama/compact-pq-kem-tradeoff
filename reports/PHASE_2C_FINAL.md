# Phase 2C: final compact NTRU research decision

27 September 2026. Scope: DAWN α/β-512, BAT-512 proof correction, and a decision on a new NTRU-family construction. This report builds on the supplied Phase 1 and Phase 2A material and the local Phase 2B files. It does not define a new KEM.

## Evidence and work completed

| Priority | Result | Limit |
|---|---|---|
| Canonical DAWN | [ePrint 2025/1520](https://eprint.iacr.org/2025/1520) metadata, [ASIACRYPT proceedings](https://doi.org/10.1007/978-981-95-5099-9_13) abstract, [author slides](https://datatracker.ietf.org/meeting/125/materials/slides-125-cfrg-ntru-based-public-key-encryption-01), and pinned [author DFR repository](https://github.com/Icarid-Liu/lattice-KEM-DFR-estimator) located | Full 2025-10-27 ePrint PDF / authoritative 32-page chapter inaccessible; no SHA-256, theorem-level diff or official encryption implementation |
| Correctness | Exact `wu=t` identity, explicit centered lift and carry `K`, conditional message-residue recovery proved in `DAWN_CORRECTNESS_PROOF_AUDIT.md` | Full single-error decoder, sampled invertibility, precise rounding and CCA handling lack canonical specification; classification **AMBIGUOUS BUT RESOLVABLE** for the algebraic skeleton |
| DFR | Independent positive float64 convolution reproduces author α `-132.676946974`, β `-130.133613254` log2 model outputs to nine decimals | Actual correlated average, key/message conditioned and adversarial-input DFR remain unbounded; paired-dependence surrogate shows binomial independence is inexact |
| BAT correction | [ePrint record](https://eprint.iacr.org/2022/031) explicitly announces a 2026-04-12 security-proof fix | Neither versioned old nor corrected new PDF acquired; theorem change and its effect on BAT-512 **unknown** |
| Attack and structure | Current estimator commit identified; exact 128 quartic CRT factors and 512 cyclotomic automorphisms analyzed; no useful projected attack established | Sage unavailable; **no numerical independent attack run** or classical/quantum cost ranking |
| Gap screen | β current `514+450=964 B`, same-alphabet whole-byte bound `513+449=962 B`; thresholds 915 B and 867 B for ≥5% and ≥10% | No mathematical mechanism survives a plausible security/correctness/byte-count screen |

Reproducible code for the DFR model, paired surrogate and ring identities is in `experiments/`. The prior Phase 2B independent codec is not an official DAWN wire-format implementation. See the eight supporting Phase 2C Markdown files for source records, equations, numerical assumptions and falsification criteria.

## Decision logic

Pure coding has about two bytes of modeled slack per β key/ciphertext pair. A meaningful 49-byte reduction must change a mathematical object and revalidate decoder tails, key and ephemeral attacks, and CCA behavior. None of the three constrained mechanism agendas presently supplies those proofs or a safe parameter region. Thus **Phase 3 should not construct an NTRU-family candidate on present evidence**.

The formal outcome must nevertheless be *insufficient evidence* under the supplied rubric: the canonical DAWN 2025-10-27 full text (or full ASIACRYPT chapter) is needed to settle the full decoder/specification and the latest pre-2026-04-12 plus 2026-04-12 corrected full BAT papers are needed to determine the proof and assumptions. Those artifacts were sought through ePrint, publication and author routes, but their complete bytes were not accessible. This is an external primary-validation block, not a request for another exploratory NTRU design phase. If the artifacts become available, a narrow document and proof comparison could revise the formal verdict; it does not justify starting construction now.

## Verdict

**INSUFFICIENT EVIDENCE — PRIMARY VALIDATION STILL IMPOSSIBLE**

### What is the strongest reproduced result?

The independent author-model DFR calculation matches α `log2=-132.676946974` and β `log2=-130.133613254`; the modular algebra and quartic factor degree also check exactly. This is reproduction of a *model*, not validation of real failure probability.

### What is the weakest security assumption?

It cannot be ranked quantitatively. For the present evidence, the least validated claims are the real correlated, potentially key-conditioned DFR and the effect of BAT's changed proof. Equivalent-key NTRU recovery and ephemeral distinguishing costs are likewise unestimated.

### What limits DAWN-beta below 964 bytes?

Its modeled alphabets already require at least 962 B for the pair. Below that, a smaller ciphertext alphabet or public relation changes rounding/decoder failure and possibly lattice security; the binding constraint among these is unknown.

### Is DAWN's DFR credible after correlation-aware analysis?

The author's arithmetic is reproduced, but the real `~2^-130` bound is **unvalidated**. Exact paired sharing gives a large joint-tail difference in a restricted n=512 iid surrogate; it cannot be promoted to an actual corrected DFR. No honest-key conditional or adversarial-input bound is known here.

### What exactly changed in BAT in April 2026?

The ePrint record says an error in the previous security proof was fixed on 12 April 2026. The changed lemma, game, assumption, reduction loss and BAT-512 implications **cannot be identified without the two full versioned PDFs**.

### Did any CRT/ring projection yield a useful attack?

**No.** Quartic projections are exact, but no projected short key, distinguisher, message recovery or lifting attack was demonstrated.

### What is the current best classical attack route?

**Unknown by cost.** Prioritize hybrid search for an equivalent short NTRU relation and primal/dual attacks on the ephemeral masked sample, then compare under a pinned estimator and correct distributions.

### What is the current best known quantum attack route?

**Unknown by cost.** Quantum-assisted lattice search/hybrid enumeration and multi-target search are candidate routes; no gate, memory, success or quantum speedup estimate was derived for these instances.

### Is there a >=5% plausible improvement mechanism?

**None that survived preliminary checks.** The 49-byte target requires a new mathematical change; quotient/decoder, secret-assisted recovery and public-relation ideas lack full DFR and attack validation.

### Is there a >=10% plausible improvement mechanism?

**No demonstrated mechanism.** The 97-byte threshold is farther outside the 2-byte packing slack.

### Should Phase 3 construct an NTRU-family candidate?

**NO.** Shift Phase 3 investigation to Phase 1's **C5 quasi-cyclic Hamming decoding** family, with **C1 module noisy relations** as a mature control. This is a research direction, not a claim that C5 has smaller ciphertexts or a ready candidate.
