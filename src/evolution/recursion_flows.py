"""
recursion_flows.py
==================
All recursive flow families for the spacetime system.

Each flow is clearly labeled:
  [PHYS]   = physically motivated (derived from exact thermodynamic identities)
  [CONV]   = mathematically convenient (preserves structure but not uniquely derived)
  [EXPL]   = exploratory / constructed (free parameters, no physical derivation)

The key upgrade from the horizon-only model: flows now act on the full
physical parameter space (M, Lambda) or (M, Q, Lambda), NOT just on
Eisenstein coordinates (u,v) at fixed Lambda.

This means orbits can explore 2D (SdS) or 3D (RNdS) parameter spaces,
unlike the old model which was constrained to a 1D arc.
"""

import numpy as np
from typing import Callable, Optional
from dataclasses import dataclass

from .sds_state import SdSState, sds_from_x, _is_sub_extremal
from .rnds_state import RNdSState, _rnds_admissible


PI = np.pi


# ---------------------------------------------------------------------------
# SdS flows: state = (M, Lambda)
# ---------------------------------------------------------------------------

class SdS_M_GradientFlow:
    """
    [PHYS] Gradient descent on entropy deficit with respect to M, fixed Lambda.

    Update rule:
      M_{d+1} = M_d - step * (∂Δ/∂M) = M_d - step * (1/T_c - 1/T_b)

    Derivation: ∂Δ/∂M|_Lambda = 1/T_c - 1/T_b  (Prop 4.2, sds_entropy_paper.md)

    Since 1/T_c > 1/T_b for sub-extremal SdS (T_c < T_b), this derivative is positive.
    Gradient DESCENT on Δ means dM/dt < 0 (mass decreases toward 0, pure dS).

    Physical interpretation: the system relaxes toward pure de Sitter space.
    Fixed point: M = 0 (boundary, pure dS — not interior).

    If direction='ascent': drives M toward Nariai (mass increases).
    """
    label = "PHYS"
    name = "SdS_M_GradientFlow"

    def __init__(self, step: float = 0.01, direction: str = 'descent', lam: float = 1.0):
        self.step = step
        self.sign = -1.0 if direction == 'descent' else +1.0
        self.lam = lam

    def __call__(self, M: float, lam: float) -> tuple[float, float]:
        s = SdSState(M, lam)
        if not s.is_valid():
            return M, lam
        dM = self.sign * s.dDelta_dM()
        if np.isnan(dM):
            return M, lam
        M_new = M - self.step * dM  # subtract: descent = toward smaller Δ
        # Wait: dDelta_dM = 1/T_c - 1/T_b > 0.
        # Gradient DESCENT on Δ: dM = -step * (∂Δ/∂M) = -step * (1/T_c - 1/T_b) < 0
        # So M_new < M_d (mass decreases). Fixed at sign convention:
        M_new = M + self.sign * self.step * dM
        M_new = max(1e-8, min(M_new, 0.999 / (3.0 * np.sqrt(lam))))
        return M_new, lam


class SdS_Nariai_LinearMap:
    """
    [CONV] Linearly interpolate between current (M, Lambda) and Nariai point.

    M_Nariai = 1/(3*sqrt(Lambda)). At Nariai: r_b = r_c = 1/sqrt(Lambda).

    Update rule:
      M_{d+1} = (1 - alpha) * M_d + alpha * M_Nariai(Lambda_d)
      Lambda_{d+1} = Lambda_d  (Lambda fixed)

    This is a contraction mapping with fixed point at M_Nariai (boundary).
    Not physically derived — it's just a linear interpolation.

    Physical meaning: none specific. It's a "relax toward Nariai" map.
    """
    label = "CONV"
    name = "SdS_Nariai_LinearMap"

    def __init__(self, alpha: float = 0.1):
        self.alpha = np.clip(alpha, 0.0, 1.0)

    def __call__(self, M: float, lam: float) -> tuple[float, float]:
        M_nariai = 1.0 / (3.0 * np.sqrt(lam))
        M_new = (1.0 - self.alpha) * M + self.alpha * M_nariai
        M_new = max(1e-8, min(M_new, 0.9999 * M_nariai))
        return M_new, lam


class SdS_Coupled_MLambda_Flow:
    """
    [EXPL] Coupled flow varying both M and Lambda simultaneously.

    Update rules:
      M_{d+1} = M_d + eps_M * G_M(M_d, Lambda_d)
      Lambda_{d+1} = Lambda_d + eps_Lambda * G_Lambda(M_d, Lambda_d)

    where G_M, G_Lambda are coupling functions. Three variants:

    variant='gradient_both':
      G_M = -(∂Δ/∂M) = -(1/T_c - 1/T_b)   [from exact formula]
      G_Lambda = -(∂Δ/∂Lambda)               [numerical gradient]

    variant='thermalization':
      G_M = T_b - T_c  (drive toward equal temperatures = Nariai)
      G_Lambda = -Lambda * (T_b - T_c) / T_b  (heuristic scaling)

    variant='free':
      G_M = cos(theta), G_Lambda = sin(theta)  (arbitrary direction in param space)
      where theta is a fixed angle parameter

    IMPORTANT: All three variants are EXPLORATORY. The physical motivation is weak.
    The main purpose is to test whether 2D parameter orbits have richer dynamics
    than the 1D Eisenstein arc.
    """
    label = "EXPL"
    name = "SdS_Coupled_MLambda_Flow"

    def __init__(self, eps_M: float = 0.02, eps_Lambda: float = 0.01,
                 variant: str = 'gradient_both', theta: float = 0.5,
                 lam_min: float = 0.1, lam_max: float = 5.0):
        self.eps_M = eps_M
        self.eps_Lambda = eps_Lambda
        self.variant = variant
        self.theta = theta
        self.lam_min = lam_min
        self.lam_max = lam_max

    def __call__(self, M: float, lam: float) -> tuple[float, float]:
        s = SdSState(M, lam)
        if not s.is_valid():
            return M, lam

        if self.variant == 'gradient_both':
            dDelta_dM = s.dDelta_dM()
            dDelta_dLam = s.dDelta_dLambda()
            if np.isnan(dDelta_dM) or np.isnan(dDelta_dLam):
                return M, lam
            M_new = M - self.eps_M * dDelta_dM
            lam_new = lam - self.eps_Lambda * dDelta_dLam

        elif self.variant == 'thermalization':
            dT = s.T_b - s.T_c
            M_new = M + self.eps_M * dT
            lam_new = lam - self.eps_Lambda * lam * dT / (s.T_b + 1e-30)

        elif self.variant == 'free':
            M_new = M + self.eps_M * np.cos(self.theta)
            lam_new = lam + self.eps_Lambda * np.sin(self.theta)

        else:
            return M, lam

        # Clamp to physical region
        M_nariai = 1.0 / (3.0 * np.sqrt(max(lam_new, 1e-6)))
        M_new = max(1e-8, min(M_new, 0.999 * M_nariai))
        lam_new = max(self.lam_min, min(lam_new, self.lam_max))

        # Final admissibility check
        if not _is_sub_extremal(M_new, lam_new):
            return M, lam
        return M_new, lam_new


class SdS_ConstantX_Flow:
    """
    [CONV] Flow that preserves x = r_b/r_c while scaling Lambda.

    Preserving x means M ∝ 1/sqrt(Lambda) (from Vieta: M = r_b r_c (r_b+r_c)/6
    and r_c = sqrt(3/(Lambda*(x²+x+1))), so M ∝ r_c³ ∝ Lambda^{-3/2}).

    Update rule: Lambda_{d+1} = Lambda_d * f_scale, M_{d+1} = M_d * f_scale^{-3/2}

    This traces a path of constant thermodynamic ratio T_c/T_b in (M, Lambda) space.
    Physical meaning: changes the overall energy scale without changing the
    horizon ratio.
    """
    label = "CONV"
    name = "SdS_ConstantX_Flow"

    def __init__(self, scale: float = 1.05):
        self.scale = scale

    def __call__(self, M: float, lam: float) -> tuple[float, float]:
        lam_new = lam * self.scale
        M_new = M * self.scale**(-1.5)
        if not _is_sub_extremal(M_new, lam_new):
            return M, lam
        return M_new, lam_new


# ---------------------------------------------------------------------------
# RNdS flows: state = (M, Q, Lambda)
# ---------------------------------------------------------------------------

class RNdS_MQ_GradientFlow:
    """
    [PHYS] Gradient flow on two-horizon entropy deficit for RNdS, fixed Lambda.

    Two-horizon deficit: Delta = S_Lambda - (S_outer + S_cosmo)

    The gradient components (using first laws for outer horizon):
      ∂(S_outer)/∂M|_{Q,Lambda} = 1/T_outer
      ∂(S_outer)/∂Q|_{M,Lambda} = -Phi_outer/T_outer  (from charged first law)
      ∂(S_cosmo)/∂M|_{Q,Lambda} = -1/T_cosmo  (mass decreases cosmo entropy)
      ∂(S_cosmo)/∂Q|_{M,Lambda} ≈ +Phi_cosmo/T_cosmo  (approximate)

    So:
      ∂Delta/∂M = -(1/T_outer - 1/T_cosmo)   [sign: Delta = S_Lambda - (S_outer+S_cosmo)]
      ∂Delta/∂Q = Phi_outer/T_outer - Phi_cosmo/T_cosmo

    Note on inner horizon: its first law is not well-defined (Cauchy horizon),
    so we only use outer + cosmo thermodynamics.

    LABEL: PHYS for the structure (derived from first laws), EXPL for the specific
    choices of which terms to include from inner horizon.
    """
    label = "PHYS (outer+cosmo only; inner horizon thermodynamics excluded)"
    name = "RNdS_MQ_GradientFlow"

    def __init__(self, step_M: float = 0.005, step_Q: float = 0.005,
                 direction: str = 'descent'):
        self.step_M = step_M
        self.step_Q = step_Q
        self.sign = -1.0 if direction == 'descent' else +1.0

    def __call__(self, M: float, Q: float, lam: float) -> tuple[float, float, float]:
        s = RNdSState(M, Q, lam)
        if not s.is_valid():
            return M, Q, lam

        T_out = s.T_outer
        T_cos = s.T_cosmo
        Phi_out = s.Phi_outer
        Phi_cos = s.Phi_cosmo

        if T_out <= 0 or T_cos <= 0:
            return M, Q, lam

        # ∂Δ/∂M = -(1/T_outer - 1/T_cosmo)
        dDelta_dM = -(1.0/T_out - 1.0/T_cos)
        # ∂Δ/∂Q ≈ Phi_outer/T_outer - Phi_cosmo/T_cosmo
        dDelta_dQ = Phi_out/T_out - Phi_cos/T_cos

        M_new = M + self.sign * self.step_M * dDelta_dM
        Q_new = Q + self.sign * self.step_Q * dDelta_dQ

        # Clamp
        M_new = max(1e-8, M_new)
        Q_new = max(0.0, Q_new)

        # Admissibility check
        if not _rnds_admissible(M_new, Q_new, lam):
            # Try smaller step
            for factor in [0.5, 0.25, 0.1, 0.05]:
                M_try = M + self.sign * self.step_M * dDelta_dM * factor
                Q_try = Q + self.sign * self.step_Q * dDelta_dQ * factor
                M_try = max(1e-8, M_try)
                Q_try = max(0.0, Q_try)
                if _rnds_admissible(M_try, Q_try, lam):
                    return M_try, Q_try, lam
            return M, Q, lam  # stay put if all steps fail

        return M_new, Q_new, lam


class RNdS_MQ_CircularFlow:
    """
    [EXPL] Circular flow in (M, Q) space at fixed Lambda.

    Traces an approximately circular orbit in (M, Q) parameter space
    centered at some reference point (M_0, Q_0).

    Update rule (discrete rotation):
      [M - M_0]_{d+1} = R(θ) * [M - M_0]_d
      [Q - Q_0]_{d+1}         [Q - Q_0]_d

    where R(θ) is a 2x2 rotation matrix.

    Physical motivation: NONE. This is purely exploratory.
    Purpose: test whether a genuinely 2D orbit in (M, Q) space gives
    spectral dimension ≈ 2 (unlike the 1D SdS arc which gives d_s ≈ 1).
    """
    label = "EXPL"
    name = "RNdS_MQ_CircularFlow"

    def __init__(self, theta: float = 0.1, M_0: Optional[float] = None,
                 Q_0: Optional[float] = None, radius: float = 0.02):
        self.theta = theta
        self.M_0 = M_0
        self.Q_0 = Q_0
        self.radius = radius
        self._cos = np.cos(theta)
        self._sin = np.sin(theta)

    def __call__(self, M: float, Q: float, lam: float) -> tuple[float, float, float]:
        M0 = self.M_0 if self.M_0 is not None else M
        Q0 = self.Q_0 if self.Q_0 is not None else Q

        dM = M - M0
        dQ = Q - Q0

        # Rotate
        dM_new = self._cos * dM - self._sin * dQ
        dQ_new = self._sin * dM + self._cos * dQ

        M_new = M0 + dM_new
        Q_new = Q0 + dQ_new

        M_new = max(1e-8, M_new)
        Q_new = max(0.0, Q_new)

        if not _rnds_admissible(M_new, Q_new, lam):
            return M, Q, lam
        return M_new, Q_new, lam


class RNdS_Coupled_3D_Flow:
    """
    [EXPL] Fully coupled 3D flow in (M, Q, Lambda).

    The 3D state space is the most general option.
    This is entirely exploratory — no physical derivation.

    Purpose: test whether orbits in 3D parameter space produce
    spectral dimension ≈ 3 or some non-trivial value.
    """
    label = "EXPL"
    name = "RNdS_Coupled_3D_Flow"

    def __init__(self, step: float = 0.01, coupling_matrix: Optional[np.ndarray] = None):
        self.step = step
        if coupling_matrix is None:
            # Default: slight rotation + contraction in (M, Q, Lambda) space
            angle = 0.15
            self.A = np.array([
                [np.cos(angle), -np.sin(angle), 0.1],
                [np.sin(angle),  np.cos(angle), 0.05],
                [-0.05,          0.02,           0.98],
            ])
        else:
            self.A = coupling_matrix

    def __call__(self, M: float, Q: float, lam: float) -> tuple[float, float, float]:
        v = np.array([M, Q, lam])
        v_new = self.A @ v

        M_new = max(1e-8, v_new[0])
        Q_new = max(0.0, v_new[1])
        lam_new = max(0.05, min(v_new[2], 10.0))

        if not _rnds_admissible(M_new, Q_new, lam_new):
            # Try scaling down the step
            for f in [0.5, 0.25, 0.1]:
                v_try = (1-f)*v + f*v_new
                M_t, Q_t, L_t = max(1e-8, v_try[0]), max(0.0, v_try[1]), max(0.05, v_try[2])
                if _rnds_admissible(M_t, Q_t, L_t):
                    return M_t, Q_t, L_t
            return M, Q, lam
        return M_new, Q_new, lam_new


# ---------------------------------------------------------------------------
# Orbit integrators
# ---------------------------------------------------------------------------

def iterate_sds(flow, M0: float, lam0: float, n_steps: int) -> np.ndarray:
    """
    Iterate a (M, Lambda) flow for n_steps steps.
    Returns array of shape (n_steps+1, 2).
    """
    traj = np.zeros((n_steps + 1, 2))
    traj[0] = [M0, lam0]
    M, lam = M0, lam0
    for i in range(1, n_steps + 1):
        M, lam = flow(M, lam)
        traj[i] = [M, lam]
    return traj


def iterate_rnds(flow, M0: float, Q0: float, lam0: float, n_steps: int) -> np.ndarray:
    """
    Iterate an (M, Q, Lambda) flow for n_steps steps.
    Returns array of shape (n_steps+1, 3).
    """
    traj = np.zeros((n_steps + 1, 3))
    traj[0] = [M0, Q0, lam0]
    M, Q, lam = M0, Q0, lam0
    for i in range(1, n_steps + 1):
        M, Q, lam = flow(M, Q, lam)
        traj[i] = [M, Q, lam]
    return traj
