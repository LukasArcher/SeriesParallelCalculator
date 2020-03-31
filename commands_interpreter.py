import math


class CapCalculator:
    @staticmethod
    def cap_calculator(cap_basic_power: float, cap_target: float, precision: float) -> str:
        error_abs = 0
        parallel_caps = 0
        parallel_caps_float = cap_target / cap_basic_power

        # ----------------------------------------------------------------------------- #
        # print(f"This is parallel capacitors in float: {parallel_caps_float}")
        # ----------------------------------------------------------------------------- #

        less_parallel_caps = math.floor(parallel_caps_float)
        more_parallel_caps = math.floor(parallel_caps_float) + 1
        less_parallel_prec = abs(parallel_caps_float - less_parallel_caps)
        more_parallel_prec = abs(parallel_caps_float - more_parallel_caps)

        if less_parallel_prec <= more_parallel_prec:
            error_abs = abs(cap_target - (less_parallel_caps * cap_basic_power))
            parallel_caps = less_parallel_caps
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
            """we choose less_parallel_caps to be able to reach our target with serial caps"""
            parallel_caps_power = less_parallel_caps * cap_basic_power
            num_of_serial_cap = 2
            serial_caps = []
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
                    print(f"Parallel capacitors:\n{parallel_caps}")
                    for i in range(len(serial_caps)):
                        print(f"Serial capacitors in the row number {i+1}:\n{serial_caps[i]}")
                    return f'With all these capacitors you will get:\n{final_power} F'
                else:
                    if final_power > cap_target:
                        num_of_serial_cap += 1
                    else:
                        serial_caps.append(num_of_serial_cap)
                        num_of_serial_cap += 1








