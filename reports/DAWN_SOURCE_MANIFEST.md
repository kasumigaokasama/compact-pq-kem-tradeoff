# DAWN source manifest — 2026-09-27 UTC

| Artifact | URL | Version/date | Bytes/hash | Role/status |
|---|---|---|---|---|
| IACR ePrint record | https://eprint.iacr.org/2025/1520 | Four revisions, last 2025-10-27; accessed 2026-09-27 | HTML not locally saved; SHA-256 unavailable | Primary metadata and abstract: 436-byte α ciphertext, 964-byte β combined claim |
| Canonical ePrint PDF | https://eprint.iacr.org/2025/1520.pdf | Intended last revision | **Not obtained**; web retrieval restricted | Cannot pin PDF SHA-256, algorithms, theorem text or Table 8 to this source |
| ASIACRYPT proceedings | https://doi.org/10.1007/978-981-95-5099-9_13 | 2025 | **Not obtained** | Alternative primary full text; access unconfirmed |
| Official author implementation | not located in primary records examined | unknown | No commit or vectors | No byte-for-byte comparison possible |
| Phase 2A report | local `PQC-Phase-2A-Compact-NTRU-Audit.md` | 2026-09-27 | local analysis | Hypothesis source, not primary evidence |
| Independent model code | `experiments/dawn_codec.py` | 2026-09-27 | SHA-256 `bfb3fdd74abe89a4cb11e9d1679921d24757c95f4353e210df630fa6c733f0a3` | Derives grouping from Phase 2A's transcription; **not** official wire specification |
| Codec tests | `experiments/test_dawn_codec.py` | 2026-09-27 | SHA-256 `bf788d99162a92a8243f379ed06b478d5090a932f40ebd088d4af6b912784f2c` | Independent tests |
| Toy correlation experiment | `experiments/toy_correlation.py` | 2026-09-27 | SHA-256 `e19dcd5c7c46b90c4e200f7582a6b7a0ce468314c08b516eafb8447a9c02b0ae` | Explanatory counterexample, not DAWN parameters |

The ePrint page describes the 2025-10-27 manuscript as a minor revision of the ASIACRYPT publication. PDF endpoints returned a restricted-URL error; no checksum has been invented. A separately accessible Scribd manuscript was used in Phase 2A and to identify questions here, **never as sole proof of a security-critical conclusion**. Its order of bit fields is insufficient to establish byte-for-byte compatibility.

**Gate:** no conclusion about exact theorem wording, DAWN's deployed DFR or reference-code correctness until a canonical full text and matching code (if available) have been obtained, hashed and compared.
