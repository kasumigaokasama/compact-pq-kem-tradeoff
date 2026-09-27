# The Compact Post-Quantum KEM Trade-Off

**Yusuf Kaya · Jan Moser**  
Independent Research Project · Evidence cutoff: 27 September 2026

> This repository accompanies a falsification-led investigation into compact post-quantum key encapsulation. It does not introduce a new production cryptographic primitive.

[Read the paper](paper/Compact_Post_Quantum_KEM_Tradeoff.pdf) · [Reproduce the calculations](REPRODUCIBILITY.md) · [Evidence ledger](reports/EVIDENCE_LEDGER.md)

## Research question and motivation

Can a new KEM simultaneously provide materially shorter public keys plus ciphertexts, credible post-quantum security, modest runtime and memory, manageable implementation complexity, mature assumptions and a defensible IND-CCA path?

Compact objects matter for communication and storage. Their representation alone does not settle quantum security, rare decryption failures, validation or CCA overhead.

## Main result

Within the investigated design space and evidence available through 27 September 2026, no candidate mechanism simultaneously justified substantial communication reduction, credible post-quantum security, mature assumptions, practical implementation and a defensible IND-CCA construction.

This is a scoped negative construction result. It is not an impossibility theorem, proof of ML-KEM optimality, or proof that MIKE or an entire mathematical family is insecure.

## Research process and investigated families

A broad landscape survey led to compact NTRU audits, model reproduction and falsification, followed by QC-Hamming and class-group/isogeny-action investigations. Module-LWE provided a standardized control; plain LWE and Classic McEliece supplied architectural contrasts.

- Phase 2C: insufficient primary validation; no new NTRU construction recommended.
- Phase 3: QC-Hamming NO-GO under the project gates.
- Phase 4A: group-action NO-GO under the project gates.
- Phase 5: final synthesis.
- Phase 6: publication and reproducibility.

## Key project-reproduced results

- Modeled DAWN object sizes: 615/436 B (alpha), 514/450 B (beta).
- Same-alphabet beta encoding: 964 → 962 B, a 2 B (0.2075%) saving. Serialization engineering, not a new primitive.
- DAWN independence-model log2 DFR: −132.676946974 / −130.133613254. These are model outputs, not validated real DFR bounds.
- HQC-1 support entropy: 622.952 / 694.542 bits. Those sparse supports are not the transmitted dense objects.
- Ring identities and 128 quartic factors at q = 257 and 769. No key-recovery attack follows.

See [observed outputs and their limits](results/reproduced_results.md).

## Repository structure

| Path | Contents |
|---|---|
| `paper/` | Final PDF and editable LaTeX/Markdown source |
| `experiments/` | Seven original research scripts plus an output checker |
| `results/` | Actual observed outputs and interpretation |
| `docs/` | Methodology, evidence model and limitations |
| `reports/` | Preserved project reports and ledgers |
| `.github/workflows/` | Deterministic calculation checks |

## Reproducing the experiments

Tested with Python 3.12.14 and NumPy 2.3.5. From the repository root:

```sh
python -m pip install -r requirements.txt
python -m unittest discover -s experiments -p 'test_*.py' -v
python experiments/check_reproduced_results.py
```

Expected: three original codec tests pass, and the deterministic result checker passes. Full commands and scientific boundaries: [REPRODUCIBILITY.md](REPRODUCIBILITY.md).

## Paper

[Final academic PDF](paper/Compact_Post_Quantum_KEM_Tradeoff.pdf) · [Editable LaTeX](paper/source/Compact_Post_Quantum_KEM_Tradeoff.tex) · [Publication Markdown](paper/source/publication.md) · [Authoritative Phase 5 manuscript](reports/FINAL_RESEARCH_PAPER.md)

## Evidence model and limitations

Labels distinguish established encoding facts, conditional assessments, reproduced models, inferences and unknowns. [Evidence model](docs/evidence_model.md) · [Limitations](docs/limitations.md) · [Reopening triggers](reports/FUTURE_TRIGGER_CONDITIONS.md).

## Security warning

**Do not use this research code to protect production data.** Software tests validate calculations; they do not validate cryptographic security. A green workflow is a reproducibility result only. See [SECURITY.md](SECURITY.md).

## Authors

Yusuf Kaya and Jan Moser. The project is joint work. See [AUTHORS.md](AUTHORS.md).

## Citation

Yusuf Kaya and Jan Moser, “The Compact Post-Quantum KEM Trade-Off: A Falsification-Led Investigation of Compactness, Security, Correctness and Maturity in Post-Quantum Key Encapsulation”, Independent Research Project, 2026.

[CITATION.cff](CITATION.cff) provides the report as `preferred-citation` with `type: report`, following CFF 1.2.0. No DOI, journal or conference is claimed.

## Licensing

Copyright 2026 Yusuf Kaya and Jan Moser.

- **Code: Apache-2.0.** See [LICENSE](LICENSE) and [NOTICE](NOTICE).
- **Paper and original documentation, figures and diagrams: CC BY 4.0.** See [documentation license](LICENSE-DOCUMENTATION.md).

Commercial reuse is allowed subject to the applicable license conditions and attribution requirements. Third-party papers, standards, external source material, trademarks and datasets retain their own rights and licenses and are **not** relicensed by this repository.
