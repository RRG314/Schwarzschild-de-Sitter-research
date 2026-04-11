"""
tests/test_state_space.py
=========================
Unit tests for the state_space module.
All tested against known analytic values.
"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

import numpy as np
from src.state_space import (
    x_to_uv, uv_to_x, eisenstein_norm_sq, normalize_to_ellipse,
    entropies, entropy_deficit, temperatures, temperature_ratio,
    carnot_efficiency, mass, nariai_mass, j_invariant, verify_constraint
)


PI = np.pi
LAMBDA = 1.0


def test_eisenstein_norm_at_midpoint():
    """At x = 0.5: u = 0.5/sqrt(0.75), v = 1/sqrt(0.75)."""
    u, v = x_to_uv(0.5)
    N = eisenstein_norm_sq(u, v)
    assert abs(N - 1.0) < 1e-12, f"Eisenstein norm should be 1, got {N}"


def test_uv_roundtrip():
    """x -> (u, v) -> x should be identity."""
    for x in [0.1, 0.3, 0.5, 0.7, 0.9]:
        u, v = x_to_uv(x)
        x_back = uv_to_x(u, v)
        assert abs(x_back - x) < 1e-12, f"Roundtrip failed at x={x}"


def test_normalization():
    """normalize_to_ellipse should return point on unit ellipse."""
    for a, b in [(0.3, 0.7), (0.5, 0.5), (0.1, 0.9)]:
        u, v = normalize_to_ellipse(a, b)
        N = eisenstein_norm_sq(u, v)
        assert abs(N - 1.0) < 1e-12


def test_entropy_identity():
    """S_Lambda = S_b + S_c + sqrt(S_b * S_c) = 3*pi/Lambda."""
    S_Lambda_exact = 3.0 * PI / LAMBDA
    for x in [0.1, 0.3, 0.5, 0.7, 0.9]:
        u, v = x_to_uv(x)
        sb, sc = entropies(u, v)
        delta = entropy_deficit(u, v)
        S_Lambda_computed = sb + sc + delta
        assert abs(S_Lambda_computed - S_Lambda_exact) < 1e-10, \
            f"Entropy identity failed at x={x}: got {S_Lambda_computed}, expected {S_Lambda_exact}"


def test_temperature_ratio():
    """T_c / T_b = x(2+x)/(1+2x)."""
    for x in [0.2, 0.4, 0.6, 0.8]:
        u, v = x_to_uv(x)
        tb, tc = temperatures(u, v)
        ratio_computed = tc / tb
        ratio_formula = x * (2 + x) / (1 + 2 * x)
        assert abs(ratio_computed - ratio_formula) < 1e-10, \
            f"T_ratio failed at x={x}: got {ratio_computed}, expected {ratio_formula}"


def test_carnot_formula():
    """eta_C = 1 - T_c/T_b = (1 - x^2)/(1 + 2x)."""
    for x in [0.2, 0.4, 0.6, 0.8]:
        u, v = x_to_uv(x)
        eta = carnot_efficiency(u, v)
        t_ratio = temperature_ratio(u, v)
        assert abs(eta - (1 - t_ratio)) < 1e-12, \
            f"Carnot formula mismatch at x={x}"


def test_nariai_limit():
    """At Nariai x -> 1: T_b and T_c both -> 0."""
    u, v = x_to_uv(0.999)
    tb, tc = temperatures(u, v)
    assert tb < 0.01 and tc < 0.01, f"Temperatures at Nariai should be small: T_b={tb}, T_c={tc}"


def test_pure_ds_limit():
    """At x -> 0: T_c -> sqrt(Lambda)/(2*pi*sqrt(3)) and T_b -> infinity."""
    u, v = x_to_uv(0.001)
    tb, tc = temperatures(u, v)
    tc_expected = np.sqrt(LAMBDA) / (2 * PI * np.sqrt(3))
    assert abs(tc / tc_expected - 1.0) < 0.01, \
        f"T_c at pure dS limit wrong: got {tc}, expected {tc_expected}"
    assert tb > 1.0, f"T_b should be large near pure dS: {tb}"


def test_mass_range():
    """0 <= M <= M_Nariai for all physical x."""
    M_N = nariai_mass()
    for x in np.linspace(0.01, 0.99, 20):
        u, v = x_to_uv(x)
        M = mass(u, v)
        assert 0 <= M <= M_N + 1e-10, f"Mass out of range at x={x}: M={M}, M_N={M_N}"


def test_j_invariant_pure_ds():
    """At M=0 (x -> 0): j -> 1728."""
    u, v = x_to_uv(0.001)
    j = j_invariant(u, v)
    assert abs(j - 1728) / 1728 < 0.01, f"j at pure dS should be ~1728, got {j}"


def test_verify_constraint():
    """verify_constraint should pass for all valid (u,v)."""
    for x in [0.1, 0.5, 0.9]:
        u, v = x_to_uv(x)
        assert verify_constraint(u, v), f"Constraint failed at x={x}"


if __name__ == "__main__":
    # Run all tests manually
    test_fns = [
        test_eisenstein_norm_at_midpoint,
        test_uv_roundtrip,
        test_normalization,
        test_entropy_identity,
        test_temperature_ratio,
        test_carnot_formula,
        test_nariai_limit,
        test_pure_ds_limit,
        test_mass_range,
        test_j_invariant_pure_ds,
        test_verify_constraint,
    ]
    passed = 0
    failed = 0
    for fn in test_fns:
        try:
            fn()
            print(f"  PASS  {fn.__name__}")
            passed += 1
        except Exception as e:
            print(f"  FAIL  {fn.__name__}: {e}")
            failed += 1
    print(f"\n  {passed}/{passed+failed} tests passed")
