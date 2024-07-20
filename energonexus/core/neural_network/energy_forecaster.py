import pandas as pd
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense

class EnergyForecaster:
    def __init__(self):
        self.model = Sequential()
        self.model.add(LSTM(units=50, return_sequences=True, input_shape=(30, 1)))
        self.model.add(LSTM(units=50))
        self.model.add(Dense(1))
        self.model.compile(loss='mean_squared_error', optimizer='adam')

    def train(self, data: pd.DataFrame):
        X = data.drop(['energy_consumption'], axis=1)
        y = data['energy_consumption']
        self.model.fit(X, y, epochs=100, batch_size=32)

    def predict(self, data: pd.DataFrame):
        return self.model.predict(data)

energy_forecaster = EnergyForecaster()
