import joblib
import pandas as pd # noqa
import numpy as np # noqa
from pathlib import Path


class PredictionPipeline:
    def __init__(self):
        self.model = joblib.load(Path('artifacts/model_trainer/model.joblib'))

    def predict(self, data):
        prediction = self.model.predict(data)

        return prediction
