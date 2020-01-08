# The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways:
#   1. each of the three terms are prime
#   2. each of the 4-digit numbers are permutations of one another.
#
# There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property,
# but there is one other 4-digit increasing sequence.
#
# What 12-digit number do you form by concatenating the three terms in this sequence?

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


def is_permutation(a: int, b: int) -> bool:
    return ''.join(sorted(str(a))) == ''.join(sorted(str(b)))


def solution() -> str:
    primes: list = get_primes_list(1000, 9999)

    for i in range(0, len(primes)):
        for j in range(i + 1, len(primes)):
            if is_permutation(primes[i], primes[j]):
                diff = primes[j] - primes[i]
                if (primes[j] + diff) in primes and is_permutation(primes[j], primes[j] + diff):
                    if not primes[i] == 1487:
                        return str(primes[i]) + str(primes[j]) + str(primes[j] + diff)


def main():
    start = time.time()

    print('result:', solution())

    end = time.time()
    print('Seconds: ' + str(end - start))


if __name__ == '__main__':
    main()
else:
    print('__name__ is', __name__)
