# BAT 2026 proof correction: unavailable versioned pair

The [IACR ePrint record](https://eprint.iacr.org/2022/031) lists a **2026-04-12** revision and states that it fixes an error in the previous security proof. The [TCHES 2022 publication](https://tches.iacr.org/) and a historical author-hosted PDF can serve as an older baseline only after an exact version is pinned. The ePrint version-history and PDF endpoints were restricted in the research interface; the 2026 version was not obtained. Springer is not a BAT proof substitute. The [author BAT code](https://github.com/pornin/BAT) also cannot establish a proof change.

| Field | Latest pre-2026 version | Revision of 2026-04-12 | Result |
|---|---|---|---|
| Versioned PDF URL, SHA-256, page count | Not obtained | Not obtained | **BLOCKED** |
| Lemma/theorem/game hop and changed equation | Unknown | Unknown | **BLOCKED** |
| Added assumption or changed adversary model | Unknown | Unknown | **BLOCKED** |
| Advantage loss, query bound, concrete security, BAT-512 parameters | Unknown | Unknown | **BLOCKED** |
| Required classification | — | — | **UNCLASSIFIED**; no basis for “minor repair” |

No text/equation/theorem/dependency diff is fabricated. Precisely needed external artifacts: **(a)** the latest immutable ePrint 2022/031 PDF before 2026-04-12, **(b)** the ePrint 2022/031 revision dated 2026-04-12. On receipt, hash both, extract text/equations, identify identifiers and redo the proof dependency tree. Until then the claim that BAT-512's corrected proof preserves its assumptions and parameters is **unknown**.
