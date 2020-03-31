from interface import CapInput
from commands_interpreter import CapCalculator
from wrong_command import WrongCommand
import time

sleep_time = 1
error_limit = 3



class Controller:
    def __init__(self):
        self.interface = CapInput()
        self.cap_calc = CapCalculator()

    def run(self) -> str:
        do_input = True
        error_count = 0
        while True:
            if do_input:
                try:
                    cap_basic, cap_target, precision = self.interface.cap_input()
                    if cap_basic <= 0 or cap_target <= 0 or precision <= 0:
                        raise WrongCommand("Wrong command")
                    result = self.cap_calc.cap_calculator(cap_basic, cap_target, precision)
                    print(result)
                    error_count = 0
                except ValueError:
                    error_count += 1
                    print("Oh, come on man...you surely know that this is a wrong value!")
                    time.sleep(sleep_time)
                    if error_count >= error_limit:
                        break
                    continue

                except WrongCommand:
                    error_count += 1
                    print("Dude, are you fucking stupid?!")
                    print("Don't you know that all values have to be GREATER then zero?! Try again!")
                    time.sleep(sleep_time)
                    if error_count >= error_limit:
                        break
                    continue

            next_calculation = self.interface.next_calculation()
            try:
                if next_calculation == 'N' or next_calculation == 'NO':
                    break
                elif next_calculation != 'Y' and next_calculation != 'YES':
                    raise WrongCommand("Wrong command")
                do_input = True
            except WrongCommand:
                error_count += 1
                print("Are you a fucking retard?")
                time.sleep(sleep_time)
                do_input = False
                if error_count >= error_limit:
                    break
        return self.interface.goodbye()
