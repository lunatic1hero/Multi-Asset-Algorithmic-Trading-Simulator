# file: src/utils.py
from __future__ import annotations
import plotly.graph_objects as go
import numpy as np
from typing import Iterable, Sequence

def plot_price_timeseries(dates: Sequence, prices: np.ndarray, asset_names: Sequence[str], title="Price Series"):
    fig = go.Figure()
    for idx, name in enumerate(asset_names):
        fig.add_trace(go.Scatter(x=dates, y=prices[:, idx], name=name))
    fig.update_layout(title=title, xaxis_title="Date", yaxis_title="Price")
    return fig

def plot_equity_curve(dates: Sequence, equity: Iterable[float], title="Equity Curve"):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=dates, y=list(equity), name="Equity"))
    fig.update_layout(title=title, xaxis_title="Date", yaxis_title="Portfolio Value")
    return fig
