# Group-action landscape — evidence through September 2026

## Taxonomy

| Line | Action / object | Public auxiliary data | Main use / status | SIDH attack transfer |
| --- | --- | --- | --- | --- |
| CRS / ordinary curves | ideal class group on ordinary CM curves | curve invariant | foundational NIKE; historically slow | no SIDH torsion images by default |
| CSIDH | imaginary quadratic class group on supersingular curves over \(\mathbb F_p\) | Montgomery coefficient / invariant | commutative NIKE, 512-bit field historical | no direct torsion-image path |
| CSURF | related class-group action, efficient 2-isogeny surface | curve coefficient | modest action speed improvement (~5.68% at 512 in original study) | same separation as CSIDH |
| CTIDH / dCTIDH | same general CSIDH action, secret distribution and constant-time action engineering | curve coefficient | hardened implementation, **not** a new hidden-shift hardness claim | no direct transfer; fault threats remain |
| oriented action / PEGASIS | oriented supersingular curves, full effective class-group action using dimension-four isogenies | orientation or implicit handling protocol dependent | 2025 research action, ~1.5 s at 512 and 21 s at 2048 prototype | orientation disclosure needs separate audit |
| CSI-FiSh | CSIDH class-group relation computations | signature transcripts | signature, not a KEM | no direct transfer; public relation/curve exposure audit |
| PRISM | large-prime-degree isogeny identification/signature | proof/signature material | 2025 signature research, different hard problem | no automatic KEM construction |
| ⊗-MIKE | Hermitian-module symmetric monoidal action, supersingular \(\mathbb F_{p^2}\) curve j-invariant, shared dimension-four variety | no SIDH torsion images in 2024 proposal | NIKE, 64 B Level 1 object; 2026 implementation/proof claims | CD mechanism absent; new attacks still possible |
| PIKE / POKÉ | supersingular isogeny PKE line, pairing assisted decryption | scheme-specific | 2025–26 PKE novelty, not demonstrated <1KB CCA KEM here | audit scheme-specific torsion/pairings |

**SIDH/SIKE lesson:** Castryck–Decru exploits *images of auxiliary torsion basis points* sent with an SIDH public key; with the known starting endomorphism ring, Kani's reducibility criterion and gluing recover the secret efficiently (SIKEp434 about ten minutes on one core in their reported implementation). A lone CSIDH curve coefficient or MIKE j-invariant does not contain those particular images. This establishes only nontransfer of this attack's prerequisites, never general security. [Castryck–Decru](https://eprint.iacr.org/2022/975.pdf).

CSIDH-512's 64 B arises from the ~512-bit field representation, not 128-bit quantum evidence. CSIDH's action is regular abelian, hence the hidden-shift formulation applies in principle. Class-group relations can make exponent vectors equivalent. An \(n\)-bit curve encoding contains at most \(n\) bits; that alone says little about security. Thirty-two-byte objects might identify a small family of curves but lack a demonstrated PQ128 action here. 64/96/128-byte curves are mathematically plausible when a different action avoids the regular abelian hidden-shift bottleneck, as MIKE illustrates, but this is conditional on new security and CCA evidence. More metadata for version, domain, validation or proofs is protocol-specific.

## 2025–26 developments and scope

2025 dCTIDH and dummy-free hardened dCTIDH improve constant-time action engineering. PEGASIS makes full effective class-group evaluation practical in a different oriented setting, though seconds per action are not competitive KEM evidence. A 2025 shifted-input analysis demonstrates large losses from publishing related public curves. The 2026 algebraic-isogeny model offers model-based reductions for isogeny key exchange, not a standard-model or CCA proof by itself. The MIKE team announced 64 B Level 1 / 128 B Level 5 keys, <1 ms keygen and <5 ms exchange on Ryzen 7 PRO 7840U, roughly 4200 Rust LOC excluding field arithmetic, and validation within timing. Author's publication list updated 21 September 2026 still lists the 2024 module-action preprint but no completed team MIKE paper; this is an observation about available sources, not proof of non-publication.

Primary sources: [Robert 2024](https://eprint.iacr.org/2024/1556.pdf), [author publication list](https://www.math.u-bordeaux.fr/~damienrobert/pro/publications/index.html), [MIKE announcement](https://mailarchive.ietf.org/arch/msg/cfrg/QM3t6di1bsgla6iIJ3gN6BbDoVk/), [algebraic isogeny model](https://eprint.iacr.org/2026/032), [PEGASIS](https://eprint.iacr.org/2025/401), [CSURF](https://biblio.ugent.be/publication/8665496), [PRISM](https://eprint.iacr.org/2025/135).

**Novelty check:** CSIKE (Qi, 2022) already claims a CSIDH-based IND-CCA KEM with an extra tag, so “apply FO to CSIDH” is not novel. Its precise matched modern PQ128 byte/runtime/QROM evidence was not established in this audit. PIKE and POKÉ show PKE is an active separate line. These do not turn a NIKE claim into an independently verified compact IND-CCA KEM. [CSIKE publisher](https://doi.org/10.1515/jmc-2022-0007), [PIKE proceedings](https://link.springer.com/book/10.1007/978-3-032-26737-5).
