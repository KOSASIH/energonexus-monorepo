import unittest
from energy_trading_platform import EnergyTradingPlatform, PiNode

class TestEnergyTradingPlatform(unittest.TestCase):
    def test_add_pi_node(self):
        platform = EnergyTradingPlatform()
        node = PiNode('Node 1', 100)
        platform.add_pi_node(node)
        self.assertIn(node, platform.pi_nodes)

    def test_set_energy_price(self):
        platform = EnergyTradingPlatform()
        node = PiNode('Node 1', 100)
        platform.add_pi_node(node)
        platform.set_energy_price(node, 10)
        self.assertEqual(platform.energy_prices[node], 10)

    def test_trade_energy(self):
        platform = EnergyTradingPlatform()
        buyer = PiNode('Buyer', 100)
        seller = PiNode('Seller', 100)
        platform.add_pi_node(buyer)
        platform.add_pi_node(seller)
        platform.set_energy_price(buyer, 10)
        platform.set_energy_price(seller, 5)
        platform.trade_energy(buyer, seller, 20)
        self.assertEqual(buyer.energy_level, 80)
        self.assertEqual(seller.energy_level, 120)

if __name__ == '__main__':
    unittest.main()
