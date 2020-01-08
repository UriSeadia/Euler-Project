# The prime 41, can be written as the sum of six consecutive primes:
# 41 = 2 + 3 + 5 + 7 + 11 + 13
#
# This is the longest sum of consecutive primes that adds to a prime below 100.
# The longest sum of consecutive primes below 1000 that adds to a prime, contains 21 terms, and is equal to 953.
#
# Which prime, below 1000000, can be written as the sum of the most consecutive primes?

import time


def is_prime(number: int) -> bool:
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


def get_primes_list(from_number: int, to_number: int) -> list:
    list_of_primes = []
    for i in range(from_number, to_number + 1):
        if is_prime(i):
            list_of_primes.append(i)
    return list_of_primes


def longest_prime_sum(limit):
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

    print('result:', longest_prime_sum(1000000))

    end = time.time()
    print('Seconds: ' + str(end - start))


if __name__ == '__main__':
    main()
else:
    print('__name__ is', __name__)
