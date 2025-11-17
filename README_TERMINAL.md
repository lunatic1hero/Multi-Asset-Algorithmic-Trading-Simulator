Multi-Asset Trading System — SMA, Momentum, ML Wrapper, Vector Backtester, Dash UI

This repository is a clean, modern reimplementation of a multi-asset algorithmic trading framework. It includes:
- Simple technical strategies (SMA, Momentum)
- A vectorized multi-asset backtester
- ML model wrapper for plug-and-play predictions
- Plotly/Dash interactive UI
- A reproducible demo notebook
- Synthetic multi-asset dataset
- Basic unit tests
- Docker support

This codebase is inspired by earlier public trading projects, but the entire structure, algorithms, APIs, visuals, and file layout have been redesigned from scratch.
Nothing has been copy-pasted; the implementation is fully original.

--------------------------------------------------------------------------------
Repository Structure
--------------------------------------------------------------------------------

multi-asset-trading/
  src/
    data/
      loader.py                MarketDataLoader, loads CSV, price and return matrices
    strategies/
      sma.py                   SMA strategy (long/short/flat signals)
      momentum.py              Momentum-based signals
      ml_strategy.py           Produces signals from ML model predictions
    backtest/
      vector_backtester.py     Vectorized multi-asset portfolio backtester
    ml/
      model_wrapper.py         Simple sklearn model wrapper (fit, predict, save, load)
    utils.py                   Plotly helpers (price charts, equity curves)
    cli.py                     CLI runner for SMA backtests
  dash_app/
    app.py                     Interactive Dash UI for exploring SMA parameters
  notebooks/
    demo.ipynb                 Notebook demo of loader → strategy → backtester → plots
  data/
    sample_multi_asset.csv     Synthetic multi-asset price dataset
    sample_generator.py        Script to generate the dataset
  tests/
    test_loader.py
    test_backtester.py
  requirements.txt
  Dockerfile
  README.md

--------------------------------------------------------------------------------
Installation
--------------------------------------------------------------------------------

1. Create and activate a virtual environment:

   python -m venv .venv
   source .venv/bin/activate               (Linux/macOS)
   .venv\Scripts\Activate.ps1            (Windows PowerShell)

2. Install dependencies:

   pip install --upgrade pip
   pip install -r requirements.txt

3. (Optional) If sample_multi_asset.csv is missing, generate it:

   python data/sample_generator.py

--------------------------------------------------------------------------------
Running Examples
--------------------------------------------------------------------------------

CLI SMA Backtest:

   python -m src.cli --csv data/sample_multi_asset.csv

Launch Dash Interactive UI:

   python dash_app/app.py
   (Open http://127.0.0.1:8050 in your browser)

Run Tests:

   pytest -q

--------------------------------------------------------------------------------
Demo Notebook Overview
--------------------------------------------------------------------------------

notebooks/demo.ipynb performs:
- Adding repo root to sys.path so src/ imports work
- Loading data/sample_multi_asset.csv using MarketDataLoader
- Running a simple SMA strategy on a selected asset
- Generating signals and returns
- Running the vector backtester
- Displaying interactive Plotly price charts and equity curves inline

If running from notebooks/ folder, the CSV path is ../data/sample_multi_asset.csv.

--------------------------------------------------------------------------------
Core Components
--------------------------------------------------------------------------------

1. Loader (src/data/loader.py)
   - Loads CSV with a date column and multiple asset columns
   - Returns price matrix (T x N)
   - Computes log or simple returns

2. Strategies (src/strategies/)
   SMA Strategy:
     simple_moving_average_signals(prices, window_short, window_long)
     Signals: {1, 0, -1}

   Momentum Strategy:
     momentum_signals(prices, lookback, threshold)

   ML Strategy:
     ml_signals(feature_matrix, model_predict)
     Converts model outputs to signals

3. Backtester (src/backtest/vector_backtester.py)
   vector_backtest(signals, returns, transaction_cost)
   - Vectorized multi-asset backtesting
   - Computes PnL, equity curve, total return, Sharpe ratio
   - Includes transaction cost handling

4. ML Wrapper (src/ml/model_wrapper.py)
   - Wrapper for sklearn models
   - Fit, predict, save, load
   - Extendable for TensorFlow/PyTorch

5. Dash UI (dash_app/app.py)
   - Interactive SMA explorer for any asset
   - Dynamic equity curves
   - Adjustable SMA windows

--------------------------------------------------------------------------------
Troubleshooting
--------------------------------------------------------------------------------

- If imports fail in the notebook, ensure repo root is added to sys.path.
- If Plotly charts do not appear, set:  pio.renderers.default = "notebook"
- If Dash server fails, ensure port 8050 is free.

--------------------------------------------------------------------------------
License & Credit
--------------------------------------------------------------------------------

This project is a new implementation inspired by earlier public trading repositories.
Structure, logic, and visualization are uniquely rewritten.
Recommended license: MIT.
