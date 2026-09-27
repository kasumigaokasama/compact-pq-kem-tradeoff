# Rejected ideas and boundary conditions

| Idea | Why it fails now | Evidence that could reopen it |
| --- | --- | --- |
| Rebrand CSIDH-512 64 B as PQ128 CCA KEM | hidden-shift resource controversy and missing complete CCA bytes/proof | independent accepted concrete quantum model and complete KEM |
| Count one public curve and omit encapsulator curve | false communication ledger | exact serialized PK and ciphertext |
| Increase p silently while retaining 64 B claim | p determines field-element storage | valid compressed representation with security proof |
| Declare all isogenies broken from SIKE | Castryck–Decru requires SIDH torsion point images, absent in these bare public keys | attack adapted to precise disclosed data |
| Declare MIKE safe because Kuperberg is inapplicable | monoidal action has a different, less studied attack surface; “presumably” in original work | independent classical/quantum analysis and tight parameters |
| Hash raw shared curve and label IND-CCA | active decapsulation oracle and malformed-object inputs remain | explicit reduction and exact handling of malicious ciphertexts |
| Apply FO to NIKE without constructing correct reencryption PKE | transform hypotheses and QROM loss unspecified | full PKE/KEM algorithms and proof |
| Publish torsion images, orientations, CRT hop curves or many shifted curves to accelerate action | known SIDH leakage pattern, classical/quantum shifted-input attacks, larger bytes | explicit zero-knowledge/leakage bound and complete accounting |
| Treat CTIDH's speedup as a quantum-hardness result | same regular abelian hidden shift | genuinely different security structure |
| Transfer compact PRISM/CSI-FiSh signatures to KEM | identification/signature transcript and extraction do not supply shared secret or CCA security | independent encapsulation construction and reduction |
| Claim 2048-bit field is automatically NIST level 1 | field size does not determine all tradeoffs, distributions or oracle costs | parameter-specific full attack resource and keygen study |
| Port MIKE's <5 ms claim to constant-time CCA decapsulation | announced full exchange timing does not include a specified CCA transform | code, reproducible matched benchmark, validation and fault audit |

**Stop rule:** Phase 4B does not construct a new candidate under current requirements. The project uses established PQ KEMs for engineering needs. Reassessment would be triggered by genuinely new, independently reviewed mathematical and CCA evidence, not by an unexamined switch to another exotic family.
