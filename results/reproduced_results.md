# Reproduced results

Publication rerun on 27 September 2026: Linux x86-64, Python 3.12.14, NumPy 2.3.5. All original scripts exited successfully. These are actual project rerun outputs; literature security claims are not classified as project-reproduced.

## DAWN codec

**Result / expected output:** Grouped sizes 615/436/514/450 B; minima 614/435/513/449 B.

**Script / command:** `python experiments/dawn_codec.py`

**Interpretation:** Exact modeled representation accounting.

**Limitation:** No official wire compatibility or KEM security.

```text
alpha_pk: grouped_bits=4916 actual=615B entropy=4908.461971bits minimum=614B slack=1B
alpha_ct: grouped_bits=3482 actual=436B entropy=3472.056173bits minimum=435B slack=1B
beta_pk: grouped_bits=4106 actual=514B entropy=4101.748355bits minimum=513B slack=1B
beta_ct: grouped_bits=3594 actual=450B entropy=3589.748355bits minimum=449B slack=1B
```

## Original codec unit tests

**Result / expected output:** 3 tests pass.

**Script / command:** `python -m unittest discover -s experiments -p 'test_*.py' -v`

**Interpretation:** Seeded round trips, boundary vectors and local malformed encoding rejection.

**Limitation:** No production hardening, constant-time audit or cryptographic proof.

```text
test_invalid_group_field (test_dawn_codec.TestCodec.test_invalid_group_field) ... ok
test_invalid_length_and_padding (test_dawn_codec.TestCodec.test_invalid_length_and_padding) ... ok
test_roundtrips_and_boundaries (test_dawn_codec.TestCodec.test_roundtrips_and_boundaries) ... ok

----------------------------------------------------------------------
Ran 3 tests in 0.086s

OK
```

## DAWN DFR model

**Result / expected output:** alpha log2 −132.676946974; beta −130.133613254.

**Script / command:** `python experiments/reproduce_dawn_dfr_model.py`

**Interpretation:** The specified author independence-model arithmetic.

**Limitation:** Not actual correlated, per-key or adversarial-input DFR.

```text
n=512 q=769 rounding=range(-3, 4)
 P1=8.298056923815e-41, log2=-133.146278336
 P2=3.190334597218e-41, log2=-134.525344151
 DFR_model=1.148839152103e-40, log2=-132.676946974
n=512 q=257 rounding=range(0, 2)
 P1=5.072008904858e-40, log2=-130.534566517
 P2=1.624970547882e-40, log2=-132.176710226
 DFR_model=6.696979452740e-40, log2=-130.133613254
```

## QC entropy analysis

**Result / expected output:** HQC-1 622.952/694.542 support bits; BIKE-1 error 1196.018 bits.

**Script / command:** `python experiments/qc_entropy_frontier.py`

**Interpretation:** Binomial support entropy and dense-byte arithmetic.

**Limitation:** Not a public compressor, ISD estimate or security theorem.

```text
HQC-1: n=17669 L=17664 k=128 rate=0.00724638, redundancy=17536
  PK=2241; CT=4433 [u=2209, v=2208, salt=16]; DK=2321 / seed=32; K=32
  padding PK_s=3, CT_u=3, CT_v=0 bits
  support entropy each x/y=622.952, r1/r2/e=694.542 bits
  Hamming ball log2 V(L,75)=694.517 bits (illustrative, not decoder radius)
HQC-3: n=35851 L=35840 k=192 rate=0.00535714, redundancy=35648
  PK=4514; CT=8978 [u=4482, v=4480, salt=16]; DK=4602 / seed=32; K=32
  padding PK_s=5, CT_u=5, CT_v=0 bits
  support entropy each x/y=988.008, r1/r2/e=1105.304 bits
  Hamming ball log2 V(L,114)=1105.258 bits (illustrative, not decoder radius)
HQC-5: n=57637 L=57600 k=256 rate=0.00444444, redundancy=57344
  PK=7237; CT=14421 [u=7205, v=7200, salt=16]; DK=7333 / seed=32; K=32
  padding PK_s=3, CT_u=3, CT_v=0 bits
  support entropy each x/y=1334.285, r1/r2/e=1490.485 bits
  Hamming ball log2 V(L,149)=1490.350 bits (illustrative, not decoder radius)
BIKE-1: r=12323 d=71 t=134; PK=1541 CT=1573 pair=3114
  entropy secret pair=1251.858; error pair=1196.018 bits
  Hamming ball log2 V(24646,134)=1196.026 bits
BIKE-3: r=24659 d=103 t=199; PK=3083 CT=3115 pair=6198
  entropy secret pair=1915.325; error pair=1864.062 bits
  Hamming ball log2 V(49318,199)=1864.068 bits
BIKE-5: r=40973 d=137 t=264; PK=5122 CT=5154 pair=10276
  entropy secret pair=2638.363; error pair=2560.301 bits
  Hamming ball log2 V(81946,264)=2560.306 bits
HQC-1 pair=6674; 20% target <= 5339 bytes; ML-KEM-512 pair=1568
  CT <= 2048 requires >= 2385 bytes removed; either dense component alone plus salt >= 2224
  CT <= 1536 requires >= 2897 bytes removed; either dense component alone plus salt >= 2224
  CT <= 1024 requires >= 3409 bytes removed; either dense component alone plus salt >= 2224
  CT <= 750 requires >= 3683 bytes removed; either dense component alone plus salt >= 2224
  CT <= 500 requires >= 3933 bytes removed; either dense component alone plus salt >= 2224
```

## Ring experiment

**Result / expected output:** 128 quartic factors at q=257 and 769; 512 odd-power automorphisms.

**Script / command:** `python experiments/ring_structure.py`

**Interpretation:** Polynomial identities and cyclotomic factor-degree calculation.

**Limitation:** No lattice attack or key-recovery gain.

```text
identities: w*u=t; w*(1-y+y²-y³)=2; t²=2y²
q=257: ord_1024(q)=4, irreducible factors=128, degree each=4
q=769: ord_1024(q)=4, irreducible factors=128, degree each=4
odd-power automorphisms modulo 1024: 512
```

## Toy correlation

**Result / expected output:** 3136 pairs; exact multi-exceedance 0 versus iid 0.01804193.

**Script / command:** `python experiments/toy_correlation.py`

**Interpretation:** Small fixed-weight negacyclic dependence counterexample.

**Limitation:** Toy parameters are not DAWN decryption behavior.

```text
n=8, weight=(+1,-1), threshold=1, total=3136
P(single exceed)=3/112 (0.02678571)
P(at least 2), exact=0 (0.00000000)
P(at least 2), iid=63815922298017/3537090251849728 (0.01804193)
event-count histogram=[2576, 560, 0, 0, 0, 0, 0, 0, 0]
```

## Paired surrogate

**Result / expected output:** beta joint/product ratio 966622.186.

**Script / command:** `python experiments/paired_noise_check.py`

**Interpretation:** Dependence inside the restricted iid paired-transform surrogate.

**Limitation:** No corrected real DAWN DFR; actual encoding and fixed-weight dependencies omitted.

```text
n=512 q=257 |A_i-A_j|>128: 5.717076364e-25
paired exceed probability=3.159400956e-43; iid product=3.268496215e-49
pair/iid ratio=966622.186
n=512 q=769 |A_i-A_j|>384: 8.851564900e-24
paired exceed probability=3.737524506e-44; iid product=7.835020118e-47
pair/iid ratio=477.028068
```

