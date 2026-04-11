"""
RDT (Recursive Depth Transform) tools.

R(n, alpha) = number of times n must be divided by floor(log(n)^alpha)
to reduce to <= 1. Minimum divisor is 2.

Used for:
- Hierarchical labeling of overtone towers
- Comparing RDT-organized spectral summaries to uniform summaries
"""

import numpy as np


def rdt_depth(n: int, alpha: float = 1.5) -> int:
    """Compute RDT depth of integer n."""
    if n <= 1:
        return 0
    steps = 0
    x = n
    while x > 1:
        d = int(np.log(x) ** alpha)
        d = max(2, d)
        x = x // d
        if x == 0:
            break
        steps += 1
        if steps > 1000:
            break
    return steps


def rdt_table(N: int, alpha: float = 1.5) -> np.ndarray:
    """Compute RDT depth for all integers 1..N."""
    R = np.zeros(N + 1, dtype=int)
    for n in range(1, N + 1):
        R[n] = rdt_depth(n, alpha)
    return R


def rdt_level_sets(N: int, alpha: float = 1.5) -> dict:
    """Return dict mapping depth -> list of integers at that depth."""
    R = rdt_table(N, alpha)
    levels = {}
    for n in range(1, N + 1):
        d = R[n]
        if d not in levels:
            levels[d] = []
        levels[d].append(n)
    return levels


def overtone_rdt_summary(omega_sequence: list, alpha: float = 1.5) -> dict:
    """
    Given a sequence of QNM frequencies omega_n (n=1, 2, ...),
    compute the mean and std of |omega_n| grouped by RDT depth of n.

    Returns dict with depth -> {'mean': ..., 'std': ..., 'count': ...}
    """
    results = {}
    for i, omega in enumerate(omega_sequence):
        n = i + 1  # overtone index starts at 1
        depth = rdt_depth(n, alpha)
        if depth not in results:
            results[depth] = []
        results[depth].append(abs(omega))

    summary = {}
    for depth, vals in sorted(results.items()):
        arr = np.array(vals)
        summary[depth] = {
            'mean': float(np.mean(arr)),
            'std': float(np.std(arr)),
            'count': len(arr),
            'min': float(np.min(arr)),
            'max': float(np.max(arr)),
        }
    return summary


def compare_rdt_vs_uniform(omega_sequence: list, n_bins: int = 5, alpha: float = 1.5) -> dict:
    """
    Compare RDT-grouped statistics to uniform-bin statistics.
    Returns: {'rdt': {...}, 'uniform': {...}, 'entropy_rdt': float, 'entropy_uniform': float}

    Shannon entropy of the mean-absolute-frequency distribution is used as
    a diversity measure. Higher entropy means more uniform spread.
    """
    rdt_sum = overtone_rdt_summary(omega_sequence, alpha=alpha)

    # Uniform binning by overtone number
    N = len(omega_sequence)
    bin_size = max(1, N // n_bins)
    uniform_sum = {}
    for b in range(n_bins):
        start = b * bin_size
        end = min((b + 1) * bin_size, N)
        vals = [abs(omega_sequence[i]) for i in range(start, end)]
        if vals:
            arr = np.array(vals)
            uniform_sum[b] = {
                'mean': float(np.mean(arr)),
                'std': float(np.std(arr)),
                'count': len(arr),
            }

    def shannon_entropy(groups):
        counts = np.array([g['count'] for g in groups.values()], dtype=float)
        probs = counts / counts.sum()
        probs = probs[probs > 0]
        return float(-np.sum(probs * np.log(probs)))

    return {
        'rdt': rdt_sum,
        'uniform': uniform_sum,
        'entropy_rdt': shannon_entropy(rdt_sum),
        'entropy_uniform': shannon_entropy(uniform_sum),
    }
