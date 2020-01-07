# A perfect number is a number for which the sum of its proper divisors is exactly equal to the number.
# For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.
#
# A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.
#
# As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16,
# the smallest number that can be written as the sum of two abundant numbers is 24.
#
# By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers.
#
# However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number
# that cannot be expressed as the sum of two abundant numbers is less than this limit.
#
# Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.


def get_sum_of_divisors(num):
    i = 1
    result = 0

    while i < num and result <= num:

        if num % i == 0:
            result += i

        i += 1

    return result


def is_abundant(num):
    sum_of_divisors = get_sum_of_divisors(num)

    if sum_of_divisors > num:
        return True

    return False


def get_list_of_abundant():
    num = 12
    abundant_list = []

    while num <= 28123:

        if is_abundant(num):
            abundant_list.append(num)

        num += 1

    return abundant_list


def get_sum_of_numbers_that_are_not_sum_of_2_abundant():
    result = 0
    list_of_abundant = get_list_of_abundant()
    length = len(list_of_abundant)
    num = 1

    while num <= 28123:

        i = 0
        number_to_add = num

        while i < length:

            first_num = list_of_abundant[i]
            second_num = num - first_num

            if second_num in list_of_abundant:
                number_to_add = 0
                break

            i += 1

        result += number_to_add
        num += 1

    print(result)
    return result


get_sum_of_numbers_that_are_not_sum_of_2_abundant()
