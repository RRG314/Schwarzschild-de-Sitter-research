"""
sds_state.py
============
Full physical state for 4D Schwarzschild-de Sitter spacetime.

Parameters: (M, Lambda) — the two independent physical parameters.
All other quantities are DERIVED from these via exact formulas.

Physical domain: 0 < M < M_Nariai = 1/(3*sqrt(Lambda)), Lambda > 0.

The SdS horizon cubic:
  r^3 - (3/Lambda)*r + (6M/Lambda) = 0
has three real roots for sub-extremal configurations:
  r_- < 0 < r_b < r_c
where r_b = BH horizon, r_c = cosmo horizon.

Units: G = hbar = c = kB = 1.
"""

import numpy as np
from dataclasses import dataclass
from typing import Optional
from numpy.polynomial import polynomial as P


PI = np.pi


# ---------------------------------------------------------------------------
# Horizon solver
# ---------------------------------------------------------------------------

def _solve_sds_cubic(M: float, lam: float) -> tuple[float, float, float]:
    """
    Solve r^3 - (3/Lambda)*r + (6M/Lambda) = 0 for all three real roots.
    Returns (r_minus, r_b, r_c) in ascending order.
    Raises ValueError if the configuration is not sub-extremal.
    """
    # Coefficients for numpy.roots: highest power first
    # r^3 + 0*r^2 + (-3/lam)*r + (6M/lam) = 0
    coeffs = [1.0, 0.0, -3.0 / lam, 6.0 * M / lam]
    roots = np.roots(coeffs)

    # Filter to real roots
    real_roots = sorted(r.real for r in roots if abs(r.imag) < 1e-8 * abs(r.real + 1e-30))

    if len(real_roots) != 3:
        raise ValueError(
            f"SdS cubic does not have 3 real roots for M={M:.6g}, Lambda={lam:.6g}. "
            f"Check sub-extremal condition 9*Lambda*M^2 < 1 "
            f"(current: {9*lam*M**2:.6g})"
        )

    r_minus, r_b, r_c = real_roots

    # Validate
    if r_minus >= 0:
        raise ValueError(f"Expected r_minus < 0, got {r_minus:.6g}")
    if r_b <= 0 or r_c <= 0:
        raise ValueError(f"Expected positive r_b, r_c, got {r_b:.6g}, {r_c:.6g}")
    if r_b >= r_c:
        raise ValueError(f"Expected r_b < r_c, got r_b={r_b:.6g}, r_c={r_c:.6g}")

    return r_minus, r_b, r_c


def _nariai_mass(lam: float) -> float:
    """M_Nariai = 1 / (3 * sqrt(Lambda))."""
    return 1.0 / (3.0 * np.sqrt(lam))


def _is_sub_extremal(M: float, lam: float) -> bool:
    """Check 0 < M < M_Nariai and Lambda > 0."""
    return M > 0 and lam > 0 and 9 * lam * M**2 < 1.0


# ---------------------------------------------------------------------------
# Physical state dataclass
# ---------------------------------------------------------------------------

@dataclass
class SdSState:
    """
    Complete physical state for a 4D SdS configuration.

    Constructed from (M, Lambda). All derived quantities are exact.
    """
    M: float
    Lambda: float

    # Derived (set by __post_init__)
    r_minus: float = 0.0
    r_b: float = 0.0
    r_c: float = 0.0
    T_b: float = 0.0
    T_c: float = 0.0
    S_b: float = 0.0
    S_c: float = 0.0
    S_Lambda: float = 0.0
    Delta: float = 0.0
    x: float = 0.0          # = r_b / r_c
    eta_C: float = 0.0      # Carnot efficiency = 1 - T_c/T_b
    admissible: bool = False

    def __post_init__(self):
        self._compute()

    def _compute(self):
        if not _is_sub_extremal(self.M, self.Lambda):
            self.admissible = False
            return
        try:
            self.r_minus, self.r_b, self.r_c = _solve_sds_cubic(self.M, self.Lambda)
            self.admissible = True
        except ValueError:
            self.admissible = False
            return

        lam = self.Lambda
        rb, rc = self.r_b, self.r_c

        # Temperatures (exact from surface gravity)
        self.T_b = (1.0 - lam * rb**2) / (4.0 * PI * rb)
        self.T_c = (lam * rc**2 - 1.0) / (4.0 * PI * rc)

        # Entropies
        self.S_b = PI * rb**2
        self.S_c = PI * rc**2
        self.S_Lambda = 3.0 * PI / lam
        self.Delta = PI * rb * rc   # = sqrt(S_b * S_c)

        # Ratio and efficiency
        self.x = rb / rc
        self.eta_C = 1.0 - self.T_c / self.T_b

        # Validate signs
        if self.T_b <= 0 or self.T_c <= 0:
            self.admissible = False

    def is_valid(self) -> bool:
        """Full physical admissibility check."""
        if not self.admissible:
            return False
        if self.T_b <= 0 or self.T_c <= 0:
            return False
        if self.S_b <= 0 or self.S_c <= 0:
            return False
        if self.r_b >= self.r_c:
            return False
        return True

    def entropy_identity_residual(self) -> float:
        """
        Should be zero: S_Lambda - (S_b + S_c + Delta).
        Non-zero means numerical error.
        """
        if not self.admissible:
            return np.nan
        return self.S_Lambda - (self.S_b + self.S_c + self.Delta)

    def dDelta_dM(self) -> float:
        """
        ∂Δ/∂M|_Lambda = 1/T_c - 1/T_b.
        EXACTLY DERIVED in sds_entropy_paper.md Proposition 4.2.
        Label: PHYSICALLY MOTIVATED.
        """
        if not self.admissible or self.T_b <= 0 or self.T_c <= 0:
            return np.nan
        return 1.0 / self.T_c - 1.0 / self.T_b

    def dDelta_dLambda(self) -> float:
        """
        ∂Δ/∂Lambda|_M  (numerical, via finite difference).
        Label: NUMERICALLY COMPUTED.
        """
        if not self.admissible:
            return np.nan
        h = self.Lambda * 1e-5
        try:
            s1 = SdSState(self.M, self.Lambda + h)
            s2 = SdSState(self.M, self.Lambda - h)
            if s1.admissible and s2.admissible:
                return (s1.Delta - s2.Delta) / (2 * h)
        except Exception:
            pass
        return np.nan

    def as_dict(self) -> dict:
        return {
            "M": self.M,
            "Lambda": self.Lambda,
            "r_b": self.r_b,
            "r_c": self.r_c,
            "T_b": self.T_b,
            "T_c": self.T_c,
            "S_b": self.S_b,
            "S_c": self.S_c,
            "S_Lambda": self.S_Lambda,
            "Delta": self.Delta,
            "x": self.x,
            "eta_C": self.eta_C,
            "admissible": self.admissible,
        }


# ---------------------------------------------------------------------------
# Convenience constructors
# ---------------------------------------------------------------------------

def sds_from_x(x: float, lam: float) -> SdSState:
    """
    Construct SdSState from x = r_b/r_c ∈ (0,1) and Lambda.

    From Vieta: r_b² + r_b r_c + r_c² = 3/Lambda
    So r_c² (x² + x + 1) = 3/Lambda → r_c = sqrt(3/(Lambda*(x²+x+1)))
    And M = r_b * r_c * (r_b + r_c) / 6.
    """
    if not (0 < x < 1) or lam <= 0:
        raise ValueError(f"Need x ∈ (0,1), Lambda > 0; got x={x}, Lambda={lam}")
    r_c = np.sqrt(3.0 / (lam * (x**2 + x + 1.0)))
    r_b = x * r_c
    M = r_b * r_c * (r_b + r_c) / 6.0
    return SdSState(M, lam)


def sds_scan_x(n: int, lam: float, x_min: float = 0.01, x_max: float = 0.99) -> list:
    """Return a list of SdSState objects scanning x from x_min to x_max."""
    xs = np.linspace(x_min, x_max, n)
    return [sds_from_x(x, lam) for x in xs]


def sds_nariai_approach(lam: float, n_steps: int = 10) -> list:
    """Return states approaching Nariai (x -> 1)."""
    xs = 1.0 - np.geomspace(0.001, 0.5, n_steps)[::-1]
    return [sds_from_x(x, lam) for x in xs if 0 < x < 1]
