# BAT proof-version comparison — blocked, with exact evidence boundary

**Primary record:** https://eprint.iacr.org/2022/031, checked 2026-09-27. It says “Fixing the error in the previous security proof” and lists a revision on **2026-04-12**; initial receipt was 2022-01-14. The “all versions” endpoint and PDF endpoints were inaccessible in this environment. A historical author manuscript is indexed at https://www.h2020prometheus.eu/sites/default/files/2022-06/main-2_0.pdf; it cannot serve as the post-correction text. The author's implementation is https://github.com/pornin/BAT, but no commit was pinned or code downloaded.

| Requested comparison | Pre-2026 text | 2026-04-12 text | Result |
|---|---|---|---|
| Full PDF SHA-256 | unavailable | unavailable | Cannot freeze either version |
| Theorem/lemma identifier | unavailable for reliable pairwise comparison | unavailable | **Unknown** |
| Incorrect game hop and reason | unavailable | unavailable | **Unknown** |
| Changed assumption, parameter, bound, query loss | unavailable | unavailable | **Unknown** |
| Classification | — | — | **UNCLASSIFIED**, not cosmetic by default |

No mathematical diff is asserted. The metadata is evidence of a correction, **not** evidence about which theorem changed or whether published concrete parameters survive. Any claim to identify the precise flaw from the metadata would fabricate a result. The next reproducible step is to obtain versioned PDFs from the authors/ePrint history, record hashes, run `pdftotext -layout` and a textual diff, then verify the changed proof algebra and code/parameter compatibility.
