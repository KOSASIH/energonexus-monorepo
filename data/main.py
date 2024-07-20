import energy_trading_platform
import energy_production
import energy_consumption
import energy_storage
import visualization

def main():
    # create energy trading platform
    platform = energy_trading_platform.EnergyTradingPlatform()

    # create pi nodes
    node1 = energy_trading_platform.PiNode('Node 1', 100)
    node2 = energy_trading_platform.PiNode('Node 2', 100)

    # add pi nodes to platform
    platform.add_pi_node(node1)
    platform.add_pi_node(node2)

    # set energy prices
    platform.set_energy_price(node1, 10)
    platform.set_energy_price(node2, 5)

    # simulate energy production
    production = energy_production.EnergyProduction()
    production_amount = production.simulate_production('solar', 100)

    # simulate energy consumption
    consumption = energy_consumption.EnergyConsumption()
    consumption_amount = consumption.simulate_consumption('home', 50)

    # simulate energy storage
    storage = energy_storage.EnergyStorage()
    storage_amount = storage.simulate_storage('battery', 20)

    # trade energy
    platform.trade_energy(node1, node2, 20)

    # visualize energy trading
    visualization.visualize_energy_trading(platform.get_energy_trades())

if __name__ == '__main__':
    main()
