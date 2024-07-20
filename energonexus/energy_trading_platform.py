import pyenergy
import matplotlib.pyplot as plt

class EnergyTradingPlatform:
    def __init__(self):
        self.pi_nodes = []  # list of Pi Node objects
        self.energy_prices = {}  # dictionary of energy prices by node
        self.energy_trades = []  # list of energy trades

    def add_pi_node(self, node):
        self.pi_nodes.append(node)

    def set_energy_price(self, node, price):
        self.energy_prices[node] = price

    def trade_energy(self, buyer, seller, amount):
        # logic for trading energy between buyer and seller nodes
        if buyer in self.pi_nodes and seller in self.pi_nodes:
            if self.energy_prices[buyer] > self.energy_prices[seller]:
                # buyer wants to buy energy from seller
                self.energy_trades.append((buyer, seller, amount))
                self.pi_nodes[buyer].energy_level -= amount
                self.pi_nodes[seller].energy_level += amount
            else:
                # seller wants to sell energy to buyer
                self.energy_trades.append((seller, buyer, amount))
                self.pi_nodes[seller].energy_level -= amount
                self.pi_nodes[buyer].energy_level += amount
        else:
            print("Error: Node not found")

    def visualize_energy_trading(self):
        # use Matplotlib to visualize energy trading between nodes
        plt.plot(self.pi_nodes, self.energy_prices)
        plt.xlabel('Pi Node')
        plt.ylabel('Energy Price')
        plt.title('Energy Trading Platform')
        plt.show()

    def get_energy_trades(self):
        return self.energy_trades

class PiNode:
    def __init__(self, name, energy_level):
        self.name = name
        self.energy_level = energy_level

    def __str__(self):
        return f"Pi Node {self.name} - Energy Level: {self.energy_level}"
