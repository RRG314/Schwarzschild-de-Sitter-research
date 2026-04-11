"""
EXP02: Lambda-Scaling Law for SdS QNM Frequencies

Primary question:
  Does omega / sqrt(Lambda) depend only on x = r_b/r_c (and l, n),
  and not on Lambda separately?

Theoretical prediction (dimensional argument):
  Under r -> lambda*r with Lambda -> Lambda/lambda^2 and M -> lambda*M,
  the SdS metric is invariant (x unchanged). The potential scales as
  V -> V/lambda^2, so omega^2 -> omega^2/lambda^2, i.e., omega -> omega/lambda.
  Since r_c = sqrt(3/Lambda) / sqrt(x^2+x+1), we have r_c ~ Lambda^{-1/2}.
  Fixing x and varying Lambda: r_c ~ Lambda^{-1/2}, so lambda = Lambda^{-1/2},
  and omega ~ Lambda^{1/2}.

  Therefore: omega / sqrt(Lambda) should be a function of x, l, n only.

Tests:
  1. Fix x at multiple values, vary Lambda over 3 orders of magnitude.
     Verify omega/sqrt(Lambda) is constant to < 1% across Lambda.
  2. Map omega_re/sqrt(Lambda) and omega_im/sqrt(Lambda) vs x.
  3. Test whether these Eisenstein-arc functions have any algebraic simplicity.
  4. Quality factor Q = Re(omega)/|Im(omega)| should be Lambda-independent.
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


def test_lambda_scaling():
    """
    For each x in x_probe, vary Lambda over a large range.
    Check that omega/sqrt(Lambda) is constant.
    """
    print("\n=== TEST 1: Lambda Scaling ===")
    x_probe = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
    lam_values = np.array([0.01, 0.05, 0.1, 0.3, 0.5, 1.0, 2.0, 5.0, 10.0])
    l, n = 2, 0

    all_results = []
    print(f"  l={l}, n={n}: testing {len(x_probe)} x values over {len(lam_values)} Lambda values")

    for x in x_probe:
        row = {'x': x, 'lam_values': lam_values.tolist(), 'omega_re_norm': [], 'omega_im_norm': []}
        for lam in lam_values:
            state = sds_from_x(x, lam)
            if state is None:
                row['omega_re_norm'].append(None)
                row['omega_im_norm'].append(None)
                continue
            res = wkb_3rd_order(state, l=l, n=n)
            row['omega_re_norm'].append(res.omega.real / np.sqrt(lam))
            row['omega_im_norm'].append(res.omega.imag / np.sqrt(lam))

        # Check constancy
        vals_re = [v for v in row['omega_re_norm'] if v is not None]
        vals_im = [v for v in row['omega_im_norm'] if v is not None]
        std_re = np.std(vals_re) / np.mean(np.abs(vals_re))
        std_im = np.std(vals_im) / np.mean(np.abs(vals_im))
        row['std_re_frac'] = std_re
        row['std_im_frac'] = std_im
        print(f"  x={x:.2f}: omega_re/sqrt(L) = {np.mean(vals_re):.5f} +/- {std_re:.2e}  "
              f"omega_im/sqrt(L) = {np.mean(vals_im):.5f} +/- {std_im:.2e}")
        all_results.append(row)

    max_std = max(r['std_re_frac'] for r in all_results)
    print(f"\n  Max fractional std of omega_re/sqrt(Lambda) across Lambda: {max_std:.2e}")
    if max_std < 1e-4:
        print("  VERDICT: SCALING LAW HOLDS to < 0.01%. Lambda cancels exactly.")
    elif max_std < 1e-2:
        print("  VERDICT: SCALING LAW HOLDS to < 1%. Minor WKB numerical variation.")
    else:
        print("  VERDICT: SCALING LAW DOES NOT HOLD cleanly.")
    return all_results


def map_dimensionless_qnm_vs_x():
    """
    At Lambda=1, map omega_re/sqrt(Lambda) and omega_im/sqrt(Lambda) vs x
    for several (l, n) pairs. These are the universal spectral functions F_l^n(x).
    """
    print("\n=== TEST 2: Dimensionless QNM Functions F(x) ===")
    x_values = np.linspace(0.04, 0.96, 200)
    lam = 1.0
    ln_pairs = [(2, 0), (3, 0), (4, 0), (2, 1), (3, 1)]

    results = {}
    for (l, n) in ln_pairs:
        re_vals, im_vals, Q_vals = [], [], []
        for x in x_values:
            state = sds_from_x(x, lam)
            if state is None:
                re_vals.append(np.nan); im_vals.append(np.nan); Q_vals.append(np.nan)
                continue
            res = wkb_3rd_order(state, l=l, n=n)
            if not res.converged:
                re_vals.append(np.nan); im_vals.append(np.nan); Q_vals.append(np.nan)
                continue
            re_vals.append(res.omega.real / np.sqrt(lam))
            im_vals.append(res.omega.imag / np.sqrt(lam))
            Q = abs(res.omega.real / res.omega.imag) if res.omega.imag != 0 else np.nan
            Q_vals.append(Q)

        key = f'l{l}_n{n}'
        results[key] = {
            'x': x_values.tolist(),
            'F_re': re_vals,
            'F_im': im_vals,
            'Q': Q_vals,
        }
        valid = [(x, re, im) for x, re, im in zip(x_values, re_vals, im_vals)
                 if not (np.isnan(re) or np.isnan(im))]
        if valid:
            x0, re0, im0 = valid[len(valid)//2]
            print(f"  l={l}, n={n}: at x=0.5, F_re={re0:.4f}, F_im={im0:.4f}, "
                  f"Q={abs(re0/im0):.3f}")
    return results


def test_quality_factor_universality():
    """
    Test whether Q = Re(omega)/|Im(omega)| is Lambda-independent.
    This should follow from the scaling law.
    """
    print("\n=== TEST 3: Quality Factor Universality ===")
    x_test = 0.5
    lam_values = np.logspace(-2, 1, 20)
    l, n = 2, 0

    Q_values = []
    for lam in lam_values:
        state = sds_from_x(x_test, lam)
        if state is None:
            continue
        res = wkb_3rd_order(state, l=l, n=n)
        Q = abs(res.omega.real / res.omega.imag)
        Q_values.append(Q)

    Q_arr = np.array(Q_values)
    print(f"  x={x_test}, l={l}, n={n}:")
    print(f"  Q = {np.mean(Q_arr):.6f} +/- {np.std(Q_arr):.2e}  "
          f"(fractional variation: {np.std(Q_arr)/np.mean(Q_arr):.2e})")
    print("  Q should be Lambda-independent (depends only on x, l, n).")
    return {'x': x_test, 'Q_mean': float(np.mean(Q_arr)), 'Q_std': float(np.std(Q_arr)),
            'Q_frac_var': float(np.std(Q_arr)/np.mean(Q_arr))}


def probe_algebraic_structure():
    """
    Examine whether F_re(x) = omega_re(x, Lambda=1) / sqrt(Lambda)
    and F_im(x) have algebraic simplicity in terms of x.

    Tests:
    - F_re vs sqrt(l*(l+1)) (WKB leading order ~ sqrt(l(l+1))/r_max)
    - F_re * r_max vs simple functions of x
    - Q(x) vs simple functions of x
    - Check if Q(x) is monotone, has a zero, etc.
    """
    print("\n=== TEST 4: Algebraic Structure Probe ===")
    x_values = np.linspace(0.05, 0.95, 500)
    lam = 1.0
    l, n = 2, 0

    omega_re_norm = []
    omega_im_norm = []
    r_max_norm = []  # r_max / r_c (should be Lambda-independent)
    Q_vals = []
    V0_norm = []     # V_max / Lambda

    for x in x_values:
        state = sds_from_x(x, lam)
        if state is None:
            omega_re_norm.append(np.nan); omega_im_norm.append(np.nan)
            r_max_norm.append(np.nan); Q_vals.append(np.nan); V0_norm.append(np.nan)
            continue
        res = wkb_3rd_order(state, l=l, n=n)
        omega_re_norm.append(res.omega.real / np.sqrt(lam))
        omega_im_norm.append(res.omega.imag / np.sqrt(lam))
        r_max_norm.append(res.r_max / state.r_c)
        V0_norm.append(res.V0 / lam)
        Q = abs(res.omega.real / res.omega.imag) if res.omega.imag != 0 else np.nan
        Q_vals.append(Q)

    # Convert to arrays
    x_a = np.array(x_values)
    re_a = np.array(omega_re_norm)
    im_a = np.array(omega_im_norm)
    Q_a = np.array(Q_vals)
    r_max_a = np.array(r_max_norm)
    V0_a = np.array(V0_norm)
    mask = ~(np.isnan(re_a) | np.isnan(im_a))

    # Leading-order WKB: omega_re ~ sqrt(V0) ~ sqrt(l(l+1)) / r_max
    # Check: omega_re * r_max / sqrt(l(l+1)) should be ~ 1 at leading order
    lead_check = re_a[mask] * r_max_a[mask] / np.sqrt(l*(l+1))
    print(f"  omega_re * r_max / sqrt(l(l+1)): mean={np.nanmean(lead_check):.4f}, "
          f"std={np.nanstd(lead_check):.4f}")
    print(f"  (Should be ~1 at leading WKB; deviations = f(r) correction terms)")

    # Check if Q is monotone in x
    Q_valid = Q_a[mask]
    x_valid = x_a[mask]
    is_monotone = bool(np.all(np.diff(Q_valid) > 0) or np.all(np.diff(Q_valid) < 0))
    print(f"  Q(x) range: [{Q_valid.min():.4f}, {Q_valid.max():.4f}]  Monotone: {is_monotone}")

    # Try to fit Q vs simple functions: Q ~ a + b*x^2, Q ~ a + b*(1-x)^{-1}, etc.
    from numpy.polynomial import polynomial as P
    # Polynomial fit to Q vs x
    coefs = np.polyfit(x_valid, Q_valid, 3)
    Q_fit = np.polyval(coefs, x_valid)
    rms_poly = np.sqrt(np.mean((Q_valid - Q_fit)**2))
    print(f"  Q(x) cubic polynomial fit RMS: {rms_poly:.5f}")

    # Fit Q vs (1-x^2)/(1+2x) = eta_C (Carnot efficiency)
    from src.sds_physics import sds_from_x as sfx
    eta_vals = np.array([sfx(x, 1.0).eta_C for x in x_valid])
    coefs_eta = np.polyfit(eta_vals, Q_valid, 2)
    Q_fit_eta = np.polyval(coefs_eta, eta_vals)
    rms_eta = np.sqrt(np.mean((Q_valid - Q_fit_eta)**2))
    print(f"  Q(x) quadratic fit in eta_C(x): RMS = {rms_eta:.5f}")
    print(f"    Interpretation: if RMS small, Q correlates with Carnot efficiency.")

    return {
        'x': x_a[mask].tolist(),
        'omega_re_norm': re_a[mask].tolist(),
        'omega_im_norm': im_a[mask].tolist(),
        'Q': Q_valid.tolist(),
        'r_max_norm': r_max_a[mask].tolist(),
        'V0_norm': V0_a[mask].tolist(),
        'lead_check_mean': float(np.nanmean(lead_check)),
        'Q_monotone': is_monotone,
        'Q_range': [float(Q_valid.min()), float(Q_valid.max())],
        'rms_poly_cubic': float(rms_poly),
        'rms_eta_quadratic': float(rms_eta),
    }


def plot_dimensionless_qnm(scaling_results, fn_results, save=True):
    """Generate figures for the scaling results."""
    fig, axes = plt.subplots(2, 2, figsize=(12, 9))

    # Top-left: omega_re/sqrt(Lambda) vs Lambda for several x values
    ax = axes[0, 0]
    lam_arr = np.logspace(-2, 1, 20)
    x_probe = [0.1, 0.3, 0.5, 0.7, 0.9]
    colors = plt.cm.viridis(np.linspace(0.1, 0.9, len(x_probe)))
    from src.wkb_qnm import wkb_3rd_order as w3

    for i, x in enumerate(x_probe):
        norm_vals = []
        for lam in lam_arr:
            st = sds_from_x(x, lam)
            if st is None:
                norm_vals.append(np.nan)
                continue
            res = w3(st, l=2, n=0)
            norm_vals.append(res.omega.real / np.sqrt(lam))
        ax.semilogx(lam_arr, norm_vals, '-', color=colors[i], lw=1.5, label=f'x={x:.1f}')

    ax.set_xlabel('Λ')
    ax.set_ylabel('Re(ω) / √Λ')
    ax.set_title('Lambda-Scaling: Re(ω)/√Λ vs Λ (l=2, n=0)')
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)

    # Top-right: F_re(x) and F_im(x) for several (l,n)
    ax = axes[0, 1]
    ln_colors = {'l2_n0': 'blue', 'l3_n0': 'red', 'l4_n0': 'green',
                 'l2_n1': 'orange', 'l3_n1': 'purple'}
    for key, data in fn_results.items():
        xv = np.array(data['x'])
        rv = np.array(data['F_re'])
        mask = ~np.isnan(rv)
        ax.plot(xv[mask], rv[mask], '-', color=ln_colors.get(key, 'gray'),
                lw=1.5, label=key.replace('l', 'l=').replace('_n', ', n='))
    ax.set_xlabel('x = r_b / r_c')
    ax.set_ylabel('Re(ω) / √Λ')
    ax.set_title('Dimensionless QNM Frequency F_re(x)')
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)

    # Bottom-left: Quality factor Q(x)
    ax = axes[1, 0]
    for key, data in fn_results.items():
        xv = np.array(data['x'])
        Qv = np.array(data['Q'])
        mask = ~np.isnan(Qv)
        ax.plot(xv[mask], Qv[mask], '-', color=ln_colors.get(key, 'gray'),
                lw=1.5, label=key.replace('l', 'l=').replace('_n', ', n='))
    ax.set_xlabel('x = r_b / r_c')
    ax.set_ylabel('Q = |Re(ω)/Im(ω)|')
    ax.set_title('Quality Factor Q(x) - Lambda-Independent')
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)

    # Bottom-right: Q(x) vs eta_C(x) — scatter plot
    ax = axes[1, 1]
    x_fine = np.linspace(0.05, 0.95, 300)
    lam = 1.0
    Q_fine, eta_fine = [], []
    for x in x_fine:
        st = sds_from_x(x, lam)
        if st is None:
            continue
        res = w3(st, l=2, n=0)
        if res.converged and res.omega.imag != 0:
            Q_fine.append(abs(res.omega.real / res.omega.imag))
            eta_fine.append(st.eta_C)
    ax.plot(eta_fine, Q_fine, 'b.', ms=2, alpha=0.6)
    ax.set_xlabel('Carnot efficiency η_C = (T_b − T_c)/T_b')
    ax.set_ylabel('Q = |Re(ω)/Im(ω)|')
    ax.set_title('Quality Factor vs Carnot Efficiency (l=2, n=0)')
    ax.grid(True, alpha=0.3)

    plt.suptitle('SdS QNM Λ-Scaling Analysis', fontsize=13, fontweight='bold')
    plt.tight_layout()
    if save:
        path = os.path.join(FIGURES_DIR, 'exp02_lambda_scaling.png')
        plt.savefig(path, dpi=150, bbox_inches='tight')
        print(f"  Figure saved: {path}")
    plt.close()


def run():
    print("=" * 60)
    print("EXP02: Lambda-Scaling Law")
    print("=" * 60)

    r1 = test_lambda_scaling()
    r2 = map_dimensionless_qnm_vs_x()
    r3 = test_quality_factor_universality()
    r4 = probe_algebraic_structure()
    plot_dimensionless_qnm(r1, r2)

    # Serialize (drop x arrays from r1 to keep compact)
    r1_compact = [{'x': r['x'], 'std_re_frac': r['std_re_frac'],
                   'mean_re': float(np.mean([v for v in r['omega_re_norm'] if v is not None]))}
                  for r in r1]

    results = {
        'scaling_test': r1_compact,
        'quality_factor': r3,
        'algebraic_probe': {k: v for k, v in r4.items() if not isinstance(v, list)},
    }

    # Also save the full x-dependent functions for plotting
    full_path = os.path.join(RESULTS_DIR, 'exp02_fn_curves.json')
    with open(full_path, 'w') as f:
        json.dump(r2, f, cls=NumpyEncoder)
    print(f"  Full F(x) curves saved: {full_path}")

    path = os.path.join(RESULTS_DIR, 'exp02_lambda_scaling.json')
    with open(path, 'w') as f:
        json.dump(results, f, indent=2, cls=NumpyEncoder)
    print(f"Results saved: {path}")
    print("EXP02 DONE.")
    return results


if __name__ == '__main__':
    run()
