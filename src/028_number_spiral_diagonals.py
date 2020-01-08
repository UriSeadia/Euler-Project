# Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:
#
# 21 22 23 24 25
# 20  7  8  9 10
# 19  6  1  2 11
# 18  5  4  3 12
# 17 16 15 14 13
#
# It can be verified that the sum of the numbers on the diagonals is 101.
#
# What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?

import time


def get_sum_of_diagonals(max_width: int):
    start = time.time()

    sum_of_diagonals = 1
    current_number = 1
    jump = 2

    while jump < max_width:
        i = 0

        while i < 4:
            current_number += jump
            sum_of_diagonals += current_number
            i += 1

        jump += 2

    print(sum_of_diagonals)

    end = time.time()
    print('Calculated in ' + str(end - start) + ' seconds.')


get_sum_of_diagonals(1001)


def get_sum_of_diagonals_1():
    start = time.time()

    numbers = [1]

    for k in range(2, 1001, 2):
        for i in range(1, 5):
            numbers.append(numbers[-1] + k)

    print(sum(numbers))

    end = time.time()
    print('Calculated in ' + str(end - start) + ' seconds.')


get_sum_of_diagonals_1()
