import joblib
import numpy as np
from preprocess import HeartDataPreprocessor
import pandas as pd

class HeartRiskModel:
    def __init__(self, path: str = "heart_risk_model.pkl"):
        try:
            self.model = joblib.load(path)
        except Exception as e:
            raise RuntimeError(f"Ошибка загрузки модели: {e}")

    def predict(self, data: dict) -> int:
        """
        data — словарь с признаками ровно как в датасете.
        """
        X = pd.DataFrame([data])
        pred = self.model.predict(X)[0]
        return int(pred)

    def predict_proba(self, data: dict) -> float:
        X = pd.DataFrame([data])
        proba = self.model.predict_proba(X)[0][1]
        return float(proba)
