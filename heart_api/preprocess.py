import numpy as np
import re
from sklearn.base import BaseEstimator, TransformerMixin

class HeartDataPreprocessor(BaseEstimator, TransformerMixin):
    def __init__(self):

        self.lifestyle_cols = [
            "diabetes",
            "family_history",
            "smoking",
            "alcohol_consumption",
            "previous_heart_problems",
            "medication_use",
            "stress_level",
            "physical_activity_days_per_week"
        ]

        self.binary_cols = [
            "diabetes",
            "family_history",
            "smoking",
            "alcohol_consumption",
            "previous_heart_problems",
            "medication_use",
            "lifestyle_data_missing"
        ]

        self.data_leak_cols = ["ckmb", "troponin"]
        self.tech_cols = ["id", "unnamed_0"]

    def fit(self, X, y=None):
        return self

    def to_snake_case(self, df):
        df = df.copy()
        df.columns = [
            re.sub(r"[^a-z0-9_]", "",
                col.strip()
                   .replace(" ", "_")
                   .lower()
            )
            for col in df.columns
        ]
        return df

    def transform(self, X):
        X = X.copy()

        X = self.to_snake_case(X)

        X = X.drop(columns=self.tech_cols, errors="ignore")

        X = X.drop(columns=self.data_leak_cols, errors="ignore")

        X["gender"] = X["gender"].replace({"1.0": np.nan, "0.0": np.nan})
        X["gender"] = X["gender"].fillna("unknown")

        X["lifestyle_data_missing"] = X[self.lifestyle_cols].isna().all(axis=1).astype(int)

        X[self.lifestyle_cols] = X[self.lifestyle_cols].fillna(0)

        for col in self.binary_cols:
            if col in X.columns:
                X[col] = X[col].astype("int64")

        return X
