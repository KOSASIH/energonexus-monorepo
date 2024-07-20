# ai_model.py
import tensorflow as tf

# Define the AI model
model = tf.keras.models.Sequential([
  tf.keras.layers.Dense(64, activation="relu", input_shape=(1,)),
  tf.keras.layers.Dense(64, activation="relu"),
  tf.keras.layers.Dense(1)
])

# Compile the model
model.compile(optimizer="adam", loss="mean_squared_error")

# Train the model
model.fit(X_train, y_train, epochs=10)
