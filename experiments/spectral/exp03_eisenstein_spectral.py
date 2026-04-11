"""
EXP03: Eisenstein Structure in the QNM Spectrum

Primary question:
  The entropy identity S_Λ = S_b + S_c + sqrt(S_b*S_c) is exact and follows
  from the Eisenstein constraint r_b^2 + r_b*r_c + r_c^2 = 3/Λ.

  Does any analogous structure exist in the QNM spectrum?

  Specifically:
  (a) Is there an exact or approximate combination of QNM frequencies
      omega_{l,n}(x) that is invariant under x -> 1-x (the Nariai symmetry)?
  (b) Does the overtone ratio omega_{l,1}/omega_{l,0} have a simple closed-form
      dependence on x?
  (c) Does the combination omega_re^2 + omega_re*omega_im + omega_im^2 (the
      Eisenstein norm of the frequency) show any special behavior?
  (d) Is there any spectral combination that is a function of S_b, S_c, or
      Delta = sqrt(S_b*S_c) alone?

These tests directly probe whether the Eisenstein geometry of the state space
is reflected in the QNM observables.
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import numpy as np
import json
import matplotlib
from src.json_utils import NumpyEncoder
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from src.sds_physics import sds_from_x
from src.wkb_qnm import wkb_3rd_order

RESULTS_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'results')
FIGURES_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'figures')
os.makedirs(RESULTS_DIR, exist_ok=True)
os.makedirs(FIGURES_DIR, exist_ok=True)


def test_nariai_symmetry():
    """
    The Nariai limit is x -> 1 (r_b -> r_c). There is no exact symmetry
    x -> 1-x in SdS thermodynamics. But the potential maximum location
    r_max/r_c is roughly symmetric in x for the angular potential.

    Test: Is omega_re(x, l, n) / omega_re(1-x, l, n) close to 1?
    If yes: approximate symmetry. If not: no symmetry.
    """
    print("\n=== TEST 1: x -> 1-x Symmetry Test ===")
    lam = 1.0
    x_vals = np.linspace(0.05, 0.45, 20)  # pairs (x, 1-x) up to x=0.45

    results = []
    for l, n in [(2, 0), (3, 0), (2, 1)]:
        print(f"  l={l}, n={n}:")
        for x in x_vals:
            x2 = 1.0 - x
            if x2 >= 0.99:
                continue
            s1 = sds_from_x(x, lam)
            s2 = sds_from_x(x2, lam)
            if s1 is None or s2 is None:
                continue
            r1 = wkb_3rd_order(s1, l=l, n=n)
            r2 = wkb_3rd_order(s2, l=l, n=n)
            ratio_re = r1.omega.real / r2.omega.real
            ratio_im = r1.omega.imag / r2.omega.imag
            results.append({'x': x, 'x2': x2, 'l': l, 'n': n,
                             'ratio_re': ratio_re, 'ratio_im': ratio_im})

        symm_re = [abs(r['ratio_re'] - 1) for r in results if r['l'] == l and r['n'] == n]
        if symm_re:
            print(f"    Max |ratio_re - 1|: {max(symm_re):.4f}  "
                  f"(0 = exact symmetry, >0.1 = no symmetry)")

    return results


def test_overtone_ratio():
    """
    Compute omega_{l,1} / omega_{l,0} as a function of x.
    If the scaling law holds, the Lambda cancels and this ratio depends on x only.
    The question is whether this ratio has algebraic simplicity.

    Compare to the entropy ratio: S_b/S_c = x^2, or sqrt(S_b/S_c) = x.
    Does omega_{l,1}/omega_{l,0} have a simple polynomial form in x?
    """
    print("\n=== TEST 2: Overtone Ratio omega_{l,1}/omega_{l,0} ===")
    x_values = np.linspace(0.05, 0.88, 300)  # n=1 requires l>=2 and n<l
    lam = 1.0
    l = 2  # l=2, n=0 and n=1

    ratios_re, ratios_im = [], []
    x_valid = []

    for x in x_values:
        state = sds_from_x(x, lam)
        if state is None:
            continue
        res0 = wkb_3rd_order(state, l=l, n=0)
        res1 = wkb_3rd_order(state, l=l, n=1)
        # Note: n=1 WKB-3rd often has large corrections (converged=False) but
        # still gives a useful frequency estimate for ratio analysis.
        if res0.omega == 0 or res1.omega == 0:
            continue
        ratio_re = res1.omega.real / res0.omega.real
        ratio_im = res1.omega.imag / res0.omega.imag
        ratios_re.append(ratio_re)
        ratios_im.append(ratio_im)
        x_valid.append(x)

    xv = np.array(x_valid)
    rr = np.array(ratios_re)
    ri = np.array(ratios_im)

    print(f"  Re ratio omega_1/omega_0: range [{rr.min():.4f}, {rr.max():.4f}]")
    print(f"  Im ratio omega_1/omega_0: range [{ri.min():.4f}, {ri.max():.4f}]")

    # Polynomial fits
    coef_re = np.polyfit(xv, rr, 3)
    coef_im = np.polyfit(xv, ri, 2)
    rms_re = np.sqrt(np.mean((rr - np.polyval(coef_re, xv))**2))
    rms_im = np.sqrt(np.mean((ri - np.polyval(coef_im, xv))**2))
    print(f"  Re ratio cubic fit RMS: {rms_re:.6f}")
    print(f"  Im ratio quadratic fit RMS: {rms_im:.6f}")

    # Key WKB prediction: Im ratio = omega_1.im / omega_0.im ~ 3/1 = 3 at leading order
    # (since Im(omega_n) ~ -(n+1/2) at leading WKB)
    # So im_ratio should be ~3 for n=0,1 pair
    print(f"  Im ratio mean: {ri.mean():.4f}  (WKB leading order predicts ~3.0)")

    return {
        'x': xv.tolist(), 'ratio_re': rr.tolist(), 'ratio_im': ri.tolist(),
        'rms_re': float(rms_re), 'rms_im': float(rms_im),
        'im_ratio_mean': float(ri.mean()), 'im_ratio_std': float(ri.std()),
        're_ratio_mean': float(rr.mean()), 're_ratio_std': float(rr.std()),
    }


def test_eisenstein_norm_frequency():
    """
    Compute the Eisenstein quadratic form of the QNM frequency vector.

    The Eisenstein norm of (a, b) is a^2 + a*b + b^2.
    For the frequency: |omega_re^2 + omega_re*omega_im + omega_im^2| / Lambda.

    Does this quantity have simple dependence on x?
    Compare to the entropy Eisenstein norm: S_b^2 + S_b*S_c + S_c^2 = ...
    From the identity: S_b + S_c + sqrt(S_b*S_c) = S_Λ,
    so S_b*S_c = Delta^2 and S_b^2 + S_b*S_c + S_c^2 = (S_b+S_c)^2 - S_b*S_c.
    """
    print("\n=== TEST 3: Eisenstein Norm of QNM Frequency ===")
    x_values = np.linspace(0.05, 0.95, 500)
    lam = 1.0
    l = 2

    eisen_norms = []
    x_valid = []
    entropy_eisen = []

    for x in x_values:
        state = sds_from_x(x, lam)
        if state is None:
            continue
        res = wkb_3rd_order(state, l=l, n=0)
        if res.omega == 0:
            continue

        a = res.omega.real / np.sqrt(lam)
        b = res.omega.imag / np.sqrt(lam)
        EN = a**2 + a*b + b**2
        eisen_norms.append(EN)
        x_valid.append(x)

        # Entropy Eisenstein: S_b/S_Λ = x^2/(x^2+x+1), S_c/S_Λ = 1/(x^2+x+1)
        denom = x**2 + x + 1
        sb_norm = x**2 / denom
        sc_norm = 1.0 / denom
        entropy_eisen.append(sb_norm**2 + sb_norm*sc_norm + sc_norm**2)

    xv = np.array(x_valid)
    EN = np.array(eisen_norms)
    EE = np.array(entropy_eisen)

    print(f"  QNM Eisenstein norm (omega^2+omega_re*omega_im+omega_im^2)/Lambda:")
    print(f"  Range: [{EN.min():.5f}, {EN.max():.5f}]")
    print(f"  Is it constant? Std/Mean: {EN.std()/abs(EN.mean()):.4f}")

    # Check correlation with entropy Eisenstein norm
    corr = np.corrcoef(EN, EE)[0,1]
    print(f"  Correlation with entropy Eisenstein norm: {corr:.6f}")

    # Check correlation with omega_re^2 + omega_im^2 (ordinary norm-squared)
    l2_norms = np.array([wkb_3rd_order(sds_from_x(x, lam), l=l, n=0).omega.real**2 +
                         wkb_3rd_order(sds_from_x(x, lam), l=l, n=0).omega.imag**2
                         for x in xv]) / lam
    corr_l2 = np.corrcoef(EN, l2_norms)[0,1]
    print(f"  Correlation of Eisenstein norm with L2 norm-squared: {corr_l2:.6f}")

    return {
        'x': xv.tolist(),
        'eisenstein_norm_qnm': EN.tolist(),
        'eisenstein_norm_entropy': EE.tolist(),
        'corr_entropy': float(corr),
        'corr_l2': float(corr_l2),
        'EN_range': [float(EN.min()), float(EN.max())],
        'EN_std_over_mean': float(EN.std()/abs(EN.mean())),
    }


def test_spectral_combination_vs_thermodynamics():
    """
    Are there combinations of QNM frequencies that directly encode
    thermodynamic quantities (T_b, T_c, Delta, eta_C)?

    Tests:
    - omega_re * r_b vs T_b * r_b (dimensionless temperature)
    - omega_re / (T_b + T_c) -- does this simplify?
    - Q vs eta_C regression (from EXP02, extended here with l-dependence)
    - omega_im * r_c vs T_c * r_c
    """
    print("\n=== TEST 4: QNM vs Thermodynamic Quantities ===")
    x_values = np.linspace(0.05, 0.93, 400)
    lam = 1.0

    data = {key: [] for key in [
        'x', 'T_b_norm', 'T_c_norm', 'eta_C',
        'omega_re_l2', 'omega_im_l2', 'omega_re_l3',
        'Q_l2', 'Q_l3',
        'omega_re_l2_over_Tb', 'omega_im_l2_over_Tc',
    ]}

    for x in x_values:
        state = sds_from_x(x, lam)
        if state is None:
            continue
        res2 = wkb_3rd_order(state, l=2, n=0)
        res3 = wkb_3rd_order(state, l=3, n=0)
        if res2.omega == 0 or res3.omega == 0:
            continue

        rl = np.sqrt(lam)
        data['x'].append(x)
        data['T_b_norm'].append(state.T_b / rl)
        data['T_c_norm'].append(state.T_c / rl)
        data['eta_C'].append(state.eta_C)
        data['omega_re_l2'].append(res2.omega.real / rl)
        data['omega_im_l2'].append(res2.omega.imag / rl)
        data['omega_re_l3'].append(res3.omega.real / rl)
        data['Q_l2'].append(abs(res2.omega.real / res2.omega.imag))
        data['Q_l3'].append(abs(res3.omega.real / res3.omega.imag))
        data['omega_re_l2_over_Tb'].append(res2.omega.real / max(state.T_b, 1e-15))
        data['omega_im_l2_over_Tc'].append(res2.omega.imag / max(state.T_c, 1e-15))

    for key in data:
        data[key] = np.array(data[key])

    # Correlations
    pairs = [
        ('Q_l2', 'eta_C', 'Quality factor Q vs Carnot efficiency'),
        ('omega_re_l2', 'T_b_norm', 'Re(omega_l2)/sqrt(L) vs T_b/sqrt(L)'),
        ('omega_im_l2', 'T_c_norm', '|Im(omega_l2)/sqrt(L)| vs T_c/sqrt(L)'),
    ]

    for k1, k2, desc in pairs:
        v1, v2 = data[k1], data[k2]
        corr = np.corrcoef(v1, np.abs(v2))[0, 1]
        print(f"  Corr({k1}, {k2}): {corr:.6f}  [{desc}]")
        # Linear regression
        c = np.polyfit(np.abs(v2), v1, 1)
        fit = np.polyval(c, np.abs(v2))
        rms = np.sqrt(np.mean((v1 - fit)**2))
        print(f"    Linear fit: {k1} = {c[0]:.4f}*|{k2}| + {c[1]:.4f}  RMS={rms:.5f}")

    # Serialize
    result = {k: v.tolist() for k, v in data.items()}
    return result


def plot_eisenstein_analysis(symmetry_res, overtone_res, eisen_res, save=True):
    """Figures for Eisenstein structure tests."""
    fig, axes = plt.subplots(2, 2, figsize=(12, 9))

    # Top-left: Overtone ratio omega_1/omega_0
    ax = axes[0, 0]
    xv = np.array(overtone_res['x'])
    ri = np.array(overtone_res['ratio_im'])
    rr = np.array(overtone_res['ratio_re'])
    ax.plot(xv, ri, 'b-', lw=1.5, label='Im ratio ω₁/ω₀')
    ax.axhline(y=3.0, color='r', linestyle='--', lw=1, label='WKB leading order = 3')
    ax.set_xlabel('x = r_b / r_c')
    ax.set_ylabel('Im(ω₁) / Im(ω₀)')
    ax.set_title('Overtone Im-ratio (l=2)')
    ax.legend(fontsize=9)
    ax.grid(True, alpha=0.3)

    ax2 = ax.twinx()
    ax2.plot(xv, rr, 'g-', lw=1.5, label='Re ratio', alpha=0.7)
    ax2.set_ylabel('Re(ω₁)/Re(ω₀)', color='g')
    ax2.axhline(y=1.0, color='orange', linestyle=':', lw=1, label='=1 (same Re)')
    ax2.legend(fontsize=9, loc='lower right')

    # Top-right: Eisenstein norm of QNM frequency
    ax = axes[0, 1]
    xv2 = np.array(eisen_res['x'])
    EN = np.array(eisen_res['eisenstein_norm_qnm'])
    EE = np.array(eisen_res['eisenstein_norm_entropy'])
    ax.plot(xv2, EN, 'b-', lw=1.5, label='QNM: ωᵣ²+ωᵣωᵢ+ωᵢ² (×1/Λ)')
    ax.set_xlabel('x = r_b / r_c')
    ax.set_ylabel('Eisenstein norm')
    ax.set_title(f'QNM Eisenstein Norm (l=2, n=0)\nCorr w/ entropy Eisenstein: {eisen_res["corr_entropy"]:.4f}')
    ax.grid(True, alpha=0.3)
    ax_r = ax.twinx()
    ax_r.plot(xv2, EE, 'r--', lw=1.5, label='Entropy Eisenstein', alpha=0.7)
    ax_r.set_ylabel('Entropy EN', color='r')
    ax.legend(fontsize=9, loc='upper left')
    ax_r.legend(fontsize=9, loc='upper right')

    # Bottom-left: x -> 1-x symmetry
    ax = axes[1, 0]
    sym_l2 = [(r['x'], r['ratio_re']) for r in symmetry_res if r['l'] == 2 and r['n'] == 0]
    if sym_l2:
        xs, rs = zip(*sym_l2)
        ax.plot(xs, rs, 'b.', ms=4, label='l=2, n=0 Re ratio')
    ax.axhline(y=1.0, color='r', linestyle='--', lw=1, label='=1 (exact symmetry)')
    ax.set_xlabel('x')
    ax.set_ylabel('ω(x).re / ω(1-x).re')
    ax.set_title('x → 1−x Symmetry Test (l=2)')
    ax.legend(fontsize=9)
    ax.grid(True, alpha=0.3)

    # Bottom-right: Q vs eta_C scatter
    ax = axes[1, 1]
    lam = 1.0
    x_fine = np.linspace(0.05, 0.93, 300)
    Q_vals, eta_vals = [], []
    for x in x_fine:
        st = sds_from_x(x, lam)
        if st is None: continue
        r2 = wkb_3rd_order(st, l=2, n=0)
        r3 = wkb_3rd_order(st, l=3, n=0)
        if r2.converged:
            Q_vals.append(abs(r2.omega.real / r2.omega.imag))
            eta_vals.append(st.eta_C)
    ax.plot(eta_vals, Q_vals, 'b.', ms=2, alpha=0.5, label='l=2, n=0')
    ax.set_xlabel('Carnot efficiency η_C')
    ax.set_ylabel('Q = |Re(ω)/Im(ω)|')
    ax.set_title('Quality Factor vs Carnot Efficiency')
    ax.grid(True, alpha=0.3)
    ax.legend(fontsize=9)

    plt.suptitle('Eisenstein Structure in SdS QNM Spectrum', fontsize=13, fontweight='bold')
    plt.tight_layout()
    if save:
        path = os.path.join(FIGURES_DIR, 'exp03_eisenstein_spectral.png')
        plt.savefig(path, dpi=150, bbox_inches='tight')
        print(f"  Figure saved: {path}")
    plt.close()


def run():
    print("=" * 60)
    print("EXP03: Eisenstein Structure in QNM Spectrum")
    print("=" * 60)

    r1 = test_nariai_symmetry()
    r2 = test_overtone_ratio()
    r3 = test_eisenstein_norm_frequency()
    r4 = test_spectral_combination_vs_thermodynamics()
    plot_eisenstein_analysis(r1, r2, r3)

    results = {
        'nariai_symmetry_max_deviation': float(max(abs(r['ratio_re'] - 1) for r in r1
                                                   if r['l'] == 2 and r['n'] == 0) if r1 else 0),
        'overtone_ratio': {k: v for k, v in r2.items() if not isinstance(v, list)},
        'eisenstein_norm': {k: v for k, v in r3.items() if not isinstance(v, list)},
    }

    path = os.path.join(RESULTS_DIR, 'exp03_eisenstein_spectral.json')
    with open(path, 'w') as f:
        json.dump(results, f, indent=2, cls=NumpyEncoder)
    print(f"Results saved: {path}")
    print("EXP03 DONE.")
    return results


if __name__ == '__main__':
    run()
