# The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.
#
# There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.
#
# How many circular primes are there below one million?

import time


def has_same_digits(a, b):
    return sorted(list(str(a))) == sorted(list(str(b)))


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


def count_circular_primes():
    count = 0

    for num in range(2, 1000000):
        if is_prime(num):
            number_of_digits = len(str(num))
            circular_num = num

            for i in range(0, number_of_digits):
                circular_num = ((circular_num % 10) * (10 ** (number_of_digits - 1))) + (circular_num // 10)

                if not is_prime(circular_num):
                    break
                if i == number_of_digits - 1:
                    count += 1
    return count


def main():
    start = time.time()

    print(count_circular_primes())

    end = time.time()
    print('Seconds: ' + str(end - start))


main()
