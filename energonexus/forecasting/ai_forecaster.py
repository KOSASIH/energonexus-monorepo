import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense

class AIForecaster:
    def __init__(self, data_path, model_type='random_forest'):
        self.data_path = data_path
        self.model_type = model_type
        self.data = pd.read_csv(data_path)
        self.X = self.data.drop(['energy_consumption'], axis=1)
        self.y = self.data['energy_consumption']

    def preprocess_data(self):
        self.X = pd.get_dummies(self.X, columns=['season', 'day_of_week'])
        self.X = self.X.fillna(self.X.mean())
        self.y = self.y.fillna(self.y.mean())

    def train_model(self):
        if self.model_type == 'random_forest':
            X_train, X_test, y_train, y_test = train_test_split(self.X, self.y, test_size=0.2, random_state=42)
            self.model = RandomForestRegressor(n_estimators=100, random_state=42)
            self.model.fit(X_train, y_train)
            y_pred = self.model.predict(X_test)
            print(f'RMSE: {mean_squared_error(y_test, y_pred, squared=False)}')
        elif self.model_type == 'lstm':
            self.model = Sequential()
            self.model.add(LSTM(units=50, return_sequences=True, input_shape=(self.X.shape[1], 1)))
            self.model.add(LSTM(units=50))
            self.model.add(Dense(1))
            self.model.compile(loss='mean_squared_error', optimizer='adam')
            self.model.fit(self.X, self.y, epochs=50, batch_size=32, validation_split=0.2)

    def forecast(self, input_data):
        if self.model_type == 'random_forest':
            return self.model.predict(input_data)
        elif self.model_type == 'lstm':
            return self.model.predict(input_data)

if __name__ == '__main__':
    forecaster = AIForecaster('energy_data.csv', model_type='lstm')
    forecaster.preprocess_data()
    forecaster.train_model()
    input_data = pd.DataFrame({'temperature': [25, 26, 27], 'humidity': [60, 61, 62]})
    forecast = forecaster.forecast(input_data)
    print(f'Forecasted energy consumption: {forecast}')
