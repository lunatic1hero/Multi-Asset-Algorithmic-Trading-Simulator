# file: dash_app/app.py
import dash
from dash import dcc, html, Input, Output
import pandas as pd
from src.data.loader import MarketDataLoader
from src.utils import plot_price_timeseries, plot_equity_curve
from src.strategies.sma import simple_moving_average_signals
from src.backtest.vector_backtester import vector_backtest
import numpy as np

CSV = "data/sample_multi_asset.csv"

loader = MarketDataLoader(CSV)
df = loader.load()
dates, asset_names, prices = loader.price_matrix(df)

app = dash.Dash(__name__)
app.layout = html.Div([
    html.H3("Multi-Asset Trading Explorer"),
    dcc.Dropdown(id="asset-dropdown", options=[{"label": n, "value": n} for n in asset_names], value=asset_names[0]),
    dcc.Slider(id="short-window", min=5, max=60, step=1, value=20),
    dcc.Slider(id="long-window", min=10, max=200, step=1, value=50),
    dcc.Graph(id="price-plot"),
    dcc.Graph(id="equity-plot")
])

@app.callback(
    Output("price-plot", "figure"),
    Output("equity-plot", "figure"),
    Input("asset-dropdown", "value"),
    Input("short-window", "value"),
    Input("long-window", "value"),
)
def update(asset, short, long):
    fig_price = plot_price_timeseries(dates, prices, asset_names, title="Prices (all assets)")
    # compute signals using cross-sectional SMA applied to selected asset or all
    if asset in asset_names:
        idx = asset_names.index(asset)
        sig = simple_moving_average_signals(prices[:, idx], short, long)[:, None]
        returns = np.concatenate(([0.0], (prices[1:, idx] / prices[:-1, idx] - 1.0)))[:, None]
    else:
        N = prices.shape[1]
        sig = np.zeros_like(prices, dtype=int)
        returns = np.zeros_like(prices, dtype=float)
        for j in range(N):
            sig[:, j] = simple_moving_average_signals(prices[:, j], short, long)
            returns[:, j] = np.concatenate(([0.0], (prices[1:, j] / prices[:-1, j] - 1.0)))
    equity, tot, sharpe = vector_backtest(sig, returns, transaction_cost=0.0005)
    fig_equity = plot_equity_curve(dates, equity, title=f"Equity curve (Sharpe {sharpe:.2f})")
    return fig_price, fig_equity

if __name__ == "__main__":
    app.run_server(debug=True, port=8050)
