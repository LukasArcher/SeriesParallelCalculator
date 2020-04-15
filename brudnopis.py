from best_possibility import FindTheBestPossibility


class CapCalculator:
    @staticmethod
    def cap_calculator(cap_basic_power: float, cap_target: float, precision: float) -> str:
        error_abs = 0
        parallel_caps = 0
        parallel_caps_float = cap_target // cap_basic_power

        # ----------------------------------------------------------------------------- #
        # print(f"This is parallel capacitors in float: {parallel_caps_float}")
        # ----------------------------------------------------------------------------- #

        fewer_parallel_caps = parallel_caps
        more_parallel_caps = parallel_caps + 1
        less_parallel_prec = abs(parallel_caps_float - fewer_parallel_caps)
        more_parallel_prec = abs(parallel_caps_float - more_parallel_caps)

        if less_parallel_prec <= more_parallel_prec:
            error_abs = abs(cap_target - (fewer_parallel_caps * cap_basic_power))
            parallel_caps = fewer_parallel_caps
        elif more_parallel_prec < less_parallel_prec:
            error_abs = abs(cap_target - (more_parallel_caps * cap_basic_power))
            parallel_caps = more_parallel_caps
        error_relative = error_abs/cap_target
        error_percent = error_relative * 100

        # ----------------------------------------------------------------------------- #
        # print(f"This is the error_relative: {error_relative}")
        # print(f"This is the error_percent: {error_percent}")
        # ----------------------------------------------------------------------------- #

        if error_percent <= precision and parallel_caps > 0:
            print(f"Number of parallel capacitors needed:\n{parallel_caps}")
            return f'With all these capacitors you will get:\n{parallel_caps * cap_basic_power} F'
        else:
            find_the_best_possibility = FindTheBestPossibility()
            """we choose fewer_parallel_caps to be able to reach our target with serial caps"""
            parallel_caps_power = fewer_parallel_caps * cap_basic_power
            num_of_serial_cap = 2
            serial_caps = []
            list_of_possibilities = []
            while True:

                final_power = cap_basic_power / num_of_serial_cap + parallel_caps_power

                for n in serial_caps:
                    final_power += cap_basic_power / n
                error_abs = abs(cap_target - final_power)
                error_relative = error_abs / cap_target
                error_percent = error_relative * 100

                # ----------------------------------------------------------------------------- #
                # print(f"This is the trial power: {final_power}")
                # print(f"This is the error_relative: {error_relative}")
                # print(f"This is the error_percent: {error_percent}")
                # ----------------------------------------------------------------------------- #

                if error_percent <= precision:
                    serial_caps.append(num_of_serial_cap)
                    fewer_parallel_caps, serial_caps = find_the_best_possibility.best_possibility(cap_basic_power, cap_target, precision, fewer_parallel_caps, serial_caps)
                    final_power = fewer_parallel_caps * cap_basic_power
                    for n in serial_caps:
                        final_power += cap_basic_power / n

                    print(f"Parallel capacitors:\n{fewer_parallel_caps}")
                    for i in range(len(serial_caps)):
                        print(f"Serial capacitors in the row number {i + 1}:\n{serial_caps[i]}")
                    return f'With all these capacitors you will get:\n{final_power} F'
                else:
                    if final_power > cap_target:
                        num_of_serial_cap += 1
                    else:
                        serial_caps.append(num_of_serial_cap)
                        num_of_serial_cap += 1


if __name__ == '__main__':
    calc = CapCalculator()
    print(calc.cap_calculator(39.3, 5.8, 1))


