# file: tests/test_loader.py
import pandas as pd
from src.data.loader import MarketDataLoader
import tempfile, os

def test_load_and_matrix():
    df = pd.DataFrame({
        "date": ["2020-01-01", "2020-01-02"],
        "A": [1.0, 1.1],
        "B": [2.0, 2.1]
    })
    fn = tempfile.NamedTemporaryFile(delete=False, suffix=".csv")
    try:
        df.to_csv(fn.name, index=False)
        loader = MarketDataLoader(fn.name)
        d = loader.load()
        dates, cols, m = loader.price_matrix(d)
        assert m.shape == (2,2)
        assert len(cols) == 2
    finally:
        os.unlink(fn.name)
