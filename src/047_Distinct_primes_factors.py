# The first two consecutive numbers to have two distinct prime factors are:
# 14 = 2 × 7
# 15 = 3 × 5
#
# The first three consecutive numbers to have three distinct prime factors are:
# 644 = 2² × 7 × 23
# 645 = 3 × 5 × 43
# 646 = 2 × 17 × 19.
#
# Find the first four consecutive integers to have four distinct prime factors each.
# What is the first of these numbers?

import time


def number_of_distinct_prime_factors(num):
    prime_factors = set()
    while num % 2 == 0:
        prime_factors.add(2)
        num /= 2
    for i in range(3, int(num ** 0.5) + 1, 2):
        while num % i == 0:
            prime_factors.add(i)
            num /= i
    if num > 1:
        prime_factors.add(num)
    return len(prime_factors)


def solution():
    num = 1
    while True:
        if number_of_distinct_prime_factors(num) == 4:
            if number_of_distinct_prime_factors(num + 3) == 4:
                if number_of_distinct_prime_factors(num + 2) == 4:
                    if number_of_distinct_prime_factors(num + 1) == 4:
                        return num
                    else:
                        num += 2
                else:
                    num += 3
            else:
                num = num + 4 if number_of_distinct_prime_factors(num + 8) == 4 else num + 9
        else:
            num = num + 1 if number_of_distinct_prime_factors(num + 4) == 4 else num + 6


def main():
    start = time.time()

    print('result:', solution())

    end = time.time()
    print('Seconds: ' + str(end - start))


if __name__ == '__main__':
    main()
else:
    print('__name__ is', __name__)


# def is_prime(number: int) -> bool:
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
# def count_4_primes(num, primes):
#     count = 0
#     i = 0
#     while count < 4 and i < len(primes):
#         if num % primes[i] == 0:
#             count += 1
#         i += 1
#     return count == 4
#
#
# def solution():
#     first_num = 644
#     primes = sorted(set(i for i in range(1, 10000) if is_prime(i)))
#
#     while True:
#         num = first_num
#
#         while count_4_primes(num, primes):
#             num += 1
#
#         if num - first_num > 3:
#             return first_num
#         first_num += 1
