# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143?

import time


def get_prime_factors(number: int):
    prime_factor = 2
    largest_prime_factor = 1

    while number > 1:
        if number % prime_factor == 0:
            number /= prime_factor

            if largest_prime_factor < prime_factor:
                largest_prime_factor = prime_factor
        else:
            prime_factor += 1

    return largest_prime_factor


def main():
    start = time.time()

    print('result:', get_prime_factors(600851475143))

    end = time.time()
    print('Milliseconds: ' + str((end - start) * 1000))


main()
