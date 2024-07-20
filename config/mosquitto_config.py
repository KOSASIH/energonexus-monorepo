# mosquitto_config.py
import mosquitto

# Set up MQTT broker
broker = mosquitto.Mosquitto()

# Configure broker settings
broker.username_pw_set("username", "password")
broker.connect("localhost", 1883)

# Subscribe to topics
broker.subscribe("energy/usage")
broker.subscribe("energy/production")

# Publish messages
broker.publish("energy/usage", "100W")
broker.publish("energy/production", "200W")
