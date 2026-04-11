"""
recursion_models.py
===================
Iterated maps on the Eisenstein arc.

Analogy: think of each horizon state (u, v) as the coordinates of a ball
sitting somewhere on an ellipse.  A recursion is a rule that moves the ball
to a new spot on the same ellipse.  We iterate the rule many times and ask:
  - Does the ball settle into a fixed point?
  - Does it bounce forever between a few spots (cycle)?
  - Does it wander chaotically?
  - What does the resulting "orbit" look like geometrically?

Three families of maps are implemented:

  1. SymmetricPowerMap   : T_lambda(u, v) = normalize(u^lambda, v^lambda)
  2. CoupledSymmetricMap : T_{lambda,eps}(u, v) = normalize(u^lambda + eps*v,
                                                             v^lambda + eps*u)
  3. CoupledAsymmetricMap: T(u, v) = normalize(u^lambda + eps*v^beta,
                                               v^lambda + delta*u^gamma)

All maps re-project onto the unit Eisenstein ellipse after each step.
"""

import numpy as np
from typing import Callable
from .state_space import normalize_to_ellipse, verify_constraint, x_to_uv


# ---------------------------------------------------------------------------
# Map classes
# ---------------------------------------------------------------------------

class SymmetricPowerMap:
    """
    T_lambda(u, v) = normalize(u^lambda, v^lambda).

    For lambda=1 this is the identity map.
    For lambda > 1, high-v (cosmological) states get amplified relative to
    low-v states (since v > u), so the orbit drifts toward the pure-dS limit.
    For 0 < lambda < 1 the inverse happens.
    """
    def __init__(self, lam: float):
        if lam <= 0:
            raise ValueError("lambda must be positive")
        self.lam = lam
        self.name = f"Sym(λ={lam:.3f})"

    def __call__(self, u: float, v: float) -> tuple[float, float]:
        EPS = 1e-9
        a = max(u**self.lam, EPS)
        b = max(v**self.lam, EPS)
        return normalize_to_ellipse(a, b)

    def fixed_points(self) -> list[tuple[float, float]]:
        """
        Fixed points satisfy normalize(u^lambda, v^lambda) = (u, v).
        This means u^lambda / v^lambda = u / v, i.e., (u/v)^(lambda-1) = 1.
        For lambda != 1: only x=1 (Nariai, excluded) or x -> boundary.
        For lambda == 1: every point is a fixed point.
        """
        if abs(self.lam - 1.0) < 1e-12:
            return []  # every point fixed
        # Only solution: u/v = 1, i.e., x=1 (Nariai, boundary — excluded)
        return []


class CoupledSymmetricMap:
    """
    T_{lambda, eps}(u, v) = normalize(u^lambda + eps*v, v^lambda + eps*u).

    The coupling eps mixes the two horizon coordinates.  For eps=0 this
    reduces to SymmetricPowerMap.  For large eps the mixing dominates.
    """
    def __init__(self, lam: float, eps: float):
        self.lam = lam
        self.eps = eps
        self.name = f"CoupSym(λ={lam:.3f},ε={eps:.3f})"

    def __call__(self, u: float, v: float) -> tuple[float, float]:
        a = u**self.lam + self.eps * v
        b = v**self.lam + self.eps * u
        if a <= 0 or b <= 0:
            # Degenerate — return current point (absorbing boundary)
            return u, v
        return normalize_to_ellipse(a, b)


class CoupledAsymmetricMap:
    """
    T(u, v) = normalize(u^lambda + eps*v^beta, v^lambda + delta*u^gamma).

    Fully general coupling.  For eps=delta and beta=gamma=1 this reduces
    to CoupledSymmetricMap.
    """
    def __init__(self, lam: float, eps: float, beta: float,
                 delta: float, gamma: float):
        self.lam = lam
        self.eps = eps
        self.beta = beta
        self.delta = delta
        self.gamma = gamma
        self.name = f"CoupAsym(λ={lam:.2f},ε={eps:.2f},β={beta:.2f},δ={delta:.2f},γ={gamma:.2f})"

    def __call__(self, u: float, v: float) -> tuple[float, float]:
        a = u**self.lam + self.eps * (v**self.beta if v > 0 else 0.0)
        b = v**self.lam + self.delta * (u**self.gamma if u > 0 else 0.0)
        if a <= 0 or b <= 0:
            return u, v
        return normalize_to_ellipse(a, b)


# ---------------------------------------------------------------------------
# Orbit integration
# ---------------------------------------------------------------------------

def iterate(
    f: Callable,
    u0: float,
    v0: float,
    n_steps: int,
    clip_boundary: float = 1e-6,
) -> np.ndarray:
    """
    Iterate map f starting from (u0, v0) for n_steps steps.

    Returns array of shape (n_steps+1, 2) — includes the initial point.
    Points that drift to the boundary (x < clip_boundary or x > 1-clip_boundary)
    are clipped to prevent numerical blow-up.
    """
    trajectory = np.zeros((n_steps + 1, 2))
    trajectory[0] = [u0, v0]
    u, v = u0, v0
    for i in range(1, n_steps + 1):
        u, v = f(u, v)
        # Clip to physical interior
        x = u / v
        if x < clip_boundary:
            u, v = x_to_uv(clip_boundary)
        elif x > 1.0 - clip_boundary:
            u, v = x_to_uv(1.0 - clip_boundary)
        trajectory[i] = [u, v]
    return trajectory


def find_attractor(
    f: Callable,
    u0: float,
    v0: float,
    n_warmup: int = 5000,
    n_collect: int = 2000,
    tol: float = 1e-9,
) -> dict:
    """
    Run the map for n_warmup steps (discard), then collect n_collect steps.

    Returns a dict with:
      attractor_type : 'fixed', 'cycle', 'quasi-periodic', 'chaotic'
      period         : cycle length (if cycle) or None
      mean_x         : mean x = u/v in the attractor
      std_x          : std of x in the attractor
      orbit          : collected orbit array (n_collect, 2)
    """
    # Warm up (using iterate for safe boundary clipping)
    warmup_traj = iterate(f, u0, v0, n_warmup)
    u, v = warmup_traj[-1]

    # Collect
    orbit = iterate(f, u, v, n_collect)
    xs = orbit[:, 0] / orbit[:, 1]

    # Classify
    std_x = np.std(xs)
    mean_x = np.mean(xs)

    if std_x < tol:
        atype = "fixed"
        period = 1
    else:
        # Check for cycles up to period 20
        period = _detect_period(orbit, max_period=20, tol=1e-7)
        if period is not None:
            atype = "cycle"
        elif std_x < 1e-4:
            atype = "quasi-periodic"
        else:
            atype = "chaotic"

    return {
        "attractor_type": atype,
        "period": period,
        "mean_x": float(mean_x),
        "std_x": float(std_x),
        "orbit": orbit,
        "final_u": float(u),
        "final_v": float(v),
    }


def _detect_period(orbit: np.ndarray, max_period: int, tol: float) -> int | None:
    """
    Check if the orbit is eventually periodic with period p in {1, ..., max_period}.
    """
    n = len(orbit)
    tail = orbit[n // 2:]  # use second half
    for p in range(1, max_period + 1):
        if len(tail) < 2 * p:
            continue
        diff = np.max(np.abs(tail[:-p] - tail[p:]))
        if diff < tol:
            return p
    return None


# ---------------------------------------------------------------------------
# Convenience: build map from parameter dict
# ---------------------------------------------------------------------------

def build_map(kind: str, **kwargs) -> Callable:
    """
    Factory for recursion maps.

    kind: 'symmetric' | 'coupled_sym' | 'coupled_asym'
    kwargs passed to respective constructor.
    """
    if kind == "symmetric":
        return SymmetricPowerMap(lam=kwargs["lam"])
    elif kind == "coupled_sym":
        return CoupledSymmetricMap(lam=kwargs["lam"], eps=kwargs["eps"])
    elif kind == "coupled_asym":
        return CoupledAsymmetricMap(
            lam=kwargs["lam"],
            eps=kwargs["eps"],
            beta=kwargs.get("beta", 1.0),
            delta=kwargs.get("delta", 0.0),
            gamma=kwargs.get("gamma", 1.0),
        )
    else:
        raise ValueError(f"Unknown map kind: {kind}")
