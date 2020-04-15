import unittest
from interface import CapInput
from unittest.mock import patch


class InterfaceTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.cap_input = CapInput()

    # @patch('interface.CapInput.cap_input', side_effect=[1.0, 2.0, 3.0])
    # def test_input(self, mock_input):
    #     assert mock_input() == 1.0
    #
    #     assert mock_input() == 2.0
    #
    #     assert mock_input() == 3.0
    #
    # @patch('builtins.input', side_effect=[1.0, 2.0, 3.0])
    # def test_input2(self, mock_input):
    #     assert mock_input() == 1.0
    #     assert mock_input() == 2.0
    #     assert mock_input() == 3.0
    #
    # def test_input3(self):
    #     with patch('builtins.input', side_effect=[1.0, 2.0, 3.0]):
    #         result = self.cap_input.cap_input()
    #
    #         assert result[0] == 1.0
    #         assert result[1] == 2.0
    #         assert result[2] == 3.0

    def test_cap_input(self):
        with patch('builtins.input', return_value=1.0):
            cap_basic, cap_target, precision = self.cap_input.cap_input()

            assert cap_basic == 1.0
            assert cap_target == 1.0
            assert precision == 1.0

    def test_next_calculation(self):
        with patch('builtins.input', return_value='no'):
            next_calc = self.cap_input.next_calculation()
            assert next_calc == "NO"

    def test_goodbye(self):
        result = self.cap_input.goodbye()
        assert result == 'Fuck off then!'


if __name__ == '__main__':
    unittest.main()
