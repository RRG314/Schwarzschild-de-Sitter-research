"""
SdS spacetime physics: exact algebraic relations, horizon structure,
effective potential, and thermodynamic observables.

All formulas are derived from the Vieta relations of the horizon cubic.
Units: G = c = hbar = k_B = 1.
"""

import numpy as np
from dataclasses import dataclass
from typing import Optional


@dataclass
class SdSState:
    x: float        # r_b / r_c, the horizon ratio
    lam: float      # cosmological constant Lambda
    r_b: float      # black hole horizon radius
    r_c: float      # cosmological horizon radius
    r_lam: float    # de Sitter radius sqrt(3/Lambda)
    M: float        # mass parameter
    T_b: float      # Hawking temperature at BH horizon
    T_c: float      # Hawking temperature at cosm. horizon
    S_b: float      # BH entropy
    S_c: float      # cosm. entropy
    S_lam: float    # pure dS entropy 3*pi/Lambda
    Delta: float    # entropy deficit sqrt(S_b * S_c)
    eta_C: float    # Carnot efficiency (T_b - T_c) / T_b


def sds_from_x(x: float, lam: float) -> Optional[SdSState]:
    """
    Construct a SdS state from (x, Lambda).
    x = r_b / r_c in (0, 1).
    Returns None if parameters are outside the sub-extremal range.
    """
    if not (0.001 < x < 0.999):
        return None
    if lam <= 0:
        return None

    # From Eisenstein constraint: r_b^2 + r_b*r_c + r_c^2 = 3/Lambda
    # With r_b = x * r_c: r_c^2 (x^2 + x + 1) = 3/Lambda
    denom = x * x + x + 1.0
    r_c = np.sqrt(3.0 / (lam * denom))
    r_b = x * r_c
    r_lam = np.sqrt(3.0 / lam)

    # Mass from Vieta: r_b * r_c * (r_b + r_c) = 6M/Lambda
    # r_- = -(r_b + r_c), r_- * r_b * r_c = -6M/Lambda
    M = r_b * r_c * (r_b + r_c) * lam / 6.0

    # Temperatures
    T_b = (1.0 - lam * r_b**2) / (4.0 * np.pi * r_b)
    T_c = (lam * r_c**2 - 1.0) / (4.0 * np.pi * r_c)

    # Entropies
    S_b = np.pi * r_b**2
    S_c = np.pi * r_c**2
    S_lam = 3.0 * np.pi / lam

    Delta = np.sqrt(S_b * S_c)

    # Carnot efficiency
    eta_C = (T_b - T_c) / T_b if T_b > 0 else 0.0

    return SdSState(
        x=x, lam=lam, r_b=r_b, r_c=r_c, r_lam=r_lam,
        M=M, T_b=T_b, T_c=T_c,
        S_b=S_b, S_c=S_c, S_lam=S_lam, Delta=Delta, eta_C=eta_C
    )


def sds_effective_potential(r: np.ndarray, state: SdSState, l: int = 2, spin: int = 0) -> np.ndarray:
    """
    SdS effective potential for spin-s perturbations.
    V(r) = f(r) * [l(l+1)/r^2 + (1-s^2) * f'(r)/r]

    For spin=0 (scalar): V = f(r) * [l(l+1)/r^2 + f'(r)/r]
    For spin=1 (vector): V = f(r) * l(l+1)/r^2
    For spin=2 (tensor/gravitational Regge-Wheeler): slightly different,
      but we use the scalar formula as our primary test case.

    f(r) = 1 - 2M/r - Lambda*r^2/3
    f'(r) = 2M/r^2 - 2*Lambda*r/3
    """
    M = state.M
    lam = state.lam

    f = 1.0 - 2.0 * M / r - lam * r**2 / 3.0
    fp = 2.0 * M / r**2 - 2.0 * lam * r / 3.0

    angular = l * (l + 1) / r**2
    s2 = spin * spin

    V = f * (angular + (1.0 - s2) * fp / r)
    return V


def find_potential_maximum(state: SdSState, l: int = 2, spin: int = 0,
                           n_search: int = 2000) -> tuple[float, float]:
    """
    Find the maximum of V(r) in the static region (r_b, r_c).
    Returns (r_max, V_max).
    Uses a dense grid search followed by golden-section refinement.
    """
    r_b = state.r_b
    r_c = state.r_c

    # Dense grid search
    r_grid = np.linspace(r_b * 1.001, r_c * 0.999, n_search)
    V_grid = sds_effective_potential(r_grid, state, l=l, spin=spin)
    idx_max = np.argmax(V_grid)
    r_lo = r_grid[max(0, idx_max - 1)]
    r_hi = r_grid[min(len(r_grid) - 1, idx_max + 1)]

    # Golden-section refinement
    phi = (1 + np.sqrt(5)) / 2
    resphi = 2 - phi
    tol = 1e-12 * r_c

    a, b = r_lo, r_hi
    x1 = a + resphi * (b - a)
    x2 = b - resphi * (b - a)
    f1 = -sds_effective_potential(np.array([x1]), state, l=l, spin=spin)[0]
    f2 = -sds_effective_potential(np.array([x2]), state, l=l, spin=spin)[0]

    for _ in range(200):
        if abs(b - a) < tol:
            break
        if f1 < f2:
            b = x2
            x2 = x1
            f2 = f1
            x1 = a + resphi * (b - a)
            f1 = -sds_effective_potential(np.array([x1]), state, l=l, spin=spin)[0]
        else:
            a = x1
            x1 = x2
            f1 = f2
            x2 = b - resphi * (b - a)
            f2 = -sds_effective_potential(np.array([x2]), state, l=l, spin=spin)[0]

    r_max = (a + b) / 2.0
    V_max = sds_effective_potential(np.array([r_max]), state, l=l, spin=spin)[0]
    return r_max, V_max


def potential_second_derivative(r_max: float, state: SdSState, l: int = 2,
                                spin: int = 0, h: float = None) -> float:
    """
    Numerical second derivative of V at r_max using 5-point stencil.
    """
    if h is None:
        h = r_max * 1e-5
    r = np.array([r_max - 2*h, r_max - h, r_max, r_max + h, r_max + 2*h])
    V = sds_effective_potential(r, state, l=l, spin=spin)
    # 5-point stencil: (-V[-2] + 16V[-1] - 30V[0] + 16V[1] - V[2]) / (12 h^2)
    d2V = (-V[0] + 16*V[1] - 30*V[2] + 16*V[3] - V[4]) / (12.0 * h**2)
    return d2V


def potential_derivatives_higher(r_max: float, state: SdSState, l: int = 2,
                                  spin: int = 0, h: float = None) -> dict:
    """
    Compute V and its derivatives at r_max up to 6th order.
    Used for higher-order WKB corrections.
    """
    if h is None:
        h = r_max * 5e-5

    # Sample at 7 points for up to 6th derivative
    pts = np.array([r_max + k * h for k in range(-3, 4)])
    V = sds_effective_potential(pts, state, l=l, spin=spin)

    V0 = V[3]
    # 1st: antisymmetric, exact for odd
    d1V = (-V[0] + 9*V[1] - 45*V[2] + 45*V[4] - 9*V[5] + V[6]) / (60.0 * h)
    # 2nd: symmetric
    d2V = (2*V[0] - 27*V[1] + 270*V[2] - 490*V[3] + 270*V[4] - 27*V[5] + 2*V[6]) / (180.0 * h**2)
    # 3rd
    d3V = (-V[0] + 8*V[1] - 13*V[2] + 13*V[4] - 8*V[5] + V[6]) / (8.0 * h**3)
    # 4th
    d4V = (V[0] - 4*V[1] + 5*V[2] - 2*V[3] - 2*V[4] + 5*V[5] - 4*V[6] + 0) / (h**4)
    # Use simpler 4th-order central diff
    d4V = (V[0] - 4*V[1] + 6*V[2] - 4*V[3] + V[4]) / h**4  # 5-point, at shifted index
    # recompute properly at center
    r5 = np.array([r_max + k * h for k in range(-2, 3)])
    V5 = sds_effective_potential(r5, state, l=l, spin=spin)
    d4V = (V5[0] - 4*V5[1] + 6*V5[2] - 4*V5[3] + V5[4]) / h**4
    d6V = (V[0] - 6*V[1] + 15*V[2] - 20*V[3] + 15*V[4] - 6*V[5] + V[6]) / h**6

    return {
        'V0': V0, 'd1V': d1V, 'd2V': d2V, 'd3V': d3V,
        'd4V': d4V, 'd6V': d6V
    }


def verify_eisenstein(state: SdSState) -> float:
    """Return residual of r_b^2 + r_b*r_c + r_c^2 - 3/Lambda."""
    return abs(state.r_b**2 + state.r_b*state.r_c + state.r_c**2 - 3.0/state.lam)


def verify_entropy_identity(state: SdSState) -> float:
    """Return residual of S_Lambda - S_b - S_c - sqrt(S_b * S_c)."""
    return abs(state.S_lam - state.S_b - state.S_c - np.sqrt(state.S_b * state.S_c))
