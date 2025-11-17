# file: data/sample_generator.py
# Run this to create data/sample_multi_asset.csv
import pandas as pd
import numpy as np
from datetime import datetime
np.random.seed(123)

dates = pd.date_range(start="2018-01-01", end="2024-12-31", freq="B")  # business days
# pick 8 assets: 3 equities, 2 FX, 3 futures-like
asset_names = ["EQ_A", "EQ_B", "EQ_C", "FX_USD_EUR", "FX_USD_JPY", "FUT_OIL", "FUT_GOLD", "FUT_SPX"]
n = len(asset_names)

rows = []
prices = np.zeros((len(dates), n))
# initialize base prices
base = np.array([100.0, 80.0, 60.0, 1.0, 110.0, 50.0, 1200.0, 3000.0])
vol = np.array([0.02, 0.015, 0.025, 0.003, 0.004, 0.03, 0.01, 0.02])

for t in range(len(dates)):
    if t == 0:
        prices[t] = base
    else:
        shock = np.random.normal(scale=vol)
        prices[t] = prices[t-1] * (1 + shock)
df = pd.DataFrame(prices, columns=asset_names)
df.insert(0, "date", dates.strftime("%Y-%m-%d"))
df.to_csv("data/sample_multi_asset.csv", index=False)
print("Saved data/sample_multi_asset.csv")
