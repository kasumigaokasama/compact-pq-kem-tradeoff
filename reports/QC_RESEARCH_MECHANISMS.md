# Attack-first mechanism screen

No new mechanism has the evidence required to enter Phase 4 construction. To make the central public/secret-decoder question concrete, three **research hypotheses** were challenged, with outcomes below. They are not schemes, parameters or security claims.

## M1 — Replace the public codeword with a secret-decodable syndrome

- Current bottleneck / change: remove 2208-byte HQC-1 `v` and recover a weight-bounded error from `u` using a hidden sparse parity check; expected arithmetic saving >20%.
- Honest recovery / assumption: a QC-MDPC decoder and hardness of both QC syndrome decoding and sparse dual recovery, with per-key rare-tail control.
- Attack and DFR: ISD for message recovery, low-weight dual and rotation attacks for check recovery, weak-key/error-floor and adaptive reaction attacks; quantum ISD/list attacks require memory models. CCA reencryption must remain canonical and constant time.
- Closest prior art: **BIKE**, 2026 [bounded-DFR QC-MDPC work](https://eprint.iacr.org/2025/1043). **REJECTED AS A NEW MECHANISM**: size advantage is real but occupied by established constructions; DFR proof gap is the hard part.

## M2 — Split a decoder between a public code and a small private hint

- Current bottleneck / change: shorten `v` by ≥1335 bytes of pair communication while retaining `u`, with a compact private or seeded hint enabling recovery.
- Honest recovery / assumption: secret-assisted correction beyond public RMRS radius; must identify an exact hint distribution and reduction distinct from existing QC-MDPC/syndrome designs.
- Attack and DFR: publicly inferable sparse hint invites low-weight dual search, linearization and rotation/orbit filtering; secret hint creates key-dependent failures and reaction oracles. Multi-sample use can amplify any hint leakage. CCA encoding needs a unique representation.
- Closest prior art: BIKE, QC-LDPC/LEDAcrypt, [2026 semi-MDPC](https://link.springer.com/article/10.1186/s42400-026-00576-5) and [2026 bounded-DFR QC-MDPC](https://eprint.iacr.org/2025/1043). **UNCLEAR**: no exact decoder, size, per-key DFR, security assumption or novelty proof; does not qualify as a surviving design mechanism.

## M3 — Embed the message in a coset and jointly represent ciphertext components

- Current bottleneck / change: avoid explicit `v` codeword by choosing a coset/syndrome class so receiver derives `m` from a compact syndrome; at least 887 CT bytes needed for 20% CT-only improvement.
- Honest recovery / assumption: an efficiently decodable keyed quotient preserving hard QC syndrome decoding and FO reencryption.
- Attack and DFR: public coset maps can linearize the message or reveal the chosen error; secret cosets revert to a hidden decoder with low-weight dual and reaction risk. Joint entropy is small only because the message/seed is secret; publishing it loses KEM secrecy. Quantum ISD and multikey search remain. No concrete CCA transform or constant-time decoder was obtained.
- Closest prior art: Niederreiter, Classic McEliece, BIKE and HQC original framework. **REJECTED AS A READY MECHANISM**; no distinct secure construction was derived.

No candidate has a defensible estimate for PK/CT/secret bytes, peak RAM, stack, CPU or decoder iterations *at new parameters*. The existing BIKE comparison has `3114 B` PK+CT at level 1 and slower/key-sensitive decoding, already far below HQC's `6674 B` but still above the requested 2-KB pair target. The 2026 DFR literature makes this an active research field, not an empty novelty slot. ML-KEM-512's `1568 B` pair is the mature size/control baseline; code-based assumption diversity is a genuine reason to use **existing HQC** despite bandwidth, rather than a reason to publish an unsupported new KEM.
