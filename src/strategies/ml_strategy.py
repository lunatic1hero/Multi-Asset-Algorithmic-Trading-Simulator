# file: src/strategies/ml_strategy.py
from __future__ import annotations
import numpy as np
from typing import Callable

def ml_signals(feature_matrix: np.ndarray, model_predict: Callable[[np.ndarray], np.ndarray]) -> np.ndarray:
    """
    feature_matrix: (T, F)
    model_predict: function that takes (batch_of_features) and returns numeric predictions
    Returns discretized signals based on predicted returns: 1 long, -1 short, 0 flat
    """
    preds = model_predict(feature_matrix)
    signals = np.where(preds > 0.001, 1, np.where(preds < -0.001, -1, 0))
    return signals
