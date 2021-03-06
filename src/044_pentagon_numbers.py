# Pentagonal numbers are generated by the formula, Pn = n(3n − 1) / 2

# The first ten pentagonal numbers are:
# 1, 5, 12, 22, 35, 51, 70, 92, 117, 145, ...
#
# It can be seen that P4 + P7 = 22 + 70 = 92 = P8.
# However, their difference, 70 − 22 = 48, is not pentagonal.
#
# Find the pair of pentagonal numbers, Pj and Pk, for which their sum and difference are pentagonal and D = |Pk − Pj| is minimised;
# what is the value of D?

import time
from common_functions import is_pentagonal


def pentagon_numbers() -> int:
    n = 2
    pk = 1
    pentagonals: set = {1}

    while True:
        for pj in pentagonals:
            if pk - pj in pentagonals and is_pentagonal(pk + pj):
                return pk - pj

        pentagonals.add(pk)
        pk += 3 * n - 2
        n += 1


def main():
    start = time.time()

    print('result:', pentagon_numbers())

    end = time.time()
    print('Seconds: ' + str(end - start))


if __name__ == '__main__':
    main()
else:
    print('__name__ is', __name__)


# def get_list_of_pentagonal_numbers(length: int):
#     pentagonal_list = []
#
#     for n in range(1, length + 1):
#         pentagonal_list.append(int((n * ((3 * n) - 1)) / 2))
#
#     return pentagonal_list
#
#
# def is_sum_and_diff_are_pentagonal(pentagonal_1: int, pentagonal_2: int, pentagonal_list: list):
#     return ((pentagonal_1 + pentagonal_2) in pentagonal_list) and ((pentagonal_1 - pentagonal_2) in pentagonal_list)
#
#
# def pentagon_numbers():
#     pentagonal_list = get_list_of_pentagonal_numbers(2000)
#     for i in pentagonal_list:
#         for j in pentagonal_list:
#             if is_sum_and_diff_are_pentagonal(i, j, pentagonal_list):
#                 print('i: ' + str(i))
#                 print('j: ' + str(j))
#     return True
