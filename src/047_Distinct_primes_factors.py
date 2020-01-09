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


def number_of_distinct_prime_factors(num: int) -> int:
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


def distinct_primes_factors() -> int:
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

    print('result:', distinct_primes_factors())

    end = time.time()
    print('Seconds: ' + str(end - start))


if __name__ == '__main__':
    main()
else:
    print('__name__ is', __name__)
