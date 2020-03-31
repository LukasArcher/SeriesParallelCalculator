import unittest
from interface import CapInput
from unittest.mock import Mock
from unittest.mock import patch
import interface

class InterfaceTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.cap_input = CapInput()

    # @patch('builtins.input', side_effect=[1.0, 2.0, 3.0])
    # def test_input(self, cap_input):
    #     cap_basic = cap_input()
    #     cap_target = cap_input()
    #     precision = cap_input()
    #     self.assertTrue(cap_basic == 1.0 and cap_target == 2.0 and precision == 3.0)

    @patch('interface.CapInput.input', side_effect=[1.0, 2.0, 3.0])
    def test_input(self, mock_choice):
        cap_basic = self.cap_input.cap_input()
        assert cap_basic == 1.0

        cap_target = self.cap_input.cap_input()
        assert cap_target == 2.0

        precision = self.cap_input.cap_input()
        assert precision == 3

