import unittest
from energia_core import *

class TestEnergyProduction(unittest.TestCase):
    def setUp(self):
        self.board = LaunchPadBoard()

    def test_solar_panel_voltage(self):
        self.board.init_board()
        voltage = self.board.read_analog_input(0)  # Solar panel voltage pin
        self.assertAlmostEqual(voltage, 12.0, delta=0.5)  # Expected voltage: 12V ± 0.5V

    def test_wind_turbine_current(self):
        self.board.init_board()
        current = self.board.read_analog_input(1)  # Wind turbine current pin
        self.assertAlmostEqual(current, 5.0, delta=0.5)  # Expected current: 5A ± 0.5A

    def test_energy_production(self):
        self.board.init_board()
        energy_production = self.board.read_analog_input(2)  # Energy production pin
        self.assertGreaterEqual(energy_production, 0)  # Energy production should be non-negative

if __name__ == '__main__':
    unittest.main()
