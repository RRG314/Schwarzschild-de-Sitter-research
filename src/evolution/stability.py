"""
stability.py — Jacobians, Lyapunov exponents, fixed-point analysis.
"""

import numpy as np
from typing import Callable


def jacobian_2d(f: Callable, x: float, y: float, h: float = 1e-5) -> np.ndarray:
    J = np.zeros((2, 2))
    for j, (dx, dy) in enumerate([(h, 0), (0, h)]):
        fp = np.array(f(x + dx, y + dy))
        fm = np.array(f(x - dx, y - dy))
        J[:, j] = (fp - fm) / (2 * (h if j == 0 else h))
    return J


def jacobian_3d(f: Callable, x: float, y: float, z: float, h: float = 1e-5) -> np.ndarray:
    J = np.zeros((3, 3))
    deltas = [(h,0,0),(0,h,0),(0,0,h)]
    for j, (dx,dy,dz) in enumerate(deltas):
        fp = np.array(f(x+dx, y+dy, z+dz))
        fm = np.array(f(x-dx, y-dy, z-dz))
        J[:, j] = (fp - fm) / (2*h)
    return J


def spectral_radius(J: np.ndarray) -> float:
    return float(np.max(np.abs(np.linalg.eigvals(J))))


def classify_fixed_point(sr: float) -> str:
    if sr < 1.0 - 1e-8:
        return "stable"
    elif sr > 1.0 + 1e-8:
        return "unstable"
    else:
        return "marginal"


def max_lyapunov_2d(f: Callable, x0: float, y0: float,
                    n_steps: int = 3000, n_renorm: int = 50) -> float:
    x, y = x0, y0
    Q = np.eye(2)
    log_exp = 0.0
    steps_per_block = max(1, n_steps // n_renorm)
    count = 0
    for _ in range(n_renorm):
        for _ in range(steps_per_block):
            J = jacobian_2d(f, x, y)
            Q = J @ Q
            nx, ny = f(x, y)
            if not (np.isfinite(nx) and np.isfinite(ny)):
                break
            x, y = nx, ny
            count += 1
        Q, R = np.linalg.qr(Q)
        log_exp += np.log(abs(R[0, 0]) + 1e-300)
    return float(log_exp / max(count, 1))


def max_lyapunov_3d(f: Callable, x0: float, y0: float, z0: float,
                    n_steps: int = 2000, n_renorm: int = 30) -> float:
    x, y, z = x0, y0, z0
    Q = np.eye(3)
    log_exp = 0.0
    steps_per_block = max(1, n_steps // n_renorm)
    count = 0
    for _ in range(n_renorm):
        for _ in range(steps_per_block):
            J = jacobian_3d(f, x, y, z)
            Q = J @ Q
            nx, ny, nz = f(x, y, z)
            if not all(np.isfinite([nx, ny, nz])):
                break
            x, y, z = nx, ny, nz
            count += 1
        Q, R = np.linalg.qr(Q)
        log_exp += np.log(abs(R[0, 0]) + 1e-300)
    return float(log_exp / max(count, 1))


def find_fixed_points_2d(f: Callable, grid_x, grid_y,
                          tol: float = 1e-7, n_iter: int = 2000) -> list:
    """
    Search for fixed points by iterating from a grid and checking convergence.
    """
    fps = []
    seen = []
    for x0 in grid_x:
        for y0 in grid_y:
            x, y = x0, y0
            for _ in range(n_iter):
                xn, yn = f(x, y)
                if abs(xn - x) + abs(yn - y) < tol:
                    break
                x, y = xn, yn
            # Check
            xn, yn = f(x, y)
            if abs(xn - x) + abs(yn - y) < tol * 10:
                # Deduplicate
                dup = any(abs(x - sx) + abs(y - sy) < 1e-4 for sx, sy in seen)
                if not dup:
                    seen.append((x, y))
                    J = jacobian_2d(f, x, y)
                    sr = spectral_radius(J)
                    fps.append({
                        "x": float(x), "y": float(y),
                        "spectral_radius": float(sr),
                        "stability": classify_fixed_point(sr),
                        "eigenvalues": np.linalg.eigvals(J).tolist(),
                    })
    return fps
