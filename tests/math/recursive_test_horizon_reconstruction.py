"""
test_horizon_reconstruction.py

Verify that the cubic/quartic root solvers give physically correct results.
Tests: root signs, ordering, Vieta identities.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

import numpy as np
from src.sds_state import SdSState, _nariai_mass
from src.rnds_state import RNdSState, _solve_rnds_quartic


def test_sds_cubic_vieta():
    """
    For SdS, the cubic r^3 - (3/Lambda)*r + 6M/Lambda = 0 has Vieta relations:
      r_- + r_b + r_c = 0
      r_-*r_b + r_-*r_c + r_b*r_c = -3/Lambda
      r_-*r_b*r_c = -6M/Lambda
    """
    test_cases = [(0.1, 1.0), (0.05, 2.0), (0.2, 0.5), (0.3, 1.0)]
    for M, lam in test_cases:
        s = SdSState(M, lam)
        if not s.admissible:
            continue
        r_minus = s.r_minus
        r_b = s.r_b
        r_c = s.r_c
        lam_val = lam

        e1 = r_minus + r_b + r_c  # should be 0
        e2 = r_minus*r_b + r_minus*r_c + r_b*r_c  # should be -3/Lambda
        e3 = r_minus*r_b*r_c  # should be -6M/Lambda

        assert abs(e1) < 1e-10, f"Vieta e1 = {e1:.2e} for M={M}, lam={lam}"
        assert abs(e2 - (-3.0/lam)) < 1e-10, f"Vieta e2 residual = {abs(e2+3.0/lam):.2e}"
        assert abs(e3 - (-6.0*M/lam)) < 1e-10, f"Vieta e3 residual = {abs(e3+6.0*M/lam):.2e}"
    print(f"  [PASS] sds_cubic_vieta")


def test_sds_root_signs():
    """r_- < 0 < r_b < r_c for all valid SdS states."""
    lam = 1.0
    M_nar = _nariai_mass(lam)
    for M in np.linspace(0.05*M_nar, 0.95*M_nar, 20):
        s = SdSState(M, lam)
        if s.is_valid():
            assert s.r_minus < 0, f"r_- not negative: {s.r_minus}"
            assert s.r_b > 0, f"r_b not positive: {s.r_b}"
            assert s.r_c > 0, f"r_c not positive: {s.r_c}"
            assert s.r_b < s.r_c, f"r_b >= r_c: {s.r_b} >= {s.r_c}"
    print(f"  [PASS] sds_root_signs")


def test_rnds_quartic_vieta():
    """
    For RNdS quartic r^4 - (3/Lam)r^2 + (6M/Lam)r - (3Q^2/Lam) = 0:
      e1 = sum(r_i) = 0
      e2 = sum(r_i*r_j, i<j) = -3/Lambda
      e3 = sum(r_i*r_j*r_k, i<j<k) = -6M/Lambda
      e4 = product(r_i) = -3Q^2/Lambda
    """
    test_cases = [(0.1, 0.05, 1.0), (0.2, 0.1, 0.5), (0.15, 0.08, 2.0)]
    for M, Q, lam in test_cases:
        s = RNdSState(M, Q, lam)
        if not s.is_valid():
            continue
        v = s.vieta_check()
        for key, val in v.items():
            if key != "admissible":
                assert val < 1e-8, f"Vieta {key} = {val:.2e} for M={M}, Q={Q}, lam={lam}"
    print(f"  [PASS] rnds_quartic_vieta")


def test_rnds_root_ordering():
    """r_- < 0 < r_inner < r_outer < r_cosmo for valid RNdS states."""
    test_cases = [(0.1, 0.05, 1.0), (0.2, 0.1, 0.5), (0.08, 0.03, 2.0)]
    for M, Q, lam in test_cases:
        s = RNdSState(M, Q, lam)
        if not s.is_valid():
            continue
        assert s.r_minus < 0
        assert s.r_inner > 0
        assert s.r_inner < s.r_outer
        assert s.r_outer < s.r_cosmo
    print(f"  [PASS] rnds_root_ordering")


def test_rnds_blackening_function_zeros():
    """f(r_i) ≈ 0 at each horizon root."""
    from src.rnds_state import _rnds_f
    test_cases = [(0.1, 0.05, 1.0), (0.2, 0.1, 0.5)]
    for M, Q, lam in test_cases:
        s = RNdSState(M, Q, lam)
        if not s.is_valid():
            continue
        for r, name in [(s.r_inner, "inner"), (s.r_outer, "outer"), (s.r_cosmo, "cosmo")]:
            fval = abs(_rnds_f(r, M, Q, lam))
            assert fval < 1e-10, f"f({name}={r:.4f}) = {fval:.2e} not ~0"
    print(f"  [PASS] rnds_blackening_function_zeros")


def test_sds_blackening_function_zeros():
    """f(r_b) ≈ 0 and f(r_c) ≈ 0 for SdS."""
    def f_sds(r, M, lam):
        if r <= 0:
            return float('inf')
        return 1.0 - 2.0*M/r - lam*r**2/3.0

    lam = 1.0
    M_nar = _nariai_mass(lam)
    for M in np.linspace(0.1*M_nar, 0.9*M_nar, 10):
        s = SdSState(M, lam)
        if s.is_valid():
            fb = abs(f_sds(s.r_b, M, lam))
            fc = abs(f_sds(s.r_c, M, lam))
            assert fb < 1e-10, f"f(r_b={s.r_b:.4f}) = {fb:.2e}"
            assert fc < 1e-10, f"f(r_c={s.r_c:.4f}) = {fc:.2e}"
    print(f"  [PASS] sds_blackening_function_zeros")


def test_sds_q0_matches_rnds():
    """RNdSState(M, Q=0, Lambda) should give r_outer ≈ r_b, r_cosmo ≈ r_c of SdSState."""
    M, lam = 0.15, 1.0
    s_sds = SdSState(M, lam)
    s_rnds = RNdSState(M, 1e-6, lam)  # Q ~ 0

    if not (s_sds.is_valid() and s_rnds.is_valid()):
        print(f"  [SKIP] sds_q0_matches_rnds (invalid states)")
        return

    # At Q=0, RNdS should reduce to SdS
    assert abs(s_rnds.r_outer - s_sds.r_b) / s_sds.r_b < 0.01, \
        f"r_outer={s_rnds.r_outer:.4f} vs r_b={s_sds.r_b:.4f}"
    assert abs(s_rnds.r_cosmo - s_sds.r_c) / s_sds.r_c < 0.01, \
        f"r_cosmo={s_rnds.r_cosmo:.4f} vs r_c={s_sds.r_c:.4f}"
    print(f"  [PASS] sds_q0_matches_rnds")


if __name__ == "__main__":
    tests = [
        test_sds_cubic_vieta,
        test_sds_root_signs,
        test_rnds_quartic_vieta,
        test_rnds_root_ordering,
        test_rnds_blackening_function_zeros,
        test_sds_blackening_function_zeros,
        test_sds_q0_matches_rnds,
    ]
    passed = 0
    failed = 0
    for t in tests:
        try:
            t()
            passed += 1
        except AssertionError as e:
            print(f"  [FAIL] {t.__name__}: {e}")
            failed += 1
    print(f"\n  Results: {passed} passed, {failed} failed")
