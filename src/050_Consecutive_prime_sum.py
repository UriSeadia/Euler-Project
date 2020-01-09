# The prime 41, can be written as the sum of six consecutive primes:
# 41 = 2 + 3 + 5 + 7 + 11 + 13
#
# This is the longest sum of consecutive primes that adds to a prime below 100.
# The longest sum of consecutive primes below 1000 that adds to a prime, contains 21 terms, and is equal to 953.
#
# Which prime, below 1000000, can be written as the sum of the most consecutive primes?

import time
from common_functions import is_prime, get_primes_list


def consecutive_primes_sum(limit: int) -> int:
    prime_list = get_primes_list(2, limit)
    total = 0

    for max_length, p in enumerate(prime_list):
        total += p
        if total >= limit:
            break

    for length in range(max_length + 1, 0, -1):
        for x in range(len(prime_list) - length + 1):
            total = sum(prime_list[x:x+length])
            if total >= limit:
                break
            elif total in prime_list:
                return total


def main():
    start = time.time()

    limit = 1000000
    print('result:', consecutive_primes_sum(limit))

    end = time.time()
    print('Seconds: ' + str(end - start))


if __name__ == '__main__':
    main()
else:
    print('__name__ is', __name__)
