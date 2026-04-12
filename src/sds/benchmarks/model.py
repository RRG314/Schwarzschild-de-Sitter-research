from __future__ import annotations

from dataclasses import dataclass

import numpy as np


@dataclass
class LossResult:
    loss: float
    grads: dict[str, np.ndarray]
    accuracy: float | None


class TinyMLP:
    def __init__(self, in_dim: int, hidden_dim: int, out_dim: int, task: str, seed: int) -> None:
        self.task = task
        rng = np.random.default_rng(seed)
        self.params: dict[str, np.ndarray] = {
            "W1": rng.normal(scale=0.35, size=(in_dim, hidden_dim)),
            "b1": np.zeros((1, hidden_dim)),
            "W2": rng.normal(scale=0.25, size=(hidden_dim, out_dim)),
            "b2": np.zeros((1, out_dim)),
        }

    def forward(self, x: np.ndarray):
        z1 = x @ self.params["W1"] + self.params["b1"]
        h1 = np.tanh(z1)
        logits = h1 @ self.params["W2"] + self.params["b2"]
        return z1, h1, logits

    def predict(self, x: np.ndarray) -> np.ndarray:
        _, _, logits = self.forward(x)
        if self.task == "classification":
            return 1.0 / (1.0 + np.exp(-logits))
        return logits

    def loss_and_grads(self, x: np.ndarray, y: np.ndarray, weight_decay: float = 0.0) -> LossResult:
        z1, h1, logits = self.forward(x)
        n = len(x)
        if self.task == "classification":
            probs = 1.0 / (1.0 + np.exp(-logits))
            probs = np.clip(probs, 1e-7, 1.0 - 1e-7)
            loss = -np.mean(y * np.log(probs) + (1.0 - y) * np.log(1.0 - probs))
            dlogits = (probs - y) / n
            accuracy = float(((probs >= 0.5) == (y >= 0.5)).mean())
        else:
            diff = logits - y
            loss = float(np.mean(diff * diff))
            dlogits = 2.0 * diff / n
            accuracy = None

        grads = {
            "W2": h1.T @ dlogits,
            "b2": dlogits.sum(axis=0, keepdims=True),
        }
        dh1 = dlogits @ self.params["W2"].T
        dz1 = dh1 * (1.0 - np.tanh(z1) ** 2)
        grads["W1"] = x.T @ dz1
        grads["b1"] = dz1.sum(axis=0, keepdims=True)

        if weight_decay > 0.0:
            loss += 0.5 * weight_decay * sum(float((p * p).sum()) for name, p in self.params.items() if name.startswith("W"))
            grads["W1"] += weight_decay * self.params["W1"]
            grads["W2"] += weight_decay * self.params["W2"]

        return LossResult(loss=float(loss), grads=grads, accuracy=accuracy)
