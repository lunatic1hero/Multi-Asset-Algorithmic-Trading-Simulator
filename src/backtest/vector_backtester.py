# file: src/backtest/vector_backtester.py
from __future__ import annotations
import numpy as np
from typing import Tuple

def vector_backtest(signals: np.ndarray, returns: np.ndarray, transaction_cost: float = 0.0) -> Tuple[np.ndarray, float, float]:
    """
    signals: (T, N) positions in {1,0,-1} for each time and asset
    returns: (T, N) period returns aligned (same T)
    Returns:
      equity_curve: 1D cumulative returns (length T)
      total_return: final cumulative return (scalar)
      sharpe: simple Sharpe ratio (annualized, using 252 periods)
    Assumes signals are applied at time t and returns[t] is the period return (vectorized).
    """
    # PnL per period: element-wise product (positions * returns)
    pnl = (signals * returns).sum(axis=1)  # portfolio daily return (sum across assets)
    # apply transaction costs on changes in positions
    pos_change = np.abs(np.diff(signals, axis=0)).sum(axis=1)  # sum across assets
    pos_change = np.concatenate(([0.0], pos_change))
    pnl = pnl - transaction_cost * pos_change
    equity = np.cumprod(1 + pnl)  # starting at 1.0
    total_return = float(equity[-1] - 1.0)
    ann_factor = 252  # assume daily
    mean = pnl.mean() * ann_factor
    std = pnl.std() * (ann_factor ** 0.5)
    sharpe = float(mean / std) if std > 0 else 0.0
    return equity, total_return, sharpe
