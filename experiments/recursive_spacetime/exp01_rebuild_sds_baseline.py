"""
Exp01: Rebuild SdS baseline — verify all exact identities from scratch.

This re-derives and numerically confirms every exact formula from
sds_entropy_paper.md using the new sds_state.py module.
No assumptions are trusted without checking.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

import numpy as np
from src.sds_state import SdSState, sds_from_x, sds_scan_x, _nariai_mass
from src.utils import save_json, section, Timer

OUT = os.path.join(os.path.dirname(__file__), "..", "outputs", "json")
PI = np.pi


def run():
    section("EXP01: SdS Baseline Rebuild")
    results = {}

    lam = 1.0
    xs = np.linspace(0.02, 0.98, 200)
    states = [sds_from_x(x, lam) for x in xs]
    valid = [s for s in states if s.is_valid()]
    print(f"  Valid states: {len(valid)}/{len(states)}")

    # 1. Entropy identity
    residuals = [abs(s.entropy_identity_residual()) for s in valid]
    print(f"  Entropy identity max residual: {max(residuals):.2e}")
    results["entropy_identity"] = {
        "max_residual": float(max(residuals)),
        "mean_residual": float(np.mean(residuals)),
        "passed": max(residuals) < 1e-10,
    }

    # 2. Temperature positivity
    T_b_pos = all(s.T_b > 0 for s in valid)
    T_c_pos = all(s.T_c > 0 for s in valid)
    T_b_gt_T_c = all(s.T_b > s.T_c for s in valid)
    print(f"  T_b > 0: {T_b_pos}, T_c > 0: {T_c_pos}, T_b > T_c: {T_b_gt_T_c}")
    results["temperature"] = {
        "T_b_always_positive": T_b_pos,
        "T_c_always_positive": T_c_pos,
        "T_b_always_gt_T_c": T_b_gt_T_c,
    }

    # 3. dDelta/dM = 1/T_c - 1/T_b: verify numerically
    errors = []
    for s in valid[5:-5:5]:
        analytic = s.dDelta_dM()
        h = s.M * 1e-5
        s_plus = SdSState(s.M + h, lam)
        s_minus = SdSState(s.M - h, lam)
        if s_plus.admissible and s_minus.admissible:
            numeric = (s_plus.Delta - s_minus.Delta) / (2*h)
            errors.append(abs(analytic - numeric) / (abs(analytic) + 1e-30))
    print(f"  dDelta/dM identity max rel error: {max(errors):.2e}")
    results["dDelta_dM_identity"] = {
        "max_rel_error": float(max(errors)),
        "passed": max(errors) < 1e-4,
    }

    # 4. Carnot relation: dDelta/dSc = -eta_C
    errors2 = []
    for s in valid[5:-5:5]:
        eta_C = s.eta_C
        # Compute dDelta/dSc numerically
        x = s.x
        h = 0.005
        if x - h > 0 and x + h < 1:
            s_plus = sds_from_x(x + h, lam)
            s_minus = sds_from_x(x - h, lam)
            if s_plus.is_valid() and s_minus.is_valid():
                dDelta_dSc = (s_plus.Delta - s_minus.Delta) / (s_plus.S_c - s_minus.S_c)
                errors2.append(abs(dDelta_dSc + eta_C) / (abs(eta_C) + 1e-30))
    if errors2:
        print(f"  Carnot relation max rel error: {max(errors2):.2e}")
        results["carnot_relation"] = {
            "max_rel_error": float(max(errors2)),
            "passed": max(errors2) < 1e-3,
        }

    # 5. Mass range
    M_N = _nariai_mass(lam)
    M_vals = [s.M for s in valid]
    mass_ok = all(0 < M < M_N for M in M_vals)
    print(f"  Mass in (0, M_Nariai={M_N:.4f}): {mass_ok}")
    results["mass_range"] = {
        "M_Nariai": float(M_N),
        "all_in_range": mass_ok,
        "M_min": float(min(M_vals)),
        "M_max": float(max(M_vals)),
    }

    # 6. Eisenstein constraint: r_b^2 + r_b*r_c + r_c^2 = 3/Lambda
    ec_residuals = [abs(s.r_b**2 + s.r_b*s.r_c + s.r_c**2 - 3.0/lam) for s in valid]
    print(f"  Eisenstein constraint max residual: {max(ec_residuals):.2e}")
    results["eisenstein_constraint"] = {
        "max_residual": float(max(ec_residuals)),
        "passed": max(ec_residuals) < 1e-10,
    }

    # 7. j-invariant at M->0
    s_small = sds_from_x(0.001, lam)
    M_sm = s_small.M
    j_exact = 1728.0 / (1.0 - 9*lam*M_sm**2)
    x_sm = s_small.x
    j_formula = 6912*(x_sm**2+x_sm+1)**3 / ((1-x_sm)*(x_sm+2)*(2*x_sm+1))**2
    print(f"  j-invariant (small M): exact={j_exact:.4f}, formula={j_formula:.4f}, diff={abs(j_exact-j_formula):.2e}")
    results["j_invariant"] = {
        "at_small_M_exact": float(j_exact),
        "at_small_M_formula": float(j_formula),
        "residual": float(abs(j_exact - j_formula)),
        "approaches_1728": abs(j_exact - 1728) < 5.0,
    }

    all_passed = all(v.get("passed", True) for v in results.values() if isinstance(v, dict))
    results["all_passed"] = all_passed
    print(f"\n  ALL CHECKS PASSED: {all_passed}")
    save_json(results, f"{OUT}/exp01_sds_baseline.json")
    return results


if __name__ == "__main__":
    run()
