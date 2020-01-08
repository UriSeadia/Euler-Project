# Surprisingly there are only 3 numbers that can be written as the sum of 4th powers of their digits:
#
# 1634 =  1 ^ 4  +  6 ^ 4  +  3 ^ 4  +  4 ^ 4
# 8208 =  8 ^ 4  +  2 ^ 4  +  0 ^ 4  +  8 ^ 4
# 9474 =  9 ^ 4  +  4 ^ 4  +  7 ^ 4  +  4 ^ 4

# As 1 = 1 ^ 4 is not a sum it is not included.
#
# The sum of these numbers is 1634 + 8208 + 9474 = 19316.
#
# Find the sum of all the numbers that can be written as the sum of 5th powers of their digits.

import time


def get_sum_of_list(numbers_list: list):
    sum_of_list = 0

    for item in numbers_list:
        sum_of_list += item

    return sum_of_list


def get_list_of_fifth_power_of_digits(number: int):
    numbers_list = []

    while number > 0:
        digit = number % 10
        list_item = digit ** 5
        numbers_list.append(list_item)
        number = number // 10

    return numbers_list


def get_list_of_numbers_that_can_be_written_as_fifth_power_of_their_digits():
    current_number = 10
    result_list = []

    while current_number < 200000:
        list_of_fifth_power_of_digits = get_list_of_fifth_power_of_digits(current_number)
        sum_of_list = get_sum_of_list(list_of_fifth_power_of_digits)

        if sum_of_list == current_number:
            result_list.append(current_number)

        current_number += 1

    return result_list


def get_sum_of_numbers_that_can_be_written_as_fifth_power_of_their_digits():
    start = time.time()

    result_list = get_list_of_numbers_that_can_be_written_as_fifth_power_of_their_digits()
    result_sum = get_sum_of_list(result_list)

    end = time.time()

    print(result_sum)
    print('Calculated in ' + str(end - start) + ' seconds.')

    return result_sum


get_sum_of_numbers_that_can_be_written_as_fifth_power_of_their_digits()


# Other solutions (My is better...)
def dig_fifth_powers_1():
    start = time.time()

    result = sum([n for n in range(10, 200000) if sum([int(d)**5 for d in str(n)]) == n])
    print(result)

    end = time.time()
    print('Calculated in ' + str(end - start) + ' seconds.')


def dig_fifth_powers_2():
    start = time.time()

    nums = []

    for num in range(10, 200000):
        num_as_string = str(num)
        digits_sum = 0

        for j in num_as_string:
            digits_sum += int(j) ** 5

        if digits_sum == int(num_as_string):
            nums.append(int(num_as_string))

    result = 0

    for num in nums:
        result += num

    end = time.time()

    print(result)
    print('Calculated in ' + str(end - start) + ' seconds.')


dig_fifth_powers_1()
dig_fifth_powers_2()
