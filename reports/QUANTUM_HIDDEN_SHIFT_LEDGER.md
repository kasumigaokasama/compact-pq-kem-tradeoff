# Quantum hidden-shift ledger

All exponents below are base-two logarithms, not “security bits.” Costs in different resources cannot be added or compared as one number. A coherent action oracle must be reversible and its T gates, depth, width and QRAM implementation accounted for.

## Reduction and algorithm families

A free transitive abelian action supplies two functions \(f_0(g)=g\cdot x\), \(f_1(g)=g\cdot(a\cdot x)\): they differ by hidden shift \(a\). This connects vectorisation to dihedral hidden subgroup / hidden shift algorithms. Kuperberg's sieve trades subexponential query/time against extensive quantum storage; Regev-style variants reduce quantum space at time cost; hybrid collimation and quantum walks/classical lists redistribute resources. An oracle for a *single public action* is not automatically cheap quantumly. Even a good vectorisation attack need not be the best parallelisation attack; no converse hardness theorem is assumed.

| Source / target | Quantum oracle queries | Modeled T gates | Classical work | Quantum storage / classical memory | Qualification |
| --- | ---: | ---: | ---: | --- | --- |
| Bonnetain–Schrottenloher, CSIDH-512 §3.2 | \(2^{33}\) | \(2^{85.6}\) | \(2^{33}\) | \(2^{31}\) quantum memory | enormous coherent memory |
| Same §3.3 | \(2^{19}\) | \(2^{71.6}\) | \(2^{86}\) | quantum memory <\(2^{15.3}\) plus oracle | expensive classical stage |
| Same §3.4 | \(2^{24}\) | \(2^{76.6}\) | \(2^{63}\) | quantum memory <\(2^{15.3}\) plus oracle | intermediate tradeoff |
| Their aggressive NIST-1 discussion, ~2260-bit p | \(2^{20}\) | not independently established here | \(2^{69}\) | \(2^{59}\) classical; ~\(2^{18}\) quantum qubits cited | *one* resource constraint choice |
| Their conservative discussion, ~5280-bit p | \(2^{40}\) | not independently established here | \(2^{128}\) | \(2^{64}\) classical | not a certified bound on every algorithm |
| 2025 shifted-input analyses of CSI-SharK/BCP | construction-dependent | examples \(2^{45}\) or \(2^{57}\) | construction-dependent | examples \(2^{38}\) or \(2^{16}\) QRAM | assumes roughly \(2^{12}\) correlated public shifts; not a plain CSIDH key |
| ⊗-MIKE | unknown | unknown | unknown | unknown | monoidal action; no demonstrated regular abelian hidden-shift reduction, no concrete FTQC margin |

First three rows reproduce Table 4 of [Bonnetain–Schrottenloher](https://zhengxuisogeny.github.io/Isogeny-Based-Cryptography/index/quantumcsidh.pdf). Their 52.6-log oracle T-gate estimate is included in the first three totals. Their circuit discussion cites about 40,000 logical qubits for the then-current oracle; this workspace is separate from abstract sieve storage and is not a physical-qubit count. Error correction further matters. Depth/parallelism are **unreported for these complete attacks** here. Claims that CSIDH-512 is physically broken or has exactly 71.6-bit security would overinterpret the table. [CSIDH team analysis](https://csidh.isogeny.org/analysis.html) disputes quantum oracle undercounting; [quantum circuit analysis](https://quantum.isogeny.org/) emphasizes it.

The [2025 shifted-input paper](https://eprint.iacr.org/2025/376.pdf) models multiple known shifts and QRAM; do not mix its attack cost into the plain two-curve NIKE row. Likewise, Grover enumeration applies to a concretely specified effective secret distribution and oracle, at square root of its support before precomputation/multitarget effects; it does not validate CSIDH parameter choices by itself. Quantum walks and alternative relation algorithms need target-specific accounting. Multi-user work sharing and classical relation precomputation may change marginal costs.

**Parameter implication:** CSIDH-512's 64 B is a representation fact, not a robust approximately 128-bit quantum-cost conclusion. Enlarging p to 2260–5280 bits increases each curve to 283–660 B and honest action work. MIKE avoids the *known formulation* of this ledger only if its structural distinction and concrete endomorphism assumptions survive new quantum cryptanalysis; “Kuperberg does not apply” is explicitly presented as a presumption in [Robert 2024](https://eprint.iacr.org/2024/1556.pdf).
