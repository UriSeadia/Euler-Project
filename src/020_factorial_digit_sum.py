# n! means n × (n − 1) × ... × 3 × 2 × 1
#
# For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800

# The sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
#
# Find the sum of the digits in the number 100!


def get_factorial(num):
    if num == 1:
        return num
    return num * get_factorial(num - 1)


def get_sum_of_digits_in_factorial(num):
    result = 0
    factorial = get_factorial(num)
    num_as_string = str(factorial)

    for char in num_as_string:
        digit = int(char)
        result += digit

    print(result)
    return result


get_sum_of_digits_in_factorial(100)
