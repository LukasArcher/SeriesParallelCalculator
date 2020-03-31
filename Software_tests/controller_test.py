import unittest
from controller import Controller
from interface import CapInput
from commands_interpreter import CapCalculator
from unittest.mock import Mock


class ControllerTest(unittest.TestCase):
    def setUp(self) -> None:
        self.controller = Controller()

    def test_run(self):
        with unittest.mock.patch.object(CapInput, "cap_input", return_value=(1, 1, 1)):
            with unittest.mock.patch.object(CapCalculator, "cap_calculator", return_value=1):
                with unittest.mock.patch.object(CapInput, "next_calculation", return_value="NO"):
                    with unittest.mock.patch.object(CapInput, "goodbye", return_value="TEST") as mock_input:
                        result = self.controller.run()
                        self.assertEqual(result, "TEST")
                        mock_input.assert_called_with()

    def test_run_next_calc_error(self):
        with unittest.mock.patch.object(CapInput, "cap_input", return_value=(1, 1, 1)):
            with unittest.mock.patch.object(CapCalculator, "cap_calculator", return_value=1):
                with unittest.mock.patch.object(CapInput, "next_calculation", return_value="ERROR"):
                    with unittest.mock.patch.object(CapInput, "goodbye", return_value="TEST") as mock_input:
                        result = self.controller.run()
                        self.assertEqual(result, "TEST")
                        mock_input.assert_called_with()

    def test_run_wrong_command_which_is_zero(self):
        with unittest.mock.patch.object(CapInput, "cap_input", return_value=(0, 1, 1)):
            with unittest.mock.patch.object(CapCalculator, "cap_calculator", return_value=1):
                with unittest.mock.patch.object(CapInput, "goodbye", return_value="TEST") as mock_input:
                    result = self.controller.run()
                    self.assertEqual(result, "TEST")
                    mock_input.assert_called_with()

    def test_run_value_error(self):
        with self.assertRaises(TypeError):
            with unittest.mock.patch.object(CapInput, "cap_input", return_value=("ERROR", 1, 1)):
                self.controller.run()
        with self.assertRaisesRegex(TypeError, "'<=' not supported between instances of 'str' and 'int'"):
            with unittest.mock.patch.object(CapInput, "cap_input", return_value=("ERROR", 1, 1)):
                self.controller.run()


if __name__ == '__main__':
    unittest.main()
