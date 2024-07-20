class EnergyStorage:
    def __init__(self):
        self.storage_devices = ['battery', 'capacitor']

    def simulate_storage(self, device, amount):
        # simulate energy storage using a given device
        if device in self.storage_devices:
            storage_amount = amount
            return storage_amount
        else:
            return 0

    def get_storage_devices(self):
        return self.storage_devices
