# file: src/data/loader.py
from __future__ import annotations
import pandas as pd
import numpy as np
from dataclasses import dataclass
from typing import List, Tuple

@dataclass
class MarketDataLoader:
    csv_path: str
    date_col: str = "date"

    def load(self) -> pd.DataFrame:
        """Loads CSV with a date column and multiple asset price columns."""
        df = pd.read_csv(self.csv_path, parse_dates=[self.date_col])
        df = df.sort_values(self.date_col).reset_index(drop=True)
        return df

    def price_matrix(self, df: pd.DataFrame) -> Tuple[pd.DatetimeIndex, List[str], np.ndarray]:
        """Return (dates, asset_names, prices_matrix) with shape (T, N)"""
        asset_cols = [c for c in df.columns if c != self.date_col]
        prices = df[asset_cols].astype(float).values
        return pd.DatetimeIndex(df[self.date_col]), asset_cols, prices

    def returns_matrix(self, df: pd.DataFrame, log: bool = True) -> np.ndarray:
        _, _, prices = self.price_matrix(df)
        if log:
            return np.diff(np.log(prices), axis=0)
        else:
            return np.diff(prices, axis=0) / prices[:-1]
