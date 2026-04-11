"""
EXP04: Inverse Horizon Spectroscopy

Primary question:
  Given a small number of QNM frequencies (observable in principle from
  gravitational wave detections), can we recover the horizon ratio x = r_b/r_c?

  Since omega / sqrt(Lambda) = F(x, l, n), the ratio
      R_{l} = omega_{l,0} / omega_{l,1}
  is Lambda-independent (Lambda cancels). If R_l = G_l(x) is invertible,
  then x is recoverable from a single (l, n=0) + (l, n=1) measurement.

  Similarly, the cross-mode ratio
      S_{l,l'} = omega_{l,0} / omega_{l',0}
  is also Lambda-independent and encodes x.

Tests:
  1. Construct G_l(x) and test its invertibility (monotonicity, range).
  2. Build an inversion table: given R, return x estimate.
  3. Test inversion accuracy: inject known x, compute R, invert, compare.
  4. Test robustness: add WKB error (estimated ~1-5%) and see how x-recovery degrades.
  5. Compare cross-mode inversion (omega_l2 / omega_l3) to overtone inversion.
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
from scipy.interpolate import interp1d
from src.sds_physics import sds_from_x
from src.wkb_qnm import wkb_3rd_order

RESULTS_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'results')
FIGURES_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'figures')
os.makedirs(RESULTS_DIR, exist_ok=True)
os.makedirs(FIGURES_DIR, exist_ok=True)


def build_inversion_maps(lam=1.0):
    """
    Build the functions G_l(x) = Re(omega_{l,1}) / Re(omega_{l,0})
    and H_l(x) = Im(omega_{l,1}) / Im(omega_{l,0}) over x in (0, 1).
    Also build S_{l,l'}(x) = Re(omega_{l,0}) / Re(omega_{l',0}).
    Returns interpolation functions for inversion.
    """
    print("\n=== BUILD: Inversion Maps ===")
    x_vals = np.linspace(0.03, 0.97, 1000)

    maps = {}
    # Overtone ratios for l=2
    G2_re, G2_im, x_valid2 = [], [], []
    for x in x_vals:
        st = sds_from_x(x, lam)
        if st is None: continue
        r0 = wkb_3rd_order(st, l=2, n=0)
        r1 = wkb_3rd_order(st, l=2, n=1)
        # Include n=1 even when WKB-3rd correction is large (unconverged) —
        # the ratio still encodes useful x-dependence.
        if r0.omega != 0 and r1.omega != 0:
            G2_re.append(r1.omega.real / r0.omega.real)
            G2_im.append(r1.omega.imag / r0.omega.imag)
            x_valid2.append(x)

    xv2 = np.array(x_valid2)
    G2r = np.array(G2_re)
    G2i = np.array(G2_im)

    # Cross-mode ratio omega_{l=3} / omega_{l=2} (n=0 for both)
    S_re, S_im, x_valid_s = [], [], []
    for x in x_vals:
        st = sds_from_x(x, lam)
        if st is None: continue
        r2 = wkb_3rd_order(st, l=2, n=0)
        r3 = wkb_3rd_order(st, l=3, n=0)
        if r2.omega != 0 and r3.omega != 0:
            S_re.append(r3.omega.real / r2.omega.real)
            S_im.append(r3.omega.imag / r2.omega.imag)
            x_valid_s.append(x)

    xvs = np.array(x_valid_s)
    Sr = np.array(S_re)
    Si = np.array(S_im)

    # Check monotonicity
    g2r_mono = np.all(np.diff(G2r) > 0) or np.all(np.diff(G2r) < 0)
    g2i_mono = np.all(np.diff(G2i) > 0) or np.all(np.diff(G2i) < 0)
    sr_mono = np.all(np.diff(Sr) > 0) or np.all(np.diff(Sr) < 0)

    print(f"  G_l2_re (Re overtone ratio): monotone={g2r_mono}, "
          f"range=[{G2r.min():.4f}, {G2r.max():.4f}]")
    print(f"  G_l2_im (Im overtone ratio): monotone={g2i_mono}, "
          f"range=[{G2i.min():.4f}, {G2i.max():.4f}]")
    print(f"  S_32 (cross-mode Re ratio):  monotone={sr_mono}, "
          f"range=[{Sr.min():.4f}, {Sr.max():.4f}]")

    # Build interpolation inverses (x as function of ratio)
    inverses = {}
    if g2r_mono:
        inverses['G2_re'] = interp1d(G2r, xv2, kind='cubic', bounds_error=False,
                                      fill_value=(xv2[0], xv2[-1]))
    if g2i_mono:
        inverses['G2_im'] = interp1d(G2i, xv2, kind='cubic', bounds_error=False,
                                      fill_value=(xv2[0], xv2[-1]))
    if sr_mono:
        inverses['S_32'] = interp1d(Sr, xvs, kind='cubic', bounds_error=False,
                                     fill_value=(xvs[0], xvs[-1]))

    maps = {
        'x_vals_overtone': xv2.tolist(), 'G2_re': G2r.tolist(), 'G2_im': G2i.tolist(),
        'x_vals_crossmode': xvs.tolist(), 'S_32_re': Sr.tolist(), 'S_32_im': Si.tolist(),
        'G2_re_monotone': g2r_mono, 'G2_im_monotone': g2i_mono, 'S_32_monotone': sr_mono,
    }
    return maps, inverses


def test_inversion_accuracy(inverses, lam=1.0):
    """
    Test inversion accuracy: inject x_true, compute ratio, invert, compare.
    """
    print("\n=== TEST 1: Inversion Accuracy (no noise) ===")
    x_test = np.linspace(0.05, 0.93, 50)
    results = []

    for x_true in x_test:
        st = sds_from_x(x_true, lam)
        if st is None: continue

        row = {'x_true': x_true}

        # G2_re inversion
        if 'G2_re' in inverses:
            r0 = wkb_3rd_order(st, l=2, n=0)
            r1 = wkb_3rd_order(st, l=2, n=1)
            if r0.omega != 0 and r1.omega != 0:
                G2_val = r1.omega.real / r0.omega.real
                x_rec = float(inverses['G2_re'](G2_val))
                row['G2_re_ratio'] = G2_val
                row['x_rec_G2_re'] = x_rec
                row['err_G2_re'] = abs(x_rec - x_true)

        # S_32 inversion
        if 'S_32' in inverses:
            r2 = wkb_3rd_order(st, l=2, n=0)
            r3 = wkb_3rd_order(st, l=3, n=0)
            if r2.omega != 0 and r3.omega != 0:
                S_val = r3.omega.real / r2.omega.real
                x_rec2 = float(inverses['S_32'](S_val))
                row['S_32_ratio'] = S_val
                row['x_rec_S32'] = x_rec2
                row['err_S32'] = abs(x_rec2 - x_true)

        results.append(row)

    if 'err_G2_re' in results[0]:
        errs = [r['err_G2_re'] for r in results if 'err_G2_re' in r]
        print(f"  G2_re inversion: mean error = {np.mean(errs):.6f}, "
              f"max = {np.max(errs):.6f}")

    if 'err_S32' in results[0]:
        errs2 = [r['err_S32'] for r in results if 'err_S32' in r]
        print(f"  S_32 inversion:  mean error = {np.mean(errs2):.6f}, "
              f"max = {np.max(errs2):.6f}")
        print("  (Small errors = interpolation residuals from finite grid)")

    return results


def test_inversion_with_noise(inverses, lam=1.0):
    """
    Test inversion robustness with added noise (simulating WKB error or
    observational uncertainty).
    Noise levels: 0.5%, 1%, 2%, 5% (relative to |omega|).
    """
    print("\n=== TEST 2: Inversion Under Noise ===")
    x_test = np.array([0.2, 0.4, 0.6, 0.8])
    noise_levels = [0.005, 0.01, 0.02, 0.05]
    n_trials = 200

    rng = np.random.default_rng(42)
    results = []

    for x_true in x_test:
        st = sds_from_x(x_true, lam)
        if st is None or 'G2_re' not in inverses:
            continue

        r0 = wkb_3rd_order(st, l=2, n=0)
        r1 = wkb_3rd_order(st, l=2, n=1)
        if r0.omega == 0 or r1.omega == 0:
            continue

        true_G2 = r1.omega.real / r0.omega.real

        row = {'x_true': x_true, 'noise_results': {}}
        for eps in noise_levels:
            x_recs = []
            for _ in range(n_trials):
                # Add multiplicative noise to both frequencies
                noise_0 = 1.0 + eps * rng.standard_normal()
                noise_1 = 1.0 + eps * rng.standard_normal()
                G2_noisy = (r1.omega.real * noise_1) / (r0.omega.real * noise_0)
                x_rec = float(inverses['G2_re'](G2_noisy))
                x_recs.append(x_rec)

            x_arr = np.array(x_recs)
            mean_err = float(np.mean(np.abs(x_arr - x_true)))
            std_err = float(np.std(x_arr))
            row['noise_results'][f'eps_{eps}'] = {
                'mean_abs_err': mean_err, 'std': std_err,
                'bias': float(np.mean(x_arr) - x_true),
            }
            print(f"  x={x_true:.2f}, eps={eps:.1%}: mean |error| = {mean_err:.4f}, "
                  f"std = {std_err:.4f}")

        results.append(row)

    return results


def test_lambda_independence_of_inversion(inverses):
    """
    Since omega/sqrt(Lambda) is Lambda-independent, the ratio G2 should be
    Lambda-independent too. Verify this explicitly.
    """
    print("\n=== TEST 3: Lambda Independence of Inversion ===")
    x_true = 0.5
    lam_values = [0.05, 0.1, 0.5, 1.0, 2.0, 5.0, 10.0]

    G2_vals = []
    for lam in lam_values:
        st = sds_from_x(x_true, lam)
        if st is None: continue
        r0 = wkb_3rd_order(st, l=2, n=0)
        r1 = wkb_3rd_order(st, l=2, n=1)
        if r0.omega != 0 and r1.omega != 0:
            G2_vals.append(r1.omega.real / r0.omega.real)
            print(f"  Lambda={lam:.3f}: G2_re = {G2_vals[-1]:.7f}")

    G2_arr = np.array(G2_vals)
    print(f"  Std of G2 across Lambda: {G2_arr.std():.2e}  "
          f"(should be ~0 if Lambda-independent)")
    return {'x': x_true, 'lam_values': lam_values, 'G2_values': G2_arr.tolist(),
            'G2_std': float(G2_arr.std())}


def plot_inversion_results(maps, acc_results, noise_results, save=True):
    """Figures for inverse spectroscopy."""
    fig, axes = plt.subplots(2, 2, figsize=(12, 9))

    # Top-left: Inversion maps G2_re(x) and S_32(x)
    ax = axes[0, 0]
    xv = np.array(maps['x_vals_overtone'])
    G2r = np.array(maps['G2_re'])
    ax.plot(xv, G2r, 'b-', lw=2, label='G₂(x) = Re(ω₁)/Re(ω₀), l=2')
    xvs = np.array(maps['x_vals_crossmode'])
    Sr = np.array(maps['S_32_re'])
    ax.plot(xvs, Sr, 'r-', lw=2, label='S₃₂(x) = Re(ω₃)/Re(ω₂), n=0')
    ax.set_xlabel('x = r_b / r_c')
    ax.set_ylabel('Frequency ratio (Λ-independent)')
    ax.set_title('Inversion Maps: Frequency Ratio vs x')
    ax.legend(fontsize=9)
    ax.grid(True, alpha=0.3)

    # Top-right: Inversion accuracy
    ax = axes[0, 1]
    if acc_results and 'x_rec_G2_re' in acc_results[0]:
        x_true = [r['x_true'] for r in acc_results if 'x_rec_G2_re' in r]
        x_rec = [r['x_rec_G2_re'] for r in acc_results if 'x_rec_G2_re' in r]
        errs = [r['err_G2_re'] for r in acc_results if 'err_G2_re' in r]
        ax.scatter(x_true, errs, c='blue', s=20, alpha=0.7, label='G2_re error')
        ax.axhline(y=0, color='k', lw=0.5)
    ax.set_xlabel('x_true')
    ax.set_ylabel('|x_recovered − x_true|')
    ax.set_title('Inversion Accuracy (no noise)\n(small error = interpolation residual)')
    ax.set_yscale('log')
    ax.legend(fontsize=9)
    ax.grid(True, alpha=0.3)

    # Bottom-left: Noise robustness
    ax = axes[1, 0]
    if noise_results:
        for row in noise_results:
            x_t = row['x_true']
            eps_list = [0.005, 0.01, 0.02, 0.05]
            errs = [row['noise_results'][f'eps_{eps}']['mean_abs_err'] for eps in eps_list]
            ax.semilogy(np.array(eps_list)*100, errs, 'o-', ms=5,
                        label=f'x={x_t:.1f}')
    ax.set_xlabel('Frequency noise level (%)')
    ax.set_ylabel('Mean |Δx|')
    ax.set_title('Inversion Error vs Noise Level\n(G2_re method)')
    ax.legend(fontsize=9)
    ax.grid(True, alpha=0.3)

    # Bottom-right: x_true vs x_recovered scatter
    ax = axes[1, 1]
    if acc_results and 'x_rec_G2_re' in acc_results[0]:
        x_true2 = [r['x_true'] for r in acc_results if 'x_rec_G2_re' in r]
        x_rec2 = [r['x_rec_G2_re'] for r in acc_results if 'x_rec_G2_re' in r]
        ax.scatter(x_true2, x_rec2, c='blue', s=15, alpha=0.7, label='G2_re')
    if acc_results and 'x_rec_S32' in acc_results[0]:
        x_true3 = [r['x_true'] for r in acc_results if 'x_rec_S32' in r]
        x_rec3 = [r['x_rec_S32'] for r in acc_results if 'x_rec_S32' in r]
        ax.scatter(x_true3, x_rec3, c='red', s=15, alpha=0.7, marker='x', label='S_32')
    x_line = [0, 1]
    ax.plot(x_line, x_line, 'k--', lw=1, label='perfect recovery')
    ax.set_xlabel('x_true = r_b/r_c')
    ax.set_ylabel('x_recovered')
    ax.set_title('Inverse Spectroscopy: Recovery')
    ax.legend(fontsize=9)
    ax.grid(True, alpha=0.3)
    ax.set_xlim(0, 1); ax.set_ylim(0, 1)

    plt.suptitle('SdS Inverse Horizon Spectroscopy', fontsize=13, fontweight='bold')
    plt.tight_layout()
    if save:
        path = os.path.join(FIGURES_DIR, 'exp04_inverse_spectroscopy.png')
        plt.savefig(path, dpi=150, bbox_inches='tight')
        print(f"  Figure saved: {path}")
    plt.close()


def run():
    print("=" * 60)
    print("EXP04: Inverse Horizon Spectroscopy")
    print("=" * 60)

    maps, inverses = build_inversion_maps()
    r1 = test_inversion_accuracy(inverses)
    r2 = test_inversion_with_noise(inverses)
    r3 = test_lambda_independence_of_inversion(inverses)
    plot_inversion_results(maps, r1, r2)

    # Summary
    noise_summary = {}
    if r2:
        for row in r2:
            x_t = row['x_true']
            for eps_key, val in row['noise_results'].items():
                if eps_key not in noise_summary:
                    noise_summary[eps_key] = []
                noise_summary[eps_key].append(val['mean_abs_err'])
        noise_summary = {k: float(np.mean(v)) for k, v in noise_summary.items()}

    results = {
        'inversion_maps': {k: v for k, v in maps.items()
                           if not isinstance(v, list) or len(v) < 10},
        'lambda_independence': r3,
        'noise_robustness_mean_err': noise_summary,
    }

    path = os.path.join(RESULTS_DIR, 'exp04_inverse_spectroscopy.json')
    with open(path, 'w') as f:
        json.dump(results, f, indent=2, cls=NumpyEncoder)
    print(f"Results saved: {path}")
    print("EXP04 DONE.")
    return results


if __name__ == '__main__':
    run()
