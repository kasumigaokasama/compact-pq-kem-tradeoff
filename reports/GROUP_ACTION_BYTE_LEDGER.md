# Byte ledger — public key plus transmitted encapsulation

**Counting rule:** count the recipient's public key once plus all bytes sent by the encapsulator. Do not count shared secret output as network bytes. Unpublished CCA components are **unknown**, never zero. \(\lceil\log_2p/8\rceil\) is a field-element storage lower bound, subject to actual format and canonical validation; it is not a proof that every curve requires all those bits.

| Case | Recipient PK | Ephemeral object | Other mandatory CT | Complete PK+CT | Evidence |
| --- | ---: | ---: | --- | --- | --- |
| ML-KEM-512 | 800 | included in 768 CT | included | **1568** | FIPS 203 exact |
| DAWN-beta project control | — | — | — | ~964 | research control, not standardized |
| BIKE-1 project control | — | — | — | ~3114 | research control |
| HQC-1 project control | — | — | — | ~6674 | research control |
| CSIDH-512 historic raw NIKE | 64 | 64 | none in raw NIKE | **128 raw** | historically published, PQ128 disputed |
| CSIDH-like 2048-bit raw | ~256 | ~256 | none in raw NIKE | **~512 raw** | size arithmetic; PQ128 not certified |
| CSIDH-like 2260-bit raw | ~283 | ~283 | none in raw NIKE | **~566 raw** | proposed aggressive parameter, no CCA proof |
| CSIDH-like 5280-bit raw | ~660 | ~660 | none in raw NIKE | **~1320 raw** | proposed conservative parameter, no CCA proof |
| MIKE Level 1 announced raw exchange | 64 claimed | 64 **inferred** from symmetric public-curve exchange | none in raw NIKE | **~128 raw inference** | not an IND-CCA byte specification |
| MIKE complete CCA KEM | 64 claimed | likely curve object | validation tag/proof/binding unknown | **unknown** | no verified specification |
| CSIKE 2022 | CSIDH curve | curve / scheme-specific data | additional tag, size depends on scheme | **unverified** | CCA claim not matched to modern PQ128 budget |

**Thresholds:** under 500 B, only the 128 B historical/MIKE raw examples qualify, with material security qualifications. Under 750 B, the aggressive ~566 B plain CSIDH pair qualifies as *raw* exchange; any CCA overhead must fit <184 B. Under 1000 B, that pair has <434 B headroom, while conservative 1320 B fails before overhead. MIKE has enormous nominal headroom, but a CCA transform and security proof, including validation and ciphertext format, are missing. A tag of 16/32 B or commitment of 32 B shown in a future design would be additional bytes, not a measured result or a universally sufficient transform.

**Auxiliary-data multiplier:** publishing \(2^{12}\) shifted 64-byte curves costs ~262,144 B, even before security degradation. Publishing a basis, torsion images, orientation witness, or NIZK has scheme-specific sizes and can change attack complexity. Do not squeeze those into “curve size.” Static pk and ephemeral pk are both public objects even when the ephemeral one is called a ciphertext.

Sources: [FIPS 203](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.203.pdf); [quantum parameter discussion](https://zhengxuisogeny.github.io/Isogeny-Based-Cryptography/index/quantumcsidh.pdf); [module action](https://eprint.iacr.org/2024/1556.pdf); [MIKE team announcement](https://mailarchive.ietf.org/arch/msg/cfrg/QM3t6di1bsgla6iIJ3gN6BbDoVk/); [CSIKE](https://doi.org/10.1515/jmc-2022-0007). Rough rows are arithmetic scenarios, not published parameter-set KEM totals.
