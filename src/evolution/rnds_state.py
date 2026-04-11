"""
rnds_state.py
=============
Full physical state for 4D Reissner-Nordström-de Sitter spacetime.

Parameters: (M, Q, Lambda) — mass, charge, cosmological constant.
The blackening function:
  f(r) = 1 - 2M/r + Q²/r² - Lambda*r²/3

Setting f(r) = 0 and multiplying by 3r²/Lambda (and flipping sign):
  r^4 - (3/Lambda)*r^2 + (6M/Lambda)*r - (3Q^2/Lambda) = 0

This quartic has up to 4 real roots. For sub-extremal charged configurations
with 0 < Q < Q_extremal(M, Lambda) and M < M_Nariai(Q, Lambda):
  r_- < 0 < r_1 (inner/Cauchy) < r_2 (outer/BH) < r_3 (cosmo)

The physics of r_1 (inner horizon) involves causal subtleties.
We work with r_2 (outer BH) and r_3 (cosmo) for thermodynamics.

NOTE: There is NO exact closed-form entropy identity analogous to SdS's
S_Lambda = S_b + S_c + sqrt(S_b*S_c). The correction gap universality
analysis in correction_gap_universality.md shows the RNdS entropy closure
has a non-zero correction gap.

Units: G = hbar = c = kB = 1.
"""

import numpy as np
from dataclasses import dataclass, field
from typing import Optional

PI = np.pi


# ---------------------------------------------------------------------------
# Horizon solver for RNdS quartic
# ---------------------------------------------------------------------------

def _solve_rnds_quartic(
    M: float, Q: float, lam: float
) -> tuple[Optional[float], Optional[float], Optional[float], Optional[float]]:
    """
    Solve: r^4 - (3/Lambda)*r^2 + (6M/Lambda)*r - (3Q^2/Lambda) = 0

    Returns (r_minus, r_inner, r_outer, r_cosmo) if 4 real roots found,
    else returns (None, None, None, None).

    r_minus < 0 < r_inner < r_outer < r_cosmo for fully sub-extremal case.
    """
    if lam <= 0 or M <= 0:
        return None, None, None, None

    coeffs = [1.0, 0.0, -3.0 / lam, 6.0 * M / lam, -3.0 * Q**2 / lam]
    roots_complex = np.roots(coeffs)

    # Extract real roots
    real_roots = sorted(
        r.real for r in roots_complex
        if abs(r.imag) < 1e-7 * (abs(r.real) + 1e-30)
    )

    if len(real_roots) == 4:
        r_minus, r_inner, r_outer, r_cosmo = real_roots
        return r_minus, r_inner, r_outer, r_cosmo
    elif len(real_roots) == 2:
        # Two coincident roots (extremal case)
        return None, None, None, None
    else:
        return None, None, None, None


def _rnds_admissible(M: float, Q: float, lam: float) -> bool:
    """Quick admissibility check before full solve."""
    if M <= 0 or lam <= 0:
        return False
    if Q < 0:
        return False
    r_minus, r_inner, r_outer, r_cosmo = _solve_rnds_quartic(M, Q, lam)
    if r_minus is None:
        return False
    if r_minus >= 0:
        return False
    # We need r_inner < r_outer < r_cosmo, all positive
    if r_inner <= 0 or r_outer <= 0 or r_cosmo <= 0:
        return False
    if not (r_inner < r_outer < r_cosmo):
        return False
    return True


def _rnds_f(r: float, M: float, Q: float, lam: float) -> float:
    """f(r) = 1 - 2M/r + Q²/r² - Lambda*r²/3"""
    if r <= 0:
        return -np.inf
    return 1.0 - 2.0 * M / r + Q**2 / r**2 - lam * r**2 / 3.0


def _rnds_fprime(r: float, M: float, Q: float, lam: float) -> float:
    """f'(r) = 2M/r² - 2Q²/r³ - 2Lambda*r/3"""
    if r <= 0:
        return np.nan
    return 2.0 * M / r**2 - 2.0 * Q**2 / r**3 - 2.0 * lam * r / 3.0


# ---------------------------------------------------------------------------
# Physical state
# ---------------------------------------------------------------------------

@dataclass
class RNdSState:
    """
    Complete physical state for 4D RNdS.

    The outer (r_outer) and cosmological (r_cosmo) horizons have
    well-defined thermodynamics analogous to SdS.
    The inner (r_inner) horizon is a Cauchy horizon — its thermodynamics
    is less well-defined and we report it but use it cautiously.
    """
    M: float
    Q: float
    Lambda: float

    # Derived
    r_minus: Optional[float] = None
    r_inner: Optional[float] = None
    r_outer: Optional[float] = None
    r_cosmo: Optional[float] = None
    T_inner: float = np.nan
    T_outer: float = np.nan
    T_cosmo: float = np.nan
    Phi_outer: float = np.nan   # electric potential at outer BH horizon
    Phi_cosmo: float = np.nan   # electric potential at cosmo horizon
    S_inner: float = np.nan
    S_outer: float = np.nan
    S_cosmo: float = np.nan
    S_Lambda: float = np.nan
    Delta_total: float = np.nan   # S_Lambda - (S_outer + S_cosmo) [two-horizon deficit]
    admissible: bool = False
    n_real_horizons: int = 0

    def __post_init__(self):
        self._compute()

    def _compute(self):
        self.S_Lambda = 3.0 * PI / self.Lambda if self.Lambda > 0 else np.nan

        r_minus, r_inner, r_outer, r_cosmo = _solve_rnds_quartic(
            self.M, self.Q, self.Lambda
        )

        if r_minus is None:
            self.admissible = False
            return

        if r_minus >= 0 or r_inner <= 0 or r_outer <= 0 or r_cosmo <= 0:
            self.admissible = False
            return

        if not (r_inner < r_outer < r_cosmo):
            self.admissible = False
            return

        self.r_minus = r_minus
        self.r_inner = r_inner
        self.r_outer = r_outer
        self.r_cosmo = r_cosmo
        self.n_real_horizons = 3

        M, Q, lam = self.M, self.Q, self.Lambda

        # Surface gravities and temperatures
        # κ_i = (1/2)|f'(r_i)|, T_i = κ_i / (2π)
        # For outer BH: f'(r_outer) > 0, so T_outer = f'(r_outer)/(4π)
        # For cosmo:    f'(r_cosmo) < 0, so T_cosmo = |f'(r_cosmo)|/(4π)
        # For inner:    f'(r_inner) < 0, so T_inner = |f'(r_inner)|/(4π)

        fp_inner = _rnds_fprime(r_inner, M, Q, lam)
        fp_outer = _rnds_fprime(r_outer, M, Q, lam)
        fp_cosmo = _rnds_fprime(r_cosmo, M, Q, lam)

        self.T_inner = abs(fp_inner) / (4.0 * PI) if not np.isnan(fp_inner) else np.nan
        self.T_outer = fp_outer / (4.0 * PI) if fp_outer > 0 else np.nan
        self.T_cosmo = abs(fp_cosmo) / (4.0 * PI) if not np.isnan(fp_cosmo) else np.nan

        # Electric potentials: Phi_i = Q / r_i  (in natural units)
        self.Phi_outer = Q / r_outer
        self.Phi_cosmo = Q / r_cosmo

        # Entropies
        self.S_inner = PI * r_inner**2
        self.S_outer = PI * r_outer**2
        self.S_cosmo = PI * r_cosmo**2

        # Two-horizon entropy deficit (outer + cosmo only, analogous to SdS)
        self.Delta_total = self.S_Lambda - (self.S_outer + self.S_cosmo)

        # Admissibility: all temperatures positive, horizons separated
        self.admissible = (
            self.T_outer > 0 and self.T_cosmo > 0
            and r_inner < r_outer < r_cosmo
        )

    def is_valid(self) -> bool:
        return (
            self.admissible
            and self.T_outer > 0
            and self.T_cosmo > 0
            and self.S_outer > 0
            and self.S_cosmo > 0
        )

    def vieta_check(self) -> dict:
        """
        Verify Vieta identities for the quartic.
        Returns residuals (should be ~0 if solve was correct).
        """
        if not self.admissible:
            return {"admissible": False}
        r = [self.r_minus, self.r_inner, self.r_outer, self.r_cosmo]
        lam = self.Lambda
        M, Q = self.M, self.Q
        e1 = sum(r)                              # should be 0
        e2 = sum(r[i]*r[j] for i in range(4) for j in range(i+1,4))  # should be -3/Lambda
        e3 = sum(r[i]*r[j]*r[k] for i in range(4) for j in range(i+1,4) for k in range(j+1,4))  # should be -6M/Lambda
        e4 = r[0]*r[1]*r[2]*r[3]               # should be -3Q^2/Lambda
        return {
            "e1_residual": abs(e1),                      # target: 0
            "e2_residual": abs(e2 - (-3.0/lam)),         # target: 0
            "e3_residual": abs(e3 - (-6.0*M/lam)),       # target: 0
            "e4_residual": abs(e4 - (-3.0*Q**2/lam)),    # target: 0
        }

    def as_dict(self) -> dict:
        return {
            "M": self.M,
            "Q": self.Q,
            "Lambda": self.Lambda,
            "r_inner": self.r_inner,
            "r_outer": self.r_outer,
            "r_cosmo": self.r_cosmo,
            "T_inner": self.T_inner,
            "T_outer": self.T_outer,
            "T_cosmo": self.T_cosmo,
            "S_outer": self.S_outer,
            "S_cosmo": self.S_cosmo,
            "S_Lambda": self.S_Lambda,
            "Delta_total": self.Delta_total,
            "admissible": self.admissible,
        }


# ---------------------------------------------------------------------------
# Convenience: parameter space scans
# ---------------------------------------------------------------------------

def rnds_extremal_charge(M: float, lam: float) -> float:
    """
    Estimate the maximum charge for given M, Lambda such that
    outer and inner BH horizons do not coincide (BH extremal limit).
    Uses a numerical search.
    Returns Q_extreme or nan if not found.
    """
    # For pure RN (Lambda=0): Q_extreme = M.
    # For RNdS, slightly less. Use bisection.
    Q_lo, Q_hi = 0.0, M * 1.5  # rough upper bound

    def n_real_positive_roots(Q):
        r = _solve_rnds_quartic(M, Q, lam)
        if r[0] is None:
            return 0
        # Count distinct real positive roots
        roots = [ri for ri in r if ri is not None and ri > 0]
        return len(roots)

    # Find Q where we transition from 3 to 2 positive roots
    for _ in range(50):
        Q_mid = (Q_lo + Q_hi) / 2
        n = n_real_positive_roots(Q_mid)
        if n >= 3:
            Q_lo = Q_mid
        else:
            Q_hi = Q_mid
        if Q_hi - Q_lo < 1e-8:
            break

    result = (Q_lo + Q_hi) / 2
    # Verify
    if not _rnds_admissible(M, result * 0.99, lam):
        return np.nan
    return result * 0.99  # slightly inside extremal


def rnds_scan_mq(
    n_M: int = 10, n_Q: int = 10, lam: float = 1.0,
    M_frac_max: float = 0.9,
) -> list:
    """
    Scan over (M, Q) grid at fixed Lambda.
    Returns list of admissible RNdSState objects.
    """
    M_nariai_sds = 1.0 / (3.0 * np.sqrt(lam))
    states = []
    for M in np.linspace(0.05 * M_nariai_sds, M_frac_max * M_nariai_sds, n_M):
        Q_ext = rnds_extremal_charge(M, lam)
        if np.isnan(Q_ext) or Q_ext <= 0:
            Q_ext = M * 0.8  # fallback
        for Q in np.linspace(0.0, 0.85 * Q_ext, n_Q):
            s = RNdSState(M, Q, lam)
            if s.is_valid():
                states.append(s)
    return states
