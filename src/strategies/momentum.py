# file: src/strategies/momentum.py
from __future__ import annotations
import numpy as np

def momentum_signals(prices: np.ndarray, lookback: int = 90, threshold: float = 0.0) -> np.ndarray:
    """
    Cross-sectional momentum signals for a single asset time series.
    Returns 1/0/-1 signals
    """
    T = len(prices)
    sig = np.zeros(T, dtype=int)
    for t in range(lookback, T):
        ret = (prices[t] - prices[t - lookback]) / prices[t - lookback]
        sig[t] = 1 if ret > threshold else (-1 if ret < -threshold else 0)
    return sig
