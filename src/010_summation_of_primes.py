# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

import time


def summation_of_primes(max_number: int):
    primes = [True] * max_number
    result = 0

    for i in range(2, max_number):
        if primes[i]:
            result += i

            for j in range(2 * i, max_number, i):
                primes[j] = False

    return result


def main():
    start = time.time()

    print(summation_of_primes(2000000))

    end = time.time()
    print('seconds: ' + (str((end - start))))


main()

# def is_prime(number: int):
#
#     if number <= 1:
#         return False
#
#     if number <= 3:
#         return True
#
#     if number % 2 == 0 or number % 3 == 0:
#         return False
#
#     i = 5
#     while i * i <= number:
#         if (number % i == 0) or (number % (i + 2) == 0):
#             return False
#         i = i + 6
#
#     return True
#
#
# def summation_of_primes(max_number: int):
#     result = 0
#     number_to_check = 2
#
#     while number_to_check < max_number:
#         if is_prime(number_to_check):
#             result += number_to_check
#         number_to_check += 1
#
#     return result
