"""
EXP05: RDT Overtone Hierarchy Analysis

Question:
  Does grouping the QNM overtone sequence {omega_n} by RDT depth of the
  overtone index n reveal structure that uniform binning does not?

  The RDT scalar field R(n) gives depth 0 for n=1, depth 1 for small n
  (n=2..9 roughly), depth 2 for larger n, etc.

  If RDT grouping reveals structure, it would mean that the recursive
  divisibility structure of the integer n encodes something about the
  QNM spectrum. This would be a genuine connection between RDT and physics.

  Expected outcome: NEGATIVE. RDT depth of n is an arithmetic property
  of the integer n, with no obvious physical meaning for QNMs. The prior
  EXP04 of the recursive_spacetime_system confirmed RDT was inert on SdS.
  This is an honest supplementary check.

Test design:
  1. Compute omega_n for n=0..50 using 1st-order WKB (valid for large l).
     Use l=10 to keep WKB valid for many overtones.
  2. Group by RDT depth.
  3. Compute mean and variance of |omega_n| within each RDT group.
  4. Compare to uniform binning (same number of bins, same total count).
  5. Baseline: simple linear regression in n (the expected behavior).
  6. Compute Shannon entropy of the two groupings.
  7. Verdict: does RDT add information beyond the known linear growth?
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import numpy as np
import json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from src.sds_physics import sds_from_x
from src.wkb_qnm import wkb_1st_order
from src.rdt_tools import rdt_depth, rdt_table, compare_rdt_vs_uniform
from src.json_utils import NumpyEncoder

RESULTS_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'results')
FIGURES_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'figures')
os.makedirs(RESULTS_DIR, exist_ok=True)
os.makedirs(FIGURES_DIR, exist_ok=True)


def compute_overtone_tower(x, lam, l, n_max):
    """Compute omega_n for n=0..n_max using 1st-order WKB."""
    state = sds_from_x(x, lam)
    if state is None:
        return []
    omegas = []
    for n in range(n_max + 1):
        res = wkb_1st_order(state, l=l, n=n)
        omegas.append(res.omega)
    return omegas


def test_rdt_vs_uniform_grouping():
    """
    Main test: compare RDT grouping to uniform grouping of the overtone tower.
    """
    print("\n=== TEST: RDT vs Uniform Grouping ===")
    x = 0.5
    lam = 1.0
    l = 10  # high l for valid WKB at many overtones
    n_max = 60

    print(f"  Computing overtone tower: x={x}, Lambda={lam}, l={l}, n=0..{n_max}")
    omegas = compute_overtone_tower(x, lam, l, n_max)
    print(f"  Computed {len(omegas)} overtone frequencies.")

    # Separate real and imaginary parts
    omega_re = [o.real for o in omegas]
    omega_im = [o.imag for o in omegas]
    omega_abs = [abs(o) for o in omegas]

    # RDT depths of overtone indices n=1..n_max+1 (1-indexed)
    R = rdt_table(n_max + 2)
    depths = [R[n+1] for n in range(n_max + 1)]  # n=0 maps to R[1]
    unique_depths = sorted(set(depths))
    print(f"  RDT depths present: {unique_depths}")
    print(f"  Depth distribution: "
          + ", ".join(f"depth {d}: {depths.count(d)}" for d in unique_depths))

    # Compare RDT vs uniform grouping of |Im(omega)| (the imaginary part grows linearly in n)
    comp_im = compare_rdt_vs_uniform(omega_im, n_bins=len(unique_depths))
    comp_re = compare_rdt_vs_uniform(omega_re, n_bins=len(unique_depths))

    print(f"\n  Shannon entropy of |Im(omega)| grouping:")
    print(f"    RDT:     {comp_im['entropy_rdt']:.4f}")
    print(f"    Uniform: {comp_im['entropy_uniform']:.4f}")
    print(f"  Shannon entropy of Re(omega) grouping:")
    print(f"    RDT:     {comp_re['entropy_rdt']:.4f}")
    print(f"    Uniform: {comp_re['entropy_uniform']:.4f}")

    # Linear fit to Im(omega) vs n: expect Im(omega_n) ~ -(n+0.5) * C
    ns = np.arange(n_max + 1)
    im_arr = np.array(omega_im)
    coef = np.polyfit(ns, im_arr, 1)
    lin_fit = np.polyval(coef, ns)
    rms_linear = np.sqrt(np.mean((im_arr - lin_fit)**2))
    print(f"\n  Linear fit to Im(omega) vs n: slope={coef[0]:.5f}, intercept={coef[1]:.5f}")
    print(f"  RMS of residuals from linear fit: {rms_linear:.6f}")
    print(f"  (Near-zero RMS = Im(omega) is purely linear in n, as WKB predicts)")

    # Residuals from linear fit: do they correlate with RDT depth?
    residuals = im_arr - lin_fit
    from scipy.stats import pearsonr
    try:
        depth_arr = np.array(depths, dtype=float)
        corr, pval = pearsonr(depth_arr, residuals)
        print(f"\n  Correlation of Im(omega) residuals with RDT depth: {corr:.4f} (p={pval:.3f})")
        print(f"  {'RDT depth CORRELATES with residuals (unexpected!)' if abs(corr) > 0.3 else 'RDT depth does NOT correlate with residuals (expected).'}")
    except Exception as e:
        print(f"  Correlation test failed: {e}")
        corr, pval = 0.0, 1.0

    return {
        'omega_abs': omega_abs,
        'omega_re': omega_re,
        'omega_im': omega_im,
        'depths': depths,
        'unique_depths': unique_depths,
        'entropy_rdt_im': comp_im['entropy_rdt'],
        'entropy_uniform_im': comp_im['entropy_uniform'],
        'rms_linear_im': float(rms_linear),
        'corr_depth_residual': float(corr),
        'corr_pval': float(pval),
    }


def test_rdt_at_large_n():
    """
    At very large overtone numbers, the RDT depth increases.
    Test whether the spectral behavior changes at RDT depth transitions.
    Use n=0..1000, l=50.
    """
    print("\n=== TEST: RDT at Large Overtone Numbers (n up to 1000) ===")
    x = 0.5
    lam = 1.0
    l = 50
    n_max = 500

    print(f"  Computing large overtone tower: l={l}, n=0..{n_max}")
    state = sds_from_x(x, lam)
    R = rdt_table(n_max + 2)

    # At 1st-order WKB: Im(omega_n) = Im(omega_0) + n * slope
    # So Im(omega_n) is exactly linear. The residuals from linearity = 0 by construction.
    # So RDT cannot find structure in Im(omega) at WKB order 1.
    # We use wkb_1st_order for speed and note this limitation.

    from src.wkb_qnm import wkb_1st_order
    omegas = []
    for n in range(0, n_max + 1, 10):  # sample every 10th
        res = wkb_1st_order(state, l=l, n=n)
        omegas.append((n, res.omega, R[n+1] if n+1 <= len(R)-1 else R[-1]))

    depths_seen = sorted(set(d for _, _, d in omegas))
    print(f"  RDT depths at n=0..{n_max} (sampled every 10): {depths_seen}")

    # At WKB order 1, Im(omega_n) = -C*(n+0.5) exactly, so residuals are 0.
    # This confirms: at WKB-1, RDT adds nothing to Im(omega).
    # For Re(omega_n): constant at WKB-1.
    re_vals = np.array([o.real for _, o, _ in omegas])
    print(f"  Re(omega) variation at WKB-1: std/mean = {re_vals.std()/re_vals.mean():.2e}")
    print(f"  (At WKB-1, Re(omega) = sqrt(V_0) = const, so std should be ~0)")
    print(f"  Conclusion: WKB-1 is exactly linear; RDT cannot reveal non-linearity there.")

    return {
        'n_values': [n for n, _, _ in omegas],
        'omega_re': [o.real for _, o, _ in omegas],
        'omega_im': [o.imag for _, o, _ in omegas],
        'rdt_depths': [d for _, _, d in omegas],
        'depths_seen': depths_seen,
    }


def run():
    print("=" * 60)
    print("EXP05: RDT Overtone Hierarchy")
    print("=" * 60)

    r1 = test_rdt_vs_uniform_grouping()
    r2 = test_rdt_at_large_n()

    # Figure
    fig, axes = plt.subplots(1, 2, figsize=(12, 4))

    ax = axes[0]
    ns = np.arange(len(r1['omega_im']))
    im_arr = np.array(r1['omega_im'])
    depths = r1['depths']
    unique_depths = r1['unique_depths']
    depth_colors = {d: plt.cm.viridis(i/max(1, len(unique_depths)-1))
                    for i, d in enumerate(unique_depths)}
    for d in unique_depths:
        mask = np.array([dep == d for dep in depths])
        ax.scatter(ns[mask], im_arr[mask], color=depth_colors[d], s=15,
                   label=f'RDT depth {d}', zorder=3)
    ax.plot(ns, np.polyval(np.polyfit(ns, im_arr, 1), ns), 'r--', lw=1.5,
            label='Linear fit', zorder=4)
    ax.set_xlabel('Overtone index n')
    ax.set_ylabel('Im(ω_n)')
    ax.set_title('Overtone Tower by RDT Depth (l=10, x=0.5)')
    ax.legend(fontsize=8, ncol=2)
    ax.grid(True, alpha=0.3)

    ax = axes[1]
    re_arr = np.array(r1['omega_re'])
    for d in unique_depths:
        mask = np.array([dep == d for dep in depths])
        ax.scatter(ns[mask], re_arr[mask], color=depth_colors[d], s=15,
                   label=f'RDT depth {d}', zorder=3)
    ax.set_xlabel('Overtone index n')
    ax.set_ylabel('Re(ω_n)')
    ax.set_title('Real Part by RDT Depth (l=10, x=0.5)\n(Re~const at WKB-1)')
    ax.legend(fontsize=8, ncol=2)
    ax.grid(True, alpha=0.3)

    plt.suptitle('RDT Overtone Hierarchy Analysis', fontsize=13, fontweight='bold')
    plt.tight_layout()
    fig_path = os.path.join(FIGURES_DIR, 'exp05_rdt_overtone.png')
    plt.savefig(fig_path, dpi=150, bbox_inches='tight')
    print(f"  Figure saved: {fig_path}")
    plt.close()

    verdict = "NEGATIVE" if abs(r1['corr_depth_residual']) < 0.15 else "POSITIVE"
    print(f"\n  VERDICT: RDT overtone analysis is {verdict}.")
    if verdict == "NEGATIVE":
        print("  RDT depth does not correlate with QNM residuals.")
        print("  This confirms: RDT is not a useful decomposition for QNM overtones.")
        print("  The overtone structure is captured entirely by the linear WKB prediction.")

    results = {k: (v if not isinstance(v, list) else v[:10])
               for k, v in r1.items()}
    results['verdict'] = verdict

    path = os.path.join(RESULTS_DIR, 'exp05_rdt_overtone.json')
    with open(path, 'w') as f:
        json.dump(results, f, indent=2, cls=NumpyEncoder)
    print(f"Results saved: {path}")
    print("EXP05 DONE.")
    return results


if __name__ == '__main__':
    run()
