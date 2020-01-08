# It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.
#
# 9  = 7  + 2 * 1 ** 2
# 15 = 7  + 2 * 2 ** 2
# 21 = 3  + 2 * 3 ** 2
# 25 = 7  + 2 * 3 ** 2
# 27 = 19 + 2 * 2 ** 2
# 33 = 31 + 2 * 1 ** 2
#
# It turns out that the conjecture was false.
#
# What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?

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


def solution():
    primes = [2]
    squares = [2]
    num_to_square = 1
    num = 1

    while True:
        num += 2

        # if num is prime number ---> add it to the primes list and continue
        if is_prime(num):
            primes.append(num)
            continue

        # if the last squares < num ---> increase num_to_square & add (2 * num_to_square^2) to squares
        if squares[len(squares) - 1] < num:
            num_to_square += 1
            squares.append(2 * num_to_square ** 2)

        # initiate primes_index to last item of primes & squares_index to 0
        primes_index = len(primes) - 1
        squares_index = 0

        while True:
            # run on squares until end or equation >= num
            while squares_index < len(squares) and primes[primes_index] + squares[squares_index] < num:
                squares_index += 1

            # break the loop if found that the condition is not fulfilled
            if primes[primes_index] + squares[squares_index] == num:
                break

            # start again with primes_index - 1
            primes_index -= 1
            squares_index = 0

            # if not found primes_index - num found!
            if primes_index == 0:
                return num


def main():
    start = time.time()

    print('result:', solution())

    end = time.time()
    print('Seconds: ' + str(end - start))


if __name__ == '__main__':
    main()
else:
    print('__name__ is', __name__)

# def get_list_of_primes() -> list:
#     list_of_primes = [1]
#     for i in range(1, 10000):
#         if is_prime(i):
#             list_of_primes.append(i)
#     return list_of_primes
#
#
# def get_list_of_composites() -> list:
#     list_of_composites = []
#     for i in range(9, 10000, 2):
#         if not is_prime(i):
#             list_of_composites.append(i)
#     return list_of_composites
#
#
# def solution():
#     composites = get_list_of_composites()
#     primes = get_list_of_primes()
#
#     for comp in composites:
#         to_check = 0
#         for prime in primes:
#             for i in range(0, 1000):
#                 to_check = prime + 2 * (i ** 2)
#                 if comp == to_check:
#                     break
#             if comp == to_check:
#                 break
#         if not comp == to_check:
#             return comp
