# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# a ^ 2 + b ^ 2 = c ^ 2
#
# For example: 3 ^ 2 + 4 ^ 2 = 9 + 16 = 25 = 5 ^ 2.
#
# There exists exactly one Pythagorean triplet for which a + b + c = 1000. Find the product abc.

import time


def is_pythagorean(a: int, b: int, c: int):
    return (a ** 2 + b ** 2) == c ** 2


def find_special_pythagorean():
    a = 1
    b = 1
    is_special_pythagorean = False

    while a < 332:
        while a + b <= 666:
            c = 1000 - a - b
            is_special_pythagorean = is_pythagorean(a, b, c)

            if is_special_pythagorean:
                break

            b += 1

        if is_special_pythagorean:
            break

        a += 1
        b = a

    print('a:', a, ', b:', b, ', c:', c)
    print(a ** 2, '+', b ** 2, '=', c ** 2)
    print('Product abc:', a * b * c)
    return a * b * c


def main():
    start = time.time()

    print('result:', find_special_pythagorean())

    end = time.time()
    print('milliseconds: ' + (str((end - start) * 1000)))


main()
