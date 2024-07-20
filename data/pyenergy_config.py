class PyEnergyConfig:
    def __init__(self):
        self.config = self.load_config()

    def load_config(self):
        with open('config.json', 'r') as f:
            return json.load(f)

    def get_energy_production_config(self):
        return self.config['energy_production']

    def get_energy_consumption_config(self):
        return self.config['energy_consumption']

    def get_energy_storage_config(self):
        return self.config['energy_storage']

    def get_visualization_config(self):
        return self.config['visualization']

    def get_blockchain_config(self):
        return self.config['blockchain']
