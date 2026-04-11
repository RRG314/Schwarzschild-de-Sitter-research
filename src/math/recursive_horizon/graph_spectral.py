"""
graph_spectral.py
=================
Graph Laplacian and spectral dimension estimation from recursive orbits.

Analogy: imagine the orbit as a trail of footprints on the Eisenstein arc.
We connect nearby footprints with edges to form a graph.  The graph's
spectrum (eigenvalues of its Laplacian) tells us how many "effective
dimensions" the trail explores.

The spectral dimension d_s is estimated by fitting a power law to the
return probability of a random walk on the graph:

  P(t) ~ t^(-d_s/2)   as t -> infinity

A d_s close to 1 means the orbit lives on a 1-D curve (as expected for
points on an arc).  Non-trivial recursive maps can produce d_s != 1,
indicating effective multi-scale structure.
"""

import numpy as np
from scipy.linalg import eigh
from typing import Optional


# ---------------------------------------------------------------------------
# Graph construction
# ---------------------------------------------------------------------------

def build_proximity_graph(
    orbit: np.ndarray,
    k_neighbors: int = 5,
    sigma: Optional[float] = None,
) -> np.ndarray:
    """
    Build a weighted adjacency matrix from the orbit using k-nearest neighbors.

    Edge weight between i and j:  W_ij = exp(-||orbit[i] - orbit[j]||^2 / (2 sigma^2))
    Only the k nearest neighbors of each node are connected.

    Parameters
    ----------
    orbit : ndarray, shape (N, 2)
    k_neighbors : int
    sigma : float  (if None, use median pairwise distance)

    Returns
    -------
    W : ndarray, shape (N, N) — symmetric weight matrix
    """
    N = len(orbit)
    # Pairwise squared distances
    diff = orbit[:, None, :] - orbit[None, :, :]  # (N, N, 2)
    dist_sq = np.sum(diff**2, axis=-1)             # (N, N)

    if sigma is None:
        sigma = np.sqrt(np.median(dist_sq[dist_sq > 0]))

    W = np.exp(-dist_sq / (2.0 * sigma**2))
    np.fill_diagonal(W, 0.0)

    # Keep only k nearest neighbors (symmetric)
    W_sparse = np.zeros_like(W)
    for i in range(N):
        idx = np.argsort(dist_sq[i])[1:k_neighbors + 1]  # skip self
        W_sparse[i, idx] = W[i, idx]
    W_final = 0.5 * (W_sparse + W_sparse.T)  # symmetrize

    return W_final


def graph_laplacian(W: np.ndarray) -> np.ndarray:
    """
    Normalized graph Laplacian L = I - D^{-1/2} W D^{-1/2}.

    Eigenvalues lie in [0, 2].  Multiplicity of eigenvalue 0 = number of
    connected components.
    """
    deg = W.sum(axis=1)
    deg_inv_sqrt = np.where(deg > 0, 1.0 / np.sqrt(deg), 0.0)
    D_inv_sqrt = np.diag(deg_inv_sqrt)
    L = np.eye(len(W)) - D_inv_sqrt @ W @ D_inv_sqrt
    return L


# ---------------------------------------------------------------------------
# Spectral dimension estimation
# ---------------------------------------------------------------------------

def heat_kernel_trace(eigenvalues: np.ndarray, t_values: np.ndarray) -> np.ndarray:
    """
    Compute the heat kernel trace K(t) = sum_i exp(-lambda_i * t).

    This is the return probability of a diffusion process on the graph.
    For a d-dimensional manifold: K(t) ~ t^(-d/2) for small t.
    """
    lam = eigenvalues[eigenvalues > 1e-12]  # skip near-zero (zero mode)
    K = np.array([np.sum(np.exp(-lam * t)) for t in t_values])
    return K


def estimate_spectral_dimension(
    orbit: np.ndarray,
    k_neighbors: int = 5,
    t_min: float = 0.1,
    t_max: float = 5.0,
    n_t: int = 30,
    fit_frac: float = 0.5,
) -> dict:
    """
    Estimate the spectral dimension d_s of the orbit graph.

    Algorithm:
      1. Build k-NN proximity graph
      2. Compute normalized Laplacian eigenvalues
      3. Compute heat kernel trace K(t)
      4. Fit log K(t) vs log t to extract slope -d_s/2

    Parameters
    ----------
    orbit : ndarray, shape (N, 2)
    k_neighbors : int
    t_min, t_max : float  — range of diffusion times
    n_t : int             — number of time points
    fit_frac : float      — fraction of t range to use for fit (from t_min end)

    Returns
    -------
    dict with:
      d_s             : estimated spectral dimension
      d_s_std         : standard error of estimate
      eigenvalues     : Laplacian eigenvalues
      t_values        : diffusion times used
      K_values        : heat kernel trace
      fit_residuals   : residuals of the log-log fit
      n_zero_modes    : number of zero eigenvalues (connected components)
    """
    W = build_proximity_graph(orbit, k_neighbors=k_neighbors)
    L = graph_laplacian(W)

    # Eigenvalues of symmetric L
    eigenvalues = eigh(L, eigvals_only=True)
    n_zero = int(np.sum(eigenvalues < 1e-10))

    t_values = np.geomspace(t_min, t_max, n_t)
    K_values = heat_kernel_trace(eigenvalues, t_values)

    # Fit log K(t) = -d_s/2 * log(t) + const over fit_frac range
    n_fit = max(3, int(fit_frac * n_t))
    log_t = np.log(t_values[:n_fit])
    log_K = np.log(K_values[:n_fit] + 1e-30)

    # Linear regression
    A = np.vstack([log_t, np.ones(n_fit)]).T
    coeffs, residuals, rank, sv = np.linalg.lstsq(A, log_K, rcond=None)
    slope = coeffs[0]
    d_s = -2.0 * slope

    # Standard error
    log_K_pred = A @ coeffs
    res = log_K - log_K_pred
    if len(res) > 2:
        sigma_fit = np.std(res) * np.sqrt(n_fit / (n_fit - 2))
        # Approximate SE of slope from OLS
        Sxx = np.sum((log_t - log_t.mean())**2)
        se_slope = sigma_fit / np.sqrt(Sxx) if Sxx > 0 else np.nan
    else:
        se_slope = np.nan

    d_s_std = 2.0 * se_slope if not np.isnan(se_slope) else np.nan

    return {
        "d_s": float(d_s),
        "d_s_std": float(d_s_std) if not np.isnan(d_s_std) else None,
        "eigenvalues": eigenvalues,
        "t_values": t_values,
        "K_values": K_values,
        "fit_residuals": res,
        "n_zero_modes": n_zero,
        "n_nodes": len(orbit),
    }


# ---------------------------------------------------------------------------
# Multi-scale spectral dimension (local d_s at different scales)
# ---------------------------------------------------------------------------

def multiscale_spectral_dim(
    orbit: np.ndarray,
    t_ranges: list[tuple[float, float]],
    k_neighbors: int = 5,
    n_t: int = 20,
) -> list[dict]:
    """
    Estimate spectral dimension over multiple diffusion time scales.

    This probes whether d_s varies with scale — a signature of
    fractal or multi-scale structure.

    Returns a list of dicts, one per t_range, each with keys:
      t_min, t_max, d_s, d_s_std
    """
    W = build_proximity_graph(orbit, k_neighbors=k_neighbors)
    L = graph_laplacian(W)
    eigenvalues = eigh(L, eigvals_only=True)

    results = []
    for t_min, t_max in t_ranges:
        t_values = np.geomspace(t_min, t_max, n_t)
        K_values = heat_kernel_trace(eigenvalues, t_values)

        log_t = np.log(t_values)
        log_K = np.log(K_values + 1e-30)
        A = np.vstack([log_t, np.ones(n_t)]).T
        coeffs, *_ = np.linalg.lstsq(A, log_K, rcond=None)
        d_s = -2.0 * coeffs[0]

        results.append({
            "t_min": t_min,
            "t_max": t_max,
            "d_s": float(d_s),
        })
    return results
