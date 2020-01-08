# 145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
#
# Find the sum of all numbers which are equal to the sum of the factorial of their digits.
#
# Note: as 1! = 1 and 2! = 2 are not sums they are not included.

import time


def get_factorial(num):
    if num <= 1:
        return 1

    return num * get_factorial(num - 1)


def digit_factorials():
    result = 0

    for num in range(3, 100000):
        product = 0

        for digit in str(num):
            product += get_factorial(int(digit))

        if product == num:
            result += product

    print(result)
    return result


def main():
    start = time.time()

    digit_factorials()

    end = time.time()
    print('Seconds: ' + str(end - start))


main()
