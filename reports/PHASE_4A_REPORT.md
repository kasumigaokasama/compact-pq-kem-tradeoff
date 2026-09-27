# Phase 4A — C7 class-group and isogeny actions

**Evidence cutoff:** 27 September 2026. **Question:** Can a defensible approximately 128-bit post-quantum, compact, practical, IND-CCA KEM be constructed from current group-action mathematics? This is a literature audit, not a new construction or a security claim.

## Executive finding

The two interesting branches have different problems. Ordinary commutative CSIDH/CSURF/CTIDH has a real small public-object representation, but concrete quantum hidden-shift analysis makes its historical 64-byte CSIDH-512 parameter controversial. Published conservative/aggressive replacement field sizes imply approximately 283–660 bytes **per curve**, before a KEM transform. The 2024 module-action proposal ⊗-MIKE and July 2026 team announcement offer a 64-byte public object, <5 ms full key exchange, and no SIDH torsion images. This changes the feasibility outlook for *key exchange*, but relies on a newer module-action/endomorphism-ring security story, an algebraic-isogeny-model reduction, and has no verified complete IND-CCA ciphertext budget in the sources found. No audited mechanism simultaneously meets the project's evidence, performance, size and CCA requirements.

The CSIDH quantum estimates are disputed: the original authors argue that some attacks underprice the coherent quantum group-action oracle. We therefore record attack *resource vectors*, not declare a physical break or a certified 128-bit level. [Bonnetain–Schrottenloher](https://zhengxuisogeny.github.io/Isogeny-Based-Cryptography/index/quantumcsidh.pdf), [CSIDH authors' response](https://csidh.isogeny.org/analysis.html).

## Common model and what each primitive needs

Let a finite abelian group \(G\) act freely and transitively on a set \(X\), with base object \(x\). A secret \(a\in G\) produces public \(a\cdot x\). **Vectorisation:** given \(x,a\cdot x\), find \(a\) or equivalent action. **Parallelisation:** given \(x,a\cdot x,b\cdot x\), compute \((ab)\cdot x\). NIKE needs computational parallelisation hardness; indistinguishable KEM keys may require a decisional assumption or an appropriate hashing theorem. PKE needs an encryption/decapsulation construction and correctness; IND-CCA KEM further needs robust validation and a transform/proof. Vectorisation hardness alone does **not** prove parallelisation hardness. In MIKE, replace this group-action algebra by a symmetric monoidal Hermitian-module action; its security cannot be inherited from the CSIDH ledger.

## Security-per-byte vector

| Branch | Classical attack | Quantum attack | PK | Encapsulation object / complete CT | Honest cost | RAM | Assumption maturity |
| --- | --- | --- | ---: | --- | --- | --- | --- |
| ML-KEM-512 control | standardized estimates | standardized estimates | 800 B | 768 B / 768 B | mature implementations | implementation dependent | FIPS 203, IND-CCA |
| CSIDH-512 historical | generic class-group collision roughly square root of effective group order, relation dependent | hidden-shift vectors below; disputed oracle accounting | 64 B | 64 B bare / CCA unverified | CTIDH-512 .124 Gcycles/action | implementation dependent | researched, parameter dispute |
| CSIDH-like ~2260-bit aggressive | parameter-specific re-audit needed | cited tradeoff: \(2^{20}\) queries, \(2^{69}\) classical time and \(2^{59}\) memory | ~283 B | ~283 B bare / CCA unverified | larger than 512, no matched benchmark | unreported | model-sensitive |
| CSIDH-like ~5280-bit conservative | parameter-specific re-audit needed | cited tradeoff: \(2^{40}\) queries, \(2^{128}\) classical time and \(2^{64}\) memory | ~660 B | ~660 B bare / CCA unverified | larger than 2048, no matched benchmark | unreported | model-sensitive |
| ⊗-MIKE claim | supersingular endomorphism ring / module problems, no accepted concrete minimum | no transferable CSIDH Kuperberg cost; no independent concrete FTQC bound | 64 B claimed | 64 B ephemeral **inferred** / full CCA unknown | <5 ms full key exchange claimed, specific CPU | unreported | 2024 framework, 2026 announcement/model |

These rows are incomparable as a scalar. Gcycles are from one benchmark platform, MIKE milliseconds from another; CTIDH-2048 is *not* a proved 128-bit post-quantum parameter. Controls DAWN-beta ~964 B, BIKE-1 ~3114 B, HQC-1 ~6674 B are project comparison figures, not endorsements of equal maturity. [FIPS 203](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.203.pdf), [dCTIDH](https://eprint.iacr.org/2025/107.pdf), [MIKE announcement](https://mailarchive.ietf.org/arch/msg/cfrg/QM3t6di1bsgla6iIJ3gN6BbDoVk/).

## Concrete quantum decision

For CSIDH-512, Bonnetain–Schrottenloher Table 4 gives (base-two logs) three different combinations: queries/T gates/classical time/quantum memory of (33,85.6,33,31), (19,71.6,86,<15.3), and (24,76.6,63,<15.3). The T-gate column adds a modeled 52.6-log coherent oracle cost to the query count. No row simultaneously has cheap quantum, classical and memory resources; depth, physical qubits and QRAM architecture cannot be inferred from these totals. The first row's quantum memory is enormous, while the other rows move cost to classical work. Newer shifted-input attacks can be much cheaper when protocols publish many related curves, which argues against auxiliary curve acceleration. See the dedicated ledger.

## Final thirteen answers

1. **Smallest defensible public object:** 64 B as a *research key-exchange object* in MIKE's published mathematical proposal and 2026 announcement; no equivalently defensible complete CCA-KEM public key. A historical CSIDH-512 64 B object has disputed PQ128 parameters.
2. **Smallest defensible complete PK+CT:** 1568 B for the standardized ML-KEM-512 control. For a *group-action* IND-CCA KEM, no verified total can be reported; the 128 B MIKE figure is only a two-object, conditional raw-exchange inference.
3. **Best classical attack:** For plain CSIDH, class-group/vectorisation collision or meet-in-the-middle and relation-sensitive secret enumeration; for MIKE no independently settled concrete best attack. SIDH's torsion-image attack does not mechanically transfer without its data.
4. **Best quantum attack:** CSIDH: hidden-shift/Kuperberg-family tradeoffs, with large model disagreements; shifted-input protocols: multi-input hidden-shift reductions. MIKE: unknown concrete quantum minimum.
5. **Kuperberg importance:** Central to regular abelian actions, including CSIDH/CTIDH/CSURF; its absence for the monoidal module action is a research proposition, not a security proof.
6. **Honest action evaluation:** dCTIDH-2048 ~1.695 Gcycles per action, hardened variant ~1.59–1.60 Gcycles, vs MIKE team claim <5 ms for a complete exchange on a named laptop; benchmarks are not apples to apples.
7. **Validation:** Parse canonical curve encodings, reject singular/wrong-field/wrong-domain objects, establish required supersingularity and orientation/endomorphism/action-domain conditions; MIKE announcement says an \(\mathbb F_{p^2}\) supersingularity test is included. Fault and side-channel behavior remain critical.
8. **CCA conversion destroys size advantage?** Unknown for MIKE; may require tags, deterministic reencryption, proof data or a separate construction. A naked curve plus hash is not a CCA proof.
9. **Below 1 KB?** Raw aggressive CSIDH-like pair (~566 B) and MIKE pair (~128 B) plausibly yes, *without* claiming IND-CCA. Conservative plain CSIDH pair (~1320 B) no. No verified below-1 KB group-action IND-CCA KEM at target security found.
10. **Newer assumption than ML-KEM?** Yes, every surviving isogeny branch; MIKE especially.
11. **Why use instead of ML-KEM?** If mature independent analysis eventually validates MIKE, much smaller exchanged objects and perhaps competitive latency; those conditions are unmet here.
12. **Phase 4B new candidate?** **NO.**
13. **Decision basis:** The compact branch has unresolved concrete quantum, IND-CCA and full-byte evidence; the better-studied regular action pays a parameter/runtime cost and still lacks a compelling verified KEM advantage.

Under the project's stop rule, terminate the search for a new compact primitive under current requirements. Established post-quantum constructions are the engineering choice; new mathematical results and independent cryptanalysis could justify a *new* assessment later.

**NO-GO — RISK/COMPLEXITY OUTWEIGHS COMPACTNESS**
