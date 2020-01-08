# We shall say that an n-digit number is pan-digital if it makes use of all the digits 1 to n exactly once.
# For example, 2143 is a 4-digit pan-digital and is also prime.
#
# What is the largest n-digit pan-digital prime that exists?

import time
import itertools


def is_pan_digital(num_as_str: str):
    set_of_str = set(num_as_str)

    return ('0' not in set_of_str) and (len(set_of_str) == 9)


def is_prime(number: int):

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


def get_list_of_permutations(s: str):
    return sorted(["".join(perm) for perm in itertools.permutations(s)], reverse=True)


def pan_digital_prime():
    num_as_str = '987654321'

    while num_as_str:
        list_of_perm = get_list_of_permutations(num_as_str)
        for num in list_of_perm:
            if is_prime(int(num)):
                return num

        num_as_str = num_as_str.replace(num_as_str[0], "")


def main():
    start = time.time()

    print(pan_digital_prime())

    end = time.time()
    print('Seconds: ' + str(end - start))


main()
