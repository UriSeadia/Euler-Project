# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10,001st prime number?

import time


def is_prime(number):

    if number <= 1:
        # print('False: number <= 1')
        return False

    if number <= 3:
        # print('True: number between 1 and 3')
        return True

    if number % 2 == 0 or number % 3 == 0:
        # print('False:', number, 'is divisible by 2 or 3')
        return False

    i = 5
    while i * i <= number:
        if (number % i == 0) or (number % (i + 2) == 0):
            # print('False:', number, 'is divisible by', i, 'or', i + 2)
            return False
        i = i + 6

    # print(number, 'is prime')
    return True


def get_number_prime(number):
    number_to_check = 3
    counter = 1
    result = 0

    while counter < number:
        if is_prime(number_to_check):
            counter += 1
            result = number_to_check

        number_to_check += 2

    return result


def main():
    start = time.time()

    print('result:', get_number_prime(10001))

    end = time.time()
    print('milliseconds: ' + (str((end - start) * 1000)))


main()
