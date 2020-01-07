# 2 ** 15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
#
# What is the sum of the digits of the number 2 ** 1000?

# print(2 ** 1000)


def get_power_digit_sum(num):
    num_as_str = str(num)
    sum_of_digits = 0

    for char in num_as_str:
        digit = int(char)
        sum_of_digits += digit

    print(sum_of_digits)
    return sum_of_digits


get_power_digit_sum(2 ** 1000)
