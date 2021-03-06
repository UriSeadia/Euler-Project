# The series, 1 ^ 1 + 2 ^ 2 + 3 ^ 3 + ... + 10 ^ 10 = 10405071317.
#
# Find the last 10 digits of the series, 1 ^ 1 + 2 ^ 2 + 3 ^ 3 + ... + 1000 ^ 1000.


import time


def self_powers(last_num: int) -> str:
    result = 0

    for i in range(1, last_num + 1):
        result += i ** i

    str_result = str(result)

    return str_result[len(str_result) - 10: len(str_result)]


def main():
    start = time.time()

    last_num = 1000
    print('result:', self_powers(last_num))

    end = time.time()
    print('Seconds: ' + str(end - start))


if __name__ == '__main__':
    main()
else:
    print('__name__ is', __name__)
