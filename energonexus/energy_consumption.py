import random

class EnergyConsumption:
    def __init__(self):
        self.consumption_devices = ['home', 'business', 'industry']

    def simulate_consumption(self, device, amount):
        # simulate energy consumption by a given device
        if device in self.consumption_devices:
            consumption_amount = random.uniform(0, amount)
            return consumption_amount
        else:
            return 0

    def get_consumption_devices(self):
        return self.consumption_devices
