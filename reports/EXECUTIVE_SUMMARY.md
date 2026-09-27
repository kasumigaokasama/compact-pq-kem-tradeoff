# Executive summary — Phase 5

**Question.** Why was no new substantially smaller, simple and high-confidence post-quantum KEM constructed? The joint requirements were short PK *and* CT, efficient honest operation and low memory, a stable average-case hardness story against classical and quantum attacks, rigorous correctness and a credible IND-CCA transform. A local byte improvement that fails any security gate does not meet the brief.

**Result · PROJECT-DERIVED, STRONGLY SUPPORTED within investigated families:** No investigated mechanism passed every gate. This does not prove a universal lower bound or ML-KEM optimality. The project deliberately terminated candidate construction.

| Branch | Most informative positive evidence | Limiting evidence | Decision |
|---|---|---|---|
| NTRU / DAWN | Modeled DAWN-β 514+450=964 B; independently reproduced grouping; author DFR model reproduced to nine decimals | Same-alphabet packing leaves only 2 B pair slack; real correlated/per-key DFR and primary full decoder unverified; BAT correction undiffed | Phase 2C **INSUFFICIENT EVIDENCE** formally; **NO** new NTRU construction |
| QC-Hamming | HQC 2025 spec 2241+4433=6674 B; BIKE research 1541+1573=3114 B; exact entropy arithmetic | HQC dense \(u,v\) serve decoding; secret decoder saves bytes but adds difficult rare DFR/weak-key and reaction analysis; no novel ≤2 KB pair path found | Phase 3 **NO-GO** |
| Group actions | CSIDH's historical 64 B curve; MIKE's 64 B Level-1 public-object and <5 ms exchange *author claim* | CSIDH hidden-shift tradeoffs force parameter-resource scrutiny; MIKE's concrete quantum margin, complete IND-CCA construction and CT bytes unknown | Phase 4A **NO-GO** for Phase 4B |

**Why ML-KEM recurred as control.** [FIPS 203](https://csrc.nist.gov/pubs/fips/203/final) specifies an IND-CCA-oriented Module-LWE KEM with PK+CT 1568/2272/3136 B at the three parameter sets. Its seeded matrix, polynomial representation and compression yield moderate sizes without relying on the novel mechanisms screened here. Standardization and broad analysis do not make it mathematically optimal or side-channel-proof.

**Engineering recommendation.** For present deployment, use standardized, reviewed PQ KEMs with protocol and side-channel safeguards. HQC is [selected for ongoing standardization](https://csrc.nist.gov/projects/post-quantum-cryptography), not yet labeled final FIPS here. Treat DAWN/BAT/BIKE/MIKE as research in the exact senses detailed in the paper.

**Reopen only with a changed gate:** independent MIKE quantum and CCA analysis, real DAWN correlated DFR and canonical source, BAT proof diff, rigorous per-key QC decoder, or other substantive new average-case mathematics. [FINAL_RESEARCH_PAPER.md](FINAL_RESEARCH_PAPER.md) carries the argument; [EVIDENCE_LEDGER.md](EVIDENCE_LEDGER.md) exposes the qualifications.
