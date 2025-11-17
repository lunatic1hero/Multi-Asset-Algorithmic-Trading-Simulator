# file: src/cli.py
from __future__ import annotations
import argparse
import numpy as np
from src.data.loader import MarketDataLoader
from src.strategies.sma import simple_moving_average_signals
from src.backtest.vector_backtester import vector_backtest

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--csv", required=True)
    p.add_argument("--asset", default=None, help="Single asset column to demo (optional)")
    p.add_argument("--short", type=int, default=20)
    p.add_argument("--long", type=int, default=50)
    args = p.parse_args()

    loader = MarketDataLoader(args.csv)
    df = loader.load()
    dates, asset_names, prices = loader.price_matrix(df)

    # use single-asset demo if specified, otherwise build simple cross-sectional portfolio
    if args.asset and args.asset in asset_names:
        idx = asset_names.index(args.asset)
        pseries = prices[:, idx]
        signals = simple_moving_average_signals(pseries, args.short, args.long)[:, None]  # (T,1)
        # compute returns
        returns = (pseries[1:] / pseries[:-1] - 1.0)
        returns = np.concatenate(([0.0], returns))[:, None]  # align
    else:
        # cross-sectional: for each asset compute SMA signal separately
        T, N = prices.shape
        signals = np.zeros((T, N), dtype=int)
        returns = np.zeros((T, N))
        for j in range(N):
            signals[:, j] = simple_moving_average_signals(prices[:, j], args.short, args.long)
            r = np.concatenate(([0.0], (prices[1:, j] / prices[:-1, j] - 1.0)))
            returns[:, j] = r

    equity, total_return, sharpe = vector_backtest(signals, returns, transaction_cost=0.0005)
    print(f"Total return: {total_return:.4%}, Sharpe (ann): {sharpe:.2f}")

if __name__ == "__main__":
    main()
