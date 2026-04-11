"""
stability_analysis.py
=====================
Jacobian-based stability and bifurcation analysis.

Analogy: the Jacobian of a map at a fixed point is like measuring how
quickly nearby points diverge.  If all eigenvalues are less than 1 in
absolute value, the fixed point is stable (nearby orbits converge to it).
If any eigenvalue > 1, it's unstable.

We also compute Lyapunov exponents to quantify orbit divergence over time.
"""

import numpy as np
from typing import Callable
from .state_space import normalize_to_ellipse, x_to_uv


# ---------------------------------------------------------------------------
# Jacobian via finite differences
# ---------------------------------------------------------------------------

def numerical_jacobian(
    f: Callable,
    u: float,
    v: float,
    h: float = 1e-6,
) -> np.ndarray:
    """
    Compute the 2x2 Jacobian of f at (u, v) using central differences.

    J[i,j] = d f_i / d x_j
    """
    x0 = np.array([u, v])
    J = np.zeros((2, 2))
    for j in range(2):
        x_plus = x0.copy(); x_plus[j] += h
        x_minus = x0.copy(); x_minus[j] -= h

        # Clip to physical domain
        for x in [x_plus, x_minus]:
            if x[0] < 1e-8: x[0] = 1e-8
            if x[1] < 1e-8: x[1] = 1e-8

        fp = np.array(f(x_plus[0], x_plus[1]))
        fm = np.array(f(x_minus[0], x_minus[1]))
        J[:, j] = (fp - fm) / (2 * h)
    return J


def jacobian_spectrum(J: np.ndarray) -> dict:
    """
    Eigenvalues and stability classification of a 2x2 Jacobian.
    """
    eigenvalues = np.linalg.eigvals(J)
    spectral_radius = np.max(np.abs(eigenvalues))
    stable = spectral_radius < 1.0 - 1e-10
    marginal = abs(spectral_radius - 1.0) < 1e-6
    return {
        "eigenvalues": eigenvalues,
        "spectral_radius": float(spectral_radius),
        "stable": bool(stable),
        "marginal": bool(marginal),
        "unstable": bool(spectral_radius > 1.0 + 1e-10),
    }


# ---------------------------------------------------------------------------
# Fixed point search
# ---------------------------------------------------------------------------

def find_fixed_points_grid(
    f: Callable,
    n_grid: int = 50,
    tol: float = 1e-8,
    n_iter: int = 1000,
) -> list[dict]:
    """
    Search for fixed points by running the map from a grid of initial conditions.

    For each starting x in a grid, iterate n_iter times and check if the
    orbit has converged.  Returns a deduplicated list of fixed points found.
    """
    xs_grid = np.linspace(0.01, 0.99, n_grid)
    fixed_points = []
    seen = []

    for x0 in xs_grid:
        u, v = x_to_uv(x0)
        for _ in range(n_iter):
            u_new, v_new = f(u, v)
            if abs(u_new - u) + abs(v_new - v) < tol:
                break
            u, v = u_new, v_new

        # Check convergence
        u_next, v_next = f(u, v)
        dist = abs(u_next - u) + abs(v_next - v)
        if dist < tol * 10:
            x_fp = u / v
            # Deduplicate
            duplicate = any(abs(x_fp - s) < 1e-4 for s in seen)
            if not duplicate:
                seen.append(x_fp)
                J = numerical_jacobian(f, u, v)
                spec = jacobian_spectrum(J)
                fixed_points.append({
                    "u": float(u),
                    "v": float(v),
                    "x": float(x_fp),
                    "jacobian": J,
                    **spec,
                })

    return fixed_points


# ---------------------------------------------------------------------------
# Lyapunov exponents
# ---------------------------------------------------------------------------

def max_lyapunov_exponent(
    f: Callable,
    u0: float,
    v0: float,
    n_steps: int = 5000,
    n_renorm: int = 50,
) -> float:
    """
    Estimate the maximal Lyapunov exponent (MLE) using the standard
    QR reorthogonalization algorithm.

    If MLE > 0: orbit is chaotic.
    If MLE ≈ 0: orbit is on the boundary of stability.
    If MLE < 0: orbit is attracting.
    """
    u, v = u0, v0
    # Initial tangent vector
    Q = np.eye(2)
    log_expansion = 0.0
    count = 0

    step_per_renorm = n_steps // n_renorm

    for block in range(n_renorm):
        for _ in range(step_per_renorm):
            J = numerical_jacobian(f, u, v)
            Q = J @ Q
            u, v = f(u, v)

        # QR decomposition to track stretching
        Q, R = np.linalg.qr(Q)
        log_expansion += np.log(abs(R[0, 0]) + 1e-300)
        count += step_per_renorm

    mle = log_expansion / count
    return float(mle)


def lyapunov_spectrum_along_orbit(
    f: Callable,
    orbit: np.ndarray,
) -> np.ndarray:
    """
    Compute local Lyapunov exponents at each point of the orbit.

    Returns array of shape (N,) with local log-stretching at each step.
    """
    N = len(orbit)
    local_exp = np.zeros(N - 1)
    for i in range(N - 1):
        u, v = orbit[i]
        J = numerical_jacobian(f, u, v)
        sv = np.linalg.svd(J, compute_uv=False)
        local_exp[i] = np.log(sv[0] + 1e-300)
    return local_exp


# ---------------------------------------------------------------------------
# Bifurcation scan
# ---------------------------------------------------------------------------

def bifurcation_scan_lambda(
    map_factory: Callable,
    lam_range: np.ndarray,
    x0: float = 0.3,
    n_warmup: int = 500,
    n_collect: int = 200,
    **kwargs,
) -> dict:
    """
    Scan over lambda values and record attractor x-values.

    Parameters
    ----------
    map_factory : callable that takes lam as first arg and returns a map
    lam_range   : array of lambda values to scan
    x0          : initial x = r_b/r_c
    n_warmup    : transient steps to discard
    n_collect   : steps to record

    Returns
    -------
    dict with 'lam_values' and 'attractor_x' (list of arrays)
    """
    from .state_space import x_to_uv
    from .recursion_models import iterate

    attractor_x = []
    for lam in lam_range:
        f = map_factory(lam, **kwargs)
        u, v = x_to_uv(x0)
        # Warm up
        for _ in range(n_warmup):
            u, v = f(u, v)
        # Collect
        traj = iterate(f, u, v, n_collect)
        xs = traj[:, 0] / traj[:, 1]
        attractor_x.append(xs)

    return {
        "lam_values": lam_range,
        "attractor_x": attractor_x,
    }
