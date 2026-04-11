"""
test_sds_identities.py

Verify that all SdS exact algebraic identities hold to machine precision.
These are NOT approximations — they must hold to < 1e-10 or the
solver/formulas have a bug.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

import math
import numpy as np
from src.sds_state import SdSState, sds_from_x, _nariai_mass


PI = math.pi


def _get_valid_states(n=30):
    """Return a list of valid SdSState objects across parameter space."""
    states = []
    for lam in [0.1, 0.5, 1.0, 2.0]:
        M_nar = _nariai_mass(lam)
        for M in np.linspace(0.05 * M_nar, 0.95 * M_nar, n):
            s = SdSState(M, lam)
            if s.is_valid():
                states.append(s)
    return states


def test_entropy_identity():
    """S_Lambda = S_b + S_c + sqrt(S_b * S_c) to machine precision."""
    states = _get_valid_states()
    assert len(states) > 20, f"Not enough valid states: {len(states)}"
    max_resid = 0.0
    for s in states:
        resid = s.entropy_identity_residual()
        max_resid = max(max_resid, resid)
    assert max_resid < 1e-10, f"Entropy identity max residual: {max_resid:.2e}"
    print(f"  [PASS] entropy_identity: max_resid={max_resid:.2e}")


def test_s_lambda_formula():
    """S_Lambda = 3*pi/Lambda (from de Sitter area)."""
    states = _get_valid_states()
    for s in states:
        expected = 3.0 * PI / s.Lambda
        resid = abs(s.S_Lambda - expected) / expected
        assert resid < 1e-12, f"S_Lambda formula residual={resid:.2e}"
    print(f"  [PASS] s_lambda_formula")


def test_entropy_areas():
    """S_b = pi * r_b^2, S_c = pi * r_c^2."""
    states = _get_valid_states()
    for s in states:
        resid_b = abs(s.S_b - PI * s.r_b**2)
        resid_c = abs(s.S_c - PI * s.r_c**2)
        assert resid_b < 1e-12, f"S_b area residual={resid_b:.2e}"
        assert resid_c < 1e-12, f"S_c area residual={resid_c:.2e}"
    print(f"  [PASS] entropy_areas")


def test_eisenstein_constraint():
    """r_b^2 + r_b*r_c + r_c^2 = 3/Lambda (Vieta)."""
    states = _get_valid_states()
    max_resid = 0.0
    for s in states:
        lhs = s.r_b**2 + s.r_b * s.r_c + s.r_c**2
        rhs = 3.0 / s.Lambda
        resid = abs(lhs - rhs) / rhs
        max_resid = max(max_resid, resid)
    assert max_resid < 1e-10, f"Eisenstein constraint max residual: {max_resid:.2e}"
    print(f"  [PASS] eisenstein_constraint: max_resid={max_resid:.2e}")


def test_temperatures_positive():
    """T_b, T_c > 0 for all valid states."""
    states = _get_valid_states()
    for s in states:
        assert s.T_b > 0, f"T_b <= 0: {s.T_b}"
        assert s.T_c > 0, f"T_c <= 0: {s.T_c}"
    print(f"  [PASS] temperatures_positive ({len(states)} states)")


def test_temperature_ordering():
    """T_b > T_c for all valid SdS states (hotter black hole horizon)."""
    states = _get_valid_states()
    for s in states:
        assert s.T_b > s.T_c, f"T_b={s.T_b:.4f} not > T_c={s.T_c:.4f} at M={s.M:.4f}, Lam={s.Lambda}"
    print(f"  [PASS] temperature_ordering T_b > T_c ({len(states)} states)")


def test_sub_extremal_horizon_ordering():
    """r_b < r_c for all valid states."""
    states = _get_valid_states()
    for s in states:
        assert s.r_b < s.r_c, f"r_b={s.r_b:.4f} not < r_c={s.r_c:.4f}"
    print(f"  [PASS] sub_extremal_ordering r_b < r_c ({len(states)} states)")


def test_carnot_efficiency_range():
    """0 < eta_C < 1 for all valid states."""
    states = _get_valid_states()
    for s in states:
        assert 0 < s.eta_C < 1, f"eta_C={s.eta_C:.4f} out of (0,1)"
    print(f"  [PASS] carnot_efficiency_range ({len(states)} states)")


def test_delta_equals_sqrt_product():
    """Delta = sqrt(S_b * S_c) = pi * r_b * r_c."""
    states = _get_valid_states()
    for s in states:
        expected = math.sqrt(s.S_b * s.S_c)
        resid = abs(s.Delta - expected) / (expected + 1e-30)
        assert resid < 1e-12, f"Delta residual={resid:.2e}"
    print(f"  [PASS] delta_equals_sqrt_product ({len(states)} states)")


def test_x_ratio_in_unit_interval():
    """x = r_b/r_c ∈ (0, 1)."""
    states = _get_valid_states()
    for s in states:
        x = s.r_b / s.r_c
        assert 0 < x < 1, f"x={x:.4f} not in (0,1)"
    print(f"  [PASS] x_in_unit_interval ({len(states)} states)")


def test_sds_from_x_roundtrip():
    """sds_from_x reconstructs M, Lambda consistent with x."""
    lam = 1.0
    for x in [0.1, 0.3, 0.5, 0.7, 0.9]:
        s = sds_from_x(x, lam)
        if s.is_valid():
            x_computed = s.r_b / s.r_c
            assert abs(x_computed - x) < 0.01, f"x roundtrip failed: {x_computed:.4f} vs {x}"
    print(f"  [PASS] sds_from_x_roundtrip")


if __name__ == "__main__":
    tests = [
        test_entropy_identity,
        test_s_lambda_formula,
        test_entropy_areas,
        test_eisenstein_constraint,
        test_temperatures_positive,
        test_temperature_ordering,
        test_sub_extremal_horizon_ordering,
        test_carnot_efficiency_range,
        test_delta_equals_sqrt_product,
        test_x_ratio_in_unit_interval,
        test_sds_from_x_roundtrip,
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
