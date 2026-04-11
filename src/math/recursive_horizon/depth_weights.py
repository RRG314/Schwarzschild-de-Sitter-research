"""
depth_weights.py
================
RDT (Recursive Depth Transform) weighting scheme.

Analogy: imagine you're looking at layers of an onion. The outermost layer
is the most recent; inner layers are older.  RDT says deeper layers have
geometrically less influence, with base-e decay:

  P(depth = D - k) ~ (1 - 1/e) * (1/e)^k,    k = 0, 1, 2, ...

Here k=0 is the current (shallowest visible) depth; k=1 is one layer deeper;
and so on.  The weights form a probability distribution that sums to 1.

Applications:
  - Weighted averages of observables over an orbit
  - RDT-reweighted effective entropy
  - Depth-stratified stability analysis
"""

import numpy as np

E_INV = 1.0 / np.e  # 1/e ≈ 0.3679
ONE_MINUS_E_INV = 1.0 - E_INV  # 1 - 1/e ≈ 0.6321


def rdt_weights(D: int) -> np.ndarray:
    """
    Return the RDT probability weights for depths k = 0, 1, ..., D-1.

    w[k] = (1 - 1/e) * (1/e)^k, normalised to sum exactly to 1
           (the tail truncation error is (1/e)^D which is negligible for D>20).

    Parameters
    ----------
    D : int
        Number of depth layers.

    Returns
    -------
    np.ndarray, shape (D,)
        Probability weights summing to 1.
    """
    k = np.arange(D, dtype=float)
    w = ONE_MINUS_E_INV * (E_INV ** k)
    w /= w.sum()  # exact normalisation
    return w


def rdt_weighted_mean(values: np.ndarray, D: int | None = None) -> float:
    """
    Compute the RDT-weighted mean of a 1-D array.

    The most recent values (end of array) get the highest weight (k=0).
    Older values get exponentially less weight.

    Parameters
    ----------
    values : 1-D array of length N
    D : number of depth layers to use (default: len(values))
    """
    N = len(values)
    if D is None:
        D = N
    D = min(D, N)
    # Take the last D values (most recent)
    recent = values[-D:]
    w = rdt_weights(D)
    # w[0] corresponds to the most recent value (last element)
    # Reverse: w[0] -> recent[-1], w[1] -> recent[-2], ...
    w_ordered = w[::-1]  # so w_ordered[i] weights recent[i]
    # But rdt_weights gives w[0] = highest weight = most recent
    # recent[-1] is most recent => pair w[0] with recent[-1]
    # Simple: dot(w, recent[::-1]) reverses recent so index 0 = most recent
    return float(np.dot(w, recent[::-1]))


def rdt_weighted_observable(obs_array: np.ndarray, D: int | None = None) -> np.ndarray:
    """
    Apply RDT weighting to each column of a 2-D observable array.

    Parameters
    ----------
    obs_array : ndarray, shape (N, M)
    D : depth layers

    Returns
    -------
    ndarray, shape (M,) — one RDT-weighted mean per observable column.
    """
    N, M = obs_array.shape
    result = np.zeros(M)
    for j in range(M):
        result[j] = rdt_weighted_mean(obs_array[:, j], D)
    return result


def depth_stratified_variance(values: np.ndarray, n_strata: int = 5) -> dict:
    """
    Split the orbit into n_strata equal-length depth layers and compute
    the variance within each layer.

    Purpose: test whether variance is smaller in recent (shallow) layers
    than in deep layers — a sign of convergence to attractor.
    """
    N = len(values)
    stratum_size = N // n_strata
    variances = []
    means = []
    for i in range(n_strata):
        start = i * stratum_size
        end = start + stratum_size if i < n_strata - 1 else N
        layer = values[start:end]
        variances.append(float(np.var(layer)))
        means.append(float(np.mean(layer)))
    return {
        "stratum_variances": variances,
        "stratum_means": means,
        "converging": variances[-1] < variances[0],  # last layer quieter than first
        "variance_ratio": variances[-1] / (variances[0] + 1e-30),
    }


def effective_rdt_entropy(S_b_orbit: np.ndarray, S_c_orbit: np.ndarray,
                           D: int | None = None) -> dict:
    """
    RDT-weighted effective entropy observables.

    Returns the depth-weighted S_b, S_c, Delta, and A = S_b + S_c.
    """
    Delta_orbit = np.sqrt(S_b_orbit * S_c_orbit)
    A_orbit = S_b_orbit + S_c_orbit
    return {
        "S_b_rdt": rdt_weighted_mean(S_b_orbit, D),
        "S_c_rdt": rdt_weighted_mean(S_c_orbit, D),
        "Delta_rdt": rdt_weighted_mean(Delta_orbit, D),
        "A_rdt": rdt_weighted_mean(A_orbit, D),
    }
