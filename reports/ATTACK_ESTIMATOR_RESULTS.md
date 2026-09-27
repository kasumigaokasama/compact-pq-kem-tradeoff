# Attack estimator and attacker-goal ledger — 27 September 2026

## Reproducibility status

The current `malb/lattice-estimator` repository was identified at commit `53da5982597709ba0fdf94ea37a84d822310fd84` (2026-08-19). The required Sage runtime is unavailable in this workspace (`sageall` cannot be imported), and no pinned model/configuration was executed. **There are no independent numerical attack estimates to report.** Author security numbers, generic BKZ folklore and cross-family category labels are not substitutes. No single claimed classical or quantum bit cost is entered into the comparison.

| Target | Natural attack object | Easiest useful success condition to check | Numerical result |
|---|---|---|---|
| DAWN α-512, β-512 | NTRU relation `f h = g (mod q)` in nominal rank-1024 coefficient lattice | Any short equivalent `(f',g')` that enables the actual decoder, including a nonoriginal pair | **Not estimated** |
| DAWN α-512, β-512 | Mask `h s+e`, compressed ciphertext and encoded message | Single-ciphertext message recovery, distinguishing or partial secret information | **Not estimated** |
| BAT-512 | NTRU/short-basis trapdoor and its precise corrected sampling/proof distribution | Equivalent useful decoding key, not necessarily exact original key | **Not estimated** |
| ML-KEM-512 | Module-LWE primal/dual and hybrid attacks | Message recovery or distinguishing | **Not estimated; incompatible raw NTRU input** |
| NTRU-HPS/HRSS comparable sets | Ring NTRU relation, distribution-specific hybrids | Equivalent key or ciphertext attack | **Not estimated** |

Exact secret recovery is sufficient but may be harder than equivalent-relation or equivalent-decoding-key recovery. A partial projection is useful only if it predicts a message, filters keys substantially, or combines into a global short solution. A distinguisher may suffice against IND-CPA; CCA claims further require the exact transformation and decapsulation behavior. These objectives have different lattices and success predicates; their costs cannot be ranked numerically here.

## Required run configuration when Sage is available

Pin an estimator commit, Sage version, source parameter distributions, success probability, lattice embedding and preprocessing assumptions. For each compatible target report conservative/standard/aggressive classical and quantum attack models, block-size and memory, hybrid guess dimensions, and uncertainty from sieving constants, quantum enumeration, secret modeling and structured samples. Model primal/dual attacks and sparse-secret/hybrid attacks separately. Test a recovered *equivalent* relation against the actual DAWN decoder. BAT needs its corrected proof and sampling assumptions first. ML-KEM is a module-LWE control, not the same NTRU problem. Do not apply a generic square-root quantum discount to BKZ.

## Multi-sample and multi-user exposure

For one reused public key, each encapsulation supplies another correlated masked sample under the same `h`; classical preprocessing may amortize, while the distribution of `s,e,m` and deterministic rounding must be included in a distinguisher. Many public keys yield independent target relations, permitting multi-target work sharing or a search advantage whose size depends on the exact goal and memory. Ring automorphisms generate deterministic transforms of *existing* instances, not independent fresh secrets or fresh noise. No concrete amortization exponent or quantum circuit cost was established.

**Current route to prioritize:** classical hybrid short-equivalent-relation search in the NTRU key lattice, and primal/dual attacks on ephemeral masks; the winner is unknown without a comparable run. **Quantum route to prioritize:** quantum-assisted lattice search/hybrid enumeration plus multi-target search under explicit memory and circuit assumptions; no proved best route for these parameters.
