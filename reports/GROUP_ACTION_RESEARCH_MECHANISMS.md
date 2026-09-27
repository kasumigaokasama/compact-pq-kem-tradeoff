# Three research mechanisms and immediate falsification

These sketches are **not KEM specifications**, endorsements or implementation instructions. Classification applies to the project's simultaneous PQ128/size/runtime/CCA gate.

## M1 — plain enlarged CSIDH/CTIDH ephemeral action

**Action/public/secret:** regular quadratic ideal-class action; one curve coefficient \(A=a\cdot x\); bounded exponent vector sampled with distribution analysis. **Encapsulation/decapsulation:** send \(B=b\cdot x\), derive \(H(b\cdot A)=H(a\cdot B)\). **Assumption:** computational/hashed parallelisation plus any decisional/transform assumption; vectorisation alone insufficient. **Size:** at ~2260-bit p, PK ~283 B, raw CT ~283 B; at ~5280, ~660 B each; complete CCA CT unknown. **Classical:** collision/MITM, relation and weak-vector attacks. **Quantum:** hidden-shift vectors; no single certified exponent. **Validation:** supersingularity and action orbit, canonical encoding; expensive at large p. **CCA path:** formal PKE and quantum-aware FO or other proof, adds encrypted seed/tag and reencryption; unknown overhead. **Closest art:** CSIDH, CTIDH, CSIKE.

**Falsification:** 512-bit baseline cannot be casually called PQ128. Aggressive ~566 B pair leaves 184 B to stay <750 B, with uncertain quantum resource accounting and no complete CCA proof. Conservative ~1320 B pair already loses <1KB. Secret relations and multi-target tables need new parameter audit. **Classification: REJECTED under this project's gate.**

## M2 — module-action MIKE ephemeral exchange

**Action/public/secret:** 2024 Hermitian module monoidal action, public 64 B \(j\)-invariant over \(\mathbb F_{p^2}\); secret is module/isogeny data, not a CSIDH group element. **Encapsulation/decapsulation:** exchange ephemeral \(j\)-invariant, compute common dimension-four variety and hash a canonical shared invariant; last hashing specification is a *research requirement*, not a claimed published KEM. **Assumption:** announced AIM reduction to supersingular endomorphism ring problem for passive NIKE/KEM; active NIKE separately claimed. **Size:** PK 64 B claimed; raw ephemeral ~64 B inferred; CCA CT unknown. **Classical:** endomorphism/path and invalid-object attacks require independent concrete analysis. **Quantum:** no known direct regular-action hidden-shift reduction, but no concrete lower bound or FTQC resource estimate. **Validation:** \(\mathbb F_{p^2}\) supersingularity claimed in timing; full CCA object validation needs proof. **CCA path:** unspecified; prove decisional/hashed key and IND-CCA with exact transform and QROM losses. **Closest art:** Robert 2024 ⊗-MIKE, team 2026 announcement/AIM.

**Falsification:** no SIDH torsion images, but that only rules out a particular attack input. Kuperberg non-applicability is presumed, not a generic hardness theorem. The 2026 team's fast full exchange is an author benchmark, not an independent constant-time KEM benchmark. Complete CCA bytes, proof and loss absent in audited material. **Classification: UNCLEAR as future academic NIKE; REJECTED for Phase 4B construction gate.**

## M3 — accelerated regular action with published shifted curves

**Action/public/secret:** CSIDH-like class group, one base public curve plus many related hop curves and relation guidance; secrets bounded vectors. **Encapsulation/decapsulation:** attempt shorter online action using public precomputed shifted objects. **Assumption:** multi-input hidden-shift remains hard plus parallelisation. **Size:** for \(2^{12}\) extra 64 B curves, ~262,144 B auxiliary data; CT and CCA overhead additional. **Classical/quantum:** relation-assisted search and 2025 shifted-input attack examples \(2^{45}\) or \(2^{57}\) modeled T gates with large QRAM alternatives. **Validation:** each curve and its relation consistency. **CCA path:** unsolved with extra proof burden. **Closest art:** CSI-SharK/BCP shifted-input analysis, 2026 CRT-hop-curve warning.

**Falsification:** immediately fails compactness and creates attack side information; a quantum resource tradeoff can beat the single-curve setting. **Classification: REJECTED.**

These are mechanisms only. None survives *all* required criteria. [Robert 2024](https://eprint.iacr.org/2024/1556.pdf), [2025 shifted-input study](https://eprint.iacr.org/2025/376.pdf), [2026 CRT study](https://arxiv.org/abs/2609.26258), [dCTIDH](https://eprint.iacr.org/2025/107.pdf).
