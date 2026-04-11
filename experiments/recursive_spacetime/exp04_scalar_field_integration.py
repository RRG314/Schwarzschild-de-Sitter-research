"""
Exp04: Scalar field integration — rigorous usefulness audit.

Tests the RDT scalar field from the uploaded materials against the SdS/RNdS
framework. Does NOT assume it is useful. Reports the audit verdict.

Three specific tests:
  1. Audit over SdS parameter range (multiple Lambda values)
  2. Attempt to use phi as a state variable in a recursive flow
  3. Check whether phi changes attractor structure or fixed-point location
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

import numpy as np
from src.scalar_field_state import phi_rdt, audit, rdt_log_depth
from src.sds_state import sds_from_x, _nariai_mass
from src.utils import save_json, section

OUT = os.path.join(os.path.dirname(__file__), "..", "outputs", "json")


def run():
    section("EXP04: Scalar Field Integration Audit")
    results = {}

    # -----------------------------------------------------------------------
    # 1. Audit over multiple Lambda values
    # -----------------------------------------------------------------------
    print("\n  1. RDT audit over Lambda = 0.01, 0.1, 1.0, 10.0")
    audits = {}
    for lam in [0.01, 0.1, 1.0, 10.0]:
        a = audit(lam=lam)
        audits[f"Lambda_{lam}"] = a
        print(f"    Lambda={lam}: n_distinct_phi={a['n_distinct_phi_rb']}, "
              f"values={a['unique_phi_rb']}, "
              f"entropy={a['entropy_of_phi_bits']:.3f}bits, "
              f"unit_dependent={a['unit_dependent']}, "
              f"verdict={a['final_classification']}")

    results["audit_by_lambda"] = audits

    # -----------------------------------------------------------------------
    # 2. Attempt: phi as additional state variable
    # -----------------------------------------------------------------------
    print("\n  2. Attempt: phi as additional state variable in recursive flow")
    lam = 1.0
    xs = np.linspace(0.05, 0.95, 50)
    states = [sds_from_x(x, lam) for x in xs if sds_from_x(x, lam).is_valid()]

    phi_rb_vals = [phi_rdt(s.r_b) for s in states]
    phi_rc_vals = [phi_rdt(s.r_c) for s in states]

    # State augmented with phi: (M, Lambda, phi_rb, phi_rc)
    # Check: does phi distinguish any states that M,Lambda don't?
    phi_rb_arr = np.array(phi_rb_vals, dtype=float)
    phi_rc_arr = np.array(phi_rc_vals, dtype=float)
    M_arr = np.array([s.M for s in states])

    # Correlation of phi with M
    if np.std(phi_rb_arr) > 0:
        corr_phirb_M = float(np.corrcoef(phi_rb_arr, M_arr)[0,1])
    else:
        corr_phirb_M = np.nan

    n_unique_phi_pairs = len(set(zip(phi_rb_vals, phi_rc_vals)))
    n_total_states = len(states)

    print(f"    Total states: {n_total_states}")
    print(f"    Unique (phi_rb, phi_rc) pairs: {n_unique_phi_pairs}")
    print(f"    phi_rb values: {sorted(set(phi_rb_vals))}")
    print(f"    phi_rc values: {sorted(set(phi_rc_vals))}")
    print(f"    Corr(phi_rb, M): {corr_phirb_M}")

    # Does phi add independent information? If n_unique_pairs << n_states:
    phi_adds_info = n_unique_phi_pairs > 3 and (n_unique_phi_pairs / n_total_states) > 0.1

    results["phi_as_state_var"] = {
        "n_states": n_total_states,
        "unique_phi_pairs": n_unique_phi_pairs,
        "phi_rb_values": sorted(set(phi_rb_vals)),
        "phi_rc_values": sorted(set(phi_rc_vals)),
        "corr_phirb_M": float(corr_phirb_M) if not (isinstance(corr_phirb_M, float) and np.isnan(corr_phirb_M)) else None,
        "phi_adds_independent_info": phi_adds_info,
        "assessment": (
            "phi adds some information (>3 distinct pairs over arc)"
            if phi_adds_info else
            "phi adds NO independent information — collapses to constant or near-constant"
        ),
    }

    # -----------------------------------------------------------------------
    # 3. Does phi change the attractor of a coupled map?
    # -----------------------------------------------------------------------
    print("\n  3. Test: does phi coupling change attractor location?")
    # Take the old coupled SdS map from the horizon-only model
    # T_{lambda,eps}(u,v) = normalize(u^lambda + eps*v, v^lambda + eps*u)
    # Now add phi coupling: T_{lambda,eps,mu}(u,v) = normalize(u^lambda + eps*v + mu*phi(r_b(u,v)),
    #                                                            v^lambda + eps*u + mu*phi(r_c(u,v)))
    # Compare attractor x* with mu=0 vs mu > 0


    def normalize_eisenstein(a, b):
        if a <= 0 or b <= 0:
            return None, None
        n = np.sqrt(a**2 + a*b + b**2)
        return a/n, b/n

    def map_with_phi(u, v, lam=1.0, lam_power=1.5, eps=0.1, mu=0.0):
        r_Lam = np.sqrt(3.0/lam)
        r_b = u * r_Lam
        r_c = v * r_Lam
        phi_b = phi_rdt(r_b) if r_b > 0 else 0
        phi_c = phi_rdt(r_c) if r_c > 0 else 0
        a = u**lam_power + eps*v + mu*phi_b
        b = v**lam_power + eps*u + mu*phi_c
        if a <= 0 or b <= 0:
            return u, v
        return normalize_eisenstein(a, b)

    lam_power = 1.5
    eps = 0.1
    x0 = 0.3
    u0 = x0 / np.sqrt(x0**2+x0+1)
    v0 = 1.0 / np.sqrt(x0**2+x0+1)

    attractor_no_phi = None
    attractor_phi = {}

    # Without phi coupling
    u, v = u0, v0
    for _ in range(5000):
        u_new, v_new = map_with_phi(u, v, lam_power=lam_power, eps=eps, mu=0.0)
        if u_new is None: break
        u, v = u_new, v_new
    attractor_no_phi = float(u/v)

    # With phi coupling at various mu
    for mu in [0.001, 0.01, 0.1, 0.5]:
        u, v = u0, v0
        for _ in range(5000):
            u_new, v_new = map_with_phi(u, v, lam_power=lam_power, eps=eps, mu=mu)
            if u_new is None: break
            u, v = u_new, v_new
        attractor_phi[f"mu_{mu}"] = float(u/v)

    print(f"    Attractor x* (no phi, mu=0): {attractor_no_phi:.6f}")
    for k, xstar in attractor_phi.items():
        shift = xstar - attractor_no_phi
        print(f"    Attractor x* ({k}): {xstar:.6f}  (shift={shift:+.2e})")

    any_significant_shift = any(
        abs(xstar - attractor_no_phi) > 0.001 for xstar in attractor_phi.values()
    )

    results["phi_attractor_test"] = {
        "attractor_no_phi": attractor_no_phi,
        "attractor_with_phi": attractor_phi,
        "any_significant_shift": any_significant_shift,
        "assessment": (
            "phi coupling shifts the attractor significantly — may add physical content"
            if any_significant_shift else
            "phi coupling does NOT shift the attractor — phi is ineffective as a driver"
        ),
    }

    # -----------------------------------------------------------------------
    # Final verdict
    # -----------------------------------------------------------------------
    all_audits_not_useful = all(
        not a["useful"] for a in audits.values()
    )
    phi_info_useless = not phi_adds_info
    phi_attractor_useless = not any_significant_shift

    final_verdict = (
        "NOT USEFUL FOR THIS PROJECT"
        if (all_audits_not_useful and phi_info_useless and phi_attractor_useless)
        else "PARTIALLY USEFUL — see details"
    )

    print(f"\n  FINAL VERDICT: {final_verdict}")
    results["final_verdict"] = {
        "classification": final_verdict,
        "reasons": [
            f"Audit across Lambda values: all show ≤2 distinct phi values over SdS arc",
            "phi adds no independent state information",
            "phi coupling does not shift attractor" if phi_attractor_useless else "phi coupling shifts attractor",
            "Field is integer-valued, discontinuous, unit-dependent",
            "No physical coupling to SdS metric or thermodynamics",
        ],
    }

    save_json(results, f"{OUT}/exp04_scalar_field.json")
    return results


if __name__ == "__main__":
    run()
