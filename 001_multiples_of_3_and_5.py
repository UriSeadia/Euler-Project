# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
# The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

import time


def get_sum_of_multiple(multiple: int, below_number: int):

    if multiple >= below_number:
        return 0

    result = 0
    number_to_add = multiple

    while number_to_add < below_number:
        result += number_to_add
        number_to_add += multiple

    return result


def find_sum_of_3_and_5_multiples(below_number: int):
    sum_of_five_multiple = get_sum_of_multiple(5, below_number)
    sum_of_three_multiple = get_sum_of_multiple(3, below_number)
    sum_of_fifteen_multiple = get_sum_of_multiple(15, below_number)
    result = sum_of_five_multiple + sum_of_three_multiple - sum_of_fifteen_multiple

    return result


def main():
    start = time.time()

    print('result:', find_sum_of_3_and_5_multiples(1000))

    end = time.time()
    print('Milliseconds: ' + str((end - start) * 1000))


main()

# one liner (my solution has better performance)
# print(sum([i for i in range(1, 1000) if i % 3 == 0 or i % 5 == 0]))
