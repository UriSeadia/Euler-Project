# Euler discovered the remarkable quadratic formula:
# n ^ 2 + n + 41

# It turns out that the formula will produce 40 primes for the consecutive integer values 0 ≤ n ≤39.
# However, when n = 40, 40 ^ 2 + 40 + 41 = 40(40 + 1) + 41 is divisible by 41,
# and certainly when n = 41, 41 ^ 2 + 41 + 41 is clearly divisible by 41.
#
# The incredible formula n ^ 2 − 79n + 1601 was discovered, which produces 80 primes for the consecutive values 0 ≤n ≤ 79.
# The product of the coefficients, −79 and 1601, is −126479.
#
# Considering quadratics of the form:
# n ^ 2 + an + b, where |a| < 1000 and |b| ≤ 1000
# where |n| is the modulus/absolute value of n
# e.g. |11| = 11 and |−4| = 4
#
# Find the product of the coefficients, a and b,
# for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n = 0.

import time


def get_absolute_value(number):
    return abs(number)


def is_prime(number):

    if number <= 1:
        return False

    if number <= 3:
        return True

    if number % 2 == 0 or number % 3 == 0:
        return False

    i = 5

    while i * i <= number:
        if (number % i == 0) or (number % (i + 2) == 0):
            return False

        i = i + 6

    return True


def get_quadratic_expression_result(a, b, n):
    return (n ** 2) + (a * n) + b


# a between -999 and 999, b between -1000 and 1000
def get_result(a_max, b_max):
    a = -a_max
    b = 0
    n = 0
    max_consecutive_primes = 0
    max_product = 0

    while a <= a_max:
        while b <= b_max:
            if is_prime(b):
                quadratic_expression_result = get_quadratic_expression_result(a, b, n)

                if is_prime(quadratic_expression_result):
                    n += 1
                else:
                    if n > max_consecutive_primes:
                        max_consecutive_primes = n
                        max_product = a * b
                    n = 0
                    b += 1
            else:
                b += 1
        b = 0
        a += 1

    return max_product


def main():
    start = time.time()

    print('result:', get_result(999, 1000))

    end = time.time()
    print('Seconds: ' + str(end - start))


if __name__ == '__main__':
    main()
else:
    print('__name__ is', __name__)
