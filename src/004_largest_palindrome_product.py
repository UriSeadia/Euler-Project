# A palindromic number reads the same both ways.
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

import time


def is_palindrome(string: str):
    return string == string[::-1]


def check_palindromes():
    max_palindrome = 0
    three_digit_number_a = 100
    three_digit_number_b = 100

    while three_digit_number_a <= 999:
        while three_digit_number_b <= 999:
            number_to_check = three_digit_number_a * three_digit_number_b

            if is_palindrome(str(number_to_check)) and max_palindrome < number_to_check:
                max_palindrome = number_to_check
                # print(max_palindrome, '=', three_digit_number_a, '*', three_digit_number_b)

            three_digit_number_b += 1

        three_digit_number_b = 100
        three_digit_number_a += 1

    return max_palindrome


def main():
    start = time.time()

    print('result:', check_palindromes())

    end = time.time()
    print('Milliseconds: ' + str((end - start) * 1000))


main()
