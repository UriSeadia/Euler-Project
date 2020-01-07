# The sum of the squares of the first ten natural numbers is,
# 1 ^ 2 + 2 ^ 2 + ... + 10 ^ 2 = 385
#
# The square of the sum of the first ten natural numbers is,
# (1 + 2 + ... + 10) ^ 2 = 55 ^ 2 = 3025

# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is
# 3025 − 385 = 2640.
#
# Find the difference between the sum of the squares of the first 100 natural numbers and the square of the sum.

import time


def get_sum_of_squares(number: int):
    current_number = 1
    result = 0

    while current_number <= number:
        square_of_current = current_number * current_number
        result += square_of_current
        current_number += 1

    return result


def get_square_of_sum(number: int):
    number_to_add = 1
    result = 0

    while number_to_add <= number:
        result += number_to_add
        number_to_add += 1

    return result ** 2


def get_sum_square_difference(number: int):
    return get_square_of_sum(number) - get_sum_of_squares(number)


def main():
    start = time.time()

    print('result:', get_sum_square_difference(100))

    end = time.time()
    print('milliseconds: ' + (str((end - start) * 1000)))


main()
