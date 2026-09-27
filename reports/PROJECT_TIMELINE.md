# Logical project timeline

| Stage | Why attempted | Pivot and decision |
|---|---|---|
| Initial goal | Smaller post-quantum KEM with low communication, CPU/RAM and credible IND-CCA | Replace “unbreakable” with explicit threat models; count PK and CT together |
| Phase 1 landscape | Survey lattice, code, rank, multivariate, isogeny, tensor and exploratory areas | C3 NTRU, C5 QC-Hamming, C7 group actions selected for attack-led scrutiny; UNKNOWN ≠ HARD |
| Phase 2A NTRU | DAWN/BAT showed compact prior art | Reproduce packing, proof and DFR before considering new design |
| Phase 2B reproduction | Test codec, quotient algebra, toy dependence | Four modeled sizes and two-byte beta slack reproduced; canonical source/BAT diff blocked; **NOT YET** |
| Phase 2C NTRU decision | Test ≥5% gain with correctness and security gates | DFR *model* reproduced, actual tail unknown; formal **INSUFFICIENT EVIDENCE**, **NO** new construction |
| Phase 3 QC-Hamming | Diversify beyond lattices | HQC dense public decoding versus BIKE private decoder and failure burden; **NO-GO** |
| Phase 4A group actions | Test unusually small curve objects | Hidden-shift parameter tradeoffs; MIKE CCA/quantum evidence incomplete; **NO-GO** |
| Phase 5 synthesis | Explain negative result and future evidence needed | No new KEM; standardized reviewed primitives for deployment |

This is a logical research path, not a claim of long independent field trials. See [EVIDENCE_LEDGER.md](EVIDENCE_LEDGER.md).
