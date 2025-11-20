import joblib
import pandas as pd

class HeartRiskModel:
    def __init__(self, path="heart_risk_model.pkl"):
        try:
            self.model = joblib.load(path)
        except Exception as e:
            raise RuntimeError(f"Ошибка загрузки модели: {e}")

    def predict(self, data: dict) -> int:
        X = pd.DataFrame([data])
        pred = self.model.predict(X)[0]
        return int(pred)

    def predict_csv(self, df: pd.DataFrame):
        preds = self.model.predict(df)
        return preds.astype(int)
