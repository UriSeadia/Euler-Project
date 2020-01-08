# An irrational decimal fraction is created by concatenating the positive integers:
# 0.12345678910 11 12 131415161718192021...
#
# It can be seen that the 12th digit of the fractional part is 1.
#
# If dn represents the nth digit of the fractional part, find the value of the following expression.
#
# d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000

import time


def champernownes_constant():
    initial_string = ''
    result = 1

    for i in range(1, 186000):
        initial_string += str(i)

    for d in {1, 10, 100, 1000, 10000, 100000, 1000000}:
        result *= int(initial_string[d - 1])

    return result


def main():
    start = time.time()

    print(champernownes_constant())

    end = time.time()
    print('Seconds: ' + str(end - start))


main()
