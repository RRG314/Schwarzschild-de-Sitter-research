"""
state_space.py
==============
Schwarzschild-de Sitter Eisenstein state space.

Think of SdS spacetime as having two concentric fences around a point mass:
  - r_b: the black hole horizon (inner fence — light can't escape inward)
  - r_c: the cosmological horizon (outer fence — light can't escape outward)

The Eisenstein constraint is an exact algebraic relation between these radii:
  r_b^2 + r_b*r_c + r_c^2 = 3/Lambda

We rescale to dimensionless Eisenstein coordinates:
  u = r_b / r_Lambda,  v = r_c / r_Lambda,  r_Lambda = sqrt(3/Lambda)

These satisfy the unit Eisenstein ellipse:  u^2 + u*v + v^2 = 1

The full SdS phase space is the arc of this ellipse with 0 < u < v < 1,
i.e., x = u/v = r_b/r_c in (0, 1).
"""

import numpy as np
from dataclasses import dataclass


LAMBDA = 1.0   # cosmological constant; all formulas assume Lambda=1 unless noted
PI = np.pi


# ---------------------------------------------------------------------------
# Core parameterisation
# ---------------------------------------------------------------------------

def x_to_uv(x: float) -> tuple[float, float]:
    """
    Convert ratio x = r_b/r_c in (0,1) to Eisenstein coordinates (u,v).

    u = x / sqrt(x^2 + x + 1)
    v = 1 / sqrt(x^2 + x + 1)

    The factor sqrt(x^2+x+1) is the Eisenstein norm of (x,1).
    """
    n = np.sqrt(x**2 + x + 1.0)
    return x / n, 1.0 / n


def uv_to_x(u: float, v: float) -> float:
    """Return ratio x = u/v (= r_b/r_c) from Eisenstein coordinates."""
    return u / v


def eisenstein_norm_sq(u: float, v: float) -> float:
    """N(u,v) = u^2 + u*v + v^2.  Should equal 1 on the unit ellipse."""
    return u**2 + u * v + v**2


def normalize_to_ellipse(a: float, b: float) -> tuple[float, float]:
    """
    Project point (a, b) back onto the unit Eisenstein ellipse.

    If N(a,b) = a^2 + ab + b^2 = c^2, then (a/c, b/c) satisfies N=1.
    Requires a > 0 and b > 0.
    """
    if a <= 0 or b <= 0:
        raise ValueError(f"Both coordinates must be positive; got ({a}, {b})")
    c = np.sqrt(eisenstein_norm_sq(a, b))
    return a / c, b / c


# ---------------------------------------------------------------------------
# Physical observables from (u, v)  [with Lambda = 1]
# ---------------------------------------------------------------------------

def radii(u: float, v: float, lam: float = LAMBDA) -> tuple[float, float]:
    """Return (r_b, r_c) from Eisenstein coordinates."""
    r_lam = np.sqrt(3.0 / lam)
    return u * r_lam, v * r_lam


def entropies(u: float, v: float, lam: float = LAMBDA) -> tuple[float, float]:
    """S_b = pi r_b^2,  S_c = pi r_c^2."""
    r_b, r_c = radii(u, v, lam)
    return PI * r_b**2, PI * r_c**2


def entropy_deficit(u: float, v: float, lam: float = LAMBDA) -> float:
    """
    Delta = sqrt(S_b * S_c) = pi * r_b * r_c.

    The SdS entropy identity:  S_dS = S_b + S_c + Delta
    where S_dS = 3*pi/Lambda is the pure-dS entropy.
    """
    r_b, r_c = radii(u, v, lam)
    return PI * r_b * r_c


def temperatures(u: float, v: float, lam: float = LAMBDA) -> tuple[float, float]:
    """
    Exact SdS horizon temperatures (natural units, G=hbar=c=kB=1).

    T_b = sqrt(Lambda)/(4*pi*sqrt(3)) * (1-x)(2x+1) / (x * sqrt(x^2+x+1))
    T_c = sqrt(Lambda)/(4*pi*sqrt(3)) * (1-x)(x+2)  /     sqrt(x^2+x+1)

    where x = u/v = r_b/r_c.
    """
    x = uv_to_x(u, v)
    prefactor = np.sqrt(lam) / (4.0 * PI * np.sqrt(3.0))
    denom = np.sqrt(x**2 + x + 1.0)
    T_b = prefactor * (1.0 - x) * (2.0 * x + 1.0) / (x * denom)
    T_c = prefactor * (1.0 - x) * (x + 2.0) / denom
    return T_b, T_c


def temperature_ratio(u: float, v: float) -> float:
    """T_c / T_b = x(2+x)/(1+2x),  x = u/v."""
    x = uv_to_x(u, v)
    return x * (2.0 + x) / (1.0 + 2.0 * x)


def carnot_efficiency(u: float, v: float) -> float:
    """
    Carnot efficiency eta_C = 1 - T_c/T_b = (1-x^2)/(1+2x).

    This equals the fractional deficit slope: partial(Delta)/partial(S_c) = -eta_C.
    """
    x = uv_to_x(u, v)
    return (1.0 - x**2) / (1.0 + 2.0 * x)


def mass(u: float, v: float, lam: float = LAMBDA) -> float:
    """
    SdS mass from Vieta:  M = r_b * r_c * (r_b + r_c) / 6.

    In Eisenstein coords (Lambda=1):  M = sqrt(3)*u*v*(u+v)/2.
    """
    r_b, r_c = radii(u, v, lam)
    return r_b * r_c * (r_b + r_c) / 6.0


def nariai_mass(lam: float = LAMBDA) -> float:
    """Maximum mass M_N = 1/(3*sqrt(Lambda)); Nariai limit where r_b = r_c."""
    return 1.0 / (3.0 * np.sqrt(lam))


def j_invariant(u: float, v: float) -> float:
    """
    Classical j-invariant of the SdS cubic:

      j = 6912 * (x^2 + x + 1)^3 / [(1-x)^2 (x+2)^2 (2x+1)^2]
        = 1728 / (1 - 9*Lambda*M^2)

    At M=0 (pure dS): j = 1728 (CM by Z[i], Gaussian integers).
    At Nariai: j -> infinity.
    """
    x = uv_to_x(u, v)
    numerator = 6912.0 * (x**2 + x + 1.0)**3
    denominator = ((1.0 - x) * (x + 2.0) * (2.0 * x + 1.0))**2
    return numerator / denominator


# ---------------------------------------------------------------------------
# Phase-space utilities
# ---------------------------------------------------------------------------

def sample_arc(n: int = 200) -> np.ndarray:
    """
    Sample n evenly-spaced points along the SdS arc on the Eisenstein ellipse.

    x = r_b/r_c ranges over (0, 1); endpoints are excluded (degenerate cases).
    Returns array of shape (n, 2) with columns (u, v).
    """
    xs = np.linspace(1e-4, 1.0 - 1e-4, n)
    pts = np.array([x_to_uv(x) for x in xs])
    return pts


def arc_angle_deg(u: float, v: float) -> float:
    """
    Parametric angle (degrees) of (u, v) in the eigenbasis of the Eisenstein form.

    The SdS arc spans exactly 30 degrees (pi/6 radians).
    """
    # Rotate to principal axes: P = (u+v)/sqrt(2), Q = (u-v)/sqrt(2) - scaled
    # Use the fact that Eisenstein form diagonalises as P^2 + Q^2/3 = 1
    P = (u + v) / np.sqrt(2.0)
    Q = (u - v) / np.sqrt(2.0)
    theta_rad = np.arctan2(Q, P * np.sqrt(3.0))
    return np.degrees(theta_rad)


# ---------------------------------------------------------------------------
# Validation
# ---------------------------------------------------------------------------

def verify_constraint(u: float, v: float, tol: float = 1e-10) -> bool:
    """Check that u^2 + u*v + v^2 = 1 to within tol."""
    return abs(eisenstein_norm_sq(u, v) - 1.0) < tol


def check_physical(u: float, v: float) -> dict:
    """
    Return a dict of physical checks for a point (u, v).
    """
    x = uv_to_x(u, v)
    on_ellipse = verify_constraint(u, v)
    physical = 0.0 < x < 1.0 and on_ellipse
    return {
        "x": x,
        "on_ellipse": on_ellipse,
        "physical": physical,
        "u": u,
        "v": v,
    }
