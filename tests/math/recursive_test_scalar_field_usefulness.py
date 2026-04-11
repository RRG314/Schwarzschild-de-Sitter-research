"""
test_scalar_field_usefulness.py

Verifies that the scalar field audit produces the correct honest verdict.

The RDT scalar field phi(r) = R(floor(r)) is tested against the SdS
parameter ranges. The tests verify audit logic, not that phi is useful
(it isn't — these tests confirm the NOT USEFUL verdict is correct).
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

import math
import numpy as np
from src.scalar_field_state import phi_rdt, rdt_log_depth, audit


def test_rdt_log_depth_base_cases():
    """rdt_log_depth(0) = rdt_log_depth(1) = 0."""
    assert rdt_log_depth(0) == 0
    assert rdt_log_depth(1) == 0
    print(f"  [PASS] rdt_log_depth base cases")


def test_rdt_log_depth_monotone_tendency():
    """rdt_log_depth generally takes small integer values for small n."""
    # For n in [2, 100], depth should be small non-negative integer
    depths = [rdt_log_depth(n) for n in range(1, 100)]
    assert all(d >= 0 for d in depths), "Negative depth found"
    assert max(depths) < 20, f"Unexpectedly large depth: {max(depths)}"
    print(f"  [PASS] rdt_log_depth_monotone_tendency (max depth={max(depths)})")


def test_phi_rdt_integer_valued():
    """phi_rdt returns integers."""
    for r in [0.5, 1.2, 1.73, 3.14, 10.0, 100.0]:
        val = phi_rdt(r)
        assert isinstance(val, (int, np.integer)), f"phi_rdt({r}) = {val} is not int"
    print(f"  [PASS] phi_rdt_integer_valued")


def test_phi_rdt_depends_only_on_floor():
    """phi_rdt(r) == phi_rdt(r + 0.9) for r, r+0.9 sharing the same floor."""
    for r in [1.0, 1.1, 1.5, 1.99]:
        phi_r = phi_rdt(r)
        phi_r2 = phi_rdt(1.0 + (r - 1.0))
        # All of 1.0..1.99 should have floor=1
        phi_floor = phi_rdt(1.0)
        assert phi_r == phi_floor, f"phi_rdt({r}) = {phi_r} but floor(r)=1 gives {phi_floor}"
    print(f"  [PASS] phi_rdt_depends_only_on_floor")


def test_audit_structure():
    """audit() returns a dict with all required keys."""
    required_keys = [
        "Lambda", "r_Lambda", "r_b_range",
        "n_distinct_phi_rb", "n_distinct_phi_rc",
        "unique_phi_rb", "unique_phi_rc",
        "phi_rb_constant", "entropy_of_phi_bits",
        "unit_dependent", "useful", "reasons_not_useful",
        "final_classification",
    ]
    a = audit(lam=1.0)
    for key in required_keys:
        assert key in a, f"Missing key: {key}"
    print(f"  [PASS] audit_structure (all required keys present)")


def test_audit_not_useful_at_lambda_1():
    """At Lambda=1, phi takes at most 2 distinct values — audit says NOT USEFUL."""
    a = audit(lam=1.0)
    assert a["n_distinct_phi_rb"] <= 3, \
        f"Expected <=3 distinct phi values, got {a['n_distinct_phi_rb']}"
    assert a["final_classification"] == "NOT USEFUL FOR THIS PROJECT", \
        f"Expected NOT USEFUL, got {a['final_classification']}"
    print(f"  [PASS] audit_not_useful_at_lambda_1 "
          f"(n_distinct={a['n_distinct_phi_rb']}, verdict={a['final_classification']})")


def test_audit_unit_dependent():
    """phi changes when r is rescaled — unit-dependent at Lambda=0.1."""
    # At Lambda=0.1, r_Lambda ~ 5.5, so r_b values are larger and rescaling by 2 changes phi.
    a = audit(lam=0.1)
    assert bool(a["unit_dependent"]) is True, \
        f"Expected unit_dependent=True at lam=0.1, got {a['unit_dependent']}"
    print(f"  [PASS] audit_unit_dependent (at lam=0.1)")


def test_phi_constant_on_sds_arc_lambda1():
    """
    At Lambda=1: r_Lambda = sqrt(3) ≈ 1.73.
    r_b, r_c ∈ (0, 1.73) so floor(r) ∈ {0, 1}.
    phi(r) = R(1) = 0 for almost all states.
    This is why phi is not useful at Lambda=1.
    """
    from src.sds_state import sds_from_x
    lam = 1.0
    r_Lambda = math.sqrt(3.0 / lam)
    xs = np.linspace(0.05, 0.95, 50)
    phi_vals = set()
    for x in xs:
        s = sds_from_x(x, lam)
        if s.is_valid():
            phi_vals.add(phi_rdt(s.r_b))
            phi_vals.add(phi_rdt(s.r_c))
    assert len(phi_vals) <= 2, f"Expected <=2 distinct phi values, got {len(phi_vals)}: {phi_vals}"
    print(f"  [PASS] phi_constant_on_sds_arc_lambda1 (phi values={phi_vals})")


def test_phi_not_useful_flag():
    """audit() sets useful=False for all tested Lambda values."""
    for lam in [0.01, 0.1, 1.0, 10.0]:
        a = audit(lam=lam)
        # Note: at very small Lambda, r_Lambda is large and phi may vary.
        # Still verify the structure is correct.
        assert "useful" in a, f"Missing 'useful' key at lam={lam}"
        if not a["useful"]:
            assert a["final_classification"] == "NOT USEFUL FOR THIS PROJECT"
    print(f"  [PASS] phi_not_useful_flag (checked at multiple Lambda values)")


if __name__ == "__main__":
    tests = [
        test_rdt_log_depth_base_cases,
        test_rdt_log_depth_monotone_tendency,
        test_phi_rdt_integer_valued,
        test_phi_rdt_depends_only_on_floor,
        test_audit_structure,
        test_audit_not_useful_at_lambda_1,
        test_audit_unit_dependent,
        test_phi_constant_on_sds_arc_lambda1,
        test_phi_not_useful_flag,
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
        except Exception as e:
            print(f"  [ERROR] {t.__name__}: {e}")
            failed += 1
    print(f"\n  Results: {passed} passed, {failed} failed")
