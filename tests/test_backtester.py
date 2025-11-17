# file: tests/test_backtester.py
import numpy as np
from src.backtest.vector_backtester import vector_backtest

def test_backtest_identity():
    # trivial test: single asset, buy-and-hold (signal=1), returns constant 0.001
    T = 100
    signals = np.ones((T,1))
    rets = np.ones((T,1)) * 0.001
    equity, total, sharpe = vector_backtest(signals, rets, transaction_cost=0.0)
    assert equity[-1] > 1.0
    assert total > 0
