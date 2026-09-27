# From action exchange to PKE and CCA KEM

## The missing implications

Given recipient public \(A=a\cdot x\), an encapsulator samples \(b\), sends \(B=b\cdot x\), and derives \(H(b\cdot A,B,A,context)\). Decapsulation computes \(H(a\cdot B,B,A,context)\). Correctness follows from commutativity in CSIDH, or the corresponding module identity in MIKE. **Passive key secrecy** needs more than inability to recover \(a\): a parallelisation/CDH-style or hashed/decisional assumption and a suitable proof. An adaptive adversary can submit arbitrary \(B\) for decapsulation; hashing alone does not supply IND-CCA.

| Route | Needed security work | Communication consequence | ROM/QROM status for considered system |
| --- | --- | --- | --- |
| Raw hashed action | parallelisation/decisional hardness, random-oracle extraction, key binding and validation | one ephemeral curve plus recipient PK | passive/CPA story only unless a specific active NIKE theorem applies |
| Action-derived PKE + Fujisaki–Okamoto style reencryption | deterministic coins from message/PK/context, correct PKE, decapsulation reencryption and constant-time comparison, fallback key | ciphertext includes ephemeral object and encrypted seed/tag; exact sizes depend on PKE | generic FO QROM analyses exist; no plug-and-play theorem asserted for MIKE or CSIDH without checking hypotheses/reduction loss |
| KEM from active NIKE / authenticated encapsulation | formal IND-CCA game and simulator able to handle decapsulation queries | at least ephemeral object; binding/authentication/proof data may be needed | announced MIKE “actively-secure NIKE” and AIM passive NIKE/KEM are distinct claims; no verified concrete IND-CCA proof |
| NIZK / proof of well-formed action or consistency | soundness and zero knowledge under quantum queries; extraction in chosen-ciphertext reduction | proof, commitments, challenges/responses, possibly more curves; unknown bytes | a CSIDH signature/QROM proof does not directly instantiate compact KEM |
| Existing CSIKE (2022) | examine its precise IND-CCA reduction, assumption, tag format and quantum security at enlarged p | extra tag and possibly other fields | published CCA claim; matched PQ128 byte/QROM audit not completed |

Generic FO is not a free wrapper on a bare NIKE: it usually starts with an encryption mechanism whose randomness can be regenerated, decrypted message recovered and ciphertext reencryption checked. Building such PKE from group actions can need extra assumptions and transmitted masked message/seed. Generic ROM proof does not automatically survive quantum random-oracle queries; reductions can be loose and require explicit domain separation, correctness, public-key validation and ciphertext binding. For MIKE the announced proof is in an *algebraic isogeny model* and described as passive NIKE or KEM from supersingular endomorphism ring; neither “KEM” as a primitive name nor “actively secure NIKE” alone certifies IND-CCA. [MIKE announcement](https://mailarchive.ietf.org/arch/msg/cfrg/QM3t6di1bsgla6iIJ3gN6BbDoVk/), [AIM](https://eprint.iacr.org/2026/032), [FO modular analysis](https://eprint.iacr.org/2017/604), [CSIKE](https://doi.org/10.1515/jmc-2022-0007).

## CCA audit gate

Before a byte claim: provide algorithms and exact serialization; explicit IND-CCA or IND-CCA2 definition; a classical and quantum reduction with loss as function of oracle and decapsulation queries; exact hardness assumption; deterministic reencryption or alternative simulator; implicit rejection; malformed-point validation and cost; multi-user and decryption-failure analysis. Report \(PK,CT,PK+CT\) at the **same** parameter set and benchmark all actions/validation/hash/reencryption. No audited branch passes this gate in Phase 4A.
