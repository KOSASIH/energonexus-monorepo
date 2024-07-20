import unittest
from energia_core import *

class TestEnergyStorage(unittest.TestCase):
    def setUp(self):
        self.board = LaunchPadBoard()

    def test_battery_voltage(self):
        self.board.init_board()
        voltage = self.board.read_analog_input(6)  # Battery voltage pin
        self.assertAlmostEqual(voltage, 12.0, delta=0.5)  # Expected voltage: 12V ± 0.5V

    def test_battery_state_of_charge(self):
        self.board.init_board()
        soc = self.board.read_analog_input(7)  # Battery state of charge pin
        self.assertGreaterEqual(soc, 0)  # State of charge should be non-negative
        self.assertLessEqual(soc, 100)  # State of charge should be less than or equal to 100%

    def test_energy_storage(self):
        self.board.init_board()
        energy_storage = self.board.read_analog_input(8)  # Energy storage pin
        self.assertGreaterEqual(energy_storage, 0)  # Energy storage should be non-negative

if __name__ == '__main__':
    unittest.main()
