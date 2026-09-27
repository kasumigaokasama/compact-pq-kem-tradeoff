# HQC versus BIKE: mathematical compactness trade

Sources and dates: [HQC specification 2025-08-22](https://pqc-hqc.org/doc/hqc_specifications_2025_08_22.pdf); [BIKE v5.2 specification 2024-10-10](https://bikesuite.org/files/v5.2/BIKE_Spec.2024.10.10.1.pdf), with its architecture and size table indexed by the source; [NIST IR 8545](https://nvlpubs.nist.gov/nistpubs/ir/2025/NIST.IR.8545.pdf). The BIKE PDF timed out on full-text retrieval, so exact details beyond indexed primary excerpts/NIST are identified accordingly.

BIKE uses `R=F₂[X]/(X^r−1)`, sparse private `(h₀,h₁)` of weight `w/2` each and a dense public `h=h₁h₀⁻¹`. Its sender derives weight-`t` pair `(e₀,e₁)` from a 256-bit `m` bound to public-key prefix, then transmits `c=(c₀,c₁)=(e₀+h e₁, m⊕L(e₀,e₁))`. Receiver multiplies `c₀h₀=e₀h₀+e₁h₁`, applies a private QC-MDPC iterative bit-flipping decoder, unmasks `m`, rederives errors and implicitly rejects a mismatch. Here the ciphertext has **one dense ring element plus 32 bytes**, unlike HQC's dense `u` and dense noisy public codeword `v` plus 16 bytes.

| Level | HQC PK / CT / pair (2025-08) | BIKE PK / CT / pair (v5.2) | Difference in ciphertext |
|---|---|---|---:|
| 1 | 2241 / 4433 / **6674 B** | 1541 / 1573 / **3114 B** | BIKE 2860 B smaller |
| 3 | 4514 / 8978 / **13492 B** | 3083 / 3115 / **6198 B** | BIKE 5863 B smaller |
| 5 | 7237 / 14421 / **21658 B** | 5122 / 5154 / **10276 B** | BIKE 9267 B smaller |

At level 1, HQC spends 2208 bytes on `v`, where BIKE spends 32 bytes on a hash-masked message. BIKE also uses a shorter ring (`12323` versus `17669`, reducing the dense first component by 668 B) but adds 16 B more mask than HQC's salt. Precisely: `4433−1573=(2209−1541)+(2208−32)+16=2860`. That identity explains the bytes, not why the alternative is equally secure.

HQC's secret `(x,y)` is independent of the public random double-circulant code; its **public** RMRS decoder handles residual `x r₂+r₁ y+e`. BIKE's secret parity-check structure directly decodes `(e₀,e₁)` from a syndrome. This cuts communication but binds correctness to a secret iterative decoder, key-specific graph structure, threshold/iteration choice and difficult extreme failure tails. NIST selected HQC mainly for its more stable DFR analysis, while noting that HQC itself makes a coefficient-independence simplification. NIST documented gathering weak keys with an average DFR lower bound of `2^-117` for an earlier BIKE decoder/configuration, subsequent BIKE-flip improvements with limited rare-tail evidence, and near-codeword error floors. These findings must not be misrepresented as a proof that every BIKE v5.2 ciphertext is broken.

`m` is public-code encoded in HQC; in BIKE it is recovered only after the secret error decoder succeeds. Both KEMs use implicit-rejection/reencryption patterns, so BIKE's smaller size is **not** an absence of CCA transform. Any partial-secret decoder hint or public parity-check portion occupies a spectrum between these approaches, but can expose low-weight dual information; no safe intermediate point has been established. Classic McEliece supplies the complementary non-QC baseline: a very small ciphertext and perfect valid-input correctness, paid for by a very large public key.
