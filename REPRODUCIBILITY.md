# Reproducibility

Software tests validate calculations. They **do not validate cryptographic security**.

## Environment

Tested on Linux x86-64 with Python 3.12.14 and NumPy 2.3.5. The CI targets Python 3.12. NumPy is the only external runtime dependency, used by the two numerical DFR scripts. The other original scripts use only the Python standard library. Embedded constants are the inputs; no live research downloads are required.

Run commands from the repository root:

```sh
python -m venv .venv
. .venv/bin/activate
python -m pip install -r requirements.txt
```

## DAWN codec

```sh
python experiments/dawn_codec.py
```

Expected result: Grouped sizes 615/436/514/450 B; minima 614/435/513/449 B.

Demonstrates: Exact modeled representation accounting.

Does not establish: No official wire compatibility or KEM security.

## Original codec unit tests

```sh
python -m unittest discover -s experiments -p 'test_*.py' -v
```

Expected result: 3 tests pass.

Demonstrates: Seeded round trips, boundary vectors and local malformed encoding rejection.

Does not establish: No production hardening, constant-time audit or cryptographic proof.

## DAWN DFR model

```sh
python experiments/reproduce_dawn_dfr_model.py
```

Expected result: alpha log2 −132.676946974; beta −130.133613254.

Demonstrates: The specified author independence-model arithmetic.

Does not establish: Not actual correlated, per-key or adversarial-input DFR.

## QC entropy analysis

```sh
python experiments/qc_entropy_frontier.py
```

Expected result: HQC-1 622.952/694.542 support bits; BIKE-1 error 1196.018 bits.

Demonstrates: Binomial support entropy and dense-byte arithmetic.

Does not establish: Not a public compressor, ISD estimate or security theorem.

## Ring experiment

```sh
python experiments/ring_structure.py
```

Expected result: 128 quartic factors at q=257 and 769; 512 odd-power automorphisms.

Demonstrates: Polynomial identities and cyclotomic factor-degree calculation.

Does not establish: No lattice attack or key-recovery gain.

## Toy correlation

```sh
python experiments/toy_correlation.py
```

Expected result: 3136 pairs; exact multi-exceedance 0 versus iid 0.01804193.

Demonstrates: Small fixed-weight negacyclic dependence counterexample.

Does not establish: Toy parameters are not DAWN decryption behavior.

## Paired surrogate

```sh
python experiments/paired_noise_check.py
```

Expected result: beta joint/product ratio 966622.186.

Demonstrates: Dependence inside the restricted iid paired-transform surrogate.

Does not establish: No corrected real DAWN DFR; actual encoding and fixed-weight dependencies omitted.

## Regression checker

```sh
python experiments/check_reproduced_results.py
```

Checks exact modeled sizes, known rounded DFR model values, QC support entropies and ring identities. The original three codec tests remain separate. A green check is not a cryptographic security result.

## Build the PDF

The committed PDF can be read without installing typesetting tools. To rebuild it, use XeLaTeX (tested with TeX Live 2023) with Latin Modern Roman/Sans, Latin Modern Math, DejaVu Sans Mono, TikZ, booktabs, longtable, pdflscape, fancyhdr, fvextra, xurl and the normal Pandoc LaTeX dependencies. The standalone `.tex` file includes its preamble.

```sh
cd paper/source
mkdir -p build
xelatex -interaction=nonstopmode -halt-on-error -output-directory=build Compact_Post_Quantum_KEM_Tradeoff.tex
xelatex -interaction=nonstopmode -halt-on-error -output-directory=build Compact_Post_Quantum_KEM_Tradeoff.tex
xelatex -interaction=nonstopmode -halt-on-error -output-directory=build Compact_Post_Quantum_KEM_Tradeoff.tex
cp build/Compact_Post_Quantum_KEM_Tradeoff.pdf ../Compact_Post_Quantum_KEM_Tradeoff.pdf
```

To regenerate LaTeX from the publication Markdown, run `python build_source.py` in `paper/source/` (Pandoc 3.1.3 was used). The Markdown is a typesetting source containing raw LaTeX figures. It is not intended as the GitHub reading edition; use the PDF or the preserved Phase 5 manuscript.

PDF builds can differ in timestamps and font/library metadata. Numerical research output is the reproducibility target; byte-identical PDF output is not promised.

## Provenance and modifications

The seven original scripts received copyright/SPDX comments only; their mathematical behavior is unchanged. `check_reproduced_results.py` is a new publication regression checker. Equations derived from the author DFR model are identified in the source docstring with the pinned upstream commit. No third-party source tree or paper PDF is redistributed.

For CFF 1.2.0, the report is represented as `preferred-citation.type: report`; the top-level package metadata does not incorrectly use a top-level `type: report`.
