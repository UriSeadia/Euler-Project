# If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.
#
# {20,48,52}, {24,45,51}, {30,40,50}
#
# For which value of p ≤ 1000, is the number of solutions maximised?

import time


def count_solutions(p=120):
    count = 0

    for i in range(1, p // 3):
        for j in range(p // 3, p // 2):
            if (i ** 2) + (j ** 2) == ((p - i - j) ** 2):
                count += 1
    return count


def integer_right_triangle():
    max_count = 0
    result = 0

    for num in range(10, 1001):
        max_candidate = count_solutions(num)
        if max_candidate > max_count:
            max_count = max_candidate
            result = num

    return result


def main():
    start = time.time()

    print(integer_right_triangle())

    end = time.time()
    print('Seconds: ' + str(end - start))


main()
