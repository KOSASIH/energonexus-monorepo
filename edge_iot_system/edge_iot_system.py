# edge_iot_system.py
import esp32
import mqtt

# Set up ESP32 board
board = esp32.ESP32()

# Set up MQTT connection
mqtt_client = mqtt.Client()
mqtt_client.connect("localhost", 1883)

# Publish data to MQTT broker
mqtt_client.publish("energy/usage", "100W")
mqtt_client.publish("energy/production", "200W")
