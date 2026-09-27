# DAWN DFR: author model reproduced, actual tail unresolved

## Primary model and independent calculation

The [authors' DFR repository](https://github.com/Icarid-Liu/lattice-KEM-DFR-estimator), pinned to `3c2602c30e13ce15ed7094ef97d9e4ed2dde01f6`, supplies a Sage notebook for both 512 variants. It models the coefficient law of `g*s`, `f*(e+rounding)`, and `f*m` by independent products/sums, forms **two independent copies** of the first two laws plus the `f*m` law, then applies binomial tail formulas for (P1) two or more exceedances and (P2) a decoder-position event. Its α rounding law is uniform `[-3,3]`; β rounding law uniform `{0,1}`. The notebook's stored outputs are `-132.676946973757` and `-130.133613253826` in log base 2.

`experiments/reproduce_dawn_dfr_model.py` independently combines per-index positive probability kernels, computes 512-fold convolutions in float64, and sums rare-event tails directly (avoiding `1-(1-p)^n` cancellation). It matches the authors' three printed exponents for each set to nine decimals:

| Set | `log2(P1)` | `log2(P2)` | `log2(P1+P2)` |
|---|---:|---:|---:|
| α-512 | -133.146278336 | -134.525344151 | **-132.676946974** |
| β-512 | -130.534566517 | -132.176710226 | **-130.133613254** |

This verifies **arithmetic under the authors' independence model**, not that it upper-bounds honest-key DFR. The author utility uses approximate rationalization and tail cutoffs; our positive float64 convolution makes a distinct numerical implementation and obtains the same figures. It treats the compressed rounding residual as uniform and independent, even though the actual residual is determined by the public key and encryption inputs. The model also samples fixed-weight polynomial coefficients as if independent within and across products.

## Explicit dependency graph

For secret `f,g`, ephemeral `s,e`, message `m`, public ratio `h=g/f`, and deterministic rounding `ρ=ρ(h,s,e,m)`, define `A=gs+f(e+ρ)`. The exact transcribed algebra yields effective integer expression `Z=tA+u f m`, `u=y²-y³`; wraps are `K=(Z-L_q(Z))/q` under a matching lift. Edges: `f↔h↔ρ`; `g↔h↔ρ`; `s,e,m↔ρ`; `f↔f(e+ρ)↔f m`; each fixed-weight sampler couples its own coefficients; convolution couples output coefficients; `t` explicitly pairs indices `i` and `i+256`. In particular, if `A_i,A_(i+256)` were independent, then `(tA)_i=A_i-A_(i+256)` and `(tA)_(i+256)=A_i+A_(i+256)`. These two outputs share both inputs and are generally dependent even if their covariance vanishes.

`experiments/paired_noise_check.py` measures this **restricted iid surrogate**, with actual `n=512` author parameter weights but omitting `u f m`, actual rounding dependence and fixed-weight cross-coefficient dependence. For β it obtains single exceedance `5.7171e-25`, joint paired exceedance `3.1594e-43`, versus product of marginals `3.2685e-49` (ratio about `9.67e5`). For α the analogous ratio is about `477`. These results show that a binomial *joint* calculation is not exact even after granting the author's iid input law. The absolute joint effect cannot be inserted into the real DFR without the omitted encoding term and full decoder logic. This is an **anomaly in the approximation**, not a proven vulnerability or a corrected `2^-x` value.

## Sensitivity of the reproduced model

| β-512 change, all else fixed | `log2` model DFR | Interpretation |
|---|---:|---|
| rounding error exactly 0 | -216.146 | Hypothetical no-rounding baseline; larger ciphertext would be expected |
| uniform `{0,1}` (authors) | **-130.134** | Published modeled setting |
| uniform `{-1,0,1}` | -114.743 | One extra rounding-error value strongly worsens tail |
| reduce `kg` 64→60 | -132.482 | Secret distribution/security changes, so not a free gain |
| reduce `kf` 32→28 | -142.123 | Particularly sensitive; sparse-secret attack may improve |
| reduce `ks` 48→44 | -133.281 | Also changes ephemeral security |
| reduce `ke` 64→60 | -131.879 | Also changes RLWE distinguishing costs |

These are finite differences **only in the author independence model**. They point to rounding width and secret weight as active modeled ciphertext bottlenecks, but do not justify selecting new parameters.

## What remains unbounded

No defensible 512-level numerical upper bound or confidence interval for *actual* average, key-conditioned, message-conditioned or adversarial-input DFR is established. Ordinary Monte Carlo cannot verify `~2^-130`. A suitable next method is a conditional-on-key generating-function or importance-sampling analysis that preserves shared `f,g` and the paired transform, followed by rigorous error control of rare-event weights and cross-check against the actual decoder/reference implementation. Input handling and FO implicit rejection also need code measurements. Until then the statement “DFR is `2^-130`” must be read as **the output of a documented approximation**.
