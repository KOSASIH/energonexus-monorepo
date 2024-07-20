import unittest
from energia_core import *

class TestEnergyConsumption(unittest.TestCase):
    def setUp(self):
        self.board = LaunchPadBoard()

    def test_led_current(self):
        self.board.init_board()
        self.board.write_digital_output(0, 1)  # Turn on LED
        current = self.board.read_analog_input(3)  # LED current pin
        self.assertAlmostEqual(current, 0.02, delta=0.005)  # Expected current: 20mA ± 5mA

    def test_motor_current(self):
        self.board.init_board()
        self.board.write_digital_output(1, 1)  # Turn on motor
        current = self.board.read_analog_input(4)  # Motor current pin
        self.assertAlmostEqual(current, 1.0, delta=0.1)  # Expected current: 1A ± 0.1A

    def test_energy_consumption(self):
        self.board.init_board()
        energy_consumption = self.board.read_analog_input(5)  # Energy consumption pin
        self.assertGreaterEqual(energy_consumption, 0)  # Energy consumption should be non-negative

if __name__ == '__main__':
    unittest.main()
