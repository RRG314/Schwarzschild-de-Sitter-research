"""
flow_constraints.py
===================
Physical admissibility checks and conservation law tracking.
Every orbit step should pass these checks. Failures are preserved, not hidden.
"""

import numpy as np
from .sds_state import SdSState, _is_sub_extremal
from .rnds_state import RNdSState, _rnds_admissible

PI = np.pi


def check_sds_orbit(traj: np.ndarray) -> dict:
    """
    Full physical admissibility check for an SdS orbit.

    traj: shape (N, 2), columns = (M, Lambda)

    Returns dict with:
      n_admissible: number of admissible steps
      n_total: total steps
      admissibility_rate: fraction admissible
      S_Lambda_conservation: max relative deviation of S_Lambda along orbit
      temperature_positivity: fraction with T_b > 0 and T_c > 0
      entropy_identity_max_residual: max |S_Lambda - S_b - S_c - Delta|
      subextremal_rate: fraction where 9*Lambda*M^2 < 1
    """
    N = len(traj)
    admissible = np.zeros(N, dtype=bool)
    S_Lambda_vals = np.full(N, np.nan)
    T_b_vals = np.full(N, np.nan)
    T_c_vals = np.full(N, np.nan)
    entropy_residuals = np.full(N, np.nan)
    subextremal = np.zeros(N, dtype=bool)

    for i, (M, lam) in enumerate(traj):
        subextremal[i] = _is_sub_extremal(M, lam)
        s = SdSState(M, lam)
        admissible[i] = s.is_valid()
        if s.admissible:
            S_Lambda_vals[i] = s.S_Lambda
            T_b_vals[i] = s.T_b
            T_c_vals[i] = s.T_c
            entropy_residuals[i] = abs(s.entropy_identity_residual())

    valid_S = S_Lambda_vals[~np.isnan(S_Lambda_vals)]
    valid_res = entropy_residuals[~np.isnan(entropy_residuals)]

    S_Lambda_cons = (
        float(np.std(valid_S) / np.mean(valid_S))
        if len(valid_S) > 1 and np.mean(valid_S) > 0
        else np.nan
    )

    return {
        "n_admissible": int(admissible.sum()),
        "n_total": N,
        "admissibility_rate": float(admissible.mean()),
        "subextremal_rate": float(subextremal.mean()),
        "S_Lambda_conservation_rel_std": S_Lambda_cons,
        "entropy_identity_max_residual": float(valid_res.max()) if len(valid_res) > 0 else np.nan,
        "temperature_positivity_rate": float(
            np.nanmean((T_b_vals > 0) & (T_c_vals > 0))
        ),
    }


def check_rnds_orbit(traj: np.ndarray) -> dict:
    """
    Physical admissibility check for an RNdS orbit.

    traj: shape (N, 3), columns = (M, Q, Lambda)
    """
    N = len(traj)
    admissible = np.zeros(N, dtype=bool)
    T_outer_vals = np.full(N, np.nan)
    T_cosmo_vals = np.full(N, np.nan)
    Delta_vals = np.full(N, np.nan)

    for i, (M, Q, lam) in enumerate(traj):
        s = RNdSState(M, Q, lam)
        admissible[i] = s.is_valid()
        if s.admissible:
            T_outer_vals[i] = s.T_outer
            T_cosmo_vals[i] = s.T_cosmo
            Delta_vals[i] = s.Delta_total

    return {
        "n_admissible": int(admissible.sum()),
        "n_total": N,
        "admissibility_rate": float(admissible.mean()),
        "temperature_positivity_rate": float(
            np.nanmean((T_outer_vals > 0) & (T_cosmo_vals > 0))
        ),
        "Delta_mean": float(np.nanmean(Delta_vals)),
        "Delta_std": float(np.nanstd(Delta_vals)),
    }


def sds_orbit_observables(traj: np.ndarray) -> dict:
    """
    Extract all physical observables along an SdS (M, Lambda) orbit.
    Returns dict of arrays of length N.
    """
    N = len(traj)
    keys = ["M", "Lambda", "r_b", "r_c", "T_b", "T_c",
            "S_b", "S_c", "S_Lambda", "Delta", "x", "eta_C"]
    result = {k: np.full(N, np.nan) for k in keys}
    result["M"] = traj[:, 0]
    result["Lambda"] = traj[:, 1]

    for i, (M, lam) in enumerate(traj):
        s = SdSState(M, lam)
        if s.admissible:
            result["r_b"][i] = s.r_b
            result["r_c"][i] = s.r_c
            result["T_b"][i] = s.T_b
            result["T_c"][i] = s.T_c
            result["S_b"][i] = s.S_b
            result["S_c"][i] = s.S_c
            result["S_Lambda"][i] = s.S_Lambda
            result["Delta"][i] = s.Delta
            result["x"][i] = s.x
            result["eta_C"][i] = s.eta_C

    return result


def rnds_orbit_observables(traj: np.ndarray) -> dict:
    """
    Extract all physical observables along an RNdS (M, Q, Lambda) orbit.
    """
    N = len(traj)
    keys = ["M", "Q", "Lambda", "r_inner", "r_outer", "r_cosmo",
            "T_outer", "T_cosmo", "S_outer", "S_cosmo", "S_Lambda", "Delta_total"]
    result = {k: np.full(N, np.nan) for k in keys}
    result["M"] = traj[:, 0]
    result["Q"] = traj[:, 1]
    result["Lambda"] = traj[:, 2]

    for i, (M, Q, lam) in enumerate(traj):
        s = RNdSState(M, Q, lam)
        if s.admissible:
            result["r_inner"][i] = s.r_inner or np.nan
            result["r_outer"][i] = s.r_outer or np.nan
            result["r_cosmo"][i] = s.r_cosmo or np.nan
            result["T_outer"][i] = s.T_outer
            result["T_cosmo"][i] = s.T_cosmo
            result["S_outer"][i] = s.S_outer
            result["S_cosmo"][i] = s.S_cosmo
            result["S_Lambda"][i] = s.S_Lambda
            result["Delta_total"][i] = s.Delta_total

    return result
