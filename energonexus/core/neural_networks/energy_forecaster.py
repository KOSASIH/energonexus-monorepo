import pandas as pd
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense

class EnergyForecaster:
    def __init__(self):
        self.model = Sequential()
        self.model.add(LSTM(units=50, return_sequences=True, input_shape=(10, 1)))
        self.model.add(LSTM(units=50))
        self.model.add(Dense(1))
        self.model.compile(loss='mean_squared_error', optimizer='adam')

    def train(self, data: pd.DataFrame):
        self.model.fit(data, epochs=100, batch_size=32)

    def forecast(self, future_days: int):
        future_data = pd.DataFrame(index=range(future_days), columns=['energy_consumption'])
        for i in range(future_days):
            input_data = future_data.iloc[i-10:i].values.reshape((1, 10, 1))
            output = self.model.predict(input_data)
            future_data.iloc[i, 0] = output[0][0]
        return future_data

energy_forecaster = EnergyForecaster()
