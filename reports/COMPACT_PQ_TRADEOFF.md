# Compact post-quantum trade-off

## Multidimensional objective

For a fixed security game, adversarial model, parameter set and hardware, compare

\[
B=(PK,CT,SK,CPU,RAM,stack,decoder/failure,validation,code/proof,assumptions).
\]

Store exact sizes and measured resources separately. A raw curve-exchange object is not a complete ciphertext; an expanded decapsulation key is not a regeneration seed; time/memory/quantum-query exponents cannot be summed into one “security bit” number. Public-key amortization is a protocol choice with reuse and multi-target consequences.

## Empirical mechanism map

| Change | Honest-party advantage | Security/engineering question exposed | Project instance |
|---|---|---|---|
| Seed *independent public randomness* | Compress matrix description | The dependent noisy product still needs representation; do not expose secret sampler seed | ML-KEM, FrodoKEM, HQC |
| Polynomial/module/QC regularity | Small algebraic map, fast convolution | Automorphisms, projections, weak distributions, reduced attack dimension | ML-KEM, NTRU, HQC/BIKE |
| Stronger rounding or decoding | Smaller coefficient alphabet or omit public codeword | Correlated failures, key-conditioned tails, reaction/CCA reduction | DAWN; HQC → BIKE comparison |
| Secret trapdoor basis | Small ciphertext with fast secret recovery | Basis generation/validation, proof dependence, RAM | BAT |
| Large public redundant code | Easier public correction and analysis | Bandwidth | HQC |
| Tiny mathematical curve | 64 B public object at historical CSIDH/MIKE point | Hidden shift or newer module-action assumptions, validation, CCA bytes | CSIDH, MIKE |
| Few public ciphertext bytes | Small repeated encapsulation | Often very large stored/distributed PK | Classic McEliece |

**Observed relationship, not theorem:** compression often increases algebraic regularity or decoder dependence; either can enlarge attacker structure or correctness burden. Less structure can enlarge transmitted objects. A hypothetical new relation may escape these specific tensions, but a hard average-case distribution, secret-assisted recovery and CCA proof would have to be exhibited.

## Qualitative trade-off regions

“Maturity” refers to evidence through 27 September 2026, not an unconditional security rating. “High implementation complexity” is qualitative and platform dependent.

| System | Communication | Assumption maturity | Quantum-analysis maturity | Implementation complexity | DFR/correctness complexity |
|---|---|---|---|---|---|
| ML-KEM | moderate | high, standardized | substantial | moderate, constant-time still needed | specified and studied |
| FrodoKEM | high | long-studied plain LWE | substantial | large matrix/RAM | reconciliation |
| DAWN | research sub-kB pair | newer two-assumption instance | incomplete independent instance costs | codec+special decoder | correlated tail unresolved |
| BAT | research ~1 kB pair | older proposal, 2026 proof correction undiffed | incomplete project estimator | complex key generation | special secret decoder |
| HQC | high | NIST selected | substantial ISD work | public code decoder | model assumptions, less secret-key dependence |
| BIKE | medium-high | researched, not selected | substantial QC/ISD work | secret iterative decoder | weak-key/per-key/reaction burden |
| Classic McEliece | enormous PK / small CT | long studied, new 2026 preprints | substantial but evolving | large key handling | no valid-input DFR in classic design |
| CSIDH/CTIDH | small-to-medium *raw* | active research | contested concrete hidden-shift accounting | expensive actions/validation | group-action KEM unspecified |
| MIKE | tiny *raw inference* | new module action | concrete quantum margin unknown | author-reported fast, independent audit absent | CCA KEM unspecified |

The comparison deliberately has no winner. “More structure → shorter” is a useful research hypothesis only when paired with a target-specific attack and implementation ledger.
