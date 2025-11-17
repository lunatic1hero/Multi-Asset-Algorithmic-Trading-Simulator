# file: src/ml/model_wrapper.py
from __future__ import annotations
import numpy as np
from typing import Any, Callable, Optional
import joblib
from dataclasses import dataclass

@dataclass
class SklearnModelWrapper:
    model: Any

    def fit(self, X: np.ndarray, y: np.ndarray):
        self.model.fit(X, y)
        return self

    def predict(self, X: np.ndarray) -> np.ndarray:
        return self.model.predict(X)

    def save(self, path: str):
        joblib.dump(self.model, path)

    @classmethod
    def load(cls, path: str):
        m = joblib.load(path)
        return cls(model=m)
