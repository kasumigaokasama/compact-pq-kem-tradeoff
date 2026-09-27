# Quasi-cyclic structure budget

`R=F₂[X]/(X^r−1)` represents one `r×r` circulant block by `r` bits. A generic systematic parity-check block for `[2r,r]` needs about `r²` bits; one QC block needs `r`. At BIKE-1 `r=12323`, that is about 18.98 MB versus 1541 B for the block alone (excluding generation/format). This is why a 261120-byte level-1 Classic McEliece public key can coexist with a 96-byte ciphertext: its Goppa decoder offers near-perfect correctness but the public matrix is not QC-compressed in the same way. A QC ring is a **major key compression**, already spent in HQC and BIKE.

| Structure | Size benefit | Computational benefit | Attack benefit | Security cost/obligation |
|---|---|---|---|---|
| One binary circulant block | `r²→r` raw matrix bits | Fast cyclic multiplication, compact storage | Rotations of a relation produce correlated equivalent relations | Account for orbit/multiple-target ISD and special algebraic projections |
| Seeded public HQC `h` | `n→256` stored public bits | Expand as needed | Seed is public; adversary regenerates exactly the same `h` | None from secrecy; PRG/XOF assumption and implementation cost |
| Systematic QC-MDPC `h=h₁/h₀` | One dense public block instead of two | Polynomial inversion at keygen, sparse private parity checks | Search for low-weight dual/secret check instead of generic decoding | DFR and weak-key/reaction analysis; invertibility distribution |
| Primitive-prime HQC length | Avoid many tiny factor projections if `2` is primitive modulo `n` | Ring arithmetic remains cyclic | Parity factor `X−1` and rotational orbits remain | Explicit decisional QCSD-with-parity and truncation assumptions |
| Full rotation orbit | Up to `r` representations of one generic nonperiodic support | Equivalent public equations | Known DOOM speedup roughly `√r` for relevant ISD models; log₂ benefit ~6.9 bits at HQC-1 | **Already considered** in HQC known-attacks section; do not subtract another independent `log₂ r` |

The potential orbit reduction depends on the target and algorithm: naive counting divides a nonperiodic solution set by `r` (log₂ `r≈14.11` at HQC-1), while the *algorithmic* DOOM benefit cited by the HQC authors is `O(√r)` (≈7.05 bits). These are not interchangeable cost results. BIKE's small dual basis yields a different, sometimes larger structural gain for key recovery. Additional automorphism, folding or multi-sample gain beyond the accounted orbit has **not** been demonstrated here. Attackers can rotate `(x,y)` and its syndrome, but those are related views of the same sample.

Sources: [HQC 2025 specification, Section 6.3](https://pqc-hqc.org/doc/hqc_specifications_2025_08_22.pdf); [BIKE v5.2 specification](https://bikesuite.org/files/v5.2/BIKE_Spec.2024.10.10.1.pdf); [NIST IR 8545](https://nvlpubs.nist.gov/nistpubs/ir/2025/NIST.IR.8545.pdf).
