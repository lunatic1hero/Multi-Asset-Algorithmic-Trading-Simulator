# file: src/strategies/sma.py
from __future__ import annotations
import numpy as np
from typing import Tuple, List

def simple_moving_average_signals(prices: np.ndarray, window_short: int = 20, window_long: int = 50) -> np.ndarray:
    """
    prices: 1D price series (T,)
    returns: signal series aligned with input: 1 = long, -1 = short, 0 = flat (length T)
    """
    T = len(prices)
    signals = np.zeros(T, dtype=int)
    if T < window_long + 1:
        return signals
    short = np.convolve(prices, np.ones(window_short)/window_short, mode='same')
    long = np.convolve(prices, np.ones(window_long)/window_long, mode='same')
    # generate signals where we have enough history
    for t in range(window_long, T):
        if short[t] > long[t]:
            signals[t] = 1
        elif short[t] < long[t]:
            signals[t] = -1
    return signals
