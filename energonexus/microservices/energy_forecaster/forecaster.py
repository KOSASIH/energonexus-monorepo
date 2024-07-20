import pandas as pd
from prophet import Prophet

class EnergyForecaster:
    def __init__(self):
        self.model = Prophet()

    def train(self, data: pd.DataFrame):
        self.model.fit(data)

    def forecast(self, future_days: int):
        future = self.model.make_future_dataframe(periods=future_days)
        forecast = self.model.predict(future)
        return forecast

energy_forecaster = EnergyForecaster()
