# The number 3797 has an interesting property.
# Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7.
# Similarly we can work from right to left: 3797, 379, 37, and 3.
#
# Find the sum of the only 11 primes that are both truncatable from left to right and right to left.
#
# NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.

import time


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


def find_sum_of_truncatable_primes():
    sum_of_primes = 0
    count = 0
    num = 11

    while count < 11:
        if is_prime(num):
            number_of_digits = len(str(num))
            num_1 = num
            num_2 = num
            i = number_of_digits - 1
            while num_1 > 0:
                num_1 = num_1 // 10
                num_2 = num_2 % (10 ** i)
                i -= 1
                if is_prime(num_1) and is_prime(num_2):
                    continue
                else:
                    break

            if num_1 == 0:
                count += 1
                print(num)
                sum_of_primes += num
        num += 1

    return sum_of_primes


def main():
    start = time.time()

    print(find_sum_of_truncatable_primes())

    end = time.time()
    print('Seconds: ' + str(end - start))


main()
