# Group-action implementation and validation analysis

| Implementation / parameter | Measurement | Meaning / limitation |
| --- | --- | --- |
| CSIDH-512 variable-time baseline | 0.114 Gcycles | one group action, not suitable as constant-time secret baseline |
| CTIDH-512 | 0.124 Gcycles | one constant-time action, same benchmark study |
| CTIDH-2048 | 1.695 Gcycles | one constant-time action; 2048 does not itself prove target quantum strength |
| SQALE-2048 / dCSIDH-2048 | 6.209 / 7.039 Gcycles | same study's comparison |
| Hardened dCTIDH-2048-194/205 | 1.59–1.60 Gcycles median, ~357k–362k \(\mathbb F_p\) multiplications | 2025 dummy-free deterministic evaluation; excludes small primes 3,5,7 |
| PEGASIS prototype | ~1.5 s at CSIDH-512-scale, ~21 s at 2048, ~2 min at 4096 | oriented full effective action in Sage; different platform/algorithm |
| MIKE team 2026 | <1 ms keygen; <5 ms full exchange including validation, Ryzen 7 PRO 7840U 3.3 GHz | author-reported Rust claim; code ~4200 LOC excluding field arithmetic; no independent matched benchmark here |

Source: [dCTIDH Table 2](https://eprint.iacr.org/2025/107.pdf), [hardened CTIDH](https://arxiv.org/abs/2509.12877), [PEGASIS](https://eprint.iacr.org/2025/401), [MIKE announcement](https://mailarchive.ietf.org/arch/msg/cfrg/QM3t6di1bsgla6iIJ3gN6BbDoVk/). Gcycle means a billion cycles and does not directly equal milliseconds without CPU frequency and benchmark environment; multiplying by two is a rough two-action exchange model, not a measured full protocol. Validation, hashing and CCA checks add costs. No honest-party RAM measurements across comparable platforms were established.

## Constant-time and object validation

The action consists of field arithmetic, torsion point sampling, degree-specific isogenies and exceptional cases. Secret-dependent branch counts, early exits and variable rejection reveal exponent-vector information through timing/cache/power. Constant-time selection and fixed work schedules help but dummy operations themselves can become fault targets; published “disorientation faults” attacks include the original CSIDH software and CTIDH. Hardened 2025 dCTIDH validates intermediate points and removes dummy operations at the reported cost.

An input decoder must enforce canonical field encodings, field membership, nonsingularity, action-domain membership and the exact supersingularity/orientation or endomorphism condition the security proof assumes. A public Montgomery coefficient merely being in range does not prove it is a valid action orbit point. For MIKE, the team says its public validation is a supersingularity test over \(\mathbb F_{p^2}\) included in the claimed timing; whether this suffices for all CCA ciphertext properties must follow a concrete KEM proof. Invalid-object decapsulation should not leak branch, error or shared-secret differences in an exploitable way.

Memory and coding complexity: fixed-size \(p\)-arithmetic, isogeny workspaces and precomputed chains increase with parameter size; exact RAM budgets, constant-time audit coverage and physical side-channel resistance are not established here. Relative to ML-KEM, there is a larger and less standardized algebraic validation surface and more difficult fault analysis. This is a qualitative engineering judgment, not a cycle or LOC equivalence.

## What modern speedups change

CTIDH/dCTIDH improve secret sampling and side-channel handling; fast large-degree isogenies improve evaluation asymptotics from roughly linear to square-root in degree under their conditions; CSURF adds efficient 2-isogenies; PEGASIS uses dimension-four pushforward techniques; 2026 module representation conversion develops high-dimensional arithmetic. These do not remove regular abelian hidden shift from CSIDH or prove an IND-CCA KEM. Threshold and multi-party schemes may add further objects and assumptions. [Fast large-degree isogenies](https://arxiv.org/abs/2003.10118), [module representation conversion](https://www.math.u-bordeaux.fr/~damienrobert/pro/publications/index.html).
