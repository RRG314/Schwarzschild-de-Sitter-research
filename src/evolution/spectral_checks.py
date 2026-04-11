"""
spectral_checks.py
==================
Spectral dimension estimation for orbits in parameter space.

Key upgrade: we now work in (M, Lambda) or (M, Q, Lambda) space,
so orbits CAN be genuinely multi-dimensional. The spectral dimension
test is only meaningful here if the orbit actually explores more than 1D.

Unlike the old model (1D Eisenstein arc), here:
- SdS (M, Lambda) orbits live in 2D space → d_s should be ~1-2
- RNdS (M, Q, Lambda) orbits live in 3D space → d_s should be ~1-3

We report actual d_s and compare to the ambient dimension.
"""

import numpy as np
from scipy.linalg import eigh


def build_knn_graph(points: np.ndarray, k: int = 5) -> np.ndarray:
    """Build k-NN weighted adjacency matrix. points: (N, D)."""
    N = len(points)
    diff = points[:, None, :] - points[None, :, :]
    dist_sq = np.sum(diff**2, axis=-1)
    sigma = np.sqrt(np.median(dist_sq[dist_sq > 0]) + 1e-30)
    W = np.exp(-dist_sq / (2 * sigma**2))
    np.fill_diagonal(W, 0.0)
    W_sparse = np.zeros_like(W)
    for i in range(N):
        idx = np.argsort(dist_sq[i])[1:k+1]
        W_sparse[i, idx] = W[i, idx]
    return 0.5 * (W_sparse + W_sparse.T)


def normalized_laplacian(W: np.ndarray) -> np.ndarray:
    deg = W.sum(axis=1)
    d_inv_sqrt = np.where(deg > 1e-12, 1.0/np.sqrt(deg), 0.0)
    D = np.diag(d_inv_sqrt)
    return np.eye(len(W)) - D @ W @ D


def heat_kernel_trace(eigenvalues: np.ndarray, t_values: np.ndarray) -> np.ndarray:
    lam = eigenvalues[eigenvalues > 1e-10]
    return np.array([np.sum(np.exp(-lam * t)) for t in t_values])


def estimate_spectral_dim(points: np.ndarray, k: int = 5,
                           t_min: float = 0.3, t_max: float = 3.0,
                           n_t: int = 20, fit_frac: float = 0.6) -> dict:
    """
    Estimate spectral dimension d_s of the point cloud.

    Returns d_s and supporting data. The ambient dimension of `points` is
    points.shape[1] — we report the ratio d_s / ambient_dim as a key check.
    """
    if len(points) < 10:
        return {"d_s": np.nan, "error": "too few points"}
    ambient_dim = points.shape[1]

    # Normalize each column to [0,1] for stable graph construction
    pmin, pmax = points.min(axis=0), points.max(axis=0)
    scale = pmax - pmin
    scale[scale < 1e-15] = 1.0
    pts_norm = (points - pmin) / scale

    W = build_knn_graph(pts_norm, k=k)
    L = normalized_laplacian(W)
    eigvals = eigh(L, eigvals_only=True)

    n_zero = int(np.sum(eigvals < 1e-9))
    t_values = np.geomspace(t_min, t_max, n_t)
    K = heat_kernel_trace(eigvals, t_values)

    n_fit = max(4, int(fit_frac * n_t))
    log_t = np.log(t_values[:n_fit])
    log_K = np.log(K[:n_fit] + 1e-30)

    A = np.vstack([log_t, np.ones(n_fit)]).T
    coeffs, *_ = np.linalg.lstsq(A, log_K, rcond=None)
    slope = coeffs[0]
    d_s = -2.0 * slope

    res = log_K - A @ coeffs
    if len(res) > 2:
        Sxx = np.sum((log_t - log_t.mean())**2)
        se_slope = np.std(res) * np.sqrt(n_fit/(n_fit-2)) / np.sqrt(Sxx + 1e-30)
        d_s_se = 2.0 * se_slope
    else:
        d_s_se = np.nan

    return {
        "d_s": float(d_s),
        "d_s_se": float(d_s_se) if not np.isnan(d_s_se) else None,
        "ambient_dim": ambient_dim,
        "d_s_over_ambient": float(d_s / ambient_dim),
        "n_zero_modes": n_zero,
        "n_points": len(points),
        "t_range": [t_min, t_max],
    }


def multiscale_spectral_dim(points: np.ndarray, k: int = 5) -> list:
    """Estimate d_s at 4 different scale ranges."""
    results = []
    for t_min, t_max, label in [
        (0.05, 0.3, "short"),
        (0.3, 1.0, "intermediate"),
        (1.0, 5.0, "long"),
        (5.0, 20.0, "very_long"),
    ]:
        r = estimate_spectral_dim(points, k=k, t_min=t_min, t_max=t_max)
        r["scale_label"] = label
        results.append(r)
    return results


def intrinsic_dimension_pca(points: np.ndarray, variance_threshold: float = 0.95) -> int:
    """
    Estimate intrinsic dimension from PCA (number of components
    explaining variance_threshold fraction of total variance).
    """
    if len(points) < 3:
        return 1
    pmin = points.min(axis=0)
    pmax = points.max(axis=0)
    scale = pmax - pmin
    scale[scale < 1e-15] = 1.0
    pts_norm = (points - points.mean(axis=0)) / scale
    _, sv, _ = np.linalg.svd(pts_norm, full_matrices=False)
    var_explained = np.cumsum(sv**2) / (np.sum(sv**2) + 1e-30)
    n_components = int(np.searchsorted(var_explained, variance_threshold)) + 1
    return min(n_components, points.shape[1])
