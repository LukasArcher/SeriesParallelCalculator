import unittest
from commands_interpreter import CapCalculator


class CommandInterpreterTest(unittest.TestCase):
    def setUp(self) -> None:
        self.cap_calculator = CapCalculator()

    def test_cap_calculator(self):
        result = self.cap_calculator.cap_calculator(4, 103, 0.1)
        self.assertEqual(result, 'With all these capacitors you will get:\n103.0 F')
