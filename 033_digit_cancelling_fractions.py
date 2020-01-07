# The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may
# incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.
#
# We shall consider fractions like, 30/50 = 3/5, to be trivial examples.
#
# There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.
#
# If the product of these four fractions is given in its lowest common terms, find the value of the denominator.

import time
import math


def lcm(a, b):
    result = int(a * b / math.gcd(a, b))  # math.gcd - greatest common divisor of 2 numbers
    print(result)
    return result


def digit_cancelling_fractions():
    numerators_product = 1
    denominators_product = 1

    for denominator in range(10, 100):
        for numerator in range(10, 100):
            if numerator >= denominator:
                break

            numerator_as_string = str(numerator)
            denominator_as_string = str(denominator)

            for digit_n in numerator_as_string:
                for digit_d in denominator_as_string:
                    if digit_n == digit_d and digit_n != '0':
                        x = numerator_as_string.replace(digit_n, "", 1)
                        y = denominator_as_string.replace(digit_d, "", 1)
                        product = numerator / denominator

                        if int(y) != 0 and float(x) / float(y) == product:
                            # print('product:' + str(product) + ' | numerator: ' + str(numerator) + ' | denominator: ' + str(denominator) + ' | x: ' + x + ' | y: ' + y)
                            numerators_product *= int(x)
                            denominators_product *= int(y)

    print(str(denominators_product / math.gcd(numerators_product, denominators_product)))


# better solution
def solution():
    dp = 1
    np = 1

    for c in range(1, 10):
        for d in range(1, c):
            for n in range(1, d):
                if ((n * 10 + c) * d) == ((c * 10 + d) * n):
                    np *= n
                    dp *= d

    result = int(dp / math.gcd(np, dp))
    print(result)
    return result


def main():
    start = time.time()

    solution()

    end = time.time()
    print('Seconds: ' + str((end - start) * 1000))

    start = time.time()

    digit_cancelling_fractions()

    end = time.time()
    print('Milliseconds: ' + str((end - start) * 1000))


main()
