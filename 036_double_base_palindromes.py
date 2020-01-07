# The decimal number, 585 = 1001001001 (binary), is palindromic in both bases.
#
# Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.
#
# (Please note that the palindromic number, in either base, may not include leading zeros.)

import time


def is_palindrome(number_as_string: str):
    return number_as_string == number_as_string[::-1]


def get_number_as_binary_string(num: int):
    return '{0:b}'.format(num)


def sum_of_double_base_palindromes():
    result = 0
    for num in range(1, 1000000):
        if is_palindrome(str(num)) and is_palindrome(get_number_as_binary_string(num)):
            result += num
    return result


def main():
    start = time.time()

    print(sum_of_double_base_palindromes())

    end = time.time()
    print('Seconds: ' + (str(end - start)))


main()
