# The Fibonacci sequence is defined by the recurrence relation:
#
# Fn = (Fn − 1) + (Fn − 2), where F1 = 1 and F2 = 1.
#
# Hence the first 12 terms will be:
# F1 = 1
# F2 = 1
# F3 = 2
# F4 = 3
# F5 = 5
# F6 = 8
# F7 = 13
# F8 = 21
# F9 = 34
# F10 = 55
# F11 = 89
# F12 = 144
# The 12th term, F12, is the first term to contain three digits.
#
# What is the index of the first term in the Fibonacci sequence to contain 1000 digits?


import functools


@functools.lru_cache(None)
def get_fibonacci(num):
    if num < 2:
        return num
    return get_fibonacci(num - 1) + get_fibonacci(num - 2)


def get_index_of_first_1000_digits_fibonacci():
    number_of_digits = 0
    i = 1

    while number_of_digits < 1000:
        fibonacci_result = get_fibonacci(i)
        number_of_digits = len(str(fibonacci_result))
        # print("index:", i, "| digits:", number_of_digits, "| number:", fibonacci_result)
        i += 1


get_index_of_first_1000_digits_fibonacci()
