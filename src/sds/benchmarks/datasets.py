from __future__ import annotations

import numpy as np


def _split(rng: np.random.Generator, x: np.ndarray, y: np.ndarray, val_fraction: float = 0.25):
    idx = rng.permutation(len(x))
    cut = int(len(x) * (1.0 - val_fraction))
    train_idx = idx[:cut]
    val_idx = idx[cut:]
    return x[train_idx], y[train_idx], x[val_idx], y[val_idx]


def make_noisy_moons(seed: int, n_samples: int = 480, noise: float = 0.14):
    rng = np.random.default_rng(seed)
    n_half = n_samples // 2
    theta = rng.uniform(0.0, np.pi, size=n_half)
    outer = np.stack([np.cos(theta), np.sin(theta)], axis=1)
    inner = np.stack([1.0 - np.cos(theta), 0.5 - np.sin(theta)], axis=1)
    x = np.vstack([outer, inner])
    x += rng.normal(scale=noise, size=x.shape)
    y = np.concatenate([np.zeros(n_half), np.ones(n_half)])[:, None]
    x = (x - x.mean(axis=0, keepdims=True)) / (x.std(axis=0, keepdims=True) + 1e-8)
    return _split(rng, x, y)


def make_stiff_regression(seed: int, n_samples: int = 512, noise: float = 0.08):
    rng = np.random.default_rng(seed)
    x = rng.uniform(-1.25, 1.25, size=(n_samples, 2))
    y = (
        2.5 * x[:, :1]
        - 1.5 * x[:, 1:2]
        + 0.8 * np.sin(3.0 * x[:, :1])
        + 0.3 * x[:, :1] * x[:, 1:2]
    )
    y += rng.normal(scale=noise, size=y.shape)
    x = (x - x.mean(axis=0, keepdims=True)) / (x.std(axis=0, keepdims=True) + 1e-8)
    y = (y - y.mean(axis=0, keepdims=True)) / (y.std(axis=0, keepdims=True) + 1e-8)
    return _split(rng, x, y)
