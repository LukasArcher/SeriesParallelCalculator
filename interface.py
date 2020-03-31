from typing import Tuple


class CapInput:
    @staticmethod
    def cap_input() -> Tuple[float, float, float]:
        cap_basic = float(input("Put basic value of capacitor: "))
        cap_target = float(input("Put target value of capacitors: "))
        precision = float(input("Put precision in %: "))
        return cap_basic, cap_target, precision

    @staticmethod
    def next_calculation() -> str:
        next_calc = input("Would you like to calculate other capacitors? [Y/N] or [yes/no]: ").upper()
        return next_calc

    @staticmethod
    def goodbye() -> str:
        return 'Fuck off then!'
