# A permutation is an ordered arrangement of objects.
# For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4.

# If all of the permutations are listed numerically or alphabetically, we call it lexicographic order.

# The lexicographic permutations of 0, 1 and 2 are:
# 012   021   102   120   201   210
#
# What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?


def get_factorial(num):
    if num < 2:
        return 1

    return num * get_factorial(num - 1)


def convert_digits_list_to_number(digits_list):
    result = 0
    index = len(digits_list) - 1
    multi = 1

    while index >= 0:
        result += (digits_list[index] * multi)
        multi *= 10
        index -= 1

    return result


def get_millionth_permutation():
    remaining_from_million = 1000000
    digits = []
    remaining_digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    while len(remaining_digits) > 0:

        count_factorials = 0
        num_of_remaining_digits = len(remaining_digits) - 1
        factorial = get_factorial(num_of_remaining_digits)

        while True:

            if (remaining_from_million - factorial) > 0:
                remaining_from_million -= factorial
                count_factorials += 1
            else:
                break

        digits.append(remaining_digits[count_factorials])
        remaining_digits.pop(count_factorials)

    result = convert_digits_list_to_number(digits)

    print(result)
    return result


get_millionth_permutation()
