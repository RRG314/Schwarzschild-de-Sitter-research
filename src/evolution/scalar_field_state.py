"""
scalar_field_state.py
=====================
Implements the RDT scalar field exactly as described in the uploaded materials,
then performs a rigorous usefulness audit against the SdS/RNdS framework.

The RDT scalar field (from uploaded code):
  phi(x, y) = R(floor(sqrt(x^2 + y^2)))
  where R(n) = rdt_log_depth(n, alpha) = number of steps to reduce n to ≤ 1
  by repeatedly dividing by floor(log(n)^alpha), with divisor clamped to ≥ 2.

This module:
1. Implements the field exactly as uploaded
2. Evaluates it over the SdS/RNdS parameter ranges
3. Reports what values it takes and whether they add any information
4. Draws an honest verdict

IMPORTANT: Do not use this module's field as a physics input unless
the audit shows it is meaningful. The audit currently shows it is NOT useful.
See audit() function for detailed verdict.
"""

import numpy as np
import math


# ---------------------------------------------------------------------------
# Exact implementation of uploaded RDT scalar field
# ---------------------------------------------------------------------------

def rdt_log_depth(n: int, alpha: float = 1.5) -> int:
    """
    Compute RDT depth of integer n using repeated division by floor(log(n)^alpha).

    Exactly as in the uploaded visualizer code:
      if n <= 1: return 0
      while x > 1:
          d = int(log(x)^alpha), d = max(2, d)
          x = x // d
          steps += 1
    """
    if n <= 1:
        return 0
    steps = 0
    x = int(n)
    while x > 1:
        d = int(math.log(x) ** alpha)
        d = max(2, d)
        x = x // d
        if x == 0:
            break
        steps += 1
        if steps > 1000:
            break
    return steps


def phi_rdt(r: float, alpha: float = 1.5) -> int:
    """
    RDT scalar field value at radius r (1D version for horizon radii).
    phi(r) = R(floor(r)).
    """
    n = max(1, int(math.floor(r)))
    return rdt_log_depth(n, alpha)


# ---------------------------------------------------------------------------
# Audit function
# ---------------------------------------------------------------------------

def audit(lam: float = 1.0, alpha: float = 1.5) -> dict:
    """
    Rigorous usefulness audit of the RDT scalar field
    over the SdS physical parameter range.

    Returns a dict with verdict and supporting evidence.
    """
    import sys
    sys.path.insert(0, '..')
    from src.sds_state import sds_from_x

    # Physical range of r_b, r_c for Lambda = lam
    r_Lambda = math.sqrt(3.0 / lam)
    r_b_range = (1e-3, r_Lambda - 1e-3)
    r_c_range = (1e-3, r_Lambda - 1e-3)

    # Sample many (r_b, r_c) pairs
    xs = np.linspace(0.01, 0.99, 100)
    r_b_vals = []
    r_c_vals = []
    phi_rb_vals = []
    phi_rc_vals = []

    for x in xs:
        try:
            s = sds_from_x(x, lam)
            if s.is_valid():
                r_b_vals.append(s.r_b)
                r_c_vals.append(s.r_c)
                phi_rb_vals.append(phi_rdt(s.r_b, alpha))
                phi_rc_vals.append(phi_rdt(s.r_c, alpha))
        except Exception:
            pass

    r_b_vals = np.array(r_b_vals)
    r_c_vals = np.array(r_c_vals)
    phi_rb = np.array(phi_rb_vals)
    phi_rc = np.array(phi_rc_vals)

    unique_phi_rb = np.unique(phi_rb)
    unique_phi_rc = np.unique(phi_rc)

    # Check 1: How many distinct values does phi take?
    n_distinct_rb = len(unique_phi_rb)
    n_distinct_rc = len(unique_phi_rc)

    # Check 2: Is phi constant over the arc?
    phi_rb_constant = bool(np.all(phi_rb == phi_rb[0])) if len(phi_rb) > 0 else True
    phi_rc_constant = bool(np.all(phi_rc == phi_rc[0])) if len(phi_rc) > 0 else True

    # Check 3: Does phi correlate with any physical observable?
    # Compute correlation with x = r_b/r_c
    if len(phi_rb) > 5 and len(np.unique(phi_rb)) > 1:
        corr_rb_x = float(np.corrcoef(phi_rb, r_b_vals / r_c_vals)[0, 1])
    else:
        corr_rb_x = np.nan  # can't compute if constant

    # Check 4: Is the field unit-dependent?
    # If we rescale by factor 2 (change of units):
    phi_rb_rescaled = np.array([phi_rdt(r * 2.0, alpha) for r in r_b_vals])
    unit_dependent = bool(not np.allclose(phi_rb, phi_rb_rescaled))

    # Check 5: Does adding phi as state variable create new dimensions?
    # phi is integer-valued, constant or near-constant over the arc.
    # Count the actual information content.
    if len(phi_rb) > 0:
        entropy_of_phi = 0.0
        counts = np.bincount(phi_rb.astype(int))
        counts = counts[counts > 0]
        probs = counts / counts.sum()
        entropy_of_phi = float(-np.sum(probs * np.log2(probs + 1e-30)))
    else:
        entropy_of_phi = 0.0

    verdict = _build_verdict(
        lam=lam,
        r_Lambda=r_Lambda,
        n_distinct_rb=n_distinct_rb,
        n_distinct_rc=n_distinct_rc,
        phi_rb_constant=phi_rb_constant,
        phi_rc_constant=phi_rc_constant,
        unique_phi_rb=unique_phi_rb.tolist(),
        unique_phi_rc=unique_phi_rc.tolist(),
        entropy_of_phi=entropy_of_phi,
        corr_rb_x=corr_rb_x,
        unit_dependent=unit_dependent,
        r_b_range=(float(r_b_vals.min()), float(r_b_vals.max())) if len(r_b_vals) > 0 else (np.nan, np.nan),
    )

    return verdict


def _build_verdict(lam, r_Lambda, n_distinct_rb, n_distinct_rc,
                    phi_rb_constant, phi_rc_constant,
                    unique_phi_rb, unique_phi_rc,
                    entropy_of_phi, corr_rb_x, unit_dependent, r_b_range):
    """
    Build the honest verdict dict.
    """
    useful = (
        not phi_rb_constant
        and n_distinct_rb > 3
        and entropy_of_phi > 0.5
        and not unit_dependent
    )

    reasons_not_useful = []
    if phi_rb_constant:
        reasons_not_useful.append(
            f"phi is CONSTANT over the SdS arc at Lambda={lam}: "
            f"all r_b ∈ ({r_b_range[0]:.3f}, {r_b_range[1]:.3f}) give floor(r_b)=same integer."
        )
    if n_distinct_rb <= 2:
        reasons_not_useful.append(
            f"phi takes only {n_distinct_rb} distinct value(s) over the arc: {unique_phi_rb}. "
            f"Cannot be a useful state variable."
        )
    if unit_dependent:
        reasons_not_useful.append(
            "phi is unit-dependent: rescaling r by 2 changes phi values. "
            "This makes phi physically meaningless — it depends on arbitrary unit choices."
        )
    if entropy_of_phi < 0.5:
        reasons_not_useful.append(
            f"Information content of phi is very low: entropy = {entropy_of_phi:.3f} bits. "
            f"(Maximum possible = log2({n_distinct_rb}) = {np.log2(max(n_distinct_rb,1)):.2f} bits)"
        )

    return {
        "Lambda": lam,
        "r_Lambda": r_Lambda,
        "r_b_range": r_b_range,
        "n_distinct_phi_rb": n_distinct_rb,
        "n_distinct_phi_rc": n_distinct_rc,
        "unique_phi_rb": unique_phi_rb,
        "unique_phi_rc": unique_phi_rc,
        "phi_rb_constant": phi_rb_constant,
        "entropy_of_phi_bits": entropy_of_phi,
        "corr_phi_rb_with_x": float(corr_rb_x) if not (isinstance(corr_rb_x, float) and np.isnan(corr_rb_x)) else None,
        "unit_dependent": unit_dependent,
        "useful": useful,
        "reasons_not_useful": reasons_not_useful,
        "final_classification": (
            "USEFUL AND RETAINED" if useful else
            "NOT USEFUL FOR THIS PROJECT"
        ),
    }
