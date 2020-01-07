# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

import math
import time


# lcm - Least common multiple
def lcm(a: int, b: int):
    return int(a * b / math.gcd(a, b))  # math.gcd - greatest common divisor of 2 numbers


def smallest_multiples(higher: int):
    num = 1

    for i in range(2, higher + 1):
        num = lcm(num, i)

    return num


def main():
    start = time.time()

    print('result:', smallest_multiples(20))

    end = time.time()
    print('milliseconds: ' + str((end - start) * 1000))


main()


# def is_divisible_by_all_numbers(number_to_check: int, max_number_for_divide: int):
#     result = True
#     number_for_divide = 2
#
#     while result and number_for_divide <= max_number_for_divide:
#         if number_to_check % number_for_divide == 0:
#             number_for_divide += 1
#         else:
#             result = False
#
#     return result
#
#
# def find_smallest_divisible_by_all_numbers(max_number_for_divide: int):
#     result = max_number_for_divide
#     is_divisible = False
#
#     while is_divisible is False:
#         result += 1
#         is_divisible = is_divisible_by_all_numbers(result, max_number_for_divide)
#
#     return result
