class FindTheBestPossibility:
    @staticmethod
    def best_possibility(cap_basic_power: float, cap_target: float, precision: float, original_parallel_caps, original_serial_caps: list):

        parallel_caps_power = original_parallel_caps * cap_basic_power
        counter = 1
        num_of_serial_cap = original_serial_caps[0] + counter
        serial_caps = [num_of_serial_cap]
        list_of_possibilities = [original_serial_caps]
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
                list_of_possibilities.append(serial_caps)
                if original_serial_caps[-1] // 2 <= serial_caps[0]:
                    sum_list = []
                    result = 0
                    for l in list_of_possibilities:
                        sum_list.append(sum(l))
                    for i in range(len(sum_list)):
                        if sum_list[i] < sum_list[result]:
                            result = i
                    result = list_of_possibilities[result]
                    return original_parallel_caps, result

                counter += 1
                num_of_serial_cap = original_serial_caps[0] + counter
                serial_caps = [num_of_serial_cap]
                num_of_serial_cap = 2

            else:
                if final_power > cap_target:
                    num_of_serial_cap += 1
                else:

                    serial_caps.append(num_of_serial_cap)
                    num_of_serial_cap += 1

        # count_subtracted_parallels = 1
        # fewer_parallel_caps = original_parallel_caps
        # while fewer_parallel_caps > 0:
        #     fewer_parallel_caps -= 1
        #
        #     parallel_caps_power = fewer_parallel_caps * cap_basic_power
        #     counter = 1
        #     num_of_serial_cap = counter
        #     serial_caps = [num_of_serial_cap]
        #     list_of_possibilities = []
        #     while True:
        #         final_power = cap_basic_power / num_of_serial_cap + parallel_caps_power
        #
        #         for n in serial_caps:
        #             final_power += cap_basic_power / n
        #         error_abs = abs(cap_target - final_power)
        #         error_relative = error_abs / cap_target
        #         error_percent = error_relative * 100
        #
        #         # ----------------------------------------------------------------------------- #
        #         # print(f"This is the trial power: {final_power}")
        #         # print(f"This is the error_relative: {error_relative}")
        #         # print(f"This is the error_percent: {error_percent}")
        #         # ----------------------------------------------------------------------------- #
        #
        #         if error_percent <= precision:
        #             serial_caps.append(num_of_serial_cap)
        #             list_of_possibilities.append(serial_caps)
        #             if original_serial_caps[-1] <= serial_caps[0]:
        #                 sum_list = []
        #                 result_2 = 0
        #                 for l in list_of_possibilities:
        #                     sum_list.append(sum(l))
        #                     print(fewer_parallel_caps, l)
        #                     print()
        #                 for i in range(len(sum_list)):
        #                     if sum_list[i] < sum_list[result_2]:
        #                         result_2 = i
        #                 result_2 = list_of_possibilities[result_2]
        #                 if sum(result_2) < sum(result) + count_subtracted_parallels:
        #                     result = result_2
        #                     original_parallel_caps = fewer_parallel_caps
        #                     count_subtracted_parallels += 1
        #                 break
        #
        #             counter += 1
        #             num_of_serial_cap = counter
        #             serial_caps = []
        #             # num_of_serial_cap = 2
        #
        #         else:
        #             if final_power > cap_target:
        #                 num_of_serial_cap += 1
        #             else:
        #
        #                 serial_caps.append(num_of_serial_cap)
        #                 num_of_serial_cap += 1
        # return original_parallel_caps, result


if __name__ == '__main__':
    test_calc = FindTheBestPossibility()
    print(test_calc.best_possibility(39.3, 5.8, 1, 0, [7, 162]))
