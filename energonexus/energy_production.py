import random

class EnergyProduction:
    def __init__(self):
        self.production_sources = ['solar', 'wind', 'hydro']

    def simulate_production(self, source, amount):
        # simulate energy production from a given source
        if source in self.production_sources:
            production_amount = random.uniform(0, amount)
            return production_amount
        else:
            return 0

    def get_production_sources(self):
        return self.production_sources
