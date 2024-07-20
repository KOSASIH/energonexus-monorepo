import java.util.ArrayList;
import java.util.List;

import org.eclipse.paho.client.mqttv3.IMqttClient;
import org.eclipse.paho.client.mqttv3.MqttClient;
import org.eclipse.paho.client.mqttv3.MqttException;
import org.eclipse.paho.client.mqttv3.persist.MemoryPersistence;

public class EnergyManager {
    private static final String MQTT_BROKER_URL = "tcp://localhost:1883";
    private static final String MQTT_CLIENT_ID = "energy_manager";
    private static final String MQTT_TOPIC = "energy/data";

    private IMqttClient mqttClient;
    private List<Device> devices;

    public EnergyManager() {
        devices = new ArrayList<>();
        try {
            mqttClient = new MqttClient(MQTT_BROKER_URL, MQTT_CLIENT_ID, new MemoryPersistence());
            mqttClient.connect();
            mqttClient.subscribe(MQTT_TOPIC);
        } catch (MqttException e) {
            System.out.println("Error connecting to MQTT broker: " + e.getMessage());
        }
    }

    public void addDevice(Device device) {
        devices.add(device);
    }

    public void removeDevice(Device device) {
        devices.remove(device);
    }

    public void processEnergyData(String energyData) {
        // Process energy data from IoT devices
        System.out.println("Received energy data: " + energyData);
        // Update device states and energy consumption data
    }

    public static void main(String[] args) {
        EnergyManager energyManager = new EnergyManager();
        energyManager.addDevice(new Device("device1", "living_room"));
        energyManager.addDevice(new Device("device2", "kitchen"));
    }
}

class Device {
    private String id;
    private String location;

    public Device(String id, String location) {
        this.id = id;
        this.location = location;
    }

    public String getId() {
        return id;
    }

    public String getLocation() {
        return location;
    }
}
