# The number, 1406357289, is a 0 to 9 pan-digital number because it is made up of each of the digits 0 to 9 in some order,
# but it also has a rather interesting sub-string divisibility property.
#
# Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:
#
# d2d3d4 = 406 is divisible by 2
# d3d4d5 = 063 is divisible by 3
# d4d5d6 = 635 is divisible by 5
# d5d6d7 = 357 is divisible by 7
# d6d7d8 = 572 is divisible by 11
# d7d8d9 = 728 is divisible by 13
# d8d9d10 = 289 is divisible by 17

# Find the sum of all 0 to 9 pan-digital numbers with this property.

import time
import itertools


def get_list_of_permutations(s: str):
    return sorted(["".join(perm) for perm in itertools.permutations(s)], reverse=True)


def is_number_divisible(num: int, divisor: int):
    return num % divisor == 0


def substring_divisibility():
    result = 0
    list_of_perm = get_list_of_permutations('0123456789')
    list_of_divisors = [2, 3, 5, 7, 11, 13, 17]

    for num in list_of_perm:
        for i in range(1, 8):
            if not (is_number_divisible(int(num[i: i + 3]), list_of_divisors[i - 1])):
                num = 0
                break
        result += int(num)

    return result


def main():
    start = time.time()

    print(substring_divisibility())

    end = time.time()
    print('Seconds: ' + str(end - start))


main()
