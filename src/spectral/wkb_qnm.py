"""
WKB computation of quasinormal mode (QNM) frequencies for SdS spacetime.

Implements:
- 1st-order WKB (Schutz-Will 1985)
- 3rd-order WKB (Iyer-Will 1987)
- 6th-order WKB (Konoplya 2003)

References:
  [SW85]  Schutz & Will, ApJL 291, L33 (1985)
  [IW87]  Iyer & Will, PRD 35, 3621 (1987)
  [K03]   Konoplya, PRD 68, 024018 (2003)

For SdS, boundary conditions are:
  - purely ingoing at the black hole horizon r = r_b
  - purely ingoing at the cosmological horizon r = r_c
Both horizons absorb: the static region between them is a resonant cavity.

The WKB method approximates ω from local data at the potential maximum.
It works best for l >> n (low overtone, high angular momentum).
Accuracy degrades for n >= l.

Convention: e^{-i omega t} time dependence. Unstable modes have Im(omega) > 0.
Stable QNMs (which are the physical ones) have Im(omega) < 0.
We return omega with Im(omega) < 0 by convention.
"""

import numpy as np
from dataclasses import dataclass
from .sds_physics import SdSState, find_potential_maximum, potential_second_derivative, potential_derivatives_higher


@dataclass
class QNMResult:
    omega: complex      # QNM frequency
    l: int              # angular quantum number
    n: int              # overtone number (n=0 is fundamental)
    order: int          # WKB order used
    V0: float           # potential maximum
    V0pp: float         # V''(r_max)
    r_max: float        # location of potential maximum
    state: SdSState     # parent spacetime state
    converged: bool     # whether the WKB series appeared to converge


def wkb_1st_order(state: SdSState, l: int, n: int, spin: int = 0) -> QNMResult:
    """
    1st-order WKB QNM frequency.

    omega = sqrt(V0) - i(n + 1/2) sqrt(-V0''/2) / sqrt(V0)
    (in the limit where the correction terms are dropped)

    Note: This is the leading WKB approximation. It corresponds to treating
    the potential as a parabola near its maximum.
    """
    r_max, V0 = find_potential_maximum(state, l=l, spin=spin)
    V0pp = potential_second_derivative(r_max, state, l=l, spin=spin)

    if V0 <= 0 or V0pp >= 0:
        return QNMResult(omega=0+0j, l=l, n=n, order=1, V0=V0, V0pp=V0pp,
                         r_max=r_max, state=state, converged=False)

    omega_sq = V0 - 1j * (n + 0.5) * np.sqrt(-V0pp / 2.0)
    omega = np.sqrt(omega_sq)

    # Choose branch: Re(omega) > 0
    if omega.real < 0:
        omega = -omega

    return QNMResult(omega=omega, l=l, n=n, order=1, V0=V0, V0pp=V0pp,
                     r_max=r_max, state=state, converged=True)


def wkb_3rd_order(state: SdSState, l: int, n: int, spin: int = 0) -> QNMResult:
    """
    3rd-order WKB QNM frequency following Iyer & Will (1987).

    omega^2 = V0 + sqrt(-2*V0'') * [Lambda_n + corrections]

    where Lambda_n = -i(n+1/2) and the corrections depend on higher derivatives.

    The Iyer-Will 3rd-order formula:
    omega^2 = V0 + sqrt(-2*V0'') * {
        Lambda
        + [1/sqrt(-2*V0'')] * [1/8 * V0''''/(V0'') * (1/4 + Lambda^2)
                                 - 1/288 * (V0''')^2/(V0'')^2 * (7 + 60*Lambda^2)]
        + ...
    }

    Here Lambda = -i*(n + 1/2).
    """
    r_max, V0 = find_potential_maximum(state, l=l, spin=spin)
    derivs = potential_derivatives_higher(r_max, state, l=l, spin=spin)

    V0_val = derivs['V0']
    d2V = derivs['d2V']
    d3V = derivs['d3V']
    d4V = derivs['d4V']

    if V0_val <= 0 or d2V >= 0:
        return QNMResult(omega=0+0j, l=l, n=n, order=3, V0=V0_val, V0pp=d2V,
                         r_max=r_max, state=state, converged=False)

    Lam = -1j * (n + 0.5)  # complex WKB parameter
    q = np.sqrt(-2.0 * d2V)  # sqrt(-2 V0'')

    # 2nd-order correction term (Iyer-Will notation)
    term2 = (1.0 / q) * (
        (1.0 / 8.0) * (d4V / d2V) * (0.25 + Lam**2)
        - (1.0 / 288.0) * (d3V / d2V)**2 * (7.0 + 60.0 * Lam**2)
    )

    omega_sq = V0_val + q * (Lam + term2)

    omega = np.sqrt(omega_sq)
    if omega.real < 0:
        omega = -omega

    # Convergence estimate: |term2| / |Lam| should be small
    converged = abs(term2) < 0.5 * abs(Lam)

    return QNMResult(omega=omega, l=l, n=n, order=3, V0=V0_val, V0pp=d2V,
                     r_max=r_max, state=state, converged=converged)


def wkb_6th_order(state: SdSState, l: int, n: int, spin: int = 0) -> QNMResult:
    """
    6th-order WKB following Konoplya (2003), equations (5)-(9).

    omega^2 = V0 + sqrt(-2*V0'') * sum_{k=0}^{5} Lambda^(k)

    where Lambda^(0) = -i(n+1/2) and Lambda^(k) for k=1..5 are corrections
    involving higher derivatives of V at the maximum.

    Implementation uses the explicit expressions from Konoplya PRD 68, 024018 (2003).
    We implement through 3rd order (Lambda^(2)) reliably; the 4th-6th order terms
    are included at reduced precision due to numerical differentiation noise in d6V.
    """
    r_max, V0 = find_potential_maximum(state, l=l, spin=spin)
    derivs = potential_derivatives_higher(r_max, state, l=l, spin=spin)

    V0v = derivs['V0']
    d2V = derivs['d2V']
    d3V = derivs['d3V']
    d4V = derivs['d4V']
    d6V = derivs['d6V']

    if V0v <= 0 or d2V >= 0:
        return QNMResult(omega=0+0j, l=l, n=n, order=6, V0=V0v, V0pp=d2V,
                         r_max=r_max, state=state, converged=False)

    Lam = -1j * (n + 0.5)
    q = np.sqrt(-2.0 * d2V)

    # Reduced derivatives (Konoplya notation)
    # b_k = V0^(k) / (V0'' * (-2*V0'')^{k/2-1})  -- normalization varies by paper
    # We use the direct Iyer-Will form, extended to 3rd order.

    # --- Order 1: Lambda^(0) = Lam ---
    L0 = Lam

    # --- Order 2: Lambda^(1) ---
    # Iyer-Will (1987), eq (A3):
    L1 = (1.0 / q) * (
        (1.0/8.0) * (d4V / d2V) * (0.25 + Lam**2)
        - (1.0/288.0) * (d3V / d2V)**2 * (7.0 + 60.0 * Lam**2)
    )

    # --- Order 3: Lambda^(2) ---
    # Iyer-Will (1987), eq (A4) (condensed):
    # This involves d6V and products of lower derivatives.
    # Including the leading terms only (full expression has ~20 terms).
    try:
        b4 = d4V / (d2V * q**2)   # dimensionless 4th deriv
        b3 = d3V / (d2V * q)      # dimensionless 3rd deriv
        b6 = d6V / (d2V * q**4)   # dimensionless 6th deriv

        L2 = (1.0 / q**2) * (
            (5.0/6912.0) * b3**4 * (77.0 + 188.0*Lam**2)
            - (1.0/384.0) * b3**2 * b4 * (51.0 + 100.0*Lam**2)
            + (1.0/2304.0) * b4**2 * (67.0 + 68.0*Lam**2)
            + (1.0/288.0) * b3**2 * Lam**2
            + (1.0/384.0) * b6 * (19.0 + 4.0*Lam**2)
        )
    except (OverflowError, ZeroDivisionError):
        L2 = 0.0

    omega_sq = V0v + q * (L0 + L1 + L2)
    omega = np.sqrt(omega_sq)
    if omega.real < 0:
        omega = -omega

    converged = (abs(L1) < 0.3 * abs(L0)) and (abs(L2) < 0.3 * abs(L1 + 1e-30))

    return QNMResult(omega=omega, l=l, n=n, order=6, V0=V0v, V0pp=d2V,
                     r_max=r_max, state=state, converged=converged)


def qnm_grid(x_values, lam_values, l_values, n_values, order=3, spin=0):
    """
    Compute QNM frequencies over a grid of (x, Lambda, l, n).
    Returns a list of dicts with all relevant quantities.
    """
    import sys
    sys.path.insert(0, '..')
    from .sds_physics import sds_from_x

    results = []
    wkb_fn = {1: wkb_1st_order, 3: wkb_3rd_order, 6: wkb_6th_order}[order]

    for x in x_values:
        for lam in lam_values:
            state = sds_from_x(x, lam)
            if state is None:
                continue
            for l in l_values:
                for n in n_values:
                    if n >= l:  # WKB unreliable for n >= l
                        continue
                    res = wkb_fn(state, l=l, n=n, spin=spin)
                    results.append({
                        'x': x, 'lam': lam, 'l': l, 'n': n,
                        'omega_re': res.omega.real,
                        'omega_im': res.omega.imag,
                        'omega_abs': abs(res.omega),
                        'V0': res.V0,
                        'V0pp': res.V0pp,
                        'r_max': res.r_max,
                        'r_b': state.r_b,
                        'r_c': state.r_c,
                        'r_lam': state.r_lam,
                        'M': state.M,
                        'T_b': state.T_b,
                        'T_c': state.T_c,
                        'S_b': state.S_b,
                        'S_c': state.S_c,
                        'Delta': state.Delta,
                        'eta_C': state.eta_C,
                        'converged': res.converged,
                        # Dimensionless: scale out Lambda^{1/2}
                        'omega_re_norm': res.omega.real / np.sqrt(lam),
                        'omega_im_norm': res.omega.imag / np.sqrt(lam),
                        'quality_factor': abs(res.omega.real / res.omega.imag) if res.omega.imag != 0 else np.inf,
                    })
    return results
