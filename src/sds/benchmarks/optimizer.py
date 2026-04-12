from __future__ import annotations

import numpy as np


class AdamOptimizer:
    def __init__(self, params: dict[str, np.ndarray], lr: float, beta1: float = 0.9, beta2: float = 0.999, eps: float = 1e-8):
        self.params = params
        self.lr = lr
        self.beta1 = beta1
        self.beta2 = beta2
        self.eps = eps
        self.step_count = 0
        self.m = {k: np.zeros_like(v) for k, v in params.items()}
        self.v = {k: np.zeros_like(v) for k, v in params.items()}

    def step(
        self,
        grads: dict[str, np.ndarray],
        lr: float | None = None,
        beta1: float | None = None,
        weight_decay: float = 0.0,
        clip_norm: float | None = None,
    ) -> dict[str, float]:
        self.step_count += 1
        lr = self.lr if lr is None else lr
        beta1 = self.beta1 if beta1 is None else beta1
        grad_norm_sq = sum(float((g * g).sum()) for g in grads.values())
        grad_norm = float(np.sqrt(max(0.0, grad_norm_sq)))
        if clip_norm is not None and grad_norm > clip_norm and grad_norm > 1e-12:
            scale = clip_norm / grad_norm
            grads = {k: g * scale for k, g in grads.items()}
            grad_norm = clip_norm

        step_norm_sq = 0.0
        for name, grad in grads.items():
            self.m[name] = beta1 * self.m[name] + (1.0 - beta1) * grad
            self.v[name] = self.beta2 * self.v[name] + (1.0 - self.beta2) * (grad * grad)
            m_hat = self.m[name] / (1.0 - beta1 ** self.step_count)
            v_hat = self.v[name] / (1.0 - self.beta2 ** self.step_count)
            update = m_hat / (np.sqrt(v_hat) + self.eps)
            if weight_decay and name.startswith("W"):
                update = update + weight_decay * self.params[name]
            self.params[name] -= lr * update
            step_norm_sq += float(((lr * update) ** 2).sum())
        return {
            "grad_norm": grad_norm,
            "step_norm": float(np.sqrt(max(0.0, step_norm_sq))),
            "param_norm": float(np.sqrt(sum(float((p * p).sum()) for p in self.params.values()))),
        }
