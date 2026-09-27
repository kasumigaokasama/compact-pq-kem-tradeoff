# DAWN ring, projections and automorphisms

Let `A=Z[x]/(x^512+1)` and `Rq=A/qA` with `q∈{257,769}`. Since `x^512+1=Φ_1024(x)`, it is irreducible over `Q`. For each listed prime, `q²≡513 (mod 1024)` and `q⁴≡1 (mod 1024)`, so `ord_1024(q)=4`. The finite-field cyclotomic theorem gives 128 distinct irreducible degree-four factors `P_j` and an exact isomorphism

`Rq ≅ ∏_(j=1)^128 F_q[x]/(P_j) ≅ ∏_(j=1)^128 F_(q^4)`.

`experiments/ring_structure.py` checks the modular order/factor count and the integral identities used below. The CRT statement uses the standard factor-degree theorem; the script does not factor all 128 polynomials.

## Image of the encryption variables

For each `j`, let `π_j(a)=a mod P_j`, a ring homomorphism. Then `f_j=π_j(f)`, `g_j=π_j(g)`, `s_j=π_j(s)`, `e_j=π_j(e)`, `m_j=π_j(m)`, `h_j=g_j/f_j` when `f_j≠0`, and `a_j=h_j s_j+e_j+w_j^-1m_j` in `F_(q^4)`. The ciphertext has the image `C_j=a_j+ρ_j` modulo `q`, where `ρ` is the deterministic coefficient-rounding residual, **not** an independently sampled projected noise. Similarly `t_j f_j C_j=t_j(g_j s_j+f_j(e_j+ρ_j))+u_j f_j m_j`. The encryption and algebra commute with projection over `F_q`; coefficientwise center lifting and message decoding do not generally commute with it.

In a quartic component, the image of a binary or ternary 512-coefficient vector is a *field element*, not a four-coordinate small vector. The same 512 coefficients and fixed-weight constraint determine all 128 component images; they cannot be treated as independent keys. Conditional on a given `h_j`, any nonzero `f_j` has `g_j=h_j f_j` in the component, so that isolated equation does not recover a short global pair. Some components may leak distinguishability if the induced low-weight image deviates measurably from uniform or an exceptional `f_j=0` is possible; these require exact distribution calculations. Candidate filtering across factors and meet-in-the-middle would have to maintain consistency of the global small polynomial and beat ordinary NTRU lattice/hybrid attacks. **No projected key recovery, message recovery or distinguisher is demonstrated.**

## Automorphisms and related samples

Every odd `a mod 1024` defines `σ_a:x↦x^a` on `A` and `Rq`, giving `φ(1024)=512` automorphisms. They permute/conjugate CRT components and map `f h=g` to `σ_a(f)σ_a(h)=σ_a(g)`. This creates correlated equivalent equations from one public key. It does not make 512 independent observations of the underlying secret. For encapsulations under a reused key, transformed ciphertexts can be analyzed alongside the originals but inherit shared coefficient and projection dependencies. This cyclotomic automorphism exposure is familiar in standard ring NTRU and Ring-LWE analyses; an improvement requires an attack exploiting this scheme's actual message/rounding distribution or decoding key.

The algebraic relation `t=1+x^256`, `w=1+x^128`, `u=x^256-x^384` satisfies `wu=t` in `A`. Its exact support pairing is relevant to the DFR dependency audit. Structural factorization alone does not imply a 4-dimensional hardness level or a break.
